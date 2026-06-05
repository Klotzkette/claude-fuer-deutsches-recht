---
name: vollstreckung-stpo-biometrischer
description: "Vollstreckung Stpo Biometrischer: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vollstreckung Stpo Biometrischer

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vollstreckung Stpo Biometrischer** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-vollstreckung-behoerden-gericht-und-registerweg` | Vollstreckung: Behörden-, Gerichts- oder Registerweg im Plugin prozessrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `stpo-biometrischer-internetabgleich-und-ki-ermittlung` | StPO-Spezialprüfung zu digitalen Ermittlungsmaßnahmen: § 98d StPO-E biometrischer Internetabgleich, § 98e StPO-E Analyseplattform, § 101 StPO-E Benachrichtigung, §§ 161 163 StPO als Grenzen manueller OSINT, KI-VO-Hochrisiko, Grundrechte, Akteneinsicht und prozessuale Angriffslogik. |
| `strafverteidigung-ersttermin` | Ersttermin bei Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, prozessuale Schritte. Normen: §§ 137 147 StPO. Prüfraster: Akteneinsichtsrecht, Mandatsverhältnis, erste Verteidigungsoptionen. Output: Checkliste Ersttermin Strafverteidigung. Abgrenzung: nicht ZPO-Prozessrecht (Zivilrecht). |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Vollstreckung Stpo Biometrischer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-vollstreckung-behoerden-gericht-und-registerweg`

**Fokus:** Vollstreckung: Behörden-, Gerichts- oder Registerweg im Plugin prozessrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vollstreckung: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Vollstreckung: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Vollstreckung: Behörden-, Gerichts- oder Registerweg / vollstreckung behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vollstreckung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `stpo-biometrischer-internetabgleich-und-ki-ermittlung`

**Fokus:** StPO-Spezialprüfung zu digitalen Ermittlungsmaßnahmen: § 98d StPO-E biometrischer Internetabgleich, § 98e StPO-E Analyseplattform, § 101 StPO-E Benachrichtigung, §§ 161 163 StPO als Grenzen manueller OSINT, KI-VO-Hochrisiko, Grundrechte, Akteneinsicht und prozessuale Angriffslogik.

# StPO: Biometrischer Internetabgleich und KI-Ermittlung

## Zweck

Dieser Skill ist die StPO-Schaltstelle für neue digitale Ermittlungsmaßnahmen. Er prüft, ob Ermittlungsbehörden biometrische Daten, öffentlich zugängliche Internetdaten oder verfahrensübergreifende Analyseplattformen rechtmäßig eingesetzt haben und welche prozessualen Reaktionen möglich sind.

Der Skill arbeitet ausdrücklich mit Rechtsstandsmarkierung: § 98d und § 98e StPO sind als Entwurfsnormen zu prüfen, solange kein verkündetes Gesetz in Kraft ist. Tragende Aussagen zum Wortlaut immer anhand aktueller amtlicher Quellen verifizieren.

## Einordnung: vier unterschiedliche Maßnahmen

| Maßnahme | Typischer Rechtsanker | Risiko |
| --- | --- | --- |
| Manuelle Internetrecherche | §§ 161, 163 StPO als Ermittlungsgeneralklauseln | Bei bloßer Kenntnisnahme meist geringere Eingriffsintensität, aber Kontext und Zweckbindung prüfen |
| Automatisierter biometrischer Internetabgleich | § 98d StPO-E | Hohe Streubreite, sensible Daten, Drittbetroffenheit, mögliche Profilbildung |
| Verfahrensübergreifende Datenanalyse | § 98e StPO-E | Zusammenführung heterogener Daten, Superdatenbank-Risiko, Zweckbindungs- und Löschungsprobleme |
| Gefahrenabwehrliche Vor-/Parallelnutzung | Polizeigesetze/BKAG/BPolG/Landesrecht | Trennung Strafverfolgung/Gefahrenabwehr, Datenübermittlung, Zweckwechsel |

## Prüfprogramm § 98d StPO-E

### 1. Ausgangsdaten

Prüfe:

