---
name: kaltstart-triage
description: "Für Kaltstart Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: bereicherungs-und-anfechtungsrecht-prüfer."
---

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Bereicherungs- und Anfechtungsrecht-Prüfer**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Mechanisches Durchprüfen von Bereicherungsrecht §§ 812 ff. BGB, AnfG und Insolvenzanfechtung §§ 129-147 InsO. Mit KI-Screening von Schuldnerakten, § 135 Gesellschafterdarlehen, Bargeschäft § 142 und Verteidigung des Anfechtungsgegners. Keine Rechtsberatung.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** Wähle zuerst den Skill, der die tragende Weiche zwischen Leistungskondiktion, Nichtleistungskondiktion, Insolvenzanfechtung, BGB-Anfechtung, Fristenlage oder Entreicherungseinwand klärt; bei Vertragsrückabwicklung regelmäßig `weichenstellung-bereicherung-oder-anfechtung`.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Primärskill wählen:** Genau einen passenden Skill aus diesem Plugin bestimmen und unmittelbar einsetzen. Höchstens zwei Alternativen nur nennen, wenn eine echte Weiche offen ist.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule gezielt und sparsam laden

1. Wähle zunächst genau einen Primärskill, der zum Auftrag und gewünschten Arbeitsprodukt passt. Weitere Skills kommen nur bei einer konkreten Schnittstelle hinzu.
2. Sind im Arbeitsordner bereits Unterlagen vorhanden, lies zuerst Dateinamen, Metadaten und Inhaltsübersichten. Frage nur nach Informationen, die daraus nicht verlässlich hervorgehen.
3. Grenze Suchen in Microsoft 365 nach Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und prägnantem Suchbegriff ein. Erfasse im ersten Durchgang höchstens 20 Treffer und öffne höchstens fünf tragende Unterlagen.
4. Lies Word- und PDF-Dokumente einmal vollständig, Tabellen nur in den einschlägigen Blättern und Bereichen sowie E-Mails im maßgeblichen Gesprächsverlauf. Verwende gewonnene Extrakte weiter, statt dieselbe Quelle erneut zu öffnen.
5. Die [vollständige Fachmodulkarte](references/fachmodule.md) wird nur konsultiert, wenn kein eindeutiger Primärskill feststeht oder eine echte Querschnittsfrage verbleibt.

## Worum geht es?

Dieses Plugin prüft mechanisch, welcher Regelungskreis bei Vermögensverschie­bungen einschlägig ist: das Bereicherungsrecht der §§ 812 ff. BGB, die ausserinsolvenzliche Gläubigeranfechtung nach dem AnfG oder die Insolvenzanfechtung nach §§ 129 bis 147 InsO. Es unterstützt Anwälte und Berater bei der Subsumtion, bei der Anspruchsformulierung und bei der Erstellung von Schriftsätzen. Das Plugin ersetzt keine Rechtsberatung und gibt keinen Rechtsrat an Mandanten.

Die Weichenstellung zwischen den drei Regelungskreisen ist die häufigste Fehlerquelle in der Praxis: Ein Bereicherungsanspruch setzt keinen Titel voraus und keinen Insolvenzantrag; eine AnfG-Anfechtung benötigt einen vollstreckbaren Titel ausserhalb der Insolvenz; eine InsO-Anfechtung setzt ein eröffnetes Insolvenzverfahren voraus. Dieses Plugin arbeitet diese Abgrenzung systematisch durch.

## Wann brauchen Sie diese Skill?

- Sie wollen prüfen, ob eine Vermögensverschiebung bereicherungsrechtlich, ausserinsolvenzlich oder insolvenzrechtlich angegriffen werden kann.
- Sie sind Insolvenzverwalter und prüfen Anfechtungsansprüche gegen Gläubiger oder Dritte.
- Sie sind Vollstreckungsgläubiger und wollen eine Vermögensverschiebung des Schuldners anfechten (AnfG).
- Sie müssen als Anfechtungsgegner Verteidigungsargumente strukturieren.
- Sie erstellen Klageschriften, Anfechtungsanzeigen oder Warnhinweise in bereicherungs- oder anfechtungsrechtlichen Mandaten.

