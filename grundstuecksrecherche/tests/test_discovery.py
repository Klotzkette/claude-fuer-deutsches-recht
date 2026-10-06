"""Deterministische Adaptertests; nur RUN_LIVE_DISCOVERY=1 nutzt das Netz.

Live-Pruefung 2026-10-06, ca. 16:43-16:55 UTC (keine Dauerzusage):
1. BKG WFS VG250: GetCapabilities, DescribeFeatureType und GetFeature mit
   GeoJSON/EPSG:4326 erfolgreich. Suchen nach Muenster (mehrere echte Gemeinden),
   Hannover 03241001, Berlin 11000000, Leipzig 14713000 und Freiburg im Breisgau
   08311000 lieferten AGS, Bounds und amtlich nachgeladene Kreisnamen.
2. NRW: Capabilities ABK/nw_abk_col, DOP/nw_dop_rgb und ALKIS/ave:Flurstueck
   bestaetigt; alle drei nennen aktuell dl-de/zero-2-0. Keine Uebernahme der
   veralteten Lizenz der Referenz. Diese Tests aktivieren keinen Kartenprovider.
3. Sachsen: WebAtlas (sechs Layer), DOP/sn_dop_020 und ALKIS/ave:Flurstueck
   Capabilities erfolgreich. Berlin: alkis_flurstuecke:flurstuecke erfolgreich
   mit curl/Systemvertrauen; Python-Runtime meldete ein Zertifikatskettenproblem.
   Keine TLS-Pruefung wurde abgeschaltet. GetMap/Flurstuecksauswahl gehoeren
   zur separaten OGC-Pruefung, nicht zu diesen Adapter-Livebefunden.
4. Muenster: Kataster-Startseite, Beleg der Postanschrift, AG-Kontakt,
   Gerichtsbezirk, Grundbuchamtsseite und E-Mail-Hinweis live abgeglichen.
   Alte /katasteramt/kontakt (404) und /abteilungen/Grundbuch (410) verworfen.
5. Bundesweites amtliches Orts-/Gerichtsverzeichnis mit ang=grundbuch:
   Leipzig -> AG Leipzig Grundbuchamt, Hannover -> AG Hannover Grundbuchamt,
   Freiburg -> AG Emmendingen Grundbuchamt. Post- und Lieferanschrift getrennt.
   Berlin -> mehrere Treffer, offen geblieben. Kataster ausser Muenster offen.
6. GDI-DE CSW /gdi-de/srv/ger/csw: GetRecords ISO-19139 anfangs erfolgreich
   (AnyText ALKIS: numberOfRecordsMatched=18812, maxRecords=2); nachfolgende
   raeumliche/ortsbezogene und einfache Queries Timeout. Laufzeitwarnung und
   regionale Seeds nachgewiesen, keine erfolgreiche Vollrecherche behauptet.
   discover inkl. Suche: Muenster 11.68 s, Leipzig 8.66 s, Berlin 8.90 s,
   Hannover 8.61 s, Freiburg 8.62 s. Transport: curl mit TLS-Pruefung.
7. Niedersachsen/BW: BKG-Basiskartenkandidat; keine live nachgewiesenen
   Flurstuecksvektoren in diesem Adapter. Manueller Ersatz bleibt erforderlich.
8. CSW-Diagnose ca. 17:00 UTC mit PublicFetcher: GetCapabilities HTTP 200,
   20.519 Bytes, 1.83 s; keine Weiterleitung. GetRecords mit reinem BBOX-Filter
   nach 10 s TimeoutError als Ursache von FetchError. Derselbe Request mit
   curl nach 10 s ebenfalls ohne Antwortheader. Kein Allowlist-/Groessenfehler.
9. RUN_LIVE_DISCOVERY=1 mit PublicFetcher: alle 32 damaligen Tests erfolgreich,
   45.159 s insgesamt; fuenf Laender inklusive Kreisnachladen und discover.
   Auch ungefiltertes CSW-GetRecords und FILTER/XML waren spaeter im Timeout.
"""

