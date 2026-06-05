---
name: urheberrechts-versand-interessen-streitwert
description: "Urheberrechts Versand Interessen Streitwert: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Urheberrechts Versand Interessen Streitwert

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Urheberrechts Versand Interessen Streitwert** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-urheberrechts-zahlen-schwellen-und-berechnung` | Urheberrecht: Zahlen, Schwellen und Berechnungen. Schöpfungshöhe, Schutzfristen (70 Jahre p.m.a.), Lizenzanalogie, Filesharing-Schadensersatz, Vergütungsansprüche nach VGG/GEMA und typische Streitwert- und Schadensberechnung. |
| `spezial-versand-mehrparteien-konflikt-und-interessen` | Mehrparteienkonstellationen im gewerblichen Rechtsschutz: Lizenzgeber/Lizenznehmer, Konzernstrukturen, Abnehmer-Klagen, Kettenverletzungen und Konflikt zwischen mehreren Schutzrechtsinhabern. Interessenkonflikte und Mandatsgrenzen. |
| `streitwert-igr-berechnen` | Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG Muenchen I LG Duesseldorf wirtschaftlicher Wert des Schutzrechts Marktstaerke Eilverfuegungs-Reduktion Streitgegenstand Streitwertherabsetzung § 51 GKG § 12 UWG. Output: Streitwertbegründung und Kostenberechnung. Abgrenzung zu mandat-triage-gewerblicher-rechtsschutz (Ersteinschaetzung) und verletzungs-triage. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Urheberrechts Versand Interessen Streitwert**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-urheberrechts-zahlen-schwellen-und-berechnung`

**Fokus:** Urheberrecht: Zahlen, Schwellen und Berechnungen. Schöpfungshöhe, Schutzfristen (70 Jahre p.m.a.), Lizenzanalogie, Filesharing-Schadensersatz, Vergütungsansprüche nach VGG/GEMA und typische Streitwert- und Schadensberechnung.

# Spezial: Urheberrecht – Zahlen, Schwellen und Berechnung

## Zweck und Mandatsbezug

Dieser Skill behandelt die **quantitativen Aspekte des Urheberrechts** – Schutzfristen, Schöpfungshöhe, Schadensberechnungen, Lizenzanalogie und typische Streitwerte. Diese Zahlen und Schwellen sind in der Praxis entscheidend für die Bewertung eines Falls, die Formulierung einer Abmahnung und die Bezifferung von Schadensersatzforderungen.

Mandatsbezug: Mandant fragt: Wie viel Schadensersatz kann ich verlangen? Oder: Fotografin wurde abgemahnt, weil ein Blogbetreiber ihr Bild verwendet hat – was kostet das typischerweise?

## Schutzdauer (§§ 64–69 UrhG)

| Werkart | Schutzdauer | Berechnung |
|---|---|---|
| Allgemein (§ 64 UrhG) | 70 Jahre nach Tod des Urhebers (p.m.a.) | Ablauf am Ende des Todesjahres + 70 |
| Filmwerk (§ 65 Abs. 2 UrhG) | 70 Jahre nach Tod des letztverstorbenen Hauptbeteiligten | Regisseur, Drehbuchautor, Komponist |
| Anonymes/pseudonymes Werk (§ 66 UrhG) | 70 Jahre nach Veröffentlichung | Wenn Urheber unbekannt bleibt |
| Lichtbild (nicht Lichtbildwerk) (§ 72 UrhG) | 50 Jahre nach Veröffentlichung | Einfacher Schutz ohne Schöpfungshöhe |
| Tonträgerhersteller (§ 85 UrhG) | 70 Jahre nach Veröffentlichung | Leistungsschutzrecht |
| Filmhersteller (§ 94 UrhG) | 50 Jahre nach Veröffentlichung | Leistungsschutzrecht |
| Presseverleger (§ 87f UrhG) | 1 Jahr nach Veröffentlichung | Leistungsschutzrecht (sehr kurz) |

