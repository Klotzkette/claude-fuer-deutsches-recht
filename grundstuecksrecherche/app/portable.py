"""Package a file-openable website; never fetch services or silently include case data."""

from __future__ import annotations

import argparse
from copy import deepcopy
from io import BytesIO
import json
from pathlib import Path
import zipfile

from documents import validate_case

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / 'static'
PUBLIC_PROFILE_FIELDS = ('name', 'state', 'district', 'municipality_code', 'center', 'bounds', 'source_url')
SCRIPTS = ('portable-bundle.js', 'vendor/docx.iife.js', 'vendor/fflate.iife.js',
           'portable-document-templates.js', 'portable-documents.js', 'portable-runtime.js')
ASSETS = ('app.js', 'styles.css', 'portable-documents.js', 'portable-runtime.js')

README = """1. Grundstücksrecherche als portable Website

Entpacken Sie das gesamte ZIP in einen Ordner. Öffnen Sie dort index.html per
Doppelklick in einem aktuellen Browser. JavaScript muss aktiviert sein.
Python, ein Terminal und ein lokaler Webserver sind hierfür nicht erforderlich.
Lassen Sie die Dateien und den Ordner vendor zusammen; öffnen Sie die Website
nicht innerhalb der ZIP-Vorschau des Dateimanagers.

2. Vorgang und Dokumente

Die Website beginnt leer. Ein mitgelieferter Ort oder ausdrücklich eingeschlossener
Vorgang wird erst über den entsprechenden Button geöffnet. Eingaben, manuelle
Flurstücke, JSON-Sicherung sowie vier bearbeitbare DOCX-Entwürfe und das
Dokumenten-ZIP werden im Browser verarbeitet. Drucken bietet je nach Browser
auch Speichern als PDF. Es wird nichts versandt oder automatisch beauftragt.
Eine lokale Browserspeicherung bei file:// ist browserabhängig; bewahren Sie
wichtige Vorgänge zusätzlich als JSON auf.

3. Karten und Grenzen

Die Kartenbibliothek und Dokumentenwerkzeuge liegen vollständig im ZIP.
Neue Kartenbilder, Ortssuchen sowie Flurstücksabfragen benötigen
Internet und einen Browserzugriff, den der jeweilige amtliche Dienst erlaubt.
Das ZIP enthält keine heruntergeladenen Kartenkacheln und keine bundesweite
Offline-Katasterdatenbank. Direkter Browserzugriff ersetzt nicht die weitergehende
Katalog- und Zuständigkeitsrecherche der App mit Python-Laufzeit. Die Adresssuche
ist nur dort verfügbar; in der portablen Website wählen Sie den Kartenausschnitt
oder setzen einen Lagehinweis. Dienstfehler
oder CORS-Sperren werden angezeigt; bitte keine Browsersicherheitsoptionen
abschalten. Verwenden Sie dann einen mitgelieferten Ort, einen JSON-Vorgang,
manuelle Flurstücksangaben oder den App-Betrieb für die erneute Quellenprüfung.
Offene Karten belegen kein Eigentum. Prüfen Sie Interesse, Zuständigkeit,
Nachweise und Freigabe vor der Verwendung der Schreiben.

4. Weitergabe

Standardmäßig enthält das ZIP nur Software und gegebenenfalls den ausgewählten
öffentlichen Ort. Absender, Empfänger, Auswahl und Begründungen werden nur bei
ausdrücklicher Auswahl eingeschlossen. Der Exportstatus steht unten. Die Datei
portable-bundle.js ist kein verschlüsselter Datenspeicher. Ein eingeschlossener
Vorgang ist für jeden Empfänger des ZIP lesbar. Geben Sie ihn nur berechtigt weiter.

5. English

Extract the entire ZIP and open index.html in a current browser. No Python or
local server is needed. Keep all bundled files together. Forms and document
generation run locally. Live maps, searches and cadastral requests still need
internet and permission from the data provider for cross-origin browser access.
An included location or case is opened explicitly, never silently. Case details
are excluded by default; if included, they are readable by everyone receiving
this archive. Review every draft before use. Nothing is sent automatically.
"""


def json_script(value):
    # External script rather than fetch: local-file browsers disallow JSON fetches.
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(',', ':'))
    return encoded.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def build_website(raw_case=None, *, include_case=False):
    if not isinstance(include_case, bool):
        raise ValueError('Die Aufnahme des Vorgangs muss ausdrücklich gewählt werden.')
    case = validate_case({} if raw_case is None else raw_case)
    original_profile = case.get('profile') or {}
    profile = {key: deepcopy(original_profile[key]) for key in PUBLIC_PROFILE_FIELDS if key in original_profile}
    if not profile.get('name') or not profile.get('center'):
        profile = None
    if include_case and profile is None:
        raise ValueError('Für einen Website-Export mit Vorgang zuerst einen Ort auswählen.')
    catalog = json.loads((ROOT / 'catalogs.json').read_text(encoding='utf-8'))
    public_catalog = {key: catalog[key] for key in ('allowed_hosts', 'places', 'providers')}
    bundle = {'catalogs': public_catalog, 'profile': profile, 'case': case if include_case else None}
    from portable_templates import template_script

    origins = sorted({'https://' + host for host in catalog['allowed_hosts']})
    policy = ("default-src 'none'; script-src 'self' file:; style-src 'self' file: 'unsafe-inline'; "
              "img-src 'self' file: data: blob: " + ' '.join(origins) + "; connect-src " + ' '.join(origins) + "; "
              "frame-src 'self' file: blob:; font-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'")
    html = (STATIC / 'index.html').read_text(encoding='utf-8')
    html = html.replace('  <!-- PORTABLE-SCRIPTS -->', '\n'.join(f'  <script defer src="./{name}"></script>' for name in SCRIPTS))
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <meta http-equiv="Content-Security-Policy" content="' + policy + '">')
    entries = {
        'index.html': html.encode('utf-8'),
        'portable-bundle.js': ('window.PORTABLE_BUNDLE=' + json_script(bundle) + ';\n').encode('utf-8'),
        'portable-document-templates.js': template_script().encode('utf-8'),
        'README.txt': (README + '\nExportstatus: ' + ('Mit Vorgangsdaten. / Includes case data.' if include_case else 'Ohne Vorgangsdaten. / No case data.') + '\n').encode('utf-8'),
    }
    for name in ASSETS:
        entries[name] = (STATIC / name).read_bytes()
    for file in sorted((STATIC / 'vendor').rglob('*')):
        if file.is_file() and not file.is_symlink():
            entries[file.relative_to(STATIC).as_posix()] = file.read_bytes()
    for name in SCRIPTS:
        if name not in entries:
            raise ValueError(f'Die Website-Abhängigkeit {name} fehlt.')
    if sum(len(data) for data in entries.values()) > 15 * 1024 * 1024:
        raise ValueError('Das Website-Paket überschreitet die Größenbegrenzung.')
    output = BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description='Portable Website zum direkten Öffnen von index.html verpacken.')
    parser.add_argument('output', type=Path)
    parser.add_argument('--case', type=Path)
    parser.add_argument('--include-case', action='store_true')
    args = parser.parse_args()
    raw = {}
    if args.case:
        if args.case.stat().st_size > 2 * 1024 * 1024:
            parser.error('Vorgangsdatei überschreitet 2 MiB.')
        raw = json.loads(args.case.read_text(encoding='utf-8'))
    data = build_website(raw, include_case=args.include_case)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
    print(f'Website-ZIP: {args.output} ({len(data)} Bytes)')


if __name__ == '__main__':
    main()
