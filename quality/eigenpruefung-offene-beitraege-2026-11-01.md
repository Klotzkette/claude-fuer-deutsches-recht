# 1. Eigenprüfung offener Beiträge

Geprüft am 1. November 2026, ausgehend von `main` mit Commit `8c9cf33ef3e6c8c7fafcc92ab1c5aa15863d6277`. Die sechs offenen externen Pull Requests wurden als Hinweise geprüft, ihre Branches, Patches und Commits nicht übernommen. Berechtigte Korrekturen wurden auf dem aktuellen Quellstand eigenständig formuliert. Weil der ausdrücklich angesprochene AI-Act-Hinweis als Issue vorliegt, wurden auch die zugehörigen offenen Fehlerberichte eingeordnet.

## 1.1. Offene Pull Requests

| Beitrag | Eigene Bewertung | Entscheidung und Umsetzung |
| --- | --- | --- |
| [PR 614](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/614) | Geschenkegrenze und Normbezeichnung sind tatsächlich veraltet beziehungsweise falsch. Ein Quellen-Sperrmuster nur bei Releases kommt für PR-Rückfälle zu spät. | Geschenkeprüfung mit Wirtschaftsjahrgrenze, Freigrenzenwirkung und Altjahren neu formuliert; Arbeitgeber-Reisekostenbefreiung richtig zugeordnet. Die verlinkten Reisekostenbefunde aus Issue 613 mit geprüft. Eigenständige Rückfalltests und lesender PR-/Main-Workflow, keine Übernahme der vorgeschlagenen Implementierung. |
| [PR 602](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/602) | Gesetzesname und DAC8-Erstmeldung waren falsch. | KStTG, Beginn, Meldegegenstand und jährliche Regelfrist eigenständig korrigiert. Unmittelbar verbundene Bußgeld-, Ausnahme- und Selbstanzeigeaussagen präzisiert. Samstag/Feiertag bei der konkreten Fristberechnung ausdrücklich gesondert prüfen. |
| [PR 549](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/549) | Softwarezahlungen lassen sich steuerlich nicht zuverlässig nach Standard-/Individualsoftware oder bloßer Vertragsbezeichnung einordnen. | Tatsächlich eingeräumte Rechte, bloße Nutzung, Verwertung und endgültigen wirtschaftlichen Erwerb getrennt. Unmittelbaren Zahlungsrichtungsfehler im Israel-Beispiel berichtigt. |
| [PR 545](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/545) | Entlastungsverfahren und Missbrauchsprüfung wurden verwechselt; ein UrhG-Kürzel war falsch. | Freistellung und Erstattung nach Paragraf 50c EStG von Paragraf 50d Absatz 3 getrennt; Abzugstatbestand und Steuersatz präzisiert; UrhG-Verweis korrigiert. Zugehörige Vollprüfung gezielt aus eigenen Quellen regeneriert. |
| [PR 543](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/543) | Die Lizenzschranke war als aktuelle Prüfung geführt; die Freistellungslaufzeit war veraltet. | Paragraf 4j EStG a.F. nur für Altjahre bis VZ 2024, damalige Voraussetzungen und Schwellen gesondert. Höchstdauer nach Paragraf 50c auf fünf Jahre, nicht automatische Laufzeit. |
| [PR 517](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/517) | Zentraler Hausstil hat Wartungsnutzen. Der Vorschlag betrifft aber 5333 Dateien und ändert die verbindliche Grundschriftregel zugunsten eines zusätzlichen Profilmodells. | Keine Hausstil-Migration, kein neues Konfigurationssystem und kein Versionssprung. Die bestehende Regel erlaubt begründete amtliche und mandantenbezogene Layoutausnahmen bereits. Verwandte, reproduzierbare Prüflücken aus Issues 518/519 eigenständig behandelt. Keine vollständige manuelle Prüfung aller 5333 Dateien behauptet. |
| [PR 598](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/598) | Eigener älterer PR von Klotzkette; kein externer Fehlerhinweis. Alle 502 PR-Dateien sind auf main vorhanden, 149 unverändert, 353 fortentwickelt. 127 ursprüngliche Testdateien stimmen überein. | Keine Übernahme. Das heutige Plugin ist bereits weiterentwickelt. Keine Schließung oder Nachricht im eigenen PR veranlasst. |

Die externen Pull Requests werden nicht gemerged oder geschlossen. Die vom Nutzer beauftragte Antwort darauf lautet ausschließlich: „Ja, vielen Dank.“

## 1.2. Weitere Fehlerberichte

