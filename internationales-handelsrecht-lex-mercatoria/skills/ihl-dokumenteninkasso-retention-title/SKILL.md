---
name: ihl-dokumenteninkasso-retention-title
description: "IHL Dokumenteninkasso Retention Title: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IHL Dokumenteninkasso Retention Title

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **IHL Dokumenteninkasso Retention Title** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-040-dokumenteninkasso` | Internationales Handelsrecht: Dokumenteninkasso nach URC 522 (ICC 1995). Dokumente-gegen-Zahlung (D/P) und Dokumente-gegen-Akzept (D/A), Inkassoauftrag, Pflichten der Inkassobank und Risiken bei Nichteinlösung. |
| `ihl-041-retention-of-title-international` | Internationales Handelsrecht: Eigentumsvorbehalt (EV) im internationalen Handel. Einfacher, erweiterter und verlängerter Eigentumsvorbehalt, Wirksamkeit nach ausländischem Sachenrecht, Kollisionsrecht (lex situs), Registrierungspflichten und UCC Art. 9 (USA). |
| `ihl-042-eigentuemsuebergang-und-sicherheiten` | Internationales Handelsrecht: Eigentumsübergang bei Warenkauf international. CISG-Lücke (Art. 4b), lex situs, Traditio vs. Konsensualprinzip, Kreditsicherheiten in der Lieferkette und Floating Charge (englisches Recht). |
| `ihl-043-qualitaetskontrolle-pre-shipment` | Internationales Handelsrecht: Qualitätskontrolle vor Versand (Pre-Shipment Inspection, PSI). CISG Art. 35 Vertragsmäßigkeit als Grundlage, PSI-Klauseln, SGS/Bureau Veritas-Praxis, WTO-PSI-Abkommen und Haftung des Inspektors bei fehlerhafter Bescheinigung. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **IHL Dokumenteninkasso Retention Title**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-040-dokumenteninkasso`

**Fokus:** Internationales Handelsrecht: Dokumenteninkasso nach URC 522 (ICC 1995). Dokumente-gegen-Zahlung (D/P) und Dokumente-gegen-Akzept (D/A), Inkassoauftrag, Pflichten der Inkassobank und Risiken bei Nichteinlösung.

# Dokumenteninkasso nach URC 522

## Worum es geht

Das Dokumenteninkasso (Documentary Collection) ist eine kostengünstigere Alternative zum Akkreditiv: Die Bank leitet Handels- und Transportdokumente an die Käufer-Bank weiter und gibt sie nur gegen Zahlung (D/P) oder Wechselakzept (D/A) heraus. URC 522 (ICC Uniform Rules for Collections 1995) gilt durch Einbeziehung. Die Bank gibt keine Zahlungsgarantie.

## Kernnormen / Kernquellen

- **URC 522 Art. 1**: Anwendungsbereich — Einbeziehung durch Inkassoauftrag
- **URC 522 Art. 4**: Inkassoauftrag — vollständige Anweisungen (kein Ermessen der Bank)
- **URC 522 Art. 7**: Dokumente gegen Zahlung (D/P) vs. Dokumente gegen Akzept (D/A)
- **URC 522 Art. 19**: Vorgehensweise bei Nichteinlösung — keine eigenständige Bankpflicht
- **URC 522 Art. 21**: Auslagen und Provisionen der Inkassobank
- **Wechselgesetz (WG)**: D/A-Wechsel als eigenständiges Wertpapier

## Schlüsselbegriffe

- D/P (CAD Cash Against Documents): Herausgabe Dokumente nur gegen sofortige Zahlung
- D/A (Akzept-Inkasso): Dokumente gegen Wechselakzept — Kredit bis Fälligkeitsdatum
- Einzugsauftrag: enthält alle Anweisungen für einkassierenden Bank
- Protestverfahren: Bank protestiert Wechsel bei Nichtakzept/Nichtzahlung
- Länderrisiko: Inkassobank zahlt nicht selbst — Käuferland-Risiko verbleibt beim Verkäufer

## Typische Streitfragen / Anwendungsfälle

