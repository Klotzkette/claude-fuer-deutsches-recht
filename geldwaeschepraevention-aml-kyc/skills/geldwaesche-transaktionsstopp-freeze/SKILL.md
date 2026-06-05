---
name: geldwaesche-transaktionsstopp-freeze
description: "Geldwaesche Transaktionsstopp Freeze: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geldwaesche Transaktionsstopp Freeze

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geldwaesche Transaktionsstopp Freeze** im Plugin Geldwäscheprävention (AML/KYC). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geldwaesche-transaktionsstopp-freeze` | Transaktionsstopp Kontoeinfrierung und Nichtdurchführung bei Sanktions- oder Verdachtstreffer. Anwendungsfall Transaktion muss gestoppt oder Konto eingefroren werden weil Sanktionstreffer oder konkreter Verdacht vorliegt. Normen § 40 GwG Nichtdurchführung § 5 AWG Embargo-Befolgung EU-Sanktionsverordnungen. Prüfraster Nichtdurchführungsbegründung vorlaeufige Sperre Vertragsabbruch Restguthaben Kontobeendigung Kommunikationslinie FIU. Output Stoppprotokoll mit Begründung Kommunikationsschreiben FIU-Meldung und Archivierungsplan. Abgrenzung zu geldwäsche-verdachtsmeldung-fiu-goaml und geldwäsche-sanktionsscreening. |
| `geldwaesche-transparenzregister` | Transparenzregister-Einsicht Abgleich und Unstimmigkeitsmeldung nach GwG. Anwendungsfall wirtschaftlich Berechtigte muessen im Transparenzregister geprüft oder Unstimmigkeit gemeldet werden. Normen § 20 GwG Meldepflicht § 23 GwG Einsichtnahme § 23a GwG Unstimmigkeitsmeldung § 11 Abs. 5 GwG Registerabgleich. Prüfraster Einsicht Registerabgleich Unstimmigkeitserkennung Meldepflicht Nachverfolgung Dokumentation. Output Transparenzregister-Prüfprotokoll mit Abgleich-Ergebnis Unstimmigkeitsmeldung und Dokumentation für KYC-Akte. Abgrenzung zu geldwäsche-ubo-wirtschaftlich-berechtigte und geldwäsche-datenqualitaet-register. |
| `geldwaesche-ubo-wirtschaftlich-berechtigte` | Ermittlung wirtschaftlich Berechtigter UBO Kontrollketten und Trust-Stiftungsstrukturen nach GwG. Anwendungsfall neue Geschäftsbeziehung mit Unternehmen und wirtschaftlich Berechtigte muessen identifiziert werden. Normen § 3 GwG wirtschaftlich Berechtigter § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister. Prüfraster Eigentumsanteile ab 25 Prozent Kontrollketten Trust-Strukturen Stiftungen Nominees Transparenzregisterdaten. Output UBO-Struktur-Diagramm mit Eigentumsanteilen Kontrollrechten und KYC-Dokumentation für Akte. Abgrenzung zu geldwäsche-transparenzregister und geldwäsche-pep-hochrisikoland. |

## Arbeitsweg

Im Plugin Geldwäscheprävention (AML/KYC) gilt für **Geldwaesche Transaktionsstopp Freeze**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geldwaesche-transaktionsstopp-freeze`

**Fokus:** Transaktionsstopp Kontoeinfrierung und Nichtdurchführung bei Sanktions- oder Verdachtstreffer. Anwendungsfall Transaktion muss gestoppt oder Konto eingefroren werden weil Sanktionstreffer oder konkreter Verdacht vorliegt. Normen § 40 GwG Nichtdurchführung § 5 AWG Embargo-Befolgung EU-Sanktionsverordnungen. Prüfraster Nichtdurchführungsbegründung vorlaeufige Sperre Vertragsabbruch Restguthaben Kontobeendigung Kommunikationslinie FIU. Output Stoppprotokoll mit Begründung Kommunikationsschreiben FIU-Meldung und Archivierungsplan. Abgrenzung zu geldwäsche-verdachtsmeldung-fiu-goaml und geldwäsche-sanktionsscreening.

# Transaktionsstopp, Freeze und Exit

## Triage zu Beginn
1. Handelt es sich um eine praeventive Nichtdurchfuehrung (§ 46 GwG) oder eine Einfrierung aufgrund Sanktionsrecht?
2. Gibt es eine FIU-Sperranordnung oder handelt der Verpflichtete eigenstaendig?
3. Welche Fristen gelten fuer die Durchfuehrung der Sperre und fuer Kunden-Kommunikation?
4. Wie wird mit Restguthaben und Kontobeendigung umgegangen?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 46 GwG — Nichtdurchfuehrung der Transaktion bei Verdacht
- § 47 GwG — Verzoegerungsmoeglichkeit bei Verdacht (bis Verdachtsmeldeentscheidung)
- § 43 Abs. 5 GwG — Tipping-Off-Verbot bei Verdachtsmeldung
- Art. 2 EU-VO 2580/2001 — Einfrierungspflicht bei Sanktionstreffer

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## 2. `geldwaesche-transparenzregister`

