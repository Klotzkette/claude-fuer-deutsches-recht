---
name: erstgespraech-mandatsannahme
description: "Erstgespraech Mandatsannahme im Plugin Fachanwalt Versicherungsrecht: prüft konkret Strukturierter Erstgespraechsleitfaden für, Klage bei abgelehnter, Deckungsklage gegen Versicherer auf Versicherungsleistung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Erstgespraech Mandatsannahme

## Arbeitsbereich

**Erstgespraech Mandatsannahme** ordnet den Fall über die tragenden Prüfungslinien: Strukturierter Erstgespraechsleitfaden für, Klage bei abgelehnter, Deckungsklage gegen Versicherer auf Versicherungsleistung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage` | Klage bei abgelehnter Berufsunfähigkeitsversicherungs-Leistung. Anwendungsfall BU-Versicherung hat Leistungsantrag abgelehnt oder Verweisung auf andere Tätigkeit ausgesprochen. Normen §§ 172 ff. VVG BU-Versicherung § 15 VVG Anzeigepflicht BAG-Begriff Berufsunfähigkeit 50-Prozent-Grenze. Prüfraster Begriff Berufsunfähigkeit letzte berufliche Tätigkeit Verweisung zumutbare andere Tätigkeit Gutachtenstreit Prüfverfahren. Output Klageschrift-Baustein mit Leistungsantrag Sachverständigenantrag Feststellungsantrag und Durchsetzungsstrategie. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und fachanwalt-versicherungsrecht-leistungsablehnung-prüfen. |
| `fachanwalt-versicherungsrecht-deckungsklage` | Deckungsklage gegen Versicherer auf Versicherungsleistung nach erfolgloser außergerichtlicher Phase. Anwendungsfall Versicherer verweigert Leistung endgueltig und Klage soll erhoben werden. Normen § 1 VVG Versicherungsanspruch § 215 VVG örtliche Zuständigkeit Wohnsitz § 256 ZPO Feststellungsantrag § 114 ZPO PKH. Prüfraster Streitwert Zuständigkeit AG oder LG Klageantrag Beweislast Sachverständigennachweis. Output Deckungsklage-Entwurf mit Antrag Sachverhalt AVB-Auslegung Sachverständigenantrag und PKH-Antrag. Abgrenzung zu klage-versicherer-strategie und fachanwalt-versicherungsrecht-leistungsablehnung-prüfen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `erstgespraech-mandatsannahme`

**Fokus:** Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Versicherungsvertragsrecht (Personen- und Sachversicherung)

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung) (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Versicherungsvertragsrecht (Personen- und Sachversicherung):

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Berufsunfaehigkeit, Unfallversicherung, Sachversicherung, RSV, Haftpflicht
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung):

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Versicherungsvertragsrecht (Personen- und Sachversicherung).
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- VVG, AVB, BU-/UV-Bedingungen, ARB, PflVG (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung)). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Hoehe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege moeglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Pruefroutinen.

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch Versicherungsrecht

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch / Mandatsannahme Versicherungsrecht

§ 6 VVG (Beratungspflicht Versicherer; Anwalt analog für Mandant) → §§ 195, 199, 203, 204 BGB (Verjährung, Hemmung) → § 215 VVG (Zuständigkeit bei Klage) → §§ 43a, 45 BRAO (Konfliktprüfung) → §§ 3, 3a RVG (Vergütungsvereinbarung) → §§ 10, 11 GwG (Identifizierungspflicht) → § 9 RVG (Vorschuss)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`

**Fokus:** Klage bei abgelehnter Berufsunfähigkeitsversicherungs-Leistung. Anwendungsfall BU-Versicherung hat Leistungsantrag abgelehnt oder Verweisung auf andere Tätigkeit ausgesprochen. Normen §§ 172 ff. VVG BU-Versicherung § 15 VVG Anzeigepflicht BAG-Begriff Berufsunfähigkeit 50-Prozent-Grenze. Prüfraster Begriff Berufsunfähigkeit letzte berufliche Tätigkeit Verweisung zumutbare andere Tätigkeit Gutachtenstreit Prüfverfahren. Output Klageschrift-Baustein mit Leistungsantrag Sachverständigenantrag Feststellungsantrag und Durchsetzungsstrategie. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und fachanwalt-versicherungsrecht-leistungsablehnung-prüfen.

### Berufsunfähigkeit-Klage

## Zweck

Mandate von Versicherungs-Nehmern bei abgelehnter Berufsunfähigkeit (BU).

