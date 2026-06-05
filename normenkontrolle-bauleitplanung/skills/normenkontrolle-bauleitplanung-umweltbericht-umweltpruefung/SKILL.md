---
name: normenkontrolle-bauleitplanung-umweltbericht-umweltpruefung
description: "Umweltbericht Umweltpruefung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Umweltbericht Umweltpruefung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Umweltbericht Umweltpruefung** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `umweltbericht-umweltpruefung` | Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden Wasser Luft Klima Landschaft Kultur Nullvariante Alternativen FFH-Vertraeglichkeit § 1a Abs. 4 BauGB. Beschleunigtes Verfahren § 13a BauGB ohne Umweltprüfung. Output: Umweltprüfungs-Audit und Angriffspunkte Normenkontrolle. Abgrenzung zu artenschutz-naturschutz-planung (Artenschutz) und beteiligung-frueh-foermlich. |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung Dauer 2 plus 1 plus Verlaengerungen Entschaedigung § 18 BauGB. Zurückstellung § 15 BauGB als milderes Mittel. Anfechtung § 47 VwGO oder Inzident. Output: Entschaedigungs- und Anfechtungsanalyse Veraenderungssperre. Abgrenzung zu normenkontrollantrag-schriftsatz (Hauptsache B-Plan) und statthaftigkeit-47-vwgo. |
| `vorhabenbezogener-bebauungsplan-12-baugb` | Prüffeld für vorhabenbezogener bebauungsplan 12 baugb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Umweltbericht Umweltpruefung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `umweltbericht-umweltpruefung`

**Fokus:** Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden Wasser Luft Klima Landschaft Kultur Nullvariante Alternativen FFH-Vertraeglichkeit § 1a Abs. 4 BauGB. Beschleunigtes Verfahren § 13a BauGB ohne Umweltprüfung. Output: Umweltprüfungs-Audit und Angriffspunkte Normenkontrolle. Abgrenzung zu artenschutz-naturschutz-planung (Artenschutz) und beteiligung-frueh-foermlich.

# Umweltbericht und Umweltprüfung

## Zweck

Der Umweltbericht ist nach dem Abwägungsgebot eines der wichtigsten Prüffelder. Fehler hier wirken doppelt: als Verfahrensfehler bei der Beteiligung und als materieller Abwägungsfehler.

## Schritt 1 — Pflicht zur Umweltprüfung § 2 Abs. 4 BauGB

### Grundregel
- Bei jedem B-Plan ist eine Umweltprüfung durchzuführen
- Die Ergebnisse werden im Umweltbericht zusammengestellt
- Umweltbericht ist Bestandteil der Begründung § 2a S. 2 Nr. 2 BauGB
- Auslegung gemeinsam mit Planentwurf § 3 Abs. 2 BauGB

### Schutzgüter § 2 Abs. 4 S. 1 BauGB
- Mensch und menschliche Gesundheit
- Tiere, Pflanzen, biologische Vielfalt
- Fläche, Boden, Wasser, Luft, Klima
- Landschaft
- Kultur- und Sachgüter
- Wechselwirkungen zwischen diesen Schutzgütern

## Schritt 2 — Scoping

### Festlegung Untersuchungsrahmen § 4 Abs. 1 BauGB
- Frühzeitige Behördenbeteiligung
- Behörden teilen mit, welche Informationen sie für die Umweltprüfung als erforderlich halten
- Gemeinde legt Untersuchungsrahmen fest

### Audit Scoping
- Wurde Scoping durchgeführt? Niederschrift?
- Wer war beteiligt? Untere Naturschutzbehörde, Wasserwirtschaftsamt, Untere Bauaufsicht?
- Wurden die Hinweise der Behörden in den Umweltbericht aufgenommen?
- Liegen Stellungnahmen der Träger öffentlicher Belange schriftlich vor?

## Schritt 3 — Inhalt Umweltbericht (Anlage 1 zu BauGB)