| Beitrag | Ergebnis am aktuellen Quellstand |
| --- | --- |
| [Issue 550](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/550) | Die materiellen Hinweise zu Artikel 25 KI-VO waren im aktuellen Hauptskill bereits umgesetzt: drei Fälle in Absatz 1, Produkthersteller in Absatz 3, Hochrisikobedingung und gesonderte Modellrolle. Die amtlichen Artikel 3 und 25 wurden erneut gegengelesen. Verbliebene alte interne Namen des Produkthersteller-Skills in Routingtexten und README eigenständig berichtigt. |
| [Issue 548](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/548) | Der fehlende Fachkern der bezeichneten Digitaldienste-Skills bestätigt sich. Fünf AGB-Skills eigenständig mit unterschiedlichen Arbeitswegen überarbeitet: SaaS, Cloud/Hosting, Export, KI-Service und KI-Output. Data-Act-Anwendungsbereich, Wechselvertrag, Entgelte und Ausnahmen sowie KI-Zweckbestimmung, Rollen und Transparenz ergänzt. Keine pauschale Rechtsfreigabe oder Neufassung aller 273 AGB-Skills behauptet. |
| [Issue 547](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/547) | CRA-Meldefristen waren vermischt. Drei Robotik-Skills trennen jetzt aktiv ausgenutzte Schwachstellen und schwerwiegende Vorfälle. Abschlussfrist und Auslöser sind unterschiedlich; der Zwischenbericht ist keine feste 72-Stunden-Meldung. Frühwarnbeispiel und Pflichtangaben passend neu formuliert. |
| [Issue 546](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/546) | Cloud-Wechsel wurde fälschlich Artikel 17 Data Act zugeordnet. Drei Datenbank-Skills neu gefasst; Kapitel VI, Entgelte, Altverträge, Artikel 43 und Geheimnisschutz sauber getrennt. Weitere pauschale Aussagen zu Backup, Auftragsverarbeitung und Betroffenenportabilität im selben Arbeitsweg präzisiert. Einen gleichartigen Nebenverweis in der Beweissicherung korrigiert. |
| [Issues 536–538](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/536), [613](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/613) | Fachliche Ausgangshinweise der obigen Steuer-PRs. Dieselben Stellen und eng verbundene Folgefehler wurden eigenständig bearbeitet, keine doppelte Implementierung. |
| [Issue 519](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/519) | Bestätigt: 31 zusätzliche Hashangaben in vier Profilen waren nicht mehr aktuell und wurden bisher nicht validiert. Aktive Hashfelder werden jetzt tatsächlich geprüft. Die alten Werte bleiben als historische Prüffassung erhalten. Vier Profile sind ausdrücklich `needs_review`; neue Ergebnisläufe bleiben bis zur dokumentierten Nachprüfung gesperrt. Keine Prüfsumme blind aktualisiert. |
| [Issue 518](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/518) | Die beanstandete Gleichsetzung von Schwerpunkt und erstem Prüffall war im heutigen Test schon behoben. Die konkrete Zielskill-/Schwerpunktbindung und die zugehörigen Vertragsregressionen laufen jetzt auch im PR-Workflow. |
| [Issue 515](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/515) | Unausgewertete Schalter konnten schreibende Generatoren starten. Hilfe und ungültige Argumente werden vor Importen und schreibendem Einstieg abgefangen. Der argumentlose Arbeitsweg bleibt erhalten. `--check` wird ausdrücklich nicht unterstützt und bricht ohne Schreiben ab; ein echter Vergleichsmodus ist nicht Teil dieser Korrektur. |
| [Issue 516](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/516) | Wunsch nach weiteren Jugendschutz-/Medienrechts-Skills, kein Fehlernachweis zu einem vorhandenen Arbeitsweg. Kein neues Plugin allein aus diesem Fehlerprüfauftrag erstellt. |

## 1.3. Quellen und unabhängige Gegenprüfung

