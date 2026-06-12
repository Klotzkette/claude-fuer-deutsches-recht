# Megaprompt: geldwaeschepraevention-aml-kyc

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 53 Skills des Plugins `geldwaeschepraevention-aml-kyc`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Geldwäscheprävention AML/KYC: ordnet Rolle (Verpflichteter (Bank, Anwalt, Notar), Kunde…
2. **geldwaeschepraevention-erstpruefung-und-mandatsziel** — Geldwaeschepraevention: Erstprüfung, Rollenklärung und Mandatsziel.
3. **geldwaesche-audit-internal-datenqualitaet** — Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer …
4. **geldwaesche-bussgeld-reputation** — Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Buß…
5. **geldwaesche-datenqualitaet-register** — Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehler…
6. **geldwaesche-gruppenweite-compliance** — Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern. Anwendungsfall Muttergesellsch…
7. **geldwaesche-immobilien-gueterhaendler** — AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendu…
8. **geldwaesche-krypto-zahlungsdienstleister** — AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll …
9. **geldwaesche-krypto-zahlungsdienstleister-kyc** — Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behördenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall…
10. **geldwaesche-kyc-onboarding** — KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäf…
11. **geldwaesche-pep-hochrisikoland-risikoanalyse** — Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwend…
12. **geldwaesche-risikoanalyse-unternehmen** — Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgesch…
13. **geldwaesche-sanktionsscreening** — Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Ge…
14. **geldwaesche-sicherungsmassnahmen-simulation** — Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder…
15. **geldwaesche-simulation-testlauf** — Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behördenfragen. Anwendungsfall Team w…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Geldwäscheprävention AML/KYC: ordnet Rolle (Verpflichteter (Bank, Anwalt, Notar), Kunde, FIU), markiert Frist (Verdachtsmeldung unverzüglich § 43 GwG), wählt Norm (GwG, FATF 40 Recommendations, EU-AMLD VI) und Zuständigkeit (FIU), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Geldwaeschepraevention Aml Kyc** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aml-kryptotransaktionen-mica-spezial` — AML Kryptotransaktionen Mica Spezial
- `aml-kyc-start-chronologie-fristen` — AML KYC Start Chronologie Fristen
- `aml-trade-based-money-laundering-spezial` — AML Trade Based Money Laundering Spezial
- `aml-verdachtsmeldung-fiu-leitfaden` — AML Verdachtsmeldung FIU Leitfaden
- `awareness-zahlen-schwellen-und-berechnung` — Awareness Zahlen Schwellen und Berechnung
- `behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` — Behoerdenverfahren Schriftsatz Brief und Memo Bausteine
- `geldwaesche-audit-internal-datenqualitaet` — Geldwaesche Audit Internal Datenqualitaet
- `geldwaesche-behoerdenverfahren` — Geldwaesche Behoerdenverfahren
- `geldwaesche-bussgeld-reputation` — Geldwaesche Bussgeld Reputation
- `geldwaesche-datenqualitaet-register` — Geldwaesche Datenqualitaet Register
- `geldwaesche-gruppenweite-compliance` — Geldwaesche Gruppenweite Compliance
- `geldwaesche-immobilien-gueterhaendler` — Geldwaesche Immobilien Gueterhaendler
- `geldwaesche-krypto-zahlungsdienstleister` — Geldwaesche Krypto Zahlungsdienstleister
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Geldwaeschepraevention Aml Kyc sind GwG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `geldwaeschepraevention-erstpruefung-und-mandatsziel`

_Geldwaeschepraevention: Erstprüfung, Rollenklärung und Mandatsziel._

# Geldwaeschepraevention: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Geldwaeschepraevention Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Geldwaeschepraevention Aml Kyc** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Geldwaeschepraevention: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** AML, KYC, GwG, UBO, PEP, FIU.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Geldwaeschepraevention** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `geldwaesche-audit-internal-datenqualitaet`

_Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer will AML-Kontrollsystem auf Wirksamkeit prüfen. Normen § 4 GwG interne Sicherungsmassnahmen § 6 GwG Risikomanagement FATF-Empfehlungen BaFin-Rundschreiben. Prüfraster AML-Kontro..._

# Audit und interne Revision

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welcher Audit-Bereich ist betroffen: KYC-Qualitaet, Transaktionsmonitoring, Verdachtsmeldungen oder Sanktionsscreening?
2. Handelt es sich um eine anlassbezogene Sonderrevision oder eine regulaere Revisionspruefung?
3. Welche Aufsichtsbehoerde und welche Berichtspflichten bestehen (BaFin, Staatsanwaltschaft, AMLA)?
4. Welcher Zeitraum und welche Stichprobenmenge sollen erfasst werden?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: Pflicht zur internen Revision
- § 7 GwG — Geldwäschebeauftragter und Berichtspflichten an Geschäftsleitung
- § 9 GwG — Gruppenweite Pflichten und Revisionsstandards
- § 56 GwG — Bußgeldtatbestaende bei Kontrollversagen

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-bussgeld-reputation`

_Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Bußgeldbescheid nach GwG ist eingegangen oder negative Berichterstattung droht. Normen § 52 GwG Bußgelder bis 5 Mio EUR oder 10 Prozent Jahresumsatz § 130 OWiG Aufsichtspflichtverl..._

# Bußgeld, Haftung und Reputation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Liegt ein BaFin-Bußgeldverfahren, eine Staatsanwaltschaftliche Ermittlung oder eine Presseanfrage vor?
2. Wer ist verantwortliche Person: Geldwäschebeauftragter, Geschaeftsfuehrer oder Verwaltungsrat?
3. Welche Remediation-Massnahmen wurden bereits eingeleitet?
4. Gibt es eine externe Kommunikations- oder PR-Strategie für den Reputationsschaden?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 56 GwG — Bußgeldtatbestaende (bis 5 Mio. EUR oder 10 % des Jahresumsatzes bei Kreditinstituten)
- § 57 GwG — Veroeffentlichung von Massnahmen (Naming and Shaming)
- § 30 OWiG — Verbandsgeldbusse
- § 130 OWiG — Aufsichtspflichtverletzung durch Geschaeftsleiter

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-datenqualitaet-register`

_Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister § 23a GwG Unstimmigkeitsmeldung. Prüfraster Datenfelder D..._

# Datenqualität, Register und Screening-Tools

## Arbeitsbereich

Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister § 23a GwG Unstimmigkeitsmeldung. Prüfraster Datenfelder Dubletten Schreibweisen Registerquellen Trefferqualitaet Auditierbarkeit. Output Datenqualitaetsbericht mit Bereinigungsliste Dubletten-Protokoll und Transparenzregister-Abgleich. Abgrenzung zu geldwäsche-ubo-wirtschaftlich-berechtigte und geldwäsche-transparenzregister. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Datenfelder oder Registerquellen weisen Qualitaetsprobleme auf?
2. Handelt es sich um Dubletten, fehlende Pflichtfelder, falsche Schreibweisen oder veraltete Eintraege?
3. Welches Screening-Tool ist betroffen und welche Trefferquoten sollen verbessert werden?
4. Gibt es einen Audit-Trail-Anforderung oder eine Behördenpruefung zu den Daten?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 10 GwG — Allgemeine Sorgfaltspflichten: Identifizierung und Ueberpruefung von Kundendaten
- §§ 18-26 GwG — Transparenzregister: Eintragungspflicht und Richtigkeit
- § 23a GwG — Unstimmigkeitsmeldung an Transparenzregister
- Art. 5 DSGVO — Datengenauigkeit und -aktualitaet als Datenschutzgrundsatz

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-gruppenweite-compliance`

_Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern. Anwendungsfall Muttergesellschaft will gruppenweite AML-Compliance sicherstellen und Tochtergesellschaften einbinden. Normen § 9 GwG Gruppenweite Pflichten § 25n KWG Auslagerung Art. 45 AMLD Gruppenweite Ver..._

# Gruppenweite Compliance und Outsourcing

## Arbeitsbereich

Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern. Anwendungsfall Muttergesellschaft will gruppenweite AML-Compliance sicherstellen und Tochtergesellschaften einbinden. Normen § 9 GwG Gruppenweite Pflichten § 25n KWG Auslagerung Art. 45 AMLD Gruppenweite Verfahren. Prüfraster Policies Auslagerung Dienstleister auslaendische Tochtergesellschaften Datenfluesse Kontrollberichte. Output Gruppenweite Compliance-Matrix mit Policies Kontrollstruktur Eskalationswegen und Berichterstattungslinien. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp und geldwäsche-audit-internal-revision. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Tochtergesellschaften oder Dienstleister sind im Scope der gruppenweiten Pruefung?
2. Gibt es laenderspezifische Anforderungen (FATF-Hochrisikolaender, EU-Mitglieder mit abweichenden Regeln)?
3. Welche Auslagerungsvertraege bestehen und wie werden die AML-Pflichten dort kontrolliert?
4. Gibt es einen gruppenweiten Policy-Rahmen oder Einzelregelungen pro Einheit?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 9 GwG — Gruppenweite Pflichten und Kontrollen
- § 6 Abs. 2 GwG — Pflicht zur Bestellung eines Geldwaeschebeauftragten auf Gruppenebene
- § 25l KWG — Gruppenweite Sorgfaltspflichten für Kreditinstitute
- Art. 45 AMLD4 — Gruppenweite Policies und Verfahren (EU-Recht)

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-immobilien-gueterhaendler`

_AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. Normen § 2 Abs. 1 Nr. 14 GwG Immobilienmakler § 2 Abs. 1 Nr. 1..._

# Immobilien, Güterhandel und Nichtfinanzsektor

## Arbeitsbereich

AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. Normen § 2 Abs. 1 Nr. 14 GwG Immobilienmakler § 2 Abs. 1 Nr. 16 GwG Gueterhaendler § 4 GwG interne Sicherungsmassnahmen. Prüfraster Verpflichtetenstatus Risikoanalyse Identifizierung Transaktionsschwellen Barzahlungsverbot. Output KYC-Prozessdesign mit Risikoeinstufung Identifizierungsprotokoll und Barzahlungsregel-Dokumentation. Abgrenzung zu geldwäsche-kyc-onboarding und geldwäsche-risikoanalyse-unternehmen. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welcher Verpflichteten-Typ: Immobilienmakler, Notarkanzlei bei Immobiliengeschaeft, Gueterthaendler (Kunst, Edelmetalle, Luxusgueter)?
2. Ueberschreitet der Barzahlungsbetrag den Schwellenwert (10.000 EUR brutto bei Gueterthaendlern, § 4 GwG)?
3. Liegen PEP- oder Hochrisikoindikatoren beim Kaeufer oder Verkaeufer vor?
4. Ist die Immobilientransaktion Teil einer komplexen Struktur mit mehreren Zwischengesellschaften?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 2 Abs. 1 Nr. 10-14 GwG — Verpflichtete aus Immobilien- und Guetersektor
- § 4 GwG — Barzahlungsschwellenwerte (10.000 EUR) für Gueterthaendler
- § 15 GwG — Verstaerkte Sorgfaltspflichten bei risikoreichen Kunden
- § 43 GwG — Meldepflicht bei Verdacht; gilt für alle Verpflichteten einschliesslich Makler

## Normfokus und Praxis (Immobilien und Güterhandel)
- Verpflichtetenkreis: § 2 Abs. 1 Nr. 14 GwG Immobilienmakler (auch Vermietungsvermittler ab Monatsmiete 10 000 EUR), Nr. 16 Güterhändler (insb. Edelmetalle, Edelsteine, hochwertige Kunst), Nr. 10 Notare bei Treuhand-/Anderkonten, Nr. 13 Steuerberater/StBuRA bei wirtschaftsberatender Tätigkeit.
- Bar­zahlungsschwellen: § 4 GwG iVm § 12 GwG — Identifizierungspflicht ab 10 000 EUR brutto, Kunstvermittler ab 10 000 EUR; ab 10.7.2027 nach AMLR (EU) 2024/1624 EU-weite 10 000-Euro-Bar-Cap (Art. 80) und bei Edelmetallhandel 1 000 EUR. Geplantes BargeldobergrenzenG (Deutschland) parallel beachten.
- Sanktionsgesetz Durchsetzungsgesetz II (SanktDG II, 19.12.2022): Bar-Erwerbsverbot für Immobilien ab 1.4.2023 mit Bar oder Kryptowerten (§ 16a GwG); Notar darf nicht beurkunden, wenn Bar­zahlung Teil ist.
- Aufsichtsbehörden: jeweilige Länderaufsicht (z. B. Regierungspräsidien, Bezirksregierungen) — nicht BaFin; gesonderte Mitteilungspflichten für Immobilien-/Notarsektor an Bundesanzeiger und Transparenzregister.
- Praktiker-Tipp: Risikoanalyse nach § 5 GwG zwingend dokumentiert; bei Immobilien­transaktionen Notar-AML-Check fragen (Vendor-KYC); bei kompliziertem UBO Briefkasten­firma Cayman/BVI mit Erwerb deutscher Immobilien immer EDD und Mittelherkunfts­beleg (Bank-Refstatement, Kaufvertragskette).

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-krypto-zahlungsdienstleister`

_AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verordnung 2023/1113 Travel Rule MiCAR Art. 59. Prüfraster Wallets..._

# Krypto, Zahlungsdienste und FinTech

## Arbeitsbereich

AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verordnung 2023/1113 Travel Rule MiCAR Art. 59. Prüfraster Wallets Travel Rule Mittelherkunft Krypto-Red-Flags Zahlungsdienstleister E-Geld technische Kontrollpunkte. Output KYC-Prüfprotokoll mit Wallet-Analyse Red-Flag-Liste Travel-Rule-Nachweis und Verdachtsprüfung. Abgrenzung zu geldwäsche-transaktionsmonitoring und geldwäsche-sanktionsscreening. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Handelt es sich um einen Kryptowertedienstleister, E-Geld-Institut oder regulaeren Zahlungsdienstleister?
2. Welche Wallets oder Transaktionen sind betroffen; greift die Travel Rule (ueber 1.000 EUR)?
3. Gibt es Hinweise auf Mixer, Anonymisierungstools oder High-Risk-Wallets laut Blockchain-Analyse?
4. Ist der VASP (Virtual Asset Service Provider) in der EU registriert oder aus einem Drittland?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 2 Abs. 1 Nr. 2a GwG — Kryptowertedienstleister als Verpflichtete
- Art. 14-16 TFR (Transfer of Funds Regulation) — Travel Rule ab 1.000 EUR
- § 64y KWG — Registrierungs- und Zulassungspflicht für Krypto-Custodians
- § 15 GwG — Verstaerkte Sorgfalt bei hohem Geldwaescherisiko (Privacy Coins, Mixer)

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-krypto-zahlungsdienstleister-kyc`

_Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behördenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen starten. Normen GwG gesamt § 43 GwG Verdachtsmeldung § 10 GwG Sorgfaltspflichten. Prüfrast..._

# AML/KYC-Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Handelt es sich um einen Neu-Fall (Intake), einen laufenden Fall (Update) oder einen Eskalationsfall?
2. Welcher Skill soll zuerst geladen werden: KYC-Onboarding, Verdachtsmeldung, Behördenverfahren oder Risikoanalyse?
3. Welche Fristen sind unmittelbar relevant (Meldepflicht § 43 GwG: unverzueglich)?
4. Sind echte oder simulierte Daten zu verarbeiten?

## Aktuelle Rechtsprechung und Behördenpraxis

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
- § 8 GwG — Aufzeichnungspflichten für alle Fallvorgaenge

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-kyc-onboarding`

_KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10 11 GwG allgemeine Sorgfaltspflichten § 15 GwG verstaerkte Sorgfaltspflicht § 1..._

# KYC-Onboarding und Kundenprüfung

## Arbeitsbereich

KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10 11 GwG allgemeine Sorgfaltspflichten § 15 GwG verstaerkte Sorgfaltspflicht § 14 GwG vereinfachte Sorgfaltspflicht. Prüfraster Identifizierung Zweck Geschäftsbeziehung Mittelherkunft Eigentumsstruktur Risikoeinstufung Freigabe. Output KYC-Akte mit Identifizierungsprotokoll Risikoeinstufung Freigabevermerk und periodischer Aktualisierungsplan. Abgrenzung zu geldwäsche-pep-hochrisikoland und geldwäsche-ubo-wirtschaftlich-berechtigte. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Handelt es sich um eine natuerliche Person, juristische Person oder einen Trust/Stiftung?
2. Gibt es PEP-Indikatoren, Hochrisikobezug oder komplexe Eigentumsstrukturen (mehr als zwei Ebenen)?
3. Welche Unterlagen liegen bereits vor und welche fehlen für die vollstaendige Identifizierung nach § 10 GwG?
4. Welche Risikoklasse (niedrig/normal/erhoehte Sorgfalt/verstaerkte Sorgfalt) wird erwartet?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 10-17 GwG — Allgemeine und vereinfachte Sorgfaltspflichten
- § 13 GwG — Identifizierung des wirtschaftlich Berechtigten
- § 15 GwG — Verstaerkte Sorgfaltspflichten (PEP, Hochrisikoland)
- § 11 Abs. 6 GwG — Risikobasierte Aktualisierungspflicht der KYC-Daten

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-pep-hochrisikoland-risikoanalyse`

_Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen. Normen § 15 GwG verstaerkte Sorgfaltspflichten § 1 Abs. 12 GwG PEP-Definition FA..._

# PEP, Hochrisikoland und verstärkte Sorgfalt

## Arbeitsbereich

Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen. Normen § 15 GwG verstaerkte Sorgfaltspflichten § 1 Abs. 12 GwG PEP-Definition FATF Hochrisikoliste EU-Delegierte VO. Prüfraster PEP Familienangehoerige nahestehende Personen Hochrisikolaender Nominees Treuhandstrukturen Enhanced Due Diligence. Output Verstaerkte KYC-Akte mit PEP-Begründung EDD-Dokumentation Freigabe auf Leitungsebene. Abgrenzung zu geldwäsche-kyc-onboarding und geldwäsche-sanktionsscreening. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Ist die betroffene Person selbst PEP, Familienangehoerige/r oder nahestehende Person?
2. Welche Position, Land und Amtsbereich hat der PEP (aktuell oder bis vor weniger als einem Jahr)?
3. Ist ein Hochrisikoland nach FATF-Liste oder EU-Delegierter Verordnung betroffen?
4. Welche verstaerkte Due Diligence wurde bereits durchgefuehrt und was fehlt noch?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 15 GwG — Verstaerkte Sorgfaltspflichten: PEP, nahestehende Personen, Hochrisikotransaktionen
- § 1 Abs. 12 GwG — Definition PEP
- §§ 14-16 GwG — Vereinfachte und normale Sorgfalt: Abgrenzung
- EU-Delegierte VO (EU) 2022/229 — Hochrisikodritt-Länderliste

## Normfokus und Praxis (PEP/EDD)
- PEP-Definition § 1 Abs. 12 GwG: politische Funktionen (Staatsoberhaupt, Minister, Parlamentarier, Verfassungsrichter, Botschafter, Generäle, Vorstandsmitglieder staatlicher Unternehmen) plus Familienangehörige (§ 1 Abs. 13 GwG) und nahestehende Personen (§ 1 Abs. 14 GwG). 12-Monats-Nachlauf nach Ende der Funktion (§ 15 Abs. 5 GwG).
- Pflichten EDD (§ 15 Abs. 4 GwG): Zustimmung Vorgesetzter, Klärung Vermögensherkunft und Geldherkunft, verstärkte laufende Überwachung; bei PEP-Kunden zwingend Senior Management Approval (i. d. R. C-Level oder MLRO).
- Hochrisikoland: konsolidierte Liste EU (Delegierte VO (EU) 2024/1657 ersetzt frühere Listen — stets aktuelle EUR-Lex-Quelle prüfen) und FATF-Black/Grey-List (Hochrisiko-/Beobachtungs­länder). Verstärkte Sorgfalt zwingend bei Geschäftsbeziehung/Transaktion mit Bezug zu diesen Ländern (§ 15 Abs. 3 Nr. 2 GwG).
- Konzern-Roll-out: Gruppenweite Compliance nach § 9 GwG — einheitliche PEP-Datenbank, Drittanbieter (Refinitiv World-Check, Dow Jones, LexisNexis) mit dokumentierter Datenqualität.
- Praktiker-Tipp: PEP-Treffer nicht automatisch ablehnen — sondern Fact-Check (richtige Person? Alias?), Senior Approval mit Memo "Warum trotz PEP-Status Geschäftsbeziehung tragbar", regelmäßiges Refresh (mind. einmal pro Jahr, bei kritischem Profil halbjährlich). Mittelherkunft mit Belegen (Steuerbescheid, Verkaufsurkunde, Erbschein) — nicht nur Selbstauskunft.

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-risikoanalyse-unternehmen`

_Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne Sicherungsmassnahmen FATF-Empfehlungen BaFin-AuA. Prüfraster Produkte Kundenstru..._

# Unternehmensweite Risikoanalyse

## Arbeitsbereich

Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne Sicherungsmassnahmen FATF-Empfehlungen BaFin-AuA. Prüfraster Produkte Kundenstruktur Länder Vertriebskanaele Transaktionen bestehende Kontrollen Risikoniveau. Output Risikoanalysedokument mit Risikoklassifizierung Kontrolllueckenbewertung und Massnahmenplan für Behördenvorlage. Abgrenzung zu geldwäsche-sicherungsmassnahmen-icp und geldwäsche-audit-internal-revision. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Branche und welche Verpflichteten-Kategorie trifft die Risikoanalyse?
2. Welche Risikofelder sollen abgedeckt werden: Kunden, Produkte, Vertriebskanaele, Länder, Transaktionen?
3. Liegt bereits eine Risikoanalyse vor, die aktualisiert werden soll, oder wird sie erstmalig erstellt?
4. Gibt es eine spezifische BaFin-/Aufsichtsvorgabe oder FATF-Leitlinie für diesen Sektor?

## Aktuelle Rechtsprechung und Behördenpraxis

Stand 05/2026:

- BaFin-AuA GwG (Allgemeiner Teil, AuA AT) — Veröffentlichung 29.11.2024; Ergänzung 06.03.2025 (Kryptowertetransfers, selbst gehostete Adressen) — anwendbar seit Februar 2025 — [bafin.de](https://www.bafin.de/SharedDocs/Downloads/DE/Auslegungsentscheidung/dl-ae-auas-2025-gw.html).
- EuGH, Urt. v. 13.02.2025 — C-383/23 (ILVA) — Unternehmensbegriff im wettbewerbsrechtlichen Sinne für DSGVO-Bußgeldobergrenze; methodisch übertragbar auf Bußgelder anderer EU-Sekundärrechtsakte mit ähnlicher Bußgeldsystematik.
- AMLA seit 01.07.2025 operativ; AMLR (EU) 2024/1624 ab 10.07.2027 anwendbar; Risikoanalyse-Anforderungen sind weiter strukturiert (Art. 7 ff. AMLR) — strategisch Migrationsplan anlegen.

Rechtsprechung im Mandat live verifizieren — keine Aktenzeichen aus Modellwissen.

## Zentrale Normen
- § 5 GwG — Unternehmenseigene Risikoanalyse: Pflichtinhalt und Aktualisierung
- § 4 Abs. 1 GwG — Interne Sicherungsmaßnahmen als Folge der Risikoanalyse
- FATF Guidance — Risk-Based Approach für Finanzinstitutionen (2021)
- BaFin-Auslegungs- und Anwendungshinweise (AuA) GwG — Risikoanalysevorgaben

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-sanktionsscreening`

_Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Geschäft soll abgeschlossen oder Transaktion freigegeben werden. Normen EU-Verordnungen 2580/2001 881/2002 Russland-VO 833/2014 269/2014 OFAC-SDN-Liste. Prüfraster Namensscreening..._

# Sanktionslistenprüfung und Embargoabgleich

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Sanktionslisten sollen geprueft werden: EU, OFAC, UN, nationale Listen?
2. Liegt ein True-Hit oder ein False-Positive vor — und welche Dokumentation gibt es bereits?
3. Sind Eigentuems- oder Kontrollbeziehungen zum Sanctioned Entity zu pruefen?
4. Gibt es eine Transaktionssperr-Pflicht oder eine Verdachtsmeldepflicht ausloesende Treffer?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 2 EU-VO 2580/2001 — Einfrierungspflicht: sofortige Sperrung bei Sanktionstreffer
- § 25h KWG — Geldwaesche- und Betrugsverhinderung in Kreditinstituten: Screeningpflicht
- Art. 4 EU-VO 269/2014 (Russlandsanktionen) — aktuelle Sanktionsregeln
- § 18 AWG — Strafbarkeit bei Verstoss gegen Ausfuhrverbote und Embargos

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-sicherungsmassnahmen-simulation`

_Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne Massnahmen § 7 GwG Gruppen-Compliance BaFin-Auslegungs- und Anwendungshinweise..._

# Interne Sicherungsmaßnahmen und ICP

## Arbeitsbereich

Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne Massnahmen § 7 GwG Gruppen-Compliance BaFin-Auslegungs- und Anwendungshinweise. Prüfraster Richtlinien Prozesse Kontrollen Eskalationen Schulungen Audit-Trail Vier-Augen-Prinzip. Output ICP-Handbuch mit Richtlinien Kontrollmatrix Eskalationswegen und Schulungsplan. Abgrenzung zu geldwäsche-risikoanalyse-unternehmen und geldwäsche-audit-internal-revision. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Sicherungsmaßnahme soll aufgebaut oder geprueft werden: Richtlinie, Kontrolle, Eskalationspfad oder Audit-Trail?
2. Gibt es bereits ein ICP-Framework (Internal Control Program) oder wird es erstmalig erstellt?
3. Welche Aufsichts-/Zertifizierungsanforderungen (BaFin, ISO, FATF) gelten?
4. Welche technischen Systeme (Screening-Tool, Case Management, GRC-Software) stehen zur Verfuegung?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: vollstaendige Pflichtkataloge
- § 6 GwG — Pflichten der Geschaeftsleitung zur Einrichtung wirksamer Kontrollen
- BaFin MaRisk AT 8.2 — Anforderungen an interne Kontrollsysteme (analoger Standard für AML)
- FATF Recommendation 18 — Internal Controls, Compliance and Audit

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Skill: `geldwaesche-simulation-testlauf`

_Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behördenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke Sanktionshit Verdachtsprüfung Schulung und Behördenfrage ab. Output Simulationsprotokol..._

# AML/KYC-Simulationsmodus

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Simulationsszenarien sollen durchgespielt werden: Onboarding, Alert, Sanktionshit, Verdachtsmeldung oder Behördenanfrage?
2. Soll mit simulierten oder geschwärzten echten Daten gearbeitet werden?
3. Welche Rollen sind beteiligt: Frontoffice, Compliance, Revision oder Geschaeftsfuehrung?
4. Gibt es einen konkreten Schulungszweck oder einen Aufsichts-Testlauf?

## Aktuelle Rechtsprechung und Behördenpraxis
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 GwG — Interne Sicherungsmaßnahmen: regelmässige Wirksamkeitspruefung eingeschlossen
- § 6 Abs. 2 Nr. 1 GwG — Geldwaeschebeauftragter hat Testverantwortung
- BaFin AuA GwG Abschn. 4 — Pruefung der Wirksamkeit interner Maßnahmen
- FATF Recommendation 18 — Testing of Internal Controls

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

