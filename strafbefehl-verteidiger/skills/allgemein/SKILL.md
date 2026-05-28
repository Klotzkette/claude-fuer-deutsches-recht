---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Strafbefehl Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Strafbefehl-Verteidiger — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Strafbefehl Verteidiger**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung.

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
| `strafbefehl-abwesenheit-vertretung` | Mandant kann oder will zur Hauptverhandlung nach Strafbefehl-Einspruch nicht erscheinen und Verteidiger soll ihn vertreten. Prüfraster Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO Voraussetzungen und Antrag.… |
| `strafbefehl-aktenanlage` | Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO… |
| `strafbefehl-akteneinsicht-147` | Akteneinsicht im Strafbefehlsverfahren nach § 147 StPO. Antrag bei Staatsanwaltschaft oder Amtsgericht. Versagungsgründe § 147 Abs. 2 StPO. Akte im Strafbefehlsverfahren: Ermittlungsakte Messakte Bußgeldheft.… |
| `strafbefehl-beweis-und-einlassung` | Beweisprüfung und Einlassungsstrategie im Strafbefehlsverfahren. Schweigen nach § 136 StPO darf nicht nachteilig gewertet werden (BGH st. Rspr.). Gestaendnis vs. Bestreiten Strategie. Beweisanträge § 244 StPO.… |
| `strafbefehl-deal-verstaendigung` | Verständigung nach § 257c StPO im Strafbefehlsverfahren. Voraussetzungen Inhalt Bindungswirkung Belehrung nach § 257c Abs. 4 und 5 StPO. Grenzen: kein Freispruch kein Schuldspruchverzicht. Abgrenzung informelle… |
| `strafbefehl-einspruch-beschraenkung` | Beschraenkter Einspruch nach § 410 Abs. 2 StPO auf Rechtsfolgen. Schuldspruch wird rechtskraeftig. Taktisches Kalkuel. Geldstrafe Tagessatz Fahrverbot Einziehung angreifbar. Vollstreckungsverzug § 456a StPO. Abgrenzung… |
| `strafbefehl-einstellung-153-153a-170` | Einstellung im Strafbefehlsverfahren: § 153 StPO (Geringfuegigkeit ohne Auflage) § 153a StPO (mit Auflage) § 170 Abs. 2 StPO (Einstellung mangels hinreichenden Tatverdachts). Opportunitaetsprinzip.… |
| `strafbefehl-fristen-einspruch` | Sichert die Einspruchsfrist nach § 410 StPO (2 Wochen ab Zustellung) und erstellt Einspruchsentwuerfe. Berechnung Zustellungsfiktion § 418 ZPO i.V.m. § 37 StPO. Unbeschraenkter oder beschraenkter Einspruch § 410 Abs. 2… |
| `strafbefehl-hauptverhandlung-vorbereitung` | Hauptverhandlung nach § 411 StPO bei Einspruch. Termin Vorbereitungspflichten. Beweisanträge § 244 StPO. Einlassung oder Schweigen. Strafzumessung § 46 StGB. Befangenheitsantrag § 24 StPO. Entbindung von… |
| `strafbefehl-inhalt-409-pruefung` | Prüft Strafbefehl auf Pflichtinhalt nach § 409 StPO (7 Mindestangaben) und identifiziert Nichtigkeitsgründe. Tatbeschreibung Bestimmtheitsgrundsatz Art. 103 Abs. 2 GG. Fehlerhafte Rechtsfolgen Geldstrafe Tagessatz… |
| `strafbefehl-kommandocenter` | Einstieg in das Strafbefehl-Mandat — Ampel-Schnelldiagnose zeigt kritische Fristen und offene Handlungsfelder auf einen Blick. Zentrales Steuerungsmodul routet auf Subskills: Frist § 410 StPO Akteneinsicht § 147 StPO… |
| `strafbefehl-nebenfolgen-fahrerlaubnis` | Fahrerlaubnisentzug § 69 StGB und Fahrverbot § 44 StGB im Strafbefehl. Regelentziehung § 69 Abs. 2 StGB bei §§ 315c 316 142 StGB. Sperrfrist § 69a StGB. Vorzeitige Aufhebung § 69a Abs. 7 StGB. Abgrenzung § 25 StVG… |
| `strafbefehl-pflichtverteidiger` | Pflichtverteidigerbestellung im Strafbefehlsverfahren nach § 140 StPO. Notwendige Verteidigung. Antrag auf Beiordnung § 141 StPO. Bestellung durch Gericht. Auswechslung des Pflichtverteidigers § 143a StPO. Gebühren Nr.… |
| `strafbefehl-quality-gate` | Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO… |
| `strafbefehl-rechtsmittel-nach-urteil` | Rechtsmittel nach Urteil in der Hauptverhandlung nach Strafbefehl-Einspruch. Berufung § 312 StPO (Frist 1 Woche schriftlich). Revision § 333 StPO (Frist 1 Woche Rechtsfehler). Revisionsbegründung § 345 StPO 1 Monat.… |
| `strafbefehl-rechtsprechungsrecherche` | Rechtsprechung zum Strafbefehlsverfahren recherchieren für Schriftsaetze oder Argumentation in der Hauptverhandlung. Prüfraster BGH OLG-Rspr zu §§ 407-412 StPO Einspruch Wiedereinsetzung Strafzumessung. Normen §§ 407… |
| `strafbefehl-tagessaetze-geldstrafe` | Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB.… |
| `strafbefehl-wiedereinsetzung` | Wiedereinsetzung in den vorigen Stand nach § 44 StPO bei versaeumter Einspruchsfrist. Voraussetzungen: kein Verschulden. Antragsfrist 1 Woche. Glaubhaftmachung § 45 StPO. Zustellungsfiktion entgegnen. Eidesstattliche… |
| `strafbefehl-zeugen-befragungsstrategie` | Hauptverhandlung nach Strafbefehl-Einspruch — Zeugen erschuettern oder Entlastungszeugen foerdern. Prüfraster Glaubwürdigkeitsanalyse Aussage-Konstanz Vorhalt fruehere Aussage Fragerecht § 240 StPO. Normen § 68 StPO… |
| `strafbefehl-zulaessigkeit-407` | Zulässigkeit des Strafbefehls nach § 407 StPO. Nur Vergehen. Sanktionskatalog § 407 Abs. 2 StPO. Sachliche Zuständigkeit Amtsgericht. Keine U-Haft. Keine Beweisprobleme die Hauptverhandlung erfordern. Ablehnung durch… |

