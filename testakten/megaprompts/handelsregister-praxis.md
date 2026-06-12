# Megaprompt: handelsregister-praxis

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 76 Skills des Plugins `handelsregister-praxis`.

## Inhaltsverzeichnis

1. **registerrecht-beschlussmaengel-und-registervollzug** — Prüft, ob das Registergericht bei Kapitalmaßnahme, Geschäftsführerbestellung oder Satzungsänderung Beschlussmängel beach…
2. **rechtsabteilung-insolvenzvermerk** — Rechtsabteilungs-Fachmodul für Insolvenzvermerk und ausländischer Trustee: Vertretungsmacht ausländischer Insolvenzorgan…
3. **rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug** — Rechtsabteilungs-Fachmodul für Geschäftsführerbestellung mit Auslandsbezug: Identität, Versicherung, Unterschrift und Üb…
4. **rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung** — Rechtsabteilungs-Fachmodul für Kapitalerhöhung und Zwischenverfügung: Zwischenverfügungen werden in heilbare Punkte, Str…
5. **rechtsabteilung-gesellschafterliste-nach-streit-und-ev** — Rechtsabteilungs-Fachmodul für Gesellschafterliste nach Streit und EV: Rechtsabteilungen bauen registertaugliche Listenp…
6. **rechtsabteilung-mopeg-gesellschaftsregister-und-ohg-sprung** — Rechtsabteilungs-Fachmodul für MoPeG-Gesellschaftsregister und OHG-Sprung: GbR, eGbR, OHG und Grundstücksfähigkeit werde…
7. **zweigniederlassung-auslaendische-gesellschaft** — Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift…
8. **kaltstart-routing** — Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welc…
9. **beanstandung-zwischenverfuegung** — Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, formuliert Nachreichung, Bitte um Frist…
10. **registergericht-rollen-datenschutz** — Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache richterlich, rechtspflegerisch oder rei…

---

## Skill: `registerrecht-beschlussmaengel-und-registervollzug`

_Prüft, ob das Registergericht bei Kapitalmaßnahme, Geschäftsführerbestellung oder Satzungsänderung Beschlussmängel beachten muss, wie weit die formelle Prüfung reicht und wann der materielle Streit auf Zivilprozess/Eilrechtsschutz verlagert wird im Handelsregister Praxis._

# Beschlussmängel im Registervollzug

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Zuschnitt

Prüft, ob das Registergericht bei Kapitalmaßnahme, Geschäftsführerbestellung oder Satzungsänderung Beschlussmängel beachten muss, wie weit die formelle Prüfung reicht und wann der materielle Streit auf Zivilprozess/Eilrechtsschutz verlagert wird.

## Spezialfokus

Besonders wichtig bei Gesellschafterstreit: nicht jedes behauptete Beschlussdefizit stoppt automatisch den Registervollzug, aber offensichtliche Nichtigkeits- und Legitimationsprobleme müssen sauber adressiert werden.

## Arbeitsmodus

1. **Dokumente sortieren:** Auszug, Urkunde, Bewilligung, Antrag, Beschluss, Vollmacht, Gerichtsschreiben, Bankauflage und Frist erfassen.
2. **Normanker setzen:** Nur Normen verwenden, die für den konkreten Schritt wirklich gebraucht werden.
3. **Hindernis qualifizieren:** behebbar, streitig, rangrelevant, zustimmungsbedürftig, genehmigungsbedürftig oder nur erläuterungsbedürftig.
4. **Arbeitsprodukt liefern:** Matrix, Nachreichung, Mandantenbrief, Amtsantwort, Beschwerdegerüst oder Vertragsklausel.
5. **Belegdisziplin:** Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst als zu verifizieren kennzeichnen.

## Ausgabe

- Kurzbefund
- Prüf- und Nachweismatrix
- offene entscheidende Fragen
- konkreter Entwurf oder Checkliste
- Risiko, das in der Praxis leicht übersehen wird

---

## Skill: `rechtsabteilung-insolvenzvermerk`

_Rechtsabteilungs-Fachmodul für Insolvenzvermerk und ausländischer Trustee: Vertretungsmacht ausländischer Insolvenzorgane wird registertauglich nachgewiesen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsregister Praxis._

