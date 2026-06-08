---
name: geldwaesche-transaktionsmonitoring
description: "Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG Verdachtsmeldepflicht FATF-Guidance Typologien. Prüfraster Barzahlungen Split-Payments Offshore-Strukturen Durchlaufkonten Round-Tripping ungewoehnliche Geschäftslogik. Output Transaktions-Risikoprotokoll mit Red-Flag-Kennzeichnung Schwellenwertberechnung und Meldeprüfung. Abgrenzung zu geldwäsche-sanktionsscreening und geldwäsche-verdachtsmeldung-fiu-goaml im Geldwaeschepraevention Aml Kyc."
---

# Transaktionsmonitoring und Red Flags

## Arbeitsbereich

Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG Verdachtsmeldepflicht FATF-Guidance Typologien. Prüfraster Barzahlungen Split-Payments Offshore-Strukturen Durchlaufkonten Round-Tripping ungewoehnliche Geschäftslogik. Output Transaktions-Risikoprotokoll mit Red-Flag-Kennzeichnung Schwellenwertberechnung und Meldeprüfung. Abgrenzung zu geldwäsche-sanktionsscreening und geldwäsche-verdachtsmeldung-fiu-goaml. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Handelt es sich um einen automatisierten Alert oder eine manuelle Auffaelligkeit?
2. Welche Muster sind erkannt: Smurfing, Roundtripping, Cash Structuring, Offshore-Routing?
3. Gibt es historische Transaktionsdaten für einen Musterabgleich (90-Tage-Fenster, Jahresdurchschnitt)?
4. Liegt der Alert bereits bei FIU-Meldepflicht-Schwelle oder noch in Pre-Suspicion-Phase?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 25h KWG — Pflicht zur Einrichtung Transaktionsmonitoring für Kreditinstitute
- § 43 GwG — Meldepflicht bei Verdacht; Monitoring als Fruehwarnsystem
- BaFin-Rundschreiben 5/2021 (BA) — Anforderungen an Transaktionsmonitoring-Systeme
- FATF Typologies Report 2022 — Aktuelle Geldwäsche-Transaktionsmuster

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

