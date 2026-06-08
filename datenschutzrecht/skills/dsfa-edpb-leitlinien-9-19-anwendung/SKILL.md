---
name: dsfa-edpb-leitlinien-9-19-anwendung
description: "Anwendung der EDPB-/EDSA-Leitlinien WP 248 rev.01 zur DSFA: die neun Kriterien für voraussichtlich hohes Risiko strukturiert pruefen. Output: Kriterien-Tabelle mit Subsumtion und Schwellwertergebnis."
---

# Anwendung der EDPB-Leitlinien WP 248 rev.01 zur DSFA

## Zweck

Strukturierte Anwendung der neun Kriterien der EDPB-/EDSA-Leitlinien WP 248 rev.01 zur Bestimmung von voraussichtlich hohem Risiko. Ergebnis ist eine Kriterien-Tabelle mit Subsumtion und einer klaren Schwellwertaussage: 0 Kriterien (DSFA entbehrlich), 1 Kriterium (Empfehlung mit Begruendung), 2 oder mehr Kriterien (DSFA zwingend, soweit keine entgegenstehende Whitelist-Position einschlaegig ist).

## Wann dieses Modul hilft

- In der Schwellwertanalyse einer DSFA-Trigger-Pruefung, wenn weder Art. 35 Abs. 3 noch Abs. 4 DSGVO greift
- Wenn die Aufsichtsbehoerde eine Begruendung der DSFA-Entscheidung verlangt
- Zur Vorpruefung von KI-, Profiling- oder Beschaeftigtendaten-Verarbeitungen
- Wenn die DSB-Stellungnahme eine EDSA-Konformitaet anfordert

## Rechtlicher Rahmen

- EDPB-/EDSA-Leitlinien WP 248 rev.01 (Artikel-29-Gruppe, von EDSA uebernommen): neun Kriterien für voraussichtlich hohes Risiko.
- Art. 35 Abs. 1 DSGVO Generalklausel — die WP-248-Kriterien konkretisieren den Tatbestand.
- Art. 35 Abs. 2 DSGVO Anhörung des DSB.
- Art. 70 Abs. 1 lit. e DSGVO Aufgabe des EDSA zur Konkretisierung.

## Die neun WP-248-Kriterien

1. Bewertung oder Scoring (einschliesslich Profiling und Prognose)
2. Automatisierte Entscheidung mit rechtlicher oder aehnlich erheblicher Wirkung (Art. 22 DSGVO)
3. Systematische Ueberwachung
4. Sensible Daten oder hoechstpersönliche Daten (Art. 9, Art. 10 DSGVO; auch Standortdaten, Finanzdaten, Kommunikationsinhalte)
5. Verarbeitung in grossem Umfang (Anzahl Betroffene, Datenmenge, Dauer, geografische Reichweite)
6. Abgleich oder Zusammenfuehrung von Datensaetzen aus unterschiedlichen Quellen
7. Daten ueber schutzbeduerftige Personen (Kinder, Patienten, Beschaeftigte, Asylsuchende, aeltere Menschen)
8. Innovative Nutzung oder Anwendung neuer technologischer oder organisatorischer Loesungen (KI, Biometrie, IoT)
9. Wenn die Verarbeitung selbst die Betroffenen daran hindert, ein Recht auszuueben oder eine Dienstleistung in Anspruch zu nehmen

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Kurze, faktenfeste Beschreibung der Verarbeitung; ohne diese ist die WP-248-Pruefung Spekulation.
2. **Verhaeltnismaessigkeitspruefung.** Erste Plausibilitaet: Reicht die Verarbeitung in eines der neun Felder hinein oder nicht?
3. **Risikoanalyse Kriterien.** Jedes der neun Kriterien einzeln pruefen und mit ja oder nein beantworten, jeweils mit kurzer Begruendung. Wo Grenzfaelle bestehen, das Pro und Contra dokumentieren.
4. **Massnahmen.** Pruefen ob bereits geplante Massnahmen ein Kriterium so entkraeften, dass es nicht mehr greift (z. B. echte Anonymisierung statt Pseudonymisierung kann das Kriterium besondere Kategorien entfallen lassen).
5. **Restrisiko / Schwellwert.** Zaehlung der erfuellten Kriterien:
 - 0 Kriterien — DSFA voraussichtlich entbehrlich
 - 1 Kriterium — Grenzfall, schriftliche Begruendung der Entscheidung
 - 2 oder mehr Kriterien — DSFA zwingend
