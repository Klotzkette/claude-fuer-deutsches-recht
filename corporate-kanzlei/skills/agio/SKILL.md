---
name: agio
description: "Strukturierung von Kapitalerhöhungen mit Agio bei VC-Finanzierungsrunden Holding-Aufbauten und M&A-Sekundärfinanzierungen. Übersetzung US-Term-Sheet-Begriffe (Original Purchase Price Par Value APIC Liquidation Preference) in deutsche Kategorien (Ausgabebetrag Nennbetrag Kapitalrücklage Vorzugsrec — Arbeitskontext: Corporate-Kanzlei (M&A, Gesellschaftsrecht), Schwerpunkt agio."
---

# Agio und Kapitalerhöhungsstruktur in der Corporate-Praxis

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage zu Beginn

Vor dem ersten Term-Sheet-Markup klären:

1. **Dealtyp:** Erste VC-Runde Folgerunde Bridge Convertible-Wandlung Anteilstausch nach § 21 UmwStG oder Sekundärtransaktion mit Kapitalmaßnahme?
2. **Beteiligungsstruktur des Lead Investors:** Deutsche GmbH KG US-LP Luxemburg-SCS oder andere Auslandsstruktur? Beeinflusst Beurkundungsbedarf und Steuerlogik.
3. **Stammkapital aktuell und post-money:** Wie viel zusätzliches Stammkapital wird ausgegeben wie viel Agio? Standardmuster bei VC-Runden 99 Prozent Agio.
4. **Agio-Charakter:** Echtes (korporatives) oder unechtes (schuldrechtliches) Agio? Beim qualifizierten Anteilstausch § 21 UmwStG ist echtes Agio Voraussetzung für Buchwertfortführung.
5. **Fälligkeit des Agios:** Bei Closing in voller Höhe (Fall 1) oder gestaffelt (Fall 2)? Bei Fall 2 muss das Agio in den aktualisierten Satzungstext sonst Eintragungshindernis.
6. **Liquidation Preference:** Bezugsgröße Ausgabebetrag (Nennbetrag plus Agio) oder fälschlich nur Nennbetrag?
7. **Steuerliche Strukturierung:** Soll das Agio in das steuerliche Einlagekonto § 27 KStG fließen für spätere steuerneutrale Rückgewähr?

## Zentrale Schnittstellen

- **Notar** (Beurkundung Kapitalerhöhungsbeschluss Übernahmeerklärung Satzungsneufassung).
- **Steuerberater** (UmwStG-Konformität § 27 KStG-Erfassung Buchwertfortführung).
- **Investor Counsel** (oft US- oder UK-Kanzlei mit Delaware-Denke).
- **CFO und Tax** der Mandantin (Cashflow-Planung Bilanzaufstellung).
- **Handelsregister** (Anmeldung neue Anteilsstruktur Gesellschafterliste § 40 GmbHG).

## Standardmuster Series-A-Runde

| Komponente | Typische Größenordnung |
|---|---|
| Stammkapital vor Runde | EUR 25.000 bis 50.000 |
| Investitionsvolumen | EUR 3 bis 20 Mio |
| Nennbetrag je neuem Geschäftsanteil | EUR 1,00 |
| Anzahl neuer Geschäftsanteile | 5.000 bis 30.000 |
| Ausgabebetrag je Anteil | abhängig von Pre-Money und Cap Table |
| Agio je Anteil | Ausgabebetrag minus EUR 1,00 |
| Agio-Anteil an Investition | typisch 99 bis 99,9 Prozent |
| Stammkapital nach Runde | EUR 35.000 bis 75.000 |

Das ist nicht atypisch sondern Standard. Wer mit einem Lead Investor verhandelt der das Agio vermeiden will hat in den meisten Fällen einen Atypiker am Tisch oder einen Investor der die deutsche GmbH-Struktur nicht versteht.

## Übersetzungstabelle US-Term-Sheet zu deutscher Satzung

