"""Prüfvertrag der zehn vollständigen Werkstattprompts und ihrer Exporte."""
from __future__ import annotations
import hashlib
import io
import json
from pathlib import Path
import re
import unicodedata
import zipfile
from urllib.parse import urljoin
from pypdf import PdfReader

VERSION = '445.36.2'
CHECKED_ON = '2026-11-15'
PDF_FOOTER = 'Quellenprüfung 15.11.2026 | ' + VERSION
MODULES = (
    '130-kongruente-deckung.md', '131-inkongruente-deckung.md',
    '132-unmittelbare-benachteiligung.md', '133-vorsatzanfechtung.md',
    '134-unentgeltliche-leistung.md', '135-gesellschafterdarlehen.md',
    '136-stille-gesellschaft.md', '137-wechsel-und-scheckzahlungen.md',
    '138-nahestehende-personen.md', '139-fristen-und-antragsauswahl.md',
)
ASSETS = {'insolvenzanfechtung-tatbestandswerkstaetten.pdf', 'insolvenzanfechtung-tatbestandswerkstaetten.zip'}
EVIDENCE = 'quality/insolvenzanfechtung/tatbestandswerkstaetten-2026-11-15/umfang.json'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized(text: str) -> str:
    # Nur Satz-Whitespace entfernen. Dezimal-/Tausenderzeichen, Vorzeichen,
    # Prozent/Promille, Vergleichszeichen und Wortlaut bleiben erhalten.
    return ''.join(char for char in unicodedata.normalize('NFC', text) if not char.isspace())


def visible_source(text: str) -> str:
    # Nur tatsächlich verwendete Markdown-Darstellungssyntax entfernen.
    # Linkziele werden gesondert gegen die PDF-Annotationen geprüft.
    text = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', r'\1', text)
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('```') or re.fullmatch(r'[-=_]{3,}', line):
            continue
        if line.startswith('|'):
            if re.fullmatch(r'[|:\-\s]+', line):
                continue
            line = ' '.join(cell.strip() for cell in line.strip('|').split('|'))
        elif re.match(r'^[-*]\s+', line):
            line = '• ' + line[2:]
        else:
            line = re.sub(r'^#{1,6}\s+', '', line)
            line = line.lstrip('> ')
        line = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)
        line = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\1', line)
        line = re.sub(r'`([^`]+)`', r'\1', line)
        lines.append(line)
    return normalized(' '.join(lines))


def _page_texts(pages, section: int) -> tuple[str, int]:
    """Prüft Einzel- und Sammelfassung mit denselben echten Seitenmerkmalen."""
    parts = []
    for n, page in enumerate(pages, 1):
        lines = (page.extract_text() or '').splitlines()
        if (len(lines) < 4 or lines[0] != f'INSOLVENZANFECHTUNG | WERKSTATT {section}'
                or lines[1] != PDF_FOOTER or lines[2] != str(n)):
            raise ValueError(f'{section}: Kopf-/Fußzeile oder Seitenfolge fehlerhaft')
        parts.append(' '.join(lines[3:]))
        fonts = page['/Resources'].get('/Font', {}).get_object()
        used = {str(font.get_object().get('/BaseFont', '')) for font in fonts.values()}
        if not any('TimesNewRoman' in name for name in used):
            raise ValueError(f'{section}: Times New Roman fehlt')
    return normalized(' '.join(parts)), len(parts)


def pdf_body(data: bytes, section: int) -> tuple[str, int]:
    return _page_texts(PdfReader(io.BytesIO(data)).pages, section)


def _consecutive_unique(values: list[str]) -> list[str]:
    # ReportLab erstellt bei einem Zeilen-/Seitenumbruch mehrere Annotationen
    # für denselben sichtbaren Hyperlink. Nur unmittelbar gleiche Ziele bündeln.
    return [value for n, value in enumerate(values) if n == 0 or value != values[n - 1]]


def source_link_targets(text: str, source: str) -> list[str]:
    base = 'https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/' + str(Path(source).parent) + '/'
    targets = re.findall(r'\[[^\]]+\]\(([^\s)]+)\)', text)
    return _consecutive_unique([urljoin(base, target) for target in targets])


