# Aktenstück 21 – BSI IT-SIG 2.0 / KRITIS-Rechtliche Analyse

**Aktenzeichen:** VK 1-32/26  
**Vorhabenbezeichnung:** LH-SN-Cyber-SOC-NSV-2026  
**Datum:** 15.03.2026 (Gutachten, erstellt vor Verfahrensbeginn)  
**Erstellt von:** RA Dr. Constantin Bährens / Fachberatung IT-Sicherheitsrecht

---

## Rechtsgutachten: BSI IT-Sicherheitsgesetz 2.0, KRITIS-Anforderungen und NIS2 im ÖPNV-Vergabeverfahren

### 1. Ausgangsfrage

Welche rechtlichen Anforderungen stellen das IT-Sicherheitsgesetz 2.0 (IT-SIG 2.0), die KRITIS-Verordnung Verkehr und die NIS2-Richtlinie an Auftragsleistungen im Bereich SOC und IT-Sicherheitsberatung für einen ÖPNV-KRITIS-Betreiber?

---

### 2. Das IT-Sicherheitsgesetz 2.0 (IT-SIG 2.0)

Das **IT-Sicherheitsgesetz 2.0** (Gesetz zur Erhöhung der Sicherheit informationstechnischer Systeme vom 18.05.2021, BGBl. I S. 1122) hat das BSIG in mehreren Punkten wesentlich verschärft:

**2.1 Erweiterung der KRITIS-Betreiberkreise**

§ 2 Abs. 10 BSIG n.F. erweitert den KRITIS-Begriff auf „Unternehmen im besonderen öffentlichen Interesse" (UNBÖFI), darunter:
- Rüstungsunternehmen (§ 2 Abs. 14 Nr. 1 BSIG)
- Unternehmen von erheblicher volkswirtschaftlicher Bedeutung (§ 2 Abs. 14 Nr. 2 BSIG)
- Betreiber kritischer Anlagen unterhalb des Schwellenwerts (§ 2 Abs. 14 Nr. 3 BSIG)

Die NSV Nahverkehr Schwerin GmbH fällt als ÖPNV-Betreiber mit mehr als 50.000 beförderten Personen täglich in den klassischen KRITIS-Sektor Verkehr (§ 2 Abs. 10 Nr. 1 lit. d BSIG i.V.m. KRITIS-VO Verkehr).

**2.2 Verschärfte Anforderungen § 8a BSIG**

§ 8a Abs. 1 BSIG n.F. verpflichtet KRITIS-Betreiber, „angemessene organisatorische und technische Vorkehrungen" zum Schutz ihrer KRITIS-Anlagen zu treffen. Konkretisierend schreibt § 8a Abs. 1a BSIG (neu durch IT-SIG 2.0) vor:

- **Systeme zur Angriffserkennung** (Attack Detection Systems – ADS): Ab 01.05.2023 verpflichtend für alle KRITIS-Betreiber
- Die ADS müssen dem BSI auf Anforderung nachgewiesen werden
- Ein SOC, das 24/7-Monitoring betreibt, gilt als qualifiziertes Angriffserkennungssystem im Sinne von § 8a Abs. 1a BSIG

Damit ist der Leistungsgegenstand der Ausschreibung (SOC Managed Service) unmittelbar gesetzlich geboten. Der Auftragnehmer des SOC-Vertrags erbringt eine Leistung, die der KRITIS-Betreiber kraft Gesetzes sicherstellen muss.

**2.3 Meldepflichten § 8b BSIG**

§ 8b Abs. 4 BSIG verpflichtet KRITIS-Betreiber, erhebliche Sicherheitsvorfälle unverzüglich (innerhalb von 72 Stunden) an das BSI zu melden. Der Auftragnehmer des SOC-Vertrags ist verpflichtet, diese Meldungen zu unterstützen und auf Anforderung forensische Erstdokumentation zu liefern.

**2.4 Anforderungen an kritische Komponenten (§ 9b BSIG)**

Kritische Komponenten – definiert als IT-Produkte, die in KRITIS-Anlagen eingesetzt werden und bei denen Beeinträchtigungen zu Ausfällen führen können – dürfen nur mit Zustimmung des Bundesministeriums des Innern (BMI) eingesetzt werden, wenn der Hersteller aus einem Nicht-EU-Drittstaat stammt.

Für die Ausschreibung bedeutet dies: SIEM-Software und andere SOC-Kernkomponenten aus Drittstaaten (z.B. aus russischer oder chinesischer Herstellers) können nach § 9b BSIG einer BMI-Prüfung unterliegen. Diese Anforderung muss in den Zuschlagskriterien berücksichtigt werden.

