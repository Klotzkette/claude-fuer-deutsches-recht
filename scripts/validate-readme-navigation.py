#!/usr/bin/env python3
"""Prüft Navigation und Direktdownloads der Markdown-Dokumentation."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from os.path import relpath
from pathlib import Path
from urllib.parse import unquote


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
RAW_BASE = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\n]*)\)")
HEADING_RE = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
HTML_RAW_LINK_RE = re.compile(
    rf'<a\s+([^>]*href="{re.escape(RAW_BASE)}/[^"]+"[^>]*)>',
    re.IGNORECASE,
)


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def relative_link(directory: Path, target: Path) -> str:
    return Path(relpath(target, start=directory)).as_posix()


def link_destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    return value.split(maxsplit=1)[0] if value else ""


def github_slug(heading: str) -> str:
    text = re.sub(r"<[^>]+>", "", heading)
    text = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text).strip().lower()
    kept = []
    for char in text:
        category = unicodedata.category(char)
        if char in "-_" or char.isspace() or category[0] in "LMN":
            kept.append(char)
    return "".join(kept).replace(" ", "-").replace("\t", "-")


def heading_anchors(path: Path) -> set[str]:
    counts: dict[str, int] = {}
    anchors: set[str] = set()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for heading in HEADING_RE.findall(text):
        base = github_slug(heading)
        duplicate = counts.get(base, 0)
        counts[base] = duplicate + 1
        anchors.add(base if duplicate == 0 else f"{base}-{duplicate}")
    return anchors


def validate_markdown_links(errors: list[str]) -> tuple[int, int]:
    markdown_files = sorted(REPO.rglob("*.md"))
    anchor_cache: dict[Path, set[str]] = {}
    checked_links = 0
    checked_anchors = 0
    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if path.name == "README.md" and not re.search(r"^#\s+\S", text, re.MULTILINE):
            errors.append(f"{repo_relative(path)}: sichtbare Hauptüberschrift fehlt")
        for match in MARKDOWN_LINK_RE.finditer(text):
            label = match.group(1).strip()
            destination = link_destination(match.group(2))
            if not label:
                errors.append(f"{repo_relative(path)}: Link ohne sichtbare Beschriftung")
            if not destination:
                errors.append(f"{repo_relative(path)}: Link ohne Ziel")
                continue
            if destination.startswith(("http://", "https://", "mailto:")):
                continue

            checked_links += 1
            base, separator, fragment = destination.partition("#")
            decoded_base = unquote(base.split("?", 1)[0])
            target = path if not decoded_base else (path.parent / decoded_base).resolve()
            try:
                target.relative_to(REPO)
            except ValueError:
                errors.append(f"{repo_relative(path)}: Ziel außerhalb des Repositorys: {destination}")
                continue
            if decoded_base and not target.exists():
                errors.append(f"{repo_relative(path)}: Ziel fehlt: {destination}")
                continue
            if target.is_dir():
                target = target / "README.md"
            if separator and target.is_file() and target.suffix.lower() == ".md":
                checked_anchors += 1
                anchors = anchor_cache.setdefault(target, heading_anchors(target))
                if unquote(fragment) not in anchors:
                    errors.append(f"{repo_relative(path)}: Überschriftenanker fehlt: {destination}")
    return checked_links, checked_anchors


def validate_raw_downloads(errors: list[str]) -> int:
    count = 0
    for path in sorted(REPO.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in HTML_RAW_LINK_RE.finditer(text):
            count += 1
            attributes = match.group(1)
            if not re.search(r"(?:^|\s)download(?:\s*=|\s|$)", attributes, re.IGNORECASE):
                errors.append(f"{repo_relative(path)}: Markdown-Direktlink ohne download-Attribut")
            href = re.search(r'href="([^"]+)"', attributes, re.IGNORECASE)
            if not href:
                continue
            raw_path = unquote(href.group(1).removeprefix(f"{RAW_BASE}/")).split("?", 1)[0]
            if not (REPO / raw_path).is_file():
                errors.append(f"{repo_relative(path)}: Markdown-Direktziel fehlt: {raw_path}")
    return count


def validate_generated_navigation(errors: list[str]) -> tuple[int, int]:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    asset_index = (REPO / "ASSET_INDEX.md").read_text(encoding="utf-8")
    plugin_count = 0
    skill_count = 0
    for plugin in marketplace["plugins"]:
        name = plugin["name"]
        source = (plugin.get("source") or f"./{name}").removeprefix("./")
        directory = REPO / source
        readme = directory / "README.md"
        detail = REPO / "skills-index" / f"{name}.md"
        if not readme.is_file() or not detail.is_file():
            errors.append(f"{name}: Plugin-README oder Skill-Detailseite fehlt")
            continue
        plugin_count += 1
        readme_text = readme.read_text(encoding="utf-8")
        expected_readme_links = [
            relative_link(directory, REPO / "README.md"),
            relative_link(directory, REPO / "SKILLS.md"),
            relative_link(directory, detail),
            relative_link(directory, REPO / "ASSET_INDEX.md"),
            relative_link(directory, REPO / "testakten" / "README.md"),
        ]
        for destination in expected_readme_links:
            if f"]({destination})" not in readme_text and f"]({destination}#was-ist-drin)" not in readme_text:
                errors.append(f"{repo_relative(readme)}: Navigationsziel fehlt: {destination}")
        if "](.)" not in readme_text:
            errors.append(f"{repo_relative(readme)}: Link auf die Plugin-Dateien fehlt")

        if f"]({source}/README.md)" not in asset_index:
            errors.append(f"ASSET_INDEX.md: README-Link für {name} fehlt")
        if f"](skills-index/{name}.md)" not in asset_index:
            errors.append(f"ASSET_INDEX.md: Skill-Link für {name} fehlt")

        skills = sorted((directory / "skills").glob("*/SKILL.md"))
        detail_text = detail.read_text(encoding="utf-8")
        for skill in skills:
            skill_count += 1
            slug = skill.parent.name
            if f"](skills/{slug}/SKILL.md)" not in readme_text:
                errors.append(f"{repo_relative(readme)}: Skill-Link fehlt: {slug}")
            raw_url = f"{RAW_BASE}/{source}/skills/{slug}/SKILL.md"
            direct = f'<a href="{raw_url}" download><code>SKILL.md</code></a>'
            if direct not in detail_text:
                errors.append(f"{repo_relative(detail)}: Direktdownload fehlt: {slug}")
    return plugin_count, skill_count


def validate_root_navigation(errors: list[str]) -> None:
    root_readme = (REPO / "README.md").read_text(encoding="utf-8")
    required = [
        "./SKILLS.md",
        "./skills-index/",
        "./ASSET_INDEX.md",
        "./PROMPTLISTE.md",
        "./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts",
        "./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts",
        "./testakten/README.md",
        "./INSTALLATION_EINFACH.md",
        "./QUICKSTART.md",
        "#was-ist-drin",
        "#schnellstart",
    ]
    for destination in required:
        if f"]({destination})" not in root_readme:
            errors.append(f"README.md: Direktnavigation fehlt: {destination}")


def validate_testakte_navigation(errors: list[str]) -> int:
    count = 0
    for directory in sorted((REPO / "testakten").iterdir()):
        readme = directory / "README.md"
        if not directory.is_dir() or not readme.is_file():
            continue
        text = readme.read_text(encoding="utf-8")
        required = ["../README.md", "../../README.md", "../../ASSET_INDEX.md"]
        for destination in required:
            if f"]({destination})" not in text:
                errors.append(f"{repo_relative(readme)}: Aktennavigation fehlt: {destination}")
        count += 1
    return count


def main() -> int:
    errors: list[str] = []
    checked_links, checked_anchors = validate_markdown_links(errors)
    raw_downloads = validate_raw_downloads(errors)
    plugin_count, skill_count = validate_generated_navigation(errors)
    validate_root_navigation(errors)
    testakte_count = validate_testakte_navigation(errors)
    if errors:
        print(f"validate-readme-navigation: {len(errors)} Fehler", file=sys.stderr)
        for error in errors[:300]:
            print(f"  FEHLER: {error}", file=sys.stderr)
        if len(errors) > 300:
            print(f"  ... und {len(errors) - 300} weitere", file=sys.stderr)
        return 1
    print(
        "validate-readme-navigation OK "
        f"({plugin_count} Plugins, {skill_count} Skills, {testakte_count} Aktenseiten, {checked_links} lokale Links, "
        f"{checked_anchors} Anker, {raw_downloads} Markdown-Direktdownloads)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
