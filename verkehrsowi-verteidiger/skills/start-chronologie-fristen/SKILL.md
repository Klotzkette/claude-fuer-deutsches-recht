---
name: start-chronologie-fristen
description: "Für VerkehrsOWi-Verteidiger — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
---

# VerkehrsOWi-Verteidiger — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verkehrsowi Verteidiger**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

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
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
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

Dieses Plugin begleitet Verkehrs-Ordnungswidrigkeitsmandate von der ersten Anhörung bis zur Rechtsbeschwerde. Es richtet sich an Rechtsanwaelte, die Mandanten bei Bussgeldbescheiden, Fahrverboten, Punkteeintragungen und Verfahren vor dem Amtsgericht vertreten. Abgedeckt werden Geschwindigkeitsmessungen, Rotlicht-OWi, Abstandsverfahren, Handyverstaesse, Alkohol und Drogen am Steuer, Fahreridentifizierung sowie die Beweisverwertung standardisierter Messverfahren.

Das Plugin folgt dem Verfahrensablauf: Anhörung → Bussgeldbescheid → Einspruch → Akteneinsicht/Messakte → Hauptverhandlung → ggf. Rechtsbeschwerde. Jede Phase hat eigene Fristen und Verteidigungsstrategien.

## Wann brauchen Sie diese Skill?

- Mandant erhaelt Anhörungsbogen oder Bussgeldbescheid wegen Geschwindigkeitsueberschreitung und braucht sofortige Beratung zu Einspruchsfrist und Strategie.
- Mandant ist auf den Fuehrerschein beruflich angewiesen und soll Fahrverbot erhalten — Haertefall-Argumentation prüfen.
- Anwalt hat Akteneinsicht beantragt und will Messakte auf Verfahrensfehler untersuchen.
- Mandant bestreitet Fahrereigenschaft — Fahreridentifizierungsstrategie entwickeln.
- OWi-Urteil des Amtsgerichts ist unbefriedigend und Rechtsbeschwerde zum OLG wird erwaogen.

## Fachbegriffe (kurz erklaert)

- **OWiG** — Gesetz über Ordnungswidrigkeiten; Rahmengesetz für alle Ordnungswidrigkeitsverfahren einschliesslich VerkehrsOWi.
- **StVG** — Strassenverkehrsgesetz; § 24 StVG Grundnorm für Verkehrsordnungswidrigkeiten, § 25 StVG Fahrverbot.
- **FAER** — Fahreignungsregister; Punkteregister in Flensburg beim Kraftfahrt-Bundesamt.
- **Messakte** — Vollstaendige Unterlagen zum Messvorgang: Eichschein, Rohmessdaten, Geraetefoto, Aufstellprotokoll.
- **Standardisiertes Messverfahren** — Prüfstandsgerechtes Verfahren mit amtlich anerkanntem Messgeraet; Gerichte dürfen auf Beweiswert vertrauen, solange keine konkreten Fehlerhinweise vorliegen.
- **Verfolgungsverjaehrung** — Nach §§ 26 StVG und 31 ff. OWiG: Verjaeht die Tat, kann kein Bussgeld mehr verhaengt werden.
- **Rechtsbeschwerde** — Rechtsmittel nach § 79 OWiG zum Oberlandesgericht gegen Urteil des Amtsgerichts im OWi-Verfahren.
- **Haertefall** — Ausnahme vom Fahrverbot nach § 25 StVG, wenn unverhieltnisgemäßige berufliche Folgen drohen.

## Rechtsgrundlagen

- § 24 StVG (Ordnungswidrigkeiten im Strassenverkehr)
- § 25 StVG (Fahrverbot)
- §§ 26 StVG (Verfolgungsverjaehrung)
- §§ 24a StVG (Alkohol- und Drogenfahrten)
- §§ 67 ff. OWiG (Einspruch gegen Bussgeldbescheid)
- § 79 OWiG (Rechtsbeschwerde zum OLG)
- §§ 62-66 OWiG (Akteneinsicht im OWi-Verfahren)
- BKatV (Bussgeldkatalogverordnung mit Regelbuessgeldern und Fahrverboten)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Aktenanlage und Mandat aufnehmen: Tatvorwurf, Verfahrensstadium, Fristen erfassen (`verkehrsowi-aktenanlage`).
2. Einspruchsfrist prüfen: Zwei Wochen ab Zustellung des Bussgeldbescheids — Fristwahrung hat Vorrang (`verkehrsowi-fristen-einspruch`).
3. Akteneinsicht und Messakte beantragen und auswerten (`verkehrsowi-akteneinsicht-messakte`).
4. Verteidigungsstrategie festlegen: Messverfahren angreifen, Fahreridentifizierung, Haertefall?
5. Quality-Gate vor Einspruch und vor Hauptverhandlung durchlaufen (`verkehrsowi-quality-gate`).

## Skill-Tour (was gibt es hier?)

