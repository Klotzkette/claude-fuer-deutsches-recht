"""Geplante Paketlinks und die spätere Aktivierung derselben öffentlichen Dateien."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess

from release_routing import RELEASE_BASE

EDITION = "paketpflege-20261122"
LINK = re.compile(re.escape(RELEASE_BASE) + r"/download/([a-z0-9.-]+)/([a-z0-9.-]+\.zip)(?![A-Za-z0-9/_.-])")


def edition_routes(root: Path, edition: str = EDITION) -> dict[str, tuple[str, str]]:
    """Ermittelt nur die ausdrücklich vorgesehenen Paketstände und vorhandenen Varianten."""
    if not re.fullmatch(r"paketpflege-[0-9]{8}", edition):
        raise ValueError("Ungültige Paketnachauflage")
    plan = json.loads((root / f"scripts/data/{edition}.json").read_text())
    if plan["edition"] != edition:
        raise ValueError("Ausgabeplan und Dateiname stimmen nicht überein")
    active = json.loads((root / "scripts/scoped-release-assets.json").read_text())["assets"]
    plugins = json.loads((root / ".claude-plugin/marketplace.json").read_text())["plugins"]
    versions = {plugin["name"]: plugin["version"] for plugin in plugins}
    excluded = {name + suffix for name in plan["unveraendert"] for suffix in (".zip", "-portable.zip")}
    successors = plan.get("nachfolger", {})
    result = {}
    for version, group in plan["gruppen"].items():
        previous, new_tag = group["vorgaenger"], f"{edition}-v{version}"
        # Früher veröffentlichte Plugins können im heutigen Marketplace zusammengeführt sein.
        # Die damaligen Routen und die Namensliste des Releases bestimmen den Archivbestand.
        names = {asset for asset, tag in active.items()
                 if asset.endswith(".zip") and tag in {previous, new_tag} and asset not in excluded}
        names.update(asset for asset, row in successors.items() if row["ausgabeversion"] == version)
        portable = {asset for asset in names if asset.endswith("-portable.zip")}
        if (len(names) - len(portable), len(portable)) != (group["native"], group["portable"]):
            raise ValueError(f"{new_tag}: Abweichende Anzahl nativer oder portabler Pakete")
        if any(asset.removesuffix("-portable.zip") + ".zip" not in names for asset in portable):
            raise ValueError(f"{new_tag}: Portables Paket ohne natives Paket")
        published = group.get("archivnamen_sha256")
        if published is not None:
            members = "".join(name + "\n" for name in sorted(names)).encode("utf-8")
            if hashlib.sha256(members).hexdigest() != published:
                raise ValueError(f"{new_tag}: Archivnamen weichen vom veröffentlichten Bestand ab")
        for asset in sorted(names):
            name = asset.removesuffix(".zip").removesuffix("-portable")
            successor = successors.get(asset)
            if successor:
                if (successor["ausgabeversion"] != version or active.get(asset) != successor["tag"]
                        or name not in versions or not successor["tag"].endswith("-v" + versions[name])):
                    raise ValueError(f"{asset}: Nachfolgetag oder Marketplace-Version stimmt nicht")
            elif name in versions and versions[name] != version:
                raise ValueError(f"{asset}: Marketplace-Version stimmt nicht mit der Ausgabe überein")
            elif name not in versions and published is None:
                raise ValueError(f"{asset}: Kein Nachweis im Marketplace oder veröffentlichten Archivbestand")
            result[asset] = previous, new_tag
    if set(successors) - result.keys():
        raise ValueError("Unbekanntes Nachfolgepaket im Ausgabeplan")
    return result


def planned_links(text: str, routes: dict[str, tuple[str, str]]) -> str:
    def replace(match):
        current, name = match.groups()
        pair = routes.get(name)
        if pair and current == pair[0]:
            return f"{RELEASE_BASE}/download/{pair[1]}/{name}"
        return match[0]
    return LINK.sub(replace, text)


def activate_routes(root: Path, routes, *, fallback_tags=None, extra_documents=()) -> int:
    """Schaltet Nutzerseiten und aktive Zuordnung auf dieselben geprüften Ausgabeziele."""
    registry = root / "scripts/scoped-release-assets.json"
    data = json.loads(registry.read_text())
    fallback_tags = fallback_tags or {}
    for asset, choices in routes.items():
        if data["assets"].get(asset, fallback_tags.get(asset)) not in choices:
            raise ValueError(f"{asset}: Diese Aktivierung würde einen anderen Paketstand überschreiben")
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    total = 0
    for relative in tracked:
        path = Path(relative)
        if not path.parts or path.parts[0] in {"quality", "archive", "archiv"} or path.parts[:2] == ("docs", "releases"):
            continue
        if not (path.name == "README.md" or path.suffix.lower() == ".html"
                or path.parts[0] in {"skills-index", "vergaberecht-werkstatt"} and path.suffix == ".md"
                or relative in {"SKILLS.md", "ASSET_INDEX.md"} or relative in extra_documents):
            continue
        file = root / path
        content = file.read_bytes()
        if RELEASE_BASE.encode() not in content:
            continue
        updated = planned_links(content.decode("utf-8"), routes).encode("utf-8")
        if content != updated:
            file.write_bytes(updated)
            total += 1
    if any(data["assets"].get(asset) != pair[1] for asset, pair in routes.items()):
        data["assets"].update({asset: pair[1] for asset, pair in routes.items()})
        registry.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        total += 1
    return total
