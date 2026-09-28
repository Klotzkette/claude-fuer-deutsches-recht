"""Dateigrenzen eigenständiger Downloads, keine Modell- oder Skillbudgets.

Eine große Werkstatt ist ein gezielt lesbares Arbeitsmittel. Die Grenze schützt
vor versehentlich vervielfachtem Dateiinhalt; sie ist kein anzustrebender Umfang.
"""

import json
from pathlib import Path

_LIMITS = json.loads(Path(__file__).with_name("prompt-limits.json").read_text(encoding="utf-8"))
MAX_WORKSHOP_BYTES = _LIMITS["workshop_max_bytes"]
MAX_MINI_BYTES = _LIMITS["mini_max_bytes"]


def mini_limit(slug: str) -> tuple[int, int]:
    """UTF-8-Dateischutz und Unicode-Zeichengrenze getrennt anwenden."""
    custom = _LIMITS.get("mini_by_plugin", {}).get(slug, {})
    return custom.get("max_bytes", MAX_MINI_BYTES), custom.get("max_characters", MAX_MINI_BYTES)


def mini_within_limits(slug: str, data: bytes) -> bool:
    byte_limit, char_limit = mini_limit(slug)
    return bool(data) and len(data) <= byte_limit and len(data.decode("utf-8")) <= char_limit
