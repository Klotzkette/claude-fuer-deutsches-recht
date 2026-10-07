---
name: 45-hausverwaltung-schnittstelle
description: "Leadskill für operative Rückfragen an Hausverwaltung, Objektbetreuung, Buchhaltung, DMS-Administration, IT und Forderungsmanagement. Nutze bei Beleglücke, Zustellung, Mängelstatus, Zahlungsklärung oder Schnittstellenmapping. Output interne Anfrage."
---

# Hausverwaltungsschnittstelle

## Zweck und Anwendungsfall

Dieser Skill macht aus juristischen und technischen Lücken konkrete interne Arbeitsaufträge an die Stellen, die SAP, DMS, Objektwissen, Belege, Zielsysteme oder Import-/Exportwege kennen. Er ist kein Intake-Startskill; er wird geladen, wenn Skill 01, 33, 34, 37, 42 oder 44 eine konkrete Rückfrage an operative Teams erzeugt.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Lückenliste.
- Zielprodukt und Frist.
- Ansprechpartner oder Organisationseinheit.
- Aktenzeichen, Objekt, Mietvertragsnummer und Datenschutzbedarf.
- Zielsystem oder Quellsystem, falls es um DocuWeb, DATEV, RA-MICRO, SAP DMS, Datenbank, XML, MCP-Gateway oder Middleware geht.

## Ablauf / Checkliste

1. Juristische Lücke in operative Rückfrage übersetzen.
2. Dringlichkeit und Frist festlegen.
3. Benötigtes Format angeben: PDF, Excel, Foto, Zeugenname, Zustellprotokoll, Wartungsbericht, Ortsterminvermerk.
4. Datenschutz und Zweckbindung knapp nennen.
5. Antwortfelder so strukturieren, dass sie direkt in Belegmatrix und Chronologie passen.
6. Rückfrage so kurz formulieren, dass operative Teams sie ohne Rechtsdebatte beantworten können.
7. Nachlieferungen mit Aktenzeichen, Objekt, Mietvertragsnummer und Frist verknüpfen.
8. Beweiswert abfragen: Wer hat was wann gesehen, dokumentiert, fotografiert oder versandt? Bei Feuchtigkeit oder Schimmel zusätzlich Originalfotos und Metadaten, Raum- und Oberflächentemperaturen, Luftfeuchte, Geräte- und Kalibrierdaten, Messlücken, Grundriss, Möbelabstände, Bau- und Fensterunterlagen, Terminangebote, Absagen, Sanierungsmaßnahmen und die jeweils eigene Wahrnehmung der Auskunftsperson getrennt anfordern.
9. Widersprüche zwischen SAP, DMS, Hausverwaltung und Objektbetreuung sichtbar machen.
10. Keine Rechtsbewertung von operativen Teams verlangen; nur Tatsachen, Belege und Ansprechpartner abfragen.
11. Bei Schnittstellenfragen den Zielsystemblock ausgeben: Pflichtfelder, Feldnamen, Dateitypen, Rechte, Importweg, Testimport, Dublettenprüfung, Fristenübernahme, Rückexport und Protokollierung.
12. Bei MCP- oder Middleware-Anschluss zwischen Lesen und Schreiben trennen. Lesende Bereitstellung kann gelb vorbereitet werden; schreibende Aktionen bleiben rot, bis Berechtigung, Freigabe und Protokollierung bestätigt sind.
13. Rückfragen so bauen, dass die Antwort direkt in `fallakte.json`, `dms-register.csv`, `fallakte.xml` oder `schnittstellenauftrag.md` übernommen werden kann.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert.

Keine Rechtsberatung an Dritte. Interne Anfrage bleibt sachlich, datenminimiert, beweis- und schnittstellenorientiert. Für technische Rückfragen `references/schnittstellenprofile.md` nutzen.

## Ausgabeformat

Ausformulierter interner Anfrageentwurf mit Betreff, Kontext, konkreten Fragen, benötigten Anlagen, Antwortformat, Beweiswertfeldern, Schnittstellenfeldern, Datenschutztext und Frist.

## Beispiele

- Hausverwaltung soll Mängelmeldungen und Ortstermine liefern.
- Buchhaltung soll Verrechnungslogik einer Teilzahlung klären.
- DMS-Administration soll Zielregister, Pflichtfelder, Importweg und Testimport für ein DocuWeb- oder DATEV-Paket bestätigen.
