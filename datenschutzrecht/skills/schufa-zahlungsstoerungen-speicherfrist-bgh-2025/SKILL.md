---
name: schufa-zahlungsstoerungen-speicherfrist-bgh-2025
description: "Für SCHUFA-Zahlungsstörungen: Speicherfrist nach BGH 2025: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel."
---

# SCHUFA-Zahlungsstörungen: Speicherfrist nach BGH 2025

## Einsatzfall

Nutze diesen Skill, wenn eine Auskunftei erledigte Zahlungsstörungen, Restschuldbefreiung, Schuldnerverzeichnis- oder Insolvenzregisterdaten speichert und der Betroffene Löschung, Einschränkung, Berichtigung, Schadensersatz oder eine Aufsichtsbeschwerde will.

## Normenanker

- DSGVO Art. 5 Abs. 1 lit. a, c, e; Art. 6 Abs. 1 lit. f; Art. 12, 15, 16, 17, 18, 21, 22, 77, 79, 82.
- DSGVO Art. 40, wenn genehmigte Verhaltensregeln der Auskunfteien als Orientierung behauptet werden.
- BDSG § 31 als nationaler Scoring-Anker nur unionsrechtskonform verwenden.
- ZPO §§ 882c, 882e, 882f zum Schuldnerverzeichnis.
- InsO § 9 und InsBekV § 3 zu öffentlichen Insolvenzbekanntmachungen.

## Verifizierte Entscheidungsanker

- **EuGH, Urteil vom 07.12.2023 - C-634/21, SCHUFA Holding (Scoring)**: Automatisiertes Scoring kann eine Entscheidung nach Art. 22 DSGVO sein, wenn Dritte den Score maßgeblich für Vertragsentscheidungen nutzen.
- **EuGH, Urteil vom 07.12.2023 - C-26/22 und C-64/22, SCHUFA Holding (Restschuldbefreiung)**: Speicherung aus öffentlichen Insolvenzregistern darf die öffentliche Löschfrist nicht unterlaufen; Art. 5 und Art. 6 DSGVO verlangen strenge Abwägung.
- **BGH, Urteil vom 18.12.2025 - I ZR 97/25**: Für von Vertragspartnern gemeldete erledigte Zahlungsstörungen ist die Löschfrist des Schuldnerverzeichnisses nicht automatisch die Obergrenze; zulässig ist nur eine konkrete Art.-6-Abs.-1-lit.-f-Abwägung mit Datenminimierung und Einzelfallbesonderheiten.

## Prüfprogramm

1. **Datenquelle bestimmen:** Insolvenzregister, Schuldnerverzeichnis, Vertragspartnermeldung, Inkasso, Bank, Telekommunikation oder interne Scoreableitung.
2. **Zweck und Erforderlichkeit prüfen:** Bonitätsauskunft, Betrugsprävention, Kreditwürdigkeitsprüfung, Vertragspartnerinteresse; pauschale Brancheninteressen reichen nicht als Subsumtion.
3. **Betroffeneninteressen konkretisieren:** Wohnung, Konto, Kredit, Mobilfunk, berufliche Selbstständigkeit, Stigmatisierung, Dauer seit Erledigung.
4. **Rechte bündeln:** Art. 15-Auskunft, Art. 16-Berichtigung, Art. 17-Löschung, Art. 18-Einschränkung, Art. 21-Widerspruch, Art. 77-Beschwerde, Art. 79-Klage.
5. **Beweisakte bauen:** Selbstauskunft, Scoremitteilung, Ablehnungsschreiben, Forderungsausgleich, Registerlöschung, Korrespondenz, wirtschaftliche Nachteile.

## Output

Erzeuge keine pauschale Löschungsforderung. Erzeuge stattdessen:

- eine Datenquellen-Tabelle,
- einen Art.-6-/Art.-17-Abwägungsvermerk,
- einen Auskunfts- und Löschungsantrag,
- eine kurze Aufsichtsbeschwerde,
- eine Klage-/Eilrechtsschutz-Matrix mit Beweislast und Risikoampel.

## Fehlerbremse

Nicht alle erledigten Zahlungsstörungen sind wie Restschuldbefreiungsdaten zu behandeln. Wenn die Auskunftei Daten nicht aus einem öffentlichen Insolvenzregister übernommen hat, muss besonders sauber zwischen EuGH-Restschuldbefreiung und BGH-Zahlungsstörungsfall getrennt werden.
