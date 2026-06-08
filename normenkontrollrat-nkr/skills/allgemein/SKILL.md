---
name: allgemein
description: "Einstieg in das Normenkontrollrat-NKR-Plugin: Triage von Gesetzesvorhaben nach Erfüllungsaufwand, One-in-one-out, Digitalcheck, Befristung, Alternativenprüfung und Vollzugsfolgenabschätzung. Routet zum passenden Spezial-Skill und liefert bei Eile eine erste Stellungnahmen-Skizze für das Ressort."
---

# Normenkontrollrat-NKR — Einstieg und Routing

## Plugin-Fokus

Dieses Plugin unterstützt Ressorts, Verbände, Bundesländer und Wissenschaft bei Stellungnahmen und Berechnungen im Verfahren vor dem Nationalen Normenkontrollrat (NKR) nach NKRG. Es deckt die Prüfschritte ab, die der NKR bei jedem Regelungsvorhaben des Bundes anlegt: Bürokratiekosten, Erfüllungsaufwand, Digitaltauglichkeit, Verständlichkeit, Alternativenprüfung und Evaluierungsfähigkeit.

## Sofortfragen für die Triage

1. **Verfahrensstand:** Referentenentwurf, Ressortabstimmung, Kabinettvorlage, BR-Drucksache, BT-Drucksache, Plenum?
2. **Art des Vorhabens:** Gesetz, Rechtsverordnung, Änderung bestehender Regelung, Aufhebung, EU-Umsetzung?
3. **Erfüllungsaufwand:** Bereits geschätzt? Adressaten (Bürger, Wirtschaft, Verwaltung)? Einmalig vs. jährlich wiederkehrend?
4. **Digitalcheck:** Schon durchlaufen? Wer war beteiligt (Ressort, BMI, OZG)?
5. **Befristung / Evaluierungsklausel:** Vorgesehen? Wenn nicht: Begründung?
6. **Alternativen:** Wurden Verzicht, Soft-Law, Vollzugsverbesserung geprüft?

## Routing zu den Spezial-Skills

| Frage | Spezial-Skill |
| --- | --- |
| Aufgaben und Befugnisse des NKR selbst | `aufgabe-und-kompetenz-nkrg` |
| Erfüllungsaufwand quantifizieren | `buerokratiekosten-vs-erfuellungsaufwand` |
| One-in-one-out-Pflicht | `one-in-one-out`-/`buerokratieabbau`-Skills |
| Digitalcheck und OZG-Tauglichkeit | `digitalcheck-und-onlinezugangsgesetz-ozg` |
| Praxistauglichkeitsprüfung | `praxistauglichkeit-vorab-test` |
| Befristung und Evaluierung | `befristung-und-evaluierungsklausel` |
| Alternativenprüfung mit Hierarchie | `alternativen-keine-aufgabe-kompetenz` / `alternativen-keine-regelung-soft-law` |
| KMU-Test | `kmu-test` |
| Erforderlichkeit der Regelung | `einmalig-vs-erforderlichkeitspruefung-warum` |

## Arbeitsweg

1. **Vorhaben einordnen.** Verfahrensstand, betroffene Adressaten, Eile-Grad.
2. **Pflichten ableiten.** Welche der NKR-Prüfungen sind nach NKRG und GGO zwingend? Welche sind nur empfohlen?
3. **Datenlage prüfen.** Liegen Mengengerüste, Verwaltungserfahrungen, Vergleichsdaten vor? Wenn nicht: Beschaffung markieren.
4. **Tragenden Spezial-Skill auswählen** und dort die Detail-Routine vollständig abarbeiten.
5. **Mehrere Spezial-Skills nur kombinieren,** wenn das Vorhaben tatsächlich mehrere NKR-Prüfdimensionen berührt.
6. **Output formulieren.** Stellungnahme an den NKR, Memo ans Ressort, Fragenkatalog an die Verbände, oder Berechnungs-Datenblatt.

## Quellenhygiene

- NKRG, GGO, Handbuch der Rechtsförmlichkeit (HdR), Leitfaden zur Ermittlung des Erfüllungsaufwands — live über `bmi.bund.de`, `normenkontrollrat.bund.de` und `bundesregierung.de` prüfen.
- Stellungnahmen des NKR (Jahresberichte, Einzel-Stellungnahmen) als Auslegungsmaßstab.
- Keine NKR-Az aus Modellwissen — Vorgangsnummer immer aus der konkreten BT-/BR-Drucksache verifizieren.

## Output

Triage-Notiz mit empfohlenem Spezial-Skill, Frist (Ressortabstimmung, NKR-Befassung), Datenlücken und konkret nächstem Arbeitsschritt.
