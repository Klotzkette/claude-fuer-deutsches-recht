---
name: pe-fundraising-vertrieb-subscription-package-side-lp-transfer
description: "PE Fundraising Vertrieb Subscription Package Side LP Transfer: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE Fundraising Vertrieb Subscription Package Side LP Transfer

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE Fundraising Vertrieb Subscription Package Side LP Transfer** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-010-fundraising-und-vertrieb` | Prüft Pitch Deck, PPM, Zeichnungsschein, Vertriebsanzeige, Reverse Solicitation und Anlegerkommunikation. |
| `pe-011-subscription-package-und-side-letter` | Prüft Beitrittserklärung, KYC, Tax Forms, MFN, Reporting, No-Fault-Divorce, Key-Person und Most-Favoured-Nation. |
| `pe-012-lp-transfer-und-secondary` | Begleitet die Übertragung von Fondsanteilen, Zustimmungserfordernisse, KYC-Neuaufnahme und Käufer-DD. |
| `pe-013-capital-calls-und-defaulting-lp` | Prüft Kapitalabrufe, Säumnisfolgen, Verwässerung, Verzugszinsen, Ausschluss und Enforcement gegen Anleger. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE Fundraising Vertrieb Subscription Package Side LP Transfer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-010-fundraising-und-vertrieb`

**Fokus:** Prüft Pitch Deck, PPM, Zeichnungsschein, Vertriebsanzeige, Reverse Solicitation und Anlegerkommunikation.

# Fundraising und Vertrieb: Teaser bis Subscription

## Fachkern: Fundraising und Vertrieb: Teaser bis Subscription
- **Spezialgegenstand:** Fundraising und Vertrieb: Teaser bis Subscription wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill verhindert, dass Vertrieb vor Regulierungs- und Compliance-Freigabe losläuft. Kernprüfung: KAGB-Vertriebsregime (§§ 293 ff. für inländische AIF, §§ 320 ff. für EU-AIF, § 330 ff. für ausländische AIF), Reverse-Solicitation-Doktrin, MiFID-Geeignetheitsprüfung, MAR-relevante Marketing-Vermerke und Greenwashing-Risiken nach SFDR.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welcher Fonds soll vertrieben werden (DE Spezial-AIF, EU-AIF mit Pass, Drittstaaten-AIF)?
2. Welche Anlegerkategorie wird angesprochen (professionell, semiprofessionell, retail)?
3. Welche Jurisdiktion(en) Ziel? Vertriebsanzeige BaFin und/oder Notifizierung in Ziel-MS?
4. Welche Marketingmaterialien existieren (Teaser, PPM, Pitch Deck, DDQ, Datenraum)?
5. Reverse-Solicitation-Vorgehen geplant?
6. Placement Agent eingeschaltet? Erlaubnispflichtig?
7. ESG-/Sustainability-Aussagen im Marketingmaterial (SFDR-Konsistenz)?
8. Datenschutz: AVV mit VDR und Placement Agent?

## Rechtlicher und transaktionaler Rahmen

KAGB §§ 293–311 (Vertrieb inländischer AIF an semiprofessionelle Anleger), §§ 312, 316 (an Privatanleger), §§ 320–321 (EU-AIF mit Pass), §§ 322–331 (Drittstaaten-AIF, National Private Placement Regime); § 295 KAGB Marketing-Kommunikations-Anforderungen; MiFID II Art. 24 ff., WpHG §§ 63 ff., 87 (Geeignetheitsprüfung); PRIIPs (VO 1286/2014) bei Retail-Vertrieb; SFDR Marketing-Kommunikation-Konsistenz (Art. 13 SFDR i.V.m. ESMA-Guidelines); Reverse-Solicitation-Doktrin (ESMA-Q&A AIFMD; BaFin-Auslegungshinweis vom Anwender zu prüfen); Wettbewerbsrecht (UWG, Greenwashing-Klauseln).

## / Schritt für Schritt

