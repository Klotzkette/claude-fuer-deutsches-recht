---
name: agb-online-altersverifikation-jugendschutz
description: "AGB Online Altersverifikation Jugendschutz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AGB Online Altersverifikation Jugendschutz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **AGB Online Altersverifikation Jugendschutz** im Plugin Ecommerce Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `agb-im-online-shop-einbeziehung-305-bgb` | AGB im Online-Shop Einbeziehung § 305 BGB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG. |
| `altersverifikation-jugendschutz` | Altersverifikation Jugendschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG. |
| `app-commerce-in-app-kaeufe` | App-Commerce In-App-Käufe: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG. |

## Arbeitsweg

Im Plugin Ecommerce Recht gilt für **AGB Online Altersverifikation Jugendschutz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `agb-im-online-shop-einbeziehung-305-bgb`

**Fokus:** AGB im Online-Shop Einbeziehung § 305 BGB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG.

# AGB im Online-Shop – Einbeziehung § 305 BGB

## Fachkern: AGB im Online-Shop – Einbeziehung § 305 BGB
- **Spezialgegenstand:** AGB im Online-Shop – Einbeziehung § 305 BGB wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Fernabsatz/Widerruf, PAngV, UWG, DSGVO, DDG/DSA, TDDDG, Produktsicherheit, Gewährleistung, Zahlungsdienste und Plattformrecht.
- **Entscheidende Weiche:** Trenne Shop-Frontend, Bestellstrecke, Informationspflicht, Preis, Widerruf, Mängelrecht, Werbung, Tracking und Plattform-/Marketplace-Pflichten.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Allgemeine Geschäftsbedingungen (AGB) werden nur Vertragsbestandteil, wenn sie wirksam einbezogen wurden (§ 305 II BGB) und einer Inhaltskontrolle (§§ 307 ff. BGB) standhalten. Im Online-Shop entscheidet die Einbeziehung über die gesamte Vertragsgrundlage (Lieferung, Mängelhaftung, Eigentumsvorbehalt, Streitbeilegung). Der Skill ordnet Einbeziehung, Klauseltypen und Inhaltskontrolle.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Wo sind die AGB im Bestellprozess platziert?
- Wird vor Bestellabgabe ausdrücklich auf die AGB hingewiesen?
- Sind die AGB unmittelbar abrufbar und speicherbar?
- Welche Klauseln sind streitig (Versand, Vorkasse, Eigentumsvorbehalt, Haftungsausschluss, Gerichtsstand)?
- B2C oder B2B?
- Schon Abmahnung wegen unwirksamer AGB erhalten?

## Rechtlicher Rahmen

- § 305 II BGB: Einbeziehung – ausdrücklicher Hinweis, zumutbare Kenntnisnahme, Einverständnis.
- § 305c BGB: Überraschende Klauseln.
- § 306 BGB: Rechtsfolge der Nichteinbeziehung/Unwirksamkeit – Vertrag im Übrigen wirksam.
- §§ 307–309 BGB: Inhaltskontrolle, Klauselverbote.
- § 310 BGB: Anwendungsbereich – AGB auch im B2B, jedoch ohne Verbraucherschutz §§ 308, 309.
- UWG § 3a: Marktverhaltensregel.
- UKlaG: Unterlassungsklage Verbraucherverbände.
- BGH zur Online-AGB-Einbeziehung – ständige Rechtsprechung: Hinweis und Möglichkeit der Kenntnisnahme reichen; Pflicht zur Aktivbestätigung (Checkbox) nicht erforderlich, aber praktisch empfohlen.

## / Schritt für Schritt

1. **Einbeziehungspfad prüfen.** Vor Bestellabgabe Hinweis "Es gelten unsere AGB"; Link unmittelbar zur Volltext-Fassung; Druck- und Speicherfunktion.
2. **AGB-Inhalt strukturieren.**
 - Geltungsbereich,
 - Vertragsschluss / Angebot,
 - Lieferung und Versand,
 - Preise und Zahlung,
 - Eigentumsvorbehalt,
 - Mängelhaftung / Gewährleistung,
 - Haftungsbegrenzung,
 - Widerrufsrecht (Verlinkung),
 - Streitbeilegung / Gerichtsstand,
 - Datenschutz (Verweis).
3. **Inhaltskontrolle.**
 - § 309 Nr. 7 BGB: Haftungsausschluss bei Vorsatz/grober Fahrlässigkeit/wesentlichen Pflichten unzulässig.
 - § 309 Nr. 8 BGB: Gewährleistungsausschluss bei Neuware unzulässig.
 - § 309 Nr. 9 BGB: Laufzeit Dauerschuldverhältnisse begrenzt.
 - § 309 Nr. 12 BGB: Vorausabtretung von Gegenforderungen.
4. **Versionierung.** Stand-Vermerk, Archivierung, Verlauf.
5. **Update-Mechanismus.** Bei wesentlichen Änderungen: Mitteilung mit Widerspruchsrecht.
6. **Streitfall.** Klausel angreifen: nicht einbezogen oder unwirksam.

## Trade-off-Matrix

| Klauseltyp | Wirksam B2C | Wirksam B2B |
| --- | --- | --- |
| Vollständiger Haftungsausschluss | unwirksam § 309 Nr. 7 | meist unwirksam § 307 |
| Pauschaler Wertersatz Widerruf | unwirksam | – |
| Verlängerungsautomatik Abo > 12 Monate | unwirksam § 309 Nr. 9 | unwirksam § 307 |
| Gerichtsstandsklausel | grundsätzlich § 38 III ZPO | wirksam unter Kaufleuten |
| Eigentumsvorbehalt | wirksam | wirksam |

## Praxistipps

