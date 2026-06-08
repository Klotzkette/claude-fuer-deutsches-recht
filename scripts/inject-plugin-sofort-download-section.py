#!/usr/bin/env python3
"""Fuegt in jede <plugin>/README.md ganz oben (direkt nach dem H1) eine
prominente 'Sofort-Download'-Sektion ein.

Inhalt der Sektion:
- Plugin-ZIP-Direktdownload (immer, fuer ALLE Plugins)
- Pro zugeordnete Testakte: ZIP-Download und Gesamt-PDF-Lesen

Quelle der Akten-Zuordnung: jede testakten/<slug>/README.md und die zentrale
testakten/README.md, soweit dort bestehende Plugin-Namen per Backtick
(`plugin-name`) referenziert werden. Identisch zur Logik in
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

# Einzelne ältere Akten nennen Skill- oder Sachgebietsnamen, die fachlich einem
# bestehenden Plugin entsprechen. Diese Aliase werden nur für README-
# Downloadsektionen verwendet; die Akten selbst bleiben unverändert.
PLUGIN_ALIASES = {
    "bauplanungsrecht": ["normenkontrolle-bauleitplanung"],
    "cisg-handelskauf": ["urteilsbauer-relationsmacher"],
    "dsgvo": ["datenschutzrecht"],
    "internationales-privatrecht": ["urteilsbauer-relationsmacher"],
}


def add_mapping(
    mapping: dict[str, set[str]],
    plugin_names: set[str],
    slug: str,
    text: str,
) -> None:
    """Fuege alle Plugin-Backticks aus text fuer slug in mapping ein."""
    tokens = set(re.findall(r"`([^`]+)`", text))
    for token in tokens:
        if token in plugin_names:
            mapping.setdefault(token, set()).add(slug)
        for alias_target in PLUGIN_ALIASES.get(token, []):
            if alias_target in plugin_names:
                mapping.setdefault(alias_target, set()).add(slug)


def discover_mapping() -> dict[str, list[str]]:
    """Sammle Plugin->Akten-Verbindungen aus Einzel-README und Gesamtuebersicht."""
    mapping: dict[str, set[str]] = {}
    if not TESTAKTEN_DIR.exists():
        return {}
    marketplace = json.loads(
        (REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugin_names = {p["name"] for p in marketplace["plugins"]}

    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir():
            continue
        readme = sub / "README.md"
        if readme.exists():
            add_mapping(mapping, plugin_names, sub.name, readme.read_text(encoding="utf-8"))

    overview = TESTAKTEN_DIR / "README.md"
    if overview.exists():
        for line in overview.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\| \[`([^/]+)/`\]\(\./\1/\) \|", line)
            if m:
                # Die zentrale Testakten-Tabelle hat im Lauf der Releases
                # verschiedene Spaltenzuschnitte bekommen. Darum nicht auf
                # eine bestimmte Plugin-Spalte verlassen, sondern die ganze
                # Zeile nach Plugin-Backticks durchsuchen.
                add_mapping(mapping, plugin_names, m.group(1), line)
    return {p: sorted(v) for p, v in mapping.items()}


def get_akte_title(akte_slug: str) -> str:
    """Lese den H1-Titel aus testakten/<slug>/README.md und bereinige Praefixe."""
    readme = TESTAKTEN_DIR / akte_slug / "README.md"
    if not readme.exists():
        return akte_slug
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            return re.sub(
                r"^(Akte|Beispielakte|Testakte|Mandantenakte)\s*[:–-]\s*",
                "",
                title,
                flags=re.IGNORECASE,
            )
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

    def insert_after_h1(current_text: str) -> str:
        h1 = H1_RE.search(current_text)
        if not h1:
            return current_text
        insert_pos = h1.end()
        after = current_text[insert_pos:]
        blank = re.match(r"\n+", after)
        if blank:
            insert_pos += blank.end()
        return current_text[:insert_pos] + "\n" + new_block + "\n\n" + current_text[insert_pos:]

    if MARKER_BEGIN in text and MARKER_END in text:
        # Replace existing and keep the block directly after the H1.
        pattern = re.compile(
            r"\n*" + re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n*",
            re.DOTALL,
        )
        without_old_block = pattern.sub("\n", text, count=1)
        new_text = insert_after_h1(without_old_block)
        if new_text == text:
            return "UNCHANGED"
        readme.write_text(new_text, encoding="utf-8")
        return "UPDATED"

    # Insert directly after H1 line (before any other content)
    if not H1_RE.search(text):
        return "SKIPPED"
    new_text = insert_after_h1(text)
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
