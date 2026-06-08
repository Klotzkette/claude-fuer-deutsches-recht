---
name: laienhilfe-sanktion-fachanwalt-sozialrecht
description: "Laienhilfe Sanktion Fachanwalt Sozialrecht im Plugin Fachanwalt Sozialrecht: prüft konkret Laienverstaendlicher Sozialrechts-Skill zu Sanktion, Versicherter erhielt Ablehnung der Erwerbsminderungsrente, Mandant hat Behinderung und moechte, Laienverstaendlicher Sozialrechts-Skill zu Aussteuerung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Laienhilfe Sanktion Fachanwalt Sozialrecht

## Arbeitsbereich

**Laienhilfe Sanktion Fachanwalt Sozialrecht** ordnet den Fall über die tragenden Prüfungslinien: Laienverstaendlicher Sozialrechts-Skill zu Sanktion, Versicherter erhielt Ablehnung der Erwerbsminderungsrente, Mandant hat Behinderung und moechte. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `laienhilfe-sanktion-minderung` | Laienverstaendlicher Sozialrechts-Skill zu Sanktion Minderung. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behörde, Widerspruch, Klage oder Beratung. |
| `fachanwalt-sozialrecht-erwerbsminderungsrente` | Versicherter erhielt Ablehnung der Erwerbsminderungsrente oder ist ausgesteuert und fragt nach Rentenanspruch. §§ 43 240 SGB VI. Prüfraster: volle Erwerbsminderung unter 3 Stunden taeglich teilweise unter 6 Stunden Wartezeit 5 Jahre § 50 SGB VI 3 Jahre Pflichtbeitraege in letzten 5 Jahren § 43 Abs. 1 Nr. 2 SGB VI. Berufsschutz § 240 SGB VI Jahrgaenge vor 1961. Medizinische Befundlage Gutachten. Output: Widerspruchsschriftsatz oder Klagebaustein Erwerbsminderungsrente. Abgrenzung zu fachanwalt-sozialrecht-krankengeld-aussteuerung (Übergang). |
| `fachanwalt-sozialrecht-gdb-schwerbehinderung` | Mandant hat Behinderung und moechte Schwerbehindertenausweis und Merkzeichen beantragen oder Ablehnungsbescheid anfechten. § 152 SGB IX Feststellungsverfahren Versorgungsmedizin-Verordnung. Prüfraster: GdB-Feststellung nach Versorgungsmedizinischer Grundsaetze Merkzeichen G aG H B Bl Gl RF Schwerbehindertenausweis ab GdB 50. Steuerliche und arbeitsrechtliche Vorteile. Output: Antragschreiben oder Widerspruchsbaustein GdB/Schwerbehinderung. Abgrenzung zu eingliederungshilfe-schule (Kinder) und fachanwalt-sozialrecht-erwerbsminderungsrente. |
| `laienhilfe-aussteuerung-nahtlosigkeit` | Laienverstaendlicher Sozialrechts-Skill zu Aussteuerung Nahtlosigkeit. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behörde, Widerspruch, Klage oder Beratung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGG §§ 51, 78, 87, 90, 130a, 144, 160, 183, 193, SGB I, II, III, V, VI, IX, X; § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch; § 84 SGG Klage; § 87 SGG Eilantrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `laienhilfe-sanktion-minderung`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Sanktion Minderung. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behörde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Sanktion Minderung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Sanktion Minderung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Worum es geht

Dieser Skill erklaert **Sanktion Minderung** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

## Erst sortieren

1. Welcher Bescheid, Brief, Anruf oder Termin liegt vor?
2. Von welcher Stelle kommt er: Jobcenter, Krankenkasse, Pflegekasse, Rentenversicherung, Sozialamt, Jugendamt, Berufsgenossenschaft oder Sozialgericht?
3. Welches Datum steht auf dem Schreiben und wann ist es angekommen?
4. Was will die Person erreichen: Geld, Leistung, Hilfsmittel, Pflegegrad, GdB, Fristverlaengerung, Akteneinsicht, Eilentscheidung oder einfach Verstehen?
5. Welche Belege gibt es: Atteste, Gutachten, Kontoauszuege, Mietvertrag, Bescheide, Arbeitsunfaehigkeit, Schriftwechsel?

## Arbeitsweise

- Schwierige Woerter erst in einfache Sprache uebersetzen.
- Fristen immer sichtbar ausgeben.
- Zwischen sicher, unklar und zu beweisen unterscheiden.
- Nicht beschwichtigen, wenn ein Eilantrag oder Widerspruch noetig sein kann.
- Keine falschen Versprechen machen.

## Ausgabe

**Kurz erklaert**
- Was bedeutet das Schreiben?
- Was ist das Risiko?
- Was muss als naechstes getan werden?

**Unterlagenliste**
| Unterlage | Warum wichtig? | Vorhanden? |
| --- | --- | --- |
| ... | ... | ... |

**Naechster Schritt**
Formuliere bei Bedarf einen einfachen Brief oder eine E-Mail mit klarer Bitte, Aktenzeichen, Datum, Anlagenliste und Frist.

## Fehler vermeiden

- Keine Frist verstreichen lassen.
- Telefonate direkt mit Datum, Uhrzeit und Namen notieren.
- Nie Originale ohne Kopie abgeben.
- Nicht nur Gefuehle schildern, sondern konkrete Tatsachen und Belege.
- Bei Existenznot, Wohnung, Krankenversicherung, Pflege oder Schulbegleitung immer Eilrechtsschutz mitdenken.

