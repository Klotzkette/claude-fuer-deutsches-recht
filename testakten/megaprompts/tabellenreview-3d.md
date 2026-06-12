# Megaprompt: tabellenreview-3d

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 84 Skills des Plugins `tabellenreview-3d`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Tabellenreview (Excel/CSV): ordnet Rolle (Datenverantwortlicher, Prüfer), markiert Fris…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Tabellenreview 3d-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und…
3. **tabellenreview-erstpruefung-und-mandatsziel** — Tabellenreview: Erstprüfung, Rollenklärung und Mandatsziel.
4. **arbeitsblatt-perspektiven-definieren** — Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO.…
5. **audit-trail-protokoll** — Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchfüh…
6. **kreuzblatt-konsistenzpruefung** — Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen:…
7. **review-durchfuehren** — 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176…
8. **start-chronologie-fristen** — Einstieg, Schnelltriage und Fallrouting im Tabellenreview 3d-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und…
9. **vorlage-ma-arbeitsblatt-perspektiven-audit** — Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, Akt…
10. **vorlage-ma-due-diligence** — Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, Akt…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Tabellenreview (Excel/CSV): ordnet Rolle (Datenverantwortlicher, Prüfer), markiert Frist (keine harten Fristen), wählt Norm (GoBD, Tax compliance) und Zuständigkeit (Finanzamt), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Tabellenreview 3d** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aggregation-spaltenprompts-definieren` — Aggregation Spaltenprompts Definieren
- `arbeitsblatt-perspektiven-definieren` — Arbeitsblatt Perspektiven Definieren
- `arbeitsblatt-schriftsatz-brief-memo-bausteine` — Arbeitsblatt Schriftsatz Brief Memo Bausteine
- `arbeitsblatt-schriftsatz-brief-und-memo-bausteine` — Arbeitsblatt Schriftsatz Brief und Memo Bausteine
- `audit-trail-protokoll` — Audit Trail Protokoll
- `belegkette-rueckverfolgung` — Belegkette Rueckverfolgung
- `belegkette-rueckverfolgung-caching-rerun` — Belegkette Rueckverfolgung Caching Rerun
- `caching-und-teil-rerun` — Caching und Teil Rerun
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `datenpunkt-dokument-excel-beweislast` — Datenpunkt Dokument Excel Beweislast
- `datenpunkt-dokumentenmatrix-lueckenliste` — Datenpunkt Dokumentenmatrix Lueckenliste
- `dokument-behoerden-gericht-und-registerweg` — Dokument Behoerden Gericht und Registerweg
- `dokumentstapel-aufnehmen` — Dokumentstapel Aufnehmen
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Tabellenreview 3D sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Tabellenreview 3d-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig:_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Tabellenreview 3d** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Tabellenreview 3d**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** 3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette.

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
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
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

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `arbeitsblatt-perspektiven-definieren` | Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster,… |
| `audit-trail-protokoll` | Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output:… |
| `belegkette-rueckverfolgung` | Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output:… |
| `caching-und-teil-rerun` | Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten… |
| `dokumentstapel-aufnehmen` | Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output:… |
| `excel-multi-sheet-export` | 3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei… |
| `kreuzblatt-konsistenzpruefung` | Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege.… |
| `pdf-bericht-erzeugen` | 3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Prüfraster: Vollständigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview.… |
| `prompt-versionierung` | Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output:… |
| `pruefer-uebergabe-paket` | Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für… |
| `review-durchfuehren` | 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung.… |
| `risikoampel-aggregation` | Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht.… |
| `spaltenprompts-definieren` | Spaltenprompts für die drei Prüfperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument.… |
| `tabellenreview-3d-kaltstart-interview` | Kaltstart-Interview für den 3D-Tabellenreview: Fallkategorie, Tabellengrösse, Prüfzweck erfassen. Normen: §§ 174 ff. InsO, HGB. Prüfraster: Zweck, Datenlage, Perspektivenwahl, Exportformat. Output:… |
| `vorlage-arbeitsvertrag-portfolio` | Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format: Forderung/Prüfung/Stellung. Normen: BGB, KSchG, ArbZG. Prüfraster: Vertragsbedingungen, Klauselgueltigkeit, HR-Compliance. Output:… |
| `vorlage-immobilien-portfolio` | Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format. Normen: §§ 535 ff. BGB, WEG, GrEStG. Prüfraster: Miete, Grundbuch, steuerliche Belastung, Instandhaltung. Output: Immobilien-Portfolio-Tabelle.… |
| `vorlage-ma-due-diligence` | Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output:… |
| `vorlage-vendor-onboarding-3d` | Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output:… |
| `wuerfel-aufbauen` | 3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output:… |
| `zeilenprompts-definieren` | Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Zeilentyp, Normverankerung, Eindeutigkeit. Output: Zeilenprompts-Dokument.… |

## Worum geht es?

Das Plugin strukturiert die Massenpruefung von Vertragsstapeln und Due-Diligence-Unterlagen als dreidimensionalen Wuerfel: Die erste Dimension sind Spaltenprompts, die je einen Pruefpunkt (z. B. Kuendigungsklausel, Laufzeit) abfragen. Die zweite Dimension sind Zeilenprompts, die jedes einzelne Dokument des Stapels repraesentieren. Die dritte Dimension sind Arbeitsblatt-Perspektiven, die denselben Datensatz aus unterschiedlichen fachlichen Blickwinkeln betrachten (Recht, Steuer, Wirtschaft).

Das Ergebnis wird als Excel-Datei mit mehreren Arbeitsblaettern exportiert, enthaelt eine Kreuzblatt-Konsistenzpruefung auf Widersprueche zwischen den Dimensionen, einen lueckenlosen Audit-Trail und eine Belegketten-Dokumentation. Typische Einsaetzgebiete sind M-und-A-Due-Diligence, Immobilien-Portfoliopruefung, Vendor-Onboarding und Arbeitsvertrags-Portfolio-Review.

## Wann brauchen Sie diese Skill?

- Sie muessen 20 oder mehr Vertraege auf dieselben Pruefpunkte hin systematisch analysieren und das Ergebnis auswertbar dokumentieren.
- Eine M-und-A-Due-Diligence erfordert die gleichzeitige Betrachtung von Vertraegen aus rechtlicher, steuerlicher und wirtschaftlicher Perspektive.
- Ein Lieferant soll ongeboardet werden und Vertrag, Compliance-Status und Leistungsindikatoren muessen dokumentiert werden.
- Der Pruefer wechselt und das bisher bearbeitete Paket soll mit vollem Kontext und offenem Status uebergeben werden.
- Zwischenergebnisse sollen gecacht und einzelne Teile ohne Vollneustart erneut ausgefuehrt werden.

## Fachbegriffe (kurz erklaert)

- **Wuerfel** — Metapher für die dreidimensionale Pruefstruktur: Zeilen (Dokumente) x Spalten (Pruefpunkte) x Perspektiven (Blickwinkel).
- **Spaltenprompt** — Einzelne Frage oder Pruefanweisung, die für jedes Dokument in einer bestimmten Spalte beantwortet wird.
- **Zeilenprompt** — Dokumentspezifische Pruefanweisung, die das einzelne Dokument als Pruefgegenstand definiert.
- **Arbeitsblatt-Perspektive** — Fachlicher Blickwinkel (Recht, Steuer, Wirtschaft), der denselben Wuerfel in einem eigenen Excel-Sheet abbildet.
- **Kreuzblatt-Konsistenzpruefung** — Abgleich der drei Dimensionen auf Widersprueche und fehlende Eintraege.
- **Audit-Trail** — Lueckenlose Protokollierung aller Pruefschritte mit Zeitstempel, Pruefer-ID und Aenderungshistorie.
- **Risikoampel** — Rot-Gelb-Gruen-Bewertung je Pruefposition zur schnellen Risikouebersicht.
- **Belegkette** — Nachverfolgung der Originalbelege hinter jeder Buchung oder Forderung.

## Rechtsgrundlagen

- §§ 174 ff. InsO — Forderungsanmeldung und -pruefung (Stammreferenz der 3D-Review-Skills)
- §§ 238 257 HGB — Buchfuehrungs- und Aufbewahrungspflichten
- GmbHG AktG HGB InsO — Relevante Normen je nach Vorlagen-Typ
- BGB §§ 305 ff. — AGB-Kontrolle bei Vertragsstapeln
- BetrAVG — Bei Arbeitsvertrag-Portfolio-Reviews
- DSGVO Art. 5 — Datensparsamkeit bei Verarbeitung von Vertragsdaten

## Schritt-für-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview: Fallkategorie, Tabellengroesse, Pruefzweck und Exportformat erfassen.
2. Wuerfelstruktur aufbauen: Spaltenprompts und Zeilenprompts definieren, Perspektiven festlegen.
3. Dokumentstapel einlesen und Inventar erstellen.
4. Review durchfuehren: jede Zeile in allen drei Perspektiven pruefen und Risikoampel setzen.
5. Kreuzblatt-Konsistenzpruefung und Audit-Trail abschliessen; Excel-Export oder PDF-Bericht erzeugen.

## Skill-Tour (was gibt es hier?)

- `arbeitsblatt-perspektiven-definieren` — Die drei Pruefperspektiven (Recht, Steuer, Wirtschaft) für den 3D-Wuerfel definieren.
- `audit-trail-protokoll` — Alle Review-Schritte mit Zeitstempel und Pruefer-ID protokollieren.
- `belegkette-rueckverfolgung` — Belegkette für Forderungen und Zahlungen zurueckverfolgen.
- `caching-und-teil-rerun` — Zwischenergebnisse cachen und Teilbereiche ohne Vollneustart erneut ausfuehren.
- `dokumentstapel-aufnehmen` — Dokumentenstapel (PDFs, Excel, Word) einlesen und Inventar erstellen.
- `excel-multi-sheet-export` — 3D-Review-Ergebnis als Excel-Datei mit Arbeitsblaettern je Perspektive exportieren.
- `kreuzblatt-konsistenzpruefung` — Abgleich der drei Dimensionen auf Widersprueche und fehlende Eintraege.
- `pdf-bericht-erzeugen` — 3D-Review-Ergebnis als PDF-Bericht mit Zusammenfassung, Tabellen und Risikoampeln erzeugen.
- `prompt-versionierung` — Prompt-Versionen für den 3D-Review verwalten und aendern.
- `pruefer-uebergabe-paket` — Uebergabepaket für Prueferwechsel mit aktuellem Stand und offenen Positionen.
- `review-durchfuehren` — 3D-Tabellenreview konkret durchfuehren: jede Zeile in allen drei Perspektiven pruefen.
- `risikoampel-aggregation` — Risikoampeln für alle geprueften Positionen aggregieren und Gesamtrisiko einschaetzen.
- `spaltenprompts-definieren` — Spaltenprompts für die drei Pruefperspektiven definieren.
- `tabellenreview-3d-kaltstart-interview` — Kaltstart-Interview: Fallkategorie, Tabellengroesse, Pruefzweck und Exportformat erfassen.
- `vorlage-arbeitsvertrag-portfolio` — Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format.
- `vorlage-immobilien-portfolio` — Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format.
- `vorlage-ma-due-diligence` — Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format.
- `vorlage-vendor-onboarding-3d` — Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format.
- `wuerfel-aufbauen` — 3D-Wuerfelstruktur aufbauen: Zeilen, Spalten und Perspektiven verknuepfen.
- `zeilenprompts-definieren` — Zeilenprompts für einzelne Pruefpositionen im 3D-Review definieren.

## Worauf besonders achten

- **Kreuzblatt-Konsistenz vor Export pruefen**: Widersprueche zwischen den Dimensionen koennen die Aussagekraft des Berichts untergraben.
- **Prompt-Versionierung dokumentieren**: Unterschiedliche Prompt-Versionen im selben Review produzieren nicht vergleichbare Ergebnisse.
- **Audit-Trail von Beginn an fuehren**: Nachtraegliches Erganzen des Protokolls ist fehleranfaellig und im Zweifel nicht beweissicher.
- **Caching konservativ einsetzen**: Gecachte Ergebnisse werden nicht neu berechnet; Aenderungen im Dokument werden nicht erfasst.
- **Vorlagen nicht ohne Anpassung verwenden**: Vorlage-Spaltenprompts sind Ausgangspunkte, keine abschliessenden Pruefkataloge.

## Typische Fehler

- Wuerfelstruktur ohne Kaltstart-Interview aufbauen; Pruefzweck und Exportformat werden spaeter nicht erfuellt.
- Alle drei Perspektiven mit identischen Prompts besetzen; der Wuerfel verliert seine Informationstiefe.
- Risikoampel-Schwellenwerte nicht explizit definieren; Ampelbewertungen werden inkonsistent.
- Prueferwechsel ohne Uebergabepaket; Nachfolger muss von vorne beginnen.
- Excel-Export ohne Kreuzblatt-Pruefung; Inkonsistenzen werden erst beim Mandanten entdeckt.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum

---

## Skill: `tabellenreview-erstpruefung-und-mandatsziel`

_Tabellenreview: Erstprüfung, Rollenklärung und Mandatsziel._

# Tabellenreview: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Tabellenreview Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Tabellenreview 3d** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Tabellenreview: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** Aufgabenbezogen statt Platzhalter: HGB §§ 238, 257; AO § 147; ZPO §§ 371 ff. bei Urkunden/elektronischen Dokumenten; DSGVO Art. 5, 6, 32; GoBD; Mandats-/Datenraumvorgaben. Bei rein wirtschaftlicher Tabellenprüfung keine Scheinnorm erfinden.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Tabellenreview** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `arbeitsblatt-perspektiven-definieren`

_Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster, Gläubigerstellung. Output: Perspektivendefinition als Grundlage für Wuerfel-Aufbau. Abgrenzung:..._

# /tabellenreview-3d:arbeitsblatt-perspektiven-definieren

## Triage zu Beginn

1. Wie viele Perspektiven sind erforderlich? (Recht / Steuer / Wirtschaft / Datenschutz / IT)
2. Muss jede Perspektive von einem anderen Pruefer verantwortet werden?
3. Gibt es GwG-Compliance-Anforderungen? → Separate Compliance-Perspektive (LkSG / GwG / IDW PS 980)
4. Ist ein M&A-Closing-Datum bekannt? → Fristen der Arbeitsblaetter entsprechend konfigurieren

## Rechtliche Grundlagen für Pruefer-Perspektiven

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Standard-Perspektiven

### Recht (Anwaltsperspektive)

- Spalten: AGB-Wirksamkeit Haftungsregime Verjährungsverkürzung Gerichtsstand Schiedsklausel Schriftformklausel
- Materialität: rot bei Klauseln die nach BGB Paragraph 307 unwirksam sind
- Prüfer: zugelassener Rechtsanwalt

### Steuer (Steuerberater)

- Spalten: Umsatzsteuer-Behandlung Rechnungspflichtangaben UStG Paragraph 14 grenzüberschreitend ja / nein Reverse-Charge ja / nein
- Materialität: rot bei UStG-Compliance-Risiken
- Prüfer: Steuerberater oder Wirtschaftsprüfer

### Wirtschaft (Buyside-Analyst)

- Spalten: Vertragsvolumen Laufzeit Kündigungsdatum Preisanpassungsmechanik Working-Capital-Effekt
- Materialität: rot bei Top-5-Kunden-Konzentration über 60 Prozent
- Prüfer: Deal-Lead / Corp-Dev

### Datenschutz (DSGVO-Beauftragter)

- Spalten: Datenkategorien Rechtsgrundlage Auftragsverarbeitung-Pflicht AVV vorhanden Drittlandtransfer SCC vorhanden
- Materialität: rot bei fehlender AVV trotz Auftragsverarbeitung (DSGVO Artikel 28)
- Prüfer: Datenschutzbeauftragter

### IT (Architekt)

- Spalten: Hosting-Modell Verschlüsselungs-Standard Lock-in-Risiko Schnittstellen-Dokumentation Exit-Daten-Format
- Materialität: rot bei nicht standardisierten Datenformaten ohne Exit-Pflicht
- Prüfer: IT-Architekt

### Betrieb (Operations)

- Spalten: Service-Level Reaktionszeit Wiederherstellungszeit Eskalationsstufen Vertretungsregelung
- Materialität: rot bei SLA-Reaktionszeit über 4 Stunden bei produktionskritischen Services
- Prüfer: Operations-Lead

### Compliance (GwG / LkSG)

- Spalten: Wirtschaftlich Berechtigter bekannt Sanktionslisten-Prüfung Lieferketten-Risiko-Region nach LkSG
- Materialität: rot bei Sanktionslisten-Treffer
- Prüfer: Compliance-Officer

## Pflichtfelder pro Arbeitsblatt

```yaml
- id: recht
 titel: "Rechtliche Perspektive"
 perspektive: "anwalt"
 pruefer-rolle: "rechtsanwalt"
 eigene-spalten-zusaetze:
 - id: agb-wirksamkeit
 prompt: "Sind die AGB-Klauseln nach BGB Paragraph 305 ff. wirksam?"
 auslassungen:
 - umsatzsteuer # Steuerblatt; hier nicht zuständig
 ampel-regel:
 rot: "Unwirksame Klausel BGB Paragraph 307"
 gelb: "AGB-Wirksamkeit zweifelhaft"
 gruen: "Wirksam oder Individualvereinbarung"
