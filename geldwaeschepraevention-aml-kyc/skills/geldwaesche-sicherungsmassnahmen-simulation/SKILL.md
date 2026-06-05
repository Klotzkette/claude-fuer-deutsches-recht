---
name: geldwaesche-sicherungsmassnahmen-simulation
description: "Geldwaesche Sicherungsmassnahmen Simulation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geldwaesche Sicherungsmassnahmen Simulation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geldwaesche Sicherungsmassnahmen Simulation** im Plugin Geldwäscheprävention (AML/KYC). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geldwaesche-sicherungsmassnahmen-icp` | Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne Massnahmen § 7 GwG Gruppen-Compliance BaFin-Auslegungs- und Anwendungshinweise. Prüfraster Richtlinien Prozesse Kontrollen Eskalationen Schulungen Audit-Trail Vier-Augen-Prinzip. Output ICP-Handbuch mit Richtlinien Kontrollmatrix Eskalationswegen und Schulungsplan. Abgrenzung zu geldwäsche-risikoanalyse-unternehmen und geldwäsche-audit-internal-revision. |
| `geldwaesche-simulation-testlauf` | Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behoerdenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke Sanktionshit Verdachtsprüfung Schulung und Behoerdenfrage ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen und Lernnotizen. Abgrenzung zu geldwäsche-kommandocenter (Echtbetrieb) und geldwäsche-audit-internal-revision. |
| `geldwaesche-transaktionsmonitoring` | Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG Verdachtsmeldepflicht FATF-Guidance Typologien. Prüfraster Barzahlungen Split-Payments Offshore-Strukturen Durchlaufkonten Round-Tripping ungewoehnliche Geschäftslogik. Output Transaktions-Risikoprotokoll mit Red-Flag-Kennzeichnung Schwellenwertberechnung und Meldeprüfung. Abgrenzung zu geldwäsche-sanktionsscreening und geldwäsche-verdachtsmeldung-fiu-goaml. |

## Arbeitsweg

Im Plugin Geldwäscheprävention (AML/KYC) gilt für **Geldwaesche Sicherungsmassnahmen Simulation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geldwaesche-sicherungsmassnahmen-icp`

**Fokus:** Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne Massnahmen § 7 GwG Gruppen-Compliance BaFin-Auslegungs- und Anwendungshinweise. Prüfraster Richtlinien Prozesse Kontrollen Eskalationen Schulungen Audit-Trail Vier-Augen-Prinzip. Output ICP-Handbuch mit Richtlinien Kontrollmatrix Eskalationswegen und Schulungsplan. Abgrenzung zu geldwäsche-risikoanalyse-unternehmen und geldwäsche-audit-internal-revision.

# Interne Sicherungsmaßnahmen und ICP

## Triage zu Beginn
1. Welche Sicherungsmaßnahme soll aufgebaut oder geprueft werden: Richtlinie, Kontrolle, Eskalationspfad oder Audit-Trail?
2. Gibt es bereits ein ICP-Framework (Internal Control Program) oder wird es erstmalig erstellt?
3. Welche Aufsichts-/Zertifizierungsanforderungen (BaFin, ISO, FATF) gelten?
4. Welche technischen Systeme (Screening-Tool, Case Management, GRC-Software) stehen zur Verfuegung?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: vollstaendige Pflichtkataloge
- § 6 GwG — Pflichten der Geschaeftsleitung zur Einrichtung wirksamer Kontrollen
- BaFin MaRisk AT 8.2 — Anforderungen an interne Kontrollsysteme (analoger Standard fuer AML)
- FATF Recommendation 18 — Internal Controls, Compliance and Audit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill übersetzt Risikoanalyse in ein funktionierendes Compliance-System nach GwG.

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

## 2. `geldwaesche-simulation-testlauf`

**Fokus:** Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behoerdenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke Sanktionshit Verdachtsprüfung Schulung und Behoerdenfrage ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen und Lernnotizen. Abgrenzung zu geldwäsche-kommandocenter (Echtbetrieb) und geldwäsche-audit-internal-revision.

# AML/KYC-Simulationsmodus

## Triage zu Beginn
1. Welche Simulationsszenarien sollen durchgespielt werden: Onboarding, Alert, Sanktionshit, Verdachtsmeldung oder Behördenanfrage?
2. Soll mit simulierten oder geschwärzten echten Daten gearbeitet werden?
3. Welche Rollen sind beteiligt: Frontoffice, Compliance, Revision oder Geschaeftsfuehrung?
4. Gibt es einen konkreten Schulungszweck oder einen Aufsichts-Testlauf?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: regelmässige Wirksamkeitspruefung eingeschlossen
- § 6 Abs. 2 Nr. 1 GwG — Geldwaeschebeauftragter hat Testverantwortung
- BaFin AuA GwG Abschn. 4 — Pruefung der Wirksamkeit interner Maßnahmen
- FATF Recommendation 18 — Testing of Internal Controls

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## 3. `geldwaesche-transaktionsmonitoring`

**Fokus:** Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG Verdachtsmeldepflicht FATF-Guidance Typologien. Prüfraster Barzahlungen Split-Payments Offshore-Strukturen Durchlaufkonten Round-Tripping ungewoehnliche Geschäftslogik. Output Transaktions-Risikoprotokoll mit Red-Flag-Kennzeichnung Schwellenwertberechnung und Meldeprüfung. Abgrenzung zu geldwäsche-sanktionsscreening und geldwäsche-verdachtsmeldung-fiu-goaml.

# Transaktionsmonitoring und Red Flags

## Triage zu Beginn
1. Handelt es sich um einen automatisierten Alert oder eine manuelle Auffaelligkeit?
2. Welche Muster sind erkannt: Smurfing, Roundtripping, Cash Structuring, Offshore-Routing?
3. Gibt es historische Transaktionsdaten fuer einen Musterabgleich (90-Tage-Fenster, Jahresdurchschnitt)?
4. Liegt der Alert bereits bei FIU-Meldepflicht-Schwelle oder noch in Pre-Suspicion-Phase?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 25h KWG — Pflicht zur Einrichtung Transaktionsmonitoring fuer Kreditinstitute
- § 43 GwG — Meldepflicht bei Verdacht; Monitoring als Fruehwarnsystem
- BaFin-Rundschreiben 5/2021 (BA) — Anforderungen an Transaktionsmonitoring-Systeme
- FATF Typologies Report 2022 — Aktuelle Geldwäsche-Transaktionsmuster

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
