---
name: krankenversicherung-buergergeld-rentner
description: "Buergergeld Rentner: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Buergergeld Rentner

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Buergergeld Rentner** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-020-buergergeld-rentner-und-krankenversicherungspflicht` | Krankenversicherung bei Bürgergeld-Bezug (SGB II) und Rentnern: Pflichtversicherung, Beitragsübernahme, KVdR, Lückenfälle und Widersprüche. |
| `kv-022-satzungsleistungen-bonusprogramm-und-rueckforderung` | Freiwillige Kassenleistungen (Satzungsleistungen, §§ 11 und 194 SGB V), Bonusprogramme und Rückforderungsansprüche der Kasse. |
| `kv-023-md-gutachten-angreifen-befundbericht-und-gegengutachten` | Strategie zur Anfechtung von MDK/MD-Gutachten: Akteneinsicht, Qualitätsprüfung, Gegengutachten, prozessuale Sachverständigenfragen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Buergergeld Rentner**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-020-buergergeld-rentner-und-krankenversicherungspflicht`

**Fokus:** Krankenversicherung bei Bürgergeld-Bezug (SGB II) und Rentnern: Pflichtversicherung, Beitragsübernahme, KVdR, Lückenfälle und Widersprüche.

# Bürgergeld, Rentner und Krankenversicherungspflicht

## Skill-Zweck

Dieser Skill klärt die **Krankenversicherung von Bürgergeld-Beziehenden und Rentnern**: Wer ist pflichtversichert, wer zahlt die Beiträge, was passiert bei Einkommenslücken und wie funktioniert die KVdR?

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 2a SGB V** – Pflichtversicherung ALG-II/Bürgergeld-Bezieher
- **§ 5 Abs. 1 Nr. 11 SGB V** – Pflichtversicherung Rentner (KVdR)
- **§ 251 Abs. 4 SGB V** – Beitragstragung bei Bürgergeld (Bundesagentur/Jobcenter)
- **§ 10 SGB V** – Familienversicherung (ggf. für Bürgergeld-Empfänger über Familienangehörigen)
- **§ 229 SGB V** – Beitragspflicht Versorgungsbezüge (Betriebsrente)
- **§ 256 SGB V** – Beitragszahlung aus Rente durch Rentenversicherungsträger
- **§ 57 SGB XI** – Pflegeversicherungsbeitrag (parallel zur KV)
- BSG B 12 KR 10/17 R (KVdR-Vorversicherungszeit)

## KVdR-Systematik

| Voraussetzung | Inhalt |
|--------------|--------|
| Vorversicherungszeit | In der 2. Hälfte des Erwerbslebens mind. 9/10 der Zeit GKV-versichert |
| Rentenbezug | Gesetzliche Rente (Deutsche Rentenversicherung) |
| Beitragssatz | Allgemeiner KV-Beitragssatz (2025: 14,6 % + kassenindividueller Zusatzbeitrag) |
| Beitragsbasis | Rente + Versorgungsbezüge + Arbeitseinkommen |
| Beitragstragung | Rentner zahlt halben Beitrag; Rentenversicherungsträger die andere Hälfte |

## Prüfprogramm

### Schritt 1 – Bürgergeld-Bezieher (§ 5 Abs. 1 Nr. 2a SGB V)
- ALG-II/Bürgergeld-Bezug → automatische Pflichtversicherung
- Beiträge: Jobcenter trägt Beiträge (§ 251 Abs. 4 SGB V)
- Kasse: Versicherter kann Kasse wählen (§ 175 SGB V)
- Ende Bürgergeld: sofortige Prüfung ob andere Pflichtversicherung oder freiwillige Versicherung

### Schritt 2 – Übergangslücken vermeiden
- Bürgergeld endet, kein sofortiger Job → freiwillige Versicherung innerhalb 3 Monate (§ 9 SGB V)
- Lücke in GKV-Versicherung: Auffangpflichtversicherung (§ 5 Abs. 1 Nr. 13 SGB V) prüfen

### Schritt 3 – KVdR (§ 5 Abs. 1 Nr. 11 SGB V)
- Vorversicherungszeit prüfen: RV-Zeiten anteilig anrechnen
- Rentenantrag stellt keine Pflichtmitgliedschaft her; KVdR-Antrag bei Kasse
- Kein KVdR-Anspruch: freiwillig versichert als Rentner → höhere Beiträge (§ 240 SGB V)