```

## Stapelung

Die Arbeitsblätter werden in der Excel-Ausgabe als Tabellenreiter nebeneinander dargestellt. Im PDF-Bericht erscheinen sie als aufeinanderfolgende Abschnitte. In `kreuzblatt-konsistenzpruefung` werden Widersprüche zwischen Arbeitsblättern gefunden (z. B. ein Vertrag der rechtlich grün aber wirtschaftlich rot ist — das ist legitim und soll markiert werden).

## Ausgabe

- `arbeitsblaetter.yaml` mit allen Arbeitsblättern, deren Spaltenzusätze, Auslassungen und Prüfer-Rollen
- `arbeitsblatt-matrix.md` als menschenlesbare Übersicht

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 2 JVEG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- § 29 VwVfG
- § 1 KSchG
- § 7 KSchG
- § 102 BetrVG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `audit-trail-protokoll`

_Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output: Audit-Trail-Protokoll. Abgrenzung: nicht inhaltliche Prüfung (Zweck: Nachvollziehb..._

# /tabellenreview-3d:audit-trail-protokoll

## Triage zu Beginn

1. Fuer welches Mandat / Projekt wird der Audit-Trail gefuehrt? (M&A-DD / Immobilien / Vendor)
2. Wer ist der verantwortliche Pruefer, der jede Abnahme unterschreiben muss?
3. Muss der Audit-Trail gerichtsfest sein? → Append-only-Format (JSONL) waehlen
4. Gibt es berufsrechtliche Aufbewahrungspflichten? (§ 50 BRAO: 5 Jahre Mandatsakte)

## Rechtliche Grundlagen zur Dokumentationspflicht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ereignistypen

### Würfel-Lebenszyklus

- `würfel.erstellt` — Würfel-Schema neu angelegt
- `würfel.dimension-erweitert` — Spalte / Zeile / Arbeitsblatt hinzugefügt
- `würfel.dimension-gekuerzt` — Spalte / Zeile / Arbeitsblatt entfernt
- `würfel.archiviert` — Würfel abgeschlossen

### Prompts

- `prompt.erstellt` — neuer Spalten- oder Zeilenprompt definiert
- `prompt.geändert` — Prompt-Wortlaut geändert (Versions-ID erhöht)
- `prompt.deaktiviert` — Prompt aus aktivem Schema genommen

### Reviewlauf

- `lauf.gestartet` — Reviewlauf begonnen, mit Würfel-Snapshot-Hash
- `lauf.beendet` — Reviewlauf beendet, mit Ergebnis-Hash
- `lauf.fehler` — Reviewlauf abgebrochen, mit Fehlermeldung

### Caching

- `cache.treffer` — Zelle aus Cache übernommen, Quell-Zell-ID
- `cache.invalidiert` — Cache-Eintrag verworfen weil Prompt-Version geändert

### Prüfer-Workflow

- `prüferflag.gesetzt` — Zelle braucht menschliche Prüfung, Grund
- `prüferabnahme.eingegeben` — Prüfer hat abgehakt, Prüfer-ID und Entscheidung
- `prüfer.kommentar` — Prüfer-Kommentar zu Zelle

### Belegkette

- `datei.gehasht` — Hash einer Quelldatei berechnet
- `hash-bruch` — Quelldatei-Hash weicht vom registrierten Hash ab (Manipulationsverdacht)

## Pflichtfelder pro Eintrag

```json
{
 "zeitstempel": "2026-05-20T14:23:11Z",
 "aktion": "lauf.beendet",
 "verantwortlicher": "system",
 "würfel-version": "v3",
 "prompt-version": "p12",
 "modell-version": "claude-opus-4-7",
 "eingangs-hash": "sha256:...",
 "ausgangs-hash": "sha256:...",
 "anzahl-zellen": 4176,
 "anzahl-prüferflag": 87,
 "begründung": "Standardlauf nach Schema-Änderung Spalte 'MAC'"
}
```

## Ablage

- `audit-trail.jsonl` — append-only, eine JSON-Zeile pro Ereignis. Nie ändern, nur anhängen.
- `audit-trail.md` — periodisch zu menschenlesbarem Markdown verdichtet (z. B. wochenweise).

## Integritaet

- Jeder Eintrag enthält den Hash des vorherigen Eintrags (Chain-of-Trust). Wer einen Eintrag ändert bricht die Kette.
- Optional: kryptografische Signatur des Prüfers bei Abnahme-Ereignissen.

## Verwendung

- Pflicht vor jeder Mandatsübergabe — der Prüfer signiert den letzten Audit-Stand.
- Bei Beschwerden Aufsicht oder Haftungsfrage rückverfolgbar nachweisen welcher Reviewlauf welchen Output produziert hat.
- Verhindert dass Prompts schleichend geändert werden und alte Zellen `nicht mehr nachvollziehbar` sind.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 2 JVEG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- § 29 VwVfG
- § 1 KSchG
- § 7 KSchG
- § 102 BetrVG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `kreuzblatt-konsistenzpruefung`

_Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege. Output: Konsistenz-Prüfbericht mit Fehlerliste. Abgrenzung: nicht Risikoampel-Aggreg..._

# /tabellenreview-3d:kreuzblatt-konsistenzprüfung

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Methodik

1. **Achsen-Match:** dieselbe Zeile dieselbe Spalte aber unterschiedliches Arbeitsblatt: vergleichen.
2. **Faktischer Widerspruch:** beide Arbeitsblätter haben das Vertragsdatum extrahiert; das eine sagt 2021-03-15, das andere 2021-03-25. Das ist ein Datenfehler — Prüfer-Flag.
3. **Perspektivischer Widerspruch:** ein Arbeitsblatt sagt 'wirksam' das andere 'unwirksam'. Wenn beide Arbeitsblätter dieselbe Norm benutzen ist es Datenfehler; wenn unterschiedliche Normen (Recht vs Steuer) ist es legitime Abweichung — als `legitim` markieren.
4. **Ampel-Inkonsistenz:** dieselbe Zeile in einem Arbeitsblatt rot in einem gelb in einem grün — Konsolidierungsempfehlung an `risikoampel-aggregation`.
5. **Norm-Bezugs-Widerspruch:** ein Arbeitsblatt verweist auf BGB Paragraph 307, ein anderes auf BGB Paragraph 305c bei derselben Klausel. Beides möglich — Prüfer-Hinweis.

## Konflikt-Klassifikation

- **echter Widerspruch:** beide Antworten beanspruchen dieselbe Tatsache aber unterscheiden sich. Prüfer-Flag rot.
- **legitime perspektivische Abweichung:** Arbeitsblätter haben unterschiedliche Pruefmassstaebe. Vermerk gelb.
- **Datenfehler:** OCR-Konfidenz schwach in einem der Arbeitsblätter — Re-Run dieser Zelle.
- **Klassifikationsfehler:** Dokumenttyp falsch erkannt — Zeile neu klassifizieren.

## Ausgabe

- `widerspruchsbericht.md` mit pro Widerspruch:
 - Zeile (Dokument)
 - Spalte (Datenpunkt)
 - Arbeitsblatt-A und Arbeitsblatt-B mit jeweiliger Antwort
 - Konflikt-Klassifikation
 - Empfohlene Aktion (Re-Run / Prüfer / Konsolidierung)

## Beispiele

- **echter Widerspruch:** Kundenvertrag-042. Spalte 'Laufzeit'. Recht: '3 Jahre + 1 Jahr Verlängerung'. Wirtschaft: '4 Jahre Festlaufzeit'. Echter Widerspruch — Wirtschaft hat den Vertrag verkürzt gelesen.
- **legitime Abweichung:** Lizenzvertrag-018. Spalte 'Haftung'. Recht: 'unwirksam BGB Paragraph 309 Nr 7'. Steuer: 'irrelevant — Pauschalhaftungs-Aufwand absetzbar'. Legitim — unterschiedliche Pruefmassstaebe.

---

## Skill: `review-durchfuehren`

_3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung. Output: Ausgefuellte 3D-Review-Tabelle. Abgrenzung: nicht Wuerfel-Aufbau (Vorbere..._

# /tabellenreview-3d:review-durchführen

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- `wuerfel-schema.yaml`
- `spaltenprompts.yaml`
- `zeilenprompts.yaml`
- `arbeitsblaetter.yaml`
- `zeilen-inventar.yaml`
- Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md`

