---
name: plan-integrierte-kommandocenter
description: "Integrierte Planrechnung aus GuV, Liquidität und Bilanz für Insolvenzplan, StaRUG oder Sanierungskonzept erstellen. §§ 220 229 InsO Finanzplanung § 14 StaRUG. Prüfraster: Ist-Zahlen, Planannahmen, Maßnahmenwirkung, Base Case, Downside, Stressszenarien, Working Capital, Steuer-/Zinseffekte, Brückenrechnung und Annahmenregister. Output: Planungsmodell, Szenariovergleich, Maßnahmen-Brücke, Lückenliste. Abgrenzung: nicht für Vergleichsrechnung (iv-plan-vergleichsrechnung) oder Konzepttext im Insolvenzverwaltung."
---

# Integrierte Planrechnung für Plan und Sanierungskonzept

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Integrierte Planrechnung für Plan und Sanierungskonzept` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Ist-Zahlen importieren und auf Stichtage normalisieren.
2. Planannahmen für Umsatz, Rohertrag, Personal, Fixkosten, Working Capital, Investitionen und Finanzierung erfassen.
3. Maßnahmen mit GuV-, Bilanz- und Liquiditätseffekt einzeln modellieren.
4. Base Case, Plan Case, Fortführung ohne Plan, Liquidation und Stress Case anlegen.
5. Bilanzielle und liquiditätsseitige Brücken erklären, statt nur Tabellen zu liefern.
6. Planversion, Datenstand, Annahmen und Belege dokumentieren.

## Ausgabe

- Planungsmodell als CSV-Struktur
- Annahmenregister
- Szenariovergleich
- Sensitivitätenliste
- Maßnahmen-Brücke
- Plausibilitäts- und Lückenliste

## Mindestmodell

| Ebene | Muss enthalten | Prüffrage |
|---|---|---|
| GuV | Umsatz, Rohertrag, Personal, sonstige Kosten, Zinsen, Steuern, Ergebnis | Erklärt das Modell, wie das Unternehmen wieder Ergebnis erwirtschaftet? |
| Bilanz | Anlagevermögen, Working Capital, Rückstellungen, Finanzschulden, Eigenkapital, Liquidität | Schließt die Bilanz rechnerisch und zeigt sie die Kapitalstruktur nach Sanierung? |
| Liquidität | Anfangsbestand, Einzahlungen, Auszahlungen, Linien, Tilgung, Mindestliquidität | Bleibt Zahlungsfähigkeit im Plan- und Downside-Fall erhalten? |
| Maßnahmen | Kosten, Wirkung, Timing, Status, Verantwortlicher, Nachweis | Ist jede Planveränderung auf eine reale Maßnahme oder belegte Annahme zurückgeführt? |

Für akute Krisen muss die Liquidität kurzfristig engmaschig sein. Für das laufende und folgende Planjahr ist regelmäßig eine monatliche Darstellung sinnvoll. Spätere Planjahre können zusammengefasst werden, wenn die rechnerischen Brücken transparent bleiben.

## Maßnahmen-Brücke

Jede Maßnahme erhält einen eigenen Datensatz:

- **Auslöser/Krisenursache:** Welche Ursache wird behoben oder entschärft?
- **GuV-Effekt:** Umsatz, Marge, Kosten, Abschreibung, Zins, Steuer.
- **Liquiditätseffekt:** Einmalzahlung, laufender Effekt, Vorfinanzierungsbedarf, Fälligkeit.
- **Bilanz-Effekt:** Forderungen, Vorräte, Verbindlichkeiten, Eigenkapital, Rückstellungen.
- **Status:** verbindlich, verhandelt, plausibel, ungeklärt, nicht tragfähig.
- **Nachweis:** Vertrag, Beschluss, Bankzusage, Bestellung, Kündigung, Kalkulation, Kontoauszug.

Keine Maßnahme doppelt zählen. Wenn eine Maßnahme in der GuV ergebniswirksam ist, muss der daraus folgende Cash- und Bilanz-Effekt konsistent abgeleitet werden.

## Sensitivitäten

Mindestens prüfen:

- Forderungseinzug später oder nur teilweise.
- Umsatz oder Auftragseingang niedriger als geplant.
- Rohmarge sinkt.
- Personal- oder Energiekosten steigen.
- Maßnahmen starten später oder wirken nur teilweise.
- Finanzierung wird nur unter zusätzlichen Bedingungen verlängert.
- Steuer-/SV-Rückstände werden nicht wie geplant gestundet.

Ergebnis immer als `trägt`, `trägt nur bei Nachweis`, `trägt nicht` ausgeben.

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.
- Liquiditätsplan, GuV und Planbilanz müssen rechnerisch geschlossen sein.
- Working-Capital-Effekte müssen erläutert werden; Wachstum ohne Liquiditätsbindung ist verdächtig.
- Steuer-, Zins- und Sozialversicherungseffekte dürfen nicht als Restgröße verschwinden.
- Kleinere Unternehmen dürfen schlanker geplant werden, aber nicht ohne Ergebnis-/Bilanz-/Liquiditätsverknüpfung.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.

## IV-Einordnung

Diese integrierte Fassung ist für Insolvenzverwalter, Sachwalter und vorläufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfähigkeit gegenüber Gericht und Gläubigerausschuss, Rollenreinheit, Dokumentation von Belegen und spätere Planvollzugsfähigkeit.

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (IV-Insolvenzplan)

§ 217 InsO (Plan-Option) → § 218 InsO (Vorlage durch IV) → §§ 220-221 InsO (Plan-Inhalte) → § 222 InsO (Gruppenbildung) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Bestaetigung) → § 254 InsO (Wirkung) → §§ 49-51 InsO (Absonderungsrechte in Plan)

## Triage — IV-Plan

Bevor losgelegt wird, klaere:
1. **Plan sinnvoller als Liquidation?** Vergleichsrechnung: Plan-Quote vs. Liquidationsquote.
2. **Gruppenbildung konsistent?** § 222 InsO: gesicherte, nicht gesicherte, Kleinglaeubieger, Arbeitnehmer.
3. **Mehrheiten realistisch?** Simulation Kopf- + Summenmehrheit je Gruppe.
4. **Cramdown-Szenario?** § 245 InsO: ablehnende Gruppe ueberstimmbar wenn Best-Interest-Test bestanden.

## IV-Einordnung

Diese integrierte Fassung ist für Insolvenzverwalter, Sachwalter und voraeufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfaehigkeit gegenueber Gericht und Glaeubigerausschuss sowie Planvollzugsfaehigkeit.

