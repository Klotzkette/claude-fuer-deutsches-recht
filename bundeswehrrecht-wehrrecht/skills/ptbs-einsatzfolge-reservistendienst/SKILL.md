---
name: ptbs-einsatzfolge-reservistendienst
description: "Ptbs Einsatzfolge Reservistendienst: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ptbs Einsatzfolge Reservistendienst

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ptbs Einsatzfolge Reservistendienst** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ptbs-einsatzfolge-beweisfuehrung` | PTBS Einsatzfolge Beweisführung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `reservistendienst-dienstleistungspflicht` | Reservistendienst und Dienstleistungspflicht: prüft SG §§ 60–69, Heranziehungsbescheid, Freistellung und Rechtsbehelfe. Norm-/Quellenanker: SG §§ 60–69, WPflG, UhSiG. |
| `sanitaetsdienst-heilfuersorge` | Sanitätsdienst und Heilfürsorge: prüft truppenärztliche Versorgung, Leistungsumfang, Ablehnung und Rechtsbehelfe. Norm-/Quellenanker: BBesG § 70, SVG §§ 69–74, SG § 30. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Ptbs Einsatzfolge Reservistendienst**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ptbs-einsatzfolge-beweisfuehrung`

**Fokus:** PTBS Einsatzfolge Beweisführung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# PTBS als Einsatzfolge – Beweisführung

## Fachkern: PTBS als Einsatzfolge – Beweisführung
- **Spezialgegenstand:** PTBS als Einsatzfolge – Beweisführung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die posttraumatische Belastungsstörung (PTBS) ist eine anerkannte psychische Erkrankung, die durch Extremereignisse im Einsatz ausgelöst werden kann (ICD-10 F43.1, ICD-11 6B40). Im Versorgungsrecht der Bundeswehr ist PTBS als Wehrdienstbeschädigung/Einsatzunfall anerkannt, wenn der Kausalzusammenhang nach den Versorgungsmedizinischen Grundsätzen wahrscheinlich gemacht ist. Der Skill ordnet Diagnose, Belastungsanamnese, Gutachten und Verfahren.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Diagnose (ICD-Code) wurde gestellt? Welche Fachärzte (Bundeswehrkrankenhaus, Vertragsarzt)?
- Welches Belastungsereignis (Gefecht, Anschlag, Tod von Kameraden, Verletzung Zivilist, Unfall, Bedrohung)?
- Zeitliche Lücke zwischen Belastung und Diagnose?
- Sekundärfolgen (Depression, Suchterkrankung, Suizidalität, Erwerbsunfähigkeit)?
- Versicherungsmedizinische Bewertung schon erfolgt? GdS festgesetzt?
- Streitiger Punkt: Diagnose, Kausalität oder GdS-Höhe?

## Rechtlicher Rahmen

- § 81 SVG: Wehrdienstbeschädigung, einschließlich psychischer Schäden.
- § 81a SVG: Einsatzunfall – PTBS als Folge des Einsatzgeschehens.
- § 81e SVG: Einmalige Entschädigung bei GdS 50 v.H. und mehr.
- § 81b SVG: Erweiterte Heilbehandlung, Pflege.
- Versorgungsmedizinische Grundsätze (VMG) – Bewertung psychischer Störungen.
- ICD-10 F43.1, ICD-11 6B40 – diagnostische Standards.
- BSG-Rechtsprechung zur Kausalität psychischer Schäden – ständige Rechtsprechung.
- Schnittstelle § 1 SGB IX (Teilhabe), Heilfürsorge der Bw.

## / Schritt für Schritt

1. **Diagnose sichern.** Facharzt für Psychiatrie/Psychotherapie oder Psychotraumatologie; ICD-Code; Symptomerfassung (Intrusionen, Vermeidung, Hyperarousal, kognitive Veränderungen).
2. **Belastungsanamnese.** Einsatzberichte, OPLAN, Kameradenberichte, eigene Tagebücher, ggf. Funkprotokolle.
3. **Kausalkette aufbauen.** Belastungsereignis -> Symptombeginn -> Chronifizierung. Auch verzögerte PTBS (delayed-onset) anerkannt.
4. **Antrag** beim BAPersBw auf Anerkennung als WDB/Einsatzunfall mit allen Befunden.
5. **Begutachtung.** Vorzugsweise traumatherapeutisch erfahrener Gutachter. Eigene Stellungnahme/Gegengutachten.
6. **GdS-Bewertung.** Nach VMG: Belastungssymptome, soziale/berufliche Funktionseinschränkung.
7. **Berufsförderung und Reha** parallel beantragen (BFD/SVG).
8. **Widerspruch und Klage** bei Unterbewertung (1 Monat).

## Trade-off-Matrix

| Konstellation | Strategie |
| --- | --- |
| Klares Kampfereignis, akute Symptome | Sofortantrag mit Befunden |
| Delayed-onset Jahre später | Belastungsanamnese plus Zeugen plus Tagebücher |
| Komorbide Depression/Sucht | Differenzialdiagnose; Mitverursachung |
| Diagnose abgelehnt | Zweitgutachten; spezialisiertes Zentrum |
| GdS zu niedrig | VMG-konforme Substantiierung |