## Worum geht es?

Das Strafbefehlsverfahren nach §§ 407 ff. StPO ermoeglicht es dem Amtsgericht, Vergehen ohne Hauptverhandlung durch schriftlichen Beschluss (Strafbefehl) zu ahnden. Der Strafbefehl ergeht auf Antrag der Staatsanwaltschaft und wird rechtskraeftig, wenn der Beschuldigte nicht innerhalb von zwei Wochen ab Zustellung Einspruch einlegt (§ 410 StPO). Diese Frist ist eine absolute Ausschlussfrist.

Das Plugin unterstuetzt Strafverteidiger beim gesamten Verteidigungsablauf: von der Fristensicherung und Akteneinsicht ueber die Inhaltspruefung, Einlassungsstrategie und Tagessatz-Berechnung bis hin zur Hauptverhandlung, Verstaendigung und zu Rechtsmitteln nach einem Urteil.

## Wann brauchen Sie diese Skill?

- Ein Mandant hat einen Strafbefehl erhalten und Sie muessen sofort die Einspruchsfrist berechnen und sichern.
- Sie pruefen, ob der Strafbefehl Pflichtinhalt nach § 409 StPO enthaelt und ob Nichtigkeitsgruende vorliegen.
- Sie berechnen die Hoehe der Geldstrafe (Tagessatz x Anzahl) und wollen sie anfechten oder den Tagessatz korrigieren.
- Der Mandant kann zur Hauptverhandlung nicht erscheinen und Sie muessen einen Entbindungsantrag nach § 411 Abs. 2 StPO stellen.
- Nach der Hauptverhandlung soll Berufung oder Revision eingelegt werden.

## Fachbegriffe (kurz erklaert)

