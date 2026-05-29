---
name: aussenwirtschaft-sanktionen-embargos
description: "Prüfung von Laenderembargos personenbezogenen Sanktionen und Umgehungsrisiken im Aussenhandel. Anwendungsfall Handelspartner koennte Sanktionslistentreffer haben oder Lieferung in Sanktionsland geht. Normen EU-Sanktionsverordnungen Art. 215 AEUV OFAC SDN-Liste AWG § 4 Genehmigungspflicht. Prüfraster Laenderembargos Personenscreening Eigentuems-Kontrolle Umgehungsrisiken Finanzmittel Dienstleistungen IP-Rechte Zahlungsstroeme. Output Sanktions-Prüfprotokoll mit Screening-Ergebnis Risikobewertung und Handlungsempfehlung Transaktion durchführen oder stoppen. Abgrenzung zu geldwäsche-sanktionsscreening und aussenwirtschaft-exportkontrolle-dual-use."
---

# Sanktionen, Embargos und Bereitstellungsverbote

## Zweck

Dieser Skill führt Sanktionsprüfung mit Trefferlog, Quellenprotokoll, False-Positive-Bewertung und Eskalationspfad.

## Wann verwenden

- wenn Waren, Software, Technologie, Dienstleistungen, Zahlungen oder Beteiligte einen Auslandsbezug haben
- wenn Exportkontrolle, Sanktionen, Embargos, Zoll, Verbrauchsteuer, CBAM, AWV oder AML/KYC berührt sind
- wenn eine Behörde prüft, ein Verstoß offengelegt werden könnte oder Presse-/Reputationsdruck entsteht

## Arbeitsweise

1. **Sachverhalt einfrieren.** Erfasse Transaktionskette, Beteiligte, Länder, Ware, Software, Technologie, Dienstleistung, Zahlungsweg, Transportweg, Bank, Endverwendung und Fristen.
2. **Datenlücken markieren.** Trenne belegte Tatsachen von Annahmen. Verlange Produktdatenblätter, technische Spezifikationen, Vertragsunterlagen, Rechnungen, Zollanmeldungen, Zahlungsdaten, Sanktionsscreening und Kommunikationsverlauf.
3. **Offizielle Quellen prüfen.** Nutze BAFA, EU Sanctions Map, konsolidierte EU-Finanzsanktionsliste, EUR-Lex, TARIC, Zoll, Bundesbank, EU-CBAM-Seiten und bei Bedarf US-Quellen. Protokolliere URL, Abrufdatum und Aussage.
4. **Verbote vor Genehmigungen.** Prüfe zuerst harte Verbote, Bereitstellungsverbote, Umgehungsrisiken, Listentreffer und Embargos. Danach Genehmigungs-, Melde-, Dokumentations-, Zoll- und Abgabenpflichten.
5. **Sofortmaßnahmen ausgeben.** Bei Risiko rot: Stop-Ship/Stop-Pay, Legal Hold, Dokumentensicherung, Eskalation an Geschäftsleitung/Compliance, Behörden- und Verteidigungsstrategie.
6. **Arbeitsprodukt erstellen.** Erzeuge Matrix, Antrag, Behördenbrief, Offenlegungsplan, KYC-Vermerk, Zollvermerk, CBAM-Register, Prüfungsreaktion, Mandantenmail oder Krisen-Q&A.
7. **Qualitätstor.** Prüfe Quellenstand, Zahlen, Fristen, Zuständigkeit, Anlagen, Datenschutz, Mandatsgeheimnis und Freigaben. Unsichere Punkte bleiben sichtbar.

## Rückfragen, wenn unklar

- Welche Ware, Software, Technologie, Dienstleistung oder Zahlung ist betroffen?
- Welche Länder, Personen, Unternehmen, Banken, Häfen, Spediteure und Endverwender sind beteiligt?
- Welche HS-/KN-/TARIC-Nummer, Güterlistenposition oder technische Spezifikation liegt vor?
- Gibt es Sanktions-, Embargo-, US-, CBAM-, Verbrauchsteuer- oder AWV-Touchpoints?
- Liegt eine Frist, Prüfungsanordnung, Anhörung, Durchsuchung, Presseanfrage oder Lieferstopp vor?

