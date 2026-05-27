---
name: mandat-triage-insolvenzrecht
description: "Eingangs-Abfrage fuer insolvenzrechtliche Mandate — Mandant ist Geschaeftsfuehrer mit Antragspflicht Glaeubiger der Forderung anmelden will oder Arbeitnehmer der Insolvenzgeld beantragt. Klaert Mandantenrolle und Vorgang (Eroeffnungsantrag Eigenverwaltung Schutzschirm StaRUG Restschuldbefreiung). Sofort-Fristen Antragspflicht § 15a InsO drei Wochen Anmeldefristen Insolvenzgeld § 165 SGB III zwei Monate. Normen §§ 13 17 18 19 InsO Eroeffnungsantrag Insolvenzgruende. Eskalation Telefon-Sofort bei Antragspflicht-Verletzung Geschaeftsfuehrer-Haftung. Output Triage-Memo Fristen-Ampel Routing zu anfechtungsrechte-pruefen und anderen Skills. Abgrenzung zu insolvenzrecht-kaltstart-interview (Plugin-Profil-Befuellung)."
---

# Mandat-Triage Insolvenzrecht

## Zweck

Insolvenz-Mandate sind hochzeitkritisch — die Drei-Wochen-Frist § 15a InsO ist strafbewehrt. Triage stellt sofort fest, ob die Antragspflicht akut ist.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Schuldner (Privatperson Selbstständig Gesellschaft)
- Geschäftsführer / Vorstand
- Gesellschafter
- Gläubiger einzelner
- Gläubiger-Banken
- Insolvenzverwalter
- Sachwalter (Eigenverwaltung)
- Arbeitnehmer
- Anfechtungs-Gegner

### Frage 2 — Vorgang?

- Antragspflicht-Prüfung § 15a InsO
- Eigenantrag stellen
- Gläubigerantrag erhalten — Reaktion
- Eigenverwaltung beantragen
- Schutzschirm § 270d InsO
- StaRUG-Verfahren
- Insolvenzgeld
- Forderungsanmeldung
- Insolvenzplan
- Anfechtungs-Verfahren
- Restschuldbefreiung
- Verbraucherinsolvenz
- Gesellschafter-Haftung
- Geschäftsführer-Haftung § 64 GmbHG a. F. / § 15b InsO

### Frage 3 — Akute Eilbedürftigkeit?

- **Antragspflicht** § 15a InsO drei Wochen — Strafbarkeit
- **Vermögensverschiebung** läuft / steht bevor
- **Massive Vermögensabflüsse** im Vorfeld
- **Gläubigerantrag** zugestellt
- **Insolvenzgericht** Termin morgen
- **Pfändung Konto** Existenz bedrohend
- **Arbeitnehmer Lohn-Ausstand**
- **Sanierungs-Krise** akut

### Frage 4 — Verfahrensstadium?

- Vor Antragspflicht — Beratung
- Antragspflicht akut
- Eröffnungsverfahren (vorläufiges Verfahren)
- Eröffnetes Verfahren
- Berichtstermin
- Prüfungstermin
- Schlussverteilung
- Aufhebung
- Wohlverhaltensphase

### Frage 5 — Schuldner-Form?

- Natürliche Person
- Selbstständig
- GmbH AG GmbH & Co. KG
- Personengesellschaft
- Verein
- Stiftung
- Genossenschaft
- Auslandsbezug (EuInsVO)

### Frage 6 — Wirtschaftliche Verhältnisse?

- Aktiva (Buchwert Verkehrswert)
- Passiva
- Liquidität-Stand
- Drohende Zahlungs-Unfähigkeit § 18 InsO
- Zahlungs-Unfähigkeit § 17 InsO
- Überschuldung § 19 InsO
- Fortbestehens-Prognose

### Frage 7 — Frist?

- **§ 15a InsO** drei Wochen Antragspflicht
- **Forderungsanmeldung** mit Anmeldefrist im Insolvenzgericht-Bekanntmachung
- **Anfechtungs-Verjährung** drei Jahre § 146 InsO
- **Restschuldbefreiungs-Antrag** mit Eigenantrag oder binnen einer Woche nach Aufforderung
- **Insolvenzgeld-Antrag** zwei Monate ab Insolvenz-Eröffnung § 165 SGB III

