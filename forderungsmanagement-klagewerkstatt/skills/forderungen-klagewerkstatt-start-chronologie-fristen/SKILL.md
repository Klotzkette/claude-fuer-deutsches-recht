---
name: forderungen-klagewerkstatt-start-chronologie-fristen
description: "Forderungen Klagewerkstatt Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Forderungen Klagewerkstatt Start Chronologie Fristen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Forderungen Klagewerkstatt Start Chronologie Fristen** im Plugin Forderungsmanagement / Klagewerkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `forderungsmanagement-klagewerkstatt-allgemein` | Einstieg, Schnelltriage und Fallrouting im Forderungsmanagement Klagewerkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin forderungsmanagement-klagewerkstatt: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin forderungsmanagement-klagewerkstatt: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsweg

Im Plugin Forderungsmanagement / Klagewerkstatt gilt für **Forderungen Klagewerkstatt Start Chronologie Fristen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `forderungsmanagement-klagewerkstatt-allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Forderungsmanagement Klagewerkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Forderungsmanagement-Klagewerkstatt — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Forderungsmanagement Klagewerkstatt**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

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
| `inkasso-zahlungsklage-ersteller` | Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten § 288… |
| `klage-aus-eigenem-skill` | Kanzlei hat hauseigenes Klage-Plugin (klagewerkstatt-kanzlei) installiert und will damit Klagen aus eigenem Sachverhalt erstellen. Laufzeit-Variante Klagewerkstatt. Prüfraster: Sachverhalt Beklagtenadresse… |
| `klagevorlage-aus-eigenen-mustern` | Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage… |

## Worum geht es?

Das Plugin begleitet Glaeubiger und Anwaelte vom Forderungsmanagement bis zur gerichtlichen Titulierung. Im Mittelpunkt steht der sogenannte Gatekeeper: Nur Forderungen, die klar beziffert, faellig und belegt sind, werden zur Zahlungsklage freigegeben. So werden aussichtslose Klagen vermieden, die Kosten verursachen ohne Erfolgsaussicht.

Das Plugin unterstuetzt zudem den Aufbau kanzleieigener Klagemuster und ermoeglicht die Integration mit vorhandenen Kanzlei-Klagewerkstatt-Plugins. Zielgruppe sind Anwaelte, Inkassounternehmen und Unternehmensjuristen im Forderungseinzug.

## Wann brauchen Sie diese Skill?

- Glaeubigerseite hat offene, unbezahlte Forderung und muss entscheiden, ob und wie sie klagen soll.
- Kanzlei will den Mahnvorlauf dokumentieren und pruefen, ob Verzug wirksam eingetreten ist.
- Mandant fragt, ob Amtsgericht oder Landgericht zustaendig ist und ob Mahnbescheid oder Klage sinnvoller ist.
- Kanzlei will hauseigene Klagemuster fuer wiederkehrende Forderungstypen strukturieren und wiederverwenden.
- Forderung liegt im Grenzbereich: Verpflichtungseinrede oder Gegenforderung des Schuldners muss vorab geprueft werden.

## Fachbegriffe (kurz erklaert)

- **Gatekeeper** — Vorabpruefung, ob Forderung klar, faellig und belegt ist, bevor Klageerstellung ausgeloest wird.
- **Verzug (§ 286 BGB)** — Schuldner leistet trotz Faelligkeit und Mahnung nicht; Voraussetzung fuer Verzugszinsen und Schadensersatz.
- **Mahnbescheid (§§ 688 ff. ZPO)** — Vereinfachtes gerichtliches Verfahren zur Titulierung unstreitiger Forderungen ohne muendliche Verhandlung.
- **Vollstreckungstitel** — Dokument, das Zwangsvollstreckung erlaubt (z.B. Urteil, Vollstreckungsbescheid, notarielle Urkunde).
- **Streitwert** — Geldwert der Forderung; entscheidet ueber Zustaendigkeit (AG bis 5.000 EUR nach altem Recht; ab 01.01.2026 AG bis 10.000 EUR, § 23 GVG) und Gerichtskosten.
- **Inkasso-Zahlungsklage** — Auf Geldzahlung gerichtete Klage mit standardisierten Pflichtbestandteilen (§§ 253 253 ZPO).

## Rechtsgrundlagen

- §§ 241 280 286 288 BGB — Leistungspflicht, Schadensersatz, Verzug, Verzugszinsen
- §§ 688 ff. ZPO — Mahnverfahren
- §§ 253 313 ZPO — Klageschrift, Urteilsbestandteile
- § 23 GVG — Sachliche Zustaendigkeit Amtsgericht
- § 71 GVG — Sachliche Zustaendigkeit Landgericht

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Forderung pruefen: Ist sie klar beziffert, faellig und belegt (Vertrag, Rechnung, Mahnung)?
2. Zustaendigkeit bestimmen: AG oder LG nach Streitwert; ggf. besonderer Gerichtsstand.
3. Mahnvorlauf dokumentieren: Liegt wirksame Mahnung vor? Ist Verzug eingetreten?
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Klagemuster pruefen oder anpassen: Eigene Kanzleimuster einbinden oder Standardmuster verwenden.

## Skill-Tour (was gibt es hier?)

- `inkasso-zahlungsklage-ersteller` — Erstellt eine vollstaendige Zahlungsklage fuer belegte und faellige Forderungen; Gatekeeper-Pruefung vor Klageerstellung.
- `klage-aus-eigenem-skill` — Verbindet Plugin mit kanzleiinternem Klagewerkstatt-Plugin (klagewerkstatt-kanzlei) fuer mandatsspezifische Klagen aus eigenem Sachverhalt.
- `klagevorlage-aus-eigenen-mustern` — Destilliert kanzleieigene Klagemuster einmalig in ein wiederverwendbares Plugin-Format.

## Worauf besonders achten

- Verzug muss wirksam begruendet sein: Mahnung nach § 286 BGB oder kalendarische Faelligkeit; fehlende Mahnung macht Verzugszinsen unbegruendet.
- Streitwertgrenzen beachten: Seit 01.01.2026 ist das AG bis 10.000 EUR sachlich zustaendig (§ 23 Nr. 1 GVG, Justizstandort-Staerkungsgesetz).
- Gegenansprueche und Einreden des Schuldners vor Klageerhebung ermitteln; unangemeldete Aufrechnung kann Klage entwerten.
- Im Mahnverfahren (§ 688 ZPO) sind von der Hauptforderung abhaengige Nebenforderungen separat zu beziffern.
- Klagemuster aus Kanzlei-Datenbanken muessen auf den konkreten Sachverhalt angepasst werden; blindes Uebernehmen fuehrt zu unzulaessigen oder unschluessigen Antraegen.

## Typische Fehler

- Klage ohne vorherige Mahnung: Ohne wirksame Mahnung kann keine Zahlungsklage auf Verzugszinsen gestellt werden.
- Streitwert falsch angegeben: Neben- und Zinsforderungen koennen Streitwert in eine andere Gerichtsstandskategorie heben.
- Forderung nicht hinreichend substantiiert: Rechnung oder Vertrag fehlt als Anlage; Klage wird unschluessig.
- Verpflichtungseinrede uebersehen: Schuldner hat eigene Gegenansprueche, die aufgerechnet werden koennen.
- Zu spaet zum Massnahmenpaket: Nach Abschluss Mahnverfahren laufen Widerspruchsfristen; versaeumte Folgeschritte fuehren zu Fristversaeumnissen.

## Querverweise

- Plugin `zwangsvollstreckung` — Sobald Titel vorhanden, Vollstreckungsschritte einleiten.
- Plugin `selbstvertreter-amtsgericht` — Klaeger ohne Anwalt; Prozessbegleitung vor dem AG.
- Plugin `grosskanzlei-corporate-ma` — Bei hohen B2B-Forderungen ggf. Konzernhaftung oder Distressed-Aspekte pruefen.

## Quellen und Aktualitaet

- Stand: 05/2026
- § 23 Nr. 1 GVG in der Fassung des Gesetzes zur Aenderung des Zustaendigkeitsstreitwerts der Amtsgerichte (BGBl. 2025 I Nr. 318 vom 11.12.2025): Amtsgerichts-Streitwertgrenze 10.000 EUR ab 01.01.2026; § 511 Abs. 2 ZPO Berufungssumme 1.000 EUR; § 47 EGZPO Uebergangsvorschrift.
- Basiszinssatz § 247 BGB zum 01.01.2026: 1,27 Prozent (Bundesbank-Bekanntmachung); B2C-Verzugszins 6,27 Prozent, B2B-Verzugszins 10,27 Prozent. Quelle: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- BGB und ZPO in aktuell geltender Fassung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin forderungsmanagement-klagewerkstatt: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieses Modul bearbeitet: Chronologie und Belegmatrix im Plugin forderungsmanagement-klagewerkstatt: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin forderungsmanagement-klagewerkstatt: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin forderungsmanagement-klagewerkstatt: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
