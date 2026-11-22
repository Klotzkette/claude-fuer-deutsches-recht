"""Geplante Paketlinks und die spätere Aktivierung derselben öffentlichen Dateien."""
from __future__ import annotations

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
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())["plugins"]
    result = {}
    for version, group in plan["gruppen"].items():
        previous, new_tag = group["vorgaenger"], f"{edition}-v{version}"
        native, portable = 0, 0
        for plugin in market:
            name = plugin["name"]
            if plugin["version"] != version or name in plan["unveraendert"]:
                continue
            for asset in (name + ".zip", name + "-portable.zip"):
                if asset.endswith("-portable.zip") and asset not in active:
                    continue
                if active.get(asset) not in (previous, new_tag):
                    raise ValueError(f"{asset}: Aktueller Paketstand gehört nicht zum Ausgabeplan")
                result[asset] = previous, new_tag
                if asset == name + ".zip":
                    native += 1
                else:
                    portable += 1
        if (native, portable) != (group["native"], group["portable"]):
            raise ValueError(f"{new_tag}: Abweichende Anzahl nativer oder portabler Pakete")
    return result


def planned_links(text: str, routes: dict[str, tuple[str, str]]) -> str:
    def replace(match):
        current, name = match.groups()
        pair = routes.get(name)
        if pair and current == pair[0]:
            return f"{RELEASE_BASE}/download/{pair[1]}/{name}"
        return match[0]
    return LINK.sub(replace, text)


def activate_routes(root: Path, routes) -> int:
    """Schaltet Nutzerseiten und aktive Zuordnung auf dieselben geprüften Ausgabeziele."""
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    total = 0
    for relative in tracked:
        path = Path(relative)
        if not path.parts or path.parts[0] in {"quality", "archive", "archiv"} or path.parts[:2] == ("docs", "releases"):
            continue
        if not (path.name == "README.md" or path.suffix.lower() == ".html"
                or path.parts[0] in {"skills-index", "vergaberecht-werkstatt"} and path.suffix == ".md"
                or relative in {"SKILLS.md", "ASSET_INDEX.md"}):
            continue
        file = root / path
        content = file.read_bytes()
        if RELEASE_BASE.encode() not in content:
            continue
        updated = planned_links(content.decode("utf-8"), routes).encode("utf-8")
        if content != updated:
            file.write_bytes(updated)
            total += 1
    registry = root / "scripts/scoped-release-assets.json"
    data = json.loads(registry.read_text())
    if any(data["assets"][asset] != pair[1] for asset, pair in routes.items()):
        data["assets"].update({asset: pair[1] for asset, pair in routes.items()})
        registry.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        total += 1
    return total
