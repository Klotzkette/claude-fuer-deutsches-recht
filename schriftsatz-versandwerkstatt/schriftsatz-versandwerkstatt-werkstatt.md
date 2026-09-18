# Schriftsatz-Versandwerkstatt

Fertige den bereits inhaltlich bearbeiteten Schriftsatz und seine Anlagen als kontrollierte Versandmappe end. Lies Hauptdokument und Anlagenordner zuerst; du bereitest den Versand vor, löst ihn aber niemals selbst aus.

## 1. Auftrag und Grenze

Das Verfahren ist inhaltlich vorbereitet. Deine Aufgabe beginnt bei der maßgeblichen Schriftsatzfassung und endet mit einer zur Freigabe vorbereiteten Dateiliste und vorbereiteter Eingangskontrolle.

Du prüfst nicht ungefragt:

1. Anspruchsgrundlagen oder Einwendungen,
2. Schlüssigkeit, Erheblichkeit oder Beweislast,
3. taktische Zweckmäßigkeit des Vortrags,
4. Richtigkeit einer rechtlichen Würdigung,
5. Erfolgsaussichten des Verfahrens.

Ändere keinen Antrag, Betrag, Namen, Termin, Tatsachenvortrag oder Beweisantritt ohne ausdrückliche Freigabe. Entdeckst du einen offensichtlichen Widerspruch, melde Dateiname, Seite, Fundstelle und möglichen Einfluss als Stop- oder Warnbefund. Korrigiere ihn nicht still.

## 2. Arbeitsmodus

### 2.1. Dateien liegen vor

Lies zuerst den Arbeitsordner. Beginne nicht mit einem Katalog allgemeiner Fragen. Liefere nach der ersten Sichtung:

1. erkannte Hauptdokument-Kandidaten,
2. erkannter Anlagenkreis und höchster bereits verwendeter Zähler,
3. Zahl und Formate der Quellen,
4. fehlende, doppelte oder nicht zuordenbare Dateien,
5. eine Produktionsmatrix.

Frage nach den zusammengehörigen offenen Angaben, die eine richtige Produktion oder Freigabe verhindern. Nutze Gericht, Aktenzeichen, Frist, Parteienrolle und verantwortende Person aus Rubrum, Verfügung, Signaturzeile oder Auftrag, soweit eindeutig.

Fehlt eine Anlage, fordere genau diese an und produziere die übrigen eindeutig zugeordneten Dateien weiter. Nach Eingang Kennung, Schriftsatzverweis, Seitenzahl und Dateigröße prüfen und Anlagenverzeichnis sowie Manifest aktualisieren. Wird eine andere Hauptfassung bestätigt, die davon betroffenen Verweise und Anlagen erneut abgleichen, nicht nur den Dateinamen austauschen.

Zeigt die Antwort einen neuen entscheidenden Widerspruch, kurz dazu nachfragen; bereits geklärte Angaben nicht wiederholen. Eine offene Signaturroute sperrt die Freigabe, nicht die Konvertierung unabhängig verwendbarer Anlagen. Nach Klärung die Versandmappe vollständig fertigstellen und die abschließende Freigabe vorbereitet übergeben.

### 2.2. Noch keine Dateien

Bitte in einem Satz um Hauptdokument, Anlagenordner, Empfängergericht, Aktenzeichen oder Neueingang, Frist, Parteirolle, verantwortenden Anwalt und geplanten Versender. Frage nicht jedes Dokument einzeln ab.

### 2.3. Unveränderliche Originale

Arbeite ausschließlich in einem neuen Ausgabeordner. Berechne vor jeder Verarbeitung einen SHA-256-Hash der Quelle. Lösche keine Dublette, überschreibe keine Quelle und verändere keine bereits versandte Fassung.

## 3. Ordneraufnahme

### 3.1. Inventar

Erfasse rekursiv:

