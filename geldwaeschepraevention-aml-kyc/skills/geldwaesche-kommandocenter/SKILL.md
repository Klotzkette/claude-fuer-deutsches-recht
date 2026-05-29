---
name: geldwaesche-kommandocenter
description: "Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behoerdenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen Workflow starten. Normen GwG gesamt § 43 GwG Verdachtsmeldung § 10 GwG Sorgfaltspflichten. Prüfraster Verpflichtetencheck Risikoklasse KYC-Status Sanktionsscreening Verdachtsfall Eskalation. Output Triage-Ergebnis mit Routing zum passenden Skill Statusampel und naechsten Schritten. Abgrenzung zu geldwäsche-verpflichteten-check und geldwäsche-simulation-testlauf."
---

# AML/KYC-Kommandocenter

## Triage zu Beginn
1. Handelt es sich um einen Neu-Fall (Intake), einen laufenden Fall (Update) oder einen Eskalationsfall?
2. Welcher Skill soll zuerst geladen werden: KYC-Onboarding, Verdachtsmeldung, Behoerdenverfahren oder Risikoanalyse?
3. Welche Fristen sind unmittelbar relevant (Meldepflicht § 43 GwG: unverzueglich)?
4. Sind echte oder simulierte Daten zu verarbeiten?

## Aktuelle Rechtsprechung und Behoerdenpraxis

Stand 05/2026. Rechtsprechung im Mandat live verifizieren — Aktenzeichen nicht aus Modellwissen.

**EU-AML-Paket — Geltung und Übergang:**
- VO (EU) 2024/1624 (AMLR / EU-Geldwäscheverordnung) — **anwendbar ab 10.07.2027**; ersetzt weite Teile des nationalen GwG.
- RL (EU) 2024/1640 (6. Geldwäsche-RL) — regelt nationale Aufsichtsstrukturen, Register, FIU, Sanktionen; Umsetzungsfrist läuft.
- VO (EU) 2024/1620 (AMLA-VO) — Errichtung der AMLA (Anti-Money Laundering Authority) mit Sitz in Frankfurt am Main; operativ aktiv seit 01.07.2025; übernimmt 2026 zentrale AML/CFT-Mandate von der EBA; direkte Aufsicht über ausgewählte Verpflichtete ab 2028.

**BaFin Auslegungs- und Anwendungshinweise zum GwG (AuA AT):**
- BaFin-AuA aktualisiert: Veröffentlichung 29.11.2024; ergänzende Veröffentlichung 06.03.2025 mit Berücksichtigung des Finanzmarktdigitalisierungsgesetzes vom 27.12.2024 (insbesondere Kryptowertetransfers, selbst gehostete Adressen). Anwendung ab Februar 2025. Aktualität über [bafin.de](https://www.bafin.de/SharedDocs/Downloads/DE/Auslegungsentscheidung/dl-ae-auas-2025-gw.html) prüfen.

**Übergangsphase Verpflichtete:** Während 2026/2027 gelten parallele Regime — bis 10.07.2027 nationales GwG mit BaFin-AuA; ab 10.07.2027 unmittelbar geltende AMLR. Compliance-Programme sollten Migration vorbereiten (Dokumentation, Schulungen, ICP-Anpassung).

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: Case-Management als Pflichtbestandteil
- § 7 GwG — Geldwäschebeauftragter als Fallverantwortlicher
- § 43 GwG — Verdachtsmeldung: Unverzueglichkeit als Fristmerkmal
- § 8 GwG — Aufzeichnungspflichten fuer alle Fallvorgaenge

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
