---
name: marketplace-agb-mediation-escalation
description: "Marketplace AGB Mediation Escalation: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Marketplace AGB Mediation Escalation

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Marketplace AGB Mediation Escalation** im Plugin AGB-Klausel- und Verbraucherschutzprüfung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `marketplace-agb` | Branchen-Fachmodul für Marketplace AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `mediation-escalation` | Klausel-Fachmodul für Mediation Escalation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `medizinische-leistungen-agb` | Branchen-Fachmodul für Medizinische Leistungen AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen. |
| `mehrdeutigkeit-305c2` | Norm- und Dogmatik-Skill für Mehrdeutigkeit 305c2: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `mehrsprachige-agb-check` | Einstiegs- und Prüffeld für Mehrsprachige AGB Check: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |

## Arbeitsweg

Im Plugin AGB-Klausel- und Verbraucherschutzprüfung gilt für **Marketplace AGB Mediation Escalation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `marketplace-agb`

**Fokus:** Branchen-Fachmodul für Marketplace AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.

# Marketplace AGB

## Fachkern: Marketplace AGB

- **Klauselproblem (Marketplace AGB):** prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Marketplace AGB besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 2. `mediation-escalation`

**Fokus:** Klausel-Fachmodul für Mediation Escalation: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.

# Mediation Escalation

## Fachkern: Mediation Escalation

- **Klauselproblem (Mediation Escalation):** prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Mediation Escalation besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 3. `medizinische-leistungen-agb`

**Fokus:** Branchen-Fachmodul für Medizinische Leistungen AGB: prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.

# Medizinische Leistungen AGB

## Fachkern: Medizinische Leistungen AGB

- **Klauselproblem (Medizinische Leistungen AGB):** prüft typische AGB-Risiken des Vertragstyps und erzeugt Klauselarchitektur, Red Flags und bessere Bedingungen.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Medizinische Leistungen AGB besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 4. `mehrdeutigkeit-305c2`

**Fokus:** Norm- und Dogmatik-Skill für Mehrdeutigkeit 305c2: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung.

# Mehrdeutigkeit 305c2

## Fachkern: Mehrdeutigkeit 305c2

- **Klauselproblem (Mehrdeutigkeit 305c2):** prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Mehrdeutigkeit 305c2 besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 5. `mehrsprachige-agb-check`

**Fokus:** Einstiegs- und Prüffeld für Mehrsprachige AGB Check: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich.

# Mehrsprachige AGB Check

## Fachkern: Mehrsprachige AGB Check

- **Klauselproblem (Mehrsprachige AGB Check):** sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei Mehrsprachige AGB Check besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.
