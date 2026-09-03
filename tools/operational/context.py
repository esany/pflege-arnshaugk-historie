"""Derived current-work context and restartability mechanics.

This module does not store task truth and does not infer scholarly meaning.
Adapters provide facts already resolved from canonical owners/state; this core
validates their minimum executable shape and derives a transient resume view.

The core also carries prerequisite validation against an explicit basis
fingerprint. A prerequisite is not invalidated by a new model/session merely
being uncertain: revalidation is required only when the declared canonical
basis changes.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Literal


PrerequisiteStatus = Literal["pass", "fail", "unresolved"]
ContextStatus = Literal["ready", "unresolved", "blocked"]
CursorReaction = Literal["continue", "redirect"]


class ContextError(ValueError):
    """The supplied canonical work facts cannot form an executable context."""


@dataclass(frozen=True, order=True)
class BasisRef:
    """One versioned/identified input that justified a prerequisite decision."""

    ref: str
    state_fingerprint: str


@dataclass(frozen=True)
class PrerequisiteState:
    ref: str
    status: PrerequisiteStatus
    basis_refs: tuple[BasisRef, ...]
    basis_fingerprint: str
    note: str = ""


@dataclass(frozen=True)
class CurrentContext:
    primary_function: str
    work_owner_ref: str
    work_order_ref: str
    objective: str
    scope: tuple[str, ...]
    exclusions: tuple[str, ...]
    leading_domains: tuple[str, ...]
    method_quality_frame: tuple[str, ...]
    required_evidence: tuple[str, ...]
    current_executable_action: str
    prerequisites: tuple[PrerequisiteState, ...]
    open_blockers: tuple[str, ...]
    unresolved: tuple[str, ...]
    may: tuple[str, ...]
    must_not: tuple[str, ...]
    stop_handoff_when: tuple[str, ...]
    return_condition: str
    persistence_target: str
    source_refs: tuple[str, ...]
    status: ContextStatus


@dataclass(frozen=True)
class CursorAssessment:
    reaction: CursorReaction
    work_owner_ref: str
    current_executable_action: str
    reason: str


def _required(value: str, field: str) -> str:
    value = value.strip()
    if not value:
        raise ContextError(f"{field} is required")
    return value


def _clean(values: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    return tuple(value.strip() for value in values if value and value.strip())


def _required_list(values: tuple[str, ...] | list[str], field: str) -> tuple[str, ...]:
    cleaned = _clean(values)
    if not cleaned:
        raise ContextError(f"{field} must not be empty")
    return cleaned


def basis_fingerprint(basis_refs: tuple[BasisRef, ...] | list[BasisRef]) -> str:
    """Return a deterministic fingerprint for the declared validation basis."""

    normalized = sorted(
        ({"ref": _required(item.ref, "basis ref"), "state": _required(item.state_fingerprint, "basis state fingerprint")} for item in basis_refs),
        key=lambda item: (item["ref"], item["state"]),
    )
    payload = json.dumps(normalized, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return sha256(payload.encode("utf-8")).hexdigest()


def prerequisite_state(
    ref: str,
    status: PrerequisiteStatus,
    basis_refs: tuple[BasisRef, ...] | list[BasisRef],
    *,
    note: str = "",
) -> PrerequisiteState:
    """Create one sticky prerequisite whose status is tied to explicit basis."""

    ref = _required(ref, "prerequisite ref")
    if status not in {"pass", "fail", "unresolved"}:
        raise ContextError(f"unsupported prerequisite status: {status}")
    refs = tuple(sorted(basis_refs))
    if not refs:
        raise ContextError("prerequisite basis_refs must not be empty")
    return PrerequisiteState(
        ref=ref,
        status=status,
        basis_refs=refs,
        basis_fingerprint=basis_fingerprint(refs),
        note=note.strip(),
    )


def prerequisite_needs_revalidation(
    previous: PrerequisiteState,
    current_basis_refs: tuple[BasisRef, ...] | list[BasisRef],
) -> bool:
    """Revalidate only when the explicit canonical basis changed."""

    return previous.basis_fingerprint != basis_fingerprint(current_basis_refs)


def derive_current_context(
    *,
    primary_function: str,
    work_owner_ref: str,
    work_order_ref: str,
    objective: str,
    scope: tuple[str, ...] | list[str],
    exclusions: tuple[str, ...] | list[str],
    leading_domains: tuple[str, ...] | list[str],
    method_quality_frame: tuple[str, ...] | list[str],
    required_evidence: tuple[str, ...] | list[str],
    current_executable_action: str,
    prerequisites: tuple[PrerequisiteState, ...] | list[PrerequisiteState],
    open_blockers: tuple[str, ...] | list[str],
    unresolved: tuple[str, ...] | list[str],
    may: tuple[str, ...] | list[str],
    must_not: tuple[str, ...] | list[str],
    stop_handoff_when: tuple[str, ...] | list[str],
    return_condition: str,
    persistence_target: str,
    source_refs: tuple[str, ...] | list[str],
) -> CurrentContext:
    """Derive a transient executable/resume view from already-canonical facts."""

    primary_function = _required(primary_function, "primary_function")
    work_owner_ref = _required(work_owner_ref, "work_owner_ref")
    work_order_ref = _required(work_order_ref, "work_order_ref")
    objective = _required(objective, "objective")
    current_executable_action = _required(current_executable_action, "current_executable_action")
    return_condition = _required(return_condition, "return_condition")
    persistence_target = _required(persistence_target, "persistence_target")

    scope_clean = _required_list(scope, "scope")
    leading_domains_clean = _required_list(leading_domains, "leading_domains")
    method_quality_frame_clean = _required_list(method_quality_frame, "method_quality_frame")
    required_evidence_clean = _required_list(required_evidence, "required_evidence")
    source_refs_clean = _required_list(source_refs, "source_refs")

    prereqs = tuple(prerequisites)
    blockers = list(_clean(open_blockers))
    unresolved_items = list(_clean(unresolved))

    for prerequisite in prereqs:
        if prerequisite.status == "fail":
            blockers.append(f"prerequisite:{prerequisite.ref}")
        elif prerequisite.status == "unresolved":
            unresolved_items.append(f"prerequisite:{prerequisite.ref}")

    blockers_tuple = tuple(dict.fromkeys(blockers))
    unresolved_tuple = tuple(dict.fromkeys(unresolved_items))
    if blockers_tuple:
        status: ContextStatus = "blocked"
    elif unresolved_tuple:
        status = "unresolved"
    else:
        status = "ready"

    return CurrentContext(
        primary_function=primary_function,
        work_owner_ref=work_owner_ref,
        work_order_ref=work_order_ref,
        objective=objective,
        scope=scope_clean,
        exclusions=_clean(exclusions),
        leading_domains=leading_domains_clean,
        method_quality_frame=method_quality_frame_clean,
        required_evidence=required_evidence_clean,
        current_executable_action=current_executable_action,
        prerequisites=prereqs,
        open_blockers=blockers_tuple,
        unresolved=unresolved_tuple,
        may=_clean(may),
        must_not=_clean(must_not),
        stop_handoff_when=_clean(stop_handoff_when),
        return_condition=return_condition,
        persistence_target=persistence_target,
        source_refs=source_refs_clean,
        status=status,
    )


def assess_cursor_request(
    context: CurrentContext,
    *,
    requested_work_owner_ref: str,
    requested_action: str,
    priority_authorized: bool = False,
) -> CursorAssessment:
    """Keep the canonical cursor unless an external authority changed priority.

    ``priority_authorized`` is an input fact supplied by the caller. This module
    neither discovers nor grants that authority.
    """

    requested_owner = _required(requested_work_owner_ref, "requested_work_owner_ref")
    requested_action = _required(requested_action, "requested_action")

    same_cursor = (
        requested_owner == context.work_owner_ref
        and requested_action == context.current_executable_action
    )
    if same_cursor:
        return CursorAssessment(
            "continue",
            context.work_owner_ref,
            context.current_executable_action,
            "requested cursor matches current canonical cursor",
        )

    if not priority_authorized:
        return CursorAssessment(
            "redirect",
            context.work_owner_ref,
            context.current_executable_action,
            "requested cursor differs from canonical cursor without external priority authority",
        )

    return CursorAssessment(
        "continue",
        requested_owner,
        requested_action,
        "external priority authority explicitly supplied by caller",
    )