## 1) BU-Begriff

### Definition

- **Berufsunfähigkeit** = > **50 % Beeintraechtigung** in der letzten beruflichen Tätigkeit
- Beruf wie vor Eintritt
- Dauerhaft (typisch > 6 Monate prognostiziert)

### Abstrakte vs. konkrete BU

- Abstrakt: alle Berufe gleichwertiger Art
- Konkret: spezifischer letzter Beruf
- Heute meist konkret

## 2) Verweisungs-Klausel

### Standard

- "Wenn Versicherter zumutbare andere Tätigkeit ausueben kann, ist nicht BU"
- Verweisung auf vergleichbare Berufe

### Verweisungslinie nach BGH-Rechtsprechung

- Seit dem grundlegenden Wandel der BGH-Rechtsprechung ist nur die **konkrete Verweisung** auf eine tatsächlich ausgeübte Vergleichstätigkeit zulässig. Abstrakte Verweisung allein auf eine theoretisch denkbare Tätigkeit reicht nicht.
- Konkretisierende Anforderungen vor Verwendung des Versicherer-Verweisungsargumentes in juris.bundesgerichtshof.de und dejure.org verifizieren; nicht aus Modellwissen.
- Wichtige Linie (Stand Mai 2026): Bedingungen, die Versicherungsschutz auf Bürotätigkeit mit > 90 % Schreibtischanteil begrenzen, sind intransparent und benachteiligend (BGH IV. ZS, st. Rspr. — konkrete Entscheidung mit Aktenzeichen und Datum vor Ausgabe verifizieren).

## 3) Ablehnungs-Gründe Versicherer

### Pflichtverletzung Anzeige-Pflicht § 19 VVG

- Vorerkrankungen nicht angegeben
- Bei Schwer-Verstoß: Vertrags-Anpassung / Aufhebung

### Mangelnder Beweis BU

- Gutachten beantwortet nicht 50 %-Schwelle
- Eigene Schädigung

### Verweisung

- Andere zumutbare Tätigkeit ausueubar
- Konkret bestätigt

## 4) Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Phase 1 — Beratung Vers.-Nehmer

- Vertragsprüfung (BU-Klausel)
- Erkrankungs-Stand
- Bisherige Korrespondenz

### Phase 2 — Versicherer-Antrag

- Vollständige Antrags-Unterlagen
- Ärztliche Atteste
- Berufs-Beschreibung

### Phase 3 — Prüfung Versicherer

- Aktenkundige Vorerkrankungen
- Gutachter-Einsatz
- Entscheidung

### Phase 4 — Bei Ablehnung

- Schriftliche Begründung verlangen
- Eigenes Gutachten
- Klage AG / LG je Streitwert

### Phase 5 — Klage

- Streitwert: jaehrliche Rente × Vermutungs-Dauer (oft 5-10 Jahre)
- Sachverständigen-Beweis
- Beweisaufnahme

## 5) Sachverständigen-Strategie

### Eigener SV

- Privatgutachten
- Vorbereitung Mandant

### Gerichtlicher SV

- Vom Gericht bestellt
- Beide Seiten konnen Fragen stellen
- Erfaehrung-Massstab

### Beweis-Niveau

- 50 %-Schwelle muss klar dargelegt sein
- Funktional-Defizite

## 6) Anzeige-Pflicht-Verletzung

### Folgen § 19 VVG

- Bei grober Fahrlaessigkeit: Vertrags-Änderung
- Bei Vorsatz: Aufhebung
- Bei einfachem Verstoß: ggf. nur Pruemien-Anpassung

### Prüfung

- Welche Frage falsch beantwortet?
- Welche Vorerkrankung verschwiegen?
- Kausalitaet mit aktueller BU

## 7) Vergleichs-Verhandlung

### Standard-Ergebnisse

- Einmal-Zahlung statt Renten-Auszahlung (40-60 % Renten-Barwert)
- Anpassung Rente-Höhe
- Befristete Rente mit Nachprüfung

### Vorteile

- Schneller
- Planungs-Sicherheit
- Kein Klage-Risiko

## 8) Aktualität — BGH-Linien (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand jeweils Volltext aufrufen):