**Berechnung:** Frist läuft bis Ende des Jahres (§ 69 UrhG); 70 Jahre p.m.a. eines 1950 verstorbenen Urhebers: Schutz bis 31.12.2020.

## Schöpfungshöhe (§ 2 Abs. 2 UrhG)

### Anforderungen

- **Allgemein:** Persönliche geistige Schöpfung; eigene schöpferische Gestaltung.
- **Kleine Münze:** Mindestmaß individueller Prägung ausreichend; BGH hält Anforderungen niedrig.
- **Rein technische Leistungen:** Kein Urheberrecht (z.B. rein maschinell generierter Text).
- **Handwerksleistungen:** Umstritten; BGH: auch handwerkliche Routineleistungen können Schöpfungshöhe erreichen.

### Werkarten und Schöpfungshöhen-Praxis

| Werkart | Schöpfungshöhe | Beispiel |
|---|---|---|
| Literarisches Werk | Gering bis mittel | Kurztext mit individuellem Ausdruck ausreichend |
| Computerprogramm (§ 69a UrhG) | Niedrig | BGH: Eigenentwicklung ausreicht; keine besondere Kreativität nötig |
| Lichtbildwerk (§ 2 Abs. 1 Nr. 5) | Mittel | Eigene Bildkomposition, Licht, Perspektive |
| Lichtbild (§ 72 UrhG) | Keine Schöpfungshöhe nötig | Einfacher Schutz für alle Fotos |
| Datenbankwerk (§ 4 UrhG) | Mittel | Auswahl und Anordnung individuell |
| Datenbankherstellerrecht (§ 87a UrhG) | Kein Schöpfungserfordernis | Investitionsschutz |

## Schadensberechnung (§ 97 Abs. 2 UrhG)

### Drei Berechnungsmethoden

**1. Tatsächlicher Schaden (§ 97 Abs. 2 Satz 1 UrhG):**
- Entgangener Gewinn + eigener Schaden.
- Schwer bezifferbar; selten praktisch.

**2. Lizenzanalogie (§ 97 Abs. 2 Satz 3 UrhG):**
- Was hätte der Verletzer zahlen müssen, wenn er eine Lizenz erworben hätte?
- Üblichste Methode in der Praxis.
- Orientierung: GEMA-Tarife, MFM-Bildhonorar-Empfehlungen, Branchenüblichkeit.

**3. Gewinnherausgabe (§ 97 Abs. 2 Satz 2 UrhG):**
- Herausgabe des Verletzergewinns, der kausal auf Verletzung beruht.
- Streitig bei mehrstufiger Nutzung.

### Lizenzanalogie in der Praxis

