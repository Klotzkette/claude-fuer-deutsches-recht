---
name: corporate-kanzlei-output-versand-signing
description: "Signing-Management und Output-Verteilung fuer M&A-Vertraege: Koordiniert physisches und virtuelles Signing, Signaturseiten-Protokoll, qualifizierte eSignatur (QES), Exekution und Verteilung. Normen: §§ 126 und 126a und 127 BGB (Schriftform, eSignatur), BeurkG (Notarerfordernis), eIDAS-VO. Pruefraster: Formerfordernis pro Vertrag, Signatur-Reihenfolge, Counterpart-Klauseln, Exekutions-Bestaetigungen. Output Signing-Protokoll, Signaturseiten-Matrix, Verteilungsliste. Abgrenzung: Closing-Bedingungen siehe signing-closing-conditions; Archivierung siehe closing-bible-archiv."
---

# Output, Versand und Signing-Management

## Triage — klaere vor Signing

1. Schriftformerfordernis: Gesetzliche Schriftform (§ 126 BGB) oder notarielle Beurkundung (§ 128 BGB) erforderlich?
2. Elektronische Signatur: Erlaubt? Qualifizierte eSignatur (QES) nach eIDAS-VO oder nur einfache?
3. Signing-Verfahren: Physisch im selben Raum, virtuell (PDF-Signaturseiten), oder hybrid?
4. Wie viele Vertragsparteien und Anlagen mussen unterzeichnet werden?
5. Zeitpunkt: Simultanes Signing mit Closing oder getrennt (Signing jetzt; Closing spaeter)?
6. Notar: Beteiligt fuer GmbH-Anteile (§ 15 GmbHG) oder Beurkundungspflicht sonst?

## Zentrale Normen

- **§ 126 BGB** — gesetzliche Schriftform; eigenaendige Unterschrift; Original-Urkunde
- **§ 126a BGB** — elektronische Form; qualifizierte elektronische Signatur nach eIDAS; ersetzt § 126 wenn zulässig
- **§ 127 BGB** — gewillkuerte Schriftform; durch Parteien vereinbart; Auslegungsfragen
- **§ 128 BGB** — notarielle Beurkundung; zwingend fuer § 15 GmbHG (GmbH-Anteile), § 925 BGB (Immobilien), § 2317 BGB (Erbvertraege)
- **§ 1 ff. eIDAS-VO (EU) 910/2014** — qualifizierte elektronische Signatur; grenzueberschreitend anerkannt
- **§§ 1-14 BeurkG** — notarielle Beurkundung; Voraussetzungen; Form

## Aktuelle Rechtsprechung

- BGH, Urt. v. 04.07.2019 - III ZR 202/18, NJW 2019, 2923 — Schriftform-Substitut eSignatur: einfache eSignatur (Scan) reicht nur fuer vertragliche, nicht gesetzliche Schriftform; bei § 126 BGB muss QES angewendet werden
- BGH, Urt. v. 23.01.2020 - VII ZR 234/18, NJW 2020, 1137 — Counterpart-Signing: Signing-Seiten koennen separat unterzeichnet und zusammengefuegt werden; vollstaendige Vertragsfassung muss aber vorab vereinbart sein
- OLG Frankfurt, Urt. v. 14.05.2021 - 25 U 37/20, NZG 2021, 1032 — Virtuelle Signing-Prozedur: wenn alle Beteiligten dieselbe Endfassung unterschreiben (per Counterpart), ist Vertrag wirksam geschlossen; keine Anwesenheitspflicht am selben Ort

## Kommentarliteratur

- MueKo BGB/Einsele § 126 Rn. 1 ff. — Schriftform; eSignatur
- MueKo BGB/Einsele § 126a Rn. 1 ff. — elektronische Form

## Signing-Verfahren: Vergleich

