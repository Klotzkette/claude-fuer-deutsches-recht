---
name: folgekorrespondenz-vorbereiten
description: "Nach Eingang einer Anfrage muss Sekretariat CRM-Eintrag und Akte anlegen. CRM-Eintrag Kanzlei-Intake. Pruefraster: Name Mail Telefon Anliegen-Stichwort Dringlichkeit Datum Sprachkennung Konfliktcheck-Status. Output: Skeleton-Eintrag fuer CRM und Aktenanlage. Abgrenzung zu anfrage-eingang-parser (Parsing) und mandanten-intake im Sozialrecht."
---

# Folgekorrespondenz-Vorbereiten

Dieser Skill erstellt auf Basis der geparsten Eingangsanfrage einen fertigen Skeleton-Eintrag für das CRM-System oder die manuelle Aktenanlage. Ziel: Die Sekretariatsmitarbeitende kann den Vorgang sofort weiterführen, ohne Informationen erneut aus der Originalmail suchen zu müssen.


## Triage zu Beginn
1. Sind alle Pflichtfelder (Name, E-Mail, Anliegen, Dringlichkeit, Datum) aus dem Parsing verfuegbar?
2. Welches CRM oder welche Aktenstruktur wird genutzt (DATEV, RA-MICRO, Advoware, manuell)?
3. Wurde der Konfliktcheck bereits durchgefuehrt oder muss er im CRM-Eintrag als ausstehend markiert werden?
4. Soll der Eintrag automatisch oder nach manueller Freigabe gespeichert werden?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — CRM-Eintrag und Aktenanlage als Teil der Kanzlei-Organisationspflicht; fehlende Dokumentation begruendet Haftungsrisiko.
- BGH, Urt. v. 26.04.2018 - I ZR 82/17, NJW 2018, 2329 — Nachweis der Mandatseingabe als Beweisfrage; strukturierter CRM-Eintrag mit Zeitstempel ist Beweisnachricht fuer Eingangsdatum.
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Speicherung von Mandantenanfrage-Daten im CRM erfordert Rechtsgrundlage nach Art. 6 DSGVO; Vertragsanbahnung (lit. b) oder berechtigtes Interesse (lit. f) als Grundlage.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Vollstaendigkeit des Akteneintrags: alle Kontaktdaten, Anliegen-Stichwort und Dringlichkeit muessen im CRM erfasst sein; lueckenhafte Eintragung begruendet spaetere Nachweisschwierigkeiten.

## Zentrale Normen
- Art. 6 Abs. 1 lit. b DSGVO — Vertragsanbahnung als Rechtsgrundlage fuer CRM-Speicherung
- Art. 5 Abs. 1 lit. e DSGVO — Speicherbegrenzung: CRM-Eintrag nur so lange, wie fuer das Ziel notwendig
- § 43 BRAO — Sorgfaltspflicht: vollstaendige und sofortige Akten-/CRM-Dokumentation
- § 51 BRAO — Haftung: mangelnde Dokumentation als Organisationspflichtverletzung

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Dokumentationspflicht: CRM und Aktenanlage als Teil der Sorgfalt)
- Kühling/Buchner DSGVO Art. 5 Rn. 60-80 (Speicherbegrenzung: Grundsaetze und CRM-Praxis)

## Skeleton-Eintrag: Standardformat

```
=== NEUER VORGANG — ERSTANFRAGE ===
Eingangsdatum:     [DATUM UND UHRZEIT]
Eingangskanal:     E-Mail

--- KONTAKT ---
Name:              [NACHNAME, VORNAME] | [Titel falls vorhanden]
E-Mail:            [ABSENDER-ADRESSE]
Telefon:           [TELEFONNUMMER oder „nicht genannt"]
Postanschrift:     [ADRESSE oder „nicht genannt"]
Sprache:           [DE / EN / FR / IT / Sonstiges]

--- ANLIEGEN ---
Rechtsgebiet:      [Ersteinschätzung: z. B. Arbeitsrecht / Mietrecht / Strafrecht]
Stichwörter:       [Kommagetrennte Liste — max. 5 Begriffe]
Beteiligte:        [Gegner / Behörde / weitere Parteien oder „nicht genannt"]
Sachverhalt-Kurzfassung:
  [2-4 Sätze aus dem Parsing — wortwörtlich oder eng paraphrasiert]

--- DRINGLICHKEIT ---
Stufe:             [HOCH / MITTEL / NIEDRIG / UNBEKANNT]
Begründung:        [Frist, Termin, Eile-Signal oder „kein Hinweis"]
Massnahme:         [Sofortiger Anwaltsrückruf erforderlich / Normale Bearbeitung / Abwarten]

--- STATUS ---
Spam-Check:        [KLAR / VERDÄCHTIG / SPAM]
Konfliktcheck:     [AUSSTEHEND — vor Terminvergabe durchführen!]
Erstantwort:       [VERSENDET am DATUM / AUSSTEHEND]
Transkription:     [AKTIV / NICHT AKTIV]

--- INTERNE NOTIZEN ---
[Platz für manuelle Ergänzungen der Sekretariatsmitarbeitenden]

=== ENDE SKELETON-EINTRAG ===
```

