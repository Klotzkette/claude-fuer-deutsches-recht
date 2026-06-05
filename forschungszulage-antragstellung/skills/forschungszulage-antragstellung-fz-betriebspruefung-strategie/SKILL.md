---
name: forschungszulage-antragstellung-fz-betriebspruefung-strategie
description: "FZ Betriebspruefung Strategie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# FZ Betriebspruefung Strategie

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **FZ Betriebspruefung Strategie** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fz-betriebspruefung-strategie` | Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn keine Steuerstraftat), Argumentationspakete, Schlussbesprechung. Pruefraster: Stundennachweise, Auftragsforschungsvertraege, Mitarbeiterzuordnung, FuE-Phasentrennung. Routet in fz-dokumentationspaket-betriebspruefung. |
| `fz-finanzamt-festsetzung-auszahlung` | Forschungszulage beim Finanzamt beantragen, festsetzen und auszahlen lassen: ELSTER-Antrag, Vorlage der BSFZ-Bescheinigung, Forschungszulagenbescheid, Anrechnung auf Einkommen- oder Körperschaftsteuer, Auszahlung eines Überschusses, Vorauszahlungssenkung. Mit Zeitlinie Q1 bis Q4, Trade-offs Sofortauszahlung vs. Verrechnung und Schritt-für-Schritt-Antragsroute. |
| `fz-historie-und-rechtsgrundlagen` | Historie und Rechtsgrundlagen der steuerlichen Forschungszulage einfuehrend: FZulG seit 2020, Wachstumschancengesetz 2024 mit Erhoehung auf 10 Mio. Euro Bemessungsgrundlage, KMU-Bonus 5 Mio. Euro. Verhaeltnis zu Projektfoerderung (Bund, Land, EU). Steuerliche Behandlung als Zulage, nicht Subvention. Beispielrechnung. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **FZ Betriebspruefung Strategie**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fz-betriebspruefung-strategie`

**Fokus:** Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn keine Steuerstraftat), Argumentationspakete, Schlussbesprechung. Pruefraster: Stundennachweise, Auftragsforschungsvertraege, Mitarbeiterzuordnung, FuE-Phasentrennung. Routet in fz-dokumentationspaket-betriebspruefung.

# FZ: Betriebspruefungs-Strategie

## Spezialwissen: FZ: Betriebspruefungs-Strategie
- **Spezialgegenstand:** FZ: Betriebspruefungs-Strategie / fz betriebspruefung strategie. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FZ.
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

## 2. `fz-finanzamt-festsetzung-auszahlung`

**Fokus:** Forschungszulage beim Finanzamt beantragen, festsetzen und auszahlen lassen: ELSTER-Antrag, Vorlage der BSFZ-Bescheinigung, Forschungszulagenbescheid, Anrechnung auf Einkommen- oder Körperschaftsteuer, Auszahlung eines Überschusses, Vorauszahlungssenkung. Mit Zeitlinie Q1 bis Q4, Trade-offs Sofortauszahlung vs. Verrechnung und Schritt-für-Schritt-Antragsroute.

# Finanzamt: Festsetzung und Auszahlung

## Worum geht es

Nach Erhalt der BSFZ-Bescheinigung beginnt die zweite Stufe: der eigentliche Antrag auf Forschungszulage beim Finanzamt. Der Antrag wird elektronisch über ELSTER eingereicht, die Festsetzung erfolgt durch einen gesonderten Forschungszulagenbescheid. Der Betrag wird auf die nächste Einkommen- oder Körperschaftsteuerfestsetzung angerechnet; ein Überschuss wird ausgezahlt (§ 10 FZulG).

## Wann dieses Modul hilft

- Sobald die BSFZ-Bescheinigung vorliegt.
- Bei der Liquiditätsplanung: wann fließt die Zulage?
- Bei Vorauszahlungsfragen.
- Bei Bescheidprüfung nach Eingang des Forschungszulagenbescheids.

## Sachrahmen

