---
name: pe-eltif-private-markets-euveca-fonds-kvg-erlaubnis
description: "PE Eltif Private Markets Euveca Fonds KVG Erlaubnis: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE Eltif Private Markets Euveca Fonds KVG Erlaubnis

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE Eltif Private Markets Euveca Fonds KVG Erlaubnis** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-006-eltif-2-0-private-markets` | Prüft, wann ein ELTIF als reguliertes Vehikel für Private Equity, Infrastruktur oder Private Debt sinnvoll ist. |
| `pe-007-euveca-und-vc-fonds` | Prüft EuVECA-Label, Venture-Capital-Fonds, Start-up-Portfolios, Minderheitsbeteiligungen und zulässige Assets. |
| `pe-008-kvg-erlaubnis-registrierung-auslagerung` | Ermittelt, ob eine KVG-Erlaubnis, Registrierung oder Auslagerungsstruktur erforderlich ist. |
| `pe-009-verwahrstelle-und-admin-funktionen` | Prüft Verwahrstelle, Fondsadministration, Bewertung, NAV, Capital Calls, Reporting und Kontrollkette. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE Eltif Private Markets Euveca Fonds KVG Erlaubnis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-006-eltif-2-0-private-markets`

**Fokus:** Prüft, wann ein ELTIF als reguliertes Vehikel für Private Equity, Infrastruktur oder Private Debt sinnvoll ist.

# ELTIF 2.0: europäischer Long-Term-Fund für Private Markets

## Fachkern: ELTIF 2.0: europäischer Long-Term-Fund für Private Markets
- **Spezialgegenstand:** ELTIF 2.0: europäischer Long-Term-Fund für Private Markets wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill stellt EU-Pass, Retail-Zugang, Anlagegrenzen, Liquidität und Vertrieb von ELTIF 2.0 gegenüber einem deutschen Spezial-AIF dar. Seit 10.01.2024 gilt die novellierte ELTIF-Verordnung (EU) 2023/606, die Retail-Hürden gesenkt, Master-Feeder zugelassen, Fund-of-Funds erleichtert und das semi-liquide Segment für Private Markets stark erweitert hat.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Soll der Fonds in mehreren EU-Mitgliedstaaten an Retail-Anleger vertrieben werden?
2. Asset-Klasse: PE, Infrastruktur, Private Debt, Real Estate, Wachstumsfonds für KMU?
3. Soll das Vehikel evergreen/open-end oder closed-end laufen?
4. Welche Liquiditätsfenster sind vorgesehen (z. B. quartalsweise Rücknahme mit Gating)?
5. Geplante Anlegerstruktur (institutionell + Retail oder Retail-only)?
6. Master-Feeder-Setup mit Spezial-AIF im Hintergrund denkbar?
7. SFDR-Kategorisierung Art. 6, 8 oder 9?
8. Vertriebspartner (Banken, Robo-Advisor, Plattformen) bereits identifiziert?

## Rechtlicher und transaktionaler Rahmen

ELTIF-VO (EU) 2015/760 in der Fassung (EU) 2023/606 (ELTIF 2.0, anwendbar seit 10.01.2024); RTS-Verordnungen der ESMA zu ELTIF 2.0 (vom Anwender mit jeweils aktuellem Stand zu prüfen); KAGB §§ 261, 320 i.V.m. § 230 KAGB; KAGB-Vertriebsregime §§ 293 ff. mit EU-Pass; MiFID-II-Zielmarkt-Konzept; PRIIPs-KID (VO (EU) 1286/2014) für Retail-Vertrieb; SFDR; KAGB-Verwahrstelle § 80; Geeignetheitsprüfung beim Vertrieb an Retail (§ 64 WpHG, jetzt § 87 WpHG vom Anwender zu prüfen).

## / Schritt für Schritt

