#!/usr/bin/env python3
"""Local-only map application; no mailbox, credentials or account required."""

from __future__ import annotations

import argparse
import collections
from concurrent.futures import ThreadPoolExecutor
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
from pathlib import Path
import secrets
import threading
import time
from urllib.parse import parse_qs, unquote, urlsplit

from discovery import search_places, discover
from documents import build_documents, export_document, validate_case
from ogc import bbox, import_geometry, map_image, parcels, query, verify_provider
from secure_net import PublicFetcher


ROOT = Path(__file__).resolve().parent
STATIC = ROOT / 'static'
EXAMPLE = ROOT.parent / 'examples/nrw-muenster/reference'
MAX_BODY = 3 * 1024 * 1024


class State:
    def __init__(self):
        catalog = json.loads((ROOT / 'catalogs.json').read_text())
        self.fetch = PublicFetcher(catalog['allowed_hosts'])
        self.token = secrets.token_urlsafe(32)
        self.places = collections.OrderedDict()
        self.profiles = collections.OrderedDict()
        self.lock = threading.RLock()
        self.setup_slot = threading.BoundedSemaphore(1)
        self.document_slots = threading.BoundedSemaphore(2)

    def search(self, q, fetch=None):
        if not 2 <= len(q) <= 120:
            raise ValueError('Bitte einen Ortsnamen mit 2 bis 120 Zeichen eingeben.')
        candidates = search_places(q, fetch or self.fetch)[:25]
        with self.lock:
            for candidate in candidates:
                candidate.setdefault('id', hashlib.sha256(json.dumps(candidate, sort_keys=True).encode()).hexdigest()[:20])
                self.places[candidate['id']] = candidate
            while len(self.places) > 100:
                self.places.popitem(last=False)
        return {'candidates': candidates}

    def setup(self, submitted, example=False):
        if not isinstance(submitted, dict):
            raise ValueError('Bitte zuerst einen Ort auswählen.')
        if not self.setup_slot.acquire(blocking=False):
            raise ValueError('Eine Ortsprüfung läuft bereits. Bitte deren Ergebnis abwarten.')
        deadline = time.monotonic() + 50
        def bounded_fetch(url, *, max_bytes=4*1024*1024, timeout=12):
            remaining = deadline - time.monotonic()
            if remaining < 1:
                raise ValueError('Zeitbudget der Ortsprüfung erreicht. Ungeprüfte Quellen bleiben inaktiv.')
            return self.fetch(url, max_bytes=max_bytes, timeout=min(timeout, remaining))
        try:
            candidate = self.places.get(submitted.get('id'))
            if example:
                matches = self.search('Münster', bounded_fetch)['candidates']
                candidate = next((p for p in matches if p.get('municipality_code') == '05515000'), None)
                if candidate:
                    candidate = dict(candidate, center=[51.9607, 7.6261])
            elif candidate is None and isinstance(submitted.get('name'), str):
                # Imported cases cannot introduce their own network services.
                candidates = self.search(submitted['name'], bounded_fetch)['candidates']
                candidate = next((p for p in candidates if p.get('municipality_code') and p.get('municipality_code') == submitted.get('municipality_code')), None)
            if candidate is None:
                raise ValueError('Ort konnte nicht amtlich zugeordnet werden. Bitte erneut in der Ortssuche auswählen.')
            discovered = discover(candidate, bounded_fetch)
            candidates = discovered.get('providers', [])[:8]
            with ThreadPoolExecutor(max_workers=3) as pool:
                verified = list(pool.map(lambda item: verify_provider(item, candidate, bounded_fetch), candidates))
            for item in discovered.get('providers', [])[8:40]:
                verified.append(dict(item, verification_state='gefunden_ungeprueft', test_result='Prüfbudget erreicht; nicht aktiviert.'))
            profile = dict(candidate, profile_id=secrets.token_hex(12), providers=verified,
                           authorities=discovered.get('authorities', []), evidence=discovered.get('evidence', []),
                           warnings=discovered.get('warnings', []))
            if len(discovered.get('providers', [])) > 8:
                profile['warnings'].append('Die ersten acht Dienstkandidaten wurden geprüft. Weitere Treffer bleiben sichtbar, aber inaktiv.')
            if not any(p.get('role') == 'parcels' and p['verification_state'] == 'verifiziert' for p in verified):
                profile['warnings'].append('Keine vollständig geprüfte öffentliche Flurstückschnittstelle. Manuelle Erfassung oder Geometrieimport verwenden.')
            with self.lock:
                self.profiles[profile['profile_id']] = profile
                while len(self.profiles) > 20:
                    self.profiles.popitem(last=False)
            return {'profile': profile}
        finally:
            self.setup_slot.release()

    def profile(self, identifier):
        profile = self.profiles.get(identifier)
        if profile is None:
            raise ValueError('Ortsprüfung abgelaufen. Bitte den Ort erneut einrichten; Ihre Auswahl bleibt im Vorgang erhalten.')
        return profile

    def provider(self, profile, identifier):
        provider = next((p for p in profile['providers'] if p['provider_id'] == identifier), None)
        if not provider or provider['verification_state'] != 'verifiziert':
            raise ValueError('Die ausgewählte Datenquelle ist nicht freigegeben.')
        return provider

    def case(self, raw):
        case = validate_case(raw)
        saved = self.profiles.get((case.get('profile') or {}).get('profile_id'))
        if saved:
            # Use current server evidence, never imported provider claims.
            case['profile'] = saved
        else:
            profile = case.get('profile') or {}
            case['profile'] = profile
            profile['verification_state'] = 'gefunden_ungeprueft'
            for item in profile.get('providers', []) + profile.get('authorities', []):
                item['verification_state'] = 'gefunden_ungeprueft'
            profile.setdefault('warnings', []).append('Importierte Quellenangaben wurden in dieser Sitzung nicht erneut geprüft.')
        return case


