# 1. Liquiditätsplanung: Fachlicher und praktischer Abgleich

Stand: 28.09.2026. Dieser Bericht dokumentiert drei unterschiedliche Prüfarten am aktualisierten Arbeitsstand: die redaktionelle und quellenbezogene Prüfung der Anweisungen, die tatsächlich ausgeführten technischen Rechen- und Anwendungstests des technischen Teilauftrags sowie drei ausgeführte qualitative Agenten-Praxistests. Ihre Ergebnisse werden nicht zu einer vermeintlichen Gesamtpunktzahl zusammengezogen.

## 1.1. Auftrag und untersuchter Umfang

Untersucht wurden die Abgrenzung von Zahlungsunfähigkeit, drohender Zahlungsunfähigkeit und Überschuldung, die Behandlung von Titelforderungen und Rangrücktritten, die Reichweite der Fortbestehensprognose sowie ihre Umsetzung in Liquiditätswerkzeugen und Beratungstexten. Die Dokumentation beschränkt sich auf die dafür tatsächlich bearbeiteten Teile. Sie behauptet keine Vollprüfung sämtlicher Skills oder Rechtsfragen des Plugins.

Die drei juristischen Aufträge sind synthetische Qualitätsszenarien. Zahlen, Titel, Investorunterlagen und behauptete Belegvollständigkeit sind Vorgaben dieser Szenarien. Es wurden damit keine realen Unternehmenszahlen oder Prozessakten geprüft. Die lesbar ausgeschriebenen Aufträge und die unverändert übernommenen tatsächlich erzeugten Ergebnisse stehen unter [faelle](README.md#11-synthetische-qualitätsszenarien).

## 1.2. Prüfarten und Aussagekraft

| Prüfart | Tatsächliches Vorgehen | Was daraus folgt |
| --- | --- | --- |
| Redaktionelle und quellenbezogene Prüfung | Die Werkstatt, drei Fachskills, die Insolvenzreferenz und die Entscheidungskarte wurden gelesen. Tragende Aussagen wurden an lokalen amtlichen BGH-PDFs sowie aktuellen Normtexten überprüft. | Dies bewertet die Anweisungen und die Reichweite ihrer Quellen; es ist kein ausgeführter Berechnungstest. |
| Rechen- und Anwendungstests | Der technische Teilauftrag führte Node-Tests, einen Chrome-Browserlauf, Vorlagenvarianten mit nativer LibreOffice-Neuberechnung und Builder-Szenarien aus. Der [Rechenkern-Vermerk](rechenkern-pruefung.md) unterscheidet Berichtsaussagen, gespeicherte Ergebnisbelege und nachträglich nachvollzogene Artefakte. | Konkrete Rechen- und Bedienzustände wurden untersucht. Ihr Bestehen bescheinigt keine juristische Gesamtqualität. |
| Qualitative Agenten-Praxistests | Ein gesonderter Agent bearbeitete die drei konkreten Geschäftsführungsaufträge anhand der gelesenen Skills bis zu ausformulierten Kurzvermerken. | Dies zeigt die tatsächliche Anwendung des Workflows in diesen drei Läufen; es ist weder eine bloße Regelprüfung noch ein statistischer Benchmark. |

Die Praxisfälle wurden bewusst mit bekannten Fehlanreizen formuliert. Der bearbeitende Agent kannte die Aufgaben und die zu prüfenden Regelungsbereiche. Es gab keine zufällige Stichprobe, keine verdeckte Bewertung, keine Wiederholungsserie und keine unabhängige anwaltliche Abnahme der gesamten Ergebnisreihe. Ein künstlicher Erfolgsprozentsatz wäre daher nicht aussagekräftig.

## 1.3. Angewandter juristischer Workflow

Vor der Bearbeitung wurden die Repositoryregeln in `AGENTS.md` und `CLAUDE.md`, die zentrale Zitierregel sowie die [Werkstatt](../../../liquiditaetsplanung/liquiditaetsplanung-werkstatt.md) gelesen. Es folgten die Fachskills [Dreiwochenplanung](../../../liquiditaetsplanung/skills/liquiditaetsvorschau-3wochen/SKILL.md), [insolvenzrechtlicher Status](../../../liquiditaetsplanung/skills/liquiditaetsvorschau-insolvenzrechtlich/SKILL.md) und [rollierende Planung und Fortbestehensprognose](../../../liquiditaetsplanung/skills/liquiditaetsvorschau-3-6-12-monate/SKILL.md) sowie die [Insolvenzprüfregeln](../../../liquiditaetsplanung/references/insolvenzpruefung.md).

Die Bearbeitung übernahm Rolle, Stichtag und Auftrag aus der jeweiligen Eingabe. Sie ordnete die vorhandenen Zahlen und Tatsachen zu, bestimmte die Methode und den maßgeblichen Zeitraum, rechnete die entscheidbaren Positionen nach, prüfte tragende Rechtsaussagen am Original und beantwortete anschließend die konkrete Geschäftsführungsfrage. Fehlende Werte wurden nicht als null behandelt. Wo Informationen fehlten, wurde der dennoch entscheidbare Teil ausgearbeitet und die verbleibende Lücke konkret benannt.

Es wurden die verlangten Kurzvermerke mit geeigneten Rechen- oder Vergleichstabellen erstellt. Eine Tabellenmappe, ein Rangrücktrittsvertrag, ein Bankschreiben oder ein Insolvenzantrag war nicht Teil dieser drei Dokumentaufträge. Deshalb wurden solche zusätzlichen Produkte nicht als vermeintlich notwendiges Paket erzeugt.

## 1.4. Primärquellen und Rechtsstand

Die tragenden Passagen wurden in den lokalen amtlichen Original-PDFs gelesen. Die [Entscheidungskarte](../../../liquiditaetsplanung/references/rechtsprechung/INDEX.md) führt Originale, amtliche Links und Anwendungsgrenzen zusammen. Für diese Praxisfälle wurden insbesondere folgende Passagen herangezogen:

| Entscheidung | Für die Fallbearbeitung geprüfte Stelle |
| --- | --- |
| BGH, Beschl. v. 22.05.2025 – Az. IX ZB 38/24 | Rn. 10–18 behandeln die Titelbeweiswirkung bei wirksamer Einstellung und allein titelabhängigem Eröffnungsgrund. |
| BGH, Urt. v. 23.01.2025 – Az. IX ZR 229/22 | Rn. 34–43 behandeln objektiven Bestand, Fälligkeit sowie Titel- und Vollstreckungsbedingungen. |
| BGH, Urt. v. 28.04.2022 – Az. IX ZR 48/21 | Rn. 27–33 behandeln die Gesamtwürdigung der Zahlungseinstellung und die Aussagekraft verspäteter Sozialversicherungszahlungen. |
| BGH, Urt. v. 13.07.2021 – Az. II ZR 84/20 | Rn. 68–85 behandeln Prognosegrundlagen, Aktualisierung, Drittmittel und Patronate. |
| BGH, Urt. v. 19.12.2017 – Az. II ZR 88/16 | Rn. 50–53 und 68–70 behandeln neue Fälligkeiten und belastbare Mittelverfügbarkeit. |
| BGH, Urt. v. 05.03.2015 – Az. IX ZR 133/14 | Rn. 15–19 behandeln Rangtiefe und vorinsolvenzliche Durchsetzungssperre. |
| BGH, Urt. v. 12.10.2006 – Az. IX ZR 228/03 | Rn. 15–19 behandeln Stundungsbitten, Erklärung der Zahlungsunfähigkeit und die Grenzen der Entlastung durch Einzelzahlungen. |
| BGH, Urt. v. 24.05.2005 – Az. IX ZR 123/04 | Leitsätze b und c sowie Original-S. 14–16 behandeln die Zehnprozentregel und ihre Ausnahmen. Das amtliche PDF hat keine Randnummern. |

Die aktuellen Paragrafen 17, 18, 15a und 15b InsO wurden im amtlichen Normportal geprüft. Für die Paragrafen 19 und 39 wurde nach fehlgeschlagenem Einzelabruf der [amtliche Gesamttext](https://www.gesetze-im-internet.de/inso/InsO.pdf), S. 10 und 16, verwendet. Der heute geltende Zwölfmonatszeitraum wurde dem Gesetz entnommen und nicht dem Altfall II ZR 84/20 zugeschrieben. Die zukünftigen Szenariostichtage im Oktober 2026 wurden nach der am 28.09.2026 verifizierten Rechtslage beurteilt.

Literaturfundstellen innerhalb der Urteile wurden nicht als selbstständig geprüfte Literatur übernommen. Überlassene Manuskripttexte oder personenbezogene Nutzerinformationen sind nicht Bestandteil dieses Ordners.

## 1.5. Tatsächliche Ergebnisse der drei Agentenläufe

### 1.5.1. Achtprozentlücke und Antragspflicht

[Auftrag 1](faelle/01-auftrag.md) führte zu einer Rechnung mit Aktiva I von 92.000 EUR, Aktiva II von null, Passiva I von 100.000 EUR und Passiva II von 30.000 EUR. Die vollständige Bilanz ergibt 38.000 EUR Unterdeckung beziehungsweise 29,23 Prozent. Der tatsächliche Mittwoch blieb Stichtag; das Fenster wurde bis zum 18.11.2026 geführt.

[Ergebnis 1](faelle/01-ergebnis.md) verwirft eine Entwarnung aus der isolierten Achtprozentquote und begründet Zahlungsunfähigkeit spätestens am 28.10.2026. Die Dreiwochenbetrachtung und die Antragshöchstfrist wurden nicht aneinandergereiht. Der 18.11.2026 wird nur als äußerste Grenze bei erstmaligem Eintritt am 28.10.2026 bezeichnet. Der mögliche frühere Eintritt bleibt ausdrücklich gesondert aufzuklären; aus der Sachverhaltslage wird kein Recht zum Abwarten hergeleitet.

### 1.5.2. Rangrücktritt, Investor und Prognosehorizonte

[Auftrag 2](faelle/02-auftrag.md) führte zur getrennten Prüfung des Klauselwortlauts, des handelsbilanziellen Befunds, der Finanzierungsaussichten und der Zeithorizonte. [Ergebnis 2](faelle/02-ergebnis.md) lässt das Darlehen wegen fehlender ausreichender Rangtiefe und Durchsetzungssperre nicht aus dem Status herausrechnen. Die rechnerische Addition zum HGB-Eigenkapital wird nicht als Überschuldungsstatus ausgegeben.

Die Investorunterlagen werden als positive Anhaltspunkte gewürdigt. Das Fehlen eines einklagbaren Anspruchs führt nicht automatisch zu einer negativen Fortbestehensprognose. Ebenso wird aus der internen Mittelreservierung keine unbedingte Finanzierung der GmbH gemacht. Fehlende konkrete Beträge, Termine, Bedingungen und die unvollständig mitgeteilte Gesamtplanung begrenzen den abschließenden Befund.

Der fehlende 30.09.2027 wird ausdrücklich benannt. Für Paragraf 18 wird der Regelhorizont bis einschließlich 30.09.2028 angesetzt; Paragraf 17 bleibt gesondert. Die Antwort bescheinigt deshalb keine vollständige Prüfung sämtlicher Insolvenzgründe.

### 1.5.3. Titel, Einstellung und Indizien

[Auftrag 3](faelle/03-auftrag.md) führte zu einer zeitlich und rechtlich getrennten Behandlung der Aktiv- und Passivseite. [Ergebnis 3](faelle/03-ergebnis.md) behandelt den Kundentitel nicht als sicheren Zufluss. Die Lieferantenforderung ist vor der Einstellung bei erfüllten Voraussetzungen mit 40.000 EUR anzusetzen. Nach der als wirksam akzeptierten Einstellung verlangt der Vermerk eine konkrete materielle Prüfung; weder ein automatischer Nullansatz noch ein allein auf die frühere Vollstreckbarkeit gestützter abschließender Nachher-Befund wird ausgegeben.

Die regelmäßig vollständigen, 45 Tage verspäteten Sozialversicherungszahlungen und bloß bezeichneten Stundungsanfragen begründen keine automatische Zahlungseinstellung. Der Inhalt der Stundungsanfragen sowie die bekannten weiteren Umstände einschließlich Lieferantenvollstreckung und Sicherheitsleistung werden in die erforderliche Gesamtwürdigung einbezogen. Ohne Stichtag und vollständige Beträge wird keine Lückenquote erfunden.

## 1.6. Stärken, verbleibende Präzisierungen und Grenzen

Die konkrete Anwendung zeigt, dass die Anweisungen die drei vorgeschlagenen Fehlentscheidungen auffangen: die Freigabe anhand eines isolierten Prozentwerts, die pauschale Verrechnung beziehungsweise Ablehnung einer Finanzierungsprognose und die Gleichsetzung von Titeln oder Indizienanzahl mit einem Insolvenzbefund. Die örtlichen Original-PDFs erleichtern die Prüfung der tatsächlichen Reichweite der Rechtsprechung. Die Ausformulierungspflicht führt bis zum bestellten Vermerk, obwohl zwei Szenarien entscheidende offene Punkte enthalten.

In diesen drei Arbeitsgängen trat kein materieller Anweisungsdefekt hervor, der eine der falschen Schlussfolgerungen erzwang oder nahelegte. Das ersetzt keine Prüfung anderer Fallgestaltungen. Die offenen Betrags- und Urkundeninhalte der Fälle 2 und 3 sind Grenzen der Eingaben und keine behaupteten Pluginfehler.

Aus den Läufen ergaben sich zwei praktische Präzisierungen, die die Hauptbearbeitung vor Abschluss in den Fachskills ergänzt hat. Der Insolvenzskill verlangt nun ausdrücklich die Gegenüberstellung vor und nach Wirksamwerden einer Einstellung sowie die Abstimmung gebundener Sicherheitsmittel. Der Langfristskill enthält ein positives Beispiel einer noch nicht einklagbaren, aber durch konkrete Prüfung und Mittelreservierung unterlegten Finanzierung. Die zuvor gelesenen allgemeinen Regeln trugen diese Bearbeitung bereits; die Ergänzungen werden deshalb als Präzisierungen und nicht als nachträglich geheilte Rechtsfehler der drei Ausgaben eingeordnet. Die übernommenen Ergebnisdateien wurden dafür nicht umgeschrieben.

Davon zu unterscheiden ist der tatsächlich reproduzierte technische Builder-Fehler bei unvollständigen Vorwochen. Er konnte spätere Fenster trotz unsicherem Anfangsbestand freigeben. Er wurde korrigiert und mit einem negativen sowie einem positiven nativen Gegenfall geprüft. Der abschließende Lauf umfasst acht erfolgreiche Builder-Szenarien; die elf Padlet-Rechenfälle wurden ebenfalls erfolgreich wiederholt. Beide Protokolle liegen unter `belege/`.

Die Ergebnisse dokumentieren einen tatsächlichen qualitativen Arbeitsgang je Auftrag. Es wurde kein eingefrorener Gesamtsnapshot aller Modell- und Laufzeitparameter angelegt. Der Arbeitsstand wurde im Team weiterbearbeitet. Das [Dateimanifest](belege/dateimanifest.json) sichert die Dokumente und übernommenen technischen Belege bei ihrer Archivierung. Der [Archivierungsstand](belege/archivierungsstand.json) hält zusätzlich die Hashes der relevanten finalen Plugin- und Testdateien fest. Diese Nachweise beweisen keinen vollständigen deterministischen Wiederholungslauf der juristischen Agentenbearbeitung. Aus den drei Fällen folgt weder eine Fehlerfreiheit des Plugins noch eine Erfolgsquote.

## 1.7. Nachprüfung und Dokumentationsumfang

Die Fallaufträge und tatsächlichen Ausgaben stehen vollständig in diesem Ordner. Die drei technischen JSON-Belege sowie die beiden abschließenden Testprotokolle sind übernommen und mit Hashes dokumentiert. Die Repo-Testbefehle und ihre Voraussetzungen stehen im [Rechenkern-Vermerk](rechenkern-pruefung.md#14-wiederholbare-repo-prüfungen). Ein neuer Lauf kann dadurch von den hier dokumentierten Ergebnissen getrennt aufgezeichnet werden. Zusätzlich im Prüfprofil hinterlegte Aufgaben sind künftige beziehungsweise getrennte Prüfvorgaben; ihr Vorhandensein wird nicht als weiterer bestandener Agentenlauf gezählt.

Vor Abschluss wurden die Dateiliste, relative Verweise und die übernommenen Hashes geprüft. Die Dateiinhalte enthalten keine privaten absoluten Benutzerpfade und keine überlassenen Manuskriptpassagen. Es wurden in diesem Dokumentationsteil ausschließlich Dateien in diesem neu angelegten Qualitätsordner geschrieben. Die abschließende Prüfung mit `git diff --check` sowie eine gesonderte Leerraumprüfung der neuen Dateien ergaben keinen Befund. Die Gesamtänderung und ein etwaiger Commit bleiben dem Hauptauftrag vorbehalten.
