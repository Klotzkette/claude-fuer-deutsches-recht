#!/usr/bin/env python3
"""Normalisiert Downloads und Vorschauen in jeder Vorlagen-README.

Hintergrund: GitHub serviert .md mit Content-Type: text/plain, was Browser
inline anzeigen. .zip wird zuverlässig heruntergeladen.

Der Link wird im Download-Block neu beschriftet als
„… – Markdown (ZIP) herunterladen — bearbeitbare Markdown-Fassung, gepackt
für direkten Download". Eine einheitliche Vorschauzeile verlinkt daneben die
ODT- und die rohe Markdown-Datei am kanonischen Speicherort.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import md_in, vorlagenordner  # noqa: E402
from _atomar import text_atomar_schreiben  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def update_readme(readme: Path, slug: str) -> bool:
    """Normalisiert den Markdown-ZIP-Link und beide lokalen Vorschauziele."""
    text = readme.read_text(encoding="utf-8")
    orig = text

    md_url_pattern = re.compile(
        r"(https://github\.com/[\w./-]+/raw/main/[\w./-]+/)" + re.escape(slug) + r"\.md(?!\.)"
    )
    text = md_url_pattern.sub(lambda m: m.group(1) + slug + ".md.zip", text)

    # Beschriftungs-Varianten an den Download-Link anpassen.
    text = text.replace(
        f"{slug}.md herunterladen",
        f"{slug}.md.zip herunterladen",
    )
    text = re.sub(
        r"(\[⬇[^\]]*?)Markdown herunterladen\]",
        r"\1Markdown (ZIP) herunterladen]",
        text,
    )
    text = re.sub(
        r"— Bearbeitbare Markdown-Fassung(?!, gepackt für direkten Download)",
        "— Bearbeitbare Markdown-Fassung, gepackt für direkten Download",
        text,
    )

    download_heading = re.search(
        r"^## (?:Download|Dateien und Direktdownload)\s*$",
        text,
        flags=re.MULTILINE,
    )
    if download_heading is not None:
        download_start = download_heading.start()
        download_end = text.find("\n## ", download_heading.end())
        if download_end < 0:
            download_end = len(text)
        download_block = text[download_start:download_end]
        odt_preview = f"]({slug}.odt)"
        md_preview = f"]({slug}.md)"
        if odt_preview not in download_block or md_preview not in download_block:
            preview_line = (
                f"Vorschau im Repository: [`{slug}.odt`]({slug}.odt) · "
                f"[`{slug}.md`]({slug}.md)"
            )
            lines = download_block.rstrip().splitlines()
            preview_index = next(
                (
                    index
                    for index, line in enumerate(lines)
                    if line.startswith("Vorschau im Repository:")
                    or line.startswith("Vorschau:")
                ),
                None,
            )
            if preview_index is None:
                lines.extend(["", preview_line])
            else:
                lines[preview_index] = preview_line
            normalized_block = "\n".join(lines) + "\n"
            text = text[:download_start] + normalized_block + text[download_end:]

    if text != orig:
        text_atomar_schreiben(readme, text)
        return True
    return False


def main() -> int:
    geaendert = 0
    untersucht = 0
    for ordner in vorlagenordner(REPO):
        md = md_in(ordner)
        if md is None:
            continue
        readme = ordner / "README.md"
        if not readme.is_file():
            continue
        untersucht += 1
        if update_readme(readme, md.stem):
            geaendert += 1
    print(f"update-readme-md-zip-links OK ({untersucht} READMEs, {geaendert} aktualisiert)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
