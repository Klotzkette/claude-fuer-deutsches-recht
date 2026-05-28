---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Legistik Werkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Legistik-Werkstatt — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Legistik Werkstatt**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Legistik-Werkstatt für Bundes- und Landesministerien. Erstellt Referentenentwuerfe Kabinettsentwuerfe Formulierungshilfen Rechtsverordnungen Satzungen mit Begründung Synopse Lesefassung XML. Prüfung Verfassungsrecht Europarecht Folgenabschaetzung Goldplating. DOCX im offiziellen HdR-Layout.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

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
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

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

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `begruendung-allgemein-und-besonders` | Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil… |
| `dokumente-rendern-docx-pdf` | Legistische Dokumente als DOCX oder PDF im offiziellen Erscheinungsbild der Bundesregierung bzw. des Bundestages rendern. Anwendungsfall fertiger Entwurf soll als lieferfähiges Dokument nach Handbuch der… |
| `europarechtskonformitaet` | Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht… |
| `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik… |
| `folgenabschaetzung-nachhaltigkeit` | Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen… |
| `formulierungshilfe-bauen` | Formulierungshilfe aus der Mitte des Bundestages oder Landtages aufbauen. Anwendungsfall Koalitionsfraktionen wollen Aenderung einbringen ohne neues Ressortabstimmungsverfahren und Verbandeanhoerung zu starten. Aufbau… |
| `gesetzesentwurf-kabinett` | Kabinettsentwurf der Bundesregierung oder Landesregierung aus dem Referentenentwurf nach Ressortabstimmung erstellen. Anwendungsfall Ressortabstimmung und Verbandeanhoerung sind abgeschlossen Kabinettsvorlage muss… |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73… |
| `goldplating-vermeiden` | Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten. Anwendungsfall Referentenentwurf setzt EU-Richtlinie um und muss auf ueberschiessende nationale Regelungen über den… |
| `inkrafttreten-uebergangsrecht` | Inkrafttretens- und Übergangsregelung für Gesetze und Verordnungen formulieren. Anwendungsfall Entwurf ist inhaltlich fertig Artikel Inkrafttreten und Übergangsrecht muessen noch ergaenzt werden. Standardformel… |
| `legistik-auftragsaufnahme` | Legistischen Auftrag strukturiert aufnehmen und in operationale Regelungsziele umwandeln. Anwendungsfall Erstkontakt zu einem neuen legistischen Vorhaben Koalitionsvertrag Beschluss Kabinett Landtag Aufsichtsweisung… |
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Aenderung aussieht ohne… |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Aenderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten… |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten.… |
| `normhierarchie-routing` | Richtige Normbene für ein legistisches Vorhaben bestimmen Bundesgesetz Landesgesetz Rechtsverordnung oder Satzung. Anwendungsfall politische Vorgabe liegt vor unklar auf welcher Ebene geregelt werden soll. Prüfkatalog… |
| `referentenentwurf-bauen` | Vollständigen Referentenentwurf des Bundes oder Landes aufbauen. Anwendungsfall legistischer Auftrag ist aufgenommen Normebene ist bestimmt Entwurfstext und Begründung muessen nach HdR erstellt werden. Format HdR… |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft… |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Schulungsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder… |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Aenderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Aenderungen schnell zu erfassen.… |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine… |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu… |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft… |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist.… |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert… |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte… |

## Worum geht es?

Die Legistik-Werkstatt ist ein Plugin fuer Referentinnen und Referenten in Bundes- und Landesministerien, fuer Verfassungsrechtlerinnen und Verfassungsrechtler sowie fuer Verbandsvertreter, die Gesetzesentwuerfe, Rechtsverordnungen und Satzungen erstellen, pruefen und in den parlamentarischen Prozess einbringen.

Das Plugin deckt alle Phasen des Gesetzgebungsverfahrens ab: von der Auftragsaufnahme ueber den Referentenentwurf, die Ressortabstimmung, Verbandeanhoerungen, die Kabinettsreife, Synopsen und Lesefassungen bis zur XML-Paralleldarstellung. Es enthaelt ausserdem Quercheckmodule fuer Verfassungsmaessigkeit, Europarechtskonformitaet, Erfuellungsaufwand und Goldplating-Vermeidung.

## Wann brauchen Sie diese Skill?

- Ein Referat im Bundesministerium erstellt einen Referentenentwurf und braucht eine strukturierte Auftragsaufnahme mit Regelungszielen.
- Eine Normenkontrollrats-Vorlage muss fristgerecht vorbereitet und mit einem KMU-Check versehen werden.
- Ein Ministerium will einen bestehenden Entwurf auf Verfassungsmaessigkeit und Europarechtskonformitaet pruefen.
- Eine Rechtsverordnung wird entworfen und die Verordnungsermaechtigung nach Art. 80 GG muss geprueft werden.
- Nach Inkrafttreten soll eine konsolidierte Lesefassung des geaenderten Stammgesetzes erstellt werden.

## Fachbegriffe (kurz erklaert)

- **HdR** — Handbuch der Rechtsfoermlichkeit; Leitfaden des Bundesjustizministeriums fuer die Formulierung von Rechtstexten.
- **GGO** — Gemeinsame Geschaeftsordnung der Bundesministerien; regelt Verfahren und Fristen fuer die Ressortabstimmung.
- **NKR** — Nationaler Normenkontrollrat; unabhaengiges Gremium, das Erfuellungsaufwand und buerokratische Belastungen prueft.
- **Goldplating** — Ueberimplementierung von EU-Richtlinien: nationale Zusatzanforderungen ueber das EU-Mindestmass hinaus.
- **Synopse** — Gegenueberststellung von bisherigem Recht, neuem Recht und Aenderungsbefehl in einer Dreispalten-Tabelle.
- **LegalDocML** — Maschinenlesbares XML-Format fuer deutsche Rechtstexte; Standard des Bundesjustizministeriums.
- **Normenkartierung** — Systematische Erfassung aller durch ein Vorhaben beruehrten Normen und ihrer Aenderungsbedarfe.
- **Kabinettsentwurf** — Abgestimmter Regierungsentwurf, der dem Kabinett zur Beschlussfassung vorgelegt wird.

## Rechtsgrundlagen

- Art. 70-74 GG (Gesetzgebungskompetenzen Bund und Laender)
- Art. 80 Abs. 1 GG (Verordnungsermaechtigung)
- Art. 76-78 GG (Gesetzgebungsverfahren im Bund)
- GGO (Gemeinsame Geschaeftsordnung der Bundesministerien)
- Art. 288 AEUV (Wirkung von EU-Verordnungen und Richtlinien)
- Art. 267 AEUV (Vorabentscheidungsverfahren EuGH)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Legistischen Auftrag aufnehmen und Regelungsziele klaeren (`legistik-auftragsaufnahme`).
2. Normhierarchie und Kompetenzgrundlage bestimmen (`normhierarchie-routing`, `gesetzgebungskompetenz-pruefen`).
3. Geeigneten Entwurfstyp auswaehlen: Referentenentwurf, Rechtsverordnung oder Satzung.
4. Quercheck-Module nutzen: Verfassungsmaessigkeit, Europarecht, Goldplating, Erfuellungsaufwand.
5. Ressortabstimmung und Verbandeanhoerung steuern, dann zur Kabinetts- oder Parlamentsreife fuehren.

## Skill-Tour (was gibt es hier?)

- `legistik-auftragsaufnahme` — Legistischen Auftrag strukturiert aufnehmen und in Regelungsziele umwandeln.
- `normhierarchie-routing` — Richtige Normbene bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung oder Satzung.
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz nach Art. 70-74 GG pruefen bevor Entwurf aufgesetzt wird.
- `satzungskompetenz-pruefen` — Satzungskompetenz fuer Koerperschaften und Anstalten des oeffentlichen Rechts pruefen.
- `verordnungsermaechtigung-art80` — Verordnungsermaechtigung nach Art. 80 Abs. 1 GG pruefen bevor Rechtsverordnung entworfen wird.
- `referentenentwurf-bauen` — Vollstaendigen Referentenentwurf des Bundes oder Landes aufbauen.
- `gesetzesentwurf-kabinett` — Kabinettsentwurf nach Ressortabstimmung aus dem Referentenentwurf erstellen.
- `formulierungshilfe-bauen` — Formulierungshilfe aus der Mitte des Bundestages oder Landtages aufbauen.
- `begruendung-allgemein-und-besonders` — Zweiteilige Begruendung zu Gesetzesentwurf oder Verordnung (Allgemeiner Teil, Besonderer Teil) verfassen.
- `verfassungsmaessigkeit-quercheck` — Querschnittspruefung Verfassungsmaessigkeit eines Gesetzesentwurfs oder einer Verordnung.
- `europarechtskonformitaet` — Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht pruefen.
- `goldplating-vermeiden` — Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten.
- `folgenabschaetzung-erfuellungsaufwand` — Erfuellungsaufwand fuer Buerger, Wirtschaft und Verwaltung ermitteln und darstellen.
- `folgenabschaetzung-nachhaltigkeit` — Weitere Folgen und Nachhaltigkeitspruefung fuer Gesetzesentwurf erstellen.
- `normenkontrollrat-kmu-check` — Vorlage an den NKR vorbereiten und KMU-Check durchfuehren.
- `normenkartierung` — Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Aenderungsmatrix aufbauen.
- `terminologie-konsistenz` — Terminologie-Konsistenz im legistischen Entwurf pruefen und Begriffstabelle aufbauen.
- `zirkelschluss-pruefen` — Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren.
- `inkrafttreten-uebergangsrecht` — Inkrafttretens- und Uebergangsregelungen fuer Gesetze und Verordnungen formulieren.
- `verbaendeanhoerung-ressortabstimmung` — Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten.
- `synopse-erstellen` — Synopse als Dreispalten-Tabelle (bisheriges Recht, neues Recht, Aenderungsbefehl) erstellen.
- `lesefassung-konsolidiert` — Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen.
- `xml-paralleldarstellung` — Maschinenlesbare Paralleldarstellung in LegalDocML.de oder eNorm-XML erstellen.
- `dokumente-rendern-docx-pdf` — Legistische Dokumente als DOCX oder PDF im offiziellen HdR-Layout rendern.
- `schulung-legistik` — Trainerleitfaden fuer Legistik-Schulungen mit der Schulungsakte erstellen.

## Worauf besonders achten

- Kompetenzgrundlage zuerst: Ohne geklarte Gesetzgebungskompetenz nach Art. 70 ff. GG darf kein Entwurf aufgesetzt werden.
- Goldplating ist politisch und juristisch heikel: Nationale Mehrbelastungen ueber EU-Mindestanforderungen hinaus muessen explizit begruendet werden.
- NKR-Fristen sind verbindlich: Vorlage muss mit vollstaendigen Erfuellungsaufwands-Angaben rechtzeitig erfolgen.
- Terminologie-Konsistenz ist elementar: Verschiedene Begriffe fuer dasselbe Konzept koennen zu Auslegungsstreitigkeiten fuehren.
- Uebergangsrecht nicht vergessen: Altfallregelungen und Bestandsschutz sichern Rechtsicherheit und vermeiden Verfassungsruegen.

## Typische Fehler

- Referentenentwurf ohne Verfassungsmaessigkeits-Check: Entwurf wird in der Ressortabstimmung oder im Parlament wegen Grundrechtsverletzung zurueckgewiesen.
- Verordnungsermaechtigung zu unbestimmt: Art. 80 Abs. 1 GG verlangt Inhalt, Zweck und Ausmass — Blankoermaechtigung ist nichtig.
- Goldplating unerkannt: Nationale Umsetzung geht ueber die Richtlinienpflichten hinaus, ohne dass dies im Entwurf kenntlich gemacht wird.
- Synopse fehlt: Ressortabstimmung und parlamentarische Beratung werden durch fehlende Gegenueberststellung ernsthaft erschwert.
- Inkrafttreten ohne Uebergangsrecht: Adressaten koennen sich nicht rechtzeitig auf neue Pflichten einstellen.

## Querverweise

- `datenschutzrecht` — DSGVO-Umsetzungsgesetze und datenschutzrechtliche Folgenabschaetzungen bei neuen Regelungsvorhaben.
- `regulatorisches-recht` — Nationale Umsetzung von Finanzmarkt-Richtlinien (KWG, ZAG, DORA) als legistisches Vorhaben.
- `energierecht` — Gesetzgebungsverfahren fuer EEG-Novellen, EnWG-Aenderungen und GEG-Fortentwicklung.

## Quellen und Aktualitaet

- Stand: 05/2026
- GG (Grundgesetz) in der zum Stand-Datum geltenden Fassung
- GGO (Gemeinsame Geschaeftsordnung der Bundesministerien) in der geltenden Fassung
- HdR (Handbuch der Rechtsfoermlichkeit) 3. Auflage des Bundesjustizministeriums
