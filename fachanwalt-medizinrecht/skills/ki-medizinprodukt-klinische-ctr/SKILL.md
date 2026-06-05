---
name: ki-medizinprodukt-klinische-ctr
description: "KI Medizinprodukt Klinische CTR: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KI Medizinprodukt Klinische CTR

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **KI Medizinprodukt Klinische CTR** im Plugin Fachanwalt Medizinrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ki-medizinprodukt-highrisk` | KI-Medizinprodukt High-Risk: moderner Medizinrechts-Skill für KI-gestützte Diagnose/Prognose/Triage, MDR plus AI Act und ärztliche Letztverantwortung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `klinische-pruefung-ctr-amg` | Klinische Prüfung CTR/AMG: moderner Medizinrechts-Skill für Arzneimittelstudie, Sponsorpflichten, Ethik, Einwilligung, Prüfplanabweichung und SAE/SUSAR. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |

## Arbeitsweg

Im Plugin Fachanwalt Medizinrecht gilt für **KI Medizinprodukt Klinische CTR**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ki-medizinprodukt-highrisk`

**Fokus:** KI-Medizinprodukt High-Risk: moderner Medizinrechts-Skill für KI-gestützte Diagnose/Prognose/Triage, MDR plus AI Act und ärztliche Letztverantwortung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# KI-Medizinprodukt High-Risk

## Fachkern: KI-Medizinprodukt High-Risk
- **Spezialgegenstand:** KI-Medizinprodukt High-Risk wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: KI-Medizinprodukt High-Risk** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** KI-gestützte Diagnose/Prognose/Triage, MDR plus AI Act und ärztliche Letztverantwortung.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** MDR, MPDG, VO (EU) 2024/1689, BGB-Behandlungsvertrag, Produkthaftung und Datenschutz.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BMG ePA für alle: https://www.bundesgesundheitsministerium.de/themen/digitalisierung/elektronische-patientenakte/epa-fuer-alle
- BfArM DiGA: https://www.bfarm.de/DE/Medizinprodukte/Aufgaben/DiGA-und-DiPA/DiGA/_node.html
- EHDS Regulation EU 2025/327: https://eur-lex.europa.eu/eli/reg/2025/327/oj/
- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

## 2. `klinische-pruefung-ctr-amg`

**Fokus:** Klinische Prüfung CTR/AMG: moderner Medizinrechts-Skill für Arzneimittelstudie, Sponsorpflichten, Ethik, Einwilligung, Prüfplanabweichung und SAE/SUSAR. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# Klinische Prüfung CTR/AMG

## Fachkern: Klinische Prüfung CTR/AMG
- **Spezialgegenstand:** Klinische Prüfung CTR/AMG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Klinische Prüfung CTR/AMG** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Arzneimittelstudie, Sponsorpflichten, Ethik, Einwilligung, Prüfplanabweichung und SAE/SUSAR.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** VO (EU) 536/2014, AMG, GCP, Ethikkommission, Datenschutz und Probandenversicherung.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- EMA Advanced therapy medicinal products overview: https://www.ema.europa.eu/en/human-regulatory-overview/advanced-therapy-medicinal-products-overview
- EMA legal framework for advanced therapies: https://www.ema.europa.eu/en/human-regulatory-overview/advanced-therapy-medicinal-products-overview/legal-framework-advanced-therapies
- Paul-Ehrlich-Institut ATMP/Gentherapie: https://www.pei.de/
