---
name: bautraeger-weg-erstgespraech
description: "Bautraeger WEG Erstgespraech im Plugin Fachanwalt Bau Architektenrecht: prüft konkret WEG-Instandhaltungsruecklage zur Uebergabe, WEG-Teilungserklaerung beim Bautraegervertrag pruefen, Erstgespraeches-Aufnahme im Bau- und Architektenrecht, Abnahme des Bauwerks unter Vorbehalt von Maengeln erklären. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Bautraeger WEG Erstgespraech

## Arbeitsbereich

**Bautraeger WEG Erstgespraech** ordnet den Fall über die tragenden Prüfungslinien: WEG-Instandhaltungsruecklage zur Uebergabe, WEG-Teilungserklaerung beim Bautraegervertrag pruefen, Erstgespraeches-Aufnahme im Bau- und Architektenrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `bautraeger-weg-instandhaltungsruecklage-uebergabe` | WEG-Instandhaltungsruecklage zur Uebergabe. Skill klaert wie die Instandhaltungsruecklage bei der WEG-Gruendung dotiert wird welche Pflichten Bautraeger hat und welche Klauseln problematisch sind. Liefert Pruefraster. |
| `bautraeger-weg-teilungserklaerung-pruefen` | WEG-Teilungserklaerung beim Bautraegervertrag pruefen. Skill klaert was in der Teilungserklaerung steht (Sondereigentum Gemeinschaftseigentum) wie sie gepruef wird und welche Klauseln problematisch sind. Liefert Pruefraster. |
| `erstgespraech-mandatsannahme` | Erstgespraeches-Aufnahme im Bau- und Architektenrecht: Sachverhalt, Vertragstyp, Mangelbild. Normen: §§ 631 633 650a ff. BGB, VOB/B. Prüfraster: Werkvertrag vs. Bauvertrag, Mangelkatalog, Fristen, Interessenlage. Output: Erstgespraeches-Protokoll Bau-Architektenrecht. Abgrenzung: nicht Klageschrift oder Gutachten. |
| `fachanwalt-bau-architektenrecht-abnahme-mit-vorbehalt` | Abnahme des Bauwerks unter Vorbehalt von Maengeln erklären: Maengelvorbehalt, Sicherungsrechte. Normen: §§ 640 641 BGB, § 12 VOB/B. Prüfraster: Abnahmeprotokoll, Maengelruege, Vorbehalt-Wirkung, Gefahruebergang. Output: Abnahmeerklärung mit Maengelvorbehalt. Abgrenzung: nicht vollständige Abnahmeverweigerung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `bautraeger-weg-instandhaltungsruecklage-uebergabe`

**Fokus:** WEG-Instandhaltungsruecklage zur Uebergabe. Skill klaert wie die Instandhaltungsruecklage bei der WEG-Gruendung dotiert wird welche Pflichten Bautraeger hat und welche Klauseln problematisch sind. Liefert Pruefraster.

# Bautraeger Weg Instandhaltungsruecklage Uebergabe

## Norm

§ 19 WEG: Erhaltungsruecklage (frueher Instandhaltungsruecklage) als Vermoegen der WEG.

## Dotierung bei Uebergabe

- Bei den meisten Bautraegervertraegen leistet der Erste Erwerber eine Eroeffnungsdotierung.
- Hoehe variabel (oft 0.5 bis 1 Prozent des Vertragspreises).

## Fortzahlung

- Monatliche Beitraege.
- Hoehe nach Wirtschaftsplan.

## Problemklauseln

- "Bautraeger leistet keine Eroeffnungsruecklage."
- Erwerber muss sofort hohe Beitraege zahlen.

## Pruefen

- Wie hoch ist die Eroeffnungsruecklage?
- Wer leistet?
- Wie schnell waechst sie?

## Pruefraster

1. Eroeffnungsruecklage vorgesehen?
2. Wer leistet?
3. Wirtschaftsplan plausibel?

