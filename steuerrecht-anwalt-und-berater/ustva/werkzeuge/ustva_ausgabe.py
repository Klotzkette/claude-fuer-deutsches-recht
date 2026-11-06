#!/usr/bin/env python3
"""Prüft einen fachlich geprüften UStVA-Arbeitsstand und erzeugt Erfassungsdateien.

Aufruf: ustva_ausgabe.py INPUT.json --out NEUES_VERZEICHNIS
Optional: --import-xml DATEI --xsd JAHRESSCHEMA
Der Helfer führt keine Anmeldung und keine Datenübermittlung aus.
Der Eingabevertrag steht in der benachbarten README.md.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote, urlparse


AMOUNT = re.compile(r"-?(?:0|[1-9]\d{0,14})(?:\.\d{1,2})?\Z")
FACTOR = re.compile(r"-?(?:0|[1-9]\d{0,4})(?:\.\d{1,6})?\Z")
FIELD = re.compile(r"\d{2,3}\Z")
PERIOD = re.compile(r"(?:Q[1-4]|M(?:0[1-9]|1[0-2]))\Z")
XML_PATH = re.compile(r"\./(?:u:[A-Za-z_][A-Za-z_0-9]*/)*u:[A-Za-z_][A-Za-z_0-9]*\Z")
UNITS = {"EUR": Decimal("1"), "EUR_CENT": Decimal("0.01"), "FLAG": Decimal("1")}
ROUNDINGS = {"HALF_UP": ROUND_HALF_UP, "DOWN": ROUND_DOWN}


def text(value, label):
    if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
        raise ValueError(f"{label}: einzeiliger Text fehlt oder enthält Steuerzeichen")
    return value


def amount(value, label, pattern=AMOUNT):
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise ValueError(f"{label}: Dezimalzahl als Zeichenfolge ohne Tausenderzeichen erforderlich")
    return Decimal(value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Doppeltes JSON-Feld: {key}")
        result[key] = value
    return result


def validate(data):
    allowed = {"schema_version", "year", "period", "taxpayer", "approval_status", "mapping",
               "fields", "arithmetic", "reconciliation"}
    if (not isinstance(data, dict) or set(data) != allowed
            or type(data["schema_version"]) is not int or data["schema_version"] != 1):
        raise ValueError("Eingabefelder oder schema_version stimmen nicht mit dem Eingabevertrag überein")
    year = data["year"]
    if type(year) is not int or year not in (2025, 2026):
        raise ValueError("Unterstützte Arbeitsjahre sind 2025 und 2026")
    if not isinstance(data["period"], str) or not PERIOD.fullmatch(data["period"]):
        raise ValueError("Voranmeldungszeitraum muss Q1 bis Q4 oder M01 bis M12 sein")
    if data["approval_status"] not in ("reviewed", "approved"):
        raise ValueError("Der Arbeitsstand muss fachlich geprüft sein")
    taxpayer = data["taxpayer"]
    if not isinstance(taxpayer, dict) or not {"name", "steuernummer"} <= set(taxpayer):
        raise ValueError("Unternehmername und betriebliche Steuernummer fehlen")
    if set(taxpayer) - {"name", "steuernummer", "ust_id", "w_id", "finanzamt", "address"}:
        raise ValueError("Nicht unterstütztes Stammdatenfeld")
    for key, value in taxpayer.items():
        text(value, f"taxpayer.{key}")

    mapping = data["mapping"]
    if not isinstance(mapping, dict) or mapping.get("year") != year:
        raise ValueError("Jahresversion der geprüften Kennzahlenzuordnung passt nicht")
    if set(mapping) - {"year", "source", "reviewed_on", "fields", "xml"}:
        raise ValueError("Nicht unterstütztes Feld der Kennzahlenzuordnung")
    text(mapping.get("source"), "mapping.source")
    date.fromisoformat(text(mapping.get("reviewed_on"), "mapping.reviewed_on"))
    definitions = mapping.get("fields")
    if not isinstance(definitions, dict) or not definitions:
        raise ValueError("Geprüfte Kennzahlendefinitionen fehlen")
    semantics = set()
    for number, definition in definitions.items():
        if not FIELD.fullmatch(number) or not isinstance(definition, dict):
            raise ValueError("Ungültige Kennzahlendefinition")
        if set(definition) != {"label", "unit", "semantic", "allow_negative"}:
            raise ValueError(f"Kennzahl {number}: Definition ist unvollständig")
        text(definition["label"], f"Kennzahl {number} Bezeichnung")
        semantic = text(definition["semantic"], f"Kennzahl {number} Bedeutung")
        if semantic in semantics:
            raise ValueError("Kennzahlbedeutung ist mehrfach vergeben")
        semantics.add(semantic)
        if definition["unit"] not in UNITS or type(definition["allow_negative"]) is not bool:
            raise ValueError(f"Kennzahl {number}: Einheit oder Vorzeichenregel ungültig")

    rows = data["fields"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("Kennzahlenwerte fehlen")
    values = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"kennzahl", "label", "amount", "unit", "source"}:
            raise ValueError("Kennzahlenzeile stimmt nicht mit dem Eingabevertrag überein")
        number = row["kennzahl"]
        if not isinstance(number, str) or number not in definitions or number in values:
            raise ValueError("Doppelte oder ungeprüfte Kennzahl")
        definition = definitions[number]
        if row["label"] != definition["label"] or row["unit"] != definition["unit"]:
            raise ValueError(f"Kennzahl {number}: Bedeutung oder Einheit weicht von der geprüften Zuordnung ab")
        value = amount(row["amount"], f"Kennzahl {number}")
        if value != value.quantize(UNITS[row["unit"]]):
            raise ValueError(f"Kennzahl {number}: zu viele Nachkommastellen für die Feldeinheit")
        if (row["unit"] == "FLAG" and value not in (0, 1)) or (value < 0 and not definition["allow_negative"]):
            raise ValueError(f"Kennzahl {number}: Wert widerspricht der Felddefinition")
        text(row["source"], f"Kennzahl {number} Belegfundstelle")
        values[number] = value

    checks = data["arithmetic"]
    if not isinstance(checks, list) or not checks:
        raise ValueError("Mindestens eine Rechenkontrolle ist erforderlich")
    results = set()
    check_ids = set()
    for check in checks:
        if not isinstance(check, dict) or set(check) != {"id", "result_field", "terms", "rounding"}:
            raise ValueError("Rechenkontrolle stimmt nicht mit dem Eingabevertrag überein")
        identifier = text(check["id"], "Kontrollbezeichnung")
        result = check["result_field"]
        if identifier in check_ids or result not in values or result in results:
            raise ValueError("Doppelte Rechenkontrolle oder unbekanntes Ergebnisfeld")
        check_ids.add(identifier)
        results.add(result)
        if check["rounding"] not in ROUNDINGS or not isinstance(check["terms"], list) or not check["terms"]:
            raise ValueError("Rechenkontrolle benötigt Terme und eine explizite Rundungsregel")
        total = Decimal(0)
        for term in check["terms"]:
            if not isinstance(term, dict) or set(term) != {"field", "factor"}:
                raise ValueError("Unvollständiger Rechenterm")
            field = term["field"]
            if field not in values or field == result:
                raise ValueError("Rechenkontrolle verwendet unbekanntes Feld oder prüft sich selbst")
            total += values[field] * amount(term["factor"], "Rechenfaktor", FACTOR)
        target_unit = UNITS[definitions[result]["unit"]]
        if total.quantize(target_unit, rounding=ROUNDINGS[check["rounding"]]) != values[result]:
            raise ValueError(f"Rechenkontrolle {identifier} stimmt nicht")
    if "83" not in values or "83" not in results:
        raise ValueError("Kennzahl 83 und ihre Rechenkontrolle fehlen")

    reconciliations = data["reconciliation"]
    if not isinstance(reconciliations, list) or not reconciliations:
        raise ValueError("Unabhängiger Betragsabgleich mit Belegfundstelle fehlt")
    for check in reconciliations:
        if not isinstance(check, dict) or set(check) != {"id", "actual", "expected", "source"}:
            raise ValueError("Betragsabgleich stimmt nicht mit dem Eingabevertrag überein")
        text(check["id"], "Abgleichbezeichnung")
        text(check["source"], "Abgleichfundstelle")
        if amount(check["actual"], "Istbetrag") != amount(check["expected"], "Sollbetrag"):
            raise ValueError(f"Betragsabgleich {check['id']} stimmt nicht")
    return values


def validate_xml(xml_path, schema_path, data, values, schema_directory=None):
    from lxml import etree

    schema_root = schema_directory.resolve() if schema_directory else schema_path.resolve().parent
    if not schema_path.resolve().is_relative_to(schema_root):
        raise ValueError("Jahresschema liegt außerhalb des lokalen Schemaverzeichnisses")

    class LocalSchemaResolver(etree.Resolver):
        def resolve(self, url, public_id, context):
            parsed = urlparse(url)
            if parsed.scheme not in ("", "file") or parsed.netloc:
                raise ValueError("Externe Schemaquelle ist gesperrt")
            path = Path(unquote(parsed.path))
            path = (schema_root / path).resolve() if not path.is_absolute() else path.resolve()
            if not path.is_relative_to(schema_root):
                raise ValueError("Schemaquelle liegt außerhalb des lokalen Schemaverzeichnisses")
            if b"<!DOCTYPE" in path.read_bytes().upper():
                raise ValueError("DOCTYPE in Schemadatei ist gesperrt")
            return self.resolve_filename(str(path), context)

    parser = etree.XMLParser(resolve_entities=False, load_dtd=False, no_network=True)
    parser.resolvers.add(LocalSchemaResolver())
    content = xml_path.read_bytes()
    if len(content) > 5_000_000 or b"<!DOCTYPE" in content.upper():
        raise ValueError("Import-XML ist zu groß oder enthält einen gesperrten DOCTYPE")
    schema = etree.XMLSchema(etree.parse(str(schema_path.resolve()), parser))
    document = etree.fromstring(content, parser)
    if document.getroottree().docinfo.encoding.upper() != "ISO-8859-15":
        raise ValueError("Der UStVA-Portalimport benötigt den Zeichensatz ISO-8859-15")
    schema.assertValid(document)
    contract = data["mapping"].get("xml")
    required = {"namespace", "version", "year_path", "period_path", "period", "period_value",
                "fields", "taxpayer", "metadata"}
    if not isinstance(contract, dict) or set(contract) != required:
        raise ValueError("Geprüfte Zuordnung zwischen Import-XML und Arbeitsstand fehlt")
    namespace = text(contract["namespace"], "XML-Namensraum")
    if not namespace.startswith("http://finkonsens.de/elster/elsteranmeldung/ustva/"):
        raise ValueError("XML-Namensraum ist keinem UStVA-Import zugeordnet")
    if document.tag != f"{{{namespace}}}Anmeldungssteuern" or document.get("version") != contract["version"]:
        raise ValueError("Importwurzel oder XML-Version stimmt nicht mit der geprüften Zuordnung überein")

    consumed = set()

    def value_at(path):
        if not isinstance(path, str) or not XML_PATH.fullmatch(path):
            raise ValueError("XML-Zuordnung muss einen einfachen lokalen Elementpfad enthalten")
        found = document.findall(path, {"u": namespace})
        if len(found) != 1 or found[0].text is None:
            raise ValueError("XML-Zuordnung ist nicht eindeutig oder ihr Wert fehlt")
        if found[0] in consumed:
            raise ValueError("Ein XML-Feld ist mehrfach einer Bedeutung zugeordnet")
        consumed.add(found[0])
        return found[0].text.strip()

    taxpayer_paths = contract["taxpayer"]
    if (not isinstance(taxpayer_paths, dict) or "steuernummer" not in taxpayer_paths
            or set(taxpayer_paths) - set(data["taxpayer"])):
        raise ValueError("XML-Zuordnung des Unternehmers einschließlich Steuernummer fehlt")
    for key, path in taxpayer_paths.items():
        actual = value_at(path)
        expected = data["taxpayer"][key]
        if key == "steuernummer":
            actual = re.sub(r"[\s/.-]", "", actual)
            expected = re.sub(r"[\s/.-]", "", expected)
            if not re.fullmatch(r"\d{13}", expected) or not re.fullmatch(r"\d{13}", actual):
                raise ValueError("Für den XML-Abgleich ist die geprüfte 13-stellige ELSTER-Steuernummer erforderlich")
        else:
            actual = " ".join(actual.split())
            expected = " ".join(expected.split())
        if actual != expected:
            raise ValueError(f"Unternehmerangabe {key} in Import-XML weicht ab")
    if value_at(contract["year_path"]) != str(data["year"]):
        raise ValueError("Jahr in Import-XML und Arbeitsstand weicht ab")
    if contract["period"] != data["period"]:
        raise ValueError("Die XML-Zeitraumzuordnung gehört zu einem anderen Arbeitszeitraum")
    if value_at(contract["period_path"]) != text(contract["period_value"], "XML-Zeitraumwert"):
        raise ValueError("Voranmeldungszeitraum in Import-XML weicht ab")
    if not isinstance(contract["fields"], dict) or set(contract["fields"]) != set(values):
        raise ValueError("Import-XML muss genau den fachlich geprüften Kennzahlen zugeordnet sein")
    for number, expected in values.items():
        if amount(value_at(contract["fields"][number]), f"XML-Kennzahl {number}") != expected:
            raise ValueError(f"Kennzahl {number} in Import-XML weicht vom geprüften Arbeitsstand ab")
    fiscal_nodes = set(consumed)
    metadata = contract["metadata"]
    if not isinstance(metadata, dict):
        raise ValueError("Geprüfte zusätzliche XML-Metadaten müssen als Pfad-Wert-Zuordnung vorliegen")
    for path, expected in metadata.items():
        if value_at(path) != text(expected, "Erwarteter XML-Metadatenwert"):
            raise ValueError("XML-Metadaten weichen von der geprüften Zuordnung ab")
    for element in document.iter():
        if not isinstance(element.tag, str):
            continue
        local_name = etree.QName(element).localname
        if element.attrib and not (element is document and set(element.attrib) == {"version"}):
            raise ValueError("Import-XML enthält ungeprüfte Attribute")
        populated = bool((element.text or "").strip())
        if populated and re.fullmatch(r"Kz\d+", local_name, flags=re.IGNORECASE) and element not in fiscal_nodes:
            raise ValueError("Import-XML enthält eine zusätzliche ungeprüfte Steuerkennzahl")
        if populated and (len(element) or element not in consumed):
            raise ValueError("Import-XML enthält einen zusätzlichen ungeprüften Wert")
    return content, {
        "status": "xsd_validated_and_reconciled",
        "xml_sha256": sha256(content).hexdigest(),
        "xsd_sha256": sha256(schema_path.read_bytes()).hexdigest(),
        "mapping_source": data["mapping"]["source"],
        "encoding": "ISO-8859-15",
        "taxpayer_fields_reconciled": sorted(taxpayer_paths),
        "all_populated_values_reconciled": True,
        "annual_plausibility_validated": False,
        "portal_acceptance_verified": False,
        "transmitted": False,
    }


def csv_text(value):
    return "'" + value if value.lstrip().startswith(("=", "+", "-", "@")) else value


def export(data, values, destination, xml=None):
    if destination.exists():
        raise ValueError("Ausgabeziel besteht bereits. Ein neues Verzeichnis verwenden")
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{destination.name}.", dir=destination.parent))
    stem = f"ustva_{data['year']}_{data['period']}"
    try:
        with (staging / f"{stem}_erfassung.csv").open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream, delimiter=";")
            writer.writerow(["Unternehmer", "Steuernummer", "Jahr", "Zeitraum", "Kennzahl", "Bezeichnung", "Wert", "Einheit", "Fundstelle"])
            for row in data["fields"]:
                value = values[row["kennzahl"]].quantize(UNITS[row["unit"]])
                formatted = format(value, "f").replace(".", ",")
                writer.writerow([csv_text(data["taxpayer"]["name"]), csv_text(data["taxpayer"]["steuernummer"]),
                                 data["year"], data["period"], row["kennzahl"], csv_text(row["label"]),
                                 formatted, row["unit"], csv_text(row["source"])])
        result = {
            **data,
            "status": "prepared_not_transmitted",
            "validation": {"mapping_consistent": True, "arithmetic_passed": True, "reconciliation_passed": True},
            "transmission": {"performed": False, "receipt": None},
        }
        if xml:
            content, report = xml
            (staging / f"{stem}_import.xml").write_bytes(content)
            (staging / f"{stem}_xml_pruefung.json").write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            result["validation"]["import_xml"] = report
        (staging / f"{stem}_arbeitsstand.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.rename(staging, destination)
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--import-xml", type=Path)
    parser.add_argument("--xsd", type=Path)
    parser.add_argument("--schema-root", type=Path)
    args = parser.parse_args()
    if bool(args.import_xml) != bool(args.xsd):
        parser.error("--import-xml und --xsd sind gemeinsam erforderlich")
    if args.schema_root and not args.xsd:
        parser.error("--schema-root benötigt --xsd")
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object)
        values = validate(data)
        xml = validate_xml(args.import_xml, args.xsd, data, values, args.schema_root) if args.import_xml else None
        export(data, values, args.out, xml)
    except (ValueError, OSError, ArithmeticError, TypeError, KeyError) as error:
        parser.exit(1, f"UStVA-Arbeitsstand abgelehnt: {error}\n")
    except Exception as error:
        # lxml ist nur für den optionalen XML-Prüfweg erforderlich.
        parser.exit(1, f"XML-Prüfung fehlgeschlagen: {type(error).__name__}: {error}\n")
    print(f"Erfassungsdateien erzeugt: {args.out}. Status prepared_not_transmitted.")


if __name__ == "__main__":
    main()
