---
name: handelsrecht-int-incoterms-auswahl-exw-fca-fob-cfr-cif-cpt
description: "INT Incoterms Auswahl EXW FCA FOB CFR CIF CPT: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INT Incoterms Auswahl EXW FCA FOB CFR CIF CPT

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **INT Incoterms Auswahl EXW FCA FOB CFR CIF CPT** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-018-incoterms-2020-auswahl` | Internationales Handelsrecht: Incoterms 2020 Klauselauswahl. Systematik der elf Klauseln (Gruppe E/F/C/D), Eignung für Containerverkehr vs. konventionellen Seehandel, FCA mit Konnossementsabrede und Auswahlkriterien für Exporte und Importe. |
| `ihl-019-exw-fca-fob-risiko` | Internationales Handelsrecht: Risikoübergang bei EXW, FCA und FOB nach Incoterms 2020. Gefahrübergang am Abgangsort, Pflichten des Verkäufers und Käufers, Exportkontrollproblem bei EXW und Containereignung von FCA vs. FOB. |
| `ihl-020-cfr-cif-cpt-cip` | Internationales Handelsrecht: CFR, CIF, CPT und CIP nach Incoterms 2020. C-Klauseln als Ankunftsklauseln für Kosten und Abgangsklauseln für Gefahr, Versicherungspflichten (CIF Klausel C vs. CIP Klausel A) und Transportdokumentenpflichten. |
| `ihl-026-konnossement-und-seefrachtbrief` | Internationales Handelsrecht: Konnossement (Bill of Lading) und Seefrachtbrief (Sea Waybill). Wertpapierfunktion, Traditionspapier-Eigenschaft, Typen (Order-BL, Bearer-BL, Straight-BL), Indossament und eKonnossement nach MLETR. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **INT Incoterms Auswahl EXW FCA FOB CFR CIF CPT**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-018-incoterms-2020-auswahl`

**Fokus:** Internationales Handelsrecht: Incoterms 2020 Klauselauswahl. Systematik der elf Klauseln (Gruppe E/F/C/D), Eignung für Containerverkehr vs. konventionellen Seehandel, FCA mit Konnossementsabrede und Auswahlkriterien für Exporte und Importe.

# Incoterms 2020: Klauselauswahl und Systematik

## Worum es geht

Incoterms 2020 (ICC-Publikation 2019, in Kraft 1. Januar 2020) regeln Risikoübergang, Kostentragung und Dokumentenpflichten im internationalen Warenkauf. Die elf Klauseln sind nach Transport-Universalität und Gefahrübergangszeitpunkt gegliedert. Neu in 2020: FCA mit Konnossementsabrede und höhere Versicherungsanforderungen bei CIP.

## Kernnormen / Kernquellen

- **Incoterms 2020 EXW**: Ex Works — Gefahrübergang ab Werk; minimal Verkäuferpflichten
- **Incoterms 2020 FCA**: Free Carrier — Gefahrübergang nach Übergabe an Frachtführer; neu: Konnossementsabrede
- **Incoterms 2020 CIF**: Cost Insurance Freight — nur für konventionelle Seefracht, nicht Container
- **Incoterms 2020 CIP**: Carriage and Insurance Paid — universell; neu: Institute Cargo Clauses (A)-Versicherung
- **Incoterms 2020 DDP**: Delivered Duty Paid — maximale Verkäuferpflichten
- **ICC-Publikation Nr. 2020**: Erläuterungen und Guidance Notes

## Schlüsselbegriffe

- Seeklauseln (FAS, FOB, CFR, CIF) vs. Universalklauseln (FCA, CPT, CIP, EXW, DAP, DPU, DDP)
- Gefahrübergang vs. Eigentumsübergang (Incoterms regeln nur Gefahr, nicht Eigentum)
- Named Place of Delivery: möglichst spezifischer Ort (Terminal, Lager)
- FCA-Konnossementsabrede: Verkäufer erhält On-Board-Konnossement nach Containerübergabe
- Versicherungspflicht: CIF (Institute Cargo Clauses C, Mindestdeckung) vs. CIP (Klausel A)

## Typische Streitfragen / Anwendungsfälle

