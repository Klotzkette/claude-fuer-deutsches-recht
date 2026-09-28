#!/usr/bin/env python3
"""PPTX-Paket offline prüfen, ohne Dateien zu ändern oder Links aufzurufen."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile
from zlib import error as CompressionError

MAX_BYTES = 100 * 1024 * 1024
MAX_PARTS = 10000
MAX_XML_BYTES = 16 * 1024 * 1024
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_R = "http://schemas.openxmlformats.org/package/2006/relationships"


def normalized(value: str) -> str:
    return ' '.join(unicodedata.normalize("NFKC", value).casefold().split())


class NoDoctype(ET.TreeBuilder):
    def doctype(self, name, pubid, system):
        raise ValueError("XML mit DTD oder Entitäten ist nicht zugelassen.")


def inspect(path: Path, forbidden: tuple[str, ...] = (), template: bool = False) -> dict:
    result = {"file": path.name, "errors": [], "warnings": [], "slides": 0,
              "layouts": 0, "animations": 0, "visual_check": "nicht durchgeführt",
              "playback_check": "nicht durchgeführt"}
    errors, warnings = result["errors"], result["warnings"]
    try:
        if path.stat().st_size > MAX_BYTES:
            raise ValueError("Datei überschreitet das Prüfbudget von 100 MiB.")
        with ZipFile(path) as archive:
            infos = archive.infolist()
            names = [info.filename for info in infos]
            if len(infos) > MAX_PARTS or sum(i.file_size for i in infos) > MAX_BYTES:
                raise ValueError("Entpackter Inhalt überschreitet das Prüfbudget.")
            if len(names) != len(set(names)):
                raise ValueError("Doppelte Paketpfade.")
            for info in infos:
                if info.flag_bits & 1:
                    raise ValueError("Verschlüsseltes Paket kann nicht geprüft werden.")
                if (info.filename.startswith('/') or '\\' in info.filename or
                        any(p in ('..', '.') for p in info.filename.split('/'))):
                    raise ValueError("Unsicherer Paketpfad.")
            parts = {i.filename for i in infos if not i.is_dir()}
            xml, total = {}, 0
            for info in infos:
                if info.is_dir():
                    continue
                is_xml = info.filename.endswith(('.xml', '.rels'))
                if is_xml and info.file_size > MAX_XML_BYTES:
                    raise ValueError("XML-Bestandteil überschreitet das Prüfbudget.")
                # Medien nur streamen; XML erst nach tatsächlicher Größenprüfung parsen.
                chunks, size = [], 0
                with archive.open(info) as stream:
                    while True:
                        chunk = stream.read(min(1024 * 1024, MAX_BYTES - total + 1))
                        if not chunk:
                            break
                        total += len(chunk)
                        size += len(chunk)
                        if total > MAX_BYTES or (is_xml and size > MAX_XML_BYTES):
                            raise ValueError("Entpackter Inhalt überschreitet das Prüfbudget.")
                        if is_xml:
                            chunks.append(chunk)
                if is_xml:
                    xml[info.filename] = ET.fromstring(
                        b''.join(chunks), parser=ET.XMLParser(target=NoDoctype()))
        for required in ('[Content_Types].xml', '_rels/.rels', 'ppt/presentation.xml',
                         'ppt/_rels/presentation.xml.rels'):
            if required not in xml:
                errors.append(f"Pflichtbestandteil fehlt: {required}")
        if errors:
            return result
        embedded = {name for name in parts if name.lower().startswith('ppt/embeddings/')}
        resolved_relations = {}
        slide_parts = {name for name, root in xml.items() if root.tag == f'{{{P}}}sld'}
        for name in parts:
            if re.search(r'(?:vbaProject|/activeX/)', name, re.I):
                errors.append(f"Aktiver oder nicht transparent prüfbarer Altbestand: {name}")
        for name, root in xml.items():
            combined = ' '.join(root.itertext()) + ' ' + ' '.join(v for n in root.iter() for v in n.attrib.values())
            run_text = ''.join(text for text in root.itertext() if text.strip())
            searchable = (normalized(combined), normalized(run_text))
            for term in forbidden:
                needle = normalized(term)
                if needle and any(needle in haystack for haystack in searchable):
                    errors.append(f"Vorgegebener Suchbegriff gefunden: {name}")
            if name.endswith('.rels'):
                owner = '' if name == '_rels/.rels' else str(PurePosixPath(name).parent.parent / PurePosixPath(name).name[:-5])
                if root.tag != f'{{{PACKAGE_R}}}Relationships' or any(
                        rel.tag != f'{{{PACKAGE_R}}}Relationship' for rel in root):
                    errors.append(f"Ungültige Beziehungsstruktur: {name}")
                    continue
                if owner and owner not in parts:
                    errors.append(f"Beziehungsquelle fehlt: {name}")
                ids = [rel.get('Id') for rel in root]
                if any(not value or not value.strip() for value in ids) or len(ids) != len(set(ids)):
                    errors.append(f"Fehlende oder doppelte Beziehungs-ID: {name}")
                for rel in root:
                    target = rel.get('Target', '')
                    if not target.strip():
                        errors.append(f"Verknüpfungsziel fehlt: {name}")
                        continue
                    if rel.get('TargetMode', 'Internal') not in ('Internal', 'External'):
                        errors.append(f"Ungültiger Beziehungsmodus: {name}")
                        continue
                    if rel.get('TargetMode') == 'External':
                        warnings.append(f"Externe Verknüpfung manuell prüfen: {owner}")
                        continue
                    uri = urlsplit(target)
                    if uri.scheme or uri.netloc or uri.query or '\\' in target:
                        errors.append(f"Ungültiges internes Verknüpfungsziel: {name}")
                        continue
                    raw = unquote(uri.path)
                    resolved = posixpath.normpath(raw.lstrip('/') if raw.startswith('/') else posixpath.join(posixpath.dirname(owner), raw))
                    if not raw or resolved not in parts:
                        errors.append(f"Internes Verknüpfungsziel fehlt: {name} -> {target}")
                    else:
                        resolved_relations[(owner, rel.get('Id'))] = resolved
                        if rel.get('Type') in (f'{R}/oleObject', f'{R}/package'):
                            embedded.add(resolved)
            if name in slide_parts:
                result['slides'] += 1
                if root.get('show') == '0':
                    warnings.append(f"Ausgeblendete Folie: {name}")
                ids = [n.get('id') for n in root.iter(f'{{{P}}}cNvPr')]
                if len(ids) != len(set(ids)):
                    errors.append(f"Doppelte Objekt-ID: {name}")
                for target in root.iter(f'{{{P}}}spTgt'):
                    if target.get('spid') not in ids:
                        errors.append(f"Animationsziel fehlt: {name}")
                result['animations'] += sum(1 for _ in root.iter(f'{{{P}}}animEffect'))
                if not template and re.search(r'\[[^\]\n]+\]|Lorem ipsum|Mastertitelformat', combined, re.I):
                    warnings.append(f"Mögliches unersetztes Inhaltsfeld: {name}")
            if re.fullmatch(r'ppt/slideLayouts/slideLayout\d+\.xml', name):
                result['layouts'] += 1
            if name.startswith(('ppt/notesSlides/', 'ppt/comments/')) and name.endswith('.xml'):
                warnings.append(f"Notizen oder Kommentare vor Weitergabe prüfen: {name}")
        presentation = xml['ppt/presentation.xml']
        if presentation.tag != f'{{{P}}}presentation':
            errors.append("Ungültiges Wurzelelement in ppt/presentation.xml.")
        entries = presentation.findall(f'{{{P}}}sldIdLst/{{{P}}}sldId')
        rels = {r.get('Id'): r for r in xml['ppt/_rels/presentation.xml.rels']}
        slide_ids = [n.get('id') for n in entries]
        if (not entries or any(not value or not value.strip() for value in slide_ids)
                or len(slide_ids) != len(set(slide_ids))):
            errors.append("Folienfolge fehlt oder enthält leere oder doppelte IDs.")
        targets = []
        for entry in entries:
            relation_id = entry.get(f'{{{R}}}id')
            rel = rels.get(relation_id)
            if (rel is None or rel.get('Type') != f'{R}/slide'
                    or rel.get('TargetMode', 'Internal') != 'Internal'):
                errors.append("Folienfolge enthält einen ungültigen Folienverweis.")
                continue
            target = resolved_relations.get(('ppt/presentation.xml', relation_id))
            if target not in slide_parts:
                errors.append("Folienverweis zeigt nicht auf einen gültigen Folienbestandteil.")
                continue
            targets.append(target)
        if len(targets) != len(set(targets)):
            errors.append("Ein Folienbestandteil wird mehrfach in der Folienfolge verwendet.")
        for name in sorted(slide_parts - set(targets)):
            warnings.append(f"Folien-Datei außerhalb der Folienfolge: {name}")
        for name in sorted(embedded):
            # Auch reguläre Diagrammtabellen können nicht sichtbare Daten enthalten.
            if Path(name).suffix.lower() in {'.xlsx', '.docx', '.pptx'}:
                warnings.append(f"Eingebettete Office-Datei vollständig manuell prüfen; Inhalt nicht untersucht: {name}")
            else:
                errors.append(f"Aktiver oder nicht transparent prüfbarer Altbestand: {name}")
    except (OSError, ValueError, BadZipFile, ET.ParseError, RuntimeError,
            NotImplementedError, EOFError, CompressionError) as exc:
        errors.append(str(exc))
    result['errors'] = sorted(set(errors))
    result['warnings'] = sorted(set(warnings))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pptx', type=Path)
    parser.add_argument('--forbid-term', action='append', default=[], help='Zusätzlicher Begriff, der nicht vorkommen darf')
    parser.add_argument('--template', action='store_true', help='Beabsichtigte Vorlagenfelder nicht beanstanden')
    args = parser.parse_args()
    result = inspect(args.pptx, tuple(t for t in args.forbid_term if t.strip()), args.template)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(result['errors']))


if __name__ == '__main__':
    sys.exit(main())