## Praxistipps

- BVerwG/BSG: Wahrscheinlichkeitsmaß genügt. Vollbeweis nur der Schädigung (Diagnose) und der haftungsbegründenden Tatsache (Einsatzereignis).
- Bundeswehr eigene Trauma-Zentren (BwKrhs Berlin, Hamburg, Westerstede). Gutachten dort ist nicht zwingend bindend.
- Tagebücher und Briefe aus dem Einsatz sind häufig stärkste Beweismittel.
- Suizidversuch oder -tod als Folge der PTBS: Hinterbliebenenversorgung (§ 88 SVG) kann ausgelöst werden.
- BFD-Berufsförderung kombiniert mit Heilfürsorge – Reha vor Rente.

## Mustertexte

**Antrag auf Anerkennung PTBS als Einsatzunfall:**
"Beim BAPersBw beantrage ich die Anerkennung einer PTBS (ICD-10 F43.1) als Einsatzunfall nach § 81a SVG. Belastungsereignis: Einsatz [Bezeichnung], [Datum/Ereignis]. Diagnose: durch Dr. [Name], BwKrhs [Standort], am [Datum]. Symptome: [...]. Beweismittel: 1. ärztlicher Bericht. 2. Einsatzbefehl / OPLAN-Auszug. 3. Kameradenbericht Stbsf [Name]. 4. Tagebuch des Mandanten. Beantragt werden: GdS 50 v.H. nach VMG, einmalige Entschädigung § 81e SVG, Heilbehandlung § 81b SVG."

**Widerspruch gegen Ablehnung:**
"Die Ablehnung stützt sich auf fehlende Kausalität. Tatsächlich genügt nach BSG-Rechtsprechung Wahrscheinlichkeit. Die Symptomatik begann zeitnah zum Einsatzereignis (Sept. [Jahr]). Delayed-onset-PTBS ist nach VMG ausdrücklich anerkannt. Es wird ein traumatherapeutisches Gutachten beantragt; vorgeschlagen werden Dr. [Name] oder das Trauma-Zentrum [...]."

## Typische Fehler

- Belastungsereignis pauschal, nicht datiert/dokumentiert.
- Diagnose von nicht spezialisiertem Arzt – verteidigungsschwach im Widerspruch.
- Komorbide Diagnosen unterschätzen – mindern den GdS.
- VMG-Tabelle nicht zitiert – Bewertung scheint pauschal.
- § 81e SVG-Einmalentschädigung nicht ausdrücklich beantragt.

## Querverweise

- soldatenversorgungsgesetz-beschaedigtenversorgung
- einsatzunfall-wehrdienstbeschaedigung
- einsatz-unfall-versorgung-dokumentenplan
- aerztliche-begutachtung-dienstfaehigkeit
- sanitaetsdienst-heilfuersorge
- dienstunfaehigkeit-entlassung-zurruhesetzung

## Quellen Stand 06/2026

- SVG §§ 81, 81a, 81b, 81e – Volltext gesetze-im-internet.de.
- VMG (Versorgungsmedizinische Grundsätze) – BMAS-Publikation.
- ICD-10 F43.1, ICD-11 6B40 – WHO-Veröffentlichungen.
- BSG zu Kausalität psychischer Schäden – ständige Rechtsprechung.
- BAPersBw – Verwaltungspraxis.
- Bundeswehrkrankenhäuser – Standorte und Fachabteilungen (bundeswehr.de).

## 2. `reservistendienst-dienstleistungspflicht`

**Fokus:** Reservistendienst und Dienstleistungspflicht: prüft SG §§ 60–69, Heranziehungsbescheid, Freistellung und Rechtsbehelfe. Norm-/Quellenanker: SG §§ 60–69, WPflG, UhSiG.

# Reservistendienst und Dienstleistungspflicht

## Fachkern: Reservistendienst und Dienstleistungspflicht
- **Spezialgegenstand:** Reservistendienst und Dienstleistungspflicht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Reservisten unterliegen der Dienstleistungspflicht nach SG §§ 60 ff. Heranziehungen zu freiwilligem Reservistendienst oder im Spannungsfall durch Heranziehungsbescheid.

Praktische Fragen: Freistellung durch Arbeitgeber, Unterhaltssicherung, Beschwerden gegen Heranziehung.

## Einschlägige Normen und Quellen

- §§ 60–69 SG — Reservistendienst
- § 81 SG — Heranziehungsbescheid
- WPflG — im Spannungsfall
- UhSiG — Unterhaltssicherung
- ArbPlSchG — Freistellung Arbeitgeber

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Freiwillige Übung oder Pflicht-Heranziehung?
- Liegt Heranziehungsbescheid vor?
- Freistellung durch Arbeitgeber gesichert?
- Unterhaltssicherung beantragt?
- Soll die Heranziehung angefochten werden?

## Prüf- und Arbeitslogik

