---
name: jahresabschluss-elektronische
description: "E-Bilanz § 5b EStG elektronische Übermittlung. Anwendungsfall Bilanzierer Pflicht zur elektronischen Übermittlung der Steuerbilanz an FA Taxonomie-Standard. Methodik DATEV-E-Bilanz Modul. Output E-Bilanz uebermittelt."
---

# E-Bilanz — § 5b EStG elektronische Uebermittlung

## Fachlicher Anker

- **Normen:** § 5b EStG, § 6a, § 109 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

§ 5b EStG verpflichtet alle Bilanzierer zur elektronischen Uebermittlung der Steuerbilanz an das Finanzamt (E-Bilanz). Die Uebermittlung erfolgt im XBRL-Format auf Basis der jaehrlich vom BMF veroeffentlichten Kerntaxonomie (BMF-Taxonomie, abrufbar über esteuer.de) und wird über das ERiC-Modul der Finanzverwaltung uebertragen (in DATEV: integrierte ERiC-Schnittstelle, in Addison/Sage separates ERiC-Plugin). Frist: parallel zur Steuererklaerung (Festsetzungsverjaehrung beachten, ggf. § 109 AO Verlaengerung). Bei Mandanten mit Handelsbilanz und Steuerbilanz uebermittelt der StB regelmaessig die Handelsbilanz nebst Ueberleitungsrechnung; die "Echte-Steuerbilanz"-Uebermittlung ist Wahlrecht.

## Kaltstart-Rueckfragen

1. Liegt Bilanzierungspflicht vor (§§ 140-141 AO)?
2. Welches Wirtschaftsjahr?
3. Welche aktuelle Taxonomie-Version (jaehrlich angepasst)?
4. Welche Mandantenstammdaten (Steuer-Nr, FA)?
5. Welche Sondersituation (Sonderbilanz, Ergaenzungsbilanz Personengesellschaft)?
6. Welche Konten-Zuordnung zu Taxonomie?
7. Liegen alle Stammdaten vor?
8. Welche DATEV-Schnittstelle aktiv?

## Rechtlicher Rahmen

### Primaernormen

**§ 5b EStG** — Pflicht elektronische Uebermittlung.

**§ 5 EStG** — Massgeblichkeit.

**§§ 140-141 AO** — Bilanzierungspflicht.

**§ 25 EStG** — Veranlagung.

### Verwaltungsanweisungen

- BMF-Schreiben vom 28.09.2011, IV C 6 - S 2133-b/11/10009 zur erstmaligen E-Bilanz-Einfuehrung (Anwendungszeitpunkte und Mindestumfang).
- BMF-Schreiben zur jaehrlichen Aktualisierung der Taxonomie (zuletzt veroeffentlichte Fassung über esteuer.de bzw. BMF-Newsletter prüfen).
- Anwendungsfragen siehe AEAO zu § 5b EStG (Anwendungserlass zur Abgabenordnung in jeweils gueltiger Fassung).

## Workflow

### Phase 1 — Pflicht-Prüfung

- Bilanzierer nach § 5 EStG: E-Bilanz Pflicht.
- EUER-Steuerpflichtige (§ 4 Abs. 3 EStG): keine E-Bilanz, Anlage EUER.
- Personengesellschaften mit Bilanzierungspflicht.

### Phase 2 — Taxonomie

- BMF-Kerntaxonomie in der jeweils gueltigen Jahresfassung (Veroeffentlichung typisch im 2. Quartal, Anwendungspflicht ab Folgejahr). Bezugsquelle: www.esteuer.de.
- Pflichtfelder ("Mussfelder") sind zwingend zu fuellen; bei nicht verfuegbarem Datum dokumentierter "NIL"-Wert (Auffangregel siehe BMF-Taxonomie-Begleitdokumentation).
- Optionale Felder ("Kannfelder") nach Bedarf; "Mussfelder, soweit vorhanden" sind bei tatsaechlichem Vorliegen verpflichtend.

### Phase 3 — Konten-Zuordnung

- Standardkontenrahmen SKR 03 / SKR 04 (DATEV) bzw. IKR sind mit Standard-Mapping zur Kerntaxonomie ausgestattet; konkrete Mapping-Pflege siehe SKR-aktuelle Fassung.
- Individuelle Konten erfordern manuelle Zuordnung zur Taxonomie-Position; Prüfen vor Versand zwingend.
- In DATEV Kanzlei-Rechnungswesen erfolgt die E-Bilanz-Erstellung typischerweise über das Modul "E-Bilanz" mit eigenem Prüfprotokoll (genaue Programmpfade in der aktuellen DATEV-Programmversion ggf. abweichend).

### Phase 4 — Uebermittlung

- Auswertung im StB-Programm generiert eine XBRL-Datei (Endung .xbrl bzw. eingebettet in das XBRL-Paket).
- Versand an die Finanzverwaltung erfolgt über das ERiC-Modul (ELSTER Rich Client) mit Authentifizierungszertifikat (in der Regel das Berater-/Organisations-Zertifikat im ELSTER-Online-Portal).
- Vor Echt-Versand: Plausibilitaetspruefung im ERiC durchlaufen; Prüfprotokoll dokumentieren.
- Nach Versand: Uebermittlungsprotokoll (Transferticket-ID) speichern; Ablage in der Mandantenakte (Pflicht zur Aufbewahrung der Versandquittung).

### Phase 5 — Steuerbilanz-Anteil

- Bei Mandanten mit Handelsbilanz und separater Steuerbilanz: beide möglich.
- Standardfall: Handelsbilanz mit Ueberleitungsrechnung.
- Steuerliche Wahlrechte hier ausgeuebt.

### Phase 6 — Wiedervorlage

- Folgejahr-E-Bilanz vorbereiten.
- Taxonomie-Updates jaehrlich.
- DATEV-Updates einspielen.

## Strategie und Praxis-Tipps

- E-Bilanz ist Standard für alle Bilanzierer.
- Bei groesseren Mandanten DATEV-E-Bilanz-Modul mit automatischer Taxonomie-Zuordnung.
- Pflicht-Felder strikt einhalten — Sendung wird sonst abgelehnt.
- Taxonomie-Updates zum 1. Januar jeden Jahres einspielen.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 5, 5b, 25.
- AO §§ 140, 141.
- BMF-Schreiben vom 28.09.2011 (IV C 6 - S 2133-b/11/10009) sowie Folgeschreiben.
- AEAO zu § 5b EStG.
- Verifikations-Hinweis: aktuelle Taxonomie-Version 2026 und Folgejahre über www.esteuer.de bzw. BMF-Newsletter prüfen.