Die Steuerprüfung mit Altjahres-, Laufzeit- und Softwarequellen ist in der [fachlichen Quellenreferenz](../steuerrecht-anwalt-und-berater/references/lizenzzahlungen-software.md) dokumentiert. Für die Geschenk-/Reisekostenprüfung wurden insbesondere [Paragraf 4 EStG](https://www.gesetze-im-internet.de/estg/__4.html), [Paragraf 9 EStG](https://www.gesetze-im-internet.de/estg/__9.html), [Paragraf 52 EStG](https://www.gesetze-im-internet.de/estg/__52.html) und die dortigen zeitlichen Regeln gelesen. DAC8 beruht auf dem [KStTG](https://www.gesetze-im-internet.de/ksttg/BJNR1600B0025.html), insbesondere Paragrafen 9, 18 und 21; DAC7-Bußgelder auf [Paragraf 25 PStTG](https://www.gesetze-im-internet.de/psttg/__25.html). Verifizierte Spezialquellen und begrenzte Prüfstände stehen zusätzlich in den betroffenen Skills.

Für Cloud und KI stehen [Primärquellen und Normzuordnung](../agb-recht-pruefer/references/digitaldienste-data-act-ki.md) bereit. Die gegengeprüften Data-Act-Passagen betreffen insbesondere Artikel 2 Nummer 8, Artikel 4 bis 9, Kapitel VI, Artikel 43 und Artikel 50. Die [amtliche CRA-Fassung](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) unterscheidet in Artikel 14 Absatz 2 Buchstabe c die Abschlussmeldung nach Verfügbarkeit einer Maßnahme von der Monatsfrist nach Absatz 4 Buchstabe c; Absatz 6 betrifft angeforderte Zwischenberichte, Artikel 71 den Beginn.

Einige direkte EUR-Lex-Seiten zeigten die JavaScript-Prüfung. Für die bezeichneten Data-Act-/CRA-Passagen waren die vollständigen einschlägigen deutschen Normabschnitte als amtliche Suchausgabe zugänglich; für den AI Act wurden die Artikel zusätzlich im [offiziellen Kommissions-Explorer](https://ai-act-service-desk.ec.europa.eu/de/ai-act-explorer) gelesen. Keine durchgehend erfolgreiche direkte EUR-Lex-Volltextlektüre behauptet. BMF-/OECD-Zugriffsgrenzen sind in der Steuerreferenz benannt. Die acht neu gefassten Datenbank-/AGB-Skills wurden unabhängig gegengelesen; das dabei gefundene Zitierweise-Linkproblem wurde korrigiert.

## 1.4. Prüfgrenzen

Die Eigenprüfung belegt die bezeichneten Korrekturen und technischen Regressionen. Sie ist keine vollständige anwaltliche Endprüfung aller übrigen Aussagen der Sammlung, keine neue Client-Modellprobe und keine Bestätigung fremder Benutzerkonten. Bestehende Dokumenten- und Quellenprüfungen bleiben an ihre damaligen Fassungen gebunden. Versionsnummern und veröffentlichte ZIP-Assets werden durch diese Quellkorrektur nicht als neu gebaut ausgegeben.

Der vollständige Schwerpunktcheck weist daneben 14 bestehende, von dieser Änderung unabhängige Download-/Zitierregelbefunde auf. Die für Issue 518 relevante Bindung und ihre Regressionen sind separat geprüft. Bereits bekannte Testakten-Downloadbefunde aus der vorigen README-Prüfung werden durch diesen Lauf nicht als erledigt ausgegeben.

## 1.5. Validierung der eigenen Änderungen

- Marketplace-Import: 310 Plugins und 23385 Skills, erfolgreich.
- YAML-Frontmatter und Pluginstruktur einschließlich lokaler Dateiverweise: erfolgreich.
- Bestandsübersicht: 310 Plugins, 308 Werkstatt- und 307 Mini-Prompts, 553 zentrale beziehungsweise 566 Testakten gesamt, erfolgreich.
- Markdown-Struktur sämtlicher 51 geänderten oder hinzugefügten Markdown-Dateien: keine Fehler.
- Quellen-Sperrmuster: 31148 Markdown-Dateien mit 230 Mustern, ohne Treffer. Die sechs zusätzlichen Kontrollen enthalten positive Fehlerbeispiele und zulässige Abgrenzungsbeispiele.
- Qualitätslabor: 73 Tests und Audit aller 310 Profile erfolgreich. Vier Profile bleiben ausdrücklich `needs_review`, also keine Freigabe der aktuellen ungeprüften Dateistände.
- Schwerpunkt-/Zielskillbindung: sechs gezielte Prüfungen erfolgreich.
- Erhaltung von Prompt-Arbeitswegen: 43 Regressionen erfolgreich; Megaprompt-Abgleich erfolgreich.
- Navigation: 51 bestehende Regressionen erfolgreich.
- Generator-CLI: zwei Tests mit 114 isolierten Hilfe-/Fehlerschalteraufrufen ohne Inhaltsänderung und einer argumentlosen Schreibprobe erfolgreich.
- Gesamt-PDF-Regeln: alle 553 zentralen Testakten erfolgreich.
- `git diff --check`: ohne Fehler.
