---
name: waehrend-insolvenz-verjaehrung-alttitel
description: "Waehrend Insolvenz Verjaehrung Alttitel: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Waehrend Insolvenz Verjaehrung Alttitel

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Waehrend Insolvenz Verjaehrung Alttitel** im Plugin Verbraucherinsolvenz Schuldenbereinigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vergleich-waehrend-insolvenz` | Vergleich während Insolvenz/Wohlverhalten: Drittzahlung, vorzeitige RSB, Gläubigerbefriedigung und Verfahrensende.; Normanker: InsO §§ 300 und 213 und 299; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `verjaehrung-und-alttitel` | Verjährung und Alttitel: dreißigjähriger Titel, Zinsverjährung, Hemmung und Vergleichsverhandlung.; Normanker: BGB §§ 195 und 197 und 199 und 212; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `versagung-restschuldbefreiung` | Versagungsgründe: falsche Angaben, unangemessene Verbindlichkeiten, Verletzung von Auskunfts-/Mitwirkungspflichten.; Normanker: InsO §§ 290 und 296 und 297 und 297a; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |

## Arbeitsweg

Im Plugin Verbraucherinsolvenz Schuldenbereinigung gilt für **Waehrend Insolvenz Verjaehrung Alttitel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vergleich-waehrend-insolvenz`

**Fokus:** Vergleich während Insolvenz/Wohlverhalten: Drittzahlung, vorzeitige RSB, Gläubigerbefriedigung und Verfahrensende.; Normanker: InsO §§ 300 und 213 und 299; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Vergleich während Insolvenz/Wohlverhalten: Drittzahlung, vorzeitige RSB, Gläubigerbefriedigung und Verfahrensende.

## Fachkern: Vergleich während Insolvenz/Wohlverhalten: Drittzahlung, vorzeitige RSB, Gläubigerbefriedigung und Verfahrensende.
- **Spezialgegenstand:** Vergleich während Insolvenz/Wohlverhalten: Drittzahlung, vorzeitige RSB, Gläubigerbefriedigung und Verfahrensende.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 300, 213, 299. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

## Arbeitsfragen

1. Geht es um Verbraucherinsolvenz, ehemalige Selbstständigkeit oder Regelinsolvenz?
2. Welche Gläubiger, Titel, Pfändungen, Inkassoschreiben, Steuern, Unterhalts- oder Deliktforderungen existieren?
3. Gibt es laufende Vollstreckung, Kontosperre, Mietrückstand, Stromsperre oder Arbeitsplatzrisiko?
4. Liegt ein außergerichtlicher Einigungsversuch vor oder muss er vorbereitet werden?
5. Welche Unterlagen fehlen für Antrag, Plan, Bescheinigung, Stundung und Restschuldbefreiung?

## Vorgehen

- Zuerst Existenz sichern: Konto, Miete, Energie, Krankenversicherung, Unterhalt, Arbeit.
- Danach Gläubigerliste, Forderungsgrund, Titel, Sicherheiten und § 302-Risiken erfassen.
- Dann Plan bauen: Nullplan, Quote, Drittmittel, Einmalzahlung oder dynamische Rate.
- Bei Antragstellung Formulare, Anlagen, RSB-Antrag und Stundung getrennt abhaken.
- In der Wohlverhaltensphase Obliegenheiten als Kalender und nicht als abstrakte Belehrung führen.

## Ergebnisformate

- Unterlagenliste, Gläubigertabelle, Planentwurf, Anschreiben, Gerichtsantrag-Check, P-Konto-Notfallplan, Red-Team-Vermerk oder Laienerklärung.

## 2. `verjaehrung-und-alttitel`

**Fokus:** Verjährung und Alttitel: dreißigjähriger Titel, Zinsverjährung, Hemmung und Vergleichsverhandlung.; Normanker: BGB §§ 195 und 197 und 199 und 212; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Verjährung und Alttitel: dreißigjähriger Titel, Zinsverjährung, Hemmung und Vergleichsverhandlung.

