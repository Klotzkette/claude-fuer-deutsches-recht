---
name: nkr-digital-anschlussfaehigkeit-digitalcheck
description: "Digital Anschlussfaehigkeit Digitalcheck: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Digital Anschlussfaehigkeit Digitalcheck

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Digital Anschlussfaehigkeit Digitalcheck** im Plugin Normenkontrollrat (NKR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nkr-digital-anschlussfaehigkeit-tauglich` | Pruefskill Digitaltauglichkeit. Adressiert die seit 2022 geltende Pflicht zum Digitalcheck (Bundesregelungsvorhaben muessen digital praktikabel sein) und die OZG-Anschlussfaehigkeit. Mit Standardpruefraster Anschluss an bestehende Standards (XOEV FIM ELSTER beA) Once-Only-Prinzip Schnittstellen Datenformate. Mustertexte zur Stellungnahme. |
| `nkr-digitalcheck-und-onlinezugangsgesetz-ozg` | Fachmodul OZG und Digitalcheck. Beschreibt das Onlinezugangsgesetz die OZG-Leistungen den Portalverbund das Once-Only-Prinzip und die ab dem 1. Januar 2023 anwendbare Digitalcheck-Methodik nach § 4 Abs. 3 i.V.m. § 9 NKRG fuer Bundesregelungsvorhaben. Mit Schnittstellen-Checkliste FIM XOEV ELSTER beA und Standardbausteinen fuer die Stellungnahme. |

## Arbeitsweg

Im Plugin Normenkontrollrat (NKR) gilt für **Digital Anschlussfaehigkeit Digitalcheck**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nkr-digital-anschlussfaehigkeit-tauglich`

**Fokus:** Pruefskill Digitaltauglichkeit. Adressiert die seit 2022 geltende Pflicht zum Digitalcheck (Bundesregelungsvorhaben muessen digital praktikabel sein) und die OZG-Anschlussfaehigkeit. Mit Standardpruefraster Anschluss an bestehende Standards (XOEV FIM ELSTER beA) Once-Only-Prinzip Schnittstellen Datenformate. Mustertexte zur Stellungnahme.

# NKR-Digitaltauglichkeit / Digital-Anschlussfaehigkeit

## Worum geht es konkret

Seit 2022 gilt der **Digitalcheck**: jedes Bundesregelungsvorhaben muss vor Kabinettsbefassung auf digitale Tauglichkeit geprueft werden. Der NKR begleitet diesen Check und kommentiert die Ergebnisse in der Stellungnahme.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorhaben sieht digitale Verfahren vor
- Vorhaben sieht analoge Verfahren vor (Pruefung, ob digital moeglich)
- Vorhaben enthaelt Datenpflichten
- Vorhaben adressiert OZG-Leistungen

Rueckfrage nur wenn unklar: *"Welche digitalen Beruehrungspunkte hat das Vorhaben — Antragsverfahren, Datenuebermittlung, Speicherung, Schnittstelle zu Bestandssystemen?"*

## Rechtlicher und methodischer Rahmen

- **Digitalcheck-Methodik** (BMI / NKR, seit 2022)
- **OZG** (Onlinezugangsgesetz, in der jeweils geltenden Fassung; OZG-Folgeregulierung Stand zu pruefen)
- **eIDAS-VO** (Verordnung (EU) 910/2014 in der jeweils geltenden Fassung)
- **§ 44 GGO** — Folgen-Pruefung umfasst auch Digitales
- **NKRG** § 4
- **Standards XOEV, FIM, ELSTER, beA**

## Fuenf Prinzipien des Digitalchecks (Standard)

1. **Digitale Kommunikation sicherstellen** — Kanal, Standards, Schnittstellen
2. **Wiederverwendung von Daten und Standards** (Once-Only)
3. **Datenschutz und Informationssicherheit by design**
4. **Klare Regelungen / einheitliche Begriffe** (maschinenlesbar)
5. **Automatisierung ermoeglichen** — Format, Strukturierung

## Pruefraster / Schritt fuer Schritt

### 1. Digitale Kommunikation

- Welche Kanaele? (Web, App, beA, De-Mail, eID-Wallet, OZG-Portalverbund)
- Sind sie bereits etabliert?
- Schnittstellen sicher und dokumentiert?
- Barrierefreiheit gewaehrleistet?

### 2. Datenstandards

- XOEV (XML in der Verwaltung) genutzt?
- FIM (Foederales Informationsmanagement) verwendet?
- Datenkataloge etabliert?

### 3. Once-Only-Prinzip

- Daten, die der Verwaltung schon vorliegen, werden wiederverwendet?
- Mehrfacherhebung vermieden?

### 4. Datenschutz / Sicherheit

- DSGVO-Konformitaet
- Rechtsgrundlage fuer Verarbeitung
- Speicherfrist
- Loeschpflichten

### 5. Maschinenlesbarkeit / Begriffsklarheit

- Klare Tatbestaende, eindeutig automatisierbar
- Vermeidung unbestimmter Rechtsbegriffe wo automatisiert geprueft werden soll

### 6. Anschluss an Bestandssysteme

- ELSTER
- beA / beBPO
- ZDR / Handelsregister
- e-Akte / e-Justice

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Kein Digitalcheck dokumentiert
- Vorhaben verwendet eigenen Standard statt etablierter
- Once-Only nicht umgesetzt
- Datenstandard fehlt (kein XOEV, kein FIM)
- Antragsverfahren weiterhin Papier
- Schnittstellen zum OZG-Portal nicht vorgesehen

## Trade-off-Matrix

| Aspekt | Plus | Minus |
|---|---|---|
| Standard verwendet (XOEV / FIM) | ja | nein, eigene Loesung |
| OZG-Portal angeschlossen | ja | nein |
| Once-Only | beachtet | Mehrfacherhebung |
| Barrierefreiheit | gewaehrleistet | nicht thematisiert |
| Maschinenlesbarkeit | eindeutig | offene Rechtsbegriffe |
| Schnittstellen | dokumentiert | unklar |

## Mustertexte / Stellungnahme-Bausteine

- "Der Digitalcheck wurde vom Ressort durchgefuehrt; die Ergebnisse sind dokumentiert. Der NKR haelt die digitale Anschlussfaehigkeit fuer gewaehrleistet."
- "Der NKR weist darauf hin, dass im Vorhaben kein Hinweis auf die Anwendung der Standards XOEV und FIM enthalten ist. Eine Klarstellung waere wuenschenswert."
- "Der NKR empfiehlt, das Verfahren an den OZG-Portalverbund anzuschliessen und das Once-Only-Prinzip im Sinne des [§ X OZG / EU-SDG-VO] umzusetzen."
- "Der NKR weist darauf hin, dass die vorgesehene Pflicht zur monatlichen [Lebensbescheid] in der bisherigen Ausgestaltung nicht maschinenlesbar abbildbar ist; eine Praezisierung des Datenformats ist erforderlich."

### Checkliste fuer den Digitalcheck (Pflichtbestandteile)

- [ ] Digitale Kommunikation moeglich
- [ ] OZG-Anschluss
- [ ] XOEV / FIM verwendet
- [ ] Once-Only umgesetzt
- [ ] Datenschutz / Sicherheit by design
- [ ] Barrierefreiheit
- [ ] Maschinenlesbarkeit
- [ ] Schnittstellen zu Bestandssystemen
- [ ] Pruefung Automatisierungsmoeglichkeit

## Typische Fehler in Ressort-Entwuerfen

- "Vorhaben ist digital tauglich" ohne Konkretisierung
- Eigener Standard ohne Verweis auf XOEV / FIM
- Mehrfacherhebung weiterhin vorgesehen
- OZG-Anschluss "in spaeterer Phase"
- Maschinenlesbarkeit nicht thematisiert

## Querverweise

- `nkr-digitalcheck-und-onlinezugangsgesetz-ozg` — Detail-Skill OZG
- `nkr-praktikabilitaet-vollzug-test`
- `nkr-handelsregister-und-elektronische-zustellung` — Beispielfall
- `nkr-stellungnahme-formulierungshilfe-vs-referentenentwurf`
- `legistik-werkstatt/folgenabschaetzung-erfuellungsaufwand`

## Quellen Stand 06/2026

- Digitalcheck-Methodik (BMI / NKR, seit 2022, jeweils aktuelle Fassung)
- OZG (Onlinezugangsgesetz) in der jeweils geltenden Fassung
- eIDAS-Verordnung (EU) 910/2014 in der jeweils geltenden Fassung
- § 44 GGO
- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- Standards XOEV, FIM, ELSTER, beA — Spezifikationen jeweils aktueller Stand
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.digitalcheck.bund.de](https://www.digitalcheck.bund.de) und [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)

## 2. `nkr-digitalcheck-und-onlinezugangsgesetz-ozg`

**Fokus:** Fachmodul OZG und Digitalcheck. Beschreibt das Onlinezugangsgesetz die OZG-Leistungen den Portalverbund das Once-Only-Prinzip und die ab dem 1. Januar 2023 anwendbare Digitalcheck-Methodik nach § 4 Abs. 3 i.V.m. § 9 NKRG fuer Bundesregelungsvorhaben. Mit Schnittstellen-Checkliste FIM XOEV ELSTER beA und Standardbausteinen fuer die Stellungnahme.

# NKR-Digitalcheck und Onlinezugangsgesetz (OZG)

## Worum geht es konkret

Das Onlinezugangsgesetz (OZG) verpflichtet Bund und Laender, Verwaltungsleistungen digital anzubieten. Der Digitalcheck (BMI / NKR; gesetzliche Grundlage § 4 Abs. 3 NKRG, ab dem **1. Januar 2023 anzuwenden** gemaess § 9 NKRG) prueft, ob Bundesregelungsvorhaben digital praktikabel sind. Beide Instrumente sind zentral fuer die NKR-Pruefung von Vorhaben mit digitalen Bezuegen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Vorhaben adressiert eine OZG-Leistung
- Vorhaben sieht Antraege / Mitteilungen vor
- Vorhaben sieht digitale Schnittstellen vor
- Vorhaben verwendet eigenen Standard statt etablierter Verwaltungsschnittstellen

Rueckfrage nur wenn unklar: *"Welche OZG-Leistung ist betroffen? Wer ist Leistungserbringer — Bund, Land, Kommune?"*

## Rechtlicher und methodischer Rahmen

- **Onlinezugangsgesetz (OZG)** in der jeweils geltenden Fassung (urspruenglich vom 14.08.2017; OZG 2.0 / Folgeregulierung Stand vom Anwender zu verifizieren)
- **Digitalcheck-Methodik** (BMI / NKR, jeweils aktuelle Fassung)
- **§ 4 Abs. 3 NKRG** — Digitalcheck als Pruefungsbestandteil (Pruefung der Moeglichkeiten digitaler Ausfuehrung)
- **§ 9 NKRG** — § 4 Abs. 3 NKRG ist **ab dem 1. Januar 2023 anzuwenden** (Uebergangsregelung)
- **eIDAS-Verordnung (EU) 910/2014** in der jeweils geltenden Fassung
- **EU Single Digital Gateway-VO (EU) 2018/1724** (Once-Only auf EU-Ebene)
- **§ 44 GGO**, **NKRG** § 4 (Pruefungsgegenstand)
- **Standards XOEV, FIM, ELSTER, beA**

## OZG-Grundbegriffe

- **OZG-Leistung**: digitalisierbare Verwaltungsleistung im OZG-Katalog
- **Portalverbund**: technische Vernetzung der Verwaltungsportale Bund und Laender
- **Nutzerkonto Bund / Mein Unternehmenskonto** als Authentifizierung
- **Servicekonto / EUDI-Wallet** als Identifizierungsmittel (in Entwicklung)
- **Once-Only**: Daten werden nur einmal erhoben, mehrfach genutzt

## Digitalcheck — fuenf Prinzipien

1. Digitale Kommunikation ermoeglichen
2. Wiederverwendung von Daten und Standards (Once-Only)
3. Datenschutz / Informationssicherheit by design
4. Klare, maschinenlesbare Regelungen
5. Automatisierung ermoeglichen

## Pruefraster / Schritt fuer Schritt

### 1. OZG-Bezug pruefen

- Ist die Leistung im OZG-Katalog?
- Welcher Reifegrad? (Information / Antrag / Bescheid / vollintegrierter Online-Prozess)
- Wer ist Leistungserbringer? (Bund / Land / Kommune)

### 2. Portalverbund-Anschluss

- Wird das Vorhaben ueber den Portalverbund abgewickelt?
- Wenn nein: Begruendung
- Schnittstellen dokumentiert?

### 3. Datenstandards

- Anwendung XOEV / FIM
- Datenformat dokumentiert
- Strukturierte Daten statt PDF

### 4. Once-Only

- Schon vorhandene Daten werden wiederverwendet?
- Beispiel: Daten aus Handelsregister, aus Steuerregister

### 5. Authentifizierung

- Nutzerkonto Bund / Mein Unternehmenskonto / EUDI-Wallet
- eIDAS-Konformitaet

### 6. Datenschutz und Sicherheit

- DSGVO-Konformitaet
- BSI-Schutzbedarfsanalyse
- Rechtsgrundlage und Loeschpflichten

### 7. Maschinenlesbarkeit

- Tatbestaende automatisierbar
- Vermeidung unbestimmter Rechtsbegriffe in automatisierbaren Bereichen

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Digitalcheck nicht durchgefuehrt
- OZG-Anschluss nicht vorgesehen
- Eigener Standard ohne XOEV / FIM
- Once-Only ignoriert (Mehrfacherhebung)
- Nutzerkonto / Authentifizierung unklar
- Maschinenlesbarkeit nicht thematisiert
- Papierbasiertes Verfahren bei moeglicher digitaler Alternative

## Trade-off-Matrix

| Aspekt | OZG-Plus | OZG-Minus |
|---|---|---|
| Anschluss Portalverbund | ja | nein |
| Standards XOEV/FIM | ja | eigener Standard |
| Once-Only | ja | Mehrfacherhebung |
| eID / Wallet | etabliert genutzt | unklare Authentifizierung |
| Datenformat | maschinenlesbar | PDF / Papier |
| Reifegrad OZG | hoch (vollintegriert) | niedrig (nur Information) |

## Mustertexte / Stellungnahme-Bausteine

- "Das Vorhaben adressiert eine OZG-Leistung im Sinne von [§ X OZG / Anlage]. Der NKR begruesst die Anwendung des Portalverbundes."
- "Der NKR weist darauf hin, dass das Vorhaben einen eigenen Datenstandard vorsieht und die etablierten Standards XOEV und FIM nicht anwendet. Der NKR empfiehlt eine Pruefung der Standardkompatibilitaet."
- "Das vorgesehene Verfahren erhebt Daten, die der Verwaltung bereits aus dem Handelsregister vorliegen. Der NKR empfiehlt eine Umsetzung des Once-Only-Prinzips im Sinne der EU-Single-Digital-Gateway-VO."
- "Der Digitalcheck wurde vom Ressort dokumentiert. Die fuenf Digitalcheck-Prinzipien sind nachvollziehbar adressiert."
- "Der NKR weist darauf hin, dass die vorgesehene monatliche Lebensbescheid-Pflicht in einem Spannungsverhaeltnis zum Once-Only-Prinzip steht; eine automatisierte Erreichbarkeitspruefung durch das Handelsregistergericht waere praktikabler."

## Typische Fehler in Ressort-Entwuerfen

- "Vorhaben ist digital tauglich" ohne Konkretisierung
- Antragsverfahren weiterhin Papier
- Eigener Datenstandard
- Mehrfacherhebung ohne Begruendung
- OZG-Anschluss "in spaeterer Phase"

## Querverweise

- `nkr-digital-anschlussfaehigkeit-tauglich`
- `nkr-handelsregister-und-elektronische-zustellung` — Praxisbeispiel
- `nkr-eu-richtlinien-umsetzung-und-goldplating`
- `nkr-praktikabilitaet-vollzug-test`
- `legistik-werkstatt/folgenabschaetzung-erfuellungsaufwand`

## Quellen Stand 06/2026

- Onlinezugangsgesetz (OZG) vom 14.08.2017 in der jeweils geltenden Fassung; OZG-Folgeregulierung Stand vom Anwender zu verifizieren
- Digitalcheck-Methodik (BMI / NKR, jeweils aktuelle Fassung)
- eIDAS-Verordnung (EU) 910/2014 in der jeweils geltenden Fassung
- EU Single Digital Gateway-VO (EU) 2018/1724
- § 44 GGO; NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4 Abs. 3 (Digitalcheck) i.V.m. § 9 (Anwendbarkeit ab 1. Januar 2023)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.digitalcheck.bund.de](https://www.digitalcheck.bund.de), [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)