1. Anlegeruniversum klären: ausschließlich institutionell (dann Spezial-AIF oft besser), oder gemischt mit Retail-Zugang (dann ELTIF).
2. Asset-Mix prüfen: ELTIF 2.0 verlangt 55 Prozent in "qualifying assets" (Equity/Debt von KMU, Real Assets, andere ELTIF/EuVECA/EuSEF, Fund-of-ELTIF).
3. Liquiditätsdesign: closed-end (klassisch 10 Jahre), semi-liquide (mit Redemption Gates), oder evergreen.
4. Master-Feeder-Architektur: ELTIF als Retail-Feeder in deutschen Spezial-AIF als Master?
5. KVG-Auswahl und Verwahrstelle (§ 80 KAGB).
6. PRIIPs-KID erstellen — Retail-relevante Risikoindikatoren, Performance-Szenarien.
7. SFDR-Disclosure und PAI-Statement.
8. EU-Pass-Vertriebsanzeige bei BaFin (§§ 322 ff. KAGB) und Notifizierung in Ziel-MS.

## Trade-off-Matrix

| ELTIF 2.0 | Deutscher Spezial-AIF | Empfehlung |
| --- | --- | --- |
| Retail-fähig (ohne Mindestticket nach ELTIF 2.0) | Nur professionell / semiprofessionell | ELTIF, wenn Retail-Distribution geplant |
| EU-Pass automatisch | EU-Pass nur über AIFMD-Notifizierung | ELTIF bei paneuropäischer Vertriebsstrategie |
| 55 Prozent Qualifying-Asset-Quote | Keine starre Anlagegrenze | Spezial-AIF bei flexibler Allokation |
| Strikte Diversifikation (10 Prozent pro Asset) | LPA-Definition flexibel | Spezial-AIF für konzentrierte Buyout-Portfolien |
| PRIIPs-KID Pflicht | Kein KID für rein professionelle | ELTIF: zusätzlicher Aufwand bedacht |

## Praktikertipps Big-Law-PE

- ELTIF 2.0 hat das Mindestticket für Retail aufgehoben — aber MiFID-Geeignetheitsprüfung bleibt zwingend.
- Master-Feeder-Setup (ELTIF als Feeder in Spezial-AIF-Master) ist seit 2024 ausdrücklich zulässig — beliebt bei Sponsoren, die institutionelle und Retail-Mandate trennen wollen.
- Redemption Gates und "Notice Periods" sauber kalibrieren; ESMA RTS legen Untergrenzen fest.
- Vertriebspartner-Auswahl entscheidet über Erfolg: Banken (S-Sparkassen, Genossenschaft) vs. Plattformen (Trade Republic, Scalable) haben unterschiedliche Onboarding-Logiken.
- PRIIPs-KID ist Haftungsrisiko — bei Performance-Szenario-Fehlern droht Anlegerhaftung.
- ELTIF-Steuer in DE: Investmentfonds nach InvStG mit Teilfreistellung — abhängig von Asset-Mix (Equity-Quote >= 51 Prozent: 30 Prozent Teilfreistellung).

## Mustertexte / SPA-Klauseln

ELTIF-Anlagepolitik (Beispiel):

> Mindestens 55 Prozent des Fondsvermögens werden in zulässige Anlagewerte im Sinne von Art. 10 ELTIF-VO investiert, davon mindestens 70 Prozent in Beteiligungen an oder Darlehen an qualifizierte Portfoliounternehmen mit Sitz in der EU. Maximale Einzelposition: 10 Prozent des Fondsvermögens.

Redemption-Gate-Klausel:

> Die Verwaltungsgesellschaft kann Rücknahmen aussetzen oder kürzen ("Gating"), wenn die Summe der Rücknahmewünsche eines Liquiditätsfensters 5 Prozent des Nettoinventarwerts übersteigt. Anteilsrücknahmen erfolgen quartalsweise mit Notice Period von 90 Tagen.

## Typische Fehler

- ELTIF-Asset-Quote (55 Prozent qualifying) wird verfehlt, weil Cash-Buffer zu hoch ist.
- Retail-Vertrieb ohne PRIIPs-KID oder ohne Geeignetheitsprüfung.
- Master-Feeder ohne saubere Tax-Brücke — Doppelbelastung droht.
- Redemption Gates zu großzügig kalibriert — Run-Risk bei Stress.

