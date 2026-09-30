---
name: 20-eakte-export-kanzleisoftware
description: "Für E-Akte, DMS, Kanzleisoftware, RA-MICRO, XML, CSV oder JSON. Normalisiert oder exportiert beleggebundene Falldaten mit Schema, Mapping und Datenschutzkontrolle. Kehrt danach zum gespeicherten Fachskill zurück."
---

# E-Akte-Export und Kanzleisoftware

## Zweck und Anwendungsfall

Dieser Skill ist die technische Schnittstelle zwischen Fallbearbeitung und Kanzlei-Infrastruktur. Er exportiert die strukturierte Fallakte in jedes gängige Zielformat — XML, CSV, JSON, Import-Strukturen für RA-MICRO und andere Kanzleisoftware, SAP-basierte Systeme, DMS und Legal-Tech-Plattformen — und normalisiert umgekehrt heterogene Eingänge (PDF, Scan, Excel, Portal-Export) in die Fallakte. Jeder Skill des Plugins kann hierher übergeben; typisch nach Skill 01 (Intake) und Skill 10 (Kanzlei-Übergabepaket). Datenschutz läuft mit: Datenminimierung, Zweckbindung, Weitergabe nur mit Abtretung oder Vollmacht.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort ein Arbeitsprodukt: bei benanntem Zielprofil die Exportdateien selbst samt ausformuliertem Kontrollbericht, sonst einen begründeten Zielprofil-Vorschlag und den Prüfstand der Pflichtfelder mit Status `belegt`, `Lücke` oder `Konflikt`. Eine Export-Prüftabelle wird nur bei mindestens drei Pflichtfeldern oder wiederkehrenden Mappingfeldern verwendet. Jede Lücke nennt Zielfeld, fehlende Quelle und Nachlieferungsauftrag; jeder Konflikt nennt beide Quellwerte und Fundstellen.
Verboten in der ersten Antwort sind Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen; eine Rückfrage unterbleibt, wenn ein vorläufiger Export mit ausgewiesenen Lücken möglich ist. Schema-Werkzeuge und Validatoren sind Beschleuniger: Sind sie nicht verfügbar oder schlagen sie fehl, wird ohne Meldungslärm manuell gegen die Beispieldateien unter `assets/examples/` geprüft; ein Werkzeugfehler blockiert nie Kontrollbericht oder Exportentwurf, wohl aber die grüne Ampel.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Fallakte aus dem Workflow (Stammdaten, Belegmatrix, Chronologie, Fristen, Schadenstabelle).
- Zielsystem und gewünschtes Format (RA-MICRO, SAP-basiert, DMS, Legal-Tech-Plattform, neutral).
- Import- oder Feldvorgaben des Zielsystems, soweit vorhanden; sonst Standardprofile.
- Umgekehrt: Portal-Exporte, Excel-Tabellen, XML/JSON-Dumps zur Normalisierung in die Fallakte.

## Ablauf / Checkliste

1. Zielprofil wählen:

| Profil | Zweck | Ausgabe |
|---|---|---|
| RA-MICRO / Kanzleisoftware | Aktenanlage und Dokumentenimport | `dms-register.csv` plus benannte PDF-Dateien, Feldmapping-Vermerk |
| SAP-basiert / Konzern | Forderungs- und Falldaten strukturiert | `fallakte.xml` flach, UTF-8, plus Mappingtabelle |
| DMS / E-Akte | Register, Metadaten, Aktenimport | `dms-register.csv` mit Registerzuordnung |
| Legal-Tech / Prozessfinanzierer | Streitstoff und Kennzahlen | `fallakte.json` mit Kernkennzahlen |
| Neutral / Systemwechsel | Übergabe an IT | `fallakte.json` plus Dateiordner |

