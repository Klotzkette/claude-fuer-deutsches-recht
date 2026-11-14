"""Opt-in-Ratensteuerung für große Komponentenreleases.

GitHub: GITHUB_TOKEN regelmäßig 1.000 REST-Aufrufe/h; generell höchstens
500 inhaltserzeugende Aufrufe/h und 80/min. Acht Sekunden Abstand lassen
Reserve für Tag/Release-Aktionen. Keine neuen Zugangsdaten erforderlich.
https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
"""
from __future__ import annotations

from email.utils import parsedate_to_datetime
import json
import re
import subprocess
import time


class RateLimitStop(RuntimeError):
    """Kontrollierter Abbruch statt weiterer Anfragen an ein gesperrtes Budget."""


def split_response(output: str) -> tuple[int | None, dict[str, str], str]:
    """Nur HTTP-Antwortheader entfernen; JSON-Antwortkörper unverändert belassen."""
    remaining = output
    status, headers = None, {}
    while remaining.startswith("HTTP/"):
        match = re.search(r"\r?\n\r?\n", remaining)
        if match is None:
            raise RateLimitStop("Unvollständige HTTP-Antwortheader der Release-API")
        lines = remaining[:match.start()].splitlines()
        first = re.match(r"HTTP/\S+\s+(\d{3})", lines[0])
        if first is None:
            raise RateLimitStop("Ungültiger HTTP-Status der Release-API")
        status = int(first.group(1))
        headers = {key.strip().lower(): value.strip() for line in lines[1:] if ":" in line
                   for key, value in [line.split(":", 1)]}
        remaining = remaining[match.end():]
    return status, headers, remaining


class PacedReleaseClient:
    """Serieller Client; Wartefenster und Wiederholungen bleiben begrenzt."""

    def __init__(self, *, clock=time.time, monotonic=time.monotonic, sleep=time.sleep,
                 execute=subprocess.run, log=print, max_seconds=10800):
        self.clock, self.monotonic, self.sleep = clock, monotonic, sleep
        self.execute, self.log = execute, log
        self.deadline = monotonic() + max_seconds
        self.next_write = self.blocked_until = 0.0
        self.stopped = False

    def wait_until(self, deadline: float, reason: str) -> None:
        delay = max(0.0, deadline - self.clock())
        if delay > 3900 or self.monotonic() + delay >= self.deadline:
            raise RateLimitStop("Release-Ratenwartezeit überschreitet das begrenzte Laufzeitbudget")
        if delay >= 30:
            self.log(f"Release-Ratensteuerung: {reason}; {delay:.0f}s warten", flush=True)
        while self.clock() < deadline:
            if self.monotonic() >= self.deadline:
                raise RateLimitStop("Laufzeitbudget der Release-Ratensteuerung aufgebraucht")
            self.sleep(min(30.0, deadline - self.clock()))

    def run(self, command: list[str], *, timeout=300) -> subprocess.CompletedProcess:
        if self.stopped:
            raise RateLimitStop("Weitere Release-Anfragen nach dauerhaftem Ratenlimit gesperrt")
        if command[:2] != ["gh", "api"]:
            return self.execute(command, check=False, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, timeout=timeout)
        method = command[command.index("--method") + 1] if "--method" in command else "GET"
        mutation = method.upper() not in {"GET", "HEAD", "OPTIONS"}
        for attempt in range(3):
            self.wait_until(max(self.blocked_until, self.next_write if mutation else 0), "API-Budget/Uploadabstand")
            if self.monotonic() >= self.deadline:
                raise RateLimitStop("Laufzeitbudget der Release-Ratensteuerung aufgebraucht")
            if mutation:
                self.next_write = self.clock() + 8.0
            raw = self.execute([*command, "--include"], check=False, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
            status, headers, body = split_response(raw.stdout)
            left = headers.get("x-ratelimit-remaining")
            reset = headers.get("x-ratelimit-reset")
            if left is not None and reset is not None and int(left) <= 10:
                self.blocked_until = max(self.blocked_until, float(reset) + 5)
            throttled = status == 429 or (status == 403 and (
                left == "0" or "retry-after" in headers or "rate limit" in (body + raw.stderr).lower()))
            if not throttled:
                return subprocess.CompletedProcess(raw.args, raw.returncode, body, raw.stderr)
            if attempt == 2:
                self.stopped = True
                raise RateLimitStop("GitHub-Ratenlimit nach drei begrenzten Versuchen weiterhin aktiv")
            retry = headers.get("retry-after")
            if retry is None:
                retry_at = self.clock() + 60 * (2 ** attempt)
            elif retry.isdigit():
                retry_at = self.clock() + int(retry)
            else:
                retry_at = parsedate_to_datetime(retry).timestamp()
            self.blocked_until = max(self.blocked_until, retry_at, self.clock() + 60)
        raise AssertionError("unerreichbar")


def require_download_budget(asset_count: int, *, client: PacedReleaseClient | None = None) -> None:
    """Alle Draft-Downloads plus Metadatenreserve vor dem ersten Download sichern.

gh release download verwendet pro Asset einen REST-Aufruf. Der spezielle
rate_limit-Endpunkt verbraucht laut GitHub kein primäres REST-Budget.
"""
    client = client or PacedReleaseClient(max_seconds=7800)
    required = asset_count + 80
    for attempt in range(3):
        response = client.run(["gh", "api", "rate_limit"])
        if response.returncode:
            raise RateLimitStop("Verbleibendes GitHub-Budget kann nicht sicher festgestellt werden")
        try:
            core = json.loads(response.stdout)["resources"]["core"]
            limit, remaining, reset = int(core["limit"]), int(core["remaining"]), float(core["reset"])
        except (KeyError, TypeError, ValueError) as exc:
            raise RateLimitStop("Unvollständiger GitHub-Ratenbudgetnachweis") from exc
        if required > limit:
            raise RateLimitStop(f"{required} benötigte API-Aufrufe überschreiten das Stundenbudget {limit}")
        if remaining >= required:
            return
        if attempt == 2:
            break
        if reset <= client.clock():
            raise RateLimitStop("GitHub meldet erschöpftes Budget ohne zukünftigen Reset")
        client.wait_until(reset + 5, f"{required} API-Aufrufe für unabhängige Draftdownloads benötigt")
    raise RateLimitStop("Downloadbudget bleibt nach zwei vollständigen Resetfenstern unzureichend")
