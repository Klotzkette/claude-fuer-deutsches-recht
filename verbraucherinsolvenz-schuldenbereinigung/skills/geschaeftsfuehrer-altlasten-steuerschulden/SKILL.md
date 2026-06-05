---
name: geschaeftsfuehrer-altlasten-steuerschulden
description: "Geschaeftsfuehrer Altlasten Steuerschulden: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geschaeftsfuehrer Altlasten Steuerschulden

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geschaeftsfuehrer Altlasten Steuerschulden** im Plugin Verbraucherinsolvenz Schuldenbereinigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geschaeftsfuehrer-altlasten` | Ehemaliger Geschäftsführer: Bürgschaften, § 15a-Altlasten, Steuerhaftung, Sozialversicherungsbeiträge und Deliktattribute.; Normanker: InsO § 304; AO §§ 69 und 34; § 266a StGB; § 15a InsO; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `steuerschulden-und-strafsteuer` | Steuerschulden: Einkommensteuer, Umsatzsteuer aus früherer Selbstständigkeit, Steuerstraftat und Restschuldbefreiungsgrenzen.; Normanker: InsO § 302 Nr. 1 Alt. 3; AO; InsO §§ 174 ff.; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `abschluss-und-neustart` | Abschluss und Neustart: RSB-Beschluss, Auskunfteien, Budget, neue Verträge, Mahnungen und Nachsorge.; Normanker: InsO §§ 300 und 301; DSGVO; Verbraucherrecht; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |

## Arbeitsweg

Im Plugin Verbraucherinsolvenz Schuldenbereinigung gilt für **Geschaeftsfuehrer Altlasten Steuerschulden**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geschaeftsfuehrer-altlasten`

**Fokus:** Ehemaliger Geschäftsführer: Bürgschaften, § 15a-Altlasten, Steuerhaftung, Sozialversicherungsbeiträge und Deliktattribute.; Normanker: InsO § 304; AO §§ 69 und 34; § 266a StGB; § 15a InsO; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Ehemaliger Geschäftsführer: Bürgschaften, § 15a-Altlasten, Steuerhaftung, Sozialversicherungsbeiträge und Deliktattribute.

## Fachkern: Ehemaliger Geschäftsführer: Bürgschaften, § 15a-Altlasten, Steuerhaftung, Sozialversicherungsbeiträge und Deliktattribute.
- **Spezialgegenstand:** Ehemaliger Geschäftsführer: Bürgschaften, § 15a-Altlasten, Steuerhaftung, Sozialversicherungsbeiträge und Deliktattribute.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 304; AO §§ 69, 34; § 266a StGB; § 15a InsO. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 2. `steuerschulden-und-strafsteuer`

**Fokus:** Steuerschulden: Einkommensteuer, Umsatzsteuer aus früherer Selbstständigkeit, Steuerstraftat und Restschuldbefreiungsgrenzen.; Normanker: InsO § 302 Nr. 1 Alt. 3; AO; InsO §§ 174 ff.; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Steuerschulden: Einkommensteuer, Umsatzsteuer aus früherer Selbstständigkeit, Steuerstraftat und Restschuldbefreiungsgrenzen.

## Fachkern: Steuerschulden: Einkommensteuer, Umsatzsteuer aus früherer Selbstständigkeit, Steuerstraftat und Restschuldbefreiungsgrenzen.
- **Spezialgegenstand:** Steuerschulden: Einkommensteuer, Umsatzsteuer aus früherer Selbstständigkeit, Steuerstraftat und Restschuldbefreiungsgrenzen.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 302 Nr. 1 Alt. 3; AO; InsO §§ 174 ff.. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 3. `abschluss-und-neustart`

**Fokus:** Abschluss und Neustart: RSB-Beschluss, Auskunfteien, Budget, neue Verträge, Mahnungen und Nachsorge.; Normanker: InsO §§ 300 und 301; DSGVO; Verbraucherrecht; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Abschluss und Neustart: RSB-Beschluss, Auskunfteien, Budget, neue Verträge, Mahnungen und Nachsorge.

## Fachkern: Abschluss und Neustart: RSB-Beschluss, Auskunfteien, Budget, neue Verträge, Mahnungen und Nachsorge.
- **Spezialgegenstand:** Abschluss und Neustart: RSB-Beschluss, Auskunfteien, Budget, neue Verträge, Mahnungen und Nachsorge.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 300, 301; DSGVO; Verbraucherrecht. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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
