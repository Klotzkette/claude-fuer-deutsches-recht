#!/usr/bin/env python3
"""Kleiner Vorcheck für Einfache Sprache und Leichte Sprache.

Das Skript ist kein DIN-Zertifikat und keine Normprüfung. Es findet
Warnsignale, die ein Mensch anschließend bewertet.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LEGAL_WORDS = [
    "frist",
    "widerspruch",
    "klage",
    "bescheid",
    "vertrag",
    "kündigung",
    "widerruf",
    "anfechtung",
    "haftung",
    "vollstreckung",
    "rechtsmittel",
    "gericht",
    "behörde",
]


def split_sentences(text: str) -> list[str]:
    rough = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    return [s.strip() for s in rough if s.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÄÖÜäöüß0-9][A-Za-zÄÖÜäöüß0-9-]*", text)


def passive_candidates(text: str) -> list[str]:
    pattern = re.compile(r"\b(?:wird|werden|wurde|wurden|worden)\b[^.!?]{0,80}\bge[A-Za-zÄÖÜäöüß-]+", re.I)
    return [m.group(0).strip() for m in pattern.finditer(text)]


def nominalizations(tokens: list[str]) -> list[str]:
    endings = ("ung", "heit", "keit", "tion", "tät", "nis")
    out = []
    for token in tokens:
        clean = token.strip("-").lower()
        if len(clean) > 8 and clean.endswith(endings):
            out.append(token)
    return out


def analyze(text: str, mode: str) -> dict[str, object]:
    sents = split_sentences(text)
    toks = words(text)
    sentence_lengths = [len(words(s)) for s in sents]
    long_sentence_limit = 20 if mode == "einfache" else 10
    long_word_limit = 18 if mode == "einfache" else 14
    long_sentences = [
        {"words": n, "sentence": s}
        for s, n in zip(sents, sentence_lengths)
        if n > long_sentence_limit
    ]
    long_words = sorted({w for w in toks if len(w) > long_word_limit})
    passives = passive_candidates(text)
    noms = sorted(set(nominalizations(toks)))
    headings = len(re.findall(r"^#{1,3}\s+", text, flags=re.M))
    lists = len(re.findall(r"^\s*(?:[-*]|\d+\.)\s+", text, flags=re.M))
    legal_hits = sorted({w for w in LEGAL_WORDS if re.search(rf"\b{re.escape(w)}\w*\b", text, flags=re.I)})

    warnings = []
    if long_sentences:
        warnings.append("lange Sätze")
    if len(long_words) > (10 if mode == "einfache" else 5):
        warnings.append("viele lange Wörter")
    if passives:
        warnings.append("Passiv-Kandidaten")
    if len(noms) > 8:
        warnings.append("Nominalstil-Kandidaten")
    if headings == 0:
        warnings.append("keine Markdown-Überschriften")
    if mode == "leichte" and lists == 0:
        warnings.append("keine sichtbaren Schrittlisten")
    if legal_hits and "schwere wörter" not in text.lower() and "glossar" not in text.lower():
        warnings.append("Rechtsbegriffe ohne sichtbares Glossar")

    return {
        "mode": mode,
        "characters": len(text),
        "sentences": len(sents),
        "words": len(toks),
        "average_sentence_words": round(sum(sentence_lengths) / len(sentence_lengths), 1) if sentence_lengths else 0,
        "long_sentence_limit": long_sentence_limit,
        "long_sentences": long_sentences[:10],
        "long_words_sample": long_words[:30],
        "passive_candidates": passives[:10],
        "nominalization_sample": noms[:30],
        "headings": headings,
        "lists": lists,
        "legal_terms_found": legal_hits,
        "warnings": warnings,
        "status": "needs_review" if warnings else "ok",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Vorcheck für Einfache Sprache und Leichte Sprache")
    parser.add_argument("file", type=Path)
    parser.add_argument("--mode", choices=["einfache", "leichte"], default="einfache")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    result = analyze(text, args.mode)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
