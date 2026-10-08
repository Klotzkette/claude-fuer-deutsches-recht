# Output-Format - verbindliche Regeln für alle Plugins, Skills und Prompts

Diese Regeln gelten für jedes Arbeitsprodukt, das aus einem Skill, einem Megaprompt oder einem Miniprompt dieses Repos herausläuft: Schriftsätze, Repliken, Erwiderungen, Vergabevermerke, Rügen, Nichtabhilfen, Bekanntmachungen, Wertungsdokumente, Beratungsschreiben, Aktenvermerke, Stellungnahmen, Memos, Tabellen, Listen.

## Schriftbild

- Schriftart: Times New Roman.
- Schriftgrad: 11 pt.
- Zeilenabstand: 1,15 bis 1,3 (Standard 1,15). Bei Schriftsätzen für Vergabekammer oder OLG: 1,5, sofern die Geschäftsordnung der Stelle das verlangt.
- Seitenränder: 2,5 cm (oben, unten, links, rechts), bei Schriftsätzen links 3,0 cm für Heftungsrand.
- Blocksatz mit automatischer Silbentrennung; bei Tabellen und Aufzählungen linksbündig.
- Absatzabstand vor jedem neuen Hauptabschnitt 6 pt, sonst kein zusätzlicher Abstand.
- Keine farbigen Hervorhebungen, keine Hintergrundfarben, keine Rahmen außer bei Tabellen.
- Hervorhebung im Text ausschließlich durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, nicht durch Fettdruck oder Unterstreichung.
- Fußnoten: Times New Roman 9 pt, einzeilig.

## Nummerierung und Gliederung

Verbindlich für jedes mehrgliedrige Arbeitsprodukt:

1. Hauptabschnitt
   1.1 Unterabschnitt
       1.1.1 Detailpunkt
       1.1.2 Detailpunkt
   1.2 Unterabschnitt
2. Hauptabschnitt
   2.1 Unterabschnitt

Regeln:

- Eine durchgängige Dezimalgliederung (1, 1.1, 1.1.1, 2, 2.1, 2.1.1, ...). Keine römischen Ziffern als Hauptebene und keine A./B./C.-Gliederung, außer die Stelle (Gericht, Kammer, Behörde) verlangt das ausdrücklich.
- Maximale Tiefe vier Ebenen (1.1.1.1). Tiefer wird nicht gegliedert; tiefere Inhalte als Aufzählungspunkte unter der vierten Ebene führen.
- Jede Ebene beginnt mit Ziffer 1 und steigt streng aufsteigend ohne Lücken.
- Eine Ziffer wird nur vergeben, wenn ihr inhaltlich mindestens ein Geschwister gegenübersteht (kein einsames 1.1 ohne 1.2; sonst wird der Punkt unmittelbar in der nächsthöheren Ebene geführt).
- Hinter der Ziffer steht kein Klammerausdruck, sondern direkt die Überschrift.
- Anträge in Schriftsätzen werden ebenfalls dezimal nummeriert: Hauptantrag 1, 1.1, Hilfsanträge 2, 2.1, 2.2, weitere Hilfsanträge 3, 3.1.
- In Wertungsdokumenten und Bewertungsmatrizen wird die Nummerierung exakt aus der Bekanntmachung beziehungsweise den Vergabeunterlagen übernommen; sie wird nicht umsortiert.

## Aufzählungen

- Aufzählungen unterhalb der Nummerierungsebene mit Spiegelstrich (-) oder Bullet (•), keine Kreise, keine Pfeile.
- Aufzählungspunkte beginnen mit Großbuchstaben und enden mit Punkt.

## Tabellen

- Tabellen in Times New Roman 10 pt, Kopfzeile in Times New Roman 10 pt, sonst gleiches Format.
- Spaltenbreiten so wählen, dass keine Spalte unter 1,5 cm fällt; bei Bedarf Tabelle quer auf die Seite stellen.
- Tabellen werden in der Dezimalgliederung als Anlage (z.B. „Anlage 1") oder unter einer eigenen Zwischenüberschrift geführt, nie ohne Bezugspunkt eingestreut.

## Zitierweise (Kurzform)

- Gesetze: § 97 Abs. 1 GWB; Art. 18 Abs. 1 Richtlinie 2014/24/EU.
- Verordnungen mit Jahr: VgV; UVgO; VOB/A 2019; SektVO; KonzVgV.
- Entscheidungen: EuGH, Urteil vom TT.MM.JJJJ, Rs. C-XXX/JJ, Parteibezeichnung. BGH, Beschluss vom TT.MM.JJJJ, X ZB X/JJ. OLG Düsseldorf, Beschluss vom TT.MM.JJJJ, Verg X/JJ. VK Bund/Land, Beschluss vom TT.MM.JJJJ, Aktenzeichen.
- Fundstellen werden über die in `references/zitierweise.md` aufgeführten amtlichen Portale live verifiziert; keine Modellwissen-Zitate.

## Anrede, Anschrift, Datum

- Briefkopf: Absender oben links, Empfänger unter dem Briefkopf, Bezugszeile, Datum rechts.
- Datum im deutschen Format „Musterstadt, den TT. Monat JJJJ".
- Anrede konservativ: „Sehr geehrte Damen und Herren," bei Behörden und Vergabekammern; bei konkretem Ansprechpartner Name nennen.
- Grußformel: „Mit freundlichen Grüßen", danach Unterschriftsblock mit Funktion und Stelle.

## Dateinamen und Ausgabe

- Wenn ein Arbeitsprodukt als Datei abgegeben wird: Dateiname `JJJJ-MM-TT_<Aktenzeichen-oder-Vorgangsbezeichnung>_<Dokumenttyp>.docx` (oder `.pdf`, wenn die Stelle PDF verlangt).
- Falls nur Markdown möglich ist (z.B. Chatbot ohne DOCX-Export): Markdown-Ausgabe mit gleicher Dezimalgliederung. Im Markdown wird kein Fettdruck verwendet (siehe Repo-Konvention).

## Geltungsbereich

Diese Regeln gelten für alle Plugins (vergabestelle-behoerden, bieter-unternehmen, konkurrenten-rechtsschutz und alle künftig hinzukommenden), für alle Skills, alle Megaprompts und alle Miniprompts. Wenn ein Skill abweichende Formatvorgaben braucht (z.B. weil ein Portal ein bestimmtes Formular verlangt), wird die Abweichung im Skill ausdrücklich benannt und gilt nur dort.