## Qualitaetsgate

Ist die Antwort freundlich, einfach, respektvoll und trotzdem rechtlich praezise? Sind die Begriffe aus SGB und SGG erklaert? Sind Umlaute und Namen sauber uebernommen? Sind offene Punkte sichtbar markiert?

## Sanktion / Minderung - Themenspezifika
- **Rechtsgrundlage SGB II:** §§ 31-32 SGB II (Pflichtverletzungen, Sanktionen); § 31a (Hoehe Minderung); § 31b SGB II (Dauer); § 32 SGB II (Meldeversaeumnis).
- **BVerfG-Rechtsprechung 2019 (1 BvL 7/16):** Sanktionen ueber 30 % verfassungswidrig wegen Verletzung Existenzminimum (Art. 1, 20 GG); Neuregelung 2023 angepasst; **Vollsanktion (100 % der Regelbedarfsstufe) nicht mehr zulaessig** ausser bei mehrfach wiederholten Pflichtverletzungen unter engen Voraussetzungen.
- **Sanktionsabstufung § 31a SGB II (Stand 2023):** 1. Pflichtverletzung 10 %, 2. innerhalb Jahresfrist 20 %, 3. innerhalb Jahresfrist 30 %; Dauer regelmaessig 1 Monat.
- **Meldeversaeumnis § 32 SGB II:** 10 %; auch bei mehrfach wiederholtem Meldeverstoss.
- **Anhörung § 24 SGB X zwingend** vor Sanktion - **Verletzung Anhörungspflicht = Bescheid rechtswidrig**.
- **Wichtiger Grund** § 31 I SGB II:
 - Krankheit (Attest pruefen, AU sofort einreichen).
 - Kinderbetreuung (Schliesstage Kita, Krankheit Kind).
 - Pflege Angehoeriger.
 - Verkehrshindernis ohne Verschulden.
 - Wirtschaftliche Existenzgefaehrdung durch zumutbare Arbeit (z. B. nicht kostendeckende Vergutung).
- **Eilantrag § 86b II SGG:** bei Existenzgefaehrdung Sanktion durch hoehere als 30 % oder bei Aussetzung KdU - Anordnungsanspruch (rechtswidrige Sanktion) + Anordnungsgrund (Existenzgefaehrdung).
- **Widerspruch § 84 SGG 1 Monat:** Anhörung pruefen, wichtigen Grund vortragen, Verhaeltnismaessigkeit pruefen (Atypischer Fall? Persoenliche Verhaeltnisse?).
- **Praxis-Tipp:** Bei wiederholten Sanktionen Aktivierungsplan in Frage stellen (Geeignetheit, Zumutbarkeit § 10 SGB II); bei psychischer Erkrankung Stellungnahme Hausarzt einholen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `fachanwalt-sozialrecht-erwerbsminderungsrente`

**Fokus:** Versicherter erhielt Ablehnung der Erwerbsminderungsrente oder ist ausgesteuert und fragt nach Rentenanspruch. §§ 43 240 SGB VI. Prüfraster: volle Erwerbsminderung unter 3 Stunden taeglich teilweise unter 6 Stunden Wartezeit 5 Jahre § 50 SGB VI 3 Jahre Pflichtbeitraege in letzten 5 Jahren § 43 Abs. 1 Nr. 2 SGB VI. Berufsschutz § 240 SGB VI Jahrgaenge vor 1961. Medizinische Befundlage Gutachten. Output: Widerspruchsschriftsatz oder Klagebaustein Erwerbsminderungsrente. Abgrenzung zu fachanwalt-sozialrecht-krankengeld-aussteuerung (Übergang).

# Erwerbsminderungsrente (§§ 43, 240 SGB VI)

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erwerbsminderungsrente (§§ 43, 240 SGB VI)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor EM-Renten-Bearbeitung
1. Leistungsvermögen: Unter 3 Stunden/Tag (volle EM, § 43 Abs. 2 SGB VI) oder 3-6 Stunden (teilweise EM, § 43 Abs. 1 SGB VI)?
2. Versicherungsrechtliche Voraussetzungen: 5 Jahre Wartezeit (§ 50 SGB VI) und 3 Jahre Pflichtbeiträge in den letzten 5 Jahren (§ 43 Abs. 1 Nr. 2 SGB VI)?
3. Geburtsjahrgang vor 02.01.1961? Dann Berufsschutz § 240 SGB VI prüfen.
4. Bereits Reha (§ 15 SGB VI) ohne Erfolg? Reha vor Rente-Prinzip beachten.
5. Ablehnungsbescheid vorhanden? Widerspruchsfrist 1 Monat (§ 84 SGG) gesichert?

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BSG, Urteil vom 05.06.2025 — B 5 R 17/23 R (5. Senat): Bei Konkurrenz höherer EM-Rente und niedrigerer Teil-EM-Rente im Nachzahlungszeitraum ist keine monatsweise Saldierung vorzunehmen; § 89 Abs. 1 Satz 5 SGB VI führt zu einer Gesamtsaldierung über den Nachzahlungszeitraum. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=05.06.2025&Aktenzeichen=B+5+R+17/23+R
- BSG, Urteil vom 27.03.2025 — B 5 R 16/23 R (5. Senat): Berücksichtigung von Kindererziehungs- und Berücksichtigungszeiten bei der Regelaltersrente — Auswirkungen auch auf die EM-Rentenberechnung relevant. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_27_B_05_R_16_23_R.html
- Verhandlungstermin BSG B 5 R 15/24 R vom 25.09.2025 (Überstundenabgeltung und Hinzuverdienst nach § 96a SGB VI): https://www.bsg.bund.de/SharedDocs/Verhandlungen/DE/2025/2025_09_25_B_05_R_15_24_R.html — Volltext vor Verwendung in dejure.org / openjur.de auf Rechtskraft und Entscheidungsformel prüfen.