1. D/P Inkasso: Käufer nimmt Dokumente und zahlt nicht — welche Rechtsbehelfe?
2. D/A: Käufer akzeptiert Wechsel, zahlt nicht bei Fälligkeit — Wechselklage?
3. Konnossement bei D/P: Sichert das Konnossement den Verkäufer ausreichend?
4. Inkassobank-Haftung: Haftet Bank für fehlerhafte Dokumentenherausgabe ohne Zahlung?
5. URC 522 vs. UCP 600: Kann dieselbe Transaktion beide Regelwerke auslösen?

## Methodik

- D/P für höheres Risiko; D/A nur bei bekannten Kunden mit guter Bonität
- Konnossement als Order-BL: sichert Dokumentenkontrolle bei D/P
- Inkassoauftrag: URC 522-Einbeziehungsklausel und vollständige Anweisungen
- Wechselakzept: Wechselrecht des Käuferlands vor D/A-Einsatz prüfen

## Output

- D/P vs. D/A Risikoanalyse
- Inkassoauftrag-Checkliste (URC 522 Art. 4)
- Wechsel-Muster (internationalem Wechselgesetz)

## Quellenregel

URC 522: iccwbo.org. WG (Wechselgesetz): gesetze-im-internet.de. Schrifttum: Malek/Quest, Documentary Credits (4. Aufl. 2009). Unsicherheit bleibt sichtbar.

## 2. `ihl-041-retention-of-title-international`

**Fokus:** Internationales Handelsrecht: Eigentumsvorbehalt (EV) im internationalen Handel. Einfacher, erweiterter und verlängerter Eigentumsvorbehalt, Wirksamkeit nach ausländischem Sachenrecht, Kollisionsrecht (lex situs), Registrierungspflichten und UCC Art. 9 (USA).

# Eigentumsvorbehalt International

## Worum es geht

Der Eigentumsvorbehalt (EV) ist das wichtigste Kreditsicherungsmittel des deutschen Lieferanten. International stößt er auf Grenzen: Das Sachenrecht richtet sich nach der lex situs (Lageort der Ware). Viele Länder kennen keinen EV oder verlangen Registrierung (USA: UCC Art. 9, UK: PPSA). In der EU regelt Rom I Art. 26 (jetzt VO (EU) 2024/...) die Kollision.

## Kernnormen / Kernquellen

- **BGB § 449**: Einfacher Eigentumsvorbehalt
- **BGB § 449 Abs. 2**: Verlängerter EV (Abtretung künftiger Forderungen) — Sittenwidrigkeit bei Übersicherung
- **CISG Art. 4 lit. b**: CISG regelt Eigentumsübergang nicht — nationales Recht gilt
- **Rom I VO Art. 26**: Sachenrecht — lex situs als Grundsatz
- **UCC Art. 9 (USA)**: Secured Transactions — Filing erforderlich (UCC-1 Financing Statement)
- **PPSA (UK)**: Personal Property Security Act-Regime nach Brexit

## Schlüsselbegriffe

- Einfacher EV: Eigentum bleibt bis zur vollständigen Kaufpreiszahlung
- Verlängerter EV: Verarbeitungsklausel (Verarbeiter → Miteigentum); Weiterverkaufsklausel (Forderungsabtretung)
- Lex situs: Sachenrechtliches Statut folgt Lageort der Ware im Zeitpunkt der Übereignung
- Registrierungspflicht (USA, UK): ohne Eintragung kein Schutz gegenüber Insolvenzverwalter
- Insolvenztestfall: EV wirkt gegen Insolvenzverwalter des Käufers wenn wirksam begründet

## Typische Streitfragen / Anwendungsfälle

1. EV Deutschland → USA: Gilt deutsches EV-Recht oder muss UCC-1-Filing erfolgen?
2. Verarbeitungsklausel: Käufer verarbeitet Ware zu neuem Produkt — verliert Verkäufer Eigentum?
3. Konzernklausel-EV: Zahlung an Muttergesellschaft befreit nicht von EV gegenüber Tochter?
4. EV bei Weiterverkauf (verlängerter EV): Abtretung der Forderung an Lieferant vs. Bank?
5. EV-Register UK: Wie funktioniert Companies House Personal Property Register nach Brexit?

## Methodik

