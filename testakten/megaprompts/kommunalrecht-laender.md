# Megaprompt: kommunalrecht-laender

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 160 Skills (gekuerzt fuer Chat-Fenster) des Plugins `kommunalrecht-laender`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Kommunalrecht der Länder: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste…
2. **kommunalrecht-mecklenburg-niedersachsen** — Kommunalrecht der Länder: Kommunalrecht Mecklenburg-Vorpommern routen. Kommunalrecht Mecklenburg-Vorpommern routen im Fa…
3. **kommunalrecht-nordrhein-westfalen-rout** — Kommunalrecht der Länder: Kommunalrecht Nordrhein-Westfalen routen. Kommunalrecht Nordrhein-Westfalen routen im Fachgebi…
4. **kommunalrecht-schleswig-holstein-route** — Kommunalrecht der Länder: Kommunalrecht Schleswig-Holstein routen. Kommunalrecht Schleswig-Holstein routen im Fachgebiet…
5. **kommunalrecht-baden-wuerttemberg-route** — Kommunalrecht der Länder: Kommunalrecht Baden-Württemberg routen. Kommunalrecht Baden-Württemberg routen im Fachgebiet K…
6. **kommunalrecht-rheinland-pfalz-routen** — Kommunalrecht der Länder: Kommunalrecht Rheinland-Pfalz routen. Kommunalrecht Rheinland-Pfalz routen im Fachgebiet Kommu…
7. **kommunalrecht-sachsen-schleswig-holstein** — Kommunalrecht der Länder: Kommunalrecht Sachsen-Anhalt routen. Kommunalrecht Sachsen-Anhalt routen im Fachgebiet Kommuna…
8. **buergerbegehren-und-buergerentscheid** — Kommunalrecht der Länder: Bürgerbegehren und Bürgerentscheid. Bürgerbegehren und Bürgerentscheid im Fachgebiet Kommunalr…

---

## Skill: `kaltstart-triage`

_Kommunalrecht der Länder: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# Kommunalrecht der Länder - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Kommunalrecht Laender** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

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

## Skill: `kommunalrecht-mecklenburg-niedersachsen`

_Kommunalrecht der Länder: Kommunalrecht Mecklenburg-Vorpommern routen. Kommunalrecht Mecklenburg-Vorpommern routen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Kommunalrecht Mecklenburg Vorpommern R

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `kommunalrecht-nordrhein-westfalen-rout`

_Kommunalrecht der Länder: Kommunalrecht Nordrhein-Westfalen routen. Kommunalrecht Nordrhein-Westfalen routen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Kommunalrecht Nordrhein Westfalen Rout

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `kommunalrecht-schleswig-holstein-route`

_Kommunalrecht der Länder: Kommunalrecht Schleswig-Holstein routen. Kommunalrecht Schleswig-Holstein routen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Kommunalrecht Schleswig Holstein Route

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `kommunalrecht-baden-wuerttemberg-route`

_Kommunalrecht der Länder: Kommunalrecht Baden-Württemberg routen. Kommunalrecht Baden-Württemberg routen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Kommunalrecht Baden Wuerttemberg Route

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `kommunalrecht-rheinland-pfalz-routen`

_Kommunalrecht der Länder: Kommunalrecht Rheinland-Pfalz routen. Kommunalrecht Rheinland-Pfalz routen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Kommunalrecht Rheinland Pfalz Routen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `kommunalrecht-sachsen-schleswig-holstein`

_Kommunalrecht der Länder: Kommunalrecht Sachsen-Anhalt routen. Kommunalrecht Sachsen-Anhalt routen im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Kommunalrecht Sachsen Anhalt Routen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Skill: `buergerbegehren-und-buergerentscheid`

_Kommunalrecht der Länder: Bürgerbegehren und Bürgerentscheid. Bürgerbegehren und Bürgerentscheid im Fachgebiet Kommunalrecht der Länder als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten im Kommunalrecht._

# Buergerbegehren Und Buergerentscheid

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GO der Länder, KomVG, KAG, GG Art. 28, BauGB, VwGO, KomHV-Doppik — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 28 Abs. 2 GG` — kommunale Selbstverwaltung.
- `§ 35 Satz 1 VwVfG` — Verwaltungsakt als Handlungsform.
- `§ 40 VwVfG` — Ermessensausübung.
- `§ 47 Abs. 1 VwGO` — Normenkontrolle gegen Satzungen, soweit landesrechtlich eroeffnet.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.
- `§ 1 Abs. 1 KAG` — Kommunalabgabenrecht als Landesrecht live pruefen.
- `§ 2 Abs. 1 KAG` — Satzungserfordernis im Abgabenrecht live nach Landesrecht pruefen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.
- Gemeindeordnungen, Landkreisordnungen, Kommunalverfassungen der Länder
- Rat/Kreistag, Bürgermeister/Landrat, Ausschüsse, Bürgerbegehren
- Kommunalaufsicht, Haushalt, Abgaben, Daseinsvorsorge, Satzungen
- VwGO, § 47 VwGO, Kommunalwahlrecht-Schnittstellen

## Prüfroutine

1. **Scope:** Was genau soll entschieden, beantragt, abgewehrt oder dokumentiert werden? Welche Einheit ist betroffen und welches Recht gilt wirklich?
2. **Zuständigkeit:** Behörde, Gericht, Register, Aufsicht, Verband, Unternehmen oder internationale Stelle sauber benennen; falsche Adressaten als Risiko ausweisen.
3. **Tatbestand:** Die relevanten Merkmale einzeln mit Belegen füllen. Unklare Tatsachen als Rückfrage oder Beweispunkt markieren, nicht glattbügeln.
4. **Rechtsfolge:** Anspruch, Ermessen, Verbot, Pflicht, Gebührenfolge, Nebenfolge, Haftung, Vollzug oder Rechtsschutz getrennt ausgeben.
5. **Taktik:** Schnellster sinnvoller Weg, sauberster Weg und Eskalationsweg nebeneinander stellen; bei Laien zusätzlich eine kurze Erklärung in Alltagssprache.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

