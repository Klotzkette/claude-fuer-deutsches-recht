---
name: retaxationsabwehr-nullretax
description: "Retaxationsabwehr Nullretax: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Retaxationsabwehr Nullretax

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Retaxationsabwehr Nullretax** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `retaxationsabwehr-nullretax-risiko` | Retaxationsabwehr Nullretax Risiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `rezeptsammelstelle-botendienst-versandhandel` | Rezeptsammelstelle Botendienst Versandhandel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `rezeptur-plausibilitaetspruefung-herstellungsanweisung` | Rezeptur Plausibilitätsprüfung Herstellungsanweisung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Retaxationsabwehr Nullretax**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `retaxationsabwehr-nullretax-risiko`

**Fokus:** Retaxationsabwehr Nullretax Risiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Retaxationsabwehr Nullretax Risiko

## Fachkern: Retaxationsabwehr Nullretax Risiko
- **Spezialgegenstand:** Retaxationsabwehr Nullretax Risiko. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Retaxation: Krankenkasse verweigert ganz oder teilweise die Erstattung einer abgegebenen Arzneimittelpackung wegen formaler oder materieller Mängel. "Null-Retax" bedeutet komplette Absetzung — Apotheke erhält keinen Cent für das abgegebene Medikament, das aber bereits ausgehändigt wurde. Dieser Skill behandelt Prävention, fristgerechten Widerspruch, Schiedsverfahren und Sondervereinbarungen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Retaxationsbescheid Krankenkasse ist eingegangen.
- Häufung von Retaxationen — Strukturproblem in Workflow.
- Beanstandung wegen Substitution, Rabattvertrag, Formfehler.
- Streit über Eintrittsdatum Verschreibungspflicht im E-Rezept.
- Schiedsstellenverfahren bei Krankenkassen-Apotheken-Streit.

Eingaben:
- Retaxbescheid mit konkreter Begründung.
- Originalrezept oder E-Rezept-Token-Abruf, ggf. PDF.
- Lieferschein-Daten Grosshandel, Charge.
- Beratungs- und Plausibilitätsdokumentation.
- Substitutionsausschluss-Liste und Rabattvertrag.

## Rechtlicher Rahmen

- **§ 129 SGB V:** Rahmenvertrag, Abrechnung und Retaxation.
- **§ 17 ApBetrO:** Abgabeordnung.
- **§ 8 SGB V:** Versicherungsverhältnis.
- **Rahmenvertrag GKV-Spitzenverband / DAV** (Stand vom Anwender zu verifizieren) — § 7 zur Retaxation, § 17 zur Schiedsstelle.
- **§ 12 SGB V:** Wirtschaftlichkeitsgebot.
- **BSG, staend. Rspr.:** Null-Retax bei reinen Formfehlern (rückläufige Praxis durch Reformbemühungen 2024–2026), Pharmazeutische Bedenken.
- **§ 109 SGG:** Sozialgerichtsweg.

## / Schritt für Schritt

1. **Eingang prüfen:** Datum, Frist Widerspruch (regelmässig vier Wochen, vom Anwender zu verifizieren).
2. **Begründung der Krankenkasse einordnen:**
 - Formaler Mangel (z. B. Datum, Unterschrift, Aut-idem-Kreuz-Übersehen)
 - Substitutionsverstoss (Rabattvertrag)
 - Mengenüberschreitung
 - Doppelabgabe
 - Pharmazeutische Bedenken nicht dokumentiert
3. **Original-Dokumentation zusammentragen:** Rezept-Token, Lieferschein, Plausibilitäts-Eintrag, Beratungsprotokoll, Charge.
4. **Widerspruch verfassen:** Konkret auf den Vorhalt eingehen; Belege als Anlage; ggf. § 17 Abs. 5 ApBetrO und § 129 Abs. 1a SGB V (Pharmazeutische Bedenken).
5. **Bei Substitution:** Substitutionsausschlussliste prüfen — war Wirkstoff nicht austauschbar?
6. **Schiedsstellenverfahren:** Bei wiederholten Streitigkeiten Schiedsstelle nach § 129 Abs. 8 SGB V anrufen.
7. **Sozialgericht:** Letzter Weg — bei grundsätzlichen Fragen.
8. **Prävention:** SOP überarbeiten, Schulung Personal.

## Trade-off-Matrix

