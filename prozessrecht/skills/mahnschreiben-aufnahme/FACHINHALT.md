---
name: mahnschreiben-aufnahme
description: "Für Mahnschreiben-Intake: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Mahnschreiben-Intake

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor dem Intake

1. **Forderungsart:** Kaufpreis, Werkverguetung, Schadensersatz, Darlehensrueckzahlung oder sonstiger Anspruch?
2. **Faelligkeit:** Ist die Forderung bereits fällig und durchsetzbar (Paragraf 271 BGB)?
3. **Verjährung:** Ist die dreijährige Regelverjährung (Paragraf 195 BGB) gewährt oder droht sie?
4. **BATNA:** Was ist die beste Alternative zum Mahnschreiben (gerichtliches Mahnverfahren, Klage, Verhandlung)?
5. **Vertraulichkeitsfilter:** Dürfen mandatsbezogene Daten in das eingesetzte KI-System eingespielt werden?

## Zentrale Normen
- Paragraf 271 BGB (Fälligkeit)
- Paragraf 286 BGB (Verzug — Mahnungserfordernis)
- Paragraf 288 BGB (Verzugszinsen)
- Paragraf 291 BGB (Prozesszinsen)
- Paragraf 195 BGB (Regelverjährung)
- Paragraf 203 BGB (Verjährungshemmung durch Verhandlungen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Neuer Slug oder vorhandenes Mandat (Slug)
- Optional: `--full` für vollständigen erweiterten Intake (inkl. BATNA, Prozesskostenrisiko, Streitwertschätzung)

## Ablauf

1. **Mandantenidentifikation:**
 - Vollständiger Name / Firma, Anschrift, Kontaktperson
 - Mandantentyp: Verbraucher (Paragraf 13 BGB) oder Unternehmer (Paragraf 14 BGB) – für Verzugszinsberechnung relevant (Paragraf 288 Abs. 1 vs. 2 BGB)

2. **Schuldneridentifikation:**
 - Vollständiger Name / Firma, Anschrift, HRB-Nummer (bei Gesellschaften)
 - Zustellungsfähige Anschrift vorhanden? (für spätere Klagezustellung, Paragraf 253 Abs. 2 Nr. 1 ZPO)
 - Ist die Passivlegitimation des Schuldners geklärt? (z. B. bei Gesamtschuld Paragraf 421 BGB, Rechtsnachfolge, Konzernmutter)

3. **Sachverhaltserfassung:**
 - Wie kam das Schuldverhältnis zustande? (Vertragsurkunde vorhanden?)
 - Was wurde nicht geleistet oder schlecht geleistet?
 - Wann war Leistung fällig?
 - Hat der Mandant bereits gemahnt? (schriftlich / mündlich / konkludent – relevant für Paragraf 286 Abs. 1 BGB)
 - Gab es Reaktionen des Schuldners (Einwände, Aufrechnungen, Minderung)?

4. **Forderungserfassung:**
 - Hauptforderung (Betrag, Art, Rechtsgrundlage)
 - Nebenforderungen: Verzugszinsen (Paragraf 288 BGB), vorgerichtliche Anwaltskosten (Paragraf 13 RVG i. V. m. VV 2300), Schadensersatz (Paragrafen 280, 281 BGB)
 - Fälligkeitsdatum und bisherige Mahnungen (mit Datum)
 - Offene Restforderung (nach Teilzahlungen)

5. **Hebel und Risiko (BATNA):**
 - Was ist die beste Alternative des Mandanten ohne Mahnschreiben?
 - Welche Risiken bestehen (Aufrechnung, Gegenansprüche, Insolvenzrisiko)?
 - Ist ein Güteantrag (Paragraf 15a EGZPO) im zuständigen Bundesland Pflicht?
 - Empfiehlt sich ein Mahnbescheid (Paragrafen 688 ff. ZPO) statt Mahnschreiben?

6. **Vertraulichkeitsfilter:**
 - Enthält der Sachverhalt vertrauliche Informationen Dritter, die nicht in das Schreiben dürfen?
 - Besteht Zeugnisverweigerungsrecht des Mandanten für bestimmte Tatsachen?

7. **Intake-Datei schreiben:** `demand-letters/[slug]/intake.md` mit allen Feldern befüllen. Fehlende Pflichtfelder markieren.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken / typische Fehler

- **Fehlende Passivlegitimation:** Bei GmbH-Schuldner Handelsregisterauszug abrufen; Insolvenzantrag prüfen (InsO Paragraf 17 ff.) – Mahnung an insolventen Schuldner ist sinnlos.
- **Gesamtschuldner übersehen:** Bei mehreren Schuldnern (Paragraf 421 BGB) alle mahnen, um Verjährungshemmung (Paragraf 213 BGB) zu bewirken.
- **Verjährung prüfen:** Intake prüft automatisch die Regelverjährung (Paragrafen 195, 199 BGB: 3 Jahre zum 31.12.); kürzere Sonderfristen (Paragraf 438 BGB: 2 Jahre für Mängelansprüche; Paragraf 548 BGB: 6 Monate für Vermieter; Paragraf 195 ff. BGB) gesondert markieren.
- **Unterlassungsaufforderung ohne Vertragsstrafe:** Abmahnungen nach UWG, UrhG, MarkenG müssen eine Unterlassungs- und Verpflichtungserklärung mit Vertragsstrafeversprechen enthalten; fehlt dies, kann der Abgemahnte eine nicht der Kostenfolge des Paragraf 97a UrhG entsprechende Erklärung abgeben.
