---
name: private-devices-byod
description: "Klärt die Grenzen des Arbeitgeberzugriffs auf private Geräte (BYOD) in Internal Investigations – Einwilligung, Verhältnismäßigkeit, § 202a StGB im Internal Investigations Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Private Geräte und BYOD in Internal Investigations

## Arbeitsbereich

Klärt die Grenzen des Arbeitgeberzugriffs auf private Geräte (BYOD) in Internal Investigations – Einwilligung, Verhältnismäßigkeit, § 202a StGB. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

BYOD-Geräte (Bring Your Own Device) sind eine der schwierigsten Beweisquellen in Internal Investigations. Der Mitarbeiter ist Eigentümer des Geräts; auf ihm befinden sich sowohl Unternehmensdaten als auch private Daten. Der Zugriff ohne Einwilligung ist regelmäßig strafbar nach § 202a StGB (Ausspähen von Daten, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html)) und datenschutzrechtswidrig (Art. 8 EMRK, Art. 7 GRCh). Gleichzeitig können auf BYOD-Geräten beweisrelevante Unternehmensdaten liegen, auf die das Unternehmen Anspruch hat.

## Ziel dieses Skills

Dieser Skill klärt, unter welchen Bedingungen Arbeitgeber auf BYOD-Geräte zugreifen dürfen, wie Einwilligungen wirksam eingeholt werden und wie Unternehmensdaten von privaten Daten getrennt werden.

## Arbeitsprogramm

### 1. BYOD-Grundkonfiguration und rechtlicher Rahmen
- **Container-Lösungen** (z. B. Microsoft Intune, BlackBerry Dynamics): trennen Unternehmenscontainer von persönlichem Bereich; nur Container ist Arbeitgeberdomäne.
- Ohne Container: keine klare Trennung; jeder Zugriff betrifft auch private Daten.
- IT-Richtlinie / BYOD-Policy: legt fest, welche Unternehmensdaten auf dem privaten Gerät zulässig sind und welche Zugriffsrechte das Unternehmen hat.
- Betriebsvereinbarung (§ 87 BetrVG): BYOD-Policy bedarf der Mitbestimmung, wenn sie die Überwachung des Verhaltens der Mitarbeiter ermöglicht.

### 2. Einwilligung und ihre Grenzen
- Einwilligung nach Art. 7 DSGVO / § 26 Abs. 2 BDSG: muss freiwillig sein.
- Im Arbeitsverhältnis: Freiwilligkeit fraglich wegen Abhängigkeitsverhältnis; BAG und DSGVO-ErwGr. 43 betonen, dass Einwilligung in Arbeitsverhältnissen nur ausnahmsweise wirksam ist.
- Alternative zu Einwilligung: vertragliche Regelung im Arbeitsvertrag oder BYOD-Policy (§ 26 Abs. 1 BDSG).
- Widerruf der Einwilligung: jederzeit möglich; Konsequenz für Unternehmenszugriff unklar, wenn Unternehmensdaten bereits auf Gerät.

### 3. Herausgabepflicht für Unternehmensdaten
- Arbeitnehmer ist verpflichtet, Unternehmensdaten auf privatem Gerät herauszugeben (§ 667 BGB analog: Herausgabe allem, was im Rahmen des Auftrags erlangt wurde).
- Nicht verpflichtet: Übergabe des gesamten Geräts zur Forensik.
- Praktische Lösung: Mitarbeiter exportiert selbst alle relevanten Unternehmens-E-Mails, Chat-Nachrichten, Dokumente.
- Vollständigkeit nicht überprüfbar; ggf. Glaubwürdigkeitsfrage bei unvollständiger Übergabe.

### 4. Zugriff nur mit Einwilligung oder zwingenden Rechtsgrundlagen
- Einwilligung zur Forensik: schriftlich, informiert, spezifisch; Hinweis, was gesichert wird und warum.
- Strafverfahren: §§ 94, 102 StPO ermöglichen Beschlagnahme auch privater Geräte, wenn diese Beweismittel enthalten.
- Notfall: kein Zugriff ohne Rechtsgrundlage, auch wenn Verdacht stark ist.
- § 202a StGB: Zugriff auf passwortgeschützte Bereiche eines fremden Geräts ohne Einwilligung ist strafbar.

### 5. Fernlöschung (Remote Wipe)
- MDM erlaubt Remote Wipe auch auf BYOD-Geräten, wenn Unternehmenscontainer gelöscht werden soll.
- Selective Wipe: nur Unternehmenscontainer löschen, nicht das gesamte Gerät.
- Full Wipe: gesamtes Gerät löschen – bei BYOD nur mit ausdrücklicher Einwilligung oder im Notfall (Geräteverlust mit hochsensiblen Daten).
- Konsequenz: Remote Wipe vor Sicherung von Beweismitteln kann Beweisverlust bedeuten – Timing kritisch.

### 6. Praktisches Vorgehen bei Verdacht
1. Mitarbeiter schriftlich auffordern, Gerät nicht zu löschen (Legal Hold).
2. Mitarbeiter auffordern, alle Unternehmensdaten selbst zu exportieren und zu übergeben.
3. Falls Einwilligung zu forensischer Sicherung erlangt werden kann: professionelle Forensik mit DSGVO-konformem Filter.
4. Falls keine Einwilligung: Unternehmen muss mit Teilergebnis aus Unternehmens-Systemen arbeiten.
5. Bei konkreten strafrechtlichen Verdachtsmomenten: Staatsanwaltschaft kann Beschlagnahme beantragen.

### 7. Dokumentation
- BYOD-Policy und Einwilligung zur Forensik aufbewahren.
- Beschreibung des Geräts (Modell, Seriennummer) und was extrahiert wurde.
- Filter-Protokoll: welche Daten als privat ausgesondert wurden.
- Widerruf der Einwilligung dokumentieren.

## Red-Team-Fragen

- Hat das Unternehmen eine wirksame BYOD-Policy mit Forensik-Klausel?
- Wurde die Einwilligung zur Forensik vor dem Untersuchungsanlass eingeholt (nicht erst im Verdachtsfall)?
- Ist die Einwilligung freiwillig gewesen, oder bestand Druck wegen Kündigung?
- Wurden private Daten tatsächlich gefiltert, und ist das nachweisbar?
- Gibt es Unternehmensdaten auf dem Gerät, auf die das Unternehmen ohne Forensik Zugriff hat (Container, Cloud-Konto)?
- Wurde der Betriebsrat über die BYOD-Policy und die geplante Forensik informiert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 202a StGB | Ausspähen von Daten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 667 BGB | Herausgabepflicht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__667.html) |
| Art. 7 DSGVO | Bedingungen für Einwilligung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |

## Ausgabeformate

- **BYOD-Forensik-Einwilligungsformular** (DSGVO-konform)
- **Herausgabe-Aufforderung** (Unternehmensdaten auf privatem Gerät)
- **Filter-Protokoll** für private Daten
- **BYOD-Policy-Prüfcheckliste** (Mitbestimmung, Forensik-Klausel, Einwilligung)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
