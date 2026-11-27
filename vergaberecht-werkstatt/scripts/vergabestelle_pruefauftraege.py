#!/usr/bin/env python3
"""Baut die einzeln abrufbaren Prüfaufträge mit dem damaligen Aktenstand."""

import argparse
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from email.utils import format_datetime
import json
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "testakten"
MAIL_PATH = Path("eml/00_pruefauftrag_vergabestelle.eml")
MIME = {
    ".docx": ("application", "vnd.openxmlformats-officedocument.wordprocessingml.document"),
    ".xlsx": ("application", "vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
    ".xml": ("application", "xml"),
    # Als native Datei anhängen. Eine erneute Serialisierung einer eingebetteten
    # Nachricht kann den Originalbeleg durch neue Zeilenumbrüche verändern.
    ".eml": ("application", "octet-stream"),
}


def read_cases():
    path = Path(__file__).with_name("pruefauftraege-vergabestelle.json")
    return json.loads(path.read_text(encoding="utf-8"))


def render(case_dir, data):
    sent = datetime.fromisoformat(data["zeit"]).replace(tzinfo=ZoneInfo("Europe/Berlin"))
    mail = EmailMessage(policy=policy.SMTP.clone(max_line_length=76))
    mail["From"] = data["von"]
    mail["To"] = data["an"]
    mail["Date"] = format_datetime(sent)
    mail["Subject"] = data["betreff"]
    mail["Message-ID"] = f"<{case_dir.name}.{sent:%Y%m%dT%H%M}@beschaffung.example>"
    mail.set_content("\n\n".join(data["text"]), charset="utf-8", cte="quoted-printable")
    files = data["anlagen"]
    if not 1 <= len(files) <= 3 or len(set(files)) != len(files):
        raise ValueError(f"{case_dir.name}: ein bis drei unterschiedliche Originalanlagen erforderlich")
    for name in files:
        path = (case_dir / name).resolve()
        if not path.is_relative_to(case_dir.resolve()) or path == (case_dir / MAIL_PATH).resolve():
            raise ValueError(f"{case_dir.name}: ungültige Anlage {name}")
        payload = path.read_bytes()
        if path.suffix == ".eml":
            original = BytesParser(policy=policy.default).parsebytes(payload, headersonly=True)
            if original["Date"].datetime > sent:
                raise ValueError(f"{case_dir.name}: {name} war bei Versand noch nicht eingegangen")
        main, sub = MIME[path.suffix]
        mail.add_attachment(payload, maintype=main, subtype=sub, filename=path.name)
    # Im Repository und bei erneutem Build identische MIME-Grenzen erzeugen.
    mail.set_boundary(f"=_Vergabestelle_{case_dir.name.split('-')[0]}_{sent:%Y%m%d%H%M}")
    return mail.as_bytes()


def write_request(case_dir, data):
    target = case_dir / MAIL_PATH
    data_bytes = render(case_dir, data)
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(data_bytes)


def validate_request(case_dir, data):
    target = case_dir / MAIL_PATH
    blob = target.read_bytes()
    if blob != render(case_dir, data):
        raise ValueError(f"{target}: Prüfauftrag oder Anlagen weichen von den Quellen ab")
    parsed = BytesParser(policy=policy.default).parsebytes(blob)
    for part, name in zip(parsed.iter_attachments(), data["anlagen"], strict=True):
        file = case_dir / name
        if part.get_filename() != file.name or part.get_payload(decode=True) != file.read_bytes():
            raise ValueError(f"{target}: MIME-Anlage {name} ist nicht originalgetreu")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Inhalt und native Anhänge prüfen")
    args = parser.parse_args()
    cases = read_cases()
    for slug, data in cases.items():
        if not args.check:
            write_request(CASES / slug, data)
        validate_request(CASES / slug, data)
    print(f"{len(cases)} Prüfaufträge mit Originalanhängen geprüft.")
