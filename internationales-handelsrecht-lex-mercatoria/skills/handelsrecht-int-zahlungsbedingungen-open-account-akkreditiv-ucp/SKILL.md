---
name: handelsrecht-int-zahlungsbedingungen-open-account-akkreditiv-ucp
description: "INT Zahlungsbedingungen Open Account Akkreditiv UCP: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INT Zahlungsbedingungen Open Account Akkreditiv UCP

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **INT Zahlungsbedingungen Open Account Akkreditiv UCP** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-036-zahlungsbedingungen-open-account` | Internationales Handelsrecht: Zahlungsbedingungen im internationalen Handel. Open Account, Cash in Advance, Dokumenteninkasso (URC 522), Akkreditiv (UCP 600) und Bankgarantie (URDG 758) im Risikoranking. Zahlungsverzug (EU-ZahlungsverzugsRL 2011/7/EU). |
| `ihl-037-akkreditiv-ucp-600` | Internationales Handelsrecht: Dokumentenakkreditiv nach UCP 600 (ICC 2007). Abstraktionsprinzip, konforme Dokumentenvorlage, Prüffrist 5 Bankarbeitstage (Art. 14b), Diskrepanzbehandlung, eUCP 2.0 und häufige Fehler bei Akkreditivdokumenten. |
| `ihl-038-standby-letter-isp98` | Internationales Handelsrecht: Standby Letter of Credit nach ISP98 (ICC 1998). Abgrenzung zu Akkreditiv und Bankgarantie, Demand-Charakter, ISP98 Rule 1.06 (Unabhängigkeit), Rule 4 (Dokumentenprüfung) und häufige Einsatzgebiete. |
| `ihl-039-bankgarantie-urgd` | Internationales Handelsrecht: Nachfrage-Bankgarantien nach URDG 758 (ICC 2010). Demand-Charakter, Unabhängigkeitsprinzip, Arten (Bietungsgarantie, Erfüllungsgarantie, Anzahlungsgarantie), Gegengarantie und Missbrauchsschutz. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **INT Zahlungsbedingungen Open Account Akkreditiv UCP**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-036-zahlungsbedingungen-open-account`

**Fokus:** Internationales Handelsrecht: Zahlungsbedingungen im internationalen Handel. Open Account, Cash in Advance, Dokumenteninkasso (URC 522), Akkreditiv (UCP 600) und Bankgarantie (URDG 758) im Risikoranking. Zahlungsverzug (EU-ZahlungsverzugsRL 2011/7/EU).

# Zahlungsbedingungen: Open Account und Trade Finance

## Worum es geht

Die Wahl der Zahlungsbedingung ist eine Risikozuweisung: Cash in Advance schützt Verkäufer vollständig; Open Account das Käuferrisiko minimal. Dazwischen liegen Dokumenteninkasso (Bankweiterleitung ohne Zahlungsgarantie) und Akkreditiv (Bankzahlungsversprechen). Die EU-Zahlungsverzugs-RL (2011/7/EU) gibt 30/60-Tage-Zahlungsfristen im B2B-Handel.

## Kernnormen / Kernquellen

- **UCP 600 (ICC, 2007)**: Einheitliche Richtlinien für Dokumentenakkreditive
- **URC 522 (ICC, 1995)**: Einheitliche Richtlinien für Inkasso
- **URDG 758 (ICC, 2010)**: Einheitliche Richtlinien für Demand Guarantees
- **EU-ZahlungsverzugsRL 2011/7/EU Art. 3-4**: 30/60-Tage-Fristen, Verzugszinsen (8%+EZB-Basiszins)
- **CISG Art. 59**: Pflicht zur Zahlung ohne Aufforderung
- **BGB § 270**: Zahlungsort — Schickschuld im deutschen Recht

## Schlüsselbegriffe

- Open Account (OA): Zahlung nach Lieferung — Verkäuferrisiko maximal
- Cash in Advance (CIA): Vorauszahlung — Käuferrisiko maximal
- Dokumenteninkasso (D/P, D/A): Bank leitet Dokumente weiter, zahlt aber nicht selbst
- Akkreditiv: unwiderrufliches Bankzahlungsversprechen bei Dokumentenkonformität
- Zahlungsverzugszins: 8% über EZB-Basiszins (EU-RL); ab 30/60 Tagen automatisch

