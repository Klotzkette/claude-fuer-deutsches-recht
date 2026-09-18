# 1. Qualitätslabor für alle Plugins

Das [Prüfverzeichnis](../QUALITY.md) erfasst für jedes Marketplace-Plugin konkrete Auswahlfälle, einen fachlichen Arbeitsauftrag und mindestens drei Ergebniskriterien. Ein vorbereitetes Profil ist kein bestandener Modelltest. Die [Schwerpunkt-Prompts](../SCHWERPUNKTE.md) sind davon getrennte Arbeitsmittel für konkrete Mandatsprobleme.

## 1.1. Vier verschiedene Prüfaussagen

| Prüfung | Aussage | Keine Aussage über |
| --- | --- | --- |
| Strukturvalidator | Dateien, Namen, Verweise, Format und Paketgrenzen stimmen | tatsächliche Auswahl oder juristische Qualität |
| Individuelle Textprüfung | Der bezeichnete Mini-, Werkstatt- oder Schwerpunkttext wurde redaktionell geprüft | Ergebnisqualität in jedem Client |
| Beobachtete Auswahl | Ein konkreter Client hat bei einer konkreten Anfrage einen Skill gewählt oder nicht gewählt | Richtigkeit des erzeugten Dokuments |
| Ergebnisbewertung | Zwei unabhängige Prüfmodelle bewerten die tatsächlich erzeugten Dateien gegen fachliche Kriterien | unabhängige Rechtsquellenprüfung oder anwaltliche Freigabe |

Die Zustände `prepared`, `unreviewed`, `needs_review`, `failed` und `passed` werden getrennt geführt. Fehlende Zugänge, Dateien, Messungen, OCR oder unvollständige Prüfantworten dürfen kein positives Ergebnis erzeugen. Ein sauber beendeter Lauf kann fachlich falsch sein; ein perfekter Text kann technisch unvollständig ausgeliefert worden sein.

## 1.2. Einen isolierten Lauf vorbereiten

Profil und Fall-ID stehen in `quality/evals/<plugin>.json`. Dieser Ordner enthält Bewertungserwartungen und darf dem bearbeitenden System nicht als Fallmaterial zugänglich gemacht werden. Es entstehen keine neuen Lösungshinweise in den Übungsakten.

`mini_review.sha256` ist verpflichtend und enthält den SHA256-Fingerprint der endgültigen Mini-Datei als 64 kleine Hexadezimalzeichen, berechnet über die unveränderten Dateibytes einschließlich Zeilenenden. Fehlende, ungültige oder abweichende Fingerprints verhindern die Profilfreigabe und Vorbereitung neuer Läufe. Bestehende eingefrorene Läufe bleiben an ihren damaligen Eingabebestand und Fall gebunden, nicht an spätere Mini-Fassungen oder deren neue Prüfvermerke. Zusätzliche Dateien oder Ordner im vorbereiteten Eingabeordner machen den Lauf ungültig.

Eine zusätzlich dokumentierte Einzelprüfung der Werkstatt steht in `workshop_review` mit Begründung, Änderungen und `sha256`. Ist dieser Prüfvermerk vorhanden, muss auch seine Prüfsumme zur aktuellen Werkstatt-Datei passen. Die Prüfsumme bestätigt nur die Identität des redaktionell geprüften Textes, nicht einen bestandenen Modelllauf. Nach inhaltlichen Änderungen zuerst erneut prüfen und erst danach den Vermerk aktualisieren; ein bloßes Neuberechnen der Prüfsumme ersetzt die Prüfung nicht.

Für ein gemeinsam geprüftes Hauptproblem-Paar enthält `focus_review` beide Dateipfade, `prompt_sha256` und `skill_sha256` sowie Datum, Begründung und Änderungen. Der Skill muss genau dem in `selection.target_skill` benannten Schwerpunkt entsprechen; der Prompt muss zum selben Plugin gehören. Die Methode `desk_review` bezeichnet ausschließlich die Textprüfung. Abweichende Dateien, Pfade oder Prüfsummen werden abgewiesen. Ein fehlender Schwerpunktvermerk in einem älteren Profil wird nicht als bestandene Paarprüfung ausgegeben.

```bash
python3 scripts/quality-lab.py audit
python3 scripts/quality-lab.py prepare PLUGIN FALL --mode schnellstart --run /absoluter/pfad/ausserhalb-des-repos/lauf-001
```

