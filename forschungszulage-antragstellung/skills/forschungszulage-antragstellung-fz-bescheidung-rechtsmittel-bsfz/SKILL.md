---
name: forschungszulage-antragstellung-fz-bescheidung-rechtsmittel-bsfz
description: "FZ Bescheidung Rechtsmittel Bsfz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# FZ Bescheidung Rechtsmittel Bsfz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **FZ Bescheidung Rechtsmittel Bsfz** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fz-bescheidung-rechtsmittel` | Bescheidung Forschungszulage: Bescheinigungsbescheid BSFZ und Festsetzungsbescheid Finanzamt sind zwei getrennte Verwaltungsakte. Rechtsmittelketten: BSFZ-Widerspruch dann Verpflichtungsklage; Finanzamt-Einspruch dann Klage Finanzgericht. Fristen und Begruendungsbausteine. |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag und FuE-Projektbeschreibung praxistauglich erstellen: Portaltexte mit Zeichenbudgets, Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete, Prüferlogik, Anti-Floskel-Regeln und Strategie Einzelantrag vs. Projektbündel. |
| `fz-dokumentationspaket-betriebspruefung` | Dokumentationspaket Forschungszulage prüfungsfest aufbauen: Projektakte mit BSFZ-Antrag und Bescheid, Stundenaufzeichnung je Mitarbeiter Tag Vorhaben, Personalkostenbeleg aus Lohnabrechnung, Auftragsforschungsbeleg mit Vertrag und Rechnung, GoBD-Logik. Mit Spaltenstruktur, 10-Jahres-Aufbewahrung und Stichprobenstrategie für die Außenprüfung. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **FZ Bescheidung Rechtsmittel Bsfz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fz-bescheidung-rechtsmittel`

**Fokus:** Bescheidung Forschungszulage: Bescheinigungsbescheid BSFZ und Festsetzungsbescheid Finanzamt sind zwei getrennte Verwaltungsakte. Rechtsmittelketten: BSFZ-Widerspruch dann Verpflichtungsklage; Finanzamt-Einspruch dann Klage Finanzgericht. Fristen und Begruendungsbausteine.

# FZ: Bescheidung und Rechtsmittel

## Spezialwissen: FZ: Bescheidung und Rechtsmittel
- **Spezialgegenstand:** FZ: Bescheidung und Rechtsmittel / fz bescheidung rechtsmittel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BSFZ, FZ.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `fz-bsfz-bescheinigung-projektbeschreibung`

**Fokus:** BSFZ-Antrag und FuE-Projektbeschreibung praxistauglich erstellen: Portaltexte mit Zeichenbudgets, Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete, Prüferlogik, Anti-Floskel-Regeln und Strategie Einzelantrag vs. Projektbündel.

# BSFZ-Bescheinigung und Projektbeschreibung

## Worum geht es

Die Bescheinigungsstelle Forschungszulage (BSFZ) prüft im ersten Verfahrensschritt, ob ein Vorhaben FuE im Sinne des FZulG ist. Sie sagt nichts zur Höhe der Förderung, nichts zur Bemessungsgrundlage, nichts zur Personalkostenberechnung. Sie sagt nur: ja, das ist Forschung — oder nein. Ohne diese Bescheinigung gibt es keine Festsetzung beim Finanzamt.

Eingang ist das Portal https://www.bescheinigung-forschungszulage.de/. Der Antrag wird elektronisch eingereicht.

## Wann dieses Modul hilft

- Sobald die FuE-Eigenschaft durch `fz-fue-definition-frascati-abgrenzung` plausibilisiert ist.
- Bei BSFZ-Rückfragen zu Inhalt oder Tiefe der Projektbeschreibung.
- Wenn mehrere verwandte Vorhaben gebearbeitet eingereicht werden sollen.
- Vor jedem Folgeantrag im Mehrjahresprojekt.

## Sachrahmen — was die BSFZ tatsächlich macht

- Eingangsprüfung (formal: Antragsteller, Vorhaben, Zeitraum, Zuordnung).
- Fachprüfung durch eine fachnahe Gutachterin oder einen Gutachter (Domäne, oft promoviert/habilitiert).
- Eventuell Rückfragen (Nachforderung).
- Bescheinigungsentscheid (positiv, eingeschränkt, ablehnend).

Bearbeitungszeit erfahrungsgemäß einige Monate; Q1-Einreichung beschleunigt erfahrungsgemäß den Durchlauf.

## Gliederung der Projektbeschreibung

Nicht mit einem Kanzlei-Memo verwechseln: Der BSFZ-Leitfaden 2026 arbeitet im Portal mit engen Zeichenbudgets. Intern darf die Analyse ausführlich sein; die Einreichungsfassung muss hart verdichtet werden.

| Portalbaustein | Zeichenbudget laut BSFZ-Leitfaden 2026 | Inhalt |
| --- | --- | --- |
| Ziel / Herausforderung / Wissenslücke | ca. 1.500 Zeichen | konkretes technisches oder wissenschaftliches Problem, Zielwert, Neuheit für das Unternehmen |
| Abgrenzung zum Stand der Technik | ca. 500 Zeichen | bisherige Lösung, messbare Grenze, warum das Neue nicht bloße Routine ist |
| Arbeiten / Lösungsweg | ca. 1.000 Zeichen | Methoden, Versuche, Iterationen, Decision-Gates, kein Marketing |
| Unsicherheiten / Scheitern | ca. 1.000 Zeichen | konkrete technische, wissenschaftliche oder methodische Risiken; keine Markt- oder Verwertungsrisiken |
| Auftragnehmer | ca. 500 Zeichen je Auftragnehmer | was der Auftragnehmer FuE-mäßig tut, nicht nur Bestellung oder Werkstückfertigung |
| Arbeitsplan | separates Portal-/PDF-Element | Arbeitspakete mit Zeitraum, Inhalt, Meilenstein, Aufwand |

Arbeite daher immer zweistufig:

1. **Interne Langfassung** zur Denk- und Belegarbeit: Quellen, Messwerte, AP-Details, Risiken, Routineabgrenzung.
2. **Portaltext** mit Zeichenlogik: kurz, technisch, konkret, ohne Unternehmenswerbung.

## Praxisleitfaden — was die Prüferin sehen will

- **Konkretes technisches Problem.** Nicht "Effizienz verbessern", sondern "Energieverbrauch von 320 Wh/Stunde auf unter 180 Wh/Stunde".
- **Konkretes Risiko.** "Versuche an Vormaterial X können wegen unbekannter Sintertemperatur scheitern" ist gut. "Risiken bestehen" reicht nicht.
- **Dokumentierter Lösungsweg.** Welche Hypothesen testen Sie? Welche Iterationen sind eingeplant?
- **Arbeitspakete in Tabellenform.** AP-1 Konzept, AP-2 Versuchsreihe, AP-3 Prototyp, AP-4 Charakterisierung. Mit Meilensteinen und Personenstunden.
- **Stand der Technik mit Quellen.** Die Prüferin ist Fachexpertin. Wer den Stand der Technik nicht zitiert, signalisiert, dass die Hausaufgaben fehlen.
- **Deutsch einreichen.** Fremdsprachige Beschreibungen und allgemeine Business-Roadmaps sind für die BSFZ-Prüfung ungeeignet.

### Anti-Floskel-Regeln (was bei der BSFZ sofort fliegt)

- "Innovative Plattform" — streichen.
- "KI-basiert" ohne ML-Konzept — präzisieren oder weglassen.
- "Digitalisierung", "Industrie 4.0", "Smart Factory" als Selbstzweck — streichen.
- Produktbeschreibung statt Forschungsfrage — komplett umschreiben.
- Roadmap-Stil ("Q3 wir launchen ...") — streichen, Meilensteinkriterien statt Marketingzeitlinie.
- Adjektive ohne Operationalisierung ("modern", "smart", "next-gen") — streichen.

### Anti-Pattern, die zur Ablehnung führen

- Beschreibung des Produkts statt des FuE-Vorgehens.
- Anforderungsliste statt Forschungsproblem.
- Keine Abgrenzung zu Serienpflege.
- Keine Quellen für den Stand der Technik.
- Risiken nur erwähnt, nicht spezifiziert.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Ein großes Vorhaben vs. mehrere | hohe Aufmerksamkeit der Prüfer | weniger Risiko je Antrag | Bündel bei technischer Verwandtschaft |
| Detailtief vs. übersichtlich | interne Langfassung | Portaltext | erst tief denken, dann brutal verdichten |
| Frühe Einreichung vs. Stabilität | Q1 minimal beschrieben | Q3 reif | Q1 reif, früh in der Bearbeitungsschlange |
| Eigene Schreibarbeit vs. Berater | inhouse, geringere Kosten | Beraterprofile mit Track Record | Berater bei Erstantrag, intern bei Folgeanträgen |

## Schritt für Schritt

1. Frascati-Memo aus `fz-fue-definition-frascati-abgrenzung` als Basis verwenden.
2. Vorhaben-Steckbrief vorbereiten: Titel, Vorhabenzeitraum, Hauptpersonen, FuE-Kategorie.
3. Ausgangsproblem in einem präzisen Absatz fassen.
4. Stand der Technik mit 2 bis 3 Quellen.
5. Neuheit klar herausarbeiten.
6. Technische Unsicherheit konkret nennen.
7. Arbeitspakete als Tabelle.
8. Abgrenzung zur Routine als eigener Abschnitt.
9. Portaltexte gegen Zeichenbudgets kürzen, ohne Neuheit/Risiko zu verlieren.
10. Antrag im BSFZ-Portal eingeben, PDF-Arbeitsplan prüfen, Plausibilitäts-Check.

## Mustertexte

**Ausgangsproblem (Vorlage):**

"Im Bereich [Domäne, z. B. Wärmetauscher für Hochtemperaturanwendungen] erreicht der derzeitige Stand der Technik (siehe [Norm/Quelle 1]; [Quelle 2]) eine [Messgröße, z. B. Wirkungsgrad] von [Wert, z. B. 72 Prozent] bei [Randbedingung, z. B. 800 Grad Celsius]. Für [Zielanwendung] ist ein Wert von mindestens [Zielwert] erforderlich. Voruntersuchungen ([eigene Quelle / Vorprojekt]) zeigen, dass dieser Wert mit bestehenden Verfahren nicht erreichbar ist."

**Neuheit (Vorlage):**

"Wir untersuchen [konkretes Verfahren / konkrete Materialkombination / konkrete Architektur]. Die Neuheit liegt in [konkrete technische Kombination, z. B. Kombination eines neuartigen Substrats mit einem bislang nur für Niedrigtemperatur eingesetzten Beschichtungsverfahren]. Nach systematischer Recherche (siehe Anlage Quellenverzeichnis) ist diese Kombination im Stand der Technik nicht beschrieben."

**Technische Unsicherheit (Vorlage):**

"Es ist offen, ob [Bedingung, z. B. die geforderte Festigkeit] unter [Randbedingung, z. B. Dauerlast bei 750 Grad Celsius] erreicht werden kann. Insbesondere [Hürde, z. B. die Diffusion an der Grenzfläche] kann zum Scheitern führen. Vergleichbare Vorhaben (siehe [Quelle]) scheiterten an [Punkt]."

**Arbeitspakete-Tabelle (Vorlage):**

| AP | Inhalt | Meilenstein | Personenstunden | Erfolgskriterium |
| --- | --- | --- | --- | --- |
| AP-1 | Literaturrecherche, Konzept | M1 Konzeptpapier | 120 | konsistentes Konzept |
| AP-2 | Versuchsreihe Variante A | M2 Datenbasis A | 400 | mindestens 8 Messreihen |
| AP-3 | Versuchsreihe Variante B | M3 Datenbasis B | 400 | mindestens 8 Messreihen |
| AP-4 | Prototyp | M4 Prototyp lauffähig | 600 | Wirkungsgrad gemessen |
| AP-5 | Charakterisierung | M5 Abschlussbericht | 200 | Bewertung gegen Zielwert |

**Mehrere Projekte:** Wenn technisch verwandt, als Vorhabenbündel mit gemeinsamer Klammer einreichen. Wenn unverbunden, je eigener Antrag.

**Portal-Kompression (Vorlage):**

| Baustein | Arbeitsanweisung |
| --- | --- |
| 1.500 Zeichen Ziel | ein Problem, ein Zielwert, ein Neuheitskern |
| 500 Zeichen Stand der Technik | zwei harte Vergleichspunkte, keine Literaturwüste |
| 1.000 Zeichen Arbeiten | AP-Logik in Prosa, keine bloße Liste |
| 1.000 Zeichen Unsicherheit | warum kann es technisch scheitern, warum ist das gerade FuE? |

## Typische Fehler

- Produktbeschreibung statt FuE-Beschreibung.
- Stand der Technik nicht oder oberflächlich zitiert.
- Risiken nur abstrakt.
- Arbeitspakete ohne Erfolgskriterium.
- Routine-Anteile versteckt statt offen abgegrenzt.
- BSFZ-Antrag und Finanzamt-Antrag verwechselt (BSFZ macht nur die FuE-Eigenschaft).

## Output

- BSFZ-taugliche Portaltexte mit Zeichenbudget.
- Interne Langfassung als Beleg- und Kürzungsgrundlage, wenn Material vorhanden ist.
- Arbeitspaket-Matrix.
- Quellenverzeichnis Stand der Technik.
- Nachforderungsvorsorge: Liste der vorbereiteten Antworten auf typische Rückfragen.
- Liste der Anlagen (Skizzen, Vorprojekt-Berichte, Patente, Publikationen).

## Querverweise

- `fz-fue-definition-frascati-abgrenzung` für die FuE-Vorprüfung.
- `fz-bemessungsgrundlage-2026` für die parallele Vorbereitung der Personalkostenrechnung.
- `fz-dokumentationspaket-betriebspruefung` für die spätere Belegfähigkeit.
- `fz-ablehnung-nachbesserung-einspruch` bei BSFZ-Rückfragen.

## Quellen Stand 05/2026

- BSFZ-Portal: https://www.bescheinigung-forschungszulage.de/
- BSFZ-Antragsverfahren: https://www.bescheinigung-forschungszulage.de/antragsverfahren/ueber-das-antragsverfahren
- BSFZ-Hilfen: https://www.bescheinigung-forschungszulage.de/hilfen-zur-antragstellung
- FZulG: https://www.gesetze-im-internet.de/fzulg/
- AGVO Art. 2 Nr. 84 bis 86 (vom Antragsteller mit konsolidierter Fassung zu prüfen).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `fz-dokumentationspaket-betriebspruefung`

**Fokus:** Dokumentationspaket Forschungszulage prüfungsfest aufbauen: Projektakte mit BSFZ-Antrag und Bescheid, Stundenaufzeichnung je Mitarbeiter Tag Vorhaben, Personalkostenbeleg aus Lohnabrechnung, Auftragsforschungsbeleg mit Vertrag und Rechnung, GoBD-Logik. Mit Spaltenstruktur, 10-Jahres-Aufbewahrung und Stichprobenstrategie für die Außenprüfung.

# Dokumentationspaket für Außenprüfung

## Worum geht es

Die Forschungszulage wird auf Antrag festgesetzt; sie steht aber unter dem ständigen Risiko einer Außenprüfung beim Finanzamt. Wer die Belege erst bei Prüfungsankündigung zusammensucht, verliert Diskussionen. Dieser Skill liefert das prüfungsfeste Belegset, die Stundenaufzeichnungslogik, die GoBD-konforme Ablage und die Stichprobenstrategie.

## Wann dieses Modul hilft

- Beim Erstantrag, parallel zur BSFZ-Vorbereitung.
- Bei jeder Folge-Beantragung.
- Bei Ankündigung einer Außenprüfung (idealerweise nicht erst dann).
- Bei Übernahme eines Mandats mit Forschungszulage-Vergangenheit.

## Sachrahmen — was wirklich geprüft wird

- **FuE-Eigenschaft:** durch BSFZ-Bescheinigung bindend bestätigt; die Außenprüfung prüft sie nicht erneut, kann aber die Konsistenz Projektakte zur BSFZ-Bescheinigung hinterfragen.
- **Personalkosten:** Höhe je Mitarbeiter und Wirtschaftsjahr, Lohnabrechnung, SV-Beiträge.
- **Stundenzuordnung:** wer hat an welchem Tag wie viele Stunden auf welches Vorhaben gebucht? Plausibilität gegen Urlaub, Krankheit, Schulungen.
- **Auftragsforschung:** Vertrag, Leistungsbeschreibung, Rechnung, Zahlung, EU/EWR-Ansässigkeit.
- **Eigenleistung:** Stundenaufzeichnung des Einzelunternehmers, 40-Stunden-Cap eingehalten.
- **Wirtschaftsgüter:** Zuordnungsnachweis zu FuE, AfA-Plan.
- **Kumulierung:** AGVO-Höchstintensität nicht überschritten, weitere Förderungen offen gelegt.

## Praxisleitfaden — die vier Belege, die das Finanzamt sehen will

### 1. Projektakte

- BSFZ-Antrag (PDF) + BSFZ-Bescheinigung mit Aktenzeichen.
- Projektsteckbrief: Titel, Zeitraum, Ziele, Arbeitspakete, Personenzuordnung.
- Stand der Technik mit Quellen.
- Meilensteinberichte oder Sprint-Reviews.
- Negative Versuchsergebnisse — diese sind FuE-typisch und entkräften den "Routine"-Vorwurf.

### 2. Stundenaufzeichnung (Mitarbeiter × Tag × Vorhaben)

Pflichtspalten:

| Datum | Mitarbeiter | Vorhaben/AP | Stunden | Tätigkeit (FuE-konkret) | Modus | Auftrag/Eigen |
| --- | --- | --- | --- | --- | --- | --- |
| 12.03.2026 | M. Müller | V-1 / AP-2 | 6.5 | Aufbau Messreihe Variante A, Kalibrierung | FuE | Eigen |
| 12.03.2026 | M. Müller | Service | 1.5 | Wartung Bestandsanlage | Routine | N |

- Wichtig: **Auftragnehmer-Auftraggeber-Trennung** bei Auftragsforschung. Wer als Auftragnehmer FuE leistet, dokumentiert separat.
- Mögliche Tools: Excel-Vorlage, Jira/Asana-Export mit angepassten Feldern, vollwertiges Zeiterfassungssystem (z. B. Personio, atvise, ZEP).
- Tagesgenaue Aufzeichnung schlägt monatliche Pauschalbuchung deutlich.

### 3. Personalkostenbeleg pro Mitarbeiter

- Jahreslohnkonto.
- Aufstellung Bruttolohn + Arbeitgeber-SV + Altersvorsorge.
- Berechnung des FuE-Anteils aus Stundenaufzeichnung (Quersumme).
- Tätigkeitsbeschreibung der Stelle (Stellenausschreibung, Stellenbeschreibung).

### 4. Auftragsforschungsbeleg

- Vertrag mit klarer Leistungsbeschreibung (FuE-Vorhaben benannt, Arbeitspakete, Vergütung).
- Rechnungen mit Bezug zum Vertrag.
- Zahlungsnachweis.
- Sitznachweis des Auftragnehmers (Handelsregisterauszug, Bestätigung EU/EWR).
- Bei Wissenschaftseinrichtung: Bestätigung des Status.

## Aufbewahrung 10 Jahre — GoBD-Logik

- Belege elektronisch, unveränderlich, geordnet.
- Verfahrensdokumentation (Wer hat wann wie gebucht? Welche Tools? Welche Korrekturlogik?).
- Schreibschutz für abgeschlossene Wirtschaftsjahre.
- Backup-Konzept.
- Aufbewahrungsdauer 10 Jahre — orientiert an GoBD und § 147 AO; vom Antragsteller mit konkreter Vorschrift abzugleichen.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Excel-Vorlage vs. Tool | niedrige Kosten, hoher Pflegeaufwand | hohe Kosten, automatisierte Belege | Tool ab ca. 5 FuE-Mitarbeitern |
| Tagesgenau vs. wochenpauschal | sicher, höherer Aufwand | weniger Aufwand, Prüfungsrisiko | tagesgenau |
| Verbale Tätigkeit vs. AP-Code | knapp, schwer prüfbar | klar, höhere Erfassung | AP-Code plus zwei bis drei Stichworte |
| Berater-gepflegte Akte vs. Inhouse | externer Aufwand | eigenes Personal | Inhouse für Stundenaufzeichnung, Berater für Akte |

## Schritt für Schritt — das Paket aufbauen

1. Stundenaufzeichnungs-Tool wählen, Pflichtspalten konfigurieren.
2. Mitarbeiter schulen: Tagesbuchung, AP-Code, Tätigkeitstext.
3. Projektakte als Master-Verzeichnis anlegen (z. B. Sharepoint, Confluence, Dateiablage mit Schreibschutz).
4. Quartalsweise Personalkosten je Mitarbeiter rechnen und der Projektakte beilegen.
5. Auftragsforschungsverträge zentral ablegen, Rechnungen verknüpfen.
6. Wirtschaftsgüter mit Zuordnungsnachweis im AfA-Plan ergänzen.
7. AGVO-Kumulierungsblatt parallel pflegen (siehe `fz-kumulierung-beihilfen-agvo`).
8. Verfahrensdokumentation in einem zentralen Memo festhalten.

## Stichprobenstrategie für die Außenprüfung

- Selber zwei bis drei Stichprobentage je Mitarbeiter und Wirtschaftsjahr durchgehen: gibt es Konsistenz Stundenaufzeichnung — Projektakte — Personalkosten?
- Bei Differenzen: nachbessern und im Memo dokumentieren.
- Krankheits- und Urlaubstage gegen die Personalakte abgleichen.
- Externe Belege (Auftragsforschungsrechnungen) stichprobenweise dem Vertrag zuordnen.

## Mustertexte / Vorlagen

**Inhaltsverzeichnis Prüfermappe:**

```
0. Verfahrensdokumentation
1. Projektakte je Vorhaben
 1.1 Projektsteckbrief
 1.2 BSFZ-Antrag und Bescheinigung
 1.3 Arbeitspakete und Meilensteine
 1.4 Versuchsberichte und Ergebnisse
 1.5 Quellenverzeichnis Stand der Technik
