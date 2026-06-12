---
name: bmleh
description: "Einstieg, Schnelltriage und Fallrouting im Legistik Werkstatt-Plugin für Bundesministerien, Bundestag, Fraktionen, Landesministerien, Landtage und sonstige Normgeber. Fragt Startbahn, Institution, Bundesland, Ressort, Fraktion, Verfahrensstand, Fristen, Unterlagen, Risiken und Wunsch-Output ab, s"
---

# Legistik-Werkstatt — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GGO Ressortbeteiligung i.d.R. 4 Wochen, NKR-Stellungnahme 4 Wochen, Bundesrat 1. Durchgang 6 Wochen / 9 Wochen, Vermittlungsausschuss nach Bedarf.
- Tragende Normen verifizieren: GGO §§ 40-49 (Rechtsetzungsverfahren), Handbuch der Rechtsförmlichkeit (BMJ), NKR-Gesetz, BGleiG, IT-Konsolidierungs-Konzept, eNorm-Standard, GG Art. 76, 77, 78 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Ressort (BMJ und Fachressort), Bundeskanzleramt, Bundesrat, NKR, Bundestagsausschüsse, Bundesregierung, Wissenschaftliche Dienste, Lobbyregister.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Referentenentwurf, BT-Drucksache, Gesetzesfolgenabschätzung, NKR-Stellungnahme, Verbändeanhörungs-Stellungnahme, Synopse, Erfüllungsaufwandsberechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Legistik Werkstatt**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Legistik-Werkstatt für Bundesministerien, Bundestag, Fraktionen, einzelne parlamentarische Initiativen in Fraktionsstärke, Landesministerien, Landesregierungen, Landtage, kommunale Rechtsämter, Kammern, Hochschulen und sonstige Normgeber. Erstellt Referentenentwürfe, Kabinettsentwürfe, Gesetzentwürfe aus der Mitte des Bundestages oder Landtages, Änderungsanträge, Entschließungsanträge, Anträge, Formulierungshilfen, Rechtsverordnungen und Satzungen mit Begründung, Synopse, Lesefassung und XML. Prüfung Verfassungsrecht, Europarecht, Folgenabschätzung, Goldplating, Rechtsförmlichkeit und parlamentarische Einreichungsfähigkeit. DOCX im passenden Regierungs-, Parlaments- oder HdR-Layout.

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

### 1. Startbahn klären: Wer steuert das Vorhaben?

Vor jedem Entwurf zuerst die institutionelle Startbahn bestimmen. Danach erst Normebene, Entwurfsformat und Fachmodule auswählen.

| Startbahn | Typische Nutzer | Typische Outputs | Sofort zu klären |
|---|---|---|---|
| Bundesressort / Bundesregierung | Bundesministerium, Bundeskanzleramt, nachgeordnete Fachvorbereitung | Eckpunkte, Referentenentwurf, Kabinettsentwurf, Rechtsverordnung, Ressortabstimmung, NKR-Unterlagen | Ressort, Referat, Federführung, Mitzeichnung, Kabinetts- oder Hausleitungsauftrag, GGO-/HdR-Format |
| Bundestag / Fraktion / Abgeordnete | Koalitionsfraktion, Oppositionsfraktion, Gruppe oder Abgeordnete in erforderlicher Stärke | Gesetzentwurf aus der Mitte des Bundestages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Ausschussfassung | Fraktion/Gruppe, Regierungs- oder Oppositionsrolle, laufende Drucksache, Ausschuss, Lesung, Einreichungsform, GO-BT-Anforderungen |
| Landesregierung / Landesministerium | Landesministerium, Staatskanzlei, Landesregierung | Landesreferentenentwurf, Landesverordnung, Kabinettsvorlage, Landtagsdrucksache | Bundesland, Ressort, Landesverfassung, Landes-Geschäftsordnung, Verkündungsblatt, Beteiligungsregeln |
| Landtag / Landtagsfraktion | Regierungsfraktion, Oppositionsfraktion, Gruppe, Ausschuss | Landesgesetzentwurf aus der Mitte des Landtags, Änderungsantrag, Entschließungsantrag, Antrag | Bundesland, Landtag, Fraktion, Verfahrensstand, Geschäftsordnung des Landtags, Haushalts- und Zuständigkeitsfragen |
| Sonstiger Normgeber | Kommune, Kammer, Hochschule, Sozialversicherungsträger, Zweckverband | Satzung, Verordnung, Verwaltungsvorschrift, Bekanntmachung, Beschlussvorlage | Rechtsgrundlage, Aufsicht, Organ, Bekanntmachungsform, Genehmigungserfordernis |

