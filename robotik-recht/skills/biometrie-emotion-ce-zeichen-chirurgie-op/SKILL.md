---
name: biometrie-emotion-ce-zeichen-chirurgie-op
description: "Biometrie Emotion CE Zeichen Chirurgie OP: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Biometrie Emotion CE Zeichen Chirurgie OP

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Biometrie Emotion CE Zeichen Chirurgie OP** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `biometrie-emotion-und-personenerkennung` | Prüft Biometrie, Emotionserkennung, Personenerkennung, Beschäftigtenkontext und Transparenzpflichten bei Robotern. |
| `ce-zeichen-fehlgebrauch-und-abmahnung` | Prüft CE-Kennzeichnung, irreführende Werbung, fehlende Unterlagen, Wettbewerbsrecht und Abmahnrisiken. |
| `chirurgie-und-op-robotik` | Prüft OP- und Chirurgierobotik: MDR-Klasse, klinische Bewertung, Vigilanz, Betreiber, Aufklärung, Wartung und Behandlungsfehlernähe. |
| `data-act-roboterdaten` | Prüft Data-Act-Fragen bei vernetzten Robotern: Nutzerdatenzugang, B2B-Datenbereitstellung, Geschäftsgeheimnisse und Cloudwechsel. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Biometrie Emotion CE Zeichen Chirurgie OP**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `biometrie-emotion-und-personenerkennung`

**Fokus:** Prüft Biometrie, Emotionserkennung, Personenerkennung, Beschäftigtenkontext und Transparenzpflichten bei Robotern.


# Biometrie, Emotion und Personenerkennung in der Robotik

## Fachkern: Biometrie, Emotion und Personenerkennung in der Robotik
- **Spezialgegenstand:** Biometrie, Emotion und Personenerkennung in der Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Roboter mit Personenerkennung kollidieren mit harten Verboten der KI-VO und mit der DSGVO. Art. 5 Abs. 1 KI-VO untersagt seit 02.02.2025 u. a. Emotionserkennung am Arbeitsplatz und in Bildungseinrichtungen (Art. 5 Abs. 1 lit. f), Social Scoring (lit. c) sowie – mit engen Ausnahmen – biometrische Echtzeit-Fernidentifizierung im öffentlich zugänglichen Raum zu Strafverfolgungszwecken (lit. h). Biometrische Daten sind besondere Kategorie (Art. 9 DSGVO). Dieser Skill prüft, welches Verfahren im konkreten Roboter zulässig ist und welche Transparenz-/Konformitätspflichten greifen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Betreiber, Datenschutzbehörde, Betriebsrat, betroffene Person.
2. **Funktion:** reine Personenanwesenheit (Anonyme Detection), Personenwiedererkennung (Tracking ohne Identität), Identifikation (1:N Match), Verifikation (1:1 Match), Emotionserkennung, Sentiment-Analyse.
3. **Einsatzort:** Werkhalle (Beschäftigte), Krankenhaus (Patienten), Bildungseinrichtung, öffentlicher Raum, Endkunden-Haushalt.
4. **Rolle der Echtzeit?** Live, post-hoc, beides?
5. **Anlass:** Konformitätsprüfung, Behördenanfrage, Beschwerde, KI-VO-Audit, DSFA.

## Rechtlicher Rahmen

- **KI-VO Art. 5** Verbotene Praktiken (ab 02.02.2025): lit. f Emotionserkennung im Arbeits- und Bildungsbereich (Ausnahme: medizinische/sicherheitsbezogene Gründe); lit. e ungezielte Massensammlung; lit. h Echtzeit-Biometrie im öffentlichen Raum zu Strafverfolgungszwecken mit engen Ausnahmen.
- **KI-VO Anhang III** Hochrisiko: biometrische Identifikation, Kategorisierung, Emotionserkennung außerhalb des Art. 5-Verbots.
- **KI-VO Art. 50** Transparenz: Information bei interaktiven KI-Systemen, Erkennung von Emotionen / biometrischer Kategorisierung.
- **DSGVO Art. 9** Verbot der Verarbeitung biometrischer Daten zur eindeutigen Identifizierung; Ausnahmen Abs. 2 lit. a (ausdrückliche Einwilligung), lit. b (Arbeitsrecht mit gesetzlicher Grundlage), lit. g (erhebliches öffentliches Interesse).
- **DSGVO Art. 22** automatisierte Einzelfallentscheidung mit Rechtsfolgen.
- **DSGVO Art. 35** DSFA verpflichtend.
- **BDSG** § 22 öffentlicher Bereich; § 26 BDSG Beschäftigte.
- **EuGH** Rs. C-184/20 - Vyriausioji tarnybinės etikos komisija (Anschluss zur weiten Auslegung biometrischer Daten).

