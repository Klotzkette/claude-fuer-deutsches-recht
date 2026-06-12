# Megaprompt: fluggastrechte

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 84 Skills des Plugins `fluggastrechte`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fluggastrechte VO 261/2004: ordnet Rolle (Fluggast, Fluggesellschaft, Reisevermittler),…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wu…
3. **anlagen-bauen** — Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsa…
4. **annullierung-schriftsatz-brief-memo-bausteine** — Annullierung: Schriftsatz-, Brief- und Memo-Bausteine im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer…
5. **ausgleich-internationaler-bezug-schnittstellen** — Ausgleich: Internationaler Bezug und Schnittstellen im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer i…
6. **aussergewoehnliche-umstaende** — Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung im Fluggastrechte: 1. Welche Rolle hat die fragende Person und…
7. **aussergewoehnliche-umstaende-strikt** — Streng auszulegende aussergewoehnliche Umstaende Art. 5 Abs. 3 VO 261: Wetter, Streik nicht eigener Mitarbeiter, gericht…
8. **distanz-interessen** — Distanz: Mehrparteienkonflikt und Interessenmatrix im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer is…
9. **distanz-und-ausgleich-berechnen** — Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und …
10. **erfassen-behoerden-gerichts-registerweg** — Erfassen: Behörden-, Gerichts- oder Registerweg im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist G…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fluggastrechte VO 261/2004: ordnet Rolle (Fluggast, Fluggesellschaft, Reisevermittler), markiert Frist (Verjährung 3 Jahre § 195 BGB), wählt Norm (VO (EG) 261/2004, Montrealer Übereinkommen, BGB §§ 631 ff.) und Zuständigkeit (LBA), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fluggastrechte** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abtretung-an-fluggastportal-spezial` — Abtretung AN Fluggastportal Spezial
- `airline-bonitaet-und-vollstreckung` — Airline Bonitaet und Vollstreckung
- `airline-standardausreden-annullierung` — Airline Standardausreden Annullierung
- `airline-standardausreden-pruefen` — Airline Standardausreden Pruefen
- `anlagen-bauen` — Anlagen Bauen
- `annullierung-oder-verspaetung-einordnen` — Annullierung Oder Verspaetung Einordnen
- `annullierung-schriftsatz-brief-memo-bausteine` — Annullierung Schriftsatz Brief Memo Bausteine
- `annullierung-schriftsatz-brief-und-memo-bausteine` — Annullierung Schriftsatz Brief und Memo Bausteine
- `anschluss-router` — Anschluss Router
- `anschlussflug-und-reiseplan` — Anschlussflug und Reiseplan
- `ausgleich-internationaler-bezug-schnittstellen` — Ausgleich Internationaler Bezug Schnittstellen
- `ausgleich-internationaler-bezug-und-schnittstellen` — Ausgleich Internationaler Bezug und Schnittstellen
- `ausnahmen-aussergewoehnliche-umstaende` — Ausnahmen Aussergewoehnliche Umstaende
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fluggastrechte sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: or_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fluggastrechte** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

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
- Sie vertreten mehrere Familienmitglieder und benoetigen Vollmachten für die Durchsetzung.
- Sie wollen eine Klageschrift für das Amtsgericht erstellen, nachdem aussergerichtliche Schritte erfolglos waren.

## Fachbegriffe (kurz erklaert)

- **Annullierung** — Streichung eines zuvor geplanten Fluges (Art. 5 VO 261/2004); unterscheidet sich rechtlich von einer Verspaetung.
- **Aussergewoehnliche Umstaende** — Ereignisse, die sich der Kontrolle des Luftfahrtunternehmens entziehen (Art. 5 Abs. 3 VO 261/2004); entlastet die Airline von der Ausgleichspflicht.
- **Grosskreisdistanz** — die für die Stufenberechnung der Ausgleichszahlung massgebliche Entfernung zwischen Abflug- und Zielflughafen.
- **Operating Carrier** — das tatsaechlich ausfuehrende Luftfahrtunternehmen; massgeblich für die Passivlegitimation, nicht das vermarktende Unternehmen bei Codeshare.
- **PNR** — Passenger Name Record (Buchungscode); identifiziert eine zusammenhaengende Buchung bei Verbindungsfluegen.
- **Sturgeon-Linie** — EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 — bei Ankunftsverspaetung am Endziel von 3+ Stunden gleicher Ausgleichsanspruch wie bei Annullierung (curia.europa.eu).

## Rechtsgrundlagen

- Art. 3 VO (EG) 261/2004 — Anwendungsbereich (EU-Abflug oder EU-Ankunft mit EU-Carrier)
- Art. 4 VO (EG) 261/2004 — Nichtbefoerderung
- Art. 5 VO (EG) 261/2004 — Annullierung
- Art. 6 VO (EG) 261/2004 — Verspaetung
- Art. 7 VO (EG) 261/2004 — Ausgleichszahlung (250/400/600 EUR)
- § 23 Nr. 1 GVG — sachliche Zuständigkeit Amtsgericht bis 10.000 EUR (seit 01.01.2026)

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

## Schritt-für-Schritt: Einstieg ins Plugin

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
- `vollmacht-familienmitglieder` — Vollmachten für Mitreisende erstellen, damit ein Hauptansprechpartner alle Ansprueche buendeln kann.
- `forderungsschreiben-erste-stufe` — Erstes Forderungsschreiben an die Airline mit Rechtsbegruendung und Fristsetzung.
- `forderungsschreiben-mahnung` — Zweite Stufe nach Ablauf der Erstfrist; Nachfrist, Verzugszinsen, Klageandrohung.
- `fluggastrechte-anlagen-bauen` — BeA-konformes Anlagenkonvolut (Buchungsbestaetigung, Boardingpass, E-Mails) für Schriftsaetze erstellen.
- `klage-amtsgericht-fluggast` — Vollstaendiger Klageschrift-Entwurf für das Amtsgericht mit Streitwert und EuGH-Begruendung.

## Worauf besonders achten

- **Operating Carrier identifizieren**: Bei Codeshare-Fluegen ist nicht das vermarktende Unternehmen, sondern der tatsaechliche Ausfuehrungs-Carrier passivlegitimiert; das Ticket nennt bisweilen nur den Verkaeufer.
- **Sturgeon-Dreistunden-Schwelle**: Die Verspaetung wird an der tatsaechlichen Ankunftszeit am Endziel gemessen — nicht an der Abflugverspaetung; der Zeitpunkt, zu dem die Passagiertuer geoeffnet wird, gilt als Ankunftszeit.
- **Anschlussflug unter einer PNR**: Wenn ein Anschlussflug verpaesst wird, zaehlt die Gesamtverspaetung am Endziel für den Ausgleich; separate PNRs begrenzen den Anspruch auf die jeweilige Strecke.
- **Aussergewoehnliche Umstaende begruendungspflichtig**: Die Airline muss sowohl das aussergewoehnliche Ereignis als auch die zumutbaren Gegenmassnahmen darlegen; pauschale Verweise genuegen nicht.
- **Verjaebrung**: Der Anspruch verjaehrt in drei Jahren nach § 195 BGB; auf Jahresende-Berechnung nach § 199 BGB achten.

## Typische Fehler

- Annullierung und lange Verspaetung werden nicht unterschieden: Beide koennen Ausgleichsansprueche ausloesen, aber die Beweislage ist unterschiedlich.
- Volle Ausgleichszahlung wird beansprucht, obwohl die Airline einen Ersatzflug mit kurzer Verspaetung angeboten hat: Art. 7 Abs. 2 VO 261/2004 sieht eine Halbierung vor.
- Forderungsschreiben ohne Bankverbindung: Airline kann nicht leisten; Verzug tritt erst mit konkreter Zahlungsmoeglichkeit ein.
- Umbuchungs-Voucher als Erfuellung akzeptiert: Ein Gutschein ersetzt den Baranspruch nicht, wenn der Passagier dem nicht ausdruecklich zugestimmt hat.
- Ansprueche von Mitreisenden ohne Vollmacht geltend gemacht: Prozessual fehlt dann die Ermaechtigung zur Einziehung fremder Forderungen.

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

---

## Skill: `anlagen-bauen`

_Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Mahnung Klage) die Belege Buchungsbestätigung Boardingpass Annullierungsbestätigung E-Mail-Verkehr Quittungen. Konvertiert alles nach PDF nummeriert in d..._

# Fluggastrechte — Anlagen bauen

## Eingaben

- **Schriftsatz** (PDF oder DOCX) — das vom vorhergehenden Skill erzeugte Forderungsschreiben, die Mahnung oder die Klage.
- **Belege-Ordner** mit den Beweisstücken in beliebigem Format:
 - PDF (Buchungsbestätigung, Annullierungsbestätigung, Tickets)
 - DOCX (eigene Aufzeichnungen, Mandanten-Sachverhaltsdarstellung)
 - JPG / PNG (Boardingpass-Foto, Anzeigetafel-Foto, Quittungs-Foto)
 - EML / MSG (E-Mail-Korrespondenz mit der Airline)
- **Zielordner** für das Ergebnis (wird angelegt).
- **Bundle-Option** (`--bundle`): zusätzlich ein einziges PDF `Schriftsatz_mit_Anlagen.pdf` mit dem Schriftsatz vorne und allen Anlagen dahinter.

## Workflow

### Schritt 1 — Belege konvertieren

Alle Belege werden zunächst nach PDF normalisiert:

| Eingang | Verfahren |
|---|---|
| PDF | unverändert übernommen |
| JPG / PNG | Pillow legt das Bild auf eine A4-Seite mit 150 dpi |
| DOCX / EML / MSG / ODT / RTF / TXT / HTML | LibreOffice headless konvertiert nach PDF |

Fehlt LibreOffice oder Pillow, gibt der Skill eine konkrete Installations-Anweisung aus und lässt den Beleg in der Eingangsliste mit Warnung stehen.

### Schritt 2 — Anlagen aus dem Schriftsatz lesen

Der Skill liest den Schriftsatz und extrahiert alle Bezugnahmen vom Muster "Anlage K 1", "Anlage K2", "Anlage K 3a". Reihenfolge: die der **ersten Erwähnung im Schriftsatz** (BGH-Stil, nicht chronologisch). Wenn der Schriftsatz noch keine Anlagen-Nummern enthält, wird alphabetisch durchnummeriert — dann sollte der Schreiben-Skill in einem zweiten Lauf die Bezeichnungen im Schriftsatz nachtragen.

### Schritt 3 — Stempel oben rechts (Arial 12 fett)

Auf der ersten Seite jeder Anlage wird ein dezenter, aber deutlicher Stempel gesetzt:

- Position: rechter oberer Rand, ca. 1,5 cm vom oberen Seitenrand, ca. 1,5 cm vom rechten Seitenrand.
- Schrift: Arial 12 pt **fett** (in der reportlab-Basisschrift Helvetica-Bold).
- Format: `Anlage K 1`, `Anlage K 7`, `Anlage K 3a`.

Mehrseitige Anlagen erhalten den Stempel nur auf Seite 1.

### Schritt 4 — beA-konforme Dateinamen

Jede Einzelanlage wird unter einem Dateinamen abgelegt, der beA-kompatibel ist:

```
Anlage_K-01_Buchungsbestaetigung.pdf
Anlage_K-02_Boardingpass.pdf
Anlage_K-03_Email-Airline-Annullierung.pdf
Anlage_K-04_Quittung-Restaurant-Flughafen.pdf
Anlage_K-05_Taxiquittung.pdf
```

Regeln: keine Umlaute, kein scharfes ß, keine Leerzeichen, Nummer zweistellig, maximal ca. 90 Zeichen.

### Schritt 5 — Konvolut + Anlagenverzeichnis

Im Zielordner entstehen:

```
konvertiert/ Zwischenstand der konvertierten Belege
gestempelt/ Einzelanlagen mit Stempel, beA-konform benannt
Anlagenkonvolut.pdf alle Anlagen, mit Lesezeichen pro Anlage
Anlagenverzeichnis.md tabellarische Übersicht (Anlage / Beschreibung / Seiten)
Anlagenverzeichnis.pdf gleiche Tabelle als PDF
```

### Schritt 6 — Optional: Schriftsatz-mit-Anlagen-Bundle

Mit `--bundle` legt der Skill **zusätzlich** `Schriftsatz_mit_Anlagen.pdf` an: der Schriftsatz vorne, dann das Konvolut, durchlaufende Lesezeichen. Genau das spart den Mandanten den letzten Schritt der Zusammenstellung, wenn er das Ganze einreichen oder per Post schicken will.

## Werkzeug

`werkzeuge/build_fluggast_anlagen.py`. Aufruf-Beispiel:

```bash
### Forderungsschreiben mit Belegen
python3 werkzeuge/build_fluggast_anlagen.py \
 --belege ./mandat-mueller/belege \
 --schriftsatz ./mandat-mueller/forderungsschreiben.pdf \
 --ausgang ./mandat-mueller/anlagen \
 --titel "Forderungsschreiben Erste Stufe"

