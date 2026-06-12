# Megaprompt: energierecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 92 Skills des Plugins `energierecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Energierecht (EnWG, EEG): ordnet Rolle (Erzeuger, Netzbetreiber, BNetzA), markiert Fris…
2. **energierecht-erstpruefung-und-mandatsziel** — Energierecht: Erstprüfung, Rollenklärung und Mandatsziel im Energierecht.
3. **anschluss** — Einstieg, Schnelltriage und Fallrouting im Energierecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wuns…
4. **eeg-kwkg-erzeugung** — EEG- und KWKG-Verguetungen für Stromerzeugungsanlagen prüfen: Einspeiseverguetung, Marktpraemie, KWK-Zuschlag. Normen: §…
5. **emobility-wasserstoff** — Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: §…
6. **energievertraege** — Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 4…
7. **infrastrukturprojekte** — Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff.…
8. **netz-speicher** — Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, G…
9. **projektfinanzierung** — Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KW…
10. **transaktionen-dd** — Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, …

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Energierecht (EnWG, EEG): ordnet Rolle (Erzeuger, Netzbetreiber, BNetzA), markiert Frist (Beschwerde BNetzA-Beschluss 1 Monat § 75 EnWG), wählt Norm (EnWG, EEG, KWKG) und Zuständigkeit (BNetzA), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Energierecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anfrage-mehrparteien-konflikt-und-interessen` — Anfrage Mehrparteien Konflikt und Interessen
- `einstieg-schnelltriage-fallrouting` — Anschluss
- `bess-abfall-recycling-rueckbau` — Bess Abfall Recycling Rueckbau
- `bess-abstandsflaechen-baurecht-brandenburg` — Bess Abstandsflaechen Baurecht Brandenburg
- `bess-baurecht-brandenburg` — Bess Baurecht Brandenburg
- `bess-behoerdenstrategie` — Bess Behoerdenstrategie
- `bess-bimschg-und-4-bimschv` — Bess Bimschg und 4 Bimschv
- `bess-brandschutz-co-location-datenschutz` — Bess Brandschutz CO Location Datenschutz
- `bess-co-location-pv-wind` — Bess CO Location PV Wind
- `bess-datenschutz-video-leitwarte` — Bess Datenschutz Video Leitwarte
- `bess-dieselgenerator-notstrom` — Bess Dieselgenerator Notstrom
- `bess-epc-fca-agnes-finanzierung` — Bess EPC FCA Agnes Finanzierung
- `bess-fca-agnes-bnetza` — Bess FCA Agnes BNETZA
- `dokumente-intake` — Dokumente Intake
- `quellen-livecheck` — Quellen Livecheck

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Energierecht sind EEG, KWKG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `energierecht-erstpruefung-und-mandatsziel`

_Energierecht: Erstprüfung, Rollenklärung und Mandatsziel im Energierecht._

# Energierecht: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Energierecht Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Energierecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Pruefungen und Leistungspunktsystem.
- `§ 16 HRG` — Pruefungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Pruefungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Energierecht: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** EEG, KWKG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Energierecht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `anschluss`

_Einstieg, Schnelltriage und Fallrouting im Energierecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordn..._

# Energierecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Energierecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung.

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
| `energierecht-eeg-kwkg-erzeugung` | EEG- und KWKG-Verguetungen für Stromerzeugungsanlagen prüfen: Einspeiseverguetung, Marktpraemie, KWK-Zuschlag. Normen: §§ 19 ff. EEG, §§ 6 ff. KWKG. Prüfraster: Anlagenanschluss, Verguetungsmodalitaeten,… |
| `energierecht-emobility-wasserstoff` | Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: § 14a EnWG, EEG, GEG, EU-Verordnung Alternative Kraftstoffe. Prüfraster: Netzintegration,… |
| `energierecht-energievertraege` | Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Prüfraster: Preisanpassungsklauseln, Laufzeiten,… |
| `energierecht-industriekunden` | Sonderregelungen für Industriekunden im Energierecht: Netzentgeltbefreiungen, Direktleitungen, Eigenerzeugung. Normen: § 19 StromNEV, §§ 17 ff. EnWG, EEG. Prüfraster: atypische Netznutzung, Eigenversorgungsprivileg,… |
| `energierecht-infrastrukturprojekte` | Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff. EnWG, NABEG, BImSchG, BauGB. Prüfraster: Genehmigungsverfahren, Einwendungen,… |
| `energierecht-kommandocenter` | Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output:… |
| `energierecht-netz-speicher-zugang` | Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher prüfen. Normen: §§ 17 ff. 20 ff. EnWG, NAV. Prüfraster: Netzanschlussrecht, Anschlussbegehren, Kapazitaetsprüfung, Diskriminierungsfreiheit. Output:… |
| `energierecht-projektfinanzierung` | Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KWKG, BGB. Prüfraster: Finanzierungsstruktur, Sicherheitenpakete, Cashflow-Analyse, Foerderdarlehen.… |
| `energierecht-transaktionen-dd` | Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Prüfraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken.… |
| `energierecht-verfahren` | Regulierungsverfahren und Gerichtsverfahren im Energierecht durchführen: BNetzA-Verfahren, Kartellamt. Normen: §§ 75 ff. EnWG, GWB, VwGO. Prüfraster: Verfahrenstyp, Beschwerde, Klage, Fristenmanagement. Output:… |
| `energierecht-vertrieb-marktrollen` | Energievertrieb und Marktrollen im liberalisierten Energiemarkt: Lieferant, Netzbetreiber, Bilanzkreis. Normen: §§ 4 ff. EnWG, MaBiS-Prozesse. Prüfraster: Marktrollen, Bilanzkreisvertrag, Lieferantenwechsel. Output:… |
| `energierecht-waerme-quartier` | Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende. Normen: AVBFernwaermeV, GEG, EnWG, EEG. Prüfraster: Konzessionspflicht, Preisanpassungsklauseln,… |
| `energierecht-wettbewerb` | Wettbewerbs- und Kartellrecht im Energiesektor prüfen: Marktmacht, Diskriminierung, Missbrauch. Normen: §§ 18 ff. GWB, Art. 101 102 AEUV, EnWG. Prüfraster: Marktabgrenzung, Marktmacht, Diskriminierungsverbot,… |

## Worum geht es?

Dieses Plugin deckt das gesamte Energierecht ab — von der Erzeugung ueber Netze bis zum Vertrieb. Adressaten sind Rechtsanwaelte, Unternehmensjuristen und Compliance-Beauftragte bei Stadtwerken, Energieversorgern, Netzbetreibern, Industriekunden und Projektierungsgesellschaften. Das Plugin unterstuetzt bei Einzelpruefungen ebenso wie bei der Begleitung von Transaktionen und Regulierungsverfahren.

Schwerpunkte sind das Energiewirtschaftsgesetz (EnWG), das EEG, das KWKG, kartellrechtliche Sektorfragen (GWB), das Recht der Waermenetze und Quartiersbloecke, die Projektfinanzierung von Erneuerbaren-Anlagen sowie Due Diligence bei M&A-Transaktionen im Energiesektor.

## Wann brauchen Sie diese Skill?

- Ein Windparkbetreiber prueft Ansprueche auf EEG-Einspeiseverguetung oder Marktpraemie nach neuer Anlageninbetriebnahme.
- Ein Stadtwerk will ein Waermenetz nach GEG-Vorgaben strukturieren und benoetigt den Rechtsrahmen.
- Ein Industrie-Gross-Kunde fragt nach Netzentgeltbefreiungen und Direktleitungsoptionen.
- Eine Investmentgesellschaft kauft einen Solarpark und benoetigt energierechtliche Due Diligence.
- Ein Versorger fuehrt ein BNetzA-Regulierungsverfahren durch oder klaegt gegen einen Netzentgeltbescheid.

## Fachbegriffe (kurz erklaert)

- **EEG** — Erneuerbare-Energien-Gesetz; regelt Einspeiseverguetung und Marktpraemie für Strom aus erneuerbaren Quellen.
- **KWKG** — Kraft-Waerme-Kopplungsgesetz; regelt KWK-Zuschlaege für effiziente Kraftwaermekopplungsanlagen.
- **EnWG** — Energiewirtschaftsgesetz; Rahmengesetz für Strom- und Gasnetzregulierung, Lieferpflichten und Marktregeln.
- **BNetzA** — Bundesnetzagentur; Regulierungsbehoerde für Netze (Strom, Gas, Telekommunikation).
- **Marktpraemie** — Foerderinstrument nach EEG: Differenz zwischen Marktpreis und anzulegendem Wert wird vom Netzbetreiber erstattet.
- **NAV** — Niederspannungsanschlussverordnung; regelt Anschlusspflichten und Bedingungen für Stromkunden.
- **GEG** — Gebaeude-Energie-Gesetz; verpflichtet Kommunen zur Waermeplanung und regelt Anforderungen an neue Heizungsanlagen.
- **Planfeststellung** — Behoerdliches Genehmigungsverfahren für groessere Leitungsinfrastrukturen nach §§ 43 ff. EnWG.

## Rechtsgrundlagen

- §§ 1 ff. EnWG (Zweck, Netzregulierung, Netzzugang)
- §§ 17 ff. EnWG (Netzanschluss), §§ 20 ff. EnWG (Netzzugang)
- §§ 43 ff. EnWG (Planfeststellung Leitungsinfrastruktur)
- §§ 75 ff. EnWG (Verfahren vor der BNetzA)
- §§ 19 ff. EEG (Einspeiseverguetung, Marktpraemie)
- §§ 6 ff. KWKG (KWK-Zuschlaege)
- §§ 18 ff. GWB (Marktmachtmissbrauch im Energiesektor)
- GEG — Gebaeude-Energie-Gesetz (Waermeplanung, Heizungspflichten)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Erzeuger, Netzbetreiber, Versorger, Industrie oder Investor?
2. Rechtsgebiet eingrenzen: EEG/KWKG-Förderung, Netz, Vertrieb, Waerme, Transaktion oder Verfahren?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Widerspruchs- und Klagfristen bei BNetzA-Bescheiden sind kurz.
5. Anschluss-Skill bestimmen: Genehmigung, Finanzierungsstruktur oder kartellrechtliches Gutachten?

## Skill-Tour (was gibt es hier?)

- `energierecht-kommandocenter` — Navigationszentrum: Weiterleitung je Rechtsthema und Anfrageart; Schnellstart für alle Energierecht-Mandate.
- `energierecht-eeg-kwkg-erzeugung` — EEG-Einspeiseverguetung und Marktpraemie sowie KWK-Zuschlaege für Stromerzeugungsanlagen pruefen.
- `energierecht-netz-speicher-zugang` — Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher nach EnWG pruefen.
- `energierecht-energievertraege` — Strom- und Gasliefervertraege mit Industrie- und Privatkunden pruefen und entwerfen.
- `energierecht-industriekunden` — Sonderregelungen für Industriekunden: Netzentgeltbefreiungen, Direktleitungen, Eigenerzeugung.
- `energierecht-infrastrukturprojekte` — Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung.
- `energierecht-vertrieb-marktrollen` — Energievertrieb und Marktrollen im liberalisierten Energiemarkt: Lieferant, Netzbetreiber, Bilanzkreis.
- `energierecht-waerme-quartier` — Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende.
- `energierecht-emobility-wasserstoff` — Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff pruefen.
- `energierecht-wettbewerb` — Wettbewerbs- und Kartellrecht im Energiesektor pruefen: Marktmacht, Diskriminierung, Missbrauch.
- `energierecht-verfahren` — Regulierungsverfahren und Gerichtsverfahren im Energierecht durchfuehren (BNetzA, Kartellamt).
- `energierecht-transaktionen-dd` — Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen.
- `energierecht-projektfinanzierung` — Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen.

## Worauf besonders achten

- EEG-Förderung ist anlagenspezifisch und zeitraumgebunden: Inbetriebnahmedatum und Ausschreibungsergebnis bestimmen den Foerdermechanismus.
- Netzanschluss-Fristen nach NAV und EnWG koennen mit Vertragsrechten kollidieren — Lieferantenwechsel und Anschlussprozesse haben eigene Taktfristen.
- Kartellrecht im Energiesektor: Marktmachtmissbrauch nach §§ 18 ff. GWB und EnWG-Diskriminierungsverbot sind parallel anwendbar.
- GEG-Pflichten zur kommunalen Waermeplanung gelten ab 2024/2026 gestaffelt — Uebergangszeitraeume beachten.
- Bei Energietransaktionen: EEG-Foerderansprueche gehen nicht automatisch auf Erwerber ueber, wenn Anlagenstruktur veraendert wird.

## Typische Fehler

- EEG-Degression und Ausschreibungspflicht-Schwellen nicht aktuell geprueft: Foerderantraege werden zu spaet gestellt oder falsch berechnet.
- Netzentgeltbefreiungen für Industriekunden als selbstverstaendlich angenommen: Voraussetzungen (Benutzungsstunden, Bandlastprofil) werden nicht konkret geprueft.
- Planfeststellungsverfahren ohne fruehzeitige Einbindung der Raumordnung gestartet: Verzoegerungen durch spaete Beteiligung der Länder.
- Wasserrechte und Naturschutzrecht bei Windparks oder Wasserkraftprojekten uebersehen.
- Waermeversorgungsvertraege ohne Preisanpassungsklausel nach § 24 AVBFernwaermeV abgeschlossen.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- EEG 2023 in der zum Stand-Datum geltenden Fassung
- GEG in der Fassung des Waermepumpen-Aenderungsgesetzes 2024

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 33 EEG
- § 75 EnWG
- § 31 EnWG
- § 80 VwG
- § 17 EnWG
- § 8 EEG
- § 41 EnWG
- § 13a EnWG
- § 46 EnWG
- § 13 EnWG
- § 123 VwG
- § 21 EEG

### Leitentscheidungen

- EuGH C-359/11
- BGH VIII ZR 158/11
- BGH VIII ZR 178/08
- BGH VIII ZR 295/09
- EuGH C-718/18

---

## Skill: `eeg-kwkg-erzeugung`

_EEG- und KWKG-Verguetungen für Stromerzeugungsanlagen prüfen: Einspeiseverguetung, Marktpraemie, KWK-Zuschlag. Normen: §§ 19 ff. EEG, §§ 6 ff. KWKG. Prüfraster: Anlagenanschluss, Verguetungsmodalitaeten, Direktvermarktung, Ausschreibungspflicht. Output: Verguetungsberechnung EEG und KWKG. Abgrenz..._

# EEG, KWKG und Erzeugung erneuerbarer Energien

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Anlagen-Typ (Wind, Photovoltaik, KWK, Biomasse, Wasserkraft, Geothermie)
- Installierte Leistung kW / MW
- Inbetriebnahme-Datum oder geplantes Datum
- Ausschreibungs-Teilnahme (Zuschlag, Höchst-Wert)
- Marktstammdatenregister-Eintrag (MaStR-Nummer)
- Förder-Bezug (EEG-Vergütung, KWKG-Zuschlag, BImSchG-Genehmigung, Investitions-Förderung)
- Netzbetreiber und Bilanzkreis

## Schritt 1 — Förder-Architektur EEG 2023

### Marktprämie + Direktvermarktung § 19, § 20 EEG

Standard-Fall: Anlagen ab 100 kW (Solar 100 kWp ab 2025, schrittweise reduziert). Vermarktung über Direktvermarkter; EEG zahlt Marktprämie als Differenz zwischen anzulegendem Wert und Marktpreis.

### Feste Einspeise-Vergütung § 21 EEG

Kleinanlagen unter 100 kW (Solar). Vergütung direkt vom Netzbetreiber.

### Anzulegender Wert

Aus Ausschreibung (Wind, Solar > 1 MW) oder gesetzlich festgelegt (Kleinanlagen, Biomasse Bestand). Inflations-Anpassung nach § 51a EEG (seit 2024 stärker eingeführt).

### Ausschreibungs-Verfahren

- **Wind onshore**: jährlich vier Termine, anzulegender Wert je MWh, Höchstwert 7,35 ct/kWh (Stand 2024, jährliche Anpassung BNetzA)
- **PV-Freifläche > 1 MW**: vier Termine pro Jahr
- **PV-Dach > 1 MW**: separate Ausschreibung
- **Biomasse**: zweimal pro Jahr
- **Wind offshore**: Bundesfachplan-Ausschreibung BSH

### Innovationsausschreibung § 39o EEG

Speicher-Kombinationen, KWK-Hybride, besondere Anlagenkonzepte. Zuschlag in MWh-Vergütung statt Cent/kWh.

## Schritt 2 — KWKG 2023

### Zuschlag-Berechtigte Anlagen § 5 KWKG

- Neuanlagen, modernisierte Anlagen, Bestandsanlagen
- Brennstoffe: Erdgas, biogene Brennstoffe, Wasserstoff (ab 2025 mit gestaffelter Quote)
- Leistungs-Klassen: < 50 kW, 50 — 100 kW, 100 — 250 kW, 250 — 2 MW, > 2 MW

### Zuschlags-Höhen

Gestaffelt nach Leistung und Inbetriebnahme. Zuschlags-Dauer typisch 30.000 — 45.000 Vollbenutzungs-Stunden.

### Wasserstoff-Quote

Seit 2024 Pflicht zu schrittweisem H2-Ready-Standard für Anlagen > 10 MW (KWKG-Reform 2023).

### Förderfähigkeits-Antrag § 10 KWKG

- BAFA als zuständige Behörde (für Standard-Anlagen)
- BNetzA für Ausschreibungs-KWK
- Frist-genau prüfen

## Schritt 3 — Anlagen-Zulassung und Genehmigung

### Marktstammdatenregister § 33 EEG

- **Eintragungs-Pflicht** binnen ein Monat nach Inbetriebnahme
- BNetzA-Webportal
- Bei Versäumnis: **anzulegender Wert auf null** § 33 Abs. 6 EEG bis zur Eintragung
- Strenge Verwaltungspraxis BNetzA

### BImSchG-Genehmigung

- Windkraftanlagen > 50 m Gesamthöhe: § 4 BImSchG förmliches Verfahren
- Biogas-Anlage > 1,2 MW: Standard-Verfahren
- Sammlung Antrags-Unterlagen: Schallgutachten, Schattenwurfprognose, artenschutzrechtliche Prüfung (saP), Bauantrag

### Solar-Freiflächen / Wind: Bauleitplanung-Bezug

- Wind: ab 1.000 m zu nächster Wohnbebauung (Bundesland-Regelung Bayern 10H abgeschafft 2023)
- Solar: Acker- und Grünland-Standorte mit eingeschränkten Möglichkeiten
- Beschleunigungs-Gebiete EU-RED III: Pflicht ab 21.02.2026 zu deren Ausweisung

### WindBG / SolarBG

- Windflächenbedarfsgesetz 2022: Länder-Quote Mindestflächen
- Solarpaket I 2024: vereinfachte Anlagenzulassung Mieterstrom, Direktversorgung

## Schritt 4 — Repowering und Modernisierung

### Repowering Wind § 23b EEG

- Ersatz Bestandsanlage durch leistungsstärkere Neuanlage am gleichen Standort
- Anrechnungs-Mechanismus
- Bevorzugte Behandlung in Ausschreibungen

### Modernisierung KWK § 5 Abs. 2 KWKG

- Mindest-Wert-Erhaltung von Bestandsanlagen
- Neuer Zuschlag bei wesentlicher Modernisierung

### Speicher-Hybridisierung

- Innovationsausschreibung
- Doppelvermarktungs-Verbot beachten

## Schritt 5 — Streit-Konstellationen

### Vergütungs-Streit mit Netzbetreiber

- Anlagenzulassung erfolgt aber Vergütung verweigert
- BGH-EnVR-Senat: laufende Rechtsprechung zum Anlagenbegriff und zur Verguetung — vor Ausgabe Aktenzeichen ueber bundesgerichtshof.de verifizieren
- Klärung Streit ueber Schiedsverfahren bei der BNetzA (§ 81 EEG) oder Klage Zivilgericht

### Bei nicht-rechtzeitiger MaStR-Eintragung

- Anlage in Betrieb, Eintrag fehlt
- Korrektur möglich, aber Vergütungs-Sperre für Zwischen-Zeitraum
- BNetzA-Verwaltungspraxis prüfen

### Ausschreibungs-Zuschlag versäumt

- Anlage gebaut, Zuschlag verfehlt
- Alternative: feste Einspeise-Vergütung bei Kleinanlagen / Sonder-Konstellationen
- Wenn kein Förderanspruch: Marktvermarktung über Direktvermarkter, PPA

### Bei Bürgerwindprojekten

- Bürgerenergiegesellschaft § 3 Nr. 15 EEG
- Privilegierungen in Ausschreibung
- Mitglieder-Anteils-Mindestanforderungen

## Schritt 6 — PPA als Alternative zur EEG-Förderung

### Corporate PPA

- Direkter Vertrag Anlage — Endkunde (Industrie)
- Vermeidet Marktrisiko
- Skill `energierecht-projektfinanzierung` für Strukturierung

### On-Site PPA

- Anlage auf Kundengelände
- Direktversorgung ohne Netzdurchleitung
- Mess- und Eichrecht beachten

## Schritt 7 — Strafzahlung BNetzA / Pönale

### Pönalen bei Nicht-Realisierung Ausschreibungs-Zuschlag

- Zuschlag erteilt aber nicht rechtzeitig umgesetzt
- Pönale je nach Volumen
- Wiederaufnahme-Sperre

### Nachträglicher Ausschluss

- Bei wesentlichen Verstößen Förderfähigkeit
- BNetzA-Anordnung, klagebar VG

## Schritt 8 — Erdgas / Biogas / Biomethan

- Biomasse-Spezial-Regelungen § 39f-h EEG
- Nachhaltigkeits-Anforderungen RED II/III
- Biomethan-Einspeisung Gasnetz
- HRG-Verfahren Wasserstoff-Hochlauf (Erdgas-Vorgriff)

## Schritt 9 — EU-Bezug

### RED III (Renewable Energy Directive III, 2024)

- Beschleunigungs-Gebiete Pflicht
- Vereinfachung Genehmigung
- Nationale Umsetzung läuft

### EU-Strommarkt-Reform 2024

- Differenzverträge (Contracts for Difference)
- PPA-Erleichterungen
- Capacity-Markt-Mechanismen

## Schritt 10 — Mandanten-Strategie

### Bei Erzeugungs-Investor (Neuanlage)

1. Anlagentyp und Standort prüfen
2. Genehmigungs-Weg klar (BImSchG / Bau)
3. Förderpfad (Ausschreibung vs. PPA vs. Eigenverbrauch)
4. MaStR-Eintragung sicherstellen
5. Vergütungs-Direktvermarkter wählen
6. Begleit-Verträge (PPA, Wartungs-Vertrag, Versicherungs-Schutz)

### Bei Bestandsanlage

1. Vergütungs-Anspruch prüfen
2. Modernisierungs-Optionen
3. Repowering-Strategie
4. Vermarktungs-Optimierung

### Bei Streit mit Netzbetreiber

1. BNetzA-Beschwerde erwägen
2. Klage VG / Bundesgerichtshof bei EnWG-Linien
3. Skill `energierecht-verfahren`

## Aktuelle Rechtsprechung & Leitsätze (Stand 05/2026)

- **EuGH 28.03.2019, C-405/16 P (PreussenElektra-Nachfolge / EEG 2012)**: EEG-Umlage stellt keine staatliche Beihilfe i.S.v. Art. 107 AEUV dar (in Vorlaeufer-Konstellation); Aenderung gegenueber Kommissions-Auffassung. Quelle: curia.europa.eu (CELEX 62016CJ0405).
- **BGH 05.07.2022, EnVR 41/20**: Anlagenbegriff EEG; Abgrenzung zwischen mehreren Anlagen am selben Standort. Quelle: bundesgerichtshof.de — Pressemitteilung BGH 99/2022. Vor Zitieren der Detailfragen Aktenzeichen ueber bundesgerichtshof.de verifizieren.
- **BVerwG 17.12.2020, 4 C 5.19**: BImSchG-Genehmigung Windkraftanlage; Anforderungen an artenschutzrechtliche Pruefung (saP). Quelle: bverwg.de.
- **EuGH 27.04.2023, C-217/22 (Aktiengesellschaft Yarpa)**: Auslegung der EE-Richtlinie 2018/2001 (RED II) — Foerderfaehigkeit. Quelle: curia.europa.eu.
- **Gesetzeslage 05/2026:**
 - EEG 2023 (BGBl. I 2022 S. 1237, mehrfach geaendert)
 - Solarpaket I — BGBl. I 2024 S. 151 (Inkraftsetzung 16.05.2024)
 - WindBG 2022 (BGBl. I S. 1353) — 2-Prozent-Flaechenziel Länder
 - KWKG 2023 — Verlaengerung Förderung bis 2030 (Wasserstoff-Pflicht ab 10 MW)
 - GEG 2024 (BGBl. I 2023 S. 280) — Heizungsgesetz, 65-Prozent-EE-Pflicht ab 2024 in Neubaugebieten
 - RED III — RL (EU) 2023/2413; Frist Umsetzung 21.05.2025; Beschleunigungsgebiete ab 21.02.2026 verpflichtend
 - BNetzA-Festlegungen Ausschreibungs-Hoechstwerte 2025/2026 ueber bundesnetzagentur.de aktuell pruefen

Konkrete Aktenzeichen vor Ausgabe ueber bundesgerichtshof.de / bverwg.de / curia.europa.eu mit Datum verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 19 EEG (Marktpraemie) — § 20 EEG (Direktvermarktung) — § 21 EEG (feste Einspeise-Verguetung) — § 23b EEG (Repowering) — § 33 EEG (MaStR-Eintragungspflicht) — § 4 BImSchG (Genehmigungspflicht) — § 35 BauGB (Privilegierung Aussenbereich) — § 44 BNatSchG (Zugriffsverbote Artenschutz)

## Verzahnung

- `energierecht-netz-speicher-zugang` — Netzanschluss
- `energierecht-vertrieb-marktrollen` — Direktvermarktung
- `energierecht-projektfinanzierung` — PPA
- `energierecht-transaktionen-dd` — bei Anlagen-Verkauf
- `umweltrecht-immissionsschutz-bimschg` — BImSchG-Genehmigung
- `klimaklagen-verbandsklage-umwrg` — bei Verbands-Klagen Wind
- `normenkontrolle-bauleitplanung` — bei Bauleit-Streit

## Quellen

- EEG 2023 + Solarpaket I 2024 §§ 19, 20, 21, 23b, 33, 39f-o, 51a
- KWKG 2023 §§ 5, 10, 25
- BImSchG §§ 4, 10
- BauGB §§ 35, 249
- WindBG, SolarBG, GEG, EnEfG
- BNetzA-Festlegungen zu Ausschreibungs-Höchstwerten
- BAFA-Merkblätter
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BVerwG 17.12.2020, 4 C 5.19 — BImSchG-Windkraft saP (bverwg.de)
- EU-RED III (Richtlinie (EU) 2023/2413, ABl. L 2413 vom 31.10.2023; eur-lex.europa.eu/eli/dir/2023/2413/oj)
- EU-Strommarkt-Verordnung (EU) 2024/1747; sowie VO (EU) 2019/943 (Grundverordnung)
- EuGH 02.09.2021, C-718/18 — Unabhaengigkeit BNetzA als Regulierungsbehoerde

---

## Skill: `emobility-wasserstoff`

_Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: § 14a EnWG, EEG, GEG, EU-Verordnung Alternative Kraftstoffe. Prüfraster: Netzintegration, Foerderrecht, Liefervertrag, Regulierungsrahmen. Output: Regulierungsrahmen E-Mobilitaet..._

# E-Mobilität und Wasserstoff

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Mandant (Ladeinfrastruktur-Betreiber, H2-Projektgesellschaft, Industrie, Versorger)
- Projekt-Phase (Konzept, Genehmigung, Aufbau, Betrieb)
- Standort und Anschluss-Werte
- Förderprogramme angefragt / beantragt
- Verzahnung mit Strombezug und Erzeugung

## Schritt 1 — Ladeinfrastruktur Recht-Rahmen

### LSV (Ladesäulenverordnung) 2023

- Mindest-Standards Ladesäulen öffentlich
- Roaming-Pflicht: jeder Ladepunkt mit Drittanbietern abrechnungsfähig
- Mess- und Eichrecht: Pflicht zur geeichten Messung pro Ladevorgang
- Authentifizierungs-Optionen (App, RFID, Kreditkarte ab 2024)

### AFIR (Alternative Fuels Infrastructure Regulation, VO 2023/1804)

- EU-Verordnung seit 13.04.2024 in Kraft
- Mindest-Dichte Ladepunkte je Streckenkilometer (TEN-T-Korridore)
- Schnelllade-Park-Standards
- Bedienungs-Vereinheitlichung

### Mess- und Eichrecht

- Mess- und Eichgesetz (MessEG)
- Geeichte Messung Kilowattstunden pro Ladevorgang
- Sonderregelungen Eich-Übergang
- BMR (Bundesamt für Messwesen) Aufsicht

## Schritt 2 — Ladeinfrastruktur-Förderung

### Förderprogramme

- **KfW-Förderung Wallbox privat** historisch (ausgelaufen 2024)
- **BMVI / BMDV-Förderung** öffentliche Ladesäulen Schnelllader
- **Bundesförderung Ladeinfrastruktur II** (LIS II)
- **Länderprogramme** (Bayern, NRW, BW spezifisch)

### Antragsverfahren

- Vor Vorhabensbeginn
- Antragsformulare BAFA / BAV
- Beleg-Pflichten

### Compliance

- Mindest-Betriebs-Dauer (typisch 5 Jahre)
- Roaming-Pflicht (AFIR)
- Daten-Übermittlung Ladevorgänge

## Schritt 3 — Standortwahl Ladeinfrastruktur

### Genehmigungs-Bedarf

- Bauantrag bei größeren Anlagen
- Stellplatz-Anrechnung Bauordnungsrecht
- Verkehrsrechtliche Anordnungen

### Netzanschluss

- Anschluss-Werte oft hoch (Schnelllader 150-350 kW)
- Stationäre Speicher als Last-Glättung
- Netzentgelt-Optimierung

### Eigentums-/Pacht-Verhältnisse

- Standorte häufig auf Pachtbasis
- Tankstellen-Konstellationen mit klassischem Mineralöl-Anbieter
- Parkhaus-/Supermarkt-Standorte

## Schritt 4 — THG-Quote § 37a BImSchG

### Konzept

- Treibhausgas-Minderungs-Quote für Kraftstoff-Lieferanten
- Ladestrom (E-Auto) wird angerechnet
- Vermarktung der Quote über THG-Quoten-Pool-Anbieter

### Anwendung

- Anlagen-Betreiber öffentlicher Ladepunkte
- Privater Wallbox-Betreiber (über Pool-Anbieter)
- Erstattungs-Beträge variabel je Marktlage

### Verwaltungsverfahren

- UBA als Behörde
- Antragsfristen jährlich
- Skill `umweltrecht-emissionshandel-tehg` bei größeren Strukturen

## Schritt 5 — Wasserstoff-Wirtschaft

### Hierarchie der Wasserstoff-Erzeugungs-Pfade

- **Grüner H2**: Elektrolyse mit erneuerbarem Strom → RED III-konform
- **Türkiser H2**: Methan-Pyrolyse mit Kohlenstoff-Sequestrierung
- **Blauer H2**: Erdgas-Reformierung mit CCS (Carbon Capture and Storage)
- **Grauer H2**: Konventionelle Methan-Reformierung (nicht förderfähig)

### RED III Erneuerbarkeits-Kriterien

- Direkte Verbindung zwischen Elektrolyseur und EE-Anlage
- Oder: Stundengleichheit (ab 2030 strenger)
- Oder: Bilanzkreis-Methode mit zusätzlichkeit
- Delegierter Akt EU 2023/1184 als Konkretisierung

### Förderung Elektrolyseure

- **KfW BEW** im Wärme-Bezug
- **EEG-Innovationsausschreibung** für Hybrid-Anlagen
- **Klimaschutzverträge (CCfD)** Differenzvertrag für Wasserstoff-Produzenten
- **Wasserstoff-Beschleunigungs-Gesetz** geplant

### Antragsverfahren

- BAFA als Hauptbehörde
- Förder-Dokumentation umfangreich
- Audit-Pflichten

## Schritt 6 — H2-Netz und H2-Stammnetz

### Wasserstoff-Stammnetz § 28r EnWG

- Bundesweites H2-Stammnetz
- Kombination Neu-Bau und Erdgas-Netz-Umstellung
- Genehmigung Bundesfachplanung

### Hochlauf-Phase (Wasserstoff-Hochlaufgesetz)

- Übergangsweise Erdgas-Anteil im H2-Netz möglich
- Förderung Aufbau-Phase

### Bundesnetzentwicklungsplan H2 (BNEP)

- 4-Jahres-Zyklus
- Bedarfs-Identifikation
- BNetzA-Festlegung

## Schritt 7 — H2-Anlagen-Genehmigung

### BImSchG-Genehmigung

- Elektrolyseure > 10 MW: § 4 BImSchG förmliches Verfahren
- Druckwasserstoff-Speicher
- Sicherheits-Anforderungen ATEX-Richtlinie

### Bauleitplanung-Bezug

- Wasserstoff-Tankstellen-Standorte
- Industrielle H2-Anlagen
- Konflikte mit Wohnbebauung

### Strom-Bezug

- Direktversorgung aus EE-Anlage bevorzugt
- PPA-Struktur
- Bilanzkreis-Strukturen

## Schritt 8 — Förderung-Konkurrenz

### Klimaschutzverträge (Carbon Contracts for Difference)

- Differenzvertrag zwischen Bund und Industrie
- Anreiz für Dekarbonisierung
- Auch für H2-Produzenten / -Verbraucher

### Industrie-Strompreis-Diskussion

- Politisch fortlaufend
- Skill `energierecht-industriekunden`

### Wasserstoff-Importe

- H2-Strategie Bundesregierung sieht erhebliche Importe
- Internationale Lieferverträge
- Anrechnungs-Mechanismus RED III

## Schritt 9 — BEHG (Brennstoffemissionshandel)

### Anwendungs-Bereich

- Verkehr und Wärme (außer ETS-pflichtig)
- CO2-Preis ansteigend (2024: 45 €/t)
- Quote für Brennstoffe-Lieferant

### Folge für E-Mobilität

- Indirekter Preis-Druck auf Verbrennungs-Pkw
- E-Auto wirtschaftlich attraktiver

### Folge für Wasserstoff

- Grauer / blauer H2 indirekt CO2-belastet
- Grüner H2 begünstigt

## Schritt 10 — Mandanten-Strategie

### Ladeinfrastruktur-Betreiber

1. Standortwahl strategisch
2. AFIR-Compliance sicherstellen
3. Mess- und Eichrecht
4. Förder-Programm beantragen
5. THG-Quoten-Optimierung

### H2-Projektgesellschaft

1. RED III-Konformität für grünen H2
2. Strom-Bezug PPA / EE-Anlage direkt
3. BImSchG-Genehmigung vorbereiten
4. KfW BEW / CCfD beantragen
5. Industrie-Abnehmer-Vertrag absichern

### Industrie-Mandant

1. H2-Versorgungs-Vertrag mit Lieferant
2. CCfD-Beteiligung
3. CBAM-Aspekte
4. Skill `energierecht-industriekunden`

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 37a BImSchG (THG-Quote) — §§ 7 ff. LSV (Ladesaeulenverordnung) — Art. 3 AFIR 2023/1804 (Mindestanforderungen Ladeinfrastruktur) — §§ 2, 6 MessEG (Eichrecht) — §§ 1, 5 EEG (Erneuerbarkeits-Kriterien RED III) — § 28 EnWG (Wasserstoff-Netz)

## Verzahnung

- `energierecht-eeg-kwkg-erzeugung` (Elektrolyseure-Strom)
- `energierecht-netz-speicher-zugang` (Anschluss Ladeinfrastruktur)
- `energierecht-projektfinanzierung` (KfW BEW / CCfD)
- `energierecht-industriekunden` (H2-Abnehmer)
- `umweltrecht-immissionsschutz-bimschg` (BImSchG-Verfahren)
- `umweltrecht-emissionshandel-tehg` (ETS / BEHG)

## Quellen

- EnWG §§ 17, 28r ff. (H2-Netz), 42a
- LSV (Ladesäulenverordnung 2023)
- AFIR VO (EU) 2023/1804
- MessEG / MessEV
- BImSchG §§ 4, 37a
- BEHG
- RED III Richtlinie 2023/2413/EU + delegierter Akt 2023/1184
- BAFA / KfW Förderrichtlinien
- Klimaschutzvertrags-Programm BMWK
- H2-Stammnetz-Beschluss BNetzA
- UBA THG-Quoten-Verwaltung
- BVerwG-/EuGH-Linien zu E-Mobilität (begrenzt)

---

## Skill: `energievertraege`

_Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Prüfraster: Preisanpassungsklauseln, Laufzeiten, Sonderkündigungsrecht, Lieferbedingungen. Output: Vertragsprüfergebnis oder Vertragsentwurf. Abgre..._

# Energie-Verträge — Strukturierung und Prüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vertrags-Typ (Strom / Gas / Wärme / Konzession / Bilanzkreis / PPA)
- Mandant-Rolle (Anbieter / Käufer / Netzbetreiber / Kommune)
- Vertrags-Phase (Verhandlung / Bestand / Streit / Migration)
- Konkrete Streit-Punkte
- AGB-Standard oder Verhandlungs-Vertrag

## Schritt 1 — Stromlieferungs-Vertrag Strukturen

### Standard-Haushaltskunden

- Grundversorgungs-Vertrag (StromGVV)
- Sondervertrag mit Wahl-Lieferant
- Tarif-Übersicht und AGB

### Gewerbe-/Industrie-Kunden

- Sondervertrag mit Anlagen-bezogenen Konditionen
- Tarif-Strukturen (Festpreis, Index, Hybrid)
- Bandlast vs. Last-Profil-Kunde

### Kern-Vertrags-Klauseln

```
1. Vertrags-Parteien und Anlagen-Bezug
2. Vertrags-Beginn und Dauer
3. Liefer-Mengen / Anschluss-Werte
4. Preisformel
5. Anpassungs-Klauseln
6. Bilanzkreis-Zuordnung
7. Force-Majeure / Höhere Gewalt
8. Mängelhaftung
9. Kündigungs-Modalitäten
10. Sicherheiten und Zahlungsbedingungen
11. Vertraulichkeit
12. Gerichtsstand / Schiedsklausel
```

### AGB-Kontrolle

- §§ 305 ff. BGB
- Bei Haushaltskunden besonders streng
- Bei Industrie-Sondervertrag Verhandlungs-Vertrag möglich
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 2 — Preisanpassungs-Klauseln

### Standard-Anforderungen

- **Transparenz** — Anpassungs-Faktor verständlich
- **Bezugnahme auf nachvollziehbare Indizes** (EEX-Preis, Basispreis-Plus, Inflation)
- **Cost-Reflektion** — Anpassung muss tatsächlich Kostenelement abbilden
- **Sonderkündigungs-Recht** bei Anpassung

### Wirksamkeits-Kriterien BGH

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Häufige Klausel-Fehler

- **Spotpreis-Indizierung** ohne Bezug zum Lieferanten-Bedarf
- **Einseitige Anpassungs-Recht** ohne Begründungs-Pflicht
- **Fehlende Cap-Mechanismen** bei extremen Markt-Schwankungen
- **Intransparente Bezugnahmen**

### Folge Unwirksamkeit

- Ausgangs-Preis bleibt
- Rückforderungs-Anspruch Kunden (Verjährung 3 Jahre)
- Schaden für Versorger erheblich

## Schritt 3 — Bilanzkreis-Vertrag

### Vertrags-Parteien

- Übertragungs-Netzbetreiber als Bilanzkreis-Manager
- Bilanzkreis-Verantwortlicher (BKV)

### Inhalte

- Bilanzkreis-Definition (Abgrenzung)
- Ausgleichsenergie-Mechanismus
- Sicherheits-Hinterlegung (oft 6-stelliger Euro-Betrag)
- Sanktion bei nicht-eingelieferten Daten
- Sicherheiten

### Bei Insolvenz BKV

- Bilanzkreis-Auflösung
- Übergang an Standard-BKV
- Kunden bleiben versorgt

## Schritt 4 — Konzessions-Vertrag § 46 EnWG

### Konzept

- Kommune vergibt Wege-Recht (Strom-/Gas-Verteilnetz)
- Konzessionsabgabe ab Endverbraucher
- Vertragsdauer max. 20 Jahre

### Vergabe-Verfahren

- Konzessions-Wettbewerb
- Diskriminierungs-Verbot
- Auswahl-Kriterien BNetzA-Festlegung

### Streit-Konstellationen

- Konkurrenten-Klage gegen Vergabe
- Konzessions-Abgabe-Streit
- Übernahme-Recht der Kommune (Re-Kommunalisierung)

### BGH-Linie

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BGH EnVR-Linie zu Übernahme-Bedingungen

## Schritt 5 — Industrie-Sondervertrag

### Verhandlungs-Vertrag

- Keine AGB-Standard
- Individuelle Konditionen je Anlagen-Profil
- Sicherheiten / Zahlungsbedingungen anlagen-spezifisch

### Sondereinrichtungen

- Bandlast-Privileg § 19 StromNEV
- Strompreiskompensation-Mit-Einbringung
- Atypisches Verbrauchsverhalten

### Risiko-Verteilung

- Strommarkt-Risiko-Übergang
- Brennstoff-Preis-Risiko (Gas)
- CO2-Preis-Risiko
- Regulierungs-Risiko (EEG-Umlage-Reform etc.)

### Vertragsanpassungs-Klauseln (Hardship-Clauses)

- Bei wesentlicher Änderung Marktverhältnisse
- Bei rechtlicher Änderung
- Anpassungs-Verhandlung

## Schritt 6 — Wärmeliefer-Vertrag (AVBFernwärmeV)

Siehe ausführlich Skill `energierecht-waerme-quartier`.

Kern-Punkte hier:

- AVBFernwärmeV als Standard-AGB
- Preisanpassungs-Klauseln nach § 24 Abs. 4 AVBFernwärmeV
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Vertragsdauer max. 10 Jahre + Verlängerung

## Schritt 7 — Mieterstrom-Vertrag

Siehe Skill `energierecht-waerme-quartier` und `energierecht-vertrieb-marktrollen`.

Kern-Punkte:

- EnWG § 42a Mieterstrom-Definition
- Anbieter unterliegt erleichtertem Regime
- Mieter behält Wahlrecht zu anderem Lieferanten
- Vertragsdauer ohne unangemessene Bindung

## Schritt 8 — Vertrags-Migration in Krisen-Zeiten

### Energie-Krise 2022/2023 als Lehrbeispiel

- Massive Preis-Erhöhungen
- Lieferanten-Insolvenzen
- Ersatzversorgung
- Strompreis-/Gaspreis-Bremse 2023

### Vertrags-Reaktion

- Sonderkündigungs-Recht
- Anpassungs-Klauseln aktiviert
- Hardship-Klauseln

### Aktuelle Anwendung

- Nachlauf-Streitigkeiten 2024-2025
- Klage-Wellen über Preisanpassungs-Klauseln
- BGH-Linien stabilisieren

## Schritt 9 — ESG-Verzahnung

### CSRD-Bezug

- Energie-Vertrag Bestandteil ESG-Reporting
- Stromherkunft im Vertrag dokumentieren
- HKN-Lieferung absichern

### Greenwashing-Risiko

- Bei "Ökostrom" ohne HKN-Belege
- UWG-Streit
- Skill `esg-greenwashing-csrd` im Umweltrecht

### CBAM-Auswirkungen

- Indirekt über CO2-Bepreisung Strom
- Vertrags-Anpassungen Industrie-Käufer

## Schritt 10 — Mandanten-Strategie

### Versorger / Lieferant

1. AGB-Audit regelmäßig
2. Preisanpassungs-Klausel-Wirksamkeit absichern
3. Transparenz-Pflichten erfüllen
4. ESG-Reporting CSRD-konform
5. Bilanzkreis-Management strict

### Industrie-Kunde

1. Vertrags-Verhandlung mit Spezialist
2. Risiko-Verteilung optimieren
3. Hardship-Klauseln einbauen
4. Bei Streit AGB-Kontrolle aktiv nutzen

### Kommune (Konzessions-Vergabe)

1. Vergabe-Verfahren EU-konform
2. Übernahme-Optionen sichern
3. Klima-Aspekte einbringen

### Endkunde

1. AGB prüfen vor Vertragsschluss
2. Bei Anpassungs-Mitteilung Plausibilität prüfen
3. Bei Wechsel Vertrags-Übergangs-Modalitäten

## Aktuelle Rechtsprechung & Leitsätze (Stand 05/2026, verifiziert dejure.org / curia.europa.eu)

- **EuGH 23.10.2014, C-359/11 (Schulz)**: Preisanpassungsklauseln in Strom-/Gaslieferungsvertraegen nach AVBEltV/GVV — Aenderungen muessen rechtzeitig mitgeteilt werden, Verbraucher muss Kuendigungsrecht haben. Quelle: curia.europa.eu (CELEX 62011CJ0359).
- **BGH 28.10.2015, VIII ZR 158/11**: Preisanpassung Energielieferungsvertrag — § 5 Abs. 2 GasGVV Transparenz-Anforderungen; AGB-Kontrolle § 307 BGB. Quelle: dejure.org/2015,33580.
- **BGH 24.03.2010, VIII ZR 178/08**: Preisaenderungsklauseln in Sondervertraegen Strom/Gas — wirksame Indexbindung erfordert klare Berechnungsformel. Quelle: dejure.org/2010,5874.
- **BGH 09.02.2011, VIII ZR 295/09**: Billigkeit der Leistungsbestimmung § 315 BGB; Beweislast Versorger für Billigkeit. Quelle: dejure.org/2011,4286.
- **EuGH 02.09.2021, C-718/18**: Unabhaengigkeit der Bundesnetzagentur als Regulierungsbehoerde. Quelle: curia.europa.eu.

**Gesetzeslage 2026:** EnSiG (Energiesicherungsgesetz) — § 24 Anpassungsklauseln bei Gasmangellage (BGBl. I 2022 S. 1054); EnWG-Novellen 2023/2024.

Weitere Aktenzeichen vor Ausgabe per dejure.org / curia.europa.eu verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 315 BGB (billiges Ermessen Leistungsbestimmung) — §§ 305-310 BGB (AGB-Kontrolle) — §§ 36-38 EnWG (Grundversorgung) — § 46 EnWG (Konzessionsvertrag) — AVBEltV / AVBFernwaermeV (Vertragsbeziehungen Grundversorgung) — §§ 313, 314 BGB (Stoerung Geschaeftsgrundlage, Hardship)

## Verzahnung

- `energierecht-vertrieb-marktrollen`
- `energierecht-waerme-quartier`
- `energierecht-industriekunden`
- `energierecht-projektfinanzierung` (PPA)
- `esg-greenwashing-csrd`
- `fachanwalt-bank-kapitalmarktrecht`

## Quellen

- BGB §§ 305 ff. AGB-Kontrolle
- EnWG §§ 36-42a, § 46 (Konzession)
- StromGVV / GasGVV
- AVBFernwärmeV
- EEG § 21 Mieterstrom
- EuGH C-359/11 (Schulz, 23.10.2014); BGH VIII ZR 158/11 (28.10.2015); BGH VIII ZR 178/08 (24.03.2010); BGH VIII ZR 295/09 (09.02.2011); EuGH C-718/18 (02.09.2021)
- DIS / ICC Schieds-Standards
- Schiedsstelle Energie

---

## Skill: `infrastrukturprojekte`

_Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff. EnWG, NABEG, BImSchG, BauGB. Prüfraster: Genehmigungsverfahren, Einwendungen, Planfeststellungsbeschluss, Enteignungsrecht. Output: Genehmigungsverfahrens-Roadmap Energieinfras..._

# Infrastrukturprojekte und Planfeststellung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vorhabentyp (Stromtrasse / Gas-Pipeline / LNG-Terminal / Offshore-Wind / H2-Pipeline)
- Mandant (Vorhabenträger / Anlieger / Umweltverband / Behörde)
- Verfahrens-Stand (Bundesfachplanung / Planfeststellung / Bau / Betrieb)
- Behördliche Zuständigkeit (BNetzA / BSH / Land)
- Klage-/Eil-Bedürfnis

## Schritt 1 — EnLAG (Energieleitungsausbaugesetz)

### Anwendungsbereich

- 24 wesentliche Übertragungs-Stromleitungen Bundeskompetenz
- Bestand seit 2009, Aktualisierung über Bundesbedarfsplan

### Verfahren

- Planfeststellung durch zuständige Landesbehörden
- Bundesnetzagentur ggf. eingebunden

### Beschleunigung

- Verkürzte Klage-Fristen (1 Monat statt 1 Jahr)
- Eingeschränkter Rechtsschutz
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 2 — BBPlG (Bundesbedarfsplangesetz)

### Anwendungsbereich

- Bedarfs-Bestätigung großer Energie-Leitungen
- Aktualisierung alle 4 Jahre
- Aktuell: BBP 2024

### Planungs-Ablauf

1. **Bedarfsplan** mit konkreten Vorhaben
2. **Bundesfachplanung** (Korridor-Bestimmung) durch BNetzA
3. **Planfeststellungsverfahren** (konkreter Trassenverlauf) durch BNetzA für vorgebene Trassen

## Schritt 3 — NABEG (Netzausbaubeschleunigungsgesetz)

### Anwendungsbereich

- Übertragungs-Stromleitungen bundesweit (BMK/Pl-NA)
- Sehr lange Strecken über Bundesländer hinweg

### Verfahrens-Phasen

1. **Bundesfachplanung** (§ 4 NABEG) — Korridor-Festlegung
2. **Planfeststellung** (§§ 18 ff. NABEG) — Detail-Trassenführung
3. **Plangenehmigung** statt Planfeststellung in einfachen Fällen
4. **Antragsverfahren** durch BNetzA

### Beschleunigungs-Mechanismen

- Erdkabel-Vorrang (bei bestimmten Konstellationen)
- Vereinfachte Genehmigung von Provisorien
- Verkürzte Klage-Fristen

### Beteiligungsverfahren

- Öffentlichkeits-Beteiligung
- Behörden-Beteiligung
- Anhörungs-Termine

## Schritt 4 — Offshore-Wind-Recht

### Windenergie-auf-See-Gesetz (WindSeeG)

- Bundeszuständigkeit BSH (Bundesamt für Seeschifffahrt und Hydrographie)
- Ausschreibungen für Offshore-Standorte (Flächen-Modell seit 2022)
- Anschluss-Leitungen verantwortet TenneT / 50Hertz

### Planfeststellung BSH

- Verfahren analog NABEG für See-Bereich
- Umwelt-Verträglichkeits-Prüfung
- Artenschutz (Seevögel, Fledermäuse, Schweinswale)
- Klage VG Hamburg

### Anbindungs-Leitungen

- Vom Offshore-Standort zur Küste (HVDC-Konverter)
- Komplexe Bundesfachplanung
- Land-Trassen-Anschluss

## Schritt 5 — Erdgas-Pipelines und LNG-Terminals

### LNG-Beschleunigungsgesetz (2022, im Zuge Energiekrise)

- Sehr starke Verfahrens-Beschleunigung
- Klage-Möglichkeiten eingeschränkt
- Übergangsweise: Direkt-Genehmigung möglich

### Beispiel-Streit

- Anerkannte Umweltverbände gegen Wilhelmshaven-, Brunsbüttel-LNG
- Klimaschutz-Argumentation (BVerfG-Klimaschluss)
- Verbandsklage UmwRG

### EuGH-Bezug

- Bezug zu RePowerEU
- Beihilfen-Recht bei LNG-Subventionen

## Schritt 6 — Wasserstoff-Stammnetz

### Wasserstoff-Beschleunigungs-Gesetz (geplant)

- H2-Netz § 28r ff. EnWG
- Vereinfachte Genehmigung für Umrüstung Erdgas-Pipelines auf H2
- Bedarfsplanung über Bundesfachplanung

### Verfahren

- Bundes-Bedarfsplan H2 (Eingang in BNEP-Strom-Gas-Integration)
- Korridor-Festlegung
- Planfeststellung detailliert

### Streit-Konstellationen

- Anlieger der umgerüsteten Erdgas-Trassen
- Sicherheits-Bedenken Wasserstoff-Druck

## Schritt 7 — Beschleunigungs-Gebiete RED III

### Mitgliedstaat-Pflicht ab 21.02.2026

- Ausweisung von Beschleunigungs-Gebieten für Erneuerbare
- Vereinfachung Genehmigungs-Verfahren
- Standort-Vorprüfung
- Mitgliedstaaten in Deutschland: Länder-Aufgabe

### Auswirkungen Verfahren

- Verkürzte Bearbeitungs-Fristen
- Reduzierte Umwelt-Verträglichkeits-Prüfung
- Bauleitplanung-Bezug

## Schritt 8 — Klagebefugnis und Rechtsschutz

### Anlieger / Grundeigentümer

- Antragsbefugnis bei direkter Betroffenheit
- Enteignungs-rechtlich relevant (Trassen-Servitut)
- Entschädigungs-Ansprüche

### Umweltverbände UmwRG

- § 2 UmwRG-Klagebefugnis
- Beteiligung im Verfahren erforderlich
- Klima- und Naturschutz-Argumentation
- Skill `klimaklagen-verbandsklage-umwrg` im Umweltrecht-Plugin

### Behörden / andere Träger öffentlicher Belange

- Mitwirkungs-Recht im Verfahren
- Eigene Klage-Befugnis eingeschränkt

### Gerichtsweg

- 1. Instanz BVerwG bei NABEG- und EnLAG-Vorhaben (Anteil-Klage)
- BVerwG sonst Revisions-Instanz nach OVG
- Klage-Frist eng (1 Monat in beschleunigten Verfahren)

## Schritt 9 — BVerwG- und EuGH-Linie

### BVerwG-Schlüssel-Urteile

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BVerwG zur Klimaschutz-Berücksichtigung in Planung

### EuGH-Bezug

- C-411/17 zur Umwelt-Verträglichkeits-Prüfung
- C-275/09 (Aarhus-Konvention)
- C-78/14 zur Beteiligungs-Pflicht

### Aktuelle Klimaklage-Linie

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anwendung auf Fossil-Infrastruktur
- LNG- und Pipeline-Streitigkeiten

## Schritt 10 — Mandanten-Strategie

### Vorhabenträger

1. Frühe Bedarfs-Identifikation
2. Bundesfachplanung-Vorbereitung
3. Öffentlichkeits-Strategie
4. Umwelt-Verträglichkeits-Prüfung sorgfältig
5. Bei Klage: Verteidigungs-Strategie BVerwG-Erfahrung

### Anlieger

1. Beteiligungs-Termine wahrnehmen
2. Substantiierte Einwendungen
3. Bei Trassenführung Alternativen vorschlagen
4. Bei Bescheid Klage erwägen
5. Entschädigungs-Anspruch sichern

### Umweltverband

1. Klima- und Naturschutz-Argumentation
2. Verbandsklage vorbereiten
3. Klimaklagen-Linie nutzen
4. Skill `klimaklagen-verbandsklage-umwrg`

## Schritt 11 — Praktische Beschleunigungs-Optionen

### Vorzeitiger Bau-Beginn

- Bei dringend benötigten Vorhaben
- Antragsverfahren BNetzA / Länder
- Risiko Rückbau bei Klage-Erfolg

### Plangenehmigung statt Planfeststellung

- Bei einfacheren Vorhaben
- Schneller, weniger Beteiligung

### Provisorien

- Bei akuten Engpässen
- Auflagen-Begrenzung

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1 ff. NABEG (Bundesfachplanung) — §§ 1 ff. BBPlG (Bundesbedarfsplan) — §§ 1 ff. EnLAG (Energieleitungsausbau) — §§ 72 ff. VwVfG (Planfeststellung) — §§ 3a, 3b UVPG (UVP-Pflicht) — § 2 UmwRG (Verbandsklagebefugnis)

## Verzahnung

- `energierecht-netz-speicher-zugang`
- `energierecht-eeg-kwkg-erzeugung` (Offshore-Wind)
- `energierecht-emobility-wasserstoff` (H2-Pipeline)
- `klimaklagen-verbandsklage-umwrg` (Umweltrecht)
- `normenkontrolle-bauleitplanung`
- `fachanwalt-verwaltungsrecht` (Klage-Strategie)
- `umweltrecht-verfahren`

## Quellen

- EnLAG / BBPlG / NABEG
- WindSeeG
- LNG-Beschleunigungsgesetz
- Wasserstoff-Beschleunigungs-Gesetz (geplant)
- EnWG § 28r
- UmwRG § 2
- BImSchG §§ 4, 10
- UVPG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BNetzA-Genehmigungs-Beschlüsse
- BSH-Beschlüsse Offshore
- RED III delegierter Akt

---

## Skill: `netz-speicher`

_Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output: Skillauswahl-Empfehlung Energierecht. Abgrenzung: kein inhaltlicher Prüf-Skill im Ener..._

# Energierecht — Kommandocenter (Eingangs-Routing)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Mandant (Stadtwerk, Versorger, Industriekunde, Investor, Behörde, Projektgesellschaft, Privater)
- Lebenszyklus-Phase (Projektentwicklung, Genehmigung, Betrieb, Streit, Transaktion, Insolvenz-/Krisennähe)
- Konkrete Anfrage / Bescheid / Vertragsentwurf
- Fristen erkennbar (Behörden-Frist, Marktrollen-Wechsel, BNetzA-Festlegung, Klagefrist)
- Beteiligte (Übertragungs-Netzbetreiber Anbieter Bilanzkreis-Verantwortliche etc.)

## Schritt 1 — Rolle und Hauptpfad bestimmen

| Rolle | Typischer Hauptpfad |
|---|---|
| Kommune / Stadtwerk | Konzessionsvertrag, Wärmeplanung, Mieterstrom, Beihilfe, EEG/KWKG-Vermarktung |
| Versorger / Stromlieferant | Vertrieb, Bilanzkreis, Beschaffungspreise, Endkunden-AGB, Strompreisbremse-Folge |
| Übertragungs-/Verteilnetzbetreiber | Netzentgelt-Festlegung BNetzA, Netzanschluss, Engpass-Management § 13 EnWG, Redispatch 2.0 |
| Industriekunde | Sondernetzentgelt § 19 StromNEV, EEG-Umlage-Befreiung BesAR-Vorgänger, Strompreiskompensation, PPA |
| Erzeugungs-Investor | EEG-Vermarktung, KWKG, Anlagenzulassung, Direktvermarktung, PPA, BImSchG-Genehmigung |
| Wärme-Projektgesellschaft | Wärmeliefervertrag AVBFernwärmeV, Preisanpassung, Quartierskonzept, Wärmenetz-Anschluss-/Benutzungs-Zwang, BEW-Förderung |
| Wasserstoff-Projektgesellschaft | Elektrolyseur-Genehmigung, RED-III-Anforderungen, Wasserstoff-Netzentwicklungsplan, HRG-Verfahren |
| Mobilität / Ladeinfrastruktur | LSV-Regelung, AFIR, Ladeinfrastruktur-Förderung, Mess- und Eichrecht |
| Privatperson / Mieter | Mieterstrom, PV-Anlage Eigenverbrauch, Heizungswechsel GEG, Energiepreis-Streit |
| Behörde | Stellungnahme, Genehmigung, Aufsichts-Anordnung |

## Schritt 2 — Sachgebiet und Skill-Routing

| Sachgebiet | Folge-Skill |
|---|---|
| EEG / KWKG / Direktvermarktung / Anlagenzulassung | `energierecht-eeg-kwkg-erzeugung` |
| Netzanschluss, Netzentgelte, Engpass, Speicher-Zugang | `energierecht-netz-speicher-zugang` |
| Stromlieferung, Bilanzkreis, GPKE-Prozesse, Marktstammdatenregister | `energierecht-vertrieb-marktrollen` |
| Industriestrompreis, BesAR-Nachfolge, Strompreiskompensation, § 19 StromNEV | `energierecht-industriekunden` |
| Fernwärme, AVBFernwärmeV, kommunale Wärmeplanung, Mieterstrom | `energierecht-waerme-quartier` |
| Wasserstoff-Elektrolyseure, E-Mobilität, Ladeinfrastruktur | `energierecht-emobility-wasserstoff` |
| Stromtrasse-Planfeststellung EnLAG/BBPlG, Genehmigung größerer Vorhaben | `energierecht-infrastrukturprojekte` |
| Energiekonzern M&A, Asset Deal Erzeugungspark, DD-Befund | `energierecht-transaktionen-dd` |
| Bankfinanzierung, PPA-Strukturierung, Förderbescheid KfW BEW | `energierecht-projektfinanzierung` |
| BNetzA-Festlegung, Klage VG/OVG/BVerwG, Bußgeld-Sache | `energierecht-verfahren` |
| Marktbeherrschungs-Verfahren, Missbrauchskontrolle, Energie-spezifische Beihilfe | `energierecht-wettbewerb` |

## Schritt 3 — Kritische Fristen-Prüfung beim Erstkontakt

- **§ 75 EnWG Beschwerde-Frist** ein Monat ab Zustellung BNetzA-Beschluss
- **§ 12 Abs. 4 EnWG Frist Engpass-Anordnung**
- **§ 47 VwGO Normenkontrolle** Wärmepläne Satzungen ein Jahr ab Bekanntmachung
- **§ 33 EEG Frist Inbetriebnahme-Anmeldung** Marktstammdatenregister
- **§ 19 Abs. 2 Satz 2 StromNEV** Antrag Sondernetzentgelt jährlich bis 30.09. für Folgejahr
- **EEG-Förderhöchstwert Ausschreibung** unterjährige Termine BNetzA
- **§ 17 GEG Beratungsgespräch** vor Heizungstausch
- **Strompreisbremse-Abwicklungs-Fristen** (auch nach Auslauf wegen Nachläufer)
- **§ 25 KWKG Antragsfrist** Zuschlag für Bestandsanlagen
- **AVBFernwärmeV § 4 Preisanpassungs-Anzeige-Frist**

## Schritt 4 — Eskalations-Trigger

### Versorgungssicherheits-Notlage

- § 24 EnSiG Maßnahmen
- § 13 EnWG-Eingriffsbefugnisse
- BNetzA-Anordnungen Gas-Notfall-Plan

### Insolvenz-Nähe Versorger

- §§ 36c f. EnWG Ersatzversorger-Mechanismen
- Grundversorger-Wechsel
- Skill `mandat-triage-insolvenzrecht`

### Behördliche Sofort-Anordnung

- § 65 EnWG aufschiebende Wirkung Klage
- Eilantrag § 80 Abs. 5 VwGO

### Kommunale Wärmeplanung Pflicht-Frist

- WPG 30.06.2026 (Großstädte)
- WPG 30.06.2028 (sonstige)
- Bei Versäumnis Sanktion / Folge-Pflichten

## Schritt 5 — Schnittstellen zu anderen Plugins

| Anliegen | Plugin |
|---|---|
| Energieanlagen-Genehmigung BImSchG | `umweltrecht`, neu im `fachanwalt-verwaltungsrecht` |
| Klima- und Naturschutz-Konflikte | `umweltrecht` |
| Stromtrassen-Planfeststellung | `fachanwalt-verwaltungsrecht` plus neuer Skill `energieanlagen-planfeststellung-enlag-bbplg` |
| Steuerliche Fragen Energiebesteuerung | `steuerrecht-anwalt-und-berater` |
| Berufsrecht Anwalt bei Energieprojekt | `kanzlei-allgemein` |
| ESG-Reporting CSRD Energie | `umweltrecht` Skill `esg-greenwashing-csrd` |
| Beihilferecht EU | `europarecht-kompass` |
| Bauleitplanung Wärmenetz-Korridore | `normenkontrolle-bauleitplanung` |
| Wettbewerbs-Verfahren Bundeskartellamt | `fachanwalt-internationales-wirtschaftsrecht` ergänzend |

## Schritt 6 — Mandatskarte und Ampel-Prüfung

Standard-Ausgabe Mandatskarte:

```
Mandant: [Name]
Rolle: [Stadtwerk / Versorger / Industriekunde / …]
Lebenszyklus-Phase: [Projektentwicklung / Betrieb / Streit / Transaktion]
Kritische Frist: [Datum + Norm]
Hauptpfad: [Skill]
Ampel: [GRÜN / GELB / ROT]
Risiko-Komponenten: [Versorgung / Genehmigung / Marktrollen / Förderung]
Naechster Schritt: [konkret]
Dokumenten-Stand: [vollstaendig / mit Luecken / fehlt]
Berufsrecht / DS-Pflichten: [Pruefung erfolgt]
```

### Ampel-Kriterien

- **ROT**: Frist binnen 14 Tagen, Versorgungs-Unterbrechung droht, Bußgeld absehbar, Insolvenz-Nähe Vertragspartner
- **GELB**: Frist binnen 3 Monaten, Genehmigungs-Verfahren mit Ausgang offen, Vertrags-Streit eskaliert
- **GRÜN**: Frist über 3 Monate, klare Rechtslage, kooperative Beteiligte

## Schritt 7 — Erstgesprächs-Fragen

1. **Mandant und Gegen-Seite**: Welche Rolle haben Sie? Wer ist Vertragspartner / Gegner / Behörde?
2. **Phase**: Projektentwicklung, Betrieb, Streit, Verkauf?
3. **Konkrete Anlass-Sache**: Bescheid? Vertragsentwurf? Behördlicher Brief? Klage?
4. **Frist erkennbar**: gibt es eine Datums-genannte Frist? Wenn ja, wann?
5. **Beteiligte Behörden**: BNetzA? Landesregulierungsbehörde? Kommune?
6. **Wirtschaftliche Größenordnung**: Volumen, Investitions-Summe, Streitwert?
7. **Strom- vs. Gas- vs. Wärme-/Wasserstoff-Bezug**?
8. **Förderung beantragt / bewilligt / abgewickelt**?
9. **EEG-/KWKG-Bezug**?
10. **Marktstammdatenregister-Eintrag**?

## Schritt 8 — Berufsrecht und Mandatsführung

- **Berufshaftpflicht** muss energierechtliche Beratung abdecken (häufig Ergänzung-Bedarf bei Allgemein-Kanzleien)
- **Spezialisten-Pflicht** wenn komplexes EEG-Vergabe-Verfahren oder BNetzA-Festlegung — ggf. Mit-Mandat Spezial-Kanzlei
- **Mandatsgeheimnis** § 43a Abs. 2 BRAO bei Geschäftsgeheimnissen Energieanlagen
- **Interessenkonflikt** Prüfung — Anbieter / Netzbetreiber / Verbraucher häufig gegenläufige Interessen

## Schritt 9 — Ausgabe-Standard

- Eingangs-Mandatskarte
- Skill-Routing-Empfehlung
- Frist-Tabelle
- Ampel-Bewertung
- Nächster Schritt formuliert
- Berufsrechts-Vermerk

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 31 EnWG (BNetzA-Beschwerde) — § 75 EnWG (OLG-Beschwerde) — §§ 4, 16 BImSchG (Genehmigung, Aenderung) — § 46 EnWG (Konzessionsvertrag) — §§ 72-78 VwVfG (Planfeststellung) — § 80 Abs. 5 VwGO (Eilrechtsschutz)

## Quellen

- EnWG 2024 (Energiewirtschaftsgesetz, Neufassung)
- EEG 2023 + Solarpaket I 2024
- KWKG 2023
- GEG (Gebäudeenergiegesetz, Reform 01/2024)
- WPG (Wärmeplanungsgesetz, ab 01/2024)
- StromNEV / GasNEV / NAV / NDAV
- AVBFernwärmeV
- EnLAG / BBPlG / WindBG / SolarBG
- BNetzA-Beschlüsse (Festlegungs- und Genehmigungs-Verfahren)
- BVerwG- und EuGH-Linien zu Energierecht

---

## Skill: `projektfinanzierung`

_Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KWKG, BGB. Prüfraster: Finanzierungsstruktur, Sicherheitenpakete, Cashflow-Analyse, Foerderdarlehen. Output: Projektfinanzierungs-Struktur Energieanlage. Abgrenzung: nicht Betrieb..._

# Projektfinanzierung Energie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Projekt-Phase (Konzept, Planung, Realisierung, Betrieb)
- Investitions-Volumen
- Vermarktungs-Strategie (EEG / PPA / Eigenverbrauch / Markt)
- Finanzierungs-Mix (Eigenkapital, Banken, Förderung)
- Bonitäts-Lage Offtaker (PPA-Käufer)
- Steuerliche Strukturierung-Pläne

## Schritt 1 — PPA (Power Purchase Agreement) Strukturierung

### Physisches PPA

- Strom-Lieferung direkt Anlage → Käufer
- Bilanzkreis-Strukturen aufzubauen
- On-Site oder Off-Site
- Mess- und Eichrecht beachten

### Finanzielles PPA (Synthetic / Virtual PPA)

- Strom geht in Markt
- Differenz-Zahlung zwischen Festpreis und Marktpreis
- Bilanz-rechtlich anders strukturiert
- Häufig für internationale Mandanten

### Corporate Direct PPA

- Industrie-Käufer langfristig
- Vorteile beidseitig
- Skill `energierecht-industriekunden`

### Standard-Inhalte PPA

```
1. Vertragsdauer (10-20 Jahre)
2. Liefer-Anlage Identifikation
3. Strom-Mengen mit Volumen-Toleranzbändern
4. Preis-Formel (fest / index-gekoppelt / hybrid)
5. Take-or-Pay-Klauseln
6. Force-Majeure-Definition
7. Anpassungs-Klauseln (Markt, Recht, Steuer)
8. Sicherheiten (Bank-Bürgschaften)
9. Beendigungs-Modalitäten
10. Streit-Klausel (Schiedsverfahren oft)
11. Vertraulichkeits-Klausel
```

## Schritt 2 — Bank-Finanzierung Energie-Projekte

### Project Finance vs. Corporate Finance

- **Project Finance**: Anlage als alleinige Sicherheit; Non-Recourse oder Limited Recourse
- **Corporate Finance**: Konzern haftet zusätzlich
- Bei großen Projekten typisch Project Finance

### Sicherheiten-Konstruktion

- Sicherungs-Übereignung Anlagen-Bestandteile
- Forderungs-Abtretung aus PPA / EEG-Vergütung
- Verpfändung Gesellschaftsanteile
- Konten-Verpfändung Projektgesellschaft
- Step-In-Rechte bei Default

### Kreditgeber-Standards (Lender Requirements)

- DSCR (Debt Service Coverage Ratio) ≥ 1,2-1,4
- Risiko-Reserven (Wartungs-Reserve, DSRA)
- Wartungs-Verträge mit anerkannten Service-Anbietern
- Versicherungs-Schutz
- Regelmäßige Reporting-Pflichten

### Typische Bank-Konsortien

- KfW als Erstkredit-Geber
- Mittelständische Banken (Sparkassen-Verbund)
- Spezial-Energiebanken (UmweltBank, GLS Bank)
- Internationale Banken bei Großprojekten

## Schritt 3 — KfW-Förderprogramme

### KfW 442 BEW (Bundesförderung effiziente Wärmenetze)

- Module 1-3 (Studie / Investition / Betrieb)
- Förderung gestaffelt nach EE-Anteil
- Verzahnung mit kommunaler Wärmeplanung

### KfW 269 EE Energie

- Standard-EE-Anlagen-Investitionen
- Zinsverbilligungen
- Direkt-Förderzuschüsse

### KfW 261 / 262 Energieeffizient Bauen / Sanieren

- Gebäude-Energetik
- Zinsverbilligung + Zuschuss

### Klimaschutzverträge (CCfD)

- BAFA als Behörde
- 4 Mrd. € erstes Förderaufrufs-Volumen
- Bevorzugung KMU
- Differenzvertrag CO2

### Voraussetzungen

- Vor Vorhabens-Beginn
- Innovations- oder Effizienz-Komponente
- Realisierung in spezifizierter Zeit
- Reporting-Pflichten

### Rückforderungs-Risiko

- Bei Verstoß gegen Auflagen
- Rückforderung mit Zinsen
- 10-Jahres-Rückblick möglich

## Schritt 4 — Förder-Bescheid und Rechtsmittel

### Bewilligungs-Bescheid

- Verwaltungsakt
- Klage VG bei Ablehnung
- Skill `energierecht-verfahren`

### Auflagen-Compliance

- Dokumentations-Pflichten
- Audit-Termine
- Bei Verstoß Eilantrag möglich

### Bei Widerruf

- Aussetzungs-Antrag § 80 Abs. 5 VwGO
- Frist eng

## Schritt 5 — Sale-and-Leaseback

### Konzept

- Anlage wird an Bank / Leasing-Gesellschaft verkauft
- Leasing-rück an Projektgesellschaft
- Steueroptimierung
- Liquiditäts-Effekt

### Konditionen

- Steuerliche Gestaltung wichtig
- Leasing-Vertrag mit Optionen
- Risiken bei Steuer-Reform

### Sektor-Akzeptanz

- Bei Wind / Solar etabliert
- Bei innovativen Technologien fragwürdig

## Schritt 6 — Bonitäts-Prüfung Offtaker

### PPA-Käufer Risiko

- Insolvenz Offtaker = Vermarktungs-Verlust Anlage
- Long-term Verträge mit Industrie-Käufern üblich
- Bonität A oder besser empfohlen

### Sicherheiten gegen Käufer-Insolvenz

- Bank-Bürgschaft Offtaker
- Eltern-Garantie Mutter-Gesellschaft
- Verbindungs-zu-Vermarktungs-Möglichkeit (Markt-Default)

### Mehrere Offtaker

- Risiko-Streuung
- Komplexere Bilanzkreis-Strukturen

## Schritt 7 — Stranded-Assets-Risiko

### Definition

- Anlage wird vorzeitig wirtschaftlich entwertet
- Z.B. fossile Anlage durch CO2-Preis
- Politik-Risiko

### Mitigation

- Förderung mit Bestandsschutz
- Vertraglich abgesicherte Vermarktung
- Diversifikation Portfolio

### ESG-Aspekt

- Banken-Politik: keine neuen fossilen Kredite
- Insurance retreat (Versicherung)
- Pension-Fund-Aspekte

## Schritt 8 — Spezial-Finanzierungen

### Bürgerwind / Bürgerenergie

- Bürgerenergie-Gesellschaften
- Privilegierungen in EEG-Ausschreibung
- Crowd-Funding-Strukturen
- Genossenschafts-Modelle

### Mezzanine-Kapital

- Hybride zwischen Eigen- und Fremd-Kapital
- Höhere Zinsen, weicherer Rückgriff

### Bond / Schuldschein

- Bei großen Anlagen
- Kapitalmarkt-Zugang
- Wertpapier-Prospekt-Pflichten

### Grüne Anleihen (Green Bonds)

- Spezifische Ratings (CICERO, ISS-Oekom)
- EU-Green-Bond-Standard ab 2024
- ESG-Investoren

## Schritt 9 — Steuerliche Aspekte

### Anlagen-Abschreibung

- AfA-Tabelle für Energie-Anlagen
- Sonder-Abschreibungs-Optionen
- Investitionsabzugsbetrag § 7g EStG

### Investitionsabzugsbetrag

- Mittelständische Investoren
- Vor Anschaffung
- Auflösungs-Pflicht bei nicht-Realisierung

### Stromsteuer-Pflicht

- Eigenstrom-Verbrauch
- Stromsteuer-Vergütung Industrie
- Skill `energierecht-industriekunden`

### Umsatzsteuer Klein-Anlagen

- Kleinunternehmer-Regelung
- Pauschalierung möglich

## Schritt 10 — Mandanten-Strategie

### Projekt-Entwickler

1. Finanzierungs-Mix optimieren
2. PPA-Vermarktung vor Bau verhandeln
3. KfW-/CCfD-Förderung beantragen
4. Sicherheiten-Konstruktion mit Anwalt
5. Closing-Termine straff

### Bank / Kreditgeber

1. DD-Standard hoch
2. Sicherheiten-Bündel umfassend
3. Reporting-Pflichten klar
4. Step-In-Rechte sichern

### Offtaker (PPA-Käufer)

1. Bonitäts-Sicherheit Anlage
2. Vermarktungs-Risiko verteilen
3. ESG-Reporting CSRD-konform

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1191 ff. BGB (Grundschuld als Sicherheit) — §§ 398, 399 BGB (Forderungsabtretung) — § 307 BGB (AGB-Kontrolle Take-or-Pay) — §§ 48, 49 VwVfG (Rücknahme, Widerruf Foerderbescheid) — §§ 19-21 EEG (Verguetungs-Anspruch als Sicherungs-Gegenstand) — §§ 1 ff. KWG (Finanzierung durch Kreditinstitute)

## Verzahnung

- `energierecht-eeg-kwkg-erzeugung`
- `energierecht-industriekunden` (PPA-Käufer)
- `energierecht-transaktionen-dd` (Erwerb)
- `energierecht-waerme-quartier` (BEW)
- `europarecht-kompass` (Beihilfen)
- `fachanwalt-bank-kapitalmarktrecht`
- `corporate-kanzlei`

## Quellen

- EEG § 27a (Doppelvermarktungs-Verbot)
- KfW-Förderrichtlinien 442, 269, 261, 262
- Klimaschutzverträge-Programm BMWK / BAFA
- EU-AGVO 651/2014
- EU-Green-Bond-Standard 2023/2631
- BFH zu Energie-Steuer und Abschreibung
- ICMA Green Bond Principles
- TLB / IF-Konzepte zu Project Finance Energie

---
<!-- AUDIT 27.05.2026 -->

---

## Skill: `transaktionen-dd`

_Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Prüfraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken. Output: Due-Diligence-Bericht Energietransaktion. Abgrenzung: nicht Projektfinanzie..._

# Energie-Transaktionen und Due Diligence

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Transaktions-Gegenstand (Anlage, Gesellschaft, Portfolio)
- Verkäufer-/Käufer-Konstellation
- Transaktions-Phase (Letter of Intent, DD, SPA-Verhandlung, Closing)
- Anlagen-Stand (Inbetriebnahme, Förderung, Vertrags-Bindungen)
- Aktive Verfahren bei BNetzA / BAFA / Gerichten

## Schritt 1 — Asset vs. Share Deal

### Asset Deal

- Einzel-Übertragung Anlage(n), Verträge, Genehmigungen
- Verträge müssen einzeln auf Käufer überführt werden
- Genehmigungen über § 16 BImSchG Wechsel-Anzeige
- EEG-Vergütung über § 33 EEG-Wechsel

### Share Deal

- Gesellschafts-Anteile gehen über
- Verträge und Genehmigungen bleiben bei Gesellschaft
- Häufig einfacher zu strukturieren
- Aber: Steuerliche und haftungsrechtliche Erbschaft

### Wahl-Kriterien

- Bei Einzel-Anlage häufig Asset Deal
- Bei Portfolio mit vielen Anlagen Share Deal
- Steuerliche Optimierung (Anschaffungs-Kosten, Abschreibungen)
- Haftungs-Verteilung (Asset Deal sauberer)

## Schritt 2 — Due Diligence Energie-spezifisch

### Technical DD

- Anlagen-Zustand, Wartungs-Historie
- Restlaufzeit-Schätzung
- Service-Verträge

### Regulatory DD

- **EEG-Vergütungs-Anspruch** und Restlaufzeit
- **MaStR-Eintrag** korrekt und aktuell
- **BImSchG-Genehmigung** und Auflagen-Compliance
- **Repowering-Potenzial** und Genehmigungs-Lage
- **Anschluss-Punkt** Bestand und Erweiterungs-Möglichkeit

### Commercial DD

- **PPA-Bestand** Laufzeiten Konditionen
- **Strompreis-Forecast** Sensitivitäten
- **Wartungs-Verträge** und Kostenstruktur
- **Versicherungs-Status**

### Legal DD Schwerpunkte

- **Grundstücks-Verträge** (Eigentum, Pacht, Nießbrauch, Dienstbarkeiten)
- **Anschluss-Vertrag Netzbetreiber**
- **Förder-Bescheide** und Auflagen
- **Streitigkeiten** anhängig
- **Wartungs-/Pacht-/PPA-Verträge**

### Tax DD

- Strom-Steuer-Pflicht
- Bewertung Anlagen-Vermögen
- Sonderabschreibungs-Möglichkeiten
- Eigenstromsteuer-Pflicht

### ESG DD

- CSRD-Berichts-Konformität
- Naturschutz-Compliance
- Sozial-Aspekte (Bürger-Beteiligung)

## Schritt 3 — EEG-Vergütungs-Anspruch im Asset Deal

### § 33 EEG Wechsel

- Anlagen-Betreiber kann wechseln
- Vergütungs-Anspruch geht auf Käufer über
- MaStR-Aktualisierung Pflicht binnen Monat

### Bedingungen Übergang

- Anlage und Stand-Ort bleiben gleich
- Vergütungs-Höhe und -Dauer unverändert
- Bei Repowering: Re-Zulassung erforderlich

### Risiken Käufer

- Vergangenheits-Verstöße des Verkäufers können auf Vergütung wirken
- BNetzA-Prüfung möglich
- Garantien im SPA erforderlich

## Schritt 4 — Distressed-Asset-Verkauf

### Insolvenz-Konstellation

- Anlage in Insolvenz des Verkäufers
- Insolvenz-Verwalter veräußert
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Anfechtungs-Risiko

- Bei Verkauf in Insolvenz-Nähe § 133 InsO
- Skill `vorsatzanfechtung-133-inso` im Insolvenzrecht-Plugin
- Gleichwertigkeits-Prüfung Verkaufs-Preis

### Bewertungs-Komplexitäten

- Anlagen-Wert in Insolvenz häufig deutlich reduziert
- Zukunftserlöse mit Risiko-Aufschlag diskontiert
- LCOE-Vergleich (Levelized Cost of Energy)

## Schritt 5 — Beihilfen-Prüfung

### Förder-Bescheide

- KfW BEW, Klimaschutzverträge, Ausschreibungs-Zuschläge
- Übertragung auf Käufer prüfen
- Häufig Genehmigungs-Pflicht durch Behörde

### De-minimis-Grenze

- EU-Beihilfenrecht
- Bei mehreren Förderungen kumulieren
- 200.000 € in 3 Jahren (allgemein)

### EU-AGVO 651/2014

- Allgemeine Gruppenfreistellungs-Verordnung
- Häufige Rechtsgrundlage Förderungen Energiebereich
- Auflagen-Compliance dokumentieren

### Rückforderungs-Risiko

- Bei Beihilfen-Verstoß EU-Kommission
- Verzinsung bis 10 Jahre rückwirkend
- Skill `europarecht-kompass`

## Schritt 6 — Strompreiskompensation-Rückforderungs-Risiko

### Konstellation

- Bei Strompreiskompensation-Empfänger Verkauf an Käufer
- Voraussetzungen müssen weitergeführt werden (Branche, Stromintensität)
- Bei nicht-Weiterführung Rückforderung BAFA

### SPA-Klausel

- Indemnification für Rückforderungs-Fälle
- Pflicht zur Weiterführung Bedingungen

## Schritt 7 — Bewertungs-Methodik

### DCF-Methode

- Frei-Cashflow-Diskontierung
- Anzulegender Wert / Marktpreis-Forecast als Einnahmen
- Wartungs-Kosten, Steuern, Försterung-Aufwendungen
- WACC-Bestimmung mit Risiko-Aufschlag

### LCOE-Vergleich

- Levelized Cost of Energy
- Vergleich mit Alternativ-Anlagen
- Investitions-Entscheidung

### Sensitivitäten

- Strompreis-Volatilität
- Anlagen-Verfügbarkeit
- Regulierungs-Risiken (Förder-Änderung)

### Multiple-Methode

- Bei Portfolio-Transaktionen
- € pro installierte MW
- € pro EBITDA

## Schritt 8 — SPA-Struktur (Share Purchase Agreement)

### Garantien Verkäufer

- Eigentum unbelastet
- Anlagen funktionsfähig
- EEG-Vergütung Bestand
- MaStR-Eintrag korrekt
- BImSchG-Compliance
- Keine offenen Verfahren

### Garantie-Erfüllungs-Zeitraum

- Typisch 24 bis 36 Monate
- Verlängert bei Steuer-Sachverhalten

### Indemnification

- Spezifische Sachverhalte (z.B. Strompreiskompensation)
- Haftungs-Höchstgrenze

### Conditions Precedent

- BNetzA-Anzeige § 33 EEG
- BImSchG-Wechsel-Anzeige § 16
- Förder-Bescheid-Übertragung
- Kartellamts-Freigabe
- ggf. § 12 BauGB-Übertragungs-Genehmigung

### Closing-Procedure

- Vor-Closing Bedingungen erfüllt
- Übertragungs-Akte
- Zahlungs-Abwicklung

## Schritt 9 — Kartellrechtliche Aspekte

### Marktbeherrschungs-Anmeldung

- Bei größeren Energieanlagen-Transaktionen
- Bundeskartellamt 9. Beschlussabteilung Energie
- Anmeldeschwelle BKartA

### EU-Anmeldepflicht

- Bei größerem Volumen EU-Kommission
- Phase-I- und Phase-II-Verfahren

## Schritt 10 — Mandanten-Strategie

### Verkäufer

1. Vendor DD durchführen
2. Garantie-Risiken minimieren
3. Indemnification-Klauseln verhandeln
4. Tax-Optimierung
5. Closing-Zeitplan straff

### Käufer

1. Sorgfältige DD mit Energie-Spezialisten
2. Bewertungs-Sensitivitäten
3. Garantie-Forderungen
4. Conditions Precedent klar
5. Integrations-Plan vorbereiten

### Investor / PE

1. Portfolio-Aufbau Logik
2. Bei mehreren Anlagen Plattform-Strategie
3. Skalen-Vorteile (Wartung, Vermarktung)
4. Exit-Strategie 5-7 Jahre

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 453, 437, 434 BGB (Rechtskauf, Maengelhaftung, Beschaffenheitsvereinbarung) — §§ 75 ff. UmwG (Spaltung, Umstrukturierung Energiegesellschaft) — §§ 48, 49 VwVfG (Widerruf Foerderbescheid) — § 33 EEG (MaStR-Eintrag) — Art. 107, 108 AEUV (Beihilfen-Rueckforderung)

## Verzahnung

- `energierecht-eeg-kwkg-erzeugung`
- `energierecht-projektfinanzierung`
- `energierecht-industriekunden` (Strompreiskompensation)
- `vorsatzanfechtung-133-inso` (Distressed)
- `europarecht-kompass` (Beihilfen)
- `corporate-kanzlei` / `grosskanzlei-corporate-ma` für M&A-Standards

## Quellen

- EEG § 33 (Anlagen-Wechsel)
- BImSchG § 16
- MaStRV § 5
- UmwG / GmbHG / AktG für Share Deals
- EU-AGVO 651/2014
- EU-Beihilfen-Verfahrens-Verordnung 2015/1589
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BFH zu Energie-Steuer-Behandlung
- Bundeskartellamt-Praxis Energie-Fusionen

---
<!-- AUDIT 27.05.2026 -->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

