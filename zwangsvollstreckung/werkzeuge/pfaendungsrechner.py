#!/usr/bin/env python3
"""Pfaendungsrechner nach Tabelle 1.7.2025.

Berechnet den pfaendbaren Anteil des Nettoarbeitseinkommens nach
Pfaendungsfreigrenzenbekanntmachung 2025 (BGBl 2025 I Nr. 110, 11.4.2025).
Gilt vom 1.7.2025 bis 30.6.2026.

Grundlagen:
- Paragraf 850c Abs. 1 ZPO  Grundfreibetrag
- Paragraf 850c Abs. 2 ZPO  Erhoehungsbetraege fuer Unterhaltsberechtigte
- Paragraf 850c Abs. 3 ZPO  Quoten 3/10, 5/10, 7/10 und Vollpfaendungsgrenze
- Paragraf 850c Abs. 5 ZPO  Aufrundung auf naechsten vollen Zehner minus 1 Cent

Quelle: NWB Datenbank, Finanztip, BGBl 2025 I Nr. 110.

Eckwerte (Tabelle 1.7.2025; BGBl 2025 I Nr. 110 vom 11.4.2025):
- Grundfreibetrag (0 Unterhaltspflichtige): 1.555,00 EUR / Monat
- Erhoehung 1. unterhaltsberechtigte Person: 585,23 EUR
- Erhoehung je weitere Person (bis 5. Person): 326,04 EUR
- Vollpfaendungsgrenze: 4.766,99 EUR (darueber alles pfaendbar)

Die Berechnung folgt der Methode der amtlichen Tabelle: Netto wird auf den
naechsten vollen 10-EUR-Schritt nach unten abgerundet (Paragraf 850c Abs. 5 ZPO);
vom Ueberschuss ueber den nach Tabelle erhoehten Freibetrag wird der pfaendbare
Anteil mit unterhaltsabhaengiger Quote berechnet.

Benutzung:
    python3 pfaendungsrechner.py --netto 2500 --unterhalt 1
    python3 pfaendungsrechner.py --netto 3200 --unterhalt 2 --privileg
    python3 pfaendungsrechner.py --tabelle  (gibt Tabelle 0-4 Unterhalt aus)
"""

from __future__ import annotations

import argparse
import datetime as _dt
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN

# --------------------------------------------------------------------------- #
# Konstanten Tabelle 1.7.2025
# --------------------------------------------------------------------------- #

TABELLE_GUELTIG_AB = _dt.date(2025, 7, 1)
TABELLE_GUELTIG_BIS = _dt.date(2026, 6, 30)

GRUNDFREIBETRAG = Decimal("1555.00")          # Paragraf 850c Abs. 1 ZPO
ERHOEHUNG_ERSTE_PERSON = Decimal("585.23")    # Paragraf 850c Abs. 2 Satz 1 ZPO
ERHOEHUNG_WEITERE_PERSON = Decimal("326.04")  # Paragraf 850c Abs. 2 Satz 2 ZPO
VOLLPFAENDUNGSGRENZE = Decimal("4766.99")     # Paragraf 850c Abs. 3 Satz 3 ZPO

# Quoten gemaess Paragraf 850c Abs. 3 ZPO (auf den den Grundfreibetrag
# uebersteigenden Teil bis zur Vollpfaendungsgrenze):
# - 0 Unterhaltspflichten:  3/10 unpfaendbar -> 7/10 pfaendbar
# - 1 Unterhaltspflicht:    3/10 + 2/10 unpfaendbar -> 5/10 pfaendbar
# - 2 Unterhaltspflichten:  6/10 unpfaendbar -> 4/10 pfaendbar
# - 3 Unterhaltspflichten:  7/10 unpfaendbar -> 3/10 pfaendbar
# - 4 Unterhaltspflichten:  8/10 unpfaendbar -> 2/10 pfaendbar
# - 5 Unterhaltspflichten:  9/10 unpfaendbar -> 1/10 pfaendbar
# Ab der 6. Person erfolgt keine automatische weitere Reduktion mehr;
# Anpassung durch das Vollstreckungsgericht nach Paragraf 850f ZPO.

QUOTE_GLAEUBIGER_NACH_UP: dict[int, Decimal] = {
    0: Decimal("0.7"),
    1: Decimal("0.5"),
    2: Decimal("0.4"),
    3: Decimal("0.3"),
    4: Decimal("0.2"),
    5: Decimal("0.1"),
}

