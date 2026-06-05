---
name: ausgleich-ma-deal-ausgleichsanmeldung
description: "Ausgleich MA Deal Ausgleichsanmeldung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ausgleich MA Deal Ausgleichsanmeldung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Ausgleich MA Deal Ausgleichsanmeldung** im Plugin Handelsvertreterrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ausgleich-berechnung` | Berechnet den Ausgleichsanspruch nach § 89b HGB: Rohertragsberechnung auf Basis der Jahresprovision, Prognoseabzug für Neukundenentwicklung, Abzinsung, Billigkeitskorrektur sowie Höchstbetragsgrenze einer durchschnittlichen Jahresvergütung nach § 89b Abs. 2 HGB und richtlinienkonformer EuGH-Rechtsprechung. |
| `ausgleich-im-ma-deal` | Analysiert Ausgleichsansprüche bei M&A-Transaktionen: Vertragsübergang nach § 613a BGB analog, Erlöschen des Ausgleichs nach § 89b Abs. 3 Nr. 3 HGB bei Übertragung der Agentur, Gestaltungsmöglichkeiten im Share- vs. Asset-Deal, Haftungszuweisung zwischen Veräußerer und Erwerber sowie Due-Diligence-Checkliste. |
| `ausgleichsanmeldung` | Unterstützt bei fristgerechter Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB: Einhaltung der Jahresfrist ab Vertragsende, Inhalt und Form der Anmeldung, Wahrung gegenüber dem Unternehmer und Rechtsfolgen bei Fristversäumnis; Musterschreiben für Handelsvertreter und Unternehmerseite. |
| `ausgleichsanspruch-89b` | Analysiert den Ausgleichsanspruch des Handelsvertreters nach § 89b HGB vollständig: Entstehungsvoraussetzungen (neue Kunden, wesentliche Erweiterung), Höchstbetrag von einer Jahresprovision, Ausschlussgründe nach § 89b Abs. 3 HGB, Berechnung nach der BGH-Stufenmethode sowie Anmeldefrist nach § 89b Abs. 4 HGB. |

## Arbeitsweg

