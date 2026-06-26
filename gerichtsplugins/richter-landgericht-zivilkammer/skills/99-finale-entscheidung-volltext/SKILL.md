---
name: 99-finale-entscheidung-volltext
description: Erzeugt die finale entscheidung als volltext (urteil zivilkammer) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung.
---

# Finale Entscheidung als Volltext (Urteil Zivilkammer)

## Zweck

Dieser Skill erzeugt die finale Entscheidung des Spruchkörpers nicht als bloßen Vorschlag oder Votum, sondern als versandfertigen Volltext im richtigen Layout — so, wie er das Gericht verlassen würde. Die Entscheidung wird zur Unterschrift fertig gebaut: mit Rubrum, vollständigem Tenor, Tatbestand oder Sachverhalt, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung.

Gegenstand: Urteil der Zivilkammer beim Landgericht.

## Rechtlicher Rahmen

Paragrafen 313, 313a ZPO; Paragrafen 91 ff. ZPO; Paragrafen 708, 709 ZPO für vorläufige Vollstreckbarkeit beim Landgericht.

## Eingangsvoraussetzungen

Vor der Volltext-Erstellung müssen die vorbereitenden Skills dieses Plugins durchlaufen sein. Insbesondere müssen vorliegen:

- Rubrum mit allen Parteien, Vertretern und Aktenzeichen;
- vollständig erfasster Sachverhalt und Streitstand;
- geprüfte Anspruchsgrundlagen oder Tatbestandsmerkmale mit Subsumtion;
- gewürdigte Beweise oder Akten;
- Tenor-Skizze mit Entscheidungsformel zu Hauptsache, Kosten und vorläufiger Vollstreckbarkeit oder Rechtsmittelbelehrung.

Fehlt eines dieser Stücke, weist der Skill darauf hin und unterbricht die Volltext-Erstellung, bevor er Phantasie produziert.

## Aufbau des Volltextes

### 1. Briefkopf und Rubrum

Gerichtsbezeichnung in der ersten Zeile (zum Beispiel „Amtsgericht München"), Aktenzeichen, Verkündungsdatum, vollständiges Rubrum mit Parteien, Prozessbevollmächtigten, Streitgegenstand und Spruchkörper.

### 2. Tenor (Entscheidungsformel)

Der Tenor wird vollständig ausformuliert. Er ist die rechtskraftfähige Anordnung. Beispiel für diesen Spruchkörper:

1. Die Beklagte wird verurteilt, an die Klägerin EUR 85.000 nebst Zinsen in Höhe von fuenf Prozentpunkten über dem Basiszinssatz seit Rechtshängigkeit zu zahlen.
2. Im Übrigen wird die Klage abgewiesen.
3. Von den Kosten des Rechtsstreits tragen die Klägerin 15 Prozent und die Beklagte 85 Prozent.
4. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 Prozent des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.

Der Tenor enthält zwingend: Hauptausspruch zur Sache, Kostenentscheidung, ggf. Aussprache zur vorläufigen Vollstreckbarkeit, ggf. Streitwertfestsetzung.

### 3. Tatbestand oder Sachverhalt

Knappe, sachlich-distanzierte Darstellung des unstreitigen Sachverhalts und des streitigen Parteivortrags. Bei Beschlüssen entsprechend „Gründe I."; bei Strafurteilen die Feststellungen zum Tatgeschehen. Verwende den Imperfekt für Geschehensschilderung, das Präsens für Antrag und Verfahrensstand.

### 4. Entscheidungsgründe

Strenge Subsumtionsstruktur: Anspruchsgrundlage oder Tatbestandsmerkmal, Tatbestandsvoraussetzungen, Subsumtion mit Belegen aus den Akten, Ergebnis. Einreden und Einwendungen am Ende der jeweiligen Prüfungsebene. Bei Strafurteilen Beweiswürdigung und Strafzumessung getrennt darstellen.

### 5. Nebenentscheidungen

Kosten, vorläufige Vollstreckbarkeit, Streitwertfestsetzung. Bei Familien- und Sozialsachen die jeweils einschlägigen Kostenregeln.

### 6. Rechtsmittelbelehrung

Vollstaendige Belehrung über statthaftes Rechtsmittel, Frist, Form und Adressat. Niemals weglassen, niemals abkuerzen.

### 7. Unterschriftenzeile

Ort, Datum, Name(n) der entscheidenden Berufs- und Laienrichter mit Funktionsbezeichnung. Bei Verhinderung Vertretungsvermerk.

## Prozessuale Glanzkontrolle

Vor der finalen Entscheidung wird zwingend geprüft:

1. Antrag, Rechtsschutzziel und Tenor sind deckungsgleich und vollstreckbar.
2. Schlüssigkeit, Erheblichkeit, Beweisbedürftigkeit und Beweislast wurden nicht vermischt.
3. Hinweise nach Paragraf 139 ZPO sind bei überraschenden oder übersehenen Punkten früh, konkret und aktenkundig erteilt.
4. Artikel 103 Absatz 1 GG ist sichtbar gewahrt: entscheidungserheblicher Vortrag ist zur Kenntnis genommen und erwogen.
5. Beweiswürdigung nach Paragraf 286 ZPO und gegebenenfalls Schätzung nach Paragraf 287 ZPO sind nachvollziehbar begründet.
6. Nebenentscheidungen zu Kosten, Vollstreckbarkeit, Streitwert und Rechtsmittelbelehrung passen zum Tenor.
7. Rechtsprechungsanker: BVerfG, 19.05.1992 - 1 BvR 986/91 für das Verbot der Überraschungsentscheidung; BVerfG, 03.05.2021 - 2 BvR 1176/20 für Gehör, Kenntnisnahme und Erwägung.

## Format und Stil

- Echte Umlaute (ae, oe, ue, ss als ae-Umschrift nur in Slugs; im Volltext durchgehend echte ae, oe, ue, ss).
- Sachlich, knapp, in deutscher Gerichtssprache.
- Generisches Maskulinum.
- Paragrafenzeichen ausgeschrieben als „Paragraf".
- Aktenzeichen Punkt- oder Schrägstrich-Stil, niemals Komma.
- Keine Doppelsterne für Fettschrift im Fliesstext.

## Ergebnis

Ein vollständiger, versandfertiger Entscheidungstext, der von Rubrum bis Unterschrift alles enthält. Der Spruchkörper kann ihn unterschreiben — oder vor der Unterschrift redaktionell pruefen. Bei offenen Lückenpunkten bleibt der Volltext stehen, die Lücken werden in eckigen Klammern markiert und am Ende in einer Lücken-Liste zusammengefasst.

## Eigenkontrolle

Bevor der Volltext freigegeben wird, durchlaeuft der Skill eine Eigenkontrolle:

1. Stimmt der Tenor mit den Entscheidungsgründen überein?
2. Ist die Kostenentscheidung folgerichtig?
3. Ist die Rechtsmittelbelehrung vollständig und richtig?
4. Sind alle Parteibezeichnungen einheitlich?
5. Sind alle Daten, Aktenzeichen und Betraege widerspruchsfrei?
6. Sind alle Lückenpunkte explizit markiert?

Erst nach bestandener Eigenkontrolle wird der Volltext als final ausgegeben.
