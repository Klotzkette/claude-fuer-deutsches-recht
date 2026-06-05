---
name: datenbankrecht-db-gerichtsstand-anwendbares-api-nutzung
description: "DB Gerichtsstand Anwendbares API Nutzung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Gerichtsstand Anwendbares API Nutzung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Gerichtsstand Anwendbares API Nutzung** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-048-gerichtsstand-und-anwendbares-recht` | Gerichtsstand und anwendbares Recht im Datenbankrecht: Internationale Zuständigkeit nach EuGVVO Art. 4 und Art. 7 Nr. 2 (Tatort), Kollisionsrecht nach Art. 8 Rom-II-VO (Schutzlandprinzip), fliegender Gerichtsstand bei Internet-Verletzungen und Schiedsklauseln für Datenbanklizenzen. Bewertet Klagestrategien und Forum-Shopping-Risiken. |
| `db-007-api-nutzung-rate-limits-und-vertragsbruch` | Prüft die rechtliche Bewertung von API-Nutzung im Datenbankkontext: Vertragsbruch bei Überschreitung von Rate-Limits oder Nutzungsbedingungen, Verhältnis zu §§ 87a-87e UrhG, Schadensersatz bei unerlaubter Massenabfrage sowie Gestaltung wirksamer API-Nutzungsbedingungen. Bewertet Kündigungsrecht und Sperrbefugnis des Datenbankbetreibers. |
| `db-009-datenbanklizenz-entwurf-nutzungsumfang-und-audit` | Entwurf und Prüfung von Datenbanklizenzen nach §§ 87a-87e UrhG: Definition des Nutzungsumfangs (Entnahme/Weiterverwendung wesentlicher Teile), Audit-Klauseln, Nutzungsberichts­pflichten, Sublizenzierungsverbote und Kündigungsrechte. Bewertet AGB-Wirksamkeit nach § 307 BGB und erstellt lizenzrechts­konforme Vertragsklauseln für SaaS- und Datenprovider. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Gerichtsstand Anwendbares API Nutzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-048-gerichtsstand-und-anwendbares-recht`

**Fokus:** Gerichtsstand und anwendbares Recht im Datenbankrecht: Internationale Zuständigkeit nach EuGVVO Art. 4 und Art. 7 Nr. 2 (Tatort), Kollisionsrecht nach Art. 8 Rom-II-VO (Schutzlandprinzip), fliegender Gerichtsstand bei Internet-Verletzungen und Schiedsklauseln für Datenbanklizenzen. Bewertet Klagestrategien und Forum-Shopping-Risiken.

# Gerichtsstand und anwendbares Recht im Datenbankrecht

## Mandantenfall

- Deutsches Unternehmen wird von einem Tschechischen Wettbewerber, der in Prag sitzt, gecrawlt — vor welchem Gericht klagen?
- Datenbankbetreiber fragt, ob er den Verletzer in Deutschland oder am Tatort (Serverstandort des Verletzers) verklagen muss.
- Lizenzvertrag für eine Datenbank enthält eine Schiedsklausel für Wien — welches Recht gilt für den Inhalt des Streits?

## Erste Schritte

1. Internationale Zuständigkeit bestimmen: EuGVVO — Wohnsitz des Beklagten (Art. 4 EuGVVO) oder besonderer Gerichtsstand Unerlaubte Handlung (Art. 7 Nr. 2 EuGVVO) am Erfolgs- oder Handlungsort.
2. Tatort bei Internet-Verletzungen: Erfolgsort = Ort, wo die Verletzung eingetreten ist (Datenbankbetreiber-Sitz); Handlungsort = Server des Verletzers.
3. Anwendbares Recht nach Rom-II-VO: Art. 8 Abs. 1 Rom-II-VO — Recht des Schutzlandes (lex loci protectionis) bei IP-Verletzungen.
4. Fliegender Gerichtsstand bei Internet: Bei abrufbaren Inhalten in ganz Deutschland — welcher Tatort-Gerichtsstand ist der günstigste (LG Hamburg, LG München, LG Köln)?
5. Vertragliche Gerichtsstandsvereinbarung prüfen: Ist eine Gerichtsstandsklausel im Lizenzvertrag wirksam — EuGVVO Art. 25?
6. Schiedsklausel bewerten: Schiedsgericht für Datenbankrechts-Streitigkeiten — welches Recht gilt für Hauptsache und Verfahren?

## Rechtsrahmen

- Art. 4 EuGVVO: Allgemeiner Gerichtsstand — Beklagtenwohnsitz in seinem EU-Mitgliedsstaat.
- Art. 7 Nr. 2 EuGVVO: Besonderer Gerichtsstand für unerlaubte Handlungen — Handlungs- oder Erfolgsort.
- Art. 8 Abs. 1 Rom-II-VO: Anwendbares Recht bei IP-Verletzungen — Recht des Schutzlandes (lex loci protectionis).
- Art. 25 EuGVVO: Gerichtsstandsvereinbarung — Prorogation für EU-Gerichte wirksam.
- § 32 ZPO: Fliegender Gerichtsstand bei unerlaubten Handlungen — Handlungs- oder Erfolgsort, auch bei Internet-Verletzungen.
- EuGH C-170/12 (Pinckney/KDG): Tatortgerichtsstand für IP-Verletzungen im Internet — Anknüpfung an den Mitgliedsstaat, in dem die Website zugänglich ist.

## Prüfraster

- Hat der Beklagte seinen Sitz in einem EU-Mitgliedsstaat — gilt EuGVVO?
- Wo liegt der Handlungsort (Server des Verletzers) und wo der Erfolgsort (Datenbankbetreiber-Sitz)?
- Ist ein fliegender Gerichtsstand in Deutschland begründet — ist die verletzte Datenbank in Deutschland abrufbar?
- Welches Recht gilt nach Art. 8 Rom-II-VO — deutsches Recht (Schutzland) oder ausländisches Recht?
- Enthält der Lizenzvertrag eine wirksame Gerichtsstandsvereinbarung (Art. 25 EuGVVO)?
- Ist eine Schiedsklausel vorhanden und welches Recht gilt für Haupt- und Verfahrensfragen?
- Welches Forum ist strategisch günstiger — LG Hamburg (schnell, Expertise), LG München oder LG Köln?

## Typische Fallstricke

- Fliegender Gerichtsstand bei Internet-Verletzungen ist nicht universell — bundesweite Abrufbarkeit allein reicht nicht immer aus.
- Rom-II-VO Art. 8 Abs. 1 ist zwingend — vertragliche Rechtswahl ändert das anwendbare Recht bei Verletzungen nicht (nur bei Vertragsrecht).
- Schiedsklauseln in Lizenzverträgen schließen einstweiligen Verfügungsschutz vor staatlichen Gerichten nicht aus.
- Beklagter im Drittland (außerhalb EU) — keine EuGVVO-Anwendung; nationale Zuständigkeitsregeln prüfen.
- Forum-Shopping zwischen EU-Gerichten muss rechtsmissbräuchliche Antizipation vermeiden — LG-Wahl muss sachlich gerechtfertigt sein.

## Output

- Gerichtsstandsanalyse (EU-intern und international) für Datenbankrechts-Verletzungsklage
- Forum-Shopping-Strategie-Empfehlung (LG Hamburg / München / Köln)
- Anwendbares-Recht-Check nach Art. 8 Rom-II-VO
- Gerichtsstandsklausel-Vorlage für Datenbanklizenzverträge (Art. 25 EuGVVO)
- Schiedsklausel-Analyse für internationale Datenbankstreitigkeiten

## Quellen

- [Art. 7 EuGVVO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32012R1215)
- [Art. 8 Rom-II-VO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32007R0864)
- [§ 32 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/32.html)
- [EuGH C-170/12 Pinckney — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-170/12)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [Art. 25 EuGVVO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32012R1215)

## 2. `db-007-api-nutzung-rate-limits-und-vertragsbruch`

**Fokus:** Prüft die rechtliche Bewertung von API-Nutzung im Datenbankkontext: Vertragsbruch bei Überschreitung von Rate-Limits oder Nutzungsbedingungen, Verhältnis zu §§ 87a-87e UrhG, Schadensersatz bei unerlaubter Massenabfrage sowie Gestaltung wirksamer API-Nutzungsbedingungen. Bewertet Kündigungsrecht und Sperrbefugnis des Datenbankbetreibers.

# API-Nutzung, Rate-Limits und Vertragsbruch im Datenbankrecht

## Mandantenfall

- SaaS-Anbieter stellt fest, dass ein Geschäftskunde über seine API weit mehr Abfragen tätigt als vertraglich erlaubt, und will Schadenersatz und Kündigung prüfen.
- Startup hat eine API-Schnittstelle zu einer Fremddatenbank genutzt und überschreitet unbewusst die Rate-Limits — die Gegenseite droht mit Abmahnung.
- Unternehmen entwirft neue API-Nutzungsbedingungen und will sicherstellen, dass diese das Datenbankherstellerrecht wirksam ergänzen.

## Erste Schritte

1. Vertragliche Grundlage klären: API-Nutzungsvertrag, AGB, Developer-Agreement — welche Rate-Limits und Nutzungszwecke sind vereinbart?
2. Vertragsbruch bewerten: Überschreitung der Abfragelimits, unerlaubte Weiterverwendung, Verstoß gegen Zweckbindung — § 280 BGB, § 241 Abs. 2 BGB.
3. Urheberrechtliche Parallelprüfung: Erfüllt die Abfrageintensität den Tatbestand der wesentlichen Entnahme nach § 87b UrhG unabhängig vom Vertrag?
4. Kündigung und Sperre prüfen: Außerordentliche Kündigung (§ 314 BGB) bei schwerwiegendem Vertragsbruch; technische Sperre als berechtigte Maßnahme.
5. Schadensersatz berechnen: Überschussabfragen nach Lizenzanalogie bewerten; Nutzungsausfallschaden des Betreibers.
6. AGB-Wirksamkeit prüfen: Rate-Limit-Klauseln nach § 307 BGB; transparente Formulierung und klar definierte Folgen.

## Rechtsrahmen

- § 280 Abs. 1 BGB: Schadensersatz bei Pflichtverletzung aus dem Schuldverhältnis.
- § 314 BGB: Kündigung von Dauerschuldverhältnissen aus wichtigem Grund bei schwerwiegendem Vertragsbruch.
- § 307 BGB: AGB-Kontrolle — Rate-Limit-Klauseln müssen klar, verständlich und nicht unangemessen benachteiligend sein.
- § 87b UrhG: Urheberrechtlicher Anspruch neben dem Vertragsanspruch bei wesentlicher Entnahme.
- § 97 UrhG: Unterlassung und Schadensersatz bei Urheberrechtsverletzung — Lizenzanalogie als Berechnungsmethode.
- § 97a UrhG: Abmahnung als Voraussetzung für Erstattung von Rechtsanwaltsgebühren.

## Prüfraster

- Liegt ein wirksamer API-Nutzungsvertrag vor, und was regelt er zu Abfragevolumen, Zweck und Weiterverwendung?
- Überschreiten die tatsächlichen Abfragen die vertraglich vereinbarten Rate-Limits messbar?
- Sind die Rate-Limits technisch nachweisbar (Server-Logs, API-Gateway-Protokolle)?
- Erfüllen die Abfragen unabhängig vom Vertrag den urheberrechtlichen Verletzungstatbestand (§ 87b UrhG)?
- Hat der Betreiber vor der Kündigung abgemahnt oder eine Frist zur Abhilfe gesetzt (§ 314 Abs. 2 BGB)?
- Sind Rate-Limit-Klauseln in AGB nach § 307 BGB wirksam — sind Schwellenwerte und Rechtsfolgen transparent?
- Kann der Schaden nach Lizenzanalogie (übliche API-Lizenzgebühr) berechnet werden?

## Typische Fallstricke

- Rate-Limits ohne klare Rechtsfolge in den AGB lassen offen, ob Überschreitung Vertragsbruch oder nur technische Einschränkung ist.
- Urheberrechtliche Ansprüche laufen auch ohne Vertragsverletzung — der Betreiber kann beide Ansprüche nebeneinander geltend machen.
- Kündigung ohne vorherige Abmahnung bei erstmaligem Verstoß ist oft unwirksam (§ 314 Abs. 2 BGB).
- Technische Sperren ohne vorherige Abmahnung können ihrerseits Vertragsbruch des Betreibers darstellen (§ 280 BGB).
- Entwickler-Teams überschreiten Rate-Limits oft versehentlich — culpa levis reicht aber für vertraglichen Schadensersatzanspruch.

## Output

- Vertragsbruchanalyse mit Anspruchsübersicht (§ 280 BGB / § 97 UrhG)
- Rate-Limit-Klausel-Vorlage für wirksame AGB-Gestaltung
- Abmahnschreiben bei API-Missbrauch
- Schadensberechnung nach Lizenzanalogie
- Kündigung aus wichtigem Grund — Musterformulierung (§ 314 BGB)

## Quellen

- [§ 280 BGB — dejure.org](https://dejure.org/gesetze/BGB/280.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 3. `db-009-datenbanklizenz-entwurf-nutzungsumfang-und-audit`

**Fokus:** Entwurf und Prüfung von Datenbanklizenzen nach §§ 87a-87e UrhG: Definition des Nutzungsumfangs (Entnahme/Weiterverwendung wesentlicher Teile), Audit-Klauseln, Nutzungsberichts­pflichten, Sublizenzierungsverbote und Kündigungsrechte. Bewertet AGB-Wirksamkeit nach § 307 BGB und erstellt lizenzrechts­konforme Vertragsklauseln für SaaS- und Datenprovider.

# Datenbanklizenz: Entwurf, Nutzungsumfang und Audit-Klauseln

## Mandantenfall

- Datenanbieter will einen Lizenzvertrag für seine Immobiliendatenbank aufsetzen und benötigt klare Klauseln zu erlaubten Nutzungen, Audit-Rechten und Vergütung.
- Lizenznehmer hat einen bestehenden Datenbanknutzungsvertrag erhalten und möchte Umfang, Risiken und Ausstiegsrechte bewerten lassen.
- SaaS-Plattform überarbeitet ihre AGB und muss Datenbanklizenzbedingungen DSGVO-konform und urheberrechtskonform formulieren.

## Erste Schritte

1. Schutzgegenstand definieren: Welche Rechte werden lizenziert — Datenbankwerkschutz (§ 4 Abs. 2 UrhG), Herstellerrecht (§§ 87a ff. UrhG) oder beides?
2. Nutzungsumfang präzisieren: Erlaubte Entnahmen, Weiterverwendung, Bearbeitungsrecht, Sublizenzierung, Territorialität, Zeitraum.
3. Vergütungsmodell festlegen: Pauschal, volumenbasiert (Abrufanzahl), revenuesharing — Messbarkeit und Audit-Fähigkeit sicherstellen.
4. Audit-Klausel entwerfen: Zugangsrecht des Lizenzgebers zu Nutzungsdaten, Ankündigungsfrist, Kosten, Vertraulichkeit der Audit-Ergebnisse.
5. Kündigung und Rechtefolgen regeln: Ordentliche Kündigung, außerordentliche Kündigung (§ 314 BGB), Pflicht zur Datenlöschung nach Vertragsende.
6. AGB-Wirksamkeit prüfen: Einseitig belastende Klauseln nach § 307 BGB — Transparenzgebot, unangemessene Benachteiligung?

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht als Lizenzgegenstand — abtrennbar vom Urheberrecht an Einzelinhalten.
- § 87e UrhG: Zwingende Schranken können nicht vertraglich ausgeschlossen werden.
- § 307 BGB: Inhaltskontrolle von AGB — unklare oder einseitig benachteiligende Klauseln sind unwirksam.
- § 314 BGB: Außerordentliches Kündigungsrecht bei Vertragsbruch durch Lizenznehmer.
- § 31 UrhG: Urhebervertragsrecht — Nutzungsrechte müssen hinreichend bestimmt eingeräumt werden (Spezifizierungspflicht).
- Art. 8 RL 96/9/EG: Rechte und Pflichten des rechtmäßigen Nutzers — Mindestrechte nicht einschränkbar.

## Prüfraster

- Sind alle lizenzierten Rechte (Entnahme, Weiterverwendung, Bearbeitung) im Vertrag explizit und vollständig aufgeführt?
- Ist der Nutzungsumfang messbar — gibt es eindeutige Abfrage-/Entnahmelimits mit klarer Einheit?
- Enthält der Vertrag ein wirksames Audit-Recht mit verhältnismäßigen Bedingungen?
- Sind Sublizenzierungsverbote klar formuliert, und welche Ausnahmen gelten (verbundene Unternehmen)?
- Ist die Datenlöschungspflicht nach Vertragsende technisch umsetzbar und rechtlich durchsetzbar?
- Entsprechen die Audit-Klauseln dem AGB-Transparenzgebot (§ 307 BGB)?
- Sind TDM-Schranken (§ 44b UrhG) vertraglich ausgeschlossen oder eingeschränkt — ist das zulässig?

## Typische Fallstricke

- Zu vage definierter Nutzungsumfang führt zu Streit über erlaubte Nutzung und erschwert Audit-Durchsetzung.
- Audit-Klauseln ohne Verhältnismäßigkeitssicherung (z. B. unbegrenzte Häufigkeit) sind nach § 307 BGB angreifbar.
- Vertraglich vereinbarte Opt-outs gegen TDM-Schranken (§ 44b UrhG) sind bei kommerziellen Nutzern zulässig, bei wissenschaftlichen teilweise nicht (§ 60d UrhG).
- Sublizenzierungsverbote müssen auch verbundene Unternehmen explizit erfassen, sonst entstehen Lücken.
- Datenlöschungspflicht nach Vertragsende kollidiert mit gesetzlichen Aufbewahrungspflichten des Lizenznehmers (HGB, AO) — Regelung nötig.

## Output

- Datenbanklizenz-Vertragsvorlage mit kommentierten Klauseln
- Nutzungsumfang-Matrix (erlaubt/verboten nach Handlungstyp)
- Audit-Klausel-Muster mit Verhältnismäßigkeitssicherung
- AGB-Wirksamkeits-Checkliste (§ 307 BGB)
- Datenlöschungsprotokoll für Vertragsende

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87e UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87e.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 31 UrhG Nutzungsrechte — dejure.org](https://dejure.org/gesetze/UrhG/31.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [Art. 8 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
