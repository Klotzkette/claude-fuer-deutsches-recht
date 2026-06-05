---
name: e-rezept-erlaubnis-filialverbund
description: "E Rezept Erlaubnis Filialverbund: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# E Rezept Erlaubnis Filialverbund

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **E Rezept Erlaubnis Filialverbund** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `e-rezept-ti-gematik-apothekenprozess` | E-Rezept TI Gematik Apothekenprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `erlaubnis-filialverbund-routing` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Erlaubnis Filialverbund Routing. |
| `filialapotheke-hauptapotheke-leitung-vertretung` | Filialapotheke Hauptapotheke Leitung Vertretung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **E Rezept Erlaubnis Filialverbund**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `e-rezept-ti-gematik-apothekenprozess`

**Fokus:** E-Rezept TI Gematik Apothekenprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# E-Rezept TI Gematik Apothekenprozess

## Fachkern: E-Rezept TI Gematik Apothekenprozess
- **Spezialgegenstand:** E-Rezept TI Gematik Apothekenprozess. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Seit dem 01.01.2024 ist das E-Rezept für apothekenpflichtige Fertigarzneimittel in der GKV-Versorgung verpflichtend (§ 360 SGB V). Der Skill behandelt: Einlösewege (eGK, Token-Ausdruck, App), TI-Konnektivität, Signaturprüfung, Ersatzverfahren bei Störung, Datenschutz, Apothekenpflichten gegenüber Gematik, Krankenkasse und Aufsicht. BtM- und T-Rezept sind bisher noch papierbasiert (Stand zu verifizieren).

## Wann dieses Modul hilft / Kaltstart-Fragen

- E-Rezept lässt sich nicht einlösen — TI-Störung oder Defekt der eGK.
- Retax wegen E-Rezept-Formfehler oder Doppelabgabe.
- Anfrage Aufsicht zur TI-Konformität.
- Schulung neuer Mitarbeiter zum E-Rezept-Workflow.
- Datenschutz: Patient verlangt Auskunft über E-Rezept-Verarbeitung.

Eingaben:
- E-Rezept-Token (QR-Code-Ausdruck oder über App), eGK des Patienten.
- Apothekenkartenlesegerät, Konnektor, gSMC-K, HBA.
- Apotheken-Warenwirtschaftssystem mit TI-Integration.
- TI-Störungsmeldung (sofern vorhanden) Gematik / IT-Dienstleister.

## Rechtlicher Rahmen

- **§ 360 SGB V:** E-Rezept-Pflicht ab 01.01.2024 für apothekenpflichtige Fertigarzneimittel zu Lasten GKV.
- **§§ 311 ff. SGB V:** Telematikinfrastruktur (TI), Gematik als Verantwortliche.
- **§ 312 SGB V:** Verarbeitung medizinischer Daten in der TI.
- **Gematik-Spezifikationen** (TI-Spec): Konnektor, eGK, HBA, gSMC-K, E-Rezept-Fachdienst.
- **DSGVO Art. 9:** Gesundheitsdaten — strengere Rechtfertigung erforderlich.
- **§ 7 ApBetrO:** Pharmazeutische Letztverantwortung; bei TI-Störung kein Ersatzweg ausserhalb der Regelungen.
- **§ 129 SGB V:** Rahmenvertrag, Retaxation bei formalen Fehlern.

## / Schritt für Schritt

1. **Einlösung:** Patient legt eGK ein, scannt Token (App), gibt Ausdruck mit QR-Code. Apothekensoftware ruft Rezept vom Fachdienst ab.
2. **Signaturprüfung:** Qualifizierte elektronische Signatur des Arztes wird automatisch verifiziert.
3. **Plausibilitätsprüfung** (analog Papierrezept, siehe `arzneimittelabgabe-verschreibungspflicht`).
4. **Aut-idem / Rabattvertrag** (siehe `substitution-rabattvertrag-aut-idem`).
5. **Aushändigung + Quittung:** Quittung über E-Rezept-Fachdienst zurück.
6. **Dokumentation:** Im Warenwirtschaftssystem; Token wird nach Einlösung im Fachdienst gesperrt.
7. **TI-Störung — Ersatzverfahren:** Bei Ausfall TI-Konnektor folgt nach Gematik-Vorgabe das "Ersatzverfahren" — Patient erhält ggf. Papierausdruck, Apotheke dokumentiert Ausfallzeitfenster. Bei länger andauerndem Ausfall: Rücksprache Krankenkasse zur Retaxprävention.
8. **Datenschutz:** Patient hat Auskunfts- und Löschanspruch (Art. 15, 17 DSGVO). E-Rezept-Token-Daten unterliegen Gesundheitsdatenschutz.

## Trade-off-Matrix

| Einlöseweg | Technischer Aufwand | Datenschutz | Verfügbarkeit |
|---|---|---|---|
| eGK direkt am Lesegerät | gering | strikt geschützt | nur in Apotheke |
| Token-Ausdruck | sehr gering | OK | überall |
| App (gematik) | mittel | OK | Smartphone notwendig |
| Vorabreservierung Online-Apotheke | hoch | DSGVO-pflichtig | Patient bestimmt |