- **Strafbefehl** — schriftlicher Beschluss des Amtsgerichts auf Antrag der Staatsanwaltschaft; ersetzt die Hauptverhandlung bei Vergehen mit bestimmten Rechtsfolgen (§ 407 Abs. 2 StPO).
- **Einspruch** — Rechtsmittel gegen den Strafbefehl; fuehrt zur Anberaumung einer Hauptverhandlung (§§ 410 f. StPO); Frist zwei Wochen ab Zustellung.
- **Beschraenkter Einspruch** — Einspruch nur gegen die Rechtsfolgen; der Schuldspruch wird rechtskraeftig (§ 410 Abs. 2 StPO).
- **Tagessatz** — Einheit der Geldstrafe; Hoehe richtet sich nach Nettoeinkommen des Taeters (ein Dreissigstel des monatlichen Nettoeinkommens, § 40 StGB).
- **Pflichtverteidiger** — vom Gericht beigeordneter Verteidiger bei notwendiger Verteidigung nach § 140 StPO.
- **Wiedereinsetzung** — Wiederherstellung einer versaeumten Einspruchsfrist bei fehlendem Verschulden (§ 44 StPO).
- **Verstaendigung** — Absprache nach § 257c StPO; bindend fuer das Gericht bei Gestaendnis und Zustimmung aller Beteiligten.

## Rechtsgrundlagen

- §§ 407-412 StPO — Strafbefehlsverfahren
- § 409 StPO — Pflichtinhalt des Strafbefehls
- § 410 StPO — Einspruch, Frist und beschraenkter Einspruch
- § 411 StPO — Hauptverhandlung nach Einspruch
- § 412 StPO — Verwerfung des Einspruchs bei Ausbleiben
- § 44 StPO — Wiedereinsetzung in den vorigen Stand
- § 140 StPO — Notwendige Verteidigung
- § 147 StPO — Akteneinsicht
- §§ 40-43 StGB — Geldstrafe, Tagessatz, Ersatzfreiheitsstrafe
- § 257c StPO — Verstaendigung im Strafverfahren

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Ist der Strafbefehl bereits zugegangen? Wann genau?
2. Phase des Mandats bestimmen: Vor Einspruchsfrist-Ablauf (sofortige Fristensicherung), nach Einspruch (Strategie), Hauptverhandlung oder Urteil?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: § 410 StPO — zwei Wochen ab Zustellung; keine Verlaengerung moeglich ausser Wiedereinsetzung nach § 44 StPO.
5. Anschluss-Skill bestimmen: Nach Einspruch zu Akteneinsicht, dann Beweis- und Einlassungsstrategie, dann Hauptverhandlung.

## Skill-Tour (was gibt es hier?)

- `strafbefehl-kommandocenter` — Einstieg und Ampel-Schnelldiagnose: kritische Fristen und offene Handlungsfelder auf einen Blick.
- `strafbefehl-aktenanlage` — Neue Mandatsakte mit Fristen, Vollmacht und Beweismittelverzeichnis anlegen.
- `strafbefehl-fristen-einspruch` — Einspruchsfrist nach § 410 StPO berechnen und Einspruchsentwurf erstellen.
- `strafbefehl-inhalt-409-pruefung` — Strafbefehl auf Pflichtinhalt nach § 409 StPO und Nichtigkeitsgruende pruefen.
- `strafbefehl-zulaessigkeit-407` — Zulaessigkeitsvoraussetzungen (nur Vergehen, Sanktionskatalog, Zustaendigkeit) pruefen.
- `strafbefehl-akteneinsicht-147` — Akteneinsicht nach § 147 StPO beantragen und Versagungsgruende pruefen.
- `strafbefehl-tagessaetze-geldstrafe` — Tagessatzhoehe und Geldstrafe nach §§ 40 ff. StGB berechnen und anfechten.
- `strafbefehl-nebenfolgen-fahrerlaubnis` — Fahrerlaubnisentzug (§ 69 StGB) und Fahrverbot (§ 44 StGB) pruefen und haertere Folgen abwenden.
- `strafbefehl-einspruch-beschraenkung` — Beschraenkten Einspruch auf Rechtsfolgen nach § 410 Abs. 2 StPO taktisch einsetzen.
- `strafbefehl-beweis-und-einlassung` — Beweispruefung und Einlassungsstrategie (Schweigen vs. Gestaendnis vs. Bestreiten).
- `strafbefehl-pflichtverteidiger` — Pflichtverteidigerbestellung nach § 140 StPO beantragen.
- `strafbefehl-wiedereinsetzung` — Wiedereinsetzung bei versaeumter Einspruchsfrist nach § 44 StPO.
- `strafbefehl-einstellung-153-153a-170` — Einstellungsmoeglichkeiten nach §§ 153/153a/170 Abs. 2 StPO ausloten.
- `strafbefehl-deal-verstaendigung` — Verstaendigung nach § 257c StPO im Strafbefehlsverfahren.
- `strafbefehl-hauptverhandlung-vorbereitung` — Hauptverhandlung nach § 411 StPO vorbereiten: Beweisantraege, Einlassung, Schlussvortrag.
- `strafbefehl-abwesenheit-vertretung` — Entbindung von Erscheinungspflicht nach § 411 Abs. 2 StPO und Vertretung des Mandanten.
- `strafbefehl-zeugen-befragungsstrategie` — Belastungszeugen erschuettern und Entlastungszeugen foerdern in der Hauptverhandlung.
- `strafbefehl-rechtsprechungsrecherche` — BGH- und OLG-Rechtsprechung zu §§ 407-412 StPO fuer Schriftsaetze recherchieren.
- `strafbefehl-rechtsmittel-nach-urteil` — Berufung (§ 312 StPO) und Revision (§ 333 StPO) nach Urteil in der Hauptverhandlung.
- `strafbefehl-quality-gate` — Abschluss-Pruefung vor Einspruch-Versand, vor Hauptverhandlung oder nach Urteil.

