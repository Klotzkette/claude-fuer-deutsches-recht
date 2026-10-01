#!/usr/bin/env python3
"""Prüfdaten exportieren; optional eine XJustiz-Tabelle ohne Erklärungen bilden."""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timezone
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import uuid
from xml.etree import ElementTree as ET

NS = "http://www.xjustiz.de"
ROOT_NAME = "nachricht.inso.insolvenztabelle.uebergabe.0300005"
MONEY = re.compile(r"(?:0|[1-9][0-9]{0,11})\.[0-9]{2}\Z")
ZERO = Decimal("0.00")
MAX_INPUT = 10 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def fields(value, required, optional=()):
    require(isinstance(value, dict), "Ein Objekt wurde erwartet.")
    require(set(required) <= value.keys(), f"Pflichtfelder fehlen: {set(required) - value.keys()}")
    require(value.keys() <= set(required) | set(optional), f"Unbekannte Felder: {value.keys() - set(required) - set(optional)}")


def string(value, maximum=5000):
    require(isinstance(value, str) and bool(value.strip()), "Leerer oder ungültiger Text.")
    require(len(value) <= maximum, f"Text überschreitet {maximum} Zeichen; keine automatische Kürzung.")
    require(not any(ord(c) < 32 and c not in "\n\r\t" for c in value), "Unzulässiges Steuerzeichen.")
    return value


def amount(value):
    require(isinstance(value, str) and MONEY.fullmatch(value), "Geldbetrag als Zeichenkette mit zwei Dezimalstellen und Punkt erwartet.")
    return Decimal(value)


def iso_date(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value), "Datum im Format JJJJ-MM-TT erforderlich.")
    return date.fromisoformat(value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Doppeltes JSON-Feld: {key}")
        result[key] = value
    return result


def read_input(path):
    require(path.stat().st_size <= MAX_INPUT, "Eingabedatei zu groß; getrennte Prüflose bilden.")
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object)


def validate(data):
    fields(data, ("schema_version", "verfahren", "forderungen"), ("xjustiz",))
    require(type(data["schema_version"]) is int and data["schema_version"] == 1, "Unbekannte Eingabeversion.")
    v = data["verfahren"]
    fields(v, ("aktenzeichen", "schuldner", "gericht", "eroeffnung", "anmeldefrist", "stichtag"))
    for key in ("aktenzeichen", "schuldner", "gericht"):
        string(v[key], 255)
    opening, deadline, cutoff = (iso_date(v[k]) for k in ("eroeffnung", "anmeldefrist", "stichtag"))
    require(opening <= deadline and opening <= cutoff, "Eröffnung und Stichtage sind widersprüchlich.")
    require(isinstance(data["forderungen"], list) and 0 < len(data["forderungen"]) <= 10000, "1 bis 10000 Forderungen je Prüflos erforderlich.")
    ids, sheets = set(), set()
    for c in data["forderungen"]:
        fields(c, ("id", "tabellenblatt", "glaeubiger", "eingang", "rang_angemeldet", "hauptforderung", "zinsen", "kosten", "unerlaubte_handlung", "grund", "belege", "tituliert", "titel_bei_den_akten", "fuer_den_ausfall", "sicherheit", "pruefung"), ("xjustiz", "zinsgrund", "kostengrund"))
        for key in ("id", "glaeubiger", "rang_angemeldet", "grund", "sicherheit"):
            string(c[key], 255 if key in ("id", "grund") else 5000)
        require(c["id"] not in ids, "Doppelte Forderungskennung.")
        require(type(c["tabellenblatt"]) is int and c["tabellenblatt"] > 0 and c["tabellenblatt"] not in sheets, "Tabellenblatt muss eindeutig und positiv sein.")
        ids.add(c["id"])
        sheets.add(c["tabellenblatt"])
        require(opening <= iso_date(c["eingang"]) <= cutoff, "Anmeldung außerhalb des erfassten Verfahrenszeitraums.")
        total = sum((amount(c[k]) for k in ("hauptforderung", "zinsen", "kosten")), ZERO)
        require(total > ZERO, "Leere Forderung.")
        require(amount(c["unerlaubte_handlung"]) <= total, "Deliktsbetrag darf die Anmeldung nicht überschreiten.")
        for key, ground in (("zinsen", "zinsgrund"), ("kosten", "kostengrund")):
            if amount(c[key]) > ZERO or ground in c:
                require(ground in c, f"Begründung für {key} fehlt.")
                string(c[ground], 255)
        for key in ("tituliert", "titel_bei_den_akten", "fuer_den_ausfall"):
            require(type(c[key]) is bool, f"{key} muss true oder false sein.")
        require(not c["titel_bei_den_akten"] or c["tituliert"], "Titel liegt vor, aber tituliert=false.")
        require(isinstance(c["belege"], list) and c["belege"], "Mindestens ein Belegverweis, etwa auf die Anmeldung, ist erforderlich.")
        for evidence in c["belege"]:
            string(evidence, 500)
        review = c["pruefung"]
        fields(review, ("status", "begruendung"), ("nicht_bestritten", "bestritten"))
        string(review["begruendung"])
        require(review["status"] in ("offen", "vorschlag"), "Nur interne Prüfung: keine gerichtliche Feststellung erzeugen.")
        if review["status"] == "vorschlag":
            require("nicht_bestritten" in review and "bestritten" in review, "Beide Teilbeträge des Vorschlags fehlen.")
            require(amount(review["nicht_bestritten"]) + amount(review["bestritten"]) == total, "Vorschlag muss die gesamte Anmeldung erfassen; Differenz nicht still löschen.")
        else:
            require("nicht_bestritten" not in review and "bestritten" not in review, "Offene Prüfung darf keine entschiedenen Teilbeträge enthalten.")
        if "xjustiz" in c:
            x = c["xjustiz"]
            fields(x, ("rollennummer", "beteiligtennummer", "beteiligtenkennung", "rang_code"))
            for value in x.values():
                string(value, 255)
    if "xjustiz" in data:
        fields(data["xjustiz"], ("empfaenger_code", "waehrungsliste_version"))
        for value in data["xjustiz"].values():
            string(value, 100)
    return data


