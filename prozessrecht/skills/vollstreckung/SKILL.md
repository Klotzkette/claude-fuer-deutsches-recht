---
name: vollstreckung
description: "Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: §§ 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: Vollstreckungsauftrag und Pfaendungsbeschluss-Antrag. Abgrenzung: nicht AnfG-Anfechtung im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Zwangsvollstreckung – Überblick und Praxis

## Arbeitsbereich

Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: §§ 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: Vollstreckungsauftrag und Pfaendungsbeschluss-Antrag. Abgrenzung: nicht AnfG-Anfechtung. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Dieser Skill bleibt der prozessrechtliche Überblick. Für die operative Durchführung – Antragsformulare,
Drittschuldnerwahl, P-Konto-Berechnung, ZVollstrDigitG-Übergänge 2026/2027, notarielle Urkunde § 800 ZPO,
Tabellenauszug § 201 InsO, Räumung § 885 ZPO, Schuldnerschutz – lädt das freistehende Plugin
`zwangsvollstreckung` mit 17 spezialisierten Skills (`zv-kommandocenter`, `zv-titel-klausel-zustellung`,
`zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-pfueb-mieter-finanzamt`, `zv-vermoegensauskunft-gv`,
`zv-kontensuche-drittschuldner`, `zv-notarielle-urkunde-grundschuld`, `zv-zvg-antrag-glaeubiger`,
`zv-tabellenauszug-201-inso`, `zv-mobiliar-gv-auftrag`, `zv-raeumung-885`, `zv-abwehr-schuldner`,
`zv-pfaendungstabelle-2025`, `zv-elektronische-zustellung-2027`, `zv-mahnbescheid-online`,
`zv-vollstreckungsbescheid-folge`). Dieser Hub-Skill ist die richtige Adresse für die dogmatische
Gesamtschau; das Plugin ist die richtige Adresse für die einzelne Vollstreckungsmaßnahme.

## Zweck

Dieser Skill begleitet die Durchführung der Zwangsvollstreckung aus Urteilen, Beschlüssen,
Vollstreckungsbescheiden, notariellen Urkunden und anderen Titeln. Er deckt alle wesentlichen
Vollstreckungsarten ab: Mobiliarvollstreckung (Pfändung körperlicher Sachen), Geldvollstreckung
in Forderungen (PfÜB), Immobiliarvollstreckung (ZVG), Vermögensauskunft, Räumungsvollstreckung
und Herausgabevollstreckung. Auf der Schuldnerseite: Abwehr rechtswidriger Vollstreckung,
Vollstreckungsgegenklage, Drittwiderspruchsklage.

## Eingaben

Das Modell benötigt:

1. **Vollstreckungstitel**: Art (Urteil, Beschluss, VB, notarielle Urkunde, Vergleich),
 Datum, Gericht/Notar, Rechtskraft/Vollstreckbarkeit
2. **Vollstreckungsklausel**: Liegt eine vollstreckbare Ausfertigung vor? (§ 724 ZPO)
3. **Zustellung**: Wurde der Titel dem Schuldner zugestellt? (§ 750 ZPO – Voraussetzung!)
4. **Vollstreckungsgegenstand**: Geld/Mobilien/Forderungen/Immobilie/Herausgabe/Räumung
5. **Bekannte Vermögenswerte**: Kontonummern, Arbeitgeber, Grundstücke, Kfz
6. **Schuldnersituation**: Privatperson oder Unternehmen; Pfändungsfreigrenzen beachten

## Rechtlicher Rahmen

### Normen

- **§§ 704–707 ZPO** – Vollstreckungstitel und allgemeine Voraussetzungen (Titel, Klausel,
 Zustellung = "drei Säulen")
- **§ 724 ZPO** – vollstreckbare Ausfertigung (Klausel); § 725 ZPO – Klauselerteilung durch
 Urkundsbeamten; § 732 ZPO – Erinnerung gegen Klauselerteilung
- **§ 750 ZPO** – Zustellungserfordernis vor Beginn der Vollstreckung
- **§ 767 ZPO** – Vollstreckungsgegenklage (materielle Einwendungen gegen den Anspruch selbst)
- **§ 771 ZPO** – Drittwiderspruchsklage (Eigentum oder Recht eines Dritten an Vollstreckungs-
 gegenstand)
- **§ 802a–802l ZPO** – Vermögensauskunft (§ 802c: Abgabe durch Schuldner; § 802d: Sperrfrist
 2 Jahre; § 802l: Abruf beim Gerichtsvollzieher aus Schuldnerverzeichnis)