## 2. `bautraeger-weg-teilungserklaerung-pruefen`

**Fokus:** WEG-Teilungserklaerung beim Bautraegervertrag pruefen. Skill klaert was in der Teilungserklaerung steht (Sondereigentum Gemeinschaftseigentum) wie sie gepruef wird und welche Klauseln problematisch sind. Liefert Pruefraster.

# Bautraeger Weg Teilungserklaerung Pruefen

## Norm

§ 8 WEG: Teilung des Grundeigentums durch den Bautraeger.

## Inhalt

- Liste der einzelnen Wohnungen.
- Sondereigentum jeder Wohnung.
- Gemeinschaftseigentum (Treppenhaus Dach Heizung).
- Sondernutzungsrechte (Garten Stellplatz Kellerraum).

## Pruefung

### Sondereigentum klar abgegrenzt?
- Innenausbau Trennwaende waende.
- Bei mehrgeschossigen Bauten: Stockwerks-Eigentum.

### Sondernutzungsrechte?
- Garten — Sondernutzung oder Sondereigentum?
- Stellplatz — Sondereigentum (Tiefgaragen-Stellplatz) oder Sondernutzung (Aussenstellplatz).

### Verwaltungsregeln
- Verwaltervergangenheit / Erstverwaltung.
- Stimmrechte.

## Problematische Klauseln

- Festschreibung des Erstverwalters auf zu lange Zeit (z. B. 10 Jahre).
- Stimmrechte ueberproportional für Bautraeger.
- Festschreibung der Hausordnung mit Bautraeger-Privilegien.

## Pruefraster

1. Teilungserklaerung als Anlage vorhanden?
2. Sondereigentum konkret?
3. Sondernutzung klar?
4. Verwaltungsregeln angemessen?

## 3. `erstgespraech-mandatsannahme`

**Fokus:** Erstgespraeches-Aufnahme im Bau- und Architektenrecht: Sachverhalt, Vertragstyp, Mangelbild. Normen: §§ 631 633 650a ff. BGB, VOB/B. Prüfraster: Werkvertrag vs. Bauvertrag, Mangelkatalog, Fristen, Interessenlage. Output: Erstgespraeches-Protokoll Bau-Architektenrecht. Abgrenzung: nicht Klageschrift oder Gutachten.

# Erstgespraech und Mandatsannahme im Privates Baurecht, Architekten- und Ingenieurrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Privates Baurecht, Architekten- und Ingenieurrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Privates Baurecht, Architekten- und Ingenieurrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Werkvertrag, BGB-/VOB-Bau, Maengel, Abnahme, HOAI, Sicherheiten, Bauhandwerker
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Klage auf Werklohn, Schadensersatzklage Baumangel, Honorarklage HOAI). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Privates Baurecht, Architekten- und Ingenieurrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Privates Baurecht, Architekten- und Ingenieurrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 631 ff. BGB, VOB/B, HOAI, MaBV, BauFordSiG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Privates Baurecht, Architekten- und Ingenieurrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Privates Baurecht, Architekten- und Ingenieurrecht: Erfahrungswerte nach Instanz.
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

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `fachanwalt-bau-architektenrecht-abnahme-mit-vorbehalt`

**Fokus:** Abnahme des Bauwerks unter Vorbehalt von Maengeln erklären: Maengelvorbehalt, Sicherungsrechte. Normen: §§ 640 641 BGB, § 12 VOB/B. Prüfraster: Abnahmeprotokoll, Maengelruege, Vorbehalt-Wirkung, Gefahruebergang. Output: Abnahmeerklärung mit Maengelvorbehalt. Abgrenzung: nicht vollständige Abnahmeverweigerung.

# Abnahme mit Vorbehalt

## Mandantenfragen beim Kaltstart

