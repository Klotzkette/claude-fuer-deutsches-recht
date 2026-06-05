---
name: pensionsmodelle-fuenf-bav-cta-pensionsfond
description: "Pensionsmodelle Fuenf BAV CTA Pensionsfond: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pensionsmodelle Fuenf BAV CTA Pensionsfond

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pensionsmodelle Fuenf BAV CTA Pensionsfond** im Plugin Bav Strategie Konzern. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pensionsmodelle-fuenf-durchfuehrungswege` | Fuenf Durchführungswege der betrieblichen Altersversorgung vergleichen und waehlen. Normen: §§ 1 1b BetrAVG. Prüfraster: Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds - Vor- und Nachteile. Output: Durchführungsweg-Empfehlung. Abgrenzung: nicht steuerliche Behandlung § 6a EStG. |
| `bav-cta-treuhand-spezial` | Spezialfall Contractual Trust Arrangement CTA: doppelseitige Treuhand, Insolvenzschutz durch Verpfaendung an Arbeitnehmer, IFRS-Status Trust Assets, deutsche HGB-Bilanzierung. Pruefraster und Mustertexte fuer Trust-Setup im Konzern. |
| `bav-pensionsfond-rueckdeckung-spezial` | Spezialfall Pensionsfonds mit Rueckdeckungsversicherung: hybride Konstruktion, Trennung Versorgungstraeger und Versicherer, PSV-Schutz im Insolvenzfall, Anlagenrestriktionen. Pruefraster und Mustertexte fuer Wechsel Direktzusage zu Pensionsfonds. |

## Arbeitsweg

Im Plugin Bav Strategie Konzern gilt für **Pensionsmodelle Fuenf BAV CTA Pensionsfond**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pensionsmodelle-fuenf-durchfuehrungswege`

**Fokus:** Fuenf Durchführungswege der betrieblichen Altersversorgung vergleichen und waehlen. Normen: §§ 1 1b BetrAVG. Prüfraster: Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds - Vor- und Nachteile. Output: Durchführungsweg-Empfehlung. Abgrenzung: nicht steuerliche Behandlung § 6a EStG.

# Pensionsmodelle — Die fünf Durchführungswege der betrieblichen Altersversorgung

## Fachkern: Pensionsmodelle — Die fünf Durchführungswege der betrieblichen Altersversorgung

- **bAV-Problem:** §§ 1 1b BetrAVG. Prüfraster: Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds - Vor- und Nachteile. Output: Durchführungsweg-Empfehlung. Abgrenzung: nicht steuerliche Behandlung § 6a EStG.
- **Normenanker:** BetrAVG, EStG/LSt, SGB IV, HGB/IFRS-Bilanzierung, InsO, ArbGG und arbeitsrechtliche Zusage-/Änderungsdogmatik je nach Durchführungsweg prüfen.
- **Entscheidende Weiche:** Zusageart, Durchführungsweg, Unverfallbarkeit, Anpassung, PSV-Schutz, Steuer-/SV-Folge und M&A-/Insolvenzrisiko getrennt ausweisen.
- **Arbeitsprodukt:** bAV-Entscheidungsvorlage mit Leistungsversprechen, Zahlenbasis, Risikoampel, HR-/Finance-To-dos und belastbarer Kommunikationslinie.

## Rechtsgrundlagen

