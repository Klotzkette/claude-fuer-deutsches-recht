---
name: cold-start-interview
description: >
  Führt das Erstgespräch zur Mandatsaufnahme im Vertragsrecht durch und schreibt
  das Kanzlei- bzw. Mandatsprofil. Lädt beim ersten Einsatz des Plugins, wenn
  die Konfigurationsdatei noch Platzhalter enthält oder wenn der Nutzer
  „Plugin einrichten", „Profil erstellen", „Erstgespräch starten" oder
  „Vertragsmandat aufnehmen" sagt.
language: de
triggers:
  - "Plugin einrichten"
  - "Erstgespräch"
  - "Mandatsaufnahme"
  - "Profil erstellen"
  - "Vertragsrecht konfigurieren"
  - "Kanzleiprofil"
  - "Playbook erstellen"
  - "Neueinrichtung"
---

# Erstgespräch Vertragsrecht — Mandatsaufnahme

## Zweck

Diese Skill führt das strukturierte Erstgespräch, um die konkrete Vertragspraxis
der Kanzlei oder Rechtsabteilung zu erfassen und in ein lebendes Kanzleiprofil
zu schreiben. Jede andere Skill des Plugins liest dieses Profil, bevor sie
tätig wird. Ohne ausgefülltes Profil arbeiten alle anderen Skills mit
Standardwerten — das Erstgespräch ist der Hebel, der die Ausgaben von
„generisch" auf „so wie Ihre Kanzlei arbeitet" verschiebt.

Lädt beim ersten Einsatz des Plugins oder wenn `--redo` übergeben wird.

## Eingaben

- Angaben zum Anwalt/zur Anwältin: Rolle, Kanzleigröße, Tätigkeitsschwerpunkt
- Vertragsvolumen und -mix (Lieferantenverträge, Dienstleistungsverträge,
  Lizenzverträge, AGB-basierte Massenverträge etc.)
- Mandatseite: Auftraggeber-Seite (Unternehmer/Verwender) oder
  Auftragnehmer-Seite (Vertragspartner/Verbraucher)
- Verhandlungsstil und Eskalationsmatrix
- 5–20 bereits unterzeichnete Musterverträge als Referenz (optional, aber
  dringend empfohlen)

## Rechtlicher Rahmen

### Kernvorschriften

**BGB Schuldrecht Allgemeiner Teil:**
- §§ 241 ff. BGB — Pflichten aus dem Schuldverhältnis
- §§ 280 ff. BGB — Schadensersatz wegen Pflichtverletzung
- §§ 305–310 BGB — Allgemeine Geschäftsbedingungen (AGB-Recht)
- §§ 311 ff. BGB — Rechtsgeschäftliche Schuldverhältnisse, culpa in contrahendo
- §§ 312 ff. BGB — Verbraucherverträge, Widerrufsrecht

**BGB Schuldrecht Besonderer Teil:**
- §§ 433 ff. BGB — Kaufvertrag
- §§ 437, 439 ff. BGB — Gewährleistung beim Kauf
- §§ 535 ff. BGB — Mietvertrag
- §§ 611 ff. BGB — Dienstvertrag
- §§ 631 ff. BGB — Werkvertrag; §§ 634 ff. BGB — Mängelrechte beim Werkvertrag
- §§ 650a ff. BGB — Bauvertrag

**AGB-Kontrolle:**
- § 305 BGB — Einbeziehung von AGB
- § 305c BGB — Überraschende und mehrdeutige Klauseln
- § 306 BGB — Rechtsfolgen bei Nichteinbeziehung und Unwirksamkeit
- § 307 BGB — Inhaltskontrolle, Transparenzgebot
- §§ 308, 309 BGB — Klauselverbote mit und ohne Wertungsmöglichkeit
- § 310 BGB — Anwendungsbereich (B2B vs. B2C)

### Leitentscheidungen

- BGH, Urt. v. 19.11.2019 – XI ZR 9/18, NJW 2020, 461 Rn. 22 ff.
  (Transparenzgebot bei Zinsklauseln in AGB)
- BGH, Urt. v. 25.10.2016 – VI ZR 516/15, NJW 2017, 1104 Rn. 14
  (Haftungsbeschränkung in AGB; Inhaltskontrolle § 307 BGB)
