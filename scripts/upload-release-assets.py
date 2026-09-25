#!/usr/bin/env python3
"""Lädt Release-Dateien parallel, wiederaufnehmbar und hashbewusst hoch."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import random
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

from release_asset_common import expected_asset_metadata, release_assets


PRINT_LOCK = threading.Lock()


def log(message: str, *, error: bool = False) -> None:
    with PRINT_LOCK:
        print(message, file=sys.stderr if error else sys.stdout, flush=True)


def run(command: list[str], *, timeout: int = 300) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )


def gh_json(resource: str) -> Any:
    detail = ""
    for attempt in range(1, 6):
        try:
            result = run(["gh", "api", resource])
        except subprocess.TimeoutExpired:
            detail = "Zeitüberschreitung"
        else:
            if result.returncode == 0:
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError as exc:
                    detail = "ungültige JSON-Antwort"
                    if attempt == 5:
                        raise RuntimeError(f"gh api {resource}: {detail}") from exc
            else:
                detail = result.stderr.strip() or result.stdout.strip()
        if attempt < 5:
            time.sleep(min(2 ** attempt, 15) + random.uniform(0, 1))
    raise RuntimeError(f"gh api {resource}: {detail}")


def view_release(repo: str, tag: str) -> dict[str, Any] | None:
    result = run(
        [
            "gh",
            "release",
            "view",
            tag,
            "--repo",
            repo,
            "--json",
            "databaseId,tagName,isDraft",
        ]
    )
    if result.returncode:
        return None
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Release {tag}: ungültige JSON-Antwort") from exc
    release_id = data.get("databaseId")
    if not release_id:
        raise RuntimeError(f"Release-ID für {repo}@{tag} fehlt")
    return {"id": int(release_id), **data}


def ensure_release(repo: str, tag: str) -> dict[str, Any]:
    release = view_release(repo, tag)
    if release is not None:
        return release

    create = run(
        [
            "gh",
            "release",
            "create",
            tag,
            "--repo",
            repo,
            "--title",
            tag,
            "--generate-notes",
            "--draft",
        ]
    )
    if create.returncode:
        release = view_release(repo, tag)
        if release is not None:
            return release
        raise RuntimeError(f"Release {tag} konnte nicht angelegt werden: {create.stderr.strip()}")
    log(f"Entwurfsrelease {tag} angelegt")

    for attempt in range(1, 6):
        release = view_release(repo, tag)
        if release is not None:
            return release
        if attempt < 5:
            time.sleep(min(2 ** attempt, 15) + random.uniform(0, 1))
    raise RuntimeError(f"Release-ID für {repo}@{tag} blieb nach dem Anlegen unsichtbar")


def fetch_remote_assets(repo: str, release_id: int) -> dict[str, dict[str, Any]]:
    assets: dict[str, dict[str, Any]] = {}
    page = 1
    while True:
        batch = gh_json(f"repos/{repo}/releases/{release_id}/assets?per_page=100&page={page}")
        if not isinstance(batch, list):
            raise RuntimeError(f"Asset-Seite {page} ist keine Liste")
        for asset in batch:
            name = asset.get("name")
            if not name:
                raise RuntimeError(f"Asset ohne Namen auf Seite {page}")
            if name in assets:
                raise RuntimeError(f"Doppeltes Remote-Asset: {name}")
            assets[name] = asset
        if len(batch) < 100:
            return assets
        page += 1


def same_asset(local: dict[str, int | str], remote: dict[str, Any]) -> bool:
    return (
        remote.get("state") == "uploaded"
        and int(remote.get("size") or -1) == int(local["size"])
        and remote.get("digest") == local["digest"]
    )


def delete_asset(repo: str, asset: dict[str, Any]) -> None:
    asset_id = asset.get("id")
    if not asset_id:
        raise RuntimeError(f"Remote-Asset ohne ID: {asset.get('name')}")
    detail = ""
    for attempt in range(1, 6):
        try:
            result = run(
                ["gh", "api", "--method", "DELETE", f"repos/{repo}/releases/assets/{asset_id}"]
            )
        except subprocess.TimeoutExpired:
            detail = "Zeitüberschreitung"
        else:
            if result.returncode == 0 or "HTTP 404" in result.stderr:
                return
            detail = result.stderr.strip() or result.stdout.strip()
        if attempt < 5:
            time.sleep(min(2 ** attempt, 15) + random.uniform(0, 1))
    raise RuntimeError(f"Asset {asset.get('name')} konnte nicht gelöscht werden: {detail}")


def upload_one(
    repo: str,
    release_id: int,
    path: Path,
    local: dict[str, int | str],
    attempts: int,
) -> None:
    # Der Entwurf wurde bereits aufgelöst. Ein erneuter Tag-Lookup je Datei kann
    # trotz vorhandener Release-ID vor dem eigentlichen Upload fehlschlagen.
    upload_url = (
        f"https://uploads.github.com/repos/{repo}/releases/{release_id}/assets?"
        + urlencode({"name": path.name})
    )
    for attempt in range(1, attempts + 1):
        try:
            result = run(
                [
                    "gh", "api", "--method", "POST", upload_url,
                    "--header", "Content-Type: application/octet-stream",
                    "--input", str(path),
                ],
                timeout=300,
            )
        except subprocess.TimeoutExpired:
            detail = "Zeitüberschreitung"
        else:
            if result.returncode == 0:
                try:
                    uploaded = json.loads(result.stdout)
                except json.JSONDecodeError:
                    detail = "Uploadantwort enthält kein gültiges JSON"
                else:
                    if (
                        isinstance(uploaded, dict)
                        and uploaded.get("name") == path.name
                        and same_asset(local, uploaded)
                    ):
                        return
                    detail = "Uploadantwort bestätigt Zustand, Größe und SHA256 nicht"
            else:
                detail = result.stderr.strip() or result.stdout.strip() or f"Exit {result.returncode}"

        # Eine verlorene Antwort kann einen bereits fertigen Upload verbergen.
        # Nie --clobber verwenden: korrekte Dateien bleiben auch dann erhalten.
        try:
            remote = fetch_remote_assets(repo, release_id).get(path.name)
        except RuntimeError as exc:
            detail += f"; Remotezustand nicht lesbar: {exc}"
        else:
            if remote is not None:
                if same_asset(local, remote):
                    return
                if remote.get("state") == "starter":
                    delete_asset(repo, remote)
                else:
                    raise RuntimeError(
                        f"{path.name}: vorhandenes Remote-Asset weicht ab; "
                        "kein automatisches Ersetzen während der Wiederholung"
                    )
        if attempt == attempts:
            raise RuntimeError(f"{path.name}: Upload nach {attempts} Versuchen fehlgeschlagen: {detail}")
        delay = min(15 * (2 ** (attempt - 1)), 180) + random.uniform(0, 5)
        log(
            f"{path.name}: Versuch {attempt} fehlgeschlagen: {detail}; "
            f"neuer Versuch in {delay:.0f} s",
            error=True,
        )
        time.sleep(delay)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path)
    parser.add_argument("tag")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--attempts", type=int, default=6)
    args = parser.parse_args()
    if not 1 <= args.workers <= 8:
        parser.error("--workers muss zwischen 1 und 8 liegen")
    if not 1 <= args.attempts <= 10:
        parser.error("--attempts muss zwischen 1 und 10 liegen")

    try:
        metadata = expected_asset_metadata(args.dist)
        paths = {path.name: path for path in release_assets(args.dist)}
        release = ensure_release(args.repo, args.tag)
        remote = fetch_remote_assets(args.repo, int(release["id"]))

        stale_names = sorted(set(remote) - set(metadata))
        changed_names = sorted(
            name for name in set(remote) & set(metadata) if not same_asset(metadata[name], remote[name])
        )
        for name in stale_names + changed_names:
            delete_asset(args.repo, remote[name])
        pending = sorted((set(metadata) - set(remote)) | set(changed_names))
        skipped = len(metadata) - len(pending)
        log(
            f"Release {args.tag}: {len(metadata)} Dateien, {skipped} unverändert, "
            f"{len(pending)} hochzuladen, {len(stale_names)} veraltet"
        )

        failures: list[str] = []
        completed = 0
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(
                    upload_one, args.repo, int(release["id"]), paths[name],
                    metadata[name], args.attempts,
                ): name
                for name in pending
            }
            for future in as_completed(futures):
                name = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    failures.append(str(exc))
                    log(str(exc), error=True)
                else:
                    completed += 1
                    if completed == len(pending) or completed % 25 == 0:
                        log(f"Uploadfortschritt: {completed}/{len(pending)}")
        if failures:
            raise RuntimeError(f"{len(failures)} Upload(s) fehlgeschlagen")
    except (OSError, RuntimeError, ValueError) as exc:
        log(f"upload-release-assets fehlgeschlagen: {exc}", error=True)
        return 1

    print(f"upload-release-assets OK ({len(metadata)} Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
