---
name: tk-regulierungsakte-tk-aktenzugang
description: "TK Regulierungsakte TK Aktenzugang: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TK Regulierungsakte TK Aktenzugang

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **TK Regulierungsakte TK Aktenzugang** im Plugin Bundesnetzagentur Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-regulierungsakte-nummernverwaltung-stellungnahme-entwurf` | Nummernverwaltung: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `tk-regulierungsakte-rufnummernmissbrauch-stellungnahme-entwurf` | Rufnummernmissbrauch: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht. |
| `aktenzugang-geschaeftsgeheimnisse-schwaerzung` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Aktenzugang Geschäftsgeheimnisse Schwärzung. |
| `beschwerde-verbraucher-unternehmen-verband` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Beschwerde Verbraucher Unternehmen Verband. |

## Arbeitsweg

Im Plugin Bundesnetzagentur-Verfahren gilt für **TK Regulierungsakte TK Aktenzugang**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-regulierungsakte-nummernverwaltung-stellungnahme-entwurf`

**Fokus:** Nummernverwaltung: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.


# TK-Regulierungsakte: Nummernverwaltung — Stellungnahme-Entwurf

## Fachkern: TK-Regulierungsakte: Nummernverwaltung — Stellungnahme-Entwurf
- **Spezialgegenstand:** TK-Regulierungsakte: Nummernverwaltung — Stellungnahme-Entwurf - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** TKG, TDDDG, EECC-Rahmen, Frequenz-/Rufnummernzuteilung, Universaldienst, Marktregulierung, Missbrauchsaufsicht, Kundenschutz und BNetzA-Schlichtung.
- **Spezifische Weiche:** Prüfe zuerst, ob es um Endkundenrechte, Zugang/Interconnection, Frequenzen, Rufnummern, Sicherheit/Resilienz oder Marktregulierung geht; davon hängen Formular, Beschlusskammer, Beiladung und Rechtsweg ab.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
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

## 2. `tk-regulierungsakte-rufnummernmissbrauch-stellungnahme-entwurf`

**Fokus:** Rufnummernmissbrauch: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: TKG/Frequenzrecht/Nummernrecht.


# TK-Regulierungsakte: Rufnummernmissbrauch — Stellungnahme-Entwurf

## Fachkern: TK-Regulierungsakte: Rufnummernmissbrauch — Stellungnahme-Entwurf
- **Spezialgegenstand:** TK-Regulierungsakte: Rufnummernmissbrauch — Stellungnahme-Entwurf - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** TKG, TDDDG, EECC-Rahmen, Frequenz-/Rufnummernzuteilung, Universaldienst, Marktregulierung, Missbrauchsaufsicht, Kundenschutz und BNetzA-Schlichtung.
- **Spezifische Weiche:** Prüfe zuerst, ob es um Endkundenrechte, Zugang/Interconnection, Frequenzen, Rufnummern, Sicherheit/Resilienz oder Marktregulierung geht; davon hängen Formular, Beschlusskammer, Beiladung und Rechtsweg ab.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
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

## 3. `aktenzugang-geschaeftsgeheimnisse-schwaerzung`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Aktenzugang Geschäftsgeheimnisse Schwärzung.


# Aktenzugang, Geschäftsgeheimnisse, Schwärzung bei der Bundesnetzagentur

## Zweck und Anwendungsfall
Dieser Skill steuert die anwaltliche Arbeit am Schnittpunkt von Akteneinsicht und Geheimnisschutz in Verfahren der Bundesnetzagentur (BNetzA). Typische Konstellationen: Antrag eines Wettbewerbers auf Einsicht in die Marktanalyse- oder Entgeltakte einer Beschlusskammer; Verlangen der BNetzA, Kostendaten oder Vertragsentwürfe vorzulegen; Streit über die Reichweite der Schwärzung im Tenor oder in den Anlagen eines Beschlusses; Konflikt zwischen § 29 VwVfG, § 71 TKG, § 71 EnWG, § 67 PostG, § 75 ERegG und §§ 17 ff. GeschGehG. Der Skill ist auf alle Sektoren der BNetzA anwendbar (TK, Energie, Post, Eisenbahn, Digital Services).

