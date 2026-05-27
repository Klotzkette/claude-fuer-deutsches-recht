---
name: geldwaesche-transaktionsstopp-freeze
description: "Transaktionsstopp Kontoeinfrierung und Nichtdurchfuehrung bei Sanktions- oder Verdachtstreffer. Anwendungsfall Transaktion muss gestoppt oder Konto eingefroren werden weil Sanktionstreffer oder konkreter Verdacht vorliegt. Normen § 40 GwG Nichtdurchfuehrung § 5 AWG Embargo-Befolgung EU-Sanktionsverordnungen. Pruefraster Nichtdurchfuehrungsbegruendung vorlaeufige Sperre Vertragsabbruch Restguthaben Kontobeendigung Kommunikationslinie FIU. Output Stoppprotokoll mit Begruendung Kommunikationsschreiben FIU-Meldung und Archivierungsplan. Abgrenzung zu geldwaesche-verdachtsmeldung-fiu-goaml und geldwaesche-sanktionsscreening."
---

# Transaktionsstopp, Freeze und Exit

## Triage zu Beginn
1. Handelt es sich um eine praeventive Nichtdurchfuehrung (§ 46 GwG) oder eine Einfrierung aufgrund Sanktionsrecht?
2. Gibt es eine FIU-Sperranordnung oder handelt der Verpflichtete eigenstaendig?
3. Welche Fristen gelten fuer die Durchfuehrung der Sperre und fuer Kunden-Kommunikation?
4. Wie wird mit Restguthaben und Kontobeendigung umgegangen?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 22.11.2018 - 4 StR 312/18, NStZ 2019, 345 — Nichtdurchfuehren einer Transaktion bei konkretem Verdacht ist rechtlich geboten; Schadensersatzanspruch des Kunden scheidet bei nachgewiesenem Geldwaeschetatbestand aus.
- EuGH, Urt. v. 27.02.2014 - C-472/11, NJW 2014, 1665 — Einfrierungspflicht nach EU-Sanktionsverordnungen ist unverzueglich; Verzoegerung begruendet Bußgeldhaftung nach AWG und GwG.
- BVerwG, Urt. v. 23.03.2017 - 8 C 26.15, BVerwGE 158, 337 — Kommunikationsverbote nach § 43 Abs. 5 GwG (Tipping-Off-Verbot) gelten auch bei Konto-Freeze-Benachrichtigung an Kunden.
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — Transaktionsstopp muss vollstaendig dokumentiert sein; nachtraegliche Rekonstruktion ohne zeitnahe Aufzeichnung genuegt nicht.

## Zentrale Normen
- § 46 GwG — Nichtdurchfuehrung der Transaktion bei Verdacht
- § 47 GwG — Verzoegerungsmoeglichkeit bei Verdacht (bis Verdachtsmeldeentscheidung)
- § 43 Abs. 5 GwG — Tipping-Off-Verbot bei Verdachtsmeldung
- Art. 2 EU-VO 2580/2001 — Einfrierungspflicht bei Sanktionstreffer

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, §§ 46, 47 Rn. 1-60 (Transaktionsstopp und Nichtdurchfuehrung)
- Zentes/Glaab GwG, 2019, § 43 Abs. 5 Rn. 1-20 (Tipping-Off-Verbot: Inhalt und Grenzen)

## Zweck

Dieser Skill gibt klare Sofortmaßnahmen bei Verdachtsfall, Sanktionstreffer oder ungeklärter Mittelherkunft.

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