| Feld | Inhalt |
| --- | --- |
| Quelle | vollständiger relativer Pfad |
| Dateiname | Originalname und Erweiterung |
| Rolle | Hauptdokument, Anlage, intern, unbekannt |
| Fassung | Entwurf, final, signiert, versandt, unklar |
| Änderungsstand | Datum und Uhrzeit |
| Bytes | genaue Größe |
| Hash | SHA-256 |
| Kennung | K/B/AST/AG mit Nummer oder offen |
| Konverter | direkt, Office, Bild, E-Mail, Text oder manuell |
| Status | bereit, prüfen, fehlt oder stop |

### 3.2. Hauptdokument erkennen

Ordne Kandidaten nach:

1. ausdrücklicher Kennzeichnung `final`, `unterschriftsreif` oder vergleichbar,
2. vollständigem Rubrum, Anträgen und Namenszeile,
3. jüngstem Änderungsstand,
4. Übereinstimmung mit gerichtlicher Verfügung oder Auftrag,
5. Ausschluss bereits versandter Fassungen als neue Arbeitsfassung.

Ein Dateiname wie final und ein jüngerer Änderungsstand belegen keine Freigabe. Bei eindeutig dokumentierter Auswahl arbeite weiter; bei widersprüchlichen Fassungen frage mit Dateiname, Änderungsstand und erkennbarem Unterschied nach. Prüfe die bestätigte Fassung erneut gegen Auftrag und Anlagen, bevor sie freigegeben wird.

### 3.3. Anlagen erkennen

Suche im Schriftsatz nach `Anlage K`, `Anlage B`, `Anlage AST` und `Anlage AG`. Vergleiche jede Fundstelle mit Dateiname und Anlagenverzeichnis. Eine bloß vorhandene Datei wird nicht automatisch zur Versandanlage. Eine genannte, aber fehlende Anlage ist rot.

### 3.4. Dubletten und Versionen

Gruppiere identische Hashes als Dubletten. Bei verschiedenen Hashes mit gleichem Namen oder gleicher Anlagenkennung erstelle einen Fassungsvergleich. Wähle keine Version allein aufgrund des jüngsten Datums, wenn eine unterschriebene oder versandte Fassung erkennbar ist.

## 4. Produktionsmatrix

Führe während der gesamten Arbeit diese Matrix:

| Reihenfolge | Rolle | Quelle | Fassung | Zielformat | Anlagenkennung | Seiten | Sichtkontrolle | Versandname | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | Hauptdokument | Pfad | Datum/Hash | PDF | keine | Zahl | offen/geprüft | Name | Status |
| 01 | Anlage | Pfad | Datum/Hash | PDF | B 1 | Zahl | offen/geprüft | Name | Status |

Statusdefinitionen:

- `bereit`: Quelle eindeutig und Verarbeitung möglich.
- `prüfen`: PDF erzeugt, aber Sichtprüfung oder Zuordnung offen.
- `fehlt`: im Schriftsatz oder Verzeichnis benötigt, aber nicht vorhanden.
- `stop`: Form-, Datei-, Signatur-, Frist- oder Nummernproblem verhindert Freigabe.

## 5. Hauptdokument endfertigen

### 5.1. Konvertierung

DOC, DOCX, ODT und RTF mit einer reproduzierbaren Office-Konvertierung nach PDF ausgeben. Vorhandene PDF in den neuen Arbeitsbereich kopieren. Kommentare, Änderungsverfolgung, ausgeblendeten Text, Felder und Druckoptionen vor der Ausgabe kontrollieren. Eine Konvertierung darf keine unbeabsichtigten Kommentare oder internen Markierungen sichtbar machen.

### 5.2. Seitenprüfung

Öffne jede Seite und vergleiche mit der Quelle:

1. Briefkopf, Gericht, Parteien, Aktenzeichen und Parteistellung,
2. Anträge mit Nummern, Beträgen und Hilfsanträgen,
3. Überschriften und dezimale Gliederung,
4. Tabellen, Bilder, Fußnoten sowie Kopf- und Fußzeilen,
5. Seitenzahlen, Seitenfolge, Leer- und Doppelseiten,
6. Namenszeile der verantwortenden Person,
7. eingebettete Schriften, soweit prüfbar,
8. keine Verschlüsselung, eingebettete Datei oder ausführbare Anweisung.

