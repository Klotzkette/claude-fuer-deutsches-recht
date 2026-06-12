# Megaprompt: status-navigator-step-plan

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 35 Skills des Plugins `status-navigator-step-plan`.

## Inhaltsverzeichnis

1. **excel-reiter-1-ueberblick** — Baut Reiter 1 der Step-Plan-Excel: Ueberblick aller fuer die Durchsetzung erforderlichen Dokumente. Spalten Dokument, Da…
2. **status-navigator-einstieg** — Einstiegs-Skill fuer den Status-Navigator: nimmt einen ungeordneten Dokumentenklumpatsch entgegen und liefert die ersten…
3. **ziel-praezisieren** — Klaert mit dem Auftraggeber das konkrete Ziel des Status-Navigators: Faelligstellung und Vollstreckung, Vollzug einer Ka…
4. **szenario-faelligstellung-vollstreckung** — Anwendungsszenario gescheiterte Finanzierung mit Vorbereitung von Faelligstellung und Vollstreckung. Status-Navigator er…
5. **padlet-spalte-1-ueberblick** — Baut die erste Padlet-Spalte als Pendant zu Reiter 1 der Step-Plan-Excel. Ueberblick aller erforderlichen Dokumente mit …
6. **excel-reiter-4-workflow** — Baut Reiter 4 der Step-Plan-Excel: Workflow je Dokument in Reihenfolge der Beschaffung. Spalten erforderliches Dokument,…
7. **excel-reiter-2-vorhanden** — Baut Reiter 2 der Step-Plan-Excel: vorhandene Dokumente mit Augenmerk auf Unterschriftsstatus und Vertretungsbefugnis. S…
8. **padlet-als-werkzeug** — Erlaeutert, wann Padlet als visuelle Alternative zur Step-Plan-Excel sinnvoll ist und wann nicht. Beschreibt das Format …
9. **erweiterung-rangfolge-reiter** — Optionaler Reiter Rangfolge bei mehreren Finanzierungsinstrumenten. Stellt die Rang- und Befriedigungsreihenfolge dar: S…
10. **zugang-zustellung-pruefung** — Erfasst den Versendungs- und Zustellungsstatus aller zugangsbeduerftigen Willenserklaerungen: Kuendigungen, Faelligstell…
11. **szenario-finanzierungsstruktur-bereinigen** — Anwendungsszenario komplexe Finanzierungsstruktur bereinigen. Status-Navigator erfasst Wandeldarlehen, Bankfinanzierung,…
12. **szenario-due-diligence** — Anwendungsszenario Due Diligence. Status-Navigator strukturiert eine grosse disparate Dokumentensammlung im Rahmen einer…
13. **excel-reiter-3-fehlend** — Baut Reiter 3 der Step-Plan-Excel: fehlende Dokumente mit Beschaffungsweg. Spalten erforderliches Dokument, angefordert …
14. **dokumententyp-vertraege** — Erkennt Vertraege als Dokumentenklasse: Darlehensvertraege, Wandeldarlehen, Gesellschaftervereinbarungen, Pflichtenheft,…
15. **dokumententyp-cap-tables** — Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter und Ante…

---

## Skill: `excel-reiter-1-ueberblick`

_Baut Reiter 1 der Step-Plan-Excel: Ueberblick aller fuer die Durchsetzung erforderlichen Dokumente. Spalten Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Unterzeichnet von (Partei und Funktion), Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) und Zweck. Mit Ampelfaerbung und Sorti..._

# Reiter 1 Ueberblick Statuslage

## Rolle und Fokus
Reiter 1 ist die Gesamtsituation auf einen Blick. Alle fuer die Durchsetzung erforderlichen Dokumente in einer Zeile mit den wichtigsten Statusfeldern.