1. FOB Container: Warum ist FOB für Containerware ungeeignet (Gefahrübergang am Kai — vor Verladung)?
2. FCA mit Konnossementsabrede: Wie funktioniert die Abrede mit der Reederei in der Praxis?
3. DDP und Mehrwertsteuer: Muss Verkäufer USt. im Importland bezahlen?
4. CIF vs. CIP: Wann welche Klausel bei See- vs. Multimodaltransport?
5. EXW und Exportkontrolle: Kann Verkäufer Exportformalitäten an Käufer delegieren?

## Methodik

- Klauselwahl nach Transportmodus: Container → FCA/CPT/CIP/DAP; Bulk-See → FOB/CFR/CIF
- Named Place immer spezifisch (Terminal-Name, nicht nur "Hamburg")
- Versicherungscheck: CIF Mindestdeckung (Klausel C) oft unzureichend
- EXW-Risiko für Verkäufer: Exportkontrolle liegt beim Käufer — Compliance-Lücke

## Output

- Incoterms 2020 Auswahlmatrix (11 Klauseln × Transportmodus × Risikoposition)
- FCA-Konnossementsabrede-Muster
- Checkliste Named Place

## Quellenregel

Incoterms 2020: iccwbo.org (Publikation Nr. 2020). ICC Guidance Notes 2020: iccwbo.org. Schrifttum: Ramberg, ICC Guide to Incoterms 2020 (2019). Unsicherheit bleibt sichtbar.

## 2. `ihl-019-exw-fca-fob-risiko`

**Fokus:** Internationales Handelsrecht: Risikoübergang bei EXW, FCA und FOB nach Incoterms 2020. Gefahrübergang am Abgangsort, Pflichten des Verkäufers und Käufers, Exportkontrollproblem bei EXW und Containereignung von FCA vs. FOB.

# EXW, FCA, FOB: Risikoübergang und Pflichten

## Worum es geht

EXW (Ex Works), FCA (Free Carrier) und FOB (Free on Board) sind Abgangsklauseln: der Gefahrübergang findet am Abgangsort statt. Bei EXW am Werk des Verkäufers, bei FCA nach Übergabe an Frachtführer, bei FOB nach Übergabe an Bord. FOB ist für Containerverkehr ungeeignet, da der Container im Terminal übergeben wird, bevor er "on board" geht.

## Kernnormen / Kernquellen

- **Incoterms 2020 EXW A2/B2**: Lieferpflicht — Abholung am Werk; Exportanmeldung Sache des Käufers
- **Incoterms 2020 FCA A2/B2**: Gefahrübergang nach Übergabe an benannten Frachtführer; A6 Konnossementsabrede
- **Incoterms 2020 FOB A2/B2**: Gefahrübergang nach Übergabe an Bord; nur für Seefracht
- **CISG Art. 67**: Gefahrübergang bei Beförderungsvertrag — ergänzt Incoterms
- **CISG Art. 69**: Gefahrübergang ohne Beförderungsvertrag (wie EXW)

## Schlüsselbegriffe

- EXW-Exportproblem: Käufer muss exportieren — bei EXW keine Exportkontroll-Compliance durch Verkäufer
- FCA-Terminal-Übergabe: Containerübergabe am CFS/CY ist "Übergabe an Frachtführer"
- FOB "on board": Gefahrübergang erst nach Verladen auf Schiff — für Container zu spät (Terminal-Verlust nicht gedeckt)
- Konnossementsabrede FCA: On-Board-BL kann für Akkreditivzwecke vereinbart werden
- Laderaumrisiko: wer trägt Mehrkosten bei Schiffscharterausfall?

## Typische Streitfragen / Anwendungsfälle

1. EXW Deutschland → China: Wer ist Exporteur i.S.d. EU-Exportkontrollrechts?
2. FCA Hamburg CFS: Wann genau geht Gefahr über — Übergabe ans Terminal oder Verladen?
3. FOB Shanghai: Ware beschädigt im Terminal vor Verladung — wer trägt Schaden?
4. FCA-Konnossementsabrede: Bank akzeptiert nur On-Board-BL — wie organisieren?
5. EXW mit Beladeassistenz durch Verkäufer: Ändert das den Gefahrübergang?

