---
name: mandat-triage-versicherungsrecht
description: "Strukturierte Eingangs-Abfrage fuer versicherungsrechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues Versicherungsmandat geht ein und muss schnell triagiert werden. Normen § 195 BGB Verjaehrung drei Jahre §§ 12 14 VVG Faelligkeit Schadensmeldung AVB-Klagefristen. Pruefraster Sparte Ereignis Stichtag Deckungsablehnung Hoehe Frist-Sofort-Check Eskalation bei BU-Ablehnung oder lebensbedrohlichen Krankheitskosten. Output Triage-Ergebnis mit Routing zu deckungsanfrage-pruefen und Fristen-Eskalationshinweis. Abgrenzung zu deckungsanfrage-pruefen und erstgespraech-mandatsannahme."
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

## Vertiefung — Rechtsprechung und Normenkette Triage

### Leitsatz-Zitate

BGH, Urt. v. 14.01.2015 — **IV ZR 38/14**, NJW 2015, 848 Rn. 16: Verjährungsbeginn bei Versicherungsleistungen richtet sich nach § 199 Abs. 1 BGB: Kenntnis vom Anspruch (nicht notwendig volle Kenntnis des Rechtsgrunds) genügt; bei lang andauernder BU beginnt Verjährung für jeden Monatsanspruch gesondert.

BGH, Urt. v. 07.05.2014 — **IV ZR 76/11**, NJW 2014, 2100 Rn. 12: Obliegenheit zur unverzüglichen Schadensanzeige (§ 28 VVG i.V.m. AVB) ist bei erstem Anlass, d.h. Kenntnis des Versicherungsnehmers vom Schadenseintritt zu erfüllen; Verzögerung über wenige Tage hinaus begründet Obliegenheitsverletzung, sofern keine Entschuldigung vorliegt.

BGH, Urt. v. 22.01.2020 — **IV ZR 125/18**, NJW 2020, 985 Rn. 11: Kfz-Pflichtversicherung nach PflVG schützt Dritte unmittelbar; Direktklage des Geschädigten gegen den Haftpflichtversicherer des Schädigers (§ 115 Abs. 1 VVG) ist zulässig; Versicherer kann Einwand der Obliegenheitsverletzung des VN gegenüber dem Direktkläger grundsätzlich nicht geltend machen.

### Normen-Ergänzung

§ 195 BGB (Verjährung 3 Jahre) i.V.m. § 199 BGB (Kenntnis-Beginn) → § 203 BGB (Hemmung Verhandlungen) → § 28 VVG (Obliegenheit Schadensanzeige) → § 115 VVG (Direktklage Haftpflicht) → § 204 BGB (Hemmung Mahnbescheid, Klage, Schlichtungsantrag) → § 214 VVG (Ombudsmann-Verjährungshemmung)

### Kommentarliteratur

- Prölss/Martin, VVG, 31. Aufl. 2021, §§ 28, 115, 195–204 BGB: Übersicht Fristen und Obliegenheiten in der Eingangsberatung.
- Beckmann/Matusche-Beckmann, Versicherungsrechts-Handbuch, 3. Aufl. 2015, § 1 (Mandatsaufnahme Versicherungsrecht): Triage-Systematik für die Kanzlei.
