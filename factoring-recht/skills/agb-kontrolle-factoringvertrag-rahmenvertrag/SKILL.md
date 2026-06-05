---
name: agb-kontrolle-factoringvertrag-rahmenvertrag
description: "AGB Kontrolle Factoringvertrag Rahmenvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AGB Kontrolle Factoringvertrag Rahmenvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **AGB Kontrolle Factoringvertrag Rahmenvertrag** im Plugin Factoring Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `agb-kontrolle-factoringklauseln-b2b` | AGB Kontrolle Factoringklauseln B2B: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |
| `factoringvertrag-rahmenvertrag-forderungskauf-kaufpreis-sicherhe` | Factoringvertrag Rahmenvertrag Forderungskauf Kaufpreis Sicherheitseinbehalt: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |
| `kuendigung-rahmenvertrag-exit-und-rueckuebertragung` | Kündigung Rahmenvertrag Exit und Rückübertragung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO. |

## Arbeitsweg

Im Plugin Factoring Recht gilt für **AGB Kontrolle Factoringvertrag Rahmenvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `agb-kontrolle-factoringklauseln-b2b`

**Fokus:** AGB Kontrolle Factoringklauseln B2B: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# AGB Kontrolle Factoringklauseln B2B

## Fachkern: AGB Kontrolle Factoringklauseln B2B
- **Spezialgegenstand:** AGB Kontrolle Factoringklauseln B2B. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Factoringverträge sind in der Regel **Formularverträge** des Factors. Damit unterliegen sie der AGB-Kontrolle nach §§ 305 ff. BGB. Auch im B2B-Verhältnis gelten die Inhaltskontrollen der §§ 307 BGB – die Klauselverbote der §§ 308 und 309 BGB greifen nicht direkt, sind aber als **Indikatoren** für die Unangemessenheit im Rahmen des § 307 BGB heranzuziehen (Indizwirkung, st. Rspr. BGH).

Dieser Skill prüft die typischen Risikoklauseln im Factoringvertrag: Veritäts- und Bonitätshaftung, Rückbelastungsrechte, Verzugszinsen, Aufrechnungsverbote, Vorfälligkeitsentschädigungen, Kündigungsregelungen, Schiedsklauseln. Ziel ist eine durchsetzbare und zugleich faire Klauselgestaltung.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sie entwerfen oder überarbeiten einen Factoring-Rahmenvertrag.
- Ein Factoringkunde greift einzelne Klauseln aus dem Rahmenvertrag an (Unwirksamkeit der Rückbelastung).
- Im Streitfall stellt sich die Frage, ob der Vertrag noch durchsetzbar bleibt, wenn Einzelklauseln fallen (§ 306 BGB).
- Sie prüfen einen Factoringvertrag, der dem Mandanten vom Factor vorgelegt wurde.

Fragen zum Einstieg:
- Wer hat den Vertrag gestellt (Factor oder Kunde)?
- Liegt der Vertrag in vorformulierter Form vor (Verwendung in Vielzahl von Verträgen)?
- Welche konkreten Klauseln sind kritisch (Rückbelastung, Bonitätsverlust, Sperrkonto)?
- Gibt es Indizien für ausgehandelte Klauseln (Versionierung, Verhandlungsprotokoll)?
- Ist der Kunde wirtschaftlich gleichstark oder als unterlegene Partei einzuordnen?

## Rechtlicher Rahmen

- **§ 305 BGB**: Definition AGB – vorformuliert, gestellt, mehrfache Verwendung. Aushandeln macht die Klausel zur Individualabrede.
- **§ 305c BGB**: Überraschende Klauseln werden nicht Vertragsbestandteil.
- **§ 307 BGB**: Inhaltskontrolle – unangemessene Benachteiligung des Vertragspartners. Im B2B-Bereich greift das Transparenzgebot (§ 307 Abs. 1 S. 2 BGB) und die Generalklausel.
- **§ 308, 309 BGB**: Klauselverbote – im B2B nicht direkt anwendbar, aber Indizwirkung nach BGH.
- **§ 310 Abs. 1 BGB**: Modifikation für B2B – Klauselverbote der §§ 308, 309 gelten nicht direkt, aber im Rahmen der Angemessenheitsprüfung nach § 307.
- **§ 306 BGB**: Teilnichtigkeit – unwirksame Klausel fällt, der Vertrag bleibt im Übrigen wirksam.
- **§ 138 BGB**: Wucherische Vertragsgestaltung als äußerste Grenze.
- **§ 242 BGB**: Treu und Glauben als ergänzender Kontrollmaßstab.

## / Schritt für Schritt

