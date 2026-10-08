# Schriftsatzwerkstatt beA

Eigenständiges Cowork-Plugin für die letzte technische Strecke vor einer gerichtlichen Einreichung. Der rechtliche Inhalt ist bereits fertig und freigegeben; die Werkstatt inventarisiert den Ordner, sperrt die richtige Schriftsatzversion, ordnet Anlagen, erzeugt einzelne PDFs, prüft jede Seite, bildet kurze ASCII-Dateinamen und bereitet Signatur, Versandauftrag und Eingangsnachlauf vor.

Das Plugin bewertet weder Anspruch noch Antrag, Fristberechnung, Beweiswürdigung oder Prozessstrategie. Sobald eine inhaltliche Änderung nötig wird, stoppt es und gibt die Datei an die fachlich verantwortliche Person zurück.

## In 30 Sekunden starten

1. Lege den finalen Schriftsatz und alle Anlagen in einen gemeinsamen Projektordner. Typische Quellen sind DOC/DOCX, ODT/RTF, XLS/XLSX/ODS/CSV, EML/MSG, PDF, JPEG/PNG/TIFF/HEIC sowie zuverlässig renderbare Präsentationen.
2. Lade das Plugin und den Projektordner in Cowork.
3. Schreibe: `Mache diesen Ordner beA-fertig. Verändere den juristischen Inhalt nicht und frage nur nach Angaben, die du nicht sicher aus den Dateien entnehmen kannst.`
4. Das Plugin startet mit [`01-bea-ordner-annahme`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/01-bea-ordner-annahme/SKILL.md) und führt die übrigen Schritte selbst. Eine manuelle Skillauswahl ist nicht nötig.

Die Werkstatt zeigt zuerst eine Paketkarte mit Paket-ID, erkanntem Hauptschriftsatz, Quellenzahl, frühester Frist, Parteirolle, Anlagenstand, Ampel und genau einer nächsten Arbeitsaktion. Sicher erkennbare Angaben übernimmt sie mit Quelle. Nur offene Pflichtangaben fragt sie gebündelt nach, insbesondere Hauptdatei, Parteirolle, vorhandener Anlagenfolge, Gericht/Aktenzeichen, verantwortlicher Person und tatsächlichem Versender. Wer diese Angaben schon kennt, kann sie direkt im Startsatz ergänzen. Die Werkstatt verändert niemals die Quellen im Eingangsordner.

## Ergebnisordner

Die Werkstatt nutzt bereits erkennbare Angaben. Fehlt nur der Versender, können eindeutige Dokumente schon konvertiert werden; die Paketfreigabe bleibt offen. Fehlende Konvertierungswerkzeuge werden mit betroffenen Dateien benannt. Ein erfolgloser identischer Aufruf wird nicht endlos wiederholt. Im Chat erscheinen Paketstatus und nächste Aktion, die vollständigen Prüfprotokolle liegen intern.

```text
_bea_ausgabe/
├── arbeit/
├── cache/
├── upload/
│   ├── 01_K_Replik_Mietrueckstand.pdf
│   ├── 02_Anlage_K07_Mietkonto_2026-07-10.pdf
│   └── 03_Anlage_K08_Zustellnachweis_2026-07-11.pdf
└── intern/
    ├── versandmanifest.csv
    ├── konvertierungsprotokoll.md
    ├── pruefprotokoll.md
    └── versandauftrag.md
```

Nur die Dateien unter `upload/` sind für die beA-Nachricht vorgesehen. Interne Protokolle werden nicht automatisch mitgesendet. Originale bleiben im Eingangsordner unverändert; jede Ausgabe erhält Quelle, Seitenzahl, Größe und SHA-256-Hash im Manifest.

`arbeit/` enthält neue Renderfassungen, `cache/` nur technisch wiederverwendbare Zwischenstände. Beide Ordner bleiben intern. Eine Cache-Datei wird nur übernommen, wenn Quellhash, Konvertierungsprofil, Werkzeugversion und Ausgabehash übereinstimmen; der finale Upload durchläuft immer den vollständigen Preflight.

