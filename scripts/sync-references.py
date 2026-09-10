#!/usr/bin/env python3
"""Synchronisiert die Repo-Root-Referenzen in die Plugin-Spiegel.

Hintergrund: methodenlehre-deutsches-recht/ und zitierweise-deutsches-recht/
liefern als eigenstaendige ZIPs ihre eigenen References mit. Diese muessen
identisch zur Repo-Root sein, sonst driften die Plugins gegen die Skills,
die in anderen Plugins per relativem Pfad auf die Root-References zeigen.

Aufruf: python3 scripts/sync-references.py
Exit 0 wenn nichts zu tun war oder erfolgreich synchronisiert.
Exit 1 wenn Quelldateien fehlen.
"""
from __future__ import annotations
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PAIRS = [
    (REPO / "references" / "methodik-buergerliches-recht.md",
     REPO / "methodenlehre-buergerliches-recht" / "references" / "methodik-buergerliches-recht.md"),
    (REPO / "references" / "zitierweise.md",
     REPO / "zitierweise-deutsches-recht" / "references" / "zitierweise.md"),
]

# Diese Fachplugins werden einzeln installiert; die Rechtsstandkarte muss
# deshalb auch ohne einen Zugriff auf andere Pluginordner verfügbar sein.
OMNIBUS_PLUGINS = (
    "ki-vo-ai-act-pruefer", "ki-governance", "ki-richtlinie-kanzleien",
    "berufsrecht-ki-vertragspruefung", "datenschutzrecht",
    "datenschutz-sanktionsverfahren-verteidigung", "fachanwalt-it-recht",
    "robotik-recht",
)
PAIRS.extend(
    (REPO / "references" / reference,
     REPO / plugin / "references" / reference)
    for plugin in OMNIBUS_PLUGINS
    for reference in ("digitaler-omnibus-2026.md", "zitierweise.md")
)


def main() -> int:
    changed = 0
    for src, dst in PAIRS:
        if not src.exists():
            print(f"FEHLER: Quelldatei fehlt: {src}", file=sys.stderr)
            return 1
        if not dst.parent.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or src.read_bytes() != dst.read_bytes():
            shutil.copy2(src, dst)
            print(f"sync: {src.relative_to(REPO)} -> {dst.relative_to(REPO)}")
            changed += 1
        else:
            print(f"ok:   {dst.relative_to(REPO)} ist aktuell")
    if changed == 0:
        print("Alle Plugin-Spiegel sind aktuell. Nichts zu tun.")
    else:
        print(f"Synchronisiert: {changed} Datei(en).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
