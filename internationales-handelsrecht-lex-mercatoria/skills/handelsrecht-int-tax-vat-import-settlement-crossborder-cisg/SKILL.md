---
name: handelsrecht-int-tax-vat-import-settlement-crossborder-cisg
description: "INT TAX VAT Import Settlement Crossborder CISG: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INT TAX VAT Import Settlement Crossborder CISG

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **INT TAX VAT Import Settlement Crossborder CISG** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-054-tax-vat-import-export` | Internationales Handelsrecht: Steuerrecht im internationalen Handel. Umsatzsteuer bei grenzüberschreitenden Lieferungen (§ 4 Nr. 1a UStG, 0%-Satz), Einfuhrumsatzsteuer, Verrechnungspreise (OECD-Leitsätze), Betriebsstättenrisiko und withholding tax. |
| `ihl-087-settlement-crossborder` | Internationales Handelsrecht: Grenzüberschreitende Vergleiche. Vergleichsvertrag (§ 779 BGB), Singapur-Konvention-Vollstreckung, Consent Award im Schiedsverfahren, Release-Klauseln, Steuerfolgen und Vollstreckungssicherung. |
| `ihl-002-cisg-anwendungsbereich` | Internationales Handelsrecht: CISG Anwendungsbereich nach Art. 1-13 CISG. Räumlicher Anwendungsbereich (Vertragsstaatenprinzip), sachlicher Ausschluss nach Art. 2 CISG (Verbraucher, Wertpapiere, Strom), und Lückenfüllung nach Art. 7 Abs. 2 CISG. |
| `ihl-003-cisg-ausschluss-und-rechtswahl` | Internationales Handelsrecht: CISG Ausschluss nach Art. 6 CISG und Rechtswahl nach Rom I (EG) 593/2008. Formulierung wirksamer Ausschlussklauseln, Teilausschluss einzelner Artikel und Zusammenspiel mit nationaler Kaufrechtsergänzung. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **INT TAX VAT Import Settlement Crossborder CISG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-054-tax-vat-import-export`

**Fokus:** Internationales Handelsrecht: Steuerrecht im internationalen Handel. Umsatzsteuer bei grenzüberschreitenden Lieferungen (§ 4 Nr. 1a UStG, 0%-Satz), Einfuhrumsatzsteuer, Verrechnungspreise (OECD-Leitsätze), Betriebsstättenrisiko und withholding tax.

# Steuerrecht im internationalen Handel

## Worum es geht

Grenzüberschreitende Warenlieferungen haben Umsatzsteuer- und Zollkonsequenzen. EU-Ausfuhrlieferungen sind steuerfrei (§ 4 Nr. 1a UStG, § 6 UStG), wenn Nachweise vorliegen. Bei Dienstleistungen kommt das Reverse-Charge-Verfahren zur Anwendung. Konzerninterne Lieferungen unterliegen OECD-Verrechnungspreisrichtlinien.

## Kernnormen / Kernquellen

- **§ 4 Nr. 1a UStG**: Steuerfreiheit von Ausfuhrlieferungen
- **§ 6 UStG**: Ausfuhrlieferung — Gelangensvermutung und Nachweisführung
- **§ 13b UStG**: Übergang der Steuerschuldnerschaft (Reverse Charge) bei Dienstleistungen
- **MwStSystRL Art. 138**: EU-innergemeinschaftliche Lieferung — Steuerfreiheit
- **OECD-Verrechnungspreisleitlinien 2022**: Arm's-Length-Prinzip
- **§§ 1, 1a AStG**: Außensteuergesetz — Einkünftekorrektur bei verbundenen Unternehmen

## Schlüsselbegriffe

- Ausfuhrnachweis: Ausfuhranmeldung (zertifizierter Ausgangsvermerk ATLAS) + Versendungsbeleg
- Gelangensvermutung: ab 2020 vereinfachter Nachweis für innergemeinschaftliche Lieferungen
- Einfuhrumsatzsteuer (EUSt): Entsteht bei Einfuhr; abziehbar als Vorsteuer
- Verrechnungspreis: fremdvergleichskonformer Preis im Konzernverbund
- Betriebsstättenrisiko: Dauerpräsenz im Ausland → Betriebsstätte → Körperschaftsteuer

## Typische Streitfragen / Anwendungsfälle