## Querverweise

- pe-004 für KAGB-Scope.
- pe-005 für Spezial-AIF als Alternative oder Master.
- pe-008 für KVG-Erlaubnis.
- pe-010 für Vertrieb und Fundraising.
- pe-018 für SFDR/ESG.

## Quellen Stand 06/2026

- ELTIF-VO (EU) 2015/760 i.d.F. (EU) 2023/606 (ELTIF 2.0, anwendbar seit 10.01.2024).
- ESMA Final Report und RTS zu ELTIF 2.0 (jeweils aktuelle Fassung vom Anwender zu prüfen).
- KAGB §§ 230, 261, 293 ff., 320, 322 ff. (Vertrieb).
- PRIIPs-VO (EU) 1286/2014 und Delegated Regulation (EU) 2017/653.
- MiFID II (RL 2014/65/EU), §§ 63 ff., 87 WpHG.
- SFDR (VO (EU) 2019/2088); InvStG §§ 20, 21 (Teilfreistellung).

## 2. `pe-007-euveca-und-vc-fonds`

**Fokus:** Prüft EuVECA-Label, Venture-Capital-Fonds, Start-up-Portfolios, Minderheitsbeteiligungen und zulässige Assets.

# EuVECA und VC-Fonds: Wagniskapital richtig etikettieren

## Fachkern: EuVECA und VC-Fonds: Wagniskapital richtig etikettieren
- **Spezialgegenstand:** EuVECA und VC-Fonds: Wagniskapital richtig etikettieren wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill liefert die Strukturentscheidung zwischen EuVECA-Label (VO 345/2013), klassischem Sub-Threshold-AIFM (§ 2 Abs. 4 KAGB) und vollerlaubnispflichtiger KVG für Venture-Capital-Fonds. Kerneinsatz bei Fondsmarketing und wenn ein VC-Fonds nicht wie ein Buyout-Fonds funktionieren soll — andere Anlegerlogik, andere Ticketgrößen, andere Reporting-Erwartungen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Geplantes Fondsvolumen (EuVECA: < 500 Mio. EUR; sub-threshold-AIFM: typisch < 100/500 Mio. EUR)?
2. Soll EU-weit vertrieben werden (EuVECA hat eigenen Pass)?
3. Ticketgröße der LPs (EuVECA-Mindestticket 100 000 EUR plus Eignungserklärung)?
4. Investmentstrategie: Seed, Series A, Growth, Cross-Stage?
5. Geografischer Fokus (EuVECA verlangt mindestens 70 Prozent in "qualifying portfolio undertakings")?
6. ESG-/Impact-Profil?
7. Side-Letter-Erwartungen (Carry-Allocation an Operating Partner, Advisory Board)?
8. Anlegerstruktur (HNWI, Family Offices, Corporate VCs, Pension Funds)?

## Rechtlicher und transaktionaler Rahmen

EuVECA-VO (EU) 345/2013, geändert durch VO (EU) 2017/1991; ESMA-Q&A zu EuVECA (vom Anwender mit aktuellem Stand zu prüfen); KAGB § 2 Abs. 4 (Sub-Threshold-AIFM für VC < 500 Mio. EUR Lock-up >= 5 Jahre); § 337 KAGB (Vertriebsregime EuVECA); Wirtschaftlich Berechtigte i.S.d. GwG bei Start-up-Targets; Beteiligungsverträge nach BGB, GmbHG/AktG; INVEST-Zuschuss als steuerliche Spielwiese; § 8c, § 8d KStG für Mantel-/Forschungs-Verlustvorträge; Wachstumschancengesetz und Zukunftsfinanzierungsgesetz 2023/2024 (Mitarbeiterbeteiligung in Start-ups, § 19a EStG).

## / Schritt für Schritt