6. **Konsultation / Genehmigung.** Ergebnis dem DSB vorlegen; Aufsichtsbehoerde wird nur konsultiert, wenn nach DSFA hohes Restrisiko verbleibt (Art. 36 DSGVO).

## Mustertext / Template

```
WP-248-PRUEFUNG ZUR DSFA-PFLICHT [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]

Kriterium | Erfuellt | Begruendung
1 Scoring / Profiling / Prognose | ja/nein | [...]
2 Automatisierte Entscheidung Art. 22 DSGVO | ja/nein | [...]
3 Systematische Ueberwachung | ja/nein | [...]
4 Sensible Daten Art. 9 / Art. 10 DSGVO | ja/nein | [...]
5 Verarbeitung in grossem Umfang | ja/nein | [...]
6 Abgleich / Zusammenfuehrung | ja/nein | [...]
7 Schutzbeduerftige Personen | ja/nein | [...]
8 Neue Technologien | ja/nein | [...]
9 Verhinderung Rechtsausuebung | ja/nein | [...]

Summe erfuellter Kriterien: [X] von 9

Ergebnis
[ ] 0 — DSFA voraussichtlich entbehrlich
[ ] 1 — Grenzfall; schriftliche Entscheidung beigefuegt
[ ] 2 oder mehr — DSFA zwingend nach Art. 35 Abs. 1 DSGVO i. V. m. WP 248 rev.01

Naechster Schritt: [Vollstaendige DSFA / Dokumentation der Negativentscheidung]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Indikatoren für Kriterium 5 (grosser Umfang)

- Anzahl Betroffener absolut und relativ zur Bevoelkerung der Zielregion.
- Datenmenge pro Betroffenem (Datensaetze, Bytes, Dokumente).
- Dauer und Persistenz der Verarbeitung.
- Geografische Ausdehnung (regional, national, EU-weit, global).
- Aufbewahrungsdauer.
- Indikatorenkombinationen statt Einzelschwellen verwenden.

## Hinweise zu Kriterium 8 (neue Technologien)

- KI- und Maschinelles-Lernen-Systeme — regelmaessig einschlaegig.
- Biometrische Identifikation (Gesicht, Stimme, Fingerabdruck).
- IoT-Geraete mit personenbezogenen Sensoren.
- Verhaltensbasierte Verfahren (Tippmuster, Mausbewegung).
- Auch neue organisatorische Loesungen (z. B. neue Form der Zusammenarbeit mit Auftragsverarbeitern, neue Datenpools).

## Typische Fehler

- Kriterium 5 (grosser Umfang) wird ohne Zahlen behauptet — EDSA verlangt konkrete Indikatoren.
- Kriterium 4 wird auf Art. 9 reduziert; Standort-, Finanz- und Kommunikationsdaten werden uebersehen.
- Kriterium 8 wird auf KI beschraenkt — auch neue organisatorische Loesungen koennen einschlaegig sein.
- Begruendung wird in Floskeln gehalten — Aufsicht erwartet faktenfeste Subsumtion.
- Die Zahl 2 wird als starre Schwelle verstanden — Art. 35 Abs. 1 DSGVO kennt auch das Einzelkriterium, wenn dessen Intensitaet hoch ist.
- Negativabgrenzung fehlt — wenn Kriterium nicht erfuellt ist, muss auch das begruendet werden.
- Mehrfachzaehlung (ein Sachverhalt für zwei Kriterien) ohne Begruendung.

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md` — Trigger-Gesamtpruefung
- `datenschutzrecht/skills/dsfa-bfdi-und-laender-blacklist/SKILL.md` — Listenabgleich
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Risikoanalyse-Methodik
- `datenschutzrecht/skills/dsfa-für-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` — KI-DSFA-Schnittstelle
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- EDSA-/EDPB-Leitlinien WP 248 rev.01 — neun Kriterien
- Art. 35 Abs. 1, 2, 3 DSGVO
- Art. 70 Abs. 1 lit. e DSGVO
- EDSA-Stellungnahme 28/2024 zu KI-Modellen — Auslegungshilfe für Kriterium 8
- BfDI- und Landeslisten (live pruefen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
