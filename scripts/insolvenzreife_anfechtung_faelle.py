"""Originalunterlagen zu drei konkret abgegrenzten Zahlungskomplexen.

Die Funktion ergänzt den vorhandenen Aktenbestand und verändert weder die
Bankbuchungen noch die historischen Statusdaten. Beträge sind integer EUR-Cent.
Die CSV-Dateien sind rohe ERP-/Belegablageauszüge, keine Berechnungsvorlage.
"""
from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
import json
from pathlib import Path
import re
import unicodedata

from docx import Document
from docx.shared import Cm
from insolvenzreife_grundakten import BUSINESS, office_document


DATA = Path(__file__).resolve().parent / "data/insolvenzreife-anfechtungskomplexe.json"
FOLDER = "09_Zahlungskomplex"


def load_complexes():
    return json.loads(DATA.read_text(encoding="utf-8"))["cases"]


def _domain(name):
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", plain).strip("-")[:55] + ".example"


def _email(path, item, folder):
    message = EmailMessage(policy=policy.SMTP)
    message["From"] = f"{item['issuer']} <post@{_domain(item['issuer'])}>"
    message["To"] = f"{item['recipient']} <post@{_domain(item['recipient'])}>"
    message["Date"] = format_datetime(datetime.fromisoformat(item["date"] + "T10:14:00").replace(tzinfo=timezone.utc))
    message["Message-ID"] = f"<{item['id'].lower()}@{_domain(item['issuer'])}>"
    message["Subject"] = item["subject"]
    message["Content-Language"] = "de-DE"
    message.set_content("\n\n".join(item["body"] + [item["signature"]]), charset="utf-8")
    for filename in item.get("attachments", []):
        source = folder / filename
        if source.parent != folder or not source.is_file():
            raise ValueError(f"Fehlende oder unzulässige Mailanlage: {filename}")
        mime = {".pdf": ("application", "pdf"), ".docx": ("application", "vnd.openxmlformats-officedocument.wordprocessingml.document")}[source.suffix]
        message.add_attachment(source.read_bytes(), maintype=mime[0], subtype=mime[1], filename=filename)
    path.write_bytes(message.as_bytes())


def _validate(case, item):
    transactions = {row["id"]: row for row in case["transactions"]}
    for reference in item["payment_refs"]:
        if reference not in transactions:
            raise ValueError(f"Unbelegte Zahlung: {reference}")
    if case["prefix"] == "CB":
        payment = transactions["CB-CAPEX-01-BK"]
        if payment["date"] != item["event_date"] or -payment["amount_cents"] != item["amount_cents"]:
            raise ValueError("Cottbuser Schlusszahlung weicht von Bankquelle ab")
        if sum(x["amount_cents"] for x in item["components"]) != item["amount_cents"]:
            raise ValueError("Kapital, Material und Zins stimmen nicht mit Bankbetrag überein")
        loan = item["loan"]
        calculated = Decimal(loan["principal_cents"]) * Decimal(loan["annual_rate_percent"]) / 100 * loan["interest_days_30_360"] / 360
        if calculated != loan["interest_cents"]:
            raise ValueError("Darlehenszins ist rechnerisch nicht belegt")
    elif case["prefix"] == "BZ":
        offset = item["setoff"]
        debts = {r["id"]: r for r in case["obligations"]}
        claims = {r["id"]: r for r in case["receivables"]}
        if claims[offset["claim_id"]]["amount_cents"] != offset["claim_cents"] or debts[offset["counterclaim_id"]]["amount_cents"] != offset["counterclaim_cents"]:
            raise ValueError("Verrechnungsbeträge weichen von Nebenbuch ab")
        if item["payment_refs"] or offset["bank_amount_cents"] != 0:
            raise ValueError("Die Verrechnung darf keinen erfundenen Bankfluss erhalten")
        if offset["claim_debtor"] == offset["counterclaim_creditor"]:
            raise ValueError("Verschiedene Rechtsträger des Verrechnungsfalls verloren")
    else:
        main = transactions["PR-FUEL-01-BK"]
        if main["date"] != item["event_date"] or -main["amount_cents"] != item["amount_cents"]:
            raise ValueError("Treibstoffzahlung weicht von Bankbeleg ab")
    comparison = item.get("comparison_payment")
    if comparison and (abs(transactions[comparison["id"]]["amount_cents"]) != comparison["amount_cents"] or transactions[comparison["id"]]["date"] != comparison["event_date"]):
        raise ValueError("Abgrenzungszahlung weicht von Bankbeleg ab")


def build_avoidance_material(case, directory, letter_pdf, csv_file):
    """Liefert nur Grundaktenquellen; keine Lösung oder fertige Anspruchsschrift."""
    config = load_complexes()[case["prefix"]]
    _validate(case, config)
    folder = directory / FOLDER
    folder.mkdir(parents=True, exist_ok=True)
    sources = []
    for item in config["documents"]:
        if item["kind"] == "eml":
            continue
        target = folder / f"{item['id']}.{item['kind']}"
        if item["kind"] == "pdf":
            letter_pdf(target, case, {**item, "type": "accounting", "color": "#" + BUSINESS[case["prefix"]]["color"],
                                     "letterhead_line": "Geschäftsunterlagen und Zahlungsabwicklung"})
        elif item["kind"] == "docx":
            office_document(target, case, item)
            document = Document(target)
            for section in document.sections:
                section.page_width, section.page_height = Cm(21), Cm(29.7)
            document.save(target)
        else:
            raise ValueError(f"Nicht unterstütztes Originalformat {item['kind']}")
        sources.append(target)
    for item in config["documents"]:
        if item["kind"] == "eml":
            target = folder / f"{item['id']}.eml"
            _email(target, item, folder)
            sources.append(target)
    prefix = case["prefix"]
    # Unveränderter Auszug aus dem Bankjournal. Bei BZ nur getrennte Hauptauftragszahlung.
    refs = set(config["payment_refs"])
    if config.get("comparison_payment"):
        refs.add(config["comparison_payment"]["id"])
    bank_rows = [{**row, "Zuordnung": "Abgrenzungszahlung; kein Eingang auf BZ-DEB-06" if prefix == "BZ" else
                  "Gesonderter Vorkasseabruf TK-26" if row["id"] == "PR-FUEL-02-BK" else config["title"]}
                 for row in case["transactions"] if row["id"] in refs]
    target = folder / f"{prefix}-ZK-11_Bankzuordnung.csv"
    csv_file(target, ("date", "value_on", "id", "counterparty", "description", "amount_cents", "balance_cents", "ledger_account", "Zuordnung"), bank_rows)
    sources.append(target)
    # Belegregister bewahrt Erklärungs-/Ausführungsdaten und Originalformate, ohne Anspruchssumme.
    registry = [{"Beleg": item["id"], "Datum": item["date"], "Aussteller": item["issuer"],
                 "Empfaenger": item["recipient"], "Betreff": item["subject"],
                 "Datei": f"{item['id']}.{item['kind']}", "Anlagen": " | ".join(item.get("attachments", []))}
                for item in config["documents"]]
    target = folder / f"{prefix}-ZK-12_Belegregister.csv"
    csv_file(target, tuple(registry[0]), registry)
    sources.append(target)
    return sources