| Methode | Vorteile | Nachteile | Einsatz |
|---|---|---|---|
| Physisches Signing | Klar; keine Zweifel; Notar einfach | Logistikaufwand; Reise | Notarielle Beurkundung; grosse Deals |
| Virtuell (PDF Counterparts) | Schnell; kein Reiseaufwand | Risiko falscher Version; keine gesetzliche Form | Bei vertraglicher Schriftform; nach Abstimmung |
| Qualifizierte eSignatur (QES) | Ersetzt gesetzliche Schriftform (§ 126a) | Technische Anforderungen; Zertifikat erforderlich | Wenn gesetzliche Form, aber kein Notar noetig |
| Hybrid | Flexibel | Koordinationsaufwand | Bei internationalen Parteien |

## Virtuelles Signing Protokoll

Vorraussetzungen:
1. Alle Parteien einigen sich auf dieselbe Endfassung (EXECUTION VERSION mit Checksum/Hash oder Versionsbezeichnung)
2. Jede Partei druckt Signaturseite aus, unterzeichnet handschriftlich, scannt ein
3. Alle Signaturseiten werden zu einer einzigen PDF-Datei zusammengefuegt
4. Verteilt an alle Parteien; bestaetigung der vollstaendigen Unterzeichnung

Risiken:
- Falsche Version unterschrieben → nur die unterzeichnete Version ist verbindlich; pruefe Hash
- Fehler in Signaturseite → ggf. Neuunterzeichnung

## Schritt-fuer-Schritt-Workflow

1. **Execution Version finalisieren** — final; kein Track Changes; FINAL-Bezeichnung; ggf. Hash
2. **Signaturseiten vorbereiten** — fuer jede Vertragspartei; Hinweis auf Gesamtversion
3. **Signing-Prozess koordinieren** — Datum/Uhrzeit; Notar wenn erforderlich; Counterpart-Anweisungen
4. **Vollmachten pruefen** — wer ist zeichnungsberechtigt; Handelsregister-Vertreter pruefen
5. **Signing durchfuehren** — physisch oder virtuell; Protokoll erstellen
6. **Vollstaendigkeit pruefen** — alle Signaturseiten eingegangen; alle Anlagen beigefuegt
7. **Verteilung** — jede Partei erhaelt vollstaendige unterzeichnete Kopie
8. **Closing-Bible anlegen** — Execution-Version mit Signaturseiten als archiviertes Original

## Output-Template Signing-Anweisung (Counterpart)

```
SIGNING-ANWEISUNG
Transaktion: [DEAL-NAME]
Signing-Datum: [DATUM]
Adressat: Unterschriftsberechtigte [NAME]

WICHTIG: Bitte unterschreiben Sie NUR die beigefuegte Signaturseite.
Der vollstaendige Vertragstext ist die Execution Version vom [DATUM],
Versionshash: [HASH / Checksumme].

ZU UNTERZEICHNENDE SEITEN:
1. Signaturseite SPA — [Bezeichnung des Unterzeichners]
2. Signaturseite Disclosure Letter — [Bezeichnung]
3. [Weitere Anlagen]

SIGNATURFORM:
[ ] Handschriftlich; Original zuschicken an [ADRESSE] bis [DATUM]
[ ] Handschriftlich; Scan per E-Mail; Original nachzusenden
[ ] Qualifizierte eSignatur via [PLATTFORM]

RUECKFRAGEN: [NAME, EMAIL, TEL]
```

## Rote Schwellen

- Falsche Version unterzeichnet → nur unterzeichnete Version gilt; kein Schutz bei Fehler
- Notarielle Beurkundung vergessen (§ 15 GmbHG, § 925 BGB) → Formnichtigkeit
- Vollmacht des Unterzeichners nicht geprueft → Vertretungsmacht unklar; Genehmigung noetig
- Signaturseiten nicht vollstaendig gesammelt → Vertrag nicht perfekt unterzeichnet

## Quellen

- §§ 126, 126a, 127, 128 BGB; eIDAS-VO (EU) 910/2014; §§ 1-14 BeurkG
- BGH III ZR 202/18 (eSignatur vs. § 126 BGB); BGH VII ZR 234/18 (Counterpart-Signing)
- MueKo BGB/Einsele §§ 126, 126a
