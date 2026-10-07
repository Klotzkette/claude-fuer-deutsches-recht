# Dateinamen- und Manifeststandard

## Ausgabeordner

```text
_bea_ausgabe/
├── arbeit/   neue Render-, OCR- und Kennzeichnungsfassungen
├── cache/    nur nach Hash geprüfte wiederverwendbare Arbeitskopien
├── upload/   Versand-PDFs und gegebenenfalls zugeordnete CAdES-Dateien
└── intern/   Manifest, Protokolle, Prüfstatus und Versandauftrag
```

Der Eingangsordner bleibt unverändert. Jede Konvertierung, Drehung, OCR-Schicht oder Anlagenkennzeichnung entsteht ausschließlich als neue Arbeitskopie.

`arbeit/`, `cache/` und `intern/` werden niemals mitgesendet. Der Cache ist keine Freigabe: Er darf nur verwendet werden, wenn Quellhash, Konvertierungsprofil, Werkzeugversion und Ausgabehash unverändert sind. Der finale Upload wird unabhängig davon vollständig geprüft.

## Dateinamen

Interner Standard: maximal 80 Zeichen einschließlich `.pdf`; zulässig sind nur `A-Z`, `a-z`, `0-9`, Unterstrich und Minus. Ein Punkt ist ausschließlich vor `pdf` zulässig.

Für eine real vom Signatur-/Versandsystem erzeugte abgesetzte CAdES-Datei gelten höchstens 90 Zeichen und die Endungen `.p7`, `.p7s`, `.p7m` oder `.pkcs7`. Konkatenierte Endungen wie `Schriftsatz.pdf.p7s` sind zulässig. Die Werkstatt benennt das Artefakt nicht um; ASCII, Eindeutigkeit und Zuordnung werden dennoch geprüft.

Ersetzungen:

| Original | Ziel |
|---|---|
| `ä`, `Ä` | `ae`, `Ae` |
| `ö`, `Ö` | `oe`, `Oe` |
| `ü`, `Ü` | `ue`, `Ue` |
| `ß` | `ss` |
| Leerzeichen | `_` |
| `/`, `\\`, `:`, `;`, Komma und Klammern | `_` oder Weglassen |
| mehrere Unterstriche | ein Unterstrich |

Schema:

- Hauptschriftsatz: `01_[K|B]_[Dokumenttyp]_[Kurzgegenstand].pdf`
- Anlage: `[Reihenfolge]_Anlage_[K|B][Nummer]_[Kurzinhalt]_[Datum].pdf`
- Beispiel: `01_K_Replik_Mietrueckstand.pdf`
- Beispiel: `02_Anlage_K07_Mietkonto_2026-07-10.pdf`

Die Breite des Nummernpräfixes richtet sich nach der Dateizahl: bis 99 Dateien zweistellig, ab 100 dreistellig und bei 1.000 Dateien vierstellig. Alle Dateien desselben Pakets verwenden dieselbe Breite. Zielnamen müssen auch ohne Beachtung der Groß-/Kleinschreibung eindeutig sein.

`K 7` ist die sichtbare Anlagenbezeichnung; `K07` ist die kompakte Dateinamensform. Bereits verwendete K-/B-Nummern bleiben gesperrt. Bei weiteren Schriftsätzen wird die höchste vorhandene Nummer fortgesetzt.

## Sichtbare Anlagenkennzeichnung

1. Erste Seite rechts oben mit `Anlage K 7` oder `Anlage B 4` kennzeichnen.
2. Originalinhalt, Briefkopf, Datum, Seitenzahl, Barcode und vorhandene Signatur nicht überdecken.
3. Ist kein freier Bereich vorhanden, bei einer unsignierten Arbeitskopie einen weißen Rand ergänzen oder ein Anlagen-Deckblatt voranstellen.
4. Bei bereits elektronisch signierten PDFs weder Stempel, Rand noch Deckblatt anfügen. Das signierte Original bewahren und den Kennzeichnungsweg vor jeder Änderung mit der verantwortlichen Person festlegen.
5. Konvolute erhalten ein Inhaltsblatt und eine eindeutige Seitenfolge. Unterschiedliche Dokumente werden nicht nur zur Bequemlichkeit zusammengeführt.

## Versandmanifest

Pflichtspalten in exakt dieser Reihenfolge:

| Feld | Inhalt |
|---|---|
| Reihenfolge | `01`, `02`, `03` |
| Rolle | Hauptschriftsatz oder Anlage |
| Anlage | leer, `K 7` oder `B 4` |
| Quelldatei | relativer unveränderter Quellpfad |
| Zieldatei | exakter Name im Upload-Ordner |
| Seiten | geprüfte Seitenzahl |
| Bytes | exakte Dateigröße |
| SHA256 | Hash der finalen Versanddatei |
| OCR | `vorhanden` oder `nicht nötig`; `fehlgeschlagen` sperrt die Freigabe |
| Kennzeichnung | `geprüft`, `Deckblatt`, `signiertes Original` oder beim Hauptschriftsatz `nicht anwendbar` |
| Datenschutz | `geprüft`; jeder andere Status sperrt die Freigabe |
| Status | nur `bereit` darf in ein freigegebenes Upload-Paket gelangen |

