# KI-Halluzinationsreduzierer

Dieses juristische Plugin prüft Fundstellen in Schriftsätzen, Gutachten, Verträgen und anderen Rechtstexten. Es untersucht jede Quellenverwendung vom Originalnachweis bis zur Anwendung auf den Fall und erstellt einen ausformulierten Prüfbericht mit nachvollziehbarer Korrekturfassung. Es eignet sich für Kanzleien, Rechtsabteilungen, Gerichte und juristische Redaktionen. Ob der Ausgangstext mit KI erzeugt wurde, spielt für die Prüfung keine Rolle.

**Ohne zugänglichen maßgeblichen Originalvolltext gibt es keine Bestätigung des Inhalts.** Das System muss offen sagen: „Ich weiß es nicht; diese Fundstelle konnte inhaltlich nicht verifiziert werden.“ Eine erfolglose Suche beweist umgekehrt nicht, dass die Entscheidung nicht existiert.

Starten Sie mit: **„Prüfen Sie sämtliche Fundstellen dieses Textes. Belegen Sie getrennt Existenz, Identität, Fundpunkt, Aussagekraft und Übertragbarkeit. Erstellen Sie einen Prüfbericht und eine getrennte Korrekturfassung.“** Laden Sie dann den zu untersuchenden Text einschließlich Fußnoten und Anlagen hoch. Bereits bekannte Angaben werden übernommen; nur entscheidende Lücken werden nachgefragt.

[Startseite](../README.md) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/ki-halluzinationsreduzierer.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten aller Themen](../testakten/README.md) · [Plugin-Dateien](.)

Version 1.1.0 · zehn Fachskills und ein Hauptskill · Prüfstand 19.10.2026. [Änderungsverzeichnis](CHANGELOG.md).

## 1. Was genau geprüft wird

| Prüfung | Typischer Befund |
| --- | --- |
| Existenz und tatsächlicher Zugang | Die amtliche Liste nennt die Entscheidung; der Volltext ist gesperrt. Existenz belegt, Inhalt unbekannt. |
| Identität | Gericht und Datum stimmen, aber das Aktenzeichen oder die Zeitschriftenfundstelle führt zu etwas anderem. |
| Fundpunkt und Wiedergabe | Die Randnummer enthält Parteivortrag, eine Auslassung verändert den Sinn oder die angegebene Seite fehlt. |
| Aussagekraft | Die Passage ist echt, trägt aber den behaupteten allgemeinen Rechtssatz nicht. |
| Fallübertragbarkeit | Der Rechtssatz gilt unter anderen Voraussetzungen, in einer anderen Verfahrensart oder unter einer alten Normfassung. |

Die Ergebnisse bleiben getrennt. Eine echte Entscheidung führt nicht automatisch zu einem positiven Gesamtbefund. Dieselbe Quelle wird für jede damit belegte Aussage erneut bewertet. Eine zusätzliche unbestätigte Zeitschriftenfundstelle bleibt sichtbar, auch wenn der amtliche Entscheidungsnachweis stimmt.

### 1.1 Maßstäbe aus sieben gerichtlichen Beschlüssen

Der [Rechtsprechungsüberblick mit amtlichen Volltextlinks](references/rechtsprechung-ki-schriftsaetze.md) erschließt drei Beschlüsse des Kammergerichts, drei des VGH Baden-Württemberg und BAG, Beschluss vom 30.09.2026 – 2 AZN 339/26. Jeder Anker benennt seine Aussage und seine Grenze. **KI-Schriftsätze sind nicht pauschal unwirksam.** Fehlende eigenverantwortliche Prüfung und unzureichende Rechtsmittelbegründung können aber erhebliche prozessuale Folgen haben.

Deshalb ergänzt die [Schriftsatzprüfung](references/schriftsatzpruefung.md) die Quellenkontrolle um Aktenbezug, Auseinandersetzung mit der angegriffenen Entscheidung und tatsächliche anwaltliche Verantwortungsübernahme. Ein Quellenbericht, eine Signatur oder ein automatisch gesetzter Freigabevermerk ersetzt keine eigene fachliche Prüfung. Das Prüfjournal ist eine organisatorische Hilfe; es ist keine vom Gericht vorgeschriebene zusätzliche Form.

