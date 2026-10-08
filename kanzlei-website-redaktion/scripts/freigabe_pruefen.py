#!/usr/bin/env python3
"""Prüft lokale Freigabedaten; verbindet sich nicht mit einer Website."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit


def fassungs_hash(publication: dict, transparency: dict) -> str:
    data = json.dumps({"publication": publication, "transparency": transparency}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def ausgefuellt(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def pruefen(data: dict) -> dict:
    errors = []
    if not isinstance(data, dict):
        return {"formal_vollstaendig": False, "fehler": ["JSON-Objekt erforderlich"]}
    publication = data.get("publication")
    if not isinstance(publication, dict):
        return {"formal_vollstaendig": False, "fehler": ["publication fehlt"]}
    digest = fassungs_hash(publication, data.get("transparency"))
    for name in ("request_id", "target_url", "base_revision", "body"):
        if not ausgefuellt(publication.get(name)):
            errors.append(f"publication.{name} fehlt")
    try:
        url = urlsplit(publication.get("target_url", ""))
        if url.scheme != "https" or not url.hostname or url.username or url.password or url.fragment:
            errors.append("Ziel muss eine eindeutige HTTPS-URL ohne Zugangsdaten oder Fragment sein")
    except (ValueError, TypeError, AttributeError):
        errors.append("Ungültige Ziel-URL")
    if not isinstance(publication.get("media"), list):
        errors.append("publication.media muss eine Liste sein")
    else:
        for media in publication["media"]:
            if not isinstance(media, dict) or not ausgefuellt(media.get("file")) or not isinstance(media.get("sha256"), str) or len(media["sha256"]) != 64 or any(c not in "0123456789abcdef" for c in media["sha256"]):
                errors.append("Medien benötigen Datei und SHA256 der konkreten Veröffentlichungskopie")
    checks = data.get("checks")
    if not isinstance(checks, dict):
        checks = {}
    for key in ("sources", "personal_data", "rights", "preview"):
        if checks.get(key) is not True:
            errors.append(f"Bestätigung fehlt: checks.{key}")

    transparency = data.get("transparency")
    if not isinstance(transparency, dict):
        transparency = {}
    for key in ("generated_text", "public_interest", "deepfake"):
        if type(transparency.get(key)) is not bool:
            errors.append(f"Transparenzeinordnung offen: {key}")
    if not ausgefuellt(transparency.get("reason")):
        errors.append("Begründung der Transparenzeinordnung fehlt")
    review = data.get("human_review")
    if not isinstance(review, dict):
        review = {}
    reviewed = (review.get("content_hash") == digest and all(ausgefuellt(review.get(k)) for k in ("reviewer", "at", "scope", "editorial_responsible")))
    release = data.get("release")
    if not isinstance(release, dict):
        release = {}
    if transparency.get("generated_text") is True and transparency.get("public_interest") is True and not reviewed:
        if not ausgefuellt(publication.get("text_disclosure")):
            errors.append("Ohne belegte Textausnahme fehlt der sichtbare Texthinweis")
        if release.get("allow_unreviewed_publication") is not True:
            errors.append("Kanzleiregel: ungeprüfter öffentlicher Informationstext bleibt Entwurf")
    if transparency.get("deepfake") is True and not ausgefuellt(publication.get("media_disclosure")):
        errors.append("Deepfake-Offenlegung fehlt; Textprüfung ersetzt sie nicht")
    if release.get("approved") is not True or not all(ausgefuellt(release.get(k)) for k in ("by", "at")):
        errors.append("Konkrete Veröffentlichungsfreigabe fehlt")
    if release.get("content_hash") != digest:
        errors.append("Freigabe gehört nicht zur aktuellen Fassung samt Ziel und Medien")
    return {"formal_vollstaendig": not errors, "content_hash": digest, "fehler": errors,
            "grenze": "Selbstauskünfte, keine rechtliche Prüfung oder Zugangserlaubnis. Tatsächliche Kontrolle, Rechte, Medienbytes, Hinweisposition und Zielrevision separat verifizieren. Kein Versand und keine Veröffentlichung."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("datei", type=Path)
    args = parser.parse_args()
    try:
        if args.datei.stat().st_size > 1_000_000:
            raise ValueError("Freigabedatei überschreitet ein Megabyte")
        result = pruefen(json.loads(args.datei.read_text(encoding="utf-8")))
    except (OSError, ValueError, RecursionError) as error:
        print(json.dumps({"formal_vollstaendig": False, "fehler": [str(error)]}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["formal_vollstaendig"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