Die Varianten sind `plugin`, `werkstatt`, `schnellstart`, `hauptproblem` und `baseline`. Die letzte Variante verwendet keine zusätzliche Fachanweisung. Ein Schwerpunkt ist nur bei den dafür ausgestatteten Fachpaketen verfügbar. Für `plugin` das Paket in einer frischen Sitzung installieren; keinen bestimmten Skill vorab erzwingen. Die automatische Auswahl ist Teil der Beobachtung.

Dem ausführenden Client ausschließlich `input/` zugänglich machen und einen leeren, beschreibbaren Ausgabeordner bereitstellen. `run.json`, Prüfkriterien und Prüferantworten bleiben außerhalb seiner Zugriffsrechte. Eine bloße Bitte, nicht in den übergeordneten Ordner zu schauen, ist keine Isolation. Der Export richtet diese Rechte im fremden Client nicht selbst ein.

Der Client bearbeitet `request.txt` mit der passenden Anweisung aus `instructions.md`. Die Ergebnisse anschließend unverändert nach `output/` übernehmen. Erwartete Dateinamen sind verbindlich; eine ähnliche oder anders benannte Datei wird nicht heimlich als Ersatz gewertet. Die Vorbereitung überschreibt keinen bestehenden Lauf und bindet Eingaben, Fachvariante und Zielskill an Prüfsummen. Git-Revision und tatsächlicher Dateiinhalt werden getrennt protokolliert.

## 1.3. Messwerte und Abbrüche erfassen

Neben `run.json` eine `metrics.json` aus dem tatsächlichen Client-Lauf ablegen:

```json
{
  "client": "Arbeitsoberfläche mit Versionsangabe",
  "model": "tatsächliche Modellkennung",
  "finish_reason": "finish_tool",
  "duration_ms": 42000,
  "input_tokens": null,
  "output_tokens": null,
  "selected_skills": [],
  "measurement": "client_export"
}
```

Unbekannte Tokenzahlen bleiben `null`, nicht null Verbrauch. Bei händischer Erfassung `manual_record` angeben und den Originalablauf für eine Nachprüfung getrennt aufbewahren. Zulässige Abschlussgründe: `finish_tool`, `no_tool_calls`, `user_confirmed`, `max_turns_exceeded`, `context_overflow`, `timeout`, `provider_error`, `cancelled`. Die letzten fünf sind keine sauberen Abschlüsse. Eine Meldung ohne Werkzeugaufruf beweist für sich noch nicht, dass alle Dateien vorhanden sind.

```bash
python3 scripts/quality-lab.py inspect /absoluter/pfad/lauf-001
```

Die Prüfung kontrolliert erwartete, nicht leere und lesbare Dateien. Keine stillschweigende Kürzung übergroßer Texte, kein umbenanntes Textdokument als PDF, keine Auswertung außerhalb des Ausgabeordners. Bei DOCX werden auch Kommentare, Kopf-/Fußzeilen und Änderungsinhalte berücksichtigt; das ist kein Ersatz für eine visuelle Endkontrolle. XLSX-Formeln werden als Formeln gelesen, nicht als hier neu berechnete Werte ausgegeben. Für Bilder und Scans ist eine gesonderte nachvollziehbare Sicht- oder OCR-Prüfung erforderlich.

## 1.4. Zwei unabhängige Ergebnisprüfer

Die Prüfkonfiguration liegt außerhalb des Repositorys. Zwei unterschiedliche Modelle und getrennte IDs verwenden. Unterstützte API-Protokolle: `messages`, `responses`, `chat-completions`. Der Endpunkt ist die vollständige HTTPS-Adresse des jeweiligen API-Aufrufs. Zugangsdaten stehen ausschließlich in Umgebungsvariablen, nicht in JSON, Prompts oder Versionskontrolle.

Die Prüfer-ID `dual` ist für den Gesamtbericht reserviert und darf keinem Einzelprüfer zugewiesen werden.

```json
{
  "judges": [
    {"id": "pruefer-eins", "model": "MODELLKENNUNG_1", "protocol": "messages", "endpoint": "https://api.example.invalid/v1/messages", "key_env": "QUALITY_KEY_ONE"},
    {"id": "pruefer-zwei", "model": "MODELLKENNUNG_2", "protocol": "responses", "endpoint": "https://api.example.invalid/v1/responses", "key_env": "QUALITY_KEY_TWO"}
  ]
}
```

