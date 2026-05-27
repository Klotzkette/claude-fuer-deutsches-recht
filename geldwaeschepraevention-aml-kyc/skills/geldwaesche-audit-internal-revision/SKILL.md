---
name: geldwaesche-audit-internal-revision
description: "Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Pruefer will AML-Kontrollsystem auf Wirksamkeit pruefen. Normen § 4 GwG interne Sicherungsmassnahmen § 6 GwG Risikomanagement FATF-Empfehlungen BaFin-Rundschreiben. Pruefraster AML-Kontrollen Stichproben Fallakten Screeningqualitaet Monitoring Verdachtsmeldungen Remediation. Output Revisionsbericht mit Befunden Massnahmenplan Priorisierung und Abschluss-Freigabe. Abgrenzung zu geldwaesche-sicherungsmassnahmen-icp (Aufbau) und geldwaesche-behoerdenverfahren (externe Pruefung)."
---

# Audit und interne Revision

## Triage zu Beginn
1. Welcher Audit-Bereich ist betroffen: KYC-Qualitaet, Transaktionsmonitoring, Verdachtsmeldungen oder Sanktionsscreening?
2. Handelt es sich um eine anlassbezogene Sonderrevision oder eine regulaere Revisionspruefung?
3. Welche Aufsichtsbehoerde und welche Berichtspflichten bestehen (BaFin, Staatsanwaltschaft, AMLA)?
4. Welcher Zeitraum und welche Stichprobenmenge sollen erfasst werden?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 18.12.2019 - 1 StR 597/18, NJW 2020, 1462 — Interne Revision muss AML-Kontrollmaengel unverzueglich an Geschaeftsleitungsebene eskalieren; Unterlassen begruendet Aufsichtspflichtverletzung.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — BaFin kann Revisionsmaengel in AML-Kontrollen selbstaendig feststellen und Massnahmenbescheide erlassen.
- BGH, Urt. v. 17.07.2019 - 5 StR 255/18, BGHSt 64, 195 — Geschaeftsleiterhaftung bei Systemversagen der AML-Kontrollen: subjektiver Vorsatz bei Kenntnis von Kontrollmaengeln.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Risikobasierter Audit-Ansatz nach 4. EU-GeldwaescheRL verpflichtet zur dokumentierten Pruefung aller risikorelevanten Kundenkategorien.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: Pflicht zur internen Revision
- § 7 GwG — Geldwäschebeauftragter und Berichtspflichten an Geschäftsleitung
- § 9 GwG — Gruppenweite Pflichten und Revisionsstandards
- § 56 GwG — Bußgeldtatbestaende bei Kontrollversagen

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 4 Rn. 1-50 (Interne Sicherungsmaßnahmen und Revision)
- Bülte in: Schimansky/Bunte/Lwowski Bankrechts-Handbuch, § 145 Rn. 30-60 (AML-Revision in Kreditinstituten)

## Zweck

Dieser Skill erzeugt Auditpläne und Findings, die Geschäftsleitung und Aufsicht nachvollziehen können.

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