### Frage 8 — Besondere Konstellationen?

- Konzern-Insolvenz
- Eigenverwaltung möglich (Liquidität ausreichend Geschäftsführer geeignet)
- Schutzschirm-Verfahren möglich
- StaRUG vor Insolvenz?
- Auslandsbezug
- Familieninsolvenz

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Antragspflicht-Prüfung | `antragspflicht-15a-inso` |
| Gläubigerantrag erhalten | `glaeubigerantrag-pruefung` |
| Zahlungsunfähigkeit-Prüfung | `zahlungsunfaehigkeit-pruefung-17-inso` |
| Überschuldungs-Prüfung | `ueberschuldung-pruefung-19-inso` |
| Liquiditätsvorschau | `liquiditaetsvorschau-insolvenzrechtlich` |
| Anfechtungs-Verteidigung / -Aktivierung | `anfechtungsrechte-pruefen` |
| Fortbestehensprognose | weiter an `fortbestehensprognose`-Plugin |
| Plugin-Konfiguration | `kaltstart-interview` |
| Eigenverwaltung-Beratung | (Skill eigenverwaltung-beratung — perspektivisch) |
| StaRUG-Restrukturierung | (Skill starug-verfahren — perspektivisch) |
| Insolvenzplan | (Skill insolvenzplan — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** sehr strikt — Insolvenzverwalter Schuldner Gläubiger
- **Streitwert** bei Anfechtung Forderung Restmasse
- **Honorarvereinbarung** RVG / Insolvenzverwalter-Vergütung nach InsVV
- **Versicherungs-Deckung** D&O bei Geschäftsführer Berufshaftpflicht Insolvenzverwalter

## Eskalation

- **Telefon-Sofort** Antragspflicht-Frist Strafbarkeit
- **Binnen einer Stunde** Gläubigerantrag-Reaktion Vermögensverschiebung verhindern
- **Heute** Eigenantrag-Vorbereitung Forderungsanmeldung
- **Diese Woche** Insolvenzplan-Erstentwurf Anfechtungs-Klage

## Ausgabe

- `triage-protokoll-insolvenzrecht.md`
- Aktenanlage
- Frist im Fristenbuch (§ 15a InsO drei Wochen vorrangig)
- Sofort-Strategie-Vorschlag
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Quellen

- InsO §§ 1 ff. 15a 17 18 19 129 ff. 146 165 270 270d
- StaRUG
- GmbHG § 64 (a. F.) ersetzt durch § 15b InsO
- StGB §§ 283 ff.
- SGB III § 165
- BGH IX. Zivilsenat
- Uhlenbruck InsO
- MüKo InsO


## Weitere Leitentscheidungen — Mandats-Triage

- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Fortbestehensprognose in der Triage: erste Frage bei jedem Mandat ob Ueberschuldung vorliegt (zweistufig); positive Prognose heilt; negative Prognose loest Antragspflicht aus.
- BGH, Urt. v. 24.05.2005 — IX ZR 123/04, BGHZ 163, 134 — ZU-Schnellcheck in Triage: 10%-Luecken-Test; Zahlungsstockung 3-Wochen-Fenster; rasches Screening ermoeglichen.
- BGH, Urt. v. 06.05.2021 — IX ZR 72/20, NZI 2021, 631 — Mandats-Triage Anfechtungsrisiko: fruehere Anwaltstatigkeit des Mandatsanwalts in der Krise kann selbst Anfechtung ausloesen wenn Zahlungen an Kanzlei in letzten 3 Jahren; Konflikt-Check zwingend.
- BGH, Urt. v. 26.04.2018 — IX ZR 238/17, NZI 2018, 584 — Plan-Mandat Erstpruefung: bei Plan-Mandat als erste Massnahme Vergleichsrechnung (Liquidationswert) erstellen; Mandant muss wissen ob Plan besser als Liquidation.
