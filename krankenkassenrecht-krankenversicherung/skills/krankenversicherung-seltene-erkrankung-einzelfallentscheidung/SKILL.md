---
name: krankenversicherung-seltene-erkrankung-einzelfallentscheidung
description: "Seltene Erkrankung Einzelfallentscheidung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Seltene Erkrankung Einzelfallentscheidung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Seltene Erkrankung Einzelfallentscheidung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-053-seltene-erkrankung-einzelfallentscheidung` | GKV-Leistungsanspruch bei seltenen Erkrankungen: § 2 Abs. 1a SGB V, Nikolaus-Beschluss des BVerfG, Off-Label-Use ohne Nutzenbewertung und Einzelfallgenehmigung. |
| `kv-054-kostenerstattung-privatarzt-in-der-gkv` | Kostenerstattungsverfahren nach § 13 SGB V: Wahlerklärung, Systemversagen, Notfall, GOÄ-Abrechnung und Erstattungsgrenzen in der GKV. |
| `kv-055-versicherte-im-ausland-lebend-deutsche-rente` | Krankenversicherung für im Ausland lebende Rentner mit deutschen Rentenansprüchen: KVdR, S1-Formular, EU-Koordinierungsrecht und bilaterale Abkommen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Seltene Erkrankung Einzelfallentscheidung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-053-seltene-erkrankung-einzelfallentscheidung`

**Fokus:** GKV-Leistungsanspruch bei seltenen Erkrankungen: § 2 Abs. 1a SGB V, Nikolaus-Beschluss des BVerfG, Off-Label-Use ohne Nutzenbewertung und Einzelfallgenehmigung.

# Seltene Erkrankung: Einzelfallentscheidung

## Skill-Zweck

Bei seltenen Erkrankungen fehlen oft zugelassene Therapien oder G-BA-Beschlüsse. Dieser Skill entwickelt die **Argumentation nach § 2 Abs. 1a SGB V und dem Nikolaus-Beschluss des BVerfG**.

## Rechtlicher Rahmen

- **§ 2 Abs. 1a SGB V** – Grundrechtsorientierte Auslegung: bei lebensbedrohlicher/regelmäßig tödlicher Erkrankung
- **BVerfG 1 BvR 347/98** – „Nikolaus-Beschluss": Grundrecht auf Leben schlägt Wirtschaftlichkeit
- **§ 31 Abs. 1 Satz 4 SGB V** – Nicht-verschreibungspflichtige AM auf Einzelantrag
- **§ 35c SGB V** – Besondere Therapierichtungen (Off-Label mit Sonderregelung)
- **§ 116b SGB V** – Ambulante spezialfachärztliche Versorgung (ASV): für seltene Erkrankungen
- VO (EG) 141/2000 – Orphan-Drug-Verordnung (EU-Zulassung)
- BSG B 1 KR 37/04 R (Off-Label-Dreitest), BSG B 1 KR 10/12 R (§ 2 Abs. 1a SGB V)

## § 2 Abs. 1a SGB V – Normvoraussetzungen

| Voraussetzung | Inhalt |
|--------------|--------|
| Erkrankung | Lebensbedrohlich oder regelmäßig tödlich |
| Keine zugelassene Therapie | Oder Therapiealternative nicht wirksam/unzumutbar |
| Behandlungsaussicht | Nicht ganz fernliegende Aussicht auf Heilung oder Linderung |
| Anspruchsgrundlage | Trotz fehlendem G-BA-Beschluss |

## Prüfprogramm

### Schritt 1 – Erkrankung einordnen
- Seltene Erkrankung (Orphan Disease): Prävalenz < 5 von 10.000 (EU-Definition)
- ICD-10 / ORPHA-Code: verwenden
- Lebensbedrohlichkeit: ist die Erkrankung in ihrem natürlichen Verlauf lebensbedrohlich?

### Schritt 2 – Behandlungsoptionen prüfen
- Alle GKV-anerkannten Therapien ausgeschöpft oder kontraindiziert?
- Ist eine alternative zugelassene Behandlung verfügbar und wirksam?
- Wenn keine Alternative: § 2 Abs. 1a SGB V greift potenziell

### Schritt 3 – Off-Label nach BVerfG-Maßstäben
- BSG B 1 KR 37/04 R: 3-Voraussetzungen-Test (Erkrankung, Alternativlosigkeit, Aussicht)
- Wissenschaftliche Belege: Phase II/III-Studien, Fallberichte, Fachgesellschafts-Empfehlungen
- Kein Beschluss des G-BA erforderlich wenn BVerfG-Voraussetzungen erfüllt

### Schritt 4 – ASV für seltene Erkrankungen (§ 116b SGB V)
- ASV: Fachärzte können ambulant stationäre Eingriffe und komplexe Behandlungen abrechnen
- Liste der seltenen Erkrankungen nach § 116b SGB V: G-BA-Beschlüsse
- Team-Versorgung: Konsortium von Spezialisten
- Keine Überweisung nötig; direkt zum ASV-Team

### Schritt 5 – Antrag und Begründung
- Antrag mit ärztlichem Gutachten: ausführliche Darstellung der Erkrankung, Alternativlosigkeit, Therapieaussicht
- Literaturrecherche: PubMed, ORPHAN-Datenbank, Fachgesellschaftsleitlinien
- Anwalt: bei Ablehnung empfehlen (komplexe Materie)

## Typische Fallen

- **Zu geringe Erkrankungsschwere**: § 2 Abs. 1a SGB V gilt nicht bei chronisch-schweren Erkrankungen die nicht lebensbedrohlich sind; dann Off-Label-Dreitest.
- **Orphan Drug ≠ automatisch GKV-Leistung**: EU-Zulassung als Orphan Drug begründet keinen automatischen GKV-Anspruch; G-BA oder § 2 Abs. 1a nötig.
- **Experimentelle Therapien**: BVerfG verlangt „nicht ganz fernliegende Aussicht"; rein experimentelle Therapien ohne Wirksamkeitshinweise genügen nicht.
- **Eilantrag bei seltener Erkrankung**: Häufig lebensbedrohlich → Eilantrag SG; einstweilige Anordnung.

## Output-Formate

- Antragsschreiben § 2 Abs. 1a SGB V
- Off-Label-Dreitest-Analyse
- Literaturübersicht (Wirksamkeitsbelege)
- Eilantrag Sozialgericht (Muster)
- Widerspruchsbegründung bei Ablehnung

## Quellen

- [§ 2 Abs. 1a SGB V](https://www.gesetze-im-internet.de/sgb_5/__2.html)
- [BVerfG 1 BvR 347/98 – Nikolaus-Beschluss](https://www.bverfg.de/e/rs19990109_1bvr034798.html)
- [§ 116b SGB V – ASV](https://www.gesetze-im-internet.de/sgb_5/__116b.html)
- [BSG B 1 KR 37/04 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [ORPHANET Seltene Erkrankungen](https://www.orpha.net)
- [dejure.org § 2 SGB V](https://dejure.org/gesetze/SGB_V/2.html)

## 2. `kv-054-kostenerstattung-privatarzt-in-der-gkv`

**Fokus:** Kostenerstattungsverfahren nach § 13 SGB V: Wahlerklärung, Systemversagen, Notfall, GOÄ-Abrechnung und Erstattungsgrenzen in der GKV.

# Kostenerstattung: Privatarzt in der GKV

## Skill-Zweck

GKV-Versicherte können unter bestimmten Umständen einen Privatarzt aufsuchen und Kostenerstattung von der Kasse verlangen. Dieser Skill klärt **Wahlerklärung, Systemversagen, Notfall und Erstattungsgrenzen nach § 13 SGB V**.

## Rechtlicher Rahmen

- **§ 13 SGB V** – Kostenerstattung: mehrere Varianten
- **§ 13 Abs. 1 SGB V** – Kostenerstattungswahlrecht: freiwillig Versicherte wählen Kostenerstattung
- **§ 13 Abs. 2 SGB V** – Ermächtigung Kasse bei Systemversagen
- **§ 13 Abs. 3 SGB V** – Systemversagen und Notfall: Erstattung selbst beschaffter Leistungen
- **§ 13 Abs. 3a SGB V** – Genehmigungsfiktion
- BSG B 1 KR 35/04 R (Systemversagen), BSG B 1 KR 3/13 R (Kostenerstattungsgrenze)

## Kostenerstattungs-Typen (§ 13 SGB V)

| Variante | Voraussetzung | Erstattungshöhe |
|----------|--------------|-----------------|
| § 13 Abs. 1 | Wahlerklärung Kostenerstattung | GKV-Ausgaben abzgl. Abzüge |
| § 13 Abs. 3 Alt. 1 | Systemversagen (Kasse konnte Leistung nicht rechtzeitig verschaffen) | Kassenleistungsniveau |
| § 13 Abs. 3 Alt. 2 | Notfall | Kassenleistungsniveau |
| § 13 Abs. 3a | Genehmigungsfiktion | Volle Kostenerstattung |

## Prüfprogramm

### Schritt 1 – Wahlerklärung (§ 13 Abs. 1 SGB V)
- Freiwillig Versicherte können Kostenerstattung wählen statt Sachleistung
- Wahlerklärung gegenüber Kasse: bindet für mindestens 1 Quartal
- Erstattung: was Kasse für Sachleistung aufgewendet hätte abzgl. 5 % Verwaltungskosten
- Nicht für jeden sinnvoll: Sachleistungsprinzip ist meist günstiger

### Schritt 2 – Systemversagen (§ 13 Abs. 3 Alt. 1)
- Kasse konnte Leistung nicht rechtzeitig beschaffen oder hatte sie zu Unrecht abgelehnt
- Vorabablehnung durch Kasse: direkte Pflicht zur Kostenerstattung
- Systemversagen bei Wartezeiten: Psychotherapie-Fälle häufigster Anwendungsfall
- Dokumentation: Nachweis Wartezeiten, erfolglose Suche nach Kassenleistungserbringer

### Schritt 3 – Notfall (§ 13 Abs. 3 Alt. 2)
- Sofortige Behandlung erforderlich, kein Kassenarzt erreichbar
- Keine Vorabgenehmigung möglich
- Erstattung: auf GKV-Sachleistungsniveau
- Wichtig: Sofort nach Notfall Kasse informieren

### Schritt 4 – Erstattungsgrenzen
- BSG B 1 KR 3/13 R: Erstattung maximal auf GKV-Sachleistungsniveau
- Privatärztliche Mehrleistungen über GKV-Niveau: trägt Versicherter selbst
- GOÄ-Rechnung oft höher als GKV-Leistung → Differenz wird nicht erstattet

### Schritt 5 – Genehmigungsfiktion (§ 13 Abs. 3a SGB V)
- Kasse entscheidet nicht innerhalb von 5 Wochen (3 Wochen bei Eilbedarf)
- Leistung gilt als genehmigt
- Selbstbeschaffung nach Fiktionseintritt: volle Kostenerstattung

## Typische Fallen

- **Kostenerstattung vor Behandlung nicht erklärt**: § 13 Abs. 1 muss VOR Behandlung gewählt werden; nachträgliche Umstellung nicht möglich.
- **Systemversagen nicht dokumentiert**: Ohne Nachweis erfolgloser Kassenleistungssuche kein Systemversagen.
- **Erstattungsgrenze missachtet**: GOÄ-Rechnung übersteigt GKV-Niveau erheblich; Differenz bleibt beim Versicherten.
- **IGeL und Kostenerstattung**: IGeL ist keine GKV-Leistung; keine Kostenerstattung möglich.

## Output-Formate

- Wahlerklärung Kostenerstattung (§ 13 Abs. 1)
- Systemversagen-Dokumentationsbogen
- Kostenerstattungsantrag nach § 13 Abs. 3
- Genehmigungsfiktion-Schreiben
- GKV/GOÄ-Leistungsvergleichsanalyse

## Quellen

- [§ 13 SGB V – Kostenerstattung](https://www.gesetze-im-internet.de/sgb_5/__13.html)
- [BSG B 1 KR 35/04 R – Systemversagen](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [BSG B 1 KR 3/13 R – Erstattungsgrenze](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 13 SGB V](https://dejure.org/gesetze/SGB_V/13.html)
- [GKV-Spitzenverband Kostenerstattung](https://www.gkv-spitzenverband.de)
- [Kassenärztliche Bundesvereinigung](https://www.kbv.de)

## 3. `kv-055-versicherte-im-ausland-lebend-deutsche-rente`

**Fokus:** Krankenversicherung für im Ausland lebende Rentner mit deutschen Rentenansprüchen: KVdR, S1-Formular, EU-Koordinierungsrecht und bilaterale Abkommen.

# Versicherte im Ausland lebend mit deutscher Rente

## Skill-Zweck

Deutsche Rentner, die im EU-Ausland oder in Drittstaaten leben, haben komplexe Krankenversicherungsansprüche. Dieser Skill klärt **Leistungsansprüche, zuständige Träger und praktische Umsetzung**.

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 11 SGB V** – KVdR auch für auslandswohnende Rentner
- **VO (EG) 883/2004 Art. 23, 24** – Rentenempfänger im Ausland: Leistungsanspruch im Wohnstaat
- **§ 140e SGB V** – EU-Patientenrechte
- **S1-Formular** – Registrierung im Wohnstaat für vollständige Leistungen
- Bilaterale Sozialversicherungsabkommen (z.B. mit USA, Türkei, Kanada)
- BSG B 12 KR 8/16 R (KVdR-Anspruch Auslandsrenter)

## Prüfprogramm

### Schritt 1 – KVdR-Anspruch auch im Ausland
- Deutsche Rente + GKV-Vorversicherungszeit → KVdR-Mitgliedschaft auch wenn im EU-Ausland wohnhaft
- Beitrag: wird von Rentenversicherungsträger einbehalten (§ 256 SGB V)
- Kasse in Deutschland bleibt Mitgliedskasse

### Schritt 2 – S1-Formular für EU-Auslandsrentner
- S1 ausstellen lassen: bei der GKV-Kasse in Deutschland
- Im Wohnstaat registrieren: Krankenversicherungsträger des Wohnstaates
- Ergebnis: Voller Leistungsanspruch nach dem Recht des Wohnstaates
- Rückvergütung: Wohnstaat rechnet mit Deutschland ab

### Schritt 3 – Behandlung im Wohnstaat
- Versicherter erhält Leistungen wie Einheimische des Wohnstaates
- Eigenbeteiligungen des Wohnstaates sind zu zahlen (nicht durch deutsche GKV erstattet)
- Geplante Behandlung in Deutschland: wie Inländer; Kasse trägt Kosten

### Schritt 4 – Nicht-EU-Ausland
- Bilaterale Abkommen: z.B. D-Türkei → gegenseitige Leistungsansprüche
- Länder ohne Abkommen (USA, Australien): kein gegenseitiger Anspruch; freiwillige GKV-Mitgliedschaft in Deutschland möglich
- GKV-Mitglied im Ausland ohne Abkommen: Leistungen nur in Deutschland; teuer

### Schritt 5 – Freiwillige GKV für Auslandsrentner
- KVdR nicht erfüllbar (Vorversicherungszeit fehlt) → freiwillige GKV
- Wohnsitz im Ausland: GKV zahlt grundsätzlich nur in Deutschland; Auslandsleistungen eingeschränkt
- Alternative: lokale Krankenversicherung im Wohnstaat + freiwillige GKV für Deutschland-Aufenthalte

## Typische Fallen

- **S1 nicht beantragt**: Rentner wohnt im EU-Ausland ohne S1 → voller Leistungsanspruch dort entgeht; nur Notfallversorgung mit EHIC.
- **Unterschied EHIC/S1**: EHIC für vorübergehende Aufenthalte; S1 für dauerhaften Wohnort.
- **Pflegeversicherung im Ausland**: Ähnliche Regelungen wie KV; PV zahlt bei dauerhaftem EU-Aufenthalt an Wohnstaatträger.
- **Rückkehr nach Deutschland**: KVdR bleibt; Leistungen sofort in Deutschland abrufbar.

## Output-Formate

- S1-Antrag (Muster)
- KVdR-Anspruchscheck für Auslandsrentner
- Bilaterale Abkommens-Übersicht
- Leistungsüberblick EU-Ausland-Rentner
- Kassenanschreiben (S1-Registrierung)

## Quellen

- [§ 5 SGB V – KVdR](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [VO (EG) 883/2004 Art. 23–24](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004R0883)
- [Deutsche Verbindungsstelle Krankenversicherung Ausland (DVKA)](https://www.dvka.de)
- [S1-Formular Informationen](https://www.dvka.de)
- [BSG Auslandsrentner](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)
## Schritt 6 – Rückkehr nach Deutschland und Statusänderung

- Bei Rückkehr nach Deutschland endet S1-Registrierung im Ausland
- KVdR-Mitgliedschaft in Deutschland bleibt bestehen; Leistungsanspruch sofort aktiv
- Wohnortwechsel der Kasse melden (§ 175 SGB V analog)
- Pflegeversicherungsansprüche prüfen (§ 34 SGB XI für Auslandsaufenthalte)

## Hinweis: Pflegeversicherung im Ausland

- Gleiche Koordinierungsregeln wie Krankenversicherung (VO 883/2004 Art. 35)
- Pflegegeld bei dauerhaftem EU-Aufenthalt: Zahlung an Wohnstaatträger, dort nach lokalem Recht
- Bei Nicht-EU-Ausland ohne Abkommen: kein Anspruch auf Pflegeleistungen im Wohnstaat

## Weiterführende Quellen (ergänzend)

- [§ 256 SGB V – Beitragseinbehalt Rentenversicherungsträger](https://www.gesetze-im-internet.de/sgb_5/__256.html)
- [DVKA – Deutsche Verbindungsstelle Krankenversicherung Ausland](https://www.dvka.de)
- [VO (EG) 987/2009 – Durchführungsverordnung](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32009R0987)
