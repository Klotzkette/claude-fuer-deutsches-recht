---
name: arbeitsschutz-betrsichv-robotik
description: "Prüft Arbeitsschutz und Betriebssicherheit bei Robotern im Betrieb: Gefährdungsbeurteilung, Unterweisung, Prüfungen, Betriebsanweisung."
---

# Arbeitsschutz und BetrSichV in der Robotik

## Fachkern: Arbeitsschutz und BetrSichV in der Robotik
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Roboter im betrieblichen Einsatz sind Arbeitsmittel i. S. d. BetrSichV. Den Arbeitgeber treffen Pflichten zur Gefährdungsbeurteilung (§ 3 BetrSichV), zu Schutzmaßnahmen, Unterweisung (§ 12 ArbSchG), wiederkehrenden Prüfungen (§ 14 BetrSichV) und zur Erstellung einer Betriebsanweisung. Bei Cobots, autonomen Transportrobotern (AMR) und Service-Robotern entstehen typische Risiken: Quetschung, Stoß, Sturz nach Kollision, psychische Belastung. Dieser Skill leitet durch die Pflichten und liefert Vorlagen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Arbeitgeber/Betreiber, Sicherheitsfachkraft (Sifa), Sicherheitsbeauftragter, Betriebsrat, Berufsgenossenschaft.
2. **Robotertyp:** Industrieroboter mit Zaun, Cobot ohne Zaun, AMR/AGV mit Personen im Verkehrsraum, Service-Roboter in Mischarbeit.
3. **Anlass:** Erstinbetriebnahme, wesentliche Veränderung, Unfall, Berufsgenossenschafts-Audit, Mitarbeiter-Beschwerde.
4. **Mitbestimmung:** Betriebsrat vorhanden? § 87 Abs. 1 Nr. 6, 7 BetrVG einschlägig.
5. **Unterlagen:** Risikobeurteilung des Herstellers, EU-Konformitätserklärung, Anleitung, vorhandene Gefährdungsbeurteilung, Unterweisungsnachweise, Wartungsplan.

## Rechtlicher Rahmen

- **ArbSchG** §§ 3-7 Grundpflichten Arbeitgeber, §§ 12, 13 Unterweisung.
- **BetrSichV** §§ 3, 4, 5, 6, 12, 14: Gefährdungsbeurteilung, Schutzmaßnahmen, Prüfungen.
- **DGUV Vorschrift 1** "Grundsätze der Prävention"; DGUV Information 209-074 "Industrieroboter".
- **TRBS 1111** Gefährdungsbeurteilung; **TRBS 2111** Mechanische Gefährdungen.
- **MaschinenVO** VO (EU) 2023/1230 (ab 20.01.2027) für Inverkehrbringen; Schnittstelle zur BetrSichV beim Inbetriebnehmen.
- **ISO 10218-1/-2** Industrieroboter; **ISO/TS 15066** Cobot-Druck-/Kraftgrenzwerte.
- **BetrVG** § 87 Abs. 1 Nr. 6 technische Überwachung, Nr. 7 Arbeits- und Gesundheitsschutz.

## Schritt für Schritt

1. **Gefährdungsbeurteilung** spezifisch für den Robotertyp und Arbeitsplatz; Beteiligung von Sifa, Betriebsarzt, Beschäftigten.
2. **Risikobeurteilung des Herstellers** auswerten und auf den konkreten Einsatz übertragen; Restrisiken explizit benennen.
3. **Schutzmaßnahmen** nach STOP-Prinzip: Substitution, Technik (Schutzzaun, Lichtgitter, Geschwindigkeitsreduktion, Power-and-Force-Limiting nach ISO/TS 15066), Organisation, Persönliche Schutzausrüstung.
4. **Cobot-Validierung** mit biomechanischen Druck-/Kraftmessungen; Grenzwerte ISO/TS 15066:2016 Tabelle 5.4.
5. **Betriebsanweisung** in verständlicher Sprache, Sprachen aller Beschäftigten.
6. **Unterweisung** vor Aufnahme und mindestens jährlich; Nachweis.
7. **Wiederkehrende Prüfungen** § 14 BetrSichV; Prüffristen aus Gefährdungsbeurteilung ableiten.
8. **Vorfall** dokumentieren, Berufsgenossenschaft melden (§ 193 SGB VII bei meldepflichtigen Unfällen), Wiederholungsprävention.
9. **Mitbestimmung** § 87 Abs. 1 Nr. 6, 7 BetrVG: Betriebsvereinbarung über Cobot-Einsatz und Mitarbeiterdaten.

## Trade-off-Matrix

| Maßnahme | Pro | Contra | Empfehlung |
|---|---|---|---|
| Schutzzaun | hoher Schutz | Platzverlust, Cobot-Vorteil weg | bei klassischen Industrierobotern Standard |
| Power-and-Force-Limiting | Mensch-Roboter-Kollaboration möglich | Reduzierte Geschwindigkeit, niedrigere Taktzeit | bei echter Kollaboration Standard, Messprotokolle nötig |
| Speed-and-Separation-Monitoring | flexibler | LiDAR/Vision-Aufwand | bei wechselnden Tätigkeiten attraktiv |
| Volle Trennung | maximaler Schutz | keine Kooperation | bei hohen Lasten/Geschwindigkeiten Pflicht |