1. Ausfuhrnachweis fehlt: Verliert Exporteur Steuerfreiheit rückwirkend?
2. DDP-Lieferant ohne USt.-Registrierung im Importland: Wer schuldet EUSt.?
3. Verrechnungspreise: "Cost-Plus" vs. "Comparable Uncontrolled Price" — wann welche Methode?
4. Digitale Dienstleistungen: OSS (One-Stop-Shop) für Mehrwertsteuer in EU?
5. Betriebsstättenrisiko: Handelsvertreter im Ausland als Betriebsstätte des Auftraggebers?

## Methodik

- Ausfuhrnachweis: ATLAS-Ausgangsvermerk obligatorisch; alternativ Versendungsbelege
- EUSt.: Importeur-Registrierung vor Einfuhr prüfen; DDP-Verträge USt.-Klausel einbeziehen
- Verrechnungspreise: Dokumentation nach § 90 Abs. 3 AO (Sachverhaltsaufzeichnung)
- Betriebsstättenprüfung: "Dependent Agent"-Test nach OECD Musterabkommen Art. 5

## Output

- Ausfuhrnachweis-Checkliste (§ 6 UStG)
- Verrechnungspreismethoden-Übersicht (OECD 2022)
- Betriebsstättenrisiko-Matrix für Handelsvertreter

## Quellenregel

UStG §§ 4, 6, 13b: gesetze-im-internet.de. MwStSystRL Art. 138: eur-lex.europa.eu. OECD-Verrechnungspreisleitlinien: oecd.org. AStG §§ 1, 1a: gesetze-im-internet.de. Unsicherheit bleibt sichtbar.

## 2. `ihl-087-settlement-crossborder`

**Fokus:** Internationales Handelsrecht: Grenzüberschreitende Vergleiche. Vergleichsvertrag (§ 779 BGB), Singapur-Konvention-Vollstreckung, Consent Award im Schiedsverfahren, Release-Klauseln, Steuerfolgen und Vollstreckungssicherung.

# Grenzüberschreitende Vergleiche

## Worum es geht

Vergleiche in internationalen Streitigkeiten können als privatrechtlicher Vertrag (§ 779 BGB), als Consent Award im Schiedsverfahren oder als Mediationsvergleich (Singapur-Konvention-vollstreckbar) strukturiert werden. Die Vollstreckungssicherung ist entscheidend: Consent Award nach NY Convention vollstreckbar; Mediationsvergleich nach Singapur-Konvention.

## Kernnormen / Kernquellen

- **§ 779 BGB**: Vergleichsvertrag — gegenseitiges Nachgeben; Irrtum über Grundlage
- **§ 794 Abs. 1 Nr. 1 ZPO**: Gerichtlicher Vergleich als Vollstreckungstitel
- **NY Convention Art. I**: Consent Award als Schiedsspruch vollstreckbar
- **Singapur-Konvention Art. 1**: Mediationsvergleich vollstreckbar in Vertragsstaaten
- **CISG Art. 29**: Vertragsänderung durch Vergleich wirksam (formfrei wenn kein Art. 12-Vorbehalt)
- **§ 57 InsO**: Vergleich im Insolvenzverfahren

## Schlüsselbegriffe

- Consent Award: Schiedsspruch der den Vergleich beurkundet — NY-Convention-vollstreckbar
- Full and Final Release: Alle Ansprüche aus dem Rechtsstreit erledigt; Abgrenzung zu Teilvergleich
- Stundungs- vs. Erlassvergleich: Ratenzahlung mit Vollstreckungs-Einstellung vs. vollständiger Erlass
- Steuerfolgen: Vergleichsleistung in bestimmten Ländern steuerpflichtig (Quellensteuern)
- Vollstreckungsverzicht (Waiver): Gläubiger verzichtet auf Vollstreckung bei bestimmter Erfüllung

## Typische Streitfragen / Anwendungsfälle

1. Consent Award: Kann Schiedsgericht Vergleich als Award beurkunden ohne eigene Prüfung?
2. Full Release: Schließt eine allgemeine Release-Klausel auch Ansprüche aus, die Partei nicht kannte?
3. Steuerfolgen D: Ist Vergleichszahlung aus Deutschland an ausländischen Gläubiger quellensteuerpflichtig?
4. § 779 BGB Irrtum: Vergleich über Sachverhalt der sich später als anders herausstellt — anfechtbar?
5. Singapur-Konvention und EU: Gilt die Konvention auch in EU-Mitgliedstaaten?

