#!/usr/bin/env python3
"""Ruft die amtlichen Normtexte der KI-nativen Kanzlei ab und gibt den gelesenen Wortlaut aus.

Läuft in GitHub Actions, weil dort die amtlichen Seiten erreichbar sind. Ausgabe: Markdown mit
Abrufstatus, Abrufzeit, SHA-256 der Rohdaten und Wortlaut (vollständig oder nach Suchbegriffen
gefiltert). Kein Urteil über die Richtigkeit der Skills; das bleibt der redaktionellen Prüfung.
"""
import hashlib, html, json, re, sys, time, urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = 'Mozilla/5.0 (normcheck ki-native-kanzlei; +https://github.com/Klotzkette/claude-fuer-deutsches-recht)'


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'de'})
    err = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(), r.headers.get_content_charset()
        except Exception as exc:  # noqa: BLE001 - Protokoll statt Abbruch
            err = exc
            time.sleep(2)
    return None, str(err).encode(), None


def fallback_url(url):
    """dejure.org als gekennzeichnete Sekundärquelle, wenn die amtliche Seite nicht antwortet."""
    m = re.match(r'https://www\.gesetze-im-internet\.de/([^/]+)/__(\w+)\.html', url)
    if not m:
        return None
    abbr = {'ustg_1980': 'UStG', 'ao_1977': 'AO', 'gwg_2017': 'GwG', 'gkg_2004': 'GKG', 'dlinfov': 'DL-InfoV',
            'vwvfg': 'VwVfG', 'bverfgg': 'BVerfGG', 'egzpo': 'EGZPO'}.get(m.group(1), m.group(1).upper())
    return f'https://dejure.org/gesetze/{abbr}/{m.group(2)}.html'


def html_text(raw, charset):
    s = raw.decode(charset or 'iso-8859-1', errors='replace')
    m = re.search(r'<div class="jnhtml">(.*?)<div class="jnfussnote|<div class="jnhtml">(.*)', s, re.S)
    body = s
    if 'jnhtml' in s:
        start = s.find('<div class="jnheader">')
        body = s[start if start >= 0 else 0:]
        end = body.find('<div id="fusszeile"')
        body = body[:end if end > 0 else len(body)]
    body = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', body, flags=re.S)
    body = re.sub(r'<(br|/p|/div|/dd|/dt|/tr|/li)[^>]*>', '\n', body)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(body)
    lines = [re.sub(r'[ \t ]+', ' ', l).strip() for l in body.splitlines()]
    return '\n'.join(l for l in lines if l)


def pdf_text(raw):
    import io
    from pypdf import PdfReader
    return '\n'.join((page.extract_text() or '') for page in PdfReader(io.BytesIO(raw)).pages)


def sections(text, numbers, word):
    out = []
    for n in numbers:
        pat = re.compile(rf'(?m)^\s*{word}\s*{re.escape(n)}\b.*?(?=^\s*{word}\s*\d+[a-z]?\b(?!\s*Abs)|\Z)', re.S)
        hits = [m.group(0) for m in pat.finditer(text)]
        best = max(hits, key=len) if hits else f'[{word} {n} nicht gefunden]'
        out.append(best.strip()[:6000])
    return '\n\n'.join(out)


def needle_view(text, needles, limit=9000):
    paras = re.split(r'\n(?=\(\d+[a-z]?\)|\d+[a-z]?\.\s|Nr\.|\d{4}\s)', text)
    keep = [p for p in paras if any(re.search(n, p) for n in needles)]
    return ('\n'.join(keep) if keep else text)[:limit]


def check_entry(e):
    url = e['url']
    status, raw, cs = fetch(url)
    source = 'amtlich'
    if status != 200 and fallback_url(url):
        url = fallback_url(url)
        status, raw, cs = fetch(url)
        source = 'SEKUNDÄRQUELLE dejure.org'
    digest = hashlib.sha256(raw).hexdigest()[:16]
    head = f'\n## {e["id"]}\n\nURL: {url}\nQuelle: {source}\nStatus: {status} sha256:{digest}\n'
    if status != 200:
        return False, head + 'FEHLER: ' + raw.decode(errors='replace')[:300] + '\n'
    if url.endswith('.pdf'):
        body = sections(pdf_text(raw), e.get('sections', []), '§')
    else:
        text = html_text(raw, cs)
        if e.get('articles'):
            body = sections(text, e['articles'], 'Artikel')
        elif e.get('needles'):
            body = needle_view(text, e['needles'])
        else:
            body = text[:9000]
    return True, head + '\n```text\n' + body + '\n```\n'


def main():
    from concurrent.futures import ThreadPoolExecutor
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    entries = cfg['entries']
    import os
    only = Path(os.environ.get('NORMCHECK_ONLY_FILE', '-'))
    if only.is_file():
        wanted = {l.strip() for l in only.read_text(encoding='utf-8').splitlines() if l.strip()}
        entries = [e for e in entries if e['id'] in wanted]
    workers = int(os.environ.get('NORMCHECK_WORKERS', '8'))
    pause = float(os.environ.get('NORMCHECK_PAUSE', '0'))
    parts = [None] * len(entries)
    def slow(e):
        time.sleep(pause)
        return check_entry(e)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(slow, e): i for i, e in enumerate(entries)}
        for fut in futures:
            i = futures[fut]
            try:
                ok, part = fut.result(timeout=240)
            except Exception as exc:  # noqa: BLE001
                ok, part = False, f'\n## {entries[i]["id"]}\n\nFEHLER: {exc}\n'
            parts[i] = (ok, part)
            print(part, flush=True)
    failures = sum(1 for ok, _ in parts if not ok)
    report = f'# Normcheck KI-native Kanzlei\n\nAbruf: {datetime.now(timezone.utc).isoformat(timespec="seconds")}\n' + ''.join(p for _, p in parts)
    if out:
        out.write_text(report, encoding='utf-8')
    print(f'\nAbgerufen: {len(entries) - failures}, Fehler: {failures}', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
