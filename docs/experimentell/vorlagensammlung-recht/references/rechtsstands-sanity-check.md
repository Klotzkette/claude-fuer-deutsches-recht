# Rechtsstands-Sanity-Check

Dieser Arbeitszettel ergänzt `CLAUDE.md`, `CONTRIBUTING.md` und
`references/pruefquellen.md`. Er ist für kurze Korrekturläufe gedacht, bei
denen nicht ein ganzes Rechtsgebiet neu geschrieben wird, sondern gezielt
geprüft wird, ob Vorlagen noch auf der richtigen Rechtslage und
Rechtsprechung beruhen.

## 1. Ziel

Der Rechtsstands-Sanity-Check soll drei Dinge leisten:

1. Offensichtlich überholte Normbezüge, Formanforderungen und Übergangsregeln
   finden.
2. Rechtsprechungsanker nur dort stehen lassen, wo sie als Quelle oder
   Rechercheanker sauber eingeordnet sind.
3. Korrekturen klein halten: Eine belastbar falsche Stelle wird berichtigt;
   unsichere Fragen werden als `[noch zu klären: …]` markiert oder in die
   README verlagert.

## 2. Prüfungsreihenfolge

1. Vollständigen Arbeitsstand ziehen und `python3 scripts/check-all.py`
   laufen lassen.
2. Fehlermeldungen der Validatoren zuerst beheben. Ein formaler Fehler kann
   einen materiellen Fehler verdecken, etwa eine unzulässige
   Gegenstandszeile im Rubrum.
3. Danach gezielt nach bekannten Rechtsstandsfallen suchen. Beispiele:

```bash
rg -n "Privacy Shield|Safe Harbor|§ 12 VVG|TTDSG|KAWG|Schriftform gemäß § 40 UrhG|schriftliche Ablehnung|Gegenstand:" --glob "*.md"
```

4. Treffer nicht mechanisch ersetzen. Zuerst prüfen, ob die Stelle
   tatsächlich eine falsche Aussage trifft oder nur einen überholten Begriff
   als Warnbeispiel nennt.
5. Für jede fachliche Korrektur die Primärquelle prüfen: Gesetzestext,
   amtliche Entscheidungsdatenbank, Gericht, Behörde oder EU-Amtsblatt.
6. Nach jeder Änderung an einer Hauptvorlage die ODT-Datei und die
   Markdown-ZIP-Datei neu erzeugen.
7. Abschließend erneut den vollständigen Gate laufen lassen.

## 3. Typische Risikofelder

1. Formvorschriften: Schriftform, Textform, qualifizierte elektronische
   Signatur, notarielle Form, elektronische Einreichung und Übergangsrecht
   nicht vermischen.
2. Fristen: Beginn, Dauer, Hemmung, Wiedereinsetzung, Fiktion und
   Übergangsrecht getrennt prüfen.
3. Zuständigkeit: Rechtsweg, sachliche Zuständigkeit, Wertgrenzen,
   Spezialkammern und Übergangsvorschriften nach Eingangsdatum trennen.
4. Datenschutz und Plattformrecht: aufgehobene Transferinstrumente,
   TDDDG-Bezüge, DSA-Verfahrenspflichten und DSGVO-Fristen nicht nach alter
   Terminologie fortschreiben.
5. Aufsichtsrecht und Krypto: nationale Spezialnorm, EU-Verordnung,
   Übergangsregime und konkrete Erlaubnisrolle auseinanderhalten.
6. Urheber- und Medienrecht: Nutzungsart, Rechtekette, unbekannte
   Nutzungsarten, künftige Werke, Landespressegesetze und gerichtliche
   Eilmechanik nicht in eine Pauschalklausel ziehen.

## 4. Korrekturmaßstab

Eine Korrektur ist releasefähig, wenn sie alle vier Punkte erfüllt:

1. Die bisherige Aussage ist nach aktueller Primärquelle falsch,
   missverständlich oder formal validatorwidrig.
2. Die neue Aussage ist enger, genauer und besser prüfbar.
3. Der Eingriff bleibt auf die betroffene Vorlage, README, ODT, ZIP und den
   Changelog beschränkt.
4. `python3 scripts/check-all.py` läuft grün.

Wenn eine Aussage nur zweifelhaft ist, aber nicht sicher falsch, bleibt sie
nicht als Behauptung im Mustertext stehen. Sie wird entweder als
`[noch zu klären: …]` markiert oder in der README als Prüfhinweis formuliert.

## 5. Dokumentation im PR

Der PR-Text nennt:

1. Welche Rechtsstandsfallen gesucht wurden.
2. Welche Treffer bewusst nicht geändert wurden, weil sie nur Warnbeispiele
   oder Suchanker sind.
3. Welche Primärquellen die Korrektur tragen.
4. Welche ODT- und ZIP-Artefakte neu erzeugt wurden.
5. Den vollständigen Gate-Status.