## Ablauf pro Zelle

1. **Prompt zusammenführen:** Arbeitsblatt-Perspektive vor Spaltenprompt vor Zeilenprompt. Konflikte protokollieren.
2. **Quelldokument öffnen:** Pfad + Hash gegen Inventar abgleichen — falls Hash abweicht: Belegkette unterbrochen Prüfer-Flag setzen.
3. **Antwort extrahieren:** Antworttyp aus Spaltenprompt-Definition beachten (Freitext / zitat-mit-fundstelle / ja-nein / Datum / Geldbetrag / Aufzählung).
4. **Belegkette schreiben:** wörtliches Zitat in Anführungszeichen, danach Fundstelle (Datei-ID + Seite + Absatz + ggf. Ziffer).
5. **Ampel setzen:** anhand `ampel-regel` aus dem Spaltenprompt (rot / gelb / grün).
6. **Prüfer-Flag setzen wenn:**
 - OCR-Konfidenz unter 90 Prozent
 - Antworttyp `zitat-mit-fundstelle` aber kein Zitat extrahierbar
 - Konflikt zwischen Spalten- und Zeilenprompt
 - Mehrdeutigkeit (mehrere plausible Antworten im Dokument)
7. **Querweis aufbauen:** wenn Zellen-Ergebnis auf anderen Vertrag referenziert (`siehe Anlage 7 zu Vertrag X`) als Cross-Ref vermerken.
8. **Cache prüfen:** bei Quasi-Duplikaten (Ähnlichkeit über 95 Prozent) zur Zelle eines bereits geprüften Dokuments Cache-Treffer vorschlagen — Prüfer entscheidet ob übernommen.

