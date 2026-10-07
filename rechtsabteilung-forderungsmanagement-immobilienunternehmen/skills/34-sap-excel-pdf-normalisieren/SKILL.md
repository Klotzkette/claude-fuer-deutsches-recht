---
name: 34-sap-excel-pdf-normalisieren
description: "Technischer Anschluss-Skill nach Autostart oder SAP-Intake. Normalisiert SAP, Excel, PDF, DocuWeb, DATEV, RA-MICRO, XML, JSON, Datenbankexport, DMS-Register und MCP-Planung. Kein Fachpfad. Output fallakte.json, dms-register.csv, fallakte.xml und Mapping-Rückfragen."
---

# SAP-, Excel- und PDF-Ausgaben normalisieren

## Zweck und Anwendungsfall

Dieser Skill macht aus technischen Exporten eine bearbeitbare Rechtsakte. Er ist der Leadskill für Normalisierung, Mapping, Rückexport, DocuWeb, DATEV, RA-MICRO, Datenbankexport, DMS-Register, XML, JSON und MCP-/Kontext-Gateway. Er ersetzt nicht die fachliche Triage; nach der Normalisierung führt der Weg zu Skill 06 oder zum passenden Fachskill.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- SAP-Statusauszug, FBL5N, RE-FX-Export oder Excel-Tabelle.
- CSV-, XML-, JSON-, SQL-/BI-Auszug oder sonstiger Datenbankexport mit Feldbeschreibung, soweit vorhanden.
- DocuWeb-, DATEV-, RA-MICRO-, DocuWare- oder sonstiger DMS-Export mit Dokumenten und Metadaten.
- Mietvertrag und Nachträge.
- Korrespondenz oder Belege aus DMS.
- Zielsystem, gewünschter Rückexport, Rechte- oder Importvorgaben, soweit bekannt.

## Ablauf / Checkliste

1. Feldmapping erstellen: SAP-Feld, erkannter Wert, Zielspalte, Unsicherheit.
2. Datumsformate vereinheitlichen auf ISO-Datum und deutsche Anzeigeform.
3. Geldbeträge als EUR-Werte ohne Rechenverlust erfassen.
4. Personen, Objekt und Vertragsdaten eindeutig zusammenführen.
5. Mietkonto chronologisch sortieren und Soll/Ist/Saldo trennen.
6. Ergebnis an Skills `03`, `04` und `05` weitergeben.
7. Jede Zahl mit Quelle, Buchungsdatum, Wertstellung und Import-Sicherheit versehen.
8. Abweichungen zwischen SAP, Excel und PDF nicht glätten, sondern als Konfliktzeile ausgeben.
9. DMS-Metadaten normalisieren: Fremd-Aktenzeichen, Dokument-ID, Register, Dokumenttyp, Erstellungsdatum, Eingangsdatum, Absender, Empfänger, Fristbezug, Datenschutzklasse, Dateipfad und Prüfsumme falls vorhanden.
10. Zielprofile anbieten:

| Profil | Zweck | Ausgabe |
|---|---|---|
| DocuWeb/DMS | Register, Metadaten und Webservice-Import vorbereiten | `dms-register.csv` plus PDF-Dateien |
| DATEV-Dokumentenablage | Ordner-/Registerstruktur einer Papierakte digital nachbilden | `dms-register.csv` mit Zielordnern |
| RA-MICRO E-Akte | E-Akte mit Dokumentenkennzeichen und Aktenbezug vorbereiten | `dms-register.csv` mit DKz-Vorschlag |
| XML/Legacy | Middleware oder Altimport mit flacher Struktur vorbereiten | `fallakte.xml` plus Mappingtabelle |
| MCP/Kontext-Gateway | Ressourcen und erlaubte Werkzeuge planbar machen | `mcp-context-manifest.json` |
| Neutral | Systemwechsel oder Übergabe an IT | `fallakte.json` plus Dateiordner |

11. Standardformate erzeugen, wenn Export verlangt wird:
    - `fallakte.json`: UTF-8, stabile Schlüssel für Stammdaten, Forderungen, Fristen, Dokumente, Beweise, Risiken und nächste Schritte.
    - `dms-register.csv`: Semikolon-CSV mit `datei`, `zielregister`, `dokumenttyp`, `datum`, `absender`, `empfaenger`, `aktenzeichen`, `vertragsnummer`, `betrag`, `frist`, `datenschutzklasse`, `quelle`, `bemerkung`.
    - `fallakte.xml`: gleiche Fachinhalte wie `fallakte.json`, flach und UTF-8, ohne proprietäre Annahmen.
    - `schnittstellenauftrag.md`: Rückfragen, Mapping, Pflichtfelder, Rechte, Testimport und Rückexport.
    - `mcp-context-manifest.json`: geplante Resources, Tools, Prompts, Schreibsperren, Protokollierung und Freigabepunkte.
12. Datenbankexporte nur mit Stichtag, Filter, Primärschlüssel und Feldbedeutung verwenden. Fehlt eine dieser Angaben, die konkrete Rückfrage formulieren.
13. Originaldateien nicht verändern. PDF/A oder durchsuchbares PDF nur als abgeleitete Arbeitskopie ausweisen.
14. Keine herstellerspezifische API erfinden. Wenn DocuWeb, DATEV, RA-MICRO, SAP, ein MCP-Server oder eine Middleware ein anderes Importfeld verlangt, Mapping offenlegen und als IT-Klärung markieren.
15. Ampel setzen: grün bei geprüftem Mapping und Testimport, gelb bei strukturierter Akte ohne Zielsystemklärung, rot bei Widerspruch, Fristunsicherheit oder ungeprüftem Schreibzugriff.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert.

Keine juristischen Schlussfolgerungen ohne Normanker. Datenunsicherheiten nicht glätten, sondern kennzeichnen. Für Schnittstellenprofile, neutrale Formate und MCP-Planung `references/schnittstellenprofile.md` nutzen.

## Ausgabeformat

Normalisierte Fallakte mit Stammdatentabelle, Mietkontotabelle, Vertragsdaten, Belegliste, Konflikttabelle, Lückenliste, `fallakte.json`-Schema, `dms-register.csv`-Schema, optionalem `fallakte.xml`, `mcp-context-manifest.json` und `schnittstellenauftrag.md`. Alle Hinweise werden ausformuliert.

## Beispiele

- FBL5N-PDF mit Zeilenumbrüchen: in Monatszeilen normalisieren.
- Excel mit negativen Habenwerten: Rechenlogik offenlegen, bevor die Forderung beziffert wird.
- DocuWeb-Export ohne Feldbeschreibung: Dokumentregister aus Dateinamen, Ordnern und sichtbaren Metadaten bilden, Importfähigkeit gelb markieren.
- DATEV- oder RA-MICRO-Übergabe: Register, Dokumenttyp und Aktenzeichen ausgeben, aber den tatsächlichen Importpfad nicht behaupten.
- Legacy-XML-Import: flaches `fallakte.xml` und Mapping-Rückfragen erzeugen, bis Zielsystemfelder bestätigt sind.
- MCP-Planung: Akte und Dokumentregister als Resources, schreibende Aktionen nur als gesperrte Tool-Vorschläge mit Rechteprüfung ausgeben.