def csv_cell(value):
    value = str(value)
    return "'" + value if value.lstrip().startswith(("=", "+", "-", "@")) or value.startswith(("\t", "\r", "\n")) else value


def neutral_exports(data):
    out = io.StringIO(newline="")
    writer = csv.writer(out, delimiter=";")
    writer.writerow(("Kennung", "Tabellenblatt", "Gläubiger", "Eingang", "Nach Anmeldefrist", "Rang angemeldet", "Hauptforderung EUR", "Zinsen EUR", "Kosten EUR", "Gesamt EUR", "Prüfstatus", "Nicht bestritten vorgeschlagen EUR", "Bestritten vorgeschlagen EUR", "Sicherheit", "Begründung", "Belege"))
    for c in data["forderungen"]:
        p = c["pruefung"]
        money_de = lambda value: str(value).replace(".", ",")
        values = (c["id"], c["tabellenblatt"], c["glaeubiger"], c["eingang"], "ja" if c["eingang"] > data["verfahren"]["anmeldefrist"] else "nein", c["rang_angemeldet"], money_de(c["hauptforderung"]), money_de(c["zinsen"]), money_de(c["kosten"]), money_de(sum((amount(c[k]) for k in ("hauptforderung", "zinsen", "kosten")), ZERO)), p["status"], money_de(p.get("nicht_bestritten", "")), money_de(p.get("bestritten", "")), c["sicherheit"], p["begruendung"], " | ".join(c["belege"]))
        writer.writerow(map(csv_cell, values))
    root = ET.Element("pruefdaten", {"format": "intern-1", "gerichtlich-festgestellt": "false"})

    def append(parent, value):
        if isinstance(value, dict):
            for key, item in value.items():
                append(ET.SubElement(parent, key), item)
        elif isinstance(value, list):
            for item in value:
                append(ET.SubElement(parent, "eintrag"), item)
        else:
            parent.text = str(value).lower() if type(value) is bool else str(value)

    append(root, data)
    ET.indent(root)
    return {"Prueftabelle.csv": out.getvalue().encode("utf-8-sig"), "Pruefdaten.json": (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode(), "Pruefdaten_INTERN.xml": ET.tostring(root, encoding="utf-8", xml_declaration=True)}


def xjustiz_export(data, template, schema_path, export_date=None):
    try:
        from lxml import etree as X
    except ImportError as exc:
        raise ValueError("Für die optionale XJustiz-Prüfung wird lxml benötigt; neutrale Exporte funktionieren ohne Zusatzpaket.") from exc
    today = export_date or date.today()
    require(date(2026, 4, 30) <= today < date(2027, 4, 30), "XJustiz 3.6.2 außerhalb des unterstützten Gültigkeitszeitraums; Standards zuerst aktualisieren.")
    require("xjustiz" in data and all("xjustiz" in c for c in data["forderungen"]), "Explizite XJustiz-Zuordnung fehlt.")
    require(template.stat().st_size <= MAX_INPUT, "Stammdatenvorlage zu groß.")
    parser = X.XMLParser(resolve_entities=False, load_dtd=False, no_network=True)
    try:
        tree = X.parse(str(template), parser)
    except X.LxmlError as exc:
        raise ValueError(f"Ungültige XML-Vorlage: {exc}") from exc
    require(not tree.docinfo.doctype, "DTD und externe Entitäten sind nicht zugelassen.")
    root = tree.getroot()
    ns = {"x": NS}
    tag = lambda name: "{" + NS + "}" + name
    require(root.tag == tag(ROOT_NAME), "Nur erstmalige Tabellenübergabe 0300005; Änderungen 0300006 über die Fachsoftware.")
    require(root.find("x:nachrichtenkopf", ns).get("xjustizVersion") == "3.6.2", "Vorlage muss XJustiz 3.6.2 verwenden.")
    require(root.xpath("x:nachrichtenkopf/x:ereignis/code/text()", namespaces=ns) == ["044"], "Nur Ereignis 044 ohne Erklärungen; interne Vorschläge werden nicht als Feststellungen exportiert.")
    require(root.findtext("x:nachrichtenkopf/x:empfaenger/x:auswahl_aktenzeichen/x:aktenzeichen.freitext", namespaces=ns) == data["verfahren"]["aktenzeichen"], "Gerichtsaktenzeichen stimmen nicht überein.")
    require(root.findtext("x:nachrichtenkopf/x:empfaenger/x:informationen/x:auswahl_kommunikationspartner/x:gericht/code", namespaces=ns) == data["xjustiz"]["empfaenger_code"], "Gerichtscode stimmt nicht überein.")
    fd = root.find("x:fachdaten", ns)
    require(fd is not None and len(fd.findall("x:forderung", ns)) == 0, "Vorlage enthält bereits Forderungen; keine stillen Überschreibungen oder Verdoppelungen.")
    roles = {}
    for person in root.findall("x:grunddaten/x:verfahrensdaten/x:beteiligung", ns):
        number = person.findtext("x:beteiligter/x:beteiligtennummer", namespaces=ns)
        for role in person.findall("x:rolle/x:rollennummer", ns):
            require(role.text not in roles, "Doppelte Rollennummer.")
            roles[role.text] = number
    persons = {}
    for person in fd.findall("x:beteiligte.inso", ns):
        number = person.findtext("x:beteiligter/x:ref.beteiligtennummer", namespaces=ns)
        require(number and number not in persons, "Fehlende oder doppelte Beteiligtennummer.")
        persons[number] = person.findtext("x:identifier", namespaces=ns)

    def add(parent, name, text=None):
        element = X.SubElement(parent, "code", nsmap={None: ""}) if name == "code" else X.SubElement(parent, tag(name))
        if text is not None:
            element.text = str(text)
        return element

    def money(parent, value):
        add(parent, "zahl", value)
        currency = add(add(parent, "auswahl_waehrung"), "waehrung")
        currency.set("listVersionID", data["xjustiz"]["waehrungsliste_version"])
        add(currency, "code", "EUR")

    for c in data["forderungen"]:
        x = c["xjustiz"]
        require(roles.get(x["rollennummer"]) == x["beteiligtennummer"] and persons.get(x["beteiligtennummer"]) == x["beteiligtenkennung"], "Rollen- und Beteiligtenzuordnung stimmen nicht überein.")
        f = X.Element(tag("forderung"))
        add(add(f, "referenz"), "ref.rollennummer", x["rollennummer"])
        add(f, "identifier", c["id"])
        add(f, "datumDerAnmeldung", c["eingang"])
        add(add(f, "angemeldeterRang"), "code", x["rang_code"])
        add(f, "tabellenblatt.nr", c["tabellenblatt"])
        for key in ("hauptforderung", "zinsen", "kosten"):
            if key == "hauptforderung" or amount(c[key]) != ZERO:
                part = add(f, key)
                money(add(part, "betrag"), c[key])
                add(part, "grund", c[{"hauptforderung": "grund", "zinsen": "zinsgrund", "kosten": "kostengrund"}[key]])
        for field, key in (("tituliert", "tituliert"), ("titelBeiDenAkten", "titel_bei_den_akten"), ("fuerDenAusfall", "fuer_den_ausfall")):
            add(f, field, str(c[key]).lower())
        money(add(f, "betrag.unerlaubteHandlung"), c["unerlaubte_handlung"])
        # Vollmachten müssen nach den Forderungen stehen; vorhandene Stammdaten bleiben unverändert.
        power = fd.find("x:vollmacht", ns)
        if power is None:
            fd.append(f)
        else:
            power.addprevious(f)
    root.find("x:nachrichtenkopf/x:erstellungszeitpunkt", ns).text = datetime.now(timezone.utc).isoformat()
    root.find("x:nachrichtenkopf/x:absender/x:eigeneNachrichtenID", ns).text = str(uuid.uuid4())
    maker = root.find("x:nachrichtenkopf/x:herstellerinformation", ns)
    require(maker is not None, "Herstellerinformation fehlt.")
    for child in list(maker):
        maker.remove(child)
    for key, value in (("nameDesProdukts", "Insolvenzforderungen-Checker"), ("herstellerDesProdukts", "Klotzkette"), ("version", "1")):
        add(maker, key, value)
    require(schema_path.name == "xjustiz_0300_insolvenz_3_5.xsd", "INSO-Einstiegsschema des vollständigen amtlichen Pakets 3.6.2 erforderlich.")
    try:
        schema = X.XMLSchema(X.parse(str(schema_path), parser))
        schema.assertValid(tree)
        schema.assertValid(X.fromstring(X.tostring(tree), parser))
    except X.LxmlError as exc:
        raise ValueError(f"XJustiz-XSD-Prüfung fehlgeschlagen: {exc}") from exc
    return X.tostring(tree, encoding="UTF-8", xml_declaration=True, pretty_print=True)


def export(data, output, template=None, schema=None):
    validate(data)
    require(not output.exists(), "Zielordner existiert bereits; neuen Ordner wählen.")
    require(bool(template) == bool(schema), "XJustiz-Vorlage und XSD gemeinsam angeben.")
    payload = neutral_exports(data)
    if template:
        payload["Insolvenztabelle_XJustiz_3_6_2_ENTWURF.xml"] = xjustiz_export(data, template, schema)
    note = "Prüfdaten der Insolvenzverwaltung. Keine gerichtliche Feststellung.\n\nPruefdaten_INTERN.xml ist kein XJustiz-Dokument. CSV-Textfelder mit Tabellenformeln sind durch ein vorangestelltes Apostroph entschärft; JSON enthält die unveränderten Texte. Die Fristmarkierung bezeichnet nur einen späteren Eingang, keinen Ausschluss. Sicherheiten werden nicht automatisch abgezogen.\n\n"
    note += "XJustiz: " + ("Entwurf für Ereignis 044 ohne Erklärungen gegen das bereitgestellte XSD geprüft. Schematron, aktuelle externe Codelisten, Gläubigeridentität, vollständiges Verzeichnis, Gerichtsprofil, Anhänge und Versandfreigabe sind noch separat zu prüfen. Keine Signatur, keine Übermittlung.\n" if template else "Nicht erzeugt. Für Gerichtseinreichungen das freigegebene Fachverfahren verwenden oder die dokumentierte Vorlagenübergabe samt amtlichem Schema prüfen.\n")
    payload["README.txt"] = note.encode()
    report = {"forderungen": len(data["forderungen"]), "xjustiz_xsd_geprueft": bool(template), "schematron_geprueft": False, "versandfreigabe": False, "sha256": {name: hashlib.sha256(content).hexdigest() for name, content in payload.items()}}
    if template:
        report["vorlage_sha256"] = hashlib.sha256(template.read_bytes()).hexdigest()
        report["xsd_dateien_sha256"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(schema.parent.glob("*.xsd"))}
    payload["Pruefprotokoll.json"] = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".forderungsexport-", dir=output.parent))
    try:
        for name, content in payload.items():
            (staging / name).write_bytes(content)
        # Ein vorhandenes Ziel darf auch zwischen Prüfung und Veröffentlichung nicht ersetzt werden.
        output.mkdir()
        for path in staging.iterdir():
            path.rename(output / path.name)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return sorted(payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eingabe", type=Path)
    parser.add_argument("ausgabe", type=Path)
    parser.add_argument("--xjustiz-vorlage", type=Path)
    parser.add_argument("--xsd", type=Path)
    args = parser.parse_args()
    try:
        files = export(read_input(args.eingabe), args.ausgabe, args.xjustiz_vorlage, args.xsd)
    except (ValueError, OSError, TypeError, KeyError, AttributeError) as exc:
        parser.exit(2, f"Export abgebrochen: {exc}\n")
    print("Erzeugt: " + ", ".join(files))
    print("Nur Entwürfe. Prüfung und Versandfreigabe durch die Insolvenzverwaltung erforderlich.")


if __name__ == "__main__":
    main()
