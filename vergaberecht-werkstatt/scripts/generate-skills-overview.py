#!/usr/bin/env python3
"""
Generiert in jeder Plugin-README einen Abschnitt
'## Alle Skills im Überblick (automatisch generiert)'
am Ende der Datei. Der Abschnitt listet alle Skills mit Description
aus den jeweiligen SKILL.md-Dateien.

Idempotent: erkennt vorhandene Markierungsblöcke und ersetzt sie.
Bestehende, manuell gepflegte Skills-Sektionen werden NICHT angetastet.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
END = "<!-- END SKILLS-OVERVIEW (auto-generated) -->"
from public_release import RAW_BASE as GH_RAW, with_working_downloads


def clean_description(desc: str) -> str:
    """Bereinigt Beschreibungen für die menschenlesbare Markdown-Ausgabe."""
    desc = re.sub(
        r"\s+[—-]\s*Arbeitskontext:\s*[^.]+,\s*Schwerpunkt\s+[^.]+\.?",
        "",
        desc,
    )
    desc = re.sub(r"\s+im Plugin\s+[^.:\"`|]+(?=[:.])", "", desc)
    desc = re.sub(r"\s+im Plugin\s+[^\"`|]+$", "", desc)
    # Frontmatter muss für den Marketplace "Paragraf" ausschreiben. In der
    # sichtbaren Dokumentation ist dagegen das juristisch übliche Zeichen klarer.
    desc = re.sub(r"\b(?:Paragrafen|Paragraphen)\s+(?=\d)", "§§ ", desc)
    desc = re.sub(r"\b(?:Paragraf|Paragraph)\s+(?=\d)", "§ ", desc)
    desc = re.sub(r"\b(?:Paragraf|Paragraph)-(?=\d)", "§-", desc)
    desc = re.sub(r"\s{2,}", " ", desc)
    return desc.strip()


def read_description(skill_md: Path) -> str:
    """Liest description aus YAML-Frontmatter einer SKILL.md."""
    if not skill_md.is_file():
        return ""
    with skill_md.open("r", encoding="utf-8") as fh:
        first = fh.readline()
        if first.strip() != "---":
            return ""
        frontmatter_lines: list[str] = []
        for idx, line in enumerate(fh, start=1):
            if idx > 200:
                return ""
            if line.strip() == "---":
                break
            frontmatter_lines.append(line)
        else:
            return ""
    fm = "".join(frontmatter_lines)
    if not fm:
        return ""
    # description kann mehrzeilig (mit Anführungszeichen) oder einzeilig sein
    desc = ""
    for line in fm.splitlines():
        if line.startswith("description:"):
            desc = line.split(":", 1)[1].strip()
            break
    if not desc:
        return ""
    # Anführungszeichen entfernen
    if len(desc) >= 2 and desc[0] == desc[-1] and desc[0] in {'"', "'"}:
        desc = desc[1:-1]
    # Pipes für Tabelle escapen, Zeilenumbrüche in Spaces
    desc = clean_description(desc.replace("\n", " ").strip())
    desc = desc.replace("|", "\\|").strip()
    # Lange Beschreibungen sauber kürzen, ohne sichtbare Datendump-Ellipsen.
    if len(desc) > 240:
        cut = max(desc.rfind(". ", 0, 225), desc.rfind("; ", 0, 225), desc.rfind(", ", 0, 225))
        if cut >= 120:
            desc = desc[: cut + 1].rstrip(" ,;:")
            if not desc.endswith((".", "!", "?")):
                desc += "."
        else:
            desc = desc[:236].rstrip(" ,.;:") + "."
    return desc


def build_overview(plugin_dir: Path) -> str:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return ""
    skills = sorted(
        d.name
        for d in skills_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file()
    )
    if not skills:
        return ""

    lines = [
        BEGIN,
        "",
        "## Alle Skills im Überblick",
        "",
        f"Der vollständige Katalog enthält {len(skills)} Skills. "
        "Für die normale Fallbearbeitung genügt der rollenbezogene Startworkflow weiter oben; "
        "die Gesamtliste lässt sich bei Bedarf aufklappen.",
        "",
        "<details>",
        f"<summary><strong>Alle {len(skills)} Skills mit Beschreibung und Rohdatei anzeigen</strong></summary>",
        "",
        "| Skill | Beschreibung | Rohdatei |",
        "| --- | --- | --- |",
    ]
    for s in skills:
        desc = read_description(skills_dir / s / "SKILL.md")
        raw_url = f"{GH_RAW}/{plugin_dir.name}/skills/{s}/SKILL.md"
        lines.append(
            f"| [`{s}`](skills/{s}/SKILL.md) | {desc} | [Raw .md]({raw_url}) |"
        )

    support_files: list[Path] = []
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if manifest.is_file():
        support_files.append(manifest)
    for dirname in ("assets", "references"):
        base = plugin_dir / dirname
        if base.is_dir():
            support_files.extend(sorted(p for p in base.rglob("*") if p.is_file()))

    if support_files:
        lines.extend(
            [
                "",
                "</details>",
                "",
                "## Vorlagen, Referenzen und Manifest",
                "",
                "Alle mitgelieferten Hilfsdateien sind einzeln erreichbar und zusätzlich "
                "im Plugin-ZIP enthalten.",
                "",
                "<details>",
                f"<summary><strong>Alle {len(support_files)} Vorlagen, Referenzen und Manifestdateien anzeigen</strong></summary>",
                "",
                "| Datei | Ansehen | Rohdatei |",
                "| --- | --- | --- |",
            ]
        )
        for path in support_files:
            rel = path.relative_to(plugin_dir).as_posix()
            raw_url = f"{GH_RAW}/{plugin_dir.name}/{rel}"
            lines.append(
                f"| `{rel}` | [Ansehen]({rel}) | [Raw]({raw_url}) |"
            )
        lines.extend(["", "</details>"])
    else:
        lines.extend(["", "</details>"])
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def update_readme(readme: Path, overview: str) -> bool:
    """Returns True if file was changed."""
    if not overview:
        return False
    original = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    new = original

    if BEGIN in new and END in new:
        # Ersetze bestehende Autogen-Blöcke und ziehe versehentliche
        # Duplikate zu genau einem aktuellen Block zusammen.
        start = new.find(BEGIN)
        end = new.rfind(END) + len(END)
        new = new[:start] + overview + new[end:]
    else:
        # Anhängen am Ende, mit Trenner
        sep = "" if new.endswith("\n\n") else ("\n" if new.endswith("\n") else "\n\n")
        new = new + sep + "\n" + overview + "\n"

    new = with_working_downloads(new, readme)
    if new == original:
        return False
    readme.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    os.chdir(repo)
    changed = 0
    total = 0
    for plugin_json in sorted(repo.glob("*/.claude-plugin/plugin.json")):
        plugin_dir = plugin_json.parent.parent
        readme = plugin_dir / "README.md"
        if not readme.is_file():
            print(f"  SKIP {plugin_dir.name}: keine README.md")
            continue
        overview = build_overview(plugin_dir)
        if not overview:
            continue
        total += 1
        if update_readme(readme, overview):
            changed += 1
            print(f"  UPD  {plugin_dir.name}")
    print(f"\nFertig: {changed}/{total} READMEs aktualisiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
