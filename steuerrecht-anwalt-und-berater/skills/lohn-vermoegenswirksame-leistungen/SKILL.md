---
name: lohn-vermoegenswirksame-leistungen
description: "Vermögenswirksame Leistungen VL AG-Anteil AN-Sparzulage. Anwendungsfall AG-Zuschuss bis 480 EUR jaehrlich AN-Sparzulage einkommensabhaengig Bausparen Aktien-Fonds. Methodik Prüfung Antrag AN-Sparzulage Beratung. Output VL-Konfiguration."
---

# Vermoegenswirksame Leistungen (VL) und AN-Sparzulage

## Fachlicher Anker

- **Normen:** § 6a, § 13, §§ 13.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Vermoegenswirksame Leistungen (VL) sind Sparleistungen, die der AG für den AN auf ein VL-faehiges Sparkonto einzahlt. Hoehe und Vertragsgestaltung sind tariflich oder einzelvertraglich vereinbart. Bei Einkommens-Schwellenwerten kommt die AN-Sparzulage als staatliche Förderung hinzu (5. VermBG). Die VL sind lohnsteuerpflichtig und SV-pflichtig — keine steuerliche Förderung der AG-Leistung selbst.

## Kaltstart-Rueckfragen

1. Liegt VL-Vereinbarung im Arbeitsvertrag oder Tarifvertrag vor?
2. Welche Hoehe — AG-Zuschuss pro Monat (typisch 6,65 oder 40 EUR)?
3. Welche VL-Sparform — Bausparen, Aktien-Fonds, Banksparen?
4. Welches Einkommen hat der AN (Sparzulage-Grenze)?
5. Hat der AN bereits VL-Antrag bei Anlage-Institut gestellt?
6. Bei verheirateten AN: Familienverhaeltnisse für Sparzulage-Grenze?
7. Anzahl VL-Vertraege (max. 1 für Sparzulage)?
8. Welche Dauer (Sperrfrist 7 Jahre Standard)?

## Rechtlicher Rahmen

### Primaernormen

**5. VermBG** — 5. Vermoegensbildungsgesetz.

**§ 13 5. VermBG** — AN-Sparzulage (Anspruchsgrundlage; Saetze und Einkommensgrenzen in §§ 13, 14 5. VermBG; bei Gesetzesaenderung Norm-Bestand pruefen).

**§ 19 EStG** — VL als Arbeitslohn (AG-Zuschuss ist steuerpflichtig; Förderung ausschliesslich AN-seitig ueber Sparzulage).

### Verwaltungsanweisungen

- BMF zur Sparzulage.
- BZSt-Vordrucke.

## Workflow

### Phase 1 — VL-Hoehe und Vertragsform

- Tariflich: oft 6,65 oder 26,59 oder 40 EUR/Monat AG-Zuschuss.
- Einzelvertraglich: vereinbart.
- VL bis 480 EUR jaehrlich (40 EUR/Monat) staatlich foerderungsfaehig.

### Phase 2 — AN-Sparzulage Voraussetzungen

| Sparform | Sparzulage | Einkommensgrenze (zu versteuerndes Einkommen, Stand 2025) |
|---|---|---|
| Bausparen / wohnungswirtschaftliche Verwendung | 9 Prozent (max. 43 EUR/Jahr) | 17.900 EUR ledig / 35.800 verheiratet |
| Aktien-Fonds / Beteiligung am AG-Unternehmen | 20 Prozent (max. 80 EUR/Jahr) | 20.000 EUR ledig / 40.000 verheiratet |

(Werte Stand 2025, 5. VermBG; bei Gesetzesaenderung ueber BZSt pruefen.)

### Phase 3 — Lohnabrechnung

- AG-Zuschuss in DATEV LODAS als Lohnzuschlag eingeben.
- LSt-pflichtig: AN versteuert den Zuschuss.
- SV-pflichtig.
- AN-Sparbeitrag aus Netto (Eigenanteil moeglich, aber nicht gefoerdert).

### Phase 4 — Sparzulage-Antrag

- AN beantragt jaehrlich beim FA ueber Anlage VL der Steuererklaerung.
- Sparzulage wird mit Einkommensteuer-Erstattung ausgezahlt.
- Auszahlung erst nach Ablauf der Sperrfrist (7 Jahre).

### Phase 5 — Sperrfrist

- 7 Jahre ab Vertragsabschluss.
- Bei Aufloesung vor Ablauf: Sparzulage zurueckzuzahlen.
- Ausnahmen: Tod, dauernde Erwerbsunfaehigkeit, Arbeitslosigkeit ueber 1 Jahr.

### Phase 6 — VL-Bescheinigung

- Anlageinstitut erstellt jaehrliche Bescheinigung.
- AG benoetigt die Bescheinigung als Beleg.
- Im Lohnordner archivieren.

## Output

- VL in Lohnabrechnung konfiguriert.
- Sparzulage-Berechnung für Steuererklaerung.
- VL-Bescheinigung im Lohnordner.

## Strategie und Praxis-Tipps

- VL ist KEINE steuerliche Sonderfoerderung des AG-Zuschusses — Zuschuss ist normaler Lohn.
- Die staatliche Förderung kommt ueber AN-Sparzulage (Einkommensabhaengig).
- Bei Bauspar-VL und Aktien-VL beide Hoechstgrenzen separat (Doppelfoerderung max. 123 EUR/Jahr).
- AN mit Einkommen ueber Grenzen: VL wirtschaftlich nur als zusaetzliches Sparen ohne staatliche Zulage.
- StBVV: in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS VL-Konfiguration mit Anlageinstitut-Schnittstelle.

## Querverweise

- `stb-lohn-betriebliche-altersversorgung-grundlagen` — bAV.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-sv-beitraege-grundlagen` — SV.

## Quellen und Updates

Stand: 05/2026.

- 5. VermBG.
- EStG § 19.
- BMF zur Sparzulage.
- Sparzulage-Saetze 2025: Bausparen 9% (max. 43 EUR/Jahr, Grenze 17.900 EUR ledig), Aktien-Fonds 20% (max. 80 EUR/Jahr, Grenze 20.000 EUR ledig); 5. VermBG; BZSt pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 2 bestaetigt (VermBG-Saetze 2025 eingesetzt), 1 ersetzt (Normbestand Pruefhinweis ohne Marker) -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
