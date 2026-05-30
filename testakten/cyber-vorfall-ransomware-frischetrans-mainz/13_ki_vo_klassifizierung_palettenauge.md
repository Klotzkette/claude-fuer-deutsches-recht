# KI-Verordnung — Klassifizierung und Konformitätsbewertung „PalettenAuge AI"

**Aktenstück:** 13  
**Datum:** 12.05.2026  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Anbieter des KI-Systems:** DachAuge GmbH, Rosenthaler Str. 34, 10178 Berlin  
**Bearbeiter:** RA Lukas Drosten, Fachanwalt für IT-Recht

---

## 1. Hintergrund

Die Frischetrans Mittelrhein GmbH setzt das KI-System **„PalettenAuge AI"** der DachAuge GmbH (Berlin) ein. Das System dient der **vorausschauenden Routenoptimierung und Personaleinsatzplanung** für den Fuhrpark von 64 LKW.

Konkreter Einsatz:
- Automatische Tourenplanung basierend auf KI-Prognosen (Auftragslage, Verkehr, Wetter, Fahrerleistungsdaten)
- Personaleinsatzplanung: Das System schlägt vor, welcher Fahrer welche Tour übernimmt, unter Berücksichtigung von Fahrzeugtyp-Qualifikation, Lenk-/Ruhezeiten (EU-VO 561/2006), vergangenen Leistungsdaten und Gesundheitszustand (Krankheitstage aus SAP HR)
- Auslastungsoptimierung und präventive Wartungsvorschläge

**Frage:** Fällt „PalettenAuge AI" unter Anhang III der EU-KI-Verordnung (Verordnung (EU) 2024/1689) als Hochrisiko-KI-System?

---

## 2. Rechtlicher Rahmen — EU-KI-Verordnung

Die Verordnung (EU) 2024/1689 des Europäischen Parlaments und des Rates über künstliche Intelligenz (KI-VO) ist am 01.08.2024 in Kraft getreten. Für Hochrisiko-KI-Systeme gelten die Pflichten ab dem 02.08.2026 (Art. 113 Abs. 2 KI-VO — zwei Jahre nach Inkrafttreten).

**Relevante Geltungszeitpunkte:**
- Allgemeines Inkrafttreten: 01.08.2024
- Geltung Hochrisiko-Pflichten: 02.08.2026 ← **6 Monate bis zur Geltung, Frischetrans muss jetzt handeln**

---

## 3. Klassifizierungsprüfung nach Anhang III KI-VO

### 3.1 Screening aller Anhang-III-Kategorien

**Nr. 1 — Biometrische Identifizierung:** Nicht anwendbar.

**Nr. 2 — Kritische Infrastruktur:** Routenoptimierung für LKW-Logistik könnte als Komponente einer kritischen Versorgungsinfrastruktur gelten. Frischetrans ist als Lebensmittellogistiker für systemrelevante Bäckereien tätig. Eingeschränkte Relevanz — keine eindeutige Einschlägigkeit.

**Nr. 3 — Allgemeine und berufliche Bildung:** Nicht anwendbar.

**Nr. 4 — Beschäftigung, Personalmanagement und Zugang zur Selbstständigkeit:**  
☑ **EINSCHLÄGIG**

Art. 6 Abs. 2 i.V.m. Anhang III Nr. 4 lit. a) und b) KI-VO erfasst KI-Systeme, die bei der **Einstellung oder Auswahl natürlicher Personen** oder für **Entscheidungen über Arbeitsbedingungen, Beförderungen und Kündigungen** eingesetzt werden.

Das PalettenAuge-AI-System schlägt die Personaleinsatzplanung vor — also, welcher Fahrer welche Tour übernimmt. Dabei fließen leistungsbezogene Daten und Gesundheitsdaten (Krankheitstage) ein. Die Entscheidungsvorschläge des Systems haben direkten Einfluss auf:
- Arbeitsbedingungen (Tourenlänge, Nacht-/Frühschichten)
- Tatsächliche Arbeitszuweisung
- Indirekt: Leistungsbeurteilung (da Tourdaten archiviert werden)

**Nr. 5 — Zugang zu Dienstleistungen:** Nicht primär anwendbar.

**Nr. 6 — Strafverfolgung:** Nicht anwendbar.

**Nr. 7 — Migration, Asyl, Grenzkontrolle:** Nicht anwendbar.

**Nr. 8 — Rechtspflege und demokratische Prozesse:** Nicht anwendbar.

### 3.2 Ergebnis der Klassifizierung

**PalettenAuge AI fällt unter Anhang III Nr. 4 KI-VO (Beschäftigung / Personalmanagement) und ist als Hochrisiko-KI-System einzustufen.**

**Begründung im Einzelnen:**

1. Das System trifft Empfehlungen zur Personaleinsatzplanung, die in der Praxis regelmäßig ohne nennenswerte menschliche Überprüfung übernommen werden (de-facto-Automatisierung).

2. Die Einbeziehung von Gesundheitsdaten (Krankheitstage) in den Algorithmus erhöht das Risiko einer faktischen Diskriminierung gesundheitlich beeinträchtigter Mitarbeiter.

3. Die Leistungshistorie (welche Touren, welche Zeiten, Tempodaten) fließt in eine Art implizites Bewertungssystem ein, das arbeitsrechtlich relevant ist.

