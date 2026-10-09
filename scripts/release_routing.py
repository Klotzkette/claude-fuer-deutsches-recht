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


def validate_companion_part(part: int) -> int:
    if type(part) is not int or part < 1:
        raise ValueError(f"Invalid companion release part: {part!r}")
    return part


def companion_tag(version: str, part: int = 1) -> str:
    part = validate_companion_part(part)
    prefix = "akten" if part == 1 else f"akten-{part}"
    return f"{prefix}-v{validate_version(version)}"


def companion_stage(part: int) -> str:
    part = validate_companion_part(part)
    return "companion" if part == 1 else f"companion-{part}"


def companion_asset_names(slugs: tuple[str, ...]) -> set[str]:
    return {f"testakte-{slug}{suffix}.zip" for slug in slugs for suffix in ("", "-einzelpdfs")}


def companion_case_groups(slugs: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    """Sort cases once per release and keep each original/PDF ZIP pair together.

    Each part reserves one asset for its own checksum list. The first part keeps
    its historic tag and directory; further parts have one-based numeric suffixes.
    """
    if any(not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)
           for slug in slugs) or len(set(slugs)) != len(slugs):
        raise ValueError("Invalid or duplicate companion case slugs")
    if len(companion_asset_names(slugs)) != 2 * len(slugs):
        raise ValueError("Companion case ZIP filenames overlap")
    capacity = (MAX_RELEASE_ASSETS - 1) // 2
    if capacity < 1:
        raise ValueError("Release asset limit cannot hold a case ZIP pair and checksums")
    ordered = tuple(sorted(slugs))
    return tuple(ordered[start:start + capacity] for start in range(0, len(ordered), capacity))


def scoped_asset_url(asset: str, *, root: Path = ROOT) -> str | None:
    """An explicitly published component can precede the next complete release.

    Pins are per asset, never an implicit fallback to another version. Remove a
    pin only after that asset is verified in the corresponding complete release.
    """
    path = root / "scripts/scoped-release-assets.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if set(data) != {"schema_version", "assets"} or data["schema_version"] != 1:
        raise ValueError(f"Unsupported scoped release configuration: {path}")
    if not isinstance(data["assets"], dict):
        raise ValueError("Scoped assets must map filenames to release tags")
    for name, tag in data["assets"].items():
        if not re.fullmatch(r"[a-z0-9][a-z0-9.-]*\.zip", name) or not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", tag):
            raise ValueError(f"Invalid scoped release route: {name!r}: {tag!r}")
    tag = data["assets"].get(asset)
    return f"{RELEASE_BASE}/download/{tag}/{asset}" if tag else None


def plugin_asset_url(slug: str, *, root: Path = ROOT) -> str:
    asset = f"{slug}.zip"
    return scoped_asset_url(asset, root=root) or f"{RELEASE_BASE}/latest/download/{asset}"


def verified_scoped_package_version(asset: str, tag: str, version: str, *, root: Path = ROOT) -> bool:
    """Accept a differing bundle tag only with an exact, recorded package proof."""
    path = root / "scripts/scoped-release-package-versions.json"
    if not path.exists():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or set(data) != {"schema_version", "assets"} or data["schema_version"] != 1 \
            or not isinstance(data["assets"], dict):
        raise ValueError(f"Unsupported scoped package version configuration: {path}")
    entry = data["assets"].get(asset)
    if entry is None:
        return False
    if not isinstance(entry, dict) or set(entry) != {"tag", "version", "sha256", "evidence"}:
        raise ValueError(f"Invalid scoped package proof: {asset}")
    if entry["tag"] != tag or entry["version"] != version:
        return False
    digest, evidence = entry["sha256"], entry["evidence"]
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest) \
            or not isinstance(evidence, str):
        raise ValueError(f"Invalid scoped package digest or evidence: {asset}")
    relative = Path(evidence)
    if relative.is_absolute() or not relative.parts or relative.parts[0] != "quality" \
            or ".." in relative.parts or relative.as_posix() != evidence or relative.suffix != ".json" \
            or any((root / Path(*relative.parts[:index])).is_symlink() for index in range(1, len(relative.parts) + 1)):
        raise ValueError(f"Invalid scoped package evidence path: {evidence}")
    try:
        proof = json.loads((root / relative).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"Cannot read scoped package evidence: {evidence}") from exc
    if not isinstance(proof, dict) or proof.get("version") != version or proof.get("release") != tag \
            or not isinstance(proof.get("assets"), dict) or proof["assets"].get(asset) != digest \
            or not isinstance(proof.get("plugins"), list) \
            or not any(isinstance(plugin, dict) and plugin.get("name") == asset.removesuffix(".zip")
                       for plugin in proof["plugins"]):
        raise ValueError(f"Scoped package evidence does not match asset, tag, version and digest: {asset}")
    return True


def validate_plugin_version(plugin: dict, version: str, *, root: Path = ROOT) -> None:
    """Abweichende Paketversionen nur mit exakt zugeordnetem Komponentenrelease."""
    candidate = validate_version(plugin.get("version"))
    if candidate == validate_version(version):
        return
    asset = f"{plugin['name']}.zip"
    url = scoped_asset_url(asset, root=root)
    if url:
        tag = url.removeprefix(f"{RELEASE_BASE}/download/").split("/", 1)[0]
        if tag.endswith(f"-v{candidate}") or verified_scoped_package_version(asset, tag, candidate, root=root):
            return
    raise ValueError(f"{plugin['name']}: Version {candidate} ohne passendes Komponentenrelease")


def case_asset_url(slug: str, suffix: str = "", *, version: str | None = None,
                   root: Path = ROOT, config: Path = CONFIG) -> str:
    if suffix not in ("", "-einzelpdfs"):
        raise ValueError(f"Unsupported case ZIP suffix: {suffix!r}")
    pin = scoped_asset_url(f"testakte-{slug}{suffix}.zip", root=root)
    if pin:
        return pin
    route = "latest/download"
    for part, slugs in enumerate(companion_case_groups(companion_cases(config, root)), start=1):
        if slug in slugs:
            route = f"download/{companion_tag(version if version is not None else marketplace_version(root), part)}"
            break
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
    def resolve(match):
        name = match[1][len("testakte-"):-len(".zip")]
        suffix = "-einzelpdfs" if name.endswith("-einzelpdfs") else ""
        slug = name[:-len(suffix)] if suffix else name
        return case_asset_url(slug, suffix, version=version, root=root, config=config)
    return pattern.sub(resolve, text)


def check_asset_limit(names: list[str] | set[str]) -> None:
    if len(names) > MAX_RELEASE_ASSETS:
        raise ValueError(f"{len(names)} assets exceed the GitHub limit of {MAX_RELEASE_ASSETS} (including checksums)")
