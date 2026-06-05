---
name: krankenversicherung-statuswechsel-arbeitnehmer-selbststaendiger
description: "Statuswechsel Arbeitnehmer Selbststaendiger: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Statuswechsel Arbeitnehmer Selbststaendiger

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Statuswechsel Arbeitnehmer Selbststaendiger** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-003-statuswechsel-arbeitnehmer-selbststaendiger-student-rentn` | Krankenversicherungsrechtliche Folgen beim Wechsel des Erwerbsstatus – Fristen, Beitragsanpassungen, Kassenpflichten. |
| `kv-004-beitragsschuld-saeumniszuschlag-und-ruhen-der-leistung` | Beitragsrückstände in der GKV und PKV: Säumniszuschläge, Leistungsruhen, Schuldenbereinigung und Wiederherstellung des Versicherungsschutzes. |
| `kv-006-hilfsmittel-rollstuhl-hoergeraet-cpap-und-wirtschaftlichk` | Hilfsmittelanspruch nach § 33 SGB V: Hilfsmittelverzeichnis, Wirtschaftlichkeitsgebot, Mehrkostenerklärung, MDK-Gutachten und Widerspruch. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Statuswechsel Arbeitnehmer Selbststaendiger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-003-statuswechsel-arbeitnehmer-selbststaendiger-student-rentn`

**Fokus:** Krankenversicherungsrechtliche Folgen beim Wechsel des Erwerbsstatus – Fristen, Beitragsanpassungen, Kassenpflichten.

# Statuswechsel: Arbeitnehmer, Selbstständiger, Student, Rentner

## Skill-Zweck

Jeder Wechsel des Erwerbsstatus hat unmittelbare krankenversicherungsrechtliche Konsequenzen. Dieser Skill analysiert den **Übergang zwischen Versicherungsstatus** und sichert Fristen, Beiträge und Lückenfreiheit der Absicherung.

## Rechtlicher Rahmen

- **§ 5 SGB V** – Pflichtversicherungstatbestände (Arbeitnehmer, Rentner, ALG-Bezieher, Studenten)
- **§ 6 SGB V** – Versicherungsfreiheit bei JAEG-Überschreitung, Beamten, Selbstständigen
- **§ 9 SGB V** – Freiwillige Weiterversicherung nach Statuswechsel (3-Monats-Frist)
- **§ 188 SGB V** – Beginn der Mitgliedschaft
- **§ 190 SGB V** – Ende der Mitgliedschaft
- **§ 192 SGB V** – Erhaltung der Mitgliedschaft (Krankengeldanspruch)
- **§ 240 SGB V** – Mindestbeitrag freiwillig Versicherter
- **§ 5 Abs. 1 Nr. 9 SGB V** – Studentische Krankenversicherung (bis 25/14. Fachsemester)
- BSG B 12 KR 5/13 R (Statuswechsel Selbstständige)

## Statuswechsel-Matrix

| Von → Nach | Frist | Rechtsgrundlage | Beitragsänderung |
|------------|-------|-----------------|------------------|
| AN → Selbstständig | 3 Monate für freiw. KV | § 9 Abs. 2 Nr. 1 | Mindestbeitrag § 240, Einkommensnachweise |
| AN → Rentner | Automatisch KVdR-Prüfung | § 5 Abs. 1 Nr. 11 | Aus Rente + Versorgungsbezügen |
| Student → AN | Ende Studentenversicherung mit Exmatrikulation | § 190 Abs. 9 | Vollbeitrag AN |
| AN → Elternzeit | Beitragsfreiheit bei keinem Einkommen | § 224 SGB V | Ggf. Beitragsfreiheit |
| PKV → GKV | Nur bei Unterschreiten JAEG oder Statuswechsel | § 5 SGB V | Neubeginn Pflichtmitgliedschaft |

## Prüfprogramm

### Schritt 1 – Statusänderung datieren
- Wann genau ändert sich der Erwerbsstatus (Datum des Aufhebungsvertrags, Rentenbescheid, Exmatrikulationsbescheinigung)?
- Nahtlosigkeit prüfen: Gibt es einen Tag ohne KV-Schutz?

