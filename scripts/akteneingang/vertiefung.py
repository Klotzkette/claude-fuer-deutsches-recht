"""Führt die fachlich redigierten Fassungen mit der datierten ursprünglichen Eingangspost zusammen."""

from __future__ import annotations

import json
from copy import deepcopy
from datetime import date

from .quellen import DATA

VERZEICHNIS = DATA.parent / "grundakten-vertiefung"
TAG = "grundakten-fachakten-v1.1.0"
FACHDATEIEN = ("sozial-arbeit", "datenschutz-gesellschaft", "insolvenz")


def fachredaktion():
    by_case = {}
    for fach in FACHDATEIEN:
        with (VERZEICHNIS / (fach + ".json")).open() as f:
            for case, record in json.load(f).items():
                by_case.setdefault(case, []).append((fach, record))
    return by_case


def falldokumente(base, fassungen):
    original = deepcopy(base)
    start = len(original["unterlagen"])
    for fach, teil in fassungen:
        if not teil["ausbau"] or len(teil["wechsel"]) < 2:
            raise ValueError(
                f"{fach}: bisherige Unterlage und mindestens zwei weitere Eingangsbelege erforderlich"
            )
        for fortsetzung in teil["ausbau"]:
            nr = fortsetzung["nr"]
            if not isinstance(nr, int) or not 1 <= nr <= start:
                raise ValueError(f"{fach}: unbekannte Ausgangsunterlage {nr}")
            doc = original["unterlagen"][nr - 1]
            if "berichtigung" in fortsetzung:
                korrektur = fortsetzung["berichtigung"]
                if not korrektur or korrektur.keys() - {"von", "datum"}:
                    raise ValueError("Unbekannte Berichtigung: " + str(korrektur))
                if "von" in korrektur and (
                    not isinstance(korrektur["von"], str)
                    or not korrektur["von"].strip()
                ):
                    raise ValueError("Für die Absenderberichtigung fehlt der Name")
                if "datum" in korrektur:
                    date.fromisoformat(korrektur["datum"])
                doc.update(korrektur)
            text = fortsetzung["absatz"]
            if (
                not isinstance(text, list)
                or not all(isinstance(p, str) and p.strip() for p in text)
                or not text
            ):
                raise ValueError("Leere Fortsetzung: " + doc["titel"])
            doc["text"].extend(text)
            doc["_fachfassung"] = True
        offset = len(original["unterlagen"]) - start
        for item in deepcopy(teil["wechsel"]):
            for feld in ("antwort_auf", "anlage_nr"):
                if feld in item:
                    nr = item[feld]
                    if not isinstance(nr, int) or not 1 <= nr <= start + len(
                        teil["wechsel"]
                    ):
                        raise ValueError(f"{fach}: ungültige Dokumentnummer {nr}")
                    item[feld] = nr + offset if nr > start else nr
            item["_fachfassung"] = True
            original["unterlagen"].append(item)
    return original


def fachrouten(records, keys):
    return {
        key: (
            records[key].get("id", key.split("/")[-1]),
            "druckakte-" + records[key].get("id", key.split("/")[-1]) + ".zip",
        )
        for key in keys
    }


def fachauswahl(catalog, artikel):
    themen = fachredaktion()
    if set(themen) - set(catalog):
        raise ValueError(
            "Unbekannter Aktenpfad in der Fachredaktion: "
            + str(set(themen) - set(catalog))
        )
    selected = {k: catalog[k] for k in artikel if k in themen}
    ausgabe = {k: falldokumente(artikel[k], themen[k]) for k in selected}
    original = json.loads((VERZEICHNIS / "fortschreibungen.json").read_text())
    for key in original:
        if key not in themen:
            raise ValueError("Fortschreibung außerhalb der Fachauswahl: " + key)
        if key in ausgabe:
            ausgabe[key]["fortschreibungen"] = original[key]
    return selected, ausgabe, fachrouten(selected, selected)