Wenn die Startbahn unklar ist, frage genau eine Entscheidungsfrage: "Kommt das Vorhaben aus einem Ministerium, aus dem Bundestag/Landtag oder von einem sonstigen Normgeber?"

### 2. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle / Institution | Wer fragt: Bundesministerium, Bundestagsfraktion, Abgeordneter, Oppositionsfraktion, Landesministerium, Landtagsfraktion, Kommune, Kammer, Hochschule, Verband? | Verfahrensrecht, Ton und Einreichungsform hängen daran. |
| Gebietskörperschaft | Bund oder welches Bundesland? Bei sonstigen Normgebern: welche Gemeinde/Kammer/Hochschule und welches Aufsichtsrecht? | Landesrecht und Geschäftsordnungen unterscheiden sich stark. |
| Ressort / Fraktion / Organ | Welches Ministerium, Referat, Ausschuss, Fraktion, Gruppe, Organ oder Gremium steuert? | Zuständigkeit, Federführung und formaler Absender müssen getrennt werden. |
| Ziel | Was soll entstehen: Eckpunkte, Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte, Änderungsantrag, Entschließungsantrag, Antrag, Rechtsverordnung, Satzung, Synopse, Lesefassung, XML? | Output sofort sauber ausrichten. |
| Verfahrensstand | Vorfeld, Ressortabstimmung, Kabinett, 1./2./3. Lesung, Ausschuss, Vermittlung, Landesverfahren, Satzungsbeschluss? | Der richtige Skill hängt am Stadium. |
| Sachverhalt | Welches Problem, welche Adressaten, welche Regelungsalternativen und welche politischen Vorgaben sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Kabinettstermine, Ausschussfristen, Drucksachenschluss, Landtagsfristen, Anhörungsfristen, EU-Fristen oder Verkündungstermine? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Entwürfe, Drucksachen, Änderungsanträge, Synopsen, Kabinettsvorlagen, Stellungnahmen, Tabellen oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Kompetenzmangel, Verfassungsbruch, EU-Verstoß, Haushaltsproblem, Vollzugsdefizit, NKR-/Erfüllungsaufwand, Reputationsschaden oder politische Angreifbarkeit? | Priorität und Vorsicht einstellen. |
| Format | Regierungsstil, BT-/Landtagsdrucksache, Fraktionspapier, Ministeriumsvermerk, kurze Sprechfassung, DOCX, PDF, XML? | Ergebnis direkt verwendbar machen. |

### 3. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Startbahn:** Bund, Bundestag, Land, Landtag oder sonstiger Normgeber festlegen.
2. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
3. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was politisch gewollt ist, was rechtlich streitig ist und was fehlt.
4. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Entwurf, Änderungsantrag, parlamentarischer Antrag, Kabinettsmappe, Synopse, Aktenextraktion, Red Team oder Rendern.
5. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
6. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
7. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, formaler Absender, nächster Handlungsschritt.

### 4. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.
- Bei parlamentarischen Vorhaben immer trennen: Wer liefert fachlich zu, wer ist formaler Initiator, wer unterzeichnet, welches Parlament und welche Geschäftsordnung gelten.
- Bei Ländern immer das Bundesland abfragen und die jeweilige Landesverfassung, Geschäftsordnung der Landesregierung, Geschäftsordnung des Landtags und Verkündungsregeln als offene Prüfposten führen.
- Bei Oppositionsvorhaben nicht mit Kabinetts-, Ressort- oder NKR-Pflichten arbeiten, als wären sie formale Einreichungsvoraussetzungen. Stattdessen parlamentarische Zulässigkeit, Kompetenz, Haushaltswirkung, Verfassungsrecht, EU-Recht und politische Angreifbarkeit prüfen.

### 5. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Startbahn: [Bundesressort / Bundestag / Landesministerium / Landtag / sonstiger Normgeber]
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

