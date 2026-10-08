#!/usr/bin/env python3
"""Verify GitHub Release assets after upload.

The release workflow uploads many ZIP, Markdown and manifest assets. A green
upload command is not quite enough: GitHub may throttle, replace assets slowly,
or leave stale assets on an existing release. This script polls the Release API
until every expected local asset exists remotely with uploaded state, matching
size and matching sha256 digest. It also validates that the checksum manifest
lists every other expected asset exactly once with the correct local digest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


ASSET_NAMES = {"marketplace.json", "checksums-sha256.txt"}
GH_API_TIMEOUT_SECONDS = 30
HASH_CHUNK_SIZE = 1024 * 1024


def fail(message: str) -> None:
    print(f"validate-release-assets failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def run_gh_api(resource: str) -> Any:
    try:
        proc = subprocess.run(
            ["gh", "api", resource],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=GH_API_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        fail(f"gh api {resource!r} timed out after {GH_API_TIMEOUT_SECONDS} seconds")
    if proc.returncode != 0:
        fail(f"gh api {resource!r} failed: {proc.stderr.strip()}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        fail(f"gh api {resource!r} returned invalid JSON: {exc}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(HASH_CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def expected_assets(dist: Path) -> dict[str, dict[str, Any]]:
    expected: dict[str, dict[str, Any]] = {}
    for path in sorted(dist.iterdir(), key=lambda p: p.name):
        if not path.is_file():
            continue
        is_unified_mini_prompt = path.name.endswith("-unified-mini-prompt.md")
        is_root_prompt = (
            path.name.startswith("vergaberecht-arbeitsprompt-")
            or path.name.startswith("vergaberecht-kurzprompt-")
        ) and path.suffix == ".md"
        if (
            path.suffix != ".zip"
            and path.name not in ASSET_NAMES
            and not is_unified_mini_prompt
            and not is_root_prompt
        ):
            continue
        expected[path.name] = {
            "size": path.stat().st_size,
            "digest": "sha256:" + sha256_file(path),
        }
    if not expected:
        fail(f"{dist}: no release assets found")
    return expected


def fetch_assets(repo: str, tag: str) -> dict[str, dict[str, Any]]:
    release = run_gh_api(f"repos/{repo}/releases/tags/{tag}")
    release_id = release.get("id")
    if not release_id:
        fail(f"{repo}@{tag}: release id missing")

    assets: dict[str, dict[str, Any]] = {}
    page = 1
    while True:
        batch = run_gh_api(f"repos/{repo}/releases/{release_id}/assets?per_page=100&page={page}")
        if not isinstance(batch, list):
            fail(f"{repo}@{tag}: assets response page {page} is not a list")
        for asset in batch:
            name = asset.get("name")
            if not name:
                fail(f"{repo}@{tag}: asset without name on page {page}")
            if name in assets:
                fail(f"{repo}@{tag}: duplicate asset name {name}")
            assets[name] = asset
        if len(batch) < 100:
            break
        page += 1
    return assets


def diff_assets(expected: dict[str, dict[str, Any]], actual: dict[str, dict[str, Any]]) -> list[str]:
    problems: list[str] = []
    expected_names = set(expected)
    actual_names = set(actual)

    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    if missing:
        problems.append(f"missing assets: {missing[:20]}")
    if extra:
        problems.append(f"unexpected stale assets: {extra[:20]}")

    for name in sorted(expected_names & actual_names):
        asset = actual[name]
        want = expected[name]
        if asset.get("state") != "uploaded":
            problems.append(f"{name}: state={asset.get('state')!r}")
        if int(asset.get("size") or 0) != int(want["size"]):
            problems.append(f"{name}: size remote={asset.get('size')} local={want['size']}")
        remote_digest = asset.get("digest")
        if remote_digest != want["digest"]:
            problems.append(f"{name}: digest remote={remote_digest!r} local={want['digest']!r}")
    return problems


def validate_checksums_manifest(dist: Path, expected: dict[str, dict[str, Any]]) -> None:
    manifest = dist / "checksums-sha256.txt"
    if not manifest.is_file():
        fail(f"{manifest.name}: missing from local dist")

    entries: dict[str, str] = {}
    for line_no, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            fail(f"{manifest.name}:{line_no}: expected sha256 digest and asset name")
        digest, name = parts
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            fail(f"{manifest.name}:{line_no}: invalid sha256 digest {digest!r}")
        name = name.lstrip("*").strip()
        if "/" in name or name in {"", ".", ".."}:
            fail(f"{manifest.name}:{line_no}: invalid asset name {name!r}")
        if name in entries:
            fail(f"{manifest.name}:{line_no}: duplicate asset {name!r}")
        entries[name] = digest

    expected_names = set(expected) - {"checksums-sha256.txt"}
    actual_names = set(entries)
    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    if missing:
        fail(f"{manifest.name}: missing checksum entries: {missing[:20]}")
    if extra:
        fail(f"{manifest.name}: unexpected checksum entries: {extra[:20]}")

    for name in sorted(expected_names):
        want = str(expected[name]["digest"]).split(":", 1)[1]
        if entries[name] != want:
            fail(f"{manifest.name}: checksum mismatch for {name}: {entries[name]} != {want}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path)
    parser.add_argument("tag")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"))
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--poll-seconds", type=int, default=10)
    args = parser.parse_args()

    if not args.repo:
        fail("--repo or GITHUB_REPOSITORY is required")

    expected = expected_assets(args.dist)
    validate_checksums_manifest(args.dist, expected)
    deadline = time.monotonic() + args.timeout_seconds
    last_problems: list[str] = []

    while True:
        actual = fetch_assets(args.repo, args.tag)
        last_problems = diff_assets(expected, actual)
        if not last_problems:
            print(f"validate-release-assets OK ({len(expected)} assets verified on {args.repo}@{args.tag})")
            return
        if time.monotonic() >= deadline:
            break
        print(
            f"Waiting for release assets ({len(last_problems)} issue(s)); "
            f"first issue: {last_problems[0]}",
            flush=True,
        )
        time.sleep(args.poll_seconds)

    for problem in last_problems[:50]:
        print(problem, file=sys.stderr)
    fail(f"{len(last_problems)} release asset problem(s) after polling")


if __name__ == "__main__":
    main()
