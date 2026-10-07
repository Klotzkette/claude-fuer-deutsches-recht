---
name: 33-dokumentenmix-ocr-sichten
description: "Verbindlicher Default-Start für neuen Fall, Projektordner, Aktenordner, Upload-Bundle und gemischten Neuzugang. Aktiviert bei kurzen Aufträgen wie neuer Fall, Ordner prüfen oder Akte fertig machen. Fragt nie nach einer Skillauswahl, sichert zuerst Fristen, zeigt die einheitliche Sofortkarte und arbeitet danach automatisch in priorisierten Stapeln bis zu Startkarte oder Änderungskarte weiter."
---

# Dokumentenmix und OCR-Intake

## Zweck und Anwendungsfall

Dieser Skill ist der verbindliche Default-Start, wenn der Nutzer nur einen Ordner bereitstellt, "neuer Fall", "hier ist der Ordner", "mach die Akte fertig" sagt oder den universellen Auftrag verwendet: `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.` Er startet auch bei gemischtem Export aus SAP, DMS, E-Mail, Scan, Foto, PDF, Excel, XML, JSON, Datenbankauszug oder handschriftlicher Korrespondenz. Kommen zu einer bereits strukturierten Akte nur neue Unterlagen, arbeitet er im Delta-Modus und bewahrt den bisherigen Aktenstand. Bei sauberem SAP-Statusauszug führt Skill 01; bei technischer Normalisierung, Mapping, Rückexport oder MCP-Planung führt Skill 34.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Dateiordner oder Upload-Bundle mit beliebigen Dokumenttypen.
- Export aus SAP DMS, DocuWeb, DATEV-Dokumentenablage, RA-MICRO E-Akte, DocuWare-ähnlichem DMS oder Netzlaufwerk.
- Datenbank-, BI-, XML-, JSON- oder CSV-Export mit Feldnamen und Stichtag, soweit vorhanden.
- Kurzer Auftrag der Rechtsabteilung.
- Falls vorhanden: SAP-Objekt, Mietvertragsnummer, Mietername, Objektadresse.
- Bei laufender Akte: bisherige Startkarte, Akten-ID, letzter Stichtag, Chronologie und nur die neu eingegangenen Unterlagen.

## Ablauf / Checkliste

