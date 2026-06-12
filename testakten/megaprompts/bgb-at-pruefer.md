# Megaprompt: bgb-at-pruefer

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 83 Skills des Plugins `bgb-at-pruefer`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im BGB-AT-Prüfer. Fragt Fallfrage, Rolle, Anspruchsziel, Tatsachen, Fristen, Erk…
2. **klausurloesungen-fehlerdiagnose-konsens** — Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüf…
3. **stellvertretung-routing-paragraphen-164-181** — Routing-Skill zur Stellvertretung nach §§ 164 bis 181 BGB: Vollmachtserteilung und -erlöschen, Offenkundigkeit des Hande…
4. **klausurloesungen-fehlerdiagnose** — Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüf…
5. **vertragsschluss-antrag-abgabe** — Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschun…
6. **rechtlich-vorteilhaft-paragraph-107** — Klausurfall zu lediglich rechtlich vorteilhaften Rechtsgeschäften nach § 107 BGB: Minderjähriger erwirbt ohne Einwilligu…
7. **invitatio-ad-offerendum-und-werbung** — Klausurfall zur Abgrenzung von Angebot und invitatio ad offerendum nach §§ 145 bis 147 BGB: Werbung im Schaufenster und …
8. **willenserklaerung-wucher-ausbeutung-zugang** — Klausurfall zum Tatbestand der Willenserklärung: objektiver Erklärungstatbestand, Rechtsbindungswille, Erklärungsbewusst…
9. **vertreter-ohne-vertretungsmacht-paragraphen-177-179** — Klausurfall zum vollmachtlosen Vertreter nach §§ 177 bis 179 BGB: schwebende Unwirksamkeit des Vertreterhandelns, Genehm…
10. **vertragsschluss-antrag-annahme** — Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschun…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im BGB-AT-Prüfer. Fragt Fallfrage, Rolle, Anspruchsziel, Tatsachen, Fristen, Erklärungen, Beteiligte und Wunsch-Output ab, baut einen schönen Arbeitsplan und schlägt passende Fachmodule aus diesem Plugin vor._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Bgb At Pruefer** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normanker

BGB AT insgesamt. Bei tragenden Normen `amtlicher-bgb-zpo-normcheck` zuschalten und den aktuellen Gesetzestext prüfen, insbesondere bei §§ 104-113, 116-124, 125-130, 133-157, 164-185, 186-218 BGB sowie bei ZPO-Schnittstellen zu §§ 130a, 130d, 130e, 166-190, 222, 371a ZPO.

## Intake

- Welche Rolle hat die Nutzerin oder der Nutzer: Kanzlei, Rechtsabteilung, Ausbildung, Gerichtsvorbereitung oder Selbststudium?
- Was ist das konkrete Arbeitsziel: Anspruchsprüfung, Memo, Klausurlösung, Schriftsatzbaustein, Fristenvermerk oder Rückfragenkatalog?
- Welche Tatsachen sind belegt, welche sind nur Behauptung, welche fehlen noch?
- Welche Daten, Uhrzeiten, Erklärungen, Vollmachten, Formvorgaben und Fristen sind im Sachverhalt erkennbar?

## Prüfraster

1. Fallziel und Anspruchsebene bestimmen
2. Personen, Erklärungen, Zeitpunkte und Dokumente erfassen
3. Themenkarte zu Geschäftsfähigkeit, Vertragsschluss, Zugang, Form, Anfechtung, Stellvertretung und Verjährung bauen
4. zwei bis fünf Fachmodule mit Grund und erwartetem Output vorschlagen
5. Ergebnis mit Norm, Tatbestandsmerkmal, Subsumtion und Rechtsfolge festhalten.
6. Offene Tatsachen als Rückfrage formulieren und nicht durch Vermutung ersetzen.

## Anschluss-Skills

- bgb-at-fallaufnahme-und-pruefprogramm
- anspruchsaufbau-zivilrecht-bgb-at
- vertragsschluss-antrag-annahme
- anfechtung-routing
- stellvertretung-routing-paragraphen-164-181
- elektronische-form-bea-qes-formfiktion
- verjaehrung-grundschema-paragraphen-194-218
- amtlicher-bgb-zpo-normcheck

---

## Skill: `klausurloesungen-fehlerdiagnose-konsens`

_Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüfungsreihenfolge (Auslegung vor Anfechtung), übersehene Normen wie § 122 BGB und § 179 BGB, unvollständige Subsumtion. Output: annotiertes Feedback und Verbesserungsvorschläge im..._

# Klausurlösungen — Fehlerdiagnose und Verbesserung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Examenskandidat hat Klausurlösung zu § 119 BGB eingereicht — Auslegung fehlt, Motivirrtum als Anfechtungsgrund gewertet.
- Student prüft § 164 BGB ohne Offenkundigkeit zu erörtern und übersieht den vollmachtlosen Vertreter.
- Klausurkonstellation: Gutachtenstil-Mängel — Ergebnis steht vor Begründung, Normen fehlen.

## Erste Schritte

1. Prüfungsreihenfolge kontrollieren: Anspruchsgrundlage — Tatbestand — Subsumtion — Ergebnis.
2. Vorrang der Auslegung (§§ 133 und 157 BGB) vor Anfechtung, Dissens und Lückenfüllung prüfen.
3. Übersehene Normen identifizieren: § 122 BGB bei Anfechtung, § 179 BGB bei Vertretung ohne Vollmacht.
4. Subsumtion auf Vollständigkeit prüfen: Norm — Tatbestandsmerkmal — Sachverhalt — Rechtsfolge.
5. Gutachtenstil vs. Urteilsstil: Im Gutachten Ergebnis nicht vorwegnehmen.
6. Feedback formulieren: konkret, normenbezogen, mit Korrekturanweisung.

## Rechtsrahmen

- §§ 133 und 157 BGB: Auslegung als vorrangige Prüfungsstufe.
- § 119 BGB: Anfechtungsrecht — Irrtumskategorien und Motivirrtum.
- § 122 BGB: Schadensersatzpflicht des Anfechtenden — häufig übersehen.
- § 164 BGB: Stellvertretung — Offenkundigkeit als Tatbestandsmerkmal.
- § 179 BGB: Haftung des Vertreters ohne Vertretungsmacht.

## Prüfraster