- `verkehrsowi-kommandocenter` — Zentrales Steuerungsmodul: schnelle Orientierung für jedes OWi-Mandat vom Intake bis zur Strategie.
- `verkehrsowi-aktenanlage` — Akte im VerkehrsOWi-Mandat anlegen und strukturieren.
- `verkehrsowi-anhoerung-bussgeldbescheid` — Reaktion auf Anhörungsbogen oder Bussgeldbescheid strategisch vorbereiten.
- `verkehrsowi-fristen-einspruch` — Einspruchsfrist berechnen und wahren; Fristversaeumnis-Risiken erkennen.
- `verkehrsowi-akteneinsicht-messakte` — Vollstaendige Messakte anfordern und auf Verfahrensfehler und Eichluecken prüfen.
- `verkehrsowi-messverfahren-geschwindigkeit` — Geschwindigkeitsmessungen (TraffiStar, Riegl, ESO) auf Verwertbarkeit angreifen.
- `verkehrsowi-beweisverwertung-standardisiert` — Beweisverwertbarkeit im standardisierten Messverfahren angreifen.
- `verkehrsowi-rotlicht-abstand-handy` — Rotlicht-, Abstands- und Handy-OWi verteidigen.
- `verkehrsowi-alkohol-drogen-24a` — Alkohol- und Drogen-OWi nach § 24a StVG verteidigen (0,5-Promille, Drogennachweis).
- `verkehrsowi-fahreridentifizierung` — Fahrereigenschaft angreifen oder Fahreridentifizierung als Verteidigungsstrategieklaeren.
- `verkehrsowi-punkte-fahrverbot-flensburg` — Punkte im FAER und Fahrverbot nach § 25 StVG prüfen und Maßnahmen besprechen.
- `verkehrsowi-haertefall-fahrverbot` — Haertefall-Argumentation gegen Fahrverbot bei beruflicher Angewiesenheit entwickeln.
- `verkehrsowi-verjaehrung-zustellung` — Verfolgungsverjaehrung prüfen und Zustellungsfehler identifizieren.
- `verkehrsowi-hauptverhandlung-amtsgericht` — Hauptverhandlung am Amtsgericht vorbereiten und fuehren.
- `verkehrsowi-rechtsbeschwerde` — Rechtsbeschwerde nach § 79 OWiG zum OLG einlegen.
- `verkehrsowi-zeugen-polizei-strategie` — Zeugen-Strategie gegenueber Polizeibeamten in der Hauptverhandlung entwickeln.
- `verkehrsowi-quality-gate` — Checkliste vor Einspruch, nach Akteneingang und vor Hauptverhandlung durchlaufen.
- `verkehrsowi-mandantenkommunikation` — Mandant verstaendlich über Verfahren, Kosten und Aussichten informieren.
- `verkehrsowi-rechtsprechungsrecherche` — OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverboten recherchieren.
- `verkehrsowi-simulation-training` — Simulationstraining für OWi-Mandate: Messverfahren, Rotlicht, Handy, Alkohol, Fahreridentifizierung.

## Worauf besonders achten

- Einspruchsfrist ist zwei Wochen ab Zustellung — keine Hemmung, kein Neubeginn bei blossem Schweigen; Fristverpassen = Rechtskraft.
- Verfolgungsverjaehrung nach § 26 StVG betraegt 3 Monate ab Tatbegehung, Unterbrechung durch behordliche Maßnahmen — Zeitstrahl prüfen.
- Akteneinsicht in Messakte inklusive Rohmessdaten ist einzufordern; ohne Rohmessdaten ist effektive Verteidigung eingeschraenkt.
- Haertefall-Fahrverbot: Nicht jede berufliche Betroffenheit genuegt — wirtschaftliche Existenzgefaehrdung oder alternativlose Infrastruktur noetig.
- Rechtsbeschwerde setzt Anwaltszwang voraus (§ 79 Abs. 3 OWiG i. V. m. § 341 StPO analog).

## Typische Fehler

- Einspruch ohne gleichzeitige Akteneinsicht: Verteidigung beginnt blind ohne Kenntnis der Messumstaende.
- Schweigen im Anhörungsbogen unterlassen: Mandant macht Angaben, die später als Beweismittel verwendet werden.
- Fahreridentifizierungsstrategie zu spaet entwickelt: Fotoabgleich wird im Bussgeldbescheid bereits verwendet und nicht mehr angegriffen.
- Haertefall nicht rechtzeitig vorgetragen: Amtsgericht prüft von Amts wegen nicht — Vortrag Sache des Verteidigers.
- Rechtsbeschwerde ohne Zulassungsgrund: Nur bei Verfahrensfehlern oder Rechtsfragen von grundsaetzlicher Bedeutung zulässig.

## Quellen und Aktualitaet

- Stand: 05/2026
- StVG in der zum Stand-Datum geltenden Fassung
- OWiG in der geltenden Fassung
- BKatV (Bussgeldkatalogverordnung) in der geltenden Fassung
