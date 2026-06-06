---
name: anschluss-router
description: "Einstieg, Schnelltriage und Fallrouting im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Fluggastrechte — Allgemein

## Arbeitsbereich

Einstieg, Schnelltriage und Fallrouting im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: VO 261/2004 keine Anmeldefrist, Verjährung 3 Jahre § 195 BGB, MontÜ Art. 35 zweijährige Ausschlussfrist, Anzeige Gepäckschaden 7/21 Tage Art. 31 MontÜ.
- Tragende Normen verifizieren: EU-Fluggastrechte-VO 261/2004 Art. 5, 6, 7, 8, 9, EU-VO 2027/97 (Montrealer Übereinkommen), MontÜ Art. 17, 19, 22, BGB §§ 631, 651a ff. (Pauschalreise), LuftVG, AGB der Luftfahrtunternehmen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Fluggast, Luftfahrtunternehmen (EU-Carrier / Non-EU), Reisebüro, SÖP (Schlichtungsstelle Öffentlicher Personenverkehr), LBA (Luftfahrt-Bundesamt), AG/LG am Sitz des Carriers oder Abflug/Ankunft.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Buchungsbestätigung, Boardingpass, Verspätungsbestätigung, Foto Anzeigetafel, Abrechnung Auslagen, Ablehnungsschreiben, Klageschrift AG, SÖP-Antrag — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fluggastrechte**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspaetung prüfen außergewoehnliche Umstaende Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden.

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
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter… |
| `annullierung-oder-verspaetung-einordnen` | Einordnung des Stoerungsereignisses als Annullierung (Art. 5 VO 261/2004), Verspaetung (Art. 6 nach Sturgeon-Linie) oder Nichtbefoerderung (Art. 4). |
| `anschlussflug-und-reiseplan` | Berechnung bei Verbindungsfluegen; Endziel-Verspaetung nach EuGH-Linie (Folkerts u.a.) massgeblich. |
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
- **Sturgeon-Linie** — EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 — bei Ankunftsverspaetung am Endziel von 3+ Stunden gleicher Ausgleichsanspruch wie bei Annullierung (curia.europa.eu).

## Rechtsgrundlagen

- Art. 3 VO (EG) 261/2004 — Anwendungsbereich (EU-Abflug oder EU-Ankunft mit EU-Carrier)
- Art. 4 VO (EG) 261/2004 — Nichtbefoerderung
- Art. 5 VO (EG) 261/2004 — Annullierung
- Art. 6 VO (EG) 261/2004 — Verspaetung
- Art. 7 VO (EG) 261/2004 — Ausgleichszahlung (250/400/600 EUR)
- § 23 Nr. 1 GVG — sachliche Zustaendigkeit Amtsgericht bis 10.000 EUR (seit 01.01.2026)

Zentrale EuGH-Entscheidungen (Stand Mai 2026; jeweils Volltext in curia.europa.eu vor Versand aufrufen):

- EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 (Sturgeon u.a.) — 3-Stunden-Schwelle
- EuGH, Urt. v. 23.10.2012, C-581/10 und C-629/10 (Nelson u.a.) — Bestaetigung Sturgeon
- EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — technische Defekte kein außergewöhnlicher Umstand
- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspaetung bei Anschlussfluegen
- EuGH, Urt. v. 4.5.2017, C-315/15 (Pesková) — Vogelschlag als außergewöhnlicher Umstand
- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener) — einheitliche Buchung in Drittstaat
- EuGH, Urt. v. 21.12.2021, C-146/20, C-188/20, C-196/20 — Vorverlegung als Annullierung
- EuGH, Urt. v. 16.5.2024, C-405/23 — Personalmangel Flughafen
- EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung bestaetigend
- EuGH, Urt. v. 13.6.2025, C-411/23 — versteckter Konstruktionsfehler Triebwerk
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag

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
- `ausnahmen-aussergewoehnliche-umstaende-pruefen` — Pruefung Art. 5 Abs. 3 VO 261/2004 mit aktuellem EuGH-Katalog.
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

## Quellen und Aktualitaet (Stand Mai 2026)

- VO (EG) Nr. 261/2004 in geltender Fassung
- § 23 Nr. 1 GVG: Streitwertgrenze 10.000 EUR seit 01.01.2026
- EuGH-Rechtsprechung (verifiziert mit curia.europa.eu, Auszug):
 - C-402/07 / C-432/07 (Sturgeon, 19.11.2009) — 3-Stunden-Schwelle
 - C-549/07 (Wallentin-Hermann, 22.12.2008) — technischer Defekt kein außergewöhnlicher Umstand
 - C-11/11 (Folkerts, 26.2.2013) — Endziel-Verspätung bei Anschlussfluegen
 - C-315/15 (Pesková, 4.5.2017) — Vogelschlag
 - C-537/17 (Wegener, 31.5.2018) — einheitliche Buchung Drittstaat
 - C-146/20, C-188/20, C-196/20 (21.12.2021) — Vorverlegung als Annullierung
 - C-405/23 (16.5.2024) — Personalmangel Flughafen
 - C-394/23 (9.1.2025) — Vorverlegung bestaetigend
 - C-411/23 (13.6.2025) — versteckter Konstruktionsfehler
 - C-399/24 (16.10.2025) — Blitzschlag
- Leitlinien der Kommission zur Auslegung VO 261/2004: ABl. EU C 2024/05687

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