1. Geplantes Anlegeruniversum und Asset-Allokation klären.
2. EuVECA-Test: 70 Prozent Qualifying Portfolio Undertakings (KMU, max. 499 Beschäftigte, nicht börsennotiert, Umsatz <= 50 Mio. EUR), Restquote in Cash/Equivalents.
3. Manager-Registrierung als EuVECA-Manager bei BaFin oder Heimataufsicht.
4. Anlagebedingungen mit EuVECA-Asset-Test verzahnen.
5. Subscription-Paket mit Eignungserklärung (Mindestticket 100 000 EUR plus Sachkundeerklärung).
6. ESG-Sondervarianten (EuSEF für Social Entrepreneurship als Alternative) prüfen.
7. Vertriebsanzeige in Ziel-MS über BaFin-Pass.

## Trade-off-Matrix

| EuVECA | Klassischer Sub-Threshold-AIFM | Vollerlaubnis-KVG |
| --- | --- | --- |
| EU-Pass automatisch | Kein EU-Pass | EU-Pass via AIFMD |
| Mindestticket 100 000 EUR + Eignungserklärung | Keine Untergrenze (§ 1 Abs. 19 KAGB beachten) | Frei skalierbar |
| 70 Prozent QPU-Asset-Test | Keine Asset-Test | Anlagepolitik in LPA |
| Volumen < 500 Mio. EUR | < 100 Mio. (mit Hebel) bzw. 500 Mio. (ohne Hebel, Lock-up >= 5 Jahre) | Beliebige Größe |

## Praktikertipps Big-Law-PE

- "Qualifying Portfolio Undertakings" sind KMU (nicht börsennotiert, < 499 Beschäftigte, Umsatz <= 50 Mio. EUR) — Wachstum über Schwellen führt zu Asset-Drift; Übergangsregel beachten.
- EuVECA-Pass ist deutlich günstiger als AIFMD-Notifizierung, aber Manager bleibt 1:1 registriert; bei zweitem, größerem Fonds Vollerlaubnis prüfen.
- INVEST-Zuschuss für Privatanleger ist Marketing-Instrument, aber begünstigt nur natürliche Personen; Fondsstruktur muss INVEST-konform sein.
- Operating-Partner-Carry-Allocation präzise dokumentieren — sonst arbeitsrechtliche Reklassifizierung droht.
- Founder-Friendly-Klauseln (Tag-Along, Founder Vesting Acceleration) standardisieren; bei späteren Folge-Runden Stress mit Series-A/B-Investoren möglich.
- § 19a EStG (Mitarbeiterbeteiligung) bietet seit 2024 erweiterte Möglichkeiten — in MIP/ESOP einbauen.

## Mustertexte / SPA-Klauseln

Qualifying-Portfolio-Undertaking-Test (LPA):

> Mindestens 70 Prozent des aggregierten Kapitalwerts der Beteiligungen entsprechen Qualifying Portfolio Undertakings i.S.v. Art. 3(d) EuVECA-VO zum Zeitpunkt der Investition. Eine spätere Überschreitung der Schwellen durch das Portfolio führt nicht zu einer Disqualifikation.

Founder Vesting (EN/DE):

> Founder Shares vest over 48 months with a 12-month cliff. Upon a Good Leaver event, vested shares are retained; Bad Leaver triggers compulsory transfer at nominal value. / Gründeranteile vesten über 48 Monate mit 12-Monats-Cliff. Bei Good Leaver bleiben gevestete Anteile erhalten; Bad Leaver löst Pflichtübertragung zu Nominalwert aus.

## Typische Fehler

- 70-Prozent-Asset-Test wird bei Recycling unterschritten — Disqualifikation.
- Mindestticket 100 000 EUR ohne dokumentierte Eignungserklärung gesammelt.
- INVEST-Zuschuss kollidiert mit Fonds-Struktur, weil Privatanleger nicht direkt halten.
- Founder Vesting fehlt — späterer Streit beim Founder-Exit.

## Querverweise

