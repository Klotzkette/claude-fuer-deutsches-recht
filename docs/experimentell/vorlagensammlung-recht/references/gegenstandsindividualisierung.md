# Gegenstandsindividualisierung und Anti-Generik-Doktrin

Dieser Standard ist verbindlich für jede Überarbeitung, Neufassung oder
Bewertung einer Vorlage, eines Legal-AI-Skills oder eines Legal-AI-Plugins in
diesem Repository. Er ergänzt `references/kautelarstandard.md`,
`references/regelungstiefe-vertraege.md` und `CLAUDE.md` Abschnitt 17.

Leitsatz: **Ein Satz, der unverändert in einem völlig anderen Dokument stehen
könnte, ist noch nicht spezifisch genug.** Die Vorlage darf Platzhalter
enthalten; die umgebende Sprache muss aber den konkreten Gegenstand, die
Parteien, die Interessenlage, die Risiken und den Zweck gerade dieses Dokuments
erkennbar tragen.

## 1. Gegenstand und Zweck vor jeder Änderung fixieren

Vor der ersten Textänderung wird intern festgelegt:

1.1 Was genau geregelt oder geleistet wird: konkreter Vertragsgegenstand,
Schriftsatzgegenstand, Formularzweck, Skill-Funktion oder Plugin-Leistung.

1.2 Wer beteiligt oder adressiert ist und welche Interessen in diesem Fall
aufeinandertreffen. Bei Verträgen sind das insbesondere Leistungsschuldner,
Gegenleistungsschuldner, Nutzerinnen und Nutzer, Sicherungsgeber,
Sicherungsnehmer, Erwerber, Veräußerer, Arbeitgeber, Betriebsrat, Behörde,
Gericht oder sonstige konkrete Rollen.

1.3 Welche Rechtsordnung und welches Rechtsgebiet die Fassung tragen. Default
ist deutsches Recht; unionsrechtliche oder internationale Bezüge werden nur
aufgenommen, wenn sie für den konkreten Gegenstand wirklich erheblich sind.

1.4 Welche fallspezifischen Besonderheiten, Risiken und Streitpunkte diesen
Gegenstand von ähnlichen Dokumenten unterscheiden. Dazu gehören etwa
Verbraucherschutz, notarielle Form, registerrechtlicher Vollzug,
aufsichtsrechtliche Erlaubnis, Datenschutz, Sicherheitenrang, Abnahme,
technische Schnittstellen, Zahlungsplan, Kündigungsrisiko, Beweislast,
Fristenlauf oder Zustellungsweg.

Jede Struktur-, Begriffs- und Formulierungsentscheidung muss danach auf diese
Festlegung zurückgeführt werden können.

## 2. Generische Formulierungen beseitigen

2.1 Eine Formulierung ist generisch, wenn sie ohne inhaltlichen Verlust in
einem anderen Vertrag, Schriftsatz, Formular, Skill oder Plugin stehen könnte.
Der Prüfmaßstab lautet nicht, ob der Satz „professionell klingt", sondern ob er
auf genau diesen Gegenstand einrastet.

2.2 Leerformeln werden durch gegenstandsspezifische Regelungen ersetzt. Statt
„die Parteien wirken zusammen" steht, wer welche Unterlage, Erklärung, Freigabe
oder technische Mitwirkung bis wann, in welcher Form und mit welcher Folge bei
Unterlassen erbringt.

2.3 Abstrakte Qualitätsmaßstäbe werden konkretisiert. Statt
„handelsübliche Qualität" beschreibt der Text die konkrete Beschaffenheit,
Spezifikation, Abnahmeprobe, Funktion, Dokumentation, Schnittstelle oder
Leistungskennzahl, die für dieses Geschäft zählt.

2.4 Austauschbare Definitionen werden eng auf das Vertrags- oder
Funktionsobjekt zugeschnitten. Eine Maschinenlieferung definiert die konkrete
Anlage, Peripherie, Software, Dokumentation, Schnittstellen, Testläufe und
Ersatzteile; sie definiert nicht allgemein „Waren". Ein StaRUG-Plan definiert
Gruppen, Forderungen, Planwirkungen und Vergleichsrechnung; er definiert nicht
abstrakt „Sanierungsmaßnahmen".

2.5 Standardballast entfällt. Klauseln ohne erkennbaren Regelungsbedarf für den
konkreten Gegenstand werden gestrichen, auch wenn sie in Musterverträgen üblich
sind. Korrekte juristische Vertragssprache bleibt erhalten, wenn sie
inhaltlich trägt.

## 3. Individualisierung nach Dokumenttyp

### 3.1 Verträge und sonstige Formatvorlagen

3.1.1 Der Text bildet den konkreten Leistungsaustausch ab: Leistung,
Gegenleistung, Mengen, Qualitäten, Termine, Übergabe, Abnahme, Mitwirkung,
Gefahrübergang, Nutzungsrechte, Vertraulichkeit, Datenschutz, Haftung,
Gewährleistung, Laufzeit, Beendigung und Vollzug nur in der Tiefe, die für
dieses Geschäft einschlägig ist.

3.1.2 Platzhalter bleiben nur dort stehen, wo echte Variabilität besteht. Jeder
Platzhalter steht in einem vollständigen Satz und enthält einen präzisen
Ausfüllhinweis, etwa `[konkreter Übergabeort]`, `[Frist in Bankarbeitstagen]`
oder `[Bezeichnung der gesicherten Forderung]`. In Vorlagen werden
Ausfüllfelder durchgehend in eckigen Klammern geschrieben.

