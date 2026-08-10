# Kanzlei-Builder-Hub

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/kanzlei-builder-hub.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/kanzlei-builder-hub.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Kanzlei-Builder-Hub:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet. Beginne mit folgendem Arbeitsschritt: Dokumentenregister: Datei, Typ, Datum, Version, Autor, Signatur, Bezug, Fundstelle, Status und Lücke. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`kanzlei-builder-hub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/kanzlei-builder-hub-schnellstart.md" download><code>kanzlei-builder-hub-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/kanzlei-builder-hub-werkstatt.md" download><code>kanzlei-builder-hub-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kanzleigründung Eckermann Friedrich Sandhof Rechtsanwaltsgesellschaft mbH — Aachen](../testakten/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen/README.md) | [Gesamt-PDF](../testakten/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen/gesamt-pdf/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen_gesamt.pdf) | [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip) | [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Community-Skills für Kanzleien: Entdecken, prüfen und installieren. Durchsucht GitHub-Registries (kanzlei-skills und weitere, die über `/kanzlei-builder-hub:verzeichnis-durchsuchen` ergänzt werden können), installiert und aktualisiert Skills automatisch (mit Diff-Review), und zeigt in anderen Kanzlei-Plugins verwandte Community-Skills an. Das Erstgespräch-Interview (`kanzlei-builder-hub-kaltstart-interview`) ist gleichzeitig der Starter-Pack-Empfehlungsassistent — es fragt nach Kanzleityp und Tätigkeitsschwerpunkt und empfiehlt passende Skills zur Installation.

**Jeder Community-Skill wird vor der Installation im Rohformat angezeigt, auf Prompt-Injection-Muster gescannt und gegen das Kanzlei-Skill-Design-Framework geprüft. Sicherheits- und Berufsrechtsprüfung (DSGVO, BRAO/BORA, Mandantengeheimnis) erfolgen vor jeder Installation. Der Hub hilft beim Finden und Bewerten — die Entscheidung, was vertraut wird, liegt beim Anwender.**

---

## Für wen ist dieser Hub

Für alle, die die anderen Kanzlei-Plugins nutzen. Dies ist der App-Store.

---

## Erster Start: Kaltstart-Interview

Das Interview fragt nach Kanzleityp, Rechtsgebiet, Teamgröße und technischer Vertrautheit. Es empfiehlt ein Starter-Paket passender Community-Skills und installiert die ausgewählten.

```
/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview
```

Die Konfiguration wird gespeichert unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` und bleibt bei Plugin-Updates erhalten.

---

## Sicherheits- und Datenschutzhaltung

Installierte Community-Skills laufen mit Zugriff auf Mandantendaten, Aktendateien und das Kanzlei-Playbook. Der Hub behandelt jede Installation und jedes Update als Vertrauensentscheidung.

### Vier Verteidigungsebenen

- **Positivliste (admin-kontrolliert):** `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/positivliste.yaml` legt fest, welche Registries, Publisher und MCP-Konnektoren Community-Skills nutzen dürfen. Der Modus `permissive` (Standard) warnt bei allem außerhalb der Liste; der Modus `restrictive` (empfohlen für Kanzlei- und Unternehmensdeployments) verweigert die Installation. Die Positivliste wird geprüft, bevor Drittanbieterinhalte geladen werden.
- **Rohquelle statt Zusammenfassung:** Der Installer zeigt den vollständigen SKILL.md-Rohtext — keine KI-Zusammenfassung — bevor irgendetwas geschrieben wird.
- **Heuristische Scans:** Installer und `skills-qualitaetspruefung` scannen den Skill auf Prompt-Injection-Muster (Override-/Authority-Claims, unerlaubte Lese-/Schreibzugriffe, externe URLs, verstecktes Unicode, Shell-Ausführung, Credential-Anfragen). Diese KI-Heuristik ist kein Sicherheitsaudit.
- **Menschliche Genehmigung, jedes Mal:** Nichts wird ohne frisch eingetipptes `ja` auf Disk geschrieben. Genehmigung wird nicht aus früheren Nachrichten abgeleitet.