## Typische Streitfragen / Anwendungsfälle

1. Open Account mit neuem Kunden: Welche Sicherheiten (Kreditversicherung, Bürgschaft)?
2. D/P Inkasso: Käufer nimmt Dokumente und zahlt nicht — was kann Verkäufer tun?
3. Akkreditiv vs. Bankgarantie: Wann welches Instrument für internationale Anzahlungen?
4. EU-ZahlungsverzugsRL: Gilt automatisch 30 Tage oder kann B2B abweichen?
5. CISG Art. 59: Muss Verkäufer nach CISG Rechnung stellen um Fälligkeit auszulösen?

## Methodik

- Zahlungsbedingung nach Länderrisiko, Kundenkenntnis und Transaktionswert wählen
- Dokumenteninkasso: URC 522 als AGB in Inkassoauftrag einbeziehen
- Akkreditiv: UCP 600 als Grundlage, eUCP für elektronische Dokumente
- Zahlungsverzugs-Monitoring: Fälligkeitsdatum und 30-Tage-Frist dokumentieren

## Output

- Zahlungsbedingungen-Risikoranking (CIA bis OA)
- Zahlungsverzug-Mahnschreiben-Muster (EU-RL-Zinsen)
- Akkreditiv vs. Inkasso Entscheidungsmatrix

## Quellenregel

UCP 600: iccwbo.org. URC 522: iccwbo.org. EU-ZahlungsverzugsRL 2011/7/EU: eur-lex.europa.eu. CISG Art. 59: uncitral.un.org. Unsicherheit bleibt sichtbar.

## 2. `ihl-037-akkreditiv-ucp-600`

**Fokus:** Internationales Handelsrecht: Dokumentenakkreditiv nach UCP 600 (ICC 2007). Abstraktionsprinzip, konforme Dokumentenvorlage, Prüffrist 5 Bankarbeitstage (Art. 14b), Diskrepanzbehandlung, eUCP 2.0 und häufige Fehler bei Akkreditivdokumenten.

# Akkreditiv nach UCP 600

## Worum es geht

Das Dokumentenakkreditiv (Letter of Credit, L/C) ist die sicherste Zahlungsform im internationalen Handel: Die Bank des Käufers verpflichtet sich unwiderruflich zur Zahlung gegen konforme Dokumente. UCP 600 (ICC Uniform Customs and Practice for Documentary Credits, 2007, 39 Artikel) regelt weltweit den Standard. Wichtigste Neuerung: 5-Bankarbeitstage-Prüffrist (Art. 14 lit. b) und strengere Diskrepanzbehandlung.

## Kernnormen / Kernquellen

- **UCP 600 Art. 2**: Definitionen — Honour, Presentation, Complying Presentation
- **UCP 600 Art. 5**: Dokumente (nicht Waren, Dienstleistungen, Vertragserfüllung)
- **UCP 600 Art. 14**: Dokumentenprüfung — 5-Bankarbeitstage, Compliance-Standard
- **UCP 600 Art. 16**: Diskrepante Dokumente — Ablehnung, Waiver, Halten auf Anweisung
- **UCP 600 Art. 20**: Konnossement-Anforderungen
- **eUCP v2.0 (ICC 2019)**: Elektronische Präsentation — Ergänzung zu UCP 600

## Schlüsselbegriffe

- Abstraktionsprinzip: Akkreditiv unabhängig von Grundgeschäft und Transportvertrag
- Strikte Konformität: Dokumente müssen akkreditiv-konform sein (keine Substanzdivergenz geduldet)
- Soft-Law: UCP 600 ist keine Rechtsverordnung — gilt nur durch Einbeziehung ("subject to UCP 600")
- Diskrepanz: jede Abweichung vom Akkreditiv-Wortlaut → Ablehnung möglich
- Fraud: Betrugsverdacht als einzige Ausnahme zum Abstraktionsprinzip (englisches/deutsches Recht)

## Typische Streitfragen / Anwendungsfälle

1. Tippfehler im Dokumenten-Empfängernamen: Diskrepanz oder tolerierbar?
2. Art. 14 lit. b: Was passiert wenn Bank 5-Tage-Frist überschreitet?
3. Akkreditiv-Fraud: Wann kann Käufer Injunction gegen Zahlung erwirken?
4. eUCP: Kann Konnossement als PDF-Dokument unter eUCP präsentiert werden?
5. Transferables Akkreditiv Art. 38 UCP: Kann Händler L/C auf Zulieferer übertragen?

