---
name: dsfa-art-35-dsgvo-trigger-anwendungsbereich
description: "Pruefung wann eine DSFA nach Art. 35 DSGVO ueberhaupt erforderlich ist. Trigger-Pruefung Anwendungsbereich Schwellwert. Generalklausel Art. 35 Abs. 1 voraussichtlich hohes Risiko; Regelbeispiele Art. 35 Abs. 3; Pflichtlisten Art. 35 Abs. 4 BfDI. Output: Triage-Vermerk DSFA-pflichtig oder nicht."
---

# DSFA Trigger und Anwendungsbereich nach Art. 35 DSGVO

## Zweck

Dieser Skill liefert eine strukturierte Erstpruefung der Frage, ob für eine konkrete Verarbeitungstaetigkeit eine Datenschutz-Folgenabschaetzung (DSFA) nach Art. 35 DSGVO durchzufuehren ist. Ergebnis ist ein Triage-Vermerk mit klarer Aussage DSFA-pflichtig, optional oder entbehrlich und einer Begruendung mit Norm-Anker.

## Wann dieses Modul hilft

- Vor Einfuehrung einer neuen Verarbeitungstaetigkeit
- Bei wesentlicher Aenderung einer bestehenden Verarbeitung (Art. 35 Abs. 11 DSGVO)
- Bei Aufnahme eines neuen Auftragsverarbeiters, neuer Technologie oder neuer Datenkategorie
- Wenn die interne Compliance, der DSB oder eine Aufsichtsbehoerde die Frage stellt
- Vor Erstellung einer vollstaendigen DSFA (Vorab-Triage)

## Rechtlicher Rahmen

- Art. 35 Abs. 1 DSGVO Generalklausel: DSFA verpflichtend wenn eine Form der Verarbeitung, insbesondere bei Verwendung neuer Technologien, aufgrund Art, Umfang, Umstaenden und Zwecken voraussichtlich ein hohes Risiko für die Rechte und Freiheiten natuerlicher Personen zur Folge hat.
- Art. 35 Abs. 3 DSGVO Regelbeispiele:
 - lit. a systematische und umfassende Bewertung persönlicher Aspekte einschliesslich Profiling und darauf gestuetzter automatisierter Entscheidung mit Rechtswirkung
 - lit. b umfangreiche Verarbeitung besonderer Kategorien nach Art. 9 Abs. 1 oder von Daten ueber strafrechtliche Verurteilungen nach Art. 10
 - lit. c systematische umfangreiche Ueberwachung oeffentlich zugaenglicher Bereiche
- Art. 35 Abs. 4 DSGVO Pflichtliste der Aufsichtsbehoerde (BfDI bzw. zuständige Landesbehoerde) — sogenannte Blacklist.
- Art. 35 Abs. 5 DSGVO optionale Whitelist der Aufsichtsbehoerde.
- Art. 35 Abs. 10 DSGVO Ausnahme bei gesetzlicher Grundlage mit bereits durchgefuehrter allgemeiner DSFA durch den Gesetzgeber.
- EDSA-Leitlinien WP 248 rev.01 (uebernommen durch EDSA), insbesondere die 9 Kriterien zur Bestimmung von voraussichtlich hohem Risiko.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Kurzbeschreibung der Verarbeitung in maximal 10 Saetzen: Zweck, Datenarten, Betroffenenkreise, Technologie, Drittlandbezug, Aufbewahrung. Ohne diese Beschreibung ist die Trigger-Pruefung nicht moeglich.
2. **Verhaeltnismaessigkeitspruefung.** In dieser Stufe nur grobe Plausibilitaet: Liegt ein offensichtliches Missverhaeltnis von Zweck und Eingriff vor? Falls ja, ist die DSFA bereits aus diesem Grund angezeigt.
3. **Risikoanalyse Trigger-Ebene.** Pruefen der 9 EDSA-Kriterien:
 - Bewertung oder Scoring
 - automatisierte Entscheidung mit Rechtswirkung
 - systematische Ueberwachung
 - besondere Kategorien Art. 9 oder Art. 10
 - umfangreiche Verarbeitung
 - Zusammenfuehrung oder Abgleich von Datensaetzen
 - schutzbeduerftige Personen (Kinder, Patienten, Beschaeftigte)
 - neue Technologien (KI, Biometrie, IoT)
 - Verhinderung der Ausübung von Betroffenenrechten