### Pflichtinhalte
- Einleitung mit Beschreibung der Festsetzungen, Ziele und Standortmerkmalen
- Bestandsaufnahme der Umwelt
- Prognose der Umweltauswirkungen
- Geprüfte Alternativen einschließlich Nullvariante
- Maßnahmen zur Vermeidung, Verringerung und zum Ausgleich
- Allgemein verständliche Zusammenfassung
- Monitoring-Konzept

### Häufige Lücken
- Bestandsaufnahme veraltet (mehr als 5 Jahre alt)
- Prognose ohne Berechnung, nur Behauptung
- Alternativen nur formelhaft erwähnt
- Nullvariante nicht ernsthaft erörtert
- Monitoring fehlt

## Schritt 4 — Eingriffsregelung § 1a Abs. 3 BauGB

### Vermeidung-Minimierung-Ausgleich
- Eingriffe in Natur und Landschaft sind zu vermeiden
- Unvermeidbare Eingriffe sind zu minimieren
- Verbleibende Eingriffe sind auszugleichen oder zu ersetzen

### Bilanzierung
- Eingriffs-Ausgleichs-Bilanz mit Punkten/Werten
- Häufig in Anlage zum Umweltbericht
- Audit auf Plausibilität und Aktualität

### Ausgleichsflächen
- Räumliche und funktionale Zuordnung
- Sicherstellung dauerhaft
- Häufig externe Ausgleichsflächen im Pool

## Schritt 5 — Schutzgut Klima und Klimaschutz

### Klimaschutz § 1 Abs. 5 BauGB
- Bauleitpläne sollen den Klimaschutz und die Klimaanpassung berücksichtigen
- Seit 2011 ausdrücklich

### Stadtklimatische Untersuchung
- Bei großen Plänen in dicht besiedelten Gebieten — Stadtklima-Gutachten erforderlich
- Hitzeinseln, Frischluftschneisen, Kaltluft-Abfluss
- Augsburg: Lechfelder Frischluftbahn

### Häufige Treffer
- Fehlende Klimauntersuchung trotz Verdichtung
- Versiegelungsgrad ohne klimatische Bewertung
- Begrünungsmaßnahmen unklar quantifiziert

## Schritt 6 — FFH-Vorprüfung § 1a Abs. 4 BauGB i.V.m. § 34 BNatSchG

### Pflicht
- Wenn das Plangebiet ein FFH-Gebiet oder Vogelschutzgebiet ist oder daran angrenzt
- Vorprüfung auf erhebliche Beeinträchtigung von Schutz- und Erhaltungszielen
- Bei Vorprüfungs-Bejahung volle FFH-Verträglichkeitsprüfung

### Bei Verzicht
- Begründungspflicht: warum keine erhebliche Beeinträchtigung
- Inhaltliche Substanz erforderlich, nicht bloße Floskel

## Schritt 7 — Spezielle artenschutzrechtliche Prüfung (saP)

### § 44 BNatSchG
- Zugriffsverbote für besonders geschützte Arten
- Bei B-Plan-Aufstellung muss saP durchgeführt werden
- Liste der relevanten Arten je nach Standort

### Häufige Arten in Stadtgebieten
- Mauersegler, Schwalben, Spatzen — gebäudebrütend
- Fledermäuse — Quartierwechsel, Wochenstuben
- Eidechsen, Zauneidechse — bei Brachflächen
- Pflanzenarten bei Renaturierungsflächen

### Audit saP
- Wurde saP durchgeführt? Datierung?
- Wer hat sie erstellt? Sachverständige?
- Begehung im richtigen Zeitraum?
- Sind die einschlägigen Arten erfasst?

## Schritt 8 — Verzahnung UVPG

### UVPG-relevante Pläne
- Wenn ein Vorhaben im Plangebiet UVP-pflichtig wäre
- Z.B. größere Verkehrsanlagen, Einzelhandelsprojekte ab Schwellenwert
- UVPG Anlage 1

### Verzicht im B-Plan
- Wird im B-Plan eine UVP-pflichtige Anlage zugelassen, muss UVP-Prüfung integriert werden
- Verzicht ist beachtlicher Fehler

## Schritt 9 — Beschleunigtes Verfahren § 13a BauGB

