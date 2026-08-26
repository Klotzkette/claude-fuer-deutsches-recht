---
name: vollstreckung
description: "Für Zwangsvollstreckung – Überblick und Praxis: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Zwangsvollstreckung – Überblick und Praxis

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Dieser Skill bleibt der prozessrechtliche Überblick. Für die operative Durchführung – Antragsformulare,
Drittschuldnerwahl, P-Konto-Berechnung, ZVollstrDigitG-Übergänge 2026/2027, notarielle Urkunde Paragraf 800 ZPO,
Tabellenauszug Paragraf 201 InsO, Räumung Paragraf 885 ZPO, Schuldnerschutz – lädt das freistehende Plugin
`zwangsvollstreckung` mit spezialisierten Skills (`kommandocenter`, `titel-klausel-zustellung`,
`pfueb-bank`, `pfueb-arbeitsentgelt`, `pfueb-802l-arbeit`, `vermoegensauskunft-gv`,
`kontensuche-drittschuldner`, `notarielle-urkunde-grundschuld`, `zvg-antrag-glaeubiger`,
`tabellenauszug-201-inso`, `mobiliar-gv-auftrag`, `raeumung-tabellenauszug-inso`, `abwehr-schuldner`,
`pfaendungstabelle-pfueb-arbeitsentgelt`, `elektronische-zustellung-eu`, `mahnbescheid-online-mobiliar-gv`,
`vollstreckungsbescheid-zv`). Dieser Hub-Skill ist die richtige Adresse für die dogmatische
Gesamtschau; das Plugin ist die richtige Adresse für die einzelne Vollstreckungsmaßnahme.

## Eingaben

Das Modell benötigt:

1. **Vollstreckungstitel**: Art (Urteil, Beschluss, VB, notarielle Urkunde, Vergleich),
 Datum, Gericht/Notar, Rechtskraft/Vollstreckbarkeit
2. **Vollstreckungsklausel**: Liegt eine vollstreckbare Ausfertigung vor? (Paragraf 724 ZPO)
3. **Zustellung**: Wurde der Titel dem Schuldner zugestellt? (Paragraf 750 ZPO – Voraussetzung!)
4. **Vollstreckungsgegenstand**: Geld/Mobilien/Forderungen/Immobilie/Herausgabe/Räumung
5. **Bekannte Vermögenswerte**: Kontonummern, Arbeitgeber, Grundstücke, Kfz
6. **Schuldnersituation**: Privatperson oder Unternehmen; Pfändungsfreigrenzen beachten

## Rechtlicher Rahmen

### Normen

- **Paragrafen 704–707 ZPO** – Vollstreckungstitel und allgemeine Voraussetzungen (Titel, Klausel,
 Zustellung = "drei Säulen")
- **Paragraf 724 ZPO** – vollstreckbare Ausfertigung (Klausel); Paragraf 725 ZPO – Klauselerteilung durch
 Urkundsbeamten; Paragraf 732 ZPO – Erinnerung gegen Klauselerteilung
- **Paragraf 750 ZPO** – Zustellungserfordernis vor Beginn der Vollstreckung
- **Paragraf 767 ZPO** – Vollstreckungsgegenklage (materielle Einwendungen gegen den Anspruch selbst)
- **Paragraf 771 ZPO** – Drittwiderspruchsklage (Eigentum oder Recht eines Dritten an Vollstreckungs-
 gegenstand)
- **Paragraf 802a–802l ZPO** – Vermögensauskunft (Paragraf 802c: Abgabe durch Schuldner; Paragraf 802d: Sperrfrist
 2 Jahre; Paragraf 802l: Abruf beim Gerichtsvollzieher aus Schuldnerverzeichnis)
- **Paragraf 808 ZPO** – Pfändung körperlicher Sachen (Mobiliarpfändung durch GV; Gewahrsam des
 Schuldners; Pfändungsprotokoll)
- **Paragrafen 811, 811c ZPO** – Unpfändbare Sachen (Hausrat, Arbeitsgeräte, Sozialgeräte)
- **Paragraf 829 ZPO** – Forderungspfändung (Pfändungs- und Überweisungsbeschluss = PfÜB; Beschluss
 durch Vollstreckungsgericht; Zustellung an Drittschuldner und Schuldner)
