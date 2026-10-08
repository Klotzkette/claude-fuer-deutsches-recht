#!/usr/bin/env python3
"""Prueft Menuefuehrung, Einzeldateizugriff und Release-Download-Abdeckung."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from public_release import BLOB_BASE, RAW_BASE, RELEASE_BASE, RELEASE_TAG, REPOSITORY, markdown_download

REPO = Path(__file__).resolve().parent.parent
SKIP_TESTAKTEN = {"formatvorlagen-paradebeispiele", "megaprompts"}
GH_COMMAND_TIMEOUT_SECONDS = 30

PROMPT_SUFFIXES = {
    "vergabestelle-behoerden": "vergabestelle",
    "bieter-unternehmen": "bieter",
    "konkurrenten-rechtsschutz": "konkurrenten",
}

FIXED_ASSETS = {
    "alle-plugins-megazip.zip",
    "alle-skills-markdown.zip",
    "testakten-vergaberecht-werkstatt.zip",
    "alles-komplettpaket.zip",
    "marketplace.json",
    "checksums-sha256.txt",
}


def plugin_names() -> list[str]:
    marketplace = json.loads(
        (REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    return [plugin["name"] for plugin in marketplace["plugins"]]


def testakten_slugs() -> list[str]:
    base = REPO / "testakten"
    return [
        path.name
        for path in sorted(base.iterdir())
        if path.is_dir() and path.name not in SKIP_TESTAKTEN
    ]


def expected_assets(plugins: list[str], testakten: list[str]) -> set[str]:
    assets = set(FIXED_ASSETS)
    for plugin in plugins:
        assets.update(
            {
                f"{plugin}.zip",
                f"{plugin}-skills-markdown.zip",
                f"{plugin}-unified-mini-prompt.md",
            }
        )
    for suffix in PROMPT_SUFFIXES.values():
        assets.add(f"vergaberecht-arbeitsprompt-{suffix}.md")
        assets.add(f"vergaberecht-kurzprompt-{suffix}.md")
    assets.update(f"testakte-{slug}.zip" for slug in testakten)
    assets.update(f"testakte-{slug}-einzelpdfs.zip" for slug in testakten)
    assets.update(f"{slug}_gesamt.pdf" for slug in testakten)
    return assets


def linked_release_assets(text: str) -> set[str]:
    prefix = f"{RELEASE_BASE}/"
    assets: set[str] = set()
    for part in text.split(prefix)[1:]:
        name = part.split(")", 1)[0].split(" ", 1)[0].strip()
        if name:
            assets.add(name)
    return assets


def require(text: str, needle: str, label: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{label}: Link oder Eintrag fehlt: {needle}")


def markdown_link_targets(text: str) -> set[str]:
    """Extrahiert nutzbare Inline-Links, aber keine Bilder, Kommentare oder Codeblöcke."""
    visible = re.sub(r"<!--[\s\S]*?-->", "", text)
    visible = re.sub(r"^[ \t]*(```|~~~)[\s\S]*?^[ \t]*\1[ \t]*$", "", visible, flags=re.MULTILINE)
    targets: set[str] = set()
    pattern = re.compile(
        r"(?<!!)\[[^\]\n]+\]\(\s*(<[^>\n]+>|[^)\s]+)"
        r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
    )
    for match in pattern.finditer(visible):
        target = match.group(1).strip("<>")
        target = unquote(target.split("#", 1)[0])
        if target:
            targets.add(target)
    return targets


def numbered_case_docs(directory: Path) -> list[Path]:
    docs = [
        path
        for path in directory.glob("*.md")
        if re.fullmatch(r"\d+_.+\.md", path.name)
    ]
    return sorted(
        docs,
        key=lambda path: (int(path.name.split("_", 1)[0]), path.name),
    )


def validate_root(expected: set[str], errors: list[str]) -> None:
    path = REPO / "README.md"
    text = path.read_text(encoding="utf-8")
    linked = linked_release_assets(text)
    for asset in sorted(expected - linked):
        errors.append(f"README.md: Release-Datei nicht verlinkt: {asset}")
    for asset in sorted(linked - expected):
        errors.append(f"README.md: unbekannte oder veraltete Release-Datei: {asset}")
    for needle in (
        "[Dateikatalog](#dateikatalog)",
        "[Downloads](#sofort-downloads)",
        "[Vergabestelle](vergabestelle-behoerden/README.md)",
        "[Bieter](bieter-unternehmen/README.md)",
        "[Konkurrent](konkurrenten-rechtsschutz/README.md)",
        "[Skills](SKILLS.md)",
        "[Testakten](testakten/README.md)",
        "[Rechtsprechung](references/leitentscheidungen-anker.md)",
        "Nur der Unified Mini Prompt ist auf höchstens 7.500 Zeichen begrenzt.",
        "unified-mini-prompts/vergabestelle-behoerden.md",
        "unified-mini-prompts/bieter-unternehmen.md",
        "unified-mini-prompts/konkurrenten-rechtsschutz.md",
        "https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/vergaberecht-werkstatt",
        "https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip",
        "/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht",
        "/reload-plugins",
        "https://support.claude.com/en/articles/13837440-use-plugins-in-claude",
    ):
        require(text, needle, "README.md", errors)
    if "/plugin load " in text:
        errors.append("README.md: veralteter Plugin-Ladebefehl vorhanden")


def validate_plugins(plugins: list[str], errors: list[str]) -> None:
    for plugin in plugins:
        readme_path = REPO / plugin / "README.md"
        detail_path = REPO / "skills-index" / f"{plugin}.md"
        readme = readme_path.read_text(encoding="utf-8")
        detail = detail_path.read_text(encoding="utf-8")
        suffix = PROMPT_SUFFIXES[plugin]
        required = (
            "[Repo-Start](../README.md)",
            "[Dateikatalog](../README.md#dateikatalog)",
            "[Vergabestelle](../vergabestelle-behoerden/README.md)",
            "[Bieter](../bieter-unternehmen/README.md)",
            "[Konkurrent](../konkurrenten-rechtsschutz/README.md)",
            "[Alle Skills](../SKILLS.md)",
            "[Testakten](../testakten/README.md)",
            f"../skills-index/{plugin}.md",
            f"../unified-mini-prompts/{plugin}.md",
            f"../vergaberecht-arbeitsprompt-{suffix}.md",
            f"../vergaberecht-kurzprompt-{suffix}.md",
            f"../testakten/megaprompts/{plugin}.md",
            f"{RAW_BASE}/testakten/megaprompts/{plugin}.md",
            f"{RELEASE_BASE}/{plugin}.zip",
            f"{RELEASE_BASE}/{plugin}-skills-markdown.zip",
            f"{RELEASE_BASE}/{plugin}-unified-mini-prompt.md",
            f"/plugin install {plugin}@klotzkette-german-legal-skills",
            "Autarker Kurzprompt mit vertiefter Fallprüfung",
            "Autarker Mini-Schnellstart bis 7.500 Zeichen",
            "## Direkt starten",
            "Kein zusätzlicher Prompt",
            "höchstens drei echte",
            "<details>",
            "</details>",
            "Skills mit Beschreibung und Rohdatei anzeigen",
        )
        for needle in required:
            require(readme, needle, f"{plugin}/README.md", errors)
        if "Autarker Schnellstart bis 7.500 Zeichen" in readme:
            errors.append(
                f"{plugin}/README.md: Kurzprompt wird fälschlich als "
                "7.500-Zeichen-Prompt bezeichnet"
            )
        if readme.count("<details>") != readme.count("</details>"):
            errors.append(f"{plugin}/README.md: aufklappbare Bereiche sind nicht ausgeglichen")

        skills_dir = REPO / plugin / "skills"
        for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
            skill = skill_dir / "SKILL.md"
            if not skill.is_file():
                continue
            rel = f"skills/{skill_dir.name}/SKILL.md"
            require(readme, f"({markdown_download(f'{plugin}/{rel}')})", f"{plugin}/README.md", errors)
            full_rel = f"{plugin}/{rel}"
            require(
                detail,
                markdown_download(full_rel),
                f"skills-index/{plugin}.md",
                errors,
            )
            require(
                detail,
                markdown_download(full_rel),
                f"skills-index/{plugin}.md",
                errors,
            )

        support_files = [REPO / plugin / ".claude-plugin" / "plugin.json"]
        for dirname in ("assets", "references"):
            base = REPO / plugin / dirname
            if base.is_dir():
                support_files.extend(sorted(path for path in base.rglob("*") if path.is_file()))
        for path in support_files:
            rel = path.relative_to(REPO / plugin).as_posix()
            require(readme, f"({rel})", f"{plugin}/README.md", errors)
            require(readme, f"{RAW_BASE}/{plugin}/{rel}", f"{plugin}/README.md", errors)


def validate_testakten(testakten: list[str], errors: list[str]) -> None:
    overview = (REPO / "testakten" / "README.md").read_text(encoding="utf-8")
    numbered_total = 0
    for needle in (
        "[Repo-Start](../README.md)",
        "[Dateikatalog](../README.md#dateikatalog)",
        "[Downloads](../README.md#sofort-downloads)",
        "[Vergabestelle](../vergabestelle-behoerden/README.md)",
        "[Bieter](../bieter-unternehmen/README.md)",
        "[Konkurrent](../konkurrenten-rechtsschutz/README.md)",
    ):
        require(overview, needle, "testakten/README.md", errors)
    require(
        overview,
        f"{RELEASE_BASE}/testakten-vergaberecht-werkstatt.zip",
        "testakten/README.md",
        errors,
    )
    for index, slug in enumerate(testakten):
        pdf_rel = f"testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf"
        require(overview, f"./{slug}/README.md", "testakten/README.md", errors)
        require(overview, f"{RAW_BASE}/{pdf_rel}", "testakten/README.md", errors)
        require(
            overview,
            f"{RELEASE_BASE}/testakte-{slug}.zip",
            "testakten/README.md",
            errors,
        )

        readme_path = REPO / "testakten" / slug / "README.md"
        text = readme_path.read_text(encoding="utf-8")
        label = f"testakten/{slug}/README.md"
        numbered_docs = numbered_case_docs(readme_path.parent)
        numbered_total += len(numbered_docs)
        targets = markdown_link_targets(text)
        for needle in (
            "[Repo-Start](../../README.md)",
            "[Dateikatalog](../../README.md#dateikatalog)",
            "[Downloads](../../README.md#sofort-downloads)",
            "[Testakten-Übersicht](../README.md)",
            f"{RELEASE_BASE}/testakte-{slug}.zip",
            f"{RAW_BASE}/{pdf_rel}",
        ):
            require(text, needle, label, errors)
        if index > 0:
            require(text, f"../{testakten[index - 1]}/README.md", label, errors)
        if index + 1 < len(testakten):
            require(text, f"../{testakten[index + 1]}/README.md", label, errors)
        for numbered_doc in numbered_docs:
            if numbered_doc.name not in targets and f"./{numbered_doc.name}" not in targets:
                errors.append(
                    f"{label}: nummeriertes Aktenstück nicht verlinkt: "
                    f"{numbered_doc.name}"
                )

    count_match = re.search(
        r"insgesamt\s+(\d+)\s+nummerierten Aktenstücken",
        overview,
    )
    if not count_match:
        errors.append(
            "testakten/README.md: Gesamtzahl der nummerierten Aktenstücke fehlt"
        )
    elif int(count_match.group(1)) != numbered_total:
        errors.append(
            "testakten/README.md: angegebene Gesamtzahl "
            f"{count_match.group(1)} stimmt nicht mit {numbered_total} Dateien überein"
        )


def validate_mini_prompts(plugins: list[str], errors: list[str]) -> None:
    text = (REPO / "unified-mini-prompts" / "README.md").read_text(encoding="utf-8")
    require(text, "[Repo-Start](../README.md)", "unified-mini-prompts/README.md", errors)
    require(text, "[Dateikatalog](../README.md#dateikatalog)", "unified-mini-prompts/README.md", errors)
    for needle in (
        "[Vergabestelle](../vergabestelle-behoerden/README.md)",
        "[Bieter](../bieter-unternehmen/README.md)",
        "[Konkurrent](../konkurrenten-rechtsschutz/README.md)",
    ):
        require(text, needle, "unified-mini-prompts/README.md", errors)
    for plugin in plugins:
        require(text, f"./{plugin}.md", "unified-mini-prompts/README.md", errors)
        require(
            text,
            f"{RELEASE_BASE}/{plugin}-unified-mini-prompt.md",
            "unified-mini-prompts/README.md",
            errors,
        )


def validate_skill_indexes(plugins: list[str], errors: list[str]) -> None:
    overview = (REPO / "SKILLS.md").read_text(encoding="utf-8")
    index = (REPO / "skills-index" / "README.md").read_text(encoding="utf-8")
    for needle in (
        "[Dateikatalog](README.md#dateikatalog)",
        "[Vergabestelle](vergabestelle-behoerden/README.md)",
        "[Bieter](bieter-unternehmen/README.md)",
        "[Konkurrent](konkurrenten-rechtsschutz/README.md)",
    ):
        require(overview, needle, "SKILLS.md", errors)
    for needle in (
        "[Dateikatalog](../README.md#dateikatalog)",
        "[Vergabestelle](../vergabestelle-behoerden/README.md)",
        "[Bieter](../bieter-unternehmen/README.md)",
        "[Konkurrent](../konkurrenten-rechtsschutz/README.md)",
    ):
        require(index, needle, "skills-index/README.md", errors)
    for plugin in plugins:
        detail = (REPO / "skills-index" / f"{plugin}.md").read_text(encoding="utf-8")
        for needle in (
            "[Dateikatalog](../README.md#dateikatalog)",
            "[Vergabestelle](../vergabestelle-behoerden/README.md)",
            "[Bieter](../bieter-unternehmen/README.md)",
            "[Konkurrent](../konkurrenten-rechtsschutz/README.md)",
        ):
            require(detail, needle, f"skills-index/{plugin}.md", errors)


def validate_live_assets(expected: set[str], errors: list[str]) -> None:
    try:
        proc = subprocess.run(
            ["gh", "release", "view", RELEASE_TAG, "--repo", REPOSITORY, "--json", "assets"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=False,
            timeout=GH_COMMAND_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        errors.append(
            f"Live-Release-Prüfung nach {GH_COMMAND_TIMEOUT_SECONDS} Sekunden abgebrochen"
        )
        return
    if proc.returncode != 0:
        errors.append(f"Live-Release nicht lesbar: {proc.stderr.strip()}")
        return
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        errors.append(f"Live-Release liefert ungültiges JSON: {exc}")
        return
    remote = {asset["name"] for asset in payload.get("assets", [])}
    for asset in sorted(expected - remote):
        errors.append(f"Aktuelles Release: Datei fehlt: {asset}")
    for asset in sorted(remote - expected):
        errors.append(f"Aktuelles Release: unerwartete Datei: {asset}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--live",
        action="store_true",
        help="vergleicht zusaetzlich die Assets des aktuellen GitHub-Releases",
    )
    args = parser.parse_args()

    plugins = plugin_names()
    testakten = testakten_slugs()
    expected = expected_assets(plugins, testakten)
    errors: list[str] = []
    validate_root(expected, errors)
    validate_plugins(plugins, errors)
    validate_testakten(testakten, errors)
    validate_mini_prompts(plugins, errors)
    validate_skill_indexes(plugins, errors)
    if args.live:
        validate_live_assets(expected, errors)

    if errors:
        print(f"validate-navigation: {len(errors)} Fehler", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    live = " inklusive Live-Release" if args.live else ""
    print(
        f"validate-navigation OK ({len(plugins)} Plugins, {len(testakten)} Testakten, "
        f"{len(expected)} Release-Dateien{live})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