4. **Massnahmen.** Pruefen ob bereits getroffene risikomindernde Massnahmen den Schwellwert unter hohes Risiko druecken (Pseudonymisierung, Anonymisierung, technische Beschraenkung). Ergebnis dokumentieren.
5. **Restrisiko / Schwellwertergebnis.** Drei moegliche Ergebnisse:
 - DSFA-PFLICHTIG (Art. 35 Abs. 3, Abs. 4 oder mindestens 2 EDSA-Kriterien)
 - DSFA-EMPFOHLEN (1 EDSA-Kriterium, Grenzfall)
 - DSFA-ENTBEHRLICH (kein Kriterium erfuellt, Blacklist nicht einschlaegig)
6. **Konsultation / Genehmigung.** DSB nach Art. 35 Abs. 2 DSGVO anhoeren. Triage-Vermerk gegenzeichnen lassen und in Verarbeitungsverzeichnis nach Art. 30 verlinken.

## Mustertext / Template

```
DSFA-TRIAGE-VERMERK [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME, ROLLE]
Vorpruefer: [NAME] | DSB-Anhörung: [DATUM]

1. Kurzbeschreibung
[Zweck, Datenarten, Betroffene, Technologie, Drittlandbezug, Aufbewahrung]

2. Pruefung Art. 35 Abs. 3 DSGVO (Regelbeispiele)
- lit. a Profiling mit Rechtswirkung: ja / nein — [Begruendung]
- lit. b besondere Kategorien umfangreich: ja / nein — [Begruendung]
- lit. c öffentlicher Bereich Ueberwachung: ja / nein — [Begruendung]

3. Pruefung Art. 35 Abs. 4 DSGVO BfDI-/Landes-Blacklist
- Einschlaegig: ja / nein — [Listen-Position]

4. EDSA-Kriterien WP 248 rev.01 (Anzahl erfuellt)
- [X] von 9

5. Ergebnis
[ ] DSFA PFLICHTIG nach Art. 35 [Abs. 1 / Abs. 3 / Abs. 4]
[ ] DSFA EMPFOHLEN (Grenzfall, Dokumentation der Nicht-DSFA)
[ ] DSFA ENTBEHRLICH (Dokumentation der Begruendung)

6. Naechster Schritt
[ ] Vollstaendige DSFA durchfuehren (Skill dsfa-template-deutsch-vollvorlage)
[ ] Negative Triage-Dokumentation ablegen (Art. 5 Abs. 2 DSGVO Rechenschaftspflicht)

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Typische Fehler

- Triage wird muendlich erledigt, kein Vermerk angelegt — Verstoss gegen Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO.
- Nur Art. 35 Abs. 3 geprueft, Generalklausel Abs. 1 uebersehen — auch ausserhalb der Regelbeispiele kann DSFA-Pflicht bestehen.
- Blacklist der eigenen Landesbehoerde uebersehen (siehe Skill dsfa-bfdi-und-laender-blacklist).
- Negative Triage nicht dokumentiert — bei spaeterem Aufsichtsverfahren kein Nachweis.
- DSB nicht beteiligt obwohl Art. 35 Abs. 2 ausdruecklich Anhörung verlangt.
- Wesentliche Aenderung uebersehen — Re-Triage nach Art. 35 Abs. 11 notwendig.

## Querverweise

- `datenschutzrecht/skills/dsfa-bfdi-und-laender-blacklist/SKILL.md` — Blacklist-Abgleich
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md` — EDSA-Kriterien im Detail
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage nach positiver Triage
- `datenschutzrecht/skills/dsfa-typische-fehler-bei-erstpruefung/SKILL.md` — Fehlerquellen Erstpruefung
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Plugin-weite Triage
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36 DSGVO (Verordnung EU 2016/679)
- Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht)
- § 67 BDSG (Pflichtliste BfDI)
- EDSA-Leitlinien WP 248 rev.01 zur DSFA
- BfDI: bfdi.bund.de — aktuelle Blacklist und Whitelist live pruefen
- Landesdatenschutzbehoerden (LfDI BW, LDA Bayern u.a.) — eigene Listen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle oder lizenziertem Live-Zugriff