import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
import discovery as d


PLACE = {"id": "ags:05515000", "name": "M\u00fcnster", "municipality_code": "05515000",
         "state": "Nordrhein-Westfalen", "bounds": [7.474, 51.8402, 7.7742, 52.0602],
         "verification_state": "amtlich_verifiziert"}


def feature(name="M\u00fcnster", ags="05515000", bounds=None):
    return {"type": "Feature", "id": str(ags), "properties": {"ags": ags, "gen": name},
            "bbox": bounds or [7.474, 51.8402, 7.7742, 52.0602],
            "geometry": {"type": "MultiPolygon", "coordinates": []}}


def collection(features):
    return json.dumps({"type": "FeatureCollection", "features": features}).encode()


def csw(records="", next_record=0):
    return (f'<csw:GetRecordsResponse xmlns:csw="{d.NS["csw"]}" '
            f'xmlns:gmd="{d.NS["gmd"]}" xmlns:srv="{d.NS["srv"]}" '
            'xmlns:gco="http://www.isotc211.org/2005/gco">'
            f'<csw:SearchResults numberOfRecordsMatched="2" numberOfRecordsReturned="1" '
            f'nextRecord="{next_record}">{records}</csw:SearchResults></csw:GetRecordsResponse>').encode()


def record(url="https://unknown.example/wfs?service=WFS&amp;typeNames=test:parcel", west=7, east=8):
    return f'''<gmd:MD_Metadata>
      <gmd:fileIdentifier><gco:CharacterString>record-123</gco:CharacterString></gmd:fileIdentifier>
      <gmd:identificationInfo><gmd:MD_DataIdentification>
        <gmd:citation><gmd:CI_Citation><gmd:title><gco:CharacterString>ALKIS Flurstuecke</gco:CharacterString></gmd:title></gmd:CI_Citation></gmd:citation>
        <gmd:pointOfContact><gmd:CI_ResponsibleParty><gmd:organisationName><gco:CharacterString>Metadatenbetrieb</gco:CharacterString></gmd:organisationName></gmd:CI_ResponsibleParty></gmd:pointOfContact>
        <gmd:extent><gmd:EX_Extent><gmd:geographicElement><gmd:EX_GeographicBoundingBox>
          <gmd:westBoundLongitude><gco:Decimal>{west}</gco:Decimal></gmd:westBoundLongitude>
          <gmd:eastBoundLongitude><gco:Decimal>{east}</gco:Decimal></gmd:eastBoundLongitude>
          <gmd:southBoundLatitude><gco:Decimal>51</gco:Decimal></gmd:southBoundLatitude>
          <gmd:northBoundLatitude><gco:Decimal>53</gco:Decimal></gmd:northBoundLatitude>
        </gmd:EX_GeographicBoundingBox></gmd:geographicElement></gmd:EX_Extent></gmd:extent>
      </gmd:MD_DataIdentification></gmd:identificationInfo>
      <gmd:distributionInfo><gmd:MD_Distribution><gmd:transferOptions><gmd:MD_DigitalTransferOptions>
        <gmd:onLine><gmd:CI_OnlineResource><gmd:linkage><gmd:URL>{url}</gmd:URL></gmd:linkage>
          <gmd:protocol><gco:CharacterString>OGC:WFS</gco:CharacterString></gmd:protocol>
        </gmd:CI_OnlineResource></gmd:onLine>
      </gmd:MD_DigitalTransferOptions></gmd:transferOptions></gmd:MD_Distribution></gmd:distributionInfo>
    </gmd:MD_Metadata>'''


def court_page(name="Leipzig", court="Amtsgericht Leipzig - Grundbuchamt -"):
    return (f'<main>Gesucht wurde: <strong>Grundbuchsachen, {name}</strong>'
            f'<h6>{court}</h6><address><strong>Lieferanschrift</strong><br>Schongauerstrasse 5<br>04328 Leipzig</address>'
            '<address><strong>Postanschrift</strong><br>04174 Leipzig</address></main>').encode()


