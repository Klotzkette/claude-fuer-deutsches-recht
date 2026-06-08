---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Vertragsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aenderungs-historie-agb-eskalations-marker` — Aenderungs Historie Agb Eskalations Marker
- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `bgb-business-einzelabrufe-sonderfall` — Bgb Business Einzelabrufe Sonderfall
- `fernabsatz-lieferanten-red-team` — Fernabsatz Lieferanten Red Team
- `fristennotiz-naechster-vertriebsvertraege-lieferantenvertrag` — Fristennotiz Naechster Vertriebsvertraege Lieferantenvertrag
- `mandat-arbeitsbereich-vr-einfuehrung-abmahnung-uwg` — Mandat Arbeitsbereich Vr Einfuehrung Abmahnung Uwg
- `nda-durchsetzer` — Nda Durchsetzer
- `nda-pruefungsvorschlaege-saas-msa` — Nda Pruefungsvorschlaege Saas Msa
- `rahmenvertrag-beweislast-vertragsrecht-vert-rahmenvertrag` — Rahmenvertrag Beweislast Vertragsrecht Vert Rahmenvertrag
- `renewal-review-routing` — Renewal Review Routing
- `saas-tracking-vert` — Saas Tracking Vert
- `vert-agb-vert-leistungsstoerungen-vr-agb` — Vert Agb Vert Leistungsstoerungen Vr Agb
- `vert-vertragsschluss-vertragspruefung-vertragsrecht` — Vert Vertragsschluss Vertragspruefung Vertragsrecht
- `vertragsrecht-kaltstart-interview` — Vertragsrecht Kaltstart Interview

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunde, AGB, Anbot/Annahme, Mahnschreiben, Rücktrittserklärung, Kündigungsschreiben, Anfechtungserklärung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Vertragsrecht (BGB Allgemeiner Teil und Schuldrecht)-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB §§ 116–144, 145–157, 158–163, 195, 199, 241, 242, 249, 254, 273, 275, 276, 280, 281, 282, 284, 286, 288, 305–310, 311, 311a, 311b, 313, 314, 320, 323, 324, 339–345, 433 ff., 535 ff., 631 ff., 651a ff., 765 ff., 812 ff., 823 ff. — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Vertragsparteien, AGB-Verwender, Verbraucher (§ 13), Unternehmer (§ 14), Verbraucherzentrale prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Vertragsparteien.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
