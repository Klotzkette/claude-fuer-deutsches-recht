---
name: geldwaesche-pep-hochrisikoland-risikoanalyse
description: "Geldwaesche PEP Hochrisikoland Risikoanalyse: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geldwaesche PEP Hochrisikoland Risikoanalyse

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geldwaesche PEP Hochrisikoland Risikoanalyse** im Plugin Geldwäscheprävention (AML/KYC). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geldwaesche-pep-hochrisikoland` | Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen. Normen § 15 GwG verstaerkte Sorgfaltspflichten § 1 Abs. 12 GwG PEP-Definition FATF Hochrisikoliste EU-Delegierte VO. Prüfraster PEP Familienangehoerige nahestehende Personen Hochrisikolaender Nominees Treuhandstrukturen Enhanced Due Diligence. Output Verstaerkte KYC-Akte mit PEP-Begründung EDD-Dokumentation Freigabe auf Leitungsebene. Abgrenzung zu geldwäsche-kyc-onboarding und geldwäsche-sanktionsscreening. |
| `geldwaesche-risikoanalyse-unternehmen` | Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne Sicherungsmassnahmen FATF-Empfehlungen BaFin-AuA. Prüfraster Produkte Kundenstruktur Laender Vertriebskanaele Transaktionen bestehende Kontrollen Risikoniveau. Output Risikoanalysedokument mit Risikoklassifizierung Kontrolllueckenbewertung und Massnahmenplan für Behoerdenvorlage. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp und geldwäsche-audit-internal-revision. |
| `geldwaesche-schulung-awareness` | Zielgruppengerechte AML/KYC-Schulungen und Awareness-Massnahmen nach § 6 Abs. 2 Nr. 6 GwG. Anwendungsfall jaehrliche Pflichtschulung muss durchgeführt oder neue Mitarbeiter eingearbeitet werden. Normen § 6 Abs. 2 Nr. 6 GwG Schulungspflicht BaFin-Mindestanforderungen FATF-Empfehlungen. Prüfraster Zielgruppen Inhalte Red-Flag-Karten Tests Teilnahmeprotokolle Auffrischungskonzept. Output Schulungspaket mit Kursinhalt Tests Teilnahmeprotokoll und E-Learning-Konzept. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp und geldwäsche-audit-internal-revision. |

## Arbeitsweg

Im Plugin Geldwäscheprävention (AML/KYC) gilt für **Geldwaesche PEP Hochrisikoland Risikoanalyse**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geldwaesche-pep-hochrisikoland`

**Fokus:** Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen. Normen § 15 GwG verstaerkte Sorgfaltspflichten § 1 Abs. 12 GwG PEP-Definition FATF Hochrisikoliste EU-Delegierte VO. Prüfraster PEP Familienangehoerige nahestehende Personen Hochrisikolaender Nominees Treuhandstrukturen Enhanced Due Diligence. Output Verstaerkte KYC-Akte mit PEP-Begründung EDD-Dokumentation Freigabe auf Leitungsebene. Abgrenzung zu geldwäsche-kyc-onboarding und geldwäsche-sanktionsscreening.

# PEP, Hochrisikoland und verstärkte Sorgfalt

## Triage zu Beginn
1. Ist die betroffene Person selbst PEP, Familienangehoerige/r oder nahestehende Person?
2. Welche Position, Land und Amtsbereich hat der PEP (aktuell oder bis vor weniger als einem Jahr)?
3. Ist ein Hochrisikoland nach FATF-Liste oder EU-Delegierter Verordnung betroffen?
4. Welche verstaerkte Due Diligence wurde bereits durchgefuehrt und was fehlt noch?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 15 GwG — Verstaerkte Sorgfaltspflichten: PEP, nahestehende Personen, Hochrisikotransaktionen
- § 1 Abs. 12 GwG — Definition PEP
- §§ 14-16 GwG — Vereinfachte und normale Sorgfalt: Abgrenzung
- EU-Delegierte VO (EU) 2022/229 — Hochrisikodritt-Laenderliste

## Normfokus und Praxis (PEP/EDD)
- PEP-Definition § 1 Abs. 12 GwG: politische Funktionen (Staatsoberhaupt, Minister, Parlamentarier, Verfassungsrichter, Botschafter, Generäle, Vorstandsmitglieder staatlicher Unternehmen) plus Familienangehörige (§ 1 Abs. 13 GwG) und nahestehende Personen (§ 1 Abs. 14 GwG). 12-Monats-Nachlauf nach Ende der Funktion (§ 15 Abs. 5 GwG).
- Pflichten EDD (§ 15 Abs. 4 GwG): Zustimmung Vorgesetzter, Klärung Vermögensherkunft und Geldherkunft, verstärkte laufende Überwachung; bei PEP-Kunden zwingend Senior Management Approval (i. d. R. C-Level oder MLRO).
- Hochrisikoland: konsolidierte Liste EU (Delegierte VO (EU) 2024/1657 ersetzt frühere Listen — stets aktuelle EUR-Lex-Quelle prüfen) und FATF-Black/Grey-List (Hochrisiko-/Beobachtungs­länder). Verstärkte Sorgfalt zwingend bei Geschäftsbeziehung/Transaktion mit Bezug zu diesen Ländern (§ 15 Abs. 3 Nr. 2 GwG).
- Konzern-Roll-out: Gruppenweite Compliance nach § 9 GwG — einheitliche PEP-Datenbank, Drittanbieter (Refinitiv World-Check, Dow Jones, LexisNexis) mit dokumentierter Datenqualität.
- Praktiker-Tipp: PEP-Treffer nicht automatisch ablehnen — sondern Fact-Check (richtige Person? Alias?), Senior Approval mit Memo "Warum trotz PEP-Status Geschäftsbeziehung tragbar", regelmäßiges Refresh (mind. einmal pro Jahr, bei kritischem Profil halbjährlich). Mittelherkunft mit Belegen (Steuerbescheid, Verkaufsurkunde, Erbschein) — nicht nur Selbstauskunft.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill entscheidet nicht pauschal, sondern führt durch Risikofaktoren, Freigaben und laufende Überwachung.

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

