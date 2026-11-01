"""Argumentprüfung vor dem schreibenden Einstieg bestehender Generatoren."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def parse_generator_cli(description: str | None, argv: Sequence[str] | None = None) -> None:
    """Erlaubt den bisherigen argumentlosen Lauf und eine schreibfreie Hilfe.

    Ein echter Prüfmodus ist hier nicht implementiert. Insbesondere --check und
    unbekannte Argumente müssen abbrechen, bevor der Generator gestartet wird.
    """
    parser = argparse.ArgumentParser(
        description=description,
        add_help=False,
        allow_abbrev=False,
        epilog=(
            "Ohne Argumente wird der bisherige Generatorlauf ausgeführt; dabei können "
            "Dateien geschrieben werden. Ein Prüfmodus (--check) wird nicht unterstützt."
        ),
    )
    parser.add_argument(
        "-h", "--help", action="help", help="Diese Hilfe anzeigen und beenden, ohne Dateien zu erzeugen."
    )
    _, unknown = parser.parse_known_args(argv)
    if unknown:
        parser.error("Nicht unterstützte Argumente: " + " ".join(unknown))
