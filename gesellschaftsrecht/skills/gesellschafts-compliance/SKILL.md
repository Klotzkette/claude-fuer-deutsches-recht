---
name: gesellschafts-compliance
description: >
  Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht,
  Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml
  aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger
  und Rechtsordnung und zeigt auf, was in den nächsten 30/60/90 Tagen fällig ist.
  Trigger: „Gesellschafts-Compliance", „Einreichungsfristen", „Bilanzpublizität",
  „Transparenzregister", „Jahresabschluss einreichen", „was ist fällig".
language: de
triggers:
  - "Gesellschafts-Compliance"
  - "Einreichungsfristen"
  - "Bilanzpublizität"
  - "Transparenzregister"
  - "Jahresabschluss"
  - "Handelsregisterpflicht"
---

# Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)

## Zweck

Jahresabschluss-Einreichungen, Handelsregisterpflichten, Transparenzregister-Meldungen, Gesellschafterlisten – jede Gesellschaft in jeder Rechtsordnung hat ihren eigenen Zeitplan und eigene Konsequenzen bei Fristversäumnis. Dieser Skill pflegt einen einzigen YAML-Tracker, der weiß, was fällig ist, wann und für welche Gesellschaft.

## Rechtlicher Rahmen

- **Bilanzpublizität:** § 325 HGB – Jahresabschluss + Lagebericht beim Betreiber des Bundesanzeigers (Unternehmensregister) einzureichen; Frist: spätestens 12 Monate nach Ende des Geschäftsjahres (§ 325 Abs. 1a HGB). Ordnungsgeldverfahren nach § 335 HGB bei Verstoß (Bundesamt für Justiz).
- **Gesellschafterliste:** § 40 GmbHG – Notare und in bestimmten Fällen Geschäftsführer haben aktualisierte Gesellschafterliste zum Handelsregister einzureichen. Frist: unverzüglich nach jeder Änderung.
- **Transparenzregister:** §§ 18 ff. GwG – Eintragung wirtschaftlich Berechtigter (§ 3 GwG); § 20 GwG: Mitteilungspflicht der Vereinigung; Frist: 2 Wochen nach Änderung. Ausnahme: Meldung entbehrlich bei Eintragung im Handelsregister (§ 20 Abs. 2 GwG); seit 01.08.2021 kein vollständiges Transparenzregister mehr für alle.
- **Handelsregisteranmeldungen:** § 12 HGB (notarielle Beglaubigung); §§ 7 ff. HGB (Anmeldung GmbH), §§ 36 ff. AktG (Anmeldung AG).
- **Jahresabschlussprüfung:** § 316 HGB – Pflicht für mittelgroße und große Kapitalgesellschaften (Schwellen § 267 HGB).
- **Offenlegungspflicht Konzern:** §§ 290 ff. HGB – Konzernabschluss und Konzernlagebericht; § 325a HGB bei Tochterunternehmen ausländischer Muttergesellschaften.

## Wichtiger Hinweis zu Fristen

> Die Einreichungsfristen in diesem Skill spiegeln öffentlich verfügbare Anforderungen wider. Fristen und Anforderungen können sich ändern. **Fristen immer mit dem Bundesamt für Justiz (§ 335 HGB), dem Handelsregister oder dem Transparenzregister direkt bestätigen, bevor sie für Compliance-Zwecke verwendet werden.** `[Modellwissen — prüfen]`

## Tracker-Datei

Unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/gesellschaften/compliance-tracker.yaml`. Struktur:

```yaml
# Gesellschafts-Compliance-Tracker
# Erstellt: [Datum]
# Zuletzt aktualisiert: [Datum]
# Hinweis: Fristen sind nur Referenz – beim Bundesanzeiger/HR/TR bestätigen

metadaten:
  unternehmen: "[Unternehmensname]"
  erstellt: "[Datum]"
  zuletzt_aktualisiert: "[Datum]"
  letztes_audit: "[Datum oder null]"

gesellschaften:
  - name: "[Gesellschaftsname]"
    typ: "[GmbH / AG / GmbH & Co. KG / OHG / GbR]"
    handelsregisternummer: "[HRB/HRA-Nummer oder null]"
    registergericht: "[z. B. Amtsgericht München]"
    gruendungsdatum: "[Datum oder null]"
    status: "[aktiv / ruhend / in Auflösung]"
    groessenklasse: "[klein § 267 Abs. 1 HGB / mittelgroß § 267 Abs. 2 / groß § 267 Abs. 3]"
    geschaeftsjahr_ende: "[MM-DD, z. B. 12-31]"
    abschlusspruefung_pflicht: "[ja / nein / unbekannt]"
    gesellschafter_liste_aktuell: "[Datum letzte Einreichung oder null]"
    notizen: ""

    pflichten:
      - typ: "[Jahresabschluss § 325 HGB / Gesellschafterliste § 40 GmbHG / Transparenzregister § 20 GwG / Handelsregisteranmeldung / sonstig]"
        faellig: "[JJJJ-MM-TT]"
        faelligkeits_grundlage: "[GJ-Ende + 12 Monate / unverzüglich nach Änderung / andere]"
        zuletzt_eingereicht: "[Datum oder null]"
        status: "[aktuell / bald_fällig / überfällig / unbekannt]"
        notizen: ""
