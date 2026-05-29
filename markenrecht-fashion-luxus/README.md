# markenrecht-fashion-luxus

**Version:** 3.2.1  
**Mandantin:** klôtzzkètté SA, Paris/Mailand — Haute-Couture-Label, Geschäftsführerin Comtesse Beatrice de Klotzzkettie  
**US-Tochter:** klôtzzkètté Inc., 712 Fifth Avenue, New York, NY 10019  
**Kanzlei DE:** Steinacker Lichtenberg, München (Boutique-IP-Kanzlei)  
**Kanzlei US:** Whitman Brennan Forsythe LLP, 1290 Avenue of the Americas, New York, NY 10104  
**Fiktive Gegner:** Brezelmann Discount KG (Bad Mergentheim), Donauzon Marketplace GmbH  

---

Markenrecht-Plugin für Luxus-Modehäuser: DPMA, EUIPO Alicante, USPTO (Lanham Act, TTAB), alle Markenarten, Widerspruch, Löschung, Verletzungsdurchsetzung, Produktpiraterie (DE/US), Selektivvertrieb (Coty/Leegin), Plattformrecht (DSA), US Trade Dress und CBP.

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Markenrecht Fashion & Luxus (`markenrecht-fashion-luxus`) | [markenrecht-fashion-luxus.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/markenrecht-fashion-luxus.zip) |

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `markenrecht-fashion-luxus.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte den Markenrecht-Workflow für unsere neue Couture-Linie.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Testakte

- Marken-Streit klôtzzkètté ./. Brezelmann/Donauzon: [testakten/markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon/](../testakten/markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon/) -> [testakte-markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon.zip)

---

## Skills-Übersicht (32 Skills, Blöcke A–F)

### Block A — Anmeldung & Markenarten (10 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 1 | `anmeldung-strategie-portfolio` | Strategie DE/EU/Madrid-Protokoll, Nizza-Klassen, Multi-Class-Portfolio (Kl. 3/14/18/25/35), Prioritätskaskade, Kostenoptimierung | "Markenstrategie", "Portfolio", "Nizza-Klassen", "Madrid-Protokoll" |
| 2 | `wortmarke-anmeldung-dpma` | DPMA-Anmeldung Wortmarke, §§ 32 ff. MarkenG, absolute Schutzhindernisse § 8 MarkenG, Beanstandungsbescheid-Antwort | "Wortmarke", "DPMA-Anmeldung", "Unterscheidungskraft", "Markenprüfung" |
| 3 | `bildmarke-und-wort-bild` | Bildmarke Couture-Logo, Wort-Bild-Marke, Farbansprüche RGB/Pantone, EUIPO Vienna Classification | "Bildmarke", "Wort-Bild-Marke", "Logo-Marke", "Farbanspruch" |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 5 | `soundmarke-und-bewegungsmarke` | Hörmarke MMA-Verfahren, Sonogramm, Notenschrift, MP3-Hinterlegung, Bewegungsmarke | "Höermarke", "Soundmarke", "Jingle schützen", "Bewegungsmarke" |
| 6 | `duftmarke-und-geschmacksmarke` | Riechmarken Sieckmann-Kriterien, faktisch nicht eintragbar, Workarounds: Patente/UWG/GeschGehG | "Duftmarke", "Riechmarke", "Parfum Marke", "Duft schützen" |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| 8 | `positionsmarke` | Positionsmarke roter Sohlenstreifen, Adidas-Drei-Streifen, Bottega-Intrecciato, Burberry-Karo | "Positionsmarke", "Stripe Marke", "Sohlen-Marke", "Muster Marke" |
| 9 | `anti-ki-marke-und-kennzeichen` | Kennzeichenklassen für KI-frei-Garantie, EU AI Act 2024/1689, Human-Made-Label-Strategien | "Anti-KI Marke", "Human-Made Label", "KI-frei Zertifikat", "AI Act" |
| 10 | `haptik-und-tastmarke` | Tastmarken/Haptik-Marken Stoffstruktur/Flakon, Sieckmann-Kriterien analog, DesignG-Workaround, USPTO David Yurman | "Tastmarke", "Haptik-Marke", "Stoff-Struktur-Schutz", "Materialfühlung" |

---

### Block B — EUIPO Alicante & Widerspruch (3 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 11 | `unionsmarken-anmeldung-euipo` | Unionsmarke UMV (EU) 2017/1001, Alicante-Verfahren, e-Filing, Vertretungszwang Art. 119 UMV | "Unionsmarke", "EUIPO Anmeldung", "EU-Marke anmelden", "EUTM" |
| 12 | `euipo-widerspruchsverfahren` | Widerspruch Art. 8 UMV, Verwechslungsgefahr Art. 8 I lit. b, Bekanntheitsschutz Art. 8 V, Beschwerdekammer | "EUIPO Widerspruch", "Opposition EUIPO", "Verwechslungsgefahr EU", "BoA" |
| 13 | `dpma-widerspruch-und-loeschung` | DPMA-Widerspruch §§ 42 ff. MarkenG, Verfall § 49, Nichtigkeit § 50, BPatG-Beschwerde § 66 MarkenG | "DPMA Widerspruch", "Marke löschen", "Verfall Marke", "BPatG Beschwerde" |

---

### Block C — Verletzung & Durchsetzung (4 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 14 | `messe-verletzung-und-gv-einsatz` | Verletzende Ware auf Messen, Eilantrag §§ 935/940 ZPO, einstweilige Verfügung, GV-Sicherstellung, § 19 MarkenG | "Messe Verletzung", "GV Sicherstellung", "einstweilige Verfügung Marke" |
| 15 | `abmahnung-markenrecht-uwg` | Abmahnung mit strafbewehrter Unterlassungserklärung, Hamburger Brauch Vertragsstrafe, § 14 MarkenG | "Abmahnung Marke", "Unterlassungserklärung", "Vertragsstrafe Marke" |
| 16 | `produktpiraterie-und-zoll` | Anti-Counterfeiting, Grenzbeschlagnahme VO (EU) 608/2013, Zoll-AWA-Antrag, Vernichtung | "Produktpiraterie", "Zollbeschlagnahme", "AWA-Antrag", "Grenzbeschlagnahme" |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

---

### Block D — Selektiver Vertrieb & Wettbewerb (4 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 19 | `vertikale-preisbindung-vbe-vo` | Vertikal-GVO (EU) 2022/720, Hardcore-Beschränkungen Art. 4, UPE vs. Mindestpreis, Dual Pricing | "Preisbindung", "Vertikal-GVO", "Mindestpreis Händler", "UPE Empfehlung" |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| 21 | `agb-haendlervertrag-luxus` | AGB im Selektivvertrieb §§ 305 ff. BGB im B2B, BGH-Klauselverbote, MFN-Klauseln nach Coty II | "AGB Händler", "Händlervertrag Luxus", "MFN-Klausel", "AGB-Kontrolle B2B" |

---

### Block E — Kanzlei-Werkzeuge (2 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 22 | `fashion-luxus-kaltstart-interview` | Mandantenaufnahme Modehaus, IP-Audit-Fragenkatalog, Portfolio-Inventur, Prioritäten-Matrix | "IP-Audit", "Mandantenaufnahme", "Kaltstart", "Markenportfolio prüfen" |
| 23 | `markenmonitoring-und-watchlist` | DPMA-/EUIPO-/WIPO-Watch, Madrid-Monitor, Frühwarnung bei Trittbrettfahrer-Anmeldungen | "Markenmonitoring", "Watchlist Marke", "EUIPO Watch", "WIPO-Alert" |

---

### Block F — USPTO & Lanham Act / US-Markenrecht (8 Skills)

*Koordination: Whitman Brennan Forsythe LLP, 1290 Avenue of the Americas, New York, NY 10104.*  
*Partner J. Halston Whitman III, Esq. (USD 1.450/h); Senior Associate Eleanor M. Quintero, Esq. (USD 695/h).*

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 24 | `uspto-anmeldung-und-lanham-act` | USPTO-Anmeldung Lanham Act 15 U.S.C. § 1051 ff., Use in Commerce vs. Intent-to-Use, TEAS Plus/Standard, Specimen of Use, Extension Requests | "USPTO Anmeldung", "US Marke anmelden", "TEAS Plus", "Intent to Use" |
| 25 | `uspto-office-actions-und-tess-tsdr` | Office Actions vom Examining Attorney: Section 2(d) DuPont Factors (In re E.I. DuPont 476 F.2d 1357), Merely Descriptive, Surname Refusal. TESS und TSDR Recherche | "USPTO Office Action", "Section 2(d) refusal", "DuPont factors" |
| 26 | `madrid-protokoll-und-internationale-registrierung` | Madrid-Protokoll WIPO, Subsequent Designations US/JP/CN/GB, Section 66(a), Central Attack 5 Jahre, Transformation, Madrid-Monitor | "Madrid-Protokoll", "IR-Marke", "internationale Registrierung", "Subsequent Designation" |
| 27 | `ttab-opposition-und-cancellation` | TTAB: Opposition 37 C.F.R. § 2.101 ff., Cancellation § 2.111 ff., Dilution 15 U.S.C. § 1125(c), Fraud In re Bose 580 F.3d 1240, Federal Circuit Appeal | "TTAB Opposition", "Cancellation Petition", "Notice of Opposition US" |
| 28 | `us-trade-dress-und-secondary-meaning` | Trade Dress § 43(a) 15 U.S.C. § 1125(a), Product Configuration (Wal-Mart 529 U.S. 205), Product Packaging (Two Pesos 505 U.S. 763), Functionality TrafFix 532 U.S. 23 | "Trade Dress US", "Secondary Meaning", "Product Configuration", "Flakon Trade Dress" |
| 29 | `us-counterfeit-und-customs-cbp` | Trademark Counterfeiting Act 18 U.S.C. § 2320, CBP Recordation 19 C.F.R. § 133, § 34 Injunctive Relief, § 35 Treble Damages, Octane Fitness 572 U.S. 545 | "US Counterfeit", "CBP Recordation", "Lanham Act enforcement" |
| 30 | `us-selektivvertrieb-und-mfp-tiffany-vs-costco` | RPM nach Leegin 551 U.S. 877 (Rule of Reason), MAP-Policies, Unilateral Colgate Doctrine, Tiffany v. Costco 971 F.3d 74 | "US Resale Price Maintenance", "MAP Policy", "Tiffany Costco", "Leegin" |
| 31 | `nyc-korrespondenz-und-conflict-check` | Mandats-Workflow mit Whitman Brennan Forsythe LLP: Engagement Letter, Conflict Check, POA USPTO, Outside Counsel Guidelines, Common Interest Privilege | "US-Korrespondenzkanzlei", "NYC Trademark Counsel", "USPTO Power of Attorney" |

---

## Persona

**Rolle:** Partnerin, Boutique-IP-Kanzlei Steinacker Lichtenberg (im Stil von Hogan Lovells IP, Bird & Bird Fashion Practice, Boehmert & Boehmert)  
**Mandantin:** klôtzzkètté SA (Haute-Couture-Label, Paris/Mailand) — fiktive italo-französische Maison  
**Geschäftsführerin:** Comtesse Beatrice de Klotzzkettie  
**Ton:** präzise, abgeklärt, mit einem Hauch Pariser Hauteur und Münchener IP-Härte  
**Sprache:** Deutsch (Anwaltsstil); US-Korrespondenz mit Whitman Brennan Forsythe LLP auf Englisch  

---

## Wichtige Normen-Übersicht

| Norm | Inhalt |
|---|---|
| §§ 3/4/8/9 MarkenG | Markenfähigkeit, Entstehung, Schutzhindernisse, relative Hindernisse |
| §§ 14/18/19 MarkenG | Verletzung, Vernichtung, Auskunft |
| §§ 42/49/50 MarkenG | Widerspruch, Verfall, Nichtigkeit |
| UMV (EU) 2017/1001 | Unionsmarkenrecht (Art. 4/7/8/15/46/47/67-73) |
| VO (EU) 608/2013 | Zoll-Anti-Counterfeiting |
| DSA VO (EU) 2022/2065 | Digital Services Act — Notice-and-Action |
| Vertikal-GVO (EU) 2022/720 | Selektivvertrieb, Preisbindung |
| EU AI Act 2024/1689 | KI-Transparenz, Human-Made-Labels |
| 15 U.S.C. §§ 1051-1141 | Lanham Act (US Trademark Law) |
| 18 U.S.C. § 2320 | US Trademark Counterfeiting (Strafrecht) |
| 19 C.F.R. § 133 | CBP Recordation (US Zoll) |

---

*Plugin erstellt für die Kanzlei Steinacker Lichtenberg — alle Personen, Firmennamen und Aktenzeichen außerhalb von echten Gerichtsentscheidungen sind fiktiv.*
