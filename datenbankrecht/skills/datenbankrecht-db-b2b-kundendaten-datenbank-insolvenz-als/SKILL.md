---
name: datenbankrecht-db-b2b-kundendaten-datenbank-insolvenz-als
description: "DB B2B Kundendaten Datenbank Insolvenz ALS: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB B2B Kundendaten Datenbank Insolvenz ALS

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB B2B Kundendaten Datenbank Insolvenz ALS** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-017-b2b-kundendaten-crm-export-durch-mitarbeiter` | Analysiert Datenbankherstellerrecht (§§ 87a-87e UrhG) und GeschGehG bei CRM-Datenbankexporten durch ausscheidende Mitarbeiter: Verletzungstatbestände, arbeitsrechtliche Sanktionen, einstweilige Verfügung sowie DSGVO-Pflichten bei unrechtmäßiger Datenweitergabe. Erstellt Präventionskonzept mit technischen Schutzmaßnahmen und Vertragsklauseln. |
| `db-018-datenbank-in-insolvenz-asset-deal-und-rechtekette` | Datenbankrecht in der Insolvenz: Übergang von Datenbankherstellerrechten (§§ 87a-87e UrhG) im Insolvenzverfahren und Asset Deal, Due-Diligence-Prüfung der Rechtekette, Freigabe durch den Insolvenzverwalter und DSGVO-Pflichten bei Übertragung personenbezogener Datensätze. Erstellt Transaktions-Checkliste für Datenbankrechte-Erwerb aus Insolvenzmasse. |
| `db-019-datenbank-als-kreditsicherheit-due-diligence` | Bewertet Datenbankrechte (§§ 87a-87e UrhG) als Kreditsicherheit: Verpfändung und Sicherungsübertragung von Datenbankherstellerrecht, Due-Diligence-Prüfung für Kreditgeber (Investitionsnachweis, Schutzdauer, Verletzungsfreiheit) und Verwertung im Sicherungsfall. Analysiert Bankpraxis und erstellt IP-Sicherheitenprüfbogen für Datenbankrechte. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB B2B Kundendaten Datenbank Insolvenz ALS**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-017-b2b-kundendaten-crm-export-durch-mitarbeiter`

**Fokus:** Analysiert Datenbankherstellerrecht (§§ 87a-87e UrhG) und GeschGehG bei CRM-Datenbankexporten durch ausscheidende Mitarbeiter: Verletzungstatbestände, arbeitsrechtliche Sanktionen, einstweilige Verfügung sowie DSGVO-Pflichten bei unrechtmäßiger Datenweitergabe. Erstellt Präventionskonzept mit technischen Schutzmaßnahmen und Vertragsklauseln.

# B2B-Kundendaten und CRM-Export durch Mitarbeiter — Datenbankrecht und Arbeitsrecht

## Mandantenfall

- Vertriebsmitarbeiter verlässt das Unternehmen und nimmt dabei die vollständige CRM-Kundendatenbank auf einem USB-Stick mit zum Wettbewerber.
- Unternehmen fragt, welche Ansprüche gegen den ausgeschiedenen Mitarbeiter und den aufnehmenden Wettbewerber bestehen.
- Arbeitgeber will präventiv sicherstellen, dass CRM-Exporte technisch verhindert und vertraglich verboten werden.

## Erste Schritte

1. Datenbankherstellerrecht prüfen: Hat das Unternehmen eine wesentliche Investition in seine CRM-Kundendatenbank (Beschaffung, Überprüfung, Darstellung der Kundendaten) getätigt?
2. Geschäftsgeheimnisschutz prüfen: Sind die Kundendaten als Geschäftsgeheimnis nach § 2 Nr. 1 GeschGehG geschützt — geheim, wertvoll, Geheimhaltungsmaßnahmen vorhanden?
3. Verletzungshandlung bestimmen: § 87b UrhG (Entnahme wesentlicher Teile), § 4 GeschGehG (rechtswidrige Erlangung und Nutzung), Arbeitsvertragsverletzung.
4. Ansprüche gegen Mitarbeiter und Wettbewerber formulieren: Unterlassung, Herausgabe, Schadensersatz, Auskunft.
5. Einstweilige Verfügung prüfen: Dringlichkeit bejaht bei aktueller Verwendung beim Wettbewerber — Verfügungsanspruch und Verfügungsgrund.
6. DSGVO-Pflichten klären: Datenpanne nach Art. 33-34 DSGVO melden — wenn personenbezogene Kundendaten betroffen.

