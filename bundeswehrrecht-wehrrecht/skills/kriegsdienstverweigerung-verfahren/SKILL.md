---
name: kriegsdienstverweigerung-verfahren
description: "Kriegsdienstverweigerung Verfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kriegsdienstverweigerung Verfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kriegsdienstverweigerung Verfahren** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kriegsdienstverweigerung-verfahren` | Kriegsdienstverweigerung Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `rechtsbeistand-im-disziplinarverfahren` | Rechtsbeistand im Disziplinarverfahren: prüft Verteidigungsrecht § 91 WDO, Bestellungsverfahren, Verteidigungsstrategien und Kosten. Norm-/Quellenanker: WDO §§ 91–92, BRAO. |
| `truppendienstgericht-zustaendigkeit-verfahren` | Truppendienstgericht Zuständigkeit Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Kriegsdienstverweigerung Verfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kriegsdienstverweigerung-verfahren`

**Fokus:** Kriegsdienstverweigerung Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Kriegsdienstverweigerung – Verfahren

## Fachkern: Kriegsdienstverweigerung – Verfahren
- **Spezialgegenstand:** Kriegsdienstverweigerung – Verfahren. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Das Recht auf Kriegsdienstverweigerung aus Gewissensgründen ist in Art. 4 III GG verankert. Soldaten, Wehrpflichtige, Reservisten und Bewerber können das Recht in Anspruch nehmen. Verfahren und Voraussetzungen regelt das Kriegsdienstverweigerungsgesetz (KDVG). Anerkannte Verweigerer leisten Dienst nach dem Zivildienstgesetz (für Wehrpflichtige in einer Spannungs-/Verteidigungslage) oder werden aus dem Wehrdienst entlassen (Soldaten). Der Skill ordnet Antragsweg, Gewissensprüfung und Folgen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Aktueller Status (Wehrpflichtiger, Reservist, Soldat auf Zeit, Berufssoldat, FWDL)?
- Beweggründe (religiös, ethisch, weltanschaulich, politisch-moralisch)?
- Bisherige Vorgänge (frühere Anträge, Verfahren beim Bundesamt für Familie und zivilgesellschaftliche Aufgaben/BAFzA bzw. Vorgängerbehörden)?
- Ist die Verweigerung absolut oder bezogen auf einen bestimmten Konflikt (sog. Situationsverweigerung)?
- Welche Frist (zB Zeitsoldat während des Wehrdienstverhältnisses, Bewerber vor Einstellung)?
- Welche dienstliche Lage (Heranziehung, Einsatzbefehl, Übung)?

## Rechtlicher Rahmen

- Art. 4 III GG: Niemand darf gegen sein Gewissen zum Kriegsdienst mit der Waffe gezwungen werden.
- KDVG: Verfahren der Anerkennung als Kriegsdienstverweigerer.
- § 1 KDVG: Recht der Verweigerung.
- § 2 KDVG: Schriftlicher Antrag, Begründung, persönliche Anhörung.
- § 5 KDVG: Anerkennungsverfahren – Anhörung durch die zuständige Stelle.
- § 7 KDVG: Wirkung der Anerkennung – Entlassung des Soldaten oder Wegfall der Heranziehung.
- BVerfGE zu Art. 4 III GG: Gewissensentscheidung ist verbindlich, wenn ernsthaft, sittlich begründet und absolut.
- § 1 WPflG i.V.m. KDVG: Wehrpflichtige.
- § 1 SG i.V.m. KDVG: Soldaten und Reservisten.

## / Schritt für Schritt

1. **Statusbestimmung.** Antragsweg differenziert je nach Status. Soldat: Antrag beim Vorgesetzten, weiter ans BAFzA / Wehrdienstrechtsamt. Reservist: vor Heranziehung. Wehrpflichtiger: bei Musterung oder im Wehrdienst.
2. **Antragsschrift.** Schriftlich, persönlich verfasst, Begründung der Gewissensentscheidung. Lebensgeschichte, prägende Erfahrungen, ethische/religiöse Grundlagen, Folgen für eigene Lebensführung.
3. **Beweismittel.** Zeugenangaben, Zertifikate (Friedensdienst, religiöse Tätigkeit), persönliche Korrespondenz.
4. **Anhörung.** Persönliche Anhörung Pflicht. Recht auf Beistand. Fragen zur Genese der Entscheidung, Glaubhaftigkeit, Konsistenz.
5. **Bescheid abwarten.** Bei Anerkennung: Entlassung des Soldaten (§ 7 KDVG), Wegfall der Heranziehung des Reservisten / Wehrpflichtigen.
6. **Rechtsbehelfe.** Widerspruch, Klage Verwaltungsgericht (KDVG-Verfahren ist Verwaltungsverfahren, kein WBO-Verfahren).
7. **Folgen für Versorgung.** Anerkennung schließt Heilfürsorge und WDB-Ansprüche aus dienstzeitabhängigen Verlusten ein – Einzelfall prüfen.

## Trade-off-Matrix

| Konstellation | Antrag stellen | Alternative |
| --- | --- | --- |
| Reine Gewissensnot | Anerkennung KDVG | Befehlsverweigerung im Einzelfall (§ 11 II SG) |
| Situationsverweigerung | KDVG nicht statthaft (Rspr. eng) | Versetzung, Entlassung auf Antrag |
| Zeitsoldat vor Vertragsende | Anerkennung + Entlassung | Antrag § 55 SG |
| Reservist heranziehbar | KDVG vor Heranziehung | Widerspruch gegen Heranziehung |

## Praxistipps

- Antragsbegründung muss "absolute" Verweigerung dokumentieren – Situationsablehnung führt häufig zur Ablehnung.
- BVerfG: Innere Konsistenz und Glaubhaftigkeit reichen – kein "Beweis" des Gewissens, aber überzeugende Darlegung.
- Bei Soldaten ist die Wirkung primär die Entlassung; während des Verfahrens grundsätzlich kein Anspruch auf Dienstbefreiung – aber Einsatzbefreiung möglich (Einzelfall).
- Bei Soldaten auf Zeit kann Rückforderung der Ausbildungskosten drohen – Skill "ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten" parallel prüfen.
- Anhörung schriftlich vorbereiten, ggf. Probeanhörung mit Anwalt durchgehen.

## Mustertexte

**KDV-Antrag eines Soldaten:**
"Hiermit erkläre ich gemäß Art. 4 III GG, § 1 KDVG, dass ich den Kriegsdienst mit der Waffe aus Gewissensgründen verweigere. Persönliche Begründung: 1. Lebensgeschichte: [...]. 2. Entwicklung der Gewissensentscheidung: [...]. 3. Konsequenzen für meine Lebensführung: [...]. 4. Bekenntnisse / Mitgliedschaften: [...]. Ich beantrage die Anerkennung als Kriegsdienstverweigerer sowie meine Entlassung aus dem Soldatenverhältnis (§ 7 KDVG)."

**Beistand-Vollmacht für Anhörung:**
"Ich bevollmächtige Herrn/Frau [Name] als Beistand zur Teilnahme an der mündlichen Anhörung nach § 5 KDVG. Der Beistand ist zur Akteneinsicht und zur Stellung von Anträgen befugt."

## Typische Fehler

- Antragsschrift formelhaft / Textbaustein – Anhörung deckt Unglaubhaftigkeit auf.
- Situationsverweigerung als KDV – wird regelmäßig abgelehnt.
- Folgen Versorgung/Ausbildungskostenrückforderung nicht bedacht.
- Anhörung ohne Beistand – ungeschickte Antworten begründen Ablehnung.
- KDV als reine Strategie zur Entlassung – Glaubhaftigkeit wird kritisch geprüft, Risiko Rückforderung.

## Querverweise

- soldatengesetz-rechtsstellung-grundpflichten
- gehorsam-befehl-und-rechtswidriger-befehl
- befehl-verweigern-gewissensnot-rechtswidrigkeit
- entlassung-auf-eigenen-antrag
- ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten
- reservistendienst-dienstleistungspflicht

## Quellen Stand 06/2026

- Art. 4 III GG.
- KDVG – Volltext gesetze-im-internet.de.
- BVerfG zu Art. 4 III GG – ständige Rechtsprechung; Volltexte bundesverfassungsgericht.de.
- BVerwG zur Gewissensentscheidung – ständige Rechtsprechung (Az. nach Verifikation).
- BAFzA – Verwaltungspraxis und Verfahrensmerkblatt (bafza.de).

## Spezialplugin

Für KDV-Fälle ab 2026, insbesondere Antrag über BAPersBw, § 13 KDVG n. F., aktive Soldaten, Reservisten, Untätigkeit und Gewissensbegründung, vorrangig das Spezialplugin `kriegsdienstverweigerung-wehrdienst` verwenden. Dieser Skill bleibt als Routing im Bundeswehrrecht erhalten.

## 2. `rechtsbeistand-im-disziplinarverfahren`

**Fokus:** Rechtsbeistand im Disziplinarverfahren: prüft Verteidigungsrecht § 91 WDO, Bestellungsverfahren, Verteidigungsstrategien und Kosten. Norm-/Quellenanker: WDO §§ 91–92, BRAO.

# Rechtsbeistand im Disziplinarverfahren

## Fachkern: Rechtsbeistand im Disziplinarverfahren
- **Spezialgegenstand:** Rechtsbeistand im Disziplinarverfahren. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Das Recht auf einen Verteidiger im gerichtlichen Disziplinarverfahren ist ein grundlegendes Verfahrensrecht. § 91 WDO: Soldat kann Rechtsanwalt oder sonstigen Rechtsbeistand bestellen.

Ein erfahrener Verteidiger kennt die Besonderheiten des Truppendienstgerichts (Richter sind Berufsrichter + ehrenamtliche Richter aus der Truppe).

## Einschlägige Normen und Quellen

- § 91 WDO — Recht auf Verteidiger
- § 92 WDO — Wahlverteidiger, Pflichtverteidiger
- WDO §§ 18–21 — Akteneinsicht des Verteidigers
- BRAO — Rechtsanwälte
- RDGEG — Rechtsdienstleistungsgesetz

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Wann wurde Rechtsbeistand bestellt oder soll er bestellt werden?
- Ist es ein einfaches oder gerichtliches Disziplinarverfahren?
- Hat der Soldat bereits Unterlagen an den Verteidiger übergeben?
- Gibt es Prozesskostenhilfe oder Kostentragung durch Dienstherrn?
- Welche Verfahrensstadien stehen an?

## Prüf- und Arbeitslogik

### Schritt 1 — Verteidigungsrecht § 91 WDO

§ 91 WDO: Soldat kann sich in gerichtlichem Disziplinarverfahren eines Verteidigers bedienen.
Zeitpunkt: spätestens nach Einleitungsverfügung, besser früher (Untersuchungsverfahren).
Pflichtverteidiger: im WDO-Verfahren nicht vorgesehen; Wahlverteidiger.

### Schritt 2 — Aufgaben des Verteidigers

Akteneinsicht §§ 18–21 WDO.
Teilnahme an Beweisaufnahme (Untersuchungsführer).
Anwesenheit bei Hauptverhandlung.
Beweisantragsrecht.
Schlussplädoyer § 92 WDO.

### Schritt 3 — Kostenregelung

Kosten des Verteidigers: grundsätzlich der Soldat.
Bei Freispruch: Erstattung durch Bundeskasse (§ 114 WDO analog).
Prozesskostenhilfe: im WDO-Verfahren eingeschränkt möglich.
Kostentragung bei Einstellung: analog § 114 WDO.

### Schritt 4 — Strategische Punkte

Frühe Mandatsübernahme: vor Vernehmungen!
Aussageverweigerung empfehlen bis Akteneinsicht.
Untersuchungsverfahren: Fehler hier beeinflussen Hauptverhandlung.
Verzögerungsstrategie: Ausschlussfrist § 17 WDO prüfen.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Checkliste: Erste Schritte als Verteidiger im WDO-Verfahren
- Tabelle: Verfahrensstadien und Verteidigungsoptionen
- Muster-Vollmacht für WDO-Verfahren

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wdo_2002/ — WDO §§ 91–92
- https://www.bverwg.de — BVerwG Wehrdienstsenat
- https://openjur.de
- https://www.brak.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `truppendienstgericht-zustaendigkeit-verfahren`

**Fokus:** Truppendienstgericht Zuständigkeit Verfahren: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Truppendienstgericht – Zuständigkeit und Verfahren

## Fachkern: Truppendienstgericht – Zuständigkeit und Verfahren
- **Spezialgegenstand:** Truppendienstgericht – Zuständigkeit und Verfahren. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Truppendienstgerichte (Süd in München, Nord in Münster) sind erstinstanzlich zuständig für gerichtliche Disziplinarverfahren gegen Soldaten und für Anträge auf gerichtliche Entscheidung nach WBO. Sie sind eigenständige Bundesgerichte unter Vorsitz von Berufsrichtern, ergänzt durch Beisitzer aus der Truppe. Der Skill ordnet ein, wann TDG zuständig ist, wie das Verfahren abläuft und welche Rechtsmittel bestehen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Verfahrensart liegt vor: WBO-Antrag, gerichtliches Disziplinarverfahren, vorläufige Maßnahmen?
- Truppenteil und Standort des Mandanten – welches TDG (Süd/Nord) ist örtlich zuständig?
- Bisheriger Verfahrensstand: Anhörung erfolgt? Disziplinarverfügung? Beschwerdebescheid?
- Liegt ein Antrag auf Einleitung des gerichtlichen Disziplinarverfahrens vor?
- Frist bereits gewahrt (2 Wochen nach § 17 WBO, § 42 WDO)?
- Mündliche Verhandlung beantragt oder schriftliches Verfahren?

## Rechtlicher Rahmen

- §§ 68 ff. WDO: Errichtung und Besetzung der Truppendienstgerichte – Süd und Nord, jeweils mit Vorsitzendem Richter, weiteren Richtern und ehrenamtlichen Beisitzern aus der Truppe.
- § 70 WDO: Geschäftsverteilung – Truppendienstkammern.
- §§ 76 ff. WDO: Einleitung des gerichtlichen Disziplinarverfahrens durch Einleitungsbehörde (BMVg oder beauftragte Stelle).
- §§ 90 ff. WDO: Hauptverhandlung – Anwesenheit, Verteidigung, Beweisaufnahme.
- § 91 WDO: Mündliche Verhandlung als Regel.
- § 17 WBO i.V.m. §§ 76 ff. WDO: Verfahren über Anträge auf gerichtliche Entscheidung.
- § 22a WDO: Vorläufige Dienstenthebung und Einbehaltung von Bezügen durch das TDG.
- § 23a WDO: Rechtsmittel – Berufung/Revision zum BVerwG (Wehrdienstsenat).

## / Schritt für Schritt

1. **Zuständigkeit prüfen.** Truppendienstgericht Süd (Standorte südlich der Mainlinie) bzw. Nord. Bei Auslandsverwendung – Standort des Stammteils.
2. **Antrag/Schriftsatz vorbereiten.** Beim Antrag auf gerichtliche Entscheidung nach § 17 WBO: Beschwer, Tatsachenvortrag, Beweismittel, Anträge. Beim gerichtlichen Disziplinarverfahren: Verteidigungsschrift nach Anklage durch Einleitungsbehörde.
3. **Frist sichern.** 2 Wochen nach Zustellung des Beschwerdebescheids (§ 17 WBO) bzw. 2 Wochen nach Anklageschrift.
4. **Beweisanträge.** Zeugen, Sachverständige, Urkunden – schriftlich vor der Hauptverhandlung mit Beweisthema.
5. **Akteneinsicht** umfassend; auch beigezogene Personalakten, ärztliche Gutachten, Beurteilungen.
6. **Verteidigerbestellung.** Auf Antrag bei drohender hoher Maßnahme; Pflichtverteidiger nicht vorgesehen, aber Beistand zulässig.
7. **Hauptverhandlung.** Erscheinen Pflicht; Beweisaufnahme; Schlussvortrag; Urteil mit Maßnahme oder Freispruch.
8. **Rechtsmittel.** Berufung/Revision zum BVerwG nach § 23a WDO; 1 Monat ab Zustellung des Urteils.

## Trade-off-Matrix

| Verfahrenslage | Mündliche Verhandlung | Schriftliches Verfahren |
| --- | --- | --- |
| Tatsächlich streitig | Beweisaufnahme nötig | nicht sinnvoll |
| Rein rechtliche Frage | nicht zwingend | schneller |
| Maßnahmebemessung | Persönlicher Eindruck wertvoll | – |
| Verfahrenseinstellung erwartet | – | nach § 108 WDO möglich |

## Praxistipps

- TDG ist kein klassisches Verwaltungsgericht. Beisitzer aus der Truppe haben Stimmrecht und Einfluss auf die Bemessung der Maßnahme.
- Erscheinen des Mandanten ist Pflicht – Vorführung möglich bei unentschuldigtem Fernbleiben.
- Wehrdisziplinaranwaltschaft (§ 84 WDO) verfolgt im gerichtlichen Verfahren; im Antragsverfahren nach WBO tritt sie als Beteiligte auf.
- Beweisanträge nicht erst in der Hauptverhandlung stellen – vorbereitende Schriftsätze sind günstiger.
- Bei vorläufiger Dienstenthebung (§ 22a WDO) eigener Eilantrag prüfen.

## Mustertexte

**Antragsschrift auf gerichtliche Entscheidung nach § 17 WBO:**
"An das Truppendienstgericht [Süd/Nord], [Adresse]. Gegen den Beschwerdebescheid vom [Datum], zugestellt am [Datum], beantrage ich nach § 17 WBO gerichtliche Entscheidung. Es wird beantragt: 1. den Bescheid und die zugrunde liegende Maßnahme aufzuheben, 2. die Aussetzung der Vollziehung anzuordnen, 3. die Hinzuziehung der Personalakte und der Disziplinarvorgänge."

**Verteidigungsschrift im gerichtlichen Disziplinarverfahren:**
"In dem gerichtlichen Disziplinarverfahren gegen [Name], Az.: [...] nehme ich für den Soldaten Stellung: Die Anschuldigungsschrift vom [Datum] enthält folgende Tatvorwürfe: [...]. Eingeräumt wird: [...]. Bestritten wird: [...]. Es werden folgende Beweisanträge gestellt: 1. Vernehmung des Zeugen [...] zum Beweis von [...]. 2. Hinzuziehung des Personalaktenstücks [...]. 3. Sachverständigengutachten zur Frage [...]."

## Typische Fehler

- Falsches TDG angerufen – verzögert Verfahren.
- Frist § 17 WBO mit der WBO-Beschwerdefrist verwechselt.
- Beweisantrag erst in der Hauptverhandlung – nach § 244 StPO entsprechend kann abgewiesen werden.
- Vorläufige Dienstenthebung nicht gesondert angegriffen.
- Pflichtige Anwesenheit übersehen – Folge: Vorführung oder Verfahrensnachteile.

## Querverweise

- wehrbeschwerdeordnung-beschwerde-frist-form
- gerichtliches-disziplinarverfahren-soldat
- bundesverwaltungsgericht-wehrdienstsenate
- vorlaeufige-dienstenthebung-einbehaltung-bezuege
- eilverfahren-konkurrentenstreit-wehrdienstsenat
- rechtsbeistand-im-disziplinarverfahren

## Quellen Stand 06/2026

- WDO §§ 68 ff., 90 ff. – Volltext gesetze-im-internet.de.
- WBO § 17, § 21 – Volltext gesetze-im-internet.de.
- Geschäftsverteilung Truppendienstgerichte – jährlich veröffentlicht beim BVerwG.
- BVerwG Wehrdienstsenate – Rechtsprechung zu Verfahrensgrundsätzen vor dem TDG.
- Keine Kommentarstellen oder Aufsätze aus Modellwissen.