## Fachkern: Verjährung und Alttitel: dreißigjähriger Titel, Zinsverjährung, Hemmung und Vergleichsverhandlung.
- **Spezialgegenstand:** Verjährung und Alttitel: dreißigjähriger Titel, Zinsverjährung, Hemmung und Vergleichsverhandlung.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

BGB §§ 195, 197, 199, 212. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

## Arbeitsfragen

1. Geht es um Verbraucherinsolvenz, ehemalige Selbstständigkeit oder Regelinsolvenz?
2. Welche Gläubiger, Titel, Pfändungen, Inkassoschreiben, Steuern, Unterhalts- oder Deliktforderungen existieren?
3. Gibt es laufende Vollstreckung, Kontosperre, Mietrückstand, Stromsperre oder Arbeitsplatzrisiko?
4. Liegt ein außergerichtlicher Einigungsversuch vor oder muss er vorbereitet werden?
5. Welche Unterlagen fehlen für Antrag, Plan, Bescheinigung, Stundung und Restschuldbefreiung?

## Vorgehen

- Zuerst Existenz sichern: Konto, Miete, Energie, Krankenversicherung, Unterhalt, Arbeit.
- Danach Gläubigerliste, Forderungsgrund, Titel, Sicherheiten und § 302-Risiken erfassen.
- Dann Plan bauen: Nullplan, Quote, Drittmittel, Einmalzahlung oder dynamische Rate.
- Bei Antragstellung Formulare, Anlagen, RSB-Antrag und Stundung getrennt abhaken.
- In der Wohlverhaltensphase Obliegenheiten als Kalender und nicht als abstrakte Belehrung führen.

## Ergebnisformate

- Unterlagenliste, Gläubigertabelle, Planentwurf, Anschreiben, Gerichtsantrag-Check, P-Konto-Notfallplan, Red-Team-Vermerk oder Laienerklärung.

## 3. `versagung-restschuldbefreiung`

**Fokus:** Versagungsgründe: falsche Angaben, unangemessene Verbindlichkeiten, Verletzung von Auskunfts-/Mitwirkungspflichten.; Normanker: InsO §§ 290 und 296 und 297 und 297a; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Versagungsgründe: falsche Angaben, unangemessene Verbindlichkeiten, Verletzung von Auskunfts-/Mitwirkungspflichten.

## Fachkern: Versagungsgründe: falsche Angaben, unangemessene Verbindlichkeiten, Verletzung von Auskunfts-/Mitwirkungspflichten.
- **Spezialgegenstand:** Versagungsgründe: falsche Angaben, unangemessene Verbindlichkeiten, Verletzung von Auskunfts-/Mitwirkungspflichten.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 290, 296, 297, 297a. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

## Arbeitsfragen

1. Geht es um Verbraucherinsolvenz, ehemalige Selbstständigkeit oder Regelinsolvenz?
2. Welche Gläubiger, Titel, Pfändungen, Inkassoschreiben, Steuern, Unterhalts- oder Deliktforderungen existieren?
3. Gibt es laufende Vollstreckung, Kontosperre, Mietrückstand, Stromsperre oder Arbeitsplatzrisiko?
4. Liegt ein außergerichtlicher Einigungsversuch vor oder muss er vorbereitet werden?
5. Welche Unterlagen fehlen für Antrag, Plan, Bescheinigung, Stundung und Restschuldbefreiung?

## Vorgehen

- Zuerst Existenz sichern: Konto, Miete, Energie, Krankenversicherung, Unterhalt, Arbeit.
- Danach Gläubigerliste, Forderungsgrund, Titel, Sicherheiten und § 302-Risiken erfassen.
- Dann Plan bauen: Nullplan, Quote, Drittmittel, Einmalzahlung oder dynamische Rate.
- Bei Antragstellung Formulare, Anlagen, RSB-Antrag und Stundung getrennt abhaken.
- In der Wohlverhaltensphase Obliegenheiten als Kalender und nicht als abstrakte Belehrung führen.

## Ergebnisformate

- Unterlagenliste, Gläubigertabelle, Planentwurf, Anschreiben, Gerichtsantrag-Check, P-Konto-Notfallplan, Red-Team-Vermerk oder Laienerklärung.
