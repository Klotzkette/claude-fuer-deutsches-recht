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

Eckwerte (Tabelle 1.7.2025):
- Grundfreibetrag (0 Unterhaltspflichtige): 1.559,99 EUR / Monat
- Erhoehung 1. unterhaltsberechtigte Person: 585,23 EUR
- Erhoehung je weitere Person: 326,04 EUR
- Vollpfaendungsgrenze: 4.766,99 EUR (darueber alles pfaendbar)

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

GRUNDFREIBETRAG = Decimal("1559.99")          # Paragraf 850c Abs. 1 ZPO
ERHOEHUNG_ERSTE_PERSON = Decimal("585.23")    # Paragraf 850c Abs. 2 Satz 1 ZPO
ERHOEHUNG_WEITERE_PERSON = Decimal("326.04")  # Paragraf 850c Abs. 2 Satz 2 ZPO
VOLLPFAENDUNGSGRENZE = Decimal("4766.99")     # Paragraf 850c Abs. 3 Satz 3 ZPO

# Quoten gemaess Paragraf 850c Abs. 3 ZPO
# 0   bis Freibetrag                  unpfaendbar
# 1   3/10 des den Freibetrag uebersteigenden Teils gehen an den Schuldner
# 2   weitere 2/10 fuer 1. Unterhaltspflichtigen
# 3   weitere 1/10 fuer jede weitere Person (bis 5)
# In der vereinfachten praktischen Berechnung des BMJ wird mit gestaffelten
# Sockelbetraegen pro Unterhaltspflichtigem gearbeitet. Diese Implementierung
# folgt der Tabellenmethode: Freibetrag = Sockel + n * Erhoehung, darueber
# 7/10 pfaendbar (Schuldneranteil 3/10), ab Vollpfaendungsgrenze 100 % pfaendbar.

QUOTE_SCHULDNER = Decimal("0.3")  # 3/10 bleiben Schuldner
QUOTE_GLAEUBIGER = Decimal("0.7")  # 7/10 sind pfaendbar

# P-Konto Sockel Paragraf 850k ZPO (AG SBV Bescheinigung Stand 1.7.2025)
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
    freibetrag = GRUNDFREIBETRAG
    if unterhaltspflichten >= 1:
        freibetrag += ERHOEHUNG_ERSTE_PERSON
    if unterhaltspflichten >= 2:
        freibetrag += ERHOEHUNG_WEITERE_PERSON * (unterhaltspflichten - 1)

    ueber = max(netto_d - freibetrag, Decimal("0"))

    if netto_d >= VOLLPFAENDUNGSGRENZE:
        # alles oberhalb Vollpfaendungsgrenze ist 100 % pfaendbar,
        # darunter quotal
        teil_unter_grenze = max(VOLLPFAENDUNGSGRENZE - freibetrag, Decimal("0"))
        teil_ueber_grenze = netto_d - VOLLPFAENDUNGSGRENZE
        pfaendbar_quotal = teil_unter_grenze * QUOTE_GLAEUBIGER
        pfaendbar = _quantize(pfaendbar_quotal + teil_ueber_grenze)
        hinweise.append(
            f"Netto liegt ueber der Vollpfaendungsgrenze {VOLLPFAENDUNGSGRENZE} EUR; "
            "darueber 100 Prozent pfaendbar."
        )
    else:
        pfaendbar = _quantize(ueber * QUOTE_GLAEUBIGER)

    schuldneranteil = _quantize(netto_d - pfaendbar)

    if unterhaltspflichten > 5:
        hinweise.append(
            "Tabelle stuft bis 5 Unterhaltspflichtige; ab der 6. Person erfolgt "
            "Anpassung durch das Vollstreckungsgericht (Paragraf 850f ZPO)."
        )

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
    """Sockelbetrag Paragraf 850k ZPO inkl. Erhoehungen."""
    if unterhaltspflichten < 0:
        raise ValueError("Unterhaltspflichten darf nicht negativ sein")
    betrag = P_KONTO_SOCKEL
    if unterhaltspflichten >= 1:
        betrag += P_KONTO_ERHOEHUNG_ERSTE
    if unterhaltspflichten >= 2:
        betrag += P_KONTO_ERHOEHUNG_WEITERE * (unterhaltspflichten - 1)
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
        help="Druckt eine kompakte Tabelle (0-4 Unterhaltspflichten, 1500-5000 EUR).",
    )
    return p


def _print_tabelle() -> None:
    print("Pfaendungstabelle (Auszug) - Tabelle 1.7.2025")
    print()
    kopf = ["Netto"] + [f"U={n}" for n in range(0, 5)]
    print(" | ".join(f"{c:>10}" for c in kopf))
    print("-" * (12 * len(kopf)))
    for netto in range(1500, 5001, 100):
        zeile = [f"{netto:>10}"]
        for n in range(0, 5):
            r = berechne(Decimal(netto), n)
            zeile.append(f"{r.pfaendbar:>10}")
        print(" | ".join(zeile))


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    ns = parser.parse_args(argv)

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
