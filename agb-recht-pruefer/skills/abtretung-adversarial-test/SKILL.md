---
name: abtretung-adversarial-test
description: "Abtretung Adversarial Test: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Abtretung Adversarial Test

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Abtretung Adversarial Test** im Plugin Agb Recht Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `abtretung` | Klausel-Fachmodul für Abtretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `adversarial-test-agb` | Output- und Streit-Skill für Adversarial Test AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen. |
| `aenderungsvorbehalt-308` | Norm- und Dogmatik-Skill für Änderungsvorbehalt 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung. |
| `agb-arbeitnehmerueberlassung-aueg` | AGB bei Arbeitnehmerueberlassung (AUeG). Skill klaert die AGB-rechtliche Pruefung der Standardvertraege zwischen Verleiher Entleiher und Leiharbeitnehmer Equal-Pay-Klauseln Branchenzuschlaege Verleihbarkeitsausschluss Vertragsstrafe bei Abwerbung. Aktualisierungen AUeG 2017 und Folgejudikatur. Liefert Pruefraster. |

## Arbeitsweg

Im Plugin AGB-Klausel- und Verbraucherschutzprüfung gilt für **Abtretung Adversarial Test**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `abtretung`

**Fokus:** Klausel-Fachmodul für Abtretung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.


# Abtretung

## Fachkern: Abtretung

- **Klauselproblem (Abtretung):** prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung.
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
5. **Spezialfokus:** Bei Abtretung besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
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

## 2. `adversarial-test-agb`

**Fokus:** Output- und Streit-Skill für Adversarial Test AGB: macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen.


# Adversarial Test AGB

## Fachkern: Adversarial Test AGB

- **Klauselproblem (Adversarial Test AGB):** macht aus der AGB-Prüfung verwertbare Redlines, Entwürfe, Playbooks, Abmahnreaktionen oder Entscheidungsunterlagen.
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
5. **Spezialfokus:** Bei Adversarial Test AGB besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
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

## 3. `aenderungsvorbehalt-308`

**Fokus:** Norm- und Dogmatik-Skill für Änderungsvorbehalt 308: prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung.


# Änderungsvorbehalt 308

## Fachkern: Änderungsvorbehalt 308

- **Klauselproblem (Änderungsvorbehalt 308):** prüft die AGB-Kontrolle quellenstreng entlang BGB §§ 305 bis 310 und ordnet Rechtsfolge, Risiko und bessere Fassung.
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
5. **Spezialfokus Änderungsvorbehalt (§ 308 Nr. 4 BGB):**
 - **Voraussetzungen:** (a) Änderung der versprochenen Leistung muss vereinbart sein, (b) sie ist nur zulässig, wenn dem Vertragspartner zumutbar - was nur bei einem Sachgrund gegeben ist, der die einseitige Änderungsbefugnis rechtfertigt, und (c) bei Berücksichtigung der Interessen des Verwenders.
 - **Notwendige Konkretisierung:** Anlass und Umfang der Änderung müssen vorab beschrieben sein. Generalklauseln ("aus sachlichem Grund", "soweit erforderlich", "zur Anpassung an neue Entwicklungen") sind regelmäßig zu unbestimmt und damit unwirksam (BGH, ständige Rechtsprechung).
 - **Hauptpflicht vs. Nebenleistung:** Änderungsvorbehalt für die Hauptleistung (Was wird geschuldet, zu welchem Preis) ist regelmäßig unwirksam, da Vertragskern. Bei Nebenleistungen (Schnittstellen, technische Spezifikationen, Modalitäten) eher zulässig.
 - **Praxisbeispiel digitale Produkte:** § 327r BGB (Bereitstellungsänderung digitaler Produkte) verlangt: triftiger Grund, kostenfrei, Informationspflicht, ggf. Rücktrittsrecht des Verbrauchers.
 - **B2B:** § 308 Nr. 4 BGB greift direkt nicht (§ 310 Abs. 1 BGB), aber Wertung über § 307 BGB. Im B2B wird ein Änderungsvorbehalt häufiger zugestanden, jedoch nur bei klarer Anlassbeschreibung und Reziprozität.
 - **Pflicht zur Information:** Über die Änderung muss in angemessener Frist vorab informiert werden (z.B. 6 Wochen). Stillschweigende Zustimmungsfiktion ist Klauselverbot nach § 308 Nr. 5 BGB (B2C).
6. **Rechtsfolge:** Unwirksamkeit; § 308 Nr. 4 BGB ist Klauselverbot mit Wertungsmöglichkeit. Ersatzregel: Änderung nur einvernehmlich.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

### Mustertext (zulässiger Änderungsvorbehalt, eng)

> Der Anbieter ist berechtigt, die in Anlage [X] aufgeführten Leistungsmerkmale anzupassen, soweit dies aufgrund (a) gesetzlicher Vorgaben, (b) zwingender Anforderungen an die IT-Sicherheit oder (c) der Weiterentwicklung der zugrundeliegenden Software erforderlich ist und für den Kunden zumutbar ist. Über die geplante Anpassung wird der Anbieter den Kunden mindestens 6 Wochen vor Wirksamwerden in Textform informieren. Verändert die Anpassung den vertragstypischen Leistungsumfang erheblich, kann der Kunde den Vertrag bis zum Wirksamwerden außerordentlich kündigen.

