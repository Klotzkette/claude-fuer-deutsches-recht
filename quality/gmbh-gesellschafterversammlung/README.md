# 1. Tatsächliche Probeläufe des Gesellschafterversammlungs-Organisators

## 1.1. Durchführung und Reichweite

Am 29.09.2026 bearbeiteten drei getrennte Agenten mit eigenem Gesprächskontext jeweils einen fiktiven Nutzerauftrag. Sie erhielten den jeweiligen Skill beziehungsweise Standalone-Prompt und den Rohauftrag, aber keine erwartete Antwort, kein Bewertungsraster und keine Ergebnisse anderer Läufe. Amtliche Quellenrecherche war erlaubt. Der Hauptskill-Lauf durfte die verknüpften Fachskills/Referenzen verwenden; die beiden anderen Läufe erhielten ausschließlich ihren jeweiligen Prompt. Die Ergebnisse entstanden als Markdown; es wurde nichts versandt, beurkundet oder angemeldet.

Dies sind begrenzte beobachtete Probeläufe in der Entwicklungsumgebung. Sie belegen weder automatische Skill-Auswahl in einem anderen Client noch eine erfolgreiche Installation in einem fremden Konto, eine vollständige Fehlerfreiheit aller Rechtsfragen oder die visuelle Qualität einer Word-/PDF-Ausgabe. Im Werkstatt-Lauf fällt eine zusätzliche vorsorgliche Nachfrage zur bereits mitgeteilten Organstellung Bertas auf; die Ausgabe bleibt dadurch verwendbar, ist aber kein Beleg für einen in jedem Detail minimalen Fragenumfang. Die sechs Aufträge im allgemeinen Evaluationsprofil sind davon getrennt und wurden nicht sämtlich als Modelllauf ausgeführt.

## 1.2. Aufträge, Ergebnisse und geprüfte Beobachtungen

| Zugang | Unverdeckter Auftrag und tatsächliches Ergebnis | Nachprüfung |
| --- | --- | --- |
| Hauptproblem-Skill | [Auftrag](hauptskill-auftrag.md), [Ergebnis](hauptskill-ergebnis.md), [Laufnotiz](hauptskill-laufnotiz.md) | Die beiden Gesellschaften bleiben getrennte Einladungsadressaten. Der E-Mail-Nachtrag heilt die fehlende Erstladung nicht. Es entstehen eine Absage und eine neue Einladung; unbekannte TOP und Stammdaten werden sichtbar offengelassen. Der neue Termin ist ein bedingter Planungsvorschlag. |
| Mini-Prompt | [Auftrag](mini-auftrag.md), [Ergebnis](mini-ergebnis.md), [Laufnotiz](mini-laufnotiz.md) | Fehlendes Format-Einverständnis wird erkannt. Eine Präsenzfassung und ein ausdrücklich austauschbarer notarieller TOP werden formuliert. Der beratende Ersatz wird als vorläufige Option gekennzeichnet; zur tatsächlichen Beschlussfassung braucht es die Klärung des Notartermins. Private PDF-Datei und formgerechte Anmeldung werden getrennt. |
| Werkstatt | [Auftrag](workshop-auftrag.md), [Ergebnis](workshop-ergebnis.md), [Laufnotiz](workshop-laufnotiz.md) | Keine vorweggenommene Einstimmigkeit oder ungeprüft sichere Stimmsperre. Die Varianten 10.000/25.000 und 10.000/10.000 sind richtig. Organamt und Vertrag erhalten getrennte Anträge; die sofort zu klärende Kündigungsfrist nach § 626 BGB wird vor dem Oktobertermin hervorgehoben. |

## 1.3. Technische Prüfung getrennt von der Modellbeobachtung

Der Stimmenprüfer besteht 13 Python-Tests mit mehreren Eingabe-Unterfällen: exakte Schwellen, Gleichstand, alternative Nenner, Ausschlussvarianten, Nullbasis, skalierte Gewichte und CLI-Fehler. Vier gesonderte Regressionstests prüfen optionale Codex-Manifeste mit fehlenden beziehungsweise abweichenden Namen/Versionen. Die sechs Skill-Dateien bestehen die Skill-Frontmatterprüfung. Marketplace-, Struktur-, Laufzeit- und Quellen-Sperrmusterprüfungen sind zusätzliche technische Kontrollen, keine rechtliche Ergebnisbewertung.

Die Quellenkarten beruhen auf der gesonderten amtlichen Recherche; die Laufnotizen geben die tatsächlich erneuten Zugriffe der ausführenden Agenten wieder. Gelesene Satzungsdateien oder echte Versammlungsereignisse werden nicht behauptet: Die Sachverhalte waren jeweils im Auftrag beschrieben. Alle Namen, Firmen, Anschriften und Vorgänge der drei Testaufträge sind fiktiv.

## 1.4. Reproduzierbarer Stand

[Dateimanifest](dateimanifest.json) hält die geprüften Prompt-, Skill- und Ergebnisdateien per SHA-256 fest. Die Ausgabeinhalte wurden ohne inhaltliche Änderungen übernommen. Markdown-Zeilenumbrüche mit nachgestellten Leerzeichen wurden gleichwertig als Backslash-Zeilenumbrüche dargestellt. Lokale absolute Verzeichnisse in den Laufnotizen sind für die Veröffentlichung ersetzt. Eine spätere Änderung eines Prompts ist kein neuer Probelauf.
