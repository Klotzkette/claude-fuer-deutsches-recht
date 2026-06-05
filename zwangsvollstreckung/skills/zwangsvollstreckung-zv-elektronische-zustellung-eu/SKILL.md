---
name: zwangsvollstreckung-zv-elektronische-zustellung-eu
description: "ZV Elektronische Zustellung EU: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZV Elektronische Zustellung EU

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZV Elektronische Zustellung EU** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zv-elektronische-zustellung-2027` | Gläubiger oder Kreditinstitut fragt: Was aendert sich durch die Digitalisierung der Zwangsvollstreckung ab 2026/2027? ZVollstrDigitG BT-Drs. 21/4815. Prüfraster: XML-Antrag § 829 Abs. 5 ZPO n.F. ab 1.10.2026 Pflicht sicherer Übermittlungsweg Kreditinstitute § 173 Abs. 2 Nr. 1 ZPO n.F. ab 1.10.2027 eBO ZVFV-Formulare neu § 840 ZPO. Output: Umstellungs-Checkliste und aktualisierte Workflow-Anpassung. Abgrenzung zu zv-pfueb-bank (PfUeB gegen Konto) und zv-titel-klausel-zustellung (Klassisch). |
| `zv-eu-kontenpfaendung-655-2014` | Gläubiger hat Schuldner der im EU-Ausland ein Bankkonto haelt und moechte dieses vorlaeufig sichern. EuKtPVO VO (EU) 655/2014 §§ 946 ff. ZPO. Prüfraster: Antrag deutsches Gericht Glaubhaftmachung Anspruch Sicherungsbedürfnis Sicherheitsleistung Drittstaaten-Wirkung alle EU-Mitgliedstaaten außer Daenemark anschließender PfUeB national § 829 ZPO. Output: Antrag Europaeische Kontenpfaendung und Folgepfaendung. Abgrenzung zu zv-pfueb-bank (inlaendisches Konto) und zv-kommandocenter. |
| `zv-kommandocenter` | Gläubiger oder Anwalt hat vollstreckbaren Titel und fragt: Welche Vollstreckungsart ist im konkreten Fall am sinnvollsten und wie wird sie eingeleitet? Startpunkt Zwangsvollstreckung. Prüfraster: Titelart und Vollstreckungsziel Routing zu passenden Skills Drei-Saeulen-Prüfung Titel Klausel Zustellung. Output: Vollstreckungs-Routing-Entscheidung mit passendem Folge-Skill. Abgrenzung zu zv-titel-klausel-zustellung (Formalprüfung) und allen anderen ZV-Skills. |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZV Elektronische Zustellung EU**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zv-elektronische-zustellung-2027`

**Fokus:** Gläubiger oder Kreditinstitut fragt: Was aendert sich durch die Digitalisierung der Zwangsvollstreckung ab 2026/2027? ZVollstrDigitG BT-Drs. 21/4815. Prüfraster: XML-Antrag § 829 Abs. 5 ZPO n.F. ab 1.10.2026 Pflicht sicherer Übermittlungsweg Kreditinstitute § 173 Abs. 2 Nr. 1 ZPO n.F. ab 1.10.2027 eBO ZVFV-Formulare neu § 840 ZPO. Output: Umstellungs-Checkliste und aktualisierte Workflow-Anpassung. Abgrenzung zu zv-pfueb-bank (PfUeB gegen Konto) und zv-titel-klausel-zustellung (Klassisch).

# Elektronische Zustellung in der Zwangsvollstreckung – ZVollstrDigitG


## Triage zu Beginn

