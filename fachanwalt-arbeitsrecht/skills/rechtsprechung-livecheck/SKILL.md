---
name: rechtsprechung-livecheck
description: "Rechtsprechung Livecheck im Plugin Fachanwalt Arbeitsrecht: prüft konkret Red-Team Qualitätsgate, Internationaler Bezug im Arbeitsrecht, Live-Check für arbeitsrechtliche Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Rechtsprechung Livecheck

## Arbeitsbereich

**Rechtsprechung Livecheck** ordnet den Fall über die tragenden Prüfungslinien: Red-Team Qualitätsgate, Internationaler Bezug im Arbeitsrecht, Live-Check für arbeitsrechtliche Rechtsprechung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-redteam-qualitygate` | Red-Team Qualitätsgate: abschließende Qualitätskontrolle vor Ausgabe eines Schriftsatzes, Memos, Mandantenbriefs oder Vergleichs — Quellenverifikation, Gegenargument-Check, Fristencheck, Scheingenauigkeit-Scan, Mandatsziel-Abgleich. |
| `spezial-rechtsprechung-internationaler-bezug-und-schnittstellen` | Internationaler Bezug im Arbeitsrecht: EuGH-Rechtsprechung (Massenentlassung, Befristung, Diskriminierung, Urlaub), EU-Richtlinien (RL 2023/970, RL 2001/23, RL 2008/94, RL 2003/88), Entsendung AEntG, internationales Privatrecht Rom I. |
| `spezial-rechtsprechung-livecheck-arbeitsrecht` | Live-Check für arbeitsrechtliche Rechtsprechung: Prüfprotokoll für BAG-, LAG- und EuGH-Zitate, Verifizierungswege über bundesarbeitsgericht.de, openjur.de, dejure.org, curia.europa.eu, Umgang mit nicht verifizierbaren Quellen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitätsgate: abschließende Qualitätskontrolle vor Ausgabe eines Schriftsatzes, Memos, Mandantenbriefs oder Vergleichs — Quellenverifikation, Gegenargument-Check, Fristencheck, Scheingenauigkeit-Scan, Mandatsziel-Abgleich.

# Workflow: Red-Team Qualitätsgate

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Workflow: Red-Team Qualitätsgate` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Abschließende Qualitätskontrolle, bevor ein Produkt (Schriftsatz, Memo, Brief, Vergleich) den Skill verlässt. Dieser findet Fehler, Lücken und Scheingenauigkeiten — bevor der Gegner oder das Gericht sie findet.

## Einstieg
Wenn ein Dokument zur Qualitätskontrolle vorliegt:

1. **Was ist das Dokument?** Schriftsatz (Klage, Schriftsatz, Berufung), Memo, Mandantenbrief, Vergleich?
2. **Für wen?** Gericht, Mandant, Gegenseite, Akte?
3. **Was ist das Ziel des Dokuments?** Klage einlegen, informieren, Vergleich schließen, Qualitätsnachweis?
4. **Was sind die 3 stärksten Angriffspunkte der Gegenseite?**

## Gate 1: Quellenverifikation

**Prüfaufgabe:** Sind alle Normen und Urteile korrekt zitiert und frei prüfbar?

Checkliste:
- [ ] Alle Paragrafenzitate mit Norm und Fassung korrekt?
- [ ] Alle Aktenzeichen auf bundesarbeitsgericht.de oder openjur.de verifiziert?
- [ ] Kein BeckRS als alleinige Fundstelle?
- [ ] Keine KI-generierten Aktenzeichen ohne verifizierten Link?
- [ ] EuGH-Zitate auf curia.europa.eu geprüft?
- [ ] Normtexte aktuell? (Letzte Änderung bekannt?)

**Fehler-Kategorie:** Rot — kein Dokument mit unverifizierten Quellen ausgeben.

## Gate 2: Scheingenauigkeit-Scan

**Prüfaufgabe:** Gibt es Aussagen, die präzise klingen, aber ohne Grundlage sind?

