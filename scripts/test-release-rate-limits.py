#!/usr/bin/env python3
"""Ratensteuerung mit virtueller Zeit; kein Netzwerk und keine realen Pausen."""
import json
import subprocess
import unittest

from release_rate_limits import PacedReleaseClient, RateLimitStop, require_download_budget, split_response


class RateTests(unittest.TestCase):
    def setUp(self):
        self.now = 10000.0
        self.calls = []
        self.responses = []
        self.client = PacedReleaseClient(clock=lambda: self.now, monotonic=lambda: self.now,
                                         sleep=self.sleep, execute=self.execute, log=lambda *a, **kw: None)

    def sleep(self, seconds):
        self.now += seconds

    def execute(self, command, **kwargs):
        self.calls.append((self.now, command))
        return self.responses.pop(0) if self.responses else self.response()

    def response(self, status=200, body="{}", headers=None):
        text = f"HTTP/2.0 {status}\r\n" + "".join(f"{k}: {v}\r\n" for k, v in (headers or {}).items()) + "\r\n" + body
        return subprocess.CompletedProcess([], 0 if status < 400 else 1, text, "")

    def test_uploads_stay_below_hourly_and_minute_content_limits(self):
        for _ in range(733):
            self.client.run(["gh", "api", "--method", "POST", "https://uploads.github.com/example"])
        times = [t for t, _ in self.calls]
        self.assertEqual(times[-1] - times[0], 732 * 8)
        self.assertLessEqual(max(sum(start <= t < start + 3600 for t in times) for start in times), 450)
        self.assertLessEqual(max(sum(start <= t < start + 60 for t in times) for start in times), 8)
        self.assertTrue(all("--include" in command for _, command in self.calls))

    def test_primary_budget_is_preserved_before_next_request(self):
        self.responses = [self.response(headers={"x-ratelimit-remaining": "10", "x-ratelimit-reset": "10100"}), self.response()]
        self.client.run(["gh", "api", "repos/example"])
        self.client.run(["gh", "api", "repos/example"])
        self.assertEqual(self.calls[1][0], 10105)

    def test_primary_failure_waits_until_reset_and_preserves_json(self):
        self.responses = [self.response(403, '{"message":"rate limit"}', {"x-ratelimit-remaining": "0", "x-ratelimit-reset": "10300"}), self.response(body='{"id":7}')]
        result = self.client.run(["gh", "api", "--method", "POST", "upload"])
        self.assertEqual(result.stdout, '{"id":7}')
        self.assertEqual(self.calls[1][0], 10305)

    def test_retry_after_and_secondary_exponential_wait_are_respected(self):
        self.responses = [self.response(429, headers={"Retry-After": "120"}), self.response(403, '{"message":"secondary rate limit"}'), self.response()]
        self.client.run(["gh", "api", "--method", "POST", "upload"])
        self.assertEqual([t for t, _ in self.calls], [10000, 10120, 10240])

    def test_persistent_rate_limit_stops_queue_after_three_attempts(self):
        self.responses = [self.response(429) for _ in range(3)]
        with self.assertRaises(RateLimitStop):
            self.client.run(["gh", "api", "upload"])
        with self.assertRaises(RateLimitStop):
            self.client.run(["gh", "api", "another-upload"])
        self.assertEqual(len(self.calls), 3)

    def test_permission_failure_is_not_misclassified_as_rate_limit(self):
        self.responses = [self.response(403, '{"message":"Resource not accessible by integration"}')]
        self.assertEqual(self.client.run(["gh", "api", "upload"]).returncode, 1)
        self.assertEqual(len(self.calls), 1)

    def test_download_reserves_whole_asset_batch_before_start(self):
        def budget(remaining, reset):
            return self.response(body=json.dumps({"resources": {"core": {"limit": 1000, "remaining": remaining, "reset": reset}}}))
        self.responses = [budget(740, 10300), budget(1000, 13900)]
        require_download_budget(733, client=self.client)
        self.assertEqual([t for t, _ in self.calls], [10000, 10305])

    def test_impossible_budget_and_unbounded_wait_fail_closed(self):
        self.responses = [self.response(body=json.dumps({"resources": {"core": {"limit": 1000, "remaining": 1000, "reset": 13000}}}))]
        with self.assertRaisesRegex(RateLimitStop, "überschreiten"):
            require_download_budget(1000, client=self.client)
        with self.assertRaises(RateLimitStop):
            self.client.wait_until(self.now + 4000, "zu lange")

    def test_header_parser_accepts_intermediate_continue(self):
        status, headers, body = split_response('HTTP/1.1 100 Continue\n\nHTTP/2.0 201 Created\nx-ratelimit-remaining: 999\n\n{"id":1}')
        self.assertEqual((status, headers, body), (201, {"x-ratelimit-remaining": "999"}, '{"id":1}'))


if __name__ == "__main__":
    unittest.main()
