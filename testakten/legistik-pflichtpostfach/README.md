# Akte - Elektronisches Pflichtpostfach

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf`](gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-legistik-pflichtpostfach.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-legistik-pflichtpostfach-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-legistik-pflichtpostfach` (Akte) | [testakte-legistik-pflichtpostfach.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.

> Arbeitsakte für das Plugin `legistik-werkstatt`. Die Akte simuliert einen vollständigen Legistik-Durchlauf vom Koalitionsvertrag bis zur fertigen Kabinettsmappe.

## Politische Vorgabe (Auszug Koalitionsvertrag)

> "Wir wollen die Digitalisierung der Rechtskommunikation entschlossen voranbringen. Alle im Handelsregister eingetragenen Gesellschaften, ihre Zweigniederlassungen sowie sehr große Online-Plattformen und Online-Suchmaschinen im Sinne des Digital Services Act sollen verpflichtet werden, ein elektronisches Pflichtpostfach vorzuhalten. Dieses Pflichtpostfach soll für Zustellungen durch Gerichte, Behörden und in Wahrnehmung öffentlicher Aufgaben handelnde Stellen geeignet sein. Wir gewährleisten Interoperabilität mit den vorhandenen Postfächern (beA, beBPo, eBO, ELSTER-Postfach, Mein Unternehmenskonto)."

## Aufgabe an die Legistinnen und Legisten

Aus dieser politischen Vorgabe ist ein **Stammgesetz "Pflichtpostfachgesetz - PflPostG"** zu erstellen, das

- in HGB, ZPO, FamFG, VwZG, AO die nötigen Folgeänderungen anstößt,
- Bezüge zu DSA, eIDAS 2.0, GoBD herstellt und
- über das Notifizierungsverfahren 2015/1535 europarechtlich abgesichert wird.

Ein vollständiger Verfahrensdurchlauf durch die 25 Skills des Plugins `legistik-werkstatt` ist im Methodikvermerk beschrieben (`methodik_verfahrensdurchlauf.docx`).

## Akteninterne Reibungspunkte

1. **Goldplating** - die DSA-Pflicht auf 45 Mio Nutzer ist klar, aber der Entwurf zieht sie auf eine "vergleichbare Größe" herab. Skill `goldplating-vermeiden` muss greifen.
2. **Bestimmtheit** - die Formulierung "ab einer gewissen Größe" ist verfassungsrechtlich nicht haltbar. Skill `verfassungsmaessigkeit-quercheck` muss eine Untergrenze fordern.
3. **Verordnungsermächtigung** - Inhalt, Zweck und Ausmass nach Art. 80 GG müssen so bestimmt sein, dass der Bürger sie aus dem Gesetz heraus erkennt. Skill `verordnungsermaechtigung-art80` zwingt zur Nachschärfung.
4. **Notifizierung** - technische Vorschrift im Sinne der Richtlinie (EU) 2015 1535, deshalb dreimonatige Stillhaltefrist gegenüber Kommission und Mitgliedstaaten.
5. **Zuständigkeit** - HGB ist Bürgerliches Recht (Art. 74 Abs. 1 Nr. 1 GG), Verfahrensrecht ZPO und FamFG (Art. 74 Abs. 1 Nr. 1 GG), Zuständigkeit für die VLOP-Pflicht aber komplett DSA-getrieben (DSA-DG als Stammgesetz, Bundeszuständigkeit).
6. **Zirkelschluss** - die Definition "Pflichtpostfach im Sinne des § 1 PflPostG" wird in HGB § 33a verwendet, der wieder auf das PflPostG zurückverweist - in Ordnung, aber das XML muss das sauber abbilden.

## Ordnerstruktur

```
testakten/legistik-pflichtpostfach/
  README.md                # diese Datei
  methodik_verfahrensdurchlauf.docx       # Methodikvermerk und Verfahrensdurchlauf
  eingang/
    auftragsblatt.md       # Auftrag des federführenden Ressorts
    metadaten.yaml         # Titel, Kurztitel, Federfuehrung, Bearbeitungsstand
    vorblatt.md            # A bis F nach HdR
    gesetzestext.md        # Artikelgesetz mit PflPostG + Folgeaenderungen
    begruendung-a.md       # Allgemeiner Teil I-VII
    begruendung-b.md       # Besonderer Teil
    synopse.csv            # Spaltensynopse alt/neu/begruendung
  referenzen/
    hgb-auszug-33a.md      # Bestandsnormen, die geaendert werden
    zpo-130d-ff.md
    famfg-14.md
    dsa-art-33.md          # DSA Art. 33 - VLOP-Kriterien
    eidas-2-bezug.md
  anlagen/
    nkr-stellungnahme.md
    notifizierung-2015-1535.md
    stellungnahme-verbaendeanhoerung-berw.md   # Verbandsstellungnahme BERW: Erfuellungsaufwand, Uebergangsfrist, Zustellfiktion
  ressortabstimmung_mitzeichnung_bmf.eml       # BMF-Mitzeichnung mit Massgaben zur AO-Folgeaenderung und zum Zollaufwand
  output/                  # leer am Anfang, wird vom render.py gefuellt
```

## So läuft die Bearbeitung

1. Auftrag aus `eingang/auftragsblatt.docx` lesen
2. Skill `legistik-auftragsaufnahme` durchlaufen
3. Skill `normhierarchie-routing` -> Ergebnis: Bundesstammgesetz
4. Skills `gesetzgebungskompetenz-pruefen`, `verfassungsmaessigkeit-quercheck`, `europarechtskonformitaet`
5. Skill `normenkartierung` -> Karte mit HGB, ZPO, FamFG, DSA, eIDAS, VwZG
6. Skill `terminologie-konsistenz` -> ein einheitlicher Begriff für "Pflichtpostfach"
7. Skill `referentenentwurf-bauen` -> baut das Markdown-Gerüst
8. Skill `begruendung-allgemein-und-besonders`
9. Skill `synopse-erstellen` -> CSV
10. Skill `xml-paralleldarstellung` -> LegalDocML.de
11. Skill `folgenabschaetzung-erfuellungsaufwand` und `folgenabschaetzung-nachhaltigkeit`
12. Skill `verbaendeanhoerung-ressortabstimmung`
13. Skill `normenkontrollrat-kmu-check`
14. Skill `inkrafttreten-uebergangsrecht`
15. Skill `gesetzesentwurf-kabinett` -> Kabinettsmappe
16. **Skill `dokumente-rendern-docx-pdf`** -> erstellt am Ende eine echte DOCX-Datei im offiziellen HdR-Layout

## Beispielaufruf des Render-Skripts

```bash
cd claude-fuer-deutsches-recht
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```

Ausgabe: `Referentenentwurf-PflPostG.docx` im offiziellen Arial-11pt-Layout mit Bearbeitungsstand-Kopf, A-F-Vorblatt, Artikelgesetz und Begründung in Teil A und B.

Für das BT-Drucksachen-Layout (Times New Roman, Drucksachennummer im Kopf, Anschreiben des Bundeskanzlers):

```bash
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format bt-drucksache \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```
