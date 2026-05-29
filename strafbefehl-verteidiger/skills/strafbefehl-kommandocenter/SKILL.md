---
name: strafbefehl-kommandocenter
description: "Einstieg in das Strafbefehl-Mandat — Ampel-Schnelldiagnose zeigt kritische Fristen und offene Handlungsfelder auf einen Blick. Zentrales Steuerungsmodul routet auf Subskills: Frist § 410 StPO Akteneinsicht § 147 StPO Inhaltsprüfung § 409 StPO Beweis Einlassung Verständigung Einstellung Tagessaetze Nebenfolgen Pflichtverteidiger Wiedereinsetzung. Normen §§ 407-412 StPO. Output Mandats-Ampelstatus mit priorisierten naechsten Schritten. Abgrenzung: strafbefehl-fristen-einspruch für die isolierte Fristprüfung."
---

# Strafbefehl-Verteidiger — Kommandocenter

## Zweck

Dieses Kommandocenter ist der Einstiegspunkt fuer alle Mandate im Strafbefehlsverfahren. Es erfasst den Mandats-Kontext, bewertet die Dringlichkeit und routet zur richtigen Subskill-Anleitung.

## Sofort-Triage bei Mandatsaufnahme

**Die drei kritischen Fragen zuerst:**

1. **Fristlage:** Wann wurde der Strafbefehl zugestellt? Einspruchsfrist § 410 Abs. 1 StPO: 2 Wochen ab Zustellung. Ist die Frist noch offen oder abgelaufen?
   - Frist offen → Einspruch sofort einlegen, dann vertiefen
   - Frist abgelaufen → Wiedereinsetzung § 44 StPO pruefen

2. **Delikt und Sanktion:** Was wird vorgeworfen (§§ StGB/StVG/OWiG)? Welche Rechtsfolge ist angesetzt (Tagessaetze, Geldstrafe, Fahrverbot, Bewaehrungsstrafe)?

3. **Mandantenziel:** Freispruch / Einstellung / Strafmassreduzierung / Fahrverbots-Vermeidung?

## Ampel-Schnelldiagnose

| Situation | Ampel | Massnahme |
|-----------|-------|-----------|
| Frist laeuft in < 3 Tagen | ROT | Einspruch SOFORT, dann vertiefen |
| Frist laeuft in 4-7 Tagen | GELB | Einspruch und Akteneinsicht parallel |
| Frist > 7 Tage | GRUEN | Strukturierte Bearbeitung |
| Frist abgelaufen, keine Wiedereinsetzungsgruende | ROT | Strafbefehl rechtskraeftig |
| Frist abgelaufen, Grund fuer Wiedereinsetzung | GELB | Wiedereinsetzungsantrag § 44 StPO |

## Routing-Matrix

| Aufgabe | Subskill |
|---------|---------|
| Einspruchsfrist berechnen + einlegen | `strafbefehl-fristen-einspruch` |
| Strafbefehl-Inhalt auf § 409 pruefen | `strafbefehl-inhalt-409-pruefung` |
| Akteneinsicht anfordern | `strafbefehl-akteneinsicht-147` |
| Beweis- und Einlassungsstrategie | `strafbefehl-beweis-und-einlassung` |
| Beschraenkter Einspruch | `strafbefehl-einspruch-beschraenkung` |
| Verstaendigung / § 153a | `strafbefehl-deal-verstaendigung` |
| Einstellung § 153 / § 153a / § 170 | `strafbefehl-einstellung-153-153a-170` |
| Tagessatz-Berrechnung | `strafbefehl-tagessaetze-geldstrafe` |
| Nebenfolgen Fahrerlaubnis | `strafbefehl-nebenfolgen-fahrerlaubnis` |
| Pflichtverteidiger-Bestellung | `strafbefehl-pflichtverteidiger` |
| Wiedereinsetzung nach Fristversaeumnis | `strafbefehl-wiedereinsetzung` |
| Hauptverhandlung vorbereiten | `strafbefehl-hauptverhandlung-vorbereitung` |
| Abwesenheit in der HV | `strafbefehl-abwesenheit-vertretung` |
| Rechtsmittel nach Urteil | `strafbefehl-rechtsmittel-nach-urteil` |
| Zeugen befragen | `strafbefehl-zeugen-befragungsstrategie` |
| Rechtsprechungsrecherche | `strafbefehl-rechtsprechungsrecherche` |
| Quality Gate | `strafbefehl-quality-gate` |
| Aktenanlage | `strafbefehl-aktenanlage` |

## Zentrale Normen im Strafbefehlsverfahren

- **§ 407 StPO** — Zulassungsvoraussetzungen
- **§ 408 StPO** — Richterliche Entscheidung
- **§ 409 StPO** — Pflichtinhalt
- **§ 410 StPO** — Einspruch, 2-Wochen-Frist, Beschraenkung
- **§ 411 StPO** — Hauptverhandlung nach Einspruch
- **§ 412 StPO** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 44 StPO** — Wiedereinsetzung

## Aktuelle Querschnitts-Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Harte Leitplanken

- Frist immer zuerst — kein Schritt ohne Fristensicherung.
- Vollmacht vor Akteneinsicht.
- Keine Einlassung ohne Aktenkenntnis.
- Anwaltliche Endkontrolle bei allen Fristen, Antraegen und Einlassungen.