## Schritt für Schritt

1. **Funktion exakt benennen.** "Personenerkennung" ist nicht gleich "Identifikation". Detection ≠ Recognition ≠ Identification ≠ Verifikation.
2. **Verbots-Check Art. 5 KI-VO.** Arbeitsplatz/Bildung + Emotion? Social Scoring? Massensammlung? Echtzeit-Biometrie in öffentlichem Raum?
3. **Hochrisiko-Check Anhang III.** Falls nicht verboten: Anhang III Nr. 1, Nr. 4. Konformitätsbewertung notwendig.
4. **DSGVO-Check.** Art. 9 Erlaubnistatbestand vorhanden? Art. 22 Folge? Art. 35 DSFA gemacht?
5. **Transparenzpflichten Art. 50 KI-VO** umsetzen: Hinweis am Roboter, vor Interaktion.
6. **Technische Maßnahmen.** On-device-Verarbeitung, kein Cloud-Upload, Templates statt Rohdaten, kurze Speicherfristen.
7. **Betriebsrat / Aufsichtsbehörde** beteiligen.
8. **Dokumentation.** Risikomanagement Art. 9 KI-VO, technische Dokumentation Anhang IV.

## Trade-off-Matrix

| Funktion | Klar erlaubt | Riskant | Klar verboten |
|---|---|---|---|
| Anonyme Personenanwesenheit (sicherheitskritisch) | ja | – | – |
| Biometrische Authentifizierung Mitarbeiter | mit BV und Einwilligung | dauerhaftes Tracking | – |
| Emotionserkennung Patient (med. Indikation) | mit DSFA und Aufklärung | – | – |
| Emotionserkennung Beschäftigte (HR) | – | – | Art. 5 Abs. 1 lit. f KI-VO |
| Live-Gesichtserkennung im öffentlichen Raum | – | – | grundsätzlich Art. 5 lit. h KI-VO |

## Praxistipps

- **Templates** statt Rohbilder; Hash-Based-Matching.
- **Hinweisschilder** am Roboter mit Symbol und Text.
- **Mitarbeiter-Beteiligung früh** – nicht erst bei Beschwerde.
- **Ausnahmen restriktiv lesen** – KI-VO sieht enge Voraussetzungen vor.
- **Cloud-Verarbeitung** vermeiden bei biometrischen Daten.

## Mustertexte

**Hinweisschild (Auszug):**

> Hinweis. Dieser Service-Roboter erkennt anonym, ob eine Person anwesend ist, um den Schutzraum freizugeben. Es findet keine Gesichts- oder Identifizierungserkennung statt. Verantwortlicher: [Firma]. Datenschutzbeauftragter: [E-Mail]. Weitere Informationen: [QR/URL].

**Klausel im Liefervertrag (Auszug):**

> Der Lieferant garantiert, dass das KI-System des Roboters Typ X (a) keine Emotionserkennung im Arbeits- oder Bildungskontext (Art. 5 Abs. 1 lit. f KI-VO) und (b) keine biometrische Identifizierung außerhalb der vom Betreiber vorgesehenen Verifikation an autorisierten Türen ermöglicht. Verstöße berechtigen den Betreiber zur sofortigen Vertragsauflösung und zur Geltendmachung pauschalisierten Schadensersatzes i. H. v. 100.000 EUR je Verstoß; weitere Schäden bleiben unberührt.

## Typische Fehler

- **Emotionserkennung als "soft sentiment"** im HR-Tool – Art. 5 KI-VO greift.
- **"Anonyme" Personenerkennung** mit Re-Identifikationspotenzial – DSGVO greift.
- **DSFA nicht durchgeführt** – Aufsichtsbehörden-Risiko.
- **Cloud-Übermittlung** ohne TIA.
- **Beschwerde ignoriert** – Bußgeldrisiko Art. 99 Abs. 3 KI-VO (bis 35 Mio. EUR oder 7 %).