```

Status-Werte:
- `aktuell` – eingereicht für laufende Periode; nichts fällig in 90 Tagen
- `bald_fällig` – fällig innerhalb von 90 Tagen
- `überfällig` – Fälligkeitsdatum überschritten ohne eingetragenes Einreichungsdatum
- `unbekannt` – keine Information; manuelle Bestätigung erforderlich

---

## Modus 1: Initialisierung

Ohne Tracker oder mit `--rebuild`.

### Schritt 1: Gesellschaftstabelle laden

Aus Praxisprofil `## Gesellschafts-Compliance` → Gesellschaftstabelle. Falls vorhanden: direkt verwenden. Falls nicht: Nutzer bitten, Kaltstart-Modul auszuführen oder Gesellschaftsliste bereitzustellen.

### Schritt 2: Für jede Gesellschaft Pflichten ermitteln

**GmbH – Standardpflichten:**

| Pflicht | Norm | Frist | Konsequenz bei Verstoß |
|---|---|---|---|
| Jahresabschluss Offenlegung | § 325 Abs. 1 HGB | 12 Monate nach GJ-Ende | Ordnungsgeld BfJ § 335 HGB (mind. 2.500 EUR) |
| Gesellschafterliste | § 40 GmbHG | Unverzüglich nach Änderung | Gutgläubiger Erwerb nach § 16 Abs. 3 GmbHG riskiert |
| Transparenzregister | § 20 GwG | 2 Wochen nach Änderung | Bußgeld §§ 56 f. GwG |
| Jahresabschlussprüfung | § 316 HGB | Vor Offenlegung (mittelgroß/groß) | Strafbarkeit § 331 HGB; keine Testierung |

**AG – Standardpflichten:**

| Pflicht | Norm | Frist |
|---|---|---|
| Jahresabschluss Offenlegung | § 325 HGB | 12 Monate nach GJ-Ende |
| Prüfpflicht | § 316 HGB | Alle AG (keine Größenausnahme) |
| Bekanntmachung im Bundesanzeiger | § 325 Abs. 2 HGB | Mit Einreichung |
| Hauptversammlung | § 175 AktG | Binnen 8 Monaten nach GJ-Ende |
| Transparenzregister | § 20 GwG | 2 Wochen nach Änderung |

**Wichtige Größenklassen (§ 267 HGB; Werte ab Bilanzrechtsmodernisierungsgesetz; `[Modellwissen — prüfen]`):**

| Klasse | Bilanzsumme | Umsatzerlöse | Arbeitnehmer |
|---|---|---|---|
| Klein | ≤ 7,5 Mio. EUR | ≤ 15 Mio. EUR | ≤ 50 |
| Mittelgroß | ≤ 25 Mio. EUR | ≤ 50 Mio. EUR | ≤ 250 |
| Groß | > 25 Mio. EUR | > 50 Mio. EUR | > 250 |

Zwei von drei Merkmalen müssen zutreffen.

### Schritt 3: Tracker schreiben

Compliance-Tracker mit allen Gesellschaften und berechneten Pflichten generieren. Anfangsstatus setzen:
- `aktuell` wenn zuletzt_eingereicht innerhalb der laufenden Periode
- `bald_fällig` wenn fällig innerhalb 90 Tagen ohne Einreichung
- `überfällig` wenn Fälligkeitsdatum überschritten ohne Einreichung
- `unbekannt` wenn Gründungsdatum fehlt oder Pflicht unklar

---

## Modus 2: Bericht

```
/gesellschaftsrecht:gesellschafts-compliance --bericht [--tage 30|60|90|180]
```

```
GESELLSCHAFTS-COMPLIANCE-BERICHT — [Datum]
[Unternehmensname]

🔴 ÜBERFÄLLIG ([N]):
  [Gesellschaft] / [Pflicht] — war fällig am [Datum]

⏰ FÄLLIG INNERHALB [N] TAGE ([N]):
  [Gesellschaft] / [Pflicht] — fällig [Datum]

✅ KÜRZLICH EINGEREICHT ([N] in letzten 90 Tagen):
  [Gesellschaft] / [Pflicht] — eingereicht [Datum]

❓ UNBEKANNTER STATUS ([N]):
  [Gesellschaft] / [Pflicht] — keine Information; direkt beim Registerführer bestätigen

TRANSPARENZREGISTER:
  Zuletzt geprüft: [Datum]
  Gesellschaften mit aktueller Eintragung: [N] von [N]
  Gesellschaften ohne Prüfung in letzten 12 Monaten: [Liste]
```

---

## Modus 3: Update

### Folgenreiche-Handlung-Sperre (Einreichung)

Falls Rolle **Nichtjurist**:
> Eine Jahresabschluss-Einreichung beim Bundesanzeiger oder eine Handelsregistereintragung hat rechtliche Konsequenzen. Vor Einreichung mit einem Rechtsanwalt oder Steuerberater besprechen. `[Prüfen]`

