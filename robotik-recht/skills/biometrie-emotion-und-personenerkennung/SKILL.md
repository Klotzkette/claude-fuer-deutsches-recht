---
name: biometrie-emotion-und-personenerkennung
description: "Prüft Biometrie, Emotionserkennung, Personenerkennung, Beschäftigtenkontext und Transparenzpflichten bei Robotern."
---

# Biometrie, Emotion und Personenerkennung in der Robotik

## Fachkern: Biometrie, Emotion und Personenerkennung in der Robotik
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

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
