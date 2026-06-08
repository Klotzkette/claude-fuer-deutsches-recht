---
name: dokumente-intake
description: "Dokumentenintake für Schriftform/Textform BGB: sortiert Vertrag, Unterschrift, qualifizierte e-Signatur, prüft Datum, Absender, Frist und Beweiswert (Empfangsbestätigung, Versandbeleg); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Schriftform Und Textform Bgb** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `amtlicher-formkern-bgb-zpo-check` — Amtlicher Formkern BGB ZPO Check
- `anspruchsformulierungen-formverstoss` — Anspruchsformulierungen Formverstoss
- `arbeitsrecht-befristung-schriftform-checker` — Arbeitsrecht Befristung Schriftform Checker
- `befristungsabrede-qes-rechtsprechung` — Befristungsabrede QES Rechtsprechung
- `befristungsabrede-qes-rechtsprechung-stand-2026` — Befristungsabrede QES Rechtsprechung Stand 2026
- `bgb-mehrparteien-konflikt-und-interessen` — BGB Mehrparteien Konflikt und Interessen
- `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` — Buergschaft Verbraucherdarlehen und Andere Strenge Formen
- `checklisten-schriftsatz-brief-und-memo-bausteine` — Checklisten Schriftsatz Brief und Memo Bausteine
- `dokumentations-und-beweisarchitektur` — Dokumentations und Beweisarchitektur
- `elektronische-paragraph-formerfordernisse` — Elektronische Paragraph Formerfordernisse
- `empfangsbeduerftiger-international` — Empfangsbeduerftiger International
- `empfangsbeduerftiger-international-schnittstellen` — Empfangsbeduerftiger International Schnittstellen
- `form-checker-fuer-vertrag-oder-willenserklaerung` — Form Checker Fuer Vertrag Oder Willenserklaerung
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Schriftform Und Textform Bgb-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Vertragsparteien.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
