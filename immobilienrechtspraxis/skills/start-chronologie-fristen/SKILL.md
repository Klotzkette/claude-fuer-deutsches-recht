---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Immobilienrechtspraxis-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Immobilienrechtspraxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Immobilienrechtspraxis — Allgemein

## Arbeitsbereich

Einstieg, Schnelltriage und Fallrouting im Immobilienrechtspraxis-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Immobilienrechtspraxis**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Werkzeuge für immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz; Vertragsprüfung gegen Playbook; Grundbuchanalyse; Sachverhaltsermittlung; Mieteranfragen mit BGH-Verankerung; Case Management; projektbasierte Arbeitsweise mit AVV-Prüfung.

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
| `case-management` | Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output:… |
| `grundbuchanalyse` | Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Prüfraster: Abteilung I bis III, Widersprueche, Rangverhältnisse,… |
| `mieteranfragen-bearbeitung` | Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kündigung. Normen: §§ 535 536 556 573 BGB, WEG. Prüfraster: Anfragetyp, Rechtsgrundlage, Fristen, Handlungspflichten. Output:… |
| `projekt-arbeitsweise` | Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan… |
| `sachverhaltsermittlung` | Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog.… |
| `vertragserstellung-musterbasiert` | Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis.… |
| `vertragspruefung-playbook` | Immobilienrechtliche Vertraege nach standardisiertem Playbook prüfen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Prüfraster: Playbook-Checkliste, Risikoklauseln, Notar- und… |

## Worum geht es?

Das Plugin unterstuetzt immobilienrechtliche Rechtsabteilungen bei der taeglich anfallenden Vertragsarbeit, der Grundbuch- und Sachverhaltsanalyse sowie der Verwaltung von Miet- und WEG-Mandaten. Es verbindet musterbasierte Vertragserstellung mit einem strukturierten Pruefungs-Playbook und integriert den gesetzlichen Rahmen aus BGB, WEG, GBO und GrEStG.

Zielgruppe sind Unternehmensjuristen und Rechtsanwaelte, die Immobilienprojekte mit mehreren Beteiligten und langer Laufzeit koordinieren muessen. Das Plugin setzt auf eine projektartige Arbeitsweise, die Fristen, Dokumente und Beteiligte in einer Gesamtschau haelt.

## Wann brauchen Sie diese Skill?

- Sie starten ein neues Immobilienrechtsmandat und muessen Eigentumsverhaeltnisse, Grundbuchbelastungen und Vertragshistorie systematisch erfassen.
- Sie wollen einen Kaufvertrag, Mietvertrag oder WEG-Beschluss auf Musterbasis erstellen oder nach einem Playbook auf Risiken pruefen.
- Ein Mieter oder WEG-Eigentumer stellt eine Anfrage zu Instandsetzung, Betriebskosten oder Kuendigung.
- Sie muessen mehrere Beteiligte, Fristen und Meilensteine in einem komplexen Immobilienprojekt steuern.
- Sie benoetigen einen Sachverhalts-Ermittlungsbericht als Grundlage fuer die rechtliche Bewertung.

## Fachbegriffe (kurz erklaert)

- **Grundbuch** — Oeffentliches Register der Eigentumsverhaeltnisse und dinglichen Belastungen eines Grundstuecks; gefuehrt nach der Grundbuchordnung (GBO).
- **Grundschuld** — Dingliches Sicherungsrecht am Grundstueck nach §§ 1191 ff. BGB; haufig Sicherungsmittel fuer Bankdarlehen.
- **WEG** — Wohnungseigentumsgesetz; regelt die Gemeinschaft der Wohnungseigentuemer, Beschlusse und Verwaltung.
- **Dienstbarkeit** — Beschraenkung des Eigentuemers zugunsten Dritter (z. B. Wegerecht, Niesbrauch) nach §§ 1018 ff. BGB.
- **GrEStG** — Grunderwerbsteuergesetz; regelt Steuertatbestand beim Eigentumsubergang.
- **Notarerfordernis** — Formpflicht: Kaufvertraege ueber Grundstuecke beduerften nach § 311b BGB notarieller Beurkundung.
- **Playbook** — Standardisierter Pruefkatalog der Rechtsabteilung mit Risikoklauseln und Ampelbewertung.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; relevant beim KI-Einsatz in der Mandatsbearbeitung.

## Rechtsgrundlagen