1. Welche Abnahmeform liegt vor — förmlich (Begehungsprotokoll), konkludent (Ingebrauchnahme), fiktiv (§ 640 Abs. 2 BGB nach Fristablauf), VOB/B § 12?
2. Liegt eine Abnahmeerklärung schriftlich oder mündlich vor? Welche Mängel waren bei Abnahme erkennbar oder bekannt?
3. Bestehen Vertragsstrafenansprüche wegen Bauzeitüberschreitung (§ 339 BGB) — wurde Vorbehalt nach § 341 Abs. 3 BGB bei Abnahme erklärt?
4. Sollen einzelne Werkteile abgenommen werden (Teilabnahme § 640 Abs. 1 Satz 2 BGB) oder Gesamtabnahme?
5. Welche Mängel werden im Abnahmeprotokoll dokumentiert, mit welchen Nachbesserungsfristen?
6. Besteht Streit über Abnahmefähigkeit — verweigert der Besteller Abnahme wegen behaupteter wesentlicher Mängel?
7. Wie hoch ist der Werklohn, der mit Abnahme fällig wird? Gibt es offene Abschlagsrechnungen?
8. Soll Einbehalt nach § 641 Abs. 3 BGB (doppelter Mängelbeseitigungsaufwand) ausgeübt werden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 640 Abs. 1 BGB | Abnahmepflicht — Besteller muss vertragsgemäß fertiggestelltes Werk abnehmen; Verweigerung wegen unwesentlicher Mängel unzulässig |
| § 640 Abs. 2 BGB | Fiktive Abnahme — Fristsetzung zur Abnahme; nach fruchtlosem Fristablauf Abnahmewirkung kraft Gesetzes |
| § 640 Abs. 3 BGB | Vorbehalt bei bekannten Mängeln — zwingend bei Kenntnis; sonst Verlust Mängelansprüche §§ 634 Nr. 1–3 BGB |
| § 641 Abs. 1 BGB | Fälligkeit Werklohn mit Abnahme |
| § 641 Abs. 3 BGB | Einbehalt — doppelter Mängelbeseitigungsaufwand bis zur Nacherfüllung |
| § 644 BGB | Gefahrübergang mit Abnahme — Zufallsschäden trägt danach Besteller |
| § 634a BGB | Verjährungsbeginn der Mängelansprüche mit Abnahme — 5 Jahre Bauwerk |
| § 341 Abs. 3 BGB | Vertragsstrafenvorbehalt — muss bei Annahme der Leistung (= Abnahme) erklärt werden |
| § 339 BGB | Vertragsstrafe — verwirkt bei Überschreitung Fertigstellungstermin |
| § 12 VOB/B | Förmliche Abnahme — gemeinsame Begehung, Niederschrift, Vorbehalte; fiktive Abnahme § 12 Nr. 5 VOB/B |
| § 13 Nr. 5 VOB/B | Verjährung Mängelansprüche nach VOB/B — 4 Jahre Bauwerk |

## Leitentscheidungen (verifiziert dejure.org)

| Gericht | Aktenzeichen | Datum | Kernaussage | Quelle |
|---------|-------------|-------|-------------|--------|
| BGH | VII ZR 49/15 | 25.02.2016 | Bautraegervertrag: Abnahme-Klausel in AGB, die einen vom Bautraeger bestimmten Sachverstaendigen ueber die Abnahme entscheiden laesst, ist nach §§ 307, 309 Nr. 8 BGB unwirksam (Erwerberschutz) | dejure.org/2016,3146 / NJW 2016, 1572 |
| BGH | VII ZR 25/13 | 30.04.2014 | Konkludente Abnahme: Ingebrauchnahme + Restzahlung + Ablauf angemessener Pruefzeit (regelmaessig 6 Monate) deuten auf Abnahme hin | dejure.org/2014,7990 |
| BGH | VII ZR 46/17 | 22.02.2018 | Aufgabe der fiktiven Schadensberechnung nach Mangelbeseitigungskosten | dejure.org/2018,2890 |

Weitere Entscheidungen vor Verwendung per dejure.org / BGH-Webseite verifizieren.

