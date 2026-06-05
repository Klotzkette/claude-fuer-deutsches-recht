---
name: blutprodukte-transfusionsrecht-system-klinik
description: "Blutprodukte Transfusionsrecht System Klinik: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Blutprodukte Transfusionsrecht System Klinik

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Blutprodukte Transfusionsrecht System Klinik** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `blutprodukte-transfusionsrecht-dokumentation` | Blutprodukte Transfusionsrecht Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `compliance-system-klinik-einkauf-forschung-spenden` | Compliance-System Klinik Einkauf Forschung Spenden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR. |
| `datenschutz-krankenhaus-patientenakte-forschung` | Datenschutz im Krankenhaus: DSGVO, BDSG, Landeskrankenhausgesetze, Patientenakte, ePA-Anbindung, Forschungsdaten, Auftragsverarbeitung Cloud/KI, Betroffenenrechte und Datenpannen. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Blutprodukte Transfusionsrecht System Klinik**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `blutprodukte-transfusionsrecht-dokumentation`

**Fokus:** Blutprodukte Transfusionsrecht Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Blutprodukte Transfusionsrecht Dokumentation

## Fachkern: Blutprodukte Transfusionsrecht Dokumentation
- **Spezialgegenstand:** Blutprodukte Transfusionsrecht Dokumentation. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Blutprodukte Transfusionsrecht Dokumentation** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

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

## 2. `compliance-system-klinik-einkauf-forschung-spenden`

**Fokus:** Compliance-System Klinik Einkauf Forschung Spenden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Landeskrankenhausrecht, MD-Prüfregeln, IfSG, MPDG/MDR.

# Compliance-System Klinik Einkauf Forschung Spenden

## Fachkern: Compliance-System Klinik Einkauf Forschung Spenden
- **Spezialgegenstand:** Compliance-System Klinik Einkauf Forschung Spenden. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Compliance-System Klinik Einkauf Forschung Spenden** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

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

## 3. `datenschutz-krankenhaus-patientenakte-forschung`

**Fokus:** Datenschutz im Krankenhaus: DSGVO, BDSG, Landeskrankenhausgesetze, Patientenakte, ePA-Anbindung, Forschungsdaten, Auftragsverarbeitung Cloud/KI, Betroffenenrechte und Datenpannen.

# Datenschutz Krankenhaus Patientenakte Forschung

## Fachkern: Datenschutz Krankenhaus Patientenakte Forschung
- **Spezialgegenstand:** Datenschutz Krankenhaus Patientenakte Forschung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Patientendaten sind besonders schutzwuerdig (Art. 9 DSGVO Gesundheitsdaten). Im Krankenhaus uberlagern sich DSGVO, BDSG, Landeskrankenhausgesetze, § 203 StGB, SGB X, MBO-Aerzte. Sekundaerthemen: ePA-Anbindung, Forschung, KI-Tools, Cloud-Auftragsverarbeitung, Datenpannen-Meldepflicht.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welcher Verarbeitungszweck: Behandlung, Abrechnung, Forschung, Qualitaetssicherung, ePA?
- Liegt Auftragsverarbeitungsvertrag (AVV, Art. 28 DSGVO) vor?
- Wird KI eingesetzt (Diagnoseunterstuetzung, OCR, Spracherkennung)?
- Auskunfts-/Loeschungsbegehren eines Patienten?
- Datenpanne (Verlust, Diebstahl, Fehlversand)?

## Rechtlicher Rahmen
- **DSGVO Art. 5, 6, 9, 12-22, 32, 33, 34** Grundprinzipien, Gesundheitsdaten, Betroffenenrechte, TOM, Meldepflicht.
- **BDSG §§ 22, 23** Verarbeitung Gesundheitsdaten.
- **Landeskrankenhausgesetze** patientendatenschutz (z. B. § 9 KHG NRW).
- **SGB X §§ 67, 76 ff.** Sozialdatenschutz, Datenweitergabe.
- **§ 203 StGB** strafrechtliche Schweigepflicht.
- **MBO-Aerzte § 9** aerztliche Schweigepflicht.
- **PatientendatenSchutzG (PDSG)** ePA-Anbindung.