## Reihenfolge

Standard: Arbeitsblatt-außen, Zeile-mittel, Spalte-innen. Optional: Spalte-außen wenn Spaltenprompt aufwaendig (z. B. Volltext-Indexierung) und über den Stapel gemeinsam profitiert.

## Grenzen

Jede Zelle ist ein Hinweis kein Befund. Prüfer-Flags sind die wichtigste Ausgabe — sie sagen wo der menschliche Prüfer hinschauen muss. Untermarkierung ist eine Einbahnstraße; Übermarkierung ist eine Zweiwegtür die ein Anwalt in 30 Sekunden schließt.

---

## Skill: `start-chronologie-fristen`

_Einstieg, Schnelltriage und Fallrouting im Tabellenreview 3d-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig:_

# Tabellenreview 3D — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Tabellenreview 3d**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** 3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette.

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
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
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

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `arbeitsblatt-perspektiven-definieren` | Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster,… |
| `audit-trail-protokoll` | Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output:… |
| `belegkette-rueckverfolgung` | Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output:… |
| `caching-und-teil-rerun` | Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten… |
| `dokumentstapel-aufnehmen` | Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output:… |
| `excel-multi-sheet-export` | 3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei… |
| `kreuzblatt-konsistenzpruefung` | Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege.… |
| `pdf-bericht-erzeugen` | 3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Prüfraster: Vollständigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview.… |
| `prompt-versionierung` | Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output:… |
| `pruefer-uebergabe-paket` | Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für… |
| `review-durchfuehren` | 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung.… |
| `risikoampel-aggregation` | Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht.… |
| `spaltenprompts-definieren` | Spaltenprompts für die drei Prüfperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument.… |
| `tabellenreview-3d-kaltstart-interview` | Kaltstart-Interview für den 3D-Tabellenreview: Fallkategorie, Tabellengrösse, Prüfzweck erfassen. Normen: §§ 174 ff. InsO, HGB. Prüfraster: Zweck, Datenlage, Perspektivenwahl, Exportformat. Output:… |
| `vorlage-arbeitsvertrag-portfolio` | Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format: Forderung/Prüfung/Stellung. Normen: BGB, KSchG, ArbZG. Prüfraster: Vertragsbedingungen, Klauselgueltigkeit, HR-Compliance. Output:… |
| `vorlage-immobilien-portfolio` | Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format. Normen: §§ 535 ff. BGB, WEG, GrEStG. Prüfraster: Miete, Grundbuch, steuerliche Belastung, Instandhaltung. Output: Immobilien-Portfolio-Tabelle.… |
| `vorlage-ma-due-diligence` | Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output:… |
| `vorlage-vendor-onboarding-3d` | Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output:… |
| `wuerfel-aufbauen` | 3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output:… |
| `zeilenprompts-definieren` | Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Zeilentyp, Normverankerung, Eindeutigkeit. Output: Zeilenprompts-Dokument.… |

