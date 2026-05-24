---
name: mandat-triage-bau-architektenrecht
description: Strukturierte Eingangs-Abfrage fuer bau- und architektenrechtliche Mandate. Klaert Mandantenrolle (Bauherr Unternehmer Subunternehmer Architekt Bautraeger Investor) Vertragstyp (BGB-Werkvertrag VOB/B-Werkvertrag Verbraucherbauvertrag Bautraegervertrag § 650 ff. BGB Architektenvertrag § 650p) Phase (vor Vertragsschluss Bauphase nach Abnahme Streit ueber Mangel ueber Schlussrechnung) Fristen Verjaehrung § 634a BGB Vertragsstrafen Abschlagsrechnungen. Eskalation Telefon-Sofort bei Bauunterbrechung drohendem Baustillstand Insolvenz Auftragnehmer. Routing zu werkmangel-vob-bgb-pruefen.
---

# Mandat-Triage Bau- und Architektenrecht

## Zweck

Baurecht-Mandate hängen massiv vom Vertragstyp und der Mandantenrolle ab. Triage stellt sicher dass das richtige Bedingungswerk und die richtige Norm angewendet werden.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Privater Bauherr (Verbraucherbauvertrag — § 650i BGB)
- Gewerblicher Bauherr / Investor
- Bauunternehmer / Generalunternehmer
- Subunternehmer / Nachunternehmer
- Architekt / Ingenieur (Planung Bauüberwachung)
- Bauträger
- Sachverständiger

### Frage 2 — Vertragstyp?

- BGB-Werkvertrag §§ 631 ff.
- VOB/B-Werkvertrag (Einbeziehung wirksam?)
- Verbraucherbauvertrag § 650i ff. BGB
- Bauträgervertrag § 650u BGB plus MaBV
- Architektenvertrag § 650p ff. BGB
- HOAI-Honorarstreit
- Public-Vergaberecht (an `fachanwalt-vergaberecht` weiter)

### Frage 3 — Phase?

- Vor Vertragsschluss (Beratung Vertragsentwurf)
- Während Bauphase (Ausführung Nachträge Behinderungen)
- Abnahme (anstehend strittig)
- Nach Abnahme — Mängel
- Schlussrechnung — Streit über Vergütung
- Insolvenz Auftragnehmer
- Insolvenz Bauherr

### Frage 4 — Akute Eilbedürftigkeit?

- Bauunterbrechung droht
- Sicherheitsleistung-Anspruch § 650f BGB
- Bauhandwerker-Sicherungshypothek § 650e BGB
- Insolvenz des Auftragnehmers
- Witterungsbedingt fristkritische Arbeiten
- Vertragsstrafe verwirkt vor Abnahme

### Frage 5 — Streitgegenstand?

- Mangel
- Nachtrag (Anordnung § 650b BGB nicht erfüllt)
- Vergütung Schlussrechnung
- Verzug
- Mehrkostenforderung
- Vertragsbeendigung Kündigung § 648a BGB außerordentlich aus wichtigem Grund
- Architekten-Planungs-/Überwachungsfehler

### Frage 6 — Abnahme erfolgt?

- Ja förmlich (Datum Protokoll)
- Ja konkludent (Ingebrauchnahme)
- Ja fiktiv § 640 Abs. 2 BGB
- Nein — strittig
- Verweigerungsrecht? Wesentlicher Mangel?

### Frage 7 — Frist?

- Verjährung Bauwerk-Mangel fünf Jahre § 634a BGB
- VOB/B vier Jahre § 13 Abs. 4
- Vertragsstrafe-Anspruch — Vorbehalt bei Abnahme § 341 Abs. 3 BGB

### Frage 8 — Wirtschaftliche Verhältnisse?

- Berufshaftpflichtversicherung Architekt
- Bauherrenhaftpflicht
- Bauwesensversicherung
- Insolvenz droht?

## Routing-Matrix

| Streitgegenstand | Folge-Skill |
|---|---|
| Mangel-Auseinandersetzung | `werkmangel-vob-bgb-pruefen` |
| Schlussrechnung | (Skill schlussrechnung-prüfen — perspektivisch) |
| Nachtrag § 650b BGB | (Skill nachtragsmanagement — perspektivisch) |
| Bauhandwerkersicherungshypothek | (Skill sicherungs-hypothek — perspektivisch) |
| Architekten-Haftung Planungs/Überwachung | `werkmangel-vob-bgb-pruefen` plus Architekten-Spezifikum |
| Insolvenz Auftragnehmer | weiter an `mandat-triage-insolvenzrecht` |
| Vergabe öffentliche Hand | weiter an `mandat-triage-vergaberecht` |

## Mandatsannahme

- **Konflikt-Check** — keine doppelte Vertretung Bauherr/Unternehmer/Architekt selbe Sache
- **Streitwert** bei Mängeln Mangelbeseitigungskosten; bei Vergütung restl. Vergütung; bei Architektenhonorar Differenz nach HOAI
- **Sachverständigen-Bedarf** Bauschäden oft SV nötig
- **Versicherungsdeckung** klären

## Eskalation

- **Telefon-Sofort** Bauunterbrechung Sicherheitsleistung Insolvenz-Eröffnung
- **Binnen einer Stunde** Mangelbeseitigungsfrist droht Fristablauf
- **Heute** Mangelrüge Vorbehalt bei Abnahme
- **Diese Woche** Klage-Erstentwurf Sachverständigenauftrag

## Ausgabe

- `triage-protokoll-baurecht.md`
- Aktenanlage
- Frist im Fristenbuch
- Mandatsvereinbarung mit Streitwertabschätzung
- Empfehlung Folge-Skill plus eventuell Sachverständigenauftrag

## Quellen

- BGB §§ 631 ff. 650 ff. 650e 650f 650i 650p 650u
- VOB/B
- HOAI
- BGH VII. Zivilsenat
- Werner/Pastor Bauprozess
