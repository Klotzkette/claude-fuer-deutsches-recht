# Akte - Elektronisches Pflichtpostfach


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in zwei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 335 KB) | PDF | [`gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf`](gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-legistik-pflichtpostfach.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |

Die ZIP-URL ist stabil und zeigt immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

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

- in HGB, ZPO, FamFG, VwZG, AO die nötigen Folgeänderungen anstoesst,
- Bezüge zu DSA, eIDAS 2.0, GoBD herstellt und
- über das Notifizierungsverfahren 2015/1535 europarechtlich abgesichert wird.

Ein vollständiger Verfahrensdurchlauf durch die 25 Skills des Plugins `legistik-werkstatt` ist im Methodikvermerk beschrieben (`methodik_verfahrensdurchlauf.md`).

## Akteninterne Reibungspunkte

1. **Goldplating** - die DSA-Pflicht auf 45 Mio Nutzer ist klar, aber der Entwurf zieht sie auf eine "vergleichbare Größe" herab. Skill `goldplating-vermeiden` muss greifen.
2. **Bestimmtheit** - die Formulierung "ab einer gewissen Größe" ist verfassungsrechtlich nicht haltbar. Skill `verfassungsmaessigkeit-quercheck` muss eine Untergrenze fordern.
3. **Verordnungsermächtigung** - Inhalt, Zweck und Ausmass nach Art. 80 GG müssen so bestimmt sein, dass der Bürger sie aus dem Gesetz heraus erkennt. Skill `verordnungsermaechtigung-art80` zwingt zur Nachschaerfung.
4. **Notifizierung** - technische Vorschrift im Sinne der Richtlinie (EU) 2015 1535, deshalb dreimonatige Stillhaltefrist gegenüber Kommission und Mitgliedstaaten.
5. **Zuständigkeit** - HGB ist Bürgerliches Recht (Art. 74 Abs. 1 Nr. 1 GG), Verfahrensrecht ZPO und FamFG (Art. 74 Abs. 1 Nr. 1 GG), Zuständigkeit für die VLOP-Pflicht aber komplett DSA-getrieben (DSA-DG als Stammgesetz, Bundeszuständigkeit).
6. **Zirkelschluss** - die Definition "Pflichtpostfach im Sinne des § 1 PflPostG" wird in HGB § 33a verwendet, der wieder auf das PflPostG zurückverweist - in Ordnung, aber das XML muss das sauber abbilden.

## Ordnerstruktur

```
testakten/legistik-pflichtpostfach/
  README.md                # diese Datei
  methodik_verfahrensdurchlauf.md       # Methodikvermerk und Verfahrensdurchlauf
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
  output/                  # leer am Anfang, wird vom render.py gefuellt
```

## So läuft die Bearbeitung

1. Auftrag aus `eingang/auftragsblatt.md` lesen
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