1. Vertriebsregime klären: § 293 (inländischer AIF, semiprofessionell) — kurzer Anzeigepfad bei BaFin (3 Wochen Stillhalte); § 312 (Retail) — erfordert Vertriebsanzeige mit Anlagebedingungen und Verkaufsprospekt.
2. Marketingmaterialien gegen § 295 KAGB prüfen: korrekte Risikohinweise, keine Performance-Garantie-Ansätze, "as a marketing communication" Kennzeichnung.
3. SFDR-Konsistenz: Aussagen im PPM müssen mit Disclosure-Dokumenten (Pre-Contractual Disclosure, Website) übereinstimmen.
4. Placement Agent: KAGB-Erlaubnis (oder MiFID-Pass) prüfen; Vertrag mit Conduct- und IDD-Klauseln.
5. Reverse Solicitation: dokumentierte Anlegerinitiierung; "Pull"-Doktrin streng prüfen.
6. Datenraum-Set-up mit Vertraulichkeitsmanagement, Watermarking, Audit-Trail.
7. Closing-Workflow: Sub-Doc-Eingang, KYC-Komplettierung, Anlegerklassifizierung, Side-Letter-Aushandlung.

## Trade-off-Matrix

| Vertriebsanzeige (Pass) | National Private Placement Regime | Reverse Solicitation |
| --- | --- | --- |
| Aktive Marketingrechte EU-weit | Limitierte Reichweite, häufig nur professionelle | Kein aktives Marketing, nur Anleger-initiiert |
| 4–8 Wochen Vorlauf | 4–12 Wochen pro MS | Sofort, aber engste Linie |
| AIFMD-Compliance erforderlich | Manche MS verlangen zusätzliche Bedingungen | Hohes Dokumentationsrisiko |
| Standardstrategie für EU-Sponsoren | Drittstaaten-AIF | Notfall- und Add-On-Lösung |

## Praktikertipps Big-Law-PE

- Reverse Solicitation ist 2024/2025 zunehmend eng ausgelegt — ESMA/BaFin verlangen klare Anleger-Initiation Dokumentation; bloße Folge-E-Mail-Konversation reicht oft nicht.
- PPM darf keine "Track Record"-Aussagen ohne saubere Datenkonsistenz enthalten; "verified GIPS"-Aussagen prüfen lassen.
- Greenwashing: ESMA und BaFin haben 2024/2025 mehrere Bußgelder verhängt; "ESG"-Aussagen mit SFDR-Klassifizierung konsistent halten.
- Placement-Agent-Verträge mit Erfolgsfee enthalten häufig kein "tail fee" — Verhandlung sinnvoll, falls Anleger erst nach Vertragsende zeichnet.
- Datenraum-Index pre-launch sauber strukturieren; Watermarking pro Investor und Trail-Logs (für spätere Confidentiality-Disputes).
- AIFMD-II ab April 2026: Pre-Marketing-Regime wird stringenter, Notifizierung nach Pre-Marketing wird erweitert.

## Mustertexte / SPA-Klauseln

Reverse-Solicitation-Erklärung (im Sub-Doc):

> Der Anleger bestätigt, dass er aus eigener Initiative ohne vorhergehende Aufforderung oder Anwerbung durch den Fonds, die KVG, deren verbundene Unternehmen oder einen Placement Agent an die Initiatoren herangetreten ist und Informationen zum Fonds angefragt hat.

Marketing-Disclaimer (PPM):

> Diese Marketing-Mitteilung dient ausschließlich zur Information professioneller und semiprofessioneller Anleger i.S.v. § 1 Abs. 19 Nr. 32, 33 KAGB. Sie stellt kein Angebot und keine Aufforderung zur Zeichnung von Fondsanteilen dar. Maßgeblich sind ausschließlich die Anlagebedingungen, der LPA und das Subscription Agreement.

## Typische Fehler