### Voraussetzung
- B-Plan der Innenentwicklung
- Grundfläche unter 20.000 m² (oder bis 70.000 m² bei Vorprüfung)
- Keine Verpflichtung zur Umweltprüfung
- Aber Umweltbericht entfällt nicht ohne weiteres

### Häufige Treffer
- § 13a missbräuchlich gewählt
- Grundfläche über Schwelle
- Tatsächlich keine reine Innenentwicklung
- Vorprüfung nicht durchgeführt

## Schritt 10 — Audit-Checkliste Umweltbericht

| Punkt | Prüfung |
|---|---|
| Scoping dokumentiert? | Ja/nein |
| Alle Schutzgüter behandelt? | Ja/nein |
| Bestandsaufnahme aktuell? | Ja/nein |
| Prognose belastbar? | Ja/nein |
| Alternativen geprüft inkl. Nullvariante? | Ja/nein |
| Eingriffs-Ausgleichs-Bilanz plausibel? | Ja/nein |
| Klima-Untersuchung vorhanden? | Ja/nein |
| FFH-Vorprüfung erforderlich? Durchgeführt? | Ja/nein |
| saP durchgeführt? | Ja/nein |
| UVPG-Prüfung integriert? | Ja/nein |
| Monitoring-Konzept? | Ja/nein |

## Quellen

- BauGB §§ 1 1a 2 2a 3 4 13a Anlage 1
- BNatSchG §§ 34 44
- UVPG (BGBl. I 2017 S. 2808 zuletzt geändert)
- BVerwG, Urteil vom 24.3.2010 – 4 CN 3.09 (Umweltbericht)
- BVerwG, Urteil vom 9.4.2008 – 4 CN 1.07 (saP B-Plan)

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `veraenderungssperre-zurueckstellung-14-15-baugb`

**Fokus:** Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung Dauer 2 plus 1 plus Verlaengerungen Entschaedigung § 18 BauGB. Zurückstellung § 15 BauGB als milderes Mittel. Anfechtung § 47 VwGO oder Inzident. Output: Entschaedigungs- und Anfechtungsanalyse Veraenderungssperre. Abgrenzung zu normenkontrollantrag-schriftsatz (Hauptsache B-Plan) und statthaftigkeit-47-vwgo.

# Veränderungssperre und Zurückstellung — §§ 14, 15 BauGB

## Zweck

Während der Bauleitplanung kann die Gemeinde die Realisierung von Bauvorhaben, die der Plan-Entwicklung widersprechen würden, sichern — durch Veränderungssperre § 14 BauGB oder Zurückstellung § 15 BauGB. Beide Instrumente sind sowohl von Behörden- als auch von Bauherren-/Nachbarseite zu prüfen.

## Eingaben

- Plan-Stand (Aufstellungsbeschluss vorhanden? Konkretisierungs-Stand?)
- Vorhandensein konkreter Bauanträge / Bauvoranfragen
- Bestehende Veränderungssperre oder Zurückstellung?
- Dauer bisheriger Sicherungs-Maßnahmen
- Vertragslage (Durchführungsvertrag mit Vorhabenträger?)

## Schritt 1 — Veränderungssperre § 14 BauGB

### Voraussetzungen

a) **Aufstellungsbeschluss** für Bebauungsplan, der für das Gebiet gelten soll
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
c) **Sicherungs-Bedürfnis** zur Wahrung der Plan-Ziele

### Inhalt § 14 Abs. 1 BauGB

Während der Sperre dürfen nicht durchgeführt werden:

a) Vorhaben im Sinne des § 29 BauGB
b) erhebliche oder wesentliche wertsteigernde Veränderungen von Grundstücken (Hilfsweise Erläuterungs-Sperre)

### Ausnahmen § 14 Abs. 2 BauGB

- Wenn das Vorhaben den Zielen des Bebauungsplans nicht entgegensteht
- Ausnahme-Erteilung durch Gemeinde im Einzelfall

### Dauer § 17 BauGB

- **Zwei Jahre** Regelfall
- **Plus ein Jahr** Verlängerung möglich (Stadtratsbeschluss)
- **Plus ein weiteres Jahr** bei besonderen Umständen (insgesamt max. vier Jahre)

### Beschluss und Bekanntmachung