- pe-004 für KAGB-Scope und Fund Formation.
- pe-005 für Spezial-AIF als Alternative.
- pe-008 für KVG-Registrierung.
- pe-014 für Carry-Strukturen.
- pe-020 für Tax-Aspekte (§ 8c/8d KStG, § 19a EStG).

## Quellen Stand 06/2026

- EuVECA-VO (EU) 345/2013 i.d.F. (EU) 2017/1991.
- ESMA-Q&A EuVECA (jeweils aktuelle Fassung vom Anwender zu prüfen).
- KAGB § 2 Abs. 4, § 337 (Vertriebsregime).
- INVEST-Förderrichtlinie des BMWK (Stand vom Anwender zu prüfen).
- § 19a EStG (Zukunftsfinanzierungsgesetz, Stand 2024); § 8c, § 8d KStG.
- Wachstumschancengesetz 2024.

## 3. `pe-008-kvg-erlaubnis-registrierung-auslagerung`

**Fokus:** Ermittelt, ob eine KVG-Erlaubnis, Registrierung oder Auslagerungsstruktur erforderlich ist.

# KVG: Erlaubnis, Registrierung und Auslagerung

## Fachkern: KVG: Erlaubnis, Registrierung und Auslagerung
- **Spezialgegenstand:** KVG: Erlaubnis, Registrierung und Auslagerung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill baut die BaFin-Kommunikations- und Dokumentenmatrix für Fondsmanager. Kernfrage: Vollerlaubnis nach §§ 17 ff. KAGB, Registrierung als Sub-Threshold-AIFM nach § 2 Abs. 4/5 KAGB oder Auslagerung auf Service-KVG ("Master-KVG-Modell"). Setup-Zeit, Kosten, Personalanforderungen und EU-Pass-Verfügbarkeit unterscheiden sich erheblich.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Geplantes AuM-Wachstum (jetzt vs. 5 Jahre)?
2. Sub-Threshold-Kriterien erfüllt: < 100 Mio. EUR mit Hebel oder < 500 Mio. EUR ohne Hebel und Lock-up >= 5 Jahre?
3. EU-Pass für Vertrieb gewünscht (zwingt zu Vollerlaubnis)?
4. Vorhandenes Personal: zwei Geschäftsleiter (§ 18 KAGB) mit Branchenerfahrung?
5. Risikomanagement, Compliance, Innenrevision intern oder ausgelagert?
6. Verwahrstelle bereits mandatiert?
7. Budget für Setup (Vollerlaubnis: 12–24 Monate, 1.5–3 Mio. EUR Anlauf; Master-KVG: 2–6 Monate, ab 200 TEUR p.a.)?
8. IT-Set-up (Portfoliomanagement, Risikosystem, Reporting)?

## Rechtlicher und transaktionaler Rahmen

KAGB §§ 17 ff. (Vollerlaubnis-Voraussetzungen), § 18 (Geschäftsleiter), § 19 (Kapitalanforderungen: 125 000 EUR + 0.02 Prozent AuM, Cap 10 Mio. EUR; Eigenmittelaufschlag bei höheren AuM), § 20 (Eigenmittel-Pufferanforderung), § 21 (Erlaubnisantrag), § 22 (Versagungsgründe), § 26 (Auslagerung); § 2 Abs. 4/5 (Sub-Threshold-AIFM, Registrierung); AIFMD-Delegated-Regulation (EU) 231/2013 Art. 76 ff. (Auslagerung); BaFin-MaRisk-VA, MaComp; BaFin-Auslegungshilfe zu Auslagerungen (vom Anwender mit aktuellem Stand zu prüfen).

## / Schritt für Schritt

