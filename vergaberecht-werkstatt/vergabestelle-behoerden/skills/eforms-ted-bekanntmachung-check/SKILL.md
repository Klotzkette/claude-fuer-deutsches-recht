---
name: eforms-ted-bekanntmachung-check
description: "eForms- und TED-Bekanntmachungen auf Auftraggeberseite prüfen: validiert Datensatz, CPV, Lose, Eignung, Zuschlag, Fristen, Unterlagenlink und Rechtsbehelf und liefert ein versionsfestes Sende-, Berichtigungs- oder Uploadpaket."
---

# eForms- und TED-Bekanntmachung prüfen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Datensatz-Gate

1. Bekanntmachungsart und Rechtsregime bestimmen. § 10a VgV verlangt den jeweils geltenden eForms-Datenaustauschstandard; § 37 Abs. 2 VgV ordnet für die Auftragsbekanntmachung die einschlägige eForms-Spalte zu.
2. Verfahren, Auftraggeber-ID, Beschafferprofil, Rechtsgrundlage, Sprache, CPV, Leistungsort, Laufzeit, Optionen, Lose, geschätzter Wert und EU-Mittel mit den Vergabeunterlagen abgleichen.
3. Eignung, Ausschluss, Zuschlagskriterien, Gewichtung oder zulässige Rangfolge, Nebenangebote, Varianten und geforderte Sicherheiten auf vollständige Bekanntgabe prüfen.
4. Fristen mit Veröffentlichungstag, Mindestfristen und gewählten Verkürzungen neu berechnen; Datum und Uhrzeit einschließlich Zeitzone kontrollieren.
5. Direkten, unentgeltlichen, vollständigen und uneingeschränkten Unterlagenzugang nach § 41 VgV testen. Nicht nur den Portalstart, sondern Zielpfad, Berechtigungen und Dateidownload prüfen.
6. Zuständige Vergabekammer nach § 37 Abs. 3 VgV sowie Rügehinweise und Kontaktdaten kontrollieren.

## Versand und Veröffentlichung

Den gesendeten eForms-Datensatz, Portalvorschau, Übermittlungsquittung und TED-Bestätigung gemeinsam archivieren. Nach § 40 Abs. 1 VgV muss der maßgebliche Übermittlungstag nachweisbar sein; ein angegebener späterer Veröffentlichungstag steuert die Fristberechnung. Nationale Veröffentlichung erst unter den Voraussetzungen des § 40 Abs. 3 VgV und ohne zusätzliche oder abweichende Angaben.

## Berichtigungsweiche

- rein redaktioneller Fehler ohne Einfluss: korrigieren und dokumentieren;
- kalkulations-, teilnahme- oder wertungsrelevante Änderung: Berichtigungsbekanntmachung, neue Unterlagenversion und angemessene Fristverlängerung prüfen;
- Änderung des Beschaffungsgegenstands oder der Wettbewerbsgrundlage: Aufhebung und Neubekanntmachung erwägen;
- bereits versandter, aber nicht veröffentlichter Datensatz: Status beim Datenservice sichern, keine parallelen widersprüchlichen Fassungen erzeugen.

## Pflichtoutput

1. Feldmatrix `eForms-Wert | Unterlagenfundstelle | Abweichung | Rechtsfolge`.
2. Fristen- und Veröffentlichungsprotokoll.
3. Link- und Downloadtest mit Zeitstempel.
4. Freigabefähiger Datensatz oder konkrete Berichtigungsliste.
5. Uploadmanifest mit Dateiname, Version, Hashwert, Zielsystem, Verantwortlichem und Rückbestätigung.
