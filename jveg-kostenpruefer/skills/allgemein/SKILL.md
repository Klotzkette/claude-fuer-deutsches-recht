---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im JVEG Kostenpruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# JVEG-Kostenpruefer — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **JVEG Kostenpruefer**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle.

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
| `jveg-aktenstripper` | JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter… |
| `jveg-anspruchsberechtigung` | Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis… |
| `jveg-antragsgenerator` | Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach… |
| `jveg-dolmetscher-uebersetzer` | Verguetung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output:… |
| `jveg-fahrtkosten` | Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG.… |
| `jveg-festsetzung-beschwerde` | Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output:… |
| `jveg-fristen-erloeschen` | Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung.… |
| `jveg-gerichtsschreiben-pruefung` | Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben… |
| `jveg-kommandocenter` | Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output:… |
| `jveg-kuerzung-wegfall-8a` | Kuerzung oder Wegfall der JVEG-Verguetung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit… |
| `jveg-quality-gate` | Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht… |
| `jveg-rechenblatt` | JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares… |
| `jveg-sachverstaendigenrechnung` | Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte… |
| `jveg-sonstige-aufwendungen-belege` | Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Hoehe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG.… |
| `jveg-uebernachtung-aufwand` | Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output:… |
| `jveg-verdienstausfall-haushalt-zeit` | Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output:… |
| `jveg-vorschuss` | Vorschuss auf JVEG-Verguetung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung:… |
| `jveg-zeugenentschaedigung` | Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Prüfraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung.… |
| `pruefung-sachverstaendigengutachten-ki-deklaration` | KI-Deklaration in Sachverständigengutachten prüfen: Hat der Sachverständige KI-Nutzung offengelegt? Normen: §§ 404 ff. ZPO, JVEG. Prüfraster: Deklarationspflicht, Methodentransparenz, Beeinflussung des Gutachtenwertes.… |

## Worum geht es?

Das JVEG-Kostenpruefer-Plugin prueft und berechnet Verguetungsansprueche nach dem Justizvergutungs- und -entschaedigungsgesetz (JVEG) fuer alle gerichtlich herangezogenen Personen: Sachverstaendige, Dolmetscher und Uebersetzer, Zeugen sowie sonstige Beteiligte. Es erstellt belegfeste Rechenprotokolle, prueft Kuerz­ungen durch das Gericht, bereitet Antraege und Beschwerden vor und bewertet die Korrektheit von Gerichtsschreiben zur Kostenfestsetzung.

Das Plugin ist mandatsneutral: Es wird sowohl von Sachverstaendigen genutzt, die ihre Rechnung optimieren wollen, als auch von Gerichten, Anwaelten oder Parteien, die eine Sachverstaendigenrechnung pruefen. Es ersetzt keine Rechtsberatung.

## Wann brauchen Sie diese Skill?

- Sachverstaendiger hat seine Rechnung gestellt und moechte pruefen, ob alle Positionen nach JVEG ansetzbar sind.
- Gericht hat eine Kostenfestsetzung erlassen und Sachverstaendiger oder Zeuge will widersprechen oder Beschwerde einlegen.
- Anwalt prueft, ob die Sachverstaendigenrechnung der Gegenseite korrekt ist und Kuerzungsmoeglichkeiten bestehen.
- Zeuge moechte nach einer Aussage vor Gericht seine Entschaedigung (Fahrtkosten, Zeitversaeumnis, Verdienstausfall) beantragen.
- Dolmetscher oder Uebersetzer will seine Stundenverguetung und Nebenkosten nach JVEG abrechnen.

## Fachbegriffe (kurz erklaert)

