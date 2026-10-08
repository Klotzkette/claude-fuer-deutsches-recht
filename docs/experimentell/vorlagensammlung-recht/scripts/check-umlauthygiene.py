#!/usr/bin/env python3
"""Prüft sichtbaren deutschen Text auf typische ASCII-Umlautersetzungen."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
PATTERN = re.compile(
    r"\b(fuer|ueber|gemaess|maessig|aenderung|beduerf|moeglich|natuerl|"
    r"grosse|grossen|massgeblich|ausschliesslich|verstaerkt|haeufig|haengt|"
    r"haette|persoenlich|oeffentlich|aussergerichtlich|veroeffentlich|"
    r"nuetzlich|zustaendig|gewaehr|geprueft)\b",
    re.IGNORECASE,
)


def link_label(match: re.Match[str]) -> str:
    """Lässt sichtbaren Linktext stehen und entfernt technische Dateilabels."""
    label = match.group(1)
    if re.fullmatch(
        r"[\w./-]+(?:\.(?:md|odt|yaml|yml|py|sh))?/?",
        label,
        re.IGNORECASE,
    ):
        return ""
    return label


def git_dateien() -> list[Path]:
    """Liefert versionierte und neue, nicht ignorierte Markdown-/YAML-Dateien."""
    ausgabe = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
            "--",
            "*.md",
            "*.yaml",
            "*.yml",
        ],
        cwd=REPO,
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8")
    return [REPO / name for name in sorted(filter(None, ausgabe.split("\0")))]


def fundstellen() -> list[tuple[Path, list[str]]]:
    treffer: list[tuple[Path, list[str]]] = []
    for path in git_dateien():
        if " 2." in path.name:
            continue
        zeilen: list[str] = []
        for nummer, line in enumerate(
            path.read_text(encoding="utf-8", errors="ignore").splitlines(),
            start=1,
        ):
            stripped = line.lstrip()
            if path.suffix in {".yaml", ".yml"} and (
                stripped.startswith("#")
                or stripped.startswith("id:")
                or stripped.startswith("- id:")
                or stripped.startswith("path:")
                or stripped.startswith("pattern:")
            ):
                continue
            sichtbar = re.sub(r"\[([^\]]*)\]\([^)]*\)", link_label, line)
            sichtbar = re.sub(r"https?://\S+", "", sichtbar)
            sichtbar = re.sub(r"`[^`]*`", "", sichtbar)
            if PATTERN.search(sichtbar):
                zeilen.append(f"{nummer}:{line}")
        if zeilen:
            treffer.append((path, zeilen[:5]))
    return treffer


def main() -> int:
    print("Suche nach typischen ASCII-Ersatzschreibungen in *.md, *.yaml ...\n")
    treffer = fundstellen()
    if not treffer:
        print("OK: keine typischen ASCII-Ersatzschreibungen gefunden.")
        return 0
    for path, zeilen in treffer:
        print(f"→ {path.relative_to(REPO)}")
        print("\n".join(zeilen))
        print()
    print(
        f"Treffer in {len(treffer)} Datei(en). Bitte sichten und ersetzen, soweit es\n"
        "tatsächlich deutsche Wörter sind (ä/ö/ü/ß-Schreibung erforderlich)."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
