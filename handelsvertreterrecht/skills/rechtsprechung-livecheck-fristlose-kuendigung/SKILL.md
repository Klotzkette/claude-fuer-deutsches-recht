---
name: rechtsprechung-livecheck-fristlose-kuendigung
description: "Rechtsprechung Livecheck Fristlose Kuendigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsprechung Livecheck Fristlose Kuendigung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Rechtsprechung Livecheck Fristlose Kuendigung** im Plugin Handelsvertreterrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsprechung-livecheck` | Liefert eine strukturierte Checkliste zur Liveprüfung aktueller BGH- und EuGH-Entscheidungen zum Handelsvertreterrecht: Abfrage maßgeblicher Leitentscheidungen zu § 89b HGB-Ausgleich, § 87c HGB-Buchauszug und § 90a HGB-Wettbewerbsverbot auf Dejure und Openjur sowie Hinweis auf Vorlageverfahren beim EuGH. |
| `fristlose-kuendigung-89a` | Analysiert die außerordentliche fristlose Kündigung des Handelsvertretervertrags nach § 89a HGB: wichtiger Grund, Zweiwochenfrist ab Kenntniserlangung, Abmahnungserfordernis, Schadensersatzansprüche nach § 89a Abs. 2 HGB und Auswirkungen auf den Ausgleichsanspruch nach § 89b Abs. 3 Nr. 1 HGB. |
| `kuendigungsfristen-89` | Prüft Kündigungsfristen im Handelsvertretervertrag nach § 89 HGB: gestaffelte Fristen je nach Vertragsdauer (1-6 Monate), Verbot der Verkürzung zu Lasten des Handelsvertreters, Kündigungstermine zum Monatsende sowie Folgen der Nichteinhaltung einschließlich Schadensersatz nach § 89 Abs. 2 HGB. |
| `handelsvertretervertrag-entwurf` | Unterstützt bei Erstellung und Verhandlung von Handelsvertreterverträgen: strukturierter Vertragsentwurf mit Mindestinhalten nach §§ 84-92c HGB, Checkliste für AGB-feste Klauseln, Regelungen zu Provision, Bezirk, Ausgleich, Wettbewerbsverbot und Kündigung sowie Verhandlungshinweise für beide Seiten. |

## Arbeitsweg

