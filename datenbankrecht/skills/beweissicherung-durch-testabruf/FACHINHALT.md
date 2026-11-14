---
name: beweissicherung-durch-testabruf
description: "Für Beweissicherung durch Testabruf-Werkzeug — Zulässigkeit und Verwertbarkeit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix."
---

# Beweissicherung durch Testabruf-Werkzeug — Zulässigkeit und Verwertbarkeit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber will ein eigenes Testabruf-Werkzeug einsetzen, das die Verletzungen eines Wettbewerbers dokumentiert — ist das rechtlich zulässig?
- Anwalt fragt, ob durch ein Testabruf-Werkzeug gewonnene Beweise im Datenbankrechts-Prozess vor dem LG Hamburg verwertbar sind.
- IT-Abteilung soll ein Testabruf-Werkzeug entwickeln, das regelmäßig Wettbewerber-Websites auf Datenbankübereinstimmungen prüft.

## Erste Schritte

1. Zulässigkeit des Testabruf-Werkzeugs prüfen: Ist der automatisierte Abruf der Wettbewerber-Website erlaubt — AGB-Bindung, robots.txt, § 202a StGB bei Zugangssicherungen?
2. Beweisziel definieren: Was soll das Testabruf-Werkzeug nachweisen — Übernahme eigener Datenbankeinträge, systematische Entnahme, Honey-Pot-Treffer?
3. Testabruf-Werkzeug-Protokoll aufsetzen: Zeitstempel, Hashwerte der abgerufenen Daten, Vergleich mit eigener Datenbank, Abrufvolumen und Herkunft.
4. Notarielle oder technische Zertifizierung: Einsatz eines qualifizierten Zeitstempels (eIDAS-VO) oder notarielle Protokollierung des Auslesevorgangs.
5. Honey-Pot-Vergleich integrieren: Wenn eigene Datenbank Honey-Pot-Einträge enthält, können diese bei Wettbewerber nachgewiesen werden.
6. Verwertbarkeit im Prozess sichern: § 286 ZPO — technische Protokolle als Augenscheinsbeweis; Sachverständigen-Gutachten über die Vergleichsmethodik.

## Rechtsrahmen

- § 286 ZPO: Freie Beweiswürdigung — technische Protokolle und Abruflauf-Ergebnisse als Augenscheinsbeweis verwertbar.
- § 202a StGB: Ausspähen von Daten — Testabruf-Werkzeug darf keine Zugangssicherungen (Passwort, CAPTCHA, technische Sperre) überwinden.
- § 1 UWG: Unlautere Mittel — Testabruf-Werkzeug ohne Täuschung ist kein UWG-Verstoß, wenn nur öffentlich zugängliche Daten abgerufen werden.
- DSGVO Art. 6: Personenbezogene Daten — Testabruf-Werkzeug darf keine personenbezogenen Daten ohne Rechtsgrundlage erheben.
- eIDAS-VO Art. 41: Qualifizierter elektronischer Zeitstempel für Nachweis des Abrufzeitpunkts.
- § 87b UrhG: Verletzungstatbestand als Beweisziel — Testabruf-Werkzeug dokumentiert Entnahme von Teilen der eigenen Datenbank.

## Prüfraster

- Ist die Zielwebsite öffentlich zugänglich ohne Zugangssicherung (kein Login, kein CAPTCHA, keine technische Blockade)?
- Verletzt das Testabruf-Werkzeug die AGB der Zielwebsite — kann der Betreiber des Testabruf-Werkzeugs deshalb haftbar werden?
- Ist § 202a StGB ausgeschlossen — werden keine Zugangssicherungen überwunden?
- Enthält das Abruflauf-Protokoll alle für die Beweiswürdigung erforderlichen Daten (Zeitstempel, URLs, abgerufene Inhalte, Hashwerte)?
- Wurden Honey-Pot-Datensätze bei der Zielwebsite gefunden — sind diese eindeutig identifizierbar?
- Ist das Protokoll von einem neutralen Dritten (Notar, IT-Sachverständiger) zertifiziert?
- Enthält der Testabruf-Abruf personenbezogene Daten — welche DSGVO-Rechtsgrundlage gilt?

## Typische Fallstricke

- Testabruf-Werkzeug, das robots.txt ignoriert, kann AGB-Verletzung begehen — technische und vertragliche Compliance prüfen.
- Ohne neutrale Zertifizierung kann der Gegner die Authentizität der Abruflauf-Ergebnisse im Prozess angreifen.
- Honey-Pot-Datensätze müssen vor dem Verdachtsfall in der eigenen Datenbank vorhanden sein — nachträgliches Einpflegen entwertet den Beweis.
- DSGVO-Verletzung durch personenbezogene Datenabrufe im Testabruf-Werkzeug kann die Beweise unverwertbar machen.
- Sachverständiger muss die Abruflauf-Vergleichsmethodik vor Gericht erklären können — Briefing ist entscheidend.

## Quellen

- [§ 286 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/286.html)
- [§ 202a StGB — dejure.org](https://dejure.org/gesetze/StGB/202a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [eIDAS-VO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0910)
- [DSGVO Art. 6 — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 371 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/371.html)
