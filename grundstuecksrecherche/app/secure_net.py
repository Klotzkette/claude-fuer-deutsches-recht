"""Bounded public-data transport. No caller-controlled forwarding proxy."""

from __future__ import annotations

import collections
import http.client
import ipaddress
import socket
import ssl
import threading
import time
from urllib.parse import urljoin, urlsplit


class FetchError(ValueError):
    pass


class PublicFetcher:
    def __init__(self, allowed=None, max_cache_bytes=24 * 1024 * 1024):
        self.allowed = dict(allowed or {})
        self.cache = collections.OrderedDict()
        self.cache_bytes = 0
        self.max_cache_bytes = max_cache_bytes
        self.lock = threading.RLock()
        self.slots = threading.BoundedSemaphore(6)
        self.last_request = {}
        self.context = ssl.create_default_context()
        self.dns_slots = threading.BoundedSemaphore(3)
        self.dns_cache = {}

    def allow(self, host, prefixes):
        with self.lock:
            self.allowed[host.lower()] = tuple(prefixes)

    def _resolve(self, host, timeout):
        with self.lock:
            hit = self.dns_cache.get(host)
            if hit and hit[0] > time.monotonic():
                return hit[1]
        if not self.dns_slots.acquire(timeout=min(timeout, 0.5)):
            raise FetchError('Namensauflösung ausgelastet. Bitte erneut versuchen.')
        done, result = threading.Event(), []
        def resolve():
            try:
                result.append(socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM))
            except OSError:
                result.append(None)
            finally:
                self.dns_slots.release()
                done.set()
        threading.Thread(target=resolve, daemon=True).start()
        if not done.wait(timeout) or not result or not result[0]:
            raise FetchError('Namensauflösung fehlgeschlagen oder Zeitlimit erreicht.')
        with self.lock:
            self.dns_cache[host] = (time.monotonic() + 60, result[0])
        return result[0]

    def validate(self, url, timeout=5):
        p = urlsplit(url)
        if p.scheme != 'https' or not p.hostname or p.username or p.password or p.port not in (None, 443) or p.fragment:
            raise FetchError('Nur freigegebene HTTPS-Quellen ohne Zugangsdaten sind zulässig.')
        host = p.hostname.lower()
        prefixes = self.allowed.get(host, ())
        if not any(p.path == prefix or p.path.startswith(prefix.rstrip('/') + '/') or prefix == '/' for prefix in prefixes):
            raise FetchError('Diese Quelle ist nicht im geprüften Quellenkatalog freigegeben.')
        if '%' in p.path or '\\' in p.path or '..' in p.path.split('/') or any(ord(c) < 32 for c in url):
            raise FetchError('Ungültiger Quellenpfad.')
        try:
            answers = self._resolve(host, min(5, max(0.1, timeout)))
        except OSError as exc:
            raise FetchError('Die Quelle ist derzeit nicht erreichbar.') from exc
        addresses = list(dict.fromkeys(item[4][0] for item in answers))
        if not addresses or any(not ipaddress.ip_address(addr).is_global for addr in addresses):
            raise FetchError('Lokale und nicht öffentliche Netzadressen sind gesperrt.')
        return host, p.path or '/', p.query, addresses

    def __call__(self, url, max_bytes=4 * 1024 * 1024, timeout=12):
        max_bytes = min(int(max_bytes), 8 * 1024 * 1024)
        timeout = min(max(float(timeout), 1), 20)
        with self.lock:
            hit = self.cache.get(url)
            if hit and hit[0] > time.monotonic() and len(hit[1]) <= max_bytes:
                self.cache.move_to_end(url)
                return hit[1]
        if not self.slots.acquire(timeout=1):
            raise FetchError('Mehrere Quellen werden bereits gelesen. Bitte kurz warten.')
        try:
            result = self._fetch(url, max_bytes, timeout)
            with self.lock:
                previous = self.cache.pop(url, None)
                if previous:
                    self.cache_bytes -= len(previous[1])
                self.cache[url] = (time.monotonic() + 300, result)
                self.cache_bytes += len(result)
                while self.cache_bytes > self.max_cache_bytes or len(self.cache) > 256:
                    _, old = self.cache.popitem(last=False)
                    self.cache_bytes -= len(old[1])
            return result
        finally:
            self.slots.release()

    def _fetch(self, url, max_bytes, timeout):
        deadline = time.monotonic() + timeout
        for _ in range(4):
            host, path, query, addresses = self.validate(url, deadline-time.monotonic())
            with self.lock:
                now = time.monotonic()
                wait = max(0, self.last_request.get(host, 0) + 0.12 - now)
                self.last_request[host] = now + wait
            if wait > 1:
                raise FetchError('Quellenabrufe vorübergehend begrenzt. Bitte erneut versuchen.')
            time.sleep(wait)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise FetchError('Zeitlimit der Datenquelle erreicht.')
            connection = http.client.HTTPSConnection(host, timeout=remaining, context=self.context)
            timer = None
            try:
                # Pin the validated address while retaining TLS SNI and certificate checks.
                raw = socket.create_connection((addresses[0], 443), timeout=remaining)
                try:
                    connection.sock = self.context.wrap_socket(raw, server_hostname=host)
                except Exception:
                    raw.close()
                    raise
                wire = connection.sock
                def expire():
                    try:
                        wire.shutdown(socket.SHUT_RDWR)
                    except OSError:
                        pass
                    wire.close()
                timer = threading.Timer(max(0.01, deadline-time.monotonic()), expire)
                timer.daemon = True
                timer.start()
                connection.request('GET', path + ('?' + query if query else ''), headers={
                    'User-Agent': 'Grundstuecksrecherche/1.0 (public geodata; local application)',
                    'Accept-Encoding': 'identity', 'Accept': '*/*', 'Connection': 'close',
                })
                response = connection.getresponse()
                if response.status in (301, 302, 303, 307, 308):
                    location = response.getheader('Location')
                    if not location:
                        raise FetchError('Weiterleitung ohne Ziel.')
                    url = urljoin(url, location)
                    continue
                if response.status != 200:
                    raise FetchError(f'Die Quelle antwortet mit HTTP {response.status}.')
                if response.getheader('Content-Encoding', 'identity') != 'identity':
                    raise FetchError('Komprimierte Netzwerkantwort nicht freigegeben.')
                length = response.getheader('Content-Length')
                if length and (not length.isdigit() or int(length) > max_bytes):
                    raise FetchError('Antwort der Datenquelle überschreitet die Größenbegrenzung.')
                chunks, size = [], 0
                while True:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise FetchError('Zeitlimit der Datenquelle erreicht.')
                    # The connection may clear .sock after a Connection: close response.
                    # The response stream still owns the socket and needs the deadline.
                    if response.fp and getattr(response.fp, 'raw', None):
                        response.fp.raw._sock.settimeout(remaining)
                    chunk = response.read1(min(65536, max_bytes - size + 1))
                    if not chunk:
                        if time.monotonic() >= deadline:
                            raise FetchError('Zeitlimit der Datenquelle erreicht.')
                        if length is not None and size != int(length):
                            raise FetchError('Die Datenquelle hat eine unvollständige Antwort geliefert.')
                        break
                    size += len(chunk)
                    if size > max_bytes:
                        raise FetchError('Antwort der Datenquelle überschreitet die Größenbegrenzung.')
                    chunks.append(chunk)
                return b''.join(chunks)
            except (OSError, http.client.HTTPException) as exc:
                raise FetchError('Quellenabruf fehlgeschlagen oder Zeitlimit erreicht.') from exc
            finally:
                if timer:
                    timer.cancel()
                connection.close()
        raise FetchError('Zu viele Weiterleitungen der Datenquelle.')
