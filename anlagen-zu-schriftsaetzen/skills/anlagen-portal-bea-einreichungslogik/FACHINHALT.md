---
name: anlagen-portal-bea-einreichungslogik
description: "Steuert den formwirksamen elektronischen Versand gerichtlicher Dokumente: bestimmt Verfahrensordnung und Portal, trennt qualifizierte Signatur vom persönlichen sicheren Übermittlungsweg, prüft Empfänger und Aktenzeichen, plant Ersatzeinreichung und kontrolliert nach Versand jede gerichtliche Eingangsbestätigung samt Anhängen und Zeitstempel."
---

# Portal, beA und Einreichungslogik

## 1. Verfahrensordnung zuerst

Bestimme Zivil-, Arbeits-, Sozial-, Verwaltungs-, Finanz- oder Strafverfahren. Verwende die jeweils einschlägige Pflichtnorm und nicht automatisch ZPO Paragraf 130d. Bei einer direkten Klage vor dem Gericht der Europäischen Union ist e-Curia statt beA zu prüfen.

## 2. Formweg

| Weg | Hauptdokument | tatsächlicher Versand |
| --- | --- | --- |
| qualifizierte elektronische Signatur | qualifiziert von der verantwortenden Person signiert | Mitarbeiter kann technisch versenden |
| sicherer Übermittlungsweg | einfach signiert, regelmäßig durch Namenswiedergabe am Ende | verantwortender Postfachinhaber versendet persönlich |

BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23, und BGH, Beschluss vom 4. September 2024, IV ZB 31/23, verlangen bei einfacher Signatur die Übereinstimmung von verantwortender Person und persönlichem Versender. BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23, bestätigt, dass Mitarbeiter-Versand keinen sicheren Übermittlungsweg herstellt.

## 3. Vor Versand

1. Empfänger aus dem Verzeichnis auswählen und Gericht mit Rubrum abgleichen.
2. Gerichtliches Aktenzeichen exakt in das Empfängerfeld übernehmen; bei Neueingang entsprechend kennzeichnen.
3. Hauptdokument, Anlagenzahl, Dateinamen und Hashmanifest abgleichen.
4. Signaturweg dokumentieren.
5. Bei Eilsache Betreff nach gerichtlichem Hinweis konkret kennzeichnen.
6. Ausreichende Zeitreserve für Übertragung, Eingangsprüfung und erneuten Versand lassen.

## 4. Nach Versand

Nach ZPO Paragraf 130a Absatz 5 liegt Eingang mit Speicherung auf der für das Gericht bestimmten Einrichtung vor. KG, Beschluss vom 22. August 2023, 27 U 40/23, ordnet die spätere interne Aktenzuweisung der Gerichtssphäre zu.

Kontrolliere trotzdem unverzüglich oder innerhalb der noch sicheren Organisationsreserve:

1. positiven Eingangsstatus,
2. richtiges Gericht und gerichtliches Aktenzeichen,
3. Hauptdokument und vollständige Anhangsliste,
4. Eingangszeitpunkt,
5. Prüfvermerk zum sicheren Übermittlungsweg oder zur Signatur.

BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22, und BGH, Beschluss vom 24. April 2025, III ZB 12/24, bilden den Kern der Ausgangskontrolle.

## 5. Störung

ZPO Paragraf 130a Absatz 6 ist keine Ersatzeinreichungsnorm. Für vorübergehende technische Unmöglichkeit gilt ZPO Paragraf 130d Sätze 2 bis 4. Nutze dann `bea-wiedereinsetzung-ersatzeinreichung-2026` aus dem Prozessrechtsplugin und liefere eine geschlossene, belegte Minutenchronologie.

## 6. Output

Liefere Versanddatenblatt, Signaturentscheidung, Vorversandcheck, Ersatzeinreichungsreserve und Eingangskontrollvermerk. Nutze `bea-versandmappe-endfertigung` als abschließenden Gesamtworkflow.