1. Aufbaurüge: Entspricht die Prüfungsstruktur dem Anspruchsaufbau (Wer will was von wem woraus)?
2. Auslegungsvorrang: Wurde Auslegung vor Anfechtung und Dissens geprüft?
3. Normzitate: Sind alle einschlägigen Normen genannt und korrekt zitiert?
4. Subsumtion: Ist jedes Tatbestandsmerkmal auf den Sachverhalt angewendet?
5. Rechtsfolge: Ist die Rechtsfolge der einschlägigen Norm korrekt benannt?
6. Gutachtenstil-Einhaltung: Kein Ergebnis vor Begründung im Obersatz.
7. Fehlende Folgeprüfungen (§§ 122 und 179 BGB) ergänzt?

## Typische Fallstricke

- Motivirrtum als Anfechtungsgrund nach § 119 Abs. 1 BGB zu werten ist ein klassischer Fehler.
- § 122 BGB wird systematisch übersehen — immer nach erfolgreicher Anfechtung prüfen.
- Offenkundigkeit bei § 164 BGB fehlt häufig — kein Stellvertretungseffekt ohne sie.
- Urteilsstil in Klausuren verwenden statt Gutachtenstil ist ein Bewertungsmangel.

## Quellen

- [§ 133 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__133.html)
- [§ 119 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__119.html)
- [§ 122 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__122.html)
- [§ 179 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [dejure.org § 164 BGB](https://dejure.org/gesetze/BGB/164.html)

## Vertiefung

### Systematisches Fehler-Tracking

Für die Klausurvorbereitung empfiehlt sich ein persönliches Fehlerprotokoll: Welche Normen werden
regelmäßig übersehen? Wo fehlt die Subsumtion? Wo wird der Gutachtenstil verletzt? Systematische
Wiederholung der häufigsten Fehler beschleunigt den Lernfortschritt erheblich.

### Punktgewichtung in der Klausur

BGB-AT-Klausuren gewichten: Anspruchsaufbau (5-10 %), Tatbestandsprüfung (40-50 %), Subsumtion
(20-30 %), Ergebnis (5-10 %), Gutachtenstil (10-20 %). Fehler in der Subsumtion kosten die meisten
Punkte.

### Klausur-Checkliste Fehlerdiagnose

- Falsche Anspruchsgrundlage gewählt?
- Auslegung vor Anfechtung unterlassen?
- Tatbestandsmerkmale unvollständig oder falsch definiert?
- § 122 BGB nach Anfechtung übersehen?
- Gutachtenstil verletzt (Ergebnis vor Begründung)?

---

## Skill: `stellvertretung-routing-paragraphen-164-181`

_Routing-Skill zur Stellvertretung nach §§ 164 bis 181 BGB: Vollmachtserteilung und -erlöschen, Offenkundigkeit des Handelns im fremden Namen, Duldungs- und Anscheinsvollmacht, Vertreter ohne Vertretungsmacht §§ 177 bis 179 BGB und Insichgeschäft § 181 BGB. Output: Prüfpfad und Verweis auf Teilski..._

# Stellvertretung — Routing §§ 164 bis 181 BGB

## Mandantenfall

- Mitarbeiter schließt ohne ausdrückliche Vollmacht Vertrag ab — Vollmacht, Duldungs- oder Anscheinsvollmacht?
- Prokurist überschreitet seine Vollmacht — §§ 177 bis 179 BGB oder Missbrauch der Vertretungsmacht?
- Klausurkonstellation: Komplexes Stellvertretungsproblem mit mehreren Fragen — Routing zum richtigen Teilskill.

## Erste Schritte

1. Handeln in fremdem Namen prüfen: Offenkundigkeit nach § 164 Abs. 1 BGB gegeben?
2. Vollmacht identifizieren: Innen- oder Außenvollmacht, Prokura, gesetzliche Vertretung?
3. Vollmachtsumfang: Reicht die Vollmacht für das konkrete Geschäft aus?
4. Bei fehlender Vollmacht: Duldungs- oder Anscheinsvollmacht als Rechtsscheintatbestand?
5. Vollmachtsmissbrauch: Handeln im Außenverhältnis mit Vollmacht, aber gegen Innenverhältnis?
6. Vertreter ohne Vertretungsmacht: §§ 177 bis 179 BGB — schwebende Unwirksamkeit und Haftung.

## Rechtsrahmen

- § 164 BGB: Stellvertretung — Handeln im fremden Namen mit Vertretungsmacht.
- § 167 BGB: Vollmachtserteilung — Innen- und Außenvollmacht.
- § 168 BGB: Erlöschen der Vollmacht.
- §§ 177 bis 179 BGB: Vertretung ohne Vertretungsmacht und Haftung des Vertreters.
- § 181 BGB: Insichgeschäft — Selbstkontrahieren und Mehrfachvertretung.

## Prüfraster

1. Offenkundigkeit (§ 164 Abs. 1 BGB): Im fremden Namen oder im eigenen Namen gehandelt?
2. Vollmacht vorhanden: Innen- oder Außenvollmacht, Prokura oder gesetzliche Vertretung?
3. Vollmachtsumfang: Geschäft vom Umfang der Vollmacht gedeckt?
4. Duldungs- oder Anscheinsvollmacht: Rechtsscheintatbestand und Zurechenbarkeit?
5. Vollmachtsmissbrauch: Kenntnis/Kennenmüssen des Dritten vom Innenverhältnis-Verstoß?
6. § 177 BGB: Genehmigung schwebend unwirksamen Vertreterhandelns?
7. § 179 BGB: Haftung des vollmachtlosen Vertreters gegenüber Drittem?
8. § 181 BGB: Insichgeschäft — Ausnahmen beachten?

## Typische Fallstricke

- Offenkundigkeit nach § 164 BGB ist Voraussetzung — Namensnennung nicht immer erforderlich.
- Duldungsvollmacht setzt voraus, dass der Vertretene das Handeln kannte und duldete.
- Anscheinsvollmacht erfordert, dass der Vertretene das Erscheinungsbild hätte erkennen und verhindern können.
- § 181 BGB ist abdingbar durch ausdrückliche Gestattung — Ausnahme prüfen.

## Quellen

- [§ 164 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__164.html)
- [§ 167 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__167.html)
- [§ 179 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [dejure.org § 164 BGB](https://dejure.org/gesetze/BGB/164.html)
- [dejure.org § 181 BGB](https://dejure.org/gesetze/BGB/181.html)

## Vertiefung

### Prüfungsreihenfolge Stellvertretung

Empfohlene Reihenfolge: (1) Offenkundigkeit nach § 164 Abs. 1 BGB, (2) Vertretungsmacht
(Vollmacht, Prokura, gesetzliche Vertretung), (3) Vollmachtsumfang, (4) Handeln im Rahmen
der Vollmacht, (5) Ausnahmen: Duldungs-/Anscheinsvollmacht, (6) Vollmachtloser Vertreter
(§§ 177 bis 179 BGB), (7) Insichgeschäft (§ 181 BGB).

### Routing-Logik

Dient als Einstiegspunkt. Bei komplexen Stellvertretungsfragen werden die spezifischen
Teilskills aufgerufen: vollmacht-erteilung-umfang-erloeschen für Vollmachtsfragen,
duldungs-anscheinsvollmacht für Rechtsschein, insichgeschaeft-paragraph-181 für § 181 BGB.

### Klausur-Checkliste Routing

- Einstieg: Offenkundigkeit und Vollmacht als erste Prüfungspunkte?
- Vollmacht vorhanden: Umfang ausreichend für das konkrete Geschäft?
- Vollmacht fehlend: Rechtsschein (Duldung/Anschein) oder vollmachtloser Vertreter?
- Insichgeschäft: § 181 BGB mit Ausnahmen geprüft?
- Richtiger Teilskill für Detailprüfung ausgewählt?

---

## Skill: `klausurloesungen-fehlerdiagnose`

_Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüfungsreihenfolge (Auslegung vor Anfechtung), übersehene Normen wie § 122 BGB und § 179 BGB, unvollständige Subsumtion. Output: annotiertes Feedback und Verbesserungsvorschläge._

# Klausurlösungen — Fehlerdiagnose und Verbesserung

## Mandantenfall

- Examenskandidat hat Klausurlösung zu § 119 BGB eingereicht — Auslegung fehlt, Motivirrtum als Anfechtungsgrund gewertet.
- Student prüft § 164 BGB ohne Offenkundigkeit zu erörtern und übersieht den vollmachtlosen Vertreter.
- Klausurkonstellation: Gutachtenstil-Mängel — Ergebnis steht vor Begründung, Normen fehlen.

## Erste Schritte

1. Prüfungsreihenfolge kontrollieren: Anspruchsgrundlage — Tatbestand — Subsumtion — Ergebnis.
2. Vorrang der Auslegung (§§ 133 und 157 BGB) vor Anfechtung, Dissens und Lückenfüllung prüfen.
3. Übersehene Normen identifizieren: § 122 BGB bei Anfechtung, § 179 BGB bei Vertretung ohne Vollmacht.
4. Subsumtion auf Vollständigkeit prüfen: Norm — Tatbestandsmerkmal — Sachverhalt — Rechtsfolge.
5. Gutachtenstil vs. Urteilsstil: Im Gutachten Ergebnis nicht vorwegnehmen.
6. Feedback formulieren: konkret, normenbezogen, mit Korrekturanweisung.

## Rechtsrahmen

- §§ 133 und 157 BGB: Auslegung als vorrangige Prüfungsstufe.
- § 119 BGB: Anfechtungsrecht — Irrtumskategorien und Motivirrtum.
- § 122 BGB: Schadensersatzpflicht des Anfechtenden — häufig übersehen.
- § 164 BGB: Stellvertretung — Offenkundigkeit als Tatbestandsmerkmal.
- § 179 BGB: Haftung des Vertreters ohne Vertretungsmacht.

## Prüfraster

1. Aufbaurüge: Entspricht die Prüfungsstruktur dem Anspruchsaufbau (Wer will was von wem woraus)?
2. Auslegungsvorrang: Wurde Auslegung vor Anfechtung und Dissens geprüft?
3. Normzitate: Sind alle einschlägigen Normen genannt und korrekt zitiert?
4. Subsumtion: Ist jedes Tatbestandsmerkmal auf den Sachverhalt angewendet?
5. Rechtsfolge: Ist die Rechtsfolge der einschlägigen Norm korrekt benannt?
6. Gutachtenstil-Einhaltung: Kein Ergebnis vor Begründung im Obersatz.
7. Fehlende Folgeprüfungen (§§ 122 und 179 BGB) ergänzt?

## Typische Fallstricke

- Motivirrtum als Anfechtungsgrund nach § 119 Abs. 1 BGB zu werten ist ein klassischer Fehler.
- § 122 BGB wird systematisch übersehen — immer nach erfolgreicher Anfechtung prüfen.
- Offenkundigkeit bei § 164 BGB fehlt häufig — kein Stellvertretungseffekt ohne sie.
- Urteilsstil in Klausuren verwenden statt Gutachtenstil ist ein Bewertungsmangel.

## Quellen

- [§ 133 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__133.html)
- [§ 119 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__119.html)
- [§ 122 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__122.html)
- [§ 179 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [dejure.org § 164 BGB](https://dejure.org/gesetze/BGB/164.html)

## Vertiefung

### Systematisches Fehler-Tracking

Für die Klausurvorbereitung empfiehlt sich ein persönliches Fehlerprotokoll: Welche Normen werden
regelmäßig übersehen? Wo fehlt die Subsumtion? Wo wird der Gutachtenstil verletzt? Systematische
Wiederholung der häufigsten Fehler beschleunigt den Lernfortschritt erheblich.

### Punktgewichtung in der Klausur

BGB-AT-Klausuren gewichten: Anspruchsaufbau (5-10 %), Tatbestandsprüfung (40-50 %), Subsumtion
(20-30 %), Ergebnis (5-10 %), Gutachtenstil (10-20 %). Fehler in der Subsumtion kosten die meisten
Punkte.

### Klausur-Checkliste Fehlerdiagnose

- Falsche Anspruchsgrundlage gewählt?
- Auslegung vor Anfechtung unterlassen?
- Tatbestandsmerkmale unvollständig oder falsch definiert?
- § 122 BGB nach Anfechtung übersehen?
- Gutachtenstil verletzt (Ergebnis vor Begründung)?

---

## Skill: `vertragsschluss-antrag-abgabe`

_Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschungsgründe, Annahmefrist unter An- und Abwesenden, verspätete und abgeänderte Annahme sowie Zeitpunkt des Vertragsschlusses. Output: vollständiger Subsumtionspfad im BGB AT._

# Vertragsschluss — Antrag und Annahme §§ 145 bis 156 BGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Angebot per Brief abgegeben — Käufer nimmt nach zwei Wochen an; Frist abgelaufen?
- Annahme mit Änderung des Preises — gilt dies als neues Angebot oder als (abgeänderte) Annahme?
- Klausurkonstellation: Anbieter stirbt nach Abgabe des Angebots, bevor der Empfänger annimmt.

## Erste Schritte

1. Antrag bestimmen: Vollständiges, auf Vertragsschluss gerichtetes Angebot mit Rechtsbindungswillen.
2. Bindungswirkung nach § 145 BGB: Antragende ist an das Angebot gebunden, solange Annahmefrist läuft.
3. Erlöschen des Antrags: § 146 BGB — Ablehnung oder nicht rechtzeitige Annahme.
4. Annahmefrist: § 147 BGB — unter Anwesenden sofort, unter Abwesenden angemessene Postlaufzeit.
5. Verspätete Annahme: § 149 BGB — gilt als neues Angebot; Antragender kann sofort annehmen.
6. Abgeänderte Annahme: § 150 Abs. 2 BGB — gilt als Ablehnung verbunden mit neuem Antrag.

## Rechtsrahmen

- § 145 BGB: Bindungswirkung des Antrags — Antragender ist grundsätzlich gebunden.
- § 146 BGB: Erlöschen des Antrags bei Ablehnung oder nicht rechtzeitiger Annahme.
- § 147 BGB: Annahmefrist — unter Anwesenden sofort, unter Abwesenden angemessene Zeit.
- § 149 BGB: Verspätete Annahme — gilt dem Antragenden gegenüber als neues Angebot.
- § 150 Abs. 2 BGB: Abgeänderte Annahme — gilt als Ablehnung und neues Angebot.

## Prüfraster

1. Antrag vollständig: Alle essentialia negotii enthalten und Rechtsbindungswille erkennbar?
2. Antrag zugegangen: § 130 BGB — Zeitpunkt des Zugangs beim Empfänger.
3. Annahmefrist nach § 147 BGB: Unter Anwesenden sofort, unter Abwesenden wie lange?
4. Annahme innerhalb der Frist zugegangen: Zeitpunkt dokumentiert?
5. Verspätete Annahme nach § 149 BGB: Antragender muss unverzüglich ablehnen, sonst gilt Vertrag?
6. Abgeänderte Annahme nach § 150 Abs. 2 BGB: Änderung wesentlich oder unwesentlich?
7. Tod oder Geschäftsunfähigkeit des Antragenden: § 130 Abs. 2 BGB — Antrag bleibt grundsätzlich wirksam.

## Typische Fallstricke

- Verspätete Annahme ist kein Vertragsschluss, sondern neues Angebot — Antragender muss annehmen.
- Abgeänderte Annahme, auch bei geringfügiger Änderung, gilt als Ablehnung und neues Angebot.
- § 130 Abs. 2 BGB: Tod des Antragenden nach Abgabe hindert Wirksamkeit nicht — häufig falsch gelöst.
- Kaufmännisches Bestätigungsschreiben kann Vertragsinhalt nachträglich modifizieren.

## Quellen

- [§ 145 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__145.html)
- [§ 147 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__147.html)
- [§ 150 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__150.html)
- [dejure.org § 145 BGB](https://dejure.org/gesetze/BGB/145.html)
- [dejure.org § 150 BGB](https://dejure.org/gesetze/BGB/150.html)

## Vertiefung

### Annahmefrist-Berechnung

§ 147 Abs. 2 BGB: Die angemessene Frist umfasst Bearbeitungszeit für das Angebot, Postlaufzeit
hin und zurück sowie eine kurze Überlegungszeit. Bei Angeboten per E-Mail ist die Frist kürzer
als bei Briefangeboten, weil die Übermittlungszeit kürzer ist.

### Vertragsschluss im internationalen Handel

Bei grenzüberschreitenden Verträgen kann das UN-Kaufrecht (CISG) anwendbar sein, das eigene
Regeln für Angebot und Annahme enthält. Das CISG kennt kein Abstraktionsprinzip — wichtig für
den internationalen BGB-AT-Vergleich.

### Klausur-Checkliste Vertragsschluss

- Antrag vollständig mit allen essentialia negotii?
- Zugangszeitpunkt des Antrags nach § 130 BGB bestimmt?
- Annahmefrist nach § 147 BGB berechnet?
- Annahme innerhalb der Frist zugegangen?
- Verspätete Annahme (§ 149 BGB) oder abgeänderte Annahme (§ 150 Abs. 2 BGB) als neues Angebot?

---

## Skill: `rechtlich-vorteilhaft-paragraph-107`

_Klausurfall zu lediglich rechtlich vorteilhaften Rechtsgeschäften nach § 107 BGB: Minderjähriger erwirbt ohne Einwilligung des Vertreters, wenn das Geschäft keinen rechtlichen Nachteil bringt. Abgrenzung zu wirtschaftlichen Vorteilen, gemischte Rechtsgeschäfte und Schenkung mit Auflagen._

# Lediglich rechtlich vorteilhaft — § 107 BGB

## Mandantenfall

- 14-Jähriger erhält Schenkung eines Grundstücks ohne elterliche Einwilligung — wirksam nach § 107 BGB?
- Minderjähriger wird aus einer Bürgschaft entlassen — lediglich rechtlich vorteilhaft?
- Klausurkonstellation: Schenkung mit Auflage an Minderjährigen — Auflage als rechtlicher Nachteil?

## Erste Schritte

1. Geschäftsfähigkeit des Minderjährigen nach §§ 104 bis 106 BGB prüfen.
2. § 107 BGB: Einwilligung des gesetzlichen Vertreters entbehrlich, wenn das Geschäft lediglich rechtlich vorteilhaft ist.
3. Maßstab: Rechtliche — nicht wirtschaftliche — Betrachtung; OLG-Rspr. zur Einheitlichkeit.
4. Schenkung mit Auflage: Auflage als rechtliche Verpflichtung begründet Nachteil.
5. Grundstückserwerb: Grundbuchbelastungen prüfen — Hypothek, Grundschuld, Nießbrauch als Nachteile.
6. Rechtsfolge bei fehlendem Vorteil: schwebende Unwirksamkeit nach § 108 BGB, Genehmigung erforderlich.

## Rechtsrahmen

- § 107 BGB: Einwilligungsfreiheit bei lediglich rechtlich vorteilhaften Geschäften.
- §§ 104 bis 106 BGB: Geschäftsfähigkeit Minderjähriger als Grundlage.
- § 108 BGB: Schwebende Unwirksamkeit ohne Einwilligung.
- § 109 BGB: Widerrufsrecht des Dritten bis zur Genehmigung.
- § 516 BGB: Schenkung — Hauptanwendungsfall von § 107 BGB.

## Prüfraster

1. Minderjähriger: Alter und Geschäftsfähigkeitsstufe nach §§ 104 bis 106 BGB?
2. Rechtlicher Vorteil: Erlangt der Minderjährige ein Recht ohne rechtliche Pflicht?
3. Grundstückserwerb: Sind Belastungen im Grundbuch eingetragen — Nachteil nach h.M.?
4. Auflage bei Schenkung: Begründet Auflage eine rechtliche Verpflichtung — Nachteil?
5. Wirtschaftliche Betrachtung ausschließen: Nur rechtliche Nachteilsprüfung maßgeblich.
6. Konsequenz: Einwilligung erforderlich oder schwebende Unwirksamkeit nach § 108 BGB?
7. Widerruf des Dritten nach § 109 BGB bis zur Genehmigung?

## Typische Fallstricke

- Wirtschaftliche Vorteile sind irrelevant — nur rechtliche Betrachtung nach § 107 BGB.
- Grundstückserwerb mit Grundschuldeintragung ist nicht mehr lediglich vorteilhaft — häufiger Klausurfehler.
- Schenkung mit Auflagen begründet rechtliche Pflichten — kein lediglich rechtlicher Vorteil.
- § 107 BGB gilt nur für beschränkt Geschäftsfähige, nicht für Geschäftsunfähige (§ 104 BGB).

## Quellen

- [§ 107 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__107.html)
- [§ 108 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__108.html)
- [§ 109 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__109.html)
- [dejure.org § 107 BGB](https://dejure.org/gesetze/BGB/107.html)
- [dejure.org § 108 BGB](https://dejure.org/gesetze/BGB/108.html)

## Vertiefung

### Grundbucheintragungen als Nachteil

Die h.M. geht davon aus, dass ein Grundstückserwerb nicht lediglich vorteilhaft ist, wenn das
Grundstück mit einer Hypothek, Grundschuld oder einem Nießbrauch belastet ist. Die Belastung
ist eine rechtliche Pflicht, auch wenn sie wirtschaftlich neutral oder sogar vorteilhaft wäre.

### Praxisrelevanz bei Schenkungen

Eltern schenken Minderjährigem ein Grundstück: Wenn das Grundstück schuldenfrei ist, gilt die
Schenkung als lediglich rechtlich vorteilhaft (§ 107 BGB). Wenn eine Grundschuld eingetragen ist,
ist eine Einwilligung des gesetzlichen Vertreters erforderlich (§ 108 BGB).

### Klausur-Checkliste § 107 BGB

- Geschäft erlangt der Minderjährige ein Recht oder wird er von einer Pflicht befreit?
- Rein rechtliche Betrachtung: Entstehen durch das Geschäft rechtliche Pflichten?
- Grundstückserwerb: Sind im Grundbuch Belastungen eingetragen?
- Schenkung mit Auflage: Auflage als rechtliche Pflicht des Minderjährigen?
- Wirtschaftliche Vorteile bleiben außer Betracht — nur rechtliche Betrachtung?

---

## Skill: `invitatio-ad-offerendum-und-werbung`

_Klausurfall zur Abgrenzung von Angebot und invitatio ad offerendum nach §§ 145 bis 147 BGB: Werbung im Schaufenster und Online-Shop als bloße Aufforderung zur Angebotsabgabe, verbindliche Preisauszeichnung, automatisierte Bestellbestätigung. Output: Subsumtionsraster und Gutachtenstil._

# Invitatio ad offerendum und Werbung — Angebot oder Aufforderung?

## Mandantenfall

- Online-Shop listet Artikel für 1 € statt 100 € — Preisfehler: Ist die Preisangabe ein verbindliches Angebot?
- Schaufensterwerbung mit Preisschild: Kunde fordert Verkauf zum angezeigten Preis — Angebot oder invitatio?
- Klausurkonstellation: Katalogversand eines Händlers enthält konkrete Mengen- und Preisangaben — Bindungswirkung?

## Erste Schritte

1. Willenserklärung des Werbenden prüfen: Enthält die Werbung alle wesentlichen Vertragsbestandteile (essentialia negotii)?
2. Rechtsbindungswille: Wollte der Erklärende sich verbindlich binden oder nur zur Angebotsabgabe auffordern?
3. Auslegung nach §§ 133 und 157 BGB: Empfängerhorizont eines objektiven Dritten anlegen.
4. Lagerbestand und Kapazitätsgrenzen: Kann ein Anbieter bei Massengeschäften an unbegrenzt viele Kunden gebunden sein?
5. Automatisierte Bestellbestätigung: Ist sie Annahme oder nur Eingangsbestätigung?
6. Rechtsfolge: Vertragsschluss oder Anfechtung wegen Irrtums (§ 119 Abs. 1 BGB) bei Preisfehler.

## Rechtsrahmen

- § 145 BGB: Antrag — Bindungswirkung für den Antragenden.
- § 147 BGB: Annahmefrist unter Anwesenden und Abwesenden.
- §§ 133 und 157 BGB: Auslegung von Willenserklärungen und Verträgen nach Treu und Glauben.
- § 119 Abs. 1 BGB: Irrtumsanfechtung wegen Inhalts- oder Erklärungsirrtum bei Preisfehler.
- § 122 BGB: Schadensersatzpflicht des Anfechtenden gegenüber dem gutgläubigen Empfänger.

## Prüfraster

1. Enthält die Werbung alle wesentlichen Vertragsbestandteile (Ware, Preis, Menge)?
2. Rechtsbindungswille nach objektivem Empfängerhorizont bejaht oder verneint?
3. Handelt es sich um ein Massengeschäft ohne feste Mengenbegrenzung (typisch invitatio)?
4. Automatisierte Bestellbestätigung: Rechtsfolge Annahme oder nur Zugangsbestätigung?
5. Bei Preisfehler: Voraussetzungen der Irrtumsanfechtung § 119 Abs. 1 BGB prüfen.
6. Schadensersatz aus § 122 BGB: positives oder negatives Interesse des Empfängers?
7. Sonderproblem Online-Auktionen: §§ 156 und 312 ff. BGB beachten.

## Typische Fallstricke

- Schaufensterwerbung ist in Deutschland grundsätzlich invitatio, nicht Angebot — häufiger Klausurfehler.
- Automatisierte Eingangsbestätigungen im Online-Handel sind keine Annahmeerklärung.
- Preisfehler-Anfechtung nach § 119 Abs. 1 BGB erfordert unverzügliche Erklärung (§ 121 BGB).
- § 122 BGB schützt den Empfänger: Anfechtender haftet auf das negative Interesse.

## Quellen

- [§ 145 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__145.html)
- [§ 119 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__119.html)
- [§ 122 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__122.html)
- [dejure.org § 145 BGB](https://dejure.org/gesetze/BGB/145.html)
- [dejure.org § 157 BGB](https://dejure.org/gesetze/BGB/157.html)

## Vertiefung

### Wirtschaftliche Bedeutung der Abgrenzung

Die Abgrenzung von Angebot und invitatio ad offerendum hat erhebliche wirtschaftliche Konsequenzen:
Wäre jede Preisauszeichnung ein verbindliches Angebot, wäre der Einzelhändler an jeden Preis gebunden,
auch bei Schreibfehlern. Deshalb ist die Schaufensterwerbung in Deutschland grundsätzlich invitatio.

### Internet-Preisfehler in der Praxis

BGH-Rechtsprechung zu Preisfehlern im Internet: Das Einstellen eines Artikels im Online-Shop ist
in der Regel eine invitatio. Die Bestellung des Kunden ist das Angebot. Die Bestellbestätigung
kann Annahme sein — hier kommt es auf die konkrete Formulierung an.

### Klausur-Checkliste invitatio

- Alle essentialia negotii in der Werbung enthalten?
- Rechtsbindungswille nach objektivem Empfängerhorizont?
- Massengeschäft ohne Mengenbegrenzung typischerweise invitatio?
- Automatisierte Bestellbestätigung: Annahme oder nur Eingangsbestätigung?
- Preisfehler: Anfechtung nach § 119 Abs. 1 BGB — unverzüglich nach § 121 BGB?

---

## Skill: `willenserklaerung-wucher-ausbeutung-zugang`

_Klausurfall zum Tatbestand der Willenserklärung: objektiver Erklärungstatbestand, Rechtsbindungswille, Erklärungsbewusstsein und potentielles Bewusstsein, Abgrenzung zu Gefälligkeiten und sozialtypischem Verhalten. Prüfraster für §§ 116 ff. BGB in Examens- und Anwaltsprüfung im BGB AT._

# Willenserklärung — Tatbestand §§ 116 ff. BGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Bieter auf Auktion hebt irrtümlich die Hand — liegt eine Willenserklärung vor?
- Schreiben unter Scherz oder Druck verfasst — fehlt der Rechtsbindungswille?
- Klausurkonstellation: Internetbestellung durch Kind auf Eltern-Account — Willenserklärung der Eltern?

## Erste Schritte

1. Objektiver Tatbestand prüfen: Gibt es eine nach außen getretene Erklärung mit erkennbarem Rechtsbindungswillen?
2. Subjektiver Tatbestand: Handlungswille, Erklärungsbewusstsein (Bewusstsein, irgendwie rechtserheblich zu handeln), Geschäftswille.
3. Fehlendes Erklärungsbewusstsein: Gilt als Willenserklärung, wenn der Erklärende hätte erkennen können (potentielles Bewusstsein, h.M.).
4. Rechtsbindungswille: Wollten die Parteien rechtlich gebunden sein — Abgrenzung zu Gefälligkeit und sozialem Kontakt.
5. Scherzerklärung nach § 118 BGB: Erkennbare Scherzerklärung ist nichtig, Schadensersatz nach § 122 BGB.
6. Geisteskrankheit oder vorübergehende Störung nach § 105 BGB: Kein Rechtsbindungswille möglich.

## Rechtsrahmen

- §§ 116 bis 118 BGB: Geheimvorbehalt, Scheingeschäft und Scherzerklärung.
- § 105 BGB: Nichtigkeit der Willenserklärung bei Geschäftsunfähigkeit.
- §§ 133 und 157 BGB: Auslegung zur Ermittlung des objektiven Erklärungssinns.
- § 122 BGB: Schadensersatzpflicht bei Nichtigkeit nach § 118 BGB.
- § 242 BGB: Vertrauensschutz als Grenze beim fehlenden subjektiven Tatbestand.

## Prüfraster

1. Objektiver Erklärungstatbestand: Äußeres Erklärungszeichen vorhanden und empfangsbedürftig?
2. Rechtsbindungswille: Wollte der Erklärende bei objektivem Empfängerhorizont rechtlich gebunden sein?
3. Erklärungsbewusstsein vorhanden oder zumindest potentiell vorhanden?
4. Handlungswille: Hat der Erklärende die Handlung bewusst vorgenommen?
5. Scherzerklärung nach § 118 BGB: War Scherz für Empfänger erkennbar?
6. Geisteskrankheit oder Rausch nach § 105 BGB: Kein Erklärungswille möglich?
7. Fehler bei Internetgeschäften: Wem ist die Erklärung zuzurechnen (Zurechnung nach § 164 BGB analog)?

## Typische Fallstricke

- Potentielles Erklärungsbewusstsein reicht nach h.M. aus — Erklärende haftet, wenn sie hätten erkennen können.
- Scherzerklärung (§ 118 BGB) ist nichtig, aber Schadensersatzpflicht nach § 122 BGB entsteht.
- Gefälligkeit ohne Rechtsbindungswillen begründet kein Schuldverhältnis — rein sozialer Bereich.
- Vorübergehende Störung nach § 105 Abs. 2 BGB: Erklärung nichtig, auch wenn nicht auf Dauer geschäftsunfähig.

## Quellen

- [§ 116 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__116.html)
- [§ 118 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__118.html)
- [§ 105 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__105.html)
- [dejure.org § 116 BGB](https://dejure.org/gesetze/BGB/116.html)
- [dejure.org § 105 BGB](https://dejure.org/gesetze/BGB/105.html)

## Vertiefung

### Dreigliedriger Tatbestand

Die Willenserklärung hat drei Elemente: (1) Handlungswille (der Erklärende handelt bewusst),
(2) Erklärungsbewusstsein (Bewusstsein des Erklärenden, rechtserheblich zu handeln — nach h.M.
genügt potentielles Bewusstsein), (3) Geschäftswille (der Erklärende will genau dieses Rechtsgeschäft).

### Fehlen einzelner Elemente

Fehlt der Handlungswille: Keine Willenserklärung (z.B. geführte Hand).
Fehlt das Erklärungsbewusstsein: Streitig — nach h.M. WE mit Anfechtungsrecht.
Fehlt der Geschäftswille: Anfechtungsrecht nach § 119 Abs. 1 BGB (Inhaltsirrtum).

### Klausur-Checkliste Tatbestand WE

- Handlungswille: Hat der Erklärende die äußere Handlung bewusst vorgenommen?
- Erklärungsbewusstsein: Aktuell vorhanden oder nur potentiell — welche Ansicht?
- Geschäftswille: Wollte Erklärende genau dieses Rechtsgeschäft?
- Empfangsbedürftigkeit: Bedarf die WE des Zugangs beim Empfänger?
- Objektiver Empfängerhorizont: Wie musste der Empfänger die Erklärung verstehen?

---

## Skill: `vertreter-ohne-vertretungsmacht-paragraphen-177-179`

_Klausurfall zum vollmachtlosen Vertreter nach §§ 177 bis 179 BGB: schwebende Unwirksamkeit des Vertreterhandelns, Genehmigung des Vertretenen nach § 177 BGB, Widerrufsrecht des Dritten nach § 178 BGB, Haftung des Vertreters auf Erfüllung oder Schadensersatz nach § 179 BGB im BGB AT._

# Vertreter ohne Vertretungsmacht — §§ 177 bis 179 BGB

## Arbeitsbereich

Klausurfall zum vollmachtlosen Vertreter nach §§ 177 bis 179 BGB: schwebende Unwirksamkeit des Vertreterhandelns, Genehmigung des Vertretenen nach § 177 BGB, Widerrufsrecht des Dritten nach § 178 BGB, Haftung des Vertreters auf Erfüllung oder Schadensersatz nach § 179 BGB. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Mitarbeiter schließt ohne Vollmacht Vertrag ab — Vertretener verweigert Genehmigung; Dritter verlangt Schadensersatz.
- Bevollmächtigter überschreitet seine Vollmacht — Vertretener genehmigt nachträglich; wirksam?
- Klausurkonstellation: vollmachtloser Vertreter handelt; gutgläubiger Dritter wählt zwischen Erfüllung und Schadensersatz.

## Erste Schritte

1. Vollmachtlosigkeit feststellen: Fehlt die Vollmacht ganz oder wurde sie überschritten?
2. Schwebende Unwirksamkeit nach § 177 Abs. 1 BGB: Vertrag hängt von Genehmigung des Vertretenen ab.
3. Genehmigung nach § 177 Abs. 1 BGB: Form (grundsätzlich formfrei) und Frist (auf Verlangen nach § 177 Abs. 2 BGB).
4. Widerruf des Dritten nach § 178 BGB: Bis zur Genehmigung kann Dritter den Vertrag widerrufen.
5. Haftung nach § 179 BGB bei Verweigerung der Genehmigung: Erfüllung oder Schadensersatz nach Wahl des Dritten.
6. Gutgläubigkeit des Dritten nach § 179 Abs. 3 BGB: Kannte Dritter fehlende Vollmacht — keine Haftung.

## Rechtsrahmen

- § 177 BGB: Schwebende Unwirksamkeit und Genehmigung bei vollmachtlosem Vertreter.
- § 178 BGB: Widerruf des Dritten bis zur Entscheidung über Genehmigung.
- § 179 BGB: Haftung des vollmachtlosen Vertreters — Erfüllung oder Schadensersatz.
- § 166 BGB: Wissenszurechnung — Kenntnis des Vertreters bei Vollmachtsgeschäften.
- § 164 BGB: Stellvertretungsvoraussetzungen als Grundlage.

## Prüfraster

1. Vollmacht fehlend oder überschritten — konkret belegt?
2. Schwebende Unwirksamkeit nach § 177 Abs. 1 BGB: Vertrag in der Schwebe.
3. Genehmigung durch Vertretenen: erteilt, verweigert oder Frist gesetzt nach § 177 Abs. 2 BGB?
4. Widerruf des Dritten nach § 178 BGB: innerhalb der Schwebezeit erklärt?
5. § 179 Abs. 1 BGB: Haftung des Vertreters auf Erfüllung oder Schadensersatz.
6. Ausschluss nach § 179 Abs. 3 BGB: Kannte der Dritte die fehlende Vollmacht?
7. Schadensersatz nach § 179 BGB: positives oder negatives Interesse — Wahl des Dritten.

## Typische Fallstricke

- Schwebende Unwirksamkeit (§ 177 BGB) bedeutet weder Wirksamkeit noch Nichtigkeit — Übergangszustand.
- § 179 Abs. 3 BGB: Wusste der Dritte von der fehlenden Vollmacht, haftet der Vertreter nicht.
- Genehmigung nach § 177 BGB wirkt ex tunc — auf Zeitpunkt des Vertragsschlusses zurück.
- Widerruf nach § 178 BGB kann nur bis zur Genehmigung erfolgen — dann kein Widerruf mehr.

## Output

- Gutachtenstil-Abschnitt zu §§ 177 bis 179 BGB mit vollständiger Subsumtion
- Entscheidungsbaum: Genehmigung erteilt / verweigert → Haftung des Vertreters
- Prüfampel: Vertrag wirksam (Genehmigung) / Haftung § 179 BGB / Ausschluss § 179 Abs. 3 BGB
- Klausurlösungsskizze mit Widerrufsoption des Dritten nach § 178 BGB

## Quellen

- [§ 177 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__177.html)
- [§ 178 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__178.html)
- [§ 179 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [dejure.org § 177 BGB](https://dejure.org/gesetze/BGB/177.html)
- [dejure.org § 179 BGB](https://dejure.org/gesetze/BGB/179.html)

## Vertiefung

### Schwebende Unwirksamkeit im Detail

Während des Schwebezustands nach § 177 BGB gilt: Der Dritte kann weder Erfüllung noch
Schadensersatz verlangen. Er kann den Vertrag widerrufen (§ 178 BGB), aber er kann nicht
verlangen, dass der Vertretene sofort genehmigt. Der Vertretene hat eine angemessene Zeit.

### Haftung nach § 179 BGB

§ 179 Abs. 1 BGB: Haftung auf Erfüllung oder Schadensersatz nach Wahl des Dritten.
§ 179 Abs. 2 BGB: Kannte der Dritte die fehlende Vollmacht, haftet der Vertreter nur auf das
negative Interesse (Vertrauensschaden).
§ 179 Abs. 3 BGB: Kannte der Dritte die fehlende Vollmacht, haftet der Vertreter gar nicht.

### Klausur-Checkliste §§ 177 bis 179 BGB

- Vollmacht fehlend oder überschritten — konkret festgestellt?
- Schwebende Unwirksamkeit nach § 177 Abs. 1 BGB und Genehmigungsfrist nach § 177 Abs. 2 BGB?
- Widerruf des Dritten nach § 178 BGB: Innerhalb der Schwebezeit erklärt?
- Haftungsumfang nach § 179 Abs. 1 oder Abs. 2 BGB — Dritter gutgläubig?
- Ausschluss nach § 179 Abs. 3 BGB: Kannte Dritter fehlende Vollmacht?

---

## Skill: `vertragsschluss-antrag-annahme`

_Klausurfall zum Vertragsschluss durch Antrag und Annahme nach §§ 145 bis 156 BGB: Bindungswirkung des Antrags, Erlöschungsgründe, Annahmefrist unter An- und Abwesenden, verspätete und abgeänderte Annahme sowie Zeitpunkt des Vertragsschlusses. Output: vollständiger Subsumtionspfad._

# Vertragsschluss — Antrag und Annahme §§ 145 bis 156 BGB

## Mandantenfall

- Angebot per Brief abgegeben — Käufer nimmt nach zwei Wochen an; Frist abgelaufen?
- Annahme mit Änderung des Preises — gilt dies als neues Angebot oder als (abgeänderte) Annahme?
- Klausurkonstellation: Anbieter stirbt nach Abgabe des Angebots, bevor der Empfänger annimmt.

## Erste Schritte

1. Antrag bestimmen: Vollständiges, auf Vertragsschluss gerichtetes Angebot mit Rechtsbindungswillen.
2. Bindungswirkung nach § 145 BGB: Antragende ist an das Angebot gebunden, solange Annahmefrist läuft.
3. Erlöschen des Antrags: § 146 BGB — Ablehnung oder nicht rechtzeitige Annahme.
4. Annahmefrist: § 147 BGB — unter Anwesenden sofort, unter Abwesenden angemessene Postlaufzeit.
5. Verspätete Annahme: § 149 BGB — gilt als neues Angebot; Antragender kann sofort annehmen.
6. Abgeänderte Annahme: § 150 Abs. 2 BGB — gilt als Ablehnung verbunden mit neuem Antrag.

## Rechtsrahmen

- § 145 BGB: Bindungswirkung des Antrags — Antragender ist grundsätzlich gebunden.
- § 146 BGB: Erlöschen des Antrags bei Ablehnung oder nicht rechtzeitiger Annahme.
- § 147 BGB: Annahmefrist — unter Anwesenden sofort, unter Abwesenden angemessene Zeit.
- § 149 BGB: Verspätete Annahme — gilt dem Antragenden gegenüber als neues Angebot.
- § 150 Abs. 2 BGB: Abgeänderte Annahme — gilt als Ablehnung und neues Angebot.

## Prüfraster

1. Antrag vollständig: Alle essentialia negotii enthalten und Rechtsbindungswille erkennbar?
2. Antrag zugegangen: § 130 BGB — Zeitpunkt des Zugangs beim Empfänger.
3. Annahmefrist nach § 147 BGB: Unter Anwesenden sofort, unter Abwesenden wie lange?
4. Annahme innerhalb der Frist zugegangen: Zeitpunkt dokumentiert?
5. Verspätete Annahme nach § 149 BGB: Antragender muss unverzüglich ablehnen, sonst gilt Vertrag?
6. Abgeänderte Annahme nach § 150 Abs. 2 BGB: Änderung wesentlich oder unwesentlich?
7. Tod oder Geschäftsunfähigkeit des Antragenden: § 130 Abs. 2 BGB — Antrag bleibt grundsätzlich wirksam.

## Typische Fallstricke

- Verspätete Annahme ist kein Vertragsschluss, sondern neues Angebot — Antragender muss annehmen.
- Abgeänderte Annahme, auch bei geringfügiger Änderung, gilt als Ablehnung und neues Angebot.
- § 130 Abs. 2 BGB: Tod des Antragenden nach Abgabe hindert Wirksamkeit nicht — häufig falsch gelöst.
- Kaufmännisches Bestätigungsschreiben kann Vertragsinhalt nachträglich modifizieren.

## Quellen

- [§ 145 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__145.html)
- [§ 147 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__147.html)
- [§ 150 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__150.html)
- [dejure.org § 145 BGB](https://dejure.org/gesetze/BGB/145.html)
- [dejure.org § 150 BGB](https://dejure.org/gesetze/BGB/150.html)

## Vertiefung

### Annahmefrist-Berechnung

§ 147 Abs. 2 BGB: Die angemessene Frist umfasst Bearbeitungszeit für das Angebot, Postlaufzeit
hin und zurück sowie eine kurze Überlegungszeit. Bei Angeboten per E-Mail ist die Frist kürzer
als bei Briefangeboten, weil die Übermittlungszeit kürzer ist.

### Vertragsschluss im internationalen Handel

Bei grenzüberschreitenden Verträgen kann das UN-Kaufrecht (CISG) anwendbar sein, das eigene
Regeln für Angebot und Annahme enthält. Das CISG kennt kein Abstraktionsprinzip — wichtig für
den internationalen BGB-AT-Vergleich.

### Klausur-Checkliste Vertragsschluss

- Antrag vollständig mit allen essentialia negotii?
- Zugangszeitpunkt des Antrags nach § 130 BGB bestimmt?
- Annahmefrist nach § 147 BGB berechnet?
- Annahme innerhalb der Frist zugegangen?
- Verspätete Annahme (§ 149 BGB) oder abgeänderte Annahme (§ 150 Abs. 2 BGB) als neues Angebot?

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