- Stadtratsbeschluss erforderlich
- Bekanntmachung wie Bebauungsplan-Satzung (§ 14 Abs. 4 BauGB iVm § 10 BauGB)
- Mit Bekanntmachung Wirkung

## Schritt 2 — Zurückstellung § 15 BauGB

### Voraussetzungen

a) **Aufstellungsbeschluss** liegt vor
b) **Konkretes Bauvorhaben** angemeldet (Bauantrag, Bauvoranfrage)
c) **Befürchten** dass das Vorhaben die Plan-Entwicklung gefährdet

### Mildere Maßnahme zur Veränderungssperre

- Gilt nur für einzelne, konkrete Vorhaben
- Antrag des Bauherrn wird **zurückgestellt** (nicht beschieden)
- Bauherr kann nicht weiter realisieren bis Ende der Zurückstellung

### Dauer

- **Maximal zwölf Monate** (§ 15 Abs. 1 Satz 2 BauGB)
- **Verlängerung um sechs Monate** bei besonderen Umständen (§ 15 Abs. 1 Satz 3)
- Insgesamt 18 Monate

### Rechtsfolgen

- Bauherr behält Antragsrecht — wird nur ausgesetzt
- Nach Ablauf der Zurückstellung muss beschieden werden
- Bei Plan-Beschluss vor Ablauf: Bescheidung nach neuem Plan
- Bei Plan-Verzögerung über Frist hinaus: Bescheidung nach altem Recht

## Schritt 3 — Entschädigungs-Pflicht § 18 BauGB

### Voraussetzungen

- Veränderungssperre länger als **vier Jahre** in Kraft
- Eigentümer hat zumutbare Nutzungsmöglichkeiten verloren
- Anspruch auf Entschädigung nach § 42 BauGB analog

### Bemessung

- Wertminderung im Sinne der Eigentumsgarantie
- Wirtschaftliche Folgen für Eigentümer
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 4 — Wirkung auf Vorhabenträger / Bauherrn

### Bei bestehender Veränderungssperre

- **Kein neuer Bauantrag möglich** im gesperrten Gebiet (außer Ausnahme-Erteilung § 14 Abs. 2)
- Bauanträge werden abgelehnt oder zurückgestellt
- Wirtschaftliche Folge erheblich (Finanzierungs-Kosten)

### Bei Zurückstellung

- Bauantrag bleibt anhängig, aber wird nicht beschieden
- Bauherr kann auf Bescheidung klagen (Untätigkeits-Klage § 75 VwGO)

### Bei "vertraglich-faktischer Sperre"

- Stadt hat keine § 14-Sperre erlassen, aber durch Durchführungs-Vertrag Konkurrenz-Vorhaben praktisch ausgeschlossen
- Rechtsschutz dann schwieriger
- Argumentation: städtebaulicher Vertrag bewirkt Vorprägung

## Schritt 5 — Anfechtung Veränderungssperre

### Statthafter Rechtsweg

- **Normenkontrollantrag** § 47 VwGO (Veränderungssperre ist Satzung)
- **Inzident** im Anfechtungsverfahren gegen Bauablehnung
- **Untätigkeits-Klage** bei Zurückstellung mit Bauantrag-Druck

### Begründetheit-Punkte

#### Aufstellungsbeschluss formal mangelhaft

- Bekanntmachungs-Fehler
- Beschluss-Fehler

#### Konkretisierungs-Mangel

- Plan-Ziele zu unbestimmt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Verhältnismäßigkeit

- Maßnahme nicht erforderlich
- Mildere Mittel verfügbar (z.B. Zurückstellung)
- Übermäßige Geltungsdauer

#### Entschädigungs-Frage

- Bei längerer Dauer (über vier Jahre) Anspruch nach § 18 BauGB

## Schritt 6 — Prüfraster aus Bauherrn-Sicht

### Erste Schritte bei Sperre

- Bekanntmachungs-Daten prüfen (Beginn, voraussichtliches Ende)
- Aufstellungsbeschluss anfordern (Akteneinsicht)
- Konkretisierungs-Stand bewerten

### Optionen

