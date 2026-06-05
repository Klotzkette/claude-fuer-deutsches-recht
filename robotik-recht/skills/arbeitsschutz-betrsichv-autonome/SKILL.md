---
name: arbeitsschutz-betrsichv-autonome
description: "Arbeitsschutz Betrsichv Autonome: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arbeitsschutz Betrsichv Autonome

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Arbeitsschutz Betrsichv Autonome** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arbeitsschutz-betrsichv-robotik` | Prüft Arbeitsschutz und Betriebssicherheit bei Robotern im Betrieb: Gefährdungsbeurteilung, Unterweisung, Prüfungen, Betriebsanweisung. |
| `autonome-lieferroboter-oeffentlicher-raum` | Prüft autonome Lieferroboter im öffentlichen Raum: Verkehrsrecht, Sondernutzung, Haftung, Datenschutz und kommunale Genehmigungen. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Arbeitsschutz Betrsichv Autonome**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arbeitsschutz-betrsichv-robotik`

**Fokus:** Prüft Arbeitsschutz und Betriebssicherheit bei Robotern im Betrieb: Gefährdungsbeurteilung, Unterweisung, Prüfungen, Betriebsanweisung.


# Arbeitsschutz und BetrSichV in der Robotik

## Fachkern: Arbeitsschutz und BetrSichV in der Robotik
- **Spezialgegenstand:** Arbeitsschutz und BetrSichV in der Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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

## 2. `autonome-lieferroboter-oeffentlicher-raum`

**Fokus:** Prüft autonome Lieferroboter im öffentlichen Raum: Verkehrsrecht, Sondernutzung, Haftung, Datenschutz und kommunale Genehmigungen.


# Autonome Lieferroboter im öffentlichen Raum

## Fachkern: Autonome Lieferroboter im öffentlichen Raum
- **Spezialgegenstand:** Autonome Lieferroboter im öffentlichen Raum wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Lieferroboter auf Gehwegen, in Fußgängerzonen und in Mischverkehrsräumen berühren ein Mosaik aus Bundes-, Landes- und Kommunalrecht: StVO/StVG, Landesstraßengesetze (Sondernutzung), Kommunalsatzungen, DSGVO (Kamerasensorik), KI-VO (autonome Wahrnehmung), MaschinenVO/ProdSG (Sicherheit) und Vertragsrecht zum Endkunden. Dieser Skill ordnet die Regulierungsebenen, gibt einen Genehmigungs-und enthält Vorlagen für Sondernutzungsanträge und Datenschutzhinweise.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Betreiber/Logistik-Plattform, Kommune, Verkehrsbehörde, Datenschutzbehörde, Geschädigte (Fußgänger).
2. **Robotertyp:** Sidewalk Delivery Robot (SDR) mit <25 km/h, Größe und Gewicht?
3. **Einsatzgebiet:** Mehrere Kommunen? Test- oder Regelbetrieb? Innenstadt / Wohngebiet?
4. **Sensorik:** RGB-Kamera, LiDAR, Mikrofone? Cloud-Anbindung? Speicherung?
5. **Anlass:** Genehmigungsantrag, Unfall mit Personenschaden, Bürgerbeschwerde, Anzeige der Kommune.

## Rechtlicher Rahmen

- **StVG** § 1a (automatisiertes Fahren) gilt für Kraftfahrzeuge; Lieferroboter sind regelmäßig keine Kfz – Einordnung als "fahrzeugähnliches Gerät" oder gänzlich außerhalb. Klärung über Landesrecht/Kommune.
- **StVO** § 24 fahrzeugähnliche Geräte (Skater, Tretroller); analoge Anwendung diskutiert.
- **Landesstraßengesetze**, z. B. § 18 StrWG NRW, Art. 18 BayStrWG, § 16 StrG BW: Sondernutzungserlaubnis bei Inanspruchnahme der Straße über den Gemeingebrauch hinaus.
- **Kommunalsatzungen** (Sondernutzungssatzungen, Stadtordnungen) – Gebührentarife.
- **DSGVO** Art. 6 Abs. 1 lit. f Interessenabwägung; Art. 13 Informationspflicht; Art. 35 DSFA bei Kameras im öffentlichen Raum.
- **KI-VO** VO (EU) 2024/1689; Personenerkennung kann Hochrisiko sein (Anhang III).
- **MaschinenVO** VO (EU) 2023/1230 als Produkt; CE-Pflicht.
- **ProdHaftG / VO (EU) 2024/2853** und § 823 BGB Halter-/Hersteller-/Betreiberhaftung.

## Schritt für Schritt

1. **Produktklassifizierung.** Maschine nach MaschinenVO; KI-Funktion einordnen (Anhang III KI-VO?); ggf. Funkanlagengesetz.
2. **Genehmigung Verkehrsbehörde / Kommune.** Sondernutzungsantrag mit Fahrtrouten, Geschwindigkeit, Sicherheitsabständen, Notfall-Konzept; Anhörung Polizei, Tiefbauamt, Ordnungsamt.
3. **Datenschutz.** DSFA Art. 35 DSGVO (Bildverarbeitung im öffentlichen Raum ist regelmäßig pflichtig); Hinweisschilder am Roboter; Privacy-by-Design (Blurring von Gesichtern und Kennzeichen on-device).
4. **Sicherheitskonzept.** Maximalgeschwindigkeit (typisch 6 km/h Schrittgeschwindigkeit), Hindernisstopp, akustische und visuelle Signale; Begleitperson bei Erstbetrieb.
5. **Haftungsregelung.** Halter-Pflichtversicherung analog § 1 PflVG, soweit als Kfz eingestuft; sonst Betriebshaftpflicht mit ausdrücklicher Robotik-Klausel; Mindestsumme.
6. **Vertragsregelung Endkunde.** AGB-Klauseln zur Übergabe (Person, Mindestalter bei Apothekenwaren), Identifikationsverfahren, Datenverarbeitung.
7. **Vorfallmanagement.** Logging, Übermittlung an Behörde, ggf. Art. 73 KI-VO Meldung.