---

### 3. KRITIS-Verordnung Verkehr

Die **KRITIS-Verordnung (KritisV)** in der Fassung vom 22.04.2016 (zuletzt geändert durch Änderungsverordnung 2021) definiert in Anhang 7 (Sektor Verkehr) die Schwellenwerte:

| Anlagetyp | Schwellenwert (Betroffene) |
|---|---|
| ÖPNV-Netz | 15 Millionen Fahrgäste pro Jahr |
| Flughafen | 50.000 Flugbewegungen |
| Schienennetz | 15 Millionen Zugkilometer |

Die NSV überschreitet den ÖPNV-Schwellenwert (Schwerin: ca. 25 Mio. Fahrgäste/Jahr). Die KRITIS-Registrierung ist damit obligatorisch.

---

### 4. NIS2-Richtlinie und Übergangsregelungen

Die **NIS2-Richtlinie** (EU 2022/2555, in Kraft seit 16.01.2023) ersetzt die NIS-1-Richtlinie. Umsetzungsfrist: 17.10.2024. Deutschland hat die NIS2 durch das **NIS2-Umsetzungsgesetz (NIS2UmsuCG)** umgesetzt, das am 01.11.2024 in Kraft getreten ist.

**4.1 Einordnung NSV als „wichtige Einrichtung"**

Die NSV fällt als ÖPNV-Betreiber mit mehr als 250 Mitarbeitern und/oder mehr als 50 Mio. EUR Jahresumsatz unter die Kategorie „wichtige Einrichtung" (Annex II NIS2-RL: Sektor Verkehr, Personenbeförderung). Für wichtige Einrichtungen gelten:

- Verschärfte Sicherheitsanforderungen (Art. 21 NIS2-RL) – 10 Mindestmaßnahmen, darunter Incident Detection und SOC-Äquivalent
- Meldepflichten: Frühwarnung binnen 24 Stunden, vollständige Meldung binnen 72 Stunden (Art. 23 NIS2-RL)
- Aufsichtspflichten: Nationaler Behörde (BSI als NCA für Deutschland)

**4.2 Übergangsregelungen**

Das NIS2UmsuCG enthält Übergangsfristen für die Registrierung (bis 31.01.2025) und für die technischen Maßnahmen (ab Registrierung 12 Monate Umsetzungsfrist). Für die NSV laufen diese Fristen Anfang 2026 ab – was die Dringlichkeit der SOC-Beschaffung zusätzlich unterstreicht.

---

### 5. Vergaberechtliche Konsequenzen

**5.1 Eignung: KRITIS-Kompetenz als valides Differenzierungskriterium**

Angesichts der gesetzlichen Anforderungen des IT-SIG 2.0 und der NIS2-RL ist es grundsätzlich zulässig, von Bietern sektorspezifische KRITIS-Erfahrung als qualitatives Zuschlagskriterium zu verlangen. Der ausschreibungsrechtliche Spielraum erlaubt:

- Als **Zuschlagskriterium**: Differenzierung zwischen KRITIS-Sektoren (ÖPNV vs. andere Sektoren) → zulässig und angemessen
- Als **KO-Eignungskriterium**: Zwingender Ausschluss bei fehlender ÖPNV-Erfahrung → nur zulässig, wenn in den Vergabeunterlagen **klar, eindeutig und zwingend** formuliert

Im vorliegenden Fall: Das Kriterium T-2 formulierte „bevorzugt" – kein KO-Kriterium. Der Ausschluss war daher unverhältnismäßig und vergaberechtswidrig (→ bestätigt durch VK-Beschluss vom 25.06.2026).

**5.2 BSI-zertifizierte Anbieter**

Das BSI betreibt ein IT-Sicherheitskennzeichen und anerkannte Prüfstellen. Eine Anforderung, dass der SOC-Betreiber einen BSI-anerkannten Qualitätsstatus hat, wäre sachlich gerechtfertigt. Die Ausschreibung hat dies durch ISO 27001-Anforderung abgedeckt (T-3).

**5.3 Kritische Komponenten (§ 9b BSIG)**

Die Leistungsbeschreibung hätte explizit klarstellen sollen, dass Komponenten aus Nicht-EU-Drittstaaten einer BMI-Prüfung unterliegen können. Dies ist ein Gestaltungshinweis für zukünftige Ausschreibungen.

---

*Dokument-Ende Aktenstück 21*