| Werkart | Typische Ansätze | Quelle |
|---|---|---|
| Fotografie | MFM-Empfehlungen; 150–1.500 EUR je Bild | [mfm.de](https://www.mfm.de) |
| Musik (Online) | GEMA-Online-Tarife | [gema.de](https://www.gema.de) |
| Text (Blog/Website) | Keine offizielle Tabelle; ca. 1–5 EUR/Wort | Branchenpraxis |
| Software | Lizenzgebühren vergleichbarer Software | Sachverständigengutachten |
| Foto (fehlende Nennung Urheber) | Verdoppelung der Lizenz (BGH-Rechtsprechung) | Bgh.de |

**Urheberrechtsvermerk vergessen:** BGH hat Verdoppelung der Lizenzgebühr bei fehlender Urhebernennung bestätigt (§ 13 UrhG-Verletzung).

## Filesharing-Schadensersatz

### Bereinigte Streitwerte und Schadensersatz nach BGH-Rechtsprechung

| Kriterium | BGH-Praxis |
|---|---|
| Streitwert Unterlassung | 1.000–10.000 EUR je Werk; typisch 2.500–3.000 EUR (nach BGH „BearShare" 2014) |
| Schadensersatz Filesharing | BGH: 200 EUR je musikfremder Titel als Mindestsatz (BGH 2016); höhere Beträge möglich |
| Abmahnkostendeckelung Privat | § 97a Abs. 3 UrhG: max. 178 EUR Erstattung bei Privatperson; bei erstmaliger Abmahnung |
| Abmahnkostendeckelung greift nur | Wenn: Privat, Erstverstoß, keine gewerbliche Tätigkeit | |

**Berechnung Anwaltskosten-Erstattung (privater Bereich):**
- Streitwert 2.500 EUR + RVG: 1,3 Geschäftsgebühr.
- Deckelung auf 178 EUR nach § 97a Abs. 3 UrhG bei Privatperson, erstmaliger Abmahnung.

## Vergütungsansprüche (VGG – Verwertungsgesellschaftengesetz)

| Organisation | Bereich | Ansprüche |
|---|---|---|
| GEMA | Musik (Komponist, Texter, Verleger) | Rundfunk, Online, Live |
| VG Wort | Text (Autoren, Verleger) | Pauschalabgaben, Geräteabgaben |
| VG Bild-Kunst | Bildende Kunst, Foto, Design | Ausstellungen, Reproduktionen |
| GVL | Tonträgerhersteller, ausübende Künstler | Rundfunk, Online |
| GVLI | Filmhersteller | – |

**VGG (Verwertungsgesellschaftengesetz):** Regelt Aufgaben, Rechte und Pflichten von Verwertungsgesellschaften. [gesetze-im-internet.de/vgg](https://www.gesetze-im-internet.de/vgg/)

## Schätzung nach § 287 ZPO

- Wenn exakte Berechnung nicht möglich: Gericht schätzt.
- Kläger muss Grundlagen liefern (Anhaltspunkte, Tabellen, Sachverständigengutachten).
- BGH: Auch bei dürftiger Grundlage Schätzung möglich; kein Klageabweisung wegen Unberechenbarkeit.

## Quellenregel

- [§ 97 UrhG – dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 97a UrhG – dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 64 UrhG – dejure.org](https://dejure.org/gesetze/UrhG/64.html)
- UrhG vollständig: [gesetze-im-internet.de/urhg](https://www.gesetze-im-internet.de/urhg/)
- MFM-Bildhonorarempfehlungen: [mfm.de](https://www.mfm.de)
- BGH-Rechtsprechung zum Filesharing-Schadensersatz: [bgh.de](https://www.bundesgerichtshof.de); Gericht, Datum, AZ angeben.
- Keine BeckRS-Blindzitate; konkrete Schadensangaben immer mit aktuellem Quellennachweis.

## Anschluss-Skills

- `abmahnung-urheberrecht` – Urheberrechtliche Abmahnung
- `spezial-klausel-beweislast-und-darlegungslast` – Beweislast Urheberrecht
- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand Urheberrecht
- `verletzungs-triage` – IP-Verletzung Erstentscheidung

## 2. `spezial-versand-mehrparteien-konflikt-und-interessen`

**Fokus:** Mehrparteienkonstellationen im gewerblichen Rechtsschutz: Lizenzgeber/Lizenznehmer, Konzernstrukturen, Abnehmer-Klagen, Kettenverletzungen und Konflikt zwischen mehreren Schutzrechtsinhabern. Interessenkonflikte und Mandatsgrenzen.

# Spezial: Mehrparteien-Konstellationen und Interessenkonflikte

## Zweck und Mandatsbezug

Dieser Skill behandelt **Mehrparteienkonstellationen im gewerblichen Rechtsschutz** – Fälle, in denen mehr als zwei Parteien in IP-Streitigkeiten involviert sind oder in denen Interessenkonflikte zwischen Beteiligten entstehen. Diese Konstellationen stellen besondere Anforderungen an die anwaltliche Beratung.

Mandatsbezug: Lizenzgeber und Lizenznehmer streiten über Verletzung durch Dritte; Konzernmutter und -tochter haben überkreuzende IP-Rechte; Mandant ist Abnehmer eines Verletzers und wird in Klage hineingezogen.

## Typische Mehrparteienkonstellationen

### Konstellation 1: Lizenzgeber vs. Lizenznehmer vs. Verletzer

**Szenario:** Markeninhaber hat exklusive Lizenz an Unternehmen B vergeben. Unternehmen C verletzt die Marke. Wer kann klagen?

**Rechtslage:**
- Ausschließlicher Lizenznehmer hat eigenes Klagerecht, wenn Lizenz entsprechende Klausel enthält (§ 30 Abs. 3 MarkenG).
- Nicht-ausschließlicher Lizenznehmer: Kein eigenständiges Klagerecht; muss Markeninhaber zur Klageerhebung auffordern.
- Markeninhaber kann stets klagen.
- Problem: Wenn Lizenznehmer klagt, muss Markeninhaber häufig als Partei beigeladen werden.

**Koordinationsbedarf:**
- Abstimmung Markeninhaber / Lizenznehmer vor Klageerhebung.
- Klare Regelung in Lizenzvertrag, wer Verletzungen verfolgt.
- Schadensersatz: Wem steht welcher Anteil zu (Lizenzinhaber, Lizenznehmer)?

**Prüfpunkte:**
- [ ] Art der Lizenz: Ausschließlich oder nicht ausschließlich?
- [ ] Lizenzvertrag: Regelung zur Verletzungsverfolgung vorhanden?
- [ ] Interessenkonflikt: Lizenznehmer will klagen; Lizenzgeber nicht (Kundenbeziehung zum Verletzer)?

### Konstellation 2: Konzernstrukturen und IP-Rechte

**Szenario:** Muttergesellschaft hält IP; Tochtergesellschaft vertreibt Produkte. Tochter wird wegen Verletzung eines Drittpatents abgemahnt.

**Rechtslage:**
- IP liegt bei Mutter; Tochter hat keine formale Lizenz → Nutzung technisch ohne Recht.
- Gegenseitige Lizenzierung innerhalb des Konzerns oft notwendig.
- Tochter kann Verletzungsklage erheben, wenn Mutter sie zur Prozessstandschaft ermächtigt.

**Prüfpunkte:**
- [ ] Konzernweite Lizenzierung geregelt (Konzernlizenzvertrag)?
- [ ] Haftungsfragen: Haftet Mutter für Verletzungen der Tochter?
- [ ] Verteilung der Prozesskosten intern?

### Konstellation 3: Abnehmerklagen (Kettenverletzung)

**Szenario:** Patent A verletzt durch Hersteller B; Händler C kauft von B und verkauft weiter. Patentinhaber klagt beide.

**Rechtslage:**
- Beide Hersteller und Händler können nach § 9 PatG verletzt haben.
- Patentinhaber kann gegen jeden in der Kette vorgehen.
- Händler C kann Hersteller B auf Freistellung in Anspruch nehmen (Gewährleistung, Schadenersatz).
- Praktisch: Gesamtschuldnerschaft zwischen Verletzern möglich.

**Strategie für Händler C:**
- Sofortige Benachrichtigung von Hersteller B.
- Freistellungsanspruch gegenüber B sichern.
- Ggf. Streitverkündung an B im laufenden Verfahren (§ 72 ZPO).

### Konstellation 4: Cross-License und IP-Portfolios

**Szenario:** Zwei Unternehmen haben überkreuzende Patentportfolios. Beide verletzt jeweils Patente des anderen.

**Rechtslage:**
- Beide haben potenziell Ansprüche gegeneinander.
- Lösung: Cross-License (gegenseitige Lizenzierung); oder Patentpooling.
- Kartellrechtliche Grenzen: Art. 101 AEUV / § 1 GWB bei horizontalen Absprachen.

**Verhandlungsstrategie:**
- Stärke des eigenen Portfolios bewerten.
- Entgeltfragen: Ausgleichszahlung bei ungleichem Portfolio?
- Laufzeit und Kündigungsrechte der Cross-License.

### Konstellation 5: Mehrere Verletzer (Parallelverletzungen)

**Szenario:** Sechs verschiedene Online-Händler verletzten gleichzeitig dieselbe Marke.

**Strategie:**
- Priorität setzen: Größte Verletzer zuerst.
- Massen-Abmahnung: Jede Abmahnung individuell; keine Musterbriefe ohne Einzelfallprüfung (§ 8c UWG-Risiko!).
- Kosteneffizienz: EV gegen einen als Präzedenz; andere mahnen ab.
- Monitoring: IP-Watch-Service einrichten.

## Interessenkonflikt-Management

### Interessenkonflikt zwischen Mandanten

- BRAO §§ 43a, 356 – Verbot der Vertretung bei widerstreitenden Interessen.
- Wenn Kanzlei sowohl Lizenzgeber als auch Lizenznehmer vertritt, die in Conflict geraten → Mandat niederlegen.
- Erkennung frühzeitig: Bei Mandatsannahme Interessenkonflikt-Prüfung.

### Berufsrechtliche Schranken

- Verschwiegenheitspflicht (§ 43a BRAO): Informationen aus dem Mandat dürfen nicht gegen Mandanten verwendet werden.
- Parallelmandate im selben Verfahren (§ 356 StGB – Parteiverrat): Strafbar.
- Checkliste bei Mandatsannahme:
 - [ ] Steht neuer Mandant in einem IP-Streit mit bestehendem Mandant?
 - [ ] Hat Kanzlei vertrauliche Informationen der Gegenseite?
 - [ ] Bestehen persönliche oder geschäftliche Beziehungen der Anwälte zur Gegenseite?

## Koordination bei Mehrparteienkonstellationen

### Absprache-Matrix

| Partei | Interesse | Konflikt mit | Koordinationsmaßnahme |
|---|---|---|---|
| Markeninhaber | Verletzung stoppen | Ggf. kein Prozess wegen Kunde | Mandate trennen oder Interessenabgleich |
| Lizenznehmer | Schadensersatz | Markeninhaber will nur Unterlassung | Klares Prozessmandat mit Kostenregelung |
| Händler (Abnehmer) | Freistellung | Hersteller | Streitverkündung |
| Konzernmutter | Haftungsbegrenzung | Tochter-Klagerisiko | Konzernlizenz prüfen |

## Quellenregel

- [§ 30 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/30.html) (Lizenzrecht)
- [§ 72 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/72.html) (Streitverkündung)
- [§ 43a BRAO – dejure.org](https://dejure.org/gesetze/BRAO/43a.html)
- Art. 101 AEUV: [eur-lex.europa.eu](https://eur-lex.europa.eu)
- Keine BeckRS-Blindzitate; Rechtsprechung zu Lizenznehmerklagen mit Gericht, Datum, AZ.

## Anschluss-Skills

- `verletzungs-triage` – IP-Verletzung Erstentscheidung
- `spezial-operate-verhandlung-vergleich-und-eskalation` – Vergleichsverhandlung
- `spezial-gewerblicher-erstpruefung-und-mandatsziel` – Erstprüfung und Mandatsziel
- `mandat-triage-gewerblicher-rechtsschutz` – Mandatstriage

## 3. `streitwert-igr-berechnen`

**Fokus:** Anwalt muss Streitwert für IP-Verletzungsklage oder einstweilige Verfuegung im gewerblichen Rechtsschutz festlegen. Streitwertbemessung MarkenG PatG UWG UrhG. Prüfraster: Senatspraxis OLG Hamburg LG Frankfurt LG Muenchen I LG Duesseldorf wirtschaftlicher Wert des Schutzrechts Marktstaerke Eilverfuegungs-Reduktion Streitgegenstand Streitwertherabsetzung § 51 GKG § 12 UWG. Output: Streitwertbegründung und Kostenberechnung. Abgrenzung zu mandat-triage-gewerblicher-rechtsschutz (Ersteinschaetzung) und verletzungs-triage.

# Streitwert im Gewerblichen Rechtsschutz berechnen

## Zweck

Die richtige Streitwertbemessung ist im gewerblichen Rechtsschutz entscheidend für Kosten, Gerichtsstand, Anwaltskosten und Sicherheitsleistung. Sie ist häufig der zentrale Verhandlungspunkt.

## Eingaben

- Schutzrecht (Marke Patent Design Geschmacksmuster Urheber Sortenschutz)
- Wirtschaftliche Bedeutung (Umsatz Marktanteil Branchenstellung)
- Verletzungs-Charakter (Umfang Dauer schuldhaft Eile)
- Klage-Anträge (Unterlassung Auskunft Schadensersatz Vernichtung Rückruf)
- Eilverfahren oder Hauptsache
- Sitz der Parteien
- Bisherige Korrespondenz

## Schritt 1 — Wert des Schutzrechts

### Marke § 51 GKG

- **Aufbau-Investitionen** und Marketing-Aufwendungen
- **Marktstellung** der Marke
- **Lizenz-Einkünfte** wenn vorhanden
- **Wettbewerbsschutz** Bedeutung in der Branche
- Typische Spannweite EUR 50000 bis EUR 1000000

### Patent

- **Branchenüblicher Lizenzsatz** mal jährlicher Umsatz mal verbleibende Laufzeit
- **Forschungs- und Entwicklungs-Kosten**
- **Marktbedeutung** in der Branche
- Typisch hoher Wert — sechs- bis siebenstellig

### Design / Gebrauchsmuster

- Geringerer Wert typisch — EUR 25000 bis EUR 500000
- Hängt von Umsatz mit dem geschützten Design ab

### Urheber

- **Wert des Werks** und seines Umsatz-Potenzials
- Bei Filesharing EUR 1000 nach § 97a Abs. 3 UrhG bei Verbrauchern Standard
- Bei gewerblicher Verwendung deutlich höher

### UWG-Unterlassungsklage

- **Wirtschaftliches Interesse** des Verletzten
- Typischer Streitwert EUR 30000 bis EUR 200000 je nach Schwere
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 2 — Eilverfahren-Reduktion

- Allgemein: **etwa ein Drittel bis Halb** des Hauptsachewerts
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Begründung: vorläufige Sicherung
- Bei Klage in der Hauptsache Streitwert hoch — nach Vergleich auch hoch
- Bei Reduktion Wert der Begründungs-Schritte einkalkulieren

## Schritt 3 — Streitwertherabsetzung § 51 Abs. 5 GKG / § 12 UWG

### Bei UWG-Verfahren § 12 UWG

- Auf Antrag bei wirtschaftlich-existenzbedrohlicher Belastung
- **Streitwertbegünstigung** auf Antrag — Anwalt muss Antrag stellen
- Anwendung bei kleinem / mittelständischem Verletzer

### Bei GRUR § 51 Abs. 5 GKG

- Vergleichbare Norm

## Schritt 4 — Kumulation verschiedener Klage-Anträge

- **Unterlassung** Hauptantrag — höchster Wert
- **Auskunft** typisch 10 Prozent des Unterlassungs-Werts
- **Vernichtung** vergleichbar oder geringer
- **Rückruf** vergleichbar
- **Schadensersatz** konkrete Forderung
- Kumulative Wertfestsetzung bei mehreren Anträgen mit § 39 GKG
- Senatspraxis kann unterschiedlich sein — typisch nicht alle einzelnen Werte addiert

## Schritt 5 — Senatspraxis-Tabelle (typisch)

### LG Hamburg / OLG Hamburg

- Marke: gerne hoher Streitwert bei bekannten Marken EUR 100000+
- UWG: typisch EUR 30000 bis 100000
- Lizenz-Streit: nach Lizenz-Wert

### LG Frankfurt / OLG Frankfurt

- Marke: konservativer als Hamburg
- Wettbewerb: typisch EUR 25000 bis 100000

### LG München I / OLG München

- Patent-Streit häufig EUR 250000 bis Millionen
- Design: konservativ

### LG Düsseldorf / OLG Düsseldorf

- **Patent-Senat-Praxis** zentral
- Patent typisch sechs- bis siebenstellig
- Wettbewerb mittlere Spannweite

## Schritt 6 — Berufungs- und Revisions-Streitwert

- **Berufung** Streitwert des Berufungs-Antrags § 47 GKG
- **Revision** nur bei Streitwert über EUR 20000 zugelassen (§ 26 EGZPO) oder bei rechtlich relevanter Frage
- **Nichtzulassungsbeschwerde** OLG-Streitwert plus EUR 20000

## Schritt 7 — Sicherheitsleistung

### § 709 ZPO (Hauptsache)

- Vollstreckung gegen Sicherheitsleistung
- Höhe typisch 110 oder 120 Prozent des Vollstreckungs-Volumens

### § 940 ZPO (Einstweilige Verfügung)

- Sicherheitsleistung zur Schadensabsicherung
- Höhe ermessen — meist Bruchteil des Hauptsache-Volumens

## Schritt 8 — Strategische Aspekte

| Konstellation | Strategie |
|---|---|
| Verletzer klein — Streitwert begünstigt | § 12 UWG Antrag stellen |
| Hauptsache nach EV | Wertabgleich — keine Bevorzugung wegen frühere EV |
| Mehrere Verletzungs-Akte | Einheitlicher Streitwert oder einzeln? |
| Streit über Anwaltskosten | Streitwert beeinflusst Gebühren |
| EuGVVO Vollstreckung im Ausland | Streitwert im Heimatstaat klar machen |

## Schritt 9 — Praktische Schritte

1. Schutzrecht-Wert kalkulieren (Lizenz-Analogie Marketing-Aufwand Marktstellung)
2. Verletzungs-Umfang dokumentieren
3. Verfahrensart wählen Eile vs. Hauptsache
4. Senat-Wahl bei Konkurrenzzuständigkeit (Gerichtsstands-Auswahl strategisch)
5. § 12 UWG Antrag prüfen wenn Verletzer-Existenz gefährdet

## Ausgabe

- `streitwert-bewertung.md` mit Berechnungsschritten
- Tabelle für die einzelnen Anträge
- Begründung gegenüber Gericht für gewählten Streitwert
- Vergleichs-Werte aus aktuellen Senatsentscheidungen
- Bei § 12 UWG-Antrag: Begründung mit Bilanzen Umsatz

## Quellen

- GKG §§ 39 47 48 51
- UWG § 12
- ZPO §§ 709 940
- EGZPO § 26
- BGH I. Zivilsenat (GRUR-Sachen)
- GRUR / GRUR-RR Senatsentscheidungen
- Hefermehl/Köhler/Bornkamm UWG
- Köhler/Feddersen UWG
- Ingerl/Rohnke MarkenG
- Benkard PatG

## Triage-Fragen bei Streitwert-Berechnung

Bevor der Streitwert festgesetzt wird, klaere:
1. Handelt es sich um ein UWG-Verfahren (§ 12 II UWG — Antragsgebundenheit), Markenrecht oder Patentrecht?
2. Wird einstweiliger Rechtsschutz (Gegenstandswert = 50-100 % des Hauptsachewerts) oder Hauptsacheklage beantragt?
3. Welchen wirtschaftlichen Wert hat das Unterlassungsbegehren — Umsatz des Verletzers, Bedeutung der Marke/des Patents?
4. Gibt es Vergleichswerte aus OLG-Beschluessen fuer aehnliche Faelle (GRUR-RR, WRP)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- BGH I ZR 20/07 (NOT_FOUND: Aktenzeichen nicht in dejure nachweisbar): ersetzt durch verifizierte Entscheidung BGH X ZR 171/12 vom 13.11.2013 (Einkaufskuehltasche), GRUR 2014, 206 (Quelle: dejure.org/2013,31771)
