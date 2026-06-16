---
name: anlagen-bauen
description: "Baut aus den Belegen eines Fahrgastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Widerspruch Schlichtungsantrag Klage) die Belege Buchungsbestaetigung E-Ticket Verspaetungsbestaetigung Foto Anzeigetafel App-Screenshots Belege zu Ausla..."
---

# Fahrgastrechte — Anlagen bauen

## Eingaben

```yaml
schriftsatz: <pfad zum Schriftsatz, z.B. widerspruch-2026-05-15.md>
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # erzeugt zusätzlich Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold        # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

## Workflow

### 1. Schriftsatz parsen

Liest den Schriftsatz und identifiziert alle erwähnten Anlagen anhand der Bezeichnung `Anlage K 1`, `Anlage K 2`, ... oder `Anlage K1`, `Anlage K2`. Erstellt geordnete Liste in Reihenfolge der Erwähnung im Text.

### 2. Rohbelege zuordnen

Verzeichnis `belege/` durchsuchen und jedem Anlage-K-Eintrag eine Datei zuordnen. Typische Belege im Fahrgastrechte-Kontext:

| Anlage typisch | Datei-Pattern | Beschreibung |
|---|---|---|
| K1 | `buchung-*.pdf` | Buchungsbestätigung der DB / des EVU |
| K2 | `e-ticket-*.pdf` oder `fahrkarten-*.pdf` | E-Tickets / Fahrkarten aller Reisenden |
| K3 | `verspaetung-*.png` oder `db-navigator-*.png` | DB-Verspätungsmitteilung (App / SMS / E-Mail) |
| K4 | `anzeigetafel-*.jpg` | Foto Anzeigetafel Zielbahnhof mit Uhrzeit |
| K5 | `belege-auslagen/*.pdf` | Belege zu Ersatzbeförderung / Verpflegung / Hotel |
| K6 | `erstantrag-*.pdf` | Eigener Erstantrag an DB Servicecenter |
| K7 | `ablehnung-*.pdf` | Ablehnungsschreiben der DB |
| K8 | `widerspruch-*.pdf` | Eigener Widerspruch (in Klage relevant) |
| K9 | `schlichtungsspruch-*.pdf` | Schlichtungsspruch der Schlichtungsstelle Reise & Verkehr |
| K10 ff. | `vollmacht-*.pdf` | Vollmachten der Mitreisenden |

Wenn eine erwähnte Anlage nicht zugeordnet werden kann: **Prüfer-Flag** mit Liste der unzugeordneten Bezugnamen.

### 3. Belege konvertieren und stempeln

Jeden Rohbeleg in PDF konvertieren (HEIC / JPG / PNG / DOCX / XLSX → PDF). Auf jedem Anlagen-PDF oben rechts in **Arial 12 FETT** (Helvetica-Bold 12pt) den Bezeichner stempeln:

```
                                                                    Anlage K 1
[Inhalt]
```

Dateibenennung: ohne Umlaute und Leerzeichen — `Anlage_K_1.pdf`, `Anlage_K_2.pdf`, … gemäß beA-Konvention.

### 4. Sammel-PDF optional

Wenn `bundle: true`: Sammel-PDF `Schriftsatz_mit_Anlagen.pdf` erzeugen — Schriftsatz vorne, Anlagen in nummerierter Reihenfolge mit Lesezeichen je Anlage. Nützlich für Akteneintrag und Sicht-Backup.

### 5. Ausgabe

Im `ausgabeverzeichnis/`:

- `Anlage_K_1.pdf`, `Anlage_K_2.pdf`, … (separate Anlagen-PDFs für beA-Upload)
- `Schriftsatz_mit_Anlagen.pdf` (Sammel-PDF, wenn bundle: true)
- `anlagen-uebersicht.md` (Tabelle Anlage K → Datei → Beschreibung; Fehlen-Hinweise)

## beA-Konvention

- Anlagen werden im beA als **separate PDFs** eingereicht.
- Jeweils mit Stempel oben rechts in **Arial 12 FETT**.
- **Dateiname** ohne Umlaute, ohne Leerzeichen: `Anlage_K_1.pdf`.
- **Reihenfolge** muss der Erwähnung im Schriftsatz entsprechen.
- Sammel-PDF zusätzlich für eigenes Aktenexemplar (nicht für beA-Upload).

## Foto-Belege bei DB-Verspätung — besondere Hinweise

- **Foto Anzeigetafel:** Uhrzeit muss erkennbar sein. Bei mehreren Anzeigetafeln nur die maßgebliche (Zielbahnhof). Datum eines Tages-Vergleichs ggf. durch EXIF-Daten ergänzen.
- **DB-Navigator-Screenshot:** möglichst mit Verbindungsdetails-Seite, die geplante und tatsächliche Ankunftszeit zeigt.
- **Ablehnungsschreiben:** alle Seiten in einer PDF (auch Rückseiten / Anlagen des Schreibens).
- **Vollmachten:** Originale-Scans hoher Qualität. Beidseitige Unterschriften bei sorgeberechtigten Eltern eines Minderjährigen.

## Fehlerquellen

- Schriftsatz erwähnt `Anlage K5`, im Belege-Verzeichnis fehlt die zugehörige Datei → Skript bricht ab; Prüfer-Flag.
- Doppelte Anlage K-Nummerierung im Schriftsatz → Fehlermeldung; manueller Eingriff.
- HEIC-Dateien iOS → automatische Konvertierung; bei OCR-Bedarf Hinweis.
- Mehrseitige Anlage in mehreren Dateien (z.B. Ablehnungsschreiben S. 1 separat) → Pre-Merge in eine Datei vor Stempelung.

## Ausgabe-Beispiel

```
anlagen-uebersicht.md
============================
Fall: FGR-2026-0042
Schriftsatz: widerspruch-2026-05-15.md
Erzeugte Anlagen:

| Anlage   | Datei                       | Beschreibung                          | Status |
|----------|-----------------------------|----------------------------------------|--------|
| Anlage K 1 | Anlage_K_1.pdf             | Buchungsbestätigung PNR ABC123          | ok      |
| Anlage K 2 | Anlage_K_2.pdf             | E-Tickets Mueller (3 Personen)          | ok      |
| Anlage K 3 | Anlage_K_3.pdf             | DB-Navigator Verspätungsmitteilung       | ok      |
| Anlage K 4 | Anlage_K_4.pdf             | Foto Anzeigetafel Muenchen Hbf 15:05   | ok      |
| Anlage K 5 | Anlage_K_5.pdf             | Kassenbon Bahnhofs-Imbiss 12,50 EUR    | ok      |
| Anlage K 6 | Anlage_K_6.pdf             | Erstantrag an DB Servicecenter           | ok      |
| Anlage K 7 | Anlage_K_7.pdf             | Ablehnungsschreiben DB vom 12.05.2026    | ok      |

Sammel-PDF: Schriftsatz_mit_Anlagen.pdf erzeugt (28 Seiten, 4.2 MB).
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 13 DSGVO
- § 71 GVG
- § 32 VSBG
- § 23 VSBG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
