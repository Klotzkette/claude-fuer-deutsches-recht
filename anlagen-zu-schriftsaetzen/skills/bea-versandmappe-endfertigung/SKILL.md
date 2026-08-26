---
name: bea-versandmappe-endfertigung
description: "Endfertigung gerichtlicher Schriftsätze und Anlagen für beA und E-Akte: liest zuerst den vorhandenen Aktenordner, prüft Anträge, Belegbezüge, Signaturweg und ERVV, konvertiert Anlagen kontrolliert in PDF, stempelt jede Anlagenseite, vergibt fortlaufende K-, B-, AST- oder AG-Nummern und liefert Versandmappe, Anlagenverzeichnis, Freigabevermerk und."
---

# beA-Versandmappe endfertigen

## 1. Auftrag

Nutze diesen Skill, wenn ein Schriftsatz inhaltlich weitgehend steht und mit seinen Anlagen so fertiggestellt werden soll, dass der verantwortliche Anwalt ihn nach eigener Schlussprüfung über den vorgesehenen elektronischen Übermittlungsweg versenden kann.

Das Arbeitsprodukt ist nicht nur eine Checkliste. Es ist ein geordneter Versandordner mit Hauptdokument, einzeln bezeichneten Anlagen, Anlagenverzeichnis, Versandmanifest, Freigabevermerk und Plan für die Eingangskontrolle. Ein Versand wird niemals selbst ausgelöst.

## 2. Direktstart ohne Fragenkatalog

Wenn Dateien oder ein Aktenordner vorliegen, lies zuerst:

1. den neuesten Schriftsatzentwurf,
2. ein vorhandenes Anlagenverzeichnis,
3. alle im Schriftsatz genannten Anlagen,
4. gerichtliche Verfügungen mit Form-, Frist- oder Benennungsvorgaben,
5. vorhandene Versand- oder Kanzleistandards.

Liefere danach sofort eine erste Produktionsmatrix. Frage nur nach einem Punkt, der sich aus dem Material nicht zuverlässig ergibt und den nächsten Arbeitsschritt sperrt. Typische Sperrpunkte sind das Empfängergericht, der Nummernkreis, die laufende Frist oder die Entscheidung zwischen persönlichem Versand und qualifizierter elektronischer Signatur.

Wenn kein Material vorliegt, frage in einem Satz nach Schriftsatz, Anlagenordner, Gericht, Frist und Rolle. Frage nicht jedes Dokument einzeln ab.

## 3. Produktionsmatrix

Beginne mit dieser Tabelle und halte sie während der Arbeit aktuell:

| Position | Fundstelle im Schriftsatz | vorhandene Datei | Beweisthema | Nummer | technischer Status | offener Punkt |
| --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | gesamte Fassung | Datei | Anträge und Vortrag | 00 | Entwurf oder final | Freigabe |
| Anlage | Seite und Absatz | Datei | konkrete Tatsache | K 1 oder B 1 | PDF, lesbar, gestempelt | keiner oder Lücke |

Eine Anlage erhält erst dann den Status `versandfertig`, wenn Dateiinhalte, Anlagenzitat, Nummer, Stempel, Dateiname und Anlagenverzeichnis übereinstimmen.

## 4. Verfahrens- und Rollenweichen

### 4.1 Nummernkreis

- Kläger: `K 1`, `K 2` und fortlaufend.
- Beklagter: `B 1`, `B 2` und fortlaufend.
- Antragsteller: regelmäßig `AST 1`, `AST 2`, sofern Gericht oder Kanzleistandard nichts anderes vorgibt.
- Antragsgegner: regelmäßig `AG 1`, `AG 2`, sofern Gericht oder Kanzleistandard nichts anderes vorgibt.

Eine Replik beginnt keinen neuen Nummernkreis. Sie führt die Anlagen derselben Partei nach der zuletzt wirksam eingereichten Nummer fort. Dasselbe gilt für Duplik, Berufungsbegründung und weiteren Schriftsatz, sofern das Gericht keine abweichende Ordnung verfügt hat.

### 4.2 Verfahrensordnung

Prüfe zuerst die einschlägige Verfahrensordnung. ZPO Paragraf 130a und Paragraf 130d dürfen nicht ungeprüft auf jedes Verfahren übertragen werden. Bei Arbeits-, Sozial-, Verwaltungs-, Finanz- und Strafsachen gelten insbesondere ArbGG Paragraf 46c und Paragraf 46g, SGG Paragraf 65a und Paragraf 65d, VwGO Paragraf 55a und Paragraf 55d, FGO Paragraf 52a und Paragraf 52d sowie StPO Paragraf 32a und Paragraf 32d.