- **Ausnahme-Antrag § 14 Abs. 2 BauGB** wenn Vorhaben nicht plan-widrig
- **Anfechtung** der Sperre wenn formal mangelhaft
- **Entschädigungs-Antrag** nach Ablauf vier Jahre
- **Verkauf** des Vorhabens wenn Realisierungs-Verzögerung unzumutbar

## Schritt 7 — Prüfraster aus Nachbar-Sicht

### Bei Bauantrag des Nachbarn trotz Plan-Verfahrens

- Wird die Bau-Genehmigung trotz laufendem Plan-Verfahren erteilt?
- Hat die Gemeinde Veränderungssperre / Zurückstellung erwogen?
- Wenn nicht: warum nicht?

### Argumentation gegen Bau-Genehmigung

- Gemeinde hat trotz drohender Plan-Widrigkeit nicht zurückgestellt
- Bauherr profitiert vom "dem ersten kommt das Recht"
- Bei plangleichem Vorhaben Indiz für Gefälligkeitsplanung

## Schritt 8 — Stadtplanungs-Sicht

### Sicherung der Plan-Entwicklung

- Bei Plan-Beginn früh erwägen
- Veränderungssperre eher als Schutz
- Bei einzelnem konkreten Konflikt-Vorhaben: Zurückstellung

### Risiken Veränderungssperre

- Bei Anfechtung Sperre-Fall
- Entschädigungs-Pflicht ab vier Jahren
- Imageschaden bei zu strenger Anwendung

## Schritt 9 — Konkurrenz zu privatrechtlichen Sicherungs-Instrumenten

### Vertragliche Sicherung

- Bei Durchführungs-Vertrag mit Vorhabenträger faktische Sperre für andere
- Aber keine Veränderungssperre im rechtlichen Sinne
- Folge: Konkurrenz-Vorhaben können trotzdem beantragen

### Vorkaufsrecht § 24 BauGB

- Allgemeines Vorkaufsrecht der Gemeinde
- Bei privater Veräußerung im Plangebiet
- Sicherung Plan-Entwicklung möglich

## Schritt 10 — Verfahren bei Klage

### Inzidente Prüfung

- In Bauablehnungs-Klage Verwaltungsgericht
- Veränderungssperre wird auf Wirksamkeit geprüft
- Bei Unwirksamkeit Bauantrag zu bescheiden nach altem Recht

### Normenkontrollantrag

- Vor OVG / VGH
- Frist ein Jahr § 47 Abs. 2 VwGO
- Antragsbefugnis: Eigentümer im Sperre-Gebiet, Nachbarn mit konkreter Beeinträchtigung

### Eilantrag § 47 Abs. 6 VwGO

- Aufschiebende Wirkung gegen Sperre
- Bei Eilbedürftigkeit (z.B. Genehmigungs-Frist läuft)

## Schritt 11 — Anwendung auf Bebauungsplan Augsburg Nr. 900

**Erkenntnis aus dem Fall:**

Die Stadt Augsburg hat **keine Veränderungssperre** im Bahnhofsviertel West verhängt. Stattdessen sicherte sie die Plan-Entwicklung durch den **Durchführungs-Vertrag vom 12.05.2022** — faktische Sperre.

**Bewertung:**

a) Die Stadt hätte rechtlich die Möglichkeit gehabt, mit Aufstellungs-Beschluss 14.06.2022 zugleich eine Veränderungssperre nach § 14 BauGB zu erlassen.

b) Sie hat darauf verzichtet, weil der Vorhabenträger einziger relevanter Eigentümer der Plan-Flächen war.

c) Stattdessen hat sich die Stadt durch den Durchführungs-Vertrag faktisch gebunden — und damit den Schutz vor Konkurrenz-Vorhaben durch privatrechtliche Vereinbarung erreicht.

d) Damit: **kein § 14-Verfahren möglich**, aber **Indiz für Gefälligkeitsplanung** im Hauptsache-Verfahren.

**Bauantrag MU 3 vom 02.07.2024** des Vorhabenträgers — **18 Tage nach Bekanntmachung**:

- Vorhabenträger nutzt schnelle Anschluss-Realisierung
- Erschwert Eilantrag im Normenkontroll-Verfahren (Vollzugs-Folge bereits eingetreten?)
- Begründet aber gerade die Eilbedürftigkeit für Antragstellerseite

## Verzahnung mit anderen Skills

- `aufstellungsbeschluss-bekanntmachung`
- `vorhabenbezogener-bebauungsplan-12-baugb`
- `einstweilige-anordnung-47-abs-6-vwgo`
- `mandat-erstgespraech-normenkontrolle`

## Quellen

- BauGB §§ 14, 15, 17, 18, 24, 42
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Ernst/Zinkahn/Bielenberg BauGB
- Battis/Krautzberger/Löhr BauGB

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `vorhabenbezogener-bebauungsplan-12-baugb`

**Fokus:** Prüffeld für vorhabenbezogener bebauungsplan 12 baugb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Vorhabenbezogener Bebauungsplan § 12 BauGB

## Zweck

Bei vielen Plänen ist die Frage zentral, ob es sich um einen qualifizierten Bebauungsplan oder einen vorhabenbezogenen Bebauungsplan (VEP) handelt. Die Abgrenzung hat erhebliche Folgen für Aktivlegitimation, Anfechtbarkeit, Realisierungs-Pflicht und Beendigung.

## Eingaben

- Bebauungsplan-Bezeichnung und Beschluss-Datum
- Vorhandensein eines Durchführungsvertrags / Erschließungsvertrags
- Identität Vorhabenträger und Grundstücks-Eigentümer
- Förmliche Erklärung im Plan, ob VEP oder qualifizierter B-Plan

## Schritt 1 — Drei-Säulen-Konstruktion VEP

Ein VEP setzt **drei verknüpfte Akte** voraus:

1. **Vorhaben- und Erschließungsplan (VEP)** — vom Vorhabenträger aufgestellt, mit konkretem Bauvorhaben (Geometrie, Nutzung, Erschließung) statt nur Festsetzungen
2. **Durchführungsvertrag** zwischen Stadt und Vorhabenträger — verpflichtet zur Plan-Umsetzung
3. **Satzung** der Gemeinde — übernimmt den VEP als Festsetzungs-Grundlage

Fehlt eine Säule, ist es kein VEP. Fehlt der Plan im förmlichen Sinne und die Satzung benennt sich als "normaler" B-Plan, gilt § 11 BauGB für den Vertrag, nicht § 12 BauGB.

## Schritt 2 — Identitäts-Erfordernis

### Vorhabenträger gleich Plan-Schuldner

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Vorhabenträger muss zur Plan-Realisierung **verpflichtet und in der Lage** sein
- Wechselt der Vorhabenträger nach Plan-Beschluss, bleibt der Plan nur wirksam wenn der Nachfolger den Durchführungsvertrag übernimmt
- § 12 Abs. 5 BauGB ausdrücklich

### Wirkung Wechsel ohne Übernahme

- VEP wird unwirksam § 12 Abs. 6 BauGB
- Aufhebungs-Pflicht der Stadt
- Konsequenz für Bauherren / Investoren erheblich

## Schritt 3 — Abgrenzung VEP vs. qualifizierter B-Plan

| Merkmal | VEP § 12 BauGB | qualifizierter B-Plan § 30 BauGB |
|---|---|---|
| Aufsteller | Vorhabenträger reicht Plan ein | Gemeinde stellt selbst auf |
| Inhalt | Konkretes Bauvorhaben | Abstrakte Festsetzungen |
| Vertrag | Durchführungsvertrag zwingend | nicht zwingend, ggf. § 11 BauGB |
| Realisierungspflicht | Vorhabenträger pflicht zur Durchführung | Bauherren frei |
| Wirksamkeit | Hängt an Realisierungs-Vertrag | Unabhängig von einzelner Realisierung |
| § 9 BauGB | nicht abschließend, § 12 Abs. 3 erweitert | abschließend |
| Festsetzung außerhalb § 9 | möglich nach § 12 Abs. 3 | nur § 9 BauGB |

## Schritt 4 — Praktische Konstellationen

### Konstellation A — Ausdrücklicher VEP