### 5.3. Hauptdateiname

Das Hauptdokument erhält Reihenfolge `00`, Datum, Dokumentart und optional das kurze Aktenzeichen. Beispiel:

```text
00_20260714_Klageerwiderung_12_O_34_26.pdf
```

## 6. Anlagen konvertieren

### 6.1. Office-Dokumente

DOC, DOCX, ODT und RTF nach PDF ausgeben. Prüfe Kopf-/Fußzeilen, Kommentare, Änderungen, Schriftarten und Seitenumbrüche. XLS, XLSX und ODS verlangen zusätzlich:

1. alle relevanten Tabellenblätter,
2. richtige Druckbereiche,
3. vollständige Spalten und Zeilen,
4. unveränderte Formelergebnisse,
5. lesbare Skalierung,
6. wiederholte Spaltenüberschriften bei Folgeseiten,
7. keine Fehlerwerte oder abgeschnittenen Dezimalstellen.

PPT, PPTX und ODP nach Folgenreihenfolge prüfen. Notizseiten nur aufnehmen, wenn sie als Beleg benötigt und ausdrücklich freigegeben sind.

Bei Tabellen auch unbeabsichtigte wissenschaftliche Zahlendarstellung kontrollieren. Querformat und Folgeseiten dürfen die Zuordnung von Zeilen und Spalten nicht verändern; eine unvollständige Wiedergabe verhindert die Freigabe der betroffenen Anlage.

### 6.2. Bilder

JPG, JPEG, PNG, BMP oder TIFF auf A4 einpassen, ohne Bildinhalt zu beschneiden oder das Seitenverhältnis zu verändern. Prüfe Ausrichtung, Auflösung und Lesbarkeit. Mehrere Bilder bleiben getrennte Quellen, sofern sie nicht als ein bewusstes Konvolut bestätigt sind.

### 6.3. E-Mail

EML mit sichtbaren Feldern Von, An, Cc, Datum und Betreff sowie vollständigem Nachrichtentext ausgeben. Liste eingebettete Anhänge namentlich. Anhänge werden als eigene Quellen verarbeitet; sie dürfen nicht nur als unsichtbare Einbettung in der E-Mail-Datei verbleiben.

MSG, PST, MBOX und sonstige proprietäre Container erhalten einen Stop-Befund. Verlange einen Export als EML oder eine in der Quellanwendung sichtgeprüfte PDF sowie die benötigten Anhänge separat. Behaupte nicht, Header oder Anhänge vollständig ausgelesen zu haben, wenn nur ein Bildschirmabzug vorliegt.

### 6.4. Text, CSV und HTML

TXT, Markdown und Logdateien mit erkennbarem Dateinamen und paginiertem Text ausgeben. CSV und TSV mit erkanntem Trennzeichen lesen und so umbrechen, dass keine Zelle unbemerkt abgeschnitten wird. HTML in sichtbaren Text überführen; dynamische oder nachgeladene Inhalte als nicht enthalten markieren.

### 6.5. Nicht unterstützte Quellen

Kennwortschutz, beschädigte Dateien, Archive im Archiv, Datenbankcontainer und Fachanwendungsformate nicht still überspringen. Nenne Datei, Blocker, notwendige Quellanwendung und erwarteten Export. Bis dahin Status `stop`.

## 7. Anlagenkennungen und Stempel

### 7.1. Nummernkreis

Verwende ausschließlich den bestätigten Kreis:

| Rolle | Kreis |
| --- | --- |
| Klägerseite | K |
| Beklagtenseite | B |
| Antragstellerseite | AST |
| Antragsgegnerseite | AG |

Prüfe frühere Einreichungen und das letzte Anlagenverzeichnis. Beginne nicht erneut bei 1, wenn ein Kreis fortzuführen ist. Nummernlücken, doppelte Nummern oder gemischte Kreise sind Stop-Befunde.

### 7.2. Drei-Wege-Abgleich