- §§ 1–6 BetrAVG (Grunddefinitionen, Unverfallbarkeit, Zusagearten)
- § 1b BetrAVG (gesetzliche Unverfallbarkeit nach drei Jahren Betriebszugehörigkeit und Vollendung 21. Lebensjahr — seit 1.1.2018)
- § 7 BetrAVG (Insolvenzsicherung PSV)
- §§ 1–3 BetrAVG (Durchführungswege: § 1 Abs. 1 S. 2 BetrAVG — Direktzusage; § 1b Abs. 4 BetrAVG — Unterstützungskasse; § 1b Abs. 3 BetrAVG — Direktversicherung, Pensionskasse, Pensionsfonds)
- § 6a EStG (Pensionsrückstellungen Direktzusage — steuerliche Voraussetzungen)
- § 4d EStG (Zuwendungen an Unterstützungskassen)
- §§ 236–242 VAG (Pensionsfonds-Aufsicht durch BaFin)
- §§ 232–235 VAG (Pensionskassen)
- IAS 19 (Employee Benefits — Defined Benefit Obligations, DBO, Service Cost)
- IORP II (EU-Richtlinie 2016/2341/EU — Einrichtungen der betrieblichen Altersversorgung)
- HGB § 246 Abs. 2 S. 2 (Saldierungsgebot bei CTA-Deckungsvermögen)
- BAG-Rechtsprechung zu Durchführungswegen, Unverfallbarkeit und Insolvenzsicherung: konkrete Aktenzeichen vor Versand in bundesarbeitsgericht.de oder dejure.org aufrufen.
- BSG-Rechtsprechung zu Sozialversicherungspflicht von bAV-Beiträgen: konkrete Aktenzeichen in bsg.bund.de oder dejure.org verifizieren.
- **Stand Mai 2026: Mindestbesteuerungsgesetz (MinBestG)** vom 27.12.2023, BGBl. I 2023 Nr. 397 — OECD Pillar 2 / GloBE-Regeln; 15 % Mindeststeuer ab 750 Mio. EUR Umsatz; Auswirkung auf Steuerwirkung von Pensionsrückstellungen § 6a EStG und Deferred Tax Assets im IFRS-Konzern. OECD GloBE Administrative Guidance (5. Tranche Januar 2025).
- **Beitragsbemessungsgrenze 2025**: erstmals einheitliche BBG West/Ost (alle Werte vor Versand auf bundesfinanzministerium.de oder deutsche-rentenversicherung.de prüfen).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vorgehen

### Schritt 1: Bestandsaufnahme und Ausgangslage

fachliche Leitung eröffnet die Mandatsbearbeitung stets mit einem strukturierten Fragebogen (→ Checkliste unten). Erfasst werden:
1. Anzahl aktiver Anwärter, Rentner, unverfallbar Ausgeschiedener (getrennt nach Gesellschaften)
2. Bestehende Zusagearten (Leistungs-, Beitrags-, beitragsorientierte Leistungszusage gem. § 1 Abs. 2 BetrAVG)
3. Derzeitiger Durchführungsweg und etwaige Mischstrukturen
4. Bilanzierungspflicht (HGB-Konzernabschluss, IFRS-Konzernabschluss, beides)
5. Sanierungsbedarf Unterdeckung (Pensionskassen §§ 232 ff. VAG)
6. Tarifbindung und kollektivrechtliche Einschränkungen

### Schritt 2: Analyse der fünf Durchführungswege

#### 2.1 Direktzusage (Pensionsrückstellung)

**Rechtsform:** Unmittelbare Verpflichtung des Arbeitgebers.

**Steuer:** Rückstellungsbildung gem. § 6a EStG; Teilwert-Methode; steuerlicher Rechnungszins 6 % (steuerpolitisch kontrovers, verfassungsrechtlich noch nicht abschließend geklärt — BVerfG-Vorlage ausstehend).

**Handelsrecht:** Pflichtansatz gem. § 249 Abs. 1 HGB; Abzinsungszinssatz gem. § 253 Abs. 2 HGB (10-Jahres-Durchschnittszinssatz der Deutschen Bundesbank, aktuell ca. 1,8 %).

**IFRS:** IAS 19 — DBO (Defined Benefit Obligation) nach PUC-Methode (Projected Unit Credit); Service Cost, Interest Cost, Remeasurements in OCI.

**PSV-Pflicht:** Ja, gem. § 7 BetrAVG.

**Vorteile:**
- Maximale Flexibilität bei Leistungsgestaltung
- Kein aufsichtsrechtlicher Rahmen
- Steuerliche Abzugsfähigkeit der Zuführungen

**Nachteile:**
- Volle Bilanzbelastung (IFRS und HGB)
- Finanzierungsrisiko liegt beim Arbeitgeber
- PSV-Beiträge

