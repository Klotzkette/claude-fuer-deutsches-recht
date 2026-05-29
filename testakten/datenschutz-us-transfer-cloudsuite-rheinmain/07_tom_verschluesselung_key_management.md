# TOMs und ergänzende Maßnahmen

Stand: 20.05.2026

## 1. Zugriff und Freigabe

Supportzugriffe aus den USA dürfen nur nach Freigabe eines RheinMain-Administrators erfolgen. Die Freigabe ist ticketbezogen, zeitlich befristet und muss den Zweck enthalten. CloudSuite protokolliert Nutzerkennung, Zeit, Ticket-ID, Zugriffsdauer und ausgeführte Admin-Aktionen.

## 2. Verschlüsselung

| Bereich | Stand | Bewertung |
|---|---|---|
| Transport | TLS 1.3 | Ausreichend |
| Datenbank | AES-256 | Ausreichend |
| Backups | AES-256, getrennte Backup-Schlüssel | Ausreichend |
| ReplyPilot-Payload | Anbieter-KMS, keine Kundenschlüssel | Für sensible Freitexte unzureichend |
| Exportdateien | SFTP oder verschlüsselter Downloadlink | Nur mit Ablaufdatum und MFA |

## 3. Key Management

CloudSuite nutzt standardmäßig Anbieter-KMS. RheinMain prüft die kostenpflichtige EU-Key-Option. Bis zur Entscheidung werden Ticketkategorien mit erhöhtem Schutzbedarf von ReplyPilot ausgeschlossen. Für Supportexporte wird ein RheinMain-PGP-Schlüssel eingesetzt.

## 4. Datenminimierung

- ReplyPilot erhält nur den letzten relevanten Ticketauszug, nicht die vollständige Historie.
- Maschinenseriennummern werden für Telemetrie gehasht.
- IP-Adressen werden nach 24 Stunden gekürzt.
- Anhänge werden nicht an ReplyPilot übertragen.

## 5. Organisatorische Maßnahmen

- Schulung Supportteam am 22.05.2026: keine privaten, gesundheitlichen oder HR-bezogenen Angaben in CloudSuite erfassen.
- Ticketkategorie `Rechtsfall` nur noch mit manueller Bearbeitung ohne KI-Vorschlag.
- Monatliche Stichprobe von 50 Tickets auf Freitextabweichungen.
- Subprozessor-Änderungen gehen an Legal, DSB und IT Security.

## 6. Behördenzugriff

CloudSuite verpflichtet sich laut Security Addendum, Behördenanfragen zu prüfen, anzufechten, soweit rechtlich zulässig, und RheinMain zu informieren, soweit kein Verbot besteht. Ein Jahresbericht 2025 liegt als Summary vor. RheinMain fordert für 2026 quartalsweise Aktualisierung oder Negativbestätigung.

## 7. Offene TOM-Punkte

| Punkt | Risiko | Termin |
|---|---|---|
| EU-Key-Option technisch und preislich klären | Mittel | 15.06.2026 |
| ReplyPilot-Payload-Maskierung testen | Hoch | 31.05.2026 |
| TicketForge Zugriff deaktiviert bestätigen | Hoch | 24.05.2026 |
| Audit-Log-Export automatisieren | Mittel | 30.06.2026 |
