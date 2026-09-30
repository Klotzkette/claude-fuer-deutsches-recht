# Schnittstellenprofile für Fahrzeugakte, Kanzlei-DMS und Fremddaten

Diese Referenz beschreibt, wie das Plugin Daten aus heterogenen Quellen übernimmt und wieder übergabefähig macht. Sie ist kein technischer API-Vertrag. Sie ist ein Arbeitsstandard für Diesel-Geschädigte, Kanzleien, Verbraucherschützer, Legal-Tech-Dienste und IT, damit aus unstrukturierten Kaufunterlagen, Finanzierungsdaten und Gutachten ein prüfbares Übergabepaket wird.

## 1. Grundsatz

1. Originaldateien bleiben unverändert.
2. Jedes erkannte Datum, jeder Betrag und jede Frist erhält eine Quelle.
3. Technische Herkunftsdaten werden nicht überschrieben: Herkunftssystem, Exportdatum, Fremd-Aktenzeichen, Dokument-ID, Register, Dateipfad, Dateiname, Hashwert und Bearbeitungsstand bleiben erhalten, soweit sie vorliegen.
4. Importfähigkeit wird erst grün markiert, wenn Zielsystem, Pflichtfelder, Rechte, Dateitypen, Feldlängen, Zeichensatz, Dublettenlogik und Importweg geklärt sind.
5. Wenn ein Zielsystem unbekannt ist, wird ein neutrales Paket erstellt und die offenen IT-Fragen werden als Rückfrageblock ausgegeben.

## 2. Eingangsprofile

| Profil | Typische Quelle | Mindestprüfung |
|---|---|---|
| Kaufunterlagen | Kaufvertrag, Rechnung, verbindliche Bestellung, Fahrzeugschein/Zulassungsbescheinigung Teil I und II | Kaufdatum, Kaufpreis, FIN, Erstzulassung, Kilometerstand bei Kauf, Verkäufer (Händler/privat) |
| Fahrzeug- und Motordaten | COC-Papier, Typgenehmigung, Motorcode, KBA-Rückrufschreiben, Software-Update-Bestätigung | FIN, Typgenehmigungsnummer, Motorkennbuchstabe (EA189/EA288/OM651 usw.), KBA-Aktion, Update-Datum |
| Finanzierung / Leasing | Darlehensvertrag, Leasingvertrag, Kontoauszüge, Widerrufsinformation, Tilgungsplan | Bank/Leasinggeber, verbundenes Geschäft, Anzahlung, Rate, Restwert, Widerrufsbelehrung |
| Kanzlei-/Legal-Tech-Export (RA-MICRO, advoware, Portal) | Aktenexport, Dokumentenkennzeichen, Fristen, Abtretungserklärung | Aktennummer, Beteiligte, Frist, Abtretungs-/Vollmachtsbezug, Prozessfinanzierer |
| Gutachten / Werkstatt | Sachverständigengutachten, Prüfbericht, Werkstattrechnung, Fotos | Gutachter, Datum, Befund zur Abschalteinrichtung, Kilometerstand, Restwert |
| Netzlaufwerk / E-Mail-Bundle | ZIP, Ordner, EML, MSG, PDF, Scan, Foto | Dateiname, Absender, Eingangsdatum, Lesbarkeit, Dubletten |
| Datenbank- oder BI-Export | CSV, XLSX, JSON, XML, SQL-Auszug | Spaltenbedeutung, Datentyp, Primärschlüssel, Exportfilter, Stichtag |

## 3. Neutrale Ausgabeformate

| Format | Einsatz | Pflichtinhalt |
|---|---|---|
| `fallakte.json` | strukturierte Fallakte für Automatisierung, MCP-Server, DMS-Importvorbereitung oder IT-Übergabe | Aktenkopf, Fahrzeug, Kauf, Beteiligte, Ansprüche, Zahlungen, Fristen, Dokumente, Beweise, Risiken, nächste Schritte |
| `dms-register.csv` | Dokumentregister für Kanzlei-DMS, Legal-Tech-Portal, RA-MICRO oder neutrale E-Akte | Datei, Zielregister, Dokumenttyp, Datum, Absender, Empfänger, Aktenzeichen, FIN, Betrag, Frist, Datenschutzklasse, Quelle, Bemerkung |
| `fallakte.xml` | Legacy-Systeme mit XML-Import oder Middleware | gleiche Inhalte wie `fallakte.json`, aber mit flacher, gut lesbarer Elementstruktur und UTF-8 |
| `schnittstellenauftrag.md` | Rückfrage- und Umsetzungsauftrag an IT oder DMS-Administration | Zielsystem, Mappingtabelle, offene Pflichtfelder, Rechte, Testimport, Rückexport, Verantwortliche, Frist |
| `mcp-context-manifest.json` | Vorbereitung für einen MCP-Server oder ein anderes Kontext-Gateway | Resources, Tools, Prompts, Rechte, erlaubte Aktionen, Schreibsperren, Protokollierung |

