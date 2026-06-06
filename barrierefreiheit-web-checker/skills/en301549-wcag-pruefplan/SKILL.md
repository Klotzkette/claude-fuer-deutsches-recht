---
name: en301549-wcag-pruefplan
description: "Erstellt Prüfkatalog nach EN 301 549 und WCAG. Trennt rechtlich harmonisierten Standard von fachlicher WCAG-2.2-Erweiterung, definiert Seitentypen, Stichprobe, A/AA-Kriterien, manuelle Checks und Nachweise. Output: Auditplan im Barrierefreiheit Web Checker: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# EN 301 549 und WCAG-Prüfplan

## Arbeitsbereich

Erstellt Prüfkatalog nach EN 301 549 und WCAG. Trennt rechtlich harmonisierten Standard von fachlicher WCAG-2.2-Erweiterung, definiert Seitentypen, Stichprobe, A/AA-Kriterien, manuelle Checks und Nachweise. Output: Auditplan. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieses Fachmodul macht aus einer Website einen belastbaren Auditplan.

## Auditstruktur

1. Rechtsmaßstab festlegen.
2. Seitentypen bestimmen: Start, Navigation, Suche, Produkt, Checkout, Login, Formular, Konto, PDF, Fehlerseite.
3. Kritische User Journeys auswählen.
4. Automatisierte Checks einplanen.
5. Manuelle Tastatur- und Screenreader-Prüfung einplanen.
6. Ergebnisse nach Schwere, Häufigkeit und Nutzerimpact priorisieren.
7. Nachweise sammeln: Screenshot, URL, DOM-Auszug, Reproduktionsschritt, erwartetes Verhalten.

## Prüftabelle

| Bereich | Prüfung | Methode | Priorität |
| --- | --- | --- | --- |
| Wahrnehmbar | Textalternativen, Kontrast, Zoom | Tool + manuell | hoch |
| Bedienbar | Tastatur, Fokus, Skiplinks | manuell | hoch |
| Verständlich | Labels, Fehlermeldungen, Sprache | manuell | hoch |
| Robust | Semantik, ARIA, Screenreader | manuell + DOM | hoch |
| Dokumente | PDF-Tags, Lesereihenfolge | PDF-Prüfung | mittel/hoch |

## Hinweis

WCAG 2.2 ist fachlich sinnvoll, aber nicht automatisch der harmonisierte Rechtsmaßstab für jede EU-Konstellation. Das Audit kann deshalb zwei Spalten führen: rechtliche Mindestprüfung und empfehlenswerte Zusatzprüfung.

## Rechtsmaßstab präzise
- **EN 301 549 V3.2.1 (03/2021)**: harmonisierte Norm, die WCAG 2.1 Level A/AA inkorporiert (Kapitel 9 für Web, Kapitel 10 für Dokumente, Kapitel 11 für Software).
- **BITV 2.0**: für öffentliche Stellen des Bundes, verweist über § 3 Abs. 2 BITV 2.0 auf EN 301 549.
- **BFSG** (gilt seit 28.06.2025) und **BFSGV**: für Wirtschaftsakteure (B2C-Produkte/Dienstleistungen) — Anhang 1 BFSGV nennt die Anforderungen, harmonisierte Normen erzeugen Konformitätsvermutung (§ 4 BFSG).
- **WAD-Richtlinie 2016/2102**: öffentliche Stellen, in Deutschland über BITV 2.0 / Landesrecht umgesetzt.
- **WCAG 2.2** wurde im Oktober 2023 vom W3C veröffentlicht; eine entsprechende EN-Aktualisierung ist noch nicht im Amtsblatt veröffentlicht. Bis dahin bleibt WCAG 2.1 AA der harmonisierte Standard.

## Audit-Output-Felder
Pro Befund: Erfolgskriterium (z. B. WCAG 2.1 SC 1.4.3 Contrast Minimum AA), EN-301-549-Klausel (z. B. 9.1.4.3), Schwere (kritisch/hoch/mittel/niedrig), Umsetzungsempfehlung, Verantwortlicher, Frist.

## Trade-off
Reine Tool-Audits (Axe, Lighthouse, Wave) decken nur ca. 30-40 % der WCAG-Verstöße ab. Tastatur- und Screenreader-Manualtests bleiben unverzichtbar; nutzungsorientierte Tests mit Betroffenen sind das Gold-Standard.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
