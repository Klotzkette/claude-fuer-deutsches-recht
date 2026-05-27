---
name: fachanwalt-strafrecht-chatcontrol-csam-anwaltsgeheimnis-53-stpo
description: "Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prueft ob Chat-Control-Massnahmen Anwaltsgeheimnis verletzen oder Mandatskommunikation abhoeren koennten. § 53 StPO Zeugnisverweigerungsrecht, § 97 StPO Beschlagnahmeverbot, BRAO Anwaltsgeheimnis, EU-Chat-Control-VO-Entwurf. Pruefraster Anwaltsgeheimnis-Schutz, Beschlagnahmeschutz, EU-Regulierungsrisiken, Mandatskommunikation-Sicherheit. Output Rechtsgutachten zu Chat-Control-Risiken fuer Anwaltsgeheimnis. Abgrenzung zu KI-Governance-Berufsrecht und zu Akteneinsicht."
---

# ChatControl / EU-CSAM und Anwaltsgeheimnis § 53 StPO

## Zweck

Spezial-Mandat: Mandant ist Anwalt oder Anwalt-Mitarbeiter, der Sorge hat, dass ChatControl 2.0 (EU-Verordnungsvorschlag zur Bekämpfung von CSAM — Child Sexual Abuse Material) seine Mandantenkommunikation kompromittiert. Konflikt mit Anwaltsgeheimnis (§ 43a Abs. 2 BRAO), Zeugnisverweigerungsrecht (§ 53 StPO), Beschlagnahmeverboten (§ 97 StPO).

## Eingaben

- Kommunikationskanal (E-Mail, Messenger Signal/WhatsApp/Threema, beA)
- Verschlüsselungs-Status (E2E, Transport, keine)
- Mandantenfälle (insbes. Strafverteidigung, Familienrecht mit Kindeswohl)
- Bestehende IT-Compliance der Kanzlei
- Cloud-Anbieter (USA / EU / Hybrid)

## Rechtlicher Rahmen

### EU-Ebene

- **Vorschlag COM(2022) 209** "ChatControl 2.0" — Pflicht-Scanning aller Kommunikationsdienste auf CSAM-Material und Grooming
- **EU-Datenschutzbeauftragter EDPS-Stellungnahme** (2022) — sieht Verstoß gegen Grundrechte
- **EuGH C-401/19** (Polnische Klage) — Grundrechte-Maßstab für Online-Filter

### Nationales Anwaltsrecht

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht Anwalt
- **§ 53 Abs. 1 Nr. 3 StPO** — Zeugnisverweigerungsrecht Anwalt
- **§ 53a StPO** — Personen, die Anwalt unterstützen
- **§ 97 StPO** — Beschlagnahmeverbot Verteidigungs-Unterlagen
- **§ 160a Abs. 1 StPO** — **Absolutes Erhebungsverbot** für Anwalts-Verteidiger-Kommunikation
- **§ 203 StGB** — Verletzung von Privatgeheimnissen
- **§ 33 BORA** — Datenverarbeitung in Kanzlei

### Leitentscheidungen

- BVerfG, Beschl. v. 27.4.2021 — 1 BvR 745/21 (Anwaltsgeheimnis bei staatlichem Zugriff)
- BVerfG, Urt. v. 19.4.2016 — 1 BvR 3309/13 (Beschlagnahmeverbot)
- BGH, Beschl. v. 13.5.2021 — 5 StR 26/21 (Reichweite § 160a StPO)

## Konflikt mit ChatControl 2.0

| ChatControl 2.0 Pflicht | Konflikt |
|---|---|
| Client-Side-Scanning aller Inhalte | Bricht Anwaltsgeheimnis vor Versand |
| Hash-Datenbank-Abgleich auf Endgerät | E2E-Verschlüsselung wird umgangen |
| Meldung an EU Centre | Mandatsdaten an Behörde |
| Verpflichtende Implementierung durch Provider | Anwalt kann nicht ausweichen |

## Strategie für Anwalts-Mandant

### Phase 1 — Status-Analyse

- Welche Kommunikationswege werden für Mandantengespräche genutzt?
- E2E-verschlüsselte vs. Server-side-Klartext
- Provider-Auswahl: EU-basiert vs. US (DPF-zertifiziert)

### Phase 2 — Verschlüsselungs-Konzept

- beA für Anwalts-Gerichts-Kommunikation (zwingend nach § 31a BRAO i.V.m. § 130d ZPO)
- Threema Work / Wire / Element für Mandantengespräche (Schweiz/EU, kein US-Server)
- PGP/S-MIME E-Mail-Verschlüsselung
- Vermeidung WhatsApp/Telegram (US-Server, ChatControl-Risiko)

### Phase 3 — Mandanten-Information

- Mandanten informieren: Verschlüsselte Kanäle bevorzugt
- Beratung Hochrisiko-Mandanten (politisch verfolgt, journalistische Quellen)
- Notizen physisch sichern

### Phase 4 — Politisches Engagement

- DAV-Stellungnahmen zu ChatControl
- BfDI-Konsultation
- Verfassungsbeschwerde-Beteiligung möglich (Verein Digitalcourage e.V., DAV)

### Phase 5 — Bei Vollziehung ChatControl (post-Verabschiedung)

- Verfassungsbeschwerde gegen Implementierung in Deutschland
- Beweisverwertungsverbot in Strafverfahren bei Anwalt-Mandanten-Material § 97 StPO
- BVerfG-Antrag auf einstweilige Anordnung

## Kanzlei-IT-Compliance

### Pflichten

- **§ 19 BORA / § 50 BRAO** — Datenträger-Verwendung sicher
- **BORA-Pflicht zu sicheren Kommunikationswegen** seit DSGVO
- **§ 43e BRAO** — Berufshaftpflichtversicherung mit IT-Sicherheits-Komponente
- **TLS Mindest-Standard** für E-Mail
- **Kanzlei-Server EU-Standort** empfohlen

### Konkrete Tools

- beA (anwaltliche Kommunikation Gericht)
- Threema Work / Wire (Mandanten-Chat)
- Tresorit / Boxcryptor / Strato HiDrive für Cloud-Speicherung
- Hardware-Token für Auth (YubiKey)

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| WhatsApp / iMessage für Mandantengespräche | ChatControl-Risiko + § 203 StGB | Migration läuft | Threema/Signal mit EU-Server |
| Cloud-Anbieter USA ohne DPF | DSGVO-Verstoß + ChatControl-Risiko | DPF-Prüfung | EU-Cloud mit BSI C5 |
| Klare CSAM-Falschtreffer in eigener Kanzlei | Strafverfolgung trotz Verteidiger-Privilegs | Klärung läuft | § 160a StPO greift |
| Verzicht auf Verschlüsselung | § 43a BRAO-Verstoß | Konzept in Arbeit | E2E-konsistent |

## Querverweise

- `fachanwalt-strafrecht-orientierung` — Triage
- `fachanwalt-strafrecht-wahlverteidiger-mandat` — Verteidigung
- `berufsrecht-ki-vertragspruefung` — bei KI-Anbieter-Risiken
- `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` — bei Vorfall

## Quellen und Updates

Stand: 05/2026. ChatControl 2.0 COM(2022) 209 weiterhin im Rat-Verfahren (Stand 2026); Verabschiedung verzögert. BVerfG 1 BvR 745/21 als Schutz-Maßstab. Bei Verabschiedung dringend Konsultation aktualisieren.
