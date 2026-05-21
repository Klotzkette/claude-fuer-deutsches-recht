# Rechtsrahmen für Online-Banking-Phishing

Diese Datei ist ein Arbeitsrahmen für den Prüfmodus. Normtexte, Rechtsprechung und Verwaltungshinweise müssen im konkreten Mandat aktuell geprüft werden.

## Amtliche Normlinks

- § 675u BGB: Erstattung bei nicht autorisiertem Zahlungsvorgang
  https://www.gesetze-im-internet.de/bgb/__675u.html
- § 675v BGB: Haftung des Zahlers
  https://www.gesetze-im-internet.de/bgb/__675v.html
- § 675w BGB: Nachweis der Authentifizierung und Ausführung
  https://www.gesetze-im-internet.de/bgb/__675w.html
- § 675l BGB: Pflichten des Zahlers in Bezug auf Zahlungsinstrumente
  https://www.gesetze-im-internet.de/bgb/__675l.html
- § 676b BGB: Anzeige nicht autorisierter oder fehlerhaft ausgeführter Zahlungsvorgänge
  https://www.gesetze-im-internet.de/bgb/__676b.html
- § 55 ZAG: Starke Kundenauthentifizierung
  https://www.gesetze-im-internet.de/zag_2018/__55.html

## Kernlogik

1. Ausgangspunkt ist nicht "Phishing ja/nein", sondern: War der konkrete Zahlungsvorgang autorisiert?
2. Bei nicht autorisierten Zahlungsvorgängen steht der Erstattungsanspruch dem Grunde nach im Raum.
3. Die Bank kann sich je nach Fall auf Vorsatz oder grobe Fahrlässigkeit berufen.
4. Authentifizierungsprotokolle sind wichtig, ersetzen aber nicht die rechtliche Prüfung der Autorisierung.
5. Der Beweiswert hängt stark an konkreten App-Texten, Transaktionsbindung, Warnhinweisen, IP-/Geräte-Logs und Risikomanagement.

## Prüfungsbausteine

### Nicht autorisierter Zahlungsvorgang

Zu prüfen:

- Hat der Kunde die konkrete Zahlung mit Betrag und Empfänger freigegeben?
- Wurde nur ein vermeintlicher Sicherheitsvorgang bestätigt?
- War die Anzeige mehrdeutig oder irreführend?
- Wurde eine Sammel-/Batch-TAN verwendet?
- War die technische Freigabe an eine konkrete Transaktion gebunden?

### Grobe Fahrlässigkeit

Zu prüfen:

- TAN oder Freigabe am Telefon weitergegeben?
- Warnhinweise ignoriert?
- Berufliche oder besondere Kenntnisse?
- Plausibilität des Betrugsnarrativs?
- Drucksituation und Call-ID-Spoofing?
- Eindeutigkeit der App-Anzeige?
- Sofortige Sperrung und Anzeige?

### Bankpflichten

Zu prüfen:

- Starke Kundenauthentifizierung.
- Dynamische Verknüpfung mit Betrag und Empfänger.
- Risikobasiertes Transaktionsmonitoring.
- Umgang mit neuen Empfängern, neuen Geräten, auffälligen IPs, Tor/VPN, schneller Transaktionskette.
- Warnhinweise im konkreten Freigabedialog.
- Reaktionszeit nach Sperranruf.

## Beweisprogramm

Regelmäßig anfordern:

- Vollständige Authentifizierungs- und Autorisierungslogs.
- Exakter Wortlaut und Layout der App-Freigabe.
- Device-ID, Gerätebindung, App-Version, Betriebssystem.
- IP-Adressen, User-Agent, Geo-/Risikokennzeichen.
- Empfängeranlage und Änderung von Limits.
- Risikoscore/Monitoringentscheidung und Schwellenwerte.
- interne Fraud-Notizen, soweit prozessual erreichbar.
- Sicherheitswarnungen, Zustellung und konkrete Kenntnis des Kunden.

## Taktische Hinweise

- Früh Beweise sichern: Screenshots, Anruflisten, Sperrprotokolle, Strafanzeige, Kontoauszüge.
- Keine endgültigen Zugeständnisse zur TAN-Wirkung ohne App-Dialog prüfen.
- Bankablehnung in Tatsachenbehauptungen, Rechtsansichten und fehlende Belege zerlegen.
- Ombudsmann kann sinnvoll sein, wenn Beweisrisiko hoch und Vergleichsquote realistisch ist.
- Klage nur mit sauberer Transaktionsmatrix und konkret formulierten Beweisantritten.
