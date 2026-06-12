# Megaprompt: arbeitszeugnis-analyse

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 50 Skills des Plugins `arbeitszeugnis-analyse`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Arbeitszeugnis-Analyse: ordnet Rolle (Mandant/Arbeitnehmer, Arbeitgeber/HR, Vorgesetzte…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Workflow-Steuerung für das Arbeitszeugnis-Analyse-Plugin. Erkennt Zeugnisart, Ziel, Fristen,…
3. **geheimcode-katalog** — Zentraler Referenzkatalog aller Standardformulierungen im deutschen Arbeitszeugnis mit Ampelzuordnung. Anwendungsfall An…
4. **klage-strategie-zeugnisberichtigung** — Strategie und Antragsformulierungen für die Zeugnisberichtigungsklage vor dem Arbeitsgericht. Anwendungsfall außergerich…
5. **erstgespraech-und-mandatsannahme** — Mandatsannahme im Zeugnisrecht mit Erstgespraech Unterlagenerfassung und Fristen-Erstprognose. Anwendungsfall Arbeitnehm…
6. **rechtliche-bewertung-bag-rechtsprechung** — Rechtliche Einordnung von Zeugnisansprüchen nach § 109 GewO und BAG-Rechtsprechung für die anwaltliche Praxis. Anwendung…
7. **branchen-spezifische-formulierungen** — Decodiert branchenspezifische Formulierungen im Arbeitszeugnis zur praezisen Noteneinordnung. Anwendungsfall Zeugnis ent…
8. **zeugnisart-erkennung** — Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse…
9. **zeugnis-ueberblick-extraktion** — Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde ho…
10. **azubi-zeugnis-analyse** — Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubild…
11. **gesamtnoten-aggregation** — Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Ei…
12. **notenrelevante-saetze-identifizieren** — Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfal…
13. **satzweise-notenmatrix** — Bewertet jeden notenrelevanten Satz eines Arbeitszeugnisses mit Schulnote 1 bis 5. Anwendungsfall notenrelevante Saetze …
14. **muster-arbeitszeugnis-note-1** — Vollständiges Musterarbeitszeugnis Note 1 als Referenzdokument für Vergleich und Berichtigung. Anwendungsfall Anwalt ode…
15. **muster-arbeitszeugnis-gemischte-noten** — Anonymisiertes Schulungszeugnis mit Schaufenster-Pattern für Training und Demonstration. Anwendungsfall Rechtsanwalt ode…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Arbeitszeugnis-Analyse: ordnet Rolle (Mandant/Arbeitnehmer, Arbeitgeber/HR, Vorgesetzte), markiert Frist (BAG 5.7.2018 – 9 AZR 244/17 Anspruch entstehung), wählt Norm (§ 109 GewO Wohlwollensgrundsatz, § 109 II GewO Wahrheits-/Klarheitspflicht, BGB §§ 241 II, 280 I Nebenpflicht) und Zuständigkeit (Arbeitsgericht), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Arbeitszeugnis Analyse** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `ampelsystem-tabellenausgabe` — Ampelsystem Tabellenausgabe
- `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste` — Arbeitszeugnis Ampelsystem Dokumentenmatrix Lueckenliste
- `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk` — Arbeitszeugnis Codeworte Compliance Dokumentation Aktenvermerk
- `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen` — Arbeitszeugnis Deutscher Tatbestandsmerkmale Beweisfragen
- `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine` — Arbeitszeugnis Geheimcodes Schriftsatz Brief Memo Bausteine
- `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` — Arbeitszeugnis Gruen Behoerden Gerichts Registerweg
- `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung` — Arbeitszeugnis Negative Zahlen Schwellenwerte Berechnung
- `arbeitszeugnis-orange-risikoampel-gegenargumente` — Arbeitszeugnis Orange Risikoampel Gegenargumente
- `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation` — Arbeitszeugnis Schaufenster Verhandlung Vergleich Eskalation
- `arbeitszeugnis-zeugnisanalyse-wortlaut-codes` — Arbeitszeugnis Zeugnisanalyse Wortlaut Codes
- `aufforderungsschreiben-arbeitgeber` — Aufforderungsschreiben Arbeitgeber
- `azubi-zeugnis-analyse` — Azubi Zeugnis Analyse
- `bereichs-drift-detektor` — Bereichs Drift Detektor
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Arbeitszeugnis Analyse sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.


## Leitentscheidungs-Anker (Uebersicht, vor Schriftsatzverwendung live verifizieren)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast fuer bessere Note beim Arbeitnehmer, fuer schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast fuer bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Aenderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |


## Sofortstart und Rueckfrage-Disziplin

**Der haeufigste Fall ist der einfachste: jemand fuegt ein Zeugnis ein - sonst nichts.** Dann gilt:

1. **Sofort loslegen.** Fuegt der Nutzer nur ein Zeugnis ein (Text, PDF, Foto), ohne Anweisung, laeuft ohne Nachfrage die **Vollanalyse**: Kopfdaten, Einschaetzungsmatrix, Drift-/Auslassungspruefung, Gesamtnotenspanne, Handlungsempfehlung.
2. **Fehlende Angaben sind kein Blocker.** Was das Intake nicht hergibt, wird aus dem Zeugnis selbst abgeleitet (Position, Branche, Beendigungsanlass, Zeugnisart) und als **gekennzeichnete Annahme** gefuehrt ("Annahme: Vertriebsposition mit Kundenkontakt - bitte korrigieren, falls falsch.").
3. **Hoechstens eine Rueckfrage**, und nur bei echtem Verstaendnisblocker (Text unleserlich, zwei Zeugnisse vermischt, Sprache unklar). Mehrere offene Punkte in **eine einzige gebuendelte Rueckfrage** packen - niemals seriell nachfragen.
4. **Wuenschefragen ans Ende.** Ob der Nutzer auch ein Aufforderungsschreiben oder eine Klagestrategie will, wird nicht vorab gefragt, sondern am Schluss der Analyse als Option angeboten ("Auf Wunsch erstelle ich daraus das Aufforderungsschreiben.").
5. **Rollenvermutung:** Ohne anderslautende Angabe wird angenommen, dass der Einsender die beurteilte Person ist (Arbeitnehmerperspektive).

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Workflow-Steuerung für das Arbeitszeugnis-Analyse-Plugin. Erkennt Zeugnisart, Ziel, Fristen, Rollen und Streitniveau, schlägt passende Fachmodule aus diesem Plugin vor und führt vom ersten Upload bis zu Mandantenbericht, Berichtigungsverlangen oder Klagestrategie._

## Wenn nur ein Zeugnis hochgeladen wird

Wenn der Nutzer nur ein PDF, Foto, Screenshot oder Textauszug hochlädt, beginne direkt. Keine generische Empfangsbestätigung, keine lange Intake-Liste.

**Erste Antwort:**

- **Erkannt:** Zeugnisart, Arbeitgeber, Arbeitnehmer, Zeitraum, Datum, Seitenumfang, soweit sichtbar.
- **Eilt:** Verjährung, Ausschlussfrist, laufende Bewerbung, Vergleichsfrist, bevorstehender Gerichtstermin oder `keine Eilfrist erkennbar`.
- **Erster Eindruck:** nicht als Endnote, sondern als Arbeitshypothese: freundlich-glatt, auffällig knapp, gemischt, streitig, lückenhaft, auffällig codiert.
- **Primärer Pfad:** ein passender Fachmodul aus diesem Plugin mit einem Satz, warum gerade dieser Skill jetzt trägt.
- **Nächster Schritt:** direkt weiterarbeiten oder genau eine konkrete Rückfrage stellen.

## Intake in 60 Sekunden

Frage nur, was den Weg ändert. Wenn die Information schon im Material steht, fasse sie zusammen und frage nicht erneut.

| Punkt | Frage |
|---|---|
| Rolle | Arbeitnehmer, Anwalt/Kanzlei, Betriebsrat, Arbeitgeber, Personalabteilung oder Rechtsabteilung? |
| Ziel | Nur verstehen, nachverhandeln, Arbeitgeber anschreiben, Klage prüfen, Vergleichstext bauen oder Schulungsfall analysieren? |
| Zeugnisart | Einfaches Zeugnis, qualifiziertes Endzeugnis, Zwischenzeugnis, Ausbildungszeugnis oder Entwurf? |
| Zeitpunkt | Wann ausgestellt, wann erhalten, gibt es Bewerbungs- oder Vergleichsdruck? |
| Kontext | Kündigung, Aufhebungsvertrag, Eigenkündigung, Elternzeit, Wechsel, Ruhestand, Streit oder gute Trennung? |
| Vergleichsmaterial | Vorzeugnis, Zwischenzeugnis, Beurteilungen, Zielvereinbarungen, Bonusunterlagen, E-Mails mit Lob, Vergleichstext? |

## Fünf Arbeitswege

Wähle einen dieser Wege und sage dem Nutzer, welchen Weg du nimmst.

1. **Schnellscan:** Für eine erste Einschätzung. Nutze `zeugnisart-erkennung`, `zeugnis-ueberblick-extraktion`, `zufriedenheitsformel-decodierung` und `schlussformel-bewertung`.
2. **Vollanalyse:** Für belastbare Mandatsarbeit. Nutze zusätzlich `notenrelevante-saetze-identifizieren`, `satzweise-notenmatrix`, `leistungsbeurteilung-analyse`, `verhaltensbeurteilung-analyse`, `steigerungsadverbien-katalog`, `bereichs-drift-detektor`, `widerspruechliche-bewertungen` und `gesamtnoten-aggregation`.
3. **Verhandlung:** Wenn ein besseres Zeugnis erreicht werden soll. Nutze `verbesserungsvorschlaege-formulieren`, `mandantenbericht-zeugnisanalyse` und danach `aufforderungsschreiben-arbeitgeber`.
4. **Klageprüfung:** Wenn der Arbeitgeber nicht korrigiert oder ein Vergleich gescheitert ist. Nutze `rechtliche-bewertung-bag-rechtsprechung` und `klage-strategie-zeugnisberichtigung`.
5. **Sonderfall:** Bei Führungskräften, Ausbildung oder branchentypischen Codes nutze früh `leitende-positionen-zeugnisse`, `azubi-zeugnis-analyse` oder `branchen-spezifische-formulierungen`.

## Routing nach Befund

| Befund | Nächster Skill | Warum |
|---|---|---|
| Zeugnisart oder Kopfdaten unklar | `zeugnisart-erkennung`, `zeugnis-ueberblick-extraktion` | Erst wissen, welches Dokument geprüft wird. |
| Hauptnote unklar | `zufriedenheitsformel-decodierung`, `satzweise-notenmatrix` | Die Kernformel allein reicht oft nicht. |
| Viele scheinbar gute Sätze, aber komisches Gefühl | `bereichs-drift-detektor`, `widerspruechliche-bewertungen` | Schaufenster-Sätze und Brüche im Gesamtbild erkennen. |
| Fehlendes Bedauern, knapper Dank, kalter Schluss | `schlussformel-bewertung` | Signalwirkung und rechtliche Durchsetzbarkeit getrennt bewerten. |
| Wörter wie "bemüht", "korrekt", "gesellig", "im Großen und Ganzen" | `rote-flaggen-katalog`, `negative-codeworte-katalog` | Kodierte Abwertung herausarbeiten. |
| Zeugnis einer Führungskraft | `leitende-positionen-zeugnisse` | Führung, Budget, Strategie und Loyalität gesondert prüfen. |
| Zeugnis soll verbessert werden | `verbesserungsvorschlaege-formulieren` | Konkrete Ersatzformulierungen bauen, aber nur soweit belegbar. |
| Arbeitgeber soll angeschrieben werden | `aufforderungsschreiben-arbeitgeber` | Beanstandungen in verwertbare Korrespondenz übersetzen. |
| Gerichtliche Durchsetzung steht im Raum | `rechtliche-bewertung-bag-rechtsprechung`, `klage-strategie-zeugnisberichtigung` | Beweislast, Antrag und Kostenrisiko sauber trennen. |

## Juristische Leitplanken

- **§ 109 GewO:** Anspruch auf einfaches oder qualifiziertes Zeugnis; bei qualifiziertem Zeugnis Angaben zu Leistung und Verhalten.
- **§ 16 BBiG:** Ausbildungszeugnis; auf Verlangen auch Angaben zu Verhalten und Leistung.
- **Wahrheit vor Wohlwollen:** Ein gutes Zeugnis darf nicht unwahr sein. Wohlwollen steuert die Ausdrucksweise, ersetzt aber keine Tatsachen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Geheimcode:** Nicht jede unglückliche Formulierung ist automatisch ein unzulässiger Code. Prüfe den objektiven Empfängerhorizont und den Gesamtzusammenhang.
- **Keine Mathematik-Illusion:** Ampel, Note und Drift sind Arbeitsinstrumente. Die Ausgabe muss als begründete Spanne erscheinen, nicht als Scheingenauigkeit.

## Antwortformate

### Kurzscan

**Kurzbild**
- Zeugnisart:
- Erste Notentendenz:
- Kritische Stellen:
- Eilt wegen:

**Nächster sinnvoller Skill**
`skill-name` - kurzer Grund.

### Vollanalyse

**Arbeitsplan**
1. Kopfdaten und Zeugnisart sichern.
2. Notenrelevante Sätze markieren.
3. Leistung, Verhalten, Schluss und Auslassungen getrennt bewerten.
4. Drift und Widersprüche prüfen.
5. Gesamtnotenspanne bilden.
6. Handlungsoptionen und konkrete Ersatzformulierungen ausgeben.

**Fachmodule**
Nenne zwei bis fünf Skills, nicht die ganze Plugin-Liste. Zu jedem Skill: Input, Zweck, Output.

### Mandatsoutput

Wenn der Nutzer anwaltliche Weiterverarbeitung will, liefere:

- Zusammenfassung für Mandant oder Mandantin.
- Streitstellen mit Originalwortlaut und gewünschter Neufassung.
- Beweislast und Belegbedarf pro Streitstelle.
- Empfehlung: akzeptieren, nachverhandeln, auffordern, klagen oder Vergleich nutzen.

## Qualitätsgate

Vor jeder abschließenden Antwort prüfe:

- Sind Umlaute, ß, Namen, Daten und Zitate sauber übernommen?
- Ist die Zeugnisart korrekt bestimmt?
- Sind Schlussformel-Signal und Schlussformel-Anspruch getrennt?
- Ist die Beweislast richtig herum dargestellt?
- Gibt es keine erfundenen Fundstellen, Zeugnisinhalte oder Noten?
- Sind die vorgeschlagenen Skills wirklich aus diesem Plugin?
- Wirkt das Ergebnis wie eine verwendbare anwaltliche Arbeitsfassung und nicht wie ein Schema?

## Testakten nutzen

Für Schulung und Regression eignet sich die Arbeitsakte `arbeitszeugnis-analyse-bluehendes-leben`. Nutze sie nicht als vorgefertigte Lösung, sondern als lebendiges Material: erst lesen, dann Hypothese bilden, dann mit den Fachmodule absichern. Die Fälle sollen zeigen, dass Arbeitszeugnisse oft höflich aussehen und trotzdem in einzelnen Abschnitten hart abwerten.


## Leitentscheidungs-Anker (Uebersicht, vor Schriftsatzverwendung live verifizieren)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast fuer bessere Note beim Arbeitnehmer, fuer schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast fuer bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Aenderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |


## Sofortstart und Rueckfrage-Disziplin

**Der haeufigste Fall ist der einfachste: jemand fuegt ein Zeugnis ein - sonst nichts.** Dann gilt:

1. **Sofort loslegen.** Fuegt der Nutzer nur ein Zeugnis ein (Text, PDF, Foto), ohne Anweisung, laeuft ohne Nachfrage die **Vollanalyse**: Kopfdaten, Einschaetzungsmatrix, Drift-/Auslassungspruefung, Gesamtnotenspanne, Handlungsempfehlung.
2. **Fehlende Angaben sind kein Blocker.** Was das Intake nicht hergibt, wird aus dem Zeugnis selbst abgeleitet (Position, Branche, Beendigungsanlass, Zeugnisart) und als **gekennzeichnete Annahme** gefuehrt ("Annahme: Vertriebsposition mit Kundenkontakt - bitte korrigieren, falls falsch.").
3. **Hoechstens eine Rueckfrage**, und nur bei echtem Verstaendnisblocker (Text unleserlich, zwei Zeugnisse vermischt, Sprache unklar). Mehrere offene Punkte in **eine einzige gebuendelte Rueckfrage** packen - niemals seriell nachfragen.
4. **Wuenschefragen ans Ende.** Ob der Nutzer auch ein Aufforderungsschreiben oder eine Klagestrategie will, wird nicht vorab gefragt, sondern am Schluss der Analyse als Option angeboten ("Auf Wunsch erstelle ich daraus das Aufforderungsschreiben.").
5. **Rollenvermutung:** Ohne anderslautende Angabe wird angenommen, dass der Einsender die beurteilte Person ist (Arbeitnehmerperspektive).

---

## Skill: `geheimcode-katalog`

_Zentraler Referenzkatalog aller Standardformulierungen im deutschen Arbeitszeugnis mit Ampelzuordnung. Anwendungsfall Anwalt oder Arbeitnehmer will eine Zeugnisformulierung einordnen und weiss nicht ob sie positiv neutral oder negativ kodiert ist. Normen § 109 GewO Wahrheits- und Wohlwollenspflicht BAG-Rechtsprechung Zeugnissprache. Themen Leistung Verhalten Engagement Belastbarkeit Teamarbeit Führung Schlussformel. Output Ampeltabelle mit Notentendenzen Erlaeuterungen und Alternativformulierungen für Berichtigungsverlangen. Abgrenzung zu rote-flaggen-katalog orange-flaggen-katalog und gruen-flaggen-katalog (spezialisierte Teilkataloge)._

# Geheimcode-Katalog der Zeugnissprache

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

### Leistung und Arbeitsqualität

| Formulierung | Bedeutung | Ampel |
|---|---|---|
| "stets einwandfreie Arbeitsergebnisse" | Höchste Qualität | Grün |
| "sorgfältig und gewissenhaft" | Sehr gute Qualität | Grün |
| "hat die Aufgaben sorgfältig erledigt" | Befriedigend | Orange |
| "bemüht, die Aufgaben zu erfüllen" | Guter Wille, schlechtes Ergebnis | Rot |
| "im Wesentlichen ordnungsgemäß" | Erhebliche Mängel | Rot |

### Engagement und Motivation

| Formulierung | Bedeutung | Ampel |
|---|---|---|
| "stets einsatzbereit und motiviert" | Hohe Motivation | Grün |
| "mit großem Engagement" | Gute Motivation | Grün |
| "zeigte Interesse an seinen Aufgaben" | Mäßige Motivation | Orange |
| "war bemüht" | Fehlende Ergebnisse | Rot |
| "erledigte Aufgaben nach Anweisung" | Keine Eigeninitiative | Rot |

### Belastbarkeit

| Formulierung | Bedeutung | Ampel |
|---|---|---|
| "auch unter Druck stets souverän" | Sehr belastbar | Grün |
| "zuverlässig auch in Stressphasen" | Gut belastbar | Grün |
| "hat Belastungen gut gemeistert" | Ausreichend belastbar | Orange |
| "gelegentlich überfordert" (implizit) | Geringe Belastbarkeit | Rot |

### Teamarbeit

| Formulierung | Bedeutung | Ampel |
|---|---|---|
| "hervorragendes Teammitglied" | Note 1-2 | Grün |
| "teamfähig und kollegial" | Note 2-3 | Grün/Orange |
| "hat sich ins Team integriert" | Note 3-4 | Orange |
| "hatte eine eigenständige Arbeitsweise" | Schwierig im Team | Rot |

## Beispiele

**Beispiel 1 – Positivkette:** "stets einsatzbereit, sorgfältig, belastbar, kollegial, zuverlässig" → durchgehend grüne Kette, Note 1-2.

**Beispiel 2 – Negativkette:** "bemüht, eigenständig, hat die Erwartungen erfüllt, direkte Kommunikationsweise" → durchgehend rote Signale, Note 4-5.

**Beispiel 3 – Gemischtes Zeugnis:** Leistungsformulierungen grün, Verhaltensformulierungen orange → Gesamtnote Note 2-3 mit Anmerkung zur sozialen Komponente.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Wohlwollensgebot; auch wahre kodierte Aussagen sind berichtigungspflichtig, wenn sie Fortkommen unnötig erschweren
- **§ 109 Abs. 2 GewO** — Klarheitspflicht; versteckter Code, der nur Eingeweihten verständlich ist, verletzt Transparenzanforderung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `klage-strategie-zeugnisberichtigung`

_Strategie und Antragsformulierungen für die Zeugnisberichtigungsklage vor dem Arbeitsgericht. Anwendungsfall außergerichtliches Berichtigungsverlangen ist gescheitert und Klage soll eingereicht werden. Normen § 109 GewO Berichtigungsanspruch § 46 ArbGG Verfahren § 253 ZPO Klageantrag BAG-Beweislastverteilung. Prüfraster Streitwertberechnung Klageantrag mit Wortlautformulierung Fristen Verjährung außergerichtliche Phase Kostenrisiko. Output Klageschrift-Baustein mit Antrag Sachverhalt Zeugnisanalyse Beweisangeboten und Kostenantrag. Abgrenzung zu aufforderungsschreiben-arbeitgeber (außergerichtlich) und schriftsatzkern-substantiierung._

# Klagestrategie Zeugnisberichtigung

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

### Erfolgsaussichten je Befundtyp

| Befund | Klagbarkeit | Erfolgsaussicht |
|---|---|---|
| "bemueht" als Leistungsformel | Klagbar | Hoch |
| Falsche Reihenfolge im Sozialverhalten | Klagbar | Hoch |
| Unvollständige Schlussformel | Meist Verhandlungspunkt, Klage nur mit Zusatzkontext | Niedrig bis Mittel |
| Negatives Codewort aus dem Codeworte-Katalog | Klagbar | Hoch |
| Drift im selben Themenbereich | Klagbar (bei nachgewiesenem Schaufenster) | Mittel |
| Konstante Note 3 in weichen Bereichen | Klagbar bei Wohlwollensverstoss | Mittel |
| Note 3 bei aktenkundig besserer Leistung | Klagbar (Arbeitnehmer beweisbelastet) | Mittel |
| Note 4 im Standardfall | Klagbar (Arbeitgeber beweisbelastet) | Hoch |

### Beweislastregel

| Streitfrage | Beweislast |
|---|---|
| Note schlechter als befriedigend | Arbeitgeber |
| Note besser als befriedigend | Arbeitnehmer |
| Wohlwollensverstoss | Arbeitnehmer |
| Wahrheitsverstoss | Arbeitnehmer |
| Sozialverhalten-Reihenfolge | Arbeitgeber muss falsche Reihenfolge begruenden |

### Streitwert

| Klagegegenstand | Streitwert |
|---|---|
| Vollstaendige Zeugnisberichtigung | ein Monatsbruttogehalt |
| Einzelne Note im Hauptteil | ein Monatsbruttogehalt |
| Schlussformel-Korrektur | ein Drittel bis ein Halbes Monatsgehalt |
| Mehrere Punkte | ein Monatsbruttogehalt insgesamt |
| Erstmalige Erteilung des Zeugnisses | ein Monatsbruttogehalt |

## Beispiele

### Beispiel 1 – Aussergerichtliches Berichtigungsverlangen

Sehr geehrte Damen und Herren,

das mir unter dem aktuellen Datum erteilte Arbeitszeugnis habe ich erhalten. Mit folgenden Formulierungen bin ich nicht einverstanden und bitte um Berichtigung mit den jeweils vorgeschlagenen Wortlauten:

Statt "war stets bemueht, die ihm uebertragenen Aufgaben zur vollen Zufriedenheit zu erledigen": "erledigte die ihm uebertragenen Aufgaben stets zu unserer vollen Zufriedenheit".

Statt "sein Verhalten gegenueber Kollegen und Vorgesetzten war korrekt": "sein Verhalten gegenueber Vorgesetzten, Kollegen und Kunden war stets einwandfrei".

Als Vergleichsvorschlag zur knappen Schlussformel: "Wir bedauern sein Ausscheiden, danken ihm für die geleistete Arbeit und wünschen ihm für seinen weiteren beruflichen und privaten Lebensweg alles Gute und weiterhin viel Erfolg". Nur als Klageantrag verwenden, wenn der Einzelfall dafür tragfähige Umstände bietet.

Ich bitte um Uebersendung des berichtigten Zeugnisses innerhalb von zwei Wochen ab Zugang dieses Schreibens.

Mit freundlichen Gruessen

### Beispiel 2 – Klageantrag bei Berichtigungsstreit

Der Beklagte wird verurteilt, der Klaegerin ein qualifiziertes Arbeitszeugnis zu erteilen, das auf dem Briefkopf der Beklagten ausgestellt wird, vom Tag des Beendigungsdatums datiert und vom dazu Befugten unterschrieben ist und folgenden Inhalt aufweist:

Erstens, in der Leistungsbeurteilung statt "war stets bemueht" die Formulierung "erledigte die ihr uebertragenen Aufgaben stets zu unserer vollen Zufriedenheit".

Zweitens, in der Verhaltensbeurteilung statt "Kollegen und Vorgesetzten" die Reihenfolge "Vorgesetzten, Kollegen und Kunden" mit dem Steigerer "stets" und dem Praedikat "einwandfrei".

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Beispiel 3 – Streitwert-Begruendung

Der Streitwert wird in Anlehnung an die staendige Rechtsprechung der Landesarbeitsgerichte auf ein Monatsbruttogehalt der Klaegerin festgesetzt. Der Wert betraegt nach den Angaben der Klaegerin im Tatbestand brutto Eurobetrag. Die Mehrzahl der Streitpunkte fuehrt nicht zu einer Wertaddition, weil der Anspruch auf das berichtigte Zeugnis insgesamt nur einmal entstehen kann.

### Beispiel 4 – Beweisangebote des Arbeitnehmers für bessere Note

Bei dem Begehren einer Note besser als befriedigend kommen folgende Beweisangebote in Betracht: zuständige Zwischenzeugnisse mit guter oder sehr guter Bewertung, Beurteilungsbeleg aus Jahresgespraechen, Boni und Praemien im Zeitraum, ausgezeichnete Performancereports, schriftliche Lob-E-Mails von Vorgesetzten, Zeugenaussagen unmittelbarer Vorgesetzter, Kundenfeedback in dokumentierter Form.

### Beispiel 5 – Verwirkung als Risiko

Wartet der Arbeitnehmer zwei Jahre, bevor er das Berichtigungsverlangen erhebt, ohne plausiblen Grund für die Verzoegerung, kann der Anspruch nach den Grundsaetzen der Verwirkung untergehen, auch wenn die Verjährungsfrist nicht abgelaufen ist. Empfehlung: Berichtigungsverlangen innerhalb der ersten Monate nach Zeugnisuebergabe stellen.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf Berichtigung; Grundlage der Klage
- **§§ 195, 199 BGB** — Verjährung drei Jahre; beginnt mit Schluss des Ausstellungsjahres
- **§ 242 BGB** — Verwirkung: Zeitmoment (mehrere Jahre) + Umstandsmoment

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (Vollstreckung, Holschuld, Form)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 21.09.1999 - 9 AZR 893/98** | Aeussere Form: zweimaliges Falten zulaessig, wenn Original kopierfaehig bleibt und Knicke nicht durchschlagen. Wer mit Maschinenname unterzeichnet, muss eigenhaendig unterschreiben. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 27.04.2021 - 9 AZR 262/20** | Tabellarische Ankreuz-/Schulnotenformulare erfuellen $ 109 GewO regelmaessig nicht - individuelle Hervorhebung verlangt Fliesstext. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Beschl. v. 07.05.2026 - 8 AZB 25/25** | Im gerichtlichen Vergleich uebernommene Pflicht, Zeugnis nach dem ENTWURF des Arbeitnehmers zu erteilen mit Abweichungs-Vorbehalt aus wichtigem Grund, hat vollstreckungsfaehigen Inhalt. | bundesarbeitsgericht.de / dejure.org (vor Schriftsatzverwendung live verifizieren - Entscheidung aus 2026) |
| **BAG, Urt. v. 08.03.1995 - 5 AZR 848/93** | Zeugniserteilung ist Holschuld ($ 269 BGB): Arbeitnehmer holt im Betrieb ab; nur ausnahmsweise (Unzumutbarkeit, $ 242 BGB) Schickschuld. | bundesarbeitsgericht.de / dejure.org |


## Vollstreckung des Zeugnisanspruchs

Wenn Urteil oder Vergleich vorliegt, der Arbeitgeber aber nicht oder falsch erfuellt:

| Lage | Instrument |
| --- | --- |
| Titulierter Zeugnisanspruch wird nicht erfuellt | Zwangsgeld, ersatzweise Zwangshaft ($ 888 ZPO - nicht vertretbare Handlung) |
| Vergleich mit Entwurfsklausel ("Zeugnis nach Entwurf des Arbeitnehmers, Abweichung nur aus wichtigem Grund") | Unmittelbar vollstreckbar (BAG 07.05.2026 - 8 AZB 25/25 - vor Verwendung live verifizieren) |
| Erteiltes Zeugnis weicht vom Titel ab | Im Vollstreckungsverfahren ruegen; ironische Uebererfuellung ist Nichterfuellung (LAG Hamm 12 Ta 475/16) |
| Streit ueber "wichtigen Grund" der Abweichung | Arbeitgeber muss den wichtigen Grund darlegen; sonst Zwangsmittel |

**Praxisregel:** Schon beim Vergleichsschluss an die Vollstreckung denken - die Entwurfsklausel mit Wichtiger-Grund-Vorbehalt macht aus dem Vergleich einen scharfen Titel.

---

## Skill: `erstgespraech-und-mandatsannahme`

_Mandatsannahme im Zeugnisrecht mit Erstgespraech Unterlagenerfassung und Fristen-Erstprognose. Anwendungsfall Arbeitnehmer erhaelt Zeugnis das er für mangelhaft haelt und sucht anwaltliche Hilfe. Normen § 109 GewO Anspruch auf qualifiziertes Zeugnis § 195 BGB Verjährung drei Jahre § 611a BGB Arbeitsvertrag. Prüfraster Zielklaerung fehlende Unterlagen Arbeitsvertrag Aenderungen Vorzeugnisse Fristen Vergleichsbereitschaft Verguetungsvereinbarung Beweislast. Output Mandatsannahmeprotokoll mit Unterlagenliste Erstprognose und naechsten Schritten. Abgrenzung zu klage-strategie-zeugnisberichtigung und aufforderungsschreiben-arbeitgeber._

# Erstgespraech und Mandatsannahme im Zeugnisrecht

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Eingangsbestaetigung

Auf den ersten Kontakt des Mandanten antwortet die Kanzlei zeitnah, in der Regel innerhalb eines Werktages. Die Eingangsbestaetigung enthaelt vier Bausteine: Dank für das uebersandte Zeugnis, kurze Beschreibung des weiteren Vorgehens, Liste der noch benoetigten Unterlagen sowie Hinweis auf die zu klaerenden Fristen.

Wichtig ist der Hinweis, dass die Bewertung erst nach Sichtung aller Unterlagen erfolgen kann. Eine vorschnelle Einschaetzung allein anhand des Zeugnistextes ist riskant, weil der Kontext (Aufgabenzuschnitt, Krankheitstage, Abmahnungen, Vergleichszeugnisse) die Bewertung erheblich verschieben kann. Der Mandant erhaelt daher zunaechst nur eine Eingangsbestaetigung, keine Bewertung.

## Anforderungsliste der Unterlagen

Die folgende Liste ist abschliessend strukturiert und sollte vollstaendig angefordert werden. Lueckenhafte Akten fuehren spaeter zu Beweisproblemen.

| Unterlage | Zweck |
| --- | --- |
| Arbeitsvertrag (Erstfassung) | Aufgabenzuschnitt, Eingruppierung, vereinbarte Taetigkeit |
| Aenderungsvereinbarungen, Versetzungsschreiben | Veraenderungen im Taetigkeitsbild |
| Stellenbeschreibung, Organigramm | Hierarchische Einordnung, Fuehrungsverantwortung |
| Vorzeugnisse (Zwischenzeugnis, Beurteilungen) | Vergleichsmassstab, Sperrwirkung der besseren Vorbewertung |
| Kuendigungsschreiben, Aufhebungsvertrag | Beendigungsgrund, Schlussformel-Erwartung |
| Abmahnungen | Belastbarkeit des Verhaltens-Themas, Risikoeinschaetzung |
| Krankheitstage- und Fehlzeitenuebersicht | Pruefung von Krankheits-Codeworten und langer Fehlzeit |
| Schriftwechsel zum Zeugnis | Bisherige aussergerichtliche Korrespondenz, Berichtigungsverlangen |
| Lohnabrechnungen der letzten drei Monate | Streitwertberechnung (Monatsbruttogehalt) |
| Eigene Aufgabenliste des Mandanten | Abgleich mit dem Zeugnistext, fehlende Aufgaben |

Bei besonderen Konstellationen kommen weitere Unterlagen hinzu: Schwerbehindertenausweis (Sonderkuendigungsschutz), Elternzeit-Bescheinigungen (Sperrzeit-Pruefung), Betriebsratstaetigkeit (Diskriminierungsrisiko), Pflegezeit, Mutterschutz.

## Erstgespraech-Leitfaden

Das Erstgespraech ist strukturiert in fuenf Bloecken zu fuehren.

Der erste Block ist die Sachverhaltsaufnahme. Eckdaten der Beschaeftigung (Beginn, Ende, Position, Vorgesetzte, letzte Aufgabe) werden notiert. Schwerpunkt ist nicht das Zeugnis, sondern das tatsaechliche Leistungs- und Verhaltensbild aus Sicht des Mandanten.

Der zweite Block ist die Zielklaerung. Will der Mandant ein besseres Zeugnis, eine bestimmte Note, eine bestimmte Schlussformel, eine konkrete Taetigkeitsbeschreibung oder die Entfernung bestimmter Passagen. Auch der Zeitdruck wird erfragt: Steht ein Vorstellungsgespraech an, ist Eile geboten.

Der dritte Block ist die Vergleichsbereitschaft. Ist der Mandant bereit, eine Note zwischen seiner Wunschnote und der erhaltenen Note zu akzeptieren. Ist er bereit, auf eine Schlussformel-Wendung zu verzichten, wenn dafür die Notenstufe stimmt. Diese Vorabklaerung erspart spaeter unnoetige Schriftsatzwechsel.

Der vierte Block ist die rechtliche Erstinformation. Der Mandant wird ueber den Anspruch nach Paragraf 109 GewO, die Beweislastregel (Note ab Drei: Arbeitnehmer, oberhalb der Drei: Arbeitgeber), die Verjährung und das Risiko der Verwirkung aufgeklaert. Ohne diese Aufklaerung ist eine wirksame Mandatsbeauftragung nicht moeglich.

Der fuenfte Block ist die Vereinbarung. Vergueterung (RVG oder Stundensatz), Kostenvorschuss, Rechtsschutzversicherung, Vollmacht und Mandatsumfang werden schriftlich festgehalten.

## Schreibmuster Eingangsbestaetigung

Sehr geehrter Herr [Name],

vielen Dank für Ihre Beauftragung und die uebersandten Unterlagen. Wir haben Ihr Arbeitszeugnis vom [Datum] erhalten und werden eine detaillierte Ampelanalyse durchfuehren.

Damit wir die Bewertung rechtssicher vornehmen und die Erfolgsaussichten eines Berichtigungsverlangens beurteilen koennen, benoetigen wir noch die folgenden Unterlagen:

- Arbeitsvertrag nebst allen Aenderungsvereinbarungen
- Stellenbeschreibung oder schriftliche Aufgabenuebersicht
- gegebenenfalls vorhandene Zwischenzeugnisse und Beurteilungen
- Kuendigungsschreiben oder Aufhebungsvertrag
- gegebenenfalls erteilte Abmahnungen
- Uebersicht ueber Krankheits- und Fehlzeiten im letzten Beschaeftigungsjahr
- bisheriger Schriftwechsel zum Zeugnis
- Lohnabrechnungen der letzten drei Monate

Bitte beachten Sie, dass der Anspruch auf Berichtigung eines Arbeitszeugnisses der Verjährung und gegebenenfalls der Verwirkung unterliegt. Wir empfehlen daher eine zuegige Bearbeitung. Nach Eingang der vollstaendigen Unterlagen erhalten Sie binnen einer Woche unsere Bewertung mit Vorschlag für das weitere Vorgehen.

Mit freundlichen Gruessen
[Kanzlei]

## Pruefliste vor Mandatsannahme

Vor der formellen Annahme prueft die Kanzlei drei Punkte. Erstens den Interessenkonflikt: Vertritt die Kanzlei den frueheren Arbeitgeber oder einen verbundenen Konzern, ist das Mandat zu versagen. Zweitens die Verjährung: Liegt das Zeugnisdatum mehr als drei Jahre zurueck, ist die Erfolgsaussicht ohne besondere Umstaende gering. Drittens die Werthaltigkeit: Bei einer reinen Schlussformel-Diskussion ohne wirtschaftliche Bedeutung sollte der Mandant ueber das Kostenrisiko offen aufgeklaert werden.

## Anschluss an die weiteren Skills

Nach Mandatsannahme folgt die Ampelanalyse mit den Skills zur Notenmatrix, Drift-Erkennung und rechtlichen Bewertung. Das Ergebnis fliesst in den Skill `mandantenbericht-zeugnisanalyse`. Die Aufforderung an den Arbeitgeber wird ueber den Skill `aufforderungsschreiben-arbeitgeber` erstellt, der weitere Verfahrensweg ueber `klage-strategie-zeugnisberichtigung`.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf Zeugnis; Grundlage aller Mandate
- **§§ 195, 199 BGB** — Regelverjährung drei Jahre; Mandant über Verwirkungsrisiko aufklären
- **§ 242 BGB** — Verwirkung bei jahrelanger Untätigkeit; sofortige Mandatsannahme empfohlen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — Erstgesprächs-Einstieg

1. Wann wurde das Zeugnis ausgestellt und wann übergeben?
2. Gibt es Vorzeugnisse oder Zwischenzeugnisse zum Vergleich?
3. Welche Unterlagen hat der Mandant bereits mitgebracht?
4. Welches Ziel hat der Mandant konkret? (Gesamtnote verbessern / einzelne Passagen / Schlussformel)
5. Steht ein Vorstellungsgespräch an? → Eilbedürftigkeit prüfen!

---

## Skill: `rechtliche-bewertung-bag-rechtsprechung`

_Rechtliche Einordnung von Zeugnisansprüchen nach § 109 GewO und BAG-Rechtsprechung für die anwaltliche Praxis. Anwendungsfall Anwalt benoetigt Beweislastverteilung und Rechtsgrundlagen für Zeugnisstreit oder Klagebegründung. Normen § 109 GewO Anspruchsgrundlage § 611a BGB § 241 Abs. 2 BGB Wohlwollenspflicht BAG-Linie zur Beweislast. Prüfraster Anspruch auf qualifiziertes Zeugnis Beweislast bei Zeugnisstreit Grenzen Wahrheitspflicht Verjährung. Output Rechtliche Einordnung mit BAG-Nachweisen für Klagebegründung oder Verhandlungsstrategie. Abgrenzung zu klage-strategie-zeugnisberichtigung und aufforderungsschreiben-arbeitgeber._

# Rechtliche Bewertung und BAG-Rechtsprechung zum Arbeitszeugnis

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln (Rechtliche Ebene)

| Rechtsproblem | Rechtsgrundlage | Handlungsempfehlung |
|---|---|---|
| Anspruch auf qualifiziertes Zeugnis | § 109 Abs. 1 Satz 3 GewO | Schriftlich verlangen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Geheimcodeformeln in Zeugnis | Anspruch auf wohlwollendes Zeugnis | Berichtigung verlangen |
| Zeugnis nach BAG-Recht zu berichtigen | § 109 GewO | Klage ArbG, kein Fristproblem |
| Codewort verstößt gegen Klarheit oder Wohlwollen | § 109 Abs. 2 GewO, BAG-Linie | Berichtigung verlangen, Kontext begründen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Drift im selben Themenbereich | Wohlwollensgebot | Aufwertung der schwachen Sätze verlangen |
| Streitwert Berichtigungsklage | Rechtsprechung Landesarbeitsgerichte | ein Monatsbruttogehalt |
| Verjährung des Berichtigungsanspruchs | §§ 195, 199 BGB | drei Jahre ab Schluss des Jahres |
| Verwirkung trotz nicht abgelaufener Verjährung | Treu und Glauben § 242 BGB | Berichtigung innerhalb weniger Monate stellen |

## Beispiele

**Beispiel 1 – Anspruch auf Berichtigung:** Ein Zeugnis enthält "bemüht" (Note 4). Der Arbeitnehmer hat nachweislich gute Beurteilungen in Mitarbeitergesprächen erhalten. Die Berichtigung kann verlangt werden; der Arbeitgeber muss die Schlechterbeurteilung beweisen.

**Beispiel 2 – Beweislast beim Arbeitnehmer:** Der Arbeitnehmer begehrt die Note "sehr gut" (Note 1 bis 2). Er muss konkrete Leistungsnachweise erbringen, die eine Übererfüllung der Anforderungen belegen — allgemeine Zufriedenheitsbekundungen reichen nicht.

**Beispiel 3 – Verwirkung:** Ein Arbeitnehmer nimmt ein Zeugnis mit Note 4 entgegen und beanstandet es erst vier Jahre später. Das Gericht kann Verwirkung des Berichtigungsanspruchs annehmen, wenn ein Vertrauenstatbestand entstanden ist.

**Beispiel 4 – Schlussformel als Signal, nicht Automatismus:** Ein Zeugnis enthält "Wir wünschen ihm alles Gute" ohne Bedauern und ohne Dank. Der Arbeitnehmer war nachweislich beliebt und leistungsstark. Das ist ein Distanzsignal und ein guter Verhandlungspunkt. Als Klagepunkt ist es nur tragfähig, wenn zusätzliche Umstände hinzukommen, etwa ein Vergleichstext, ein bindendes Zwischenzeugnis, eine betriebliche Übung oder ein widersprüchliches Gesamtbild.

**Beispiel 5 – Auskunftspflicht des Arbeitgebers:** In manchen Fällen kann der Arbeitnehmer verlangen, dass der Arbeitgeber erklärt, warum bestimmte Formulierungen gewählt wurden. Das setzt voraus, dass der Arbeitnehmer eine plausible Berichtigung konkret benannt hat.

**Beispiel 6 – Codewort als Klarheitsproblem:** Ein Zeugnis enthält bei einem Buchhalter ohne Kassentätigkeit die isolierte Aussage "war ehrlich und korrekt". Die Aussage kann wahr sein, kann aber nach Stellung im Zeugnis und Branchenkontext einen Verdacht wecken. Der Angriff sollte nicht behaupten, jedes Wort "ehrlich" sei verboten, sondern begründen, warum gerade diese Platzierung im Gesamtzusammenhang eine verdeckte negative Aussage erzeugt.

**Beispiel 7 – Drift-Berichtigung:** Ein Zeugnis enthält im Fachbereich eine Maximalformulierung und im Bereich Lernbereitschaft einen Standardsatz. Der Arbeitnehmer kann die Aufwertung der schwachen Sätze verlangen, soweit er die entsprechenden Leistungen substantiiert. Eine uneinheitliche Bewertung ohne Tatsachengrund wird als Widerspruch im Gesamtbild geführt, nicht als bloßes Rechenproblem.

**Beispiel 8 – Streitwert und Vertretungspflicht:** Die Streitwertfestsetzung folgt der staendigen Praxis: ein Monatsbruttogehalt, unabhängig von der Anzahl der beanstandeten Sätze. Eine anwaltliche Vertretung ist im ersten Rechtszug vor dem Arbeitsgericht möglich, aber nicht erforderlich. In komplexen Berichtigungsfällen mit mehreren beanstandeten Punkten ist sie ratsam, weil die Wortlautformulierung des Klageantrags entscheidend ist.

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (vollstaendige BAG-Linie)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast fuer bessere Note beim Arbeitnehmer, fuer schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast fuer bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 20.02.2001 - 9 AZR 44/00** | Beginn der staendigen Linie: kein Anspruch auf Schlussformel mit Dank und guten Wuenschen; Fehlen kein unzulaessiges Geheimzeichen. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 11.12.2012 - 9 AZR 227/11** | Kein Anspruch auf Dank/Wuensche; bei unzufriedener Mandantschaft mit erteilter Schlussformel ist nur ein Zeugnis OHNE Schlussformel einklagbar - keine Umformulierung. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 25.01.2022 - 9 AZR 146/21** | Bestaetigung der Linie; Abwaegung mit Meinungsfreiheit des Arbeitgebers (Art. 5 I GG). | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 06.06.2023 - 9 AZR 272/22** | Massregelungsverbot $ 612a BGB: eine einmal erteilte Dankes-/Wunschformel darf nicht in spaeterer Fassung gestrichen werden, nur weil der Arbeitnehmer berechtigte Aenderungswuensche geltend gemacht hat. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 21.09.1999 - 9 AZR 893/98** | Aeussere Form: zweimaliges Falten zulaessig, wenn Original kopierfaehig bleibt und Knicke nicht durchschlagen. Wer mit Maschinenname unterzeichnet, muss eigenhaendig unterschreiben. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 27.04.2021 - 9 AZR 262/20** | Tabellarische Ankreuz-/Schulnotenformulare erfuellen $ 109 GewO regelmaessig nicht - individuelle Hervorhebung verlangt Fliesstext. | bundesarbeitsgericht.de / dejure.org |
| **LAG Hamm, Beschl. v. 14.11.2016 - 12 Ta 475/16** | Ironisch ueberzogenes Lob ist unzulaessig; Arbeitnehmer hat Anspruch auf geschaeftsuebliche Unterschrift des Ausstellers; quer-laufende Unterschrift weckt Zweifel an Ernsthaftigkeit. | nrwe.de / justiz.nrw.de |
| **ArbG Kiel, Urt. v. 18.04.2013 - 5 Ca 80 b/13** | In die Unterschrift eingearbeiteter Smiley mit herabgezogenen Mundwinkeln ist ein unzulaessiges Geheimzeichen ($ 109 II 2 GewO). | frei publiziert / dejure-Suche |
| **BAG, Beschl. v. 07.05.2026 - 8 AZB 25/25** | Im gerichtlichen Vergleich uebernommene Pflicht, Zeugnis nach dem ENTWURF des Arbeitnehmers zu erteilen mit Abweichungs-Vorbehalt aus wichtigem Grund, hat vollstreckungsfaehigen Inhalt. | bundesarbeitsgericht.de / dejure.org (vor Schriftsatzverwendung live verifizieren - Entscheidung aus 2026) |
| **BAG, Urt. v. 08.03.1995 - 5 AZR 848/93** | Zeugniserteilung ist Holschuld ($ 269 BGB): Arbeitnehmer holt im Betrieb ab; nur ausnahmsweise (Unzumutbarkeit, $ 242 BGB) Schickschuld. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `branchen-spezifische-formulierungen`

_Decodiert branchenspezifische Formulierungen im Arbeitszeugnis zur praezisen Noteneinordnung. Anwendungsfall Zeugnis enthaelt Formulierungen die nur im Kontext einer bestimmten Branche verstaendlich sind. Branchen Vertrieb (Umsatz Zielerreichung) Recht (Mandatsführung Kanzlei) IT (Projektverantwortung Technologie) Pflege (Patientenkontakt Empathie) und weitere. Normen § 109 GewO § 241 Abs. 2 BGB Wohlwollenspflicht. Output Ampelzuordnung branchenspezifischer Formulierungen mit Notentendenzen und Alternativformulierungen. Abgrenzung zu geheimcode-katalog (allgemeine Geheimcodes) und leistungsbeurteilung-analyse._

# Branchenspezifische Formulierungen

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Branche | Pflichtformulierung | Fehlen bedeutet |
|---|---|---|
| Vertrieb | Zielerreichung, Kundenbindung | Unterdurchschnittliche Vertriebsleistung |
| Recht/Kanzlei | Mandatsführung, Schriftsatzqualität | Qualitätsprobleme beim Kernjob |
| IT | Projektabschlüsse, Technologiekompetenz | Fehlende Kernergebnisse |
| Pflege | Patientenkontakt, Empathie | Probleme mit Patienten |
| Finanzwesen | Zuverlässigkeit, Genauigkeit, Vertrauen | Verdacht auf Unregelmäßigkeiten |
| Personalwesen | Mitarbeiterentwicklung, Verhandlungsführung | Schwäche im Kernbereich |

## Beispiele

**Beispiel 1 – Vertrieb (Grün):** "Herr Kurz übertraf seine Vertriebsziele im Beobachtungszeitraum durchgehend und war maßgeblich an der Neukundengewinnung beteiligt."

**Beispiel 2 – IT (Orange):** "Frau Kramer hat an mehreren Softwareprojekten mitgewirkt und dabei ihre technischen Fähigkeiten eingesetzt." — Passiv, keine Erfolgsaussagen, keine Verantwortungsaussage.

**Beispiel 3 – Pflege (Rot durch Auslassung):** Zeugnis einer Stationsschwester ohne jede Aussage zu Patientenversorgung oder Empathie → klassisches rotes Signal im Pflegebereich.

**Beispiel 4 – Recht (Grün):** "Frau Dr. Bauer führte ihre Mandate stets eigenverantwortlich und erzielte für unsere Mandanten regelmäßig hervorragende Ergebnisse. Ihre Schriftsätze waren stets von höchster Qualität."

**Beispiel 5 – Finanzwesen (Rot durch Schweigen):** Buchhalter-Zeugnis ohne ein einziges Wort zu Sorgfalt, Genauigkeit oder Vertrauenswürdigkeit → klassisches Warnsignal bei finanzrelevanten Positionen.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Wohlwollend formuliertes qualifiziertes Zeugnis; tatsächliche Tätigkeit und Anforderungsprofil prägen den Maßstab

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Branchenanalyse

1. Welcher Branche ist das Zeugnis zuzuordnen?
2. Gibt es branchentypisch erwartete Aussagen (z.B. Kassenführung im Einzelhandel, Patientenumgang in der Pflege)?
3. Erfordert die Funktion besondere Sicherheitshinweise oder Vertrauensstellungen?


## Leitentscheidungs-Anker (Empfaengerhorizont, Grenzen der Decodierung)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `zeugnisart-erkennung`

_Unterscheidet qualifiziertes Endzeugnis einfaches Zeugnis Zwischenzeugnis und Ausbildungszeugnis am Beginn jeder Analyse. Anwendungsfall Zeugnis liegt vor und muss bevor Analyse startet der richtigen Zeugnisart zugeordnet werden. Normen § 109 GewO qualifiziertes vs. einfaches Zeugnis § 16 BBiG Ausbildungszeugnis. Prüfraster Inhalt Zeitbezug Position Stichtag Ausstellungsanlass. Output Zeugnisart-Klassifikation mit Erlauterungen zu Inhalt Erwartungshaltung und Interpretationsrahmen für alle Folge-Skills. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und notenrelevante-saetze-identifizieren._

# Zeugnisart-Erkennung

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Zeugnisart | Mindest- und Erwartungsbausteine | Fehlende Bausteine |
|---|---|---|
| Einfaches Zeugnis | Art und Dauer der Tätigkeit | Keine Leistungsaussage erwartet |
| Qualifiziertes Endzeugnis | Art, Dauer, Leistung, Verhalten, Schlussformel | Rotes Signal |
| Zwischenzeugnis | Art, Dauer, Leistung, Verhalten (Präsens) | Kein Enddatum, keine Verabschiedung OK |
| Ausbildungszeugnis | Lernleistung, Berufsschule, Verhalten, Praxis | Nach BBiG-Maßstab |
| Führungskraft (qualifiziert) | Plus Führung, Strategie, Repräsentation | Fehlen = Orange/Rot |

## Beispiele

**Beispiel 1 – Korrekte Zeugnisart-Erkennung:** "Wir stellen dieses Zeugnis auf eigenen Wunsch aus" + kein Enddatum → Zwischenzeugnis auf Wunsch des Arbeitnehmers.

**Beispiel 2 – Einfaches Zeugnis korrekt interpretiert:** Zeugnis ohne jede Leistungsbeurteilung und ohne Verhaltensabschnitt, aber mit explizitem Hinweis "einfaches Zeugnis" oder keine Bewertungsformulierungen — nicht als Abwertung zu lesen.

**Beispiel 3 – Fehlendes Verhalten bei Endzeugnis (Orange):** Qualifiziertes Zeugnis mit Leistungsbeurteilung, aber ohne Verhaltensabschnitt gegenüber Kollegen/Kunden — Auslassung ist auffällig.

**Beispiel 4 – Ausbildungszeugnis ohne Berufsschulangabe (Orange):** Bei einem BBiG-Zeugnis fehlt die Beurteilung des schulischen Teils komplett, obwohl Schule und Betrieb im Sachverhalt eine tragende Rolle spielen — erwarteter Baustein fehlt.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `zeugnis-ueberblick-extraktion`

_Extrahiert Kopfdaten aus deutschen Arbeitszeugnissen für Mandatsanlage und Analysestart. Anwendungsfall Zeugnis wurde hochgeladen und Basisdaten sollen für Akte und Analyse erfasst werden. Normen § 109 GewO Pflichtinhalt § 16 BBiG Ausbildungszeugnis. Prüfraster Arbeitgeber Arbeitnehmer Beschaeftigungszeitraum Position Ausstellungsdatum Unterschriftsberechtigte Vollständigkeit. Output Strukturiertes Kopfdatenblatt mit Vollständigkeitsprüfung und Zeugnisart-Einordnung als Eingabe für alle Folge-Analyse-Skills. Abgrenzung zu zeugnisart-erkennung und notenrelevante-saetze-identifizieren._

# Zeugnis-Überblick und Kopfdaten-Extraktion

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Merkmal | Bedeutung | Ampel |
|---|---|---|
| Unterschrift rangniederer Person | Verdeckte Abwertung der Stellung | Rot |
| Kein Briefkopf / kein Stempel | Formfehler, möglicherweise anfechtbar | Orange |
| Datum weit nach Austritt | Zeigt Widerstand oder Nachlässigkeit | Orange |
| Vollständige Angaben, ranghöhere Unterschrift | Erwartungskonformes Zeugnis | Grün |
| Beschäftigungszeitraum weicht von Vertrag ab | Klärungsbedarf | Orange |

## Beispiele

**Beispiel 1 – Vollständige Kopfdaten (Grün):** "Frau Sabine Müller, geboren am 12. März 1985, war vom 1. April 2018 bis zum 31. März 2024 in unserem Unternehmen als Abteilungsleiterin Marketing tätig." — Alle Pflichtangaben vorhanden.

**Beispiel 2 – Fehlende Positionsangabe (Orange):** "Herr Thomas Braun war von 2019 bis 2023 bei uns beschäftigt." — Keine Positionsbezeichnung, kein vollständiges Datum.

**Beispiel 3 – Unterschrift Sachbearbeiter (Rot):** Unterschrift eines HR-Sachbearbeiters für einen ausscheidenden Abteilungsleiter — hierarchisches Missverhältnis signalisiert Abwertung.

**Beispiel 4 – Datum vor Austritt (Orange):** Ausstellungsdatum liegt drei Monate vor dem angegebenen letzten Arbeitstag — formale Unstimmigkeit.

**Beispiel 5 – Zwischenzeugnis ohne Enddatum (Grün):** Kein Enddatum bei einem als Zwischenzeugnis bezeichneten Dokument — korrekt und unauffällig.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `azubi-zeugnis-analyse`

_Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubildender hat Ausbildungszeugnis erhalten das er für schlecht haelt. Normen § 16 BBiG Zeugnispflicht § 109 GewO analog. Prüfraster Lernfortschritt Berufsschulleistungen praktische Ausbildungsaufgaben Verhalten im Betrieb Ampelzuordnung branchenspezifische Formulierungen. Output Ampeltabelle mit Notentendenzen Begründungen und Verbesserungsvorschlaegen. Abgrenzung zu leistungsbeurteilung-analyse und schlussformel-bewertung (Arbeitszeugnisse Erwachsener)._

# Ausbildungszeugnis-Analyse (Azubi-Zeugnis)

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Azubi-Formulierung | Bedeutung | Ampel |
|---|---|---|
| "schnell und sicher aufgenommen" | Hervorragender Lernfortschritt | Grün |
| "zuverlässig die Ausbildungsinhalte angeeignet" | Guter Lernfortschritt | Grün |
| "hat sich die Inhalte erarbeitet" | Befriedigender Fortschritt | Orange |
| "war bereit zu erlernen" | Unterdurchschnittlicher Fortschritt | Rot |
| Fehlender Berufsschulabschnitt (duale Ausbildung) | Mögliche Schulprobleme | Orange |
| "hat sich positiv entwickelt" | Für Azubi: gut; für Vollkraft: schwach | Grün (Azubi) |
| "pünktlich und zuverlässig" | Wichtiges Grundverhalten | Grün |
| Fehlende Pünktlichkeitsaussage | Fehlzeiten/Verspätungen | Orange |

## Beispiele

**Beispiel 1 – Grünes Azubi-Zeugnis:** "Herr Müller hat die Ausbildungsinhalte stets schnell und sicher aufgenommen, zeigte großes Interesse an seinem Ausbildungsberuf und zeichnete sich durch hervorragende Berufsschulleistungen aus."

**Beispiel 2 – Orange Azubi-Zeugnis:** "Frau Weber hat sich die Ausbildungsinhalte erarbeitet und dabei guten Willen gezeigt. Die Berufsschulleistungen entsprachen den Anforderungen." — Kein Superlativ, kein Engagement, keine Begeisterung.

**Beispiel 3 – Rotes Azubi-Zeugnis:** "Herr Bauer war stets bereit, die Ausbildungsinhalte zu erlernen, und hat die Anforderungen im Wesentlichen erfüllt." — "Bereit" + "im Wesentlichen" = doppeltes rotes Signal.

**Beispiel 4 – Fehlender Berufsschulabschnitt:** Zeugnis eines Industriekaufmanns (duale Ausbildung) ohne jede Aussage zur Berufsschule → orangefarbenes Signal.

**Beispiel 5 – Vollständige positive Schlussformel:** "Wir bedauern es sehr, Frau Klein am Ende ihrer Ausbildung zu verlieren, und danken ihr herzlich für ihr Engagement. Wir empfehlen sie uneingeschränkt." — Starkes Signal für einen Übernahme- oder Weiterempfehlungswunsch.

## Rechtliche Einordnung und Normen

- **§ 16 BBiG** — Anspruch des Auszubildenden auf qualifiziertes Zeugnis nach Beendigung der Ausbildung
- **§ 13 BBiG** — Pflichten des Auszubildenden; Pflichtverletzungen dürfen nur bei tragfähiger Tatsachengrundlage in die Beurteilung einfließen
- Allgemeine Zeugnisgrundsätze zu Wahrheit, Klarheit und Wohlwollen sind bei Ausbildungszeugnissen entsprechend zu berücksichtigen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Azubi-Analyse

1. Abschlusszeugnis oder Zwischenzeugnis (§ 16 Abs. 2 BBiG)?
2. Duales Ausbildungsverhältnis? → Berufsschulbewertung vorhanden?
3. Ausbildung abgebrochen? → Nur Anspruch auf einfaches Zeugnis nach § 16 Abs. 1 BBiG
4. Beendigungsgrund: Bestehen der Prüfung oder Kündigung/Aufhebung?


## Leitentscheidungs-Anker (Notenstufen & Beweislast)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast fuer bessere Note beim Arbeitnehmer, fuer schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast fuer bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `gesamtnoten-aggregation`

_Aggregiert Einzelbewertungen aus Leistungs- Verhaltens- und Schlussformel-Analyse zur Gesamtnote. Anwendungsfall alle Einzelsaetze sind analysiert und eine gewichtete Gesamtnote soll bestimmt werden. Normen § 109 GewO Gesamteindruck BAG-Linie zur Gewichtung Zeugnisbereiche. Prüfraster Gewichtung Leistungsteil Verhaltensteil Schlussformel Ausreisser-Saetze Bereichs-Drift. Output Begründete Gesamtnotenspanne mit Gewichtungsmatrix für Mandantenbericht und Klageantrag. Abgrenzung zu satzweise-notenmatrix (Einzelsatz-Bewertung) und bereichs-drift-detektor._

# Gesamtnoten-Aggregation

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Teilbereich | Gewicht | Besonderheit |
|---|---|---|
| Leistungsbeurteilung gesamt | ca. 50% | Zufriedenheitsformel als Kernindikator |
| Verhaltensbeurteilung | ca. 30% | Reihenfolge und Auslassungen beachten |
| Schlussformel | Kontextsignal | Signalwirkung und Anspruch trennen |
| Rote Auslassung (Integrität/Loyalität) | Gesondert | Kann Gesamtnote um eine Note senken |
| Widersprechende Signale | Gesondert | Führen zu Unsicherheitsabschlag |
| Bereichs-Drift zwei Stufen | minus halbe Stufe | Schaufenster-Pattern |
| Konstante Note 3 in weichen Bereichen | minus halbe Stufe | Lernen, Innovation, Sozialverhalten |

## Beispiele

**Beispiel 1 – Klares Note-1-Zeugnis:** Leistungsbeurteilung grün (Note 1), Verhalten grün (Note 1), Schlussformel grün (Note 1) → Gesamtnote: Note 1. Keine Abweichungen.

**Beispiel 2 – Gemischtes Zeugnis Note 2-3:** Leistung grün (Note 2), Verhalten orange (Note 3), Schlussformel orange (Note 3) → Gewichteter Wert: ca. Note 2 bis 3. Empfehlung: Verhaltens- und Schlussformel nachverhandeln.

**Beispiel 3 – Rote Auslassung senkt Note:** Zeugnis insgesamt Note 2 aus Einzelwertungen, aber fehlende Loyalitätsaussage bei einer Führungskraft → Gesamtnote abgesenkt auf Note 2-3 mit Hinweis auf das Loyalitätssignal.

**Beispiel 4 – Widersprüchliches Zeugnis:** Leistung grün, Verhalten rot, Schlussformel grün → Note 2 bis 3 mit Unsicherheitsabschlag wegen Widerspruchs; Skill empfiehlt Verweis auf widerspruechliche-bewertungen.

**Beispiel 5 – Minimalistisches Zeugnis:** Alle Aussagen orange (Note 3), vollständige Schlussformel → Gesamtnote: Note 3. Verbesserungspotenzial in allen Bereichen.

**Beispiel 6 – Schaufenster-Zeugnis:** Spitzensätze grün (Note 1) bei Fachkenntnissen, Arbeitsweise, Arbeitsergebnis; daneben orange Sätze (Note 3) zu Lernbereitschaft, Innovation, Sozialverhalten; Schlussformel grün (Note 1). Rechnerischer Wert vor Penalty: Note 1 bis 2. Drift-Penalty Lernbereitschaft: minus halbe Stufe. Konstante Note 3 in weichen Bereichen: minus halbe Stufe. Gesamtnote: Note 2 bis Note 3, nicht Note 1 wie die Schaufenster-Sätze suggerieren.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis; Grundlage aller Bewertungen
- **§§ 195, 199 BGB** — Verjährung drei Jahre ab Jahresende

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (Notenstufen & Beweislast)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 14.10.2003 - 9 AZR 12/03** | Zur vollen Zufriedenheit bescheinigt durchschnittliche Leistung (Note 3); Beweislast fuer bessere Note beim Arbeitnehmer, fuer schlechtere beim Arbeitgeber. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 18.11.2014 - 9 AZR 584/13** | "Befriedigend" als Mitte der Skala; Arbeitnehmer traegt Beweislast fuer bessere Note; Branchenueblichkeit guter Noten verschiebt die Beweislast nicht. | bundesarbeitsgericht.de / dejure.org |

---

## Skill: `notenrelevante-saetze-identifizieren`

_Identifiziert notenrelevante Saetze im Arbeitszeugnis und trennt sie von neutralen Aufgabenbeschreibungen. Anwendungsfall Zeugnis liegt vor und muss für Ampelanalyse vorbereitet werden. Normen § 109 GewO Inhalte eines qualifizierten Zeugnisses BAG-Anforderungen an Vollständigkeit. Kategorisierung Aufgabenbeschreibung Leistungsbeurteilung Verhaltensbeurteilung Schlussformel. Output Kategorisierte Satzliste als Eingabe für satzweise-notenmatrix und Bereichs-Drift-Detektor. Abgrenzung zu zeugnis-ueberblick-extraktion (Kopfdaten) und zeugnisart-erkennung._

# Notenrelevante Sätze identifizieren

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Satztyp | Notenrelevant? | Ampel-Analyse |
|---|---|---|
| Aufgabenbeschreibung (rein deskriptiv) | Nein | Keine Ampelzuordnung |
| Leistungsaussage mit Qualitätsmerkmal | Ja | Ampel nach Formulierung |
| Verhaltensaussage zu Dritten | Ja | Ampel nach Formulierung und Reihenfolge |
| Schlussformel (Dank, Bedauern, Wünsche) | Signalrelevant | Ampel nach Ton; Anspruch gesondert prüfen |
| Satz mit impliziter Bewertung | Ja | Ampel nach Gesamttendenz |
| Kurze Aufgabenbeschreibung trotz hoher Stellung | Grenzfall | Orange |

## Beispiele

**Beispiel 1 – Rein deskriptiv (nicht notenrelevant):** "Frau Weber war in unserem Haus als Projektmanagerin tätig und verantwortete die Koordination externer Dienstleister." — Keine Qualitätsaussage.

**Beispiel 2 – Leistungsbeurteilung (notenrelevant):** "Sie erledigte alle ihr übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit." — Kernbeurteilungssatz, Note 1, Grün.

**Beispiel 3 – Verhaltensbeurteilung (notenrelevant):** "Ihr Verhalten gegenüber Vorgesetzten und Kollegen war einwandfrei." — Reihenfolge und Qualifikationswort bestimmen Ampelfarbe.

**Beispiel 4 – Implizite Bewertung (notenrelevant):** "Herr Schmidt war stets bemüht, seine Aufgaben pünktlich abzuliefern." — Scheinbar positiv, tatsächlich rotes Signal durch "bemüht".

**Beispiel 5 – Schlussformel (signalrelevant):** Fehlen des Bedauerns über das Ausscheiden — mögliches Distanzsignal trotz positiver Leistungsformulierungen; rechtlich nicht automatisch einklagbar.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `satzweise-notenmatrix`

_Bewertet jeden notenrelevanten Satz eines Arbeitszeugnisses mit Schulnote 1 bis 5. Anwendungsfall notenrelevante Saetze wurden identifiziert und sollen systematisch bewertet werden. Normen § 109 GewO Bewertungsmassstab BAG-Linie zur Zeugnissprache. Prüfraster Satzkurzform Themenbereich Note Steigerungsadverb-Befund Begründung. Output Geschlossene Notenmatrix als Grundlage für Bereichs-Drift-Detektor und Gesamtnoten-Aggregation. Abgrenzung zu notenrelevante-saetze-identifizieren (Vorstufe) und gesamtnoten-aggregation (Folgestufe)._

# Satzweise Notenmatrix

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Sprachmuster | Note |
|---|---|
| Steigerungsadverb plus Superlativ ("stets äußerst", "jederzeit hervorragend") | Note 1 |
| Superlativ ohne Adverb oder Adverb ohne Superlativ | Note 2 |
| Grundaussage ohne Adverb, ohne Superlativ ("gute Ideen", "hohe Lernbereitschaft") | Note 3 |
| Einschränkung ("im Wesentlichen", "weitgehend") oder Codewort "bemüht" | Note 4 |
| "angemessen", "korrekt" im Leistungsteil, fehlende positive Aussage | Note 5 |
| "zeigte", "fand", "war in der Lage zu" ohne Steigerung | Note 3 |
| "verfügt über" ohne Steigerung | Note 3 |
| "verfügt über äußerst profundes" plus Maximalbereich | Note 1 |

## Beispiele

**Beispiel 1 – Note 1:** "verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches ueber aeusserst profundes Fachwissen" → Steigerungsadverb "aeusserst", Maximalbereichsangabe "auch in Randbereichen", Superlativ "profundes". Themenbereich Fachkenntnisse.

**Beispiel 2 – Note 3:** "nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil" → kein Steigerungsadverb, kein Superlativ ("regelmaessig" ist Haeufigkeit, kein Steigerer). Themenbereich Lernbereitschaft.

**Beispiel 3 – Note 1:** "Alle Aufgaben fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus" → drei Steigerer ("jederzeit", "vollkommen", "aeusserst"). Themenbereich Arbeitsweise.

**Beispiel 4 – Note 3:** "war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze" → "gute" statt "hervorragende", kein Steigerungsadverb, Verb "fand" statt "entwickelte". Themenbereich Innovation.

**Beispiel 5 – Note 1:** "Arbeitsergebnisse lagen stets sehr weit ueber unseren Anforderungen" → Steigerer "stets sehr weit", expliziter Vergleich "ueber unseren Anforderungen". Themenbereich Arbeitsergebnis.

**Beispiel 6 – Note 3:** "war ein geschaetzter Ansprechpartner, sein persönliches Verhalten war einwandfrei" → "geschaetzt" ohne Steigerung, "einwandfrei" ohne "stets". Themenbereich Sozialverhalten.

**Beispiel 7 – Note 4:** "war stets bemueht" → Codewort, unabhaengig vom restlichen Satz. Themenbereich je nach Kontext.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `muster-arbeitszeugnis-note-1`

_Vollständiges Musterarbeitszeugnis Note 1 als Referenzdokument für Vergleich und Berichtigung. Anwendungsfall Anwalt oder Mandant will wissen wie ein optimales Zeugnis aussieht. Alle Kernbausteine in grüner Formulierung: Kopfdaten, Aufgabenbeschreibung, Leistungsbeurteilung, Verhaltensbeurteilung und warme Schlussformel. Output Musterdokument mit Erläuterungen je Baustein als Referenz für Zeugnisberichtigungsantrag. Abgrenzung zu muster-arbeitszeugnis-mit-roten-flaggen und verbesserungsvorschlaege-formulieren._

# Muster-Arbeitszeugnis Note 1 (Referenzdokument)

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

Alle in diesem Muster verwendeten Formulierungen sind grün kodiert:

| Satz | Ampel | Note |
|---|---|---|
| "stets zur vollsten Zufriedenheit" | Grün | Note 1 |
| "hervorragende Fachkenntnisse" | Grün | Note 1 |
| "außerordentliches Engagement" | Grün | Note 1 |
| "stets einwandfrei" (Verhalten) | Grün | Note 1 |
| Warme Schlussformel mit Bedauern | Grün | Starkes Praxissignal |

## Beispiele

### Vollständiges Muster-Zeugnis Note 1

---

**[Briefkopf des Unternehmens]**
Musterunternehmen GmbH | Musterstraße 1 | 10000 Musterstadt

**Arbeitszeugnis**

Frau Anna Musterfrau, geboren am 1. Januar 1985, war vom 1. März 2018 bis zum 28. Februar 2025 in unserem Unternehmen als Leiterin der Abteilung Controlling tätig.

**Aufgaben:**
Frau Musterfrau verantwortete die vollständige Führung unserer Controlling-Abteilung mit zwölf direkt unterstellten Mitarbeiterinnen und Mitarbeitern. Sie war zuständig für die monatliche Ergebnisberichterstattung an den Vorstand, die Erstellung der Jahresplanung und des mittelfristigen Finanzplans, die Durchführung von Abweichungsanalysen sowie die Koordination externer Prüfungsgesellschaften.

**Leistungsbeurteilung:**
Frau Musterfrau verfügt über hervorragende Fachkenntnisse, die sie stets sicher, souverän und mit außerordentlichem Erfolg eingesetzt hat. Ihre Arbeitsweise war stets strukturiert, präzise und ergebnisorientiert. Auch in Phasen hoher Arbeitsbelastung behielt sie stets die Übersicht und erzielte konstant hervorragende Ergebnisse. Ihre Eigeninitiative und ihr außerordentliches Engagement haben unser Unternehmen maßgeblich vorangebracht. Alle ihr übertragenen Aufgaben erledigte sie stets zu unserer vollsten Zufriedenheit.

**Verhaltensbeurteilung:**
Das Verhalten von Frau Musterfrau gegenüber Vorgesetzten, Kolleginnen und Kollegen sowie externen Partnern war stets einwandfrei. Sie führte ihre Mitarbeiterinnen und Mitarbeiter mit klarer Zielorientierung, hoher Wertschätzung und nachhaltigem Erfolg. Ihre Kommunikation war stets klar, konstruktiv und auf das Gesamtergebnis ausgerichtet. Frau Musterfrau genoss das vollste Vertrauen der Geschäftsführung und aller Kolleginnen und Kollegen.

**Schlussformel:**
Frau Musterfrau scheidet auf eigenen Wunsch aus unserem Unternehmen aus. Wir bedauern dies außerordentlich und danken ihr herzlich für ihre hervorragenden Leistungen, ihren unermüdlichen Einsatz und ihren wertvollen Beitrag zum Erfolg unseres Unternehmens. Für ihren weiteren beruflichen und persönlichen Weg wünschen wir ihr nur das Allerbeste und weiterhin großen Erfolg.

Musterstadt, den 28. Februar 2025

[Unterschrift Geschäftsführung]
Max Mustermann, Geschäftsführer

---

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `muster-arbeitszeugnis-gemischte-noten`

_Anonymisiertes Schulungszeugnis mit Schaufenster-Pattern für Training und Demonstration. Anwendungsfall Rechtsanwalt oder Mitarbeiter will Zeugnisanalyse-Skills an einem Musterfall trainieren. Zeigt klassisches Drift-Muster einzelne Saetze Note eins benachbarte Saetze Note drei gleicher Themenbereich. Output vollständige Satz-für-Satz-Notenmatrix mit Bereichs-Drift-Analyse als kommentiertes Lernbeispiel. Abgrenzung zu muster-arbeitszeugnis-mit-roten-flaggen und muster-arbeitszeugnis-note-1._

# Muster-Arbeitszeugnis mit gemischten Noten (Schulungsmaterial)

## Fachlicher Anker

- **Normen:** §§ 611a, §§ 1, §§ 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Satz im Muster | Themenbereich | Note | Befund |
|---|---|---|---|
| "verfuegt auch in Randbereichen ueber aeusserst profundes Fachwissen" | Fachkenntnisse | 1 | Steigerer plus Maximalbereich |
| "nahm regelmaessig erfolgreich an Weiterbildungsseminaren teil" | Lernbereitschaft | 3 | Kein Steigerungsadverb |
| "ausgepraegt strategisches Denkvermoegen, stets in kuerzester Zeit optimale Loesungen" | Strategisches Denken | 1 | "stets" plus Superlativ |
| "zeigte sich bei neuen Aufgabenbereichen flexibel und aufgeschlossen" | Flexibilitaet | 3 | "zeigte" ohne Steigerung |
| "besonders hohe Arbeitsmoral, stets aeusserst motiviert, beharrlich zu verfolgen" | Engagement | 1 | Drei Steigerer |
| "zeigte eine hohe Lernbereitschaft" | Lernbereitschaft | 3 | "hohe" ohne Adverb |
| "jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig, planvoll durchdacht" | Arbeitsweise | 1 | Drei Steigerer |
| "fand gute neue Ideen und innovative Ansaetze" | Innovation | 3 | "gute" statt "hervorragende" |
| "Arbeitsergebnisse lagen stets sehr weit ueber unseren Anforderungen" | Arbeitsergebnis | 1 | Maximalvergleich |
| "war in der Lage, Konflikte erfolgreich zu bewaeltigen" | Sozialverhalten | 3 | "war in der Lage" |
| "vollsten Zufriedenheit erfuellt und teilweise sogar uebertroffen" | Gesamtbeurteilung | 1 | Maximalformel |
| "geschaetzter Ansprechpartner, persönliches Verhalten war einwandfrei" | Sozialverhalten | 3 | "einwandfrei" ohne "stets" |
| "stets ausgezeichnete Mitarbeit" plus volles Bedauern und voller Dank | Schlussformel | 1 | Vollstaendig auf Spitze |

## Beispiele

### Vollstaendiges Muster-Schulungszeugnis

---

**Beispiel GmbH, Beispielstrasse 5, 20000 Beispielstadt**

**Arbeitszeugnis**

Herr Albert Beispiel, geboren am neunten Juni neunzehnhundertsiebzig, war vom ersten Januar zweitausendelf bis zum dreissigsten September zweitausenddreizehn als Baumeister im Bereich Geschaeftsleitung unseres Unternehmens taetig.

Herr Beispiel verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches ueber aeusserst profundes Fachwissen.

Herr Beispiel nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil.

Hervorzuheben ist sein ausgepraegt strategisches Denkvermoegen, das es ihm ermoeglichte, auch bei neuen geschaeftlichen Entwicklungen stets in kuerzester Zeit optimale Loesungen zu entwickeln.

Er zeigte sich auch bei der Bewaeltigung neuer Aufgabenbereiche flexibel und aufgeschlossen.

Herr Beispiel verfuegt ueber eine besonders hohe Arbeitsmoral und war stets aeusserst motiviert, die gesetzten Ziele beharrlich zu verfolgen.

Herr Beispiel zeigte eine hohe Lernbereitschaft.

Alle Aufgaben fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus. Er agierte immer ruhig, ueberlegt und zielorientiert und in hoechstem Masse praezise.

Herr Beispiel war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze.

Die von Herrn Beispiel entwickelten Arbeitsergebnisse lagen stets sehr weit ueber unseren Anforderungen.

Herr Beispiel war in der Lage, Konflikte erfolgreich zu bewaeltigen. Durch sein konstruktives Verhalten und ueberlegtes Handeln konnte er so ein gutes Arbeitsklima in seinem Team schaffen.

Herr Beispiel hat die an ihn gestellten sehr hohen Erwartungen zu unserer vollsten Zufriedenheit erfuellt und teilweise sogar uebertroffen.

Wegen seines freundlichen und hilfsbereiten Auftretens war Herr Beispiel ein geschaetzter Ansprechpartner. Sein persönliches Verhalten gegenueber Vorgesetzten, Mitarbeitern und Externen war einwandfrei.

Das Arbeitsverhaeltnis endet aus betriebsbedingten Gruenden zum dreissigsten September zweitausenddreizehn. Wir bedanken uns für seine stets ausgezeichnete Mitarbeit in unserem Unternehmen. Sein Ausscheiden bedauern wir sehr und wuenschen ihm für seine Zukunft beruflich und privat weiterhin viel Erfolg und alles Gute.

---

### Bereichs-Drift-Analyse

| Themenbereich | Hoechste Note | Niedrigste Note | Drift | Ampel |
|---|---|---|---|---|
| Fachkenntnisse | 1 | 1 | keine | Grün |
| Lernbereitschaft | 1 (indirekt aus Engagement) | 3 | zwei Stufen | Rot |
| Strategisches Denken | 1 | 1 | keine | Grün |
| Flexibilitaet | 3 | 3 | keine | Orange |
| Engagement | 1 | 1 | keine | Grün |
| Arbeitsweise | 1 | 1 | keine | Grün |
| Innovation | 3 | 3 | keine | Orange |
| Arbeitsergebnis | 1 | 1 | keine | Grün |
| Sozialverhalten | 3 | 3 | keine | Orange |
| Gesamtbeurteilung und Schlussformel | 1 | 1 | keine | Grün |

### Gesamtnoten-Aggregation

Gewichteter Wert vor Drift-Penalty: Note 1 bis 2. Drift-Penalty Lernbereitschaft (zwei Stufen, weicher Bereich): minus eine halbe Stufe. Konstante Note 3 in Innovation und Sozialverhalten (heikle weiche Bereiche): minus eine halbe Stufe. Gesamtnote nach Aggregation: Note 2 bis Note 3.

### Empfehlung

Spitzensaetze sind authentisch (Fachkenntnisse, Arbeitsweise, Arbeitsergebnis, Engagement). Drift bei Lernbereitschaft, konstant niedrige Note bei Innovation und Sozialverhalten. Nachverhandelbar: Saetze zu Lernbereitschaft, Innovation und Sozialverhalten. Beweislast nach BAG: Gesamtnote schlechter als befriedigend muesste der Arbeitgeber beweisen, Gesamtnote besser als befriedigend muss der Arbeitnehmer beweisen — bei diesem Zeugnis ist die Drei in den weichen Bereichen aus den Formulierungen selbst herauslesbar.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **§ 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