# P-Konto Sockel Paragraf 850k ZPO (AG SBV Bescheinigung Stand 1.7.2025).
# Aufrundung des Grundfreibetrags auf naechsten vollen 10er.
P_KONTO_SOCKEL = Decimal("1560.00")
P_KONTO_ERHOEHUNG_ERSTE = Decimal("585.23")
P_KONTO_ERHOEHUNG_WEITERE = Decimal("326.04")

# Selbstbehalt Paragraf 850d ZPO (Duesseldorfer Tabelle Stand 2025,
# Erwerbstaetiger gegenueber minderjaehrigen Kindern)
SELBSTBEHALT_PRIVILEG = Decimal("1450.00")


# --------------------------------------------------------------------------- #
# Berechnung
# --------------------------------------------------------------------------- #


@dataclass
class Berechnungsergebnis:
    netto: Decimal
    unterhaltspflichten: int
    freibetrag: Decimal
    ueber_freibetrag: Decimal
    pfaendbar: Decimal
    schuldneranteil: Decimal
    privilegiert: bool
    hinweise: list[str]

    def als_text(self) -> str:
        zeilen = [
            "PFAENDUNGSBERECHNUNG (Tabelle 1.7.2025)",
            "",
            f"Netto:                  {self.netto:>10} EUR / Monat",
            f"Unterhaltspflichten:    {self.unterhaltspflichten:>10}",
            f"Freibetrag:             {self.freibetrag:>10} EUR",
            f"Ueber Freibetrag:       {self.ueber_freibetrag:>10} EUR",
            f"Pfaendbar / Monat:      {self.pfaendbar:>10} EUR",
            f"Schuldneranteil:        {self.schuldneranteil:>10} EUR",
            f"Privileg Paragraf 850d: {'ja' if self.privilegiert else 'nein':>10}",
            "",
            f"Tabelle gueltig bis:    {TABELLE_GUELTIG_BIS.strftime('%d.%m.%Y')}",
        ]
        if self.hinweise:
            zeilen.append("")
            zeilen.append("Hinweise:")
            for h in self.hinweise:
                zeilen.append(f"- {h}")
        return "\n".join(zeilen)


