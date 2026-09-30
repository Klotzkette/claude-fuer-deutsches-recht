# 1. Rechtsprechungsanker: zweiter Durchgang am 30.09.2026

## 1.1. Ergebnis und Umfang

Der automatische Bestandsabgleich erfasst **256 Plugins und 24.704 Markdown-Dateien** mit Skills, Referenzen und Promptfassungen. Danach wurden **17 Plugins** anhand konkreter zusätzlicher Quellen nachgeschärft, darunter **36 Werkstatt-, Mini- und Hauptproblem-Prompts**. Fachliche Korrekturen, Normberichtigungen und ihre Ableitungen sind in [aenderungen.json](aenderungen.json) aufgeführt. Der bisherige erste Durchgang bleibt unter [2026-09-30](../2026-09-30/) dokumentiert; er wurde als PR #465 auf main integriert.

Ausgangsstand dieses zweiten Durchgangs: `b21e767b` (v445.19.1). Seit der ersten Prüfung hinzugekommen ist `diesel-schadensersatz`; dort wurde der 2026-Anker VIa ZR 1559/22 gezielt bestätigt. Keine pauschale Neubewertung sämtlicher Dieselquellen.

Die vier Fachberichte dokumentieren zusammen 16 Entscheidungen mit Entscheidungsdatum 2026 sowie drei gezielt erneut gelesene ältere Entscheidungen. Diese Zahl bezeichnet überprüfte Entscheidungen, nicht 16 erstmals im gesamten Repository auftauchende Aktenzeichen. Jeder Bericht benennt gelesene Passage, amtliche Quelle, Anwendung und Grenze. Wo kein sachlich passender neuer Anker festgestellt wurde, wurde kein beliebiges 2026-Urteil eingefügt.

## 1.2. Fachliche Änderungen

| Fachbereich | Konkrete Punkte | Nachweis |
| --- | --- | --- |
| Notariat, Erbrecht, Gesellschaft | Vorsorgeregisterauftrag und Gebühren, Auslandsnotar in Deutschland, Beschwer bei Pflichtteilsauskunft, Managementbeteiligung; alte Verwahrungs-/Geschäftsstellennormen berichtigt | [Fachbericht](notariat-erbe-gesellschaft.md) |
| Vertrag, AGB, Verbraucher, Versicherung | Auslegung einer anwaltlichen Rückabwicklungserklärung, kein freies Gesamtnichtigkeitswahlrecht, Kasko-Werkstattrisiko, PKV-Beweislast und konkrete Leckageausschlussklausel | [Fachbericht](vertraege-versicherung.md) |
| Verwaltung, Migration, Vergabe, Verwaltungsgericht | Tatsächliche Anhörung, Reiseausweis und Aufenthaltstitel, Passersatzmitwirkung, Inhouse über 80 Prozent, echte öffentliche Kooperation und passender Eilrechtsschutztenor | [Fachbericht](verwaltung-migration-vergabe.md) |
| Insolvenz, Liquiditätsplanung, StaRUG | Tatsächlich verfügbare Drittmittel, Zahlungseinstellung ohne Indizienzählung, Zehnprozent-Ausnahmen und Passiva II, Geldauflagenempfänger sowie Fortsetzung rechtshängiger Restrukturierung bei Insolvenzreife | [Fachbericht](insolvenz-und-neuer-bestand.md) |

Die Anker stehen an den passenden Bearbeitungsschritten und ändern konkrete Belegfragen, Berechnungen oder Entwürfe. Thematisch anders gelagerte Hauptproblem-Prompts, etwa zur Berufsunfähigkeit, erhielten keine sachfremden Urteile. Bestehende Quellenprüfdaten bleiben erhalten; gezielte Nachträge tragen ein eigenes Prüfdatum. Keine pauschale Umstellung alter Profile auf „alles am 30.09.2026 verifiziert“.

## 1.3. Technische Nachführung

Prompthashes, generierte Vollprüfungen, Skill-Indizes und betroffene README-Tabellen wurden nachgeführt. Bestehende Prüfungen decken Profilkonsistenz, Struktur, Import, Rechtsstands-Fehlermuster, Mini-Nutzung, Promptabläufe, Navigation und Testakten-PDFs ab. Die konkreten Befehle, Exitcodes und Ausgabeprüfsummen stehen in [pruefungen.json](pruefungen.json). Lokale Plugin-ZIPs und Markdown-Bündel werden getrennt nach dem Release-Rezept geprüft; ein erfolgreicher lokaler Paketbau bedeutet keine neue öffentliche Release-Veröffentlichung.

Keine Fallakte gelöscht, keine Skillzahl erhöht, keine Versionsnummer angehoben. Der Inhalt wird auf main integriert; die öffentliche Release-Version bleibt von diesem Commit getrennt.

## 1.4. Reichweite

Der repositoryweite automatische Abgleich ist **keine vollständige juristische Einzelprüfung aller Dateien**. Rechtsprechungserkennung ist heuristisch; Aktenzeichen allein beweisen weder Jahr noch Aussage. Die materielle Nachprüfung umfasst die ausdrücklich dokumentierten Stellen und Entscheidungen. Nicht genannte Altquellen, Literatur und sämtliche seitdem erschienenen Entscheidungen sind damit nicht pauschal bestätigt. Es wurden keine neuen statistischen Live-Modelltests durchgeführt.
