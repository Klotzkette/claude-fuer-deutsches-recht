---
name: sachverhaltsermittlung
description: "Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog. Output: Sachverhalts-Ermittlungsbericht. Abgrenzung: nicht rechtliche Bewertung."
---

# Sachverhaltsermittlung

## Leitidee

Der Engpass in Inhouse-Arbeit ist selten die rechtliche Bewertung. Es
ist die saubere Erfassung des Sachverhalts. Asset-Management und
Hausverwaltung liefern selten freiwillig den vollen Sachverhalt. Der
Skill fragt strukturiert ab und liefert dem Juristen ein konsolidiertes
Memo, das wirklich verwertbar ist.

## Inputs

- Eingangskorrespondenz (Mieterschreiben Anwaltsschreiben Email)
- Vorhandene Unterlagen (Vertrag Übergabeprotokoll Mahnungen
  Hausverwaltungsberichte)
- Optional: interne Kommentare aus der Akte

## Methodik in vier Stufen

### Stufe 1 — Extraktion aus Unterlagen

Aus jedem vorhandenen Dokument werden Datum Akteure Ereignisse und
behauptete Mängel extrahiert. Ergebnis ist eine erste rohe
Zeitleiste.

### Stufe 2 — Gezielter Fragenkatalog

Der Skill erzeugt einen Fragenkatalog für Asset-Management bzw.
Hausverwaltung. Fragen sind kurz, geschlossen wo möglich, jeweils
mit Begründung warum die Frage relevant ist (zB "Wann erfolgte
Mangelanzeige formell? Relevant für Beginn Minderungsrecht
§ 536 BGB").

### Stufe 3 — Zeitleisten-Rekonstruktion

Antworten werden in die Zeitleiste integriert. Konflikte zwischen
Aussagen werden markiert.

### Stufe 4 — Beweis und Lücken

Pro Tatsachenbehauptung wird vermerkt: durch welches Beweismittel
gesichert (Urkunde Zeuge Augenschein), bloss plausibel oder offen.

## Output

- `SV_Memo_<Aktenzeichen>.md` mit Abschnitten:
  - Gesicherter Sachverhalt
  - Plausible Annahmen mit Quelle
  - Offene Punkte mit Fragestellung
  - Zeitleiste in Tabellenform
  - Beweisübersicht
- `Fragenkatalog_<Adressat>.docx` — versendungsfertig an
  Asset-Management oder Hausverwaltung

## Anti-Halluzinations-Regel

Der Skill erfindet KEINE Sachverhaltsdetails. Wo eine Information
fehlt, steht "OFFEN" mit konkreter Frage. Inhouse-Juristen verlieren
sonst das Vertrauen — und das ist der teuerste Verlust.

## Typische Fallkonstellationen

- Mietmängel — wann angezeigt, wann besichtigt, welcher Mietzins,
  welche Minderungsquote behauptet
- Kündigung — Form, Zugang, Begründung, Widerspruch nach
  § 574 BGB
- Eigenbedarf — Bedarfsperson Verwandtschaftsgrad konkrete
  Nutzungsabsicht
- Betriebskostenabrechnung — Abrechnungszeitraum Zugang § 556
  Abs. 3 BGB Frist Einwendungen
- Schönheitsreparaturen Endrenovierung — Vertragsklausel
  Zeitpunkt der Vertragsbegründung Renovierungszustand bei
  Einzug
- Bauschäden — Erstanzeige Sachverständiger Beweissicherung

## Beispielformulierungen

- "Mieterschreiben mit Mietmängelanzeige liegt vor. Erstelle
  Sachverhalts-Memo und Fragenkatalog an Hausverwaltung."
- "Kündigungsstreit gegen Mieter Schmitt. Antworten der
  Hausverwaltung anbei. Konsolidiere zum Memo."
- "Ich habe nur eine halbe Akte. Welche Fragen muss ich stellen,
  bevor ich rechtlich prüfe?"

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Mangelanzeige/Mietminderung: §§ 536, 536a, 543 BGB
- Kuendigung: §§ 543, 569, 573 BGB
- Betriebskosten: § 556 Abs. 3 BGB, BetrKV

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.