1. Ist das ZVollstrDigitG bereits im BGBl verkündet und in Kraft getreten (Stand: aktuelles Datum prüfen)?
2. Soll die Zustellung vor oder nach dem 1.10.2027 erfolgen (Bank-Pflicht eBO)?
3. Hat die Kanzlei-Software die XML-Unterstützung (§ 829 Abs. 5 ZPO n.F.) bereits implementiert?
4. Ist die Zielbank bereits im eBO-Verzeichnis registriert?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 130a ZPO — elektronischer Rechtsverkehr (Schriftsätze)
- § 130d ZPO — aktive Nutzungspflicht für Rechtsanwälte (beA, eBO)
- § 173 ZPO n.F. (ZVollstrDigitG) — elektronische Zustellung an Drittschuldner
- § 829 Abs. 5 ZPO n.F. — XML-Antrag Pfändungs- und Überweisungsbeschluss
- § 840 ZPO — Drittschuldnererklärung
- § 750 ZPO — Voraussetzungen der Vollstreckung (Zustellnachweis)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Praktische Begleitung der größten ZPO-Reform der letzten Jahre für die Zwangsvollstreckung. Skill stellt sicher, dass Anträge ab Inkrafttreten formgerecht eingereicht und an die richtigen Empfänger über den richtigen Weg zugestellt werden.

## Reform-Eckdaten (Stand 25.5.2026)

| Datum | Inhalt |
| --- | --- |
| 19.3.2026 | Bundestag beschließt das Gesetz (BT-Drs. 21/4815) |
| April 2026 | Bundesrat – nicht zustimmungspflichtig |
| Verkündung im BGBl | bei Skill-Erstellung noch offen – Skill prüft aktuelles Datum |
| 1.10.2026 | Inkrafttreten Hauptteile: neue ZVFV-Formulare, XML-Antrag § 829 Abs. 5 ZPO n.F. |
| 1.10.2027 | Kreditinstitute MÜSSEN sicheren elektronischen Übermittlungsweg eröffnen (§ 173 Abs. 2 Nr. 1 ZPO n.F.) |

Bei jeder neuen Beratung **erst prüfen**, ob die Verkündung erfolgt ist und ob das Inkrafttreten verschoben wurde. Quellen:

- BT-Drs. 21/4815 (PDF auf dserver.bundestag.de)
- Bundestag Textarchiv 12/2026
- BRAK-Newsletter Ausgabe 8/2026 vom 1.5.2026 ("Zwangsvollstreckung künftig mit weniger Medienbrüchen")
- DGVB-Beitrag zum elektronischen Rechtsverkehr in der Vollstreckung

## Rechtsgrundlagen

- § 130a ZPO – elektronischer Rechtsverkehr Schriftsätze
- § 130d ZPO – aktive Nutzungspflicht Rechtsanwalt/Behörde
- § 173 ZPO n.F. (ZVollstrDigitG) – elektronische Zustellung an Drittschuldner
- § 829 Abs. 5 ZPO n.F. – XML-Antrag PfÜB
- § 840 ZPO – Drittschuldnererklärung (zusätzlich Postzustellung möglich)
- § 802a Abs. 2 ZPO – Gerichtsvollzieher-Aufträge
- ERV-Verordnungen ERVV und ERVB

## Die drei Stoßrichtungen der Reform

### 1. XML-Antrag § 829 Abs. 5 ZPO n.F.

Ab 1.10.2026 kann der PfÜB-Antrag zusätzlich zum PDF-Antrag eine maschinenlesbare XML-Struktur enthalten. Bei Diskrepanz **gilt das XML** – also XML führt PDF (BT-Drs. 21/4815). Wer Software einsetzt: schon vor 1.10.2026 testen, ob die Kanzlei-Software den ZVFV-konformen XML-Anhang erzeugt.

### 2. Pflicht der Kreditinstitute zum sicheren Übermittlungsweg

Ab 1.10.2027 sind Kreditinstitute verpflichtet, einen sicheren elektronischen Übermittlungsweg im Sinne des § 130a Abs. 4 ZPO zu eröffnen (§ 173 Abs. 2 Nr. 1 ZPO n.F.). In Frage kommen:

- **eBO** (elektronisches Bürger- und Organisationenpostfach) – die Bank registriert sich beim Bundesnotarvereinszentral / SAFE-Verzeichnis.
- **De-Mail** mit Absenderbestätigung
- weitere Übermittlungswege nach § 130a Abs. 4 ZPO und ERVV

