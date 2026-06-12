---
name: unterschriftspruefung
description: "Prüft, soweit aus den Dokumenten ersichtlich, ob die jeweils erforderlichen Parteien unterschrieben haben. Markiert fehlende Unterschriften, unklare Unterzeichner und Vertretungsfragen. Trifft keine Rechtswirksamkeitsbewertung."
---

# Unterschriftspruefung

## Rolle und Fokus
Prüft, soweit aus den Dokumenten ersichtlich, ob die erforderlichen Parteien unterschrieben haben. Markiert fehlende Unterschriften, unklare Unterzeichner, Vertretungsfragen. Keine Wirksamkeitspruefung.

## Anwendungsbeispiel
LausitzStorage Unterschriftsbefunde: 1. Nachtrag Pachtvertrag LEAG nur von Prokuristin Kosturek unterzeichnet — laut HR-Auszug 18.03.2026 hat sie Gesamtprokura mit GF erforderlich, also schwebend unwirksam nach § 177 BGB Analogie. 2. Nachtrag von GF Vansel allein — laut Satzung nur Gesamtvertretung. Wandeldarlehen NordCap § 4 verweist auf Beschluss der nicht existiert.

## Output-Module
- Unterschrifts-Befundliste mit Klasse (vollstaendig/fragwuerdig/Entwurf/unleserlich)
- Vertretungsanalyse je Partei (HR-Stand zum Unterzeichnungszeitpunkt)
- Querverweis an `dokumententyp-beschluesse` wenn Beschlussbezug betroffen