Im Plugin Handelsvertreterrecht gilt für **Ausgleich MA Deal Ausgleichsanmeldung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ausgleich-berechnung`

**Fokus:** Berechnet den Ausgleichsanspruch nach § 89b HGB: Rohertragsberechnung auf Basis der Jahresprovision, Prognoseabzug für Neukundenentwicklung, Abzinsung, Billigkeitskorrektur sowie Höchstbetragsgrenze einer durchschnittlichen Jahresvergütung nach § 89b Abs. 2 HGB und richtlinienkonformer EuGH-Rechtsprechung.

# Berechnung des Ausgleichsanspruchs nach § 89b HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Berechnung des Ausgleichsanspruchs nach § 89b HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X beendet nach 12 Jahren das Vertreterverhältnis mit Unternehmer Y; X berechnet seinen Ausgleichsanspruch auf Basis der Neukundenprovision der letzten fünf Jahre.
- Unternehmer Y bestreitet die Höhe des Ausgleichs und beauftragt eine Gegenkalkulation unter Berücksichtigung von Kundenabwanderungen und Prognoseabzügen.
- Handelsvertreterin Z ermittelt den Höchstbetrag nach § 89b Abs. 2 HGB als Kappungsgrenze und vergleicht ihn mit der Rohertragsmethode.

## Erste Schritte

1. Jahresprovision der letzten fünf Vertragsjahre aus Abrechnungen ermitteln.
2. Neukundenanteil und wesentlich erweiterter Altkundenanteil herausrechnen.
3. Prognoseabzug für zukünftige Kundenabwanderung schätzen und dokumentieren.
4. Abzinsung des zukünftigen Vorteils für den Unternehmer berechnen.
5. Höchstbetrag nach § 89b Abs. 2 HGB (durchschnittliche Jahresvergütung der letzten fünf Jahre) bestimmen.
6. Billigkeitskorrektur nach § 89b Abs. 1 S. 1 HGB prüfen — Unbilligkeit senkt den Anspruch.

## Rechtsrahmen

- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen und Billigkeit
- § 89b Abs. 2 HGB — Höchstbetrag eine durchschnittliche Jahresvergütung
- § 89b Abs. 3 HGB — Ausschlussgründe
- § 89b Abs. 4 HGB — Anmeldefrist ein Jahr nach Vertragsende
- Art. 17 Abs. 2 RL 86/653/EWG — Berechnungsrahmen des Ausgleichs
- EuGH C-381/19 — Saint-Gobain: Billigkeit bei der Berechnung

## Prüfraster

- Welche Provisionen entfallen auf Neukunden oder wesentliche Erweiterung bestehender Kunden?
- Welcher Prognoseabzug ist für Kundenabwanderung nach Vertragsende sachgerecht?
- Übersteigt der berechnete Rohausgleich den Höchstbetrag nach § 89b Abs. 2 HGB?
- Erfordert die Billigkeit eine Korrektur des errechneten Betrags nach oben oder unten?
- Ist die Ausgleichsanmeldung fristgerecht innerhalb eines Jahres erfolgt?
- Gibt es Ausschlussgründe nach § 89b Abs. 3 HGB, die den Anspruch zum Erlöschen bringen?

## Typische Fallstricke

- Neukundenprovision nicht sauber vom Stammkundenumsatz getrennt — fehlerhafte Berechnungsgrundlage.
- Höchstbetrag nach § 89b Abs. 2 HGB übersehen — Anspruch wird zu hoch angesetzt.
- Prognoseabzug zu pauschal geschätzt — gerichtlich angreifbar.
- Anmeldefrist nach § 89b Abs. 4 S. 2 HGB versäumt — Anspruch erlischt.

## Output

Ausgleichsberechnung (tabellarisch), Höchstbetragsvergleich, Klageschriftentwurf mit Ausgleichsforderung.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [Art. 17 RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [EuGH C-381/19 Saint-Gobain auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A62019CJ0381)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)
- [BGH Rechtsprechung Openjur](https://openjur.de/)

## 2. `ausgleich-im-ma-deal`

**Fokus:** Analysiert Ausgleichsansprüche bei M&A-Transaktionen: Vertragsübergang nach § 613a BGB analog, Erlöschen des Ausgleichs nach § 89b Abs. 3 Nr. 3 HGB bei Übertragung der Agentur, Gestaltungsmöglichkeiten im Share- vs. Asset-Deal, Haftungszuweisung zwischen Veräußerer und Erwerber sowie Due-Diligence-Checkliste.

# Ausgleichsanspruch bei M&A-Transaktionen und Unternehmensübergang

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Ausgleichsanspruch bei M&A-Transaktionen und Unternehmensübergang.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X erfährt, dass Unternehmer Y sein Unternehmen an Erwerber Z verkauft hat; X klärt, ob sein Ausgleichsanspruch gegen Y oder Z geltend zu machen ist.
- Erwerber Z übernimmt im Asset-Deal alle Handelsvertreterverträge; er prüft, ob bestehende Ausgleichsansprüche auf ihn übergehen oder ob Y haftet.
- Im Share-Deal verbleibt der Unternehmer als GmbH; Handelsvertreter X klärt, ob die Veräußerung der Gesellschaftsanteile seine Rechte berührt.

## Erste Schritte

1. Transaktionsstruktur bestimmen: Share-Deal (Anteile) vs. Asset-Deal (Betrieb/Verträge).
2. Vertragsübergang bei Asset-Deal nach § 613a BGB analog oder vertraglicher Übernahme prüfen.
3. Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB: erlischt er bei Vertragsübertragung?
4. Haftungsverteilung zwischen Veräußerer und Erwerber in SPA und Übergangsvertrag prüfen.
5. Ausgleichsrückstellungen in der Bilanz des Unternehmers identifizieren.
6. Due-Diligence-Checkliste für offene Ausgleichsansprüche aller Handelsvertreter erstellen.

## Rechtsrahmen

- § 89b Abs. 3 Nr. 3 HGB — Ausschluss des Ausgleichs bei Übertragung der Agentur
- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen des Ausgleichsanspruchs
- § 613a BGB — Betriebsübergang (analog bei Vertragsübernahme)
- § 25 HGB — Haftung des Erwerbers bei Firmenfortführung
- § 414 BGB — Schuldübernahme
- Art. 17 RL 86/653/EWG — Ausgleichsanspruch bei Vertragsende

## Prüfraster

- Handelt es sich um einen Share-Deal oder Asset-Deal?
- Gehen Handelsvertreterverträge auf den Erwerber über?
- Erlischt der Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB durch Agenturübertragung?
- Wer haftet für Ausgleichsansprüche — Veräußerer, Erwerber oder beide gesamtschuldnerisch?
- Sind bestehende Ausgleichsansprüche in der Due Diligence identifiziert und bewertet?
- Schützt der Kaufvertrag den Erwerber durch Freistellungs- oder Garantieklauseln?

## Typische Fallstricke

- Ausgleichsansprüche in der Due Diligence nicht erfasst — unerwartete Haftung des Erwerbers.
- § 89b Abs. 3 Nr. 3 HGB zu weit ausgelegt — nicht jede Unternehmensübertragung schließt Ausgleich aus.
- Keine klare Haftungsverteilung im SPA — Veräußerer und Erwerber streiten über Freistellung.
- Rückstellungen für Ausgleichsansprüche unzureichend bewertet — Kaufpreisrisiko.

## Output

Due-Diligence-Checkliste Ausgleichsansprüche, Haftungsmatrix, Vertragsentwurf Freistellungsklausel.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 613a BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__613a.html)
- [§ 25 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__25.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

## 3. `ausgleichsanmeldung`

**Fokus:** Unterstützt bei fristgerechter Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB: Einhaltung der Jahresfrist ab Vertragsende, Inhalt und Form der Anmeldung, Wahrung gegenüber dem Unternehmer und Rechtsfolgen bei Fristversäumnis; Musterschreiben für Handelsvertreter und Unternehmerseite.

# Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X hat das Vertreterverhältnis mit Unternehmer Y im März beendet; X prüft, bis wann er den Ausgleichsanspruch anmelden muss und was die Anmeldung enthalten soll.
- Unternehmer Y bestreitet den Ausgleich mit dem Argument, die Anmeldung sei nach Ablauf der Jahresfrist des § 89b Abs. 4 HGB erfolgt.
- Handelsvertreter X meldet den Ausgleich vorsorglich an, bevor die genaue Höhe berechnet ist; er klärt, ob eine Anmeldung dem Grunde nach ausreicht.

## Erste Schritte

1. Datum der Vertragsbeendigung exakt bestimmen (Zeitpunkt der Kündigung oder Aufhebung).
2. Frist berechnen: ein Jahr ab Vertragsende nach § 89b Abs. 4 S. 2 HGB.
3. Anmeldungsschreiben dem Grunde nach formulieren; genaue Höhe muss noch nicht feststehen.
4. Anmeldung per Einschreiben mit Rückschein oder Boten mit Empfangsbestätigung übermitteln.
5. Fristablauf im Kalender notieren und Bestätigung des Erhalts anfordern.
6. Gleichzeitig Provisionsabrechnungen für Ausgleichsberechnung anfordern.

## Rechtsrahmen

- § 89b Abs. 4 S. 2 HGB — Jahresfrist für die Anmeldung des Ausgleichs
- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen des Ausgleichsanspruchs
- § 89b Abs. 2 HGB — Höchstbetrag des Ausgleichs
- § 130 BGB — Wirksamkeit einer empfangsbedürftigen Willenserklärung
- § 193 BGB — Fristverlängerung bei Fristende an Sonn- oder Feiertag
- Art. 17 RL 86/653/EWG — Ausgleichsanspruch nach Vertragsende

## Prüfraster

- Wann endete der Handelsvertretervertrag genau?
- Ist die Jahresfrist nach § 89b Abs. 4 S. 2 HGB noch nicht abgelaufen?
- Enthält die Anmeldung zumindest den Anspruch dem Grunde nach?
- Ist die Anmeldung dem Unternehmer oder seinen Bevollmächtigten zugegangen?
- Wurde der Zugang der Anmeldung dokumentiert (Einschreiben, Empfangsbestätigung)?
- Greift eine Verlängerung nach § 193 BGB, weil der Jahrestag auf einen Feiertag fällt?

## Typische Fallstricke

- Jahresfrist verpasst — der Ausgleichsanspruch erlischt unwiederbringlich.
- Anmeldung nur mündlich erklärt — Nachweis des Zugangs fehlt.
- Falscher Adressat: Anmeldung geht an Niederlassung statt an Hauptsitz des Unternehmers.
- Fristbeginn falsch berechnet: Nicht Kündigungsdatum, sondern Datum der Vertragsbeendigung ist maßgeblich.

## Output

Muster-Anmeldungsschreiben Ausgleichsanspruch, Fristenkalender, Checkliste Zugangsnachweis.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Zwingende Vorschriften nach § 92c HGB können vertraglich nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89, 89a HGB).

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 130 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__130.html)
- [§ 193 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__193.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

## 4. `ausgleichsanspruch-89b`

**Fokus:** Analysiert den Ausgleichsanspruch des Handelsvertreters nach § 89b HGB vollständig: Entstehungsvoraussetzungen (neue Kunden, wesentliche Erweiterung), Höchstbetrag von einer Jahresprovision, Ausschlussgründe nach § 89b Abs. 3 HGB, Berechnung nach der BGH-Stufenmethode sowie Anmeldefrist nach § 89b Abs. 4 HGB.

# Ausgleichsanspruch nach § 89b HGB — Entstehung, Berechnung und Durchsetzung

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Ausgleichsanspruch nach § 89b HGB — Entstehung, Berechnung und Durchsetzung.
Er deckt HGB §§ 84–92c und die EU-Handelsvertreterrichtlinie 86/653/EWG ab.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.
Zwingende Normen (§ 92c HGB) schützen den Handelsvertreter auch bei ausländischer Rechtswahl.
BGH und EuGH haben zentrale Rechtsfragen durch Leitentscheidungen geprägt.

## Mandantenfall

- Handelsvertreter X hat nach fünfjähriger Tätigkeit einen großen Kundenstamm aufgebaut; nach Kündigung durch Unternehmer Y fragt X, wie hoch sein Ausgleich nach § 89b HGB ist.
- Unternehmer Y behauptet, der Ausgleichsanspruch des Handelsvertreters X sei nach § 89b Abs. 3 HGB ausgeschlossen, weil X selbst gekündigt habe; X prüft, ob ein Ausnahmetatbestand greift.
- Anwältin A berechnet den Ausgleich für Handelsvertreter X nach der BGH-Stufenmethode und möchte wissen, welche Provisionsdaten sie für die Berechnung benötigt.

## Erste Schritte

1. Ausgleichsvoraussetzungen nach § 89b Abs. 1 HGB prüfen: neue Kunden, wesentliche Erweiterung.
2. Unternehmervorteile nach Vertragsende als Ausgleichsgrundlage feststellen.
3. Höchstbetrag nach § 89b Abs. 2 HGB: durchschnittliche Jahresprovision der letzten fünf Jahre.
4. Ausschlussgründe nach § 89b Abs. 3 HGB: eigene Kündigung ohne wichtigen Grund, schwere Pflichtverletzung.
5. Anmeldung des Ausgleichs innerhalb eines Jahres nach Vertragsende nach § 89b Abs. 4 HGB.
6. BGH-Stufenmethode anwenden: Rohausgleich, Abwanderungsquote, Billigkeitskorrekturen.

## Rechtsrahmen

- § 89b Abs. 1 HGB — Voraussetzungen: neue Kunden und wesentliche Erweiterung
- § 89b Abs. 2 HGB — Höchstbetrag: eine durchschnittliche Jahresprovision
- § 89b Abs. 3 HGB — Ausschlussgründe: eigene Kündigung ohne wichtigen Grund
- § 89b Abs. 4 HGB — Ausschlussfrist: Anmeldung innerhalb eines Jahres
- Art. 17 RL 86/653/EWG — Europäischer Mindeststandard für den Ausgleich
- § 92c HGB — Ausgleich ist zwingend: vorherige Einschränkung unwirksam

## Prüfraster

- Liegen neue Kunden oder wesentliche Geschäftserweiterung als Ausgleichsvoraussetzung vor?
- Hat der Unternehmer nach Vertragsende nachhaltige Vorteile aus dem Kundenstamm?
- Greift ein Ausschlussgrund nach § 89b Abs. 3 HGB (eigene Kündigung ohne wichtigen Grund)?
- Ist die Anmeldefrist von einem Jahr nach § 89b Abs. 4 HGB gewahrt?
- Überschreitet der Rohausgleich den Höchstbetrag von einer Jahresprovision?
- Sind Billigkeitskorrekturen nach § 89b Abs. 1 S. 1 HGB vorzunehmen?

## Typische Fallstricke

- Ausschlussfrist nach § 89b Abs. 4 HGB versäumt — Anspruch erloschen.
- Eigene Kündigung ohne wichtigen Grund — Ausschlussgrund nach § 89b Abs. 3 HGB.
- Rohausgleich über Höchstbetrag berechnet — Korrektur nach § 89b Abs. 2 HGB vergessen.
- Neue Kunden nicht dokumentiert — Ausgleichsgrundlage nicht nachweisbar.

## Output

Ausgleichsberechnung nach BGH-Stufenmethode, Anmeldefristschreiben, Klageschrift auf Ausgleich.

## Hintergrund und Kontext

Das Handelsvertreterrecht steht im fünften Buch des HGB (§§ 84 bis 92c).
Es gilt als Sonderprivatrecht zwischen Arbeits- und allgemeinem Handelsrecht.
Die EU-Handelsvertreterrichtlinie 86/653/EWG setzt europäische Mindeststandards.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Buchauszug, Ausgleich bei Vertragsende.
Nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Delkredere (§ 86b HGB) regeln Sonderlagen.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Für grenzüberschreitende Sachverhalte bestimmt die Rom-I-Verordnung das anwendbare Recht.
Zwingende Normen wie Ausgleich (§ 89b HGB) und Buchauszug (§ 87c HGB) stehen nicht zur Disposition.
Bei Statusfragen (Selbständigkeit) ist das Statusfeststellungsverfahren nach § 7a SGB IV maßgeblich.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [Art. 17 RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [BGH-Entscheidungen auf bgh.de](https://www.bgh.de/entscheidungen/entscheidungen-online)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)
