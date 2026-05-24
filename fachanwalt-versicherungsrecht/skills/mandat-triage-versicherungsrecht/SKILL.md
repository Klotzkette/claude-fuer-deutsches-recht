---
name: mandat-triage-versicherungsrecht
description: Strukturierte Eingangs-Abfrage fuer versicherungsrechtliche Mandate. Klaert Sparte (KFZ Haftpflicht Hausrat Gebaeude Lebensversicherung Berufsunfaehigkeit Krankenversicherung Rechtsschutz Industrieversicherung) Ereignis Stichtag Deckungsablehnung Hoehe der Forderung. Frist-Sofort-Check Verjaehrung drei Jahre § 195 BGB Klagefrist § 12 Abs. 3 VVG entfallen seit Reform 2008 aber AVB-Fristen pruefen Anzeigefrist Schadensmeldung. Eskalation Telefon-Sofort bei drohendem Existenzverlust (BU-Leistungsablehnung Krankheitskosten lebensbedrohlich). Routing zu deckungsanfrage-pruefen.
---

# Mandat-Triage Versicherungsrecht

## Zweck

Versicherungsmandate sind sparten-spezifisch — KFZ-Vollkasko ist anders als BU oder Industrieversicherung. Strukturierte Triage stellt sicher dass die richtige Bedingungslage zugrunde gelegt wird.

## Ablauf — sieben Fragen

### Frage 1 — Versicherungsnehmer oder Anspruchsteller?

- Versicherungsnehmer gegen eigene Versicherung (Erstrisikomandant)
- Geschädigter gegen Haftpflichtversicherer (Direktanspruch § 115 VVG)
- Versicherer als Mandant (Deckungsklage)
- Vermittler-Haftung

### Frage 2 — Sparte?

- KFZ-Vollkasko / Teilkasko / Haftpflicht
- Privathaftpflicht
- Hausrat / Gebäude
- Berufshaftpflicht
- Lebensversicherung (Erlebensfall Todesfall)
- Berufsunfähigkeit BU
- Krankenversicherung gesetzlich / privat
- Krankentagegeld
- Pflegeversicherung
- Rechtsschutz
- Insassenunfallversicherung
- Rentenversicherung (privat)
- Industrieversicherung Sonder-Industriedeckungen
- D&O Direktoren- und Manager-Haftpflicht
- Cyber-Versicherung

### Frage 3 — Akute Eilbedürftigkeit?

- BU-Ablehnung — kein Einkommen drohend
- Krankenversicherung weigert lebenswichtige Behandlung
- Hausrat-Brand kein Vorschuss
- Gewerbe-Betriebsunterbrechung
- Rechtsschutz-Deckungsablehnung mit drohender Verjährung Hauptverfahren

### Frage 4 — Versicherungsfall genau?

- Datum Ereignis
- Schadens-Höhe geschätzt
- Anzeige beim Versicherer Datum
- Bisherige Reaktion (Ablehnung Stillschweigen Teilzahlung)

### Frage 5 — Bedingungswerk?

- Police vorhanden?
- AVB welche Fassung?
- Tarif konkret bezeichnet?
- Risikofragebogen beim Vertragsschluss vorhanden?
- Versicherungsbeginn — technisch / formell

### Frage 6 — Frist?

- **Verjährung Versicherungsleistung** drei Jahre § 195 BGB ab Schluss des Jahres der Anspruchsentstehung und Kenntnis (§ 199 BGB)
- **AVB-Klagefrist** früher § 12 Abs. 3 VVG sechs Monate — seit VVG-Reform 2008 entfallen; aber manche älteren Verträge prüfen
- **Anzeigefrist** Schaden je nach AVB sieben Tage bis sofort
- **Wahrung der Frist durch Klage** bei Verjährung

### Frage 7 — Hauptaktenstand?

- Vollständiger Schriftwechsel?
- Bedingungswerk komplett?
- Schadensgutachten vorhanden?
- Bei BU ärztliches Gutachten?

## Routing-Matrix

| Sparte/Vorgang | Folge-Skill | Frist |
|---|---|---|
| Deckungsablehnung Sachsparte | `deckungsanfrage-pruefen` | drei Jahre Verjährung |
| BU-Ablehnung | `deckungsanfrage-pruefen` plus medizinische Gegenbegutachtung | drei Jahre |
| Leben Todesfall | `deckungsanfrage-pruefen` | drei Jahre |
| Krankenversicherung medizinische Notwendigkeit | (Skill kv-prüfung — perspektivisch) | drei Jahre |
| Rechtsschutz Deckungsablehnung | (Skill rs-deckung — perspektivisch) | drei Jahre |
| Direktanspruch Geschädigter | Skill aus `fachanwalt-verkehrsrecht` `unfall-haftungsquote-berechnen` | drei Jahre |
| Vermittlerhaftung | (Skill vermittler-haftung — perspektivisch) | drei Jahre |
| Industrieversicherung | (Skill industriedeckung — perspektivisch) | drei Jahre |

## Mandatsannahme

- **Konflikt-Check** — keine Mandate auf beiden Seiten der Versicherungs-Beziehung
- **Streitwert** ab EUR 10000 LG
- **Rechtsschutz-Deckungsanfrage** prüfen vor Mandatsannahme
- **Komplexität** AVB-Auslegung BGH-Urteilskette

## Eskalation

- **Telefon-Sofort** lebensbedrohliche KV-Ablehnung
- **Binnen einer Stunde** drohende Verjährung
- **Heute** Stellungnahme an Versicherung Rechtsschutz-Deckungsanfrage
- **Diese Woche** Klage-Erstentwurf

## Ausgabe

- `triage-protokoll-versicherungsrecht.md`
- Aktenanlage
- Rechtsschutz-Deckungsanfrage als Entwurf
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorarvereinbarung über RVG
- Empfehlung Folge-Skill

## Quellen

- VVG §§ 1 ff.
- BGB §§ 195 199 305 ff.
- BGH IV. Zivilsenat
- Prölss/Martin VVG
- Langheid/Wandt Münchener Kommentar
