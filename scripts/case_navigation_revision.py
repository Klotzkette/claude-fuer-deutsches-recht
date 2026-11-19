"""Rekonstruiert die vier vor #696 geprüften Aktenseiten aus ihren rein additiven Downloadhinweisen."""
from hashlib import sha256
import json
from pathlib import Path

from testakte_disclaimer import NOTICE_MARKDOWN

EVIDENCE = "quality/paketnavigation-2026-11-19/testakten-verweise.json"
CASES = {
    "arbeitszeugnispruefer/testakte/arbeitszeugnis-analyse-bluehendes-leben/README.md",
    "bautraegervertragspruefer/testakte/README.md",
    "bautraegervertragspruefer/testakte/bautraegervertrag/README.md",
    "bautraegervertragspruefer/testakte/bautraegervertrag-marewald/README.md",
}


def previous_case_readme(root, relative, current):
    if relative not in CASES:
        return None
    evidence = json.loads((Path(root) / EVIDENCE).read_text(encoding="utf-8"))
    if set(evidence) != CASES:
        raise ValueError("Nachweis der vier Aktenseiten unvollständig")
    record = evidence[relative]
    if sha256(current).hexdigest() != record["after_sha256"]:
        raise ValueError(f"{relative}: Aktenseite seit der belegten Ergänzung verändert")
    slug = relative.split("/", 1)[0]
    title = "## Vollakte mit Originalbelegen und Nachreichungen"
    url = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/testakten-praxis-v1.0.0/{slug}-mit-nachtrag.zip"
    link = f"[Vollakte mit Nachträgen herunterladen (ZIP)]({url})"
    previous = bytearray()
    offset = 0
    sections = 0
    for addition in record["insertions"]:
        start = addition["offset"]
        end = start + addition["length"]
        if not offset <= start < end <= len(current):
            raise ValueError(f"{relative}: ungültige oder überlappende Einfügung")
        block = current[start:end]
        if sha256(block).hexdigest() != addition["sha256"]:
            raise ValueError(f"{relative}: abweichender Ergänzungsblock")
        paragraphs = block.decode("utf-8").strip().split("\n\n")
        if paragraphs != [NOTICE_MARKDOWN]:
            if (len(paragraphs) != 4 or paragraphs[0] != title
                    or not paragraphs[1] or "\n" in paragraphs[1] or "](" in paragraphs[1]
                    or paragraphs[2:] != [NOTICE_MARKDOWN, link]):
                raise ValueError(f"{relative}: Ergänzung ist kein geprüfter Downloadhinweis")
            sections += 1
        previous.extend(current[offset:start])
        offset = end
    previous.extend(current[offset:])
    if sections != 1 or sha256(previous).hexdigest() != record["before_sha256"]:
        raise ValueError(f"{relative}: Vorfassung nicht bytegleich rekonstruiert")
    return bytes(previous)