- "Pre-Marketing" ohne saubere Pre-Marketing-Anzeige nach § 306b KAGB.
- ESG-Aussagen ohne SFDR-Konsistenz.
- Track-Record-Daten ohne Verifizierung.
- Sub-Doc-Versand vor abgeschlossener KYC-Prüfung.

## Querverweise

- pe-004 für KAGB-Scope und Fund Formation.
- pe-005 für Spezial-AIF.
- pe-006 für ELTIF.
- pe-011 für Subscription-Paket.
- pe-018 für ESG/SFDR.
- pe-019 für KYC/GwG.

## Quellen Stand 06/2026

- KAGB §§ 293–311, 312, 316, 320–321, 322–331, 306b (Pre-Marketing).
- AIFMD (RL 2011/61/EU); AIFMD-II (RL (EU) 2024/927, Anwendung ab April 2026).
- MiFID II (RL 2014/65/EU); WpHG §§ 63 ff., 87.
- PRIIPs-VO (EU) 1286/2014.
- SFDR (VO (EU) 2019/2088); ESMA Greenwashing-Bericht (Stand vom Anwender zu prüfen).
- UWG-Greenwashing-Rechtsprechung (BGH ständige Rspr., konkrete Az. vom Anwender zu verifizieren).

## 2. `pe-011-subscription-package-und-side-letter`

**Fokus:** Prüft Beitrittserklärung, KYC, Tax Forms, MFN, Reporting, No-Fault-Divorce, Key-Person und Most-Favoured-Nation.

# Subscription Package und Side Letter

## Fachkern: Subscription Package und Side Letter
- **Spezialgegenstand:** Subscription Package und Side Letter wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill arbeitet das vollständige Subscription-Paket ab: Beitrittserklärung (Subscription Agreement), Anlegerklassifizierungsbogen, KYC-Anhang, FATCA/CRS-Selbstauskunft, AnlV-Bescheinigung bei Versicherern, ESG-Erklärung und Side Letter mit MFN-Logik. Fokus auf LP-Rechte, Gleichbehandlung, Side-Letter-Kollisionen und spätere Durchsetzbarkeit.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche LP-Kategorie zeichnet (institutionell, Family Office, semiprofessionell)?
2. Ticketgröße (entscheidet MFN-Tier)?
3. Welche Side-Letter-Wünsche bringen die LP-Vertreter (MFN, Reporting, ESG, Excuse, Co-Invest, Key Person, No-Fault Divorce)?
4. Anwendbares Recht des LPA und der Anlagebedingungen (DE / LUX / Cayman)?
5. Bestehen existierende Investorengruppen (Anchor LPs) mit Sonderkonditionen?
6. Steuerstatus des LP (Tax-Exempt, Pension Plan, Sovereign Wealth Fund)?
7. Gibt es interne Approval-Hürden des LPs (IC Memo, Beirat, Compliance)?
8. Closing-Termin und KYC-Frist?

## Rechtlicher und transaktionaler Rahmen

KAGB § 67 (Anlagebedingungen), §§ 281 ff. (Spezial-AIF), § 162 KAGB (Berichts- und Informationspflichten); BGB §§ 305 ff. AGB-Recht; GwG §§ 10 ff. (KYC, UBO); FATCA-Abkommen DE-USA und §§ 138 ff. AO; FKAustG (CRS); VAG/AnlV für Versicherer; SFDR Pre-Contractual Disclosure (Art. 6, 8, 9); MFN-Doktrin als ILPA-Standard; § 162 KAGB Reporting-Pflichten; Datenschutz Art. 6, 28 DSGVO.

## / Schritt für Schritt

