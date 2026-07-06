# Akte: Familie Tannenberg - vier Sozialrechtsverfahren parallel


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 379 KB) | PDF | [`gesamt-pdf/sozialrecht-rollstuhl-tannenberg_gesamt.pdf`](gesamt-pdf/sozialrecht-rollstuhl-tannenberg_gesamt.pdf) |
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
├── Fristen_Familie_Tannenberg.docx                      <- Markdown-Vorschau der Fristen-XLSX
├── 01-olaf-rollstuhl/                                 <- Hilfsmittelstreit Aktivrollstuhl (SGB V)
│   ├── Notiz_Kanzlei_Erstgespraech.txt                <- Erstgespräch und Auftragsklärung
│   ├── Verordnung_Muster16_09-02-2026.pdf             <- Ärztliche Verordnung des Aktivrollstuhls
│   ├── Aerztliches_Attest_Wallenstein_05-05-2026.pdf  <- Neurologisches Attest zur MS und Sturzgefahr
│   ├── MDK-Gutachten_03-04-2026.pdf                   <- MD-Stellungnahme nach Aktenlage
│   ├── Bescheid_Nordsee-BKK_18-04-2026.pdf            <- Ablehnungsbescheid der Krankenkasse
│   ├── Korrespondenz_mit_Nordsee-BKK.pdf              <- Schriftwechsel mit der Kasse
│   ├── Kostenvoranschlag_Sanitaetshaus_Reha-Aktiv-Nord.pdf <- Kostenvoranschlag Aktivrollstuhl
│   ├── Pflegegrad_2_Bescheid_04-05-2023.pdf           <- Pflegegrad-Vorgeschichte
│   ├── Reha-Bericht_2024_Damp.pdf                     <- Reha-Entlassungsbericht
│   ├── Wegeaufstellung_Mandant.docx (+ .md)           <- Alltagswege und Distanzen des Mandanten
│   ├── Wohnungsskizze_Mandant_Beschreibung.md         <- Wohnung, Zuschnitt, Engstellen
│   ├── Bildbeschreibung_Rollator_kaputt.md            <- Zustand des vorhandenen Rollators
│   ├── Widerspruchsschreiben_RA_Holm_20-05-2026.md    <- Anwaltlicher Widerspruch
│   └── Eilantrag_SG_Kiel_25-08-2026.md                <- Eilantrag nach § 86b SGG
├── 02-lena-schulbegleitung/                           <- Eingliederungshilfe Schulbegleitung (SGB VIII)
│   ├── Bescheid_Jugendamt_Kiel_12-03-2026.pdf         <- Ablehnung der Schulbegleitung
│   ├── KJP-Stellungnahme_Dr_Maibaum_22-02-2026.pdf    <- Kinder- und jugendpsychiatrische Stellungnahme
│   ├── Schulgutachten_Gelehrtenschule_Kiel_08-02-2026.pdf <- Schulische Dokumentation der Krisen
│   ├── Vollmacht_Eltern_Tannenberg.docx (+ .md)       <- Vollmacht der Eltern
│   ├── Mandantenbrief_Eltern_Tannenberg_Lena.md       <- Mandantenbrief in einfacher Sprache
│   └── Widerspruchsentwurf_Lena_Schulbegleitung.md    <- Anwaltlicher Widerspruchsentwurf
├── 03-margarete-pflegegrad/                           <- Höherstufung Pflegegrad 3 auf 4 (SGB XI)
│   ├── Bescheid_Pflegekasse_AOK_NW_05-04-2026.pdf     <- Ablehnung der Höherstufung
│   ├── MD-Pflegegutachten_18-03-2026.pdf              <- Pflegegutachten nach Hausbesuch
│   ├── Pflegetagebuch_Margarete_Februar_2026.xlsx (+ .md) <- Pflegetagebuch der Schwiegertochter
│   ├── Hausarzt_Stellungnahme_Dr_Petersen_25-03-2026.pdf <- Hausärztliche Stellungnahme
│   └── Widerspruchsentwurf_Pflegegrad.md              <- Anwaltlicher Widerspruchsentwurf
├── 04-bodo-em-rente/                                  <- Volle Erwerbsminderungsrente (SGB VI)
│   ├── Notiz_Kanzlei_Erstgespraech_Bodo.txt           <- Erstgespräch und Einkommenslage
│   ├── DRV-Bescheid_Bodo_Petersen_15-04-2026.pdf      <- Ablehnung der vollen EM-Rente
│   ├── Sozialmed_Gutachten_DRV_Brunsbuettel_27-02-2026.pdf <- Sozialmedizinisches Gutachten der DRV
│   ├── Reha-Entlassungsbericht_Bad_Bramstedt_24-04-2024.pdf <- Reha-Bericht als Gegenbeweis
│   ├── Psychiatrisches_Attest_Dr_Lornsen-Joost_06-04-2026.pdf <- Attest zu Depression und Schmerz
│   └── Widerspruchsentwurf_Bodo_EM-Rente.md           <- Widerspruchsentwurf mit PKH-Hinweis
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