### Berufsrechtliches Security-Review-Gate

**Vor jeder Community-Skill-Installation** prüft der Installer:

1. **Datenschutz (DSGVO/BDSG):** Werden personenbezogene Mandantendaten verarbeitet? Ist eine Auftragsverarbeitung nach Art. 28 DSGVO erforderlich? Existiert ein entsprechender AVV?
2. **Berufsrecht (BRAO/BORA):** Entspricht der Skill den Berufspflichten nach §§ 43 ff. BRAO und §§ 2 ff. BORA? Wird die anwaltliche Unabhängigkeit gewahrt?
3. **Mandantengeheimnis:** Könnten Mandantendaten den vertraulichen Bereich verlassen (§ 43a Abs. 2 BRAO, § 203 StGB)? Ist sichergestellt, dass keine Daten unverschlüsselt übertragen oder bei Drittanbietern gespeichert werden?
4. **Technisch-organisatorische Maßnahmen (TOM):** Wurde vor dem Einsatz geprüft, ob eine TOM nach Art. 25, 32 DSGVO erforderlich ist? Dokumentation in der Verfahrensübersicht empfohlen.

Updates verwenden dieselbe Haltung: Der Auto-Updater pinnt auf Commit-SHAs (keine veränderbaren Tags), zeigt den vollständigen Diff inklusive Hooks und MCP-Änderungen und erfordert explizite Genehmigung pro Update.

Bei Problemen nach der Installation: `/kanzlei-builder-hub:deaktivieren [skill]` deaktiviert den Skill ohne Dateientfernung; `/kanzlei-builder-hub:deinstallieren [skill]` entfernt ihn vollständig. Beide Befehle sind auf Community-Skills beschränkt, die über diesen Hub installiert wurden — Erstanbieter-Plugin-Skills sind geschützt.

---

## Voraussetzungen

- Slack-Benachrichtigungen des Registry-Sync-Agenten erfordern einen konfigurierten Slack-MCP-Server. Ohne diesen schreibt der Agent seinen Digest in eine Datei.
- Die Standard-Registry-Liste in `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` wird leer ausgeliefert (außer `kanzlei-skills`). Weitere Registries können über `/kanzlei-builder-hub:verzeichnis-durchsuchen` oder durch direktes Bearbeiten von `CLAUDE.md` hinzugefügt werden.

---

## Befehle

| Befehl | Funktion |
|---|---|
| `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview` | Kanzleiprofil erstellen + Starter-Paket empfehlen |
| `/kanzlei-builder-hub:verzeichnis-durchsuchen [Suchbegriff]` | Beobachtete Registries nach Skills durchsuchen |
| `/kanzlei-builder-hub:skill-installierer [skill]` | Community-Skill installieren (mit Security- und Berufsrechtsprüfung) |
| `/kanzlei-builder-hub:automatischer-aktualisierer` | Updates für installierte Skills prüfen (mit Diff-Review) |
| `/kanzlei-builder-hub:verwandte-skills-vorschlag` | Verwandte Skills basierend auf aktueller Tätigkeit empfehlen |
| `/kanzlei-builder-hub:skills-qualitaetspruefung [skill]` | Skill gegen das Kanzlei-Skill-Design-Framework prüfen (inkl. Zitierweise und Methodik) |
| `/kanzlei-builder-hub:kanzlei-builder-hub-anpassen` | Kanzleiprofil und Einstellungen anpassen |
| `/kanzlei-builder-hub:deaktivieren [skill]` | Installierten Community-Skill deaktivieren (Dateien bleiben erhalten) |
| `/kanzlei-builder-hub:deinstallieren [skill]` | Community-Skill vollständig entfernen |

---