1. Subscription Agreement Draft mit Anlegerstammdaten, Commitment, Anlegerklassifizierung, FATCA/CRS, AnlV-Erklärung, ESG-Negativliste, Datenschutzhinweis.
2. KYC-Anhang: UBO-Kette, Quellenachweis (Wealth Source, Funds Source), Sanktionserklärung, PEP-Erklärung.
3. Side-Letter-Verhandlung: jeden Wunsch in eine MFN-Kategorie einsortieren (typisch Tier-A >= 100 Mio. EUR, Tier-B 25–100 Mio. EUR, Tier-C < 25 Mio. EUR).
4. MFN-Election-Process nach Final Closing: alle LPs erhalten redaktierte Liste der gewährten Rechte zur Wahl.
5. Conflict-Check: Side-Letter-Rechte mit LPA-Standard und anderen Side Lettern abgleichen.
6. Eskalationspfad bei Disput: Sponsor-Counsel vs. LP-Counsel, ggf. Anchor-LP-Comfort-Letter.
7. Closing-Pack: signiertes Sub-Doc, KYC-Komplett, Side Letter, Capital Call Notice für Initial Funding.

## Trade-off-Matrix

| Strikt standardisiert (kein Side Letter) | Stark individualisierte Side Letter | Tiering mit MFN |
| --- | --- | --- |
| Maximaler Schutz vor Kollision | Maximale LP-Bindung | Beste Praxis |
| Aber: Anchor-LP-Verlust droht | Side-Letter-Hölle bei Final Closing | Klare Erwartungssteuerung |
| Realistisch nur bei Mid-Cap-Fonds | Nur bei Single-Anchor-LP | Marktstandard für Multi-LP-Fonds |

## Praktikertipps Big-Law-PE

- Side Letter mit Sovereign Wealth Funds und Pension Plans enthalten häufig "regulatory carve-outs" — proaktiv in MFN-Modul ausschließen.
- ESG-Negativlisten der LPs sammeln und in einem "Master-Excuse-Schedule" konsolidieren; spart bei jedem Capital Call Zeit.
- Reporting-Side-Letter (zusätzliche ILPA-Templates, individuelle Quartalsberichte) sind häufig der größte Operations-Treiber — Aufwand mit Administrator vorab klären.
- "Key Person Clause" bei Reduzierung der Investment Period (typisch 12 Monate Suspension Period) ist hart verhandelt.
- "No-Fault Divorce" / Removal of GP mit 75–80 Prozent Supermajority ist ILPA-Standard; bei Sponsor-Strukturen Übergangsregeln präzise verhandeln.
- AnlV-Bescheinigung wird häufig erst zum Final Closing nachgereicht — Sub-Doc enthält Erklärung "wird beigebracht bis zum Final Closing".

## Mustertexte / SPA-Klauseln

MFN-Mechanik (Sub-Doc):

> Nach Final Closing erhält jeder Limited Partner eine redaktierte Liste sämtlicher von der KVG mit anderen LPs gewährter Side-Letter-Rechte. Jeder LP kann innerhalb von 30 Bankarbeitstagen die Anwendung beanspruchen, soweit (i) seine Tier-Klassifizierung dies zulässt, (ii) das Recht nicht ausgeschlossen ist (Regulatory Carve-Out, Tax-Specific Provision) und (iii) das Recht nicht ein individueller Vorteil aufgrund spezifischer LP-Anforderungen ist.

Key Person Suspension (LPA):

> Bei Ausscheiden von mehr als 50 Prozent der Key Persons innerhalb eines Zwölfmonatszeitraums tritt automatisch eine Investment Suspension ein. Während der Suspension darf der Fonds keine neuen Investments tätigen. Die Suspension endet (i) durch LPAC-Mehrheitsbeschluss nach Nachbesetzung oder (ii) 12 Monate nach Eintritt, sofern keine Suspension-Aufhebung erfolgt.

## Typische Fehler

- Side-Letter mit Vetorechten gewähren — kippt LPA-Governance.
- MFN ohne Tiering — Kaskade von Nachverhandlungen nach Final Closing.
- KYC-Lücke beim Anchor-LP — Initial Closing rutscht.
- Datenschutzhinweis fehlt — AVV-Lücke gegenüber Administrator.

## Querverweise

