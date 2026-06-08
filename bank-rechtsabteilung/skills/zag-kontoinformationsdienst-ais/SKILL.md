---
name: zag-kontoinformationsdienst-ais
description: "Kontoinformationsdienst nach ZAG und PSD2 prüfen: Registrierung, Datenzugriff, Schnittstelle, Consent, Versicherung, Datenschutz, Open-Banking-Verträge und White-Label-Modelle im Bank-Rechtsabteilung."
---

# Kontoinformationsdienst (AIS) nach ZAG und PSD2

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Dieser Skill prüft Kontoinformationsdienste (Account Information Services, AIS) nach § 1 Abs. 1 Satz 2 Nr. 8 ZAG und Art. 67 PSD2. AIS-Provider unterliegen einem Light-Registrierungsregime (§ 34 ZAG) statt einer vollständigen Erlaubnis. Datenzugriffsrechte, Consent-Management, Haftungskette und die Anforderungen aus RTS-SCA Art. 36 (dedizierte Schnittstellen) werden normseitig verankert.

## Kernnormen

- **§ 1 Abs. 1 Satz 2 Nr. 8 ZAG** – Definition Kontoinformationsdienst: Online-Dienst zur Bereitstellung konsolidierter Informationen über ein oder mehrere Zahlungskonten; kein Zahlungsvorgang, nur Datenabruf
- **§ 34 ZAG** – Registrierungspflicht (nicht Erlaubnis); erleichtertes Verfahren; Mindestanforderungen: Berufshaftpflichtversicherung oder gleichwertige Garantie
- **§ 50 ZAG** – Zugangsrecht des AIS-Providers zu Kontoinformationen beim kontoführenden Zahlungsdienstleister; Nicht-Diskriminierungsgebot
- **§ 51 ZAG** – Haftungskette: AIS-Provider haftet für Schäden durch unbefugten Datenzugriff oder Datenweitergabe; Nachweis autorisierter Sitzung Voraussetzung
- **§ 46 ZAG i.V.m. RTS-SCA Art. 10** – SCA auch beim AIS-Datenabruf: erstmaliger Zugang und alle 90 Tage erneute SCA (Art. 10 Abs. 2 RTS-SCA VO 2018/389)
- **Art. 67 PSD2** (Richtlinie 2015/2366) – Rechte und Pflichten des AIS-Providers: Zugang nur auf explizite Zustimmung des Nutzers, Verbot der Verwendung für andere Zwecke als Informationsbereitstellung, keine Datenanreicherung ohne Einwilligung
- **RTS-SCA Art. 36** (VO 2018/389) – AIS-spezifische Schnittstellenanforderungen: kontoführender PSP muss AIS denselben Zugang gewähren wie dem Kontoinhaber; Fallback-Mechanismus
- **DSGVO Art. 6 Abs. 1 lit. a** – Rechtsgrundlage Einwilligung für AIS-Datenzugriff; Zweckbindung, Datensparsamkeit; Schnittstelle zu § 25 DSGVO Datenschutz by Design

## Prüfschritte

1. **Dienst-Klassifikation** (§ 1 Abs. 1 Satz 2 Nr. 8 ZAG): Nur Kontoinfos oder auch Zahlungsauslösung? Kombi-Dienst erfordert PIS-Erlaubnis (§ 10 ZAG) zusätzlich.
2. **Registrierung** (§ 34 ZAG): Berufshaftpflichtversicherung beschaffen (EBA-Mindestdeckung: 0,5 Mio. Euro pro Schaden); Registrierungsantrag BaFin.
3. **Consent-Mechanismus**: Explizite Einwilligung des Nutzers nach Art. 67 Abs. 2 lit. a PSD2; DSGVO-konforme Consent-UI; Scope klar begrenzen.
4. **SCA-Implementierung** (§ 46 ZAG, RTS-SCA Art. 10): 90-Tage-Erneuerungs-SCA; erstmaliger Zugang mit vollständiger SCA.
5. **API-Anforderungen** (RTS-SCA Art. 36, § 50 ZAG): Kontoführer muss Zugang ermöglichen; Qualitätsmessung gem. EBA-Leitlinie EBA/GL/2018/07 (jetzt RTS Art. 32).
6. **Datenschutz-Check** (DSGVO, Bundesdatenschutzgesetz): Zweckbindung (nur Kontoinformation), Speicherbegrenzung, Auskunftsrechte des Nutzers.
7. **Haftung** (§ 51 ZAG): Schadensersatzpflicht bei unbefugtem Zugriff; Nachweis gültiger Sitzung und Nutzer-Consent als Haftungsbefreiung.

## Typische Fallkonstellationen

- PFM-App (Personal Finance Management): § 1 Abs. 1 Satz 2 Nr. 8 ZAG, § 34 Registrierung, DSGVO Consent, 90-Tage-SCA-Erneuerung
- White-Label AIS für Kreditprüfung: § 50 ZAG Datenzugang, DSGVO Art. 22 Profilierungsverbot prüfen, Zweckbindung dokumentieren
- Kontoführer verweigert AIS-Zugang: § 50 ZAG Diskriminierungsverbot, RTS-SCA Art. 36, EBA-Eskalationsverfahren
- AIS-Dienstleister gibt Daten weiter: § 51 ZAG Haftung, DSGVO Art. 83 Abs. 4 Bußgeld bis 10 Mio. Euro
- Kombi AIS+PIS: Erlaubnis § 10 ZAG (PIS) + Registrierung § 34 ZAG (AIS) kombinieren