1. AuM-Plan und Wachstumsperspektive klären — bestimmt, ob Sub-Threshold-Pfad realistisch ist.
2. Vertriebsperspektive: nur DE oder paneuropäisch (EU-Pass → Vollerlaubnis).
3. Personalverfügbarkeit: zwei Geschäftsleiter mit Branchenerfahrung sind harte Voraussetzung.
4. Auslagerungsplan: Portfolio Management, Risk Management, Administration, IT, AML — was bleibt KVG-Kernfunktion?
5. Kapitalplan: § 19 KAGB-Mindestkapital plus Eigenmittel-Puffer plus Operating Reserve.
6. Erlaubnisantrag inkl. Geschäftsplan, Geschäftsorganisation, Risikomanagement-Konzept, Geldwäscheprävention, Vergütungspolitik, IT-Sicherheit.
7. BaFin-Vorgespräch (typisch 6–8 Wochen Vorlauf).
8. Antragsphase 6–12 Monate; bei Registrierung nach § 2 Abs. 4/5: 4–8 Wochen.

## Trade-off-Matrix

| Vollerlaubnis-KVG | Registrierung Sub-Threshold | Auslagerung an Master-KVG |
| --- | --- | --- |
| EU-Pass, beliebige AuM | Kein EU-Pass, AuM-Cap | Schneller Start, keine eigene Erlaubnis |
| 12–24 Monate Setup | 4–8 Wochen | 2–6 Wochen |
| Kapital ab 125 000 EUR + 0.02 % AuM | Geringere Eigenmittel | Service-KVG-Gebühr (10–25 Bps p.a. plus Fixum) |
| Volle Reportingpflichten (AIFMD Annex IV) | Reduzierte Reportingpflichten | Service-KVG übernimmt |
| Volle Personalstärke | Skinny Team möglich | Sponsor stellt nur Advisor-Team |

## Praktikertipps Big-Law-PE

- "Zwei Geschäftsleiter" mit Branchenerfahrung ist häufig der knappste Engpass — Headhunter parallel zur Antragsphase ansetzen.
- Auslagerung von Portfolio Management auf Sponsor-Tochter ist die "Investmentadvisor-Konstruktion" — BaFin verlangt klare Trennung von Letztverantwortung.
- Master-KVG-Vertrag enthält oft Exit-Penalty bei Wechsel auf eigene KVG; Penalty-Caps und Servicequalitäts-KPIs sauber verhandeln.
- DORA-Compliance (EU 2022/2554) gilt seit 17.01.2025 auch für KVGs — ICT-Risikomanagement, TLPT, Auslagerungsregister.
- AIFMD-II (RL (EU) 2024/927, Anwendung ab April 2026) verschärft Auslagerungs-Reporting und Loan-Origination-Regelung — bei Direct-Lending-Fonds prüfen.
- Vergütungspolitik nach Annex II AIFMD: 50 Prozent variable Vergütung in Fondsanteilen, mindestens 40 Prozent Deferral über 3–5 Jahre — beim Onboarding von Senior Hires bedenken.

## Mustertexte / SPA-Klauseln

Service-KVG-Vertrag (Auszug):

> Die KVG behält die Letztverantwortung für Portfolio Management und Risikomanagement. Der Investmentadvisor erbringt Anlageempfehlungen ohne Entscheidungsbefugnis. Anlageentscheidungen werden ausschließlich durch die KVG getroffen und dokumentiert.

Auslagerungsregister (Pflichtfeld):

> Bezeichnung des Auslagerungsempfängers, Sitz, ausgelagerte Funktion, Vertragsbeginn, Wesentlichkeit (ja/nein), Sub-Outsourcing, Notfallplan, Kündigungsfrist, Datenschutzbasis (Art. 28 DSGVO), letzte Risikobewertung.

## Typische Fehler

- Vollerlaubnisantrag mit Geschäftsleitern ohne Branchenerfahrung — Versagungsgrund § 22 Abs. 1 Nr. 4 KAGB.
- Registrierungspfad gewählt, dann Wachstum über AuM-Schwelle — zwangsweise Vollerlaubnis ohne ausreichende Vorbereitung.
- Auslagerung ohne Letztverantwortungs-Klausel — § 26 KAGB-Verstoß.
- DORA-Auslagerungsregister fehlt seit 2025 — Bußgeldgefahr.

