---
name: heimversorgung-versorgungsvertrag-mietvertrag
description: "Heimversorgung Versorgungsvertrag Mietvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Heimversorgung Versorgungsvertrag Mietvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Heimversorgung Versorgungsvertrag Mietvertrag** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `heimversorgung-versorgungsvertrag` | Heimversorgung Versorgungsvertrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `mietvertrag-apothekenstandort-konkurrenzschutz` | Mietvertrag Apothekenstandort Konkurrenzschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `substitution-rabattvertrag-aut-idem` | Substitution Rabattvertrag Aut-idem: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Heimversorgung Versorgungsvertrag Mietvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `heimversorgung-versorgungsvertrag`

**Fokus:** Heimversorgung Versorgungsvertrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Heimversorgung Versorgungsvertrag

## Fachkern: Heimversorgung Versorgungsvertrag
- **Spezialgegenstand:** Heimversorgung Versorgungsvertrag. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Versorgung von Bewohnern stationärer Pflegeeinrichtungen (Pflegeheime, betreute Wohnformen für Behinderte) durch eine "versorgende Apotheke". Versorgungsvertrag nach § 12a ApoG i.V.m. ApBetrO (Heimversorgungsrecht). Apotheke übernimmt Medikationsmanagement, regelmässige Lieferung, Verblisterung (manuell oder maschinell), Anwesenheit für Beratung. Zentrale Streitpunkte: Antikorruption, Patientenwahlfreiheit, Verblisterungsentgelt.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Apotheke schliesst neuen Versorgungsvertrag mit Heim.
- Aufsicht beanstandet Vertragskonditionen (Wahlfreiheit, Geldfluss).
- Heim verlangt "Versorgungspauschale" oder kostenlose Leistungen — § 11 ApoG-Risiko.
- Verblisterungsservice eingeführt; Vergütung mit GKV/PKV-Konflikt.
- Konkurrenz-Apotheke wirft Wettbewerbsverletzung vor.

Eingaben:
- Versorgungsvertragsentwurf oder bestehender Vertrag.
- Heim-Konzept (Anzahl Bewohner, Pflegegrade, Klinik-Anschluss).
- Geplante Vergütungsstrukturen (Verblisterung, Beratung, Notdienst).
- Patientenwahlfreiheits-Erklärung (sofern vorhanden).
- ABDA-Mustervertrag (sofern verwendet).

## Rechtlicher Rahmen

- **§ 12a ApoG:** Versorgungsvertrag — Schriftform, Anzeige Landesaufsicht, Anforderungen an Inhalt.
- **§ 35 ApBetrO und Anlage:** Pflichten der versorgenden Apotheke (Medikationsmanagement, Beratung, Notdienst, regelmässige Visiten).
- **§ 33 SGB XI:** Pflegeheimbetreuung.
- **§ 11 ApoG:** Zuweisungsverbot Arzt-Apotheke; analog auch im Verhältnis Heim-Apotheke.
- **§§ 299a, 299b StGB:** Antikorruption.
- **§ 7 HWG:** Zuwendungsverbot.
- **§ 78 AMG / AMPreisV:** Preisbindung Rx.
- **DSGVO Art. 9, 28:** Verarbeitung Gesundheitsdaten, Auftragsverarbeitung.
- BGH staend. Rspr. zur Heimversorgung.

## / Schritt für Schritt

1. **Vertragsinhalt prüfen:**
 - Schriftform, Unterschrift Heimleitung + Apothekenleitung.
 - Pflichten Apotheke (Beratung, Visite, Notdienst, Verblisterung).
 - Patientenwahlfreiheit gesondert betont.
 - Vergütung: ausschliesslich für tatsächliche Leistungen, marktüblich.
2. **Anzeige Landesaufsicht:** § 12a ApoG verlangt unverzügliche Anzeige.
3. **Patientenwahlfreiheit:** Heim muss Bewohner über Freiheit informieren; Apotheke darf nicht als "Vertragsapotheke" durch Heimleitung zugewiesen werden.
4. **Geldflüsse:** Keine "Versorgungspauschale" als verdeckte Zuweisung. Verblisterungsentgelt nur auf Patient/GKV-Seite, nicht ans Heim.
5. **Verblisterung:** Patienteneinwilligung, Hygiene-SOP, separate Räume (siehe ApBetrO § 35 Anlage), QM.
6. **Visiten:** Regelmässige Anwesenheit Apotheker:in im Heim — Frequenz im Vertrag definieren.
7. **Notdienst:** 24h-Erreichbarkeit, klare Kontaktdaten.
8. **Dokumentation:** Versorgungsprotokolle, Beratungsdokumentation pro Bewohner.

