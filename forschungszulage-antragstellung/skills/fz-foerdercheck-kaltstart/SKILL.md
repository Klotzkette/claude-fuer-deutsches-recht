---
name: fz-foerdercheck-kaltstart
description: "Schneller Fördercheck Forschungszulage in zehn Minuten: Anspruchsberechtigung, FuE-Kategorie nach Frascati, KMU-Status, Personalkosten-Schwelle, Projektjahre, Kostenarten, BSFZ-/Finanzamt-Status, Kumulierung, Ausschlussrisiken und realistische Sofortpotenzialschätzung. Liefert Ampelschema und Empfehlung Antrag jetzt oder Quartal warten."
---

# Fördercheck Kaltstart

## Worum geht es

Vor jedem FZulG-Antrag steht eine Wirtschaftlichkeitsfrage: lohnt der Aufwand für BSFZ-Antrag, Stundenerfassung, Personalkostenrechnung und Finanzamt-Antrag? Dieser Skill liefert nach maximal zehn Minuten eine belastbare Erstaussage als Ampel und benennt den nächsten Arbeitsblock.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

Sie nutzen `fz-foerdercheck-kaltstart`:

- Erstkontakt mit einem potenziellen Antragsteller.
- Sanity-Check vor BSFZ-Investition.
- Re-Assessment, wenn Vorjahr abgelehnt wurde.
- Vor Mandatszusage, um Honorarmodell und Erwartung zu kalibrieren.

## 7-Fragen-Diagnose

1. **FuE nach Frascati?** Neuheit, Schöpferisch, Ungewisses Ergebnis, Systematisch, Übertragbar/Reproduzierbar. Mindestens drei der fünf Kriterien tragend?
2. **Personaleinsatz** für FuE-Vorhaben: wie viele Mitarbeiter, welche Anteile, welche Bruttogehälter?
3. **Auftragsforschung** mit Externen? In EU/EWR? Vertrag oder nur Bestellung?
4. **KMU-Status** nach EU-Definition (Mitarbeiterzahl, Umsatz, Bilanzsumme — vom Antragsteller mit Empfehlung 2003/361/EG zu prüfen)?
5. **Jahresumsatz** und steuerliche Situation: Gewinn, Verlust, Holding-Struktur?
6. **Verlustsituation** aktuell und für die nächsten zwei Jahre?
7. **Antragshistorie:** schon einmal BSFZ-Antrag gestellt, Bescheinigung erhalten, Finanzamt-Antrag gestellt?

## Praxisleitfaden

### Faustregel Wirtschaftlichkeit

- FuE-Personalkosten unter 100k Euro/Jahr: Aufwand selten wirtschaftlich, prüfen ob Sammelantrag mit anderen Vorhaben sinnvoll.
- 100k bis 500k Euro/Jahr: regulärer Antrag, BSFZ-Antrag und Stundenerfassung lohnen.
- Über 500k Euro/Jahr: Mehrjahresstrategie, Roadmap aufsetzen (`fz-roadmap-mehrjahresantrag`).

### BSFZ-Trigger als rote Flaggen im Vorhaben

Wenn der Mandant nur folgendes liefert, ist das Vorhaben aus BSFZ-Sicht nicht förderfähig:

- "Innovative Plattform" ohne klare technische Aufgabe.
- "KI-basiert" ohne konkretes ML-Modell, Trainingsproblem, Datengrundlage.
- "Industrie 4.0" als Schlagwort, ohne neuartiges Steuerungs-/Sensorproblem.
- "ERP-Anpassung" oder "Customizing" einer bekannten Software.
- Lastenheft mit Anforderungsliste statt Beschreibung des technischen Problems.

### Schnelltests für die Ampel

- **Grün:** echtes technisches Problem, dokumentiertes Risiko, eigener Personaleinsatz, Stundenerfassung machbar, kein AGVO-Konflikt.
- **Gelb:** FuE plausibel, aber Belege fehlen; Auftragsforschungsanteil hoch; KMU-Status unklar; alte Wirtschaftsjahre offen.
- **Rot:** reines Customizing, Routine, Auftragsforschung außerhalb EU/EWR, alle Förderquellen schon ausgeschöpft.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Jetzt Antrag vs. Quartal warten | sofort BSFZ stellen | warten auf neues Personal/Klarheit | sofort, wenn Vorhaben technisch klar |
| Ein Vorhaben vs. Bündel | nur das stärkste Projekt | mehrere Projekte in einem Antrag | Bündel, wenn technisch zusammenhängend |
| Eigen- vs. Auftragsforschung | nur Eigen (BMG 100 Prozent) | Auftrag (BMG 70 Prozent) | Mix bewusst kalkulieren |
| Antrag selbst vs. Berater | Inhouse | Spezialberater | Berater bei Erstantrag und über 500k Euro BMG |

## Schritt für Schritt