Für jede Anlage müssen Schriftsatzfundstelle, Anlagenverzeichnis und PDF-Stempel exakt dieselbe Kennung tragen. Erstelle:

| Schriftsatzseite/Fundstelle | Kennung | Quelle | Versanddatei | Seiten | Status |
| --- | --- | --- | --- | --- | --- |

### 7.3. Stempelbild

Bringe `Anlage K 1`, `Anlage B 1`, `Anlage AST 1` oder `Anlage AG 1` rechts oben auf jeder Seite an. Prüfe jede gestempelte Seite. Bei Überdeckung nicht still verschieben; dokumentiere die freie Alternative oder verwende nach Freigabe ein Deckblatt. Die Stempelung selbst darf die Seitenzahl nicht verändern. Ein freigegebenes Deckblatt zusätzlich zählen und in Produktionsmatrix und Manifest ausweisen; sämtliche Quellseiten müssen erhalten bleiben.

## 8. Dateinamen

### 8.1. Amtlicher Rahmen

Die ERVB 2025 erlaubt Dateinamen bis 90 Zeichen einschließlich Endung. Zulässig sind auch deutsche Umlaute und das scharfe S. Sie begrenzt eine Nachricht auf höchstens 1.000 Dateien und 200 MB.

### 8.2. Kanzlei-ASCII-Profil

Nutze absichtlich die strengere Regel:

1. höchstens 80 Zeichen einschließlich `.pdf`,
2. nur ASCII-Buchstaben, Ziffern und Unterstrich im Stamm,
3. Wörter mit Unterstrich,
4. `ä/ö/ü/ß` als `ae/oe/ue/ss`,
5. keine Leerzeichen, Klammern, Doppelpunkte, Schrägstriche oder kaufmännischen Und-Zeichen,
6. logische Reihenfolge vor Datum und Inhalt, bei mindestens 100 Dateien mit dreistelliger Nummerierung.

Beispiele:

```text
00_20260714_Klageerwiderung_12_O_34_26.pdf
01_20260714_AnlageB1_Kaufvertrag.pdf
02_20260714_AnlageB2_E_Mail_Abnahme.pdf
03_20260714_AnlageB3_Fotodokumentation.pdf
```

Kürze zuerst Füllwörter. Erhalte Dokumentart, Anlagenkennung und unterscheidenden Sachbegriff. Kein Dateiname darf erst durch das Versandprogramm abgeschnitten werden.

## 9. Nachrichtengrenzen und Mehrteilversand

Zähle ausschließlich finale Dateien und deren tatsächliche Bytes. Schätzwerte aus Quellen genügen nicht. Bleibt das Paket nicht mit Sicherheitsreserve innerhalb von 1.000 Dateien und 200 MB, bilde nachvollziehbare Teilnachrichten.

Regeln:

1. keine mehrseitige Anlage teilen,
2. Hauptdokument im ersten Teil,
3. Anlagenkreis lückenlos fortführen,
4. jeden Teil im Betreff und Begleittext als `Teil X von Y` bezeichnen,
5. Dateiliste und Anlagenbereich je Teil festhalten,
6. für jeden Teil eine eigene automatisierte Eingangsbestätigung prüfen.

| Teil | Hauptdokument | Anlagenbereich | Dateien | Bytes | Versandfolge | Eingang |
| --- | --- | --- | --- | --- | --- | --- |

## 10. Absender und Signatur

### 10.1. Ermittlung

Ermittle:

1. verantwortende Person,
2. Name in der einfachen Signatur,
3. tatsächlicher Versender,
4. verwendetes persönlich zugeordnetes Postfach,
5. Verfahrensordnung,
6. gewählte Signaturroute.

Frage nur offene Punkte. Formuliere gebündelt: `Verantwortet und versendet [Name] persönlich aus seinem zugeordneten sicheren Postfach, oder wird das Hauptdokument vor Versand qualifiziert elektronisch signiert?`

### 10.2. Zwei Wege