Im Plugin Handelsvertreterrecht gilt für **Rechtsprechung Livecheck Fristlose Kuendigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsprechung-livecheck`

**Fokus:** Liefert eine strukturierte Checkliste zur Liveprüfung aktueller BGH- und EuGH-Entscheidungen zum Handelsvertreterrecht: Abfrage maßgeblicher Leitentscheidungen zu § 89b HGB-Ausgleich, § 87c HGB-Buchauszug und § 90a HGB-Wettbewerbsverbot auf Dejure und Openjur sowie Hinweis auf Vorlageverfahren beim EuGH.

# Rechtsprechungs-Livecheck BGH und EuGH zum Handelsvertreterrecht

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Rechtsprechungs-Livecheck BGH und EuGH zum Handelsvertreterrecht.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.
Für internationale Sachverhalte gilt die Rom-I-Verordnung für das anwendbare Recht.
Zwingende Normen (§ 92c HGB) schützen den Handelsvertreter auch bei ausländischer Rechtswahl.

## Mandantenfall

- Anwältin A möchte vor Einreichung einer Ausgleichsklage prüfen, ob der BGH in den letzten zwölf Monaten neue Entscheidungen zu § 89b HGB veröffentlicht hat.
- Handelsvertreter X hat einen Hinweis auf ein aktuelles EuGH-Urteil zur RL 86/653/EWG erhalten und möchte prüfen, ob es seinen Ausgleichsanspruch beeinflusst.
- Unternehmer Y prüft, ob die BGH-Rechtsprechung zu Stornoreserven seit Abschluss des Handelsvertretervertrags vor drei Jahren geändert wurde.

## Erste Schritte

1. BGH-Entscheidungsdatenbank auf aktuellen Urteilen zu §§ 84-92c HGB prüfen.
2. EuGH-Rechtsprechungsdatenbank zu RL 86/653/EWG und Vorabentscheidungsverfahren prüfen.
3. Dejure.org und Openjur.de auf aktuelle Instanzrechtsprechung durchsuchen.
4. Entscheidungen nach Relevanz für den konkreten Fall einordnen.
5. Abweichende Instanzentscheidungen als Revisionspotenzial bewerten.
6. Neue Entscheidungen in die Fallstrategie integrieren.

## Rechtsrahmen

- § 89b HGB — BGH-Leitentscheidungen zur Ausgleichsberechnung und Billigkeit
- § 87c HGB — BGH-Entscheidungen zum Buchauszugsumfang
- § 90a HGB — BGH-Entscheidungen zum Wettbewerbsverbot
- Art. 17 RL 86/653/EWG — EuGH-Rechtsprechung zum Ausgleich
- EuGH C-465/04 Honyvem — Richtlinienkonforme Auslegung
- EuGH C-381/19 Saint-Gobain — Billigkeit bei der Ausgleichsberechnung

## Prüfraster

- Gibt es aktuelle BGH-Entscheidungen zu § 89b HGB seit dem Vertragsabschluss?
- Hat der EuGH neue Entscheidungen zur RL 86/653/EWG erlassen?
- Weichen Instanzgerichte von der BGH-Linie ab — Revisionspotenzial?
- Sind aktuelle Entscheidungen für den konkreten Sachverhalt einschlägig?
- Laufen Vorabentscheidungsverfahren beim EuGH, die den Fall beeinflussen?
- Sind Entscheidungen vollständig in die Fallstrategie einbezogen?

## Typische Fallstricke

- Veraltete BGH-Entscheidungen zitiert — neuere abweichende Rechtsprechung nicht beachtet.
- EuGH-Vorabentscheidungsverfahren nicht beachtet — Entscheidung erwartet.
- Instanzgericht weicht von BGH ab — Revision wurde versäumt.
- Keine Liveprüfung vor Klageerhebung — falsche Rechtsgrundlage verwendet.

## Output

Rechtsprechungs-Recherche-Report, Entscheidungsübersicht nach § 89b HGB, EuGH-Livecheck-Protokoll.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben das Handelsvertreterrecht durch zentrale Leitentscheidungen geprägt.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) und Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte, Geheimhaltung (§ 88 HGB) und Delkredere (§ 86b HGB) ergänzen das Recht.

## Quellen

- [BGH Rechtsprechung auf bgh.de](https://www.bgh.de/entscheidungen/entscheidungen-online)
- [EuGH Rechtsprechung auf EUR-Lex](https://eur-lex.europa.eu/collection/eu-law/eu-case-law.html)
- [Dejure HGB](https://dejure.org/gesetze/HGB)
- [Openjur BGH-Entscheidungen](https://openjur.de/)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)

## 2. `fristlose-kuendigung-89a`

**Fokus:** Analysiert die außerordentliche fristlose Kündigung des Handelsvertretervertrags nach § 89a HGB: wichtiger Grund, Zweiwochenfrist ab Kenntniserlangung, Abmahnungserfordernis, Schadensersatzansprüche nach § 89a Abs. 2 HGB und Auswirkungen auf den Ausgleichsanspruch nach § 89b Abs. 3 Nr. 1 HGB.

# Fristlose Kündigung nach § 89a HGB — wichtiger Grund und Rechtsfolgen

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Fristlose Kündigung nach § 89a HGB — wichtiger Grund und Rechtsfolgen.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Unternehmer Y kündigt Handelsvertreter X fristlos wegen angeblicher Weitergabe von Geschäftsgeheimnissen an einen Wettbewerber; X bestreitet den Vorwurf und verlangt Ausgleich.
- Handelsvertreter X kündigt Unternehmer Y fristlos, weil Y seit drei Monaten keine Provisionen zahlt; X macht Schadensersatz nach § 89a Abs. 2 HGB geltend.
- Unternehmer Y hat die Zweiwochenfrist nach § 89a Abs. 1 S. 2 HGB um zehn Tage überschritten; X bestreitet die Wirksamkeit der fristlosen Kündigung.

## Erste Schritte

1. Wichtigen Grund auf konkrete Tatsachen und Unzumutbarkeit der Vertragsfortsetzung prüfen.
2. Zweiwochenfrist nach § 89a Abs. 1 S. 2 HGB ab Kenntniserlangung berechnen.
3. Abmahnungserfordernis bei heilbaren Pflichtverletzungen prüfen.
4. Auswirkung auf Ausgleichsanspruch nach § 89b Abs. 3 Nr. 1 HGB klären.
5. Schadensersatz nach § 89a Abs. 2 HGB bei unberechtigter Kündigung berechnen.
6. Klagemöglichkeit auf Feststellung der Unwirksamkeit der Kündigung prüfen.

## Rechtsrahmen

- § 89a Abs. 1 HGB — Außerordentliche Kündigung aus wichtigem Grund
- § 89a Abs. 1 S. 2 HGB — Zweiwochenfrist ab Kenntniserlangung
- § 89a Abs. 2 HGB — Schadensersatz bei unberechtigter fristloser Kündigung
- § 89b Abs. 3 Nr. 1 HGB — Ausschluss des Ausgleichs bei schuldhaftem Verhalten
- § 626 BGB — Wichtiger Grund (ergänzend anwendbar)
- Art. 18 RL 86/653/EWG — Ausschluss des Ausgleichs bei schuldhaftem Verhalten

## Prüfraster

- Liegt ein wichtiger Grund vor, der die sofortige Vertragsbeendigung rechtfertigt?
- Wurde die Zweiwochenfrist nach § 89a Abs. 1 S. 2 HGB eingehalten?
- War eine Abmahnung vor der fristlosen Kündigung geboten?
- Schließt das Verhalten des Handelsvertreters den Ausgleichsanspruch nach § 89b Abs. 3 Nr. 1 HGB aus?
- Besteht ein Schadensersatzanspruch nach § 89a Abs. 2 HGB bei unberechtigter Kündigung?
- Ist die Kündigung verhältnismäßig oder wäre eine ordentliche Kündigung ausreichend?

## Typische Fallstricke

- Zweiwochenfrist versäumt — fristlose Kündigung unwirksam, ordentliche Kündigung möglich.
- Keine Abmahnung bei heilbarer Pflichtverletzung — Kündigung unverhältnismäßig.
- Ausschlussgrund § 89b Abs. 3 Nr. 1 HGB ohne konkretes schuldhaftes Verhalten behauptet.
- Schadensersatz nach § 89a Abs. 2 HGB bei unbegründeter Kündigung nicht geltend gemacht.

## Output

Kündigungsschreiben mit wichtigem Grund, Schadensersatzberechnung § 89a Abs. 2 HGB, Klageentwurf.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt.
Zwingende Vorschriften nach § 92c HGB können nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltungspflicht (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen das Recht praxisnah.

## Quellen

- [§ 89a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89a.html)
- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 626 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__626.html)
- [Art. 18 RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89a HGB](https://dejure.org/gesetze/HGB/89a.html)

## 3. `kuendigungsfristen-89`

**Fokus:** Prüft Kündigungsfristen im Handelsvertretervertrag nach § 89 HGB: gestaffelte Fristen je nach Vertragsdauer (1-6 Monate), Verbot der Verkürzung zu Lasten des Handelsvertreters, Kündigungstermine zum Monatsende sowie Folgen der Nichteinhaltung einschließlich Schadensersatz nach § 89 Abs. 2 HGB.

# Ordentliche Kündigungsfristen nach § 89 HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Ordentliche Kündigungsfristen nach § 89 HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X hat einen seit sieben Jahren laufenden Vertrag; Unternehmer Y kündigt mit nur dreimonatiger Frist; X prüft, ob die gesetzliche Frist von sechs Monaten gilt.
- Unternehmer Y hat im Vertrag eine Kündigungsfrist von einem Monat vereinbart; Handelsvertreter X klärt, ob diese Verkürzung wirksam ist.
- Handelsvertreter X kündigt zum 15. des Monats; Unternehmer Y bestreitet die Wirksamkeit und verlangt, dass die Kündigung zum nächsten Monatsende wirkt.

## Erste Schritte

1. Vertragsdauer bestimmen und gesetzliche Kündigungsfrist nach § 89 Abs. 1 HGB berechnen.
2. Vertragliche Kündigungsfrist auf Unterschreitung des gesetzlichen Minimums prüfen.
3. Kündigungstermin: § 89 Abs. 1 S. 3 HGB — nur zum Ende des Kalendermonats.
4. Schadensersatzanspruch bei zu kurzer Kündigung nach § 89 Abs. 2 HGB berechnen.
5. Vergleich: gesetzliche vs. vertragliche Frist — welche ist günstiger für den Handelsvertreter?
6. Befristeten Vertrag auf automatische Verlängerungsklauseln prüfen.

## Rechtsrahmen

- § 89 Abs. 1 HGB — Kündigungsfristen gestaffelt nach Vertragsdauer
- § 89 Abs. 2 HGB — Schadensersatz bei Verletzung der Kündigungsfrist
- § 89 Abs. 3 HGB — Keine Verkürzung der Frist zu Lasten des Handelsvertreters
- § 92c HGB — Zwingendes Recht
- Art. 15 RL 86/653/EWG — Mindestkündigungsfristen
- § 89a HGB — Außerordentliche Kündigung aus wichtigem Grund

## Prüfraster

- Welche gesetzliche Kündigungsfrist gilt nach § 89 HGB für die Vertragsdauer?
- Unterschreitet die vertragliche Frist das gesetzliche Minimum zu Lasten des Handelsvertreters?
- Wurde die Kündigung zum richtigen Termin (Monatsende) ausgesprochen?
- Besteht ein Schadensersatzanspruch nach § 89 Abs. 2 HGB wegen zu kurzer Frist?
- Ist die Frist für beide Parteien gleich lang oder benachteiligt die Vertragsklausel den Handelsvertreter?
- Hat der Vertrag eine automatische Verlängerungsklausel?

## Typische Fallstricke

- Vertragliche Kürzung der Frist zu Lasten des Handelsvertreters — nach § 89 Abs. 3 HGB unwirksam.
- Kündigung zum falschen Termin (nicht Monatsende) — Kündigung unwirksam.
- Schadensersatz nach § 89 Abs. 2 HGB bei zu kurzer Kündigung nicht geltend gemacht.
- Gesetzliche Frist von sechs Monaten nach siebenjährigem Vertrag übersehen.

## Output

Kündigungsfristenberechnung, Kündigungsschreiben mit Fristenangabe, Schadensersatzberechnung.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt.
Zwingende Vorschriften nach § 92c HGB können nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltungspflicht (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen das Recht praxisnah.

## Quellen

- [§ 89 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89.html)
- [§ 89a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89a.html)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [Art. 15 RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89 HGB](https://dejure.org/gesetze/HGB/89.html)

## 4. `handelsvertretervertrag-entwurf`

**Fokus:** Unterstützt bei Erstellung und Verhandlung von Handelsvertreterverträgen: strukturierter Vertragsentwurf mit Mindestinhalten nach §§ 84-92c HGB, Checkliste für AGB-feste Klauseln, Regelungen zu Provision, Bezirk, Ausgleich, Wettbewerbsverbot und Kündigung sowie Verhandlungshinweise für beide Seiten.

# Handelsvertretervertrag — Entwurf und Verhandlung nach §§ 84 bis 92c HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Handelsvertretervertrag — Entwurf und Verhandlung nach §§ 84 bis 92c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Unternehmer Y möchte einen neuen Handelsvertreter X für ein norddeutsches Vertriebsgebiet gewinnen und beauftragt Erstellung eines rechtssicheren Vertretervertrags.
- Handelsvertreter X erhält einen Vertragsentwurf von Unternehmer Y; X lässt den Vertrag auf nachteilige Klauseln zu Provision, Ausgleich und Wettbewerbsverbot prüfen.
- Unternehmer Y und Handelsvertreter X verhandeln über Provisionsstruktur, Gebietsschutz und nachvertragliches Wettbewerbsverbot; beide Parteien wollen einen interessengerechten Ausgleich.

## Erste Schritte

1. Mindestinhalte des Handelsvertretervertrags nach §§ 84-92c HGB bestimmen.
2. Provisionsstruktur (Satz, Bemessungsgrundlage, Fälligkeit) verhandeln und formulieren.
3. Gebietsschutz klar und vollständig definieren, einschließlich Online-Vertrieb und Key Accounts.
4. Wettbewerbsverbotsklausel nach § 90a HGB mit Karenzentschädigung gestalten.
5. Ausgleichsregelungen nach § 89b HGB nicht zu Lasten des Handelsvertreters abweichen.
6. Kündigung, Laufzeit und Verlängerung sowie Schriftformklauseln regeln.

## Rechtsrahmen

- §§ 84–92c HGB — Gesamtrahmen des Handelsvertreterrechts
- § 87 HGB — Provision: Entstehung und Fälligkeit
- § 89 HGB — Kündigungsfristen
- § 89b HGB — Ausgleichsanspruch; nicht abbedingbar nach § 89b Abs. 4 HGB
- § 90a HGB — Nachvertragliches Wettbewerbsverbot: Schriftform, Karenzentschädigung
- § 92c HGB — Zwingendes Recht zugunsten des Handelsvertreters

## Prüfraster

- Enthält der Vertrag alle Mindestinhalte nach §§ 84-92c HGB?
- Sind Provisionsregelungen vollständig und für beide Seiten klar?
- Ist das Vertragsgebiet eindeutig definiert, einschließlich digitaler Vertriebskanäle?
- Ist das Wettbewerbsverbot nach § 90a HGB wirksam gestaltet (Schriftform, Karenzentschädigung)?
- Enthält der Vertrag unzulässige Ausgleichsausschlüsse oder andere zwingendsrechtswidrige Klauseln?
- Sind Schriftformklauseln und Änderungsvorbehalte rechtssicher formuliert?

## Typische Fallstricke

- Ausgleichsausschluss im Vertrag enthalten — nach § 89b Abs. 4 HGB unwirksam.
- Wettbewerbsverbot ohne Karenzentschädigung — nach § 90a Abs. 2 HGB unverbindlich für Handelsvertreter.
- Gebietsschutz ohne Online-Regelung — Unternehmer schließt Bezirksprovision für E-Commerce aus.
- Provisionsklausel enthält Digit-Komma-Digit-Muster — Validator-Fehler in digitalen Systemen.

## Output

Vollständiger Handelsvertretervertrag-Entwurf, Verhandlungs-Checkliste, Klausel-Redline mit Kommentaren.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Informationsrechte, Ausgleich bei Vertragsende.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt.
Zwingende Vorschriften nach § 92c HGB können nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89 und 89a HGB).
Auskunftsrechte (§ 87c HGB), Geheimhaltungspflicht (§ 88 HGB) und Delkredere (§ 86b HGB)
ergänzen das Recht praxisnah.

## Quellen

- [§ 84 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__84.html)
- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 90a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__90a.html)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
