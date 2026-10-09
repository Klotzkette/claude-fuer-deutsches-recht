#!/usr/bin/env python3
"""Resolve a complete build first; create its immutable tag only after validation."""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

from release_routing import ROOT, marketplace_version

# Reuse the publisher's authenticated, fail-closed annotated-tag resolution.
SPEC = importlib.util.spec_from_file_location(
    "complete_release_publisher", Path(__file__).with_name("publish-release-assets.py"),
)
PUBLISH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PUBLISH)


def validate_tag(tag: str) -> str:
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        raise ValueError(f"Invalid complete release tag: {tag!r}")
    return tag


def validate_sha(sha: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ValueError(f"Invalid build commit: {sha!r}")
    return sha


def resolve_commit(repo: str, tag: str, fallback_sha: str) -> str:
    """Existing tags select their exact commit; only an actual 404 permits main."""
    validate_tag(tag)
    validate_sha(fallback_sha)
    return PUBLISH.tag_commit(repo, tag, allow_missing=True) or fallback_sha


def ensure_tag(repo: str, tag: str, expected_sha: str, root: Path = ROOT) -> str:
    validate_tag(tag)
    validate_sha(expected_sha)
    if tag != f"v{marketplace_version(root)}":
        raise ValueError("Complete release tag must match the built marketplace version")
    head = PUBLISH.run(["git", "-C", str(root), "rev-parse", "HEAD"])
    if head.returncode or head.stdout.strip() != expected_sha:
        raise ValueError("Build checkout does not match the resolved build commit")
    actual = PUBLISH.tag_commit(repo, tag, allow_missing=True)
    if actual is None:
        result = PUBLISH.run([
            "gh", "api", f"repos/{repo}/git/refs", "--method", "POST",
            "-f", f"ref=refs/tags/{tag}", "-f", f"sha={expected_sha}",
        ])
        # A lost creation response or concurrent run is safe only at the same SHA.
        actual = PUBLISH.tag_commit(repo, tag, allow_missing=True)
        if actual is None:
            raise RuntimeError(f"Could not create {tag}: {result.stderr.strip()}")
    if actual != expected_sha:
        raise ValueError(f"Release tag {tag} points to {actual}, expected {expected_sha}; not changed")
    return actual


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    resolve = commands.add_parser("resolve", help="Read the tag commit or use the workflow commit")
    resolve.add_argument("tag")
    resolve.add_argument("--repo", required=True)
    resolve.add_argument("--fallback-sha", required=True)
    ensure = commands.add_parser("ensure-tag", help="Create a missing tag at the validated build commit")
    ensure.add_argument("tag")
    ensure.add_argument("--repo", required=True)
    ensure.add_argument("--expected-sha", required=True)
    ensure.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        sha = resolve_commit(args.repo, args.tag, args.fallback_sha) if args.command == "resolve" else (
            ensure_tag(args.repo, args.tag, args.expected_sha, args.root)
        )
    except (OSError, ValueError, RuntimeError, KeyError, subprocess.SubprocessError) as exc:
        print(f"prepare-complete-release failed: {exc}", file=sys.stderr)
        return 1
    print(sha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
