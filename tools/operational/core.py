"""Small shared core for deterministic Histo-Orla operational commands.

This module owns mechanics only: repository paths, UTF-8/JSON loading and
JSON-Schema error normalization. Domain and rule semantics stay in their
owning validators and canonical contracts.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - exercised by command error paths
    Draft202012Validator = None


class OperationalError(RuntimeError):
    """A deterministic command could not read or validate its inputs."""


@dataclass(frozen=True)
class SchemaViolation:
    location: str
    message: str
    item_id: str | None = None


def repo_root_from(module_file: str | Path, parent_levels: int = 2) -> Path:
    return Path(module_file).resolve().parents[parent_levels]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise OperationalError(f"Cannot read {path}: {exc}") from exc


def load_json(path: Path) -> Any:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise OperationalError(f"Invalid JSON in {path}: {exc}") from exc


def schema_violations(
    schema: dict,
    data: dict,
    *,
    collection_key: str = "records",
) -> list[SchemaViolation]:
    if Draft202012Validator is None:
        raise OperationalError(
            "Python package 'jsonschema' is required; install "
            "tools/requirements/requirements.txt"
        )

    violations: list[SchemaViolation] = []
    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        parts = list(error.absolute_path)
        item_id = None
        if len(parts) >= 2 and parts[0] == collection_key and isinstance(parts[1], int):
            try:
                item_id = data[collection_key][parts[1]].get("id")
            except (AttributeError, IndexError, KeyError, TypeError):
                pass
        violations.append(
            SchemaViolation(
                location="/".join(str(part) for part in parts) or "<root>",
                message=error.message,
                item_id=item_id,
            )
        )
    return violations
