"""Minimal canonical identity/owner/reference spine for admitted WP1.

The spine owns only stable internal IDs, settled roles and references to existing
canonical owners. It does not copy research statements, source metadata,
reviewed locator geometry, task truth, method truth or promotion state.

The current resolver is deliberately bounded to the real #51/#46 -> #55 audit
roundtrip admitted by WP1-STATE-SPINE-V0. Derived audit state is reconstructed
read-only from the registry plus the referenced canonical owners.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
import re
from typing import Any

from tools.operational.core import (
    OperationalError,
    load_json,
    read_text,
    repo_root_from,
    schema_violations,
)


class ResearchStateError(ValueError):
    """The admitted identity/reference spine cannot be resolved safely."""


REGISTRY_RELATIVE_PATH = Path("tools/research_state/data/records.json")
SCHEMA_PATH = Path(__file__).with_name("registry.schema.json")

ROLE_SELECTORS = {
    "source": "heading",
    "representation": "representation_id",
    "instance": "instance_id",
    "findspot": "locator_id",
    "finding": "heading",
}


def repo_root() -> Path:
    return repo_root_from(__file__)


def _schema() -> dict[str, Any]:
    try:
        data = load_json(SCHEMA_PATH)
    except OperationalError as exc:
        raise ResearchStateError(str(exc)) from exc
    if not isinstance(data, dict):
        raise ResearchStateError("research-state registry schema must be an object")
    return data


def _split_canonical_ref(canonical_ref: str) -> tuple[Path, str, str]:
    if "#" not in canonical_ref:
        raise ResearchStateError(f"canonical_ref lacks selector fragment: {canonical_ref}")
    path_text, fragment = canonical_ref.split("#", 1)
    if "=" not in fragment:
        raise ResearchStateError(f"canonical_ref selector must be key=value: {canonical_ref}")
    selector, value = fragment.split("=", 1)
    if not path_text or not selector or not value:
        raise ResearchStateError(f"canonical_ref is incomplete: {canonical_ref}")

    relative = Path(path_text)
    if relative.is_absolute() or ".." in relative.parts:
        raise ResearchStateError(f"canonical_ref must stay inside repository: {canonical_ref}")
    return relative, selector, value


def _safe_target(root: Path, relative: Path) -> Path:
    root_resolved = root.resolve()
    target = (root_resolved / relative).resolve()
    try:
        target.relative_to(root_resolved)
    except ValueError as exc:
        raise ResearchStateError(f"canonical_ref escapes repository: {relative}") from exc
    return target


def _internal_id(record_id: str) -> None:
    if "://" in record_id or "/" in record_id or "\\" in record_id:
        raise ResearchStateError(f"internal id must not be a provider URL/path: {record_id}")


def _markdown_section(text: str, heading_id: str) -> str:
    pattern = re.compile(
        rf"^(?P<marks>#{{2,6}})\s+{re.escape(heading_id)}(?:\s+[–—-]\s+.*)?\s*$",
        re.MULTILINE,
    )
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise ResearchStateError(
            f"canonical markdown heading {heading_id} resolved {len(matches)} times"
        )

    match = matches[0]
    level = len(match.group("marks"))
    next_heading = re.compile(rf"^#{{1,{level}}}\s+", re.MULTILINE).search(text, match.end())
    end = next_heading.start() if next_heading else len(text)
    return text[match.start():end].rstrip() + "\n"


def _json_matches(value: Any, selector: str, expected: str) -> list[Mapping[str, Any]]:
    matches: list[Mapping[str, Any]] = []

    def walk(item: Any) -> None:
        if isinstance(item, Mapping):
            if item.get(selector) == expected:
                matches.append(item)
            for child in item.values():
                walk(child)
        elif isinstance(item, list):
            for child in item:
                walk(child)

    walk(value)
    return matches


def resolve_record(root: Path, record: Mapping[str, Any]) -> dict[str, Any]:
    record_id = record.get("id")
    role = record.get("role")
    canonical_ref = record.get("canonical_ref")
    if not isinstance(record_id, str) or not isinstance(role, str) or not isinstance(canonical_ref, str):
        raise ResearchStateError("registry record is missing id/role/canonical_ref")

    _internal_id(record_id)
    relative, selector, value = _split_canonical_ref(canonical_ref)
    expected_selector = ROLE_SELECTORS.get(role)
    if expected_selector is None:
        raise ResearchStateError(f"unsupported research-state role: {role}")
    if selector != expected_selector:
        raise ResearchStateError(
            f"{record_id} role {role} requires selector {expected_selector}, got {selector}"
        )
    if value != record_id:
        raise ResearchStateError(
            f"{record_id} canonical_ref targets different identity {value}"
        )

    target_path = _safe_target(root, relative)
    try:
        if selector == "heading":
            text = read_text(target_path)
            section = _markdown_section(text, record_id)
            return {
                "path": target_path,
                "kind": "markdown",
                "section": section,
                "document": text,
            }

        document = load_json(target_path)
    except OperationalError as exc:
        raise ResearchStateError(str(exc)) from exc

    matches = _json_matches(document, selector, record_id)
    if len(matches) != 1:
        raise ResearchStateError(
            f"{record_id} canonical JSON selector resolved {len(matches)} times"
        )
    return {
        "path": target_path,
        "kind": "json",
        "target": matches[0],
        "document": document,
    }


def validate_registry_data(root: Path, data: Any) -> None:
    violations = schema_violations(_schema(), data)
    if violations:
        details = "; ".join(
            f"{item.location}: {item.message}" for item in violations
        )
        raise ResearchStateError(f"research-state registry schema violation: {details}")

    records = data["records"]
    seen: set[str] = set()
    for record in records:
        record_id = record["id"]
        if record_id in seen:
            raise ResearchStateError(f"duplicate research-state id: {record_id}")
        seen.add(record_id)
        resolve_record(root, record)


def load_registry(root: Path | None = None) -> dict[str, Any]:
    root = root or repo_root()
    try:
        data = load_json(root / REGISTRY_RELATIVE_PATH)
    except OperationalError as exc:
        raise ResearchStateError(str(exc)) from exc
    validate_registry_data(root, data)
    return data


def _index_registry(data: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {record["id"]: record for record in data["records"]}


def _record(
    index: Mapping[str, Mapping[str, Any]],
    record_id: str,
    role: str,
) -> Mapping[str, Any]:
    record = index.get(record_id)
    if record is None:
        raise ResearchStateError(f"research-state id is not registered: {record_id}")
    if record.get("role") != role:
        raise ResearchStateError(
            f"research-state id {record_id} has role {record.get('role')}, expected {role}"
        )
    return record


def _field(section: str, label: str) -> str | None:
    pattern = re.compile(
        rf"^\s*(?:-\s+)?\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$",
        re.MULTILINE,
    )
    match = pattern.search(section)
    return match.group(1).strip() if match else None


def _heading_label(section: str, record_id: str) -> str | None:
    first = section.splitlines()[0] if section.splitlines() else ""
    match = re.match(
        rf"^#{{2,6}}\s+{re.escape(record_id)}\s+[–—-]\s+(.+?)\s*$",
        first,
    )
    return match.group(1).strip() if match else None


def _case_for_locator(document: Mapping[str, Any], locator_id: str) -> Mapping[str, Any]:
    cases = []
    for case in document.get("reference_cases", []):
        if not isinstance(case, Mapping):
            continue
        if any(
            isinstance(locator, Mapping) and locator.get("locator_id") == locator_id
            for locator in case.get("locators", [])
        ):
            cases.append(case)
    if len(cases) != 1:
        raise ResearchStateError(
            f"locator {locator_id} belongs to {len(cases)} reference cases"
        )
    return cases[0]


def _manifest_finding(document: Mapping[str, Any], finding_id: str) -> Mapping[str, Any]:
    matches = [
        finding
        for finding in document.get("findings", [])
        if isinstance(finding, Mapping) and finding.get("finding_id") == finding_id
    ]
    if len(matches) != 1:
        raise ResearchStateError(
            f"manifest finding {finding_id} resolved {len(matches)} times"
        )
    return matches[0]


def _findspot_text(locator: Mapping[str, Any]) -> str:
    parts: list[str] = []
    printed = locator.get("printed_page")
    if isinstance(printed, Mapping):
        if printed.get("status") == "resolved" and printed.get("label"):
            parts.append(f"print p. {printed['label']}")
        elif printed.get("status"):
            parts.append(f"print page {printed['status']}")

    if isinstance(locator.get("pdf_page_index"), int):
        parts.append(f"PDF index {locator['pdf_page_index']}")
    parts.append(f"locator {locator['locator_id']}")
    if locator.get("role"):
        parts.append(f"role {locator['role']}")
    if locator.get("scope_note"):
        parts.append(str(locator["scope_note"]))
    return " / ".join(parts)


def build_audit_state(
    root: Path | None,
    finding_id: str,
) -> tuple[dict[str, Any], str]:
    """Resolve one admitted real audit chain from canonical owners, read-only."""

    root = root or repo_root()
    registry = load_registry(root)
    index = _index_registry(registry)

    finding_record = _record(index, finding_id, "finding")
    finding_resolved = resolve_record(root, finding_record)
    finding_section = finding_resolved["section"]

    selected: list[tuple[Mapping[str, Any], Mapping[str, Any], Mapping[str, Any]]] = []
    manifest_paths: set[Path] = set()
    for record in registry["records"]:
        if record.get("role") != "findspot":
            continue
        resolved = resolve_record(root, record)
        document = resolved["document"]
        if not isinstance(document, Mapping):
            raise ResearchStateError(f"{record['id']} manifest must be an object")
        case = _case_for_locator(document, record["id"])
        if case.get("finding_id") == finding_id:
            selected.append((record, resolved["target"], document))
            manifest_paths.add(resolved["path"])

    if not selected:
        raise ResearchStateError(f"finding {finding_id} has no registered #51 findspots")
    if len(manifest_paths) != 1:
        raise ResearchStateError(
            f"finding {finding_id} spans {len(manifest_paths)} manifests; WP1 v0 admits one"
        )

    manifest = selected[0][2]
    instance = manifest.get("instance")
    if not isinstance(instance, Mapping):
        raise ResearchStateError("reference manifest has no instance object")

    source_id = instance.get("source_id")
    representation_id = instance.get("representation_id")
    instance_id = instance.get("instance_id")
    if not all(isinstance(value, str) and value for value in (source_id, representation_id, instance_id)):
        raise ResearchStateError("reference manifest instance lacks source/representation/instance IDs")

    source_record = _record(index, source_id, "source")
    representation_record = _record(index, representation_id, "representation")
    instance_record = _record(index, instance_id, "instance")
    source_resolved = resolve_record(root, source_record)
    resolve_record(root, representation_record)
    resolve_record(root, instance_record)

    source_section = source_resolved["section"]
    source_label = _heading_label(source_section, source_id)
    source_type = _field(source_section, "source_type")
    finding_statement = _field(finding_section, "Finding")
    finding_status = _field(finding_section, "Status")
    finding_boundary = _field(finding_section, "Aussagegrenze")
    if not source_label or not source_type or not finding_statement or not finding_status:
        raise ResearchStateError(
            "canonical source/finding owner lacks fields required by admitted audit consumer"
        )

    selected_ids = {record["id"] for record, _, _ in selected}
    unresolved_relations = []
    for relation in manifest.get("relations", []):
        if not isinstance(relation, Mapping):
            continue
        if relation.get("evaluation") != "unresolved":
            continue
        if relation.get("from_locator_id") in selected_ids or relation.get("to_locator_id") in selected_ids:
            unresolved_relations.append(
                {
                    key: relation[key]
                    for key in ("relation_id", "type", "evaluation", "note")
                    if key in relation
                }
            )

    manifest_finding = _manifest_finding(manifest, finding_id)
    uncertainty: dict[str, Any] = {}
    if finding_boundary:
        uncertainty["finding_boundary"] = finding_boundary
    if manifest_finding.get("limit"):
        uncertainty["reference_limit"] = manifest_finding["limit"]
    if unresolved_relations:
        uncertainty["unresolved_reference_relations"] = unresolved_relations

    excerpts = []
    excerpt_ids = []
    for record, locator, _ in selected:
        excerpt_id = f"AUD-EXC-{record['id']}"
        excerpt_ids.append(excerpt_id)
        excerpts.append(
            {
                "id": excerpt_id,
                "instance_id": instance_id,
                "findspot": _findspot_text(locator),
            }
        )

    finding: dict[str, Any] = {
        "id": finding_id,
        "statement": finding_statement,
        "status": finding_status,
        "excerpt_ids": excerpt_ids,
    }
    if uncertainty:
        finding["uncertainty"] = uncertainty

    claim_id = f"AUDIT-ROOT-{finding_id}"
    state = {
        "sources": [
            {
                "id": source_id,
                "label": source_label,
                "type": source_type,
            }
        ],
        "representations": [
            {
                "id": representation_id,
                "source_id": source_id,
                "kind": instance.get("representation_kind"),
            }
        ],
        "instances": [
            {
                "id": instance_id,
                "representation_id": representation_id,
                "source_id": source_id,
                "inspection_status": instance.get("inspection_status"),
                "content_hash": (
                    f"sha256:{instance['sha256']}" if instance.get("sha256") else None
                ),
            }
        ],
        "derivatives": [],
        "excerpts": excerpts,
        "findings": [finding],
        "claims": [
            {
                "id": claim_id,
                "statement": (
                    f"Derived audit navigation root for canonical finding {finding_id}; "
                    "not a new historical claim."
                ),
                "status": "derived-view-root",
                "finding_ids": [finding_id],
            }
        ],
        "method_applications": [],
    }
    return state, claim_id
