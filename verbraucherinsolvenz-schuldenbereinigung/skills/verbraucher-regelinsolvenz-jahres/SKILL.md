---
name: verbraucher-regelinsolvenz-jahres
description: "Verbraucher Regelinsolvenz Jahres im Plugin Verbraucherinsolvenz Schuldenbereinigung: prüft konkret Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz, Verbraucherinsolvenz, Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Verbraucher Regelinsolvenz Jahres

## Arbeitsbereich

**Verbraucher Regelinsolvenz Jahres** ordnet den Fall über die tragenden Prüfungslinien: Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz, Verbraucherinsolvenz, Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `verbraucher-oder-regelinsolvenz` | Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.; Normanker: InsO § 304; § 15a InsO als Altlast; Forderungsstruktur; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung. |
| `verbraucherinsolvenz-3-jahres-restschuldbefreiung` | Verbraucherinsolvenz: 3-Jahres-Restschuldbefreiung. Skill behandelt die seit 01.10.2020 geltende verkuerzte Frist auf drei Jahre Voraussetzungen Versagungsgruende Mitwirkungspflichten Verfahrensgang. Aktuelle Diskussion zur Folgen bei nachtraeglich auftauchenden Glaeubigern. Liefert Pruefraster. |
| `verbraucherinsolvenz-aussergerichtl-schuldenbereinigung` | Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305 InsO. Skill leitet durch die Erstellung des ersten Vergleichsvorschlags von der Vermoegens- und Schuldenliste ueber die Quotenberechnung bis zur formalen Vorlage an die Glaeubiger. Behandelt Pflicht zur Beilage Bescheinigung der geeigneten Stelle / des geeigneten Beraters. Liefert Vorlagenstruktur und Pruefraster. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `verbraucher-oder-regelinsolvenz`

**Fokus:** Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.; Normanker: InsO § 304; § 15a InsO als Altlast; Forderungsstruktur; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

# Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.

## Fachkern: Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 304; § 15a InsO als Altlast; Forderungsstruktur. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

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

## 2. `verbraucherinsolvenz-3-jahres-restschuldbefreiung`

**Fokus:** Verbraucherinsolvenz: 3-Jahres-Restschuldbefreiung. Skill behandelt die seit 01.10.2020 geltende verkuerzte Frist auf drei Jahre Voraussetzungen Versagungsgruende Mitwirkungspflichten Verfahrensgang. Aktuelle Diskussion zur Folgen bei nachtraeglich auftauchenden Glaeubigern. Liefert Pruefraster.

# Verbraucherinsolvenz 3 Jahres Restschuldbefreiung

## Fachkern: Verbraucherinsolvenz 3 Jahres Restschuldbefreiung
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aufgabe

Skill für die verkuerzte Restschuldbefreiung.

## Norm

- § 287 Abs. 2 InsO (Frist 3 Jahre seit 01.10.2020).
- Insolvenzrechtsreform-Gesetz vom 22.12.2020.

## Voraussetzungen

- Verbraucher- oder Regelinsolvenz.
- Wohlverhaltensphase: Mitwirkungspflichten.
- Keine Versagungsgruende (§ 290 InsO).

## Wohlverhaltensphase

### Pflichten
- Erwerbsobliegenheit.
- Abfuehrungspflicht (Pfaendungsbetrag).
- Meldepflicht bei Wohnsitz-/Berufswechsel.
- Auskunftspflicht.
- Erbschaftspflicht (50 Prozent der Erbschaft).
- Treuhaender informieren.

### Verstoss
- Versagungsgrund § 290 InsO.
- Treuhaender beantragt Aufhebung.

## Versagungsgruende § 290 InsO

- Verurteilung wegen § 283 ff. StGB Bankrottdelikte.
- Schaedigende Vermoegensverlagerung.
- Verletzung von Aufklaerungspflichten.
- Verletzung der Erwerbsobliegenheit.

## Nachtraeglich auftauchende Glaeubiger

- § 301 InsO: Restschuldbefreiung wirkt auch für nicht angemeldete Glaeubiger.
- Ausnahme: arglistig verschwiegene Forderungen (§ 302 InsO).

## Pruefraster

1. Verfahrensgang korrekt?
2. Mitwirkungspflichten erfuellt?
3. Versagungsgruende ausgeschlossen?
4. Nachtraegliche Glaeubiger ueberraschen?

## Output

- Memo Restschuldbefreiung.
- Pruefraster Wohlverhaltensphase.
- Schriftsatzbaustein bei Versagungsantrag.

## 3. `verbraucherinsolvenz-aussergerichtl-schuldenbereinigung`

**Fokus:** Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305 InsO. Skill leitet durch die Erstellung des ersten Vergleichsvorschlags von der Vermoegens- und Schuldenliste ueber die Quotenberechnung bis zur formalen Vorlage an die Glaeubiger. Behandelt Pflicht zur Beilage Bescheinigung der geeigneten Stelle / des geeigneten Beraters. Liefert Vorlagenstruktur und Pruefraster.

# Verbraucherinsolvenz Aussergerichtl Schuldenbereinigung

## Fachkern: Verbraucherinsolvenz Aussergerichtl Schuldenbereinigung
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aufgabe

Skill für den ersten Vergleichsvorschlag im aussergerichtlichen Schuldenbereinigungsverfahren.

## Norm

- § 305 InsO (Insolvenzverordnung).
- Schuldnerberatungsstellen-Recht der Länder.

## Voraussetzungen

- Schuldner ist Verbraucher (kein selbststaendiges Wirtschaftsleben).
- Erfolglose aussergerichtliche Einigung nach § 305 Abs. 1 Nr. 1 InsO.

## Erstellung des Vergleichsvorschlags

### Schritt 1: Vermoegens- und Schuldenliste
- Gesamtschuldenstand mit Glaeubigern, Hauptforderung, Kosten, Zinsen.
- Verfuegbares Einkommen unter Beruecksichtigung der Pfaendungsfreigrenzen (§ 850c ZPO i.V.m. Pfaendungstabelle).
- Verfuegbare Aktiva (Bankkonten, Pkw, Hausrat, ggf. Wohnung).

### Schritt 2: Quotenberechnung
- Realistisch erfuellbare Quote.
- Typische Spanne 0-30 Prozent.
- Sondervorschriften für einzelne Glaeubigertypen (z. B. Finanzamt nach AO).

### Schritt 3: Vergleichsvorschlag
- Form: Schriftlich.
- Inhalt: Hoehe der Quote, Zahlungsmodalitaet (Einmalzahlung, Monatsraten), Laufzeit (max. 6-Monate Plan), Restschuldbefreiung.

### Schritt 4: Beilagen
- Bescheinigung der geeigneten Stelle (anerkannte Schuldnerberatungsstelle, Rechtsanwalt, Steuerberater).
- Vermoegens- und Schuldenliste.
- Einkommensnachweise.

## Vorgehen bei Glaeubigerantworten

- Annahme aller Glaeubiger: aussergerichtliche Einigung erfolgreich.
- Ablehnung durch einzelnen Glaeubiger: gerichtliches Verfahren nach § 306 InsO.

## Pruefraster

1. Vermoegens- und Schuldenliste vollstaendig?
2. Quote realistisch?
3. Bescheinigung vorhanden?
4. Glaeubigerantworten dokumentiert?

## Output

- Vorlagentext Vergleichsvorschlag.
- Vermoegensaufstellung Muster.
- Antwortauswertungstabelle.
