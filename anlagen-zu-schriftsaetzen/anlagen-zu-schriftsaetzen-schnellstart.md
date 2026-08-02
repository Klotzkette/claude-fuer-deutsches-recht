# Anlagen zu Schriftsätzen: Schnellstart zur beA-Versandmappe

## 1. Auftrag

Mache aus dem vorhandenen Schriftsatz und dem zugehörigen Dokumentenordner eine kontrollierte, versandfertige Gerichtsmappe. Lies zuerst alle Dateien, liefere dann die Produktionsmatrix, arbeite erkennbare Schritte sofort ab und frage höchstens nach einer Weiche, ohne die Nummernkreis, Frist, Gericht oder Signaturweg falsch würden.

Versende niemals selbst. Das Endprodukt ist so vorbereitet, dass der verantwortliche Anwalt es nach eigener Schlussprüfung elektronisch versenden kann.

## 2. Sofortausgabe

Beginne mit höchstens sieben Sätzen: Schriftsatzstand und Verfahrensrolle, Gericht mit Aktenzeichen und Frist, Zahl der genannten und der vorhandenen Anlagen, erste Nummernlücke oder erster Widerspruch, gewähltes oder offenes Dateinamensprofil, stärkster Stop-Punkt und der nächste unmittelbar ausgeführte Produktionsschritt.

Danach diese Matrix ausfüllen:

| Position | Schriftsatzstelle | Datei | Beweisthema | Nummer | PDF/Stempel | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | gesamte Fassung | Datei | Anträge und Vortrag | 00 | final oder offen | Status |
| Anlage | Seite und Absatz | Datei | konkrete Tatsache | K 1 oder B 1 | offen oder fertig | Status |

## 3. Arbeitsfolge

### 3.1. Schriftsatz lesen

Prüfe Rubrum, Gericht, Aktenzeichen, Anträge, Datum, Unterschriftszeile und jede Anlagenreferenz. Eine tragende Tatsache muss im Schriftsatz stehen; eine Anlage darf sie belegen, aber nicht ersetzen.

### 3.2. Dateien zuordnen

Ordne jede Datei genau einer Anlagenreferenz oder einer begründeten internen Kategorie zu. Weise fehlende Belege, Dubletten, alte Fassungen, unleserliche Scans, widersprüchliche Daten und Dateien ohne Schriftsatzbezug aus.

### 3.3. Nummernkreis fortführen

- Kläger: `K`.
- Beklagter: `B`.
- Antragsteller oder Antragsgegner: erkennbare gerichtliche oder kanzleiinterne `AST`- oder `AG`-Logik.

Replik, Duplik und weiterer Schriftsatz setzen den bisherigen Nummernkreis fort. Beginne nicht wieder bei 1. Bei fehlender Vorakte nur diese eine Weiche erfragen.

### 3.4. PDF erzeugen

Jede Versandanlage wird eine eigene PDF. Originaldatei intern erhalten. Word, Tabelle, Präsentation oder Bild kontrolliert konvertieren; danach Seitenumbrüche, abgeschnittene Spalten, Kommentare, Drehung, Auflösung und OCR visuell prüfen. PDF/A nur bestätigen, wenn technisch validiert.

### 3.5. Jede Seite stempeln

Setze `Anlage K 1`, `Anlage B 1` oder die festgelegte Bezeichnung auf jeder Seite oben rechts. Nichts überdecken. Bei engem Rand Position oder Seitenrand kontrolliert anpassen. Stempel, Dateiname, Verzeichnis und Schriftsatz müssen identisch nummeriert sein.

### 3.6. Dateinamen bilden

Gerichtshinweis geht vor. Fehlt er, nutze das strenge Profil: ASCII, Unterstriche, führende Reihenfolge, höchstens 60 Zeichen einschließlich `.pdf`.

- Hauptdokument: `00_20260710_Replik.pdf`
- Anlage: `01_20260710_AnlageK1_Kaufvertrag.pdf`

Berlin empfiehlt `00` für das Hauptdokument, Anlagen ab `01`, Datum, Kurzinhalt, keine Umlaute und maximal 60 Zeichen. NRW empfiehlt die Rolle nur am Hauptdokument, etwa `K_Schriftsatz_mit_Antraegen.pdf`, und neutrale Anlagen wie `Anlage_01.pdf`. Die ERVB 2025 erlaubt bundesweit bis zu 90 Zeichen und auch Umlaute; ASCII mit 60 Zeichen ist deshalb ein strenger Kanzleistandard, kein gesetzliches Verbot.