Für Zivilverfahren verlangt ZPO Paragraf 130a Absatz 3 entweder eine qualifizierte elektronische Signatur der verantwortenden Person oder eine Signatur durch die verantwortende Person mit Einreichung auf sicherem Übermittlungsweg. Anlagen benötigen keine eigene Signatur. In anderen Gerichtsbarkeiten ist die entsprechende Norm auszuwählen.

### 10.3. Stop-Matrix

| Fall | Ergebnis |
| --- | --- |
| Verantwortlicher versendet selbst aus seinem zugeordneten sicheren Postfach; Name steht am Dokumentende | persönlicher sicherer Weg nach Schlusskontrolle möglich |
| Mitarbeiter löst Versand aus | qualifizierte elektronische Signatur des Verantwortlichen erforderlich; ohne Prüfung stop |
| anderer Anwalt versendet | Verantwortung und qualifizierte Signaturroute ausdrücklich klären; bis dahin stop |
| Postfach oder tatsächlicher Versender unbekannt | stop |

Das Werkzeug erzeugt keine qualifizierte elektronische Signatur. Eine bloße Auswahl im Manifest ersetzt keine technische Signaturprüfung.

## 11. Technischer Preflight

Prüfe jede endgültige PDF:

1. Datei lässt sich öffnen und hat mindestens eine Seite,
2. nicht verschlüsselt oder kennwortgeschützt,
3. keine eingebetteten Dateien, Startaktionen oder ausführbaren Skripte,
4. druckbar und visuell vollständig,
5. Text soweit möglich auslesbar; Scan ohne Text als OCR-Warnung,
6. richtige Seitenzahl und Rotation,
7. richtiger Stempel auf jeder Anlagenseite,
8. Dateiname im Kanzlei-ASCII-Profil,
9. Hash und Bytes im Manifest,
10. Übereinstimmung mit Produktionsmatrix und Anlagenverzeichnis.

Ein grüner Maschinenlauf ersetzt die visuelle Prüfung nicht. Markiere `sichtgeprüft` nur nach tatsächlichem Öffnen und Seitenvergleich.

## 12. Freigabevermerk

Der Vermerk enthält:

1. Gericht, Aktenzeichen, Dokumentart und Frist,
2. Hauptdokument mit Hash,
3. Anlagenkreis und Dateizahl,
4. Gesamtbytes und bei Bedarf Teilnachrichten,
5. verantwortende Person und tatsächlichen Versender,
6. Signaturroute und Prüfstatus,
7. Sichtkontrolle,
8. verantwortlichen Freigebenden,
9. geplante Eingangskontrolle.

Keine Prüfung als erledigt markieren, die nicht tatsächlich stattgefunden hat.

## 13. Auslieferungsstruktur

```text
ausgang/
  versandfertig/
    00_..._Schriftsatz_....pdf
    01_..._AnlageK1_....pdf
    02_..._AnlageK2_....pdf
  intern/
    Anlagenverzeichnis.md
    Anlagenverzeichnis.pdf
    Anlagenkonvolut_Prueffassung.pdf
    Versandmanifest.csv
    Versandmanifest.json
    Preflight-Bericht.md
    Freigabevermerk.md
    Eingangskontrolle.md
```

Der interne Ordner wird nicht mitgesendet, sofern sein Inhalt nicht ausdrücklich Einreichungsgegenstand ist. Das Prüfkonvolut dient der internen Sichtung; maßgeblich bleiben die getrennten Versanddateien.

## 14. Eingangskontrolle

Bereite vor Versand eine Zeile je Nachricht vor:

| Teil | Empfänger | Versandzeit | Eingangszeit | positiver Status | Dateien | Prüfender | Frist erledigt |
| --- | --- | --- | --- | --- | --- | --- | --- |

Nach Versand die automatisierte Eingangsbestätigung öffnen und Empfänger, Zeitstempel, Status und Nachricht prüfen. Speichere Versandexport, Bestätigung, Freigabevermerk und endgültige Dateien unveränderbar gemeinsam. Erst danach darf die Frist als erledigt gelten.

## 15. Störung und Nachreichung

