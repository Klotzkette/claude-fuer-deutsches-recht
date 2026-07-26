#!/usr/bin/env python3
"""Regressionstests für portable EML-Aktenstücke."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path


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
            "bitte übersenden Sie die vollständige Übergabebestätigung.\n",
            encoding="utf-8",
        )
        require(not V.eml_quality_errors(valid), "valide UTF-8-E-Mail muss bestehen")

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

    print("test-testakten-email-quality OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