## Verbindlicher Werkstattstandard

Die ERVB 2025 erlaubt Dateinamen bis 90 Zeichen einschließlich Endung sowie deutsche Umlaute. Dieses Plugin verwendet absichtlich den strengeren Konzernstandard:

- höchstens 80 Zeichen einschließlich `.pdf`;
- nur ASCII-Buchstaben, Ziffern, Unterstrich und Minus;
- `ä` zu `ae`, `ö` zu `oe`, `ü` zu `ue`, `ß` zu `ss`;
- Wörter mit Unterstrich verbinden;
- genau ein Punkt vor der Endung;
- logische Reihenfolge mit `01_`, `02_`, `03_`;
- Hauptschriftsatz und jede Anlage als eigene PDF-Datei, keine Versand-ZIP.

Amtliche Obergrenze je Nachricht: höchstens 1.000 Dateien und 200 MB. Die interne Warnschwelle liegt bei 900 Dateien oder 180 MB, damit Korrekturen und Metadaten nicht erst am technischen Maximum scheitern. Einzelheiten stehen im [ERV-Versandstandard](./references/erv-versandstandard.md) und im [Dateinamen- und Manifeststandard](./references/dateinamen-und-manifest.md).

## Schnell und reproduzierbar arbeiten

- Pflichtfragen werden zu Beginn einmal gebündelt gestellt; klare Eingaben starten ohne weitere Skillauswahl.
- Quellen werden blockweise und genau einmal gehasht. Die Annahme läuft in Stapeln von höchstens 100 Dateien oder 250 MB Rohdaten; eine größere Einzeldatei erhält einen eigenen Stapel.
- Nach jedem Stapel sichert eine Fortsetzungsmarke Paket-ID, verarbeitet/offen, letzten Pfad und Hash sowie den nächsten Arbeitsblock. Eine Wiederaufnahme beginnt nicht wieder bei Datei 1.
- Bis zu vier voneinander unabhängige Konvertierungen dürfen parallel laufen; ein Stapel umfasst höchstens 20 Dateien. Ein blockiertes Format hält die übrigen Dateien nicht auf, bleibt aber als roter Einzelbefund sichtbar.
- Die Sichtprüfung rendert höchstens 30 Seiten je Stapel und höchstens zwei Aufträge parallel. Seitenbilder werden nicht als riesige Gesamtmontage im Speicher gehalten.
- Vor Freigabe wird das Paket im tatsächlich vorgesehenen beA-/eBO-/Kanzleisystem vorgeprüft. Datum, aktiver Clientstand, XJustiz-Profil und jede Dateinamens-, Anhangs-, Signatur- oder Strukturwarnung bleiben in der internen Kontrollspur; ein grüner lokaler Check überstimmt keine Clientwarnung.
- Der [Inhaltstreue- und Renderabgleich](./references/inhaltstreue-und-renderabgleich.md) bindet jede Arbeitskopie an Quellhash, Seitenvollständigkeit und Sichtprüfung. Eine technische Konvertierung darf keinen Antrag, Betrag, Namen, Termin oder juristischen Satz verändern.
- Sichtbare Tabellen haben höchstens sieben Spalten. Hashes, Werkzeugprofile und sonstige Technikdetails stehen in getrennten internen Protokollen.
- Inhaltsgleiche Dateien werden erkannt. Sie werden nicht still gelöscht, sondern zur Zuordnungsentscheidung vorgelegt.
- Nach jeder gezielten Korrektur werden nur betroffene Arbeitskopien neu erzeugt; Reihenfolge, Manifest und finaler Paketcheck werden dennoch vollständig neu gebildet.
- Der [100-Punkte-Fehlerkatalog](./references/100-punkte-fehlerkatalog.md) hält die vollständige Kontrollspur kompakt und prüfbar.

## Signatur- und Versenderentscheidung