Typische Scheingenauigkeiten:
- Pauschale Angaben zu BA-Praxis oder Sperrzeiten ohne BA-Quellennachweis
- BAG-Entscheidungen aus Modellwissen ohne Verifikation
- Kostenangaben ohne RVG-Normprüfung
- Formulierungen wie „nach ständiger BAG-Rechtsprechung" ohne konkrete Fundstelle

**Fehler-Kategorie:** Gelb bis Rot — je nach Tragweite der Aussage.

## Gate 3: Beweislast-Check

**Prüfaufgabe:** Sind alle Behauptungen durch Beweismittel unterlegt oder als Beweisangebote formuliert?

Checkliste:
- [ ] Zugangsdatum der Kündigung belegt?
- [ ] BR-Anhörung: Nachweis vorhanden oder Beweisangebot formuliert?
- [ ] Sozialauswahl: Rüge formuliert; Aufklärungsantrag angeboten?
- [ ] Sachverhalt-Angaben durch Urkunden oder Zeugen belegt?

**Fehler-Kategorie:** Gelb — fehlende Beweisangebote schwächen den Schriftsatz.

## Gate 4: Fristencheck

**Prüfaufgabe:** Sind alle laufenden Fristen im Dokument korrekt berücksichtigt?

Checkliste:
- [ ] Klagefrist § 4 KSchG korrekt berechnet und erwähnt?
- [ ] Berufungsfrist § 66 ArbGG wenn relevant?
- [ ] AGG-Frist § 15 Abs. 4 AGG wenn relevant?
- [ ] Ausschlussfristen im Vertrag oder TV beachtet?

**Fehler-Kategorie:** Rot — Fristfehler können irreversibel sein.

## Gate 5: Gegenargument-Simulation

**Prüfaufgabe:** Was wird die Gegenseite angreifen?

Strukturiertes Red-Team:
1. Was ist das schwächste Argument im Dokument?
2. Welche Tatsachenbehauptung ist am leichtesten zu bestreiten?
3. Gibt es eine alternative rechtliche Einordnung, die für die Gegenseite günstiger ist?
4. Gibt es eine prozessuale Falle (Fristversäumnis, fehlendes Beweisangebot, falsche Anträge)?

**Output nach Gate 5:**
> „Die 2 schwächsten Punkte sind: (1) [Punkt] — Gegner wird [Angriff] vorbringen. Reaktion: [Vorab-Antwort im Schriftsatz]. (2) [Punkt] — [gleich]."

## Gate 6: Mandatsziel-Abgleich

**Prüfaufgabe:** Dient das Dokument tatsächlich dem Mandatsziel?

Checkliste:
- [ ] Ist das Mandatsziel (Bestandsschutz / Abfindung / Schadensersatz) klar erkennbar im Dokument?
- [ ] Widerspricht das Dokument einem früheren Schriftsatz oder einer Aussage des Mandanten?
- [ ] Enthält das Dokument Aussagen, die das Mandatsziel gefährden?

## Gate 7: Formelle Vollständigkeit

**Prüfaufgabe:** Ist das Dokument vollständig und einreichungsfertig?

Checkliste:
- [ ] Gericht, Aktenzeichen, Parteienbezeichnung korrekt?
- [ ] Unterschrift des Anwalts (bei Schriftsatz)?
- [ ] Anlagen nummeriert und beigefügt?
- [ ] beA-Einreichung vorbereitet? qeS oder einfache Signatur aus eigenem beA?

## Gesamt-Ampel nach Allen Gates

| Gates bestanden | Gesamtampel | Freigabe |
|---|---|---|
| Alle 7 | Grün | Dokument kann ausgegeben werden |
| 6 von 7, kein Rot | Gelb | Mit Kommentar zu offenem Punkt ausgeben |
| 1 Rot | Rot | Nicht ausgeben; erst korrigieren |
| Mehrere Rot | Rot | Vollständige Überarbeitung erforderlich |

## Anschluss-Skills
- `spezial-aktenzeichen-red-team-und-qualitaetskontrolle` für Aktenzeichen-spezifisches Red-Team
- `workflow-rechtsquellen-livecheck` für Quellenverifikation
- `spezial-quelle-beweislast-und-darlegungslast` für Quellenregeln

