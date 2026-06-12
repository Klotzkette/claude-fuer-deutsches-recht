---
name: lohn-jobticket-mobilitaet
description: "Jobticket Deutschlandticket steuerliche Behandlung. Anwendungsfall AG erstattet AN Mobilitaetsticket OePNV oder bietet Jobticket steuerfrei nach § 3 Nr 15 EStG Auswirkung auf Entfernungspauschale. Methodik Prüfung Konfiguration. Output Lohn-Abrechnung mit Jobticket."
---

# Jobticket und Deutschlandticket — Steuerliche Behandlung

## Fachlicher Anker

- **Normen:** § 6a, § 3 Nr. 15 EStG, § 40 Abs. 2 EStG.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Der AG kann AN ein Jobticket für OePNV steuerfrei zur Verfuegung stellen, wenn dieses zusaetzlich zum geschuldeten Arbeitslohn gewaehrt wird (§ 3 Nr. 15 EStG). Seit 2023 ist das Deutschlandticket (49 EUR/Monat ab 01.05.2023, ab 01.01.2025 58 EUR; Preis wird politisch jaehrlich festgelegt — aktuellen Wert über Verkehrsministerkonferenz prüfen) ebenso behandelbar. Bei voller AG-Finanzierung ist das Ticket steuer- und SV-frei. Bei AN-Eigenanteil wird der AG-Zuschuss steuerfrei behandelt. Die Entfernungspauschale wird beim AN um die steuerfreien AG-Leistungen gekuerzt.

## Kaltstart-Rueckfragen

1. Welches Ticket — Jobticket, Deutschlandticket, anderes OePNV-Ticket?
2. Wer zahlt — AG voll, AG-Zuschuss + AN-Eigenanteil?
3. Wird zusaetzlich zum Lohn gewaehrt oder durch Gehaltsumwandlung?
4. Welche Entfernung Wohnung-Arbeit hat der AN (Auswirkung auf Entfernungspauschale)?
5. Liegt nur OePNV-Nutzung vor, oder auch privat?
6. Pauschalierung § 40 Abs. 2 EStG 25 Prozent gewuenscht (AG-finanzierte Sachzuwendung)?
7. Welche Versorger (DB, Verkehrsverbund, Deutschlandticket-Vertrieb)?
8. Anwendung im DATEV LODAS bereits konfiguriert?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 15 EStG** — Steuerfreiheit Jobticket für OePNV.

**§ 9 Abs. 1 Nr. 4 EStG** — Entfernungspauschale.

**§ 40 Abs. 2 Satz 2 EStG** — Pauschalbesteuerung 25 Prozent.

**§ 8 Abs. 2 EStG** — Sachbezug.

### Verwaltungsanweisungen

- BMF v. 15.08.2019 zu Jobticket.
- BMF zu Deutschlandticket 2023/2024.
- LStR R 3.15.

## Workflow

### Phase 1 — Voraussetzungen Steuerfreiheit § 3 Nr. 15 EStG

- Sachbezug für Fahrten Wohnung-Arbeit oder im OePNV.
- "Zusaetzlich zum ohnehin geschuldeten Arbeitslohn" (kein Gehaltsumwandlung).
- Ticket ist auch privat nutzbar (z.B. Deutschlandticket).

### Phase 2 — Steuerfreiheit oder Pauschalierung

| Variante | Lohnsteuer | SV |
|---|---|---|
| AG-finanziertes Jobticket zusaetzlich zum Lohn | Steuerfrei (§ 3 Nr. 15 EStG) | SV-frei |
| Jobticket durch Gehaltsumwandlung (kein "zusaetzlich") | Steuerpflichtig | SV-pflichtig (alternativ Pauschal § 40 Abs. 2) |
| Pauschal versteuert 25 Prozent (§ 40 Abs. 2) | Pauschal 25 Prozent | Pauschal beitragsfrei |

### Phase 3 — Entfernungspauschale-Kuerzung

- Steuerfreier AG-Zuschuss zum Jobticket wird beim AN von der Entfernungspauschale abgezogen.
- AN-Werbungskostenabzug entsprechend gemindert.
- Bei Pauschalierung § 40 Abs. 2 EStG: keine Kuerzung.

### Phase 4 — Deutschlandticket-Sondersituation

- 01.05.2023: Einfuehrung Deutschlandticket 49 EUR/Monat.
- Ab 01.01.2025: 58 EUR/Monat; Preis wird politisch jaehrlich festgelegt — aktuellen Wert über Verkehrsministerkonferenz (VMK) prüfen.
- Behandlung wie Jobticket nach § 3 Nr. 15 EStG.
- Bei AG-Zuschuss zum Deutschlandticket des AN: steuerfrei, wenn über Job-Karte erworben.
- **Zahlenbeispiel:** AG zahlt für AN das Deutschlandticket voll (58 EUR/Monat Stand 2025; Preis prüfen), zusaetzlich zum Lohn → 696 EUR/Jahr LSt- und SV-frei nach § 3 Nr. 15 EStG; allerdings beim AN Kuerzung der Entfernungspauschale (§ 9 Abs. 1 Nr. 4 Satz 6 EStG) — der AN gibt in der Anlage N die AG-Leistung an, das FA mindert den Werbungskostenabzug. Alternative Pauschalierung 25 Prozent (§ 40 Abs. 2 Satz 2 EStG): keine Kuerzung der Entfernungspauschale.

### Phase 5 — Lohnabrechnung

- DATEV LODAS: Lohnart "Jobticket steuerfrei".
- Buchung im Hauptbuch (Lohnnebenkosten).
- AN-LSt-Bescheinigung mit Jobticket-Vermerk Zeile 17.

### Phase 6 — Dokumentation

- Bestellnachweis Ticket.
- AG-Erstattungsbeleg.
- Vertrag mit Verkehrsverbund.

## Strategie und Praxis-Tipps

- Deutschlandticket ist guenstig für AG — minimale Buchung, hohe AN-Bindung.
- "Zusaetzlich zum Lohn" streng prüfen — bei Gehaltsumwandlung kein § 3 Nr. 15.
- Bei Pauschalierung 25 Prozent: keine Entfernungspauschalen-Kuerzung beim AN; attraktiv.
- Bei vollstaendiger AG-Erstattung: AN profitiert über Werbungskosten-Differenz.
- StBVV: in Lohnpauschale; Konfiguration einmalig.
- DATEV-Tipp: DATEV LODAS Jobticket-Konfiguration mit eigenem Lohnart.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 15, 8, 9 Abs. 1 Nr. 4, 40 Abs. 2.
- BMF v. 15.08.2019 (Jobticket).
- LStR R 3.15.
- Deutschlandticket-Preis: 58 EUR/Monat ab 01.01.2025 (jaehrlich durch VMK festgelegt; prüfen).

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 2 bestaetigt (Deutschlandticket 58 EUR ab 01.01.2025), 2 ersetzt (Prüfhinweise ohne Marker) -->