- BGH IV ZR 153/20, Urt. v. 14.7.2021 — Versicherungsfall BU: Eintritt erst nach Ablauf des sechs-monatigen Prognosezeitraums. Quelle: juris.bundesgerichtshof.de
- BGH IV ZR 19/18, Urt. v. 26.6.2019 — Vergleichsverweisung; tatsächlich erzieltes Einkommen ist nicht ohne Weiteres auf Vergleichszeitpunkt fortzuschreiben. Quelle: juris.bundesgerichtshof.de
- BGH IV ZR 32/24, Urt. v. 12.3.2025 — Krankentagegeldversicherung: einseitige Tagessatz-Herabsetzung durch Klauselersetzung nach § 164 Abs. 1 VVG unzulässig; Bedeutung auch für Bedingungswechsel in BU/PKV-Klauselgestaltung. Pressemitteilung Nr. 47/25 vom 12.3.2025. Quelle: bundesgerichtshof.de Pressemitteilungen
- BGH IV ZR 70/25, 2025 — PKV-Beitragsanpassung: Begründung der Beitragsanpassung muss konkrete Rechnungsgrundlage benennen; sonst Rückforderung. Quelle: juris.bundesgerichtshof.de (Volltext vor Versand verifizieren)
- BGH IV ZR 86/24, Urt. v. 15.10.2025 — PKV-Beitragsanpassung; Prüfungsmaßstab. Quelle: bundesgerichtshof.de (Volltext-Verifikation Pflicht)

## 9) Honorar

- Beratung 500-1.500 EUR pauschal
- Klage nach Streitwert
- Erfolgs-Vereinbarung bei Beratung möglich

## 10) Typische Fehler

1. **Anzeige-Pflichten unvollständig** bei Antragstellung
2. **Privatgutachten ohne BU-Spezialisten**
3. **Verweisung-Klausel nicht angefochten**
4. **Verjährung 3 Jahre** versäumt

## Anschluss

- `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf` — bei LV
- `fachanwalt-versicherungsrecht-do-deckungsabwehr` — bei D&O
- `fachanwalt-sozialrecht-krankengeld-aussteuerung` — bei KG-Bezug

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026)

Verifizierte Aktenzeichen mit Anker zu offener Quelle. Volltext vor Versand erneut aufrufen und Randnummer einsetzen:

1. **Versicherungsfall BU**: BGH, Urt. v. 14.7.2021, IV ZR 153/20 — Eintritt des Versicherungsfalls erst nach Ablauf der bedingungsgemäßen Prognosezeit (sechs Monate). Offene Quelle: juris.bundesgerichtshof.de
2. **Vergleichstätigkeit / Verweisung**: BGH, Urt. v. 26.6.2019, IV ZR 19/18 — Tatsächlich erzieltes Einkommen aus Verweisungstätigkeit nicht ohne weiteres auf Vergleichszeitpunkt fortzuschreiben. Quelle: juris.bundesgerichtshof.de
3. **AVB-Auslegung Maßstab**: st. Rspr. BGH IV. ZS — Auslegung aus Sicht eines durchschnittlichen, verständigen Versicherungsnehmers ohne versicherungsrechtliche Spezialkenntnisse. Konkrete Entscheidung mit Aktenzeichen vor Versand in offener Quelle verifizieren.
4. **Klauselersetzung nach Intransparenz**: BGH, Urt. v. 12.3.2025, IV ZR 32/24 — Nach Unwirksamkeit einer Bedingung darf der Versicherer keine im Kern identische neue Bedingung einseitig einführen (zur Krankentagegeldversicherung; übertragbar). Pressemitteilung Nr. 47/25 vom 12.3.2025.

### Paragrafenkette

§§ 172 ff. VVG (BU-Versicherung) → § 19 VVG (Anzeigepflicht) → § 28 VVG (Obliegenheitsverletzung) → § 81 VVG (vorsätzliche/grob fahrlässige Herbeiführung) → § 286 ZPO (freie Beweiswürdigung Gutachten) → § 287 ZPO (Schadensschätzung) → § 402 ZPO (Sachverständiger) → § 195 BGB (Verjährung 3 Jahre) → § 203 BGB (Hemmung durch Verhandlungen) → § 256 ZPO (Feststellungsklage bei laufender Rente)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Situation | Frist | Norm |
|---|---|---|
| BU-Leistungsantrag beim Versicherer | laut AVB (typisch unverzüglich) | § 28 VVG, AVB |
| Verjährung BU-Rentenanspruch | 3 Jahre ab Fälligkeit/Kenntnis | § 195, 199 BGB |
| Hemmung durch Verhandlungen | läuft bis Abbrucherklärung | § 203 BGB |
| Feststellungsklage (laufende Rente) | kein strikter Ablauf | § 256 ZPO |
| Nachprüfungsverfahren (Verbesserung) | laut AVB | AVB-BU |

