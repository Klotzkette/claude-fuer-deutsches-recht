---
name: wandelereignis-eingang
description: "Workflow nach Eingang der Wandlungserklaerung des Lenders: Dokumentation des Eingangs, Vier-Augen-Pruefung der formellen Voraussetzungen (Textform, Frist, vollstaendige Erklaerung), Eingangsbestaetigung und Weiterleitung an zustaendige Stellen. Phase C des Lebenszyklus."
---

# Wandelereignis – Eingang Wandlungserklärung

## Zweck

Dieser Skill strukturiert den Workflow nach Eingang der Wandlungserklärung des Lenders. Er prüft formelle Voraussetzungen, dokumentiert den Eingang und leitet den Prozess weiter. Phase C des Lebenszyklus.

## Eingaben

- Wandlungserklärung (Dokument oder E-Mail) des Lenders
- Wandeldarlehensvertrag (§§ 4.1, 4.4 zur Fristenprüfung)
- Datum der Wandlungsmitteilung der Gesellschaft (falls bereits erfolgt)
- Datum des Wandlungsereignisses (Qualified Financing, Maturity, Liquidation Event)

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform: Wandlungserklärung muss in Textform erfolgen)
- § 130 BGB (Zugang der Willenserklärung: Erklärung wirksam bei Zugang beim Empfänger)
- § 132 BGB (Zugang bei Verweigerung der Annahme)
- § 4.4 Wandeldarlehensvertrag (Frist: ein Monat nach Zugang Wandlungsmitteilung)
- § 286 BGB (Verzug bei Fristversäumnis der Gesellschaft)
- Zugangsfiktion bei einfachem Brief: seit Postrechtsmodernisierungsgesetz (PostModG, 1.1.2025) gilt regelmäßig **vier-Tage-Frist** ab Aufgabe zur Post (zuvor drei Tage); maßgeblich bei Berechnung der Wandlungsfrist, wenn Wandlungserklärung oder Wandlungsmitteilung postalisch verschickt wird

### Rechtsprechung
- BGH, Urt. v. 12. März 2009 – IX ZR 85/08 (Zugang von Erklärungen per E-Mail – Eingangszeitpunkt)
- BGH, Urt. v. 3. November 1982 – IVa ZR 204/80 (Wirksamkeit einseitiger Gestaltungserklärungen)

## Vorgehen

### 1. Eingang dokumentieren
Datum und Uhrzeit des Eingangs (E-Mail-Eingang im Postfach oder Briefeingang). Screenshot oder Eingangsbestätigung erstellen. Eingangsstempel anbringen.

### 2. Formelle Prüfung (Vier-Augen-Prinzip)
a) Textform (§ 126b BGB): Ist die Erklärung in lesbarer Form auf dauerhaftem Datenträger (E-Mail, PDF)?
b) Person des Erklärenden: Ist der Lender (oder sein Bevollmächtigter) eindeutig erkennbar?
c) Inhalt: Erklärung der Wandlungsabsicht für den gesamten offenen Betrag?
d) Frist: Innerhalb eines Monats nach Zugang der Wandlungsmitteilung (§ 4.4)?
e) Empfänger: An die Gesellschaft adressiert?

### 3. Inhaltliche Vollständigkeit prüfen
Enthält die Erklärung den Wandlungsbetrag (Darlehen + Zinsen), das Wandlungsereignis und den Stichtag? Falls nicht vollständig: Rückfrage an Lender.

### 4. Eingangsbestätigung senden
Bestätigung an Lender: „Ihre Wandlungserklärung vom [Datum] ist bei uns am [Datum] eingegangen und wird geprüft." Kein Anerkenntnis inhaltlicher Berechtigung.

### 5. Interne Weiterleitung
Weitergabe an zuständige Stellen: Gesellschaft (Geschäftsführerin), Gesellschafterinnen (Mitwirkungspflicht § 5 aktivieren), Steuerberater, Buchhaltung. Fristenkalender aktualisieren.

### 6. Nächste Schritte einleiten
Je nach Trigger-Typ: Skill `wandlungspruefung-trigger-qualified-financing`, `wandlungspruefung-trigger-maturity` oder `wandlungspruefung-trigger-liquidation` aufrufen.

## Beispiel-Eingangsbestätigung

```
Betreff: Eingangsbestätigung Wandlungserklärung vom [Datum]
An: Northstar Pre-Seed Partners GmbH & Co. KG

Sehr geehrte Damen und Herren,

wir bestätigen den Eingang Ihrer Wandlungserklärung vom [Datum] per E-Mail
am [Datum, Uhrzeit]. Ihre Erklärung wird formell und inhaltlich geprüft.
Wir melden uns innerhalb von fünf Bankarbeitstagen mit dem Ergebnis.

Mit freundlichen Grüßen
Dr. Mira Schoeneck, Geschäftsführerin
Sonnenglas Solartechnologie UG (haftungsbeschränkt)
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Wandlungserklärung nach Fristablauf | Erklärung verfristet, unwirksam für dieses Ereignis | Frist grenzwertig | Innerhalb der Frist |
| Erklärung nicht in Textform | Formunwirksamkeit | Mündliche Erklärung mit schriftlicher Bestätigung | Textform gewahrt |
| Betrag fehlerhaft | Nachklärung erforderlich | Kleinere Abweichung | Betrag vollständig korrekt |
| Kein Zugang nachweisbar | Zugangsproblematik | Einwurf-Einschreiben fehlt | Zugangsbeweis vorhanden |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-qualified-financing/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlung-kommunikation-paketverteilung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB Zugangsregeln aktualisieren.
