---
name: dsfa-ki-systeme-schnittstelle-art-26-kivo
description: "DSFA für KI-Systeme an der Schnittstelle zur KI-Verordnung: Koordination Art. 35 DSGVO mit Art. 26 KI-VO Betreiberpflichten und Art. 27 KI-VO Grundrechte-Folgenabschaetzung. Output: integriertes DSFA-FRIA-Konzept."
---

# DSFA für KI-Systeme an der Schnittstelle zur KI-Verordnung

## Zweck

Koordination einer Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO mit den Anwender- bzw. Betreiberpflichten nach Art. 26 KI-VO und der Grundrechte-Folgenabschaetzung (Fundamental Rights Impact Assessment, FRIA) nach Art. 27 KI-VO. Ergebnis ist ein integriertes Konzept, das DSFA und FRIA koordiniert, ohne sie rechtlich zu verschmelzen.

## Wann dieses Modul hilft

- Bei Einsatz von Hochrisiko-KI-Systemen nach Anhang III KI-VO (Verordnung EU 2024/1689)
- Bei generativen KI-Diensten, die personenbezogene Daten verarbeiten
- Bei Profiling-Systemen mit Rechtswirkung (Art. 22 DSGVO und Anhang III KI-VO)
- Bei Biometrie, Beschaeftigtenscoring, Kreditscoring, Versicherungsrisikobewertung
- Vor Vertragsschluss mit KI-Anbietern (Anbieter- versus Betreiberrolle)

## Rechtlicher Rahmen

- Art. 35 DSGVO Pflicht-DSFA bei voraussichtlich hohem Risiko, insbesondere bei neuen Technologien (Art. 35 Abs. 1, Abs. 3 lit. a DSGVO).
- Art. 22 DSGVO automatisierte Einzelentscheidung.
- VO (EU) 2024/1689 KI-VO:
 - Art. 6, Anhang III: Hochrisiko-KI-Kategorien
 - Art. 26 Betreiberpflichten (englisch: deployers): bestimmungsgemaesse Nutzung, menschliche Aufsicht, Logging, Information Betroffener
 - Art. 27 Pflicht zur Grundrechte-Folgenabschaetzung (FRIA) für bestimmte Betreiber (öffentliche Stellen, oeffentlich finanzierte Dienste, Kreditwuerdigkeit, Kranken- und Lebensversicherung)
 - Art. 50 Transparenzpflichten generative KI
- EDSA-Stellungnahme 28/2024 zu KI-Modellen (Auslegung DSGVO bei KI).
- EDSA-Leitlinien WP 248 rev.01 zur DSFA.
- Anwendungsbeginn KI-VO: gestaffelt, Hochrisiko-Pflichten 02.08.2026.

## Abgrenzung Anbieter und Betreiber

- Anbieter (provider) entwickelt oder bringt das KI-System in Verkehr und ist primaer adressiert durch Art. 8 bis Art. 21 KI-VO.
- Betreiber (deployer) setzt das KI-System ein und ist adressiert durch Art. 26, 27 KI-VO.
- Die DSGVO-Verantwortlichkeit haengt nicht an dieser Rolle, sondern an der Entscheidung ueber Zwecke und Mittel der Verarbeitung (Art. 4 Nr. 7 DSGVO).
- Praxisregel: Wer ein KI-System für eigene Personalentscheidung, Kundenbewertung oder Behördenentscheidung nutzt, ist regelmaessig Betreiber nach KI-VO und Verantwortlicher nach DSGVO.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welches KI-System, welcher Zweck, welche Datenarten, welche Betroffenenkreise? Anbieter und Betreiber benennen, Anhang-III-Kategorie pruefen.
2. **Verhaeltnismaessigkeitspruefung.** Notwendigkeit und Verhaeltnismaessigkeit der KI-gestuetzten Verarbeitung; Pruefung ob ein nicht-automatisiertes Verfahren ausreicht. Art. 5 Abs. 1 DSGVO und Erforderlichkeitspruefung.
3. **Risikoanalyse.** Doppelblick:
 - DSGVO-Risiken: Profiling, automatisierte Entscheidung, Trainingsdatenleck, Halluzination ueber Personen.
 - KI-VO-Risiken: Diskriminierung durch Datenbias, fehlende menschliche Aufsicht, fehlende Robustheit.
