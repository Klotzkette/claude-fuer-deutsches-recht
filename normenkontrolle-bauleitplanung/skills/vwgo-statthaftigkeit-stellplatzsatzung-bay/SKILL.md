---
name: vwgo-statthaftigkeit-stellplatzsatzung-bay
description: "Vwgo Statthaftigkeit Stellplatzsatzung BAY: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vwgo Statthaftigkeit Stellplatzsatzung BAY

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vwgo Statthaftigkeit Stellplatzsatzung BAY** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-vwgo-schriftsatz-brief-und-memo-bausteine` | VwGO: Schriftsatz-, Brief- und Memo-Bausteine im Plugin normenkontrolle bauleitplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `statthaftigkeit-47-vwgo` | Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12 BauGB § 13a-B-Plan örtliche Bauvorschriften Art. 81 BayBO FNP grundsaetzlich nicht statthaft (Ausnahme Konzentrationsflaeche § 35 Abs. 3 S. 3 BauGB) Inkrafttreten Norm. Output: Statthaftigkeits-Entscheidung. Abgrenzung zu antragsbefugnis-eigentuemer-nachbar (Befugnis) und jahresfrist-47-abs-2-vwgo (Frist). |
| `stellplatzsatzung-bay-bauordnung` | Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch örtliche Bauvorschrift sachliche Rechtfertigung Mobilitaetskonzept Parkdruck-Verlagerung Stellplatzbilanz. Output: Stellplatzsatzungs-Prüfprotokoll und Angriffspunkt Normenkontrolle. Abgrenzung zu festsetzungskatalog-9-baugb-baunvo (Festsetzungen gesamt) und normenkontrollantrag-schriftsatz. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Vwgo Statthaftigkeit Stellplatzsatzung BAY**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-vwgo-schriftsatz-brief-und-memo-bausteine`

**Fokus:** VwGO: Schriftsatz-, Brief- und Memo-Bausteine im Plugin normenkontrolle bauleitplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# VwGO: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: VwGO: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** VwGO: Schriftsatz-, Brief- und Memo-Bausteine / vwgo schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VwGO, OVG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **VwGO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `statthaftigkeit-47-vwgo`

**Fokus:** Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12 BauGB § 13a-B-Plan örtliche Bauvorschriften Art. 81 BayBO FNP grundsaetzlich nicht statthaft (Ausnahme Konzentrationsflaeche § 35 Abs. 3 S. 3 BauGB) Inkrafttreten Norm. Output: Statthaftigkeits-Entscheidung. Abgrenzung zu antragsbefugnis-eigentuemer-nachbar (Befugnis) und jahresfrist-47-abs-2-vwgo (Frist).

# Statthaftigkeit § 47 VwGO

## Zweck

Klärung, ob die angegriffene Vorschrift überhaupt Gegenstand eines Normenkontrollverfahrens sein kann. Statthaftigkeit ist die erste der vier Zulässigkeits-Säulen und wird vor Antragsbefugnis, Frist und Rechtsschutzbedürfnis geprüft.

## Schritt 1 — Grundtatbestand § 47 Abs. 1 VwGO

### Wortlaut sinngemäß
- Das Oberverwaltungsgericht entscheidet im Rahmen seiner Gerichtsbarkeit auf Antrag über die Gültigkeit
- **Nr. 1**: von Satzungen, die nach den Vorschriften des Baugesetzbuchs erlassen sind, sowie von Rechtsverordnungen aufgrund § 246 Abs. 2 BauGB
- **Nr. 2**: von anderen im Rang unter dem Landesgesetz stehenden Rechtsvorschriften, sofern das Landesrecht dies bestimmt

### Bayerische Landesregelung
- Art. 5 BayAGVwGO erweitert die Statthaftigkeit auf andere im Rang unter dem Landesgesetz stehende Rechtsvorschriften
- Damit auch örtliche Bauvorschriften, kommunale Satzungen, Verordnungen erfasst

## Schritt 2 — Bebauungsplan als Satzung

### Klassischer qualifizierter B-Plan
- Erlassen als Satzung der Gemeinde § 10 Abs. 1 BauGB
- Mindestfestsetzungen Art Maß Bauweise überbaubare Grundstücksfläche § 30 Abs. 1 BauGB
- Statthaftigkeit unproblematisch

### Einfacher B-Plan
- Festsetzungen unterhalb des qualifizierten Maßes
- § 30 Abs. 3 BauGB
- Trotzdem Satzung und statthaft

### Vorhabenbezogener B-Plan § 12 BauGB
- Vorhaben- und Erschließungsplan plus B-Plan
- Wird als Satzung beschlossen § 10 BauGB
- Statthaft