- **JVEG** — Justizvergutungs- und -entschaedigungsgesetz; regelt Verguetung und Entschaedigung fuer Sachverstaendige, Dolmetscher, Zeugen und andere vom Gericht herangezogene Personen.
- **Anspruchsberechtigung** — Nur gerichtlich beauftragte Personen (§§ 1 und 2 JVEG) sind anspruchsberechtigt; kein Anspruch fuer privatgutachterliche Taetigkeit.
- **Dreimonatsfrist** — Verguetungsanspruch erlischt, wenn er nicht innerhalb von drei Monaten nach Abschluss der Taetigkeit geltend gemacht wird (§ 2 Abs. 1 JVEG).
- **Verguetungssaetze Anlage 1** — Stundenverguetung fuer Sachverstaendige nach Honorargruppen; fuer Dolmetscher nach § 9 JVEG und Anlage 1 JVEG.
- **Barauslagen** — Erstattungsfaehige Aufwendungen nach § 7 JVEG (Porto, Kopieren, technische Geraete); Belegpflicht.
- **§ 8a JVEG** — Kuerzung oder Wegfall der Verguetung bei verspaetem oder fehlerhaftem Gutachten; Verschuldens- und Kausalitaetserfordernis.
- **Kostenfestsetzungsbeschluss** — Gerichtliche Entscheidung ueber die Hoehe der JVEG-Verguetung; anfechtbar per Beschwerde nach § 4 Abs. 3 JVEG.
- **KI-Deklaration** — Pflicht zur Offenlegung, ob und wie KI-Systeme bei der Gutachtenerstattung eingesetzt wurden; pruefungsrelevant fuer Gutachtenwert.

## Rechtsgrundlagen

- §§ 1 und 2 JVEG — Anwendungsbereich und Anspruchsberechtigung.
- § 2 Abs. 1 JVEG — Dreimonatsfrist Geltendmachung.
- § 3 JVEG — Vorschuss.
- § 4 JVEG — Festsetzung; § 4 Abs. 3 JVEG — Beschwerde.
- § 5 JVEG — Fahrtkosten.
- § 6 JVEG — Uebernachtungs- und Verpflegungskosten.
- § 7 JVEG — Sonstige Aufwendungen.
- § 8 JVEG — Verguetung Sachverstaendige; § 8a JVEG — Kuerzung und Wegfall.
- § 9 JVEG, Anlage 1 JVEG — Dolmetscher und Uebersetzer.
- §§ 19 bis 22 JVEG — Zeugenentschaedigung, Verdienstausfall, Haushaltsfuehrung.
- §§ 165 ff. SGB III (im Kontext) — Insolvenzgeld; nicht JVEG.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Personenkategorie bestimmen: Sachverstaendiger, Dolmetscher, Uebersetzer oder Zeuge?
2. Verfahrensschritt bestimmen: Erstrechnung, Widerspruch gegen Kuerzung, Beschwerde, Vorschuss?
3. Routing: Skill `jveg-kommandocenter` fuer die Weiterleitung zum richtigen Spezial-Skill.
4. Fristen pruefen: `jveg-fristen-erloeschen` — ist die Dreimonatsfrist noch offen?
5. Rechnung pruefen oder erstellen: `jveg-sachverstaendigenrechnung` oder `jveg-rechenblatt`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Navigation**

- `jveg-kommandocenter` — Navigationszentrum fuer alle JVEG-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt.
- `jveg-anspruchsberechtigung` — Anspruchsberechtigung nach JVEG pruefen: Personenkategorie und gerichtliche Beauftragung.
- `jveg-fristen-erloeschen` — Dreimonatsfrist pruefen; Fristbeginn, Fristende, Wiedereinsetzungsmoeglichkeit.

**Verguetungsberechnung Sachverstaendige**

- `jveg-sachverstaendigenrechnung` — Sachverstaendigenrechnung pruefen oder erstellen: Stundenverguetung und Nebenkosten.
- `jveg-rechenblatt` — Strukturiertes Rechenblatt fuer alle JVEG-Kostenpositionen je Kategorie.
- `jveg-aktenstripper` — JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren.
- `jveg-kuerzung-wegfall-8a` — Kuerzung oder Wegfall der Verguetung nach § 8a JVEG bei Verspaetung oder Fehlern.
- `pruefung-sachverstaendigengutachten-ki-deklaration` — KI-Deklaration in Sachverstaendigengutachten pruefen.

**Verguetungsberechnung Dolmetscher und Uebersetzer**