- Lex situs Analyse: Zielland des EV und dortige Anforderungen vor Vertragsabschluss prüfen
- USA-Export: UCC-1 Financing Statement im US-Staat des Käufers einreichen
- Verlängerter EV: Übersicherungs-Verbot (§ 138 BGB) bei Kombination mit Bank-Abtretungen prüfen
- Insolvenzschutz: EV immer in Vertrag und AGB klar formulieren (AGR § 449 BGB)

## Output

- EV-Wirksamkeit-Checkliste für Top-Exportländer (USA, UK, Frankreich, China)
- UCC-1 Filing-Schritt-für-Schritt-Anleitung
- Verlängerter-EV-Klausel-Muster

## Quellenregel

BGB §§ 449, 138: gesetze-im-internet.de. UCC Art. 9: uniform.law.cornell.edu (US). CISG Art. 4: uncitral.un.org. Schrifttum: Staudinger/Beckmann, BGB § 449 (2020). Unsicherheit bleibt sichtbar.

## 3. `ihl-042-eigentuemsuebergang-und-sicherheiten`

**Fokus:** Internationales Handelsrecht: Eigentumsübergang bei Warenkauf international. CISG-Lücke (Art. 4b), lex situs, Traditio vs. Konsensualprinzip, Kreditsicherheiten in der Lieferkette und Floating Charge (englisches Recht).

# Eigentumsübergang und Kreditsicherheiten

## Worum es geht

Das CISG regelt Eigentumsübergang ausdrücklich nicht (Art. 4 lit. b). Nationales Sachenrecht nach lex situs entscheidet. Im deutschen Recht gilt Einigung + Übergabe (§§ 929 ff. BGB); in Common-Law-Systemen oft Konsensualprinzip (Eigentum geht mit Vertragsschluss über, SGA 1979 UK). Kreditsicherheiten (Sicherungsübereignung, Sicherungszession, Floating Charge) haben unterschiedliche internationale Anerkennungsgrade.

## Kernnormen / Kernquellen

- **BGB §§ 929-931**: Übereignung — Einigung + Übergabe (Traditionsprinzip)
- **Sale of Goods Act 1979 (UK) s. 17-18**: Eigentumsübergang bei best. Ware — Parteiwille
- **CISG Art. 4 lit. b**: Eigentumsübergang ausdrücklich ausgeschlossen
- **Rom I VO Art. 26**: Sachenrecht folgt lex situs
- **Sicherungstreuhand / Floating Charge**: englische Floating Charge — keine genaue Entsprechung im deutschen Recht
- **UCC Art. 9**: US-Secured Transactions (Security Interest)

## Schlüsselbegriffe

- Traditionsprinzip (D): Übereignung durch Einigung + körperliche Übergabe
- Konsensualprinzip (UK, Frankreich): Eigentum geht mit Vertrag über
- Floating Charge: bewegliches Sicherungsrecht über wechselnden Warenbestand (nur Common Law)
- Sicherungszession: Abtretung von Forderungen zur Sicherung (deutsches Recht)
- PPSA/UCC-Registrierung: Schutz gegen Insolvenz und Dritterwerber nur mit Filing

## Typische Streitfragen / Anwendungsfälle

1. Warenkauf D → UK: Übergang Eigentum mit Vertrag (UK) oder erst mit Übergabe (D)?
2. Floating Charge: Wie wird sie in deutschem Insolvenzverfahren anerkannt?
3. Sicherungszession in Frankreich: Dailly-Zession-Gesetz als besonderes Formerfordernis?
4. Insolvenz des Käufers: EV oder Sicherungsübereignung — was geht vor?
5. CISG: Können Parteien Eigentumsübergang in CISG-Kaufvertrag regeln?

## Methodik

- Lageortrecht (lex situs) vor Vertragsabschluss identifizieren
- UK Floating Charge: Eintragung im Companies House erforderlich (Companies Act 2006 s. 859A)
- Sicherungszession: Formvorschriften des Rechts des Drittschuldners prüfen
- CISG-Vertrag: Eigentumsklausel ausdrücklich in Vertrag aufnehmen

## Output