## Eingaben
- Verfahrensart und Beschlusskammer (BK1 TK Allgemein, BK2 Nummern, BK3 Marktanalyse, BK4 Entgelte, BK6/7/8/9 Energie, BK10 Post, BK11 Anti-Discrimination Office Telekommunikation).
- Rolle: Antragsteller, betroffenes Unternehmen, beigeladener Wettbewerber, Verband, Verbraucher.
- Konkretes Verlangen (Einsicht in Antragsschrift, Kostenkalkulation, Marktdaten, interne Stellungnahme).
- Schon erfolgte Schwärzungen und deren Begründung.
- Frist (Stellungnahme, Widerspruch, Eilantrag).

## Rechtsrahmen
- § 29 VwVfG (allgemeine Akteneinsicht im Verwaltungsverfahren).
- § 71 TKG 2021 (Verfahrensvorschriften BNetzA, Akteneinsicht, Geheimnisschutz).
- § 71 EnWG (Verfahren vor Beschlusskammern, Geheimnisschutz).
- § 67 PostG 2024 (Verfahren).
- § 75 ERegG (Verfahren der BNetzA als Regulierungsbehörde Eisenbahn).
- § 134 BNetzAG (Aufgaben und Befugnisse).
- §§ 17–19 GeschGehG (Definition und prozessualer Schutz von Geschäftsgeheimnissen; Geheimhaltungsstreitverfahren).
- § 99 VwGO (in-camera-Verfahren bei Vorlageverweigerung).
- Art. 339 AEUV (unionsrechtliches Berufsgeheimnis), Art. 5 DSA-VO, Art. 84 TK-Kodex-RL.

## Ablauf

1. **Verfahrensstand klären.**
 - Beschlusskammer und Az. (Format z. B. BK3-23-XXX-XX).
 - Stand der Konsultation gem. § 12 TKG bzw. § 56 EnWG.
 - Anstehende Anhörung, Termin der Beschlusskammer, parallele Bußgeldverfahren.
 - Vorgeschichte: Antrag, Marktanalyse, Konsultation, Notifikation an EU-Kommission Art. 32 EECC.

2. **Schutzinteresse identifizieren.** Welche Daten sind streng vertraulich?
 - Kostenrechnung, Nachfragerstruktur, Margen.
 - Identität von Whistleblowern, IT-Sicherheitsdaten.
 - Vertragsentwürfe und unterzeichnete Verträge.
 - Trennung in: Geschäftsgeheimnis i. S. v. § 2 Nr. 1 GeschGehG, personenbezogene Daten (Art. 4 Nr. 1 DSGVO), behördliches Beratungsgeheimnis, sicherheitsrelevante Daten (§ 165 TKG).

3. **Schwärzungsstrategie.** Drei Versionsstufen:
 - Vollversion für die Beschlusskammer.
 - Geschwärzte Version für die Akteneinsicht der Beigeladenen.
 - Ggf. weiter reduzierte Version für die Öffentlichkeit (Online-Stellung des Beschlusses).

4. **Begründungspflicht erfüllen.** Pro geschwärzter Passage:
 - Konkret darlegen, warum gerade dieser Wert oder dieser Satz Geheimnis ist.
 - Wettbewerbsrelevanz beziffern.
 - Pauschale Schwärzungen werden von der BNetzA und vom VG Köln regelmäßig zurückgewiesen.

5. **Akteneinsichtsantrag formulieren oder abwehren.**
 - Antragsteller: konkrete Aktenteile bezeichnen, Verfahrensbezug darlegen.
 - Geheimnisinhaber: differenziert widersprechen, Alternativvorschläge (Zusammenfassung, gerundete Werte, Bandbreitenangaben).
 - Bei Beigeladenen-Antrag: Anhörung des Geheimnisinhabers ist Standard und muss verlangt werden, falls unterblieben.

6. **In-camera-Mechanismen.**
 - Bei Vorlageverweigerung Antrag nach § 99 Abs. 2 VwGO an den Fachsenat des OVG/BVerwG.
 - Im verwaltungsbehördlichen Verfahren: faktischer in-camera-Vortrag in der Beschlusskammer.

