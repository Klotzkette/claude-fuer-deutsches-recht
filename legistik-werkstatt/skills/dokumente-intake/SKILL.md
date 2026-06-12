---
name: dokumente-intake
description: "Dokumentenintake für Legistik-Werkstatt (Gesetzgebung): sortiert Referentenentwurf, Kabinettvorlage, BR-Drucksache, prüft Datum, Absender, Frist und Beweiswert (Folgenabschätzung, Stellungnahmen Verbände); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Legistik Werkstatt** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Legistik Werkstatt** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aa-ausfuhrkontrolle` — AA Ausfuhrkontrolle
- `aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension` — AA Ausfuhrkontrolle und Aussenwirtschaftsdimension
- `aa-eu-bmi-verwaltungsverfahren` — AA EU BMI Verwaltungsverfahren
- `aa-eu-grundlagen-und-ratsverfahren` — AA EU Grundlagen und Ratsverfahren
- `aa-konsular-bmas-arbeitsrecht` — AA Konsular Bmas Arbeitsrecht
- `aa-konsular-und-passrecht` — AA Konsular und Passrecht
- `aa-sanktionsumsetzung-internationale` — AA Sanktionsumsetzung Internationale
- `aa-sanktionsumsetzung-und-internationale-abkommen` — AA Sanktionsumsetzung und Internationale Abkommen
- `aa-voelkerrecht-und-vertragsgesetzgebung` — AA Voelkerrecht und Vertragsgesetzgebung
- `aenderungs-formular-portal-einreichungslogik` — Änderungs Formular Portal Einreichungslogik
- `aenderungs-formular-portal-und-einreichung` — Änderungs Formular Portal und Einreichung
- `baut-quellenkarte` — Baut Quellenkarte
- `begruendung-allgemein-und-besonders` — Begruendung Allgemein und Besonders
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Normenanker

Arbeitsfokus: **Dokumentenintake**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Legistik Werkstatt-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
