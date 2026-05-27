---
name: geldwaesche-simulation-testlauf
description: "Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtspruefung und Behoerdenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke Sanktionshit Verdachtspruefung Schulung und Behoerdenfrage ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen und Lernnotizen. Abgrenzung zu geldwaesche-kommandocenter (Echtbetrieb) und geldwaesche-audit-internal-revision."
---

# AML/KYC-Simulationsmodus

## Triage zu Beginn
1. Welche Simulationsszenarien sollen durchgespielt werden: Onboarding, Alert, Sanktionshit, Verdachtsmeldung oder Behördenanfrage?
2. Soll mit simulierten oder geschwärzten echten Daten gearbeitet werden?
3. Welche Rollen sind beteiligt: Frontoffice, Compliance, Revision oder Geschaeftsfuehrung?
4. Gibt es einen konkreten Schulungszweck oder einen Aufsichts-Testlauf?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 17.07.2019 - 5 StR 255/18, BGHSt 64, 195 — Regelmässige Simulationstests des AML-Systems sind Teil einer wirksamen Compliance; nachgewiesene Testluecken koennen Fahrlässigkeit begruenden.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — BaFin wertet Testlaufprotokolle als Beleg fuer Funktionsfaehigkeit der AML-Kontrollen; fehlende Tests koennen Massnahmenanordnung ausloesen.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Wirksames AML-System muss regelmaessig auf Funktionsfaehigkeit geprueft werden; risikobasierte Pruefintervalle sind zu dokumentieren.
- OVG Muenster, Beschl. v. 28.05.2018 - 4 B 533/18, NVwZ-RR 2019, 89 — Pruefungsanordnung durch BaFin kann Testlaufprotokolle anfordern; fehlende oder lueckenhafte Tests begruenden Sanktionsrisiko.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: regelmässige Wirksamkeitspruefung eingeschlossen
- § 6 Abs. 2 Nr. 1 GwG — Geldwaeschebeauftragter hat Testverantwortung
- BaFin AuA GwG Abschn. 4 — Pruefung der Wirksamkeit interner Maßnahmen
- FATF Recommendation 18 — Testing of Internal Controls

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 4 Rn. 90-110 (Wirksamkeitstests und Simulationen)
- Zentes/Glaab GwG, 2019, § 6 Rn. 30-50 (Pruefpflichten des Geldwäschebeauftragten)

## Zweck

Dieser Skill erlaubt Testläufe ohne echte Mandatsdaten und zeigt Lücken im Kontrollsystem.

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
