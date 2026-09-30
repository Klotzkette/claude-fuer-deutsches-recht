#!/usr/bin/env python3
"""Shared, explicit routing for central case ZIPs; all other assets stay put."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path(__file__).with_name("release-routes.json")
REPOSITORY = "Klotzkette/claude-fuer-deutsches-recht"
RELEASE_BASE = f"https://github.com/{REPOSITORY}/releases"
MAX_RELEASE_ASSETS = 1000
CENTRAL_CASE_SCOPE = "all-central"
CENTRAL_CASE_SKIP_DIRS = {"megaprompts"}


def central_case_slugs(root: Path = ROOT) -> tuple[str, ...]:
    testakten = root / "testakten"
    if not testakten.is_dir():
        raise ValueError(f"Central case directory missing: {testakten}")
    return tuple(sorted(
        path.name for path in testakten.iterdir()
        if path.is_dir() and path.name not in CENTRAL_CASE_SKIP_DIRS
    ))


def companion_cases(config: Path = CONFIG, root: Path = ROOT) -> tuple[str, ...]:
    data = json.loads(config.read_text(encoding="utf-8"))
    if data == {"schema_version": 2, "companion_case_scope": CENTRAL_CASE_SCOPE}:
        return central_case_slugs(root)
    if set(data) != {"schema_version", "companion_case_slugs"} or data["schema_version"] != 1:
        raise ValueError(f"Unsupported release routing configuration: {config}")
    slugs = data["companion_case_slugs"]
    if not isinstance(slugs, list) or any(
        not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)
        for slug in slugs
    ) or len(set(slugs)) != len(slugs):
        raise ValueError("Invalid or duplicate companion case slugs")
    return tuple(slugs)


def validate_version(version: str) -> str:
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError(f"Invalid marketplace version: {version!r}")
    return version


def marketplace_version(root: Path = ROOT) -> str:
    data = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    return validate_version(data["version"])


def companion_tag(version: str) -> str:
    return f"akten-v{validate_version(version)}"


def companion_asset_names(slugs: tuple[str, ...]) -> set[str]:
    return {f"testakte-{slug}{suffix}.zip" for slug in slugs for suffix in ("", "-einzelpdfs")}


def case_asset_url(slug: str, suffix: str = "", *, version: str | None = None,
                   root: Path = ROOT, config: Path = CONFIG) -> str:
    if suffix not in ("", "-einzelpdfs"):
        raise ValueError(f"Unsupported case ZIP suffix: {suffix!r}")
    route = "latest/download"
    if slug in companion_cases(config, root):
        route = f"download/{companion_tag(version if version is not None else marketplace_version(root))}"
    return f"{RELEASE_BASE}/{route}/testakte-{slug}{suffix}.zip"


def rewrite_case_asset_urls(text: str, *, version: str | None = None,
                            root: Path = ROOT, config: Path = CONFIG) -> str:
    """Resolve agent placeholders and older version pins, only for routed ZIPs."""
    names = companion_asset_names(companion_cases(config, root))
    if not names:
        return text
    pattern = re.compile(
        re.escape(RELEASE_BASE) + r"/(?:latest/download|download/[^/\s<>\)\"]+)/"
        + "(" + "|".join(re.escape(name) for name in sorted(names)) + r")(?![\w.-])"
    )
    if not pattern.search(text):
        return text
    tag = companion_tag(version if version is not None else marketplace_version(root))
    return pattern.sub(lambda match: f"{RELEASE_BASE}/download/{tag}/{match[1]}", text)


def check_asset_limit(names: list[str] | set[str]) -> None:
    if len(names) > MAX_RELEASE_ASSETS:
        raise ValueError(f"{len(names)} assets exceed the GitHub limit of {MAX_RELEASE_ASSETS} (including checksums)")
