# Megaprompt: tierschutzrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 100 Skills des Plugins `tierschutzrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Tierschutzrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe.
2. **eilrechtsschutz-tierhalter** — Tierschutzrecht: Eilrechtsschutz gegen Haltungsverbot. Eilrechtsschutz gegen Haltungsverbot im Fachgebiet Tierschutzrech…
3. **tierschg-grundsatz-haltung-betreuung** — Tierschutzrecht: TierSchG-Grundsatz und Leiden prüfen. TierSchG-Grundsatz und Leiden prüfen im Fachgebiet Tierschutzrech…
4. **haltung-und-betreuung-dokumentieren** — Tierschutzrecht: Haltung und Betreuung dokumentieren. Haltung und Betreuung dokumentieren im Fachgebiet Tierschutzrecht …
5. **tierschutz-strafanzeige-vorbereiten** — Tierschutzrecht: Tierschutz-Strafanzeige vorbereiten. Tierschutz-Strafanzeige vorbereiten im Fachgebiet Tierschutzrecht …
6. **tierschutzverein-handlungsoptionen** — Tierschutzrecht: Tierschutzverein Handlungsoptionen. Tierschutzverein Handlungsoptionen im Fachgebiet Tierschutzrecht al…
7. **tierhalter-zivilrechtlich-beraten** — Tierschutzrecht: Tierhalter zivilrechtlich beraten. Tierhalter zivilrechtlich beraten im Fachgebiet Tierschutzrecht als …
8. **tierarzt-und-behandlungsfehler** — Tierschutzrecht: Tierarzt und Behandlungsfehler. Tierarzt und Behandlungsfehler im Fachgebiet Tierschutzrecht als geführ…
9. **anordnung-und-wegnahme-pruefen** — Tierschutzrecht: Anordnung und Wegnahme prüfen. Anordnung und Wegnahme prüfen im Fachgebiet Tierschutzrecht als geführte…
10. **gefaehrlicher-hund-zucht-qualzucht** — Tierschutzrecht: Gefährlicher Hund Landesrecht. Gefährlicher Hund Landesrecht im Fachgebiet Tierschutzrecht als geführte…

---

## Skill: `kaltstart-triage`

_Tierschutzrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# Tierschutzrecht - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Tierschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Startfragen

1. Wer nutzt das Plugin: Laie, Verband, Kanzlei, Behörde, Unternehmen, Presse, Verwaltung oder Fachabteilung?
2. Welche Entscheidung steht jetzt an und welche Frist läuft?
3. Welche Dokumente liegen vor, welche fehlen und welche Quelle muss live geprüft werden?
4. Welche Behörde, welches Gericht, welches Register oder welcher private Akteur ist betroffen?
5. Soll am Ende ein Antrag, ein Widerspruch, eine Klage-/Eilantragslinie, ein Dashboard, ein Memo oder ein Schreiben entstehen?

## Workflow

1. Sachverhalt in Akte, Normpfad, Zuständigkeit, Frist, Beweis und Ziel zerlegen.
2. Die einschlägige Norm nicht aus dem Gedächtnis final behaupten, sondern als Live-Check gegen amtliche Quelle markieren.
3. Ablehnungs-, Kosten-, Zuständigkeits- und Beweisrisiken offen in einer Ampel führen.
4. Bei Mehr-Ebenen-Recht immer Bund, Land, Kommune, EU/international und Spezialgesetz trennen.
5. Ausgabe mit konkretem nächsten Schritt, offenen Rückfragen und einer kurzen Fassung für Nichtjuristen schließen.

## Typische Ausgaben

- Prüfvermerk mit Normpfad und Live-Check-Liste
- Fristen- und Zuständigkeitsmatrix
- Entwurf für Antrag, Widerspruch, Klagebaustein oder Behördenbrief
- Dashboard-/Tracker-Eintrag mit Status, Risiko und nächster Aktion

## Red Flags

- blindes Zitieren nicht verifizierter Rechtsprechung oder alter Gesetzesstände
- falsche Behörde, falscher Rechtsweg oder unbemerkte Spezialzuständigkeit
- Gebühren-, Frist-, Präklusions-, Geheimschutz-, Datenschutz- oder Drittbetroffenenproblem
- politisch klingende Bewertung ohne saubere Rechtsgrundlage und Beleglogik

## Quellen- und Qualitätsregel

