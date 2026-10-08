from __future__ import annotations

import io
import importlib.util
import stat
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
spec = importlib.util.spec_from_file_location(
    "md_to_odt_layout_test",
    SCRIPTS / "md-to-odt.py",
)
if spec is None or spec.loader is None:
    raise RuntimeError("md-to-odt.py konnte nicht geladen werden")
md_to_odt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md_to_odt)


def tabelle(spalten: int, zeilen: int) -> str:
    return "\n".join(
        "|" + "|".join(f"Zelle {nummer}" for nummer in range(spalten)) + "|"
        for _ in range(zeilen)
    )


class OdtLayoutTest(unittest.TestCase):
    def test_sehr_breite_kurze_tabellen_erhalten_querformat(self) -> None:
        self.assertTrue(md_to_odt.needs_landscape_layout(tabelle(9, 3)))
        self.assertTrue(md_to_odt.needs_landscape_layout(tabelle(8, 4)))
        self.assertTrue(md_to_odt.needs_landscape_layout(tabelle(7, 6)))

    def test_kompakte_tabellen_bleiben_im_hochformat(self) -> None:
        self.assertFalse(md_to_odt.needs_landscape_layout(tabelle(9, 2)))
        self.assertFalse(md_to_odt.needs_landscape_layout(tabelle(8, 3)))
        self.assertFalse(md_to_odt.needs_landscape_layout(tabelle(7, 5)))

    def test_maskierte_zelltrenner_zaehlen_nicht_als_spalten(self) -> None:
        zweispaltig = "\n".join([
            "| Deutsch | English |",
            "|---|---|",
            *[
                "| Risiko \\| Kontrolle \\| Folge | Risk \\| Control \\| Consequence |"
                for _ in range(8)
            ],
        ])
        self.assertFalse(md_to_odt.needs_landscape_layout(zweispaltig))

    def test_erstseitenhinweis_ist_zweisprachig_einmalig_und_idempotent(self) -> None:
        styles = (
            '<office:document-styles>'
            '<office:styles>'
            '<style:style style:family="paragraph" style:name="Footer" />'
            '</office:styles>'
            '<office:master-styles>'
            '<style:master-page style:name="Standard" style:page-layout-name="Mpm1">'
            '<style:footer><text:p text:style-name="MP1">'
            '<text:page-number text:select-page="current">1</text:page-number>'
            '</text:p></style:footer>'
            '</style:master-page>'
            '</office:master-styles>'
            '</office:document-styles>'
        )

        einmal = md_to_odt.ensure_first_page_ai_notice(styles)
        zweimal = md_to_odt.ensure_first_page_ai_notice(einmal)

        self.assertEqual(einmal, zweimal)
        self.assertEqual(1, einmal.count("<style:footer-first>"))
        self.assertEqual(1, einmal.count(md_to_odt.FIRST_PAGE_NOTICE_DE))
        self.assertEqual(1, einmal.count(md_to_odt.FIRST_PAGE_NOTICE_EN))
        self.assertIn(
            f'style:name="{md_to_odt.FIRST_PAGE_NOTICE_STYLE}"',
            einmal,
        )
        self.assertIn("· Seite / Page ", einmal)

    def test_fehlgeschlagener_export_bewahrt_die_letzte_gute_odt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ordner = Path(tmp)
            markdown = ordner / "muster.md"
            odt = ordner / "muster.odt"
            markdown.write_text("# Muster\n\nText.\n", encoding="utf-8")
            odt.write_bytes(b"letzte gute Fassung")

            def pandoc_simulieren(befehl, *, check, cwd):
                self.assertTrue(check)
                self.assertEqual(ordner.resolve(), cwd)
                self.assertEqual(str(ordner.resolve()), befehl[befehl.index("--resource-path") + 1])
                ausgabe = Path(befehl[befehl.index("-o") + 1])
                ausgabe.write_bytes(b"noch nicht normalisierter Export")

            with (
                patch.object(md_to_odt.subprocess, "run", side_effect=pandoc_simulieren),
                patch.object(
                    md_to_odt,
                    "normalize_odt_layout",
                    side_effect=RuntimeError("Layoutfehler"),
                ),
                self.assertRaisesRegex(RuntimeError, "Layoutfehler"),
            ):
                md_to_odt.md_to_odt(markdown)

            self.assertEqual(b"letzte gute Fassung", odt.read_bytes())
            self.assertEqual([], list(ordner.glob(".muster.*.odt")))

    def test_erfolgreicher_export_erhaelt_portable_leserechte(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ordner = Path(tmp)
            markdown = ordner / "muster.md"
            markdown.write_text("# Muster\n\nText.\n", encoding="utf-8")

            def pandoc_simulieren(befehl, *, check, cwd):
                self.assertTrue(check)
                self.assertEqual(ordner.resolve(), cwd)
                self.assertEqual(str(ordner.resolve()), befehl[befehl.index("--resource-path") + 1])
                ausgabe = Path(befehl[befehl.index("-o") + 1])
                ausgabe.write_bytes("gültiger simulierter Export".encode("utf-8"))

            with (
                patch.object(md_to_odt.subprocess, "run", side_effect=pandoc_simulieren),
                patch.object(md_to_odt, "normalize_odt_layout"),
                patch.object(md_to_odt, "pruefe_generiertes_odt"),
            ):
                odt = md_to_odt.md_to_odt(markdown)

            self.assertEqual(
                "gültiger simulierter Export".encode("utf-8"),
                odt.read_bytes(),
            )
            self.assertEqual(0o644, stat.S_IMODE(odt.stat().st_mode))

    def test_ungueltiger_eingabepfad_ist_ein_fehler(self) -> None:
        with (
            patch.object(md_to_odt.shutil, "which", return_value="/usr/bin/pandoc"),
            redirect_stderr(io.StringIO()),
        ):
            self.assertEqual(1, md_to_odt.main(["md-to-odt.py", "fehlt.md"]))


if __name__ == "__main__":
    unittest.main()