- Stadt setzt VEP-Satzung
- Bezeichnung "Vorhabenbezogener Bebauungsplan Nr. X"
- Plan-Urkunde enthält VEP-Bezeichnung
- Durchführungsvertrag in Anlagen aufgeführt
- Vorhabenträger benannt

### Konstellation B — Verdeckter VEP / Mischform

- Stadt setzt qualifizierten B-Plan (kein VEP-Etikett)
- Durchführungsvertrag mit Vorhabenträger vor Aufstellungs-Beschluss
- Festsetzungen sind passgenau auf das Vorhaben des Vorhabenträgers zugeschnitten
- **Rechtsfolge:** Vertrag als § 11 BauGB-Vertrag zu prüfen, nicht § 12 BauGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konstellation C — Reiner Erschließungs-Vertrag

- § 124 BauGB-Vertrag zwischen Stadt und Erschließungs-Träger
- Keine Bauleit-Verzahnung
- VEP nicht einschlägig

### Konstellation D — Sanierungs-/Entwicklungsmaßnahme

- §§ 142 ff. BauGB
- Eigenes Regime
- Nicht VEP

## Schritt 5 — Vor- und Nachteile aus Mandanten-Sicht

### Vorteile VEP für Antragsteller (Anfechtung)

- **Identitäts-Erfordernis** — wenn Vorhabenträger insolvent oder wechselt ohne Übernahme, Plan wird unwirksam
- **Realisierungs-Pflicht** — bei Nicht-Realisierung kann Aufhebungs-Antrag gestellt werden
- **Konkrete Festsetzungen** — leichtere Auseinandersetzung mit konkretem Vorhaben statt mit abstrakten Festsetzungen
- **Vorprägung-Argument** stärker (Vertrag vor Plan)

### Vorteile qualifizierter B-Plan für Stadt

- Nicht an einzelnen Vorhabenträger gebunden
- Auch ohne Realisierung wirksam
- Mehr Festsetzungs-Spielraum

## Schritt 6 — § 11 BauGB städtebaulicher Vertrag

Wenn die Vertragskonstruktion nicht VEP ist, bleibt § 11 BauGB:

- Vertragsformen: Erschließungsvertrag, Folge-Lasten-Vertrag, sonstige städtebauliche Verträge
- **Angemessenheits-Erfordernis** § 11 Abs. 2 BauGB
- **Verbot der Koppelung** mit Plan-Aufstellung in unangemessener Weise
- **Schriftform** § 11 Abs. 3 BauGB

### Angemessenheits-Prüfung

- Verhältnis Vertragsleistung zur Belastung
- Keine Übertragung von hoheitlichen Aufgaben gegen Bauleit-Versprechen
- Bei Erschließungsverträgen Aufwand übersichtlich

### Verletzungs-Folgen

- Vertragsteil nichtig § 134 BGB iVm § 11 Abs. 2 BauGB
- Auswirkung auf Plan: Indiz für Gefälligkeitsplanung, schwerer Abwägungsmangel

## Schritt 7 — Antragsbefugnis und VEP

Die Antragsbefugnis nach § 47 Abs. 2 VwGO ist beim VEP häufig erleichtert:

- Konkrete Festsetzungen erlauben konkrete Betroffenheits-Darstellung
- Eigentümer im Plangebiet stets antragsbefugt
- Nachbarn mit konkreter Beeinträchtigung antragsbefugt
- Bei nicht-VEP gleiche Regel, aber abstrakte Festsetzungen erfordern abstraktere Begründung

## Schritt 8 — Rechtsfolgen Unwirksamkeit § 12 Abs. 6

### Eintritts-Tatbestände

- Vorhabenträger zur Realisierung nicht in der Lage
- Wechsel ohne Übernahme
- Insolvenz Vorhabenträger
- Realisierung in vertraglich vereinbarter Frist nicht erfolgt

### Verfahren

- Stadt hat Aufhebungs-Beschluss zu fassen
- Bekanntmachung gemäß § 10 BauGB
- Frühere Festsetzungen entfallen
- Übergangsregelung für genehmigte Bauvorhaben