### Klage mit gebundeltem Schriftsatz + Anlagen
python3 werkzeuge/build_fluggast_anlagen.py \
 --belege ./mandat-mueller/belege \
 --schriftsatz ./mandat-mueller/klage.pdf \
 --ausgang ./mandat-mueller/anlagen \
 --titel "Klage Amtsgericht Hamburg" \
 --bundle
```

Abhängigkeiten: `pypdf`, `reportlab`, optional `Pillow` (für Bild-Konvertierung), optional LibreOffice (für DOCX/EML).

## Rückfragen, falls etwas fehlt

Der Skill stoppt mit einer klaren Frage zurück an den Mandanten / die Sekretariatskraft, wenn:

- der Belege-Ordner leer ist (Frage: "Welche Belege liegen vor und in welchem Format? Bitte alle in den Ordner kopieren, auch Fotos und E-Mails.");
- der Schriftsatz weder PDF noch DOCX ist (Frage: "Liegt der Schriftsatz als PDF vor? Wenn er noch in der Mahnung-Skill-Vorschau steht, bitte erst dort als PDF exportieren.");
- mehr Anlagen im Schriftsatz benannt sind, als Belege im Ordner liegen (Frage: "Der Schriftsatz nennt Anlage K 5, im Ordner sind aber nur 4 Dateien — welcher Beleg fehlt?");
- ein Beleg im Ordner liegt, der im Schriftsatz nicht erwähnt wird (Hinweis: "Beleg X wird im Schriftsatz nicht zitiert. Soll er trotzdem als zusätzliche Anlage angehängt werden, oder weggelassen?").

## Was dieser Skill bewusst NICHT tut

- **Keine inhaltliche Schwärzung** (Kontonummern, Personalausweis-Daten, fremde Passagierdaten auf Boardingpässen). Wenn die Anlage geschwärzt werden muss, wird das vor diesem Skill manuell erledigt.
- **Keine OCR-Vollerkennung.** Das Werkzeug liest nur den Schriftsatz, um Anlagen-Nummern zu finden — es liest die Belege nicht inhaltlich aus.
- **Keine elektronische Signatur** und **kein automatisches beA-Hochladen.** Das macht der Mandant oder die Kanzlei selbst.
- **Keine Echtheitsprüfung** der Belege.

## Beispiele typischer Nutzerformulierungen, die diesen Skill auslösen

- "Bitte die Belege aus dem Ordner ./belege als Anlagen K 1 bis K 5 zum Forderungsschreiben aufbereiten."
- "Erstelle ein Anlagenkonvolut für die Klage, alles in einem PDF."
- "Stemple meine Belege als Anlagen und benenne sie beA-konform."
- "Mach aus dem Schriftsatz und den Belegen ein einziges PDF zum Einreichen."

## Übergabe

Die Schreiben-Skills (`forderungsschreiben-erste-stufe`, `forderungsschreiben-mahnung`, `klage-amtsgericht-fluggast`) rufen diesen Skill **automatisch** am Ende ihrer Arbeit auf, sobald ein Belege-Ordner im Mandatsverzeichnis vorhanden ist. Der Nutzer kann das mit der Option "Anlagen separat lassen" abwählen.

## Leitentscheidungen Anlagen / Schriftsatz

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)

---

## Skill: `annullierung-schriftsatz-brief-memo-bausteine`

_Annullierung: Schriftsatz-, Brief- und Memo-Bausteine im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch? 4. Wel..._

# Annullierung: Schriftsatz-, Brief- und Memo-Bausteine

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Annullierung: Schriftsatz-, Brief- und Memo-Bausteine
- **Normen-/Quellenanker:** VO, EG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Annullierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 71 GVG
- § 29 VwVfG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- Art. 13 DSGVO
- § 14 UKlaG

### Leitentscheidungen

- EuGH C-402/07
- EuGH C-549/07
- EuGH C-204/08
- EuGH C-394/23
- EuGH C-188/20

---

## Skill: `ausgleich-internationaler-bezug-schnittstellen`

_Ausgleich: Internationaler Bezug und Schnittstellen im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch? 4. Welch..._

# Ausgleich: Internationaler Bezug und Schnittstellen

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Ausgleich: Internationaler Bezug und Schnittstellen
- **Normen-/Quellenanker:** VO, EG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ausgleich** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `aussergewoehnliche-umstaende`

_Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch? 4...._

# Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung
- **Normen-/Quellenanker:** VO, EG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aussergewoehnliche** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `aussergewoehnliche-umstaende-strikt`

_Streng auszulegende aussergewoehnliche Umstaende Art. 5 Abs. 3 VO 261: Wetter, Streik nicht eigener Mitarbeiter, gerichtlich verfuegte Flugverbote, Wildschlag in Triebwerk. Keine aussergewoehnlichen Umstaende: technische Defekte (EuGH Wallentin-Hermann), Krankheit Crew, ATC-Engpaesse mit Routine...._

# Aussergewoehnliche Umstaende

## Spezialwissen: Aussergewoehnliche Umstaende
- **Normen-/Quellenanker:** Art. 5, VO, ATC.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `distanz-interessen`

_Distanz: Mehrparteienkonflikt und Interessenmatrix im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch? 4. Welche..._

# Distanz: Mehrparteienkonflikt und Interessenmatrix

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Distanz: Mehrparteienkonflikt und Interessenmatrix
- **Normen-/Quellenanker:** VO, EG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Distanz** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `distanz-und-ausgleich-berechnen`

_Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich oder 1500 bis 3500 km nicht-innergemeinschaftlich / 600 EUR mehr als 3500 km nich..._

# Distanz und Ausgleichszahlung berechnen

## Norm

Art. 7 VO 261/2004 — Ausgleichsanspruch in drei Stufen:

| Stufe | Distanz | Höhe pro Passagier |
|---|---|---|
| 1 | bis 1500 km | 250 EUR |
| 2 | mehr als 1500 km innergemeinschaftlich | 400 EUR |
| 2 | 1500 bis 3500 km nicht-innergemeinschaftlich | 400 EUR |
| 3 | mehr als 3500 km nicht-innergemeinschaftlich | 600 EUR |

## Distanzberechnung

- **Großkreisrechnung** (Great Circle Distance) zwischen Abflug- und Zielflughafen.
- IATA-Standardkoordinaten der Flughaefen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anschlussflug über Drittstaat als Umweg zählt nicht (Direktverbindungs-Maßstab).

## Begriff innergemeinschaftlich vs nicht-innergemeinschaftlich

- **Innergemeinschaftlich** Flug zwischen zwei Flughaefen die in der EU liegen.
- **Nicht-innergemeinschaftlich** mindestens ein Flughafen außerhalb der EU.
- **Sondergebiete** Kanaren Madeira Azoren EU-Außengebiete EU-Recht gilt (innergemeinschaftlich).
- **Norwegen Schweiz Island Liechtenstein** mehrere bilaterale Abkommen — beachten ob VO 261/2004 anwendbar.

## Beispielberechnungen

- **Berlin (BER) — Madrid (MAD)** ca. 1872 km innergemeinschaftlich → Stufe 2 → 400 EUR
- **München (MUC) — Lissabon (LIS)** ca. 2280 km innergemeinschaftlich → Stufe 2 → 400 EUR
- **Frankfurt (FRA) — Mallorca (PMI)** ca. 1245 km innergemeinschaftlich → Stufe 1 → 250 EUR
- **Hamburg (HAM) — New York (JFK)** ca. 6125 km nicht-innergemeinschaftlich → Stufe 3 → 600 EUR
- **Wien (VIE) — Dubai (DXB)** ca. 4275 km nicht-innergemeinschaftlich → Stufe 3 → 600 EUR

## Halbierungsregel (Art. 7 Abs. 2 VO 261/2004)

Die Airline kann den Ausgleich **um 50 Prozent kuerzen** wenn dem Fluggast eine **anderweitige Beförderung** angeboten wurde **und** die tatsächliche Ankunftszeit am Endziel nicht überschreitet:

- Bei Distanz **bis 1500 km** die geplante Ankunftszeit um **mehr als zwei Stunden**.
- Bei Distanz **1500 bis 3500 km nicht-innergemeinschaftlich oder über 1500 km innergemeinschaftlich** die geplante Ankunftszeit um **mehr als drei Stunden**.
- Bei Distanz **mehr als 3500 km nicht-innergemeinschaftlich** die geplante Ankunftszeit um **mehr als vier Stunden**.

Folge: Stufe 1 → 125 EUR; Stufe 2 → 200 EUR; Stufe 3 → 300 EUR.

## Mehrere Passagiere

- **Eigenständiger Anspruch pro Passagier** (Art. 7 VO 261/2004 ist persönlich).
- **Auch Kinder** mit eigener Beförderung (eigenes Ticket) haben den vollen Anspruch — auch bei Kindertarif.
- **Babys ohne eigenen Sitzplatz** (Lap-Infant) haben i. d. R. keinen eigenen Ausgleichsanspruch wenn nicht gesondert befoerdert.

## Nebenforderungen

- **Verzugszinsen** ab Mahnung (§§ 286 288 BGB) — Verbraucher 5 Prozentpunkte über Basiszinssatz.
- **Auslagen** wenn Verbraucher selbst Auslagen getragen hat (Hotel Verpflegung Telefon) bei verletzter Betreuungspflicht (Art. 9 VO 261/2004) — separat zur Ausgleichszahlung.

## Pauschalreise

- Bei Pauschalreise greifen zusätzliche Ansprueche gegen den Reiseveranstalter nach §§ 651a ff. BGB.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

```
Berechnung Ausgleich
Fall-ID: FG-2026-0042
Flug: LH 1234 MUC-LIS
Distanz: 2280 km (innergemeinschaftlich)
Stufe: 2 (mehr als 1500 km innergemeinschaftlich)
Ausgleich pro Passagier: 400 EUR
Anzahl Passagiere: 3
Gesamtausgleich: 1200 EUR