- pe-005 für Spezial-AIF-Setup.
- pe-013 für Capital Calls.
- pe-014 für Carry/Waterfall.
- pe-018 für ESG-Reporting.
- pe-019 für KYC/GwG.

## Quellen Stand 06/2026

- KAGB §§ 67, 162, 281 ff.
- GwG §§ 10 ff.; § 138 AO; FKAustG; FATCA-Abkommen DE-USA.
- BGB §§ 305 ff. AGB-Recht; AGG bei Anlegerausschlüssen.
- SFDR (VO (EU) 2019/2088) Pre-Contractual Disclosure.
- ILPA Principles 3.0 (Stand vom Anwender zu prüfen).
- DSGVO Art. 6, 28.

## 3. `pe-012-lp-transfer-und-secondary`

**Fokus:** Begleitet die Übertragung von Fondsanteilen, Zustimmungserfordernisse, KYC-Neuaufnahme und Käufer-DD.

# LP-Transfer und Secondary Interest Sale

## Fachkern: LP-Transfer und Secondary Interest Sale
- **Spezialgegenstand:** LP-Transfer und Secondary Interest Sale wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill prüft, ob ein Secondary schnell closingfähig ist oder an Consent, Tax oder Side-Letter-Rechten hängt. Sekundärmarktverkäufe von LP-Interests sind seit 2020 die schnellstwachsende PE-Subklasse — Buyer (Coller, Ardian, Lexington, HarbourVest) verlangen klare Closing-Mechanik, Seller wollen liquide Exits unter NAV-Discount.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche Fonds-Interests werden veräußert (Vintage, Sponsor, Volumen, Commitment/Unfunded)?
2. Sind die Anteile vinkuliert nach LPA (Standard: 100 Prozent Sponsor-Consent)?
3. Buyer-Identität (Secondaries-Fund, Strategic, Family Office)?
4. Pricing-Struktur: % of NAV, fixed price, deferred consideration, contingent value rights?
5. Welcher Reference Date für NAV-Pricing?
6. Unfunded Commitment: Wer trägt nach Closing das Risiko?
7. Side-Letter-Rechte des Sellers: gehen sie über (mit Sponsor-Consent) oder fallen sie weg?
8. Tax-Setup: Capital Gains beim Seller, Eintritt in laufende Gewinne beim Buyer (§ 18 InvStG)?

## Rechtlicher und transaktionaler Rahmen

LPA-Vinkulierung (regelmäßig § 13 LPA "Transfers"); KAGB-Spezialregeln (§ 281 KAGB i.V.m. § 1 Abs. 19 für semiprofessionelle Anleger); GwG §§ 10 ff. (KYC-Neuaufnahme); InvStG §§ 16, 19, 20 (Anteilsveräußerung); BGB §§ 398 ff. Forderungsabtretung (für Unfunded Commitment) und § 415 BGB Vertragsübernahme bei Zustimmung des Vertragspartners; UmwG bei Verkauf an verbundenes Unternehmen; AnlV bei Versicherern; FATCA/CRS-Re-Documentation; Secondary Purchase Agreement (SPA) ist eigenständiges Vertragswerk mit Reps & Warranties zur Anteilseigenschaft, Funding Status, Side Letter, Tax.

## / Schritt für Schritt

1. LPA-Transfer-Klausel prüfen: Consent-Voraussetzungen, Notice Period (typisch 20–30 BTage), Right-of-First-Refusal des Sponsors?
2. Reference Date und Cut-Off-Mechanik für Pricing definieren: NAV per Last Reported Date plus Cash Flow Adjustments seitdem.
3. Buyer-KYC und Anlegerklassifizierung: erfüllt der Buyer die Anlegerkategorie nach Anlagebedingungen?
4. Tax-Strukturierung: Asset-Deal-Element bei Unfunded Commitment? Stempelsteuer-Schnittstellen (DE: keine; LUX/UK: prüfen)?
5. Side-Letter-Mitübertragung verhandeln; Sponsor entscheidet, häufig kein Transfer der LP-spezifischen Rechte.
6. Closing Mechanics: simultaneous Signing/Closing oder Long-Stop mit Conditions Precedent (Sponsor-Consent, KYC, Funding)?
7. Capital Account Transfer: Original-Cost-Basis übergeht, Buyer übernimmt anteilig Ergebnisse seit Acquisition Date.
8. Post-Closing Side-Letter-Renegotiation mit Sponsor.