## Worum geht es?

Das Plugin strukturiert die Massenpruefung von Vertragsstapeln und Due-Diligence-Unterlagen als dreidimensionalen Wuerfel: Die erste Dimension sind Spaltenprompts, die je einen Pruefpunkt (z. B. Kuendigungsklausel, Laufzeit) abfragen. Die zweite Dimension sind Zeilenprompts, die jedes einzelne Dokument des Stapels repraesentieren. Die dritte Dimension sind Arbeitsblatt-Perspektiven, die denselben Datensatz aus unterschiedlichen fachlichen Blickwinkeln betrachten (Recht, Steuer, Wirtschaft).

Das Ergebnis wird als Excel-Datei mit mehreren Arbeitsblaettern exportiert, enthaelt eine Kreuzblatt-Konsistenzpruefung auf Widersprueche zwischen den Dimensionen, einen lueckenlosen Audit-Trail und eine Belegketten-Dokumentation. Typische Einsaetzgebiete sind M-und-A-Due-Diligence, Immobilien-Portfoliopruefung, Vendor-Onboarding und Arbeitsvertrags-Portfolio-Review.

## Wann brauchen Sie diese Skill?

- Sie muessen 20 oder mehr Vertraege auf dieselben Pruefpunkte hin systematisch analysieren und das Ergebnis auswertbar dokumentieren.
- Eine M-und-A-Due-Diligence erfordert die gleichzeitige Betrachtung von Vertraegen aus rechtlicher, steuerlicher und wirtschaftlicher Perspektive.
- Ein Lieferant soll ongeboardet werden und Vertrag, Compliance-Status und Leistungsindikatoren muessen dokumentiert werden.
- Der Pruefer wechselt und das bisher bearbeitete Paket soll mit vollem Kontext und offenem Status uebergeben werden.
- Zwischenergebnisse sollen gecacht und einzelne Teile ohne Vollneustart erneut ausgefuehrt werden.