#### 2.2 Unterstützungskasse

**Rechtsform:** Rechtlich selbständige Einrichtung (e.V., GmbH, Stiftung); kein Rechtsanspruch des Begünstigten auf Leistung gem. § 1b Abs. 4 BetrAVG.

**Steuer:** Zuwendungen abzugsfähig gem. § 4d EStG (bei Rentnern sofort, bei Anwärtern nach Tabellenwert-Methode begrenzt); Kasse selbst körperschaftsteuerfrei.

**Handelsrecht/IFRS:** Rückdeckungsversicherung bei Saldierung gem. HGB § 246 Abs. 2 S. 2 / IAS 19 plan asset möglich.

**PSV-Pflicht:** Ja.

**Vorteile:**
- Eigenständige Vermögensverwaltung möglich
- Flexibilität bei Kapitalanlage
- Steuerliche Vorteile bei Rückdeckungsgestaltung

**Nachteile:**
- Kein Rechtsanspruch des Arbeitnehmers gegenüber Kasse (nur gegenüber Arbeitgeber)
- Komplexe Verwaltung
- § 4d EStG-Beschränkungen

#### 2.3 Pensionskasse

**Rechtsform:** VAG-beaufsichtigtes VVaG oder AG; Arbeitnehmer hat Rechtsanspruch gegen Kasse.

**Aufsicht:** BaFin gem. §§ 232–235 VAG; Bedeckungspflicht (Solvency I-analoges Regime für kleine Kassen, IORP II für EbAV).

**PSV-Pflicht:** Nur für Kassen, die nicht der Sicherungseinrichtung gem. § 8 BetrAVG angeschlossen sind.

**Handelsrecht/IFRS:** Bei ausreichender Dotierung ggf. keine HGB-Rückstellung (§ 249 Abs. 1 S. 3 HGB a.F. — beachte aktuelle Rechtsprechungsentwicklung); IAS 19 plan asset.

**Vorteile:**
- Risikotransfer auf Kasse
- Steuerliche Förderung (§ 3 Nr. 63 EStG bis EUR 7.248 steuerfrei — 2024)
- Arbeitnehmer hat direkten Rechtsanspruch

**Nachteile:**
- Haftung für Sanierungsbeiträge (§ 233 Abs. 1 VAG i.V.m. Satzung) kann zurückfallen
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Eingeschränkte Kapitalanlage-Flexibilität

#### 2.4 Pensionsfonds

**Rechtsform:** Rechtsfähige Versorgungseinrichtung gem. § 236 VAG; kapitalmarktnäher Durchführungsweg.

**Aufsicht:** BaFin gem. §§ 236–242 VAG; IORP II; MaRisk entsprechend.

**PSV-Pflicht:** Ja, aber eingeschränkt wenn Leistungsplan (§ 7 Abs. 1 S. 2 Nr. 1 BetrAVG).

**Steuer:** § 4e EStG — Beiträge sofort abzugsfähig (kein § 6a-Tabellenschema).

**IFRS:** IAS 19 plan asset bei ausreichender Saldierbarkeit.

**Vorteile:**
- Hohe Kapitalanlage-Flexibilität
- Sofortige steuerliche Abzugsfähigkeit
- Für große Konzerne: eigener Pensionsfonds möglich
- Beste Möglichkeit zur Bilanzentlastung (IFRS plan asset)

**Nachteile:**
- Komplex und kostenintensiv zu etablieren
- Aufsichtsrechtliches Regime (BaFin)
- Bei Unterdeckung: Arbeitgeber muss leisten

#### 2.5 Direktversicherung

**Rechtsform:** Lebensversicherung auf das Leben des Arbeitnehmers; Versicherungsnehmer = Arbeitgeber oder Arbeitnehmer (nach Übertragung gem. § 4 BetrAVG).

**PSV-Pflicht:** Nein (wenn unwiderrufliches Bezugsrecht, § 7 Abs. 1 S. 2 Nr. 2 BetrAVG).

