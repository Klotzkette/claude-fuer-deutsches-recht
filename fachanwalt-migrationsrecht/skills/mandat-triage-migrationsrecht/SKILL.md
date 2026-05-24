---
name: mandat-triage-migrationsrecht
description: Strukturierte Eingangs-Abfrage fuer migrationsrechtliche Mandate. Klaert Vorgang (Asylantrag Visum-Erteilung Aufenthaltstitel-Verlaengerung Niederlassungserlaubnis Familiennachzug Abschiebungsandrohung Ausweisung Einbuergerung Schutz vor Abschiebung Dublin-III Asyl-Folgeantrag) Mandantenstatus Asylsuchender Geduldeter Anerkannter unerlaubt eingereist EU-Buerger Drittstaatsangehoeriger. Sofort-Fristen Asylklage zwei Wochen § 74 AsylG Abschiebungsandrohung einstweiliger Rechtsschutz § 80 Abs. 5 VwGO. Eskalation Telefon-Sofort bei Abschiebung in 24 Stunden Hafterhalt Ueberstellung Dublin. Routing zu aufenthaltstitel-pruefung.
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
