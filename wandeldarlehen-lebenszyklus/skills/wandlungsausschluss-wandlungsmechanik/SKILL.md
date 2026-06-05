---
name: wandlungsausschluss-wandlungsmechanik
description: "Wandlungsausschluss Wandlungsmechanik: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wandlungsausschluss Wandlungsmechanik

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Wandlungsausschluss Wandlungsmechanik** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wandlungsausschluss-pruefung` | Prüfen ob Wandlung gesperrt oder ausgeschlossen ist bei vertraglichen oder gesetzlichen Hindernissen. §§ 134 138 BGB Nichtigkeit § 30 GmbHG Kapitalerhaltung. Prüfraster: Ausschlusstatbestaende Insolvenzreife Kapitalerhaltungsverbot Vorzugsrecht Dritter. Output: Ausschluss-Prüfmemo Empfehlung. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren). |
| `wandlungsmechanik-konzipieren` | Wandlungsmechanik eines SAFE oder Convertible Note konzipieren: Preis Verwasserungsschutz Sonderrechte. SAFE Y-Combinator-Terminologie §§ 53 55 GmbHG §§ 488 ff. BGB. Prüfraster: Wandlungspreis Bewertungsdeckel Rabatt Verwasserungsschutz MFN-Klausel Liquidationspraeference. Output: Term-Sheet Wandlungsmechanik-Beschreibung. Abgrenzung: nicht für konkrete Wandlungsberechnung (wandlungspreis-berechnung). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Wandlungsausschluss Wandlungsmechanik**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wandlungsausschluss-pruefung`

**Fokus:** Prüfen ob Wandlung gesperrt oder ausgeschlossen ist bei vertraglichen oder gesetzlichen Hindernissen. §§ 134 138 BGB Nichtigkeit § 30 GmbHG Kapitalerhaltung. Prüfraster: Ausschlusstatbestaende Insolvenzreife Kapitalerhaltungsverbot Vorzugsrecht Dritter. Output: Ausschluss-Prüfmemo Empfehlung. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren).

# Wandlungsausschluss-Prüfung

## Zweck

Dieser Skill prüft, ob das Wandlungsrecht des Lenders erloschen, verfristet, verjährt oder durch Verzicht ausgeschlossen ist, bevor eine Wandlung durchgeführt wird. Phase C des Lebenszyklus.

## Eingaben

- Wandeldarlehensvertrag (§§ 4.4, 4.10)
- Datum der Wandlungsmitteilung
- Datum der Wandlungserklärung des Lenders
- Frühere Wandlungsereignisse und Ausübungserklärungen
- Etwaige Verzichtserklärungen des Lenders
- Gesellschaftervertrag (SHA) – enthält er weitere Ausschlüsse?

## Rechtlicher Rahmen

### Primärnormen
- § 194 BGB (Verjährung: drei Jahre ab Entstehung des Anspruchs, § 199 BGB)
- § 397 BGB (Erlasserklärung / Verzicht)
- § 4.4 Wandeldarlehensvertrag (Verfristung: ein Monat nach Wandlungsmitteilung)
- § 242 BGB (Treu und Glauben – Verwirkung nach langem Zuwarten)
- § 93 InsO (Anfechtung von Verfügungen über Wandlungsrechte)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Fristprüfung (§ 4.4)
Frist: ein Monat nach Zugang der Wandlungsmitteilung. Maßgeblicher Zeitpunkt: Eingang der Wandlungsmitteilung beim Lender (§ 130 BGB). Ist Wandlungserklärung innerhalb dieser Frist eingegangen? Wenn nein: Wandlungsrecht für dieses Ereignis erloschen.

### 2. Mehrfache Wandlungsereignisse
Gilt Fristversäumnis für ein Ereignis: Wandlungsrecht erlischt nur für dieses Ereignis (§ 4.4 Satz 2). Für spätere Wandlungsereignisse bleibt das Recht bestehen. Prüfen: Gibt es ein weiteres Wandlungsereignis?

### 3. Verjährungsprüfung
Reguläre Verjährung drei Jahre (§ 195 BGB) ab Entstehung. Wandlungsrecht entsteht mit Eintritt des Wandlungsereignisses. Prüfung: Liegt der Wandlungsereignis-Zeitpunkt mehr als drei Jahre zurück?

### 4. Verwirkung prüfen (§ 242 BGB)
Hat der Lender über längere Zeit nach Kenntnis des Wandlungsereignisses nicht reagiert? Hat die Gesellschaft berechtigterweise darauf vertraut, dass kein Wandlungsrecht mehr ausgeübt wird (Vertrauensgesichtspunkt)? BGH: Verwirkung erfordert Zeit- und Umstandsmoment.