### 6. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `begruendung-allgemein-und-besonders` | Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil… |
| `dokumente-rendern-docx-pdf` | Legistische Dokumente als DOCX oder PDF im Erscheinungsbild der Bundesregierung, des Bundestages, eines Landes oder eines Landtags rendern. Anwendungsfall fertiger Entwurf, parlamentarische Vorlage, Synopse oder Lesefassung soll lieferfähig ausgegeben werden. |
| `europarechtskonformitaet` | Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht… |
| `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik… |
| `folgenabschaetzung-nachhaltigkeit` | Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen… |
| `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Entschließungsantrag oder parlamentarischen Antrag bauen. Geeignet für Ministerialzulieferungen, Koalitionsfraktionen, Oppositionsfraktionen, Gruppen oder Abgeordnete in der erforderlichen Stärke. |
| `gesetzesentwurf-kabinett` | Kabinettsentwurf der Bundesregierung oder Landesregierung aus dem Referentenentwurf nach Ressortabstimmung erstellen. Anwendungsfall Ressortabstimmung und Verbandeanhoerung sind abgeschlossen Kabinettsvorlage muss… |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73… |
| `goldplating-vermeiden` | Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten. Anwendungsfall Referentenentwurf setzt EU-Richtlinie um und muss auf ueberschiessende nationale Regelungen über den… |
| `inkrafttreten-uebergangsrecht` | Inkrafttretens- und Übergangsregelung für Gesetze und Verordnungen formulieren. Anwendungsfall Entwurf ist inhaltlich fertig Artikel Inkrafttreten und Übergangsrecht müssen noch ergaenzt werden. Standardformel… |
| `legistik-auftragsaufnahme` | Legistischen Auftrag strukturiert aufnehmen: Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Adressaten, Eingriffstiefe, Dringlichkeit, Entwurfstyp und Beteiligte klären. |
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Änderung aussieht ohne… |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Änderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten… |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten.… |
| `normhierarchie-routing` | Richtige Startbahn und Normebene bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschließungsantrag. |
| `referentenentwurf-bauen` | Vollständigen Referentenentwurf des Bundes oder Landes aufbauen, wenn ein Bundes- oder Landesministerium den Entwurf steuert. Klärt Bundesland, Ressort, GGO oder Landesvorgaben und HdR-/Landesstil. |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft… |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder… |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Änderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Änderungen schnell zu erfassen.… |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine… |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu… |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft… |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist.… |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert… |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte… |

## Worum geht es?

Die Legistik-Werkstatt ist ein Plugin für Referentinnen und Referenten in Bundesministerien und Landesministerien, für Bundestags- und Landtagsfraktionen, für Oppositionsarbeit, Ausschussarbeit, kommunale und kammerliche Normgeber, Verfassungsrechtlerinnen und Verfassungsrechtler sowie für fachlich zuliefernde Verbände. Sie hilft, Gesetzesentwürfe, Änderungsanträge, Entschließungsanträge, Rechtsverordnungen und Satzungen zu erstellen, zu prüfen und in den jeweils passenden Regierungs- oder Parlamentsprozess einzubringen.

Das Plugin deckt alle Phasen des Gesetzgebungsverfahrens ab: von der Auftragsaufnahme über den Referentenentwurf, die Ressortabstimmung, Verbandeanhoerungen, die Kabinettsreife, Synopsen und Lesefassungen bis zur XML-Paralleldarstellung. Es enthaelt ausserdem Quercheckmodule für Verfassungsmaessigkeit, Europarechtskonformitaet, Erfuellungsaufwand und Goldplating-Vermeidung.

## Wann brauchen Sie diese Skill?

- Ein Referat im Bundesministerium erstellt einen Referentenentwurf und braucht eine strukturierte Auftragsaufnahme mit Regelungszielen.
- Eine Bundestagsfraktion will einen Gesetzentwurf aus der Mitte des Bundestages oder einen Änderungsantrag zu einer laufenden Drucksache bauen.
- Eine Oppositionsfraktion braucht einen formal tragfähigen Antrag, Entschließungsantrag oder Alternativentwurf mit klarer Begründung und Angriffsfestigkeit.
- Ein Landesministerium oder eine Landtagsfraktion arbeitet in einem bestimmten Bundesland und muss Landesverfassung, Landes-Geschäftsordnung, Landtagsverfahren und Verkündungsregeln sauber mitführen.
- Eine Normenkontrollrats-Vorlage muss fristgerecht vorbereitet und mit einem KMU-Check versehen werden.
- Ein Ministerium will einen bestehenden Entwurf auf Verfassungsmaessigkeit und Europarechtskonformitaet prüfen.
- Eine Rechtsverordnung wird entworfen und die Verordnungsermaechtigung nach Art. 80 GG muss geprueft werden.
- Nach Inkrafttreten soll eine konsolidierte Lesefassung des geaenderten Stammgesetzes erstellt werden.

## Fachbegriffe (kurz erklaert)

