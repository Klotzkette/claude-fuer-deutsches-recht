#!/usr/bin/env python3
"""Plugin-Nachauflagen bauen, prüfen und ihre veröffentlichten Downloads in den Nutzerseiten aktivieren."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen

from package_edition import activate_routes, edition_routes
from release_asset_common import read_checksums
from release_routing import RELEASE_BASE, REPOSITORY

ROOT = Path(__file__).resolve().parents[1]


def verify_public(publisher, routes, tags, commit):
    """Prüft für jede Gruppe Publikationsstatus, Git-Tag, Bestandsbeleg und alle GitHub-Assetdigests."""
    public = publisher.B.load_module("validate-public-downloads.py")
    for tag in tags:
        assets = public.public_assets(tag, public.github_cli_json)
        expected = {name for name, pair in routes.items() if pair[1] == tag}
        report_name, sums_name = publisher.B.REPORT, publisher.B.CHECKSUMS
        if set(assets) != expected | {report_name, sums_name} or publisher.P.tag_commit(REPOSITORY, tag) != commit:
            raise ValueError(f"{tag}: Unvollständiges Release oder abweichender Quellcommit")
        if any(row.get("state") != "uploaded" or not row.get("size") for row in assets.values()):
            raise ValueError(f"{tag}: Leere oder nicht hochgeladene Datei")
        with TemporaryDirectory() as directory:
            for name in (report_name, sums_name):
                request = Request(f"{RELEASE_BASE}/download/{tag}/{name}", headers={"User-Agent": "Paketabgleich"})
                with urlopen(request, timeout=60) as response:
                    data = response.read()
                if assets[name].get("digest") != "sha256:" + hashlib.sha256(data).hexdigest():
                    raise ValueError(f"{tag}/{name}: Öffentliche Prüfsumme weicht ab")
                (Path(directory) / name).write_bytes(data)
            sums = read_checksums(Path(directory) / sums_name)
            report = json.loads((Path(directory) / report_name).read_bytes())
        if (report["tag"] != tag or report["source_state"] != {"commit": commit, "clean": True}
                or set(sums) != expected | {report_name}):
            raise ValueError(f"{tag}: Bestandsnachweis oder Quellenbindung stimmt nicht")
        if any(assets[name].get("digest") != "sha256:" + digest for name, digest in sums.items()):
            raise ValueError(f"{tag}: Öffentliche Asset-Prüfsumme stimmt nicht mit der Freigabe überein")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tags", action="store_true", help="Vorgesehene Routengruppen als JSON ausgeben")
    parser.add_argument("--tag", help="Eine Versionsgruppe auswählen")
    parser.add_argument("--dist", type=Path, help="Leeres Ausgabe- oder vorhandenes Prüfverzeichnis")
    parser.add_argument("--expected-commit", help="Vollständiger geprüfter Main-Commit")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--verify", action="store_true", help="Vorhandene Dateien offline prüfen")
    mode.add_argument("--publish", action="store_true", help="Pakete bauen, hochladen und vollständig zurücklesen")
    mode.add_argument("--activate", action="store_true", help="Alle vier öffentlichen Ausgaben prüfen und verlinken")
    parser.add_argument("--repo", default=REPOSITORY)
    args = parser.parse_args()
    routes = edition_routes(ROOT)
    tags = sorted({tag for _, tag in routes.values()})
    if args.tag and args.tag not in tags:
        parser.error("Der ausgewählte Tag gehört nicht zum Ausgabeplan")
    if args.tags:
        print(json.dumps([args.tag] if args.tag else tags))
        return
    if (args.activate or args.publish) and not re.fullmatch(r"[a-f0-9]{40}", args.expected_commit or ""):
        parser.error("Veröffentlichung und Aktivierung benötigen den vollständigen geprüften Main-Commit")

    spec = importlib.util.spec_from_file_location("publisher", ROOT / "scripts/publish-skill-quality-release.py")
    publisher = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(publisher)
    if args.activate:
        if args.tag or args.dist or args.repo != REPOSITORY:
            parser.error("Die Aktivierung prüft gemeinsam alle Veröffentlichungen im Quellrepository")
        verify_public(publisher, routes, tags, args.expected_commit)
        print(f"{activate_routes(ROOT, routes)} aktive Dokumentations- und Routingdateien aktualisiert")
        return
    if not args.dist or not args.tag:
        parser.error("Tag und Zielverzeichnis erforderlich")
    builder = publisher.B
    scope = builder.paketpflege_scope(args.tag, ROOT)
    dist = args.dist.resolve()
    if args.verify:
        builder.validate_assets(dist, scope, ROOT, expected_commit=args.expected_commit)
        return
    builder.build(dist, scope, expected_commit=args.expected_commit)
    if args.publish:
        existing = publisher.P.companion_release(args.repo, args.tag)
        if existing and existing.get("isDraft") is False:
            if publisher.P.tag_commit(args.repo, args.tag) != args.expected_commit:
                raise ValueError("Das veröffentlichte Release gehört zu einem anderen Commit")
            builder.verify_download(dist, scope, ROOT, args.repo, args.expected_commit)
        else:
            publisher.publish(dist, scope, args.expected_commit, args.repo)


if __name__ == "__main__":
    main()
