---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Datenschutzrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `anwendungsfall-triage` — Anwendungsfall Triage
- `avv-art-26-joint-controllership-deutsch` — Avv Art 26 Joint Controllership Deutsch
- `avv-art-28-dsgvo-grundtatbestand` — Avv Art 28 Dsgvo Grundtatbestand
- `avv-art-28-mindestinhalte-checkliste` — Avv Art 28 Mindestinhalte Checkliste
- `avv-audit-avv-cloud-avv-eu-avv-konzern-avv` — Avv Audit Avv Cloud Avv Eu Avv Konzern Avv
- `avv-audit-und-kontrollrechte` — Avv Audit Und Kontrollrechte
- `avv-bestehender-avv-rolemix-avv-tom-datenpanne-meldung` — Avv Bestehender Avv Rolemix Avv Tom Datenpanne Meldung
- `avv-cloud-und-subverarbeitung-art-28-iv` — Avv Cloud Und Subverarbeitung Art 28 Iv
- `avv-eu-kommission-musterklauseln-2021-915` — Avv Eu Kommission Musterklauseln 2021 915
- `avv-eu-us-data-privacy-framework-bezug` — Avv Eu Us Data Privacy Framework Bezug
- `avv-haftung-datenschutz-schadensersatz-dsfa-risikoanalyse-dsr` — Avv Haftung Datenschutz Schadensersatz Dsfa Risikoanalyse Dsr
- `avv-haftung-risikoallokation-art-82-dsgvo` — Avv Haftung Risikoallokation Art 82 Dsgvo
- `avv-konzern-und-multi-party-konstellation` — Avv Konzern Und Multi Party Konstellation
- `avv-loeschung-rueckgabe-nach-vertragsende` — Avv Löschung Rueckgabe Nach Vertragsende

## Arbeitsweg

- Ergebnis sichten: Welche Datenschutzrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Datenschutzrecht DSGVO/BDSG.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.