## Skills im Überblick

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Kanzleiprofil → Starter-Paket |
| **verzeichnis-durchsuchen** | Registries nach Skills durchsuchen |
| **skill-installierer** | Positivliste-Gate, Abruf, Rohtext-Anzeige, DSGVO/BRAO-Prüfung, QA, Installation |
| **uninstall** | Community-Skill deinstallieren (Erstanbieter-Plugin-Skills sind gesperrt) |
| **disable** | Community-Skill ohne Dateilöschung deaktivieren; später wieder aktivierbar |
| **skill-verwalter** | Referenz: Detaillierte Deinstallations-, Deaktivierungs- und Reaktivierungsworkflows |
| **skills-qualitätsprüfung** | Skill gegen das Kanzlei-Skill-Design-Framework prüfen — Design, Fehlerquellen, Trust-Surface, Zitierweise, Methodik |
| **automatischer-aktualisierer** | Updates prüfen; Diff und Trust-Review anzeigen; Anwendung nur nach expliziter Genehmigung |
| **verwandte-skills-vorschlag** | Verwandte Community-Skills nach einer Aufgabe empfehlen |
| **anpassen** | Kanzleiprofil, Positivliste, Registry-Watchlist und Aktualisierungseinstellungen anpassen |
| **playbook-aus-eigenen-daten** | Aus E-Mails, Mandantenkorrespondenz und eigenen Dokumenten ein wiederverwendbares Kanzlei-Spielbuch destillieren (DSGVO/BRAO-konforme Pseudonymisierung) |
| **fundstellenglattzieher** | Juristische Fundstellen im Text gegen die hauseigene Zitierweise prüfen und vereinheitlichen (Heftnummern, `S.`-Zusätze, Bearbeiter, Auflage, Aufsatztitel-Entfall, `vgl.`-Floskeln, Abkürzungen) |

---

## Interaktive Befehle vs. geplante Agenten

Die obigen Befehle werden bei Aufruf ausgeführt — für die aktive Mandatsarbeit. Die folgenden Agenten laufen planmäßig im Hintergrund:

| Agent | Was er beobachtet | Standard-Kadenz |
|---|---|---|
| **verzeichnis-synchronisierung** | Beobachtete Registries auf neue und aktualisierte Skills; sendet Benachrichtigungen gemäß Einstellungen | Wöchentlich |

---

## Beobachtete Registries (Standard)

Die Standard-Positivliste enthält von uns geprüfte Community-Registries. Eigene Registries können über `references/positivliste-standard.yaml` im Repo oder über die persönliche Positivliste unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/positivliste.yaml` hinzugefügt, entfernt oder zwischen den Modi gewechselt werden.

- **kanzlei-skills** — Skills für deutsche Kanzleien und Rechtsabteilungen — Kanzlei-Community auf GitHub

---

## Wie der Hub dazulernt

Das Kanzleiprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` ist nicht statisch — es verbessert sich mit der Nutzung. Der Hub liest es bei jedem `/kanzlei-builder-hub:verzeichnis-durchsuchen`- und `/kanzlei-builder-hub:verwandte-skills-vorschlag`-Aufruf neu, sodass Änderungen an Kanzleityp, Rechtsgebiet oder beobachteten Registries künftige Empfehlungen schärfen. Die Datei kann direkt bearbeitet oder mit `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview --redo` neu durchgeführt werden.

---

## Hinweise