Weitere Rechtsprechung vor Ausgabe live verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Welche Erkrankungen liegen vor (somatisch, psychisch, Kombination) — und welche Fachärzte sind behandelnd?
2. Wie viele Stunden täglich kann der Mandant noch auf dem allgemeinen Arbeitsmarkt tätig sein (Selbsteinschätzung und ärztliche Einschätzung)?
3. Ist die Mandantschaft bereits in stationärer Rehabilitation (§ 15 SGB VI) gewesen — mit welchem Entlassungsbefund?
4. Geburtsjahrgang vor dem 02.01.1961? → Berufsschutz § 240 SGB VI prüfen.
5. Versicherungsrechtliche Voraussetzungen: Fünf Jahre Wartezeit (§ 50 SGB VI) und drei Jahre Pflichtbeiträge in den letzten fünf Jahren erfüllt?
6. Liegt bereits ein Ablehnungsbescheid der Deutschen Rentenversicherung vor — mit welcher Begründung?
7. Wurde ein rentenversicherungsinternes Gutachten erstattet — wurde Akteneinsicht beantragt?
8. Sind Hinzuverdienstgrenzen relevant (§ 96a SGB VI — Mandant geringfügig beschäftigt)?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 43 Abs. 1 SGB VI | Teilweise Erwerbsminderungsrente: Leistungsvermögen 3 bis unter 6 Stunden täglich |
| § 43 Abs. 2 SGB VI | Volle Erwerbsminderungsrente: Leistungsvermögen unter 3 Stunden täglich |
| § 43 Abs. 3 SGB VI | Arbeitsmarktrente (verschlossener Teilzeitmarkt bei 3–6 Stunden) |
| § 50 SGB VI | Allgemeine Wartezeit: fünf Jahre Beitragszeiten |
| § 43 Abs. 1 S. 1 Nr. 2 SGB VI | Drei Jahre Pflichtbeiträge in den letzten fünf Jahren vor EM-Eintritt |
| § 53 SGB VI | Ausnahmen von der versicherungsrechtlichen Voraussetzung (z.B. BU vor Wartezeit) |
| § 96a SGB VI | Hinzuverdienstgrenzen bei teilweiser EM-Rente |
| § 99 SGB VI | Beginn der Rente (frühestens Rentenantrag; Rückwirkung ausgeschlossen) |
| § 102 Abs. 2 SGB VI | Befristung auf drei Jahre; Verlängerung bis Regelaltersgrenze möglich |
| § 109 SGG | Gutachten durch Arzt des Vertrauens im Klageverfahren auf Antrag |
| § 240 SGB VI | Berufsschutz (Rente wegen Berufsunfähigkeit) für Geburtsjahrgänge vor 02.01.1961 |
| § 15 SGB VI | Medizinische Rehabilitation als vorrangige Leistung |

### Leitentscheidungen (Stand Mai 2026)

| Aktenzeichen | Gericht/Datum | Tragende Aussage | Offene Fundstelle |
|---|---|---|---|
| B 5 R 17/23 R | BSG, Urteil 05.06.2025 | Bei Konkurrenz höherer voller EM-Rente und niedrigerer Teil-EM-Rente im Nachzahlungszeitraum: Gesamtsaldierung statt monatsweiser Verrechnung; § 89 Abs. 1 S. 5 SGB VI | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=05.06.2025&Aktenzeichen=B+5+R+17/23+R |
| B 5 R 16/23 R | BSG, Urteil 27.03.2025 | Kindererziehungs- und Berücksichtigungszeiten in der Rentenberechnung | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_27_B_05_R_16_23_R.html |
| B 5 R 2/24 R | BSG, Urteil 27.03.2025 | Rentenberechnung | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=27.03.2025&Aktenzeichen=B+5+R+2/24+R |

Weitere Entscheidungen vor Verwendung in dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Prüfschema (14 Schritte)

