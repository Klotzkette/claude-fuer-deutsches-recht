# Akte: Familie Tannenberg - vier Sozialrechtsverfahren parallel


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 384 KB) | PDF | [`gesamt-pdf/sozialrecht-rollstuhl-tannenberg_gesamt.pdf`](gesamt-pdf/sozialrecht-rollstuhl-tannenberg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-sozialrecht-rollstuhl-tannenberg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-sozialrecht-rollstuhl-tannenberg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-sozialrecht-rollstuhl-tannenberg` (Akte) | [testakte-sozialrecht-rollstuhl-tannenberg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sozialrecht-rollstuhl-tannenberg.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.


## Idee der Akte

Die Familie Tannenberg in Kiel wickelt zur gleichen Zeit **vier sozialrechtliche Verfahren** über dieselbe Kanzlei (RA Holm) ab. Jeder Fall ist eigenständig, hat einen eigenen Bescheid, eine eigene Frist und ein eigenes Sachgebiet. Zusammen decken sie die wichtigsten Felder ab, die in einer typischen Sozialrechts-Kanzlei täglich vorkommen.

| Mandant | Verfahren | Sozialgesetzbuch | Sachgebiet |
|---|---|---|---|
| Olaf Tannenberg (62) | Aktivrollator | SGB V | Hilfsmittel, Krankenkasse, Eilrechtsschutz |
| Lena Tannenberg (16) | Schulbegleitung | SGB VIII iVm IX | Eingliederungshilfe, Jugendamt |
| Margarete Tannenberg (84) | Pflegegrad 3 auf 4 | SGB XI | Pflegekasse, MD-Gutachten |
| Bodo Petersen (62) | Volle EM-Rente | SGB VI | DRV, sozialmedizinisches Gutachten |

## Struktur der Akte

```
testakten/sozialrecht-rollstuhl-tannenberg/
  README.md                           <- dies hier
  Fallkonferenz_Tannenberg_Workflow.md         <- Fallkonferenz und Prüfmatrix
  Familien-Stammbaum.md               <- wer ist mit wem verwandt
  Fristen_Familie_Tannenberg.xlsx     <- alle Fristen auf einen Blick
  Fristen_Familie_Tannenberg.md       <- Markdown-Vorschau dafuer

  01-olaf-rollstuhl/                  <- bisheriger Hauptfall MS / Rollator
    Aerztliches_Attest_Wallenstein_05-05-2026.pdf
    Bescheid_Nordsee-BKK_18-04-2026.pdf
    Eilantrag_SG_Kiel_25-08-2026.md
    Bildbeschreibung_Rollator_kaputt.md
    Korrespondenz_mit_Nordsee-BKK.pdf
    Kostenvoranschlag_Sanitaetshaus_Reha-Aktiv-Nord.pdf
    MDK-Gutachten_03-04-2026.pdf
    Notiz_Kanzlei_Erstgespraech.txt
    Pflegegrad_2_Bescheid_04-05-2023.pdf
    Reha-Bericht_2024_Damp.pdf
    Verordnung_Muster16_09-02-2026.pdf
    Wegeaufstellung_Mandant.docx (+ .md-Vorschau)
    Widerspruchsschreiben_RA_Holm_20-05-2026.md
    Wohnungsskizze_Mandant_Beschreibung.md

  02-lena-schulbegleitung/            <- neuer Fall Schulbegleitung
    Bescheid_Jugendamt_Kiel_12-03-2026.pdf
    KJP-Stellungnahme_Dr_Maibaum_22-02-2026.pdf
    Schulgutachten_Gelehrtenschule_Kiel_08-02-2026.pdf
    Mandantenbrief_Eltern_Tannenberg_Lena.md
    Widerspruchsentwurf_Lena_Schulbegleitung.md
    Vollmacht_Eltern_Tannenberg.docx (+ .md-Vorschau)

  03-margarete-pflegegrad/            <- neuer Fall Pflegegrad-Hoeherstufung
    Bescheid_Pflegekasse_AOK_NW_05-04-2026.pdf
    MD-Pflegegutachten_18-03-2026.pdf
    Pflegetagebuch_Margarete_Februar_2026.xlsx (+ .md-Vorschau)
    Hausarzt_Stellungnahme_Dr_Petersen_25-03-2026.pdf
    Widerspruchsentwurf_Pflegegrad.md

  04-bodo-em-rente/                   <- neuer Fall volle EM-Rente abgelehnt
    DRV-Bescheid_Bodo_Petersen_15-04-2026.pdf
    Sozialmed_Gutachten_DRV_Brunsbuettel_27-02-2026.pdf
    Reha-Entlassungsbericht_Bad_Bramstedt_24-04-2024.pdf
    Psychiatrisches_Attest_Dr_Lornsen-Joost_06-04-2026.pdf
    Widerspruchsentwurf_Bodo_EM-Rente.md
    Notiz_Kanzlei_Erstgespraech_Bodo.txt
```

## Bearbeitungsworkflow (Kurz)

1. **Triage** - vier Bescheide auf den Tisch, SGB-Buch zuordnen
2. **Frist-Quick-Check** - 60 Sekunden pro Bescheid, Ampel rot/gelb/grün
3. **Bescheidanalyse** - Begründungsmängel finden
4. **Widerspruch** - Bausteine zusammensetzen
5. **Mandantenbrief** - in einfacher Sprache
6. **Strategie** - PKH, Eilrechtsschutz, Untätigkeitsklage

Details: `Fallkonferenz_Tannenberg_Workflow.md`.

## Stand der Verfahren (Datum 22.05.2026)

- **Olaf:** Widerspruch eingelegt am 20.05.2026, Eilantrag für Sitzung 25.08.2026 vorbereitet
- **Lena:** Widerspruch eingelegt am 06.04.2026, Antwort Jugendamt steht aus
- **Margarete:** Widerspruchsentwurf vom 28.04.2026 eingereicht, Antwort AOK steht aus
- **Bodo:** Widerspruchsentwurf vom 02.05.2026 eingereicht, PKH für mgl. Klage vorbereitet

## Empfohlener Einstieg

1. `Fallkonferenz_Tannenberg_Workflow.md` lesen, um den Aufbau zu verstehen
2. Im Plugin `fachanwalt-sozialrecht` mit Skill `sozialrecht-fallaufnahme-routing` starten
3. Bei jedem Fall den Bescheid lesen, dann das Gutachten, dann den Widerspruchsentwurf
4. Fristen-XLSX dazulegen, um die Termin-Logik zu verstehen
5. Den Mandantenbrief von Lena lesen und überlegen, wie er für Bodo aussehen würde

## Disclaimer
