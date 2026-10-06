"""Echte HTTPResponse-Streams an lokalen Socketpaaren, ohne externe Netzaufrufe.

Nur DNS, TCP-Verbindungsaufbau und die TLS-Hülle werden ersetzt. HTTP-Parsing,
read1, Socket-Zeitlimits und der absolute Abschalttimer bleiben unverändert.
"""

from contextlib import contextmanager
import http.client
from pathlib import Path
import socket
import sys
import threading
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
from secure_net import FetchError, PublicFetcher


URL = "https://example.org/wfs"
PUBLIC_DNS = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("8.8.8.8", 443))]


class NetworkDeadlineTests(unittest.TestCase):
    def assert_slots_available(self, semaphore, count):
        acquired = 0
        try:
            for _ in range(count):
                self.assertTrue(semaphore.acquire(blocking=False), "Ein Netzwerk-Slot blieb belegt.")
                acquired += 1
            self.assertFalse(semaphore.acquire(blocking=False))
        finally:
            for _ in range(acquired):
                semaphore.release()

    @contextmanager
    def transport(self, respond, *, dns_delay=0, tls_delay=0):
        fetch = PublicFetcher({"example.org": ["/wfs"]})
        client, peer = socket.socketpair()
        peer.settimeout(3)
        stop = threading.Event()
        request_received = threading.Event()
        failures, responses, connect_timeouts, dns_threads = [], [], [], []

        class ObservedResponse(http.client.HTTPResponse):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.read1_calls = 0
                responses.append(self)

            def read1(self, amount=-1):
                self.read1_calls += 1
                return super().read1(amount)

        def serve():
            try:
                request = b""
                while b"\r\n\r\n" not in request:
                    chunk = peer.recv(4096)
                    if not chunk:
                        return
                    request += chunk
                request_received.set()
                respond(peer, stop)
            except (BrokenPipeError, ConnectionResetError, OSError):
                # Die Frist darf den Datenstrom während einer Übertragung schließen.
                pass
            except Exception as exc:
                failures.append(exc)
            finally:
                peer.close()

        def connect(address, timeout):
            self.assertEqual(address, ("8.8.8.8", 443))
            connect_timeouts.append(timeout)
            client.settimeout(timeout)
            return client

        def resolve(*args, **kwargs):
            dns_threads.append(threading.current_thread())
            if dns_delay:
                stop.wait(dns_delay)
            return PUBLIC_DNS

        def wrap(raw, *, server_hostname):
            self.assertEqual(server_hostname, "example.org")
            if tls_delay:
                stop.wait(tls_delay)
            return raw

        worker = threading.Thread(target=serve, daemon=True)
        worker.start()
        try:
            with patch("secure_net.socket.getaddrinfo", side_effect=resolve), \
                    patch("secure_net.socket.create_connection", side_effect=connect), \
                    patch.object(fetch.context, "wrap_socket", side_effect=wrap), \
                    patch.object(http.client.HTTPSConnection, "response_class", ObservedResponse):
                yield fetch, responses, connect_timeouts
        finally:
            stop.set()
            try:
                client.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            client.close()
            worker.join(timeout=3)
            for thread in dns_threads:
                thread.join(timeout=3)
            for response in responses:
                response.close()
            self.assertFalse(worker.is_alive(), "Die lokale Gegenstelle wurde nicht beendet.")
            self.assertFalse(failures, failures)
            self.assertTrue(request_received.is_set(), "Der echte HTTP-Request wurde nicht gelesen.")
            self.assertTrue(responses, "Der HTTPResponse-Parser wurde nicht durchlaufen.")
            self.assertTrue(all(isinstance(response, http.client.HTTPResponse) for response in responses))
            self.assert_slots_available(fetch.slots, 6)
            self.assert_slots_available(fetch.dns_slots, 3)

    def expect_deadline(self, fetch, *, upper=1.6):
        started = time.monotonic()
        with self.assertRaises(FetchError):
            fetch(URL, timeout=1)
        elapsed = time.monotonic() - started
        self.assertGreaterEqual(elapsed, 0.8)
        self.assertLess(elapsed, upper, "Die Gesamtfrist wurde durch fortlaufende Daten verlängert.")
        self.assertNotIn(URL, fetch.cache, "Eine abgebrochene Antwort darf nicht im Cache landen.")

    def test_complete_response_uses_real_read1_and_releases_slots(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 6\r\nConnection: close\r\n\r\nabc")
            if not stop.wait(0.04):
                peer.sendall(b"def")

        with self.transport(respond) as (fetch, responses, timeouts):
            self.assertEqual(fetch(URL, timeout=1), b"abcdef")
            self.assertEqual(fetch.cache[URL][1], b"abcdef")
            self.assertEqual(fetch(URL, timeout=1), b"abcdef")
            self.assertEqual(len(responses), 1)
            self.assertGreaterEqual(responses[0].read1_calls, 2)
            self.assertTrue(0 < timeouts[0] <= 1)

    def test_trickling_body_cannot_refresh_total_deadline(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 80\r\nConnection: close\r\n\r\n")
            for _ in range(80):
                if stop.wait(0.08):
                    return
                peer.sendall(b"x")

        with self.transport(respond) as (fetch, responses, _):
            self.expect_deadline(fetch)
            self.assertGreater(responses[0].read1_calls, 2)

    def test_trickling_headers_cannot_refresh_total_deadline(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nX-Progress: ")
            for _ in range(80):
                if stop.wait(0.08):
                    return
                peer.sendall(b"x")
            peer.sendall(b"\r\nContent-Length: 0\r\n\r\n")

        with self.transport(respond) as (fetch, _, _):
            self.expect_deadline(fetch)

    def test_dns_tls_and_headers_leave_only_remaining_body_deadline(self):
        def respond(peer, stop):
            if stop.wait(0.25):
                return
            peer.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 20\r\nConnection: close\r\n\r\nabc")
            stop.wait(3)

        with self.transport(respond, dns_delay=0.2, tls_delay=0.15) as (fetch, responses, timeouts):
            self.expect_deadline(fetch, upper=1.45)
            self.assertLess(timeouts[0], 0.85)
            self.assertGreaterEqual(responses[0].read1_calls, 2)

    def test_timer_shutdown_must_not_return_empty_body_as_success(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 4\r\nConnection: close\r\n\r\n")
            stop.wait(3)

        with self.transport(respond) as (fetch, _, _):
            self.expect_deadline(fetch)

    def test_early_eof_must_not_cache_partial_content_length_body(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 20\r\nConnection: close\r\n\r\nabc")

        with self.transport(respond) as (fetch, _, _):
            with self.assertRaises(FetchError):
                fetch(URL, timeout=1)
            self.assertNotIn(URL, fetch.cache)

    def test_complete_empty_close_delimited_and_chunked_responses_remain_valid(self):
        for wire, expected in (
            (b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\nConnection: close\r\n\r\n", b""),
            (b"HTTP/1.0 200 OK\r\n\r\nabc", b"abc"),
            (b"HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\nConnection: close\r\n\r\n3\r\nabc\r\n0\r\n\r\n", b"abc"),
        ):
            with self.subTest(wire=wire):
                def respond(peer, stop):
                    peer.sendall(wire)

                with self.transport(respond) as (fetch, _, _):
                    self.assertEqual(fetch(URL, timeout=1), expected)
                    self.assertEqual(fetch.cache[URL][1], expected)

    def test_early_eof_without_final_chunk_is_not_cached(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\nConnection: close\r\n\r\n3\r\nabc\r\n")

        with self.transport(respond) as (fetch, _, _):
            with self.assertRaises(FetchError):
                fetch(URL, timeout=1)
            self.assertNotIn(URL, fetch.cache)

    def test_trickling_chunked_body_without_end_chunk_hits_deadline(self):
        def respond(peer, stop):
            peer.sendall(b"HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\nConnection: close\r\n\r\n")
            for _ in range(80):
                if stop.wait(0.08):
                    return
                peer.sendall(b"1\r\nx\r\n")

        with self.transport(respond) as (fetch, responses, _):
            self.expect_deadline(fetch)
            self.assertGreater(responses[0].read1_calls, 2)

    def test_dns_timeout_uses_bounded_daemon_worker_and_never_connects(self):
        fetch = PublicFetcher({"example.org": ["/wfs"]})
        release, entered = threading.Event(), threading.Event()
        workers = []

        def resolve(*args, **kwargs):
            workers.append(threading.current_thread())
            entered.set()
            release.wait(4)
            return PUBLIC_DNS

        try:
            with patch("secure_net.socket.getaddrinfo", side_effect=resolve), \
                    patch("secure_net.socket.create_connection") as connect:
                self.expect_deadline(fetch)
                self.assertTrue(entered.is_set())
                connect.assert_not_called()
                self.assertEqual(len(workers), 1)
                self.assertTrue(workers[0].daemon)
                self.assertNotIn("example.org", fetch.dns_cache)
                self.assert_slots_available(fetch.slots, 6)
        finally:
            release.set()
            for worker in workers:
                worker.join(timeout=3)
                self.assertFalse(worker.is_alive())
        self.assert_slots_available(fetch.dns_slots, 3)

    def test_dns_cache_reuses_public_result_without_resolving_again(self):
        fetch = PublicFetcher({"example.org": ["/wfs"]})
        with patch("secure_net.socket.getaddrinfo", return_value=PUBLIC_DNS) as dns:
            first = fetch.validate(URL)
            self.assertEqual(fetch.validate(URL + "?next=1"), (first[0], first[1], "next=1", first[3]))
            self.assertEqual(first[3], ["8.8.8.8"])
            dns.assert_called_once()
        self.assert_slots_available(fetch.dns_slots, 3)

    def test_dns_worker_limit_prevents_unbounded_resolver_threads(self):
        fetch = PublicFetcher({"example.org": ["/wfs"]})
        release = threading.Event()
        workers = []

        def resolve(*args, **kwargs):
            workers.append(threading.current_thread())
            release.wait(3)
            return PUBLIC_DNS

        try:
            with patch("secure_net.socket.getaddrinfo", side_effect=resolve):
                for _ in range(4):
                    with self.assertRaises(FetchError):
                        fetch._resolve("example.org", 0.05)
                self.assertEqual(len(workers), 3)
                self.assertTrue(all(worker.daemon for worker in workers))
                self.assertNotIn("example.org", fetch.dns_cache)
        finally:
            release.set()
            for worker in workers:
                worker.join(timeout=3)
                self.assertFalse(worker.is_alive())
        self.assert_slots_available(fetch.dns_slots, 3)


if __name__ == "__main__":
    unittest.main()