## Trade-off-Matrix

| Frage | Restriktiv | Liberal | Empfehlung |
|---|---|---|---|
| Einordnung als Kfz | StVZO-Pflichten | freier | Klärung mit Behörde pro Bundesland; nicht zu schnell festlegen |
| Kameras dauerhaft an | Beweissicherung | DSGVO-Risiko | nur Ereignisspeicher (Pre/Post-Event) und on-device Blurring |
| Audio | Sprachbefehle | Lauschverbot | bei Aufnahme grundsätzlich nein; Live-Audio nur bei klarer Trigger-Logik |
| Geschwindigkeit | 4 km/h | 12 km/h | 6 km/h Schrittgeschwindigkeit als Standard |

## Praxistipps

- **Frühzeitige Behördenrunde** mit Verkehrsbehörde, Polizei und Datenschutzbehörde; Protokoll.
- **Probebetrieb in Begleitung**, dokumentierte Lernkurve.
- **Notabbruch** auch remote durch Operator möglich.
- **Versicherung schriftlich klären** – Standard-Betriebshaftpflicht deckt autonome Mobilität oft nicht.
- **Lokale Akzeptanz**: Bürgerinformation, Beschwerde-Hotline.

## Mustertexte

**Sondernutzungsantrag (Auszug):**

> Hiermit beantragen wir die Erteilung einer Sondernutzungserlaubnis gemäß [§ 18 StrWG NRW] für den Einsatz von [n] Lieferrobotern Typ [Y] im Stadtgebiet [X] für den Zeitraum vom [Datum] bis [Datum]. Einsatzkorridor: [Kartenanlage]; Maximalgeschwindigkeit 6 km/h; Begleitung in den ersten 4 Wochen; Haftpflichtversicherung Deckungssumme 10 Mio. EUR. Datenschutz-Folgenabschätzung gemäß Art. 35 DSGVO ist beigefügt. Wir bitten um Genehmigung sowie Festsetzung der Sondernutzungsgebühr.

**Datenschutzhinweis (Aufkleber am Roboter):**

> Dieser Lieferroboter zeichnet zur Hinderniserkennung Kamerabilder auf. Gesichter und Kennzeichen werden bereits im Gerät verfremdet (on-device anonymisation). Speicherung nur ereignisbezogen, längstens 7 Tage. Verantwortlicher: [Firma], [Adresse]; Datenschutzbeauftragter: [E-Mail]. Weitere Informationen: [URL/QR].

## Typische Fehler

- **Pauschal "Roboter sind keine Fahrzeuge"** – Landesrecht beachten.
- **Daueraufzeichnung der Kamera** ohne DSFA – DSGVO-Verstoß.
- **Keine Kommunikationslinie** zur Polizei vor Ort.
- **Halterhaftung übersehen** bei Einordnung als Kfz.
- **Einsatz im Winter** ohne Anpassung der Sensorik – Sturzfälle.

## Querverweise

- `datenschutz-kameras-und-sensorik`
- `dronen-und-robotik-schnittstelle`
- `robotik-recht-allgemein`

## Behördenpfad (Genehmigung)

1. **Vorab-Kontakt** Verkehrsbehörde der Kommune, Polizei, Datenschutzbehörde des Bundeslandes.
2. **Antrag** mit Detail-Konzept, Karten, Geschwindigkeit, Begleitung, Versicherung, DSFA.
3. **Anhörung** Tiefbauamt, Ordnungsamt, ggf. Verkehrsausschuss.
4. **Probelauf** in Begleitung, mit Berichtspflichten.
5. **Regelbetrieb** mit Quartalsberichten (Beschwerden, Unfälle, KI-Performance).

## Checkliste Datenschutz

- [ ] DSFA Art. 35 DSGVO durchgeführt
- [ ] Privacy-by-Design: On-device-Blurring von Gesichtern/Kennzeichen
- [ ] Ereignisspeicher statt Daueraufzeichnung
- [ ] Hinweisschild am Roboter (Art. 13 DSGVO)
- [ ] AVV mit Cloud-Anbieter
- [ ] Speicherfrist klar (max. 7 Tage Standard)
- [ ] Auskunfts- und Löschpfad für Betroffene
- [ ] Aufsichtsbehörde informiert bei großflächigem Einsatz

## Quellen Stand 06/2026

- StVG; StVO; Landesstraßengesetze (NRW, Bayern, Baden-Württemberg u. a.).
- DSGVO Art. 6, 13, 35.
- VO (EU) 2024/1689 (KI-VO), Anhang III.
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2024/2853 (neue ProdHaftRL); ProdHaftG; § 823 BGB.
- Live-Verifikation auf eur-lex.europa.eu, gesetze-im-internet.de, BfDI; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
