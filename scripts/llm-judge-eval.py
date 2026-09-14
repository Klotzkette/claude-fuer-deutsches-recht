#!/usr/bin/env python3
"""llm-judge-eval.py - LLM-Judge fuer Skill-Output-Bewertung.

Skelett-Implementierung. Erwartet eine ANTHROPIC_API_KEY-Umgebungsvariable.
Faellt ohne API-Key auf einen 'dry-run' zurueck und gibt fertige Prompts aus,
die manuell oder ueber einen anderen Kanal an ein Modell uebergeben werden
koennen.

Verwendung:
    python3 scripts/llm-judge-eval.py <skill-output.md> <rubric-criterion.md>
    python3 scripts/llm-judge-eval.py --batch eval-out/ runs/judge-out.json

Rubric-Criterion-Datei enthaelt freie-Form Pruefkriterien wie:
    "Output enthaelt eine $-4-KSchG-Frist-Erwaehnung."
    "Output zitiert kein BeckRS oder juris ohne Live-Verifikation."
    "Output ist auf Deutsch."
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

JUDGE_SYSTEM_PROMPT = """Du bist ein Pruefer fuer anwaltliche Arbeitsergebnisse.
Deine Aufgabe: Bewerte den vorgelegten Skill-Output gegen das benannte Pass/Fail-Kriterium.
Antworte ausschliesslich in JSON wie folgt:
{
  "passed": true|false,
  "reason": "knapper Satz mit Begruendung",
  "evidence": "Zitat oder Stelle im Output, die die Bewertung stuetzt"
}
Wenn ein Kriterium eine Live-Verifikation verlangt, bewerte rein das im
Output gegebene Material. Pruefe NICHT externe URLs.
"""


def build_prompt(skill_output: str, criterion: str) -> str:
    return f"""Pass/Fail-Kriterium:
{criterion}

Skill-Output (zu pruefen):
---
{skill_output}
---

Bewerte das Pass/Fail-Kriterium und antworte in JSON wie im System-Prompt beschrieben."""


def call_anthropic(prompt: str) -> dict | None:
    """Optionaler Aufruf der Anthropic-API.
    Faellt auf None zurueck, wenn anthropic-SDK oder API-Key fehlen.
    """
    try:
        from anthropic import Anthropic  # type: ignore
    except ImportError:
        return None
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    client = Anthropic(api_key=api_key, timeout=45, max_retries=2)
    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",  # schneller, gut genug fuer Pass/Fail
        max_tokens=512,
        system=JUDGE_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    if msg.stop_reason != "end_turn":
        return {"passed": None, "reason": "Prüferausgabe unvollständig", "evidence": "Keine abgeschlossene Bewertung"}
    text = "".join(block.text for block in msg.content if block.type == "text")
    try:
        # Faengt Antworten ab, die in ```json gewrapped sind
        text = text.strip()
        if text.startswith("```json\n") and text.endswith("```"):
            text = text[8:-3].strip()
        elif text.startswith("```\n") and text.endswith("```"):
            text = text[4:-3].strip()
        result = json.loads(text)
        if not isinstance(result, dict) or type(result.get("passed")) is not bool:
            raise ValueError("passed muss ein boolescher Wert sein")
        if not all(isinstance(result.get(k), str) and result[k].strip() for k in ("reason", "evidence")):
            raise ValueError("Begründung und Beleg fehlen")
        return result
    except Exception as e:
        return {"passed": None, "reason": f"unparseable JSON: {e}", "evidence": text[:300]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skill_output", help="Datei mit dem Skill-Output")
    ap.add_argument("criterion", help="Datei mit dem Pass/Fail-Kriterium (eine Zeile oder Markdown)")
    ap.add_argument("--out", help="Schreibt JSON-Bewertung in Datei")
    ap.add_argument("--allow-remote", action="store_true", help="Externe Übermittlung ausdrücklich freigeben")
    args = ap.parse_args()

    skill_text = Path(args.skill_output).read_text(encoding="utf-8")
    criterion_text = Path(args.criterion).read_text(encoding="utf-8")

    prompt = build_prompt(skill_text, criterion_text.strip())
    print("--- Judge-Prompt ---")
    print(prompt[:600] + "..." if len(prompt) > 600 else prompt)
    print("--- /Prompt ---\n")

    if not args.allow_remote:
        print("Nicht bewertet: --allow-remote fehlt. Für zwei Prüfer quality-lab.py verwenden.")
        return 2
    result = call_anthropic(prompt)
    if result is None:
        print("[dry-run] Kein ANTHROPIC_API_KEY und/oder anthropic-SDK nicht installiert.")
        print("        Prompt oben kann manuell an ein Modell uebergeben werden.")
        return 2

    print("--- Judge-Ergebnis ---")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nErgebnis geschrieben: {args.out}")
    if result.get("passed") is None:
        return 2
    return 0 if result.get("passed") else 1


if __name__ == "__main__":
    sys.exit(main())