4. **Massnahmen.** TOMs nach Art. 32 DSGVO plus KI-VO-Massnahmen: menschliche Aufsicht, Logging, Transparenz, Information Betroffener (Art. 26 Abs. 11 KI-VO).
5. **Restrisiko.** Doppelte Restrisikobewertung — für DSFA (Art. 35 DSGVO) und für FRIA (Art. 27 KI-VO), wenn diese Pflicht besteht.
6. **Konsultation / Genehmigung.** DSB Anhörung Art. 35 Abs. 2 DSGVO. Bei hohem Restrisiko: Art. 36 DSGVO Vorabkonsultation. Nach KI-VO: nationale Marktueberwachungsbehoerde nach Art. 70 KI-VO ggf. einbinden. Integration in Verarbeitungsverzeichnis und KI-Bestandsverzeichnis.

## Integriertes DSFA-FRIA-Konzept Template

```
INTEGRIERTES DSFA-FRIA-KONZEPT [DATUM]

KI-System: [BEZEICHNUNG, Version, Anbieter]
Betreiber (Verantwortlicher): [NAME]
Anhang-III-Kategorie: [Nummer, Beschreibung]

1. Beschreibung
- KI-Funktion: [Klassifikation / Regression / Generation / Profiling]
- Trainingsdaten Herkunft: [Anbieterangabe]
- Personenbezogene Eingabedaten: [Datenarten, Betroffenenkreise]
- Personenbezogene Ausgabe: [...]

2. Rechtsgrundlage DSGVO
- Art. 6 / Art. 9 DSGVO: [...]
- Art. 22 DSGVO Schutzmechanismus: [Menschenentscheidung / Einwilligung / Vertragserforderlichkeit / Rechtsvorschrift]

3. DSFA nach Art. 35 DSGVO
- Schwellwert: erfuellt durch [Profiling / neue Technologien / sensible Daten]
- Risikoanalyse: [Verweis auf Risikomatrix]
- Massnahmen: [TOMs Art. 32 DSGVO]
- Restrisiko: [GRUEN / GELB / ORANGE / ROT]

4. KI-VO Betreiberpflichten Art. 26
- Bestimmungsgemaesse Nutzung: [...]
- Menschliche Aufsicht Art. 14 KI-VO: [Rollen, Eingriffsmoeglichkeiten]
- Logging Art. 26 Abs. 6 KI-VO: [Aufbewahrungsdauer, Inhalt]
- Information Betroffener Art. 26 Abs. 11 KI-VO: [Form, Zeitpunkt]
- Datenqualitaet bei Inputdaten Art. 26 Abs. 4 KI-VO: [...]

5. FRIA nach Art. 27 KI-VO (falls einschlaegig)
- Beschreibung Einsatz: [Zweck, Zeitraum, Betroffenenkreise]
- Auswirkungen Grundrechte: [Wuerde, Gleichheit, Datenschutz, Meinungsaeusserung]
- Risikomindernde Massnahmen: [...]
- Beobachtung: [...]
- Meldung an nationale Marktueberwachungsbehoerde: [Datum, Aktenzeichen]

6. Vorab-Konsultation
- Art. 36 DSGVO: erforderlich ja / nein
- KI-VO Konsultation Marktueberwachung: erforderlich ja / nein

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
Unterschrift KI-Beauftragter (falls bestellt): ____________________
```

## Typische Fehler

- DSFA und FRIA werden vermischt — beide Instrumente sind rechtlich eigenstaendig und muessen getrennt nachweisbar sein.
- Betreiberpflichten Art. 26 KI-VO werden auf den Anbieter abgeschoben — die Pflicht trifft den Einsetzenden.
- Logging-Pflicht Art. 26 Abs. 6 KI-VO wird mit DSGVO-Loeschpflichten konfligierend behandelt, ohne Pruefung der Rechtsgrundlage des Loggings.
- Anhang III KI-VO wird nicht geprueft — Kategorisierung fehlt.
- KI-Anbieter im Drittland: zusaetzliche Transferpruefung uebersehen (Skill dsfa-für-internationale-datentransfers).
- Generative KI: Art. 50 KI-VO Transparenzpflichten uebersehen.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Vorab-Konsultation
- `datenschutzrecht/skills/dsfa-für-internationale-datentransfers/SKILL.md` — Drittlandtransfer
- `datenschutzrecht/skills/ki-verordnung-compliance/SKILL.md` — KI-VO Compliance
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36, 22 DSGVO
- VO (EU) 2024/1689 KI-VO, insbesondere Art. 6, 14, 26, 27, 50, Anhang III
- EDSA-Stellungnahme 28/2024 zu KI-Modellen
- EDSA-Leitlinien WP 248 rev.01
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