### 4.3 Europäische Gerichte

beA-Regeln gelten nicht für eine direkte Klage beim Gericht der Europäischen Union. Dort ist e-Curia der eigene Einreichungsweg. Verfahrensschriftstücke sind als PDF einzureichen, eine Datei darf nach der veröffentlichten e-Curia-Anleitung höchstens 30 MB groß sein; handschriftliche Signatur und Scan sind grundsätzlich nicht erforderlich. Diese Akte deshalb nicht in ein beA-Profil zwingen.

## 5. Inhaltliche Schlussprüfung des Schriftsatzes

Prüfe vor der technischen Produktion:

1. Stimmen Gericht, Parteien, Anschriften, Prozessrollen und gerichtliches Aktenzeichen?
2. Sind die Anträge bestimmt, vollständig und mit dem Vortrag vereinbar?
3. Steht jede tragende Tatsache im Schriftsatz selbst, statt nur in einer Anlage?
4. Ist jedes Beweisangebot einer konkreten Tatsachenbehauptung zugeordnet?
5. Werden alle Anlagen im Text eingeführt und wird keine nicht vorhandene Anlage zitiert?
6. Stimmen Datum, Beträge, Namen und Seitenfundstellen zwischen Schriftsatz und Beleg?
7. Sind Anlagen, die personenbezogene oder geschützte Daten Dritter enthalten, auf Erforderlichkeit und Schwärzung geprüft?

Verändere den materiellen Vortrag nicht stillschweigend. Weise Widersprüche aus und liefere einen konkreten Korrekturvorschlag zur Freigabe.

## 6. Anlagenproduktion

### 6.1 Konvertierung

Jede einzureichende Anlage wird spätestens für den Versand in eine eigene lesbare PDF-Datei überführt. Für Word-, Tabellen-, Präsentations- und Bilddateien gilt:

1. Originaldatei unverändert in der internen Akte erhalten.
2. PDF aus der Originalanwendung oder kontrolliert mit einem Konvertierungswerkzeug erzeugen.
3. Seitenumbrüche, ausgeblendete Tabellenbereiche, Kommentare, Änderungsmarken, abgeschnittene Spalten und Bilddrehung visuell prüfen.
4. Bei Scans OCR ergänzen, ohne das sichtbare Seitenbild zu ersetzen.
5. Die erzeugte PDF erneut öffnen und jede Seite auf Vollständigkeit prüfen.

Ein bloßer erfolgreicher Konvertierungsbefehl ist keine Freigabe. PDF/A-Konformität nur behaupten, wenn sie mit einem geeigneten Prüfwerkzeug nachgewiesen wurde.

### 6.2 Anlagenstempel

Bringe die Bezeichnung auf jeder Seite der jeweiligen Anlage oben rechts an, etwa `Anlage K 7`. Der Stempel darf Text, Stempel, Unterschriften, Seitenzahlen oder maschinenlesbare Codes nicht überdecken. Bei zu engem Rand ist zunächst eine sichere Position oder ein zusätzlicher Rand zu schaffen; ein unsichtbarer oder abgeschnittener Stempel ist ein Stop-Fehler.

Bei einem Konvolut bleibt die Hauptbezeichnung auf jeder Seite sichtbar. Untergliederungen wie `K 12.1` werden nur verwendet, wenn Schriftsatz, Deckblatt und Verzeichnis dieselbe Logik durchhalten.

### 6.3 Dateinamen

Wähle das Profil anhand des Empfängergerichts und dokumentiere die Quelle:

| Profil | Regel | Beispiel |
| --- | --- | --- |
| Gerichtssicher | maximal 60 Zeichen, ASCII, Unterstriche, führende Reihenfolge | `01_20260710_AnlageK1_Kaufvertrag.pdf` |
| Berlin | Hauptdokument `00`, Anlagen `01` fortlaufend, Datum und Kurzinhalt, maximal 60 Zeichen, keine Umlaute oder Sonderzeichen | `02_20260710_AnlageK2_Mahnung.pdf` |
| NRW | Rolle nur am Hauptdokument, gerichtlicher Dokumenttyp, Anlagen neutral fortlaufend | `K_Schriftsatz_mit_Antraegen.pdf` und `Anlage_01.pdf` |
| Bund | ERVB-Grenze maximal 90 Zeichen einschließlich Endung; das strengere ASCII-Profil bleibt als Kanzleistandard zulässig | `01_Anlage_K1_Kaufvertrag.pdf` |

Das Bundesrecht erlaubt in Dateinamen mehr Zeichen als das strenge Gerichtssicher-Profil. Bezeichne das ASCII-Profil deshalb als vorsorglichen Kanzleistandard, nicht als bundesrechtliches Verbot von Umlauten.

