---
name: autonome-lieferroboter-oeffentlicher-raum
description: "Prüft autonome Lieferroboter im öffentlichen Raum: Verkehrsrecht, Sondernutzung, Haftung, Datenschutz und kommunale Genehmigungen."
---

# Autonome Lieferroboter im öffentlichen Raum

## Fachkern: Autonome Lieferroboter im öffentlichen Raum
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

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
