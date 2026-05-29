---
name: stb-bwa-branchenvergleich-bbe-datev
description: "Branchenvergleich BWA auf Basis BBE-Datenbank über DATEV. Anwendungsfall Quartals- oder Jahres-BWA mit anonymisierten Branchen-Mittelwerten Median Top-Quartil. Methodik Branche identifizieren Vergleichsperiode waehlen Kennzahlenprüfung. Output BWA mit Branchenvergleichs-Spalte Erlaeuterung."
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

- WZ-Code des Mandanten ermitteln (aktuelle Klassifikation der Wirtschaftszweige des Statistischen Bundesamtes; bisher WZ 2008, Aktualisierung pruefen).
- Beispiele typischer WZ-Codes: Restaurants mit Bedienung, Lebensmittel-Einzelhandel, Bau von Wohngebaeuden (konkrete Schluessel im Mandantenstamm gegen die aktuelle WZ-Fassung pruefen).
- Im DATEV-Stammblatt erfassen — Voraussetzung fuer BBE-Auswertung (Klickpfad: Mandantendaten → Allgemeines → Branchenschluessel).
- Bei Mischbetrieb: Hauptbranche festlegen und Nebenbranche dokumentieren.

### Phase 2 — BBE-Datenabruf

- DATEV-Klickpfad: Kanzlei-Rechnungswesen → Auswertungen → BBE-Branchenvergleich.
- Berichtsjahr und Vergleichsperiode auswaehlen.
- Datenstand pruefen — BBE-Daten weisen typischerweise einen Zeitverzug von ein bis zwei Jahren auf.
- Filter nach Mandantengroesse (Umsatzklasse) setzen, damit Vergleich zur Peer-Gruppe sauber ist.

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
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- DSGVO / BDSG.
- DATEV BBE-Branchenbericht.
- Klassifikation der Wirtschaftszweige (WZ 2008, Statistisches Bundesamt; aktuelle Fassung unter destatis.de abrufbar).
- IDW PS 480.
- Hinweis: BBE-Datenstand vor Mandanteneinsatz pruefen (Zeitverzug von ein bis zwei Jahren ueblich); Branchenrichtwerte aus aktuellem DATEV-BBE-Bericht oder Branchenverbands-Daten entnehmen.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (WZ 2008 Statistisches Bundesamt bestaetigt), 1 ersetzt (Hinweis ohne Marker neu formuliert) -->
