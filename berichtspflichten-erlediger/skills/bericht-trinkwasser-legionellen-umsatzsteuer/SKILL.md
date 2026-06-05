---
name: bericht-trinkwasser-legionellen-umsatzsteuer
description: "Bericht Trinkwasser Legionellen Umsatzsteuer: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bericht Trinkwasser Legionellen Umsatzsteuer

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bericht Trinkwasser Legionellen Umsatzsteuer** im Plugin Berichtspflichten Erlediger. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bericht-trinkwasser-legionellen-meldung` | Trinkwasserpflichten: Legionellenprüfung, Anzeige, Betreiberpflicht, Mieterinformation und Maßnahmenplan. |
| `bericht-umsatzsteuer-voranmeldung-elster` | USt-Voranmeldung als Berichtspflicht: Frist, Dauerfristverlängerung, Beleglogik, innergemeinschaftliche Lieferungen und Korrektur. |
| `bericht-verdienststatistik-verdstatg` | Verdienst-/Entgeltstatistik: Auswahl, Beschäftigtengruppen, Entgeltbestandteile, Arbeitszeit, Datenschutz und Plausibilität. |

## Arbeitsweg

Im Plugin Berichtspflichten Erlediger gilt für **Bericht Trinkwasser Legionellen Umsatzsteuer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bericht-trinkwasser-legionellen-meldung`

**Fokus:** Trinkwasserpflichten: Legionellenprüfung, Anzeige, Betreiberpflicht, Mieterinformation und Maßnahmenplan.

# Trinkwasser und Legionellenmeldung

## Einsatz

Für Eigentümer, Hausverwaltungen und Betriebe mit Trinkwasseranlagen.

## Norm- und Quellenanker

- TrinkwV § 31 für Untersuchungspflichten in Bezug auf Legionella spec.
- TrinkwV § 51 für Handlungspflichten bei Erreichen des technischen Maßnahmenwerts, insbesondere Risikoabschätzung, Maßnahmen und Information.
- IfSG nur ziehen, wenn Gesundheitsamt, Infektionsschutzmaßnahme oder konkrete Gefahr für Nutzer betroffen ist.
- UBA-Empfehlungen, Landesgesundheitsbehörden und lokale Merkblätter live prüfen; sie konkretisieren Probenahme, Gefährdungsanalyse und Kommunikation praktisch.

## Arbeitsfragen

1. Welche Wasserversorgungsanlage: Gebäudewasserversorgung, mobile/zeitweilige Anlage, öffentliche oder gewerbliche Tätigkeit?
2. Liegt eine Großanlage zur Trinkwassererwärmung vor und wird Wasser an Dritte abgegeben?
3. Welche Probenahmestellen, Laborbefunde, Datum, technischer Maßnahmenwert und Laborakkreditierung liegen vor?
4. Wer ist Betreiber: Eigentümer, WEG, Hausverwaltung, Pächter, Arbeitgeber, Hotel/Kita/Pflegeheim?
5. Welche Sofortmaßnahmen sind nötig: Nutzerinformation, Duschverbot, Spülplan, technische Prüfung, Sanierung, Nachbeprobung?

## Output

Trinkwasser-Melde- und Maßnahmenplan mit Betreiberrolle, Befundtabelle, Gesundheitsamt-Kontakt, Nutzerinformation, Gefährdungsanalyse, Sanierungsfahrplan und Nachbeprobung.

## Red Flags

- Prüffrist verpasst
- Mieter nicht informiert
- Sanierung nicht dokumentiert
- Laborbefund liegt vor, aber Betreiber wartet auf "zweite Meinung" statt Handlungspflichten zu starten
- WEG/Hausverwaltung streiten intern, während Nutzerinformation und Gesundheitsamtfrist laufen
- Probenahme war nicht systemisch verwertbar, wird aber als Entwarnung verkauft

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `bericht-umsatzsteuer-voranmeldung-elster`

**Fokus:** USt-Voranmeldung als Berichtspflicht: Frist, Dauerfristverlängerung, Beleglogik, innergemeinschaftliche Lieferungen und Korrektur.

# Umsatzsteuer-Voranmeldung und ELSTER

## Einsatz

Für Unternehmen, die Steuerberichtspflichten operationalisieren müssen.

## Norm- und Quellenanker

- UStG §§ 13, 13a, 14, 15, 18 für Steuerentstehung, Steuerschuldner, Rechnung, Vorsteuer und Voranmeldung.
- AO §§ 149, 150, 152, 153, 168 für Erklärung, Verspätung, Berichtigung und Steueranmeldung unter Vorbehalt.
- UStDV, ELSTER-Hinweise und BMF-Schreiben nur aktuell verwenden; innergemeinschaftliche Meldungen mit ZM und OSS/IOSS abgleichen.

## Arbeitsfragen

1. Welche Voranmeldungsperiode, Dauerfristverlängerung, Sondervorauszahlung und Organschaft?
2. Welche Ausgangs-/Eingangsrechnungen, Gutschriften, Anzahlungen, Reverse-Charge-Fälle und Berichtigungen?
3. Welche innergemeinschaftlichen Lieferungen/Erwerbe, Dreiecksgeschäfte, OSS/IOSS, Importumsatzsteuer?
4. Stimmen UStVA, ZM, Buchhaltung, Bank, Rechnungsausgang und Warenwirtschaft?
5. Ist eine Berichtigung nach AO § 153 nötig oder nur eine laufende Korrektur in der nächsten Periode?

## Output

UStVA-Abgabecheck mit Kontenabstimmung, Steuerkennzeichen, ZM-/OSS-Abgleich, ELSTER-Protokoll, Korrekturpfad und Freigabenachweis.

## Red Flags

- Beleg fehlt
- ZM und UStVA widersprechen sich
- Dauerfristverlängerung vergessen

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 3. `bericht-verdienststatistik-verdstatg`

**Fokus:** Verdienst-/Entgeltstatistik: Auswahl, Beschäftigtengruppen, Entgeltbestandteile, Arbeitszeit, Datenschutz und Plausibilität.

# Verdienststatistik und Entgeltdaten

## Einsatz

Für Lohnbuchhaltung/HR bei amtlichen Entgelterhebungen.

## Norm- und Quellenanker

VerdStatG und BStatG live prüfen; DSGVO; Entgeltabrechnungsdaten.

## Arbeitsfragen

1. Welche Beschäftigten sind einzubeziehen?
2. Welche Entgeltbestandteile und Arbeitszeiten?
3. Welche Datenschutzfreigabe intern?

## Output

Entgeltmelde-Matrix und Plausibilitätscheck.

## Red Flags

- Bonus falsch zugeordnet
- Teilzeit nicht sauber umgerechnet
- Personendaten unnötig breit

## Arbeitsstil

Berichtspflichten werden wie kleine Verfahren behandelt: Rechtsgrundlage lesen, Pflichtenträger und Schwelle prüfen, Datenquelle sichern, nur erforderliche Daten melden, Vier-Augen-Freigabe dokumentieren, Versandnachweis ablegen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
