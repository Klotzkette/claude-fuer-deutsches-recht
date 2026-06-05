---
name: verl-loeschpflicht-archivierung-loseblattwerk
description: "Verl Loeschpflicht Archivierung Loseblattwerk: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verl Loeschpflicht Archivierung Loseblattwerk

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Verl Loeschpflicht Archivierung Loseblattwerk** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verl-loeschpflicht-und-archivierung-fachzs` | Loeschpflicht und Archivierung bei juristischer Fachzeitschrift: DSGVO Art. 17 Recht auf Vergessen, Online-Archiv, Aktenzeichen-Anonymisierung, Pressefreiheitsabwaegung, Versionierung. |
| `verl-loseblattwerk-spezial` | Spezialfall Loseblattwerk: Ergaenzungslieferung, Stichtag, Hinweisapparat, Abonnentenpflege. Pruefraster fuer Verlag und Redaktion. |
| `verl-manuskript-merkwuerdige-formate-rettung` | Rettet Manuskripte aus DOCX-/Markdown-/LaTeX-Mix, alten Word97-Dateien und KI-generiertem Wust; legt saubere Konvertierungspfade fuer die Verlagsredaktion. |
| `verl-newsletter-redaktion-jur` | Newsletter-Redaktion juristisch: Konzept, Themenkasten, Empfaengerverwaltung nach DSGVO und UWG § 7, double opt-in, Mustertexte fuer wochen- und monatsweisen Versand. |
| `verl-online-kommentar-update-spezial` | Spezialfall Online-Kommentar und Update-Workflow: Versionierung, Rechtsprechungsmonitoring, Verlinkung. Pruefraster fuer Verlag und Hauptbearbeiter. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Verl Loeschpflicht Archivierung Loseblattwerk**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verl-loeschpflicht-und-archivierung-fachzs`

**Fokus:** Loeschpflicht und Archivierung bei juristischer Fachzeitschrift: DSGVO Art. 17 Recht auf Vergessen, Online-Archiv, Aktenzeichen-Anonymisierung, Pressefreiheitsabwaegung, Versionierung.

# Loeschpflicht und Archivierung

## Worum geht es konkret

Eine Person verlangt die Loeschung oder Anonymisierung eines Beitrags im Online-Archiv, weil dort identifizierbare Daten stehen (Aktenzeichen, Name, Lebenslauf, Lichtbild). Der Skill schluesselt die Abwaegung Loeschpflicht vs. Archivinteresse vs. Pressefreiheit nach DSGVO Art. 17 und dem Medienprivileg (Art. 85 DSGVO, MStV) und liefert Mustertexte fuer Ablehnung, Anonymisierung und Loeschung.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Wer verlangt was (Betroffener, Anwalt, Behoerde, Gericht)?
2. Welche Daten (Name, Az., Verfahrensdetails, Bild)?
3. Welches Medium (Online-Zeitschrift, Datenbank, Volltextarchiv, Loseblatt-Onlineversion)?
4. Wann wurde der Beitrag erstveroeffentlicht (Aktualitaet sinkt mit Zeit)?
5. Welcher Verfahrensstand (laufendes Verfahren vs. rechtskraeftig abgeschlossen)?
6. Gibt es Sperrwirkung nach BVerfG (z. B. nach Resozialisierungsgrundsatz)?
7. Pruefraster intern oder bereits Abmahnung / Klage?

## Rechtlicher und sachlicher Rahmen

- DSGVO Art. 17 - Recht auf Loeschung; Art. 18 Einschraenkung; Art. 21 Widerspruch.
- DSGVO Art. 85 - Medienprivileg; nationaler Umsetzungsspielraum.
- MStV §§ 9c-g und LDSG-Mediengesetze - Datenschutz-Regelungen fuer journalistisch-redaktionelle Telemedien.
- KUG §§ 22, 23 - Bildnisrecht.
- BVerfG, st. Rspr. zum Resozialisierungsgrundsatz (Lebach-Entscheidung BVerfGE 35, 202; zur Pruefung am Wortlaut unter bundesverfassungsgericht.de).
- BGH-Rechtsprechung zu Suchmaschinen-Auslistung und Online-Archivpflege; Folgeentscheidungen nach EuGH Google Spain (C-131/12).
- UrhG § 51 - Zitatrecht (bei Anonymisierung von Zitierten).

