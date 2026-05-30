#!/usr/bin/env python3
"""Fuegt in jede <plugin>/README.md ganz oben (direkt nach dem H1) eine
prominente 'Sofort-Download'-Sektion ein.

Inhalt der Sektion:
- Plugin-ZIP-Direktdownload (immer, fuer ALLE Plugins)
- Pro zugeordnete Testakte: ZIP-Download und Gesamt-PDF-Lesen

Quelle der Akten-Zuordnung: jede testakten/<slug>/README.md, die das Plugin per
Backtick (`plugin-name`) referenziert. Identisch zur Logik in
inject-plugin-testakten-section.py.

Idempotent ueber HTML-Marker. Position: ZWISCHEN H1 und der Testakten-Sektion.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN_DIR = REPO_ROOT / "testakten"

MARKER_BEGIN = "<!-- BEGIN plugin-sofort-download-section (autogen) -->"
MARKER_END = "<!-- END plugin-sofort-download-section (autogen) -->"
TESTAKTEN_MARKER_BEGIN = "<!-- BEGIN plugin-testakten-section (autogen) -->"

RELEASE_BASE = (
    "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"
)

H1_RE = re.compile(r"^# .+$", re.MULTILINE)


def discover_mapping() -> dict[str, list[str]]:
    """Lese alle testakten/*/README.md und sammle Plugin->Akten-Verbindungen
    ueber Backtick-Erwaehnungen `plugin-name`."""
    mapping: dict[str, list[str]] = {}
    if not TESTAKTEN_DIR.exists():
        return {}
    marketplace = json.loads(
        (REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugin_names = [p["name"] for p in marketplace["plugins"]]
    plugin_set = set(plugin_names)

    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir():
            continue
        readme = sub / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        for name in plugin_set:
            if f"`{name}`" in text:
                mapping.setdefault(name, []).append(sub.name)
    return mapping


def get_akte_title(akte_slug: str) -> str:
    """Lese den H1-Titel aus testakten/<slug>/README.md."""
    readme = TESTAKTEN_DIR / akte_slug / "README.md"
    if not readme.exists():
        return akte_slug
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return akte_slug


def build_section(plugin_name: str, akten_slugs: list[str]) -> str:
    lines: list[str] = []
    lines.append(MARKER_BEGIN)
    lines.append("## \u2b07\ufe0f Sofort-Downloads")
    lines.append("")
    lines.append("Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).")
    lines.append("")
    lines.append("### Plugin als ZIP")
    lines.append("")
    lines.append("| Inhalt | Download |")
    lines.append("| --- | --- |")
    lines.append(
        f"| **Dieses Plugin** (`{plugin_name}`) | "
        f"[`{plugin_name}.zip`]({RELEASE_BASE}/{plugin_name}.zip) |"
    )
    lines.append("")

    if akten_slugs:
        lines.append("### Demonstrations-Akten")
        lines.append("")
        lines.append("| Akte | PDF lesen | Akten-ZIP |")
        lines.append("| --- | --- | --- |")
        for slug in akten_slugs:
            title = get_akte_title(slug)
            pdf_url = (
                f"../testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf"
            )
            zip_url = f"{RELEASE_BASE}/testakte-{slug}.zip"
            lines.append(
                f"| **{title}** (`{slug}`) | "
                f"[Gesamt-PDF lesen]({pdf_url}) | "
                f"[`testakte-{slug}.zip`]({zip_url}) |"
            )
        lines.append("")
    else:
        lines.append("Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.")
        lines.append("")

    lines.append(MARKER_END)
    return "\n".join(lines)


def inject_section(readme: Path, plugin_name: str, akten_slugs: list[str]) -> str:
    """Returns one of: 'INSERTED', 'UPDATED', 'UNCHANGED', 'SKIPPED'."""
    if not readme.exists():
        return "SKIPPED"
    text = readme.read_text(encoding="utf-8")
    new_block = build_section(plugin_name, akten_slugs)

    if MARKER_BEGIN in text and MARKER_END in text:
        # Replace existing
        pattern = re.compile(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END),
            re.DOTALL,
        )
        new_text = pattern.sub(new_block, text)
        if new_text == text:
            return "UNCHANGED"
        readme.write_text(new_text, encoding="utf-8")
        return "UPDATED"

    # Insert directly after H1 line (before any other content)
    h1 = H1_RE.search(text)
    if not h1:
        return "SKIPPED"
    insert_pos = h1.end()
    # Skip blank lines after H1
    after = text[insert_pos:]
    blank = re.match(r"\n+", after)
    if blank:
        insert_pos += blank.end()
    new_text = text[:insert_pos] + "\n" + new_block + "\n\n" + text[insert_pos:]
    readme.write_text(new_text, encoding="utf-8")
    return "INSERTED"


def main() -> int:
    mapping = discover_mapping()
    marketplace = json.loads(
        (REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugin_names = [p["name"] for p in marketplace["plugins"]]

    counts = {"INSERTED": 0, "UPDATED": 0, "UNCHANGED": 0, "SKIPPED": 0}

    for name in plugin_names:
        plugin_dir = REPO_ROOT / name
        readme = plugin_dir / "README.md"
        akten = sorted(mapping.get(name, []))
        status = inject_section(readme, name, akten)
        counts[status] += 1
        if status in ("INSERTED", "UPDATED"):
            count_str = f"  ({len(akten)} Akte/n)" if akten else "  (keine Akte)"
            print(f"  {status:8s}  {name}{count_str}")

    print(
        f"\nFertig: {counts['INSERTED']} neu, {counts['UPDATED']} aktualisiert, "
        f"{counts['UNCHANGED']} unveraendert, {counts['SKIPPED']} uebersprungen"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
