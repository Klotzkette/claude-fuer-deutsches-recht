"""Render README navigation against the contents of an installable plugin package."""
from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit, urlunsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

REPOSITORY = "https://github.com/Klotzkette/claude-fuer-deutsches-recht"
MAIN_LINK = re.compile(re.escape(REPOSITORY) + r"/(?:tree|blob)/main/")
# Keep the source Markdown, including code examples, labels, optional titles,
# angle brackets, query strings and fragments. Replace only the destination.
TOKENS = re.compile(
    r"(?P<fence>^ {0,3}(?P<marker>`{3,}|~{3,})[^\n]*\n.*?^ {0,3}(?P=marker)[`~]*[ \t]*\r?$)"
    r"|(?P<comment><!--.*?-->)|(?P<code>(?P<ticks>`+).*?(?P=ticks))"
    r"|(?P<start>\]\([ \t]*|^ {0,3}\[[^\]\n]+\]:[ \t]*)(?P<dest><[^<>\n]*>|(?:[^\s()<>]|\([^\s()<>]*\))+)",
    re.M | re.S,
)


def render_readme(root: Path, directory: Path, members, commit: str | None, *, name: str = "README.md") -> bytes | None:
    """Use local links for shipped files or directories, commit links for omitted targets."""
    names = {name.rstrip("/") for name in members}
    if name not in names:
        return None
    root, directory = root.resolve(), directory.resolve()
    readme = (directory / name).resolve()
    if readme.name != "README.md" or not readme.is_relative_to(directory):
        raise ValueError(f"Ungültiger README-Pfad: {name}")
    directories = {parent.as_posix() for name in names for parent in PurePosixPath(name).parents}

    def replace(match):
        raw = match["dest"]
        if raw is None:
            return match[0]
        angle = raw.startswith("<")
        dest = raw[1:-1] if angle else raw
        main = MAIN_LINK.match(dest)
        parts = urlsplit(dest[main.end():] if main else dest)
        if parts.scheme or parts.netloc or not parts.path:
            return match[0]
        path = unquote(parts.path)
        if path.startswith("/") or "\\" in path:
            raise ValueError(f"Ungültiges README-Ziel in {directory.name}: {dest}")
        target = ((root if main else readme.parent) / path).resolve()
        if not target.is_relative_to(root):
            raise ValueError(f"README-Ziel außerhalb des Repositorys: {dest}")
        local = target.relative_to(directory).as_posix() if target.is_relative_to(directory) else None
        if local in names or local in directories:
            if not main and ".." not in path.split("/"):
                return match[0]
            new_path = quote(Path(os.path.relpath(target, readme.parent)).as_posix(), safe="/")
        else:
            if not target.exists():
                raise ValueError(f"README-Ziel im Repository fehlt: {dest}")
            if not commit or not re.fullmatch(r"[a-f0-9]{40}", commit):
                raise ValueError("Externer Paketverweis benötigt den vollständigen Git-Commit")
            view = "tree" if target.is_dir() else "blob"
            source = quote(target.relative_to(root).as_posix(), safe="/")
            new_path = f"{REPOSITORY}/{view}/{commit}"
            if target != root:
                new_path += f"/{source}"
        new = urlunsplit(("", "", new_path, parts.query, parts.fragment))
        return match["start"] + (f"<{new}>" if angle else new)

    return TOKENS.sub(replace, readme.read_bytes().decode("utf-8")).encode("utf-8")


def add_to_archive(archive_path: Path, root: Path, directory: Path, commit: str):
    with ZipFile(archive_path, "a") as archive:
        names = archive.namelist()
        if "README.md" in names:
            raise ValueError(f"Paket enthält bereits einen README-Eintrag: {archive_path}")
        info = ZipInfo.from_file(directory / "README.md", "README.md")
        data = render_readme(root, directory, [*names, "README.md"], commit)
        archive.writestr(info, data, compress_type=ZIP_DEFLATED)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    add_to_archive(args.archive, repo, args.directory, commit)