## Fachbegriffe (kurz erklärt)

- **Leistungskondiktion** — Rückforderungsanspruch wegen einer Leistung ohne Rechtsgrund (§ 812 Abs. 1 S. 1 Alt. 1 BGB); setzt bewusste und zweckgerichtete Vermehrung fremden Vermögens voraus.
- **Eingriffskondiktion** — Bereicherungsanspruch bei Eingriff in eine fremde Rechtsposition mit Zuweisungsgehalt ohne Leistungsbeziehung (§ 812 Abs. 1 S. 1 Alt. 2 BGB).
- **Entreicherung** — Einrede des Bereicherten, soweit er das Erlangte nicht mehr hat (§ 818 Abs. 3 BGB); bei Bösgläubigkeit ausgeschlossen (§ 819 BGB).
- **AnfG-Anfechtung** — Ausserinsolvenzliche Gläubigeranfechtung durch Vollstreckungsgläubiger mit Titel; schützt vor Vereitelung der Zwangsvollstreckung.
- **Kongruente Deckung** — Befriedigung oder Sicherung, die dem Gläubiger so zustand; nach § 130 InsO anfechtbar bei Zahlungsunfähigkeit und Kenntnis.
- **Inkongruente Deckung** — Befriedigung oder Sicherung, die so nicht oder nicht zu der Zeit beansprucht werden konnte (§ 131 InsO); erleichterte Anfechtbarkeit.
- **Bargeschäft** — unmittelbarer Austausch gleichwertiger Leistungen; schützt nach § 142 InsO, bleibt bei § 133 InsO aber nur geschützt, wenn keine erkannte Unlauterkeit des Schuldners hinzukommt.
- **Vorsatzanfechtung** — Anfechtung wegen Benachteiligungsvorsatzes des Schuldners und Kenntnis des Anfechtungsgegners (§ 133 InsO bzw. § 3 AnfG); längste Anfechtungsfrist.

## Rechtsgrundlagen

- §§ 812 bis 822 BGB — Bereicherungsrecht (Leistungs-, Nichtleistungskondiktion, Umfang, Ausschlüsse).
- §§ 1 bis 15 AnfG — Ausserinsolvenzliche Gläubigeranfechtung.
- §§ 129 bis 147 InsO — Insolvenzanfechtung (Grundtatbestand, Deckungsanfechtung, Vorsatz, Rechtsfolgen).
- § 142 InsO — Bargeschäftsprivileg.
- §§ 195 und 199 BGB — Regelmäßige Verjährung drei Jahre, Beginn mit Jahresende.
- § 15 AnfG — Verjährung AnfG-Anfechtungsanspruch drei Jahre.
- § 146 InsO — Verjährung des Insolvenzanfechtungsanspruchs nach den Regeln der regelmäßigen Verjährung des BGB.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Wer hat was an wen geleistet, wann, gegen welche Gegenleistung?
2. Weichenstellung treffen: Liegt ein eröffnetes Insolvenzverfahren vor? Liegt ein vollstreckbarer Titel vor?
3. Passenden Regelungskreis auswählen: Skill `weichenstellung-bereicherung-oder-anfechtung` oder `triage-vermoegensverschiebung-erfassen`.
4. Fristen prüfen: Skill `verjaehrung-bereicherung-anfechtung-fristen`.
5. Anspruchsgutachten oder Schriftsatz erstellen mit dem Fachmodul des gewählten Regelungskreises.

## Skill-Tour (was gibt es hier?)

**Triage und Weichenstellung**

- `triage-vermoegensverschiebung-erfassen` — Erster Schritt zur strukturierten Erfassung der Vermögensverschiebung für alle drei Regelungskreise.
- `weichenstellung-bereicherung-oder-anfechtung` — Triage-Entscheidung: welcher Regelungskreis ist einschlägig.
- `falsche-wiese-warnung-bereicherung-anfechtung` — Erkennt typische Falschverortungen und leitet zum richtigen Regelungskreis weiter.
- `parallel-und-konkurrenz-pruefung` — Prüft alle drei Regelungskreise gleichzeitig auf Anspruchskonkurrenzen.

**Bereicherungsrecht — Grundtatbestände**

