---
name: beschaeftigtendatenschutz-cobot
description: "Prüft Beschäftigtendatenschutz bei Cobots: Leistungsdaten, Standort, Video, Betriebsrat, Zweckbindung und Löschfristen."
---

# Beschäftigtendatenschutz bei Cobot-Einsatz

## Fachkern: Beschäftigtendatenschutz bei Cobot-Einsatz
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Cobots erfassen regelmäßig Beschäftigtendaten: Pickrate je Schicht, Standortdaten innerhalb des Arbeitsplatzes, biometrische Marker (Hand-, Körpererkennung), ggf. Videoschnitt zur Sicherheit. Dazu kommt Cloud-Telemetrie für Predictive Maintenance. Das berührt DSGVO, § 26 BDSG (a. F.; nach EuGH C-34/21 "Hauptpersonalrat Hessen" eingeschränkt), den Beschäftigtendatenschutz-Entwurf (Bundesgesetzgebung in Vorbereitung), § 87 Abs. 1 Nr. 6 BetrVG und Art. 22, 35 DSGVO. Dieser Skill liefert Prüfschema, Betriebsvereinbarungsklauseln und Datenschutzhinweise.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Arbeitgeber, Datenschutzbeauftragter, Betriebsrat, Beschäftigte/r, Aufsichtsbehörde.
2. **Cobot-Modell:** Welche Sensoren? Welche Daten werden lokal/Cloud verarbeitet? Anbieter im EWR oder Drittland?
3. **Zweck:** Sicherheit (PFL/SSM), Wartung, Leistungssteuerung, Schichtplanung, individuelle Mitarbeiterauswertung?
4. **Bestehende BV** zu Mitarbeiterüberwachung?
5. **Anlass:** Erstinbetriebnahme, Beschwerde Mitarbeiter, Anfrage Aufsichtsbehörde, Audit, Anti-Diskriminierungsfall.

## Rechtlicher Rahmen

- **DSGVO** Art. 5, 6, 9, 13, 14, 22, 25, 32, 35.
- **§ 26 BDSG** in seinem nach EuGH C-34/21 verbleibenden Anwendungsbereich; bundesgesetzliche Reform des Beschäftigtendatenschutzes seit 2024/2025 im Gesetzgebungsverfahren.
- **BetrVG** § 87 Abs. 1 Nr. 6 (Einführung und Anwendung technischer Einrichtungen zur Überwachung), Nr. 7 Arbeits- und Gesundheitsschutz, § 80 Mitwirkungsrechte, § 90 Unterrichtung.
- **KI-VO** Art. 26 Abs. 7 Information der Beschäftigten und Betriebsräte bei Einsatz von Hochrisiko-KI am Arbeitsplatz; Art. 5 Verbote (insb. Emotionserkennung am Arbeitsplatz, Art. 5 Abs. 1 lit. f ab 02.02.2025).
- **MaschinenVO** VO (EU) 2023/1230 und ArbSchG für Sicherheits-Sensorik.

## Schritt für Schritt

1. **Datenkatalog.** Welche Daten entstehen (Sensor, Kamera, Audio, Vibration, Bedien-Logs)? Welche sind personenbezogen oder personenbeziehbar? Welche sind besonderer Kategorien (Art. 9 DSGVO)?
2. **Zweckbindung.** Pro Datenkategorie konkreten Zweck definieren; "Allzweck-Telemetrie" ist nicht zulässig.
3. **Rechtsgrundlage.** Für jeden Zweck: § 26 BDSG / Art. 6 Abs. 1 lit. b/c/f DSGVO / Kollektivvereinbarung Art. 88 DSGVO + § 26 Abs. 4 BDSG.
4. **DSFA Art. 35 DSGVO** bei systematischer Überwachung am Arbeitsplatz; Konsultation des DSB.
5. **Betriebsrat.** Mitbestimmung § 87 Abs. 1 Nr. 6 BetrVG; Betriebsvereinbarung mit klaren Zweck-, Erforderlichkeits-, Löschungs-, Auswertungsregeln.
6. **Technische Datenminimierung.** On-device-Aggregation; keine Roh-Videos in Cloud; Hashes statt Klartext.
7. **KI-VO-Pflichten.** Information der Beschäftigten und des Betriebsrats vor Inbetriebnahme; Verbot Emotionserkennung am Arbeitsplatz.
8. **Auftragsverarbeitung** Art. 28 DSGVO mit Cloud-Anbieter; bei Drittland: Standardvertragsklauseln, TIA.
9. **Auskunfts- und Löschpflichten** Art. 15, 17 DSGVO; klare Prozesse.

