# 1. Lokale Prüfhilfe für Befunde und Berichte

Die optionale Datei `scripts/playbook_review.py` prüft bereits erarbeitete Befunde. Sie liest keine Rechtsposition aus einem Vertrag heraus und entscheidet keine Rechtsfrage. Sie kontrolliert Quelldateien und wörtliche Zitate, verlangt einen Befund für jede Regel, zählt die Ergebnisse und erzeugt einen strukturierten Bericht. Die Skills und eigenständigen Prompts funktionieren auch ohne diese Datei.

## 1.1. Ausführen

Python ab Version 3.10 genügt für TXT, Markdown, DOCX und EML. PDF-Quellen benötigen zusätzlich `pypdf`, Word-Ausgaben `python-docx`. Fehlende Bibliotheken werden gemeldet und nicht automatisch installiert. Das Programm stellt keine Netzwerkverbindung her und versendet keine Dokumente.

Vom Pluginordner aus lässt sich das kleine technische Beispiel so ausführen:

```sh
python3 scripts/playbook_review.py assets/review-beispiel.json --output /tmp/playbook-beispiel-001.json
python3 scripts/playbook_review.py assets/review-beispiel.json --output /tmp/playbook-beispiel-001.md
python3 scripts/playbook_review.py assets/review-beispiel.json --output /tmp/playbook-beispiel-001.docx
```

Bereits vorhandene Ausgaben werden nicht überschrieben. Wählen Sie für jede Revision einen neuen Dateinamen. `--draft` erlaubt Zwischenstände mit Pending; ein Abschlusslauf ohne diesen Schalter lehnt Pending ab. `--source-root ORDNER` bezeichnet den vereinbarten lokalen Quellenordner; standardmäßig gilt der Ordner der JSON-Eingabe. Relative Dokumentpfade müssen darin bleiben, auch nach Auflösung symbolischer Links.

## 1.2. Aufbau der Eingabe

`assets/review-beispiel.json` ist eine vollständig lauffähige Eingabe mit zwei Topics. Sie ist ein technisches Zählbeispiel und weder Musterlösung einer Testakte noch vollständig freigegebenes NDA-Playbook. Die reichhaltigen Testakten enthalten ihre eigenen Unternehmens-Playbooks in Word. Eine Übertragung dieser Playbooks muss Regel für Regel mit dem Original abgeglichen werden; das Beispiel ersetzt diesen Schritt nicht.

| Feld | Inhalt |
| --- | --- |
| `schema_version` | Derzeit `1`. |
| `review_id` | Eindeutige Bezeichnung des Laufs. |
| `document_precedence` | Tatsächlich geklärte maßgebliche Fassung, Anlagenrangfolge und verbleibende Einschränkungen. |
| `documents` | Dateien mit eindeutiger `id`, `title`, `version`, relativem `path`, SHA-256 der Originalbytes und `role`. |
| `playbook` | `id`, `version`, `approved_by`, `approval_reference`, `contract_type`, `client_side` und vollständige `topics`. |
| `topic_observations` | Objekt mit einem Eintrag für jede Topic-ID: `presence`, `reasoning` und gegebenenfalls gesonderte `legal_findings`. |
| `observations` | Objekt mit genau einem Eintrag für jede Regel-ID. Fehlende oder zusätzliche IDs brechen den Lauf ab. |

Jedes Topic enthält `id`, `title`, das ausdrücklich boolesche Feld `required` und `positions`. Jede Position enthält eine weltweit im Lauf eindeutige `id`, `type` und mindestens eine Regel. Genau eine Position je Topic heißt `starting`; weitere können `fallback` sein. Mindestens eine heißt `not_acceptable`. Die Fallback-Reihenfolge in der Liste ist ihre ausgehandelte Priorität. Eine Regel enthält `id` und eine konkrete testbare `condition`. Topic-, Positions- und Regel-IDs sollen bei bloßen Textkorrekturen stabil bleiben; eine sachlich geänderte Bedingung erhält eine neue Playbookversion.

