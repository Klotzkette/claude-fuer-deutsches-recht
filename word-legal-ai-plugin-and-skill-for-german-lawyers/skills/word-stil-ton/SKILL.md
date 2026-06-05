---
name: word-stil-ton
description: "Stil TON: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Stil TON

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Stil TON** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-word-erstpruefung-und-mandatsziel` | Word: Erstprüfung, Rollenklärung und Mandatsziel im Plugin word legal ai plugin and skill for german lawyers; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `stil-und-ton-juristische-texte` | Adressatengerechte Schreibhygiene fuer juristische Texte. Bestimmt Register und Ton je nach Adressat: Mandantenbrief klar und mit Empfehlung, Gegenseitenbrief kuehl und mit Frist, Schriftsatz urteilsstil und beweisbar, Memo gutachtenstil, Behoerdenschreiben nuechtern. Mit Tabelle Adressat zu Register zu Beispielsatz, Sie-Form als Default und konkreten Anti-Mustern. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Stil TON**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-word-erstpruefung-und-mandatsziel`

**Fokus:** Word: Erstprüfung, Rollenklärung und Mandatsziel im Plugin word legal ai plugin and skill for german lawyers; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Word: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Word: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Word: Erstprüfung, Rollenklärung und Mandatsziel / word erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, DE, EN, US, UK.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Word** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `stil-und-ton-juristische-texte`

**Fokus:** Adressatengerechte Schreibhygiene fuer juristische Texte. Bestimmt Register und Ton je nach Adressat: Mandantenbrief klar und mit Empfehlung, Gegenseitenbrief kuehl und mit Frist, Schriftsatz urteilsstil und beweisbar, Memo gutachtenstil, Behoerdenschreiben nuechtern. Mit Tabelle Adressat zu Register zu Beispielsatz, Sie-Form als Default und konkreten Anti-Mustern.

# Stil und Ton juristischer Texte

## Zweck

Juristische Texte erreichen ihr Ziel nur, wenn Stil und Ton zum Adressaten passen. Ein Mandantenbrief im Schriftsatzton verunsichert; ein Schriftsatz im Coaching-Ton wirkt unprofessionell. Dieser Skill macht die Wahl des Registers explizit und reproduzierbar.

Er ist kein Stillehrer, sondern eine Pruefcheckliste. Er sagt Ihnen, welches Register zu welchem Adressaten passt, und liefert pro Adressat Beispielsaetze.

Im Zweifel gilt: Sie-Form, nuechterner Ton, kurze Saetze, klare Empfehlung am Ende.

## Eingaben

- Textentwurf oder Textaufgabe
- Adressat (Mandant, Gegenseite, Gericht, Behoerde, intern)
- Anlass (Erstkontakt, Mahnung, Vergleichsangebot, Schriftsatz, Memo)
- Ggf. Praeferenz des Mandats (formell, vertraulich, deeskalierend)

## Rechtlicher und methodischer Rahmen

- § 43a Abs. 3 BRAO: Sachlichkeitsgebot. Anwalt darf nicht herabwuerdigen oder beleidigen.
- § 11 BORA: Mandantenkommunikation. Klar und unverzueglich.
- CLAUDE.md im Repository: Sie-Form als Standardregister; Du-Form nur, wenn Mandat es vorgibt.
- Methodische Grundlage: Gutachtenstil fuer Memos, Urteilsstil fuer Schriftsaetze. Siehe `references/methodik-buergerliches-recht.md`.

## Ablauf / Checkliste

1. **Adressat identifizieren.** Wer liest? Wer entscheidet?
2. **Register waehlen.** Tabelle unten konsultieren.
3. **Anrede festlegen.** "Sehr geehrte Frau ...", "Sehr geehrter Herr ...", "Sehr geehrtes Gericht", "Sehr geehrte Damen und Herren".
4. **Empfehlung am Ende.** Mandantenbrief und Gegenseitenbrief enthalten Handlungsempfehlung oder Frist.
5. **Sachlichkeitsfilter.** Streichen Sie Adjektive ohne Funktion ("voellig unverstaendlich", "schlichtweg falsch", "offenkundig").
6. **Frist immer beziffert.** "kurzfristig" wird zu "bis zum Datum".

### Tabelle Adressat zu Register

| Adressat | Stil | Ton | Lieblings-Satzbau |
|---|---|---|---|
| Mandant | Mandantenbrief, gegliedert | Klar, beratend, nicht herablassend | "Wir empfehlen, dass Sie ..." |
| Gegenseite | Anwaltsschreiben | Kuehl, praezise, mit Frist | "Wir fordern Sie auf, bis zum ..." |
| Gericht | Schriftsatz, Urteilsstil | Knapp, sachlich, beweisbar | "Die Klage ist begruendet, weil ..." |
| Behoerde | Antragsschrift, sachlich | Nuechtern, formal, ohne Polemik | "Es wird beantragt, ..." |
| Intern (Memo) | Gutachtenstil | Pruefend, abwaegend | "Es koennte ... Dazu muesste ..." |
| Gegenanwalt | Schriftverkehr Anwalt zu Anwalt | Kollegial-distanziert | "Sehr geehrte Frau Kollegin, ..." |

