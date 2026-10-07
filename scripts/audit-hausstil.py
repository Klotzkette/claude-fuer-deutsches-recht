#!/usr/bin/env python3
"""Meldet jede Schriftnennung ausserhalb der kanonischen Phrase aus hausstil.json und der
dort eingetragenen Ausnahmen und Fremdvorgaben, mit Datei und Zeile. Prueft ausserdem,
dass CLAUDE.md die aktuelle Phrase enthaelt. Endet mit Status 1, wenn etwas zu melden ist.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hausstil as hs  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=hs.REPO, help="Repository-Wurzel (Standard: dieses Repo)")
    argumente = parser.parse_args(argv)
    repo = argumente.repo.resolve()
    stil = hs.lade_hausstil(repo / "hausstil.json")
    meldungen = []
    for pfad in hs.repo_textdateien(repo, hs.ENDUNGEN_PRUEFEN):
        if pfad == hs.QUELLDATEI or hs.ist_ausgenommen(pfad, stil):
            continue
        text = (repo / pfad).read_text(encoding="utf-8", errors="replace")
        for nummer, zeile in hs.finde_verstoesse(text, stil):
            meldungen.append(f"{pfad}:{nummer}: {zeile[:160]}")

    claude_md = (repo / "CLAUDE.md").read_text(encoding="utf-8")
    if not hs.claude_md_nennt_phrase(claude_md, stil):
        meldungen.append(f"CLAUDE.md: kanonische Phrase fehlt: {hs.kanonische_phrase(stil)!r}")

    for meldung in meldungen:
        print(meldung)
    print(f"verstoesse={len(meldungen)} phrase={hs.kanonische_phrase(stil)!r}")
    return 1 if meldungen else 0


if __name__ == "__main__":
    sys.exit(main())