Primär mit amtlichen Gesetzestexten, Behördenhinweisen, Gerichtsentscheidungen mit Datum/Aktenzeichen und frei prüfbaren Quellen arbeiten. Literatur, Datenbanken hinter Paywalls und Fundstellen ohne Nutzerquelle nicht behaupten. Wenn Landesrecht, EU-Recht oder ausländisches Recht berührt ist, den Rechtsstand ausdrücklich live prüfen und die Ausgabe als Arbeitsfassung kennzeichnen.

---

## Skill: `eilrechtsschutz-tierhalter`

_Tierschutzrecht: Eilrechtsschutz gegen Haltungsverbot. Eilrechtsschutz gegen Haltungsverbot im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Eilrechtsschutz Gegen Haltungsverbot

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 1 TierSchG
- § 2 TierSchG
- § 3 TierSchG
- § 4 TierSchG
- § 6 TierSchG
- § 11 TierSchG
- § 16 TierSchG
- § 17 TierSchG
- § 18 TierSchG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `tierschg-grundsatz-haltung-betreuung`

_Tierschutzrecht: TierSchG-Grundsatz und Leiden prüfen. TierSchG-Grundsatz und Leiden prüfen im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Tierschg Grundsatz Und Leiden Pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `haltung-und-betreuung-dokumentieren`

_Tierschutzrecht: Haltung und Betreuung dokumentieren. Haltung und Betreuung dokumentieren im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Haltung Und Betreuung Dokumentieren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `tierschutz-strafanzeige-vorbereiten`

_Tierschutzrecht: Tierschutz-Strafanzeige vorbereiten. Tierschutz-Strafanzeige vorbereiten im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Tierschutz Strafanzeige Vorbereiten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `tierschutzverein-handlungsoptionen`

_Tierschutzrecht: Tierschutzverein Handlungsoptionen. Tierschutzverein Handlungsoptionen im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Tierschutzverein Handlungsoptionen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `tierhalter-zivilrechtlich-beraten`

_Tierschutzrecht: Tierhalter zivilrechtlich beraten. Tierhalter zivilrechtlich beraten im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Tierhalter Zivilrechtlich Beraten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `tierarzt-und-behandlungsfehler`

_Tierschutzrecht: Tierarzt und Behandlungsfehler. Tierarzt und Behandlungsfehler im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Tierarzt Und Behandlungsfehler

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `anordnung-und-wegnahme-pruefen`

_Tierschutzrecht: Anordnung und Wegnahme prüfen. Anordnung und Wegnahme prüfen im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Anordnung Und Wegnahme Pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 1 TierSchG
- § 2 TierSchG
- § 3 TierSchG
- § 4 TierSchG
- § 6 TierSchG
- § 11 TierSchG
- § 16 TierSchG
- § 17 TierSchG
- § 18 TierSchG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `gefaehrlicher-hund-zucht-qualzucht`

_Tierschutzrecht: Gefährlicher Hund Landesrecht. Gefährlicher Hund Landesrecht im Fachgebiet Tierschutzrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Tierschutzrecht._

# Gefaehrlicher Hund Landesrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; TierSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 TierSchG` — Schutzzweck und Mitgeschoepflichkeit.
- `§ 2 TierSchG` — Haltung, Pflege, verhaltensgerechte Unterbringung.
- `§ 3 TierSchG` — Verbote.
- `§ 4 TierSchG` — Toeten von Tieren.
- `§ 6 TierSchG` — Amputation/Gewebeentnahme.
- `§ 11 TierSchG` — erlaubnispflichtige Taetigkeiten.
- `§ 16 TierSchG` — Behördenaufsicht.
- `§ 17 TierSchG` — Straftaten.
- `§ 18 TierSchG` — Ordnungswidrigkeiten.
- `§ 90a BGB` — Tiere sind keine Sachen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- TierSchG, Tierschutz-Nutztierhaltungsverordnung, EU-Tiertransport
- § 90a BGB, Sachenrecht nur entsprechend und mit Schutzlogik
- Veterinärbehörden, Anordnung, Fortnahme, Haltungserlaubnis
- Straf-/OWi-Schnittstelle, Beweis, Gutachten, Eilrechtsschutz

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 1 TierSchG
- § 2 TierSchG
- § 3 TierSchG
- § 4 TierSchG
- § 6 TierSchG
- § 11 TierSchG
- § 16 TierSchG
- § 17 TierSchG
- § 18 TierSchG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

