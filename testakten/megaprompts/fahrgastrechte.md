# Megaprompt: fahrgastrechte

## Zusammensetzung

Dieser Megaprompt enthaelt alle 13 Skills des Plugins `fahrgastrechte`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Fahrgastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wu…
2. **anlagen-bauen** — Baut aus den Belegen eines Fahrgastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsa…
3. **db-ablehnungsgruende-pruefen** — Katalog typischer Ablehnungsgruende des DB-Servicecenters Fahrgastrechte mit Gegenargumenten und Pinpoint auf Art. 18 un…
4. **eigenbefoerderung-und-betreuung-art-18** — Pruefraster für Selbstbefoerderung des Fahrgasts (Art. 18 Abs. 3 Unterabs. 2 VO 2021/782 mit 100-Minuten-Frist) und Hilf…
5. **einfuehrung-vo-2021-782** — Einfuehrung VO (EU) 2021/782 Fahrgastrechte Eisenbahn. Anwendungsbereich Art. 2 (auch SPNV mit Ausnahmen § 2 EVO), Begri…
6. **entschaedigung-berechnen** — Berechnet die Entschaedigung nach Art. 19 VO (EU) 2021/782. Zwei Stufen 25 Prozent (ab 60 Minuten Endziel-Verspaetung) u…
7. **forderung-an-db-erste-stufe** — Erstes Forderungsschreiben an das DB-Servicecenter Fahrgastrechte. Erfasst Anspruchsteller (alle Reisenden mit Vollmacht…
8. **klage-amtsgericht-fahrgast** — Klageentwurf zum Amtsgericht in Fahrgastrechte-Angelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bi…
9. **schlichtung-reise-verkehr-anrufen** — Schlichtungsantrag bei der Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) nach erfolgloser Reklamation beim Eisen…
10. **ticket-und-reisedaten-erfassen** — Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestaetigungen Reservierungen Foto-Belegen für Fahrgastrechte-Ma…
11. **verspaetung-und-anschlussverlust-einordnen** — Ordnet das Stoerungsereignis rechtlich ein: Verspaetung (Art. 19 VO 2021/782 bei mindestens 60 Min Endziel), Zugausfall …
12. **vollmacht-mitreisende** — Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde Reisegruppe) damit ein Hauptansprechpartner deren Fahrga…
13. **widerspruch** — Erstellt einen formellen Widerspruchsbrief gegen die Ablehnung eines Fahrgastrechte-Antrags der Deutschen Bahn oder eine…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Fahrgastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenstaendig:..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fahrgastrechte** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **fahrgastrechte**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Fahrgastrechte im Eisenbahnverkehr selber geltend machen — VO (EU) 2021/782 plus EVO 2023. Tickets erfassen, Verspätung vs. Zugausfall einordnen, Entschädigung berechnen (25/50 Prozent ab 60/120 Minuten), Forderung an die DB, Widerspruch gegen Ablehnung, Schlichtungsstelle Reise & Verkehr e.V. (vormals söp — Schlichtungsstelle für den öffentlichen Personenverkehr) und Klage zum Amtsgericht. Vollmacht für Mitreisende. Katalog typischer DB-Ablehnungsgründe.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Buchungsbestätigung, Ticket, Reservierungsbeleg, Ablehnungsschreiben der DB, Verspätungs-Bestätigung, Korrespondenz, Klageschrift, Schlichtungsspruch, Tabelle, Foto-Beleg, Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Aktenzeichen / Vorgangsnummer DB, Adressat, Datum und erkennbaren Lebenssachverhalt (Strecke, Datum, Zugnummer, Verspätung).
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet oder Arbeitsmodus zu — Art. 18/19 VO 2021/782, § 11 EVO, Widerspruch, Klage, Schlichtung.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Vorgangsnummer falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Reisende:r selbst, Familienangehörige:r mit Vollmacht, Anwalt, Verbraucherzentrale? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Erstforderung an DB, Widerspruch gegen Ablehnung, Schlichtungsantrag, Klage, Memo? | Output sofort sauber ausrichten. |
| Sachverhalt | Welche Strecke, welcher Zug, welche Verspätung am Zielort, welche Ticketart, welches Datum? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Ablehnungs-Datum, Verjährungs-Annäherung, gerichtliche Frist, Vorgangs-Status? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Belege liegen vor: Ticket, Buchungsbestätigung, Ablehnungsschreiben, Verspätungs-Bestätigung, Korrespondenz, Kostenbelege Verpflegung/Taxi/Hotel? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Verjährung, Klagekosten, abweisende DB-Argumentation, Beweislücken? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Verjährung (drei Jahre nach § 195 BGB ab Jahresende), Bearbeitungsfristen der DB (Art. 18 Abs. 5, 19 Abs. 7 VO 2021/782 — 30 Tage / ein Monat), Anhängige Schlichtung.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Erstforderung, Widerspruch, Schlichtung, Klage, Vollmacht.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Forderungsschreiben, Widerspruch oder eine Klage gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn die Rechtslage aktuell sein kann (neue EuGH/BGH-Rechtsprechung zu VO 2021/782), ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Verjährung sichern, Sachverhalt ordnen, nächster Fachmodul.

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
| `fahrgastrechte-einfuehrung-vo-2021-782` | Wenn Mandant Grundlagen-Erklärung zur EU-VO und ihrem Anwendungsbereich braucht (60/120-Min-Schwellen, Sturgeon-Äquivalent, Art. 18/19/20). |
| `ticket-und-reisedaten-erfassen` | Wenn Tickets, Buchungsbestätigungen oder Beweis-Belege hochgeladen oder geschildert werden — extrahiert Fallakte. |
| `verspaetung-und-anschlussverlust-einordnen` | Wenn unklar ist, ob Verspätung, Zugausfall, Anschlussverlust oder Vorverlegung vorliegt — Differenzierung Art. 17 / Art. 18 VO. |
| `entschaedigung-berechnen` | Berechnet 25/50 % auf Basis Ticketart (Flexpreis, Sparpreis, BC100, Deutschlandticket, Zeitkarte) — pro Person, ggf. Mehrpassagiere. |
| `eigenbefoerderung-und-betreuung-art-18` | Wenn Mandant Taxi/Bus/anderer Anbieter genutzt hat, Hotel buchte oder Verpflegung kaufte — Art. 18 Abs. 3, 20 VO und § 11 EVO. |
| `forderung-an-db-erste-stufe` | Erstforderungsschreiben an Servicecenter Fahrgastrechte mit Rechtsbegründung und Frist. |
| `fahrgastrechte-widerspruch` | Wenn DB den Antrag abgelehnt hat — strukturierter Widerspruch mit Pinpoint auf konkreten Ablehnungsgrund und Art. 19 VO. |
| `db-ablehnungsgruende-pruefen` | Katalog der zehn häufigsten DB-Ablehnungsgründe mit Gegenargumenten und Norm-Pinpoint — vor jedem Widerspruchs- oder Klage-Entwurf konsultieren. |
| `schlichtung-reise-verkehr-anrufen` | Wenn DB auch nach Widerspruch ablehnt oder schweigt — Antrag an die Schlichtungsstelle Reise & Verkehr e.V. (vormals söp). |
| `klage-amtsgericht-fahrgast` | Wenn aussergerichtliche Schritte erfolglos waren — Klageschrift mit Streitwert, Antrag, Begründung, Beweisangeboten. |
| `vollmacht-mitreisende` | Wenn ein Hauptansprechpartner Ansprüche mehrerer Reisender bündeln will — Vollmachten erstellen. |
| `fahrgastrechte-anlagen-bauen` | Nach jedem Schriftsatz: erzeugt sortiertes Anlagenkonvolut mit "Anlage K"-Stempel und Sammel-PDF. |

## Worum geht es?

Die Verordnung (EU) 2021/782 (in Kraft seit 7. Juni 2023) gibt Fahrgästen im Eisenbahnverkehr bei Verspätung von 60 Minuten und mehr am Zielort einen Anspruch auf Entschädigung in Höhe von 25 % des Fahrpreises, ab 120 Minuten 50 %. Bei Zugausfall, verpasstem Anschluss oder absehbarer Verspätung über 60 Minuten bestehen zusätzlich Wahlrechte nach Art. 18 VO (Erstattung, Weiterreise, Selbstbeförderung nach 100 Minuten Wartezeit ohne Alternativangebot der Bahn).

Das Plugin deckt den vollständigen Mandatsablauf ab: vom Erfassen der Ticket- und Reisedaten über die Berechnung des Anspruchs, das Forderungsschreiben, den Widerspruch gegen eine Ablehnung des DB-Servicecenters, die Schlichtung bei der Schlichtungsstelle Reise & Verkehr bis zur Klage vor dem Amtsgericht.

## Wann dieses Modul hilft?

- Ihr Zug fiel aus oder war erheblich verspätet und Sie wollen Ihre Ansprüche klären.
- Sie haben ein Ablehnungsschreiben der DB erhalten und wollen Widerspruch einlegen.
- Sie haben Taxi-, Bus- oder Hotelkosten getragen, weil die DB keine zumutbare Alternative bot, und wollen Erstattung verlangen.
- Sie vertreten mehrere Mitreisende und benötigen Vollmachten.
- Sie wollen Klage zum Amtsgericht erheben, nachdem die DB und ggf. die Schlichtungsstelle Reise & Verkehr nicht entschieden haben.

## Fachbegriffe (kurz erklärt)

- **Operating EVU** — das tatsächlich ausführende Eisenbahnverkehrsunternehmen; maßgeblich für die Passivlegitimation. Bei DB-Tickets in der Regel DB Fernverkehr AG, DB Regio AG oder konkretes Konkurrenz-EVU wie ÖBB, FlixTrain, NWB, Vlexx.
- **PNR / Buchungscode** — identifiziert eine zusammenhängende Buchung; bei Anschlussfahrten innerhalb einer PNR greift Art. 12 Abs. 3 VO 2021/782 (Durchgangsfahrkarte → Endziel-Verspätung maßgeblich).
- **Sturgeon-Äquivalent im Eisenbahnverkehr** — der EuGH hat im Flugverkehrsrecht entschieden, dass auch erhebliche Verspätungen Ausgleichsansprüche auslösen. Für die Eisenbahn ist die 60-Min-Schwelle in Art. 19 VO 2021/782 ausdrücklich normiert (also kein Auslegungsschritt nötig).
- **SPNV** — Schienenpersonennahverkehr; bei reinen SPNV-Fahrten greift ergänzend § 11 EVO mit 20-Min-Schwelle und Höchstbetrag 120 EUR für Ersatzbeförderung.
- **Zugbindung** — bei Sparpreis-Tickets normalerweise gegeben, wird aber laut Ziffer 9 BB DB ab 20 Min absehbarer Verspätung **aufgehoben**. Praxisrelevant gegen die DB-Ablehnung "andere Verbindung genommen".

## Rechtsgrundlagen

- Art. 1, 2, 3 VO (EU) 2021/782 — Gegenstand, Anwendungsbereich, Begriffsbestimmungen
- Art. 7 VO (EU) 2021/782 — Verzichtsverbot (Beförderungsbedingungen dürfen Rechte nicht einschränken)
- Art. 12 VO (EU) 2021/782 — Durchgangsfahrkarten und verpasste Anschlüsse
- Art. 17 VO (EU) 2021/782 — Haftung für Verspätungen
- Art. 18 VO (EU) 2021/782 — Erstattung oder Weiterreise; 100-Min-Frist für Eigenbeförderung
- Art. 19 VO (EU) 2021/782 — Entschädigung (25/50 %)
- Art. 20 VO (EU) 2021/782 — Hilfeleistung (Verpflegung, Hotel, Transport bei ≥ 60 Min)
- Art. 27 VO (EU) 2021/782 — Beschwerderecht (3-Monats-Verfahrensfrist gegenüber EVU)
- §§ 1, 2 EVO — Anwendungsbereich, Verhältnis EU-VO/EVO
- § 6 EVO — Erhöhtes Beförderungsentgelt (Schwarzfahrer)
- § 11 EVO — Zusätzliche SPNV-Rechte bei Verspätung (20-Min-Schwelle, 120-EUR-Höchstbetrag)
- § 15 EVO — Schlichtungsstelle
- § 23 Nr. 1 GVG (i.d.F. seit 01.01.2026) — sachliche Zuständigkeit AG bis 10.000 EUR
- § 29 ZPO + Art. 7 Nr. 1 lit. b VO (EU) 1215/2012 (Brüssel-Ia) — örtliche Zuständigkeit
- § 195, § 199 Abs. 1 BGB — Verjährung drei Jahre

## Schritt-für-Schritt: Einstieg ins Plugin

1. **Mandantenkonstellation klären:** Einzelreisende:r oder Reisegruppe / Familie? Verbraucher-Selbstmandat oder anwaltliche Vertretung?
2. **Phase des Mandats bestimmen:** Vor Antrag bei DB? Antrag gestellt, noch keine Reaktion? Ablehnungsschreiben erhalten? Schlichtungsverfahren? Klage?
3. **Passenden Skill auswählen** (siehe Skill-Tour unten).
4. **Eilfristen prüfen:** Verjährung drei Jahre nach § 195 BGB ab Jahresende; Beschwerdefrist Art. 27 VO drei Monate (Verfahren); Bearbeitungsfrist DB 30 Tage / ein Monat.
5. **Anschluss-Skill bestimmen:** Nach Einordnung des Störungsereignisses Entschädigung berechnen, dann Forderungsschreiben — bei Ablehnung Widerspruch — bei weiterer Ablehnung Schlichtung — als letzter Schritt Klage.

## Skill-Tour (was gibt es hier?)

- `fahrgastrechte-einfuehrung-vo-2021-782` — Norm-Übersicht mit Anwendungsbereich, Schwellen, Hilfeleistungen, Befreiungstatbeständen.
- `ticket-und-reisedaten-erfassen` — Falldaten aus Tickets, Buchungsbestätigungen, Verspätungs-Bestätigungen extrahieren und Fallakte anlegen.
- `verspaetung-und-anschlussverlust-einordnen` — Einordnung als Verspätung, Zugausfall oder verpasster Anschluss; Endziel-Maßstab nach Art. 12 VO.
- `entschaedigung-berechnen` — 25/50 % nach Art. 19 VO; DB-Tarif-Pauschalen für BC100, Deutschlandticket, Zeitkarte.
- `eigenbefoerderung-und-betreuung-art-18` — Selbstbeförderung nach 100 Minuten, Verpflegung, Hotel, Transport.
- `forderung-an-db-erste-stufe` — Erstes Forderungsschreiben an Servicecenter Fahrgastrechte mit Rechtsgrundlagen.
- `fahrgastrechte-widerspruch` — Widerspruch gegen DB-Ablehnungsschreiben; zwingend mit Pinpoint auf konkreten Ablehnungsgrund.
- `db-ablehnungsgruende-pruefen` — Katalog der zehn häufigsten DB-Ablehnungen mit Gegenargumenten.
- `schlichtung-reise-verkehr-anrufen` — Schlichtungsantrag an die Schlichtungsstelle Reise & Verkehr e.V. (vormals söp).
- `klage-amtsgericht-fahrgast` — Vollständiger Klageschrift-Entwurf für das Amtsgericht.
- `vollmacht-mitreisende` — Vollmachten für Mitreisende erstellen.
- `fahrgastrechte-anlagen-bauen` — Sortiertes Anlagenkonvolut für Schriftsätze.

## Worauf besonders achten

- **Operating EVU identifizieren:** Bei FlixTrain, NWB oder ÖBB-Strecken ist nicht die DB Anspruchsgegnerin. Bei DB Fernverkehr-Tickets: DB Fernverkehr AG. Bei DB Regio: DB Regio AG bzw. zuständige Tochter.
- **60-Min-Endziel-Schwelle:** Die Verspätung wird am Zielort gemessen (Türöffnung, Art. 3 Nr. 18 VO 2021/782) — nicht an Zwischenstationen. Bei Anschlussverlust unter einer PNR ist die Gesamtverspätung am Endziel maßgeblich (Art. 12 Abs. 3 VO).
- **Sparpreis-Zugbindung aufgehoben ab 20 Min:** DB-AGB Ziffer 9 — relevante Verteidigung gegen "Sie haben einen anderen Zug genommen".
- **Streiks DB-eigenes Personal NICHT befreiend:** Art. 19 Abs. 10 Unterabs. 2 VO 2021/782 nimmt Streiks des EVU-Personals sowie Handlungen und Unterlassungen anderer Unternehmen, die dieselbe Infrastruktur nutzen, und der Infrastruktur- und Bahnhofsbetreiber ausdrücklich von der Ausnahme aus.
- **100-Min-Frist Art. 18 Abs. 3:** Wenn DB nicht binnen 100 Min nach planmäßiger Abfahrt eine Weiterreise-Option mitteilt, darf Fahrgast eigene Beförderung organisieren — EVU erstattet notwendige, angemessene und zumutbare Kosten.
- **Mindestbetrag 4 EUR:** Art. 19 Abs. 8 VO erlaubt Mindestauszahlbetrag von bis zu 4 EUR — bei Sparpreisen kann die 25 %-Entschädigung darunter fallen.

## Typische Fehler

- "Sparpreis hat keine Fahrgastrechte" → falsch. Art. 7 VO verbietet Einschränkung.
- "Verspätung des Zuges X war 70 Min, aber durch Anschluss-Erreichbarkeit war Endziel-Verspätung nur 30 Min" → kein Anspruch (Art. 19 Abs. 9 VO: weniger als 60 Min am Zielort = kein Anspruch).
- "Verspätung war wegen Personalmangel der DB" → kein außergewöhnlicher Umstand, Anspruch besteht weiter.
- "Antrag muss innerhalb 30 Tagen gestellt werden" → DB-Argumentation greift nicht; VO sieht keine kurze Ausschlussfrist vor, § 195 BGB drei Jahre maßgeblich.
- "Voucher als Erfüllung akzeptiert" → schließt Anspruch auf Geld nicht aus, wenn Fahrgast nicht ausdrücklich verzichtet hat (Art. 19 Abs. 7 VO: auf Wunsch in Geld).

## Quellen und Aktualität (Stand Juni 2026)

- VO (EU) 2021/782 in geltender Fassung (eur-lex.europa.eu, CELEX 32021R0782)
- EVO 2023 (BGBl. 2023 I Nr. 208) (gesetze-im-internet.de/evo_2023)
- DB-Beförderungsbedingungen und Tarifbestimmungen (bahn.de/agb)
- § 23 Nr. 1 GVG — Streitwertgrenze 10.000 EUR seit 01.01.2026
- Schlichtungsstelle Reise & Verkehr e.V. (schlichtungsstelle-reise-verkehr.de)
- EuGH- und BGH-Linie — siehe `references/rechtsprechung-fahrgastrechte.md`; Live-Check vor jedem Versand.

---

## Skill: `anlagen-bauen`

_Baut aus den Belegen eines Fahrgastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Widerspruch Schlichtungsantrag Klage) die Belege Buchungsbestaetigung E-Ticket Verspaetungsbestaetigung Foto Anzeigetafel App-Screenshots Belege zu Ausla..._

# Fahrgastrechte — Anlagen bauen

## Eingaben

