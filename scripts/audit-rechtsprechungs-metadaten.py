#!/usr/bin/env python3
"""Vergleicht ausdrücklich datierte Aktenzeichen mit amtlichen Entscheidungsindizes."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlencode
from urllib.request import urlopen
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FEDERAL = ('BVerfG', 'BVerwG', 'BGH', 'BAG', 'BFH', 'BSG', 'BPatG')
EU = ('EuGH', 'EuG')
COURTS = {name.lower(): name for name in (*FEDERAL, *EU)}
COURT_NAMES = '|'.join(COURTS)
MONTHS = 'januar februar märz april mai juni juli august september oktober november dezember'.split()
DOCKET = (
    r'(?:[IVX]+[a-z]?\s+(?:Z[RBS]|ARZ|[RBSK])|\d+\s+(?:AZ[RBN]|ABR|AS|St[RB]|Bv[RLEQBF]|ARs)|'
    r'B\s+\d+\s+[A-Z]{1,4})\s+\d+\s*/\s*\d{2}(?:\s+R\b)?'
    r'|\d+\s+(?:A|B|C|CN|F|V|VR|WB|WD|WDS-VR)\s+\d+\.\d{2}\b|[CT][–-]\s*\d+/\d{2}\b'
)
DATED = re.compile(
    rf'(?<![\w/])(?P<court>{COURT_NAMES})(?![\w/])'
    rf'(?P<prefix>(?:(?!\b(?:{COURT_NAMES})\b)[^\n|;:]){{0,66}}?)'
    rf'(?P<day>\d{{1,2}})\.\s*(?P<month>\d{{1,2}}\s*\.|{"|".join(MONTHS)})\s*(?P<year>19\d{{2}}|20\d{{2}})'
    rf'[\s,*–—\-:()]{{0,12}}(?:Az\.?\s*)?[`* ]{{0,4}}(?P<docket>{DOCKET})',
    re.IGNORECASE,
)
KIND = re.compile(r'\b(?:Urteil|Versäumnisurteil|Teilurteil|Beschluss|Urt\.|Beschl\.|Schlussanträge)(?!\w)', re.I)
SPARQL_ENDPOINT = 'https://publications.europa.eu/webapi/rdf/sparql'


def docket_key(value):
    return re.sub(r'\s+', '', value.lower()).replace('–', '-')


def references(lines):
    for lineno, line in enumerate(lines, 1):
        for match in DATED.finditer(line):
            prefix = match['prefix']
            if not KIND.search(prefix) and not re.fullmatch(r'[,\s*]*', prefix):
                continue
            month = match['month'].lower()
            month_number = int(month.strip(' .')) if month[0].isdigit() else MONTHS.index(month) + 1
            try:
                decision_date = date(int(match['year']), month_number, int(match['day']))
            except ValueError:
                continue
            key = (COURTS[match['court'].lower()], docket_key(match['docket']), decision_date.isoformat())
            yield key, lineno, match.group(0)


def federal_index(path):
    index = defaultdict(lambda: defaultdict(set))
    for _, item in ET.iterparse(path, events=('end',)):
        if item.tag != 'item':
            continue
        court = (item.findtext('gericht') or '').split()
        day = item.findtext('entsch-datum') or ''
        link = item.findtext('link') or ''
        if court and len(day) == 8 and link:
            decision_date = f'{day[:4]}-{day[4:6]}-{day[6:]}'
            for match in re.finditer(DOCKET, item.findtext('aktenzeichen') or '', re.I):
                index[court[0], docket_key(match[0])][decision_date].add(link.replace('http://', 'https://', 1))
        item.clear()
    return index


def eu_query(codes):
    values = ' '.join(f'<http://publications.europa.eu/resource/celex/{code}>' for code in codes)
    query = f"""
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT DISTINCT ?uri ?day WHERE {{
    VALUES ?uri {{ {values} }}
    ?work owl:sameAs ?uri ;
          cdm:work_date_document ?day .
}}
"""
    url = SPARQL_ENDPOINT + '?' + urlencode({'query': query, 'format': 'application/sparql-results+json'})
    with urlopen(url, timeout=45) as response:
        return json.load(response)['results']['bindings']


def include_eu(index, citations):
    lookups = {}
    for court, docket, _ in citations:
        if court not in EU:
            continue
        match = re.fullmatch(r'([ct])-(\d+)/(\d{2})', docket)
        if not match:
            continue
        prefix, number, year = match.groups()
        year = int(year) + (2000 if int(year) < 80 else 1900)
        for kind in ('J', 'O', 'C'):
            lookups[f'6{year}{prefix.upper()}{kind}{int(number):04}'] = (court, docket)
    codes = sorted(lookups)
    batches = [codes[i:i + 35] for i in range(0, len(codes), 35)]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for rows in pool.map(eu_query, batches):
            for row in rows:
                celex = row['uri']['value'].rsplit('/', 1)[-1]
                index[lookups[celex]][row['day']['value'][:10]].add(
                    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:' + celex
                )


def workshop_inventory():
    """Findet versionierte Promptquellen auch in verschachtelten Plugins."""
    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    active = {Path(entry['source']): entry['name'] for entry in market['plugins']}
    excluded = {'testakte', 'testakten', 'templates', 'beispiele', 'eval-fixtures'}
    tracked = subprocess.check_output(['git', 'ls-files', '-z', '--', '*.md'], cwd=ROOT)
    result = []
    for item in tracked.decode('utf-8').split('\0'):
        path = Path(item)
        if (path.name != 'werkstatt.md' and not path.name.endswith('-werkstatt.md')
                and not (path.parent.name == 'werkstattprompts' and path.name != 'README.md')):
            continue
        owner = next((parent for parent in path.parents if parent in active), None)
        if owner is None or excluded.intersection(path.relative_to(owner).parts[:-1]):
            continue
        data = (ROOT / path).read_bytes()
        result.append({'path': item, 'plugin': active[owner], 'sha256': hashlib.sha256(data).hexdigest()})
    return len(active), result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--inventory', type=Path, help='Bestandsinventar mit --include-files')
    mode.add_argument('--workshops', action='store_true', help='Nur eigenständige Werkstatt-Prompts aktiver Plugins')
    parser.add_argument('--cutoff', type=date.fromisoformat, help='Entscheidungsstichtag (JJJJ-MM-TT)')
    parser.add_argument('--federal-index', type=Path, required=True, help='Amtliche rii-toc.xml')
    parser.add_argument('--eu', action='store_true', help='Zusätzlich das EU-Publikationsamt online abfragen')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    citations = defaultdict(set)
    if args.workshops:
        plugin_count, files = workshop_inventory()
    else:
        inventory = json.loads(args.inventory.read_text(encoding='utf-8'))
        plugin_count = inventory['plugin_count']
        files = [record for plugin in inventory['plugins'] for record in plugin['files']]
        for plugin in inventory['plugins']:
            profile = f'quality/evals/{plugin["plugin"]}.json'
            for number, anchor in enumerate(plugin['profile_anchors'], 1):
                for key, _, raw in references([anchor.get('citation', '')]):
                    citations[key].add((profile, number, raw))
    for record in files:
        path = record['path']
        found = list(references((ROOT / path).read_text(encoding='utf-8').splitlines()))
        if args.workshops:
            record['dated_citation_occurrences'] = len(found)
        for key, lineno, raw in found:
            citations[key].add((path, lineno, raw))

    index = federal_index(args.federal_index)
    if args.eu:
        include_eu(index, citations)
    totals = {'Bund': Counter(), 'EU': Counter()}
    candidates = []
    after_cutoff = []
    for (court, docket, decision_date), contexts in sorted(citations.items()):
        entries = index.get((court, docket), {})
        scope = 'EU' if court in EU else 'Bund'
        if scope == 'EU' and not args.eu:
            status = 'not_checked'
        elif decision_date in entries:
            status = 'matched'
        else:
            status = 'different_dates' if entries else 'not_indexed'
        totals[scope][status] += 1
        if args.cutoff and date.fromisoformat(decision_date) > args.cutoff:
            after_cutoff.append(dict(court=court, docket=docket, date=decision_date, contexts=sorted(contexts)))
        if status in ('different_dates', 'not_indexed'):
            candidates.append(dict(
                court=court, docket=docket, date=decision_date, status=status,
                entries={day: sorted(urls) for day, urls in sorted(entries.items())},
                contexts=sorted(contexts),
            ))
    report = dict(
        method='Heuristischer Metadatenabgleich. Kein Nachweis des Inhalts, der Vollständigkeit oder der Übertragbarkeit.',
        plugins=plugin_count, files=len(files) if args.workshops else inventory['file_count'],
        distinct=dict(totals), occurrences=sum(map(len, citations.values())), candidates=candidates,
    )
    if args.cutoff:
        report.update(cutoff=args.cutoff.isoformat(), after_cutoff=after_cutoff)
    if args.workshops:
        report.update(workshops=files, federal_index_sha256=hashlib.sha256(args.federal_index.read_bytes()).hexdigest())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ('method', 'candidates', 'workshops', 'after_cutoff')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
