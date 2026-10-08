from __future__ import annotations

import importlib.util
import json
import re
import stat
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
sys.path.insert(0, str(SCRIPTS))

from _vorlagen_dateien import (  # noqa: E402
    THEMENORDNER,
    pruefe_bestandsstruktur,
    vorlagenordner,
)
from _atomar import bytes_atomar_schreiben  # noqa: E402


def lade_script(name: str, dateiname: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / dateiname)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"{dateiname} konnte nicht geladen werden")
    modul = importlib.util.module_from_spec(spec)
    sys.modules[name] = modul
    spec.loader.exec_module(modul)
    return modul


download_index = lade_script("build_download_index_test", "build-download-index.py")
release_assets = lade_script("build_release_assets_test", "build-release-assets.py")
kategorien_check = lade_script("check_kategorien_index_test", "check-kategorien-index.py")
run_eval = lade_script("run_eval_inventory_test", "run-eval.py")
validate_vorlagen = lade_script("validate_vorlagen_inventory_test", "validate-vorlagen.py")


class RepositoryInventoryTest(unittest.TestCase):
    def test_gesamtpaket_schliesst_geheimnisse_und_bauprodukte_aus(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            erlaubt = {"README.md", "IMPORT.json", ".gitignore", ".github/workflows/eval.yml", "gebiet/vorlage.odt", "gebiet/.gitkeep"}
            ausgeschlossen = {".git/config", ".env", "schluessel.pem", "dist/alt.zip", "__pycache__/cache.py", ".dist.staging.test/alt.zip"}
            for name in erlaubt | ausgeschlossen:
                datei = repo / name
                datei.parent.mkdir(parents=True, exist_ok=True)
                datei.write_text("Inhalt", encoding="utf-8")
            with patch.object(release_assets, "REPO", repo):
                self.assertEqual(erlaubt, {p.as_posix() for p in release_assets.gesamt_dateien()})

    def test_gesamtpaket_verweigert_symbolische_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "README.md").write_text("Inhalt", encoding="utf-8")
            (repo / "kopie.md").symlink_to(repo / "README.md")
            with patch.object(release_assets, "REPO", repo), self.assertRaisesRegex(RuntimeError, "Symbolischer Link"):
                release_assets.gesamt_dateien()

    def test_validator_blockiert_bekannte_generische_altbausteine(self) -> None:
        for bezeichnung, baustein in validate_vorlagen.VERBOTENE_GENERIK_BAUSTEINE.items():
            with self.subTest(baustein=bezeichnung):
                self.assertEqual(
                    [bezeichnung],
                    validate_vorlagen.generik_altbausteine(baustein),
                )
        self.assertEqual(
            [],
            validate_vorlagen.generik_altbausteine(
                "Die Anlage 2 enthält Chargennummer, Wareneingangsdatum und Prüfzeugnis."
            ),
        )

    def test_validator_erkennt_spezifischen_adressaten_ohne_universalrubrum(self) -> None:
        self.assertTrue(
            validate_vorlagen.hat_rubrum_oder_adressat(
                "# Antrag\n\n**Amtsgericht [Ort]**\n— Insolvenzgericht —\n"
            )
        )
        self.assertFalse(
            validate_vorlagen.hat_rubrum_oder_adressat(
                "# Antrag\n\nDer Antrag wird nach Prüfung eingereicht.\n"
            )
        )

    def test_alle_bestandsverbraucher_nutzen_dieselben_hauptvorlagen(self) -> None:
        kanonisch = {
            ordner.relative_to(REPO).as_posix()
            for ordner in vorlagenordner(REPO)
        }
        im_downloadindex = {
            ordner.relative_to(REPO).as_posix()
            for _, ordnerliste in download_index.bereiche()
            for ordner in ordnerliste
        }
        in_releasepaketen = {
            ordner.relative_to(REPO).as_posix()
            for ordner in release_assets.hauptvorlagen()
        }
        in_kategorien = kategorien_check.vorlagenziele()
        im_eval = {slug for slug, _ in run_eval.discover_vorlagen()}

        self.assertTrue(kanonisch)
        self.assertEqual(kanonisch, im_downloadindex)
        self.assertEqual(kanonisch, in_releasepaketen)
        self.assertEqual(kanonisch, in_kategorien)
        self.assertEqual(kanonisch, im_eval)

    def test_kanonische_themenliste_ist_eindeutig_und_vollstaendig(self) -> None:
        self.assertEqual(len(THEMENORDNER), len(set(THEMENORDNER)))
        vorhandene_themen = {
            ordner.parent.name
            for ordner in vorlagenordner(REPO)
        }
        self.assertEqual(set(THEMENORDNER), vorhandene_themen)

    def test_bestandsstruktur_blockiert_fehlende_und_unbekannte_themen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            for name in THEMENORDNER:
                (repo / name).mkdir()

            fehlend = repo / THEMENORDNER[-1]
            fehlend.rmdir()
            with self.assertRaisesRegex(RuntimeError, "Kanonische Themenordner fehlen"):
                pruefe_bestandsstruktur(repo)

            fehlend.mkdir()
            fremde_vorlage = repo / "neues-rechtsgebiet" / "neue-vorlage"
            fremde_vorlage.mkdir(parents=True)
            (fremde_vorlage / "neue-vorlage.md").write_text("# Neu\n", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "außerhalb der kanonischen Themenliste"):
                pruefe_bestandsstruktur(repo)

            (fremde_vorlage / "neue-vorlage.md").unlink()
            (fremde_vorlage / "vertrag.md").write_text("# Generisch benannt\n", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "außerhalb der kanonischen Themenliste"):
                pruefe_bestandsstruktur(repo)

    def test_downloadindex_verwirft_uneindeutige_vorlagenquellen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            for name in THEMENORDNER:
                (repo / name).mkdir()
            defekte_vorlage = repo / THEMENORDNER[0] / "falscher-dateistamm"
            defekte_vorlage.mkdir()
            (defekte_vorlage / "vertrag.md").write_text("# Falscher Stamm\n", encoding="utf-8")

            with (
                patch.object(download_index, "REPO", repo),
                self.assertRaisesRegex(RuntimeError, "Uneindeutige Vorlagenquelle"),
            ):
                download_index.bereiche()

    def test_bestandsscripte_pflegen_keine_eigenen_ausschlusslisten(self) -> None:
        dateien = (
            "build-download-index.py",
            "build-md-zips.py",
            "build-release-assets.py",
            "check-kategorien-index.py",
            "check-md-zip-integrity.py",
            "update-readme-md-zip-links.py",
        )
        for dateiname in dateien:
            with self.subTest(dateiname=dateiname):
                text = (SCRIPTS / dateiname).read_text(encoding="utf-8")
                self.assertNotIn("NICHT_BEREICHE", text)

    def test_offline_index_ist_eindeutig_verlinkt_und_responsiv(self) -> None:
        eintraege = release_assets.haupt_eintraege(
            release_assets.hauptvorlagen(),
            "md",
        )
        index = release_assets.offline_index("Testindex", eintraege).decode("utf-8")
        ids = re.findall(r'\bid="([^"]+)"', index)

        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(1, index.count('button { width: 100%; }'))
        self.assertIn('class="sprunglink" href="#vorlagenliste"', index)
        self.assertIn(
            'id="zuruecksetzen" type="button" aria-controls="vorlagen" disabled',
            index,
        )
        self.assertIn("window.setTimeout(filtern, 80)", index)
        self.assertIn("@media (prefers-reduced-motion: reduce)", index)
        self.assertIn("thead { display: none; }", index)
        self.assertIn("minmax(0, 1fr)", index)
        self.assertIn('aria-controls="vorlagen"', index)
        self.assertIn('<tbody id="vorlagen">', index)
        self.assertIn(f"Stand {release_assets.aktuelle_version()}", index)
        self.assertEqual(len(eintraege), index.count('data-label="Arbeitsdatei"'))
        self.assertEqual(len(eintraege), index.count('data-label="Vorlage"><a href='))

        for eintrag in eintraege:
            with self.subTest(datei=eintrag.datei):
                self.assertIn(f'href="{eintrag.datei}"', index)
                self.assertIn(f'href="{eintrag.hinweise}"', index)

    def test_offline_suche_und_manifest_tragen_fachbegriffe_und_integritaet(self) -> None:
        eintraege = release_assets.haupt_eintraege(
            release_assets.hauptvorlagen(),
            "md",
        )
        unfall = next(
            eintrag for eintrag in eintraege
            if eintrag.datei.endswith("anspruchsschreiben-unfallversicherung.md")
        )
        self.assertIn("mitwirkende", unfall.suchbegriffe)
        self.assertGreater(unfall.dateigroesse_bytes, 0)
        self.assertRegex(unfall.sha256, r"^[0-9a-f]{64}$")

        daten = json.loads(release_assets.manifest("Test", [unfall]))
        self.assertEqual(2, daten["schema_version"])
        self.assertEqual(release_assets.aktuelle_version(), daten["version"])
        self.assertEqual(unfall.sha256, daten["eintraege"][0]["sha256"])

    def test_sonderindex_unterscheidet_gericht_und_staatsanwaltschaft(self) -> None:
        eintraege = release_assets.sonder_eintraege()
        typen = {
            eintrag.dokumenttyp
            for eintrag in eintraege
        }
        self.assertEqual(
            {"Gerichtsleitend", "Staatsanwaltschaftlich", "Amtsanwaltschaftlich"},
            typen,
        )
        self.assertGreater(
            len({eintrag.suchbegriffe for eintrag in eintraege}),
            len(eintraege) // 2,
        )

    def test_releasepakete_enthalten_arbeits_und_pruefdokumentation(self) -> None:
        navigation = {
            pfad.relative_to(REPO).as_posix()
            for pfad in release_assets.navigationsdateien()
        }
        erwartete_wurzeldokumente = {
            pfad.name
            for pfad in REPO.glob("*.md")
        }
        erwartete_referenzen = {
            pfad.relative_to(REPO).as_posix()
            for pfad in (REPO / "references").glob("*.md")
        }
        self.assertTrue(erwartete_wurzeldokumente <= navigation)
        self.assertTrue(erwartete_referenzen <= navigation)
        self.assertIn("vorlagen-gerichtsleitend/INDEX.md", navigation)

    def test_releasepakete_verfolgen_keine_symbolischen_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            basis = Path(tmp)
            repo = basis / "repo"
            repo.mkdir()
            ausserhalb = basis / "geheim.txt"
            ausserhalb.write_text("vertraulich", encoding="utf-8")
            link = repo / "verknuepfung.txt"
            try:
                link.symlink_to(ausserhalb)
            except OSError:
                self.skipTest("Symbolische Links werden auf diesem System nicht unterstützt")

            with patch.object(release_assets, "REPO", repo):
                with self.assertRaisesRegex(RuntimeError, "Symbolischer Link"):
                    release_assets.relative({link})

    def test_releasepakete_ersetzen_vorhandene_dateien_atomar(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            with patch.object(release_assets, "REPO", repo):
                quelle = repo / "quelle.txt"
                quelle.write_text("vollständig", encoding="utf-8")
                ziel = repo / "paket.zip"
                ziel.write_bytes(b"letzte gute Fassung")
                with self.assertRaises(FileNotFoundError):
                    release_assets.zip_schreiben(
                        ziel,
                        [Path("quelle.txt"), Path("fehlt.txt")],
                    )
                self.assertEqual(b"letzte gute Fassung", ziel.read_bytes())
                self.assertEqual([], list(repo.glob(".paket.zip.*.tmp")))

    def test_releasepakete_verwerfen_doppelte_und_unsichere_archivnamen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            quelle = repo / "index.html"
            quelle.write_text("Quelle", encoding="utf-8")
            ziel = repo / "paket.zip"
            ziel.write_bytes(b"letzte gute Fassung")
            with patch.object(release_assets, "REPO", repo):
                with self.assertRaisesRegex(RuntimeError, "kollidierender Pfad"):
                    release_assets.zip_schreiben(
                        ziel,
                        [Path("index.html")],
                        {"INDEX.HTML": b"Zusatz"},
                    )
                with self.assertRaisesRegex(RuntimeError, "Unsicherer Pfad"):
                    release_assets.zip_schreiben(
                        ziel,
                        [Path("index.html")],
                        {"../manifest.json": b"{}"},
                    )
                for name in ("unterordner//manifest.json", "C:/manifest.json", "manifest?.json"):
                    with (
                        self.subTest(name=name),
                        self.assertRaisesRegex(RuntimeError, "Unsicherer Pfad"),
                    ):
                        release_assets.zip_schreiben(
                            ziel,
                            [Path("index.html")],
                            {name: b"{}"},
                        )
            self.assertEqual(b"letzte gute Fassung", ziel.read_bytes())
            self.assertEqual([], list(repo.glob(".paket.zip.*.tmp")))

    def test_releaseartefakte_erhalten_portable_leserechte(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            quelle = repo / "quelle.txt"
            quelle.write_text("vollständig", encoding="utf-8")
            paket = repo / "paket.zip"
            summen = repo / "SHA256SUMS.txt"
            with patch.object(release_assets, "REPO", repo):
                release_assets.zip_schreiben(paket, [Path("quelle.txt")])
                release_assets.text_atomar_schreiben(
                    summen,
                    "abc  paket.zip\n",
                    encoding="ascii",
                )
            self.assertEqual(0o644, stat.S_IMODE(paket.stat().st_mode))
            self.assertEqual(0o644, stat.S_IMODE(summen.stat().st_mode))

    def test_atomare_schreibpruefung_bewahrt_die_letzte_gute_datei(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ziel = Path(tmp) / "bestand.bin"
            ziel.write_bytes(b"letzte gute Fassung")

            def ablehnen(_: Path) -> None:
                raise RuntimeError("simulierter Prüffehler")

            with self.assertRaisesRegex(RuntimeError, "Prüffehler"):
                bytes_atomar_schreiben(
                    ziel,
                    "unvollständig".encode("utf-8"),
                    pruefen=ablehnen,
                )
            self.assertEqual(b"letzte gute Fassung", ziel.read_bytes())
            self.assertEqual([], list(Path(tmp).glob(".bestand.bin.*.tmp")))

    def test_releasebau_veroeffentlicht_erst_nach_vollstaendigem_staging(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ausgabe = Path(tmp) / "dist"
            ausgabe.mkdir()
            alt = {name: f"alt:{name}".encode() for name in release_assets.RELEASE_DATEIEN}
            for name, inhalt in alt.items():
                (ausgabe / name).write_bytes(inhalt)

            def abbrechen(staging: Path) -> int:
                (staging / release_assets.RELEASE_DATEIEN[0]).write_bytes(b"neu")
                raise RuntimeError("simulierter Paketfehler")

            with (
                patch.object(release_assets, "paketset_bauen", side_effect=abbrechen),
                self.assertRaisesRegex(RuntimeError, "Paketfehler"),
            ):
                release_assets.release_bauen(ausgabe)
            for name, inhalt in alt.items():
                self.assertEqual(inhalt, (ausgabe / name).read_bytes())
            self.assertEqual([], list(Path(tmp).glob(".dist.staging.*")))

    def test_releasebau_veroeffentlicht_ein_vollstaendiges_paketset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ausgabe = Path(tmp) / "dist"

            def erfolgreich(staging: Path) -> int:
                for name in release_assets.RELEASE_DATEIEN:
                    (staging / name).write_bytes(f"neu:{name}".encode())
                return 981

            with patch.object(release_assets, "paketset_bauen", side_effect=erfolgreich):
                self.assertEqual(981, release_assets.release_bauen(ausgabe))
            for name in release_assets.RELEASE_DATEIEN:
                self.assertEqual(f"neu:{name}".encode(), (ausgabe / name).read_bytes())

    def test_relative_markdown_links_duerfen_das_repo_nicht_verlassen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            basis = Path(tmp)
            repo = basis / "repo"
            ordner = repo / "bereich"
            ordner.mkdir(parents=True)
            geheim = basis / "geheim.txt"
            geheim.write_text("vertraulich", encoding="utf-8")
            (ordner / "README.md").write_text(
                "[falsches lokales Ziel](../../geheim.txt)\n",
                encoding="utf-8",
            )
            with patch.object(validate_vorlagen, "REPO", repo):
                fehler = validate_vorlagen.relative_linkfehler()
            self.assertEqual(1, len(fehler))
            self.assertIn("verlässt das Repository", fehler[0])

    def test_relative_markdown_links_pruefen_fragmente_und_schreibweise(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            quelle = repo / "Bereich"
            quelle.mkdir()
            (repo / "Ziel.md").write_text("# Titel\n\n## Abschnitt Eins\n", encoding="utf-8")
            (repo / "Ziel Datei.md").write_text("# Dateititel\n", encoding="utf-8")
            (quelle / "Quelle.md").write_text(
                "[Repo-Wurzel](..)\n"
                "[gültig](../Ziel.md#abschnitt-eins)\n"
                "[Ziel mit Leerzeichen](<../Ziel Datei.md> \"Titel\")\n"
                "[falscher Anker](../Ziel.md#nicht-vorhanden)\n"
                "[falsche Schreibweise](../ziel.md)\n",
                encoding="utf-8",
            )
            with patch.object(validate_vorlagen, "REPO", repo):
                fehler = validate_vorlagen.relative_linkfehler()
            self.assertEqual(2, len(fehler))
            self.assertTrue(any("Markdown-Anker fehlt" in fehlertext for fehlertext in fehler))
            self.assertTrue(any("Groß-/Kleinschreibung" in fehlertext for fehlertext in fehler))


if __name__ == "__main__":
    unittest.main()
