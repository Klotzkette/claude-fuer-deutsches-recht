#!/usr/bin/env python3
"""Prüft Navigation und Direktdownloads der Markdown-Dokumentation."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from os.path import relpath
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from markdown_it import MarkdownIt
import yaml


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="
MARKDOWN = MarkdownIt("gfm-like")


class ExplicitAnchors(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: set[str] = set()
        self.destinations: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self.anchors.update(value for key, value in attrs if key in {"id", "name"} and value)
            self.destinations.extend(value for key, value in attrs if key == "href" and value)


def markdown_tokens(text: str):
    text = text.removeprefix('\ufeff').replace('\r\n', '\n')
    front = re.match(r'\A---[ \t]*\n(.*?)\n(?:---|\.\.\.)[ \t]*(?:\n|\Z)', text, re.S)
    if front:
        try:
            metadata = yaml.safe_load(front.group(1))
        except yaml.YAMLError:
            metadata = False
        if isinstance(metadata, (dict, list)) or metadata is None:
            text = text[front.end():]
    return MARKDOWN.parse(text)


def markdown_links(tokens) -> list[tuple[str, str]]:
    links = []
    for token in tokens:
        destination = None
        label = []
        for child in token.children or []:
            if child.type == "link_open":
                destination = child.attrGet("href") or ""
                label = []
            elif child.type == "link_close" and destination is not None:
                links.append(("".join(label).strip(), destination))
                destination = None
            elif destination is not None:
                label.append(child.content)
    return links


def explicit_html(tokens) -> ExplicitAnchors:
    html = ExplicitAnchors()
    for token in tokens:
        if token.type == "html_block":
            html.feed(token.content)
        for child in token.children or []:
            if child.type == "html_inline":
                html.feed(child.content)
    html.close()
    return html


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def relative_link(directory: Path, target: Path) -> str:
    return Path(relpath(target, start=directory)).as_posix()


def markdown_download_url(repo_path: str) -> str:
    return DOWNLOAD_BASE + quote(repo_path, safe="/")


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
    tokens = markdown_tokens(text)
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            base = github_slug(tokens[index + 1].content)
            duplicate = counts.get(base, 0)
            counts[base] = duplicate + 1
            anchors.add(base if duplicate == 0 else f"{base}-{duplicate}")
    anchors.update(explicit_html(tokens).anchors)
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
        for label, destination in markdown_links(markdown_tokens(text)):
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
                if target not in anchor_cache:
                    anchor_cache[target] = heading_anchors(target)
                anchors = anchor_cache[target]
                if unquote(fragment) not in anchors:
                    errors.append(f"{repo_relative(path)}: Überschriftenanker fehlt: {destination}")
    return checked_links, checked_anchors


def is_markdown_work_file(destination: str) -> bool:
    path = urlsplit(destination).path.lower()
    if "skills-index" in path.split("/"):
        return False
    name = path.rsplit("/", 1)[-1]
    return (
        name == "skill.md"
        or name.endswith("-werkstatt.md")
        or name.endswith("-schnellstart.md")
    )


def is_markdown_download_target(repo_path: str) -> bool:
    """Entspricht dem Pfadformat der Downloadseite, auch für Quellenhilfen."""
    return (
        re.fullmatch(r"[A-Za-z0-9._/ -]+\.md", repo_path) is not None
        and not repo_path.startswith("/")
        and not {"..", ".git"}.intersection(repo_path.split("/"))
    )


def user_facing_download_docs() -> list[Path]:
    market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    files = {REPO / "README.md"}
    for plugin in market["plugins"]:
        source = str(plugin["source"]).removeprefix("./")
        files.add(REPO / source / "README.md")
    files.update((REPO / "skills-index").glob("*.md"))
    files.update(
        {
            REPO / "SKILLS.md",
            REPO / "ASSET_INDEX.md",
            REPO / "PROMPTLISTE.md",
            REPO / "QUICKSTART.md",
            REPO / "INSTALLATION_EINFACH.md",
            REPO / "docs" / "werkstatt-und-schnellstart-coverage.md",
        }
    )
    return sorted(path for path in files if path.is_file())


def validate_markdown_downloads(errors: list[str]) -> int:
    download_page = REPO / "uebersicht-fachanwaltschaften" / "download.html"
    if not download_page.is_file():
        errors.append("Statische Markdown-Downloadseite fehlt")
    else:
        page_text = download_page.read_text(encoding="utf-8")
        if "downloads/${encodedPath}" not in page_text or "download.click()" not in page_text:
            errors.append("Statische Markdown-Downloadseite ist unvollständig")

    pages_workflow = REPO / ".github" / "workflows" / "pages.yml"
    if not pages_workflow.is_file():
        errors.append("Pages-Workflow für Markdown-Downloads fehlt")
    else:
        workflow_text = pages_workflow.read_text(encoding="utf-8")
        required_fragments = ("-name '*.md'", "_site/downloads", "path: ./_site")
        if not all(fragment in workflow_text for fragment in required_fragments):
            errors.append("Pages-Workflow stellt nicht alle Markdown-Dateien bereit")

    count = 0
    for path in user_facing_download_docs():
        text = path.read_text(encoding="utf-8", errors="ignore")
        tokens = markdown_tokens(text)
        destinations = [destination for _, destination in markdown_links(tokens)]
        destinations.extend(explicit_html(tokens).destinations)
        for destination in destinations:
            if not destination or destination.startswith(("mailto:", "#")):
                continue
            if destination.startswith(DOWNLOAD_BASE):
                continue
            if path.parent == REPO / "skills-index" and not urlsplit(destination).scheme:
                continue
            if is_markdown_work_file(destination):
                errors.append(
                    f"{repo_relative(path)}: Markdown-Arbeitsdatei umgeht den Downloadweg: {destination}"
                )
        for destination in destinations:
            if not destination.startswith(DOWNLOAD_BASE):
                continue
            count += 1
            repo_path = unquote(destination[len(DOWNLOAD_BASE):])
            if not is_markdown_download_target(repo_path):
                errors.append(f"{repo_relative(path)}: unzulässiges Markdown-Downloadziel: {repo_path}")
                continue
            target = (REPO / repo_path).resolve()
            if not target.is_relative_to(REPO.resolve()):
                errors.append(f"{repo_relative(path)}: Markdown-Downloadziel außerhalb des Repositorys: {repo_path}")
            elif not target.is_file():
                errors.append(f"{repo_relative(path)}: Markdown-Downloadziel fehlt: {repo_path}")
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
        prompt_paths = [
            f"{source}/{name}-werkstatt.md",
            f"{source}/{name}-schnellstart.md",
        ]
        for prompt_path in prompt_paths:
            direct = markdown_download_url(prompt_path)
            if direct not in readme_text or direct not in detail_text or direct not in asset_index:
                errors.append(f"{name}: Markdown-Download fehlt in README, Skill-Detailseite oder Asset-Index: {prompt_path}")
        for skill in skills:
            skill_count += 1
            slug = skill.parent.name
            direct = markdown_download_url(f"{source}/skills/{slug}/SKILL.md")
            if direct not in readme_text:
                errors.append(f"{repo_relative(readme)}: Skill-Download fehlt: {slug}")
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
    markdown_downloads = validate_markdown_downloads(errors)
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
        f"{checked_anchors} Anker, {markdown_downloads} echte Markdown-Downloads)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
