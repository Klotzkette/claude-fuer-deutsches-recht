---
name: landesaufsicht-krankenhausaufsicht
description: "Landesaufsicht Krankenhausaufsicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Landesaufsicht Krankenhausaufsicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Landesaufsicht Krankenhausaufsicht** im Plugin Krankenhausrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `landesaufsicht-krankenhausaufsicht-beanstandung` | Landesaufsicht ueber Krankenhaeuser nach Landeskrankenhausgesetzen: Beanstandungen, Ersatzvornahme, Schliessungsanordnung, Klage und einstweiliger Rechtsschutz. |
| `landeskrankenhausplan-aufnahme-herausnahme-aenderung` | Landeskrankenhausplan: Aufnahme, Herausnahme oder Aenderung des Plankrankenhausstatus, Beteiligungs- und Anhoerungsrechte, Klage und einstweiliger Rechtsschutz gegen Planentscheidungen. |
| `landesrecht-und-bundesrecht-trennen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Landesrecht und Bundesrecht trennen. |

## Arbeitsweg

Im Plugin Krankenhausrecht gilt für **Landesaufsicht Krankenhausaufsicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `landesaufsicht-krankenhausaufsicht-beanstandung`

**Fokus:** Landesaufsicht ueber Krankenhaeuser nach Landeskrankenhausgesetzen: Beanstandungen, Ersatzvornahme, Schliessungsanordnung, Klage und einstweiliger Rechtsschutz.

# Landesaufsicht Krankenhausaufsicht Beanstandung

## Fachkern: Landesaufsicht Krankenhausaufsicht Beanstandung
- **Spezialgegenstand:** Landesaufsicht Krankenhausaufsicht Beanstandung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Die Landeskrankenhausaufsicht prueft strukturelle Maengel, Versorgungssicherheit, Hygiene, Personal- und Geraeteausstattung. Werkzeuge: Beanstandung, Auflagen, Anordnung, Bussgeld, im Extremfall Schliessung oder Herausnahme aus dem Krankenhausplan.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welche Aufsichtsbehoerde (Bezirksregierung, Landesministerium, Gesundheitsamt) handelt?
- Was ist Gegenstand (Hygiene, Personal, Bauzustand, MDK-Strukturpruefung, OP-Bereich, Patientensicherheit)?
- Liegt eine schriftliche Beanstandung mit Frist und Rechtsbehelfsbelehrung vor?
- Welche Folgemassnahmen drohen (Auflage, Bussgeld, Schliessung)?
- Wurden Anhoerungs- und Verteidigungsrechte gewahrt?

## Rechtlicher Rahmen
- **Landeskrankenhausgesetze** (z. B. § 32 ff. KHGG NRW, BayKrG, GKKG BW) — Aufsichtskompetenzen.
- **VwVfG / Landes-VwVfG §§ 28, 35 ff., 48, 49** Verwaltungsakte, Anhoerung.
- **IfSG §§ 23, 36** Hygieneueberwachung durch Land/Gesundheitsamt.
- **SGB V § 137** Qualitaetssicherung.
- **KHG § 8** Versorgungsauftrag und Foerderungsvoraussetzungen.
- **VwGO §§ 42, 80** Klagen und einstweiliger Rechtsschutz.

## / Schritt fuer Schritt
1. **Aufsichtsbehoerde und Anlass identifizieren:** Routineprueung, Beschwerde, MD-Bericht, Vorfall?
2. **Anhoerung wahrnehmen:** Sachverhaltsdarstellung, Gegendarstellung, Sachverstaendigenstellungnahme.
3. **Bescheid pruefen:** Auflage, Anordnung, Bussgeld, Schliessungsdrohung; Ermessen und Verhaeltnismaessigkeit.
4. **Frist sichern:** Widerspruch (wenn vorgesehen) oder Klage binnen 1 Monat.
5. **Massnahmen umsetzen:** Auflagen erfuellen, Nachweis fuehren, Aufsichtsdialog suchen.
6. **Rechtsschutz:** Klage VG, ggf. einstweiliger Rechtsschutz § 80 Abs. 5 VwGO (insbesondere bei Sofortvollzug).

## Trade-off-Matrix

| Massnahme Aufsicht | Reaktion | Risiko |
|---|---|---|
| Beanstandung mit Frist | Anhoerungsstellungnahme + Plan | i. d. R. heilbar |
| Anordnung mit Sofortvollzug | einstweiliger Rechtsschutz | Verfahrensdauer |
| Bussgeld | Einspruch (OWiG) | Bestaetigung droht |
| Schliessungsdrohung | Klage + Eil-Antrag | existenzielle Wirkung |

## Praxistipps
- Anhoerung ist zentrale Phase — fruehzeitig substanziell stellungnehmen, Sachverstaendige einsetzen.
- Aufsichtsdialog meist konstruktiver als Eskalation; Auflagen erfuellen und dokumentieren.
- Bei Sofortvollzug § 80 Abs. 2, 5 VwGO der einzige Weg gegen sofortige Wirksamkeit.
- Hygienevorfaelle, Personalmaengel, OP-Komplikationen interne Ursachenanalyse + Korrekturplan, das ueberzeugt die Aufsicht.
- Schliessungsanordnung ist Ultima Ratio; oft milder Mittel (Teilschliessung, Auflagen) durchsetzbar.

## Mustertexte
**Stellungnahme auf Anhoerung:**
> Sehr geehrte Damen und Herren, zu Ihrer Beanstandung vom [Datum] nehmen wir wie folgt Stellung. Die festgestellten Maengel sind teilweise abgestellt: 1. … (Belege Anlage A). Verbleibende Massnahmen erfolgen bis [Frist]. Wir bitten von belastenden Anordnungen abzusehen und um Aufsichtsdialog.

**Klage VG mit Eilantrag:**
> Klageantrag: Der Bescheid vom [Datum] wird aufgehoben. Eilantrag § 80 Abs. 5 VwGO: Die aufschiebende Wirkung der Klage wird wiederhergestellt. Begruendung: 1. Bescheid ist rechtswidrig (Sachverhalt, Ermessensfehler) … 2. Aussetzungsinteresse ueberwiegt …

## Typische Fehler
- Anhoerung formelhaft beantwortet — Sachverhalt nicht widerlegt.
- Frist Widerspruch/Klage versaeumt — Bestandskraft.
- Sofortvollzug uebersehen — Massnahme wird umgesetzt.
- Aufsichtsdialog verweigert — Eskalation zur Schliessungsanordnung.

## Querverweise
- `krankenhausfinanzierungsgesetz-khg-grundstruktur`
- `landeskrankenhausplan-aufnahme-herausnahme-aenderung`
- `krankenhaushygiene-ifsg-landesrecht`
- `patientenbeschwerde-und-risikomanagement`
- `personaluntergrenzen-pflege-ppugv`
- `triage-notaufnahme-ueberlastung-dokumentation`

## Quellen Stand 06/2026
- Landeskrankenhausgesetze 16 Laender (Live-Check Landesministerien).
- Landes-VwVfG / Bundes-VwVfG §§ 28, 35 ff., 48, 49.
- IfSG §§ 23, 36.
- BVerwG, staend. Rspr. zu Aufsichtsmassnahmen und Verhaeltnismaessigkeit.
- VwGO §§ 42, 80, 113.

## 2. `landeskrankenhausplan-aufnahme-herausnahme-aenderung`

**Fokus:** Landeskrankenhausplan: Aufnahme, Herausnahme oder Aenderung des Plankrankenhausstatus, Beteiligungs- und Anhoerungsrechte, Klage und einstweiliger Rechtsschutz gegen Planentscheidungen.

# Landeskrankenhausplan Aufnahme Herausnahme Aenderung

## Fachkern: Landeskrankenhausplan Aufnahme Herausnahme Aenderung
- **Spezialgegenstand:** Landeskrankenhausplan Aufnahme Herausnahme Aenderung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret
Der Krankenhausplan des Landes weist Plankrankenhaus-Status zu, definiert Versorgungsauftrag, Bettenkapazitaeten und (mit KHVVG) Leistungsgruppen. Aufnahme, Herausnahme oder Aenderung sind Verwaltungsakte mit grundrechtsrelevanten Folgen — Klage zum VG ist regelmaeßig zulaessig.

## Wann dieses Modul hilft / Kaltstart-Fragen
- Welcher Verfahrensschritt steht an (Aufnahmeantrag, Herausnahme, Strukturaenderung)?
- Liegt ein Bescheid mit Rechtsbehelfsbelehrung vor?
- Welches Landesgesetz gilt (NRW: KHGG NRW; Bayern: BayKrG; BW: GKKG; …)?
- Gibt es Anhoerungs-/Beteiligungsrechte (Land, Kassen, Krankenhausgesellschaft)?
- Sind grundrechtsrelevante Folgen erkennbar (Schliessungseffekt, Versorgungsluecke)?

## Rechtlicher Rahmen
- **KHG § 6** Krankenhausplan (Bundesrecht).
- **Landeskrankenhausgesetze** konkretisieren Aufnahme/Herausnahme.
- **KHG § 6a** Leistungsgruppen seit KHVVG (eingegliedert in Planungssystem).
- **GG Art. 12 Abs. 1, Art. 3 Abs. 1** Berufsausuebung, Gleichbehandlung (BVerfG).
- **VwGO §§ 42, 80, 113** Anfechtungs-, Verpflichtungs-, einstweiliger Rechtsschutz.
- **VwVfG §§ 28 (Anhoerung), 39 (Begruendung), 48/49 (Aufhebung)**.
- **EU-Beihilfenrecht** bei oeffentlich gefoerderten Kliniken.

## / Schritt fuer Schritt
1. **Verfahrensstand klaeren:** Anhoerung, Bescheid-Entwurf, Bescheid, Widerspruchsverfahren, Klage?
2. **Bedarfslage darlegen:** Versorgungsbedarf, demographische Entwicklung, Erreichbarkeit, Krankheitsspektrum.
3. **Eigene Strukturqualitaet beweisen:** Personal, Geraete, Notfallstufe, LG-Profil.
4. **Beteiligungsrechte ausueben:** Stellungnahme zur Anhoerung, ggf. mit Sachverstaendigengutachten.
5. **Bescheid pruefen:** Ermessen (§ 40 VwVfG), Begruendung, Sachverhaltsfeststellung.
6. **Rechtsbehelf:** Widerspruch (wenn vom Land vorgesehen), Klage zum VG (§ 42 VwGO), einstweiliger Rechtsschutz § 80 Abs. 5 VwGO bei sofortvollziehbarer Herausnahme.

## Trade-off-Matrix

| Lage | Strategie | Erfolgswahrscheinlichkeit |
|---|---|---|
| Aufnahmebescheid mit weniger LG als beantragt | Widerspruch zur erweiterten LG-Zuweisung | mittel, wenn Strukturqualitaet erfuellt |
| Herausnahme aus Versorgungsbedarfsgruenden | Klage + einstweiliger Rechtsschutz | abhaengig von Versorgungsluecke |
| Strukturveraenderung erforderlich | konstruktive Verhandlung mit Land | hoch bei realistischer Anpassungsplan |
| Beihilferechtliche Bedenken kommunaler Klinik | EU-Beihilfen-Notifizierung | hoch, formal aufwendig |

## Praxistipps
- Bedarfsanalyse muss aktuell und differenziert sein (Demografie, ICD-Spektrum, Verbund-Versorgung).
- Anhoerung ist die wichtigste Phase — substanzielle Stellungnahme einreichen.
- BVerfG (1 BvR 1167/14) hat fuer Plankrankenhaus-Auswahlentscheidungen Auswahlkriterien definiert (Qualitaet, Wirtschaftlichkeit, Vielfalt der Traegerschaft).
- Sicherstellungsausnahme nach Landeskrankenhausgesetz pruefen.
- Einstweiliger Rechtsschutz § 80 Abs. 5 VwGO greift, wenn Sofortvollzug angeordnet ist.

## Mustertexte
**Stellungnahme zur Anhoerung:**
> Sehr geehrte Damen und Herren, in Ihrer Anhoerung vom [Datum] beabsichtigen Sie die Herausnahme der Klinik aus dem Krankenhausplan. Wir nehmen wie folgt Stellung: 1. Versorgungsbedarf ist durch [Daten] belegt. 2. Strukturqualitaet erfuellt LG-Anforderungen. 3. Erreichbarkeitsanalyse Land zeigt … Wir beantragen, von der Herausnahme abzusehen.

**Klage Verwaltungsgericht (Antrag):**
> Klageantrag: Den Bescheid vom [Datum] aufzuheben und das beklagte Land zu verpflichten, die Klaegerin als Plankrankenhaus … fortzufuehren. Begruendung: 1. Sachverhaltsfeststellung fehlerhaft, 2. Ermessensfehler, 3. Verstoss gegen Verhaeltnismaessigkeit …

## Typische Fehler
- Anhoerungsstellungnahme zu spaet oder unsubstanziell.
- Bedarfsdaten veraltet (Demografie, ICD).
- Strukturqualitaetsnachweise unvollstaendig.
- Sofortvollzug uebersehen — Klinik wird abgewickelt, bevor Klage entschieden ist.
- Beihilfenrecht nicht beruecksichtigt bei kommunaler Klinik.

## Querverweise
- `krankenhausfinanzierungsgesetz-khg-grundstruktur`
- `leistungsgruppen-und-qualitaetskriterien-reformlogik`
- `krankenhausreform-leistungsgruppen-routing`
- `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung`
- `landesaufsicht-krankenhausaufsicht-beanstandung`
- `notfallstufen-und-sicherstellungszuschlaege`

## Quellen Stand 06/2026
- KHG §§ 6, 6a.
- Landeskrankenhausgesetze 16 Laender (Live-Check Landesministerien).
- BVerfG, staend. Rspr. zu Plankrankenhaus-Auswahlentscheidung.
- BVerwG, staend. Rspr. zu Bedarfsplanung und Ermessensgrenzen.
- BSG, staend. Rspr. zu Versorgungsauftrag (§ 109 SGB V).
- VwGO §§ 42, 80, 113.

## 3. `landesrecht-und-bundesrecht-trennen`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Landesrecht und Bundesrecht trennen.

# Landesrecht und Bundesrecht trennen

## Fachkern: Landesrecht und Bundesrecht trennen
- **Spezialgegenstand:** Landesrecht und Bundesrecht trennen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KHG/KHEntgG, SGB V, Krankenhausplanung der Länder, Qualitätsvorgaben, Vergütung, MD-Prüfung, Haftung, Datenschutz und Arbeits-/Medizinprodukterecht.
- **Entscheidende Weiche:** Planung/Zulassung, Vergütung, Behandlungspflicht, Organisation, Qualität, Datenschutz, Haftung und Behördenkommunikation trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Landesrecht und Bundesrecht trennen** im Bereich **Krankenhausrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

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
