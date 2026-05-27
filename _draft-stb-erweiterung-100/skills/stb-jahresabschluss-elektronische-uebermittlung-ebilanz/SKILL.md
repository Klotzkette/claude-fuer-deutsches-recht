---
name: stb-jahresabschluss-elektronische-uebermittlung-ebilanz
description: "E-Bilanz § 5b EStG elektronische Uebermittlung. Anwendungsfall Bilanzierer Pflicht zur elektronischen Uebermittlung der Steuerbilanz an FA Taxonomie-Standard. Methodik DATEV-E-Bilanz Modul. Output E-Bilanz uebermittelt."
---

# E-Bilanz — § 5b EStG elektronische Uebermittlung

## Kernsachverhalt

§ 5b EStG verpflichtet alle Bilanzierer zur elektronischen Uebermittlung der Steuerbilanz an das Finanzamt (E-Bilanz). Die Uebermittlung erfolgt im XBRL-Format ueber eine standardisierte Taxonomie. Frist parallel zur Steuererklaerung. Bei Mandanten mit Handelsbilanz und Steuerbilanz: beide oder Ueberleitung uebermitteln.

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

- BMF v. 28.09.2011 zu E-Bilanz.
- BMF jaehrliche Taxonomie-Aktualisierung.

## Workflow

### Phase 1 — Pflicht-Pruefung

- Bilanzierer nach § 5 EStG: E-Bilanz Pflicht.
- EUER-Steuerpflichtige (§ 4 Abs. 3 EStG): keine E-Bilanz, Anlage EUER.
- Personengesellschaften mit Bilanzierungspflicht.

### Phase 2 — Taxonomie

- Aktuelle Taxonomie (BMF-Verzeichnis ueber bzst.de).
- Pflichtfelder pruefen.
- Optionale Felder bei Bedarf nutzen.

### Phase 3 — Konten-Zuordnung

- Standard-Konten SKR 03 / SKR 04 sind taxonomie-konform.
- Individuelle Konten: manuelle Zuordnung.
- DATEV-E-Bilanz-Modul automatisiert.

### Phase 4 — Uebermittlung

- ELSTER-Zugang.
- XBRL-Dokument generieren.
- Sendung an FA.
- Quittung mit Transaktions-Nummer.

### Phase 5 — Steuerbilanz-Anteil

- Bei Mandanten mit Handelsbilanz und separater Steuerbilanz: beide moeglich.
- Standardfall: Handelsbilanz mit Ueberleitungsrechnung.
- Steuerliche Wahlrechte hier ausgeuebt.

### Phase 6 — Wiedervorlage

- Folgejahr-E-Bilanz vorbereiten.
- Taxonomie-Updates jaehrlich.
- DATEV-Updates einspielen.

## Output

- E-Bilanz uebermittelt.
- ELSTER-Quittung.
- Steuererklaerung mit E-Bilanz-Bezug.

## Strategie und Praxis-Tipps

- E-Bilanz ist Standard fuer alle Bilanzierer.
- Bei groesseren Mandanten DATEV-E-Bilanz-Modul mit automatischer Taxonomie-Zuordnung.
- Pflicht-Felder strikt einhalten — Sendung wird sonst abgelehnt.
- Taxonomie-Updates zum 1. Januar jeden Jahres einspielen.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.
- `stb-bwa-kontenrahmen-skr03-skr04` — Kontenrahmen.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 5, 5b, 25.
- AO §§ 140, 141.
- BMF v. 28.09.2011.
- Verifikations-Hinweis: aktuelle Taxonomie 2026 ueber BMF/BZSt.