class FakeFetch:
    def __init__(self, features=None, records=None, html=None):
        self.features = features if features is not None else [feature()]
        self.records = records if records is not None else csw()
        self.html = html if html is not None else b"<html>Keine eindeutige Behoerde</html>"
        self.calls = []

    def __call__(self, url, **kwargs):
        self.calls.append((url, kwargs))
        p = parse_qs(urlsplit(url).query)
        if p.get("typeNames") == ["vg250:vg250_gem"]:
            return collection(self.features)
        if p.get("typeNames") == ["vg250:vg250_krs"]:
            return collection([{"properties": {"ags": "05515", "gen": "M\u00fcnster"}},
                               {"properties": {"ags": "06432", "gen": "Darmstadt-Dieburg"}}])
        if urlsplit(url).path.endswith("/csw"):
            return self.records
        return self.html


class PlacesTests(unittest.TestCase):
    def test_real_ags_ambiguity_and_axis_order(self):
        fetch = FakeFetch([feature(), feature("M\u00fcnster (Hessen)", "06432015")])
        places = d.search_places("M\u00fcnster", fetch)
        self.assertEqual([p["municipality_code"] for p in places], ["05515000", "06432015"])
        self.assertEqual(places[0]["id"], "ags:05515000")
        self.assertEqual(places[1]["district"], "Darmstadt-Dieburg")
        self.assertAlmostEqual(places[0]["center"][0], 51.9502)
        self.assertAlmostEqual(places[0]["center"][1], 7.6241)
        self.assertIn("sgx.geodatenzentrum.de", places[0]["source_url"])
        self.assertTrue(all("max_bytes" in args and "timeout" in args for _, args in fetch.calls))

    def test_exact_ags_keeps_leading_zero_and_rejects_unrelated_feature(self):
        fetch = FakeFetch([feature(), feature("Hannover", "03241001")])
        places = d.search_places("05515000", fetch)
        self.assertEqual(len(places), 1)
        self.assertEqual(parse_qs(urlsplit(fetch.calls[0][0]).query)["cql_filter"], ["ags = '05515000'"])

    def test_numeric_or_missing_ags_is_never_invented(self):
        fetch = FakeFetch([feature(ags=5515000), feature(ags="5515000"), feature(ags="00000000"), feature(ags=None)])
        self.assertEqual(d.search_places("Teststadt", fetch), [])

    def test_missing_or_invalid_geometry_bounds_not_silently_guessed(self):
        a, b, c = feature(), feature(), feature()
        del a["bbox"]
        b["bbox"] = [7, 51, float("nan"), 52]
        c["bbox"] = [8, 51, 7, 52]
        self.assertEqual(d.search_places("Teststadt", FakeFetch([a, b, c])), [])

    def test_land_and_water_parts_merge_by_ags(self):
        places = d.search_places("M\u00fcnster", FakeFetch([feature(), feature(bounds=[7.7, 51.9, 7.9, 52.1])]))
        self.assertEqual(len(places), 1)
        self.assertEqual(places[0]["bounds"], [7.474, 51.8402, 7.9, 52.1])

    def test_xml_http_200_is_not_a_place(self):
        with self.assertRaises(d.DiscoveryError):
            d.search_places("Muenster", lambda *a, **kw: b"<ExceptionReport>Denied</ExceptionReport>")

    def test_offline_no_hardcoded_city_fallback(self):
        def fail(*args, **kwargs):
            raise TimeoutError()
        with self.assertRaises(d.DiscoveryError):
            d.search_places("Muenster", fail)

    def test_query_validation_precedes_fetch(self):
        for query in ("", "x", "a" * 101, "%", "xx*", "<script>", None):
            fetch = FakeFetch()
            with self.assertRaises(d.DiscoveryError):
                d.search_places(query, fetch)
            self.assertFalse(fetch.calls)

    def test_cql_quote_is_escaped(self):
        fetch = FakeFetch()
        d.search_places("O'Brien", fetch)
        self.assertEqual(parse_qs(urlsplit(fetch.calls[0][0]).query)["cql_filter"], ["gen ILIKE 'O''Brien%'"])

    def test_district_failure_is_explicit(self):
        fetch = FakeFetch()
        def wrapped(url, **kwargs):
            if "vg250_krs" in url:
                raise TimeoutError()
            return fetch(url, **kwargs)
        p = d.search_places("Muenster", wrapped)[0]
        self.assertEqual(p["district"], "")
        self.assertTrue(p["warnings"])

    def test_pagination_bounded_and_truncated(self):
        fetch = FakeFetch([feature(f"Test {i}", f"05515{i:03d}") for i in range(40)])
        places = d.search_places("Test", fetch)
        self.assertEqual(len(fetch.calls), 3)
        self.assertEqual(len(places), 40)
        self.assertTrue(any("begrenzt" in w for w in places[0]["warnings"]))