## / Schritt fuer Schritt
1. **Rechtsgrundlage je Verarbeitung:** Art. 6/9 DSGVO; Behandlung Art. 9 Abs. 2 lit. h; Forschung Art. 9 Abs. 2 lit. j + § 27 BDSG; Abrechnung gesetzliche Pflicht.
2. **Patienteninformation Art. 13/14 DSGVO:** Verstaendlich, schriftlich, fuer jeden Hauptzweck.
3. **Einwilligungen separat:** Behandlung (gesetzlich nicht erforderlich), Forschung (i. d. R. erforderlich), Werbung/Sekundaerzweck.
4. **AVV bei Auftragsverarbeitung** (Cloud, IT, KI-Anbieter): Inhalt § 28 DSGVO; technische und organisatorische Massnahmen.
5. **Patientenakte/Einsichtsrecht:** §§ 630g BGB, Art. 15 DSGVO; unverzueglich, ggf. Gebuehr fuer Kopien.
6. **Forschungsprojekt:** Konzept, Ethikkommission, DSGVO-Pruefung, Pseudonymisierung/Anonymisierung.
7. **Datenpanne:** Innerhalb 72h Meldung Aufsicht (Art. 33), bei hohem Risiko Betroffene informieren (Art. 34).

## Trade-off-Matrix

| Vorhaben | Rechtsgrundlage | Risiko |
|---|---|---|
| Behandlung | Art. 9 Abs. 2 lit. h DSGVO | niedrig, Information noetig |
| Abrechnung | gesetzliche Pflicht | Sozialdatenschutz pruefen |
| Qualitaetssicherung | Art. 9 Abs. 2 lit. h/i | Pseudonymisierung empfohlen |
| Forschung | Einwilligung / § 27 BDSG | Ethikkommission, DSFA |
| KI-Diagnose | Art. 6/9, ggf. DSFA | sektorale Risiken |
| Cloud | AVV + Art. 44 ff. DSGVO | Drittlandsthematik |

## Praxistipps
- Patientendatenschutz hat zwei Schutzebenen: DSGVO/BDSG zivil-/oeffentlichrechtlich; § 203 StGB strafrechtlich.
- AVV im Cloud-Kontext muss Subunternehmer, Loeschpflichten, Audit-Rechte enthalten.
- ePA-Anbindung verlangt PDSG-konforme Schnittstellen.
- KI-Anwendungen mit Patientendaten: Datenschutz-Folgenabschaetzung (DSFA, Art. 35).
- Forschungsdaten meist pseudonymisiert; vollanonymisierte Daten fallen aus DSGVO heraus.
- Datenpanne-Meldung 72h ist Frist, kein Soll.

## Mustertexte
**Patienteninformation Art. 13 DSGVO (Auszug):**
> Verantwortlich: [Klinik]. Zwecke: Behandlung, Abrechnung, Qualitaetssicherung. Rechtsgrundlagen: Art. 9 Abs. 2 lit. h DSGVO; gesetzliche Pflichten. Empfaenger: Kassen, MD, Aufsichtsbehoerden. Rechte: Auskunft, Berichtigung, Loeschung (eingeschraenkt), Beschwerde. Datenschutzbeauftragter: …

**Datenpanne-Meldung (Skizze):**
> An Landesdatenschutzbeauftragten. Wir melden gemaess Art. 33 DSGVO eine Datenpanne. Ereignis: [Datum/Zeit]. Betroffene: [Anzahl]. Daten: [Kategorien]. Ursache: …. Massnahmen: …. Ansprechpartner: …

## Typische Fehler
- AVV fehlt oder ist unvollstaendig.
- Patientendaten in unverschluesselten E-Mails an Externe.
- Forschung ohne Ethik-/Datenschutzfreigabe.
- Datenpannen-Frist 72h versaeumt.
- KI-Tools ohne DSFA und ohne Pseudonymisierungspruefung.

## Querverweise
- `patientenrechte-behandlungsvertrag-aufklaerung`
- `dokumentation-aufbewahrung-beweislast`
- `forschung-studien-ethikkommission-datenschutz`
- `krankenhausdigitalisierung-khzg-it-sicherheit`
- `kritis-krankenhaus-bsi-gesetz-nis2`
- `dora-und-it-dienstleister-soweit-einschlaegig`

## Quellen Stand 06/2026
- DSGVO.
- BDSG §§ 22, 23, 27.
- Landeskrankenhausgesetze 16 Laender (Live-Check Landesministerien).
- SGB X §§ 67, 76.
- StGB § 203.
- PatientendatenSchutzG (PDSG) zur ePA.
- BfDI- und Landesdatenschutzaufsicht-Hinweise (Live-Check bfdi.bund.de).
- BGH, staend. Rspr. zur aerztlichen Schweigepflicht.
