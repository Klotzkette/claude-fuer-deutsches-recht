---
name: 01-bea-ordner-annahme
description: "Bei Ordner beA-fertig, Schriftsatz versandfertig oder Dateien in Gerichts-PDFs umwandeln: startet die technische Werkstatt ohne juristische Inhaltsänderung. Inventarisiert Originale, klärt fehlende Pflichtdaten und führt durch Version, Anlagen, PDF, Namen und Signatur bis zum Paket mit Freigabe- und Eingangskontrolle."
---

# beA-Ordner annehmen und Werkstatt starten

## Zweck und Anwendungsfall

Dieser Skill ist der einzige notwendige Einstieg. Der kürzeste vollständige Auftrag lautet: `Mache diesen Ordner beA-fertig. Verändere den juristischen Inhalt nicht und frage nur nach Angaben, die du nicht sicher aus den Dateien entnehmen kannst.` Auch Aufträge wie `Schriftsatz mit Anlagen versandfertig machen` oder `alles in gerichtstaugliche PDFs umwandeln` aktivieren ihn. Er übernimmt den Projektordner, ohne Quellen zu verändern, und steuert automatisch die Skills 02 bis 09.

Eine manuelle Auswahl weiterer Skills ist nicht nötig. Der Einstieg bleibt aktiv, bis das Paket entweder mit einem konkreten Stoppbefund zurückgegeben oder an die nächste Werkstattstufe übergeben ist.

Der juristische Inhalt gilt als abgeschlossen. Erkennt der Skill eine nötige Änderung an Antrag, Vortrag, Frist, Beweiswürdigung oder Rechtsausführung, stoppt er die technische Werkstatt und gibt die konkrete Datei an die fachlich verantwortliche Person zurück.

## Eingaben

- Projektordner mit Schriftsatz und allen Anlagen.
- Hauptschriftsatz, soweit bereits bekannt.
- Kläger-/Beklagtenrolle oder andere Anlagenlogik.
- höchste bereits verwendete K-/B-Nummer oder `keine`.
- Gericht, Aktenzeichen oder `Neueingang`, Frist und Dokumenttyp.
- verantwortliche Person, tatsächlicher Versender und vorgesehener Signaturweg.
- vorgesehenes beA-/eBO-/Kanzleisystem; aktiver Clientstand und XJustiz-Profil, soweit im System sichtbar.

## Ablauf / Checkliste

1. Eingangsordner nur lesen. Keine Quelle umbenennen, verschieben, überschreiben oder konvertieren.
2. Frühere `_bea_ausgabe`-Ordner, temporäre Office-Dateien und Systemdateien aus dem Quellenlauf ausschließen, aber als Ausschluss protokollieren. Symlinks nicht verfolgen.
3. Für jede echte Quelle relativen Pfad, Typ, Größe, Änderungsdatum und SHA-256-Hash genau einmal erfassen. Große Dateien blockweise lesen und niemals vollständig in den Arbeitsspeicher laden.
4. Große Ordner in Annahmestapeln von höchstens 100 Dateien oder 250 MB Rohdaten inventarisieren; eine einzelne größere Datei bildet einen eigenen Stapel. Bereits ausgeschlossene Ordner oder Cache-Dateien nicht erneut durchlaufen.
5. Nach jedem Annahmestapel eine Fortsetzungsmarke sichern: Paket-ID, verarbeitet/offen, letzter relativer Pfad, letzter Quellhash, kumulierte Bytes, rote Einzelbefunde und nächster Stapel. Nach Unterbrechung nur bei identischem Pfad-, Größen-, Zeit- und Hashstand fortsetzen.
6. Möglichen Hauptschriftsatz, Anlagen, E-Mail-Anhänge, Archiv-Inhalte, Dubletten, temporäre Dateien und offensichtlich alte Versionen gruppieren.
7. Gefährliche oder unklare Eingänge rot markieren: Passwortschutz, Makro, ausführbare Datei, defekte Datei, leere Datei oder unbekanntes Format. Ein Einzelfehler stoppt nur die betroffene Quelle, nicht das Inventar der übrigen Dateien.
8. Vorhandenes Konvertierungsprotokoll abgleichen und Delta-Status bilden: `unverändert`, `geändert`, `neu`, `fehlt`, `unklar`. Nur ein Treffer aus Quellhash, Konvertierungsprofil, Werkzeugversion, Ausgabehash und früherem grünen Sichtstatus ist wiederverwendbar.
9. Fehlen Pflichtangaben, einmal gebündelt fragen:
   - Welche Datei ist die inhaltlich freigegebene Hauptfassung?
   - Welche Parteirolle und welche höchste bereits verwendete K-/B-Nummer gelten?
   - Gericht, Aktenzeichen/Neueingang, Frist und Dokumenttyp?
   - Wer verantwortet den Schriftsatz, wer löst den Versand tatsächlich aus und ist qeS vorgesehen?
   - Über welches konkrete beA-/eBO-/Kanzleisystem wird versendet, und welcher Client-/XJustiz-Stand ist dort tatsächlich aktiv?