## 3a. Versionierte Schnittstellenverträge

Die neutrale Übergabe ist ab Schema-Version 1.0.0 nicht nur beschrieben, sondern im Plugin maschinenlesbar gebündelt:

| Datei | Funktion |
|---|---|
| `assets/schemas/fallakte.schema.json` | JSON-Schema 2020-12 für `fallakte.json` mit Pflichtfeldern, Ampeln, Quellen-, Fristen-, Beweis- und Konfliktstatus |
| `assets/schemas/dms-register.schema.json` | JSON-Schema 2020-12 für eine DMS-Registerzeile samt verbindlicher CSV-Spaltenfolge |
| `assets/examples/fallakte-beispiel.json` | vollständig anonymisiertes, schema-valides Beispiel |
| `assets/examples/dms-register-beispiel.csv` | anonymisierte Beispielzeile im verbindlichen Semikolonformat |
| `assets/templates/dms-register-vorlage.csv` | leere Importvorlage mit stabiler Kopfzeile |
| `assets/templates/kontrollbericht-vorlage.md` | Pflichtstruktur für Schema-, Quellen-, Konflikt-, Datenschutz- und Testimportkontrolle |

Jeder Export führt seine `schema_version`. Eine unbekannte Schema-Version, ein fehlendes Pflichtfeld oder eine abweichende Spaltenfolge ist mindestens gelb; vor produktivem Import bleibt die Ampel rot, bis Mapping und Testimport bestätigt sind.

## 4. Kernschema für `fallakte.json`

Die Schlüssel werden stabil gehalten und deutsch benannt, damit Fachabteilung und IT dieselbe Sprache sprechen. Verbindlich ist `assets/schemas/fallakte.schema.json`; die folgende Darstellung zeigt nur den Umschlag:

```json
{
  "schema_version": "1.0.0",
  "aktenkopf": {
    "fall_id": "",
    "herkunftssystem": "",
    "fremd_aktenzeichen": "",
    "exportdatum": "",
    "bearbeitungsampel": "",
    "quellenstand": ""
  },
  "fahrzeug": {
    "fin": "",
    "hersteller": "",
    "modell": "",
    "motorcode": "",
    "erstzulassung": "",
    "typgenehmigung": "",
    "kba_rueckruf": ""
  },
  "kauf": {
    "kaufdatum": "",
    "kaufpreis": "",
    "waehrung": "EUR",
    "verkaeufer": "",
    "kaeufer": [],
    "finanzierung": "",
    "kilometerstand_kauf": ""
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

Semikolon-CSV, UTF-8, eine Dokumentzeile je Datei. Verbindlich sind `assets/schemas/dms-register.schema.json` und die folgende Kopfzeile:

```csv
schema_version;dokument_id;datei;zielregister;dokumenttyp;datum;absender;empfaenger;aktenzeichen;fin;motorcode;betrag;frist;datenschutzklasse;quelle;sha256;konfliktstatus;bemerkung
```

Wenn ein Zielsystem andere Feldnamen verlangt, wird keine Importfähigkeit behauptet. Stattdessen wird eine Mappingtabelle erzeugt:

| Plugin-Feld | Zielsystem-Feld | Pflicht? | Beispiel | Klärung |
|---|---|---|---|---|
| fin | [offen] | ja | WVWZZZ1KZAW000000 | Feldname im Zielsystem bestätigen |

## 6. MCP-Anschluss

MCP wird hier als Andockmuster verstanden: Ein System kann Ressourcen bereitstellen, Werkzeuge anbieten und Prompts als wiederholbare Arbeitsabläufe freigeben. Das Plugin baut keinen MCP-Server. Es liefert aber eine sauber strukturierte Vorlage, aus der IT oder Plattformteam einen Server oder ein Gateway ableiten können.

| MCP-Baustein | Diesel-Schadensersatz | Beispiel |
|---|---|---|
| Resources | lesbare Kontextquellen ohne Seiteneffekt | Fahrzeugakte, Kaufunterlagen, Dokumentregister, BGH-/EuGH-Anker, Verjährungsliste |
| Tools | kontrollierte Aktionen mit Berechtigung und Protokoll | Dokument abrufen, Zahlungsliste lesen, DMS-Register schreiben, Frist anlegen |
| Prompts | wiederverwendbare Arbeitsabläufe | Intake, Anspruchsschreiben, Schadensersatzklage, Replik, Kostenfestsetzung |

Arbeitsregel: Lesen ist leichter als Schreiben. Schreibende Tools bleiben gelb oder rot, bis Rechte, Freigabe, Protokollierung, Rückrollbarkeit und Testsystem geklärt sind.

Wenn Ansprüche an einen Legal-Tech-Dienst oder Prozessfinanzierer abgetreten werden, ist die Abtretungserklärung eine eigene, datenschutzrelevante Ressource. Weitergabe von Fahrzeug- und Finanzierungsdaten an Dritte nur bei belegter Vollmacht oder Abtretung.

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
