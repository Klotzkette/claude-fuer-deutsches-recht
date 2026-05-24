---
name: mandat-triage-familienrecht
description: Strukturierte Eingangs-Abfrage fuer familienrechtliche Mandate. Routet anhand von fuenf bis sieben Fragen zum richtigen Folge-Skill (Scheidungsverbund Sorgerecht Umgang Kindesunterhalt Ehegattenunterhalt Zugewinn Versorgungsausgleich Gewaltschutz). Prueft Konflikt-Check Eilbeduerftigkeit (Gewaltschutz Sorge-Eilantrag) Streitwert und Komplexitaet. Sofort-Fristen-Check (Beschwerde § 63 FamFG ein Monat / Vaterschaftsanfechtung § 1600b BGB zwei Jahre). Eskalation Telefon-Sofort bei Gewaltschutz Kindeswohl-Gefaehrdung. Ausgabe Triage-Protokoll plus Empfehlung des Folge-Skills.
---

# Mandat-Triage Familienrecht

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
- Bei Beschluss eingegangen heute: Beschwerdefrist endet in vier Wochen Plus drei-Tage-Fiktion
- Eintrag in `fristenbuch.yaml` (Skill `kanzlei-cowork`)

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
