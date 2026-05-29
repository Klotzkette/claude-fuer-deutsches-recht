---
name: mandat-triage-sozialrecht
description: "Neues sozialrechtliches Mandat: Sekretariat oder Anwalt muss Sachgebiet klaeren und zum richtigen Skill weiterleiten. Eingangs-Triage Sozialrecht SGB I-XIV. Prüfraster: Sachgebiet (SGB II Buergergeld SGB V Krankenversicherung SGB VI Rente SGB IX Reha SGB XI Pflege SGB XII Sozialhilfe SGB VII Unfall) Sofort-Fristen Widerspruch 1 Monat § 84 SGG Klage 1 Monat § 87 SGG Untätigkeitsklage 6 Monate § 88 SGG. Output: Routing-Entscheidung mit Folge-Skill und Fristen. Abgrenzung zu mandanten-intake (Stammdaten) und sozialrecht-fallaufnahme-routing (Master-Routing)."
---

# Mandat-Triage Sozialrecht

## Zweck

Sozialrechts-Mandate sind heterogen über die zwölf SGBs und Nebengesetze. Triage stellt das richtige Sachgebiet und den richtigen Folge-Skill sicher — ergänzend zu `mandanten-intake` der die Stammdaten erfasst.

## Ablauf — sieben Fragen

### Frage 1 — Sachgebiet?

- **SGB II** Bürgergeld (vormals ALG II Hartz IV)
- **SGB III** Arbeitsförderung (Arbeitslosengeld I)
- **SGB V** Gesetzliche Krankenversicherung
- **SGB VI** Gesetzliche Rentenversicherung
- **SGB VII** Gesetzliche Unfallversicherung
- **SGB VIII** Kinder- und Jugendhilfe
- **SGB IX** Rehabilitation Schwerbehindertenrecht Eingliederungshilfe
- **SGB X** Verfahrensrecht Verwaltungsverfahren
- **SGB XI** Soziale Pflegeversicherung
- **SGB XII** Sozialhilfe
- **AsylbLG** Asylbewerberleistungs-Recht
- **BAföG** Ausbildungsförderung
- **WoGG** Wohngeld
- **KindG** Kindergeld
- **Familien- und Erziehungsgeld** BEEG ElterngeldPlus
- **SchwbR** Schwerbehindertenrecht (in SGB IX integriert)
- **Versorgungsrecht** Bundesversorgungsgesetz BVG
- **Beamtenrecht-versorgung** parallel zu SGB

### Frage 2 — Mandantenrolle?

- Antragsteller / Leistungsberechtigter
- Behörde (Erstattungsansprüche)
- Familienangehöriger
- Pflegeperson
- Arzt / Heilberufler (KV-Streit)
- Krankenkasse
- Sozialleistungs-Träger

### Frage 3 — Vorgang?

- Antrag-Stellung
- Bescheid erhalten — Widerspruch erwogen
- Widerspruchsverfahren läuft
- Klage am SG erhoben
- Berufung LSG
- Revision BSG
- Eilantrag § 86b SGG
- Schwerbehinderten-Feststellungs-Verfahren
- Erstattungs-Streit zwischen Leistungs-Trägern
- Beitragsrechtlicher Streit
- Versicherungs-Pflicht / -Status

### Frage 4 — Akute Eilbedürftigkeit?

- **Bürgergeld-Wegfall** existenzbedrohlich
- **Krankenversicherungs-Schutz** verloren
- **Hilfsmittel** lebenswichtig nicht bewilligt
- **Eingliederungshilfe** Schule beginnt
- **Wohnungsverlust** wegen Mietkosten-Übernahme
- **Klage-Frist** ein Monat läuft
- **Untätigkeit** sechs Monate erreicht — Klage statthaft

### Frage 5 — Stand?

- Beratung vor Antrag
- Antrag gestellt — wartet auf Bescheid
- Bescheid liegt vor — Widerspruchsfrist offen
- Widerspruchsbescheid — Klage Frist offen
- Klage erhoben
- LSG / BSG
- Verfassungsbeschwerde
- Eilantrag SG

### Frage 6 — Frist?

- **Widerspruchsfrist** ein Monat § 84 SGG
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr § 66 SGG
- **Klagefrist** ein Monat § 87 SGG
- **Untätigkeitsklage** sechs Monate § 88 SGG (drei Monate in Eilfällen)
- **Eilantrag** § 86b SGG keine starre Frist aber zeitnah
- **Wiedereinsetzung** § 27 SGB X ein Monat

### Frage 7 — Wirtschaftliche Verhältnisse?

- PKH wahrscheinlich
- Beratungshilfe vor Klage
- Anwaltszwang nur ab LSG (kein erstinstanzlich)
- Streitwert geringe Bedeutung (SG-Verfahren weitgehend gerichtskostenfrei)

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Erst-Intake Stammdaten | `mandanten-intake` |
| Bescheid analyse | `bescheidanalyse` |
| Widerspruch formulieren | `widerspruch-formulieren` |
| Bürgergeld prüfen | `buergergeld-pruefen` |
| Hilfsmittelantrag | `hilfsmittelantrag-pruefen` |
| Eingliederungshilfe Schule | `eingliederungshilfe-schule` |
| Eilantrag Sozialrecht | `eilantrag-sozialrecht` |
| Klage Sozialgericht | `klage-sozialgericht` |
| PKH-Antrag | `prozesskostenhilfe-antrag` |
| Akteneinsicht anfordern | `akteneinsicht-anfordern` |
| Akteneinsicht auswerten | `akteneinsicht-auswerten` |
| Anlagen erstellen | `anlagen-erstellen` |
| Fristenbuch | `fristenbuch-sozialrecht` |
| Frist-Berechnung Zustellung | `widerspruchsfrist-und-zustellung-sgb` |
| Schwerbehinderten GdB | (Skill schwerbehinderten-feststellung — perspektivisch) |
| Erwerbsminderung | (Skill erwerbsminderungs-rente — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** häufig unproblematisch (Behörde vs. Bürger)
- **PKH bzw. Beratungshilfe** häufig
- **Streitwert / Kostenrisiko** SG-Verfahren gerichtskostenfrei für Versicherte
- **Sprachbedarf** Dolmetscher bei Migrationshintergrund

## Eskalation

- **Telefon-Sofort** Bürgergeld-Wegfall existenzbedrohlich
- **Binnen einer Stunde** Eilantrag § 86b SGG
- **Heute** Widerspruchs-Frist heute / morgen
- **Diese Woche** Klage Erstentwurf

## Ausgabe

- `triage-protokoll-sozialrecht.md`
- Aktenanlage mit Verweis auf `mandanten-intake`
- Frist im Fristenbuch
- PKH-Antrag-Entwurf wenn relevant
- Mandatsvereinbarung
- Empfehlung Folge-Skill

## Quellen

- SGG §§ 66 84 86a 86b 87 88
- SGB X §§ 27 37 65
- SGB I — XII
- AsylbLG BAföG WoGG BEEG
- BSG Std.Spruch
- Krasney/Udsching SGG
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Aktuelle Rechtsprechung — allgemeine Verfahrensgrundsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.