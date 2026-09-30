# 1. Insolvenzrecht und neu hinzugekommener Bestand

## 1.1. Gezielter zweiter Abgleich

Ausgangsstand `b21e767b` (256 Plugins, v445.19.1). Im ersten Durchgang mit PR #465 überprüfte Entscheidungen werden nicht als neue Prüfung gezählt. Dieser Nachtrag betrifft vier Insolvenz-/Planungsplugins und einen gezielten Kontrollpunkt des neu hinzugekommenen Dieselplugins. Die Quellen wurden am 30.09.2026 direkt vom BGH geladen und mit pypdf ausgelesen. Abruf-URLs, Umfang und SHA-256 stehen in [insolvenz-abrufe.json](insolvenz-abrufe.json).

## 1.2. Konkrete Anker

| Entscheidung | Tatsächlich gelesen | Einordnung |
| --- | --- | --- |
| [BGH, Beschluss vom 23.04.2026 – IX ZB 18/25](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZB__18-25.pdf?__blob=publicationFile&v=1) | Gesamter 13-seitiger Volltext, insbesondere Rn. 10–24 | Regelhafte Aufhebung nach Insolvenzreifeanzeige, zwei Ermessensausnahmen und Nachweislast des Schuldners. Ein unsicherer Drittbeitrag und bloß fehlende Vorteile eines Insolvenzverfahrens genügen nicht. Gruppenbildung bleibt offen. Werkstatt, Mini und Verfahrenswahl-Skill der Planwerkstatt ergänzt. Die falsche pauschale Schutzschirmoption bei bereits eingetretener Zahlungsunfähigkeit korrigiert. |
| [BGH, Urteil vom 12.03.2026 – IX ZR 18/25](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZR__18-25.pdf?__blob=publicationFile&v=1) | Kopf, Leitsätze, Tenor/Sachverhalt sowie Rn. 21–39, besonders 24–32 und 36–38 | Drittmittel zählen nach tatsächlicher Verfügbarkeit, nicht allein nach Einklagbarkeit; konkrete Zahlungseinstellungsindizien und Wissensnähe des Prozessgegners. In Liquiditätsplanung und Insolvenzrecht einschließlich Hauptproblem und §-17-Skill ergänzt. Insolvenzverwaltung erhält den eigenständigen Anker zur Geldauflage nach § 153a StPO: unmittelbare gemeinnützige Empfängerin ist richtige Gegnerin, nicht automatisch die Landeskasse. Keine pauschale Anfechtbarkeit oder abschließende Insolvenzfeststellung behauptet. |
| [BGH, Urteil vom 18.06.2026 – VIa ZR 1559/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIa_ZS/2022/VIa_ZR_1559-22.pdf?__blob=publicationFile&v=1) | Gesamter sechsseitiger Volltext, insbesondere Rn. 6–8 | Im neu hinzugekommenen Dieselplugin vorhandenen elektronischen Einreichungsanker bestätigt. qES beziehungsweise einfache Signatur plus verantworteter sicherer Übermittlungsweg; bloßes Kanaletikett ersetzt Nachweis nicht. Keine Dateikorrektur nötig, keine Vollprüfung sämtlicher Dieselanker behauptet. |
| [BGH, Urteil vom 24.05.2005 – IX ZR 123/04](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2004/IX_ZR_123-04.pdf?__blob=publicationFile&v=1) | Bereits amtlich archiviertes PDF erneut auf S. 1–2 und 10 gelesen; historische Quellenkarte bleibt maßgeblich | Im §-17-Skill falsche automatische Insolvenzfeststellung bei jeder nach drei Wochen verbleibenden kleinen Lücke und ausnahmslos ab zehn Prozent entfernt. Ausnahmen beider Richtungen, Passiva II und vollständige Lückenformel eingearbeitet; Beispiel mit 7,8125 Prozent richtig eingeordnet. |

Zusätzlich amtlich gelesen: [§ 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html), [§ 32 StaRUG](https://www.gesetze-im-internet.de/starug/__32.html), [§ 33 StaRUG](https://www.gesetze-im-internet.de/starug/__33.html) und [§ 270d InsO](https://www.gesetze-im-internet.de/inso/__270d.html). Die vorhandene, am 28.09.2026 dokumentierte Quellenprüfung zu IX ZR 48/21 und II ZR 88/16 wird weiterverwendet, nicht als neue vollständige Recherche ausgegeben.

## 1.3. Workflow und Grenzen

Die neuen Entscheidungen verändern konkrete Arbeitsschritte: Zahlungseingänge belegen und Status fortschreiben; Drittfinanzierungsbedingungen in Route und Plantext übernehmen; Geldauflagen nach dem tatsächlichen Empfänger prüfen. Die bestehenden Rückfragen, Fortsetzung nach Antwort und vollständigen Arbeitsprodukte bleiben erhalten. Ein Indizienzählautomat, ein rechnerischer Schlusswert als alleinige Entwarnung und verbindliche Literaturzitate ohne Zugriff wurden im §-17-Skill entfernt.

Acht Werkstatt-/Mini-Prompts und ein Hauptproblem wurden angepasst, passende Profile und Prüfsummen nachgeführt. Keine Testakte gelöscht oder verändert, keine neuen Skills und keine neuen DOCX/PDF-Artefakte erstellt. Die Nachprüfung ist gezielt; sie bestätigt weder sämtliche Literaturstellen in Altdateien noch Vollständigkeit aller 2026-Entscheidungen. Technische Gesamtergebnisse stehen getrennt in pruefungen.json.

## 1.4. Unabhängiger Diff-Review

Ein zweiter Bearbeiter hat die neuen Insolvenz-Aussagen anhand der amtlichen Extrakte kontrolliert. Zwei Präzisierungen übernommen: tatsächlich verfügbare Drittmittel nicht an eine allgemeine Schriftform knüpfen; bei rechtshängiger Restrukturierung das Ruhen der Antragspflicht, unverzügliche Insolvenzreifeanzeige und Wiederaufleben nach Wirkungsverlust gemäß am 30.09.2026 amtlich gelesenem [§ 42 StaRUG](https://www.gesetze-im-internet.de/starug/__42.html) in Verfahrenswahl und beide Planprompts aufnehmen.