## Prüfschema — Abnahme und ihre Rechtswirkungen

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Folge |
|---------|-----------|------|-------|
| 1 | Werk fertiggestellt (vertragsgemäß)? | § 640 Abs. 1 BGB | Abnahmepflicht entsteht |
| 2 | Wesentliche Mängel vorhanden? | § 640 Abs. 1 Satz 2 BGB | Ja → Abnahme berechtigt verweigert; Nein → Abnahmepflicht |
| 3 | Abnahmeform bestimmt | §§ 640, 12 VOB/B | Protokoll / konkludent / fiktiv |
| 4 | Bekannte Mängel bei Abnahme — Vorbehalt erklärt? | § 640 Abs. 3 BGB | Nein → Verlust Mängelansprüche §§ 634 Nr. 1–3 |
| 5 | Vertragsstrafe verwirkt — Vorbehalt § 341 Abs. 3 erklärt? | § 341 Abs. 3 BGB | Nein → Verlust Vertragsstrafenrecht |
| 6 | Einbehalt nach § 641 Abs. 3 BGB? | § 641 Abs. 3 BGB | Bis zu doppelte Mängelbeseitigungskosten zurückbehalten |
| 7 | Verjährungsfrist dokumentiert? | § 634a BGB | Beginn Fristlauf; Fristenbuch eintragen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Abnahmeformen im Detail

### Förmliche Abnahme (§ 640 / § 12 VOB/B)

**Ablauf:**
1. Begehungstermin vereinbaren (beide Parteien + ggf. Architekt, SV)
2. Systematische Begehung nach Leistungsverzeichnis
3. Fotodokumentation aller Beanstandungen
4. Niederschrift mit Unterschriften beider Seiten
5. Vorbehalte im Protokoll dokumentieren

**Bestandteile Abnahmeprotokoll:**
- Datum, Uhrzeit, Anwesende
- Gegenstand der Abnahme (Gewerk, LV-Nummer)
- Aufgelistete Mängel mit Lokalisation, Beschreibung, Nachbesserungsfrist
- Vorbehalt § 640 Abs. 3 BGB (Mängelvorbehalt)
- Vorbehalt § 341 Abs. 3 BGB (Vertragsstrafenvorbehalt)
- Einbehalt § 641 Abs. 3 BGB

### Konkludente Abnahme

**Tatbestand:** Ingebrauchnahme ohne ausdrückliche Rüge oder Vorbehalt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gefahr: Auftraggeber nimmt Werk in Betrieb → Abnahme unterstellt
- Schutz: Nutzungsaufnahme unter Vorbehalt schriftlich erklären

**Praxis-Fallen:**
- Restzahlung ohne Mängelrüge → Indiz konkludente Abnahme
- Einzug in Wohnung/Inbetriebnahme Anlage → konkludente Abnahme
- Lange Nutzungsdauer ohne Beanstandung → stillschweigende Abnahme

### Fiktive Abnahme § 640 Abs. 2 BGB

**Voraussetzungen:**
1. Werk ist fertiggestellt
2. Auftragnehmer hat Fertigstellung mitgeteilt (schriftlich)
3. Besteller setzt (oder erhält) Frist zur Abnahme
4. Frist verstrichen ohne Abnahmeerklärung oder Mängelrüge

**Folge:** Abnahmewirkung kraft Gesetzes — alle Rechtsfolgen wie bei förmlicher Abnahme.

**Schutz vor ungewollter fiktiver Abnahme:**
- Mängel schriftlich rügen vor Fristablauf
- Abnahme-Verweigerungserklärung mit Begründung

### Fiktive Abnahme VOB/B § 12 Nr. 5

- 12 Werktage nach Schlussrechnungsübergabe und Fertigstellungsmeldung
- Auftraggeber muss binnen dieser Frist Mängel rügen oder Abnahme verweigern
- Abweichung durch Parteivereinbarung möglich

## Wirkungen der Abnahme im Detail

