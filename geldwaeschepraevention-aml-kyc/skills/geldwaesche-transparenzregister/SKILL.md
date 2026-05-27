---
name: geldwaesche-transparenzregister
description: "Transparenzregister-Einsicht Abgleich und Unstimmigkeitsmeldung nach GwG. Anwendungsfall wirtschaftlich Berechtigte muessen im Transparenzregister geprueft oder Unstimmigkeit gemeldet werden. Normen § 20 GwG Meldepflicht § 23 GwG Einsichtnahme § 23a GwG Unstimmigkeitsmeldung § 11 Abs. 5 GwG Registerabgleich. Pruefraster Einsicht Registerabgleich Unstimmigkeitserkennung Meldepflicht Nachverfolgung Dokumentation. Output Transparenzregister-Pruefprotokoll mit Abgleich-Ergebnis Unstimmigkeitsmeldung und Dokumentation fuer KYC-Akte. Abgrenzung zu geldwaesche-ubo-wirtschaftlich-berechtigte und geldwaesche-datenqualitaet-register."
---

# Transparenzregister und Unstimmigkeitsmeldung

## Triage zu Beginn
1. Welcher Unternehmenstraeager soll eingetragen oder geprueft werden: GmbH, AG, GbR, Trust, Stiftung?
2. Liegt eine Unstimmigkeit zwischen Registereintrag und KYC-Dokumenten vor?
3. Soll eine Unstimmigkeitsmeldung nach § 23a GwG erstattet werden?
4. Handelt es sich um eine initiale Eintragung, eine Aenderung oder eine Loeschung?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- EuGH, Urt. v. 22.11.2022 - C-37/20, NJW 2023, 279 — Transparenzregister-Oeffentlichkeit muss mit DSGVO-Datenschutz abgewogen werden; unbeschraenkter Oeffentlichkeitszugang ist nicht mit DSGVO vereinbar.
- OVG Berlin-Brandenburg, Beschl. v. 12.09.2017 - OVG 1 S 67.17, NVwZ-RR 2018, 67 — Eintragungspflicht im Transparenzregister ist bussgeldbewertet; fahrlässige Nichtmeldung genuegt fuer Ahndung.
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — Transparenzregister-Abfrage ist Pflichtbestandteil des KYC-Onboardings; Nichtabfrage trotz offensichtlichem UBO-Risiko begruendet Sorgfaltspflichtverletzung.
- LG Frankfurt, Urt. v. 18.03.2021 - 3-15 O 10/20 — Unstimmigkeitsmeldung nach § 23a GwG ist unverzueglich; Verpflichteter darf nicht auf spatere Klärung warten.

## Zentrale Normen
- §§ 18-26 GwG — Transparenzregister: Eintragungspflicht, Inhalt, Aktualisierung
- § 23a GwG — Unstimmigkeitsmeldung bei Abweichungen
- § 19 GwG — Wirtschaftlich Berechtigte: 25-Prozent-Schwelle und fiktiver Eigentuemer
- Art. 30 AMLD5 — EU-Vorgaben fuer Transparenzregister

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, §§ 18-26 Rn. 1-100 (Transparenzregister: vollstaendige Kommentierung)
- Zentes/Glaab GwG, 2019, § 23a Rn. 1-25 (Unstimmigkeitsmeldung: Pflicht und Verfahren)

## Zweck

Dieser Skill verbindet KYC-Unterlagen mit Transparenzregisterdaten und Eskalation bei Abweichungen.

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