### 5. Verzicht prüfen (§ 397 BGB)
Hat der Lender schriftlich auf sein Wandlungsrecht verzichtet? Enthält eine Vereinbarung (Side Letter, SHA, Änderungsvertrag) einen Ausschluss?

### 6. Ergebnis und Empfehlung
Wandlungsrecht besteht: Weiter zu `wandlungspreis-berechnung`. Wandlungsrecht erloschen: Rückzahlungsanspruch prüfen (§ 2.2 Wandeldarlehensvertrag – Rückzahlung fällig).

## Prüfmatrix

| Ausschlussgrund | Tatbestand | Rechtsfolge |
|---|---|---|
| Fristversäumnis § 4.4 | Erklärung nach einem Monat | Erlöschen für dieses Ereignis |
| Verjährung | Mehr als drei Jahre seit Ereignis | Anspruch nicht mehr durchsetzbar |
| Verwirkung | Zeit + Umstandsmoment | Recht verwirkt |
| Verzicht § 397 BGB | Schriftliche Verzichtserklärung | Wandlungsrecht endgültig erloschen |
| Gesellschaft insolvent | Keine Kapitalerhöhung möglich | Rangrücktritt, Wandlung faktisch unmöglich |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Wandlungsmitteilung nie verschickt | Fristlauf unklar | Mitteilung verspätet | Mitteilung dokumentiert |
| Lender drei Monate ohne Reaktion | Verwirkungsrisiko | Reaktion verzögert | Reaktion innerhalb Frist |
| SHA enthält weiteren Ausschluss | Wandlungsrecht eingeschränkt | SHA auslegungsbedürftig | Kein Ausschluss |
| Insolvenz Gesellschaft | Kapitalerhöhung unmöglich | Insolvenzantrag gestellt | Gesellschaft solvent |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandelereignis-eingang/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-maturity/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Verjährungsrecht aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 305c Abs. 2 BGB (Unklarheitenregelung gegen Verwender) → § 307 BGB (AGB-Kontrolle) → § 39 InsO (Nachrang Gesellschafterdarlehen) → § 119 InsO (Unwirksamkeit insolvenzabhängiger Lösungsklauseln) → §§ 55, 56 GmbHG (Kapitalerhöhung, Voraussetzung Wandlung)

## 2. `wandlungsmechanik-konzipieren`

**Fokus:** Wandlungsmechanik eines SAFE oder Convertible Note konzipieren: Preis Verwasserungsschutz Sonderrechte. SAFE Y-Combinator-Terminologie §§ 53 55 GmbHG §§ 488 ff. BGB. Prüfraster: Wandlungspreis Bewertungsdeckel Rabatt Verwasserungsschutz MFN-Klausel Liquidationspraeference. Output: Term-Sheet Wandlungsmechanik-Beschreibung. Abgrenzung: nicht für konkrete Wandlungsberechnung (wandlungspreis-berechnung).

# Wandlungsmechanik konzipieren

## Zweck

Dieser Skill entwirft die vollständige Wandlungsmechanik für § 4 des Wandeldarlehensvertrags: Trigger-Logik, Preisformel, Schutzmechanismen (Cap, Discount, MFN) und Mitwirkungspflichten. Phase A des Lebenszyklus.

## Eingaben

- Valuation Cap (Pre-Money EUR): Höchstbewertung, bei der der Lender wandelt
- Discount (in Prozent): Abschlag auf den Preis der Finanzierungsrunde (Standard zwanzig Prozent)
- Mindest-Bewertung Qualified Financing (Pre-Money EUR): z. B. EUR 4000000
- Mindest-Investitionsvolumen Qualified Financing (EUR): z. B. EUR 500000
- Fall-back-Bewertung bei Maturity (EUR): Bewertung falls kein Wandelereignis eingetreten
- Wandlungsrecht: einseitig (Lender) oder beidseitig?
- Liquidationspräferenz: Wahlrecht Lender zwischen Bar-Rückzahlung und Wandlung?
- Pro-rata-Recht bei Folgerunde: gewünscht?
- Most-Favoured-Nation: aktiv?

## Rechtlicher Rahmen