- BGH, Urt. v. 29.06.2011 – VIII ZR 212/08, BGHZ 190, 115 Rn. 20 ff.
  (Einbeziehung von AGB im unternehmerischen Verkehr; § 305 Abs. 2 BGB)
- BGH, Urt. v. 09.04.2014 – VIII ZR 404/12, NJW 2014, 2100 Rn. 30
  (Überraschungsklausel § 305c BGB; Leitentscheidung zur Klauselkontrolle)

### Kommentarliteratur

- Palandt/Grüneberg, BGB, 83. Aufl. 2024, § 305 Rn. 3 ff. (Einbeziehungsvoraussetzungen AGB)
- MüKoBGB/Wurmnest, 9. Aufl. 2022, § 307 Rn. 1 ff. (Inhaltskontrolle, Transparenzgebot)
- Wolf/Lindacher/Pfeiffer, AGB-Recht, 7. Aufl. 2020, § 307 BGB Rn. 100 ff. (Generalklausel)
- Staudinger/Coester-Waltjen, BGB, Neubearbeitung 2022, § 307 Rn. 200 ff.

## Ablauf

### Schritt 0 — Vorabprüfung Konfigurationsstatus

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`:

- **Existiert nicht** → Erstgespräch starten.
- **Enthält `[PLATZHALTER]` oder `[Kanzleiname]`** → Vorlage unvollständig;
  Erstgespräch starten oder fortsetzen.
- **Enthält `<!-- EINRICHTUNG PAUSIERT BEI: -->`** → Nutzer begrüßen und
  Wiederaufnahme an der gespeicherten Stelle anbieten.
- **Vollständig ausgefüllt (keine Platzhalter)** → bereits konfiguriert;
  nur mit `--redo` neu starten.

### Schritt 1 — Einleitung (2 Minuten)

Zeige diese Kurzorientierung — nicht länger als 4 Zeilen:

> **Dieses Plugin unterstützt die Vertragspraxis** — Prüfung, Verhandlung und
> Verwaltung von Verträgen nach deutschem Recht (BGB Schuldrecht, AGB-Recht,
> Verbraucherrecht, Gewährleistung, Schadensersatz). Kein anderes Rechtsgebiet?
> Wählen Sie ein anderes Plugin.
>
> **2 Minuten** ergeben Rolle, Kanzleisetting, Mandatsschwerpunkt und eine
> funktionierende Standardkonfiguration. **15 Minuten** fügen echte
> Verhandlungspositionen, Eskalationsmatrix, AGB-Klauseln und Referenzverträge
> hinzu.
>
> Kurz oder vollständig?

### Schritt 2 — Nutzerprofil

**Wer nutzt dieses Plugin?**

> 1. **Rechtsanwalt/in, Syndikusrechtsanwalt/in oder juristischer
>    Mitarbeiter/Mitarbeiterin** unter anwaltlicher Aufsicht
> 2. **Nichtjurist/in mit Anwaltszugang** (Geschäftsführer, Einkauf,
>    Vertragsmanager) — hat einen Anwalt zur Rücksprache
> 3. **Nichtjurist/in ohne regelmäßigen Anwaltszugang**

Bei Wahl 2 oder 3: Ausgaben werden als Recherchegrundlage zur anwaltlichen
Überprüfung formuliert, nicht als abschließende Rechtswertung.

**Kanzlei-/Unternehmenssetting:**
- Einzelkanzlei / Kleinkanzlei (keine Hierarchie)
- Mittelgroße oder große Kanzlei
- Rechtsabteilung (In-house / Syndikusrechtsanwalt)
- Sonstig — bitte beschreiben

### Schritt 3 — Das Mandat (2–3 Minuten)

**Was tut Ihr Unternehmen / Ihre Kanzlei?**
Kurzbeschreibung oder Link zur Website genügt.

**Wer sind Sie?**
- Kanzlei-/Unternehmensname und Rechtsform
- Größe des juristischen Teams
- Wer hat die letzte Entscheidungsverantwortung (GF, Partner, GC)?

**Was kommt herein?**
- Ungefähres Aufkommen: 10 Verträge/Monat? 100?
- Mix: hauptsächlich Lieferantenverträge? Dienstleistungsverträge?
  Lizenzverträge? AGB-basierte Massenverträge? Alles davon?
- Wer stellt typischerweise den Vertragsentwurf? Sie (eigenes Muster), die
  Gegenseite oder gemischt?

**Mandatseite:**
> Auf welche Seite kalibriere ich Ihr Verhandlungs-Playbook?
>
> - **Verwender-Seite** — Sie stellen AGB/Mustervertrag. Typisch für
>   Lieferanten, Dienstleister, Software-Anbieter.
> - **Kunden-Seite** — Sie akzeptieren oder verhandeln fremde AGB/Verträge.
>   Typisch für Einkauf, Auftraggeber.
> - **Beide Seiten.**

### Schritt 4 — Verhandlungs-Playbook (3–4 Minuten)

Vor den Fragen: Haben Sie bereits ein Verhandlungshandbuch, eine
Klauselliste oder Fallback-Positionen-Dokument? Wenn ja, teilen Sie es;
ich lese es und frage nur nach den Lücken.

**Haftungsbeschränkung (§§ 309 Nr. 7, 307 BGB):**
- Ihre Standardposition? (z. B. Haftung auf grobe Fahrlässigkeit/Vorsatz
  beschränkt, oder Jahresvergütung als Cap)
- Welche Carve-outs akzeptieren Sie? (Verletzung von Leben/Körper/Gesundheit
  ist nach § 309 Nr. 7 lit. a BGB zwingend, Vorsatz/grobe Fahrlässigkeit
  nach § 309 Nr. 7 lit. b BGB)
- Wo ziehen Sie die Grenze?

**Gewährleistung (§§ 437 ff. BGB, 634 ff. BGB):**
- Verkürzung der gesetzlichen Verjährungsfrist (§ 438 BGB: 2 Jahre;
  aber § 309 Nr. 8 BGB beachten)?
- Welche Nacherfüllungsrechte räumen Sie ein?
- Schadensersatz statt der Leistung: Wann akzeptieren Sie Ausschluss?

**Datenschutz (DSGVO/BDSG):**
- Eigener Standardauftragsdatenverarbeitungsvertrag (AVV gemäß Art. 28 DSGVO)
  oder Übernahme des AVV der Gegenseite?
- Subunternehmer-Genehmigungsrechte: Blockierende Zustimmung oder nur
  Benachrichtigung?
- Datenlöschung nach Vertragsende: Frist und Nachweis?

**Laufzeit und Kündigung:**
- Ordentliche Kündigung: Welche Mindestfrist ist für Sie akzeptabel?
- Automatische Verlängerung: Welche maximale Ankündigungsfrist zum Kündigen
  akzeptieren Sie?
- Vertragsstrafe (§ 339 BGB): Grundsätzlich nein, oder unter welchen
  Bedingungen?

**Gerichtsstand und anwendbares Recht:**
- Bevorzugt? Akzeptabel? Nie?

**Das eine Dealbreaker-Kriterium:**
- Wenn ein Vertrag genau ein Problem hat, das Sie zum Ablehnen bewegt,
  was ist es?

### Schritt 5 — Eskalationsmatrix (1–2 Minuten)

Haben Sie eine Eskalationsmatrix, Zeichnungsbefugnisregelung oder
Delegationsrahmen? Wenn ja, teilen; ich lese und frage nur nach Lücken.

- Wer kann was bis zu welchem Schwellenwert genehmigen?
- Was eskaliert automatisch unabhängig vom Wert? (z. B. unbeschränkte Haftung,
  IP-Abtretung an Gegenseite)
- Wie wird eskaliert — E-Mail, Slack, Jour fixe?

### Schritt 6 — Referenzverträge

> Wo liegen Ihre unterzeichneten Verträge? (Vertragsmanagement-System,
> SharePoint, lokale Ablage?) Das bestimmt, ob das Plugin automatisch
> auf Laufzeitdaten zugreifen kann.

Bitten Sie um 5–10 unterzeichnete Verträge (20 ergibt klarere Muster).
Lesen Sie Musterverträge zuerst (Ausgangspositionen), dann unterzeichnete
Verträge (tatsächlich vereinbarte Positionen). Das Delta ist das echte
Playbook.

### Schritt 7 — Kanzleiprofil schreiben

Schreiben Sie das Profil nach folgender Struktur (Prosatext mit Tabellen, 
kein YAML, direkt editierbar):

```markdown
# Kanzleiprofil Vertragsrecht

