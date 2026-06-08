---
name: verletzung-dokumentieren-hashlog-screenshot-crawl-protoko
description: "Beweissicherung bei Datenbankrechts-Verletzungen: Methoden zur gerichtsfesten Dokumentation von Scraping und unerlaubter Entnahme durch Hash-Logs, Screenshot-Serien, Crawl-Protokolle, Honey-Pot-Datensätze und notarielle Sicherung. Erstellt Beweis-Checkliste für § 87b UrhG-Klagen und einstweilige Verfügungen sowie technisches Sachverständigen-Briefing im Datenbankrecht."
---

# Verletzung dokumentieren — Hash-Logs, Screenshots und Crawl-Protokolle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber hat Hinweise auf systematisches Scraping durch einen Wettbewerber und fragt, wie er Beweise gerichtsfest sichert.
- Anwalt bereitet eine Klage nach § 87b UrhG vor und benötigt verwertbare Beweismittel für Entnahmemenge und Systematik des Verletzers.
- IT-Abteilung eines Unternehmens soll ein Beweissicherungsprotokoll entwickeln, das bei zukünftigen Datenbankrechts-Verletzungen sofort einsetzbar ist.

## Erste Schritte

1. Beweissicherungsziele definieren: Was muss bewiesen werden — Tatsache der Entnahme, Umfang, Systematik, Zurechenbarkeit zum Verletzer?
2. Technische Beweismittel sichern: Server-Logs (IP-Adressen, User-Agents, Zeitstempel, Anfragevolumen), API-Gateway-Protokolle, Datenbankabfrage-Logs.
3. Hash-Logs erstellen: Kryptographische Hashwerte der Datenbankzustände vor und nach Verletzungszeitraum als Integritätsnachweis.
4. Screenshots und Zeitstempel sichern: Dokumentation der verletzenden Website/App, notariell beglaubigt oder mit qualifizierter elektronischer Zeitstempelung (eIDAS-VO).
5. Honey-Pot-Datensätze als Beweismittel: Einzigartiger Datensatz in der Datenbank, der beim Verletzer nachweisbar auftaucht.
6. Notarielle oder gerichtliche Sicherung: Einstweilige Beweissicherung nach § 485 ZPO; Internetseiten-Protokollierung durch Notar.

## Rechtsrahmen

- § 87b UrhG: Verletzungstatbestand — Nachweis der Entnahme wesentlicher Teile und Zurechenbarkeit erforderlich.
- § 485 ZPO: Selbstständiges Beweisverfahren zur vorprozessualen Sicherung von Beweismitteln.
- § 97a UrhG: Abmahnerfordernis — Abmahnung muss auf gesichertem Beweisstand beruhen.
- eIDAS-VO Art. 41: Qualifizierter elektronischer Zeitstempel als Beweis für Zeitpunkt der Sicherung.
- § 286 ZPO: Freie Beweiswürdigung — technische Protokolle sind als Beweismittel zulässig, müssen aber authentisch und vollständig sein.
- § 371 ZPO: Augenscheinsbeweis für digitale Inhalte — Screenshots, Videos, Protokolle als Beweismittel.

## Prüfraster

- Sind Server-Logs lückenlos und manipulationsgeschützt gespeichert (Schreibschutz, Hash-Signaturen)?
- Lässt sich aus den Logs die IP-Adresse, User-Agent-Zeichenkette und das Abfragevolumen des Verletzers eindeutig ermitteln?
- Sind Honey-Pot-Datensätze vorhanden und eindeutig identifizierbar, wenn sie beim Verletzer auftauchen?
- Wurde die verletzende Website/App durch Notar oder mit qualifiziertem Zeitstempel dokumentiert?
- Ist der Sachverständige benannt und gebrieft, um technische Beweismittel vor Gericht zu erläutern?
- Wurden die Beweismittel zeitnah gesichert und nicht nachträglich verändert?
- Ist die Kette der Beweismittel lückenlos — von der Entnahme bis zum Erscheinen beim Verletzer?

## Typische Fallstricke

- Server-Logs werden regelmäßig überschrieben — ohne Sicherungsprozess gehen entscheidende Beweise verloren.
- IP-Adressen allein sind kein sicherer Täternachweis — VPN, TOR, Proxy-Ketten können Verschleierung ermöglichen.
- Screenshots ohne Zeitstempel sind als Beweismittel schwach — notarielle oder elektronische Zeitstempelung ist erforderlich.
- Honey-Pot-Datensätze müssen von Anfang an in der Datenbank vorhanden sein — nachträgliches Einpflegen ist als Beweis wertlos.
- Ohne Sachverständigen scheitern technische Beweismittel im Prozess häufig an mangelnder gerichtlicher Würdigung.

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 485 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/485.html)
- [§ 97a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 286 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/286.html)
- [eIDAS-VO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0910)
- [§ 371 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/371.html)

