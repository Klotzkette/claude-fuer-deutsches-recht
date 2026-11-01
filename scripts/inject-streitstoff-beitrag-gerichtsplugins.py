#!/usr/bin/env python3
"""Ergänzt bestehende Gerichts- und StA-Skills um ihren Streitstoff-Beitrag."""

from __future__ import annotations


if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)

import json
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
MARKER = "## Beitrag zum Streitstoff in diesem Verfahren"


def load_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def is_target(plugin: dict) -> bool:
    source = (plugin.get("source") or "").removeprefix("./")
    name = plugin["name"]
    return source.startswith("gerichtsplugins/") and (
        name.startswith("richter-")
        or name in {
            "relationstechnik-zivilrecht",
            "staatsanwaltschaft-amtsanwaltschaft",
            "staatsanwaltschaft-praxis-einstieg",
        }
    )


def block_for(plugin_name: str, skill_slug: str) -> str:
    if skill_slug == f"{plugin_name}-schnellstart":
        return ""
    if "relationstechnik" in plugin_name:
        return f"""{MARKER}

Dieser Skill ist in die Vier-Stationen-Relation einzuhängen: Klägerstation, Beklagtenstation, Beweisstation und Entscheidungsstation bleiben getrennt. Er benennt zu jedem Streitpunkt die tragende Tatsache, den Vortrag der Gegenseite, das Beweisangebot, die Beweislast und die Rechtsfolge. Fehlt eine Station, wird nicht frei ergänzt, sondern als Lücke mit Anschlussverfügung ausgewiesen.
"""
    if "staatsanwaltschaft" in plugin_name or "amtsanwaltschaft" in plugin_name:
        return f"""{MARKER}

Dieser Skill trägt zur staatsanwaltschaftlichen Streitstoff-Sortierung bei, indem Sachverhalts-Eckdaten, Beweismittel, rechtliche Würdigung und Anschlussverfügung getrennt werden. Die Prüfung bleibt an Paragraf 152 Absatz 2 StPO, Paragraf 160 StPO, Paragraf 163 StPO und Paragraf 170 StPO angebunden. Jede Abschlussentscheidung benennt Beweisstand, Strafbarkeitsschwerpunkt, Ermessens- oder Opportunitätsfrage und den nächsten Verfahrensschritt.
"""
    if "straf" in plugin_name:
        return f"""{MARKER}

Dieser Skill sortiert den strafrichterlichen Streitstoff nach Anklagevorwurf, Einlassung, Beweismittel, rechtlicher Würdigung und Rechtsfolgenfrage. Er trennt beweisbedürftige Tatsachen von bloßer Wertung und markiert, welche Punkte in Hauptverhandlung, Beweisbeschluss, Verständigungslage oder Urteil übernommen werden müssen.
"""
    if "familiengericht" in plugin_name:
        return f"""{MARKER}

Dieser Skill ordnet den familiengerichtlichen Streitstoff nach Antragstellerstation, Antragsgegnerstation, Kindeswohl- oder Unterhaltsachse, Belegen, Anhörungen und Beschlussformel. Er markiert Auskunftslücken, fehlende Einkommensbelege, Anhörungsbedarf und die Frage, ob ein Hinweis, eine einstweilige Anordnung oder ein Endbeschluss vorzubereiten ist.
"""
    if "arbeitsgericht" in plugin_name:
        return f"""{MARKER}

Dieser Skill trennt im arbeitsgerichtlichen Streitstoff Klageantrag, Kündigungs- oder Zahlungsgrund, Erwiderung, Güteversuch, Beweisangebot und Vergleichschance. Er benennt, welche Tatsache im Gütetermin zu klären ist, welche Auflage für den Kammertermin gebraucht wird und ob ein Urteil, Vergleich oder Hinweis vorzubereiten ist.
"""
    if "sozialgericht" in plugin_name:
        return f"""{MARKER}

Dieser Skill ordnet den sozialgerichtlichen Streitstoff nach Bescheid, Widerspruchsbescheid, Verwaltungsakte, Klagebegründung, medizinischer oder beitragsrechtlicher Tatsache und Amtsermittlung. Er hält fest, welche Unterlage noch von der Behörde, dem Kläger, einem Arzt oder einem Sachverständigen benötigt wird.
"""
    if "finanzgericht" in plugin_name:
        return f"""{MARKER}

Dieser Skill trennt Steuerbescheid, Einspruchsentscheidung, Klagegrund, Mitwirkung, Schätzung, Beweisangebot und Entscheidungsreife. Er macht sichtbar, welche Tatsache aus Buchführung, Prüfungsbericht, Steuerakte oder Parteivortrag stammt und welche Aufklärungsanordnung nach FGO-Logik erforderlich bleibt.
"""
    if "verwaltungsgericht" in plugin_name:
        return f"""{MARKER}

Dieser Skill sortiert den verwaltungsgerichtlichen Streitstoff nach Verwaltungsakt, Vorverfahren, Klagegrund, Behördenakte, Ermessen, Amtsermittlung und Tenorfolge. Er benennt, ob ein Hinweis, eine Aktenanforderung, ein Eilbeschluss oder ein Urteil vorbereitet werden muss.
"""
    if "bverfg" in plugin_name:
        return f"""{MARKER}

Dieser Skill trennt Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Subsidiarität, Grundrechtsrüge, Annahmegrund und Entscheidungsvorschlag. Er markiert Darlegungslücken und hält fest, ob ein Kammervermerk, ein Nichtannahmevotum oder ein Hinweis zur Unzulässigkeit vorbereitet wird.
"""
    if "handelsregister" in plugin_name:
        return f"""{MARKER}

Dieser Skill ordnet den registergerichtlichen Streitstoff nach Anmeldung, Urkunde, Vertretungsnachweis, Registerstand, Eintragungshindernis und Zwischenverfügung. Er trennt behebbare Formmängel von materiellen Hindernissen und benennt die nächste Registerverfügung.
"""
    if "insolvenz" in plugin_name:
        return f"""{MARKER}

Dieser Skill trennt Antrag, Gläubigerstellung, Forderung, Eröffnungsgrund, Sicherungsbedarf, Schuldnereinwand und Beschlussfolge. Er macht sichtbar, ob eine Aufklärungsverfügung, Sicherungsmaßnahme, Gutachterbestellung, Eröffnung oder Abweisung vorzubereiten ist.
"""
    return f"""{MARKER}

Dieser Skill ordnet den gerichtlichen Streitstoff nach Antrag, Gegenvorbringen, unstreitigem Sachverhalt, streitiger Tatsache, Beweisangebot, Rechtsfrage und Anschlussverfügung. Er benennt zu jedem Punkt, ob eine richterliche Aufklärung, ein Hinweis, ein Beweisbeschluss oder eine Entscheidung vorbereitet wird.
"""


def inject_one(path: Path, plugin_name: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    block = block_for(plugin_name, path.parent.name)
    if not block:
        return False
    new_text = text.rstrip() + "\n\n" + block.strip() + "\n"
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    changed = 0
    checked = 0
    for plugin in load_plugins():
        if not is_target(plugin):
            continue
        skills_dir = plugin_dir(plugin) / "skills"
        if not skills_dir.is_dir():
            continue
        for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
            checked += 1
            if inject_one(skill_md, plugin["name"]):
                changed += 1
    print(f"Streitstoff-Beitrag geprüft: {checked} Skills, ergänzt: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
