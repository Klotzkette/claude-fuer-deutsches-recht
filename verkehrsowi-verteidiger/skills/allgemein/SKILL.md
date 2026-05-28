---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Verkehrsowi Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# VerkehrsOWi-Verteidiger — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verkehrsowi Verteidiger**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

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
| `verkehrsowi-aktenanlage` | Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster:… |
| `verkehrsowi-akteneinsicht-messakte` | Vollständige Messakte im OWi-Verfahren anfordern und prüfen: Pflichtverteidigung benoetigt Rohmessdaten und Eichunterlagen. Normen: § 49 OWiG i.V.m. § 147 StPO (Akteneinsicht), BVerfG NJW 2021 455 (Rohmessdaten-Recht).… |
| `verkehrsowi-alkohol-drogen-24a` | Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis… |
| `verkehrsowi-anhoerung-bussgeldbescheid` | Anhoerung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhoerungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhoerung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67… |
| `verkehrsowi-beweisverwertung-standardisiert` | Beweisverwertbarkeit im standardisierten OWi-Messverfahren angreifen: Mandant bestreitet Messergebnis. Normen: BGH NJW 1993 3081 (standardisiertes Messverfahren), § 77 Abs. 2 OWiG (Sachverständigen-Antrag). Prüfraster:… |
| `verkehrsowi-fahreridentifizierung` | Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG… |
| `verkehrsowi-fristen-einspruch` | Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG… |
| `verkehrsowi-haertefall-fahrverbot` | Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG… |
| `verkehrsowi-hauptverhandlung-amtsgericht` | Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG… |
| `verkehrsowi-kommandocenter` | Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf,… |
| `verkehrsowi-mandantenkommunikation` | Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden,… |
| `verkehrsowi-messverfahren-geschwindigkeit` | Geschwindigkeitsmessungen im OWi-Verfahren angreifen: Mandant bestreitet Messergebnis von TraffiStar, Riegl, ESO 3.0 oder PoliScan. Normen: BGH NJW 1993 3081 (standardisiertes Messverfahren), § 77 OWiG (Beweisanträge),… |
| `verkehrsowi-punkte-fahrverbot-flensburg` | Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8… |
| `verkehrsowi-quality-gate` | Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte… |
| `verkehrsowi-rechtsbeschwerde` | Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG… |
| `verkehrsowi-rechtsprechungsrecherche` | Rechtsprechungsrecherche für OWi-Verkehrsmandate: Anwalt sucht OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverbot. Normen: §§ 24 StVG, 25 StVG, 4 StVG; OWiG §§ 67 und 79 und 80. Prüfraster:… |
| `verkehrsowi-rotlicht-abstand-handy` | Rotlicht-OWi, Abstand-OWi und Handy-OWi verteidigen: Mandant hat Bußgeldbescheid wegen Rotlicht, zu geringem Abstand oder Handynutzung erhalten. Normen: § 37 StVO (Rotlicht: einfach vs. qualifiziert 1 Sekunde), § 4… |
| `verkehrsowi-simulation-training` | Simulationstraining für OWi-Mandate. Uebungsszenarien Messverfahren Rotlicht Handy Alkohol Fahreridentifizierung. Rollenspiel Mandantengespraeche Hauptverhandlung. Beispielfaelle mit Musterlösung. Training ohne echte… |
| `verkehrsowi-verjaehrung-zustellung` | Verfolgungsverjährung im OWi-Verfahren prüfen: Anwalt will Verjährungseinwand erheben. Normen: § 26 StVG i.V.m. § 31 OWiG (Verjährungsfrist 3 Monate nach Tatende), § 33 OWiG (Unterbrechungshandlungen), absolute… |
| `verkehrsowi-zeugen-polizei-strategie` | Zeugen-Strategie gegenüber Polizeibeamten im OWi-Verfahren: Polizeibeamter als einziger Zeuge in der HV. Normen: § 240 StPO i.V.m. § 71 OWiG (Fragerecht), §§ 373 ff. StPO (Zeugenvernehmung). Prüfraster:… |

## Worum geht es?

Dieses Plugin begleitet Verkehrs-Ordnungswidrigkeitsmandate von der ersten Anhoerung bis zur Rechtsbeschwerde. Es richtet sich an Rechtsanwaelte, die Mandanten bei Bussgeldbescheiden, Fahrverboten, Punkteeintragungen und Verfahren vor dem Amtsgericht vertreten. Abgedeckt werden Geschwindigkeitsmessungen, Rotlicht-OWi, Abstandsverfahren, Handyverstaesse, Alkohol und Drogen am Steuer, Fahreridentifizierung sowie die Beweisverwertung standardisierter Messverfahren.

