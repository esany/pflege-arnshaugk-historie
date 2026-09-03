"""Deterministic pre-write guards for repository text mutations.

This module implements mechanics only. It does not decide whether a scholarly
or project change is substantively correct or authorised. Its purpose is to
make a caller declare the mutation shape before writing and to prevent two
observed execution failures:

* a bounded edit being submitted as a broader/destructive replacement; and
* an already-satisfied target state producing another write/commit.

Adapters should call an assessment function before any write. ``change`` means
that the returned candidate may be written, ``no_change`` means that no write
must be emitted, and ``blocked`` means that the declared mutation contract was
not satisfied.
"""

from __future__ import annotations

import os
import stat
import tempfile
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Literal


MutationStatus = Literal["change", "no_change", "blocked"]


class MutationBlocked(RuntimeError):
    """A requested write violated its declared mechanical mutation contract."""


@dataclass(frozen=True)
class MutationAssessment:
    status: MutationStatus
    reason: str
    current_sha256: str
    candidate_sha256: str | None
    candidate_text: str | None


def text_fingerprint(text: str) -> str:
    """Return a stable SHA-256 fingerprint for exact UTF-8 text state."""

    return sha256(text.encode("utf-8")).hexdigest()


def _assessment(
    status: MutationStatus,
    reason: str,
    current_text: str,
    candidate_text: str | None,
) -> MutationAssessment:
    return MutationAssessment(
        status=status,
        reason=reason,
        current_sha256=text_fingerprint(current_text),
        candidate_sha256=(text_fingerprint(candidate_text) if candidate_text is not None else None),
        candidate_text=candidate_text,
    )


def assess_state_delta(current_text: str, candidate_text: str) -> MutationAssessment:
    """Classify an exact candidate state without assigning mutation authority.

    This is the smallest progress/idempotency guard: an identical candidate is
    ``no_change`` and therefore must not produce another write or commit.
    """

    if candidate_text == current_text:
        return _assessment(
            "no_change",
            "candidate state is byte-equivalent to current UTF-8 text; skip write",
            current_text,
            current_text,
        )
    return _assessment(
        "change",
        "candidate state differs from current state",
        current_text,
        candidate_text,
    )


def plan_bounded_replace(
    current_text: str,
    expected_fragment: str,
    replacement_fragment: str,
) -> MutationAssessment:
    """Construct the only valid result for one declared bounded text edit.

    The expected fragment must occur exactly once. If it no longer occurs and
    the replacement occurs exactly once, the requested postcondition is treated
    as already satisfied and the result is ``no_change``. Ambiguous or missing
    preconditions fail closed.
    """

    if not expected_fragment:
        return _assessment(
            "blocked",
            "bounded edit requires a non-empty expected fragment",
            current_text,
            None,
        )

    if expected_fragment == replacement_fragment:
        return _assessment(
            "no_change",
            "declared replacement is identical to expected fragment; skip write",
            current_text,
            current_text,
        )

    expected_count = current_text.count(expected_fragment)
    if expected_count == 1:
        candidate = current_text.replace(expected_fragment, replacement_fragment, 1)
        return assess_state_delta(current_text, candidate)

    if expected_count == 0:
        replacement_count = current_text.count(replacement_fragment)
        if replacement_fragment and replacement_count == 1:
            return _assessment(
                "no_change",
                "expected fragment is absent and replacement is already present exactly once; postcondition already satisfied",
                current_text,
                current_text,
            )
        return _assessment(
            "blocked",
            "expected fragment is absent and the requested postcondition is not uniquely established",
            current_text,
            None,
        )

    return _assessment(
        "blocked",
        f"expected fragment is ambiguous ({expected_count} occurrences); bounded edit requires exactly one",
        current_text,
        None,
    )


def assess_bounded_candidate(
    current_text: str,
    candidate_text: str,
    expected_fragment: str,
    replacement_fragment: str,
) -> MutationAssessment:
    """Verify that a full candidate file represents only the declared edit.

    This is the destructive-loss guard for callers that still need to submit a
    complete file body to a storage API. The candidate must be exactly equal to
    the result constructed from the freshly read current state. Any unrelated
    deletion, insertion or rewrite is blocked.
    """

    plan = plan_bounded_replace(current_text, expected_fragment, replacement_fragment)
    if plan.status == "blocked":
        return plan

    if plan.status == "no_change":
        if candidate_text == current_text:
            return plan
        return _assessment(
            "blocked",
            "requested postcondition is already satisfied, but candidate introduces additional changes",
            current_text,
            candidate_text,
        )

    if candidate_text != plan.candidate_text:
        return _assessment(
            "blocked",
            "candidate differs outside the declared bounded replacement",
            current_text,
            candidate_text,
        )

    return plan


def assess_full_replacement(
    current_text: str,
    candidate_text: str,
    *,
    explicit: bool = False,
) -> MutationAssessment:
    """Require an explicit mutation type before allowing a full replacement.

    This does not assert that a full replacement is substantively safe. It only
    prevents a caller from silently treating a broad rewrite as a bounded edit.
    Consequential full replacements still require the appropriate diff/review/
    admission path outside this mechanical helper.
    """

    delta = assess_state_delta(current_text, candidate_text)
    if delta.status == "no_change":
        return delta
    if not explicit:
        return _assessment(
            "blocked",
            "full replacement was not explicitly declared",
            current_text,
            candidate_text,
        )
    return _assessment(
        "change",
        "explicit full replacement declared; downstream admission/review remains required",
        current_text,
        candidate_text,
    )


def apply_bounded_file_edit(
    path: str | Path,
    expected_fragment: str,
    replacement_fragment: str,
) -> MutationAssessment:
    """Apply one guarded bounded edit to a local UTF-8 file atomically.

    The file is read fresh inside this function. ``blocked`` raises
    :class:`MutationBlocked`; ``no_change`` returns without touching the file;
    only ``change`` reaches the atomic replace. Existing permission bits are
    retained. This is a thin execution adapter, not a source of mutation
    authority.
    """

    target = Path(path)
    try:
        current_bytes = target.read_bytes()
        current_text = current_bytes.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise MutationBlocked(f"cannot read UTF-8 mutation target {target}: {exc}") from exc

    assessment = plan_bounded_replace(current_text, expected_fragment, replacement_fragment)
    if assessment.status == "blocked":
        raise MutationBlocked(assessment.reason)
    if assessment.status == "no_change":
        return assessment

    candidate_text = assessment.candidate_text
    if candidate_text is None:
        raise MutationBlocked("mutation plan produced no candidate text")

    mode = stat.S_IMODE(target.stat().st_mode)
    fd, temp_name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(candidate_text.encode("utf-8"))
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp_path, mode)
        os.replace(temp_path, target)
    except Exception:
        try:
            temp_path.unlink(missing_ok=True)
        finally:
            raise

    return assessment