## Praxisleitfaden / Schritt fuer Schritt

1. **Eingang.** Loeschungsbegehren protokollieren mit Datum und Frist (DSGVO: einen Monat zur Antwort, verlaengerbar).
2. **Pruefraster anwenden.**
 - Tatsachenbehauptung oder Werturteil?
 - Aktualitaet noch gegeben?
 - Informationsinteresse (oeffentlich vs. privat)?
 - Identifizierbarkeit zwingend?
 - Medienprivileg einschlaegig?
3. **Abwaegung dokumentieren.** Pflicht zur Begruendung, auch bei Ablehnung.
4. **Optionen.**
 - Loeschung des gesamten Beitrags (nur in seltenen Faellen).
 - Anonymisierung (Initialen, generische Funktionsbeschreibung).
 - Korrektur einzelner Passagen mit Versionierung.
 - Ablehnung mit Begruendung; Hinweis auf Beschwerde und Klage.
5. **Datenbankanbieter informieren** (juris, beck-online): Aenderung muss in der Datenbank nachvollzogen werden.
6. **Backup-Pflichten.** Auch in internen Backups Anonymisierung sicherstellen, soweit zumutbar.
7. **Folgen kommunizieren.** Bei kompletter Loeschung Hinweisseite mit Datum.
8. **Archivierungsverpflichtungen** beruecksichtigen (Pflichtablieferung an Deutsche Nationalbibliothek; Loeschung dort nicht moeglich).

## Trade-off-Matrix

| Aspekt | Loeschung | Anonymisierung | Ablehnung mit Begruendung |
|---|---|---|---|
| Datenschutz | Maximal | Hoch | Niedrig |
| Wissenschaftliche Nachvollziehbarkeit | Verlust | Erhalten | Erhalten |
| Aufwand | Hoch (Backup, Cache) | Mittel | Niedrig |
| Folgerisiko | Niedrig | Mittel | Klage moeglich |
| Praezedenzwirkung | Stark | Mittel | Schwach |

## Praxistipps der alten Redaktion

- Aktenzeichen sind im juristischen Beitrag essentiell - Anonymisierung nur als Initialen, nicht Streichung.
- Identifizierbarkeit pruefen: bei kleinen Faechern reicht oft die Funktionsbeschreibung.
- Lebach-Logik: Bei lang zurueckliegenden Strafverfahren und Resozialisierung Pflicht zur Anonymisierung.
- Pflichtexemplare an Deutsche Nationalbibliothek koennen nicht zurueckgezogen werden; dortige Anfrage sinnlos.
- Bei Anonymisierung Versionierung im System; Original im internen Archiv bleibt.
- Ablehnung mit Begruendung schriftlich; sonst erscheint sie als ignorierte Beschwerde.
- Eilbedarf bei einstweiliger Verfuegung - 24-Stunden-Eskalation an Justiziariat.

## Mustertexte / Vorlagen

**Empfangsbestaetigung Loeschbegehren**

```
Sehr geehrte Frau/Herr [Name],

wir haben Ihr Loeschungsbegehren vom [Datum] erhalten und bestaetigen
hiermit den Eingang.

Wir werden Ihre Anfrage innerhalb der gesetzlichen Frist von einem
Monat (DSGVO Art. 12 Abs. 3) pruefen. Bei besonderer Komplexitaet
behalten wir uns eine Fristverlaengerung um zwei Monate vor.

Bitte teilen Sie uns mit, an welche Adresse wir die Entscheidung
senden duerfen, falls abweichend von dieser E-Mail.

Mit freundlichen Gruessen
[Datenschutzbeauftragter / Verlag]
```

**Antwort mit Anonymisierung**

```
Sehr geehrte Frau/Herr [Name],

Ihr Loeschungsbegehren vom [Datum] zum Beitrag "[Titel]" haben wir
geprueft.

Eine vollstaendige Loeschung lehnen wir ab. Begruendung:
- Der Beitrag dient der wissenschaftlichen Aufbereitung von [...].
- Das oeffentliche Informationsinteresse ueberwiegt im Sinne von
 DSGVO Art. 85 und der nationalen Mediengesetze.

Im Rahmen der Abwaegung haben wir jedoch beschlossen, im Beitrag
folgende Anonymisierungen vorzunehmen:
- Ihr Name wird durch Initialen ersetzt.
- Funktionsbezeichnung wird generisch.
- Wohnortangabe entfaellt.

Die Anonymisierung wird in der Online-Ausgabe und in den Datenbanken
[...] umgesetzt. Die Print-Ausgabe (Archiv und Pflichtexemplare)
bleibt unveraendert.

Gegen diese Entscheidung steht Ihnen das Recht auf Beschwerde bei
der zustaendigen Aufsichtsbehoerde (DSGVO Art. 77) und der Rechtsweg
offen.

Mit freundlichen Gruessen
[Name]
```

