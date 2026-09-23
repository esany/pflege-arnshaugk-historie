"""Deterministic checks for bounded, model-agnostic execution work orders."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
import re


@dataclass(frozen=True)
class ExecutionFinding:
    rule_id: str
    severity: str
    message: str


_REQUIRED = ("schema_version", "work_order_ref", "work_owner_ref", "primary_function", "causal_driver_slice", "authority", "accepted_requirements", "scope", "minimal_context", "tests", "stop_handoff_when", "persistence_target", "return_contract", "non_goals")
_MODEL_FIELDS = {"model", "model_name", "provider", "provider_name", "token_budget", "reasoning_effort", "temperature"}
_REQ_RE = re.compile(r"\bREQ-[A-Z0-9-]+\b")
_BROAD_CONTEXT = {"entire repository", "all repository files", "all issues", "all source files"}


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(_text(item) for item in value)


def _finding(rule_id: str, message: str) -> ExecutionFinding:
    return ExecutionFinding(rule_id, "error", message)


def _all_keys(value: Any) -> set[str]:
    if isinstance(value, dict):
        keys = set(value)
        for child in value.values():
            keys |= _all_keys(child)
        for child in value.values():
            if isinstance(child, list):
                for item in child:
                    keys |= _all_keys(item)
        return keys
    return set()


def _canonical_requirement_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    for relative in ("docs/research/synthesis/requirements-baseline.md", "docs/research/synthesis/requirements-extensions.md"):
        path = root / relative
        if path.exists():
            ids.update(_REQ_RE.findall(path.read_text(encoding="utf-8")))
    return ids


def _safe_relative(path: Any) -> bool:
    if not _text(path):
        return False
    candidate = PurePosixPath(path)
    return not candidate.is_absolute() and ".." not in candidate.parts


def validate_execution_order(data: dict[str, Any], *, root: str | Path) -> list[ExecutionFinding]:
    root_path = Path(root)
    findings: list[ExecutionFinding] = []
    missing = [key for key in _REQUIRED if key not in data]
    if missing:
        findings.append(_finding("EXEC001", f"missing required fields: {', '.join(missing)}"))
        return findings
    if data.get("schema_version") != "0.1":
        findings.append(_finding("EXEC001", "unsupported execution-order schema_version"))
    unknown_model_fields = sorted(_MODEL_FIELDS & _all_keys(data))
    if unknown_model_fields:
        findings.append(_finding("EXEC002", f"model/provider-specific fields are forbidden: {', '.join(unknown_model_fields)}"))
    drivers = data["causal_driver_slice"]
    if not isinstance(drivers, dict) or not any(_strings(drivers.get(key)) for key in ("goal_refs", "need_refs", "pain_refs")):
        findings.append(_finding("EXEC003", "causal_driver_slice needs at least one non-empty goal, need, or pain reference"))
    authority = data["authority"]
    if not isinstance(authority, dict) or authority.get("work_owner_ref") != data["work_owner_ref"]:
        findings.append(_finding("EXEC004", "authority.work_owner_ref must equal work_owner_ref"))
    elif not _strings(authority.get("semantic_authority_refs")) or not _strings(authority.get("acceptance_authority_refs")):
        findings.append(_finding("EXEC004", "semantic and acceptance authority references are required"))
    accepted = data["accepted_requirements"]
    known_requirements = _canonical_requirement_ids(root_path)
    if not isinstance(accepted, list) or not accepted:
        findings.append(_finding("EXEC005", "accepted_requirements must not be empty"))
    else:
        for index, item in enumerate(accepted):
            if not isinstance(item, dict) or not _text(item.get("id")):
                findings.append(_finding("EXEC005", f"accepted_requirements[{index}] needs an id"))
                continue
            if known_requirements and item["id"] not in known_requirements:
                findings.append(_finding("EXEC005", f"unknown accepted requirement: {item['id']}"))
            if not _strings(item.get("acceptance_refs")) or not _strings(item.get("verification_refs")):
                findings.append(_finding("EXEC006", f"{item['id']} needs acceptance_refs and verification_refs"))
    scope = data["scope"]
    included = scope.get("included_files") if isinstance(scope, dict) else None
    if not isinstance(included, list) or not included:
        findings.append(_finding("EXEC007", "scope.included_files must be a non-empty exact file list"))
    else:
        for index, item in enumerate(included):
            path = item.get("path") if isinstance(item, dict) else None
            if not _safe_relative(path):
                findings.append(_finding("EXEC007", f"scope.included_files[{index}] needs a safe relative path"))
                continue
            if path.startswith("sources/") or path == "sources":
                findings.append(_finding("EXEC007", "sources/ is read-only and cannot be an execution target"))
            if not (root_path / path).is_file():
                findings.append(_finding("EXEC007", f"exact execution file does not exist: {path}"))
            if not _text(item.get("purpose")) or not _text(item.get("allowed_change")):
                findings.append(_finding("EXEC008", f"scope entry {path} needs purpose and allowed_change"))
    context = data["minimal_context"]
    if not isinstance(context, dict) or not isinstance(context.get("required_refs"), list) or not context["required_refs"]:
        findings.append(_finding("EXEC009", "minimal_context.required_refs must be non-empty"))
    else:
        max_refs = context.get("max_refs")
        if not isinstance(max_refs, int) or max_refs < 1 or len(context["required_refs"]) > max_refs:
            findings.append(_finding("EXEC009", "minimal_context exceeds its declared max_refs"))
        for item in context["required_refs"]:
            if not isinstance(item, dict) or not _text(item.get("ref")) or not _text(item.get("why")):
                findings.append(_finding("EXEC009", "each required context ref needs ref and why"))
            elif item["ref"].strip().lower() in _BROAD_CONTEXT:
                findings.append(_finding("EXEC009", "broad, non-minimal context is forbidden"))
    tests = data["tests"]
    kinds: set[str] = set()
    if not isinstance(tests, list) or not tests:
        findings.append(_finding("EXEC010", "tests must be non-empty"))
    else:
        for index, item in enumerate(tests):
            if not isinstance(item, dict) or not _text(item.get("ref")) or not _text(item.get("purpose")) or not _text(item.get("kind")):
                findings.append(_finding("EXEC010", f"tests[{index}] needs ref, purpose, and kind"))
            elif item["kind"] in {"positive", "negative"}:
                kinds.add(item["kind"])
        if kinds != {"positive", "negative"}:
            findings.append(_finding("EXEC011", "tests must include both positive and negative checks"))
    if not _strings(data["stop_handoff_when"]):
        findings.append(_finding("EXEC012", "stop_handoff_when must be non-empty"))
    if not _text(data["persistence_target"]):
        findings.append(_finding("EXEC012", "persistence_target is required"))
    contract = data["return_contract"]
    required_return = {"delta", "verification", "open_points", "handoff"}
    required_handoff = {"from", "to", "trigger", "established", "unresolved", "request", "acceptance", "persistence_target"}
    if not isinstance(contract, dict) or contract.get("format") != "delta-only":
        findings.append(_finding("EXEC013", "return_contract.format must be delta-only"))
    else:
        if set(contract.get("required_fields", [])) != required_return:
            findings.append(_finding("EXEC013", "delta-only return must require exactly delta, verification, open_points, handoff"))
        if set(contract.get("handoff_fields", [])) != required_handoff:
            findings.append(_finding("EXEC014", "handoff fields are incomplete; restartability state would be lost"))
    non_goals = " ".join(data["non_goals"]) if isinstance(data["non_goals"], list) else ""
    if "multi-agent" not in non_goals.lower() or "workflow" not in non_goals.lower():
        findings.append(_finding("EXEC015", "non_goals must explicitly exclude product multi-agent/workflow architecture"))
    return findings


def check_changed_files(order: dict[str, Any], changed_files: Iterable[str]) -> list[ExecutionFinding]:
    scope = order.get("scope", {})
    allowed = {item.get("path") for item in scope.get("included_files", []) if isinstance(item, dict)}
    outside = sorted(set(changed_files) - allowed)
    return [_finding("EXEC016", f"scope drift outside exact file list: {', '.join(outside)}")] if outside else []


def load_execution_order(path: str | Path, *, root: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("execution order must be a JSON object")
    findings = validate_execution_order(data, root=root)
    if findings:
        raise ValueError("invalid execution order: " + "; ".join(item.message for item in findings))
    return data
