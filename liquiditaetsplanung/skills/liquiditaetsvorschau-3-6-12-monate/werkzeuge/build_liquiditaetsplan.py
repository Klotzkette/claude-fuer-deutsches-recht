#!/usr/bin/env python3
"""
build_liquiditaetsplan.py
=========================

Erstellt eine rollierende Liquiditätsvorschau (13 / 26 / 52 Wochen) im
Layout der Klotzkette-Vorlage `vorlage-liquiditaetsplan.xlsx`:

    Bestand Start Planung
      Kassenbestand
      Kontostand
      Liquidität Wochenanfang            (hellblau, fett)
    Einnahmen                            (gelb, fett)
      Umsatzerlöse
      erhaltene Anzahlungen
      sonstige Einnahmen
      Summe Einnahmen
     Ausgaben                            (rot, fett)
      Löhne und Gehälter einschl. LSt
      Sozialversicherung
      Waren/ Material
      Miete
      Heizung/Strom/Wasser
      Verwaltung
      Werbung/Marketing
      Fahrzeug-/Leasingkosten
      Versicherungen
      Beratungskosten
      sonstige Ausgaben
      Investitionen
      Betriebliche Steuern
      sonstige Ausgaben (II)
      Darlehenstilgung
      Zinsen
      Privatentnahmen
      Summe Ausgaben
    Cash Flow Woche
    Liquidität Woche Ende                (hellblau, fett)

Erweitert um:
    fällige Verbindlichkeiten Folgewoche
    3-Wochen-Lücke (kumuliert)
    Lücken-Quote (%)
    Ampel § 17 InsO  (bedingte Formatierung GRÜN/GELB/ROT)

Sheets: 13-Wochen, 26-Wochen, 52-Wochen, Fortfuehrungsprognose, Annahmen.

Eingabe: YAML- oder JSON-Datei. Beispiel-YAML siehe Beispielakte.

Verwendung:
    python build_liquiditaetsplan.py --eingabe mandant.yaml \\
                                     --ausgabe liquiditaetsplan.xlsx

Standard-Bibliothek: Dieses Skript braucht **kein** pip-Paket. Der XLSX-
Schreiber ist intern implementiert (zipfile + xml.etree). PyYAML ist
optional (Mini-YAML-Parser-Fallback inkludiert).

Quellen:
- BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 12 ff. (§ 17 InsO)
- BGH, Urt. v. 19.11.2019 – II ZR 233/18, NJW 2020, 1809 Rn. 17 ff.
- IDW S 6 (Sanierungskonzepte), IDW S 11 (Insolvenzeröffnungsgründe)
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as xml_escape

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


# ----------------------------------------------------------------------------
# Eingabe
# ----------------------------------------------------------------------------

def load_input(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            return load_simple_yaml(text, path)
        return yaml.safe_load(text) or {}
    if path.suffix.lower() == ".json":
        return json.loads(text)
    raise SystemExit(f"Unbekanntes Eingabeformat: {path.suffix}")


def load_simple_yaml(text: str, path: Path) -> dict[str, Any]:
    """Kleiner YAML-Fallback für die mitgelieferten Akten, falls PyYAML fehlt."""
    root: dict[Any, Any] = {}
    stack: list[tuple[int, dict[Any, Any] | list[Any]]] = [(-1, root)]
    lines: list[tuple[int, int, str]] = []

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        if "\t" in raw_line[: len(raw_line) - len(raw_line.lstrip())]:
            raise SystemExit(f"{path}:{lineno}: Tabs in Einrückungen werden nicht unterstützt.")

        line = strip_yaml_comment(raw_line).rstrip()
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        content = line[indent:]
        lines.append((lineno, indent, content))

    for index, (lineno, indent, content) in enumerate(lines):
        while indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if content.startswith("- "):
            if not isinstance(parent, list):
                raise SystemExit(f"{path}:{lineno}: YAML-Liste ohne Listenkontext.")

            item_text = content[2:].strip()
            split_at = find_yaml_key_separator(item_text)
            if item_text and split_at is not None:
                item: dict[Any, Any] = {}
                parent.append(item)
                stack.append((indent, item))

                key_text = item_text[:split_at].strip()
                value_text = item_text[split_at + 1:].strip()
                if not key_text:
                    raise SystemExit(f"{path}:{lineno}: Leerer YAML-Schlüssel.")
                key = parse_yaml_scalar(key_text)
                if value_text == "":
                    child: dict[Any, Any] | list[Any]
                    child = [] if next_yaml_child_is_list(lines, index, indent) else {}
                    item[key] = child
                    stack.append((next_yaml_child_stack_indent(lines, index, indent), child))
                else:
                    item[key] = parse_yaml_scalar(value_text)
            elif item_text:
                parent.append(parse_yaml_scalar(item_text))
            else:
                item = {}
                parent.append(item)
                stack.append((next_yaml_child_stack_indent(lines, index, indent), item))
            continue

        if not isinstance(parent, dict):
            raise SystemExit(f"{path}:{lineno}: YAML-Schlüssel ohne Mapping-Kontext.")

        split_at = find_yaml_key_separator(content)
        if split_at is None:
            raise SystemExit(f"{path}:{lineno}: YAML-Zeile nicht verstanden: {content!r}")

        key_text = content[:split_at].strip()
        value_text = content[split_at + 1:].strip()
        if not key_text:
            raise SystemExit(f"{path}:{lineno}: Leerer YAML-Schlüssel.")

        key = parse_yaml_scalar(key_text)

        if value_text == "":
            child: dict[Any, Any] | list[Any]
            child = [] if next_yaml_child_is_list(lines, index, indent) else {}
            parent[key] = child
            stack.append((next_yaml_child_stack_indent(lines, index, indent), child))
        else:
            parent[key] = parse_yaml_scalar(value_text)

    return root


def next_yaml_child_is_list(lines: list[tuple[int, int, str]], index: int, indent: int) -> bool:
    for _, next_indent, content in lines[index + 1:]:
        if next_indent <= indent:
            return False
        if next_indent > indent:
            return content.startswith("- ")
    return False


def next_yaml_child_stack_indent(lines: list[tuple[int, int, str]], index: int, indent: int) -> int:
    for _, next_indent, _ in lines[index + 1:]:
        if next_indent > indent:
            return next_indent - 1
    return indent


def strip_yaml_comment(line: str) -> str:
    quote: str | None = None
    escaped = False
    for i, ch in enumerate(line):
        if quote == '"':
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
        elif quote == "'":
            if ch == quote:
                quote = None
        else:
            if ch in {"'", '"'}:
                quote = ch
            elif ch == "#":
                return line[:i]
    return line


def find_yaml_key_separator(content: str) -> int | None:
    quote: str | None = None
    escaped = False
    for i, ch in enumerate(content):
        if quote == '"':
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = None
        elif quote == "'":
            if ch == quote:
                quote = None
        else:
            if ch in {"'", '"'}:
                quote = ch
            elif ch == ":":
                return i
    return None


def parse_yaml_scalar(value: str) -> Any:
    if value.startswith('"') and value.endswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")

    lower = value.lower()
    if lower in {"null", "~"}:
        return None
    if lower == "true":
        return True
    if lower == "false":
        return False

    normalized = value.replace("_", "")
    try:
        return int(normalized)
    except ValueError:
        pass
    try:
        return float(normalized)
    except ValueError:
        return value


# ----------------------------------------------------------------------------
# Mini-XLSX-Schreiber (stdlib only: zipfile + xml-Strings)
# ----------------------------------------------------------------------------

def col_letter(col: int) -> str:
    """1 -> A, 27 -> AA."""
    s = ""
    while col > 0:
        col, rem = divmod(col - 1, 26)
        s = chr(65 + rem) + s
    return s


class XlsxStyle:
    """Style-Definition als Dict-Schluessel zur Deduplizierung in styles.xml."""
    __slots__ = ("font_bold", "font_color", "fill_color", "num_fmt", "align_h", "border")

    def __init__(self, font_bold=False, font_color=None, fill_color=None,
                 num_fmt=None, align_h=None, border=False):
        self.font_bold = font_bold
        self.font_color = font_color
        self.fill_color = fill_color
        self.num_fmt = num_fmt
        self.align_h = align_h
        self.border = border

    def key(self):
        return (self.font_bold, self.font_color, self.fill_color,
                self.num_fmt, self.align_h, self.border)


class XlsxSheet:
    def __init__(self, name: str):
        self.name = name
        # cells[(row, col)] = (value, formula, style_id)
        self.cells: dict[tuple[int, int], tuple[Any, str | None, int]] = {}
        self.column_widths: dict[int, float] = {}
        self.freeze: tuple[int, int] | None = None
        # cf_rules: list of (range, "ROT"/"GELB"/"GRÜN", dxf_id)
        self.cf_rules: list[tuple[str, str, int]] = []
        self.show_grid = True

    def set(self, row: int, col: int, value=None, formula: str | None = None, style_id: int = 0):
        self.cells[(row, col)] = (value, formula, style_id)

    def set_column_width(self, col: int, width: float):
        self.column_widths[col] = width

    def freeze_panes(self, row: int, col: int):
        """Friert Spalten links und Zeilen oben ein (col-1 / row-1 sichtbar)."""
        self.freeze = (row, col)


class XlsxWorkbook:
    """Minimaler XLSX-Writer mit Styles, Formeln und bedingter Formatierung."""

    NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    NS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

    def __init__(self):
        self.sheets: list[XlsxSheet] = []
        self.shared_strings: list[str] = []
        self.shared_string_idx: dict[str, int] = {}
        # Styles: erstes ist Default-Style (id 0)
        self.styles: list[XlsxStyle] = [XlsxStyle()]
        self.style_idx: dict[tuple, int] = {self.styles[0].key(): 0}
        # DXF (differential formats for conditional formatting):
        # liste von (bg_color, font_color, bold)
        self.dxfs: list[tuple[str, str, bool]] = []

    def add_sheet(self, name: str) -> XlsxSheet:
        ws = XlsxSheet(name)
        self.sheets.append(ws)
        return ws

    def add_style(self, **kwargs) -> int:
        s = XlsxStyle(**kwargs)
        k = s.key()
        if k in self.style_idx:
            return self.style_idx[k]
        self.styles.append(s)
        self.style_idx[k] = len(self.styles) - 1
        return self.style_idx[k]

    def add_dxf(self, bg_color: str, font_color: str, bold: bool = True) -> int:
        key = (bg_color, font_color, bold)
        for i, d in enumerate(self.dxfs):
            if d == key:
                return i
        self.dxfs.append(key)
        return len(self.dxfs) - 1

    def _intern_string(self, s: str) -> int:
        if s in self.shared_string_idx:
            return self.shared_string_idx[s]
        self.shared_strings.append(s)
        self.shared_string_idx[s] = len(self.shared_strings) - 1
        return self.shared_string_idx[s]

    def save(self, path: Path | str):
        # Sheets zuerst rendern (intern_string fuellt shared_strings);
        # erst danach sharedStrings.xml schreiben.
        sheet_xmls = [self._sheet_xml(ws) for ws in self.sheets]
        with zipfile.ZipFile(str(path), "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("[Content_Types].xml", self._content_types_xml())
            zf.writestr("_rels/.rels", self._rels_xml())
            zf.writestr("xl/workbook.xml", self._workbook_xml())
            zf.writestr("xl/_rels/workbook.xml.rels", self._workbook_rels_xml())
            zf.writestr("xl/styles.xml", self._styles_xml())
            zf.writestr("xl/sharedStrings.xml", self._shared_strings_xml())
            for i, xml in enumerate(sheet_xmls, start=1):
                zf.writestr(f"xl/worksheets/sheet{i}.xml", xml)

    # ----- XML-Bausteine -----

    def _content_types_xml(self) -> str:
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
            '<Default Extension="xml" ContentType="application/xml"/>',
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
            '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>',
            '<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>',
        ]
        for i in range(1, len(self.sheets) + 1):
            parts.append(
                f'<Override PartName="/xl/worksheets/sheet{i}.xml" '
                f'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            )
        parts.append("</Types>")
        return "".join(parts)

    def _rels_xml(self) -> str:
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
            'Target="xl/workbook.xml"/>'
            '</Relationships>'
        )

    def _workbook_xml(self) -> str:
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
            "<sheets>",
        ]
        for i, ws in enumerate(self.sheets, start=1):
            name = xml_escape(ws.name)
            parts.append(f'<sheet name="{name}" sheetId="{i}" r:id="rId{i}"/>')
        parts.append("</sheets></workbook>")
        return "".join(parts)

    def _workbook_rels_xml(self) -> str:
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
        ]
        rid = 1
        for i in range(1, len(self.sheets) + 1):
            parts.append(
                f'<Relationship Id="rId{rid}" '
                f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
                f'Target="worksheets/sheet{i}.xml"/>'
            )
            rid += 1
        parts.append(
            f'<Relationship Id="rId{rid}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '
            f'Target="styles.xml"/>'
        )
        rid += 1
        parts.append(
            f'<Relationship Id="rId{rid}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" '
            f'Target="sharedStrings.xml"/>'
        )
        parts.append("</Relationships>")
        return "".join(parts)

    def _styles_xml(self) -> str:
        # NumFmts: alle nicht-Builtin Format-Codes ab id 164
        custom_fmts: dict[str, int] = {}
        for s in self.styles:
            if s.num_fmt and s.num_fmt not in custom_fmts:
                custom_fmts[s.num_fmt] = 164 + len(custom_fmts)

        # Fonts: 0 = default; weitere fuer bold / Farbe
        # Wir konstruieren eindeutige Fonts pro (bold, color)
        font_keys: list[tuple[bool, str | None]] = [(False, None)]
        font_idx_map: dict[tuple[bool, str | None], int] = {(False, None): 0}
        for s in self.styles:
            k = (s.font_bold, s.font_color)
            if k not in font_idx_map:
                font_keys.append(k)
                font_idx_map[k] = len(font_keys) - 1

        # Fills: 0 = none, 1 = gray125 (Pflicht-Default), ab 2 = solid mit Farbe
        fill_colors: list[str | None] = [None, None]  # 0 + 1 sind reserviert
        fill_idx_map: dict[str | None, int] = {None: 0}
        for s in self.styles:
            if s.fill_color and s.fill_color not in fill_idx_map:
                fill_colors.append(s.fill_color)
                fill_idx_map[s.fill_color] = len(fill_colors) - 1

        # Borders: 0 = none, 1 = thin all sides
        # Wir nutzen nur diese zwei
        # cellXfs: Pflicht-Default (id 0) + alle styles
        parts: list[str] = []
        parts.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        parts.append(
            '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        )

        # numFmts
        if custom_fmts:
            parts.append(f'<numFmts count="{len(custom_fmts)}">')
            for code, fid in custom_fmts.items():
                parts.append(f'<numFmt numFmtId="{fid}" formatCode="{xml_escape(code)}"/>')
            parts.append("</numFmts>")

        # fonts
        parts.append(f'<fonts count="{len(font_keys)}">')
        for bold, color in font_keys:
            parts.append("<font>")
            parts.append('<sz val="10"/>')
            parts.append('<name val="Calibri"/>')
            if bold:
                parts.append("<b/>")
            if color:
                parts.append(f'<color rgb="FF{color}"/>')
            parts.append("</font>")
        parts.append("</fonts>")

        # fills
        parts.append(f'<fills count="{len(fill_colors)}">')
        parts.append('<fill><patternFill patternType="none"/></fill>')
        parts.append('<fill><patternFill patternType="gray125"/></fill>')
        for color in fill_colors[2:]:
            parts.append(
                f'<fill><patternFill patternType="solid">'
                f'<fgColor rgb="FF{color}"/><bgColor indexed="64"/>'
                f'</patternFill></fill>'
            )
        parts.append("</fills>")

        # borders (0 = none, 1 = thin BFBFBF auf allen Seiten)
        parts.append('<borders count="2">')
        parts.append("<border><left/><right/><top/><bottom/><diagonal/></border>")
        parts.append(
            '<border>'
            '<left style="thin"><color rgb="FFBFBFBF"/></left>'
            '<right style="thin"><color rgb="FFBFBFBF"/></right>'
            '<top style="thin"><color rgb="FFBFBFBF"/></top>'
            '<bottom style="thin"><color rgb="FFBFBFBF"/></bottom>'
            '<diagonal/>'
            "</border>"
        )
        parts.append("</borders>")

        # cellStyleXfs (Pflicht)
        parts.append('<cellStyleXfs count="1">')
        parts.append('<xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>')
        parts.append("</cellStyleXfs>")

        # cellStyles (Default-Style "Normal" zwingend benoetigt von Excel/LibreOffice/openpyxl)
        # Wird erst nach cellXfs unten geschrieben, weil cellStyles auf cellXfs[0] verweist.

        # cellXfs (eigentliche Styles)
        parts.append(f'<cellXfs count="{len(self.styles)}">')
        for s in self.styles:
            font_id = font_idx_map[(s.font_bold, s.font_color)]
            fill_id = fill_idx_map.get(s.fill_color, 0)
            border_id = 1 if s.border else 0
            num_fmt_id = custom_fmts.get(s.num_fmt, 0) if s.num_fmt else 0
            xf_attrs = [
                f'numFmtId="{num_fmt_id}"',
                f'fontId="{font_id}"',
                f'fillId="{fill_id}"',
                f'borderId="{border_id}"',
                'xfId="0"',
            ]
            if num_fmt_id:
                xf_attrs.append('applyNumberFormat="1"')
            if font_id:
                xf_attrs.append('applyFont="1"')
            if fill_id:
                xf_attrs.append('applyFill="1"')
            if border_id:
                xf_attrs.append('applyBorder="1"')
            if s.align_h:
                xf_attrs.append('applyAlignment="1"')
                parts.append(
                    f'<xf {" ".join(xf_attrs)}>'
                    f'<alignment horizontal="{s.align_h}"/>'
                    f"</xf>"
                )
            else:
                parts.append(f'<xf {" ".join(xf_attrs)}/>')
        parts.append("</cellXfs>")

        # cellStyles (Default "Normal" verweist auf cellStyleXfs[0])
        parts.append('<cellStyles count="1">')
        parts.append('<cellStyle name="Normal" xfId="0" builtinId="0"/>')
        parts.append("</cellStyles>")

        # dxfs (für conditional formatting)
        if self.dxfs:
            parts.append(f'<dxfs count="{len(self.dxfs)}">')
            for bg, fc, bold in self.dxfs:
                parts.append("<dxf>")
                parts.append("<font>")
                if bold:
                    parts.append("<b/>")
                parts.append(f'<color rgb="FF{fc}"/>')
                parts.append("</font>")
                parts.append(
                    f'<fill><patternFill><bgColor rgb="FF{bg}"/></patternFill></fill>'
                )
                parts.append("</dxf>")
            parts.append("</dxfs>")

        parts.append("</styleSheet>")
        return "".join(parts)

    def _shared_strings_xml(self) -> str:
        n = len(self.shared_strings)
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{n}" uniqueCount="{n}">',
        ]
        for s in self.shared_strings:
            # preserve-Whitespace falls am Anfang/Ende
            preserve = ' xml:space="preserve"' if (s.startswith(" ") or s.endswith(" ")) else ""
            parts.append(f"<si><t{preserve}>{xml_escape(s)}</t></si>")
        parts.append("</sst>")
        return "".join(parts)

    def _sheet_xml(self, ws: XlsxSheet) -> str:
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
        ]

        # sheetViews mit Gridlines + Freeze
        sv_attrs = []
        if not ws.show_grid:
            sv_attrs.append('showGridLines="0"')
        sv_attrs.append('workbookViewId="0"')
        parts.append("<sheetViews>")
        parts.append(f"<sheetView {' '.join(sv_attrs)}>")
        if ws.freeze:
            frow, fcol = ws.freeze
            xsplit = fcol - 1
            ysplit = frow - 1
            top_left = f"{col_letter(fcol)}{frow}"
            pane_attrs = []
            if xsplit > 0:
                pane_attrs.append(f'xSplit="{xsplit}"')
            if ysplit > 0:
                pane_attrs.append(f'ySplit="{ysplit}"')
            pane_attrs.append(f'topLeftCell="{top_left}"')
            pane_attrs.append('state="frozen"')
            parts.append(f"<pane {' '.join(pane_attrs)}/>")
        parts.append("</sheetView>")
        parts.append("</sheetViews>")

        # cols
        if ws.column_widths:
            parts.append("<cols>")
            for col, w in sorted(ws.column_widths.items()):
                parts.append(
                    f'<col min="{col}" max="{col}" width="{w}" customWidth="1"/>'
                )
            parts.append("</cols>")

        # sheetData
        parts.append("<sheetData>")
        rows_by_row: dict[int, list[tuple[int, Any, str | None, int]]] = {}
        for (r, c), (value, formula, style_id) in ws.cells.items():
            rows_by_row.setdefault(r, []).append((c, value, formula, style_id))

        for r in sorted(rows_by_row.keys()):
            parts.append(f'<row r="{r}">')
            for c, value, formula, style_id in sorted(rows_by_row[r]):
                ref = f"{col_letter(c)}{r}"
                s_attr = f' s="{style_id}"' if style_id else ""
                if formula is not None:
                    # Formel-Zelle: kein Type-Attribut, Wert wird von Excel berechnet
                    parts.append(
                        f'<c r="{ref}"{s_attr}>'
                        f'<f>{xml_escape(formula)}</f>'
                        f'</c>'
                    )
                elif value is None or value == "":
                    parts.append(f'<c r="{ref}"{s_attr}/>')
                elif isinstance(value, bool):
                    parts.append(
                        f'<c r="{ref}"{s_attr} t="b"><v>{1 if value else 0}</v></c>'
                    )
                elif isinstance(value, (int, float)):
                    parts.append(f'<c r="{ref}"{s_attr}><v>{value}</v></c>')
                else:
                    idx = self._intern_string(str(value))
                    parts.append(
                        f'<c r="{ref}"{s_attr} t="s"><v>{idx}</v></c>'
                    )
            parts.append("</row>")
        parts.append("</sheetData>")

        # conditionalFormatting (gruppiert pro range)
        cf_by_range: dict[str, list[tuple[str, int]]] = {}
        for rng, op, dxf_id in ws.cf_rules:
            cf_by_range.setdefault(rng, []).append((op, dxf_id))
        for rng, rules in cf_by_range.items():
            parts.append(f'<conditionalFormatting sqref="{rng}">')
            for pr, (op_text, dxf_id) in enumerate(rules, start=1):
                parts.append(
                    f'<cfRule type="cellIs" dxfId="{dxf_id}" priority="{pr}" '
                    f'operator="equal">'
                    f'<formula>"{op_text}"</formula>'
                    f"</cfRule>"
                )
            parts.append("</conditionalFormatting>")

        parts.append("</worksheet>")
        return "".join(parts)


# ----------------------------------------------------------------------------
# Styles (1:1 nach Vorlage) — Stdlib-Variante: Style-IDs werden zur Laufzeit
# in der Workbook registriert.
# ----------------------------------------------------------------------------

NUM_FMT = '#,##0_);[Red](#,##0)'
NUM_FMT_PCT = '0.0%'

COLOR_HEADER_GRAY = "D8D8D8"
COLOR_LIQUI_BLUE = "00CCFF"
COLOR_EIN_YELLOW = "FFFF00"
COLOR_AUS_RED = "FF0000"


# ----------------------------------------------------------------------------
# Wochenraster
# ----------------------------------------------------------------------------

def monday_of(d: dt.date) -> dt.date:
    return d - dt.timedelta(days=d.weekday())


def week_buckets(start: dt.date, n_weeks: int) -> list[tuple[int, dt.date, dt.date]]:
    mon = monday_of(start)
    weeks = []
    for i in range(n_weeks):
        a = mon + dt.timedelta(days=7 * i)
        b = a + dt.timedelta(days=6)
        _, iso_week, _ = a.isocalendar()
        weeks.append((iso_week, a, b))
    return weeks


# Vorlagen-Layout: Spalte A = Label, Spalte B = "Bestand Start"-Spalte (KW vor Start),
# Spalten C ff. = Planungs-KW.
LABEL_COL = 1   # A
START_COL = 2   # B = Bestand Start (KW vor Stichtag)
PLAN_COL_START = 3   # C ff. = KW 1 ff.

# Zeilen exakt wie Vorlage:
R_TITLE = 1
R_STAND = 2
R_BESTAND_HEADER = 6
R_KASSE = 7
R_KONTO = 8
R_LIQUI_START = 9
R_EIN_HEADER = 11
R_EIN_UMSATZ = 12
R_EIN_ANZAHLUNG = 13
R_EIN_SONST = 14
R_EIN_SUMME = 15
R_AUS_HEADER = 17
R_AUS_LOHN = 18
R_AUS_SV = 19
R_AUS_WAREN = 20
R_AUS_MIETE = 21
R_AUS_ENERGIE = 22
R_AUS_VERWALTUNG = 23
R_AUS_WERBUNG = 24
R_AUS_LEASING = 25
R_AUS_VERSICH = 26
R_AUS_BERATUNG = 27
R_AUS_SONST = 28
R_AUS_INVEST = 29
R_AUS_STEUERN = 30
R_AUS_SONST2 = 31
R_AUS_TILGUNG = 32
R_AUS_ZINSEN = 33
R_AUS_ENTNAHME = 34
R_AUS_SUMME = 35
R_CASHFLOW = 37
R_LIQUI_END = 39
# Klotzkette-Ergänzung: § 17 InsO-Block
R_FAELLIG = 41
R_LUECKE_3W = 42
R_QUOTE = 43
R_AMPEL = 44

EIN_KEYS = {
    "umsatz": R_EIN_UMSATZ,
    "anzahlungen": R_EIN_ANZAHLUNG,
    "sonstige": R_EIN_SONST,
}
AUS_KEYS = {
    "lohn": R_AUS_LOHN,
    "sv": R_AUS_SV,
    "waren": R_AUS_WAREN,
    "miete": R_AUS_MIETE,
    "energie": R_AUS_ENERGIE,
    "verwaltung": R_AUS_VERWALTUNG,
    "werbung": R_AUS_WERBUNG,
    "leasing": R_AUS_LEASING,
    "versicherung": R_AUS_VERSICH,
    "beratung": R_AUS_BERATUNG,
    "sonstige": R_AUS_SONST,
    "investitionen": R_AUS_INVEST,
    "steuern": R_AUS_STEUERN,
    "sonstige2": R_AUS_SONST2,
    "tilgung": R_AUS_TILGUNG,
    "zinsen": R_AUS_ZINSEN,
    "entnahmen": R_AUS_ENTNAHME,
}


# ----------------------------------------------------------------------------
# Sheet-Aufbau
# ----------------------------------------------------------------------------

def build_skeleton(wb: XlsxWorkbook, ws: XlsxSheet, styles: dict, daten: dict, n_weeks: int):
    """Statische Zellen und Beschriftungen anlegen."""
    ws.show_grid = False
    ws.set_column_width(1, 28)
    ws.set_column_width(START_COL, 12)
    for i in range(n_weeks):
        ws.set_column_width(PLAN_COL_START + i, 13)

    # Titel
    ws.set(R_TITLE, 1, "Liquiditätsplan", style_id=styles["bold"])
    ws.set(
        R_STAND, 1,
        f"Stand: {daten.get('stichtag', '')} – {daten.get('mandant', {}).get('name', '')}",
        style_id=styles["default"],
    )

    # Header Zeile 6 – Bestand Start
    ws.set(R_BESTAND_HEADER, LABEL_COL, "Bestand Start Planung", style_id=styles["header_gray_bold"])

    # KW-Header
    _, iso_week, _ = monday_of(dt.date.fromisoformat(daten["stichtag"])).isocalendar()
    prev_kw = iso_week - 1 if iso_week > 1 else 52
    ws.set(R_BESTAND_HEADER, START_COL, f"KW {prev_kw}", style_id=styles["bold_center"])

    stichtag = dt.date.fromisoformat(daten["stichtag"])
    for i, (kw, _a, _b) in enumerate(week_buckets(stichtag, n_weeks)):
        ws.set(R_BESTAND_HEADER, PLAN_COL_START + i, f"KW {kw}", style_id=styles["bold_center"])

    # Zeilen-Labels
    label_default = styles["default"]
    ws.set(R_KASSE, LABEL_COL, "Kassenbestand", style_id=label_default)
    ws.set(R_KONTO, LABEL_COL, "Kontostand", style_id=label_default)
    ws.set(R_LIQUI_START, LABEL_COL, "Liquidität Wochenanfang", style_id=styles["liqui_bold_num"])

    ws.set(R_EIN_HEADER, LABEL_COL, "Einnahmen", style_id=styles["ein_yellow_bold_num"])
    ws.set(R_EIN_UMSATZ, LABEL_COL, "Umsatzerlöse", style_id=label_default)
    ws.set(R_EIN_ANZAHLUNG, LABEL_COL, "erhaltene Anzahlungen", style_id=label_default)
    ws.set(R_EIN_SONST, LABEL_COL, "sonstige Einnahmen", style_id=label_default)
    ws.set(R_EIN_SUMME, LABEL_COL, "Summe Einnahmen", style_id=styles["bold_num"])

    ws.set(R_AUS_HEADER, LABEL_COL, " Ausgaben", style_id=styles["aus_red_bold_num"])
    ws.set(R_AUS_LOHN, LABEL_COL, "Löhne und Gehälter einschl. LSt", style_id=label_default)
    ws.set(R_AUS_SV, LABEL_COL, "Sozialversicherung", style_id=label_default)
    ws.set(R_AUS_WAREN, LABEL_COL, "Waren/ Material", style_id=label_default)
    ws.set(R_AUS_MIETE, LABEL_COL, "Miete", style_id=label_default)
    ws.set(R_AUS_ENERGIE, LABEL_COL, "Heizung/Strom/Wasser", style_id=label_default)
    ws.set(R_AUS_VERWALTUNG, LABEL_COL, "Verwaltung", style_id=label_default)
    ws.set(R_AUS_WERBUNG, LABEL_COL, "Werbung/Marketing", style_id=label_default)
    ws.set(R_AUS_LEASING, LABEL_COL, "Fahrzeug-/Leasingkosten", style_id=label_default)
    ws.set(R_AUS_VERSICH, LABEL_COL, "Versicherungen", style_id=label_default)
    ws.set(R_AUS_BERATUNG, LABEL_COL, "Beratungskosten", style_id=label_default)
    ws.set(R_AUS_SONST, LABEL_COL, "sonstige Ausgaben", style_id=label_default)
    ws.set(R_AUS_INVEST, LABEL_COL, "Investitionen", style_id=label_default)
    ws.set(R_AUS_STEUERN, LABEL_COL, "Betriebliche Steuern", style_id=label_default)
    ws.set(R_AUS_SONST2, LABEL_COL, "sonstige Ausgaben", style_id=label_default)
    ws.set(R_AUS_TILGUNG, LABEL_COL, "Darlehenstilgung", style_id=label_default)
    ws.set(R_AUS_ZINSEN, LABEL_COL, "Zinsen", style_id=label_default)
    ws.set(R_AUS_ENTNAHME, LABEL_COL, "Privatentnahmen", style_id=label_default)
    ws.set(R_AUS_SUMME, LABEL_COL, "Summe Ausgaben", style_id=styles["bold_num"])

    ws.set(R_CASHFLOW, LABEL_COL, "Cash Flow Woche", style_id=styles["bold_num"])
    ws.set(R_LIQUI_END, LABEL_COL, "Liquidität Woche Ende", style_id=styles["liqui_bold_num"])

    # Ampel-Block (Klotzkette-Erweiterung)
    ws.set(R_FAELLIG, LABEL_COL, "fällige Verb. Folgewoche", style_id=styles["bold_num"])
    ws.set(R_LUECKE_3W, LABEL_COL, "3-Wochen-Lücke (kumuliert)", style_id=styles["bold_num"])
    ws.set(R_QUOTE, LABEL_COL, "Lücken-Quote (%)", style_id=styles["bold_pct"])
    ws.set(R_AMPEL, LABEL_COL, "Ampel § 17 InsO", style_id=styles["bold"])


def fill_sheet(ws: XlsxSheet, styles: dict, daten: dict, n_weeks: int):
    """Werte und Formeln in die Spalten B (Start) und C..(C+n) eintragen."""
    kasse_start = float(daten.get("kassenbestand_start", 0))
    konto_start = float(daten.get("kontostand_start", 0))
    ws.set(R_KASSE, START_COL, kasse_start, style_id=styles["num"])
    ws.set(R_KONTO, START_COL, konto_start, style_id=styles["num"])
    ws.set(
        R_LIQUI_START, START_COL,
        formula=f"{col_letter(START_COL)}{R_KASSE}+{col_letter(START_COL)}{R_KONTO}",
        style_id=styles["liqui_bold_num"],
    )

    plan = daten.get("plan", {}) or {}

    for i in range(n_weeks):
        col = PLAN_COL_START + i
        L = col_letter(col)
        L_prev = col_letter(col - 1)
        kw_data: dict[str, Any] = {}
        if isinstance(plan, dict):
            kw_data = plan.get(i, plan.get(str(i), {}))
        elif isinstance(plan, list) and i < len(plan):
            kw_data = plan[i]

        # Liquidität Wochenanfang
        if i == 0:
            ws.set(R_LIQUI_START, col,
                   formula=f"{col_letter(START_COL)}{R_LIQUI_START}",
                   style_id=styles["liqui_bold_num"])
        else:
            ws.set(R_LIQUI_START, col,
                   formula=f"{L_prev}{R_LIQUI_END}",
                   style_id=styles["liqui_bold_num"])

        ein = kw_data.get("einnahmen", {}) if isinstance(kw_data, dict) else {}
        for key, row in EIN_KEYS.items():
            ws.set(row, col, float(ein.get(key, 0)), style_id=styles["num"])
        ws.set(R_EIN_SUMME, col,
               formula=f"SUM({L}{R_EIN_UMSATZ}:{L}{R_EIN_SONST})",
               style_id=styles["bold_num"])

        aus = kw_data.get("ausgaben", {}) if isinstance(kw_data, dict) else {}
        for key, row in AUS_KEYS.items():
            ws.set(row, col, float(aus.get(key, 0)), style_id=styles["num"])
        ws.set(R_AUS_SUMME, col,
               formula=f"SUM({L}{R_AUS_LOHN}:{L}{R_AUS_ENTNAHME})",
               style_id=styles["bold_num"])

        ws.set(R_CASHFLOW, col,
               formula=f"{L}{R_EIN_SUMME}-{L}{R_AUS_SUMME}",
               style_id=styles["bold_num"])

        ws.set(R_LIQUI_END, col,
               formula=f"{L}{R_LIQUI_START}+{L}{R_CASHFLOW}",
               style_id=styles["liqui_bold_num"])

        faellig = float(kw_data.get("faellig_folgewoche", 0))
        ws.set(R_FAELLIG, col, faellig, style_id=styles["num"])

    # 3-Wochen-Lücke und Quote/Ampel
    for i in range(n_weeks):
        col = PLAN_COL_START + i
        L = col_letter(col)
        if i + 2 < n_weeks:
            L1 = col_letter(col + 1)
            L2 = col_letter(col + 2)
            faellig_sum = f"{L}{R_FAELLIG}+{L1}{R_FAELLIG}+{L2}{R_FAELLIG}"
            mittel = f"{L}{R_LIQUI_END}+{L1}{R_EIN_SUMME}+{L2}{R_EIN_SUMME}"
            ws.set(R_LUECKE_3W, col,
                   formula=f"MAX(0,({faellig_sum})-({mittel}))",
                   style_id=styles["bold_num"])
            ws.set(R_QUOTE, col,
                   formula=f"IFERROR({L}{R_LUECKE_3W}/({faellig_sum}),0)",
                   style_id=styles["bold_pct"])
        else:
            ws.set(R_LUECKE_3W, col,
                   formula=f"MAX(0,{L}{R_FAELLIG}-{L}{R_LIQUI_END})",
                   style_id=styles["bold_num"])
            ws.set(R_QUOTE, col,
                   formula=f"IFERROR({L}{R_LUECKE_3W}/{L}{R_FAELLIG},0)",
                   style_id=styles["bold_pct"])
        ws.set(R_AMPEL, col,
               formula=(
                   f'IF({L}{R_QUOTE}>=0.1,"ROT",'
                   f'IF({L}{R_QUOTE}>0,"GELB","GRÜN"))'
               ),
               style_id=styles["bold_center"])

    # bedingte Formatierung Ampel
    first_col = col_letter(PLAN_COL_START)
    last_col = col_letter(PLAN_COL_START + n_weeks - 1)
    rng = f"{first_col}{R_AMPEL}:{last_col}{R_AMPEL}"
    ws.cf_rules.append((rng, "ROT", styles["dxf_rot"]))
    ws.cf_rules.append((rng, "GELB", styles["dxf_gelb"]))
    ws.cf_rules.append((rng, "GRÜN", styles["dxf_gruen"]))

    ws.freeze_panes(R_BESTAND_HEADER + 1, PLAN_COL_START)


# ----------------------------------------------------------------------------
# Fortführungsprognose und Annahmen
# ----------------------------------------------------------------------------

def build_prognose_sheet(wb: XlsxWorkbook, styles: dict, daten: dict):
    ws = wb.add_sheet("Fortfuehrungsprognose")
    ws.show_grid = False
    ws.set_column_width(1, 32)
    ws.set_column_width(2, 60)
    ws.set_column_width(3, 22)

    ws.set(1, 1, "Fortführungsprognose nach IDW S 6 / IDW S 11", style_id=styles["title14_bold"])

    for i, h in enumerate(["IDW-S-6-Element", "Befund / Annahme", "Status"]):
        ws.set(3, 1 + i, h, style_id=styles["header_gray_bold_center"])

    elemente = [
        ("1. Auftrag/Auftragsdurchführung", daten.get("prognose", {}).get("auftrag", "")),
        ("2. Basisinformationen", daten.get("prognose", {}).get("basis", "")),
        ("3. Krisenstadium und Ursachen", daten.get("prognose", {}).get("krise", "")),
        ("4. Leitbild des sanierten Unternehmens", daten.get("prognose", {}).get("leitbild", "")),
        ("5. Maßnahmen zur Krisenbewältigung", daten.get("prognose", {}).get("massnahmen", "")),
        ("6. Integrierte Planung 24+ Monate", daten.get("prognose", {}).get("planung", "")),
        ("7. Aussage Sanierungsfähigkeit", daten.get("prognose", {}).get("sanierung", "")),
        ("8. Fortbestehensprognose § 19 InsO", daten.get("prognose", {}).get("fortbestehen", "")),
    ]
    for i, (label, befund) in enumerate(elemente):
        r = 4 + i
        ws.set(r, 1, label, style_id=styles["bold_border"])
        ws.set(r, 2, befund, style_id=styles["border"])
        ws.set(r, 3, "", style_id=styles["border_center"])

    r = 4 + len(elemente) + 2
    ws.set(r, 1, "Quellen:", style_id=styles["bold"])
    quellen = [
        "BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 12 ff. (§ 17 InsO).",
        "BGH, Urt. v. 12.10.2006 – IX ZR 228/03, NJW 2007, 78 Rn. 16 ff. (Indizienkatalog).",
        "BGH, Urt. v. 19.11.2019 – II ZR 233/18, NJW 2020, 1809 Rn. 17 ff. (Fortbestehensprognose).",
        "BGH, Urt. v. 09.10.2012 – II ZR 298/11, BGHZ 195, 42 Rn. 12 ff. (insolvenzrechtl. Überschuldung).",
        "IDW S 6 (Sanierungskonzepte), IDW S 11 (Insolvenzeröffnungsgründe).",
        "K. Schmidt/Herchen, K. Schmidt, InsO, 20. Aufl. 2023, §§ 17, 19 InsO.",
        "Uhlenbruck/Mock, InsO, 16. Aufl. 2024, §§ 17, 19 InsO.",
    ]
    for i, q in enumerate(quellen):
        ws.set(r + 1 + i, 1, "• " + q, style_id=styles["default"])


def build_annahmen_sheet(wb: XlsxWorkbook, styles: dict, daten: dict):
    ws = wb.add_sheet("Annahmen")
    ws.show_grid = False
    ws.set_column_width(1, 36)
    ws.set_column_width(2, 60)

    ws.set(1, 1, "Annahmen und Inputs", style_id=styles["title14_bold"])
    rows = [
        ("Mandant", daten.get("mandant", {}).get("name", "")),
        ("Rechtsform", daten.get("mandant", {}).get("rechtsform", "")),
        ("Branche", daten.get("mandant", {}).get("branche", "")),
        ("Mitarbeiter", daten.get("mandant", {}).get("mitarbeiter", "")),
        ("Stichtag", daten.get("stichtag", "")),
        ("Kassenbestand Start", daten.get("kassenbestand_start", 0)),
        ("Kontostand Start", daten.get("kontostand_start", 0)),
        ("Kreditlinie gesamt", daten.get("kreditlinie_gesamt", 0)),
        ("Kreditlinie genutzt", daten.get("kreditlinie_genutzt", 0)),
        ("Szenario", daten.get("szenario", "Base")),
    ]
    for i, (k, v) in enumerate(rows):
        r = 3 + i
        ws.set(r, 1, k, style_id=styles["bold"])
        ws.set(r, 2, v, style_id=styles["default"])


# ----------------------------------------------------------------------------
# Styles-Registry
# ----------------------------------------------------------------------------

def build_styles(wb: XlsxWorkbook) -> dict[str, int]:
    """Registriert alle wiederkehrenden Styles als ID-Map."""
    s = {}
    s["default"] = wb.add_style()
    s["bold"] = wb.add_style(font_bold=True)
    s["num"] = wb.add_style(num_fmt=NUM_FMT)
    s["bold_num"] = wb.add_style(font_bold=True, num_fmt=NUM_FMT)
    s["bold_pct"] = wb.add_style(font_bold=True, num_fmt=NUM_FMT_PCT)
    s["bold_center"] = wb.add_style(font_bold=True, align_h="center")
    s["header_gray_bold"] = wb.add_style(
        font_bold=True, fill_color=COLOR_HEADER_GRAY, num_fmt=NUM_FMT
    )
    s["header_gray_bold_center"] = wb.add_style(
        font_bold=True, fill_color=COLOR_HEADER_GRAY, align_h="center"
    )
    s["liqui_bold_num"] = wb.add_style(
        font_bold=True, fill_color=COLOR_LIQUI_BLUE, num_fmt=NUM_FMT
    )
    s["ein_yellow_bold_num"] = wb.add_style(
        font_bold=True, fill_color=COLOR_EIN_YELLOW, num_fmt=NUM_FMT
    )
    s["aus_red_bold_num"] = wb.add_style(
        font_bold=True, fill_color=COLOR_AUS_RED, num_fmt=NUM_FMT
    )
    s["title14_bold"] = wb.add_style(font_bold=True)  # Größe vereinfacht
    s["border"] = wb.add_style(border=True)
    s["bold_border"] = wb.add_style(font_bold=True, border=True)
    s["border_center"] = wb.add_style(border=True, align_h="center")

    # DXF (für conditional formatting): (bg_color, font_color, bold)
    s["dxf_rot"] = wb.add_dxf("F4B7BA", "9C0006", bold=True)
    s["dxf_gelb"] = wb.add_dxf("FFE9A8", "8F6A00", bold=True)
    s["dxf_gruen"] = wb.add_dxf("C9E5C1", "2C6E1F", bold=True)
    return s


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eingabe", "-i", required=True, type=Path)
    parser.add_argument("--ausgabe", "-o", required=True, type=Path)
    args = parser.parse_args()

    daten = load_input(args.eingabe)

    wb = XlsxWorkbook()
    styles = build_styles(wb)

    for name, n in [("13-Wochen", 13), ("26-Wochen", 26), ("52-Wochen", 52)]:
        ws = wb.add_sheet(name)
        build_skeleton(wb, ws, styles, daten, n)
        fill_sheet(ws, styles, daten, n)

    build_prognose_sheet(wb, styles, daten)
    build_annahmen_sheet(wb, styles, daten)

    wb.save(args.ausgabe)
    print(f"OK: geschrieben nach {args.ausgabe}")


if __name__ == "__main__":
    main()
