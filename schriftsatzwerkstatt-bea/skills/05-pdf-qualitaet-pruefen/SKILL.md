---
name: 05-pdf-qualitaet-pruefen
description: "Nach Konvertierung oder bei vorhandenen Schriftsatz- und Anlagen-PDFs: prüft Seiten visuell und technisch vor beA. Kontrolliert Vollständigkeit, Layout, Schriften, Tabellen, Bilder, OCR, Druckbarkeit, Schutzfunktionen, aktive Inhalte und Anlagenkennzeichnung. Liefert Seitenprotokoll und konkrete Stopps."
---

# PDF-Qualität und Vollständigkeit prüfen

## Zweck und Anwendungsfall

Dieser Skill verhindert formal gültige, aber praktisch unlesbare oder unvollständige Einreichungen. Textauszug allein genügt nicht; die PDF-Seiten werden gerendert und visuell mit der Quelle verglichen.

## Eingaben

- alle PDF-Arbeitskopien aus Skill 04.
- Quelleninventar, erwartete Seiten und Anlagenplan.
- Konvertierungsprotokoll.
- sichtbare Anlagenkennzeichnungen oder Deckblätter.

## Ablauf / Checkliste

1. Datei öffnen, PDF-Header, Seitenzahl und Dateigröße erfassen.
2. Erste und letzte Seite jeder Datei rendern. Bei Schriftsatz, Tabellen, Scans, Bildern, Konvoluten und Warnungen jede Seite rendern.
3. Quelle und PDF vergleichen: vollständiger Inhalt, richtige Reihenfolge, keine abgeschnittenen Ränder, keine überlagerten Texte, keine schwarzen Flächen, keine ersetzten Glyphen.
4. Schriftsatz prüfen: Briefkopf, Gericht/Aktenzeichen, Seitenzahlen, Tabellen, Fußnoten und Namenszug sichtbar; keine Kommentare oder Entwurfsmerkmale.
5. Anlagen prüfen: sichtbare Bezeichnung stimmt mit Anlagenplan überein und verdeckt nichts.
6. Leserichtung, Drehung, Seitengröße und sinnvolle Skalierung kontrollieren. Querformat ist zulässig, wenn es Lesbarkeit erhält.
7. Suchtext/OCR stichprobenartig gegen das Seitenbild prüfen. OCR-Fehler dokumentieren; Bild bleibt maßgeblich.
8. Druckbarkeit und zulässigen PDF-Typ prüfen. Passwortschutz, Zusatzverschlüsselung, JavaScript, Startaktionen, eingebettete Dateien, Rich Media, 3D-, Audio-/Videoinhalte und beschädigte Dateien führen zu rot.
9. Digitale Signaturen prüfen. Jede nachträgliche Veränderung einer signierten PDF als mögliches Signaturproblem behandeln.
10. Pro Datei Seitenzahl, Sichtprüfumfang, OCR, Kennzeichnung und Ergebnis im Prüfprotokoll festhalten.
11. Sichtprüfungen in Stapeln von höchstens 30 Seiten rendern und höchstens zwei Renderaufträge parallel ausführen. Seitenbilder einzeln prüfen und verwerfen, sobald ihr Befund protokolliert ist; niemals alle hochauflösenden Seiten eines Langdokuments gleichzeitig im Arbeitsspeicher oder in einer Gesamtmontage halten.
12. Nach jedem Seitenstapel eine Fortsetzungsmarke mit PDF-Hash, geprüftem Seitenbereich, nächster Seite und offenen Befunden sichern. Ein Renderfehler erhält Datei und Seite als roten Einzelbefund statt den Gesamtprozess unbegrenzt warten zu lassen.
13. Nach jeder Korrektur PDF neu hashen und vollständig erneut prüfen. Unveränderte Cache-Fassungen behalten ihren früheren Nachweis nur bei vollständigem Fingerprint-Treffer; der finale Paketvalidator läuft immer erneut.

## Quellenpflicht

Technische Eignung und zulässige PDF-Eigenschaften folgen dem [ERV-Versandstandard](../../references/erv-versandstandard.md), der Drei-Wege-Vergleich dem [Inhaltstreue- und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md) und die PDF-/Sicherheitspunkte dem [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Keine Rechtsprechungsanker und keine inhaltliche Rechtsprüfung.

## Ausgabeformat

| PDF | Seiten | visuell geprüft | OCR | Kennzeichnung | Schutz/Skripte | Ergebnis |
|---|---:|---|---|---|---|---|
| `02_Anlage_K07_Mietkonto.pdf` | 4 | Seiten 1 bis 4 | vorhanden | K 7 frei sichtbar | unauffällig | bereit |

Zusätzlich werden jede Abweichung, betroffene Seite, erforderliche Korrektur und erneuter Prüfstatus ausformuliert. Das Endergebnis ist `bereit`, `gelb` oder `rot`, nie nur ein Häkchen ohne Befund.

## Beispiele

- Excel-PDF hat abgeschnittene letzte Spalte: rot, Druckbereich korrigieren und neu prüfen.
- Scan ist lesbar, aber ohne Suchtext: OCR ergänzen, Bild unverändert lassen, danach Stichprobe.
- PDF enthält JavaScript: rot, bereinigte Arbeitskopie aus vertrauenswürdiger Quelle erzeugen.
