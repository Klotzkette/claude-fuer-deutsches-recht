---
name: geldwaesche-verdachtsmeldung-fiu-goaml
description: "Vorbereitung und Einreichung von Verdachtsmeldungen nach § 43 GwG über goAML-Portal an die FIU. Anwendungsfall Sachverhalt mit Verdacht auf Geldwäsche oder Terrorismusfinanzierung ist festgestellt und Meldung muss erstattet werden. Normen § 43 GwG Meldepflicht § 44 GwG Meldeinhalte § 47 GwG Tipping-off-Verbot goAML-Merkblatt FIU. Prüfraster Sachverhaltskern Beteiligte Konten Transaktionen goAML-Felder Anlagen Dokumentationsentscheidung. Output Vollständige goAML-Verdachtsmeldung mit Sachverhaltsbeschreibung Anhalt-Tabelle und Meldungsprotokoll. Abgrenzung zu geldwäsche-transaktionsstopp-freeze und geldwäsche-transaktionsmonitoring."
---

# Verdachtsmeldung an FIU/goAML

## Triage zu Beginn
1. Liegt ein konkreter Verdacht i.S.v. § 43 GwG vor oder noch eine Abwaegungsphase?
2. Was ist der Sachverhaltskern der Verdachtsmeldung in ein bis zwei Saetzen?
3. Welche Belege (Transaktionsdaten, KYC-Dokumente, Screeningprotokolle) liegen vor?
4. Ist das Tipping-Off-Verbot (§ 43 Abs. 5 GwG) relevant — darf der Kunde informiert werden?

## Aktuelle Rechtsprechung und Behoerdenpraxis

Stand 05/2026. Rechtsprechung im Mandat live verifizieren.

- BaFin-AuA zum GwG, Stand 06.03.2025 — anwendbar seit Februar 2025; ergänzte Hinweise zu Kryptowertetransfers/selbst gehosteten Adressen — [bafin.de](https://www.bafin.de/SharedDocs/Downloads/DE/Auslegungsentscheidung/dl-ae-auas-2025-gw.html).
- FIU-Jahresberichte und Typologiepapiere — [fiu.bund.de](https://www.zoll.de/DE/FIU/fiu_node.html).
- AMLR (EU) 2024/1624 — wird das nationale Meldewesen ab 10.07.2027 weitgehend europäisieren; Verdachtsmeldung verbleibt in nationaler FIU-Zuständigkeit, formale Anforderungen folgen den europäischen Standards.

## Zentrale Normen
- § 43 GwG — Verdachtsmeldepflicht: Tatbestand, Fristen, Verfahren
- § 43 Abs. 5 GwG — Tipping-Off-Verbot
- § 46 GwG — Nichtdurchfuehrung der Transaktion bei Verdacht
- § 261 StGB — Geldwaesche: Hintergrundtatbestand der Meldepflicht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt von Verdachtsprüfung bis Meldungsentwurf, ohne voreilig Schuldeingeständnisse zu erzeugen.

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
