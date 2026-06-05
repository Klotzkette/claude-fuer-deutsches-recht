---
name: anlagenpaket-antrag-insolvenzgericht-arbeit
description: "Anlagenpaket Antrag Insolvenzgericht Arbeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anlagenpaket Antrag Insolvenzgericht Arbeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anlagenpaket Antrag Insolvenzgericht Arbeit** im Plugin Verbraucherinsolvenz Schuldenbereinigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anlagenpaket-fuer-gericht` | Anlagenpaket für Gericht: Bescheinigung, Plan, Gläubigerliste, Vermögen, Einkommen, Vollstreckungen und Nachweise.; Normanker: InsO § 305 Abs. 1; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `antrag-insolvenzgericht` | Antrag beim Insolvenzgericht: Formulare, Anlagen, Vermögensverzeichnis, Forderungsverzeichnis, RSB-Antrag und Stundung.; Normanker: InsO §§ 305 und 287 und 4a; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `arbeit-wechsel-und-mehrverdienst` | Arbeitsaufnahme, Jobwechsel und Mehrverdienst: pfändbarer Anteil, Motivation, Anzeige und Vergleichschancen.; Normanker: InsO § 295; ZPO § 850c; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |

## Arbeitsweg

Im Plugin Verbraucherinsolvenz Schuldenbereinigung gilt für **Anlagenpaket Antrag Insolvenzgericht Arbeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anlagenpaket-fuer-gericht`

**Fokus:** Anlagenpaket für Gericht: Bescheinigung, Plan, Gläubigerliste, Vermögen, Einkommen, Vollstreckungen und Nachweise.; Normanker: InsO § 305 Abs. 1; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Anlagenpaket für Gericht: Bescheinigung, Plan, Gläubigerliste, Vermögen, Einkommen, Vollstreckungen und Nachweise.

## Fachkern: Anlagenpaket für Gericht: Bescheinigung, Plan, Gläubigerliste, Vermögen, Einkommen, Vollstreckungen und Nachweise.
- **Spezialgegenstand:** Anlagenpaket für Gericht: Bescheinigung, Plan, Gläubigerliste, Vermögen, Einkommen, Vollstreckungen und Nachweise.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 305 Abs. 1. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 2. `antrag-insolvenzgericht`

**Fokus:** Antrag beim Insolvenzgericht: Formulare, Anlagen, Vermögensverzeichnis, Forderungsverzeichnis, RSB-Antrag und Stundung.; Normanker: InsO §§ 305 und 287 und 4a; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Antrag beim Insolvenzgericht: Formulare, Anlagen, Vermögensverzeichnis, Forderungsverzeichnis, RSB-Antrag und Stundung.

## Fachkern: Antrag beim Insolvenzgericht: Formulare, Anlagen, Vermögensverzeichnis, Forderungsverzeichnis, RSB-Antrag und Stundung.
- **Spezialgegenstand:** Antrag beim Insolvenzgericht: Formulare, Anlagen, Vermögensverzeichnis, Forderungsverzeichnis, RSB-Antrag und Stundung.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 305, 287, 4a. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 3. `arbeit-wechsel-und-mehrverdienst`

**Fokus:** Arbeitsaufnahme, Jobwechsel und Mehrverdienst: pfändbarer Anteil, Motivation, Anzeige und Vergleichschancen.; Normanker: InsO § 295; ZPO § 850c; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Arbeitsaufnahme, Jobwechsel und Mehrverdienst: pfändbarer Anteil, Motivation, Anzeige und Vergleichschancen.

## Fachkern: Arbeitsaufnahme, Jobwechsel und Mehrverdienst: pfändbarer Anteil, Motivation, Anzeige und Vergleichschancen.
- **Spezialgegenstand:** Arbeitsaufnahme, Jobwechsel und Mehrverdienst: pfändbarer Anteil, Motivation, Anzeige und Vergleichschancen.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 295; ZPO § 850c. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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
