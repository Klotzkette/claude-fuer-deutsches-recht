# Dashboard-Vorlage

*Referenziert durch die Dashboard-Angebots-Schutzregel. Dashboards sollen einfach und einheitlich bleiben — der Wert liegt in der Schnelligkeit der Erfassung, nicht im visuellen Aufwand.*

## Aufbau (von oben nach unten)

1. **Titel und Metadaten.** Gegenstand, Erstellungsdatum, Abdeckungsbereich. Eine Zeile.
2. **Zusammenfassungsstatistik.** Die relevanten Kennzahlen, farblich codiert. Beispiel: „40 Befunde: 🔴 3 blockierend · 🟠 8 hoch · 🟡 15 mittel · 🟢 14 niedrig — 6 fällig diese Woche." Dies ist die wertvollste Zeile. Sie muss auf einen Blick lesbar sein.
3. **Prüfhinweis.** Dasselbe Einblock-Format wie bei jeder anderen Ausgabe. Quellen, Geltungsbereich, Vorbehalte, Hinweis vor Verwendung. Dashboards lassen die Sicherheitsmetadaten nicht weg.
4. **Diagramm(e).** Maximal eines oder zwei. Wählen Sie das Diagramm, das die Struktur am besten zeigt:
   - **Risikoverteilung** (Balken): Anzahl nach Schweregrad. Verwenden für Befunde, Probleme, Hinweise.
   - **Kategorieaufschlüsselung** (Kreis oder gestapelter Balken): Anzahl nach Typ. Verwenden für OSS-Lizenzen, Vertragsarten, Mandatskategorien.
   - **Zeitschiene** (Gantt-ähnlich oder sortierte Tabelle): Termine in chronologischer Reihenfolge. Verwenden für Verlängerungsregister, Fristentracker, Closing-Checklisten.
   - Nie mehr als zwei. Ein Dashboard mit fünf Diagrammen ist ein Bericht — und Berichte sind schwerer zu lesen als die Tabelle allein.
5. **Die Tabelle.** Sortierbar, filterbar, farblich nach Schweregrad/Status codiert. Spalten: die aus der Ursprungsausgabe, gekürzt auf das, was auf einen Bildschirm passt. Die Spalte „Details" oder „Anmerkungen" steht zuletzt — sie wird als erste abgeschnitten.
6. **Der Entscheidungsbaum.** Dieselben Optionen wie in der Textausgabe. „Wie weiter?"

## Darstellung je nach Oberfläche