## Trade-off-Matrix

| 100 % Anteilskauf | Strip Sale (Teilanteil) | Stapled Secondary |
| --- | --- | --- |
| Komplette Übertragung | Teilausstieg, Seller bleibt LP | Secondary + Primary in Continuation Fund |
| Einfacher | Komplexere LPA-Anpassung | Komplex, aber GP-friendly |
| Standard für Seller-Exit | Liquiditätsoption | Standard bei GP-led Secondaries |

## Praktikertipps Big-Law-PE

- Sponsor-Consent ist regelmäßig "may not be unreasonably withheld" — bei Verweigerung Begründung verlangen; standhafte Consent-Verweigerung ist seltener als gedacht.
- Side Letter mit MFN-Logik gehen häufig nicht über; Buyer muss neuen Side Letter mit Sponsor verhandeln.
- "Old Money" / "New Money" Allocations: Buyer übernimmt unrealisierte Bewertungsdifferenzen seit Reference Date; präzise Mechanik im SPA.
- Reps & Warranties typisch: (i) gute Inhaberschaft, (ii) keine Pfändungen, (iii) Funded/Unfunded Commitment, (iv) keine ungezeichneten Capital Calls, (v) Side-Letter-Vollständigkeit.
- Bei Versicherern (AnlV) wird häufig Capital Gain ausgewiesen — Buyer-Tax-Verifizierung sinnvoll.
- Buy-Side-Due-Diligence-Standard: Coller Capital Secondary DDQ als Marktstandard.

## Mustertexte / SPA-Klauseln

Transfer-Conditions (LPA-Snippet):

> Eine Übertragung von Limited Partner Interests bedarf der vorherigen schriftlichen Zustimmung der KVG. Die Zustimmung darf nur aus wichtigem Grund verweigert werden, insbesondere bei (i) regulatorischen Hindernissen, (ii) KYC-Mängeln, (iii) Konflikt mit der Anlegerstruktur oder (iv) Tax-Adverse-Position für den Fonds.

Apportionment of Distributions / Capital Calls (Secondary SPA):

> Distributions and Capital Calls received or made after the Reference Date and before Closing shall be apportioned: pre-Closing economic ownership remains with Seller, post-Closing with Buyer. Seller shall promptly remit to Buyer any Distributions received post-Closing that relate to the transferred Interest.

## Typische Fehler

- Sponsor-Consent nicht eingeholt — Closing scheitert.
- Unfunded Commitment ohne klare Apportionment — Streit über nächste Capital Call.
- Side-Letter-Erwartungen des Buyers ohne Sponsor-Confirmation — späteres Veto.
- Tax-Stempel oder Substanz-Test in LUX/UK ignoriert.

## Querverweise

- pe-011 für Side Letter und Sub-Doc.
- pe-013 für Capital Calls / Unfunded.
- pe-017 für GP-led Secondaries / Continuation Funds.
- pe-019 für KYC bei Buyer-Onboarding.
- pe-020 für Tax-Schnittstellen.

## Quellen Stand 06/2026

- KAGB §§ 1 Abs. 19, 281 ff.
- BGB §§ 398, 415; AGG; GwG §§ 10 ff.
- InvStG §§ 16, 19, 20.
- AnlV (für Versicherer); FKAustG (CRS); FATCA-Abkommen DE-USA.
- ILPA Secondary Market Guidance (jeweils aktuelle Fassung vom Anwender zu prüfen).
- Coller Capital Global Private Equity Barometer (Stand vom Anwender zu prüfen).

