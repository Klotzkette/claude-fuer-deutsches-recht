---
name: output-alltagssprache-de
description: "Gibt das Subsumtionsergebnis in verstaendlicher Alltagssprache aus: ohne Fachbegriffe oder mit Erklärung, für Mandanten, Betroffene oder Behördenmitarbeiter. Behaelt die Strukturierung bei, vermeidet aber Lateinismen und Fachterminologie ohne Erklärung."
---

# Output: Alltagssprache (Deutsch)

## Zweck

Rechtliche Ergebnisse müssen auch für Menschen verständlich sein, die keine juristische Ausbildung haben. Dieser Skill übersetzt das Subsumtionsergebnis in klare, verständliche Alltagssprache. Er behält die inhaltliche Korrektheit bei, vermeidet aber unnötige Fachbegriffe und erklärt alle unvermeidlichen Rechtsbegriffe sofort.

## Triage zu Beginn

1. Wer ist der Adressat? (Mandant / Bürger / Behördenmitarbeiter ohne juristische Ausbildung)
2. Wie stark ist die juristische Vorbildung des Adressaten?
3. Muss der Brief fristgebunden sein? → Fristhinweis in Alltagssprache formulieren
4. Enthält das Ergebnis eine Empfehlung zum Handeln? → Handlungsaufforderung klar benennen
5. Liegt ein behördlicher Bescheid vor? → Rechtsmittelbelehrung in einfacher Sprache erklären

## Übersetzungsprinzipien

### Fachbegriffe ersetzen oder erklären

| Fachbegriff | Alltagssprache |
|------------|----------------|
| Anspruchsgrundlage | gesetzliche Grundlage, auf die Sie sich stützen |
| Tatbestandsmerkmal | Voraussetzung, die erfüllt sein muss |
| Subsumtion | Prüfung, ob Ihr Fall zur Regel passt |
| Verjährung | Frist, nach der Sie Ihr Recht nicht mehr einfordern können |
| Einrede | Gegenargument der anderen Seite |
| Widerrechtlichkeit | dass die Handlung verboten war |
| Schadensersatz | Ausgleich für einen Ihnen entstandenen Schaden |
| Kläger / Beklagter | die klagende Person / die verklagte Person |
| Verwaltungsakt | offizieller Bescheid einer Behörde |
| Grundrechtsverletzung | Verletzung Ihrer verfassungsrechtlich geschützten Rechte |
| Beweislast | Wer etwas beweisen muss, wenn es streitig wird |
| einstweilige Verfügung | dringende richterliche Sofortmaßnahme |
| Verzug | wenn jemand eine Pflicht nicht rechtzeitig erfüllt |
| Erfüllungsort | der Ort, an dem eine Leistung erbracht werden muss |

### Satzstruktur

- Kurze Sätze (max. 25 Wörter)
- Aktiv statt Passiv
- Konkrete Beispiele aus dem Nutzersachverhalt
- Keine Verweise auf Paragrafenzahlen ohne Erklärung des Inhalts
- Keine Genitivkonstruktionen ("Erfüllung der Leistungspflicht des Schuldners" → "wenn der Schuldner das, was er schuldet, erledigt hat")

## Struktur des Ausgabedokuments

### 1. Zusammenfassung in zwei Sätzen

Was geht es? Was ist das Ergebnis? Beispiel: "Sie möchten Geld zurück, weil das gekaufte Produkt kaputt war. Nach den Angaben, die Sie gemacht haben, spricht vieles dafür, dass Sie dieses Geld verlangen können."

### 2. Was musste gegeben sein?

Liste der Voraussetzungen in einfacher Sprache, mit Haken (erfüllt), Kreuz (nicht erfüllt) oder Fragezeichen (unklar).

### 3. Was bedeutet das für Sie?

Klare Aussage: Haben Sie (nach den genannten Angaben) einen Anspruch? Was können Sie konkret tun?

### 4. Was Sie jetzt brauchen

Checkliste: Welche Dokumente, welche nächsten Schritte, an wen wenden (Anwalt, Behörde, Schlichtungsstelle)?

### 5. Fristen

Falls eine Frist besteht: Klarer Hinweis mit Datum (wenn bekannt) und konkreter Handlungsaufforderung.

### 6. Wichtiger Hinweis

> **Dieses Ergebnis ist kein Rechtsrat.** Es zeigt Ihnen, was für und gegen Ihren Anspruch spricht, basierend auf dem, was Sie uns gesagt haben. Ob Sie wirklich Recht bekommen, hängt von vielen Dingen ab, die hier nicht geprüft werden konnten. Bitte wenden Sie sich an einen Rechtsanwalt, bevor Sie wichtige Schritte unternehmen.

## Sprachliche Qualitätssicherung

Das System vermeidet:
- Lateinische Begriffe ohne sofortige Erklärung
- Mehrfach verschachtelte Relativsätze
- Amtsdeutsch und Bürokratensprache ("hiermit", "infolgedessen", "vorgenannten")
- Passivkonstruktionen ohne erkennbares Subjekt

Das System prüft: Würde ein 16-Jähriger ohne Jurastudium diesen Text verstehen?

## Quellenregel

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren (dejure.org, bgh.de, bverfg.de).
- Gesetzestext in Alltagssprache paraphrasieren; Paragrafenzahl in Klammern ergänzen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (Bund), eur-lex.europa.eu (EU), dejure.org (Querverweise).
