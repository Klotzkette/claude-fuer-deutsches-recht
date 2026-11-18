# Prüfung offener Beitragsanfragen

Am 18. November 2026 wurden neben den Pull Requests sämtliche zwölf offenen Issues gelesen. Die Ausgangsbasis war Main-Commit `e458e111f94ce0bcd9788e192beeb61a81d20812`. Es lagen keine offenen Pull Requests vor; GitHub Discussions waren deaktiviert. Die Vorschläge wurden als Prüfhinweise behandelt. Es wurden keine fremden Patches, Commits oder Textfassungen übernommen.

| Anfrage | Ergebnis und eigene Bearbeitung |
|---|---|
| [515](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/515) | Der Schreibfehler bei Hilfe und unbekannten Argumenten ist behoben und regressionsgeprüft. Ein echter `--check`-Modus ist weiterhin ausdrücklich nicht vorgesehen. |
| [516](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/516) | Eigenständiges vollständiges Jugendmedienschutz-Plugin mit zehn Skills, Werkstatt, Mini-Prompt und Wolkenwerft-Testakte. |
| [518](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/518) | Hauptworkflow und erster Spezialprüffall dürfen unterschiedliche Ziele haben. Die bestehende explizite Auswahlprüfung besteht zwölf Tests. |
| [519](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/519) | Aktive Hashbindungen und Abschlussketten nachgeprüft. Die ursprünglichen 27 Angaben sind in 31 historischen Einträgen nachvollziehbar erhalten; keine offene Nachprüfung. |
| [536](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/536) | § 4j EStG nur für einschlägige Altjahre und fünfjährige Höchstgeltung der Freistellungsbescheinigung bereits korrekt. |
| [537](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/537) | Softwarevergütung wird bereits anhand tatsächlich eingeräumter Rechte eingeordnet, nicht nach Vertriebsbezeichnungen. |
| [538](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/538) | Das Verfahren ist bereits zutreffend § 50c EStG zugeordnet. |
| [546](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/546) | Anbieterwechsel bereits zutreffend Kapitel VI, Art. 23 ff. Data Act zugeordnet. |
| [547](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/547) | Getrennte CRA-Meldepfade bereits richtig. Weitere Präzisierungen zu risikobezogener Abhilfe, Support und Richtlinien eigenständig ergänzt. |
| [548](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/548) | Vier verbliebene allgemeine AGB-Vertiefungen vollständig fachspezifisch überarbeitet; aktuelle unverbindliche Data-Act-Vertragsmuster eingeordnet. |
| [550](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/550) | Art. 25 und GPAI bereits getrennt; Anbieterdefinition nach Art. 3 Abs. 3 konkretisiert. |
| [613](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/613) | Geschenkgrenze, Reise- und Verpflegungszuordnung sowie Bewirtung bereits korrigiert und nachkontrolliert. |

## 1. Nachweise und Grenzen

[Jugendmedienrecht](jugendmedien.md), [KI, Daten und AGB](ki-daten.md), [Steuerrecht](steuer.md), [Technische Prüfungen](technik.md). Die Einzelberichte unterscheiden gelesene Volltexte, amtliche Erläuterungen, Ersatzabrufe und verbleibende Grenzen. Historische Abschlussberichte werden nicht als neue vollständige Rechtsrecherche ausgegeben.

Die Marktübersichten führen 312 Plugins und 3163 aktive Skills. Die unveränderte Zählerkorrektur von 311 auf 312 in bestehenden Plugin-Einstiegen ist in [navigation.json](navigation.json) mit Vorher-/Nachher-Hashes belegt. Alle Testakten bleiben erhalten. Die neue Testakte ergänzt den Bestand.

Die automatisierten Paket- und Regressionstests prüfen Dateien, Verweise, Prüfsummen und Trennung der Aktenstufen. Sie sind kein Nachweis einer behördlichen Anerkennung und kein beobachteter juristischer Modell-Pass. Veröffentlichungs- und Downloadprüfung werden gesondert protokolliert.

## 2. Vorbestehender Prüfungsfehler

Der vollständige Release-Testlauf fand bei `test-vergaberecht-module-routing.py` zwei veraltete Rückführungsnachweise. Die betroffenen Gesamtprompts für Bieter und Vergabestelle waren bereits auf dem unveränderten Ausgangs-Main anders als im historischen Nachweis; die Inhalte wurden in dieser Runde nicht verändert. Die historische Fassung vor Commit `76b7d5c31f0fa286b94175696b4594d29a8ce931` wurde über ihren gespeicherten Hash gefunden. Aus ihr wurde mit dem vorhandenen inversen Änderungsverfahren das ursprüngliche Dokument rekonstruiert. Der neue Nachweis bindet die heutige Fassung und stellt weiterhin exakt dieselben ursprünglichen Bytes wieder her. Originalhashes und ursprüngliche Texte bleiben erhalten; der Test wurde nicht abgeschwächt.

## 3. Technischer Abschluss

Der [lokale Prüfplan](checks.json) dokumentiert 41 bestandene Prüfkommandos und die zwölf zusätzlichen Paket-/Aktenregressionen. Die Akte umfasst 34 Originale in drei getrennten Stufen und eine separate Lesefassung mit 47 Seiten. Word-Dokumente wurden tatsächlich gerendert, alle Seiten gesichtet und die eingebetteten Times-New-Roman-Schriften geprüft. Eine Regression weist die beim ersten Rendering gefundene Ersatzschrift ausdrücklich zurück. Das native Archiv enthält keine Gesamt-PDF und keine Musterlösung.
