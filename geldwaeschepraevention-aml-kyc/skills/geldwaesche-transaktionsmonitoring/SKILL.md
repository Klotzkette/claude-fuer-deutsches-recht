---
name: geldwaesche-transaktionsmonitoring
description: "Erkennung auffaelliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwaescherisiko pruefen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG Verdachtsmeldepflicht FATF-Guidance Typologien. Pruefraster Barzahlungen Split-Payments Offshore-Strukturen Durchlaufkonten Round-Tripping ungewoehnliche Geschaeftslogik. Output Transaktions-Risikoprotokoll mit Red-Flag-Kennzeichnung Schwellenwertberechnung und Meldepruefung. Abgrenzung zu geldwaesche-sanktionsscreening und geldwaesche-verdachtsmeldung-fiu-goaml."
---

# Transaktionsmonitoring und Red Flags

## Triage zu Beginn
1. Handelt es sich um einen automatisierten Alert oder eine manuelle Auffaelligkeit?
2. Welche Muster sind erkannt: Smurfing, Roundtripping, Cash Structuring, Offshore-Routing?
3. Gibt es historische Transaktionsdaten fuer einen Musterabgleich (90-Tage-Fenster, Jahresdurchschnitt)?
4. Liegt der Alert bereits bei FIU-Meldepflicht-Schwelle oder noch in Pre-Suspicion-Phase?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 26.09.2019 - 5 StR 94/19, NStZ 2020, 222 — Ungewoehliche Transaktionsmuster (split payments, roundtripping) begründen Verdacht i.S.v. § 43 GwG; Monitoring muss diese Muster erkennen.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Transaktionsmonitoring muss risikobasiert kalibriert sein; uebermässig hohe False-Positive-Rate kann auf fehlende Risikoanpassung hinweisen.
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — Barzahlungen von Immobilienkaufpreis-Teilen sind strukturbedingte Geldwaescheindikatoren; fehlende Monitoring-Reaktion begruendet Fahrlässigkeit.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — Automatisiertes Monitoring ersetzt nicht manuelle Expertise bei Alerts; jeder Treffer erfordert dokumentierte Einschaetzung.

## Zentrale Normen
- § 25h KWG — Pflicht zur Einrichtung Transaktionsmonitoring fuer Kreditinstitute
- § 43 GwG — Meldepflicht bei Verdacht; Monitoring als Fruehwarnsystem
- BaFin-Rundschreiben 5/2021 (BA) — Anforderungen an Transaktionsmonitoring-Systeme
- FATF Typologies Report 2022 — Aktuelle Geldwäsche-Transaktionsmuster

## Kommentarliteratur
- Schimansky/Bunte/Lwowski Bankrechts-Handbuch § 145 Rn. 110-140 (Transaktionsmonitoring: System und Rechtspflichten)
- Zentes/Glaab GwG, 2019, § 43 Rn. 15-40 (Schwellenwerte und Monitoring-Reaktion)

## Zweck

Dieser Skill baut ein Monitoring- und Alert-Bearbeitungsmodell mit Triage, Eskalation und Dokumentation.

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Arbeitsweise

1. **Rolle und Pflichtenkreis klären.** Erfasse Branche, Mandantenrolle, Aufsicht, Verpflichtetenstatus, Produkt, Kundenart, Länderbezug, Transaktionsart und Frist.
2. **Daten sauber ziehen.** Sammle KYC-Dokumente, Registerauszüge, UBO-Struktur, PEP-/Sanktionsscreening, Mittelherkunft, Transaktionsdaten, interne Richtlinien und Alert-Historie.
3. **Quellenstand protokollieren.** Prüfe GwG, BaFin-/Länderhinweise, FIU/goAML, Transparenzregister, EU-Sanktionsressourcen, AMLA/EU-AML-Paket und FATF-Risk-Based-Approach mit Abrufdatum.
4. **Risikobasiert entscheiden.** Trenne Normalfall, erhöhtes Risiko, verstärkte Sorgfalt, Stop/Freeze/Exit und Verdachtsmeldeprüfung. Keine automatische Freigabe bei Datenlücken.
5. **Verzeihend nachziehen.** Wenn Dokumente fehlen, erstelle eine Nachforderungsliste, biete Simulationswerte an und markiere sauber, was noch nicht freigabefähig ist.
6. **Arbeitsprodukt liefern.** Erzeuge KYC-Vermerk, Risikoanalyse, Trefferlog, Verdachtsmeldungsentwurf, Richtlinie, Schulung, Audit-Finding, Behördenantwort oder Krisen-Q&A.
7. **Qualitätstor.** Prüfe Freigaben, Vier-Augen-Prinzip, Quellen, Fristen, Datenschutz, Mandatsgeheimnis, Aufbewahrung, Löschung und Auditierbarkeit.

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Ausgabeformat

- Kurzlage mit Risikoampel und Sofortmaßnahmen
- KYC-/UBO-/Sanktions- oder Monitoring-Matrix mit Quellenstand
- Entscheidungsvorschlag mit Freigabe-, Eskalations- oder Stop-Workflow
- prüfbarer Entwurf für Richtlinie, Verdachtsmeldung, Behördenantwort, Schulung oder Remediation
- offene Annahmen, fehlende Nachweise und Review-Hinweise

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.