1. Modus bestimmen: ohne belastbaren Aktenstand Vollintake; mit Akten-ID, Startkarte oder Chronologie und nur neuen Unterlagen Delta-Fortschreibung.
2. Sofortscan über den gesamten sichtbaren Bestand durchführen, bevor einzelne Dokumente vertieft werden: Dateinamen, Dokumenttypen, Gerichts- und Zustelldokumente, erkennbare Fristdaten, Zahlungen, Kündigungen sowie beschädigte oder unlesbare Dateien erfassen. Eine Frist darf nicht deshalb übersehen werden, weil ihr Dokument in einem späteren Stapel liegt.
3. Unmittelbar die einheitliche Sofortkarte ausgeben: Modus, Akten-ID/Stichtag, erkannte Fallart, früheste mögliche Frist mit Quelle und Rechenstatus, Ampel mit Grund, Zahl der sichtbaren und bereits lesbaren Dateien, höchstens drei Kernlücken sowie Feld `Jetzt` mit genau einer Arbeitsaktion in Klartext. Interne Skillnummern gehören nicht in die Nutzerentscheidung.
4. Nach der Sofortkarte ohne erneute Aufforderung weiterarbeiten, solange kein roter Stopp vorliegt. Dateien inventarisieren: Dateiname, Typ, Datum, mutmaßlicher Inhalt, Lesbarkeit.
5. Im Delta-Modus Akten-ID und letzten Stichtag übernehmen; nur Neuzugang prüfen und gegen den bisherigen Stand vergleichen.
6. Im Delta-Modus geänderten Saldo, neue Frist, neue Einwendung, neuen Beleg und überholte Annahme markieren. Frühere Entwürfe nie still überschreiben.
7. Große Uploads nach dem Sofortscan in priorisierten Stapeln vertiefen: zuerst Gericht und Zustellung, dann Zahlung und Konto, danach Kündigung und Vertrag, anschließend Korrespondenz und übrige Belege. Ein Stapel umfasst höchstens 20 Dateien oder 30 PDF-Seiten, je nachdem, welche Grenze zuerst erreicht ist. Bei einem neuen roten Risiko den Stapel sofort beenden.
8. Nach jedem Stapel eine Fortsetzungsmarke ausgeben: Akten-ID, Stichtag, verarbeitet/offen, letzte Quelle mit Seite oder Hash, früheste mögliche Frist, offene rote/gelbe Punkte und nächster Stapel. Diese Angaben sind der Wiederaufnahmepunkt nach Unterbrechung oder Kontextwechsel.
9. Bei Wiederaufnahme Quelle und Version der Fortsetzungsmarke abgleichen und ab der letzten bestätigten Datei oder Seite weiterarbeiten. Unveränderte Dokumente, Roh-OCR und Tabellen nicht erneut lesen oder vollständig ausgeben. Bei Versionsabweichung nur das betroffene Dokument neu prüfen und gelb markieren.
10. OCR-Bedarf markieren: Scan, Foto, Handschrift, schlechter PDF-Export. OCR-Probleme blockieren nicht die Auswertung der lesbaren Unterlagen. Nach jedem OCR-Fehler mit dem nächsten lesbaren Dokument fortfahren; Fehlerdatei und Seite bleiben in der Lückenliste.
11. Dokumenttyp klassifizieren: SAP-Stammdaten, Mietvertrag, Konto, Korrespondenz, Beleg, gerichtliches Schreiben, Fristdokument.
12. Beweiswert einschätzen: Original, Kopie, Screenshot, E-Mail, Parteivortrag, ungesicherte Notiz.
13. Fristen und Zustellhinweise sofort herausziehen. Ein errechnetes Datum stets mit Auslöser, Quelle, Rechenweg und Sicherheitsstatus ausgeben.
14. Lückenliste für fehlende Pflichtdokumente erstellen.
15. Dubletten, widersprüchliche Fassungen und die mutmaßlich jüngste Version kennzeichnen.
16. Personenbezogene und besonders sensible Daten nur aufnehmen, wenn Zweck und Verfahren das erfordern.
17. Technische Metadaten sichern: Fremd-Aktenzeichen, Dokument-ID, Register, Exportdatum, Dateipfad, Dateiformat, Seitenzahl, Prüfsumme falls vorhanden.
18. Zielsystem-Profil setzen: DocuWeb/DMS mit Register- und Webservice-Logik, DATEV mit Ordner-/Register-Ablage, RA-MICRO mit E-Akte/Dokumentenkennzeichen oder neutraler DMS-Import.
19. Keine automatische Importfähigkeit behaupten. Wenn Feldnamen des Zielsystems fehlen, Mapping-Tabelle ausgeben und den IT- oder DMS-Verantwortlichen als Klärungspunkt benennen.
20. Bei Datenbank- oder XML-Exporten Primärschlüssel, Tabellen-/Elementnamen, Stichtag, Exportfilter und Zeichensatz sichern. Wenn diese Angaben fehlen, nicht inhaltlich raten, sondern Rückfragen ausgeben.
21. Wenn ein MCP-Anschluss gewünscht ist, mögliche Resources markieren: Aktenkopf, Mietkonto, Dokumentregister, Fristenliste, Belegmatrix und freigegebene Vorlagen. Schreibende Tools nur als Vorschlag mit Rechteprüfung kennzeichnen.
22. Autostart abschließen: Nach der Sofortkarte ohne Aufforderung `weiter` fortfahren. Beim Vollintake Startkarte, bei Fortschreibung Änderungskarte mit Stichtag alt/neu, Neuzugang, geänderten Werten, überholten Annahmen, Sofortfrist und genau einer nächsten Arbeitsaktion in Klartext ausgeben. Nur blockierende Fragen stellen, deren Antwort die sofortige Frist-, Rollen- oder Maßnahmenentscheidung ändert; andere Unsicherheiten als gelbe Lücke führen.
23. Nächsten Skill intern festlegen: sauberer SAP-Teil an Skill 01, technisches Mapping an Skill 34, operative Rückfrage an Skill 45, fachliche Triage nach vollständigem Inventar an Skill 06; neue Gerichtspost direkt an Skill 37 oder 42. Dem Nutzer nur den verständlichen Arbeitsnamen und das erwartete Ergebnis zeigen. Bei mehreren Ereignissen führt die nächste harte Frist; übrige Aufgaben folgen als geordnete Warteschlange.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert.