- §§ 433 ff. BGB — Kaufvertrag
- §§ 535 ff. BGB — Mietrecht
- §§ 873 ff. BGB — Eigentumsuebertragung und dingliche Rechte
- §§ 1018 ff. BGB — Grunddienstbarkeiten
- §§ 1105 ff. BGB — Reallast
- §§ 1191 ff. BGB — Grundschuld
- WEG — Wohnungseigentumsgesetz
- GBO — Grundbuchordnung
- GrEStG — Grunderwerbsteuergesetz

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren (Kaeufer, Verkaeufer, Vermieter, WEG-Verwalter, Rechtsabteilung).
2. Phase des Mandats bestimmen (Sachverhaltsaufnahme, Vertragserstellung, Vertragspruefung, laufende Verwaltung, Streitfall).
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Fristen pruefen (Kaufvertragsfrist, Kuendigungsfristen, GrESt-Zahlungsfristen).
5. Bei Projekten mit mehreren Beteiligten: Projektplan anlegen und Case Management aktivieren.

## Skill-Tour (was gibt es hier?)

- `case-management` — Fallmanagement fuer Immobilienrechtsmandate: Verfahrensstand, Fristen und Dokumente im Ueberblick.
- `grundbuchanalyse` — Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten und Rangverhaeltnisse.
- `mieteranfragen-bearbeitung` — Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kuendigung.
- `projekt-arbeitsweise` — Projektmethodik fuer Immobilienrechtsprojekte mit mehreren Beteiligten, Meilensteinen und Dokumentenstruktur.
- `sachverhaltsermittlung` — Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhaeltnisse, Vertragshistorie, Beweismittel.
- `vertragserstellung-musterbasiert` — Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss.
- `vertragspruefung-playbook` — Immobilienrechtliche Vertraege nach standardisiertem Playbook pruefen: Kaufvertrag, Grundschuld, WEG.

## Worauf besonders achten

- **Formzwang**: Kaufvertraege ueber Grundstuecke beduerften notarieller Beurkundung (§ 311b BGB); Formmangel fuehrt zu Nichtigkeit des gesamten Vertrages.
- **Grundbuchstand vor Vertragsschluss pruefen**: Nicht eingetragene Belastungen und Widersprueche koennen Eigentumsuebergang erschweren.
- **WEG-Beschluesse**: Nicht ordnungsgemaesse Einberufung oder fehlende Mehrheiten fuehren zur Anfechtbarkeit; Fristen nach § 45 WEG beachten.
- **GrEStG-Grunderwerbsteuer**: Zahlungsfrist nach § 15 GrEStG; Unbedenklichkeitsbescheinigung Voraussetzung fuer Grundbucheintragung.
- **AVV beim KI-Einsatz**: Mandatsdaten duerfen nur in KI-Systeme eingegeben werden, wenn ein datenschutzkonformer AVV vorliegt.

## Typische Fehler

- Mustervertrag ohne Anpassung an Sachverhalt verwenden: fehlende Sondervereinbarungen zu Moebeln, Inventar oder Baumangeln fuehren spaeter zu Streit.
- Grundbuch-Abt. III (Grundschulden) nicht vollstaendig pruefen: ueberraschende Belastungen koernen Kaufpreis und Finanzierung gefaehrden.
- Kuendigungsfristen nach § 573c BGB verwechseln mit Kuendigungsgruenden nach § 573 BGB.
- WEG-Beschluesse ohne Protokollpruefung uebernehmen: Fehler in der Abstimmung sind nicht immer offensichtlich.
- Sachverhaltsermittlung und rechtliche Bewertung vermischen: Tatsachen erst vollstaendig erfassen, dann bewerten.

## Querverweise

- `kanzlei-allgemein` — Allgemeines Kanzlei-Workflow-Plugin fuer Fristen, Schriftsaetze und Mandatsmanagement.
- `zwangsverwaltung-zvg` — Bei Zwangsverwaltung und Zwangsversteigerung von Immobilien.
- `aktenauszug-gerichtsverfahren` — Fuer schnelle Einarbeitung in laufende Immobilienprozesse.
- `insolvenzverwaltung` — Wenn Immobilien Teil einer Insolvenzmasse sind.
- `selbstvertreter-amtsgericht` — Wenn Mieter ohne Anwalt im Mietprozess vor dem Amtsgericht auftreten.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- BGH-Rechtsprechung zu §§ 535 ff. BGB (Mietrecht) und WEG laufend beachten

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