## Methodik

- Vollstreckungssicherung: Consent Award bevorzugen wenn Schiedsverfahren läuft
- Full Release: präzise formulieren (alle Ansprüche aus Sachverhalt X; kein catch-all)
- Steuerberater einbeziehen: Quellensteuerrisiko bei grenzüberschreitender Vergleichszahlung
- Ratenzahlung: Vollstreckungsverzicht nur für pünktliche Raten; bei Verzug sofortige Vollstreckung

## Output

- Consent-Award-Request-Muster
- Full-and-Final-Release-Klausel-Muster
- Ratenzahlungsvergleich-Struktur

## Quellenregel

BGB § 779: gesetze-im-internet.de. NY Convention: newyorkconvention.org. Singapur-Konvention: uncitral.un.org. ZPO § 794: gesetze-im-internet.de. Unsicherheit bleibt sichtbar.

## 3. `ihl-002-cisg-anwendungsbereich`

**Fokus:** Internationales Handelsrecht: CISG Anwendungsbereich nach Art. 1-13 CISG. Räumlicher Anwendungsbereich (Vertragsstaatenprinzip), sachlicher Ausschluss nach Art. 2 CISG (Verbraucher, Wertpapiere, Strom), und Lückenfüllung nach Art. 7 Abs. 2 CISG.

# CISG Anwendungsbereich (Art. 1-13)

## Worum es geht

Das UN-Kaufrecht (CISG, Wien 1980, in Kraft seit 1988) gilt in 97 Vertragsstaaten. Es erfasst Kaufverträge über Waren zwischen Parteien mit Niederlassungen in verschiedenen Vertragsstaaten (Art. 1 Abs. 1 lit. a) oder wenn IPR auf das Recht eines Vertragsstaates verweist (lit. b, aber viele Staaten mit Vorbehalt). Art. 2 enthält abschließende Ausschlüsse.

## Kernnormen / Kernquellen

- **Art. 1 CISG**: Anwendungsvoraussetzungen — Niederlassung in Vertragsstaat
- **Art. 2 CISG**: Ausschlüsse — Verbraucherkauf, Versteigerungen, Wertpapiere, Schiffe, Elektrizität, Luftfahrzeuge
- **Art. 3 CISG**: Werklieferungsvertrag (Grenze: wesentlicher Anteil Material)
- **Art. 6 CISG**: Vertragsfreiheit — vollständiger Ausschluss oder Abweichung
- **Art. 7 CISG**: Auslegung nach Treu und Glauben im int. Handel; Lückenfüllung aus allgemeinen CISG-Grundsätzen
- **Art. 9 CISG**: Handelsbräuche und Gepflogenheiten der Parteien
- **Art. 10 CISG**: Maßgebliche Niederlassung bei mehreren

## Schlüsselbegriffe

- Vertragsstaat (Ratifikation, Beitritt, Vorbehalt nach Art. 92-96 CISG)
- Sachlicher Ausschluss vs. Opting-out (Art. 2 vs. Art. 6)
- Mixed-contract (Art. 3 Abs. 2: überwiegende Arbeitsleistung → kein CISG)
- Autonome Auslegung (Art. 7 Abs. 1: keine nationale Rechtsdogmatik)
- Lückenfüllung: interne Lücken aus CISG-Grundsätzen, externe Lücken aus IPR

## Typische Streitfragen / Forschungsfragen

1. Gilt CISG für Softwarelieferung? (Streitig: körperliche Verkörperung entscheidend)
2. Konsumgüterkauf über B2B-Plattform: Art. 2 lit. a Ausschluss auch bei gewerblichem Verwendungszweck?
3. Werklieferungsvertrag: Wann überwiegt Arbeitsleistung (Art. 3 Abs. 2)?
4. Wie füllt man CISG-intern die Lücke bei Zinshöhe (Art. 78 schweigt zur Rate)?
5. Reservation nach Art. 95 (USA): kein lit. b-Verweis — Auswirkung auf US-Verträge?

## Methodik