| US-Begriff | Deutsche Entsprechung | Häufige Fehler |
|---|---|---|
| Original Purchase Price (OPP) | Ausgabebetrag je Geschäftsanteil | wird mit Kaufpreis übersetzt — falsch |
| Original Issue Price (OIP) | Ausgabebetrag je Geschäftsanteil | wie OPP |
| Par Value | Nennbetrag § 5 Abs. 2 GmbHG | wird mit Nennwert übersetzt — akzeptabel aber nicht juristisch präzise |
| Additional Paid-In Capital (APIC) | Kapitalrücklage § 272 Abs. 2 Nr. 1 HGB | wörtlich Zusätzliches eingezahltes Kapital — falsche Bilanzposition |
| Premium over par | Agio Aufgeld | wird mit Aufpreis übersetzt — umgangssprachlich nicht falsch aber unpräzise |
| Stated Capital | Gezeichnetes Kapital Stammkapital | manchmal mit Grundkapital verwechselt (das ist AG-Begriff § 6 AktG) |
| Issued Shares | Ausgegebene Geschäftsanteile | bei der GmbH gibt es keine Shares im US-Sinne |
| Outstanding Shares | Ausgegebene und nicht eingezogene Geschäftsanteile | dasselbe wie Issued Shares minus Treasury Shares (in DE selten relevant) |
| Authorized Capital | Genehmigtes Kapital — bei der AG § 202 AktG, bei der GmbH seit MoMiG ausdrücklich § 55a GmbHG (für VC-Runden zunehmend genutzt; eigener Skill gesellschaftsgruender-genehmigtes-kapital im Repo) | gelegentlich mit Stammkapital verwechselt; früher verbreiteter Irrtum, GmbH kenne kein genehmigtes Kapital |
| Pre-Money Valuation | Pre-Money-Bewertung Vor-Investitionsbewertung | unkritisch |
| Post-Money Valuation | Post-Money-Bewertung | unkritisch |
| Liquidation Preference 1x OPP | Einfache Liquidationspräferenz auf den Ausgabebetrag | wird oft als 1x Nennbetrag interpretiert — katastrophal für den Investor |
| Anti-Dilution Adjustment | Anti-Dilution-Anpassung des Ausgabebetrags | wird oft als Anpassung der Nennbeträge missverstanden — § 5 Abs. 2 GmbHG verbietet das |
| Conversion Price | Wandlungspreis | unkritisch |
| Conversion Ratio | Wandlungsverhältnis | unkritisch |

## Strukturierungsentscheidungen mit Kostenrelevanz

### Wieviel Stammkapital wird ausgegeben?

Die Versuchung des unerfahrenen Berators ist groß, das Stammkapital möglichst hoch anzusetzen — etwa weil der Investor mehr Stammkapital als ehrenhafter ansieht. Das ist ein Fehler:

- Hohes Stammkapital = dauerhafte Kapitalbindung § 30 GmbHG.
- Kapitalherabsetzung später nur über §§ 58 ff. GmbHG mit Sperrjahr Gläubigeraufruf und 6-Monats-Frist.
- Geschäftsführerhaftung steigt mit der Stammkapitalhöhe wegen § 43 Abs. 3 GmbHG in Verbindung mit § 30 GmbHG.

Praxismuster: Nennbetrag je Anteil bei EUR 1,00 belassen Stammkapital nur um Anzahl der neuen Anteile erhöhen — der Rest als Agio in die Kapitalrücklage.

### Echtes oder unechtes Agio?

| Anwendungsfall | Empfehlung |
|---|---|
| VC-Runde mit Lead Investor | Echtes Agio |
| Bridge-Finanzierung durch Altgesellschafter | Echtes Agio einfacher zu erklären |
| Convertible-Wandlung | Echtes Agio (Wandlungspreis als Ausgabebetrag) |
| Quersubventionierung zwischen Gesellschaftern | Unechtes Agio (schuldrechtliche Nebenabrede) |
| Holding-Strukturierung § 21 UmwStG | Echtes Sachagio zwingend für Buchwertfortführung |
| Mitarbeiterbeteiligung (ESOP) | Hängt vom Modell ab — bei echter Anteilsausgabe echtes Agio bei virtueller Beteiligung kein Agio |

### Fälligkeit des Agios

Standardmuster: Fälligkeit bei Eintragung der Kapitalerhöhung in das Handelsregister. Damit greift Fall 1 — keine Aufnahme des Agios in den Satzungstext erforderlich Kapitalerhöhungsbeschluss und Übernahmeerklärung genügen.

Abweichende Konstellationen bei denen Fall 2 (Aufnahme in Satzungstext) angezeigt ist:

- Staged Closings (z.B. Tranche bei Closing Tranche bei Erreichen von Milestones).
- Earn-out-ähnliche Strukturen mit nachgelagertem Agio.
- Bridge-to-Series-A-Strukturen mit Wandlungsverzögerung.
- Sachagio mit nachgelagerter Werthaltigkeitsprüfung.

Bei Fall 2 unbedingt in den neuen § 3a oder § 4 der Satzung aufnehmen sonst Eintragungshindernis und doppelter Notartermin.