Das Plugin folgt dem Verfahrensablauf: Anhoerung → Bussgeldbescheid → Einspruch → Akteneinsicht/Messakte → Hauptverhandlung → ggf. Rechtsbeschwerde. Jede Phase hat eigene Fristen und Verteidigungsstrategien.

## Wann brauchen Sie diese Skill?

- Mandant erhaelt Anhoerungsbogen oder Bussgeldbescheid wegen Geschwindigkeitsueberschreitung und braucht sofortige Beratung zu Einspruchsfrist und Strategie.
- Mandant ist auf den Fuehrerschein beruflich angewiesen und soll Fahrverbot erhalten — Haertefall-Argumentation pruefen.
- Anwalt hat Akteneinsicht beantragt und will Messakte auf Verfahrensfehler untersuchen.
- Mandant bestreitet Fahrereigenschaft — Fahreridentifizierungsstrategie entwickeln.
- OWi-Urteil des Amtsgerichts ist unbefriedigend und Rechtsbeschwerde zum OLG wird erwaogen.

## Fachbegriffe (kurz erklaert)

- **OWiG** — Gesetz ueber Ordnungswidrigkeiten; Rahmengesetz fuer alle Ordnungswidrigkeitsverfahren einschliesslich VerkehrsOWi.
- **StVG** — Strassenverkehrsgesetz; § 24 StVG Grundnorm fuer Verkehrsordnungswidrigkeiten, § 25 StVG Fahrverbot.
- **FAER** — Fahreignungsregister; Punkteregister in Flensburg beim Kraftfahrt-Bundesamt.
- **Messakte** — Vollstaendige Unterlagen zum Messvorgang: Eichschein, Rohmessdaten, Geraetefoto, Aufstellprotokoll.
- **Standardisiertes Messverfahren** — Pruefstandsgerechtes Verfahren mit amtlich anerkanntem Messgeraet; Gerichte duerfen auf Beweiswert vertrauen, solange keine konkreten Fehlerhinweise vorliegen.
- **Verfolgungsverjaehrung** — Nach §§ 26 StVG und 31 ff. OWiG: Verjaeht die Tat, kann kein Bussgeld mehr verhaengt werden.
- **Rechtsbeschwerde** — Rechtsmittel nach § 79 OWiG zum Oberlandesgericht gegen Urteil des Amtsgerichts im OWi-Verfahren.
- **Haertefall** — Ausnahme vom Fahrverbot nach § 25 StVG, wenn unverhieltnisgemaessige berufliche Folgen drohen.

## Rechtsgrundlagen

- § 24 StVG (Ordnungswidrigkeiten im Strassenverkehr)
- § 25 StVG (Fahrverbot)
- §§ 26 StVG (Verfolgungsverjaehrung)
- §§ 24a StVG (Alkohol- und Drogenfahrten)
- §§ 67 ff. OWiG (Einspruch gegen Bussgeldbescheid)
- § 79 OWiG (Rechtsbeschwerde zum OLG)
- §§ 62-66 OWiG (Akteneinsicht im OWi-Verfahren)
- BKatV (Bussgeldkatalogverordnung mit Regelbuessgeldern und Fahrverboten)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Aktenanlage und Mandat aufnehmen: Tatvorwurf, Verfahrensstadium, Fristen erfassen (`verkehrsowi-aktenanlage`).
2. Einspruchsfrist pruefen: Zwei Wochen ab Zustellung des Bussgeldbescheids — Fristwahrung hat Vorrang (`verkehrsowi-fristen-einspruch`).
3. Akteneinsicht und Messakte beantragen und auswerten (`verkehrsowi-akteneinsicht-messakte`).
4. Verteidigungsstrategie festlegen: Messverfahren angreifen, Fahreridentifizierung, Haertefall?
5. Quality-Gate vor Einspruch und vor Hauptverhandlung durchlaufen (`verkehrsowi-quality-gate`).

## Skill-Tour (was gibt es hier?)

