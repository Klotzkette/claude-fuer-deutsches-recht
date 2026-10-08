#!/usr/bin/env python3
"""llm-judge-eval.py — LLM-Judge für Stiltreue-Prüfung von Vorlagen.

Erwartet ANTHROPIC_API_KEY. Ohne Key Dry-Run: gibt den fertigen Prompt aus,
der manuell an ein Modell übergeben werden kann.

Verwendung:
    python3 scripts/llm-judge-eval.py <vorlage.md> <stilkriterium.md>
    python3 scripts/llm-judge-eval.py <vorlage.md> <stilkriterium.md> --out judge.json

Stilkriterium-Datei: freie Form, ein Pass/Fail-Kriterium pro Datei.
Beispiele:
    "Prüfe, ob die Vorlage durchgehend klassisches Latein verwendet."
    "Prüfe, ob die Sie-Form konsequent eingehalten wird."
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

JUDGE_SYSTEM_PROMPT = """Du bist ein Prüfer für anwaltliche Arbeitsergebnisse.
Deine Aufgabe: Bewerte den vorgelegten Vorlagentext gegen das benannte Pass/Fail-Kriterium.
Antworte ausschließlich in JSON wie folgt:
{
  "passed": true|false,
  "reason": "knapper Satz mit Begründung",
  "evidence": "Zitat oder Stelle im Text, die die Bewertung stützt"
}
Wenn ein Kriterium eine Live-Verifikation verlangt (z. B. Az.-Check), bewerte
ausschließlich das im Text gegebene Material. Prüfe keine externen URLs.
"""


def build_prompt(vorlage_text: str, criterion: str) -> str:
    return f"""Pass/Fail-Kriterium:
{criterion}

Vorlagentext (zu prüfen):
---
{vorlage_text}
---

Bewerte das Pass/Fail-Kriterium und antworte in JSON wie im System-Prompt beschrieben."""


def call_anthropic(prompt: str) -> dict | None:
    try:
        from anthropic import Anthropic  # type: ignore
    except ImportError:
        return None
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    client = Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=JUDGE_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    text = msg.content[0].text  # type: ignore
    text = text.strip().lstrip("```json").lstrip("```").rstrip("```")
    try:
        return json.loads(text)
    except Exception as e:
        return {"passed": None, "reason": f"unparseable JSON: {e}", "evidence": text[:300]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("vorlage", help="Datei mit dem Vorlagentext (z. B. grundschuldbestellung-notariell.md)")
    ap.add_argument("criterion", help="Datei mit dem Pass/Fail-Kriterium")
    ap.add_argument("--out", help="Schreibt JSON-Bewertung in Datei")
    args = ap.parse_args()

    vorlage_text = Path(args.vorlage).read_text(encoding="utf-8")
    criterion_text = Path(args.criterion).read_text(encoding="utf-8")

    prompt = build_prompt(vorlage_text, criterion_text.strip())
    print("--- Judge-Prompt ---")
    print(prompt[:600] + "..." if len(prompt) > 600 else prompt)
    print("--- /Prompt ---\n")

    result = call_anthropic(prompt)
    if result is None:
        print("[dry-run] Kein ANTHROPIC_API_KEY und/oder anthropic-SDK nicht installiert.")
        print("        Der Prompt oben kann manuell an ein Modell übergeben werden.")
        return 0

    print("--- Judge-Ergebnis ---")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nErgebnis geschrieben: {args.out}")
    return 0 if result.get("passed") else 1


if __name__ == "__main__":
    sys.exit(main())
