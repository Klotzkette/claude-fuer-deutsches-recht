#!/usr/bin/env python3
"""Geprüfte Qualitätsrunde am unveränderlichen Main-Commit veröffentlichen.

Verwendet den vorhandenen Uploader mit protect-published und die vorhandene
Assetprüfung. Ein vollständiger unabhängiger Download und Quellbyteabgleich
stehen zwingend vor dem Veröffentlichen des Entwurfs.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def load(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B = load("build-skill-quality-release.py")
P = load("publish-release-assets.py")


def execute(command, *, root=ROOT, timeout=900):
    subprocess.run(command, cwd=root, check=True, timeout=timeout)


def publish(dist: Path, scope: dict, expected_commit: str, repo: str, *, root: Path = ROOT, builder=None) -> None:
    builder = builder or B
    if not re.fullmatch(r"[a-f0-9]{40}", expected_commit):
        raise ValueError("Vollständiger unveränderlicher Zielcommit erforderlich")
    builder.checkout_state(root, expected_commit)
    execute(["git", "merge-base", "--is-ancestor", expected_commit, "origin/main"], root=root)
    builder.validate_assets(dist, scope, root, expected_commit=expected_commit)
    tag = scope["tag"]
    notes_name = tag.rsplit("-v", 1)[0] if B.PAKETPFLEGE_TAG.fullmatch(tag) else tag
    notes = root / "docs/releases" / (notes_name + ".md")
    if not notes.is_file() or not notes.read_text().strip():
        raise ValueError("Konkrete Release-Notiz fehlt")
    existing_tag = P.tag_commit(repo, tag, allow_missing=True)
    existing_release = P.companion_release(repo, tag)
    if existing_tag is not None and existing_tag != expected_commit:
        raise ValueError("Bestehender Tag zeigt auf einen anderen Commit und bleibt unverändert")
    if existing_release is not None and existing_release.get("isDraft") is not True:
        raise ValueError("Veröffentlichtes Release bleibt unverändert")
    # Erst nach allen lokalen Prüfungen darf ein bisher fehlender Tag entstehen.
    if existing_tag is None:
        execute(["gh", "api", f"repos/{repo}/git/refs", "--method", "POST",
                 "-f", f"ref=refs/tags/{tag}", "-f", f"sha={expected_commit}"], root=root)
    if P.tag_commit(repo, tag) != expected_commit:
        raise ValueError("Tag konnte nicht am freigegebenen Commit bestätigt werden")
    if existing_release is None:
        execute(["gh", "release", "create", tag, "--repo", repo, "--verify-tag", "--target", expected_commit,
                 "--draft", "--latest=false", "--title", scope.get("title", f"Qualitätsrunde {scope['version']}"), "--notes-file", str(notes)], root=root)
    draft = P.companion_release(repo, tag)
    if draft is None or draft.get("isDraft") is not True:
        raise ValueError("Release ist kein bestätigter Entwurf")
    execute([sys.executable, str(ROOT / "scripts/upload-release-assets.py"), str(dist), tag, "--repo", repo,
             "--require-existing", "--protect-published", "--workers", "1", "--attempts", "6",
             "--paced-github-token"], root=root, timeout=10800)
    execute([sys.executable, str(ROOT / "scripts/validate-release-assets.py"), str(dist), tag, "--repo", repo,
             "--timeout-seconds", "900", "--poll-seconds", "10"], root=root)
    builder.verify_download(dist, scope, root, repo, expected_commit)
    final_draft = P.companion_release(repo, tag)
    if P.tag_commit(repo, tag) != expected_commit or final_draft != draft:
        raise ValueError("Tag oder Releaseidentität hat sich während der Verifikation verändert")
    execute(["gh", "release", "edit", tag, "--repo", repo, "--draft=false", "--latest=false"], root=root)
    published = P.companion_release(repo, tag)
    if published is None or published.get("isDraft") is not False or P.tag_commit(repo, tag) != expected_commit:
        raise ValueError("Veröffentlichung konnte nicht bestätigt werden")
    print(json.dumps({"tag": tag, "commit": expected_commit, "assets": len(list(dist.iterdir())),
                      "download_verified": True, "published": True}, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--scope", type=Path, default=ROOT / "scripts/data/skill-quality-release-scope.json")
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--repo", default="Klotzkette/claude-fuer-deutsches-recht")
    args = parser.parse_args()
    publish(args.dist.resolve(), json.loads(args.scope.read_text()), args.expected_commit, args.repo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
