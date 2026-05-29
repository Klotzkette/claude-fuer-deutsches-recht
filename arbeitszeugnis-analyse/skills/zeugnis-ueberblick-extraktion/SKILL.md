---
name: zeugnis-ueberblick-extraktion
description: "Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbildungszeugnis. Prüfraster Arbeitgeber Arbeitnehmer Beschaeftigungszeitraum Position Ausstellungsdatum Unterschriftsberechtigte Vollständigkeit. Output Strukturiertes Kopfdatenblatt mit Vollständigkeitsprüfung und Zeugnisart-Einordnung als Eingabe für alle Folge-Analyse-Skills. Abgrenzung zu zeugnisart-erkennung und notenrelevante-saetze-identifizieren."
---

# Zeugnis-Überblick und Kopfdaten-Extraktion

Dieser Skill liest ein deutsches Arbeitszeugnis und extrahiert systematisch alle Kopfdaten, bevor die inhaltliche Analyse beginnt. Vollständige Kopfdaten sind Voraussetzung für jede weitere Bewertung, da fehlende Angaben bereits eigenständige Hinweise auf die Qualität des Zeugnisses liefern können.

Ein qualifiziertes Zeugnis nach § 109 Abs. 1 Satz 3 GewO muss Angaben zu Art und Dauer der Tätigkeit sowie zu Leistung und Verhalten enthalten. Das einfache Zeugnis beschränkt sich auf Art und Dauer. Die Unterscheidung ist für die Erwartungshaltung an die Formulierungen entscheidend: Bei einem einfachen Zeugnis fehlt die Leistungsbeurteilung bewusst und ist kein negativer Hinweis.

Beim Aussteller ist zu prüfen, ob die Firma korrekt bezeichnet ist, ob ein Briefkopf vorhanden ist und ob Ort und Datum plausibel sind. Das Datum des Zeugnisses darf nicht vor dem letzten Arbeitstag liegen (bei Endzeugnis). Bei Zwischenzeugnissen wird kein Enddatum angegeben — die fehlende Angabe ist kein Fehler.

Die Unterschrift muss von einer zeichnungsberechtigten Person stammen. In der Regel sind das Geschäftsführer, Personalabteilungsleiter oder bevollmächtigte HR-Manager. Eine Unterschrift durch einen hierarchisch tiefer stehenden Mitarbeiter als den beurteilten Arbeitnehmer ist ein rotes Signal. Fehlt die Unterschrift ganz oder ist sie unleserlich ohne Namensangabe, kann das Zeugnis anfechtbar sein.

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

## Ausgabeformat

Der Skill gibt eine strukturierte Übersichtstabelle aus mit den Feldern: Arbeitgeber (Name, Rechtsform, Ort), Arbeitnehmer (Name, ggf. Geburtsdatum), Beschäftigungszeitraum (Von–Bis oder "Zwischenzeugnis"), Position/Tätigkeit, Ausstellungsdatum, Unterschriftsberechtigte(r) (Name, Titel), Zeugnisart (einfach/qualifiziert/Zwischen-/Endzeugnis). Unter der Tabelle folgt ein Hinweis auf erkannte Vollständigkeitsmängel.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