# Rechtsabteilung: Insolvenzvermerk und ausländischer Trustee

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Insolvenzvermerk und ausländischer Trustee

- **Konkretes Problem:** Vertretungsmacht ausländischer Insolvenzorgane wird registertauglich nachgewiesen.
- **Norm-/Quellenanker:** HGB, GmbHG, AktG, MoPeG/Gesellschaftsregister, FamFG, HRV, Registerportal, notarielle Einreichung und Zwischenverfügungspraxis.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

InsO §§ 343 ff.; Registerrecht; Grundbuch-/Handelsregister-Inzidentprüfung

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Vertretungsmacht ausländischer Insolvenzorgane wird registertauglich nachgewiesen.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug`

_Rechtsabteilungs-Fachmodul für Geschäftsführerbestellung mit Auslandsbezug: Identität, Versicherung, Unterschrift und Übersetzung werden sauber vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsregister Praxis._

# Rechtsabteilung: Geschäftsführerbestellung mit Auslandsbezug

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Geschäftsführerbestellung mit Auslandsbezug

- **Konkretes Problem:** Identität, Versicherung, Unterschrift und Übersetzung werden sauber vorbereitet.
- **Norm-/Quellenanker:** HGB, GmbHG, AktG, MoPeG/Gesellschaftsregister, FamFG, HRV, Registerportal, notarielle Einreichung und Zwischenverfügungspraxis.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

GmbHG §§ 6, 39; Apostille; Registerpraxis

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Identität, Versicherung, Unterschrift und Übersetzung werden sauber vorbereitet.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung`

_Rechtsabteilungs-Fachmodul für Kapitalerhöhung und Zwischenverfügung: Zwischenverfügungen werden in heilbare Punkte, Streitpunkte und Beschwerde sortiert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsregister Praxis._

# Rechtsabteilung: Kapitalerhöhung und Zwischenverfügung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Kapitalerhöhung und Zwischenverfügung

- **Konkretes Problem:** Zwischenverfügungen werden in heilbare Punkte, Streitpunkte und Beschwerde sortiert.
- **Norm-/Quellenanker:** HGB, GmbHG, AktG, MoPeG/Gesellschaftsregister, FamFG, HRV, Registerportal, notarielle Einreichung und Zwischenverfügungspraxis.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

GmbHG §§ 55 ff.; FamFG; Notarunterlagen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Zwischenverfügungen werden in heilbare Punkte, Streitpunkte und Beschwerde sortiert.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-gesellschafterliste-nach-streit-und-ev`

_Rechtsabteilungs-Fachmodul für Gesellschafterliste nach Streit und EV: Rechtsabteilungen bauen registertaugliche Listenpakete und Widerspruchsstrategien. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsregister Praxis._

# Rechtsabteilung: Gesellschafterliste nach Streit und EV

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Gesellschafterliste nach Streit und EV

- **Konkretes Problem:** Rechtsabteilungen bauen registertaugliche Listenpakete und Widerspruchsstrategien.
- **Norm-/Quellenanker:** HGB, GmbHG, AktG, MoPeG/Gesellschaftsregister, FamFG, HRV, Registerportal, notarielle Einreichung und Zwischenverfügungspraxis.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

GmbHG § 40; FamFG; einstweiliger Rechtsschutz

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Rechtsabteilungen bauen registertaugliche Listenpakete und Widerspruchsstrategien.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-mopeg-gesellschaftsregister-und-ohg-sprung`

_Rechtsabteilungs-Fachmodul für MoPeG-Gesellschaftsregister und OHG-Sprung: GbR, eGbR, OHG und Grundstücksfähigkeit werden registerlogisch abgegrenzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsregister Praxis._

# Rechtsabteilung: MoPeG-Gesellschaftsregister und OHG-Sprung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: MoPeG-Gesellschaftsregister und OHG-Sprung

- **Konkretes Problem:** GbR, eGbR, OHG und Grundstücksfähigkeit werden registerlogisch abgegrenzt.
- **Norm-/Quellenanker:** HGB, GmbHG, AktG, MoPeG/Gesellschaftsregister, FamFG, HRV, Registerportal, notarielle Einreichung und Zwischenverfügungspraxis.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