class Handler(BaseHTTPRequestHandler):
    server_version = 'Grundstuecksrecherche'

    def log_message(self, format, *args):
        # Query parameters may contain address searches; do not record them.
        pass

    @property
    def state(self):
        return self.server.state

    def allowed(self):
        host = self.headers.get('Host', '')
        allowed = {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}
        if host not in allowed:
            raise PermissionError('Nicht freigegebener Hostname.')
        origin = self.headers.get('Origin')
        if origin and origin not in {'http://' + item for item in allowed}:
            raise PermissionError('Anfragen fremder Webseiten sind gesperrt.')
        if self.headers.get('Sec-Fetch-Site') == 'cross-site':
            raise PermissionError('Anfragen fremder Webseiten sind gesperrt.')

    def respond(self, data, content_type='application/json; charset=utf-8', status=200, filename=None):
        if not isinstance(data, bytes):
            data = json.dumps(data, ensure_ascii=False, allow_nan=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Cross-Origin-Resource-Policy', 'same-origin')
        self.send_header('Content-Security-Policy', "default-src 'self'; connect-src 'self'; img-src 'self' data: blob:; style-src 'self' 'unsafe-inline'; script-src 'self'; frame-src 'self' blob:; object-src 'none'; base-uri 'none'; frame-ancestors 'self'")
        if filename:
            if not all(c.isalnum() or c in '._-' for c in filename) or len(filename) > 150:
                filename = 'grundstuecksrecherche.zip'
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def error(self, exc):
        status = 403 if isinstance(exc, PermissionError) else 400
        self.respond({'error': str(exc)[:500]}, status=status)

    def do_GET(self):
        try:
            self.allowed()
            parsed = urlsplit(self.path)
            params = {key: values[0] for key, values in parse_qs(parsed.query).items()}
            path = parsed.path
            if path == '/api/config':
                return self.respond({'csrf_token': self.state.token, 'max_parcels': 200, 'min_parcel_zoom': 17})
            if path == '/api/places':
                return self.respond(self.state.search(params.get('q', '').strip()))
            if path in ('/api/map', '/api/parcels', '/api/address'):
                profile = self.state.profile(params.get('profile_id'))
                if path == '/api/address':
                    q = params.get('q', '').strip()
                    if not 3 <= len(q) <= 160:
                        raise ValueError('Bitte eine Adresse mit 3 bis 160 Zeichen eingeben.')
                    lat, lon = profile['center']
                    url = query('https://photon.komoot.io/api/', q=q, lat=lat, lon=lon, limit=5, lang='de', bbox=','.join(map(str, profile['bounds'])))
                    raw = json.loads(self.state.fetch(url, max_bytes=256*1024))
                    result = []
                    for feature in raw.get('features', [])[:5]:
                        coords = feature.get('geometry', {}).get('coordinates', [])
                        props = feature.get('properties', {})
                        if len(coords) >= 2:
                            result.append({'label': ', '.join(str(props[key]) for key in ('name', 'street', 'housenumber', 'postcode', 'city') if props.get(key)), 'center': [coords[1], coords[0]]})
                    return self.respond({'candidates': result})
                if path == '/api/map':
                    provider = self.state.provider(profile, params.get('provider_id'))
                    data, mime = map_image(provider, params.get('bbox', params.get('BBOX', '')), params.get('width', params.get('WIDTH', 256)), params.get('height', params.get('HEIGHT', 256)), self.state.fetch)
                    return self.respond(data, mime)
                provider = next((p for p in profile['providers'] if p['role'] == 'parcels' and p['verification_state'] == 'verifiziert' and p['protocol'].upper() == 'WFS'), None)
                if not provider:
                    raise ValueError('Kein geprüfter Flurstückdienst; bitte manuell erfassen oder importieren.')
                return self.respond(parcels(provider, profile, params.get('bbox', ''), params.get('page', 0), self.state.fetch))
            if path.startswith('/api/'):
                return self.respond({'error': 'Schnittstelle nicht vorhanden.'}, status=404)
            base = EXAMPLE if path.startswith('/reference/') else STATIC
            relative = unquote(path[len('/reference/'):] if base == EXAMPLE else path.lstrip('/')) or 'index.html'
            file = (base / relative).resolve()
            if not file.is_relative_to(base.resolve()) or not file.is_file() or file.stat().st_size > 5*1024*1024:
                return self.respond({'error': 'Datei nicht vorhanden.'}, status=404)
            return self.respond(file.read_bytes(), mimetypes.guess_type(file.name)[0] or 'application/octet-stream')
        except (ValueError, KeyError, TypeError, PermissionError, OSError) as exc:
            self.error(exc)
        except Exception:
            self.respond({'error': 'Die Anfrage konnte nicht abgeschlossen werden. Ihr gespeicherter Vorgang bleibt unverändert.'}, status=500)

    def do_POST(self):
        try:
            self.allowed()
            if not secrets.compare_digest(self.headers.get('X-Local-Token', ''), self.state.token):
                raise PermissionError('Sitzung nicht bestätigt. Seite neu laden.')
            if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                raise ValueError('JSON-Anfrage erforderlich.')
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= MAX_BODY or self.headers.get('Transfer-Encoding'):
                raise ValueError('Anfrage ist leer oder größer als 3 MB.')
            self.connection.settimeout(15)
            raw = self.rfile.read(length)
            data = json.loads(raw, parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Ungültige Zahl.')))
            if not isinstance(data, dict):
                raise ValueError('JSON-Objekt erforderlich.')
            path = urlsplit(self.path).path
            if path == '/api/setup':
                return self.respond(self.state.setup(data.get('place')))
            if path == '/api/example':
                return self.respond(self.state.setup({}, example=True))
            if path == '/api/import-geo':
                profile = self.state.profile(data.get('profile_id'))
                return self.respond(import_geometry(data.get('content'), profile))
            if path in ('/api/documents', '/api/export', '/api/import'):
                if not self.state.document_slots.acquire(blocking=False):
                    raise ValueError('Dokumente werden gerade erstellt. Bitte kurz warten.')
                try:
                    case = self.state.case(data.get('case'))
                    if path == '/api/import':
                        for parcel in case.get('selected_parcels', []):
                            is_point = (parcel.get('geometry') or {}).get('type') == 'Point'
                            parcel['identification_status'] = 'location_hint' if is_point or parcel.get('identification_status') == 'location_hint' else 'manuell_ergaenzt'
                        return self.respond({'case': case})
                    if path == '/api/documents':
                        return self.respond({'documents': build_documents(case), 'warnings': case.get('profile', {}).get('warnings', [])})
                    payload, mime, filename = export_document(case, data.get('format'), data.get('document_id'))
                    return self.respond(payload, mime, filename=filename)
                finally:
                    self.state.document_slots.release()
            self.respond({'error': 'Schnittstelle nicht vorhanden.'}, status=404)
        except (ValueError, KeyError, TypeError, PermissionError, OSError) as exc:
            self.error(exc)
        except Exception:
            self.respond({'error': 'Dokument konnte nicht erstellt werden. Eingaben bleiben erhalten; bitte die fehlenden Angaben prüfen.'}, status=500)


class LocalServer(ThreadingHTTPServer):
    daemon_threads = True
    request_queue_size = 12

    def __init__(self, address, handler):
        self.slots = threading.BoundedSemaphore(16)
        super().__init__(address, handler)

    def process_request(self, request, client_address):
        if not self.slots.acquire(blocking=False):
            request.close()
            return
        request.settimeout(20)
        super().process_request(request, client_address)

    def process_request_thread(self, request, client_address):
        try:
            super().process_request_thread(request, client_address)
        finally:
            self.slots.release()


def main():
    parser = argparse.ArgumentParser(description='Lokale Grundstücksrecherche ohne automatische Versendung.')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    server = LocalServer(('127.0.0.1', args.port), Handler)
    server.state = State()
    print(f'Grundstücksrecherche: http://127.0.0.1:{server.server_port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
