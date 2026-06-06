---
name: mahnschreiben-aufnahme
description: "Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empfehlung Reaktion. Abgrenzung: nicht eigenes Mahnschreiben erstellen im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Mahnschreiben-Intake

## Arbeitsbereich

Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empfehlung Reaktion. Abgrenzung: nicht eigenes Mahnschreiben erstellen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor dem Intake

1. **Forderungsart:** Kaufpreis, Werkverguetung, Schadensersatz, Darlehensrueckzahlung oder sonstiger Anspruch?
2. **Faelligkeit:** Ist die Forderung bereits fällig und durchsetzbar (§ 271 BGB)?
3. **Verjaehrung:** Ist die dreijährige Regelverjährung (§ 195 BGB) gewährt oder droht sie?
4. **BATNA:** Was ist die beste Alternative zum Mahnschreiben (gerichtliches Mahnverfahren, Klage, Verhandlung)?
5. **Vertraulichkeitsfilter:** Dürfen mandatsbezogene Daten in das eingesetzte KI-System eingespielt werden?

## Zentrale Normen
- § 271 BGB (Fälligkeit)
- § 286 BGB (Verzug — Mahnungserfordernis)
- § 288 BGB (Verzugszinsen)
- § 291 BGB (Prozesszinsen)
- § 195 BGB (Regelverjährung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Strukturierte Erfassung aller für ein Mahnschreiben oder eine vorgerichtliche Aufforderung notwendigen Informationen, bevor der Entwurf erstellt wird. Der Skill führt ein geordnetes Interview und schreibt die Antworten in `demand-letters/[slug]/intake.md`.

## Eingaben

- Neuer Slug oder vorhandenes Mandat (Slug)
- Optional: `--full` für vollständigen erweiterten Intake (inkl. BATNA, Prozesskostenrisiko, Streitwertschätzung)

## Ablauf

1. **Mandantenidentifikation:**
 - Vollständiger Name / Firma, Anschrift, Kontaktperson
 - Mandantentyp: Verbraucher (§ 13 BGB) oder Unternehmer (§ 14 BGB) – für Verzugszinsberechnung relevant (§ 288 Abs. 1 vs. 2 BGB)

2. **Schuldneridentifikation:**
 - Vollständiger Name / Firma, Anschrift, HRB-Nummer (bei Gesellschaften)
 - Zustellungsfähige Anschrift vorhanden? (für spätere Klagezustellung, § 253 Abs. 2 Nr. 1 ZPO)
 - Ist die Passivlegitimation des Schuldners geklärt? (z. B. bei Gesamtschuld § 421 BGB, Rechtsnachfolge, Konzernmutter)

3. **Sachverhaltserfassung:**
 - Wie kam das Schuldverhältnis zustande? (Vertragsurkunde vorhanden?)
 - Was wurde nicht geleistet oder schlecht geleistet?
 - Wann war Leistung fällig?
 - Hat der Mandant bereits gemahnt? (schriftlich / mündlich / konkludent – relevant für § 286 Abs. 1 BGB)
 - Gab es Reaktionen des Schuldners (Einwände, Aufrechnungen, Minderung)?

4. **Forderungserfassung:**
 - Hauptforderung (Betrag, Art, Rechtsgrundlage)
 - Nebenforderungen: Verzugszinsen (§ 288 BGB), vorgerichtliche Anwaltskosten (§ 13 RVG i. V. m. VV 2300), Schadensersatz (§§ 280, 281 BGB)
 - Fälligkeitsdatum und bisherige Mahnungen (mit Datum)
 - Offene Restforderung (nach Teilzahlungen)

5. **Hebel und Risiko (BATNA):**
 - Was ist die beste Alternative des Mandanten ohne Mahnschreiben?
 - Welche Risiken bestehen (Aufrechnung, Gegenansprüche, Insolvenzrisiko)?
 - Ist ein Güteantrag (§ 15a EGZPO) im zuständigen Bundesland Pflicht?
 - Empfiehlt sich ein Mahnbescheid (§§ 688 ff. ZPO) statt Mahnschreiben?

6. **Vertraulichkeitsfilter:**
 - Enthält der Sachverhalt vertrauliche Informationen Dritter, die nicht in das Schreiben dürfen?
 - Besteht Zeugnisverweigerungsrecht des Mandanten für bestimmte Tatsachen?

7. **Intake-Datei schreiben:** `demand-letters/[slug]/intake.md` mit allen Feldern befüllen. Fehlende Pflichtfelder markieren.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```yaml
# demand-letters/[slug]/intake.md
mandant:
 name: ""
 typ: "Unternehmer / Verbraucher"
 anschrift: ""
schuldner:
 name: ""
 anschrift: ""
 hrb: ""
 passivlegitimation_geklaert: true/false
schuldverhaeltnis:
 entstehungsgrund: ""
 vertrag_vorhanden: true/false
 anlage: ""
forderung:
 art: ""
 hauptbetrag: 0.00
 faelligkeit: ""
 bisherige_mahnungen: []
 verzugszinsen_p_a: "5% / 9% über Basiszinssatz"
 anwaltskosten: 0.00
anspruchsgrundlage: ""
fristen_geplant:
 fristsetzung_bis: ""
batna: ""
risiken: []
gueteantrag_erforderlich: false
vertraulichkeit_geprueft: true
```

## Risiken / typische Fehler

- **Fehlende Passivlegitimation:** Bei GmbH-Schuldner Handelsregisterauszug abrufen; Insolvenzantrag prüfen (InsO § 17 ff.) – Mahnung an insolventen Schuldner ist sinnlos.
- **Gesamtschuldner übersehen:** Bei mehreren Schuldnern (§ 421 BGB) alle mahnen, um Verjährungshemmung (§ 213 BGB) zu bewirken.
- **Verjährung prüfen:** Intake prüft automatisch die Regelverjährung (§§ 195, 199 BGB: 3 Jahre zum 31.12.); kürzere Sonderfristen (§ 438 BGB: 2 Jahre für Mängelansprüche; § 548 BGB: 6 Monate für Vermieter; § 195 ff. BGB) gesondert markieren.
- **Unterlassungsaufforderung ohne Vertragsstrafe:** Abmahnungen nach UWG, UrhG, MarkenG müssen eine Unterlassungs- und Verpflichtungserklärung mit Vertragsstrafeversprechen enthalten; fehlt dies, kann der Abgemahnte eine nicht der Kostenfolge des § 97a UrhG entsprechende Erklärung abgeben.