## 2. Downloads und Verwendung

[Claude-Plugin als ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-halluzinationsreduzierer-v1.1.0/ki-halluzinationsreduzierer.zip) · [Portables Paket](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-halluzinationsreduzierer-v1.1.0/ki-halluzinationsreduzierer-portable.zip) · [Alle Release-Dateien](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-halluzinationsreduzierer-v1.1.0)

Das Pluginpaket enthält alle elf Skills und ihre Referenzen. Werkstatt, Mini und Hauptproblem sind eigenständig nutzbare Fassungen desselben Prüfmaßstabs und separate Downloads. Der Mini ist kein zwölfter Skill. MD und TXT enthalten jeweils denselben Text; PDF ist die Lesefassung.

| Einstieg | Bearbeitbarer Prompt | Lesefassung |
| --- | --- | --- |
| Große Werkstatt: vollständiger Prüfablauf mit Grenzfällen und Durchläufen | [MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/ki-halluzinationsreduzierer-werkstatt.md) · [TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/ki-halluzinationsreduzierer-werkstatt.txt) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-halluzinationsreduzierer-v1.1.0/ki-halluzinationsreduzierer-werkstatt.pdf) |
| Mini-Prompt: kompakter vollständiger Ablauf | [MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/ki-halluzinationsreduzierer-schnellstart.md) · [TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/ki-halluzinationsreduzierer-schnellstart.txt) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-halluzinationsreduzierer-v1.1.0/ki-halluzinationsreduzierer-schnellstart.pdf) |
| Hauptproblem: eine entscheidende Fundstelle und ihre abhängigen Aussagen aufklären | [MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/ki-halluzinationsreduzierer-hauptproblem.md) · [TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/ki-halluzinationsreduzierer-hauptproblem.txt) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-halluzinationsreduzierer-v1.1.0/ki-halluzinationsreduzierer-hauptproblem.pdf) |

Claude Code und kompatible Cowork-Umgebungen verwenden die Pluginstruktur. Das Paket enthält außerdem Codex- und portable Metadaten. In ChatGPT können Sie den Mini-Prompt als Anweisung und die Werkstatt als ergänzende Datei verwenden. Importfunktionen, Browser und Datenbankzugang hängen von Ihrer tatsächlichen Umgebung ab. Das Paket stellt selbst weder ein kostenpflichtiges Recherchekonto noch einen Browser bereit; eine Ausführung in sämtlichen Oberflächen wird nicht behauptet.

## 3. Arbeitsablauf und Ergebnis

1. Ausgangstext und lesbaren Umfang sichern, Aussagen und sämtliche erkennbaren Fundstellenvorkommen erfassen.
2. Maßgebliche Originalquellen tatsächlich öffnen und Zugangsgrenzen dokumentieren.
3. Identität, Fundpunkt und konkrete Aussage einzeln prüfen.
4. Zeitbezug, Fallunterschiede und Gegenargumente untersuchen.
5. Prüfbericht, Quellenprotokoll und gegebenenfalls Korrekturfassung mit Änderungsverzeichnis erstellen.
6. Alle Vorkommen gegen das Register nachprüfen; bei Schriftsätzen Aktenbezug und Verfahrensbegründung gesondert kontrollieren.
7. Geprüfte Fassung und offene Punkte zur tatsächlichen menschlichen Entscheidung und Fortsetzung übergeben.

Die Originaldatei bleibt erhalten. Eine vermutete richtige Ersatzentscheidung wird nicht still in eine falsche Fundstelle eingesetzt. Korrekturen zeigen alten Satz, neuen Satz, Grund und verknüpfte Quellen. Bei fehlenden Fallangaben kann die Quellenprüfung fortgesetzt werden; die Fallübertragung bleibt ausdrücklich offen.

## 4. Quellen und Grenzen

