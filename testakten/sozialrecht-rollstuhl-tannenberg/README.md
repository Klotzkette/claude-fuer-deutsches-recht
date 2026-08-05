# Akte: Familie Tannenberg - vier Sozialrechtsverfahren parallel

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/sozialrecht-rollstuhl-tannenberg_gesamt.pdf`](gesamt-pdf/sozialrecht-rollstuhl-tannenberg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-sozialrecht-rollstuhl-tannenberg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-sozialrecht-rollstuhl-tannenberg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## Idee der Akte

Die Familie Tannenberg in Kiel wickelt zur gleichen Zeit **vier sozialrechtliche Verfahren** über dieselbe Kanzlei (Holm · Petersen · Sönnichsen, RA Lasse Holm) ab. Jeder Fall ist eigenständig, hat einen eigenen Bescheid, eine eigene Frist und ein eigenes Sachgebiet. Zusammen decken sie die wichtigsten Felder ab, die in einer typischen Sozialrechts-Kanzlei täglich vorkommen.

| Mandant | Verfahren | Sozialgesetzbuch | Sachgebiet |
|---|---|---|---|
| Olaf Tannenberg (62) | Aktivrollstuhl | SGB V | Hilfsmittel, Krankenkasse, Eilrechtsschutz |
| Lena Tannenberg (16) | Schulbegleitung | SGB VIII iVm IX | Eingliederungshilfe, Jugendamt |
| Margarete Tannenberg (84) | Pflegegrad 3 auf 4 | SGB XI | Pflegekasse, MD-Gutachten |
| Bodo Petersen (62) | Volle EM-Rente | SGB VI | DRV, sozialmedizinisches Gutachten |

## Aktenstruktur

```
sozialrecht-rollstuhl-tannenberg/
├── README.md                                          <- diese Übersicht
├── rubric.yaml                                        <- Prüfkriterien für die Bearbeitung
├── Fallkonferenz_Tannenberg_Workflow.docx               <- Fallkonferenz, Triage und Prüfmatrix über alle vier Verfahren
├── Familien-Stammbaum.docx                              <- Verwandtschaft, Haushalte, Versicherungen, PKH-Lage
├── Fristen_Familie_Tannenberg.xlsx                    <- Fristenübersicht als Tabelle mit Verfahrensverlauf
├── Fristen_Familie_Tannenberg.docx                      <- Lesefassung der Fristen-XLSX
├── Email_Sanitaetshaus_Olaf_Rollstuhl_12-08-2026.eml    <- Sanitätshaus zu abgelaufenem Kostenvoranschlag, Lieferzeit und untauglicher Leihversorgung
├── 01-olaf-rollstuhl/                                 <- Hilfsmittelstreit Aktivrollstuhl (SGB V)
│   ├── Notiz_Kanzlei_Erstgespraech.txt                <- Erstgespräch und Auftragsklärung
│   ├── Verordnung_Muster16_09-02-2026.docx            <- Ärztliche Verordnung des Aktivrollstuhls
│   ├── Aerztliches_Attest_Wallenstein_05-05-2026.docx <- Neurologisches Attest zur MS und Sturzgefahr
│   ├── MDK-Gutachten_03-04-2026.docx                  <- MD-Stellungnahme nach Aktenlage
│   ├── Bescheid_Nordsee-BKK_18-04-2026.docx           <- Ablehnungsbescheid der Krankenkasse
│   ├── 01_antrag_aktivrollstuhl_olaf_tannenberg_2026-02-11.pdf <- Eigenständiger Antrag des Versicherten
│   ├── 02_nordsee_bkk_nachforderung_2026-03-22.pdf     <- Gesondertes Nachforderungsschreiben der Krankenkasse
│   ├── 03_ergaenzung_olaf_tannenberg_dr_wallenstein_2026-03-30.pdf <- Gemeinsame Ergänzung mit ärztlicher Stellungnahme
│   ├── Kostenvoranschlag_Sanitaetshaus_Reha-Aktiv-Nord.docx <- Nachgerechneter Kostenvoranschlag Aktivrollstuhl
│   ├── Pflegegrad_2_Bescheid_04-05-2023.docx          <- Pflegegradbescheid mit den im Jahr 2023 geltenden Beträgen
│   ├── Reha-Bericht_2024_Damp.docx                    <- Reha-Entlassungsbericht
│   ├── Wegeaufstellung_Mandant.docx                   <- Alltagswege und Distanzen des Mandanten
│   ├── Wohnungsskizze_Mandant_Beschreibung.docx       <- Wohnung, Zuschnitt, Engstellen
│   ├── Bildbeschreibung_Rollator_kaputt.docx          <- Zustand des vorhandenen Rollators
│   ├── Widerspruchsschreiben_RA_Holm_20-05-2026.docx  <- Anwaltlicher Widerspruch
│   └── Eilantrag_SG_Kiel_25-08-2026.docx              <- Eilantrag nach Paragraf 86b SGG
├── 02-lena-schulbegleitung/                           <- Eingliederungshilfe Schulbegleitung (SGB VIII)
│   ├── Bescheid_Jugendamt_Kiel_12-03-2026.pdf         <- Ablehnung der Schulbegleitung
│   ├── KJP-Stellungnahme_Dr_Maibaum_22-02-2026.pdf    <- Kinder- und jugendpsychiatrische Stellungnahme
│   ├── Schulgutachten_Gelehrtenschule_Kiel_08-02-2026.pdf <- Schulische Dokumentation der Krisen
│   ├── Vollmacht_Eltern_Tannenberg.docx               <- Vollmacht der Eltern
│   ├── Mandantenbrief_Eltern_Tannenberg_Lena.docx     <- Mandantenbrief in einfacher Sprache
│   └── Widerspruchsentwurf_Lena_Schulbegleitung.docx  <- Anwaltlicher Widerspruchsentwurf
├── 03-margarete-pflegegrad/                           <- Höherstufung Pflegegrad 3 auf 4 (SGB XI)
│   ├── Bescheid_Pflegekasse_AOK_NW_05-04-2026.pdf     <- Ablehnung der Höherstufung
│   ├── MD-Pflegegutachten_18-03-2026.pdf              <- Pflegegutachten nach Hausbesuch
│   ├── Pflegetagebuch_Margarete_Februar_2026.xlsx     <- Pflegetagebuch der Schwiegertochter
│   ├── Hausarzt_Stellungnahme_Dr_Petersen_25-03-2026.pdf <- Hausärztliche Stellungnahme
│   └── Widerspruchsentwurf_Pflegegrad.docx            <- Anwaltlicher Widerspruchsentwurf
├── 04-bodo-em-rente/                                  <- Volle Erwerbsminderungsrente (SGB VI)
│   ├── Notiz_Kanzlei_Erstgespraech_Bodo.txt           <- Erstgespräch und Einkommenslage
│   ├── DRV-Bescheid_Bodo_Petersen_15-04-2026.pdf      <- Ablehnung der vollen EM-Rente
│   ├── Sozialmed_Gutachten_DRV_Brunsbuettel_27-02-2026.pdf <- Sozialmedizinisches Gutachten der DRV
│   ├── Reha-Entlassungsbericht_Bad_Bramstedt_24-04-2024.pdf <- Reha-Bericht als Gegenbeweis
│   ├── Psychiatrisches_Attest_Dr_Lornsen-Joost_06-04-2026.pdf <- Attest zu Depression und Schmerz
│   └── Widerspruchsentwurf_Bodo_EM-Rente.docx         <- Widerspruchsentwurf mit PKH-Hinweis
└── gesamt-pdf/                                        <- konsolidierte Lesefassung als PDF
```

## Bearbeitungsworkflow (Kurz)

1. **Triage** - vier Bescheide auf den Tisch, SGB-Buch zuordnen
2. **Frist-Quick-Check** - 60 Sekunden pro Bescheid, Ampel rot/gelb/grün
3. **Bescheidanalyse** - Begründungsmängel finden
4. **Widerspruch** - Bausteine zusammensetzen
5. **Mandantenbrief** - in einfacher Sprache
6. **Strategie** - PKH, Eilrechtsschutz, Untätigkeitsklage

Details: `Fallkonferenz_Tannenberg_Workflow.docx`.

## Stand der Verfahren (Datum 22.05.2026)

- **Olaf:** Widerspruch eingelegt am 20.05.2026, Eilantrag für Sitzung 25.08.2026 vorbereitet
- **Lena:** Widerspruch eingelegt am 06.04.2026, Antwort Jugendamt steht aus
- **Margarete:** Widerspruchsentwurf vom 28.04.2026 eingereicht, Antwort AOK steht aus
- **Bodo:** Widerspruchsentwurf vom 02.05.2026 eingereicht, PKH für mgl. Klage vorbereitet

## Empfohlener Einstieg

1. `Fallkonferenz_Tannenberg_Workflow.docx` lesen, um den Aufbau zu verstehen
2. Im Plugin `fachanwalt-sozialrecht` mit Skill `sozialrecht-fallaufnahme-routing` starten
3. Bei jedem Fall den Bescheid lesen, dann das Gutachten, dann den Widerspruchsentwurf
4. Fristen-XLSX dazulegen, um die Termin-Logik zu verstehen
5. Den Mandantenbrief von Lena lesen und überlegen, wie er für Bodo aussehen würde
