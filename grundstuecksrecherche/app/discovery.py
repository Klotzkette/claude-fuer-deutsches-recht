"""Amtliche Ortssuche und Quellenkandidaten; keine Karten- oder Eigentumspruefung.

Alle Netzaufrufe laufen ausschliesslich ueber fetch(url, max_bytes=, timeout=).
Metadatenlinks erweitern niemals die Netz-Allowlist. HTML ist nur Datenquelle.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import time
import unicodedata
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from defusedxml import ElementTree as ET


class DiscoveryError(ValueError):
    """Die Quelle erlaubt kein belastbares Rechercheergebnis."""


STATES = dict(zip(
    [f"{n:02d}" for n in range(1, 17)],
    ["Schleswig-Holstein", "Hamburg", "Niedersachsen", "Bremen",
    "Nordrhein-Westfalen", "Hessen", "Rheinland-Pfalz", "Baden-W\u00fcrttemberg",
     "Bayern", "Saarland", "Berlin", "Brandenburg", "Mecklenburg-Vorpommern",
     "Sachsen", "Sachsen-Anhalt", "Th\u00fcringen"],
))
NS = {"gmd": "http://www.isotc211.org/2005/gmd",
      "srv": "http://www.isotc211.org/2005/srv",
      "csw": "http://www.opengis.net/cat/csw/2.0.2"}
MAX_BYTES = 4_000_000


def load_catalogs():
    return json.loads(Path(__file__).with_name("catalogs.json").read_text(encoding="utf-8"))


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _url(base, **parameters):
    parts = urlsplit(base)
    keys = {key.casefold() for key in parameters}
    pairs = [(k, v) for k, v in parse_qsl(parts.query) if k.casefold() not in keys]
    return urlunsplit((parts.scheme, parts.netloc, parts.path,
                       urlencode(pairs + list(parameters.items())), ""))


def _read(fetch, url, max_bytes=MAX_BYTES, timeout=12):
    data = fetch(url, max_bytes=max_bytes, timeout=timeout)
    if not isinstance(data, bytes) or len(data) > max_bytes:
        raise DiscoveryError("Quellenantwort fehlt oder ist zu groß.")
    return data


def _json(fetch, url):
    try:
        data = json.loads(_read(fetch, url))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise DiscoveryError("Keine gültige GeoJSON-Antwort (möglicherweise OGC-Fehler).") from exc
    if not isinstance(data, dict) or data.get("type") != "FeatureCollection" or not isinstance(data.get("features"), list):
        raise DiscoveryError("Keine GeoJSON-FeatureCollection.")
    return data


def _xml(data):
    root = ET.fromstring(data, forbid_dtd=True, forbid_entities=True, forbid_external=True)
    if root.tag.rsplit("}", 1)[-1] in {"Exception", "ExceptionReport", "ServiceException", "ServiceExceptionReport"}:
        raise DiscoveryError("OGC-Dienst meldet einen Fehler statt Nutzdaten.")
    return root


def _bounds(value):
    if not isinstance(value, (list, tuple)) or len(value) != 4:
        return None
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in value):
        return None
    w, s, e, n = value
    return list(value) if -180 <= w < e <= 180 and -90 <= s < n <= 90 else None


def _overlaps(a, b):
    return a[0] <= b[2] and b[0] <= a[2] and a[1] <= b[3] and b[1] <= a[3]


def _normal(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def _query(value):
    if not isinstance(value, str):
        raise DiscoveryError("Bitte einen Gemeindenamen oder achtstelligen AGS eingeben.")
    value = " ".join(unicodedata.normalize("NFC", value).split())
    if not 2 <= len(value) <= 100 or any(ord(c) < 32 for c in value):
        raise DiscoveryError("Der Gemeindename muss 2 bis 100 Zeichen haben.")
    if any(c in value for c in "%_*\\<>"):
        raise DiscoveryError("Bitte ohne Suchoperatoren suchen.")
    return value


def search_places(query, fetch):
    """Gemeinden zur Laufzeit aus VG250; AGS immer unveraendert aus der Quelle.

    Bewusste Suche, keine Autocomplete-Schleife. Keine erfundenen Ersatzorte bei
    einem Ausfall. Landkreis wird mit einem gebuendelten amtlichen WFS-Abruf
    aufgeloest. Gemeindegrenzen sind nur generalisierte VG250-Grenzen.
    """
    query = _query(query)
    config = load_catalogs()["places"]
    literal = query.replace("'", "''")
    condition = f"ags = '{literal}'" if re.fullmatch(r"[0-9]{8}", query) else f"gen ILIKE '{literal}%'"
    urls = []
    features = []
    truncated = False
    try:
        # Prefixsuche bewahrt Muenster/Muenster (Hessen); enthaelt-Suche erst
        # ohne Praefixtreffer, damit kleine Trefferlimits keinen Ort verdraengen.
        for start in (0, 40):
            url = _url(config["service_url"], service="WFS", version="2.0.0",
                       request="GetFeature", typeNames=config["municipalities_type"],
                       outputFormat="application/json", srsName="EPSG:4326",
                       count=40, startIndex=start, cql_filter=condition, sortBy="gen A,ags A")
            payload = _json(fetch, url)
            urls.append(url)
            page = payload["features"]
            features.extend((f, url) for f in page)
            if len(page) < 40:
                break
            truncated = start == 40
        if not features and not query.isdigit():
            url = _url(url, cql_filter=f"gen ILIKE '%{literal}%'", startIndex=0)
            payload = _json(fetch, url)
            urls.append(url)
            features = [(f, url) for f in payload["features"]]
            truncated = len(features) == 40
    except Exception as exc:
        raise DiscoveryError("Amtliche BKG-Ortssuche derzeit nicht verfügbar; bitte später erneut suchen.") from exc

    candidates = {}
    for feature, feature_url in features:
        if not isinstance(feature, dict):
            continue
        props = feature.get("properties") or {}
        if not isinstance(props, dict):
            continue
        ags, name = props.get("ags"), props.get("gen")
        bounds = _bounds(feature.get("bbox"))
        if not isinstance(ags, str) or not re.fullmatch(r"[0-9]{8}", ags) or ags[:2] not in STATES:
            continue
        if re.fullmatch(r"[0-9]{8}", query) and ags != query:
            continue
        if not isinstance(name, str) or not name.strip() or not bounds:
            continue
        # VG250 liefert u.a. Land- und Wasserflaechen separat mit derselben AGS.
        if ags in candidates:
            old = candidates[ags]["bounds"]
            candidates[ags]["bounds"] = [min(old[0], bounds[0]), min(old[1], bounds[1]),
                                         max(old[2], bounds[2]), max(old[3], bounds[3])]
            continue
        candidates[ags] = {
            "id": "ags:" + ags, "name": name, "state": STATES[ags[:2]],
            "state_code": ags[:2], "district": "", "municipality_code": ags,
            "bounds": bounds, "source_url": feature_url, "source_urls": urls,
            "verification_state": "amtlich_verifiziert", "verified_at": _now(),
            "data_date": props.get("wsk") or props.get("beginn") or "",
            "attribution": config["attribution"], "license": config["license"],
            "warnings": [],
        }
    districts = {}
    district_url = ""
    if candidates:
        codes = sorted({a[:5] for a in candidates})
        district_url = _url(config["service_url"], service="WFS", version="2.0.0",
                            request="GetFeature", typeNames=config["districts_type"],
                            outputFormat="application/json", propertyName="gen,ags,bez",
                            count=160, cql_filter="ags IN (" + ",".join(f"'{c}'" for c in codes) + ")")
        try:
            for f in _json(fetch, district_url)["features"]:
                p = f.get("properties") or {}
                if p.get("ags") in codes and isinstance(p.get("gen"), str):
                    districts[p["ags"]] = p["gen"]
        except Exception:
            pass
    for ags, candidate in candidates.items():
        w, s, e, n = candidate["bounds"]
        candidate["center"] = [(s + n) / 2, (w + e) / 2]
        candidate["center_method"] = "Mittelpunkt der generalisierten Gemeinde-Bounding-Box, kein Amtssitz"
        candidate["district"] = districts.get(ags[:5], "")
        candidate["district_source_url"] = district_url if candidate["district"] else ""
        if not candidate["district"]:
            candidate["warnings"].append("Kreiszuordnung derzeit nicht abrufbar; amtlichen Kreis prüfen.")
        if truncated or len(candidates) > 40:
            candidate["warnings"].append("Trefferliste begrenzt; Suche mit vollständigem Gemeindenamen oder AGS verfeinern.")
    return sorted(candidates.values(), key=lambda p: (_normal(p["name"]) != _normal(query), _normal(p["name"]), p["municipality_code"]))[:40]


def _text(node, path):
    found = node.find(path, NS)
    return " ".join(" ".join(found.itertext()).split())[:3000] if found is not None else ""


def _metadata_bounds(record):
    result = []
    for box in record.findall(".//gmd:EX_GeographicBoundingBox", NS):
        try:
            values = [float(_text(box, "gmd:" + n)) for n in
                      ("westBoundLongitude", "southBoundLatitude", "eastBoundLongitude", "northBoundLatitude")]
            if _bounds(values):
                result.append(values)
        except ValueError:
            continue
    return result


def _service_url(raw):
    try:
        p = urlsplit(raw)
        if p.scheme != "https" or not p.hostname or p.username or p.password or p.port not in (None, 443):
            return ""
        if any(ord(c) < 33 for c in raw):
            return ""
        transient = {"service", "request", "version", "layers", "typenames", "typename", "bbox",
                     "width", "height", "format", "srs", "crs", "styles", "count", "outputformat"}
        pairs = [(k, v) for k, v in parse_qsl(p.query) if k.casefold() not in transient]
        return urlunsplit((p.scheme, p.netloc, p.path, urlencode(pairs), ""))
    except ValueError:
        return ""


def _role(title):
    title = _normal(title)
    if any(word in title for word in ("flurst", "alkis", "cadastral", "katasterparzellen")):
        return "parcels"
    if any(word in title for word in ("orthophoto", "orthofoto", "dop", "luftbild")):
        return "aerial"
    if any(word in title for word in ("basiskarte", "webatlas", "topplus", "topographische", "basemap")):
        return "base"
    return None


def _csw_records(root, query_url, place):
    providers, contacts = [], []
    for record in root.findall(".//gmd:MD_Metadata", NS):
        title = _text(record, ".//gmd:identificationInfo//gmd:title")
        role = _role(title)
        boxes = _metadata_bounds(record)
        if not role or (boxes and not any(_overlaps(b, place["bounds"]) for b in boxes)):
            continue
        identifier = _text(record, "gmd:fileIdentifier")
        source = _url(urlunsplit((*urlsplit(query_url)[:3], "", "")), service="CSW", version="2.0.2",
                      request="GetRecordById", id=identifier, elementSetName="full", outputSchema=NS["gmd"]) if identifier else query_url
        attribution = _text(record, ".//gmd:identificationInfo//gmd:organisationName")
        license_text = _text(record, ".//gmd:resourceConstraints//gmd:otherConstraints") or _text(record, ".//gmd:resourceConstraints//gmd:useLimitation")
        online = record.findall(".//gmd:distributionInfo//gmd:CI_OnlineResource", NS)
        online += record.findall(".//srv:connectPoint/gmd:CI_OnlineResource", NS)
        for resource in online:
            raw = _text(resource, "gmd:linkage/gmd:URL")
            service_url = _service_url(raw)
            if not service_url:
                continue
            params = {k.lower(): v for k, v in parse_qsl(urlsplit(raw).query)}
            hint = (_text(resource, "gmd:protocol") + " " + params.get("service", "")).upper()
            protocol = "WFS" if "WFS" in hint else "WMS" if "WMS" in hint else "OGCAPI" if "OGC:API" in hint or "OGCAPI" in hint else None
            if not protocol:
                continue
            identity = f"{service_url}|{protocol}|{role}|{params.get('layers', '')}|{params.get('typenames', '')}"
            providers.append({
                "provider_id": "csw-" + hashlib.sha256(identity.encode()).hexdigest()[:16],
                "title": title, "role": role, "protocol": protocol,
                "service_url": service_url, "layers": params.get("layers", ""),
                "type_name": params.get("typenames", params.get("typename", "")),
                "version": params.get("version", ""), "crs": "", "axis_order": "",
                "license": license_text or "Lizenz in Dienstmetadaten zu prüfen",
                "attribution": attribution, "catalog_source_url": source,
                "verification_state": "gefunden_ungeprueft",
                "coverage": {"bounds": boxes, "verification_state": "metadatenangabe" if boxes else "zu_pruefen"},
            })
        # Ein Metadatenkontakt ist kein Nachweis oertlicher Auskunftszustaendigkeit.
        for party in record.findall(".//gmd:pointOfContact/gmd:CI_ResponsibleParty", NS):
            name = _text(party, "gmd:organisationName")
            if name:
                contacts.append({"kind": "metadata_contact", "official_name": name,
                                 "source_url": source, "verification_state": "zu_pruefen",
                                 "note": "Datenkontakt, keine bestätigte Kataster- oder Grundbuchzuständigkeit."})
    return providers, contacts


class _Page(HTMLParser):
    """Nur Text und semantische Adressbloecke, niemals aktiven Inhalt auswerten."""

    def __init__(self, data):
        super().__init__(convert_charrefs=True)
        self.parts, self.headings, self.addresses = [], [], []
        self.skip = 0
        self.capture = None
        self.feed(data.decode("utf-8", errors="replace"))

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if not self.skip and tag in ("h6", "address"):
            self.capture = (tag, [])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if self.capture and tag == self.capture[0]:
            target = self.headings if tag == "h6" else self.addresses
            target.append(" ".join(self.capture[1]))
            self.capture = None

    def handle_data(self, data):
        if not self.skip and data.strip():
            text = " ".join(data.split())
            self.parts.append(text)
            if self.capture:
                self.capture[1].append(text)

    @property
    def text(self):
        return " ".join(self.parts)


def _empty_authority(kind, url=""):
    return {"authority_type": kind, "official_name": "", "postal_address": "", "visitor_address": "",
            "evidence_urls": [url] if url else [], "verification_state": "zu_pruefen",
            "verified_at": None, "submission_information": "Zuständigkeit, Anschrift und Einreichungsweg amtlich prüfen."}


def _authorities(place, fetch, config, evidence, warnings):
    profiles = config.get("authority_profiles", {}).get(place["municipality_code"], [])
    authorities = []
    for profile in profiles:
        candidate = {k: v for k, v in profile.items() if k not in ("checks", "type")}
        candidate["authority_type"] = profile["type"]
        candidate.update(evidence_urls=[c["url"] for c in profile["checks"]],
                         verification_state="zu_pruefen", verified_at=None)
        valid = True
        for check in profile["checks"]:
            try:
                page = _Page(_read(fetch, check["url"], max_bytes=1_000_000, timeout=8))
                found = all(_normal(t) in _normal(page.text) for t in check["required_text"])
                valid = valid and found
                evidence.append({"kind": "authority_page", "source_url": check["url"],
                                 "checked_at": _now(), "verification_state": "belegt" if found else "zu_pruefen"})
            except Exception:
                valid = False
        if valid:
            candidate.update(verification_state="amtlich_verifiziert", verified_at=_now())
        else:
            candidate["submission_information"] = "Referenzangaben konnten aktuell nicht vollständig bestätigt werden. Vor Versand erneut amtlich prüfen."
            warnings.append(f"{profile['type']}: Referenzangaben aktuell nicht vollständig verifiziert.")
        authorities.append(candidate)
    if not any(a["authority_type"] == "grundbuch" for a in authorities):
        directory = config["authority_directory"]
        url = _url(directory["service_url"], ang=directory["subject"], plzort=place["name"])
        candidate = _empty_authority("grundbuch", url)
        try:
            page = _Page(_read(fetch, url, max_bytes=1_000_000, timeout=8))
            courts = [h for h in page.headings if "grundbuch" in h.casefold()]
            postal = [a.removeprefix("Postanschrift").strip() for a in page.addresses if a.startswith("Postanschrift")]
            visitors = [a.removeprefix("Lieferanschrift").strip() for a in page.addresses if a.startswith("Lieferanschrift")]
            matched = _normal("Grundbuchsachen, " + place["name"]) in _normal(page.text)
            ambiguous = any(s in _normal(page.text) for s in ("mehrere treffer", "mehrere gerichte", "bitte verfeinern"))
            if matched and not ambiguous and len(courts) == len(postal) == len(visitors) == 1 and postal[0] and visitors[0]:
                candidate.update(official_name=courts[0], postal_address=postal[0], visitor_address=visitors[0],
                                 verification_state="amtlich_verifiziert", verified_at=_now(),
                                 submission_information="Amtliches Orts- und Gerichtsverzeichnis, Angelegenheit Grundbuchsachen. Konkreten Einreichungsweg bei diesem Gericht prüfen; keine Freigabe für gewöhnliche E-Mail.")
            else:
                warnings.append("Grundbuchzuständigkeit nicht eindeutig; amtliche Ortssuche anhand der konkreten Grundstückslage verfeinern.")
            evidence.append({"kind": "authority_directory", "source_url": url,
                             "checked_at": _now(), "verification_state": candidate["verification_state"]})
        except Exception:
            warnings.append("Amtliches Orts- und Gerichtsverzeichnis derzeit nicht abrufbar.")
        authorities.append(candidate)
    if not any(a["authority_type"] == "kataster" for a in authorities):
        authorities.insert(0, _empty_authority("kataster"))
        warnings.append("Zuständige Katasterauskunft noch offen; Datenanbieter oder Metadatenkontakt ist nicht automatisch die Auskunftsbehörde.")
    return authorities


def discover(place, fetch):
    """Begrenzte CSW-Recherche und regionale Seeds, alle Provider unaktiviert.

    Nicht gefundene Dienste bedeuten keine negative Vollabdeckungsfeststellung.
    Der Aufrufer muss place aus search_places uebernehmen, nicht aus Fremd-JSON.
    """
    if not isinstance(place, dict) or not re.fullmatch(r"[0-9]{8}", str(place.get("municipality_code", ""))):
        raise DiscoveryError("Eine amtlich identifizierte Gemeinde mit achtstelliger AGS ist erforderlich.")
    if not isinstance(place["municipality_code"], str) or not _bounds(place.get("bounds")):
        raise DiscoveryError("AGS muss eine Zeichenkette sein; gültige Gemeindegrenzen sind erforderlich.")
    _query(place.get("name"))
    config = load_catalogs()
    deadline = time.monotonic() + 35
    original_fetch = fetch

    def fetch(url, *, max_bytes=MAX_BYTES, timeout=8):
        remaining = deadline - time.monotonic()
        if remaining <= 0.1:
            raise TimeoutError("Zeitbudget für Quellenrecherche aufgebraucht.")
        return original_fetch(url, max_bytes=max_bytes, timeout=min(timeout, remaining))

    code = place["municipality_code"][:2]
    providers = [p for p in config["providers"] if not p["coverage"]["state_codes"] or code in p["coverage"]["state_codes"]]
    # Regionale Basiskarten zuerst; bundesweite Basiskarte bleibt Rueckfalloption.
    providers.sort(key=lambda p: not bool(p["coverage"]["state_codes"]))
    evidence, warnings = [], []
    for catalog in config["catalogs"]:
        # OGC BBOX ist lon/lat. Nur oeffentliche Ortsangaben verlassen den Server.
        w, s, e, n = place["bounds"]
        constraint = ("(Title LIKE '%ALKIS%' OR Title LIKE '%Flurst%' OR Title LIKE '%Orthophoto%' "
                      "OR Title LIKE '%Basiskarte%' OR Title LIKE '%WebAtlas%') "
                      f"AND BBOX(ows:BoundingBox,{w},{s},{e},{n})")
        start = 1
        for page_number in range(catalog["max_pages"]):
            url = _url(catalog["service_url"], service="CSW", version="2.0.2", request="GetRecords",
                       resultType="results", typeNames="csw:Record", elementSetName="full",
                       outputSchema=NS["gmd"], constraintLanguage="CQL_TEXT", constraint_language_version="1.1.0",
                       constraint=constraint, maxRecords=catalog["max_records"], startPosition=start)
            try:
                root = _xml(_read(fetch, url, timeout=catalog["timeout"]))
                results = root.find("csw:SearchResults", NS)
                if root.tag != "{" + NS["csw"] + "}GetRecordsResponse" or results is None:
                    raise DiscoveryError("Keine gültige CSW-Ergebnisliste.")
                found, contacts = _csw_records(root, url, place)
                providers.extend(found)
                evidence.extend(contacts)
                evidence.append({"kind": "catalog_query", "source_url": url, "checked_at": _now(),
                                 "matched": results.get("numberOfRecordsMatched"),
                                 "returned": results.get("numberOfRecordsReturned"), "verification_state": "abgerufen"})
                next_record = int(results.get("nextRecord", "0"))
                if next_record <= start:
                    break
                start = next_record
                if page_number == catalog["max_pages"] - 1:
                    warnings.append("Katalogrecherche begrenzt; weitere Metadatentreffer können vorhanden sein.")
            except Exception as exc:
                warnings.append(f"{catalog['title']}: Abfrage derzeit fehlgeschlagen ({type(exc).__name__}). Die Katalogrecherche ist unvollständig; den gesonderten Prüfstatus der verfügbaren Dienste beachten.")
                evidence.append({"kind": "catalog_query", "source_url": url, "checked_at": _now(), "verification_state": "nicht_verfuegbar"})
                break
    unique = {}
    for p in providers:
        p["verification_state"] = "gefunden_ungeprueft"
        parts = urlsplit(p["service_url"])
        p["requires_host_approval"] = not any(parts.path == prefix or parts.path.startswith(prefix.rstrip("/") + "/") for prefix in
                                             config["allowed_hosts"].get(parts.hostname, []))
        service_key = (p["service_url"], p["protocol"], p["role"])
        resource = p.get("layers") or p.get("type_name") or ""
        if not resource and any(k[:3] == service_key for k in unique):
            continue
        unique.setdefault((*service_key, resource), p)
    authorities = _authorities(place, fetch, config, evidence, warnings)
    if not any(p["role"] == "parcels" and p["protocol"] in ("WFS", "OGCAPI") for p in unique.values()):
        warnings.append("Keine Flurstücksvektoren gefunden. Amtliche manuelle Eingabe oder Import erforderlich; keine bundesweite Flurstücksabdeckung.")
    return {"providers": list(unique.values()), "authorities": authorities,
            "evidence": evidence, "warnings": warnings}
