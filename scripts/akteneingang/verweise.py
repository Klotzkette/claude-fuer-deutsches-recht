"""Stabile Verweise auf die vollständigen Grundakten und deren thematische Lesepakete."""

from __future__ import annotations

from functools import lru_cache

from .quellen import URL, catalogs

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


def links(key):
    slug, group = all_routes()[key]
    base = URL + TAG + "/"
    return (
        f"[Arbeits-ZIP mit Eingangspost]({base}lebensakte-{slug}.zip)",
        f"[Druckpaket {group[10:12]}]({base}{group})",
    )


def central_row(slug, columns=3):
    key = "testakten/" + slug
    if key not in all_routes():
        return ""
    native, group = links(key)
    label = "Vollakte mit Eingangspost"
    return (
        f"| **{label}** | ZIP | {native} · {group} |"
        if columns == 3
        else f"| **{label}** | {native} · {group} |"
    )
