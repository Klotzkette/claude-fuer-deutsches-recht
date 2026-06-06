---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Patentrecherche-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Patentrecherche: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Patentrecherche — Allgemein

## Arbeitsbereich

Einstieg, Schnelltriage und Fallrouting im Patentrecherche-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Patentrecherche**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Patentrecherche für Patentanwaelte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit § 3 PatG Art. 54 EPUe erfinderische Tätigkeit § 4 PatG Art. 56 EPUe Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht.

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
| `agentische-datenbank-recherche` | Agentische Patentdatenbank-Recherche: Suchauftrag in natuerlicher Sprache mit Erfindungsmaterial (Anspruchsentwurf, Beschreibung, Skizzen) wird automatisch in Suchstrings für Espacenet, Google Patents, DPMAregister,… |
| `erfinderische-taetigkeit-pruefen` | Prüft erfinderische Tätigkeit nach § 4 PatG und Art. 56 EPUe mit dem Problem-Solution-Approach der EPA-Beschwerdekammern. Drei Stufen: (1) Bestimmung des naechstliegenden Stands der Technik (closest prior art) anhand… |
| `freedom-to-operate-recherche` | Freedom-to-Operate-Recherche (FTO) vor Markteintritt eines konkreten Produkts oder Verfahrens der Mandantin. Sucht **in Kraft befindliche** Patente und Gebrauchsmuster Dritter im Zielmarkt deren Schutzbereich nach § 14… |
| `klassifikation-cpc-ipc` | CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche muessen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC… |
| `neuheit-pruefen` | Prüft Neuheit nach § 3 PatG und Art. 54 EPUe. Methodisches Schema: ein Anspruch wird in seine Merkmale zerlegt und Merkmal-fuer-Merkmal gegen genau eine Entgegenhaltung verglichen. Neuheitsschaedlich ist nur die… |
| `patentfamilien-analyse` | Patentfamilien-Analyse über INPADOC und Espacenet-Family-View. Sammelt zu einem konkreten Treffer alle Familienmitglieder weltweit DE EP US JP CN KR WO und sonstige Aemter mit gleichem Prioritaetstag. Liefert eine… |
| `patentrecherche-kaltstart-interview` | Kaltstart-Interview für das Patentrecherche-Plugin. Stellt fest wer recherchiert (Patentanwaeltin Patentanwalt Patentassessor Patentingenieur Recherchekraft) welche Kanzlei und welche Technikgebiete (Mechanik… |
| `pruefungsbescheid-vorbereiten` | Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45 PatG oder des EPA nach Art. 94 EPUe systematisch vor. Liest den Bescheid und die zitierten Entgegenhaltungen ein. Strukturiert pro Beanstandung: Beanstandung… |
| `recherchebericht-erstellen` | Formaler Recherchebericht für den Mandanten oder die Akte. Bringt Auftrag Methodik durchsuchte Datenbanken verwendete Suchstrings Klassen Schlagworte Zeitraum Trefferzahlen Treffertabelle und Bewertungen aus Skills… |
| `rechtsstand-pruefen` | Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR.… |
| `rueckfragen-mandant` | Generiert Rückfragen an den Mandanten wenn das vorgelegte Material für eine sinnvolle Recherche nicht ausreicht oder Abgrenzungsfragen offen sind. Pflichtfragen: Was ist der wesentliche Lösungsbeitrag der Erfindung… |
| `stand-der-technik-recherche` | Recherche Stand der Technik vor eigener Patentanmeldung. Identifiziert anhand des Erfindungsmaterials und der ermittelten CPC-IPC-Klassen die wichtigsten Veröffentlichungen die der Anmeldetag-Reife der… |
| `ueberwachung-konkurrenten` | Laufende Überwachung neuer Patentanmeldungen von Konkurrenten der Mandantin. Definiert Watch-Profile pro Mandant mit Anmelder-Namen (inklusive Konzern-Toechter und ehemaliger Schreibweisen), CPC-IPC-Klassen,… |

## Worum geht es?

Das Plugin unterstuetzt Patentanwaelte, Patentassistenten und technische Berater bei der systematischen Patentrecherche in nationalen und internationalen Datenbanken. Es deckt die gesamte Bandbreite von der Neuheitspruefung vor Anmeldung ueber die Pruefung erfinderischer Taetigkeit bis zur Freedom-to-Operate-Recherche (FTO) ab.

Das Plugin arbeitet agentisch: Es steuert Datenbankabfragen in Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO und USPTO nach den CPC/IPC-Klassifikationen und dem Problem-Solution-Approach der EPA-Beschwerdekammern. Ergebnisse werden in formalen Rechercheberichten und Anmelde-Antwort-Paketen dokumentiert.

## Wann brauchen Sie diese Skill?

- Mandant hat neue Erfindung und will wissen, ob sie neuheitlich und erfinderisch genueg fuer eine Patentanmeldung ist.
- Unternehmen plant Markteintritt mit neuem Produkt und braucht FTO-Recherche zu aktiven Schutzrechten von Wettbewerbern.
- Patentanwalt erhaelt Pruefungsbescheid des DPMA oder EPA und muss Antwort mit Stand-der-Technik-Analyse vorbereiten.
- Mandant will Patentportfolio eines Konkurrenten laufend beobachten (Ueberwachung Neuanmeldungen).
- Rechtsstandpruefung eines Patents: Ist das Schutzrecht noch in Kraft? Sind Jahresgebuehren bezahlt?

## Fachbegriffe (kurz erklaert)

- **Neuheit (§ 3 PatG / Art. 54 EPUe)** — Eine Erfindung gilt als neu, wenn sie nicht zum Stand der Technik gehoert; jeder Voroffenbarung (weltweit, zeitlos) schadet.
- **Erfinderische Taetigkeit (§ 4 PatG / Art. 56 EPUe)** — Erfindung darf sich fuer den Fachmann nicht in naheliegender Weise aus dem Stand der Technik ergeben.
- **Problem-Solution-Approach (PSA)** — Standardmethode der EPA-Beschwerdekammern: naechster Stand der Technik, objektive technische Aufgabe, naheliegend?
- **CPC / IPC** — Cooperative Patent Classification / International Patent Classification; hierarchische Klassifikationssysteme fuer Patentdokumente.
- **Freedom to Operate (FTO)** — Pruefung, ob ein Produkt oder Verfahren in einen Anspruch eines Drittpatents faellt und damit Verletzungsrisiko besteht.
- **INPADOC** — Internationaler Patenddokumentationsdienst; liefert Familienzusammenhaenge und Rechtsstanddaten ueber EPO.
- **Patentfamilie** — Alle nationalen und regionalen Schutzrechte, die auf dieselbe Prioritaetsanmeldung zurueckgehen.

## Rechtsgrundlagen

- §§ 1-5 PatG — Patentierbarkeit (Neuheit, erfinderische Taetigkeit, gewerbliche Anwendbarkeit)
- § 3 PatG — Neuheit
- § 4 PatG — Erfinderische Taetigkeit
- §§ 34 ff. PatG — Patentanmeldung beim DPMA
- §§ 44 45 PatG — Pruefungsverfahren DPMA
- Art. 52-57 EPUe — Patentierbarkeit nach Europaeischem Patentrecht
- Art. 94 EPUe — Pruefungsverfahren EPA

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Neuanmeldung, FTO, Pruefungsbescheid-Antwort oder Konkurrenzueberwachung?
2. Erfindungsmaterial aufnehmen: Anspruchsentwurf, Beschreibung oder technisches Dokument hochladen.
3. Klassifikation bestimmen: CPC/IPC-Klassen fuer gezielte Datenbanksuche festlegen.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Recherchebericht erstellen und Ergebnisse dem Mandanten kommunizieren.

## Skill-Tour (was gibt es hier?)

- `patentrecherche-kaltstart-interview` — Erstkontakt und Aufnahme der Rechercheanforderungen: Wer recherchiert, was ist das Ziel, welches Material liegt vor?
- `klassifikation-cpc-ipc` — CPC- und IPC-Klassen fuer die Datenbankrecherche bestimmen und Klassifikationsdossier erstellen.
- `agentische-datenbank-recherche` — Agentische Suche in natuerlicher Sprache ueber Espacenet, Google Patents, DEPATISnet, WIPO und USPTO.
- `stand-der-technik-recherche` — Stand der Technik vor Patentanmeldung identifizieren und bewerten.
- `neuheit-pruefen` — Neuheit nach § 3 PatG und Art. 54 EPUe systematisch pruefen; Merkmal-fuer-Merkmal-Abgleich.
- `erfinderische-taetigkeit-pruefen` — Erfinderische Taetigkeit nach § 4 PatG und Art. 56 EPUe mit Problem-Solution-Approach pruefen.
- `freedom-to-operate-recherche` — FTO-Recherche vor Markteintritt: aktive Drittpatente mit relevantem Scope identifizieren.
- `patentfamilien-analyse` — Alle Familienmitglieder eines Schutzrechts ueber INPADOC und Espacenet ermitteln.
- `rechtsstand-pruefen` — Aktuellen Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Register pruefen.
- `pruefungsbescheid-vorbereiten` — Antwort auf DPMA-Pruefungsbescheid (§ 45 PatG) oder EPA-Bescheid (Art. 94 EPUe) systematisch vorbereiten.
- `recherchebericht-erstellen` — Formalen Recherchebericht mit Methodik, Datenbanken, Suchstrategien und Ergebnissen erstellen.
- `ueberwachung-konkurrenten` — Watch-Profile fuer laufende Ueberwachung neuer Patentanmeldungen von Wettbewerbern anlegen.
- `rueckfragen-mandant` — Rueckfragen an den Mandanten generieren, wenn Erfindungsmaterial unvollstaendig oder ambivalent ist.

## Worauf besonders achten

- Neuheitsschaedlichkeit ist weltweit und zeitlich unbegrenzt: Auch 20 Jahre alte Veroeffentlichungen koennen Neuheit zerstoeren.
- FTO und Anmelderecherche sind unterschiedliche Aufgaben mit unterschiedlichem Scope; Verwechslung fuehrt zu falschen Ergebnissen.
- Pruefungsbescheide haben feste Fristen (§ 45 PatG: 4 Monate, verlaengerbar; Art. 94 EPUe: aehnlich); versaeumte Fristen fuehren zu Zurueckweisung.
- Patentfamilien-Analyse ist essenziell: Ein nationales Schutzrecht kann international wirken; nur Famille-Pruefung zeigt Gesamtscope.
- Veroeffentlichungen des Anmelders vor dem Prioritaetstag koennen neuheitsschaedlich sein (Ausnahme: 6-Monats-Schonfrist in manchen Systemen, z.B. USPTO).

## Typische Fehler

- Recherche nur in einer Datenbank: Relevante Dokumente sind oft nur in DEPATISnet oder USPTO-Datenbanken, nicht in Espacenet.
- Falschen Zeitschnitt gesetzt: FTO-Recherche erfordert nur noch in Kraft befindliche Schutzrechte; Neuheitsrecherche erfordert alle Veroeffentlichungen bis zum Anmeldetag.
- CPC-Klassifikation zu eng gewaehlt: Aehnliche Technologien in Nachbarklassen werden uebersehen.
- Pruefungsbescheid-Argumente zu schwach: Ohne detaillierten Merkmals-Abgleich (Feature-by-Feature-Analysis) akzeptiert EPA keine summarischen Stellungnahmen.
- Rechtsstand nicht gecheckt: FTO-Recherche gegen abgelaufene oder fallen lassene Patente liefert unnoetigen Aufwand.

## Querverweise

- Plugin `markenrecht-fashion-luxus` — Bei Design- und Markenstreitigkeiten ergaenzt Patentrecherche Schutzrechtspruefung.
- Plugin `grosskanzlei-corporate-ma` — Bei M&A-Transaktionen ist IP-Due-Diligence (Patentportfolio des Targets) ein Kernthema.
- Plugin `umweltrecht` — Greentech-Patente koennen mit Genehmigungspflichten nach BImSchG zusammentreffen.

## Quellen und Aktualitaet

- Stand: 05/2026
- PatG und EPUe in aktuell geltender Fassung
- Espacenet, DEPATISnet, DPMAregister, USPTO, WIPO PatentScope (Stand 05/2026)

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