| Rechtswirkung | Inhalt | Konsequenz |
|--------------|--------|-----------|
| Fälligkeit Werklohn | § 641 Abs. 1 BGB | Auftraggeber muss Schlussrechnung innerhalb vereinbarter Frist bezahlen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Verjährungsbeginn | § 634a Abs. 2 BGB | 5-Jahres-Frist beginnt mit Abnahme; Fristenbuch eintragen |
| Gefahrübergang | § 644 BGB | Zufallsschäden (Brand, Sturm) nach Abnahme trägt Auftraggeber |
| Verlust Mangelansprüche | § 640 Abs. 3 BGB | Für bei Abnahme bekannte Mängel ohne Vorbehalt |
| Vertragsstrafenrecht | § 341 Abs. 3 BGB | Ohne Vorbehalt bei Abnahme: Verlust Vertragsstrafenrecht |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Abnahme mit Maengelvorbehalten erklaeren | Abnahmeprotokoll-Vorlage und Fristsetzung unten |
| Variante A — Abnahme soll ganz verweigert werden (wesentliche Maengel) | Abnahme-Verweigerungsschreiben; Template weiter unten nutzen |
| Variante B — fiktive Abnahme bereits eingetreten | Fiktionswirkung pruefen § 640 Abs. 2 BGB; Vorbehalt nachholen wenn moeglich |
| Variante C — Auftraggeber will Preis einbehalten | Maengeleinbehalt und Vorbehalts-Erklaerung kombinieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Abnahmeprotokoll mit Vorbehalten (Vorlage)

```
ABNAHMEPROTOKOLL
Bauvorhaben: [Bezeichnung]
LV-Nummer: [Nr.]
Datum: [Datum], [Uhrzeit] Uhr
Ort: [Baustelle]
Anwesende:
 Auftraggeber: [Name, Funktion]
 Auftragnehmer: [Name, Funktion]
 Architekt: [Name, Büro]
 SV (falls): [Name]

I. GEGENSTAND DER ABNAHME
Gewerk [Bezeichnung] gemäß Leistungsverzeichnis vom [Datum],
Vertrag vom [Datum].

II. BEGEHUNGSERGEBNIS
Das Werk wird hiermit nach § 640 BGB abgenommen.
Folgende Mängel wurden festgestellt und sind zur Nachbesserung
in der angegebenen Frist zu beseitigen:

Lfd. | Raum/Lokalisation | Mangelbeschreibung | Frist
1. | [Raum/Bauteil] | [Beschreibung] | [Datum]
2. | [Raum/Bauteil] | [Beschreibung] | [Datum]
3. | [Raum/Bauteil] | [Beschreibung] | [Datum]

III. VORBEHALTE
1. Mängelvorbehalt § 640 Abs. 3 BGB
 Hinsichtlich der vorstehend aufgeführten Mängel wird
 ausdrücklich Vorbehalt nach § 640 Abs. 3 BGB erklärt.
 Die Mängelrechte nach § 634 BGB bleiben in vollem Umfang
 vorbehalten.

2. Vertragsstrafenvorbehalt § 341 Abs. 3 BGB
 Hinsichtlich der Vertragsstrafe wegen Überschreitung des
 vereinbarten Fertigstellungstermins [Datum] wird Vorbehalt
 nach § 341 Abs. 3 BGB erklärt.
 [Hinweis: Vertragsstrafe nach § 339 BGB wird gesondert
 geltend gemacht.]

3. Einbehalt § 641 Abs. 3 BGB
 Die Schlusszahlung wird um den doppelten Betrag der
 voraussichtlichen Mängelbeseitigungskosten (EUR [Betrag] × 2
 = EUR [Einbehalt]) bis zur vollständigen Nacherfüllung
 einbehalten.

IV. FRISTEN
Schlussrechnung: bis [Datum] einzureichen
Zahlungsfrist: [Datum]
Verjährung Mängel: [Datum = Abnahme + 5 Jahre BGB / + 4 Jahre VOB/B]

UNTERSCHRIFTEN
Auftraggeber: ............................ Datum: ..............
Auftragnehmer: ............................ Datum: ..............
Architekt: ............................ Datum: ..............
```