- **Paragrafen 850–850k ZPO** – Pfändungsschutz für Arbeitseinkommen und P-Konto (Paragraf 850c ZPO –
 Pfändungstabelle; Paragraf 850k ZPO – Pfändungsschutzkonto)
- **Paragraf 883 ZPO** – Herausgabevollstreckung beweglicher Sachen
- **Paragraf 885 ZPO** – Räumungsvollstreckung (durch GV; Androhung 3 Wochen vor Termin)
- **ZVG** – Zwangsversteigerung und Zwangsverwaltung von Grundstücken (Paragrafen 15 ff. ZVG
 Antrag beim AG; Paragrafen 35 ff. ZVG Versteigerungstermin)
- **Paragrafen 900–915h ZPO** – Insolvenzantrag als ultima ratio; Paragraf 17 InsO – Zahlungsunfähigkeit

### Leitentscheidungen und Normfassungen

- BGH VII. ZS Linie zur Klauselpruefung: Die Prüfungstiefe im Klauselerteilungsverfahren ist formal eng begrenzt; materielle Einwendungen sind im Wege der Vollstreckungsgegenklage (Paragraf 767 ZPO) oder Erinnerung (Paragraf 766 ZPO) geltend zu machen. Aktuelle Aktenzeichen (z.B. BGH, Beschl. v. 30.01.2025 – Az. VII ZB 10/24) vor Verwendung über https://www.bundesgerichtshof.de und https://dejure.org verifizieren.
- BGH-Linie zu Paragraf 850k ZPO P-Konto-Schutz: Pfaendungsschutz wirkt automatisch gegenueber dem Gläubiger; nachtraegliche Aufhebung erfordert gesonderten Antrag. Aktenzeichen vor Schriftsatzverwendung prüfen.
- Vollstreckungsvoraussetzung Paragraf 750 ZPO: Vollstreckungsmassnahmen ohne vorherige Zustellung sind rechtswidrig und auf Erinnerung hin aufzuheben (staendige Rechtsprechung).

### Rechtsstand 2025/2026

- Pfändungsfreigrenzenbekanntmachung 2026 (BGBl. 2026 I Nr. 80): Grundfreibetrag 1.587,40 Euro vom 1. Juli 2026 bis 30. Juni 2027. Amtliche Quelle: https://www.gesetze-im-internet.de/pf_ndfreigrbek_2026/
- Justizstandort-Staerkungsgesetz (BGBl. 2025 I Nr. 318 vom 11.12.2025): Wertgrenzenreform ab 01.01.2026 mit Auswirkungen auf Beschwerdesummen Paragraf 511 Abs. 2 ZPO (jetzt 1.000 EUR) und Paragraf 23 GVG (AG 10.000 EUR).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### A. Geldvollstreckung – Mobiliarpfändung (Paragraf 808 ZPO)

1. **Voraussetzungen prüfen**: Titel + Klausel + Zustellung; Wartefrist Paragraf 750 Abs. 1 ZPO
 (i. d. R. 2 Wochen nach Zustellung)
2. **GV beauftragen**: Vollstreckungsauftrag an Gerichtsvollzieher; Angabe bekannter Vermögens-
 werte; ggf. Auftrag zur Vermögensauskunft kombinieren
3. **Pfändung**: GV pfändet körperliche Sachen im Gewahrsam des Schuldners; Unpfändbarkeit
 Paragrafen 811 ff. ZPO beachten; Pfändungsprotokoll ausstellen

### B. Forderungspfändung – PfÜB (Paragrafen 829, 835 ZPO)

1. **Antrag beim Vollstreckungsgericht** (AG am Wohnsitz des Schuldners): Bezeichnung von
 Forderung und Drittschuldner (Bank, Arbeitgeber, Mieter)
2. **Erlass des PfÜB**: Gericht prüft nur formal → PfÜB wird erlassen
3. **Zustellung**: Zunächst an Drittschuldner (Pfändungswirkung), dann an Schuldner
4. **Drittschuldnererklärung** Paragraf 840 ZPO: Drittschuldner muss binnen 2 Wochen Auskunft geben
5. **Überweisung** Paragraf 835 ZPO: zur Einziehung oder an Zahlungs Statt