- Eigentumsübergangs-Matrix: D, UK, F, USA
- Kreditsicherheiten-Checkliste (national und international)
- Floating-Charge-Anerkennung im deutschen Insolvenzverfahren

## Quellenregel

BGB §§ 929 ff.: gesetze-im-internet.de. SGA 1979 (UK): legislation.gov.uk. CISG Art. 4: uncitral.un.org. UCC Art. 9: uniform.law.cornell.edu. Unsicherheit bleibt sichtbar.

## 4. `ihl-043-qualitaetskontrolle-pre-shipment`

**Fokus:** Internationales Handelsrecht: Qualitätskontrolle vor Versand (Pre-Shipment Inspection, PSI). CISG Art. 35 Vertragsmäßigkeit als Grundlage, PSI-Klauseln, SGS/Bureau Veritas-Praxis, WTO-PSI-Abkommen und Haftung des Inspektors bei fehlerhafter Bescheinigung.

# Qualitätskontrolle: Pre-Shipment Inspection

## Worum es geht

Pre-Shipment Inspection (PSI) ist die Warenprüfung vor Verschiffung durch unabhängige Inspektoren (SGS, Bureau Veritas, Intertek). Sie sichert Qualität, Menge und Preis. WTO-PSI-Abkommen (1994) regelt staatlich vorgeschriebene PSI. CISG Art. 35 definiert die Vertragsmäßigkeit als rechtliche Grundlage.

## Kernnormen / Kernquellen

- **CISG Art. 35**: Vertragsmäßigkeit — Basis für Qualitätsstandard
- **CISG Art. 38**: Untersuchungspflicht — interagiert mit PSI-Ergebnis
- **WTO PSI Agreement (1994)**: Anforderungen an staatlich mandatierte PSI (Preisvergleich, Zolltarif)
- **SGS/Bureau Veritas AGB**: Haftungsbeschränkungen bei fehlerhafter Inspektion
- **ISO 2859**: Statistische Stichproben-Verfahren für Qualitätskontrolle
- **Akkreditiv UCP 600 Art. 26**: Inspection Certificate als Akkreditivdokument

## Schlüsselbegriffe

- Clean Inspection Certificate: Bescheinigung der Vertragskonformität durch Inspektor
- Back-to-Back-Haftung: Verkäufer haftet für Mängel auch wenn PSI frei war (CISG Priorität)
- PSI-Klausel: Käufer nominiert Inspektor, Kosten wer trägt?
- AQL (Acceptable Quality Level): statistische Fehlerquotenakzeptanz
- Inspektionsfehler: Inspektor haftet nur wenn grob fahrlässig oder vorsätzlich (AGB-Haftungslimit)

## Typische Streitfragen / Anwendungsfälle

1. PSI "klar" aber Ware bei Ankunft mangelhaft: CISG-Mängelanspruch trotzdem möglich?
2. Inspektionskosten: Incoterms — wer zahlt PSI-Kosten bei CIF vs. FOB?
3. Akkreditiv mit PSI-Zertifikat: Was wenn Inspektor zertifiziert aber UCP-Dokument fehlerhaft?
4. Staatliche PSI (WTO-Abkommen): Preisvergleich durch Staat — WTO-konforme Grenzen?
5. Inspektor-Haftung: Schadenersatzklage gegen SGS bei grober Fehlinspektion?

## Methodik

- PSI-Klausel: Warenspezifikation, Inspektionsnorm (ISO 2859), Inspektionszeitpunkt definieren
- Haftungskettenanalyse: Verkäufer → Inspektor → Käufer; wer kann von wem fordern?
- Akkreditiv: PSI-Zertifikat-Format mit Bank vorab abstimmen (UCP 600 Art. 26)
- Kosten-Risikoanalyse: PSI-Kosten vs. Mangelrisiko nach Transaktionsgröße

## Output

- PSI-Klausel-Muster (Vertragsbaustein)
- PSI vs. CISG Haftungsmatrix
- Inspektionszertifikat-Checkliste für Akkreditivzwecke

## Quellenregel

CISG Art. 35/38: uncitral.un.org. WTO PSI Agreement: wto.org. UCP 600 Art. 26: iccwbo.org. ISO 2859: iso.org. Unsicherheit bleibt sichtbar.