2. Profi- oder Bulk-Modus ausführen, wenn der Nutzer "Profi-Modus", "Schnelllauf", "Bulk", "nur Ergebnis" oder "E-Akte fertig" verlangt. Dann in einem Durchgang `fallakte.json`, `dms-register.csv` und `kontrollbericht.md` erzeugen; `fallakte.xml` kommt bei entsprechendem Zielprofil hinzu. Das Paket behält Schema, Pflichtfelder, Konfliktzeilen, Datenschutzklassen und Hinweise zum Testimport bei; ein unkommentierter Rohdaten-Dump ist unzulässig.
3. Standardformate erzeugen — schnell und ohne Rückfragen, wenn ein Profil benannt ist:
   - `fallakte.json`: UTF-8 nach `assets/schemas/fallakte.schema.json`, `schema_version` 1.0.0, stabile Schlüssel für Stammdaten, Fahrzeug, Kauf, Forderungen, Zahlungen, Fristen, Dokumente, Beweise, Risiken und nächste Schritte.
   - `dms-register.csv`: Semikolon-CSV nach `assets/schemas/dms-register.schema.json`; jede Zeile führt `schema_version`, `dokument_id`, Quelldaten, Datenschutzklasse, SHA-256 und Konfliktstatus. Die verbindliche Spaltenfolge steht in `assets/templates/dms-register-vorlage.csv`.
   - `fallakte.xml`: gleiche Fachinhalte flach als XML, ohne proprietäre Annahmen.
4. Vor Übergabe gegen die mitgelieferten Verträge prüfen. `assets/examples/fallakte-beispiel.json` und `assets/examples/dms-register-beispiel.csv` zeigen die Sollstruktur; `assets/templates/kontrollbericht-vorlage.md` ist vollständig auszufüllen. Schemafehler oder fehlende Pflichtfelder verhindern die grüne Ampel.
5. Feldmapping dokumentieren: Quellfeld, Wert, Zielfeld, Unsicherheit; Datumsformate ISO plus deutsche Anzeigeform; Beträge ohne Rechenverlust.
6. Metadaten mitführen: Fremd-Aktenzeichen, Dokument-ID, Dokumenttyp, Eingangsdatum, Absender, Empfänger, Fristbezug, Datenschutzklasse, Prüfsumme falls vorhanden.
7. Datenschutz erzwingen: Datenminimierung und Zweckbindung (Art. 5, 6 DSGVO), Datenschutzklasse je Dokument, Weitergabe an Legal-Tech oder Finanzierer nur mit wirksamer Abtretung oder Vollmacht; Verstöße als rote Zeile.
8. Normalisierungsrichtung: heterogene Eingänge (Scan, Excel, Portal-Export, XML/JSON-Dump) in die Fallakte mappen; Konflikte zwischen Quellen nicht glätten, sondern als Konfliktzeile ausgeben; Originaldateien nie verändern.
9. Testimport vorschlagen: kleine Probedatei, Rückfragenliste für das Zielsystem (Pflichtfelder, Rechte, Importweg); keine herstellerspezifische API oder Portalanbindung erfinden — offene Punkte als Mapping-Rückfrage.
10. Ampel: grün bei bestandenem Vertragscheck, geprüftem Mapping und Testimport, gelb bei Export ohne Zielsystemklärung, rot bei Schemafehler, Datenschutzverstoß oder Widerspruch in den Quelldaten.
11. beA-Abgrenzung: Dieser Skill erzeugt die dauerhafte Kanzlei-/DMS-Akte, nicht das gerichtliche Versandpaket. Für einen konkreten Schriftsatz übergibt er Originale, Dokument-IDs und SHA-256-Werte an Skill `21-bea-versandfertig-schriftsatz-anlagen`; Skill 21 erzeugt `versand/`, Skill 16 übermittelt und liefert Eingangsbestätigung/Versandvermerk an die E-Akte zurück.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Juristische Aussage, Aktenfundstelle und technisches Exportfeld verlustfrei abbilden, ohne aus Mappingdaten neue Tatsachen zu erzeugen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Jedes anspruchstragende Feld besitzt Quelle, Konfliktstatus, Schemafassung und dokumentiertes Zielsystem-Mapping.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

