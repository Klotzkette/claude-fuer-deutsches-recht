---
name: bag-leitentscheidungen-notenstufen
description: "Übersetzt belegte Leistungstatsachen in eine konsistente Zeugnisnote und prüft Zufriedenheitsformel, Einzelmerkmale und Gesamtnote an der Rechtsprechung."
---

# BAG-Leitentscheidungen zu Notenstufen

## Ziel

Die relevanten BAG-Entscheidungen zur Notenstufenmatrix kennen und beim Generieren korrekt anwenden.

## Kernentscheidungen

### BAG, Urteil v. 14.10.2003 – 9 AZR 12/03
„Zur vollen Zufriedenheit" entspricht einer durchschnittlichen Leistung (Note 3). Wer eine bessere als die durchschnittliche Beurteilung verlangt, trägt die Darlegungs- und Beweislast. Für eine unterdurchschnittliche Beurteilung trägt der Arbeitgeber die Darlegungs- und Beweislast.

**Konsequenz für den Generator:** Note 3 ist der Ausgangspunkt. Noten besser als 3 können frei vergeben werden — bei einer Klage muss der Arbeitnehmer aber nachweisen, dass er die bessere Note verdient. Noten schlechter als 3 erfordern dokumentierte Belege des Arbeitgebers.

### BAG, Urteil v. 18.11.2014 – 9 AZR 584/13
„Befriedigend" ist die mittlere Note der Zufriedenheitsskala. Der Arbeitnehmer trägt die Darlegungs- und Beweislast für eine bessere Note — auch dann, wenn in der Branche überwiegend gute oder sehr gute Noten vergeben werden. **Branchenüblichkeit verschiebt die Beweislast nicht.**

**Konsequenz für den Generator:** Der Generator soll bei Note 3 nicht davon abraten, nur weil die Branche üblicherweise Note 2 vergibt. Das ist zulässig, aber die Beweislast-Realität bleibt beim Arbeitnehmer, der Note 2 einklagen möchte.

### BAG, Urteil v. 15.11.2011 – 9 AZR 386/10
Der Arbeitgeber hat bei Werturteilen einen Formulierungsspielraum. Grenzen sind Zeugniswahrheit und Zeugnisklarheit. „Kennen gelernt" allein ist kein unzulässiger Geheimcode.

**Konsequenz für den Generator:** Innerhalb einer Notenstufe darf der Arbeitgeber zwischen mehreren korrekten Formulierungen wählen. Beispiel: Für Note 2 gibt es Variante A und Variante B — beides ist zulässig.

## Notenstufen-Matrix nach BAG-Rechtsprechung

| Note | Bezeichnung | Hauptformel | Beweislast |
|---|---|---|---|
| 1 | sehr gut | stets zur vollsten Zufriedenheit | kein Streit; Arbeitgeber hat Spielraum |
| 2 | gut | stets zur vollen Zufriedenheit | kein Streit; Arbeitgeber hat Spielraum |
| 3 | befriedigend (Ausgangspunkt) | zur vollen Zufriedenheit | Arbeitnehmer trägt Beweislast für bessere Note |
| 4 | ausreichend | zur Zufriedenheit | Arbeitgeber trägt Beweislast |
| 5 | mangelhaft | im Großen und Ganzen zur Zufriedenheit | Arbeitgeber trägt Beweislast, erhöht |

## Praktische Konsequenzen

- Wenn ein Arbeitnehmer Note 2 statt Note 3 möchte: Er muss Vorzeugnis, Boni, Zielvereinbarungen oder andere Belege liefern.
- Wenn ein Arbeitgeber Note 4 ausgibt: Er muss dokumentieren (Abmahnungen, Leistungsbeurteilungen, Beschwerden).
- Branchenüblichkeit ist kein Argument vor Gericht.

## Verifikationspflicht

Alle Angaben sind als Arbeitsgrundlage eingebettet. Vor Verwendung in einem Schriftsatz sind die Entscheidungen erneut über die Entscheidungsdatenbank des BAG, dejure.org oder das Rechtsprechungsportal des Bundes auf Fortgeltung zu prüfen.

## Stolpersteine

- Note 3 als „schlechtes" Zeugnis kommunizieren — es ist der gesetzliche Ausgangspunkt.
- Beweislast umkehren: bei Note 4 trägt der Arbeitgeber die Last, nicht der Arbeitnehmer.
- Branchenüblichkeit als Argument für Note 2 einsetzen — das ändert nichts an der Beweislastsituation.

## Anti-Muster

- Dem Arbeitnehmer sagen, er habe „automatisch" Anspruch auf Note 2, weil in seiner Branche Note 2 Standard ist.
- Note 3 mit Note 4 verwechseln — die Formulierungen unterscheiden sich klar.
- BAG-Entscheidungen ohne Verifikation in Schriftsätzen zitieren.

## v392 Notenanker für die Ausgabe

Bei jedem Zeugnis wird die Hauptformel mit den Einzelfeldern abgeglichen. Sehr gut verlangt durchgängige Beständigkeit, besondere Qualität und klaren Erfolg. Gut verlangt verlässlich überdurchschnittliche Leistung. Befriedigend ist nicht als Abwertung zu behandeln, sondern als mittlere Ausgangsstufe. Die Schlussformel darf die Hauptnote nicht unterlaufen: Eine sehr gute Leistungsformel mit kaltem Abschluss wird als Drift markiert; ein sehr warmer Abschluss bei schwacher Leistung wird als Wahrheitsrisiko markiert.
