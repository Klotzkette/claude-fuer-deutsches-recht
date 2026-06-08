---
name: quellen-livecheck
description: "Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Mandantenanfragen Assistent** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `dankt-dsgvo-sonderfall-e-mail` — Dankt Dsgvo Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis-erstantwort-generator` — Dringlichkeitsmarker Einwilligung Hinweis Erstantwort Generator
- `erstantwort-foermlich-mail` — Erstantwort Foermlich Mail
- `folgekorrespondenz-vorbereiten-konfliktcheck-vorab-ma` — Folgekorrespondenz Vorbereiten Konfliktcheck Vorab Ma
- `ma-einfuehrung-ma-erstvermerk-ma-konfliktcheck` — Ma Einfuehrung Ma Erstvermerk Ma Konfliktcheck
- `ma-mandant-manda-erstgespraechsleitfaden-manda-erstkontakt` — Ma Mandant Manda Erstgespraechsleitfaden Manda Erstkontakt
- `manda-mandatsablehnung-rechtsschutz-eintrittsanfrage` — Manda Mandatsablehnung Rechtsschutz Eintrittsanfrage
- `mandantenanfragen-anfrage-eingang-anrede-uebernehmen` — Mandantenanfragen Anfrage Eingang Anrede Uebernehmen
- `mehrsprachige-antwort-muster-erstantwort-spam-massen` — Mehrsprachige Antwort Muster Erstantwort Spam Massen
- `nennt-sachverhalt-telefon` — Nennt Sachverhalt Telefon
- `telefonische-terminvergabe-interessen-transkription-beweislast` — Telefonische Terminvergabe Interessen Transkription Beweislast
- `uebernimmt-telefon-konfiguration-transkriptionsdienst-erklaerung` — Uebernimmt Telefon Konfiguration Transkriptionsdienst Erklaerung

## Arbeitsweg

- Tragende Normen (DSGVO) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Mandantenanfragen Assistent (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
