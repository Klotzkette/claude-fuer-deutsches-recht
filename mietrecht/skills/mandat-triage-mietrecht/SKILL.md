---
name: mandat-triage-mietrecht
description: Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkostenabrechnung Mietkaution-Rückforderung Eigenbedarf Sanierung Räumung WEG-Beschluss WEG-Hausgeld-Klage). Fristen-Sofort-Check Kündigungs-Frist nach § 573c BGB Räumungs-Frist § 721 ZPO WEG-Klage ein Monat § 45 WEG Modernisierung-Ankündigung drei Monate vorher Mieterhoehung Zustimmungs-Frist zwei Monate § 558b BGB. Eskalation Telefon-Sofort bei Räumungstermin laufender Kündigungs-Frist.
---

# Mandat-Triage Mietrecht

## Zweck

Mietrechts-Mandate sind heterogen — Wohnraummietrecht (sozial geschützt) Gewerbemietrecht (vertragsdominiert) WEG (eigene Logik). Triage stellt richtige Spur sicher.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Vermieter (Privat / Wohnungsunternehmen)
- Mieter
- WEG-Eigentümer (in eigener Sache)
- WEG-Verwalter / Hausverwaltung
- Sondereigentums-Verwalter
- Untermieter

### Frage 2 — Gegenstandsart?

- Wohnraum
- Gewerbe
- Garage / Stellplatz (separat oder im Mietvertrag enthalten)
- WEG (Sondereigentum + Gemeinschaftseigentum)
- Pacht
- Mischmietvertrag

### Frage 3 — Sachgebiet?

- **Kündigung** (ordentlich außerordentlich Eigenbedarf Zahlungsverzug)
- Räumung
- **Mieterhöhung** (Vergleichsmiete Modernisierung)
- **Mietminderung** (Mangel)
- Modernisierung
- **Nebenkostenabrechnung** (Erstellung Prüfung)
- **Mietkaution** Rückforderung
- **Schönheitsreparaturen** Anspruch
- Mietmangel-Anspruch
- WEG-Beschluss-Anfechtung
- WEG-Hausgeld-Klage / Forderung
- Räumungsfrist
- Anschlussraum (Garage Stellplatz)
- Untermiete

### Frage 4 — Akute Eilbedürftigkeit?

- **Räumungstermin** binnen Tagen — Räumungsschutz
- **Kündigung gestern erhalten** Klage-Frist nach Vorbemerkung
- **Eigenbedarfsräumung droht** Räumungsklage zugestellt
- **Modernisierung morgen** unzumutbar
- **Mietminderungs-Stopp** Vermieter klagt Mietrückstand
- **Schimmelbefall lebensbedrohlich**
- **WEG-Beschluss-Anfechtung** ein-Monats-Frist

### Frage 5 — Vertragsbasis?

- Schriftlicher Mietvertrag (Datum)
- Mündlicher Mietvertrag
- Wohnraum-Mietvertrag mit gestaffelten Mieten / Indexmiete
- Gewerbemietvertrag
- WEG-Gemeinschaftsordnung
- Teilungserklärung

### Frage 6 — Frist?

- **Kündigungs-Frist Vermieter** § 573c BGB drei Monate (bei langer Mietdauer länger)
- **Kündigungs-Frist Mieter** drei Monate (nicht abhängig von Mietdauer)
- **Räumungsfrist Vollstreckung** § 721 ZPO Gewährung
- **Mieterhöhungs-Zustimmungsfrist § 558b BGB** zwei Monate
- **Mietminderungs-Anzeige** § 536c BGB unverzüglich
- **Betriebskostenabrechnung** § 556 Abs. 3 BGB zwölf Monate
- **WEG-Beschluss-Anfechtung** § 45 WEG ein Monat

### Frage 7 — Wirtschaftliche Verhältnisse?

- Miete-Volumen
- Eigenkapital (Mietkaution Selbstbeteiligung)
- Rechtsschutz Mieter Vermieter
- PKH bei Mieter

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Eigenbedarfskündigung erstellen | `eigenbedarfskuendigung-erstellen` |
| Mieterhöhung — Vermieter | `mieterhoehungsverlangen-erstellen` |
| Mieterhöhung — Mieter | `mieterhoehung-pruefen-widersprechen` |
| Mietsenkungsverlangen | `mietsenkungsverlangen` |
| Nebenkosten erstellen | `nebenkostenabrechnung-erstellen` |
| Nebenkosten prüfen | `nebenkostenabrechnung-pruefen` |
| Klage am AG | `klageentwurf-amtsgericht` |
| Mahnung Zahlungsverzug | `mahnung-zahlungsverzug-mieter` |
| Mieteranfragen beantworten | `mieteranfragen-beantworten` |
| Lage und Ausstattung erheben | `lage-und-ausstattung-erheben` |
| WEG-Beschluss-Anfechtung | `weg-beschluss-anfechten` |
| Mietkaution-Rückforderung | (Skill mietkaution-rueckforderung — perspektivisch) |
| Mietminderung wegen Mangel | (Skill mietminderung-prüfen — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Mieter/Vermieter
- **Streitwert** Wohnraum Jahresmiete EUR (KSchG-Streitwert vergleichbar)
- **AG-Zuständigkeit** Mietrecht-Streit über Wohnraum § 23 Nr. 2 a) GVG ausschließlich AG
- **Versicherungs-Deckung** Mietrechtsschutz häufig

## Eskalation

- **Telefon-Sofort** Räumungstermin Räumungsklage Schimmel
- **Binnen einer Stunde** WEG-Beschluss-Anfechtung Frist läuft heute
- **Heute** Kündigungs-Widerspruch Mieterhöhungs-Antwort
- **Diese Woche** Klageschrift Räumungsschutz

## Ausgabe

- `triage-protokoll-mietrecht.md`
- Aktenanlage
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 535 ff. 558 558b 573c 556
- WEG §§ 14 19 20 44 45
- ZPO § 721 (Räumungsfrist)
- BGH VIII. Zivilsenat V. Zivilsenat
- Schmidt-Futterer Mietrecht
- Sternel Mietrecht aktuell

## Aktuelle Rechtsprechung — Leitsaetze (Triage-Relevant)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
