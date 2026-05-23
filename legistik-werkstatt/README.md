# Legistik-Werkstatt

Vollstaendige Werkstatt fuer Legistinnen und Legisten in Bundes- und Landesministerien sowie kommunalen Rechtsaemtern. Vom politischen Auftrag ueber Normhierarchie Kompetenzpruefung Normenkartierung Terminologie zu Referentenentwurf Kabinettsmappe Formulierungshilfe Rechtsverordnung und Satzung. Mit Querschnittspruefungen Verfassungsrecht Europarecht Folgenabschaetzung Goldplating Bestimmtheit Zirkelschluss. Erzeugt am Ende ein DOCX und PDF im offiziellen Layout nach Handbuch der Rechtsfoermlichkeit - entweder ministerieller Referentenentwurf-Stil (Arial 11pt) oder BT-Drucksachen-Stil (Times New Roman 11pt, Sperrsatz, Drucksachennummer in der Kopfzeile).

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Legistik-Werkstatt (`legistik-werkstatt`, dieses Plugin) | [legistik-werkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Testakte

- **Legistik Pflichtpostfach** (Vom Koalitionsvertrag zum Referentenentwurf, Stammgesetz mit Begruendung und Folgenabschaetzung): [testakten/legistik-pflichtpostfach/](../testakten/legistik-pflichtpostfach/) -> [testakte-legistik-pflichtpostfach.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip)

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP“ verwenden.

## Was kann das Plugin?

Das Plugin deckt **alle Normebenen** ab:

- Bundesgesetz (Stammgesetz, Mantelgesetz, Aenderungsgesetz)
- Landesgesetz
- Rechtsverordnung des Bundes und der Laender (Art. 80 GG, Landesverfassungen)
- Satzungen von Kommunen, Kammern und Hochschulen (Art. 28 Abs. 2 GG, Selbstverwaltung)
- Sekundaerrechtsdurchfuehrung und Notifizierung

Das Plugin pruet **immer**:

- Verfassungsrecht (GG, Landesverfassungen, BVerfG-Rechtsprechung)
- Europarecht (Primaerrecht, Sekundaerrecht, Notifizierung 2015/1535)
- Folgen (Erfuellungsaufwand, Buerokratiekosten, Nachhaltigkeit, KMU-Test)
- Goldplating und Wesentlichkeit
- Bestimmtheit, Terminologie und Zirkelschluss

Am Ende erzeugt es ein **lieferfertiges DOCX und PDF** im offiziellen Layout:

- **Referentenentwurf** (Arial 11pt, Bearbeitungsstand-Kopf, A-F-Vorblatt)
- **BT-Drucksache** (Times New Roman 11pt, Drucksachennummer + Wahlperiode in der Kopfzeile, Sperrsatz fuer Hauptueberschriften, Anschreiben des Bundeskanzlers)
- **Formulierungshilfe** (kurz, fuer die Fraktionen)
- **Synopse** (dreispaltig)
- **Lesefassung** (konsolidiert nach Inkrafttreten)
- **Kabinettsmappe** (Deckblatt + Anlagenverzeichnis)

## Skill-Tabelle

| Phase | Skill | Zweck |
| --- | --- | --- |
| Auftrag | `legistik-auftragsaufnahme` | Politische Vorgabe in Regelungsauftrag uebersetzen |
| Normhierarchie | `normhierarchie-routing` | Gesetz vs Verordnung vs Satzung; Bund vs Land |
| Kompetenz | `gesetzgebungskompetenz-pruefen` | Art. 70 bis 74 GG, Erforderlichkeit |
| Kompetenz | `verordnungsermaechtigung-art80` | Inhalt Zweck Ausmass nach Art. 80 GG |
| Kompetenz | `satzungskompetenz-pruefen` | Art. 28 Abs. 2 GG, Kammern, Hochschulen |
| Mapping | `normenkartierung` | Verweisnetz und Aenderungsstellen |
| Sprache | `terminologie-konsistenz` | Begriffsbrueche aufspueren |
| Sprache | `zirkelschluss-pruefen` | Verweisgraf zykelfrei |
| Entwurf | `referentenentwurf-bauen` | Vollformat des Entwurfs |
| Entwurf | `formulierungshilfe-bauen` | Kurzfassung fuer die Mitte des Hauses |
| Entwurf | `gesetzesentwurf-kabinett` | Kabinettsmappe |
| Entwurf | `begruendung-allgemein-und-besonders` | Teil A I-VII und Teil B |
| Entwurf | `synopse-erstellen` | Dreispaltige Synopse |
| Entwurf | `lesefassung-konsolidiert` | Konsolidierte Fassung nach Inkrafttreten |
| Entwurf | `xml-paralleldarstellung` | LegalDocML.de und eNorm |
| Pruefung | `europarechtskonformitaet` | Primaerrecht Sekundaerrecht Notifizierung |
| Pruefung | `goldplating-vermeiden` | Ueberschiessende Umsetzung von Unionsrecht |
| Pruefung | `verfassungsmaessigkeit-quercheck` | Grundrechte Verhaeltnismaessigkeit Bestimmtheit |
| Folgen | `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand quantifizieren |
| Folgen | `folgenabschaetzung-nachhaltigkeit` | SDGs Klima Generationengerechtigkeit |
| Inkrafttreten | `inkrafttreten-uebergangsrecht` | Zeitpunkt Uebergang Verkuendung |
| Beteiligung | `verbaendeanhoerung-ressortabstimmung` | Anhoerung und Abstimmung |
| Beteiligung | `normenkontrollrat-kmu-check` | NKR-Stellungnahme einholen |
| Lieferung | `dokumente-rendern-docx-pdf` | DOCX und PDF im offiziellen Layout |
| Schulung | `schulung-legistik` | Trainerleitfaden fuer Schulungen |

Insgesamt **25 Skills**.

## Beispielprojekt - Pflichtpostfachgesetz

Das Repository enthaelt eine vollstaendige Schulungsakte unter `testakten/legistik-pflichtpostfach/`. Sie simuliert den Weg von der politischen Vorgabe (Koalitionsvertrag) zum lieferfertigen Referentenentwurf eines neuen Stammgesetzes ueber das elektronische Pflichtpostfach fuer HReg-Gesellschaften und sehr grosse Online-Plattformen.

So erzeugen Sie die fertigen Dokumente:

```bash
cd claude-fuer-deutsches-recht
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output

python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format bt-drucksache \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```

Voraussetzung: `pip install python-docx pyyaml`. Fuer die PDF-Konvertierung zusaetzlich LibreOffice (`soffice`).

## Disclaimer

Dieses Plugin ist ein Werkzeug zur Beschleunigung legistischer Arbeit. Es ersetzt nicht die juristische Pruefung durch verantwortliche Fachreferentinnen und Fachreferenten und nicht die Pruefung durch die Ressortleitung und das Bundesministerium der Justiz im Rahmen der Rechtsfoermlichkeitspruefung.
