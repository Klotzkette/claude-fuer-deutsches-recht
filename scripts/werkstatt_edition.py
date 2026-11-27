"""Frühere Werkstatttexte und zugehörige Quellennachweise bytegenau rekonstruieren."""
import gzip
import hashlib
import json
from functools import lru_cache
from pathlib import Path

PIN = json.loads((Path(__file__).parent / "data/werkstatt-vorfassungen-20261127.json").read_bytes())
PROOF = Path(PIN["path"])
PROOF_SHA256 = PIN["sha256"]


def digest(content):
    return hashlib.sha256(content).hexdigest()


def is_workshop(name):
    path = Path(name)
    return (path.name in ("werkstatt.md", "werkstatt.txt")
            or path.name.endswith(("-werkstatt.md", "-werkstatt.txt"))
            or (path.parent.name == "werkstattprompts" and path.suffix in (".md", ".txt")
                and path.name != "README.md"))


@lru_cache(maxsize=4)
def _load(path, size, mtime, ctime):
    data = gzip.decompress(path.read_bytes())
    if digest(data) != PROOF_SHA256:
        raise ValueError("Prüfbeleg der Werkstatttexte verändert")
    return json.loads(data)


def proof(root):
    path = root / PROOF
    if not path.exists() and not path.parent.exists():
        return {}
    stat = path.stat()
    return _load(path, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)


# Die eigenständigen Vergabe-Rollenprompts liegen außerhalb der drei Plugin-Verzeichnisse.
COMPONENT = "vergaberecht-werkstatt"
ROLES = {"bieter": "bieter-unternehmen", "konkurrenten": "konkurrenten-rechtsschutz",
         "vergabestelle": "vergabestelle-behoerden"}
PUBLICATIONS = {
    "insolvenzsachbearbeitung/README.md": "insolvenzsachbearbeitung",
    "strafvollzug-jva/README.md": "strafvollzug-jva",
    f"{COMPONENT}/README.md": COMPONENT,
    "references/leitentscheidungen-anker.md": "repository",
    "ki-native-kanzlei/references/repository/references/leitentscheidungen-anker.md": "ki-native-kanzlei",
    "testakten/megaprompts/richter-verwaltungsgericht.md": "richter-verwaltungsgericht",
    "gerichtsplugins/richter-verwaltungsgericht/references/hauptworkflow-fachpruefung.md": "richter-verwaltungsgericht",
    "gerichtsplugins/richter-verwaltungsgericht/skills/juristischer-argumentationskern/SKILL.md": "richter-verwaltungsgericht",
    "gerichtsplugins/richter-verwaltungsgericht/skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md": "richter-verwaltungsgericht",
}
for suffix, role in ROLES.items():
    PUBLICATIONS[f"{COMPONENT}/vergaberecht-arbeitsprompt-{suffix}.md"] = role
    PUBLICATIONS[f"{COMPONENT}/{role}/README.md"] = role
    PUBLICATIONS[f"{COMPONENT}/skills-index/{role}.md"] = role


def is_reviewed_source(name):
    # Die Registry bindet jeden einzelnen Dateipfad; andere Dateien bleiben unverändert.
    return (is_workshop(name) or name in PUBLICATIONS
            or (name.startswith(COMPONENT + "/") and name.endswith(".md"))
            or name == f"{COMPONENT}/scripts/generate-megaprompt.py")


PRIOR_TAGS = {
    "vergabestelle-behoerden": "qualitaetsrunde-v445.36.18",
    "bieter-unternehmen": "paketpflege-20261122-v445.36.9",
    "konkurrenten-rechtsschutz": "paketpflege-20261122-v445.36.9",
}


def edition_links(name, content, *, activating):
    """Exakte Downloadziele und Versionszeile der drei veröffentlichten Rollenpakete."""
    for role, tag in PRIOR_TAGS.items():
        old = f"/releases/download/{tag}/{role}.zip".encode()
        new = f"/releases/download/qualitaetsrunde-v445.36.19/{role}.zip".encode()
        content = content.replace(old, new) if activating else content.replace(new, old)
        if name == f"{COMPONENT}/skills-index/{role}.md":
            old = f"Pluginstand `v{tag.rsplit('-v', 1)[1]}`".encode()
            new = b"Pluginstand `v445.36.19`"
            content = content.replace(old, new) if activating else content.replace(new, old)
    return content


def previous(root, name, content, *, plugin=None):
    if not is_reviewed_source(name):
        return content
    row = proof(root).get("files", {}).get(name)
    if row is None:
        return content
    if plugin is not None and plugin != row["plugin"]:
        raise ValueError(f"{name}: Werkstatttext gehört zu anderem Plugin")
    if "activated_sha256" in row and digest(content) == row["activated_sha256"]:
        content = edition_links(name, content, activating=False)
    if digest(content) != row["after_sha256"]:
        raise ValueError(f"{name}: Werkstatttext seit der dokumentierten Prüfung verändert")
    pieces = []
    cursor = 0
    for start, end, old_text in row["reverse"]:
        if not cursor <= start <= end <= len(content):
            raise ValueError(f"{name}: ungültige Position im Nachweis der Vorfassung")
        pieces.extend((content[cursor:start], old_text.encode("utf-8")))
        cursor = end
    pieces.append(content[cursor:])
    original = b"".join(pieces)
    if digest(original) != row["before_sha256"]:
        raise ValueError(f"{name}: Vorfassung des Werkstatttexts nicht bytegleich rekonstruierbar")
    return original


def preserved_in_release(root, scope, source, expected, plugin):
    """Einen erhaltenen Prompt nur im unveränderten, früher veröffentlichten Scope prüfen."""
    prior = proof(root).get("prior_scopes", {}).get(scope["tag"])
    if not prior:
        return False
    canonical = json.dumps(scope, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    if digest(canonical) != prior:
        return False
    name = source.relative_to(root).as_posix()
    record = proof(root)["files"].get(name)
    if record is None or record["before_sha256"] != expected:
        return False
    return digest(previous(root, name, source.read_bytes(), plugin=plugin)) == expected


def validate_all(root):
    rows = proof(root).get("files", {})
    for name, row in rows.items():
        if not is_reviewed_source(name):
            raise ValueError(f"{name}: kein registrierbarer Werkstatttext oder Downloadverweis")
        previous(root, name, (root / name).read_bytes(), plugin=row["plugin"])
    return len(rows)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print(f"{validate_all(root)} Werkstatt-Vorfassungen geprüft.")
