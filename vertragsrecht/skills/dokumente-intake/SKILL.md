---
name: dokumente-intake
description: "Dokumentenintake für Vertragsrecht (BGB-Vertragsrecht): sortiert Vertrag, AGB, Korrespondenz, prüft Datum, Absender, Frist und Beweiswert (Mailverkehr, Verhandlungsprotokolle); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Vertragsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `abmahnung-uwg` — Abmahnung UWG
- `aenderungs-historie-agb-eskalations-marker` — Aenderungs Historie AGB Eskalations Marker
- `agb-pruefung` — AGB Pruefung
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `bgb-business-einzelabrufe-sonderfall` — BGB Business Einzelabrufe Sonderfall
- `business-compliance-dokumentation-und-akte` — Business Compliance Dokumentation und Akte
- `einzelabrufe-sonderfall-und-edge-case` — Einzelabrufe Sonderfall und Edge Case
- `eskalations-marker` — Eskalations Marker
- `eskalations-quellenkarte` — Eskalations Quellenkarte
- `fernabsatz-lieferanten-red-team` — Fernabsatz Lieferanten RED Team
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `fristennotiz-naechster-vertriebsvertraege` — Fristennotiz Naechster Vertriebsvertraege
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

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