| Schriftsatz | Tatsächlicher Versand | Ergebnis |
|---|---|---|
| qeS der verantwortlichen Person | technisch berechtigte Person | technisch möglich; Berechtigung und qeS-Prüfung dokumentieren |
| einfache Signatur mit Namenszug | dieselbe verantwortliche Person persönlich aus ihrem sicheren Postfach | freigabefähig |
| einfache Signatur mit Namenszug | andere Person löst den Versand aus | rot; qeS oder identischer verantwortlicher Versender erforderlich |
| keine einfache Signatur und keine qeS | beliebig | rot |
| Anlage zum Schriftsatz | zusammen mit formgerechtem Schriftsatz | keine eigene Signatur erforderlich |

Der persönliche Versand aus dem eigenen beA ersetzt die qeS, nicht aber die einfache Signatur am Schriftsatz. Der Name der verantwortlichen Person muss am Dokumentende lesbar wiedergegeben sein und mit der Person übereinstimmen, die den sicheren Übermittlungsweg tatsächlich nutzt.

Eine eingesetzte Unterschriftsgrafik wird nicht automatisch als einfache Signatur behandelt. Entscheidend sind eine lesbare Namenswiedergabe am Dokumentende, die eindeutige Zuordnung zur verantwortlichen Person und der passende sichere Übermittlungsweg; eine qeS ersetzt die Grafik nie. Das Plugin versendet nicht selbst, öffnet kein beA und behauptet keine erfolgreiche Einreichung. Freigabe und tatsächlicher Versand bleiben bei real benannten Personen.

Bei einer eingebetteten PAdES-Signatur bleibt der Upload eine PDF. Bei einer abgesetzten CAdES-Signatur akzeptiert die Werkstatt ausschließlich `.p7`, `.p7s`, `.p7m` oder `.pkcs7`. Dann ist [`signaturmanifest.csv`](./templates/signaturmanifest.csv) Pflicht: Signaturdatei, konkrete Ziel-PDF mit Zielhash, eigener Hash und Bytes, Format `CAdES`, Signaturniveau `qeS`, grüner Prüfstatus, Unterzeichner und internes Prüfprotokoll müssen zusammenpassen. Signaturdateien werden in die Grenzen von 1.000 Dateien und 200 MB eingerechnet; der Validator führt selbst keine kryptografische Signaturprüfung durch.

## Die neun Skills