## Quellenregel
- Normtext live prüfen auf [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- BAG: [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de).
- EuGH: [curia.europa.eu](https://curia.europa.eu).
- Keine Aktenzeichen aus Modellwissen ohne Verifikation.
- Annahmen explizit kennzeichnen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für vollständige anwaltliche Prüfung.
- Keine Garantie für Fehlerfreiheit; menschliche Kontrolle bleibt zwingend.

## 2. `spezial-rechtsprechung-internationaler-bezug-und-schnittstellen`

**Fokus:** Internationaler Bezug im Arbeitsrecht: EuGH-Rechtsprechung (Massenentlassung, Befristung, Diskriminierung, Urlaub), EU-Richtlinien (RL 2023/970, RL 2001/23, RL 2008/94, RL 2003/88), Entsendung AEntG, internationales Privatrecht Rom I.

# Spezial: Rechtsprechung — Internationaler Bezug und Schnittstellen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Rechtsprechung — Internationaler Bezug und Schnittstellen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Überblick über die EuGH-Linie im Arbeitsrecht und die relevanten EU-Richtlinien mit ihren deutschen Umsetzungsgesetzen. Besondere Bedeutung: Richtlinienkonforme Auslegung, Vorabentscheidungsverfahren und direkte Anwendbarkeit von EU-Recht.

## Einstieg
Wenn ein Sachverhalt mit internationalem Bezug oder einer EU-Rechtsfrage vorliegt:

1. **EuGH oder nationales Recht?** Ist eine EU-Richtlinie berührt?
2. **Entsendung?** Gelten Pflichten nach AEntG oder EU-Entsenderecht (RL 96/71/EG, RL 2018/957)?
3. **Grenzüberschreitendes Arbeitsverhältnis?** Welches Recht gilt? (Rom I-VO Art. 8)
4. **Aktuelle EuGH-Vorlage?** Liegt ein Vorabentscheidungsverfahren zu einer relevanten Norm vor?

## EuGH-Linien im Deutschen Arbeitsrecht

### 1. Massenentlassung — RL 98/59/EG

**EuGH C-134/24 / C-402/24 (30.10.2025):** Massenentlassungsanzeige ist Wirksamkeitsvoraussetzung. Fehler bei der Anzeige führen zur Unwirksamkeit der Kündigungen; keine Heilung nach Kündigungsausspruch. Die Anzeige muss vor Ausspruch der Kündigungen bei der zuständigen Behörde eingegangen sein.

**Umsetzung in Deutschland:** § 17 KSchG; Konsequenz aus BAG 6 AZR 152/22 und EuGH-Linie: Anzeige nach Abschluss der BR-Konsultation, vor Ausspruch der Kündigungen.

**Quellenregel:** EuGH-Urteile via [curia.europa.eu](https://curia.europa.eu); BAG via [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de).

### 2. Betriebsübergang — RL 2001/23/EG (Übergangsrichtlinie)

- EuGH-Linie (Spector Rs. C-13/95 — Süzen und Nachfolgeentscheidungen): wirtschaftliche Einheit muss ihre Identität wahren; Kriterien für betriebsmittelintensive vs. dienstleistungsintensive Branchen unterschiedlich
- Umsetzung in Deutschland: § 613a BGB
- Haftungsfolgen: gesamtschuldnerische Haftung alter und neuer Inhaber (§ 613a Abs. 2 BGB)

### 3. Urlaubsrecht — RL 2003/88/EG (Arbeitszeitrichtlinie)

- **EuGH-Urteile:** Kein Verfall des Urlaubs ohne Hinweis des Arbeitgebers (Schultz-Hoff, King, Kreuziger); Deutschland hat dies im BUrlG durch BAG-Rechtsprechung umgesetzt
- **BAG 9 AZR 104/24 (03.06.2025):** Kein Urlaubsverzicht durch Prozessvergleich
- Umsetzung in Deutschland: §§ 1–13 BUrlG; BAG hat die EuGH-Linie integriert

### 4. Gleichbehandlung / Diskriminierung

- **RL 2006/54/EG** (Gleichbehandlung bei Beschäftigung, Geschlecht): Umsetzung durch AGG
- **RL 2000/43/EG** (Rassendiskriminierung), **RL 2000/78/EG** (allgemeiner Rahmen): ebenfalls AGG
- **EuGH zur Beweislast:** Indizienvortrag genügt; Arbeitgeber muss widerlegen (umgesetzt in § 22 AGG)
- **EU-Lohntransparenz-RL 2023/970:** Umsetzung bis 7. Juni 2026; aktuellen Stand live prüfen

### 5. Befristung — RL 1999/70/EG (Befristungsrichtlinie)

- **Kettenbefristungsverbot:** RL schreibt Maßnahmen gegen Missbrauch vor; BAG hat Missbrauchsprüfung entwickelt
- **EuGH zu Betriebsratsmitgliedern:** BAG 7 AZR 50/24 (18.06.2025) nach EuGH-Vorlage: § 14 Abs. 2 TzBfG gilt auch für BR-Mitglieder; Verweigerung des Folgevertrags wegen BR-Mandat = Schadensersatz

## Internationales Privatrecht — Rom I-VO Art. 8

### Anzuwendendes Recht bei Auslandsbezug
Art. 8 Rom I-VO (VO EG 593/2008): Für Arbeitnehmer gilt das Recht des Staates, in dem der Arbeitnehmer gewöhnlich seine Arbeit verrichtet — auch wenn er vorübergehend in einen anderen Staat entsandt wird. Abweichung durch Rechtswahl möglich, wenn das gewählte Recht den Arbeitnehmer nicht schlechter stellt als das objektiv anwendbare.

**Praxis-Beispiel:** Deutsches Unternehmen entsendet Arbeitnehmer nach Polen für 2 Jahre → grundsätzlich deutsches Recht bleibt anwendbar; polnische Mindeststandards nach AEntG zu beachten.

## Entsendung — AEntG und EU-Entsenderecht

### Anwendung des AEntG
- Bei Entsendung von Arbeitnehmern nach Deutschland (inbound): AEntG gilt; Mindestlohn, Urlaub, Sicherheit und Gesundheitsschutz nach deutschem Recht für die Dauer der Entsendung
- Umsetzung der RL 2018/957/EU (Änderungsrichtlinie): bei Entsendungen > 12 Monate im Wesentlichen alle Arbeitsbedingungen des Aufnahmestaats

### Meldepflichten
Entsendendes Unternehmen muss Entsendung bei der ZKA (Zentrale Kontrolle der Schwarzarbeit / Zoll) melden. Unterlassung → Ordnungswidrigkeit.

## Vorabentscheidungsverfahren und Bedeutung für deutsche Praxis

| EuGH-Verfahren | Streitfrage | Deutsche Norm | Status |
|---|---|---|---|
| C-134/24 | Massenentlassung: Wirksamkeitsvoraussetzung | § 17 KSchG | Entschieden 30.10.2025 |
| C-13/95 (Süzen) | Betriebsübergang: Identitätskriterien | § 613a BGB | Grundlegendes Urteil |
| Schultz-Hoff | Urlaubsverfall bei Krankheit | § 7 BUrlG | Umgesetzt in BAG-Linie |
| King | Urlaubsanspruch bei fehlendem Hinweis | § 7 BUrlG | Umgesetzt in BAG-Linie |

**Wichtig:** Vor Ausgabe von EuGH-Aktenzeichen stets verifizieren auf [curia.europa.eu](https://curia.europa.eu). Keine Aktenzeichen aus Modellwissen ohne Verifikation.

## Anschluss-Skills
- `spezial-rechtsprechung-livecheck-arbeitsrecht` für Live-Verifikation von Urteilen
- `fachanwalt-arbeitsrecht-massenentlassung-17-kschg` für § 17 KSchG-Details
- `ar-betriebsuebergang-spezial` für § 613a BGB

## Quellenregel
- EuGH-Urteile via [curia.europa.eu](https://curia.europa.eu).
- BAG-Urteile via [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de).
- EU-Richtlinien via [eur-lex.europa.eu](https://eur-lex.europa.eu).
- Nationales Recht via [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Keine Aktenzeichen aus Modellwissen ohne Verifikation.

## Was dieser Arbeitsgang nicht macht
- Keine umfassende Beratung zu internationalem Arbeitsrecht in Drittstaaten (USA, Großbritannien etc.).
- Keine Prüfung von Sozialversicherungs-Entsenderecht (A1-Bescheinigung, Entsende-SV-Koordinierung).

## 3. `spezial-rechtsprechung-livecheck-arbeitsrecht`

**Fokus:** Live-Check für arbeitsrechtliche Rechtsprechung: Prüfprotokoll für BAG-, LAG- und EuGH-Zitate, Verifizierungswege über bundesarbeitsgericht.de, openjur.de, dejure.org, curia.europa.eu, Umgang mit nicht verifizierbaren Quellen.

# Spezial: Rechtsprechung Live-Check Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Rechtsprechung Live-Check Arbeitsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Strukturierter Prüffür die Verifikation arbeitsrechtlicher Rechtsprechungszitate — bevor sie in Schriftsätze, Memos oder Beratungshinweise einfließen. Dieser Skill verhindert Scheinzitate und stärkt die anwaltliche Glaubwürdigkeit.

## Einstieg
Wenn Urteile zitiert werden sollen oder bereits zitierte Urteile zu prüfen sind:

1. **Welche Urteile sind zu prüfen?** Liste der Aktenzeichen mit Datum
2. **Welche Quelle ist bisher angegeben?** BeckRS, juris, Modellwissen, URL?
3. **Ist das Urteil öffentlich zugänglich?** Via BAG-Website, openjur.de, dejure.org?
4. **Wird nur der Tenorierungssatz gebraucht oder der vollständige Begründungstext?**

## Prüfprotokoll: BAG-Entscheidungen

### Schritt 1: BAG-Website
Primärquelle für BAG-Entscheidungen: [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de)
- Rubrik „Entscheidungen" → Suche nach Datum oder Aktenzeichen
- Volltext in PDF verfügbar (nicht für alle Entscheidungen; ältere oft nur Kurzform)
- Pressemitteilungen für aktuelle Leitsätze

### Schritt 2: Dejure.org
[dejure.org](https://dejure.org) vernetzt BAG-Aktenzeichen mit dem Gesetzestext und zeigt zitierende und zitierte Entscheidungen.
- Gut für Normverknüpfung und Überblick
- Nicht für vollständige Urteilstexte; verlinkt zum BAG oder openjur.de

### Schritt 3: OpenJur
[openjur.de](https://openjur.de) enthält Volltext-Entscheidungen von BAG, LAG und ArbG (soweit veröffentlicht).
- Kostenlos; gute Volltextsuche
- Nicht alle Entscheidungen vorhanden; Abdeckung variiert

### Schritt 4: Wenn Quelle nicht öffentlich
- Entscheidung als „zu prüfen" kennzeichnen
- Keine Zitierung ohne Verifikation in Schriftsätzen
- Im Memo: explizit vermerken „Quelle: [Angabe]; nicht frei zugänglich — vor Verwendung in Schriftsatz verifizieren"

## Prüfprotokoll: EuGH-Entscheidungen

**Primärquelle:** [curia.europa.eu](https://curia.europa.eu)
- Volltextsuche nach Rechtssache-Nummer (z.B. C-134/24) oder Suchbegriff
- Alle Entscheidungen in allen EU-Amtssprachen kostenlos verfügbar

**Alternativ:** [eur-lex.europa.eu](https://eur-lex.europa.eu) für Verlinkung mit Richtlinien und Verordnungen.

## Prüfprotokoll: BVerfG-Entscheidungen

**Primärquelle:** [bverfg.de](https://www.bverfg.de)
- Volltext-Entscheidungen kostenlos; Pressemitteilungen für aktuelle Entscheidungen
- Suche nach Aktenzeichen (z.B. 1 BvR 123/24) oder Datum

## Prüfprotokoll: LAG-Entscheidungen

- [openjur.de](https://openjur.de): Hauptquelle für LAG-Volltext
- Landesjustizportale (z.B. NRW: nrwe.de; Bayern: gesetze-bayern.de)
- Direkte LAG-Website (manche LAG veröffentlichen eigene Entscheidungsdatenbanken)

## Typische Fehlerquellen und Risiken

| Fehler | Risiko | Vermeidung |
|---|---|---|
| BAG-Aktenzeichen aus KI-Output | Aktenzeichen existiert nicht oder passt nicht | Stets über bundesarbeitsgericht.de verifizieren |
| Falsche Zuordnung Senat/Datum | Zitat passt nicht zum Streitpunkt | Volltext lesen, nicht nur Leitsatz |
| Veraltete Rechtsprechung | Urteil durch neueres überholt | Dejure.org: „nachfolgende Entscheidungen" prüfen |
| BeckRS als einzige Fundstelle | Nicht öffentlich zugänglich; nicht frei prüfbar | Nur BeckRS-Nummer verwenden wenn BAG-URL als Primärquelle angegeben |
| Falsche Randnummer | Urteil wird mit falscher Randnummer zitiert | Volltext lesen und Rn. prüfen |

## Live-Check-(Kurzfassung)

```
1. Aktenzeichen und Datum notieren
2. Suche auf bundesarbeitsgericht.de (BAG) / curia.europa.eu (EuGH)
3. Entscheidung gefunden? → URL notieren; Kernsatz aus Volltext entnehmen
4. Nicht gefunden? → openjur.de versuchen
5. Immer noch nicht gefunden? → Als "nicht verifiziert" markieren
6. Nie aus Modellwissen zitieren ohne Verifikation
```

## Muster-Quellenangabe für Schriftsatz
> „BAG, Urteil vom 01.04.2026, Az. 6 AZR 152/22, Rn. [X], abrufbar unter: [URL auf bundesarbeitsgericht.de]"

> „EuGH, Urteil vom 30.10.2025, Rs. C-134/24, ECLI:EU:C:2025:[XXX], abrufbar unter: [URL auf curia.europa.eu]"

## Aktuelle Leitentscheidungen (Stand Mai 2026) — Kurze Referenzliste

| Entscheidung | Kernsatz | Primärquelle |
|---|---|---|
| BAG 6 AZR 152/22 (01.04.2026) | Massenentlassung: Anzeige vor BR-Konsultationsabschluss → Unwirksamkeit | bundesarbeitsgericht.de |
| EuGH C-134/24 (30.10.2025) | Massenentlassungsanzeige als Wirksamkeitsvoraussetzung | curia.europa.eu |
| BAG 5 AZR 108/25 (25.03.2026) | Pauschale Freistellungsklausel § 307 BGB unwirksam | bundesarbeitsgericht.de |
| BAG 9 AZR 104/24 (03.06.2025) | Kein Urlaubsverzicht durch Prozessvergleich | bundesarbeitsgericht.de |
| BAG 8 AZR 300/24 (23.10.2025) | Paarvergleich genügt für AGG-Vermutung | bundesarbeitsgericht.de |
| BAG 7 AZR 50/24 (18.06.2025) | § 14 Abs. 2 TzBfG gilt für BR-Mitglieder | bundesarbeitsgericht.de |

**Wichtig:** Alle Aktenzeichen in dieser Liste müssen vor Verwendung in Schriftsätzen live auf bundesarbeitsgericht.de verifiziert werden. Die obige Liste dient als Orientierung, nicht als zitierfähige Quelle.

## Anschluss-Skills
- `spezial-quelle-beweislast-und-darlegungslast` für Quellenregeln
- `spezial-aktenzeichen-red-team-und-qualitaetskontrolle` für Schriftsatzprüfung
- `workflow-rechtsquellen-livecheck` für Live-Prüfung von Normen

## Quellenregel
- BAG: [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de)
- EuGH: [curia.europa.eu](https://curia.europa.eu)
- BVerfG: [bverfg.de](https://www.bverfg.de)
- LAG/ArbG: [openjur.de](https://openjur.de)
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de)
- Vernetzung: [dejure.org](https://dejure.org)
- Keine Aktenzeichen aus Modellwissen ohne Verifikation.

## Was dieser Arbeitsgang nicht macht
- Keine automatische Live-Prüfung von Rechtsprechungsdatenbanken; Prüfung erfolgt durch den Anwalt.
- Keine Verfügbarkeitsgarantie für ältere oder unveröffentlichte Entscheidungen.