### Schritt 4 – Versorgungsbezüge (§ 229 SGB V)
- Betriebsrenten, Pensionen, Direktversicherungen: beitragspflichtig als Versorgungsbezug
- Freibetrag 2025: 187,25 €/Monat (halber Mindestbeitrag)
- Kapitalzahlungen: auf 10 Jahre verteilt beitragspflichtig (BSG-Rechtsprechung)

### Schritt 5 – Doppelverbeitragung-Problem (→ Skill kv-061)
- Betriebsrente aus Direktversicherung: Beiträge aus Nettolohn gezahlt + nochmals als Versorgungsbezug verbeitragt
- Reform 2020: Freibetrag eingeführt (§ 226 Abs. 2 SGB V), aber Problem nicht vollständig gelöst

## Typische Fallen

- **Bürgergeld endet, Krankheit besteht**: Wenn Krankengeld-Anspruch endet und Bürgergeld endet, entsteht Versicherungslücke; Jobcenter informieren.
- **KVdR-Vorversicherungszeit knapp nicht erfüllt**: Widerspruch mit genauer Berechnung; PKV-Zeiten zählen nicht, aber freiwillige GKV-Zeiten schon.
- **Hinterbliebenenrente**: Empfänger einer Witwenrente können KVdR-Berechtigung haben; eigene Vorversicherungszeit des Hinterbliebenen.
- **Grenzgänger im Rentenbezug**: VO 883/2004 regelt Beitragspflicht; ggf. Beitrag nur in einem Land.

## Output-Formate

- KVdR-Vorversicherungszeitberechnung
- Widerspruch gegen KVdR-Ablehnung
- Bürgergeld-Beitragsübernahme-Checkliste
- Versorgungsbezüge-Beitragsberechnung
- Übergangslücken-Handlungsplan

## Quellen

