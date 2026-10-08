---
name: vergabeakte-dokumentationsvermerk-builder
description: "Vergabeakte der Behörde reproduzierbar aufbauen: ordnet Originale, Versionen, Kommunikation, Entscheidungen und Freigaben entlang Paragraf 8 VgV, erkennt Beleglücken und erzeugt Vergabevermerk, Index und exportierbares Aktenmanifest."
---

# Vergabeakte und Vergabevermerk aufbauen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Aktenstruktur

Originale unverändert in Phasen ordnen: Bedarf und Budget, Markterkundung, Auftragswert/Regime, Verfahrenswahl, Bekanntmachung, Unterlagen/Versionen, Kommunikation, Teilnahmeanträge, Angebote/Öffnung, Eignung/Ausschluss, Aufklärung, Wertung, § 134-Information, Rügen, Zuschlag, Vertrag und Änderungen. Arbeitskopien und Entwürfe kennzeichnen.

## Fortlaufende Dokumentation

§ 8 Abs. 1 VgV verlangt Dokumentation von Beginn an und auf jeder Entscheidungsstufe. Für jedes Ereignis festhalten:

| Zeitpunkt | Entscheidung/Kommunikation | verantwortliche Person | Tatsachen | Norm/Kriterium | Originalfundstelle | Freigabe |
|---|---|---|---|---|---|---|

Nachträgliche Ergänzungen als solche mit Autor, Datum, Anlass und zugrunde liegenden zeitnahen Belegen kennzeichnen. Keine rückdatierte Begründung. Portalexporte, E-Mails, Tabellenformeln, Bewertungsstände und Sitzungsnotizen in lesbarer Form erhalten.

## Vergabevermerk nach § 8 Abs. 2 VgV

Mindestens Auftraggeber, Gegenstand und Wert, berücksichtigte und nicht berücksichtigte Unternehmen samt Gründen, ungewöhnlich niedrige Angebote, Zuschlagsempfänger und Auswahlgrund, Unterauftragnehmer soweit bekannt sowie einschlägige Sonderentscheidungen aufnehmen. Verfahrensausnahmen, Aufhebung, nicht elektronische Mittel, Interessenkonflikte, Loszusammenfassung und fehlende Kriteriengewichtung nur mit konkreter Begründung dokumentieren.

Aufbewahrung nach § 8 Abs. 4 VgV und längere haushalts-, förder-, revisions-, steuer- oder vertragsrechtliche Fristen in einem Lösch- und Sperrplan zusammenführen. Vertraulichkeit nach § 5 VgV sowie Akteneinsichtsrisiken markieren.

## Exportfähigkeit

Jede Datei erhält stabile ID, verständlichen Namen, Dokumentdatum, Eingangsdatum, Quelle, Version, Vertraulichkeitsstufe und Hashwert. Das Manifest bildet Beziehungen zwischen Bekanntmachung, Unterlagenversion, Bieterfrage, Angebot, Prüfung und Entscheidung ab. Fehlende oder nicht lesbare Anhänge werden nicht durch Platzhalter als vorhanden ausgegeben.

## Pflichtoutput

1. Aktenindex mit Phase, ID, Dateipfad, Datum, Quelle und Status.
2. Chronologie und Entscheidungslog.
3. Lückenliste nach Risiko und spätestem Schließzeitpunkt.
4. Ausformulierter Vergabevermerk nach § 8 VgV.
5. Exportmanifest für ZIP, DMS oder Prüfbehörde einschließlich Hashwerten und Vertraulichkeitskennzeichnung.
