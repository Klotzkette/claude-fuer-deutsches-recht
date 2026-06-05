---
name: geldwaesche-audit-internal-datenqualitaet
description: "Geldwaesche Audit Internal Datenqualitaet: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geldwaesche Audit Internal Datenqualitaet

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geldwaesche Audit Internal Datenqualitaet** im Plugin Geldwäscheprävention (AML/KYC). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geldwaesche-audit-internal-revision` | Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer will AML-Kontrollsystem auf Wirksamkeit prüfen. Normen § 4 GwG interne Sicherungsmassnahmen § 6 GwG Risikomanagement FATF-Empfehlungen BaFin-Rundschreiben. Prüfraster AML-Kontrollen Stichproben Fallakten Screeningqualitaet Monitoring Verdachtsmeldungen Remediation. Output Revisionsbericht mit Befunden Massnahmenplan Priorisierung und Abschluss-Freigabe. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp (Aufbau) und geldwäsche-behoerdenverfahren (externe Prüfung). |
| `geldwaesche-datenqualitaet-register` | Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister § 23a GwG Unstimmigkeitsmeldung. Prüfraster Datenfelder Dubletten Schreibweisen Registerquellen Trefferqualitaet Auditierbarkeit. Output Datenqualitaetsbericht mit Bereinigungsliste Dubletten-Protokoll und Transparenzregister-Abgleich. Abgrenzung zu geldwäsche-ubo-wirtschaftlich-berechtigte und geldwäsche-transparenzregister. |
| `geldwaesche-immobilien-gueterhaendler` | AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. Normen § 2 Abs. 1 Nr. 14 GwG Immobilienmakler § 2 Abs. 1 Nr. 16 GwG Gueterhaendler § 4 GwG interne Sicherungsmassnahmen. Prüfraster Verpflichtetenstatus Risikoanalyse Identifizierung Transaktionsschwellen Barzahlungsverbot. Output KYC-Prozessdesign mit Risikoeinstufung Identifizierungsprotokoll und Barzahlungsregel-Dokumentation. Abgrenzung zu geldwäsche-kyc-onboarding und geldwäsche-risikoanalyse-unternehmen. |

## Arbeitsweg

Im Plugin Geldwäscheprävention (AML/KYC) gilt für **Geldwaesche Audit Internal Datenqualitaet**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geldwaesche-audit-internal-revision`

**Fokus:** Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer will AML-Kontrollsystem auf Wirksamkeit prüfen. Normen § 4 GwG interne Sicherungsmassnahmen § 6 GwG Risikomanagement FATF-Empfehlungen BaFin-Rundschreiben. Prüfraster AML-Kontrollen Stichproben Fallakten Screeningqualitaet Monitoring Verdachtsmeldungen Remediation. Output Revisionsbericht mit Befunden Massnahmenplan Priorisierung und Abschluss-Freigabe. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp (Aufbau) und geldwäsche-behoerdenverfahren (externe Prüfung).

# Audit und interne Revision

## Triage zu Beginn
1. Welcher Audit-Bereich ist betroffen: KYC-Qualitaet, Transaktionsmonitoring, Verdachtsmeldungen oder Sanktionsscreening?
2. Handelt es sich um eine anlassbezogene Sonderrevision oder eine regulaere Revisionspruefung?
3. Welche Aufsichtsbehoerde und welche Berichtspflichten bestehen (BaFin, Staatsanwaltschaft, AMLA)?
4. Welcher Zeitraum und welche Stichprobenmenge sollen erfasst werden?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: Pflicht zur internen Revision
- § 7 GwG — Geldwäschebeauftragter und Berichtspflichten an Geschäftsleitung
- § 9 GwG — Gruppenweite Pflichten und Revisionsstandards
- § 56 GwG — Bußgeldtatbestaende bei Kontrollversagen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill erzeugt Auditpläne und Findings, die Geschäftsleitung und Aufsicht nachvollziehen können.

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

## 2. `geldwaesche-datenqualitaet-register`

**Fokus:** Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister § 23a GwG Unstimmigkeitsmeldung. Prüfraster Datenfelder Dubletten Schreibweisen Registerquellen Trefferqualitaet Auditierbarkeit. Output Datenqualitaetsbericht mit Bereinigungsliste Dubletten-Protokoll und Transparenzregister-Abgleich. Abgrenzung zu geldwäsche-ubo-wirtschaftlich-berechtigte und geldwäsche-transparenzregister.

# Datenqualität, Register und Screening-Tools