- `jveg-dolmetscher-uebersetzer` — Stundenverguetung, Mindestwartezeit, Anfahrt und schriftliche Uebersetzung je Seite.

**Zeugenentschaedigung**

- `jveg-zeugenentschaedigung` — Fahrtkosten, Zeitversaeumnis und Verdienstausfall fuer Zeugen.
- `jveg-verdienstausfall-haushalt-zeit` — Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG.

**Kostenpositionen**

- `jveg-fahrtkosten` — Fahrtkosten: eigenes Fahrzeug, oeff. Verkehrsmittel, Flug.
- `jveg-uebernachtung-aufwand` — Uebernachtungs- und Verpflegungskosten nach § 6 JVEG.
- `jveg-sonstige-aufwendungen-belege` — Sonstige Aufwendungen nach § 7 JVEG mit Belegpflicht.

**Antrag, Vorschuss und Rechtsmittel**

- `jveg-vorschuss` — Vorschuss nach § 3 JVEG: Voraussetzungen, Formerfordernis, Verfahren.
- `jveg-antragsgenerator` — Verguetungsantrag, Anlagen und Fristen fuer die gerichtliche Kostenfestsetzung.
- `jveg-gerichtsschreiben-pruefung` — Gerichtsschreiben zur Kostenkuerzung rechtlich pruefen und widersprechen.
- `jveg-festsetzung-beschwerde` — Beschwerde gegen Kostenfestsetzungsbeschluss nach § 4 Abs. 3 JVEG.

**Qualitaetssicherung**

- `jveg-quality-gate` — Vollstaendigkeits- und Konsistenzpruefung aller Kostenpositionen vor Einreichung.

## Worauf besonders achten

- **Dreimonatsfrist ist Ausschlussfrist** — § 2 Abs. 1 JVEG kennt keine automatische Verlaengerung; nach Ablauf ist der Anspruch erloschen.
- **Belegpflicht fuer Aufwendungen** — Sonstige Aufwendungen nach § 7 JVEG werden ohne Beleg nicht erstattet; Porto und Kopien muessen belegt sein.
- **§ 8a JVEG ist kein Automatismus** — Kuerzung oder Wegfall setzt Verschulden und Kausalitaet voraus; ein verspaetendes Gutachten fuehrt nicht zwingend zum Verguetungsverlust.
- **KI-Nutzung deklarieren** — Gerichte verlangen zunehmend Offenlegung des KI-Einsatzes; fehlende Deklaration kann Gutachtenwert beeinflussen und Verguetungsstreit ausloesen.
- **Honorargruppe korrekt einordnen** — Falsche Einordnung in Anlage 1 JVEG fuehrt zur Kuerzung; Sachgebiet und Schwierigkeitsgrad des Gutachtens bestimmen die Gruppe.

## Typische Fehler

- Sachverstaendiger stellt Vorschussantrag, aber das Gericht hat keine Vorschussanforderung gestellt; Verfahrensfehler.
- Zeuge beantragt Verguetung nach drei Monaten; Anspruch ist erloschen.
- Fahrtkosten werden mit privatem Pkw abgerechnet, obwohl guenstigeres Bahnticket zumutbar war.
- Sachverstaendiger ordnet sich selbst in eine hoehere Honorargruppe ein, ohne Begrunndung; Gericht kuerzt auf naechste Gruppe.
- Widerspruch gegen Kuerzung wird als formelle Beschwerde nach § 4 Abs. 3 JVEG eingereicht, obwohl Beschwerdesumme unterschritten ist.

## Querverweise

- `normenkontrolle-bauleitplanung` — Bei Sachverstaendigenkosten im oeffentlich-rechtlichen Normenkontrollverfahren.
- `insolvenzrecht` — Bei Sachverstaendigenbeauftragung im Insolvenzverfahren.
- `bereicherungs-und-anfechtungsrecht-pruefer` — Wenn zu Unrecht gezahlte JVEG-Verguetung zurueckgefordert werden soll.

## Quellen und Aktualitaet

- Stand: 05/2026
- JVEG in der geltenden Fassung
- Anlage 1 JVEG (Honorargruppen und Stundensaetze) in der geltenden Fassung
