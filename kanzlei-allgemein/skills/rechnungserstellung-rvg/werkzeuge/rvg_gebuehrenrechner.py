#!/usr/bin/env python3
"""
rvg_gebuehrenrechner.py
=======================

Rechnet RVG-Gebuehren aus dem Gegenstandswert nach RVG Anlage 2
(Gebuehrentabelle, Fassung Kostenrechtsaenderungsgesetz 2021,
gueltig seit 01.01.2021).

Eingabe
-------

* Gegenstandswert in Euro,
* gewuenschter Gebuehrensatz (Faktor) wie 1,3 (Geschaeftsgebuehr Nr. 2300 VV RVG),
* optional Anzahl Auslagen-Posten / Pauschalen,
* optional Umsatzsteuersatz (19 %).

Ausgabe
-------

* einfache Gebuehr nach Anlage 2 RVG,
* gewichtete Gebuehr (= einfache Gebuehr x Faktor),
* Post- und Telekommunikationspauschale (Nr. 7002 VV RVG: 20 % der Gebuehren, max. 20,00 €),
* Zwischensumme netto, Umsatzsteuer, Brutto.

Beispiele
---------

    python3 rvg_gebuehrenrechner.py --wert 5000 --faktor 1.3
    python3 rvg_gebuehrenrechner.py --wert 25000 --faktor 1.3 --pauschale --ust 19

Quelle
------

RVG Anlage 2 (Gebuehrentabelle) i. d. F. des Kostenrechtsaenderungs-
gesetzes 2021. Die Stufen sind oeffentliches Gesetz, der Code listet
sie zu Pruefzwecken im DataFrame `STUFEN` auf.

Lizenz / Verantwortung
----------------------

Der Rechner deckt die Standardfaelle ab (Anlage 2, glatte Streitwerte
und Auslagenpauschale). Er ersetzt keine RVG-Berechnung durch das
Anwaltskostensoftware-System der Kanzlei und keine Pruefung im
Einzelfall.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import List, Optional


# ---------------------------------------------------------------------------
# RVG Anlage 2 — Gebuehrentabelle (Stand 01.01.2021)
# Liste von (Gegenstandswert_obergrenze, einfache_Gebuehr).
# Innerhalb einer Stufe gilt jeweils der angegebene einfache Gebuehrenbetrag.
# Ueber 500.000 EUR: ab da je 50.000 EUR Erhoehung um 150 EUR (Anlage 2 Stufenfortschreibung).
# ---------------------------------------------------------------------------

STUFEN: List[tuple] = [
    (500, 49.00),
    (1000, 88.00),
    (1500, 127.00),
    (2000, 166.00),
    (3000, 222.00),
    (4000, 278.00),
    (5000, 334.00),
    (6000, 390.00),
    (7000, 446.00),
    (8000, 502.00),
    (9000, 558.00),
    (10000, 614.00),
    (13000, 666.00),
    (16000, 718.00),
    (19000, 770.00),
    (22000, 822.00),
    (25000, 874.00),
    (30000, 955.00),
    (35000, 1036.00),
    (40000, 1117.00),
    (45000, 1198.00),
    (50000, 1279.00),
    (65000, 1373.00),
    (80000, 1467.00),
    (95000, 1561.00),
    (110000, 1655.00),
    (125000, 1749.00),
    (140000, 1843.00),
    (155000, 1937.00),
    (170000, 2031.00),
    (185000, 2125.00),
    (200000, 2219.00),
    (230000, 2351.00),
    (260000, 2483.00),
    (290000, 2615.00),
    (320000, 2747.00),
    (350000, 2879.00),
    (380000, 3011.00),
    (410000, 3143.00),
    (440000, 3275.00),
    (470000, 3407.00),
    (500000, 3539.00),
]


def einfache_gebuehr(wert: float) -> float:
    """Einfache Gebuehr (1,0) nach RVG Anlage 2."""
    if wert <= 0:
        raise ValueError("Gegenstandswert muss > 0 sein.")
    for obergrenze, gebuehr in STUFEN:
        if wert <= obergrenze:
            return gebuehr
    # > 500.000 EUR: pro angefangene 50.000 EUR + 150,00 EUR
    ueberschuss = wert - 500000
    schritte = -(-int(ueberschuss) // 50000)  # ceiling division
    return 3539.00 + schritte * 150.00


# ---------------------------------------------------------------------------
# Auslagenpauschale Nr. 7002 VV RVG
# ---------------------------------------------------------------------------

def post_pauschale(gewichtete_gebuehr: float) -> float:
    """Nr. 7002 VV RVG: 20 % der Gebuehren, hoechstens 20,00 EUR."""
    return min(round(gewichtete_gebuehr * 0.20, 2), 20.00)


# ---------------------------------------------------------------------------
# Ergebnis
# ---------------------------------------------------------------------------

@dataclass
class RVGErgebnis:
    wert: float
    faktor: float
    einfache_gebuehr: float
    gewichtete_gebuehr: float
    pauschale: float
    ust_satz: float
    netto: float
    ust: float
    brutto: float

    @staticmethod
    def _de(value: float, dezimal: int = 2) -> str:
        """Formatiert eine Zahl in deutscher Schreibweise: 1.234,56."""
        return f"{value:>12,.{dezimal}f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def als_text(self) -> str:
        zeilen = [
            f"Gegenstandswert:        {self._de(self.wert)} EUR",
            f"Einfache Gebuehr 1,0:   {self._de(self.einfache_gebuehr)} EUR",
            f"Faktor:                 {self._de(self.faktor)}",
            f"Gewichtete Gebuehr:     {self._de(self.gewichtete_gebuehr)} EUR",
            f"Pauschale Nr. 7002:     {self._de(self.pauschale)} EUR",
            f"Netto-Summe:            {self._de(self.netto)} EUR",
            f"Umsatzsteuer {int(self.ust_satz * 100):>3}%:     {self._de(self.ust)} EUR",
            f"Brutto-Summe:           {self._de(self.brutto)} EUR",
        ]
        return "\n".join(zeilen)


def berechne(wert: float, faktor: float, mit_pauschale: bool = True, ust_satz: float = 0.19) -> RVGErgebnis:
    eg = einfache_gebuehr(wert)
    gg = round(eg * faktor, 2)
    pauschale = post_pauschale(gg) if mit_pauschale else 0.0
    netto = round(gg + pauschale, 2)
    ust = round(netto * ust_satz, 2)
    brutto = round(netto + ust, 2)
    return RVGErgebnis(
        wert=wert,
        faktor=faktor,
        einfache_gebuehr=eg,
        gewichtete_gebuehr=gg,
        pauschale=pauschale,
        ust_satz=ust_satz,
        netto=netto,
        ust=ust,
        brutto=brutto,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="RVG-Gebuehrenrechner nach Anlage 2 (Stand 01.01.2021).")
    parser.add_argument("--wert", required=True, type=float, help="Gegenstandswert in EUR.")
    parser.add_argument("--faktor", required=True, type=float, help="Gebuehrenfaktor (z. B. 1.3 fuer Nr. 2300).")
    parser.add_argument("--ohne-pauschale", action="store_true", help="Auslagenpauschale Nr. 7002 weglassen.")
    parser.add_argument("--ust", type=float, default=19.0, help="Umsatzsteuersatz in Prozent (Default 19).")
    args = parser.parse_args(argv)

    if args.wert <= 0:
        print("FEHLER: Gegenstandswert muss positiv sein.", file=sys.stderr)
        return 1
    if args.faktor <= 0:
        print("FEHLER: Faktor muss positiv sein.", file=sys.stderr)
        return 1

    ergebnis = berechne(
        wert=args.wert,
        faktor=args.faktor,
        mit_pauschale=not args.ohne_pauschale,
        ust_satz=args.ust / 100.0,
    )
    print(ergebnis.als_text())
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