## Schnittstellenmanagement im Deal

### Notar

- Notar verlangt deutsche Beurkundungssprache § 5 BeurkG. Term Sheet bleibt englisch Satzung wird zweisprachig oder deutsch.
- Notar muss Agio in Kapitalerhöhungsbeschluss und Übernahmeerklärung sauber wiederfinden — sonst Beanstandung.
- Bei Sachagio: Sachgründungsbericht analog § 5 Abs. 4 GmbHG mit Werthaltigkeitsbeleg.
- Vor dem Notartermin: Liste der zu beurkundenden Dokumente mit dem Notariat abstimmen.

### Steuerberater

- Bestätigung dass Buchwertfortführung nach § 21 UmwStG möglich ist (qualifizierter Anteilstausch).
- Bestätigung dass das Agio korrekt in das steuerliche Einlagekonto § 27 KStG fließt.
- Bei Verlustvorträgen Prüfung des § 8c KStG (schädlicher Beteiligungserwerb bei mehr als 50 Prozent Übergang).
- Bei US-Investoren mit LP-Struktur: Quellensteuerprüfung DBA-Anwendung.

### Investor Counsel

- US- oder UK-Kanzlei denkt in Delaware-Kategorien — Par Value 0,0001 USD APIC selbstverständlich.
- Erklärungsbedarf für deutsche Spezialitäten: notarielle Beurkundung Vinkulierung § 15 Abs. 5 GmbHG keine echten Anteilsklassen Sonderrechte über Satzungsautonomie und § 35 BGB analog.
- Investor Counsel will oft Liquidation Preference 1x non-participating preferred. Das ist sauber zu übersetzen als einfache Liquidationspräferenz auf den Ausgabebetrag mit Catch-up oder ohne.

### CFO der Mandantin

- Cashflow-Planung: wann fließt das Agio? Voll bei Closing oder gestaffelt?
- Bilanzielle Behandlung: Erhöhung Kapitalrücklage § 272 Abs. 2 Nr. 1 HGB nicht Stammkapital.
- Reporting an Bestandsgesellschafter: wie wird die Verwässerung kommuniziert?

## Häufige Streitpunkte und ihre Lösung

### Liquidation Preference auf Nennbetrag oder Ausgabebetrag

Standard: **Ausgabebetrag** (Nennbetrag plus Agio). Eine Liquidation Preference 1x Nennbetrag wäre für den Investor wirtschaftlich katastrophal — bei einem 99 Prozent Agio bleiben dem Investor 1 Prozent seiner Investition als Vorrecht. Das ist kein Markt.

### Anti-Dilution mit Folgewirkung auf Liquidation Preference

Wenn der Anti-Dilution-Mechanismus den Conversion Price (deutsch: Wandlungspreis) anpasst muss die Liquidation Preference darauf reagieren. Häufig anzutreffen: Weighted Average broad-based oder narrow-based oder Full Ratchet. Bei der GmbH wird das technisch über Anpassung des wirtschaftlichen Bezugswertes umgesetzt nicht über Anpassung des Nennbetrags (§ 5 Abs. 2 GmbHG verbietet Nennbeträge unter EUR 1).

### Pari-passu oder Senior bei mehreren Series

In Series-B-Runden stellt sich die Frage ob die Series-B-Liquidation-Preference pari passu mit Series A oder senior dazu ist. Pari passu ist Markt für Bestandsinvestoren senior typisch für Lead-getriebene B-Runden. Die Satzung muss das eindeutig formulieren — andernfalls Auslegungsstreit.

### Bezugsrechtsausschluss bei Down-Rounds

Bei Down-Rounds (Pre-Money unter letztem Post-Money) ist ein Bezugsrechtsausschluss zugunsten des Lead Investors oft notwendig. Sachliche Rechtfertigung nach Kali+Salz-Grundsatz (BGHZ 71, 40) erforderlich. Das Agio in der Down-Round ist niedriger als in der Vorrunde oder Null — ein **negatives Agio ist rechtlich ausgeschlossen**, weil eine Ausgabe unter pari (Ausgabebetrag unter Nennbetrag) gegen § 9 Abs. 1 GmbHG / § 5 Abs. 2 GmbHG verstößt (Verbot der Unter-pari-Emission). Wirtschaftlich erreicht man die Verwässerung in einer Down-Round durch (i) sehr niedriges oder Null-Agio bei gleichem Nennbetrag, (ii) Ausgabe einer größeren Stückzahl neuer Geschäftsanteile zum reduzierten Preis je Anteil oder (iii) flankierende Instrumente (Wandeldarlehen, Anti-Dilution-Anpassung der bestehenden Series). Wer einem Mandanten ein negatives Agio vorschlägt, beschließt eine nichtige Kapitalerhöhung.