- Welche biometrischen Daten wurden aus welchem Strafverfahren genutzt?
- Sind sie rechtmäßig erhoben worden?
- Gehören sie zum selben Verfahren oder zu einem anderen Verfahren?
- Waren sie noch speicherungsfähig oder bereits löschungsreif?
- Betreffen sie Beschuldigte, Zeugen, Opfer oder unbeteiligte Dritte?

Biometrische Daten sind nicht nur Gesichter. Erfasst sein können auch Stimme, Gang, Fingerabdruck, Iris, Retina, Handgeometrie oder andere technische Identifikationsmerkmale.

### 2. Vergleichsdaten

Prüfe:

- Waren die Internetdaten wirklich öffentlich zugänglich?
- Wurden Daten einbezogen, die erst nach Registrierung, Genehmigung oder Zahlung erreichbar waren?
- Wurden durch Dritte veröffentlichte Bilder/Clips verwendet, auf deren Veröffentlichung die betroffene Person keinen Einfluss hatte?
- Wurden Live-Streams, Webcams oder Echtzeitdaten ausgeschlossen?
- Wurde Privatkommunikation, Messenger-Kommunikation oder ein geschlossener Personenkreis berührt?

### 3. Zweck

Die Zwecke müssen getrennt werden:

- Identitätsfeststellung,
- Aufenthaltsort Beschuldigter,
- Aufenthaltsort Zeuge,
- Sachverhaltserforschung,
- Vollstreckungs-/Fahndungszweck.

Je weiter der Zweck von Identität oder Aufenthaltsort des Beschuldigten wegführt, desto stärker muss die Maßnahme begründet werden. Besonders sensibel ist ein Einsatz zur allgemeinen Sachverhaltserforschung, weil dadurch Interessen, Kontakte, Orte und Verhaltensmuster in den Blick geraten können.

### 4. Verdacht und Anlasstat

Prüfe:

- bestimmte Tatsachen statt bloßer Vermutungen,
- Täter- oder Teilnehmerverdacht,
- Straftat von auch im Einzelfall erheblicher Bedeutung,
- Versuch/Vorbereitung nur, wenn strafbar und konkretisiert,
- kein bloßes “Katalogtat-Etikett” ohne Einzelfallgewicht.

Wenn nur auf § 100a Abs. 2 StPO verwiesen wird, muss zusätzlich geklärt werden, ob der konkrete Fall die Eingriffsintensität des biometrischen Massenabgleichs trägt.

### 5. Subsidiarität

Die Formel “wesentlich erschwert oder aussichtslos” muss mit Tatsachen gefüllt werden:

- Welche milderen Mittel wurden geprüft?
- Warum reicht klassische Lichtbildvorlage, Zeugenbefragung, Registerabfrage, Telekommunikations-/Bestandsdatenermittlung oder gezielte Observation nicht?
- Gab es Zeitdruck oder nur Ermittlungsökonomie?
- Wurde der hohe Drittbetroffenheitsgrad einbezogen?

## Prüfprogramm § 98e StPO-E

Bei Analyseplattformen zusätzlich:

- Welche Dateien und Informationssysteme wurden zusammengeführt?
- Rechtmäßigkeit und Zweckbindung jeder Datenquelle prüfen.
- Dürfen TKÜ-, Verkehrsdaten-, Asservaten- oder andere Daten aus fremden Verfahren einbezogen werden?
- Sind Daten aus Wohnraumüberwachung oder Online-Durchsuchung ausgeschlossen?
- Keine direkte Anbindung an nicht-polizeiliche Register oder Internetdienste?
- Suchbegriffe anlassbezogen und aus konkretem Sachverhalt abgeleitet?
- Keine automatisierte Entscheidung mit unmittelbar nachteiliger Rechtsfolge?
- Diskriminierungsvermeidung technisch und organisatorisch dokumentiert?

## Grundrechte und Verfassungsmaßstab

Markiere in jedem Memo:

- Recht auf informationelle Selbstbestimmung,
- Menschenwürde und Subjektstellung im Strafverfahren,
- faires Verfahren,
- Berufsgeheimnisschutz, insbesondere Verteidiger, Ärzte, Seelsorge, Presse,
- Kernbereich privater Lebensgestaltung,
- Streubreite gegenüber Unbeteiligten,
- Heimlichkeit und Benachrichtigung,
- Risiko von Abschreckungseffekten bei Nutzung öffentlicher Kommunikation und Social Media.

