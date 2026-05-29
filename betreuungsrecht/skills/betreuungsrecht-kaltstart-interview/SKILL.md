---
name: betreuungsrecht-kaltstart-interview
description: "Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md mit Angaben zur Betreuerrolle (Berufsbetreuer / ehrenamtlich / Vereinsbetreuer / Behördenbetreuer), zuständigem Betreuungsgericht, typischen Aufgabenkreisen (Vermögenssorge / Gesundheitssorge / Aufenthaltsbestimmung) und Eskalationsstrukturen. Lädt bei Erstinstallation oder wenn die Konfiguration noch [PLATZHALTER]-Marker enthält. Mit --redo für ein erneutes Interview, mit --integrationen-prüfen nur für eine Konnektoren-Prüfung."
---

# /betreuungsrecht:betreuungsrecht-kaltstart-interview

## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (Dokumentenspeicher, E-Mail-System für Betreuungsbehörde-Kommunikation, Kalender für Anhörungs-/Berichtstermine). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `✓` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren.

---

## Kaltstart-Interview: Betreuungsrecht

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Berufsbetreuer (§ 1897 Abs. 6 BGB) / ehrenamtlicher Betreuer / Vereinsbetreuer / Behördenbetreuer / Anwalt mit Betreuungsmandaten?
- **Anwaltlicher Ansprechpartner** (bei Nicht-Anwälten): Name, Kanzlei, Erreichbarkeit
- **Berufsverband:** BdB, VfB, VGT, sonstiger oder keiner
- **Aufsichtsbehörde** (bei Berufsbetreuern): zuständige Betreuungsbehörde, Stammbehörde nach BtRegG

### 2. Aktuelle Betreuungen

- **Anzahl aktiver Betreuungen:** N (für Berufsbetreuer: Höchstgrenzen § 23 Abs. 1 VBVG beachten)
- **Typische Aufgabenkreise:** Vermögenssorge / Gesundheitssorge / Aufenthaltsbestimmung / Wohnungsangelegenheiten / Postangelegenheiten / Behördenangelegenheiten
- **Zuständige Betreuungsgerichte:** Hauptgericht + weitere

### 3. Berichtswesen

- **Berichtsformat:** Jahresbericht nach § 1840 BGB i.V.m. § 1841 BGB (Vermögensverzeichnis, Rechnungslegung)
- **Berichtsturnus:** Standardmäßig jährlich; bei großem Vermögen ggf. abweichend
- **Vorlagen vorhanden:** ja / nein, Ablageort

### 4. Genehmigungspflichtige Geschäfte

Bekannte Bereiche, in denen regelmäßig Genehmigungen erforderlich sind:
- Grundstücksgeschäfte (§ 1850 BGB)
- Erbschaftsausschlagung (§ 1851 BGB)
- Heim-/Pflegeverträge mit längerer Bindung (§ 1907 BGB a. F. / §§ 1831 ff. BGB n. F.)
- Freiheitsentziehende Maßnahmen (§ 1831 BGB)
- Sterilisation (§ 1830 BGB)
- Risikoreiche Heilbehandlung (§ 1829 BGB)

### 5. Eskalation

- **Wer entscheidet bei rechtlich kritischen Fragen?** Eigene Entscheidung / Rücksprache mit Anwalt / Rücksprache mit Betreuungsverein / Anfrage beim Betreuungsgericht
- **Wann wird das Betreuungsgericht informiert?** Bei jedem genehmigungspflichtigen Geschäft, bei wesentlichen Statusänderungen, bei vermutetem Missbrauch

### 6. Standort und Sprachen

- **Bundesland / Betreuungsgerichtsbezirk:** [Bayern / NRW / etc.]
- **Sprachkenntnisse der Betreuten:** Deutsch / weitere

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde (Zusammenfassung der Antworten)
- Welche Skills jetzt sinnvoll als nächstes laufen können:
  - `/betreuungsrecht:vermögensverzeichnis-prüfung` — bei Eröffnung einer Betreuung
  - `/betreuungsrecht:genehmigungspflicht-prüfung` — vor wesentlichen Geschäften
  - `/betreuungsrecht:jahresbericht-betreuungsgericht` — bei jährlicher Berichtspflicht
- Hinweis auf das Mandatsgeheimnis (§ 1816 Abs. 1 BGB, § 203 StGB analog für Berufsbetreuer)

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rechtlicher Rahmen

- **§ 1814 ff. BGB** — Betreuungsrecht (seit 01.01.2023 reformiert)
- **§ 1816 BGB** — Verschwiegenheitspflicht des Betreuers
- **§§ 1829–1832 BGB** — Genehmigungspflichten
- **VBVG** — Vergütung Berufsbetreuer
- **BtRegG** — Betreuungsregistergesetz (Registrierungspflicht für Berufsbetreuer seit 2023)
- **FamFG §§ 271–341** — Verfahrensrecht Betreuungssachen

## Hinweise

Dieses Plugin ersetzt keine anwaltliche Beratung. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang, Gesetze im Internet) zu prüfen.
