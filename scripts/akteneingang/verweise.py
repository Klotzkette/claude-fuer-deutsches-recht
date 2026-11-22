"""Stabile Verweise auf die vollständigen Grundakten und deren thematische Lesepakete."""

from __future__ import annotations

from functools import lru_cache
from release_routing import scoped_asset_url

from .quellen import URL, catalogs
from .vertiefung import TAG as FACHTAG
from .vertiefung import fachredaktion

TAG = "grundakten-lebenswelt-v1.0.0"


def routes(records):
    ordered = sorted(
        (record.get("id", key.split("/")[-1]), key) for key, record in records.items()
    )
    if len(dict(ordered)) != len(ordered):
        raise ValueError("Nicht eindeutiger Ausgabename")
    return {
        key: (slug, f"lesepaket-{n // 15 + 1:02d}.zip")
        for n, (slug, key) in enumerate(ordered)
    }


@lru_cache(maxsize=1)
def all_routes():
    return routes(catalogs())


@lru_cache(maxsize=1)
def fachpfade():
    return frozenset(fachredaktion())


def links(key, historisch=False):
    slug, group = all_routes()[key]
    if not historisch and key in fachpfade():
        base = URL + FACHTAG + "/"
        native = f"lebensakte-{slug}.zip"
        printed = f"druckakte-{slug}.zip"
        return (
            f"[Arbeits-ZIP mit Eingangspost]({scoped_asset_url(native) or base + native})",
            f"[Druckfassungen dieses Falls]({scoped_asset_url(printed) or base + printed})",
        )
    base = URL + TAG + "/"
    return (
        f"[Arbeits-ZIP mit Eingangspost]({base}lebensakte-{slug}.zip)",
        f"[Druckpaket {group[10:12]}]({base}{group})",
    )


def central_row(slug, columns=3, historisch=False):
    key = "testakten/" + slug
    if key not in all_routes():
        return ""
    native, group = links(key, historisch)
    label = "Vollakte mit Eingangspost"
    return (
        f"| **{label}** | ZIP | {native} · {group} |"
        if columns == 3
        else f"| **{label}** | {native} · {group} |"
    )
