"""Thin JSON work-order adapter for the derived current-context core.

The JSON record is canonical curated work/task state. The returned
:class:`CurrentContext` is transient/derived. This adapter validates structure
and checks declared Git-blob fingerprints for prerequisite basis files; it does
not infer meaning from Markdown or grant scholarly/priority authority.
"""

from __future__ import annotations

from hashlib import sha1
import json
from pathlib import Path
from typing import Any

from tools.operational.context import (
    BasisRef,
    ContextError,
    CurrentContext,
    derive_current_context,
    prerequisite_needs_revalidation,
    prerequisite_state,
)


def git_blob_sha(path: Path) -> str:
    """Compute the Git SHA-1 object id for a file without invoking Git."""

    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


def _mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContextError(f"{field} must be an object")
    return value


def _list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise ContextError(f"{field} must be an array")
    return value


def load_work_order(path: str | Path, *, root: str | Path | None = None) -> CurrentContext:
    """Load one canonical JSON work order and derive the current resume context.

    A prerequisite whose previously recorded ``pass`` basis no longer matches
    current repository bytes is downgraded to ``unresolved`` for revalidation.
    Existing ``unresolved``/``fail`` states remain explicit.
    """

    spec_path = Path(path)
    repo_root = Path(root) if root is not None else spec_path.parent
    try:
        data = json.loads(spec_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContextError(f"cannot load work-order JSON {spec_path}: {exc}") from exc

    data = _mapping(data, "work order")
    if data.get("schema_version") != "0.1":
        raise ContextError("unsupported work-order schema_version")

    prereqs = []
    for index, raw in enumerate(_list(data.get("prerequisites", []), "prerequisites")):
        item = _mapping(raw, f"prerequisites[{index}]")
        basis_specs = _list(item.get("basis", []), f"prerequisites[{index}].basis")
        previous_basis: list[BasisRef] = []
        current_basis: list[BasisRef] = []
        for basis_index, raw_basis in enumerate(basis_specs):
            basis = _mapping(raw_basis, f"prerequisites[{index}].basis[{basis_index}]")
            rel_path = str(basis.get("path", "")).strip()
            expected_sha = str(basis.get("git_blob_sha", "")).strip()
            if not rel_path or not expected_sha:
                raise ContextError("basis path and git_blob_sha are required")
            target = repo_root / rel_path
            try:
                current_sha = git_blob_sha(target)
            except OSError as exc:
                raise ContextError(f"cannot inspect prerequisite basis {rel_path}: {exc}") from exc
            previous_basis.append(BasisRef(rel_path, f"git-blob:{expected_sha}"))
            current_basis.append(BasisRef(rel_path, f"git-blob:{current_sha}"))

        status = str(item.get("status", "")).strip()
        previous = prerequisite_state(
            str(item.get("ref", "")),
            status,  # validated by prerequisite_state
            previous_basis,
            note=str(item.get("note", "")),
        )
        if previous.status == "pass" and prerequisite_needs_revalidation(previous, current_basis):
            prereqs.append(
                prerequisite_state(
                    previous.ref,
                    "unresolved",
                    current_basis,
                    note="declared prerequisite basis changed; revalidation required",
                )
            )
        else:
            prereqs.append(previous)

    return derive_current_context(
        primary_function=str(data.get("primary_function", "")),
        work_owner_ref=str(data.get("work_owner_ref", "")),
        work_order_ref=str(data.get("work_order_ref", "")),
        objective=str(data.get("objective", "")),
        scope=_list(data.get("scope", []), "scope"),
        exclusions=_list(data.get("exclusions", []), "exclusions"),
        leading_domains=_list(data.get("leading_domains", []), "leading_domains"),
        method_quality_frame=_list(data.get("method_quality_frame", []), "method_quality_frame"),
        required_evidence=_list(data.get("required_evidence", []), "required_evidence"),
        current_executable_action=str(data.get("current_executable_action", "")),
        prerequisites=prereqs,
        open_blockers=_list(data.get("open_blockers", []), "open_blockers"),
        unresolved=_list(data.get("unresolved", []), "unresolved"),
        may=_list(data.get("may", []), "may"),
        must_not=_list(data.get("must_not", []), "must_not"),
        stop_handoff_when=_list(data.get("stop_handoff_when", []), "stop_handoff_when"),
        return_condition=str(data.get("return_condition", "")),
        persistence_target=str(data.get("persistence_target", "")),
        source_refs=_list(data.get("source_refs", []), "source_refs"),
    )
