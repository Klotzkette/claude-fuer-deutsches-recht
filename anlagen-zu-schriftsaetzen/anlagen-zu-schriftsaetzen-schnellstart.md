# Anlagen zu Schriftsätzen: Schnellstart zur beA-Versandmappe

Lies Nutzersachverhalt, Schriftsatz und vorhandene Anlagen zuerst. Führe den konkreten Produktionsauftrag aus; ohne solchen beginne mit der Zuordnung der Belege. Frage nur nach blockierenden Lücken. Bei großen Ordnern Teilstand und ungelesene Dateien nennen. Geänderte Fassungen neu prüfen. Ohne Export Text liefern, keinen Dateilink erfinden. Ungeprüfte Dateien nicht freigeben.

## 1. Auftrag

Lies den Schriftsatz, ordne genannte Anlagen anhand von Name, Format, Größe und Datum zu und öffne sie in Nummernfolge. Führe die Matrix fort; frage nur bei offenem Nummernkreis, Frist, Gericht oder Signaturweg.

Versende niemals selbst. Das Endprodukt ist so vorbereitet, dass der verantwortliche Anwalt es nach eigener Schlussprüfung elektronisch versenden kann.

## 2. Sofortausgabe

Ohne konkreten Produktionsauftrag genügen zunächst Schriftsatzstand, Rolle, Gericht, Aktenzeichen, Frist, Anlagenzahl, Nummernlücke, Namensprofil und Stop-Punkt. Sonst direkt den verlangten Produktionsschritt ausführen.

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

Das 60-Zeichen-Profil ist eine interne Konvention, kein gesetzliches Verbot längerer Dateinamen oder von Umlauten. Prüfe vor Freigabe die aktuelle ERVB und konkrete gerichtliche Hinweise. Die [amtlichen Hinweise zum elektronischen Rechtsverkehr](https://www.berlin.de/gerichte/arbeitsgericht/service/elektronischer-rechtsverkehr-erv/was-ist-bei-den-elektronischen-dokumenten-zu-beachten/) erläutern die ERVB 2025 mit maximal 90 Zeichen einschließlich Dateiendung.

Eine Versandnachricht betrifft genau ein Verfahren. Füge Hauptdokument und Anlagen als einzelne PDFs bei, niemals als ZIP; verwende keinen Kennwortschutz und kontrolliere die erzeugten Strukturdaten.

### 3.7. Technisch prüfen

Prüfe Öffnung ohne Kennwort, Seitenzahl, Lesbarkeit, OCR, eingebettete Dateien, aktive Inhalte, Dateinamenlänge, Hashwert, Einzelgröße und Gesamtgröße. Nach ERVB 2025 höchstens 1000 Dateien und insgesamt 200 MB je Nachricht; die oben verlinkten amtlichen Hinweise bestätigen diese Grenzen. Große Pakete in bezeichnete Nachrichten aufteilen. Eine mehrseitige Anlage möglichst zusammenhalten; überschreitet sie allein die Grenze, einen gesonderten Übermittlungsplan nach aktueller ERVV prüfen, statt technische Versandfähigkeit zu behaupten.

## 4. Formanker

### 4.1. Signaturweg

Nach [Paragraf 130a Absatz 3 ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) benötigt das elektronische Hauptdokument eine qualifizierte elektronische Signatur der verantwortenden Person oder deren Signatur und einen sicheren Übermittlungsweg. Die Vorschrift nimmt beigefügte Anlagen davon aus. Dokumentiere verantwortende Person, Signaturart und vorgesehene versendende Person konkret; ungeklärte Delegation sperrt die Versandfreigabe, nicht die Anlagenzuordnung.

### 4.2. Eingangskontrolle

Paragraf 130a Absatz 5 ZPO knüpft den Eingang an die Speicherung auf der gerichtlichen Empfangseinrichtung und sieht eine automatisierte Bestätigung vor. Bereite einen Kontrollauftrag für Empfänger, Verfahren, Dateien, Übermittlungsstatus und Eingangszeitpunkt vor. Ein lokal fertiges Paket belegt keinen gerichtlichen Eingang. Die Frist bleibt im internen Ablauf bis zur positiven Eingangskontrolle offen.

### 4.3. Störung

ZPO Paragraf 130a Absatz 6 betrifft ein eingegangenes, aber technisch ungeeignetes Dokument. Die Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit steht in [Paragraf 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html). Halte Fehlerzeit, betroffene Funktion, Fehlermeldung und Versuche fest. Keine Ersatzübermittlung allein aus einem unspezifischen Fehlerhinweis freigeben. Fallbezogene Rechtsprechung nur nach amtlicher Verifikation hinzunehmen.

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

Optional vertieft [Schriftsatz-Anlagen-Mapping](skills/schriftsatz-anlagen-mapping/SKILL.md) die Zuordnung; ohne diese Datei genügt die Arbeitsfolge oben. Vermerke in vollständigen Sätzen mit dezimaler Gliederung und Leerzeilen ausgeben; Times New Roman 11 pt verwenden oder als Exporthinweis nennen. Tabellen dürfen für lesbare Spalten abweichen.