- CISG-Anwendbarkeit immer dreistufig prüfen: (1) sachlich, (2) räumlich, (3) kein Ausschluss
- Vertragsstaaten-Liste UNCITRAL laufend prüfen (uncitral.un.org/en/texts/saleofgoods)
- Bei Art. 3 Werklieferung: Wertanteil Material vs. Dienstleistung nach Vertragsursprung
- Autonome Auslegung: keine Rückgriffe auf BGB-Dogmatik bei CISG-Begriffen

## Output

- Subsumtionsschema CISG-Anwendbarkeit (ja/nein/condizional)
- Checkliste Art. 2-Ausschlüsse
- Formulierungsvorschlag Opting-out-Klausel nach Art. 6

## Quellenregel

CISG-Text: uncitral.un.org. Rechtsprechungsdatenbank: CISG-online.ch, jusmundi.com. Schrifttum: Schlechtriem/Schwenzer (7. Aufl. 2019) mit Stelle angeben. Unsicherheit bleibt sichtbar.

## 4. `ihl-003-cisg-ausschluss-und-rechtswahl`

**Fokus:** Internationales Handelsrecht: CISG Ausschluss nach Art. 6 CISG und Rechtswahl nach Rom I (EG) 593/2008. Formulierung wirksamer Ausschlussklauseln, Teilausschluss einzelner Artikel und Zusammenspiel mit nationaler Kaufrechtsergänzung.

# CISG-Ausschluss und Rechtswahl

## Worum es geht

Art. 6 CISG erlaubt Parteien, das gesamte CISG oder einzelne Bestimmungen auszuschließen oder abzuweichen. Ein wirksamer Ausschluss erfordert klare Formulierung; der bloße Verweis auf nationales Recht genügt nicht immer (BGH-Rspr. kontrovers). Die Rechtswahl nach Rom I bestimmt das ergänzende nationale Recht.

## Kernnormen / Kernquellen

- **CISG Art. 6**: Ausschluss- und Abweichungsfreiheit
- **CISG Art. 12**: Schriftformerfordernis bei Vorbehalt nach Art. 96 (z.B. Argentinien, Russland)
- **Rom I VO Art. 3**: Ausdrückliche oder konkludente Rechtswahl
- **Rom I VO Art. 4**: Subsidiäre Anknüpfung (Verkäuferstatut)
- **Rom I VO Art. 10 Abs. 1**: Formwirksamkeit nach Vertragsstatut
- **BGH VIII ZR 304/00 v. 25.11.2002**: Deutsches Recht ohne expliziten CISG-Ausschluss lässt CISG bestehen

## Schlüsselbegriffe

- Opting-out (Art. 6 CISG) vs. Opting-in (z.B. UNIDROIT Principles statt CISG)
- Teilausschluss (z.B. Art. 39 Abs. 1 Rügefrist verlängern)
- Abweichung nach oben/unten (Schadensersatzcap)
- Ergänzendes nationales Recht (Lücken nach CISG-Ausschluss)
- Schriftformvorbehalt Art. 96 CISG

## Typische Streitfragen / Anwendungsfälle

1. Reicht "This contract is governed by German law" als CISG-Ausschluss? (Nein — BGH)
2. Kann Art. 79 CISG (Force Majeure) einzeln ausgeschlossen und durch eigene FM-Klausel ersetzt werden?
3. Welches nationale Recht füllt Lücken nach Art. 6-Ausschluss (Rom I Art. 4)?
4. Gilt Schriftformvorbehalt Art. 96/12 CISG auch für elektronische Nachrichten?
5. Können Parteien UNIDROIT Principles als Vertragsstatut wählen (statt CISG)?

## Methodik

- Ausschlussklausel explizit formulieren: "The CISG shall not apply."
- Bei Teilabweichung: die konkreten Artikel benennen
- Rom I-Statut separat festlegen — CISG und Vertragsstatut sind unabhängig
- Schriftformvorbehalt-Staaten vor Vertragsabschluss prüfen

## Output

- Musterkausel: CISG-Ausschluss (vollständig und partiell)
- Checkliste: Wahl CISG vs. nationales Recht vs. UNIDROIT
- Risikoanalyse: Lückenrecht nach Ausschluss

## Quellenregel

CISG: uncitral.un.org. Rom I: eur-lex.europa.eu (32008R0593). BGH-Rspr.: dejure.org, juris.de. CISG-online.ch für Rechtsprechungsübersichten. Unsicherheit bleibt sichtbar.