## Querverweise

- `beschaeftigtendatenschutz-cobot`
- `datensatzqualitaet-und-bias-hri`
- `datenschutz-kameras-und-sensorik`

## Quellen Stand 06/2026

- VO (EU) 2024/1689 (KI-VO), Art. 5 Abs. 1 lit. b, c, e, f, h; Anhang III; Art. 50; Art. 99.
- DSGVO Art. 9, 22, 35.
- BDSG §§ 22, 26.
- EuGH, Urteil vom 1. August 2022, Rs. C-184/20 - Vyriausioji tarnybinės etikos komisija, ECLI:EU:C:2022:601.
- Live-Verifikation auf eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 2. `ce-zeichen-fehlgebrauch-und-abmahnung`

**Fokus:** Prüft CE-Kennzeichnung, irreführende Werbung, fehlende Unterlagen, Wettbewerbsrecht und Abmahnrisiken.


# CE-Kennzeichnung, Fehlgebrauch und Abmahnung

## Fachkern: CE-Kennzeichnung, Fehlgebrauch und Abmahnung
- **Spezialgegenstand:** CE-Kennzeichnung, Fehlgebrauch und Abmahnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Falsche CE-Kennzeichnung, fehlende EU-Konformitätserklärung, irreführende Werbung mit nicht erlangten Zertifikaten oder vorgetäuschten Prüfsiegeln sind klassische Felder für Abmahnungen nach UWG, behördliche Verfügungen (Marktüberwachung) und – seit GPSR VO (EU) 2023/988 – auch direkte Marktverbote. In der Robotik betreffen mehrere Rechtsakte gleichzeitig die CE: MaschinenVO, KI-VO, CRA, Funkanlagengesetz (FuAG), ggf. MDR. Dieser Skill prüft eine CE-Akte und gibt sowohl Verteidigungs- als auch Angriffsschriftsätze.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, Mitbewerber, Marktüberwachung, Verbraucherschutzverband, Abmahner.
2. **Anlass:** Abmahnung erhalten, Konkurrent ohne CE/falsches CE, Marktüberwachungsanfrage, Plattform-Notiz, Online-Shop-Compliance.
3. **Produktklasse:** Maschine, KI-System, Funkanlage, Medizinprodukt – meist mehrere zugleich.
4. **Kennzeichnungsfehler:** kein CE; CE ohne Konformitätsbewertung; CE der Benannten Stelle ohne tatsächliche Beteiligung; "CCC"-Schummelmarke.
5. **Unterlagen:** EU-Konformitätserklärung, technische Dokumentation, Bewertungsmodul, NB-Bescheinigung, Werbematerial.

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 Art. 16 ff. Kennzeichnung, Anhang II EU-Konformitätserklärung; Übergang aus Maschinen-RL 2006/42/EG bis 19.01.2027.
- **VO (EG) 765/2008 / VO (EU) 2019/1020 / NLF** allgemeine Kennzeichnungsregeln; Marktüberwachung.
- **GPSR** VO (EU) 2023/988 seit 13.12.2024 geltend.
- **KI-VO** Art. 16, 47, 48 EU-Konformitätserklärung; CE-Kennzeichnung Art. 48 Abs. 2 KI-VO.
- **CRA** VO (EU) 2024/2847 (Hauptpflichten ab 11.12.2027): CE-Pflicht für Produkte mit digitalen Elementen.
- **MDR** VO (EU) 2017/745 für medizinische Robotik.
- **FuAG** für Funkroboter (WLAN, Bluetooth, 5G).
- **UWG** §§ 3, 3a (Rechtsbruch), § 5 (Irreführung), § 13 (Abmahnung), § 8c (Missbrauch).
- **ProdSG** § 7 ff. Wirtschaftsakteure.

## Schritt für Schritt