## Methodik

- Gefahrübergang nach Incoterms-Klausel bestimmen → mit CISG Art. 67-69 abgleichen
- Containerverkehr: FOB durch FCA ersetzen
- EXW: Exportkontrolle explizit im Vertrag regeln
- Konnossement-Abrede: immer in Sales-Contract und Letter of Credit abstimmen

## Output

- Risikomatrix: EXW / FCA / FOB — Gefahrübergang, Kostentragung, Dokumentenpflicht
- Klauselcheck: EXW vs. FCA für exportkontrollierte Güter
- FCA-Konnossementsabrede-Formulierung

## Quellenregel

Incoterms 2020: iccwbo.org. CISG Art. 67-69: uncitral.un.org. Schrifttum: Ramberg, ICC Guide to Incoterms 2020; Piltz, Internationales Kaufrecht § 5. Unsicherheit bleibt sichtbar.

## 3. `ihl-020-cfr-cif-cpt-cip`

**Fokus:** Internationales Handelsrecht: CFR, CIF, CPT und CIP nach Incoterms 2020. C-Klauseln als Ankunftsklauseln für Kosten und Abgangsklauseln für Gefahr, Versicherungspflichten (CIF Klausel C vs. CIP Klausel A) und Transportdokumentenpflichten.

# CFR, CIF, CPT, CIP: C-Klauseln

## Worum es geht

Die C-Klauseln (CFR, CIF, CPT, CIP) sind Hybrid-Klauseln: Gefahrübergang am Abgangsort (wie F-Klauseln), aber Kostentragung bis zum Bestimmungsort durch den Verkäufer. Incoterms 2020 hat CIP aufgewertet: Verkäufer muss jetzt mit Institute Cargo Clauses (A) versichern (All-Risk), während CIF bei der Mindestdeckung (Klausel C) bleibt.

## Kernnormen / Kernquellen

- **Incoterms 2020 CFR A3/B3**: Kosten bis Bestimmungshafen; Gefahr nach Verladung
- **Incoterms 2020 CIF A5**: Versicherungspflicht — ICC-Klausel C (Mindestdeckung); nur Seefracht
- **Incoterms 2020 CPT A3/B3**: Multimodal; Kosten bis benannten Ort; Gefahr nach Übergabe an Frachtführer
- **Incoterms 2020 CIP A5**: Versicherungspflicht — ICC-Klausel A (All Risk); Upgrade ggü. 2010
- **Institute Cargo Clauses (A), (B), (C)**: Lloyd's Market Association (LMA/IUA)
- **UCP 600 Art. 28**: Transportversicherungsdokument im Akkreditivrecht

## Schlüsselbegriffe

- Gefahrübergang bei C-Klauseln: am Abgangsort (nicht am Bestimmungsort — trotz Kostentragung)
- CIF vs. CIP: Seefracht (CIF) vs. multimodal (CIP); Versicherungsniveau unterschiedlich
- Institute Cargo Clauses A: umfassende Deckung inkl. Diebstahl, Beschädigung; B/C eingeschränkter
- Akkreditiv und CIF: UCP 600 Art. 28 — Mindestanforderungen Versicherungszeugnis
- Named Port of Destination: möglichst spezifisch (Terminal) für Kostenzwecke

## Typische Streitfragen / Anwendungsfälle

1. CIF: Ware beschädigt nach Verladung — Käufer trägt Gefahr, aber Verkäufer hat versichert — wer klagt Versicherer?
2. CIP 2020: Kann Käufer downgrade auf ICC Klausel C verlangen?
3. CFR vs. CIF im Akkreditiv: Was wenn Akkreditiv CIF fordert aber Vertrag CFR hat?
4. CPT multimodal: Wann genau geht Gefahr über bei Containerübergabe (FCA und CPT identisch)?
5. Akkreditiv: UCP 600 Art. 28 — Mindestversicherungswert (110% Fakturwert)?

## Methodik

