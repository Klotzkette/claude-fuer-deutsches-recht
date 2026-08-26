---
name: kaltstart-interview
description: "Für /steuerrecht-anwalt-und-berater:stb-kaltstart-interview: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# /steuerrecht-anwalt-und-berater:stb-kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/steuerrecht-anwalt-und-berater:stb-kaltstart-interview` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Rechtliche Grundlagen (Orientierung für das Interview)

### Zentrale Normen
- **StBerG** § 3 (Befugnis), § 57 (Verschwiegenheit), § 64 (Vergütung)
- **AO** §§ 149 ff. (Erklärungspflichten), § 153 (Berichtigungspflicht), § 371 (Selbstanzeige)
- **HGB** §§ 238 ff. (Buchführungspflicht), §§ 264 ff. (Jahresabschluss)
- **InsO** Paragrafen 17 bis 19 (Insolvenzgründe), Paragraf 15a (Antragspflicht)
- **StaRUG** Paragraf 102 (begrenzter Hinweis bestimmter Berufsträger bei Jahresabschlusserstellung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (DATEV-Schnittstelle, Dokumentenspeicher, Mandanten-Portal, E-Mail). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen nur „verfügbar“ melden, wenn ein Werkzeugaufruf tatsächlich erfolgreich war. Konfigurierte, aber ungetestete Verbindungen als „nicht verifiziert“ markieren.

---

## Kaltstart-Interview: Steuerberater-Werkzeuge

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Steuerberater (§ 3 StBerG) / Wirtschaftsprüfer mit Steuerberatungsmandat / Bilanzbuchhalter / Geschäftsleiter (Eigenbilanzierung) / Finanzleiter?
- **Anwaltlicher / steuerlicher Ansprechpartner** (bei Nicht-Steuerberatern): Name, Kanzlei
- **Berufsverband:** DStV, BStBK, IDW, sonstiger oder keiner
- **Kammer-Zugehörigkeit:** Steuerberaterkammer Bezirk

### 2. Mandanten-Struktur

- **Mandanten-Typen:** KMU / Freiberufler / GmbH / GmbH & Co. KG / Einzelunternehmer / Vereine / sonstige
- **Branchen-Schwerpunkte** (falls vorhanden): Bau / Handel / Dienstleistung / Healthcare / Immobilien / Gastronomie
- **Anzahl aktiver Mandanten:** N (orientiert die Skalierung der Werkzeuge)
- **Typische Umsatzgröße der Mandanten:** Bandbreite (für BWA- und Liquiditätsplanungs-Kalibrierung)

### 3. Buchhaltungs- und Bilanzierungssystem

- **Buchhaltungs-Software:** DATEV / Lexware / sevDesk / Addison / SAP / sonstige
- **Bilanzierungsstandard:** HGB / IFRS (selten bei KMU) / Mischung
- **Bilanzerstellung:** durch Steuerberater (für Mandanten) / durch Mandanten selbst (mit Plausibilisierung)

### 4. Liquiditätsplanung

- **Standard-Horizonte:** drei, sechs oder zwölf Monate für die Beratung; 13 Wochen für die operative Krisensteuerung; Drei-Wochen-Status für die Prüfung eingetretener Zahlungsunfähigkeit nach Paragraf 17 InsO; in aller Regel 24 Monate für drohende Zahlungsunfähigkeit nach Paragraf 18 Absatz 2 InsO
- **Schwellenwert für Warnungen:** Liquiditätsgrad I, II, III nach Bilanz-Kennzahlen
- **Eskalation an Insolvenzberater / Sanierungsberater:** ab wann (z. B. < 7 Tage Liquidität)?

### 5. Berichtspflichten

- **Hauptverpflichtungen:**
 - Umsatzsteuer-Voranmeldung (§ 18 UStG): monatlich / quartalsweise
 - Aufstellung des Jahresabschlusses nach Paragraf 264 Absatz 1 HGB grundsätzlich in den ersten drei Monaten; kleine Kapitalgesellschaften dürfen bei ordnungsgemäßem Geschäftsgang bis zu sechs Monate nutzen
 - Offenlegung nach Paragraf 325 HGB grundsätzlich spätestens ein Jahr nach dem Abschlussstichtag; Sonderfristen gesondert prüfen
 - Lohnsteueranmeldung
 - E-Bilanz nach § 5b EStG
- **Hinweis nach Paragraf 102 StaRUG:** nur bei Jahresabschlusserstellung, offenkundigen Anhaltspunkten für einen möglichen Insolvenzgrund und vermuteter Unkenntnis des Mandanten

### 6. Beratungstiefe

- **Reines Steuermandat:** ja / nein
- **Mit betriebswirtschaftlicher Beratung:** ja / nein
- **Mit Sanierungsberatung:** ja / nein (Hinweis: Sanierungsberatung jenseits Steuerberatung kann Rechtsdienstleistung sein — § 5 RDG beachten)

### 7. Standort

- **Bundesland:** [Bayern / NRW / etc.]
- **Praxistypus:** Einzelkanzlei / Sozietät / Partnerschaftsgesellschaft

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde
- Welche Skills jetzt sinnvoll als nächstes laufen können:
 - `/steuerrecht-anwalt-und-berater:stb-bwa-sus-bilanz-pruefung` — bei Plausibilisierung der laufenden BWA/SuSa/Bilanz
 - `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3-6-12-monate` — für klassische Liquiditätsplanung
 - `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3wochen` — bei akutem Liquiditätsengpass / drohender Zahlungsunfähigkeit
- Hinweis auf Mandatsgeheimnis (§ 57 StBerG, § 203 StGB)

## Rechtlicher Rahmen

- **StBerG** — Steuerberatungsgesetz: § 3 (Befugnis), § 5 (Vorbehaltene Tätigkeiten), § 57 (Verschwiegenheit), § 64 (Vergütung)
- **AO** — Abgabenordnung: Erklärungspflichten §§ 149 ff., Berichtigungspflicht § 153, Selbstanzeige § 371
- **UStG** — § 18 (Voranmeldung, Jahreserklärung)
- **EStG** — § 5b (E-Bilanz)
- **HGB** — §§ 238 ff. (Buchführungspflicht), §§ 264 ff. (Jahresabschluss), § 325 (Offenlegung)
- **InsO** — Paragrafen 17 bis 19 und 15a für Insolvenzgründe und Antragspflicht
- **StaRUG** — Paragraf 102 für den tatbestandsgebundenen Hinweis der dort genannten Berufsträger bei Jahresabschlusserstellung; die Pflicht der Geschäftsleitung steht in Paragraf 1 StaRUG

## Hinweise

Dieses Plugin ist kein Ersatz für die individuelle Mandantenberatung durch einen Steuerberater. Es liefert Werkzeuge und Vorlagen zur Strukturierung der Arbeit. Tragende Zitate und Rechtsstände sind vor Verwendung anhand amtlicher oder frei zugänglicher Primärquellen zu prüfen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