1. **Anwendbare Rechtsakte** abschließend bestimmen; multiple CE-Bewertungen sind Standard.
2. **Bewertungsmodul** prüfen: Selbsterklärung, Stichprobenprüfung, Typprüfung, vollständiges QM – pro Rechtsakt.
3. **Notified Body** prüfen: vier Stellen, Kennnummer; sind die Nummern wirklich aktiv? (NANDO-Datenbank).
4. **EU-Konformitätserklärung** vollständig: alle Rechtsakte, alle Normen, Benannte Stelle, Verantwortlicher, Datum, Unterschrift.
5. **CE-Anbringung** korrekt: Mindesthöhe 5 mm, sichtbar, lesbar, dauerhaft, an der Maschine angebracht – nicht nur auf Verpackung.
6. **Werbeaussagen** prüfen: "TÜV-geprüft" nur, wenn echte Zertifikat-Nummer; "ISO 9001"-zertifizierte Firma ≠ ISO-zertifiziertes Produkt.
7. **Abmahnung handhaben:** Frist prüfen, modifizierte Unterlassungserklärung, Gegenangriff ggf. § 8c UWG (Missbrauch).
8. **Anzeige Marktüberwachung** bei klaren Verstößen.

## Trade-off-Matrix

| Verstoß | Schwere | Sanktionen | Strategie |
|---|---|---|---|
| Komplett fehlendes CE | sehr hoch | Marktverbot, Bußgeld bis 30 Mio. KI-VO | sofortiger Rückzug, Konformitätsbewertung |
| Werbung mit Notified Body, der nicht beteiligt war | hoch | UWG, ggf. § 263 StGB | sofortiger Stopp |
| CE-Anbringung zu klein/unleserlich | mittel | Bußgeld; Mängelbeseitigung | korrigieren, ggf. RAPEX |
| Konformitätserklärung formell unvollständig | gering | Mängelbeseitigung | nachholen, Akte aktualisieren |

## Praxistipps

- **Cross-Check** zwischen Konformitätserklärung und Werbung.
- **Schulung Vertrieb** zu zulässigen Aussagen.
- **NB-Nummer** nur drauf, wenn NB tatsächlich beteiligt.
- **GPSR-Verbraucherinfo**: Online-Shop muss Importeur/Verantwortlicher in EU benennen.
- **Plattformen** (Amazon, eBay) prüfen und Listings korrigieren.

## Mustertexte

**Modifizierte Unterlassungserklärung (Auszug):**

> Der Schuldner verpflichtet sich, es bei Vermeidung einer für jeden Fall der Zuwiderhandlung fälligen Vertragsstrafe in angemessener Höhe (im Streitfall durch das zuständige Gericht festzusetzen) zu unterlassen, geschäftlich Roboter der Modellreihe XYZ ohne CE-Kennzeichnung oder ohne beigefügte EU-Konformitätserklärung in Verkehr zu bringen oder zu bewerben.

**Mahnschreiben (Mitbewerber, Auszug):**

> Sehr geehrte Damen und Herren, wir machen Sie auf einen Verstoß gegen § 3a UWG i. V. m. Art. 16, 47 KI-VO und Art. 16 MaschinenVO aufmerksam. Sie bewerben den Roboter Typ Z auf Ihrer Website (URL) mit dem Hinweis "CE-zertifiziert nach KI-VO". Eine EU-Konformitätserklärung gemäß Art. 47 KI-VO ist nicht beigefügt; die Notified-Body-Kennnummer NB 0123 ist in NANDO nicht für den Anhang VI KI-VO gelistet. Wir fordern Sie auf, Werbung und Inverkehrbringen bis [Frist] zu unterlassen und eine strafbewehrte Unterlassungserklärung beigefügten Musters abzugeben.

## Typische Fehler

- **CE auf Verpackung** statt am Produkt.
- **NB-Nummer** der ISO-9001-zertifizierenden Stelle als Konformitäts-NB ausgegeben.
- **CE für Cobot** nur nach MaschinenVO, ohne CE nach KI-VO.
- **Konformitätserklärung** in falscher Amtssprache.
- **Missbräuchliche Abmahnung** ohne § 8 Abs. 3 UWG-Aktivlegitimation.

## Querverweise

- `cra-produkt-mit-digitalen-elementen`
- `betriebsanleitung-sprache-und-warnhinweise`
- `robotik-recht-allgemein`

## Quellen Stand 06/2026