| Nr. | Skill | Ergebnis |
|---:|---|---|
| 01 | Bei Ordner beA-fertig, Schriftsatz versandfertig oder Dateien in Gerichts-PDFs umwandeln: startet die technische Werkstatt ohne juristische Inhaltsänderung. Inventarisiert Originale, klärt fehlende Pflichtdaten und führt durch Version, Anlagen, PDF, Namen und Signatur bis zum Paket mit Freigabe- und Eingangskontrolle. | Autostart, Quelleninventar, Rückfragen und Werkstattplan |
| 02 | Bei mehreren DOCX-, ODT- oder PDF-Fassungen, Kommentaren, Änderungen, Platzhaltern oder unklarem Unterschriftsblock: bestimmt die fachlich freigegebene Schriftsatzversion vor der PDF-Konvertierung. Prüft Version und technische Vollständigkeit ohne juristische Inhaltsänderung; liefert Quellen- und Renderfassung. | gesperrte Hauptfassung ohne Kommentare oder unklare Entwurfsstände |
| 03 | Bei fertigem Schriftsatz mit gemischten Belegen: ordnet Anlagen technisch zu, führt vorhandene K- oder B-Nummern fort und bereitet die Kennzeichnung rechts oben vor. Prüft Zitate, Dubletten, Seitenfolge und fehlende Dateien. Liefert einen Anlagenplan ohne neue Bewertung des Beweiswerts oder juristischen Inhalts. | fortlaufende K-/B-Folge, Zitierabgleich und Anlagenkennzeichnung |
| 04 | Bei fertigem Schriftsatz und Anlagen aus Office, Tabellen, E-Mails, Bildern, Scans oder PDF: erzeugt separate PDF-Arbeitskopien. Behandelt Layout, Druckbereiche, Kopfzeilen, Bildausrichtung, OCR und Anhänge formatspezifisch. Erhält Originale unverändert; Keine bloße Umbenennung der Dateiendung. | separate PDF-Arbeitskopien aus Office, E-Mail, Bild und Scan |
| 05 | Nach Konvertierung oder bei vorhandenen Schriftsatz- und Anlagen-PDFs: prüft Seiten visuell und technisch vor beA. Kontrolliert Vollständigkeit, Layout, Schriften, Tabellen, Bilder, OCR, Druckbarkeit, Schutzfunktionen, aktive Inhalte und Anlagenkennzeichnung. Liefert Seitenprotokoll und konkrete Stopps. | visuelle Seitenprüfung, OCR-, Schutz- und Vollständigkeitsstatus |
| 06 | Nach PDF-Prüfung oder bei langen, kryptischen oder ungeeigneten Dateinamen: benennt Schriftsatz und Anlagen kurz und sprechend. Verwendet den internen 80-Zeichen-Standard einschließlich Endung mit ASCII und genau einem Punkt vor pdf. Liefert geordnete Dateinamen und das interne Versandmanifest. | ASCII-Zielnamen, Reihenfolge, Hash- und Versandmanifest |
| 07 | Vor beA-Versand bei einfacher Signatur, qeS, Vertretung oder Mitarbeiterzugang: prüft verantwortliche Person, tatsächlichen Versender, Berechtigung und Signaturbezug zur finalen PDF. Kontrolliert bei einfacher Signatur den persönlichen Versand durch die verantwortliche Person. Liefert Prüfmatrix und konkrete Stopps. | dokumentierte qeS-/einfache-Signatur-Entscheidung und Versenderidentität |
| 08 | Unmittelbar vor Übergabe eines konvertierten beA-Pakets an den Versender: gleicht PDFs, Anlagenfolge, Manifest, Hashes, Dateinamen, Gericht, Aktenzeichen, Frist, Signaturweg, Dateizahl und Größe ab. Liefert Freigabekarte und Versandauftrag. Versendet nicht selbst; Freigabe nur durch eine reale benannte Person. | Preflight, Upload-Ordner, Freigabekarte und Versandauftrag |
| 09 | Nach realem beA-Versand mit Nachricht, Exportprotokoll oder Eingangsbestätigung: prüft Gericht, Aktenzeichen, Zeitstempel, Dateiliste, Fehler und Hashstand. Sichert Versandfassung, erstellt Eingangsvermerk und bereitet DMS-Ablage sowie Wiedervorlage vor. Der Status gesendet allein belegt keinen Gerichtseingang. | Eingangsprüfung, Hashstand, DMS-Ablage und Wiedervorlage |

## Schnellbefehle

- `Mache den gesamten Ordner beA-fertig und ändere den Inhalt nicht.`
- `Prüfe die Replik und die Anlagen K 7 bis K 12 technisch für den beA-Versand.`
- `Wandle alle Anlagen in separate PDFs um, stemple sie rechts oben und erzeuge das Manifest.`
- `Prüfe, ob einfache Signatur und tatsächlicher beA-Versender zusammenpassen.`
- `Prüfe dieses bereits erzeugte Upload-Paket noch einmal vollständig.`
- `Dokumentiere die Eingangsbestätigung und lege den Versandstand für das DMS ab.`

## Vorlagen und Prüfhilfen

