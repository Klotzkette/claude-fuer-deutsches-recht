---
name: sachverhaltsermittlung
description: "Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhaeltnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Pruefraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog. Output: Sachverhalts-Ermittlungsbericht. Abgrenzung: nicht rechtliche Bewertung."
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

- BGH, Urt. v. 12.10.2022 — VIII ZR 339/21, NJW 2023, 218 Rn. 20: Bei Mietmaengelstreitigkeiten muss der Mieter die Ursache des Mangels nicht beweisen; es genuegt die Darlegung der Mangelerscheinung; der Vermieter traegt dann die Last des Gegenbeweises (keine mangelfreie Beschaffenheit).
- BGH, Urt. v. 26.10.2022 — VIII ZR 328/21, NJW 2023, 296 Rn. 28: Eigenbedarfskuendigung erfordert im Schreiben konkrete Angabe von Eigenbedarfsinteressent und Nutzungszweck — fehlende Angaben machen Kuendigung formell unwirksam.
- BGH, Urt. v. 31.05.2023 — VIII ZR 143/22, NJW 2023, 2735: Sachverhaltsunsicherheiten bei Betriebskosten gehen zu Lasten des Vermieters; er traegt Darlegungslast fuer Umlagefaehigkeit jeder Position.

## Paragrafenkette

- Mangelanzeige/Mietminderung: §§ 536, 536a, 543 BGB
- Kuendigung: §§ 543, 569, 573 BGB
- Betriebskosten: § 556 Abs. 3 BGB, BetrKV

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. — Sachverhaltsermittlung als Praxisvoraussetzung
- BeckOK Mietrecht — §§ 536 ff. Beweislast
