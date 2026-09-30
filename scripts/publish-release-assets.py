#!/usr/bin/env python3
"""Upload and verify staged releases, then publish companion before main."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

from release_asset_common import expected_asset_metadata
from release_routing import (
    CONFIG, ROOT, companion_asset_names, companion_cases, companion_tag, marketplace_version,
)

SCRIPTS = Path(__file__).resolve().parent


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=False, timeout=300)


def api(resource: str, *, allow_missing: bool = False) -> dict | None:
    result = run(["gh", "api", resource])
    if result.returncode:
        if allow_missing and "(HTTP 404)" in result.stderr:
            return None
        raise RuntimeError(f"GitHub API {resource}: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    if not isinstance(data, dict):
        raise ValueError(f"Unexpected API response: {resource}")
    return data


def tag_commit(repo: str, tag: str, *, allow_missing: bool = False) -> str | None:
    ref = api(f"repos/{repo}/git/ref/tags/{quote(tag, safe='')}", allow_missing=allow_missing)
    if ref is None:
        return None
    obj = ref["object"]
    seen = set()
    while True:
        kind, sha = obj["type"], obj["sha"]
        if not re.fullmatch(r"[0-9a-f]{40}", sha) or sha in seen:
            raise ValueError(f"Invalid or cyclic tag object for {tag}")
        seen.add(sha)
        if kind == "commit":
            return sha
        if kind != "tag" or len(seen) > 16:
            raise ValueError(f"Tag {tag} does not resolve to a commit")
        obj = api(f"repos/{repo}/git/tags/{sha}")["object"]


def companion_release(repo: str, tag: str) -> dict | None:
    # gh also looks up drafts by pending tag; REST releases/tags only finds published releases.
    result = run(["gh", "release", "view", tag, "--repo", repo, "--json", "databaseId,tagName,isDraft"])
    if result.returncode:
        if result.stderr.strip() == "release not found":
            return None
        raise RuntimeError(f"Could not read release {tag}: {result.stderr.strip()}")
    release = json.loads(result.stdout)
    if not isinstance(release, dict) or release.get("tagName") != tag or not release.get("databaseId") or not isinstance(release.get("isDraft"), bool):
        raise ValueError(f"Unexpected release metadata for {tag}")
    return release


def ensure_companion(repo: str, tag: str, primary: str, sha: str) -> None:
    actual = tag_commit(repo, tag, allow_missing=True)
    if actual is None:
        created = run([
            "gh", "api", f"repos/{repo}/git/refs", "--method", "POST",
            "-f", f"ref=refs/tags/{tag}", "-f", f"sha={sha}",
        ])
        # A lost response or concurrent creation is safe only at the exact commit.
        actual = tag_commit(repo, tag, allow_missing=True)
        if actual is None:
            raise RuntimeError(f"Could not create {tag}: {created.stderr.strip()}")
    if actual != sha:
        raise ValueError(f"Companion tag {tag} points to {actual}, expected {sha}; not changed")

    release = companion_release(repo, tag)
    if release is None:
        created = run([
            "gh", "release", "create", tag, "--repo", repo, "--title", tag,
            "--target", sha, "--verify-tag", "--latest=false", "--draft",
            "--notes", f"Akten-ZIPs zu [{primary}](https://github.com/{repo}/releases/tag/{primary}). "
            "Die Sammelpakete bleiben vollständig im Hauptrelease. "
            "checksums-sha256.txt gilt nur für die Assets dieses Begleitreleases.",
        ])
        release = companion_release(repo, tag)
        if release is None:
            raise RuntimeError(f"Could not create draft {tag}: {created.stderr.strip()}")


def execute(command: list[str]) -> None:
    # Keep the existing uploader's progress visible and propagate failures.
    subprocess.run(command, check=True)


def publish(staging: Path, primary: str, repo: str, *, root: Path = ROOT,
            config: Path = CONFIG) -> None:
    slugs = companion_cases(config, root)
    main_assets = set(expected_asset_metadata(staging / "main"))
    tag = companion_tag(marketplace_version(root)) if slugs else None
    sha = None
    if tag:
        if primary != f"v{marketplace_version(root)}":
            raise ValueError("Primary tag must match the current marketplace version")
        companion_assets = set(expected_asset_metadata(staging / "companion"))
        routed = companion_asset_names(slugs)
        if companion_assets != routed | {"checksums-sha256.txt"} or main_assets & routed:
            raise ValueError("Staged assets do not match the configured release routes")
        sha = tag_commit(repo, primary)
        head = run(["git", "-C", str(root), "rev-parse", "HEAD"])
        if head.returncode or head.stdout.strip() != sha:
            raise ValueError("Build checkout does not match the exact primary tag commit")
        ensure_companion(repo, tag, primary, sha)
    elif (staging / "companion").exists():
        raise ValueError("Unexpected companion stage with empty routing configuration")

    releases = [(staging / "main", primary)]
    if tag:
        releases.append((staging / "companion", tag))
    for directory, release_tag in releases:
        command = [
            sys.executable, str(SCRIPTS / "upload-release-assets.py"), str(directory), release_tag,
            "--repo", repo, "--workers", "4", "--attempts", "6",
        ]
        if tag:
            command.append("--protect-published")
        if release_tag == tag:
            command.append("--require-existing")
        execute(command)
    for directory, release_tag in releases:
        execute([
            sys.executable, str(SCRIPTS / "validate-release-assets.py"), str(directory), release_tag,
            "--repo", repo, "--timeout-seconds", "900", "--poll-seconds", "10",
        ])
    if tag:
        if tag_commit(repo, primary) != sha or tag_commit(repo, tag) != sha:
            raise ValueError("Release tag moved during upload; refusing publication")
        execute(["gh", "release", "edit", tag, "--draft=false", "--latest=false", "--repo", repo])
    execute(["gh", "release", "edit", primary, "--draft=false", "--repo", repo])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("staging", type=Path)
    parser.add_argument("tag")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--config", type=Path, default=CONFIG)
    args = parser.parse_args()
    try:
        publish(args.staging, args.tag, args.repo, root=args.root, config=args.config)
    except (OSError, ValueError, RuntimeError, KeyError, subprocess.SubprocessError) as exc:
        print(f"publish-release-assets failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
