# Wochenraster – Aufbau und Buckets

## Zeilenstruktur

```
A  Anfangsbestand Bank (Saldo Mo, 00:00 Uhr)
B  + Forderungseingänge (Top-10 namentlich, dann Sammelposition "Übrige")
C  + USt-Erstattung
D  + sonstige Einzahlungen (Maschinenverkauf, Gesellschafterzuschuss, Kreditauszahlung)
E  Summe Einzahlungen = SUM(B:D)

F  − Personal (Netto-Lohn + Pauschalsteuer)
G  − Sozialversicherung (drittletzter Bankarbeitstag des Monats)
H  − Lohnsteuer/SolZ/KiSt
I  − USt-Vorauszahlung (10. Folgemonat, Dauerfristverlängerung +1 Monat)
J  − KSt/GewSt-Vorauszahlung (10.03. / 10.06. / 10.09. / 10.12.)
K  − Miete/Pacht (1. des Monats)
L  − Leasing (vertragsgemäß)
M  − Zinsen + Tilgung Bankkredite
N  − Lieferantenzahlungen (geplant nach Fälligkeit und Skontofrist)
O  − Versicherungen / Energie / Sonstige Daueraufträge
P  − Sonderaufwendungen (Investitionen, Reparaturen)
Q  Summe Auszahlungen = SUM(F:P)

R  Wochensaldo = E − Q
S  Endbestand Bank = A + R
T  Freie Kreditlinie (zugesagt und ungenutzt)
U  Verfügbar gesamt = S + T

V  fällige Verbindlichkeiten Folgewoche (aus Kreditorenliste)
W  3-Wochen-Lücke kumuliert = MAX(0; V_t + V_t+1 + V_t+2 − U_t − E_t+1 − E_t+2)
X  Quote = W / V_t
Y  Ampel = WENN(X >= 10%; "ROT"; WENN(X > 0%; "GELB"; "GRÜN"))
```

## Plausibilitätsregeln

- **SV-Beiträge**: drittletzter Bankarbeitstag des Monats (Vorschätzung; Korrektur im Folgemonat).
- **Lohnsteuer**: 10. Folgemonat (bei Monatszahler), 10. Quartalsfolge (Quartalszahler).
- **USt-Vorauszahlung**: 10. Folgemonat; mit Dauerfristverlängerung (§ 46 UStDV) Verschiebung um einen Monat.
- **KSt/GewSt-Vorauszahlung**: 10.03., 10.06., 10.09., 10.12.
- **Lieferanten**: Skonto nutzen, wenn IRR > Kreditzins; sonst Zielausnutzung.
- **Großauftrag**: Zahlungseingang frühestens 30 Tage nach Lieferung; im Worst-Case 60 Tage und Skonto-Wahrnehmung durch Kunde berücksichtigen.

## Sensitivitäten

| Szenario | Forderungseingänge | Auftragsausführung | Lieferantenstundung |
|---|---|---|---|
| Best   | 100 % zum Zieltermin | wie geplant | keine zusätzliche |
| Base   | 90 % zum Zieltermin, 10 % +14 Tage | −5 % | + 7 Tage Lieferantenziel |
| Worst  | 70 % zum Zieltermin, 20 % +30 Tage, 10 % Ausfall | −15 % | + 21 Tage Lieferantenziel, 1 Großgläubiger fordert sofort |

## Reporting

- **Wöchentliche Aktualisierung** zum Montag mit Ist-Saldo und rollierender Vorschau.
- **Monatliches Reporting** an Geschäftsleitung mit Abweichungsanalyse Plan vs. Ist.
- **Quartalsweise** integrierte Planung (Ertrag/Bilanz/Liquidität) aktualisieren.

## Quellen

- IDW S 11 Rn. 35 ff. (Liquiditätsstatus, 3-Wochen-Finanzplan)
- IDW S 6 Tz. 6.4 (integrierte Planung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- K. Schmidt/Herchen, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 InsO Rn. 12
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
