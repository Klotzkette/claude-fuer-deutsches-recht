---
name: liquiditaet-12-monate
description: Erstellt die rollierende Zwoelf-Monats-Liquiditaetsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib. Pruefung ob in jedem Zeitabschnitt mehr als die geschuldeten Verbindlichkeiten zur Verfuegung stehen. Bezuege zur Zahlungsfaehigkeit nach § 17 InsO (Zehn-Prozent-Schwelle Drei-Wochen-Frist nach BGH IX ZR 123/04). Falls Plugin liquiditaetsplanung installiert — dort die detaillierte Wochenplanung; dieses Plugin uebernimmt die Monatsaggregate.
---

# Zwölf-Monats-Liquidität

## Zweck

Die Fortbestehensprognose erfordert dass das Unternehmen über den **Prognosehorizont von zwölf Monaten** zahlungsfähig bleibt. Das bedeutet: in jedem Monat müssen die liquiden Mittel plus Kreditlinien plus Zufluesse die fälligen Verbindlichkeiten decken.

## Drei Schichten

### Schicht 1 — Monatliche Liquiditätsplanung

Aus den Annahmen aus `annahmen-sammeln-fortfuehrung` plus Plausibilisierung:

```yaml
liquiditaet:
  startbestand-2026-05-20: 18000
  kreditlinie-verfuegbar: 12000  # Linie 150000 minus 138000 ausgenutzt
  
  monatsdaten:
    - monat: 2026-06
      einzahlungen:
        forderungen-laul: 185000
        gesellschafter-darlehen: 0
        sonstige: 0
        summe: 185000
      auszahlungen:
        lieferanten: 130000
        loehne-gehaelter: 78000
        sozialabgaben: 24000
        steuern: 14000
        bank-tilgung: 8000
        miete: 6000
        energie: 9000
        sonstige: 5000
        summe: 274000
      saldo-monat: -89000
      monatsendbestand: -71000  # negativ — Linie reicht nicht
      bemerkung: Liquiditätslücke
```

### Schicht 2 — Detaillierte Wochenplanung

Bei kritischen Phasen (Monaten mit knapp positivem Saldo oder negativem Endbestand) muss die Wochenplanung herangezogen werden:

- Drei-Wochen-Schwelle § 17 InsO BGHZ 163, 134 — bei Lücke größer als zehn Prozent über laenger als drei Wochen liegt Zahlungsunfähigkeit vor.
- Plugin `liquiditaetsplanung` enthält die wochenbasierten Vorlagen.

### Schicht 3 — Sensitivitätsszenarien

Drei Szenarien aus `annahmen-belastbarkeit-plausibilisieren` werden in der Liquidität durchgerechnet:

- **Basis-Szenario** — Plan
- **Negativ-Szenario** — ambitionierte Annahmen reduziert
- **Stress-Szenario** — Top-Kunde weg

Bei jedem Szenario die monatlichen Salden über die zwölf Monate.

## Prüfkriterien

### Pro Monat

- **Monatsendbestand mindestens null** (besser kein voll ausgenutzter Kontokorrent).
- **Keine roten Monate** im Plan.

### Über den Horizont

- **Steigender Trend** oder Stabilisierung der Liquidität.
- **Wesentliche Risikoposten** identifiziert.
- **Maßnahmenoptionen** bei Risiko-Eintritt vorhanden.

### Bei Sensitivitaet

- **Negativ-Szenario** Liquidität auch positiv? Wenn nein: dann ist die Prognose **nur** im Basis-Szenario tragfähig. Das ist **nicht** ausreichend für eine positive Fortbestehensprognose.
- **Stress-Szenario** soll mit den Maßnahmen abgefedert werden können — gegebenenfalls Patronatserklärungen Comfortletter Gesellschafterdarlehen.

## Konsolidierung mit dem Plugin `liquiditaetsplanung`

Wenn das Plugin `liquiditaetsplanung` installiert ist:

- Die detaillierte Wochenplanung erfolgt dort (Skill `liquiditaetsvorschau-3-6-12-monate`).
- Hier importieren wir die Monatsaggregate.
- Die Drei-Wochen-Schwelle § 17 InsO wird in `liquiditaetsplanung` separat geprüft.

Wenn nicht installiert: einfache Tabelle hier; bei Bedarf nachinstallieren.

## Beispielergebnis

```
Liquiditätsprüfung Zwölf Monate
Basis-Szenario: positiv (Endbestand jeweils über null)
Negativ-Szenario: kritisch (Monat 11 unter null)
Stress-Szenario: negativ ab Monat 4

Bewertung: ohne Sanierungsmaßnahmen ist die Liquidität im Stress-Szenario
überschritten. Mit Maßnahmen aus Skill sanierungsbausteine-vorschlagen
ist die Liquidität über den Horizont zu sichern.
```

## 90-Prozent-Deckung ist der operative Maßstab

Die „überwiegende Wahrscheinlichkeit" nach § 19 Abs. 2 InsO ist nicht abstrakt zu prüfen, sondern operativ über den Liquiditätsplan. Das Unternehmen ist „überwiegend wahrscheinlich fortfuehrbar" wenn über den gesamten Zwölf-Monats-Horizont mit hoher Wahrscheinlichkeit **keine Zahlungsunfähigkeit nach § 17 InsO eintritt**. Damit gilt durchgehend der BGH-Maßstab aus BGHZ 163, 134 (BGH IX ZR 123/04):

- **In jedem Zeitabschnitt** muss die Deckung der fälligen Verbindlichkeiten mindestens **90 Prozent** betragen (Liquiditätslücke unter zehn Prozent).
- **Eine vorübergehende Lücke** über zehn Prozent darf höchstens **drei Wochen** andauern. Wer laenger als drei Wochen unter 90 Prozent Deckung liegt ist nach BGH zahlungsunfähig — und das ist gerade nicht „fortfuehrbar".
- **Über den vollen Zwölf-Monats-Horizont** muss diese Schwelle eingehalten werden — andernfalls ist die Fortbestehensprognose **negativ**.

Die „mehr als 50 Prozent Wahrscheinlichkeit" der Prognose bezieht sich darauf dass dieses Szenario (Einhaltung der BGH-Schwelle über zwölf Monate) eintritt — also nicht ein abstrakter Erfolgswert sondern die methodische Wahrscheinlichkeit dass das Unternehmen die 90-Prozent-Deckung bzw. die Drei-Wochen-Karenz **über den gesamten Horizont durchhaelt**.

**Konsequenz für die Liquiditätsprognose:**

- Pro Monat (besser pro Woche in kritischen Phasen): Liquiditätsbestand plus Linie / fällige Verbindlichkeiten = Deckungsquote.
- Deckungsquote in jedem Zeitabschnitt mindestens **90 Prozent**.
- Bei Unterschreitung max. drei Wochen — danach muss die Quote zwingend über 90 Prozent zurückkehren.
- Im Negativ- und Stress-Szenario diese Prüfung **wiederholen**. Wenn auch das Negativ-Szenario die Schwelle einhaelt: starke Prognose. Wenn nur das Basis-Szenario einhaelt aber das Negativ-Szenario reisst: knappe Prognose — nur mit zusätzlichen verbindlichen Maßnahmen positiv.

## Ausgabe

- `liquiditaet-12-monate.xlsx` mit monatlichen Werten je Szenario.
- `liquiditaet-monatssalden.md` als menschenlesbare Übersicht.
- Hinweis auf Prüfer-Flag bei roten Monaten.
- Empfehlung auf nächsten Skill `fortbestehensprognose-zusammenfuehren`.