def _quantize(value: Decimal) -> Decimal:
    """Auf zwei Nachkommastellen kaufmaennisch abrunden (Glaeubiger bekommt
    nicht mehr als rechnerisch ausgewiesen)."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_DOWN)


def gueltigkeits_warnung(heute: _dt.date | None = None) -> str | None:
    """Gibt eine Warnung zurueck, wenn die aktuelle Tabelle bald ablaeuft
    oder bereits abgelaufen ist. Pflicht-Selbstcheck nach § 850c Abs. 4 ZPO
    (jaehrliche Anpassung der Pfaendungsfreigrenzen)."""
    today = heute if heute is not None else _dt.date.today()
    # Die jaehrliche Bekanntmachung knuepft an den Tabellenstart an,
    # nicht an das Kalenderjahr des Tagesdatums (sonst wird bei spaeter
    # Aktualisierung auf das falsche Veroeffentlichungsjahr verwiesen).
    fehlendes_jahr = TABELLE_GUELTIG_AB.year + 1
    if today > TABELLE_GUELTIG_BIS:
        return (
            f"WARNUNG: Pfaendungstabelle ist seit {TABELLE_GUELTIG_BIS.strftime('%d.%m.%Y')} "
            f"abgelaufen. Aktuelles Tagesdatum {today.strftime('%d.%m.%Y')}. "
            f"Die hier hinterlegten Eckwerte (Stand 1.7.2025) duerfen nicht mehr verwendet werden. "
            f"Pflicht: Pfaendungsfreigrenzenbekanntmachung {fehlendes_jahr} (BGBl. I) abrufen "
            f"und Modul aktualisieren. Verwendung alter Werte = Pfaendungsfehler mit Aufhebungsrisiko."
        )
    abstand = (TABELLE_GUELTIG_BIS - today).days
    if 0 <= abstand <= 30:
        return (
            f"HINWEIS: Pfaendungstabelle laeuft am {TABELLE_GUELTIG_BIS.strftime('%d.%m.%Y')} ab "
            f"(in {abstand} Tagen). Naechste Bekanntmachung des BMJ zu § 850c Abs. 4 ZPO "
            f"vorbereiten und Modul aktualisieren."
        )
    return None


def berechne(
    netto: Decimal | float | str,
    unterhaltspflichten: int = 0,
    privileg_850d: bool = False,
    selbstbehalt: Decimal | float | str | None = None,
) -> Berechnungsergebnis:
    """Berechne den pfaendbaren Anteil des Arbeitseinkommens.

    Parameters
    ----------
    netto
        Monatliches Nettoeinkommen in EUR.
    unterhaltspflichten
        Anzahl unterhaltsberechtigter Personen.
    privileg_850d
        True, wenn die Forderung eine privilegierte Unterhaltsforderung
        nach Paragraf 850d ZPO ist. Selbstbehalt wird dann vom Gericht
        festgesetzt; das Werkzeug zeigt nur einen Richtwert.
    selbstbehalt
        Optionaler Selbstbehalt fuer Paragraf 850d ZPO; default ist
        SELBSTBEHALT_PRIVILEG.
    """
    netto_d = Decimal(str(netto))
    if netto_d < 0:
        raise ValueError("Netto darf nicht negativ sein")
    if unterhaltspflichten < 0:
        raise ValueError("Unterhaltspflichten darf nicht negativ sein")

    hinweise: list[str] = []

    # Paragraf 850c Abs. 5 ZPO: Netto auf naechsten vollen 10-EUR-Schritt
    # nach unten abrunden (Tabellenmethode). Nur fuer die regulaere
    # Tabellenberechnung; Paragraf 850d ZPO laeuft separat.
    netto_abger = (netto_d / Decimal("10")).to_integral_value(
        rounding=ROUND_DOWN
    ) * Decimal("10")

    if privileg_850d:
        selbst = Decimal(str(selbstbehalt)) if selbstbehalt is not None else SELBSTBEHALT_PRIVILEG
        freibetrag = selbst
        ueber = max(netto_d - freibetrag, Decimal("0"))
        pfaendbar = _quantize(ueber)  # privilegiert: voller Zugriff oberhalb Selbstbehalt
        schuldneranteil = _quantize(netto_d - pfaendbar)
        hinweise.append(
            "Paragraf 850d ZPO: Selbstbehalt wird vom Vollstreckungsgericht "
            "festgesetzt; hier Richtwert nach Duesseldorfer Tabelle."
        )
        return Berechnungsergebnis(
            netto=_quantize(netto_d),
            unterhaltspflichten=unterhaltspflichten,
            freibetrag=_quantize(freibetrag),
            ueber_freibetrag=_quantize(ueber),
            pfaendbar=pfaendbar,
            schuldneranteil=schuldneranteil,
            privilegiert=True,
            hinweise=hinweise,
        )

    # Regulaere Berechnung Paragraf 850c ZPO
    # Freibetrag fuer die Anzeige (Sockel + Tabellen-Erhoehungen bis 5 Personen).
    freibetrag = GRUNDFREIBETRAG
    if unterhaltspflichten >= 1:
        freibetrag += ERHOEHUNG_ERSTE_PERSON
    if unterhaltspflichten >= 2:
        bis_fuenf = min(unterhaltspflichten, 5) - 1
        freibetrag += ERHOEHUNG_WEITERE_PERSON * bis_fuenf

    if unterhaltspflichten > 5:
        hinweise.append(
            "Tabelle stuft bis 5 Unterhaltspflichtige; ab der 6. Person erfolgt "
            "Anpassung durch das Vollstreckungsgericht (Paragraf 850f ZPO). "
            "Werkzeug rechnet hier mit Tabellenwerten fuer 5 Personen."
        )

    ueber = max(netto_abger - freibetrag, Decimal("0"))

    # Pfaendbarkeitsquote im Tabellenbereich nach Unterhaltsstaffel
    # Paragraf 850c Abs. 3 Saetze 1 und 2 ZPO.
    quote_glaeubiger = QUOTE_GLAEUBIGER_NACH_UP[min(unterhaltspflichten, 5)]

    if netto_abger >= VOLLPFAENDUNGSGRENZE:
        # alles oberhalb Vollpfaendungsgrenze ist 100 % pfaendbar,
        # darunter quotal mit unterhaltsabhaengiger Quote
        teil_unter_grenze = max(VOLLPFAENDUNGSGRENZE - freibetrag, Decimal("0"))
        teil_ueber_grenze = netto_abger - VOLLPFAENDUNGSGRENZE
        pfaendbar_quotal = teil_unter_grenze * quote_glaeubiger
        pfaendbar = _quantize(pfaendbar_quotal + teil_ueber_grenze)
        hinweise.append(
            f"Netto liegt ueber der Vollpfaendungsgrenze {VOLLPFAENDUNGSGRENZE} EUR; "
            "darueber 100 Prozent pfaendbar."
        )
    else:
        pfaendbar = _quantize(ueber * quote_glaeubiger)

    schuldneranteil = _quantize(netto_d - pfaendbar)

    return Berechnungsergebnis(
        netto=_quantize(netto_d),
        unterhaltspflichten=unterhaltspflichten,
        freibetrag=_quantize(freibetrag),
        ueber_freibetrag=_quantize(ueber),
        pfaendbar=pfaendbar,
        schuldneranteil=schuldneranteil,
        privilegiert=False,
        hinweise=hinweise,
    )


def p_konto_freibetrag(unterhaltspflichten: int = 0) -> Decimal:
    """Sockelbetrag Paragraf 850k ZPO inkl. Erhoehungen (bis 5 Personen tabelliert;
    ab der 6. Person Anpassung durch das Vollstreckungsgericht)."""
    if unterhaltspflichten < 0:
        raise ValueError("Unterhaltspflichten darf nicht negativ sein")
    betrag = P_KONTO_SOCKEL
    if unterhaltspflichten >= 1:
        betrag += P_KONTO_ERHOEHUNG_ERSTE
    if unterhaltspflichten >= 2:
        bis_fuenf = min(unterhaltspflichten, 5) - 1
        betrag += P_KONTO_ERHOEHUNG_WEITERE * bis_fuenf
    return _quantize(betrag)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Pfaendungsrechner nach Tabelle 1.7.2025 (Paragraf 850c ZPO)."
    )
    p.add_argument("--netto", type=str, help="Nettoeinkommen pro Monat in EUR.")
    p.add_argument(
        "--unterhalt",
        type=int,
        default=0,
        help="Anzahl unterhaltsberechtigter Personen (Default 0).",
    )
    p.add_argument(
        "--privileg",
        action="store_true",
        help="Privilegierte Unterhaltsforderung Paragraf 850d ZPO.",
    )
    p.add_argument(
        "--selbstbehalt",
        type=str,
        default=None,
        help="Selbstbehalt fuer Paragraf 850d ZPO (Default 1.450,00 EUR).",
    )
    p.add_argument(
        "--p-konto",
        action="store_true",
        help="Statt Berechnung den P-Konto-Freibetrag ausgeben.",
    )
    p.add_argument(
        "--tabelle",
        action="store_true",
        help="Druckt eine kompakte Tabelle (0-5 Unterhaltspflichten / 1500-5000 EUR).",
    )
    return p


def _print_tabelle() -> None:
    print("Pfaendungstabelle (Auszug) - Tabelle 1.7.2025")
    print()
    kopf = ["Netto"] + [f"U={n}" for n in range(0, 6)]
    print(" | ".join(f"{c:>10}" for c in kopf))
    print("-" * (12 * len(kopf)))
    for netto in range(1500, 5001, 100):
        zeile = [f"{netto:>10}"]
        for n in range(0, 6):
            r = berechne(Decimal(netto), n)
            zeile.append(f"{r.pfaendbar:>10}")
        print(" | ".join(zeile))


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    ns = parser.parse_args(argv)

    # Gueltigkeits-Pruefung vor jeder Ausgabe: Pflicht-Selbstcheck, damit
    # nach Ablauf der Tabelle (30.6.2026) keine alten Werte unbemerkt
    # weiterverwendet werden.
    warn = gueltigkeits_warnung()
    if warn:
        import sys
        print(warn, file=sys.stderr)

    if ns.tabelle:
        _print_tabelle()
        return 0

    if ns.p_konto:
        print(
            f"P-Konto-Freibetrag (Paragraf 850k ZPO) bei "
            f"{ns.unterhalt} Unterhaltspflichtigen: "
            f"{p_konto_freibetrag(ns.unterhalt)} EUR / Monat"
        )
        return 0

    if not ns.netto:
        parser.error("--netto ist erforderlich (oder --tabelle bzw. --p-konto).")

    result = berechne(
        netto=ns.netto,
        unterhaltspflichten=ns.unterhalt,
        privileg_850d=ns.privileg,
        selbstbehalt=ns.selbstbehalt,
    )
    print(result.als_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