- VO (EU) 2023/1230 (MaschinenVO), Art. 16, Anhang II.
- VO (EG) 765/2008; VO (EU) 2019/1020.
- VO (EU) 2023/988 (GPSR).
- VO (EU) 2024/1689 (KI-VO), Art. 16, 47, 48; Art. 99.
- VO (EU) 2024/2847 (CRA).
- VO (EU) 2017/745 (MDR).
- FuAG.
- UWG §§ 3, 3a, 5, 8, 8c, 13.
- NANDO-Datenbank der EU-Kommission.
- Live-Verifikation auf eur-lex.europa.eu, BAuA, ec.europa.eu/growth (NANDO); lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 3. `chirurgie-und-op-robotik`

**Fokus:** Prüft OP- und Chirurgierobotik: MDR-Klasse, klinische Bewertung, Vigilanz, Betreiber, Aufklärung, Wartung und Behandlungsfehlernähe.


# Chirurgie- und OP-Robotik

## Fachkern: Chirurgie- und OP-Robotik
- **Spezialgegenstand:** Chirurgie- und OP-Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

OP- und Chirurgieroboter sind regelmäßig Medizinprodukte hoher Risikoklasse (MDR Klasse IIb/III). Ihr rechtlicher Rahmen ist die MDR VO (EU) 2017/745 und das nationale MPDG, ergänzt um den Behandlungsvertrag (§§ 630a ff. BGB), das ärztliche Berufsrecht, die KI-VO (bei autonomen oder unterstützenden KI-Funktionen), die DSGVO (Patientendaten) und das ProdHaftG/VO (EU) 2024/2853. Dieser Skill ordnet die Pflichten von Hersteller, Krankenhaus und Operateur sowie typische Risikofelder: Aufklärung über Roboter-Beteiligung, Schulungsstand des Operateurs, Wartungspflichten, Vigilanz-Meldungen, Behandlungsfehlernähe.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Krankenhausträger, Chefarzt/Operateur, MPDG-Beauftragter, Patient/Angehörige, Versicherer, BfArM, Notified Body.
2. **Robotertyp:** telemanipuliert (z. B. da-Vinci-Architektur), teilautonom, vollautonom für definierte Schritte; mit oder ohne KI-Unterstützung.
3. **Eingriffstyp:** Urologie, Gynäkologie, Allgemeinchirurgie, Orthopädie, Neurochirurgie.
4. **Anlass:** Inverkehrbringen, Vigilanz-Vorfall, Behandlungsfehlervorwurf, Schulungslücke, Wartungsversäumnis, BfArM-Inspektion.
5. **Unterlagen:** EU-Konformitätserklärung, klinische Bewertung, Vigilanz-Berichte, Wartungsprotokolle, Schulungsnachweise, OP-Berichte, Logs.

## Rechtlicher Rahmen

- **MDR** VO (EU) 2017/745: Art. 5 ff. Konformität, Art. 52 ff. Bewertung, Art. 87 ff. Vigilanz, Anhang VIII Klassifizierung.
- **MPDG** §§ 4 ff. Pflichten Wirtschaftsakteure, §§ 14 ff. Betreiber, §§ 35 ff. Vigilanz.
- **MPBetreibV** Pflichten Betreiber, insb. § 3 Einweisung, § 6 Bestandsverzeichnis, § 11 sicherheitstechnische Kontrollen.
- **BGB** §§ 630a, 630c, 630e (Aufklärung), 630f (Dokumentation), 630h (Beweislastregeln).
- **§§ 823, 831 BGB** und ärztliche Haftung; ständige Rspr. BGH (Aufklärung, voll beherrschbare Risiken).
- **KI-VO** Anhang III bei sicherheitskritischer KI-Funktion; integrierte Konformitätsbewertung mit MDR.
- **DSGVO** Art. 9 Patientendaten; § 22 BDSG.
- **VO (EU) 2024/2853** Produkthaftung.

## Schritt für Schritt

