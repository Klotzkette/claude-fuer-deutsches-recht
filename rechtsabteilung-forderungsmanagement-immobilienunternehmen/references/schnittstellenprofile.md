# Schnittstellenprofile für E-Akte, DMS und Legacy-Systeme

Diese Referenz beschreibt, wie das Plugin Daten aus heterogenen Fachsystemen übernimmt und wieder übergabefähig macht. Sie ist kein technischer API-Vertrag. Sie ist ein Arbeitsstandard für Renofas, Rechtsfachwirte, DMS-Administration, IT und Fachkoordination, damit aus unstrukturierten Exporten ein prüfbares Übergabepaket wird.

## 1. Grundsatz

1. Originaldateien bleiben unverändert.
2. Jedes erkannte Datum, jeder Betrag und jede Frist erhält eine Quelle.
3. Technische Herkunftsdaten werden nicht überschrieben: Herkunftssystem, Exportdatum, Fremd-Aktenzeichen, Dokument-ID, Register, Dateipfad, Dateiname, Hashwert und Bearbeitungsstand bleiben erhalten, soweit sie vorliegen.
4. Importfähigkeit wird erst grün markiert, wenn Zielsystem, Pflichtfelder, Rechte, Dateitypen, Feldlängen, Zeichensatz, Dublettenlogik und Importweg geklärt sind.
5. Wenn ein Zielsystem unbekannt ist, wird ein neutrales Paket erstellt und die offenen IT-Fragen werden als Rückfrageblock ausgegeben.

## 2. Eingangsprofile

| Profil | Typische Quelle | Mindestprüfung |
|---|---|---|
| SAP RE-FX / FI-CA | Statusauszug, FBL5N, Objekt-/Vertragsdaten | Vertragsnummer, Debitor, Objekt, Soll/Ist, Buchungsdatum, Wertstellung, Saldo |
| SAP DMS | Vertragsakte, Mahnungen, Kündigungen, Belege | Dokument-ID, Ablagepfad, Version, Register, Exportdatum |
| DocuWeb / DocuWare-artiges DMS | Dokumentregister, PDF-Export, Metadatenliste | Register, Dokumenttyp, Eingangsdatum, Dateiname, Fristbezug |
| DATEV-Dokumentenablage | Ordnerstruktur, Dokumentkorb, PDF/CSV-Export | Zielordner, Belegtyp, Datum, Aktenzeichen, Zugriffsrechte |
| RA-MICRO E-Akte | Aktenexport, Dokumentenkennzeichen, Fristen | Aktennummer, Dokumentenkennzeichen, Beteiligte, Frist, Schriftsatzbezug |
| Netzlaufwerk / E-Mail-Bundle | ZIP, Ordner, EML, MSG, PDF, Scan, Foto | Dateiname, Absender, Eingangsdatum, Lesbarkeit, Dubletten |
| Datenbank- oder BI-Export | CSV, XLSX, JSON, XML, SQL-Auszug | Spaltenbedeutung, Datentyp, Primärschlüssel, Exportfilter, Stichtag |

## 3. Neutrale Ausgabeformate

| Format | Einsatz | Pflichtinhalt |
|---|---|---|
| `fallakte.json` | strukturierte Fallakte für Automatisierung, MCP-Server, DMS-Importvorbereitung oder IT-Übergabe | Aktenkopf, Mietverhältnis, Parteien, Forderungen, Zahlungen, Fristen, Dokumente, Beweise, Risiken, nächste Schritte |
| `dms-register.csv` | Dokumentregister für DocuWeb, DATEV, RA-MICRO, SAP DMS oder neutrale E-Akte | Datei, Zielregister, Dokumenttyp, Datum, Absender, Empfänger, Aktenzeichen, Vertragsnummer, Betrag, Frist, Datenschutzklasse, Quelle, Bemerkung |
| `fallakte.xml` | Legacy-Systeme mit XML-Import oder Middleware | gleiche Inhalte wie `fallakte.json`, aber mit flacher, gut lesbarer Elementstruktur und UTF-8 |
| `schnittstellenauftrag.md` | Rückfrage- und Umsetzungsauftrag an IT oder DMS-Administration | Zielsystem, Mappingtabelle, offene Pflichtfelder, Rechte, Testimport, Rückexport, Verantwortliche, Frist |
| `mcp-context-manifest.json` | Vorbereitung für einen MCP-Server oder ein anderes Kontext-Gateway | Resources, Tools, Prompts, Rechte, erlaubte Aktionen, Schreibsperren, Protokollierung |

## 4. Kernschema für `fallakte.json`

