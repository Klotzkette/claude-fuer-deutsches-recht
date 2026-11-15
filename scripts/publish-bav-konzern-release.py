#!/usr/bin/env python3
"""bAV-Komponente mit den bestehenden unveränderten Veröffentlichungsschranken."""
from pathlib import Path
import argparse
import importlib.util


def load(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--repo", default="Klotzkette/claude-fuer-deutsches-recht")
    args = parser.parse_args()
    builder = load("build-bav-konzern-release.py")
    publisher = load("publish-skill-quality-release.py")
    publisher.publish(args.dist.resolve(), builder.SCOPE, args.expected_commit, args.repo, builder=builder)


if __name__ == "__main__":
    main()