## Methodik

- Akkreditiv-Eröffnung: Alle Dokumentenanforderungen klar mit Käufer abstimmen
- Dokumentenprüfung: Checkliste UCP 600 Art. 20-28 für jedes Dokumententyp
- Diskrepanz-Management: Waiver-Anfrage vs. Neuvorlage vs. Ablehnung priorisieren
- eUCP: nur wenn Akkreditiv ausdrücklich eUCP einbezieht

## Output

- UCP 600 Dokumenten-Prüfcheckliste (Konnossement, Rechnung, Packzettel, Versicherung)
- Diskrepanz-Behandlungs-Flowchart
- eUCP 2.0 Einbeziehungsklausel-Muster

## Quellenregel

UCP 600: iccwbo.org. eUCP 2.0: iccwbo.org. ICC Opinions on UCP 600: iccwbo.org. Schrifttum: Byrne, The Comparison of UCP 600 (2007). Unsicherheit bleibt sichtbar.

## 3. `ihl-038-standby-letter-isp98`

**Fokus:** Internationales Handelsrecht: Standby Letter of Credit nach ISP98 (ICC 1998). Abgrenzung zu Akkreditiv und Bankgarantie, Demand-Charakter, ISP98 Rule 1.06 (Unabhängigkeit), Rule 4 (Dokumentenprüfung) und häufige Einsatzgebiete.

# Standby Letter of Credit nach ISP98

## Worum es geht

Der Standby Letter of Credit (SBLC) ist ein auf Ersterstkenntnisfordering basierendes Sicherungsmittel — die Bank zahlt bei Vorlage einer Zahlungsaufforderung und ggf. Dokument. ISP98 (International Standby Practices 1998, ICC Publication 590) bietet den spezialisierten Rechtsrahmen für SBLCs; UCP 600 kann alternativ angewendet werden, ist aber für Standby weniger geeignet.

## Kernnormen / Kernquellen

- **ISP98 Rule 1.06**: Unabhängigkeit — SBLC unabhängig vom Grundgeschäft
- **ISP98 Rule 2.01**: Geeignete Präsentation
- **ISP98 Rule 4.01-4.20**: Dokumentenprüfung — flexible Standards für Demand-Dokumente
- **ISP98 Rule 6.01**: Transferabilität (Standby-spezifisch)
- **UCP 600 Art. 1**: UCP 600 gilt auch für Standbys (subsidiär zu ISP98)
- **URDG 758 (ICC 2010)**: Alternative — Demand Guarantee (vergleichbar aber eigenständig)

## Schlüsselbegriffe

- Demand-Charakter: Zahlung auf erste Anforderung + Erklärung über Vertragsverletzung
- Unabhängigkeitsprinzip (ISP98 Rule 1.06): Einwendungen aus Grundgeschäft grundsätzlich irrelevant
- Automatic Extension: "Evergreen"-Klausel verlängert SBLC automatisch
- SBLC vs. Bankgarantie: juristisch ähnlich, aber SBLC US-Bankrecht, Garantie kontinentaleuropäisch
- Fraud-Ausnahme: Missbrauch der SBLC durch Begünstigten — nationale Gerichte können Injunction gewähren

## Typische Streitfragen / Anwendungsfälle

1. SBLC-Abruf bei Vertragstreit: Kann Käufer Gerichtsverfügung gegen Zahlung erwirken?
2. ISP98 vs. UCP 600: Welcher Standard wenn Akkreditiv "subject to UCP 600 or ISP98"?
3. Automatic Extension: Wann und wie kann Emittent Verlängerung ablehnen?
4. Transfer nach ISP98 Rule 6: Kann SBLC auf Tochtergesellschaft des Begünstigten übertragen werden?
5. SBLC vs. URDG 758 Garantie: Welches Instrument bei Bietungsgarantie in internationalem Tender?

## Methodik

- ISP98 vs. UCP 600 Wahl: ISP98 bevorzugt für Standbys (spezifischeres Regime)
- Abrufbedingungen: klar und so simpel wie möglich definieren
- Anti-Fraud: Gerichtsstandsklausel für Injunction-Fälle mitdenken
- Evergreen-Klausel: Ablaufdatum und Nichterneuerungs-Notifikationsfrist sorgfältig prüfen