- **§ 808 ZPO** – Pfändung körperlicher Sachen (Mobiliarpfändung durch GV; Gewahrsam des
 Schuldners; Pfändungsprotokoll)
- **§§ 811, 811c ZPO** – Unpfändbare Sachen (Hausrat, Arbeitsgeräte, Sozialgeräte)
- **§ 829 ZPO** – Forderungspfändung (Pfändungs- und Überweisungsbeschluss = PfÜB; Beschluss
 durch Vollstreckungsgericht; Zustellung an Drittschuldner und Schuldner)
- **§§ 850–850k ZPO** – Pfändungsschutz für Arbeitseinkommen und P-Konto (§ 850c ZPO –
 Pfändungstabelle; § 850k ZPO – Pfändungsschutzkonto)
- **§ 883 ZPO** – Herausgabevollstreckung beweglicher Sachen
- **§ 885 ZPO** – Räumungsvollstreckung (durch GV; Androhung 3 Wochen vor Termin)
- **ZVG** – Zwangsversteigerung und Zwangsverwaltung von Grundstücken (§§ 15 ff. ZVG
 Antrag beim AG; §§ 35 ff. ZVG Versteigerungstermin)
- **§§ 900–915h ZPO** – Insolvenzantrag als ultima ratio; § 17 InsO – Zahlungsunfähigkeit

### Leitentscheidungen und Normfassungen

- BGH VII. ZS Linie zur Klauselpruefung: Die Pruefungstiefe im Klauselerteilungsverfahren ist formal eng begrenzt; materielle Einwendungen sind im Wege der Vollstreckungsgegenklage (§ 767 ZPO) oder Erinnerung (§ 766 ZPO) geltend zu machen. Aktuelle Aktenzeichen (z.B. BGH, Beschl. v. 30.01.2025 – Az. VII ZB 10/24) vor Verwendung ueber https://www.bundesgerichtshof.de und https://dejure.org verifizieren.
- BGH-Linie zu § 850k ZPO P-Konto-Schutz: Pfaendungsschutz wirkt automatisch gegenueber dem Glaeubiger; nachtraegliche Aufhebung erfordert gesonderten Antrag. Aktenzeichen vor Schriftsatzverwendung pruefen.
- Vollstreckungsvoraussetzung § 750 ZPO: Vollstreckungsmassnahmen ohne vorherige Zustellung sind rechtswidrig und auf Erinnerung hin aufzuheben (staendige Rechtsprechung).

### Rechtsstand 2025/2026

- Pfaendungsfreigrenzenbekanntmachung 2025 (BGBl. 2025 I Nr. 110): Grundfreibetrag 1.555 EUR ab 01.07.2025 bis 30.06.2026. Quelle: https://www.recht.bund.de/bgbl/1/2025/110/VO.html
- Justizstandort-Staerkungsgesetz (BGBl. 2025 I Nr. 318 vom 11.12.2025): Wertgrenzenreform ab 01.01.2026 mit Auswirkungen auf Beschwerdesummen § 511 Abs. 2 ZPO (jetzt 1.000 EUR) und § 23 GVG (AG 10.000 EUR).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### A. Geldvollstreckung – Mobiliarpfändung (§ 808 ZPO)

1. **Voraussetzungen prüfen**: Titel + Klausel + Zustellung; Wartefrist § 750 Abs. 1 ZPO
 (i. d. R. 2 Wochen nach Zustellung)
2. **GV beauftragen**: Vollstreckungsauftrag an Gerichtsvollzieher; Angabe bekannter Vermögens-
 werte; ggf. Auftrag zur Vermögensauskunft kombinieren
3. **Pfändung**: GV pfändet körperliche Sachen im Gewahrsam des Schuldners; Unpfändbarkeit
 §§ 811 ff. ZPO beachten; Pfändungsprotokoll ausstellen

### B. Forderungspfändung – PfÜB (§§ 829, 835 ZPO)

1. **Antrag beim Vollstreckungsgericht** (AG am Wohnsitz des Schuldners): Bezeichnung von
 Forderung und Drittschuldner (Bank, Arbeitgeber, Mieter)
2. **Erlass des PfÜB**: Gericht prüft nur formal → PfÜB wird erlassen
3. **Zustellung**: Zunächst an Drittschuldner (Pfändungswirkung), dann an Schuldner
4. **Drittschuldnererklärung** § 840 ZPO: Drittschuldner muss binnen 2 Wochen Auskunft geben
5. **Überweisung** § 835 ZPO: zur Einziehung oder an Zahlungs Statt

### C. Vermögensauskunft (§ 802c ZPO)