| Schritt | Inhalt | Norm |
|---|---|---|
| 1 | Versicherungsrechtliche Voraussetzungen prüfen | § 43 Abs. 1 S. 1 Nr. 2, 3 SGB VI |
| 2 | Wartezeit fünf Jahre ermitteln (inkl. Anrechnungszeiten § 58 SGB VI) | § 50 SGB VI |
| 3 | Pflichtbeiträge drei Jahre in letzten fünf Jahren vor EM-Eintritt | § 43 Abs. 1 S. 1 Nr. 2 SGB VI |
| 4 | Ausnahmen von versicherungsrechtlichen Voraussetzungen prüfen | § 53 SGB VI |
| 5 | Leistungsvermögen medizinisch quantifizieren (Stunden täglich) | § 43 Abs. 1, 2 SGB VI |
| 6 | Verschlossener Teilzeitarbeitsmarkt bei 3 bis unter 6 h | BSG-Linie "Arbeitsmarktrente" — vor Ausgabe Aktenzeichen live in dejure.org prüfen |
| 7 | Berufsschutz § 240 SGB VI bei Jahrgang vor 02.01.1961 | § 240 SGB VI |
| 8 | Summierung ungewöhnlicher Leistungseinschränkungen / qualitative Einschränkungen | BSG-Linie B 13 R / B 5 R — vor Ausgabe Aktenzeichen live in dejure.org prüfen |
| 9 | Befristung § 102 Abs. 2 SGB VI beachten | § 102 SGB VI |
| 10 | Beginn der Rente (§ 99 SGB VI — Antragsdatum) | § 99 SGB VI |
| 11 | Hinzuverdienstgrenze § 96a SGB VI klären | § 96a SGB VI |
| 12 | Sozialmedizinisches Gutachten der DRV analysieren | § 109 SGG |
| 13 | Eigenes Gutachten § 109 SGG beantragen (Vertrauensarzt) | § 109 SGG |
| 14 | Widerspruch § 84 SGG (1 Monat), Klage § 87 SGG (1 Monat) | §§ 84, 87 SGG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Erwerbsminderungsrente Widerspruch | Widerspruchsschriftsatz; Template unten |
| Variante A — Volle statt teilweise EM-Rente angestrebt | Gutachterliche Stellungnahme zur Leistungsfaehigkeit kleiner als 3h |
| Variante B — Rentenanpassung statt Neuantrag | § 48 SGB X Wesentliche Aenderung; guenstigerer Weg |
| Variante C — Berufsunfaehigkeit Privatversicherung parallel | BU-Versicherungs-Leistungsklage koordinieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Vollständige Widerspruchsbegründung

```
An die Deutsche Rentenversicherung [Träger]
Widerspruchsstelle
[Anschrift]

Versicherungsnummer: [VsNr]
betr. [Name, Geburtsdatum]

Widerspruch gegen den Bescheid vom [Datum],
zugegangen am [Datum]

Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft legen wir gegen
den oben bezeichneten Bescheid

 W i d e r s p r u c h

ein und begründen diesen wie folgt:

I. Sachverhalt

Unsere Mandantschaft [Name, Geburtsdatum] leidet seit [Datum]
an folgenden Erkrankungen:
- [Diagnose 1, ICD, behandelnder Arzt]
- [Diagnose 2, ICD, behandelnder Arzt]
- [Diagnose 3, ICD, behandelnder Arzt]

Die letzte berufliche Tätigkeit als [Beruf] wurde am [Datum]
aus gesundheitlichen Gründen aufgegeben. Seitdem besteht
volle Arbeitsunfähigkeit.

II. Versicherungsrechtliche Voraussetzungen sind erfüllt

Die allgemeine Wartezeit von fünf Jahren (§ 50 SGB VI) ist
erfüllt (Beitragszeiten von [Datum] bis [Datum], insgesamt
[X] Monate).

Die besonderen versicherungsrechtlichen Voraussetzungen des
§ 43 Abs. 1 S. 1 Nr. 2 SGB VI sind erfüllt: In den letzten
fünf Jahren vor Eintritt der Erwerbsminderung ([Zeitraum])
liegen mindestens 36 Monate Pflichtbeitragszeiten vor
(Anlage W1: Versicherungsverlauf).

III. Medizinische Voraussetzungen

Das Leistungsvermögen ist auf unter drei Stunden täglich
gesunken (volle Erwerbsminderung § 43 Abs. 2 SGB VI).
Belegt durch:
- Hausarzt Dr. [Name], Attest vom [Datum] (Anlage W2)
- Facharzt [Fachrichtung] Dr. [Name], Bericht vom [Datum]
 (Anlage W3)
- Reha-Entlassungsbericht [Klinik] vom [Datum] (Anlage W4)

Die Erkrankungen sind in ihrer Gesamtwirkung zu beurteilen
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

[Falls 3–6 Stunden angenommen wird:]
IV. Verschlossener Teilzeitarbeitsmarkt

Sollte die Beklagte lediglich ein quantitatives Leistungs-
vermögen von 3 bis unter 6 Stunden täglich annehmen, ist
die Rente wegen voller Erwerbsminderung dennoch zu gewähren.
Der Teilzeitarbeitsmarkt ist für Personen mit dem Profil
unserer Mandantschaft faktisch verschlossen (BSG, Beschl.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Stellen in dem in Betracht kommenden Bereich sind nicht
benannt worden.

[Falls Jahrgang vor 02.01.1961:]
V. Berufsschutz § 240 SGB VI

Unsere Mandantschaft hat Geburtsjahrgang [Jahr] und fällt
damit in den Anwendungsbereich des § 240 SGB VI. Sie ist
als [Beruf] im bisherigen Beruf nicht mehr zu sechs Stunden
täglich einsetzbar. Eine sozial und gesundheitlich zumutbare
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
worden.

Wir beantragen:
1. Den ablehnenden Bescheid aufzuheben.
2. Unserer Mandantschaft ab [Datum] eine Rente wegen voller
 Erwerbsminderung nach § 43 Abs. 2 SGB VI zu gewähren.
3. Akteneinsicht in die vollständige Verwaltungsakte
 (§ 25 SGB X), insbesondere das sozialmedizinische
 Gutachten.

Mit freundlichen Grüßen
[Fachanwalt/-anwältin für Sozialrecht]
```