| Datei | Einsatz |
|---|---|
| [Konvertierungsprotokoll](./templates/konvertierungsprotokoll.md) | Quellenfingerprint, Delta-Entscheidung, Werkzeugstand und Ausgabehash |
| [Versandmanifest](./templates/versandmanifest.csv) | exakte Reihenfolge, Quelle, Ziel, Seiten, Bytes und SHA-256 jeder Upload-PDF |
| [Prüfprotokoll](./templates/pruefprotokoll.md) | personengebundener Preflight und reale Freigabe |
| [Versandauftrag](./templates/versandauftrag.md) | Übergabe des unveränderten Pakets an die tatsächlich versendende Person |
| [Eingangsvermerk](./templates/eingangsvermerk.md) | Soll-Ist-Abgleich der automatisierten gerichtlichen Eingangsbestätigung |
| [100-Punkte-Fehlerkatalog](./references/100-punkte-fehlerkatalog.md) | vollständige Stoppliste von Ordnerannahme bis DMS-Ablage |
| [Inhaltstreue und Renderabgleich](./references/inhaltstreue-und-renderabgleich.md) | Quellbindung, zulässige technische Änderungen, Drei-Wege-Abgleich und Stopps |

## Lokaler Paketcheck

Das mitgelieferte Prüfskript kontrolliert Upload-Ordner, PDF-Struktur, Dateinamen, Reihenfolge, Gesamtgröße und die Übereinstimmung mit Versand- und optionalem Signaturmanifest. Abgesetzte CAdES-Dateien werden nur mit eindeutigem Zielhash und belegtem grünen qeS-Prüfprotokoll freigegeben. Für die vollständige PDF-Strukturprüfung muss `pypdf` in der Python-Umgebung verfügbar sein.

```bash
uv run --with pypdf python3 schriftsatzwerkstatt-bea/scripts/validate_bea_package.py /pfad/zur/_bea_ausgabe
```

Der eingebaute Selbsttest prüft mehr als 100 gültige und gezielt fehlerhafte Varianten:

```bash
uv run --with pypdf python3 schriftsatzwerkstatt-bea/scripts/validate_bea_package.py --selftest
```

Ein grüner Skriptlauf ersetzt weder die visuelle Seitenkontrolle noch die reale Freigabe, Signaturprüfung, Empfängerkontrolle oder automatisierte Eingangsbestätigung.

## Downloads und Navigation

- [Projektübersicht: Rechtsabteilung Forderungsmanagement Immobilienunternehmen](../projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md)
- [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/rechtsabteilung-immobilien-v445.33.1/schriftsatzwerkstatt-bea.zip)
- [Fachplugin für die inhaltliche Bearbeitung](../rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md)
- [Arbeitsregeln und Abgrenzung](./AGENTS.md)
- [Root-README](../README.md)