1. 7-Fragen-Diagnose mit Mandanten in 15 Minuten durchgehen.
2. FuE-Personalkosten grob schätzen (Köpfe × Bruttogehalt × FuE-Anteil).
3. Bemessungsgrundlage abschätzen: Eigenpersonal + 70 Prozent Auftrag + Eigenleistung + 20 Prozent Pauschale.
4. Fördersumme schätzen: BMG × 25 Prozent (KMU eventuell 35 Prozent — Voraussetzungen prüfen).
5. Engpass benennen: BSFZ-Text, Stundenerfassung, Auftragsforschung, AGVO-Kumulierung.
6. Ampel setzen. Bei Grün direkt zu `fz-bsfz-bescheinigung-projektbeschreibung`. Bei Gelb zu `fz-fue-definition-frascati-abgrenzung`. Bei Rot Mandanten ehrlich beraten.

## Mustertexte

**Kurzbild-Email an Mandant (Vorlage):**

"Sehr geehrte/r [Name], auf Basis Ihrer Angaben ([Vorhaben], [FuE-Personalkosten ca. X Euro/Jahr], [BSFZ-Antrag noch nicht gestellt]) sehen wir die Forschungszulage als [grün/gelb/rot]. Die geschätzte Förderung liegt bei [Y Euro/Jahr] über [Z Jahre]. Nächster Schritt ist [BSFZ-Projektbeschreibung / Stundenerfassung / Klärung KMU-Status]. Fristkritisch ist [Wirtschaftsjahr/Festsetzungsfrist]."

**Ampel-Tabelle für Memo:**

| Kriterium | Status | Begründung |
| --- | --- | --- |
| FuE-Eigenschaft | grün/gelb/rot | konkretes technisches Problem? |
| Personalkosten | grün/gelb/rot | über/unter 100k Euro? |
| KMU | grün/gelb/rot | unter/über 250 Mitarbeiter, 50 Mio. Euro Umsatz? |
| Kumulierung | grün/gelb/rot | andere Förderungen? AGVO-Reserve? |
| Dokumentation | grün/gelb/rot | Stundenerfassung vorhanden? |

## Typische Fehler

- Mandant beschreibt nur das Produkt und nicht das technische Problem.
- Auftragsforschungsanteil wird übersehen — 70-Prozent-Kürzung kostet Förderung.
- Eigenleistung des Geschäftsführers nicht berücksichtigt.
- BMG wird nur grob geschätzt, ohne Personalkostenformel.
- Kumulierung mit ZIM/BMBF wird vergessen, später AGVO-Konflikt.
- KMU-Status pauschal angenommen, ohne Schwellenprüfung über die EU-Definition.
- Antragshistorie nicht abgefragt — Vorablehnungen vergiften die Folgeanträge.
- Rückwirkende Jahre vergessen, obwohl Belege noch greifbar wären.

## Praxis-Trick — die fünf Fragen für die Eingangs-Email

Wenn ein Interessent meldet "wir wollen Forschungszulage", reichen diese fünf Fragen für eine Erstantwort innerhalb einer halben Stunde:

1. "Welches konkrete technische Problem wollen Sie lösen, das mit bekannten Verfahren nicht lösbar ist?"
2. "Wie viele Mitarbeiter arbeiten daran, und welcher Bruttoaufwand pro Jahr entsteht für diese FuE-Tätigkeit?"
3. "Haben Sie für dieses Vorhaben bereits andere Förderungen erhalten oder beantragt (ZIM, BMBF, Land, EU, Bayern Innovativ etc.)?"
4. "Sind Sie KMU im Sinne der EU-Definition (Mitarbeiter, Umsatz, Bilanzsumme)?"
5. "Welche Wirtschaftsjahre sind betroffen, und wie steht es um die Stundenaufzeichnung Ihrer FuE-Mitarbeiter?"

Die Antworten geben in Verbindung mit der 7-Fragen-Diagnose oben ein belastbares Bild.

## Output

- Ampelschema mit Begründung je Kriterium.
- Förderchance in Euro (Bandbreite konservativ/realistisch/optimistisch).
- Engpass-Liste mit dem nächsten Spezialskill.
- Liste der sofort zu sichernden Belege.

## Querverweise

- `fz-fue-definition-frascati-abgrenzung` für die FuE-Tiefenprüfung.
- `fz-bemessungsgrundlage-2026` für die belastbare Förderhöhenrechnung.
- `fz-bsfz-bescheinigung-projektbeschreibung` wenn die Ampel grün ist.
- `fz-kumulierung-beihilfen-agvo` bei Mehrfachförderung.

## Quellen Stand 05/2026

- FZulG: https://www.gesetze-im-internet.de/fzulg/
- BSFZ Antragsverfahren: https://www.bescheinigung-forschungszulage.de/antragsverfahren/ueber-das-antragsverfahren
- KMU-Definition Empfehlung 2003/361/EG (vom Antragsteller live zu prüfen)
- `references/forschungszulage-quellen-und-zahlen.md`
