---
name: mandantenakte-anlegen
description: Legt eine Mandantenakte nach Kanzleikonvention an. Erfasst Stammdaten Bevollmaechtigte Mandatsumfang Konfliktpruefung (§ 43a Abs. 4 BRAO § 3 BORA) Datenschutzhinweis (Art. 13 DSGVO) Geldwaesche-Identifizierung (§§ 10 11 GwG) Honorarvereinbarung oder RVG-Hinweis. Erzeugt Aktenstruktur unter mandate/Aktenzeichen/ mit Standardunterordnern Vollmachts-Entwurf Datenschutzhinweis Geldwaesche-Pruefbeleg. Eintrag im Mandantenstamm. Verbindung zum Fristenbuch falls Fristen mitgeliefert.
---

# Mandantenakte anlegen

## Konfliktprüfung (§ 43a Abs. 4 BRAO)

**Vor jeder Mandatsannahme** Pflichtschritt:

- Prüfung im Mandantenstamm ob Mandat gegen einen bisherigen oder laufenden Mandanten der Kanzlei.
- Prüfung ob Mandatsannahme gegen § 3 BORA (widerstreitende Interessen) verstoesst.
- Bei Konflikt: Mandat ablehnen oder schriftliches Einverständnis aller Betroffenen.
- Prüfer-Eintrag mit Datum Initialen.

## Aktennummernsystem

Empfehlung:

`<Jahr>/<lfd. Nr.>` (z. B. `2026/0042`)

oder

`<RG>-<Jahr>-<Nr>` (z. B. `Z-2026-0042` für Zivilrecht).

## Verzeichnisstruktur

Unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandate/<az>/`:

```
01_stammdaten/
  mandatsblatt.md
  vollmacht.docx
  vollmacht-unterschrieben.pdf
  datenschutzhinweis.md
  gwg-identifizierung.pdf
  konfliktprüfung.md
  honorarvereinbarung.docx (falls Vereinbarung)
02_eingaenge/
03_schriftsaetze/
04_anlagen/
05_fristen/
06_honorar/
  rechnungen/
  zahlungseingang.yaml
07_korrespondenz_mandant/
08_korrespondenz_dritte/
09_aktennotizen/
_archiv/
```

## Mandatsblatt

```yaml
mandat-az: 2026/0042
mandat-eroeffnet: 2026-05-20
zustaendiger-anwalt: RA Mueller
sekretariat: Frau Schmidt

mandant:
  typ: juristische-person  # juristische-person / natürliche-person / ehepaare-vergleichsweise
  name: Mueller GmbH
  anschrift: ...
  rechtsform: GmbH
  vertretungsberechtigte: Hans Mueller (Geschäftsführer)
  registergericht: HRB ... AG München
  ust-id: DE...
  steuernummer: ...

ansprechpartner:
  name: Hans Mueller
  funktion: Geschäftsführer
  telefon: ...
  e-mail: ...

mandatsumfang:
  beschreibung: Verteidigung in Zivilrechtsstreit gegen ABC GmbH (Klage)
  rechtsgebiet: Zivilrecht / Vertragsrecht
  instanz: 1. Instanz LG München
  streitwert: 35.000 EUR

honorar:
  basis: rvg  # rvg / vereinbarung
  stundensatz: 320  # bei Vereinbarung
  pkh-pruefung: nein

konfliktpruefung:
  erfolgt-am: 2026-05-20
  ergebnis: kein-konflikt
  geprueft-von: RA Mueller
```

## Vollmacht

Vollmachtstext mit:

- Beauftragung des Rechtsanwalts der Kanzlei.
- Mandatsumfang konkret bezeichnet (Vorverfahren Klage Vergleich auch über Klageweg hinaus).
- Untervollmacht und Substituierung.
- Empfangsvollmacht für Zustellungen.
- beA-Vollmacht.
- Datum und Unterschrift des Mandanten.

## Datenschutzhinweis (Art. 13 DSGVO)

Standardhinweis mit:

- Identität des Verantwortlichen (Kanzlei).
- Zweck der Verarbeitung (Mandatsdurchführung).
- Rechtsgrundlage (Art. 6 Abs. 1 lit. b DSGVO + § 50 BRAO Aktenführung).
- Empfänger (Gericht Behörde Steuerberater Gegenseite — je nach Bedarf).
- Speicherdauer (mindestens 6 Jahre nach Mandatsende § 50 Abs. 1 BRAO).
- Betroffenenrechte (Auskunft Berichtigung Löschung Widerspruch).

## Geldwäsche-Identifizierung (§§ 10 11 GwG)

Bei Mandaten die unter GwG fallen (z. B. Immobilientransaktionen Bargeldgeschäfte ab Schwellenwert):

- Identifizierung der natürlichen Person mit Lichtbildausweis Kopie.
- Bei juristischer Person Registerauszug HRB plus wirtschaftlich Berechtigte nach Transparenzregister.
- Prüfung gegen Sanktionslisten EU und nationale.
- Prüfer-Eintrag mit Datum Initialen.

## Mandantenstamm-Eintrag

In `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandantenstamm.yaml`:

```yaml
- mandant-id: M-00874
  name: Mueller GmbH
  typ: juristische-person
  mandate:
    - 2026/0042
  konfliktstatus: kein-konflikt
  letzte-pruefung: 2026-05-20
```

## Audit

- Aktenanlage mit Audit-Eintrag (Datum Anwalt Sekretariat).
- Änderungen mit Audit-Trail.

## Ausgabe

- Vollständige Aktenstruktur.
- Mandatsblatt und Pflichtdokumente.
- Eintrag im Mandantenstamm.
- Hinweis ans Fristenbuch falls Fristen sofort relevant.
