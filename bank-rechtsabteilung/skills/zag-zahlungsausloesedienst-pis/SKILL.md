---
name: zag-zahlungsausloesedienst-pis
description: "Zahlungsauslösedienst nach ZAG und PSD2 prüfen: Erlaubnis, starke Kundenauthentifizierung, Haftungskette, Interface, technische Dienstleister und Händlerkommunikation im Bank-Rechtsabteilung."
---

# Zahlungsauslösedienst (PIS) nach ZAG und PSD2

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Dieser Skill prüft Zahlungsauslösedienste (Payment Initiation Services, PIS) nach § 1 Abs. 1 Satz 2 Nr. 7 ZAG und Art. 66 PSD2. Er deckt die Erlaubnisanforderungen, die starke Kundenauthentifizierung (SCA), die Haftungskette zwischen PIS-Provider und kontoführender Bank sowie die technischen Schnittstellenanforderungen nach der RTS-SCA (Delegierte VO 2018/389) ab.

## Kernnormen

- **§ 1 Abs. 1 Satz 2 Nr. 7 ZAG** – Definition Zahlungsauslösedienst: Dienst zur Auslösung eines Zahlungsauftrags auf Veranlassung des Zahlungsdienstnutzers vom Zahlungskonto bei einem anderen Zahlungsdienstleister
- **§ 10 ZAG** – Erlaubnispflicht; Anfangskapital für PIS nach § 17 ZAG: 50 TEUR (alternativ Berufshaftpflichtversicherung nach § 16 Abs. 3 ZAG)
- **§ 49 ZAG** – Pflichten und Rechte des kontoführenden Zahlungsdienstleisters gegenüber PIS-Providern: Schnittstellenbereitstellung, Nicht-Diskriminierung, Authentifizierungs-Weiterleitung
- **§ 55 ZAG** – Anmeldepflichten des PIS-Providers; Registrierung im BaFin-Zahlungsinstituts-Register
- **§ 46 ZAG** – Starke Kundenauthentifizierung (SCA): Pflicht zur SCA bei elektronischen Zahlungsvorgängen; Ausnahmen nach RTS-SCA Art. 10–18
- **§ 27 ZAG** – Haftung des PIS-Providers: bei nicht autorisierten Zahlungen Haftung gegenüber kontoführender Bank; Regress bei Verschulden des PIS-Providers
- **Art. 66 PSD2** (Richtlinie 2015/2366) – Rechte des Zahlungsauslösedienstleisters: Zugang zum Zahlungskonto, Informationspflichten, Authentifizierungsweiterleitung, Verbot Speicherung von Zahlungsdaten
- **Delegierte VO 2018/389 (RTS-SCA)** – technische Standards für SCA und sichere Kommunikation: Art. 4 SCA-Elemente, Art. 10–18 SCA-Ausnahmen, Art. 19–32 sichere Kommunikation (API/Fallback-Interface), Art. 33–36 dedizierte Schnittstelle

## Prüfschritte

1. **Dienst-Klassifikation** (§ 1 Abs. 1 Satz 2 Nr. 7 ZAG): Löst der Dienst tatsächlich einen Zahlungsauftrag aus (nicht nur Weiterleitung), vom Konto bei einem Dritten?
2. **Erlaubnis** (§ 10 ZAG): Anfangskapital 50 TEUR oder Berufshaftpflichtversicherung (Deckungssumme nach EBA-Orientierung 0,5 Mio. Euro pro Schaden, 1 Mio. Euro pro Jahr).
3. **SCA-Pflicht** (§ 46 ZAG, RTS-SCA Art. 4): Prüfe ob Ausnahme greift (geringer Betrag Art. 16, vertrauenswürdige Empfänger Art. 13, Unternehmenstransaktionen Art. 17).
4. **Schnittstellenrecht** (§ 49 ZAG, RTS-SCA Art. 30): Kontoführer muss API bereitstellen; Fallback nur wenn dedizierte Schnittstelle nicht verfügbar.
5. **Haftungskette** (§ 27 ZAG): PIS-Provider haftet unmittelbar bei Verschulden; Beweislast: Kontoführer muss Autorisierung nachweisen (§ 675w BGB).
6. **Informationspflichten** (Art. 66 Abs. 3 PSD2): Transaktionsreferenz, Betrag, Empfänger; keine Speicherung von Authentifizierungsdaten.
7. **Registrierung** (§ 55 ZAG): Eintragung im BaFin-Zahlungsinstituts-Register; Passporting in andere EWR-Staaten via § 38 ZAG-Notifizierung.

## Typische Fallkonstellationen

- E-Commerce-Händler integriert PIS-API: § 1 Abs. 1 Satz 2 Nr. 7 ZAG Erlaubnispflicht des PIS-Providers; Händler selbst erlaubnisfrei
- Bank verweigert API-Zugang: § 49 ZAG Diskriminierungsverbot; EBA-Beschwerdeverfahren; RTS-SCA Art. 33 Qualitätsanforderungen
- SCA-Ausnahme für Dauerauftrag: RTS-SCA Art. 14 (wiederkehrende Transaktionen gleicher Betrag/Empfänger); Erstauslösung mit SCA
- Unbefugter Zahlungsvorgang über PIS: § 27 ZAG Haftung PIS; § 675u BGB Erstattungsanspruch Zahler gegen Kontoführer; Regress
- Cross-Border-Betrieb (Deutschland + Frankreich): § 38 ZAG Notifizierung; RTS-SCA einheitlich anwendbar im EWR

