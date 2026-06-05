---
name: kv-mutterschaftsgeld
description: "KV Mutterschaftsgeld: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KV Mutterschaftsgeld

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **KV Mutterschaftsgeld** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-065-mutterschaftsgeld-und-schwangerschaftsleistungen` | GKV-Leistungen für Schwangere und Mütter: Mutterschaftsgeld (§ 24i SGB V), Schwangerschaftsvorsorge, Entbindungsleistungen und Nachsorge. |
| `kv-066-kinderkrankengeld-und-pflegezeit` | Kinderkrankengeld nach § 45 SGB V: Anspruch, Dauer, Erweiterung durch Corona-Regelungen; Pflege und Betreuung erkrankter Kinder im Leistungsrecht. |
| `kv-067-verletztengeld-krankengeld-abgrenzung` | Abgrenzung Verletztengeld (BG, § 45 SGB VII) und Krankengeld (GKV, § 44 SGB V): Zuständigkeit bei Arbeitsunfall, Höhe, Übergang und Gleichzeitigkeit. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **KV Mutterschaftsgeld**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-065-mutterschaftsgeld-und-schwangerschaftsleistungen`

**Fokus:** GKV-Leistungen für Schwangere und Mütter: Mutterschaftsgeld (§ 24i SGB V), Schwangerschaftsvorsorge, Entbindungsleistungen und Nachsorge.

# Mutterschaftsgeld und Schwangerschaftsleistungen

## Skill-Zweck

Dieser Skill klärt alle **GKV-Leistungen rund um Schwangerschaft und Geburt**: Mutterschaftsgeld, Vorsorgeuntersuchungen, Entbindung und Nachsorge.

## Rechtlicher Rahmen

- **§ 24a SGB V** – Schwangerschaftsvorsorge und -beratung
- **§ 24b SGB V** – Empfängnisverhütung, Sterilisation, Schwangerschaftsabbruch
- **§ 24c SGB V** – Entbindung
- **§ 24d SGB V** – Hebammenhilfe
- **§ 24e SGB V** – Stillförderung
- **§ 24i SGB V** – Mutterschaftsgeld
- **§ 26a SGB V** – Zusätzliche Leistungen Schwangere (Satzungsleistungen)
- **MuSchG** (Mutterschutzgesetz) §§ 18–24 – Arbeitnehmerinnen
- BSG B 1 KR 7/21 R (Mutterschaftsgeld, Berechnung)

## Mutterschaftsgeld-Systematik

| Parameter | Inhalt |
|-----------|--------|
| Anspruch | 6 Wochen vor + 8 Wochen (12 bei Mehrlingen/Frühgeburt) nach Geburt |
| Betrag | 100 % des Nettoentgelts (bis max. 13 €/Kalendertag aus GKV) |
| Aufstockung | AG zahlt Differenz zu 100 % (MuSchG § 20) |
| Anspruchsvoraussetzung | Beschäftigung + GKV-Mitgliedschaft mit Anspruch auf Krankengeld |

## Prüfprogramm

### Schritt 1 – Mutterschaftsgeld-Anspruch (§ 24i SGB V)
- GKV-Mitglied mit Krankengeld-Anspruch (Pflichtmitglied in Beschäftigung)?
- Beschäftigungsverbot nach MuSchG ab 6 Wochen vor Geburt?
- Antragsstellung: bei der Kasse; spätestens ab 7. Monat
- Höhe: durchschnittliches Nettoentgelt der letzten 3 Monate; max. 13 €/Tag aus GKV

### Schritt 2 – AG-Aufstockung (MuSchG § 20)
- AG zahlt Differenz zwischen Mutterschaftsgeld (13 €/Tag) und tatsächlichem Nettoentgelt
- Bei variablem Entgelt: Durchschnitt letzter 3 Monate vor Beginn des Beschäftigungsverbots
- AG erhält Ausgleich durch Arbeitgeberumlage (U2)

### Schritt 3 – Schwangerschaftsvorsorge (§ 24a SGB V)
- Mutterschaftsrichtlinien (G-BA): Vorsorgeuntersuchungen, Blutgruppe, Ultraschall
- Kosten vollständig von GKV getragen
- Zusätzliche IGeL-Untersuchungen: privat zu zahlen; keine Kassenleistung
- Ersttrimester-Screening, 3D-Ultraschall: nicht automatisch GKV-Leistung

### Schritt 4 – Entbindung (§ 24c SGB V)
- Im Krankenhaus: vollstationäre Behandlung (§ 39 SGB V)
- Außerklinische Geburt (Geburtshaus, Hausgeburt): GKV-Leistung (§ 24c Abs. 1)
- Hebamme: GKV-Leistung (§ 24d SGB V); freie Hebammenwahl
- Zuzahlung: keine für Entbindung; nur ggf. § 39 Abs. 4 für KH-Aufenthalt