### 3a: Manuelles Update

```
/gesellschaftsrecht:gesellschafts-compliance --update
```

Anwalt teilt mit, was eingereicht wurde:
> „Jahresabschluss der Alpha GmbH zum 31.12.2024 am 05.03.2025 beim Bundesanzeiger eingereicht."

### 3b: Massen-Update (Wirtschaftsprüfer-Bericht)

Nutzer lädt Wirtschaftsprüfer-Bericht oder HR-Auszug hoch. Matching-Gesellschaften aktualisieren.

---

## Modus 4: Gesundheits-Audit

```
/gesellschaftsrecht:gesellschafts-compliance --audit
```

Über Einreichungsstatus hinaus:

**Einreichungs-Compliance:** Überfällige und unbekannte Punkte.

**Gesellschaftsgesundheit:**
- `ruhend`-Gesellschaften: Soll aufgelöst werden? Tragekosten (Registergebühren, Steuer, RA-Honorar).
- Fehlende Gründungsdaten.
- Gesellschafterliste nicht aktuell (§ 40 GmbHG): Risiko für gutgläubigen Erwerb § 16 Abs. 3 GmbHG.

**Transparenzregister-Lücken:**
- Gesellschaften ohne Transparenzregister-Eintragung oder -Befreiung prüfen (§ 20 Abs. 2 GwG bei HR-Eintragung)
- Änderungen an wirtschaftlich Berechtigten nicht gemeldet?

**Bilanzpublizitäts-Lücken:**
- Gesellschaften, bei denen Offenlegung >12 Monate zurückliegt: Ordnungsgeldgefahr.
- Prüfungspflicht nach § 316 HGB für neue mittelgroße/große Gesellschaften?

**Konzern-Pflichten:**
- § 290 HGB-Konzernabschluss: Muttergesellschaft prüfen.
- § 325a HGB: Ausländische Tochtergesellschaften, die einen deutschen Jahresabschluss einreichen müssen?

```
GESELLSCHAFTS-GESUNDHEITS-AUDIT — [Datum]

EINREICHUNGS-COMPLIANCE
  Überfällig: [N]
  Unbekannter Status: [N]
  Handlungsempfehlung: --sweep ausführen

RUHENDE GESELLSCHAFTEN ([N])
  [Liste mit Alter und jährlichen Tragekosten falls bekannt]
  Auflösungskandidaten (>5 Jahre ruhend): [Liste]

TRANSPARENZREGISTER
  Nicht eingetragen / geprüft: [N] Gesellschaften
  Zuletzt geändert, aber nicht gemeldet: [N] Gesellschaften

BILANZPUBLIZITÄT § 325 HGB
  Überfällig (>12 Monate): [N] Gesellschaften
  Ordnungsgeldgefahr BfJ: [Liste]

EMPFOHLENE MASSNAHMEN
  1. [Höchste Priorität]
  2. [etc.]
```

---

## Modus 5: Export

```
/gesellschaftsrecht:gesellschafts-compliance --export [--format csv|tabelle]
```

CSV-Spalten:
`Gesellschaftsname, Typ, HR-Nummer, Registergericht, Gründungsdatum, Status, Größenklasse, GJ-Ende, Pflicht, Fällig, Zuletzt eingereicht, Notizen`

---

## Quellen und Zitierweise

- § 325 HGB (Bilanzpublizität; Offenlegungspflicht)
- § 335 HGB (Ordnungsgeldverfahren Bundesamt für Justiz)
- § 40 GmbHG (Gesellschafterliste)
- §§ 18 ff., 20 GwG (Transparenzregister)
- § 267 HGB (Größenklassen)
- § 316 HGB (Prüfungspflicht)
- § 16 Abs. 3 GmbHG (Gutgläubiger Erwerb)

Zitierweise nach `../../references/zitierweise.md`.

Kommentarliteratur:
- MüKoHGB/Störk/Leuz, 4. Aufl. 2020, § 325 Rn. 5 ff. (Bilanzpublizität).
- Scholz, GmbHG, 12. Aufl. 2018, § 40 Rn. 3 ff. (Gesellschafterliste).
- BGH, Urt. v. 02.07.2019 – II ZR 406/17, NJW 2019, 2774 (gutgläubiger Erwerb bei unrichtiger Gesellschafterliste).

## Was dieser Skill nicht tut

- Er reicht keine Dokumente ein. Ausgabe ist Tracker und Aufgabenliste; Einreichung erfolgt durch Anwalt/Steuerberater.
- Er ruft keine Registerauszüge ab; er verfolgt, wann sie zuletzt bestätigt wurden.
- Er bestimmt nicht, ob eine Konzernabschluss-Pflicht besteht – das erfordert eine Analyse der tatsächlichen Konzernverhältnisse.
- Er ersetzt keine Steuerberatung (§ 316 HGB-Prüfung = Steuerberater/Wirtschaftsprüfer).
