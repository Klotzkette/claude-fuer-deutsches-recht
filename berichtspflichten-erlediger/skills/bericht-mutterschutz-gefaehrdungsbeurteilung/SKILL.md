---
name: bericht-mutterschutz-gefaehrdungsbeurteilung
description: "Bericht Mutterschutz Gefaehrdungsbeurteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bericht Mutterschutz Gefaehrdungsbeurteilung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bericht Mutterschutz Gefaehrdungsbeurteilung** im Plugin Berichtspflichten Erlediger. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-mutterschutz-gefaehrdungsbeurteilung` | Mutterschutz: Gefährdungsbeurteilung, Meldung an Aufsicht, Schutzmaßnahmen und Dokumentation. |
| `bericht-nis2-bsi-incident` | IT-Sicherheitsmeldungen: NIS2/BSI, Geschäftsleitung, Incident-Kategorien, Fristen, Nachbericht und Beweissicherung. |
| `bericht-produktsicherheit-rueckruf-market` | Produktsicherheitsrecht: gefährliches Produkt, Rückruf, Safety Gate, Marktüberwachung, Händler-/Herstellerrolle und Dokumentation. |

## Arbeitsweg

Im Plugin Berichtspflichten Erlediger gilt für **Bericht Mutterschutz Gefaehrdungsbeurteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bericht-mutterschutz-gefaehrdungsbeurteilung`

**Fokus:** Mutterschutz: Gefährdungsbeurteilung, Meldung an Aufsicht, Schutzmaßnahmen und Dokumentation.

# Mutterschutz Gefährdungsbeurteilung und Meldung

## Einsatz

Für HR und Führungskräfte bei Schwangerschaftsmeldung.

## Norm- und Quellenanker

MuSchG; ArbSchG; DSGVO.

## Arbeitsfragen

1. Welche Tätigkeit/Gefährdung?
2. Welche Behörde/Meldung?
3. Welche Schutzmaßnahme?

## Output

Mutterschutz-Maßnahmenplan und Behördenmeldung.

## Red Flags

- Gesundheitsdaten zu breit
- Meldung vergessen
- Beschäftigungsverbot vorschnell

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `bericht-nis2-bsi-incident`

**Fokus:** IT-Sicherheitsmeldungen: NIS2/BSI, Geschäftsleitung, Incident-Kategorien, Fristen, Nachbericht und Beweissicherung.

# NIS2/BSI Incident Reporting

## Einsatz

Für Unternehmen mit relevanten digitalen Diensten oder kritischen Prozessen.

## Norm- und Quellenanker

NIS2; BSI-Gesetz/Umsetzung live prüfen; DSGVO Art. 33/34.

## Arbeitsfragen

1. Ist das Unternehmen erfasst?
2. Welcher Incident und welche Frist?
3. Welche Behörden parallel?

## Output

Incident-Meldeplan und Vorstandsvorlage.

## Red Flags

- DSGVO-only-Meldung
- Geschäftsleitung nicht informiert
- Forensik nicht gesichert

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 3. `bericht-produktsicherheit-rueckruf-market`

**Fokus:** Produktsicherheitsrecht: gefährliches Produkt, Rückruf, Safety Gate, Marktüberwachung, Händler-/Herstellerrolle und Dokumentation.

# Produktsicherheit und Marktüberwachung melden

## Einsatz

Für Hersteller, Importeure, Händler und Plattformverkäufer.

## Norm- und Quellenanker

- Verordnung (EU) 2023/988 über die allgemeine Produktsicherheit (GPSR) für Verbraucherprodukte, Risikobewertung, Meldepflichten und Safety-Gate-Logik.
- ProdSG und Marktüberwachungsrecht für nationale Zuständigkeiten, Marktüberwachungsmaßnahmen und Ordnungswidrigkeiten.
- Spezialrecht vorrangig prüfen: Medizinprodukte, Maschinen, Spielzeug, Elektrogeräte, Funkanlagen, Lebensmittelkontakt, Kosmetik, Fahrzeuge.
- Produkthaftung, Gewährleistung, UWG und Datenschutz nur als Folge-/Parallelrisiken einordnen.

## Arbeitsfragen

1. Welches Produkt, Charge, Seriennummer, Vertriebsweg, Zeitraum und Nutzergruppe?
2. Welche Rolle: Hersteller, Bevollmächtigter, Importeur, Händler, Fulfilment-Dienstleister, Online-Marktplatz?
3. Welches Risiko: Verletzung, Brand, Stromschlag, Verschlucken, Chemie, Cyber-/Softwareupdate, Fehlanleitung?
4. Welche Maßnahme ist verhältnismäßig: Warnung, Softwarepatch, Reparatur, Austausch, Rücknahme, Rückruf?
5. Welche Behörden, Plattformen, Händler, Versicherer und Kunden müssen wann informiert werden?

## Output

Rückruf- und Behördenpaket mit Risikobewertung, Rollenmatrix, Meldeentwurf, Kundenkommunikation, Plattformtext, FAQ, Händleranweisung und Dokumentationslog.

## Red Flags

- Risiko verharmlost
- Kundenliste fehlt
- Plattform nicht informiert
- Rückruftext beruhigt, aber erklärt die konkrete Gefahr nicht
- Online-Marktplatz sperrt schneller als die interne Freigabe läuft
- Software-/Cyberrisiko wird nicht als Produktsicherheitsrisiko erkannt

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