**Fokus:** Transparenzregister-Einsicht Abgleich und Unstimmigkeitsmeldung nach GwG. Anwendungsfall wirtschaftlich Berechtigte muessen im Transparenzregister geprüft oder Unstimmigkeit gemeldet werden. Normen § 20 GwG Meldepflicht § 23 GwG Einsichtnahme § 23a GwG Unstimmigkeitsmeldung § 11 Abs. 5 GwG Registerabgleich. Prüfraster Einsicht Registerabgleich Unstimmigkeitserkennung Meldepflicht Nachverfolgung Dokumentation. Output Transparenzregister-Prüfprotokoll mit Abgleich-Ergebnis Unstimmigkeitsmeldung und Dokumentation für KYC-Akte. Abgrenzung zu geldwäsche-ubo-wirtschaftlich-berechtigte und geldwäsche-datenqualitaet-register.

# Transparenzregister und Unstimmigkeitsmeldung

## Triage zu Beginn
1. Welcher Unternehmenstraeager soll eingetragen oder geprueft werden: GmbH, AG, GbR, Trust, Stiftung?
2. Liegt eine Unstimmigkeit zwischen Registereintrag und KYC-Dokumenten vor?
3. Soll eine Unstimmigkeitsmeldung nach § 23a GwG erstattet werden?
4. Handelt es sich um eine initiale Eintragung, eine Aenderung oder eine Loeschung?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 18-26 GwG — Transparenzregister: Eintragungspflicht, Inhalt, Aktualisierung
- § 23a GwG — Unstimmigkeitsmeldung bei Abweichungen
- § 19 GwG — Wirtschaftlich Berechtigte: 25-Prozent-Schwelle und fiktiver Eigentuemer
- Art. 30 AMLD5 — EU-Vorgaben fuer Transparenzregister

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bearbeitet KYC-Unterlagen mit Transparenzregisterdaten und Eskalation bei Abweichungen.

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

## 3. `geldwaesche-ubo-wirtschaftlich-berechtigte`

**Fokus:** Ermittlung wirtschaftlich Berechtigter UBO Kontrollketten und Trust-Stiftungsstrukturen nach GwG. Anwendungsfall neue Geschäftsbeziehung mit Unternehmen und wirtschaftlich Berechtigte muessen identifiziert werden. Normen § 3 GwG wirtschaftlich Berechtigter § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister. Prüfraster Eigentumsanteile ab 25 Prozent Kontrollketten Trust-Strukturen Stiftungen Nominees Transparenzregisterdaten. Output UBO-Struktur-Diagramm mit Eigentumsanteilen Kontrollrechten und KYC-Dokumentation für Akte. Abgrenzung zu geldwäsche-transparenzregister und geldwäsche-pep-hochrisikoland.

# Wirtschaftlich Berechtigte und UBO

## Triage zu Beginn
1. Handelt es sich um eine einfache oder komplexe Eigentumsstruktur (Ketten, Trusts, Stiftungen, Nominees)?
2. Welche Quellen fuer die UBO-Ermittlung stehen zur Verfuegung: Transparenzregister, KYC-Dokumente, Registerauszuege?
3. Liegt ein Nominee-Hinweis oder eine Treuhandstruktur vor, die transparent gemacht werden muss?
4. Gibt es Indikatoren dafuer, dass der angegebene UBO nicht der tatsaechliche wirtschaftlich Berechtigte ist?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 3 GwG — Wirtschaftlich Berechtigter: Definition und 25-Prozent-Schwelle
- § 13 GwG — Pflicht zur Ermittlung des wirtschaftlich Berechtigten
- § 19 GwG — Transparenzregister: fiktiver wirtschaftlich Berechtigter bei fehlender Identifizierbarkeit
- Art. 3 AMLD5 — UBO-Definitionen im EU-Recht (Erweiterungen auf Trusts und Stiftungen)

## Normfokus und Praxis (UBO-Ermittlung)
- 25 %-Schwelle (§ 3 Abs. 2 GwG): direkt oder mittelbar Kapital-/Stimmrechtsmehrheit oder vergleichbare Kontrolle (z. B. Aufsichtsratsbestimmungsrecht, Gewinnverteilung). Bei mehrstufigen Beteiligungen Multiplikationsprinzip (z. B. 60 % x 50 % = 30 % indirekt — UBO).
- Fiktiver UBO (§ 3 Abs. 2 Satz 5 GwG): wenn kein natürlicher UBO ermittelbar oder keine 25 % erreicht, gilt der gesetzliche Vertreter (Geschäftsführer, Vorstand) als fiktiver UBO; dies entbindet aber nicht von der Pflicht, alle Versuche zur Ermittlung zu dokumentieren.
- Trusts/Stiftungen (§ 3 Abs. 3 GwG): jeder Treugeber, Treuhänder, Protector, Begünstigter und Person mit Bestimmungsbefugnis. Bei diskretionären Trusts: gesamte Begünstigtenklasse.
- EuGH 22.11.2022 (C-37/20, C-601/20, WM): öffentlicher Zugang zum Transparenzregister durch jedermann nicht zulässig — seitdem berechtigtes Interesse erforderlich (§ 23 GwG); kommerzielle Datenanbieter dürfen Daten nur eingeschränkt nutzen.
- Praktiker-Tipp: UBO-Diagramm erstellen mit Eigentumsanteilen, Kontrollrechten, ggf. Aktionärsvereinbarungen; Quellen dokumentieren (Handelsregister, Transparenzregister, KYC-Fragebogen, Gesellschaftsvertrag, Aktionärsregister); bei Diskrepanz Transparenzregister vs. KYC: Mitteilungsmeldung an Bundesanzeiger (§ 23a GwG, Discrepancy Reporting) zwingend.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill erzeugt eine prüfbare UBO-Karte mit Registerabgleich und offenen Nachweisen.

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
