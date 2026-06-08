---
name: 020-elektronischer-rechtsverkehr-ben-xnotar-xjustiz
description: "Notariat im Alltag: Elektronischer Rechtsverkehr – beN, XNotar, XJustiz und Registerportal. Technische und rechtliche Anforderungen für elektronische Einreichungen beim Handelsregister, Grundbuchamt und den Gerichten im Notariat."
---

# Notariat im Alltag: Elektronischer Rechtsverkehr – beN, XNotar, XJustiz, Registerportal

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck und Anwendungsbereich

Der elektronische Rechtsverkehr ist für Notare seit 2022 obligatorisch. Dieser Skill führt durch die technischen Anforderungen, Übermittlungswege (beN, EGVP, XJustiz) und die Besonderheiten des Registerportals sowie der elektronischen Grundbucheinreichung.

Rechtsgrundlagen: § 12 HGB i.V.m. § 10 EGovG (elektronische Anmeldung HR), § 39a BeurkG (elektronische Beglaubigung), § 137l EGBGB (Übergangsnormen), ERVV (Elektronischer Rechtsverkehr Verordnung), ERV-Verordnung, § 130a ZPO, §§ 14–15 GBO (elektronische Einreichung), NotVO, BNotO §§ 78a–78e (Notarpostfach beN).

## Übermittlungswege im Überblick

| Weg | Für | Besonderheit |
|---|---|---|
| beN (besonderes elektronisches Notarpostfach) | Gerichtskommunikation, HR-Einreichung | Ende-zu-Ende-verschlüsselt, § 78b BNotO |
| EGVP (Elektronisches Gerichts- und Verwaltungspostfach) | Bundesweite Gerichtskommunikation | XJustiz-Container-Format |
| Registerportal (www.handelsregister.de) | HR-Anmeldungen | XJUSTIZ-basiert, direkt |
| Elektronisches Grundbuch | Grundbuchanträge (je nach Bundesland) | XGBO-Format, Bundesland-abhängig |
| XNotar | Elektronische notarielle Urkunden | qualifizierte elektronische Signatur (qeS) |

## Qualifizierte Elektronische Signatur (qeS)

Die qeS (§ 126a BGB, eIDAS-Verordnung) ersetzt die eigenhändige Unterschrift in elektronischen Dokumenten. Für Notare:
- Signaturkarte der Bundesnotarkammer
- Nur für eigene Amtshandlungen (kein Aufgabenausgliedern)
- Zeitstempel empfohlen (qualifizierter Zeitstempel nach eIDAS)
- Signaturformat: XAdES oder PAdES (je nach Übermittlungsweg)

## Elektronische Beglaubigung (§ 39a BeurkG)

Notar kann Dokumente elektronisch beglaubigen (qualifizierte elektronische Signatur). Diese Beglaubigung ist der papierenen Beglaubigung gleichwertig (§ 39a Abs. 1 BeurkG). Einreichung beim Grundbuchamt oder HR möglich.

## XNotar und Urkundenübermittlung

XNotar ist das standardisierte Datenformat der Bundesnotarkammer für den Austausch notarieller Urkunden. Elektronisch signierte Urkunden können direkt aus dem Notarsystem via beN an Register und Gerichte übermittelt werden.

## Registerportal (Handelsregister)

- Über www.handelsregister.de können HR-Anmeldungen elektronisch eingereicht werden
- Notar authentifiziert sich mit beN oder qeS-Karte
- Anlagen (Urkunden, Beschlüsse) als PDF/A mit qeS
- Einreichungsdatum ist verbindlich für Fristen
- Registergericht sendet Zwischenverfügungen/Beschlüsse zurück via beN

## Grundbuch: Elektronische Einreichung

In vielen Bundesländern ist elektronische Einreichung möglich (ELRV-Landesrecht). Antrag mit qeS des Notars. Anlagen als PDF/A. Rangdatum ab Eingang beim Grundbuchamt (§ 17 GBO).

## Prüfprogramm

- beN-Zertifikat aktuell und gültig?
- Dokument als PDF/A (ISO 19005) gespeichert?
- qeS korrekt angebracht (Signaturbereich, kein nachträgliches Ändern)?
- XJustiz-Container vollständig strukturiert?
- Dateigrößenbeschränkung beachtet (je nach System max. 60 MB)?
- Eingangsbestätigung vom Register erhalten und dokumentiert?

## Typische Fallen

- beN-Zertifikat abgelaufen → Einreichung schlägt fehl.
- PDF nicht PDF/A-konform → Registergericht weist zurück.
- Signatur nach PDF-Änderung ungültig.
- Falsche XJustiz-Nachrichtentyp verwendet.
- Keine Eingangsbestätigung archiviert → Fristnachweis fehlt.

## Rechtsquellen

- § 39a BeurkG: https://dejure.org/gesetze/BeurkG/39a.html
- § 78b BNotO (beN): https://dejure.org/gesetze/BNotO/78b.html
- § 12 HGB: https://dejure.org/gesetze/HGB/12.html
- ERVV: https://www.gesetze-im-internet.de/ervv/
- eIDAS-VO: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910
- BNotK ERV-Leitfaden: https://www.bnotk.de

## Output-Formate

- **Einreichungs-Checkliste** (je nach Zielregister)
- **qeS-Prüfprotokoll** (Signatur, Format, Zeitstempel)
- **Fehleranalyse bei Zurückweisung** (typische Fehlerbilder)
- **Mandantenhinweis** (was elektronisch geht und was nicht)
- **beN-Konfigurationsleitfaden** (intern)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

