# 1. Quellen- und Werkzeugvermerk

## 1.1. Tatsächlich verwendete Werkzeuge

`functions.exec` wurde als Aufrufhülle verwendet. Darin wurden ausschließlich `tools.exec_command` und `tools.web__run` aufgerufen.

`tools.exec_command` wurde für das Lesen von AGENTS.md, CLAUDE.md und des Kanzlei-Schnellstarts, die Dateiliste mit `rg --files`, das Lesen der nachstehend genannten Referenzen und Skills mit `cat` beziehungsweise `sed`, die Erstellung dieses temporären Ergebnisverzeichnisses, eine Python-Datumskontrolle sowie das Schreiben und anschließende Lesen der Ergebnisdateien verwendet. Mehrere unabhängige Leseaufrufe wurden mit `Promise.allSettled` zusammengefasst; umfangreiche Ausgaben waren teilweise vom Werkzeug gekürzt. Es wurden keine Repositorydateien geändert und keine Git-Befehle ausgeführt.

`tools.web__run` wurde mit `open`, `search_query`, `click` und `find` für amtliche Normen, Berliner Feiertagsinformationen und Veröffentlichungen der BRAK verwendet. Die Suchausgaben enthielten auch nichtamtliche Treffer; diese wurden nicht als Belege übernommen. Zwei bezeichnete amtliche BGH-PDFs waren nicht abrufbar. Mehrere Einzelnormabrufe endeten mit einem Abruffehler; insoweit wurden erfolgreiche Suchauszüge oder amtliche Gesamttexte genutzt. Es wurden keine Suchmaschinen-Snippets als gelesene Entscheidungsrandnummern ausgegeben.

`collaboration.send_message` wurde einmal verwendet, um dem übergeordneten Agenten ausschließlich den Bearbeitungsstand und das temporäre Ausgabeverzeichnis mitzuteilen. Es wurden keine anderen Agentenergebnisse gelesen und keine Unteragenten mit Fachbearbeitung beauftragt.

Kein Kanzleihelfer wurde ausgeführt: `kanzlei.py`, `mandatslauf.py` und `fristen.py` wurden nicht aufgerufen. Ebenso wurden kein Mandatsordner, kein Kalender, kein beA, keine E-Mail, kein Bankzugang und kein Buchhaltungssystem geöffnet oder geändert. Es wurden keine Kalender-, Journal-, Rechnungs-, Versand-, Zahlungs-, Archivierungs- oder Löschvorgänge simuliert als tatsächlich vollzogen dargestellt.

## 1.2. Zulässig gelesene lokale Unterlagen

Das Arbeitsverzeichnis war `/Users/klotzkette/Desktop/Codex Projects/legal-work/ki-kanzlei-glaettung-20261008`.

Gelesen wurden AGENTS.md, CLAUDE.md und `ki-native-kanzlei/ki-native-kanzlei-schnellstart.md` sowie `references/zitierweise.md`, `ki-native-kanzlei/references/mandatslauf-und-freigaben.md` und `ki-native-kanzlei/references/kanzleialltag-workflows.md`.

Die passenden Fachskills waren `ki-kanzlei-steuern`, `fristen-berechnen-ueberwachen`, `schriftsaetze-entwerfen`, `zeiten-erfassen`, `abrechnung-e-rechnung` und `mandat-abschliessen`, jeweils `ki-native-kanzlei/skills/<Name>/SKILL.md`. Weitere Skillnamen wurden nur in der Dateiliste sichtbar. Keine quality-Datei, kein vorheriger Probelauf, kein Git-Diff und kein fremdes Ergebnis wurde geöffnet.

## 1.3. Quellen, die die Arbeitsprodukte tragen

Der tatsächliche Abruf erfolgte am 08.10.2026. Die Fristberechnung verwendet den simulierten Sachverhaltsstand 23.03.2026. Die Daten der amtlichen Osterübersicht wurden zusätzlich mit einer eigenen Datumsrechnung abgeglichen. Eine vollständige historische Gesetzessynopse wurde nicht erzeugt.