Folge: Der Gerichtsvollzieher stellt PfÜB an Banken nicht mehr per Papier zu, sondern elektronisch. Das ist schneller, planbarer und vermeidet den klassischen Streit um Zustellungszeitpunkt. Bis 1.10.2027 dürfen Banken freiwillig elektronisch annehmen – viele Kreditinstitute tun das bereits.

### 3. § 840 ZPO Drittschuldnererklärung – Postzustellung erlaubt

Die Drittschuldnererklärung darf zusätzlich zur elektronischen Form auch per Post übermittelt werden. Erleichterung vor allem für Banken, die parallel den eBO-Empfang aufbauen müssen.

## für die Praxis bis 1.10.2027

1. **Soft Start ab 1.10.2026**: Wer XML-Antrag schreibt, sollte die ZVFV-Schemata kennen. Pilotphase nutzen.
2. **Bestandsaufnahme Kanzlei-Software**: kann sie eBO senden? Erzeugt sie ZVFV-XML? Mit dem Software-Anbieter klären.
3. **Bestandsaufnahme Banken**: viele Großbanken haben eBO bereits eröffnet. Liste der Drittschuldner mit eBO-Adressen pflegen.
4. **Schulung der GV** in Berücksichtigung – die örtlich zuständigen Gerichtsvollzieher werden ab 1.10.2027 elektronisch zustellen.
5. **Doppelte Wege vermeiden**: nicht parallel Papier UND eBO – Zustellungszeitpunkt ist sonst streitbefangen.

## Was bleibt analog

- Pfändung gegen Privatpersonen ohne eBO (Schuldnerzustellung) bleibt grundsätzlich Papier (außer Schuldner hat eBO).
- Gerichtsvollzieher-Mobiliarvollstreckung bleibt Vor-Ort-Termin.
- Zwangsversteigerung ZVG verfahrenstechnisch unverändert.

## Häufige Fehlerquellen

- Antrag in Papier eingereicht, obwohl § 130d ZPO aktive Nutzungspflicht der Anwaltschaft greift – Form fehlt, Antrag unzulässig.
- XML und PDF widersprechen sich – Skill warnt: XML führt. Datenpflege im DMS einrichten.
- Zustellung per beA statt eBO an Drittschuldner – Bank hat ggf. nur eBO eröffnet.
- Übergangsphase: nicht jede Bank ist vor 1.10.2027 elektronisch erreichbar – im Zweifel beim GV-Bezirk anfragen.

## Ausgabeformat

