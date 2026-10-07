#!/usr/bin/env python3
"""generate-formatvorlagen.py - Erzeugt Formatvorlagen pro Plugin als .md + .odt.

Ausgabe: testakten/formatvorlagen-paradebeispiele/<plugin>/<filename>.{md,odt}

Regeln:
- Hausschrift und Grundgröße aus hausstil.json, A4, ordentliche Ränder (2,5 cm umlaufend)
- kurzer Warnhinweis oben: Arbeitsvorlage, keine Haftung
- Felder mit [Bracketed-Variables]
- Bei bilingualen Vorlagen: Maßgeb-Klausel deutsche Fassung
- Normen, Fristen, Zuständigkeit, Anlagen und Rechtsprechungsstand vor Verwendung prüfen
"""
from __future__ import annotations
from pathlib import Path
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hausstil  # noqa: E402

HAUSSTIL = hausstil.lade_hausstil()
SCHRIFT = HAUSSTIL.schrift
GRUNDGROESSE = hausstil.groesse_in_punkt(HAUSSTIL)

try:
    from odf.opendocument import OpenDocumentText
    from odf.style import Style, TextProperties, ParagraphProperties, PageLayout, PageLayoutProperties, MasterPage, FontFace
    from odf.text import P, H
    ODFPY_OK = True
except ImportError:
    ODFPY_OK = False

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / 'testakten' / 'formatvorlagen-paradebeispiele'

WARNUNG_DE = ('Achtung: Diese Arbeitsvorlage ist eine Prüf- und Formulierungshilfe. '
                 'Keine Haftung, keine Gewähr, keine Rechtsberatung. Vor Verwendung im '
                 'Mandat Sachverhalt, Fristen, Zuständigkeit, Normstand, Rechtsprechung '
                 'und Anlagen eigenständig prüfen.')
WARNUNG_EN = ('Caution: This is an experimental working template. No liability, '
                 'no warranty. For workflow exploration only; not legal advice. '
                 'Must be reviewed by a lawyer before any use in a mandate.')


def make_doc():
    """Erstellt ein ODT-Doc mit Times-Roman-11pt-Standardstil."""
    if not ODFPY_OK:
        raise RuntimeError("odfpy fehlt")
    doc = OpenDocumentText()
    # Schrift registrieren
    doc.fontfacedecls.addElement(
        FontFace(name=SCHRIFT, fontfamily=SCHRIFT,
                 fontfamilygeneric='roman', fontpitch='variable'))

    # Seitenformat A4 mit 2,5 cm Rändern
    pl = PageLayout(name='Standard')
    pl.addElement(PageLayoutProperties(
        pagewidth='21cm', pageheight='29.7cm',
        margintop='2.5cm', marginbottom='2.5cm',
        marginleft='2.5cm', marginright='2.5cm',
        writingmode='lr-tb'))
    doc.automaticstyles.addElement(pl)
    mp = MasterPage(name='Standard', pagelayoutname='Standard')
    doc.masterstyles.addElement(mp)

    # Default-Body-Stil: Hausschrift in Grundgroesse
    default = Style(name='Default', family='paragraph')
    default.addElement(TextProperties(fontname=SCHRIFT, fontsize=f'{GRUNDGROESSE:g}pt'))
    default.addElement(ParagraphProperties(textalign='justify', marginbottom='0.2cm'))
    doc.styles.addElement(default)

    # Kursivstil für Warnhinweis
    italic = Style(name='Warnhinweis', family='paragraph', parentstylename='Default')
    italic.addElement(TextProperties(fontname=SCHRIFT, fontsize='10pt',
                                     fontstyle='italic', color='#444444'))
    italic.addElement(ParagraphProperties(textalign='justify', marginbottom='0.4cm'))
    doc.automaticstyles.addElement(italic)

    # Header-Stile
    # Ueberschriften folgen der Grundgroesse, damit sie nie kleiner als der Fliesstext werden.
    for lvl, sz in [(1, GRUNDGROESSE + 5), (2, GRUNDGROESSE + 2), (3, GRUNDGROESSE + 0.5)]:
        s = Style(name=f'H{lvl}', family='paragraph', parentstylename='Default')
        s.addElement(TextProperties(fontname=SCHRIFT, fontsize=f'{sz}pt',
                                    fontweight='bold'))
        s.addElement(ParagraphProperties(textalign='left',
                                         margintop='0.4cm', marginbottom='0.2cm'))
        doc.automaticstyles.addElement(s)

    # Center + Bold
    center_bold = Style(name='CenterBold', family='paragraph', parentstylename='Default')
    center_bold.addElement(TextProperties(fontname=SCHRIFT,
                                           fontsize=f'{GRUNDGROESSE + 1}pt', fontweight='bold'))
    center_bold.addElement(ParagraphProperties(textalign='center', marginbottom='0.2cm'))
    doc.automaticstyles.addElement(center_bold)

    # Center
    center = Style(name='Center', family='paragraph', parentstylename='Default')
    center.addElement(TextProperties(fontname=SCHRIFT, fontsize=f'{GRUNDGROESSE:g}pt'))
    center.addElement(ParagraphProperties(textalign='center', marginbottom='0.2cm'))
    doc.automaticstyles.addElement(center)

    return doc