## Trade-off-Matrix

| Vertragsmodell | Zulässig | Risiko | Hinweis |
|---|---|---|---|
| Klassischer Versorgungsvertrag § 12a ApoG | ja | gering | Wahlfreiheit dokumentiert |
| Versorgungsvertrag mit Pauschale ans Heim | nein | hoch | § 11 ApoG / § 299a StGB |
| Verblisterung mit Vergütung von GKV | ja, soweit Rahmenvertrag erlaubt | gering bei Doku | aktueller Stand vom Anwender |
| Apothekenmietet Räume im Heim | grenzwertig | umsatzabhängige Miete: hoch | Festmiete marktüblich |
| Apotheker:in als Beirat des Heims (entgeltlich) | grenzwertig | Geldfluss-Begründung | strenge Doku |
| Patient erhält "Heim-Bonus" für Apothekenwahl | nein | UWG, HWG | unzulässig |

## Praxistipps

- Patientenwahlfreiheit darf nicht nur im Vertrag stehen, sondern muss tatsächlich gelebt werden — schriftlicher Hinweis an jeden Bewohner bei Aufnahme.
- "Beratungsverträge" mit Heimleitung sind oft verdeckte Zuweisung — nur bei echter Beratungsleistung mit Tätigkeitsnachweis zulässig.
- Verblisterung: gesonderter Raum, eigene SOPs, Lagerung der Blister kennzeichnen.
- Bei Heimbetreiberwechsel: Vertrag neu abschliessen; Übergang dokumentieren.
- Notdienst-Vertretung: Vertretungsapotheke muss in den Vertrag einbezogen werden (Apothekerkammer-Notdienstplan).

## Mustertexte

### Versorgungsvertrag (Auszug Kerninhalt)
"§ 1 Gegenstand: Die Apotheke versorgt die Bewohner der [Heim] mit Arzneimitteln nach ärztlicher Verschreibung. Die Apotheke leistet Medikationsmanagement, regelmässige pharmazeutische Visiten (mind. monatlich), Verblisterung auf Wunsch und Notdienstbereitschaft. § 2 Patientenwahlfreiheit: Die Bewohner sind in der Wahl der versorgenden Apotheke frei. Eine vertragliche Zuweisung der Bewohner an die Apotheke ist ausgeschlossen. Das Heim weist Bewohner bei Einzug schriftlich auf das Wahlrecht hin (Anlage 1). § 3 Vergütung: Die Apotheke erhält ausschliesslich die regulären Erlöse aus der Arzneimittelabgabe nach AMPreisV. Pauschalzahlungen vom Heim oder Heimträger sind ausgeschlossen. § 4 Datenschutz: Auftragsverarbeitungsvertrag nach Art. 28 DSGVO ist Vertragsbestandteil (Anlage 2). § 5 Dauer und Kündigung: Vertrag läuft auf unbestimmte Zeit, Kündigung mit Frist von drei Monaten zum Quartalsende."

### Anzeige Landesaufsicht (Auszug)
"Sehr geehrte Damen und Herren, hiermit zeige ich gemäss § 12a Abs. 5 ApoG den Abschluss eines Versorgungsvertrages an. Apotheke: [Name, Anschrift, Erlaubnis vom Datum]. Heim: [Name, Anschrift, Trägerschaft]. Vertragsbeginn: [Datum]. Vertragsdauer: unbefristet. Beigefügt sind: 1. Versorgungsvertrag (Kopie), 2. Patientenwahlfreiheits-Information (Muster), 3. Verblisterungs-SOP, 4. Notdienst-Bereitschaftsregelung."

## Typische Fehler

- "Versorgungspauschale" an Heim — § 11 ApoG / § 299a StGB.
- Patientenwahlfreiheit nur im Vertrag, aber Bewohner werden in der Praxis nicht informiert.
- Verblisterung ohne separate SOP, Hygienemängel.
- Notdienst-Vertretung nicht geregelt; Heim erreicht niemanden bei Krise.
- Mietvertrag mit Umsatzkomponente — verdeckte Beteiligung Heim am Apothekenerlös.

## Querverweise

- `versorgung-pflegeheim-schnittstelle` (operativer Workflow)
- `kooperation-arzt-apotheke-antikorruption` (Antikorruption)
- `skonti-boni-rabatte-zuweisungsverbot` (Geldflüsse)
- `datenschutz-in-apotheke-gesundheitsdaten` (DSGVO)
- `mietvertrag-apothekenstandort-konkurrenzschutz` (Miete im Heim)
- `qualitaetsmanagement-qms-sops` (Verblisterung)

## Quellen Stand 06/2026

