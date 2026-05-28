---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Fluggastrechte — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fluggastrechte**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspaetung prüfen außergewoehnliche Umstaende Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden.

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
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter… |
| `annullierung-oder-verspaetung-einordnen` | Ordnet das Stoerungsereignis rechtlich ein — Annullierung (Art. 5 VO 261/2004) Verspaetung (Art. 6 VO 261/2004 plus EuGH-Sturgeon-Rechtsprechung) Nichtbefoerderung wegen Overbooking (Art. 4 VO 261/2004) oder reine… |
| `anschlussflug-und-reiseplan` | Behandelt Reiseplaene mit Anschlussfluegen (Connecting Flights) und mehreren Etappen. Massgeblich ist die Ankunftsverspaetung am Endziel der Reise (EuGH C-11/11 Folkerts und C-559/16 Wegener). Prüfraster eine Buchung… |
| `ausnahmen-aussergewoehnliche-umstaende-pruefen` | Prüft die Einrede außergewoehnliche Umstaende nach Art. 5 Abs. 3 VO 261/2004. Differenziert zwischen Wetter Vulkanasche Vogelschlag Streik Flugsicherung Streik der eigenen Mitarbeiter wilder Streik technischem Defekt… |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich… |
| `fluggastrechte-anlagen-bauen` | Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Mahnung Klage) die Belege Buchungsbestätigung Boardingpass… |
| `fluggastrechte-kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klaert Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und… |
| `forderungsschreiben-erste-stufe` | Erstes Forderungsschreiben an die Airline. Erfasst Anspruchsteller (alle Passagiere mit Vollmachten) Anspruchsgrundlage Art. 7 VO 261/2004 konkrete Berechnung Frist zur Zahlung (typisch zwei Wochen) Bankverbindung.… |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und… |
| `klage-amtsgericht-fluggast` | Klageentwurf zum Amtsgericht in Fluggastrechtsangelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bis zehntausend Euro (i. d. F. seit 01.01.2026). Örtlich wahlweise Abflughafen oder Zielflughafen… |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante… |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene… |

## Worum geht es?

Die Verordnung (EG) Nr. 261/2004 gibt Fluggaesten bei Annullierung, erheblicher Verspaetung (ab drei Stunden am Endziel nach EuGH-Sturgeon-Rechtsprechung) und Nichtbefoerderung wegen Ueberbuchung einen Ausgleichsanspruch von 250 bis 600 EUR pro Person gegen das ausfuehrende Luftfahrtunternehmen. Das Plugin deckt den vollstaendigen Mandatsablauf ab: von der Falldaten-Erfassung ueber die Berechnung der Ausgleichszahlung, die Pruefung von Airline-Ausreden, das Forderungsschreiben bis hin zur Klageschrift vor dem Amtsgericht.

Dieses Plugin richtet sich sowohl an Verbraucher, die ihre Ansprueche selbst geltend machen wollen, als auch an Anwalte, die Fluggaeste vertreten.

## Wann brauchen Sie diese Skill?

- Ihr Flug wurde annulliert oder Sie sind wegen Ueberbuchung nicht befoerdert worden und Sie wollen Ihre Ansprueche klaeren.
- Ihr Flug hatte Verspaetung und Sie wollen wissen, ob Sie mehr als drei Stunden am Endziel verspaetet angekommen sind.
- Die Airline hat Ihre Forderung mit einer Standardausrede (technischer Defekt, aussergewoehnliche Umstaende) abgelehnt und Sie wollen dagegen vorgehen.
- Sie vertreten mehrere Familienmitglieder und benoetigen Vollmachten fuer die Durchsetzung.
- Sie wollen eine Klageschrift fuer das Amtsgericht erstellen, nachdem aussergerichtliche Schritte erfolglos waren.

## Fachbegriffe (kurz erklaert)

- **Annullierung** — Streichung eines zuvor geplanten Fluges (Art. 5 VO 261/2004); unterscheidet sich rechtlich von einer Verspaetung.
- **Aussergewoehnliche Umstaende** — Ereignisse, die sich der Kontrolle des Luftfahrtunternehmens entziehen (Art. 5 Abs. 3 VO 261/2004); entlastet die Airline von der Ausgleichspflicht.
- **Grosskreisdistanz** — die fuer die Stufenberechnung der Ausgleichszahlung massgebliche Entfernung zwischen Abflug- und Zielflughafen.
- **Operating Carrier** — das tatsaechlich ausfuehrende Luftfahrtunternehmen; massgeblich fuer die Passivlegitimation, nicht das vermarktende Unternehmen bei Codeshare.
- **PNR** — Passenger Name Record (Buchungscode); identifiziert eine zusammenhaengende Buchung bei Verbindungsfluegen.
- **Sturgeon-Rechtsprechung** — EuGH C-402/07: Verspaetungen ab drei Stunden Ankunftsverspaetung am Endziel sind Annullierungen gleichgestellt.

## Rechtsgrundlagen

- Art. 3 VO (EG) 261/2004 — Anwendungsbereich (EU-Abflug oder EU-Ankunft mit EU-Carrier)
- Art. 4 VO (EG) 261/2004 — Nichtbefoerderung
- Art. 5 VO (EG) 261/2004 — Annullierung
- Art. 6 VO (EG) 261/2004 — Verspaetung
- Art. 7 VO (EG) 261/2004 — Ausgleichszahlung (250/400/600 EUR)
- § 23 Nr. 1 GVG — sachliche Zustaendigkeit Amtsgericht bis 10.000 EUR (seit 01.01.2026)
- EuGH C-402/07 (Sturgeon) — Verspaetung ab drei Stunden gleichgestellt
- EuGH C-11/11 (Folkerts) — Anschlussflug, Endziel-Verspaetung massgeblich

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Einzelperson oder Reisegruppe/Familie? Selbstmandat oder anwaltliche Vertretung?
2. Phase des Mandats bestimmen: Stoerungsereignis noch nicht eingeordnet (Annullierung vs. Verspaetung?), aussergerichtliche Phase oder Klage?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Verjaebrung der Ansprueche aus VO 261/2004 richtet sich nach nationalem Recht; in Deutschland 3 Jahre (§ 195 BGB) zum Jahresende.
5. Anschluss-Skill bestimmen: Nach Einordnung des Stoerungsereignisses Ausgleichszahlung berechnen, dann Forderungsschreiben.

## Skill-Tour (was gibt es hier?)

- `fluggastrechte-kaltstart-interview` — Ersteinrichtung des Plugins: Anwendungsrolle, Buchungskonvention und Profil anlegen.
- `ticket-und-fluginformationen-erfassen` — Falldaten aus Tickets und Buchungsbestaetigungen extrahieren und Fallakte anlegen.
- `annullierung-oder-verspaetung-einordnen` — Rechtliche Einordnung des Stoerungsereignisses nach Art. 4-6 VO 261/2004 und Sturgeon-Rechtsprechung.
- `distanz-und-ausgleich-berechnen` — Ausgleichszahlung nach Art. 7 VO 261/2004 berechnen (Grosskreis-Distanz, Staffelung 250/400/600 EUR).
- `ausnahmen-aussergewoehnliche-umstaende-pruefen` — Prueft die Einrede aussergewoehnlicher Umstaende (Art. 5 Abs. 3 VO 261/2004) mit EuGH-Pinpoints.
- `airline-standardausreden-pruefen` — Katalog typischer Airline-Ablehnungsgruende mit Gegenargumenten und EuGH-Rechtsprechungs-Pinpoints.
- `anschlussflug-und-reiseplan` — Berechnung bei Verbindungsfluegen: Endziel-Verspaetung nach EuGH Folkerts massgeblich.
- `vollmacht-familienmitglieder` — Vollmachten fuer Mitreisende erstellen, damit ein Hauptansprechpartner alle Ansprueche buendeln kann.
- `forderungsschreiben-erste-stufe` — Erstes Forderungsschreiben an die Airline mit Rechtsbegruendung und Fristsetzung.
- `forderungsschreiben-mahnung` — Zweite Stufe nach Ablauf der Erstfrist; Nachfrist, Verzugszinsen, Klageandrohung.
- `fluggastrechte-anlagen-bauen` — BeA-konformes Anlagenkonvolut (Buchungsbestaetigung, Boardingpass, E-Mails) fuer Schriftsaetze erstellen.
- `klage-amtsgericht-fluggast` — Vollstaendiger Klageschrift-Entwurf fuer das Amtsgericht mit Streitwert und EuGH-Begruendung.

## Worauf besonders achten

- **Operating Carrier identifizieren**: Bei Codeshare-Fluegen ist nicht das vermarktende Unternehmen, sondern der tatsaechliche Ausfuehrungs-Carrier passivlegitimiert; das Ticket nennt bisweilen nur den Verkaeufer.
- **Sturgeon-Dreistunden-Schwelle**: Die Verspaetung wird an der tatsaechlichen Ankunftszeit am Endziel gemessen — nicht an der Abflugverspaetung; der Zeitpunkt, zu dem die Passagiertuer geoeffnet wird, gilt als Ankunftszeit.
- **Anschlussflug unter einer PNR**: Wenn ein Anschlussflug verpaesst wird, zaehlt die Gesamtverspaetung am Endziel fuer den Ausgleich; separate PNRs begrenzen den Anspruch auf die jeweilige Strecke.
- **Aussergewoehnliche Umstaende begruendungspflichtig**: Die Airline muss sowohl das aussergewoehnliche Ereignis als auch die zumutbaren Gegenmassnahmen darlegen; pauschale Verweise genuegen nicht.
- **Verjaebrung**: Der Anspruch verjaehrt in drei Jahren nach § 195 BGB; auf Jahresende-Berechnung nach § 199 BGB achten.

## Typische Fehler

- Annullierung und lange Verspaetung werden nicht unterschieden: Beide koennen Ausgleichsansprueche ausloesen, aber die Beweislage ist unterschiedlich.
- Volle Ausgleichszahlung wird beansprucht, obwohl die Airline einen Ersatzflug mit kurzer Verspaetung angeboten hat: Art. 7 Abs. 2 VO 261/2004 sieht eine Halbierung vor.
- Forderungsschreiben ohne Bankverbindung: Airline kann nicht leisten; Verzug tritt erst mit konkreter Zahlungsmoeglichkeit ein.
- Umbuchungs-Voucher als Erfuellung akzeptiert: Ein Gutschein ersetzt den Baranspruch nicht, wenn der Passagier dem nicht ausdruecklich zugestimmt hat.
- Ansprueche von Mitreisenden ohne Vollmacht geltend gemacht: Prozessual fehlt dann die Ermaechtigung zur Einziehung fremder Forderungen.

## Querverweise

- `prozessrecht` — Wenn der Fluggast-Fall vor dem Amtsgericht wird und prozessrechtliche Fragen (Zustaendigkeit, Fristen, Mahnbescheid) auftauchen.
- `selbstvertreter-amtsgericht` — Wenn der Mandant ohne Anwalt klagen will und eine Orientierung fuer das Amtsgerichtsverfahren benoetigt.

## Quellen und Aktualitaet

- Stand: 05/2026
- VO (EG) Nr. 261/2004 in geltender Fassung
- § 23 Nr. 1 GVG: Streitwertgrenze 10.000 EUR seit 01.01.2026
- EuGH C-402/07 (Sturgeon), EuGH C-11/11 (Folkerts), EuGH C-559/16 (Wegener), EuGH C-257/14 (van der Lans), EuGH C-74/19 (Kruesemann)