class DiscoveryTests(unittest.TestCase):
    def test_region_restriction_and_unverified_contract(self):
        for code, expected in (("05515000", "nrw-alkis"), ("14713000", "sn-alkis"), ("11000000", "be-alkis"), ("03241001", None)):
            result = d.discover(dict(PLACE, municipality_code=code), FakeFetch())
            ids = {p["provider_id"] for p in result["providers"]}
            self.assertIn("bkg-topplus-open", ids)
            if expected:
                self.assertIn(expected, ids)
            if code[:2] != "05":
                self.assertNotIn("nrw-alkis", ids)
            self.assertTrue(all(p["verification_state"] == "gefunden_ungeprueft" for p in result["providers"]))
            self.assertEqual({"providers", "authorities", "evidence", "warnings"}, set(result))

    def test_official_csw_getrecords_not_fake_search_link(self):
        fetch = FakeFetch()
        d.discover(dict(PLACE, private_reason="SECRET-REASON"), fetch)
        calls = [u for u, _ in fetch.calls if "/csw?" in u]
        params = parse_qs(urlsplit(calls[0]).query)
        self.assertEqual(params["request"], ["GetRecords"])
        self.assertEqual(params["outputSchema"], [d.NS["gmd"]])
        self.assertIn("BBOX(ows:BoundingBox,7.474,51.8402,7.7742,52.0602)", params["constraint"][0])
        self.assertNotIn("SECRET-REASON", " ".join(u for u, _ in fetch.calls))

    def test_metadata_unknown_host_retained_but_never_fetched(self):
        fetch = FakeFetch(records=csw(record()))
        result = d.discover(PLACE, fetch)
        p = next(p for p in result["providers"] if p["provider_id"].startswith("csw-"))
        self.assertTrue(p["requires_host_approval"])
        self.assertEqual(p["type_name"], "test:parcel")
        self.assertEqual(p["service_url"], "https://unknown.example/wfs")
        self.assertEqual(p["crs"], "")
        self.assertEqual(p["axis_order"], "")
        self.assertEqual(p["verification_state"], "gefunden_ungeprueft")
        self.assertFalse(any("unknown.example" in u for u, _ in fetch.calls))
        self.assertNotIn("constraint", parse_qs(urlsplit(p["catalog_source_url"]).query))

    def test_metadata_contact_not_promoted_to_competent_authority(self):
        result = d.discover(dict(PLACE, municipality_code="03241001"), FakeFetch(records=csw(record())))
        contact = next(e for e in result["evidence"] if e["kind"] == "metadata_contact")
        self.assertEqual(contact["verification_state"], "zu_pruefen")
        self.assertFalse(any(a["official_name"] == "Metadatenbetrieb" for a in result["authorities"]))

    def test_outside_coverage_discarded(self):
        result = d.discover(PLACE, FakeFetch(records=csw(record(west=12, east=13))))
        self.assertFalse(any(p["provider_id"].startswith("csw-") for p in result["providers"]))

    def test_wms_only_does_not_claim_parcel_vectors(self):
        data = record("https://unknown.example/wms?service=WMS&amp;layers=parcel").replace("OGC:WFS", "OGC:WMS")
        result = d.discover(dict(PLACE, municipality_code="03241001"), FakeFetch(records=csw(data)))
        self.assertTrue(any(p["role"] == "parcels" and p["protocol"] == "WMS" for p in result["providers"]))
        self.assertTrue(any("Keine Flurstücksvektoren" in w for w in result["warnings"]))

    def test_distinct_layers_on_one_service_survive_deduplication(self):
        a = record("https://unknown.example/wfs?service=WFS&amp;typeNames=test:a")
        b = record("https://unknown.example/wfs?service=WFS&amp;typeNames=test:b")
        result = d.discover(PLACE, FakeFetch(records=csw(a + b)))
        self.assertEqual({p["type_name"] for p in result["providers"] if p["provider_id"].startswith("csw-")}, {"test:a", "test:b"})

    def test_insecure_service_links_are_not_providers(self):
        for url in ("http://example.org/wfs", "file:///etc/passwd", "https://user:pass@example.org/wfs", "https://example.org:444/wfs"):
            result = d.discover(PLACE, FakeFetch(records=csw(record(url))))
            self.assertFalse(any(p["provider_id"].startswith("csw-") for p in result["providers"]))

    def test_no_xxe_dtd_or_xml_error_acceptance(self):
        for data in (b'<!DOCTYPE x [<!ENTITY x SYSTEM "file:///etc/passwd">]><x>&x;</x>',
                     b'<ExceptionReport><Exception>Denied</Exception></ExceptionReport>', b'<html>Upstream error</html>'):
            result = d.discover(PLACE, FakeFetch(records=data))
            self.assertTrue(any("fehlgeschlagen" in w for w in result["warnings"]))
            self.assertTrue(any(e["verification_state"] == "nicht_verfuegbar" for e in result["evidence"]))

    def test_capabilities_exception_format_is_not_error(self):
        root = d._xml(b'<WMS_Capabilities><Capability><Exception><Format>XML</Format></Exception></Capability></WMS_Capabilities>')
        self.assertEqual(root.tag, "WMS_Capabilities")

    def test_csw_pagination_bounded(self):
        fetch = FakeFetch(records=csw(record(), next_record=13))
        result = d.discover(PLACE, fetch)
        self.assertEqual(len([u for u, _ in fetch.calls if "/csw?" in u]), 2)
        self.assertEqual(len([p for p in result["providers"] if p["provider_id"].startswith("csw-")]), 1)

    def test_budget_exhaustion_prevents_additional_fetch(self):
        fetch = FakeFetch()
        with patch.object(d.time, "monotonic", side_effect=[0] + [36] * 10):
            result = d.discover(PLACE, fetch)
        self.assertFalse(fetch.calls)
        self.assertTrue(result["warnings"])

    def test_oversized_transport_rejected(self):
        with self.assertRaises(d.DiscoveryError):
            d._read(lambda *a, **kw: b"1234", "https://example.org", max_bytes=3)

    def test_invalid_place_no_fetch(self):
        for place in ({}, dict(PLACE, municipality_code=5515000), dict(PLACE, bounds=[8, 51, 7, 52])):
            fetch = FakeFetch()
            with self.assertRaises(d.DiscoveryError):
                d.discover(place, fetch)
            self.assertFalse(fetch.calls)

    def test_allowlist_is_explicit_and_seeds_covered(self):
        config = d.load_catalogs()
        self.assertIsInstance(config["allowed_hosts"], dict)
        for provider in config["providers"]:
            u = urlsplit(provider["service_url"])
            self.assertIn(u.path, config["allowed_hosts"][u.hostname])
        self.assertNotIn("unknown.example", config["allowed_hosts"])