- **Anker:** Keine Dieselgate-Leitentscheidung einschlägig. Für den Export-Arbeitsschritt trägt keine Dieselgate-Leitentscheidung; maßgeblich sind Art. 5, 6 und 15 DSGVO. Exportiert werden die anspruchstragenden Felder der geprüften Linien: FIN, Kaufpreis, Motorcode, Rückrufstatus, Fristen und Schadensrechnung. **Status:** Hinweis.

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Übergabevermerk zum Export (in den Kontrollbericht einzusetzen):**

1

Übergeben wird die Fallakte [Fallnummer] der Anspruchstellerin [Name] gegen [Name des Herstellers] wegen des Fahrzeugs [Modell] mit der FIN [FIN] im Zielprofil [Zielprofil] mit den Dateien `fallakte.json` (Schema-Version 1.0.0, SHA-256 [Hashwert]) und `dms-register.csv` ([Anzahl] Zeilen, SHA-256 [Hashwert]) [sowie `fallakte.xml`, SHA-256 [Hashwert]].

2

Der Export wurde am [Datum TT.MM.JJJJ] gegen die Schemas unter `assets/schemas/` geprüft; alle Pflichtfelder sind belegt, [Anzahl] Konfliktzeilen sind offen ausgewiesen und nicht geglättet, die Originaldateien blieben unverändert.

3

Datenschutz: Jede Dokumentzeile trägt eine Datenschutzklasse; die Weitergabe erfolgt auf Grundlage der [Vollmacht vom Datum TT.MM.JJJJ / Abtretungsvereinbarung vom Datum TT.MM.JJJJ]. Eine über den Übergabezweck hinausgehende Verarbeitung ist durch Datenminimierung und Zweckbindung nach Art. 5 Abs. 1 DSGVO ausgeschlossen.

4

Offene Punkte: [Rückfragenliste zum Zielsystem, z. B. Pflichtfelder, Rechte, Importweg]. Vor der Vollübernahme wird ein Testimport mit [Anzahl] Dokumenten empfohlen; das Ergebnis ist in diesem Vermerk nachzutragen.

**Baustein 2 — Feldmapping-Ergebnissatz bei sauberer Abbildung:**

Das Quellfeld [Quellfeldname] aus [Quelldatei] wurde mit dem Wert [Wert] verlustfrei auf das Zielfeld [Zielfeldname] abgebildet; Datumswerte werden als [JJJJ-MM-TT] gespeichert und als [TT.MM.JJJJ] angezeigt, Beträge ohne Rundungs- oder Rechenverlust übernommen.

**Baustein 3 — Feldmapping-Ergebnissatz bei Konflikt:**

Für das Zielfeld [Zielfeldname] liegen zwei abweichende Quellwerte vor: [Wert 1] aus [Quelle 1 mit Fundstelle] und [Wert 2] aus [Quelle 2 mit Fundstelle]. Die Abweichung wurde nicht geglättet, sondern als Konfliktzeile mit beiden Werten ausgewiesen; die fachliche Klärung obliegt [zuständige Person oder Skill] bis zum [Datum TT.MM.JJJJ].

**Baustein 4 — Feldmapping-Ergebnissatz bei Lücke:**

Das Pflichtfeld [Zielfeldname] konnte aus keiner vorliegenden Quelle belegt werden; es ist als Lücke markiert und verhindert die grüne Ampel, bis [Dokument oder Person] den Wert nachliefert.

### Export-Prüftabelle

Die Tabelle ist vor jeder Übergabe vollständig durchzugehen; jede rote Zeile sperrt die grüne Ampel.