### B-Plan der Innenentwicklung § 13a BauGB
- Beschleunigtes Verfahren
- Verzicht auf Umweltprüfung im Einzelfall möglich
- Trotzdem Satzung und statthaft
- Häufiger Angriffspunkt: zu Unrecht beschleunigtes Verfahren gewählt

### Vereinfachtes Verfahren § 13 BauGB
- Bei Änderungen oder Ergänzungen die Grundzüge nicht berühren
- Auch hier Satzung — Statthaftigkeit gegeben

## Schritt 3 — Örtliche Bauvorschriften Art. 81 BayBO

### Statthaftigkeitsgrundlage
- Art. 81 BayBO ermächtigt zu örtlichen Bauvorschriften als Satzung
- Insbesondere Stellplatzsatzung Art. 81 Abs. 1 Nr. 4 BayBO
- Gestaltungssatzung Art. 81 Abs. 1 Nr. 1 BayBO
- Werbeanlagensatzung Art. 81 Abs. 1 Nr. 2 BayBO
- Satzungsform — Statthaftigkeit unproblematisch nach § 47 Abs. 1 Nr. 2 VwGO i.V.m. Art. 5 BayAGVwGO

### Kombination mit B-Plan
- Häufig erlässt Gemeinde mit dem B-Plan zugleich örtliche Bauvorschriften in derselben Satzung
- Beide separat angreifbar — getrennte Anträge sinnvoll wenn Mängel unterschiedlich
- Im Praxisfall ein einheitlicher Antrag mit getrennten Begründungsabschnitten

## Schritt 4 — Flächennutzungsplan grundsätzlich nicht statthaft

### Regelfall
- FNP ist Selbstbindung der Gemeinde, kein Rechtsetzungsakt mit Außenwirkung
- Bürger kann sich nicht unmittelbar darauf berufen
- BVerwG, Urteil vom 26.4.2007 – 4 CN 3.06 (st. Rspr.)
- Normenkontrolle gegen FNP regelmäßig unstatthaft

### Ausnahme Außenwirkung
- FNP-Darstellungen mit gesteigerter Außenwirkung sind statthaft
- Konzentrationsflächen für Windenergie § 35 Abs. 3 S. 3 BauGB
- BVerwG, Urteil vom 26.4.2007 – 4 CN 3.06 (Wendepunkt)
- Hier ist Normenkontrolle gegen FNP statthaft

### Inzident-Kontrolle
- Wenn FNP nicht direkt angegriffen werden kann, gelegentlich Inzident-Kontrolle im Rahmen B-Plan-Normenkontrolle möglich (Anpassungsgebot § 8 Abs. 2 BauGB)

## Schritt 5 — Inkrafttreten der Norm

### Voraussetzung Bekanntmachung
- B-Plan tritt mit Bekanntmachung in Kraft § 10 Abs. 3 BauGB
- Ohne Inkrafttreten kein Normenkontrollgegenstand — Antrag wäre verfrüht
- Aufstellungsbeschluss alleine reicht nicht

### Nachträgliche Außerkraftsetzung
- Wird der Plan aufgehoben oder ersetzt, entfällt das Rechtsschutzbedürfnis nicht zwangsläufig (Fortsetzungsfeststellungsinteresse möglich)

## Schritt 6 — Abgrenzungen

### Gegen Baugenehmigung
- Wenn nur die konkrete Genehmigung stört — Anfechtungsklage gegen die Genehmigung
- Inzident-Kontrolle des B-Plans im Anfechtungsprozess möglich
- Parallel-Strategie: Normenkontrolle plus Anfechtung

### Gegen Vorhabenbezogenen Durchführungsvertrag § 12 Abs. 1 S. 1 BauGB
- Vertrag selbst nicht direkter Antragsgegenstand
- Aber als Indiz für Vorfestlegung Stadt relevant für materielle Begründung

### Gegen städtebaulichen Vertrag § 11 BauGB
- Vertrag selbst nicht Antragsgegenstand
- Inhalt im Rahmen Abwägungsprüfung relevant

## Schritt 7 — Antrags-Bezeichnung im Schriftsatz

### Präzise Antrags-Fassung
- "Der Bebauungsplan Nr. X der Stadt Y mit dem Namen Z, bekanntgemacht im Amtsblatt der Stadt Y Nr. A vom B, wird für unwirksam erklärt."
- Bei Teilangriff: "Der Bebauungsplan Nr. X wird in Bezug auf die textliche Festsetzung Nr. Y für unwirksam erklärt."
- Teilangriff nur wenn restlicher Plan ohne den angegriffenen Teil sinnvoll bleibt (BVerwG-Linie zur Teilbarkeit)

## Schritt 8 — Häufige Statthaftigkeits-Fallen