```bash
python3 scripts/quality-lab.py evaluate /absoluter/pfad/lauf-001 --config /absoluter/pfad/pruefer.json --allow-remote
```

`--allow-remote` bestätigt die externe Übermittlung des Aufgabenmaterials und der relevanten Ergebnisse an die konfigurierten Prüfer. Ohne diese ausdrückliche Auswahl wird nichts übertragen. Nur dafür freigegebene Daten verwenden. Jeder API-Aufruf hat ein Zeitlimit; vorübergehende Fehler werden höchstens zweimal wiederholt. Weiterleitungen werden nicht mit Zugangsdaten verfolgt. Eine fehlende Funktion wird nicht durch unbeschränkte Wiederholungen ersetzt.

Jedes Kriterium wird einzeln anhand der ihm zugeordneten Ergebnisse bewertet. Kurze Begründung, Urteil und Beleg sind Pflicht. Ein positives Urteil ohne tatsächlich im Ergebnis vorhandenen Textbeleg wird verworfen. Einzelantworten bleiben erhalten; das gemeinsame Ergebnis wird nur nach Abschluss beider Prüfungen geschrieben. Scheitert eine Wiederholungsprüfung, wird ein früheres gemeinsames Ergebnis entfernt. Nachträglich geänderte Ergebnisse machen ihre Bewertung ungültig.

`dual_all_pass_rate` ist ein Diagnosewert zwischen null und eins. Der Wert 0.5 bedeutet nicht freigegeben. `all_pass` ist nur wahr, wenn beide Prüfer sämtliche Kriterien bestehen lassen. Unterschiedliche Urteile führen zu `needs_review`. Quellenidentität, Normstand und Reichweite einer Entscheidung bleiben gesondert anhand tatsächlich konsultierter Primärquellen zu prüfen; zwei zustimmende Modelle ersetzen das nicht. Bei Uneinigkeit den konkreten Beleg fachlich entscheiden, nicht solange neu würfeln, bis beide zustimmen.

Verschiedene Modellkennungen beweisen keine statistische Unabhängigkeit. Gemeinsame Fehler sind möglich; besonders folgenreiche Feststellungen benötigen eine gesonderte fachliche Kontrolle. Der `responses`-Aufruf fordert keine Speicherung zur späteren API-Abfrage an; dies ersetzt keine Prüfung der sonstigen Speicher- und Verarbeitungsbedingungen des gewählten Anbieters.

## 1.5. Auswahl und Wiederholbarkeit messen

```bash
python3 scripts/quality-lab.py selection-export PLUGIN
python3 scripts/quality-lab.py selection-score /absoluter/pfad/beobachtungen.json
python3 scripts/quality-lab.py compare /absoluter/pfad/lauf-001 /absoluter/pfad/lauf-002
```

Der Auswahl-Export enthält Anfragen und stabile IDs, keine Soll-Antworten. Jede Anfrage in einer neuen Sitzung bearbeiten. Die Beobachtungsdatei enthält `plugin`, `selection_hash` aus dem Export, `client`, `model` und `observations`. Jeder Eintrag benötigt `id`, `status` (bei vollständiger Ausführung `completed`) und `selected_skills` als Liste tatsächlich gewählter `plugin/skill`-Namen. Eine leere Liste ist eine beobachtete Nichtauswahl; ein fehlender Eintrag ist ungeprüft. Falsch-positive und falsch-negative Pluginaktivierungen werden getrennt gezählt. Das sind importierte Beobachtungen, keine heimlich ausgeführten Client-Tests.

Für Vergleiche dieselben Fallaufträge, Eingaben, Prüfer und Budgets verwenden. Alte und neue Fachanweisung getrennt vorbereiten und mindestens drei unabhängige Wiederholungen pro Vergleichsbedingung vorsehen. Ergebnisse zur qualitativen Gegenprüfung neutral als A/B vorlegen. Zeit- und Tokenmittelwerte mit Streuung lesen, nicht nur einen besonders guten Lauf auswählen. Ein zusätzlicher, bei der Überarbeitung unberührter Fallsatz dient der Abschlusskontrolle. Die Mindestprofile im Repository sind ein Ausgangspunkt, kein statistisch repräsentativer Nachweis über alle enthaltenen Skills.