## Ausgabeformat

- Kurzlage mit Ampel und Sofortmaßnahmen
- Quellenprotokoll mit Abrufdatum und offizieller Quelle
- Prüfmatrix mit offenen Datenpunkten, Annahmen und Zuständigkeiten
- behörden- oder mandantenfähiger Entwurf
- Review-Liste für Berufsträger, Compliance, Zoll, Steuer und Geschäftsleitung

## Typische Fehler vermeiden

- Keine Sanktionsentscheidung ohne aktuelle Quellenprüfung und Trefferlog.
- Keine Güterklassifizierung ohne technische Parameter, Verwendungszweck und Quellenangabe.
- Keine Zolltarifnummer ohne TARIC-/EZT-Prüfung und Begründung.
- Keine CBAM-Berechnung ohne Warencode, Warenmenge, Emissionsdatenquelle und markierte Annahmen.
- Keine Offenlegung oder Selbstanzeige ohne Verteidigungsstrategie und Freigabe durch Berufsträger.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.

## Triage vor Sanktionspruefung

Kläre vor der Pruefung:

1. Welche Sanktionsregimes sind betroffen — EU, OFAC, UN, oder Vereinigtes Koenigreich (OFSI)?
2. Sind Personen, Entitaeten, Sektoren oder Gebiete als Sanktionsanknuepfungspunkt relevant?
3. Handelt es sich um Bereitstellung von Finanzmitteln, Wirtschaftsressourcen, Dienstleistungen oder Transport?
4. Liegt ein OFAC-SDN-Treffer, ein EU-konsolidierter-Listen-Treffer oder ein False Positive vor?
5. Besteht Zeitdruck durch laufende Transaktion, Zahlung oder Lieferung?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette Sanktionen/Embargos

- Art. 2, 3, 7 VO (EU) 833/2014 — Russland-Sektor- und Gutersanktionen
- Art. 2 VO (EU) 269/2014 — Russland-Personensanktionen (Krim/Ukraine)
- Art. 29 EUV, Art. 215 AEUV — Rechtsgrundlage EU-Sanktionen
- § 18 I, II AWG — Straftatbestand Embargoverstoss, bis 15 Jahre Freiheitsstrafe
- § 82 AWV — Embargobezogene Verbote im nationalen Recht
- OFAC 31 CFR Part 560 (Iran), Part 589 (Russland) — US-Sanktionsregimes

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Sanktionspruefungsvermerk

**Adressat:** Compliance/Vorstand — **Tonfall:** prazise, aktionsbasiert

```
SANKTIONSPRUEFUNGSVERMERK
Datum: [DATUM]  Abrufdatum Listen: [DATUM]
Mandat/Transaktion: [BEZEICHNUNG]
Bearbeiter: [NAME]

1. GEPRUEFT GEGEN
   [ ] EU-Konsolidierte Finanzsanktionsliste (EUR-Lex)
   [ ] OFAC SDN List (US Treasury)
   [ ] UK HM Treasury (OFSI) Sanctions List
   [ ] UN Security Council Consolidated List

2. TREFFERPROTOKOLL
   Suchbegriff | Liste | Treffer (J/N) | Typ (Exact/Fuzzy) | Bewertung
   ------------|-------|--------------|-------------------|----------
   [NAME/ENTITY]| EU   | [J/N]        | [TYP]             | [Echttreffer/FP]

3. BEREITSTELLUNGSVERBOT-ANALYSE
   Gegenstand: [Ware / Zahlung / Dienstleistung]
   Begueinstigter (direkt): [...]
   Begueinstigter (mittelbar): [...]
   Ergebnis: KEIN VERBOT / VERBOT / GENEHMIGUNGSPFLICHTIG

4. EMPFEHLUNG
   [ ] Transaktion freigegeben
   [ ] Stop-Pay/-Ship — Freigabe erst nach [Bedingung]
   [ ] Genehmigung BAFA/Bundesbank erforderlich
   [ ] OFAC-Licence erforderlich (bei US-Nexus)

5. QUELLENPROTOKOLL
   - [Liste/Quelle] abgerufen am [DATUM] unter [URL]
```
