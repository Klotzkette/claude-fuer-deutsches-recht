---
name: transr-haftungssystem-erstgespraech
description: "Transr Haftungssystem Erstgespraech: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Transr Haftungssystem Erstgespraech

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Transr Haftungssystem Erstgespraech** im Plugin Fachanwalt Transport- und Speditionsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `transr-haftungssystem-grundzuege` | Haftungssystem Grundzuege: Obhutshaftung Frachtfuehrer §§ 425 ff. HGB, Hoechstgrenze 8.33 SZR pro Kilogramm, qualifiziertes Verschulden § 435 HGB durchbricht Hoechstgrenze. Pruefraster Schadensermittlung und Anspruchsberechnung. |
| `erstgespraech-mandatsannahme` | Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp. Normen: §§ 407 ff. HGB, CMR, BRAO. Prüfraster: Sachverhaltserfassung, Frachtvertrag vs. Speditionsauftrag, Interessenlage, Fristen. Output: Erstgespraeches-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Klageschrift. |
| `fachanwalt-transport-adr-gefahrgut` | Gefahrguttransport-Haftung und ADR-Verstoss klaeren: Gefahrgutkennzeichnung, Verantwortlichkeiten, Bußgelder. Normen: ADR, §§ 407 ff. HGB, GefahrgutG. Prüfraster: ADR-Klassen, Kennzeichnungspflicht, Haftungsverteilung. Output: Gefahrgut-Haftungsanalyse und Massnahmenplan. Abgrenzung: nicht allgemeine Frachtführerhaftung HGB. |

## Arbeitsweg

Im Plugin Fachanwalt Transport- und Speditionsrecht gilt für **Transr Haftungssystem Erstgespraech**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `transr-haftungssystem-grundzuege`

**Fokus:** Haftungssystem Grundzuege: Obhutshaftung Frachtfuehrer §§ 425 ff. HGB, Hoechstgrenze 8.33 SZR pro Kilogramm, qualifiziertes Verschulden § 435 HGB durchbricht Hoechstgrenze. Pruefraster Schadensermittlung und Anspruchsberechnung.

# Transport: Haftungssystem

## Spezialwissen: Transport: Haftungssystem
- **Spezialgegenstand:** Transport: Haftungssystem / transr haftungssystem grundzuege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** HGB, SZR.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `erstgespraech-mandatsannahme`

**Fokus:** Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp. Normen: §§ 407 ff. HGB, CMR, BRAO. Prüfraster: Sachverhaltserfassung, Frachtvertrag vs. Speditionsauftrag, Interessenlage, Fristen. Output: Erstgespraeches-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Klageschrift.

# Erstgespraech und Mandatsannahme im Transport-, Speditions- und Logistikrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Transport-, Speditions- und Logistikrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster fuer Transport-, Speditions- und Logistikrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Frachtvertrag, CMR, Spediteur, Versicherung, Multimodal, Zoll
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Frachtklage, Klage CMR-Schaden, Klage HGB-Spediteur-Haftung). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG fuer RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behoerde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebuehrenvereinbarung

Standard-Streitwerte im Bereich Transport-, Speditions- und Logistikrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzustaendig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjaehrung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO fuer Fachanwaltschaft Transport-, Speditions- und Logistikrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 407 ff. HGB, CMR, MC, ADSp, RVS-Konvention (fuer fachliche Erstpruefung).
- DSGVO und BDSG fuer den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Transport-, Speditions- und Logistikrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behoerdenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum fuer Verjaehrungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Transport-, Speditions- und Logistikrecht: Erfahrungswerte nach Instanz.
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

