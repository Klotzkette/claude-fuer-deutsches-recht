---
name: 036-signatur-qualifizierte-elektronische-signatur-und-d
description: "Notariat im Alltag: Signatur – qualifizierte elektronische Signatur und Dateiformate. Rechtliche Anforderungen der qeS nach eIDAS, notarielle Signaturpflichten, zulässige Dateiformate und Signaturprüfung im Notariat."
---

# Notariat im Alltag: Signatur – qualifizierte elektronische Signatur und Dateiformate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck und Anwendungsbereich

Die qualifizierte elektronische Signatur (qeS) ist das digitale Äquivalent zur eigenhändigen Unterschrift. Im Notarwesen ersetzt sie bei zugelassenen Verfahren die papierene Beglaubigung. Dieser Skill klärt technische Anforderungen, rechtliche Wirkungen und typische Fehlerquellen.

Rechtsgrundlagen: eIDAS-Verordnung (EU) Nr. 910/2014 (Art. 25–32), § 126a BGB (elektronische Form), § 39a BeurkG (elektronische Beglaubigung), § 78b BNotO (beN), ERVV (Elektronischer Rechtsverkehr Verordnung), EIDAS-DurchführungsVO (Signaturformate), § 130a ZPO (elektronisches Dokument an Gericht).

## Signaturtypen nach eIDAS

| Typ | Sicherheit | Rechtswirkung |
|---|---|---|
| Einfache elektronische Signatur (EES) | Niedrig | Kein Formäquivalent |
| Fortgeschrittene elektronische Signatur (FES) | Mittel | Kein gesetzliches Formäquivalent, aber beweisrechtlich relevant |
| Qualifizierte elektronische Signatur (QES/qeS) | Hoch | Schriftformäquivalent nach § 126a BGB; eIDAS Art. 25 Abs. 2 |

## Anforderungen an die qeS (eIDAS Art. 28–32)

- Einmaliger Signaturerstellungsschlüssel
- Zertifikat eines qualifizierten Vertrauensdienstleisters (TSP, EU-Vertrauensliste)
- Secure Signature Creation Device (SSCD): Signaturkarte oder Hardware-Token
- Für Notare: Signaturkarte der Bundesnotarkammer (BNotK)

## Zulässige Dateiformate für Einreichungen

| Format | Standard | Empfohlen für |
|---|---|---|
| PDF/A-1b | ISO 19005-1 | Archivierbare Dokumente, HR/Grundbuch |
| PDF/A-2a | ISO 19005-2 | Strukturierte PDFs mit Metadaten |
| XDF/XJustiz | XML | Registerportale, beN-Container |
| PKCS#7 (.p7s) | RFC 2315 | Signatur-Datei separat |
| CAdES | ETSI EN 319 122 | Container-Signatur |
| PAdES | ETSI EN 319 132 | Signatur im PDF integriert |
| XAdES | ETSI EN 319 132 | XML-basierte Signatur |

## Signaturvalidierung

Jede Einreichung muss vor dem Versand signaturvalidiert werden. Tools:
- BNotK-Signatur-Check (intern)
- Bundesvalidierungsdienst (BVD): https://www.bundesvalidierungsdienst.de
- Adobe Acrobat: Signaturprüfung im PDF

Prüfpunkte:
- Zertifikat gültig (nicht abgelaufen, nicht widerrufen)?
- Zertifikat auf EU-Vertrauensliste (https://esignature.ec.europa.eu/efts/tl)?
- Signatur nach letzter Änderung des Dokuments → ungültig!
- Zeitstempel vorhanden (empfohlen)?

## Notarielle Signaturpflichten

- Handelsregister-Anmeldungen: qeS der Notarin/des Notars (§ 12 HGB)
- Elektronische Beglaubigung (§ 39a BeurkG): qeS des Notars
- beN-Nachrichten: qualifizierter Container
- Beurkundungen als PDF: qeS bei elektronischer Ausfertigung

## Prüfprogramm

- Ist das Dokument PDF/A-konform?
- Wurde es nach der qeS-Anbringung nicht verändert?
- Ist das Zertifikat aktuell und auf der EU-Vertrauensliste?
- Wurde ein qualifizierter Zeitstempel gesetzt?
- Signaturformat kompatibel mit dem Zielsystem (Register, Gericht)?

## Typische Fallen

- PDF nach Signatur noch einmal gespeichert → Signatur ungültig.
- Signaturkarte abgelaufen → qeS technisch ungültig.
- Falsches Format: PAdES statt XAdES für XML-Container.
- Kein Zeitstempel → Signaturzeitpunkt unklar.
- Einreichung bei Gericht: falsches ERVV-Format.

## Rechtsquellen

- eIDAS-Verordnung: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910
- § 126a BGB: https://dejure.org/gesetze/BGB/126a.html
- § 39a BeurkG: https://dejure.org/gesetze/BeurkG/39a.html
- ERVV: https://www.gesetze-im-internet.de/ervv/
- BNotK Signaturleitfaden: https://www.bnotk.de
- Bundesvalidierungsdienst: https://www.bundesvalidierungsdienst.de

## Output-Formate

- **Signaturprüf-Protokoll** (Zertifikat, Datum, Formatprüfung)
- **Dateiformats-Entscheidungsmatrix** (je nach Zielregister)
- **Fehlerbehebungsleitfaden** (ungültige Signatur, falsches Format)
- **Mandantenhinweis** (qeS bei Fernbeglaubigungen)
- **Einreichungs-Checkliste** (PDF/A, qeS, Zeitstempel)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