- **Antragsweg:** elektronisch über ELSTER (Antrag auf Forschungszulage — Bezeichnung und konkretes Formular vom Antragsteller mit aktueller Fassung zu verifizieren).
- **Antragszeitpunkt:** frühestens nach Ablauf des Wirtschaftsjahres, in dem die Aufwendungen entstanden sind.
- **Erforderliche Anlagen:** BSFZ-Bescheinigung, Berechnung der Bemessungsgrundlage, Personalkostennachweise, ggf. Auftragsforschungsverträge und Rechnungen.
- **Festsetzung:** gesonderter Forschungszulagenbescheid.
- **Anrechnung:** bei der nächsten erstmaligen Einkommen- oder Körperschaftsteuerfestsetzung.
- **Auszahlung:** Überschuss zugunsten des Steuerpflichtigen wird als Einkommen- oder Körperschaftsteuererstattung ausgezahlt — auch in Verlustlagen.
- **Vorauszahlungssenkung:** § 10 Abs. 2a FZulG (vom Antragsteller mit aktueller Fassung zu prüfen) erlaubt unter Voraussetzungen Vorauszahlungssenkung.

## Praxisleitfaden — der schnelle Bescheid

### Trick parallele Vorbereitung

- BSFZ-Antrag und Personalkostenrechnung **parallel** vorbereiten.
- Sobald BSFZ-Bescheinigung eingeht, sind alle Belege schon zusammengestellt. Der Finanzamt-Antrag verlässt das Büro innerhalb einer Woche, nicht erst nach Wochen.

### Antragsweg Schritt für Schritt

1. BSFZ-Bescheinigung im PDF-Format sichern, als Anlage ablegen.
2. Berechnung der Bemessungsgrundlage je Wirtschaftsjahr fertig stellen (siehe `fz-bemessungsgrundlage-2026`).
3. ELSTER-Konto prüfen (Anmeldung des Antragstellers, Bevollmächtigtenzugang Steuerberater).
4. Antrag auf Forschungszulage in ELSTER auswählen, Daten eingeben, BSFZ-Bescheinigung und Berechnung anhängen.
5. Antrag einreichen und Eingangsbestätigung sichern.
6. Auf Rückfragen des Finanzamts vorbereitet sein (Personalkosten-Detail, Stundenaufzeichnungen, Auftragsforschungsverträge).
7. Forschungszulagenbescheid nach Eingang prüfen: Höhe, Anrechnungsmodus, Erstattung.

### Frist-Fallen

- **Antragsfrist:** bis zu mehrere Jahre rückwirkend (vom Antragsteller mit § 5 Abs. 1 FZulG und der AO konkret zu prüfen). Keine erfundenen Datumswerte.
- **Festsetzungsverjährung** der zugrundeliegenden Steuer beachten.
- **BSFZ-Bescheinigung** muss zum Zeitpunkt des Finanzamt-Antrags vorliegen.

### Beispiel-Zeitlinie

| Phase | Zeit | Inhalt |
| --- | --- | --- |
| Q1 Folgejahr | Januar bis März | BSFZ-Antrag einreichen, Stundenaufzeichnung abschließen |
| Q2 bis Q3 | April bis September | BSFZ-Bearbeitung, parallel Personalkostenrechnung finalisieren |
| Q3 oder Q4 | Sommer bis Herbst | BSFZ-Bescheinigung trifft ein, Finanzamt-Antrag innerhalb 1 bis 2 Wochen einreichen |
| Q1 Folgejahr +1 | Januar bis April | Forschungszulagenbescheid, Anrechnung/Auszahlung |

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Sofortauszahlung vs. Verrechnung | Erstattung jetzt | reduziert künftige Steuerzahlung | Sofortauszahlung in Verlustlagen |
| Antrag direkt nach Bescheinigung vs. mit Steuererklärung | schneller Bescheid | gebearbeitet mit Veranlagung | direkt, wegen Liquidität |
| Vorauszahlungssenkung vs. abwarten | sofort Liquidität | spätere Erstattung | Vorauszahlung senken, wenn Voraussetzungen vorliegen |
| Rückwirkende Jahre einzeln vs. zusammen | je Jahr separater Antrag | Sammeleinreichung | je Jahr separater Antrag, weil je Wirtschaftsjahr eigene BMG |

## Schritt für Schritt

1. Eingang BSFZ-Bescheinigung dokumentieren.
2. BMG-Berechnung pro Wirtschaftsjahr fertigstellen.
3. ELSTER-Antrag vorbereiten, Anlagen prüfen.
4. Antrag einreichen, Eingangsbestätigung dokumentieren.
5. Auf Rückfragen reagieren (binnen typischer Bearbeitungsfristen).
6. Forschungszulagenbescheid prüfen, gegebenenfalls Einspruch (siehe `fz-ablehnung-nachbesserung-einspruch`).
7. Verrechnung/Auszahlung beobachten.
8. Vorauszahlung 1. Quartal Folgejahr senken, soweit Voraussetzungen vorliegen.

