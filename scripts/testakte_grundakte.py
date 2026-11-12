"""Geprüfte Auswahl der Eingangsunterlagen für native Testakten-ZIPs."""

from email import policy
from email.parser import BytesParser
from functools import lru_cache
import json
from pathlib import Path, PurePosixPath
import re


FOLDER = "Grundakte"
CONFIG = Path(__file__).resolve().parent / "data/testakten-grundakten.json"
ADDITIONAL_CONFIGS = (
    CONFIG.with_name("testakten-grundakten-eingangsbestand.json"),
    CONFIG.with_name("testakten-grundakten-hameln.json"),
    CONFIG.with_name("testakten-grundakten-ergaenzung.json"),
)
PROCEEDING = re.compile(
    r"widerspruch|einspruch|klageschrift|klageerwiderung|klage.entwurf|"
    r"gerichtlich|klageverfahren|(?:^|[-_])klage(?:[-_.]|$)|urteils?|mahnbescheid|erwiderung|"
    r"berufungsbegruendung|nachbesprechung|musterl(?:oe|ö)sung|"
    r"gesamt[-_]?pdf|(?:[-_]gesamt|gesamtakte)\.pdf$",
    re.IGNORECASE,
)


@lru_cache
def base_selection():
    return json.loads(CONFIG.read_text(encoding="utf-8"))


@lru_cache
def selection():
    selections = {**base_selection(), "central": dict(base_selection()["central"])}
    for path in ADDITIONAL_CONFIGS:
        if not path.is_file():
            continue
        cases = json.loads(path.read_text(encoding="utf-8"))
        overlap = selections["central"].keys() & cases.keys()
        if overlap:
            raise ValueError(f"Doppelte Grundaktenauswahl in {path.name}: {sorted(overlap)}")
        selections["central"].update(cases)
    return selections


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
