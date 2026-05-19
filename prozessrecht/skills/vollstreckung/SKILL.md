---
name: vollstreckung
description: |
  Unterstützt bei der Durchführung der Zwangsvollstreckung nach §§ 704 ff. ZPO: Mobiliarvoll-
  streckung, Forderungspfändung, Immobiliarvollstreckung, Vermögensauskunft, Räumung und
  Herausgabe. Lädt, wenn ein Mandat die Einleitung, Durchführung oder Abwehr von Vollstreckungs-
  maßnahmen betrifft.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Zwangsvollstreckung
  - Vollstreckung
  - Gerichtsvollzieher
  - Pfändung
  - PfÜB
  - Forderungspfändung
  - Vermögensauskunft
  - Räumung
  - ZVG
  - Herausgabevollstreckung
  - § 829 ZPO
  - § 808 ZPO
---

# Zwangsvollstreckung – Überblick und Praxis

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
  Zustellung = „drei Säulen")
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

### Leitentscheidungen

- BGH, Beschl. v. 23.10.2014 – VII ZB 17/14, NJW 2015, 73 Rn. 12 ff.: Zur Pfändung von
  Kontoguthaben; das Vollstreckungsgericht prüft den PfÜB nur formal; materielle Einwendungen
  des Schuldners sind im Wege der Vollstreckungsgegenklage (§ 767 ZPO) oder Erinnerung (§ 766
  ZPO) geltend zu machen.
- BGH, Urt. v. 20.05.2010 – IX ZR 165/09, NJW 2010, 2507 Rn. 20 ff.: Zur Drittwiderspruchs-
  klage § 771 ZPO; der Dritte muss ein die Veräußerung hinderndes Recht (insbes. Eigentum,
  Nießbrauch, Pfandrecht) an dem gepfändeten Gegenstand haben; bloße Schuldrechtliche Ansprüche
  genügen nicht.
- BGH, Beschl. v. 09.11.2021 – VII ZB 22/20, NJW 2022, 229 Rn. 18 ff.: Zum P-Konto und
  Pfändungsschutz; der Gläubiger muss den Pfändungsschutz des § 850k ZPO gegen sich gelten
  lassen; eine nachträgliche Aufhebung des Pfändungsschutzes erfordert einen gesonderten Antrag.
- BGH, Beschl. v. 12.05.2016 – VII ZB 62/13, NJW 2016, 2659 Rn. 22: Zur Zustellung als
  Vollstreckungsvoraussetzung § 750 ZPO; Vollstreckungsmaßnahmen ohne vorherige Zustellung
  sind rechtswidrig und auf Erinnerung hin aufzuheben.

### Kommentarliteratur

- Hess, in: MüKoZPO, 6. Aufl. 2020, § 829 Rn. 1 ff. (Forderungspfändung: Antrag, Inhalt
  des PfÜB, Zustellungsreihenfolge; Rn. 45 ff. zu Drittschuldnerpflichten und Drittschuldner-
  erklärung § 840 ZPO).
- Stöber/Rellermeyer, Forderungspfändung, 17. Aufl. 2022, Rn. B.1 ff. (Praxisleitfaden;
  Muster für PfÜB-Antrag; Besonderheiten bei Bankkonten, Mietforderungen, Sozialleistungen).
- Gruber, in: MüKoZPO, 6. Aufl. 2020, § 802c Rn. 1 ff. (Vermögensauskunft: Ablauf,
  Pflichten des Schuldners, Eidesstattliche Versicherung, Eintragung ins Schuldnerverzeichnis).
- Vollkommer, in: Zöller, ZPO, 35. Aufl. 2024, § 885 Rn. 1 ff. (Räumungsvollstreckung:
  Androhung, Terminierung, Einlagerungspflicht des GV für unpfändbare Sachen).

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
Schutz nach § 850k ZPO prüfen (BGH, Beschl. v. 09.11.2021 – VII ZB 22/20, NJW 2022, 229 Rn. 18).

## Risiken und typische Fehler

- **Fehlende Zustellung** (§ 750 ZPO): Vollstreckung rechtswidrig; Erinnerung § 766 ZPO
  hat Erfolg (BGH, Beschl. v. 12.05.2016 – VII ZB 62/13, NJW 2016, 2659 Rn. 22).
- **P-Konto übersehen**: Pfändung auf Girokonto leer, wenn Schuldner P-Konto führt;
  Freibeträge sind automatisch geschützt (§ 850k ZPO).
- **Falsche Pfändungsfreigrenze**: Bei Unterhaltspflichten des Schuldners erhöhte Freigrenze
  (§ 850c Abs. 2 ZPO); Überpfändung macht Gläubiger schadensersatzpflichtig.
- **Drittwiderspruchsklage** § 771 ZPO: Gepfändeter Gegenstand gehört Dritten → Klage suspendiert
  Vollstreckung; materiell-rechtliches Eigentum des Dritten prüfen (BGH, Urt. v. 20.05.2010 –
  IX ZR 165/09, NJW 2010, 2507 Rn. 20).
- **Vollstreckungsgegenklage** § 767 ZPO: Schuldner hat nach Titelerlass erfüllenden Umstand
  (Zahlung, Aufrechnung, Stundung) → Klage beim Prozessgericht.
- **Berufsrecht**: Vollstreckungsaufträge mit Vermögensdaten des Schuldners unterliegen
  § 43a Abs. 2 BRAO, § 203 StGB.

## Quellenpflicht

Jede Aussage zu Vollstreckungsvoraussetzungen, Pfändungsfreigrenzen und Rechtsbehelfen ist
nach `references/zitierweise.md` zu belegen. BGH-Beschlüsse vollständig mit Datum, Az.,
NJW-Fundstelle und Rn. Kommentare mit Bearbeiter, Werk, Aufl., §, Rn. Bei Monographien
(Stöber/Rellermeyer) Autoren, Titel, Aufl., Jahr, Rn. zitieren.