### Baustein 2 — Antrag auf Gutachten nach § 109 SGG

```
An das Sozialgericht [Ort]

Az. S [X] R [Az]

In dem Rechtsstreit [Name] ./. Deutsche Rentenversicherung [Träger]

beantragen wir:

Gemäß § 109 SGG wird ein Gutachten über die Arbeitsfähigkeit
der Klägerin / des Klägers durch folgende Gutachterin / folgenden
Gutachter eingeholt:

[Name des Gutachters]
[Facharzt für Neurologie/Psychiatrie/Innere Medizin]
[Praxisadresse]

Beweisfrage:
1. An welchen Erkrankungen leidet die Klägerin / der Kläger?
2. Welches quantitative Leistungsvermögen auf dem allgemeinen
 Arbeitsmarkt besteht in zeitlicher Hinsicht täglich?
3. Welche qualitativen Einschränkungen bestehen?

Die Auslagen des Gutachters trägt die Klägerin / der Kläger
vorläufig.

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Position | Träger | Beweismittel |
|---|---|---|
| Versicherungsrechtliche Voraussetzungen | Kläger | Versicherungsverlauf DRV, Beitragsnachweise |
| Quantitatives Leistungsvermögen (< 3 h) | Kläger | Ärztliche Berichte, Gutachten, Entlassungsberichte |
| Verschlossener Teilzeitarbeitsmarkt | DRV (Arbeitsmarktrente-Linie) | DRV muss benennbare Stellen darlegen, sonst Arbeitsmarktrente |
| Berufsschutz § 240 (bisheriger Beruf) | Kläger | Arbeitsvertrag, Tätigkeitsbeschreibung |
| Zumutbare Verweisungstätigkeit | DRV | Konkrete Verweisungstätigkeit benennen und zumutbar begründen |
| Befristung sachlich gerechtfertigt | DRV | Gutachten, Prognose |

---

## Fristen und Verjährung

| Frist | Grundlage | Inhalt |
|---|---|---|
| Ein Monat | § 84 Abs. 1 SGG | Widerspruchsfrist nach Bekanntgabe Bescheid |
| Ein Monat | § 87 Abs. 1 SGG | Klagefrist nach Widerspruchsbescheid |
| Ab Antragsdatum | § 99 SGB VI | Rentenbeginn; Rückwirkung auf Antragsdatum |
| Drei Monate | § 88 Abs. 1 SGG | Untätigkeitsklage wenn kein Widerspruchsbescheid |
| Vier Jahre | § 44 SGB X | Rücknahme rechtswidriger Ablehnungen |

---

## Typische Gegenargumente der Rentenversicherung

| DRV-Argument | Rechtliche Gegenstrategie |
|---|---|
| "Teilzeitmarkt offen" | Konkrete Stellen benennen lassen; ohne Stellenbenennung greift Arbeitsmarktrente nach BSG-Linie (vor Ausgabe Aktenzeichen in dejure.org prüfen) |
| "Versicherungsrechtliche Voraussetzungen fehlen" | Beitragszeiten exakt nachweisen; Ausnahmen § 53 SGB VI prüfen |
| "Eigenes Gutachten widerspricht" | § 109 SGG: Antrag auf Gegengutachten; Widersprüche im Gutachten angreifen |
| "Rehabilitation vorrangig" | § 15 SGB VI: Reha bereits durchgeführt und ohne Erfolg; DRV muss konkrete Maßnahmen benennen |
| "Befristung auf 3 Jahre korrekt" | Bei dauerhafter Erkrankung Verlängerung beantragen; Unbefristung ab Regelaltersgrenze-Nähe |
| "Hinzuverdienst zu hoch" | § 96a SGB VI: Grenzwerte exakt berechnen; Differenzierung Brutto/Netto |

---

## Streitwert / Kosten

| Position | Richtwert |
|---|---|
| Streitwert EM-Rente (Vollrente) | 13-facher monatlicher Rentenwert (§ 42 GKG i.V.m. § 9 ZPO analog) |
| Gerichtskosten SG | Kostenfrei § 183 SGG |
| Anwaltskosten | PKH/LSG prüfen; sonst ca. EUR 1200 bis 2000 (erste Instanz) |
| § 109-Gutachten | EUR 800 bis 3000; Vorschuss Kläger, Erstattung bei Erfolg |
| LSG-Berufung | Streitwert > EUR 750 (§ 144 Abs. 1 SGG) |

---

## Strategische Empfehlung

| Fallkonstellation | Empfehlung |
|---|---|
| DRV-Ablehnung, Gutachten intern ungünstig | § 109 SGG-Antrag eigener Gutachter; inhaltliche Fehler des internen Gutachtens angreifen |
| Nachzahlung mit konkurrierender Teil-EM | BSG 05.06.2025 — B 5 R 17/23 R beachten: Gesamtsaldierung statt monatsweise Verrechnung; Bescheidberechnung gezielt nachprüfen |
| Berufsschutz § 240 | Bisherigen Beruf und Verweisungstätigkeiten präzise definieren |
| Versicherungszeiten-Lücke | § 53 SGB VI-Ausnahmen prüfen; Anrechnungszeiten nachweisen |
| Klage anhängig | Parallele Leistungssicherung (Bürgergeld, Krankengeld) sicherstellen |

---

## Häufige Schwachstellen im DRV-Bescheid

1. Sozialmedizinisches Gutachten allein nach Aktenlage, kein persönlicher Vorstellungstermin
2. Psychiatrische Diagnosen nicht vollständig erfasst
3. Schmerzsyndrome im Belastbarkeitsprofil unterbewertet
4. Wegefähigkeit nicht geprüft
5. Summierung ungewöhnlicher Leistungseinschränkungen nicht thematisiert
6. Falsche Anwendung Drei-Stunden-Sechs-Stunden-Grenze
7. Leistungsfall zu spät angesetzt → Drei-aus-Fünf-Regel scheitert

## Beweisanträge

- Beiziehung der DRV-Verwaltungsakte vollständig
- Sachverständigengutachten Fachgebiet [Innere Medizin / Orthopädie / Psychiatrie]
- Vernehmung der behandelnden Ärzte als Zeugen / sachverständige Zeugen
- Beiziehung Berentungsgutachten DGUV (wenn berufsgenossenschaftliche Vorgeschichte)

---

## Anschluss-Skills

- `fachanwalt-sozialrecht-widerspruch-sozialleistung` — allgemeiner Widerspruchsprozess
- `fachanwalt-sozialrecht-sgb-ii-bescheid` — Bürgergeld während des Verfahrens
- `fachanwalt-sozialrecht-long-covid-bk-anerkennung-bg` — bei Long-COVID als Auslöser
- `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` — Vergleichsstrategie SG

## Quellen (Stand Mai 2026)

- BSG 05.06.2025 — B 5 R 17/23 R (Gesamtsaldierung Nachzahlung): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=05.06.2025&Aktenzeichen=B+5+R+17/23+R
- BSG 27.03.2025 — B 5 R 16/23 R (Kindererziehungszeiten): https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_27_B_05_R_16_23_R.html
- BSG-Verhandlung 25.09.2025 — B 5 R 15/24 R (Überstundenabgeltung als Hinzuverdienst): https://www.bsg.bund.de/SharedDocs/Verhandlungen/DE/2025/2025_09_25_B_05_R_15_24_R.html
- Weitere Rechtsprechung vor Verwendung live in dejure.org / openjur.de / bsg.bund.de verifizieren.

---

## 3. `fachanwalt-sozialrecht-gdb-schwerbehinderung`

**Fokus:** Mandant hat Behinderung und moechte Schwerbehindertenausweis und Merkzeichen beantragen oder Ablehnungsbescheid anfechten. § 152 SGB IX Feststellungsverfahren Versorgungsmedizin-Verordnung. Prüfraster: GdB-Feststellung nach Versorgungsmedizinischer Grundsaetze Merkzeichen G aG H B Bl Gl RF Schwerbehindertenausweis ab GdB 50. Steuerliche und arbeitsrechtliche Vorteile. Output: Antragschreiben oder Widerspruchsbaustein GdB/Schwerbehinderung. Abgrenzung zu eingliederungshilfe-schule (Kinder) und fachanwalt-sozialrecht-erwerbsminderungsrente.

# GdB-Feststellung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `GdB-Feststellung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Antrag und Klage zur Feststellung Grad der Behinderung (GdB).