Die neun Skills und Prüfhilfen sind vollständig übernommen. Die bereits vorhandenen Werkstätten `bea-versand` und `schriftsatz-versandwerkstatt` bleiben unverändert. Für ein Versandpaket nur einen dieser Wege wählen; doppelte Anlagenstempel oder konkurrierende Freigaben vermeiden.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`01-bea-ordner-annahme`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/01-bea-ordner-annahme/SKILL.md) | Bei Ordner beA-fertig, Schriftsatz versandfertig oder Dateien in Gerichts-PDFs umwandeln: startet die technische Werkstatt ohne juristische Inhaltsänderung. Inventarisiert Originale, klärt fehlende Pflichtdaten und führt durch Version, Anlagen, PDF, Namen und Signatur bis zum Paket mit Freigabe- und Eingangskontrolle. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/01-bea-ordner-annahme/SKILL.md) |
| [`02-schriftsatzversion-festlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/02-schriftsatzversion-festlegen/SKILL.md) | Bei mehreren DOCX-, ODT- oder PDF-Fassungen, Kommentaren, Änderungen, Platzhaltern oder unklarem Unterschriftsblock: bestimmt die fachlich freigegebene Schriftsatzversion vor der PDF-Konvertierung. Prüft Version und technische Vollständigkeit ohne juristische Inhaltsänderung; liefert Quellen- und Renderfassung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/02-schriftsatzversion-festlegen/SKILL.md) |
| [`03-anlagenfolge-kennzeichnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/03-anlagenfolge-kennzeichnen/SKILL.md) | Bei fertigem Schriftsatz mit gemischten Belegen: ordnet Anlagen technisch zu, führt vorhandene K- oder B-Nummern fort und bereitet die Kennzeichnung rechts oben vor. Prüft Zitate, Dubletten, Seitenfolge und fehlende Dateien. Liefert einen Anlagenplan ohne neue Bewertung des Beweiswerts oder juristischen Inhalts. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/03-anlagenfolge-kennzeichnen/SKILL.md) |
| [`04-dateien-in-pdf-umwandeln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/04-dateien-in-pdf-umwandeln/SKILL.md) | Bei fertigem Schriftsatz und Anlagen aus Office, Tabellen, E-Mails, Bildern, Scans oder PDF: erzeugt separate PDF-Arbeitskopien. Behandelt Layout, Druckbereiche, Kopfzeilen, Bildausrichtung, OCR und Anhänge formatspezifisch. Erhält Originale unverändert; Keine bloße Umbenennung der Dateiendung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/04-dateien-in-pdf-umwandeln/SKILL.md) |
| [`05-pdf-qualitaet-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/05-pdf-qualitaet-pruefen/SKILL.md) | Nach Konvertierung oder bei vorhandenen Schriftsatz- und Anlagen-PDFs: prüft Seiten visuell und technisch vor beA. Kontrolliert Vollständigkeit, Layout, Schriften, Tabellen, Bilder, OCR, Druckbarkeit, Schutzfunktionen, aktive Inhalte und Anlagenkennzeichnung. Liefert Seitenprotokoll und konkrete Stopps. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/05-pdf-qualitaet-pruefen/SKILL.md) |
| [`06-dateinamen-manifest-erzeugen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/06-dateinamen-manifest-erzeugen/SKILL.md) | Nach PDF-Prüfung oder bei langen, kryptischen oder ungeeigneten Dateinamen: benennt Schriftsatz und Anlagen kurz und sprechend. Verwendet den internen 80-Zeichen-Standard einschließlich Endung mit ASCII und genau einem Punkt vor pdf. Liefert geordnete Dateinamen und das interne Versandmanifest. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/06-dateinamen-manifest-erzeugen/SKILL.md) |
| [`07-signatur-versandweg-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/07-signatur-versandweg-pruefen/SKILL.md) | Vor beA-Versand bei einfacher Signatur, qeS, Vertretung oder Mitarbeiterzugang: prüft verantwortliche Person, tatsächlichen Versender, Berechtigung und Signaturbezug zur finalen PDF. Kontrolliert bei einfacher Signatur den persönlichen Versand durch die verantwortliche Person. Liefert Prüfmatrix und konkrete Stopps. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/07-signatur-versandweg-pruefen/SKILL.md) |
| [`08-bea-paket-freigeben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/08-bea-paket-freigeben/SKILL.md) | Unmittelbar vor Übergabe eines konvertierten beA-Pakets an den Versender: gleicht PDFs, Anlagenfolge, Manifest, Hashes, Dateinamen, Gericht, Aktenzeichen, Frist, Signaturweg, Dateizahl und Größe ab. Liefert Freigabekarte und Versandauftrag. Versendet nicht selbst; Freigabe nur durch eine reale benannte Person. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/08-bea-paket-freigeben/SKILL.md) |
| [`09-eingang-versandakte-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/09-eingang-versandakte-sichern/SKILL.md) | Nach realem beA-Versand mit Nachricht, Exportprotokoll oder Eingangsbestätigung: prüft Gericht, Aktenzeichen, Zeitstempel, Dateiliste, Fehler und Hashstand. Sichert Versandfassung, erstellt Eingangsvermerk und bereitet DMS-Ablage sowie Wiedervorlage vor. Der Status gesendet allein belegt keinen Gerichtseingang. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatzwerkstatt-bea/skills/09-eingang-versandakte-sichern/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->


## Verzeichnisse der Rechtssammlung

[Startseite](../README.md) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/schriftsatzwerkstatt-bea.md) · [Downloads](../ASSET_INDEX.md) · [Weitere Testakten](../testakten/README.md) · [Plugin-Dateien](.)