## 7. Technischer Preflight

Prüfe für jede PDF:

1. Datei öffnet ohne Kennwort und ohne Reparaturmeldung.
2. Seitenzahl und Reihenfolge stimmen.
3. Text ist lesbar; bei Scan liegt eine brauchbare OCR-Ebene vor oder das Fehlen ist begründet.
4. Keine eingebetteten Dateien, aktiven Inhalte, Skripte oder unerwarteten Formulare.
5. Dateiname entspricht dem gewählten Profil.
6. Stempel ist auf jeder Anlagenseite sichtbar.
7. Hashwert und Dateigröße sind im Versandmanifest erfasst.
8. Gesamtpaket bleibt innerhalb der aktuellen ERVB-Grenzen. Nach ERVB 2025 sind höchstens 1000 Dateien und insgesamt 200 MB je Nachricht vorgesehen.

Sind mehrere Nachrichten nötig, nummeriere sie als `Teil 1 von 3` und liste in jeder Nachricht den Anlagenbereich. Trenne keine mehrseitige Anlage zwischen zwei Nachrichten.

Eine EGVP-Nachricht darf nur ein Verfahren betreffen. Hauptdokument und Anlagen werden als einzelne PDF-Dateien beigefügt; ein ZIP-Archiv ist keine zulässige Versandfassung. Verwende weder zusätzlichen Kennwortschutz noch eine gesonderte Dateiverschlüsselung oder eingeschränkte Leserechte. Prüfe im Versanddialog außerdem Empfänger, Aktenzeichen, Dokumentart und die von der Sendeanwendung erzeugten Strukturdaten.

## 8. Formwirksamkeit und Signaturweg

### 8.1 Zwei Wege

Ein formbedürftiges elektronisches Hauptdokument wird entweder

1. mit einer qualifizierten elektronischen Signatur der verantwortenden Person versehen oder
2. von der verantwortenden Person einfach signiert und persönlich über deren sicheren Übermittlungsweg versandt.

Anlagen benötigen nach ZPO Paragraf 130a Absatz 3 keine eigene Signatur. Wird das beA durch einen Mitarbeiter bedient, ersetzt das nicht den persönlichen Versand durch den Postfachinhaber; ohne persönlichen Versand ist für das Hauptdokument grundsätzlich die qualifizierte elektronische Signatur erforderlich.

### 8.2 Verifizierte Entscheidungsanker

- BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23: Bei einfacher Signatur müssen verantwortende Person und tatsächlicher Versender über das persönlich zugeordnete Postfach übereinstimmen.
- BGH, Beschluss vom 4. September 2024, IV ZB 31/23: Die Nutzung des Postfachs eines anderen Anwalts durch die verantwortende Prozessbevollmächtigte stellt ohne qualifizierte elektronische Signatur keinen sicheren Übermittlungsweg her.
- BGH, Beschluss vom 27. März 2025, V ZB 27/24: Ein Anwalt kann auch als Beteiligter in eigener Sache zur elektronischen Rechtsmitteleinlegung verpflichtet sein; die private Rolle ist kein verlässlicher Papierweg.
- BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23: Versand durch Mitarbeiter erzeugt keinen sicheren Übermittlungsweg; dann ist die qualifizierte elektronische Signatur unverzichtbar.

## 9. Eingang und Ausgangskontrolle

Der Versand ist erst abgeschlossen, wenn die automatisierte Eingangsbestätigung nach der jeweiligen Verfahrensordnung abgerufen und auf Empfänger, Aktenzeichen, Dateinamen, Anzahl der Anhänge, Zeitstempel und positiven Eingangsstatus geprüft wurde.

- KG, Beschluss vom 22. August 2023, 27 U 40/23: Eingang liegt mit Speicherung auf der für das Gericht bestimmten Empfangseinrichtung vor; eine spätere interne Zuordnung ändert den Eingangszeitpunkt nicht.
- OLG Brandenburg, Beschluss vom 23. August 2022, 12 U 113/22: Die Frist darf erst gelöscht werden, wenn die gerichtliche Eingangsbestätigung `request executed` und den Übermittlungsstatus `erfolgreich` ausweist; bloße Kanzleivermerke genügen nicht.
- BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22: Die Ausgangskontrolle muss den erfolgreichen Eingang und die richtige Übermittlung des fristgebundenen Dokuments erfassen.
- BGH, Beschluss vom 24. April 2025, III ZB 12/24: Die Eingangsbestätigung muss abgerufen und kontrolliert werden; der organisatorische Zeitpunkt ist frei, solange noch eine ausreichende Reaktionsreserve bleibt.

