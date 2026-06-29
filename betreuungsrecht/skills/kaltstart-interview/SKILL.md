---
name: kaltstart-interview
description: "Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil mit Angaben zur Rolle (betreute Person / Angehöriger / ehrenamtlicher Familienbetreuer / Berufsbetreuer / Vereinsbetreuer / Behördenbetreuer / anwaltliche Begleitung), Betreuungsgericht, Aufgabenkreisen, Unterstützungsst..."
---

# /betreuungsrecht:betreuungsrecht-kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

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

- **Rolle:** betreute Person / Angehöriger / ehrenamtlicher Familienbetreuer / ehrenamtlicher Betreuer ohne persönliche Bindung / Berufsbetreuer / Vereinsbetreuer / Behördenbetreuer / Anwalt mit Betreuungsmandaten?
- **Status:** Schon bestellt, nur vorgeschlagen, eigene Anregung läuft, einstweilige Anordnung oder bloße Vorsorgefrage?
- **Anwaltlicher Ansprechpartner** (falls vorhanden): Name, Kanzlei, Erreichbarkeit
- **Berufsverband:** BdB, VfB, VGT, sonstiger oder keiner
- **Unterstützungsstellen:** zuständige Betreuungsbehörde, Betreuungsverein, Betreuungsgericht, ggf. Verhinderungsbetreuung

### 2. Aktuelle Betreuungen

- **Anzahl aktiver Betreuungen:** N; bei Familienbetreuern meist eine konkrete Betreuung, bei Berufsbetreuern Praxisumfang gesondert erfassen.
- **Typische Aufgabenkreise:** Vermögenssorge / Gesundheitssorge / Aufenthaltsbestimmung / Wohnungsangelegenheiten / Postangelegenheiten / Behördenangelegenheiten
- **Zuständige Betreuungsgerichte:** Hauptgericht + weitere
- **Wünsche der betreuten Person:** bekannte Wünsche, frühere Äußerungen, Patientenverfügung, Vorsorgevollmacht, Betreuungsverfügung
- **Dringende Alltagsthemen:** Bank, Miete/Heim, Pflege, Arzt, Bescheide, Schulden, Telefonbetrug, Angehörigenkonflikt

### 3. Berichtswesen

- **Berichtsformat:** Anfangs-/Jahres-/Schlussbericht nach § 1863 BGB; bei Vermögenssorge zusätzlich Vermögensverzeichnis nach § 1835 BGB und Vermögens-/Rechnungslegung nach gerichtlicher Vorgabe.
- **Berichtsturnus:** Standardmäßig jährlich; bei großem Vermögen ggf. abweichend
- **Vorlagen vorhanden:** ja / nein, Ablageort
- **Kalender/Reminder:** gewünschtes System: Papierkalender, Outlook, Apple Kalender, Excel, Aufgabenliste, keine Integration.

### 4. Genehmigungspflichtige Geschäfte

Bekannte Bereiche, in denen regelmäßig Genehmigungen erforderlich sind:
- Grundstücksgeschäfte (§ 1850 BGB)
- Erbschaftsausschlagung (§ 1851 BGB)
- Aufgabe oder Kündigung selbstgenutzten Wohnraums (§ 1833 BGB)
- Freiheitsentziehende Maßnahmen (§ 1831 BGB)
- Sterilisation (§ 1830 BGB)
- Risikoreiche Heilbehandlung (§ 1829 BGB)

### 5. Eskalation

- **Wer hilft bei rechtlich kritischen Fragen?** Betreuungsverein / Betreuungsbehörde / Betreuungsgericht / Anwalt / Notar / Pflegeberatung
- **Wann wird das Betreuungsgericht informiert?** Bei jedem genehmigungspflichtigen Geschäft, bei wesentlichen Statusänderungen, bei vermutetem Missbrauch
- **Überforderungsschwelle:** Welche Themen soll das System rot markieren, damit nicht allein entschieden wird?

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
 - `/betreuungsrecht:ehrenamtlicher-betreuer-erster-monat` — bei familiärer oder ehrenamtlicher Erstbetreuung
 - `/betreuungsrecht:dokumentenscan-aktenablage-und-belegmappe` — bei unsortierten Scans, Fotos und Bescheiden
 - `/betreuungsrecht:kalender-reminder-und-fristenmanagement` — für Berichtspflichten, Bescheidfristen und Routinekontakte
- Hinweis auf Datenschutz, Vertraulichkeit und sparsame Verarbeitung sensibler Gesundheits- und Vermögensdaten

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtlicher Rahmen

- **§ 1814 ff. BGB** — Betreuungsrecht (seit 01.01.2023 reformiert)
- **§ 1821 BGB** — Pflichten des Betreuers und Wünsche der betreuten Person
- **§§ 1829–1832 BGB** — Genehmigungspflichten
- **VBVG** — Vergütung Berufsbetreuer
- **BtOG** und **BtRegV** — Organisation, Registrierung beruflicher Betreuer und Unterstützung ehrenamtlicher Betreuer
- **FamFG §§ 271–341** — Verfahrensrecht Betreuungssachen

## Hinweise

Dieses Plugin ersetzt keine anwaltliche Beratung. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang, Gesetze im Internet) zu prüfen.
