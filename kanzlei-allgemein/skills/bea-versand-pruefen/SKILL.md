---
name: bea-versand-pruefen
description: "Prüft einen konkreten elektronischen Gerichtsversand vor und nach dem Absenden: bestimmt Verfahrensordnung, Empfänger und Frist, trennt qualifizierte Signatur vom persönlichen sicheren Übermittlungsweg, kontrolliert Hauptdokument und Anhänge, sichert Prüfvermerk und gerichtliche Eingangsbestätigung und routet technische Störungen in eine belegte."
---

# beA-Versand prüfen

## 1. Direktstart

Lies zuerst Schriftsatz, Versandmappe, Fristnotiz und vorhandene beA-Protokolle. Wenn der Versand noch bevorsteht, liefere eine Stop-Liste. Wenn er bereits erfolgt ist, beginne mit der gerichtlichen Eingangsbestätigung und gleiche Empfänger, Aktenzeichen und Anhänge ab.

## 2. Verfahrensordnung

Bestimme die einschlägige Norm:

- Zivilverfahren: ZPO Paragraf 130a und Paragraf 130d.
- Arbeitsgericht: ArbGG Paragraf 46c und Paragraf 46g.
- Sozialgericht: SGG Paragraf 65a und Paragraf 65d.
- Verwaltungsgericht: VwGO Paragraf 55a und Paragraf 55d.
- Finanzgericht: FGO Paragraf 52a und Paragraf 52d.
- Strafverfahren: StPO Paragraf 32a und Paragraf 32d.

Direkte Klagen beim Gericht der Europäischen Union werden über e-Curia und nicht über beA eingereicht.

## 3. Signaturentscheidung

| Variante | Erfordernis |
| --- | --- |
| qualifizierte elektronische Signatur | verantwortende Person signiert qualifiziert; technischer Versand kann durch Mitarbeiter erfolgen |
| einfacher Namenszug und sicherer Übermittlungsweg | verantwortender Postfachinhaber versendet selbst über sein Postfach |

BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23, BGH, Beschluss vom 4. September 2024, IV ZB 31/23, und BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23, tragen diese Trennung. Anlagen benötigen nach ZPO Paragraf 130a Absatz 3 keine eigene Signatur.

## 4. Vorversandkontrolle

1. Gericht und Empfängeradresse stimmen mit Rubrum und Rechtsmittelzuständigkeit überein.
2. Gerichtliches Aktenzeichen ist exakt oder der Vorgang ist als Neueingang gekennzeichnet.
3. Hauptdokument ist final und einfach oder qualifiziert signiert.
4. Anlagenzitate, Dateinamen, sichtbare Stempel und Anlagenverzeichnis stimmen überein.
5. Dateien sind lesbar, nicht verschlüsselt und nach ERVV sowie aktueller ERVB geeignet.
6. Anzahl und Gesamtgröße sind aus den finalen Dateien berechnet.
7. Ausreichende Reaktionsreserve vor Fristablauf bleibt.

## 5. Nachversandkontrolle

Die Frist wird erst erledigt, wenn die automatisierte gerichtliche Eingangsbestätigung kontrolliert ist. Prüfe:

1. positives Übermittlungsergebnis,
2. richtiges Gericht und richtiges Aktenzeichen,
3. richtige Hauptdatei,
4. vollständige Anhangsliste,
5. Zeitstempel vor Fristablauf,
6. Prüfvermerk zum sicheren Übermittlungsweg oder zur Signatur.

BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22, verlangt eine organisierte Ausgangskontrolle. BGH, Beschluss vom 24. April 2025, III ZB 12/24, lässt den organisatorischen Zeitpunkt offen, verlangt aber Abruf und Kontrolle innerhalb einer noch ausreichenden Reaktionsreserve.

## 6. Störung und ungeeignetes Dokument

ZPO Paragraf 130a Absatz 6 betrifft die geeignete Nachreichung nach Hinweis auf ein bereits eingegangenes, technisch ungeeignetes Dokument. Eine vorübergehende technische Unmöglichkeit und Ersatzeinreichung richtet sich nach ZPO Paragraf 130d Sätze 2 bis 4 beziehungsweise der Parallelvorschrift.

Bei Störung direkt in `bea-wiedereinsetzung-ersatzeinreichung-2026` wechseln. Die Angabe `beA ging nicht` reicht nicht.

## 7. Output

Liefere Vorversand- oder Nachversandprotokoll, Stop-Liste, Signaturentscheidung, Eingangskontrolle und Archivierungsliste. Für die vollständige Dateiproduktion nutze `bea-versandmappe-endfertigung` im Plugin Anlagen zu Schriftsätzen.
