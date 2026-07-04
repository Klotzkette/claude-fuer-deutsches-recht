# Kanzlei-Builder-Hub

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kanzlei-builder-hub`) | [`kanzlei-builder-hub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kanzleigründung Eckermann Friedrich Sandhof Rechtsanwaltsgesellschaft mbH — Aachen** (`kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen`) | [Gesamt-PDF lesen](../testakten/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen/gesamt-pdf/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen_gesamt.pdf) | [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`kanzlei-builder-hub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/kanzlei-builder-hub-werkstatt.md" download><code>kanzlei-builder-hub-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/kanzlei-builder-hub/kanzlei-builder-hub-schnellstart.md" download><code>kanzlei-builder-hub-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Kanzleigründung Eckermann Friedrich Sandhof Rechtsanwaltsgesellschaft mbH — Aachen: [Gesamt-PDF](../testakten/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen/gesamt-pdf/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen_gesamt.pdf), [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip), [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
| **skills-qualitaetspruefung** | Skill gegen das Kanzlei-Skill-Design-Framework prüfen — Design, Fehlerquellen, Trust-Surface, Zitierweise, Methodik |
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
| 1. Einstieg und Fallrouting | `anschluss-router`, `dokumente-intake`, `einstieg-routing`, `kaltstart-interview`, `workflow-anschluss-skills-router`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `community-leistungsmatrix-fristennotiz`, `eigenen-formular-portal-und-einreichung`, `installiert-tatbestand-beweis-und-belege`, `kanzlei-quellenkarte`, `khub-leistungsmatrix-mandanten-checkliste`, `leistungsmatrix-fristennotiz-und-naechster-schritt`, `playbook-aus-eigenen-daten`, `playbook-qualitaetspruefung-beweislast-review`, `qualitaetspruefung-beweislast-und-darlegungslast`, `quellen-livecheck`, `rechtsquellen`, `spezial-kanzlei-livequellen-und-rechtsprechungscheck`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `fristen-risikoampel-mandantenkommunikation`, `kanzlei-fundstellencheck-zitate-links`, `kanzleiumgebung-khub-sonderfall-livecheck`, `livecheck-mehrparteien-konflikt-und-interessen`, `review-risikoampel-und-gegenargumente` |
| 5. Verfahren, Behörde und Gericht | `gate-behoerden-gericht-und-registerweg` |
| 6. Ergebnis, Schreiben und Kommunikation | `einsteiger-mandantenkommunikation-entscheidungsvorlage`, `output-waehlen`, `workflow-mandantenkommunikation` |
| 7. Kontrolle, Qualität und Gegenprüfung | `daten-red-team-und-qualitaetskontrolle`, `qualitaetspruefung-builder-daten-red-team-korrektur`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `anpassen`, `automatischer-aktualisierer`, `builder-uebersicht-fuer-einsteiger`, `builder-zahlen-schwellen-und-berechnung`, `deaktivieren`, `deinstallieren`, `deployment-eigenen-einsteiger`, `findet-gate-installiert`, `fundstellenglattzieher`, `grosskanzlei-rollout-thema-prozesse-abbilden`, `kanzlei-prozesse-abbilden`, `khub-kanzlei-coi-onboarding-bauleiter`, `khub-kanzlei-onboarding-bauleiter`, `khub-mandantenkonferenz-paralegal-rollen`, `khub-sonderfall-und-edge-case`, `paralegal-rollen-automatisieren`, `qa-kanzleiweit-templating-praxis-verwalter`, `rentier-rechtsanwalt-spezial`, ... plus 8 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anpassen` | Wenn es um /anpassen — Kanzleiprofil und Einstellungen anpassen in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anschluss-router` | Wenn es um Kanzlei-Builder-Hub — Allgemein in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `automatischer-aktualisierer` | Wenn es um /automatischer-aktualisierer — Automatische Aktualisierung mit Diff-Review in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `builder-uebersicht-fuer-einsteiger` | Wenn es um Builder: Uebersicht Einsteiger in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `builder-zahlen-schwellen-und-berechnung` | Wenn es um Builder: Zahlen, Schwellenwerte und Berechnung in Kanzlei-Builder-Hub geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `community-leistungsmatrix-fristennotiz` | Wenn es um Community: Fristen, Form, Zuständigkeit und Rechtsweg in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `daten-red-team-und-qualitaetskontrolle` | Wenn es um Daten: Red-Team und Qualitätskontrolle in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `deaktivieren` | Wenn es um /deaktivieren — Skill deaktivieren (ohne Dateilöschung) in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `deinstallieren` | Wenn es um Deinstallation in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `deployment-eigenen-einsteiger` | Wenn es um Deployment: Schriftsatz-, Brief- und Memo-Bausteine in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| `dokumente-intake` | Wenn es um Dokumentenintake in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eigenen-formular-portal-und-einreichung` | Wenn es um Eigenen: Formular, Portal und Einreichungslogik in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einsteiger-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Einsteiger: Mandantenkommunikation und Entscheidungsvorlage in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Kanzlei-Builder-Hub geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `findet-gate-installiert` | Wenn es um Findet: Erstprüfung, Rollenklärung und Mandatsziel in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristen-risikoampel-mandantenkommunikation` | Wenn es um Fristen- und Risikoampel in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fundstellenglattzieher` | Wenn es um Fundstellenglattzieher in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `gate-behoerden-gericht-und-registerweg` | Wenn es um Gate: Behörden-, Gerichts- oder Registerweg in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `grosskanzlei-rollout-thema-prozesse-abbilden` | Wenn es um Grosskanzlei-Rollout in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `installiert-tatbestand-beweis-und-belege` | Wenn es um Installiert: Tatbestandsmerkmale, Beweisfragen und Beleglage in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `kaltstart-interview` | Wenn es um /kaltstart-interview — Kanzleiprofil-Interview in Kanzlei-Builder-Hub geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kanzlei-fundstellencheck-zitate-links` | Wenn es um Fundstellenglattzieher / Zitatenkorrektor in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kanzlei-prozesse-abbilden` | Wenn es um Kanzlei-Prozesse abbilden in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kanzlei-quellenkarte` | Wenn es um Kanzlei Quellenkarte in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `kanzleiumgebung-khub-sonderfall-livecheck` | Wenn es um Kanzleiumgebung: Verhandlung, Vergleich und Eskalation in Kanzlei-Builder-Hub geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `khub-kanzlei-coi-onboarding-bauleiter` | Wenn es um Khub: COI-Konfliktmatrix in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `khub-kanzlei-onboarding-bauleiter` | Wenn es um Khub: Kanzlei-Onboarding Bauleiter in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `khub-leistungsmatrix-mandanten-checkliste` | Wenn es um Khub: Leistungsmatrix in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `khub-mandantenkonferenz-paralegal-rollen` | Wenn es um Khub: Mandantenkonferenz-Templates in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `khub-sonderfall-und-edge-case` | Wenn es um Khub: Sonderfall und Edge-Case-Prüfung in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `leistungsmatrix-fristennotiz-und-naechster-schritt` | Wenn es um Leistungsmatrix: Fristennotiz und nächster Schritt in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `livecheck-mehrparteien-konflikt-und-interessen` | Wenn es um Livecheck: Mehrparteienkonflikt und Interessenmatrix in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-waehlen` | Wenn es um Output wählen in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `paralegal-rollen-automatisieren` | Wenn es um Paralegal-Aufgaben automatisieren in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `playbook-aus-eigenen-daten` | Wenn es um Skill: Playbook aus eigenen Daten in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `playbook-qualitaetspruefung-beweislast-review` | Wenn es um Playbook: Internationaler Bezug und Schnittstellen in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `qa-kanzleiweit-templating-praxis-verwalter` | Wenn es um Skill-QA kanzleiweit in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `qualitaetspruefung-beweislast-und-darlegungslast` | Wenn es um Qualitaetspruefung: Beweislast, Darlegungslast und Substantiierung in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `qualitaetspruefung-builder-daten-red-team-korrektur` | Wenn es um Skills-QA in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `rechtsquellen` | Wenn es um Rechtsquellen: Compliance-Dokumentation und Aktenvermerk in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rentier-rechtsanwalt-spezial` | Wenn es um Einzelanwalt-Spezial in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `review-risikoampel-und-gegenargumente` | Wenn es um Review: Risikoampel, Gegenargumente und Verteidigungslinien in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `security-installation` | Wenn es um Security: Dokumentenmatrix, Lückenliste und Nachforderung in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `skill-installation-security-gate` | Wenn es um Skill-Installation mit Security-, Herkunfts- und Mandatsgeheimnis-Gate in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... |
| `skill-installierer` | Wenn es um Skill-Installer in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `skill-templating-praxis` | Wenn es um Skill-Templating Praxis in Kanzlei-Builder-Hub geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `skill-verwalter` | Wenn es um Skill-Manager in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-kanzlei-livequellen-und-rechtsprechungscheck` | Wenn es um Kanzlei: Livequellen- und Rechtsprechungscheck in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `uebersicht-einsteiger-deaktivieren` | Wenn es um Builder: Übersicht Einsteiger in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verwandte-skills-vorschlag` | Wenn es um /verwandte-skills-vorschlag — Verwandte-Skills-Empfehlung in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verzeichnis-durchsuchen` | Wenn es um /verzeichnis-durchsuchen — Skill-Registry-Browser in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-anschluss-skills-router` | Wenn es um Anschluss-Skills Router in Kanzlei-Builder-Hub geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Kanzlei-Builder-Hub geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-mandantenkommunikation` | Wenn es um Mandantenkommunikation in Kanzlei-Builder-Hub geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Kanzlei-Builder-Hub geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Kanzlei-Builder-Hub geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
