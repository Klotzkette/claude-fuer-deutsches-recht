#!/usr/bin/env python3
"""Structured first-pass gate for online-banking phishing cases."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal
from pathlib import Path
from typing import Any


def money(value: Any) -> Decimal:
    return Decimal(str(value).replace(",", "."))


def flag(data: dict[str, Any], name: str) -> bool:
    return bool(data.get("factors", {}).get(name, False))


def score_case(data: dict[str, Any]) -> dict[str, Any]:
    transactions = data.get("transactions", [])
    stated_damage = money(data.get("damage_amount", "0"))
    transaction_total = sum((money(tx.get("amount", "0")) for tx in transactions), Decimal("0"))

    claimant_points: list[str] = []
    bank_points: list[str] = []
    missing: list[str] = []

    if flag(data, "spoofed_bank_number"):
        claimant_points.append("Call-ID-Spoofing mit plausibler Banknummer")
    if flag(data, "app_text_ambiguous"):
        claimant_points.append("Freigabedialog war mehrdeutig oder als Sicherheitsvorgang gerahmt")
    if flag(data, "tan_entry_foreign_tor_ip"):
        claimant_points.append("TAN-Einsatz aus fremder oder riskanter IP-Umgebung")
    if flag(data, "account_holder_location_mismatch"):
        claimant_points.append("Ort/Gerät des Kontoinhabers passt nicht zum Transaktionsauslöser")
    if int(data.get("immediate_block_call_minutes", 999)) <= 60:
        claimant_points.append("Sperre/Reklamation erfolgte zeitnah")
    if flag(data, "bank_rejected_ombudsman"):
        claimant_points.append("Ombudsmann-Vorschlag wurde bankseitig nicht umgesetzt")

    if flag(data, "tan_shared_by_phone"):
        bank_points.append("TAN oder Freigabe wurde telefonisch weitergegeben")
    if flag(data, "security_warnings_before"):
        bank_points.append("vorherige Sicherheitswarnungen können der Bank helfen")
    if flag(data, "strong_customer_authentication_logged"):
        bank_points.append("Bank behauptet protokollierte starke Kundenauthentifizierung")
    if flag(data, "app_text_clear_amount_recipient"):
        bank_points.append("Freigabedialog nannte nach Bankvortrag Betrag und Empfänger klar")

    for needed in [
        "exact_app_dialog",
        "full_authentication_logs",
        "risk_score_thresholds",
        "recipient_creation_log",
        "recall_attempts",
    ]:
        if not flag(data, needed):
            missing.append(needed)

    unauthorized = "GRUEN" if claimant_points else "GELB"
    gross_negligence = "GELB"
    if len(bank_points) >= 3 and not flag(data, "app_text_ambiguous"):
        gross_negligence = "ROT"
    if len(bank_points) <= 1 and len(claimant_points) >= 3:
        gross_negligence = "GRUEN"

    bank_duty = "GELB"
    if flag(data, "tan_entry_foreign_tor_ip") and flag(data, "account_holder_location_mismatch"):
        bank_duty = "GRUEN"
    if not (flag(data, "tan_entry_foreign_tor_ip") or flag(data, "account_holder_location_mismatch")):
        bank_duty = "GELB"

    process_gate = "GELB"
    if unauthorized == "GRUEN" and gross_negligence == "GRUEN":
        process_gate = "GRUEN"
    if gross_negligence == "ROT" and bank_duty != "GRUEN":
        process_gate = "ROT"

    recommendation = (
        "Klagefähig, aber nicht als Selbstläufer behandeln. Erst Banklogs und App-Dialog sichern; "
        "§ 675v-Einwand aktiv vorwegnehmen und hilfsweise Vergleichs-/Ombudsmannquote prüfen."
    )
    if process_gate == "GRUEN":
        recommendation = "Gute Anspruchslage. Bankaufforderung mit kurzer Frist und konkretem Logverlangen vorbereiten."
    elif process_gate == "ROT":
        recommendation = "Derzeit hohes Klagerisiko. Vor Klage weitere Belege, App-Dialog und Monitoringlogs beschaffen."

    return {
        "case_name": data.get("case_name"),
        "damage_amount": str(stated_damage),
        "transaction_total": str(transaction_total),
        "damage_matches_transactions": stated_damage == transaction_total,
        "traffic_lights": {
            "erstattung_dem_grunde": unauthorized,
            "grobe_fahrlaessigkeit_einwand": gross_negligence,
            "bankpflichten_monitoring": bank_duty,
            "prozessfreigabe": process_gate,
        },
        "claimant_points": claimant_points,
        "bank_points": bank_points,
        "missing_evidence": missing,
        "recommended_next_steps": [
            "Transaktionsmatrix finalisieren und Doppelzählungen ausschließen",
            "App-Freigabetext und vollständige Banklogs anfordern",
            "Sperr-, Anzeige- und Strafanzeigenachweise beilegen",
            "Bankargumente zu § 675v BGB tabellarisch vorwegnehmen",
            "Ombudsmann- oder Vergleichspfad nur mit dokumentierter Quote nutzen",
        ],
        "recommendation": recommendation,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to case JSON")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = score_case(data)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