- Mandant will FNP angreifen — Aufklärung erforderlich
- Plan ist noch nicht in Kraft — Beschluss abwarten oder Eilantrag prüfen
- Plan ist bereits aufgehoben — Fortsetzungsfeststellungsinteresse prüfen
- Angegriffen wird städtebaulicher Vertrag oder Durchführungsvertrag — Hinweis Mandant
- Plan eines anderen Bundeslandes — andere Landesregelung prüfen

## Quellen

- VwGO § 47 Abs. 1, Abs. 2, Abs. 6
- BauGB §§ 8 10 11 12 13 13a 30 35 246
- BayAGVwGO Art. 5
- BayBO Art. 81
- BVerwG, Urteil vom 26.4.2007 – 4 CN 3.06 (FNP Windenergie Konzentration)
- BVerwG, Urteil vom 18.11.2010 – 4 CN 3.10 (Präklusion)
- BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16 (Antragsbefugnis Nachbar)

## Ergänzende Rechtsprechung (Stand 05/2026, verifiziert bverwg.de)

- **BVerwG 14.10.2020, 4 CN 4.19**: Antragsbefugnis im Normenkontrollverfahren — § 47 Abs. 2 VwGO setzt Geltendmachung einer moeglichen Rechtsverletzung voraus; abwaegungsfehlerhafte Plaene begruenden Antragsbefugnis, wenn der Antragsteller einen abwaegungserheblichen Belang geltend macht. Quelle: bverwg.de.
- **BVerwG 04.05.2022, 4 CN 2.21**: Konzentrationszonen-Bauleitplanung (Wind/Solar) — Anforderungen an Statthaftigkeit und Antragsbefugnis von Nachbarn ausserhalb der Konzentrationszone. Quelle: bverwg.de.
- **BVerwG 11.04.2024, 4 BN 50.23**: Klimaschutz als Abwaegungs- und ggf. Antragsbefugnis-relevanter Belang. Quelle: bverwg.de.

Konkrete Aktenzeichen vor Ausgabe per bverwg.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `stellplatzsatzung-bay-bauordnung`

**Fokus:** Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch örtliche Bauvorschrift sachliche Rechtfertigung Mobilitaetskonzept Parkdruck-Verlagerung Stellplatzbilanz. Output: Stellplatzsatzungs-Prüfprotokoll und Angriffspunkt Normenkontrolle. Abgrenzung zu festsetzungskatalog-9-baugb-baunvo (Festsetzungen gesamt) und normenkontrollantrag-schriftsatz.

# Stellplatzsatzung — Art. 47 BayBO

## Zweck

Stellplatzfragen sind ein Hauptkampffeld bei Innenstadt-Verdichtungen. Reduzierte Stellplatzschlüssel führen häufig zu Parkdruck-Verlagerung in Wohnstraßen — abwägungserheblicher Belang der Mandantenseite.

## Schritt 1 — Grundregel Art. 47 BayBO

### Stellplatzpflicht
- Bei der Errichtung von baulichen Anlagen sind Stellplätze in ausreichender Zahl auf dem Baugrundstück oder in zumutbarer Entfernung herzustellen

### Bemessungsgrundlage
- Ein Stellplatz je Wohnung als Grundwert
- Bei Nicht-Wohnnutzung nach Verwaltungsvorschriften
- Konkrete Zahl in Garagen- und Stellplatzverordnung (GaStellV) oder kommunaler Satzung

## Schritt 2 — Reduzierung durch örtliche Bauvorschrift Art. 81 Abs. 1 Nr. 4 BayBO

### Befugnis
- Gemeinden können durch örtliche Bauvorschrift die notwendige Zahl der Stellplätze abweichend von Art. 47 Abs. 1 und 2 BayBO festsetzen

### Reduzierungsfaktoren
- 0,5 typisch in innerstädtischen Quartieren mit guter ÖPNV-Anbindung
- 0,3 sehr ambitionierte Reduzierung
- 0,1 Pilotprojekte autoarmes Wohnen

### Voraussetzungen
- Sachliche Rechtfertigung erforderlich
- Empirische Datenbasis
- Begründung in der Satzung oder Plan-Begründung

## Schritt 3 — Mobilitätskonzept als Voraussetzung

### Anforderungen Mobilitätskonzept
- Substanzielle Untersuchung Bewohnerverhalten
- ÖPNV-Anbindung — Frequenz, Erreichbarkeit, Tarifsystem
- Fahrradinfrastruktur — Abstellplätze, Wege, Diebstahlsicherung
- Car-Sharing-Stationen vor Ort
- Lieferverkehr und Müllabfuhr
- Bewohnerparken-Regelung
- Notfall- und Rettungsanfahrt

### Verbindlichkeit
- Mobilitätskonzept muss in textlichen Festsetzungen abgesichert sein, sonst leeres Versprechen
- Häufige Treffer:
 - Konzept nicht in Festsetzungen übernommen
 - Konzept verweist nur auf "Bemühungen"
 - Vermieter-/Bauträger-Konzepte ohne rechtliche Bindung