## 4. `pe-013-capital-calls-und-defaulting-lp`

**Fokus:** Prüft Kapitalabrufe, Säumnisfolgen, Verwässerung, Verzugszinsen, Ausschluss und Enforcement gegen Anleger.

# Capital Calls und Defaulting LP

## Fachkern: Capital Calls und Defaulting LP
- **Spezialgegenstand:** Capital Calls und Defaulting LP wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill erzeugt Default Notice, Risikoampel und Kommunikationsplan beim säumigen LP. Capital Calls sind das wirtschaftliche Lebenselixier des Fonds; ein Defaulting LP kann durch Verwässerung, Verzugszinsen, Übernahme durch andere LPs (Topping-Up Right) oder Zwangsverkauf des Interests sanktioniert werden. Der Skill arbeitet die LPA-Mechanik im konkreten Default-Fall ab.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Wer ruft ab (KVG) und an wen (LP), in welcher Höhe und mit welcher Notice Period (typisch 10 Bankarbeitstage)?
2. Hat der LP bereits einen Default oder eine Late Payment Notice erhalten?
3. Liegt ein Defaulting-LP-Tatbestand nach LPA vor (Zahlungsverzug, Insolvenz, Material Breach)?
4. Welche LPA-Remedies stehen offen (Default Interest, Forfeit, Compulsory Sale, Dilution)?
5. Gibt es Topping-Up-Rights anderer LPs oder Sponsor-Übernahme?
6. Steuerliche und regulatorische Konsequenzen (AnlV-Bruch beim Versicherer, ILPA-Reporting)?
7. Verfahrenslage: ist Insolvenz beantragt, läuft Sanktionsthematik, gibt es Asset-Frost?
8. Zielergebnis: Cure, Forfeiture, oder Compulsory Sale an Secondary Buyer?

## Rechtlicher und transaktionaler Rahmen

LPA Capital Call Mechanics (Sec. 5 / 6 typisch); KAGB § 281 ff.; BGB §§ 280, 286 (Verzug), § 315 BGB (Leistungsbestimmung), § 320 BGB (Einrede des nicht erfüllten Vertrags); InsO §§ 80, 91, 130, 131 (Insolvenzanfechtung bei spätem Capital Call); GwG bei Buyer-Onboarding; § 19 GwG (Sanktionsfolgen, Asset-Frost); InvStG zur Behandlung des Sanktionsverlusts; AnlV (Versicherer); CRR/CRD bei Bank-LPs.

## / Schritt für Schritt

1. Capital Call Notice mit allen LPA-Pflichtangaben (Höhe, Verwendungszweck, Termin, Bankverbindung) versenden.
2. Bei verspäteter Zahlung: Late Payment Notice mit Cure Period (typisch 5–10 BTage).
3. Default Notice nach Ablauf der Cure Period; Default Interest (typisch 8 % p.a. oder höher) und Diluition / Forfeiture trigger.
4. Kommunikation mit Defaulting LP: Cure-Plan, Compulsory Sale, Allokationsanpassung.
5. Andere LPs: Topping-Up-Rights und Side-Letter-konforme Informationspflichten.
6. Bei Compulsory Sale: Reference Pricing (typisch NAV minus Discount 50 %), Buyer-Onboarding, KYC, Side-Letter-Ersatz.
7. ILPA-Reporting an LPAC und alle LPs (anonymisiert, falls vertraglich vorgesehen).
8. Dokumentation aller Schritte für spätere Disputes / Audit.

## Trade-off-Matrix

| Soft Cure (Cure Period verlängern) | Hard Default (Forfeiture) | Compulsory Sale |
| --- | --- | --- |
| Verzug ausgleichen, LP bleibt im Fonds | LP verliert Anteil, Verwässerung | Anteil wird zu Discount verkauft |
| Akzeptabel bei einmaligen Liquiditäts-Engpässen | Bei strukturellem Default | Optimal bei systemischem Issue (Sanktion, Insolvenz) |
| Kein Reputationsschaden | Klares Signal | Bringt liquide Mittel ohne LP-Kollateralschaden |