## Anwendungsbeispiel
LausitzStorage Reiter 1: 28 Zeilen ueber 4 Cluster, davon 4 rot (NordCap-Drawstop-Schreiben Zugang, Anlage 4 Konsortial, BImSchG-Vorbescheid Auflagen, Avalstatus 50Hertz), 7 gelb (Cap-Table-Versionen, drei Unterschriftsbefunde, ein Beschluss-Formfrage), Rest gruen. Pro Cluster eine Subsumtionszeile mit Cluster-Gesamtstatus.

## Output-Module
- Reiter 1 als Master-Index mit Querverweis in jede Detailpruefung
- Cluster-Gesamtstatuszeile je Vertragsebene
- Spalte Querverweis zu Reiter 2/3/4

---

## Skill: `status-navigator-einstieg`

_Einstiegs-Skill fuer den Status-Navigator: nimmt einen ungeordneten Dokumentenklumpatsch entgegen und liefert die ersten Antworten auf die zwei Kernfragen — was ist eigentlich los und was muss als Naechstes geschehen. Setzt den Rahmen fuer alle Folgeschritte und erzeugt eine erste grobe Bestandsa..._

# Einstieg: Was haben wir und was muss geschehen

## Rolle und Fokus
Erstes Sichten und grobes Strukturieren der Dokumentenlage. Setzt den Rahmen fuer alle Folgeschritte und beantwortet die zwei Kernfragen: Was haben wir? Was muss als Naechstes geschehen?

## Anwendungsbeispiel
LausitzStorage Erstsichtung 02.06.2026 nach Mandatsannahme: 80 PDFs aus drei Quellen; nach 90 Minuten liegt eine erste Reiter-1-Liste mit 28 Eintraegen, drei Sofortmassnahmen (Zugangsnachweis Drawstop sichern, Anlage 4 Konsortial nachfordern, Wandlungsfrist Wandeldarlehen pruefen) und ein Cluster-Ampelbild vor.

## Output-Module
- Erstrunde-Reiter-1 mit grober Verfuegbarkeit
- Liste der zwei bis drei Sofortmassnahmen
- Auftrag fuer Folgeskills (Inventur, Dokumententypen, Zustellung)

---

## Skill: `ziel-praezisieren`

_Klaert mit dem Auftraggeber das konkrete Ziel des Status-Navigators: Faelligstellung und Vollstreckung, Vollzug einer Kapitalmassnahme, Bereinigung der Finanzierungsstruktur, Due-Diligence-Vorbereitung oder Mandatsuebernahme. Das Ziel bestimmt Reiterstruktur, Pruefschwerpunkte und Workflow._

# Ziel praezisieren

## Rolle und Fokus
Klaert mit der Mandantin das konkrete Ziel des Status-Navigators. Faelligstellung, Bereinigung, Due Diligence, Mandatsuebernahme — das Ziel bestimmt die Reiterstruktur, Erweiterungen und Priorisierung.

## Anwendungsbeispiel
LausitzStorage Ziel laut Mandantenwunsch: (1) vollstaendige Bestandsaufnahme aller Vertraege und Genehmigungen, (2) Excel-Tracker, (3) Strategiepapier 14 Tage, (4) Zugangspruefung Drawstop-Schreiben. Daraus folgt Reiterstruktur mit Sicherheiten- und Fristen-Reiter (Pflicht), Cap-Table-Versionsregister noetig, BImSchG-Cluster eigenstaendig.

## Output-Module
- Schriftliche Zielnotiz (eine halbe Seite)
- Reiter- und Erweiterungs-Auswahl daraus abgeleitet
- Priorisierungsregel fuer Reiter 4 (Workflow)

---

## Skill: `szenario-faelligstellung-vollstreckung`

_Anwendungsszenario gescheiterte Finanzierung mit Vorbereitung von Faelligstellung und Vollstreckung. Status-Navigator erfasst Darlehensvertraege, Kuendigungs- und Faelligstellungsschreiben, Zustellungsnachweise und Sicherheiten. Workflow zeigt die naechsten Schritte fuer die Vollstreckung._

# Szenario gescheiterte Finanzierung