### Sieben Stilregeln

1. Sie-Form. Du-Form nur bei ausdruecklicher Vorgabe.
2. Aktiv vor Passiv.
3. Subjekt vor Praedikat. Verschachtelte Saetze meiden.
4. Ein Gedanke, ein Satz. Maximal 25 Woerter.
5. Keine Adjektivkette ohne Funktion.
6. Keine Wertungen, die nicht der Mandant traegt.
7. Empfehlung oder naechster Schritt am Ende.

### Beispielsaetze nach Adressat

**Mandantenbrief:** "Wir empfehlen, der Aufforderung nicht zu folgen, weil die Gegenseite den Anspruch nicht ausreichend belegt hat. Eine Antwort ist bis zum 12. Juni 2026 erforderlich. Bitte teilen Sie uns mit, ob Sie diese Linie billigen."

**Gegenseitenbrief:** "Wir vertreten Frau Mustermann. Namens und in Vollmacht unserer Mandantin fordern wir Sie auf, den Betrag von 8.450 Euro bis zum 12. Juni 2026 auf das Konto IBAN ... zu zahlen. Bei fruchtlosem Fristablauf werden wir Klage erheben."

**Schriftsatz (Urteilsstil):** "Die Klage ist begruendet. Der Klaegerin steht der geltend gemachte Anspruch aus § 433 Abs. 2 BGB zu. Die Beklagte hat den Kaufpreis trotz Faelligkeit am 1. April 2026 nicht gezahlt."

**Memo (Gutachtenstil):** "Es koennte ein Anspruch der A gegen B aus § 280 Abs. 1 BGB bestehen. Dazu muesste ein Schuldverhaeltnis zwischen A und B vorliegen ..."

**Behoerdenbrief:** "Mit anliegender Vollmacht zeige ich an, dass ich die Rechte des Herrn Mustermann wahrnehme. Es wird beantragt, Akteneinsicht zu gewaehren. Eine Reaktion bis zum 12. Juni 2026 wird erbeten."

## Typische Drafting-Fehler

- **Mandantenbrief in Schriftsatzsprache.** "Anspruchsgrundlagen", "Tatbestandsmerkmale", "Subsumtion" gehoeren nicht in den Mandantenbrief, es sei denn, der Mandant ist Volljurist.
- **Schriftsatz mit Polemik.** "Es ist schlichtweg unverstaendlich" verstoesst gegen § 43a Abs. 3 BRAO.
- **Behoerdenbrief mit Wertungen.** Verwaltung mag kuehle Sachlichkeit.
- **Memo ohne Kurzantwort.** Gutachtenstil ohne Ergebnissatz ist unlesbar.
- **Gegenseitenbrief ohne Frist.** Ohne Frist keine Verzugswirkung.
- **Bratwurst-Saetze.** Saetze ueber drei Zeilen sind nur in der Hauptbegruendung eines Schriftsatzes vertretbar, und auch dort selten.

## Ausgabeformat

- Stilbefund (Adressat erkannt, Register bewertet).
- Ueberarbeitungsvorschlag mit konkret zitiertem Originalsatz und Alternative.
- Optional: Komplett-Neuentwurf im richtigen Register.

## Beispiel

**Original (Mandantenbrief, fehlerhaft):** "Vorstehend duerften die Tatbestandsmerkmale des § 433 BGB erfuellt sein, was kausal die im Tenor begehrte Rechtsfolge zu tragen vermag, weshalb wir Ihnen vorschlagen, in Erwaegung zu ziehen, ob Sie nicht doch zur Zahlung schreiten wollen."

**Ueberarbeitet:** "Nach unserer Einschaetzung sind Sie zur Zahlung verpflichtet. Wir empfehlen, den Betrag bis zum 12. Juni 2026 zu ueberweisen. Sollten Sie der Einschaetzung nicht folgen, schlagen wir ein kurzes Telefonat vor."

## Querverweise

- `drafting-prinzipien-klarheit-bestimmtheit-praezision`
- `anwaltsschreiben-aussergerichtlich`
- `gutachten-memo-internes-drafting`
- `dokumentarchitektur-vertrag-und-schriftsatz`

## Quellen (Stand 05/2026)

- § 43a Abs. 3 BRAO; § 11 BORA. gesetze-im-internet.de und brak.de fuer aktuelle Fassung.
- CLAUDE.md im Repository fuer Sie-Form und Methodikvorgaben.
- `references/methodik-buergerliches-recht.md` fuer Gutachtenstil und Urteilsstil.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
