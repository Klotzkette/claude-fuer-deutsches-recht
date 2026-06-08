---
name: buergschaften-mithaftung-strafbefehl-bussgeld
description: "Buergschaften Mithaftung Strafbefehl Bussgeld im Plugin Verbraucherinsolvenz Schuldenbereinigung: prüft konkret Bürgschaften und Mithaftung, Strafbefehl, Geldstrafe und Bußgeld, Deliktforderung und § 302 InsO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Buergschaften Mithaftung Strafbefehl Bussgeld

## Arbeitsbereich

**Buergschaften Mithaftung Strafbefehl Bussgeld** ordnet den Fall über die tragenden Prüfungslinien: Bürgschaften und Mithaftung, Strafbefehl, Geldstrafe und Bußgeld. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `buergschaften-und-mithaftung` | Bürgschaften und Mithaftung: Ehepartner, Bankdarlehen, Sittenwidrigkeitseinwand und Regress.; Normanker: BGB §§ 765 ff., 138; InsO Forderungsprüfung; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |
| `strafbefehl-bussgeld-und-insolvenz` | Strafbefehl, Geldstrafe und Bußgeld: Restschuldbefreiung, Ersatzfreiheitsstrafe, Raten und Prioritäten.; Normanker: InsO § 302; StGB Geldstrafe; OWiG; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |
| `deliktforderung-und-302-inso` | Deliktforderung und § 302 InsO: vorsätzliche unerlaubte Handlung, Unterhalt, Steuerstraftat und Widerspruch gegen Attribut.; Normanker: InsO § 302; InsO § 174 Abs. 2; BGB § 823; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `buergschaften-und-mithaftung`

**Fokus:** Bürgschaften und Mithaftung: Ehepartner, Bankdarlehen, Sittenwidrigkeitseinwand und Regress.; Normanker: BGB §§ 765 ff., 138; InsO Forderungsprüfung; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Bürgschaften und Mithaftung: Ehepartner, Bankdarlehen, Sittenwidrigkeitseinwand und Regress.

## Fachkern: Bürgschaften und Mithaftung: Ehepartner, Bankdarlehen, Sittenwidrigkeitseinwand und Regress.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

BGB §§ 765 ff., 138; InsO Forderungsprüfung. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 2. `strafbefehl-bussgeld-und-insolvenz`

**Fokus:** Strafbefehl, Geldstrafe und Bußgeld: Restschuldbefreiung, Ersatzfreiheitsstrafe, Raten und Prioritäten.; Normanker: InsO § 302; StGB Geldstrafe; OWiG; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Strafbefehl, Geldstrafe und Bußgeld: Restschuldbefreiung, Ersatzfreiheitsstrafe, Raten und Prioritäten.

## Fachkern: Strafbefehl, Geldstrafe und Bußgeld: Restschuldbefreiung, Ersatzfreiheitsstrafe, Raten und Prioritäten.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 302; StGB Geldstrafe; OWiG. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 3. `deliktforderung-und-302-inso`

**Fokus:** Deliktforderung und § 302 InsO: vorsätzliche unerlaubte Handlung, Unterhalt, Steuerstraftat und Widerspruch gegen Attribut.; Normanker: InsO § 302; InsO § 174 Abs. 2; BGB § 823; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Deliktforderung und § 302 InsO: vorsätzliche unerlaubte Handlung, Unterhalt, Steuerstraftat und Widerspruch gegen Attribut.

## Fachkern: Deliktforderung und § 302 InsO: vorsätzliche unerlaubte Handlung, Unterhalt, Steuerstraftat und Widerspruch gegen Attribut.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 302; InsO § 174 Abs. 2; BGB § 823. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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
