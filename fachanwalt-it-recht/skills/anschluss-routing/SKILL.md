---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt It Recht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `dma-dsa-dsgvo-fachanwalt-governance` — Dma Dsa Dsgvo Fachanwalt Governance
- `dsv-aufnahme-dsv-benachrichtigung-dsv-benachrichtigung-dsv` — Dsv Aufnahme Dsv Benachrichtigung Dsv Benachrichtigung Dsv
- `dsv-dsfa-update-erstgespraech-vorfallmeldung-eskalationsmatrix` — Dsv Dsfa Update Erstgespraech Vorfallmeldung Eskalationsmatrix
- `dsv-kinderdaten-besondere-kommunikationssperre-lead-authority` — Dsv Kinderdaten Besondere Kommunikationssperre Lead Authority
- `dsv-massenbenachrichtigung-dsv-meldekette-dsv-meldung-dsv` — Dsv Massenbenachrichtigung Dsv Meldekette Dsv Meldung Dsv
- `dsv-meldung-baylda-bfdi-bln-bdi-hbdi-hmbbfdi` — Dsv Meldung Baylda Bfdi Bln Bdi Hbdi Hmbbfdi
- `dsv-meldung-lda-ldi-nrw-lfd-niedersachsen-sachsen-anhalt-lfdi` — Dsv Meldung Lda Ldi Nrw Lfd Niedersachsen Sachsen Anhalt Lfdi
- `dsv-meldung-lfdi-mv-rlp-saarland-saechsdsb` — Dsv Meldung Lfdi Mv Rlp Saarland Saechsdsb
- `dsv-meldung-tlfdi-uld-sh-nachmeldung-aktualisierung-enisa` — Dsv Meldung Tlfdi Uld Sh Nachmeldung Aktualisierung Enisa
- `dsv-pressemitteilung-krisenkommunikation-sammelklagen-vvt-update` — Dsv Pressemitteilung Krisenkommunikation Sammelklagen Vvt Update
- `dsv-rechtsprechung-saas-vertrag-fristennotiz-fachanwalt-it` — Dsv Rechtsprechung Saas Vertrag Fristennotiz Fachanwalt It
- `dsv-risikobewertung-art-schnelltriage-risiko-sofortmassnahmen` — Dsv Risikobewertung Art Schnelltriage Risiko Sofortmassnahmen
- `dsv-stakeholder-dsv-tonfall-dsv-verdacht-dsv-zeitleiste` — Dsv Stakeholder Dsv Tonfall Dsv Verdacht Dsv Zeitleiste
- `fachanwalt-it-cloud-vertrag-datenschutz-itr-ki-saas-bauleiter` — Fachanwalt It Cloud Vertrag Datenschutz Itr Ki Saas Bauleiter

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt It Recht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt IT-Recht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 DSGVO
- Art. 34 DSGVO
- Art. 9 DSGVO
- Art. 56 DSGVO
- Art. 32 DSGVO
- § 32 BSIG
- Art. 28 DSGVO
- Art. 82 DSGVO
- § 203 StGB
- Art. 55 DSGVO
- Art. 36 DSGVO
- § 8b BSIG

### Leitentscheidungen

- EuGH C-311/18
- EuGH C-300/21
- EuGH C-589/22