## Rechtsrahmen

- § 87a UrhG: CRM-Datenbank als Datenbank mit wesentlicher Investition in Kundendatenbeschaffung und -pflege.
- § 87b UrhG: Entnahme wesentlicher Teile durch den Mitarbeiter als Verletzung des Herstellerrechts.
- § 2 Nr. 1 GeschGehG: Kundendaten als Geschäftsgeheimnis, wenn nicht allgemein bekannt, wirtschaftlich wertvoll und angemessen geheim gehalten.
- § 4 GeschGehG: Verbotene Handlungen — rechtswidrige Erlangung, Nutzung und Offenlegung.
- Art. 33-34 DSGVO: Meldepflicht bei Datenpannen an Aufsichtsbehörde und betroffene Kunden.
- § 241 Abs. 2 BGB: Nebenpflicht des Arbeitnehmers zur Rücksicht auf Arbeitgeberinteressen — verletzt durch CRM-Export.

## Prüfraster

- Hat das Unternehmen angemessene Geheimhaltungsmaßnahmen für die CRM-Datenbank ergriffen (Zugangsbeschränkungen, NDA, Löschpflicht bei Ausscheiden)?
- Enthält der Arbeitsvertrag explizite Verbote zur Mitnahme von Kundendaten bei Ausscheiden?
- Weist die exportierte Datenmenge auf eine Entnahme wesentlicher Teile hin (§ 87b UrhG)?
- Verwendet der Wettbewerber die Daten bereits aktiv — besteht Dringlichkeit für einstweilige Verfügung?
- Sind personenbezogene Kundendaten betroffen — ist eine Datenpannen-Meldung nach Art. 33 DSGVO erforderlich?
- Kann technisch nachgewiesen werden, dass ein Export stattgefunden hat (USB-Logs, E-Mail-Forensik, Zugriffsprotokoll)?
- Ist der aufnehmende Wettbewerber gutgläubig oder wusste er von der rechtswidrigen Herkunft der Daten?

## Typische Fallstricke

- Fehlende technische Sperren (kein USB-Block, kein Export-Verbot im CRM) schwächen die Position im GeschGehG-Prozess erheblich.
- Ohne DSGVO-Datenpannen-Meldung droht zusätzliches Bußgeld durch die Datenschutzbehörde.
- Ansprüche gegen den Wettbewerber setzen Kenntnis oder fahrlässige Unkenntnis von der unrechtmäßigen Herkunft voraus.
- Arbeitsrechtliche Abmahnung und außerordentliche Kündigung müssen zeitnah erfolgen — keine Verwirkung.
- Berechnung des Schadens ist komplex: entgangene Aufträge, Lizenzanalogie oder pauschaler Schadensersatz nach § 97 Abs. 2 UrhG.

## Output