## Schritt 4 — Verkehrsmodellierung

### Anforderung
- Verkehrsuntersuchung mit Prognose Mehrverkehr
- Berücksichtigung Pendler, Anwohner, Besucher
- Spitzenzeit-Analyse
- Worst-case-Annahmen statt Bestcase

### Audit
- Wer hat das Gutachten erstellt? Investor-Beauftragung?
- Sind die Annahmen plausibel?
- Sind reale ÖPNV-Frequenzen berücksichtigt?
- Sind Sonderveranstaltungen am Standort berücksichtigt?

## Schritt 5 — Parkdruck-Verlagerung

### Verbraucherbelang Anwohner
- Bestehende Anwohner haben einen abwägungserheblichen Belang, dass nicht das Parkraumangebot durch Plan-Verdichtung knapper wird
- BVerwG zur Berücksichtigung verkehrlicher Auswirkungen

### Audit
- Sind die umliegenden Straßen bereits jetzt zu Spitzenzeiten ausgelastet?
- Wurde die Auslastung erhoben? Stichproben?
- Wurde Anwohnerparken vorgesehen?
- Bewohnerparken-Lizenzen ausreichend?

### Strategischer Angriffspunkt
- Wenn die Stadt den Parkdruck-Effekt ausblendet — Abwägungsdefizit
- Wenn die Stadt den Effekt erkennt, aber bagatellisiert — Fehlgewichtung
- Wenn der Effekt im Ergebnis die Anwohner massiv belastet — Disproportionalität möglich

## Schritt 6 — Stellplatzfestsetzung im B-Plan

### § 9 Abs. 1 Nr. 4 BauGB
- B-Plan kann Stellplätze und Garagen festsetzen
- Pflicht zur Herstellung Stellplätze auf bestimmten Flächen

### Tiefgaragen-Festsetzungen
- Tiefgaragen-Zufahrten auf Plan
- Begrünungsverpflichtung Tiefgaragen-Decke
- Höhe Tiefgarage / Abstand zur Grundstücksgrenze

### Häufige Treffer
- Tiefgaragen-Zufahrt durch Wohnstraße ohne Lärmausgleich
- Tiefgarage unter Grundwasserspiegel ohne Begründung
- Festsetzungen für Stellplätze ohne Bezug zur Reduzierungssatzung

## Schritt 7 — Stellplatzbilanz prüfen

### Tabellarisches Audit
| Position | Wert | Quelle |
|---|---|---|
| Wohneinheiten Plan-Anzahl | n | Begründung |
| Stellplatz-Soll Art. 47 BayBO | n × 1,0 | Verordnung |
| Stellplatz-Festsetzung Plan | x | Festsetzung |
| Reduzierungsfaktor | x/n | Berechnung |
| Begründung der Reduzierung | Mobilitätskonzept ja/nein | Begründung |
| Verkehrsgutachten Datum | dd.mm.yyyy | Anlage |
| ÖPNV-Frequenz Realwert | min/Takt | Stadtwerke |
| Parkdruck-Untersuchung | ja/nein | Anlage |

## Schritt 8 — Innenstadt-Sonderlage Bahnhof

### Argumente Stadt für Reduzierung
- ÖPNV-Hauptknoten mit Bahn, Tram, Bus
- Bahnhofsnähe als ÖPNV-Privilegium
- Junges Klientel mit geringerer Autoaffinität
- Klimaschutz / Verkehrswende

### Gegenargumente Mandantenseite
- Hauptbahnhof-Nutzer parken trotzdem dort (Park-and-Ride umgekehrt)
- Verlagerung in angrenzende Wohnstraßen
- Bewohner-Klientel nicht steuerbar (Mietverträge)
- Auto-Abhängigkeit für Besucher, Pflege, Lieferung

## Schritt 9 — BayBO 2023-Novelle Stellplätze

### Aktuelle Entwicklung
- Tendenz zur stärkeren Flexibilisierung
- Förderung autoreduzierter Quartiere
- Aber: Anwohnerbelange weiterhin abwägungserheblich
- BayVGH-Rechtsprechung zur Anwohner-Klagebefugnis bei Stellplatz-Knappheit

## Quellen

- BayBO Art. 47, Art. 81 Abs. 1 Nr. 4
- BauGB § 9 Abs. 1 Nr. 4
- GaStellV (Bayerische Garagen- und Stellplatzverordnung)
- BVerwG, Urteil vom 26.5.2004 – 9 A 6.03 (Verkehrsbelang)
- BayVGH, Urteil vom 17.12.2018 – 15 N 16.2373 (Stellplatzreduzierung)
- BayVGH, Urteil vom 23.6.2015 – 1 BV 13.2336 (Mobilitätskonzept)

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
