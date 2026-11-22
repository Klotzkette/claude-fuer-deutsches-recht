#!/usr/bin/env python3
"""Prüft Navigation und Direktdownloads der Markdown-Dokumentation."""

from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser
from os.path import relpath
from pathlib import Path

from prompt_profiles import formats, standalone_kinds
from release_routing import RELEASE_BASE, plugin_asset_url
from urllib.parse import parse_qs, quote, unquote, urlsplit

from markdown_it import MarkdownIt
import yaml


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="
CANONICAL_REPO_BLOB_BASE = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/"
REPOSITORY_URL_PREFIXES = {
    "github.com": ("blob/main/", "tree/main/"),
    "raw.githubusercontent.com": ("main/", "refs/heads/main/"),
}
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
        if tag == "img":
            self.destinations.extend(value for key, value in attrs if key == "src" and value)


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
    text = heading.strip().lower()
    kept = []
    for char in text:
        category = unicodedata.category(char)
        if char in "-_" or char.isspace() or category[0] in "LMN":
            kept.append(char)
    return "".join(kept).replace(" ", "-").replace("\t", "-")


def heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    text = path.read_text(encoding="utf-8", errors="ignore")
    tokens = markdown_tokens(text)
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            heading = "".join(child.content for child in tokens[index + 1].children
                              if child.type in {"text", "code_inline"})
            base = github_slug(heading)
            slug = base
            duplicate = 0
            while slug in anchors:
                duplicate += 1
                slug = f"{base}-{duplicate}"
            anchors.add(slug)
    anchors.update(explicit_html(tokens).anchors)
    return anchors


def repository_markdown_files() -> list[Path]:
    excluded = {".git", ".venv", "venv", "node_modules", "__pycache__", ".cache", "dist", "release-staging"}
    files = []
    for directory, children, names in os.walk(REPO):
        children[:] = [name for name in children if name not in excluded]
        files.extend(Path(directory) / name for name in names if name.endswith(".md"))
    return sorted(files)


def internal_link(path: Path, destination: str) -> tuple[Path, str] | None:
    url = urlsplit(destination)
    fragment = unquote(url.fragment)
    if not url.netloc and not url.scheme:
        relative = unquote(url.path)
        if relative.startswith("/"):
            return REPO / relative.lstrip("/"), fragment
        return (path.parent / relative if relative else path), fragment

    if url.hostname == "klotzkette.github.io" and url.path.startswith("/claude-fuer-deutsches-recht/"):
        relative = unquote(url.path.removeprefix("/claude-fuer-deutsches-recht/"))
        if relative == "download.html" or relative.startswith("downloads/"):
            target = (relative.removeprefix("downloads/") if relative.startswith("downloads/")
                      else parse_qs(url.query).get("path", [""])[0])
            if not is_markdown_download_target(target):
                raise ValueError(f"unzulässiges Markdown-Downloadziel: {target}")
            return REPO / target, ""
        return REPO / "uebersicht-fachanwaltschaften" / (relative or "index.html"), fragment

    # Nur URLs auf main spiegeln den aktuellen Checkout. Tags und feste
    # Commit-Links beziehen sich auf einen anderen Stand.
    parts = url.path.split("/", 3)
    if len(parts) == 4 and parts[1].lower() == "klotzkette" and parts[2].lower() == "claude-fuer-deutsches-recht":
        for prefix in REPOSITORY_URL_PREFIXES.get(url.hostname, ()):
            if parts[3].startswith(prefix):
                return REPO / unquote(parts[3][len(prefix):]), fragment
    return None


def validate_markdown_links(errors: list[str], plugin_urls: dict[str, str] | None = None) -> tuple[int, int]:
    markdown_files = repository_markdown_files()
    anchor_cache: dict[Path, set[str]] = {}
    checked_links = 0
    checked_anchors = 0
    for path in markdown_files:
        release_notes = path.is_relative_to(REPO / "docs" / "releases")
        text = path.read_text(encoding="utf-8", errors="ignore")
        if path.name == "README.md" and not re.search(r"^#\s+\S", text, re.MULTILINE):
            errors.append(f"{repo_relative(path)}: sichtbare Hauptüberschrift fehlt")
        # Ohne Linksyntax oder unsere kanonischen Domains gibt es kein lokales
        # Ziel. Große reine Fachtexte müssen dann nicht als GFM geparst werden.
        if "[" not in text and "<" not in text and "github" not in text.lower():
            continue
        tokens = markdown_tokens(text)
        links = markdown_links(tokens)
        for label, _ in links:
            if not label:
                errors.append(f"{repo_relative(path)}: Link ohne sichtbare Beschriftung")
        destinations = [destination for _, destination in links]
        destinations.extend(explicit_html(tokens).destinations)
        destinations.extend(child.attrGet("src") or "" for token in tokens
                            for child in token.children or [] if child.type == "image")
        for destination in destinations:
            if not destination:
                errors.append(f"{repo_relative(path)}: Link ohne Ziel")
                continue
            if plugin_urls and not release_notes and destination.startswith(
                (RELEASE_BASE + "/latest/download/", RELEASE_BASE + "/download/")
            ):
                url = urlsplit(destination)
                asset = unquote(url.path.rsplit("/", 1)[-1])
                expected = plugin_urls.get(asset)
                if expected and unquote(url._replace(query="", fragment="").geturl()) != expected:
                    errors.append(f"{repo_relative(path)}: veralteter Plugin-Download: {destination} (aktuell: {expected})")
            try:
                local = internal_link(path, destination)
            except ValueError as exc:
                errors.append(f"{repo_relative(path)}: {exc}")
                continue
            if local is None:
                continue
            checked_links += 1
            target, fragment = local
            target = target.resolve()
            try:
                target.relative_to(REPO)
            except ValueError:
                errors.append(f"{repo_relative(path)}: Ziel außerhalb des Repositorys: {destination}")
                continue
            if not target.exists():
                errors.append(f"{repo_relative(path)}: Ziel fehlt: {destination}")
                continue
            if target.is_dir():
                target = target / "README.md"
                if fragment and not target.is_file():
                    errors.append(f"{repo_relative(path)}: Verzeichnis ohne README für Sprungmarke: {destination}")
                    continue
                if fragment.lower() == "readme":
                    continue
            if fragment and target.is_file() and target.suffix.lower() == ".md":
                checked_anchors += 1
                lines = re.fullmatch(r"L([1-9]\d*)(?:-L([1-9]\d*))?", fragment)
                if lines:
                    first, last = lines.groups()
                    if not int(first) <= int(last or first) <= len(target.read_bytes().splitlines()):
                        errors.append(f"{repo_relative(path)}: Zeilenbereich fehlt: {destination}")
                    continue
                if target not in anchor_cache:
                    anchor_cache[target] = heading_anchors(target)
                anchors = anchor_cache[target]
                if fragment not in anchors:
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
        or name.endswith("-hauptproblem.md")
    )