1. **Vertragstyp einordnen**: Rahmenvertrag, Einzelankaufverträge, Annex-Sicherungsverträge.
2. **AGB-Eigenschaft prüfen**: Vorformuliert? Mehrfach verwendet? Vom Factor gestellt?
3. **Klauselinventur**: Alle kritischen Klauseln auflisten (Rückbelastung, Verzug, Zinsen, Sperrkonto, Bonitätshaftung).
4. **Klauselkontrolle pro Klausel**: Transparenz, Angemessenheit, Indizwirkung der § 308, 309 BGB.
5. **Salvatorische Klausel** prüfen: BGH hält salvatorische Klauseln in AGB für unwirksam, da sie versuchen, die Folgen der § 306 BGB zu umgehen.
6. **Risikobewertung**: Welche Klauseln sind im Streitfall wahrscheinlich unwirksam? Reicht der Vertrag ohne sie aus?
7. **Anpassungsempfehlung**: Klauseln umformulieren, alternative Strukturen vorschlagen.

## Trade-off-Matrix

| Klausel | Risiko § 307 BGB | Empfehlung |
|---|---|---|
| Vollständige Bonitäts- und Veritätshaftung des Kunden im echten Factoring | Widerspruch zu Wesen des echten Factorings – Indiz für Unangemessenheit | Klare Trennung: Verität bleibt, Bonität nur im unechten Factoring |
| Unbegrenztes Rückbelastungsrecht bei Reklamationen | Zu weit, Treu und Glauben | Fristen, Schwellen, Nachweispflichten |
| Pauschalierte Bearbeitungsgebühr für Mahnung | Wenn unangemessen hoch: § 307 BGB | An tatsächlichem Aufwand orientieren |
| Aufrechnungsverbot für Kundenforderungen | Indiz § 309 Nr. 3 BGB | Nur für streitige, nicht für unstreitige Gegenforderungen |
| Pauschale Vertragsstrafe bei Kündigung | § 309 Nr. 5 BGB-Indiz | Schadenpauschale mit Beweismöglichkeit |
| Schiedsklausel mit ausschließlicher Zuständigkeit | Im B2B grds. zulässig | Klare Sprachfassung, Kosten verteilen |

## Praxistipps

- **Verhandlungsdokumentation**: Wenn Klauseln tatsächlich ausgehandelt werden, ist das in einem Verhandlungsprotokoll festzuhalten – sonst bleibt es AGB.
- **Mehrere Versionen**: Häufig nutzen Factoringgesellschaften Standardversionen mit Optionsklauseln. Die Optionsstruktur kann selbst AGB sein.
- **Sprachklarheit**: Komplexe Verrechnungsformeln in der Rückbelastungsklausel sind regelmäßig intransparent und damit nach § 307 Abs. 1 S. 2 BGB unwirksam.
- **Kein Misch-AGB**: Eine Klausel sollte nicht in einem Atemzug regelmäßige Kosten und Sanktionen mischen – Trennung verbessert die Standhaltigkeit.
- **Klauselbibliothek pflegen**: Klauseln, die in einem Gerichtsverfahren standgehalten haben, dokumentieren und wiederverwenden.

## Mustertexte

**Klausel Veritätshaftung (zulässig)**

"Der Kunde haftet für den Bestand und die Einredefreiheit der abgetretenen Forderungen (Veritätshaftung). Bei Mängeln der Forderung kann der Factor die Forderung zurückübertragen und den Kaufpreis abzüglich der angefallenen Kosten zurückfordern."

**Klausel Rückbelastung mit Fristen**

"Wird eine Forderung vom Debitor reklamiert oder nicht innerhalb von 90 Tagen nach Fälligkeit beglichen, hat der Factor das Recht, die Forderung mit Wirkung für die Zukunft zurückzuübertragen, sofern die Reklamation auf Umständen aus der Sphäre des Kunden beruht. Die Rückbelastung erfolgt binnen 30 Tagen nach Kenntnis."

**Klausel Aufrechnungsverbot (eingeschränkt)**

"Der Kunde kann nur mit unbestrittenen oder rechtskräftig festgestellten Gegenforderungen aufrechnen. Dies gilt nicht für Gegenforderungen aus dem Synallagma desselben Vertrags."

## Typische Fehler

- Verwendung salvatorischer Klauseln in AGB – sind nach BGH unwirksam, retten die Gesamtklauselgeltung nicht.
- Übersehen der Indizwirkung der §§ 308, 309 BGB im B2B-Bereich.
- Unbegrenzte Rückbelastungsrechte ohne Fristen und ohne Differenzierung.
- Vermischung von Bonitäts- und Veritätsrisiko im echten Factoring – widerspricht dem Vertragstyp und löst § 307 BGB aus.
- Unklare Definition des "Kaufpreises" in Verrechnungsklauseln.