Bei den Schwerpunktprofilen begrenzt `selection.target_skill` die Auswahlprüfung auf den konkret benannten Spezialskill. Ein anderer sinnvoller Skill desselben Plugins ist bei einer negativen Anfrage dann keine Fehlaktivierung. Ohne dieses Feld wird die Aktivierung des ganzen Plugins bewertet. Die Ergebnisfälle haben daneben ihren eigenen `target_skill`; dieser wird bei der Aufgabenbearbeitung nicht vorgegeben.

## 1.6. Entwicklung und Freigabe

Bei abgeschlossenen Auswahlbeobachtungen muss `selected_skills` ausdrücklich vorliegen; ein fehlendes Feld ist keine beobachtete Nichtauswahl. Der Vergleich weist mehrfach angegebene Laufordner auch dann zurück, wenn unterschiedliche Pfade über Symlinks denselben Ordner bezeichnen. Unabhängige Wiederholungen benötigen eigene Laufordner.

Die Offline-Prüfungen laufen vor dem Release; sie rufen keine kostenpflichtigen Modelle auf. Der öffentliche [Prüfkatalog](../QUALITY.md) zeigt deshalb vorbereitetes Material und keine erfundenen Erfolgsquoten. Protokolle echter Modellläufe bleiben außerhalb der installierbaren Plugins. Es werden nicht bei jedem Mandatsaufruf zwei Prüfmodelle gestartet.

Exit-Code `0` bedeutet: der ausdrücklich gewählte Vorgang wurde erfolgreich ausgeführt. Bei `prepare` oder `audit` ist das keine fachliche Freigabe. Exit-Code `1` bezeichnet einen negativen Befund; `2` bezeichnet eine nicht abgeschlossene oder noch fachlich zu entscheidende Bewertung. Der bisherige Aktenbestandsprüfer bietet `--structural-only` für technische CI-Prüfungen; offene menschliche Kriterien werden weiterhin ausdrücklich ausgewiesen.

## 1.7. Fortsetzung nach Rückfragen prüfen

Die zusätzlichen Fortsetzungsfälle im Familien-, Erb- und Steuerrecht enthalten einen bereits erreichten Bearbeitungsstand und eine neue Antwort. Sie prüfen, ob die Antwort berücksichtigt, die betroffene Rechnung oder Auskunft fortgeschrieben und das bestellte Schreiben tatsächlich ausformuliert wird. Eine zweite entscheidende Lücke darf nicht deshalb unbeachtet bleiben, weil schon einmal nachgefragt wurde. Der Empfängertext muss von internen Prüf- und Exporthinweisen getrennt bleiben.

Diese Fälle werden als ein Arbeitsauftrag mit beschriebenem Vorverlauf vorbereitet. Sie sind kein automatisch ausgeführter Mehr-Runden-Dialog. Für eine echte Gesprächsprüfung im verwendeten Client die Angaben schrittweise übermitteln, den unveränderten Verlauf sichern und prüfen: Wird die richtige Frage gestellt? Wird ihre Antwort verwendet? Entsteht ohne erneute Aufnahme das gewünschte Dokument? Bleibt bei fehlendem Beleg nur der davon abhängige Teil offen? Ohne diesen aufgezeichneten Client-Lauf keine bestandene Gesprächsprüfung behaupten.

Ein fachliches Gutachten kann das beauftragte Endprodukt sein. Ein verlangter Brief, Vertrag oder Schriftsatz ist dagegen nicht durch eine Analyse, eine Tabelle oder die Ankündigung seiner späteren Erstellung ersetzt. Die Bewertung richtet sich nach dem konkreten Auftrag, nicht nach der Anzahl von Überschriften, Rückfragen oder Dateien.

## 1.8. English summary

This laboratory separates package validation, observed skill selection and evaluation of actual work products. A prepared test is not a passing model run. Only expose the input directory to the working client; keep assessment criteria outside its accessible workspace. Use two independently configured judges, preserve failures and disagreements, and compare identical cases with recorded client versions, model versions, timing and artifact hashes. Automated agreement does not independently verify legal sources or authorize filing. Remote evaluation is opt-in and may incur provider charges.
