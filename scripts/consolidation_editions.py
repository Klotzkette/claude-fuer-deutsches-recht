"""Pfade und Vorfassungen der Quellenprüfung unabhängig von Git-Checkout und Fetch-Tiefe."""
from functools import lru_cache
import hashlib
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

from vergabestelle_revision import previous as before_vergabestelle

PROOF = Path("quality/plugin-consolidation/2026-11-25")
REGISTER_SHA256 = "9d33ff39da3923ea5f8c611e4b82afff006e11fa6e313709028e669b431c2b67"
BASE = "d8ec1bfd281f0ab56e801fc750d643b40afbb3df"


def sha(data):
    return hashlib.sha256(data).hexdigest()


@lru_cache(maxsize=4)
def _register(raw):
    if sha(raw) != REGISTER_SHA256:
        raise ValueError("Erhaltungsregister der Insolvenz-Zusammenführung verändert")
    return json.loads(raw)


@lru_cache(maxsize=4)
def _load(path, size, mtime, ctime):
    return _register(path.read_bytes())


def register(root):
    path = root / PROOF / "bestand.json"
    if not path.is_file():
        # Kleine Prüffixtures und Quellstände vor der Zusammenführung.
        if (root / PROOF).exists():
            raise ValueError("Erhaltungsregister der Insolvenz-Zusammenführung fehlt")
        return {}
    stat = path.stat()
    return _load(path, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)


@lru_cache(maxsize=2)
def _archive(path, size, mtime, ctime, expected):
    raw = path.read_bytes()
    if sha(raw) != expected:
        raise ValueError("Vorfassungsarchiv der Zusammenführung verändert")
    return ZipFile(BytesIO(raw))


def archived(root, proof, key):
    path = root / PROOF / "vorfassungen.zip"
    stat = path.stat()
    data = _archive(path, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns, proof["archive_sha256"]).read(key)
    if sha(data) != key:
        raise ValueError(f"Historische Fassung {key} beschädigt")
    return data


def previous(root, name, content, *, stage="edition", plugin=None):
    """Eine registrierte Ausgabe ergibt nur bei identischem Pfad und Endhash ihren Vorgänger."""
    if stage == "edition":
        content = before_vergabestelle(root, name, content, plugin=plugin)
    proof = register(root)
    row = proof.get(stage, {}).get(name)
    if row is None:
        return content
    if sha(content) != row["after_sha256"]:
        raise ValueError(f"{name}: Datei weicht von der einzeln belegten Fassung ab")
    return archived(root, proof, row["before_sha256"])


def previous_file(root, path):
    return previous(root, path.relative_to(root).as_posix(), path.read_bytes())


def retained_entries(root, catalog):
    """Zwei historische Pluginidentitäten an ihren erhaltenen Originalquellen auflösen."""
    retired = register(root).get("retired", {})
    if not retired:
        return []
    active = {p["name"] for p in catalog}
    result = []
    for name, row in retired.items():
        manifest = json.loads((root / name / ".claude-plugin/plugin.json").read_bytes())
        if name in active or row["canonical"] not in active or manifest["name"] != name:
            raise ValueError(f"{name}: Archiv- und Marketplace-Zuordnung widersprechen einander")
        result.append({"name": name, "source": "./" + name})
    return result