Juristische Wertungen nur mit Normanker und verifizierten Quellen. OCR-Unsicherheiten und technische Mappingunsicherheiten offen markieren. Für Schnittstellenprofile `references/schnittstellenprofile.md` heranziehen.

## Ausgabeformat

Nach der ersten Karte führt das konkrete Arbeitsergebnis: bei Zahlung der neue Rest, bei Beleglücke die adressierte Anfrage, bei Gerichtspost die Frist und der Prozessentwurf. Vollregister intern fortschreiben und nicht bei jedem Stapel erneut ausgeben. Ein roter Pflichtbeleg sperrt nur die davon abhängige Maßnahme; unabhängige lesbare Teile und Fristsicherung weiterbearbeiten. Ein Dateinamen-Scan zählt nicht als gelesene Akte. Die Fortschrittsangabe bezieht sich auf tatsächlich geprüfte Dateien beziehungsweise Seiten.

Die erste Ausgabe ist eine Sofortkarte, keine Volltabelle. Sie enthält nur Modus, Akten-ID/Stichtag, Fallart, früheste mögliche Frist samt Quelle und Rechenstatus, Ampel mit Grund, Dateistand als gelesen/gesamt, höchstens drei Kernlücken und Feld `Jetzt` mit genau einer Arbeitsaktion in Klartext. Danach folgen beim Vollintake die Startkarte und bei laufender Akte die Änderungskarte. Sichtbare Tabellen haben höchstens sieben Spalten und werden bei zusätzlichem Technikbedarf geteilt:

| Datei | Typ/Datum | Kerninhalt | Beweiswert | Lesbarkeit | Frist | Status |
|---|---|---|---|---|---|---|
| [Datei] | [Typ/Datum] | [ein Satz] | [Wert] | [OCR] | [Datum/Quelle] | [bereit/offen] |

Nur bei Schnittstellenbedarf folgt ein getrenntes Technikregister:

| Datei/Fremd-ID | Quelle/Pfad | Version/Hash | Format/Seiten | Ziel/Register | Rückexport | Mappingstatus |
|---|---|---|---|---|---|---|
| [ID] | [System/Pfad] | [Version] | [Format] | [Ziel] | [ja/nein] | [geprüft/offen] |

Datenschutz- oder Konflikthinweise stehen als kurze Warnzeile direkt unter dem betroffenen Eintrag. Nach jedem Stapel folgt die Fortsetzungsmarke. Die Änderungskarte trennt unveränderten Kernstand, Delta und überholte Annahmen. Zusätzlich bei Bedarf: Mapping-Rückfragen, MCP-Resource-Liste und Hinweis auf `fallakte.json`, `dms-register.csv` oder `fallakte.xml`. Maschinenlesbare Exporte dürfen alle technischen Felder enthalten; die Nutzeransicht bleibt kompakt. Freitext wird vollständig ausformuliert; keine Stichwortskelette.

## Beispiele

- PDF-Scan Kündigung unleserlich: OCR-Warnung, Zustellung nachfordern.
- Foto handschriftlicher Mieterbrief: Einwendungen extrahieren und in Skill `43-mieterverein-anwalt-korrespondenz` übergeben.
- Zu einer laufenden Zahlungsklage gehen Teilzahlung und gerichtliche Verfügung ein: Änderungskarte aktualisiert Saldo und Frist, entwertet den alten Replikstand und führt zu Skill `37-klageerwiderung-auswerten`.
