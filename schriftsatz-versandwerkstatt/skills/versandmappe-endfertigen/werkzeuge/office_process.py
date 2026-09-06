"""Begrenzte Office-Prozesse für separat installierbare Dokumentwerkzeuge.

Die beiden Pluginpakete enthalten dieselbe Datei lokal; ein Regressionstest
sichert den Gleichstand, damit keine Abhängigkeit vom ganzen Repository besteht.
"""

from __future__ import annotations

import os
import signal
import subprocess
import tempfile
from pathlib import Path


def run_office(command: list[str], *, timeout: float, env=None) -> tuple[int, str]:
    """Wartet ohne unbeschränkten PIPE-Puffer und beendet die eigene Prozessgruppe."""
    with tempfile.TemporaryFile() as log:
        process = subprocess.Popen(
            command, stdin=subprocess.DEVNULL, stdout=log, stderr=log,
            env=env, start_new_session=os.name == "posix",
        )
        try:
            process.wait(timeout=timeout)
        finally:
            # Office-Launcher können einen weiterlaufenden Kindprozess hinterlassen.
            if os.name == "posix":
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            elif process.poll() is None:
                process.kill()
            process.wait(timeout=5)
        log.seek(0, os.SEEK_END)
        log.seek(max(0, log.tell() - 2048))
        details = log.read(2048).decode("utf-8", errors="replace").strip()
        return process.returncode, details


def pdf_markers(path: Path, markers: tuple[bytes, ...]) -> set[bytes]:
    """Sucht auch über Blockgrenzen, ohne eine zweite vollständige PDF-Kopie."""
    found: set[bytes] = set()
    overlap = max((len(marker) for marker in markers), default=1) - 1
    tail = b""
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            data = tail + block
            found.update(marker for marker in markers if marker in data)
            if len(found) == len(markers):
                break
            tail = data[-overlap:] if overlap else b""
    return found
