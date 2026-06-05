---
name: deckungsprozess-vvg-rechtsabteilung
description: "Deckungsprozess VVG Rechtsabteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Deckungsprozess VVG Rechtsabteilung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Deckungsprozess VVG Rechtsabteilung** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `deckungsprozess-zustaendigkeit-215-vvg` | Deckungsprozess gegen Versicherer: Anspruchsgrundlage, Klageantrag, örtliche Zuständigkeit § 215 VVG, Beweislast, Streitwert, Feststellungs-/Leistungsklage. |
| `rechtsabteilung-rechtsschutzversicherung-im-massenverfahren` | Rechtsabteilungs-Fachmodul für Rechtsschutzversicherung im Massenverfahren: Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `sachverstaendigenverfahren-versicherung` | Sachverständigenverfahren: Obmann, Gutachterauftrag, Bindungswirkung, Kosten, Beweiswert und Schnittstelle zum Prozess. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Deckungsprozess VVG Rechtsabteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `deckungsprozess-zustaendigkeit-215-vvg`

**Fokus:** Deckungsprozess gegen Versicherer: Anspruchsgrundlage, Klageantrag, örtliche Zuständigkeit § 215 VVG, Beweislast, Streitwert, Feststellungs-/Leistungsklage.

# Deckungsprozess und Gerichtsstand § 215 VVG

## Einsatz

Der Skill bringt die versicherungsrechtliche Prüfung in eine prozessfähige Klagestruktur.

## Norm- und Quellenanker

VVG §§ 1, 14, 215; ZPO §§ 253, 256, 29; BGB; spartenspezifische Normen/AVB.

## Arbeitsfragen

1. Leistungsklage, Feststellungsklage oder Stufen-/Auskunftsantrag?
2. Welches Gericht ist örtlich und sachlich zuständig?
3. Welche Tatsachen müssen im Klageentwurf vollständig stehen?
4. Welche Beweise sind verfügbar oder durch Sachverständige zu führen?

## Output

Klagegerüst, Zuständigkeitsnotiz, Streitwertberechnung und Beweisplan.

## Red Flags

- falscher Gerichtsstand
- Deckung und Haftung vermischt
- Klageantrag zu unbestimmt
- Sachverständigenbeweis ohne Anknüpfungstatsachen

## Anschluss-Skills

- vers-deckungsablehnung-redteam
- sachverstaendigenverfahren-versicherung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `rechtsabteilung-rechtsschutzversicherung-im-massenverfahren`

**Fokus:** Rechtsabteilungs-Fachmodul für Rechtsschutzversicherung im Massenverfahren: Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: Rechtsschutzversicherung im Massenverfahren

## Spezialkern: Rechtsabteilung: Rechtsschutzversicherung im Massenverfahren

- **Konkretes Problem:** Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet.
- **Norm-/Quellenanker:** einschlägige Spezialnormen des Plugin-Fachgebiets, amtliche Gesetzesfassungen, Behördenpraxis und verifizierte Rechtsprechung mit Datum und Aktenzeichen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VVG, ARB, BGH-Linie live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Deckungsanfrage, Stichentscheid und Erfolgsaussicht werden taktisch vorbereitet.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.

## 3. `sachverstaendigenverfahren-versicherung`

**Fokus:** Sachverständigenverfahren: Obmann, Gutachterauftrag, Bindungswirkung, Kosten, Beweiswert und Schnittstelle zum Prozess.

# Sachverständigenverfahren in der Versicherung

## Einsatz

Für Sach- und BU-/Unfallnahbereiche, wenn Höhe oder Ursache fachlich streitig ist und AVB ein Verfahren vorsehen.

## Norm- und Quellenanker

VVG/AVB je Sparte; BGB Werkvertrags-/Gutachterrecht; ZPO Sachverständigenbeweis.

## Arbeitsfragen

1. Gibt es ein vertragliches Sachverständigenverfahren und wann wird es ausgelöst?
2. Welche Fragen werden dem Gutachter gestellt?
3. Welche Bindung hat das Ergebnis?
4. Wie werden Kosten verteilt und Fristen gesichert?

## Output

Gutachterauftrag, Fragenkatalog, Obmannvorschlag und Prozessrisiko.

## Red Flags

- Gutachter beantwortet Rechtsfragen
- Bindungswirkung überschätzt
- Partei benennt fachlich ungeeigneten Gutachter
- Fristen im AVB-Verfahren übersehen

## Anschluss-Skills

- wohngebaeude-leitungswasser-sturm-hagel-brand
- unfallversicherung-invaliditaet-fristen-gliedertaxe

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