```
ZVOLLSTRDIGITG-CHECK [Mandat / Pfändung]

Inkrafttreten-Stand: verkündet [JA / NEIN, Stand-Recherche DD.MM.JJJJ]
Anwendbar ab: 1.10.2026 (XML), 1.10.2027 (Bank-Pflicht eBO)
Aktueller Schritt: [PfÜB-Antrag / Zustellung an Bank / § 840-Erklärung]
Empfehlung Form: [Papier / beA + ERVV PDF / XML + PDF / eBO]
Drittschuldner: Bank [Name], eBO bekannt [JA/NEIN]
Risiko: [Formfehler / Doppelzustellung / Übergangsfrist]

NÄCHSTER SCHRITT: [konkret]
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Datum der Verkündung im BGBl bei jeder Beratung neu verifizieren.
- Niemals parallel Papier und elektronisch – Zustellungszeitpunkt eindeutig halten.
- XML-Schema-Versionen prüfen – ZVFV-Update nicht verpassen.
- Niemals annehmen, jede Bank sei vor 1.10.2027 elektronisch erreichbar – im Übergang konkret beim GV nachfragen.
- Bei Anwaltsmandat § 130d ZPO als aktive Nutzungspflicht stets beachten.

## Querverweise

- `zv-kommandocenter` – Reform-Eckdaten kurz
- `zv-pfueb-bank` – Hauptanwendungsfall
- `zv-pfueb-arbeitsentgelt`, `zv-pfueb-mieter-finanzamt`
- `zv-titel-klausel-zustellung`
- Plugin `prozessrecht` (anderes Plugin) – allgemeiner Elektronischer Rechtsverkehr (§§ 130a, 130d ZPO; beA, eBO, EGVP)

## 2. `zv-eu-kontenpfaendung-655-2014`

**Fokus:** Gläubiger hat Schuldner der im EU-Ausland ein Bankkonto haelt und moechte dieses vorlaeufig sichern. EuKtPVO VO (EU) 655/2014 §§ 946 ff. ZPO. Prüfraster: Antrag deutsches Gericht Glaubhaftmachung Anspruch Sicherungsbedürfnis Sicherheitsleistung Drittstaaten-Wirkung alle EU-Mitgliedstaaten außer Daenemark anschließender PfUeB national § 829 ZPO. Output: Antrag Europaeische Kontenpfaendung und Folgepfaendung. Abgrenzung zu zv-pfueb-bank (inlaendisches Konto) und zv-kommandocenter.

# Europäische Kontenpfändung (EuKtPVO, VO (EU) 655/2014)


## Triage zu Beginn

1. Hat der Schuldner ein Konto in einem EU-Mitgliedstaat (außer Dänemark)?
2. Liegt ein vollstreckbarer Titel vor oder ist die Hauptsache noch anhängig?
3. Besteht Sicherungsbedürfnis — droht der Schuldner Vermögen zu verbringen?
4. Ist die Forderung bezifferbar und fällig?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- Verordnung (EU) Nr. 655/2014 (EuKtPVO), in Kraft seit 18.01.2017
- §§ 946-959 ZPO — deutsche Durchführungsbestimmungen zur EuKtPVO
- Art. 5 EuKtPVO — Voraussetzungen (Anspruch + Sicherungsbedürfnis)
- Art. 7 EuKtPVO — Glaubhaftmachung (überwiegende Wahrscheinlichkeit)
- Art. 12 EuKtPVO — Sicherheitsleistung (Regelfall: 5-10 Prozent der Forderung)
- Art. 14 EuKtPVO — Kontensuche durch Auskunftsbehörde
- Art. 33, 34 EuKtPVO — Rechtsbehelfe des Schuldners

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Vorläufige grenzüberschreitende Sicherung von Bankkonten des Schuldners in einem anderen EU-Mitgliedstaat (außer Dänemark). Die EuKtPVO schließt eine Lücke zwischen der EuGVVO (Vollstreckungsanerkennung) und dem Bedürfnis nach **schneller, EU-weiter Sicherung** vor einem Hauptsacheurteil — vergleichbar mit der nationalen PfÜB-Sicherung (§ 829 ZPO), aber **EU-weit** wirkend.

> **Abgrenzung:** Die EuKtPVO ist eine **Sicherungs-Maßnahme** (vergleichbar dem Arrest § 916 ZPO), kein Vollstreckungsverfahren. Für die anschließende Befriedigung benötigt der Gläubiger einen vollstreckbaren Titel und vollstreckt dann im Sitzstaat des Drittschuldners nach dortigem Recht.

## Startet bei

- Schuldner hat (vermutet) Konto in einem EU-Mitgliedstaat außer Deutschland und außer Dänemark
- Hauptsacheverfahren in DE anhängig oder vollstreckbarer Titel in DE liegt vor
- Fluchtgefahr / Vermögensverbringung droht
- Klassische deutsche PfÜB nach § 829 ZPO reicht nicht (Bank im Ausland erkennt deutschen Titel nicht ohne Verfahren an)

## Rechtsgrundlagen

- **Verordnung (EU) Nr. 655/2014** (EuKtPVO) vom 15.5.2014, in Kraft seit 18.1.2017.
- **§§ 946–959 ZPO** — deutsche Durchführungsbestimmungen.
- **§§ 943, 946 ZPO** — Zuständigkeit (Gericht der Hauptsache oder Vollstreckungsgericht).
- **Art. 5 EuKtPVO** — Antragsvoraussetzungen (Anspruch + Sicherungsbedürfnis).
- **Art. 7 EuKtPVO** — Beweismaß (glaubhaft + überwiegende Wahrscheinlichkeit).
- **Art. 12 EuKtPVO** — Sicherheitsleistung.
- **Art. 14 EuKtPVO** — Kontensuche durch Auskunftsbehörde (in DE: Bundesamt für Justiz nach § 948 ZPO; weitere Befugnis Gerichtsvollzieher analog § 802l ZPO).
- **Art. 25 EuKtPVO** — Erklärung des Drittschuldners (Bank) über die Vollziehung nach Erlass des Beschlusses.
- **Art. 33 EuKtPVO** — Rechtsbehelf des Schuldners gegen den Beschluss (Aufhebung/Änderung im Ursprungsmitgliedstaat).
- **Art. 34 EuKtPVO** — Rechtsbehelf des Schuldners gegen die Vollziehung im Vollstreckungsmitgliedstaat.
- **Art. 35 EuKtPVO** — Sonstige Rechtsbehelfe für Schuldner und Gläubiger (Freigabe, Anpassung).
- **Art. 13 EuKtPVO** — Schadensersatzhaftung des Gläubigers bei unbegründeter Pfändung.

## Anwendungsbereich (Art. 2 EuKtPVO)

**Anwendbar bei:**
- Zivil- und Handelssachen mit grenzüberschreitendem Bezug
- Forderung muss bezifferbar sein, fällig oder künftig fällig
- Konto in Mitgliedstaat ≠ Mitgliedstaat des Gerichts (= grenzüberschreitend)

**Nicht anwendbar:**
- Familien-, Erb-, Sozial-, Steuer-, Zollsachen
- Konkurs/Insolvenz
- Schiedsverfahren
- Dänemark (Opt-out)

## Gläubiger

### Schritt 1 — Vorab-Prüfung

- Konto-Mitgliedstaat bekannt oder vermutet?
- Hauptsache anhängig (oder Titel vorhanden)?
- Sicherungsbedürfnis (drohende Vermögensverbringung) substantiierbar?
- Vorab-Kostenkalkulation: Gericht + Sicherheitsleistung + Bankgebühren in Ziel-MS

### Schritt 2 — Antrag § 946 ZPO + Formblatt

- **Standardformular** I der Durchführungsverordnung (EU) 2016/1823 verwenden
- **Sprachen:** Deutsch beim deutschen Gericht; das Gericht übersetzt für den ausländischen Drittschuldner
- **Antragsschrift** mit:
 - Personalien Gläubiger / Schuldner
 - Höhe der Forderung
 - Beleg Hauptsacheverfahren / Titel
 - Glaubhaftmachung Sicherungsbedürfnis
 - Bekannte Konto-Daten (IBAN, BIC, Bank, MS)
 - Falls Konto unbekannt: **Antrag Kontensuche** Art. 14 EuKtPVO

### Schritt 3 — Sicherheitsleistung (Art. 12 EuKtPVO)

- **Grundsatz**: Sicherheitsleistung Pflicht, wenn Gläubiger noch keinen Titel hat (typisch Bürgschaft, Hinterlegung)
- **Befreiung**: möglich, wenn vollstreckbarer Titel vorliegt
- Höhe: regelmäßig 5 %–10 % der zu sichernden Summe (gerichtliches Ermessen)

### Schritt 4 — Gerichtsentscheidung

- **Frist Gericht:**
 - Ohne Titel: bis spätestens 10. Arbeitstag nach Antrag
 - Mit Titel: bis spätestens 5. Arbeitstag nach Antrag
- **Entscheidungs-Beschluss** mit Standardformular II
- Ex-parte-Verfahren (Schuldner wird **nicht** vorher gehört)

### Schritt 5 — Übermittlung an Vollzugs-Mitgliedstaat

- Über Bundesamt für Justiz (BfJ) als Übermittlungsstelle
- BfJ übermittelt Beschluss + Formblätter an zuständige Behörde im Ziel-MS
- Vollzugsbehörde im Ziel-MS leitet Pfändung ein

### Schritt 6 — Vollzug + Rückmeldung

- Drittschuldner-Bank im Ziel-MS sperrt Konto in Höhe der Forderung (Art. 24 EuKtPVO)
- Schuldner wird **danach** informiert (Überraschungseffekt zentral)
- Drittschuldner-Erklärung Art. 25 EuKtPVO an Gläubiger

### Schritt 7 — Hauptsacheverfahren / Titel-Erlangung

- Wenn Antrag vor Titel: **30 Tage nach Pfändung** muss Hauptsache eingeleitet sein (Art. 10 EuKtPVO), sonst Aufhebung
- Bei Titel: Vollstreckung im Ziel-MS nach EuGVVO (Brüssel Ia) oder vereinfachtem Verfahren EuVTVO

## Schuldnerschutz

- **Rechtsbehelf** Art. 33 EuKtPVO: Schuldner kann den Beschluss anfechten beim ausstellenden Gericht
- **Schadensersatz** Art. 13 EuKtPVO bei unbegründeter Pfändung (Sicherheitsleistung haftet)
- **P-Konto-Schutz** des nationalen Rechts gilt im Ziel-MS (in DE: § 850k ZPO)

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Antrag ohne Sicherungsbedürfnis | Ablehnung; Schadensersatz droht | Begründung nachbessern | Klare Substantiierung |
| Konto-MS Dänemark / UK | EuKtPVO nicht anwendbar; nationales Verfahren | Alternative prüfen | EU-MS mit Anwendbarkeit |
| 30-Tage-Frist Hauptsache versäumt | Pfändung wird aufgehoben; Schadensersatz | Frist eng | Hauptsache eingeleitet |
| Sicherheit zu niedrig | Gericht setzt höher fest | Verhandlung | Angebot über 5 %-Grenze |
| Steuersachen / Familiensachen | Anwendungsbereich nicht eröffnet | falsche Rechtsgrundlage | Zivilrechtssache |

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Schlussanträge GA Szpunar v. 29.7.2019 in C-555/18
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Praxis 2026

- **Brüssel Ia und EuKtPVO** sind **getrennt** anwendbar: EuKtPVO sichert vor/nach Titel; Brüssel Ia vollstreckt nach Titel-Erlangung
- **Übersetzungskosten** trägt Gläubiger; das Gericht übernimmt aber die Übermittlung
- **Bank-Kosten** im Ziel-MS variieren; in IT/FR/ES regelmäßig 50–200 EUR

## Ausgabeformat

- Antragsschrift nach Formblatt I VO (EU) 2016/1823 (deutsch)
- Übersicht: Anspruch / Forderung / Konto / MS / Sicherheit
- Frist-Tracker: 30 Tage Hauptsache, 10/5 Arbeitstage Gerichtsentscheidung
- Schuldner-Schutz-Hinweise

## Querverweise

- `zv-pfueb-bank` — nationale Kontopfändung Inland nach § 829 ZPO (Vergleich)
- `zv-kontensuche-drittschuldner` — nationale Kontensuche § 802l ZPO
- `zv-titel-klausel-zustellung` — Titel-Vorprüfung vor EuKtPVO-Antrag bei Titel-Variante
- `fachanwalt-internationales-wirtschaftsrecht` — EuGVVO Brüssel Ia, Rom I
- `aussenwirtschaft-zoll-sanktionen` — Sanktionen / OFAC-Konflikt bei Konto-Sicherung

## Quellen und Updates

Stand: 05/2026. VO (EU) 655/2014 in Kraft seit 18.1.2017. Durchführungsverordnung (EU) 2016/1823 für Formblätter. §§ 946–959 ZPO als DurchführungsRecht. Bei Reform / DAC9-Erweiterung aktualisieren.

## 3. `zv-kommandocenter`

**Fokus:** Gläubiger oder Anwalt hat vollstreckbaren Titel und fragt: Welche Vollstreckungsart ist im konkreten Fall am sinnvollsten und wie wird sie eingeleitet? Startpunkt Zwangsvollstreckung. Prüfraster: Titelart und Vollstreckungsziel Routing zu passenden Skills Drei-Saeulen-Prüfung Titel Klausel Zustellung. Output: Vollstreckungs-Routing-Entscheidung mit passendem Folge-Skill. Abgrenzung zu zv-titel-klausel-zustellung (Formalprüfung) und allen anderen ZV-Skills.

# Zwangsvollstreckung – Kommandocenter


## Triage zu Beginn

1. Liegen alle drei Säulen vor: Titel (§ 704 ZPO), Klausel (§ 724 ZPO), Zustellung (§ 750 ZPO)?
2. Welches Vollstreckungsziel wird verfolgt (Geld, Räumung, Herausgabe, Handlung)?
3. Sind Vermögenswerte bekannt (Konto, Arbeitgeber, Grundbesitz)?
4. Ist der Schuldner in Insolvenz — § 89 InsO Vollstreckungsverbot prüfen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 704 ZPO — Vollstreckungstitel
- § 724 ZPO — vollstreckbare Ausfertigung (Klausel)
- § 750 ZPO — Zustellung als Vollstreckungsvoraussetzung
- § 802a ZPO — Aufgaben des Gerichtsvollziehers
- § 829 ZPO — Pfändungs- und Überweisungsbeschluss (Forderungspfändung)
- § 89 InsO — Vollstreckungsverbot nach Insolvenzeröffnung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Das Kommandocenter steuert den gesamten Vollstreckungspfad: vom Erstgespräch bis zur Beendigung. Es erkennt, welcher Titel vorliegt, was vollstreckt werden soll, welche Vermögenswerte bekannt sind und welcher Folge-Skill als Nächstes geladen werden muss. Es ist der einzige Skill, der ohne Vorwissen gestartet werden kann.

## Eingaben

1. **Titelart**: Urteil (rechtskräftig oder vorläufig vollstreckbar), Vollstreckungsbescheid, gerichtlicher oder notarieller Vergleich, notarielle Urkunde mit Unterwerfung (§ 794 Abs. 1 Nr. 5 ZPO), vollstreckbare Ausfertigung des Tabellenauszugs (§ 201 InsO), Kostenfestsetzungsbeschluss.
2. **Vollstreckungsziel**: Geld, Räumung, Herausgabe, Handlung, Unterlassung.
3. **Schuldnersituation**: Privatperson, Selbstständige, Unternehmen, Insolvenz, Verbraucherinsolvenz, P-Konto bekannt.
4. **Bekannte Vermögenswerte**: Bankkonten, Arbeitgeber, Grundbesitz, Kfz, Forderungen gegen Dritte.
5. **Bisherige Vollstreckungsversuche**: erfolglos, Vermögensauskunft schon abgegeben, Sperrfrist § 802d ZPO.

## Drei-Säulen-Prüfung vor jedem Vollstreckungsschritt

Niemand darf vollstrecken, ohne **alle drei** Säulen geprüft zu haben:

1. **Titel** § 704 ZPO – formgerechte Ausfertigung vorhanden.
2. **Klausel** § 724 ZPO – vollstreckbare Ausfertigung mit Klauselvermerk (Ausnahme: Vollstreckungsbescheid, der die Klausel von Gesetzes wegen trägt § 796 Abs. 1 ZPO; Tabellenauszug § 201 Abs. 2 InsO).
3. **Zustellung** § 750 ZPO – Titel mit Klausel ist dem Schuldner vor der Vollstreckung zugestellt worden (Wartefrist 2 Wochen für Klauselzustellung bei Klauseln nach §§ 726 ff. ZPO).

Wenn auch nur eine Säule fehlt: **STOPP**. Der Skill bricht die Vollstreckung ab und ruft `zv-titel-klausel-zustellung`.

## Routing-Tabelle

| Wenn vorhanden / gewünscht | Lade Skill |
| --- | --- |
| Forderung noch ohne Titel | `forderungsmanagement-klagewerkstatt/inkasso-zahlungsklage-ersteller` (anderes Plugin) |
| Antrag auf Mahnbescheid | `zv-mahnbescheid-online` |
| Mahnbescheid liegt vor, kein Widerspruch | `zv-vollstreckungsbescheid-folge` |
| Vollstreckungsbescheid in Hand, Konto bekannt | `zv-pfueb-bank` |
| Lohnforderung gepfändet werden soll | `zv-pfueb-arbeitsentgelt` |
| Forderung gegen Mieter, Finanzamt, Krankenkasse | `zv-pfueb-mieter-finanzamt` |
| Kein Vermögen bekannt | `zv-vermoegensauskunft-gv` oder `zv-kontensuche-drittschuldner` |
| Notarielle Urkunde mit Grundschuld vorhanden | `zv-notarielle-urkunde-grundschuld` |
| Vollstreckung in Immobilie | `zv-zvg-antrag-glaeubiger` |
| Tabellenauszug aus aufgehobenem oder beendetem Insolvenzverfahren | `zv-tabellenauszug-201-inso` |
| Mobile Pfändung vor Ort | `zv-mobiliar-gv-auftrag` |
| Räumung von Wohn- oder Geschäftsraum | `zv-raeumung-885` |
| Schuldnerseite: Vollstreckung wehren | `zv-abwehr-schuldner` |
| Pfändungsfreigrenze berechnen | `zv-pfaendungstabelle-2025` |

## Reform-Stand 2026/2027 (ZVollstrDigitG)

Das Gesetz zur weiteren Digitalisierung der Zwangsvollstreckung (BT-Drs. 21/4815) bringt für die Praxis drei zentrale Änderungen, die der Skill bei jeder Beratung mitberücksichtigt:

1. **Inkrafttreten Hauptteile**: 1.10.2026 – neue Pfändungsformulare, XML-Antrag nach § 829 Abs. 5 ZPO n.F. möglich (PDF + XML; XML ist führend).
2. **Pflicht für Kreditinstitute**: ab 1.10.2027 müssen Banken einen sicheren elektronischen Übermittlungsweg eröffnen (§ 173 Abs. 2 Nr. 1 ZPO n.F.) – eBO oder andere Wege nach § 130a Abs. 4 ZPO. Vorher freiwillig.
3. **§ 840 ZPO Drittschuldnererklärung**: Postzustellung zusätzlich zur GV-Zustellung und elektronischen Zustellung.

Stand 25.5.2026: Gesetz im Bundestag beschlossen am 19.3.2026, Bundesrat nicht zustimmungspflichtig, Verkündung im BGBl stand bei letzter Recherche noch aus – `zv-elektronische-zustellung-2027` enthält die operative Umsetzung und prüft, ob das Datum zwischenzeitlich angepasst werden muss.

## Ausgabeformat

```
ZV-KOMMANDOCENTER [Mandant] [Az]