## Praktikertipps Big-Law-PE

- Default Interest ist nicht Schadensersatz, sondern vertraglich vereinbarte Pauschalierung; AGB-Kontrolle (§ 307 BGB) beachten — exzessive Sätze können kippen.
- Forfeiture-Klauseln mit 50 Prozent Discount auf NAV sind ILPA-konform; 100 Prozent Forfeit ohne Restwert oft unwirksam (§ 138 BGB).
- Versicherer-LPs verlieren bei Default häufig die AnlV-Klassifizierung — Auswirkung auf Capital Reserves; vor Default-Erklärung mit Anleger sprechen.
- Sanktionsbedingter Default (Russland-Bezug, OFAC) ist ein eigener Tatbestand — Asset-Frost vs. Verkauf prüfen, Genehmigung des Außenwirtschafts-Ministeriums oder OFAC-Lizenz.
- Insolvenzanfechtung von Capital Calls in der Krise: § 130 InsO (kongruente Deckung) und § 131 InsO (inkongruent) prüfen; bei Krisenkenntnis hohe Rückforderungsrisiken.
- LPAC-Eskalation früh, nicht erst bei Default; LPAC kann Discretion ausüben (z. B. Cure Period verlängern, Forfeiture aussetzen).

## Mustertexte / SPA-Klauseln

Default Notice (Muster):

> Sehr geehrte Damen und Herren, in Bezug auf den Capital Call Nr. [X] vom [Datum] über [Höhe] EUR mit Fälligkeit [Termin] zeigen wir Ihnen den Eintritt des Default-Tatbestands gemäß § [X] LPA an. Die Cure Period gemäß § [Y] LPA endet am [Datum]. Verzugszinsen in Höhe von 8 Prozent p.a. laufen seit Fälligkeit auf. Ohne fristgerechte Heilung treten die Remedies gemäß § [Z] LPA in Kraft, insbesondere Forfeiture von [50] Prozent des Net Asset Value Ihres Interests.

Compulsory Sale Mechanic (LPA):

> Bei Anhalten des Default-Tatbestands nach Ablauf der Cure Period ist die KVG berechtigt, das Interest des Defaulting Limited Partner an einen oder mehrere Dritte oder andere LPs zu einem Preis von 50 Prozent des zuletzt ermittelten Net Asset Value zu verkaufen. Der Erlös abzüglich Kosten und Verzugszinsen wird an den Defaulting LP ausgekehrt.

## Typische Fehler

- Default Notice ohne LPA-formelle Voraussetzungen (Schriftform, Adressat, Cure Period).
- Default Interest zu hoch — AGB-rechtlich angreifbar.
- Sanktionsbedingten Verzug als gewöhnlichen Default behandelt; OFAC-Lizenz fehlt.
- LPAC nicht informiert; Side-Letter-Pflicht zur LPAC-Eskalation verletzt.

## Querverweise

- pe-011 für Sub-Doc / Side Letter.
- pe-012 für LP-Transfer / Compulsory Sale.
- pe-014 für Carry-Auswirkung bei Default.
- pe-019 für Sanktions-Compliance.

## Quellen Stand 06/2026

- KAGB §§ 281 ff.
- BGB §§ 280, 286, 315, 320; § 138 BGB Sittenwidrigkeit; § 307 BGB AGB-Kontrolle.
- InsO §§ 80, 91, 130, 131.
- GwG §§ 10 ff., § 19; EU-Sanktionsverordnungen (EU 833/2014 Russland, EU 269/2014 etc.).
- ILPA Capital Call Templates und Default Mechanics Guidance (Stand vom Anwender zu prüfen).
- AnlV für Versicherer.