Amtlich verifizierter Ausgangspunkt für Analyseplattformen: BVerfG, Urteil vom 16.02.2023, 1 BvR 1547/19, 1 BvR 2634/20. Kernaussage für diesen Skill: Eine automatisierte Verknüpfung und Auswertung heterogener Datenbestände braucht eine hinreichend bestimmte gesetzliche Grundlage und wirksame Begrenzungen.

## KI-VO und technische Mindestakte

Bei KI-Nutzung muss die Akte mindestens aufklären:

- Liegt ein KI-System im Sinne von Art. 3 Nr. 1 KI-VO vor?
- Ist der Einsatz nach Art. 5 KI-VO verboten oder fällt er in eine Ausnahme?
- Handelt es sich um ein Hochrisiko-System nach Art. 6 Abs. 2 i.V.m. Anhang III Nr. 1 lit. a KI-VO?
- Sind Risikomanagement, Datenqualität, technische Dokumentation, Protokollierung, Transparenz, menschliche Aufsicht, Genauigkeit, Robustheit und Cybersicherheit belegt?
- Gibt es eine Grundrechte-Folgenabschätzung?
- Ist die Anwendung registriert, bestimmungsgemäß eingesetzt und durch geschultes Personal überwacht?

Wenn diese Unterlagen fehlen, ist das nicht nur Datenschutz- oder Technikproblem, sondern prozessualer Verteidigungsstoff.

## Akteneinsicht und prozessuale Reaktion

### Nachforderungsliste

- Anordnung samt Begründung,
- Eilentscheidung und nachträgliche Bestätigung,
- technische Einsatzprotokolle,
- Bezeichnung der Anwendung,
- Trefferlisten und Scores,
- Schwellenwerte und Fehlerraten,
- menschliche Plausibilitätsprüfung,
- Datenquellen und Suchparameter,
- Löschvermerk,
- Benachrichtigungslage,
- KI-VO-Unterlagen,
- Vermerke zu Drittbetroffenen und Berufsgeheimnisträgern.

### Angriffsauswahl

| Lage | Reaktion |
| --- | --- |
| Entwurfsnorm noch nicht in Kraft | Rechtsgrundlage bestreiten, Grenzen §§ 161, 163 StPO herausarbeiten |
| Anordnung fehlt oder ist leerformelhaft | Rechtswidrigkeit der Maßnahme rügen, Nachermittlung verlangen |
| Software unklar | Sachverständigenprüfung und Offenlegung beantragen |
| Treffer nur Score ohne Nachprüfung | Beweiswert angreifen, Identitätsbeweis bestreiten |
| Drittbetroffenheit massiv | Verhältnismäßigkeit, Löschung, Benachrichtigung, Zweckbindung prüfen |
| Berufsgeheimnisträger/Kernbereich berührt | besondere Schutzmechanismen und Verwertungsgrenzen geltend machen |
| KI-VO-Dokumentation fehlt | Hochrisiko-Konformität, Grundrechte-Folgenabschätzung und Systemaufsicht rügen |

## Output

- StPO-Prüfvermerk zur digitalen Ermittlungsmaßnahme.
- Akteneinsichts- und Nachforderungsantrag.
- Beweisverwertungs- und Beweiswertangriff.
- Fragenkatalog an Ermittlungsbeamte, IT-Verantwortliche und Sachverständige.
- Mandanten-/Zeugeninformation in verständlicher Sprache.
- Prozessuale Risikoampel für Hauptverhandlung, Beschwerde und Revision.

## 3. `strafverteidigung-ersttermin`

**Fokus:** Ersttermin bei Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, prozessuale Schritte. Normen: §§ 137 147 StPO. Prüfraster: Akteneinsichtsrecht, Mandatsverhältnis, erste Verteidigungsoptionen. Output: Checkliste Ersttermin Strafverteidigung. Abgrenzung: nicht ZPO-Prozessrecht (Zivilrecht).