- Verletzungsanalyse (§ 87b UrhG + GeschGehG + Arbeitsrecht kombiniert)
- Abmahnschreiben und fristlose Kündigung des Mitarbeiters
- Einstweiliger Verfügungsantrag gegen Mitarbeiter und Wettbewerber
- DSGVO-Datenpannen-Meldung (Art. 33 DSGVO) — Muster
- Präventionskonzept: Technische und vertragliche CRM-Schutzmaßnahmen

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 4 GeschGehG — dejure.org](https://dejure.org/gesetze/GeschGehG/4.html)
- [Art. 33 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/33.html)
- [§ 241 BGB — dejure.org](https://dejure.org/gesetze/BGB/241.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)

## 2. `db-018-datenbank-in-insolvenz-asset-deal-und-rechtekette`

**Fokus:** Datenbankrecht in der Insolvenz: Übergang von Datenbankherstellerrechten (§§ 87a-87e UrhG) im Insolvenzverfahren und Asset Deal, Due-Diligence-Prüfung der Rechtekette, Freigabe durch den Insolvenzverwalter und DSGVO-Pflichten bei Übertragung personenbezogener Datensätze. Erstellt Transaktions-Checkliste für Datenbankrechte-Erwerb aus Insolvenzmasse.

# Datenbank in der Insolvenz — Asset Deal und Rechtekette

## Mandantenfall

- Investor möchte die Datenbank eines insolventen Unternehmens im Asset Deal erwerben und fragt, welche Datenbankrechte übergehen und welche Due-Diligence-Punkte zu klären sind.
- Insolvenzverwalter möchte die Datenbankrechte des Schuldners als Massevermögen verwerten und benötigt eine Bewertung der bestehenden Lizenzen und Schutzrechte.
- Käufer einer Datenbank aus einer Insolvenz stellt fest, dass ein Dritter ebenfalls Rechte an der Datenbank behauptet — wie ist die Rechtekette zu prüfen?

## Erste Schritte

1. Rechtslage in der Insolvenz klären: Das Datenbankherstellerrecht fällt in die Insolvenzmasse (§ 35 InsO) — Insolvenzverwalter kann darüber verfügen.
2. Bestehende Lizenzen prüfen: Laufen Datenbanklizenzen in der Insolvenz fort? § 108 InsO für gegenseitige Verträge; Wahlrecht des Insolvenzverwalters.
3. Asset Deal strukturieren: Übertragungsvertrag muss alle Rechte explizit aufführen — Herstellerrecht, Urheberrecht an Datenbankwerk, Lizenzen, Softwarerechte.
4. Rechtekette belegen: Dokumentenprüfung — wer hat die Datenbank ursprünglich erstellt, wer hat Investition getragen, sind Rechte vertraglich abgesichert?
5. DSGVO bei personenbezogenen Daten: Übertragung personenbezogener Datensätze erfordert Rechtsgrundlage nach Art. 6 DSGVO; berechtigtes Interesse des Käufers?
6. Kaufpreisbewertung: Schutzdauer (§ 87d UrhG) restlaufend, Verletzungsfreiheit, Lizenzerträge und Wert der Investition als Bewertungsgrundlage.

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht als übertragbares Vermögensrecht — Teil der Insolvenzmasse (§ 35 InsO).
- § 87d UrhG: Schutzdauer 15 Jahre — Rest-Laufzeit als Wertfaktor bei der Transaktionsbewertung.
- § 35 InsO: Insolvenzmasse umfasst alle Vermögenswerte des Schuldners einschließlich Immaterialgüterrechte.
- § 108 InsO: Fortbestand von Dauerschuldverhältnissen (Datenbanklizenzen) — Insolvenzverwalter hat Wahlrecht.
- Art. 6 Abs. 1 lit. f DSGVO: Berechtigtes Interesse als Rechtsgrundlage für Datenbankübertragung — Abwägung erforderlich.
- § 453 BGB: Rechtskauf — Mängelgewährleistung auch bei Erwerb von Datenbankrechten; Rechtsmangel bei Drittrechten.

## Prüfraster

- Ist das Datenbankherstellerrecht eindeutig dem Schuldner zugeordnet (Herstellereigenschaft, Investitionsnachweis)?
- Bestehen konkurrierende Rechte Dritter (Mitherstellerrechte, Unterlizenzen, Pfandrechte an IP)?
- Laufen bestehende Datenbanklizenzen in der Insolvenz fort — hat der Insolvenzverwalter das Wahlrecht ausgeübt?
- Sind personenbezogene Daten in der Datenbank enthalten — welche DSGVO-Pflichten treffen den Erwerber?
- Ist die Schutzdauer (§ 87d UrhG) noch ausreichend lang für den geplanten Nutzungszweck?
- Enthält der Asset Deal eine Rechtsmängelgewährleistung für den Fall unerkannter Drittrechte?
- Sind Softwarerechte, Urheberrecht am Datenbankwerk und Herstellerrecht separat erfasst und übertragen?

## Typische Fallstricke

- Datenbankherstellerrecht ohne explizite Übertragungsklausel geht nicht automatisch mit dem Unternehmensvermögen über.
- Lizenznehmer können nach § 108 InsO in laufenden Verträgen verbleiben — der Käufer erwirbt die Datenbank belastet mit bestehenden Lizenzen.
- DSGVO-Pflichten (Datenschutzhinweise, ggf. neue Einwilligungen) entstehen beim Erwerber — werden oft unterschätzt.
- Insolvenzanfechtung: Datenbankrechte-Übertragungen in den letzten Monaten vor Insolvenzantrag können anfechtbar sein.
- Bewertung des Datenbankrechts ohne Prüfung der verbleibenden Schutzdauer und des Verletzungshistorie-Risikos führt zu Fehlinvestition.

## Output

- Asset-Deal-Datenbankrechte-Checkliste (Due Diligence)
- Übertragungsvertrag-Klauseln für Datenbankherstellerrecht
- Rechteketten-Dokumentationsmatrix
- DSGVO-Pflichten-Übersicht für den Erwerber personenbezogener Datenbanken
- Schutzdauer- und Wertbewertungstool (§ 87d UrhG)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87d UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87d.html)
- [§ 35 InsO — dejure.org](https://dejure.org/gesetze/InsO/35.html)
- [§ 108 InsO — dejure.org](https://dejure.org/gesetze/InsO/108.html)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 453 BGB Rechtskauf — dejure.org](https://dejure.org/gesetze/BGB/453.html)

## 3. `db-019-datenbank-als-kreditsicherheit-due-diligence`

**Fokus:** Bewertet Datenbankrechte (§§ 87a-87e UrhG) als Kreditsicherheit: Verpfändung und Sicherungsübertragung von Datenbankherstellerrecht, Due-Diligence-Prüfung für Kreditgeber (Investitionsnachweis, Schutzdauer, Verletzungsfreiheit) und Verwertung im Sicherungsfall. Analysiert Bankpraxis und erstellt IP-Sicherheitenprüfbogen für Datenbankrechte.

# Datenbank als Kreditsicherheit — Due Diligence für Kreditgeber

## Mandantenfall

- Startup will seine proprietäre Datenbankrechte als Sicherheit für einen Kredit einsetzen und fragt, wie das rechtlich strukturiert wird.
- Bank erhält Datenbankherstellerrechte als Sicherheit und benötigt eine Due-Diligence-Checkliste zur Bewertung der Werthaltigkeit.
- Insolvenzverwalter stellt fest, dass Datenbankrechte an eine Bank sicherungsübereignet wurden und klärt Priorität gegenüber anderen Gläubigern.

## Erste Schritte

1. Verpfändbarkeit prüfen: Datenbankherstellerrecht ist ein übertragbares Vermögensrecht (§ 87a Abs. 2 UrhG) — Verpfändung nach § 1273 BGB oder Sicherungsübertragung möglich.
2. Investitionsnachweis bewerten: Kann der Kreditnehmer die wesentliche Investition in die Datenbank belegen (Kostenaufstellungen, Projektnachweise)?
3. Schutzdauer prüfen: Verbleibende Laufzeit nach § 87d UrhG bestimmt den wirtschaftlichen Wert als Sicherheit.
4. Verletzungsfreiheit prüfen: Besteht das Herstellerrecht unangefochten — keine anhängigen Rechtsstreitigkeiten, keine Drittlizenzen mit Ausschlusswirkung?
5. Verwertungsweg planen: Wie kann die Bank im Sicherungsfall die Datenbankrechte verwerten (Lizenzeinnahmen, Verkauf, Vollstreckung)?
6. Vertragliche Sicherung: Sicherungsübereignungsvertrag, Verwertungsklausel, Pflicht des Kreditnehmers zur Aufrechterhaltung des Datenbankschutzes.

## Rechtsrahmen

- § 87a Abs. 2 UrhG: Datenbankherstellerrecht als übertragbares Recht — Sicherungsübertragung rechtlich möglich.
- § 1273 BGB: Verpfändung von Rechten — gilt auch für Immaterialgüterrechte wie Datenbankherstellerrecht.
- § 87d UrhG: Schutzdauer 15 Jahre — Wertfaktor für Kreditbewertung; Verlängerung bei wesentlichen Änderungen.
- § 35 InsO: Im Insolvenzfall fällt die Datenbank in die Masse — Absonderungsrecht der Bank bei vorheriger wirksamer Sicherung.
- § 51 InsO: Absonderungsrecht für Sicherungsrechte an beweglichen Gegenständen und Rechten.
- § 87b UrhG: Laufende Verletzungen durch Dritte mindern den Wert als Sicherheit — Prüfpflicht der Bank.

## Prüfraster

- Ist das Datenbankherstellerrecht klar auf den Kreditnehmer zurückführbar (keine Fremdrechte, keine ungelösten Inhaberschaftsfragen)?
- Kann der Kreditnehmer die wesentliche Investition dokumentieren (Buchhaltung, Projektunterlagen)?
- Wie lang ist die verbleibende Schutzdauer (§ 87d UrhG) — reicht sie für die Kreditlaufzeit?
- Bestehen laufende Datenbanklizenzen, die den Verwertungswert mindern oder erhöhen?
- Sind Dritte vorhanden, die möglicherweise Herstellerrecht an Teilen der Datenbank beanspruchen?
- Enthält die Datenbank personenbezogene Daten — erschwert das die Verwertung im Sicherungsfall?
- Wurde die Sicherungsübertragung/-verpfändung wirksam vereinbart und ggf. im Rechtsverkehr kenntlich gemacht?

## Typische Fallstricke

- Datenbankherstellerrecht ist schwieriger zu bewerten als Patent oder Marke — standardisierte Bewertungsmethoden fehlen weitgehend.
- Verwertung im Sicherungsfall ist komplex — Bank muss entweder einen Käufer für das Recht finden oder selbst Lizenzen vergeben.
- Personenbezogene Daten in der Datenbank schränken den Käuferkreis im Verwertungsfall erheblich ein.
- Ohne laufende Datenbankpflege durch den Kreditnehmer sinkt der Wert der Datenbank rapide — Covenants erforderlich.
- Insolvenzanfechtung bei kurzfristiger Sicherungsübertragung (§ 133 InsO) kann die Sicherheit zunichte machen.

## Output

- IP-Sicherheitenprüfbogen Datenbankrecht (Due-Diligence-Checkliste)
- Sicherungsübertragungsvertrag-Vorlage für Datenbankherstellerrecht
- Wertbewertungsrahmen (Investitionsvolumen, Schutzdauer, Lizenzpotenzial)
- Covenant-Klauseln für Kreditvertrag (Datenbankpflege, Verletzungsabwehr)
- Verwertungsplan-Übersicht für den Sicherungsfall

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87d UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87d.html)
- [§ 1273 BGB Pfandrecht an Rechten — dejure.org](https://dejure.org/gesetze/BGB/1273.html)
- [§ 35 InsO — dejure.org](https://dejure.org/gesetze/InsO/35.html)
- [§ 51 InsO Absonderungsrecht — dejure.org](https://dejure.org/gesetze/InsO/51.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
