"""Deterministic, read-only research audit derivation for Issue #55.

The renderer consumes already-structured, provider-neutral Research State and
projects a Markdown audit path. It owns no research truth, status transition,
provider lookup, or scholarly interpretation. All research-bearing values in
its output come from the supplied state; the only added text is stable view
structure and mechanical ``missing/unresolved`` markers for absent references.

The expected roles follow the existing #50 contract (claim, finding, excerpt /
findspot, derivative, instance, representation, source, method application).
This module is a prototype adapter over those roles, not a new canonical
serialization or ontology.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any


class AuditViewError(ValueError):
    """The requested root object cannot be deterministically audited."""


def _index(state: Mapping[str, Any], collection: str) -> dict[str, Mapping[str, Any]]:
    records = state.get(collection, [])
    if not isinstance(records, list):
        raise AuditViewError(f"{collection} must be a list")

    indexed: dict[str, Mapping[str, Any]] = {}
    for record in records:
        if not isinstance(record, Mapping):
            raise AuditViewError(f"{collection} entries must be mappings")
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id.strip():
            raise AuditViewError(f"{collection} entry is missing id")
        if record_id in indexed:
            raise AuditViewError(f"duplicate {collection} id: {record_id}")
        indexed[record_id] = record
    return indexed


def _ids(value: Any) -> tuple[str, ...]:
    if isinstance(value, str):
        values = [value]
    elif isinstance(value, list):
        values = value
    else:
        values = []
    return tuple(sorted({item.strip() for item in values if isinstance(item, str) and item.strip()}))


def _stable(value: Any) -> str:
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _append_if_present(lines: list[str], label: str, record: Mapping[str, Any], key: str) -> bool:
    if key not in record or record[key] is None or record[key] == "":
        return False
    lines.append(f"- {label}: {_stable(record[key])}")
    return True


def _append_mapping(lines: list[str], prefix: str, value: Any) -> None:
    if not isinstance(value, Mapping):
        return
    for key in sorted(value):
        lines.append(f"- {prefix}.{key}: {_stable(value[key])}")


def _gap(gaps: set[str], message: str) -> None:
    gaps.add(f"missing/unresolved: {message}")


def render_audit_view(state: Mapping[str, Any], claim_id: str) -> str:
    """Render a stable Markdown audit view without mutating or enriching state.

    References are followed only when the input explicitly supplies them.
    Missing objects/links are exposed as mechanical ``missing/unresolved``
    gaps instead of being inferred. Provider references and availability are
    displayed as attributes; they never substitute for internal IDs.
    """

    claims = _index(state, "claims")
    findings = _index(state, "findings")
    excerpts = _index(state, "excerpts")
    derivatives = _index(state, "derivatives")
    instances = _index(state, "instances")
    representations = _index(state, "representations")
    sources = _index(state, "sources")
    method_applications = _index(state, "method_applications")

    claim = claims.get(claim_id)
    if claim is None:
        raise AuditViewError(f"unknown claim id: {claim_id}")

    lines = ["# Derived Research Audit", "", "## Claim / Answer", f"- claim_id: {claim_id}"]
    _append_if_present(lines, "statement", claim, "statement")
    _append_if_present(lines, "status", claim, "status")
    _append_if_present(lines, "validation_status", claim, "validation_status")

    gaps: set[str] = set()
    finding_ids = _ids(claim.get("finding_ids"))
    if not finding_ids:
        _gap(gaps, f"claim {claim_id} has no finding reference")

    for finding_id in finding_ids:
        lines.extend(["", f"## Finding {finding_id}"])
        finding = findings.get(finding_id)
        if finding is None:
            _gap(gaps, f"claim {claim_id} references absent finding {finding_id}")
            lines.append(f"- finding_id: {finding_id}")
            lines.append("- state: missing/unresolved")
            continue

        lines.append(f"- finding_id: {finding_id}")
        _append_if_present(lines, "statement", finding, "statement")
        _append_if_present(lines, "status", finding, "status")
        _append_if_present(lines, "validation_status", finding, "validation_status")
        _append_if_present(lines, "candidate_origin", finding, "candidate_origin")
        _append_if_present(lines, "superseded_by", finding, "superseded_by")
        _append_if_present(lines, "history", finding, "history")

        excerpt_ids = _ids(finding.get("excerpt_ids"))
        if not excerpt_ids:
            _gap(gaps, f"finding {finding_id} has no excerpt reference")

        for excerpt_id in excerpt_ids:
            lines.extend(["", f"### Excerpt / Findspot {excerpt_id}"])
            excerpt = excerpts.get(excerpt_id)
            if excerpt is None:
                _gap(gaps, f"finding {finding_id} references absent excerpt {excerpt_id}")
                lines.append(f"- excerpt_id: {excerpt_id}")
                lines.append("- state: missing/unresolved")
                continue

            lines.append(f"- excerpt_id: {excerpt_id}")
            _append_if_present(lines, "text", excerpt, "text")
            if not _append_if_present(lines, "findspot", excerpt, "findspot"):
                _gap(gaps, f"excerpt {excerpt_id} has no findspot")

            derivative_id = excerpt.get("derivative_id")
            instance_id = excerpt.get("instance_id")
            if isinstance(derivative_id, str) and derivative_id.strip():
                derivative_id = derivative_id.strip()
                lines.append(f"- derivative_id: {derivative_id}")
                derivative = derivatives.get(derivative_id)
                if derivative is None:
                    _gap(gaps, f"excerpt {excerpt_id} references absent derivative {derivative_id}")
                else:
                    _append_if_present(lines, "derivative_kind", derivative, "kind")
                    _append_if_present(lines, "derivative_status", derivative, "status")
                    _append_if_present(lines, "derivative_processor", derivative, "processor")
                    _append_if_present(lines, "derivative_version", derivative, "version")
                    _append_mapping(lines, "derivative.provider_ref", derivative.get("provider_refs"))
                    if not instance_id:
                        instance_id = derivative.get("instance_id")

            lines.extend(["", "### Instance / Source"])
            if not isinstance(instance_id, str) or not instance_id.strip():
                _gap(gaps, f"excerpt {excerpt_id} has no instance path")
                lines.append("- instance_id: missing/unresolved")
                continue

            instance_id = instance_id.strip()
            lines.append(f"- instance_id: {instance_id}")
            instance = instances.get(instance_id)
            if instance is None:
                _gap(gaps, f"excerpt {excerpt_id} resolves to absent instance {instance_id}")
                lines.append("- instance_state: missing/unresolved")
                continue

            _append_if_present(lines, "inspection_status", instance, "inspection_status")
            _append_mapping(lines, "instance.provider_ref", instance.get("provider_refs"))
            _append_mapping(lines, "instance.availability", instance.get("availability"))

            representation_id = instance.get("representation_id")
            source_id = instance.get("source_id")
            if isinstance(representation_id, str) and representation_id.strip():
                representation_id = representation_id.strip()
                lines.append(f"- representation_id: {representation_id}")
                representation = representations.get(representation_id)
                if representation is None:
                    _gap(gaps, f"instance {instance_id} references absent representation {representation_id}")
                else:
                    _append_if_present(lines, "representation_kind", representation, "kind")
                    _append_if_present(lines, "representation_label", representation, "label")
                    if not source_id:
                        source_id = representation.get("source_id")

            if not isinstance(source_id, str) or not source_id.strip():
                _gap(gaps, f"instance {instance_id} has no source path")
                lines.append("- source_id: missing/unresolved")
                continue

            source_id = source_id.strip()
            lines.append(f"- source_id: {source_id}")
            source = sources.get(source_id)
            if source is None:
                _gap(gaps, f"instance {instance_id} resolves to absent source {source_id}")
                lines.append("- source_state: missing/unresolved")
                continue

            _append_if_present(lines, "source_label", source, "label")
            _append_if_present(lines, "source_type", source, "type")
            _append_mapping(lines, "source.provider_ref", source.get("provider_refs"))
            _append_mapping(lines, "source.availability", source.get("availability"))

        lines.extend(["", "### Method / Validation / Uncertainty"])
        method_application_id = finding.get("method_application_id")
        if not isinstance(method_application_id, str) or not method_application_id.strip():
            _gap(gaps, f"finding {finding_id} has no method application reference")
            lines.append("- method_application_id: missing/unresolved")
        else:
            method_application_id = method_application_id.strip()
            lines.append(f"- method_application_id: {method_application_id}")
            application = method_applications.get(method_application_id)
            if application is None:
                _gap(gaps, f"finding {finding_id} references absent method application {method_application_id}")
                lines.append("- method_application_state: missing/unresolved")
            else:
                for key, label in (
                    ("profile_ref", "method_profile_ref"),
                    ("profile_version", "method_profile_version"),
                    ("profile_status", "method_profile_status"),
                    ("work_order_ref", "work_order_ref"),
                    ("scope", "scope"),
                    ("leading_domains", "leading_domains"),
                    ("application_summary", "application_summary"),
                    ("validation_status", "method_validation_status"),
                ):
                    _append_if_present(lines, label, application, key)

        validation_status = finding.get("validation_status")
        if "validation_status" not in finding or validation_status is None or validation_status == "":
            _gap(gaps, f"finding {finding_id} has no validation_status")
            lines.append("- finding_validation_status: missing/unresolved")

        uncertainty = finding.get("uncertainty")
        if "uncertainty" not in finding or uncertainty is None or uncertainty == "":
            _gap(gaps, f"finding {finding_id} has no uncertainty state")
            lines.append("- uncertainty: missing/unresolved")
        else:
            lines.append(f"- uncertainty: {_stable(uncertainty)}")

        if "alternatives" not in finding:
            _gap(gaps, f"finding {finding_id} has no alternatives field")
            lines.append("- alternatives: missing/unresolved")
        else:
            lines.append(f"- alternatives: {_stable(finding['alternatives'])}")

    lines.extend(["", "## Missing / unresolved"])
    if gaps:
        lines.extend(f"- {item}" for item in sorted(gaps))
    else:
        lines.append("- reference gaps: []")

    return "\n".join(lines) + "\n"