### Schritt 1 — Dienstleistungspflicht §§ 60–69 SG

Reservisten: Verpflichtung zu Wehrübungen und Dienstleistungen im Spannungsfall.
Umfang: abhängig von Laufbahn und früherem Status.
Freiwillige Wehrübung: auf Antrag, Zustimmung erforderlich.
Pflichtige Heranziehung: Heranziehungsbescheid.

### Schritt 2 — Heranziehungsbescheid anfechten

WBO-Beschwerde gegen Heranziehungsbescheid: 1 Monat.
Vollzugsaussetzung § 9 WBO beantragen.
Gründe: besondere persönliche Härtegründe, rechtliche Fehler im Bescheid.
TDG: gerichtliche Entscheidung.

### Schritt 3 — Arbeitgeber und Freistellung

ArbPlSchG § 1: Arbeitgeber muss freistellen.
Kündigungsverbot § 4 ArbPlSchG.
Unterhaltssicherung UhSiG: Verdienstausfall ausgleichen.
Arbeitgebererstattung: §§ 13–14 ArbPlSchG.

### Schritt 4 — Besonderheiten

Beamte: ggf. Beurlaubung durch Dienstherrn.
Selbstständige: UhSiG gesondert.
Auslandseinsatz: AVZ und SVG-Versorgungsansprüche wie Aktivsoldaten.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Reservistendienst-Arten und Ansprüche
- Checkliste: Heranziehungsbescheid anfechten
- Muster: Antrag Vollzugsaussetzung Heranziehungsbescheid

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — §§ 60–69 SG
- https://www.gesetze-im-internet.de/uhsig/ — UhSiG
- https://www.gesetze-im-internet.de/arb-plschg/ — ArbPlSchG
- https://www.bundeswehr.de/de/soldat-werden/reservisten

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `sanitaetsdienst-heilfuersorge`

**Fokus:** Sanitätsdienst und Heilfürsorge: prüft truppenärztliche Versorgung, Leistungsumfang, Ablehnung und Rechtsbehelfe. Norm-/Quellenanker: BBesG § 70, SVG §§ 69–74, SG § 30.

# Sanitätsdienst und Heilfürsorge

## Fachkern: Sanitätsdienst und Heilfürsorge
- **Spezialgegenstand:** Sanitätsdienst und Heilfürsorge. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Der Bundeswehr-Sanitätsdienst stellt truppenärztliche Versorgung für aktive Soldaten sicher. Leistungsumfang: ambulante und stationäre Behandlung, Arzneimittel, Heil- und Hilfsmittel.

Probleme: Ablehnung von Behandlungen, Wahlleistungen, externe Spezialisten, WDB-Heilbehandlung nach Entlassung.

## Einschlägige Normen und Quellen

- BBesG § 70 — Heilfürsorge
- SVG §§ 69–74 — Heilbehandlung WDB
- SG § 30 — Fürsorgepflicht
- ZSanDBw — Sanitätsdienstvorschriften
- GOÄ/GOZ — Gebührenordnungen

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Aktiver Soldat oder entlassener (WDB)?
- Welche Leistung wurde abgelehnt?
- Wahlleistung oder Regelleistung?
- Spezialist extern erforderlich?
- WDB-Heilbehandlung nach Entlassung?

## Prüf- und Arbeitslogik

### Schritt 1 — Truppenärztliche Grundversorgung

Ambulant: Sanitätszentren (SanZ), Truppenärzte.
Stationär: Bundeswehrkrankenhäuser (BwKrhs).
Überweisung für Spezialisten: Genehmigungspflicht.
Notfall: jede Behandlung, Kosten nachträglich geltend machen.

### Schritt 2 — Leistungsumfang und Genehmigung

Notwendige Behandlungen: erstattungsfähig ohne Einschränkung.
Wahlleistungen (Chefarzt, Einzelzimmer): Antrag, Zuzahlung.
Externe Spezialisten: Überweisung und Genehmigung erforderlich.
Ablehnung: WBO-Beschwerde.

### Schritt 3 — WDB-Heilbehandlung § 69 SVG

Anerkannte WDB: Heilbehandlung auf Bundeskosten, zeitlich unbegrenzt.
Antrag: BAPersBw.
Keine Vorabgenehmigung bei Notfall.
Abgrenzung: WDB-Folge vs. eigenständige neue Erkrankung.

### Schritt 4 — Rechtsbehelfe

Ablehnung Heilfürsorge: WBO-Beschwerde, dann ggf. VG.
SVG-Heilbehandlung: Widerspruch + Sozialgericht.
PKV-Streit nach Entlassung: Zivilgericht.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Leistungsarten Sanitätsdienst vs. SVG-Heilbehandlung
- Checkliste: Genehmigung externer Spezialist
- Muster: Antrag WDB-Heilbehandlung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bbesg/ — § 70 BBesG
- https://www.gesetze-im-internet.de/svg/ — §§ 69–74 SVG
- https://www.bundeswehr.de/de/organisation/streitkraefte/sanitaetsdienst

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