### Schritt 2 – Pflichtversicherung im neuen Status
- Begründet der neue Status eine Pflichtversicherung (z.B. Rentner → KVdR wenn Vorversicherungszeit erfüllt, § 5 Abs. 1 Nr. 11)?
- Vorversicherungszeit KVdR: In der zweiten Hälfte des Erwerbslebens mind. 9/10 der Zeit GKV-versichert

### Schritt 3 – Freiwillige Versicherung wenn keine Pflicht
- 3-Monats-Frist ab Ende der Pflichtversicherung beachten (§ 9 Abs. 2 Nr. 1 SGB V)
- Bei Selbstständigkeit: Einkommen schätzen, Mindestbeitrag planen, Spitzabrechnung vormerken
- Nachweis: Steuerbescheid des Vorjahres, bei Neugründung Geschäftsplan

### Schritt 4 – Rentner-Sonderfall KVdR
- Vorversicherungszeit: Rentenversicherungszeiten werden anteilig angerechnet
- Versorgungsbezüge: Betriebsrenten, Direktversicherungen beitragspflichtig (§ 229 SGB V)
- Beitragssatz: allgemeiner Beitragssatz ohne AG-Anteil aus Versorgungsbezügen

### Schritt 5 – Studentische KV
- Grenze: 25 Jahre oder 14. Fachsemester (§ 5 Abs. 1 Nr. 9 SGB V)
- Urlaubssemester zählen mit; Krankengeldbezug verlängert nicht
- Nach Exmatrikulation: 3-Monats-Frist für freiwillige Versicherung

## Typische Fallen

- **KVdR-Vorversicherungszeit**: Wird oft übersehen; ohne sie kein Pflichtversicherungsstatus als Rentner → teurer freiwilliger Beitrag.
- **Selbstständige Nebentätigkeit neben AN**: Kann bei ausreichendem Einkommen Hauptberuflichkeit begründen und Versicherungsfreiheit auslösen (§ 5 Abs. 5 SGB V).
- **Elternzeit-Falle**: Kein Krankengeldanspruch wenn kein Beschäftigungsverhältnis besteht → Mitgliedschaftserhaltung prüfen (§ 192 Abs. 1 Nr. 2).
- **Beitragsschuldübergang**: Bei Ende der Mitgliedschaft bestehende Schulden laufen weiter; Insolvenz der KK schützt nicht.

## Output-Formate

- Statuswechsel-Checkliste mit Fristen
- Beitragsvergleich alt/neu
- Antrag freiwillige Versicherung (Mustertext)
- KVdR-Vorversicherungszeitberechnung
- Bescheidwiderspruch bei falscher Statusfeststellung

## Quellen

