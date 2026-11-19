"""Vollständige Originalakten mit einer gesondert austeilbaren Belegnachlieferung."""
import argparse
from email import policy
from email.parser import BytesParser
import importlib
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / "docs/workshops/insolvenzreife-nachlieferungen"
CASES = {"CB": "keramikfabrik-cottbus", "BZ": "metallbau-berlin-zehlendorf", "PR": "hubschrauber-prenzlau"}
writer = importlib.import_module("build-testakten-release-zips")


def documents(code, slug):
    base = ROOT / "testakten" / ("insolvenzreife-" + slug)
    files = dict((name, path) for path, name in working_dump_archive_pairs(base, include_gesamt_pdf=False))
    supplement = EDITION / "quellen" / code
    reply = BytesParser(policy=policy.default).parsebytes((supplement / "02_Antwort.eml").read_bytes())
    attachments = {part.get_filename(): part.get_payload(decode=True) for part in reply.iter_attachments()}
    loose = {p.name: p.read_bytes() for p in supplement.iterdir() if p.suffix != ".eml"}
    if attachments != loose or len(loose) != 2:
        raise ValueError(f"{code}: Antwortanlagen und lose Ausfertigungen stimmen nicht überein")
    for path in sorted(supplement.iterdir()):
        files["Nachlieferung/" + path.name] = path
    return files


def verify(target, files):
    with ZipFile(target) as z:
        if (z.namelist() != [NOTICE_FILENAME, *files] or z.testzip()
                or z.read(NOTICE_FILENAME) != NOTICE_BYTES):
            raise ValueError(f"Unvollständige Ausgabe: {target.name}")
        for name, source in files.items():
            if z.read(name) != source.read_bytes():
                raise ValueError(f"Geänderte Originaldatei: {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=EDITION / "downloads")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        args.dist.mkdir(parents=True, exist_ok=True)
    for code, slug in CASES.items():
        files = documents(code, slug)
        target = args.dist / f"{slug}-mit-nachlieferung.zip"
        if not args.verify:
            with TemporaryDirectory(dir=args.dist) as temp:
                work = Path(temp) / target.name
                with ZipFile(work, "x") as z:
                    writer.write_bytes(z, NOTICE_BYTES, NOTICE_FILENAME)
                    for name, path in files.items():
                        writer.write_file(z, path, name)
                verify(work, files)
                work.replace(target)
        else:
            verify(target, files)
        print(f"{code}: {len(files)} Originaldateien, davon vier im späteren Eingang")


if __name__ == "__main__":
    main()