def is_markdown_download_target(repo_path: str) -> bool:
    """Akzeptiert die von GitHub Pages bereitgestellten Dateinamen und Endungen."""
    if re.fullmatch(r"[A-Za-z0-9._/ -]+\.(?:md|txt)", repo_path) is None:
        return False
    if {"", ".", "..", ".git"}.intersection(repo_path.split("/")):
        return False
    # Die Pages-Ausgabe umfasst auch eigenständige Prompts in Unterordnern.
    # Publikationsprofile bestimmen die Pflichtlinks der generierten Kataloge.
    return repo_path.endswith((".md", "-werkstatt.txt", "-schnellstart.txt", "-hauptproblem.txt"))


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
            REPO / "SCHWERPUNKTE.md",
            REPO / "QUALITY.md",
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


def marketplace_note_errors(text: str, expected_count: int) -> list[str]:
    block = re.search(
        r"<!-- BEGIN direkt-loslegen \(autogen\) -->(.*?)<!-- END direkt-loslegen \(autogen\) -->",
        text, flags=re.S,
    )
    if not block:
        return []
    errors = []
    for count in re.findall(r"Marketplace mit (\d+) Plugins", block[1]):
        if int(count) != expected_count:
            errors.append(f"Marketplace-Hinweis nennt {count} statt {expected_count} Plugins")
    if "Wer alle Plugins auf einmal will" in block[1]:
        errors.append("Sammelpaket wird ohne Abgrenzung zum veröffentlichten Stand angeboten")
    return errors


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
        errors.extend(
            f"{repo_relative(readme)}: {message}"
            for message in marketplace_note_errors(readme_text, len(marketplace["plugins"]))
        )
        readme_destinations = {
            destination for label, destination in markdown_links(markdown_tokens(readme_text)) if label
        }
        expected_readme_links = [
            relative_link(directory, REPO / "README.md"),
            relative_link(directory, REPO / "SKILLS.md"),
            relative_link(directory, detail),
            relative_link(directory, REPO / "ASSET_INDEX.md"),
        ]
        if standalone_kinds(name):
            expected_readme_links.append(relative_link(directory, REPO / "testakten" / "README.md"))
        for destination in expected_readme_links:
            target = (directory / destination).resolve().relative_to(REPO.resolve()).as_posix()
            canonical = CANONICAL_REPO_BLOB_BASE + quote(target, safe="/")
            accepted = {destination, destination + "#was-ist-drin", canonical, canonical + "#was-ist-drin"}
            if readme_destinations.isdisjoint(accepted):
                errors.append(f"{repo_relative(readme)}: Navigationsziel fehlt: {destination}")
        if "." not in readme_destinations:
            errors.append(f"{repo_relative(readme)}: Link auf die Plugin-Dateien fehlt")

        if f"]({source}/README.md)" not in asset_index:
            errors.append(f"ASSET_INDEX.md: README-Link für {name} fehlt")
        if f"](skills-index/{name}.md)" not in asset_index:
            errors.append(f"ASSET_INDEX.md: Skill-Link für {name} fehlt")

        skills = sorted((directory / "skills").glob("*/SKILL.md"))
        detail_text = detail.read_text(encoding="utf-8")
        prompt_paths = [f"{source}/{name}-{kind}.{ext}"
                        for kind in standalone_kinds(name) for ext in formats(name)]
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
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    plugin_urls = {plugin["name"] + ".zip": plugin_asset_url(plugin["name"], root=REPO) for plugin in plugins}
    checked_links, checked_anchors = validate_markdown_links(errors, plugin_urls)
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