7. **Rechtsschutz.**
 - Eilantrag nach § 123 VwGO oder § 80 Abs. 5 VwGO beim VG Köln (sachlich zuständig nach § 51 Abs. 1 Nr. 7 VwGO für BNetzA-Sachen).
 - Im TK-Bereich ggf. unmittelbar OVG Münster nach § 233 TKG.
 - Beschwerde § 146 VwGO mit substantiierter Beschwerdebegründung binnen Monatsfrist (bei Eilbeschluss 2 Wochen).

## Mustertexte

- **Antrag auf Akteneinsicht nach § 29 VwVfG i. V. m. § 71 TKG.** Bestandteile: Bezeichnung des Verfahrens, Bezeichnung der gewünschten Aktenteile, Rolle des Antragstellers, Verfahrensbezug, Anwaltszustellungsbevollmächtigung.
- **Schwärzungstabelle.** Spalten: Seite, Zeile, geschwärzter Inhalt, Schutzkategorie (Geschäftsgeheimnis, personenbezogene Daten, Sicherheitsdaten), Norm, Begründung in einem Satz.
- **Widerspruch gegen Akteneinsicht.** Inhalte: Geheimnisqualität, Wettbewerbsrelevanz, fehlende mildere Mittel, Bezug zu BNetzA-Praxis BK4 in Entgeltverfahren, Hinweis auf § 17 GeschGehG.
- **Klage beim VG Köln gegen die Anordnung der Offenlegung** als anfechtbare Verfahrenshandlung (Streit über Isolation der Maßnahme prüfen; § 44a VwGO-Sperre beachten).
- **Antrag auf einstweilige Anordnung § 123 VwGO** zur Verhinderung der vollendeten Tatsachen vor der Offenlegung; Glaubhaftmachung des wirtschaftlichen Schadens.

## Quellenpflicht

- BNetzA-Beschlüsse als Az. BK3-23-XXX-XX bzw. BK4-23-XXX-XX nur generisch; konkretes Az. vom Anwender zu verifizieren über die Konsultationsdatenbank der BNetzA.
- VG Köln und OVG Münster als Instanz nennen, konkrete Entscheidungen nur mit Datum, Az. und Fundstelle; nicht aus dem Modellwissen erfinden.
- BVerwG zur § 99 VwGO-Praxis nur mit verifiziertem Az.
- EuGH zu Art. 339 AEUV und zum Schutz vertraulicher Geschäftsinformationen mit Datum und Rechtssachen-Nr.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat

- Schwärzungstabelle als Anlage (Spalten: Seite, Zeile, Inhalt, Schutzkategorie, Norm, Begründung).
- Schriftsatz mit klarer Gliederung: Sachverhalt, Antrag, Begründung, Anlagen.
- Risikoampel: grün (Schwärzung tragfähig), gelb (Begründung schwach, Nachbesserung nötig), rot (Schwärzung wird voraussichtlich aufgehoben).
- Versions-Übersicht (Vollversion vs. Beigeladenen-Version vs. Öffentlichkeits-Version) mit Pflege-Vermerk.

## Beispiele

- **Entgeltverfahren TK.** Wettbewerber X verlangt Einsicht in die Kostenkalkulation der Y AG im Entgeltverfahren BK4-25-XXX-XX. Ergebnis: Bandbreitenoffenlegung, Schwärzung der Einzelwerte, Begründung über § 71 Abs. 1 TKG.
- **DSA-Verfahren.** Verbraucherverband verlangt Einsicht in die Stellungnahme eines Plattformbetreibers im DSA-Verfahren. Ergebnis: Offenlegung der rechtlichen Argumentation, Schwärzung von Nutzerzahlen und Sicherheitsdetails.
- **Energie-Anreizregulierung.** Energieversorger weigert sich, der BNetzA Effizienzwerte für die Anreizregulierung vorzulegen. Ergebnis: Vorlage unter Anordnung der Geheimhaltung, in-camera-Sichtung durch BK4 oder BK9.
- **Eisenbahnregulierung.** EVU verlangt Einsicht in das Schienennetz-Benutzungsbedingungen-Entwurfsdokument (vor Konsultation). Ergebnis: Offenlegung in Konsultationsphase, Schwärzung der internen Kalkulation.
- **Post-Universaldienst.** Mitbewerber verlangt Einsicht in die Kostenkalkulation der Deutsche Post AG zur Briefporto-Genehmigung. Ergebnis: Bandbreitenoffenlegung.

