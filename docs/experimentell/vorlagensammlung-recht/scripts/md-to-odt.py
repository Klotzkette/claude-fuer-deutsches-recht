#!/usr/bin/env python3
"""Erzeugt aus einer sprechend benannten Markdown-Datei eine gleichnamige ODT-Datei.

Nutzt pandoc als Backend. Pandoc-Aufruf:
    pandoc -f markdown -t odt -o grundschuldbestellung-notariell.odt grundschuldbestellung-notariell.md

Voraussetzung: pandoc (>= 2.x) ist installiert (apt: `pandoc`, brew: `pandoc`).
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


FIRST_PAGE_NOTICE_DE = (
    "Mit KI generiert. Dies ist ein experimentelles Dokument. "
    "Benutzung auf eigene Gefahr und eigenes Risiko."
)
FIRST_PAGE_NOTICE_EN = (
    "Generated with AI. This is an experimental document. Use at your own risk."
)
FIRST_PAGE_NOTICE_STYLE = "FirstPageAiNotice"


def md_to_odt(md_path: Path) -> Path:
    md_path = md_path.resolve()
    odt_path = md_path.with_suffix(".odt")
    markdown = md_path.read_text(encoding="utf-8")
    with tempfile.NamedTemporaryFile(
        "w",
        delete=False,
        suffix=".md",
        encoding="utf-8",
    ) as tmp:
        tmp_md_path = Path(tmp.name)
        tmp.write(escape_angle_placeholders_for_pandoc(markdown))
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".odt",
        prefix=f".{odt_path.stem}.",
        dir=odt_path.parent,
    ) as tmp_odt:
        tmp_odt_path = Path(tmp_odt.name)
    try:
        subprocess.run(
            [
                "pandoc",
                "-f",
                "markdown-yaml_metadata_block-multiline_tables-simple_tables",
                "-t",
                "odt",
                "--resource-path",
                str(md_path.parent),
                "-o",
                str(tmp_odt_path),
                str(tmp_md_path),
            ],
            cwd=md_path.parent,
            check=True,
        )
        querformat = needs_landscape_layout(markdown)
        normalize_odt_layout(tmp_odt_path, landscape=querformat)
        pruefe_generiertes_odt(tmp_odt_path, landscape=querformat)
        tmp_odt_path.chmod(0o644)
        tmp_odt_path.replace(odt_path)
    finally:
        if tmp_md_path.exists():
            tmp_md_path.unlink()
        if tmp_odt_path.exists():
            tmp_odt_path.unlink()
    return odt_path


def needs_landscape_layout(markdown: str) -> bool:
    """Erkennt dokumentprägende breite Markdown-Tabellen.

    Einzelne kompakte Anlagen bleiben im üblichen A4-Hochformat. Checklisten
    und Berechnungsschemata erhalten abhängig von Spalten- und Zeilenzahl
    A4-Querformat. Sehr breite Tabellen benötigen schon mit wenigen Datenzeilen
    mehr Satzbreite; sie dürfen nicht nur wegen ihrer Kürze übersehen werden.
    """
    tabellen: list[list[int]] = []
    aktuelle_tabelle: list[int] = []
    for line in [*markdown.splitlines(), ""]:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            aktuelle_tabelle.append(
                len(re.split(r"(?<!\\)\|", stripped[1:-1]))
            )
            continue
        if aktuelle_tabelle:
            tabellen.append(aktuelle_tabelle)
            aktuelle_tabelle = []

    breite_zeilen = sum(
        1
        for tabelle in tabellen
        for spalten in tabelle
        if spalten >= 7
    )
    if breite_zeilen >= 8:
        return True

    for tabelle in tabellen:
        spalten = max(tabelle)
        zeilen = len(tabelle)
        if (
            (spalten >= 9 and zeilen >= 3)
            or (spalten >= 8 and zeilen >= 4)
            or (spalten >= 7 and zeilen >= 6)
        ):
            return True
    return False


def escape_angle_placeholders_for_pandoc(text: str) -> str:
    """Schützt versehentliche spitze Textklammern vor Pandocs HTML-Erkennung.

    Repo-Platzhalter stehen ausschließlich in eckigen Klammern. Die zusätzliche
    Maskierung verhindert dennoch, dass sonstiger Text zwischen `<` und `>` beim
    Export irrtümlich als unbekanntes HTML-Element verschwindet.
    """
    known_html = {
        "a", "abbr", "b", "br", "cite", "code", "dd", "del", "div",
        "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6", "hr",
        "i", "img", "li", "ol", "p", "pre", "q", "s", "span",
        "strong", "sub", "sup", "table", "tbody", "td", "tfoot",
        "th", "thead", "tr", "u", "ul",
    }
    protected: list[str] = []

    def protect_html(match: re.Match[str]) -> str:
        inner = match.group(1).strip()
        name = inner.split(None, 1)[0].rstrip("/").lstrip("/").lower()
        if name not in known_html:
            return match.group(0)
        protected.append(match.group(0))
        return f"@@HTML_TAG_{len(protected) - 1}@@"

    text = re.sub(r"(?<!\\)<([^<>\n]{1,260})>", protect_html, text)
    text = text.replace("<", r"\<").replace(">", r"\>")
    for i, tag in enumerate(protected):
        text = text.replace(f"@@HTML_TAG_{i}@@", tag)
    return text


def normalize_odt_layout(odt_path: Path, *, landscape: bool = False) -> None:
    """Setzt das ODT-Basislayout auf A4 und 11 pt Grundschrift.

    Fließtext erhält 2,5 cm Seitenränder; tabellendominierte Dokumente nutzen
    A4-Querformat mit 2 cm Seitenrändern. Hinzu kommen ruhige Absatzabstände
    und eine rechte Seitenzahl in der Fußzeile. Die erste Seite erhält
    zusätzlich den verbindlichen zweisprachigen Experimentierhinweis.
    """
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".odt",
        prefix=f".{odt_path.stem}.layout.",
        dir=odt_path.parent,
    ) as tmp:
        tmp_path = Path(tmp.name)

    try:
        with zipfile.ZipFile(odt_path, "r") as source, zipfile.ZipFile(tmp_path, "w") as target:
            for item in source.infolist():
                data = source.read(item.filename)
                if item.filename == "styles.xml":
                    text = data.decode("utf-8", errors="ignore")
                    text = patch_styles_xml(text, landscape=landscape)
                    data = text.encode("utf-8")
                elif item.filename == "content.xml":
                    text = data.decode("utf-8", errors="ignore")
                    text = patch_content_xml(text)
                    data = text.encode("utf-8")
                target.writestr(item, data)
        tmp_path.replace(odt_path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def pruefe_generiertes_odt(odt_path: Path, *, landscape: bool) -> None:
    """Validiert den neuen Export, bevor er eine vorhandene Fassung ersetzt."""
    try:
        with zipfile.ZipFile(odt_path, "r") as archiv:
            defekt = archiv.testzip()
            if defekt is not None:
                raise RuntimeError(f"CRC-Fehler in {defekt}")
            namen = set(archiv.namelist())
            fehlend = {"mimetype", "content.xml", "styles.xml"} - namen
            if fehlend:
                raise RuntimeError(
                    "ODT-Kerneinträge fehlen: " + ", ".join(sorted(fehlend))
                )
            content = archiv.read("content.xml").decode("utf-8")
            styles = archiv.read("styles.xml").decode("utf-8")
    except (UnicodeDecodeError, zipfile.BadZipFile, KeyError) as exc:
        raise RuntimeError(f"ODT-Export ist nicht lesbar: {exc}") from exc

    if "<office:text" not in content:
        raise RuntimeError("ODT-Export enthält keinen Dokumenttext")
    erwartet = "landscape" if landscape else "portrait"
    if f'style:print-orientation="{erwartet}"' not in styles:
        raise RuntimeError(
            f"ODT-Export besitzt nicht das erwartete Seitenprofil {erwartet}"
        )
    for merkmal in (
        "Times New Roman",
        "11pt",
        "<style:footer>",
        "<style:footer-first",
        "<text:page-number",
        FIRST_PAGE_NOTICE_DE,
        FIRST_PAGE_NOTICE_EN,
    ):
        if merkmal not in styles:
            raise RuntimeError(f"ODT-Export ohne Layoutmerkmal: {merkmal}")
    if (
        styles.count(FIRST_PAGE_NOTICE_DE) != 1
        or styles.count(FIRST_PAGE_NOTICE_EN) != 1
    ):
        raise RuntimeError("ODT-Export enthält den Erstseitenhinweis nicht genau einmal")
    if styles.count("<style:footer-first") != 1:
        raise RuntimeError("ODT-Export enthält nicht genau eine Erstseiten-Fußzeile")


def patch_styles_xml(text: str, *, landscape: bool = False) -> str:
    replacements = {
        'fo:page-width="8.5in"': 'fo:page-width="21cm"',
        'fo:page-height="11in"': 'fo:page-height="29.7cm"',
        'fo:margin-bottom="1in"': 'fo:margin-bottom="2.5cm"',
        'fo:margin-left="1in"': 'fo:margin-left="2.5cm"',
        'fo:margin-right="1in"': 'fo:margin-right="2.5cm"',
        'fo:margin-top="1in"': 'fo:margin-top="2.5cm"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    if landscape:
        text = patch_page_layout_landscape(text)

    marker = '<style:default-style style:family="paragraph">'
    start = text.find(marker)
    if start == -1:
        return text
    end = text.find("</style:default-style>", start)
    if end == -1:
        return text
    block = text[start:end]
    for attr in ("fo:font-size", "style:font-size-asian", "style:font-size-complex"):
        block = replace_xml_attr(block, attr, "11pt")
    for attr in ("style:font-name", "style:font-name-asian", "style:font-name-complex"):
        block = replace_xml_attr(block, attr, "Times New Roman")
    text = text[:start] + block + text[end:]

    heading_styles = {
        "Heading": {"fo:font-size": "12pt", "style:font-size-asian": "12pt", "style:font-size-complex": "12pt"},
        "Heading_20_1": {"fo:font-size": "14pt", "style:font-size-asian": "14pt", "style:font-size-complex": "14pt"},
        "Heading_20_2": {"fo:font-size": "12pt", "style:font-size-asian": "12pt", "style:font-size-complex": "12pt"},
        "Heading_20_3": {"fo:font-size": "11pt", "style:font-size-asian": "11pt", "style:font-size-complex": "11pt"},
        "Heading_20_4": {"fo:font-size": "11pt", "style:font-size-asian": "11pt", "style:font-size-complex": "11pt"},
    }
    for style_name, attrs in heading_styles.items():
        text = patch_named_style(
            text,
            style_name,
            {
                **attrs,
                "style:font-name": "Times New Roman",
                "style:font-name-asian": "Times New Roman",
                "style:font-name-complex": "Times New Roman",
                "fo:font-weight": "bold",
                "style:font-weight-asian": "bold",
                "style:font-weight-complex": "bold",
                "fo:font-style": "normal",
                "style:font-style-asian": "normal",
                "style:font-style-complex": "normal",
            },
        )
    text = patch_named_style(
        text,
        "Text_20_body",
        {
            "fo:font-size": "11pt",
            "style:font-size-asian": "11pt",
            "style:font-size-complex": "11pt",
            "style:font-name": "Times New Roman",
            "style:font-name-asian": "Times New Roman",
            "style:font-name-complex": "Times New Roman",
        },
    )
    text = patch_named_style(
        text,
        "First_20_paragraph",
        {
            "fo:font-size": "11pt",
            "style:font-size-asian": "11pt",
            "style:font-size-complex": "11pt",
            "style:font-name": "Times New Roman",
            "style:font-name-asian": "Times New Roman",
            "style:font-name-complex": "Times New Roman",
        },
    )
    text = apply_readability_spacing(text)
    if landscape:
        for style_name in ("Table_20_Contents", "Table_20_Heading"):
            text = patch_named_style(
                text,
                style_name,
                {
                    "fo:font-size": "10pt",
                    "style:font-size-asian": "10pt",
                    "style:font-size-complex": "10pt",
                },
            )
    text = keep_table_rows_together(text)
    text = ensure_footer_page_number(text)
    text = ensure_first_page_ai_notice(text)
    return text


def patch_page_layout_landscape(text: str) -> str:
    """Schaltet tabellendominierte Arbeitsfassungen auf A4-Querformat."""
    import re

    pattern = r"<style:page-layout-properties\b[^>]*>"
    match = re.search(pattern, text)
    if not match:
        return text
    tag = match.group(0)
    tag = set_xml_attr(tag, "style:print-orientation", "landscape")
    tag = set_xml_attr(tag, "fo:page-width", "29.7cm")
    tag = set_xml_attr(tag, "fo:page-height", "21cm")
    tag = set_xml_attr(tag, "fo:margin-left", "2cm")
    tag = set_xml_attr(tag, "fo:margin-right", "2cm")
    return text[: match.start()] + tag + text[match.end() :]


def apply_readability_spacing(text: str) -> str:
    """Gibt dem erzeugten ODT mehr Luft zwischen Sinnabschnitten.

    Die Markdown-Quellen bleiben schlank. Die nutzbaren ODT-Arbeitsfassungen
    bekommen hier aber mehr Abstand um Überschriften, Fließtext, Listen und
    Tabellenzellen. Das macht lange juristische Vorlagen am Bildschirm und im
    Ausdruck deutlich leichter scannbar.
    """
    paragraph_spacing = {
        "Text_20_body": {
            "style:contextual-spacing": "false",
            "fo:margin-top": "0.045in",
            "fo:margin-bottom": "0.095in",
            "fo:line-height": "121%",
            "fo:widows": "2",
            "fo:orphans": "2",
        },
        "First_20_paragraph": {
            "style:contextual-spacing": "false",
            "fo:margin-top": "0.025in",
            "fo:margin-bottom": "0.095in",
            "fo:line-height": "121%",
            "fo:widows": "2",
            "fo:orphans": "2",
        },
        "Block_20_Text": {
            "style:contextual-spacing": "false",
            "fo:margin-top": "0.07in",
            "fo:margin-bottom": "0.10in",
            "fo:line-height": "118%",
            "fo:widows": "2",
            "fo:orphans": "2",
        },
        "Heading": {
            "style:contextual-spacing": "false",
            "fo:keep-with-next": "always",
            "fo:margin-top": "0.22in",
            "fo:margin-bottom": "0.10in",
        },
        "Heading_20_1": {
            "style:contextual-spacing": "false",
            "fo:keep-with-next": "always",
            "fo:margin-top": "0.26in",
            "fo:margin-bottom": "0.12in",
        },
        "Heading_20_2": {
            "style:contextual-spacing": "false",
            "fo:keep-with-next": "always",
            "fo:margin-top": "0.19in",
            "fo:margin-bottom": "0.10in",
        },
        "Heading_20_3": {
            "style:contextual-spacing": "false",
            "fo:keep-with-next": "always",
            "fo:margin-top": "0.15in",
            "fo:margin-bottom": "0.075in",
        },
        "Heading_20_4": {
            "style:contextual-spacing": "false",
            "fo:keep-with-next": "always",
            "fo:margin-top": "0.12in",
            "fo:margin-bottom": "0.065in",
        },
        "List": {
            "style:contextual-spacing": "false",
            "fo:margin-top": "0.035in",
            "fo:margin-bottom": "0.07in",
            "fo:line-height": "116%",
            "fo:widows": "2",
            "fo:orphans": "2",
        },
        "Table_20_Contents": {
            "fo:margin-left": "0.055in",
            "fo:margin-right": "0.055in",
            "fo:margin-top": "0.04in",
            "fo:margin-bottom": "0.04in",
            "fo:line-height": "114%",
        },
        "Table_20_Heading": {
            "fo:margin-left": "0.055in",
            "fo:margin-right": "0.055in",
            "fo:margin-top": "0.045in",
            "fo:margin-bottom": "0.045in",
            "fo:line-height": "114%",
        },
    }
    for style_name, attrs in paragraph_spacing.items():
        text = patch_named_paragraph_properties(text, style_name, attrs)
    return text


def patch_content_xml(text: str) -> str:
    """Gibt Pandoc-Tabellen ein ruhiges, druckfestes Zellraster.

    Ohne Nachbearbeitung erzeugt Pandoc in ODT-Dateien randlose Tabellen. Bei
    umfangreichen Anlagen-, Fristen- und Berechnungstabellen verlieren Leser
    dadurch leicht die Zeile. Kopfzeilen werden deshalb dezent hinterlegt und
    alle Zellen erhalten ein feines Raster sowie ausreichend Innenabstand.
    """
    text = patch_named_table_cell_properties(
        text,
        "TableHeaderRowCell",
        {
            "fo:background-color": "#EAF2F8",
            "fo:border": "0.5pt solid #AEB6BF",
            "fo:padding": "0.06in",
            "style:vertical-align": "middle",
        },
    )
    text = patch_named_table_cell_properties(
        text,
        "TableRowCell",
        {
            "fo:border": "0.35pt solid #D5D8DC",
            "fo:padding": "0.055in",
            "style:vertical-align": "top",
        },
    )
    return text


def keep_table_rows_together(text: str) -> str:
    """Verhindert geteilte Anlagen- und Berechnungstabellen am Seitenwechsel.

    Pandoc erlaubt standardmäßig, eine Tabellenzeile auf zwei Seiten zu
    verteilen. Das trennt Dokumentbezeichnung und Datum oder Zahlenwert und
    Erläuterung voneinander. Die ODT-Arbeitsfassung hält deshalb jede Zeile als
    lesbare Einheit zusammen und verschiebt sie erforderlichenfalls vollständig
    auf die Folgeseite.
    """
    import re

    pattern = (
        r'(<style:default-style\b(?=[^>]*style:family="table-row")'
        r'[\s\S]*?</style:default-style>)'
    )
    match = re.search(pattern, text)
    if not match:
        return text
    block = match.group(1)
    if "<style:table-row-properties" not in block:
        block = block.replace(
            "</style:default-style>",
            '<style:table-row-properties fo:keep-together="always" />'
            "</style:default-style>",
        )
    else:
        block = re.sub(
            r"<style:table-row-properties\b[^>]*/>",
            lambda m: set_xml_attr(m.group(0), "fo:keep-together", "always"),
            block,
            count=1,
        )
    return text[: match.start(1)] + block + text[match.end(1) :]


def ensure_footer_page_number(text: str) -> str:
    """Normiert die Pandoc-Fußzeile auf rechtsbündige Seitenzahlen.

    Pandoc erzeugt regelmäßig bereits eine Standard-Fußzeile. Wir machen sie
    hier ausdrücklich stabil: Times New Roman, 11 pt, rechtsbündig, aktuelle
    Seitenzahl. Dadurch ist die Paginierung auch dann angelegt, wenn die
    Vorlage erst durch spätere Bearbeitung mehrseitig wird.
    """
    text = patch_named_style(
        text,
        "Footer",
        {
            "fo:font-size": "11pt",
            "style:font-size-asian": "11pt",
            "style:font-size-complex": "11pt",
            "style:font-name": "Times New Roman",
            "style:font-name-asian": "Times New Roman",
            "style:font-name-complex": "Times New Roman",
        },
    )
    text = patch_named_style(
        text,
        "MP1",
        {
            "fo:font-size": "11pt",
            "style:font-size-asian": "11pt",
            "style:font-size-complex": "11pt",
            "style:font-name": "Times New Roman",
            "style:font-name-asian": "Times New Roman",
            "style:font-name-complex": "Times New Roman",
        },
    )
    text = patch_named_paragraph_properties(
        text,
        "MP1",
        {
            "fo:text-align": "end",
            "style:justify-single-word": "false",
        },
    )
    if "<text:page-number" not in text:
        footer = (
            '<style:footer><text:p text:style-name="MP1">'
            '<text:page-number text:select-page="current">1</text:page-number>'
            "</text:p></style:footer>"
        )
        import re

        text = re.sub(
            r'(<style:master-page\b(?=[^>]*style:name="Standard")[^>]*>)([\s\S]*?)(</style:master-page>)',
            lambda m: m.group(1) + footer + m.group(3)
            if "<style:footer" not in m.group(2)
            else m.group(0),
            text,
            count=1,
        )
    return text


def ensure_first_page_ai_notice(text: str) -> str:
    """Setzt den zweisprachigen Experimentierhinweis nur auf Seite 1.

    ``style:footer-first`` trennt die Erstseiten-Fußzeile von der regulären
    Fußzeile. Diese behält auf allen Folgeseiten ausschließlich die
    Seitenzahl. Die Operation ist idempotent, damit wiederholte Exporte keine
    doppelten Hinweise oder Stile erzeugen.
    """
    import re

    notice_style = (
        f'<style:style style:family="paragraph" style:name="{FIRST_PAGE_NOTICE_STYLE}" '
        'style:parent-style-name="Footer">'
        '<style:paragraph-properties fo:line-height="105%" fo:margin-bottom="0in" '
        'fo:margin-top="0in" fo:text-align="center" '
        'style:justify-single-word="false" />'
        '<style:text-properties fo:color="#555555" fo:font-size="8pt" '
        'style:font-size-asian="8pt" style:font-size-complex="8pt" '
        'style:font-name="Times New Roman" '
        'style:font-name-asian="Times New Roman" '
        'style:font-name-complex="Times New Roman" />'
        '</style:style>'
    )
    style_pattern = (
        r'<style:style\b(?=[^>]*style:name="'
        + re.escape(FIRST_PAGE_NOTICE_STYLE)
        + r'")[\s\S]*?</style:style>'
    )
    if re.search(style_pattern, text):
        text = re.sub(style_pattern, notice_style, text, count=1)
    elif "</office:styles>" in text:
        text = text.replace("</office:styles>", notice_style + "</office:styles>", 1)

    first_footer = (
        '<style:footer-first>'
        f'<text:p text:style-name="{FIRST_PAGE_NOTICE_STYLE}">{FIRST_PAGE_NOTICE_DE}</text:p>'
        f'<text:p text:style-name="{FIRST_PAGE_NOTICE_STYLE}">{FIRST_PAGE_NOTICE_EN}'
        '<text:span> · Seite / Page </text:span>'
        '<text:page-number text:select-page="current">1</text:page-number>'
        '</text:p>'
        '</style:footer-first>'
    )
    master_pattern = (
        r'(<style:master-page\b(?=[^>]*style:name="Standard")[^>]*>)'
        r'([\s\S]*?)'
        r'(</style:master-page>)'
    )
    master = re.search(master_pattern, text)
    if not master:
        return text
    body = re.sub(
        r'<style:footer-first\b[^>]*>[\s\S]*?</style:footer-first>',
        "",
        master.group(2),
    )
    replacement = master.group(1) + body + first_footer + master.group(3)
    return text[: master.start()] + replacement + text[master.end() :]


def replace_xml_attr(text: str, attr: str, value: str) -> str:
    import re

    pattern = rf'{re.escape(attr)}="[^"]+"'
    replacement = f'{attr}="{value}"'
    return re.sub(pattern, replacement, text, count=1)


def patch_named_style(text: str, style_name: str, attrs: dict[str, str]) -> str:
    import re

    pattern = (
        r'(<style:style\b(?=[^>]*style:name="' + re.escape(style_name) + r'")[\s\S]*?</style:style>)'
    )
    match = re.search(pattern, text)
    if not match:
        return text
    block = match.group(1)
    if "<style:text-properties" not in block:
        block = block.replace("</style:style>", "<style:text-properties /></style:style>")
    block = re.sub(
        r"<style:text-properties\b[^>]*/>",
        lambda m: patch_xml_tag(m.group(0), attrs),
        block,
        count=1,
    )
    return text[: match.start(1)] + block + text[match.end(1) :]


def patch_named_paragraph_properties(text: str, style_name: str, attrs: dict[str, str]) -> str:
    import re

    pattern = (
        r'(<style:style\b(?=[^>]*style:name="' + re.escape(style_name) + r'")[\s\S]*?</style:style>)'
    )
    match = re.search(pattern, text)
    if not match:
        return text
    block = match.group(1)
    if "<style:paragraph-properties" not in block:
        block = block.replace("</style:style>", "<style:paragraph-properties /></style:style>")
    block = re.sub(
        r"<style:paragraph-properties\b[^>]*/>|<style:paragraph-properties\b[^>]*>",
        lambda m: patch_xml_tag(m.group(0), attrs),
        block,
        count=1,
    )
    return text[: match.start(1)] + block + text[match.end(1) :]


def patch_named_table_cell_properties(text: str, style_name: str, attrs: dict[str, str]) -> str:
    import re

    pattern = (
        r'(<style:style\b(?=[^>]*style:name="' + re.escape(style_name) + r'")[\s\S]*?</style:style>)'
    )
    match = re.search(pattern, text)
    if not match:
        return text
    block = match.group(1)
    if "<style:table-cell-properties" not in block:
        block = block.replace(
            "</style:style>",
            "<style:table-cell-properties /></style:style>",
        )
    block = re.sub(
        r"<style:table-cell-properties\b[^>]*/>|<style:table-cell-properties\b[^>]*>",
        lambda m: patch_xml_tag(m.group(0), attrs),
        block,
        count=1,
    )
    return text[: match.start(1)] + block + text[match.end(1) :]


def patch_xml_tag(tag: str, attrs: dict[str, str]) -> str:
    for attr, value in attrs.items():
        tag = set_xml_attr(tag, attr, value)
    return tag


def set_xml_attr(tag: str, attr: str, value: str) -> str:
    import re

    pattern = rf'{re.escape(attr)}="[^"]*"'
    replacement = f'{attr}="{value}"'
    if re.search(pattern, tag):
        return re.sub(pattern, replacement, tag, count=1)
    return tag.replace("/>", f' {replacement} />')


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: md-to-odt.py <pfad/zur/<vorlagen-slug>.md> [weitere ...]", file=sys.stderr)
        return 2
    if shutil.which("pandoc") is None:
        print("pandoc nicht gefunden. Bitte installieren (apt install pandoc).", file=sys.stderr)
        return 3
    rc = 0
    for p in argv[1:]:
        path = Path(p)
        if not path.is_file() or path.suffix.lower() != ".md":
            print(f"FEHLER (keine lesbare .md-Datei): {p}", file=sys.stderr)
            rc = 1
            continue
        try:
            out = md_to_odt(path)
            print(f"OK  {out}")
        except (OSError, RuntimeError, subprocess.CalledProcessError) as e:
            print(f"FEHLER bei {p}: {e}", file=sys.stderr)
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
