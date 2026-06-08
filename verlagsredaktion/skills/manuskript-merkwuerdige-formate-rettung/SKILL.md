---
name: manuskript-merkwuerdige-formate-rettung
description: "Rettet Manuskripte aus DOCX-/Markdown-/LaTeX-Mix, alten Word97-Dateien und KI-generiertem Wust; legt saubere Konvertierungspfade für die Verlagsredaktion im Verlagsredaktion."
---

# Manuskript-Rettung aus merkwuerdigen Formaten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: VerlG § 17 Ablieferungsfrist, UrhG § 41 Rückrufsrecht wegen Nichtausübung nach 2 Jahren, VG-Wort-Meldungen jährlich, JuSchG-Indizierung sofort wirksam.
- Tragende Normen verifizieren: UrhG §§ 1, 7, 11, 31, 32, 34, 38, 41, 43, 50, 51, 51a, 53, 87a-h, VerlG, BGB §§ 433, 631, JuSchG, PresseG der Länder, ImpressumsR, DSGVO Art. 85 (Medienprivileg) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verlag, Autor, Lektor, Übersetzer, VG Wort, Lizenzpartner, Vertrieb, Datenschutzbeauftragter, ggf. Bundeszentrale für Kinder- und Jugendmedienschutz.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verlagsvertrag, Übersetzervertrag, Lizenzvertrag, Honorarrechnung, Pflichtexemplarmeldung, VG-Wort-Meldung, Impressum, AGB — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum geht es konkret

Autorinnen und Autoren liefern selten in der Form, die der Verlag braucht. Dieser Skill hilft, ein Manuskript aus einem unsauberen Eingangsformat (alte Word-Datei, gemischtes DOCX/Markdown, LaTeX-Fragmente, exportiertes PDF, mit KI generierter Wust) in ein verlagstaugliches Arbeitsdokument zu ueberfuehren - ohne juristischen Substanzverlust und ohne Fundstellenzerstoerung.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn, wenn Sie das Manuskript geoeffnet haben und sehen: kaputte Anfuehrungszeichen, gemischte Bullet-Stile, eingefrorene Tabellen, "smart quotes" im Quelltext, Word-Felder mit fehlenden Verweisen oder offenkundige LLM-Artefakte (Drei-Strich-Listen, Halbsatzbruch nach jedem zweiten Absatz). Klaeren Sie kurz:

1. Welches Quellformat liegt vor (.doc, .docx, .odt, .md, .tex, .rtf, .pdf, gemischt)?
2. Welches Zielformat braucht die Produktion (Verlags-DOCX-Vorlage, InDesign-XML, LaTeX-Klasse, XML-Auszeichnung für Online-Kommentar)?
3. Sind im Quelltext aktive Verweise / Felder / Track-Changes / Kommentare zu erhalten?
4. Wie hoch ist der KI-Verdacht (gleichfoermiger Absatzrhythmus, fehlende Pinpoints, "in der Regel"-Floskeln)?

## Material- bzw. Sachrahmen

- Ein Manuskriptfile (auch zip mit Anhaengen).
- Verlagsvorlage (.dotx oder Style-Sheet).
- Hinweisliste vom Autor zu Spezialzeichen, Sonderschreibweisen, Logos.

## Praxisleitfaden / Schritt für Schritt

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
| KI-Verdacht | Pandoc loescht nichts | Lektorat kann markieren | B für redaktionelle Beurteilung |

## Praxistipps der alten Redaktion

- "Word97-Files immer zuerst neu speichern lassen - es spart eine Stunde Suche nach kaputten Feldern."
- Bei LaTeX-Mix immer pruefen, ob im Quelltext `\footnote{}` oder `\cite{}` zerschossen wurde - Suche nach `\cite{??}`.
- KI-Manuskripte erkennt man oft am gleichfoermigen Absatzrhythmus und an fehlenden Randnummern bei zitierter Rspr. Markieren mit `[KI-Verdacht: Quelle pruefen]`.
- Bei verschluesselten oder passwortgeschuetzten PDFs niemals raten - Autor anrufen.

## Mustertexte / Vorlagen

**Anschreiben bei Format-Defekt:**

> Sehr geehrte Frau Dr. Mueller, Ihr Manuskript zu "Drittwirkung der Grundrechte" ist am 12.06.2026 eingegangen. Bei der technischen Eingangspruefung sind uns folgende Punkte aufgefallen, die wir vor dem Lektorat bereinigen muessten: (1) gemischte Anfuehrungszeichen, (2) zerschossene Verweise in Fussnoten 14, 27 und 41, (3) Tabelle 2 auf S. 18 ist als Bild eingefuegt. Wir wuerden Schritt 1 und 2 inhouse bereinigen; für Schritt 3 bitten wir um die Originaltabelle als .xlsx bis 19.06.2026. Mit freundlichen Gruessen, Redaktion NJW

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

## Quellen Stand 06/2026

- Pandoc User Guide, [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html) (Stand: laufend).
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024, Kapitel "Anfuehrungszeichen, Bindestrich, Sonderzeichen".
- Byrd / Lehmann, Zitierfibel für Juristen, 2. Aufl. 2016, S. 23 ff. zur Konsistenz bei Pinpoints.
- UrhG, [https://www.gesetze-im-internet.de/urhg/](https://www.gesetze-im-internet.de/urhg/) - Hinweis: bei Uebernahme fremder Tabellen / Grafiken aus PDF stets §§ 51, 63 UrhG pruefen.