Speichere Exportnachricht, Prüfvermerk, Eingangsbestätigung und endgültige Versanddateien gemeinsam und unveränderbar in der Mandatsakte.

## 10. Technische Störung und ungeeignetes Dokument

Trenne strikt:

1. ZPO Paragraf 130a Absatz 6 betrifft ein bereits eingereichtes, für die Bearbeitung ungeeignetes elektronisches Dokument. Nach gerichtlichem Hinweis kann die frühere Wirkung durch unverzügliche Nachreichung in geeigneter Form erhalten werden, wenn die inhaltliche Übereinstimmung glaubhaft gemacht wird.
2. ZPO Paragraf 130d Sätze 2 bis 4 betreffen die vorübergehende technische Unmöglichkeit der elektronischen Übermittlung und die Ersatzeinreichung nach allgemeinen Vorschriften.

Für eine Ersatzeinreichung erstelle eine geschlossene Minutenchronologie mit Fehlermeldung, betroffener Infrastruktur, Versandversuchen, Störungsquelle, Ersatzweg und Belegen.

- BGH, Beschluss vom 19. Dezember 2024, IX ZB 41/23: Ist die Ersatzeinreichung veranlasst, sind keine fortlaufenden neuen elektronischen Versuche bis zu ihrem Vollzug erforderlich; eine zuverlässige veröffentlichte Serverstörung kann die Glaubhaftmachung tragen.
- BGH, Beschluss vom 25. Februar 2025, VI ZB 19/24: Die Darstellung muss technisch, vorübergehend und aus sich heraus verständlich sein; sie muss Bedienungs- oder persönliche Gründe als Ursache nachvollziehbar zurückdrängen.
- OLG Brandenburg, Urteil vom 28. April 2023, 11 U 244/22: Eine pauschale Störungsmitteilung und ein nicht aussagekräftiger Bildschirmabzug belegen weder Dauer noch Umfang der Störung; die Nachweise sind unverzüglich zu sichern und vorzulegen.
- OLG Hamm, Beschluss vom 25. März 2022, 25 U 70/21: Fehlende einsatzbereite Zugangsmittel sprechen gegen eine nur vorübergehende technische Störung; jedenfalls muss die Glaubhaftmachung bei der Ersatzeinreichung oder unverzüglich danach erfolgen.
- LAG Berlin-Brandenburg, Beschluss vom 23. Dezember 2024, 5 Sa 982/24: Die Formel `wg. beA-Störung` genügt nicht; eine mehr als einwöchige Verzögerung der Glaubhaftmachung ist regelmäßig nicht unverzüglich.
- LG Hagen, Urteil vom 15. Oktober 2024, 4 O 209/24: Eine ohne die Voraussetzungen der Ersatzeinreichung auf Papier erhobene Klage ist unwirksam und wird nicht beliebig später durch elektronische Nachreichung geheilt.

## 11. Auslieferung

Liefere diese Ordnerstruktur:

```text
versandfertig/
  00_..._Schriftsatz_....pdf
  01_..._AnlageK1_....pdf
  02_..._AnlageK2_....pdf
intern/
  Anlagenverzeichnis.md
  Versandmanifest.csv
  Preflight-Bericht.md
  Freigabevermerk.md
  Eingangskontrolle.md
```

Der interne Ordner wird nicht mitgesendet, sofern sein Inhalt nicht ausdrücklich Teil der Einreichung sein soll.

## 12. Freigabeampel

### 12.1 Rot

- Frist, Gericht oder Übermittlungsweg ungeklärt.
- Hauptdokument nicht final oder nicht formwirksam signierbar.
- Anlage fehlt, ist unlesbar, verschlüsselt oder widerspricht dem Schriftsatz.
- Nummernkreis kollidiert mit bereits eingereichten Anlagen.
- Eingebettete Datei, aktiver Inhalt oder nicht erklärter Formfehler.

### 12.2 Gelb

- OCR fehlt bei lesbarem Scan.
- Lokale Namenskonvention ist nicht auffindbar; Gerichtssicher-Profil wird dokumentiert verwendet.
- PDF/A wurde nicht technisch validiert.

### 12.3 Grün

Grün erst, wenn Anwalt, Schriftsatzfassung, Anlagenstand, Signaturweg, Empfänger, Frist und Eingangskontrolle feststehen. Gib dann einen ausformulierten Freigabevermerk aus, aber löse keinen Versand aus.

## 13. Quellen

Nutze die amtlich verlinkte und nach Themen geordnete Referenz unter `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md`. Lokale Gerichtshinweise sind Organisationshilfen und dürfen gesetzliche Formvorschriften nicht ersetzen.
