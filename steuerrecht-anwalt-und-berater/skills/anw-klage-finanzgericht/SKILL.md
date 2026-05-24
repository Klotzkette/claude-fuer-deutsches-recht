---
name: anw-klage-finanzgericht
description: Entwurf einer Klage zum Finanzgericht nach §§ 40 ff. FGO. Klagefrist ein Monat nach Bekanntgabe der Einspruchsentscheidung (§ 47 Abs. 1 FGO); ein Jahr bei fehlender Rechtsbehelfsbelehrung (§ 55 FGO). Untaetigkeitsklage nach sechs Monaten ohne Einspruchsentscheidung (§ 46 FGO). Sachliche Zustaendigkeit Finanzgericht (§ 33 FGO) oertlich Beklagtensitz Finanzamt (§ 38 FGO). beA-Pflicht. Erzeugt Klageschrift Anlagen Beweisangebote nach FGO-Standards.
---

# Klage zum Finanzgericht

## Voraussetzungen

- **Vorverfahren** durchgeführt — Einspruchsentscheidung liegt vor (§ 44 FGO).
- **Untätigkeitsklage** alternativ nach sechs Monaten ohne Einspruchsentscheidung (§ 46 FGO).
- **Klagefrist** ein Monat ab Bekanntgabe der Einspruchsentscheidung (§ 47 Abs. 1 FGO); ein Jahr bei fehlender Rechtsbehelfsbelehrung (§ 55 FGO).

## Zuständigkeit

- **Sachlich** Finanzgericht (§ 33 FGO) für Streitigkeiten über Abgabenangelegenheiten.
- **Örtlich** das FG in dessen Bezirk die beklagte Behörde ihren Sitz hat (§ 38 FGO).
- **Eingang** über beA (Pflicht für RA) oder EGVP.

## Klagearten

- **Anfechtungsklage** § 40 Abs. 1 Var. 1 FGO — Aufhebung des Steuerbescheids.
- **Verpflichtungsklage** § 40 Abs. 1 Var. 2 FGO — Erlass des begehrten Bescheids (z. B. Erstattung).
- **Allgemeine Leistungsklage** § 40 Abs. 1 Var. 3 FGO.
- **Feststellungsklage** § 41 FGO — Bestehen / Nichtbestehen eines Rechtsverhältnisses.
- **Untätigkeitsklage** § 46 FGO.

## Klageaufbau

### 1. Rubrum

- Klagepartei mit Vertretung (RA mit beA-Adresse).
- Beklagte: Finanzamt vertreten durch den Vorsteher.
- Az der Einspruchsentscheidung und des urspruenglichen Bescheids.

### 2. Anträge

1. Den Bescheid über (Steuerart) (Jahr) vom (Datum) in Gestalt der Einspruchsentscheidung vom (Datum) aufzuheben;
2. die Steuer wie folgt festzusetzen: ... EUR;
3. Kostenantrag (§ 135 FGO);
4. Antrag auf Aussetzung der Vollziehung gemäß § 69 Abs. 3 FGO (falls erforderlich);
5. ggf. PKH-Antrag.

### 3. Sachverhalt

Knapp und chronologisch — Veranlagung Bescheid Einspruch Einspruchsentscheidung.

### 4. Rechtliche Würdigung

- Anspruchs- und Pflichtgrundlagen.
- Substantiierte Auseinandersetzung mit der Einspruchsentscheidung.
- BFH-Rechtsprechung mit Pinpoint (BFH BStBl. II Az Rn).
- BMF-Schreiben und Verwaltungsanweisungen.

### 5. Beweisangebote

Beweismittel im FG-Verfahren (§ 76 FGO Untersuchungsgrundsatz):

- Urkunden (Steuerakten beizuziehen § 71 Abs. 2 FGO).
- Zeugen mit ladungsfähiger Anschrift.
- Sachverständige (häufig Bewertungs- und Buchhaltungsfragen).
- Augenschein.

### 6. Anlagenverzeichnis

Mit Sigel K1 K2 K3.

## Sonderregeln FGO

- **Kein Anwaltszwang** vor dem FG (§ 62 FGO) — aber faktisch Pflicht bei komplexen Mandaten; Vertretung durch StB/WP zulässig.
- **beA-Pflicht** für Rechtsanwälte (§ 52d FGO).
- **Streitwert** und Gerichtskosten nach GKG (§§ 52 ff. GKG).
- **Untersuchungsgrundsatz** (§ 76 FGO) — Gericht ermittelt von Amts wegen.
- **Präklusion** § 79b Abs. 3 FGO bei Versäumung der Tatsachenpraeklusionsfrist.

## Aussetzung der Vollziehung

Wenn das FA die AdV abgelehnt hat: Antrag an FG nach § 69 Abs. 3 FGO mit Eilbedürftigkeit. Skill `anw-aussetzung-vollziehung`.

## PKH

- § 142 FGO iVm §§ 114 ff. ZPO. Bedürftigkeit und Erfolgsaussicht.
- Skill `prozesskostenhilfe-antrag` aus dem Sozialrecht-Plugin sinngemäß.

## Revision

Nach Urteil des FG: Revision an BFH (§ 115 FGO) wenn zugelassen oder Nichtzulassungsbeschwerde (§ 116 FGO).

## Ausgabe

- `klage-<fg>-<az>-<datum>.docx` und Markdown-Spiegel.
- Anlagenkonvolut.
- Fristen im Fristenbuch.

## Versand

Über beA — vor Versand `versand-vor-check` aus `kanzlei-cowork`.