## Mustertexte

**Begleitschreiben an das Finanzamt (Vorlage):**

"Sehr geehrte Damen und Herren,

namens und in Vollmacht der [Mandantin] reichen wir den Antrag auf Forschungszulage für das Wirtschaftsjahr [Jahr] ein. Beigefügt:

1. BSFZ-Bescheinigung vom [Datum], Aktenzeichen [BSFZ-AZ].
2. Berechnung der Bemessungsgrundlage je Vorhaben und Wirtschaftsjahr.
3. Übersicht Personalkosten je Mitarbeiter (Anlage 1).
4. Auftragsforschungsverträge und Rechnungen (Anlage 2).
5. Übersicht weiterer öffentlicher Förderungen (Anlage 3, AGVO-Kumulierungsblatt).

Die Forschungszulage beträgt nach unserer Berechnung [Euro-Betrag]. Wir bitten um Festsetzung und Verrechnung gemäß § 10 FZulG. Soweit ein Überschuss zugunsten der Mandantin entsteht, bitten wir um Auszahlung auf das angegebene Konto.

Mit freundlichen Grüßen [Berufsbezeichnung]."

**Bescheidprüfungsblatt:**

| Posten | Antrag | Bescheid | Differenz | Bewertung |
| --- | --- | --- | --- | --- |
| Eigene Personalkosten | | | | |
| Auftragsforschung 70 Prozent | | | | |
| Eigenleistung | | | | |
| AfA Wirtschaftsgüter | | | | |
| Pauschale 20 Prozent | | | | |
| Bemessungsgrundlage | | | | |
| Forschungszulage | | | | |
| Anrechnung | | | | |
| Auszahlung | | | | |

## Typische Fehler

- Finanzamt-Antrag ohne BSFZ-Bescheinigung eingereicht (formal zurückgewiesen).
- Berechnung ohne nachvollziehbare Anlage eingereicht.
- Personalkostenformel ohne Stundennachweis hinterlegt.
- Anrechnung auf falsches Wirtschaftsjahr beantragt.
- Vorauszahlungssenkung beantragt, ohne dass Bescheinigung schon vorliegt.

## Output

- Vollständige Antragsmappe an das Finanzamt.
- ELSTER-Eingangsbestätigung.
- Bescheidprüfungsblatt nach Eingang.
- Liquiditätszeitachse.
- Schreiben an Mandant zur Bestätigung der Antragstellung und nächsten Schritte.

## Querverweise

- `fz-bsfz-bescheinigung-projektbeschreibung` für die Vorstufe.
- `fz-bemessungsgrundlage-2026` für die Höhe der BMG.
- `fz-ablehnung-nachbesserung-einspruch` bei Bescheidkürzung.
- `fz-insolvenz-verlust-liquiditaet` bei Auszahlungsfragen in Verlustlagen.
- `fz-kumulierung-beihilfen-agvo` für AGVO-Kumulierungsblatt.

## Quellen Stand 05/2026

- FZulG, insbesondere §§ 5, 10 (vom Antragsteller mit konsolidierter Fassung zu prüfen).
- BMF-Hinweise zur Forschungszulage: https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Steuerliche_Themengebiete/Forschungszulage/forschungszulage.html
- ELSTER-Portal (Antragsformulare und elektronischer Zugang).
- `references/forschungszulage-quellen-und-zahlen.md`.

## 3. `fz-historie-und-rechtsgrundlagen`

**Fokus:** Historie und Rechtsgrundlagen der steuerlichen Forschungszulage einfuehrend: FZulG seit 2020, Wachstumschancengesetz 2024 mit Erhoehung auf 10 Mio. Euro Bemessungsgrundlage, KMU-Bonus 5 Mio. Euro. Verhaeltnis zu Projektfoerderung (Bund, Land, EU). Steuerliche Behandlung als Zulage, nicht Subvention. Beispielrechnung.

# FZ: Historie und Rechtsgrundlagen

## Spezialwissen: FZ: Historie und Rechtsgrundlagen
- **Spezialgegenstand:** FZ: Historie und Rechtsgrundlagen / fz historie und rechtsgrundlagen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FZulG, KMU, EU, FZ.
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