**Steuer:** § 3 Nr. 63 EStG bis EUR 7.248 p.a. steuerfrei (2024); Pauschalversteuerung § 40b EStG a.F. (Altverträge).

**IFRS:** Bei Qualifying Insurance Policy: plan asset gem. IAS 19.8.

**Vorteile:**
- Einfachste Administration
- Kein PSV
- Portabilität bei § 4 BetrAVG-Übertragung

**Nachteile:**
- Kapitalanlage-Flexibilität begrenzt durch Versicherungsprodukt
- Bei Kündigung: Rückkaufswert ggf. unter Prämienvolumen

### Schritt 3: Entscheidungsmatrix

| Kriterium | Direktzusage | Unterstützungskasse | Pensionskasse | Pensionsfonds | Direktversicherung |
|-----------|-------------|-------------------|---------------|---------------|--------------------|
| HGB-Bilanzbelastung | Hoch | Mittel (bei Rückdeckung) | Niedrig | Niedrig | Keine |
| IFRS plan asset | Nur mit CTA | Ja (mit CTA) | Ja | Ja | Ja (qualifying) |
| PSV-Pflicht | Ja | Ja | Ggf. Nein | Ja (begrenzt) | Nein |
| Flexibilität Leistung | Sehr hoch | Hoch | Mittel | Mittel | Niedrig |
| Kapitalanlage-Freiheit | Hoch (CTA) | Hoch | Begrenzt | Hoch | Niedrig |
| Steuerliche Effizienz | Mittel | Mittel | Hoch | Hoch | Hoch |
| Admin-Aufwand | Mittel | Hoch | Mittel | Hoch | Niedrig |
| Geeignet für | Groß-/Konzern | Groß-/Konzern | Mittelstand | Großkonzern | KMU/individuelle |

### Schritt 4: Empfehlungs-Framework bAV-Projektteam

**Regel 1 — IFRS-Bilanzentlastung priorisieren:** Bei IFRS-Abschluss sollte stets geprüft werden, ob ein CTA (→ Skill `cta-contractual-trust-arrangement-strukturierung`) oder ein ausfinanzierter Pensionsfonds die DBO auf Nettobasis darstellen kann.

**Regel 2 — PSV-Kosten minimieren:** Bei Pensionskassen mit eigener Sicherungseinrichtung und Direktversicherungen mit unwiderruflichem Bezugsrecht entfällt der PSV-Beitrag (Beitragssatz zuletzt ca. 3,4 ‰ auf Beitragsbemessungsgrundlage).

**Regel 3 — Kollektivrechtliche Bindungen prüfen:** Tarifliche BAV-Ansprüche (z.B. ATV, ATV-K) können Durchführungsweg vorgeben.

---

## Templates

### Template A: Entscheidungsprotokoll Durchführungsweg (Muster)

```
TREUENFELS YAMAMOTO RECHTSANWÄLTE PARTNERSCHAFT mbB
Königsalle 92 · 40212 Düsseldorf

INTERNES ARBEITSPROTOKOLL — VERTRAULICH

Mandant: [Fiktive Konzern GmbH & Co. KG]
Projekt: Auswahl Durchführungsweg BAV
Datum: [Datum]
Federführung: fachliche Leitung, LL.M. (Oxford)
Mitarbeit: [Senior Associate Name], [Associate Name]

1. AUSGANGSSACHVERHALT
 Anwärter aktiv: [Anzahl]
 Rentner: [Anzahl]
 DBO (IFRS, aktuariell): EUR [Betrag]
 Bestand Direktzusagen: EUR [Betrag] Rückstellungen (HGB)

2. ANALYSEERGEBNIS DURCHFÜHRUNGSWEGE
 [Tabelle Vor-/Nachteile je Durchführungsweg — mandantenspezifisch]

3. EMPFEHLUNG
 Empfohlener Durchführungsweg: [...]
 Begründung: [...]
 Erforderliche Maßnahmen: [...]

4. NÄCHSTE SCHRITTE
 □ Abstimmung mit Wirtschaftsprüfer (Bilanzierungseffekte)
 □ Abstimmung mit Betriebsrat (§ 87 Abs. 1 Nr. 8 BetrVG)
 □ Aktuarielle Bestätigung
 □ BaFin-Konzession prüfen (sofern Pensionsfonds/Pensionskasse)
```