1. **MDR-Klassifizierung.** Klasse IIb/III? Software als Medizinprodukt (SaMD) gesondert? Kombiprodukt?
2. **Konformitätsbewertung.** Modul nach Anhang IX/X MDR; Benannte Stelle eingebunden.
3. **Klinische Bewertung** und ggf. klinische Prüfung Art. 62 ff. MDR.
4. **Vigilanz-System.** Schwere Vorkommnisse Art. 87 MDR binnen 15 Tagen; FSCA (Field Safety Corrective Actions); FSN (Field Safety Notice).
5. **Krankenhaus-Pflichten.** Einweisung der Anwender § 3 MPBetreibV; Wartungsplan; sicherheitstechnische Kontrollen; medizinprodukterechtliche Risikobewertung in der OP.
6. **Aufklärung des Patienten** §§ 630c, 630e BGB: Art und Tragweite des Eingriffs, Roboter-Beteiligung, Alternativen, spezifische Risiken; Erfahrung des Operateurs.
7. **Dokumentation** OP-Bericht inkl. Robotik-Parameter, Software-Version, Vorfälle.
8. **Schadenfall**. Spurensicherung der Logs, Wartungsdokumente, Schulungsnachweise.

## Trade-off-Matrix

| Frage | Konservativ | Aggressiv | Empfehlung |
|---|---|---|---|
| Aufklärung "Roboter" | ausführlich, mit Erfahrungsstand des Operateurs | knapp | ausführlich; insb. bei neuer Methode |
| Schulungspflicht | volle MDR-Einweisung + simulationsbasiert | Hersteller-Schulung mit Kurzeinweisung | mindestens nachweisbare Mindeststunden + Fallzahl |
| KI-Funktion an/aus | aus, wenn nicht zertifiziert | an im Pilotmodus | nur dokumentiert nach Risikobewertung |
| Vigilanz-Meldung | proaktiv | nur bei klarer Schwelle | proaktiv bei Verdacht; Risk-of-Underreporting |

## Praxistipps

- **Schulungsmatrix** pro Operateur mit Fallzahlen und Versionsstand.
- **Logs als ärztliche Dokumentation** archivieren – nach § 630f BGB 10 Jahre, MDR 15 Jahre Art. 10 Abs. 8.
- **Aufklärung 24 h vor Eingriff** dokumentieren.
- **OP-Team-Briefing** vor Robotik-OPs; Notfall-Konvertierung.
- **OT-Sicherheit**: Roboter-Netzsegment, kein Internet, NIS-2-Schnittstelle.

## Mustertexte

**Aufklärungsbogen Auszug:**

> Sie werden mit dem Operationsroboter Typ XY (Hersteller: ABC, Modell-/Versionsstand: …) operiert. Der Operateur Dr. Z hat im System bisher [n] Eingriffe Ihrer Art durchgeführt; die statistische Lernkurve dieses Eingriffs liegt nach Hersteller- und Studienangaben bei etwa [n] Eingriffen für stabile Komplikationsraten. Im seltenen Fall eines Roboter-Ausfalls wird auf den konventionellen offenen oder laparoskopischen Eingriff konvertiert. Spezifische Roboter-Risiken: thermische Verletzungen durch Elektrokoagulation, Trokar-Verletzungen, vorübergehende Position-Tracking-Verluste. Alternativen: offene OP, laparoskopisch konventionell.

**Vigilanz-Meldung (Auszug):**

> Schweres Vorkommnis nach Art. 87 MDR vom [Datum]: Während laparoskopischer Nephrektomie kam es zu einem unerwarteten Stillstand des Roboter-Arms 3 nach Software-Update vom [Datum-1]. Konventionelle Konvertierung erfolgreich; Patient ohne dauerhafte Folgen. Logs gesichert. Sofortige FSN an alle Kliniken mit gleichem Modell. Korrekturmaßnahme: Rückrollen auf vorherige Software-Version. Statusupdate folgt fristgerecht.

## Typische Fehler

- **Aufklärung pauschal** – BGH verlangt patienten-/eingriffsspezifisch.
- **Schulungsstand nicht dokumentiert** – Behandlungsfehlervorwurf einfach.
- **Wartungsversäumnis** kann zur Beweislastumkehr nach § 630h BGB führen.
- **Vigilanz-Meldung zu spät** – MPDG-Bußgeld.
- **KI-Funktion ohne Konformitätsbewertung** in laufendem Eingriff aktiv.

## Querverweise

- `accuracy-robustness-cybersecurity-ai`
- `betreiber-mitverschulden-und-fehlbedienung`
- Plugin-Nachbar `medizinrecht` für Behandlungsvertrag

## Quellen Stand 06/2026

