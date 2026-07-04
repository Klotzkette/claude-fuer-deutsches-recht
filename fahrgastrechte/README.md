# Fahrgastrechte


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fahrgastrechte`) | [`fahrgastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fahrgastrechte.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fahrgastrechte im Eisenbahnverkehr nach VO (EU) 2021/782 und EVO 2023: Verspätung/Ausfall einordnen, Entschädigung berechnen (25/50 Prozent), Forderung an die DB, Widerspruch, Schlichtung und Klage zum AG. Katalog DB-Ablehnungsgründe.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fahrgastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fahrgastrechte.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fahrgastrechte/fahrgastrechte-werkstatt.md" download><code>fahrgastrechte-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fahrgastrechte/fahrgastrechte-schnellstart.md" download><code>fahrgastrechte-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Fahrgastrechte im Eisenbahnverkehr selber geltend machen — VO (EU) 2021/782 plus EVO 2023 plus DB-Beförderungsbedingungen. Tickets erfassen Verspätung oder Zugausfall einordnen Entschädigung berechnen (25/50 Prozent ab 60/120 Minuten) Forderung an die DB Widerspruch gegen die Ablehnung Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) und Klage zum Amtsgericht. Vollmacht für Mitreisende. Katalog typischer DB-Ablehnungsgründe mit Gegenargumenten.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Worum geht es?

Wer mit der Bahn unterwegs ist und eine Verspätung von mehr als einer Stunde oder einen Zugausfall erleidet, hat einen Entschädigungsanspruch nach Art. 19 VO (EU) 2021/782: 25 Prozent des Fahrpreises ab 60 Minuten Verspätung am Zielort, 50 Prozent ab 120 Minuten. Dieses Plugin deckt den vollständigen Mandatsablauf ab: vom Erfassen der Ticket- und Reisedaten über die Berechnung des Anspruchs, das Forderungsschreiben, den Widerspruch gegen eine Ablehnung, die Schlichtung bis zur Klage vor dem Amtsgericht.

Das Plugin richtet sich an Verbraucher, die ihre Ansprüche selbst durchsetzen wollen, sowie an Anwälte, die Fahrgäste vertreten.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. EuGH-, BGH- und AG-Entscheidungen werden vor jedem Versand über curia.europa.eu, bundesgerichtshof.de oder gesetze-im-internet.de verifiziert.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `kaltstart-triage` |
| 2. Unterlagen, Sachverhalt und Quellen | `ticket-und-reisedaten-erfassen` |
| 5. Verfahren, Behörde und Gericht | `klage-amtsgericht-fahrgast`, `widerspruch` |
| 8. Spezialmodule und Schnittstellen | `anlagen-bauen`, `db-ablehnungsgruende-pruefen`, `eigenbefoerderung-und-betreuung-art-18`, `einfuehrung-vo-2021-782`, `entschaedigung-berechnen`, `forderung-an-db-erste-stufe`, `schlichtung-reise-verkehr-anrufen`, `verspaetung-und-anschlussverlust-einordnen`, `vollmacht-mitreisende` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 13 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlagen-bauen` | Wenn es um Fahrgastrechte — Anlagen bauen in Fahrgastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `db-ablehnungsgruende-pruefen` | Wenn es um Katalog der DB-Ablehnungsgründe und Gegenargumente in Fahrgastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `eigenbefoerderung-und-betreuung-art-18` | Wenn es um Eigenbeförderung und Betreuung (Art. 18. 20 VO; Paragraf 11 EVO) in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einfuehrung-vo-2021-782` | Wenn es um Einführung VO (EU) 2021/782 — Fahrgastrechte Eisenbahn in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `entschaedigung-berechnen` | Wenn es um Entschädigung berechnen in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderung-an-db-erste-stufe` | Wenn es um Forderungsschreiben — Erste Stufe in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-triage` | Wenn es um Kaltstart Triage in Fahrgastrechte geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klage-amtsgericht-fahrgast` | Wenn es um Klage zum Amtsgericht (Fahrgastrechte) in Fahrgastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `schlichtung-reise-verkehr-anrufen` | Wenn es um Schlichtungsstelle Reise & Verkehr e.V. anrufen in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ticket-und-reisedaten-erfassen` | Wenn es um Ticket- und Reisedaten erfassen in Fahrgastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `verspaetung-und-anschlussverlust-einordnen` | Wenn es um Verspätung, Zugausfall oder Anschlussverlust einordnen in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vollmacht-mitreisende` | Wenn es um Vollmacht für Mitreisende in Fahrgastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `widerspruch` | Wenn es um Fahrgastrechte-Widerspruch — Skill in Fahrgastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