| Retax-Grund | Erfolgsaussicht Widerspruch | Erforderliche Doku | Hinweis |
|---|---|---|---|
| Aut-idem-Kreuz übersehen, falsches Präparat | gering | — | Schaden tragen |
| Substitutionsausschlussliste | hoch | Rezept + Liste | Bedenken dokumentieren |
| Pharmazeutische Bedenken nicht dokumentiert | gering, wenn keine Doku | nachträgliche Doku nur eingeschränkt | sofortige Doku Pflicht |
| Mengenüberschreitung | mittel | ärztliche Erklärung | Rücksprache Arzt-Doku |
| Doppelabgabe E-Rezept | hoch | TI-Logs | TI-Störungsprotokoll |
| Formaler Fehler ohne Substanzschaden | mittel-hoch nach Reform 2024 | Belege | Null-Retax bei reinen Formfehlern verfassungsrechtlich umstritten |

## Praxistipps

- Fristen sind harte Ausschlussfristen — Frist verstreichen lassen heisst Erlös endgültig verlieren.
- Sammeleinwendungen an Krankenkasse einreichen — gleichartige Retaxationen gemeinsam widerlegen.
- BGH/BSG-Linie zu Null-Retax bei rein formalen Mängeln zugunsten Apotheken — argumentativ ausschöpfen.
- Nach erfolgreichem Widerspruch: Schulung Personal mit konkreten Beispielen — Prävention.
- Versicherung gegen Retax-Schäden gibt es nicht; einziges Mittel ist Workflow-Qualität.

## Mustertexte

### Widerspruch gegen Retaxbescheid (Auszug)
"Sehr geehrte Damen und Herren, gegen den Retaxbescheid vom [Datum] (Aktenzeichen [...]) legen wir frist- und formgerecht Widerspruch ein. Begründung: 1. Die Abgabe am [Datum] erfolgte gemäss vorliegendem E-Rezept-Token [Nummer] (Token-Abruf Anlage 1). 2. Eine pharmazeutische Plausibilitätsprüfung wurde durchgeführt und unter [Vorgangs-Nr.] dokumentiert (Anlage 2). 3. Die Substitution erfolgte gemäss Rabattvertrag mit [Krankenkasse]; das vorhandene Aut-idem-Kreuz wurde respektiert (vgl. Rezept-Scan Anlage 3). Wir bitten um vollumfängliche Stornierung der Retax und Erstattung des einbehaltenen Betrages in Höhe von [EUR] binnen [Frist]. Bei Bedarf stehen wir für Rückfragen unter [Kontakt] zur Verfügung."

### Antrag Schiedsstelle § 129 Abs. 8 SGB V (Auszug)
"Hiermit beantragen wir die Anrufung der Schiedsstelle nach § 129 Abs. 8 SGB V im Streit mit der [Krankenkasse] über die Retaxationen vom [Daten, AZ]. Streitwert: [EUR]. Sachverhalt: [...]. Anliegen: Feststellung der Unwirksamkeit der Retaxationen, Erstattung der einbehaltenen Beträge."

## Typische Fehler

- Frist verpasst — Erlös unwiederbringlich verloren.
- Pauschaler Widerspruch ohne Belege — Krankenkasse weist ohne Substanzprüfung zurück.
- Pharmazeutische Bedenken erst im Widerspruchsverfahren konstruiert — nicht glaubwürdig.
- Substitutionsausschlussliste nicht aktuell — Substitution falsch beurteilt.
- Doppelabgabe E-Rezept nicht durch TI-Logs widerlegt.

## Querverweise

- `substitution-rabattvertrag-aut-idem` (Substitution)
- `rechnung-retaxation-krankenkasse` (Abrechnungsworkflow)
- `schiedsstellen-krankenkassen-apotheke` (Schiedsstellenverfahren)
- `lieferengpaesse-austausch-dokumentation` (Engpass-Austausch)
- `arzneimittelabgabe-verschreibungspflicht` (Abgabevorgang)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Logs)

## Quellen Stand 06/2026

- SGB V §§ 8, 12, 129.
- Rahmenvertrag § 129 SGB V mit Anlagen (vom Anwender zu verifizieren — Aktualität).
- BSG, staend. Rspr. zur Null-Retax und Pharmazeutische Bedenken.
- DAV-Mitteilungen zu Retaxationen.
- BMG-Reformbemühungen zur Retax-Begrenzung (Stand vom Anwender zu verifizieren).

## 2. `rezeptsammelstelle-botendienst-versandhandel`

**Fokus:** Rezeptsammelstelle Botendienst Versandhandel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Rezeptsammelstelle Botendienst Versandhandel