Für Start und Fallback ist die Logik `all`: Alle anwendbaren Bedingungen müssen erfüllt sein. Bei roten Positionen muss `match_mode` ausdrücklich `any` oder `all` sein. `any` bedeutet, dass jede einzelne verbotene Bedingung selbständig genügt. `all` bedeutet, dass erst die vollständige Kombination verboten ist. Unabhängige Verbote dürfen nicht versehentlich mit `all` zusammengebunden werden.

## 1.3. Bindung an Originale und Fassungen

Die Dokumentrolle `authoritative` bezeichnet den gemeinsam geprüften aktuellen Vertrag samt vereinbarten Anlagen. `context` bezeichnet Korrespondenz oder Tatsachenbelege. `superseded` bezeichnet überholte Fassungen. Mehrere voneinander unabhängige Verträge gehören in getrennte Reviews. Die Rangfolge wird vorab juristisch ermittelt; eine höhere Dateinummer oder ein späterer E-Mail-Zeitstempel ersetzt keine Vereinbarung.

Vor dem Lauf wird für jede Datei die SHA-256-Prüfsumme berechnet und mit dem eingegebenen Wert verglichen. Eine neue Vertragsfassung erfordert daher einen neuen dokumentierten Stand. Die Maschine kann eine absichtlich falsch zugewiesene Dokumentrolle nicht erkennen: Die Auswahl und Versionszuordnung bleiben überprüfbare fachliche Arbeit.

DOCX wird aus dem Haupttext einschließlich Tabellen gelesen. Kopfzeilen, Kommentare, Fußnoten und Text in Bildern sind keine zugesicherte Extraktionsgrundlage. Offene Word-Änderungsmarkierungen werden zurückgewiesen, bis die maßgebliche Fassung geklärt ist. EML wird aus den reinen Textteilen gelesen; Anlagen sind zusätzlich als eigene Dokumente aufzunehmen. PDF wird ohne OCR gelesen. Bei Scans oder Layoutfehlern braucht es eine überprüfte Transkription samt Originalreferenz. Ein nicht lesbarer maßgeblicher Text stoppt den Lauf.

## 1.4. Regelbefunde

Jeder Befund enthält `outcome`, `basis` und eine konkrete `reasoning`. Die internen Werte sind `met`, `not_met`, `not_verifiable`, `pending` oder `excluded`. Bei roten Positionen zeigt der Bericht `Detected` und `Not detected`; die internen Wahrheitswerte werden nicht invertiert.

Bei `basis: quote` tragen `citations` die Felder `document_id`, `locator`, `quote` und `locator_verified: true`. Das Programm prüft die Wortfolge im extrahierten Original und vereinheitlicht dabei nur Leerraum. Es verändert weder Wörter noch Satzzeichen. Eine auslegende Umschreibung gehört in die Begründung, nicht in das Zitat. Der Seiten- oder Klauselort muss zuvor tatsächlich am Original kontrolliert worden sein; `locator_verified` darf nicht als bloßer Automatismus gesetzt werden. Das Programm prüft selbst keine PDF-Markierungskoordinaten und erzeugt keine interaktiven Fundstellen-Schaltflächen.

Ein entschiedener Vertragsbefund verlangt mindestens ein Zitat aus einer maßgeblichen Vertragsdatei. Eine Kontext-E-Mail kann zusätzliche Tatsachen belegen, ersetzt jedoch nicht die Einigung im Vertrag. Überholte Fassungen werden als tragende Fundstelle zurückgewiesen. Änderungsvergleiche können sie separat beschreiben, müssen den aktuellen Befund aber neu an der maßgeblichen Fassung belegen.

Bei fehlendem Klauselinhalt darf kein Zitat erfunden werden. `basis: absence` nennt stattdessen alle `searched_document_ids` des maßgeblichen Vertragssatzes und eine konkrete `search_description`. Die fachliche Vollständigkeit dieser Suche kann die Maschine nicht beweisen. Sie kontrolliert, dass kein maßgebliches Dokument still aus dem Suchumfang herausfällt. Ob das Fehlen die konkrete Regel erfüllt oder verletzt, folgt aus deren Wortlaut; „keine Vertragsstrafe“ und „eine Vertragsstrafe ist enthalten“ haben entgegengesetzte Bedingungen.