2. Zeit- und Personalkosten
 2.1 Stundenaufzeichnung Mitarbeiter A
 2.2 ...
 2.x Personalkosten je Mitarbeiter
3. Auftragsforschung
 3.1 Verträge
 3.2 Rechnungen
 3.3 Zahlungsnachweise
 3.4 EU/EWR-Bestätigung
4. Wirtschaftsgüter
 4.1 AfA-Plan
 4.2 Zuordnungsnachweise
5. Gemein- und Betriebskostenpauschale (sofern einschlägig)
6. Andere Förderungen / AGVO-Kumulierungsblatt
7. Finanzamt-Antrag und Bescheide
8. Korrespondenz BSFZ und Finanzamt
```

**Plausibilitätscheck Stundenaufzeichnung:**

| Mitarbeiter | Soll-Stunden | Ist-Stunden | FuE-Stunden | FuE-Anteil | Plausibilität |
| --- | --- | --- | --- | --- | --- |
| M. Müller | 1.760 | 1.745 | 1.222 | 70 Prozent | konsistent |

## Typische Fehler

- Stundenaufzeichnung erst nachträglich erstellt — verliert vor jeder Außenprüfung an Glaubwürdigkeit.
- Tätigkeitstexte zu generisch ("FuE", "Forschung").
- Auftragsforschungs-Rechnungen ohne Vertragsbezug.
- Wirtschaftsgüter ohne Zuordnungsnachweis.
- AGVO-Kumulierungsblatt fehlt.
- Verfahrensdokumentation fehlt.

## Output

- Inhaltsverzeichnis der Prüfermappe.
- Fehlende-Belege-Liste mit Verantwortlichen.
- Plausibilitätscheck Stunden/Kosten/Projektfortschritt.
- Mandanten-E-Mail zur Nachforderung der offenen Belege.
- Verfahrensdokumentations-Memo.

## Querverweise

- `fz-bemessungsgrundlage-2026` für die Personalkostenformel.
- `fz-bsfz-bescheinigung-projektbeschreibung` als Quelle der Projektakte.
- `fz-kumulierung-beihilfen-agvo` für das Kumulierungsblatt.
- `fz-roadmap-mehrjahresantrag` für die jährliche Wiederholungsroutine.

## Quellen Stand 05/2026

- § 147 AO (Aufbewahrungspflichten).
- GoBD-Grundsätze (BMF-Schreiben, vom Antragsteller mit aktueller Fassung zu prüfen).
- FZulG (Belegpflichten).
- `references/forschungszulage-quellen-und-zahlen.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
