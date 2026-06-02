# Akte Vertragsausfueller - BSAG Kiosk Huckelriede


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in zwei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 41 KB) | PDF | [`gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf`](gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) |

Die ZIP-URL ist stabil und zeigt immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-vertragsausfueller-bsag-kiosk-huckelriede` (Akte) | [testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.


## Sachverhalt

Die Bremer Straßenbahn AG (BSAG) vermietet ein Kioskobjekt im Haltestellenbereich Huckelriede an die Scherflein GmbH, die dort einen Imbiss-Kiosk mit Zeitungsverkauf, Heissgetraenkeausschank und Lottoannahmestelle betreiben möchte. Es liegen zwei Word-Dokumente vor: eine generische BSAG-Mietvertragsvorlage mit Platzhaltern (zum Beispiel `<<MIETER>>`, `<<KALTMIETE>>`) und ein konkretes Term Sheet mit den vereinbarten Eckdaten zum Fall.

Aufgabe des Vertragsausfuellers ist es, die Vorlage aufzunehmen, ein Feldinventar zu erzeugen, die Werte aus dem Term Sheet sauber zu mappen und einen Clean-Entwurf zu erzeugen. Wegen Abweichungen zwischen Vorlage (zweimal zwei Jahre Verlängerung, kein Konkurrenzschutz) und Term Sheet (zweimal drei Jahre Verlängerung, Konkurrenzschutz 150 m, Sortimentsbindung Imbiss/Zeitungen) sind Rückfragen an die BSAG zwingend, bevor der Vertrag final wird. Die Akte ist bewusst so geschnitten, dass der Workflow von Feldinventar über Mapping, Rückfragen, Clean-Entwurf bis hin zu Track Changes durchgespielt werden kann.

Sensible Sonderpunkte: Konkurrenzschutz, Fettabscheider, Abfallentsorgung, Rückbaupflicht, Umsatzsteueroption, Verlängerungsoptionen. Track-Changes-Fassungen werden nur auf ausdrücklichen Wunsch erzeugt.

## Eckdaten

| Position | Wert |
|---|---|
| Vermieter | Bremer Straßenbahn AG, Flughafendamm 12, 28199 Bremen |
| Mieter | Scherflein GmbH (Geschäftsführer: Karl Scherflein) |
| Mietobjekt | Kiosk Haltestelle Huckelriede, ca. 18 qm Verkaufsraum + 6 qm Lager |
| Nutzung | Imbiss-Kiosk, Zeitungsverkauf, Heissgetraenke, Lotto |
| Kaltmiete | 1.450 EUR / Monat netto |
| Nebenkosten-Pauschale | 320 EUR / Monat netto |
| Gesamtmiete | 1.770 EUR / Monat netto (zzgl. USt nach Option) |
| Kaution | 5.310 EUR (3 Bruttomonatsmieten) |
| Laufzeit | 5 Jahre fest, Verlängerungsoption 2 x 3 Jahre |
| Sonderbedingungen | Konkurrenzschutz 150 m, Sortiment, Fettabscheider, Rückbau |
| USt-Option nach § 9 UStG | Ja, beide Seiten optieren |
| Aktenzeichen Kanzlei | VAF-2026-BSAG-007 |

## Dateien

| Datei | Beschreibung |
|---|---|
| [BSAG-Mietvertrag-Vorlage.docx](BSAG-Mietvertrag-Vorlage.docx) / [.md](BSAG-Mietvertrag-Vorlage.md) | Generische Vermietungsvorlage der BSAG mit Platzhaltern für alle Mieterdaten, Preise und Sonderbedingungen |
| [BSAG-TermSheet-Kiosk-Huckelriede.docx](BSAG-TermSheet-Kiosk-Huckelriede.docx) / [.md](BSAG-TermSheet-Kiosk-Huckelriede.md) | Konkretes Term Sheet zum Mietfall Scherflein GmbH mit allen ausgehandelten Zahlen und Sonderpunkten |
| [01_feldinventar_bsag.csv](01_feldinventar_bsag.csv) | Aus der Vorlage extrahiertes Feldinventar (Platzhalter, Typ, Bemerkung) |
| [02_mapping_notiz.md](02_mapping_notiz.md) | Mapping zwischen Vorlage-Feldern und Term-Sheet-Werten inklusive Konfliktstellen |
| [03_rueckfragen_bsag.md](03_rueckfragen_bsag.md) | Offene Rückfragen an die BSAG vor Erstellung des Clean-Entwurfs |
| [04_clean_entwurf_checkliste.md](04_clean_entwurf_checkliste.md) | Prüfliste vor Versand des Clean-Entwurfs an Mieter und Vermieter |

## Testablauf

1. Starte `vaf-kommandocenter`.
2. Lasse die Vorlage strippen und ein Feldinventar erzeugen (-> `01_feldinventar_bsag.csv`).
3. Mappe das Term Sheet auf die Mietvertragsvorlage (-> `02_mapping_notiz.md`).
4. Lasse offene Rückfragen ausgeben (-> `03_rueckfragen_bsag.md`).
5. Erstelle einen Clean-Entwurf nach Prüfliste (-> `04_clean_entwurf_checkliste.md`).
6. Erst wenn ausdrücklich gewünscht: Track-Changes- oder Redline-Fassung vorbereiten.

## Prüffokuse

- Feldinventar aus DOCX-Vorlage extrahieren und systematisch ablegen
- Konfliktstellen zwischen Vorlage und Term Sheet identifizieren (Verlängerung, Konkurrenzschutz, Sortiment)
- Offene Rückfragen formulieren, bevor der Vertrag finalisiert wird
- Clean-Entwurf vor Versand systematisch prüfen
- Track-Changes-Fassung nur auf ausdrücklichen Wunsch erzeugen

## Disclaimer