## Triage — Sofortprüfung BU-Mandat

1. **Vollständige Berufsbeschreibung sichern:** Was genau tat der Mandant in den letzten 6 Monaten vor BU-Eintritt? (Tätigkeitsauflistung, Prozentzeitenverteilung).
2. **50-%-Schwelle dokumentieren:** Ärztliche Gutachten zu verbliebener Leistungsfähigkeit; Privatgutachten beauftragen.
3. **Verweisung des Versicherers prüfen:** Konkret oder abstrakt? Übt Mandant die Verweisungstätigkeit tatsächlich aus?
4. **Anzeigepflichtverletzungseinwand prüfen:** Welche Frage wurde falsch beantwortet? Belehrung nach § 19 Abs. 5 VVG erfolgt? Kausalität zwischen Vorerkrankung und eingetretener BU?
5. **Rückwirkende Rente berechnen:** Rente ab Eintritt BU × Monate zurück = Hauptforderung; dazu Verzugszinsen.

**Entscheidungsbaum:**
```
Ablehnung Versicherer?
├─ Verweisung → konkret oder abstrakt?
│ └─ Abstrakt → unzulässig nach st. Rspr. BGH IV. ZS
│ (konkrete Entscheidung in juris.bundesgerichtshof.de
│ verifizieren und Randnummer einsetzen)
│ └─ Konkret → übt Mandant Verweisungstätigkeit tatsächlich aus?
├─ Bestreiten BU-Grad → 50-%-Schwelle ärztlich belegen
│ └─ Privatgutachten + gerichtliches Gutachten beantragen
├─ Anzeigepflichtverletzung → Belehrung erfolgt nach § 19 Abs. 5 VVG?
│ └─ Nein → Rücktritt / Anfechtung des Versicherers unwirksam
│ └─ Ja → Kausalität zwischen Vorerkrankung und BU?
└─ Verjährung → Verhandlungen dokumentieren (§ 203 BGB Hemmung)
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Klage gegen BU-Versicherer wegen Leistungsablehnung | BU-Klageschrift nach Pruefschema; Template unten |
| Variante A — Erstantrag noch nicht vollstaendig gestellt | Nachbeibringung Unterlagen zuerst; Klage danach |
| Variante B — Vergleich wirtschaftlich attraktiver als Prozess | Vergleichsverhandlung vor Klageerhebung; Klage als Druckmittel |
| Variante C — BU nur voruebergehend Reaktivierung moeglich | Teilleistung akzeptieren und beobachten statt Vollklage |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Klageschrift BU-Versicherung (Skizze)

```
[MANDANT] (Kläger) gegen [VERSICHERER] (Beklagte)
Az.: [AZ LG]

ANTRÄGE
1. Die Beklagte wird verurteilt, an den Kläger rückständige BU-Rente
 für den Zeitraum [MONAT/JAHR] bis [MONAT/JAHR] von EUR [BETRAG]
 nebst Zinsen 5 Prozentpunkte über Basiszins seit [DATUM] zu zahlen.
2. Es wird festgestellt, dass die Beklagte verpflichtet ist, dem Kläger
 ab [DATUM] eine monatliche BU-Rente von EUR [MONATSBETRAG] zu zahlen
 und die Prämien zu erlassen (§ __ AVB), solange Berufsunfähigkeit
 im Sinne der AVB vorliegt.

BEGRÜNDUNG
1. BU-Definition (§ __ AVB): Kläger übte zuletzt die Tätigkeit
 [BERUFSBEZEICHNUNG konkret] aus. Tätigkeitsprofil: [Liste mit %].
2. 50-%-Schwelle: Laut Privatgutachten Dr. [NAME] vom [DATUM]
 (Anlage K3) ist Kläger zu [X]% beeinträchtigt.
3. Verweisung verfehlt: Versicherer verweist auf [Beruf] — nicht
 konkret ausgeübt vom Kläger; abstrakte Verweisung nach st. Rspr.
 des BGH IV. ZS unzulässig (konkrete Entscheidung mit Aktenzeichen
 und Datum vor Versand in juris.bundesgerichtshof.de oder
 dejure.org verifizieren und Randnummer einfügen).
4. Anzeigepflicht: Keine Belehrung § 19 Abs. 5 VVG (Anlage K5);
 Rücktrittsrecht des Versicherers ausgeschlossen.
5. Verjährung: Durch Verhandlungen bis [DATUM] gehemmt (§ 203 BGB).