## Querverweise

- pe-004 für KAGB-Scope.
- pe-005 für Spezial-AIF.
- pe-009 für Verwahrstelle.
- pe-010 für Fundraising mit EU-Pass.

## Quellen Stand 06/2026

- KAGB §§ 2 Abs. 4/5, 17–26.
- AIFMD (RL 2011/61/EU); AIFMD-II (RL (EU) 2024/927, Anwendung ab April 2026).
- VO (EU) 231/2013 Art. 76 ff. Auslagerung.
- DORA (VO (EU) 2022/2554, anwendbar seit 17.01.2025).
- BaFin-Auslegungshilfe und MaRisk-/MaComp-Rundschreiben (jeweils aktueller Stand vom Anwender zu prüfen).

## 4. `pe-009-verwahrstelle-und-admin-funktionen`

**Fokus:** Prüft Verwahrstelle, Fondsadministration, Bewertung, NAV, Capital Calls, Reporting und Kontrollkette.

# Verwahrstelle, Administrator und Backoffice

## Fachkern: Verwahrstelle, Administrator und Backoffice
- **Spezialgegenstand:** Verwahrstelle, Administrator und Backoffice wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill ordnet die Funktionstrennung zwischen Verwahrstelle (§ 80 KAGB), Fondsadministrator und KVG. Besonders wichtig, wenn Sponsor und Administrator Aufgaben unscharf verteilen — typische Streitpunkte sind NAV-Bewertung, Capital-Call-Berechnung, Waterfall-Berechnung, Reporting-Verantwortung und ILPA-Datenformate.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche Fondsart (offener/geschlossener Spezial-AIF, ELTIF, EuVECA)?
2. Verwahrstelle bereits ausgewählt? Verwahrstellenvertrag in welcher Phase?
3. Administrator: extern (Apex, MUFG, Sanne, Citco, IQ-EQ) oder intern beim Sponsor?
4. Bewertungsmodell: Fair Value mit Independent Pricing, oder Sponsor-driven?
5. Reporting-Format: ILPA Templates, GIPS, eigene Sponsor-Reports?
6. Capital-Call-Frequenz (quartalsweise vs. ad-hoc)?
7. AIFMD-Annex-IV-Reporting an BaFin: wer erstellt, wer prüft, wer reicht ein?
8. Tax-Reporting für deutsche, EU- und US-Investoren?

## Rechtlicher und transaktionaler Rahmen

KAGB § 80 (Verwahrstellenpflicht für AIF), §§ 81–90 (Aufgaben der Verwahrstelle: Verwahrung, Zahlungsstrom-Überwachung, Kontrollfunktionen), § 84 (Haftung der Verwahrstelle), § 36 (Auslagerung Administration); AIFMD Art. 21 (Depositary); VO (EU) 231/2013 Art. 88 ff. (Depositary-Pflichten); Joint Audit der KVG-Jahresberichte (§ 105 KAGB); ILPA Standardized Reporting Templates (Stand 2.1 oder aktueller, vom Anwender zu prüfen); CRR/CRD für Verwahrstellen die Banken sind; DORA (VO (EU) 2022/2554) für ICT-Outsourcing seit 17.01.2025.

## / Schritt für Schritt

1. Funktionsmatrix erstellen: Wer entscheidet (KVG), wer kontrolliert (Verwahrstelle), wer rechnet (Administrator)?
2. Verwahrstellenvertrag verhandeln: Haftungs-Caps, Sub-Custodian-Genehmigung, Notfallplan, Kündigungsfrist (typisch 6–12 Monate).
3. Administrator-Mandat: NAV-Frequency, Capital-Call-Notice-Lead-Time, Waterfall-Berechnung, KYC/AML Support.
4. Pricing Policy: Mark-to-Market wo möglich; Mark-to-Model mit Independent Pricing für illiquide PE-Assets (typisch IPEV-Bewertungsstandards).
5. ILPA-Reporting-Schema definieren; Master Data Format vor Initial Closing fixieren.
6. AIFMD-Annex-IV-Reporting-Process: KVG erstellt, Verwahrstelle attestiert nicht, Administrator beliefert, BaFin-Frist (typisch Q+1).
7. Bei Issues: Eskalationspfad (LPAC, Beirat, externe Bewertungsstelle).

