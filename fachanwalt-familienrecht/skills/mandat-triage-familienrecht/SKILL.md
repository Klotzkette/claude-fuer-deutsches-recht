---
name: mandat-triage-familienrecht
description: "Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich. Normen: § 63 FamFG (Beschwerde 1 Monat), § 1600b BGB (Vaterschaftsanfechtung 2 Jahre), § 1666 BGB (Kindeswohlgefaehrdung Eilantrag). Prüfraster: Konflikt-Check, Eilbedürftigkeit (Gewaltschutz, Sorge-Eilantrag), Streitwert, Komplexitaet. Output Triage-Protokoll, Fristen-Ampel, Folge-Skill-Empfehlung. Abgrenzung: Detailberechnung siehe Spezialskills; Schriftsatzkern siehe schriftsatzkern-substantiierung."
---

# Mandat-Triage Familienrecht

## Aktuelle Rechtsprechung (Triage-Orientierung, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH 22.01.2025 - XII ZB 148/24 (Elternunterhalt, Selbstbehalt; Familienselbstbehalt)
- BVerfG 07.10.2025 - 1 BvR 746/23 (Umgangsausschluss: Begründungsanforderungen bei längerer Dauer)
- BVerfG 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS-Maßstäbe)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026)

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org oder openjur.de mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Strukturierte Eingangsabfrage beim Erstkontakt — verhindert falsche Spur, identifiziert Eilbedarf, ordnet das Mandat dem richtigen Folge-Skill zu.

## Ablauf — sieben Fragen in fester Reihenfolge

### Frage 1 — Wer ruft an und für wen?

- Selbst Betroffener
- Eltern eines Kindes
- Anderer Anwalt (Verweisungsmandat)
- Gericht (Verfahrensbeistand)

**Routing:** Bei Verweisungsmandat sofort an aufnehmenden Anwalt. Bei Verfahrensbeistand separater Vermerk.

### Frage 2 — Akute Eilbedürftigkeit?

- Häusliche Gewalt — Schutzanordnung gewünscht
- Kindeswohl unmittelbar gefährdet
- Kind drohend ins Ausland verbracht (HKÜ-Fall)
- Wegweisung dringend
- Sorgerecht-Eilbedürftigkeit

**Eskalation:** Bei JA — Telefon-Sofort an Anwalt; binnen ein Stunde Eilantrag-Vorbereitung. Skill `mandat-triage-familienrecht` wechselt sofort in Eilmodus.

### Frage 3 — Hauptanliegen?

- Scheidung
- Sorgerecht
- Umgangsrecht
- Kindesunterhalt
- Ehegattenunterhalt
- Zugewinnausgleich
- Versorgungsausgleich
- Vaterschaft (Anerkennung Anfechtung)
- Ehevertrag Scheidungsfolgenvereinbarung
- Adoption
- Betreuung Vorsorgevollmacht

### Frage 4 — Stand des Verfahrens?

- Außergerichtlich keine Anzeige
- Schreiben des Gegners liegt vor
- Gerichtliches Verfahren läuft (Aktenzeichen Gericht)
- Erstinstanz abgeschlossen — Beschwerde erwogen

### Frage 5 — Familienstatus?

- Verheiratet
- Getrennt lebend (Datum der Trennung)
- Geschieden
- Lebenspartnerschaft
- Nichtehelich

### Frage 6 — Wirtschaftliche Verhältnisse?

- Nettoeinkommen beide Eheleute geschätzt
- Vermögen geschätzt (Immobilie Sparvermögen Unternehmensbeteiligungen)
- Streitwert-Schätzung

**Routing PKH:** Bei knappem Einkommen Hinweis auf Prozesskostenhilfe-Antrag. Skill `prozesskostenhilfe-antrag` aus sozialrecht-kanzlei (sofern verfügbar) oder eigener Entwurf.

### Frage 7 — Fristen?

- Letztes Anwaltsschreiben oder Beschluss empfangen am ?
- Beschwerdefrist § 63 FamFG ein Monat
- Vaterschaftsanfechtung § 1600b BGB zwei Jahre ab Kenntnis

## Routing-Matrix

| Hauptanliegen | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| Scheidung | (Skill scheidungsverbund-vorbereiten — perspektivisch) | Versorgungsausgleichs-Auskunft anfordern |
| Kindesunterhalt | `unterhalt-duesseldorfer-tabelle` | Verzug § 1613 BGB durch Auskunftsschreiben |
| Ehegattenunterhalt | `unterhalt-duesseldorfer-tabelle` | Verzug § 1613 BGB |
| Sorge / Umgang | (Skill kindeswohl-prüfung — perspektivisch) | Eilantrag prüfen |
| Zugewinn | (Skill zugewinnausgleich-berechnen — perspektivisch) | Stichtag Zustellung Scheidungsantrag |
| Versorgungsausgleich | (Skill versorgungsausgleich — perspektivisch) | Auskunft DRV / Versorgungsträger |
| Vaterschaft | (Skill vaterschafts-verfahren — perspektivisch) | § 1600b BGB Zwei-Jahres-Frist |
| Gewaltschutz | EILMODUS — Antrag GewSchG Skill `mandat-triage-familienrecht` wechselt | sofort |

## Mandatsannahme-Kriterien

- **Konflikt-Check** — keine Beratung des Gegners im selben Sachverhalt (§ 43a Abs. 4 BRAO)
- **Streitwert** über EUR 30000 OLG Familiensenat erste Instanz bei Verbund
- **Komplexität** bei Auslandsbezug Selbstständigen-Einkommen Unternehmens-Beteiligungen Gesellschafter-Streit

## Sofort-Fristen-Check

- Empfangsdatum letzter Beschluss notieren
- Bei Beschluss eingegangen heute: Beschwerdefrist nach FamFG (§§ 63, 64 FamFG i.V.m. ZPO) — Zugang nach Vier-Tages-Fiktion (§ 270 ZPO n.F., seit 1.1.2025 PostModG; bis 31.12.2024 drei Tage), danach Lauf der Beschwerdefrist von einem Monat (§ 63 FamFG)
- Eintrag in `fristenbuch.yaml` (Skill `kanzlei-allgemein`)

## Eskalationspfad

- **Telefon-Sofort** Gewaltschutz Kindeswohlgefährdung HKÜ-Verbringung
- **Binnen einer Stunde** Eilantrag-Sorgerecht Wegweisung
- **Heute** Versorgungsausgleichs-Auskunft Verzug-Schreiben
- **Diese Woche** Schriftsatz-Erstentwurf Verbund-Antrag

## Ausgabe

- `triage-protokoll-familienrecht.md` strukturiert nach den sieben Fragen
- Aktenanlage mit Az-Vorschlag
- Frist-Eintrag im Fristenbuch
- Empfehlung Folge-Skill plus zwei Sätze Begründung
- Mandantenbrief-Entwurf mit Sachstand und nächsten Schritten

## Quellen

- §§ 111 ff. FamFG (Familiensachen)
- BGH XII. Zivilsenat
- Wendl/Dose
- Schwab Familienrecht