def pdf_link_targets(pages) -> list[str]:
    targets = []
    for page in pages:
        for annotation in page.get('/Annots', []):
            link = annotation.get_object()
            if link.get('/Subtype') != '/Link':
                continue
            action = link.get('/A')
            if action is None:
                raise ValueError('PDF-Linkannotation ohne überprüfbares Ziel')
            action = action.get_object()
            if action.get('/S') != '/URI' or not isinstance(action.get('/URI'), str):
                raise ValueError('PDF-Linkannotation mit unerwarteter Zielart')
            targets.append(str(action['/URI']))
    return _consecutive_unique(targets)


def validate_exports(root: Path, evidence_path: Path, archive_path: Path, handbook_path: Path) -> dict:
    evidence_bytes = evidence_path.read_bytes()
    report = json.loads(evidence_bytes)
    rows = report.get('modules', [])
    if (report.get('schema_version'), report.get('version'), report.get('font'), report.get('font_size'), report.get('module_count'), report.get('checked_on')) != (1, VERSION, 'Times New Roman', 11, 10, CHECKED_ON):
        raise ValueError('Werkstattnachweis: Schema, Version, Schrift oder Umfang falsch')
    if [Path(row['source']).name for row in rows] != list(MODULES):
        raise ValueError('Zehn konkrete Werkstattquellen in Normreihenfolge erforderlich')
    expected = {'README.txt', 'umfang.json'}
    for filename in MODULES:
        expected.update({'Markdown/'+filename, 'Text/'+Path(filename).with_suffix('.txt').name,
                         'PDF/'+Path(filename).with_suffix('.pdf').name})
    module_texts = []
    module_links = []
    with zipfile.ZipFile(archive_path) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or set(names) != expected or z.testzip():
            raise ValueError('Werkstatt-ZIP: fehlende, doppelte oder zusätzliche Mitglieder')
        if z.read('umfang.json') != evidence_bytes or not z.read('README.txt').strip():
            raise ValueError('Werkstatt-ZIP: Umfangsnachweis oder Leserhinweis fehlt')
        for section, (row, filename) in enumerate(zip(rows, MODULES), 130):
            expected_source = 'insolvenzanfechtung/werkstattprompts/'+filename
            if row['source'] != expected_source or row['section'] != section or row['pdf'] != Path(filename).with_suffix('.pdf').name:
                raise ValueError('Werkstattquelle oder Zuordnung falsch')
            source = root / expected_source
            data = source.read_bytes()
            if source.is_symlink() or sha(data) != row['source_sha256'] or len(data) != row['utf8_bytes']:
                raise ValueError(f'{section}: Quellbytes stimmen nicht')
            words = len(data.decode().split())
            if words != row['words'] or words < 5500:
                raise ValueError(f'{section}: vollständiger Großprompt mit mindestens 5500 Wörtern erforderlich')
            if z.read('Markdown/'+filename) != data or z.read('Text/'+Path(filename).with_suffix('.txt').name) != data:
                raise ValueError(f'{section}: Markdown/TXT nicht bytegleich zur Quelle')
            pdf = z.read('PDF/'+row['pdf'])
            text, pages = pdf_body(pdf, section)
            if sha(pdf) != row['pdf_sha256'] or pages != row['pages'] or not 16 <= pages <= 26:
                raise ValueError(f'{section}: PDF-Hash/Seitenumfang muss stimmen und etwa 20 Seiten betragen (16–26)')
            if text != visible_source(data.decode()):
                raise ValueError(f'{section}: PDF enthält nicht den vollständigen sichtbaren Quelltext in Quellreihenfolge')
            links = source_link_targets(data.decode(), expected_source)
            if pdf_link_targets(PdfReader(io.BytesIO(pdf)).pages) != links:
                raise ValueError(f'{section}: PDF-Linkziele stimmen nicht mit den Quellenverweisen überein')
            module_texts.append(text)
            module_links.append(links)
    handbook = handbook_path.read_bytes()
    reader = PdfReader(io.BytesIO(handbook))
    if sha(handbook) != report['handbook_sha256'] or len(reader.pages) != report['pages'] or report['pages'] != sum(row['pages'] for row in rows):
        raise ValueError('Sammel-PDF: Hash oder vollständige Seitensumme falsch')
    offset = 0
    for row, expected_text, expected_links in zip(rows, module_texts, module_links):
        pages = reader.pages[offset:offset+row['pages']]
        actual, count = _page_texts(pages, row['section'])
        if count != row['pages'] or actual != expected_text:
            raise ValueError('Sammel-PDF: Modul fehlt oder wurde verändert')
        if pdf_link_targets(pages) != expected_links:
            raise ValueError('Sammel-PDF: Linkziele wurden verändert')
        offset += row['pages']
    return report
