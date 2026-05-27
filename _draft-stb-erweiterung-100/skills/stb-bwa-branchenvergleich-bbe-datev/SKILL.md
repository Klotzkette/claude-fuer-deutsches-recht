---
name: stb-bwa-branchenvergleich-bbe-datev
description: "Branchenvergleich BWA auf Basis BBE-Datenbank ueber DATEV. Anwendungsfall Quartals- oder Jahres-BWA mit anonymisierten Branchen-Mittelwerten Median Top-Quartil. Methodik Branche identifizieren Vergleichsperiode waehlen Kennzahlenpruefung. Output BWA mit Branchenvergleichs-Spalte Erlaeuterung."
---

# Branchenvergleich BBE / DATEV in der BWA

## Kernsachverhalt

Die DATEV BBE-Datenbank (Betriebswirtschaftliche Beratung) liefert anonymisierte Vergleichsdaten von Mandanten gleicher Branche. Der Mandant kann sich so im Branchen-Mittelwert, Median und Top-Quartil verorten. Der Branchenvergleich ist starkes Beratungs-Instrument bei Quartals- und Jahresgespraechen, weil er den Mandanten nicht mit blanken Zahlen, sondern mit der Wettbewerbssituation konfrontiert. Voraussetzung: SKR 03 mit Standard-Konten, klare Branchen-Klassifikation (WZ-Code).

## Kaltstart-Rueckfragen

1. Welche Branche — WZ-Code 2008 (Statistisches Bundesamt) bzw. Branchenschluessel?
2. Welche Mandantengroesse (Umsatz, Mitarbeiterzahl)?
3. Welche Vergleichsbasis — Branchen-Median, -Mittelwert, Top-Quartil?
4. Welche Periode — Berichtsjahr abgeschlossen oder unterjaehrig vergleichend?
5. Welche Datentiefe — gesamte GuV oder einzelne Kennzahlen?
6. Welches BBE-Modul ist abonniert — Standard, erweitert?
7. Wie aktuell sind die Branchen-Daten (BBE liefert mit 1-2 Jahren Verzug)?
8. Welche Sondereffekte sind herauszurechnen (Saison, Einmaleffekte)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit (Datenqualitaet).

**§ 102 StaRUG** — Hinweispflicht; Branchenvergleich kann Krisensignal verstaerken oder relativieren.

**§ 4 BDSG / DSGVO** — Datenschutz; BBE-Daten sind anonymisiert.

### Standards

- DATEV BBE-Branchenbericht (Standard).
- BVR-Branchenanalysen (Volks- und Raiffeisenbanken).
- Sparkassen-Branchenbarometer.
- IDW PS 480.

## Workflow

### Phase 1 — Branchenklassifikation

- WZ-Code 2008 des Mandanten ermitteln (Statistisches Bundesamt).
- Beispiele: 56.10.1 Restaurants mit Bedienung, 47.11.1 Lebensmittel-Einzelhandel, 41.20.1 Bau von Wohngebaeuden.
- Im DATEV-Stammblatt erfassen — Voraussetzung fuer BBE-Auswertung.
- Bei Mischbetrieb: Hauptbranche festlegen.

### Phase 2 — BBE-Datenabruf

- DATEV Kanzlei-Rechnungswesen → BBE-Branchenbericht.
- Berichtsjahr und Vergleichsperiode auswaehlen.
- Datenstand pruefen (in der Regel 1-2 Jahre Verzug).
- Filter nach Mandantengroesse (Umsatz-Klassen).

### Phase 3 — Standard-Kennzahlen

| Kennzahl | Mandant | Branchen-Median | Top-Quartil |
|---|---|---|---|
| Materialquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Personalquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Umsatz je Mitarbeiter | [X] EUR | [Y] EUR | [Z] EUR |
| EBITDA-Marge | [X] Prozent | [Y] Prozent | [Z] Prozent |
| EBIT-Marge | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Eigenkapitalquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Anlagendeckung | [X] Prozent | [Y] Prozent | [Z] Prozent |

### Phase 4 — Verortung und Bewertung

- Mandant im Branchen-Quartil verorten (1. Quartil = bestes, 4. Quartil = schlechtestes Viertel).
- Auffaellige Abweichungen identifizieren (mehr als 20 Prozent vom Median).
- Plausibilitaet pruefen — extreme Abweichungen koennen auch auf Datenfehler hinweisen.

### Phase 5 — Beratungsansatz

- Bei unterdurchschnittlicher Materialquote: Einkaufsvorteil — staerken.
- Bei ueberdurchschnittlicher Personalquote: Produktivitaet pruefen, ggf. Personalentwicklung diskutieren.
- Bei niedriger EBITDA-Marge: Preisgestaltung, Sortimentsbereinigung pruefen.
- Bei niedriger Eigenkapitalquote: Bilanzpolitik (Thesaurierung), Finanzierungsstruktur.

### Phase 6 — Erlaeuterung im Quartalsgespraech

- Branchenvergleich Praesentation an Mandant.
- Stellen heraus: was ist Ueberdurchschnitt, was Unterdurchschnitt.
- Handlungsoptionen ableiten.
- Massnahmen-Plan zur naechsten Quartals-Pruefung.

## Output

- BWA mit Branchenvergleichs-Spalte oder Anhang.
- Verortungsbericht mit Top-Quartil-Vergleich.
- Massnahmen-Plan.

## Strategie und Praxis-Tipps

- BBE-Daten sind nicht ideal aktuell — bei schnellen Marktveraenderungen ggf. mit zusaetzlichen Quellen ergaenzen (Bundesverbaende, Bafa-Studien).
- Bei spezialisierten Branchen ist BBE manchmal duenn — alternative Datenbasis (Statistik der DStV, IfM-Bonn) pruefen.
- Mandant nicht ueberfordern — 3-5 Kennzahlen reichen, mehr verwirrt.
- Branchenvergleich nicht moralisieren — Mandant darf in einer Branche auch unterdurchschnittlich sein, wenn er bewusst Nische besetzt.
- StBVV: BBE-Bericht als Zusatzleistung, ueber Pauschal oder Zeithonorar.
- Datenschutz: BBE-Berichte enthalten anonymisierte Daten; nicht weitergeben an Dritte ohne Mandantenzustimmung.

## Querverweise

- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaetskennzahlen.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- DSGVO / BDSG.
- DATEV BBE-Branchenbericht.
- WZ 2008 Statistisches Bundesamt.
- IDW PS 480.
- Verifikations-Hinweis: BBE-Datenstand aktuell pruefen (1-2 Jahre Verzug ueblich).