## Trade-off-Matrix

| Externe Verwahrstelle (Bank) | Verwahrstelle-Light für illiquide AIF | Intern beim Konzern |
| --- | --- | --- |
| Volle Custody-Funktion | Reduzierte Verwahrung, mehr Kontrollfokus | Konzerninterne Lösung mit Konflikt-Risiko |
| Hohe Fees (5–15 Bps p.a.) | Fees 3–8 Bps p.a. | Variabel |
| Skalierung gut | Spezialisten knapp | Konfliktrisiko mit Sponsor |
| Hoher Status bei Investoren | Akzeptanz wachsend | Nur bei Konzern-Captive-Lösungen üblich |

## Praktikertipps Big-Law-PE

- IPEV-Bewertungsstandards (International Private Equity and Venture Capital Valuation Guidelines, Stand 2022) sind Marktstandard; Abweichungen dokumentieren.
- Verwahrstellen-Haftungs-Caps häufig auf das 5- bis 10-fache der Jahresgebühr — bei hohem AuM/Asset-Risiko Verhandlung der Caps.
- Sub-Custody-Genehmigung: bei internationalen Assets Vorabgenehmigung jeder neuen Jurisdiktion einplanen.
- Administrator-Wechsel ist riskant — Datenmigration und Investor-On-Boarding mindestens 6 Monate planen.
- Bei NAV-Disputen frühzeitig externe Valuer ("Big Four" oder Boutiquen) für Independent Pricing einschalten.
- DORA-ICT-Risikomanagement: TLPT-Test mit kritischen Vendoren mind. alle 3 Jahre für signifikante Marktteilnehmer.

## Mustertexte / SPA-Klauseln

Verwahrstellen-Haftung (Auszug):

> Die Verwahrstelle haftet gegenüber Anlegern für den Verlust verwahrter Finanzinstrumente verschuldensunabhängig (§ 84 Abs. 2 KAGB), für sonstige Verluste nur bei schuldhafter Pflichtverletzung. Die Gesamthaftungssumme pro Geschäftsjahr ist auf das Fünffache der Jahresgebühr begrenzt, ausgenommen Vorsatz und grobe Fahrlässigkeit.

NAV-Frequenz (Anlagebedingungen):

> Der Nettoinventarwert wird quartalsweise zum letzten Bankarbeitstag des Quartals ermittelt. Capital Calls werden mit einer Vorlauffrist von zehn Bankarbeitstagen angefordert, Distributionen mit fünf Bankarbeitstagen.

## Typische Fehler

- Verwahrstellenvertrag mit Haftungsausschluss — § 84 KAGB ist halbzwingend.
- Administrator und KVG arbeiten mit unterschiedlichen Master-Data — Reporting-Differenzen.
- IPEV-Bewertungsmethodik nicht dokumentiert — BaFin-Beanstandung.
- DORA-Vendoren-Risikobewertung fehlt seit 2025.

## Querverweise

- pe-004 für KAGB-Scope.
- pe-005 für Spezial-AIF.
- pe-008 für KVG-Auslagerung.
- pe-013 für Capital Calls.
- pe-014 für Waterfall-Berechnung.

## Quellen Stand 06/2026

- KAGB §§ 36, 80–90, 105.
- AIFMD (RL 2011/61/EU) Art. 21; VO (EU) 231/2013 Art. 88 ff.
- IPEV Valuation Guidelines (Stand 2022 oder aktueller, vom Anwender zu prüfen).
- DORA (VO (EU) 2022/2554, seit 17.01.2025).
- ILPA Standardized Reporting Templates 2.1 (jeweils aktueller Stand vom Anwender zu prüfen).