## Rolle und Fokus
Gescheiterte Finanzierung mit Vorbereitung von Faelligstellung und Vollstreckung. Status-Navigator erfasst Darlehensvertraege, Kuendigungs- und Faelligstellungsschreiben, Zustellungsnachweise, Sicherheiten.

## Anwendungsbeispiel
LausitzStorage hypothetische Spiegelung aus Glaeubigersicht (NordCap gegen LausitzStorage): Faelligstellungsgrund waere Drawstop-Folge, aber Drawstop ist einseitige Auszahlungsverweigerung — keine Faelligstellung. Echte Faelligstellung erst nach Reparaturvereinbarungs-Scheitern; dann Pfandverwertung an Anteilen und Grundschuldverwertung.

## Output-Module
- Faelligstellungs-Checkliste im Workflow-Reiter
- Zustellungs-Beweisplan je Erklaerung
- Verwertungs-Stufenplan mit Stufenstatus

---

## Skill: `padlet-spalte-1-ueberblick`

_Baut die erste Padlet-Spalte als Pendant zu Reiter 1 der Step-Plan-Excel. Ueberblick aller erforderlichen Dokumente mit Ampelfaerbung, Sortierung nach Vertragsebene und sieben Kartenfeldern (Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Unterzeichnet von, Rechtsgrundlage, Zweck)._

# Padlet Reiter 1 Ueberblick aufbauen

## Ziel
Spalte 1 des Padlets bildet Reiter 1 der Step-Plan-Excel ab: alle
erforderlichen Dokumente auf einen Blick, ampelfarblich gefuehrt.

## Vorlage-Bezug
Padlet-Spaltenkopf: `1. Uebersicht aller erforderlichen Dokumente`
Subtitle: `Alle fuer die Durchsetzung erforderlichen Dokumente in einer
einzigen Uebersicht.`

Karteninhalt pro Dokument (sieben Felder aus der Excel-Vorlage):

| Padlet-Feld | Inhalt aus Excel-Vorlage |
|---|---|
| Kartentitel | Dokument |
| Untertitel | Datum |
| Statusbadge oben rechts | Verfuegbarkeit |
| Badge zweite Reihe | Unterschriftsstatus |
| Body Absatz 1 | Unterzeichnet von (Partei und Funktion) |
| Body Absatz 2 | Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) |
| Body Absatz 3 | Zweck |

## Padlet-Konfiguration
- Layout: **Shelf** (Spalten)
- Sortierung innerhalb der Spalte: nach Vertragsebene
  (Pacht, Netz, Genehmigung, Finanzierung, Gesellschaft, EPC)
- Kartenfarbe: GRUEN, GELB, ROT entsprechend Ampel
- Standardansicht: kompakte Karten

## Anwendungsbeispiel
LausitzStorage-Akte:
- Erste Karte oben (GRUEN): Pachtvertrag LEAG Hauptvertrag, 11.07.2025,
  vorliegend, vollstaendig.
- Zweite Karte (ROT): 1. Nachtrag Pacht, 09.10.2025, vorliegend
  privatschriftlich, fragwuerdig (§ 177 BGB).
- Dritte Karte (ROT): 2. Nachtrag Pacht, 14.02.2026, fragwuerdig.
- Vierte Karte (GRUEN): Netzanschlussvertrag 50Hertz, 28.08.2025,
  vollstaendig.
- ...

## Output-Module
- Padlet-Spalte 1 mit allen Dokumenten als Karten
- Ampelfarbe je Karte
- Anhaenge verlinkt
- Sortierreihenfolge nach Vertragsebenen

## Grenzen
- **Cloud-Dienst.** Vor Einsatz Datenschutzpruefung (siehe Padlet-Intro-Skill).
- **Maximale Sinnhaftigkeit bei bis zu 50 Dokumenten.** Darueber wird
  die Spalte unuebersichtlich; dann Excel bevorzugen oder mehrere
  Padlets pro Vertragsebene.

## Plugin-Kontext
Spalte 1 ist die Eingangsansicht. Die folgenden drei Padlet-Skills bauen
die Detailspalten 2, 3 und 4 auf.

