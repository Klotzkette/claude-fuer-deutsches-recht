#!/usr/bin/env python3
"""Isolierte Regressionstests der Plugin-Validierung ohne Netzwerkzugriff."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("validate-with-claude-cli.sh")
MARKETPLACE = ".claude-plugin/marketplace.json"
SUCCESS = "OK: Alle Plugins haben die strikte CLI-Validierung bestanden."
FAKE_CLI = r'''#!/usr/bin/env python3
import json
import os
import sys

args = sys.argv[1:]
with open(os.environ["VALIDATION_TEST_LOG"], "a", encoding="utf-8") as log:
    log.write(json.dumps({"args": args, "cwd": os.getcwd()}) + "\n")

if args == ["--version"]:
    print("Test-CLI 1.0")
    sys.exit(0)
if len(args) != 4 or args[:3] != ["plugin", "validate", "--strict"]:
    sys.exit(64)

# Mehr Ausgabe als tail anzeigt; der Exitstatus muss trotzdem durchkommen.
for index in range(12):
    print(f"Pruefschritt {index + 1}")
print("Pruefung beendet.")
failures = json.loads(os.environ["VALIDATION_TEST_FAILURES"])
sys.exit(23 if args[3] in failures else 0)
'''


class OfficialPluginValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="plugin-validation-")
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name).resolve()
        self.repo = self.directory / "test repo"
        scripts = self.repo / "scripts"
        scripts.mkdir(parents=True)
        self.script = scripts / SCRIPT.name
        shutil.copy2(SCRIPT, self.script)
        self.marketplace = self.repo / MARKETPLACE
        self.marketplace.parent.mkdir()

        bin_dir = self.directory / "bin"
        bin_dir.mkdir()
        executable = bin_dir / "claude"
        executable.write_text(FAKE_CLI, encoding="utf-8")
        executable.chmod(0o755)
        (bin_dir / "python3").symlink_to(sys.executable)
        self.log = self.directory / "calls.jsonl"
        self.env = {
            "PATH": os.pathsep.join((str(bin_dir), "/usr/bin", "/bin")),
            "HOME": str(self.directory),
            "VALIDATION_TEST_LOG": str(self.log),
            "VALIDATION_TEST_FAILURES": "[]",
        }

    def plugin(self, name, source):
        manifest = self.repo / source / ".claude-plugin" / "plugin.json"
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({"name": name}), encoding="utf-8")
        return {"name": name, "source": source}

    def write_marketplace(self, plugins):
        self.marketplace.write_text(
            json.dumps({"name": "test-marketplace", "owner": {"name": "Test"},
                        "plugins": plugins}),
            encoding="utf-8",
        )

    def run_validation(self, *targets, failures=()):
        self.log.unlink(missing_ok=True)
        env = {**self.env, "VALIDATION_TEST_FAILURES": json.dumps(failures)}
        result = subprocess.run(
            ["/bin/bash", str(self.script), *targets],
            cwd=self.directory,
            env=env,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
            check=False,
        )
        calls = [json.loads(line) for line in self.log.read_text().splitlines()]
        self.assertEqual(calls[0]["args"], ["--version"])
        for call in calls:
            self.assertEqual(call["cwd"], str(self.repo))
        validations = calls[1:]
        for call in validations:
            self.assertEqual(call["args"][:3], ["plugin", "validate", "--strict"])
            self.assertEqual(len(call["args"]), 4)
        return result, [call["args"][3] for call in validations]

    def assert_failed(self, result):
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertNotIn(SUCCESS, output)

    def test_nested_sources_are_visited_in_marketplace_order(self):
        plugins = [
            self.plugin("first", "./plugins/group/first"),
            self.plugin("second", "./plugins/with spaces/second"),
        ]
        self.write_marketplace(plugins)
        result, targets = self.run_validation()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(SUCCESS, result.stdout)
        self.assertEqual(targets, [MARKETPLACE, *(p["source"] for p in plugins)])

    def test_cli_failure_survives_loop_and_output_pipeline(self):
        plugins = [self.plugin("first", "./plugins/first"),
                   self.plugin("second", "./plugins/second")]
        self.write_marketplace(plugins)
        for failed_target in (MARKETPLACE, plugins[0]["source"]):
            with self.subTest(failed_target=failed_target):
                result, targets = self.run_validation(failures=[failed_target])
                self.assert_failed(result)
                self.assertEqual(targets, [MARKETPLACE, *(p["source"] for p in plugins)])

    def test_missing_source_fails_and_other_plugins_are_still_visited(self):
        existing = self.plugin("existing", "./plugins/existing")
        self.write_marketplace([
            {"name": "missing", "source": "./plugins/missing"}, existing,
        ])
        result, targets = self.run_validation()
        self.assert_failed(result)
        self.assertIn("./plugins/missing", result.stderr)
        self.assertEqual(targets, [MARKETPLACE, existing["source"]])

    def test_one_plugin_mode_does_not_read_marketplace_or_visit_other_plugins(self):
        self.plugin("selected", "selected")
        self.plugin("nested", "plugins/nested")
        self.plugin("other", "other")
        for target in ("selected", "plugins/nested"):
            for content in (None, "{"):
                with self.subTest(target=target, marketplace=content):
                    self.marketplace.unlink(missing_ok=True)
                    if content is not None:
                        self.marketplace.write_text(content, encoding="utf-8")
                    result, targets = self.run_validation(target)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn(SUCCESS, result.stdout)
                    self.assertEqual(targets, [target])

    def test_one_plugin_mode_propagates_cli_failure(self):
        self.plugin("selected", "selected")
        result, targets = self.run_validation("selected", failures=["selected"])
        self.assert_failed(result)
        self.assertEqual(targets, ["selected"])

    def test_one_plugin_mode_rejects_missing_directory(self):
        result, targets = self.run_validation("missing")
        self.assert_failed(result)
        self.assertEqual(targets, [])

    def test_missing_marketplace_fails_even_when_cli_succeeds(self):
        result, _ = self.run_validation()
        self.assert_failed(result)

    def test_invalid_marketplace_fails_even_when_cli_succeeds(self):
        invalid_documents = (
            "", "{", "null", "[]", "{}", '{"plugins": null}',
            '{"plugins": {}}', '{"plugins": ""}',
            '{"plugins": [null]}', '{"plugins": [{}]}',
        )
        for content in invalid_documents:
            with self.subTest(content=content):
                self.marketplace.write_text(content, encoding="utf-8")
                result, _ = self.run_validation()
                self.assert_failed(result)

    def test_invalid_entry_after_valid_entry_fails(self):
        valid = self.plugin("first", "./plugins/first")
        invalid_entries = (
            {"name": "broken"},
            {"name": "broken", "source": None},
            {"name": "broken", "source": {}},
            {"name": "broken", "source": ""},
            {"name": "broken", "source": "./plugins/first\n"},
            {"name": "broken", "source": "./plugins/first\u0000"},
            {"name": "", "source": "./plugins/first"},
            {"name": "broken\tname", "source": "./plugins/first"},
        )
        for entry in invalid_entries:
            with self.subTest(entry=entry):
                self.write_marketplace([valid, entry])
                result, _ = self.run_validation()
                self.assert_failed(result)

    def test_empty_plugin_list_does_not_create_a_phantom_source(self):
        self.write_marketplace([])
        result, targets = self.run_validation()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(targets, [MARKETPLACE])


if __name__ == "__main__":
    unittest.main()
