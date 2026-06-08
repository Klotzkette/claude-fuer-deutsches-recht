---
name: unterschriftspruefung
description: "Prueft, soweit aus den Dokumenten ersichtlich, ob die jeweils erforderlichen Parteien unterschrieben haben. Markiert fehlende Unterschriften, unklare Unterzeichner und Vertretungsfragen. Trifft keine Rechtswirksamkeitsbewertung."
---

# Unterschriftspruefung

## Rolle und Fokus
Prueft, soweit aus den Dokumenten ersichtlich, ob die erforderlichen Parteien unterschrieben haben. Markiert fehlende Unterschriften, unklare Unterzeichner, Vertretungsfragen. Keine Wirksamkeitspruefung.

## Vorgehen

1. **Unterschriftsblock je Dokument identifizieren** — Wer steht da, in welcher Funktion?
2. **Abgleich mit Vertretungsregelung** — HR-Eintrag (Einzel- oder Gesamtvertretung), Prokura-Umfang, Vollmacht; Datum der Unterzeichnung gegen HR-Stand zum damaligen Zeitpunkt.
3. **Form pruefen** — Schriftform (eigenhaendige Unterschrift), Textform, qualifizierte elektronische Signatur, notarielle Beurkundung.
4. **Befund-Klassen** — `vollstaendig`, `fragwuerdig` (Anhaltspunkt fuer Vertretungsmangel), `Entwurf` (kein Unterschrift), `unleserlich`.
5. **Markierung in Reiter 2 und Querverweis** — In Anmerkungsspalte; Detail in eigenem Memo.

## Anwendungsbeispiel
LausitzStorage Unterschriftsbefunde: 1. Nachtrag Pachtvertrag LEAG nur von Prokuristin Kosturek unterzeichnet — laut HR-Auszug 18.03.2026 hat sie Gesamtprokura mit GF erforderlich, also schwebend unwirksam nach § 177 BGB Analogie. 2. Nachtrag von GF Vansel allein — laut Satzung nur Gesamtvertretung. Wandeldarlehen NordCap § 4 verweist auf Beschluss der nicht existiert.

## Output-Module
- Unterschrifts-Befundliste mit Klasse (vollstaendig/fragwuerdig/Entwurf/unleserlich)
- Vertretungsanalyse je Partei (HR-Stand zum Unterzeichnungszeitpunkt)
- Querverweis an `dokumententyp-beschluesse` wenn Beschlussbezug betroffen
