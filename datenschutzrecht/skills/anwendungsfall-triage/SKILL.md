---
name: anwendungsfall-triage
description: "Für Datenschutz-Triage neuer Verarbeitungsvorgänge: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Datenschutz-Triage neuer Verarbeitungsvorgänge

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Eingaben

- Beschreibung des Verarbeitungsvorgangs (Datenarten, Zweck, Betroffenenkreis)
- Datenkategorien (Art. 4 Nr. 1, Art. 9 DSGVO); Beschäftigtendaten (§ 26 BDSG)?
- Neu erhoben oder Zweckänderung bei vorhandenen Daten (Art. 5 Abs. 1 lit. b DSGVO)?
- Auftragsverarbeiter / Drittland-Übermittlung?
- Automatisierte Entscheidungsfindung (Art. 22 DSGVO)?
- Cookies / Endgerätezugriff (§§ 24 ff. TDDDG)?

## Rechtlicher Rahmen

### Kernvorschriften

- **DSGVO:** Art. 5 (Grundsätze), Art. 6 (Rechtsgrundlagen), Art. 9 (besondere
 Kategorien), Art. 13/14 (Informationspflichten), Art. 17 (Löschrecht), Art. 22
 (automatisierte Entscheidungen), Art. 25 (Privacy by Design/Default), Art. 28 (AVV),
 Art. 30 (Verarbeitungsverzeichnis), Art. 32 (TOM), Art. 35 (DSFA), Art. 44 ff.
 (Drittlandtransfer).
- **BDSG:** § 22 (Gesundheits-/Sozialdaten), § 26 (Beschäftigtendatenschutz), § 38
 (betrieblicher DSB).
- **TDDDG (ehem. TTDSG):** §§ 24 ff. — Einwilligung für Cookies/Endgerätezugriffe.
- **Art. 35 Abs. 4 DSGVO** i. V. m. DSK-Positivliste — nationale Pflichttatbestände.

### Leitentscheidungen

 — Ungültigkeit EU-US-Privacy-Shield; Standardvertragsklauseln erfordern Transfer
 Impact Assessment; maßgeblich für Art. 44 ff. DSGVO.
 — Automatisiertes Scoring als Entscheidung i. S. d. Art. 22 DSGVO, wenn Dritte
 maßgeblich darauf abstellen; zentral für Triage von KI-/Scoring-Vorhaben.
 — Datenschutzrechtliche Haftung Art. 82 DSGVO; Beweislastverteilung.
 *(Recht auf Vergessen I)* — Datenschutz als Teil des allgemeinen Persönlichkeitsrechts
 (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG); Abwägung mit Kommunikationsfreiheiten.

### Kommentare

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 — DSFA-Pflicht, Schwellenwerte, Verhältnis zu nationalen Listen.
- `Simitis/Hornung/Spiecker (Hrsg.), DSGVO, 2. Aufl. 2022, Art. 6 Rn. 30 ff.`
 — Rechtsgrundlagen; berechtigtes Interesse als Auffangtatbestand.
- `Gola (Hrsg.), DSGVO, 3. Aufl. 2022, Art. 22 Rn. 5 ff.`
 — Automatisierte Entscheidungsfindung; Abgrenzung zu Profiling.
- `Paal/Pauly (Hrsg.), DS-GVO BDSG, 3. Aufl. 2021, Art. 25 DSGVO Rn. 7 ff.`
 — Privacy by Design und Privacy by Default als Entwurfspflicht.
- `Ehmann/Selmayr (Hrsg.), DS-GVO, 2. Aufl. 2018, Art. 35 Rn. 25 ff.`
 — Anwendungsbereich der DSFA; Verhältnis zu Art. 5, 25 DSGVO.

## Ablauf

### Schritt 1: Verarbeitungsvorgang klären

Bei vager Beschreibung zuerst nachfragen: Datenkategorien (Art. 9?), Betroffenenkreis
(Beschäftigte → § 26 BDSG!), Zweck, Neu oder Zweckänderung, Auftragsverarbeiter,
automatisierte Entscheidung (Art. 22), Endgerätezugriff (§ 24 TDDDG).

### Schritt 2: Hausinternes DSA-Raster

Konfiguriertes Prüfraster aus CLAUDE.md lesen. Trigger erfüllt → mindestens
**DSA ERFORDERLICH**. Nicht erfüllt → weiter mit Schritt 3.

### Schritt 3: DSFA-Pflichtprüfung (Art. 35 DSGVO)

**Pflichttatbestände (Art. 35 Abs. 3, DSK-Positivliste):**
- Systematische automatisierte Bewertung persönlicher Aspekte inkl. Profiling mit
- Umfangreiche Verarbeitung besonderer Datenkategorien (Art. 9 DSGVO).
- Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche.

**Starke Indikatoren (kein Pflichttatbestand, aber DSFA dringend empfohlen):**
neue Technologie, Kinderdaten, Zusammenführung getrennter Datensätze,
Diskriminierungspotenzial, Cross-Context-Tracking, verhaltensbasierte Werbung.

Pflichttatbestand erfüllt → **DSFA PFLICHT**. Nur Indikatoren → **DSA ERFORDERLICH**.

### Schritt 4: Datenschutzrichtlinien-Abgleich

Vorhaben gegen konfigurierte Richtlinien prüfen. Typische Konflikte:
Datenkategorie nicht in Richtlinie erfasst; Drittlandweitergabe ohne Grundlage
(Art. 44 ff. DSGVO); Löschfristen (Art. 17) überschritten; Zweckbindung (Art. 5
Abs. 1 lit. b) verletzt; Betroffenenrechte unvollständig.

