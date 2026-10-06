"""Small, bounded OGC adapter; uncertain geometry is never invented."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import io
import json
import math
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from defusedxml import ElementTree as ET
from PIL import Image
from pyproj import CRS, Transformer


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def local(tag):
    return tag.rsplit('}', 1)[-1]


def query(url, **params):
    p = urlsplit(url)
    keys = {key.lower() for key in params}
    values = [(key, value) for key, value in parse_qsl(p.query) if key.lower() not in keys]
    values.extend((key, str(value)) for key, value in params.items())
    return urlunsplit((p.scheme, p.netloc, p.path, urlencode(values), ''))


def xml(data):
    if len(data) > 8 * 1024 * 1024:
        raise ValueError('XML-Datei ist zu groß.')
    root = ET.fromstring(data, forbid_dtd=True, forbid_entities=True, forbid_external=True)
    if local(root.tag) in ('Exception', 'ServiceException', 'ExceptionReport', 'ServiceExceptionReport'):
        raise ValueError('Der Geodatendienst meldet einen Dienstfehler statt Nutzdaten.')
    return root


def bbox(value, geographic=True):
    result = [float(x) for x in (value.split(',') if isinstance(value, str) else value)]
    if len(result) != 4 or not all(math.isfinite(x) for x in result):
        raise ValueError('Ungültiger Kartenausschnitt.')
    w, s, e, n = result
    if w >= e or s >= n:
        raise ValueError('Kartenausschnitt ist leer oder umgekehrt.')
    if geographic and not (-180 <= w < e <= 180 and -90 <= s < n <= 90):
        raise ValueError('Kartenausschnitt liegt außerhalb gültiger Koordinaten.')
    if not geographic and max(abs(x) for x in result) > 21000000:
        raise ValueError('Kartenausschnitt liegt außerhalb der Kartenprojektion.')
    return result


def image_bytes(data):
    if data.lstrip().startswith(b'<'):
        xml(data)
        raise ValueError('Der Kartendienst lieferte XML statt eines Kartenbildes.')
    with Image.open(io.BytesIO(data)) as im:
        if im.format not in ('PNG', 'JPEG') or max(im.size) > 2048:
            raise ValueError('Unerwartetes Kartenbild.')
        im.load()
        bands = im.convert('RGB').getextrema()
        if all(low == high for low, high in bands):
            raise ValueError('Das Kartenbild enthält keine sichtbaren Kartendaten.')
        return 'image/png' if im.format == 'PNG' else 'image/jpeg'


def map_image(provider, extent, width, height, fetch):
    extent = bbox(extent, False)
    width, height = int(width), int(height)
    if not (32 <= width <= 1024 and 32 <= height <= 1024):
        raise ValueError('Unzulässige Bildgröße.')
    if provider.get('protocol', '').upper() != 'WMS':
        raise ValueError('Dieser Kartendienst ist nicht als WMS freigegeben.')
    data = fetch(query(provider['service_url'], SERVICE='WMS', VERSION='1.3.0', REQUEST='GetMap',
                       LAYERS=provider['layers'], STYLES='', CRS='EPSG:3857',
                       BBOX=','.join(map(str, extent)), WIDTH=width, HEIGHT=height,
                       FORMAT=provider.get('format', 'image/png'), TRANSPARENT='TRUE'), max_bytes=3 * 1024 * 1024)
    return data, image_bytes(data)


def verify_provider(provider, place, fetch):
    result = dict(provider, verified_at=now(), verification_state='gefunden_ungeprueft')
    result.setdefault('provider_id', hashlib.sha256(result['service_url'].encode()).hexdigest()[:16])
    protocol = result.get('protocol', '').upper()
    try:
        caps = xml(fetch(query(result['service_url'], SERVICE=protocol, REQUEST='GetCapabilities'), max_bytes=3 * 1024 * 1024))
        fees = [node.text.strip() for node in caps.iter() if local(node.tag) == 'Fees' and node.text and node.text.strip().lower() != 'none']
        result['license'] = fees[0] if fees else result.get('license', 'Lizenz gesondert prüfen')
        result['source_url'] = query(result['service_url'], SERVICE=protocol, REQUEST='GetCapabilities')
        if protocol == 'WMS':
            names = [n.text for n in caps.iter() if local(n.tag) == 'Name']
            if not result.get('layers') or any(layer not in names for layer in result['layers'].split(',')):
                raise ValueError('Der vorgesehene Kartenlayer fehlt in den Dienstmetadaten.')
            if not any(n.text == 'EPSG:3857' for n in caps.iter() if local(n.tag) in ('CRS', 'SRS')):
                raise ValueError('Die Kartenprojektion EPSG:3857 ist nicht veröffentlicht.')
            lat, lon = place['center']
            x, y = Transformer.from_crs(4326, 3857, always_xy=True).transform(lon, lat)
            map_image(result, [x-100, y-100, x+100, y+100], 128, 128, fetch)
            result['test_result'] = 'Metadaten und nicht leeres Kartenbild am gewählten Ort geprüft.'
        elif protocol == 'WFS':
            feature_type = result.get('type_name', 'ave:Flurstueck')
            if feature_type not in [n.text for n in caps.iter() if local(n.tag) == 'Name']:
                raise ValueError('Der Flurstücktyp fehlt in den Dienstmetadaten.')
            schema = xml(fetch(query(result['service_url'], SERVICE='WFS', VERSION='2.0.0', REQUEST='DescribeFeatureType', TYPENAMES=feature_type)))
            if not any(n.get('name') in ('geometrie', 'geometry', 'position') for n in schema.iter()):
                raise ValueError('Das Flurstückschema enthält keine unterstützte Geometrie.')
            result['type_name'] = feature_type
            lat, lon = place['center']
            probe = parcels(result, place, [lon-.001, lat-.001, lon+.001, lat+.001], 0, fetch, count=3)
            if not probe['features']:
                raise ValueError('Am gewählten Ort wurden keine zuordenbaren Flurstücke geliefert.')
            result['test_result'] = 'Metadaten, Flurstückschema und reale Geometrien am Ort geprüft.'
        else:
            raise ValueError('Dieser Dienst benötigt einen zusätzlichen, geprüften Adapter.')
        result['verification_state'] = 'verifiziert'
    except Exception as exc:
        result['verification_state'] = 'eingeschraenkt'
        result['test_result'] = str(exc)[:400]
    return result


def _ring(boundary, inherited_crs, inherited_dimension):
    lists = [n for n in boundary.iter() if local(n.tag) == 'posList']
    points = []
    if lists:
        for node in lists:
            dim = int(node.get('srsDimension', inherited_dimension))
            values = [float(x) for x in (node.text or '').split()]
            if dim not in (2, 3) or len(values) % dim:
                raise ValueError('Unvollständige GML-Koordinaten.')
            points.extend([values[i:i+2] for i in range(0, len(values), dim)])
    else:
        for node in boundary.iter():
            if local(node.tag) == 'pos':
                values = [float(x) for x in (node.text or '').split()]
                if len(values) not in (2, 3):
                    raise ValueError('Ungültige GML-Position.')
                points.append(values[:2])
            elif local(node.tag) == 'coordinates':
                points.extend([[float(x) for x in pair.split(',')[:2]] for pair in (node.text or '').split()])
    if len(points) < 4 or len(points) > 50000:
        raise ValueError('GML-Ring ist leer, zu kurz oder zu groß.')
    crs = CRS.from_user_input(inherited_crs)
    swap = bool(crs.axis_info and crs.axis_info[0].direction in ('north', 'south'))
    # Short EPSG:4326 is ambiguous in old GML: refuse rather than silently swap.
    if inherited_crs == 'EPSG:4326':
        raise ValueError('GML benötigt für EPSG 4326 eine eindeutige URN-Achsenangabe.')
    transform = Transformer.from_crs(crs, 4326, always_xy=True)
    output = []
    for a, b in points:
        lon, lat = transform.transform(b, a) if swap else transform.transform(a, b)
        if not math.isfinite(lon) or not math.isfinite(lat) or not (-180 <= lon <= 180 and -90 <= lat <= 90):
            raise ValueError('Transformierte Koordinate ist ungültig.')
        output.append([lon, lat])
    if output[0] != output[-1]:
        raise ValueError('GML-Ring ist nicht geschlossen.')
    return output


def geometry_gml(feature):
    parent = {child: node for node in feature.iter() for child in node}
    polygons = []
    for polygon in feature.iter():
        if local(polygon.tag) not in ('Polygon', 'PolygonPatch'):
            continue
        node, crs, dimension = polygon, None, '2'
        while node is not None:
            if crs is None and node.get('srsName'):
                crs = node.get('srsName')
            if node.get('srsDimension'):
                dimension = node.get('srsDimension')
            node = parent.get(node)
        if not crs:
            raise ValueError('GML-Geometrie ohne Koordinatenreferenzsystem.')
        exterior, interiors = [], []
        for boundary in polygon:
            if local(boundary.tag) in ('exterior', 'outerBoundaryIs'):
                exterior = _ring(boundary, crs, dimension)
            if local(boundary.tag) in ('interior', 'innerBoundaryIs'):
                interiors.append(_ring(boundary, crs, dimension))
        if not exterior:
            raise ValueError('Flurstück ohne äußeren Polygonring.')
        polygons.append([exterior] + interiors)
    if not polygons:
        raise ValueError('Keine unterstützte Flurstückgeometrie gefunden.')
    return {'type': 'MultiPolygon', 'coordinates': polygons}


def parse_features(data, provider, municipality_code=''):
    root = xml(data)
    if local(root.tag) != 'FeatureCollection':
        raise ValueError('Keine WFS-Flurstücksammlung.')
    features = []
    members = [node for node in root if local(node.tag) in ('member', 'featureMember')]
    if len(members) > 401:
        raise ValueError('Die Flurstückantwort ist zu groß.')
    for member in members:
        if not len(member):
            continue
        feature = member[0]
        fields = {local(n.tag): (n.text or '').strip() for n in feature if not len(n)}
        if municipality_code and fields.get('gmdschl') != municipality_code:
            continue
        official_id = fields.get('idflurst') or fields.get('flstkennz')
        if not official_id:
            raise ValueError('Flurstück ohne eindeutige amtliche Kennung.')
        identifier = f"{provider['provider_id']}:{official_id}"
        props = {new: fields.get(old, '') for new, old in {
            'municipality': 'gemeinde', 'municipality_code': 'gmdschl',
            'district_name': 'gemarkung', 'district_code': 'gemaschl', 'flur': 'flur',
            'numerator': 'flstnrzae', 'denominator': 'flstnrnen',
            'official_parcel_reference': 'flstkennz', 'area_value': 'flaeche',
            'location_text': 'lagebeztxt', 'source_date': 'aktualit',
        }.items()}
        props['area_value'] = float(props['area_value']) if props['area_value'] else None
        if props['area_value'] is not None and (not math.isfinite(props['area_value']) or props['area_value'] < 0):
            raise ValueError('Ungültige Flächenangabe des Dienstes.')
        props.update(stable_id=identifier, provider_id=provider['provider_id'], area_unit='m²',
                     source_url=provider['service_url'], retrieved_at=now(), identification_status='amtliche_flurstuecksdaten')
        features.append({'type': 'Feature', 'id': identifier, 'properties': props, 'geometry': geometry_gml(feature)})
    return features, len(members), root.get('numberMatched', 'unknown')


def parcels(provider, place, extent, page, fetch, count=400):
    w, s, e, n = bbox(extent)
    if e-w > .025 or n-s > .025:
        raise ValueError('Bitte näher heranzoomen. Flurstücke werden nur für kleine Ausschnitte geladen.')
    page = int(page)
    if not 0 <= page <= 4:
        raise ValueError('Bitte Ausschnitt verkleinern; höchstens fünf Seiten je Ausschnitt.')
    ags = place.get('municipality_code', '')
    if not re.fullmatch(r'\d{8}', ags):
        raise ValueError('Die amtliche Gemeindezuordnung ist noch nicht verifiziert.')
    url = query(provider['service_url'], SERVICE='WFS', VERSION='2.0.0', REQUEST='GetFeature',
                TYPENAMES=provider.get('type_name', 'ave:Flurstueck'), SRSNAME='urn:ogc:def:crs:EPSG::4326',
                BBOX=f'{s},{w},{n},{e},urn:ogc:def:crs:EPSG::4326', COUNT=count, STARTINDEX=page*count)
    features, returned, matched = parse_features(fetch(url, max_bytes=8*1024*1024), provider, ags)
    truncated = int(matched) > page*count + returned if str(matched).isdigit() else returned >= count
    return {'type': 'FeatureCollection', 'features': features, 'truncated': truncated,
            'next_page': page+1 if truncated and returned == count and page < 4 else None,
            'warnings': ['Ausschnitt enthält möglicherweise weitere Flurstücke; näher heranzoomen oder nächste Seite laden.'] if truncated else []}


def import_geometry(content, place):
    if not isinstance(content, str) or len(content.encode()) > 2*1024*1024:
        raise ValueError('Geometrieimport ist auf 2 MB begrenzt.')
    if content.lstrip().startswith('<'):
        features, _, _ = parse_features(content.encode(), {'provider_id': 'import', 'service_url': ''})
    else:
        raw = json.loads(content)
        if raw.get('crs'):
            raise ValueError('GeoJSON nur in WGS84 ohne abweichende CRS-Angabe importieren.')
        features = raw.get('features', []) if raw.get('type') == 'FeatureCollection' else [raw]
    if not 1 <= len(features) <= 200:
        raise ValueError('Import muss zwischen 1 und 200 Flurstücken enthalten.')
    output, points = [], [0]
    def position_tree(value, depth):
        if not isinstance(value, list) or not value or len(value) > 50000:
            raise ValueError('Ungültige Geometrie.')
        if depth == 0:
            points[0] += 1
            if points[0] > 50000 or len(value) not in (2, 3) or any(type(v) not in (int, float) or not math.isfinite(v) for v in value) or not (-180 <= value[0] <= 180 and -90 <= value[1] <= 90):
                raise ValueError('GeoJSON-Koordinate ist ungültig oder Import zu umfangreich.')
        else:
            for part in value:
                position_tree(part, depth-1)
            if depth == 1 and (len(value) < 4 or value[0] != value[-1]):
                raise ValueError('Polygonring muss geschlossen sein.')
    for i, feature in enumerate(features):
        g = feature.get('geometry') or {}
        kind = g.get('type')
        if kind not in ('Polygon', 'MultiPolygon'):
            raise ValueError('Nur Polygon- und MultiPolygon-Flurstücke sind importierbar.')
        position_tree(g.get('coordinates'), 2 if kind == 'Polygon' else 3)
        props = feature.get('properties') or {}
        raw_area = props.get('area_value')
        allowed = ('district_name', 'district_code', 'flur', 'numerator', 'denominator', 'official_parcel_reference', 'area_value', 'area_unit', 'location_text', 'source_date')
        props = {key: str(props.get(key, ''))[:500] for key in allowed}
        if isinstance(raw_area, bool):
            raise ValueError('Ungültige Fläche in den importierten Geodaten.')
        props['area_value'] = float(raw_area) if raw_area not in (None, '') else None
        if props['area_value'] is not None and (not math.isfinite(props['area_value']) or props['area_value'] < 0):
            raise ValueError('Ungültige Fläche in den importierten Geodaten.')
        identifier = 'import:' + hashlib.sha256(json.dumps(g, sort_keys=True).encode()).hexdigest()[:20]
        props.update(stable_id=identifier, provider_id='import', municipality=place.get('name', ''),
                     municipality_code=place.get('municipality_code', ''), source_url='', retrieved_at=now(), identification_status='manuell_ergaenzt')
        g = {'type': kind, 'coordinates': g['coordinates']}
        output.append({'type': 'Feature', 'id': identifier, 'geometry': g, 'properties': props})
    # Imports must meet the same geometry budgets as later previews and exports.
    from documents import validate_case
    validate_case({'selected_parcels': [dict(f['properties'], geometry=f['geometry']) for f in output]})
    return {'type': 'FeatureCollection', 'features': output, 'truncated': False, 'next_page': None,
            'warnings': ['Importierte Angaben sind nicht amtlich verifiziert. Gemeindezuordnung und Flurstückkennzeichen prüfen.']}
