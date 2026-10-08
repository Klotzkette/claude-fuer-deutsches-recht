#!/usr/bin/env python3
"""Sperrt Bedien- und Fortsetzungsregressionen der drei Vergaberechtsrollen."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ROLE_FILES = {
    "vergabestelle-behoerden": {
        "start": "assets/templates/startbildschirm-applet-dashboard.md",
        "folder": "assets/templates/ordnerfall-startprotokoll.md",
        "dashboard": "assets/templates/vk-olg-streitdashboard.md",
        "orchestrator": "skills/vergabe-os-master-orchestrator/SKILL.md",
        "legacy": "skills/legacy-systeme-integration/SKILL.md",
    },
    "bieter-unternehmen": {
        "start": "assets/templates/startbildschirm-applet-dashboard.md",
        "folder": "assets/templates/ordnerfall-startprotokoll.md",
        "dashboard": "assets/templates/vk-olg-streitdashboard.md",
        "orchestrator": "skills/vergabe-os-master-orchestrator/SKILL.md",
        "legacy": "skills/legacy-systeme-integration/SKILL.md",
    },
    "konkurrenten-rechtsschutz": {
        "start": "assets/templates/startbildschirm-konkurrenten-dashboard.md",
        "folder": "assets/templates/ordnerfall-startprotokoll.md",
        "dashboard": "assets/templates/streitfall-dashboard-konkurrent.md",
        "orchestrator": "skills/konkurrenzrechtsschutz-orchestrator/SKILL.md",
        "legacy": "skills/legacy-systeme-integration/SKILL.md",
    },
}

ROLE_STARTERS = {
    "vergabestelle-behoerden": "Neuer Vergabestellenfall.",
    "bieter-unternehmen": "Neue Bewerbung.",
    "konkurrenten-rechtsschutz": "Neuer Konkurrentenfall.",
}

ROLE_FIRST_VIEW = {
    "vergabestelle-behoerden": "Lage | Rot | Akte | Rechtsweiche | Jetzt",
    "bieter-unternehmen": "Lage | Rot | Angebot | Rechtsweiche | Jetzt",
    "konkurrenten-rechtsschutz": "Lage | Rot | Angriff | Rechtsweiche | Jetzt",
}

PROMPT_SUFFIX = {
    "vergabestelle-behoerden": "vergabestelle",
    "bieter-unternehmen": "bieter",
    "konkurrenten-rechtsschutz": "konkurrenten",
}

REQUIRED = {
    "start": (
        "## Bedienprinzip",
        "## Intake-Kacheln",
        "## Arbeitsstatus",
        "## Antwortstandard",
        "## Schnellwahl",
        "## Stabiler Großaktenmodus",
        "## Applet-Suite",
        "## Output-Menü",
        "## Nutzungscheck",
        "genau ein",
        "offen",
    ),
    "folder": (
        "## 1. Fallkarte",
        "## 2. Quelleninventar",
        "## 3. Verarbeitungsstatus",
        "## 4. Fristenampel",
        "## 5. Output-Weiche",
        "## 6. Schlusskontrolle",
        "Hash geprüft",
        "Nächster Lauf",
    ),
    "dashboard": (
        "## Kurz-Cockpit",
        "## Streitfall-Applets",
        "## Abschlussstatus",
        "Akteneinsicht",
        "OLG",
        "Kostenrisiko",
        "Nächster Schritt",
    ),
    "orchestrator": (
        "## 90-Sekunden-Erstantwort",
        "## Null-Konfigurations-Vertrag",
        "## Routingbudget",
        "## Ordnerfall-Kaltstart ohne Skillwahl",
        "## Stabiler Großakten- und Fortsetzungsmodus",
        "Höchstens drei echte Blockerfragen",
        "höchstens drei Fachskills",
        "50 Dateien",
        "250 MB",
        "20 Dateien",
        "100 MB",
        "Checkpoint-Register",
    ),
    "legacy": (
        "## Erste 90 Sekunden",
        "## Last- und Fortsetzungsregel",
        "50 Dateien",
        "250 MB",
        "20 Dateien",
        "100 MB",
        "nicht erneut auslesen",
        "nie automatisch wiederholen",
    ),
}

POST_INVENTORY_SKILLS = {
    "vergabestelle-behoerden/skills/orientierung-mandat-anwaltliche-vertiefung/SKILL.md": (
        "folgt auf eine dokumentierte Erstinventur",
        "nicht der Einstieg für rohe Ordner oder ZIP-Dateien",
    ),
    "bieter-unternehmen/skills/kaltstart-triage/SKILL.md": (
        "folgt auf eine dokumentierte Erstinventur",
        "nicht der Einstieg für rohe Ordner oder ZIP-Dateien",
    ),
    "bieter-unternehmen/skills/mandat-triage-vergaberecht/SKILL.md": (
        "folgt auf eine dokumentierte Erstinventur",
        "nicht der Einstieg für rohe Ordner oder ZIP-Dateien",
    ),
    "bieter-unternehmen/skills/orientierung-mandat-anwaltliche-vertiefung/SKILL.md": (
        "folgt auf eine dokumentierte Erstinventur",
        "nicht der Einstieg für rohe Ordner oder ZIP-Dateien",
    ),
}

FORBIDDEN_VISIBLE_PHRASES = (
    "Bedienhandlungspunkt",
    "Bietergemeinschaft-Mitglied",
    "Kunden-Systemschritt",
    "Preis-only",
)


def duplicate_headings(text: str) -> list[str]:
    seen: set[tuple[int, str]] = set()
    duplicates: list[str] = []
    for level, title in re.findall(r"^(#{1,6})\s+(.+?)\s*$", text, flags=re.MULTILINE):
        key = (len(level), title.casefold())
        if key in seen:
            duplicates.append(title)
        seen.add(key)
    return duplicates


def main() -> int:
    errors: list[str] = []
    checked = 0
    for plugin, files in ROLE_FILES.items():
        for kind, relative in files.items():
            path = ROOT / plugin / relative
            label = path.relative_to(ROOT)
            if not path.is_file():
                errors.append(f"{label}: Datei fehlt")
                continue
            checked += 1
            text = path.read_text(encoding="utf-8")
            for marker in REQUIRED[kind]:
                if marker not in text:
                    errors.append(f"{label}: Bedienmarker fehlt: {marker}")
            duplicates = duplicate_headings(text)
            if duplicates:
                errors.append(f"{label}: doppelte Überschriften: {', '.join(duplicates)}")
            if kind in {"start", "folder", "dashboard"}:
                h1_count = len(re.findall(r"^#\s+\S", text, flags=re.MULTILINE))
                if h1_count != 1:
                    errors.append(f"{label}: genau eine Hauptüberschrift erwartet, gefunden: {h1_count}")
            for phrase in FORBIDDEN_VISIBLE_PHRASES:
                if phrase in text:
                    errors.append(f"{label}: veraltete Bedienphrase: {phrase}")

        readme = (ROOT / plugin / "README.md").read_text(encoding="utf-8")
        mega = readme.find("<!-- BEGIN megaprompt-und-vorlagen (autogen) -->")
        skills = readme.find("<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->")
        if mega == -1 or skills == -1 or mega > skills:
            errors.append(f"{plugin}/README.md: Werkstattprompt muss vor dem Skill-Katalog stehen")

        skill_count = sum(
            1
            for skill_dir in (ROOT / plugin / "skills").iterdir()
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file()
        )
        if not any(
            count_label in readme
            for count_label in (f"{skill_count} Skills", f"{skill_count} Kernskills")
        ):
            errors.append(
                f"{plugin}/README.md: sichtbare Skillzahl stimmt nicht mit {skill_count} überein"
            )
        if "kein zusätzlicher prompt" not in readme.casefold():
            errors.append(f"{plugin}/README.md: Plugin-Autarkie im Schnellstart fehlt")
        if ROLE_STARTERS[plugin] not in readme:
            errors.append(f"{plugin}/README.md: rollenfester Startsatz fehlt")
        install_command = f"/plugin install {plugin}@klotzkette-german-legal-skills"
        if install_command not in readme:
            errors.append(f"{plugin}/README.md: Marketplace-Installationsbefehl fehlt")
        if "/plugin load " in readme:
            errors.append(f"{plugin}/README.md: veralteter Plugin-Ladebefehl vorhanden")

        suffix = PROMPT_SUFFIX[plugin]
        prompt_paths = (
            ROOT / f"vergaberecht-arbeitsprompt-{suffix}.md",
            ROOT / f"vergaberecht-kurzprompt-{suffix}.md",
            ROOT / "testakten" / "megaprompts" / f"{plugin}.md",
            ROOT / "unified-mini-prompts" / f"{plugin}.md",
        )
        for prompt_path in prompt_paths:
            prompt_label = prompt_path.relative_to(ROOT)
            prompt_text = prompt_path.read_text(encoding="utf-8") if prompt_path.is_file() else ""
            if ROLE_STARTERS[plugin] not in prompt_text:
                errors.append(f"{prompt_label}: rollenfester Startsatz fehlt")
            if ROLE_FIRST_VIEW[plugin] not in prompt_text:
                errors.append(f"{prompt_label}: Fünf-Zeilen-Einstieg fehlt")
            if "höchstens drei" not in prompt_text:
                errors.append(f"{prompt_label}: Blocker- oder Routinggrenze fehlt")
            if prompt_path.parent.name != "unified-mini-prompts" and "## Null-Konfigurations-Start" not in prompt_text:
                errors.append(f"{prompt_label}: Null-Konfigurations-Start fehlt")

    for relative, markers in POST_INVENTORY_SKILLS.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        for marker in markers:
            if marker.casefold() not in text.casefold():
                errors.append(f"{relative}: Zuständigkeitsgrenze fehlt: {marker}")

    if errors:
        print(f"validate-workflow-usability: {len(errors)} Fehler", file=sys.stderr)
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        return 1
    print(
        "validate-workflow-usability OK "
        f"({checked} Bedienflächen, 3 Plugin-Menüs, {len(POST_INVENTORY_SKILLS)} Triagegrenzen)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