---

## Skill: `excel-reiter-4-workflow`

_Baut Reiter 4 der Step-Plan-Excel: Workflow je Dokument in Reihenfolge der Beschaffung. Spalten erforderliches Dokument, Schritte in Reihenfolge, Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag), Unterzeichnet von und Versendet an. Liefert den konkreten Action-Plan._

# Reiter 4 Workflow Step-Plan

## Rolle und Fokus
Reiter 4 ist das Herzstueck. Hier wird aus jedem fehlenden Dokument ein
konkreter Step-Plan: welche Schritte in welcher Reihenfolge, mit welcher
Rechtsgrundlage, von wem zu unterzeichnen, an wen zu versenden.

## Vorlage-Bezug
Reiter 4 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Erforderliches Dokument | aus Reiter 3 uebernommen |
| Schritte zur Beschaffung (in Reihenfolge) | nummeriert 1. 2. 3. ... |
| Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) | Klausel oder Paragraph |
| Unterzeichnet von | die Personen, die zeichnen muessen |
| Versendet an | Empfaenger, ggfs mit Sendeweg (Bote, Einschreiben, Notar, HR) |

## Anwendungsbeispiel
LausitzStorage-Akte, Reiter 4 enthaelt 12 Beschaffungs-Workflows.
Beispiele:
- Einzelaval 50Hertz: 1. Antwort ILB-Rueckfrage 18.04. ergaenzen,
  2. ILB-Komitee 18.06. abwarten, 3. Backup-Antrag Berliner Sparkasse
  parallel halten, 4. Aval-Urkunde an 50Hertz.
- Reparaturvereinbarung Wandeldarlehen NordCap: 1. Entwurf Akte 22
  finalisieren, 2. NordCap-Anwalt Mitzeichnung, 3. Bauernfeind
  unterzeichnet.

## Output-Module
- Tabelleneintraege fuer Reiter 4
- Reihenfolge-Visualisierung als Gantt-aehnliche Liste (Datumsspalte
  optional)
- Verantwortlichkeiten-Liste pro Person
- Eingangsstapel fuer optionale Reiter (Fristen, Beteiligte)

## Grenzen
- **Workflow ist Vorschlag, kein Anwaltsplan.** Anwaeltliche Pruefung der
  Rechtsgrundlagen-Spalte erforderlich.
- **Versendungswege sind Vorschlag.** Tatsaechlicher Zugangsweg muss
  haendisch abgesichert werden.
- **Zeitschaetzungen sind grob.** Behoerdliche Bearbeitungszeiten variieren.

## Plugin-Kontext
Reiter 4 ist der Action-Plan. Wenn Reiter 1 bis 3 sauber sind, schreibt
Reiter 4 sich fast von selbst. Optional ergaenzbar durch Reiter 5
(Fristen), Reiter 6 (Beteiligte), Reiter 7 (Rangfolge) und Reiter 8
(Sicherheiten).

---

## Skill: `excel-reiter-2-vorhanden`

_Baut Reiter 2 der Step-Plan-Excel: vorhandene Dokumente mit Augenmerk auf Unterschriftsstatus und Vertretungsbefugnis. Spalten Dokument, Datum, Typ, Unterzeichnet von, Unterschriftsstatus und Anmerkung. Lieferquelle fuer Unterschriftspruefung und Copy-Paste-Erkennung._

# Reiter 2 Vorhandene Dokumente

## Rolle und Fokus
Reiter 2 ist die Detailansicht aller tatsaechlich vorliegenden Dokumente,
mit Augenmerk auf Vertretungsbefugnis und Unterschriftsstatus. Hier wird
genauer hingeschaut als auf Reiter 1.