def add_para(doc, text, style='Default'):
    p = P(stylename=style)
    p.addText(text)
    doc.text.addElement(p)


def add_heading(doc, text, level=1):
    h = H(stylename=f'H{level}', outlinelevel=level)
    h.addText(text)
    doc.text.addElement(h)


def write_template(plugin: str, filename: str, title: str, lang: str,
                   sections: list[tuple[str, str, list[str]]], fields: list[str],
                   usage_checks: list[str] | None = None):
    """Schreibt .md und .odt für eine Vorlage.

    sections: liste von (kind, content, paragraphs) wo:
        kind = 'h1' | 'h2' | 'h3' | 'center_bold' | 'center' | 'p'
    fields: Liste der Bracket-Variablen in der Vorlage
    usage_checks: kurze fachliche Kontrollpunkte vor Versand oder Verwendung
    """
    target_dir = OUT / plugin
    target_dir.mkdir(parents=True, exist_ok=True)
    md_path = target_dir / f'{filename}.md'
    odt_path = target_dir / f'{filename}.odt'

    # --- Markdown ---
    md_lines = []
    md_lines.append(f'> *{WARNUNG_DE}*')
    if lang in ('en', 'bilingual'):
        md_lines.append(f'>')
        md_lines.append(f'> *{WARNUNG_EN}*')
    md_lines.append('')
    md_lines.append(f'# {title}')
    md_lines.append('')
    for kind, content, paras in sections:
        if kind == 'h1':
            md_lines.append(f'# {content}')
            md_lines.append('')
        elif kind == 'h2':
            md_lines.append(f'## {content}')
            md_lines.append('')
        elif kind == 'h3':
            md_lines.append(f'### {content}')
            md_lines.append('')
        elif kind == 'center_bold':
            md_lines.append(f'**{content}**')
            md_lines.append('')
        elif kind == 'center':
            md_lines.append(content)
            md_lines.append('')
        elif kind == 'p':
            for para in paras:
                md_lines.append(para)
                md_lines.append('')
    if usage_checks:
        md_lines.append('## Verwendungskontrolle')
        md_lines.append('')
        for item in usage_checks:
            md_lines.append(f'- {item}')
        md_lines.append('')
    if fields:
        md_lines.append('---')
        md_lines.append('')
        md_lines.append('## Ausfüllfelder')
        md_lines.append('')
        for f in fields:
            md_lines.append(f'- `{f}`')
        md_lines.append('')
    md_path.write_text('\n'.join(md_lines), encoding='utf-8')

    # --- ODT ---
    if not ODFPY_OK:
        pandoc = shutil.which("pandoc")
        if not pandoc:
            raise RuntimeError("Weder odfpy noch pandoc verfügbar; ODT kann nicht erzeugt werden")
        subprocess.run([pandoc, str(md_path), "-o", str(odt_path)], check=True)
        return md_path, odt_path

    doc = make_doc()
    add_para(doc, WARNUNG_DE, 'Warnhinweis')
    if lang in ('en', 'bilingual'):
        add_para(doc, WARNUNG_EN, 'Warnhinweis')
    add_para(doc, '', 'Default')
    add_heading(doc, title, level=1)
    for kind, content, paras in sections:
        if kind == 'h1':
            add_heading(doc, content, level=1)
        elif kind == 'h2':
            add_heading(doc, content, level=2)
        elif kind == 'h3':
            add_heading(doc, content, level=3)
        elif kind == 'center_bold':
            add_para(doc, content, 'CenterBold')
        elif kind == 'center':
            add_para(doc, content, 'Center')
        elif kind == 'p':
            for para in paras:
                add_para(doc, para, 'Default')
    if usage_checks:
        add_heading(doc, 'Verwendungskontrolle', level=2)
        for item in usage_checks:
            add_para(doc, f'• {item}', 'Default')
    if fields:
        add_para(doc, '', 'Default')
        add_heading(doc, 'Ausfüllfelder', level=2)
        for f in fields:
            add_para(doc, f'• {f}', 'Default')
    doc.save(str(odt_path))
    return md_path, odt_path


# --- Generator-Aufrufe ---

if __name__ == '__main__':
    print('Modul geladen. Importiere via Generator-Skripte.')