**Versionshinweis im Onlinearchiv**

```
AKTUALISIERUNGSHINWEIS
Diese Fassung wurde am [Datum] aktualisiert (Anonymisierungen
gemaess DSGVO Art. 17). Aenderungen im Vergleich zur Erstfassung
vom [Datum] betreffen ausschliesslich identifizierende Personen-
angaben. Inhaltliche Aenderungen wurden nicht vorgenommen.
```

## Typische Fehler / Pitfalls

- Loeschung ohne Pruefung des Medienprivilegs - Schaden fuer Archivlogik.
- Anonymisierung im Online-Volltext, aber nicht in der Datenbank - Inkonsistenz.
- Begruendung der Ablehnung fehlt - Beschwerde bei Aufsichtsbehoerde wahrscheinlich.
- Backup wird nicht angepasst - bei Restore wird Original wiederhergestellt.
- Frist von einem Monat verstrichen ohne Antwort - DSGVO-Verstoss.
- Loeschung mit Hinweis "wegen Loeschanspruch" ohne Datum - Streisand-Effekt.

## Querverweise

- `workflow-kaltstart-und-routing` - Eingangsroutung des Loeschbegehrens.
- `workflow-fristen-und-risikoampel` - DSGVO-Antwortfrist und Eilbedarf.
- `verl-richtigstellung-online-print` - bei Kombination Loeschung/Berichtigung.
- `verl-abstimmung-mit-rechtsabteilung-pruefung` - Justiziariatspflicht.
- `verl-rueckruf-fehlerbeitrag-spaet-erkannt` - parallele Rueckrufmassnahme.
- `ai-einsatz-transparenz-datenschutz` - bei KI-gestuetzter Personenanalyse.

## Quellen Stand 06/2026

- DSGVO Art. 12, 17, 18, 21, 77, 85 - Loeschung, Beschraenkung, Widerspruch, Beschwerde, Medienprivileg.
- MStV §§ 9c-g - Datenschutz fuer journalistisch-redaktionelle Telemedien.
- LDSG-Mediengesetze (z. B. NRW LMG) - jeweilige Landesfassung.
- KUG §§ 22, 23 - Bildnisrecht.
- BVerfG, Lebach (Volltext unter bundesverfassungsgericht.de); aktuelle Anschluss-Rechtsprechung pruefen.
- EuGH C-131/12 (Google Spain) - Loeschung in Suchindex; nachfolgende Rechtsprechung.
- BGH-Rechtsprechung zur Online-Archivierung (Volltexte unter bundesgerichtshof.de).

## 2. `verl-loseblattwerk-spezial`

**Fokus:** Spezialfall Loseblattwerk: Ergaenzungslieferung, Stichtag, Hinweisapparat, Abonnentenpflege. Pruefraster fuer Verlag und Redaktion.

# Verl: Loseblattwerk

## Spezialwissen: Verl: Loseblattwerk
- **Spezialgegenstand:** Verl: Loseblattwerk / verl loseblattwerk spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH, BVerfG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `verl-manuskript-merkwuerdige-formate-rettung`

**Fokus:** Rettet Manuskripte aus DOCX-/Markdown-/LaTeX-Mix, alten Word97-Dateien und KI-generiertem Wust; legt saubere Konvertierungspfade fuer die Verlagsredaktion.

# Manuskript-Rettung aus merkwuerdigen Formaten

## Worum geht es konkret