| Gegenstand | Tatsächlich zugängliche Primärquelle |
|---|---|
| Einspruchsfrist | [§ 339 ZPO](https://www.gesetze-im-internet.de/zpo/__339.html), amtlicher Suchauszug mit Normtext. |
| Beginn und Ende | [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html), [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html) und [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html). |
| Einspruchsschrift | [ZPO-Gesamttext als PDF mit § 340](https://www.gesetze-im-internet.de/zpo/ZPO.pdf), im amtlichen Suchergebnis ausgelesener Normtext. |
| Elektronische Einreichung | [Amtlicher ZPO-Gesamttext mit §§ 130a und 130d](https://www.gesetze-im-internet.de/zpo/BJNR005330950.html). |
| Anwaltsvertretung | [§ 78 ZPO](https://www.gesetze-im-internet.de/zpo/__78.html). |
| Berliner Feiertagsrecht | [Senatsverwaltung für Inneres: Sonn- und Feiertagsrecht](https://www.berlin.de/sen/inneres/buerger-und-staat/verfassungs-und-verwaltungsrecht/artikel.1435639.php). |
| Osterdaten 2026 | [Amtliche Jahresübersicht des Bezirksamts Lichtenberg](https://www.berlin.de/ba-lichtenberg/politik-und-verwaltung/bezirksverordnetenversammlung/wissenswertes/ds-1470-ix_anlage-jahresuebersicht-sitzungstermine-2026.pdf), zugänglicher amtlicher Suchauszug. |
| Form der Vergütungsvereinbarung | [§ 3a RVG](https://www.gesetze-im-internet.de/rvg/__3a.html). |
| Form und Inhalt der Berechnung | [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html). |
| Fremde Vermögenswerte | [§ 43a Absatz 7 BRAO](https://www.gesetze-im-internet.de/brao/__43a.html). |
| Fremdgeld und Zweckbindung | [BORA, Stand 01.12.2025, § 4](https://www.brak.de/fileadmin/02_fuer_anwaelte/berufsrecht/033-BORA_Stand_01.12.2025.pdf), über die BRAK-Seite geöffnet und betreffenden Text gelesen. |
| Handakte, Herausgabe, Aufbewahrung | [§ 50 BRAO](https://www.gesetze-im-internet.de/brao/__50.html). |
| Steuerliche Aufbewahrung | [Amtlicher AO-Gesamttext, § 147](https://www.gesetze-im-internet.de/ao_1977/BJNR006130976.html), betreffenden Abschnitt über Textsuche geöffnet. |

## 1.4. Nicht erfolgreich verifizierte Entscheidungsquellen

Die PDF-Adressen des BGH zu Beschluss vom 04.03.2026, Az. XII ZB 338/24, und Urteil vom 19.02.2026, Az. IX ZR 226/22, wurden geöffnet, antworteten aber mit „Forbidden“. Weitere Suche lieferte keinen erfolgreich geöffneten amtlichen Volltext dieser beiden Entscheidungen. Deshalb werden die Randnummern aus dem Kanzleiprompt nicht als selbst verifiziert übernommen. Die Arbeitsprodukte benennen diese Grenze ausdrücklich und setzen unabhängig davon die kontrollierbare Fristkorrektur sowie die fehlende Honorarerweiterung um.

## 1.5. Eigene Rechenkontrolle

Python `datetime.date(2026,3,20) + datetime.timedelta(weeks=2)` ergab den 03.04.2026 als Freitag. Die anschließende Feiertagsverschiebung wurde anhand der gesetzlichen Regel und der Berliner Feiertagsdaten manuell geprüft. Python bestätigte zudem 42/60 = 0,70 Stunden und den ausschließlich bedingten Vergleichswert 0,70 × 260 = 182,00 EUR. Es wurden weder Anwaltminuten aus einer Werkzeuglaufzeit abgeleitet noch Preise ohne Vereinbarung angesetzt.
