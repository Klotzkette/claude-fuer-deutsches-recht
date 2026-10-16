#!/usr/bin/env python3
"""Structured first-pass gate for online-banking phishing cases."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
import math
from pathlib import Path
from typing import Any


def money(value: Any) -> Decimal:
    try:
        amount = Decimal(str(value).replace(",", "."))
    except InvalidOperation as exc:
        raise ValueError("Betrag muss eine endliche nichtnegative Zahl sein.") from exc
    if not amount.is_finite() or amount < 0:
        raise ValueError("Betrag muss eine endliche nichtnegative Zahl sein.")
    return amount


def flag(data: dict[str, Any], name: str) -> bool:
    value = data.get("factors", {}).get(name, False)
    if not isinstance(value, bool):
        raise ValueError(f"Faktor {name} muss true oder false sein; Text ist kein Beleg.")
    return value


def score_case(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError("Eingabe muss ein JSON-Objekt sein.")
    authorization = data.get("authorization_status", "unknown")
    if authorization not in {"unknown", "disputed", "not_authorized", "authorized"}:
        raise ValueError("Unbekannter authorization_status.")
    factors = data.get("factors", {})
    if not isinstance(factors, dict) or any(not isinstance(value, bool) for value in factors.values()):
        raise ValueError("Faktoren müssen boolesche Angaben sein; keine Punktwertung.")
    transactions = data.get("transactions", [])
    if not isinstance(transactions, list) or any(not isinstance(tx, dict) for tx in transactions):
        raise ValueError("Transaktionen müssen als Liste von Objekten vorliegen.")
    stated_damage = money(data["damage_amount"]) if data.get("damage_amount") is not None else None
    known_amounts = [money(tx["amount"]) if tx.get("amount") is not None else None for tx in transactions]
    transaction_total = (sum(known_amounts, Decimal("0"))
                         if known_amounts and all(amount is not None for amount in known_amounts) else None)
    minutes = data.get("immediate_block_call_minutes")
    if minutes is not None and (isinstance(minutes, bool) or not isinstance(minutes, (int, float))
                                or not math.isfinite(minutes) or minutes < 0):
        raise ValueError("Zeitabstand muss eine endliche nichtnegative Minutenzahl oder null sein.")

    claimant_points: list[str] = []
    bank_points: list[str] = []
    missing: list[str] = []

    if stated_damage is None:
        missing.append("damage_amount")
    if transaction_total is None:
        missing.append("complete_transaction_amounts")
    if flag(data, "spoofed_bank_number"):
        claimant_points.append("Call-ID-Spoofing mit plausibler Banknummer")
    if flag(data, "app_text_ambiguous"):
        claimant_points.append("Freigabedialog war mehrdeutig oder als Sicherheitsvorgang gerahmt")
    if flag(data, "tan_entry_foreign_tor_ip"):
        claimant_points.append("TAN-Einsatz aus fremder oder riskanter IP-Umgebung")
    if flag(data, "account_holder_location_mismatch"):
        claimant_points.append("Ort/Gerät des Kontoinhabers passt nicht zum Transaktionsauslöser")
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

    # Die Eingaben sind Angaben des Nutzers, keine automatisch festgestellten Tatsachen.
    # C-70/25 verlangt zwei getrennte Prüfschritte; ein Indikatorenscore darf
    # weder Autorisierung beweisen noch die sofortige Erstattung zurückstellen.
    paths = {
        "unknown": "autorisierung_aufklaeren",
        "disputed": "autorisierung_aufklaeren",
        "not_authorized": "unverzuegliche_erstattung_pruefen",
        "authorized": "andere_anspruchsgrundlage_pruefen",
    }
    suspicion = data.get("payer_fraud_suspicion") or {}
    notification = data.get("authority_notification") or {}
    if not isinstance(suspicion, dict) or not isinstance(notification, dict):
        raise ValueError("Verdacht und Behördenmitteilung müssen getrennte Objekte sein.")
    supported_suspicion = bool(suspicion.get("reasons") and suspicion.get("evidence"))
    written_notification = (notification.get("written") is True and
                            all(notification.get(key) for key in ("authority", "date", "evidence")))
    exception_status = "nicht_belegt"
    if supported_suspicion and written_notification:
        exception_status = "begruendung_und_mitteilung_rechtlich_pruefen"
    elif suspicion or notification:
        exception_status = "begruendung_oder_mitteilung_unvollstaendig"
    recommendation = {
        "unknown": "Zustimmung zur konkreten Zahlung und Anzeigezeitpunkt gezielt klären; die Erstattungsprüfung nicht bis zum Abschluss der Verschuldensaufklärung zurückstellen.",
        "disputed": "Autorisierungsstreit nach § 675w BGB aufklären; technische Nutzung ist kein automatischer Zustimmungsnachweis. Unverzügliche Erstattung gesondert verlangen, soweit die Tatsachen sie tragen.",
        "not_authorized": "Unverzügliche Erstattung und Kontowiederherstellung nach § 675u BGB zuerst prüfen. Grobe Fahrlässigkeit allein rechtfertigt kein Zurückstellen; möglichen Rückgriff nach § 675v BGB gesondert bearbeiten.",
        "authorized": "Eine wirksam autorisierte Zahlung fällt nicht allein wegen Täuschung unter § 675u BGB. Rückholung, Täteransprüche und konkrete Bankpflichtverletzungen getrennt prüfen.",
    }[authorization]

    return {
        "case_name": data.get("case_name"),
        "damage_amount": str(stated_damage) if stated_damage is not None else None,
        "transaction_total": str(transaction_total) if transaction_total is not None else None,
        "damage_matches_transactions": stated_damage == transaction_total if stated_damage is not None and transaction_total is not None else None,
        "reported_block_call_minutes": minutes,
        "traffic_lights": {
            "erstattung_dem_grunde": "GELB",
            "grobe_fahrlaessigkeit_einwand": "GELB",
            "bankpflichten_monitoring": "GELB",
            "prozessfreigabe": "GELB",
        },
        "traffic_lights_note": "GELB bedeutet offene menschliche Prüfung, keine Erfolgsprognose und keine Freigabe. Die alten Schlüssel bleiben für vorhandene Eingaben lesbar.",
        "human_release_granted": False,
        "refund_review": {
            "authorization_status_as_reported": authorization,
            "path": paths[authorization],
            "fraud_exception_status": exception_status,
            "exception_limit": "Nur begründeten Verdacht eines Betrugs des Zahlers und die schriftliche Mitteilung an die zuständige Behörde prüfen. Ein Drittangriff oder grobe Fahrlässigkeit allein genügt nicht.",
            "deadline": "Kenntnis oder Anzeige, Zugang und Geschäftstag gesondert ermitteln; hier keine Kalenderberechnung.",
            "source": "EuGH, 15.10.2026, C-70/25, Rn. 31–42, 45–47, 52; §§ 675u, 675w, 676b BGB",
        },
        "recourse_review": {
            "separate_from_immediate_refund": True,
            "proof": "Konkrete Pflichtverletzung, qualifiziertes Verschulden und Verlustkausalität prüfen; Bankvortrag und Bankbeweis sind keine feststehenden Tatsachen.",
            "source": "§ 675v BGB; EuGH C-70/25, Rn. 40, 45–47",
        },
        "claimant_points": claimant_points,
        "bank_points": bank_points,
        "missing_evidence": missing,
        "recommended_next_steps": [
            "Transaktionsmatrix finalisieren und Doppelzählungen ausschließen",
            "App-Freigabetext und vollständige Banklogs anfordern",
            "Sperr-, Anzeige- und Strafanzeigenachweise beilegen",
            "Erstattung und späteren Rückgriff getrennt dokumentieren; Bankargumente zu § 675v BGB konkret prüfen",
            "Schlichtung oder Vergleich nur auf Auftrag; keine Quote oder menschliche Freigabe erfinden",
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