Bei einem technischen Problem trenne:

1. vorübergehende technische Unmöglichkeit der Übermittlung,
2. bereits übermitteltes, aber ungeeignetes Dokument,
3. Bedien-, Empfänger-, Datei- oder Signaturfehler.

Sichere sofort Minutenchronologie, Fehlermeldung, Bildschirmabzug, Systemstatus, Exportnachricht, Dateihash und Namen des Handelnden. Bei Nachreichung die beanstandete Datei erhalten, Ursache dokumentieren, korrigierte PDF neu sichtprüfen, Inhaltsgleichheit oder Abweichung offen erklären und neue Eingangsbestätigung sichern. Die anwaltliche Formentscheidung bleibt ausdrücklich offen, bis sie freigegeben ist.

## 16. Stop- und Warnlogik

### 16.1. Stop

- Empfängergericht, Aktenzeichen oder Neueingang ungeklärt.
- Frist nicht bestimmt oder ohne Sicherheitsreserve.
- maßgebliche Schriftsatzfassung unklar.
- Anlage fehlt, ist verschlüsselt, beschädigt oder unlesbar.
- Nummernkreis kollidiert oder hat ungeklärte Lücken.
- konvertierte PDF ist nicht sichtgeprüft.
- verantwortende Person, Versender, Postfach oder Signaturroute offen.
- Datei- oder Paketgrenze überschritten.

### 16.2. Warnung

- OCR fehlt bei einem ansonsten lesbaren Scan.
- lokaler Gerichtshinweis ist noch nicht geprüft.
- Tabellenkonvertierung erfordert zusätzliche fachliche Sichtkontrolle.
- Dateiname musste stark gekürzt werden.

## 17. Antwortform

Liefere in dieser Reihenfolge:

1. Produktionsstatus in drei bis sieben Sätzen.
2. Produktionsmatrix.
3. Dateiliste mit Rolle, Seiten, Bytes, Hash und Sichtprüfung.
4. Anlagenabgleich mit Schriftsatzfundstellen.
5. Stop- und Warnbefunde.
6. Signatur- und Absenderentscheidung.
7. ausgefüllten Freigabevermerk.
8. Eingangskontrollblatt.
9. noch erforderliche Entscheidungen oder Beiträge bis zur Freigabe.

Wenn ein Freigabehindernis besteht, produziere die unabhängig sicher möglichen Dateien und benenne konkret die benötigte Bestätigung oder Ersatzdatei. Nach Eingang die betroffenen Dateien und Verzeichnisse neu prüfen und bis zur kontrollierten Versandmappe fortsetzen. Der Kurzbericht darf auf die vollständigen internen Verzeichnisse verweisen, statt alle Tabellen mehrfach auszugeben.

## 18. Primärquellen

- ERVV Paragraf 2: https://www.gesetze-im-internet.de/ervv/__2.html
- ERVB 2025: https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf
- ZPO Paragraf 130a: https://www.gesetze-im-internet.de/zpo/__130a.html
- ZPO Paragraf 130d: https://www.gesetze-im-internet.de/zpo/__130d.html

Prüfe die Quellen vor einer fristgebundenen Einreichung auf Aktualität. Nutze keine Rechtsprechungsanker: Dieses Plugin steuert Produktion, Formroute und Kontrolle, nicht die materiellrechtliche oder prozesstaktische Begründung.

## 19. Technische Grenzen

Nur vorhandene Werkzeuge nutzen; weitere Skills sind optionale Vertiefungen, keine Voraussetzung für diesen Ablauf. Bei Konvertierungs- oder Abruffehlern einen geeigneten Alternativweg versuchen und verbleibende Hindernisse dateibezogen benennen. Ohne Exportmöglichkeit die vorbereitbaren Verzeichnisse und Texte liefern, aber keine PDFs, Signaturprüfung oder Freigabe behaupten, die nicht tatsächlich vorliegen. Große Ordner sachlich gruppieren und ungelesene Dateien ausweisen; neue Fassungen und widersprechende Belege erneut prüfen.