## Aktuelle BGH-Linie zu Aenderungsvorbehalten

### Norm
- § 308 Nr. 4 BGB Aenderungsvorbehalt der versprochenen Leistung; nur wirksam, wenn die Aenderung dem Verwender unter Beruecksichtigung der Interessen des Vertragspartners zumutbar ist.
- § 307 BGB als Auffangkontrolle.

### Energiepreisanpassungs-Linie
- BGH zur unwirksamen Preisanpassung in Energielieferungsvertraegen — staendige Rspr.; Leitlinien BGH VIII ZR 178/08, BGH VIII ZR 244/10, BGH VIII ZR 295/13 (Az im Digitalisat verifizieren).
- Unwirksam: einseitige Preisanpassungen ohne nachvollziehbare Berechnungsformel; einseitige Anpassung ohne paralleles Loesungsrecht.
- Wirksam: Anpassung gekoppelt an Indizes (etwa StatBA-Verbraucherpreisindex) mit transparenter Formel und Kuendigungsrecht.

### Update-Klauseln neu (§ 327f BGB)
- Seit 01.01.2022 in Kraft: § 327f BGB regelt die Aktualisierungspflicht fuer digitale Produkte. AGB-Klauseln, die diese Pflicht unterlaufen, sind unwirksam.
- BGH-Folgejudikate sind im Aufbau; Pruefung Az live verifizieren.

### Weitere relevante AGB-Klauseln § 308 BGB
- Nr. 1: Annahmefrist und Leistungsfrist.
- Nr. 1a: Zahlungsfrist.
- Nr. 1b: Ueberpruefungs- und Aenderungsfrist.
- Nr. 5: Fiktive Erklaerungen.
- Nr. 7: Aufwandsentschaedigung.

### Pruefraster
1. Bezug zur Hauptleistung oder zur Modalitaet?
2. Veraenderungsgrund konkret und beschraenkt definiert?
3. Loesungsrecht oder Anpassungsrecht des Vertragspartners?
4. Transparenzgebot § 307 Abs. 1 Satz 2 BGB?

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

## 4. `agb-arbeitnehmerueberlassung-aueg`

**Fokus:** AGB bei Arbeitnehmerueberlassung (AUeG). Skill klaert die AGB-rechtliche Pruefung der Standardvertraege zwischen Verleiher Entleiher und Leiharbeitnehmer Equal-Pay-Klauseln Branchenzuschlaege Verleihbarkeitsausschluss Vertragsstrafe bei Abwerbung. Aktualisierungen AUeG 2017 und Folgejudikatur. Liefert Pruefraster.


# Agb Arbeitnehmerueberlassung Aueg

## Fachkern: Agb Arbeitnehmerueberlassung Aueg

- **Klauselproblem (Agb Arbeitnehmerueberlassung Aueg):** AGB bei Arbeitnehmerueberlassung (AUeG). Skill klaert die AGB-rechtliche Pruefung der Standardvertraege zwischen Verleiher Entleiher und Leiharbeitnehmer Equal-Pay-Klauseln Branchenzuschlaege Verleihbarkeitsausschluss Vertragsstrafe bei Abwerbung. Aktualisierungen AUeG 2017 und Folgejudikatur. Liefert Pruefraster.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Norm

- AUeG (Arbeitnehmerueberlassungsgesetz).
- §§ 305-310 BGB anwendbar.
- BAG- und BGH-Rechtsprechung zu Verleiher-Entleiher-Vertraegen.

## Klassische Klauseln

### Equal-Pay
- § 8 AUeG: Equal-Pay-Grundsatz nach 9 Monaten.
- Branchenzuschlaege als Ausnahme nach Tarifvertrag.
- AGB-Klauseln, die Equal-Pay weiter ausschliessen, sind unwirksam.

### Vertragsstrafe bei Abwerbung
- Wettbewerbsschutz fuer Verleiher: AGB-Klausel mit Vertragsstrafe in Hoehe einer Vermittlungsprovision (3-6 Monatsgehaelter) wirksam, soweit angemessen.
- BAG 9 AZR 162/12 (Az verifizieren).

### Verleihverbot
- § 1 Abs. 1b AUeG: Verleihhoechstdauer 18 Monate.
- AGB-Klauseln muessen die Hoechstdauer beachten.

### Sicherheitenklauseln
- Stellung von Bankbuergschaften / Verleiher haftet als Gesamtschuldner.

## Pruefraster

1. Verleiher-Entleiher-Vertrag oder Arbeitsvertrag?
2. AGB-Risiko bei Equal-Pay?
3. Vertragsstrafe angemessen?
4. Verleihhoechstdauer beruecksichtigt?
5. Lizenz des Verleihers nach § 1 AUeG?

## Output

- Klauselraster.
- Schriftsatzbaustein.
