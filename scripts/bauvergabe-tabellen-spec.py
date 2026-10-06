"""Generate the spreadsheet specification from the versioned case sources.

This command writes JSON only. It never builds or changes workbook artifacts.
"""
import argparse
import json
import re
from decimal import Decimal
from pathlib import Path

from bauvergabe_aktentexte import documents
from bauvergabe_falldaten import CASES, LV, total


# Presentation labels only; quantities, rates, totals and dates come from the sources.
CHANGE_LABELS = {
    "Klinik": [
        ("03.01", "Zusätzlicher Beton der Fundamentvertiefung", "m3"),
        ("03.02", "Zusätzlicher Betonstahl", "kg"),
        ("03.03", "Zusätzliche Schalung", "m2"),
    ],
    "Wohnhaus": [
        ("04.01", "Zusätzliches Mauerwerk der Brandwand", "m2"),
        ("03.01", "Zusätzlicher Beton", "m3"),
        ("03.02", "Zusätzlicher Betonstahl", "kg"),
    ],
}
UNITS = {"Kubikmeter": "m3", "Kilogramm": "kg", "Quadratmeter": "m2"}


def german_decimal(text):
    return Decimal(text.replace(".", "").replace(",", "."))


def json_number(number):
    return int(number) if number == number.to_integral_value() else float(number)


def case_spec(case):
    records = {item["file"]: item for item in documents(case)}
    offer = records["03-bieterarbeit/04_Angebotsschreiben.docx"]
    change = records["05-nachtragsmanagement/03_Nachtragsangebot.docx"]
    section = change["body"].split("## 2. Vergütungsansatz", 1)[1].split("## 3.", 1)[0]
    amounts = re.findall(
        r"([\d.]+)\s+(Kubikmeter|Kilogramm|Quadratmeter)\s+zu\s+([\d.,]+)\s+EUR",
        section,
    )
    labels = CHANGE_LABELS[case["short"]]
    if len(amounts) != len(labels):
        raise ValueError(f"{case['slug']}: expected three identifiable N01 cost positions")
    rows = []
    direct = Decimal(0)
    for (quantity, unit, rate), (oz, description, expected_unit) in zip(amounts, labels):
        if UNITS[unit] != expected_unit:
            raise ValueError(f"{case['slug']}: N01 position order or unit has changed")
        quantity, rate = german_decimal(quantity), german_decimal(rate)
        direct += quantity * rate
        rows.append(dict(oz=oz, description=description, unit=expected_unit,
                         quantity=json_number(quantity), rate=json_number(rate)))
    stated = re.search(r"insgesamt ([\d.,]+) EUR direkte Mehrkosten", section)
    if not stated or german_decimal(stated[1]) != direct:
        raise ValueError(f"{case['slug']}: N01 direct-cost total does not reconcile")
    if len(LV) != len(case["quantities"]) or len(LV) != len(case["prices"]):
        raise ValueError(f"{case['slug']}: LV quantities and prices have different lengths")
    short_title = (case["title"].split(" – ", 1)[0] if case["short"] == "Klinik"
                   else f"{case['title'].split(' – ', 1)[1]}, {case['city']}")
    return {
        "slug": case["slug"], "short": case["short"], "reference": case["reference"],
        "shortTitle": short_title, "winner": case["winner"], "lot": case["lot"],
        "offerDate": offer["date"],
        "offerRows": [dict(oz=oz, description=description, unit=unit, quantity=quantity, rate=rate)
                      for (oz, description, unit), quantity, rate
                      in zip(LV, case["quantities"], case["prices"])],
        "changeRows": rows, "expectedOfferNet": float(total(case)),
        "expectedChangeDirect": json_number(direct),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Destination JSON specification")
    parser.add_argument("--qa-dir", type=Path, required=True, help="QA directory used by the workbook builder")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    spec = {"repo": str(repo), "qaDir": str(args.qa_dir.expanduser().resolve()),
            "cases": [case_spec(case) for case in CASES]}
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
