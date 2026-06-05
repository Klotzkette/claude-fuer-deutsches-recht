---
name: krankenversicherung-nichtversicherte-auffangpflichtversicherung
description: "Nichtversicherte Auffangpflichtversicherung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nichtversicherte Auffangpflichtversicherung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Nichtversicherte Auffangpflichtversicherung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-077-nichtversicherte-auffangpflichtversicherung` | Krankenversicherungsschutz für Personen ohne anderweitigen KV-Schutz: Auffangpflichtversicherung nach § 5 Abs. 1 Nr. 13 SGB V, Beiträge und Schuldenproblematik. |
| `kv-078-krankenkasse-und-insolvenz-beitragsschuld` | Beitragsschulden gegenüber GKV und PKV in der Insolvenz: Insolvenzforderungen, Masseverbindlichkeiten, Restschuldbefreiung und Verhalten der Kasse. |
| `kv-079-elektronische-patientenakte-zugriffsrechte` | ePA nach § 341 SGB V: Zugriffsrechte der Versicherten und Leistungserbringer, Datenschutzkontrolle, opt-out-Regelung und Pflichten der Kassen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Nichtversicherte Auffangpflichtversicherung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-077-nichtversicherte-auffangpflichtversicherung`

**Fokus:** Krankenversicherungsschutz für Personen ohne anderweitigen KV-Schutz: Auffangpflichtversicherung nach § 5 Abs. 1 Nr. 13 SGB V, Beiträge und Schuldenproblematik.

# Nichtversicherte: Auffangpflichtversicherung

## Skill-Zweck

Wer zuletzt gesetzlich versichert war und keinen anderen KV-Schutz hat, wird über die Auffangpflichtversicherung in die GKV aufgenommen. Dieser Skill klärt **Voraussetzungen, Beiträge, Beitragsschulden und Wege aus der Nichtversicherung**.

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 13 SGB V** – Auffangpflichtversicherung (zuletzt GKV-versichert)
- **§ 5 Abs. 1 Nr. 13 lit. b SGB V** – Personen ohne anderweitige KV-Pflicht
- **§ 188 Abs. 4 SGB V** – Beginn der Mitgliedschaft (automatisch)
- **§ 16 Abs. 3a SGB V** – Leistungsruhen bei Beitragsrückstand
- **§ 193 Abs. 3–5 VVG** – Auffangversicherungspflicht PKV (zuletzt privat versichert)
- BSG B 12 KR 14/07 R (Auffangpflichtversicherung, Rückwirkung)

## Auffangversicherungs-Logik

| Ausgangslage | Zuständige Auffangversicherung |
|-------------|-------------------------------|
| Zuletzt GKV-versichert | § 5 Abs. 1 Nr. 13 SGB V (GKV) |
| Zuletzt PKV-versichert | PKV-Auffangpflicht (§ 193 Abs. 3–5 VVG, Basistarif) |
| Nie versichert (und in D. wohnhaft) | § 5 Abs. 1 Nr. 13 lit. b SGB V (GKV) |
| Zuletzt im Ausland versichert | Koordinierungsrecht prüfen |

## Prüfprogramm

### Schritt 1 – Auffangpflichtversicherung GKV
- Wer war zuletzt gesetzlich versichert und hat jetzt keinen anderen Schutz?
- Automatische Versicherungspflicht bei zuletzt GKV-versicherter Person: § 5 Abs. 1 Nr. 13
- Keine Anmeldefrist wie bei freiwilliger Versicherung; rückwirkender Beginn möglich
- Letzte Kasse wird zuständig (§ 173 Abs. 5 SGB V)

### Schritt 2 – Beitragsschulden bei Nichtversicherung
- Rückwirkende Pflichtversicherung ab Datum des Verlusts anderweitigen Schutzes
- Kasse fordert rückwirkend Beiträge: Säumniszuschläge entstehen
- Stundung, Ratenzahlung: beantragen; Kasse hat Ermessen (§ 76 SGB IV)

### Schritt 3 – Leistungsruhen und Akutversorgung
- Beitragsrückstand > 2 Monate: Leistungsruhen (§ 16 Abs. 3a SGB V)
- Aber: akute Erkrankungen und Schmerzbehandlung bleiben zugänglich
- Schwangerschaft: immer vollständiger Leistungsanspruch trotz Rückstand

### Schritt 4 – PKV-Auffangpflicht
- Zuletzt PKV-versichert und jetzt ohne Schutz: PKV muss in Basistarif aufnehmen (§ 193 Abs. 5 VVG)
- Keine Risikoprüfung im Basistarif
- Beitrag: max. allgemeiner GKV-Beitragssatz * BBG

### Schritt 5 – Weg aus der Nichtversicherung
- GKV anmelden; letzte Kasse kontaktieren
- Schulden bezahlen oder Ratenzahlung vereinbaren
- Sozialamt kann Beiträge übernehmen (§ 32 SGB XII, § 26 SGB II)
- Krankenbehandlung für Nichtversicherte: stille Schulden → medizinische Behandlung in Not (§ 264 Abs. 2 SGB V)

## Typische Fallen

- **Rückwirkende Beitragsschulden**: Kasse berechnet Beiträge für Jahre der Nichtversicherung → erhebliche Schulden.
- **Unbekannte Versicherungslücke**: Person weiß nicht dass sie nicht versichert ist; oft durch Jobverlust ohne Bürgergeld-Antrag.
- **PKV und GKV-Auffang**: Klären wer zuletzt versichert war; falsche Kasse = erneuter Wechsel notwendig.
- **Kinder nicht mitangemeldet**: Kinder ohne eigene Versicherung; Familienversicherung beantragen.

## Output-Formate

- Anmeldung bei letzter GKV (Muster)
- Stundungsantrag Beitragsrückstand
- Sozialamt-Übernahmeantrag
- Schuldenbereinigungsplan
- Leistungsruhen-Informationsblatt

## Quellen

- [§ 5 Abs. 1 Nr. 13 SGB V – Auffangpflicht](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 16 Abs. 3a SGB V – Leistungsruhen](https://www.gesetze-im-internet.de/sgb_5/__16.html)
- [§ 193 VVG – PKV-Auffangpflicht](https://www.gesetze-im-internet.de/vvg_2008/__193.html)
- [§ 76 SGB IV – Stundung](https://www.gesetze-im-internet.de/sgb_4/__76.html)
- [BSG B 12 KR 14/07 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)

## 2. `kv-078-krankenkasse-und-insolvenz-beitragsschuld`

**Fokus:** Beitragsschulden gegenüber GKV und PKV in der Insolvenz: Insolvenzforderungen, Masseverbindlichkeiten, Restschuldbefreiung und Verhalten der Kasse.

# Krankenkasse und Insolvenz: Beitragsschuld

## Skill-Zweck

Beitragsschulden bei der Krankenversicherung können erheblich sein. In der Insolvenz stellen sich besondere Fragen. Dieser Skill klärt **Rang der Beitragsschulden, Insolvenzverfahren, Restschuldbefreiung und Krankenversicherungsschutz während Insolvenz**.

## Rechtlicher Rahmen

- **§ 38 InsO** – Insolvenzforderungen (vor Insolvenzeröffnung)
- **§ 55 InsO** – Masseverbindlichkeiten (nach Insolvenzeröffnung)
- **§ 286 InsO** – Restschuldbefreiung
- **§ 302 InsO** – Ausnahmen von der Restschuldbefreiung (vorsätzliche unerlaubte Handlungen; gilt für Sozialversicherungsbeiträge? → BSG prüfen)
- **§ 25 SGB IV** – Verjährung Beitragsansprüche (4 Jahre, vorsätzlich: 30 Jahre)
- **§ 24 SGB IV** – Säumniszuschlag
- BSG B 12 KR 26/09 R (Insolvenz und GKV-Beiträge)

## Insolvenzrechtliche Einordnung GKV-Beiträge

| Zeitraum | Insolvenzrechtliche Einordnung |
|----------|-------------------------------|
| Beiträge vor Insolvenzeröffnung | Insolvenzforderungen (§ 38 InsO); quotal befriedigt |
| Beiträge nach Eröffnung (Selbstständiger) | Masseverbindlichkeiten (§ 55 InsO); vorrangig |
| Angestelltenanteil (AG-Pflicht) | Masseforderung wenn nach Eröffnung |

## Prüfprogramm

### Schritt 1 – Beitragsschulden zeitlich einordnen
- Welche Beitragsschulden entstanden vor Insolvenzeröffnung? → Insolvenzforderung
- Welche entstanden nach Eröffnung? → Masseverbindlichkeit oder neue Pflichtmitgliedschaft
- GKV muss Insolvenzforderungen beim Insolvenzverwalter anmelden

### Schritt 2 – Krankenversicherung im Insolvenzverfahren
- Pflichtmitglied bleibt pflichtmitglied; kein Ruhen der Mitgliedschaft
- Freiwillig Versicherter: Beitragsrückstand → Leistungsruhen (§ 16 Abs. 3a SGB V) weiterhin möglich
- Insolvenzverwalter zahlt laufende Beiträge aus Masse (wenn vorhanden)

### Schritt 3 – Restschuldbefreiung
- § 286 InsO: nach 3 Jahren wird Versicherter von Restschulden befreit
- GKV-Beitragsschulden: grundsätzlich von Restschuldbefreiung umfasst
- Ausnahme § 302 InsO: nur bei vorsätzlicher unerlaubter Handlung; strittig ob GKV-Beiträge hierunter fallen
- BSG: keine generelle Ausnahme für Sozialversicherungsbeiträge von Restschuldbefreiung

### Schritt 4 – Verhalten der GKV im Insolvenzverfahren
- GKV kann eigene Versicherungsschutzpflicht während Insolvenz nicht einstellen
- Beitragseinzug: über Insolvenzverwalter für Masseverbindlichkeiten
- Leistungsruhen möglich aber Akutversorgung immer
- Kasse sollte Schuldenbescheid nicht erlassen während laufendem Insolvenzverfahren

### Schritt 5 – Nach Restschuldbefreiung
- Schulden erlöschen mit Restschuldbefreiung
- Neue GKV-Mitgliedschaft auf sauberem Stand
- PKV: Schulden erlöschen ebenfalls; aber Neuvertrag erfordert Risikoprüfung

## Typische Fallen

- **Säumniszuschläge in Insolvenz**: Laufen weiter solange nicht Insolvenzforderung; sorgfältig abgrenzen.
- **Freiwillig Versicherter und Selbstständige**: Beiträge als Masseverbindlichkeit wenn Selbstständigkeit fortgesetzt; erhebliche Priorität für Insolvenzverwalter.
- **GKV kündigt Mitgliedschaft**: Nicht möglich; Pflichtmitgliedschaft kann nicht wegen Insolvenz beendet werden.
- **Strafrecht und Beitragsschulden**: Vorsätzliche Beitragshinterziehung (§ 266a StGB); auch GKV-Beiträge umfasst.

## Output-Formate

- Insolvenzforderungsanmeldung (GKV-intern)
- Restschuldbefreiungsantrag mit GKV-Schuldenübersicht
- Stundungsantrag während Insolvenz
- Masseverbindlichkeits-Berechnung
- Post-Insolvenz GKV-Neustartplanung

## Quellen

- [§ 38 InsO – Insolvenzforderungen](https://www.gesetze-im-internet.de/inso/__38.html)
- [§ 286 InsO – Restschuldbefreiung](https://www.gesetze-im-internet.de/inso/__286.html)
- [§ 25 SGB IV – Verjährung](https://www.gesetze-im-internet.de/sgb_4/__25.html)
- [BSG B 12 KR 26/09 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 286 InsO](https://dejure.org/gesetze/InsO/286.html)
- [§ 302 InsO – Ausnahmen](https://www.gesetze-im-internet.de/inso/__302.html)

## 3. `kv-079-elektronische-patientenakte-zugriffsrechte`

**Fokus:** ePA nach § 341 SGB V: Zugriffsrechte der Versicherten und Leistungserbringer, Datenschutzkontrolle, opt-out-Regelung und Pflichten der Kassen.

# Elektronische Patientenakte: Zugriffsrechte

## Skill-Zweck

Die elektronische Patientenakte (ePA) wird ab 2025 für alle GKV-Versicherten angelegt. Dieser Skill klärt **Zugriffsrechte, Datenschutzkontrolle, opt-out und Pflichten der beteiligten Akteure**.

## Rechtlicher Rahmen

- **§ 341 SGB V** – Elektronische Patientenakte: Inhalt, Zugriffsrechte, Datenschutz
- **§ 342 SGB V** – Nutzung der ePA durch Versicherte und Leistungserbringer
- **§ 344 SGB V** – Datenschutzrechte in der ePA
- **§ 360 SGB V** – eRezept (Schnittstelle ePA)
- **DSGVO Art. 9** – Gesundheitsdaten als besondere Datenkategorie
- **TSGB** (Patientendaten-Schutz-Gesetz 2020) – Grundlage ePA
- BfDI (Bundesdatenschutzbeauftragter): Stellungnahmen zur ePA
- Gematik GmbH: technischer Betreiber der Telematik-Infrastruktur

## ePA-Zugriffsrechte im Überblick

| Akteur | Zugriffsrecht | Beschränkung |
|--------|--------------|--------------|
| Versicherter | Voller Zugriff auf eigene Daten | – |
| Arzt / Zahnarzt | Lesend und schreibend bei Einwilligung | Nur für Behandlung |
| Apotheke | Lesend (Medikationsplan) bei Einwilligung | Zeitlich begrenzt |
| Krankenhaus | Wie Arzt bei stationärer Behandlung | Behandlungszeitraum |
| Krankenkasse | Nur Verwaltungsdaten; KEINE Behandlungsdaten | Strenge Trennung |
| Arbeitgeber | KEIN Zugriff | Absolut verboten |

## Prüfprogramm

### Schritt 1 – opt-out-Erklärung
- Ab 2025: ePA automatisch angelegt
- Widerspruch (opt-out): schriftlich bei der Kasse; begründungslos möglich
- Widerspruch führt zur Nicht-Anlage der ePA; rückwirkende Löschung möglich

### Schritt 2 – Zugriffsrechte verwalten
- Welcher Arzt darf welche Daten sehen?
- App der Kasse oder Kiosk-System: Zugriffsrechte granular einstellen
- Zeitliche Begrenzung: Zugriff nur für Behandlungszeitraum; danach abschalten
- Daten löschen: einzelne Dokumente löschbar; nicht alle (Pflichtdaten wie Medikationsplan)

### Schritt 3 – Sicherheit und Missbrauch
- Datenmissbrauch durch Arzt: strafbar (§ 203 StGB, DSGVO); Beschwerde bei Datenschutzbehörde
- Datenpanne: Gematik und Kasse müssen informieren (DSGVO Art. 34)
- Technische Sicherheit: Ende-zu-Ende-Verschlüsselung; keine Speicherung im Klartext

### Schritt 4 – ePA-Inhalte
- Befunde: ärztliche Dokumente, Laborbefunde, Arztbriefe
- Medikationsplan: alle verordneten Medikamente (Aktualisierung durch Apotheke)
- Mutterpass, Impfpass, Zahnbonusheft: integrierbar
- DiGA-Daten: nur mit separater Einwilligung

### Schritt 5 – Forschungszugang
- Pseudonymisierte Daten für medizinische Forschung: opt-out möglich
- Datentransparenzgesetz: GKV-Daten für Forschungszwecke (pseudonymisiert)
- Opt-out-Erklärung: bei Kasse oder national (Datentransparenz)

## Typische Fallen

- **opt-out und ePA**: Wer widerspricht, verliert auch Vorteile (zentrale Medikationsliste); individuelle Abwägung.
- **Arzt sieht alle Daten**: Nur wenn Versicherter freigibt; Einschränkung möglich auf bestimmte Bereiche.
- **Kasse sieht Behandlungsdaten**: VERBOTEN; nur administrative Daten (Beiträge, Mitgliedschaft); Verstoß meldepflichtig.
- **Vererbung der ePA**: Nach Tod kein automatischer Zugang für Erben; Sonderlösung nötig.

## Output-Formate

- ePA-opt-out-Schreiben
- Zugriffsberechtigungs-Übersicht
- Datenmissbrauch-Beschwerde (BfDI)
- Forschung-opt-out
- ePA-Erklärungsblatt (Laienerklärung)

## Quellen

- [§ 341 SGB V – ePA](https://www.gesetze-im-internet.de/sgb_5/__341.html)
- [§ 344 SGB V – Datenschutzrechte](https://www.gesetze-im-internet.de/sgb_5/__344.html)
- [Gematik ePA](https://www.gematik.de/anwendungen/e-patientenakte/)
- [BfDI ePA-Stellungnahmen](https://www.bfdi.bund.de)
- [DSGVO Art. 9](https://dsgvo-gesetz.de/art-9-dsgvo/)
- [dejure.org § 341 SGB V](https://dejure.org/gesetze/SGB_V/341.html)
