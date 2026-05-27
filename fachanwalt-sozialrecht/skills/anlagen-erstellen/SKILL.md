---
name: anlagen-erstellen
description: "Anwalt muss Anlagenkonvolut zu Widerspruch Klage oder Schriftsatz in korrekter juristischer Konvention erstellen. Anlagenanhaenge Sozialrecht K1/W1/A1-Konvention. Pruefraster: Sigel Bezeichnung Quelle Datum Seitenzahl Bezug im Text. Erzeugt Anlagenverzeichnis und prueft Vollstaendigkeit jede Anlage muss im Text zitiert sein. Output: Anlagenverzeichnis als Vorblatt mit korrekter Nummerierung. Abgrenzung zu akteneinsicht-auswerten (Aktensichtung) und normenkontrollantrag-schriftsatz in anderen Plugins."
---

# Anlagen erstellen

## Aktuelle Rechtsprechung
- BSG, Urt. v. 25.06.2020 - B 9 SB 2/19 R, SozR 4-3250 § 69 Nr. 26 Rn. 14 — Beweisangebote und Anlagen im Sozialrechtsstreit: Kläger muss Beweismittel konkret bezeichnen; Gericht ist nicht verpflichtet, vage bezeichnete Beweismittel selbst zu ermitteln; vollständige Anlagenvorlage erforderlich.
- BSG, Beschl. v. 28.10.2015 - B 13 R 291/15 B, BeckRS 2015, 74219 Rn. 11 — Vorlagepflicht bei Klage: fehlende Anlagen können durch das Gericht im Wege der Amtsermittlung (§ 103 SGG) beigezogen werden; Kläger sollte dennoch alle zugänglichen Belege mit der Klageschrift einreichen.
- BSG, Urt. v. 15.11.2012 - B 8 SO 17/11 R, SozR 4-3500 § 28 Nr. 7 Rn. 12 — Beweislast beim Kläger für anspruchsbegründende Tatsachen; gut strukturierte Anlage-Vorlage unterstützt prima-facie-Beweis.

## Konvention

| Verfahrensart | Sigel-Praefix |
|---|---|
| Klage zum Sozialgericht | `K1`, `K2`, ... |
| Widerspruch | `W1`, `W2`, ... |
| Eilantrag | `E1`, `E2`, ... |
| Beweisantrag im Verfahren | `B1`, `B2`, ... |
| Allgemeines Anlagenkonvolut | `A1`, `A2`, ... |

## Eingaben

- Schriftsatz im Entwurf (aus `widerspruch-formulieren` `klage-sozialgericht` `eilantrag-sozialrecht`).
- Originaldokumente (PDF Foto Scan).

## Ablauf

### 1. Anlagenliste erstellen

Pro Anlage:
- **Sigel** (K1 W1 ...)
- **Kurzbezeichnung** ("Bescheid des Jobcenters vom 12.03.2026")
- **Quelle** (Mandant Behörde Drittstelle)
- **Datum** des Originaldokuments
- **Seitenzahl** im Original
- **Fundstelle im Schriftsatz** (z. B. "Seite 4 Randnummer 12")

### 2. PDF-Anlagen vorbereiten

- Original als PDF ablegen.
- Stempel oben rechts auf erste Seite jeder Anlage: das Sigel (`K1`).
- Doppelseitige Scans prüfen.
- Persönliche Daten Dritter schwaerzen wenn nicht erforderlich (DSGVO Datenminimierung).

### 3. Anlagenverzeichnis als Vorblatt

Vorblatt zur Klage- oder Widerspruchsakte:

```
Anlagenverzeichnis

K1   Bescheid des Jobcenters XYZ vom 12.03.2026
K2   Widerspruch vom 05.04.2026
K3   Widerspruchsbescheid vom 18.07.2026
K4   Schwerbehindertenausweis vom 14.11.2024 (GdB 70)
K5   Aerztliches Attest Dr. M. vom 03.02.2026
K6   Mietvertrag mit Anlagen
```

### 4. Vollständigkeitsprüfung

- Wird jede Anlage im Schriftsatz zitiert? Andernfalls Anlage streichen oder Schriftsatz ergänzen.
- Wird jedes Sigel im Schriftsatz auf das richtige Anlagedokument verweisen?
- Reichen die Anlagen aus um die Behauptungen glaubhaft zu machen / zu beweisen?

### 5. Anlagenkonvolut zusammenstellen

- Alle Anlagen in Reihenfolge K1 K2 K3 ... in eine PDF-Datei.
- Lesezeichen pro Anlage für schnelle Navigation.
- Endgültige Dateibenennung: `klage-anlagen-<az>-<datum>.pdf`.

## Ausgabe

- `anlagenverzeichnis-<az>.md`
- `anlagenkonvolut-<az>.pdf` mit Lesezeichen und Sigel-Stempeln
- Eintrag im Postausgang verlinkt mit dem Schriftsatz

## Versand

Vor Versand der Skill `versand-vor-check` aus dem Plugin `kanzlei-allgemein`.