## Triage zu Beginn
1. Welche Datenfelder oder Registerquellen weisen Qualitaetsprobleme auf?
2. Handelt es sich um Dubletten, fehlende Pflichtfelder, falsche Schreibweisen oder veraltete Eintraege?
3. Welches Screening-Tool ist betroffen und welche Trefferquoten sollen verbessert werden?
4. Gibt es einen Audit-Trail-Anforderung oder eine Behoerdenpruefung zu den Daten?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 10 GwG — Allgemeine Sorgfaltspflichten: Identifizierung und Ueberpruefung von Kundendaten
- §§ 18-26 GwG — Transparenzregister: Eintragungspflicht und Richtigkeit
- § 23a GwG — Unstimmigkeitsmeldung an Transparenzregister
- Art. 5 DSGVO — Datengenauigkeit und -aktualitaet als Datenschutzgrundsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill härtet die Datenbasis, damit KYC und Screening nicht an schlechten Stammdaten scheitern.

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

## 3. `geldwaesche-immobilien-gueterhaendler`

**Fokus:** AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. Normen § 2 Abs. 1 Nr. 14 GwG Immobilienmakler § 2 Abs. 1 Nr. 16 GwG Gueterhaendler § 4 GwG interne Sicherungsmassnahmen. Prüfraster Verpflichtetenstatus Risikoanalyse Identifizierung Transaktionsschwellen Barzahlungsverbot. Output KYC-Prozessdesign mit Risikoeinstufung Identifizierungsprotokoll und Barzahlungsregel-Dokumentation. Abgrenzung zu geldwäsche-kyc-onboarding und geldwäsche-risikoanalyse-unternehmen.

# Immobilien, Güterhandel und Nichtfinanzsektor

## Triage zu Beginn
1. Welcher Verpflichteten-Typ: Immobilienmakler, Notarkanzlei bei Immobiliengeschaeft, Gueterthaendler (Kunst, Edelmetalle, Luxusgueter)?
2. Ueberschreitet der Barzahlungsbetrag den Schwellenwert (10.000 EUR brutto bei Gueterthaendlern, § 4 GwG)?
3. Liegen PEP- oder Hochrisikoindikatoren beim Kaeufer oder Verkaeufer vor?
4. Ist die Immobilientransaktion Teil einer komplexen Struktur mit mehreren Zwischengesellschaften?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 2 Abs. 1 Nr. 10-14 GwG — Verpflichtete aus Immobilien- und Guetersektor
- § 4 GwG — Barzahlungsschwellenwerte (10.000 EUR) fuer Gueterthaendler
- § 15 GwG — Verstaerkte Sorgfaltspflichten bei risikoreichen Kunden
- § 43 GwG — Meldepflicht bei Verdacht; gilt fuer alle Verpflichteten einschliesslich Makler

## Normfokus und Praxis (Immobilien und Güterhandel)
- Verpflichtetenkreis: § 2 Abs. 1 Nr. 14 GwG Immobilienmakler (auch Vermietungsvermittler ab Monatsmiete 10 000 EUR), Nr. 16 Güterhändler (insb. Edelmetalle, Edelsteine, hochwertige Kunst), Nr. 10 Notare bei Treuhand-/Anderkonten, Nr. 13 Steuerberater/StBuRA bei wirtschaftsberatender Tätigkeit.
- Bar­zahlungsschwellen: § 4 GwG iVm § 12 GwG — Identifizierungspflicht ab 10 000 EUR brutto, Kunstvermittler ab 10 000 EUR; ab 10.7.2027 nach AMLR (EU) 2024/1624 EU-weite 10 000-Euro-Bar-Cap (Art. 80) und bei Edelmetallhandel 1 000 EUR. Geplantes BargeldobergrenzenG (Deutschland) parallel beachten.
- Sanktionsgesetz Durchsetzungsgesetz II (SanktDG II, 19.12.2022): Bar-Erwerbsverbot für Immobilien ab 1.4.2023 mit Bar oder Kryptowerten (§ 16a GwG); Notar darf nicht beurkunden, wenn Bar­zahlung Teil ist.
- Aufsichtsbehörden: jeweilige Länderaufsicht (z. B. Regierungspräsidien, Bezirksregierungen) — nicht BaFin; gesonderte Mitteilungspflichten für Immobilien-/Notarsektor an Bundesanzeiger und Transparenzregister.
- Praktiker-Tipp: Risikoanalyse nach § 5 GwG zwingend dokumentiert; bei Immobilien­transaktionen Notar-AML-Check fragen (Vendor-KYC); bei kompliziertem UBO Briefkasten­firma Cayman/BVI mit Erwerb deutscher Immobilien immer EDD und Mittelherkunfts­beleg (Bank-Refstatement, Kaufvertragskette).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill übersetzt GwG-Pflichten in pragmatische Workflows für Nichtfinanzunternehmen.

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
