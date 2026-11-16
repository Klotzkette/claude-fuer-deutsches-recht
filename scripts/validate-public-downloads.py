#!/usr/bin/env python3
"""Prüft Release-Links in Downloadtabellen gegen öffentliche GitHub-Releases.

Ergänzt die Offline-Prüfung: Ein Draft oder ein noch nicht hochgeladenes Asset
ist kein öffentlicher Download. Archivinhalt und Prüfsummen prüft dieses Skript
nicht; dafür bleiben die bestehenden Build- und Release-Validatoren zuständig.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen

from release_routing import REPOSITORY, RELEASE_BASE, ROOT
from testakte_download_notices import download_readmes

LINK = re.compile(
    re.escape(RELEASE_BASE)
    + r"/(?:latest/download|download/(?P<tag>[^/\s<>\"']+))/"
    + r"(?P<asset>[^\s<>\"'()?#]+)"
)


def release_links(paths: list[Path]) -> dict[tuple[str, str], list[str]]:
    links: dict[tuple[str, str], list[str]] = defaultdict(list)
    for path in paths:
        text = html.unescape(path.read_text(encoding="utf-8"))
        for match in LINK.finditer(text):
            key = (unquote(match.group("tag") or "latest"), unquote(match.group("asset")))
            line = text.count("\n", 0, match.start()) + 1
            links[key].append(f"{path}:{line}")
    return dict(links)


def public_json(resource: str):
    # Absichtlich weder gh noch einen Token verwenden: Besucher sehen keine Drafts.
    request = Request(
        f"https://api.github.com/repos/{REPOSITORY}/{resource}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "release-download-check"},
    )
    try:
        with urlopen(request, timeout=20) as response:
            return json.load(response)
    except HTTPError as exc:
        exc.close()
        if exc.code == 404:
            detail = "öffentlich nicht erreichbar (HTTP 404; fehlt oder ist noch ein Entwurf)"
        elif exc.code in (403, 429):
            detail = f"Prüfung nicht möglich (HTTP {exc.code}; Zugriff oder API-Limit prüfen)"
        else:
            detail = f"GitHub antwortet mit HTTP {exc.code}"
        raise ValueError(detail) from exc
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        raise ValueError(f"öffentliche Abfrage fehlgeschlagen: {exc}") from exc


def github_cli_json(resource: str):
    """Nutzt für große Prüfungen das Budget der bereits eingerichteten CLI."""
    endpoint = f"repos/{REPOSITORY}" + (f"/{resource}" if resource else "")
    for delay in (0, 1, 3):
        if delay:
            sleep(delay)
        try:
            result = subprocess.run(
                ["gh", "api", endpoint], capture_output=True, text=True, timeout=25, check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise ValueError(f"GitHub-CLI-Abfrage fehlgeschlagen: {exc}") from exc
        if not result.returncode or not re.search(r"\bHTTP (500|502|503|504)\b", result.stderr):
            break
    if result.returncode:
        raise ValueError(f"GitHub-CLI-Abfrage fehlgeschlagen: {result.stderr.strip()}")
    try:
        return json.loads(result.stdout)
    except ValueError as exc:
        raise ValueError("GitHub CLI lieferte kein gültiges JSON") from exc


def public_assets(tag: str, get_json=None) -> dict[str, dict]:
    if get_json is None:
        get_json = public_json
    endpoint = "releases/latest" if tag == "latest" else f"releases/tags/{quote(tag, safe='')}"
    release = get_json(endpoint)
    if not isinstance(release, dict) or release.get("draft") is not False or not release.get("published_at"):
        raise ValueError("Release ist nicht als veröffentlicht bestätigt")
    release_id = release.get("id")
    if type(release_id) is not int or release_id <= 0:
        raise ValueError("Release-ID fehlt oder ist ungültig")
    if tag != "latest" and release.get("tag_name") != tag:
        raise ValueError("Release-Tag stimmt nicht mit dem Downloadlink überein")
    assets: dict[str, dict] = {}
    # Pagination ist nötig: Der Begleitrelease hat deutlich mehr als 100 Assets.
    for page in range(1, 12):
        batch = get_json(f"releases/{release_id}/assets?per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("Assetliste ist ungültig")
        for asset in batch:
            if not isinstance(asset, dict) or not isinstance(asset.get("name"), str) or not asset["name"]:
                raise ValueError("Asset ohne gültigen Dateinamen")
            name = asset["name"]
            if name in assets:
                raise ValueError(f"Doppeltes Asset: {name}")
            assets[name] = asset
        if len(batch) < 100:
            return assets
    raise ValueError("Assetliste überschreitet die Sicherheitsgrenze")


def validate(links: dict[tuple[str, str], list[str]], get_json=None) -> list[str]:
    errors: list[str] = []
    by_tag: dict[str, list[str]] = defaultdict(list)
    for tag, name in links:
        by_tag[tag].append(name)
    for tag, names in sorted(by_tag.items()):
        try:
            assets = public_assets(tag, get_json=get_json)
        except ValueError as exc:
            errors.append(f"{tag}: {exc}; betrifft {len(names)} Downloadziele, z. B. {links[tag, names[0]][0]}")
            continue
        for name in sorted(names):
            asset = assets.get(name)
            if asset is None:
                reason = "Datei fehlt"
            elif asset.get("state") != "uploaded":
                reason = "Upload nicht abgeschlossen"
            elif type(asset.get("size")) is not int or asset["size"] <= 0:
                reason = "Datei ist leer oder Größenangabe ungültig"
            else:
                continue
            errors.append(f"{tag}/{name}: {reason}; {links[tag, name][0]}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="Ohne Pfade: alle README-Downloadtabellen und der Asset-Index")
    parser.add_argument("--github-cli", action="store_true", help="Angemeldete GitHub CLI für große Bestände nutzen")
    args = parser.parse_args()
    try:
        links = release_links(args.files or download_readmes(ROOT))
        if args.github_cli:
            repo = github_cli_json("")
            if not isinstance(repo, dict) or repo.get("private") is not False or repo.get("visibility") != "public":
                raise ValueError("Repository ist nicht als öffentlich bestätigt")
        errors = validate(links, get_json=github_cli_json if args.github_cli else None) if links else ["Keine Release-Downloadlinks gefunden"]
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors[:80]:
            print(f" - {error}", file=sys.stderr)
        print(f"validate-public-downloads: {len(errors)} Fehler", file=sys.stderr)
        return 1
    print(f"validate-public-downloads OK ({len(links)} öffentliche Release-Assets; keine Inhaltsprüfung)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
