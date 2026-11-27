#!/usr/bin/env python3
"""Regressionsproben für Datumsgrenzen und den Belegabgleich im Arbeitsvermerk."""

import unittest

from aktenarbeit_inhalte import akte, postquellen
from aktenarbeit_quellen import saetze
from aktenbestand import ROOT, fallquellen


class ArbeitsvermerkTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quellen = {v["id"]: (k, v) for k, v in fallquellen().items()}
        cls.eingang = postquellen(ROOT)

    def vermerk(self, ident):
        key, item = self.quellen[ident]
        return akte(ROOT, key, item, self.eingang)[2]

    def test_datum_und_nummer_im_fragesatz(self):
        frage = "Was prüften Sie am 20. und 21. Oktober zu Antwort Nr. 6?"
        self.assertEqual(saetze("Anbei der Bogen. " + frage), ["Anbei der Bogen.", frage])

    def test_rechnung_belegt_den_betrag(self):
        vermerk = self.vermerk("agb-fahrradwerkstatt-kettenglueck-leipzig")
        beleg = next(e for e in vermerk["evidence"] if e["title"] == "04_Rechnung_RK286.pdf")
        self.assertIn("Rechnungsbetrag 310,00 Euro", beleg["text"])
        self.assertEqual(beleg["source"], "Seite 1")

    def test_veroeffentlichte_antwort_und_interne_wertung(self):
        vermerk = self.vermerk("interstate-11-it-baupruefung")
        belege = {e["source"]: e["text"] for e in vermerk["evidence"]}
        self.assertIn("Eine separate Zuordnungsdatei ist zulässig", belege["Textabsatz 3"])
        self.assertIn("C ohne Bild im Hauptblatt", belege["Aufstellung!A6"])
        self.assertIn("Was haben die beiden Prüfenden bei C am 20. und 21. Oktober", vermerk["fields"][-1])


if __name__ == "__main__":
    unittest.main()