## Vorlage-Bezug
Reiter 2 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Dokument (Bezeichnung) | sprechend |
| Datum | Vertragsdatum |
| Typ | Vertrag, Bescheid, Erklaerung, Beschluss, Schreiben, Cap Table |
| Unterzeichnet von (Partei und Funktion) | konkret, mit Funktion |
| Unterschriftsstatus | vollstaendig / fragwuerdig / Entwurf |
| Anmerkung | Fundort, Urkundsnummer, Auffaelligkeiten |

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 2 enthaelt 16 vorliegende Dokumente. Drei
davon haben `fragwuerdig` als Unterschriftsstatus:
- 1. Nachtrag Pacht: Prokuristin Kosturek allein (Gesamtprokura mit GF
  erforderlich, § 177 BGB schwebend unwirksam) – Hinweis in Anmerkung
- 2. Nachtrag Pacht: GF Vansel allein (nur gemeinschaftliche Vertretung) – Hinweis
- Wandeldarlehen NordCap: § 4 verweist auf nicht existenten
  Gesellschafterbeschluss (Copy-Paste-Fehler) – Hinweis

## Output-Module
- Tabelleneintraege fuer Reiter 2
- Hinweisliste fuer Reiter 3 (was ist als Anlage zu beschaffen)
- Querliste fuer den Skill unterschriftspruefung
- Querliste fuer den Skill copy-paste-fehler-erkennung

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Schwebende Unwirksamkeit nach
  § 177 BGB ist nur ein Hinweis, kein Befund – Heilung pruefen anwaltlich.
- **Keine Vollmachts-Beurteilung.** Der Skill kann nur sichtbare Abweichungen
  vom HR-Eintrag herausarbeiten; gewillkuerte Vollmachten muessen aktiv
  abgefragt werden.

## Plugin-Kontext
Reiter 2 ist die Lieferquelle fuer die Skills unterschriftspruefung,
copy-paste-fehler-erkennung, diskrepanzen-aufdecken. Sauber gebauter
Reiter 2 spart Stunden in den Folgeschritten.

---

## Skill: `padlet-als-werkzeug`

_Erlaeutert, wann Padlet als visuelle Alternative zur Step-Plan-Excel sinnvoll ist und wann nicht. Beschreibt das Format Shelf mit vier Spalten als Mapping der vier Excel-Reiter, Datenschutz-Anforderungen, berufsrechtliche Grenzen sowie das Karten-Format pro Dokument._

# Padlet als Status-Navigator-Werkzeug

## Worum es geht
Padlet ist ein Online-Whiteboard-Dienst. Es eignet sich als visuelle
Variante des Step-Plans, parallel zur Excel-Tabelle. Der Vorteil: Mehrere
Personen sehen denselben Stand, Statusaenderungen sind sofort sichtbar,
Anhaenge (Vertragsscan, E-Mails) sind direkt verlinkbar.

## Wann Padlet sinnvoll ist
- Mehrere Bearbeiter, verteiltes Team
- Mandant soll Stand sehen koennen (ohne Excel-Versand)
- Schnelle Kommentar-Funktion gewuenscht
- Beweisbild fuer Beratungsgespraech: Live-Statuswand
- Workshop-Format mit Mandanten oder Mitgesellschaftern

## Wann Excel besser bleibt
- Datenschutz-strenge Mandate (keine Cloud-Drittanbieter)
- Mehr als 50 Dokumente: Padlet wird unuebersichtlich
- Anwaltlicher Schriftsatz braucht Excel-Anhang
- Druckausgabe als PDF (siehe PDF-Reiter-Variante)

## Padlet-Format der Wahl
**Padlet-Format Spalten** (heisst dort `Shelf` oder `Spalten-Layout`).
Vier Spalten = vier Reiter aus dem Step-Plan:
1. Uebersicht
2. Verfuegbar
3. Fehlend
4. Erstellung und Beschaffung

Alternative: vier separate Padlets, eines pro Reiter, falls die
Detailtiefe pro Spalte sehr hoch ist.

## Karten in Padlet
Jedes Dokument = eine Karte. Karten-Felder:
- Titel = Dokumentenbezeichnung
- Beschreibung = Datum, Vertragspartei, Status
- Farbe der Karte = Ampel (gruen, gelb, rot)
- Anhang = Scan oder Link auf DATEV-Akte
- Kommentar-Thread = Klaerungspunkte

