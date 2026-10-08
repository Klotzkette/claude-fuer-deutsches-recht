#!/usr/bin/env python3
"""Prueft die technischen Grenzen der oeffentlichen Einbettung offline."""

import json
import re
from pathlib import Path

from public_release import DOWNLOAD_BASE, PROMPT_SUFFIXES, PUBLIC_MARKETPLACE, ROOT, VERSION, canonical_prompt, with_working_downloads
from testakte_notices import README_NOTICE, with_case_warnings


def main() -> int:
    errors = []
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    expected_counts = dict(zip(PROMPT_SUFFIXES, (122, 113, 20)))
    if {plugin["name"] for plugin in marketplace["plugins"]} != set(PROMPT_SUFFIXES):
        errors.append("Marketplace: genau drei Rollen erforderlich")
    if marketplace["name"] != "vergaberecht-werkstatt":
        errors.append("Lokaler Marketplace-Name stimmt nicht")
    for plugin in marketplace["plugins"]:
        role = plugin["name"]
        if role not in PROMPT_SUFFIXES:
            continue
        if plugin["source"] != f"./{role}" or plugin["version"] != VERSION:
            errors.append(f"{role}: relative Quelle oder Version stimmt nicht")
        manifest = json.loads((ROOT / role / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        if manifest["name"] != role or manifest["version"] != VERSION:
            errors.append(f"{role}: Plugin-Identitaet stimmt nicht")
        if manifest["author"] != {"name": "Klotzkette", "email": "39582916+Klotzkette@users.noreply.github.com"}:
            errors.append(f"{role}: Autor stimmt nicht")
        skills = list((ROOT / role / "skills").glob("*/SKILL.md"))
        if len(skills) != expected_counts[role]:
            errors.append(f"{role}: unerwartete Skillanzahl {len(skills)}")
        for path in (ROOT / role / "skills").rglob("*"):
            if re.search(r"schnellstart|megaprompt|miniprompt", path.name, re.I):
                errors.append(f"{path.relative_to(ROOT)}: Promptpfad unter skills")
        for kind in ("werkstatt", "schnellstart"):
            target = ROOT / role / f"{role}-{kind}.md"
            source = (
                ROOT / f"vergaberecht-arbeitsprompt-{PROMPT_SUFFIXES[role]}.md"
                if kind == "werkstatt" else ROOT / "unified-mini-prompts" / f"{role}.md"
            )
            expected = canonical_prompt(source.read_text(encoding="utf-8"), mini=kind == "schnellstart")
            if kind == "schnellstart":
                if len(source.read_bytes()) > 7500:
                    errors.append(f"{source.relative_to(ROOT)}: ueber 7500 Bytes")
            if not target.is_file() or target.read_text(encoding="utf-8") != expected:
                errors.append(f"{target.relative_to(ROOT)}: nicht synchron zur Quelle")
            readme = (ROOT / role / "README.md").read_text(encoding="utf-8")
            url = f"{DOWNLOAD_BASE}/{role}/{role}-{kind}.md"
            if f'href="{url}" download=' not in readme:
                errors.append(f"{role}: HTML-Dateidownload fuer {kind} fehlt")
        if f"/plugin install {role}@{PUBLIC_MARKETPLACE}" not in readme:
            errors.append(f"{role}: oeffentlicher Installationsnamensraum fehlt")

    docs = [ROOT / "README.md", ROOT / "SKILLS.md", ROOT / "testakten/README.md"]
    docs += [ROOT / role / "README.md" for role in PROMPT_SUFFIXES]
    docs += list((ROOT / "testakten").glob("*/README.md"))
    docs += list((ROOT / "skills-index").glob("*.md"))
    for path in docs:
        text = path.read_text(encoding="utf-8")
        if text != with_case_warnings(text):
            errors.append(f"{path.relative_to(ROOT)}: Warnhinweis vor Downloadgruppe fehlt")
        if text != with_working_downloads(text, path):
            errors.append(f"{path.relative_to(ROOT)}: Arbeitsdatei umgeht den oeffentlichen Downloadweg")
    if not (ROOT / "testakten/README.txt").read_text(encoding="utf-8").startswith(README_NOTICE):
        errors.append("testakten/README.txt: Warnhinweis fehlt")

    private = "Klotzkette/" + "vergaberecht-werkstatt"
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if not path.is_file() or path.suffix not in {".md", ".py", ".mjs", ".json", ".yml", ".sh"}:
            continue
        if rel.parts[0] in {"dist", ".venv", "audits"} or "provenance" in path.name or path.name == "source-import.json":
            continue
        text = path.read_text(encoding="utf-8")
        if f"github.com/{private}" in text or f"raw.githubusercontent.com/{private}" in text:
            errors.append(f"{rel}: privates Downloadziel")
        for target in re.findall(r"https://(?:github.com|raw.githubusercontent.com)/Klotzkette/claude-fuer-deutsches-recht/(?:blob/|tree/)?main/[^\s)\"<>]+", text):
            if "/main/vergaberecht-werkstatt" not in target:
                errors.append(f"{rel}: Komponentenpraefix fehlt: {target}")
    for error in errors:
        print(f"FEHLER: {error}")
    print(f"validate-public-integration: {len(errors)} Fehler; 3 Rollen, 255 Skills")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
