import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'app'))
from PIL import Image
from ogc import bbox, geometry_gml, image_bytes, import_geometry, parcels, parse_features, xml
from secure_net import FetchError, PublicFetcher


GML = '''<w:FeatureCollection xmlns:w="http://www.opengis.net/wfs/2.0" xmlns:g="http://www.opengis.net/gml/3.2" numberMatched="unknown">
<w:member><Flurstueck><idflurst>ID001</idflurst><gmdschl>05515000</gmdschl><flstkennz>05500100100001______</flstkennz><geometrie>
<g:MultiSurface srsName="urn:ogc:def:crs:EPSG::4326"><g:surfaceMember><g:Polygon>
<g:exterior><g:LinearRing><g:posList>51 7 51 8 52 8 51 7</g:posList></g:LinearRing></g:exterior>
<g:interior><g:LinearRing><g:posList>51.1 7.2 51.1 7.3 51.2 7.3 51.1 7.2</g:posList></g:LinearRing></g:interior>
</g:Polygon></g:surfaceMember><g:surfaceMember><g:Polygon><g:exterior><g:LinearRing><g:posList>51 9 51 10 52 10 51 9</g:posList></g:LinearRing></g:exterior></g:Polygon></g:surfaceMember></g:MultiSurface>
</geometrie></Flurstueck></w:member></w:FeatureCollection>'''


