---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Anlagen zu Schriftsätzen: ordnet Rolle (Mandant, Gegenpartei, Gericht), markiert Frist (Klageerwiderungsfrist), wählt Norm (§§ 131/253 ZPO Anlagen, § 416 ZPO Privaturkunde, § 437 ZPO öffentliche Urkunde) und Zuständigkeit (Zivilgerichte), leitet zum passenden Spez..."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Anlagen Zu Schriftsaetzen** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

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
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

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

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Anlagen Zu Schriftsaetzen sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
