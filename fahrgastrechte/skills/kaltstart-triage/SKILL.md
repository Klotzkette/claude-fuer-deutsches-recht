---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Fahrgastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenstaendig:..."
---

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

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
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

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