## Praxistipps

- TI-Konnektor und HBA-Karte regelmässig aktualisieren — Zertifikate laufen ab. Verlängerung rechtzeitig planen.
- Bei TI-Ausfall: Tagesprotokoll mit Beginn/Ende der Störung und betroffenen Vorgängen. Krankenkasse nachweisen können.
- Patient-App: Apotheke benötigt keinen Zugriff auf personenbezogene App-Daten. Token-Scan reicht.
- Datenschutzdokumentation: TI-Verarbeitung im Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO) anlegen.
- BtM und T-Rezept bleiben aktuell papierbasiert; E-BtM ist angekündigt — Anwender muss aktuellen Stand verifizieren.

## Mustertexte

### Dokumentation TI-Ausfall (Auszug)
"TI-Störung am [Datum, Beginn ... Ende]. Apotheke konnte E-Rezept-Einlösung nicht durchführen. Patienten wurden gebeten, Token-Ausdruck mitzubringen / Folge-Termin zu vereinbaren. Notfallabgaben nach § 4 AMVV erfolgten in [N] Fällen; Folgerezepte werden eingefordert. Störung wurde an IT-Dienstleister [Name] um [Uhrzeit] gemeldet, Ticket-Nummer [X]."

### Auskunft an Patient nach Art. 15 DSGVO (Auszug)
"Sehr geehrte:r Frau/Herr [Patient:in], hiermit erhalten Sie auf Ihren Antrag vom [Datum] Auskunft zu den über Sie in unserer Apotheke gespeicherten Daten: 1. E-Rezept-Abrufdaten im Zeitraum [...], 2. abgegebene Arzneimittel und Beratung, 3. Speicherdauer und Rechtsgrundlage (§ 312 SGB V, Art. 9 Abs. 2 lit. h DSGVO). Eine Datenkopie ist beigefügt (Anlage [Nr.])."

## Typische Fehler

- Papierrezept gelangt nach gestelltem E-Rezept zur Einlösung — Doppelabgabe, Retax.
- Apotheke löst Rezept zu früh ein (Pre-Lock); System lässt Patient nicht mehr wechseln — DSGVO- und Wettbewerbsproblem.
- TI-Störung nicht dokumentiert; Krankenkasse retaxiert wegen "ungültiger" Abgabe.
- HBA-Zertifikat abgelaufen — Apotheker:in kann keine eigenen Quittungen signieren.
- Patient erteilt App-Zustimmung zur "Vorabreservierung" bei einer bestimmten Versandapotheke; lokale Apotheke fängt Patient nicht ab — Wettbewerbsfrage.

## Querverweise

- `arzneimittelabgabe-verschreibungspflicht` (Plausibilitätsprüfung)
- `versandhandel-und-e-rezept-intake` (Versandapotheken-E-Rezept)
- `datenschutz-in-apotheke-gesundheitsdaten` (DSGVO-Tiefe)
- `digitale-plattformen-marktplatz-apothekenrecht` (Plattformfragen)
- `retaxationsabwehr-nullretax-risiko` (Retax bei E-Rezept-Mängeln)
- `securpharm-faelschungsschutz` (Verifikation Fertigarzneimittel)

## Quellen Stand 06/2026

- SGB V §§ 311, 312, 360 — aktueller Stand im BMG-Veröffentlichungsverzeichnis.
- Gematik-Spezifikationen TI-Konnektor und E-Rezept-Fachdienst (vom Anwender zu verifizieren — Versionsstand).
- BfArM und BSI-Hinweise zur TI-Sicherheit.
- DSGVO Art. 9, 30; BDSG-neu §§ 22, 26 (vom Anwender zu verifizieren — laufende Anpassungen).
- ABDA-Rundschreiben zur E-Rezept-Praxis (vom Anwender zu verifizieren).

## 2. `erlaubnis-filialverbund-routing`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Erlaubnis Filialverbund Routing.

# Erlaubnis Filialverbund Routing

## Fachkern: Erlaubnis Filialverbund Routing
- **Spezialgegenstand:** Erlaubnis Filialverbund Routing. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Erlaubnis Filialverbund Routing** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

## Startfragen
- Was soll sofort entstehen: Kurztriage, Aktenplan, Fragenliste, Memo, Schriftsatz, Vertrag, Formular oder Mandantenbrief?
- Wo drohen Fristen, Formerfordernisse, Bußgelder, Gebührennachteile, Verfahrensfehler oder irreversible Schritte?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 3. `filialapotheke-hauptapotheke-leitung-vertretung`

**Fokus:** Filialapotheke Hauptapotheke Leitung Vertretung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Filialapotheke Hauptapotheke Leitung Vertretung

## Fachkern: Filialapotheke Hauptapotheke Leitung Vertretung
- **Spezialgegenstand:** Filialapotheke Hauptapotheke Leitung Vertretung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Filialapotheke Hauptapotheke Leitung Vertretung** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