## 2. `geldwaesche-risikoanalyse-unternehmen`

**Fokus:** Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne Sicherungsmassnahmen FATF-Empfehlungen BaFin-AuA. Prüfraster Produkte Kundenstruktur Laender Vertriebskanaele Transaktionen bestehende Kontrollen Risikoniveau. Output Risikoanalysedokument mit Risikoklassifizierung Kontrolllueckenbewertung und Massnahmenplan für Behoerdenvorlage. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp und geldwäsche-audit-internal-revision.

# Unternehmensweite Risikoanalyse

## Triage zu Beginn
1. Welche Branche und welche Verpflichteten-Kategorie trifft die Risikoanalyse?
2. Welche Risikofelder sollen abgedeckt werden: Kunden, Produkte, Vertriebskanaele, Laender, Transaktionen?
3. Liegt bereits eine Risikoanalyse vor, die aktualisiert werden soll, oder wird sie erstmalig erstellt?
4. Gibt es eine spezifische BaFin-/Aufsichtsvorgabe oder FATF-Leitlinie fuer diesen Sektor?

## Aktuelle Rechtsprechung und Behoerdenpraxis

Stand 05/2026:

- BaFin-AuA GwG (Allgemeiner Teil, AuA AT) — Veröffentlichung 29.11.2024; Ergänzung 06.03.2025 (Kryptowertetransfers, selbst gehostete Adressen) — anwendbar seit Februar 2025 — [bafin.de](https://www.bafin.de/SharedDocs/Downloads/DE/Auslegungsentscheidung/dl-ae-auas-2025-gw.html).
- EuGH, Urt. v. 13.02.2025 — C-383/23 (ILVA) — Unternehmensbegriff im wettbewerbsrechtlichen Sinne für DSGVO-Bußgeldobergrenze; methodisch übertragbar auf Bußgelder anderer EU-Sekundärrechtsakte mit ähnlicher Bußgeldsystematik.
- AMLA seit 01.07.2025 operativ; AMLR (EU) 2024/1624 ab 10.07.2027 anwendbar; Risikoanalyse-Anforderungen sind weiter strukturiert (Art. 7 ff. AMLR) — strategisch Migrationsplan anlegen.

Rechtsprechung im Mandat live verifizieren — keine Aktenzeichen aus Modellwissen.

## Zentrale Normen
- § 5 GwG — Unternehmenseigene Risikoanalyse: Pflichtinhalt und Aktualisierung
- § 4 Abs. 1 GwG — Interne Sicherungsmaßnahmen als Folge der Risikoanalyse
- FATF Guidance — Risk-Based Approach fuer Finanzinstitutionen (2021)
- BaFin-Auslegungs- und Anwendungshinweise (AuA) GwG — Risikoanalysevorgaben

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill macht § 5 GwG operationalisierbar: Risikoidentifikation, Bewertung, Maßnahmen, Freigabe, Aktualisierung und Dokumentation.

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

## 3. `geldwaesche-schulung-awareness`

**Fokus:** Zielgruppengerechte AML/KYC-Schulungen und Awareness-Massnahmen nach § 6 Abs. 2 Nr. 6 GwG. Anwendungsfall jaehrliche Pflichtschulung muss durchgeführt oder neue Mitarbeiter eingearbeitet werden. Normen § 6 Abs. 2 Nr. 6 GwG Schulungspflicht BaFin-Mindestanforderungen FATF-Empfehlungen. Prüfraster Zielgruppen Inhalte Red-Flag-Karten Tests Teilnahmeprotokolle Auffrischungskonzept. Output Schulungspaket mit Kursinhalt Tests Teilnahmeprotokoll und E-Learning-Konzept. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp und geldwäsche-audit-internal-revision.

# Schulung und Awareness

## Triage zu Beginn
1. Welche Zielgruppe soll geschult werden: Frontoffice, Compliance, Revisoren oder Geschaeftsfuehrung?
2. Welche Schulungsform ist gefragt: Praesenzschulung, E-Learning, Quiz, Fallstudie oder Auffrischungserinnerung?
3. Gibt es aktuelle Red Flags oder Vorfaelle, die in die Schulung eingearbeitet werden sollen?
4. Muss die Schulung Teilnahme und Pruefung protokollieren (Nachweis fuer Aufsicht)?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 Abs. 3 GwG — Mitarbeiterschulung als Pflichtbestandteil interner Sicherungsmaßnahmen
- § 7 GwG — Geldwäschebeauftragter hat Schulungsverantwortung
- BaFin AuA GwG Abschn. 4.3 — Mindestanforderungen an AML-Schulungen
- § 6 Abs. 3 Nr. 1 GwG — Schulung als Teil des risikobasierten Ansatzes

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill macht Geldwäscheprävention verständlich, wiederholbar und prüfbar.

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
