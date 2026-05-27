---
name: mandat-triage-migrationsrecht
description: "Eingangs-Abfrage fuer migrationsrechtliche Mandate — Mandant ist Asylsuchender Geduldeter oder fragt nach Aufenthaltstitel Familiennachzug Abschiebungsabwehr Ausweisung oder Einbuergerung. Sofort-Fristen § 74 AsylG zwei-Wochen-Klagefrist § 36 AsylG ein-Wochen-Frist Eilantrag § 80 Abs. 5 VwGO bei Abschiebungsandrohung. Normen AufenthG AsylG § 27 AufenthG Familiennachzug. Eskalation Telefon-Sofort bei Abschiebung in 24 Stunden Haft Dublin-Ueberstellung. Output Triage-Memo Fristen-Ampel Routing zu aufenthaltstitel-pruefung und Spezial-Skills. Abgrenzung zu erstgespraech-mandatsannahme (Mandatsaufnahme-Leitfaden)."
---

# Mandat-Triage Migrationsrecht

## Zweck

Migrationsmandate sind hochgradig zeitkritisch — Abschiebung kann in Stunden erfolgen. Triage stellt Sofort-Eilbedürftigkeit fest und ordnet zu.

## Ablauf — sieben Fragen

### Frage 1 — Akute Eilbedürftigkeit?

- **Abschiebung angekündigt / im Gange** — sofortiger Eilrechtsschutz
- **Abschiebungs-Haft** — Haftbeschwerde
- **Dublin-Überstellung** in einen anderen EU-Staat
- **Asylklage-Frist** zwei Wochen § 74 AsylG
- **Visum-Ablehnung** Klage drei Monate / mit Remonstration
- **Ausreisepflicht-Frist abgelaufen**
- **Aktuelle Festnahme** an Grenze oder im Inland

**Bei JA:** Telefon-Sofort an Anwalt — Eilantrag § 80 Abs. 5 VwGO innerhalb Stunden.

### Frage 2 — Mandantenstatus aktuell?

- Asylsuchend (Aufenthaltsgestattung)
- Asyl anerkannt (Aufenthaltserlaubnis nach § 25 AufenthG)
- Subsidiär geschützt
- Abschiebungs-Verbot (§ 60 Abs. 5 oder Abs. 7 AufenthG)
- Geduldet (§ 60a AufenthG)
- Aufenthaltserlaubnis besitzend (Zweck spezifisch)
- Niederlassungserlaubnis
- Daueraufenthalt-EU
- Unerlaubt eingereist / illegal aufhältig
- EU-Bürger Freizügigkeit
- Drittstaatsangehöriger anderweitig

### Frage 3 — Vorgang?

- Asylantrag stellen
- Asyl-Folgeantrag § 71 AsylG
- Asyl-Klage gegen BAMF
- Visum-Erteilung beantragen / klagen
- Aufenthaltstitel-Verlängerung
- Niederlassungserlaubnis beantragen
- Familiennachzug-Verfahren
- Abschiebung verhindern / Eilrechtsschutz
- Duldung beantragen § 60a AufenthG
- Einbürgerung
- Ausweisung anfechten
- Identitätsklärung
- Dublin-Verfahren

### Frage 4 — Stand des Verfahrens?

- Antrag noch nicht gestellt — Beratungsbedarf
- Antrag gestellt — wartet auf Bescheid
- Anhörung BAMF Ausländerbehörde
- Bescheid liegt vor — Klagefrist offen
- Klage erhoben (Az VG)
- Berufung / OVG
- Eilantrag § 80 Abs. 5 VwGO oder § 123 VwGO
- Bundesverfassungsgericht Verfassungsbeschwerde

### Frage 5 — Familienverhältnisse?

- Familie in Deutschland (Ehegatte Kinder)
- Familie im Herkunftsland
- Minderjährig
- Familien-Asylanerkennung § 26 AsylG
- Beistandsgemeinschaft mit deutschen Familienangehörigen
- Kindeswohl

### Frage 6 — Frist?

- **Asylklage** zwei Wochen § 74 AsylG
- **Asyl-Eilantrag** bei sofortiger Vollziehung sofort
- **Visum-Remonstration** keine Frist aber zeitnah
- **Klage gegen Visum-Versagung** ein Monat § 74 VwGO
- **Aufenthaltstitel-Antrag** vor Ablauf des bestehenden Titels — fiktive Fortgeltung § 81 Abs. 4 AufenthG
- **Einbürgerungs-Frist** keine

### Frage 7 — Sprache und Dolmetscher?

- Muttersprache
- Deutsch-Kenntnisse
- Dolmetscher-Bedarf für Mandantengespräch
- Mandanten-Dokumente Übersetzungsbedarf

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Aufenthaltstitel-Verlängerung / Neuantrag | `aufenthaltstitel-pruefung` |
| Asylantrag / Klage | (Skill asyl-anhoerung-und-klage — perspektivisch) |
| Visum-Klage | weiter an `mandat-triage-verwaltungsrecht` plus Migrationsspezifikum |
| Familiennachzug | `aufenthaltstitel-pruefung` plus Familiennachzugs-Schwerpunkt |
| Abschiebung-Eilrechtsschutz | EILMODUS sofort |
| Ausweisung anfechten | (Skill ausweisung-anfechten — perspektivisch) |
| Einbürgerung | (Skill einbürgerung-staag — perspektivisch) |

## Eilmodus Abschiebung

Bei drohender Abschiebung:

1. Sofort Mandant identifizieren — wo? Abschiebehaft / Ausreise gefordert?
2. Ausländerakte-Auskunft sofort beantragen
3. Eilantrag VG § 123 VwGO mit Sofortvollziehbarkeits-Aussetzung
4. Hilfsweise Verfassungsbeschwerde
5. Folgeantrag § 71 AsylG wenn neue Tatsachen / Beweise
6. Petition Härtefall-Kommission

## Mandatsannahme

- **Konflikt-Check** — keine Doppelvertretung Behörde / Mandant
- **Prozesskostenhilfe** § 166 VwGO iVm § 114 ZPO häufig
- **Streitwert** § 52 GKG Asyl typisch EUR 5000
- **Beratungshilfe** außergerichtlich
- **Sprache** Dolmetscher

## Eskalation

- **Telefon-Sofort** Abschiebung morgen Überstellung Dublin morgen Festnahme Grenze
- **Binnen einer Stunde** Eilantrag § 80 Abs. 5 VwGO
- **Heute** Asyl-Klage Frist zwei Wochen
- **Diese Woche** Aufenthaltstitel-Antrag Niederlassungs-Antrag

## Ausgabe

- `triage-protokoll-migrationsrecht.md`
- Aktenanlage mit Sprache und Dolmetscher-Bedarf
- Frist im Fristenbuch (Asyl zwei Wochen Klage ein Monat)
- PKH-Antrag-Entwurf
- Mandatsvereinbarung
- Empfehlung Folge-Skill plus eventuell Härtefall-Kommission

## Quellen

- AufenthG AsylG StAG VwGO §§ 80 123
- DublinIII-VO (EU) 604/2013
- BVerwGE Std.Spruch
- Hailbronner AuslR
- Bergmann/Dienelt AusländerR

## Vertiefung: Rechtsprechung und Leitsaetze

- BVerfG, Beschl. v. 12.05.2005 - 2 BvR 569/05, NJW 2005, 1858 — Eilrechtsschutz im Migrationsrecht: Gericht muss Grundrechte auch im beschleunigten Verfahren beachten; PKH-Bewilligung darf Eilbeduerftigkeit nicht ignorieren; effektiver Rechtsschutz Art. 19 Abs. 4 GG gilt auch bei drohender Abschiebung.
- BVerwG, Urt. v. 27.04.2010 - 10 C 4.09, BVerwGE 136, 360 — Wiederaufgreifenspruefung bei Folgeantrag: BAMF prueft zunaechst Zulaessigkeit; Gericht kann bei offensichtlich zulaessigem Folgeantrag Eilrechtsschutz gewaehren auch bevor BAMF entschieden hat.
- BVerwG, Urt. v. 14.12.2016 - 1 C 4.16, BVerwGE 157, 18 — Streitwert im Asylverfahren: § 52 Abs. 2 GKG Regelstreitwert EUR 5.000; gerichtskostenfrei nach § 83b AsylG; bei Abschiebungsverbot § 60 AufenthG Streitwert EUR 2.500.

## Normen-Kette Triage

- **§ 36 AsylG** — 1-Woche-Klagefrist bei offensichtlich unbegruedet; § 74 Abs. 1 AsylG — 2-Wochen-Klagefrist
- **§§ 80 Abs. 5, 123 VwGO** — Eilrechtsschutzoptionen
- **§ 52 GKG** — Streitwert (Abs. 2: EUR 5.000 Regelwert Asyl)
- **§ 83b AsylG** — Gerichtskostenfreiheit im Asylverfahren
- **§§ 166 VwGO, 114 ZPO** — PKH im Verwaltungsverfahren
- **§ 71 AsylG** — Folgeantrag bei Wiederaufgreifensgruenden

## Output-Template: Triage-Protokoll Migrationsrecht

**Adressat:** Kanzlei-intern
**Tonfall:** Strukturiert; aktionsorientiert

```
TRIAGE-PROTOKOLL MIGRATIONSRECHT
Datum: [DATUM] — Anruf / Walk-in / E-Mail
Bearbeiterin: [RA-NAME]

1. MANDANT
Name: [NAME, geb. DATUM, Staatsang.]
Aufenthaltsstatus: [Gestattung / Duldung / AE § X / NE / illegal]
Sprache / Dolmetscher: [SPRACHE; Dolmetscher erforderlich: ja/nein]

2. AKUTE EILBEDUERFTIGKEIT (Checkboxen)
[ ] Abschiebung angekuendigt — Datum: [...]
[ ] Asylklage-Frist 2 Wochen — laeuft ab: [DATUM]
[ ] § 36 AsylG 1-Woche-Frist — laeuft ab: [DATUM]
[ ] Dublin-Ueberstellung droht
[ ] Abschiebehaft
[ ] Sonstige Eilbeduerftigkeit: [...]

3. VORGANG
[ ] Asylantrag / BAMF-Anhoerung
[ ] Asyl-Klage
[ ] Folgeantrag § 71 AsylG
[ ] Aufenthaltstitel-Antrag / Verlaengerung
[ ] Familiennachzug
[ ] Abschiebungsabwehr Eilantrag
[ ] Ausweisung Widerspruch
[ ] Einbuergerung
[ ] Grenzverfahren GEAS

4. FRISTEN IM KALENDER
Naechste Frist: [DATUM — Art der Frist]
PKH-Antrag: [gestellt / noch nicht / nicht erforderlich]

5. ROUTING
Folge-Skill: [skill-name]
Eskalation: [ ] Sofort-Telefon [ ] Heute [ ] Diese Woche

Aktennummer: [AZ]
```
