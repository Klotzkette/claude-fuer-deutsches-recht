#!/usr/bin/env python3
"""Regressionstests für portable EML-Aktenstücke."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, A4, A5


SCRIPT = Path(__file__).resolve().parent / "validate-testakten-dokumentqualitaet.py"
SPEC = importlib.util.spec_from_file_location("testakten_dokumentqualitaet", SCRIPT)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="eml-qualitaet-") as tmp:
        root = Path(tmp)
        valid = root / "valid.eml"
        valid.write_text(
            "From: kanzlei@falkenried-recht.de\n"
            "To: mandant@postfach.de\n"
            "Date: Fri, 24 Jul 2026 10:15:00 +0200\n"
            "Subject: Rückfrage zur Übergabe\n"
            "Message-ID: <20260724101500@falkenried-recht.de>\n"
            "MIME-Version: 1.0\n"
            'Content-Type: text/plain; charset="utf-8"\n'
            "Content-Transfer-Encoding: 8bit\n\n"
            "Sehr geehrter Herr Müller,\n\n"
            "zum Vorgang FR-184/26 benötige ich noch die vollständige "
            "Übergabebestätigung vom 22. Juli 2026. Bitte übersenden Sie außerdem "
            "die zwei bei der Übergabe aufgenommenen Fotografien und teilen Sie "
            "mir mit, ob Frau Klein als Zeugin anwesend war. Die Unterlagen werden "
            "für den Schriftsatz benötigt, dessen Frist am 3. August 2026 endet.\n\n"
            "Mit freundlichen Grüßen\n"
            "Rechtsanwältin Anna Falkenried\n",
            encoding="utf-8",
        )
        require(not V.eml_quality_errors(valid), "valide UTF-8-E-Mail muss bestehen")

        too_short = root / "too-short.eml"
        too_short.write_text(
            valid.read_text(encoding="utf-8").replace(
                "zum Vorgang FR-184/26 benötige ich noch die vollständige "
                "Übergabebestätigung vom 22. Juli 2026. Bitte übersenden Sie außerdem "
                "die zwei bei der Übergabe aufgenommenen Fotografien und teilen Sie "
                "mir mit, ob Frau Klein als Zeugin anwesend war. Die Unterlagen werden "
                "für den Schriftsatz benötigt, dessen Frist am 3. August 2026 endet.\n\n"
                "Mit freundlichen Grüßen\n"
                "Rechtsanwältin Anna Falkenried\n",
                "Bitte senden Sie die Übergabebestätigung.\n",
            ),
            encoding="utf-8",
        )
        require(
            any("zu knapp" in error for error in V.eml_quality_errors(too_short)),
            "zu kurze E-Mail muss auffallen",
        )

        missing_charset = root / "missing-charset.eml"
        missing_charset.write_text(
            "From: kanzlei@falkenried-recht.de\n"
            "To: mandant@postfach.de\n"
            "Date: Fri, 24 Jul 2026 10:15:00 +0200\n"
            "Subject: Rückfrage\n"
            "Message-ID: <20260724101501@falkenried-recht.de>\n\n"
            "Grüße aus Köln\n",
            encoding="utf-8",
        )
        errors = V.eml_quality_errors(missing_charset)
        require(
            any("MIME-Version" in error for error in errors)
            and any("UTF-8-Zeichensatz" in error for error in errors),
            "fehlende MIME- und Zeichensatzangaben müssen auffallen",
        )

        for domain in ("beispielkanzlei.local", "aktenpost.example"):
            synthetic = root / f"synthetic-{domain.rsplit('.', 1)[-1]}.eml"
            synthetic.write_text(
                valid.read_text(encoding="utf-8").replace(
                    "falkenried-recht.de", domain
                ),
                encoding="utf-8",
            )
            require(
                any(
                    "künstliche E-Mail-Domain" in error
                    for error in V.eml_quality_errors(synthetic)
                ),
                f"künstliche Domain {domain} muss auffallen",
            )

        synthetic_url = root / "synthetic-url.eml"
        synthetic_url.write_text(
            valid.read_text(encoding="utf-8")
            + "\nUnterlagen: https://aktenraum.example/download\n",
            encoding="utf-8",
        )
        require(
            any(
                "künstliche E-Mail-Domain" in error
                for error in V.eml_quality_errors(synthetic_url)
            ),
            "künstliche URL-Domain muss auffallen",
        )

        bare_domain = root / "bare-domain.eml"
        bare_domain.write_text(
            valid.read_text(encoding="utf-8")
            + "\nMandantenportal: aktenraum.example/download\n",
            encoding="utf-8",
        )
        require(
            any(
                "künstliche E-Mail-Domain" in error
                for error in V.eml_quality_errors(bare_domain)
            ),
            "bloße Example-Domain muss auffallen",
        )

        reserved_label = root / "reserved-label.eml"
        reserved_label.write_text(
            valid.read_text(encoding="utf-8").replace(
                "kanzlei@falkenried-recht.de", "kanzlei@example.de"
            ),
            encoding="utf-8",
        )
        require(
            any(
                "künstliche E-Mail-Domain" in error
                for error in V.eml_quality_errors(reserved_label)
            ),
            "offensichtliche Example-Adresse muss auffallen",
        )

        case = root / "akten" / "bauvorhaben"
        case.mkdir(parents=True)
        contact = case / "rueckfrage.eml"
        contact.write_text(valid.read_text(encoding="utf-8").replace(
            "falkenried-recht.de", "planungsbuero.example"), encoding="utf-8")
        readme = case / "README.md"
        with patch.object(V, "TESTAKTEN", case.parent):
            require(bool(V.eml_quality_errors(contact)), "ohne Herkunftsnachweis bleibt die Domain gesperrt")
            readme.write_text(V.RESERVED_CONTACT_MARKER, encoding="utf-8")
            require(bool(V.eml_quality_errors(contact)), "Marker allein genügt nicht")
            readme.write_text("\n".join((V.RESERVED_CONTACT_MARKER, V.NOTICE_DE, V.NOTICE_EN)), encoding="utf-8")
            require(not V.eml_quality_errors(contact), "deklarierte reservierte Kontakte müssen bestehen")
            for domain in ("example.de", "planungsbuero.local", "buero.example.de"):
                require(V.has_unexplained_synthetic_contact("an info@" + domain, contact), "keine pauschale Domain-Freigabe")
            require(not V.has_unexplained_synthetic_contact("https://portal.planung.example/akten", contact), "echte reservierte Subdomain")
            contact.write_text(contact.read_text(encoding="utf-8").replace("MIME-Version: 1.0\n", ""), encoding="utf-8")
            require(any("MIME-Version" in error for error in V.eml_quality_errors(contact)), "Herkunftsmarker darf MIME-Prüfung nicht abschalten")

        for name, size, subject, draw, text_count, expected in (
            ("plan", A3, "Technische Bauzeichnung", True, 12, True),
            ("plan-a4", A4, "Technische Bauzeichnung", True, 12, True),
            ("brief", A3, "Brief", True, 12, False),
            ("falsch-deklariert", A3, "Technische Bauzeichnung", False, 12, False),
            ("unbeschriftet", A3, "Technische Bauzeichnung", True, 0, False),
            ("falsches-format", A5, "Technische Bauzeichnung", True, 12, False),
        ):
            pdf = root / (name + ".pdf")
            document = canvas.Canvas(str(pdf), pagesize=size)
            document.setSubject(subject)
            if draw:
                for index in range(25):
                    document.rect(25 + index * 5, 40 + index * 5, 100, 100)
            for index in range(text_count):
                document.drawString(25, 200 + index * 12, f"Achse {index}: lichte Breite 2400 mm, Planstand 12.09.2026")
            document.showPage()
            document.save()
            require(V.is_technical_drawing(pdf) == expected, f"Zeichnungsprüfung: {name}")

    english = "The gross salary includes no compensation for gross negligence."
    path = Path("employment.docx")
    require(not V.language_prose_errors(english, path, "en-GB"), "englische Fachbegriffe sind keine deutschen Umlautfehler")
    require(bool(V.language_prose_errors(english, path)), "ohne Sprachangabe bleibt die deutsche Prüfung aktiv")
    require(bool(V.language_prose_errors("Die Fläche ist gross.", path, "de-DE")), "deutsches gross bleibt ein Fehler")
    require(bool(V.language_prose_errors("Die Fläche ist gross.", path, "en,de")), "mehrdeutige Sprachangabe darf die Prüfung nicht abschalten")
    require(bool(V.language_prose_errors("Die Fläche ist gross.", path, "en-GB,de")), "auch eine regionale Sprachliste ist keine eindeutige englische Deklaration")
    require(bool(V.language_prose_errors("Please confirm die Verguetung.", path, "en")), "englische Metadaten dürfen andere deutsche Umlautfehler nicht verbergen")
    require(not V.language_prose_errors("Die Vergütung ist vollständig.", path, "de"), "korrekte deutsche Umlaute bleiben zulässig")
    for reference in ("kontoauszuege/Haushalt_2025-04.pdf", r"kontoauszuege\Haushalt_2025-04.pdf"):
        require(not V.language_prose_errors("Beleg für die Zahlung: " + reference, path), "technische Belegpfade sind keine Prosa")
        require(bool(V.language_prose_errors("Die auszuege fehlen;" + reference, path)), "Dateipfade dürfen fehlerhafte CSV-Prosa nicht verdecken")
    print("test-testakten-email-quality OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
