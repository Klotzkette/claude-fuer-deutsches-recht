import http.client
import json
from pathlib import Path
import sys
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'app'))
from server import Handler, LocalServer, State


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = LocalServer(('127.0.0.1', 0), Handler)
        cls.server.state = State()
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def request(self, path='/', method='GET', body=None, headers=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port, timeout=5)
        connection.request(method, path, body=body, headers=headers or {})
        response = connection.getresponse()
        status, data, result_headers = response.status, response.read(), dict(response.getheaders())
        connection.close()
        return status, data, result_headers

    def test_empty_start_and_policy(self):
        status, data, headers = self.request()
        self.assertEqual(status, 200)
        self.assertIn(b'Kein Ort', data)
        self.assertIn("connect-src 'self'", headers['Content-Security-Policy'])
        self.assertEqual(headers['X-Content-Type-Options'], 'nosniff')

    def test_csrf_host_and_origin(self):
        self.assertEqual(self.request('/api/config', headers={'Host': 'attacker.example'})[0], 403)
        self.assertEqual(self.request('/api/config', headers={'Origin': 'https://attacker.example'})[0], 403)
        self.assertEqual(self.request('/api/config', headers={'Sec-Fetch-Site': 'cross-site'})[0], 403)
        self.assertEqual(self.request('/api/example', 'POST', '{}', {'Content-Type': 'application/json'})[0], 403)

    def test_import_validation_and_no_arbitrary_fetch(self):
        headers = {'Content-Type': 'application/json', 'X-Local-Token': self.server.state.token}
        self.assertEqual(self.request('/api/import', 'POST', '{"case":{"unknown":1}}', headers)[0], 400)
        self.assertEqual(self.request('/api/import', 'POST', '{"case":{"purpose":NaN}}', headers)[0], 400)
        self.assertEqual(self.request('/api/map?url=http://127.0.0.1/', headers={})[0], 400)
        self.assertEqual(self.request('/api/fetch?url=https://example.org')[0], 404)

    def test_static_traversal_denied(self):
        for path in ('/../server.py', '/%2e%2e/server.py', '/reference/%2e%2e/%2e%2e/app/server.py'):
            self.assertEqual(self.request(path)[0], 404)

    def test_import_downgrades_unproven_parcels_and_accepts_null_profile(self):
        headers = {'Content-Type': 'application/json', 'X-Local-Token': self.server.state.token}
        raw = {'case': {'profile': None, 'selected_parcels': [{'identification_status': 'amtliche_flurstuecksdaten', 'official_parcel_reference': 'unproven'}]}}
        status, body, _ = self.request('/api/import', 'POST', json.dumps(raw), headers)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)['case']['selected_parcels'][0]['identification_status'], 'manuell_ergaenzt')

    def test_setup_cannot_inject_services(self):
        raw = {'place': {'id': 'foreign', 'providers': [{'service_url': 'http://localhost/'}]}}
        with patch('server.discover') as discover:
            status, _, _ = self.request('/api/setup', 'POST', json.dumps(raw), {'Content-Type': 'application/json', 'X-Local-Token': self.server.state.token})
        self.assertEqual(status, 400)
        discover.assert_not_called()


if __name__ == '__main__':
    unittest.main()
