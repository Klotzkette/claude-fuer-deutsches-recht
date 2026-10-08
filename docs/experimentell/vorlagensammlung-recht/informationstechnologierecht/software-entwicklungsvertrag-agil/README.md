# Agiler Softwareentwicklungsvertrag

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage passt zur agilen Individualsoftwareentwicklung mit Product Backlog, Sprint-Planung, Definition of Done, Sprint Review, inkrementeller Abnahme, Quellcodeübergabe und Change-Steuerung. Sie ist nicht als allgemeiner IT-Werkvertrag gedacht; ohne konkrete Regelung zu Backlog-Hoheit, Sprint-Ziel, Mängelklassen, Product Owner und Release-Verantwortung bleibt agile Entwicklung rechtlich zu offen.

## Einschlägige Normen

- §§ 631, 640 BGB für werkvertragliche Projekt-, Migrations-, Entwicklungs- und Abnahmepflichten.
- §§ 611, 611a, 675 BGB, wenn Beratung, Betrieb, Support oder laufende Dienste im Vordergrund stehen.
- §§ 327 ff. BGB bei digitalen Produkten gegenüber Verbrauchern; bei B2B als Prüfanker für Update-, Bereitstellungs- und Mängelmechanik.
- §§ 280, 281, 286, 307 BGB zu Pflichtverletzung, Nacherfüllung, Verzug und AGB-Kontrolle.
- Art. 28, Art. 32, Art. 33 DSGVO, wenn Betrieb, Hosting, Support oder Migration personenbezogene Daten betrifft.

## Hinweise zur Verwendung

Der Vertrag muss agile Beweglichkeit und werkvertragliche Verbindlichkeit zusammenführen. Sprint-Ergebnisse werden nicht nur präsentiert, sondern anhand der Definition of Done, Akzeptanzkriterien und Testumgebung prüfbar gemacht; offener Backlog-Umfang wird über Change-Mechanik, Budget-Cap und Priorisierung gesteuert.

Fristen- und Beweisarchitektur: Sprint Planning, Sprint Review, Abnahmefiktion, Defect-Fixing, Release-Freeze, Security-Fix, Datenmigration und Quellcodeübergabe werden mit Messpunkt, Fristbeginn und Rechtsfolge geführt. Bei personenbezogenen Daten wird parallel ein AVV nach `informationstechnologierecht/auftragsverarbeitungsvertrag-dsgvo/` oder eine eigene Verantwortlichkeitsregel genutzt.

Abgrenzung: Für SaaS `informationstechnologierecht/software-as-a-service-vertrag/`; für agile Entwicklung `informationstechnologierecht/software-entwicklungsvertrag-agil/`; für Outsourcing und Exit `informationstechnologierecht/it-outsourcing-transition-vertrag/`.

## Taktische Hinweise

### Vorgehensreihenfolge

1. Vor Sprintbeginn werden Produktvision, Rollen, Backlog-Hoheit, Definition of Ready und Definition of Done festgelegt. Der initiale Backlog muss Mindestumfang, Abhängigkeiten und nicht geschuldete Funktionen erkennen lassen.
2. Für jeden Sprint werden Ziel, Kapazität, Abnahmekriterien, Review-Termin und Vergütungsfolge dokumentiert. Änderungen gelangen nur über ein nachvollziehbares Backlog- und Change-Verfahren in den geschuldeten Umfang.
3. Nach jedem Review werden Abnahme, Mängel, technische Schulden, Quellcodeübergabe und Open-Source-Inventar aktualisiert. Die Releasefreigabe setzt reproduzierbaren Build, Sicherheitsprüfung und vereinbarte Dokumentation voraus.

### Typische Gegnereinwände mit Antwortlinie

- Der Auftragnehmer beruft sich darauf, agile Zusammenarbeit schließe einen verbindlichen Erfolg aus. Die Antwortlinie weist sprintbezogene Liefergegenstände und objektive Definition-of-Done-Kriterien als geschuldete Ergebnisse aus.
- Der Auftraggeber verlangt zusätzliche Funktionen als bloße Konkretisierung. Die Antwortlinie vergleicht Produktvision, akzeptierten Backlog und Aufwand und behandelt echte Mehrleistung im Change-Verfahren.
- Eine Partei bestreitet die Abnahme eines Inkrements. Die Antwortlinie sichert Review-Protokoll, Testresultate, erklärte Vorbehalte und den Umgang mit nicht wesentlichen Mängeln.

### Häufige Fehler

- Product Owner und Entwicklungsteam entscheiden ohne festgelegte Vertretungsmacht und Dokumentationskanäle.
- Sprint-Abnahme, Gesamtabnahme und produktive Freigabe werden begrifflich vermischt.
- Nutzungsrechte werden zugesagt, ohne Drittcode, Open-Source-Lizenzen und Vorbestand gesondert zu erfassen.

## Verwandte Vorlagen

- [IT-Projektvertrag (Werkvertrag, agil/V-Modell XT, Mitwirkungspflichten)](../it-projektvertrag-werkleistung/) — eignet sich für stärker phasen- und werkorientierte Entwicklungsprojekte.
- [Quellcode-Herausgabe- und Datenexport-Notfallplan](../quellcode-herausgabe-und-datenexport-notfallplan/) — sichert den Zugriff auf Code und Betriebswissen bei Projektabbruch.
- [Software-Escrow-Vereinbarung](../software-escrow-vereinbarung/) — ergänzt die laufende Quellcodeübergabe um unabhängige Hinterlegung.
- [Softwarepflege- und Supportvertrag (Maintenance; SLA)](../softwarepflege-und-supportvertrag/) — regelt Pflege und Störungsbearbeitung nach Abschluss der Entwicklung.

## Download

- [⬇ Agiler Softwareentwicklungsvertrag – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/software-entwicklungsvertrag-agil/software-entwicklungsvertrag-agil.md.zip)
- [⬇ Agiler Softwareentwicklungsvertrag – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/software-entwicklungsvertrag-agil/software-entwicklungsvertrag-agil.odt)

Vorschau im Repository: [`software-entwicklungsvertrag-agil.odt`](software-entwicklungsvertrag-agil.odt) · [`software-entwicklungsvertrag-agil.md`](software-entwicklungsvertrag-agil.md)

## Rechtsprechungsanker

- BGH, Urteil vom 5. Juni 2014 — VII ZR 276/13: Bei werkvertraglich geprägten Softwareleistungen genügt der Besteller seiner Darlegungslast, wenn er konkrete Mangelerscheinungen beschreibt; Ursachen muss er nicht darlegen. Für die Vertragsgestaltung spricht das für reproduzierbare Fehlerprotokolle, Testumgebungen und klare Abnahmekriterien.

Amtliche oder primäre Startpunkte:
- [BGB](https://www.gesetze-im-internet.de/bgb/)
- [UrhG](https://www.gesetze-im-internet.de/urhg/)
- [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [BGH VII ZR 276/13 bei dejure](https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=VII+ZR+276%2F13&Datum=05.06.2014&Gericht=BGH)
