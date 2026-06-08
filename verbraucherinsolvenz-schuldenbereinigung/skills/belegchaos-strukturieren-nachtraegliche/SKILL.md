---
name: belegchaos-strukturieren-nachtraegliche
description: "Belegchaos Strukturieren Nachtraegliche im Plugin Verbraucherinsolvenz Schuldenbereinigung: prüft konkret Schuldnerberatungsstelle, Verbraucherinsolvenz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Belegchaos Strukturieren Nachtraegliche

## Arbeitsbereich

**Belegchaos Strukturieren Nachtraegliche** ordnet den Fall über die tragenden Prüfungslinien: Schuldnerberatungsstelle, Verbraucherinsolvenz. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `verbraucherinsolvenz-belegchaos-strukturieren` | Schuldnerberatungsstelle: Strukturierung des Belegchaos. Skill liefert die Methodik wie Schuldnerberater die ungeordneten Belege Mahnungen Vollstreckungsbescheide Inkassobriefe und Bankauszuege des Schuldners in eine geordnete Glaeubiger- und Forderungsliste ueberfuehren. Liefert Checkliste und Vorlagenstruktur. |
| `verbraucherinsolvenz-nachtraegliche-glaeubiger` | Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung. Skill klaert ob nicht angemeldete Glaeubiger nach Erteilung der Restschuldbefreiung noch Anspruch geltend machen koennen § 301 InsO und Ausnahmen § 302 InsO. Liefert Pruefraster. |
| `verbraucherinsolvenz-pfaendungsschutzkonto` | Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto. Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos nach §§ 850k 850l ZPO Grundfreibetraege Erhoehungsbetraege Antrag und Beweisfuehrung sowie Wechselwirkung mit Insolvenzverfahren. Liefert Pruefraster. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `verbraucherinsolvenz-belegchaos-strukturieren`

**Fokus:** Schuldnerberatungsstelle: Strukturierung des Belegchaos. Skill liefert die Methodik wie Schuldnerberater die ungeordneten Belege Mahnungen Vollstreckungsbescheide Inkassobriefe und Bankauszuege des Schuldners in eine geordnete Glaeubiger- und Forderungsliste ueberfuehren. Liefert Checkliste und Vorlagenstruktur.

### Verbraucherinsolvenz Belegchaos Strukturieren

## Fachkern: Verbraucherinsolvenz Belegchaos Strukturieren
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aufgabe

Skill für Schuldnerberatungsstellen zur Strukturierung des Belegchaos.

## Ausgangslage

- Schuldner bringt Plastiktueten / Schuhkartons mit ungeordneten Unterlagen.
- Belege oft jahrealt, teils nicht mehr lesbar.
- Glaeubiger zum Teil unbekannt oder Mehrfacheintraege durch Inkasso-Kette.

## Workflow

### Schritt 1: Sortieren in Kategorien
- Forderungen (Mahnungen, Rechnungen, Vollstreckungsbescheide).
- Vertraege (Mietvertrag, Kreditvertrag, Telefonvertrag).
- Behörden (Finanzamt, Krankenkasse, Sozialamt).
- Konten (Bankauszuege, Sparbuecher).
- Einkommen (Gehaltsabrechnungen, Sozialleistungen).
- Sonstiges (Schriftverkehr, Notizen).

### Schritt 2: Glaeubigerliste anlegen
- Pro Glaeubiger eine Zeile.
- Spalten: Name, Adresse, Hauptforderung, Zinsen, Kosten, Aktenzeichen, Datum letzter Vollstreckungsakt.
- Inkasso-Ketten zusammenfuehren (Originalglaeubiger -> Inkasso 1 -> Inkasso 2).

### Schritt 3: Auskunft einholen
- Schufa-Selbstauskunft (kostenfrei).
- Schuldnerverzeichnis bei Vollstreckungsgerichten.
- Bankkonten-Abfrage.
- Anfrage an bekannte Glaeubiger nach aktuellem Forderungsstand.

### Schritt 4: Forderungen pruefen
- Verjährung (§§ 195, 199 BGB; vollstreckbare Titel 30 Jahre § 197 BGB).
- Bestreitbare Forderungen.
- Doppelte Forderungen.

### Schritt 5: Vermoegen erfassen
- Bankkonten, Sparbuecher, Lebensversicherungen, Bausparvertraege.
- Hausrat, Pkw, ggf. Immobilien.
- Pfaendungsfreies Einkommen.

## Werkzeuge

