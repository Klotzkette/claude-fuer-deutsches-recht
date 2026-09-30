#!/usr/bin/env python3
"""Canonical public BGH full-text URLs for modern civil decisions."""

from __future__ import annotations

import re
import string
from datetime import date


BGH_DOCKET_RE = re.compile(
    r"^(?P<senate>[IVX]+a?) (?P<register>ZR|ZB) (?P<number>\d+)/(?P<year>\d{2})$"
)
BGH_DOCUMENT_SUFFIX_RE = re.compile(r"^[A-Z]?$")
BGH_BASE = (
    "https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/"
    "Zivilsenate"
)


def canonical_bgh_pdf_url(docket: str, *, document_suffix: str = "") -> str:
    """Return the SharedDocs PDF URL for a modern, non-future docket.

    BGH SharedDocs may append one uppercase letter when several published
    documents share the same docket. The suffix belongs to the document URL,
    not to the docket itself.
    """
    if not isinstance(docket, str):
        raise ValueError(f"nicht unterstütztes BGH-Aktenzeichen: {docket!r}")
    match = BGH_DOCKET_RE.fullmatch(docket)
    if match is None:
        raise ValueError(f"nicht unterstütztes BGH-Aktenzeichen: {docket!r}")
    if not isinstance(document_suffix, str) or BGH_DOCUMENT_SUFFIX_RE.fullmatch(document_suffix) is None:
        raise ValueError(f"nicht unterstützter BGH-Dokumentsuffix: {document_suffix!r}")
    year = int(match.group("year"))
    full_year = 2000 + year
    if full_year > date.today().year:
        raise ValueError(
            f"historisches, mehrdeutiges oder zukünftiges BGH-Aktenzeichen: {docket!r}"
        )
    senate = match.group("senate")
    register = match.group("register")
    number = match.group("number").rjust(3, "_")
    filename = f"{senate}_{register}_{number}-{year:02d}{document_suffix}.pdf"
    return (
        f"{BGH_BASE}/{senate}_ZS/{full_year}/{filename}"
        "?__blob=publicationFile&v=1"
    )


def is_canonical_bgh_pdf_url(docket: str, url: object) -> bool:
    if not isinstance(url, str):
        return False
    try:
        return any(
            url == canonical_bgh_pdf_url(docket, document_suffix=suffix)
            for suffix in ("", *string.ascii_uppercase)
        )
    except ValueError:
        return False