- Im Bestellprozess: Checkbox "Ich habe die AGB gelesen und akzeptiere sie" mit Link – einbeziehungssicher, aber nicht zwingend.
- Versionsnummer + Datum in den AGB sichtbar – beweissicher.
- Bei AGB-Update Bestandsverträge berücksichtigen – Vereinbarung erforderlich (Änderungskündigung oder Zustimmungslösung).
- Klauseln aus Musterverträgen blind übernehmen – häufig veraltet, vor allem zu § 312k.
- Internationale Lieferung: Rom-I-Anpassungen, Geo-Blocking-VO.

## Mustertexte

**Einbeziehungshinweis im Checkout:**
"Mit Klick auf 'zahlungspflichtig bestellen' bestätigen Sie, dass Sie unsere Allgemeinen Geschäftsbedingungen [LINK] und die Widerrufsbelehrung [LINK] gelesen haben und einverstanden sind."

**Standardklauseln (Kurzfassung):**
- Vertragspartner: [Firma], [Anschrift], [HRB], [USt-IdNr.].
- Angebot der Waren stellt unverbindliche Aufforderung dar; Vertragsschluss durch Annahmebestätigung des Anbieters.
- Lieferung: [Standard innerhalb 3–5 Werktagen]; Versandkosten ausgewiesen.
- Zahlung: [Kreditkarte, PayPal, Klarna, Vorkasse].
- Eigentumsvorbehalt bis vollständige Zahlung.
- Gewährleistung gesetzlich; bei Verbrauchern 2 Jahre.
- Widerrufsbelehrung siehe Anlage.

**Update-Mitteilung:**
"Wir aktualisieren unsere AGB zum [Datum]. Wesentliche Änderungen: [...]. Sie können den Änderungen binnen 6 Wochen widersprechen; sonst gelten die neuen AGB als angenommen. Volltext: [LINK]."

## Typische Fehler

- AGB nur als PDF zum Download – Kenntnisnahme erschwert, oft nicht ausreichend.
- Klausel zur Vorauszahlung bei Verbraucherkauf ohne Liefersicherung.
- Pauschale Bearbeitungsgebühr bei Widerruf.
- Gerichtsstand auf Sitz des Unternehmers für Verbraucher – unwirksam.
- Klausel "AGB können jederzeit geändert werden" ohne konkreten Änderungsmechanismus – unwirksam.

## Querverweise

- unwirksame-klauseln-versand-ruecksendung-gewaehrleistung
- impressum-ddg-anbieterkennzeichnung
- widerrufsbelehrung-digitale-waren-dienstleistungen
- preisangaben-pangv-gesamtpreis-grundpreis
- rechtstexte-versionierung-deployment
- grenzueberschreitender-verbrauchervertrag-rom-i-bruessel-ia

## Quellen Stand 06/2026

- §§ 305–310 BGB – Volltext gesetze-im-internet.de.
- UKlaG, UWG §§ 3a – Volltexte gesetze-im-internet.de.
- BGH zur Online-AGB-Einbeziehung – ständige Rechtsprechung; Volltexte bundesgerichtshof.de.
- EuGH C-186/16 (Andriciuc) und C-26/13 (Kasler) zur Klauselkontrolle – curia.europa.eu.
- Verbraucherrechte-RL 2011/83/EU; Klausel-RL 93/13/EWG – EUR-Lex.
- VZBV – Klagepraxis und Datenbank unwirksamer Klauseln.

## 2. `altersverifikation-jugendschutz`

**Fokus:** Altersverifikation Jugendschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG.

# Altersverifikation Jugendschutz

## Fachkern: Altersverifikation Jugendschutz
- **Spezialgegenstand:** Altersverifikation Jugendschutz wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Fernabsatz/Widerruf, PAngV, UWG, DSGVO, DDG/DSA, TDDDG, Produktsicherheit, Gewährleistung, Zahlungsdienste und Plattformrecht.
- **Entscheidende Weiche:** Trenne Shop-Frontend, Bestellstrecke, Informationspflicht, Preis, Widerruf, Mängelrecht, Werbung, Tracking und Plattform-/Marketplace-Pflichten.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Altersverifikation Jugendschutz** im Bereich **E-Commerce-Recht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** E-Commerce-Recht mit Fernabsatz, Widerruf, Preisangaben, Impressum, Datenschutz, UWG, DSA, Plattformpflichten, Produktsicherheit, BFSG und internationalem Verbraucherschutz.

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

## 3. `app-commerce-in-app-kaeufe`

**Fokus:** App-Commerce In-App-Käufe: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: BGB §§ 312 ff., 355 und 327 ff., 434 ff.; EGBGB Informationspflichten; PAngV; UWG; DDG; DSA; DSGVO; BFSG; GPSR; ElektroG/VerpackG/BattG.

# App-Commerce In-App-Käufe

## Fachkern: App-Commerce In-App-Käufe
- **Spezialgegenstand:** App-Commerce In-App-Käufe wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Fernabsatz/Widerruf, PAngV, UWG, DSGVO, DDG/DSA, TDDDG, Produktsicherheit, Gewährleistung, Zahlungsdienste und Plattformrecht.
- **Entscheidende Weiche:** Trenne Shop-Frontend, Bestellstrecke, Informationspflicht, Preis, Widerruf, Mängelrecht, Werbung, Tracking und Plattform-/Marketplace-Pflichten.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: App-Commerce In-App-Käufe** im Bereich **E-Commerce-Recht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** E-Commerce-Recht mit Fernabsatz, Widerruf, Preisangaben, Impressum, Datenschutz, UWG, DSA, Plattformpflichten, Produktsicherheit, BFSG und internationalem Verbraucherschutz.

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
