---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im JVEG Kostenpruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig..."
---

# JVEG-Kostenpruefer — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: JVEG § 2 Antragsfrist 3 Monate nach Beendigung der Tätigkeit, § 4 Erinnerung 2 Wochen, Beschwerde § 4 Abs. 3 unbefristet.
- Tragende Normen verifizieren: JVEG §§ 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 19, 22, 23, RVG (Anwalt), ZSEG (alt), KostO/GNotKG, GG Art. 12 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Sachverständiger, Dolmetscher, Übersetzer, Geschäftsstelle, Kostenbeamter, Bezirksrevisor, Festsetzungsrichter, Erinnerung-/Beschwerdesenat.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vergütungsantrag, Stundennachweis, Reisekostenabrechnung, Festsetzungsbeschluss, Erinnerung, Beschwerde, Sachverständigenrechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **JVEG Kostenpruefer**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle.

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
| `jveg-aktenstripper` | JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter… |
| `jveg-anspruchsberechtigung` | Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis… |
| `jveg-antragsgenerator` | Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach… |
| `jveg-dolmetscher-uebersetzer` | Vergütung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output:… |
| `jveg-fahrtkosten` | Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG.… |
| `jveg-festsetzung-beschwerde` | Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output:… |
| `jveg-fristen-erloeschen` | Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung.… |
| `jveg-gerichtsschreiben-pruefung` | Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben… |
| `jveg-kommandocenter` | Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output:… |
| `jveg-kuerzung-wegfall-8a` | Kuerzung oder Wegfall der JVEG-Vergütung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit… |
| `jveg-quality-gate` | Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht… |
| `jveg-rechenblatt` | JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares… |
| `jveg-sachverstaendigenrechnung` | Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte… |
| `jveg-sonstige-aufwendungen-belege` | Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Höhe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG.… |
| `jveg-uebernachtung-aufwand` | Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output:… |
| `jveg-verdienstausfall-haushalt-zeit` | Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output:… |
| `jveg-vorschuss` | Vorschuss auf JVEG-Vergütung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung:… |
| `jveg-zeugenentschaedigung` | Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Prüfraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung.… |
| `pruefung-sachverstaendigengutachten-ki-deklaration` | KI-Deklaration in Sachverständigengutachten prüfen: Hat der Sachverständige KI-Nutzung offengelegt? Normen: §§ 404 ff. ZPO, JVEG. Prüfraster: Deklarationspflicht, Methodentransparenz, Beeinflussung des Gutachtenwertes.… |

## Worum geht es?

Das JVEG-Kostenpruefer-Plugin prüft und berechnet Verguetungsansprueche nach dem Justizvergutungs- und -entschaedigungsgesetz (JVEG) für alle gerichtlich herangezogenen Personen: Sachverstaendige, Dolmetscher und Übersetzer, Zeugen sowie sonstige Beteiligte. Es erstellt belegfeste Rechenprotokolle, prüft Kuerz­ungen durch das Gericht, bereitet Antraege und Beschwerden vor und bewertet die Korrektheit von Gerichtsschreiben zur Kostenfestsetzung.

Das Plugin ist mandatsneutral: Es wird sowohl von Sachverstaendigen genutzt, die ihre Rechnung optimieren wollen, als auch von Gerichten, Anwaelten oder Parteien, die eine Sachverstaendigenrechnung prüfen. Es ersetzt keine Rechtsberatung.

## Wann brauchen Sie diese Skill?

- Sachverstaendiger hat seine Rechnung gestellt und moechte prüfen, ob alle Positionen nach JVEG ansetzbar sind.
- Gericht hat eine Kostenfestsetzung erlassen und Sachverstaendiger oder Zeuge will widersprechen oder Beschwerde einlegen.
- Anwalt prüft, ob die Sachverstaendigenrechnung der Gegenseite korrekt ist und Kuerzungsmoeglichkeiten bestehen.
- Zeuge moechte nach einer Aussage vor Gericht seine Entschaedigung (Fahrtkosten, Zeitversaeumnis, Verdienstausfall) beantragen.
- Dolmetscher oder Übersetzer will seine Stundenverguetung und Nebenkosten nach JVEG abrechnen.

## Fachbegriffe (kurz erklaert)

