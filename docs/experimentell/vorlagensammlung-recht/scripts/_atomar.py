"""Kleine Helfer für ausfallsicheres Ersetzen erzeugter Dateien."""
from __future__ import annotations

import os
import tempfile
from collections.abc import Callable
from pathlib import Path


Dateipruefung = Callable[[Path], None]


def bytes_atomar_schreiben(
    ziel: Path,
    inhalt: bytes,
    *,
    pruefen: Dateipruefung | None = None,
) -> None:
    """Schreibt Bytes vollständig, prüft sie optional und ersetzt erst danach."""
    ziel.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb",
        dir=ziel.parent,
        prefix=f".{ziel.name}.",
        suffix=".tmp",
        delete=False,
    ) as temporaer:
        temp_pfad = Path(temporaer.name)
        temporaer.write(inhalt)
        temporaer.flush()
        os.fsync(temporaer.fileno())
    try:
        temp_pfad.chmod(0o644)
        if pruefen is not None:
            pruefen(temp_pfad)
        temp_pfad.replace(ziel)
    finally:
        if temp_pfad.exists():
            temp_pfad.unlink()


def text_atomar_schreiben(
    ziel: Path,
    inhalt: str,
    *,
    encoding: str = "utf-8",
    pruefen: Dateipruefung | None = None,
) -> None:
    """Kodiert Text und nutzt denselben atomaren Austauschpfad wie Binärdaten."""
    bytes_atomar_schreiben(
        ziel,
        inhalt.encode(encoding),
        pruefen=pruefen,
    )