Offene Befunde verwenden `basis: unresolved` und eine konkrete nächste `question`. Sachliche Scope-Ausnahmen verwenden `excluded` mit `scope_approval.by`, `.reason` und `.reference`. Dies dokumentiert eine zuvor geklärte Nichtanwendbarkeit; bloße Unsicherheit oder ein schwieriger Befund rechtfertigen keinen Ausschluss. Exclusions bleiben als eigene Zahl sichtbar. Eine vollständig ausgeschlossene Position wird niemals durch eine leere UND-Verknüpfung als erfüllt behandelt.

## 1.5. Zählung und Risikostufe

Der Nenner einer Position umfasst nur `met` und `not_met`. Nicht verifizierbare, offene und ausdrücklich ausgenommene Regeln werden jeweils separat gezählt. Daher bedeutet `2/2 Detected` bei einer roten Position zwei erkannte verbotene Bedingungen. `0/2 Detected` bedeutet, dass beide geprüft und nicht erkannt wurden. `0/0` bedeutet niemals einen entlastenden Vollbefund.

Ein `all`-Match ist falsch, sobald mindestens eine anwendbare Regel falsch ist; vollständig wahr ist es nur bei ausschließlich erfüllten Regeln. Ein `any`-Match ist wahr, sobald eine Regel wahr ist; vollständig falsch nur, wenn sämtliche anwendbaren Regeln falsch sind. Andernfalls ist das Match unbekannt. Diese Logik ändert keine Einzelbefunde und keine wörtlichen Zähler.

Ein nach den eigenen Bedingungen erkanntes Verbot, ein gesondert begründeter feststehender Wirksamkeitsmangel oder ein fehlendes Pflicht-Topic ergibt High risk. Dasselbe gilt bei gefundenem Topic, wenn alle akzeptablen Positionen sicher verfehlt sind. Ein solcher bereits feststehender hoher Befund wird durch zusätzlich offene Regeln nicht auf Not verifiable herabgestuft. Sonst verhindert ein ungeklärter Fundstatus, eine ungeklärte rote Position oder ein offener Rechtsbefund die abschließende Risikozuweisung. Eine vollständig erfüllte Ausgangsposition ohne solche Hindernisse ergibt „No identified playbook risk“; ein tragfähiger Fallback ergibt Medium risk. Übrige unentscheidbare Kombinationen bleiben Not verifiable.

`presence` und Risiko bleiben getrennt. Ein Topic ohne Klausel trägt `Not found`, selbst wenn sein Fehlen zugleich ein hohes Risiko begründet. Ein optionales fehlendes Thema wird nicht automatisch als freigegeben behandelt. Ein bekannter passender Fallback kann neben einer noch ungeklärten stärkeren Position stehen; die offene Regel bleibt dabei sichtbar und verhindert eine vollständige Entscheidungsvorlage.

## 1.6. Gesetzesprüfung und Entscheidung

Die Playbookampel ist keine Aussage, dass ein Vertrag in jeder Hinsicht wirksam oder wirtschaftlich sinnvoll ist. Gesonderte Rechtsbefunde nennen `status: confirmed_invalid` oder `needs_review`, `reasoning`, `authority`, `source_url`, `pinpoint`, `checked_on` und `contract_citations`. Das Programm prüft ihre formale Vollständigkeit und die Vertragszitate, aber weder die Rechtsquelle online noch die juristische Richtigkeit der Subsumtion. Ein fachlich begründeter feststehender Wirksamkeitsmangel hat Vorrang vor einer firmenintern passenden Position.

`ready_for_human_decision` bedeutet ausschließlich: Abschlusslauf ohne offene Regeln, ohne hohes Risiko und ohne unentscheidbare Topics. Auch dann wird keine Unterschrift freigegeben, keine Annahmeerklärung abgegeben und nichts versendet. Der Bericht enthält alle Regelbefunde mit Quellen sowie offene Fragen und Scope-Ausnahmen. Der Word-Export ist bearbeitbar; vor Übergabe sind Seitenlayout und Fundstellen erneut zu kontrollieren.