Die Schlüssel werden stabil gehalten und deutsch benannt, damit Fachabteilung und IT dieselbe Sprache sprechen:

```json
{
  "aktenkopf": {
    "fall_id": "",
    "herkunftssystem": "",
    "fremd_aktenzeichen": "",
    "exportdatum": "",
    "bearbeitungsampel": ""
  },
  "mietverhaeltnis": {
    "objekt": "",
    "vertragsnummer": "",
    "mietbeginn": "",
    "vermieterin": "",
    "mieter": []
  },
  "forderungen": [],
  "zahlungen": [],
  "fristen": [],
  "dokumente": [],
  "beweise": [],
  "risiken": [],
  "naechste_schritte": []
}
```

## 5. Kernschema für `dms-register.csv`

Semikolon-CSV, UTF-8, eine Dokumentzeile je Datei:

```csv
datei;zielregister;dokumenttyp;datum;absender;empfaenger;aktenzeichen;vertragsnummer;betrag;frist;datenschutzklasse;quelle;bemerkung
```

Wenn ein Zielsystem andere Feldnamen verlangt, wird keine Importfähigkeit behauptet. Stattdessen wird eine Mappingtabelle erzeugt:

| Plugin-Feld | Zielsystem-Feld | Pflicht? | Beispiel | Klärung |
|---|---|---|---|---|
| vertragsnummer | [offen] | ja | MV-104872-LA | Feldname im Zielsystem bestätigen |

## 6. MCP-Anschluss

MCP wird hier als Andockmuster verstanden: Ein System kann Ressourcen bereitstellen, Werkzeuge anbieten und Prompts als wiederholbare Arbeitsabläufe freigeben. Das Plugin baut keinen MCP-Server. Es liefert aber eine sauber strukturierte Vorlage, aus der IT oder Plattformteam einen Server oder ein Gateway ableiten können.

| MCP-Baustein | Immobilien-Forderungsmanagement | Beispiel |
|---|---|---|
| Resources | lesbare Kontextquellen ohne Seiteneffekt | Akte, Mietkonto, Dokumentregister, BGH-Anker, Fristenliste |
| Tools | kontrollierte Aktionen mit Berechtigung und Protokoll | Dokument abrufen, Zahlungsliste lesen, DMS-Register schreiben, Frist anlegen |
| Prompts | wiederverwendbare Arbeitsabläufe | Intake, Zahlungsklage, Räumung, Mieterhöhung, Kostenfestsetzung |

Arbeitsregel: Lesen ist leichter als Schreiben. Schreibende Tools bleiben gelb oder rot, bis Rechte, Freigabe, Protokollierung, Rückrollbarkeit und Testsystem geklärt sind.

## 7. Rückfragen an IT und DMS-Administration

1. Welches Zielsystem soll befüllt werden?
2. Gibt es einen Dateiimport, Webservice, MCP-Server, Middleware-Job oder nur manuelle Ablage?
3. Welche Pflichtfelder müssen je Dokument gesetzt werden?
4. Welche Feldlängen, Zeichensätze und Datumsformate gelten?
5. Welche Dateitypen sind erlaubt?
6. Wie werden Dubletten erkannt?
7. Wie werden Fristen übernommen oder bewusst nicht übernommen?
8. Welche Rollen dürfen lesen, importieren, exportieren und löschen?
9. Gibt es ein Testsystem und einen Testimport mit Rückmeldung?
10. Welche Protokolle braucht Revision, Datenschutz oder interne Kontrolle?

## 8. Ampellogik

| Ampel | Bedeutung | Nächster Schritt |
|---|---|---|
| Grün | Mapping, Rechte, Pflichtfelder und Testimport sind geprüft | Übergabepaket erzeugen und fachlich freigeben |
| Gelb | Daten sind strukturiert, aber Zielsystemdetails fehlen | `schnittstellenauftrag.md` mit Rückfragen ausgeben |
| Rot | Quelle ist widersprüchlich, Frist unklar oder Schreibzugriff ungeprüft | keine Übergabe; erst Akte oder Rechte klären |

## 9. Minimaler Rückexport

Nach Bearbeitung sollen mindestens diese Ergebnisse zurück in die E-Akte können:

1. `fallakte.json` als strukturierter Bearbeitungsstand.
2. `dms-register.csv` mit neuen Dokumenten und Zielregistern.
3. PDF/Word-Entwurf mit Dokumenttyp und Version.
4. Chronologieeintrag mit Datum, Handlung, Bearbeiterrolle und nächster Frist.
5. Entscheidungsvermerk mit Ampel, Eskalation und Freigabe.