# Strafverteidigung – Ersttermin und erste Schritte

## Zweck

Dieser Skill unterstützt Strafverteidiger bei der Vorbereitung und Durchführung des ersten
Mandantentermins sowie der unmittelbaren Folgeschritte. Er deckt ab: Pflichtverteidigerbestellung
(§ 140 StPO), Akteneinsicht (§ 147 StPO), Belehrung des Mandanten über das Schweigerecht
(§ 136 StPO), Vorbereitung von Beweisanträgen und einen Überblick über den Ablauf der
Hauptverhandlung (§§ 226 ff. StPO). Anwendungsbereich: Amtsgericht bis Landgericht, alle
Delikte; besondere Hinweise für Untersuchungshaft (§§ 112 ff. StPO).

## Eingaben

Das Modell benötigt:

1. **Verfahrensstand**: Ermittlungsverfahren, Anklage, Strafbefehl, Hauptverhandlung?
2. **Tatvorwurf**: Delikte, § BGB/StGB, Strafrahmen
3. **Mandant**: inhaftiert (U-Haft)? Erstmals beschuldigt? Vorstrafen?
4. **Zugesandte Unterlagen**: Anklageschrift, Ermittlungsakte (Teile), Strafbefehl
5. **Termin**: Datum und Gericht der Hauptverhandlung; verbleibende Zeit zur Vorbereitung

## Rechtlicher Rahmen

### Normen

- **§ 137 StPO** – Recht auf Beistand eines Verteidigers (jederzeit, auch ohne richterliche
 Genehmigung)
- **§ 140 StPO** – Notwendige Verteidigung (Pflichtverteidigerbestellung):
 Abs. 1: gesetzliche Fälle (z. B. Verbrechen, Untersuchungshaft, Hauptverhandlung beim LG,
 drohende Unterbringung); Abs. 2: sonstige Fälle schwieriger Sach-/Rechtslage oder wenn
 Beschuldigter sich nicht selbst verteidigen kann
- **§ 141 StPO** – Bestellung des Pflichtverteidigers (auf Antrag des Beschuldigten oder von
 Amts wegen)
- **§ 143a StPO** – Wahlverteidigervorrang; Rücknahme der Pflichtverteidigerbestellung bei
 Mandatsübernahme durch Wahlverteidiger
- **§ 147 StPO** – Akteneinsicht: Abs. 1: Verteidiger hat Recht auf Einsicht in die dem
 Gericht vorliegenden und die dem Gericht vorzulegenden Akten; Abs. 2: Einschränkung im
 Ermittlungsverfahren bei Gefährdung des Untersuchungszwecks
- **§ 136 Abs. 1 StPO** – Belehrungspflicht bei erster Vernehmung: Tatvorwurf, Schweigerecht,
 Recht auf Verteidigerkonsultation; Beweisverwertungsverbot bei fehlender Belehrung
- **§ 136a StPO** – Verbotene Vernehmungsmethoden (absolute Beweisverwertungsverbote)
- **§§ 226–275 StPO** – Hauptverhandlung: § 226 (Unmittelbarkeit), § 229 (Unterbrechungsfristen),
 § 240 (Fragerecht), § 244 Abs. 3–6 (Beweisantrag; Ablehnungsgründe), § 257c (Verständigung)
- **§ 243 Abs. 5 StPO** – Belehrung in der Hauptverhandlung (Schweigerecht)
- **§ 257 StPO** – Erklärungsrecht nach jeder Beweiserhebung
- **§ 344 StPO** – Revisionsbegründung (formelle/materielle Revisionsrügen)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Beschuldigten auf Beistand eines Verteidigers (§ 137 StPO) ist Ausfluss des Grundrechts auf
 ein faires Verfahren (Art. 2 Abs. 1 i. V. m. Art. 20 Abs. 3 GG) und des Grundsatzes der
 Waffengleichheit; der Staat darf die Verteidigung nicht strukturell erschweren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 bei unterlassener Belehrung nach § 136 StPO; eine ohne ordnungsgemäße Belehrung über das
 Schweigerecht gewonnene Aussage des Beschuldigten ist unverwertbar, wenn der Fehler nicht
 geheilt wurde; Heilung durch späteres Einverständnis des Beschuldigten möglich (str.).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 an einen förmlichen Beweisantrag (§ 244 Abs. 3 StPO); Beweisbehauptung muss bestimmt sein;
 bloße Beweisermittlungsanträge sind nach anderen Regeln zu bescheiden.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 des Verteidigers § 147 StPO; der Verteidiger hat Anspruch auf vollständige Akteneinsicht
 sobald die Anklageschrift beim Gericht eingereicht wurde; Ausnahmen nur nach § 147 Abs. 2
 StPO im laufenden Ermittlungsverfahren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Ersttermin – Checkliste

