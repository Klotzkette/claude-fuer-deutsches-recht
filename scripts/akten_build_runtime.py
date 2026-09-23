"""Portable Werkzeuge für die native Erzeugung der sechs Wirtschaftsmandate."""

import os
from pathlib import Path
import shutil

from PIL import ImageFont


def node_binary():
    configured = os.environ.get("AKTEN_NODE", "").strip()
    binary = shutil.which(configured or "node")
    if not binary:
        raise RuntimeError("Node.js fehlt. node im PATH bereitstellen oder AKTEN_NODE setzen.")
    return binary


def screen_font(size, bold=False):
    names = (
        ("Arial Bold.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf")
        if bold else
        ("Arial.ttf", "arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf")
    )
    directories = []
    if os.environ.get("AKTEN_FONT_DIR"):
        directories.append(Path(os.environ["AKTEN_FONT_DIR"]).expanduser())
    directories.extend([
        Path("/System/Library/Fonts/Supplemental"),
        Path("/usr/share/fonts/truetype/dejavu"),
        Path("/usr/share/fonts/truetype/liberation2"),
        Path("/usr/share/fonts/truetype/liberation"),
        Path("/usr/share/fonts/truetype/msttcorefonts"),
        Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts",
    ])
    for directory in directories:
        for name in names:
            candidate = directory / name
            if candidate.is_file():
                try:
                    return ImageFont.truetype(str(candidate), size)
                except OSError:
                    continue
    raise RuntimeError("Bildschrift fehlt. DejaVu Sans oder Liberation Sans installieren oder AKTEN_FONT_DIR setzen.")
