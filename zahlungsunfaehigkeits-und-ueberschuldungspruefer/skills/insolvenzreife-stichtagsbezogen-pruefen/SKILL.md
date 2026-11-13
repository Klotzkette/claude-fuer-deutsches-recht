---
name: insolvenzreife-stichtagsbezogen-pruefen
description: "Ermittelt aus Bankauszügen, Buchhaltung und Verträgen den nachweisbaren Eintritt von Zahlungsunfähigkeit und insolvenzrechtlicher Überschuldung. Liefert zwei getrennte Stichtagsbefunde und eine Belegmatrix für die Anfechtung."
---

# 1. Zahlungsunfähigkeit und Überschuldung zeitlich bestimmen

## 1.1. Zweck und Anwendungsfall

Bearbeite den konkreten Rechtsträger und Zeitraum. Beginne mit einem knappen Doppelbefund, sobald Quellen dafür vorliegen. Gib für jeden Insolvenzgrund den letzten belegbar unauffälligen Punkt, den frühesten tragfähigen positiven Befund und den verbleibenden Eintrittskorridor an. Bei einem dokumentierten Auslöser kann ein konkretes Eintrittsdatum tragfähig sein.

## 1.2. Eingaben

Lies zuerst die Übersicht der Akte, Konten und OPOS, Jahres- und Zwischenabschlüsse, Finanzpläne, Bewertungsbelege, Finanzierungsschreiben, Anträge und Eröffnungsbeschluss. Ermittle die interessierenden Zahlungen und Stichtage aus dem Auftrag. Frage nur nach Nachweisen, deren Fehlen einen wesentlichen Rechenschritt oder das Ergebnis hindert.

## 1.3. Ablauf

1. Stelle die Behauptungen in Anträgen und Schreiben mit Datum, Betrag und Anknüpfungstatsachen voran. Ein Eröffnungsbeschluss dokumentiert den Verfahrensstand. Ein behauptetes früheres Eintrittsdatum erfordert eine eigene Prüfung.
2. Stimme mit [Konto und Buchungen](../konto-buchungen-abgleichen/SKILL.md) die Quellensätze ab. [Verbindlichkeiten](../verbindlichkeiten-und-faelligkeit-pruefen/SKILL.md) und [verfügbare Mittel](../liquide-mittel-und-zufluesse-pruefen/SKILL.md) je Stichtag einzeln einordnen. Rechne den [Dreiwochenstatus](../dreiwochenstatus-nachrechnen/SKILL.md) und würdige [Zahlungseinstellung](../zahlungseinstellung-wuerdigen/SKILL.md) als eigenständigen Nachweisweg.
3. Rekonstruiere die [Fortbestehensprognose](../fortbestehensprognose-rekonstruieren/SKILL.md) und den [Überschuldungsstatus](../ueberschuldungsstatus-bewerten/SKILL.md). Prüfe [Nachrang und Patronat](../rangruecktritt-und-patronat-pruefen/SKILL.md) in allen drei Rechnungen mit dem jeweiligen Wirksamkeitsdatum.
4. [Grenze beide Eintrittszeitpunkte ein](../eintrittszeitpunkte-eingrenzen/SKILL.md). Ordne bei Anfechtungsvorbereitung [die konkreten Rechtshandlungen](../anfechtungsstichtage-aufbereiten/SKILL.md) zu. Führe auch einen möglichen Wegfall und späteren Neueintritt getrennt.
5. Bei verfügbaren Werkzeugen kann der lokale Rechner die normalisierten Posten reproduzierbar summieren. Nutze das [Eingabeformat](../../app/FORMAT.md) und `node app/cli.mjs Eingabe.json` aus dem Pluginordner. Vergleiche das Ergebnis mit Einzelbelegen und dokumentiere rechtliche Ansatzentscheidungen im Vermerk. In ChatGPT ohne Laufzeit liefere dieselbe Rechnung als Tabelle mit offenen Ansätzen.

## 1.4. Quellenpflicht

Prüfe insbesondere § 17 und § 19 InsO, BGH II ZR 88/16 Rn. 50–62, II ZR 112/21 Rn. 12–17 und II ZR 84/20 Rn. 68–85. Beachte den aktuellen Gesetzeswortlaut und die jeweilige Aussagegrenze. Die [amtliche Quellenübersicht](../../references/insolvenzreife-quellen.md) führt zu Normen und Volltexten. Zitiere nur fallbezogen geprüfte Fundstellen und nenne Belegdatei und Stelle für jede entscheidende Tatsache.

## 1.5. Ausgabeformat

Liefere je Insolvenzgrund Datum oder Korridor, Methode, Summen, Belege und den stärksten Gegenbefund. Ein Entscheidungssatz kann lauten, dass der Eintritt vor einem Stichtag offen und an einem späteren Stichtag belegt ist. Füge die Belegmatrix und bei Bedarf eine konkrete Nachforderungsliste bei. Liefere den Vermerk in vollständigen Sätzen und mit dezimaler Gliederung. Für formatierten Export verwende soweit technisch möglich Times New Roman, 11 pt.

## 1.6. Beispiel

Eine hohe stille Reserve deckt Verbindlichkeiten im Status zum ersten Stichtag. Die Bank entzieht erst später ihre Linie. Rekonstruiere den Fortbestand der Reserve und die Verfügbarkeit der Linie jeweils auf der richtigen Zeitachse. Die Ergebnisse können auf unterschiedliche Tage fallen.