## Datenschutz und Berufsrecht
Padlet ist ein US-Dienst. Vor Einsatz pruefen:
- DSGVO-konforme Konfiguration (EU-Server-Option)
- Anonymisierte Dokumentenbezeichnungen
- Keine Mandantennamen im Klartext
- Auftragsverarbeitungsvertrag mit Padlet-Anbieter
- Berufsrechtliche Geheimhaltung (§ 203 StGB, §§ 43a, 43e BRAO)

## Plugin-Kontext
Padlet ist eine optionale Ausspielform des Step-Plans. Inhaltlich liefert
das Padlet exakt die gleichen Daten wie die Excel-Reiter; nur die
Darstellung unterscheidet sich. Die nachfolgenden vier Skills
(padlet-reiter-1-...-4) zeigen, wie jeder einzelne Excel-Reiter als
Padlet-Spalte aufgebaut wird.

---

## Skill: `erweiterung-rangfolge-reiter`

_Optionaler Reiter Rangfolge bei mehreren Finanzierungsinstrumenten. Stellt die Rang- und Befriedigungsreihenfolge dar: Senior Secured, Senior Unsecured, Mezzanine, Gesellschafterdarlehen, sonstige Einlagen. Beruht ausschliesslich auf Mandatsangaben und Vertragstext._

# Erweiterung Rangfolge-Reiter

## Rolle und Fokus
Optionaler Reiter Rangfolge bei mehreren Finanzierungsinstrumenten. Senior Secured, Senior Unsecured, Mezzanine, Gesellschafterdarlehen, sonstige Einlagen — vertraglich vereinbarte Reihenfolge abbilden.

## Anwendungsbeispiel
LausitzStorage Rangfolge: Senior-Darlehen NordCap (besichert durch Grundschulden und Verpfaendung der Anteile) > Konsortial-Darlehen Stadtwerke Cottbus (besichert durch Sicherungsabtretung Stromabnahmevertrag) > Wandeldarlehen NordCap (unbesichert, nachrangig nach § 39 InsO automatisch nicht — aber vertraglich subordiniert) > Gesellschafter-Stundungen Bauernfeind privat.

## Output-Module
- Rangfolge-Reiter mit Spalten Instrument, Glaeubiger, Volumen, Sicherheit, Rang
- Hinweis-Spalte mit Quellnachweis (welche Klausel begruendet den Rang)
- Pflichthinweis auf anwaltliche Pruefung insolvenzrechtlicher Rangfragen

---

## Skill: `zugang-zustellung-pruefung`

_Erfasst den Versendungs- und Zustellungsstatus aller zugangsbeduerftigen Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Mahnungen. Markiert, wo der Zugang unklar ist oder noch nachzuweisen waere. Trifft keine rechtliche Bewertung des Zugangs._

# Zugang und Zustellung pruefen

## Rolle und Fokus
Erfasst den Versendungs- und Zustellungsstatus aller zugangsbeduerftigen Willenserklaerungen. Markiert, wo der Zugang unklar ist oder nachzuweisen waere. Keine rechtliche Bewertung des Zugangs.

## Anwendungsbeispiel
LausitzStorage Zugangsspuren: Drawstop-Schreiben NordCap vom 22.05.2026 ging per E-Mail ohne Empfangsbestaetigung an Bauernfeind, Zugang ungenau — § 130 BGB Voraussetzungen unklar fuer Empfangsmoeglichkeit, da Bauernfeind zu der Zeit auf Dienstreise; LEAG-Kuendigungsdrohung vom 19.05.2026 als E-Mail-Thread an mehrere Mitarbeiter, Zugangs-Beweisspur uneinheitlich; Faelligstellungs-Vorbereitung wuerde Boten-Zustellung erfordern.

## Output-Module
- Zugangs-Beweisplan je Erklaerung
- Markierung der Erklaerungen ohne sichere Zustellung in Reiter 3
- Empfehlung Boten-Zustellung fuer kritische Folge-Erklaerungen