### Template B: Mandats-Checkliste Durchführungsweg-Analyse

```
CHECKLISTE — INFORMATIONSANFORDERUNG BAV-DURCHFÜHRUNGSWEG
bAV-Projektteam · fachliche Leitung

□ Vollständige Liste aller bestehenden Versorgungsordnungen (VOs)
□ Aktuelle Mitarbeiterliste mit Eintrittsdatum, Geburtsdatum, Zusagedatum
□ Letzter versicherungsmathematischer Gutachten-Bericht
□ Jahresabschlüsse letzter drei Geschäftsjahre (HGB und ggf. IFRS)
□ PSV-Beitragsbescheide letzter zwei Jahre
□ Bestehende Treuhandverträge / CTA-Dokumentation
□ Gesellschaftsvertrag / Satzung der Versorgungseinrichtung (sofern vorhanden)
□ Alle Betriebsvereinbarungen mit BAV-Bezug
□ Kollektivverträge / Tarifverträge mit Versorgungsregelungen
□ Rückdeckungsversicherungs-Policen
```

---

## Fallstricke

1. **§ 6a EStG-Steuerstundungseffekt überschätzen:** Der Teilwert-Ansatz mit 6 % Rechnungszins führt zur erheblichen Divergenz zwischen steuerlicher Rückstellung und HGB-Rückstellung. Mandanten überschätzen häufig die steuerliche Entlastungswirkung.

1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

3. **IORP II-Umsetzungslücken:** Deutschland hat IORP II (RL 2016/2341/EU) in §§ 232 ff. VAG umgesetzt. Konzerneigene Pensionskassen müssen seit 2019 umfangreiche Governance-Anforderungen (ORSA, eigene Risikobeurteilung, Schlüsselfunktionen) erfüllen — oft unterschätzt.

4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

6. **Sozialversicherungsrechtliche Fallgruben:** § 1 Abs. 2 Nr. 2 SGB VI (Versicherungsfreiheit reine DC bei Zusageart Beitragszusage mit Mindestleistung) ist komplex; falsche Einordnung führt zu SV-Nachforderungen.

---

## Querverweise zu anderen Skills

- → `cta-contractual-trust-arrangement-strukturierung` — für Bilanzentlastung via Doppeltreuhand
- → `governance-und-anpassungsmechanismen` — für Pension Committee und Trustee-Board-Governance
- → `drei-stufen-theorie-eingriffsanalyse` — bei Umstellung bestehender Zusagen
- → `versorgungsordnung-und-betriebsvereinbarung-drafting` — für VO/BV-Templates je Durchführungsweg

## 2. `bav-cta-treuhand-spezial`

**Fokus:** Spezialfall Contractual Trust Arrangement CTA: doppelseitige Treuhand, Insolvenzschutz durch Verpfaendung an Arbeitnehmer, IFRS-Status Trust Assets, deutsche HGB-Bilanzierung. Pruefraster und Mustertexte fuer Trust-Setup im Konzern.

# bAV: CTA Treuhand

## Spezialwissen: bAV: CTA Treuhand
- **Spezialgegenstand:** bAV: CTA Treuhand / bav cta treuhand spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** CTA, IFRS, HGB.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `bav-pensionsfond-rueckdeckung-spezial`

**Fokus:** Spezialfall Pensionsfonds mit Rueckdeckungsversicherung: hybride Konstruktion, Trennung Versorgungstraeger und Versicherer, PSV-Schutz im Insolvenzfall, Anlagenrestriktionen. Pruefraster und Mustertexte fuer Wechsel Direktzusage zu Pensionsfonds.

# bAV: Pensionsfonds-Rueckdeckung

## Spezialwissen: bAV: Pensionsfonds-Rueckdeckung
- **Spezialgegenstand:** bAV: Pensionsfonds-Rueckdeckung / bav pensionsfond rueckdeckung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** PSV.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