```yaml
schriftsatz: <pfad zum Schriftsatz, z.B. widerspruch-2026-05-15.md>
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # erzeugt zusätzlich Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold        # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

## Workflow

### 1. Schriftsatz parsen

Liest den Schriftsatz und identifiziert alle erwähnten Anlagen anhand der Bezeichnung `Anlage K 1`, `Anlage K 2`, ... oder `Anlage K1`, `Anlage K2`. Erstellt geordnete Liste in Reihenfolge der Erwähnung im Text.

### 2. Rohbelege zuordnen

Verzeichnis `belege/` durchsuchen und jedem Anlage-K-Eintrag eine Datei zuordnen. Typische Belege im Fahrgastrechte-Kontext:

| Anlage typisch | Datei-Pattern | Beschreibung |
|---|---|---|
| K1 | `buchung-*.pdf` | Buchungsbestätigung der DB / des EVU |
| K2 | `e-ticket-*.pdf` oder `fahrkarten-*.pdf` | E-Tickets / Fahrkarten aller Reisenden |
| K3 | `verspaetung-*.png` oder `db-navigator-*.png` | DB-Verspätungsmitteilung (App / SMS / E-Mail) |
| K4 | `anzeigetafel-*.jpg` | Foto Anzeigetafel Zielbahnhof mit Uhrzeit |
| K5 | `belege-auslagen/*.pdf` | Belege zu Ersatzbeförderung / Verpflegung / Hotel |
| K6 | `erstantrag-*.pdf` | Eigener Erstantrag an DB Servicecenter |
| K7 | `ablehnung-*.pdf` | Ablehnungsschreiben der DB |
| K8 | `widerspruch-*.pdf` | Eigener Widerspruch (in Klage relevant) |
| K9 | `schlichtungsspruch-*.pdf` | Schlichtungsspruch der Schlichtungsstelle Reise & Verkehr |
| K10 ff. | `vollmacht-*.pdf` | Vollmachten der Mitreisenden |

Wenn eine erwähnte Anlage nicht zugeordnet werden kann: **Prüfer-Flag** mit Liste der unzugeordneten Bezugnamen.

### 3. Belege konvertieren und stempeln

Jeden Rohbeleg in PDF konvertieren (HEIC / JPG / PNG / DOCX / XLSX → PDF). Auf jedem Anlagen-PDF oben rechts in **Arial 12 FETT** (Helvetica-Bold 12pt) den Bezeichner stempeln:

```
                                                                    Anlage K 1
[Inhalt]
```

Dateibenennung: ohne Umlaute und Leerzeichen — `Anlage_K_1.pdf`, `Anlage_K_2.pdf`, … gemäß beA-Konvention.

### 4. Sammel-PDF optional

Wenn `bundle: true`: Sammel-PDF `Schriftsatz_mit_Anlagen.pdf` erzeugen — Schriftsatz vorne, Anlagen in nummerierter Reihenfolge mit Lesezeichen je Anlage. Nützlich für Akteneintrag und Sicht-Backup.

### 5. Ausgabe

Im `ausgabeverzeichnis/`:

- `Anlage_K_1.pdf`, `Anlage_K_2.pdf`, … (separate Anlagen-PDFs für beA-Upload)
- `Schriftsatz_mit_Anlagen.pdf` (Sammel-PDF, wenn bundle: true)
- `anlagen-uebersicht.md` (Tabelle Anlage K → Datei → Beschreibung; Fehlen-Hinweise)

## beA-Konvention

- Anlagen werden im beA als **separate PDFs** eingereicht.
- Jeweils mit Stempel oben rechts in **Arial 12 FETT**.
- **Dateiname** ohne Umlaute, ohne Leerzeichen: `Anlage_K_1.pdf`.
- **Reihenfolge** muss der Erwähnung im Schriftsatz entsprechen.
- Sammel-PDF zusätzlich für eigenes Aktenexemplar (nicht für beA-Upload).

## Foto-Belege bei DB-Verspätung — besondere Hinweise

- **Foto Anzeigetafel:** Uhrzeit muss erkennbar sein. Bei mehreren Anzeigetafeln nur die maßgebliche (Zielbahnhof). Datum eines Tages-Vergleichs ggf. durch EXIF-Daten ergänzen.
- **DB-Navigator-Screenshot:** möglichst mit Verbindungsdetails-Seite, die geplante und tatsächliche Ankunftszeit zeigt.
- **Ablehnungsschreiben:** alle Seiten in einer PDF (auch Rückseiten / Anlagen des Schreibens).
- **Vollmachten:** Originale-Scans hoher Qualität. Beidseitige Unterschriften bei sorgeberechtigten Eltern eines Minderjährigen.

## Fehlerquellen

- Schriftsatz erwähnt `Anlage K5`, im Belege-Verzeichnis fehlt die zugehörige Datei → Skript bricht ab; Prüfer-Flag.
- Doppelte Anlage K-Nummerierung im Schriftsatz → Fehlermeldung; manueller Eingriff.
- HEIC-Dateien iOS → automatische Konvertierung; bei OCR-Bedarf Hinweis.
- Mehrseitige Anlage in mehreren Dateien (z.B. Ablehnungsschreiben S. 1 separat) → Pre-Merge in eine Datei vor Stempelung.

## Ausgabe-Beispiel

```
anlagen-uebersicht.md
============================
Fall: FGR-2026-0042
Schriftsatz: widerspruch-2026-05-15.md
Erzeugte Anlagen:

| Anlage   | Datei                       | Beschreibung                          | Status |
|----------|-----------------------------|----------------------------------------|--------|
| Anlage K 1 | Anlage_K_1.pdf             | Buchungsbestätigung PNR ABC123          | ok      |
| Anlage K 2 | Anlage_K_2.pdf             | E-Tickets Mueller (3 Personen)          | ok      |
| Anlage K 3 | Anlage_K_3.pdf             | DB-Navigator Verspätungsmitteilung       | ok      |
| Anlage K 4 | Anlage_K_4.pdf             | Foto Anzeigetafel Muenchen Hbf 15:05   | ok      |
| Anlage K 5 | Anlage_K_5.pdf             | Kassenbon Bahnhofs-Imbiss 12,50 EUR    | ok      |
| Anlage K 6 | Anlage_K_6.pdf             | Erstantrag an DB Servicecenter           | ok      |
| Anlage K 7 | Anlage_K_7.pdf             | Ablehnungsschreiben DB vom 12.05.2026    | ok      |

Sammel-PDF: Schriftsatz_mit_Anlagen.pdf erzeugt (28 Seiten, 4.2 MB).
```

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 13 DSGVO
- § 71 GVG
- § 32 VSBG
- § 23 VSBG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `db-ablehnungsgruende-pruefen`

_Katalog typischer Ablehnungsgruende des DB-Servicecenters Fahrgastrechte mit Gegenargumenten und Pinpoint auf Art. 18 und 19 und 20 VO (EU) 2021/782 sowie EVO und DB-Befoerderungsbedingungen. Behandelt andere Verbindung als gebucht; Verspaetung unter 60 Minuten; hoehere Gewalt; Antrag verspaetet;..._

# Katalog der DB-Ablehnungsgründe und Gegenargumente

## Beweislast

**Generell:** Beweislast für außergewöhnliche Umstände und die Ergreifung zumutbarer Maßnahmen liegt beim **Eisenbahnverkehrsunternehmen** (Art. 19 Abs. 10 VO 2021/782 — Wortlaut "nachweisen kann"). Pauschale Behauptungen ohne Belege reichen nicht.

**Beweislast für Ankunftszeit:** Im Bestreitensfall liegt die sekundäre Darlegungslast bei der DB — sie verfügt über die internen Betriebsdaten (Leidis-NK / DiRail). Der Fahrgast trägt die Anfangsdarlegungslast, kann diese aber durch DB-Verspätungsbestätigung / DB-Navigator-Screenshot / Foto Anzeigetafel / Zeugen erfüllen.

## Katalog (10 typische Ablehnungsgründe)

### 1. "Sie haben eine andere Verbindung als die gebuchte genutzt"

**Typische DB-Formulierung:**

> "Leider können wir Ihrem Antrag nicht entsprechen, da die von Ihnen angegebene Verbindung nicht mit der gebuchten Verbindung übereinstimmt."

#### Bei Flexpreis

> Bei meinem Ticket handelt es sich um ein Flexpreis-Ticket. Dieses berechtigt mich, jeden beliebigen Zug auf der gebuchten Strecke zu nutzen, da keine Zugbindung besteht. Die Wahl eines anderen Zuges war somit mein gutes Recht und steht meinem Entschädigungsanspruch nicht entgegen. Maßgeblich ist ausschließlich die Verspätung am Zielbahnhof (Art. 19 Abs. 1 VO (EU) 2021/782).

#### Bei Sparpreis mit Verspätung > 20 Min Prognose

> Zwar bestand für mein Sparpreis-Ticket grundsätzlich Zugbindung. Da jedoch der gebuchte Zug [Zugnummer] am [Datum] eine Verspätung von [X] Minuten hatte bzw. eine Verspätung von mehr als 20 Minuten am Zielort absehbar war, wurde die Zugbindung gemäß Ziffer 9 der Beförderungsbedingungen der Deutschen Bahn aufgehoben. Ich war daher berechtigt, einen alternativen Zug zu nutzen. Maßgeblich für die Höhe des Anspruchs ist die Endziel-Verspätung am tatsächlichen Zielort.

#### Bei Sparpreis ohne Verspätung am Abfahrtsbahnhof

> Auch beim Sparpreis sieht Ziffer 9 BB DB die Aufhebung der Zugbindung ab 20 Min prognostizierter Verspätung am Zielort vor. Die Vorhersehbarkeit der Verspätung ergab sich aus [Quelle] — App-Hinweis, Bahnhofsdurchsage, Zugbegleiter-Mitteilung. Belege beiliegend.

---

### 2. "Die Verspätung betrug weniger als 60 Minuten"

**Typische DB-Formulierung:**

> "Die Verspätung am Zielbahnhof betrug nach unseren Aufzeichnungen weniger als 60 Minuten, sodass kein Entschädigungsanspruch besteht."

#### Wenn die tatsächliche Ankunftszeit anders war

> Ihre Angaben zur Ankunftszeit entsprechen nicht meiner tatsächlichen Ankunft. Maßgeblich ist die **Türöffnung am Bahnsteig** (Art. 3 Nr. 18 VO (EU) 2021/782), nicht der Zeitpunkt des Halts oder des Erreichens des Bahnhofsbereichs. Ich bin erst um [HH:MM] an meinem Zielbahnhof [Bahnhof] angekommen, was einer Verspätung von [X] Minuten gegenüber der planmäßigen Ankunft um [HH:MM] entspricht. Belege: Foto Anzeigetafel mit Uhrzeit / DB-Navigator-Screenshot / Zeuge [Name].

#### Wenn DB die falsche Verbindung zugrunde legt

> Sie legen Ihrer Berechnung offenbar die Verbindung [X] zugrunde. Tatsächlich war ich jedoch mit dem Zug [Y] unterwegs, der eine Verspätung von [Z] Minuten hatte. Ich bitte um Prüfung anhand der korrekten Verbindung.

#### Wenn Umsteigeverbindung betroffen war (Einheits-PNR)

> Maßgeblich für die Berechnung der Verspätung ist die Ankunft am Zielbahnhof, nicht die Verspätung einzelner Teilstrecken (Art. 12 Abs. 3 VO 2021/782). Durch die Verspätung des Zuges [Nummer] habe ich meinen Anschlusszug [Nummer] in [Umsteigebahnhof] verpasst und konnte erst mit dem nächsten Zug um [HH:MM] weiterreisen, wodurch sich eine Gesamtverspätung von [X] Minuten am Zielbahnhof ergab.

---

### 3. "Die Verspätung war auf höhere Gewalt zurückzuführen"

**Typische DB-Formulierung:**

> "Die Verspätung war auf außergewöhnliche Umstände zurückzuführen, die außerhalb unseres Einflussbereichs lagen."

#### Was ist KEINE höhere Gewalt nach Art. 19 Abs. 10 VO

Folgende Gründe sind ausdrücklich oder nach systematischer Auslegung NICHT als außergewöhnliche Umstände anerkannt:

- Technische Defekte an Zügen oder Infrastruktur (betriebsbedingt)
- Personalausfall / Personalmangel
- Signalstörungen (Infrastrukturbetreiber-Risiko)
- Weichenstörungen
- Oberleitungsstörungen
- Verspätungen aus dem vorherigen Betriebsablauf (Wagenumlauf)
- Überfüllung / Kapazitätsprobleme
- Bauarbeiten (auch ungeplante)
- **Streiks des eigenen Personals** (Art. 19 Abs. 10 Unterabs. 2 VO ausdrücklich)
- **Handlungen oder Unterlassungen eines anderen Unternehmens, das dieselbe Eisenbahninfrastruktur nutzt, sowie Handlungen oder Unterlassungen der Infrastrukturbetreiber und Bahnhofsbetreiber** (Art. 19 Abs. 10 Unterabs. 2 VO ausdrücklich)

#### Gegenargument allgemein

> Gemäß Art. 19 Abs. 10 VO (EU) 2021/782 sind außergewöhnliche Umstände nur solche, die als direkte Folge von oder im untrennbaren Zusammenhang mit außerhalb des Eisenbahnbetriebs liegenden Umständen, dem Verschulden des Fahrgasts oder dem Verhalten Dritter aufgetreten sind. Die Beweislast hierfür liegt beim Eisenbahnverkehrsunternehmen. [Konkreter Grund, z.B.:] Eine Signalstörung oder ein technischer Defekt gehört zum typischen Betriebsrisiko und stellt keinen außergewöhnlichen Umstand dar.

#### Bei Streik als Begründung

> Streiks des Personals des Eisenbahnverkehrsunternehmens sind nach Art. 19 Abs. 10 Unterabs. 2 VO (EU) 2021/782 **ausdrücklich** von der Befreiungsregel ausgenommen. Dasselbe gilt nach dem Wortlaut für Handlungen und Unterlassungen eines anderen Unternehmens, das dieselbe Eisenbahninfrastruktur nutzt, sowie für Handlungen und Unterlassungen der Infrastrukturbetreiber und Bahnhofsbetreiber — was insbesondere die DB Netz AG erfasst. Ihre Berufung auf einen Streik als außergewöhnlichen Umstand ist daher rechtlich unzutreffend.

#### Bei Wetter als Begründung

> Normale Witterungsverhältnisse, auch winterliche, stellen keinen außergewöhnlichen Umstand dar. Eisenbahnunternehmen müssen sich auf saisonale Wetterbedingungen einstellen. Nur extreme, nicht vorhersehbare Wetterphänomene (Jahrhundert-Sturm, Hochwasser, Großschneeereignisse außerhalb erwartbarer Winterintensität) können als außergewöhnlich gelten. Bitte legen Sie konkret dar, welches außergewöhnliche Wetterereignis vorlag und welche zumutbaren Vorkehrungen Sie getroffen haben.

#### Bei Personenschaden / Notarzteinsatz

Drittverschulden (Art. 19 Abs. 10 lit. c VO) — potenziell anerkannt. Dennoch:

> Selbst wenn ein außergewöhnlicher Umstand vorlag, hat das Eisenbahnverkehrsunternehmen die Pflicht, die Auswirkungen so gering wie möglich zu halten. Zudem hätte ich nach Art. 18 VO (EU) 2021/782 über Alternativen informiert und nach Art. 20 VO betreut werden müssen.

---

### 4. "Ihr Antrag wurde zu spät eingereicht"

**Typische DB-Formulierung:**

> "Leider können wir Ihren Antrag nicht berücksichtigen, da er außerhalb der vorgesehenen Frist eingereicht wurde."

#### Gegenargument

> Die VO (EU) 2021/782 sieht in Art. 19 keine Antragsfrist vor, die zum Verlust des Entschädigungsanspruchs führt. Art. 27 VO normiert eine 3-Monats-Beschwerdefrist — diese ist eine reine Verfahrensfrist, keine materielle Ausschlussfrist. Maßgeblich ist die dreijährige Verjährungsfrist gemäß § 195 BGB i.V.m. § 199 Abs. 1 BGB ab Schluss des Jahres, in dem der Anspruch entstand und ich Kenntnis hatte. Mein Antrag vom [Datum] liegt deutlich innerhalb dieser Frist. Ich bitte Sie daher, meinen Antrag ungeachtet einer eventuellen internen Fristenvorgabe erneut zu prüfen.

---

### 5. "Fehlende oder unzureichende Nachweise"

**Typische DB-Formulierung:**

> "Leider liegen uns keine ausreichenden Nachweise für Ihre Reise / die Verspätung vor."

#### Gegenargument

> Die Verspätung des Zuges [Nummer] am [Datum] ist in Ihren eigenen Betriebssystemen dokumentiert und nachvollziehbar. Ich verweise auf mein Ticket [Buchungsnummer] sowie auf die Aufzeichnungen in Ihrem Betriebs-Auskunftssystem LeiDis-NK / DiRail. Sollten weitere Nachweise erforderlich sein, bitte ich Sie, mir konkret mitzuteilen, welche Dokumente Sie benötigen.

Bei Klage: Antrag nach §§ 421 ff. ZPO auf Vorlage der DB-internen Betriebsdaten — Urkundenbeweis.

---

### 6. "Ihr Ticket ist nicht erstattungsfähig"

**Typische DB-Formulierung:**

> "Für die von Ihnen genutzte Ticketart ist leider keine Entschädigung vorgesehen."

#### Gegenargument

> Gemäß Art. 7 VO (EU) 2021/782 dürfen die Verpflichtungen gegenüber Fahrgästen — insbesondere durch abweichende oder einschränkende Bestimmungen im Beförderungsvertrag — nicht eingeschränkt oder ausgeschlossen werden. Jeder Fahrgast hat unabhängig von der Ticketart Anspruch auf Entschädigung bei Verspätung. Dies gilt ausdrücklich auch für Sparpreise, Super Sparpreise, ermäßigte BahnCard-Tickets und sonstige ermäßigte Tickets. Vertragsbedingungen, die diese Rechte einschränken, sind für mich als Fahrgast nicht verbindlich.

---

### 7. "Die angegebene Verspätung ist nicht nachvollziehbar"

**Typische DB-Formulierung:**

> "Nach unseren Aufzeichnungen lag die Ankunftszeit des Zuges innerhalb der regulären Toleranz."

#### Gegenargument

> Ich widerspreche dieser Darstellung. Die tatsächliche Ankunft meines Zuges [Nummer] am [Datum] in [Bahnhof] erfolgte ausweislich [Beleg: Foto Anzeigetafel / DB-Navigator-Screenshot / Zeuge / DB-Verspätungsbestätigung] um [HH:MM], gegenüber der planmäßigen Ankunft um [HH:MM]. Dies entspricht einer Verspätung von [X] Minuten. Ich bitte Sie, die Zugverfolgungsdaten des betreffenden Zuges für den genannten Tag erneut zu überprüfen.

---

### 8. "Die Erstattung wurde bereits vorgenommen"

**Typische DB-Formulierung:**

> "Eine Entschädigung für die genannte Reise wurde bereits ausgezahlt."

#### Wenn falsch

> Ich kann einen Eingang der genannten Erstattung auf meinem Konto nicht bestätigen. Ich bitte Sie, mir das Datum und den Betrag der angeblichen Überweisung mitzuteilen, damit ich den Sachverhalt mit meiner Bank klären kann. Sollte eine Erstattung tatsächlich erfolgt sein, bitte ich um einen Nachweis.

#### Wenn Teilerstattung

> Die von Ihnen genannte Erstattung in Höhe von [X] EUR deckt lediglich [Teilanspruch]. Mein vollständiger Anspruch umfasst jedoch auch [weiterer Anspruch, z.B. Verpflegungskosten Art. 20 VO oder Eigenbeförderung Art. 18 Abs. 3 Unterabs. 2 VO], sodass ich um Begleichung des Differenzbetrags bitte.

---

### 9. "Sie haben eine Alternativroute / einen Umweg genommen"

**Typische DB-Formulierung:**

> "Da Sie eine andere als die ursprüngliche Strecke genutzt haben, besteht kein Anspruch."

#### Gegenargument

> Aufgrund des Zugausfalls / der erheblichen Verspätung sah ich mich gezwungen, eine Alternativroute zu wählen, um mein Reiseziel zu erreichen. Dies steht im Einklang mit Art. 18 Abs. 1 lit. b VO (EU) 2021/782, wonach mir das Recht auf Weiterreise mit geänderter Streckenführung unter vergleichbaren Beförderungsbedingungen zusteht. Maßgeblich bleibt die Verspätung am Zielbahnhof gegenüber der ursprünglich geplanten Ankunftszeit. Eine Wahl der Alternativroute löst den Anspruch nicht aus, sondern lediglich Ihre Pflicht zur Erstattung der notwendigen Kosten nach Art. 18 Abs. 3 Unterabs. 2 VO.

---

### 10. "Die geltend gemachten Verpflegungskosten sind unangemessen"

**Typische DB-Formulierung:**

> "Die von Ihnen geltend gemachten Kosten überschreiten unseren Erstattungsrahmen."

#### Gegenargument

> Die von mir geltend gemachten Verpflegungskosten in Höhe von [Betrag] EUR entsprechen den üblichen Preisen für [Getränke / Essen] an einem Bahnhof. Die VO (EU) 2021/782 enthält in Art. 20 keine festen Pauschalbeträge — maßgeblich ist die Angemessenheit im Verhältnis zur Wartezeit. Da mir von der Deutschen Bahn keine Verpflegung bereitgestellt wurde — wozu sie nach Art. 20 Abs. 1 lit. a VO bei mindestens 60 Minuten Verspätung verpflichtet gewesen wäre — , war ich gezwungen, diese selbst zu beschaffen. Bahnhofs-Preise sind branchenüblich.

---

## Zusatz: Voucher als angeblich "akzeptierte Entschädigung"

**Typische DB-Formulierung:**

> "Sie haben einen Gutschein erhalten und damit die Entschädigung akzeptiert."

#### Gegenargument

> Akzeptanz oder Erhalt eines Gutscheins schließt den Anspruch auf Auszahlung in Geld nicht aus. Art. 19 Abs. 7 Satz 2 VO (EU) 2021/782 sieht ausdrücklich vor, dass die Entschädigung **auf Wunsch des Fahrgasts in Form eines Geldbetrags** zu erfolgen hat. Ich verzichte hiermit auf den Gutschein und bitte um Auszahlung des Anspruchs auf das genannte Konto. Etwaige Gutscheine sind zurückzugeben oder werden auf der Empfängerseite ungenutzt.

## Zusatz: "Streik / Personalmangel war außergewöhnlich"

Bereits in Punkt 3 detailliert behandelt. Pinpoint: Art. 19 Abs. 10 Unterabs. 2 VO 2021/782.

## Versand-Hinweis

Diesen Katalog vor jedem Widerspruchsschreiben durchgehen — den konkret im Ablehnungsschreiben genannten Ablehnungsgrund identifizieren und den entsprechenden Punkt **wortlautnah** zitieren mit Norm-Pinpoint.

## Ausgabe

- `ablehnungsgrund-analyse.md` — identifizierter Grund + Gegenargument + Norm-Pinpoint
- Verweis auf entsprechende Norm in `references/vo-2021-782-uebersicht.md` und `references/evo-2023-uebersicht.md`
- Übergabe an Skill `fahrgastrechte-widerspruch` zur Brief-Erstellung

---

## Skill: `eigenbefoerderung-und-betreuung-art-18`

_Pruefraster für Selbstbefoerderung des Fahrgasts (Art. 18 Abs. 3 Unterabs. 2 VO 2021/782 mit 100-Minuten-Frist) und Hilfeleistungs-Anspruch (Art. 20 VO Verpflegung Hotel Transport) sowie SPNV-Sonderfall § 11 EVO (20-Min-Schwelle Alternativzug; 120 EUR Hoechstbetrag Ersatzbefoerderung bei Nachtfah..._

# Eigenbeförderung und Betreuung (Art. 18, 20 VO; § 11 EVO)

## Drei Anspruchsgrundlagen

### 1. Eigenbeförderung (Art. 18 Abs. 3 Unterabs. 2 VO 2021/782)

**Tatbestand:**

Wenn dem Fahrgast die verfügbaren Optionen für Weiterreise mit geänderter Streckenführung **nicht binnen 100 Minuten** nach planmäßiger Abfahrtszeit des verspäteten oder ausgefallenen Verkehrsdienstes oder des verpassten Anschlusses **mitgeteilt** werden, ist der Fahrgast berechtigt, Verträge mit anderen Anbietern öffentlicher Verkehrsdienste zu schließen (Eisenbahn, Reisebus, Bus).

**Rechtsfolge:** Das EVU erstattet die **notwendigen, angemessenen und zumutbaren Kosten**.

**Praxisprüfung:**

| Frage | Antwort |
|---|---|
| Wann beginnt die 100-Min-Frist? | mit planmäßiger Abfahrtszeit des betroffenen Verkehrsdienstes |
| Was zählt als "Mitteilung"? | konkrete Alternativ-Verbindung mit Zeit und Route — nicht: "wir melden uns gleich"; nicht: pauschale Verspätungsanzeige in der App |
| Was sind "notwendige, angemessene und zumutbare Kosten"? | Standardklassen-Ticket bei Konkurrenz-Bahn / Fernbus; nur Standard-Hotel; Taxi bei fehlender ÖV-Alternative |
| Worauf zu achten? | Belege aufbewahren; Eingangsbestätigung der App / SMS-Mitteilung der DB sichern, um 100-Min-Verstreichen zu beweisen |

**Was NICHT erstattungsfähig ist:**

- Aufpreis 1. Klasse, wenn DB-Ticket 2. Klasse war.
- Flug, wenn vergleichbare Bahn / Bus möglich war.
- Privat-PKW-Erstattung über üblichen Tagessatz hinaus (Kilometerpauschale max. ähnlich JVEG).
- Verlust verfallener Anschluss-Tickets, wenn diese separat (eigene PNR) gebucht waren.

### 2. Hilfeleistung (Art. 20 VO 2021/782)

**Tatbestand:**

Bei Verspätung von Abfahrt oder Ankunft um **60 Minuten und mehr** bietet das EVU dem Fahrgast kostenlos:

- a) **Mahlzeiten und Erfrischungen** in angemessenem Verhältnis zur Wartezeit, sofern verfügbar oder vernünftigerweise herbeischaffbar;
- b) **Hotel oder andere Unterkunft + Transport zwischen Bahnhof und Unterkunft**, wenn ein Aufenthalt von einer oder mehreren Nächten oder ein zusätzlicher Aufenthalt notwendig wird;
- c) **Transport zwischen Zug und Bahnhof, einem anderen Verkehrsmittel oder dem Zielort**, falls Zug auf der Strecke blockiert ist.

**Wenn DB diese Leistung nicht erbringt:** Der Fahrgast darf selbst kaufen und das EVU erstattet (Schadensersatz aus Vertragsverletzung; argumentativ + § 280 BGB).

**Angemessenheit:**

- Verpflegung: typische Bahnhofs-Preise (Wasser, Brötchen, Heißgetränk). Richtwert 5–25 EUR je Stunde Wartezeit.
- Hotel: Standard-Niveau (3-Sterne), nicht Premium.
- Taxi nur, wenn ÖV nicht verfügbar (Nachtzeit) oder Hotel nicht in ÖV-Reichweite.

### 3. SPNV-Zusatzrecht § 11 EVO

**Tatbestand:** Fahrgast besitzt SPNV-Fahrausweis. Erwartet wird **mindestens 20 Min Verspätung** am Zielort wegen Ausfall oder Unpünktlichkeit.

**Rechtsfolgen:**

| Anspruch | Voraussetzung | Norm |
|---|---|---|
| Fahrt mit anderem **Zug** zum vertragsgemäßen Zielort | ≥ 20 Min prognostiziert | § 11 Abs. 1 Nr. 1 EVO |
| Fahrt mit anderem **Verkehrsmittel** (Taxi, Bus) — Erstattung notwendig + angemessen | a) Ankunft 0–5 Uhr und ≥ 60 Min Verspätung erwartet, ODER b) letzter Zug des Tages | § 11 Abs. 1 Nr. 2 EVO |
| **Höchstbetrag** Ersatzbeförderung | 120 EUR | § 11 Abs. 2 EVO |

**Ausschluss anderer Zug:** Wenn (1) Reservierungspflicht, (2) Sonderfahrt oder (3) erhebliche Störung des Betriebsablaufs zu erwarten (§ 11 Abs. 3 EVO).

## Entscheidungsbaum

```
1. Welcher Verkehr?
   ├── Fernverkehr → Art. 18 + Art. 20 VO (100-Min-Frist; 60-Min-Hilfeleistung)
   └── SPNV → § 11 EVO + Art. 18 + Art. 20 VO (kumulativ)

2. Hat DB Alternativ-Verbindung mitgeteilt?
   ├── Nein, > 100 Min nach planmäßiger Abfahrt → Eigenbeförderung Art. 18 Abs. 3 Unterabs. 2 VO
   ├── Ja, aber unzumutbar → vertragliche Klärung; Schaden ggf. nach § 280 BGB
   └── Ja, zumutbar → Annahme; bei späterer Erstattung nur Differenz wenn DB-Vorschlag genutzt

3. Hat Fahrgast Verpflegung / Hotel / Transport selbst gekauft?
   ├── Bei Wartezeit ≥ 60 Min UND DB hat nicht angeboten → Art. 20 VO Erstattung
   ├── Höhe angemessen? → Belege prüfen
   └── Eigene Beweispflicht: was hat DB konkret nicht angeboten?

4. Bei SPNV-Sondersituation (Nachtfahrt, letzte Verbindung)?
   ├── ≥ 60 Min Ankunft 0–5 Uhr → Taxi/Bus bis 120 EUR (§ 11 Abs. 2 EVO)
   └── letzte Verbindung + Zielort nicht mehr bis 24:00 Uhr erreichbar → dito
```

## Belege

Pflicht-Belege:

- **Kassenbeleg / Rechnung** (mit Datum, Position, Preis)
- **DB-Verspätungsbestätigung** (über Servicecenter Fahrgastrechte abrufbar)
- **App-Screenshot** mit DB-Information über erwartete Ankunftszeit
- **Foto Bahnhofs-Anzeigetafel** oder **Foto Zug-Display** bei Stillstand
- **SMS / E-Mail** der DB mit Information / Nicht-Information
- **Zeugen** — Mitreisende

## Argumentation gegen typische DB-Ablehnung

### "Sie hätten die DB-Hotline anrufen sollen, bevor Sie Taxi nehmen"

> **Gegenargument:** Art. 18 Abs. 3 Unterabs. 2 VO 2021/782 knüpft an objektives Verstreichen der 100-Min-Frist ohne Mitteilung an. Es besteht keine Obliegenheit, die DB-Hotline anzurufen. § 11 EVO ist im SPNV unmittelbar anwendbar.

### "Die genutzte Alternativbeförderung war nicht notwendig"

> **Gegenargument:** Maßgeblich ist die ex-ante-Sicht des Fahrgasts. Wenn die DB binnen 100 Min keine konkrete Alternative mitgeteilt hat oder die mitgeteilte Alternative unzumutbar war, war Eigenbeförderung notwendig. Beweislast für Mitteilung: DB.

### "Hotelkosten sind unangemessen"

> **Gegenargument:** Angemessen ist eine Standard-Unterkunft (3-Sterne-Niveau). Beleg über vergleichbare Verfügbarkeit zum Buchungszeitpunkt vorlegen. Bei Buchung über bahn.de eigene Empfehlung der DB einfordern.

### "Verpflegungskosten übersteigen Pauschalsatz"

> **Gegenargument:** VO 2021/782 kennt keinen Pauschalsatz. Art. 20 VO verlangt Angemessenheit im Verhältnis zur Wartezeit. Bahnhofs-Preise sind branchenüblich.

### "Sparpreis schließt Erstattung aus"

> **Gegenargument:** Art. 7 VO 2021/782 — Vertragsbedingungen dürfen Rechte aus der VO nicht einschränken. Erstattung von Auslagen folgt aus Art. 18 / 20 VO, nicht aus Ticket-Tarifart.

## Beispielfall

```
Fall: ICE 503 Berlin–München, geplante Ankunft 13:20.
Während der Fahrt Verspätungs-App-Mitteilung: "Ankunft 16:30 voraussichtlich"
(180 Min Verspätung).
Keine zumutbare Bahn-Alternative von DB angeboten.

100-Min-Frist: ab planmäßiger Abfahrt 08:25 + 100 Min = bis 10:05.
Bis 10:05 keine Alternativ-Verbindung mitgeteilt.
Fahrgast nimmt um 12:00 FlixTrain ab Frankfurt nach München (47 EUR);
erreicht München um 15:00.

Endziel-Verspätung: 100 Min → 25 % Sparpreis 79 EUR = 19,75 EUR Entschädigung.
Eigenbeförderungs-Kosten: 47 EUR FlixTrain. Plus: 18 EUR Verpflegung 4 Stunden Wartezeit.

Gesamtforderung Fahrgastrechte:
 Art. 19 Entschädigung:           19,75 EUR
 Art. 18 Abs. 3 Eigenbeförderung: 47,00 EUR  (FlixTrain-Ticket)
 Art. 20 Verpflegung:             18,00 EUR
 Summe:                           84,75 EUR
```

## Ausgabe

- `eigenbefoerderung-belegmatrix.yaml` mit erfassten Auslagen und Belegen.
- `argumentation.md` mit anwendbaren Normen pro Position.
- Empfehlung Folge-Skill (`forderung-an-db-erste-stufe` oder `fahrgastrechte-widerspruch` bei Ablehnung).

## Leitentscheidungen Eigenbeförderung und Hilfeleistung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `einfuehrung-vo-2021-782`

_Einfuehrung VO (EU) 2021/782 Fahrgastrechte Eisenbahn. Anwendungsbereich Art. 2 (auch SPNV mit Ausnahmen § 2 EVO), Begriffsbestimmungen Art. 3 (Verspaetung Ankunft Anschluss Zeitfahrkarte), Verzichtsverbot Art. 7, Durchgangsfahrkarten Art. 12, Erstattung und Weiterreise Art. 18 (100-Minuten-Frist..._

# Einführung VO (EU) 2021/782 — Fahrgastrechte Eisenbahn

## Rechtsquellen

- **VO (EU) 2021/782** vom 29. April 2021 — Neufassung, in Kraft seit 7. Juni 2023, ersetzt VO (EG) 1371/2007. ABl. L 172 vom 17.5.2021, S. 1. [eur-lex.europa.eu (CELEX 32021R0782)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32021R0782).
- **EVO 2023** — Eisenbahnverkehrs-Verordnung vom 4. August 2023 (BGBl. 2023 I Nr. 208). Ergänzt die EU-VO für deutsche Eisenbahnverkehrsunternehmen, insbesondere im SPNV.

## Anwendungsbereich (Art. 2 VO; § 2 EVO)

### Wer ist erfasst?

| Verkehr | EU-VO 2021/782 | Einschränkungen (D) |
|---|---|---|
| Fernverkehr (ICE, IC, EC, FlixTrain) | voll | keine |
| Regionalverkehr (RE, RB) — SPNV | weitgehend | § 2 EVO: Art. 20 Abs. 2 lit. a, 29, 30 Abs. 1 Satz 1, 9 Abs. 2 ausgenommen/modifiziert |
| Stadt-/Vorortverkehr (S-Bahn, U-Bahn) | von DE ausgenommen | Nationale Regelung (vorrangig Tarifbedingungen) |
| Historisch / touristisch | nur Art. 13, 14 | § 2 Abs. 2 EVO |

### Wer ist passivlegitimiert?

Anspruchsgegner ist das **ausführende Eisenbahnverkehrsunternehmen (EVU)** — Art. 19 Abs. 1 VO 2021/782. Bei DB-Tickets:

- **DB Fernverkehr AG** (ICE, IC, EC) — Stephensonstraße 1, 60326 Frankfurt am Main
- **DB Regio AG** (RE, RB im Auftrag der Bundesländer) — Stephensonstraße 1, 60326 Frankfurt am Main
- Konkurrenzanbieter mit eigener PNR: **ÖBB-Personenverkehr AG** (Wien), **FlixTrain GmbH** (München), **NWB Nordwestbahn**, **Vlexx**, **Abellio**, **Transdev**, **Go-Ahead** etc.
- Bei DB-Konkurrenz-Ticket im DB-Vertriebssystem (z.B. NWB-Strecke via bahn.de gebucht): **NWB als Operating EVU passivlegitimiert**, DB nur als Vermittler.

### Begriffe (Art. 3 VO)

- **Verspätung (Nr. 17):** Zeitdifferenz zwischen planmäßiger und tatsächlicher / erwarteter Ankunft am Zielbahnhof.
- **Ankunft (Nr. 18):** Türöffnung am Bahnsteig — nicht Halt des Zuges.
- **Durchgangsfahrkarte (Nr. 9):** Fahrkarte über mehrere aufeinander folgende Dienste als einheitlicher Beförderungsvertrag.
- **Verpasster Anschluss (Nr. 20):** Folge einer Verspätung / eines Ausfalls innerhalb einer Durchgangsfahrkarte.

## Schwellen und Beträge (Art. 19)

### Entschädigung

| Verspätung am Zielort | Anteil Fahrpreis |
|---|---|
| 60–119 Minuten | **25 %** |
| ≥ 120 Minuten | **50 %** |

**Mindestauszahlung:** 4 EUR pro Fahrkarte (Art. 19 Abs. 8). EVU darf Beträge darunter ablehnen.

**Bezugsgröße:** tatsächlich gezahlter Fahrpreis für den verspäteten Verkehrsdienst. Bei Hin- und Rückfahrt-Ticket: halber Preis als Bezugsgröße. Bei Einzelstrecken-Aufteilung: anteiliger Preis.

**Zeitfahrkarten (Abs. 2):** Pauschale nach Tarifbestimmungen — siehe `references/db-tarif-und-agb.md`:

- BahnCard 100: 10 EUR (60 Min) / 20 EUR (120 Min)
- Deutschlandticket: 1,50 EUR pro Verspätung ab 60 Min, höchstens 25 % des Monatspreises
- Wochen-/Monatskarten: anteilig analog Deutschlandticket

### Erstattung / Weiterreise (Art. 18)

**Auslöser:** Vernünftig erwartete Verspätung am Zielort ≥ 60 Min, verpasster Anschluss, Zugausfall.

**Wahlrecht:**

a) Erstattung des vollen Fahrpreises (ggf. mit Rückbeförderung)
b) Weiterreise mit nächster Gelegenheit (geänderte Streckenführung möglich)
c) Weiterreise zu späterem Zeitpunkt

**Eigenständige Beförderung (Art. 18 Abs. 3 Unterabs. 2):** Wenn Bahn **nicht binnen 100 Minuten** nach planmäßiger Abfahrt Weiterreise-Optionen mitteilt, darf Fahrgast eigene Verträge schließen (Taxi, Bus, anderer Bahn-Anbieter). EVU erstattet notwendige, angemessene und zumutbare Kosten.

**Bearbeitungsfrist Erstattung:** binnen 30 Tagen (Art. 18 Abs. 5).

### Hilfeleistung (Art. 20)

Bei Verspätung von Abfahrt oder Ankunft um **60 Minuten und mehr** kostenlos:

- Mahlzeiten und Erfrischungen in angemessenem Verhältnis (sofern verfügbar oder herbeischaffbar)
- Hotelunterkunft + Transport zwischen Bahnhof und Hotel bei notwendiger Übernachtung
- Transport bei Stillstand auf der Strecke

Wenn DB die Hilfeleistung nicht erbringt: Fahrgast darf selbst kaufen, EVU erstattet (analog Art. 18 Abs. 3 Unterabs. 2 i.V.m. § 11 Abs. 2 EVO für SPNV).

## Befreiungstatbestände (Art. 19 Abs. 10)

EVU ist befreit, wenn Verspätung, verpasster Anschluss oder Zugausfall direkte Folge von oder im untrennbaren Zusammenhang mit folgenden Umständen war:

a) **außerhalb des Eisenbahnbetriebs liegende außergewöhnliche Umstände** — Extremwetter, große Naturkatastrophen, schwere Gesundheitskrisen;
b) **Verschulden des Fahrgasts**;
c) **Verhalten eines Dritten** — Betreten der Gleise, Kabeldiebstahl, Notfälle im Zug, Strafverfolgungsmaßnahmen, Sabotage, Terrorismus.

**Ausdrücklich nicht befreiend (Art. 19 Abs. 10 Unterabs. 2):**

> "Streiks des Personals des Eisenbahnunternehmens, Handlungen oder Unterlassungen eines anderen Unternehmens, das dieselbe Eisenbahninfrastruktur nutzt, und Handlungen oder Unterlassungen der Infrastrukturbetreiber und Bahnhofsbetreiber fallen nicht unter die Ausnahme nach Unterabsatz 1 Buchstabe c."

**Praxisrelevant:**

- DB-Personalstreiks (GDL, EVG) — bleiben entschädigungspflichtig.
- DB Netz AG Störungen / Signalstörungen / Bauarbeiten — als Handlungen / Unterlassungen der Infrastrukturbetreiber NICHT befreiend.
- Andere EVUs auf gleicher Strecke (z.B. Güterverkehr blockiert ICE-Strecke) — Handlungen anderer Unternehmen NICHT befreiend.
- Wettergrund nur, wenn extrem und nicht vorhersehbar.

## Verzichtsverbot (Art. 7)

Vertragsbedingungen, die direkt oder indirekt die Rechte aus der VO aufheben oder einschränken, sind **für den Fahrgast nicht verbindlich**.

→ DB-Tarife dürfen nur **erweitern** (z.B. Sparpreis-Zugbindungsaufhebung ab 20 Min) — niemals beschränken (z.B. "Sparpreise haben keine Entschädigungsansprüche" ist unwirksam).

## Beschwerde und Schlichtung

**Art. 27 VO:** Beschwerderecht beim EVU binnen **drei Monaten** (Verfahrensfrist, nicht materielle Ausschlussfrist). EVU antwortet binnen einem Monat, in begründeten Fällen binnen drei Monaten.

**§ 15 EVO:** Schlichtungsstelle. In Deutschland: **Schlichtungsstelle Reise & Verkehr e.V.** (vormals söp), Fasanenstraße 81, 10623 Berlin. Anerkannt nach §§ 4 ff. VSBG. Kostenfrei für Verbraucher. Voraussetzung: vorgerichtlich erfolglose Reklamation; keine anhängige Klage.

## Verjährung

§ 195 BGB: drei Jahre. § 199 Abs. 1 BGB: Beginn am Schluss des Kalenderjahres, in dem der Anspruch entstand und der Verbraucher Kenntnis hatte.

**Beispiel:** Verspätung am 12.05.2026 → Verjährung mit Ablauf 31.12.2029.

## Gerichtsstand

- **Brüssel-Ia Art. 7 Nr. 1 lit. b** + § 29 ZPO — Erfüllungsort: Abfahrts- oder Zielbahnhof (Fahrgast hat Wahlrecht).
- Subsidiär §§ 12, 17 ZPO — Sitz der DB Fernverkehr AG / DB Regio AG (Frankfurt am Main) oder Konzern (DB AG Berlin).
- Sachliche Zuständigkeit: § 23 Nr. 1 GVG (10.000 EUR Schwelle seit 01.01.2026) Amtsgericht; darüber Landgericht mit Anwaltszwang (§ 78 ZPO).

## Praxis-Schwellen Übersicht

| Frage | Schwelle | Norm |
|---|---|---|
| Wann Entschädigung 25 %? | ≥ 60 Min Verspätung am Zielort | Art. 19 Abs. 1 lit. a VO |
| Wann Entschädigung 50 %? | ≥ 120 Min Verspätung am Zielort | Art. 19 Abs. 1 lit. b VO |
| Wann Hilfeleistung (Verpflegung, Hotel)? | ≥ 60 Min | Art. 20 VO |
| Wann Wahlrecht Erstattung/Weiterreise? | ≥ 60 Min prognostiziert | Art. 18 Abs. 1 VO |
| Wann Eigenbeförderung erlaubt? | DB schweigt > 100 Min ab planmäßiger Abfahrt | Art. 18 Abs. 3 Unterabs. 2 VO |
| Wann Sparpreis-Zugbindung aufgehoben? | > 20 Min prognostiziert | Ziffer 9 BB DB |
| Wann SPNV-Alternativzug (§ 11 EVO)? | ≥ 20 Min prognostiziert am Zielort | § 11 Abs. 1 Nr. 1 EVO |
| Wann SPNV-Taxi/Bus (§ 11 EVO)? | Ankunft 0–5 Uhr + ≥ 60 Min, oder letzte Verbindung Tag | § 11 Abs. 1 Nr. 2 EVO |
| Höchstbetrag SPNV-Ersatzbeförderung? | 120 EUR | § 11 Abs. 2 EVO |
| Mindestbetrag Entschädigung? | 4 EUR pro Fahrkarte | Art. 19 Abs. 8 VO |
| Verjährung Anspruch? | 3 Jahre ab Jahresende | §§ 195, 199 Abs. 1 BGB |
| Beschwerdefrist EVU (Verfahren)? | 3 Monate | Art. 27 VO |
| Bearbeitungsfrist Erstattung DB? | 30 Tage | Art. 18 Abs. 5 VO |
| Bearbeitungsfrist Entschädigung DB? | 1 Monat | Art. 19 Abs. 7 VO |
| AG-Zuständigkeit Streitwert? | bis 10.000 EUR | § 23 Nr. 1 GVG n.F. |

## Ausgabe

Bei Einsatz dieses Skills als Antwort auf eine Mandanten- oder Praxisfrage:

1. Kurze Einordnung der Frage in das System der VO 2021/782 / EVO.
2. Verweis auf konkrete Norm mit Schwelle.
3. Hinweis auf passenden Folge-Skill aus diesem Plugin.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `entschaedigung-berechnen`

_Berechnet die Entschaedigung nach Art. 19 VO (EU) 2021/782. Zwei Stufen 25 Prozent (ab 60 Minuten Endziel-Verspaetung) und 50 Prozent (ab 120 Minuten). DB-Tarif-Pauschalen für BahnCard 100 (10 oder 20 EUR), Deutschlandticket (1.50 EUR mit Monatsdeckel 25 Prozent), Zeitkarten (anteilig). Pro Reise..._

# Entschädigung berechnen

## Norm

Art. 19 VO (EU) 2021/782 — Entschädigung in zwei Stufen:

| Stufe | Verspätung am Zielort | Anteil Fahrpreis |
|---|---|---|
| 1 | 60–119 Minuten | **25 %** |
| 2 | ab 120 Minuten | **50 %** |

**Mindestauszahlung:** 4 EUR pro Fahrkarte (Art. 19 Abs. 8). EVU darf Beträge darunter ablehnen.

**Bezugsgröße:** Tatsächlich entrichteter Fahrpreis. Bei Hin- und Rückfahrt-Beförderungsvertrag: halber Fahrpreis als Bezug (Art. 19 Abs. 3 Satz 2). Bei Verspätung auf nur einer Teilstrecke: anteiliger Preis.

## Berechnungsweg

### Schritt 1: Ticketart bestimmen

| Ticketart | Bezugsgröße | Besonderheit |
|---|---|---|
| Flexpreis | gezahlter Preis | volle Fahrgastrechte; keine Zugbindung |
| Sparpreis | gezahlter Preis | volle Fahrgastrechte; Zugbindung ab 20 Min aufgehoben |
| Super Sparpreis | gezahlter Preis | dito |
| BahnCard 100 | DB-Tarif-Pauschale | 10 EUR (60 Min) / 20 EUR (120 Min) |
| Deutschlandticket | DB-Tarif-Pauschale | 1,50 EUR pro Vorfall, max. 25 % Monatspreis |
| Zeitkarte (Monat/Jahr) | DB-Tarif-Pauschale | anteilig analog Deutschlandticket |
| BahnCard 25 / BahnCard 50 | gezahlter ermäßigter Preis | volle Fahrgastrechte auf ermäßigter Basis |

### Schritt 2: Endziel-Verspätung in Minuten

Maßgeblich: tatsächliche Ankunftszeit (Türöffnung, Art. 3 Nr. 18 VO) minus planmäßige Ankunftszeit am gebuchten Endziel.

### Schritt 3: Stufe wählen

- 60–119 Min → 25 %
- ≥ 120 Min → 50 %

### Schritt 4: Pro Reisendem berechnen

Art. 19 VO ist persönlich. Pro Fahrkarte eigener Anspruch. Bei 3 Reisenden mit gleichem Ticketpreis: 3 × Einzelanspruch.

### Schritt 5: Mindestbetrag prüfen

Liegt der Einzelanspruch unter 4 EUR (Art. 19 Abs. 8): DB darf ablehnen. **Praxistipp:** Beträge in Verspätungs-Antrag zusammenfassen — bei Mehrpersonen-Familien rechnerisch über 4 EUR pro Antrag, auch wenn Einzelposition darunter.

### Schritt 6: Nebenforderungen (separat zur Entschädigung)

- **Erstattung / Hilfsleistung Auslagen** (Art. 18 Abs. 5; Art. 20 VO): Verpflegung, Hotel, Transport. Belege vorlegen.
- **Eigenständige Beförderung** (Art. 18 Abs. 3 Unterabs. 2): Wenn DB nicht binnen 100 Min nach planmäßiger Abfahrt Alternativen mitgeteilt hat — notwendige, angemessene und zumutbare Kosten.
- **SPNV-Sonderfall § 11 Abs. 2 EVO:** bis 120 EUR für Taxi/Bus bei Nachtfahrt 0–5 Uhr oder letzter Verbindung.
- **Verzugszinsen** ab Mahnung (§§ 286, 288 BGB) — Verbraucher 5 Prozentpunkte über Basiszinssatz.

## Beispielberechnungen

### Beispiel 1: Sparpreis Fernverkehr, 105 Min Verspätung, 3 Reisende

```
Ticket: Sparpreis, 79,00 EUR pro Person
Verspätung am Zielort: 105 Min → Stufe 1 (25 %)
Pro Person: 79,00 × 25 % = 19,75 EUR
3 Reisende: 3 × 19,75 = 59,25 EUR
Mindestbetrag 4 EUR — überschritten.
Endbetrag: 59,25 EUR Entschädigung
```

### Beispiel 2: Flexpreis, 130 Min Verspätung, 1 Reisender

```
Ticket: Flexpreis, 152,00 EUR
Verspätung am Zielort: 130 Min → Stufe 2 (50 %)
Berechnung: 152,00 × 50 % = 76,00 EUR
Endbetrag: 76,00 EUR Entschädigung
```

### Beispiel 3: Sparpreis Hin- und Rückfahrt, Verspätung nur Hinfahrt

```
Ticket: Sparpreis Hin- und Rückfahrt 158,00 EUR (=2 × 79,00 EUR rechnerisch je Strecke)
Bezugsgröße Hinfahrt nach Art. 19 Abs. 3 Satz 2: halber Fahrpreis = 79,00 EUR
Verspätung Hinfahrt: 90 Min → Stufe 1 (25 %)
Entschädigung: 79,00 × 25 % = 19,75 EUR
```

### Beispiel 4: BahnCard 100

```
Verspätung am Zielort: 75 Min
DB-Tarif-Pauschale (TBP § 7): 10 EUR
Endbetrag: 10 EUR
```

### Beispiel 5: Deutschlandticket

```
Verspätung am Zielort: 80 Min (Regio Berlin–Cottbus)
DB-Tarif-Pauschale: 1,50 EUR
Monatsdeckel (25 % von 58 EUR = 14,50 EUR) — noch nicht erreicht
Endbetrag: 1,50 EUR
Hinweis: Bei reinem SPNV kommt § 11 EVO kumulativ hinzu, wenn Voraussetzungen erfüllt.
```

### Beispiel 6: Wochenkarte (50 EUR, 5 Tage Gültigkeit, Verspätung 70 Min)

```
Tagespreis: 50 / 5 = 10 EUR
Stufe 1: 25 %
Entschädigung: 10 × 25 % = 2,50 EUR
Mindestbetrag 4 EUR — nicht erreicht. DB kann ablehnen.
Praxis: mit Wochenkarte mehrere Verspätungen sammeln; ab 4 EUR-Schwelle gemeinsam beantragen
       (Art. 19 Abs. 2 VO 2021/782 erlaubt das ausdrücklich für Zeitfahrkarten).
```

### Beispiel 7: Anschlussverlust unter Durchgangsfahrkarte

```
Ticket: Sparpreis 79,00 EUR Berlin–München via Erfurt (Anschluss verpasst durch Verspätung)
Anschluss erst 2 Stunden später; Endziel-Verspätung: 150 Min → Stufe 2 (50 %)
Entschädigung: 79,00 × 50 % = 39,50 EUR
Maßgebliche Verspätung: Endziel, nicht einzelne Etappe (Art. 12 Abs. 3 VO).
```

## Mehrpersonen-Konstellation

```yaml
berechnung:
  fall-id: FGR-2026-0042
  reisende:
    - name: Mueller, Hans
      ticketart: sparpreis
      preis-eur: 79.00
      stufe: 1
      anteil-prozent: 25
      einzelanspruch-eur: 19.75
    - name: Mueller, Eva
      ticketart: sparpreis
      preis-eur: 79.00
      stufe: 1
      anteil-prozent: 25
      einzelanspruch-eur: 19.75
    - name: Mueller, Lea
      ticketart: sparpreis-kind
      preis-eur: 39.50          # Kindertarif
      stufe: 1
      anteil-prozent: 25
      einzelanspruch-eur: 9.88
  gesamt-entschaedigung-eur: 49.38
  zusatz-auslagen:
    verpflegung-eur: 12.50
    hotel-eur: 0
    taxi-eur: 0
  gesamt-anspruch-eur: 61.88
```

## Pauschalreise

Bei Pauschalreise mit Bahn-Anteil: Ansprüche aus VO 2021/782 (gegen EVU) und §§ 651a ff. BGB (gegen Reiseveranstalter) **kumulieren** grundsätzlich. Anrechnung nach BGH: keine Doppelvergütung; bei dem Reiseveranstalter erstrittene Beträge werden auf die EVU-Entschädigung verrechnet und umgekehrt.

→ Bei komplexer Konstellation Verweis auf `verbraucherschutzrecht-pruefer` oder allgemeines Reiserecht-Plugin.

## Ausgabe

```
Berechnung Entschädigung
Fall-ID: FGR-2026-0042
Zug: ICE 503 Berlin Hbf — München Hbf
Datum: 12.05.2026
Endziel-Verspätung: 105 Minuten (Stufe 1 — 25 %)

Pro Reisendem:
 Hans Mueller     | Sparpreis | 79,00 EUR | 25 % | 19,75 EUR
 Eva Mueller      | Sparpreis | 79,00 EUR | 25 % | 19,75 EUR
 Lea Mueller (mj) | Sparpreis Kindertarif | 39,50 EUR | 25 %  |  9,88 EUR

Summe Entschädigung Art. 19 VO 2021/782:        49,38 EUR
Auslagen Verpflegung Art. 20 VO 2021/782:      +12,50 EUR
Gesamtforderung:                                61,88 EUR

Mindestbetrag 4 EUR pro Fahrkarte: erreicht (alle Einzelpositionen über 4 EUR).
Verzugszinsen ab Mahnung gem. §§ 286, 288 BGB.

Nächster Skill: forderung-an-db-erste-stufe
```

## Leitentscheidungen Berechnung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `forderung-an-db-erste-stufe`

_Erstes Forderungsschreiben an das DB-Servicecenter Fahrgastrechte. Erfasst Anspruchsteller (alle Reisenden mit Vollmachten) Anspruchsgrundlage Art. 19 VO 2021/782 plus Art. 18 und Art. 20 sowie ggf. § 11 EVO konkrete Berechnung Frist zur Zahlung (typisch vier Wochen) Bankverbindung. Zwei Variante..._

# Forderungsschreiben — Erste Stufe

## Empfänger

- **DB Dialog GmbH — Servicecenter Fahrgastrechte**, 60647 Frankfurt am Main (Postanschrift; korrekter Postweg auch bei Online-Antrag, wenn schriftliche Spur gewünscht).
- **Alternativ:** Online-Formular auf [bahn.de/fahrgastrechte](https://www.bahn.de/service/informationen-buchung/fahrgastrechte) oder über die **DB Navigator-App**. Empfehlung: parallel postalisch UND online für Beweisspur.
- Bei **Konkurrenz-EVU** (FlixTrain, ÖBB, NWB, Transdev, Go-Ahead etc.): Adresse des konkreten EVU auf bahn.de/impressum bzw. Webseite des Betreibers.

## Struktur

### 1. Briefkopf

```
[Vor- und Nachname Hauptansprechender]
[Strasse Hausnummer]
[PLZ Ort]
[Tel] [E-Mail]
[IBAN]

[Datum]

An:
DB Dialog GmbH
Servicecenter Fahrgastrechte
60647 Frankfurt am Main

Betreff: Antrag auf Entschädigung gemäß Art. 19 VO (EU) 2021/782
         Zug [Zugnummer] am [Datum] von [Abfahrtsbahnhof] nach [Zielbahnhof]
         Auftrags-/Buchungscode [PNR]
```

### 2. Sachverhalt knapp

```
Sehr geehrte Damen und Herren,

ich nehme Bezug auf den unter dem Buchungscode [PNR] gebuchten Zug
[Zugnummer] am [Datum] von [Abfahrtsbahnhof] nach [Zielbahnhof].

Folgende Reisende waren betroffen:
 - [Name 1], geboren [Datum 1]
 - [Name 2], geboren [Datum 2]
 - [Name 3], geboren [Datum 3] (minderjährig, vertreten durch
   die unterzeichnenden Erziehungsberechtigten)

Vollmachten der Mitreisenden sind beigefügt (Anlagen K[N] ff.).

Der genannte Zug [erreichte das Ziel mit X Stunden Verspätung / fiel aus /
fuhr nach geänderter Streckenführung].

Geplante Ankunft am Zielbahnhof [Bahnhof]: [HH:MM]
Tatsächliche Ankunft am Zielbahnhof (Türöffnung am Bahnsteig): [HH:MM]
Endziel-Verspätung: [X] Minuten.
```

### 3. Rechtliche Begründung

```
1. Anspruchsgrundlage: Art. 19 Abs. 1 VO (EU) 2021/782 des Europäischen
   Parlaments und des Rates vom 29. April 2021 über die Rechte und
   Pflichten der Fahrgäste im Eisenbahnverkehr.

2. Anwendungsbereich: Der Zug wird von [Operating EVU] als zugelassenem
   Eisenbahnverkehrsunternehmen im Geltungsbereich der VO 2021/782 ausgeführt
   (Art. 2 Abs. 1 VO).

3. Tatbestand: Endziel-Verspätung von [X] Minuten am Zielbahnhof. Damit
   greift Art. 19 Abs. 1 [lit. a: 25 % bei 60–119 Min / lit. b: 50 % bei
   ab 120 Min] VO.

4. Höhe des Anspruchs:
   Tatsächlicher Fahrpreis pro Reisendem: [P] EUR
   Anteil [25 / 50] %: [E] EUR pro Reisendem
   Anzahl Reisende: [N]
   Gesamtentschädigung Art. 19 VO: [G] EUR

[ggf. weiterhin:]

5. Hilfeleistung Art. 20 VO:
   Da der Zug das Ziel mit mehr als 60 Minuten Verspätung erreichte,
   bestand Anspruch auf Verpflegung in angemessenem Verhältnis zur
   Wartezeit. Eine Hilfeleistung wurde nicht angeboten. Ich beanspruche
   Erstattung der selbst getragenen Verpflegungskosten in Höhe von
   [V] EUR (Belege anbei).

6. Eigenbeförderung Art. 18 Abs. 3 Unterabs. 2 VO:
   Die DB hat binnen 100 Minuten nach planmäßiger Abfahrtszeit keine
   Weiterreise-Option mitgeteilt. Ich war daher zur Eigenbeförderung
   berechtigt und beanspruche Erstattung der notwendigen, angemessenen
   und zumutbaren Kosten in Höhe von [F] EUR.

[falls SPNV:]

7. § 11 EVO: Bei der gebuchten Verbindung handelt es sich um eine SPNV-Fahrt.
   Wegen einer absehbaren Verspätung von mehr als 20 Minuten am Zielort
   greifen die zusätzlichen Rechte aus § 11 Abs. 1 EVO.

8. Eine Befreiung von der Entschädigungspflicht nach Art. 19 Abs. 10 VO ist
   nicht gegeben. [Falls DB im Voraus eine Begründung mitgeteilt hat,
   diese zitieren und entkräften. Beispielsweise: Streiks des DB-Personals
   und Handlungen der Infrastrukturbetreiber sind nach Art. 19 Abs. 10
   Unterabs. 2 VO ausdrücklich nicht als außergewöhnliche Umstände
   anzuerkennen.] Die Beweislast für außergewöhnliche Umstände und für
   die Ergreifung zumutbarer Maßnahmen trägt das Eisenbahnverkehrsunternehmen.
```

### 4. Forderung

```
Hiermit fordere ich Sie auf, den Gesamtbetrag in Höhe von

   [Gesamtbetrag] EUR

zuzüglich gegebenenfalls weiterer Auslagen — Belege beiliegend —
auf folgendes Konto zu überweisen:

   Inhaber: [Name]
   IBAN:    DE [...]
   BIC:     [...]

bis spätestens [Datum + 4 Wochen].

Hinweis: Die VO 2021/782 sieht in Art. 19 Abs. 7 eine Bearbeitungsfrist
von einem Monat ab Antragseingang vor. Eine Auszahlung in Form von
Gutscheinen wird ausdrücklich nicht akzeptiert; auf Wunsch des Fahrgasts
ist die Entschädigung in Geld zu leisten (Art. 19 Abs. 7 Satz 2 VO).

Sollten Sie meinem Antrag nicht oder nicht vollständig entsprechen, werde
ich:

 a) Widerspruch einlegen und parallel
 b) die Schlichtungsstelle Reise & Verkehr e.V. (vormals söp,
    Fasanenstraße 81, 10623 Berlin) anrufen — das Verfahren ist für
    Verbraucherinnen und Verbraucher kostenfrei (Verbraucher-Entgelt-Regeln
    nach § 23 VSBG i.V.m. der Verfahrensordnung der Stelle),
 c) anschließend Klage zum zuständigen Amtsgericht erheben.
```

### 5. Anlagen

```
Anlagen:
 K1  Buchungsbestätigung Zug [Zugnummer] vom [Datum]
 K2  Fahrkarten / E-Tickets aller Reisenden
 K3  Verspätungs- / Ausfallmitteilung (App-Screenshot, SMS, E-Mail)
 K4  Foto Anzeigetafel Zielbahnhof mit tatsächlicher Ankunftszeit
 K5  Belege Auslagen (Verpflegung, ggf. Hotel, ggf. Ersatzbeförderung)
 K6  Vollmacht [Name Reisende:r 2]
 K7  Vollmacht [Name Reisende:r 3 minderjährig — durch Erziehungsberechtigte]
```

### 6. Schluss

```
Mit freundlichen Grüßen

[Unterschrift]
[Name]
```

## Versand

- **Postversand per Einschreiben mit Rückschein** — beste Beweisform.
- **Parallel** Online-Antrag über bahn.de oder DB Navigator — schnellere Bearbeitung; Eingangsnummer dokumentieren.
- **Konkurrenz-EVU:** dort übliches Reklamationsformular nutzen; postalisch parallel an Niederlassungs-Adresse.

## Verzugszinsen

- Verzug spätestens mit Fristablauf (§ 286 Abs. 1 BGB). Die im Schreiben gesetzte Zahlungsfrist (typisch vier Wochen) und die monatliche Bearbeitungsfrist aus Art. 19 Abs. 7 VO sind nicht deckungsgleich (vier Wochen sind 28 Tage; ein Monat richtet sich nach §§ 187 ff. BGB und ist regelmäßig 30 oder 31 Tage). Praxisempfehlung: die Frist so setzen, dass sie nicht vor Ablauf des Monats nach Art. 19 Abs. 7 VO endet, um Streit über den Verzugszeitpunkt zu vermeiden.
- Verzugszinsen Verbraucher 5 Prozentpunkte über Basiszinssatz (§ 288 Abs. 1 BGB).

## Bearbeitungsfristen

- **Erstattung** (Art. 18 Abs. 5 VO): 30 Tage.
- **Entschädigung** (Art. 19 Abs. 7 VO): 1 Monat.
- **Beschwerdeantwort** (Art. 27 Abs. 2 VO): 1 Monat (in begründeten Fällen bis 3 Monate).

## Praxis-Hinweise

- Die DB lehnt Anträge oft mit Verweis auf "fehlende Mindestbearbeitungsfrist 30 Tage" ab, bevor sie auf den Antrag eingeht. **Argumentation:** Frist gilt für DIE BEARBEITUNG, nicht für Antragstellung.
- Voucher als Entschädigung: nur, wenn Verbraucher ausdrücklich zustimmt. Andernfalls Geldanspruch (Art. 19 Abs. 7 Satz 2 VO).
- Bei mehrfachen Verspätungen mit Zeitkarte: gesammelte Geltendmachung erlaubt (Art. 19 Abs. 2 VO) — Vorteil bei Mindestbetrag-Schwelle.

## Ausgabe

- `forderung-erste-stufe-<datum>.md` und PDF (über Anlagen-Skill).
- Tagesnotiz: Reaktionsfrist vorgemerkt (1 Monat ab Eingang).
- Hinweis: bei Reaktion mit Standardausrede den Skill `db-ablehnungsgruende-pruefen` aufrufen, dann `fahrgastrechte-widerspruch`.

## Anlagen-Übergabe

Unmittelbar nach Erstellung des Schreibens den Skill `fahrgastrechte-anlagen-bauen` aufrufen.

Übergabe-Schema:

```yaml
schriftsatz: forderung-erste-stufe-<datum>.md
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                           # erzeugt zusätzlich Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold            # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

## Zentrale Normen

- Art. 19 Abs. 1, 2, 3, 7, 8 VO (EU) 2021/782 — Entschädigung
- Art. 18 Abs. 1, 3 Unterabs. 2, 5 VO (EU) 2021/782 — Erstattung / Eigenbeförderung
- Art. 20 VO (EU) 2021/782 — Hilfeleistung
- Art. 7 VO (EU) 2021/782 — Verzichtsverbot
- § 11 EVO — SPNV-Zusatzrechte
- § 195, § 199 Abs. 1 BGB — Verjährung
- § 286 Abs. 1, § 288 Abs. 1 BGB — Verzug und Verzugszinsen

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `klage-amtsgericht-fahrgast`

_Klageentwurf zum Amtsgericht in Fahrgastrechte-Angelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bis zehntausend Euro (i.d.F. seit 01.01.2026). Oertlich wahlweise Abfahrts- oder Zielbahnhof (Art. 7 Nr. 1 lit. b VO 1215/2012 Bruessel-Ia plus § 29 ZPO) oder Sitz / Niederlassung..._

# Klage zum Amtsgericht (Fahrgastrechte)

## Disclaimer

Eine Klage ist ein Rechtsschriftsatz mit Konsequenzen (Gerichtskosten, Streitwert-Risiko, Auslagen). Vor Einreichung Beweislage prüfen — auf konkrete Vorhalt-Antworten der DB reagieren können. Bei komplexen Fällen oder höherem Streitwert anwaltliche Hilfe einholen; ggf. Rechtsschutzversicherung prüfen.

## Voraussetzungen

- **Vorgerichtliches Verfahren** abgeschlossen (Forderung an DB → Widerspruch → Schlichtung) oder begründet nicht durchgeführt.
- **Schriftform** des Klageantrags (§ 253 ZPO).
- **Klagepartei** ist der Anspruchsteller (jeder Reisende eigener Anspruch — Streitgenossenschaft möglich nach § 60 ZPO).
- **Beklagte** das ausführende Eisenbahnverkehrsunternehmen.
- **Streitwert** Summe der Ansprüche aller Reisenden; bis 10 000 EUR AG-Zuständigkeit.

## Sachliche Zuständigkeit

- **§ 23 Nr. 1 GVG i.d.F. seit 01.01.2026:** Amtsgericht bei Streitwerten bis **zehntausend Euro**.
- Über 10 000 EUR: Landgericht (§ 71 GVG); Anwaltszwang nach § 78 Abs. 1 ZPO.

## Örtliche Zuständigkeit

- **Brüssel-Ia (VO (EU) 1215/2012) Art. 7 Nr. 1 lit. b** in Verbindung mit **§ 29 ZPO** — Erfüllungsort der Dienstleistung: Abfahrts- oder Zielbahnhof. **Fahrgast hat Wahlrecht.**
- Subsidiär **§§ 12, 13, 17 ZPO** — Sitz / Niederlassung der beklagten Gesellschaft:
  - **DB Fernverkehr AG:** Stephensonstraße 1, 60326 Frankfurt am Main → AG Frankfurt am Main.
  - **DB Regio AG:** Stephensonstraße 1, 60326 Frankfurt am Main → AG Frankfurt am Main.
  - **DB AG (Konzern):** Europaplatz 1, 10557 Berlin → AG Berlin-Mitte.
  - **FlixTrain GmbH:** Friedenheimer Brücke 16, 80639 München → AG München.
- Bei Pauschalreise zusätzlich Wohnsitz Reiseveranstalter / Verbrauchersitz nach § 651y BGB i.V.m. Brüssel-Ia Art. 17 ff.

## Klagestruktur

### 1. Rubrum

```
An das Amtsgericht [Ort des Abfahrts-/Zielbahnhofs / Sitz EVU]

In Sachen

   [Hauptkläger:in] und weitere Kläger:innen (siehe Anlage Vollmachten)
    — vertreten durch [Hauptkläger:in] aufgrund Vollmacht —

   gegen

   [Name EVU, z. B. DB Fernverkehr AG]
   vertreten durch den Vorstand
   Stephensonstraße 1
   60326 Frankfurt am Main

erhebe ich Klage und beantrage:
```

### 2. Anträge

```
1. Die Beklagte wird verurteilt, an die Klägerin zu 1 [Name]
   [Betrag 1] EUR nebst Verzugszinsen in Höhe von 5 Prozentpunkten über dem
   jeweiligen Basiszinssatz seit [Datum Frist + 1] zu zahlen.

2. Die Beklagte wird verurteilt, an den Kläger zu 2 [Name]
   [Betrag 2] EUR nebst Zinsen wie zu 1.

3. Die Beklagte wird verurteilt, an die Klägerin zu 3 [Name, minderjährig]
   vertreten durch die Erziehungsberechtigten [Namen]
   [Betrag 3] EUR nebst Zinsen wie zu 1.

4. Die Beklagte trägt die Kosten des Rechtsstreits.

5. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 Prozent des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar (§ 709 ZPO).
```

### 3. Streitwert

```
Streitwert: [Summe der Einzelansprüche]
```

### 4. Sachverhalt

```
1. Die Klagepartei buchte am [Datum] bei der Beklagten gemäß Buchungscode
   [PNR] die Beförderung auf dem Zug [Zugnummer] am [Datum] von
   [Abfahrtsbahnhof] nach [Zielbahnhof] in 2. Klasse.
   Beweis: Buchungsbestätigung, Anlage K1.

2. Die Klagepartei meldete sich am Tag der Reise pünktlich zum Antritt.
   Sie hatte ein gültiges Ticket und alle Reisedokumente.
   Beweis: E-Tickets / Fahrkarten, Anlage K2.

3. Der Zug erreichte das Ziel mit [X] Minuten Verspätung am Zielbahnhof
   (gemessen an der Türöffnung am Bahnsteig, Art. 3 Nr. 18 VO (EU) 2021/782).
   Beweis: Verspätungsmitteilung der DB, Anlage K3.
           Foto Anzeigetafel Zielbahnhof, Anlage K4.

4. [Falls Anschlussverlust]:
   Aufgrund der Verspätung des Zuges [Etappe 1] verpasste die Klagepartei
   den Anschlusszug [Etappe 2] in [Umsteigebahnhof] und konnte erst mit
   dem nächsten Zug um [HH:MM] weiterreisen.
   Beweis: Buchung im Rahmen einer einheitlichen Durchgangsfahrkarte
           (Art. 12 Abs. 3 VO 2021/782), Anlage K1.

5. [Falls Eigenbeförderung]:
   Da die Beklagte binnen 100 Minuten nach planmäßiger Abfahrt keine
   Alternativbeförderung mitgeteilt hat, organisierte die Klagepartei
   um [HH:MM] eine eigene Weiterreise mit [FlixTrain / Fernbus / Taxi]
   in Höhe von [Betrag] EUR.
   Beweis: Belege Anlage K5.

6. [Falls Verpflegung / Hotel]:
   Während der Wartezeit von [X] Stunden hat die Beklagte keine
   Verpflegung bereitgestellt (Art. 20 Abs. 1 lit. a VO 2021/782). Die
   Klagepartei hat Verpflegung im Wert von [Betrag] EUR selbst beschafft.
   Beweis: Kassenbelege, Anlage K6.

7. Mit Antrag vom [Datum] beantragte die Klagepartei beim Servicecenter
   Fahrgastrechte die Entschädigung. Mit Schreiben vom [Datum] lehnte die
   Beklagte den Antrag mit folgender Begründung ab: "[Wortlaut Ablehnung]".
   Beweis: Antrag und Ablehnungsschreiben, Anlagen K7 und K8.

8. Mit Widerspruch vom [Datum] hat die Klagepartei Widerspruch eingelegt.
   Die Beklagte hat darauf [nicht reagiert / erneut ablehnend geantwortet
   am [Datum]].
   Beweis: Widerspruch und ggf. zweite Ablehnung, Anlagen K9 und K10.

9. Das Schlichtungsverfahren bei der Schlichtungsstelle Reise & Verkehr e.V.
   [wurde durchgeführt — siehe Spruch Anlage K11 / wurde abgebrochen am
   [Datum] / wurde nicht durchgeführt, weil [Begründung]].

10. Die Beklagte hat bis heute keine Zahlung geleistet.
```

### 5. Rechtliche Würdigung

```
1. Anspruchsgrundlage: Art. 19 Abs. 1 [lit. a / lit. b] VO (EU) 2021/782
   des Europäischen Parlaments und des Rates vom 29. April 2021 (ABl. L 172
   vom 17.5.2021, S. 1).

2. Anwendungsbereich: Der Zug wurde von der Beklagten als zugelassenem
   Eisenbahnverkehrsunternehmen im Geltungsbereich der VO 2021/782 ausgeführt
   (Art. 2 Abs. 1 VO).

3. Tatbestand: Die Klagepartei erreichte den Zielbahnhof mit einer Verspätung
   von [X] Minuten gegenüber der planmäßigen Ankunft.

   Maßgeblich ist die Verspätung am Zielbahnhof — der Zeitpunkt der
   Türöffnung am Bahnsteig nach Art. 3 Nr. 18 VO 2021/782.

   [bei Anschlussverlust]:
   Innerhalb der Durchgangsfahrkarte sind alle Etappen als einheitlicher
   Beförderungsvertrag zu behandeln (Art. 12 Abs. 3 VO 2021/782).
   Maßgeblich ist die Verspätung am Endziel, nicht die einzelne
   Etappenverspätung.

4. Höhe des Anspruchs:
   Tatsächlich gezahlter Fahrpreis: [P] EUR pro Reisendem.
   Anteil [25 / 50] % gemäß Art. 19 Abs. 1 [lit. a / lit. b] VO:
   [E] EUR pro Reisendem.
   Bei [N] Reisenden ergibt sich eine Gesamtentschädigung von [G] EUR.

   [Falls weitere Posten:]
   Zuzüglich Eigenbeförderung Art. 18 Abs. 3 Unterabs. 2 VO: [F] EUR.
   Zuzüglich Hilfeleistung Art. 20 VO: [V] EUR.
   Gesamt: [GESAMT] EUR.

5. Keine Befreiung wegen außergewöhnlicher Umstände (Art. 19 Abs. 10 VO).
   Die Beklagte hat sich auf "[Wortlaut Ablehnungsbegründung]" berufen.
   Dies verfängt aus folgenden Gründen nicht:

   [Hier konkrete Gegenargumentation aus
    `db-ablehnungsgruende-pruefen`]

   Beispielsweise bei Streik-Begründung:
   Streiks des Personals des Eisenbahnverkehrsunternehmens sind nach
   Art. 19 Abs. 10 Unterabs. 2 VO 2021/782 ausdrücklich von der
   Befreiungsregel ausgenommen. Auch Streiks der Mitarbeiter
   Handlungen oder Unterlassungen anderer Unternehmen, die dieselbe
   Infrastruktur nutzen, sowie der DB Netz AG als Infrastrukturbetreiber
   fallen ebenfalls unter diese
   Ausnahme.

   Die Beweislast für außergewöhnliche Umstände und die Ergreifung
   zumutbarer Maßnahmen liegt bei der Beklagten.

6. Verzug: Mit Ablauf der mit Schreiben vom [Datum] gesetzten Zahlungsfrist
   trat Verzug ein (§ 286 Abs. 1 BGB). Verzugszinsen gemäß § 288 Abs. 1
   BGB.

7. Zuständigkeit:
   Sachlich: § 23 Nr. 1 GVG i. d. F. seit 01.01.2026 — Amtsgericht bei
   Streitwerten bis zehntausend Euro.
   Örtlich: § 29 ZPO i.V.m. Art. 7 Nr. 1 lit. b VO (EU) 1215/2012
   (Brüssel-Ia) — Erfüllungsort am Abfahrts- oder Zielbahnhof; subsidiär
   §§ 12, 17 ZPO Sitz der Beklagten.

8. Verzichtsverbot: Etwaige Vertragsbedingungen der Beklagten, die den
   Anspruch der Klagepartei einschränken, sind nach Art. 7 VO 2021/782
   für den Fahrgast nicht verbindlich.
```

### 6. Beweisangebote

```
Beweise:
   Urkundenbeweis durch beigefügte Anlagen K1 bis K[N].
   Parteivernehmung der Klagepartei zum Verlauf vor Ort.
   Im Bestreitensfall: Beiziehung der Betriebsaufzeichnungen der Beklagten
   (Leidis-NK / DiRail) zur tatsächlichen Ankunftszeit am Zielbahnhof —
   §§ 421 ff. ZPO.
   Zeugnis: [Name Mitreisende], geladen über die Klagepartei.
```

### 7. Anlagen

```
K1  Buchungsbestätigung mit PNR
K2  E-Tickets / Fahrkarten aller Reisenden
K3  Verspätungs- / Ausfallmitteilung der DB
K4  Foto Anzeigetafel Zielbahnhof
K5  Belege Ersatzbeförderung (FlixTrain / Bus / Taxi)
K6  Kassenbelege Verpflegung
K7  Erstantrag vom [Datum] an DB Servicecenter
K8  Ablehnungsschreiben der DB vom [Datum]
K9  Widerspruch vom [Datum]
K10 Zweite Ablehnung vom [Datum] (sofern vorhanden)
K11 Schlichtungsspruch (sofern vorhanden)
K12 Vollmachten der Mitreisenden
```

### 8. Unterschrift

```
[Ort, Datum]
[Name (und ggf. Initialen aller Kläger:innen oder Vollmachtsverweis)]
```

## Anwaltszwang

- **Kein Anwaltszwang** vor dem Amtsgericht (§ 78 ZPO e contrario).
- Selbstvertretung möglich; bei komplexer Beweislage anwaltliche Hilfe empfohlen.
- Vor Klage: Skill `db-ablehnungsgruende-pruefen` nutzen, damit Gegenargumentation belastbar ist.

## Versandweg

- **Schriftlich per Post** oder zur Niederschrift bei der Geschäftsstelle des AG.
- **Elektronisch** bei beA / EGVP-Zugang (Privatpersonen üblicherweise nicht).

## Streitgenossenschaft

- **Mehrere Reisende** können als Streitgenossen klagen (§ 60 ZPO).
- Eine Klageschrift für alle — separate Anträge je Kläger:in.
- Vollmacht der Mitreisenden erforderlich (Skill `vollmacht-mitreisende`).

## Ausgabe

- `klage-fahrgast-<datum>.md` und PDF.
- Anlagenkonvolut über Anlagen-Skill.
- Streitwert- und Kostenberechnung.
- Hinweis zur Gerichtswahl Abfahrtsbahnhof / Zielbahnhof / Sitz EVU.

## Anlagen-Übergabe

Unmittelbar nach Erstellung der Klageschrift den Skill `fahrgastrechte-anlagen-bauen` aufrufen — ohne ordnungsgemäßes Anlagenkonvolut ist die Klage nicht einreichungsfähig.

Übergabe-Schema:

```yaml
schriftsatz: klage-fahrgast-<datum>.md
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # beA verlangt geschlossenes PDF
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold
bezeichnung: "Anlage K"
```

beA-Konvention:

- Anlagen werden im beA als separate PDFs eingereicht, jeweils mit Stempel oben rechts in Arial 12 FETT.
- Dateiname ohne Umlaute und ohne Leerzeichen: `Anlage_K_1.pdf`, `Anlage_K_2.pdf`, …
- Reihenfolge muss der Erwähnung im Schriftsatz entsprechen.
- Sammel-PDF `Schriftsatz_mit_Anlagen.pdf` zusätzlich für eigenes Aktenexemplar.

## Hinweise

- **Verjährung** drei Jahre nach §§ 195, 199 Abs. 1 BGB ab Jahresende der Verspätung.
- Anrufung der **Schlichtungsstelle Reise & Verkehr** hemmt die Verjährung (§ 204 Abs. 1 Nr. 4 BGB) — bei Klage nach Schlichtung Stichtage prüfen.
- **Beweislast Türöffnung am Zielbahnhof:** Klagepartei kann durch Foto Anzeigetafel oder Zeugen darlegen; bei Bestreiten DB-interne Daten erforderlich (§§ 421 ff. ZPO).

## Zentrale Anspruchsgrundlagen und Normen

- Art. 19 Abs. 1, 7, 8, 10 VO (EU) 2021/782 — Entschädigung
- Art. 18 Abs. 1, 3 Unterabs. 2, 5 VO (EU) 2021/782 — Erstattung / Eigenbeförderung
- Art. 20 VO (EU) 2021/782 — Hilfeleistung
- Art. 7 VO (EU) 2021/782 — Verzichtsverbot
- Art. 12 Abs. 3 VO (EU) 2021/782 — Durchgangsfahrkarte / Anschlussverlust
- § 11 EVO — SPNV-Zusatzrechte
- § 23 Nr. 1 GVG i. d. F. seit 01.01.2026 — Amtsgericht bis 10.000 EUR
- § 29 ZPO; Art. 7 Nr. 1 lit. b VO (EU) 1215/2012 — Brüssel-Ia
- §§ 12, 13, 17 ZPO — allgemeine Zuständigkeit
- § 253 ZPO — Klagemindestinhalt
- § 60 ZPO — Streitgenossenschaft
- §§ 286, 288 BGB — Verzug und Verzugszinsen
- § 195, § 199 Abs. 1 BGB — Verjährung
- § 204 Abs. 1 Nr. 4 BGB — Verjährungshemmung durch Schlichtung
- § 709 ZPO — vorläufige Vollstreckbarkeit gegen Sicherheitsleistung; bei geringen Streitwerten alternativ § 708 Nr. 11 i.V.m. § 711 ZPO erwägen (Prüfung im Einzelfall)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage vor Klageerhebung

1. Schlichtung versucht? → Schlichtungsstelle Reise & Verkehr e.V. erst aus­schöpfen (kostenfrei); danach Klage.
2. Verjährung geprüft? → 3 Jahre ab Jahresende des Verspätungsjahres (§ 195 i.V.m. § 199 BGB).
3. Streitwert berechnet? → bei > 10 000 EUR Landgericht (§ 71 GVG) + Anwaltszwang § 78 ZPO.
4. Beweismittel vollständig? → Buchung, E-Tickets, Verspätungs-Bestätigung, Mahnschreiben.
5. Richtige Beklagte? → ausführendes EVU (nicht Reiseveranstalter, nicht DB AG-Konzern bei Tochter-Strecke), Art. 19 Abs. 1 VO 2021/782 i.V.m. Art. 3 Nr. 1 VO.

## Adressat & Tonfall

Adressat: Amtsgericht am gewählten Gerichtsstand — Tonfall sachlich-juristisch; Klageschrift ohne Anwaltszwang trotzdem nach § 253 ZPO-Mindestinhalt strukturiert (Parteien, Antrag, Begründung, Beweisangebote).

---

## Skill: `schlichtung-reise-verkehr-anrufen`

_Schlichtungsantrag bei der Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) nach erfolgloser Reklamation beim Eisenbahnverkehrsunternehmen. Kostenfrei für Verbraucher nach VSBG. Voraussetzung Vorgerichtliche Geltendmachung beim EVU mindestens vier Wochen ohne befriedigende Antwort oder Ableh..._

# Schlichtungsstelle Reise & Verkehr e.V. anrufen

## Schlichtungsstelle Reise & Verkehr e.V.

| Punkt | Wert |
|---|---|
| Trägerverein | Schlichtungsstelle Reise & Verkehr e.V. |
| Anerkennung | nach §§ 4 ff. VSBG; benannt vom Bundesamt für Justiz |
| Adresse | Fasanenstraße 81, 10623 Berlin |
| Web | schlichtungsstelle-reise-verkehr.de |
| Antragsweg | Online-Formular, postalisch, per E-Mail |
| Kosten Verbraucher | **kostenfrei** |
| Erfolgsquote (statistisch) | ca. 50–60 % einigender Vorschlag |
| Bindungswirkung | Schlichtungsspruch bindet die DB / EVU nicht zwingend, wird aber regelmäßig akzeptiert; Fahrgast kann auch nach Abschluss noch klagen |

## Voraussetzungen (§§ 4 ff. VSBG, Art. 28 VO 2021/782)

1. **Vorgerichtliche Geltendmachung** beim EVU. Der Anspruch muss zunächst bei der DB / dem EVU geltend gemacht und mindestens **vier Wochen** lang ohne befriedigende Antwort geblieben oder abgelehnt worden sein.
2. **Keine anhängige Klage**: Die Schlichtung scheidet aus, wenn der Anspruch bereits gerichtlich anhängig ist.
3. **Anwendungsbereich:** Personenverkehr (Eisenbahn, Bus, Flug, Schiff). Eisenbahn ist Kerngeschäft.
4. **Frist:** Es gibt keine gesetzliche allgemeine Ausschlussfrist für den Schlichtungsantrag. Maßgeblich ist die materielle Verjährung des Anspruchs (drei Jahre nach §§ 195, 199 BGB). Die Verfahrensordnung der Schlichtungsstelle Reise & Verkehr e.V. ist vor Antragstellung auf etwaige Spezialfristen zu prüfen.

## Inhalt des Schlichtungsantrags

### 1. Online-Formular auf schlichtungsstelle-reise-verkehr.de

Direktester Weg. Felder analog zur Postantrag-Vorlage unten; Belege als PDF hochladbar.

### 2. Postalisches Anschreiben (Vorlage)

```
[Vor- und Nachname]
[Adresse]
[Tel] [E-Mail]

[Ort], den [Datum]

An:
Schlichtungsstelle Reise & Verkehr e.V.
Fasanenstraße 81
10623 Berlin

Betreff: Antrag auf Durchführung eines Schlichtungsverfahrens
         Verspätungsanspruch nach VO (EU) 2021/782

Sehr geehrte Damen und Herren,

hiermit beantrage ich die Durchführung eines Schlichtungsverfahrens
gegen das Eisenbahnverkehrsunternehmen:

   DB Dialog GmbH — Servicecenter Fahrgastrechte
   60647 Frankfurt am Main
   (für die DB Fernverkehr AG / DB Regio AG)

[oder bei Konkurrenz-EVU entsprechende Anschrift]

I. Sachverhalt

Am [Datum] reiste ich mit dem Zug [Zugnummer] von [Abfahrtsbahnhof]
nach [Zielbahnhof]. Buchungscode (PNR / Auftrags-Nr.): [PNR].
Planmäßige Ankunft: [HH:MM]
Tatsächliche Ankunft: [HH:MM]
Endziel-Verspätung: [X] Minuten

II. Bisheriger Verlauf

1. Mit Schreiben/Antrag vom [Datum] habe ich beim Servicecenter Fahrgastrechte
   der DB Entschädigung gemäß Art. 19 VO (EU) 2021/782 beantragt.
   Vorgangs-/Aktenzeichen: [Nr.]

2. Mit Ablehnungsschreiben vom [Datum] hat die DB den Antrag mit folgender
   Begründung abgelehnt: "[wortlautnah]"

3. Mit Widerspruch vom [Datum] habe ich gegen die Ablehnung Widerspruch
   eingelegt. [Falls weitere Reaktion: kurz beschreiben.]

4. Die DB hat seit [Datum] nicht reagiert / hat erneut abgelehnt
   mit Schreiben vom [Datum].

III. Anspruch und Berechnung

Anspruchsgrundlage: Art. 19 Abs. 1 lit. [a/b] VO (EU) 2021/782.

Fahrpreis pro Reisendem:   [P] EUR
Anteil [25/50] %:          [E] EUR
Anzahl Reisende:           [N]
Entschädigung Gesamt:      [G] EUR

[ggf.] zzgl. Hilfeleistung Art. 20 VO:        [V] EUR
[ggf.] zzgl. Eigenbeförderung Art. 18 VO:     [F] EUR

Gesamtforderung:            [GESAMT] EUR

IV. Gegen den Ablehnungsgrund

Der von der DB angeführte Ablehnungsgrund "[Grund]" verfängt nicht, weil
[konkrete Gegenargumentation — siehe Skill `db-ablehnungsgruende-pruefen`].

V. Gewünschte Schlichtung

Ich beantrage einen Schlichtungsvorschlag der Schlichtungsstelle, der zur
Zahlung der genannten [GESAMT] EUR auf das nachstehende Konto führt:

   Kontoinhaber: [Name]
   IBAN: [DE...]
   BIC: [...]

VI. Belege (in Kopie beigefügt)

 - Buchungsbestätigung / E-Ticket
 - Verspätungs- / Ausfallmitteilung
 - Foto Anzeigetafel Zielbahnhof
 - Erstantrag vom [Datum] an DB Servicecenter
 - Ablehnungsschreiben der DB vom [Datum]
 - Widerspruch vom [Datum]
 - Belege zu Auslagen (Verpflegung, Hotel, Taxi)
 - Vollmachten der Mitreisenden

VII. Erklärung

Ich erkläre, dass der Anspruch nicht gerichtlich anhängig ist und kein
gerichtliches Verfahren oder anderes Schlichtungsverfahren beabsichtigt
ist, solange das hiesige Verfahren läuft.

Mit freundlichen Grüßen

[Name]
```

## Ablauf des Schlichtungsverfahrens

1. **Eingangsbestätigung** der Schlichtungsstelle (typisch binnen 1–2 Wochen).
2. **Stellungnahme des EVU** binnen ca. 4 Wochen.
3. **Schlichtungsvorschlag** der Schlichtungsstelle (typische Dauer Verfahren: 3–6 Monate).
4. **Annahme oder Ablehnung** durch beide Seiten. Wenn beide annehmen → Vergleich; sonst Verfahren als gescheitert beendet.

## Wirkung auf Verjährung

Anrufung der Schlichtungsstelle **hemmt** die Verjährung gem. § 204 Abs. 1 Nr. 4 BGB (Einleitung des Verfahrens vor einer durch das Bundesamt für Justiz nach § 32 VSBG anerkannten Stelle). Hemmung dauert für die Zeit des Verfahrens; nach Beendigung läuft die Frist weiter (mit 6-Monats-Mindest-Restfrist gemäß § 204 Abs. 2 BGB).

→ Praxisrelevant: Auch wenn die Schlichtung lange dauert, ist der Anspruch verjährungsrechtlich geschützt.

## Wann zur Schlichtung, wann direkt klagen?

| Situation | Empfehlung |
|---|---|
| Streitwert < 1 000 EUR, Vergleichswille der DB möglich | Schlichtung — kostenfrei, gute Erfolgsquote |
| DB hat mehrfach abgelehnt, keine Vergleichsbereitschaft | Direkt Klage |
| Streitwert > 5 000 EUR, hohe Komplexität | Klage; Schlichtung als Vorstufe optional |
| Verjährung naht | Klage bevorzugt; Schlichtung hemmt aber auch |
| Mehrere Mitreisende, kumulierte Forderung | Schlichtung zuerst — gut für Familienfälle |

## Wenn Schlichtung scheitert

→ Skill `klage-amtsgericht-fahrgast` aufrufen. Streitwert: kumulierte Einzelansprüche aller Reisenden. § 23 Nr. 1 GVG: bis 10.000 EUR Amtsgericht.

## Adressen weiterer Schlichtungsstellen (Konkurrenz / Spezial)

- **Bundesverband Verbraucherzentrale (vzbv)** — bei systematischen UWG-Themen.
- **Eisenbahn-Bundesamt (EBA)** — Aufsichtsbehörde; nimmt Beschwerden entgegen, aber keine Einzelfall-Schlichtung.

## Ausgabe

- `schlichtungsantrag-<datum>.md` und PDF mit allen Belegen verlinkt.
- Übergabe an `fahrgastrechte-anlagen-bauen` für Anlagen-Bundle.
- Hinweis auf Verjährungshemmung mit Stichdatum.

---

## Skill: `ticket-und-reisedaten-erfassen`

_Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestaetigungen Reservierungen Foto-Belegen für Fahrgastrechte-Mandate. Extrahiert Buchungscode (PNR) Auftragsnummer Reisetag Strecke Operating EVU Ticketart (Flexpreis Sparpreis Super Sparpreis BC100 Deutschlandticket Zeitkarte) Klasse Preis..._

# Ticket- und Reisedaten erfassen

## Eingaben

Typische Belege:

- **Buchungsbestätigung** der DB / FlixTrain / ÖBB als PDF / E-Mail
- **E-Ticket** mit IATA-/UIC-Barcode (Foto, PDF)
- **Sitzplatzreservierung** (separat oder integriert)
- **Reservierungsbestätigung** (Bahn-App-Screenshot, ausgedrucktes Ticket)
- **Verspätungs- oder Annullierungsbenachrichtigung** der DB (SMS, E-Mail, App-Push)
- **Korrespondenz** mit DB Servicecenter Fahrgastrechte
- **Belege zu Auslagen** (Hotel, Taxi, Verpflegung) — Kassenbon, Rechnung
- **DB Navigator-Screenshots** mit Verspätungs-Anzeigen

## Pflichtfelder

```yaml
fall-id: FGR-2026-0042
reisedatum: 2026-05-12
reisende:
  - name: Mueller, Hans
    geburtsdatum: 1972-08-15
    rolle: hauptbuchender
  - name: Mueller, Eva
    geburtsdatum: 1975-03-22
    rolle: ehepartner
  - name: Mueller, Lea
    geburtsdatum: 2010-06-18
    rolle: minderjährig

buchungscode: ABC123          # PNR / Auftragsnummer
buchung-bei: DB Vertrieb GmbH # Verkaufender Vertriebsweg (bahn.de, DB Reisezentrum, Reisebüro)
buchungsdatum: 2026-04-12

ticket:
  art: sparpreis              # flexpreis | sparpreis | super-sparpreis | bahncard-100 | deutschlandticket | zeitkarte | reisepass-tarif
  klasse: 2                   # 1 oder 2
  preis-eur: 79.00            # tatsächlich gezahlter Preis
  zugbindung: ja              # bei sparpreis/super-sparpreis grundsätzlich ja
  bahncard: BC50              # null | BC25 | BC50 | BC100

verbindung-gebucht:
  abfahrt:
    bahnhof: Berlin Hbf
    iata-uic: 8011160
    planmaessig: 2026-05-12T08:25:00+02:00
  ziel:
    bahnhof: Muenchen Hbf
    iata-uic: 8000261
    planmaessig: 2026-05-12T13:20:00+02:00
  zuege:
    - nr: ICE 503
      operating-evu: DB Fernverkehr AG
      abschnitt: Berlin Hbf - Muenchen Hbf
  einheitliche-pnr: ja        # → Durchgangsfahrkarte nach Art. 12 VO

verbindung-tatsaechlich:
  abfahrt-ist: 2026-05-12T08:45:00+02:00   # +20 Min
  ankunft-ist: 2026-05-12T15:05:00+02:00   # +1h 45 Min am Endziel
  zug-tatsaechlich: ICE 503                # ggf. anderer Zug bei Umbuchung
  umsteige-bahnhoefe: []
  endziel-verspaetung-min: 105             # ≥ 60 Min → 25 % Anspruch (ab 120: 50 %)

stoerung:
  art: verspaetung            # verspaetung | zugausfall | anschlussverlust | vorverlegung | nichtbefoerderung
  ursache-laut-db: technischer Defekt
  bekanntgabe-am: 2026-05-12T07:50:00+02:00
  bekanntgabe-wie: app        # app | sms | email | aushang | schalter
  ersatz-angebot: ja
  ersatz-detail: Ersatzfahrt im selben ICE 503 mit Verspätung
  hilfeleistung-erhalten:
    verpflegung: nein
    hotel: nein
    transport: nein

auslagen:
  taxi-eur: 0
  hotel-eur: 0
  verpflegung-eur: 12.50
  belege: [belege/2026-05-12/kassenbon-bahnhofsimbiss.pdf]

belege:
  - typ: buchungsbestaetigung
    pfad: belege/2026-05-12/buchung-ICE503.pdf
  - typ: e-ticket
    pfad: belege/2026-05-12/e-ticket-mueller.pdf
  - typ: stoerungsmeldung
    pfad: belege/2026-05-12/db-navigator-verspaetung.png
  - typ: ankunft-anzeigetafel
    pfad: belege/2026-05-12/foto-anzeigetafel-muenchen.jpg
  - typ: kassenbon
    pfad: belege/2026-05-12/kassenbon-bahnhofsimbiss.pdf
```

## OCR / PDF-Extraktion

- Bei PDF-Tickets automatische Extraktion von PNR / Auftragsnummer, Zugnummer, Datum, Bahnhöfen.
- Bei Foto-Belegen OCR; bei Konfidenz unter 90 Prozent Prüfer-Flag für manuelle Bestätigung.
- DB-Auftragsnummern haben das Format einer 12-stelligen alphanumerischen ID (Bahn-App) oder einer 6-stelligen PNR (klassischer Vertrieb).
- UIC-Stationscodes (8011160 Berlin Hbf, 8000261 München Hbf) prüfen — frei verfügbar bei DB Open Data.

## Beweis-Sicherung der tatsächlichen Ankunftszeit

Maßgeblich ist die **Türöffnung am Zielbahnhof** (Art. 3 Nr. 18 VO 2021/782). Beweiswege:

1. **DB Navigator** speichert die tatsächliche Ankunftszeit unter "Verbindungs-Details" — Screenshot zeitnah sichern.
2. **Fahrgastrechte-Formular der DB Bahn**: Wird die Verspätung bei der DB beantragt, generiert das System eine **Verspätungsbestätigung mit DB-eigenen Daten**. Diese ist im Streit das stärkste Beweismittel.
3. **Schalter-Stempel** auf der Fahrkarte bei Annullierung / Verspätung (älterer Weg).
4. **Foto der Bahnhofs-Anzeigetafel** mit Uhrzeit und tatsächlich angezeigter Ankunftszeit (Beweis im Bestreitensfall).
5. **Zeugen** — Mitreisende.

## DB-Zugverfolgung (intern bei DB)

Die DB verfügt über interne Aufzeichnungen aller Zugbewegungen (Betriebsdatenbank LeiDis-NK / DiRail). Im Klageverfahren kann die Vorlage beantragt werden (§§ 421 ff. ZPO Urkundenbeweis). Vorprozessuale Auskunft über § 242 BGB (sekundäre Darlegungslast).

## Mehrere Reisende

Pro Reise wird **ein** Anspruchsfall mit mehreren Reisenden erfasst. **Jeder Reisende hat einen eigenen Anspruch** (Art. 19 VO ist persönlich); Mindestbetrag 4 EUR ebenfalls pro Fahrkarte. Bei Klage je Reisender eigener Antrag (Streitgenossenschaft möglich nach § 60 ZPO). Vollmacht über `vollmacht-mitreisende`.

## Anschlussverlust unter Durchgangsfahrkarte

Wenn die Buchung mehrere Züge mit **einer PNR** enthält (Art. 12 Abs. 3 VO 2021/782), ist die **Gesamtverspätung am Endziel** maßgeblich — nicht die Verspätung eines einzelnen Etappenzuges. Der Anschlussverlust ist im Yaml unter `umsteige-bahnhoefe` zu erfassen.

Bei **mehreren separat gebuchten Tickets** (eigenständige PNRs) ist jeder Vertrag getrennt zu betrachten — Anschluss-Garantie greift nicht, außer Fahrkartenverkäufer / Reiseveranstalter hat sie ausdrücklich versprochen (Art. 12 Abs. 4 VO).

## Operating EVU prüfen

- DB-Vertrieb verkauft auch Konkurrenz-Tickets. Bei NWB-, ÖBB-, FlixTrain-Strecken im DB-Vertriebssystem: **Operating EVU ist das tatsächlich fahrende Unternehmen** — nicht DB Fernverkehr.
- Anspruchsgegner ist immer das **ausführende EVU** (Art. 19 Abs. 1 VO).
- Bei DB Regio: häufig Auftrag durch Bundesländer; passivlegitimiert bleibt DB Regio.
- Bei FlixTrain: FlixTrain GmbH, Friedenheimer Brücke 16, 80639 München.

## Pauschalreise-Konstellation

Wenn die Bahnreise Teil einer Pauschalreise (Reiseveranstalter) ist, ergänzen sich Ansprüche aus VO 2021/782 (gegen EVU) und §§ 651a ff. BGB (gegen Reiseveranstalter). Mitteilung an `verspaetung-und-anschlussverlust-einordnen` und ggf. Verweisung auf `prozessrecht` oder `verbraucherschutzrecht-pruefer`.

## Ausgabe

- `fallakte.yaml` mit allen Stammdaten.
- `belegliste.md` mit Prüfer-Flags für fehlende Belege.
- `naechste-schritte.md` Empfehlung auf nächsten Skill (`verspaetung-und-anschlussverlust-einordnen` oder direkt `entschaedigung-berechnen` bei klarer Faktenlage).

## Leitentscheidungen Datenerfassung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `verspaetung-und-anschlussverlust-einordnen`

_Ordnet das Stoerungsereignis rechtlich ein: Verspaetung (Art. 19 VO 2021/782 bei mindestens 60 Min Endziel), Zugausfall (Art. 18), verpasster Anschluss unter Durchgangsfahrkarte (Art. 12 Abs. 3) oder Vorverlegung. Differenzierung Fernverkehr vs SPNV (mit § 11 EVO 20 Min Schwelle). Behandelt Mehrf..._

# Verspätung, Zugausfall oder Anschlussverlust einordnen

## Tatbestände im Überblick

| Tatbestand | Norm | Konsequenz |
|---|---|---|
| **Verspätung am Zielort ≥ 60 Min** | Art. 19 VO + Art. 18 VO | Entschädigung (25/50 %) UND Wahlrecht Erstattung/Weiterreise |
| **Verspätung am Zielort < 60 Min** | Art. 19 Abs. 9 VO | Kein Entschädigungsanspruch (Mindestschwelle nicht erreicht) |
| **Zugausfall** | Art. 18 + Art. 19 VO | Wahlrecht Erstattung/Weiterreise; Entschädigung wenn Endziel-Verspätung ≥ 60 Min |
| **Verpasster Anschluss (Einheits-PNR)** | Art. 12 Abs. 3 VO | Wie Verspätung; Endziel-Maßstab |
| **Verpasster Anschluss (separate PNRs)** | Art. 12 Abs. 4–5 VO | Anspruch je Vertrag separat; ggf. 75 %-Entschädigung des Fahrkartenverkäufers |
| **Vorverlegung der Abfahrt** | nicht ausdrücklich in VO 2021/782 — analog Art. 8 | Falls Fahrgast den vorverlegten Zug nicht erreicht: Behandlung wie Ausfall |
| **Nichtbeförderung (Überbuchung im Eisenbahnverkehr)** | praktisch selten; Art. 18 analog | Wahlrecht; ggf. Schadensersatz nach Art. 26 Abs. 5 Anhang I CIV |
| **SPNV — 20-Min-Schwelle für Alternativzug** | § 11 EVO | Recht auf Wechsel auf anderen Zug (nicht: Entschädigung — die folgt Art. 19 VO) |

## Differenzierungs-Schema

### Schritt 1: Welcher Verkehr?

- **Fernverkehr** (ICE, IC, EC, FlixTrain, ÖBB) → Art. 19 VO ungeschmälert (60/120 Min).
- **SPNV** (RE, RB, S-Bahn im SPNV-Sinn) → Art. 19 VO ungeschmälert PLUS § 11 EVO Zusatzrechte (20-Min-Schwelle für Alternativzug; 120-EUR-Limit Ersatzbeförderung bei Nachtfahrt).
- **Stadt-/Vorortverkehr (S-Bahn-Tarifgebiete, U-Bahn)** — Deutschland hat ausgenommen; Ansprüche nach Tarifbedingungen und nationalen Sonderregeln.

### Schritt 2: Welche Ankunftsverspätung am ZIELORT (nicht Etappe)?

| Verspätung am Endziel | Anspruch |
|---|---|
| 0–59 Min | kein Entschädigungsanspruch nach Art. 19 |
| 60–119 Min | 25 % des Fahrpreises |
| ≥ 120 Min | 50 % des Fahrpreises |

**Achtung:** Auch wenn ein Etappenzug 120 Min Verspätung hatte, der Fahrgast aber durch günstigen Anschlusszug nur 30 Min am Endziel verspätet war: **kein Anspruch** (Art. 19 Abs. 9 VO).

### Schritt 3: Durchgangsfahrkarte oder separate Tickets?

- **Einheitliche PNR**: alle Etappen sind Durchgangsfahrkarte → Anspruch bezieht sich auf Endziel-Verspätung (Art. 12 Abs. 3 VO).
- **Separate PNRs** (z.B. Hin- mit Sparpreis, Anschlussfahrt mit anderem Ticket): jede Strecke einzeln zu bewerten; Anschluss-Garantie greift nicht. Ausnahme Art. 12 Abs. 4 VO: bei Fahrkartenverkäufer / Reiseveranstalter kombiniert + Fehlinformation → 75 %-Entschädigung des Vermittlers.

### Schritt 4: Tatbestand benennen

```yaml
einordnung:
  tatbestand: verspaetung-am-zielort-mindestens-60-min
  norm-anker:
    - Art. 19 Abs. 1 lit. a VO 2021/782   # 25 %
    - Art. 18 Abs. 1 VO 2021/782          # Wahlrecht
    - Art. 20 VO 2021/782                 # Hilfeleistung
  endziel-verspaetung-min: 105
  verspaetungsstufe: stufe-1-25-prozent   # stufe-1-25 | stufe-2-50
  durchgangsfahrkarte: ja
  spnv: nein                              # ja triggert zusätzlich § 11 EVO
  folge-skills:
    - entschaedigung-berechnen
    - forderung-an-db-erste-stufe
    - eigenbefoerderung-und-betreuung-art-18   # falls Auslagen entstanden
```

## Spezialfall: Vorverlegung

VO 2021/782 regelt Vorverlegung **nicht ausdrücklich**, anders als die Fluggast-VO 261/2004 (für die der EuGH Vorverlegungen als Annullierung behandelt — Aktenzeichen vor Verwendung in einem Schriftsatz über curia.europa.eu live verifizieren, nicht aus Modellwissen zitieren). In der Eisenbahn-Praxis: Die DB schickt ggf. eine Verfrühungs-Mitteilung; der Fahrgast erreicht den Zug nicht.

**Sachgerechte Einordnung:** Wenn der Fahrgast den vorverlegten Zug nicht erreichen kann und keine anderweitige Beförderung mit gleicher Ankunftszeit angeboten wird, ist die Situation funktional einem Ausfall gleichzustellen. Art. 18 (Wahlrecht) und Art. 19 (Entschädigung) sind entsprechend anwendbar.

→ Hinweis: Live-Recherche bei curia.europa.eu oder bundesgerichtshof.de prüfen, ob neuere Entscheidung speziell zu Eisenbahn-Vorverlegung vorliegt.

## Spezialfall: Nichtbeförderung (Eisenbahn-Überbuchung)

Im Eisenbahnverkehr selten (anders als bei Flügen). Wenn die DB / FlixTrain die Beförderung verweigert (z.B. wegen Überfüllung in der reservierten 1. Klasse): Wahlrecht analog Art. 18; Schadensersatz Art. 26 Abs. 5 Anhang I CIV. Im Klagefall sehr individuell — vorbereitende Eilprüfung erforderlich.

## Spezialfall: Streiks DB-Personal

Die häufigste Standardausrede der DB: "Streik = außergewöhnlicher Umstand". **Falsch.** Art. 19 Abs. 10 Unterabs. 2 VO 2021/782 schließt Streiks des EVU-Personals **ausdrücklich** von der Befreiungsregel aus. Auch Streiks bei DB Netz AG (Infrastrukturbetreiber) sind nach derselben Norm nicht befreiend.

## Spezialfall: Wetter

- Normales Winterwetter (Schnee, Glatteis) → kein außergewöhnlicher Umstand. EVU muss sich vorbereiten.
- Extremereignisse (Jahrhundert-Sturm, Hochwasser, Lawinen) → **kann** außergewöhnlich sein. Beweislast EVU; muss zumutbare Vorkehrungen darlegen.

## Spezialfall: Personenschäden (Notarzteinsatz auf der Strecke)

- Im Grunde Drittverschulden (Art. 19 Abs. 10 lit. c VO) — befreiend, wenn nicht vermeidbar.
- ABER: Wenn DB den Personenschaden zumutbar erkennen konnte und nicht alternative Routenführung anbot, bleibt sie haftungspflichtig.

## Spezialfall: Bauarbeiten und Baustellenfahrplan

Bauarbeiten gehören zum betrieblichen Risiko des EVU — kein außergewöhnlicher Umstand. Wenn der Baustellenfahrplan vorab veröffentlicht war und der Fahrgast wusste, dass eine reduzierte Streckenkapazität existiert: dennoch Anspruch, solange die VO-Schwellen erreicht sind. Bei Vorab-Information über konkreten Zugausfall vor Ticketkauf entfällt der Anspruch (Art. 19 Abs. 9 VO).

## Ausgabe

```
Einordnung Fahrgastrechte-Fall FGR-2026-0042
Datum: 12.05.2026
Strecke: Berlin Hbf — München Hbf (ICE 503, Einheits-PNR)
Geplante Ankunft: 13:20
Tatsächliche Ankunft: 15:05 (Türöffnung am Bahnsteig)
Endziel-Verspätung: 105 Minuten

Tatbestand: Verspätung am Zielort 60–119 Minuten (Art. 19 Abs. 1 lit. a VO 2021/782)

Anspruchsgrundlage:
 - Art. 19 Abs. 1 lit. a VO 2021/782 — 25 % des Fahrpreises Entschädigung
 - Art. 18 VO 2021/782 — Wahlrecht (hier nicht relevant, Fahrt durchgeführt)
 - Art. 20 VO 2021/782 — Hilfeleistung war geschuldet (Verpflegung)

Befreiung? Nein:
 - DB-Begründung "technischer Defekt" → nach VO 2021/782 Art. 19 Abs. 10 zählt nicht zu den
   außergewöhnlichen Umständen außerhalb des Eisenbahnbetriebs. Beweislast DB.

Operating EVU: DB Fernverkehr AG (passivlegitimiert)

Höhe (vorab):
 - Pro Reisendem: 25 % von 79,00 EUR Ticketpreis = 19,75 EUR
 - 3 Reisende: 59,25 EUR Entschädigung
 - Verpflegungs-Auslage: 12,50 EUR (Art. 20 VO)
 - Gesamt: 71,75 EUR

Nächster Skill: entschaedigung-berechnen (exakte Berechnung)
                forderung-an-db-erste-stufe (Antrag stellen)
```

## Leitentscheidungen Einordnung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `vollmacht-mitreisende`

_Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde Reisegruppe) damit ein Hauptansprechpartner deren Fahrgastrechte-Anspruch im Schriftverkehr Schlichtungs- und Gerichtsverfahren mitvertreten kann. Pro Person eigene Vollmacht mit Inhalt Bezug auf Buchung Mandatsumfang Empfangsvollmac..._

# Vollmacht für Mitreisende

## Vollmacht-Inhalt (Erwachsene)

```
Vollmacht

Ich, [Vor- und Nachname Vollmachtgeber:in],
geboren am [Geburtsdatum],
wohnhaft [Adresse],

bevollmächtige hiermit

   [Vor- und Nachname Vollmachtnehmer:in],
   geboren am [Geburtsdatum],
   wohnhaft [Adresse],

mich in allen Angelegenheiten betreffend meinen Anspruch aus dem Bahn-Reise

   Buchungscode (PNR / Auftrags-Nr.): [PNR]
   Zugnummer: [Zugnummer]
   Datum: [Datum]
   Strecke: [Abfahrtsbahnhof] nach [Zielbahnhof]
   Operating EVU: [z. B. DB Fernverkehr AG]

zu vertreten. Die Vollmacht umfasst insbesondere:

   - vorgerichtliche Geltendmachung der Ansprüche nach VO (EU) 2021/782
     und EVO gegenüber dem Eisenbahnverkehrsunternehmen,
   - Korrespondenz mit dem Servicecenter Fahrgastrechte der Deutschen Bahn
     bzw. dem zuständigen EVU,
   - Anrufung der Schlichtungsstelle Reise & Verkehr e.V. (vormals söp),
   - Klageerhebung beim zuständigen Amtsgericht,
   - Empfangnahme von Zahlungen und Schriftverkehr,
   - Untervollmacht an eine Rechtsanwältin oder einen Rechtsanwalt sowie
     Vertretung im Rechtsstreit.

Diese Vollmacht gilt bis zum Widerruf in Textform.

Ort, Datum
___________________

___________________________________________
[Vor- und Nachname Vollmachtgeber:in]
```

## Vollmacht für Minderjährige

Bei minderjährigen Mitreisenden ist die Vollmacht durch die erziehungsberechtigten Personen zu erteilen (regelmäßig beide Elternteile gemeinsam, sofern beide sorgeberechtigt — § 1626 BGB):

```
Vollmacht für minderjähriges Kind

Wir, die Erziehungsberechtigten

   [Name Mutter / Vater 1], geboren am [Datum], wohnhaft [Adresse]
   [Name Vater / Mutter 2], geboren am [Datum], wohnhaft [Adresse]

vertreten unser minderjähriges Kind

   [Vor- und Nachname Kind], geboren am [Datum]

und bevollmächtigen hiermit

   [Vor- und Nachname Vollmachtnehmer:in]

in dessen / deren Namen die Ansprüche aus dem Bahn-Reise

   PNR / Auftrags-Nr.: [Nummer]
   Zug:                [Zugnummer]
   Datum:              [Datum]
   Strecke:            [Abfahrtsbahnhof] nach [Zielbahnhof]

nach VO (EU) 2021/782 geltend zu machen — einschließlich vorgerichtlich,
Schlichtungsverfahren bei der Schlichtungsstelle Reise & Verkehr e.V. und
gerichtlich vor dem Amtsgericht.

Ort, Datum
___________________

___________________________________________     ___________________________________________
[Mutter / Vater 1]                                 [Vater / Mutter 2]
```

## Vollmacht für Reisegruppen (mehrere unverwandte Erwachsene)

Bei Reisegruppen — Freundeskreis, Kollegen, Vereinsfahrt — gleiches Schema wie bei Erwachsenen-Vollmacht, individuell je Person. Empfehlung: Excel-/CSV-Liste der Vollmachtgebenden mit Zuordnung zu eigenen Tickets im Anlagenkonvolut.

## Datenschutzhinweis (Art. 13 DSGVO)

Bei der Verarbeitung personenbezogener Daten der Mitreisenden im Rahmen der Fahrgastrechte-Geltendmachung gibt der Hauptansprechpartner als Verantwortlicher Hinweis auf:

- Verantwortlicher: Hauptansprechpartner (Name, Adresse, Kontakt)
- Zweck: Geltendmachung Anspruch nach VO (EU) 2021/782 / EVO
- Empfänger: EVU (DB / FlixTrain / etc.); Schlichtungsstelle Reise & Verkehr; ggf. Amtsgericht
- Speicherdauer: bis zur Anspruchsbefriedigung plus drei Jahre (Verjährungsperiode)
- Rechte: Auskunft, Berichtigung, Löschung, Beschwerde bei Aufsichtsbehörde

## Versand der Vollmachten

```
Vorlage E-Mail an Mitreisende:

Liebe / Lieber [Name],

beigefügt findest du den Entwurf einer Vollmacht in Sachen unserer
verspäteten / annullierten Bahn-Reise [Zug] vom [Datum].

Bitte unterschreibe und schicke das Dokument zurück (per Post, Foto oder
Scan reicht). Damit kann ich deinen Entschädigungsanspruch von etwa [X] EUR
zusammen mit den anderen geltend machen — ohne dass du selbst etwas tun
musst.

Ich melde mich, sobald die DB / das EVU reagiert.

Liebe Grüße
[Name]
```

## Aktenablage

- **Originale oder Scans hoher Qualität** sind Pflichtanlagen jedes Schriftverkehrs.
- **Aufbewahrung** bis Anspruchsabwicklung plus drei Jahre (Verjährung).
- **Datenschutz beachten** — keine unnötige Weiterleitung an Dritte.

## Anwaltliche Vertretung

Bei Übergabe an eine Anwältin oder einen Anwalt: die anwaltliche Untervollmacht ist in der Vollmacht ausdrücklich erfasst ("Untervollmacht an eine Rechtsanwältin oder einen Rechtsanwalt"). Die Kanzlei legt regelmäßig ein eigenes Vollmachtsformular bei.

## Leitentscheidungen Vollmacht / Familienvertretung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

- `vollmacht-<name>-<datum>.md` (eine Datei pro Mitreisendem) und PDF.
- Vollmacht-Versandliste mit Status (versendet / unterschrieben / vorliegt).
- Hinweis: Eingang der unterschriebenen Vollmachten ist Voraussetzung für die Mitvertretung in Forderungs-, Schlichtungs- und Klageverfahren.

---

## Skill: `widerspruch`

_Erstellt einen formellen Widerspruchsbrief gegen die Ablehnung eines Fahrgastrechte-Antrags der Deutschen Bahn oder eines anderen Eisenbahnverkehrsunternehmens. Verwende diesen Skill immer wenn der Nutzer ein Ablehnungsschreiben des DB-Servicecenters Fahrgastrechte (oder gleichwertiger EVU-Stelle..._

# Fahrgastrechte-Widerspruch — Skill

## Eingabedokumente

Der Nutzer lädt typischerweise drei Dokumente hoch:

1. **Ablehnungsschreiben der DB** — der Brief, in dem die DB den Antrag ablehnt (PDF oder Foto).
2. **Ursprünglicher Antrag** — das vom Nutzer ausgefüllte Fahrgastrechte-Formular bzw. die Bestätigung (PDF, Screenshot oder Foto).
3. **Ticket / Fahrkarte** — das Original-Ticket als Nachweis der Buchung (PDF aus der DB-App, Scan oder Foto).

Die Dokumente können als PDF (digital oder gescannt), als Screenshots oder als Fotos vorliegen. Wenn die Qualität nicht ausreicht, um relevante Informationen zu extrahieren, den Nutzer bitten, die fehlenden Daten manuell einzugeben.

## Workflow

### Schritt 1: Dokumente identifizieren und lesen

Sichte die hochgeladenen Dateien. Jedes Dokument identifizieren:

- **Ablehnungsschreiben erkennen an:** Absender "Servicecenter Fahrgastrechte", "DB Dialog" oder vergleichbarer EVU-Stelle; Formulierungen wie "Ihrem Antrag können wir leider nicht entsprechen"; Aktenzeichen / Vorgangsnummer.
- **Antrag erkennen an:** Formulardaten mit Verbindungsdaten, Verspätungsangaben, IBAN.
- **Ticket erkennen an:** Buchungsnummer (PNR / Auftragsnummer), Zugbindung, Tarifart, Reisedatum, Verbindungsdetails.

Bei Bildern / Screenshots: Inhalte direkt aus dem Kontext lesen. Bei gescannten PDFs mit schlechter Textextraktion: Seiten als Bilder rendern und visuell auswerten.

### Schritt 2: Relevante Daten extrahieren

Aus den drei Dokumenten folgende Informationen sammeln:

**Aus dem Ticket:**

- Ticketart: Flexpreis, Sparpreis, Super Sparpreis, BahnCard-Ticket, Deutschlandticket, Zeitkarte
- Buchungsnummer / Auftragsnummer
- Reisedatum
- Gebuchte Verbindung (Abfahrt → Ankunft, Umstiege, Zugnummern)
- Preis
- Zugbindung ja/nein (Flexpreis = keine Zugbindung → alternative Verbindungen erlaubt)
- Klasse (1./2.)
- Reisende:r
- Operating EVU (falls Konkurrenz auf bahn.de gebucht)

**Aus dem Antrag:**

- Tatsächlich gefahrene Verbindung
- Angegebene Endziel-Verspätung
- Datum des Antrags
- Beantragter Erstattungs-/Entschädigungsbetrag
- Ggf. Verpflegungskosten, Taxikosten, Hotelkosten

**Aus dem Ablehnungsschreiben:**

- Aktenzeichen / Vorgangsnummer
- Datum des Schreibens
- Konkreter Ablehnungsgrund (genauen Wortlaut notieren)
- Sachbearbeiter (falls angegeben)
- Antwortadresse

### Schritt 3: Rechtliche Analyse

Lies die References dieses Plugins (`references/vo-2021-782-uebersicht.md`, `references/evo-2023-uebersicht.md`, `references/db-tarif-und-agb.md`) und konsultiere insbesondere `skills/db-ablehnungsgruende-pruefen/SKILL.md` für das vorliegende Ablehnungs-Muster.

Kernpunkte der Analyse:

1. **Verspätungsdauer prüfen:** Ab 60 Min = 25 % des Fahrpreises, ab 120 Min = 50 %.
2. **Ablehnungsgrund identifizieren und widerlegen** — Pinpoint auf den jeweiligen Eintrag in `db-ablehnungsgruende-pruefen`.
3. **Ticketart berücksichtigen:**
   - Flexpreis: keine Zugbindung → Fahrgast durfte jede beliebige Verbindung auf der Strecke nehmen.
   - Sparpreis: Zugbindung, aber bei voraussichtlich > 20 Min Verspätung aufgehoben (Ziffer 9 BB DB) → Reisender darf umsteigen.
   - Deutschlandticket / Zeitkarte: Entschädigung pauschal nach Tarifbestimmungen (siehe `db-tarif-und-agb.md`).
4. **Verpflegungs-, Taxi-, Hotel-Ansprüche:** Art. 18 Abs. 3 (100-Min-Frist Eigenbeförderung), Art. 20 (60-Min-Hilfeleistung), § 11 EVO (SPNV, 20-Min-Schwelle, 120-EUR-Höchstbetrag).
5. **Befreiung Art. 19 Abs. 10 VO:** Streiks DB-Personal, Handlungen Infrastrukturbetreiber sind ausdrücklich KEINE Befreiungsgründe.

### Schritt 4: Widerspruchsbrief erstellen

Der Brief wird als strukturierter Schriftsatz nach folgender Vorlage erstellt:

```
[Name und Adresse der/des Reisenden — aus dem Ticket/Antrag]
[Tel] [E-Mail]
[IBAN]

                                    DB Dialog GmbH
                                    Servicecenter Fahrgastrechte
                                    60647 Frankfurt am Main

[Ort], den [aktuelles Datum]

Betreff: Widerspruch gegen Ablehnung meines Entschädigungsantrags
         Aktenzeichen / Vorgangsnummer: [Nummer aus dem Ablehnungsschreiben]
         Mein Schreiben vom [Datum des Ursprungsantrags]
         Ihr Ablehnungsschreiben vom [Datum]

Sehr geehrte Damen und Herren,

[Absatz 1: Bezugnahme]
mit Schreiben vom [Datum] haben Sie meinen Entschädigungsantrag mit dem
Aktenzeichen [Vorgangsnummer] abgelehnt. Gegen diese Entscheidung lege ich
hiermit Widerspruch ein.

[Absatz 2: Sachverhaltsdarstellung]
Am [Datum] reiste ich mit dem [Zug + Nummer] von [Abfahrtsbahnhof] nach
[Zielbahnhof]. Planmäßige Ankunft war um [HH:MM]. Tatsächlich erreichte
ich das Ziel erst um [HH:MM], was einer Verspätung von [X] Minuten am
Zielort entspricht (gemessen an der Türöffnung am Bahnsteig, Art. 3 Nr. 18
VO (EU) 2021/782).

[Absatz 3 — nur bei Bedarf: Flexpreis-Argument]
Bei meinem Ticket handelt es sich um ein Flexpreis-Ticket ohne Zugbindung.
Ich war daher berechtigt, jeden beliebigen Zug auf meiner gebuchten Strecke
zu nutzen. Die in Ihrem Ablehnungsschreiben angeführte Argumentation, ich
hätte eine andere als die gebuchte Verbindung genutzt, geht ins Leere.
Maßgeblich ist ausschließlich die Verspätung am Zielbahnhof.

[Absatz 3 alternativ — Sparpreis mit Zugbindungsaufhebung]
Zwar handelt es sich um ein Sparpreis-Ticket mit grundsätzlicher Zugbindung.
Da jedoch bereits am Abfahrtsbahnhof eine Verspätung von mehr als 20 Minuten
am Zielort absehbar war, wurde die Zugbindung gemäß Ziffer 9 der
Beförderungsbedingungen der Deutschen Bahn aufgehoben. Ich war berechtigt,
einen alternativen Zug zu nutzen.

[Absatz 4: Rechtliche Begründung]
Gemäß Art. 19 Abs. 1 [lit. a / lit. b] VO (EU) 2021/782 steht mir bei einer
Verspätung von mehr als [60 / 120] Minuten am Zielort eine Entschädigung in
Höhe von [25 / 50] Prozent des Fahrpreises zu. Der von Ihnen angeführte
Ablehnungsgrund "[Grund zitieren]" steht diesem Anspruch nicht entgegen, da
[konkrete Gegenargumentation aus db-ablehnungsgruende-pruefen — mit
Pinpoint auf den entsprechenden Artikel der VO 2021/782 oder § der EVO].

[Absatz 5 — falls Verpflegung / Hotel / Eigenbeförderung]
Darüber hinaus steht mir gemäß [Art. 20 / Art. 18 Abs. 3 Unterabs. 2] VO
(EU) 2021/782 [eine angemessene Verpflegung / eine eigenständige Beförderung]
zu. Da mir [diese von Ihnen nicht bereitgestellt wurde / Sie binnen 100
Minuten keine Alternativverbindung mitgeteilt haben], war ich gezwungen,
[Verpflegung im Wert von / Ersatzbeförderung im Wert von] [Betrag] EUR
selbst zu beschaffen. Ich bitte um Erstattung dieser Kosten.

[Absatz 6: Forderung und Frist]
Ich bitte Sie, meinen Widerspruch innerhalb von vier Wochen ab Zugang dieses
Schreibens zu prüfen und mir die zustehende Entschädigung in Höhe von
[Gesamtbetrag] EUR auf das in meinem ursprünglichen Antrag genannte Konto
zu überweisen.

Sollte meinem Widerspruch nicht entsprochen werden, behalte ich mir vor,
die Schlichtungsstelle Reise & Verkehr e.V. (vormals söp — Schlichtungs-
stelle für den öffentlichen Personenverkehr), Fasanenstraße 81, 10623
Berlin, anzurufen. Das Verfahren ist für mich als Verbraucher kostenfrei
(§§ 4 ff. VSBG). Anschließend werde ich Klage zum zuständigen Amtsgericht
erheben.

Mit freundlichen Grüßen

[Name]

Anlagen:
 K1 Kopie des Originaltickets
 K2 Kopie des ursprünglichen Antrags
 K3 Kopie des Ablehnungsschreibens
 K4 [ggf. Belege Verpflegung / Hotel / Ersatzbeförderung]
```

#### Stilrichtlinien für den Brief

- **Sachlich und bestimmt**, nicht aggressiv — aber klar in der Forderung.
- **Konkrete Rechtsnormen** zitieren (VO (EU) 2021/782 mit Artikel, EVO mit Paragraph, DB-Tarifbestimmungen mit Ziffer).
- **Spezifisch auf den Ablehnungsgrund eingehen** — nicht pauschal argumentieren. Auf den entsprechenden Punkt in `db-ablehnungsgruende-pruefen` Bezug nehmen.
- **Fristen setzen:** Antwort in angemessener Frist erbitten. Praxis: vier Wochen oder ein Monat — die Bearbeitungsfrist nach Art. 19 Abs. 7 VO ist auf einen Monat angelegt; vier Wochen sind kürzer (28 Tage) und können bei Streit über den Verzugseintritt nachteilig sein.
- **Schlichtungsstelle erwähnen:** Hinweis auf Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) als nächsten Schritt.
- **Förmlich aber nicht übertrieben juristisch** — der Brief soll von einer Privatperson kommen können, nicht zwingend von einem Anwalt.

### Schritt 5: Ausgabe und Anlagen-Übergabe

1. Den fertigen Brief als `widerspruch-<datum>.md` und PDF in der Fallakte ablegen.
2. Direkt im Anschluss den Skill `fahrgastrechte-anlagen-bauen` aufrufen.

**Anlagen-Übergabe-Schema:**

```yaml
schriftsatz: widerspruch-<datum>.md
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # Sammel-PDF Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold        # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

3. Dem Nutzer eine kurze Zusammenfassung geben:
   - Welcher Ablehnungsgrund identifiziert wurde
   - Welche Gegenargumente verwendet wurden (mit Norm-Pinpoint)
   - Welcher Entschädigungsbetrag gefordert wird
   - Empfehlung für nächste Schritte (Schlichtungsstelle Reise & Verkehr falls erneut abgelehnt — Skill `schlichtung-reise-verkehr-anrufen`)

## Fehlende Informationen

Falls wichtige Informationen nicht aus den Dokumenten extrahiert werden können, den Nutzer gezielt fragen — zum Beispiel:

- "Wie viel Verspätung hattest du am Zielbahnhof genau (Türöffnung am Bahnsteig)?"
- "Hast du eine alternative Verbindung genommen? Wenn ja, welche?"
- "Hattest du Ausgaben für Verpflegung, Taxi oder Hotel? Wenn ja, wie viel?"
- "Wie lautet deine Adresse für den Briefkopf?"
- "War der Zug im Fernverkehr (ICE / IC / FlixTrain) oder Nahverkehr (RE / RB)?"

Nicht alle Informationen auf einmal abfragen, sondern nur das, was wirklich fehlt.

## Wichtige Hinweise

- **Kein "Keine-Rechtsberatung"-Disclaimer im Brief selbst** — der Brief soll wie ein normaler Widerspruch einer Privatperson aussehen.
- **Aber dem Nutzer im Chat sagen:** "Das ist keine Rechtsberatung. Im Zweifel einen Anwalt oder eine Verbraucherzentrale konsultieren."
- **Datum:** Immer das aktuelle Datum verwenden, nicht das Datum des Ablehnungsschreibens.
- **Beschwerdefrist Art. 27 VO:** Die 3-Monats-Frist ist eine Verfahrensfrist — keine Ausschlussfrist für den materiellen Anspruch. § 195 BGB (3 Jahre) bleibt maßgeblich.
- **Bei Anwaltsmandat** zusätzlich den Standardsatz aus CLAUDE.md am Briefende mit aufnehmen: Berufsbezeichnung, Mandatsverhältnis, Kostenhinweis (RVG / Honorarvereinbarung).

## Anschluss-Skills

- Wenn DB auch auf Widerspruch ablehnt oder schweigt: `schlichtung-reise-verkehr-anrufen`.
- Wenn Klage nötig: `klage-amtsgericht-fahrgast`.
- Für die Ablehnungsgrund-Analyse: `db-ablehnungsgruende-pruefen`.

## Quellen

- VO (EU) 2021/782 — eur-lex.europa.eu (CELEX 32021R0782)
- EVO 2023 — gesetze-im-internet.de/evo_2023
- DB-Beförderungsbedingungen — bahn.de/agb
- Schlichtungsstelle Reise & Verkehr e.V. — schlichtungsstelle-reise-verkehr.de

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