- Community-Skills werden vor der Installation gelesen. Der **Rohtext** der SKILL.md wird angezeigt — keine Zusammenfassung — bevor etwas akzeptiert wird.
- Auto-Update ist standardmäßig deaktiviert. Pro Skill aktivierbar, wenn die Quelle vertrauenswürdig ist.
- Der `verwandte-skills-vorschlag` läuft innerhalb anderer Plugins: Während einer Aufgabe prüft er, ob die Community etwas Passendes anbietet.
- **Kanzlei-/Unternehmensdeployments:** `mode: restrictive` in `positivliste.yaml` setzen und `registries`, `publishers` und `connectors` befüllen. Im Restrictive-Modus verweigert der Installer das Abrufen, Analysieren und Installieren von allem aus nicht gelisteten Quellen.
- **Datenschutz-Hinweis:** Für jede KI-gestützte Verarbeitung von Mandantendaten empfiehlt sich eine Datenschutz-Folgenabschätzung (Art. 35 DSGVO) sowie die Überprüfung, ob eine Auftragsverarbeitung (Art. 28 DSGVO) vorliegt. Installierte Skills sind in der Verfahrensübersicht nach Art. 30 DSGVO zu dokumentieren.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-router`](skills/anschluss-router/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`kaltstart-interview`](skills/kaltstart-interview/SKILL.md), [`workflow-anschluss-skills-router`](skills/workflow-anschluss-skills-router/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`community-leistungsmatrix-fristennotiz`](skills/community-leistungsmatrix-fristennotiz/SKILL.md), [`eigenen-formular-portal-und-einreichung`](skills/eigenen-formular-portal-und-einreichung/SKILL.md), [`installiert-tatbestand-beweis-und-belege`](skills/installiert-tatbestand-beweis-und-belege/SKILL.md), [`kanzlei-quellenkarte`](skills/kanzlei-quellenkarte/SKILL.md), [`khub-leistungsmatrix-mandanten-checkliste`](skills/khub-leistungsmatrix-mandanten-checkliste/SKILL.md), [`leistungsmatrix-fristennotiz-und-naechster-schritt`](skills/leistungsmatrix-fristennotiz-und-naechster-schritt/SKILL.md), [`playbook-aus-eigenen-daten`](skills/playbook-aus-eigenen-daten/SKILL.md), [`playbook-qualitaetspruefung-beweislast-review`](skills/playbook-qualitaetspruefung-beweislast-review/SKILL.md), [`qualitaetspruefung-beweislast-und-darlegungslast`](skills/qualitaetspruefung-beweislast-und-darlegungslast/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`rechtsquellen`](skills/rechtsquellen/SKILL.md), [`spezial-kanzlei-livequellen-und-rechtsprechungscheck`](skills/spezial-kanzlei-livequellen-und-rechtsprechungscheck/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`fristen-risikoampel-mandantenkommunikation`](skills/fristen-risikoampel-mandantenkommunikation/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`kanzlei-fundstellencheck-zitate-links`](skills/kanzlei-fundstellencheck-zitate-links/SKILL.md), [`kanzleiumgebung-khub-sonderfall-livecheck`](skills/kanzleiumgebung-khub-sonderfall-livecheck/SKILL.md), [`livecheck-mehrparteien-konflikt-und-interessen`](skills/livecheck-mehrparteien-konflikt-und-interessen/SKILL.md), [`review-risikoampel-und-gegenargumente`](skills/review-risikoampel-und-gegenargumente/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`gate-behoerden-gericht-und-registerweg`](skills/gate-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`einsteiger-mandantenkommunikation-entscheidungsvorlage`](skills/einsteiger-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md), [`workflow-mandantenkommunikation`](skills/workflow-mandantenkommunikation/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`daten-red-team-und-qualitaetskontrolle`](skills/daten-red-team-und-qualitaetskontrolle/SKILL.md), [`qualitaetspruefung-builder-daten-red-team-korrektur`](skills/qualitaetspruefung-builder-daten-red-team-korrektur/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`anpassen`](skills/anpassen/SKILL.md), [`automatischer-aktualisierer`](skills/automatischer-aktualisierer/SKILL.md), [`builder-uebersicht-fuer-einsteiger`](skills/builder-uebersicht-fuer-einsteiger/SKILL.md), [`builder-zahlen-schwellen-und-berechnung`](skills/builder-zahlen-schwellen-und-berechnung/SKILL.md), [`deaktivieren`](skills/deaktivieren/SKILL.md), [`deinstallieren`](skills/deinstallieren/SKILL.md), [`deployment-eigenen-einsteiger`](skills/deployment-eigenen-einsteiger/SKILL.md), [`findet-gate-installiert`](skills/findet-gate-installiert/SKILL.md), [`fundstellenglattzieher`](skills/fundstellenglattzieher/SKILL.md), [`grosskanzlei-rollout-thema-prozesse-abbilden`](skills/grosskanzlei-rollout-thema-prozesse-abbilden/SKILL.md), [`kanzlei-prozesse-abbilden`](skills/kanzlei-prozesse-abbilden/SKILL.md), [`khub-kanzlei-coi-onboarding-bauleiter`](skills/khub-kanzlei-coi-onboarding-bauleiter/SKILL.md), [`khub-kanzlei-onboarding-bauleiter`](skills/khub-kanzlei-onboarding-bauleiter/SKILL.md), [`khub-mandantenkonferenz-paralegal-rollen`](skills/khub-mandantenkonferenz-paralegal-rollen/SKILL.md), [`khub-sonderfall-und-edge-case`](skills/khub-sonderfall-und-edge-case/SKILL.md), [`paralegal-rollen-automatisieren`](skills/paralegal-rollen-automatisieren/SKILL.md), [`qa-kanzleiweit-templating-praxis-verwalter`](skills/qa-kanzleiweit-templating-praxis-verwalter/SKILL.md), [`rentier-rechtsanwalt-spezial`](skills/rentier-rechtsanwalt-spezial/SKILL.md), ... plus 8 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; der Direktdownload lädt dieselbe Datei als Markdown. Beschreibungen stammen aus dem jeweiligen `description`-Feld.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anpassen`](skills/anpassen/SKILL.md) | Wenn es um /anpassen — Kanzleiprofil und Einstellungen anpassen in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/anpassen/SKILL.md" download><code>SKILL.md</code></a> |
| [`anschluss-router`](skills/anschluss-router/SKILL.md) | Wenn es um Kanzlei-Builder-Hub — Allgemein in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/anschluss-router/SKILL.md" download><code>SKILL.md</code></a> |
| [`automatischer-aktualisierer`](skills/automatischer-aktualisierer/SKILL.md) | Wenn es um /automatischer-aktualisierer — Automatische Aktualisierung mit Diff-Review in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/automatischer-aktualisierer/SKILL.md" download><code>SKILL.md</code></a> |
| [`builder-uebersicht-fuer-einsteiger`](skills/builder-uebersicht-fuer-einsteiger/SKILL.md) | Wenn es um Builder: Übersicht Einsteiger in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/builder-uebersicht-fuer-einsteiger/SKILL.md" download><code>SKILL.md</code></a> |
| [`builder-zahlen-schwellen-und-berechnung`](skills/builder-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Builder: Zahlen, Schwellenwerte und Berechnung in Kanzlei-Builder-Hub geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/builder-zahlen-schwellen-und-berechnung/SKILL.md" download><code>SKILL.md</code></a> |
| [`community-leistungsmatrix-fristennotiz`](skills/community-leistungsmatrix-fristennotiz/SKILL.md) | Wenn es um Community: Fristen, Form, Zuständigkeit und Rechtsweg in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/community-leistungsmatrix-fristennotiz/SKILL.md" download><code>SKILL.md</code></a> |
| [`daten-red-team-und-qualitaetskontrolle`](skills/daten-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Daten: Red-Team und Qualitätskontrolle in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/daten-red-team-und-qualitaetskontrolle/SKILL.md" download><code>SKILL.md</code></a> |
| [`deaktivieren`](skills/deaktivieren/SKILL.md) | Wenn es um /deaktivieren — Skill deaktivieren (ohne Dateilöschung) in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/deaktivieren/SKILL.md" download><code>SKILL.md</code></a> |
| [`deinstallieren`](skills/deinstallieren/SKILL.md) | Wenn es um Deinstallation in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/deinstallieren/SKILL.md" download><code>SKILL.md</code></a> |
| [`deployment-eigenen-einsteiger`](skills/deployment-eigenen-einsteiger/SKILL.md) | Wenn es um Deployment: Schriftsatz-, Brief- und Memo-Bausteine in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/deployment-eigenen-einsteiger/SKILL.md" download><code>SKILL.md</code></a> |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/dokumente-intake/SKILL.md" download><code>SKILL.md</code></a> |
| [`eigenen-formular-portal-und-einreichung`](skills/eigenen-formular-portal-und-einreichung/SKILL.md) | Wenn es um Eigenen: Formular, Portal und Einreichungslogik in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/eigenen-formular-portal-und-einreichung/SKILL.md" download><code>SKILL.md</code></a> |
| [`einsteiger-mandantenkommunikation-entscheidungsvorlage`](skills/einsteiger-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Einsteiger: Mandantenkommunikation und Entscheidungsvorlage in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/einsteiger-mandantenkommunikation-entscheidungsvorlage/SKILL.md" download><code>SKILL.md</code></a> |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Kanzlei-Builder-Hub geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/einstieg-routing/SKILL.md" download><code>SKILL.md</code></a> |
| [`findet-gate-installiert`](skills/findet-gate-installiert/SKILL.md) | Wenn es um Findet: Erstprüfung, Rollenklärung und Mandatsziel in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/findet-gate-installiert/SKILL.md" download><code>SKILL.md</code></a> |
| [`fristen-risikoampel-mandantenkommunikation`](skills/fristen-risikoampel-mandantenkommunikation/SKILL.md) | Wenn es um Fristen- und Risikoampel in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/fristen-risikoampel-mandantenkommunikation/SKILL.md" download><code>SKILL.md</code></a> |
| [`fundstellenglattzieher`](skills/fundstellenglattzieher/SKILL.md) | Wenn es um Fundstellenglattzieher in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/fundstellenglattzieher/SKILL.md" download><code>SKILL.md</code></a> |
| [`gate-behoerden-gericht-und-registerweg`](skills/gate-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Gate: Behörden-, Gerichts- oder Registerweg in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/gate-behoerden-gericht-und-registerweg/SKILL.md" download><code>SKILL.md</code></a> |
| [`grosskanzlei-rollout-thema-prozesse-abbilden`](skills/grosskanzlei-rollout-thema-prozesse-abbilden/SKILL.md) | Wenn es um Grosskanzlei-Rollout in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/grosskanzlei-rollout-thema-prozesse-abbilden/SKILL.md" download><code>SKILL.md</code></a> |
| [`installiert-tatbestand-beweis-und-belege`](skills/installiert-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Installiert: Tatbestandsmerkmale, Beweisfragen und Beleglage in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/installiert-tatbestand-beweis-und-belege/SKILL.md" download><code>SKILL.md</code></a> |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Kanzlei Builder Hub ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/juristischer-argumentationskern/SKILL.md" download><code>SKILL.md</code></a> |
| [`kaltstart-interview`](skills/kaltstart-interview/SKILL.md) | Wenn es um /kaltstart-interview — Kanzleiprofil-Interview in Kanzlei-Builder-Hub geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/kaltstart-interview/SKILL.md" download><code>SKILL.md</code></a> |
| [`kanzlei-fundstellencheck-zitate-links`](skills/kanzlei-fundstellencheck-zitate-links/SKILL.md) | Wenn es um Fundstellenglattzieher / Zitatenkorrektor in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/kanzlei-fundstellencheck-zitate-links/SKILL.md" download><code>SKILL.md</code></a> |
| [`kanzlei-prozesse-abbilden`](skills/kanzlei-prozesse-abbilden/SKILL.md) | Wenn es um Kanzlei-Prozesse abbilden in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/kanzlei-prozesse-abbilden/SKILL.md" download><code>SKILL.md</code></a> |
| [`kanzlei-quellenkarte`](skills/kanzlei-quellenkarte/SKILL.md) | Wenn es um Kanzlei Quellenkarte in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/kanzlei-quellenkarte/SKILL.md" download><code>SKILL.md</code></a> |
| [`kanzleiumgebung-khub-sonderfall-livecheck`](skills/kanzleiumgebung-khub-sonderfall-livecheck/SKILL.md) | Wenn es um Kanzleiumgebung: Verhandlung, Vergleich und Eskalation in Kanzlei-Builder-Hub geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/kanzleiumgebung-khub-sonderfall-livecheck/SKILL.md" download><code>SKILL.md</code></a> |
| [`khub-kanzlei-coi-onboarding-bauleiter`](skills/khub-kanzlei-coi-onboarding-bauleiter/SKILL.md) | Wenn es um Khub: COI-Konfliktmatrix in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/khub-kanzlei-coi-onboarding-bauleiter/SKILL.md" download><code>SKILL.md</code></a> |
| [`khub-kanzlei-onboarding-bauleiter`](skills/khub-kanzlei-onboarding-bauleiter/SKILL.md) | Wenn es um Khub: Kanzlei-Onboarding Bauleiter in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/khub-kanzlei-onboarding-bauleiter/SKILL.md" download><code>SKILL.md</code></a> |
| [`khub-leistungsmatrix-mandanten-checkliste`](skills/khub-leistungsmatrix-mandanten-checkliste/SKILL.md) | Wenn es um Khub: Leistungsmatrix in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/khub-leistungsmatrix-mandanten-checkliste/SKILL.md" download><code>SKILL.md</code></a> |
| [`khub-mandantenkonferenz-paralegal-rollen`](skills/khub-mandantenkonferenz-paralegal-rollen/SKILL.md) | Wenn es um Khub: Mandantenkonferenz-Templates in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/khub-mandantenkonferenz-paralegal-rollen/SKILL.md" download><code>SKILL.md</code></a> |
| [`khub-sonderfall-und-edge-case`](skills/khub-sonderfall-und-edge-case/SKILL.md) | Wenn es um Khub: Sonderfall und Edge-Case-Prüfung in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/khub-sonderfall-und-edge-case/SKILL.md" download><code>SKILL.md</code></a> |
| [`leistungsmatrix-fristennotiz-und-naechster-schritt`](skills/leistungsmatrix-fristennotiz-und-naechster-schritt/SKILL.md) | Wenn es um Leistungsmatrix: Fristennotiz und nächster Schritt in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/leistungsmatrix-fristennotiz-und-naechster-schritt/SKILL.md" download><code>SKILL.md</code></a> |
| [`livecheck-mehrparteien-konflikt-und-interessen`](skills/livecheck-mehrparteien-konflikt-und-interessen/SKILL.md) | Wenn es um Livecheck: Mehrparteienkonflikt und Interessenmatrix in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/livecheck-mehrparteien-konflikt-und-interessen/SKILL.md" download><code>SKILL.md</code></a> |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/output-waehlen/SKILL.md" download><code>SKILL.md</code></a> |
| [`paralegal-rollen-automatisieren`](skills/paralegal-rollen-automatisieren/SKILL.md) | Wenn es um Paralegal-Aufgaben automatisieren in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/paralegal-rollen-automatisieren/SKILL.md" download><code>SKILL.md</code></a> |
| [`playbook-aus-eigenen-daten`](skills/playbook-aus-eigenen-daten/SKILL.md) | Wenn es um Skill: Playbook aus eigenen Daten in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/playbook-aus-eigenen-daten/SKILL.md" download><code>SKILL.md</code></a> |
| [`playbook-qualitaetspruefung-beweislast-review`](skills/playbook-qualitaetspruefung-beweislast-review/SKILL.md) | Wenn es um Playbook: Internationaler Bezug und Schnittstellen in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/playbook-qualitaetspruefung-beweislast-review/SKILL.md" download><code>SKILL.md</code></a> |
| [`qa-kanzleiweit-templating-praxis-verwalter`](skills/qa-kanzleiweit-templating-praxis-verwalter/SKILL.md) | Wenn es um Skill-QA kanzleiweit in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/qa-kanzleiweit-templating-praxis-verwalter/SKILL.md" download><code>SKILL.md</code></a> |
| [`qualitaetspruefung-beweislast-und-darlegungslast`](skills/qualitaetspruefung-beweislast-und-darlegungslast/SKILL.md) | Wenn es um Qualitätsprüfung: Beweislast, Darlegungslast und Substantiierung in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/qualitaetspruefung-beweislast-und-darlegungslast/SKILL.md" download><code>SKILL.md</code></a> |
| [`qualitaetspruefung-builder-daten-red-team-korrektur`](skills/qualitaetspruefung-builder-daten-red-team-korrektur/SKILL.md) | Wenn es um Skills-QA in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/qualitaetspruefung-builder-daten-red-team-korrektur/SKILL.md" download><code>SKILL.md</code></a> |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/quellen-livecheck/SKILL.md" download><code>SKILL.md</code></a> |
| [`rechtsquellen`](skills/rechtsquellen/SKILL.md) | Wenn es um Rechtsquellen: Compliance-Dokumentation und Aktenvermerk in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/rechtsquellen/SKILL.md" download><code>SKILL.md</code></a> |
| [`rentier-rechtsanwalt-spezial`](skills/rentier-rechtsanwalt-spezial/SKILL.md) | Wenn es um Einzelanwalt-Spezial in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/rentier-rechtsanwalt-spezial/SKILL.md" download><code>SKILL.md</code></a> |
| [`review-risikoampel-und-gegenargumente`](skills/review-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Review: Risikoampel, Gegenargumente und Verteidigungslinien in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/review-risikoampel-und-gegenargumente/SKILL.md" download><code>SKILL.md</code></a> |
| [`security-installation`](skills/security-installation/SKILL.md) | Wenn es um Security: Dokumentenmatrix, Lückenliste und Nachforderung in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/security-installation/SKILL.md" download><code>SKILL.md</code></a> |
| [`skill-installation-security-gate`](skills/skill-installation-security-gate/SKILL.md) | Wenn es um Skill-Installation mit Security-, Herkunfts- und Mandatsgeheimnis-Gate in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/skill-installation-security-gate/SKILL.md" download><code>SKILL.md</code></a> |
| [`skill-installierer`](skills/skill-installierer/SKILL.md) | Wenn es um Skill-Installer in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/skill-installierer/SKILL.md" download><code>SKILL.md</code></a> |
| [`skill-templating-praxis`](skills/skill-templating-praxis/SKILL.md) | Wenn es um Skill-Templating Praxis in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/skill-templating-praxis/SKILL.md" download><code>SKILL.md</code></a> |
| [`skill-verwalter`](skills/skill-verwalter/SKILL.md) | Wenn es um Skill-Manager in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/skill-verwalter/SKILL.md" download><code>SKILL.md</code></a> |
| [`spezial-kanzlei-livequellen-und-rechtsprechungscheck`](skills/spezial-kanzlei-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Kanzlei: Livequellen- und Rechtsprechungscheck in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/spezial-kanzlei-livequellen-und-rechtsprechungscheck/SKILL.md" download><code>SKILL.md</code></a> |
| [`uebersicht-einsteiger-deaktivieren`](skills/uebersicht-einsteiger-deaktivieren/SKILL.md) | Wenn es um Builder: Übersicht Einsteiger in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/uebersicht-einsteiger-deaktivieren/SKILL.md" download><code>SKILL.md</code></a> |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/unterlagen-luecken/SKILL.md" download><code>SKILL.md</code></a> |
| [`verwandte-skills-vorschlag`](skills/verwandte-skills-vorschlag/SKILL.md) | Wenn es um /verwandte-skills-vorschlag — Verwandte-Skills-Empfehlung in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/verwandte-skills-vorschlag/SKILL.md" download><code>SKILL.md</code></a> |
| [`verzeichnis-durchsuchen`](skills/verzeichnis-durchsuchen/SKILL.md) | Wenn es um /verzeichnis-durchsuchen — Skill-Registry-Browser in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/verzeichnis-durchsuchen/SKILL.md" download><code>SKILL.md</code></a> |
| [`workflow-anschluss-skills-router`](skills/workflow-anschluss-skills-router/SKILL.md) | Wenn es um Anschluss-Skills Router in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/workflow-anschluss-skills-router/SKILL.md" download><code>SKILL.md</code></a> |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/workflow-chronologie-und-belegmatrix/SKILL.md" download><code>SKILL.md</code></a> |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Kanzlei-Builder-Hub geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/workflow-kaltstart-und-routing/SKILL.md" download><code>SKILL.md</code></a> |
| [`workflow-mandantenkommunikation`](skills/workflow-mandantenkommunikation/SKILL.md) | Wenn es um Mandantenkommunikation in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/workflow-mandantenkommunikation/SKILL.md" download><code>SKILL.md</code></a> |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/workflow-redteam-qualitygate/SKILL.md" download><code>SKILL.md</code></a> |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/skills/workflow-unterlagen-lueckenliste/SKILL.md" download><code>SKILL.md</code></a> |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