- VO (EU) 2017/745 (MDR), Art. 5, 10, 52, 62, 87; Anhang VIII.
- MPDG; MPBetreibV.
- BGB §§ 630a-h.
- VO (EU) 2024/1689 (KI-VO), Anhang III.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- DSGVO Art. 9; BDSG § 22.
- Live-Verifikation auf eur-lex.europa.eu, bfarm.de, dimdi/bfarm; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 4. `data-act-roboterdaten`

**Fokus:** Prüft Data-Act-Fragen bei vernetzten Robotern: Nutzerdatenzugang, B2B-Datenbereitstellung, Geschäftsgeheimnisse und Cloudwechsel.


# Data Act bei vernetzten Robotern

## Fachkern: Data Act bei vernetzten Robotern
- **Spezialgegenstand:** Data Act bei vernetzten Robotern wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Data Act (VO (EU) 2023/2854) ist seit 11.01.2024 in Kraft und gilt überwiegend ab 12.09.2025 (Art. 50). Vernetzte Roboter (industriell, im Service, im Haushalt) sind "connected products" i. S. d. Art. 2 Nr. 5 Data Act. Das löst Pflichten aus: Nutzerzugang zu den vom Produkt erzeugten Daten (Art. 4), Bereitstellung an Dritte auf Verlangen des Nutzers (Art. 5), B2G-Datenzugang bei besonderen Notlagen (Art. 14 ff.), Vertragsregeln bei B2B (Art. 13 unlautere Klauseln), Cloud-Switching (Art. 23 ff.) sowie Interoperabilität (Art. 28 ff.). Dieser Skill ordnet die Pflichten und gibt Vertragsbausteine.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller des vernetzten Roboters, Datenhalter, Nutzer (B2B oder B2C), Drittanbieter, Cloud-Anbieter, öffentliche Stelle.
2. **Rolle der Daten:** Predictive Maintenance, Performance-Optimierung, Trainingsdaten für KI, Servicegeschäft.
3. **Anlass:** Auskunftsanspruch des Kunden, Datenfreigabe an Dritten, Cloud-Switch, Vertragsverhandlung, behördlicher Datenzugriff.
4. **Geschäftsgeheimnisse:** Welche Datenkategorien sind Trade Secrets?
5. **Vertragslage:** Bestehende AGB, Lizenzbedingungen, AVV, Datennutzungsbestimmungen.

## Rechtlicher Rahmen

- **Data Act** VO (EU) 2023/2854; Kerngeltung ab 12.09.2025.
- Art. 3 Design- und Transparenzpflicht (Daten vom Produkt unmittelbar zugänglich oder spätestens auf Verlangen).
- Art. 4 Nutzerzugang.
- Art. 5 Datenfreigabe an Dritte.
- Art. 13 Unlautere Vertragsklauseln im B2B.
- Art. 14-22 B2G-Datenzugang bei "exzeptioneller Notwendigkeit".
- Art. 23-31 Cloud-Switching (Wechselrecht innerhalb 30 Tagen, Gebührenstaffel).
- Art. 28-30 Interoperabilität gemeinsamer Datenräume.
- **DSGVO** bleibt unberührt (Art. 1 Abs. 5 Data Act).
- **GeschGehG** §§ 1, 17 GeschGehG / VO Trade Secrets (RL (EU) 2016/943).
- **VO (EU) 2024/1689 (KI-VO)** Art. 10 zur Datenqualität.

## Schritt für Schritt

1. **Klassifizierung.** Ist der Roboter "connected product"? Sind Daten "produktgenerierte Daten" oder rein abgeleitete?
2. **Datenkatalog.** Welche Datenarten entstehen? Welche sind schon heute Bestandteil des Datenmodells?
3. **Datenzugang vorgehalten** Art. 3 Abs. 1: Daten sollen "by design" zugänglich sein; falls nicht praktikabel, Auskunfts- und Bereitstellungs-Pfad definieren.
4. **Vorvertragliche Information** Art. 3 Abs. 2: Datenarten, Speicherort, Zugriffsmöglichkeiten, Drittweitergaben.
5. **Nutzerzugang-Prozess** Art. 4: Anforderung, Identitätsprüfung, "ohne unangemessene Verzögerung", maschinenlesbar wenn möglich.
6. **Dritter-Bereitstellung** Art. 5: nur auf Verlangen des Nutzers, "fair, reasonable, transparent" Bedingungen (FRAND-Logik); Schutz von Geschäftsgeheimnissen Art. 5 Abs. 8.
7. **B2B-Verträge** Art. 13 prüfen auf unlautere Klauseln; Vorsicht bei einseitigen Klauseln gegen KMU.
8. **Cloud-Switching** Art. 23 ff.: Vertragsklauseln auf Wechselrecht und Datenexport; Gebührensenkung nach Übergangsphase.
9. **Geschäftsgeheimnisschutz**: Vereinbarungen mit Drittnutzer auf Schutzmaßnahmen, NDA, technische Schutzvorkehrungen.

