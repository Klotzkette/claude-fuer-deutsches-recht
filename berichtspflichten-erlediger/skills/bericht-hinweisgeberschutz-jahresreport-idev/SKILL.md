---
name: bericht-hinweisgeberschutz-jahresreport-idev
description: "Bericht Hinweisgeberschutz Jahresreport Idev: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bericht Hinweisgeberschutz Jahresreport Idev

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bericht Hinweisgeberschutz Jahresreport Idev** im Plugin Berichtspflichten Erlediger. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-hinweisgeberschutz-jahresreport` | Hinweisgeberstelle: Fallregister, Rückmeldefristen, Vertraulichkeit, Maßnahmen, Statistik und Geschäftsleitungsreport. |
| `bericht-idev-estatistik-core` | Elektronische Statistikmeldungen über IDEV/eSTATISTIK.core: Zugang, Rollen, Importdateien, Plausibilitätsprüfung, Versandnachweis und interne Ablage. |
| `bericht-immobilien-gebaeudeenergie-geg` | Gebäudeenergie: Energieausweis, Nachrüstpflichten, Heizungsdaten, Förder-/Meldeunterlagen und Vermieter-/Eigentümerpflichten. |

## Arbeitsweg

Im Plugin Berichtspflichten Erlediger gilt für **Bericht Hinweisgeberschutz Jahresreport Idev**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bericht-hinweisgeberschutz-jahresreport`

**Fokus:** Hinweisgeberstelle: Fallregister, Rückmeldefristen, Vertraulichkeit, Maßnahmen, Statistik und Geschäftsleitungsreport.

# HinSchG Reporting und Fallregister

## Einsatz

Für interne Meldestellen im Mittelstand.

## Norm- und Quellenanker

HinSchG; DSGVO; Arbeitsrecht; Geschäftsgeheimnisgesetz.

## Arbeitsfragen

1. Welche Meldungen und Fristen?
2. Welche Vertraulichkeit?
3. Welche Maßnahmen/Reports?

## Output

HinSchG-Dashboard und Geschäftsleitungsbericht.

## Red Flags

- Identität zu breit geteilt
- Rückmeldung vergessen
- NDA kollidiert mit Hinweisgeberschutz

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `bericht-idev-estatistik-core`

**Fokus:** Elektronische Statistikmeldungen über IDEV/eSTATISTIK.core: Zugang, Rollen, Importdateien, Plausibilitätsprüfung, Versandnachweis und interne Ablage.

# IDEV und eSTATISTIK.core praktisch nutzen

## Einsatz

Für Sachbearbeiter, die aus Excel/ERP fristgerecht und nachweisbar an Statistikportale melden müssen.

## Norm- und Quellenanker

BStatG; Verfahrenshinweise der Statistischen Ämter live prüfen; DSGVO; IT-Sicherheitsgrundsätze.

## Arbeitsfragen

1. Welcher Meldeweg ist zugelassen?
2. Welche Zugangsdaten und Rollen bestehen?
3. Welche Plausifehler treten auf?
4. Wie wird Versand beweissicher archiviert?

## Output

Portal-Checkliste, Importdatenplan, Plausifehlerprotokoll und Versandnachweis.

## Red Flags

- Portalaccount nur auf Privatmail
- keine Kopie der Abgabe
- Plausifehler ignoriert
- Test- und Echtmeldung verwechselt

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 3. `bericht-immobilien-gebaeudeenergie-geg`

**Fokus:** Gebäudeenergie: Energieausweis, Nachrüstpflichten, Heizungsdaten, Förder-/Meldeunterlagen und Vermieter-/Eigentümerpflichten.

# Gebäudeenergie und GEG-Nachweise

## Einsatz

Für Unternehmen mit Betriebsimmobilien.

## Norm- und Quellenanker

- GEG §§ 47 ff. für Nachrüstung bestehender Gebäude, insbesondere oberste Geschossdecke/Leitungen je nach Fall.
- GEG §§ 60 ff. und §§ 71 ff. für Heizungsprüfung, Heizungsoptimierung und Anforderungen an neue Heizungen live prüfen.
- GEG §§ 79 ff. für Energieausweise, Vorlagepflichten, Aushang und Pflichtangaben in Immobilienanzeigen.
- Förderrecht, kommunale Wärmeplanung, Landesvollzug und Bußgeldpraxis live prüfen; nicht aus alten Heizungsdebatten ableiten.

## Arbeitsfragen

1. Welche Immobilie: Wohn-/Nichtwohngebäude, gemischt genutzt, Denkmal, WEG, Betriebsgebäude, vermietet, verkauft, neu erworben?
2. Welche Pflichten: Energieausweis, Aushang, Nachrüstung, Heizungsprüfung, hydraulischer Abgleich, Dämmung, Betreiber-/Eigentümerinformation?
3. Welche Daten fehlen: Baujahr, Nutzfläche, Anlagenbuch, Energieträger, Verbrauchsdaten, Wartung, Wärmeplanung, Förderbescheid?
4. Wer ist Adressat: Eigentümer, Vermieter, WEG, Verwalter, Erwerber, Mieter, Makler, Anlagenbetreiber?
5. Was ist Frist, was ist nur Planungsstand, und welche Ausnahme muss belegt werden?

## Output

GEG-Nachweischeck mit Pflicht, Norm, Adressat, Frist, Datenquelle, Ausnahme, Förderbezug, Mieter-/WEG-Kommunikation und Bußgeldrisiko.

## Red Flags

- Energieausweis abgelaufen
- Heizungstausch nicht dokumentiert
- Mieterinformation fehlt
- WEG-Beschluss und öffentlich-rechtliche Pflicht laufen auseinander
- Förderzusage wird als Erfüllungsnachweis missverstanden
- Energieausweis wird ausgestellt, obwohl die Datengrundlage sichtbar falsch oder veraltet ist

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