## Fachkern: Rezeptsammelstelle Botendienst Versandhandel
- **Spezialgegenstand:** Rezeptsammelstelle Botendienst Versandhandel. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Rezeptsammelstelle Botendienst Versandhandel** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `rezeptur-plausibilitaetspruefung-herstellungsanweisung`

**Fokus:** Rezeptur Plausibilitätsprüfung Herstellungsanweisung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Rezeptur Plausibilitätsprüfung Herstellungsanweisung

## Fachkern: Rezeptur Plausibilitätsprüfung Herstellungsanweisung
- **Spezialgegenstand:** Rezeptur Plausibilitätsprüfung Herstellungsanweisung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Individualrezeptur: Apotheke stellt im Einzelfall auf ärztliche Verschreibung ein Arzneimittel her (z. B. Salbe mit Wirkstoff X in Konzentration Y, Saft für Kind, Kapseln nicht zugelassener Wirkstoffstärke). Pflicht ist eine **Plausibilitätsprüfung** (§ 7 ApBetrO) und eine schriftliche **Herstellungsanweisung** mit Dokumentation. Bei Fehlern droht Patientenschaden, Anhörung, Haftung (§§ 280, 823, 84 AMG-analog) und Aufsichtsmassnahmen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Individualrezeptur erstmals geplant, Schritt-für-Schritt-zu prüfen.
- Schaden eingetreten — Patient meldet Nebenwirkung; Apotheke prüft Verantwortung.
- Aufsicht beanstandet fehlende Plausibilitätsprüfung.
- Schulung der pharmazeutischen Mitarbeiter zur Rezeptur.

Eingaben:
- Verschreibung mit Wirkstoff, Konzentration, Trägermedium, Menge.
- Apothekenrezeptur-Software / NRF (Neues Rezeptur-Formularium) / DAC (Deutscher Arzneimittel-Codex).
- Ausgangsstoff-Prüfprotokoll, Lieferantennachweis.
- Plausibilitätsformular, Herstellungsanweisung, Herstellungsprotokoll.

## Rechtlicher Rahmen

- **§ 7 ApBetrO:** Pflicht zur Plausibilitätsprüfung **vor** Herstellung. Geprüft werden: Wirkstoff, Konzentration, Galenik, Kombination, Indikation, Risiken.
- **§ 8 ApBetrO:** Schriftliche Herstellungsanweisung; Pflicht zur Prüfung der Ausgangsstoffe.
- **§ 14 ApBetrO:** Dokumentation Herstellung — Herstellungsprotokoll mit Charge, Datum, Bearbeiter.
- **§ 21 ApBetrO:** QMS.
- **§ 11 ApBetrO:** Beratung Patient.
- **§ 21 AMG:** Zulassungspflicht — Rezeptur ist ausgenommen (Einzelfertigung).
- **AMVV** für die Verschreibung.
- **NRF / DAC** als anerkannte Standards (vom Anwender zu verifizieren — Aktualität).
- BGH, staend. Rspr. zur Apothekenhaftung bei Rezepturfehlern.

## / Schritt für Schritt

1. **Plausibilitätsprüfung VOR Herstellung:**
 - Wirkstoff vorhanden, geeignet, korrekt dosiert für Indikation?
 - Konzentration plausibel für angegebene Indikation? (z. B. Cortison-Salben — Stärken)
 - Galenik kompatibel mit Trägermedium?
 - Kombinationen verträglich (Hilfsstoffe, pH, Hydroskopie)?
 - Patientenfaktoren: Alter, Allergie, Schwangerschaft?
 - Bei Bedenken: Rücksprache mit Arzt — Dokumentation.
2. **Herstellungsanweisung:** Schriftlich, mit Wirkstoff, Hilfsstoffen, Gerätschaft, Reihenfolge, Endkontrolle.
3. **Ausgangsstoffe prüfen:** Identitätsprüfung (eigene oder zertifiziert), Chargenprüfung, Verfall.
4. **Herstellung:** Reinraum-Bedingungen, Personalhygiene, Geräte gereinigt.
5. **Endkontrolle:** Visuell, Gewicht, ggf. pH/Konsistenz.
6. **Etikettierung:** Apothekenname, Patient, Wirkstoff, Konzentration, Verfall, Lagerhinweis, Anwendungshinweis.
7. **Herstellungsprotokoll:** Datum, Bearbeiter, Charge, Identifikationsnummer.
8. **Beratung Patient:** Anwendung, Aufbewahrung, Verfall, Risiken.
9. **Aufbewahrung Dokumentation:** Drei Jahre, bei BtM-Rezeptur zehn Jahre.

## Trade-off-Matrix