## Trade-off-Matrix

| Daten | Sicherheits-Zweck | HR-Zweck (Leistung) | Empfehlung |
|---|---|---|---|
| Bewegungsdaten Cobot-Arm | erforderlich, dauerhaft | nicht erforderlich | dauerhaft für Safety, aggregiert für HR (oder gar nicht) |
| Standort Mitarbeiter relativ zum Cobot | nur sicherheitskritisch | grds. unzulässig | Ereignisspeicher bei Annäherungsalarm, sonst gelöscht |
| Schicht-Performance | nicht erforderlich | mit BV möglich | nur aggregiert (Team-Ebene), Löschfrist 90 Tage |
| Bild/Video | nur sicherheitsrelevant | grds. unzulässig | Ereignisspeicher, on-device Blur |

## Praxistipps

- **Trennung Safety / HR** durch Datenarchitektur: getrennte Pipelines, getrennte Zugriffsrechte.
- **Kein Permanent-Video** im Cobot-Bereich.
- **Schichtleitung darf nicht** Echtzeit-Leistungsdaten einzelner Mitarbeiter sehen.
- **Mitarbeiter informieren** (Art. 13 DSGVO) bei Inbetriebnahme und bei Änderungen.
- **Anti-Diskriminierungs-Check**: keine Auswertung nach geschützten Merkmalen.

## Mustertexte

**Klausel Betriebsvereinbarung (Auszug):**

> § 4 Datenarten und Zwecke
> 1. Die im Cobot Typ Y erhobenen Bewegungs- und Sensordaten dienen ausschließlich der Sicherheit (Power-and-Force-Limiting, Speed-and-Separation-Monitoring) sowie der Wartung. Eine personenbezogene Leistungsauswertung erfolgt nicht.
> 2. Aggregierte Schicht-Performance-Daten werden nur auf Team-Ebene (mindestens 5 Personen) ausgewertet und nach spätestens 90 Tagen gelöscht.
> 3. Verstöße gegen diese Zweckbindung führen zur sofortigen Aussetzung des Einsatzes nach § 23 Abs. 3 BetrVG.

**Mitarbeiterinformation Art. 13 DSGVO (Auszug):**

> Verantwortlicher: [Firma]. Kontakt DSB: [E-Mail]. Im Cobot-Arbeitsplatz X werden zu Sicherheits- und Wartungszwecken Bewegungsdaten des Cobots sowie ereignisbezogen Annäherungsdaten Ihres Aufenthalts im Schutzraum erhoben. Rechtsgrundlage: § 26 BDSG i. V. m. Art. 6 Abs. 1 lit. b/f DSGVO und Betriebsvereinbarung vom [Datum]. Speicherdauer: 7 Tage (Sicherheit); 90 Tage aggregiert (Wartung). Empfänger: [Cloud-Anbieter] als Auftragsverarbeiter im EWR. Ihre Rechte: Art. 15-22 DSGVO; Beschwerde bei [zuständige Aufsichtsbehörde].

## Typische Fehler

- **Permanent-Video** für Sicherheit – unverhältnismäßig.
- **Telemetrie an Hersteller** ohne AVV.
- **Emotionserkennung** als Bedienkomfort – seit 02.02.2025 nach Art. 5 KI-VO verboten am Arbeitsplatz.
- **BV nicht aktualisiert** bei Software-Update mit neuen Funktionen.
- **Schicht-Performance individualisiert** – Mitbestimmung verletzt.

## Querverweise

- `arbeitsschutz-betrsichv-robotik`
- `datenminimierung-edge-cloud`
- `biometrie-emotion-und-personenerkennung`

## Quellen Stand 06/2026

- DSGVO; BDSG § 26.
- BetrVG § 87 Abs. 1 Nr. 6, 7; § 80; § 90.
- VO (EU) 2024/1689 (KI-VO), Art. 5, Art. 26 Abs. 7.
- EuGH, Urteil vom 30. März 2023, Rs. C-34/21 - Hauptpersonalrat Hessen, ECLI:EU:C:2023:270.
- Live-Verifikation auf bfdi.bund.de, edpb.europa.eu, eur-lex.europa.eu; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
