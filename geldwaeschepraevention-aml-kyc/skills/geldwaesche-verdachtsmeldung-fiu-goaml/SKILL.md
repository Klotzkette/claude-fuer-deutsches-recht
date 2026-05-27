---
name: geldwaesche-verdachtsmeldung-fiu-goaml
description: "Vorbereitung und Einreichung von Verdachtsmeldungen nach § 43 GwG ueber goAML-Portal an die FIU. Anwendungsfall Sachverhalt mit Verdacht auf Geldwaesche oder Terrorismusfinanzierung ist festgestellt und Meldung muss erstattet werden. Normen § 43 GwG Meldepflicht § 44 GwG Meldeinhalte § 47 GwG Tipping-off-Verbot goAML-Merkblatt FIU. Pruefraster Sachverhaltskern Beteiligte Konten Transaktionen goAML-Felder Anlagen Dokumentationsentscheidung. Output Vollstaendige goAML-Verdachtsmeldung mit Sachverhaltsbeschreibung Anhalt-Tabelle und Meldungsprotokoll. Abgrenzung zu geldwaesche-transaktionsstopp-freeze und geldwaesche-transaktionsmonitoring."
---

# Verdachtsmeldung an FIU/goAML

## Triage zu Beginn
1. Liegt ein konkreter Verdacht i.S.v. § 43 GwG vor oder noch eine Abwaegungsphase?
2. Was ist der Sachverhaltskern der Verdachtsmeldung in ein bis zwei Saetzen?
3. Welche Belege (Transaktionsdaten, KYC-Dokumente, Screeningprotokolle) liegen vor?
4. Ist das Tipping-Off-Verbot (§ 43 Abs. 5 GwG) relevant — darf der Kunde informiert werden?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 26.09.2019 - 5 StR 94/19, NStZ 2020, 222 — Unverzueglichkeit der Verdachtsmeldung setzt voraus, dass Meldepflicht unmittelbar nach Entstehen des Verdachts erfuellt wird; interne Bearbeitungszeit von mehr als 3 Tagen ist rechtfertigungspflichtig.
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — Unterlassene Verdachtsmeldung bei nachgewiesenem Tatverdacht begruendet Beihilfestrafbarkeit nach § 261 StGB i.V.m. § 43 GwG.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Verdachtsmeldepflicht nach AMLD4 ist eigenstaendige Pflicht unabhaengig vom Ausgang des Strafverfahrens; Meldung schließt Strafverfolgung des Verpflichteten in der Regel aus.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — goAML-Formular muss vollstaendig ausgefuellt sein; lueckenhafte oder fehlerhafte Meldungen werden von FIU zurueckgewiesen und loesen erneute Meldepflicht aus.

## Zentrale Normen
- § 43 GwG — Verdachtsmeldepflicht: Tatbestand, Fristen, Verfahren
- § 43 Abs. 5 GwG — Tipping-Off-Verbot
- § 46 GwG — Nichtdurchfuehrung der Transaktion bei Verdacht
- § 261 StGB — Geldwaesche: Hintergrundtatbestand der Meldepflicht

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 43 Rn. 1-80 (Verdachtsmeldung: Tatbestand und Verfahren)
- Zentes/Glaab GwG, 2019, § 43 Rn. 40-80 (goAML: Formular, Inhalt, Fristen)

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