| Rezeptur-Typ | Plausibilitätsprüfung | Herstellungsanweisung | Endkontrolle |
|---|---|---|---|
| NRF-Standardrezeptur | vereinfacht (Verweis NRF) | NRF-Anleitung | Standard |
| Individuelle Salbe nach Arztwunsch | umfassend | individuell | sensorisch + Gewicht |
| Kapseln mit Wirkstoff < Zulassung | umfassend, ggf. Rücksprache | individuell | Wirkstoffmenge pro Kapsel |
| Kinderrezeptur (Saft) | umfassend, alters-/gewichtsadaptiert | individuell | pH, Geschmack, Stabilität |
| Sterilrezeptur Augentropfen | sehr hoch (Reinraum) | streng nach SOP | Sterilkontrolle |

## Praxistipps

- Bei Zweifel an Plausibilität — Rücksprache Arzt **schriftlich** dokumentieren. Telefonat allein bietet keinen Beweis.
- NRF/DAC-Standardrezepturen wann immer möglich verwenden — geprüfte Sicherheit + Vereinfachung Doku.
- Software-Tools für Plausibilität (DAP, ABDA-DB) nutzen — reduzieren menschliche Fehler erheblich.
- Bei Schaden: sofortige Untersuchung, Dokumentation aller Schritte, Versicherung informieren.
- Auszubildende dürfen Rezeptur unter Apothekeraufsicht; Letztverantwortung verbleibt bei Apotheker:in.

## Mustertexte

### Plausibilitätsprüfungs-Formular (Auszug)
"Datum / Rezept-Nr.: [...] | Patient: [Initialen, Geb.-Datum] | Verordnung: [Wirkstoff, Konzentration, Hilfsstoffe, Menge] | Prüfung: 1. Indikation [ja/nein/Rücksprache]; 2. Konzentration plausibel [ja/nein]; 3. Galenik kompatibel [ja/nein]; 4. Hilfsstoff-Verträglichkeit [ja/nein]; 5. Patientenfaktoren [Allergie/Alter/Schwangerschaft] | Rücksprache Arzt: [ja/nein, Datum, Inhalt] | Plausibilität bestätigt durch: [Name Apotheker:in] | Freigabe zur Herstellung: [Datum]"

### Herstellungsanweisung (Auszug)
"Rezeptur-Nr.: [...] | NRF/DAC-Referenz: [...] / Individualrezeptur | Wirkstoff: [Name, Menge] | Hilfsstoffe: [Liste mit Mengen] | Gerätschaft: [Liste] | Reihenfolge: 1. ... 2. ... 3. ... | Mischtechnik: [Salbenmühle, Fantaschale, Magnetrührer] | Endprüfung: [visuell/Gewicht/pH/Konsistenz] | Etikettierung: [Wortlaut] | Verfall: [Datum, basierend auf Stabilitätsstudien]"

## Typische Fehler

- Keine Plausibilitätsprüfung dokumentiert, "haben wir geprüft" reicht nicht.
- Identitätsprüfung Ausgangsstoff nur durch Zertifikat-Sichtung — die ApBetrO verlangt eigene Identitätsprüfung.
- Herstellungsprotokoll wird erst Tage später ausgefüllt — Chargennummer nicht mehr nachvollziehbar.
- Hilfsstoff allergisch beim Patient, nicht im Plausibilitätscheck erkannt.
- Verfallsdatum auf Etikett zu generös; eigene Stabilitätsdaten fehlen.

## Querverweise

- `arzneimittelpruefung-ausgangsstoffe-pruefprotokoll` (Eingangsprüfung)
- `defektur-100er-regel-qualitaetssicherung` (Serienherstellung)
- `apothekenbetriebsordnung-grundpflichten` (Rahmen)
- `qualitaetsmanagement-qms-sops` (SOP)
- `raeume-ausstattung-rezeptur-defektur-labor` (Räume/Geräte)
- `btm-rezeptur-amts-schnellcheck` (BtM-Rezeptur)

## Quellen Stand 06/2026

- ApBetrO §§ 7, 8, 11, 14, 21.
- AMG § 21.
- NRF (Neues Rezeptur-Formularium) und DAC (Deutscher Arzneimittel-Codex), Verlag GOVI; Aktualität vom Anwender zu verifizieren.
- ABDA-Leitlinien zur Rezeptur (vom Anwender zu verifizieren).
- BGH, staend. Rspr. zur Apothekenhaftung bei Herstellungsfehlern.
- Landesaufsicht-Merkblätter zur Rezeptur (vom Anwender zu verifizieren).
