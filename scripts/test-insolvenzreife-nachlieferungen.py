"""Drei nachgereichte Originalbelege gegen die öffentliche Rechenschnittstelle prüfen."""
import csv
from decimal import Decimal
import io
import json
from pathlib import Path
import subprocess
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "zahlungsunfaehigkeits-und-ueberschuldungspruefer/app/cli.mjs"
EDITION = ROOT / "docs/workshops/insolvenzreife-nachlieferungen"


def run(data):
    call = subprocess.run(["node", str(APP), "-"], input=json.dumps(data), capture_output=True, text=True, check=True)
    return json.loads(call.stdout)


def case(slug):
    return json.loads((ROOT / "quality/insolvenzreife" / (slug + "-recheninput.json")).read_bytes())


def day(data, iso):
    entries = data["dates"] if "dates" in data else data["results"]
    return next(x for x in entries if x["date"] == iso)


def tables(slug, evidence):
    with ZipFile(EDITION / "downloads" / (slug + "-mit-nachlieferung.zip")) as z:
        def csv_rows(member):
            return list(csv.DictReader(io.StringIO(z.read(member).decode("utf-8-sig")), delimiter=";"))
        return (csv_rows("Nachlieferung/" + evidence),
                csv_rows("Grundakte/02_Buchhaltung/01_Buchungsjournal_EUR_Cent.csv"))


def cents(value):
    return int(Decimal(value.replace(",", ".")) * 100)


class Nachlieferungen(unittest.TestCase):
    def test_cottbus_doppelzaehlung_des_antragsbetrags(self):
        slug = "keramikfabrik-cottbus"
        log, journal = tables(slug, "03_Linienhistorie.csv")
        date = "2026-05-11"
        data = case(slug)
        bank = next(x for x in day(data, date)["liquidity"]["assets"] if x["id"] == "CB-BANK-02")
        gross = int([r for r in journal if r["value_on"] <= date][-1]["balance_cents"])
        self.assertEqual(gross, 7_000_000)
        self.assertEqual(log[-1]["Zeit_MESZ"], "11.05.2026 07:48")
        self.assertEqual(bank["amountCents"], cents(log[-1]["Nominal_EUR"]))
        bank["decision"] = "open"
        self.assertEqual(day(run(data), date)["liquidity"]["result"], "open")
        self.assertEqual(cents(log[-1]["Zusaetzlich_abrufbar_EUR"]), 0)
        bank.update(decision="exclude", source="Nachlieferung/03_Linienhistorie.csv, 11.05.2026 07:48",
                    reason="Für L-119/2 ist kein Abruf bewilligt.")
        totals = day(run(data), date)["liquidity"]["totals"]
        self.assertEqual((totals["A1"], totals["A2"], totals["P1"], totals["P2"]), (gross, 7_700_000, 20_000_000, 13_150_000))
        self.assertEqual((totals["remainingGapCents"], totals["remainingGapBasisPoints"]), (18_450_000, 5566))

    def test_zehlendorf_bewertungsvariante_bereits_im_april(self):
        slug = "metallbau-berlin-zehlendorf"
        register, _ = tables(slug, "03_Besichtigungsbuch.csv")
        data = case(slug)
        original = run(data)
        self.assertEqual(original["firstCandidate"]["overindebtedness"]["date"], "2026-05-18")
        source = next(row for row in register if row["Termin"] == "16.04.2026")
        alternative = cents(source["Preisindikation_EUR"]) - cents(source["Nebenkosten_Verwertung_EUR"])
        self.assertEqual(alternative, 54_500_000)
        for date in ("2026-04-20", "2026-05-17"):
            hall = next(x for x in day(data, date)["overindebtedness"]["assets"] if x["id"] == "BZ-INV-01")
            hall.update(amountCents=alternative, source="Nachlieferung/03_Besichtigungsbuch.csv, 26/44-B",
                        reason="Variante mit bloßer Pkw-Zufahrt und realisierbarer Lagernutzung zum damaligen Termin.")
        revised = run(data)
        self.assertEqual(revised["firstCandidate"]["overindebtedness"]["date"], "2026-04-20")
        self.assertEqual(day(revised, "2026-04-20")["overindebtedness"]["totals"]["netAssetsCents"], -3_512_000)
        self.assertEqual([r["liquidity"] for r in original["results"]], [r["liquidity"] for r in revised["results"]])

    def test_prenzlau_buchsaldo_und_reserve_ein_konto(self):
        slug = "hubschrauber-prenzlau"
        log, journal = tables(slug, "03_Dispositionsjournal.csv")
        date = "2026-05-18"
        data = case(slug)
        assets = day(data, date)["liquidity"]["assets"]
        cash = next(x for x in assets if x["id"] == "PR-BANK-CASH")
        reserve = next(x for x in assets if x["id"] == "PR-RES-01")
        gross = int([r for r in journal if r["value_on"] <= date][-1]["balance_cents"])
        self.assertEqual(gross, cents(log[0]["Buchsaldo_EUR"]))
        # Sensitivität: Die Frühansicht vor 08:05 ließe auch den zweiten Teilbetrag frei erscheinen.
        reserve.update(decision="include", source="Nachlieferung/03_Dispositionsjournal.csv, 07:58")
        early = day(run(data), date)["liquidity"]["totals"]
        self.assertEqual((early["A1"], early["remainingGapCents"]), (gross, 11_445_000))
        self.assertEqual(gross - cents(log[1]["Reserviert_EUR"]), cents(log[1]["Verfuegbar_EUR"]))
        self.assertEqual(cash["amountCents"], cents(log[1]["Verfuegbar_EUR"]))
        reserve.update(decision="exclude", source="Nachlieferung/03_Dispositionsjournal.csv, 08:05 und 10:20",
                       reason="Kartenreserve wurde gesperrt und bis zum Fensterende nicht freigegeben.")
        after = day(run(data), date)["liquidity"]["totals"]
        self.assertEqual((after["A1"], after["A2"], after["P1"], after["P2"]), (4_000_000, 6_400_000, 11_600_000, 15_745_000))
        self.assertEqual((after["remainingGapCents"], after["remainingGapBasisPoints"]), (16_945_000, 6197))


if __name__ == "__main__":
    unittest.main()