Halbierungsregel prüfen:
- Ersatzflug am 13.05.2026 LH 1234
- Tatsächliche Ankunft 13.05.2026 12:00 statt geplant 12.05.2026 11:00
- Verspätung: 25 Stunden über drei Stunden → keine Halbierung
- → 1200 EUR Anspruch in voller Hoehe
```

## Leitentscheidungen Distanz und Ausgleich

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Hinweise

- Beweislast für Distanzangaben liegt nicht beim Fluggast (Standard-Flugplandaten frei zugänglich).
- Bei strittiger Distanz: Gericht stellt anhand IATA-Daten fest.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)

---

## Skill: `erfassen-behoerden-gerichts-registerweg`

_Erfassen: Behörden-, Gerichts- oder Registerweg im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch? 4. Welche Do..._

# Erfassen: Behörden-, Gerichts- oder Registerweg

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 535 Abs. 1 BGB` — Hauptpflichten des Mietvertrags.
- `§ 536 Abs. 1 BGB` — Minderung.
- `§ 543 Abs. 1 BGB` — ausserordentliche Kuendigung.
- `§ 556 Abs. 1 BGB` — Betriebskostenvereinbarung.
- `§ 556 Abs. 3 BGB` — Abrechnung und Einwendungsfrist.
- `§ 558 Abs. 1 BGB` — Mieterhoehung bis ortsuebliche Vergleichsmiete.
- `§ 559 Abs. 1 BGB` — Modernisierungsmieterhoehung.
- `§ 573 Abs. 1 BGB` — ordentliche Vermieterkuendigung.
- `§ 259 BGB` — Rechnungslegung.
- `§ 2 BetrKV` — Betriebskostenarten.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Erfassen: Behörden-, Gerichts- oder Registerweg
- **Normen-/Quellenanker:** VO, EG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Erfassen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

