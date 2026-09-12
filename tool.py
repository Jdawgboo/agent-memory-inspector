"""Inspect structured agent memories for quality signals."""
from __future__ import annotations

from datetime import date
from typing import Any


def inspect(memories: list[dict[str, Any]], today: str, stale_after_days: int = 30) -> dict[str, list[str]]:
    """Find entries missing provenance, stale entries, and duplicate text."""
    now = date.fromisoformat(today)
    seen: dict[str, str] = {}
    result = {"missing_source": [], "stale": [], "duplicates": []}
    for index, memory in enumerate(memories):
        memory_id = str(memory.get("id", index))
        if not memory.get("source"):
            result["missing_source"].append(memory_id)
        created = memory.get("created_at")
        if created and (now - date.fromisoformat(str(created))).days > stale_after_days:
            result["stale"].append(memory_id)
        text = " ".join(str(memory.get("text", "")).lower().split())
        if text in seen:
            result["duplicates"].append(f"{seen[text]}:{memory_id}")
        elif text:
            seen[text] = memory_id
    return result