*Erstellt vom Erstgespräch am [DATUM]. Diese Datei direkt bearbeiten —
jede Skill des Plugins liest sie vor jeder Aktion. Korrekturen hier
wirken sich sofort auf alle Ausgaben aus.*

---

## Wir sind

[Kanzlei-/Unternehmensname] ist eine [Rechtsform]. Das juristische Team
umfasst [N] Personen: [Namen/Rollen]. [Name] ist letzte Entscheidungsinstanz.
Wir bearbeiten monatlich ca. [N] Verträge, überwiegend [Mix]. Wir nutzen
[System] für die Vertragsverwaltung.

**Was belastet uns:** [In den Worten des Nutzers]

---

## Nutzerprofil

**Rolle:** [Rechtsanwalt/in / Syndikusrechtsanwalt/in / Nichtjurist/in mit
Anwaltszugang / Nichtjurist/in ohne Anwaltszugang]
**Anwaltskontakt:** [Name / Team / externe Sozietät / entfällt]

---

## Integrationen

| Integration | Status | Fallback bei Fehlen |
|---|---|---|
| Vertragsmanagement (CLM) | [✓ / ✗] | Manuelle Führung; Fristen-Tracker läuft gegen lokales Register |
| E-Signatur | [✓ / ✗] | Unterzeichnung außerhalb des Plugins |
| Dokumentenablage (SharePoint / Drive) | [✓ / ✗] | Nutzer lädt Verträge direkt hoch |
| Slack | [✓ / ✗] | Hinweise werden inline ausgegeben |