## Anfängerfehler im Corporate-Kontext

- Annahme Lead Investor will hohes Stammkapital. Falsch — Lead Investor will hohe Liquidation Preference und niedriges Stammkapital um spätere Rückgewähr zu erleichtern.
- Annahme das Agio ist ein steuerlicher Trick. Falsch — Agio ist zivilrechtlich begründet steuerlich nur die Erfassung folgt automatisch.
- Annahme jeder Kapitalerhöhungsbeschluss muss das Agio in der Satzung verankern. Falsch — Differenzierung nach Fälligkeit (Fall 1 nein Fall 2 ja).
- Übersetzung der Liquidation Preference auf Nennbetrag. Falsch — Bezugsgröße Ausgabebetrag.
- Versuch das Agio durch Sondervergünstigungen an einzelne Gesellschafter zu umgehen. Riskant — meist kapitalerhaltungswidrig (§ 30 GmbHG) und steuerlich als verdeckte Gewinnausschüttung qualifizierbar.

## Aktuelle Rechtsprechung

- BGH Urt. v. 15.10.2007 — II ZR 216/06 GmbHR 2008, 147 (Sachagio bei Gründung § 3 Abs. 2 GmbHG zwingend).
- BGH Urt. v. 16.02.1981 — II ZR 168/79 BGHZ 80, 129 (Sachkapitalerhöhung Beschluss mit satzungsändernder Wirkung).
- BGH Urt. v. 13.03.1978 — II ZR 142/76 BGHZ 71, 40 (Kali+Salz Bezugsrechtsausschluss).
- BFH Urt. v. 27.05.2009 — I R 53/08 BFHE 226, 500 BStBl II 2010, 1004 (Aufgeld als Anschaffungskosten).
- BFH Urt. v. 03.05.2023 — IX R 12/22 (Überpari-Emission kein § 42 AO-Missbrauch).
- Rechtsprechung: keine weitere Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht Entscheidungsform Datum Aktenzeichen und tragender Aussage verifizieren.

## Verwaltungspraxis

- UmwSt-Erlass v. 11.11.2011 BStBl. I 2011, 1314 Rn. 21.09 ff. (qualifizierter Anteilstausch und Sachagio).

## Outputs

- Term-Sheet-Markup mit Übersetzungstabelle Original Purchase Price etc.
- Memo zur Strukturierung der Kapitalerhöhung mit Empfehlung Stammkapitalhöhe und Agio-Aufteilung.
- Kapitalerhöhungsbeschluss-Entwurf für den Notar.
- Übernahmeerklärung-Entwurf je neuem Gesellschafter.
- Satzungsneufassung mit oder ohne Aufnahme des Agios je nach Fall 1 oder Fall 2.
- Steuerliche Stellungnahme zur Erfassung im Einlagekonto und zur Buchwertfortführung.
- Cap-Table-Update mit Pre-Money Post-Money und Verwässerungsrechnung.
- Closing-Checkliste mit allen Conditions Precedent (siehe corporate-kanzlei-signing-closing-conditions).

## Abgrenzung

- Gesellschaftsrechtliche Dogmatik des Agios siehe Skill agio-und-kapitalruecklage im Plugin gesellschaftsrecht.
- Bewertung des Sachagio-Gegenstands siehe Skill mittelstand-corporate-ma-transaktionsstruktur.
- Steuerliche Vertiefung siehe Plugin steuerrecht-anwalt-und-berater.
- Signing- und Closing-Mechanik siehe Skill corporate-kanzlei-signing-closing-conditions.

## Senior-Review-Gate

Kein Term-Sheet-Markup geht an den Investor Counsel bevor der Senior das Agio-Konzept abgezeichnet hat. Bei Holding-Strukturierung und qualifiziertem Anteilstausch ist ein gemeinsamer Termin mit Steuerberater Notar und Investor Counsel obligatorisch — die Schnittstellen zwischen Gesellschaftsrecht Steuerrecht Bilanzrecht und Notariat sind hier eng und fehleranfällig.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 15 GmbHG
- § 16 GmbHG
- § 46 GmbHG
- § 93 AktG
- § 17 UWG
- § 8c KStG
- § 43 GmbHG
- § 6a GrEStG
- § 21 UmwStG
- § 3 GwG
- § 5 GmbHG
- § 2-122 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
