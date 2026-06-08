# Kanzlei-Builder-Hub

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kanzlei-builder-hub`) | [`kanzlei-builder-hub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kanzleigründung Eckermann Friedrich Sandhof Rechtsanwaltsgesellschaft mbH — Aachen** (`kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen`) | [Gesamt-PDF lesen](../testakten/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen/gesamt-pdf/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen_gesamt.pdf) | [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anpassen` | Kanzlei-Builder-Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows. Normen: technisch/intern. Prüfraster: Anpassungsumfang, Kompatibilitaet, Testbedarf. Output: Anpassungs-Konfigurationsdokument. Abgren... |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Kanzlei Builder Hub-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dok... |
| `automatischer-aktualisierer` | Plugins und Skills in der KI-Anwaltskanzlei automatisch aktualisieren: neue Norm-Versionen, Rechtsprechungsaenderungen. Normen: technisch/intern. Prüfraster: aeltere Versionen identifizieren, Update-Prioritaet, Rollback-Option. Output: A... |
| `builder-zahlen-schwellen-und-berechnung` | Builder: Zahlen, Schwellenwerte und Berechnung im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `community-leistungsmatrix-fristennotiz` | Community: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `daten-red-team-und-qualitaetskontrolle` | Daten: Red-Team und Qualitätskontrolle im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `deaktivieren` | Einzelne Skills oder Plugins temporaer deaktivieren ohne Deinstallation. Normen: technisch/intern. Prüfraster: Abhaengigkeiten, Deaktivierungsumfang, Reaktivierungsweg. Output: Deaktivierungsbestätigung. Abgrenzung: nicht vollständige De... |
| `deinstallieren` | Plugins oder Skills vollständig deinstallieren: Abhaengigkeitsprüfung, Datensicherung. Normen: technisch/intern. Prüfraster: Abhaengigkeitscheck, Datensicherung vor Löschung, Bestätigung. Output: Deinstallationsprotokoll. Abgrenzung: nic... |
| `deployment-eigenen-einsteiger` | Deployment: Schriftsatz-, Brief- und Memo-Bausteine im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `dokumente-intake` | Dokumentenintake für Kanzlei-Builder-Hub (Plugins/Skills): sortiert Plugin-Konfiguration, Skill-Definitionen, Mandanten-AVV, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis... |
| `eigenen-formular-portal-und-einreichung` | Eigenen: Formular, Portal und Einreichungslogik im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `einsteiger-mandantenkommunikation-entscheidungsvorlage` | Einsteiger: Mandantenkommunikation und Entscheidungsvorlage im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `einstieg-routing` | Einstieg, Triage und Routing für Kanzlei-Builder-Hub (Plugins/Skills): ordnet Rolle (Kanzleiinhaber, IT-Verantwortlicher, Mitarbeitende), markiert Frist (keine harten Fristen), wählt Norm (BRAO § 43e KI-Einsatz, DSGVO, KI-VO) und Zuständ... |
| `findet-gate-installiert` | Findet: Erstprüfung, Rollenklärung und Mandatsziel im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `fristen-risikoampel-mandantenkommunikation` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Kanzlei Builder Hub. |
| `gate-behoerden-gericht-und-registerweg` | Gate: Behörden-, Gerichts- oder Registerweg im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `grosskanzlei-rollout-thema-prozesse-abbilden` | Grosskanzlei-Rollout: Pilotphase, Rollout-Welle, Trainings, Governance, Approval-für Skill-Eintraege, Audit-Trail, Datenschutz-Folgenabschaetzung. Mustertexte und Roadmap im Kanzlei Builder Hub. |
| `installiert-tatbestand-beweis-und-belege` | Installiert: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `kaltstart-interview` | Kaltstart-Interview für den Kanzlei-Builder-Hub: Kanzleiprofil, Rechtsgebiete, gewuenschte Plugins. Normen: technisch/intern. Prüfraster: Rechtsgebietsabdeckung, Mandantenstruktur, Technikvoraussetzungen. Output: Kanzlei-Profil-Konfigura... |
| `kanzlei-fundstellencheck-zitate-links` | Normen- und Rechtsprechungszitate in Schriftsätzen, Memos und Skills vereinheitlichen. Setzt die Zitierweise v4.1 durch: keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur mit Datum, Aktenzeichen und verifizie... |
| `kanzlei-prozesse-abbilden` | Typische Kanzlei-Prozesse mit Plugins und Skills abbilden: Mandatsaufnahme, Akteneinsicht, Schriftsatzentwurf, Fristenkontrolle, Rechnung, Archivierung. Pro Prozess: Welche Plugins (Skills) helfen, in welcher Reihenfolge, mit welchem Out... |
| `kanzlei-quellenkarte` | Kanzlei Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `kanzleiumgebung-khub-sonderfall-livecheck` | Kanzleiumgebung: Verhandlung, Vergleich und Eskalation im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `khub-kanzlei-coi-onboarding-bauleiter` | Spezialfall Conflicts-of-Interest-Matrix in Boutique- und Grosskanzleien: Datenbank, Pruefablauf, Chinese Walls, Informationsabschirmung. Pruefraster für Risk-and-Compliance im Kanzlei Builder Hub. |
| `khub-kanzlei-onboarding-bauleiter` | Bauleiter Onboarding neuer Anwaelte und Mitarbeitenden: Rollenmatrix, Mandatsfreigabe, IT-Setup, Berufsrecht-Briefing, Probezeit-Plan. Pruefraster für Kanzlei-Manager im Kanzlei Builder Hub. |
| `khub-leistungsmatrix-mandanten-checkliste` | Checkliste Leistungsmatrix Mandanten: Standardleistungen, Premium, Pauschale, Stundenhonorar, Erfolgskomponenten. Pruefraster Honorarvereinbarung pro Mandantensegment im Kanzlei Builder Hub. |
| `khub-mandantenkonferenz-paralegal-rollen` | Spezialfall Mandantenkonferenz- und Lenkungsgremien-Templates für Grossmandate: Tagesordnung, Protokoll, Action Items, Status-Reporting. Pruefraster für Konfliktpotenzial im Kanzlei Builder Hub. |
| `khub-sonderfall-und-edge-case` | Khub: Sonderfall und Edge-Case-Prüfung im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `leistungsmatrix-fristennotiz-und-naechster-schritt` | Leistungsmatrix: Fristennotiz und nächster Schritt im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `livecheck-mehrparteien-konflikt-und-interessen` | Livecheck: Mehrparteienkonflikt und Interessenmatrix im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `output-waehlen` | Output-Wahl für Kanzlei-Builder-Hub (Plugins/Skills): stimmt Adressat (Kanzleiinhaber, IT-Verantwortlicher, Mitarbeitende), Frist (keine harten Fristen) und Form auf den Zweck ab — typische Outputs: Plugin-Skizze, Skill-Entwurf, Validier... |
| `paralegal-rollen-automatisieren` | Spezialfall paralegale Routineaufgaben automatisieren: Aktenneuanlage, Erstkontakt, Standardanschreiben, Vorlagepruefung, Vorbescheidung. Welche Skills wie kombinieren, Datenschutz beachten, Vertraulichkeit, Pflicht zur Plausibilitaetsko... |
| `playbook-aus-eigenen-daten` | Kanzleieigenes Playbook aus vorhandenen Musterdokumenten und Vorlagen automatisch erstellen. Normen: technisch/intern, BRAO. Prüfraster: Dokumentenqualitaet, Kategorisierung, Normverankerung. Output: Kanzlei-Playbook aus eigenen Daten. A... |
| `playbook-qualitaetspruefung-beweislast-review` | Playbook: Internationaler Bezug und Schnittstellen im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `qa-kanzleiweit-templating-praxis-verwalter` | Skills kanzleiweit unter QA-Kontrolle halten: zentrale Skill-Bibliothek, Versionsverwaltung, Aenderungsfreigaben, Validatoren, Tests. Pruefraster für ausreichende Qualitaet bevor ein Skill in Produktion geht im Kanzlei Builder Hub. |
| `qualitaetspruefung-beweislast-und-darlegungslast` | Qualitaetspruefung: Beweislast, Darlegungslast und Substantiierung im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `qualitaetspruefung-builder-daten-red-team-korrektur` | Qualitaet installierter Skills prüfen: Normaktualitaet, Description-Qualitaet, Struktur-Compliance. Normen: technisch/intern, SKILL.md-Schema. Prüfraster: Description-Laenge, Normverankerung, Frontmatter-Vollständigkeit. Output: Qualitae... |
| `quellen-livecheck` | Quellen-Live-Check für Kanzlei-Builder-Hub (Plugins/Skills): prüft Normen (BRAO § 43e KI-Einsatz, DSGVO, KI-VO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt RAK und Quellenhygiene nach references/quellenhygiene... |
| `rechtsquellen` | Rechtsquellen: Quellenprüfung; Compliance-Dokumentation und Aktenvermerk: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rentier-rechtsanwalt-spezial` | Spezialnutzung für Einzelanwaeltinnen mit kleinem Backoffice: Welche Skills sparen am meisten Zeit, welche bringen Sichtbarkeit, welche reduzieren Routine. Top-10-Empfehlungen, Konfigurationsbeispiele, Sicherheits-Hinweise im Kanzlei Bui... |
| `review-risikoampel-und-gegenargumente` | Review: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `security-installation` | Security: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin kanzlei builder hub im Kanzlei Builder Hub. |
| `skill-installation-security-gate` | Skill-Installation mit Security-, Herkunfts- und Mandatsgeheimnis-Gate: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Kanzlei Builder Hub. |
| `skill-installierer` | Neue Skills in der KI-Anwaltskanzlei installieren: Verfuegbarkeitscheck, Abhaengigkeiten, Konfiguration. Normen: technisch/intern. Prüfraster: Kompatibilitaet, Abhaengigkeitsprüfung, Testlauf. Output: Installationsprotokoll neuer Skill.... |
| `skill-templating-praxis` | Skill-Templating für kanzleieigene Vorlagen: vom Schriftsatz-Bauplan zum eigenen Skill mit Platzhaltern, Pruefraster, Quellenregel. Konkrete Step-by-Step-Anleitung mit YAML-Frontmatter, Description-Regeln, Variablen-Erkennung, Ausgaberez... |
| `skill-verwalter` | Übersicht und Verwaltung aller installierten Skills: Status, Version, Abhaengigkeiten. Normen: technisch/intern. Prüfraster: aktive Skills, deaktivierte Skills, Update-Bedarf. Output: Skills-Verwaltungsuebersicht. Abgrenzung: nicht Einze... |
| `uebersicht-einsteiger-deaktivieren` | Einfuehrender Ueberblick für Einsteiger: Was kann der Kanzlei-Builder-Hub? Skills installieren, deaktivieren, deinstallieren, anpassen. Routet die wichtigsten Fragen an die passenden Sub-Skills. Mit Beispielszenarien aus dem Kanzleiallta... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Kanzlei-Builder-Hub (Plugins/Skills): trennt fehlende Tatsachen von fehlenden Belegen (Plugin-Konfiguration, Skill-Definitionen, Mandanten-AVV), nennt pro Lücke Beweisthema, Beschaffungsweg (RAK), Frist... |
| `verwandte-skills-vorschlag` | Verwandte Skills zu einem Mandat oder Rechtsproblem vorschlagen: Ergaenzungsempfehlungen. Normen: technisch/intern. Prüfraster: Rechtsgebiet, Verfahrensphase, Mandantentyp. Output: Vorschlagsliste verwandter Skills. Abgrenzung: nicht Kom... |
| `verzeichnis-durchsuchen` | Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen. Normen: technisch/intern. Prüfraster: Suchbegriff, Kategoriefilter, Ergebnispriorisierung. Output: Suchergebnisliste Skills. Abgrenzung: nicht Skill-Installation od... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Kanzlei Builder Hub. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Kanzlei Builder Hub. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Kanzlei Builder Hub. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Kanzlei Builder Hub. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