- [§ 5 SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 9 SGB V](https://www.gesetze-im-internet.de/sgb_5/__9.html)
- [§ 190 SGB V](https://www.gesetze-im-internet.de/sgb_5/__190.html)
- [§ 229 SGB V – Versorgungsbezüge](https://www.gesetze-im-internet.de/sgb_5/__229.html)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)
- [BSG Entscheidungssuche](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)

## 2. `kv-004-beitragsschuld-saeumniszuschlag-und-ruhen-der-leistung`

**Fokus:** Beitragsrückstände in der GKV und PKV: Säumniszuschläge, Leistungsruhen, Schuldenbereinigung und Wiederherstellung des Versicherungsschutzes.

# Beitragsschuld, Säumniszuschlag und Ruhen der Leistung

## Skill-Zweck

Beitragsrückstände können den Versicherungsschutz suspendieren. Dieser Skill analysiert **Beitragsschulden**, berechnet Säumniszuschläge, klärt die Voraussetzungen des Leistungsruhens und entwickelt eine Strategie zur Wiederherstellung des vollen Versicherungsschutzes.

## Rechtlicher Rahmen

- **§ 16 Abs. 3a SGB V** – Ruhen der Leistungsansprüche bei Beitragsrückstand > 2 Monatsbeiträge (freiwillig Versicherte)
- **§ 24 SGB IV** – Säumniszuschlag: 1 % des rückständigen Betrags je angefangenen Monat
- **§ 26 SGB IV** – Erstattung zu Unrecht entrichteter Beiträge
- **§ 256a SGB V** – Beitragsrückstände und Stundung
- **§ 193 Abs. 6–9 VVG** – Leistungssuspendierung PKV, Notlagentarif
- **§ 12h VAG** – PKV-Notlagentarif
- BSG B 12 KR 26/09 R (Ruhen der Leistung verfassungskonform)
- BVerfG 1 BvR 347/98 (Grundrecht auf Leben und körperliche Unversehrtheit bei Leistungsruhen)

## Berechnungslogik Säumniszuschlag

| Parameter | Wert |
|-----------|------|
| Säumniszuschlag | 1 % pro angefangenen Monat (§ 24 SGB IV) |
| Mindestbetrag | 50 € Schuld erforderlich |
| Fälligkeit | Beitrag am drittletzten Bankarbeitstag des Monats |
| Verjährung | 4 Jahre ab Ende des Kalenderjahrs (§ 25 SGB IV) |
| Stundungsmöglichkeit | § 76 SGB IV, besondere Härtegründe |

## Prüfprogramm

### Schritt 1 – Höhe der Beitragsschuld ermitteln
- Kontoauszug der Kasse anfordern (§ 25 SGB X: Akteneinsicht)
- Hauptforderung, Säumniszuschläge und Mahnkosten trennen
- Verjährte Forderungen identifizieren (§ 25 SGB IV: 4 Jahre)

### Schritt 2 – Ruhenstatbestand GKV (§ 16 Abs. 3a SGB V)
- Gilt nur für freiwillig Versicherte
- Rückstand > 2 Monatsbeiträge (Bruttobeitrag)
- Während Ruhen: nur Behandlung bei akuten Erkrankungen und Schmerzen, Schwangerschaft und Mutterschaft
- Wiederherstellung: vollständige Zahlung oder verbindliche Ratenzahlungsvereinbarung

### Schritt 3 – PKV-Leistungssuspendierung (§ 193 VVG)
- Voraussetzung: Beitragsrückstand > 1 Monat nach 2. Mahnung
- Übergang in Notlagentarif automatisch bei Rückstand > 2 Monate
- Notlagentarif: nur Akutbehandlung, Schmerzen, Schwangerschaft
- Rückkehr: Begleichung aller Rückstände inkl. Notlagentarifbeiträge

### Schritt 4 – Schuldenbereinigungsstrategie
- Verhandlung mit Kasse: Stundung (§ 76 SGB IV), Ratenzahlung, Erlass des Säumniszuschlags bei unbilliger Härte
- Insolvenzverfahren: Beitragsschulden sind insolvenzfeste Forderungen; besondere Prüfung nötig
- Jobcenter-Übernahme: § 26 SGB II (Leistungsberechtigte), § 32 SGB XII (Sozialhilfe)

## Typische Fallen

- **Pflichtversicherte**: § 16 Abs. 3a SGB V gilt nicht für Pflichtmitglieder; bei diesen gibt es kein Leistungsruhen wegen Beitragsrückstand.
- **Mindestbehandlung im Ruhen**: Kasse muss trotz Ruhen akute Behandlung finanzieren; Arzt darf nicht ablehnen.
- **Säumniszuschlag-Verjährung**: Die 4-Jahres-Frist beginnt mit dem Ende des Jahres, in dem der Zuschlag entstanden ist – nicht ab Hauptschuld.
- **PKV-Notlagentarif-Falle**: Beiträge im Notlagentarif laufen weiter und summieren sich; Schulden wachsen, auch wenn Leistungen nicht in Anspruch genommen werden.

## Output-Formate

- Schuldenaufstellung mit Verjährungsprüfung
- Stundungsantrag (Mustertext)
- Ratenzahlungsvereinbarung
- Widerspruch gegen Festsetzungsbescheid (Höhe Säumniszuschlag)
- PKV-Wiederherstellungsschreiben

## Quellen

- [§ 16 SGB V – Ruhen](https://www.gesetze-im-internet.de/sgb_5/__16.html)
- [§ 24 SGB IV – Säumniszuschlag](https://www.gesetze-im-internet.de/sgb_4/__24.html)
- [§ 193 VVG – PKV-Beitragsverzug](https://www.gesetze-im-internet.de/vvg_2008/__193.html)
- [§ 76 SGB IV – Stundung](https://www.gesetze-im-internet.de/sgb_4/__76.html)
- [BVerfG 1 BvR 347/98](https://www.bverfg.de/e/rs19990109_1bvr034798.html)
- [dejure.org SGB V § 16](https://dejure.org/gesetze/SGB_V/16.html)
## Hinweis: Insolvenz und Beitragsschuld

- Bei Insolvenz des Versicherten: Beitragsschuld ist Insolvenzforderung
- Krankenkasse meldet Forderung zur Insolvenztabelle an (§ 174 InsO)
- Nach Restschuldbefreiung: Beitragsforderungen aus der Zeit vor Insolvenz erlöschen
- Pflichtversicherung bleibt bestehen; neue Beiträge laufen weiter

## Weiterführende Quellen

- [§ 24 SGB IV – Säumniszuschlag](https://www.gesetze-im-internet.de/sgb_4/__24.html)
- [§ 16 SGB V – Ruhen der Leistung](https://www.gesetze-im-internet.de/sgb_5/__16.html)
- [§ 256a SGB V – Beiträge aus Versorgungsbezügen](https://www.gesetze-im-internet.de/sgb_5/__256a.html)

## 3. `kv-006-hilfsmittel-rollstuhl-hoergeraet-cpap-und-wirtschaftlichk`

**Fokus:** Hilfsmittelanspruch nach § 33 SGB V: Hilfsmittelverzeichnis, Wirtschaftlichkeitsgebot, Mehrkostenerklärung, MDK-Gutachten und Widerspruch.

# Hilfsmittel: Rollstuhl, Hörgerät, CPAP und Wirtschaftlichkeit

## Skill-Zweck

Dieser Skill bearbeitet **Hilfsmittelversorgung** in der GKV: vom Antrag bis zur Ablehnung, von der Mehrkostenregelung bis zum Eilantrag. Schwerpunkte sind Rollstuhl, Hörgerät, CPAP/Beatmungsgeräte, Inkontinenzversorgung und orthetische Versorgung.

## Rechtlicher Rahmen

- **§ 33 SGB V** – Hilfsmittelanspruch: Behinderungsausgleich, Sicherung des Behandlungserfolgs
- **§ 12 SGB V** – Wirtschaftlichkeitsgebot: notwendig, ausreichend, zweckmäßig, wirtschaftlich
- **§ 36 SGB V** – Festbeträge für Hilfsmittel (GKV-Spitzenverband)
- **§ 139 SGB V** – Hilfsmittelverzeichnis des GKV-Spitzenverbands
- **§ 275 SGB V** – MDK-Begutachtung
- Hilfsmittel-Richtlinie (HiMi-RL) des G-BA
- BSG B 3 KR 5/15 R (Rollstuhl, Behinderungsausgleich), BSG B 3 KR 14/13 R (CPAP)
- BSG B 3 KR 21/14 R (Hörgerät, Festbetrag und Mehrkostenpflicht)

## Behinderungsausgleich vs. Behandlungssicherung

| Typ | Beispiele | Prüfmaßstab |
|-----|-----------|-------------|
| Unmittelbarer Behinderungsausgleich | Rollstuhl, Hörgerät | Vollständiger Ausgleich angestrebt (BSG) |
| Mittelbarer Behinderungsausgleich | Pflegehilfsmittel | Grundbedürfnis Mobilität, Kommunikation, Pflege |
| Behandlungssicherung | CPAP, Insulinpumpe | Medizinische Notwendigkeit, Leitlinien |

## Prüfprogramm

### Schritt 1 – Anspruchsgrundlage § 33 SGB V
- Hilfsmittel im Verzeichnis (§ 139 SGB V)? → GKV-Spitzenverband-Datenbank prüfen
- Nicht im Verzeichnis: Einzelfallentscheidung möglich (§ 33 Abs. 1 Satz 1 Alt. 2 SGB V)
- Ziel: Behinderungsausgleich oder Sicherung des Behandlungserfolgs?

### Schritt 2 – Wirtschaftlichkeit und Festbetrag
- Festbetrag nach § 36 SGB V: Kasse zahlt bis Festbetrag; Mehrkosten trägt Versicherter
- Mehrkostenerklärung: Versicherter kann wirtschaftlicheres Gerät ablehnen, zahlt dann Differenz
- Ausnahme: Aus medizinischen Gründen ist wirtschaftlicheres Gerät nicht ausreichend → vollständige Kassenleistung

### Schritt 3 – MDK-Prüfung angreifen (§ 275 SGB V)
- MDK-Gutachten ist keine bindende Entscheidung, sondern Beratungsleistung für Kasse
- Gegengutachten: behandelnder Arzt, Rehamediziner, Orthopädie-Techniker
- Akteneinsicht: MDK-Gutachten einsehen (§ 25 SGB X)
- Formelle Fehler: Qualifikation des Gutachters, keine Untersuchung des Versicherten

### Schritt 4 – Fallspezifische Besonderheiten
**Rollstuhl**:
- Grundversorgung (einfacher Rollstuhl) vs. Spezialversorgung (Elektrorollstuhl, Aktivrollstuhl)
- Aktivrollstuhl: BSG fordert individuelle medizinische Prüfung der Notwendigkeit
- Schnittstelle Pflegeversicherung: § 40 SGB XI (Pflegehilfsmittel)

**Hörgerät**:
- Festbetrag 2024: 784,94 € je Ohr (GKV-Spitzenverband)
- Medizinische Mehrkostenpflicht: bei spezifischen Anforderungen (Beruf, Tinnitus) prüfen

**CPAP / Beatmung**:
- § 33 Abs. 1 Satz 1 Alt. 2: Sicherung des Behandlungserfolgs (Schlafapnoe)
- Compliance-Nachweis: Gerät muss regelmäßig genutzt werden (Kasse kann Nachweise fordern)

## Typische Fallen

- **Kostenvorbehalt missachtet**: Versicherter beschafft Hilfsmittel selbst, ohne Kostenerstattungsverfahren (§ 13 Abs. 3 SGB V) – Kasse kann ablehnen.
- **Festbetrag als Nullleistung missverstanden**: Kasse muss mindestens ein funktionsfähiges Gerät zum Festbetrag liefern; nur wenn keines verfügbar ist, trägt Versicherter Mehrkosten.
- **Hilfsmittelpflege**: Wartung und Reparatur sind Kassenleistung (§ 33 Abs. 1 Satz 4 SGB V).

## Output-Formate

- Antragsschreiben mit medizinischer Begründung
- Widerspruch gegen MDK-gestützte Ablehnung
- Gegengutachten-Briefing für Arzt
- Mehrkostenanalyse (Tabelle)
- Eilantrag Sozialgericht (§ 86b SGG)

## Quellen

- [§ 33 SGB V – Hilfsmittel](https://www.gesetze-im-internet.de/sgb_5/__33.html)
- [Hilfsmittelverzeichnis GKV-Spitzenverband](https://hilfsmittel.gkv-spitzenverband.de)
- [Hilfsmittel-Richtlinie G-BA](https://www.g-ba.de/richtlinien/13/)
- [BSG Entscheidungssuche](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 33 SGB V](https://dejure.org/gesetze/SGB_V/33.html)
- [§ 139 SGB V – Hilfsmittelverzeichnis](https://www.gesetze-im-internet.de/sgb_5/__139.html)