1. **Mandantenbelehrung** (bevor Mandant schildert):
 - Vertraulichkeit (§ 43a Abs. 2 BRAO, § 203 StGB)
 - Schweigerecht auch gegenüber Anwalt; keine Lügenpflicht
 - Was Mandant mitteilt, bleibt im Mandat; keine eigene Zeugenpflicht des Verteidigers
2. **Sachverhaltsaufnahme**: Mandant schildert Tatvorwurf aus seiner Sicht; kein Unterbrechen;
 danach gezielte Nachfragen (Alibis, Zeugen, Beweise)
3. **Pflichtverteidigerprüfung** (§ 140 StPO):
 - Liegt ein gesetzlicher Pflichtverteidigerfall vor? (Abs. 1 Nr. 1–11)
 - Ermessensfall Abs. 2? (schwierige Sach-/Rechtslage, Unfähigkeit zur Selbstverteidigung)
 - Ggf. sofort Antrag auf Beiordnung stellen (§ 141 StPO)
4. **Akteneinsicht** (§ 147 StPO):
 - Ist Anklage bereits erhoben? → sofortiger Anspruch auf vollständige Akteneinsicht
 - Im Ermittlungsverfahren: Einsicht ggf. eingeschränkt (§ 147 Abs. 2 StPO); Beschwerde
 bei Verweigerung (§ 304 StPO); ggf. Antrag auf gerichtliche Entscheidung (§ 147 Abs. 5 StPO)
5. **Sofortmaßnahmen bei U-Haft**:
 - Haftprüfungsantrag § 117 StPO oder Haftbeschwerde § 304 StPO
 - Haftgründe prüfen (§§ 112, 112a StPO): Flucht-/Verdunkelungsgefahr, Wiederholungsgefahr
 - Untersuchungshaftprüfung alle 3 Monate von Amts wegen (§ 122 StPO)
6. **Strategie festlegen**:
 - Schweigen bis zur vollständigen Akteneinsicht (Regelempfehlung)
 - Teilgeständnis? Kooperation? (nur nach vollständiger Aktenkenntnis)
 - Beweissicherung: Zeugenaussagen, Lichtbilder, digitale Daten (cave: §§ 94 ff. StPO –
 Beschlagnahme)
7. **Vorbereitung Hauptverhandlung** (§§ 226 ff. StPO):
 - Mandant über Ablauf informieren: Verlesung Anklage, Belehrung § 243 Abs. 5 StPO,
 Zeugenvernehmung, Plädoyers, letztes Wort § 258 Abs. 2 StPO
 - Beweisanträge (§ 244 StPO) vorbereiten; schriftlich formulieren; rechtzeitig einreichen
 - Verständigung (§ 257c StPO) als Option erwägen

### Hauptverhandlung – Ablauf (§§ 226–275 StPO)

| Schritt | Norm | Anmerkung |
|---|---|---|
| Aufruf zur Sache | § 243 Abs. 1 StPO | Feststellung Anwesenheit |
| Verlesung Anklage | § 243 Abs. 3 StPO | Beginn der Beweisaufnahme |
| Belehrung Angeklagter | § 243 Abs. 5 StPO | Schweigerecht; ggf. Einlassung |
| Beweisaufnahme | §§ 244–256 StPO | Zeugen, Sachverständige, Urkunden |
| Beweisanträge | § 244 Abs. 3–5 StPO | Schriftliche Formulierung empfohlen |
| Plädoyers | § 258 Abs. 1 StPO | Verteidiger nach Staatsanwaltschaft |
| Letztes Wort | § 258 Abs. 2 StPO | Angeklagter hat letztes Wort |
| Urteil | §§ 260–268 StPO | Tenor + Begründung |

