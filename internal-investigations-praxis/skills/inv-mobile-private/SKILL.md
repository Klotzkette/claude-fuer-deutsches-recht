---
name: inv-mobile-private
description: "Inv 018 Mobile Devices, Inv 019 Private Devices Byod: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 018 Mobile Devices, Inv 019 Private Devices Byod

## Arbeitsbereich

Dieser Skill bündelt **Inv 018 Mobile Devices, Inv 019 Private Devices Byod** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-018-mobile-devices` | Sichert und wertet Mobile Devices (Smartphones, Tablets) forensisch aus – MDM, Passwortzugriff, BYOD-Grenzen, DSGVO. |
| `inv-019-private-devices-byod` | Klärt die Grenzen des Arbeitgeberzugriffs auf private Geräte (BYOD) in Internal Investigations – Einwilligung, Verhältnismäßigkeit, § 202a StGB. |

## Arbeitsweg

Für **Inv 018 Mobile Devices, Inv 019 Private Devices Byod** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-018-mobile-devices`

**Fokus:** Sichert und wertet Mobile Devices (Smartphones, Tablets) forensisch aus – MDM, Passwortzugriff, BYOD-Grenzen, DSGVO.

# Mobile-Device-Forensik in Internal Investigations

## Rechtlicher Rahmen

Smartphones und Tablets sind in Internal Investigations zentrale Beweisquellen: Textnachrichten, WhatsApp, Signal, Fotos, GPS-Daten und Browserverläufe. Die forensische Sicherung ist jedoch rechtlich komplex: Unternehmensgeräte sind leichter zugänglich als private Geräte (BYOD). § 26 BDSG und Art. 5 Abs. 1 lit. c DSGVO (Datenminimierung) setzen klare Grenzen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)). Das Auslesen privater Geräte ohne Einwilligung oder gesonderte Rechtsgrundlage ist regelmäßig unzulässig und kann § 202a StGB (Ausspähen von Daten, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html)) erfüllen.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Mobile-Device-Daten rechtssicher gesichert werden, die richtigen technischen Methoden eingesetzt werden und DSGVO- sowie Strafrecht-Grenzen beachtet werden.

## Arbeitsprogramm

### 1. Gerätetypen und Zugangsmethoden
- **iOS (iPhone/iPad)**: Gerätesperre; Backup über iTunes/iCloud; forensisch: GrayKey, Cellebrite UFED.
- **Android**: variiert stark nach Hersteller; ABD (Android Debug Bridge), forensisch: Cellebrite, Oxygen Forensics, Magnet Axiom.
- **Unternehmensgeräte mit MDM** (Mobile Device Management, z. B. Intune, MobileIron): Remote-Backup und Fernlöschung möglich.
- **BYOD (Bring Your Own Device)**: Container-Apps trennen Unternehmensdaten von privaten; forensisch nur Container zugänglich.

### 2. Rechtsgrundlage für Unternehmensgeräte
- Eigentum des Unternehmens: IT-Richtlinie / AGB des Arbeitgebers regeln zulässige Nutzung.
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten muss verhältnismäßig sein.
- MDM-Backup-Zugriff: in der Regel vom Betriebsrat mitbestimmt (§ 87 Abs. 1 Nr. 6 BetrVG); ohne Zustimmung droht Verwertungsverbot.
- Betriebsvereinbarung über Mobile-Device-Nutzung als Erlaubnisgrundlage.

### 3. Rechtsgrundlage für private Geräte (BYOD)
- Ohne Einwilligung des Mitarbeiters: Zugriff auf private Daten ist regelmäßig unzulässig.
- Einwilligung: freiwillig, informiert, widerruflich; im Verhältnis Arbeitgeber/Arbeitnehmer nur bedingt freiwillig.
- Alternative: Mitarbeiter wird aufgefordert, selbst relevante Daten zu exportieren und zu übergeben; Vollständigkeit kann nicht überprüft werden.
- § 202a StGB: unbefugter Zugriff auf fremde Daten ist strafbar.

### 4. Technische Extraktionsmethoden
- **Logical Extraction**: Zugriff auf Betriebssystemebene (Apps, Kontakte, Nachrichten); einfachste Methode.
- **File System Extraction**: direkter Dateisystemzugriff (mehr Daten als logical, weniger als physical).
- **Physical Extraction**: bit-genaue Kopie des internen Speichers; höchste Datenmenge, aber schwieriger bei modernen Geräten.
- **Chip-Off / JTAG**: destruktive Methode für beschädigte oder passwortgesperrte Geräte; forensisches Labor erforderlich.

### 5. Passwortzugriff
- Passwort-Brute-Force: rechtlich zulässig, wenn Eigentümer Gerät nicht entsperrt; aber: Gerät löscht sich nach 10 Fehlversuchen.
- MDM-Entsperrung: Admin kann PIN-Reset durchführen (nur bei MDM-verwalteten Geräten).
- Mitarbeiter wird aufgefordert, Gerät zu entsperren: arbeitsrechtliche Pflicht, wenn Gerät dem Arbeitgeber gehört.
- Verweigerung der Entsperrung bei privaten Geräten: kann nicht erzwungen werden; Beweisverwertung durch Schlussfolgerungen aus Verweigerung ist umstritten.

### 6. Cloud-Backup und Datensynchronisation
- iCloud/Google Drive: Backups meist nicht E2E-verschlüsselt für Apple/Google selbst; Zugriff über Strafverfolgungsbehörden möglich (§ 100j StPO).
- Unternehmensadministratoren haben bei unternehmenseigenen Cloud-Konten direkten Zugriff.
- DSGVO Art. 49: Herausgabe an US-Strafverfolgungsbehörden bedarf Rechtsgrundlage.

### 7. Dokumentation
- Gerätebeschreibung: Hersteller, Modell, Seriennummer, IMEI, iOS/Android-Version.
- Hash-Werte vor und nach Extraktion.
- Chain-of-Custody-Protokoll.
- Welche Daten wurden extrahiert, welche nicht (z. B. private Apps ausgeschlossen)?

## Red-Team-Fragen

- Wurde zwischen Unternehmensgerät und BYOD-Gerät rechtssicher unterschieden?
- Haben IT-Administratoren MDM-Backups ohne vorherige Betriebsrats-Zustimmung abgerufen?
- Wurden private Daten auf Unternehmensgeräten gefiltert, bevor der Forensiker ausgewertet hat?
- Ist der Passwortzugriff dokumentiert und auf zulässige Methoden beschränkt?
- Gibt es Hinweise auf Daten in Cloud-Backups, die nicht im Gerät-Image vorhanden sind?
- Sind Hash-Werte dokumentiert und stimmen sie mit den Originaldaten überein?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 202a StGB | Ausspähen von Daten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| § 100j StPO | Auskunft über Telekommunikationsdaten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__100j.html) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |

## Ausgabeformate

- **Geräteklassifizierungs-Matrix** (Unternehmensgerät/BYOD × Zugangsmethode × Rechtsgrundlage)
- **MDM-Extraktionsprotokoll**
- **Einwilligungsformular** für BYOD-Forensik
- **Chain-of-Custody-Protokoll** für Mobile Devices
- **DSGVO-Filterkonzept** für private Daten auf Unternehmensgeräten

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-019-private-devices-byod`

**Fokus:** Klärt die Grenzen des Arbeitgeberzugriffs auf private Geräte (BYOD) in Internal Investigations – Einwilligung, Verhältnismäßigkeit, § 202a StGB.

# Private Geräte und BYOD in Internal Investigations

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