- `leistungskondiktion-grundtatbestand-812-i-1-alt-1` — Leistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 1 BGB im Vier-Schritt-Schema.
- `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` — Nichtleistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 2 BGB.
- `leistungsbegriff-bewusste-zweckgerichtete-mehrung` — Definiert den Leistungsbegriff im Bereicherungsrecht.
- `eingriffskondiktion-zuweisungsgehalt` — Eingriffskondiktion bei Eingriff in fremde Rechtspositionen.

**Bereicherungsrecht — Spezialtatbestände**

- `condictio-indebiti-813-bgb` — Rückforderung trotz Erfüllung einer einredebehafteten Verbindlichkeit.
- `verfuegung-eines-nichtberechtigten-816-bgb` — Anspruch des Berechtigten nach § 816 BGB.
- `bereicherung-eines-dritten-822-bgb` — Bereicherungsanspruch gegen Dritten bei unentgeltlicher Weitergabe.
- `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` — Bereicherungsausgleich in Drei- und Mehrpersonenverhältnissen.

**Bereicherungsrecht — Umfang und Ausschlüsse**

- `umfang-der-herausgabe-818-bgb-und-entreicherung` — Umfang der Bereicherungshaftung und Entreicherungseinrede.
- `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` — Verschärfte Haftung bei Bösgläubigkeit oder Rechtshängigkeit.
- `ausschluss-814-bgb-kenntnis-der-nichtschuld` — Ausschluss bei Kenntnis der Nichtschuld.
- `ausschluss-817-bgb-gesetzes-und-sittenverstoss` — Ausschluss bei eigenem Gesetzes- oder Sittenverstoß.

**Bereicherungsrecht — Konkurrenz**

- `konkurrenz-bereicherung-vertraglich-deliktisch` — Verhältnis Bereicherungsrecht zu vertraglichen und deliktischen Ansprüchen.
- `konkurrenz-bereicherung-anfechtung-und-vindikation` — Anspruchskonkurrenzen zwischen Bereicherungsrecht, Anfechtung und § 985 BGB.

**Ausserinsolvenzliche Anfechtung (AnfG)**

- `anfg-grundtatbestand-und-anfechtungsberechtigte` — Grundvoraussetzungen der ausserinsolvenzlichen Gläubigeranfechtung.
- `anfg-vorsatzanfechtung-3-i` — Vorsatzanfechtung nach § 3 Abs. 1 AnfG mit Zehn-Jahres-Frist.
- `anfg-unentgeltliche-leistung-4` — Anfechtung unentgeltlicher Leistungen nach § 4 AnfG.
- `anfg-mittelbare-benachteiligung-und-kongruenz` — Kongruenz und mittelbare Gläubigerbenachteiligung im AnfG.
- `anfg-rechtsfolge-rueckgewaehr-11` — Duldungspflicht und Wertersatz nach § 11 AnfG.
- `anfg-fristen-und-anfechtungszeitraum` — Anfechtungsfristen im AnfG: zehn Jahre Vorsatz, vier Jahre unentgeltlich.
- `anfg-einreden-und-verteidigung-anfechtungsgegner` — Verteidigung des Anfechtungsgegners gegen AnfG-Klage.
- `anfg-anfechtungsklage-prozessuales` — Prozessuales zur AnfG-Anfechtungsklage.

**Insolvenzanfechtung (§§ 129 ff. InsO)**