Für Rechtsprechung sind nur tatsächlich zugängliche amtliche Originalvolltexte zugelassen. Suchtreffer, Pressetexte, Leitsätze, Blogs und KI-Zusammenfassungen ersetzen sie nicht. Für Literatur und technische Standards ist nur der zugängliche Verlags- oder Herausgeberoriginaltext verwendbar, ausdrücklich als eigene nichtamtliche Quellenklasse. Wenn der Prüfauftrag ausschließlich amtliche Quellen erlaubt, werden diese nichtamtlichen Nachweise lediglich inventarisiert. Nutzerunterlagen bestätigen ihre Originalherkunft nicht selbst.

[Prüfvertrag](references/pruefvertrag.md) · [Strenger Quellenmaßstab](references/zitierweise.md) · [Quellenprotokoll und Befundbeispiele](references/quellenprotokoll.md)

Das Plugin erkennt weder verlässlich KI-Autorenschaft noch garantiert es Fehlerfreiheit. Veröffentlichungsumfang, Lesbarkeit und tatsächliche Zugänge begrenzen das Ergebnis. Vertrauliche Mandatsdaten werden nicht zur Suche an öffentliche Dienste übertragen. Gerichtliche Einreichung oder externer Versand sind kein Bestandteil dieses Prüfauftrags.

## 5. Erprobung