## Fachbegriffe (kurz erklaert)

- **Wuerfel** — Metapher für die dreidimensionale Pruefstruktur: Zeilen (Dokumente) x Spalten (Pruefpunkte) x Perspektiven (Blickwinkel).
- **Spaltenprompt** — Einzelne Frage oder Pruefanweisung, die für jedes Dokument in einer bestimmten Spalte beantwortet wird.
- **Zeilenprompt** — Dokumentspezifische Pruefanweisung, die das einzelne Dokument als Pruefgegenstand definiert.
- **Arbeitsblatt-Perspektive** — Fachlicher Blickwinkel (Recht, Steuer, Wirtschaft), der denselben Wuerfel in einem eigenen Excel-Sheet abbildet.
- **Kreuzblatt-Konsistenzpruefung** — Abgleich der drei Dimensionen auf Widersprueche und fehlende Eintraege.
- **Audit-Trail** — Lueckenlose Protokollierung aller Pruefschritte mit Zeitstempel, Pruefer-ID und Aenderungshistorie.
- **Risikoampel** — Rot-Gelb-Gruen-Bewertung je Pruefposition zur schnellen Risikouebersicht.
- **Belegkette** — Nachverfolgung der Originalbelege hinter jeder Buchung oder Forderung.

## Rechtsgrundlagen

- §§ 174 ff. InsO — Forderungsanmeldung und -pruefung (Stammreferenz der 3D-Review-Skills)
- §§ 238 257 HGB — Buchfuehrungs- und Aufbewahrungspflichten
- GmbHG AktG HGB InsO — Relevante Normen je nach Vorlagen-Typ
- BGB §§ 305 ff. — AGB-Kontrolle bei Vertragsstapeln
- BetrAVG — Bei Arbeitsvertrag-Portfolio-Reviews
- DSGVO Art. 5 — Datensparsamkeit bei Verarbeitung von Vertragsdaten

## Schritt-für-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview: Fallkategorie, Tabellengroesse, Pruefzweck und Exportformat erfassen.
2. Wuerfelstruktur aufbauen: Spaltenprompts und Zeilenprompts definieren, Perspektiven festlegen.
3. Dokumentstapel einlesen und Inventar erstellen.
4. Review durchfuehren: jede Zeile in allen drei Perspektiven pruefen und Risikoampel setzen.
5. Kreuzblatt-Konsistenzpruefung und Audit-Trail abschliessen; Excel-Export oder PDF-Bericht erzeugen.

