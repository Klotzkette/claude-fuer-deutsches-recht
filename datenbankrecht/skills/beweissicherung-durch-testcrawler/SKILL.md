---
name: beweissicherung-durch-testcrawler
description: "Rechtssichere Beweissicherung durch Testcrawler bei Datenbankrechts-Verletzungen: Aufbau und Betrieb eines eigenen Testcrawlers zur Verletzungsdokumentation, Verwertbarkeit der Ergebnisse als Beweismittel, notarielle Begleitung und Verhältnis zu § 202a StGB und DSGVO. Erstellt Testcrawler-Protokoll und rechtliche Bewertung der Zulässigkeit dieser Beweismethode im Datenbankrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Beweissicherung durch Testcrawler — Zulässigkeit und Verwertbarkeit

## Arbeitsbereich

Rechtssichere Beweissicherung durch Testcrawler bei Datenbankrechts-Verletzungen: Aufbau und Betrieb eines eigenen Testcrawlers zur Verletzungsdokumentation, Verwertbarkeit der Ergebnisse als Beweismittel, notarielle Begleitung und Verhältnis zu § 202a StGB und DSGVO. Erstellt Testcrawler-Protokoll und rechtliche Bewertung der Zulässigkeit dieser Beweismethode. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber will einen eigenen Testcrawler einsetzen, der die Verletzungen eines Wettbewerbers dokumentiert — ist das rechtlich zulässig?
- Anwalt fragt, ob durch einen Testcrawler gewonnene Beweise im Datenbankrechts-Prozess vor dem LG Hamburg verwertbar sind.
- IT-Abteilung soll einen Testcrawler entwickeln, der regelmäßig Wettbewerber-Websites auf Datenbankübereinstimmungen prüft.

## Erste Schritte

1. Zulässigkeit des Testcrawlers prüfen: Ist das Crawlen der Wettbewerber-Website erlaubt — AGB-Bindung, robots.txt, § 202a StGB bei Zugangssicherungen?
2. Beweisziel definieren: Was soll der Testcrawler nachweisen — Übernahme eigener Datenbankeinträge, systematische Entnahme, Honey-Pot-Treffer?
3. Testcrawler-Protokoll aufsetzen: Zeitstempel, Hashwerte der abgerufenen Daten, Vergleich mit eigener Datenbank, Abrufvolumen und Herkunft.
4. Notarielle oder technische Zertifizierung: Einsatz eines qualifizierten Zeitstempels (eIDAS-VO) oder notarielle Protokollierung des Crawling-Vorgangs.
5. Honey-Pot-Vergleich integrieren: Wenn eigene Datenbank Honey-Pot-Einträge enthält, können diese bei Wettbewerber nachgewiesen werden.
6. Verwertbarkeit im Prozess sichern: § 286 ZPO — technische Protokolle als Augenscheinsbeweis; Sachverständigen-Gutachten über die Vergleichsmethodik.

## Rechtsrahmen

- § 286 ZPO: Freie Beweiswürdigung — technische Protokolle und Crawl-Ergebnisse als Augenscheinsbeweis verwertbar.
- § 202a StGB: Ausspähen von Daten — Testcrawler darf keine Zugangssicherungen (Passwort, CAPTCHA, technische Sperre) überwinden.
- § 1 UWG: Unlautere Mittel — Testcrawler ohne Täuschung ist kein UWG-Verstoß, wenn nur öffentlich zugängliche Daten abgerufen werden.
- DSGVO Art. 6: Personenbezogene Daten — Testcrawler darf keine personenbezogenen Daten ohne Rechtsgrundlage erheben.
- eIDAS-VO Art. 41: Qualifizierter elektronischer Zeitstempel für Nachweis des Abrufzeitpunkts.
- § 87b UrhG: Verletzungstatbestand als Beweisziel — Testcrawler dokumentiert Entnahme von Teilen der eigenen Datenbank.

## Prüfraster

- Ist die Zielwebsite öffentlich zugänglich ohne Zugangssicherung (kein Login, kein CAPTCHA, keine technische Blockade)?
- Verletzt der Testcrawler die AGB der Zielwebsite — kann der Betreiber des Testcrawlers deshalb haftbar werden?
- Ist § 202a StGB ausgeschlossen — werden keine Zugangssicherungen überwunden?
- Enthält das Crawl-Protokoll alle für die Beweiswürdigung erforderlichen Daten (Zeitstempel, URLs, abgerufene Inhalte, Hashwerte)?
- Wurden Honey-Pot-Datensätze bei der Zielwebsite gefunden — sind diese eindeutig identifizierbar?
- Ist das Protokoll von einem neutralen Dritten (Notar, IT-Sachverständiger) zertifiziert?
- Enthält der Testcrawler-Abruf personenbezogene Daten — welche DSGVO-Rechtsgrundlage gilt?

## Typische Fallstricke

- Testcrawler, der robots.txt ignoriert, kann AGB-Verletzung begehen — Testcrawler-AGB-Compliance prüfen.
- Ohne neutrale Zertifizierung kann der Gegner die Authentizität der Crawl-Ergebnisse im Prozess angreifen.
- Honey-Pot-Datensätze müssen vor dem Verdachtsfall in der eigenen Datenbank vorhanden sein — nachträgliches Einpflegen entwertet den Beweis.
- DSGVO-Verletzung durch personenbezogene Datenabrufe im Testcrawler kann die Beweise unverwertbar machen.
- Sachverständiger muss die Crawl-Vergleichsmethodik vor Gericht erklären können — Briefing ist entscheidend.

## Output

- Testcrawler-Zulässigkeitsprüfung (§ 202a StGB / AGB / DSGVO)
- Testcrawler-Protokollvorlage (Zeitstempel, Hashwerte, Honey-Pot-Vergleich)
- Notarielle Beweissicherungs-Briefing-Vorlage für Crawl-Dokumentation
- Sachverständigen-Briefing für technischen Datenbankvergleich
- Prozessvorbereitung: Crawl-Beweis als Augenscheinsbeweis nach § 286 ZPO

## Quellen

- [§ 286 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/286.html)
- [§ 202a StGB — dejure.org](https://dejure.org/gesetze/StGB/202a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [eIDAS-VO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0910)
- [DSGVO Art. 6 — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 371 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/371.html)