- `verkehrsowi-kommandocenter` — Zentrales Steuerungsmodul: schnelle Orientierung fuer jedes OWi-Mandat vom Intake bis zur Strategie.
- `verkehrsowi-aktenanlage` — Akte im VerkehrsOWi-Mandat anlegen und strukturieren.
- `verkehrsowi-anhoerung-bussgeldbescheid` — Reaktion auf Anhoerungsbogen oder Bussgeldbescheid strategisch vorbereiten.
- `verkehrsowi-fristen-einspruch` — Einspruchsfrist berechnen und wahren; Fristversaeumnis-Risiken erkennen.
- `verkehrsowi-akteneinsicht-messakte` — Vollstaendige Messakte anfordern und auf Verfahrensfehler und Eichluecken pruefen.
- `verkehrsowi-messverfahren-geschwindigkeit` — Geschwindigkeitsmessungen (TraffiStar, Riegl, ESO) auf Verwertbarkeit angreifen.
- `verkehrsowi-beweisverwertung-standardisiert` — Beweisverwertbarkeit im standardisierten Messverfahren angreifen.
- `verkehrsowi-rotlicht-abstand-handy` — Rotlicht-, Abstands- und Handy-OWi verteidigen.
- `verkehrsowi-alkohol-drogen-24a` — Alkohol- und Drogen-OWi nach § 24a StVG verteidigen (0,5-Promille, Drogennachweis).
- `verkehrsowi-fahreridentifizierung` — Fahrereigenschaft angreifen oder Fahreridentifizierung als Verteidigungsstrategieklaeren.
- `verkehrsowi-punkte-fahrverbot-flensburg` — Punkte im FAER und Fahrverbot nach § 25 StVG pruefen und Massnahmen besprechen.
- `verkehrsowi-haertefall-fahrverbot` — Haertefall-Argumentation gegen Fahrverbot bei beruflicher Angewiesenheit entwickeln.
- `verkehrsowi-verjaehrung-zustellung` — Verfolgungsverjaehrung pruefen und Zustellungsfehler identifizieren.
- `verkehrsowi-hauptverhandlung-amtsgericht` — Hauptverhandlung am Amtsgericht vorbereiten und fuehren.
- `verkehrsowi-rechtsbeschwerde` — Rechtsbeschwerde nach § 79 OWiG zum OLG einlegen.
- `verkehrsowi-zeugen-polizei-strategie` — Zeugen-Strategie gegenueber Polizeibeamten in der Hauptverhandlung entwickeln.
- `verkehrsowi-quality-gate` — Checkliste vor Einspruch, nach Akteneingang und vor Hauptverhandlung durchlaufen.
- `verkehrsowi-mandantenkommunikation` — Mandant verstaendlich ueber Verfahren, Kosten und Aussichten informieren.
- `verkehrsowi-rechtsprechungsrecherche` — OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverboten recherchieren.
- `verkehrsowi-simulation-training` — Simulationstraining fuer OWi-Mandate: Messverfahren, Rotlicht, Handy, Alkohol, Fahreridentifizierung.

## Worauf besonders achten

- Einspruchsfrist ist zwei Wochen ab Zustellung — keine Hemmung, kein Neubeginn bei blossem Schweigen; Fristverpassen = Rechtskraft.
- Verfolgungsverjaehrung nach § 26 StVG betraegt 3 Monate ab Tatbegehung, Unterbrechung durch behordliche Massnahmen — Zeitstrahl pruefen.
- Akteneinsicht in Messakte inklusive Rohmessdaten ist einzufordern; ohne Rohmessdaten ist effektive Verteidigung eingeschraenkt.
- Haertefall-Fahrverbot: Nicht jede berufliche Betroffenheit genuegt — wirtschaftliche Existenzgefaehrdung oder alternativlose Infrastruktur noetig.
- Rechtsbeschwerde setzt Anwaltszwang voraus (§ 79 Abs. 3 OWiG i. V. m. § 341 StPO analog).

## Typische Fehler

- Einspruch ohne gleichzeitige Akteneinsicht: Verteidigung beginnt blind ohne Kenntnis der Messumstaende.
- Schweigen im Anhoerungsbogen unterlassen: Mandant macht Angaben, die spaeter als Beweismittel verwendet werden.
- Fahreridentifizierungsstrategie zu spaet entwickelt: Fotoabgleich wird im Bussgeldbescheid bereits verwendet und nicht mehr angegriffen.
- Haertefall nicht rechtzeitig vorgetragen: Amtsgericht prueft von Amts wegen nicht — Vortrag Sache des Verteidigers.
- Rechtsbeschwerde ohne Zulassungsgrund: Nur bei Verfahrensfehlern oder Rechtsfragen von grundsaetzlicher Bedeutung zulaessig.

## Querverweise

- `selbstvertreter-amtsgericht` — Fuer Mandanten ohne Anwalt gibt es das amtsgerichtliche Selbstvertretungs-Plugin.
- `datenschutzrecht` — Messdaten aus Fahrzeugkameras und Datenerhebung durch Blitzergeraete haben datenschutzrechtliche Dimensionen.

## Quellen und Aktualitaet

- Stand: 05/2026
- StVG in der zum Stand-Datum geltenden Fassung
- OWiG in der geltenden Fassung
- BKatV (Bussgeldkatalogverordnung) in der geltenden Fassung
