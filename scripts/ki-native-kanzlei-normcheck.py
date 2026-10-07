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


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read(), r.headers.get_content_charset()
        except Exception as exc:  # noqa: BLE001 - Protokoll statt Abbruch
            err = exc
            time.sleep(2 * (attempt + 1))
    return None, str(err).encode(), None


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


def main():
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    parts = [f'# Normcheck KI-native Kanzlei\n\nAbruf: {datetime.now(timezone.utc).isoformat(timespec="seconds")}\n']
    failures = 0
    for e in cfg['entries']:
        status, raw, cs = fetch(e['url'])
        digest = hashlib.sha256(raw).hexdigest()[:16]
        head = f'\n## {e["id"]}\n\nURL: {e["url"]}\nStatus: {status} sha256:{digest}\n'
        if status != 200:
            failures += 1
            parts.append(head + 'FEHLER: ' + raw.decode(errors='replace')[:300] + '\n')
            continue
        if e['url'].endswith('.pdf'):
            text = pdf_text(raw)
            body = sections(text, e.get('sections', []), '§')
        else:
            text = html_text(raw, cs)
            if e.get('articles'):
                body = sections(text, e['articles'], 'Artikel')
            elif e.get('needles'):
                body = needle_view(text, e['needles'])
            else:
                body = text[:9000]
        parts.append(head + '\n```text\n' + body + '\n```\n')
    report = ''.join(parts)
    print(report)
    if out:
        out.write_text(report, encoding='utf-8')
    print(f'\nAbgerufen: {len(cfg["entries"]) - failures}, Fehler: {failures}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
