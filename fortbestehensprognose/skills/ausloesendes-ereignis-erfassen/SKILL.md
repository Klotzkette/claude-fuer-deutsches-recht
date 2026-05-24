---
name: ausloesendes-ereignis-erfassen
description: Erfasst den Anlass der Fortbestehensprognose. Typische Ausloeser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftspruefers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass Gesellschafterhinweis eigene Sorge des Geschaeftsfuehrers. Dokumentiert Anlass Datum Hinweisgeber Mitteilungsform. Wichtig fuer spaeteren Nachweis dass der Geschaeftsfuehrer auf Insolvenzanzeichen rechtzeitig reagiert hat (Haftungsfrage § 15b InsO).
---

# Auslösendes Ereignis erfassen

## Zweck

Die Fortbestehensprognose ist kein Selbstzweck — sie ist die Antwort auf einen konkreten Anlass. Der Anlass wird dokumentiert weil **er Beweis ist**: bei späteren Haftungsfragen (§ 15b InsO, § 43 GmbHG, § 826 BGB ggue Gläubigern) zeigt die Dokumentation dass der Geschäftsführer **zeitnah** auf Anzeichen reagiert hat.

## Typische Auslöser

### 1. Hinweis des Steuerberaters nach § 102 StaRUG

Seit 01.01.2021 hat der Steuerberater eine **Hinweispflicht**: wenn ihm bei der Bilanzaufstellung Anhaltspunkte für einen möglichen Insolvenzeröffnungsgrund auffallen muss er den Mandanten darauf hinweisen.

- Datum des Hinweises (schriftlich / mündlich / im Gespräch)
- Wortlaut wenn schriftlich
- Konkrete Anhaltspunkte die der StB genannt hat
- Quittierung des Hinweises durch den Mandanten

### 2. Hinweis des Wirtschaftsprüfers

Bei prüfungspflichtigen Gesellschaften (mittelgroße oder große KapGes nach § 267 HGB) kann der Prüfer im Rahmen des Jahresabschlusses einen **Hinweis zur Going-Concern-Annahme** geben oder den Bestätigungsvermerk einschraenken oder versagen.

### 3. Eigene Feststellung bei der Bilanzaufstellung

- **Eigenkapital negativ** (Aktiva kleiner als Passiva).
- **Wesentliche stille Lasten** im Status (z. B. Pensionsrückstellungen außerbilanziell).
- **Erhebliche außergewöhnliche Verluste** im laufenden Geschäftsjahr.

### 4. Liquiditätsengpass

- Mahnungen Gerichtsbeschlüsse oder Zahlungsverzug bei wesentlichen Gläubigern.
- Kreditlinie ausgeschoepft Kontoüberziehung.
- Lohn- und Gehaltszahlungen knapp.
- Steuer- und Sozialversicherungsabgaben nicht puenktlich.

### 5. Gesellschafterhinweis

- Brief oder E-Mail des Gesellschafters mit Sorge über Lage.
- Gesellschafterbeschluss zur Prüfung der Fortbestehensprognose.

### 6. Eigene Sorge des Geschäftsführers

- Subjektive Wahrnehmung dass die Lage kritisch wird.
- Wichtig: auch ohne externen Hinweis muss der Geschäftsführer aktiv prüfen — Sorgfaltspflicht § 43 GmbHG, § 93 AktG.

### 7. Externes Ereignis

- Wegfall Hauptkunde.
- Kreditlinien-Kündigung der Bank.
- Markteinbruch.
- Insolvenz eines wesentlichen Lieferanten / Abnehmers.

## Dokumentation

```yaml
fall-id: FP-2026-0001
stichtag-pruefung: 2026-05-20
ausloeser:
  typ: hinweis-steuerberater  # hinweis-steuerberater / hinweis-wp / eigene-feststellung-bilanz / liquiditätsengpass / gesellschafterhinweis / eigene-sorge / externes-ereignis
  datum: 2026-05-15
  hinweisgeber: Steuerberater Mueller, Kanzlei XYZ
  mitteilungsform: schriftlich  # schriftlich / muendlich / e-mail
  wortlaut: |
    "Nach Aufstellung des Jahresabschlusses 2025 ergibt sich ein negatives 
    Eigenkapital von 82.000 EUR. Wir weisen Sie nach § 102 StaRUG auf die 
    Pflicht zur Prüfung einer Fortbestehensprognose nach § 19 Abs. 2 InsO 
    hin."
  konkrete-anhaltspunkte:
    - Eigenkapital negativ 82.000 EUR Stichtag 31.12.2025
    - SuSa weist Lieferantenverbindlichkeiten 410.000 EUR (Vorjahr 180.000)
    - Sozialversicherungsbeitraege drei Monate offen 45.000 EUR
  reaktion-geschaeftsfuehrung:
    erste-reaktion-am: 2026-05-20
    schritte:
      - Beauftragung Erstellung Fortbestehensprognose
      - Aktivierung Plugin fortbestehensprognose
      - Termin mit Insolvenzanwalt vereinbart für 2026-05-27 als Sicherheit
```

## Pflichthinweis Frist

Mit Eintritt der **Insolvenzreife** (Zahlungsunfähigkeit § 17 oder Überschuldung § 19 InsO) beginnen die Antragsfristen des § 15a InsO. **Die Fortbestehensprognose ist nicht zu verwechseln mit dieser Frist** — sie ist die Prüfung **ob** Überschuldung trotz negativen Bilanzbildes verneint werden kann.

- Frist Zahlungsunfähigkeit: **drei Wochen** (§ 15a Abs. 1 S. 2 InsO).
- Frist Überschuldung: **sechs Wochen** (§ 15a Abs. 1 S. 2 InsO seit SanInsFoG 2021).

Im Zweifel **vor Ablauf der Frist** Insolvenzanwalt zu Rate ziehen.

## Ausgabe

- `ausloesendes-ereignis.yaml` mit allen Pflichtfeldern.
- Erste Risikobewertung (grün / gelb / rot).
- Empfehlung: bei rot direkt zu `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einschalten — diese Prüfung kann fortgesetzt werden aber nicht ohne anwaltliche Begleitung.
