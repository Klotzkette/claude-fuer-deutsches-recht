---
name: 01-sap-akte-importieren
description: "SAP-Start bei sauberem SAP-Statusauszug, FBL5N, Mietkonto, Vertragsnummer, Saldo oder neuem SAP-Stand zu laufender Akte. Stammdaten, Delta, Herkunftssystem und Rückexportbedarf erfassen. Bei neuem Ordner oder gemischtem Upload zuerst Skill 33. Output strukturierte Akte."
---

# SAP-Akte importieren

## Zweck und Anwendungsfall

Startskill bei sauber erkennbarem SAP-Statusauszug, FBL5N, Mietkonto, Vertragsnummer oder Saldo: aus dem grafisch unübersichtlichen, inhaltlich aber vollständigen SAP-PDF-Statusauszug eine strukturierte, klagefähige Akte herstellen. Bei gemischtem Upload-Bundle, Scan, E-Mail-Ordner oder unklaren Dateien führt Skill `33-dokumentenmix-ocr-sichten`; bei technischer Normalisierung, Mapping, Rückexport oder MCP-Planung führt Skill `34-sap-excel-pdf-normalisieren`.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- SAP-PDF-Statusauszug des Mietverhältnisses.
- Soweit vorhanden: Mietkonto-Auszug (FBL5N) und Stammdaten aus SAP DMS.
- Alternativ oder zusätzlich: Export aus DocuWeb, DATEV-Dokumentenablage, RA-MICRO E-Akte, DocuWare-ähnlichem DMS, Netzlaufwerk oder E-Mail-Aktenordner.
- Soweit bekannt: Zielsystem für Rückexport oder Weiterverarbeitung, zum Beispiel DMS, Datenbank, MCP-Server, Middleware, XML-Import oder manueller Dateiimport.
- Hinweis auf bekannte Korrektur- oder Storno-Buchungen.
- Bei laufender Akte: bisherige strukturierte SAP-Tabelle, Akten-ID und letzter SAP-Stichtag.

## Ablauf / Checkliste

1. Pflichtfelder aus dem Statusauszug übernehmen:

| Feld | SAP-Bezeichnung |
|---|---|
| Objektnummer | OBJ-Nr. |
| Mieternummer | Debitor |
| Vertragsbeginn | Mietbeginn lt. Vertrag |
| Nettokaltmiete | Grundmiete |
| Betriebskostenvorauszahlung | BK-VZ |
| Heizkostenvorauszahlung | HK-VZ |
| Bruttowarmmiete | Summe |
| Sollstellung | Forderungen |
| Ist-Zahlung | Zahlungen |
| Saldo | Offene Posten |

2. Vorrangregel setzen: sauberer SAP-Input bleibt in Skill 01; gemischte oder unklare Dateien gehen an Skill 33; technische Export-/Import-/Mappingfragen gehen an Skill 34; operative Rückfragen an Hausverwaltung, Buchhaltung oder IT gehen an Skill 45.
3. Stammdaten auf Konsistenz prüfen.
4. Saldo auf Plausibilität prüfen.
5. Bei Bedarf Korrekturlauf in SAP anstossen.
6. Quelle je Wert festhalten: Datei, Seite, Tabellenzeile oder Screenshot.
7. Abweichungen zwischen SAP-Status, Mietkonto und Vertrag als Konflikt ausweisen.
8. Ampel setzen: grün vollständig, gelb klärbar, rot nicht klagereif.
9. Herkunftssystem erfassen: SAP, DocuWeb, DATEV, RA-MICRO, anderes DMS oder manuelles Upload-Bundle.
10. Fremd-Aktenzeichen, Dokument-ID, Register, Exportdatum und Dateipfad nie überschreiben, sondern als technische Herkunftsspur mitführen.
11. Zielsystem und Rückexportbedarf abfragen: Soll nur gelesen, ein Register vorbereitet, ein Importpaket gebaut oder eine Frist zurückgeschrieben werden?
12. Für Rückexport in elektronische Akten neutrale Pakete vorbereiten: `fallakte.json` für strukturierte Daten, `dms-register.csv` für Dokumentregister und bei Legacy-Bedarf `fallakte.xml` als flache UTF-8-Variante.
13. Wenn ein MCP- oder Kontext-Gateway geplant ist, nur ein `mcp-context-manifest.json` als Planungshilfe ausgeben: Ressourcen, mögliche Werkzeuge, Prompts, Rechte und Schreibsperren. Keine API behaupten, die nicht belegt ist.
14. Bei unbekannten Pflichtfeldern den Rückfrageblock aus `references/schnittstellenprofile.md` verwenden und die Schnittstellenampel gelb setzen.
15. Nach Vollintake immer an Skill `06-fallziel-renofa-triage` übergeben, bevor ein Fachpfad startet. Bei bloßer Delta-Fortschreibung nur dann neu triagieren, wenn Saldo, Frist, Einwendung, Titelstatus oder Rollengrenze den bisherigen Pfad ändern; sonst den ereignisbezogenen Folgeskill wählen.
16. Bei einem neuen SAP-Stand zur laufenden Akte Alt- und Neudaten feldweise vergleichen; geänderte Buchung, neuen Saldo, neue Quelle und überholte Bewertung als Delta ausweisen.
17. Akten-ID und unveränderte Stammdaten beibehalten. Nur bei tragendem Konflikt oder fehlendem Vorzustand zurück zu Skill `33` und zum Vollintake.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für technische Übergabeformate gilt `references/schnittstellenprofile.md`.

## Ausgabeformat

Strukturierte Tabelle mit Feld, Wert, Quelle, Sicherheit, Konflikt und Nacharbeit. Bei Fortschreibung zusätzlich Änderungskarte mit Stichtag alt/neu, geändertem Saldo, neuen Buchungen und überholten Bewertungen. Bei fehlenden Feldern Eintrag UNVOLLSTÄNDIG und konkrete Rückfrage an Buchhaltung, Hausverwaltung, DMS-Administration oder IT. Zusätzlich eine Schnittstellenzeile mit Herkunftssystem, Fremd-ID, Zielregister, Zielsystem, Rückexportwunsch, Exportformat und Ampel. Die Tabelle bleibt tabellarisch; begleitende Bewertungen und Aktenvermerke werden in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Statusauszug mit fehlender Wohnflächenangabe: Die Akte wird mit gelber Ampel angelegt, das Pflichtfeld als UNVOLLSTÄNDIG markiert und eine Rückfrage an die Hausverwaltung formuliert.
- Saldo weicht vom Mietkonto ab: Der Konflikt wird ausgewiesen und die Ampel auf rot gesetzt, bis die Buchungslogik geklärt ist.