## Felder im Detail

### Eingangsdatum und -kanal

- Automatisch befüllt mit dem aktuellen Zeitstempel (ISO 8601: `YYYY-MM-DD HH:MM`)
- Eingangskanal: E-Mail, Telefon, Kontaktformular, Post — für E-Mail-basierte Anfragen stets „E-Mail"

### Kontakt-Felder

Aus dem Parsing-Skill (`anfrage-eingang-parser`) übernommen. Fehlende Felder werden mit „nicht genannt" markiert und für manuelle Ergänzung hervorgehoben.

### Rechtsgebiet-Ersteinschätzung

**Wichtig:** Dies ist eine nicht-verbindliche Ersteinschätzung des Parsing-Algorithmus. Sie dient der Vorsortierung im Sekretariat und darf NICHT als rechtliche Einschätzung an die anfragende Person weitergegeben werden.

Mögliche Rechtsgebiete (Auswahl):
- Arbeitsrecht, Mietrecht, Familienrecht, Erbrecht, Strafrecht
- Gesellschaftsrecht, Vertragsrecht, Schadensersatz
- Verwaltungsrecht, Sozialrecht, Steuerrecht
- Verkehrsrecht, Insolvenzrecht, IP-Recht
- Sonstiges / Unbekannt

### Dringlichkeitsstufen

| Stufe | Beschreibung | Sofortmaßnahme |
|---|---|---|
| HOCH | Frist erkannt, Haftungsrisiko, bevorstehende Verhandlung | Anwalt ruft sofort zurück |
| MITTEL | Zeitdruck vorhanden, aber keine akute Frist | Rückmeldung innerhalb 24h |
| NIEDRIG | Kein Zeitdruck erkennbar | Rückmeldung im normalen Ablauf |
| UNBEKANNT | Keine Aussage zu Dringlichkeit möglich | Wie MITTEL behandeln |

### Konfliktcheck-Status

Standardmäßig: `AUSSTEHEND`. Die Sekretariatsmitarbeitende trägt nach Durchführung des Konfliktchecks ein:
- `KLAR — kein Konflikt erkannt` oder
- `KONFLIKT — Mandat nicht möglich` oder
- `KONFLIKT — Rücksprache mit RA erforderlich`

### Transkriptions-Status

- `AKTIV` wenn die anfragende Person den Transkriptionsservice nutzen soll/wird
- `NICHT AKTIV` bei Standardverfahren mit schriftlicher Sachverhaltsschilderung

## Integration in gängige CRM-Systeme

Dieser Skill gibt einen Text-basierten Skeleton aus, der in alle gängigen Systeme eingefügt werden kann:

- **RA-MICRO:** Als neue Akte anlegen; Felder manuell übertragen; Aktenzeichen generieren.
- **Advoware:** Neues Mandat anlegen; Kontaktdaten übertragen; Status auf „Erstanfrage" setzen.
- **DATEV Anwalt:** Neues Verfahren anlegen; Mandantenakte erstellen.
- **Eigenentwicklung / Excel:** Tabellenzeile; CSV-Import möglich.

## Ausgabe

```
SKELETON-EINTRAG BEREIT
Für CRM-System oder manuelle Akte kopieren und einfügen.
Ausstehende Felder sind mit [BITTE ERGÄNZEN] markiert.
Konfliktcheck: AUSSTEHEND — vor Terminvergabe durchführen!
```

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datenquelle
- `dringlichkeitsmarker` — Dringlichkeitsstufe und Begründung
- `spam-und-massen-anfrage-filter` — Spam-Check-Status
- `konfliktcheck-vorab` — Hinweis auf ausstehenden Konfliktcheck