## Output

- ISP98 vs. UCP 600 Vergleich für Standbys
- SBLC-Einsatzfälle-Matrix (Zahlungssicherung, Bietungsgarantie, Performance Bond)
- Anti-Fraud-Clause-Muster

## Quellenregel

ISP98: iccwbo.org (ICC Publication 590). URDG 758: iccwbo.org. UCP 600: iccwbo.org. Schrifttum: Byrne, International Standby Practices (ISP98) (1998). Unsicherheit bleibt sichtbar.

## 4. `ihl-039-bankgarantie-urgd`

**Fokus:** Internationales Handelsrecht: Nachfrage-Bankgarantien nach URDG 758 (ICC 2010). Demand-Charakter, Unabhängigkeitsprinzip, Arten (Bietungsgarantie, Erfüllungsgarantie, Anzahlungsgarantie), Gegengarantie und Missbrauchsschutz.

# Bankgarantien nach URDG 758

## Worum es geht

URDG 758 (Uniform Rules for Demand Guarantees, ICC 2010) ist das wichtigste Regelwerk für Nachfrage-Bankgarantien weltweit. Eine Demand Guarantee verpflichtet die Garantiebank zur Zahlung auf erste Anforderung und Vorlage einer Erklärung über Vertragsverletzung. URDG 758 bietet Gleichgewicht zwischen Begünstigten-Schutz und Missbrauchsprävention.

## Kernnormen / Kernquellen

- **URDG 758 Art. 5**: Unabhängigkeit der Garantie — kein Rückgriff auf Grundgeschäft
- **URDG 758 Art. 14**: Anforderungsabruf — Erklärung über Vertragsverletzung erforderlich
- **URDG 758 Art. 15**: Nicht-konforme Präsentation — Ablehnung und Benachrichtigung
- **URDG 758 Art. 19**: Force Majeure bei Garantiebank
- **URDG 758 Art. 20**: Verlängerungsanforderung (Extend-or-Pay)
- **URDG 758 Art. 34**: Missbrauch und Fraud — keine explizite Regelung, national ergänzen

## Schlüsselbegriffe

- Bietungsgarantie (Bid Bond): sichert Seriosität des Angebots (2-5% Angebotssumme)
- Erfüllungsgarantie (Performance Bond): sichert Vertragserfüllung (5-10%)
- Anzahlungsgarantie (Advance Payment Bond): sichert Rückzahlung von Vorauszahlungen
- Gegengarantie (Counter-Guarantee): Instruktionsbank garantiert gegenüber Garantiebank
- Extend-or-Pay: Begünstigter verlangt Verlängerung statt Sofortabruf

## Typische Streitfragen / Anwendungsfälle

1. Performance Bond Abruf ohne Vertragserfüllung: Ist Missbrauchseinwand (fraud) anerkannt?
2. Gegengarantie: Ist Instruktionsbank automatisch gebunden wenn Erstgarantiebank zahlt?
3. Extend-or-Pay: Muss Begünstigter Verlängerung gewähren oder kann er direkt abrufen?
4. URDG 758 vs. ISP98: Welches Regelwerk bei internationaler Bietungsgarantie im Nahen Osten?
5. Sprache der Abrufserklärung: URDG 758 Art. 14 — welche Sprache gilt?

## Methodik

- Garantietyp nach Zweck: Bid Bond, Performance Bond, APB nach Risikoprofil
- URDG 758 einbeziehen: "subject to URDG 758" in Garantietext
- Abrufbedingungen: so einfach wie möglich (Erklärung + ggf. Dokument)
- Fraud-Ausnahme: nationales Recht prüfen (England, Deutschland: Injunction möglich)

## Output

- URDG 758 Garantietypen-Übersicht (Bid/Performance/APB)
- Abrufbedingungen-Checkliste nach URDG 758 Art. 14-15
- Gegengarantie-Schema

## Quellenregel

URDG 758: iccwbo.org. ISP98: iccwbo.org. Schrifttum: Kelly-Louw, International Trade Finance (2012) Kap. 8. ICC Opinions URDG: iccwbo.org. Unsicherheit bleibt sichtbar.