### C. Vermögensauskunft (Paragraf 802c ZPO)

1. **Antrag beim GV**: wenn Vollstreckung erfolglos; GV lädt Schuldner vor
2. **Abgabe der Vermögensauskunft** unter Versicherung der Vollständigkeit (Paragraf 802c Abs. 3 ZPO)
3. **Eintragung ins Schuldnerverzeichnis** Paragraf 882c ZPO bei Verweigerung oder Verletzung

### D. Räumungsvollstreckung (Paragraf 885 ZPO)

1. **Titel**: rechtskräftiges Räumungsurteil oder vorläufig vollstreckbares Urteil mit
 Sicherheitsleistung
2. **Androhung**: GV setzt Termin (mind. 3 Wochen Vorlauf, Paragraf 885 Abs. 1 ZPO)
3. **Durchführung**: GV räumt; Hab und Gut des Schuldners wird eingelagert oder bei Wertlosigkeit
 vernichtet

## Beispiel

**Sachverhalt**: Gläubigerin G hat ein rechtskräftiges Urteil gegen Schuldner S über EUR 12.000
(inkl. Zinsen). S ist Arbeitnehmer bei der Musterfirma GmbH; sein Nettolohn beträgt EUR 2.400/Monat.

**Prüfung (Urteilsstil)**:

*Voraussetzungen*: Titel (Urteil), vollstreckbare Ausfertigung (Paragraf 724 ZPO), Zustellung an S
liegt vor (Paragraf 750 ZPO). Vollstreckung ist zulässig.

*Forderungspfändung Arbeitseinkommen (Paragrafen 829, 850 ff. ZPO)*: Pfändbar ist das Arbeitseinkommen
oberhalb des Pfändungsfreibetrags (Paragraf 850c ZPO; bei Nettolohn EUR 2.400/Monat ohne Unterhaltspflichten
ca. EUR 264/Monat pfändbar nach aktueller Pfändungstabelle). PfÜB ist beim Vollstreckungsgericht
am Wohnsitz des S zu beantragen; Drittschuldnerin ist die Musterfirma GmbH.

*Empfehlung*: Zusätzlich Kontopfändung bei bekannter Hausbank (Paragraf 829 ZPO); Cave: P-Konto-

## Risiken und typische Fehler

- **Fehlende Zustellung** (Paragraf 750 ZPO): Vollstreckung rechtswidrig; Erinnerung Paragraf 766 ZPO
- **P-Konto übersehen**: Pfändung auf Girokonto leer, wenn Schuldner P-Konto führt;
 Freibeträge sind automatisch geschützt (Paragraf 850k ZPO).
- **Falsche Pfändungsfreigrenze**: Bei Unterhaltspflichten des Schuldners erhöhte Freigrenze
 (Paragraf 850c Abs. 2 ZPO); Überpfändung macht Gläubiger schadensersatzpflichtig.
- **Drittwiderspruchsklage** Paragraf 771 ZPO: Gepfändeter Gegenstand gehört Dritten → Klage suspendiert
 Vollstreckung; materiell-rechtliches Eigentum des Dritten prüfen.
- **Vollstreckungsgegenklage** Paragraf 767 ZPO: Schuldner hat nach Titelerlass erfüllenden Umstand
 (Zahlung, Aufrechnung, Stundung) → Klage beim Prozessgericht.
- **Berufsrecht**: Vollstreckungsaufträge mit Vermögensdaten des Schuldners unterliegen
 Paragraf 43a Abs. 2 BRAO, Paragraf 203 StGB.

## Quellenpflicht

Jede Aussage zu Vollstreckungsvoraussetzungen, Pfändungsfreigrenzen und Rechtsbehelfen ist
nach `references/zitierweise.md` zu belegen. BGH-Beschlüsse vollständig mit Datum, Az.,
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Stöber/Rellermeyer) Autoren, Titel, Aufl., Jahr, Rn. zitieren.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