### Fristsetzung zur Abnahme (fiktive Abnahme § 640 Abs. 2 BGB)

```
An [Auftraggeber]
Bauvorhaben [Objekt], Vertragsnummer [Nr.]

Fertigstellungsmeldung und Fristsetzung zur Abnahme
gemäß § 640 Abs. 2 BGB

Sehr geehrte Damen und Herren,

wir teilen mit, dass die vertragsgemäß geschuldeten Leistungen
für das Gewerk [Bezeichnung] vollständig fertiggestellt sind.

Wir setzen Ihnen hiermit gemäß § 640 Abs. 2 BGB eine Frist
zur Abnahme bis zum [Datum] (= [Anzahl] Tage ab Zugang).

Wir bitten Sie, bis zu diesem Datum entweder
— die Abnahme zu erklären (förmliches Protokoll oder schriftlich) oder
— konkrete Mängel zu benennen, die eine Abnahme hindern.

Sollten Sie innerhalb der Frist weder Abnahme erklären noch
wesentliche Mängel benennen, tritt die Abnahme gemäß § 640
Abs. 2 BGB kraft Gesetzes ein.

Mit freundlichen Grüßen
[Auftragnehmer]
```

### Abnahme-Verweigerung wegen wesentlicher Mängel

```
An [Auftragnehmer]
Bauvorhaben [Objekt]

Abnahmeverweigerung wegen wesentlicher Mängel

Sehr geehrte Damen und Herren,

wir verweigern die Abnahme der Werkleistung für Gewerk
[Bezeichnung] wegen folgender wesentlicher Mängel:

1. [Mangelbezeichnung] — Lokalisation: [Bauteil]
 Auswirkung: [Erläuterung Wesentlichkeit]
 Grundlage: Verstoß gegen [DIN/vereinbarte Beschaffenheit]

2. [Mangelbezeichnung] — [...]

Wir fordern Sie auf, die Mängel bis [Datum] zu beseitigen
und uns nach Fertigstellung zur erneuten Abnahmebegehung
einzuladen.

Eine Abnahme ist erst nach vollständiger Beseitigung der
wesentlichen Mängel möglich.

[Auftraggeber]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast

| Partei | Beweislastgegenstand | Beweismittel |
|--------|---------------------|--------------|
| Auftragnehmer | Fertigstellung des Werks | Baubeschreibung, Fotos, Bautagebuch |
| Auftragnehmer | Abnahme erfolgt | Abnahmeprotokoll, E-Mail-Bestätigung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Auftraggeber | Vorbehalt erklärt | Abnahmeprotokoll, Vorbehaltserklärung |
| Auftraggeber | Abnahme-Verweigerung berechtigt | Wesentlicher Mangel laut SV |
| Auftragnehmer | Vorbehalt § 341 Abs. 3 (Vertragsstrafe) | Protokolleintrag oder schriftliche Erklärung |

## Fristen-Checkliste

| Frist | Auslöser | Dauer | Folge bei Versäumnis |
|-------|---------|-------|----------------------|
| Vorbehalt § 640 Abs. 3 BGB | Abnahme mit Kenntnis von Mängeln | Bei Abnahme, unverzüglich | Verlust Mängelansprüche §§ 634 Nr. 1–3 BGB |
| Vorbehalt § 341 Abs. 3 BGB | Abnahme bei Vertragsstrafen-Tatbestand | Bei Abnahme, unverzüglich | Verlust Vertragsstrafenrecht |
| Abnahme-Fristsetzung § 640 Abs. 2 BGB | Fertigstellungsmeldung AN | In Fristsetzung (üblich 12 Werktage) | Fiktive Abnahme nach Ablauf |
| Schlussrechnung VOB/B | Abnahme | Innerhalb 2 Monate § 16 Abs. 3 VOB/B | Schlusszahlungsrecht erlischt |
| Verjährung Mängelansprüche BGB | Abnahme | 5 Jahre § 634a BGB | Anspruchsverlust |
| Verjährung Mängelansprüche VOB/B | Abnahme | 4 Jahre § 13 Nr. 4 VOB/B | Anspruchsverlust |
| Verjährung Werklohnanspruch | Fälligkeit | 3 Jahre § 195 BGB | Anspruchsverlust |

## Gegenargumente und Reaktion

| Gegenargument | Reaktion |
|--------------|---------|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Vertragsstrafenvorbehalt vergessen" | § 341 Abs. 3 BGB ist Ausschlussregel — kein Wiedereinsetzungsrecht; Schaden als Schadensersatz nach §§ 280, 286 BGB geltend machen |
| "Einbehalt überhöht" | § 641 Abs. 3 BGB: Einbehalt auf doppelten Mängelbeseitigungsaufwand begrenzt; Unverhältnismäßigkeit als Einwand |

## Streitwert und Kosten

**Werklohnforderung:**
- Streitwert = offene Werklohnforderung nach Abnahme

**Einbehalt § 641 Abs. 3 BGB:**
- Einbehalt = doppelte voraussichtliche Mängelbeseitigungskosten

**Vertragsstrafe:**
- Streitwert = Vertragsstrafenbetrag (z.B. 0.2 % je Werktag Verzug der Gesamtvergütung, max. 5 % Gesamtvergütung üblich)
- Beispiel: Vertragssumme EUR 500.000, 10 Werktage Verzug × 0.2 % = EUR 10.000 Vertragsstrafe

**SV-Gutachten Mängelbeseitigung:** EUR 2.000–10.000 je Komplexität

## Strategische Empfehlung

| Strategie | Empfehlung | Begründung |
|-----------|-----------|------------|
| Abnahmebegehung vorbereiten | LV-Auszug mit Soll/Ist-Spalte, Fotos vorab machen | Systematische Erfassung; keine Mängel vergessen |
| SV-Beteiligung | Bei größeren Projekten > EUR 50.000 SV zur Abnahme hinzuziehen | Unabhängige Dokumentation; SV-Attest als Beweismittel |
| Alle Vorbehalte notieren | § 640 Abs. 3 BGB und § 341 Abs. 3 BGB immer im Protokoll | Keine Nachholung möglich; einmalige Chance |
| Einbehalt ausüben | § 641 Abs. 3 BGB-Einbehalt schriftlich im Protokoll erklären | Druckmittel; Sicherung für Nacherfüllung |
| Verjährungsfrist eintragen | Sofort nach Abnahme im Fristenbuch | 5-Jahres-Frist BGB läuft schnell; Hemmung durch Verhandlungen § 203 BGB |
| Konkludente Abnahme vermeiden | Nutzungsaufnahme schriftlich unter Vorbehalt | Verhindert ungewollten Rechtsverlust |

## Anschluss-Skills

- `werkmangel-vob-bgb-pruefen` — nach Abnahme: Mängelrüge, Fristsetzung, Sekundärrechte
- `fachanwalt-bau-architektenrecht-bauablauf-vbg` — für Behinderungsanzeigen bei Bauzeitverlängerung (parallel)
- `nachtragsmanagement-650b` — bei offenen Nachtragsforderungen zum Zeitpunkt der Abnahme

## Quellen

- BGB §§ 339, 341, 634a, 640, 641, 644
- VOB/B § 12, § 13 Nr. 4–5
- BGH VII ZR 49/15 (25.02.2016), BGH VII ZR 25/13 (30.04.2014), BGH VII ZR 46/17 (22.02.2018) — verifiziert dejure.org
- Vor Verwendung weiterer Rechtsprechung: dejure.org / bundesgerichtshof.de Verifikation
- Werner/Pastor, Der Bauprozess, 16. Aufl.
- Kniffka/Koeble, Fachüberblick des Baurechts, 5. Aufl.
- Stand: 05/2026