## Verhältnis zu anderen Skills im Plugin

- Verzahnung mit `anhoerung-auskunftsbeschluss-fristenplan`: jede Stellungnahme an die BNetzA muss zugleich die Schwärzungs-Strategie mitdenken.
- Verzahnung mit Marktdefinitions- und Entgeltskills (BK3, BK4) im TK-Sektor.
- Verzahnung mit dem DSA-Auskunfts- und Beschwerde-Komplex bei Plattformverfahren.
- Verzahnung mit dem Eisenbahn-Trassenzugang-Skill bei Beschwerdeverfahren § 66 ERegG.

## Häufige Fehler

- Pauschalschwärzung ohne Einzelbegründung führt zur Aufhebung durch die Beschlusskammer.
- Mehrfach-Versionen unsauber gepflegt, sodass die ungeschwärzte Version versehentlich in die Beigeladenen-Akte gelangt.
- Versäumte Anhörung des Geheimnisinhabers bei Drittantrag, was die Maßnahme nach § 45 VwVfG heilbar oder nach § 46 VwVfG unbeachtlich macht.
- Schwärzung von Tatsachen, die bereits in der Konsultationsphase öffentlich diskutiert wurden (Verlust des Geheimnischarakters).
- Verkennen, dass § 44a VwGO einer isolierten Klage gegen Verfahrenshandlungen Grenzen setzt.

## Qualitätsgate

Vor Versand prüfen:
- Sind alle Schwärzungen begründet?
- Ist die Frist gewahrt?
- Liegt eine Vollmacht im Original vor?
- Wurde der Geheimnisinhaber angehört (bei Antragsstellung durch Dritte)?
- Ist die Eilbedürftigkeit ggf. dargelegt?
- Liegen mehrere Versionen unterscheidbar vor (Wasserzeichen, Versionsnummer, Stempel)?

## 4. `beschwerde-verbraucher-unternehmen-verband`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Beschwerde Verbraucher Unternehmen Verband.


# Beschwerde bei der Bundesnetzagentur: Verbraucher, Unternehmen, Verband

## Zweck und Anwendungsfall
Dieser Skill steuert die Beschwerdearbeit bei der Bundesnetzagentur in den Rollen Verbraucher, Unternehmen und Verband. Die BNetzA betreibt eine Vielzahl gesetzlich angeordneter Beschwerde- und Schlichtungsstellen. Anwaltliche Praxis muss präzise zwischen formloser Beschwerde, Schlichtungsverfahren, Aufsichtsanzeige, Antrag auf Einleitung eines Beschlusskammerverfahrens und Auskunfts-Beschwerde unterscheiden. Anwendbar in: TK (Rufnummernmissbrauch, Rufnummernunterdrückung, Universaldienst, Endkundenrechte §§ 51 ff. TKG), Energie (Netzanschluss, Messstellen, Smart Meter), Post (Universaldienst, Postlaufzeiten), Eisenbahn (Diskriminierung Trassenzugang § 66 ERegG), DSA (Beschwerden gegen Plattformen).

## Eingaben
- Rolle des Mandanten: Verbraucher, Unternehmen, Verband (qualifizierte Einrichtung § 4 UKlaG, Verbraucherzentrale, BVDW, BNE, vzbv).
- Sektor und konkrete Norm.
- Gegnerunternehmen (TK-Anbieter, Netzbetreiber, Postdienstleister, EVU/EIU, Online-Plattform).
- Beschwerdegegenstand mit Tatsachenkern.
- Vorprozessuale Schritte (Schlichtung, vorgerichtliche Aufforderung).
- Frist (Verbraucherrechte häufig kurz nach § 56 TKG; Verjährung § 195 BGB).

