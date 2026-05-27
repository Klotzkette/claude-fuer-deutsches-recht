---
name: mandat-triage-urheber-medienrecht
description: "Urheber- und Medienrechtsmandat schnell einordnen und naechste Schritte bestimmen. §§ 1 2 97 UrhG §§ 22 23 KUG LPG. Pruefraster: Schutzgegenstand Verletzungsart Parteistellung Fristen Verfahrensart. Output: Triage-Memo Route Sofortmassnahmen. Abgrenzung: Triage; Detailarbeit in Spezialist-Skills."
---

# Mandat-Triage Urheber- und Medienrecht

## Triage-Fragen

1. **Sachgebiet?** (Urheberrecht, Filesharing, Foto-Lizenz, Persoenlichkeitsrecht, KUG, Gegendarstellung, VGG/Verwertungsgesellschaft, Plattformhaftung, Rundfunk, KI-Training)
2. **Mandantenrolle?** (Urheber/Schutzsuchender, Werknutzer/Verletzter, Medienhaus/Verlag, Betroffener, Plattformbetreiber, Filesharing-Beschuldigter)
3. **Ist Eilbeduerftigkeit gegeben?** (einstweilige Verfuegung, Berichterstattung in 2 Tagen, Bild im Netz, Abmahnfrist laufend)
4. **Welche Frist laeuft?** (Reaktionsfrist Abmahnung 7-14 Tage; Gegendarstellung 2-3 Monate; einstweilige Verfuegung 4 Wochen Selbstwiderlegung)
5. **Verletzungs-Gegenstand exakt?** (URL, Datum, Screenshot, Werkbezeichnung, Bildtitel)
6. **Wirtschaftliche Situation?** (Rechtsschutzversicherung, Privatperson vs. Gewerbetreibende, Streitwert-Schaetzung)

## Zentrale Normen und Paragrafenkette

- § 97 UrhG — Unterlassung + Schadensersatz (lizenzanalog, Verletzergewinn, konkreter Schaden)
- § 97a UrhG — Abmahnung, Kostenerstattung, Streitwertdeckel Privatpersonen § 97a Abs. 3 UrhG
- §§ 22, 23 KUG — Recht am eigenen Bild (Einwilligung + Ausnahmen)
- §§ 823 Abs. 1, 1004 BGB i.V.m. Art. 2 Abs. 1, 1 Abs. 1 GG — Persoenlichkeitsrecht
- §§ 195, 199 BGB, § 102 UrhG — Verjaehrung 3 Jahre ab Kenntnis
- Art. 6 DSA — Haftungsprivileg Plattform (notice and take down)
- VGG §§ 92 ff. — Schiedsstelle, § 128 VGG — Klage OLG Muenchen

## Zentrale Rechtsprechung

- BGH, Urt. v. 27.07.2017 – I ZR 228/15, GRUR 2017, 1233 Rn. 28 – Loud: Filesharing-Schadensersatz nach Lizenzanalogie; pauschale 200-600 EUR je Musiktitel als Ausgangswert; Erhoehung bei gewerblichem Zweck.
- BGH, Urt. v. 12.11.2009 – I ZR 166/07, GRUR 2010, 616 Rn. 18 – marions-kochbuch.de: Streitwert bei Foto-Urheberrechtsverletzung im Internet richtet sich nach wirtschaftlichem Interesse; 6.000-10.000 EUR je Bild als Orientierungswert.
- BGH, Urt. v. 17.11.2014 – VI ZR 76/14, NJW 2015, 773 Rn. 22 – Verdoppelung Lizenz: Lizenzanalogie bei Bilderrechtsverletzung; MFM-Empfehlungen als Ausgangspunkt; Verdoppelung bei fehlender Urheberbenennung (§ 13 UrhG).
- BGH, Urt. v. 28.07.2015 – VI ZR 340/14, NJW 2015, 3153 Rn. 18 – Suchmaschinenkontroverse: Abwaegung Pressefreiheit (Art. 5 GG) gegen Persoenlichkeitsrecht (Art. 2 Abs. 1, 1 Abs. 1 GG); Unterlassungsanspruch bei schwerwiegender Beeintraechtigung.
- EuGH, Urt. v. 22.06.2021 – C-682/18, GRUR 2021, 1331 Rn. 62 – YouTube/Cyando: Plattformbetreiber ist kein unmittelbarer Taeter fuer Nutzer-Uploads; zuegeloses Nicht-Handeln nach Kenntnis begruendet Haftung; DSA Art. 6 setzt Rspr. fort.