- `vergleichsverhandlung-strategie` (im selben Plugin) fuer den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) fuer den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` fuer Konflikt-, GwG- und PEP-Pruefroutinen.

## Aktuelle Rechtsprechung Erstgespraech Transport

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Erstgespraech Transport

- §§ 407-413 HGB — Frachtvertrag (Grundlagen, Pflichten, Haftung)
- § 439 HGB — Verjaehrung (1 Jahr ab Ablieferung; 3 Jahre bei Vorsatz)
- Art. 32 CMR — Verjaehrung im CMR-Verkehr
- Art. 5 CMR — Frachtbrief als Beweisurkunde
- §§ 10 ff. GwG — Identifizierungspflichten auch im Transportrechtsmandat

## 3. `fachanwalt-transport-adr-gefahrgut`

**Fokus:** Gefahrguttransport-Haftung und ADR-Verstoss klaeren: Gefahrgutkennzeichnung, Verantwortlichkeiten, Bußgelder. Normen: ADR, §§ 407 ff. HGB, GefahrgutG. Prüfraster: ADR-Klassen, Kennzeichnungspflicht, Haftungsverteilung. Output: Gefahrgut-Haftungsanalyse und Massnahmenplan. Abgrenzung: nicht allgemeine Frachtführerhaftung HGB.

# ADR-Gefahrgut-Transport

## Zweck

Compliance bei Gefahrgut-Transport, Sanktionen bei Verstoß.

## 1) ADR — Europaeisches UEbereinkommen

### Anwendungs-Bereich

- Straßengueter-Transport
- Internationale und nationale Strecke
- Pflicht ab kleinen Mengen je nach Klasse

### Klassen

- Klasse 1: Explosivstoffe
- Klasse 2: Gase
- Klasse 3: Entzündliche Fluessigkeiten
- Klasse 4.1: Entzündliche Feststoffe
- Klasse 5: Oxidierende Stoffe / Peroxide
- Klasse 6: Giftige / Ansteckende Stoffe
- Klasse 7: Radioaktive Stoffe
- Klasse 8: AEtzende Stoffe
- Klasse 9: Sonstige

## 2) Verpackungs-Gruppen

- I: Hochgefaehrlich
- II: Mittelgefaehrlich
- III: Niedriggefaehrlich

## 3) Kennzeichnung

- UN-Nummer (4-stellig)
- Gefahrgut-Bezeichnung
- Gefahrenklasse-Etiketten
- Orange-Tafel am Fahrzeug

## 4) Gefahrgut-Beauftragter § 3 GbV

### Pflicht-Unternehmen

- Beförderung, Verpackung, Beladung Gefahrgut

### Aufgaben § 8 GbV

- Compliance-Überwachung
- Schulung
- Vorfall-Anzeige
- Jahres-Bericht an Geschäftsleitung

### Qualifikation

- Schulung IHK
- Prüfung
- Fortbildung 5 Jahre

## 5) Anzeige bei Vorfällen

### An wer

- Bundesamt für Materialforschung (BAM)
- Bei schwerem Vorfall: zuständige Landes-Behörde
- Bei Verkehrsunfall: Polizei + Feuerwehr

### Frist

- Schwerer Vorfall: unverzueglich
- Standardvorfall: Jahresbericht

## 6) Compliance

### Phase 1 — Audit

- Pflicht-Prüfung Gefahrgut-Beauftragter
- Schulungs-Plan Personal
- Verpackungs-Genehmigung prüfen

### Phase 2 — Vorbereitung

- Gefahrgut-Anweisung
- Frachtdokument-Vorlagen
- Notfall-Plan

### Phase 3 — Vorfall

- Sofort-Maßnahmen
- Anwalt einschalten
- Anzeige Behörde

## 7) Sanktionen

### Bußgeld

- Bis 50.000 EUR (§ 17 GGVSEB)
- Bei Vorsatz / Wiederholung: höher

### Strafbarkeit § 328 StGB

- Bei Gefährdung durch ionisierende Strahlung etc.
- Freiheits-Strafe

## 8) Typische Fehler

1. **Gefahrgut-Beauftragter nicht bestellt**
2. **Schulung nicht aktuell**
3. **Kennzeichnung mangelhaft**
4. **Anzeige Behörde versäumt** bei Vorfall

## Anschluss

- `fachanwalt-transport-speditionshaftung-hgb` — bei Haftungs-Frage
- `fachanwalt-transport-cmr-schadensregulierung` — bei int. Transport
- `testakten/umweltrecht-industrieanlage-genehmigung` — bei verbundenen Anlagen

## Aktuelle Rechtsprechung Gefahrgut / ADR

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen ADR / Gefahrgut

- ADR (European Agreement concerning the International Carriage of Dangerous Goods by Road) — Anlage A (Einstufung, Verpackung) und Anlage B (Befoerderungsbedingungen)
- § 3 GbV (Gefahrgutbeauftragtenverordnung) — Bestellpflicht Gefahrgutbeauftragter
- § 35 GGVSEB (Gefahrgutverordnung Strasse, Eisenbahn und Binnenschifffahrt) — Sanktionsnormen
- § 431 HGB — Haftungsbegrenzung Frachtfuehrer (SDR-Betrag; entfaellt bei qualifiziertem Verschulden)
- § 435 HGB — qualifiziertes Verschulden: Vorsatz oder Leichtfertigkeit in Kenntnis wahrscheinlichen Schadenseintritts

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