---

## Verhandlungs-Playbook

**Aktive Seite:** [Verwender / Kunden-Seite / beide]

### Verwender-Seite (eigenes Muster / eigene AGB)

#### Haftungsbeschränkung

**Standardposition:** [z. B. Haftung auf grobe Fahrlässigkeit/Vorsatz]
**Akzeptable Fallback-Positionen:** [was unterzeichnete Verträge zeigen]
**Niemals:** [absolute Grenzen]
**Carve-outs:** [zwingend nach § 309 Nr. 7 BGB: Leben/Körper/Gesundheit]

#### Gewährleistung

[Gleiche Struktur]

#### Datenschutz / AVV

[Gleiche Struktur]

#### Laufzeit und Kündigung

[Gleiche Struktur]

#### Gerichtsstand und Recht

**Bevorzugt:** [Liste]
**Akzeptabel:** [Liste]
**Eskalieren:** [Liste]
**Nie:** [Liste]

#### Der Dealbreaker

[Was der Nutzer genannt hat — erste Prüfung bei jeder Vertragsanalyse]

---

### Kunden-Seite (fremdes Muster / fremde AGB)

*[Falls noch nicht konfiguriert: Hinweis, dass `/vertragsrecht:cold-start-interview --side auftraggeber` auszuführen ist.]*

[Gleiche Unterstruktur, kalibriert auf Kunden-Seite: was akzeptieren wir
von Vertragspartnern]

---

## Eskalation

| Genehmigen kann | Bis zu | Eskalation an | Via |
|---|---|---|---|
| [Junior-Anwalt] | [Schwellenwert] | [Sie] | [E-Mail/Slack] |
| [Sie] | [Ihr Schwellenwert] | [GC/Partner] | [Kanal] |
| [GC/Partner] | [GC-Schwellenwert] | [Geschäftsführung] | [Kanal] |

**Automatische Eskalation unabhängig vom Wert:**
- [z. B. unbeschränkte Haftung]
- [z. B. IP-Abtretung an Gegenseite]
- [z. B. Änderung anwendbares Recht]

---

## Kanzleistil

**Ton in Redlines:** [sachlich-knapp / kooperativ / richtet sich nach Gegenseite]
**Stakeholder-Zusammenfassungen:** [wer liest sie? wie lang?]
**Wo Arbeitsergebnisse abgelegt werden:** [System/Ordner]
**Wo unterzeichnete Verträge liegen:** [System/Pfad]

---

## Ausgaben

**Arbeitsergebnis-Kennzeichnung** (wird jedem Prüfungsmemo, jeder Analyse
und jeder Zusammenfassung vorangestellt):

