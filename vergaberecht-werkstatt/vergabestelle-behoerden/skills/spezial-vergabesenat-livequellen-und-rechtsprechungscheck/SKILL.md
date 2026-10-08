---
name: spezial-vergabesenat-livequellen-und-rechtsprechungscheck
description: 'Rechtsprechungs- und Quellencheck der Vergabestelle für VK und OLG: Normfassung, Entscheidungsstatus, Tenor, Randnummer, regionale Senatslinie, Beschwerdebegründung, Aktenbeleg und Rechtsstand des Paragrafen 173 GWB seit Juli 2026.'
---

# Vergabesenat: Livequellen- und Rechtsprechungscheck

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## 1. Einsatz

Diesen Skill verwenden, wenn eine Rügeerwiderung, VK-Stellungnahme, Beschwerdeerwiderung oder interne Freigabe auf Rechtsprechung gestützt werden soll. Er liefert keine bloße Trefferliste, sondern eine zitierfähige Fallkarte mit Pro- und Contra-Linie.

## 2. Verfahrensstatus zuerst

1. VK-Antrag anhängig, VK-Beschluss ergangen oder sofortige Beschwerde eingelegt?
2. Zustelldatum, Zwei-Wochen-Notfrist und gleichzeitige Begründung nach § 172 GWB gesichert?
3. Wer hat vor der VK obsiegt und welche Zuschlagswirkung folgt daraus?
4. Verfahrensbeginn nach § 187 Abs. 2 GWB belegen. Altverfahren bleiben im früheren Recht. Nur bei Neuverfahren ab 1. Juli 2026 gilt: Nach Ablehnung keine aufschiebende Wirkung gemäß § 173 Abs. 1 GWB; nach Zuschlagsuntersagung Fortwirkung gemäß § 173 Abs. 2 GWB bis zu einer Aufhebung nach §§ 176 oder 178 GWB.

## 3. Quellenhierarchie

1. Aktuelle Norm bei `gesetze-im-internet.de` einschließlich Änderungsstand.
2. EuGH über CURIA oder EUR-Lex; ECLI, Datum, Tenor und Randnummer.
3. BGH/BVerfG über amtliche Entscheidungsdatenbank.
4. Zuständiger OLG-Vergabesenat über amtliches Landesportal oder Gerichtsseite.
5. Vergabekammer über Bundeskartellamt oder amtliche Landesquelle.
6. Freie Fundstelle nur als Auffindehilfe kennzeichnen; keine paywallgebundene Fundstelle ohne bereitgestellten Volltext als geprüft ausgeben.

## 4. Fallkartenworkflow

| Feld | Inhalt |
| --- | --- |
| Rechtsfrage | [präziser Obersatz] |
| Normfassung/Stichtag | [Norm, Fassung, Inkrafttreten] |
| Entscheidung | [Gericht, Datum, Az./ECLI] |
| Verfahrenslage | [Vorlagefrage, Beschwerde, Feststellung] |
| Tragende Aussage | [paraphrasiert] |
| Randnummer | [Rn.] |
| Sachverhaltsnähe | [gleich/ähnlich/abweichend] |
| Nutzen Vergabestelle | [Argument] |
| Gegenargument | [Bieterlinie] |
| Primärquelle | [Link und Abrufdatum] |

Pro Rechtsfrage mindestens einen tragenden Anker und, wenn auffindbar, die stärkste Gegenlinie dokumentieren. Keine Entscheidung allein nach Überschrift übernehmen.

## 5. Beschwerdeerwiderungsprüfung

- Beschwerdebefugnis und bestimmte Anträge.
- § 172 GWB: zwei Wochen, zugleich begründet, Tatsachen und Beweismittel, Unterschrift, Unterrichtung der übrigen Beteiligten.
- Bindung jedes Arguments an VK-Beschluss, Vergabeakte und konkrete Aktenstelle.
- Neue Tatsachen, Geheimnisschutz und Akteneinsicht gesondert behandeln.
- Bei § 176 GWB nur den gesetzlich eröffneten Vorabgestattungsantrag von Auftraggeber oder vorgesehenem Zuschlagsempfänger bearbeiten; Tatsachen und Eilgrund glaubhaft machen.

## 6. Rechtsprechungscluster

| Thema | Startanker |
| --- | --- |
| Antragsbefugnis | BGH X ZB 14/06; EuGH Fastweb/PFE/Randstad |
| Wertung | EuGH C-19/00 SIAC; C-532/06 Lianakis |
| Preisaufklärung | BGH X ZB 10/16 |
| Produkt-/Formatvorgabe | EuGH C-424/23 DYKA Plastics |
| Vertragsänderung | EuGH C-454/06 pressetext; C-282/24 Polismyndigheten |
| Ausschluss/Selbstreinigung | EuGH C-41/18 Meca; C-267/18 Delta; C-124/17 Vossloh Laeis |

## 7. Output

Ausgeben: Quellenstatus-Tabelle, höchstens zehn tragende Fallkarten, Gegenargumentmatrix und einsetzbare Beschwerdeerwiderungsabschnitte mit Aktenfundstellen. Unbestätigte Treffer werden sichtbar als Suchhinweis, nicht als Zitat, markiert.
## Quellenregel

Jede tragende Aussage braucht Primärquelle, Abrufdatum und Randnummer. Abweichende Normfassungen vor und nach dem 1. Juli 2026 anhand des § 187 Abs. 2 GWB ausdrücklich trennen.