| Pflichtfeld | Datei | Quelle | Kontrolle |
| --- | --- | --- | --- |
| FIN | `fallakte.json` | Zulassungsbescheinigung, Kaufvertrag | 17 Zeichen, Abgleich beider Quellen; Abweichung ist Konfliktzeile |
| Kaufpreis und Kaufdatum | `fallakte.json` | Kaufvertrag, Rechnung, Kontoauszug | Betrag ohne Rechenverlust, Datum ISO plus deutsche Anzeigeform |
| Motorcode und Abgasnorm | `fallakte.json` | Zulassungsbescheinigung, Werkstattunterlagen, Rückrufschreiben | Gegen Rückrufbezug prüfen; unbelegter Motorcode ist Lücke, nicht Schätzung |
| Rückrufstatus und Rückrufcode | `fallakte.json` | KBA-Schreiben, Herstellerkorrespondenz | Quelle mit Datum erfasst; ohne Beleg keine Statusangabe |
| Fristen mit Fristgrund | `fallakte.json` | Fristenkarte aus dem Workflow | Jede Frist mit Datum, Grund und verantwortlicher Stelle; keine geschätzten Fristen |
| Forderungen und Schadensrechnung | `fallakte.json` | Schadenstabelle aus Skill 08 | Beide Linien getrennt; Rechenwerte gegen die Quelltabelle abgleichen |
| `schema_version` | beide Dateien | Schema unter `assets/schemas/` | Exakt die deklarierte Version; Abweichung ist Schemafehler und damit rot |
| `dokument_id` und SHA-256 | `dms-register.csv` | Originaldatei | Hash gegen die unveränderte Originaldatei gerechnet; Kollisionen und Dubletten ausweisen |
| Datenschutzklasse | `dms-register.csv` | Klassifizierung je Dokument | Jede Zeile klassifiziert; fehlende Klasse oder Weitergabe ohne Vollmacht/Abtretung ist rote Zeile |
| Konfliktstatus | `dms-register.csv` | Normalisierungslauf | Konflikte offen ausgewiesen, nicht aufgelöst; Anzahl stimmt mit dem Kontrollbericht überein |

## Quellenpflicht

Es gilt `references/zitierweise.md`, `references/schnittstellenprofile.md` und der versionierte Vertrag unter `assets/schemas/`. Technische Annahmen über Zielsysteme offenlegen statt erfinden; Datenschutzaussagen mit Normanker (Art. 5, 6, 15 DSGVO). Keine erfundenen Aktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Schema-validierte Exportdateien (`fallakte.json`, `dms-register.csv`, bei Bedarf `fallakte.xml`) plus vollständig ausgefüllter `kontrollbericht.md` mit Versionsstand, Mapping-Vermerk, Konflikten, Datenschutzprüfung, Testimport und Rückfragen; reine Datei-Dumps ohne Vermerk sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Kanzlei will die Akte in RA-MICRO anlegen, Fallakte aus Skill 01 liegt vor. Kernbefund: Zielprofil klar, zwei Pflichtfelder ohne Beleg. Erste Antwort: `dms-register.csv` mit Registerzuordnung und benannten PDF-Dateien plus Übergabevermerk mit zwei Lücken-Sätzen und Testimport-Vorschlag mit fünf Dokumenten.
- Eingang: Prozessfinanzierer braucht Kennzahlen bis zum Nachmittag. Kernbefund: Profi-Modus, alle Kernfelder belegt. Erste Antwort: `fallakte.json` mit Streitwert, Spur, Quote und Risiken plus vollständig ausgefüllter Kontrollbericht in einem Durchgang.
- Eingang: Legal-Tech liefert einen JSON-Dump mit 40 Feldern zur Normalisierung. Kernbefund: drei Feldkonflikte zwischen Dump und Kaufvertrag. Erste Antwort: normalisierte Fallakte mit drei offen ausgewiesenen Konfliktzeilen (Baustein 3) und gesetzter Datenschutzklasse je Dokument.
