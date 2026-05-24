---
name: anlagen-erstellen
description: Strukturiert Anlagen zu sozialrechtlichen Schriftsaetzen — Konvention K1 K2 K3 fuer Klage W1 W2 W3 fuer Widerspruch A1 A2 A3 fuer Anlagenkonvolut. Pro Anlage werden erfasst Sigel kurze Bezeichnung Quelle Datum Seitenzahl Bezug im Schriftsatz. Erzeugt Anlagenverzeichnis als Vorblatt und versieht jedes Originaldokument mit Anlagensigel im PDF (Stempel oben rechts). Prueft Vollstaendigkeit gegen den Schriftsatz — jede Anlage muss im Text zitiert sein.
---

# Anlagen erstellen

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

Vor Versand der Skill `versand-vor-check` aus dem Plugin `kanzlei-cowork`.