### Schritt 5 – Wochenbett und Nachsorge
- Nachsorgehebamme: GKV-Leistung nach § 24d SGB V
- Haushaltshilfe nach § 38 SGB V: bei stationärer Entbindung und Kind < 12 im Haushalt
- Sonderfall § 26a SGB V: manche Kassen bieten erweiterte Schwangerenleistungen als Satzungsleistung

## Typische Fallen

- **Keine Krankengeld-Berechtigung**: Freiwillig Versicherte ohne KG-Tarif: nur 13 €/Tag aus GKV-Fonds (nicht § 24i Abs. 1); kein AG-Zuschuss.
- **IGeL als Kassenleistung verkauft**: Ersttrimester-Screening als Kassenleistung vermarktet; ist es nicht → Versicherte zahlen selbst und haben keinen Rückforderungsanspruch.
- **Frühgeburt**: 12 statt 8 Wochen Schutzfrist nach Geburt; Antrag aktualisieren.
- **Beschäftigungsverbot und Entgeltverlust**: Individuelles Beschäftigungsverbot (vor den 6 Wochen) → nur MuSchG § 11 (Entgeltfortzahlung durch AG, nicht GKV).

## Output-Formate

- Mutterschaftsgeld-Antrag (Muster)
- AG-Aufstockungs-Berechnung
- Schwangerenvorsorge-Übersicht (GKV vs. IGeL)
- Haushaltshilfe-Antrag nach Geburt
- Nachsorgehebamme-Anforderungsbrief

## Quellen

