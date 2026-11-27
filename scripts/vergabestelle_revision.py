"""Rekonstruiert die acht Arbeitswege und die zugehörige Registry vor Ausgabe 445.36.17."""
from functools import lru_cache
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

PLUGIN = "vergabestelle-behoerden"
SOURCE = "vergaberecht-werkstatt/" + PLUGIN
MEGAPROMPT = f"vergaberecht-werkstatt/testakten/megaprompts/{PLUGIN}.md"
REGISTRY = "scripts/data/skill-cap-registry.json"
EVIDENCE = Path("quality/vergaberecht-werkstatt/445.36.17")
PUBLISHED = "scripts/data/qualitaetsrunde-v445.36.17-scope.json"
SKILLS = frozenset(f"{SOURCE}/skills/{slug}/SKILL.md" for slug in (
    "vergabe-os-master-orchestrator", "vergabeart-und-schwelle-bearbeiten", "vergabeunterlagen-bearbeiten",
    "ruege-bearbeiten", "nachpruefung-bearbeiten", "arbeitsprodukt-bearbeiten",
    "unterlagen-und-quellen-auswerten-bearbeiten", "arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten",
))
PROOF_SHA256 = "ddd9077bf3e3d8fbce2ab1e11fbaa4139d7820bdecccaa37a778350b896feeed"


@lru_cache(maxsize=2)
def proof(raw):
    if sha256(raw).hexdigest() != PROOF_SHA256:
        raise ValueError("Prüfnachweis für die Arbeitswege der Vergabestelle verändert")
    return json.loads(raw)


def previous(root, name, data, *, plugin=None):
    if name not in SKILLS and name not in (REGISTRY, MEGAPROMPT):
        return data
    if not (root / PUBLISHED).is_file() and not (root / EVIDENCE).exists():
        return data
    if name != REGISTRY and plugin not in {None, PLUGIN}:
        raise ValueError(f"{name}: Nachweis gehört zur Vergabestelle")
    directory = root / EVIDENCE
    record = proof((directory / "bestand.json").read_bytes())
    row = record["dateien"][name]
    if sha256(data).hexdigest() != row["nachher"]:
        raise ValueError(f"{name}: Inhalt weicht von der geprüften Fortschreibung ab")
    archive = (directory / "vorfassungen.zip").read_bytes()
    if sha256(archive).hexdigest() != record["archiv_sha256"]:
        raise ValueError("Archiv der Vergabestellen-Vorfassungen verändert")
    with ZipFile(BytesIO(archive)) as source:
        if name == REGISTRY:
            registry = json.loads(data)
            positions = [i for i, entry in enumerate(registry["plugins"]) if entry.get("name") == PLUGIN]
            if len(positions) != 1:
                raise ValueError("Vergabestellen-Eintrag der Registry nicht eindeutig")
            registry["plugins"][positions[0]] = json.loads(source.read("vergabestelle-registry.json"))
            original = (json.dumps(registry, ensure_ascii=False, indent=2) + "\n").encode()
        else:
            original = source.read(name.removeprefix(SOURCE + "/"))
    if sha256(original).hexdigest() != row["vorher"]:
        raise ValueError(f"{name}: Vorfassung nicht bytegleich rekonstruierbar")
    return original
