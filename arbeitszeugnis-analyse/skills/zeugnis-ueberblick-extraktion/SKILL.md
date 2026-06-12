---
name: zeugnis-ueberblick-extraktion
description: "Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbildungszeugnis. Prüfraster Arbeitgeber Arbeitnehmer Beschäftigungszeitraum Position Ausstellungsdatum Unterschriftsberechtigte Vollständigkeit. Output Strukturiertes Kopfdatenblatt mit Vollständigkeitsprüfung und Zeugnisart-Einordnung als Eingabe für alle Folge-Analyse-Skills. Abgrenzung zu zeugnisart-erkennung und notenrelevante-saetze-identifizieren."
---

# Zeugnis-Überblick und Kopfdaten-Extraktion

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Merkmal | Bedeutung | Ampel |
|---|---|---|
| Unterschrift rangniederer Person | Verdeckte Abwertung der Stellung | Rot |
| Kein Briefkopf / kein Stempel | Formfehler, möglicherweise anfechtbar | Orange |
| Datum weit nach Austritt | Zeigt Widerstand oder Nachlässigkeit | Orange |
| Vollständige Angaben, ranghöhere Unterschrift | Erwartungskonformes Zeugnis | Grün |
| Beschäftigungszeitraum weicht von Vertrag ab | Klärungsbedarf | Orange |

## Beispiele

**Beispiel 1 – Vollständige Kopfdaten (Grün):** "Frau Sabine Müller, geboren am 12. März 1985, war vom 1. April 2018 bis zum 31. März 2024 in unserem Unternehmen als Abteilungsleiterin Marketing tätig." — Alle Pflichtangaben vorhanden.

**Beispiel 2 – Fehlende Positionsangabe (Orange):** "Herr Thomas Braun war von 2019 bis 2023 bei uns beschäftigt." — Keine Positionsbezeichnung, kein vollständiges Datum.

**Beispiel 3 – Unterschrift Sachbearbeiter (Rot):** Unterschrift eines HR-Sachbearbeiters für einen ausscheidenden Abteilungsleiter — hierarchisches Missverhältnis signalisiert Abwertung.

**Beispiel 4 – Datum vor Austritt (Orange):** Ausstellungsdatum liegt drei Monate vor dem angegebenen letzten Arbeitstag — formale Unstimmigkeit.

**Beispiel 5 – Zwischenzeugnis ohne Enddatum (Grün):** Kein Enddatum bei einem als Zwischenzeugnis bezeichneten Dokument — korrekt und unauffällig.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