- ApoG § 12a; ApBetrO § 35 Anlage.
- SGB XI § 33.
- AMG § 78; AMPreisV.
- StGB §§ 299a, 299b.
- BGH und OLG, staend. Rspr. zur Heimversorgung.
- ABDA-Mustervertrag (vom Anwender Aktualität zu verifizieren).
- DSGVO Art. 9, 28.

## 2. `mietvertrag-apothekenstandort-konkurrenzschutz`

**Fokus:** Mietvertrag Apothekenstandort Konkurrenzschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Mietvertrag Apothekenstandort Konkurrenzschutz

## Fachkern: Mietvertrag Apothekenstandort Konkurrenzschutz
- **Spezialgegenstand:** Mietvertrag Apothekenstandort Konkurrenzschutz. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Mietvertrag Apothekenstandort Konkurrenzschutz** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 3. `substitution-rabattvertrag-aut-idem`

**Fokus:** Substitution Rabattvertrag Aut-idem: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Substitution Rabattvertrag Aut-idem

## Fachkern: Substitution Rabattvertrag Aut-idem
- **Spezialgegenstand:** Substitution Rabattvertrag Aut-idem. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Beim Abgabevorgang an GKV-Versicherte ist die Apotheke verpflichtet, ein wirkstoffgleiches Arzneimittel ("aut idem") des Rabattpartners der Krankenkasse abzugeben, sofern der Arzt das nicht ausgeschlossen hat (Aut-idem-Kreuz). Bei Abweichungen drohen Retax bis zur Vollabsetzung ("Null-Retax"). Pharmazeutische Bedenken erlauben eine Ausnahme; sie müssen jedoch im Einzelfall, schriftlich und nachvollziehbar dokumentiert werden.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Substitution kollidiert mit Patientenwunsch oder Verträglichkeit.
- Krankenkasse retaxiert wegen abweichender Abgabe.
- Patient verlangt Markenprodukt trotz Rabattvertrag.
- Aut-idem-Kreuz fehlt, aber Patient ist auf bestimmtes Präparat eingestellt.
- Abgabe von Originalpräparat trotz Generikum-Rabattvertrag — Dokumentation für Aufsicht.

Eingaben:
- Rezept / E-Rezept-Token.
- Aktueller Aut-idem-Status, Rabattvertragsliste der Krankenkasse.
- Patientenanamnese (Allergie, Unverträglichkeit, Compliance-Risiko).
- Vorherige Substitutionen, Beratungsprotokolle.

## Rechtlicher Rahmen

- **§ 129 SGB V:** Rahmenvertrag, Aut-idem-Substitution, Rabattvertragsregeln.
- **Anlage 1 Rahmenvertrag § 129 SGB V** (vom Anwender zu verifizieren — Vereinbarung GKV-Spitzenverband / DAV): Substitutionsausschlussliste.
- **§ 73 Abs. 5 SGB V:** Wirtschaftlichkeitsgebot.
- **§ 17 Abs. 5 ApBetrO:** Abgabe nach pharmazeutischer Sorgfalt.
- **§ 12 ApBetrO:** Beratungspflicht.
- BSG und LSG, staend. Rspr. zu Retaxation und Pharmazeutische Bedenken.
- BGH, staend. Rspr. zur Substitution.

## / Schritt für Schritt

1. **Aut-idem-Kreuz prüfen:** Wenn gesetzt — keine Substitution (Apotheker:in darf nicht abweichen).
2. **Wirkstoff, Stärke, Packungsgrösse, Indikationsbereich, Galenik** identifizieren.
3. **Rabattvertrag prüfen:** Welches Präparat hat die Krankenkasse mit welchem Hersteller? Datenstand aktuell?
4. **Substitutionsausschlussliste:** Bestimmte Wirkstoffe sind grundsätzlich nicht austauschbar (Liste vom Anwender zu prüfen — Anlage 1 Rahmenvertrag).
5. **Pharmazeutische Bedenken:** Liegt eine Indikation gegen Substitution vor (z. B. Allergie auf Hilfsstoff, fehlende Anwendererfahrung, Compliance-Risiko bei älteren Patienten)? Dann Bedenken schriftlich dokumentieren.
6. **Beratung:** Patient über Substitution informieren, Aufklärung über gleiche Wirkstoffe.
7. **Abgabe:** Bei dokumentierten Bedenken Originalpräparat abgeben; Kennzeichnung auf Rezept "Pharmazeutische Bedenken".
8. **Krankenkasse-Kommunikation:** Bei Retax sofort Widerspruch einlegen, Bedenken-Dokumentation beifügen.

## Trade-off-Matrix