## Worauf besonders achten

- **Zwei-Wochen-Frist ist absolut**: Die Einspruchsfrist nach § 410 StPO laeuft auch dann, wenn der Mandant von dem Strafbefehl erst nach ein paar Tagen erfahren hat; Zustellungsfiktion nach § 418 ZPO i.V.m. § 37 StPO beachten.
- **Zustellungsfiktion pruefen**: Bei Ersatzzustellung oder Niederlegung laeuft die Frist moeglicherweise schon, ohne dass der Mandant den Bescheid gelesen hat; Wiedereinsetzung nach § 44 StPO nur bei fehlendem Verschulden.
- **Beschraenkter Einspruch macht Schuldspruch rechtskraeftig**: Wer nur gegen die Rechtsfolgen vorgeht, gibt den Freispruch dauerhaft auf.
- **Tagessatz-Festsetzung des Gerichts angreifbar**: Gerichte schaetzen haeufig, wenn keine Einkommensnachweise vorliegen; dieser Schaetzung kann mit konkreten Belegen entgegengetreten werden.
- **Pflichtverteidiger sichert Verfahrensrechte**: In Faellen mit notwendiger Verteidigung (§ 140 StPO) ist der Antrag sofort zu stellen, da spaetere Bestellung Versaeumnisse nicht heilt.

## Typische Fehler

- Einspruchsfrist verpennt, weil Mandant den Bescheid ignoriert hat: Ohne Wiedereinsetzungsgrund tritt Rechtskraft ein; kein zweiter Weg.
- Schuldspruch durch beschraenkten Einspruch akzeptiert ohne Konsequenzcheck: Eintraege im Bundeszentralregister, berufsrechtliche Folgen und spaetere Strafzumessung werden nicht bedacht.
- Geldstrafe als Endpunkt gesehen: Ersatzfreiheitsstrafe (§ 43 StGB) droht bei Nichtzahlung; Ratenzahlung nach § 42 StGB rechtzeitig beantragen.
- Keine Akteneinsicht vor Einlassungsentscheidung: Ohne Kenntnis des Ermittlungsergebnisses kann keine fundierte Strategie entwickelt werden.
- Verstaendigung nach § 257c StPO ohne Belehrungspruefung: Fehlt die Belehrung nach § 257c Abs. 4 und 5 StPO, entfaltet die Verstaendigung keine Bindungswirkung.

## Querverweise

- `prozessrecht` — Wenn sich aus dem Strafbefehlsverfahren zivilrechtliche Folgefragen (Schadenersatz, Beschlagnahme) ergeben.
- `arbeitsrecht` — Wenn der Strafbefehl-Vorwurf auch arbeitsrechtliche Konsequenzen hat (Kuendigung, Abmahnung, interne Untersuchung).
- `selbstvertreter-amtsgericht` — Wenn der Mandant ohne Anwalt das Hauptverhandlungsverfahren fuehren will.

## Quellen und Aktualitaet

- Stand: 05/2026
- StPO §§ 407-412 in geltender Fassung
- StGB §§ 40-43 in geltender Fassung
- § 257c StPO (Verstaendigung) in geltender Fassung