## Praxistipps

- **Cobot ist kein Pauschalfreibrief**: Auch Cobots benötigen vor Ort eine Validierung; Herstellerangaben sind Voraussetzung, nicht Ersatz.
- **Sprachenfrage**: Betriebsanweisung in jeder Muttersprache der Belegschaft, mindestens deutsch und englisch.
- **Wartung als Sicherheitsthema**: Wartungsprotokolle archivieren; Sicherheit der Wartung selbst (LOTO) regeln.
- **Zwischenfälle als Lernchance**: Near-Miss-System; nicht erst Unfall abwarten.
- **Schnittstelle zum Datenschutz**: Cobot-Sensorik erfasst regelmäßig personenbezogene Daten; siehe `beschaeftigtendatenschutz-cobot`.

## Mustertexte

**Betriebsanweisung (Auszug Cobot, A4-Aushang):**

> Anwendungsbereich: Cobot Typ XY an Arbeitsplatz A12. Gefahren: Quetschung Hand zwischen Greifer und Werkstückträger; Augenkontakt mit Laserscanner.
> Schutzmaßnahmen: Nicht in den markierten Sicherheitsraum greifen, solange der Roboter aktiv ist. Bei Stillstand vor Eingriff Not-Halt drücken. Schutzbrille bei Wartungsarbeiten.
> Verhalten im Gefahrenfall: Not-Halt; Vorgesetzten informieren; Sifa hinzuziehen.
> Erste Hilfe: Ersthelfer Frau M. Schmidt, Raum B17, Notruf 112.
> Instandhaltung: Wartung nur durch befugtes Personal; LOTO-Verfahren beachten.

**Betriebsvereinbarung (Auszug):**

> Der Arbeitgeber setzt den Cobot Typ XY zur Unterstützung in der Montage ein. Leistungsdaten werden nur auf aggregierter Schicht-Ebene erhoben und nach 90 Tagen gelöscht. Eine personenbezogene Auswertung erfolgt nicht. Verstöße gegen diese Zweckbindung berechtigen den Betriebsrat zur Aussetzung des Einsatzes nach § 23 Abs. 3 BetrVG.

## Typische Fehler

- **Gefährdungsbeurteilung kopiert** vom Hersteller, ohne lokale Anpassung.
- **Keine Cobot-Validierung** mit Druckmessung – ISO/TS 15066 verlangt sie.
- **Unterweisung pauschal**, nicht arbeitsplatzspezifisch.
- **Wesentliche Veränderung** verkannt – kann CE-Pflicht des Betreibers auslösen (Integrator wird Hersteller).
- **Betriebsrat nicht beteiligt** – Betriebsvereinbarung anfechtbar.

## Querverweise

- `beschaeftigtendatenschutz-cobot`
- `betreiber-mitverschulden-und-fehlbedienung`
- `betriebsanleitung-sprache-und-warnhinweise`

## Checkliste Cobot-Inbetriebnahme

- [ ] EU-Konformitätserklärung und Anleitung vom Hersteller liegen vor (deutsch)
- [ ] Risikobeurteilung des Herstellers in baustellenspezifische Gefährdungsbeurteilung übernommen
- [ ] Schutzmaßnahmen STOP geplant; Power-and-Force-Limiting nach ISO/TS 15066 gemessen
- [ ] Betriebsanweisung in Muttersprachen der Belegschaft
- [ ] Unterweisung durchgeführt und dokumentiert (Datum, Unterschrift)
- [ ] Wartungsplan und Prüffristen § 14 BetrSichV festgelegt
- [ ] Betriebsvereinbarung mit dem Betriebsrat (§ 87 Abs. 1 Nr. 6, 7 BetrVG) abgeschlossen
- [ ] DSFA bei Sensorik mit Personenbezug erstellt
- [ ] Notfallplan und Erste-Hilfe-Organisation bekannt
- [ ] Berufsgenossenschaft über Einsatz informiert

## Vorfall: Sofortmaßnahmen

1. **Versorgung der Verletzten**, Notruf 112, Ersthelfer.
2. **Stillstand des Roboters**, Sicherung des Bereichs.
3. **Beweissicherung**: Fotos, Logsicherung (Schreibsperre), Zeugenaussagen schriftlich.
4. **Meldung an Berufsgenossenschaft** § 193 SGB VII binnen 3 Tagen bei Arbeitsunfall mit mehr als 3 Tagen Arbeitsunfähigkeit.
5. **Information Betriebsrat** § 89 BetrVG.
6. **Versicherer benachrichtigen** binnen 1 Woche.
7. **Ursachenanalyse** durch Sifa und ggf. externe Sachverständige.
8. **Korrekturmaßnahmen** mit Aktualisierung der Gefährdungsbeurteilung.

## Quellen Stand 06/2026

- ArbSchG; BetrSichV; DGUV Vorschrift 1; DGUV Information 209-074.
- TRBS 1111; TRBS 2111.
- VO (EU) 2023/1230 (MaschinenVO).
- ISO 10218-1:2025; ISO 10218-2:2025; ISO/TS 15066:2016.
- BetrVG § 87.
- Live-Verifikation auf baua.de, dguv.de, eur-lex.europa.eu; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