class AuthoritiesTests(unittest.TestCase):
    def test_runtime_official_directory_not_hardcoded_city_menu(self):
        place = dict(PLACE, name="Leipzig", municipality_code="14713000")
        fetch = FakeFetch(html=court_page())
        result = d.discover(place, fetch)
        authority = next(a for a in result["authorities"] if a["authority_type"] == "grundbuch")
        self.assertEqual(authority["official_name"], "Amtsgericht Leipzig - Grundbuchamt -")
        self.assertEqual(authority["postal_address"], "04174 Leipzig")
        self.assertIn("04328", authority["visitor_address"])
        self.assertEqual(authority["verification_state"], "amtlich_verifiziert")
        self.assertTrue(authority["verified_at"])
        self.assertIn("plzort=Leipzig", authority["evidence_urls"][0])
        self.assertNotIn("type", authority)

    def test_freiburg_may_resolve_to_different_city_court(self):
        place = dict(PLACE, name="Freiburg im Breisgau", municipality_code="08311000")
        result = d.discover(place, FakeFetch(html=court_page(place["name"], "Amtsgericht Emmendingen - Grundbuchamt -")))
        self.assertIn("Emmendingen", result["authorities"][1]["official_name"])

    def test_ambiguous_incomplete_or_wrong_search_stays_open(self):
        for html in (court_page() + b"mehrere Treffer", b"<h6>Amtsgericht Test - Grundbuchamt -</h6>", court_page("Anderer Ort")):
            result = d.discover(dict(PLACE, name="Leipzig", municipality_code="14713000"), FakeFetch(html=html))
            authority = result["authorities"][1]
            self.assertEqual(authority["verification_state"], "zu_pruefen")
            self.assertEqual(authority["official_name"], "")
            self.assertIsNone(authority["verified_at"])

    def test_muenster_requires_all_evidence_pages_not_http_200_alone(self):
        result = d.discover(PLACE, FakeFetch(html=b"<html>OK</html>"))
        self.assertTrue(all(a["verification_state"] == "zu_pruefen" for a in result["authorities"]))
        self.assertTrue(all(a["verified_at"] is None for a in result["authorities"]))

    def test_muenster_profile_verified_only_after_content_match(self):
        checks = {c["url"]: c["required_text"] for p in d.load_catalogs()["authority_profiles"]["05515000"] for c in p["checks"]}
        fetch = FakeFetch()
        def verified(url, **kwargs):
            if url in checks:
                return ("<main>" + " ".join(checks[url]) + "</main>").encode()
            return fetch(url, **kwargs)
        result = d.discover(PLACE, verified)
        self.assertTrue(all(a["verification_state"] == "amtlich_verifiziert" for a in result["authorities"]))
        self.assertTrue(all(a["verified_at"] for a in result["authorities"]))

    def test_script_cannot_satisfy_authority_check(self):
        page = d._Page(b"<script>Amtliches Grundbuchamt</script><main>Wartung</main>")
        self.assertEqual(page.text, "Wartung")

    def test_profile_not_mutated_between_places(self):
        first = d.discover(PLACE, FakeFetch())
        first["providers"][0]["verification_state"] = "verifiziert"
        second = d.discover(PLACE, FakeFetch())
        self.assertEqual(second["providers"][0]["verification_state"], "gefunden_ungeprueft")


@unittest.skipUnless(os.environ.get("RUN_LIVE_DISCOVERY") == "1", "Expliziter Liveabruf erforderlich")
class LiveDiscoveryTests(unittest.TestCase):
    def test_five_states_with_secure_fetch(self):
        from secure_net import PublicFetcher
        fetch = PublicFetcher(d.load_catalogs()["allowed_hosts"])
        for query, code in (("M\u00fcnster", "05515000"), ("Hannover", "03241001"),
                            ("Berlin", "11000000"), ("Leipzig", "14713000"),
                            ("Freiburg im Breisgau", "08311000")):
            with self.subTest(query=query):
                candidates = d.search_places(query, fetch)
                place = next(p for p in candidates if p["municipality_code"] == code)
                self.assertTrue(place["district"])
                result = d.discover(place, fetch)
                self.assertTrue(result["providers"])
                self.assertTrue(all(p["verification_state"] == "gefunden_ungeprueft" for p in result["providers"]))
                self.assertEqual({a["authority_type"] for a in result["authorities"]}, {"kataster", "grundbuch"})


if __name__ == "__main__":
    unittest.main()