Autorinnen und Autoren liefern selten in der Form, die der Verlag braucht. Dieser Skill hilft, ein Manuskript aus einem unsauberen Eingangsformat (alte Word-Datei, gemischtes DOCX/Markdown, LaTeX-Fragmente, exportiertes PDF, mit KI generierter Wust) in ein verlagstaugliches Arbeitsdokument zu ueberfuehren - ohne juristischen Substanzverlust und ohne Fundstellenzerstoerung.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn, wenn Sie das Manuskript geoeffnet haben und sehen: kaputte Anfuehrungszeichen, gemischte Bullet-Stile, eingefrorene Tabellen, "smart quotes" im Quelltext, Word-Felder mit fehlenden Verweisen oder offenkundige LLM-Artefakte (Drei-Strich-Listen, Halbsatzbruch nach jedem zweiten Absatz). Klaeren Sie kurz:

1. Welches Quellformat liegt vor (.doc, .docx, .odt, .md, .tex, .rtf, .pdf, gemischt)?
2. Welches Zielformat braucht die Produktion (Verlags-DOCX-Vorlage, InDesign-XML, LaTeX-Klasse, XML-Auszeichnung fuer Online-Kommentar)?
3. Sind im Quelltext aktive Verweise / Felder / Track-Changes / Kommentare zu erhalten?
4. Wie hoch ist der KI-Verdacht (gleichfoermiger Absatzrhythmus, fehlende Pinpoints, "in der Regel"-Floskeln)?

## Material- bzw. Sachrahmen

- Ein Manuskriptfile (auch zip mit Anhaengen).
- Verlagsvorlage (.dotx oder Style-Sheet).
- Hinweisliste vom Autor zu Spezialzeichen, Sonderschreibweisen, Logos.

## Praxisleitfaden / Schritt fuer Schritt

1. **Sicherungskopie ablegen.** Original nie ueberschreiben. Arbeitsdatei kopieren, Versionsstand im Dateinamen (`Mueller-Aufsatz_v1-eingang.docx`).
2. **Format identifizieren.** Bei .doc unbedingt einmal in LibreOffice oder Word neu als .docx speichern, bevor weitere Tools darauf zugreifen.
3. **Pipeline waehlen** (siehe Trade-off-Matrix).
4. **Erste Bereinigung**: doppelte Leerzeichen, harte Zeilenumbrueche im Fliesstext, falsche Anfuehrungszeichen, geschuetzte Leerzeichen vor Paragraphenzeichen (`§ 433 BGB` mit U+00A0).
5. **Strukturmarkierung**: Absatzformate auf Verlagsvorlage (`Standard`, `Ueberschrift 1-3`, `Fussnotentext`, `Zitat`).
6. **Fussnoten und Felder pruefen**: keine Word-Felder mit fehlendem Bezug, keine zerschossenen `\ref`. Bei LaTeX in DOCX: BibTeX-Quellen separat sichern.
7. **KI-Artefakte markieren**: gleichfoermige Absatzlaenge, fehlende konkrete Pinpoints, generische Formulierungen wie "in der Literatur wird vertreten" ohne Quelle. Markieren, nicht still loeschen.
8. **Auslieferung**: Arbeitsdatei + Logfile der Konvertierung an Lektorat. Im Logfile festhalten, welche Schritte automatisiert, welche manuell waren.

## Trade-off-Matrix

| Pfad | A: Pandoc-Pipeline | B: Manuelle Word-Reinigung | Empfehlung |
|------|--------------------|----------------------------|------------|
| Aufwand | gering bei sauberen Quellen | hoch | A wenn .md/.tex/.docx eindeutig |
| Risiko | Verlust von Sonderformaten | langsame Drift | B wenn Tabellen / Felder kritisch |
| Reproduzierbar | ja, Skriptbasis | nein | A bei Serienkonvertierung |
| KI-Verdacht | Pandoc loescht nichts | Lektorat kann markieren | B fuer redaktionelle Beurteilung |

## Praxistipps der alten Redaktion

- "Word97-Files immer zuerst neu speichern lassen - es spart eine Stunde Suche nach kaputten Feldern."
- Bei LaTeX-Mix immer pruefen, ob im Quelltext `\footnote{}` oder `\cite{}` zerschossen wurde - Suche nach `\cite{??}`.
- KI-Manuskripte erkennt man oft am gleichfoermigen Absatzrhythmus und an fehlenden Randnummern bei zitierter Rspr. Markieren mit `[KI-Verdacht: Quelle pruefen]`.
- Bei verschluesselten oder passwortgeschuetzten PDFs niemals raten - Autor anrufen.

## Mustertexte / Vorlagen

