---
name: dokumente-intake
description: "Dokumentenintake für Anlagen zu Schriftsätzen: sortiert Verträge, Korrespondenz, Rechnungen, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Lichtbilder); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Anlagen Zu Schriftsaetzen** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Anlagen Zu Schriftsaetzen** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `anlage-fehlerkatalog` — Anlage Fehlerkatalog
- `anlage-red-anlagen-anlagenkonvolut-sonderfall` — Anlage RED Anlagen Anlagenkonvolut Sonderfall
- `anlagen-an-assistenz-uebersetzungspflicht` — Anlagen AN Assistenz Übersetzungspflicht
- `anlagen-aus-datenraum-und-sharepoint` — Anlagen AUS Datenraum und Sharepoint
- `anlagen-aus-edv-systemen` — Anlagen AUS EDV Systemen
- `anlagen-aus-mandantenmaterial` — Anlagen AUS Mandantenmaterial
- `anlagen-bei-berufung-revision` — Anlagen bei Berufung Revision
- `anlagen-bei-eilantrag-eu-arrest` — Anlagen bei Eilantrag EU Arrest
- `anlagen-berufung-revision-eilantrag-eu-bilder` — Anlagen Berufung Revision Eilantrag EU Bilder
- `anlagen-bilder-screenshots` — Anlagen Bilder Screenshots
- `anlagen-check-zustellung-redaktion-dsgvo` — Anlagen Check Zustellung Redaktion DSGVO
- `anlagen-duplikate-versionen-hashlog` — Anlagen Duplikate Versionen Hashlog
- `anlagen-elektronische-dokumente-format` — Anlagen Elektronische Dokumente Format
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Normenanker

Arbeitsfokus: **Dokumentenintake**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Anlagen Zu Schriftsaetzen-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
