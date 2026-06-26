---
name: 99-finale-entscheidung-volltext
description: Erzeugt die finale entscheidung als volltext (beschluss familiengericht) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung.
---

# Finale Entscheidung als Volltext (Beschluss Familiengericht)

## Zweck

Dieser Skill erzeugt die finale Entscheidung des Spruchkörpers nicht als bloßen Vorschlag oder Votum, sondern als versandfertigen Volltext im richtigen Layout — so, wie er das Gericht verlassen würde. Die Entscheidung wird zur Unterschrift fertig gebaut: mit Rubrum, vollständigem Tenor, Tatbestand oder Sachverhalt, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung.

Gegenstand: Beschluss in einer Familiensache nach FamFG.

## Rechtlicher Rahmen

Paragrafen 38, 39 FamFG für Beschlussform und Rechtsmittelbelehrung; Paragrafen 1565 ff. BGB bei Ehesache; Paragraf 1684 BGB bei Umgang; Paragraf 1626 BGB bei elterlicher Sorge.

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

1. Die am [Datum] vor dem Standesbeamten in [Ort] geschlossene Ehe der Beteiligten wird geschieden.
2. Die elterliche Sorge für das gemeinsame Kind [Name, Geburtsdatum] wird der Antragstellerin allein übertragen.
3. Die Kosten des Verfahrens werden gegeneinander aufgehoben.

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

1. Kindeswohl, Elternrechte, Beteiligtenrechte und Verfahrensziel sind getrennt gewichtet.
2. Anhörungen, Verfahrensbeistand, Jugendamt und Sachverständige sind in der Begründung richtig verortet.
3. Eilentscheidungen benennen Regelungsbedürfnis, Verhältnismäßigkeit, Dauer und mildere Mittel.
4. Umgangs-, Sorge- und Schutzanordnungen sind konkret genug für Befolgung und Vollstreckung.
5. Artikel 103 Absatz 1 GG ist gewahrt; bei kindbezogenen Entscheidungen wird das rechtliche Gehör nicht durch bloße Beschleunigung ersetzt.

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
