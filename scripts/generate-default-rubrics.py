#!/usr/bin/env python3
"""Erzeugt für Testakten ohne rubric.yaml eine belastbare Baseline-Rubrik.

Bestehende Rubriken werden nicht überschrieben. Eine neue Rubrik wird nur
erzeugt, wenn sich ein tatsächlich vorhandenes Marketplace-Plugin eindeutig
aus der Testakten- oder Plugin-Dokumentation bestimmen lässt.

Standard-Checks:
- README vorhanden
- Gesamt-PDF vorhanden
- mindestens drei exportierbare Arbeitsunterlagen vorhanden
"""
from __future__ import annotations


if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TESTAKTEN = REPO / "testakten"
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
SKIP_DIRS = {"formatvorlagen-paradebeispiele", "megaprompts"}

TEMPLATE = '''# Strukturelle Baseline-Rubrik.
# Fallbezogene Inhaltschecks können ergänzend aufgenommen werden.

name: "{name}"
plugin: "{plugin}"

checks:
  - id: r01-readme-vorhanden
    check_type: file_exists
    description: "README.md vorhanden"
    path: "README.md"

  - id: r02-gesamt-pdf-vorhanden
    check_type: file_exists
    description: "Gesamt-PDF gebaut"
    path: "gesamt-pdf/{slug}_gesamt.pdf"

  - id: r03-mindestens-3-arbeitsunterlagen
    check_type: working_file_count
    description: "Mindestens drei exportierbare Arbeitsunterlagen vorhanden"
    min: 3
'''


def load_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def plugin_directory(plugin: dict) -> Path:
    source = (plugin.get("source") or f"./{plugin['name']}").removeprefix("./")
    return REPO / source


def linked_testakten(plugins: list[dict]) -> dict[str, list[str]]:
    """Ordnet Testakten anhand der Links in den Plugin-READMEs zu."""
    mapping: dict[str, list[str]] = {}
    for plugin in plugins:
        readme = plugin_directory(plugin) / "README.md"
        if not readme.is_file():
            continue
        text = readme.read_text(encoding="utf-8", errors="ignore")
        for slug in re.findall(r"\.\./testakten/([^/)]+)/README\.md", text):
            mapping.setdefault(slug, []).append(plugin["name"])
    return mapping


def discover_plugin(testakte_dir: Path, plugins: list[dict], links: dict[str, list[str]]) -> str:
    """Bestimmt das primäre Plugin aus expliziten, vorhandenen Verweisen."""
    names = {plugin["name"] for plugin in plugins}
    readme = testakte_dir / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8", errors="ignore")
        for token in re.findall(r"`([a-z0-9-]+)`", text):
            if token in names:
                return token
    candidates = links.get(testakte_dir.name, [])
    if len(candidates) == 1:
        return candidates[0]
    raise ValueError(
        f"{testakte_dir.relative_to(REPO)}: primäres Plugin nicht eindeutig; "
        f"Kandidaten: {', '.join(candidates) if candidates else 'keine'}"
    )


def main() -> int:
    plugins = load_plugins()
    links = linked_testakten(plugins)
    created = 0
    existing = 0
    errors: list[str] = []
    for d in sorted(TESTAKTEN.iterdir()):
        if not d.is_dir() or d.name in SKIP_DIRS:
            continue
        rubric = d / "rubric.yaml"
        if rubric.exists():
            existing += 1
            continue
        try:
            plugin = discover_plugin(d, plugins, links)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        name = d.name.replace("-", " ").title()
        rubric.write_text(
            TEMPLATE.format(name=name, plugin=plugin, slug=d.name),
            encoding="utf-8",
        )
        created += 1
    print(f"Baseline-Rubriken erzeugt: {created}; vorhanden gelassen: {existing}")
    if errors:
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