## Kommentarliteratur

- Schricker/Loewenheim, Urheberrecht (Beck) — §§ 97, 97a UrhG
- Dreier/Schulze, UrhG (Beck) — Schadensersatz und Abmahnung
- Wenzel, Das Recht der Wort- und Bildberichterstattung (Beck) — Presserecht und KUG
- Soehring/Hoene, Presserecht (Nomos) — Gegendarstellung und Persoenlichkeitsrecht

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|-----------|-------------|
| Urheber-Abmahnung Verteidigung | `urheber-abmahnung-pruefen` |
| Urheber-Anspruch Aktivseite | `urheber-abmahnung-pruefen` (Aktivlegitimation) |
| Foto-Lizenz Streit | `urheber-abmahnung-pruefen` + MFM-Diskussion |
| Filesharing-Verteidigung | `fachanwalt-urheber-medienrecht-filesharing-verteidigung` |
| KUG / Recht am eigenen Bild | `fachanwalt-urheber-medienrecht-abmahnung-pruefen` |
| Gegendarstellung Presse | `fachanwalt-urheber-medienrecht-gegendarstellung-presse` |
| VGG / Verwertungsgesellschaft | `fachanwalt-urheber-medienrecht-schiedsstelle-dpma-vgg` |
| KI-Training TDM | `fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out` |
| Lizenzvertrag | `fachanwalt-urheber-medienrecht-lizenzvertrag-verhandlung` |
| Software Open-Source-Compliance | `gewerblicher-rechtsschutz/open-source-pruefung` |

## Schritt-fuer-Schritt-Triage-Workflow

```
Schritt 1: Sachgebiet bestimmen (s. Routing-Matrix)

Schritt 2: Frist pruefen
  → Abmahnung: Datum + uebl. 7-14 Tage Reaktionsfrist
  → Gegendarstellung: Datum Veroeffentlichung + LPG-Frist
  → einstweilige Verfuegung: Zustellungsdatum + 14 Tage Widerspruch § 924 ZPO

Schritt 3: Eilcharakter klassifizieren
  → Heute: eV zugestellt, Berichterstattung morgen
  → 48h: Abmahnfrist laeult
  → Diese Woche: regulaere Bearbeitung

Schritt 4: Mandatsannahme-Pruefung
  → Konflikt-Check
  → GwG-Identifizierung
  → Streitwert schaetzen, Honorar vereinbaren

Schritt 5: Routing zum Folge-Skill
```

## Output: Triage-Protokoll

```
TRIAGE-PROTOKOLL — URHEBER-/MEDIENRECHT

Datum:           [TT.MM.JJJJ]
Mandant:         [NAME, ROLLE]
Sachgebiet:      [BESCHREIBUNG]
Verletzungsobjekt:[WERK/BILD/AEUSSERUNG]
Gegner:          [NAME, ADRESSE]
Frist:           [DATUM] — Art: [ABMAHNUNG/EV/GEGENDARSTELLUNG]
Eilcharakter:    [HEUTE / 48H / DIESE WOCHE / KEINE EILE]
Folge-Skill:     [SKILL-NAME]
Streitwert:      ca. [BETRAG] EUR
Naechste Schritte:[MASSNAHME 1] bis [DATUM]
                  [MASSNAHME 2] bis [DATUM]
```

## Eskalation

- **Sofort-Telefon:** einstweilige Verfuegung zugestellt; Berichterstattung in 2 Tagen
- **Binnen 1 Stunde:** Abmahnfrist laeuft heute ab; Schutzschrift-Einreichung noetig
- **Heute:** Gegendarstellungsverlangen verfassen; Reaktion auf Abmahnung
- **Diese Woche:** Lizenzverletzungs-Pruefu ng; Klageschrift-Entwurf

## Cross-Refs

- `erstgespraech-mandatsannahme` — vollstaendige Mandatsannahme
- `vergleichsverhandlung-strategie` — Vergleich nach Abmahnung
- `fachanwalt-urheber-medienrecht-orientierung` — Normen-Uebersicht