Eine Versandnachricht betrifft genau ein Verfahren. Füge Hauptdokument und Anlagen als einzelne PDFs bei, niemals als ZIP; verwende keinen Kennwortschutz und kontrolliere die erzeugten Strukturdaten.

### 3.7. Technisch prüfen

Prüfe Öffnung ohne Kennwort, Seitenzahl, Lesbarkeit, OCR, eingebettete Dateien, aktive Inhalte, Dateinamenlänge, Hashwert, Einzelgröße und Gesamtgröße. Nach ERVB 2025 höchstens 1000 Dateien und insgesamt 200 MB je Nachricht. Große Pakete in bezeichnete Teile aufteilen, aber nie eine mehrseitige Anlage zerlegen.

## 4. Formanker

### 4.1. Signaturweg

Das Hauptdokument braucht entweder eine qualifizierte elektronische Signatur der verantwortenden Person oder deren einfache Signatur mit persönlichem Versand über den eigenen sicheren Übermittlungsweg. Anlagen benötigen keine eigene Signatur.

- BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23: Bei einfacher Signatur müssen verantwortende Person und tatsächlicher Versender übereinstimmen.
- BGH, Beschluss vom 4. September 2024, IV ZB 31/23: Das Postfach eines anderen Anwalts ersetzt diesen persönlichen sicheren Weg nicht.
- BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23: Versand durch Mitarbeiter erfordert für das Hauptdokument die qualifizierte elektronische Signatur.

### 4.2. Eingangskontrolle

Die Frist wird erst nach positiver Kontrolle der automatisierten gerichtlichen Eingangsbestätigung erledigt.

- KG, Beschluss vom 22. August 2023, 27 U 40/23: Eingang mit Speicherung auf der gerichtlichen Empfangseinrichtung.
- OLG Brandenburg, Beschluss vom 23. August 2022, 12 U 113/22: Frist erst nach Kontrolle von `request executed` und `erfolgreich` löschen.
- BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22: organisierte Ausgangskontrolle anhand der Eingangsbestätigung.
- BGH, Beschluss vom 24. April 2025, III ZB 12/24: Eingangsbestätigung abrufen und innerhalb ausreichender Reaktionsreserve prüfen.

### 4.3. Störung

ZPO Paragraf 130a Absatz 6 betrifft ein eingegangenes, aber technisch ungeeignetes Dokument. Die Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit steht in ZPO Paragraf 130d Sätze 2 bis 4.

- BGH, Beschluss vom 19. Dezember 2024, IX ZB 41/23: veröffentlichte zuverlässige Serverstörung kann die Glaubhaftmachung tragen.
- BGH, Beschluss vom 25. Februar 2025, VI ZB 19/24: pauschale Störungsformel genügt nicht; technische Ursache und vorübergehende Natur geschlossen schildern.
- OLG Brandenburg, Urteil vom 28. April 2023, 11 U 244/22: Dauer, betroffene Postfächer und Fortbestand der Störung konkret belegen; bloßer Bildschirmabzug genügt nicht.
- LG Hagen, Urteil vom 15. Oktober 2024, 4 O 209/24: unzulässige Papiereinreichung wird nicht beliebig später durch elektronisches Nachreichen geheilt.

## 5. Stop-Ampel

Stoppe die Freigabe bei ungeklärter Frist oder Gericht, nicht finalem Hauptdokument, falschem Signaturweg, fehlender oder unleserlicher Anlage, widersprüchlichem Nummernkreis, aktivem PDF-Inhalt, verschlüsselter Datei oder nicht kontrollierter Konvertierung.

Bei einer bloßen OCR- oder PDF/A-Prüflücke liefere den konkreten Prüfschritt und Verantwortlichen. Stelle niemals eine nicht gemessene Eigenschaft als erfüllt dar.

## 6. Auslieferung

```text
versandfertig/
  00_..._Schriftsatz.pdf
  01_..._AnlageK1_....pdf
  02_..._AnlageK2_....pdf
intern/
  Anlagenverzeichnis.md, Versandmanifest.csv
  Preflight-Bericht.md, Freigabevermerk.md, Eingangskontrolle.md
```

Der interne Ordner wird nicht mitgesendet. Beende mit Stop-Liste oder ausformuliertem Freigabevermerk, gewähltem Signaturweg und genauer Eingangskontrolle.
