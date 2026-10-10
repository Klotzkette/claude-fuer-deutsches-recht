#!/usr/bin/env python3
"""Baut Due Diligence 1.0.0 aus elf Skills, drei Prompts und drei Testakten.

Word-Unterlagen und gespiegelte Office-Dateien werden nativ mit LibreOffice
gerendert. Die Bank-XLSX erhält eine lesbare Druckansicht aus geprüften
Formelcaches. Das Gesamt-PDF entsteht aus genau den Einzel-PDFs; Originaldateien
bleiben unverändert.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import zipfile

from dd_bankakte_pdf import FILENAME as BANK_WORKBOOK, render as render_bank_workbook

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate

from prompt_profiles import PROMPT_SUFFIXES
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import office_binary, valid_office_container

ROOT = Path(__file__).resolve().parents[1]
NAME = 'due-diligence'
VERSION = '1.0.0'
CASES = ('dd-arbeitsvertraege-innovation-berlin', 'dd-corporate-silberfalke',
         'dd-bankfiliale-verbraucherdarlehen-erfurt')
KINDS = ('werkstatt', 'schnellstart', 'hauptproblem')


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT / 'scripts' / filename)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def asset_names():
    return {f'{NAME}{suffix}.zip' for suffix in ('', '-portable')} | {
        f'{NAME}-{kind}.{ext}' for kind in KINDS for ext in ('md', 'txt', 'pdf')
    } | {f'testakte-{case}{suffix}.zip' for case in CASES for suffix in ('', '-einzelpdfs')} | {
        f'{case}_gesamt.pdf' for case in CASES
    }


def plugin_sources():
    plugin = ROOT / NAME
    result = []
    for path in sorted(plugin.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symbolischer Link nicht zulässig: {path}')
        if not path.is_file():
            continue
        if path.name in {'.DS_Store', 'CLAUDE.md'} or path.suffix == '.pyc' or '__pycache__' in path.parts:
            continue
        if path.name.endswith(PROMPT_SUFFIXES):
            continue
        if path.suffix.lower() in {'.pdf', '.docx', '.eml'} or 'testakten' in path.parts:
            raise ValueError(f'Akteninhalt gehört nicht ins Plugin-ZIP: {path}')
        result.append(path)
    return result


def render_prompt(source, target):
    """Zentralen Markdown-Renderer mit dem Repository-Schriftstandard nutzen."""
    render = module('build-testakte-gesamt-pdf.py')
    font_dir = Path('/System/Library/Fonts/Supplemental')
    font_files = ('Times New Roman.ttf', 'Times New Roman Bold.ttf')
    font_label = 'Times New Roman'
    if not all((font_dir / filename).is_file() for filename in font_files):
        font_dir = Path('/usr/share/fonts/truetype/liberation2')
        font_files = ('LiberationSerif-Regular.ttf', 'LiberationSerif-Bold.ttf')
        font_label = 'Liberation Serif (Ersatz für Times New Roman)'
    for name, filename in zip(('DD-Regular', 'DD-Bold'), font_files):
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily('DD-Regular', normal='DD-Regular', bold='DD-Bold', italic='DD-Regular', boldItalic='DD-Bold')
    render.FONT_REG, render.FONT_BOLD = 'DD-Regular', 'DD-Bold'
    for style in (render.s_body, render.s_meta):
        style.fontName, style.fontSize, style.leading = 'DD-Regular', 11, 14.3
    for style in (render.s_h1, render.s_h2, render.s_h3):
        style.fontName = 'DD-Bold'
        style.keepWithNext = True
    flow = render.md_to_flowables(source.read_text(encoding='utf-8'))
    def footer(canvas, document):
        canvas.setFont('DD-Regular', 8)
        canvas.drawString(55, 27, f'Due Diligence 1.0.0 | {font_label} 11 pt')
        canvas.drawRightString(A4[0] - 55, 27, str(document.page))
    doc = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=55, rightMargin=55,
                           topMargin=50, bottomMargin=50, invariant=1,
                           title=source.stem, author='Klotzkette', subject=f'{font_label} 11 pt')
    doc.build(flow, onFirstPage=footer, onLaterPages=footer)
    if not PdfReader(target).pages:
        raise ValueError(f'Leere Prompt-Lesefassung: {source.name}')
    print(f'Lesefassung {source.name}: {font_label}, {len(PdfReader(target).pages)} Seiten', flush=True)


def build(destination):
    if not office_binary():
        raise RuntimeError('LibreOffice fehlt; keine Veröffentlichung aus bloßer Office-Textextraktion.')
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError('Das Ausgabeziel muss leer sein.')
    plugin = ROOT / NAME
    manifests = [json.loads((plugin / p).read_text()) for p in
                 ('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json')]
    if {(m['name'], m['version']) for m in manifests} != {(NAME, VERSION)}:
        raise ValueError('Manifestversionen stimmen nicht überein.')
    if len(list((plugin / 'skills').glob('*/SKILL.md'))) != 11:
        raise ValueError('Genau elf Skills erforderlich.')
    for kind in KINDS:
        source = plugin / f'{NAME}-{kind}.md'
        twin = source.with_suffix('.txt')
        if source.read_bytes() != twin.read_bytes():
            raise ValueError(f'Promptfassungen weichen ab: {kind}')
        if kind != 'werkstatt' and len(source.read_bytes()) > 7500:
            raise ValueError(f'Kompaktprompt zu lang: {kind}')
        for path in (source, twin):
            shutil.copyfile(path, destination / path.name)
        render_prompt(source, destination / source.with_suffix('.pdf').name)
    sources = plugin_sources()
    for portable in (False, True):
        prefix = f'{NAME}/' if portable else ''
        with zipfile.ZipFile(destination / f'{NAME}{"-portable" if portable else ""}.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
            for source in sources + [ROOT / 'LICENSE']:
                name = source.relative_to(plugin).as_posix() if source != ROOT / 'LICENSE' else 'LICENSE'
                info = zipfile.ZipInfo(prefix + name, (2026, 10, 10, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, source.read_bytes())
    individual = module('build-testakten-einzelpdf-zips.py')
    originals = module('build-testakten-release-zips.py')
    for case in CASES:
        directory = ROOT / 'testakten' / case
        for source, _ in document_arcname_pairs(directory):
            if source.suffix.lower() in {'.docx', '.xlsx', '.odt'} and not valid_office_container(source):
                raise ValueError(f'Kein gültiges natives Office-Dokument: {source}')
        native_render_batch = individual.render_office_batch
        bank_workbook = directory / BANK_WORKBOOK
        def render_readable_bank_batch(paths):
            targeted = [path for path in paths if path == bank_workbook]
            rendered = native_render_batch([path for path in paths if path not in targeted])
            for path in targeted:
                rendered[path] = render_bank_workbook(path)
            return rendered
        try:
            if case == CASES[2]:
                individual.render_office_batch = render_readable_bank_batch
            individual_path, count = individual.build_single(directory, destination)
        finally:
            individual.render_office_batch = native_render_batch
        writer = PdfWriter()
        with zipfile.ZipFile(individual_path) as archive:
            for source, arcname in document_arcname_pairs(directory):
                writer.append(io.BytesIO(archive.read(arcname)), outline_item=source.relative_to(directory).as_posix())
        target = directory / 'gesamt-pdf' / f'{case}_gesamt.pdf'
        target.parent.mkdir(parents=True, exist_ok=True)
        writer.add_metadata({'/Title': f'Due Diligence: {case}', '/Author': 'Kanzleiakte'})
        writer.write(target)
        originals.build_single(directory, destination)
        shutil.copyfile(target, destination / target.name)
        print(f'{case}: {count} Einzel-PDFs, {len(PdfReader(target).pages)} Gesamtseiten', flush=True)
    actual = {p.name for p in destination.iterdir()}
    if actual != asset_names():
        raise ValueError(f'Assetliste weicht ab: {actual ^ asset_names()}')
    (destination / 'checksums-sha256.txt').write_text(''.join(
        f'{hashlib.sha256((destination / name).read_bytes()).hexdigest()}  {name}\n' for name in sorted(actual)), encoding='utf-8')
    print(json.dumps({'version': VERSION, 'assets': len(actual) + 1, 'destination': str(destination)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    build(parser.parse_args().dist.resolve())