Beweis: K1 Police + AVB, K2 Tätigkeitsbeschreibung, K3 Privatgutachten,
 K4 Ablehnungsschreiben, K5 Antragsformular, K6 Vollmacht
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 3. `fachanwalt-versicherungsrecht-deckungsklage`

**Fokus:** Deckungsklage gegen Versicherer auf Versicherungsleistung nach erfolgloser außergerichtlicher Phase. Anwendungsfall Versicherer verweigert Leistung endgueltig und Klage soll erhoben werden. Normen § 1 VVG Versicherungsanspruch § 215 VVG örtliche Zuständigkeit Wohnsitz § 256 ZPO Feststellungsantrag § 114 ZPO PKH. Prüfraster Streitwert Zuständigkeit AG oder LG Klageantrag Beweislast Sachverständigennachweis. Output Deckungsklage-Entwurf mit Antrag Sachverhalt AVB-Auslegung Sachverständigenantrag und PKH-Antrag. Abgrenzung zu klage-versicherer-strategie und fachanwalt-versicherungsrecht-leistungsablehnung-prüfen.

### Deckungsklage

## Kaltstart-Rückfragen

1. Wurde außergerichtlich vollständig die Leistung gefordert und ist die Ablehnung endgültig? Liegt ein ausdrückliches Ablehnungsschreiben vor?
2. Bei BU-Versicherung: Liegt ein Berufsunfähigkeitsgutachten und liegen ärztliche Atteste vor? Ist der Grad der BU von mindestens 50 % ärztlich belegt?
3. Welche Klageart ist erforderlich — Leistungsklage auf bezifferten Betrag oder Feststellungsklage auf künftige Rentenpflicht (§ 256 ZPO)?
4. Welcher Streitwert ergibt sich — bei wiederkehrenden Leistungen 3,5-facher Jahreswert (§ 9 ZPO); gedeckelt wenn Restlaufzeit kürzer?
5. Besteht Rechtsschutzversicherung — Deckungszusage eingeholt? Oder ist PKH (§ 114 ZPO) zu beantragen?
6. Sind alle Vertragsunterlagen (Police, AVB-Fassung zum Vertragsschluss, Antragsformular, sämtliche Schriftwechsel) vorhanden?
7. Droht Verjährung (3 Jahre ab Jahresende der Kenntnis §§ 195, 199 BGB)? Hemmung durch Ombudsstelle § 204 BGB aktiv?
8. Ist eine Streitverkündung an den Versicherungsmakler/Vermittler erforderlich (bei Beratungsfehlern)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 1 VVG** — Materielle Anspruchsgrundlage; Versicherungspflicht des VR.
- **§ 14 VVG** — Fälligkeit nach Abschluss der zur Feststellung nötigen Erhebungen; Verzug ab Mahnung oder Fristablauf.
- **§ 215 VVG** — Örtliche Zuständigkeit: VN kann am Wohnsitz / gewöhnlichen Aufenthalt klagen; auch Sitz des VR wählbar.
- **§ 23 Nr. 1 GVG** — Sachliche Zuständigkeit AG: bis EUR 10000 (ab 01.01.2026 Justizreform).
- **§ 71 Abs. 1 GVG** — Sachliche Zuständigkeit LG: ab EUR 10000.
- **§ 9 ZPO** — Streitwert wiederkehrender Leistungen: 3,5-facher Jahreswert; gedeckelter Wert bei kürzerer Restlaufzeit.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 114 ZPO** — PKH bei wirtschaftlicher Bedürftigkeit und hinreichenden Erfolgsaussichten; Beiordnung eines RA.
- **§ 379 ZPO** — Sachverständigenvorschuss; bei PKH Übernahme durch Staatskasse.
- **§ 72 ZPO** — Streitverkündung; Makler, Vermittler bei Beratungspflichtverletzung einbeziehen.
- **§§ 195, 199, 204 BGB** — Verjährung 3 Jahre; Hemmung durch Ombudsstelle und Verhandlungen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Außergerichtlich endgültige Ablehnung? | § 14 VVG | Klage erst nach endgültiger Ablehnung sinnvoll |
| 2 | Klageart — Leistung oder Feststellung? | §§ 253, 256 ZPO | BU-Rente: Feststellungsantrag; Sachschaden: Leistungsantrag |
| 3 | Sachliche Zuständigkeit (Streitwert)? | §§ 23, 71 GVG; § 9 ZPO | BU 3,5-facher Jahreswert; Sachschaden = Hauptforderung |
| 4 | Örtliche Zuständigkeit nach § 215 VVG? | § 215 VVG | Wohnsitz VN bevorzugt; auch Sitz VR möglich |
| 5 | Verjährung geprüft? | §§ 195, 199, 203, 204 BGB | Hemmung dokumentieren |
| 6 | Vollständige Vertragsunterlagen vorhanden? | AVB; Police; Antrag | Ohne AVB-Fassung zum Vertragsschluss: schwer zu klagen |
| 7 | Beweise zum Versicherungsfall vollständig? | ZPO §§ 371, 373, 402 | SV-Gutachten, Zeugen, Urkunden benennen |
| 8 | PKH-Antrag vorbereitet? | § 114 ZPO | Einkommensverhältnisse, hinreichende Erfolgsaussicht |
| 9 | Rechtsschutz-Deckungszusage eingeholt? | Rechtsschutz-AVB | Deckungszusage vor Klageerhebung erforderlich |
| 10 | Sachverständigenvorschuss eingeplant? | § 379 ZPO | Ca. EUR 2000–5000 für Medizin-SV |
| 11 | Streitverkündung Makler/Vermittler? | § 72 ZPO | Verjährungswirkung; Bindungswirkung für Folgeprozess |
| 12 | Vorläufige Vollstreckbarkeit beantragt? | § 708 Nr. 11 ZPO | Standardantrag in Klage |
| 13 | Zinsen berechnet? | §§ 280, 286, 288 BGB | Ab Verzugseinritt; 5 % über Basiszinssatz |
| 14 | Außergerichtliche Anwaltskosten berechnet? | § 249 BGB; RVG | 1,3 Geschäftsgebühr aus Gegenstandswert |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Deckungsklage gegen Versicherer | Klageschrift nach Pruefschema; Template unten |
| Variante A — Versicherer hat nur teilweise abgelehnt | Klage auf Differenzbetrag; Vergleich zu voller Deckung anstreben |
| Variante B — Verjährung droht innerhalb 3 Monaten | Klage sofort; Verhandlung parallel |
| Variante C — Mandant will keine Eskalation Folgegeschaeft | Mediation oder Ombudsmann-Verfahren zuerst; Klage danach |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Vollständige Klageschrift BU-Versicherung

