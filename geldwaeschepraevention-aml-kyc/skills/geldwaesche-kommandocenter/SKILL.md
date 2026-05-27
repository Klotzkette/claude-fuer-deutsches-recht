---
name: geldwaesche-kommandocenter
description: "Kommandocenter fuer alle Geldwaesche- KYC- Sanktions- und Behoerdenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen Workflow starten. Normen GwG gesamt § 43 GwG Verdachtsmeldung § 10 GwG Sorgfaltspflichten. Pruefraster Verpflichtetencheck Risikoklasse KYC-Status Sanktionsscreening Verdachtsfall Eskalation. Output Triage-Ergebnis mit Routing zum passenden Skill Statusampel und naechsten Schritten. Abgrenzung zu geldwaesche-verpflichteten-check und geldwaesche-simulation-testlauf."
---

# AML/KYC-Kommandocenter

## Triage zu Beginn
1. Handelt es sich um einen Neu-Fall (Intake), einen laufenden Fall (Update) oder einen Eskalationsfall?
2. Welcher Skill soll zuerst geladen werden: KYC-Onboarding, Verdachtsmeldung, Behoerdenverfahren oder Risikoanalyse?
3. Welche Fristen sind unmittelbar relevant (Meldepflicht § 43 GwG: unverzueglich)?
4. Sind echte oder simulierte Daten zu verarbeiten?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 17.07.2019 - 5 StR 255/18, BGHSt 64, 195 — AML-Compliance erfordert systematisches Case Management mit dokumentierter Entscheidungsspur; Einzelfallentscheidungen ohne Aktengrundlage koennen Fahrlässigkeit begruenden.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — BaFin prueft nicht nur Einzelfaelle, sondern Systemprozesse; luckenhaftes Kommandocenter-Protokoll begruendet Systemversagen.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Risikobasiertes AML-System muss alle relevanten Fallkategorien abdecken; Luecken im Routing-System verletzen 4. EU-GeldwaescheRL.
- BGH, Urt. v. 26.09.2019 - 5 StR 94/19, NStZ 2020, 222 — Bearbeitungsrueckstaende bei Verdachtspruefungen erfullen subjektiven Tatbestand des § 261 StGB (Geldwaesche durch Unterlassen).

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: Case-Management als Pflichtbestandteil
- § 7 GwG — Geldwäschebeauftragter als Fallverantwortlicher
- § 43 GwG — Verdachtsmeldung: Unverzueglichkeit als Fristmerkmal
- § 8 GwG — Aufzeichnungspflichten fuer alle Fallvorgaenge

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 4 Rn. 55-90 (Case Management als Sicherungsmassnahme)
- Bülte in: Schimansky/Bunte/Lwowski Bankrechts-Handbuch, § 145 Rn. 70-100 (AML-Fallesteuerung und Dokumentation)

## Zweck

Nutze diesen Skill als Einstieg für jedes AML/KYC-Mandat: Risikoanalyse, Kundenprüfung, wirtschaftlich Berechtigte, Sanktionsscreening, Verdachtsmeldung, Behördenverfahren oder Remediation.

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