## Edge Cases und Sonderkonstellationen

- **Klausel im Anlagenwerk**: AGB-Charakter haftet auch Anlagen an, wenn sie standardisiert sind (Allgemeine Geschäftsbedingungen für Sicherheitenbestellung etc.); separate Aushandlung notwendig.
- **Online-Akzeptanzklauseln (Plattform-Factoring)**: Click-Wrap-Vereinbarungen bei Online-Verträgen unterliegen voll der AGB-Kontrolle; transparenter Hinweis vor Vertragsschluss erforderlich.
- **Internationale Klauseln**: Bei englischsprachigen Factoringverträgen mit deutschem Vertragspartner gelten §§ 305 ff. BGB; Übersetzung kein Aushandeln.
- **Vergleichsklauseln**: Pauschale Streiterledigungsklauseln (alle Streitigkeiten gegen Pauschalzahlung) wegen § 307 BGB problematisch.
- **Drittsicherheiten**: Bürgschaften und Garantien Dritter zu Lasten Factor-Kunde, die formularmäßig verlangt werden, unterliegen ebenfalls AGB-Kontrolle des Kunden.
- **Verzugszinsanpassung**: Verzugszinsen über § 288 Abs. 2 BGB hinaus müssen ausdrücklich vereinbart sein; AGB-Klausel "Verzugszinsen 15 Prozent" benötigt Verhältnismäßigkeitsprüfung.

## Querverweise

- `factoringvertrag-rahmenvertrag-forderungskauf-kaufpreis-sicherhe`
- `echtes-und-unechtes-factoring-risikoverteilung`
- `kuendigung-rahmenvertrag-exit-und-rueckuebertragung`
- `gerichtsstand-rechtswahl-schiedsvereinbarung`

## Quellen Stand 06/2026

- BGB §§ 305 bis 310, insbesondere § 307 Abs. 1 S. 2 (Transparenz) und § 310 Abs. 1 (B2B-Modifikation).
- BGB § 306 zur Teilnichtigkeit und § 138 zur Sittenwidrigkeit.
- BGH, st. Rspr. zur Indizwirkung der § 308, 309 BGB im B2B-Bereich (amtliche Sammlung).
- BGH zur Unwirksamkeit salvatorischer Klauseln in AGB.
- Literatur zur AGB-Kontrolle von Factoringverträgen (nur mit eigener Recherche zitieren).

## 2. `factoringvertrag-rahmenvertrag-forderungskauf-kaufpreis-sicherhe`

**Fokus:** Factoringvertrag Rahmenvertrag Forderungskauf Kaufpreis Sicherheitseinbehalt: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Factoringvertrag Rahmenvertrag Forderungskauf Kaufpreis Sicherheitseinbehalt

## Fachkern: Factoringvertrag Rahmenvertrag Forderungskauf Kaufpreis Sicherheitseinbehalt
- **Spezialgegenstand:** Factoringvertrag Rahmenvertrag Forderungskauf Kaufpreis Sicherheitseinbehalt. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Factoringvertrag Rahmenvertrag Forderungskauf Kaufpreis Sicherheitseinbehalt** im Bereich **Factoring-Recht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Factoring als laufender Forderungsankauf, Vertrags- und Aufsichtsrecht, BaFin-Erlaubnisfragen, Abtretung, Debitorenschutz, Insolvenz, Bilanzierung und internationale Lieferkettenfinanzierung.

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

## 3. `kuendigung-rahmenvertrag-exit-und-rueckuebertragung`

**Fokus:** Kündigung Rahmenvertrag Exit und Rückübertragung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KWG § 1 Abs. 1a Satz 2 Nr. 9, § 32 KWG, BaFin-Merkblatt Factoring, BGB §§ 398 ff., HGB § 354a, ZAG, GwG, DSGVO.

# Kündigung Rahmenvertrag Exit und Rückübertragung

## Fachkern: Kündigung Rahmenvertrag Exit und Rückübertragung
- **Spezialgegenstand:** Kündigung Rahmenvertrag Exit und Rückübertragung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Kündigung Rahmenvertrag Exit und Rückübertragung** im Bereich **Factoring-Recht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Factoring als laufender Forderungsankauf, Vertrags- und Aufsichtsrecht, BaFin-Erlaubnisfragen, Abtretung, Debitorenschutz, Insolvenz, Bilanzierung und internationale Lieferkettenfinanzierung.

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
