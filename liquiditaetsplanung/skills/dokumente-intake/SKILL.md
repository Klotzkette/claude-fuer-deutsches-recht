---
name: dokumente-intake
description: "Dokumentenintake für Liquiditätsplanung: sortiert Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste, prüft Datum, Absender, Frist und Beweiswert (Bankbestätigungen, Eingangs-/Ausgangsrechnungen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Liquiditaetsplanung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `ampel-zahlen-schwellenwerte-berechnung` — Ampel Zahlen Schwellenwerte Berechnung
- `ausgabengruppen-fristennotiz-naechster` — Ausgabengruppen Fristennotiz Naechster
- `ausgabengruppen-systematik` — Ausgabengruppen Systematik
- `bei-drohender-zahlungsunfaehigkeit` — bei Drohender Zahlungsunfaehigkeit
- `bei-eingetretener-zahlungsunfaehigkeit` — bei Eingetretener Zahlungsunfaehigkeit
- `cash-pooling-konzern` — Cash Pooling Konzern
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `deutschem-dokumentationspaket-excel` — Deutschem Dokumentationspaket Excel
- `deutschem-tatbestandsmerkmale-beweisfragen` — Deutschem Tatbestandsmerkmale Beweisfragen
- `dokumentationspaket-bank` — Dokumentationspaket Bank
- `drohender-zahlungsunfaehigkeit` — Drohender Zahlungsunfaehigkeit
- `eingangsdaten-checkliste` — Eingangsdaten Checkliste
- `eingangsdaten-idw-s6-liqp` — Eingangsdaten IDW S6 Liqp
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Liquiditätsstatus, Finanzplan, Liquiditätsvorschau 3 Wochen / 3–6–12 Monate, Fortbestehensprognose, Sanierungsgutachten IDW S 6.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Liquiditätsplanung und Insolvenzrecht-Schnittstelle-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: InsO §§ 17, 18, 19, 15a, IDW S 11, IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), StaRUG §§ 1, 29, 102 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Bank, IV/Restrukturierungsbeauftragter prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Geschäftsführung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