- `inso-grundtatbestand-129-glaeubigerbenachteiligung` — Grundtatbestand Insolvenzanfechtung: Rechtshandlung und Gläubigerbenachteiligung.
- `inso-kongruente-deckung-130` — Kongruente Deckungsanfechtung nach § 130 InsO.
- `inso-inkongruente-deckung-131` — Inkongruente Deckungsanfechtung nach § 131 InsO.
- `inso-unmittelbar-nachteilige-rechtshandlungen-132` — Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO.
- `inso-vorsatzanfechtung-133` — Vorsatzanfechtung nach § 133 InsO mit Zehn-Jahres-Grundfrist, Vier-Jahres-Deckungsfrist und § 133 Abs. 3.
- `inso-unentgeltliche-leistung-134` — Anfechtung unentgeltlicher Leistungen nach § 134 InsO.
- `inso-gesellschafterdarlehen-135` — Gesellschafterdarlehen, gleichgestellte Forderungen, Drittdarlehen mit Gesellschaftersicherheit.
- `inso-bargeschaeft-142` — Bargeschäft nach § 142 InsO ohne starre 30-Tage-Regel.
- `inso-rechtsfolge-rueckgewaehr-143-bis-147` — Rechtsfolgen der Insolvenzanfechtung nach §§ 143 bis 147 InsO.
- `inso-ki-anfechtungsansprueche-schuldnerakten` — KI-gestütztes Screening von Schuldnerakten auf mögliche Anfechtungsansprüche mit Beleg- und Human-Review-Matrix.
- `inso-verteidigung-anfechtungsgegner` — Verteidigung gegen Insolvenzanfechtung aus Sicht des Anfechtungsgegners.

**Verjährung und Fristen**

- `verjaehrung-bereicherung-anfechtung-fristen` — Verjährungsfristen im Überblick für alle drei Regelungskreise.

**Output-Skills**

- `output-klageschrift-bereicherungsklage` — Klageschrift aus Bereicherungsrecht §§ 812 ff. BGB aufbauen.
- `output-anfechtungsanzeige-insolvenzverwalter` — Anschreiben des Insolvenzverwalters an Anfechtungsgegner erstellen.
- `output-anfechtungsklage-anfg` — Klageschrift für AnfG-Anfechtungsklage des Vollstreckungsgläubigers.
- `output-warnhinweis-und-pruefungsdokument` — Pflicht-Header und Warnblock für alle Prüfungsdokumente.

**Mandatssteuerung**

- `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` — Erkennt Komplexitätsindikatoren und empfiehlt Fachanwalt.

## Worauf besonders achten

- **Weichenstellung zuerst** — Die Verwechslung von Bereicherungsrecht, AnfG und InsO-Anfechtung ist der häufigste systematische Fehler; `weichenstellung-bereicherung-oder-anfechtung` immer zuerst aufrufen.
- **Insolvenzeröffnung als Voraussetzung** — InsO-Anfechtung durch Insolvenzverwalter setzt eröffnetes Verfahren voraus; ohne Eröffnungsbeschluss ist nur AnfG einschlägig.
- **Bargeschäft bei InsO-Anfechtung prüfen** — § 142 InsO schützt echten gleichwertigen Austausch; bei § 133 InsO zusätzlich erkannte Unlauterkeit prüfen.
- **Vorsatzanfechtung Reform 2017** — § 133 InsO wurde durch das Anfechtungsreformgesetz 2017 erheblich verändert; allgemeine Zehn-Jahres-Frist, Vier-Jahres-Frist für Deckungshandlungen und Zwei-Jahres-Regel bei § 133 Abs. 4 sauber trennen.
- **KI nur beleggebunden einsetzen** — KI darf Kandidaten und Indizien aus Schuldnerakten aufbereiten, aber § 133-Wertungen und komplexe Dreiecksverhältnisse nicht final entscheiden.
- **Entreicherungseinrede rechtzeitig prüfen** — § 818 Abs. 3 BGB wird häufig vergessen; bei Bösgläubigkeit (§ 819 BGB) greift sie jedoch nicht.

## Typische Fehler

- Mandant hat keinen Titel, will aber AnfG-Anfechtung betreiben — AnfG setzt vollstreckbaren Titel voraus.
- Bereicherungsanspruch wird geltend gemacht, obwohl ein vertraglicher Anspruch vorgeht und keine Subsidiarität überprüft wurde.
- Vorsatzanfechtung nach § 133 InsO wird mit der alten Rechtslage oder mit falscher Vier-Jahres-Pauschale argumentiert.
- Dreimonatsfrist des § 130 InsO wird von der Antragstellung, nicht von der Eröffnung her berechnet.
- Warnhinweis auf fehlenden Rechtsberatungscharakter fehlt im Dokument.

## Quellen und Aktualität

- Stand: 05/2026
- BGB §§ 812 ff. in der geltenden Fassung
- InsO §§ 129 ff. in der Fassung nach dem AnfRefG 2017
- AnfG in der geltenden Fassung