## Rechtsrahmen

- § 68 TKG (Beschwerde-/Schlichtungsstelle bei der BNetzA, ehemals § 47a TKG-aF).
- § 51 ff. TKG (Verbraucherschutz im TK-Markt; Vertragslaufzeiten, Kündigungsregeln, Anbieterwechsel).
- §§ 4, 5 UKlaG i. V. m. § 3 UWG (Verbandsklagebefugnis).
- § 31 EnWG (Streitbeilegungsverfahren BNetzA).
- § 24 EnWG (Beschlusskammer auf Anrufung).
- § 9 PostG 2024 (Schlichtung im Postbereich; Universaldienstpflichten).
- § 66 ERegG (Beschwerde EVU gegen EIU).
- Art. 53 DSA i. V. m. § 18 DDG (Beschwerderecht gegen Plattformen).
- § 80 GWB (zivile Verbandsklage als Parallelweg).
- § 14 UWG-Klagebefugnis qualifizierter Wirtschaftsverbände.

## Ablauf

1. **Beschwerdetyp wählen.**
 - Schlichtungsverfahren (außergerichtlich, verbraucherbezogen, kostenfrei).
 - Förmliche Aufsichts-/Verfahrensanzeige (Beschlusskammer leitet von Amts wegen ein Verfahren ein).
 - Anrufung der Streitbeilegungsstelle Energie (§ 31 EnWG).
 - Beschwerde im Eisenbahnbereich (§ 66 ERegG) für Unternehmen.

2. **Adressat klären.**
 - BNetzA-Verbraucherservice (Mainz).
 - Schlichtungsstelle Telekommunikation (Bonn).
 - Schlichtungsstelle Energie (Berlin).
 - Beschlusskammer der zuständigen Sparte (BK1–BK11).
 - Eisenbahn-Spartenkammer (konkrete BK-Bezeichnung vom Anwender zu verifizieren).

3. **Sachverhalt schreiben.**
 - Knapper, chronologischer Sachvortrag.
 - Tatsachenkern in 1–3 Seiten.
 - Belege als Anlagen (Verträge, Rechnungen, Korrespondenz, Bestätigungs-Mails, Bescheide).
 - Bei Massenphänomenen (Ping-Anrufe, irreführende Werbung): Vorlage strukturierter Tabelle.

4. **Antrag formulieren.** Konkretes Ziel: Unterlassen, Erstattung, Vertragsanpassung, Verhängung eines Bußgelds, Untersagung gem. § 192 TKG.

5. **Verbandsfunktion belegen.** Bei Verbänden: Eintragung in der Liste qualifizierter Einrichtungen (§ 4 UKlaG), Klagebefugnis, kollektive Betroffenheit der Verbraucherinnen und Verbraucher.

6. **Parallelweg.** Zivilklage gegen Anbieter trotz BNetzA-Beschwerde möglich; keine Sperrwirkung. Bei DSA-Bezug parallel Art. 21-Streitbeilegung erwägen.

7. **Akten- und Eingangsverfolgung.** Eingangsbestätigung, Verfahrensnummer, regelmäßige Sachstandsanfrage (max. 4–6 Wochen).

8. **Rechtsschutz gegen Untätigkeit.**
 - Untätigkeitsklage § 75 VwGO beim VG Köln.
 - Bei Verbandsanträgen ggf. § 42 Abs. 2 VwGO-Prüfung (drittschützende Norm?).
 - Aktivlegitimation der qualifizierten Einrichtung folgt aus § 4 UKlaG.

## Mustertexte