| Situation | Pflicht | Ausnahme | Risiko |
|---|---|---|---|
| Aut-idem Kreuz gesetzt | keine Substitution | — | gering |
| Rabattvertrag, Patient akzeptiert | substituieren | — | gering |
| Rabattvertrag, Patient lehnt ab | substituieren, sofern keine Bedenken | Pharmazeutische Bedenken | Retax bei mangelnder Dokumentation |
| Wirkstoff auf Ausschlussliste | nicht austauschen | — | bei Verstoss Retax |
| Patient älter, neu auf Substitut | Substitut, aber Aufklärung | bei begründeter Compliance-Sorge: Bedenken | Vollabsetzung möglich |
| Allergie gegen Hilfsstoff im Substitut | Originalpräparat | Bedenken-Dokumentation | gering bei guter Doku |

## Praxistipps

- Pharmazeutische Bedenken müssen einzelfallbezogen sein — Pauschalformeln wie "Patient ist alt" reichen nicht. Indikation, Hilfsstoff-Allergie, Compliance-Risiko, Galenik-Unterschied (z. B. Inhalator-Typ) — alles konkret.
- Substitutionsausschlussliste stets aktuell halten — DAV-Mitgliedsapotheken erhalten regelmässig Updates.
- Substitution-Software (SaaS) prüft tagesaktuell Rabattverträge; manuelle Kontrolle nur zur Validierung.
- Patient bewusst zu Substitution erziehen — schriftliche Patienteninformation in Wartebereich.
- Bei Null-Retax: Frist Widerspruch (vier Wochen, vom Anwender zu verifizieren) einhalten; sonst entgangener Erlös endgültig.

## Mustertexte

### Pharmazeutische Bedenken-Vermerk (Auszug)
"Patient:in [Initialen, Geb.-Datum], Rezept vom [Datum] für [Wirkstoff, Stärke]. Rabattvertrag mit Krankenkasse [Name] sieht [Generikum X] vor. Bedenken: [a) Patient ist seit [Zeit] auf [Originalpräparat] eingestellt; b) bekannte Hilfsstoff-Unverträglichkeit gegen [Hilfsstoff]; c) Galenik-Wechsel würde Compliance gefährden, vgl. § 17 Abs. 5 ApBetrO]. Beratung am [Datum] durchgeführt. Abgabe: [Originalpräparat]. Aufkleber 'Pharmazeutische Bedenken' auf Rezept angebracht."

### Widerspruch gegen Retax (Auszug)
"Mit Schreiben vom [Datum] retaxieren Sie die Abgabe vom [Datum] in Höhe von [Betrag]. Hiergegen legen wir frist- und formgerecht Widerspruch ein. Die Abgabe erfolgte abweichend vom Rabattvertrag aufgrund pharmazeutischer Bedenken (Hilfsstoff-Unverträglichkeit, dokumentiert in Anlage [Nr.]). § 17 Abs. 5 ApBetrO und § 129 Abs. 1a SGB V berechtigen zur Abweichung. Wir bitten um Stornierung der Retax."

## Typische Fehler

- Substitution ohne Aut-idem-Prüfung — sofortige Retax.
- Pauschale Pharmazeutische Bedenken ("Patient will Original") — wird als nicht ausreichend abgelehnt.
- Substitutionsausschlussliste ignoriert; Substitution eines nicht austauschbaren Wirkstoffs — Vollabsetzung.
- Bedenken nicht auf Rezept gekennzeichnet — Krankenkasse erkennt nicht, dass Apotheke begründet abweicht.
- Widerspruchsfrist versäumt — entgangener Erlös wird endgültig.

## Querverweise

- `arzneimittelabgabe-verschreibungspflicht` (allgemeiner Abgabevorgang)
- `retaxationsabwehr-nullretax-risiko` (Retax-Abwehr)
- `lieferengpaesse-austausch-dokumentation` (Austausch bei Lieferengpass)
- `rechnung-retaxation-krankenkasse` (Krankenkassen-Rechnung)
- `e-rezept-ti-gematik-apothekenprozess` (E-Rezept-Substitution)
- `schiedsstellen-krankenkassen-apotheke` (Streitschlichtung)

## Quellen Stand 06/2026

- SGB V §§ 129, 73; ApBetrO § 17.
- Rahmenvertrag § 129 SGB V mit Anlagen (vom Anwender zu verifizieren — Anlage 1 Substitutionsausschlussliste).
- BSG, staend. Rspr. zu pharmazeutischen Bedenken und Retaxation.
- DAV-Mitgliederinformationen / aktuelle Rabattvertragslisten (vom Anwender zu verifizieren).
- ABDA-Leitlinien zur Substitution.