Das Manifest ist intern. Es enthält genau eine Zeile je Upload-PDF, Datei 01 ist genau ein Hauptschriftsatz, alle Folgezeilen sind Anlagen. `Quelldatei` ist ein relativer Pfad ohne `..`, Laufwerksbuchstaben oder Rückwärtsschrägstrich. Beginnt ein echter Quellname mit `=`, `+`, `-` oder `@`, wird der relative Pfad als `./[Quellname]` notiert, damit Tabellenprogramme ihn nicht als Formel ausführen. Jede Änderung an einer PDF erzeugt einen neuen Hash und hebt den bisherigen Prüfstatus auf.

Der lokale Validator akzeptiert das Manifest nur in UTF-8 mit exakt dem vorgegebenen Kopf und höchstens 2.000.000 Bytes. Das ist keine ERV-Außengrenze, sondern ein interner Schutz gegen beschädigte oder unkontrolliert aufgeblähte CSV-Dateien; für höchstens 1.000 Versanddateien bleibt reichlich Protokollreserve.

## Signaturmanifest bei abgesetztem CAdES

Ohne separate Signaturdatei darf kein `signaturmanifest.csv` vorliegen. Liegt mindestens eine CAdES-Datei im Upload, ist das Manifest Pflicht und enthält exakt diese Spalten:

| Feld | Inhalt |
|---|---|
| Signaturdatei | exakter Name des CAdES-Artefakts im Upload |
| Zieldokument | exakt eine vorhandene finale PDF |
| Zieldokument_SHA256 | Hash der unveränderten Ziel-PDF |
| Bytes | exakte Größe der Signaturdatei |
| SHA256 | Hash der Signaturdatei |
| Format | `CAdES` |
| Signaturniveau | `qeS` |
| Prüfstatus | `grün`, `gruen` oder `erfolgreich` |
| Unterzeichner | reale Person laut Signaturprüfung |
| Prüfprotokoll | Dateiname des nicht leeren Prüfprotokolls im internen Ordner |

Das Manifest beweist die qeS nicht selbst. Es bindet den grünen Befund des realen Signaturprüfsystems an genau die geprüfte PDF-Fassung. Mehrere Signaturen derselben PDF erhalten getrennte Zeilen; dieselbe Signaturdatei darf nicht mehreren Dokumenten zugeordnet werden. Jede Änderung an der Ziel-PDF hebt Signatur- und Paketfreigabe auf.

## Schneller Delta-Lauf

1. Einmal je Quelle `Quellhash`, Format, Größe und relativen Pfad blockweise erfassen; keine große Quelle vollständig in den Arbeitsspeicher laden.
2. Konvertierungsprofil festhalten: Werkzeug und Version, Exportparameter, OCR-Sprache, Kennzeichnungsweg und Ziel-PDF-Typ.
3. Eine vorhandene Arbeitskopie nur wiederverwenden, wenn Quellhash, Profil, Werkzeugversion und gespeicherter Ausgabehash exakt passen und der frühere Sichtstatus grün war.
4. Geänderte, neue, fehlende oder nicht verifizierbare Quellen einzeln neu bearbeiten. Inhaltsgleiche Quellen dürfen dieselbe technische Konvertierung nutzen, bleiben aber getrennt im Anlagenplan dokumentiert.
5. Unabhängige Konvertierungen dürfen mit höchstens vier Arbeitsaufträgen parallel laufen. Reihenfolge und Zielnamen werden erst danach aus dem gesperrten Anlagenplan gebildet.
6. Vor Freigabe immer alle finalen Upload-PDFs, CAdES-Artefakte sowie Versand- und Signaturmanifest erneut prüfen; ein Cachetreffer ersetzt keinen Preflight.

Bei großen Beständen endet ein Annahmestapel nach höchstens 100 Dateien oder 250 MB Rohdaten, ein Konvertierungsstapel nach höchstens 20 Dateien und ein Sichtprüfstapel nach höchstens 30 PDF-Seiten. Die Fortsetzungsmarke hält Paket-ID, verarbeitete und offene Einheiten, letzten Pfad beziehungsweise PDF-Hash, Seitenstand, Einzelbefunde und nächsten Stapel fest. Nach Unterbrechung werden unveränderte Quellen und bereits protokollierte Seiten nicht erneut ausgegeben.

## Qualitätsprotokoll

Pro PDF festhalten:

- Quelle und Konvertierungswerkzeug;
- Seitenzahl vor und nach Konvertierung;
- erste und letzte Seite visuell geprüft;
- bei Tabellen, Scans und Bildern jede Seite geprüft;
- Leserichtung, Zuschnitt, Schrift, Bilder, Tabellen und Seitenfolge;
- OCR-/Suchtextstatus;
- Passwort, Verschlüsselung, eingebettete Objekte und Skripte;
- sichtbare Anlagenkennzeichnung;
- Ergebnis und prüfende Person.

Die vollständige Kontrollspur steht im [100-Punkte-Fehlerkatalog](./100-punkte-fehlerkatalog.md). Der lokale Validator deckt die automatisierbaren Namens-, Manifest-, PDF-, Signaturzuordnungs-, Hash-, Größen- und Reihenfolgeprüfungen ab; die kryptografische qeS-Prüfung bleibt Aufgabe des realen Signatur-/Versandsystems.