## Ausgabeformat

- **Checkliste Ersttermin** (Pflicht-Belehrungen, Sofortmaßnahmen, Akteneinsicht)
- **Antragsschreiben** auf Pflichtverteidigerbestellung (§§ 140, 141 StPO)
- **Akteneinsichtsantrag** (§ 147 StPO)
- **Beweisantragsformulierung** (§ 244 StPO; Beweisbehauptung + Beweismittel + Begründung)
- **Mandanteninfo** (leicht verständlich: Ablauf der Hauptverhandlung, Schweigerecht)

## Beispiel

**Sachverhalt**: Mandant M wird wegen Körperverletzung (§ 223 StGB) beschuldigt; er befindet
sich nicht in Haft; die Anklageschrift wurde zugestellt; HV-Termin ist in 4 Wochen.

**Ersttermin-Ablauf (Urteilsstil)**:

1. *Belehrung*: M wird über Vertraulichkeit und Schweigerecht belehrt; es wird empfohlen, in
 der Hauptverhandlung zunächst zu schweigen bis zur vollständigen Akteneinsicht.
2. *Pflichtverteidigerprüfung*: § 223 StGB ist eine Tat mittlerer Kriminalität; gesetzlicher
 Pflichtverteidigerfall nach § 140 Abs. 1 StPO liegt nur bei Verbrechen vor (§ 12 Abs. 1 StGB –
 Körperverletzung ist Vergehen). Pflichtverteidigerfall nach § 140 Abs. 2 StPO wäre zu prüfen,
 wenn M sich nicht selbst verteidigen kann. Ggf. Wahlverteidigermandat.
3. *Akteneinsicht* (§ 147 Abs. 1 StPO): Da Anklage erhoben, sofortiger Anspruch; Antrag
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rn. 10).
4. *Strategie*: Schweigen bis nach Akteneinsicht; danach Entscheidung über Einlassung.

## Risiken und typische Fehler

- **Fehlende Belehrung § 136 StPO**: Aussagen des Mandanten bei Polizei ohne Belehrung sind
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 in der Hauptverhandlung erklären (§ 257 StPO).
- **Zu frühe Einlassung**: Ohne vollständige Akteneinsicht einlassen → Selbstbelastung durch
 Detailwissen, das Ermittler noch nicht hatten.
- **Versäumte Haftprüfungsfrist**: Bei U-Haft sind Fristen (§§ 117, 122 StPO) absolute
 Priorität; Fristenkontrolle täglich.
- **Unzulässiger Beweisantrag** (§ 244 Abs. 3 StPO): Beweisbehauptung zu unbestimmt →
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 BGHSt 53, 112 Rn. 12).
- **Interessenkonflikt** (§ 43a Abs. 4 BRAO, § 3 BORA): Darf nicht gleichzeitig Mitbeschuldigten
 oder Verletzten vertreten.
- **Verschwiegenheit** (§ 43a Abs. 2 BRAO, § 203 StGB): Mandantendaten aus Strafakten dürfen
 nicht ungesichert weitergegeben werden; digitale Kommunikation nur über Ende-zu-Ende-
 verschlüsselte Kanäle.
- **Verständigung § 257c StPO**: Nur mit expliziter Mandantenanweisung; Gericht und StA dürfen
 in bestimmten Fällen kein Schuldbekenntnis als Verständigungsvoraussetzung fordern.

## Quellenpflicht

Jede Aussage zu Pflichtverteidigervoraussetzungen, Akteneinsicht, Schweigerecht und
Beweisverwertungsverboten ist nach `references/zitierweise.md` zu belegen. BVerfG-Entscheidungen
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Kommentare mit Bearbeiter, Werk, Aufl. bzw. Ed. (Stand), §, Rn. Mindermeinungen bei
umstrittenen Heilungsfällen § 136 StPO ausdrücklich benennen.