- **Cowork / Claude Desktop:** HTML-Artefakt. Eigenständige Einzeldatei, CSS inline. Keine externen Abhängigkeiten, kein CDN, kein npm. Tabellen: HTML `<table>` mit `data-sort`-Attributen und einem kleinen inline-JS-Sortierer. Diagramme: Inline-SVG oder Unicode-Blocksymbole für Balkendiagramme. JS auf ein Minimum beschränken — nur Sortieren und Filtern, nichts weiter.
- **Claude Code:** Dieselbe HTML-Datei in den Ausgabeordner des Plugins schreiben (`~/.claude/plugins/config/claude-fuer-deutsches-recht/<plugin>/ausgaben/dashboard-<thema>-<datum>.html`) und dem Nutzenden mitteilen, wie die Datei geöffnet wird: `open <Pfad>` unter macOS, oder „Im Browser öffnen." Zusätzlich eine Markdown-Version mit Unicode-Balkendiagrammen für die Zusammenfassungsstatistik erstellen, damit der Überblick auch im Terminal sichtbar ist, ohne den Browser zu öffnen.
- **Excel (optional, wo es passt):** Bei `tabellarischer-prüfung`, `verlängerungsregister`, `gesellschafts-compliance` und allem, was der Nutzende in eine Besprechung mitbringt oder mit Dritten teilt. Die bestehende Excel-Ausgabespezifikation verwenden. Die Formel-Injektions-Verteidigung anwenden.
- **Unsichere Eingaben escapen (bei jedem Dashboard, jedes Mal):** Jeder Wert, der von außerhalb der aktuellen Sitzung stammt — OSS-Paket-/Lizenzfelder aus Drittanbieter-Manifests, Vertragstext der Gegenseite, Due-Diligence-Befunde, Anbieternamen, Mandatsbeschreibungen, jede durch Nutzer oder Datenraum bereitgestellte Zeichenkette — muss HTML-escaped sein, bevor er in das Dokument gelangt. Die Zeichen `&`, `<`, `>`, `"`, `'` sind als HTML-Entities zu codieren, wenn sie in Tabellenzellen, Zusammenfassungszeilen, Diagrammbeschriftungen und Tooltip-Text geschrieben werden. Im inline-JS-Sortierer/Filter den Zellinhalt über `textContent` setzen, nie über `innerHTML`. Keine `<script>`-Blöcke ausgeben, deren Inhalt nicht vertrauenswürdige Zeichenketten interpoliert. Nicht vertrauenswürdige URLs nicht ohne Schema-Prüfung (`http:` / `https:` / `mailto:`) in `href`- oder `src`-Attribute rendern. Dies ist das HTML-Äquivalent der Formel-Injektions-Verteidigung auf der Excel-Seite — dieselbe Bedrohung (durch Angreifer kontrollierter Zelleninhalt), andere Ausführungsumgebung (Browser-JS statt Tabellenformel). Ein Dashboard, das der Prüfende im Browser öffnet, ist eine Vertrauensgrenze — behandeln Sie es entsprechend.

## Auf Klarheit setzen

- **Farbpalette:** Rot / Orange / Gelb / Grün für Schweregrade. Grau für neutral. Blau für Status. Nichts anderes.
- **Keine Animationen, keine Frameworks, keine externen Schriftarten.** Ein Dashboard, das offline nicht funktioniert, ist keines.
- **Keine cleveren Layouts.** Zusammenfassung, Prüfhinweis, Diagramm, Tabelle, Entscheidungsbaum. Von oben nach unten. Jedes Dashboard sieht gleich aus, damit der Lesende weiß, wo er suchen muss.
- **Die Markdown-Version ist wichtig.** Einige Nutzende arbeiten im Terminal und werden keinen Browser öffnen. Die Zusammenfassungszeile mit Unicode-Balken (z. B. `🔴 ███ 3  🟠 ████████ 8  🟡 ███████████████ 15  🟢 ██████████████ 14`) gibt ihnen den Überblick auf einen Blick.

## Mandatsspezifische Kennzahlen (Risikoampel)

Bei Mandatsübersichts-Dashboards gelten folgende Standardkennzahlen:

| KPI | Bedeutung | Anzeige |
|---|---|---|
| Offene Mandate gesamt | Aktive Mandate im Bearbeitungsstand | Zahl |
| Fällige Fristen (7 Tage) | Gesetzliche oder vereinbarte Fristen in den nächsten 7 Tagen | 🔴 bei > 0 |
| Fristen (30 Tage) | Gesetzliche oder vereinbarte Fristen in den nächsten 30 Tagen | 🟠 |
| Risikoampel gesamt | Verteilung blockierend / hoch / mittel / niedrig | Farbbalken |
| Mandatsstatus | Aktiv / Ruhend / Abgeschlossen | Kategorieaufschlüsselung |
| Letzte Aktualisierung | Zeitstempel der Datenbasis | Metadaten |

**Statusfarben:**
- 🔴 Blockierend — sofortiger Handlungsbedarf, Frist läuft ab oder gesetzliche Pflicht verletzt
- 🟠 Hoch — dringendes Handeln innerhalb von 7 Tagen erforderlich
- 🟡 Mittel — Handlung innerhalb von 30 Tagen erforderlich
- 🟢 Niedrig — kein unmittelbarer Handlungsbedarf, aber im Blick behalten
- ⚪ Unbewertet — noch kein Risiko-Screening durchgeführt