## Skill-Tour (was gibt es hier?)

- `arbeitsblatt-perspektiven-definieren` — Die drei Pruefperspektiven (Recht, Steuer, Wirtschaft) für den 3D-Wuerfel definieren.
- `audit-trail-protokoll` — Alle Review-Schritte mit Zeitstempel und Pruefer-ID protokollieren.
- `belegkette-rueckverfolgung` — Belegkette für Forderungen und Zahlungen zurueckverfolgen.
- `caching-und-teil-rerun` — Zwischenergebnisse cachen und Teilbereiche ohne Vollneustart erneut ausfuehren.
- `dokumentstapel-aufnehmen` — Dokumentenstapel (PDFs, Excel, Word) einlesen und Inventar erstellen.
- `excel-multi-sheet-export` — 3D-Review-Ergebnis als Excel-Datei mit Arbeitsblaettern je Perspektive exportieren.
- `kreuzblatt-konsistenzpruefung` — Abgleich der drei Dimensionen auf Widersprueche und fehlende Eintraege.
- `pdf-bericht-erzeugen` — 3D-Review-Ergebnis als PDF-Bericht mit Zusammenfassung, Tabellen und Risikoampeln erzeugen.
- `prompt-versionierung` — Prompt-Versionen für den 3D-Review verwalten und aendern.
- `pruefer-uebergabe-paket` — Uebergabepaket für Prueferwechsel mit aktuellem Stand und offenen Positionen.
- `review-durchfuehren` — 3D-Tabellenreview konkret durchfuehren: jede Zeile in allen drei Perspektiven pruefen.
- `risikoampel-aggregation` — Risikoampeln für alle geprueften Positionen aggregieren und Gesamtrisiko einschaetzen.
- `spaltenprompts-definieren` — Spaltenprompts für die drei Pruefperspektiven definieren.
- `tabellenreview-3d-kaltstart-interview` — Kaltstart-Interview: Fallkategorie, Tabellengroesse, Pruefzweck und Exportformat erfassen.
- `vorlage-arbeitsvertrag-portfolio` — Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format.
- `vorlage-immobilien-portfolio` — Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format.
- `vorlage-ma-due-diligence` — Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format.
- `vorlage-vendor-onboarding-3d` — Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format.
- `wuerfel-aufbauen` — 3D-Wuerfelstruktur aufbauen: Zeilen, Spalten und Perspektiven verknuepfen.
- `zeilenprompts-definieren` — Zeilenprompts für einzelne Pruefpositionen im 3D-Review definieren.

## Worauf besonders achten

- **Kreuzblatt-Konsistenz vor Export pruefen**: Widersprueche zwischen den Dimensionen koennen die Aussagekraft des Berichts untergraben.
- **Prompt-Versionierung dokumentieren**: Unterschiedliche Prompt-Versionen im selben Review produzieren nicht vergleichbare Ergebnisse.
- **Audit-Trail von Beginn an fuehren**: Nachtraegliches Erganzen des Protokolls ist fehleranfaellig und im Zweifel nicht beweissicher.
- **Caching konservativ einsetzen**: Gecachte Ergebnisse werden nicht neu berechnet; Aenderungen im Dokument werden nicht erfasst.
- **Vorlagen nicht ohne Anpassung verwenden**: Vorlage-Spaltenprompts sind Ausgangspunkte, keine abschliessenden Pruefkataloge.

## Typische Fehler

- Wuerfelstruktur ohne Kaltstart-Interview aufbauen; Pruefzweck und Exportformat werden spaeter nicht erfuellt.
- Alle drei Perspektiven mit identischen Prompts besetzen; der Wuerfel verliert seine Informationstiefe.
- Risikoampel-Schwellenwerte nicht explizit definieren; Ampelbewertungen werden inkonsistent.
- Prueferwechsel ohne Uebergabepaket; Nachfolger muss von vorne beginnen.
- Excel-Export ohne Kreuzblatt-Pruefung; Inkonsistenzen werden erst beim Mandanten entdeckt.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum

---

## Skill: `vorlage-ma-arbeitsblatt-perspektiven-audit`

_Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für M-und-A-Transaktionen. Abgrenzung: nicht allgemeines M-und-A_

# /tabellenreview-3d:vorlage-ma-due-diligence

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spalten (18 Datenpunkte)

1. **Vertragsart** — Rahmenvertrag / Einzelvertrag / NDA / Lizenz / Lieferung / Werk
2. **Laufzeit und Beginn** — Vertragsdatum + Festlaufzeit / unbefristet
3. **Kündigungsfrist** — ordentliche / außerordentliche / Sondertatbestände
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **MAC-Klausel** — Wesentlichkeitsdefinition / Rechtsfolge (BGB Paragraph 313 / 314)
6. **Abtretungsverbot** — BGB Paragraph 399 / HGB Paragraph 354a / Vertragsübernahme
7. **Haftungsbegrenzung** — pro Fall / pro Jahr / Ausschluss Vorsatz und grobe Fahrlaessigkeit
8. **Garantien** — beschaffenheitsbezogen / verschuldensunabhängig / Haftungsausschluss BGB Paragraph 444
9. **Vertragsstrafe** — Höhe / Deckelung / Verschuldensanknuepfung
10. **Service-Level** — Reaktionszeit / Verfügbarkeit / Wiederherstellungszeit
11. **Datenschutz-AVV** — DSGVO Artikel 28 / Drittlandtransfer / SCC / TIA
12. **Geheimhaltung** — Dauer / Carve-Outs / Rückgabe / Sanktionen
13. **Vergütung** — Festpreis / Stundensatz / Erfolg / Schwellen
14. **Preisanpassung** — Indexbindung / Schwellen / Kündigungsrecht der Gegenseite
15. **Schriftform** — Änderungsvorbehalt / Sprengsatz (BGB Paragraph 125 Satz 2)
16. **Gerichtsstand** — vereinbarter Gerichtsstand / Kaufmannsklausel (ZPO Paragraph 38)
17. **Schiedsklausel** — Schiedsgericht / Sitz / Sprache / Verfahrensordnung
18. **Anwendbares Recht** — Rechtswahl / kollisionsrechtliche Wirkungen

