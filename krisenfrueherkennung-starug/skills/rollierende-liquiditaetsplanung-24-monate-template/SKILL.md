---
name: rollierende-liquiditaetsplanung-24-monate-template
description: "Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), Fortbestehensprognose, Sanierungskonzept. Prüfraster: Woechentliche Granularitaet Wochen 1-13, monatliche Granularitaet Monate 14-24, Stresstests, Sensitivitaetsanalysen, Maßnahmenbrücke, StaRUG-konforme Dokumentation. Output Excel-Template Liquiditaetsplanung, Stresstest-Szenarios, Dokumentationsprotokoll. Abgrenzung: Integrierte GuV/Bilanz/CF-Planung siehe integrierte-planung-guv-bilanz-cashflow; Ampel-KPIs siehe kennzahlenset-und-ampelsystem-starug-konform im Krisenfrueherkennung Starug."
---

# Rollierende Liquiditätsplanung — 24-Monate-Template

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StaRUG; § 1 StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Die rollierende Liquiditätsplanung ist das operative Herzstück des § 1 StaRUG-Frühwarnsystems. Sie zeigt nicht nur, wo das Unternehmen heute steht, sondern wo es in zwei Jahren stehen wird — und welche Handlungskorridore noch offen sind. Ohne eine valide 24-Monats-Liquiditätssicht ist die Behauptung, drohende Zahlungsunfähigkeit nicht rechtzeitig erkannt zu haben, im Nachhinein nicht zu entkräften.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht, 24-Monats-Horizont)
- § 18 InsO (drohende Zahlungsunfähigkeit — Prognosezeitraum)
- § 29 Abs. 2 StaRUG (Zugangsvoraussetzung: drohende ZU muss vorliegen)
- Berufsständische Methodenlogik zu Fortbestehensprognose und Sanierungskonzepten: Liquiditätsplanung ist nur ein Baustein; bei Sanierungsaussagen müssen GuV, Bilanz, Maßnahmen, Leitbild und Dokumentation hinzukommen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Pflichten

### 1. Warum zwei Granularitätsstufen?

Die Unterscheidung zwischen wöchentlicher (Wochen 1-13) und monatlicher (Monate 14-24) Granularität ist kein Zufall, sondern Ausdruck der Planungssicherheit:

- **Wochen 1-13 (kurzfristig):** Fälligkeiten, Überweisungen, Lohnzahlungen, Steuertermine sind konkret und kurzfristig planbar. Wöchentliche Granularität ist hier Standard und von Banken/Gläubigern erwartet.
- **Monate 14-24 (mittelfristig):** Annahmenbasierte Prognose. Monatsgenauigkeit ausreichend und methodisch vertretbar. Zeigt strukturelle Liquiditätsreserven und Refinanzierungsbedarfe.

### 2. Mindestinhalt der Planung

Der Liquiditätsplan muss enthalten:

**Zuflüsse:**
- Umsatzerlöse (nach Debitorenlaufzeiten)
- Anzahlungen, Vorauszahlungen
- Fremdfinanzierungen (Kredit-Ziehungen)
- Subventionen, Förderungen
- Sonstige betriebliche Erträge mit Zahlungswirkung

**Abflüsse:**
- Material-/Wareneinkauf (nach Kreditorenlaufzeiten)
- Lohn- und Gehaltskosten (inkl. Sozialabgaben)
- Miete, Leasing
- Zinsen und Tilgungen
- Investitionsauszahlungen
- Steuern und Abgaben (Umsatzsteuer-Vorauszahlung, Körperschaftsteuer, Gewerbesteuer)
- Sonstige Auszahlungen

**Saldo und Kassenbestand:**
- Wöchentlicher/monatlicher Cash-Flow (netto)
- Kumulierter Kassenbestand
- Verfügbare Kreditlinien
- Gesamtliquidität (Kassenbestand + freie Linien)

---

## Templates

### Muster: Excel-Spaltenstruktur (Auszug Wochen 1-4 + Monat 14)

