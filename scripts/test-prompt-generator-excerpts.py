#!/usr/bin/env python3
"""Regressionstest für vollständige Sätze in gekürzten Prompt-Auszügen."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "generate-werkstatt-und-schnellstart-prompts.py"
SPEC = importlib.util.spec_from_file_location("generate_prompts", SCRIPT)
assert SPEC and SPEC.loader
G = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G
SPEC.loader.exec_module(G)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    source = (
        "Ein Insolvenzplan darf nur Gegenstände regeln, die nach Paragraf 217 InsO "
        "und den besonderen Planvorschriften disponibel sind. Nicht disponible "
        "Regelungen sind gesondert zu prüfen."
    )
    shortened = G.clean(source, 145)
    require(
        shortened.endswith("disponibel sind."),
        f"vollständiger Satz wurde verstümmelt: {shortened!r}",
    )

    fragment = G.clean("Frist und Form prüfen und anschließend mit den", 42)
    require(not fragment.endswith(" den."), f"echtes Hängewort blieb stehen: {fragment!r}")

    print("test-prompt-generator-excerpts OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