- [§ 5 SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 229 SGB V – Versorgungsbezüge](https://www.gesetze-im-internet.de/sgb_5/__229.html)
- [§ 251 SGB V – Beitragstragung](https://www.gesetze-im-internet.de/sgb_5/__251.html)
- [BSG KVdR-Rechtsprechung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [Deutsche Rentenversicherung KVdR](https://www.deutsche-rentenversicherung.de)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)
- [GKV-Spitzenverband Beitragsbemessung](https://www.gkv-spitzenverband.de)

## 2. `kv-022-satzungsleistungen-bonusprogramm-und-rueckforderung`

**Fokus:** Freiwillige Kassenleistungen (Satzungsleistungen, §§ 11 und 194 SGB V), Bonusprogramme und Rückforderungsansprüche der Kasse.

# Satzungsleistungen, Bonusprogramm und Rückforderung

## Skill-Zweck

Krankenkassen können freiwillige Leistungen anbieten, die über den gesetzlichen Pflichtleistungskatalog hinausgehen. Dieser Skill klärt **Anspruch auf Satzungsleistungen, Bonusprogramme** und die Grenzen von Rückforderungen.

## Rechtlicher Rahmen

- **§ 11 Abs. 6 SGB V** – Satzungsleistungen (Ermächtigungsnorm)
- **§ 194 SGB V** – Satzungsinhalt
- **§ 65a SGB V** – Bonusprogramme für gesundheitsbewusstes Verhalten
- **§ 20 SGB V** – Prävention und Gesundheitsförderung
- **§ 53 SGB V** – Wahltarife (Überschneidung mit Satzungsleistungen)
- **§ 26a SGB V** – Zusätzliche Leistungen für Schwangere
- SGB X §§ 44, 45, 48 – Rücknahme und Rückforderung von Verwaltungsakten
- BSG B 1 KR 15/19 R (Satzungsleistungen und Gleichbehandlung)

## Satzungsleistungs-Typen

| Leistungstyp | Beispiele | Rechtsgrundlage |
|-------------|-----------|-----------------|
| Individuelle Gesundheitsleistungen | Akupunktur, Homöopathie (umstritten), Sportcheck | § 11 Abs. 6 SGB V |
| Schutzimpfungen über STIKO | Reiseimpfungen, nicht STIKO-empfohlen | Kassenindividuell |
| Kurleistungen | Gesundheitsreisen, Wellnessangebote | § 23 SGB V i.V.m. Satzung |
| Bonusprogramm | Prämien für Vorsorge, Sport, gesunde Ernährung | § 65a SGB V |

## Prüfprogramm

### Schritt 1 – Satzungsleistung prüfen
- Liegt eine Leistung vor, die in der Kassenssatzung steht?
- Satzung auf Website der Kasse einsehen; aktueller Stand?
- Unterschied: Pflichtleistung (kein Ermessen) vs. Satzungsleistung (Ermessen der Kasse)
- Wenn Kasse Satzungsleistung gewährt, ist Gleichbehandlung aller Versicherten geboten

### Schritt 2 – Bonusprogramm (§ 65a SGB V)
- Registrierung beim Programm erforderlich?
- Bedingungen erfüllt? (Anzahl Vorsorgeuntersuchungen, Sportaktivitäten, etc.)
- Auszahlung: Geldprämie oder Beitragsrückerstattung
- Bonusprogramme und Beitragsrückgewähr dürfen nicht auf Leistungseinschränkungen hinauslaufen

### Schritt 3 – Rückforderung durch Kasse
- Kasse fordert gewährte Satzungsleistung zurück?
- Rechtsgrundlage: § 45 SGB X (Rücknahme begünstigender VA)
- Vertrauensschutz: Versicherter hat Mittel bereits ausgegeben → kein Rückforderungsanspruch
- Frist: 2 Jahre nach Kenntnis (§ 45 Abs. 4 SGB X)

### Schritt 4 – Gleichbehandlungsgrundsatz
- Kasse muss Satzungsleistungen allen Versicherten gleich anbieten
- Keine Zwei-Klassen-Versorgung innerhalb GKV
- BSG: Satzungsleistung muss auf objektiven Kriterien basieren, keine willkürliche Ablehnung

### Schritt 5 – Streit um Bonusprogramm-Zahlung
- Voraussetzungen erfüllt, aber Auszahlung verweigert?
- Widerspruch: Nachweis der Teilnahme und erfüllten Bedingungen
- Verjährung: 4 Jahre (SGB X i.V.m. allgemeinem Verjährungsrecht)

## Typische Fallen

- **Satzungsleistung gestrichen**: Kasse kann Satzung für zukünftige Zeiträume ändern; keine rückwirkende Streichung bei laufender Leistung.
- **Bonusprogramm und Datenschutz**: Gesundheitsdaten für Bonusprogramm verarbeitet; DSGVO beachten, Einwilligung erforderlich.
- **Homöopathie-Leistungen**: Streitig ob Satzungsleistung zulässig (keine nachgewiesene Wirksamkeit); G-BA-Beschlüsse beachten.
- **Fitnessstudio-Zuschuss**: Häufig Satzungsleistung; maximale Höhe begrenzt; steuerliche Behandlung klären.

## Output-Formate

- Antrag auf Satzungsleistung
- Bonusprogramm-Nachweis-Übersicht
- Widerspruch gegen Rückforderungsbescheid
- Gleichbehandlungs-Beschwerde
- Satzungsänderungs-Überprüfungsantrag

## Quellen

- [§ 11 SGB V – Satzungsleistungen](https://www.gesetze-im-internet.de/sgb_5/__11.html)
- [§ 65a SGB V – Bonusprogramm](https://www.gesetze-im-internet.de/sgb_5/__65a.html)
- [§ 45 SGB X – Rücknahme](https://www.gesetze-im-internet.de/sgb_10/__45.html)
- [BSG Satzungsleistungen](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 65a SGB V](https://dejure.org/gesetze/SGB_V/65a.html)
- [GKV-Spitzenverband Satzungsleistungen](https://www.gkv-spitzenverband.de)

## 3. `kv-023-md-gutachten-angreifen-befundbericht-und-gegengutachten`

**Fokus:** Strategie zur Anfechtung von MDK/MD-Gutachten: Akteneinsicht, Qualitätsprüfung, Gegengutachten, prozessuale Sachverständigenfragen.

# MD-Gutachten angreifen: Befundbericht und Gegengutachten

## Skill-Zweck

Ablehnungsbescheide der Krankenkasse stützen sich meist auf ein Gutachten des Medizinischen Dienstes (MD). Dieser Skill entwickelt eine **systematische Strategie zur Anfechtung von MD-Gutachten**: Formelle Mängel, inhaltliche Schwächen, Gegengutachten und prozessuale Verwertbarkeit.

## Rechtlicher Rahmen

- **§ 275 SGB V** – MDK-Begutachtung: Voraussetzungen, Fristen, Verfahren
- **§ 275c SGB V** – Prüfverfahren stationäre Behandlung
- **§ 275d SGB V** – Strukturprüfungen Krankenhaus
- **§ 25 SGB X** – Akteneinsicht: Versicherter hat Recht auf Einsicht in MDK-Gutachten
- **§ 2 Abs. 2 SGB V** – Qualitätsvorbehalt: Leistungen müssen dem Stand der Wissenschaft entsprechen
- **SGG §§ 118–122** – Beweis durch Sachverständige im Sozialgerichtsverfahren
- BSG B 1 KR 29/13 R (MD-Gutachten und Beweislast), BSG B 1 KR 22/17 R (Akteneinsicht MD)

## MD-Gutachten-Qualitätsprüfung

| Prüfkriterium | Typische Mängel |
|--------------|-----------------|
| Qualifikation Gutachter | Fachfremd, keine klinische Erfahrung |
| Untersuchung | Fernbegutachtung ohne persönliche Untersuchung |
| Dokumentation | Selektive Quellenauswertung, fehlende Stellungnahme zu Arztberichten |
| Methode | Keine Auseinandersetzung mit aktuellen Leitlinien |
| Schlussfolgerung | Keine schlüssige Begründung, Zirkelschluss |

## Prüfprogramm

### Schritt 1 – Akteneinsicht beantragen (§ 25 SGB X)
- Antrag bei Kasse: Vollständige Akte einschließlich MD-Gutachten, Auftragsdokumentation
- Kasse muss innerhalb angemessener Frist (2–4 Wochen) Einsicht gewähren
- Kopien der Unterlagen anfordern (gegen Kostenerstattung)
- Besonders wichtig: Auftragsinhalt, Fragestellung an MD, vollständiges Gutachten

### Schritt 2 – Formelle Mängel des Gutachtens
- Zugelassener Arzt oder sonstiger Gutachter? (§ 275 Abs. 4 SGB V: nur Ärzte)
- Facharztstandard: Muss Gutachter Facharzt der betreffenden Disziplin sein?
- Gutachten ohne persönliche Untersuchung: nur zulässig wenn aus Unterlagen ausreichend (BSG-Maßstab)
- Fristen: Gutachtenauftrag zu spät erteilt? (§ 275c Abs. 1: 6-Monats-Frist Krankenhaus)

### Schritt 3 – Inhaltliche Angriffspunkte
- Medizinischer Standard nicht beachtet: aktuelle Leitlinien, S3-Empfehlungen
- Behandelnder Arzt-Berichte ignoriert oder falsch wiedergegeben
- Beweislast-Umkehr: wenn Gutachter keine Begründung liefert
- Eigene Recherche: PubMed, Cochrane, Leitlinien-Datenbank (AWMF)

### Schritt 4 – Gegengutachten organisieren
- Behandelnder Arzt: Stellungnahme zu MD-Gutachten anfordern
- Facharzt/Spezialist: explizite Widerlegung des MD-Gutachtens
- Inhalt Gegengutachten: Diagnose bestätigen, medizinische Notwendigkeit belegen, Leitlinien zitieren
- Privatgutachter: BSG erkennt privatärztliche Gutachten als Beweis an (wenn substantiiert)

### Schritt 5 – Sozialgericht: Sachverständige beantragen
- Klage eingereicht → Gericht bestellt Sachverständigen (§ 118 SGG i.V.m. ZPO)
- Ablehnung/Befangenheit des SV: sofort rügen
- Aktuelle Leitlinien dem SV vorlegen
- Recht auf Fragen an SV (§ 118 SGG): Ergänzungsfragen stellen

## Typische Fallen

- **MD-Gutachten als bloße Beratungsleistung**: Kasse ist nicht an MD-Empfehlung gebunden; Bescheid muss eigene Prüfung enthalten.
- **Akteneinsicht verweigert**: Klage auf Akteneinsicht gesondert (Untätigkeitsklage); wichtig für Widerspruchsbegründung.
- **Kein Anspruch auf bestimmten Gutachter**: Kasse wählt MD; aber Gegengutachten des eigenen Arztes gleichwertig.
- **Fernbegutachtung in der Coronazeit**: Rechtsprechung hat Anforderungen gelockert; aber aktuell wieder persönliche Untersuchung als Regel.

## Output-Formate

- Akteneinsichtsantrag (Muster)
- Gutachten-Checkliste (formelle und materielle Mängel)
- Widerspruchsbegründung mit Gegengutachten
- Sachverständigenanfrage-Schreiben (SG)
- Ergänzungsfragen an Gerichtssachverständigen

## Quellen

- [§ 275 SGB V – MD-Begutachtung](https://www.gesetze-im-internet.de/sgb_5/__275.html)
- [§ 25 SGB X – Akteneinsicht](https://www.gesetze-im-internet.de/sgb_10/__25.html)
- [§ 118 SGG – Sachverständige](https://www.gesetze-im-internet.de/sgg/__118.html)
- [BSG B 1 KR 29/13 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [AWMF Leitliniendatenbank](https://www.awmf.org/leitlinien.html)
- [dejure.org § 275 SGB V](https://dejure.org/gesetze/SGB_V/275.html)