```
An das Landgericht [Ort]
— Zivilkammer —

KLAGESCHRIFT

[Vorname Nachname], geb. [Datum], [Adresse]
 — Kläger —
Prozessbevollmächtigte:
Rechtsanwältinnen/Rechtsanwälte [Kanzlei, Adresse]

gegen

[Versicherungs-AG], vertreten durch den Vorstand,
[Adresse]
 — Beklagte —

wegen Berufsunfähigkeitsleistung
Streitwert: vorläufig EUR ____ (3,5 × [Jahresrente])

I. ANTRÄGE

1. Es wird festgestellt, dass die Beklagte verpflichtet ist,
 dem Kläger aus dem Berufsunfähigkeitsversicherungsvertrag,
 Police Nr. [Nr.], Anlage K1, ab dem [Datum] eine monatliche
 Berufsunfähigkeitsrente von EUR [Betrag] sowie Befreiung von
 der Beitragszahlungspflicht zu leisten, solange und soweit
 beim Kläger Berufsunfähigkeit von mindestens 50 % in seiner
 zuletzt ausgeübten Tätigkeit als [Beruf] besteht.

2. Die Beklagte wird verurteilt, an den Kläger für den Zeitraum
 [Beginn] bis [aktuell] rückständige Renten in Höhe von
 EUR [Summe] nebst Zinsen in Höhe von 5 Prozentpunkten über
 dem Basiszinssatz seit [Datum] zu zahlen.

3. Die Beklagte wird verurteilt, an den Kläger vorgerichtliche
 Anwaltskosten in Höhe von EUR [Berechnung nach RVG] zu zahlen.

4. Die Kosten des Rechtsstreits trägt die Beklagte.

5. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
 vorläufig vollstreckbar.

II. SACHVERHALT

Der Kläger unterhält bei der Beklagten eine
Berufsunfähigkeitszusatzversicherung (Police Nr. [Nr.]),
abgeschlossen am [Datum], monatliche Rente EUR [Betrag],
Beitragsbefreiung bei BU (Anlage K1 Police; Anlage K2 AVB).

Seit [Datum] ist der Kläger infolge [Erkrankung/Diagnose,
ICD-Code: [X]] nicht mehr in der Lage, seinen zuletzt als
[Beruf] ausgeübten Beruf zu mindestens 50 % auszuüben.

Sein Berufsbild umfasste im Einzelnen folgende Tätigkeiten:
1. [Tätigkeit, Zeitanteil %]
2. [Tätigkeit, Zeitanteil %]
3. [Tätigkeit, Zeitanteil %]
[Detailbeschreibung der körperlichen/kognitiven Anforderungen]

Der Kläger meldete die Berufsunfähigkeit am [Datum] bei der
Beklagten an (Anlage K3). Die Beklagte lehnte die Leistung
mit Schreiben vom [Datum] ab (Anlage K4).

III. FESTSTELLUNGSINTERESSE

Die Beklagte bestreitet die Leistungspflicht dem Grunde nach.
Das Feststellungsinteresse gemäß § 256 ZPO ist gegeben —
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

IV. RECHTLICHE WÜRDIGUNG

1. Versicherungsfall — Berufsunfähigkeit liegt vor
 Der Kläger ist nach ärztlichen Attesten (Anlagen K5–K8)
 und nach dem SV-Gutachten [Name] vom [Datum] (Anlage K9)
 seit [Datum] zu mindestens 50 % berufsunfähig bezogen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Keine Obliegenheitsverletzung
 [Ablehnungsgrund Versicherer + Widerlegung]

3. Kein Risikoausschluss einschlägig
 [AVB-Ausschluss-Klausel prüfen + ggf. Transparenzrüge]

V. BEWEISANGEBOTE

- Anlage K1: Police
- Anlage K2: AVB (Fassung [Datum/Version])
- Anlage K3: Schadensmeldung
- Anlage K4: Ablehnungsschreiben
- Anlage K5–K8: Ärztliche Atteste/Befundberichte
- Anlage K9: SV-Gutachten (ggf. gerichtliche Bestellung
 beantragt: Medizinischer SV des Fachgebiets [X])
- Zeuge: Behandelnder Arzt [Name, Adresse] zum Beweis der
 Diagnose und des Verlaufs
- Parteivernehmung Kläger § 448 ZPO zur Berufstätigkeit
 (hilfsweise)

[Kanzlei]
```