---

## Skill: `szenario-finanzierungsstruktur-bereinigen`

_Anwendungsszenario komplexe Finanzierungsstruktur bereinigen. Status-Navigator erfasst Wandeldarlehen, Bankfinanzierung, Gesellschafterdarlehen, sonstige Einlagen und Stundungen. Stellt Konditionen und Rangfolge zusammen und vergleicht Cap Tables mit Vertraegen._

# Szenario Finanzierungsstruktur bereinigen

## Rolle und Fokus
Komplexe Finanzierungsstruktur bereinigen. Status-Navigator erfasst Wandeldarlehen, Bankfinanzierung, Gesellschafterdarlehen, sonstige Einlagen und Stundungen.

## Anwendungsbeispiel
LausitzStorage Bereinigung: Senior-Darlehen NordCap 80 Mio EUR, Wandeldarlehen NordCap 22 Mio EUR (Reparaturvereinbarung vom 04.06.2026 verlaengert Wandlungsfenster), Konsortial Stadtwerke Cottbus 25 Mio EUR (Sicherungsabtretung Stromabnahmevertrag), Avalrahmen ILB 8 Mio EUR (LEAG-Pachtsicherung), Gesellschafterstundung Bauernfeind 1,2 Mio EUR. Vier Klaerpunkte im Workflow.

## Output-Module
- Instrumentenkarte mit Rang und Sicherheit
- Konditionsuebersicht je Instrument
- Step-Plan mit Bereinigungs-Massnahmen und Verantwortlichkeit

---

## Skill: `szenario-due-diligence`

_Anwendungsszenario Due Diligence. Status-Navigator strukturiert eine grosse disparate Dokumentensammlung im Rahmen einer Transaktion. Prueft auf Vollstaendigkeit und Diskrepanzen. Vorbereitung der Datenraum-Indexierung fuer das Targetunternehmen._

# Szenario Due Diligence

## Rolle und Fokus
Status-Navigator als DD-Werkzeug. Strukturiert eine grosse disparate Dokumentensammlung in der Transaktion. Vorbereitung der Datenraum-Indexierung fuer das Targetunternehmen.

## Anwendungsbeispiel
LausitzStorage als hypothetisches DD-Target: 28 Reiter-1-Eintraege werden gegen eine Standard-Renewables-Q&A-Liste gespiegelt; ergeben sich 4 closing-relevante Findings (Anlage 4 Konsortial fehlt, BImSchG-Auflagen unklar, Avalstatus 50Hertz, Cap-Table-Konsistenz) und 7 reporting-relevante Findings (drei Unterschriftsbefunde, ein Beschluss-Formfrage, zwei Kommunikations-Threading-Luecken, ein Vertragsdrift NordCap).

## Output-Module
- DD-Index als Reiter 1 mit Cluster-Gliederung
- Findings-Tabelle im Workflow-Reiter mit Closing- vs. Reporting-Klassifizierung
- Vergleichsmemo Verkaeufer-Disclosure gegen Datenraum

---

## Skill: `excel-reiter-3-fehlend`

_Baut Reiter 3 der Step-Plan-Excel: fehlende Dokumente mit Beschaffungsweg. Spalten erforderliches Dokument, angefordert von, zu beschaffen von, Grund der Erforderlichkeit und Status. Sortierung nach Frist. Vorbereitung fuer den Workflow-Reiter._

# Reiter 3 Fehlende Dokumente

## Rolle und Fokus
Reiter 3 listet alles, was fehlt oder noch nicht endgueltig vorliegt.
Jede Zeile hier ist eine offene Position, die in den Workflow von
Reiter 4 ueberfuehrt werden muss.