## 1) Antrag § 152 SGB IX

### Antrag

- Beim Versorgungsamt / zuständiger Behörde
- Formulare im Land verschieden
- Arzt-Auskuenfte und Befunde einreichen

### Verfahren

- 4-6 Monate Bearbeitungszeit typisch
- Sachverständigen-Gutachten bei Bedarf
- Bescheid mit GdB-Höhe und Merkzeichen

## 2) GdB-Bewertung

### Versorgungsmedizin-Verordnung

- Versorgungsmedizinische Grundsätze (VMG)
- Anhaltspunkte für ärztliche Begutachtung
- Tabelle in Anhang VMG

### Einzel-GdB pro Funktionssystem

- Innere Organe
- Bewegungsapparat
- Nervensystem
- Psyche
- Sinnesorgane

### Gesamt-GdB

- Nicht Summe der Einzel-GdB
- Wechselwirkungs-Prüfung
- Typisch 10er-Stufen

## 3) Merkzeichen

| Merkzeichen | Bedeutung | Voraussetzungen |
|---|---|---|
| **G** | erhebliche Gehbehinderung | Gehfähigkeit < 2 km eingeschraenkt |
| **aG** | außergewoehnliche Gehbehinderung | Rollstuhl / dauernde Mobilitäts-Beschraenkung |
| **H** | hilflos | Pflege-Bedarf täglich |
| **B** | Begleitung erforderlich | im OePNV |
| **Bl** | blind | Sehfähigkeit < 1/50 |
| **Gl** | gehoerlos | Hörverlust > 80 % |
| **RF** | Rundfunkbeitrag-Ermassigung | bestimmte schwere Behinderungen |

## 4) Vorteile Schwerbehindertenausweis (ab GdB 50)

- Steuerlicher Behindertenpauschbetrag
- Kündigungs-Schutz § 168 SGB IX (Zustimmung Integrationsamt)
- Zusatz-Urlaub 5 Tage
- Vorzeitige Altersrente
- Vorteile Parkplatz (mit aG)
- Steuer-Reduktion Kfz

## 5) Klage

### Schritt 1 — Bescheid-Prüfung