- **HdR** — Handbuch der Rechtsfoermlichkeit; Leitfaden des Bundesjustizministeriums für die Formulierung von Rechtstexten.
- **GGO** — Gemeinsame Geschäftsordnung der Bundesministerien; regelt Verfahren und Fristen für die Ressortabstimmung.
- **NKR** — Nationaler Normenkontrollrat; unabhaengiges Gremium, das Erfuellungsaufwand und buerokratische Belastungen prüft.
- **Gesetzentwurf aus der Mitte** — Parlamentarische Gesetzesinitiative, die nicht von der Bundesregierung oder Landesregierung, sondern aus dem Parlament kommt; im Bund typischerweise durch eine Fraktion oder Abgeordnete in der erforderlichen Stärke.
- **Formulierungshilfe** — Fachlicher Zuliefertext, häufig aus einem Ministerium, der formal als parlamentarische Vorlage, Änderungsantrag oder Ausschussfassung weiterverwendet werden kann; formaler Initiator und fachlicher Verfasser sind sauber zu trennen.
- **Goldplating** — Ueberimplementierung von EU-Richtlinien: nationale Zusatzanforderungen über das EU-Mindestmass hinaus.
- **Synopse** — Gegenueberststellung von bisherigem Recht, neuem Recht und Änderungsbefehl in einer Dreispalten-Tabelle.
- **LegalDocML** — Maschinenlesbares XML-Format für deutsche Rechtstexte; Standard des Bundesjustizministeriums.
- **Normenkartierung** — Systematische Erfassung aller durch ein Vorhaben beruehrten Normen und ihrer Änderungsbedarfe.
- **Kabinettsentwurf** — Abgestimmter Regierungsentwurf, der dem Kabinett zur Beschlussfassung vorgelegt wird.

## Rechtsgrundlagen

- Art. 70-74 GG (Gesetzgebungskompetenzen Bund und Länder)
- Art. 80 Abs. 1 GG (Verordnungsermaechtigung)
- Art. 76-78 GG (Gesetzgebungsverfahren im Bund)
- Geschäftsordnung des Deutschen Bundestages, insbesondere Vorlagen aus der Mitte des Bundestages
- Landesverfassungen, Geschäftsordnungen der Landesregierungen und Geschäftsordnungen der Landtage
- GGO (Gemeinsame Geschäftsordnung der Bundesministerien)
- Art. 288 AEUV (Wirkung von EU-Verordnungen und Richtlinien)
- Art. 267 AEUV (Vorabentscheidungsverfahren EuGH)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Startbahn klären: Bundesressort, Bundestag, Landesressort, Landtag oder sonstiger Normgeber.
2. Legistischen Auftrag aufnehmen und Regelungsziele klären (`legistik-auftragsaufnahme`).
3. Normhierarchie und Kompetenzgrundlage bestimmen (`normhierarchie-routing`, `gesetzgebungskompetenz-pruefen`).
4. Geeigneten Entwurfstyp auswaehlen: Referentenentwurf, Kabinettsentwurf, Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Rechtsverordnung oder Satzung.
5. Quercheck-Module nutzen: Verfassungsmaessigkeit, Europarecht, Goldplating, Erfuellungsaufwand, Rechtsförmlichkeit und parlamentarische Zulässigkeit.
6. Ressortabstimmung, Verbändeanhörung, parlamentarische Einbringung oder Satzungsbeschluss steuern, dann zur lieferfähigen Fassung führen.

## Skill-Tour (was gibt es hier?)