4. Im Kontext des Datenschutzvorfalles wurden diese Daten exfiltriert — das zeigt die Sensibilität und die realen Risiken bei Missbrauch.

---

## 4. Pflichten des Betreibers (Frischetrans als Deployer)

Als **Deployer** (Betreiber) eines Hochrisiko-KI-Systems hat Frischetrans nach Art. 26 KI-VO folgende Pflichten:

| Pflicht | Rechtsgrundlage | Fälligkeit | Status |
|---|---|---|---|
| Implementierung technischer und organisatorischer Maßnahmen | Art. 26 Abs. 1 KI-VO | 02.08.2026 | Offen |
| Menschliche Aufsicht (Human Oversight) | Art. 26 Abs. 2 KI-VO | 02.08.2026 | Offen |
| Betriebstagebuch / Protokollierung | Art. 26 Abs. 5 KI-VO | 02.08.2026 | Teilweise (IT-Logs) |
| Information der Arbeitnehmer | Art. 26 Abs. 7 KI-VO | 02.08.2026 | Offen |
| Konsultation des Betriebsrats | BetrVG § 87 Abs. 1 Nr. 6 (Mitbestimmung) | Vor Einsatz / jetzt | Offen |
| Sicherstellung Konformitätserklärung des Anbieters | Art. 26 Abs. 1 i.V.m. Art. 47 KI-VO | 02.08.2026 | Offen |
| Registrierung in EU-Datenbank | Art. 26 Abs. 1 i.V.m. Art. 71 KI-VO | 02.08.2026 | Offen |

### 4.1 Pflichten des Anbieters (DachAuge GmbH als Provider)

Der Anbieter DachAuge GmbH hat als **Provider** nach Art. 16 ff. KI-VO folgende Pflichten:

- Konformitätsbewertung (Art. 43 KI-VO)
- Technische Dokumentation (Anhang IV KI-VO)
- Konformitätserklärung (Art. 47 KI-VO)
- CE-Kennzeichnung (Art. 48 KI-VO)
- Registrierung in der EU-KI-Datenbank (Art. 71 KI-VO)

**Frischetrans muss bei DachAuge die Vorlage dieser Dokumente einfordern.**

---

## 5. Arbeitsrechtliche Dimension (§ 87 BetrVG)

Das Mitbestimmungsrecht des Betriebsrats nach § 87 Abs. 1 Nr. 6 BetrVG (technische Überwachungseinrichtungen) ist eindeutig berührt:

PalettenAuge AI überwacht indirekt das Verhalten und die Leistung der Fahrer (Tourdaten, Tempoverläufe, Standortdaten) und wertet diese für die Dispositionsempfehlung aus. Eine **Betriebsvereinbarung über den Einsatz von PalettenAuge AI** ist erforderlich.

**Empfehlung:** Abschluss einer Betriebsvereinbarung nach § 87 Abs. 1 Nr. 6 BetrVG, die Folgendes regelt:
- Zweck der Datenverarbeitung durch PalettenAuge AI
- Welche Daten fließen ein
- Wie wird sichergestellt, dass die KI-Empfehlungen nur als Entscheidungsunterstützung (nicht als automatische Entscheidung) genutzt werden
- Recht der Mitarbeiter auf Auskunft über sie betreffende Auswertungen
- Aufbewahrungsfristen der Leistungsdaten

---

## 6. Empfehlungen und Handlungsplan

| Maßnahme | Zuständig | Frist |
|---|---|---|
| Anforderung Konformitätsdokumentation bei DachAuge GmbH | RA Drosten / IT | 20.05.2026 |
| Abschluss Betriebsvereinbarung PalettenAuge AI | GF Wallbruck / Betriebsrat | 30.06.2026 |
| Implementierung Human-Oversight-Prozess | IT / Disposition | 31.07.2026 |
| DSGVO-Datenschutzfolgenabschätzung PalettenAuge (Art. 35 DSGVO) | DSB Feilke | 30.06.2026 |
| Schulung Disponenten zu KI-Aufsichtspflichten | HR | 31.07.2026 |
| Registrierung in EU-KI-Datenbank (über DachAuge) | DachAuge / RA Drosten | 01.08.2026 |
| Prüfung: Weiter-Einsatz bis Konformität gesichert? | GF + RA Drosten | 20.05.2026 |

**Kritische Empfehlung:** Bis zur Sicherstellung der vollständigen KI-VO-Konformität sollte der automatisierte Personaleinsatz-Modus von PalettenAuge AI ausgesetzt und nur die Routenoptimierungsfunktion (ohne Personaldaten) genutzt werden.

---

## 7. Bußgeldrisiko

Bei Verstößen gegen die KI-VO drohen Bußgelder nach Art. 99 KI-VO:
- Verwendung eines verbotenen KI-Systems (nicht einschlägig): bis 35 Mio. EUR / 7 % des weltweiten Umsatzes
- Verwendung ohne Konformitätsbewertung (Hochrisiko): bis 15 Mio. EUR / 3 % des weltweiten Umsatzes
- Falsche Angaben gegenüber Behörden: bis 7,5 Mio. EUR / 1 %

Für Frischetrans als KMU sind reduzierte Bußgelder vorgesehen (Art. 99 Abs. 5 KI-VO). Das Risiko besteht aber auch für DachAuge als Provider.