**Anschreiben bei Format-Defekt:**

> Sehr geehrte Frau Dr. Mueller, Ihr Manuskript zu "Drittwirkung der Grundrechte" ist am 12.06.2026 eingegangen. Bei der technischen Eingangspruefung sind uns folgende Punkte aufgefallen, die wir vor dem Lektorat bereinigen muessten: (1) gemischte Anfuehrungszeichen, (2) zerschossene Verweise in Fussnoten 14, 27 und 41, (3) Tabelle 2 auf S. 18 ist als Bild eingefuegt. Wir wuerden Schritt 1 und 2 inhouse bereinigen; fuer Schritt 3 bitten wir um die Originaltabelle als .xlsx bis 19.06.2026. Mit freundlichen Gruessen, Redaktion NJW

**Pandoc-Pipeline (Bash-Snippet):**

```
pandoc input.docx --from=docx --to=docx --reference-doc=verlagsvorlage.dotx -o output.docx
pandoc input.tex --from=latex --to=docx --bibliography=quellen.bib -o output.docx
```

**Konvertierungs-Logfile (Vorlage):**

```
Datei: Mueller-Aufsatz_v1.docx
Datum: 12.06.2026
Quellformat: .docx (Word 365)
Schritte:
- Neu gespeichert in Word 365 (Format-Sanity)
- Pandoc: docx -> docx mit Verlagsvorlage
- Manuell: 17 doppelte Leerzeichen entfernt
- Manuell: 4 KI-Verdachtsstellen markiert (Fn 12, 19, 31, 47)
- Manuell: Tabelle 2 angefordert
Output: Mueller-Aufsatz_v2-clean.docx
```

## Typische Fehler / Pitfalls

- Originaldatei ueberschrieben - Versionsstand weg.
- Automatische Korrektur loescht stillschweigend Sonderzeichen (z. B. `§`, `Â§` durch Encoding-Mix).
- KI-Stellen unkommentiert uebernommen - Quellenpflicht verletzt.
- PDF-Konvertierung mit OCR ohne Pruefung - falsche Zahlen in Aktenzeichen.
- Track-Changes vom Autor verworfen statt aufgeloest.

## Querverweise

- `workflow-dokumentenintake` - allgemeiner Intake-im Plugin.
- `workflow-kaltstart-und-routing` - fuer die erste Weiche.
- `verl-zeitschriftenartikel-leitfaden` - wenn das Manuskript ein Zeitschriftenaufsatz wird.
- `lektorat-struktur-redaktion` - Anschluss-Skill nach erfolgter Bereinigung.
- `verl-formatvorlage-check-autor-manuskript` - strenger Formatvorlagen-Check als naechster Schritt.

## Quellen Stand 06/2026