- Welche Funktionssysteme erfasst?
- GdB-Höhe begründet?
- Merkzeichen vollständig?

### Schritt 2 — Widerspruch 1 Monat

- An Versorgungsamt
- Detaillierte Begründung mit Befunden

### Schritt 3 — Sachverständigen-Gutachten

- Im Klage-Verfahren angeordnet
- Kostenfrei für Antragsteller im SG
- Wiederholung möglich

### Schritt 4 — Klage SG

- Frist 1 Monat nach Widerspruchsbescheid
- Beim Sozialgericht
- Streitwert nach Vorteil-Erhöhung

## 6) Verschlechterungs-Antrag

- Bei Änderung der Gesundheit
- Neuer Antrag jederzeit
- Bei Verbesserung: Rückforderung Versorgungsamt möglich

## 7) Typische Fehler

1. **Befunde unvollständig eingereicht**
2. **Einzel-GdB falsch nach VMG bewertet**
3. **Wechselwirkung nicht beachtet**
4. **Merkzeichen-Prüfung übersehen**
5. **Frist 1 Monat versäumt**

## 8) BSG-Linien und aktuelle Rechtsprechung (Stand Mai 2026)

- BSG, Urteil vom 12.12.2024 — B 9 SB 2/24 R: GdB-Bewertung bei Diabetes mellitus Typ 1 im Kindesalter; Anwendung der VersMedV Teil B Nr. 15.1. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2024/2024_12_12_B_09_SB_02_24_R.html
- BSG, Urteil vom 09.03.2023 — B 9 SB 8/21 R: Merkzeichen aG; Maßstab Gehfähigkeit im öffentlichen Verkehrsraum, nicht in idealisierten Umgebungen. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2023/2023_03_09_B_09_SB_08_21_R.html
- BSG, Urteil vom 09.03.2023 — B 9 SB 1/22 R: Merkzeichen aG; Pflicht zur Berücksichtigung von Wechselsituationen im Alltag. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2023/2023_03_09_B_09_SB_01_22_R.html
- Stand Mai 2026: Spezifische B 9 SB-Entscheidungen des Jahres 2025/2026 sind in dejure.org/bsg.bund.de zum Zeitpunkt der Skill-Aktualisierung nicht als veröffentlichte Senatsentscheidungen mit Volltext zugänglich; vor Verwendung Aktenzeichen-Recherche unter https://www.bsg.bund.de/SharedDocs/Entscheidungen/ durchführen.

## Widerspruchsbausteine

```
I. Einzel-GdB nicht ausgewiesen — formelles Defizit

Der Bescheid weist nur den Gesamt-GdB aus. Eine Prüfung ist mangels
ausg ewiesener Einzelwerte und Wechselwirkungen nicht möglich. Wir
beantragen die Auflistung aller Einzel-GdB-Werte und die Begründung
der Gesamt-GdB-Bildung (Akteneinsicht parallel beantragt).

II. Funktionsstörung [Name] zu niedrig bewertet

Der Einzel-GdB für [Diagnose] wurde mit [X] angesetzt. Nach VersMedV
Teil B Nr. [X.Y] ist bei [konkreter Beschreibung] ein GdB von [Y] zu
vergeben. Die aktuellen Befunde [Arzt, Datum] dokumentieren [Befund].

III. Merkzeichen G — Prüfung 2-km-30-Min-Kriterium

Die Versorgungsaärztin hat ohne konkrete Prüfung das Merkzeichen G
abgelehnt. Tatsächlich kann die Mandantin nicht zwei Kilometer in
dreizig Minuten zurüclegen (VersMedV Teil D Nr. 1).
Belegt durch aerztliches Attest Dr. [Name] (Anlage W [Nr]).

IV. Gesamt-GdB fehlerhafte Bildung

Bei [Diagnose A] GdB [X] und [Diagnose B] GdB [Y] mit
[wechselseitiger Beeinflussung] ist nach VersMedV Teil A Nr. 3 ein
Gesamt-GdB von [Z] zu bilden.

V. Antrag

Wir beantragen die Feststellung eines GdB von [X] sowie der Merkzeichen
[G/aG/B/Bl/Gl/H/RF] ab Antragsdatum [TT.MM.JJJJ], hilfsweise ab Datum
des angegriffenen Bescheids.
```

## Beweisanträge

- Beiziehung der Verwaltungsakte des Versorgungsamts
- Aktualisierte Befundberichte aller behandelnden Ärzte
- Sachverständigengutachten Fachrichtung [Neurologie / Orthopädie / Psychiatrie]
- Bei Merkzeichen G/aG — Gehstreckenprüfung durch Sachverständigen

## Triage — kläre vor dem Widerspruch

1. Liegen alle aktuellen Befundberichte vor — insbesondere psychiatrische Diagnosen und Schmerzgutachten?
2. Sind alle Einzel-GdB-Werte im Bescheid ausgewiesen, oder nur ein Gesamt-GdB ohne Einzelaufschlüsselung?
3. Welche Merkzeichen wurden beantragt, welche abgelehnt? (G, aG, B, Bl, H, RF, TBl)
4. Datum des Erstbescheids: läuft die Ein-Monats-Frist (§ 84 SGG) noch?
5. Hat der Mandant steuerliche Auswirkungen (§ 33b EStG Pauschbetrag) und Schwerbehindertenrechtsstatus bereits genutzt?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

