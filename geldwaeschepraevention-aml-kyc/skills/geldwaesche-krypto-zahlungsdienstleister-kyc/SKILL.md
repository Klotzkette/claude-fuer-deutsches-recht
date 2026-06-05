---
name: geldwaesche-krypto-zahlungsdienstleister-kyc
description: "Geldwaesche Krypto Zahlungsdienstleister KYC: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geldwaesche Krypto Zahlungsdienstleister KYC

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geldwaesche Krypto Zahlungsdienstleister KYC** im Plugin Geldwäscheprävention (AML/KYC). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geldwaesche-kommandocenter` | Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behoerdenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen starten. Normen GwG gesamt § 43 GwG Verdachtsmeldung § 10 GwG Sorgfaltspflichten. Prüfraster Verpflichtetencheck Risikoklasse KYC-Status Sanktionsscreening Verdachtsfall Eskalation. Output Triage-Ergebnis mit Routing zum passenden Skill Statusampel und naechsten Schritten. Abgrenzung zu geldwäsche-verpflichteten-check und geldwäsche-simulation-testlauf. |
| `geldwaesche-krypto-zahlungsdienstleister` | AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verordnung 2023/1113 Travel Rule MiCAR Art. 59. Prüfraster Wallets Travel Rule Mittelherkunft Krypto-Red-Flags Zahlungsdienstleister E-Geld technische Kontrollpunkte. Output KYC-Prüfprotokoll mit Wallet-Analyse Red-Flag-Liste Travel-Rule-Nachweis und Verdachtsprüfung. Abgrenzung zu geldwäsche-transaktionsmonitoring und geldwäsche-sanktionsscreening. |
| `geldwaesche-kyc-onboarding` | KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10 11 GwG allgemeine Sorgfaltspflichten § 15 GwG verstaerkte Sorgfaltspflicht § 14 GwG vereinfachte Sorgfaltspflicht. Prüfraster Identifizierung Zweck Geschäftsbeziehung Mittelherkunft Eigentumsstruktur Risikoeinstufung Freigabe. Output KYC-Akte mit Identifizierungsprotokoll Risikoeinstufung Freigabevermerk und periodischer Aktualisierungsplan. Abgrenzung zu geldwäsche-pep-hochrisikoland und geldwäsche-ubo-wirtschaftlich-berechtigte. |

## Arbeitsweg

Im Plugin Geldwäscheprävention (AML/KYC) gilt für **Geldwaesche Krypto Zahlungsdienstleister KYC**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geldwaesche-kommandocenter`

**Fokus:** Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behoerdenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen starten. Normen GwG gesamt § 43 GwG Verdachtsmeldung § 10 GwG Sorgfaltspflichten. Prüfraster Verpflichtetencheck Risikoklasse KYC-Status Sanktionsscreening Verdachtsfall Eskalation. Output Triage-Ergebnis mit Routing zum passenden Skill Statusampel und naechsten Schritten. Abgrenzung zu geldwäsche-verpflichteten-check und geldwäsche-simulation-testlauf.

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

Dieser Einstieg führt in jedes AML/KYC-Mandat: Risikoanalyse, Kundenprüfung, wirtschaftlich Berechtigte, Sanktionsscreening, Verdachtsmeldung, Behördenverfahren oder Remediation.

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

## 2. `geldwaesche-krypto-zahlungsdienstleister`

**Fokus:** AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verordnung 2023/1113 Travel Rule MiCAR Art. 59. Prüfraster Wallets Travel Rule Mittelherkunft Krypto-Red-Flags Zahlungsdienstleister E-Geld technische Kontrollpunkte. Output KYC-Prüfprotokoll mit Wallet-Analyse Red-Flag-Liste Travel-Rule-Nachweis und Verdachtsprüfung. Abgrenzung zu geldwäsche-transaktionsmonitoring und geldwäsche-sanktionsscreening.

# Krypto, Zahlungsdienste und FinTech

## Triage zu Beginn
1. Handelt es sich um einen Kryptowertedienstleister, E-Geld-Institut oder regulaeren Zahlungsdienstleister?
2. Welche Wallets oder Transaktionen sind betroffen; greift die Travel Rule (ueber 1.000 EUR)?
3. Gibt es Hinweise auf Mixer, Anonymisierungstools oder High-Risk-Wallets laut Blockchain-Analyse?
4. Ist der VASP (Virtual Asset Service Provider) in der EU registriert oder aus einem Drittland?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 2 Abs. 1 Nr. 2a GwG — Kryptowertedienstleister als Verpflichtete
- Art. 14-16 TFR (Transfer of Funds Regulation) — Travel Rule ab 1.000 EUR
- § 64y KWG — Registrierungs- und Zulassungspflicht fuer Krypto-Custodians
- § 15 GwG — Verstaerkte Sorgfalt bei hohem Geldwaescherisiko (Privacy Coins, Mixer)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bildet risikoreiche digitale Geschäftsmodelle in KYC- und Monitoring-Workflows ab.

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

## 3. `geldwaesche-kyc-onboarding`

**Fokus:** KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10 11 GwG allgemeine Sorgfaltspflichten § 15 GwG verstaerkte Sorgfaltspflicht § 14 GwG vereinfachte Sorgfaltspflicht. Prüfraster Identifizierung Zweck Geschäftsbeziehung Mittelherkunft Eigentumsstruktur Risikoeinstufung Freigabe. Output KYC-Akte mit Identifizierungsprotokoll Risikoeinstufung Freigabevermerk und periodischer Aktualisierungsplan. Abgrenzung zu geldwäsche-pep-hochrisikoland und geldwäsche-ubo-wirtschaftlich-berechtigte.

# KYC-Onboarding und Kundenprüfung

## Triage zu Beginn
1. Handelt es sich um eine natuerliche Person, juristische Person oder einen Trust/Stiftung?
2. Gibt es PEP-Indikatoren, Hochrisikobezug oder komplexe Eigentumsstrukturen (mehr als zwei Ebenen)?
3. Welche Unterlagen liegen bereits vor und welche fehlen fuer die vollstaendige Identifizierung nach § 10 GwG?
4. Welche Risikoklasse (niedrig/normal/erhoehte Sorgfalt/verstaerkte Sorgfalt) wird erwartet?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 10-17 GwG — Allgemeine und vereinfachte Sorgfaltspflichten
- § 13 GwG — Identifizierung des wirtschaftlich Berechtigten
- § 15 GwG — Verstaerkte Sorgfaltspflichten (PEP, Hochrisikoland)
- § 11 Abs. 6 GwG — Risikobasierte Aktualisierungspflicht der KYC-Daten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill macht aus unvollständigen Kundenunterlagen einen geführten, verzeihenden KYC-Prozess.

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