### Baustein 2 — PKH-Erklärung und Antrag (Kurzschema)

```
ANTRAG AUF PROZESSKOSTENHILFE
gemäß § 114 ZPO

mit der Bitte um Beiordnung:
Rechtsanwalt/Rechtsanwältin [Name, Kanzlei]

I. Wirtschaftliche Bedürftigkeit
Monatliches Nettoeinkommen: EUR [Betrag]
Abzüge: [Kosten Unterkunft, Unterhalt etc.]
Verfügbares Einkommen: EUR [unter Freibetrag]
Erklärung mit Belegen: Anlage PKH 1-4

II. Hinreichende Erfolgsaussichten
Die Klage ist hinreichend aussichtsreich, da
[Zusammenfassung Ablehnungsgründe + Widerlegung].

III. Bitte um Ratenzahlung
Monatlich EUR [Betrag] ab [Datum].

[Kanzlei]
```

### Baustein 3 — Streitverkündung an Versicherungsmakler

```
STREITVERKÜNDUNG § 72 ZPO

In dem Rechtsstreit [Az] verkünden wir dem

[Makler/Vermittler GmbH], [Adresse]

den Streit.

Für den Fall, dass die Klage gegen die Beklagte Versicherungs-AG
abgewiesen werden sollte, werden wir Ersatzansprüche gegen den
Streitverkündungsempfänger geltend machen, da er bei Abschluss
des Versicherungsvertrags nicht korrekt über die Anforderungen
an die Anzeigepflicht § 19 VVG / die AVB-Klauseln [X] belehrt hat.

Die Streitverkündung erfolgt zur Bindungswirkung für einen
etwaigen Folgeprozess (§ 74 ZPO).

[Kanzlei]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Eintritt des Versicherungsfalls | Kläger (VN) |
| Grad der Berufsunfähigkeit | Kläger; SV-Gutachten |
| Schadenshöhe (Rückstände, künftige Rente) | Kläger (Police-Wert) |
| Obliegenheitsverletzung | Beklagte (Versicherer) |
| Kausalität Obliegenheit → Schaden fehlt | Kläger (§ 28 Abs. 3 VVG Exkulpation) |
| AVB-Klausel wirksam | Beklagte / Gericht (Transparenzprüfung) |
| Verjährungshemmung | Kläger |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung | 3 Jahre | Jahresende der Kenntnis | §§ 195, 199 BGB |
| Hemmung Ombudsstelle | Dauer + 6 Monate | Einleitung | § 204 Abs. 1 Nr. 4 BGB |
| Hemmung Verhandlungen | Dauer | Verhandlungsbeginn | § 203 BGB |
| Fälligkeit Versicherungsleistung | nach Abschluss Ermittlungen | Abschluss | § 14 Abs. 1 VVG |
| Streitverkündungsfrist für Regress | abhängig von Anspruch (typisch 3 Jahre) | Kenntnis Mangel | §§ 195, 199 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| BU-Grad unter 50 % | Eigenes SV-Gutachten vorlegen; gerichtlicher SV im Prozess; Berufsbildanalyse detailliert |
| Verweisung auf Vergleichsberuf | AVB auf abstrakte Verweisung prüfen; neuere AVB schließen häufig aus |
| Vorvertragliche Anzeigepflicht verletzt | Antragsfragebogen prüfen; Kausalität zwischen Nichtanzeige und Berufsunfähigkeit |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| PKH-Antrag abzuweisen wegen mangelnder Erfolgsaussichten | Konkrete Ablehnungsbegründung ist schwach; Erfolgsaussicht darlegen |
| Sachverständigenkosten zu hoch | § 379 ZPO-Vorschuss; bei PKH übernimmt Staatskasse; SV-Beauftragung notwendig |

## Streitwert und Kosten

- BU-Versicherung: 3,5-facher Jahreswert der Rente (§ 9 ZPO); bei 10 Jahren Restlaufzeit und EUR 1500/Monat = EUR 63000 Streitwert.
- Gerichtskostenvorschuss LG bei Streitwert EUR 63000: ca. EUR 1638 (GKG).
- Medizinischer SV-Vorschuss: EUR 2500–6000.
- Bei PKH-Bewilligung: Staatskasse trägt GKG-Vorschuss und SV-Kosten.
- Rechtsschutzversicherung: Deckungszusage vorab zwingend; ohne Zusage Eigenanteil des Mandanten.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| BU — klarer medizinischer Befund | SV-Gutachten vorab einholen; Klageschrift mit Gutachten einreichen |
| BU — streitiger Grad | Feststellungsklage; gerichtlicher SV-Beweis; Berufsbild detailliert beschreiben |
| Sachschaden — Ablehnung ohne Substanz | Direktklage nach 2-Wochen-Fristsetzung |
| Streitwert unter EUR 10000 | AG-Verfahren; Ombudsstelle prüfen (bindend bis EUR 10000) |
| Verjährung naht | Klageeinreichung hemmt Verjährung ab Zustellung § 204 Abs. 1 Nr. 1 BGB |

## Anschluss-Skills

- `deckungsanfrage-pruefen` — Vorprüfung vor Klage
- `klage-versicherer-strategie` — Klagestrategie-Details
- `fachanwalt-versicherungsrecht-regress-abwehr` — Regress des Versicherers

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 256 ZPO (Feststellungsklage bei laufender BU-Rente) → § 215 VVG (örtliche Zuständigkeit Klage VN gegen Versicherer) → §§ 23, 71 GVG (sachliche Zuständigkeit AG/LG nach Streitwert) → § 1 VVG (Hauptleistungspflicht) → § 286 ZPO (Beweislast und freie Beweiswürdigung) → § 402 ZPO (gerichtlicher Sachverständiger) → § 114 ZPO (PKH bei Bedürftigkeit) → § 286 ZPO (Beweiswürdigung Privatgutachten)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — Sofortprüfung Deckungsklage

1. **Zuständigkeit prüfen:** Streitwert ≤ 10.000 EUR → AG; > 10.000 EUR → LG. Örtlich: Wohnsitz VN (§ 215 VVG) oder Sitz Versicherer (§ 17 ZPO) — Wahlrecht beim Kläger.
2. **Klageantrag formulieren:** Laufende Rente → Feststellungsantrag § 256 ZPO; rückständige Beträge → Zahlungsantrag beziffert.
3. **Sachverständigenbeweis vorbereiten:** Privatgutachten als Anlage + Antrag auf gerichtliches Gutachten; Kosten-PKH prüfen.
4. **PKH-Berechtigung prüfen:** § 114 ZPO — ausreichende Erfolgsaussichten (Gutachtenlage) + Bedürftigkeit.
5. **Verjährung hemmen:** Bei Verhandlungen § 203 BGB; sonst Klageschrift einreichen vor Ablauf der 3-Jahres-Frist.

---

<!-- AUDIT 27.05.2026 — Bundle 027 Halluzinations-Reparatur
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