- **Verbraucher-Beschwerde TK.** Anschreiben mit Vertragspartner, Vertragsnummer, Sachverhalt, Antrag, Anlagen.
- **Verbands-Beschwerde DSA.** Bezug zur Plattform, behauptete Pflichtverletzung (z. B. Art. 14 DSA Allgemeine Geschäftsbedingungen, Art. 16 DSA Notice-and-Action), Belege, Antrag auf Einleitung eines Verfahrens nach § 18 DDG.
- **Unternehmens-Beschwerde Eisenbahn** nach § 66 ERegG: Beschwerdeführer, Beschwerdegegner, Diskriminierung, Antrag auf vorläufige Anordnung § 68 ERegG.
- **Verband-Beschwerde Energie** nach § 31 EnWG-Streitbeilegung: kollektive Betroffenheit, Bezug auf strukturelle Marktverstöße.
- **Post-Beschwerde** zur Universaldienstpflicht und Briefzustellung.

## Quellenpflicht

- BNetzA-Jahresberichte (öffentlich abrufbar) als Praxisbelege.
- Az. von BNetzA-Streitfällen nur generisch; konkrete Verfahren vom Anwender zu verifizieren.
- VG Köln zu BNetzA-Beschwerdeverfahren nur mit Datum und Az.
- Schlichtungsstelle TK (Veröffentlichungen) und Schlichtungsstelle Energie (Berichte).
- Zitierweise gemäß `references/zitierweise.md`.

## Ausgabeformat

- Beschwerdeschrift (2–6 Seiten).
- Anlagenverzeichnis nach Beweisstruktur (Verträge, Korrespondenz, Bestätigungs-Mails, Bescheide).
- Risikoampel und Erfolgsaussichts-Memo (intern für den Mandanten).
- Bei Verbänden: Übersicht weiterer parallel laufender Verfahren zur Stärkung der Verbandsthese.

## Beispiele

- **Rufnummernmissbrauch.** Verbraucher reklamiert Ping-Anrufe. Schlichtungsstelle TK, parallel Anzeige bei der BNetzA wegen § 67 TKG.
- **Eisenbahn-Diskriminierung.** Unternehmen rügt diskriminierenden Trassenzugang gegen die DB InfraGO. Beschwerde nach § 66 ERegG bei der BNetzA (zuständige BK10 in der Eisenbahn-Sparte; konkrete Beschlusskammer vom Anwender zu verifizieren).
- **DSA-Verbandsbeschwerde.** vzbv-Beschwerde gegen Online-Plattform wegen fehlender Beschwerdesysteme (Art. 20 DSA). Verfahren beim DSC (BNetzA).
- **Energie-Streitbeilegung.** Endkunde rügt unzulässige Lieferantenwechsel-Verzögerung. Schlichtungsstelle Energie (§ 31 EnWG).
- **Postlaufzeit.** Verband rügt systematisch verzögerte Briefzustellung. Anzeige bei der BNetzA als Postaufsicht (BK10/Postregulierung).

## Verhältnis zu anderen Skills im Plugin

- Bei DSA-Plattform-Beschwerden Routing in `digital-services-dsa-beschwerde-plattform`.
- Bei Eisenbahn-Konstellationen Routing in `eisenbahn-beschwerde-evu-gegen-infrastrukturbetreiber`.
- Bei TK-Schlichtung Schnittstelle zum TK-Endkundenrechte-Skill.
- Bei Energie-Streitbeilegung Schnittstelle zum Energie-Skill (Streitbeilegungsstelle § 31 EnWG).

## Häufige Fehler

- Verband nicht als qualifizierte Einrichtung eingetragen; Beschwerdebefugnis fehlt.
- Sachverhalt zu schmal: ohne strukturierte Belege beendet die BNetzA das Verfahren formlos.
- Verkennen, dass das Schlichtungsverfahren regelmäßig zustimmungspflichtig durch den Anbieter ist (vgl. § 68 Abs. 2 TKG-Strukturen).
- Untätigkeit zu schnell als Untätigkeitsklage ausgelegt; Frist § 75 VwGO beachten (Regel: 3 Monate).
- Zivilklage und BNetzA-Beschwerde widersprüchlich vortragen.

## Qualitätsgate

Vor Versand prüfen:
- Klagebefugnis (insbesondere bei Verbänden) tragfähig?
- Antrag konkret?
- Belege vollständig?
- Frist gewahrt?
- Parallelweg (Zivilklage) reflektiert?
- Vergleichsbereitschaft des Mandanten dokumentiert?
