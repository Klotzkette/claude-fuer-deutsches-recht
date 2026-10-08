#!/usr/bin/env python3
"""Prüft die Drei-Ordner-Sicht unter `kategorien/`.

Der Ordner `kategorien/` ist bewusst nur ein Navigationsindex. Die
kanonischen Vorlagen bleiben in ihren Rechtsgebietsordnern. Dieser Check
stellt sicher, dass jede Vorlage genau einmal in einer der drei Sichten
verlinkt ist, keine toten Links entstehen und die Zähler im
Kategorie-README stimmen.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import vorlagenordner  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
KATEGORIEN = REPO / "kategorien"

KATEGORIE_ORDNER = {
    "01-vertragliche-vorlagen",
    "02-prozessuale-vorlagen-und-formulare",
    "03-sonstige-vorlagen",
}

LINK_RE = re.compile(r"\]\((?:\.\./){2,3}([^/)]+/[^/)]+)/\)")
COUNT_RE = re.compile(r"\|\s+\[[^\]]+\]\(([^/)]+)/\)\s+\|[^|]*\|\s+(\d+)\s+\|")
ROOT_COUNT_RE = re.compile(
    r"\|\s+\[[^\]]+\]\(kategorien/([^/)]+)/\)\s+\|[^|]*\|\s+(\d+)\s+\|"
)


def vorlagenziele() -> set[str]:
    return {
        ordner.relative_to(REPO).as_posix()
        for ordner in vorlagenordner(REPO)
    }


def pruefe_struktur() -> list[str]:
    fehler: list[str] = []
    if not KATEGORIEN.is_dir():
        return ["kategorien/: Ordner fehlt"]
    if not (KATEGORIEN / "README.md").is_file():
        fehler.append("kategorien/README.md: Datei fehlt")
    vorhanden = {p.name for p in KATEGORIEN.iterdir() if p.is_dir()}
    fehlend = KATEGORIE_ORDNER - vorhanden
    extra = vorhanden - KATEGORIE_ORDNER
    for name in sorted(fehlend):
        fehler.append(f"kategorien/{name}/: Kategorieordner fehlt")
    for name in sorted(extra):
        fehler.append(f"kategorien/{name}/: unerwarteter Kategorieordner")
    for name in sorted(KATEGORIE_ORDNER & vorhanden):
        ordner = KATEGORIEN / name
        readme = ordner / "README.md"
        if not readme.is_file():
            fehler.append(f"kategorien/{name}/README.md: Datei fehlt")
        for datei in sorted(ordner.iterdir()):
            if datei.is_file() and datei.name != "README.md":
                fehler.append(
                    f"{datei.relative_to(REPO)}: Kategorieordner darf neben README.md nur Rechtsgebietsordner enthalten"
                )
            elif datei.is_dir():
                unter_readme = datei / "README.md"
                if not unter_readme.is_file():
                    fehler.append(f"{unter_readme.relative_to(REPO)}: Datei fehlt")
                for unterdatei in sorted(datei.iterdir()):
                    if unterdatei.name != "README.md":
                        fehler.append(
                            f"{unterdatei.relative_to(REPO)}: Rechtsgebietsordner darf nur README.md enthalten"
                        )
    return fehler


def indexlinks() -> dict[str, list[str]]:
    links: dict[str, list[str]] = {}
    for name in sorted(KATEGORIE_ORDNER):
        readme = KATEGORIEN / name / "README.md"
        texte = []
        if readme.is_file():
            texte.append(readme.read_text(encoding="utf-8"))
        for unter_readme in sorted((KATEGORIEN / name).glob("*/README.md")):
            texte.append(unter_readme.read_text(encoding="utf-8"))
        links[name] = LINK_RE.findall("\n".join(texte))
    return links


def zaehler_aus_root_readme() -> dict[str, int]:
    readme = KATEGORIEN / "README.md"
    if not readme.is_file():
        return {}
    text = readme.read_text(encoding="utf-8")
    return {ordner: int(zahl) for ordner, zahl in COUNT_RE.findall(text)}


def zaehler_aus_repo_readme() -> dict[str, int]:
    readme = REPO / "README.md"
    if not readme.is_file():
        return {}
    text = readme.read_text(encoding="utf-8")
    return {ordner: int(zahl) for ordner, zahl in ROOT_COUNT_RE.findall(text)}


def main() -> int:
    fehler = pruefe_struktur()
    soll = vorlagenziele()
    links_nach_kategorie = indexlinks()
    alle_links = [ziel for links in links_nach_kategorie.values() for ziel in links]
    ist = set(alle_links)

    for ziel in sorted(ist - soll):
        fehler.append(f"kategorien/: Linkziel ist kein Vorlagenordner: {ziel}")
    for ziel in sorted(soll - ist):
        fehler.append(f"kategorien/: Vorlage fehlt in Drei-Ordner-Sicht: {ziel}")

    zaehler = Counter(alle_links)
    for ziel, anzahl in sorted(zaehler.items()):
        if anzahl > 1:
            fehler.append(f"kategorien/: Vorlage mehrfach verlinkt ({anzahl}x): {ziel}")

    root_counts = zaehler_aus_root_readme()
    repo_counts = zaehler_aus_repo_readme()
    for name in sorted(KATEGORIE_ORDNER):
        aktuell = len(links_nach_kategorie.get(name, []))
        angegeben = root_counts.get(name)
        if angegeben is None:
            fehler.append(f"kategorien/README.md: Zähler für {name} fehlt")
        elif angegeben != aktuell:
            fehler.append(
                f"kategorien/README.md: Zähler für {name} ist {angegeben}, erwartet {aktuell}"
            )
        repo_angegeben = repo_counts.get(name)
        if repo_angegeben is None:
            fehler.append(f"README.md: Zähler für kategorien/{name} fehlt")
        elif repo_angegeben != aktuell:
            fehler.append(
                f"README.md: Zähler für kategorien/{name} ist {repo_angegeben}, erwartet {aktuell}"
            )

    if fehler:
        print(f"check-kategorien-index: FEHLER ({len(fehler)} Probleme):")
        for eintrag in fehler:
            print(f"  {eintrag}")
        return 1
    print(
        "check-kategorien-index OK "
        f"({len(soll)} Vorlagen, {len(KATEGORIE_ORDNER)} Kategorieordner)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