Die Qualitätssicherung umfasst sechs ausdrücklich simulierte Fehlerszenarien: gesperrter Volltext, andere Entscheidung am angegebenen Ort, Parteivortrag, falsche Verfahrensübertragung, offene Parallelfundstelle und eine Nutzerdatei mit manipulativer Anweisung. Diese Übungen behaupten keine tatsächlich ergangenen Entscheidungen und keine amtlichen Abrufe. Ergänzende Probeläufe behandeln gerichtliche Maßstäbe, falsche Verfahrensübertragungen und bereits eingereichte Fehler. Der [Prüfbericht](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/quality/ki-halluzinationsreduzierer/README.md) trennt strukturelle Tests, redaktionelle Prüfung und die begrenzte Modell-Anwendungsprobe.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`amtliche-quellen-erschliessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/amtliche-quellen-erschliessen/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`halluzinationspruefung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/halluzinationspruefung-steuern/SKILL.md), [`nachpruefung-und-qualitaetskontrolle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/nachpruefung-und-qualitaetskontrolle/SKILL.md), [`normfassungen-und-zeitbezug-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/normfassungen-und-zeitbezug-pruefen/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`pruefbericht-und-korrekturfassung-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/pruefbericht-und-korrekturfassung-erstellen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`uebertragbarkeit-und-gegenargumente-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/uebertragbarkeit-und-gegenargumente-pruefen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`aussagen-am-volltext-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/aussagen-am-volltext-pruefen/SKILL.md), [`entscheidungsidentitaet-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/entscheidungsidentitaet-abgleichen/SKILL.md), [`fundstellen-inventarisieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/fundstellen-inventarisieren/SKILL.md), [`literatur-materialien-und-standards-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/literatur-materialien-und-standards-pruefen/SKILL.md), [`zitate-und-randnummern-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/zitate-und-randnummern-pruefen/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`amtliche-quellen-erschliessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/amtliche-quellen-erschliessen/SKILL.md) | Sucht juristische Fundstellen ausschließlich in maßgeblichen Originalquellen und dokumentiert den tatsächlichen Volltextzugang. Unterscheidet amtliche Entscheidung, Pressemitteilung, Metadaten und gesperrte Quelle, ohne fehlenden Zugang... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/amtliche-quellen-erschliessen/SKILL.md) |
| [`aussagen-am-volltext-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/aussagen-am-volltext-pruefen/SKILL.md) | Prüft, ob eine gelesene Originalfundstelle die konkrete Rechtsbehauptung tatsächlich trägt. Trennt gerichtliche Aussage, Schlussfolgerung und nicht entschiedene Frage und erstellt einen begründeten Befund mit Aussagegrenzen statt bloßer... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/aussagen-am-volltext-pruefen/SKILL.md) |
| [`entscheidungsidentitaet-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/entscheidungsidentitaet-abgleichen/SKILL.md) | Prüft, ob Gericht, Entscheidungsform, Datum, Aktenzeichen, ECLI und Veröffentlichungsfundstelle wirklich dieselbe Entscheidung bezeichnen. Erkennt vermischte Nachweise und trennt eine echte Entscheidung von einer falschen Parallelfundste... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/entscheidungsidentitaet-abgleichen/SKILL.md) |
| [`fundstellen-inventarisieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/fundstellen-inventarisieren/SKILL.md) | Erfasst sämtliche Fundstellen eines juristischen Dokuments mit ihrer konkreten Aussage und Textposition. Trennt wiederkehrende Quellen von einzelnen Zitatvorkommen und weist unlesbare Teile, verkürzte Nachweise und ungeprüfte Aussagen aus. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/fundstellen-inventarisieren/SKILL.md) |
| [`halluzinationspruefung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/halluzinationspruefung-steuern/SKILL.md) | Prüft juristische Texte durchgehend auf Existenz und Identität ihrer Quellen, richtige Fundpunkte, Aussagekraft und Fallübertragbarkeit. Erstellt einen belegten Prüfbericht und eine getrennte Korrekturfassung; fehlender Originalvolltext... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/halluzinationspruefung-steuern/SKILL.md) |
| [`literatur-materialien-und-standards-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/literatur-materialien-und-standards-pruefen/SKILL.md) | Prüft Literatur, Gesetzgebungsmaterialien und technische Standards nach ihrer Quellenart. Trennt Katalognachweis von gelesenem Originalvolltext, wahrt Zugangsschranken und benennt, welche Aussage und welche rechtliche Bedeutung tatsächli... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/literatur-materialien-und-standards-pruefen/SKILL.md) |
| [`nachpruefung-und-qualitaetskontrolle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/nachpruefung-und-qualitaetskontrolle/SKILL.md) | Kontrolliert Vollständigkeit, Quellenzugriff, getrennte Prüfbefunde und Textänderungen eines juristischen Fundstellenchecks. Prüft neue Fassungen gezielt nach und verhindert unbelegte Gesamtfreigaben oder stillschweigend übernommene Altb... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/nachpruefung-und-qualitaetskontrolle/SKILL.md) |
| [`normfassungen-und-zeitbezug-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/normfassungen-und-zeitbezug-pruefen/SKILL.md) | Gleicht Normzitate mit zugänglichen amtlichen Originaltexten und dem maßgeblichen Zeitpunkt ab. Prüft Absatz, Nummer, Verweisung, Änderung und Übergangsrecht und liefert einen nachvollziehbaren Fassungs- und Anwendbarkeitsvermerk. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/normfassungen-und-zeitbezug-pruefen/SKILL.md) |
| [`pruefbericht-und-korrekturfassung-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/pruefbericht-und-korrekturfassung-erstellen/SKILL.md) | Erstellt aus einzeln belegten Quellenbefunden einen verständlichen juristischen Prüfbericht und eine nachvollziehbare Korrekturfassung. Erhält das Original, trennt ungeprüfte Stellen von Fehlern und verschleiert keinen Fundstellenwechsel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/pruefbericht-und-korrekturfassung-erstellen/SKILL.md) |
| [`uebertragbarkeit-und-gegenargumente-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/uebertragbarkeit-und-gegenargumente-pruefen/SKILL.md) | Prüft, ob eine im Originalvolltext gelesene Quelle die konkrete Fallargumentation trägt. Trennt tragende Gründe, Zusatzbemerkungen, Tatsachenunterschiede und Gegenargumente und liefert einen begründeten Übertragbarkeitsvermerk je Fundste... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/uebertragbarkeit-und-gegenargumente-pruefen/SKILL.md) |
| [`zitate-und-randnummern-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/zitate-und-randnummern-pruefen/SKILL.md) | Vergleicht wörtliche und sinngemäße Nachweise mit dem tatsächlich gelesenen amtlichen Fundpunkt. Erkennt falsche Randnummern, Seitenverwechslungen, sinnverändernde Auslassungen und die Verwechslung von Parteivortrag mit gerichtlicher Aus... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-halluzinationsreduzierer/skills/zitate-und-randnummern-pruefen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