1. **Antrag beim GV**: wenn Vollstreckung erfolglos; GV lädt Schuldner vor
2. **Abgabe der Vermögensauskunft** unter Versicherung der Vollständigkeit (§ 802c Abs. 3 ZPO)
3. **Eintragung ins Schuldnerverzeichnis** § 882c ZPO bei Verweigerung oder Verletzung

### D. Räumungsvollstreckung (§ 885 ZPO)

1. **Titel**: rechtskräftiges Räumungsurteil oder vorläufig vollstreckbares Urteil mit
 Sicherheitsleistung
2. **Androhung**: GV setzt Termin (mind. 3 Wochen Vorlauf, § 885 Abs. 1 ZPO)
3. **Durchführung**: GV räumt; Hab und Gut des Schuldners wird eingelagert oder bei Wertlosigkeit
 vernichtet

## Ausgabeformat

- **PfÜB-Antragsentwurf** (vollständig für das Vollstreckungsgericht)
- **Rechtliches Memo** zu Vollstreckungsvoraussetzungen und Pfändungsschutz
- **Checkliste** (Titel/Klausel/Zustellung; Pfändungsschutz; Drittschuldner)
- **Muster-Vermögensauskunfts-Aufforderung** für außergerichtliche Nutzung

## Beispiel

**Sachverhalt**: Gläubigerin G hat ein rechtskräftiges Urteil gegen Schuldner S über EUR 12.000
(inkl. Zinsen). S ist Arbeitnehmer bei der Musterfirma GmbH; sein Nettolohn beträgt EUR 2.400/Monat.

**Prüfung (Urteilsstil)**:

*Voraussetzungen*: Titel (Urteil), vollstreckbare Ausfertigung (§ 724 ZPO), Zustellung an S
liegt vor (§ 750 ZPO). Vollstreckung ist zulässig.

*Forderungspfändung Arbeitseinkommen (§§ 829, 850 ff. ZPO)*: Pfändbar ist das Arbeitseinkommen
oberhalb des Pfändungsfreibetrags (§ 850c ZPO; bei Nettolohn EUR 2.400/Monat ohne Unterhaltspflichten
ca. EUR 264/Monat pfändbar nach aktueller Pfändungstabelle). PfÜB ist beim Vollstreckungsgericht
am Wohnsitz des S zu beantragen; Drittschuldnerin ist die Musterfirma GmbH.

*Empfehlung*: Zusätzlich Kontopfändung bei bekannter Hausbank (§ 829 ZPO); Cave: P-Konto-
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken und typische Fehler

- **Fehlende Zustellung** (§ 750 ZPO): Vollstreckung rechtswidrig; Erinnerung § 766 ZPO
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **P-Konto übersehen**: Pfändung auf Girokonto leer, wenn Schuldner P-Konto führt;
 Freibeträge sind automatisch geschützt (§ 850k ZPO).
- **Falsche Pfändungsfreigrenze**: Bei Unterhaltspflichten des Schuldners erhöhte Freigrenze
 (§ 850c Abs. 2 ZPO); Überpfändung macht Gläubiger schadensersatzpflichtig.
- **Drittwiderspruchsklage** § 771 ZPO: Gepfändeter Gegenstand gehört Dritten → Klage suspendiert
 Vollstreckung; materiell-rechtliches Eigentum des Dritten prüfen.
- **Vollstreckungsgegenklage** § 767 ZPO: Schuldner hat nach Titelerlass erfüllenden Umstand
 (Zahlung, Aufrechnung, Stundung) → Klage beim Prozessgericht.
- **Berufsrecht**: Vollstreckungsaufträge mit Vermögensdaten des Schuldners unterliegen
 § 43a Abs. 2 BRAO, § 203 StGB.

## Quellenpflicht

Jede Aussage zu Vollstreckungsvoraussetzungen, Pfändungsfreigrenzen und Rechtsbehelfen ist
nach `references/zitierweise.md` zu belegen. BGH-Beschlüsse vollständig mit Datum, Az.,
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Stöber/Rellermeyer) Autoren, Titel, Aufl., Jahr, Rn. zitieren.

<!-- AUDIT 27.05.2026
Datum 01.07.2010 (nicht 20.05.2010), aber mit falschem Thema: real handelt das Urteil von
Vorteilsausgleichung/Steuervorteile, nicht von Drittwiderspruchsklage § 771 ZPO (WRONG_TOPIC).
Halluzinierte Referenz geloescht. Keine Ersatzquelle für § 771 ZPO-Leitentscheidung ergaenzt.
-->
