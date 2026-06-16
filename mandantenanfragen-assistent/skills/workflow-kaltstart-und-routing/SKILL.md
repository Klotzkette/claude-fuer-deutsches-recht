---
name: workflow-kaltstart-und-routing
description: "Kaltstart und Routing im Plugin mandantenanfragen-assistent: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill prüft eingehende Mandantenanfragen binnen Minuten auf Eilbedarf, Konflikt, Mandatsfähigkeit und beste Antwortroute. Er ist das Türschloss der Kanzlei und reduziert späteren Korrekturaufwand.

## Erste 4-Minuten-Triage
1. **Eingangsdatum, Frist?** Klagefrist (Kündigungsschutz § 4 KSchG: 3 Wochen), Widerspruch (1 Monat § 70 VwGO / § 84 SGG), Einspruch Mahnbescheid (2 Wochen § 694 ZPO), Strafbefehl (2 Wochen § 410 StPO).
2. **Konfliktcheck (§ 43a Abs. 4 BRAO):** Mandant gegen aktuellen oder früheren Mandanten? Datenbank konsultieren.
3. **Zuständigkeit:** Eigenes Fachgebiet? Sonst Verweisung an Kollegen oder Rechtsanwaltskammer (§ 49 BRAO Hinweispflicht).
4. **Beratungsstufe:** Vorprüfung (kostenlos), Erstberatung (§ 34 RVG: max. 190 EUR netto Verbraucher), Folge-Mandat mit RVG / Honorarvereinbarung (§ 3a RVG schriftlich/Textform).

## Routing-Optionen
- **Eilig + zuständig:** sofort Mandatsannahme in Textform; Vorbestätigung Eingang; parallel inhaltliche Klärung.
- **Eilig + nicht zuständig:** Hinweis und sofortige Verweisung; ggf. interim Notmaßnahme dokumentieren.
- **Nicht eilig + zuständig:** Erstberatungsangebot mit Kostenhinweis (§ 49b Abs. 5 BRAO Pflicht zur Kostenaufklärung).
- **Beratungshilfeberechtigt:** Hinweis auf Beratungshilfeschein des AG (BerHG).

## Anti-Muster
- Mandatsannahme ohne Vergütungsregelung -> Honorarstreit.
- Ad-hoc-Rechtsauskunft per E-Mail ohne Mandatsverhältnis -> Haftungsrisiko (§ 280 BGB i. V. m. Auskunftsvertrag).

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
