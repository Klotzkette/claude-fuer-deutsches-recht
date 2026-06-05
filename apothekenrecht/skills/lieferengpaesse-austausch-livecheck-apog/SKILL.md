---
name: lieferengpaesse-austausch-livecheck-apog
description: "Lieferengpaesse Austausch Livecheck Apog: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lieferengpaesse Austausch Livecheck Apog

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lieferengpaesse Austausch Livecheck Apog** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lieferengpaesse-austausch-dokumentation` | Lieferengpässe Austausch Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `livecheck-apog-apbetro-amg` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck ApoG ApBetrO AMG. |
| `notfallkontrazeption-beratung` | Notfallkontrazeption Beratung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Lieferengpaesse Austausch Livecheck Apog**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lieferengpaesse-austausch-dokumentation`

**Fokus:** Lieferengpässe Austausch Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Lieferengpässe Austausch Dokumentation

## Fachkern: Lieferengpässe Austausch Dokumentation
- **Spezialgegenstand:** Lieferengpässe Austausch Dokumentation. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Lieferengpässe bei rezeptpflichtigen oder apothekenpflichtigen Arzneimitteln treten häufig auf — Hersteller-Probleme, Marktrückzug, Brexit-Effekte, Sanktionen. Apotheken können nach § 17 Abs. 5 ApBetrO und gesonderten Vereinbarungen (§ 129 SGB V) gleichwertige Präparate austauschen. Dokumentation entscheidet über Retax-Sicherheit. ALBVVG (Arzneimittel-Lieferengpassbekämpfungs- und Versorgungsverbesserungsgesetz 2023) hat den Apotheken erweiterten Spielraum eingeräumt (vom Anwender zu verifizieren — Aktualität).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Patient bringt Rezept, das verordnete Präparat ist nicht lieferbar.
- Bundesweiter Engpass bei Antibiotikum oder Kinder-Fiebersaft.
- Krankenkasse retaxiert, weil Austausch nicht ausreichend dokumentiert.
- ALBVVG-Sondervorschriften greifen — Apotheke unsicher über zulässige Wirkstoff-/Packungsgrösse-Variation.
- Engpass-Datenbank BfArM prüfen.

Eingaben:
- Rezept / E-Rezept-Token.
- Anfrage Grosshandel mit Bestätigung Nichtverfügbarkeit.
- BfArM-Engpassliste oder ABDA-Datenbank.
- Patientendaten (Alter, Indikation).
- Substitutionsausschlussliste.

## Rechtlicher Rahmen

- **§ 52a AMG, § 79 AMG:** Lieferpflicht, Versorgungsmangel.
- **ALBVVG** (Arzneimittel-Lieferengpassbekämpfungs- und Versorgungsverbesserungsgesetz, 2023): erweiterte Substitutionsbefugnis bei Engpass.
- **§ 129 Abs. 2a SGB V:** Sondervereinbarungen bei Engpass.
- **§ 17 Abs. 5 ApBetrO:** Pharmazeutische Sorgfaltspflicht.
- **AMVV** für die Verschreibung.
- **§ 4 AMVV:** Notfallabgabe.
- BfArM Engpassmeldungen (Pflicht der Hersteller nach § 52b AMG).
- BSG, staend. Rspr. zu Retaxation bei Engpass-Austausch.

## / Schritt für Schritt

1. **Verfügbarkeit prüfen:** Grosshandel-Anfrage, ABDA-Datenbank, BfArM-Engpassliste.
2. **Falls nicht verfügbar — Austauschpfade:**
 a. **ALBVVG-Variation** (vom Anwender zu verifizieren): andere Packungsgrösse, andere Wirkstoffstärke unter Anpassung der Menge, gleicher Wirkstoff. Kein Rückgriff zum Arzt erforderlich, aber Dokumentation.
 b. **Substitution wirkstoffgleich** wie bei Rabattvertrag, ggf. mit Pharmazeutische Bedenken.
 c. **Rücksprache Arzt** bei wirkstofflich abweichendem Austausch — schriftlich dokumentieren.
 d. **Notfallabgabe** § 4 AMVV bei akutem Bedarf, kleinste Packung.
3. **Beratung Patient:** Erklärung Austausch, Wirkstoff, Anwendung.
4. **Dokumentation:**
 - Original-Verordnung.
 - Begründung für Austausch (Engpass, BfArM-Listen-Eintrag).
 - Ausgetauschtes Präparat mit PZN und Stärke.
 - Datum, Apotheker:in, Beratung.
5. **Krankenkasse-Hinweis:** Bei E-Rezept-Abrechnung Austauschgrund-Code; Retax-Sicherheit erhöhen.

## Trade-off-Matrix