- `legistik-auftragsaufnahme` — Legistischen Auftrag strukturiert aufnehmen und in Regelungsziele umwandeln.
- `normhierarchie-routing` — Richtige Startbahn und Normebene bestimmen: Regierung, Parlament, Gesetz, Verordnung, Satzung oder Antrag.
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz nach Art. 70-74 GG prüfen bevor Entwurf aufgesetzt wird.
- `satzungskompetenz-pruefen` — Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen.
- `verordnungsermaechtigung-art80` — Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird.
- `referentenentwurf-bauen` — Vollstaendigen Referentenentwurf des Bundes oder Landes aufbauen.
- `gesetzesentwurf-kabinett` — Kabinettsentwurf nach Ressortabstimmung aus dem Referentenentwurf erstellen.
- `formulierungshilfe-bauen` — Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Entschließungsantrag oder Antrag für Bundestag und Landtage aufbauen.
- `begruendung-allgemein-und-besonders` — Zweiteilige Begruendung zu Gesetzesentwurf oder Verordnung (Allgemeiner Teil, Besonderer Teil) verfassen.
- `verfassungsmaessigkeit-quercheck` — Querschnittspruefung Verfassungsmaessigkeit eines Gesetzesentwurfs oder einer Verordnung.
- `europarechtskonformitaet` — Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen.
- `goldplating-vermeiden` — Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten.
- `folgenabschaetzung-erfuellungsaufwand` — Erfuellungsaufwand für Buerger, Wirtschaft und Verwaltung ermitteln und darstellen.
- `folgenabschaetzung-nachhaltigkeit` — Weitere Folgen und Nachhaltigkeitspruefung für Gesetzesentwurf erstellen.
- `normenkontrollrat-kmu-check` — Vorlage an den NKR vorbereiten und KMU-Check durchfuehren.
- `normenkartierung` — Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Änderungsmatrix aufbauen.
- `terminologie-konsistenz` — Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen.
- `zirkelschluss-pruefen` — Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren.
- `inkrafttreten-uebergangsrecht` — Inkrafttretens- und Uebergangsregelungen für Gesetze und Verordnungen formulieren.
- `verbaendeanhoerung-ressortabstimmung` — Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten.
- `synopse-erstellen` — Synopse als Dreispalten-Tabelle (bisheriges Recht, neues Recht, Änderungsbefehl) erstellen.
- `lesefassung-konsolidiert` — Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen.
- `xml-paralleldarstellung` — Maschinenlesbare Paralleldarstellung in LegalDocML.de oder eNorm-XML erstellen.
- `dokumente-rendern-docx-pdf` — Legistische Dokumente als DOCX oder PDF im offiziellen HdR-Layout rendern.
- `schulung-legistik` — Trainerleitfaden für Legistik-Fortbildungen mit der Arbeitsakte erstellen.

## Worauf besonders achten

- Kompetenzgrundlage zuerst: Ohne geklarte Gesetzgebungskompetenz nach Art. 70 ff. GG darf kein Entwurf aufgesetzt werden.
- Startbahn sauber halten: Ministerielle Fachzulieferung, formaler parlamentarischer Initiator und politischer Auftraggeber dürfen nicht vermischt werden.
- Landesmodus ernst nehmen: Ohne Bundesland keine verlässliche Aussage zu Landesverfassung, Landtagsgeschäftsordnung, Kabinettsverfahren und Verkündung.
- Goldplating ist politisch und juristisch heikel: Nationale Mehrbelastungen über EU-Mindestanforderungen hinaus müssen explizit begruendet werden.
- NKR-Fristen sind verbindlich: Vorlage muss mit vollstaendigen Erfuellungsaufwands-Angaben rechtzeitig erfolgen.
- Terminologie-Konsistenz ist elementar: Verschiedene Begriffe für dasselbe Konzept können zu Auslegungsstreitigkeiten fuehren.
- Uebergangsrecht nicht vergessen: Altfallregelungen und Bestandsschutz sichern Rechtsicherheit und vermeiden Verfassungsruegen.

## Typische Fehler

- Referentenentwurf ohne Verfassungsmaessigkeits-Check: Entwurf wird in der Ressortabstimmung oder im Parlament wegen Grundrechtsverletzung zurueckgewiesen.
- Bundestags- oder Landtagsinitiative ohne klaren formalen Initiator: Der Text ist fachlich brauchbar, aber nicht einreichungsfähig.
- Landesentwurf nach Bundes-Schablone: Landeszuständigkeiten, Zitierregeln, Verkündungsblatt oder Landtagsformat werden falsch.
- Verordnungsermaechtigung zu unbestimmt: Art. 80 Abs. 1 GG verlangt Inhalt, Zweck und Ausmass — Blankoermaechtigung ist nichtig.
- Goldplating unerkannt: Nationale Umsetzung geht über die Richtlinienpflichten hinaus, ohne dass dies im Entwurf kenntlich gemacht wird.
- Synopse fehlt: Ressortabstimmung und parlamentarische Beratung werden durch fehlende Gegenueberststellung ernsthaft erschwert.
- Inkrafttreten ohne Uebergangsrecht: Adressaten können sich nicht rechtzeitig auf neue Pflichten einstellen.

## Quellen und Aktualitaet

- Stand: 05/2026
- GG (Grundgesetz) in der zum Stand-Datum geltenden Fassung
- GGO (Gemeinsame Geschäftsordnung der Bundesministerien) in der geltenden Fassung
- HdR (Handbuch der Rechtsfoermlichkeit) 3. Auflage des Bundesjustizministeriums
- Geschäftsordnung des Deutschen Bundestages und einschlägige Landtags-Geschäftsordnungen jeweils aktuell prüfen