MoPeG, HGB, BGB-Gesellschaftsregister

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

GbR, eGbR, OHG und Grundstücksfähigkeit werden registerlogisch abgegrenzt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `zweigniederlassung-auslaendische-gesellschaft`

_Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift: Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift._

# Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift.


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift.

### Zweigniederlassung ausländischer Gesellschaft

## Fachlicher Zuschnitt

Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift.

## Quellenrahmen

HGB §§ 8 ff. und § 15, FamFG-Registerverfahrensrecht, GmbHG/HGB/AktG/UmwG je nach Gesellschaftsform, HRV/Registerportal-Praxis.

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

---

## Skill: `kaltstart-routing`

_Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau._

# Kaltstart-Interview und Registerfahrplan

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Routing** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Handelsregister Praxis** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Fachlicher Zuschnitt

Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau.

## Quellenrahmen

HGB §§ 8 ff. und § 15, FamFG-Registerverfahrensrecht, GmbHG/HGB/AktG/UmwG je nach Gesellschaftsform, HRV/Registerportal-Praxis.

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

---

## Skill: `beanstandung-zwischenverfuegung`

_Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, formuliert Nachreichung, Bitte um Fristverlängerung oder Beschwerdevorbereitung im Handelsregister Praxis._

# Beanstandung und Zwischenverfügung beantworten

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Zuschnitt

Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, formuliert Nachreichung, Bitte um Fristverlängerung oder Beschwerdevorbereitung.

## Quellenrahmen

HGB §§ 8 ff. und § 15, FamFG-Registerverfahrensrecht, GmbHG/HGB/AktG/UmwG je nach Gesellschaftsform, HRV/Registerportal-Praxis.

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 39 GmbHG
- § 40 GmbHG
- § 382 FamFG
- § 395 FamFG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `registergericht-rollen-datenschutz`

_Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache richterlich, rechtspflegerisch oder rein vollzugstechnisch hängt im Handelsregister Praxis._

# Rechtspfleger, Registerrichter, Geschäftsstelle

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 8 HGB` — Handelsregister.
- `§ 12 HGB` — Anmeldungen und Einreichungen.
- `§ 15 HGB` — Publizitaet des Handelsregisters.
- `§ 29 HGB` — Anmeldung des Kaufmanns.
- `§ 106 HGB` — Eintragung der OHG.
- `§ 107 HGB` — Anmeldepflichten Personengesellschaft.
- `§ 39 GmbHG` — Aenderung der Geschaeftsfuehrung.
- `§ 40 GmbHG` — Gesellschafterliste.
- `§ 382 FamFG` — Registeranmeldung und Zwischenverfuegung.
- `§ 395 FamFG` — Loeschungsverfahren.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Zuschnitt

Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache richterlich, rechtspflegerisch oder rein vollzugstechnisch hängt.

## Quellenrahmen

HGB §§ 8 ff. und § 15, FamFG-Registerverfahrensrecht, GmbHG/HGB/AktG/UmwG je nach Gesellschaftsform, HRV/Registerportal-Praxis.

## Arbeitsmodus

1. **Aktenlage sichern:** Liste vorhandene Dokumente, fehlende Nachweise, offene Originale, Register-/Grundbuchauszüge, Aktenzeichen, Datum, Beteiligte und Entscheidungsdruck.
2. **Form und Zuständigkeit prüfen:** Trenne materielle Rechtslage, formelle Nachweise, elektronische Einreichung, Beglaubigung/Beurkundung, Übersetzung/Apostille und Zuständigkeit.
3. **Hindernisse benennen:** Formuliere jedes Hindernis konkret: behebbar, streitig, riskant, rein redaktionell oder materiell-rechtlich.
4. **Nächste Handlung erzeugen:** Liefere bei Bedarf Nachreichungsschreiben, Mandantenupdate, Checkliste, Fristenlog, Beschwerdegerüst oder Vollzugsmatrix.
5. **Belegdisziplin:** Zitiere Normen nur, wenn sie zum Schritt passen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; sonst ausdrücklich als zu verifizieren markieren.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

