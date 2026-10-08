---
name: eu-schwelle-vergabeordnung-richtlinie-2014-24
description: 'Ermittelt aus Vergabestellensicht den EU-Schwellenwert und das richtige Regime: Schätzstichtag, Auftraggeber- und Auftragsart, Netto-Gesamtwert, Optionen, Laufzeit, Lose, wiederkehrender Bedarf und Umgehungsverbot. Ordnet 2026/2027 die Verordnungen 2025/2150; 2025/2151; 2025/2152 und 2025/2487 korrekt zu und liefert Rechen- und Regimevermerk.'
---

# EU-Schwelle, Auftragswert und Vergaberegime festlegen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Einsatzlage

Einsetzen, wenn die Verfahrensordnung oder der Rechtsweg vom Auftragswert abhängt, mehrere Lose/Phasen/Systeme zusammenhängen, Optionen oder Verlängerungen bestehen, ein gemischter Auftrag vorliegt oder die Akte einen Wert knapp unter der EU-Schwelle ausweist.

## Rechtsfehlerbremse

Aufteilung ist nicht pauschal verboten. Fach- und Teillose können nach § 97a GWB geboten sein. § 3 Abs. 2 VgV untersagt dagegen die Wahl der Berechnungsmethode oder Aufteilung in der Absicht, das Oberschwellenrecht zu umgehen. Deshalb Losbildung und Schwellenwertaddition getrennt prüfen.

## Normenanker

- §§ 103, 106 GWB: Auftragsart und EU-Schwellenwerte.
- § 3 VgV: geschätzter Netto-Gesamtwert, Schätzstichtag, Optionen, Lose, wiederkehrende Leistungen, Rahmenvereinbarung und dynamisches Beschaffungssystem.
- § 2 SektVO, § 2 KonzVgV und § 3 VSVgV: jeweilige Spezialberechnung.
- § 97a GWB: Losgrundsatz und Ausnahmen; nicht mit dem Additionsgebot verwechseln.
- § 187 Abs. 2 GWB: Bei vor dem 1. Juli 2026 begonnenen Verfahren für die Losregel das fortgeltende alte Recht bestimmen.
- Art. 4 und 5 RL 2014/24/EU sowie die einschlägige Spezialrichtlinie.

## Quellenkarte 2026/2027

| Regime | Unionsquelle für 2026/2027 | Kontrollwert netto |
|---|---|---|
| klassische Liefer-/Dienstleistung | Delegierte Verordnung (EU) 2025/2152 zur RL 2014/24/EU | 140000 Euro nur für Bundeskanzleramt und Bundesministerien; 216000 Euro für sonstige klassische Auftraggeber |
| klassische Bauleistung | Delegierte Verordnung (EU) 2025/2152 | 5404000 Euro |
| Sektoren | Delegierte Verordnung (EU) 2025/2150 zur RL 2014/25/EU | 432000 Euro Liefer-/Dienstleistung; 5404000 Euro Bau |
| Konzession | Delegierte Verordnung (EU) 2025/2151 zur RL 2014/23/EU | 5404000 Euro |
| Verteidigung/Sicherheit | Delegierte Verordnung (EU) 2025/2487 zur RL 2009/81/EG | 432000 Euro Liefer-/Dienstleistung; 5404000 Euro Bau |

Die Werte sind Kontrollwerte, keine Dauerwerte. Vor Freigabe ELI/EUR-Lex, § 106 GWB, Geltungszeitraum und Sondertatbestände für soziale/besondere Dienstleistungen oder subventionierte Aufträge am Schätzstichtag öffnen.

## Prüfprogramm

1. **Schätzstichtag fixieren:** Datum der Absendung der Bekanntmachung oder sonstige Verfahrenseinleitung, Aktenversion und damals objektiv verfügbare Daten belegen.
2. **Regime klassifizieren:** Auftraggeber, Auftragsart, gemischte Leistungen, Sektorentätigkeit, Konzession oder Verteidigung/Sicherheit bestimmen. Die Verordnung nicht nur nummerisch nennen, sondern der richtigen Richtlinie zuordnen.
3. **Rechenbasis bilden:** sämtliche Zahlungen ohne Umsatzsteuer, Mengen, Laufzeit, Prämien, Optionen und Verlängerungen mit Quelle und Annahme erfassen.
4. **Zusammenrechnung prüfen:** Lose, zeitliche Phasen, wiederkehrende Beschaffungen, funktionale/technische/wirtschaftliche Einheit, Rahmenhöchstwert und geplante Abrufe einzeln begründen. Keine Addition allein wegen organisatorischer Nähe und keine Trennung allein wegen Haushaltsstelle oder Fachbereich.
5. **Kontrollrechnung:** Basisszenario, obere realistische Variante und Sensitivität um die Schwelle rechnen; Formeln und Eingabefelder gegenprüfen.
6. **Rechtsfolge bestimmen:** GWB/VgV beziehungsweise Spezialregime, Bekanntmachung, Verfahrensart, zuständiger Rechtsweg und gegebenenfalls Berichtigung oder Rückversetzung ableiten.
7. **Freigabe:** Rechenweg, Quelle, Stichtag, Verantwortliche und Gegenprüfung in der Vergabeakte festhalten.

## Pflichtoutput

- Regimeentscheidung in einem Satz.
- Rechenmatrix `Position | Menge | Laufzeit | Option | Los | Netto-Wert | Quelle | Annahme`.
- Additions-/Trennungsmatrix mit tatsächlichem Grund und Gegenargument.
- Quellenzeile mit § 106 GWB, richtiger Delegierter Verordnung, Geltungsdatum und Abrufdatum.
- Entscheidung `oberschwellig`, `unterschwellig` oder `nicht freigabefähig` samt nächster Verfahrenshandlung.

## Belege und Aktenlücken

- Bedarfs-, Mengen- und Laufzeitplanung; Optionen und Verlängerungsklauseln.
- Losplan, zusammengehörige Projekte, Vorjahresverträge, Rahmenvereinbarungen und Abrufprognosen.
- Marktpreise, Haushaltsansatz und belastbare Fachschätzung; der Haushaltsansatz ersetzt die Schätzung nicht.
- Freigabefassung der Rechenmappe und unveränderbarer Export für die Vergabeakte.

## Weiterleitung

- Nur aktuelle Beträge oder Landeswertgrenzen unsicher: `schwellenwerte-2026-2027-livecheck`.
- Rechenakte im Detail aufbauen: `02-auftragswert-schaetzung` und `schnittstelle-zahlen-schwellen-und-berechnung`.
- Aus dem Ergebnis die Verfahrensart wählen: `03-schwellenwert-pruefung` und `04-verfahrensart-waehlen`.