Titel: [Art, Datum, Aussteller]
Klausel: [vorhanden / fehlt / wo beantragen]
Zustellung: [erfolgt am DD.MM.JJJJ / offen]
Drei Säulen: [GRÜN / GELB / ROT]

Vollstreckungsziel: [Geld EUR x / Räumung / Herausgabe / ...]
Schuldner: [Privat / Unternehmen / Insolvenz / sonst]
Bekannte Werte: [Bank / AG / Immobilie / Kfz / nichts]

NÄCHSTER SKILL: [zv-...]
Begründung: [warum dieser Pfad]
Wiedervorlage: [in N Tagen wegen ...]
```

## Qualitätsgates

- Niemals Folge-Skill laden, wenn eine der drei Säulen rot ist.
- Niemals Mobiliar- oder Forderungspfändung empfehlen, wenn Schuldner in Insolvenz – dann § 89 InsO Vollstreckungsverbot greift.
- Niemals Sperrfrist § 802d ZPO (zwei Jahre Vermögensauskunft) ignorieren.
- Bei Verbraucher: stets Pfändungsfreigrenze nach Tabelle 1.7.2025 mitdenken.

## Arbeitsstil

Disziplinarisch, klar, ohne juristisches Wortgeklingel. Wenn Säulen wackeln, ist das die einzige Botschaft. Wenn der Schuldner offensichtlich vermögenslos ist, sagt der Skill das frühzeitig und schickt nicht in eine teure Mobiliarvollstreckung.