- **JVEG** — Justizvergutungs- und -entschaedigungsgesetz; regelt Vergütung und Entschaedigung für Sachverstaendige, Dolmetscher, Zeugen und andere vom Gericht herangezogene Personen.
- **Anspruchsberechtigung** — Nur gerichtlich beauftragte Personen (§§ 1 und 2 JVEG) sind anspruchsberechtigt; kein Anspruch für privatgutachterliche Taetigkeit.
- **Dreimonatsfrist** — Verguetungsanspruch erlischt, wenn er nicht innerhalb von drei Monaten nach Abschluss der Taetigkeit geltend gemacht wird (§ 2 Abs. 1 JVEG).
- **Verguetungssaetze Anlage 1** — Stundenverguetung für Sachverstaendige nach Honorargruppen; für Dolmetscher nach § 9 JVEG und Anlage 1 JVEG.
- **Barauslagen** — Erstattungsfaehige Aufwendungen nach § 7 JVEG (Porto, Kopieren, technische Geraete); Belegpflicht.
- **§ 8a JVEG** — Kuerzung oder Wegfall der Vergütung bei verspaetem oder fehlerhaftem Gutachten; Verschuldens- und Kausalitaetserfordernis.
- **Kostenfestsetzungsbeschluss** — Gerichtliche Entscheidung über die Höhe der JVEG-Vergütung; anfechtbar per Beschwerde nach § 4 Abs. 3 JVEG.
- **KI-Deklaration** — Pflicht zur Offenlegung, ob und wie KI-Systeme bei der Gutachtenerstattung eingesetzt wurden; prüfungsrelevant für Gutachtenwert.

## Rechtsgrundlagen

- §§ 1 und 2 JVEG — Anwendungsbereich und Anspruchsberechtigung.
- § 2 Abs. 1 JVEG — Dreimonatsfrist Geltendmachung.
- § 3 JVEG — Vorschuss.
- § 4 JVEG — Festsetzung; § 4 Abs. 3 JVEG — Beschwerde.
- § 5 JVEG — Fahrtkosten.
- § 6 JVEG — Uebernachtungs- und Verpflegungskosten.
- § 7 JVEG — Sonstige Aufwendungen.
- § 8 JVEG — Vergütung Sachverstaendige; § 8a JVEG — Kuerzung und Wegfall.
- § 9 JVEG, Anlage 1 JVEG — Dolmetscher und Übersetzer.
- §§ 19 bis 22 JVEG — Zeugenentschaedigung, Verdienstausfall, Haushaltsfuehrung.
- §§ 165 ff. SGB III (im Kontext) — Insolvenzgeld; nicht JVEG.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Personenkategorie bestimmen: Sachverstaendiger, Dolmetscher, Übersetzer oder Zeuge?
2. Verfahrensschritt bestimmen: Erstrechnung, Widerspruch gegen Kuerzung, Beschwerde, Vorschuss?
3. Routing: Skill `jveg-kommandocenter` für die Weiterleitung zum passendes Fachmodul.
4. Fristen prüfen: `jveg-fristen-erloeschen` — ist die Dreimonatsfrist noch offen?
5. Rechnung prüfen oder erstellen: `jveg-sachverstaendigenrechnung` oder `jveg-rechenblatt`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Navigation**

- `jveg-kommandocenter` — Navigationszentrum für alle JVEG-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt.
- `jveg-anspruchsberechtigung` — Anspruchsberechtigung nach JVEG prüfen: Personenkategorie und gerichtliche Beauftragung.
- `jveg-fristen-erloeschen` — Dreimonatsfrist prüfen; Fristbeginn, Fristende, Wiedereinsetzungsmoeglichkeit.

**Verguetungsberechnung Sachverstaendige**

- `jveg-sachverstaendigenrechnung` — Sachverstaendigenrechnung prüfen oder erstellen: Stundenverguetung und Nebenkosten.
- `jveg-rechenblatt` — Strukturiertes Rechenblatt für alle JVEG-Kostenpositionen je Kategorie.
- `jveg-aktenstripper` — JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren.
- `jveg-kuerzung-wegfall-8a` — Kuerzung oder Wegfall der Vergütung nach § 8a JVEG bei Verspaetung oder Fehlern.
- `pruefung-sachverstaendigengutachten-ki-deklaration` — KI-Deklaration in Sachverstaendigengutachten prüfen.

**Verguetungsberechnung Dolmetscher und Übersetzer**

- `jveg-dolmetscher-uebersetzer` — Stundenverguetung, Mindestwartezeit, Anfahrt und schriftliche Übersetzung je Seite.

