#!/usr/bin/env python3
"""Regressionstest für profilgebundenes Prompt-Routing und sichere Quellenwahl."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from themen_profile import PROFILE_BY_KEY


SCRIPT = Path(__file__).resolve().parent / "generate-werkstatt-und-schnellstart-prompts.py"
SPEC = importlib.util.spec_from_file_location("generate_prompt_routing", SCRIPT)
assert SPEC and SPEC.loader
G = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G
SPEC.loader.exec_module(G)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    polluted_material = [
        {
            "slug": "kuendigungsbutton",
            "heading": "Kündigungsbutton im Kundenkonto",
            "desc": "Kündigung, Betriebsrat, Arbeitsgericht und Dreiwochenfrist zuerst prüfen.",
            "body": (
                "BGB Paragraf 312k regelt die Kündigung von Verbraucherverträgen im "
                "elektronischen Geschäftsverkehr. BGH, Urteil: "
                "NICHT-KURATIERTER-ENTSCHEIDUNGSANKER."
            ),
            "raw": "BGH, Urteil: NICHT-KURATIERTER-ENTSCHEIDUNGSANKER.",
        }
    ]

    ecommerce = PROFILE_BY_KEY["ecommerce"]
    fields_with_material = G.profile_fields(ecommerce, polluted_material)
    fields_without_material = G.profile_fields(ecommerce, [])
    require(
        fields_with_material == fields_without_material,
        "Skillmaterial hat stabile Profilfelder verändert",
    )
    require(
        all("Arbeitsgericht" not in f"{title} {detail}" for title, detail in fields_with_material),
        "Arbeitsrecht ist in E-Commerce-Profilfelder gelangt",
    )

    stations = G.quick_stations(ecommerce, polluted_material)
    require(len(stations) == min(6, len(ecommerce.stationen)), "Profilstationen fehlen")
    require(stations[0].startswith("Nutzerstrecke aufnehmen:"), "Kernroute wurde umsortiert")
    require(
        all("Dreiwochenfrist" not in station for station in stations),
        "Skilltext hat die profilgebundene Kernroute verdrängt",
    )

    beamten = PROFILE_BY_KEY["beamten"]
    trusted_field, trusted_detail = G.profile_fields(beamten, [])[0]
    require(
        G.quick_grip(beamten, trusted_field, trusted_detail) == trusted_detail,
        "exaktes Profilfeld wurde im Schnellstart verkürzt oder verallgemeinert",
    )
    require(
        G.quick_grip(beamten, trusted_field, trusted_detail + " Zusatz")
        != trusted_detail + " Zusatz",
        "nur ähnlich lautendes Feld wurde fälschlich als kuratiert vertraut",
    )

    for key, profile in PROFILE_BY_KEY.items():
        profile_fields = G.profile_fields(profile, polluted_material)
        profile_stations = G.quick_stations(profile, polluted_material)
        require(profile_fields, f"Profil {key} hat keine stabilen Felder")
        require(profile_stations, f"Profil {key} hat keine stabile Kernroute")
        require(
            len(profile_stations) == len(set(profile_stations)),
            f"Profil {key} enthält doppelte Kernstationen",
        )
        require(
            all(G.phrase_is_complete(detail) for _title, detail in profile_fields),
            f"Profil {key} enthält ein unvollständiges Feld",
        )
        require(
            all(G.phrase_is_complete(station) for station in profile_stations),
            f"Profil {key} enthält eine unvollständige Kernstation",
        )

    rental = G.quick_grip(PROFILE_BY_KEY["miet"], "Kündigung", "Arbeitsgericht und Betriebsrat")
    require("Dreiwochenfrist" not in rental, "Nichtstandardprofil wurde fachfremd umgeroutet")
    inferred = G.quick_grip(
        PROFILE_BY_KEY["default"],
        "Arbeitskündigung vor dem Arbeitsgericht",
        "",
    )
    require("Dreiwochenfrist" in inferred, "geschützte Themeninferenz im Standardprofil fehlt")

    first_sentence = G.route_excerpt(
        "Prüfe Zuständigkeit, Frist und Antrag vollständig. Danach folgt eine weitere, "
        "für den Grenzwert zu lange Vertiefung ohne sichere Kürzungsstelle",
        58,
    )
    require(
        first_sentence == "Prüfe Zuständigkeit, Frist und Antrag vollständig",
        f"vollständige Satzgrenze wurde nicht genutzt: {first_sentence!r}",
    )
    fallback = "Prüfe das kuratierte Kernfeld anhand der Profilstation"
    long_fragment = "Prüfe " + "umfangreiche Einzeltatsache " * 20
    require(
        G.route_excerpt(long_fragment, 80, fallback) == fallback,
        "lange Phrase ohne sichere Grenze wurde künstlich abgeschnitten",
    )
    require(
        G.detail_question("Betriebskosten nach Paragraf 556 Abs", fallback) == fallback,
        "unvollständiger Normverweis wurde als vollständige Phrase übernommen",
    )

    require(
        G.extract_case_anchors(polluted_material) == [],
        "ungeprüfte Entscheidung wurde aus Skillmaterial übernommen",
    )
    require(
        not G.contains_decision_reference("ZIP-Datei vom 01.02.2025 mit Unterlagen"),
        "eine Dateibezeichnung wurde fälschlich als Entscheidung behandelt",
    )
    norm_anchors = G.practice_route_anchors(
        "BGB Paragraf 312k regelt den Kündigungsbutton.",
        "BGH, Urteil: NICHT-KURATIERTER-ENTSCHEIDUNGSANKER.",
    )
    require("Paragraf 312k" in norm_anchors, "fachlicher Normanker wurde verworfen")
    require("NICHT-KURATIERT" not in norm_anchors, "ungeprüfte Entscheidung blieb in Praxisroute")

    full_norm = (
        "GG Artikel 98 Absatz 1 ordnet die Rechtsstellung der Richter im Bund und in den "
        "Ländern, verlangt für die nähere Ausgestaltung die jeweils einschlägige gesetzliche "
        "Grundlage und verbindet Status, Unabhängigkeit, Dienstaufsicht und zulässige "
        "organisatorische Maßnahmen mit einer vollständigen Prüfung"
    )
    extracted_norms = G.extract_norm_anchors(
        [{"slug": "richterstatus", "heading": "", "desc": full_norm + ".", "body": "", "raw": ""}]
    )
    require(extracted_norms == [full_norm], "vollständiger Normsatz wurde gekürzt oder verworfen")
    require(not extracted_norms[0].endswith("kann"), "Normanker endet als Satzfragment")

    for plugin_slug in (
        "commercial-courts-deutschland",
        "europaeisches-prozessrecht",
        "handelsrecht-hgb",
        "urheberrecht-de-eu",
    ):
        plugin_dir = G.REPO / plugin_slug
        material = G.collect_skill_material(plugin_dir)
        plugin_manifest = G.manifest(plugin_dir)
        profile = G.profile_for(
            plugin_slug,
            G.plugin_profile_context(plugin_manifest, plugin_dir, material),
        )
        routes = G.practice_routes(profile, material, 12, plugin_slug)
        require(len(routes) == 12, f"{plugin_slug} liefert nur {len(routes)} Fachrouten")

    with TemporaryDirectory() as folder:
        plugin = Path(folder)
        manifest_dir = plugin / ".claude-plugin"
        manifest_dir.mkdir(parents=True)
        (manifest_dir / "plugin.json").write_text(
            json.dumps(
                {
                    "name": "mietrecht",
                    "version": "0.0.0",
                    "description": "Bearbeitet Mietverhältnisse anhand der konkreten Akte.",
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        prompt = G.build_schnellstart(plugin, polluted_material)
        require(
            "NICHT-KURATIERTER-ENTSCHEIDUNGSANKER" not in prompt,
            "ungeprüfte Entscheidung gelangte in den Schnellstart-Prompt",
        )
        curated = G.anchor_head(PROFILE_BY_KEY["miet"].entscheidungen[0], 130)
        require(curated in prompt, "kuratierte Profilentscheidung fehlt im Schnellstart-Prompt")
        workshop = G.build_werkstatt(plugin, polluted_material)
        require(
            "NICHT-KURATIERTER-ENTSCHEIDUNGSANKER" not in workshop,
            "ungeprüfte Entscheidung gelangte in den Werkstatt-Prompt",
        )
        require(curated in workshop, "kuratierte Profilentscheidung fehlt im Werkstatt-Prompt")

    print("test-prompt-routing-scope OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