## Arbeitsblatt-Perspektiven (4)

### Recht (Anwaltsperspektive)

- Zusatzspalten: AGB-Wirksamkeit (BGB Paragraph 305 ff.) / Klauselverbote (BGB Paragraph 308 / Paragraph 309) / Verjährungsverkürzung
- Prüfer: M&A-Lead-Counsel
- Materialität rot: unwirksame Klausel mit Hauptleistungsbezug

### Steuer (Steuerberater)

- Zusatzspalten: Umsatzsteuer-Behandlung / Reverse-Charge / verdeckte Gewinnausschuettung bei Konzernverträgen (KStG)
- Prüfer: Steuerberater
- Materialität rot: USt-Risiko mehr als 100k EUR

### Wirtschaft (Buyside)

- Zusatzspalten: Vertragsvolumen pro Jahr / Top-Kunde-Konzentration / Working-Capital-Effekt / Verlängerungsoption
- Prüfer: Deal-Lead
- Materialität rot: Vertrag > 10 Prozent Umsatz UND Kündigungsrecht der Gegenseite < 12 Monate

### Datenschutz (DSGVO)

- Zusatzspalten: Datenkategorien / Rechtsgrundlage Artikel 6 / Drittlandtransfer / Auftragsverarbeitung / Joint-Controller
- Prüfer: Datenschutzbeauftragter
- Materialität rot: Auftragsverarbeitung ohne AVV oder Drittlandtransfer ohne SCC

## BGH-Leitsätze (Auswahl)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

Würfel-Schema fix und fertig in `wuerfel-schema.yaml` mit allen drei Achsen. Direkt einsatzbereit für `review-durchfuehren`.

---

## Skill: `vorlage-ma-due-diligence`

_Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für M-und-A-Transaktionen. Abgrenzung: nicht allgemeines M-und-A_

# /tabellenreview-3d:vorlage-ma-due-diligence

## Spalten (18 Datenpunkte)

1. **Vertragsart** — Rahmenvertrag / Einzelvertrag / NDA / Lizenz / Lieferung / Werk
2. **Laufzeit und Beginn** — Vertragsdatum + Festlaufzeit / unbefristet
3. **Kündigungsfrist** — ordentliche / außerordentliche / Sondertatbestände
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **MAC-Klausel** — Wesentlichkeitsdefinition / Rechtsfolge (BGB Paragraph 313 / 314)
6. **Abtretungsverbot** — BGB Paragraph 399 / HGB Paragraph 354a / Vertragsübernahme
7. **Haftungsbegrenzung** — pro Fall / pro Jahr / Ausschluss Vorsatz und grobe Fahrlaessigkeit
8. **Garantien** — beschaffenheitsbezogen / verschuldensunabhängig / Haftungsausschluss BGB Paragraph 444
9. **Vertragsstrafe** — Höhe / Deckelung / Verschuldensanknuepfung
10. **Service-Level** — Reaktionszeit / Verfügbarkeit / Wiederherstellungszeit
11. **Datenschutz-AVV** — DSGVO Artikel 28 / Drittlandtransfer / SCC / TIA
12. **Geheimhaltung** — Dauer / Carve-Outs / Rückgabe / Sanktionen
13. **Vergütung** — Festpreis / Stundensatz / Erfolg / Schwellen
14. **Preisanpassung** — Indexbindung / Schwellen / Kündigungsrecht der Gegenseite
15. **Schriftform** — Änderungsvorbehalt / Sprengsatz (BGB Paragraph 125 Satz 2)
16. **Gerichtsstand** — vereinbarter Gerichtsstand / Kaufmannsklausel (ZPO Paragraph 38)
17. **Schiedsklausel** — Schiedsgericht / Sitz / Sprache / Verfahrensordnung
18. **Anwendbares Recht** — Rechtswahl / kollisionsrechtliche Wirkungen

## Arbeitsblatt-Perspektiven (4)

### Recht (Anwaltsperspektive)

- Zusatzspalten: AGB-Wirksamkeit (BGB Paragraph 305 ff.) / Klauselverbote (BGB Paragraph 308 / Paragraph 309) / Verjährungsverkürzung
- Prüfer: M&A-Lead-Counsel
- Materialität rot: unwirksame Klausel mit Hauptleistungsbezug

### Steuer (Steuerberater)

- Zusatzspalten: Umsatzsteuer-Behandlung / Reverse-Charge / verdeckte Gewinnausschuettung bei Konzernverträgen (KStG)
- Prüfer: Steuerberater
- Materialität rot: USt-Risiko mehr als 100k EUR

### Wirtschaft (Buyside)

- Zusatzspalten: Vertragsvolumen pro Jahr / Top-Kunde-Konzentration / Working-Capital-Effekt / Verlängerungsoption
- Prüfer: Deal-Lead
- Materialität rot: Vertrag > 10 Prozent Umsatz UND Kündigungsrecht der Gegenseite < 12 Monate

### Datenschutz (DSGVO)

- Zusatzspalten: Datenkategorien / Rechtsgrundlage Artikel 6 / Drittlandtransfer / Auftragsverarbeitung / Joint-Controller
- Prüfer: Datenschutzbeauftragter
- Materialität rot: Auftragsverarbeitung ohne AVV oder Drittlandtransfer ohne SCC

## BGH-Leitsätze (Auswahl)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

Würfel-Schema fix und fertig in `wuerfel-schema.yaml` mit allen drei Achsen. Direkt einsatzbereit für `review-durchfuehren`.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

