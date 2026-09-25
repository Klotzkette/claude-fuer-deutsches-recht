"""Dateigrenzen eigenständiger Downloads, keine Modell- oder Skillbudgets.

Eine große Werkstatt ist ein gezielt lesbares Arbeitsmittel. Die Grenze schützt
vor versehentlich vervielfachtem Dateiinhalt; sie ist kein anzustrebender Umfang.
"""

import json
from pathlib import Path

_LIMITS = json.loads(Path(__file__).with_name("prompt-limits.json").read_text(encoding="utf-8"))
MAX_WORKSHOP_BYTES = _LIMITS["workshop_max_bytes"]
MAX_MINI_BYTES = _LIMITS["mini_max_bytes"]
