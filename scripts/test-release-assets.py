#!/usr/bin/env python3
"""Regressionstest für Asset-Auswahl, Streaming-Hashes und Wiederaufnahme."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
import zipfile

from release_asset_common import expected_asset_metadata, read_checksums, release_assets, sha256_file


UPLOAD_SCRIPT = Path(__file__).resolve().parent / "upload-release-assets.py"
SPEC = importlib.util.spec_from_file_location("upload_release_assets", UPLOAD_SCRIPT)
assert SPEC and SPEC.loader
U = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = U
SPEC.loader.exec_module(U)

VALIDATE_SCRIPT = Path(__file__).resolve().parent / "validate-release-assets.py"
VALIDATE_SPEC = importlib.util.spec_from_file_location("validate_release_assets", VALIDATE_SCRIPT)
assert VALIDATE_SPEC and VALIDATE_SPEC.loader
V = importlib.util.module_from_spec(VALIDATE_SPEC)
sys.modules[VALIDATE_SPEC.name] = V
VALIDATE_SPEC.loader.exec_module(V)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="release-assets-") as tmp:
        dist = Path(tmp)
        with zipfile.ZipFile(dist / "plugin.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("README.md", "Inhalt")
        (dist / "hinweis.md").write_text("Direktdatei\n", encoding="utf-8")
        (dist / "marketplace.json").write_text('{"plugins": []}\n', encoding="utf-8")
        (dist / "intern.txt").write_text("kein Release-Asset\n", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "build-release-checksums.py"), str(dist)],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        require(result.returncode == 0, result.stderr)
        names = [path.name for path in release_assets(dist)]
        require(
            names == ["checksums-sha256.txt", "hinweis.md", "marketplace.json", "plugin.zip"],
            f"unerwartete Asset-Auswahl: {names}",
        )
        checksums = read_checksums(dist / "checksums-sha256.txt")
        require("intern.txt" not in checksums, "interne Textdatei darf nicht in der Prüfsummenliste stehen")
        require(checksums["plugin.zip"] == sha256_file(dist / "plugin.zip"), "ZIP-Hash stimmt nicht")

        metadata = expected_asset_metadata(dist)
        local = metadata["plugin.zip"]
        require(
            U.same_asset(local, {"state": "uploaded", "size": local["size"], "digest": local["digest"]}),
            "identisches Remote-Asset muss übersprungen werden",
        )
        require(
            not U.same_asset(local, {"state": "uploaded", "size": local["size"], "digest": "sha256:" + "0" * 64}),
            "abweichender Hash muss einen Upload auslösen",
        )

        responses = iter(
            [
                subprocess.CompletedProcess([], 1, "", "nicht gefunden"),
                subprocess.CompletedProcess([], 0, "", ""),
                subprocess.CompletedProcess(
                    [],
                    0,
                    '{"databaseId":12345,"tagName":"v1.2.3","isDraft":true}',
                    "",
                ),
            ]
        )
        original_run = U.run
        U.run = lambda *args, **kwargs: next(responses)
        try:
            release = U.ensure_release("example/repo", "v1.2.3")
        finally:
            U.run = original_run
        require(release["id"] == 12345, "Entwurfsrelease muss über databaseId auffindbar sein")
        require(release["isDraft"] is True, "Entwurfsstatus muss erhalten bleiben")

        uploaded = {"id": 91, "name": "plugin.zip", "state": "uploaded", **local}
        success = subprocess.CompletedProcess([], 0, json.dumps(uploaded), "")
        with patch.object(U, "run", return_value=success) as api, patch.object(
            U, "fetch_remote_assets"
        ) as fetch:
            U.upload_one("example/repo", 12345, dist / "plugin.zip", local, 1)
        command = api.call_args.args[0]
        require(command[:4] == ["gh", "api", "--method", "POST"], "Upload muss die REST-API nutzen")
        require(
            command[4] == "https://uploads.github.com/repos/example/repo/releases/12345/assets?name=plugin.zip",
            "Upload muss die bereits bekannte Release-ID ohne erneuten Tag-Lookup nutzen",
        )
        require(command[-2:] == ["--input", str(dist / "plugin.zip")], "Binärdatei muss als Requestbody übergeben werden")
        require("--clobber" not in command, "Wiederholung darf korrekte Assets nicht löschen")
        fetch.assert_not_called()

        # Auch eine beim letzten Versuch verlorene Antwort kann einen fertigen
        # Upload bedeuten. Nur Name, Zustand, Größe und Hash zusammen genügen.
        with patch.object(U, "run", side_effect=subprocess.TimeoutExpired("gh", 300)) as api, patch.object(
            U, "fetch_remote_assets", return_value={"plugin.zip": uploaded}
        ) as fetch, patch.object(U, "delete_asset") as delete:
            U.upload_one("example/repo", 12345, dist / "plugin.zip", local, 1)
        api.assert_called_once()
        fetch.assert_called_once_with("example/repo", 12345)
        delete.assert_not_called()

        # GitHub kann nach einem fehlgeschlagenen POST ein leeres starter-Asset
        # behalten. Genau dieses darf vor dem nächsten Versuch entfernt werden.
        starter = {"id": 92, "name": "plugin.zip", "state": "starter", "size": 0}
        with patch.object(
            U, "run", side_effect=[subprocess.CompletedProcess([], 1, "", "HTTP 502"), success]
        ) as api, patch.object(
            U, "fetch_remote_assets", return_value={"plugin.zip": starter}
        ), patch.object(U, "delete_asset") as delete, patch.object(U.time, "sleep"):
            U.upload_one("example/repo", 12345, dist / "plugin.zip", local, 2)
        require(api.call_count == 2, "starter-Fehler muss wiederaufnehmbar sein")
        delete.assert_called_once_with("example/repo", starter)

        conflicting = {**uploaded, "digest": "sha256:" + "0" * 64}
        with patch.object(
            U, "run", return_value=subprocess.CompletedProcess([], 1, "", "HTTP 422")
        ), patch.object(
            U, "fetch_remote_assets", return_value={"plugin.zip": conflicting}
        ), patch.object(U, "delete_asset") as delete:
            try:
                U.upload_one("example/repo", 12345, dist / "plugin.zip", local, 2)
            except RuntimeError as exc:
                require("kein automatisches Ersetzen" in str(exc), "fremder Inhalt braucht eindeutigen Fehler")
            else:
                raise AssertionError("abweichender Inhalt darf nicht als erfolgreicher Upload gelten")
        delete.assert_not_called()

        with patch.object(
            U, "run", return_value=subprocess.CompletedProcess([], 1, "", "HTTP 503")
        ), patch.object(U, "fetch_remote_assets", return_value={}):
            try:
                U.upload_one("example/repo", 12345, dist / "plugin.zip", local, 1)
            except RuntimeError as exc:
                require("HTTP 503" in str(exc), "endgültiger Uploadfehler muss den API-Befund erhalten")
            else:
                raise AssertionError("fehlendes Asset darf nach letztem Fehlversuch nicht als Erfolg gelten")

        original_subprocess_run = V.subprocess.run
        V.subprocess.run = lambda *args, **kwargs: subprocess.CompletedProcess(
            [], 0, '{"databaseId":12345}', ""
        )
        try:
            require(
                V.release_id("example/repo", "v1.2.3") == 12345,
                "Remote-Validator muss den Entwurf über databaseId lesen",
            )
        finally:
            V.subprocess.run = original_subprocess_run

        checksum_mtime = (dist / "checksums-sha256.txt").stat().st_mtime_ns
        newer = checksum_mtime + 1_000_000_000
        os.utime(dist / "plugin.zip", ns=(newer, newer))
        try:
            expected_asset_metadata(dist)
        except ValueError as exc:
            require("Prüfsummen erneut erzeugen" in str(exc), "veraltete Prüfsummen müssen auffallen")
        else:
            raise AssertionError("nachträglich geändertes Asset darf nicht akzeptiert werden")

    print("test-release-assets OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