- `fachanwalt-sozialrecht-krankengeld-aussteuerung` — bei AU-Bezug
- `fachanwalt-sozialrecht-orientierung` — Triage
- `betreuungsrecht` — bei Erwachsenen-Schutzfrage
- `fristenbuch-sozialrecht` — Fristenverwaltung
- `akteneinsicht-anfordern` — Versorgungsamt-Akte mit versorgingsärztlicher Stellungnahme

## 4. `laienhilfe-aussteuerung-nahtlosigkeit`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Aussteuerung Nahtlosigkeit. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behörde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Aussteuerung Nahtlosigkeit

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Aussteuerung Nahtlosigkeit` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Worum es geht

Dieser Skill erklaert **Aussteuerung Nahtlosigkeit** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

## Erst sortieren

1. Welcher Bescheid, Brief, Anruf oder Termin liegt vor?
2. Von welcher Stelle kommt er: Jobcenter, Krankenkasse, Pflegekasse, Rentenversicherung, Sozialamt, Jugendamt, Berufsgenossenschaft oder Sozialgericht?
3. Welches Datum steht auf dem Schreiben und wann ist es angekommen?
4. Was will die Person erreichen: Geld, Leistung, Hilfsmittel, Pflegegrad, GdB, Fristverlaengerung, Akteneinsicht, Eilentscheidung oder einfach Verstehen?
5. Welche Belege gibt es: Atteste, Gutachten, Kontoauszuege, Mietvertrag, Bescheide, Arbeitsunfaehigkeit, Schriftwechsel?

## Arbeitsweise

- Schwierige Woerter erst in einfache Sprache uebersetzen.
- Fristen immer sichtbar ausgeben.
- Zwischen sicher, unklar und zu beweisen unterscheiden.
- Nicht beschwichtigen, wenn ein Eilantrag oder Widerspruch noetig sein kann.
- Keine falschen Versprechen machen.

## Ausgabe

**Kurz erklaert**
- Was bedeutet das Schreiben?
- Was ist das Risiko?
- Was muss als naechstes getan werden?

**Unterlagenliste**
| Unterlage | Warum wichtig? | Vorhanden? |
| --- | --- | --- |
| ... | ... | ... |

**Naechster Schritt**
Formuliere bei Bedarf einen einfachen Brief oder eine E-Mail mit klarer Bitte, Aktenzeichen, Datum, Anlagenliste und Frist.

## Fehler vermeiden

- Keine Frist verstreichen lassen.
- Telefonate direkt mit Datum, Uhrzeit und Namen notieren.
- Nie Originale ohne Kopie abgeben.
- Nicht nur Gefuehle schildern, sondern konkrete Tatsachen und Belege.
- Bei Existenznot, Wohnung, Krankenversicherung, Pflege oder Schulbegleitung immer Eilrechtsschutz mitdenken.

## Qualitaetsgate

Ist die Antwort freundlich, einfach, respektvoll und trotzdem rechtlich praezise? Sind die Begriffe aus SGB und SGG erklaert? Sind Umlaute und Namen sauber uebernommen? Sind offene Punkte sichtbar markiert?

## Aussteuerung / Nahtlosigkeit - Themenspezifika
- **Rechtsgrundlage:** § 48 SGB V (Krankengeld-Hoechstdauer 78 Wochen) i.V.m. § 145 SGB III (Nahtlosigkeit ALG bei Erwerbsminderung); auch SGB VI (EM-Rente) ist Anschlussleistung.
- **Aussteuerung:** Krankengeld endet nach 78 Wochen wegen derselben Krankheit (Bezugsrahmen 3 Jahre); Krankenkasse muss rechtzeitig Reha- oder Rentenantrag-Aufforderung machen (§ 51 SGB V) - sonst Aussteuerung verschoben.
- **Nahtlosigkeitsregelung § 145 SGB III:** ALG-Anspruch auch bei festgestellter Erwerbsminderung unter 15 h pro Woche bis zur Entscheidung der DRV ueber EM-Rente; Vermeidung "Niemand-Zustand" zwischen Krankengeld-Ende und Rentenbescheid.
- **Voraussetzung Nahtlosigkeit:**
 - Letzter Tag Krankengeldbezug oder vergleichbare Leistung,
 - **Verfuegbarkeit reduziert** auf weniger als 15 h/Woche,
 - Anwartschaftszeit ALG erfuellt (§ 142 SGB III: 12 Monate Beitragszeit in den letzten 30 Monaten).
- **Antragspflicht** Versicherter bei Krankenkasse / Bundesagentur für Arbeit; § 60 SGB I Mitwirkungspflicht.
- **Rente vs. ALG-Nahtlosigkeit:** ALG ist subsidiaer; sobald EM-Rente bewilligt, Verrechnung; bei Ablehnung EM bleibt ALG.
- **Eilrechtsschutz § 86b SGG** bei Verweigerung Nahtlosigkeits-ALG (Existenzminimum); ggf. Hilfe Jobcenter/Sozialamt parallel beantragen.
- **Praxis-Tipp:** Beratungstermin bei DRV vor Aussteuerung; medizinische Stellungnahme behandelnde Aerzte zur Leistungsfaehigkeit für Reha- bzw. Rentenantrag; Anwartschafts-Aufrechterhaltung pruefen, weiterhin Krankenversicherung sichern (KV-Pflicht ALG-Bezieher § 5 I Nr. 2 SGB V).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
