"""Geprüfte Auswahl der Eingangsunterlagen für native Testakten-ZIPs."""

from email import policy
from email.parser import BytesParser
from functools import lru_cache
import json
from pathlib import Path, PurePosixPath
import re


FOLDER = "Grundakte"
CONFIG = Path(__file__).resolve().parent / "data/testakten-grundakten.json"
PROCEEDING = re.compile(
    r"widerspruch|einspruch|klageschrift|klageerwiderung|klage.entwurf|"
    r"gerichtlich|klageverfahren|(?:^|[-_])klage(?:[-_.]|$)|urteils?|mahnbescheid|erwiderung|"
    r"berufungsbegruendung|nachbesprechung|musterl(?:oe|ö)sung|"
    r"gesamt[-_]?pdf|(?:[-_]gesamt|gesamtakte)\.pdf$",
    re.IGNORECASE,
)


@lru_cache
def selection():
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def check_intake_member(name, data=None):
    """Fängt falsch eingeordnete Verfahrensstücke und ihre Mailanhänge ab."""
    path = PurePosixPath(name)
    if PROCEEDING.search(path.name) or path.suffix.lower() in {".zip", ".md"}:
        raise ValueError(f"Verfahrens- oder Redaktionsstück in der Grundakte: {name}")
    if path.suffix.lower() == ".eml" and data is not None:
        message = BytesParser(policy=policy.default).parsebytes(data)
        for part in message.iter_attachments():
            filename = part.get_filename()
            if filename:
                check_intake_member(filename, part.get_payload(decode=True))