3.1.3 Rubrum, Vertragseingang und Unterschriftenblock nennen die konkrete
Rollenlogik des Dokuments. Ein Bauträgervertrag unterscheidet Bauträgerin,
Erwerberin, Grundstück, Wohnungs- oder Teileigentum, Bauverpflichtung,
Zahlungsplan und Vormerkung; ein allgemeiner „Käufer/Verkäufer"-Kopf genügt
dort nicht.

3.1.4 Anlagen, Tabellen und Berechnungsschemata tragen den Zweck des Dokuments.
Eine Vergleichsrechnung zeigt nicht nur Spalten, sondern erläutert, welcher
Wert im Alternativszenario und welcher Wert im Planszenario angesetzt wird und
welche Position gerade nicht additiv gezählt werden darf.

### 3.2 Schriftsätze, Anträge und Behördenvorlagen

3.2.1 Der Antrag oder das Begehren ist vollziehbar, fristbezogen und auf die
zuständige Stelle zugeschnitten. Zuständigkeit, Frist, Form, Zugang,
Beweismittel, Anlagen und Rechtsfolge werden nicht als allgemeine Checkliste,
sondern im Ablauf dieses Verfahrens dargestellt.

3.2.2 Tatsachen werden beweisnah und chronologisch geschrieben. Jede
rechtserhebliche Behauptung erhält einen Beleg oder eine bewusst markierte
Prüfstelle.

### 3.3 Legal-AI-Skills

3.3.1 Skill-Instruktionen beschreiben genau die fachliche Aufgabe dieses
Skills: Eingaben, Zwischenschritte, Entscheidungspunkte, Selbstprüfung,
Fehlerfälle und Ausgabeformate.

3.3.2 Ein Skill enthält keine austauschbaren Aussagen wie „erstelle ein gutes
Dokument". Er benennt die konkrete juristische Arbeit, die anzuwendenden
Prüfschritte, die Grenzen des Modellwissens und die Fälle, in denen
Nutzerinnen und Nutzer externe Prüfung oder menschliche Freigabe brauchen.

### 3.4 Legal-AI-Plugins

3.4.1 Plugin-Beschreibungen benennen die konkrete Funktion, Parameter,
Rückgabewerte, Fehlerzustände, Rechte und Grenzen dieser Schnittstelle.

3.4.2 Fehlermeldungen und Hilfetexte erklären den konkreten Fehler und den
nächsten sinnvollen Schritt. Allgemeine Aussagen wie „etwas ist
fehlgeschlagen" genügen nicht.

## 4. Sprachliche Veredelung

4.1 Die Sprache folgt dem vorhandenen Dokument. Deutsch ist der Regelfall.
Englische Fassungen werden in idiomatischem Legal English geschrieben, ohne
Eindeutschungen und ohne falsche Freunde.

4.2 Überschriften benennen den konkreten Regelungsinhalt. „Sonstiges",
„Allgemeines", „Weitere Regelungen" oder „Schluss" werden nur verwendet, wenn
der Abschnitt tatsächlich mehrere abschließende Regelungen bündelt; sonst wird
die Überschrift konkretisiert.

4.3 Begriffe bleiben konsistent. Eine Rolle heißt nicht abwechselnd
„Anbieterin", „Verwenderin", „Auftragnehmerin" und „Dienstleisterin", wenn nur
eine Partei gemeint ist.

4.4 Der Text ist vollständig ausformuliert. Keine Stummelsprache, keine bloßen
Ankündigungen wie „hier regeln die Parteien die Vergütung", wenn die
Vergütungsregel selbst gebraucht wird.

## 5. Verbindliche Grenzen

5.1 Urteile, Aktenzeichen, Fundstellen und Literatur werden niemals erfunden.
Nicht verifizierte Quellen bleiben als Prüfbedarf markiert oder werden
weggelassen.

5.2 Vollständigkeit geht vor Kürze. Kein für den konkreten Gegenstand
einschlägiger Regelungsbereich darf fehlen; nicht einschlägige Bereiche werden
bewusst weggelassen und nicht durch Leerformeln ersetzt.

5.3 Fehlerhafte Substanz wird korrigiert. Die Anti-Generik-Arbeit ändert
nicht bloß Stil, sondern beseitigt erkennbare inhaltliche Unschärfen,
Widersprüche, falsche Querverweise und gegenstandsfremde Klauseln.

## 6. Freigabecheck

Vor Freigabe wird geprüft:

- Ist der konkrete Gegenstand in Abschnitt 1 des Arbeitsprozesses fixiert und
  im Dokument wiedererkennbar?
- Gibt es Sätze, die unverändert in einem anderen Dokument stehen könnten?
  Wenn ja, werden sie konkretisiert oder gestrichen.
- Sind Rollen, Fristen, Mengen, Qualitäten, Schnittstellen, Form,
  Rechtsfolgen und Risiken so weit benannt, wie der Gegenstand es verlangt?
- Sind Platzhalter nur dort gesetzt, wo echte Variabilität besteht?
- Sind Quellen, Querverweise, Anlagen, ODT-Fassung und Markdown-ZIP synchron?