- Excel-Tabelle "Glaeubigerliste".
- Excel-Tabelle "Vermoegensaufstellung".
- Excel-Tabelle "Einkommensberechnung".
- Standardformbriefe an Glaeubiger.
- Verschluesselte Datenablage.

## Aktenfuehrung

- Eigene Mandatsakte mit Originalen / Kopien.
- Versionierung der Vermoegens- und Schuldenliste.
- Datenschutz: DSGVO Art. 30 Verzeichnis von Verarbeitungstaetigkeiten.

## Pruefraster

1. Belege vollstaendig?
2. Glaeubigerliste sauber?
3. Verjährungspruefung erfolgt?
4. Vermoegensaufstellung erstellt?
5. Einkommensberechnung erstellt?

## Output

- Strukturierte Mandatsakte.
- Glaeubigerliste.
- Vermoegensaufstellung.
- Einkommensberechnung.
- Schuldenbereinigungsplan-Entwurf.

## 2. `verbraucherinsolvenz-nachtraegliche-glaeubiger`

**Fokus:** Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung. Skill klaert ob nicht angemeldete Glaeubiger nach Erteilung der Restschuldbefreiung noch Anspruch geltend machen koennen § 301 InsO und Ausnahmen § 302 InsO. Liefert Pruefraster.

### Verbraucherinsolvenz Nachtraegliche Glaeubiger

## Fachkern: Verbraucherinsolvenz Nachtraegliche Glaeubiger
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aufgabe

Skill für nachtraeglich auftauchende Glaeubiger.

## Norm

- § 301 InsO: Wirkung der Restschuldbefreiung gegenueber allen Glaeubigern.
- § 302 InsO: Ausnahmen.

## Wirkung

- Restschuldbefreiung wirkt auch für Glaeubiger, die ihre Forderung nicht angemeldet haben.

## Ausnahmen § 302 InsO

### Nr. 1: Arglistig verschwiegen
- Schuldner hat die Forderung in der Vermoegensaufstellung arglistig nicht angegeben.

### Nr. 2: Vorsaetzliche unerlaubte Handlung
- Forderung aus vorsaetzlicher unerlaubter Handlung (§§ 823 ff. BGB).

### Nr. 3: Unterhaltsforderungen
- Unterhalt für Zeitraum vor Insolvenzverfahren.

### Nr. 4: Geldstrafen Geldbussen
- Geldstrafen und Geldbussen.

## Pruefraster

1. Forderung angemeldet?
2. Wenn nicht: Aussnahme nach § 302 InsO?
3. Vorsatz / Arglist?
4. Verjährung?

## Output

- Memo Glaeubigeranfrage nach Restschuldbefreiung.
- Schriftsatzbaustein.

## 3. `verbraucherinsolvenz-pfaendungsschutzkonto`

**Fokus:** Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto. Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos nach §§ 850k 850l ZPO Grundfreibetraege Erhoehungsbetraege Antrag und Beweisfuehrung sowie Wechselwirkung mit Insolvenzverfahren. Liefert Pruefraster.

### Verbraucherinsolvenz Pfaendungsschutzkonto

## Fachkern: Verbraucherinsolvenz Pfaendungsschutzkonto
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aufgabe

Skill für Pfaendungsschutzkonto.

## Norm

- §§ 850k, 850l ZPO.
- Pfaendungsfreigrenzen-Bekanntmachung jaehrlich neu.

## Grundfreibetrag

- Aktueller Grundfreibetrag 2024: 1.499,99 Euro/Monat (live im Mandat verifizieren).
- Erhoehungsbetraege für Unterhaltsverpflichtungen.

## Erhoehungsbetraege

- Pro unterhaltsberechtigte Person ca. 560 Euro/Monat (live verifizieren).
- Sozialleistungsbezug komplett geschuetzt.
- Kindergeld vollstaendig geschuetzt.

## Antrag

- Bei der Bank: Umwandlung in P-Konto.
- Bescheinigung der Beratungsstelle ueber Unterhaltslast.
- Vollstreckungsgericht bei besonderem Bedarf.

## Wechselwirkung Insolvenzverfahren

- P-Konto-Schutz neben Insolvenzverfahren.
- Nicht Schuldnerkonto wechseln, sondern bestehendes Konto umwandeln.

## Pruefraster

1. P-Konto eingerichtet?
2. Grundfreibetrag korrekt?
3. Erhoehungsbetraege beantragt?
4. Bankkommunikation?

## Output

- Antragsvorlage.
- Pruefraster.