10. Ausgabeordner `_bea_ausgabe/arbeit`, `_bea_ausgabe/cache`, `_bea_ausgabe/upload` und `_bea_ausgabe/intern` planen. Noch keine Datei als freigegeben kennzeichnen.
11. Automatisch mit Skill `02-schriftsatzversion-festlegen` fortfahren und danach die Skills 03 bis 08 in Reihenfolge ausführen. Skill 09 folgt nach dem realen Versand.

## Schnell zum nutzbaren Paket

Frage nur die noch offenen Angaben aus Schritt 9 ab. Ein klar erkennbares Gericht, Aktenzeichen oder bereits dokumentierter Anlagenstand wird zur Kontrolle angezeigt und nicht noch einmal abgefragt. Fehlt die Versenderangabe, dürfen bereits eindeutig zugeordnete Arbeitskopien konvertiert und geprüft werden; die Freigabe des Upload-Pakets bleibt offen. Bei konkurrierenden Hauptfassungen werden keine Inhaltsänderungen geraten.

Vor umfangreicher Konvertierung eine repräsentative Datei pro Eingangsformat prüfen. Ist kein passendes Werkzeug verfügbar, benenne Format, betroffene Dateien und den benötigten Export konkret. Einen identischen fehlgeschlagenen Aufruf nicht endlos wiederholen; Ursache beheben oder die Datei als offen führen. Intakte übrige Quellen weiterbearbeiten.

Im Chat genügen Hauptfassung, Anlagenzahl, Paketstatus, fehlende Angaben und nächste Aktion. Vollständiges Inventar und Prüfprotokoll liegen unter `intern`; ausschließlich tatsächlich erzeugte Dateien verlinken. Für eine neue Anlage nur deren Konvertierung und die abhängigen Nummern/Querverweise aktualisieren. Vor Paketfreigabe bleibt der vollständige Endcheck erforderlich.

## Quellenpflicht

Für diese Annahme gelten der [ERV-Versandstandard](../../references/erv-versandstandard.md), der [Dateinamen- und Manifeststandard](../../references/dateinamen-und-manifest.md), der [Inhaltstreue- und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md) und die Eingangspunkte im [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Es werden keine Rechtsprechungsanker benötigt und keine juristischen Fundstellen erzeugt.

## Ausgabeformat

1. Zuerst kompakte Paketkarte mit Paket-ID, erkanntem Hauptschriftsatz, Quellenzahl, frühester Frist, Parteirolle, Anlagenstand, Ampel/Grund und genau einer nächsten Arbeitsaktion.
2. Paketkopf mit Projektordner, Gericht/Aktenzeichen, Frist und Status.
3. kompaktes Quelleninventar mit höchstens sieben Spalten; technische Zusatzfelder stehen im getrennten Maschinenprotokoll.
4. Rollenliste `Hauptschriftsatz`, `Anlage`, `intern`, `Dublettenverdacht`, `unklar`.
5. Delta-Tabelle `unverändert`, `geändert`, `neu`, `fehlt`, `unklar` mit Wiederverwendungsgrund.
6. gebündelte Rückfragen und rote Stopps.
7. Fortsetzungsmarke und Werkstattplan mit genau der nächsten Arbeitsaktion.

Das Inventar wird mit verständlichen vollständigen Bezeichnungen ausgegeben. Eine unkommentierte Dateiliste ist kein fertiges Arbeitsergebnis.

## Beispiele

- `Replik_final.docx`, zwölf PDFs und drei JPEGs: Hauptfassung bestätigen, höchste K-Nummer fragen, danach vollständige Kette starten.
- `Klage_final.docx` und `Klage_final_neu.docx`: Versionskonflikt gelb; keine automatische Wahl nach Änderungsdatum.
- ZIP mit Anlagen: ZIP nur in den Arbeitsbereich entpacken und inventarisieren; ZIP nicht für den Gerichtsversand übernehmen.