| Variante | Wirkstoff | Stärke | Packungsgrösse | Rücksprache Arzt | Risiko |
|---|---|---|---|---|---|
| ALBVVG-Variation | gleich | ggf. unterschiedlich | ggf. unterschiedlich | nein | gering bei Doku |
| Substitution wirkstoffgleich | gleich | gleich | gleich | nein | gering |
| Wirkstoffklassen-Austausch | abweichend | — | — | ja, schriftlich | mittel-hoch |
| Importpräparat § 73 III AMG | gleich (im Ausland) | ggf. abweichend | — | ja | mittel |
| Notfall § 4 AMVV | — | — | kleinste Packung | nein | gering bei Indikation |

## Praxistipps

- BfArM-Engpassliste tagesaktuell abrufen — wer übersehen hat, dass Präparat als "Engpass" gelistet ist, dem fehlt der Rechtfertigungsgrund für Variation.
- ALBVVG-Variation dokumentationspflichtig — ohne Doku-Eintrag retaxgefährdet.
- Bei Kinder-Fiebersaft und Antibiotika: Patientenkommunikation aktiv, da häufige Verärgerung.
- Telefonate mit Praxis dokumentieren (Datum, Gesprächspartner, Inhalt) — schützt vor späterem Streit.
- Engpass-Härtefall: Patient mehrfach abweisen lässt Beschwerde an Apothekerkammer wahrscheinlich werden — proaktive Lösung suchen.

## Mustertexte

### Austauschdokumentation (Vorlage)
"Rezept vom [Datum], verordnet: [Wirkstoff X, Stärke, Packungsgrösse], PZN [...]. Nicht lieferbar laut Grosshandel-Anfrage [Datum, Lieferant] und BfArM-Engpassliste vom [Datum]. Austausch erfolgt nach [ALBVVG / § 17 Abs. 5 ApBetrO / Rücksprache Arzt]. Abgegeben: [Wirkstoff Y oder X mit abweichender Stärke/Packung], PZN [...]. Menge: [...] (entspricht der ärztlich verordneten Tagesdosis x Dauer). Beratung Patient: erfolgt. Apotheker:in: [Name]."

### Information an Patient (Auszug)
"Sehr geehrte:r [Patient:in], das von Ihrer Ärztin/Ihrem Arzt verordnete Arzneimittel [Name] ist derzeit nicht lieferbar (BfArM-Engpassliste). Wir haben Ihnen daher [Austauschpräparat] mit dem gleichen Wirkstoff abgegeben. Die Anwendung erfolgt wie verordnet — bitte beachten Sie die Hinweise auf der Packung. Bei Rückfragen erreichen Sie uns unter [Telefon]."

## Typische Fehler

- Austausch ohne BfArM-Listen-Beleg — Krankenkasse retaxiert mangels Engpass-Indikation.
- Wirkstoffklassen-Austausch ohne Arzt-Rücksprache — Apothekenleitung sieht Patient nicht mehr, falls Therapieversagen.
- Engpass-Variation nur mündlich dokumentiert.
- Mehrfach-Austausch bei chronischer Therapie ohne Verlaufsdoku.
- ALBVVG-Möglichkeiten nicht ausgeschöpft, Patient mit "nicht lieferbar" weggeschickt.

## Querverweise

- `arzneimittelabgabe-verschreibungspflicht` (allgemeiner Abgabevorgang)
- `substitution-rabattvertrag-aut-idem` (Aut-idem)
- `import-einzelimport-73-amg` (Import-Variante)
- `retaxationsabwehr-nullretax-risiko` (Retax-Abwehr)
- `rechnung-retaxation-krankenkasse` (Abrechnung)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Codierung)

## Quellen Stand 06/2026

- AMG §§ 52a, 52b, 79.
- ALBVVG-Vorschriften (vom Anwender zu verifizieren — Aktualität, Detailregelungen).
- SGB V § 129 Abs. 2a und Rahmenvertrag.
- BfArM-Engpassliste (tagesaktuell online).
- ABDA-Mitteilungen zum Engpass-(vom Anwender zu verifizieren).
- BSG, staend. Rspr. zur Retaxation bei Engpass.

## 2. `livecheck-apog-apbetro-amg`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck ApoG ApBetrO AMG.

# Livecheck ApoG ApBetrO AMG

## Fachkern: Livecheck ApoG ApBetrO AMG
- **Spezialgegenstand:** Livecheck ApoG ApBetrO AMG. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Livecheck ApoG ApBetrO AMG** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `notfallkontrazeption-beratung`

**Fokus:** Notfallkontrazeption Beratung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Notfallkontrazeption Beratung

## Fachkern: Notfallkontrazeption Beratung
- **Spezialgegenstand:** Notfallkontrazeption Beratung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Notfallkontrazeption Beratung** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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