- Wenn Rolle Rechtsanwalt/in: `VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS —
  ERSTELLT UNTER ANWALTLICHER AUFSICHT`
- Wenn Nichtjurist/in: `RECHERCHENOTIZ — KEIN RECHTSGUTACHTEN —
  VOR JEDER RECHTSRELEVANTEN ENTSCHEIDUNG MIT EINEM ZUGELASSENEN RECHTSANWALT
  ABSTIMMEN`

---

## Geprüfte Referenzverträge

| Vertrag | Vertragspartner | Unterzeichnet | Erkenntnisse |
|---|---|---|---|
| [Dateiname] | [Name] | [Datum] | [Was gelernt wurde] |

---

## Prüfungseinstellungen

routing_bestaetigen: true   # Auf false setzen, um Routing-Bestätigung zu überspringen

---

## Playbook-Monitor-Einstellungen

muster_schwellenwert: 5
rueckblick_monate: 12
```

### Schritt 8 — Abschluss

Zeigen Sie eine Zusammenfassung und bieten Sie an:

- **Ersten Vertragstest:** „Möchten Sie einen Vertrag einreichen, um zu
  sehen, wie das Playbook funktioniert?"
- **Hinweis auf Änderbarkeit:** „Das Profil ist eine Textdatei — direkt
  bearbeitbar. Einzelne Positionen ändern: `/vertragsrecht:customize`."

---

## Ausgabeformat

Das Kanzleiprofil ist ein Prosatext mit Tabellen — kein YAML, kein
Config-File. Der Anwalt soll es lesen und direkt editieren können.

Nach dem Schreiben: kurze Zusammenfassung dessen, was erfasst wurde, und
Angebot eines Erste-Schritte-Tests.

## Beispiel

**Szenario:** Kanzlei mit 3 Anwälten, schwerpunktmäßig IT-Dienstleistungsverträge
aus Verwender-Perspektive, ca. 30 Verträge/Monat, Standardpapier der Kanzlei.

Das Profil würde enthalten:
- Verwender-Seite als aktive Seite
- Haftungsbeschränkung: grobe Fahrlässigkeit/Vorsatz, Cap bei 12 Monatsvergütung
- Gewährleistung: Verjährung auf 1 Jahr verkürzt (§ 309 Nr. 8 lit. b BGB Grenze beachten)
- Gerichtsstand: Sitz der Kanzlei bevorzugt

## Risiken und typische Fehler

- **Kein Playbook ohne Referenzverträge schreiben.** Das Erstgespräch zeigt
  die behaupteten Positionen; die unterzeichneten Verträge zeigen die echten.
  Das Delta ist entscheidend.
- **AGB vs. Individualvertrag nicht vermischen.** § 310 Abs. 1 BGB schließt
  §§ 308, 309 BGB im B2B-Bereich nicht vollständig aus — auch dort gilt § 307
  BGB. Das Profil muss die typische Vertragssituation (B2B/B2C, AGB/Individualvertrag)
  festhalten.
- **Zwingend zulässige Carve-outs falsch eintragen.** § 309 Nr. 7 lit. a BGB
  verbietet Haftungsausschluss für Verletzung von Leben, Körper, Gesundheit —
  das ist kein verhandelbares Playbook-Element, sondern zwingendes Recht.
- **Eskalationsmatrix mit Lücken lassen.** Jede Lücke führt zu Standard-Eskalation
  — besser explizit als „nicht konfiguriert" markieren.
- **Erstgespräch bei jeder Sitzung neu starten.** Das Profil einmal schreiben,
  danach nur mit `--redo` neu befragen.

## Quellenpflicht

Jede Vertragsanalyse und jedes Playbook-Ergebnis muss Nachweise führen aus:

- Gesetzestexten (BGB, UWG, HGB, DSGVO/BDSG) mit konkretem Paragraphen
- BGH-Rechtsprechung in korrekter Zitierweise
  (z. B. BGH, Urt. v. 25.10.2016 – VI ZR 516/15, NJW 2017, 1104)
- Kommentarliteratur im Bearbeiterstil
  (z. B. Palandt/Grüneberg, BGB, 83. Aufl. 2024, § 307 Rn. 5)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