### Primärnormen
- § 55 Abs. 1 GmbHG (Kapitalerhöhung durch Gesellschafterbeschluss)
- § 56 GmbHG (Sacheinlage bei Kapitalerhöhung)
- § 5 Abs. 1 GmbHG (Mindestanteilsnennbetrag EUR 1)
- § 272 Abs. 2 Nr. 4 HGB (Einlage in Kapitalrücklage nach Wandlung)
- § 138 BGB (Sittenwidrigkeit – Missbrauch Wandlungsrecht prüfen)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Trigger-Tatbestände abgrenzen
a) Qualified Financing: Kapitalerhöhung bar mit Mindest-Pre-Money-Bewertung EUR [X] und Mindest-Investitionsvolumen EUR [Y] ohne Berücksichtigung dieses Wandeldarlehens.
b) Maturity: Ablauf der Festen Laufzeit ohne vorheriges Wandelereignis.
c) Liquidation Event: Share Deal >50 %, Asset Deal >50 % Aktivvermögen, Fusion, IPO.

### 2. Wandlungspreis-Formel bestimmen
Wandlungspreis je Anteil (€/Anteil) = MIN(
 Pre-Money-Bewertung Runde / vollverwässerte Anteile vor Runde,
 (1 − Discount) × Pre-Money-Bewertung Runde / vollverwässerte Anteile vor Runde,
 Cap / vollverwässerte Anteile vor Runde
)
Anzahl neue Anteile = (Darlehen + aufgelaufene Zinsen) / Wandlungspreis (auf nächsten ganzen EUR aufrunden, § 5 Abs. 1 GmbHG).

### 3. Mitteilungspflicht und Fristen
Gesellschaft informiert Lender in Textform spätestens zwei Wochen vor Durchführung (Wandlungsmitteilung mit Angaben zu Investoren, Pre-Money, Investitionsvolumen, Anteilsklassen). Lender übt Wandlungsoption per Textform-Erklärung innerhalb eines Monats aus.

### 4. Neue Anteile und Rechte
Neue Anteile tragen die gleichen Rechte wie die der Investoren in der Finanzierungsrunde (oder günstigere). MFN: Wenn ein späteres Wandeldarlehen bessere Konditionen erhält, gelten diese auch hier.

### 5. Mitwirkung nach Ausübung
Gesellschaft und Gesellschafterinnen berufen unverzüglich eine Gesellschafterversammlung ein, fassen Kapitalerhöhungsbeschluss, erklären Bezugsrechtsverzicht, vollziehen Kapitalerhöhung notariell (§ 55 Abs. 2 GmbHG).

### 6. Liquidationspräferenz formulieren (falls vereinbart)
Im Liquidation Event: Lender hat Wahlrecht zwischen (a) Rückzahlung Darlehensbetrag plus Zinsen (1x non-participating) oder (b) Wandlung. Frist: zwei Wochen ab Bekanntgabe des Exit-Events.

## Beispielrechnung Wandlungspreis

| Parameter | Wert |
|---|---|
| Darlehensbetrag | EUR 250000 |
| Aufgelaufene Zinsen | EUR 25694 |
| Wandlungssumme C | EUR 275694 |
| Anzahl Anteile vor Runde | 100 |
| Pre-Money Runde | EUR 6000000 |
| Preis je Anteil (Runde) | EUR 60000 |
| Preis mit zwanzig Prozent Discount | EUR 48000 |
| Preis bei Cap EUR 4000000 | EUR 40000 |
| Wandlungspreis (MIN) | EUR 40000 (Cap greift) |
| Neue Anteile | EUR 275694 / EUR 40000 = 6.89 → aufgerundet 7 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Cap unterhalb aktueller Pre-Money-Bewertung | Lender wandelt sofort auf günstigstem Preis | Cap leicht unter erwartetem Wert | Cap deutlich über aktueller Bewertung |
| Keine Fall-back-Bewertung bei Maturity | Wandlungsbetrag unberechenbar | Grobe Schätzung vorhanden | Klarer EUR-Wert vereinbart |
| Discount über dreissig Prozent | Verwässerung Altgesellschafterinnen erheblich | Zwanzig bis dreissig Prozent | Unter zwanzig Prozent |
| MFN ohne Ausnahmen | Alle Folgerunden binden | MFN nur für gleiche Stufe | Keine MFN |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG (§§ 55 ff.) aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 55 GmbHG (Kapitalerhöhung gegen Einlage) → § 56 GmbHG (Sacheinlage, Differenzhaftung) → § 57 GmbHG (Unversehrtheit des Stammkapitals) → § 15 GmbHG (Abtretung Geschäftsanteile) → § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage aus Wandlungsagio)