## Vorlage-Bezug
Reiter 3 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Erforderliches Dokument / erforderlicher Nachweis | sprechend |
| Angefordert von | Person oder Kanzlei intern |
| Zu beschaffen von | Quelle: Behoerde, Notar, Vertragspartner |
| Grund der Erforderlichkeit | warum brauchen wir es, mit Querverweis Klausel oder Paragraph |
| Status | offen / Anforderung raus / in Bearbeitung / vorzubereiten / Frist |

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 3 enthaelt 12 Positionen, sortiert nach Frist:
- 09.06.: Aushaendigung LEAG-Aval (Frist § 11 Pacht ueberzogen)
- 10.06.: Notartermin Klarstellungs-Nachtrag Pacht
- 11.06.: Klarstellungs-Side-Letter Anlage 4
- 18.06.: ILB-Komitee Einzelaval 50Hertz
- 30.06.: BImSchG-Hauptantrag (Drohfrist LEAG)

## Output-Module
- Tabelleneintraege fuer Reiter 3
- Frist-Liste aufsteigend
- Eingangsstapel fuer Reiter 4 (Workflow)
- Optional Reiter 5 (Fristenkontrolle) mit Querverweis

## Grenzen
- **Beschaffungswege koennen sich verschieben.** Behoerdliche Bearbeitungszeiten
  realistisch ansetzen, nicht idealisieren.
- **Frist-Tracking ersetzt keinen Fristenkalender.** Anwaltlicher Fristenkalender
  bleibt verbindlich.

## Plugin-Kontext
Reiter 3 ist die Voraussetzung fuer Reiter 4. Ohne saubere Liste der
fehlenden Stuecke kann kein Workflow gebaut werden.

---

## Skill: `dokumententyp-vertraege`

_Erkennt Vertraege als Dokumentenklasse: Darlehensvertraege, Wandeldarlehen, Gesellschaftervereinbarungen, Pflichtenheft, Kaufvertraege, Sicherungsvertraege. Ordnet sie nach Vertragspartei, Datum, Vertragstyp und Bezug zu uebrigen Dokumenten._

# Dokumententyp Vertraege erkennen

## Rolle und Fokus
Erkennt Vertraege als Dokumentenklasse. Pachtvertraege, Darlehensvertraege, Konsortialvertraege, Sicherungsvertraege, Gesellschaftervereinbarungen. Ordnet nach Vertragspartei, Datum, Vertragstyp.

## Anwendungsbeispiel
LausitzStorage-Vertragslandschaft: Pachtvertrag LEAG mit 2 Nachtraegen, Senior-Darlehen NordCap, Wandeldarlehen NordCap, Konsortialvertrag Stadtwerke Cottbus, Avalrahmenvertrag ILB, Netzanschluss 50Hertz. Sieben Vertraege mit teils ueberlappenden Sicherheiten und Zustimmungserfordernissen — eine Vertragslandkarte vor der Reiterpflege ist Pflicht.

## Output-Module
- Vertragslandkarte (Bezugsgraph) als Vorblatt
- Eintraege in Reiter 2 mit Typ-Tag Vertrag und Untertyp
- Querverweise auf abhaengige Beschluesse, Vollmachten und Sicherheitenbestellungen

---

## Skill: `dokumententyp-cap-tables`

_Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter und Anteile. Vorbereitung fuer den Konsistenz-Vergleich mehrerer Cap Tables und Abgleich mit den zugrundeliegenden Vertraegen._

# Dokumententyp Cap Tables

## Rolle und Fokus
Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter, Anteile. Vorbereitung fuer Konsistenzvergleich mehrerer Versionen.

## Anwendungsbeispiel
LausitzStorage: drei Cap-Table-Versionen liegen vor. v1 (31.12.2025, von Mandantin), v2 (30.04.2026, von NordCap-Datenraum), v3 (Mai 2026, aus Investor-Update). Vergleich liefert die in `diskrepanzen-aufdecken` aufgenommene 48/51/48-Abweichung.

## Output-Module
- Versionsregister mit Stichdatum, Quelle, Status
- Normalisierte Cap-Table als Vorlage fuer den Konsistenzvergleich
- Querliste an `szenario-cap-table-bereinigung` wenn Abweichungen materiell

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

