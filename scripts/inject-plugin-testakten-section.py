#!/usr/bin/env python3
"""Fuegt in jede <plugin>/README.md eine autogen-Sektion 'Demonstrations-Akten' ein,
die fuer jede zugeordnete Testakte einen Direktdownload-Link auf das Gesamt-PDF
(im Repo) UND die Akten-ZIP (aus dem GitHub-Release) anzeigt.

Quelle der Zuordnung: jede testakten/<slug>/README.md, die das Plugin per Backtick
(`plugin-name`) referenziert. Damit ist die Zuordnung deklarativ und liegt
in der Akte selbst.

Idempotent ueber HTML-Marker. Position: direkt nach dem H1, vor anderen Sektionen
und insbesondere vor der bestehenden Installation-Section mit dem Plugin-ZIP.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN_DIR = REPO_ROOT / "testakten"

MARKER_BEGIN = "<!-- BEGIN plugin-testakten-section (autogen) -->"
MARKER_END = "<!-- END plugin-testakten-section (autogen) -->"

RELEASE_BASE = (
    "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"
)

H1_RE = re.compile(r"^# .+$", re.MULTILINE)
BACKTICK_RE_TPL = r"`{name}`"


def discover_mapping() -> dict[str, list[str]]:
    """Lese alle testakten/*/README.md und sammle Plugin->Akten-Verbindungen
    ueber Backtick-Erwaehnungen `plugin-name`."""
    mapping: dict[str, set[str]] = {}
    if not TESTAKTEN_DIR.exists():
        return {}
    marketplace = json.loads(
        (REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugin_names = [p["name"] for p in marketplace["plugins"]]
    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir():
            continue
        readme = sub / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        for name in plugin_names:
            pat = re.compile(BACKTICK_RE_TPL.format(name=re.escape(name)))
            if pat.search(text):
                mapping.setdefault(name, set()).add(sub.name)
    return {p: sorted(v) for p, v in mapping.items()}


def short_title(slug: str) -> str:
    """Lies den H1-Titel aus testakten/<slug>/README.md, bereinige Praefixe.
    Fallback: slug mit Bindestrichen zu Leerzeichen."""
    rd = TESTAKTEN_DIR / slug / "README.md"
    if rd.is_file():
        for line in rd.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^# (.+)$", line.strip())
            if m:
                title = m.group(1).strip()
                title = re.sub(
                    r"^(Akte|Beispielakte|Testakte|Mandantenakte)\s*[:–-]\s*",
                    "",
                    title,
                    flags=re.IGNORECASE,
                )
                return title
    return slug.replace("-", " ")


def section_block(plugin_name: str, akten: list[str]) -> str:
    """Erzeuge die Demonstrations-Akten-Sektion fuer ein Plugin."""
    if not akten:
        return ""
    rows: list[str] = []
    for slug in akten:
        pdf_repo = f"../testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf"
        zip_release = f"{RELEASE_BASE}/testakte-{slug}.zip"
        title = short_title(slug)
        rows.append(
            f"| **{title}** (`{slug}`) "
            f"| [Gesamt-PDF lesen]({pdf_repo}) "
            f"| [Akten-ZIP herunterladen]({zip_release}) |"
        )
    rows_md = "\n".join(rows)
    plural = "Akten demonstrieren" if len(akten) > 1 else "Akte demonstriert"
    intro = (
        f"Folgende anonymisierte {plural} dieses Plugin im laufenden Mandatsbetrieb. "
        f"Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche "
        f"Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) "
        f"im Originalordnerlayout."
    )
    return f"""{MARKER_BEGIN}
## Demonstrations-Akten

{intro}

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
{rows_md}

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

{MARKER_END}
"""


def inject(plugin_dir: Path, plugin_name: str, akten: list[str]) -> str:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return "skip (kein README)"
    text = readme.read_text(encoding="utf-8")
    new_section = section_block(plugin_name, akten)

    # Falls Plugin (noch) keine Akten hat: bestehende Sektion entfernen
    if not new_section:
        pat = re.compile(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n?",
            re.DOTALL,
        )
        if pat.search(text):
            new_text = pat.sub("", text, count=1)
            readme.write_text(new_text, encoding="utf-8")
            return "removed (keine Akten zugeordnet)"
        return "skip (keine Akten, nichts zu entfernen)"

    # Falls Sektion existiert: ersetzen
    pat = re.compile(
        re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n?",
        re.DOTALL,
    )
    if pat.search(text):
        new_text = pat.sub(new_section, text, count=1)
        if new_text == text:
            return "unchanged"
        readme.write_text(new_text, encoding="utf-8")
        return "updated"

    # Erstmalig einfuegen direkt nach H1
    m = H1_RE.search(text)
    if not m:
        new_text = new_section + "\n" + text
    else:
        end = m.end()
        rest = text[end:]
        if rest.startswith("\n\n"):
            insert_at = end + 2
        elif rest.startswith("\n"):
            insert_at = end + 1
        else:
            insert_at = end
        new_text = text[:insert_at] + "\n" + new_section + "\n" + text[insert_at:]
    readme.write_text(new_text, encoding="utf-8")
    return "inserted"


def main() -> int:
    marketplace = json.loads(
        (REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    plugin_names = [p["name"] for p in marketplace["plugins"]]
    mapping = discover_mapping()
    stats = {
        "inserted": 0,
        "updated": 0,
        "unchanged": 0,
        "removed": 0,
        "skip": 0,
    }
    for name in sorted(plugin_names):
        plugin_dir = REPO_ROOT / name
        akten = mapping.get(name, [])
        result = inject(plugin_dir, name, akten)
        key = result.split()[0]
        if key not in stats:
            key = "skip"
        stats[key] += 1
        print(f"  {result.upper():<10} {name}  ({len(akten)} Akte/n)")
    print(
        f"\nFertig: {stats['inserted']} neu, {stats['updated']} aktualisiert, "
        f"{stats['unchanged']} unveraendert, {stats['removed']} entfernt, "
        f"{stats['skip']} uebersprungen"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