Direkter Konflikt → **STOPP**. Konflikt muss aufgelöst sein vor Fortführung.

### Schritt 5: Klassifikation und Ausgabe

```
Kurzergebnis: [DSFA PFLICHT / DSA ERFORDERLICH / FREIGABE / STOPP — ein Satz]

VORGANG: [wie verstanden]
KLASSIFIKATION: [...]
Hausinternes DSA-Raster ausgelöst? [Ja / Nein]
DSFA-Pflicht (Art. 35 DSGVO)? [Ja — Tatbestand / Nein / N/A]
Richtlinienkonflikt? [Keiner / Ja — konkreter Konflikt]
Begründung: [1–3 Sätze]
```

*Voraussetzungen bei DSA / DSFA:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| Datenschutzprüfung / DSFA (Art. 35 DSGVO) | DSB | ☐ |
| Berechtigtes-Interesse-Abwägung (Art. 6 Abs. 1 lit. f) | DSB / Legal | ☐ |
| DSB-Konsultation (DSFA-Pflichtverfahren) | DSB | ☐ |
| AVV (Art. 28 DSGVO) | Legal | ☐ |
| Richtlinienaktualisierung vor Launch | DSB | ☐ |
| Eintrag Verarbeitungsverzeichnis (Art. 30) | DSB | ☐ |

**Rechtsgrundlage (Art. 6 DSGVO):** [lit. a Einwilligung / lit. b Vertrag /
lit. c rechtliche Verpflichtung / lit. f berechtigte Interessen — oder "unklar"]

Nach Klassifikation immer anbieten: "Soll ich jetzt direkt mit der DSFA beginnen?"

*Bei STOPP:*
Konflikt benennen. Optionen: (A) Vorhaben umgestalten, (B) Richtlinie aktualisieren
(Vereinbarkeit mit Rechtsgrundlage prüfen). Keinen Weg vorschlagen, wenn keiner besteht.

### Schritt 6: Weiterleitung

 KI-Folgenabschätzung erwägen.
- **Beschäftigtendatenschutz:** § 26 BDSG und Mitbestimmung (§§ 87 Abs. 1 Nr. 6,
 94 BetrVG) prüfen.

## Beispiel

**Vorgang:** ML-basiertes Kreditscoring für Bestandskunden; Ergebnis fließt in
automatisierte Kreditentscheidung.

**Klassifikation:** DSFA PFLICHT — Art. 35 Abs. 3 lit. a DSGVO: systematische
automatisierte Bewertung persönlicher Aspekte mit erheblichen Auswirkungen
(Schufa-Scoring) reicht es, dass Dritte maßgeblich auf das Scoring abstellen.
DSB-Konsultation und Verarbeitungsverzeichnis-Eintrag (Art. 30) zwingend.

## Risiken und typische Fehler

- **"Anonymisiert" = FREIGABE:** Pseudonymisierte Daten bleiben personenbezogen
 (Art. 4 Nr. 1 DSGVO). Re-Identifikationsrisiko konkret prüfen.
- **"Wir machen das ähnlich":** Bestehende, nie geprüfte Verarbeitungen legitimieren
 keine neue. Bei anderem Umfang/Zweck/Kategorie: neu triagen.
- **"Nur ein Pilot":** Pilot mit echten Personendaten unterliegt denselben Anforderungen.
- **"Der Anbieter regelt Datenschutz":** AVV nach Art. 28 zwingend; Triage bleibt beim
 Verantwortlichen (Art. 4 Nr. 7 DSGVO).
- **Inferred Data übersehen:** Score, Risikoklasse, Präferenz = personenbezogenes Datum.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jede Klassifikation muss nennen: einschlägige DSGVO-/BDSG-Normen mit Artikel/Absatz,
DSK-Listenfundstelle bei DSFA-Pflicht, einschlägige Rechtsprechung in korrekter
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

Beispiel Rechtsprechung:

Beispiel Kommentar:
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen der DSK-Blacklist/Whitelist (Art. 35 Abs. 4/5 DSGVO), neuen EDSA-Leitlinien zur DSFA sowie KI-VO-Umsetzungsakten.

**Querverweise:**
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — vollständige DSFA bei positiver Triage
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — bei Drittlandbezug in der Triage
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — bei Auftragsverarbeitung als Verarbeitungsbestandteil

## Output-Template — Triage-Ergebnis

**Adressat:** Datenschutzbeauftragter / Prozessverantwortlicher — Tonfall: sachlich-strukturiert

```
Datenschutz-Triage-Ergebnis [DATUM]
Verarbeitungsvorgang: [BEZEICHNUNG]
Beschreibung: [KURZBESCHREIBUNG]

Einstufung: FREIGABE / DSA ERFORDERLICH / DSFA PFLICHT / STOPP

Rechtsgrundlage: Art. [X] DSGVO [§ BDSG optional]
Verantwortlichkeit: Art. 24 (allein) / Art. 26 (gemeinsam) / Art. 28 (Auftragsverarbeitung)
Drittlandbezug: ja (→ Drittlandprüfung) / nein
DSFA-Pflicht: ja (Grund: [...]) / nein (Begründung: [...])

Naechste Schritte:
1. [AKTION]
2. [AKTION]

Frist: [DATUM]
Verantwortlich: [PERSON / ROLLE]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