### Rechtsschutz

- Antragsteller kann Aufhebungs-Erforderlichkeit feststellen lassen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 9 — Prüfraster für die Mandantin-Vertretung

### Schritt 9.1 — Plan-Identifikation

- Wie bezeichnet sich der Plan? VEP oder qualifizierter B-Plan?
- Liegt ein Durchführungsvertrag vor?
- Ist ein Vorhabenträger benannt?

### Schritt 9.2 — Akten-Studium

- Durchführungsvertrag im Wortlaut anfordern (Akteneinsicht)
- Vergleich Vertragsinhalt mit Plan-Festsetzungen
- Datum-Vergleich Vertrag / Aufstellungsbeschluss

### Schritt 9.3 — Konstellations-Zuordnung

- A, B, C oder D (siehe Schritt 4)
- Bei B (Mischform) Argumentation: § 11 BauGB-Vertrag mit Vorgabe-Wirkung

### Schritt 9.4 — Argumentations-Linien

- Bei VEP: Vorhabenträger-Identität, Realisierungs-Status, Wirksamkeits-Folgen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Stets Vorprägungs-Argument

## Schritt 10 — Anwendung auf Bebauungsplan Augsburg Nr. 900

**Beispiel-Akte:** Bebauungsplan Nr. 900 Augsburg-Bahnhofsviertel West

**Konstellation:** verdeckte Mischform (Konstellation B)

- Bezeichnung: qualifizierter B-Plan ("Bebauungsplan Nr. 900")
- Vorhabenträger: Bahnhofsquartier Augsburg GmbH & Co. KG
- Durchführungsvertrag vom 12.05.2022 (vor Aufstellungsbeschluss 14.06.2022)
- Notarielle Ergänzung 18.07.2022 ohne tatsächlichen VEP-Beschluss
- Vertrag-Inhalt: konkrete Geschoßzahlen, Stellplatz-Schlüssel, Tiefgaragenzufahrt — alle Eckwerte schon vor Plan

**Argumentations-Linien für Antragstellerseite:**

1. **§ 11 BauGB-Vertrag** mit konkreter Vorprägung der Plan-Inhalte
2. **Angemessenheits-Frage** § 11 Abs. 2 BauGB nicht geprüft
3. **Vertrags-§ 14 nennt VEP-Ergänzung**, aber diese ist nie förmlich beschlossen — Inkonsistenz
4. **Identitäts-Erfordernis** und Mobilitätskonzept-Verpflichtungen ohne dingliche Sicherung der Übertragung auf Nachfolge-Eigentümer
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Verzahnung mit anderen Skills

- `abwaegungsgebot-1-abs-7-baugb` — Vorprägung als Abwägungsausfall
- `erforderlichkeit-1-abs-3-baugb` — Gefälligkeitsplanung
- `normenkontrollantrag-schriftsatz` — Argumentations-Strukturen
- `antragsbefugnis-eigentuemer-nachbar` — VEP-spezifische Konstellationen

## Quellen (Stand 05/2026)

- BauGB §§ 11, 12, 30
- **BVerwG 18.09.2003, 4 CN 3.02** — VEP § 12 BauGB; Drei-Saeulen-Konstruktion (bverwg.de)
- **BVerwG 06.06.2019, 4 CN 7.18** — Anforderungen an Konkretisierung Vorhaben im VEP (bverwg.de)
- **BVerwG 04.05.2022, 4 CN 2.21** — Konzentrationszonenplanung Wind/Solar (bverwg.de)
- Konkrete weitere Aktenzeichen vor Ausgabe per bverwg.de mit Datum verifizieren
- Battis/Krautzberger/Löhr BauGB
- Ernst/Zinkahn/Bielenberg BauGB

## Ergänzende Rechtsprechung

- BVerwG 06.06.2019, 4 CN 7.18 — VEP-Konkretisierung (bverwg.de)
- BVerwG 11.04.2024, 4 BN 50.23 — Klimaschutz § 1 Abs. 5 S. 2 BauGB Abwaegungsmaengel (bverwg.de)
- Weitere Aktenzeichen vor Ausgabe per bverwg.de verifizieren

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