- [§ 24i SGB V – Mutterschaftsgeld](https://www.gesetze-im-internet.de/sgb_5/__24i.html)
- [§ 24c SGB V – Entbindung](https://www.gesetze-im-internet.de/sgb_5/__24c.html)
- [MuSchG § 20 – AG-Aufstockung](https://www.gesetze-im-internet.de/muschg_2018/__20.html)
- [Mutterschaftsrichtlinien G-BA](https://www.g-ba.de/richtlinien/19/)
- [BSG Mutterschaftsgeld](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 24i SGB V](https://dejure.org/gesetze/SGB_V/24i.html)

## 2. `kv-066-kinderkrankengeld-und-pflegezeit`

**Fokus:** Kinderkrankengeld nach § 45 SGB V: Anspruch, Dauer, Erweiterung durch Corona-Regelungen; Pflege und Betreuung erkrankter Kinder im Leistungsrecht.

# Kinderkrankengeld und Pflegezeit

## Skill-Zweck

Dieser Skill klärt den **Anspruch auf Kinderkrankengeld** bei Betreuung erkrankter Kinder, die seit Covid-Pandemie erhöhten Anspruchszeiten und Abgrenzungen zur Pflegezeit.

## Rechtlicher Rahmen

- **§ 45 SGB V** – Kinderkrankengeld: Anspruch, Dauer, Voraussetzungen
- **§ 616 BGB** – Entgeltfortzahlung bei vorübergehender Verhinderung (parallel)
- **§ 45 Abs. 2a SGB V** – Erweiterte Tage durch Corona (bis Ende 2023)
- **§ 2 PflegeZG** – Kurzzeitige Arbeitsverhinderung bei Pflege nahestehender Personen
- BSG B 1 KR 19/18 R (Kinderkrankengeld, Voraussetzungen)

## Kinderkrankengeld-Systematik 2025

| Parameter | Inhalt |
|-----------|--------|
| Anspruch pro Elternteil | 15 Arbeitstage je Kind (bis 12 Jahre) |
| Alleinerziehend | 30 Arbeitstage je Kind |
| Gesamtbegrenzung | 35 AT/Person (Alleinerziehend: 70 AT) |
| Kind mit Behinderung | Ohne Altersgrenze wenn dauerhaft pflegebedürftig |
| Höhe | 90 % des ausgefallenen Nettolohns |

## Prüfprogramm

### Schritt 1 – Anspruchsvoraussetzungen (§ 45 SGB V)
- Kind erkrankt und ärztlich attestiert?
- Kind unter 12 Jahre (oder pflegebedürftiges Kind ohne Altersgrenze)?
- Keine andere aufsichtspflichtige Person vorhanden?
- Arbeitgeber informiert; Beschäftigungsverbot oder Unmöglichkeit der Arbeit

### Schritt 2 – Kinderkrankengeld beantragen
- Krankenkasse des betreuenden Elternteils (nicht des Kindes)
- Ärztliche Bescheinigung für das Kind (§ 45 Abs. 1 Satz 3 SGB V)
- Arbeitgeberbescheinigung über Verdienstausfall
- Kasse zahlt direkt; AG muss nicht vorleisten

### Schritt 3 – Dauer und Erweiterung
- 15 Arbeitstage pro Elternteil und Kind; ggf. übertragbar zwischen Elternteilen
- Mehrere Kinder: 35 Arbeitstage max. (Alleinerziehend 70)
- Überschreitung nur bei Verlängerungsantrag; medizinische Begründung

### Schritt 4 – § 616 BGB als Alternative/Ergänzung
- § 616 BGB: kurzfristige Entgeltfortzahlung durch AG (einige wenige Tage)
- Tarifverträge: oft großzügigere Regelungen
- Kinderkrankengeld: subsidiär; erst wenn AG-Anspruch erschöpft oder ausgeschlossen

### Schritt 5 – Abgrenzung Pflegezeit
- PflegeZG (§ 2): kurzfristige Arbeitsverhinderung für Pflege nahestehender Personen (bis 10 AT)
- Bezahlte Pflegezeit: Pflegeunterstützungsgeld (§ 44a SGB XI)
- Kinderkrankengeld vs. Pflegeunterstützungsgeld: Kinderkrankengeld bei Erkrankung des Kindes; Pflegeunterstützungsgeld bei Pflegesituation

## Typische Fallen

- **Kind über 12 und krank**: Kinderkrankengeld endet mit 12. Geburtstag; Ausnahme: Behinderung.
- **Beide Elternteile beantragen gleichzeitig**: Jeder Elternteil hat eigene 15-AT-Kontingent; gleichzeitige Inanspruchnahme möglich wenn beide Eltern getrennt betreuen.
- **Schließung von Schule/Kita (nicht Krankheit)**: Kein Kinderkrankengeld bei Schließung ohne Erkrankung des Kindes (außer Corona-Sonderregeln waren befristet).
- **Freiwillig Versicherte**: Haben Anspruch; aber Höhe begrenzt (§ 45 Abs. 4 SGB V: analog).

## Output-Formate

- Kinderkrankengeld-Antrag
- Ärztliche Bescheinigung-Anforderung
- Arbeitgeberbescheinigung-Formular
- Resttage-Berechnung (Jahresübersicht)
- § 616 BGB vs. § 45 SGB V Vergleich

## Quellen

- [§ 45 SGB V – Kinderkrankengeld](https://www.gesetze-im-internet.de/sgb_5/__45.html)
- [§ 2 PflegeZG – Kurzzeitige Arbeitsverhinderung](https://www.gesetze-im-internet.de/pflegezg/__2.html)
- [§ 616 BGB – Entgeltfortzahlung](https://www.gesetze-im-internet.de/bgb/__616.html)
- [BSG B 1 KR 19/18 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband Kinderkrankengeld](https://www.gkv-spitzenverband.de)
- [dejure.org § 45 SGB V](https://dejure.org/gesetze/SGB_V/45.html)

## 3. `kv-067-verletztengeld-krankengeld-abgrenzung`

**Fokus:** Abgrenzung Verletztengeld (BG, § 45 SGB VII) und Krankengeld (GKV, § 44 SGB V): Zuständigkeit bei Arbeitsunfall, Höhe, Übergang und Gleichzeitigkeit.

# Verletztengeld und Krankengeld: Abgrenzung

## Skill-Zweck

Bei Arbeitsunfällen zahlt die Berufsgenossenschaft Verletztengeld statt der GKV Krankengeld. Dieser Skill klärt **Abgrenzung, Höhe, Übergang und was bei streitiger Zuständigkeit gilt**.

## Rechtlicher Rahmen

- **§ 45 SGB VII** – Verletztengeld: Anspruch bei Arbeitsunfall/Berufskrankheit
- **§ 46 SGB VII** – Höhe des Verletztengelds: 80 % des Regelentgelts
- **§ 47 SGB VII** – Ende des Verletztengelds
- **§ 44 SGB V** – Krankengeld: GKV-Anspruch
- **§ 49 Abs. 1 Nr. 3 SGB V** – Ruhen des Krankengelds bei Bezug von Verletztengeld
- BSG B 2 U 5/20 R (Verletztengeld-Berechnung), BSG B 1 KR 8/04 R (Vorleistung GKV)

## Vergleich: Verletztengeld vs. Krankengeld

| Merkmal | Verletztengeld (BG) | Krankengeld (GKV) |
|---------|---------------------|-------------------|
| Träger | Berufsgenossenschaft (§ 45 SGB VII) | Krankenkasse (§ 44 SGB V) |
| Auslöser | Arbeitsunfall, Wegeunfall, BK | Krankheit (nicht Arbeitsunfall) |
| Höhe | 80 % des Regelentgelts (keine Deckelung) | 70 % Regelentgelt, max. 90 % Netto |
| Dauer | Bis Arbeitsfähigkeit oder Übergang in Verletztenrente | 78 Wochen (Blockfrist) |
| Zuzahlung | Keine | Keine |

## Prüfprogramm

### Schritt 1 – Arbeitsunfall-Prüfung (→ kv-049)
- Liegt ein Arbeitsunfall vor? (§ 8 SGB VII)
- BG-Anerkennung: D-Arzt informiert BG; BG stellt Verletztengeld-Anspruch fest

### Schritt 2 – Ruhen des Krankengelds (§ 49 SGB V)
- Während Verletztengeld-Bezug: GKV-Krankengeld ruht vollständig
- GKV-Mitgliedschaft bleibt erhalten; nur Krankengeld-Zahlung suspendiert
- GKV muss vorleisten wenn BG-Zuständigkeit unklar (§ 105 SGB X)

### Schritt 3 – Höhenvergleich
- Verletztengeld: 80 % des Regelentgelts, ohne Beitragsbemessungsgrenzen-Kappung
- Krankengeld: 70 % (GKV), begrenzt auf Beitragsbemessungsgrenze
- Fazit: Verletztengeld oft höher (besonders bei besser Verdienenden)

### Schritt 4 – Übergang und Lückenlosigkeit
- BG stellt Verletztengeld ab Tag des Unfalls; GKV stellt ab Beginn der AU fest
- Nahtloser Übergang sicherstellen; keine Lücke zwischen GKV und BG
- Übergang BG→Verletztenrente: wenn Arbeitsunfähigkeit fortbesteht nach 78 Wochen

### Schritt 5 – Streitige Zuständigkeit
- BG bestreitet Arbeitsunfall: GKV zahlt Krankengeld; BG erstattet (§ 105 SGB X)
- Versicherter informiert beide Träger gleichzeitig
- Widerspruch bei BG (Ablehnung Anerkennung); parallel Krankengeld sichern

## Typische Fallen

- **D-Arzt nicht aufgesucht**: BG-Leistungen verzögert; GKV zahlt vorläufig Krankengeld; Erstattung an GKV.
- **Höhenunterschied nicht genutzt**: Versicherter weiß nicht dass Verletztengeld höher; nicht aktiv eingefordert.
- **AU-Bescheinigung gilt für beide**: GKV-AU-Bescheinigung auch für BG ausreichend; D-Arzt-Attest zusätzlich optimal.
- **BK-Verfahren dauert lange**: Berufskrankheits-Verfahren dauert Monate; GKV muss während dieser Zeit Krankengeld zahlen.

## Output-Formate

- Verletztengeld-Berechnung (Tabelle)
- Antrag auf Verletztengeld an BG
- GKV-Vorleistungsanzeige
- Zuständigkeitsprüfungs-Schreiben
- Widerspruch BG-Ablehnungsbescheid

## Quellen

- [§ 45 SGB VII – Verletztengeld](https://www.gesetze-im-internet.de/sgb_7/__45.html)
- [§ 49 SGB V – Ruhen Krankengeld](https://www.gesetze-im-internet.de/sgb_5/__49.html)
- [§ 105 SGB X – Vorleistung](https://www.gesetze-im-internet.de/sgb_10/__105.html)
- [DGUV Verletztengeld](https://www.dguv.de)
- [BSG B 2 U 5/20 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 45 SGB VII](https://dejure.org/gesetze/SGB_VII/45.html)
## Hinweis: Übergangsbereich und praktische Koordination

- Unfallmeldepflicht des Arbeitgebers (§ 193 SGB VII) ist Voraussetzung für schnelle UV-Leistung
- Krankenkasse leistete vor, wenn UV-Träger Zuständigkeit prüft → Erstattungsanspruch nach § 105 SGB X
- Verletztengeld endet bei Eintritt von Rente aus der UV (Verletztenrente) oder bei Heilung
- Übergang ins Krankengeld bei UV-Träger-Ablehnung: sofort Krankengeld bei GKV beantragen

## Weiterführende Quellen

- [§ 45 SGB VII – Verletztengeld](https://www.gesetze-im-internet.de/sgb_7/__45.html)
- [§ 44 SGB V – Krankengeld](https://www.gesetze-im-internet.de/sgb_5/__44.html)
- [§ 105 SGB X – Erstattungsanspruch nachrangiger Träger](https://www.gesetze-im-internet.de/sgb_10/__105.html)
- [BSG – Abgrenzung Verletztengeld/Krankengeld](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