## Trade-off-Matrix

| Frage | Restriktiv (Hersteller-Sicht) | Liberal (Nutzer-Sicht) | Empfehlung |
|---|---|---|---|
| Datenzugriff "by design" | nur per Antrag | direkt im Cobot-Display | mind. API auf Wunsch innerhalb 7 Tagen |
| Trade-Secrets-Schutz | breit | eng | konkret bezeichnete TS-Kategorien dokumentieren |
| Drittfreigabe-Bedingungen | hohe Gebühren | kostenfrei | Selbstkosten plus angemessener Aufschlag (Art. 9) |
| Cloud-Switch-Frist | 90 Tage | sofort | gestaffelt; 30 Tage Standard |

## Praxistipps

- **Data Catalog** für jedes Produkt.
- **API-Endpunkt** standardisiert.
- **Geschäftsgeheimnis-Markierung** in der Datenstruktur.
- **Vorlage für Nutzer-Anforderungen** in der Anleitung.
- **AGB** mit Drittnutzungsregeln, FRAND-konform.

## Mustertexte

**Vorvertragliche Information Art. 3 Abs. 2 (Auszug):**

> Daten und Datenarten: Sensor-Telemetrie (Position, Temperatur, Vibration), Bedien-Logs, Wartungsereignisse, KI-Modell-Konfidenzwerte. Speicherung: lokal auf dem Roboter (rolling 30 Tage), zusätzlich beim Anbieter (180 Tage). Zugang: Selbstauskunft des Nutzers via Web-Portal; auf Wunsch Datenexport als CSV/Parquet. Drittweitergabe: nur auf Verlangen des Nutzers gemäß Art. 5 Data Act. Geschäftsgeheimnisse: KI-Modellparameter und Service-Algorithmen ausgenommen.

**Vertragsklausel Drittnutzer:**

> Der Drittnutzer erhält Zugang zu den vom Nutzer freigegebenen Daten zum Zweck [Predictive Maintenance Vertragspartner]. Bedingungen: technische und organisatorische Schutzmaßnahmen (mind. ISO/IEC 27001), Geheimhaltungsverpflichtung, Nutzung ausschließlich für den vereinbarten Zweck. Vergütung: Selbstkosten plus angemessener Aufschlag gemäß Art. 9 Data Act. Bei Verstoß: sofortige Sperrung; Vertragsstrafe 50.000 EUR je Verstoß.

## Typische Fehler

- **"Daten gehören uns"-Klauseln** in B2B-AGB – Art. 13 Data Act-widrig.
- **Vorvertragliche Information fehlt** – Bußgeld nach § 7 ff. BfDI-Vollzugsmodell.
- **Cloud-Switching-Klauseln** mit überhöhten Gebühren oder Sperrfristen.
- **Geschäftsgeheimnis-Vorhaben pauschal** angenommen – Art. 5 verlangt konkrete Schutzbedürftigkeit.
- **Datenexport nur in proprietären Formaten** – Interoperabilitätspflicht verletzt.

## Querverweise

- `datenminimierung-edge-cloud`
- `beweislast-und-offenlegung-produkthaftung`
- `cra-produkt-mit-digitalen-elementen`

## Quellen Stand 06/2026

- VO (EU) 2023/2854 (Data Act), Art. 3, 4, 5, 9, 13, 14-22, 23-31, 50.
- DSGVO.
- GeschGehG; RL (EU) 2016/943.
- VO (EU) 2024/1689 (KI-VO), Art. 10.
- Live-Verifikation auf eur-lex.europa.eu, edpb.europa.eu, BfDI; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