**Zeugenentschaedigung**

- `jveg-zeugenentschaedigung` — Fahrtkosten, Zeitversaeumnis und Verdienstausfall für Zeugen.
- `jveg-verdienstausfall-haushalt-zeit` — Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG.

**Kostenpositionen**

- `jveg-fahrtkosten` — Fahrtkosten: eigenes Fahrzeug, oeff. Verkehrsmittel, Flug.
- `jveg-uebernachtung-aufwand` — Uebernachtungs- und Verpflegungskosten nach § 6 JVEG.
- `jveg-sonstige-aufwendungen-belege` — Sonstige Aufwendungen nach § 7 JVEG mit Belegpflicht.

**Antrag, Vorschuss und Rechtsmittel**

- `jveg-vorschuss` — Vorschuss nach § 3 JVEG: Voraussetzungen, Formerfordernis, Verfahren.
- `jveg-antragsgenerator` — Verguetungsantrag, Anlagen und Fristen für die gerichtliche Kostenfestsetzung.
- `jveg-gerichtsschreiben-pruefung` — Gerichtsschreiben zur Kostenkuerzung rechtlich prüfen und widersprechen.
- `jveg-festsetzung-beschwerde` — Beschwerde gegen Kostenfestsetzungsbeschluss nach § 4 Abs. 3 JVEG.

**Qualitaetssicherung**

- `jveg-quality-gate` — Vollstaendigkeits- und Konsistenzpruefung aller Kostenpositionen vor Einreichung.

## Worauf besonders achten

- **Dreimonatsfrist ist Ausschlussfrist** — § 2 Abs. 1 JVEG kennt keine automatische Verlaengerung; nach Ablauf ist der Anspruch erloschen.
- **Belegpflicht für Aufwendungen** — Sonstige Aufwendungen nach § 7 JVEG werden ohne Beleg nicht erstattet; Porto und Kopien müssen belegt sein.
- **§ 8a JVEG ist kein Automatismus** — Kuerzung oder Wegfall setzt Verschulden und Kausalitaet voraus; ein verspaetendes Gutachten fuehrt nicht zwingend zum Verguetungsverlust.
- **KI-Nutzung deklarieren** — Gerichte verlangen zunehmend Offenlegung des KI-Einsatzes; fehlende Deklaration kann Gutachtenwert beeinflussen und Verguetungsstreit ausloesen.
- **Honorargruppe korrekt einordnen** — Falsche Einordnung in Anlage 1 JVEG fuehrt zur Kuerzung; Sachgebiet und Schwierigkeitsgrad des Gutachtens bestimmen die Gruppe.

## Typische Fehler

- Sachverstaendiger stellt Vorschussantrag, aber das Gericht hat keine Vorschussanforderung gestellt; Verfahrensfehler.
- Zeuge beantragt Vergütung nach drei Monaten; Anspruch ist erloschen.
- Fahrtkosten werden mit privatem Pkw abgerechnet, obwohl guenstigeres Bahnticket zumutbar war.
- Sachverstaendiger ordnet sich selbst in eine hoehere Honorargruppe ein, ohne Begrunndung; Gericht kuerzt auf naechste Gruppe.
- Widerspruch gegen Kuerzung wird als formelle Beschwerde nach § 4 Abs. 3 JVEG eingereicht, obwohl Beschwerdesumme unterschritten ist.

## Quellen und Aktualitaet

- Stand: 05/2026
- JVEG in der geltenden Fassung. Quelle: https://www.gesetze-im-internet.de/jveg/
- Anlage 1 JVEG (Honorargruppen und Stundensaetze) in der durch das Kosten- und Betreuungsrechtsaenderungsgesetz 2025 (KostRAeG 2025) zum 01.06.2025 geaenderten Fassung; pauschale Erhoehung der Sachverstaendigen-Stundensaetze um 9 Prozent (nur für Auftraege ab 01.06.2025). Synopse: https://ifsforum.de/fileadmin/user_upload/Aktuelles/Synopse_JVEG__2025.pdf
- Saetze für Zeugen (§§ 19 bis 22 JVEG) durch KostRAeG 2025 unveraendert; Kilometerpauschale Zeugen 0,35 EUR (§ 5 Abs. 2 JVEG), Sachverstaendige 0,42 EUR (§ 5 Abs. 1 JVEG).