class OgcTests(unittest.TestCase):
    def test_axis_holes_multipart_and_stable_id(self):
        features, returned, _ = parse_features(GML.encode(), {'provider_id': 'nrw', 'service_url': 'https://example.org/wfs'}, '05515000')
        self.assertEqual(returned, 1)
        self.assertEqual(features[0]['id'], 'nrw:ID001')
        geometry = features[0]['geometry']['coordinates']
        self.assertEqual(len(geometry), 2)
        self.assertEqual(len(geometry[0]), 2)
        self.assertEqual(geometry[0][0][0], [7, 51])
        self.assertEqual(geometry[0][1][0], [7.2, 51.1])

    def test_municipality_filter(self):
        features, _, _ = parse_features(GML.encode(), {'provider_id': 'nrw', 'service_url': ''}, '12345678')
        self.assertFalse(features)

    def test_entity_exception_and_no_geometry(self):
        for data in ('<!DOCTYPE x [<!ENTITY x SYSTEM "file:///etc/passwd">]><x>&x;</x>', '<ExceptionReport><Exception>Denied</Exception></ExceptionReport>'):
            with self.assertRaises(Exception):
                xml(data.encode())
        with self.assertRaises(ValueError):
            geometry_gml(xml(b'<x/>'))

    def test_ambiguous_crs_rejected(self):
        with self.assertRaises(ValueError):
            parse_features(GML.replace('urn:ogc:def:crs:EPSG::4326', 'EPSG:4326').encode(), {'provider_id': 'x', 'service_url': ''})

    def test_bounded_query_and_truncated(self):
        called = []
        def fetch(url, **kwargs):
            called.append(url)
            return GML.encode()
        provider = {'provider_id': 'nrw', 'service_url': 'https://example.org/wfs'}
        place = {'municipality_code': '05515000'}
        result = parcels(provider, place, [7, 51, 7.001, 51.001], 0, fetch, count=1)
        self.assertTrue(result['truncated'])
        self.assertEqual(result['next_page'], 1)
        self.assertIn('BBOX=51.0%2C7.0', called[0])
        for bounds in ([7, 51, 9, 52], [8, 51, 7, 52], [7, 51, float('nan'), 52]):
            with self.assertRaises(ValueError):
                parcels(provider, place, bounds, 0, fetch)
        with self.assertRaises(ValueError):
            parcels(provider, place, [7, 51, 7.001, 51.001], 5, fetch)

    def test_import_no_owners_or_script_fields(self):
        content = {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[7, 51], [8, 51], [8, 52], [7, 51]]]}, 'properties': {'owner': 'Unverifiziert', 'district_name': '<img src=x onerror=alert(1)>'}}
        result = import_geometry(json.dumps(content), {'name': 'Münster'})
        self.assertNotIn('owner', result['features'][0]['properties'])
        self.assertEqual(result['features'][0]['properties']['identification_status'], 'manuell_ergaenzt')
        content['geometry']['coordinates'][0][-1] = [7, 52]
        with self.assertRaises(ValueError):
            import_geometry(json.dumps(content), {})

    def test_short_server_page_does_not_claim_completeness_or_skip_rows(self):
        result = parcels({'provider_id': 'nrw', 'service_url': 'https://example.org/wfs'},
                         {'municipality_code': '05515000'}, [7, 51, 7.001, 51.001], 0,
                         lambda *a, **kw: GML.replace('numberMatched="unknown"', 'numberMatched="1000"').encode())
        self.assertTrue(result['truncated'])
        self.assertIsNone(result['next_page'])
        self.assertTrue(result['warnings'])

    def test_import_null_area_extra_geometry_fields_and_export_parity(self):
        from documents import validate_case
        content = {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[7, 51], [8, 51], [8, 52], [7, 51]]], 'bbox': [7, 51, 8, 52]}, 'properties': {'area_value': None}}
        result = import_geometry(json.dumps(content), {})
        feature = result['features'][0]
        self.assertIsNone(feature['properties']['area_value'])
        self.assertNotIn('bbox', feature['geometry'])
        validate_case({'selected_parcels': [dict(feature['properties'], geometry=feature['geometry'])]})
        self.assertEqual(len(import_geometry(GML, {})['features']), 1)

    def test_xml_not_map_and_blank_not_map(self):
        self.assertEqual(xml(b'<WMS_Capabilities><Exception><Format>XML</Format></Exception></WMS_Capabilities>').tag, 'WMS_Capabilities')
        with self.assertRaises(ValueError):
            image_bytes(b'<ExceptionReport/>')
        im = Image.new('RGB', (32, 32), 'white')
        buffer = io.BytesIO()
        im.save(buffer, format='PNG')
        with self.assertRaises(ValueError):
            image_bytes(buffer.getvalue())
        im.putpixel((0, 0), (0, 0, 0))
        buffer = io.BytesIO()
        im.save(buffer, format='PNG')
        self.assertEqual(image_bytes(buffer.getvalue()), 'image/png')


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.fetch = PublicFetcher({'example.org': ['/wfs']})

    def test_disallowed_urls(self):
        for url in ('http://example.org/wfs', 'https://localhost/wfs', 'https://example.org/admin', 'https://user:pass@example.org/wfs', 'https://example.org:444/wfs', 'https://example.org/wfs/../private', 'https://example.org/wfs/%2e%2e/private', 'https://example.org.evil.org/wfs'):
            with self.subTest(url=url), self.assertRaises(FetchError):
                self.fetch.validate(url)

    @patch('secure_net.socket.getaddrinfo')
    def test_private_dns_and_mixed_public_private_rejected(self, dns):
        for addresses in (['127.0.0.1'], ['169.254.169.254'], ['::1'], ['8.8.8.8', '10.0.0.1']):
            dns.return_value = [(2, 1, 6, '', (address, 443)) for address in addresses]
            with self.assertRaises(FetchError):
                self.fetch.validate('https://example.org/wfs')

    @patch('secure_net.socket.getaddrinfo')
    def test_public_address_retained(self, dns):
        dns.return_value = [(2, 1, 6, '', ('8.8.8.8', 443))]
        self.assertEqual(self.fetch.validate('https://example.org/wfs')[3], ['8.8.8.8'])

    def test_cache_size_bound(self):
        self.fetch.max_cache_bytes = 6
        with patch.object(self.fetch, '_fetch', return_value=b'1234'):
            self.fetch('https://example.org/wfs?a=1')
            self.fetch('https://example.org/wfs?a=2')
        self.assertEqual(self.fetch.cache_bytes, 4)
        self.assertEqual(len(self.fetch.cache), 1)


if __name__ == '__main__':
    unittest.main()