- Pandoc User Guide, [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html) (Stand: laufend).
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024, Kapitel "Anfuehrungszeichen, Bindestrich, Sonderzeichen".
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016, S. 23 ff. zur Konsistenz bei Pinpoints.
- UrhG, [https://www.gesetze-im-internet.de/urhg/](https://www.gesetze-im-internet.de/urhg/) - Hinweis: bei Uebernahme fremder Tabellen / Grafiken aus PDF stets §§ 51, 63 UrhG pruefen.

## 4. `verl-newsletter-redaktion-jur`

**Fokus:** Newsletter-Redaktion juristisch: Konzept, Themenkasten, Empfaengerverwaltung nach DSGVO und UWG § 7, double opt-in, Mustertexte fuer wochen- und monatsweisen Versand.

# Newsletter-Redaktion juristisch

## Worum geht es konkret

Der Verlag betreibt einen oder mehrere Newsletter (Anwaltsbrief, Steuerletter, Update Mietrecht). Der Skill behandelt redaktionelle und rechtliche Pflichten: Themenmix, Anmeldung mit double opt-in, Impressum, Werbekennzeichnung, Abmeldelink, Datenschutzhinweise. Mit Mustertexten fuer Wochennewsletter, Monatsmagazin und Sonderausgabe.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Newsletter-Typ (woechentlich Curated, monatlich redaktionell, Sondernewsletter Eilthema, Buchempfehlung)?
2. Empfaengerverwaltung (eigenes Tool, Brevo, Mailchimp, CleverReach, Sendinblue)?
3. Anmeldung: double opt-in dokumentiert?
4. Wer ist redaktionell verantwortlich (V. i. S. d. P.)?
5. Sponsoring oder Anzeigen im Newsletter?
6. Welche Sprache (Du-Form, Sie-Form, Mischung)?
7. Versandtermin und Frequenz?

## Rechtlicher und sachlicher Rahmen

- UWG § 7 Abs. 2 Nr. 2 - Werbe-E-Mails nur mit vorheriger ausdruecklicher Einwilligung; Ausnahme § 7 Abs. 3 (bestehende Kundenbeziehung mit Hinweisrecht zur Abmeldung).
- DSGVO Art. 6 Abs. 1 lit. a - Einwilligung als Rechtsgrundlage; Art. 7 - Nachweisbarkeit; Art. 21 - Widerspruchsrecht.
- DDG § 5 - Impressumspflicht im Newsletter selbst (nicht nur auf Website).
- MStV § 18 - journalistische Sorgfaltspflicht.
- TTDSG / TDDDG § 25 - Einwilligung fuer Trackingpixel und Cookies.
- BGH zu double opt-in (BGH 10.02.2011 - I ZR 164/09); Bestaetigungsmail darf keine Werbung enthalten.

## Praxisleitfaden / Schritt fuer Schritt

1. **Anmeldung gestalten.** Klartext-Einwilligung, kein Vorhaken; Double-opt-in mit Bestaetigungsmail (rein technisch, keine Werbung).
2. **Empfaengerliste pflegen.** Nachweisbarkeit der Einwilligung pro Adresse (Zeitstempel, IP, Quelle).
3. **Themenmix entwickeln.** Standardrubriken (z. B. "Aktuelle Entscheidung", "Neuauflagen", "Veranstaltungstipp"); pro Ausgabe 5-7 Eintraege.
4. **Texte schreiben.** Eintrag aus drei Bausteinen: Hook (eine Zeile), Substanz (zwei bis vier Saetze, mit Quelle), Link (Volltext, Buch, Webinar).
5. **Impressum integrieren.** Im Footer jedes Newsletters, mit V. i. S. d. P., Anschrift, Vertretung.
6. **Abmeldelink** in jeder Ausgabe; Abmeldung mit einem Klick (BGH-Praxis).
7. **Werbekennzeichnung.** Anzeigen sichtbar als "Anzeige" markieren.
8. **Versand und Tracking.** Bei Tracking-Pixeln Einwilligung pruefen, alternativ trackingfrei versenden.
9. **Erfolgsmessung.** Open Rate, Klickrate, Abmeldequote; Abmeldequote > 1 Prozent ist Warnzeichen.

## Trade-off-Matrix

| Aspekt | Woechentlich | Monatlich |
|---|---|---|
| Aktualitaet | Hoch | Mittel |
| Redaktionsaufwand | Hoch | Mittel |
| Empfaenger-Ermuedung | Risiko | Niedrig |
| Werbeertrag | Hoch | Mittel |
| Datenschutzrisiko | Symmetrisch | Symmetrisch |

## Praxistipps der alten Redaktion

- Betreffzeile entscheidet ueber Open Rate; max. 50 Zeichen, konkret.
- Verzicht auf Personalisierung "Liebe Frau Mueller" wirkt seriaeser als Standard.
- Pflichtangaben Impressum nie im Bild verstecken (Spamfilter).
- Bestaetigungsmail des Double-opt-in beweissicher loggen (IP, Datum).
- Bei Eilthema (BGH-Aktuell) Sondernewsletter erlaubt, aber Frequenz im Anmeldeformular ausweisen.
- Abmeldelink ohne Login-Pflicht; sonst Abmahnungrisiko.
- Werbe-E-Mails nach UWG § 7 Abs. 3 (bestehende Kundenbeziehung) nur fuer aehnliche Produkte; bei Themenwechsel separate Einwilligung.

## Mustertexte / Vorlagen

**Anmeldeformular-Text**

```
Anmeldung Newsletter [Name]

Bitte tragen Sie hier Ihre E-Mail-Adresse ein. Wir senden Ihnen
[Frequenz] redaktionell aufbereitete Hinweise zu [Themen].

[ ] E-Mail-Adresse:

[ ] Ich willige ein, dass [Verlag] mir Newsletter und Hinweise zu
 eigenen Verlagsprodukten an die angegebene Adresse zusendet. Die
 Einwilligung kann ich jederzeit mit Wirkung fuer die Zukunft
 widerrufen, ohne dass die Rechtmaessigkeit der bisherigen Daten-
 verarbeitung beruehrt wird. Weitere Informationen in unserer
 Datenschutzerklaerung [Link].

[Button: Anmelden]

Nach Eingang erhalten Sie eine Bestaetigungsmail mit Link zur
endgueltigen Anmeldung (Double-opt-in).
```

**Bestaetigungsmail Double-opt-in**

```
Betreff: Bitte bestaetigen Sie Ihre Newsletter-Anmeldung

Sehr geehrte Empfaengerin, sehr geehrter Empfaenger,

Sie haben sich am [Datum, Uhrzeit] fuer den Newsletter [Name] des
[Verlag] angemeldet. Bitte bestaetigen Sie Ihre Anmeldung mit Klick
auf folgenden Link:

[Bestaetigungslink]

Falls Sie sich nicht angemeldet haben, ignorieren Sie diese E-Mail.

Mit freundlichen Gruessen
[Verlag]
```

**Footer mit Impressum und Abmeldung**

```
Impressum
[Verlag] - [Anschrift] - [Telefon]
V. i. S. d. P.: [Name]
Handelsregister: [Eintrag]
USt-ID: [Nummer]

Datenschutzerklaerung: [Link]

Sie erhalten diesen Newsletter, weil Sie sich am [Datum] mit der
E-Mail-Adresse [...] angemeldet haben.
Abmelden: [Direktlink ohne Login]
```

**Beispiel-Eintrag im Newsletter**

```
[Rubrik: AKTUELLE ENTSCHEIDUNG]

BGH zur Vermieterhaftung bei Schimmel
Der BGH hat am [Datum] (Az. [...]) entschieden, dass [...]. Die
Entscheidung praezisiert die [Norm] und hat Folgen fuer [...].

Mehr im Volltext: [Link Pressestelle BGH]
Vertiefend im Verlag: [Buchempfehlung mit ISBN]
```

## Typische Fehler / Pitfalls

- Single-opt-in statt double-opt-in - kein Beweis der Einwilligung.
- Werbe-Inhalt in Bestaetigungsmail - Verstoss gegen BGH-Praxis.
- Trackingpixel ohne TDDDG-Einwilligung.
- Abmeldelink mit Login-Pflicht oder Formular - faktische Verhinderung der Abmeldung.
- Impressum nur als Bild - Spamfilter und Barrierefreiheit.
- Empfaengerliste aus alten Datenbestaenden ohne Einwilligungsnachweis - DSGVO-Risiko.
- Sponsoring nicht als "Anzeige" markiert.

## Querverweise

- `workflow-kaltstart-und-routing` - Einordnung des Newsletteranlasses.
- `marketing-presse-social` - Marketing-Gesamtkonzept.
- `verl-pressetext-rechtsthemen` - parallele PM-Strecke.
- `verl-social-media-rechtsfachzeitschrift` - parallele Social-Strecke.
- `verl-impressum-pflicht-und-pruefung` - Impressumspflicht im Newsletter.
- `ai-einsatz-transparenz-datenschutz` - bei KI-gestuetzten Texten.

## Quellen Stand 06/2026

- UWG § 7 Abs. 2 Nr. 2, Abs. 3 - Werbe-E-Mails und Einwilligungspflicht.
- DSGVO Art. 6 Abs. 1 lit. a, Art. 7, Art. 21 - Einwilligung, Nachweis, Widerspruch.
- DDG § 5 - Impressumspflicht.
- TDDDG / TTDSG § 25 - Einwilligung fuer Tracking.
- MStV § 18 - journalistische Sorgfalt.
- BGH 10.02.2011 - I ZR 164/09 - Double opt-in (Volltext unter bundesgerichtshof.de und dejure.org).

## 5. `verl-online-kommentar-update-spezial`

**Fokus:** Spezialfall Online-Kommentar und Update-Workflow: Versionierung, Rechtsprechungsmonitoring, Verlinkung. Pruefraster fuer Verlag und Hauptbearbeiter.

# Verl: Online-Kommentar Update

## Spezialwissen: Verl: Online-Kommentar Update
- **Spezialgegenstand:** Verl: Online-Kommentar Update / verl online kommentar update spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