```
Kategorie | KW01 | KW02 | KW03 | KW04 | ... | M14 | M15
--------------------------|-------|-------|-------|-------|-----|-------|------
ZUFLÜSSE | | | | | | |
 Umsatzerlöse (netto) | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
 Anzahlungen | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
 Kreditziehung | | | | | | |
= ZUFLÜSSE GESAMT | [Sum] | [Sum] | [Sum] | [Sum] | | [Sum] | [Sum]
 | | | | | | |
ABFLÜSSE | | | | | | |
 Material | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
 Personal | [tsd] | | | [tsd] | | [tsd] | [tsd]
 Miete / Leasing | [tsd] | | | | | [tsd] | [tsd]
 Zinsen | | | | | | [tsd] | [tsd]
 Tilgung | | | | | | [tsd] | [tsd]
 USt-Voranmeldung | [tsd] | | | | | [tsd] | [tsd]
 Sonstiges | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
= ABFLÜSSE GESAMT | [Sum] | [Sum] | [Sum] | [Sum] | | [Sum] | [Sum]
 | | | | | | |
NETTO-CASHFLOW | [Net] | [Net] | [Net] | [Net] | | [Net] | [Net]
KASSENBESTAND (Anfang) | [K] | [K] | [K] | [K] | | [K] | [K]
KASSENBESTAND (Ende) | [K] | [K] | [K] | [K] | | [K] | [K]
FREIE KREDITLINIE | [L] | [L] | [L] | [L] | | [L] | [L]
GESAMTLIQUIDITÄT | [G] | [G] | [G] | [G] | | [G] | [G]
```

### Muster: Planprämissen-Dokumentation

```
Planprämissen — 24-Monats-Liquiditätsplanung
Gesellschaft: [Firma GmbH]
Erstellt: [Datum]
Freigegeben: [GF-Name], [Datum]

UMSATZ
 Basis: [EUR Vorjahresumsatz]
 Annahme Base Case: [+/- x% p.a.]
 Annahme Bear Case: [+/- x% p.a.]
 Begründung: [___]

DEBITORENLAUFZEIT (DSO)
 Historisch (Ø letzte 12 Monate): [x] Tage
 Annahme Planung: [x] Tage
 Begründung: [___]

KREDITORENLAUFZEIT (DPO)
 Historisch: [x] Tage
 Annahme: [x] Tage

KREDITLINIEN
 Hausbankkredit: EUR [Betrag], läuft bis [Datum]
 Kontokorrentlinie: EUR [Betrag]
 Verlängerungsannahme: [ja/nein/in Verhandlung]

INVESTITIONEN
 Geplante Investitionen: EUR [Betrag] in [Zeitraum]
 Finanzierung: [Eigenmittel / Fremdfinanzierung]
```

---

## Fallstricke

1. **Plan ohne Planprämissen ist wertlos** — Richter und Insolvenzverwalter fragen als erstes: Auf welchen Annahmen beruht dieser Plan? Fehlende Prämissendokumentation ist ein Warnzeichen.

2. **Statischer Plan statt rollierender** — ein einmal erstellter 24-Monats-Plan, der nie aktualisiert wird, zeigt nicht den aktuellen Stand. Rollen bedeutet: monatliche Aktualisierung mit Ist-Werten und Neuvorschau.

3. **Nur Ergebnis-Plan ohne Cashflow** — viele Unternehmen haben GuV-Planungen, aber keinen Cashflow-Plan. Für § 1 StaRUG und § 18 InsO ist der Cashflow entscheidend, nicht das bilanzielle Ergebnis.

4. **Zu optimistische Planprämissen** sind keine "konservative Schätzung" — Gerichte prüfen ex post, ob die Annahmen zum Zeitpunkt der Planung plausibel waren. Überhöhte Umsatzerwartungen ohne Begründung sind Haftungsrisiko.

5. **Kreditlinie als Puffer einplanen, ohne Verlängerungsrisiko zu beachten** — ausgelaufene Kreditlinien, die stillschweigend als verlängert angenommen werden, verfälschen die Liquiditätssicht erheblich.

6. **Liquiditätsplan als Sanierungskonzept behandeln** — eine positive Liquiditätskurve belegt nicht automatisch nachhaltige Sanierungsfähigkeit. Ertragskraft, Bilanz, Krisenursachen, Leitbild und Maßnahmen müssen separat plausibilisiert werden.

---

## Weitere Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

