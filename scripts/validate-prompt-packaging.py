#!/usr/bin/env python3
"""Prüft die strikte Trennung von Plugin-, Skill- und Hilfsprompt-Downloads."""

from __future__ import annotations

import io
import json
import sys
import zipfile
from pathlib import Path


PROMPT_SUFFIXES = ("-werkstatt.md", "-schnellstart.md")


def fail(message: str) -> None:
    print(f"validate-prompt-packaging failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def prompt_entries(archive: zipfile.ZipFile) -> list[str]:
    return sorted(name for name in archive.namelist() if name.endswith(PROMPT_SUFFIXES))


def assert_archive_clean(path: Path) -> None:
    if not path.is_file():
        fail(f"Archiv fehlt: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            found = prompt_entries(archive)
    except zipfile.BadZipFile as exc:
        fail(f"Ungültiges ZIP {path}: {exc}")
    if found:
        fail(f"{path}: Hilfsprompts im ZIP gefunden: {', '.join(found)}")


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    dist_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else repo_root / "dist"
    marketplace_path = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else repo_root / ".claude-plugin" / "marketplace.json"
    )
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    plugins = marketplace.get("plugins", [])

    for plugin in plugins:
        name = plugin["name"]
        source = str(plugin.get("source") or f"./{name}").removeprefix("./")
        plugin_dir = repo_root / source
        for suffix in PROMPT_SUFFIXES:
            prompt = plugin_dir / f"{name}{suffix}"
            if not prompt.is_file():
                fail(f"Direkter Markdown-Download fehlt: {prompt}")

        assert_archive_clean(dist_dir / f"{name}.zip")
        assert_archive_clean(dist_dir / "skills-markdown" / f"{name}-skills-markdown.zip")

    combined_path = dist_dir / "skills-markdown" / "alle-skills-markdown.zip"
    if not combined_path.is_file():
        fail(f"Sammelarchiv fehlt: {combined_path}")
    with zipfile.ZipFile(combined_path) as combined:
        for member in combined.infolist():
            if not member.filename.endswith("-skills-markdown.zip"):
                fail(f"{combined_path}: unerwarteter Eintrag {member.filename}")
            with zipfile.ZipFile(io.BytesIO(combined.read(member))) as nested:
                found = prompt_entries(nested)
                if found:
                    fail(
                        f"{combined_path}/{member.filename}: Hilfsprompts gefunden: "
                        f"{', '.join(found)}"
                    )

    print(f"validate-prompt-packaging OK ({len(plugins)} Plugins, keine Hilfsprompts in ZIPs)")


if __name__ == "__main__":
    main()
