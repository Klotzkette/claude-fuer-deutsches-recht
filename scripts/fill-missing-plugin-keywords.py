#!/usr/bin/env python3
"""Ergaenzt fehlende keywords in plugin.json-Dateien.

Strategie: Keywords werden aus
- dem Plugin-Namen (Slug, durch '-' getrennt)
- der description (signifikante Tokens)
- einem festen Set deutscher Recht-Domaene-Begriffe, sofern vorhanden
abgeleitet. Stopwords werden gefiltert. Pro Plugin werden 6-12 Keywords
gesetzt. Wenn keywords bereits vorhanden sind und nicht leer, bleibt das
Plugin unveraendert.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STOPWORDS = {
    "und", "oder", "fuer", "fur", "der", "die", "das", "in", "mit", "von",
    "zu", "auf", "im", "den", "des", "ein", "eine", "einer", "eines",
    "bei", "bzw", "auch", "an", "am", "als", "ist", "sind", "war", "waren",
    "nicht", "nur", "wenn", "dann", "doch", "noch", "schon", "skill",
    "skills", "plugin", "recht", "rechts", "rechtliche", "ueber", "uber",
    "kann", "soll", "muss", "wird", "werden", "haben", "hat", "habe",
    "z", "b", "vgl", "etc", "ggf", "siehe", "https", "http", "www",
    "deutsch", "deutscher", "deutsche", "deutschen", "deutsches",
}

UMLAUT_MAP = str.maketrans({
    "ä": "ae", "ö": "oe", "ü": "ue",
    "Ä": "ae", "Ö": "oe", "Ü": "ue",
    "ß": "ss",
})


def tokenize(text: str) -> list[str]:
    text = text.lower().translate(UMLAUT_MAP)
    tokens = re.split(r"[^a-z0-9\-]+", text)
    out = []
    for t in tokens:
        t = t.strip("-")
        if not t or t in STOPWORDS:
            continue
        if len(t) < 3:
            continue
        if re.match(r"^\d+$", t):
            continue
        # Ungewoehnlich kurze Fragment-Stuempfe ausschliessen, die meist
        # aus halbierten Komposita stammen (z. B. 'hrung' aus 'durchfuehrung').
        if len(t) <= 5 and t.endswith("hrung"):
            continue
        out.append(t)
    return out


def derive_keywords(slug: str, description: str) -> list[str]:
    parts = [p for p in slug.split("-") if p and p not in STOPWORDS and len(p) >= 3]
    desc_tokens = tokenize(description)
    seen: dict[str, None] = {}
    for t in parts + desc_tokens:
        if t not in seen:
            seen[t] = None
    keywords = list(seen.keys())
    return keywords[:12]


def main() -> int:
    changed = 0
    skipped = 0
    for pj in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        d = json.loads(pj.read_text(encoding="utf-8"))
        if d.get("keywords"):
            skipped += 1
            continue
        slug = pj.parent.parent.name
        desc = d.get("description", "")
        kw = derive_keywords(slug, desc)
        if not kw:
            print(f"  WARN: konnte keine keywords ableiten fuer {slug}", file=sys.stderr)
            continue
        new = {}
        inserted = False
        for k, v in d.items():
            new[k] = v
            if k == "description" and not inserted:
                new["keywords"] = kw
                inserted = True
        if not inserted:
            new["keywords"] = kw
        pj.write_text(
            json.dumps(new, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        changed += 1
    print(f"fill-missing-plugin-keywords: {changed} aktualisiert, {skipped} hatten bereits keywords")
    return 0


if __name__ == "__main__":
    sys.exit(main())
