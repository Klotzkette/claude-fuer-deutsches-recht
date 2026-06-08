---
name: liquiditaet-12-monate
description: "Prüfungslinie für liquiditaet 12 monate: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Zwölf-Monats-Liquidität

## Arbeitsbereich

Prüfungslinie für liquiditaet 12 monate: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Die Fortbestehensprognose erfordert dass das Unternehmen über den **Prognosehorizont von zwölf Monaten** zahlungsfähig bleibt. Das bedeutet: in jedem Monat müssen die liquiden Mittel plus Kreditlinien plus Zufluesse die fälligen Verbindlichkeiten decken.

## Drei Schichten

### Schicht 1 — Monatliche Liquiditätsplanung

Aus den Annahmen aus `annahmen-sammeln-fortfuehrung` plus Plausibilisierung:

```yaml
liquiditaet:
 startbestand-2026-05-20: 18000
 kreditlinie-verfuegbar: 12000 # Linie 150000 minus 138000 ausgenutzt

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
 monatsendbestand: -71000 # negativ — Linie reicht nicht
 bemerkung: Liquiditätslücke
```

### Schicht 2 — Detaillierte Wochenplanung

Bei kritischen Phasen (Monaten mit knapp positivem Saldo oder negativem Endbestand) muss die Wochenplanung herangezogen werden:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **In jedem Zeitabschnitt** muss die Deckung der fälligen Verbindlichkeiten mindestens **90 Prozent** betragen (Liquiditätslücke unter zehn Prozent).
- **Eine vorübergehende Lücke** über zehn Prozent darf höchstens **drei Wochen** andauern. Wer laenger als drei Wochen unter 90 Prozent Deckung liegt ist nach BGH zahlungsunfähig — und das ist gerade nicht "fortfuehrbar".
- **Über den vollen Zwölf-Monats-Horizont** muss diese Schwelle eingehalten werden — andernfalls ist die Fortbestehensprognose **negativ**.

Die "mehr als 50 Prozent Wahrscheinlichkeit" der Prognose bezieht sich darauf dass dieses Szenario (Einhaltung der BGH-Schwelle über zwölf Monate) eintritt — also nicht ein abstrakter Erfolgswert sondern die methodische Wahrscheinlichkeit dass das Unternehmen die 90-Prozent-Deckung bzw. die Drei-Wochen-Karenz **über den gesamten Horizont durchhaelt**.

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

## Aktuelle Leitentscheidungen — 12-Monats-Liquiditaetsplanung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette 12-Monats-Liquiditaet

§ 17 InsO (Zahlungsunfaehigkeit, 10%-Schwelle) → § 19 Abs. 2 InsO (Fortbestehensprognose — Liquiditaet als Kernbestandteil) → IDW S 11 Rn. 50-65 (Liquiditaetsplanung als Prognosebaustein) → § 15a InsO (Antragspflicht bei negativem Forecast)

## Triage — 12-Monats-Forecast Check

1. **Methode?** Direkte Methode (Cash-In/Cash-Out) bevorzugt für insolvenzrechtliche Beurteilung.
2. **Periode?** Monatsgranularitaet Minimum; Wochen-Granularitaet wenn ZU-nahe.
3. **Annahmen konsistent?** Mit Umsatz- und Kostenplanung aus `annahmen-sammeln-fortfuehrung` abgestimmt?
4. **Engpaesse sichtbar?** Negative Saldi in einzelnen Monaten klar hervorgehoben und mit Gegenmassnahmen unterlegt?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
