---
name: krankenversicherung-beitraege-krankheit
description: "Krankenversicherung Beitraege Krankheit im Plugin Verbraucherinsolvenz Schuldenbereinigung: prüft konkret Krankenversicherung und Beiträge, Krankheit, Pflege, Behinderung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Krankenversicherung Beitraege Krankheit

## Arbeitsbereich

**Krankenversicherung Beitraege Krankheit** ordnet den Fall über die tragenden Prüfungslinien: Krankenversicherung und Beiträge, Krankheit, Pflege. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `krankenversicherung-und-beitraege` | Krankenversicherung und Beiträge: gesetzlich/privat, Beitragsrückstände, Notlagentarif, Selbstständigenaltlasten.; Normanker: SGB V; VVG; InsO Forderungsbehandlung; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |
| `krankheit-pflege-behinderung` | Krankheit, Pflege, Behinderung: Mehrbedarf, Nachweise, Erwerbsobliegenheit und pfändungsfreie Leistungen.; Normanker: SGB IX/XI/XII; ZPO Pfändungsschutz; InsO § 295; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |
| `lohnpfaendung-und-arbeitgeber` | Lohnpfändung und Arbeitgeber: pfändbarer Betrag, Drittschuldner, Abtretung, Offenlegung und Arbeitsplatzschutz.; Normanker: ZPO §§ 850 ff.; InsO §§ 35 und 36; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `krankenversicherung-und-beitraege`

**Fokus:** Krankenversicherung und Beiträge: gesetzlich/privat, Beitragsrückstände, Notlagentarif, Selbstständigenaltlasten.; Normanker: SGB V; VVG; InsO Forderungsbehandlung; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Krankenversicherung und Beiträge: gesetzlich/privat, Beitragsrückstände, Notlagentarif, Selbstständigenaltlasten.

## Fachkern: Krankenversicherung und Beiträge: gesetzlich/privat, Beitragsrückstände, Notlagentarif, Selbstständigenaltlasten.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

SGB V; VVG; InsO Forderungsbehandlung. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 2. `krankheit-pflege-behinderung`

**Fokus:** Krankheit, Pflege, Behinderung: Mehrbedarf, Nachweise, Erwerbsobliegenheit und pfändungsfreie Leistungen.; Normanker: SGB IX/XI/XII; ZPO Pfändungsschutz; InsO § 295; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Krankheit, Pflege, Behinderung: Mehrbedarf, Nachweise, Erwerbsobliegenheit und pfändungsfreie Leistungen.

## Fachkern: Krankheit, Pflege, Behinderung: Mehrbedarf, Nachweise, Erwerbsobliegenheit und pfändungsfreie Leistungen.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

SGB IX/XI/XII; ZPO Pfändungsschutz; InsO § 295. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 3. `lohnpfaendung-und-arbeitgeber`

**Fokus:** Lohnpfändung und Arbeitgeber: pfändbarer Betrag, Drittschuldner, Abtretung, Offenlegung und Arbeitsplatzschutz.; Normanker: ZPO §§ 850 ff.; InsO §§ 35 und 36; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Lohnpfändung und Arbeitgeber: pfändbarer Betrag, Drittschuldner, Abtretung, Offenlegung und Arbeitsplatzschutz.

## Fachkern: Lohnpfändung und Arbeitgeber: pfändbarer Betrag, Drittschuldner, Abtretung, Offenlegung und Arbeitsplatzschutz.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

ZPO §§ 850 ff.; InsO §§ 35, 36. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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