- C-Klauseln: Gefahrübergang IMMER am Abgangsort, nicht am Bestimmungsort kommunizieren
- CIF vs. CIP Entscheidung: Transportmodus (See vs. multimodal) und Versicherungsbedarf
- Versicherungszeugnis für Akkreditiv: UCP 600 Art. 28 Anforderungen vor Vertragsabschluss abstimmen
- Named Destination: Terminal-Level-Spezifizierung für Frachtkostentransparenz

## Output

- C-Klausel Vergleichstabelle: Gefahrübergang / Kostentragung / Versicherung
- Versicherungszeugnis-Anforderungen nach UCP 600 Art. 28
- CIF vs. CIP Entscheidungsbaum

## Quellenregel

Incoterms 2020: iccwbo.org. Institute Cargo Clauses: lloyds.com (LMA). UCP 600: iccwbo.org. Schrifttum: Ramberg, ICC Guide to Incoterms 2020. Unsicherheit bleibt sichtbar.

## 4. `ihl-026-konnossement-und-seefrachtbrief`

**Fokus:** Internationales Handelsrecht: Konnossement (Bill of Lading) und Seefrachtbrief (Sea Waybill). Wertpapierfunktion, Traditionspapier-Eigenschaft, Typen (Order-BL, Bearer-BL, Straight-BL), Indossament und eKonnossement nach MLETR.

# Konnossement und Seefrachtbrief

## Worum es geht

Das Konnossement (Bill of Lading, B/L) ist das Kernwertpapier des Seehandels: es verbrieft den Beförderungsanspruch und ist Traditionspapier (Übergabe des Papiers = Übergabe der Ware). Der Seefrachtbrief (Sea Waybill) ist kein Wertpapier — er dient nur als Beweisdokument und schließt dokumentären Kredit mit Original-BL-Vorlage aus.

## Kernnormen / Kernquellen

- **HGB §§ 513-549**: Deutsches Konnossementrecht
- **HVR Art. 3 Abs. 3-7**: Mindestangaben und Wirkung des Konnossements
- **UCP 600 Art. 20**: Konnossement im Akkreditivrecht — Anforderungen (On-Board, Vollständigkeit)
- **CMI Rules for Electronic Bills of Lading 1990**: Erstes E-BL-Regelwerk
- **MLETR (UNCITRAL 2017)**: Model Law on Electronic Transferable Records
- **Bolero, essDOCS, WAVE**: Private E-BL-Plattformen

## Schlüsselbegriffe

- Order-BL vs. Straight-BL vs. Bearer-BL: Indossierbarkeit und Legitimation
- On-Board-Konnossement: Bestätigung tatsächlicher Verladung (nicht nur Empfang)
- Switch-BL: Austausch Konnossement im Transithafen — Risiken und Missbrauchspotenzial
- Claused BL: Vermerke über Verpackungsmängel → Akkreditiv-Komplikationen
- E-BL: Plattforminteroperabilität noch kein Standard (DCSA Initiative)

## Typische Streitfragen / Anwendungsfälle

1. Bank verlangt Clean On-Board-BL: Was bedeutet das und wie sicherstellen?
2. Straight-BL ohne Indossament: Wie kommt Käufer an Ware ohne Original-BL?
3. Akkreditiv friert bei Claused BL: Wie Lösung vor Verladung?
4. Switch-BL: Wer haftet bei Doppelausstellung (Fraud-Risiko)?
5. E-BL unter Bolero/essDOCS: Gilt MLETR national wenn Land nicht ratifiziert hat?

## Methodik

- BL-Typ nach Kreditrisiko wählen (Order-BL für Akkreditiv, Sea Waybill bei Konzerntransfer)
- UCP 600 Art. 20 Anforderungen vorab mit Bank abstimmen
- E-BL: nur wenn beide Parteien kompatible Plattform nutzen
- Switch-BL: immer nur Original-Set vernichten vor Neuausstellung

## Output

- Konnossementstypen-Übersicht (Funktion, Indossament, Risiko)
- UCP 600 Art. 20 Compliance-Checkliste
- E-BL-Plattformen-Übersicht

## Quellenregel

HGB §§ 513-549: gesetze-im-internet.de. HVR: uncitral.un.org. UCP 600: iccwbo.org. MLETR: uncitral.un.org. CMI Rules 1990: comitemaritime.org. Unsicherheit bleibt sichtbar.
