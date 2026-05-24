---
name: erstantwort-generator
description: "Hauptskill: erstellt die formelle Erstantwort-E-Mail an einen potenziellen Mandanten. Enthaelt Dank fuer die Anfrage, exakte Anrede aus der Eingangsmail, Hinweis auf telefonische Terminvergabe, Bitte um Sachverhaltsschilderung per E-Mail, Hinweis auf den Transkriptionsservice mit DSGVO-Einwilligungserfordernis, Mandatsverhaeltnis-Disclaimer und Schlussformel. Laedt wenn der Nutzer 'Erstantwort schreiben', 'Antwortmail erstellen', 'Eingangsbestaetigung', 'Erstreaktion Mandant' oder 'Antwort auf Anfrage' sagt."
---

# Erstantwort-Generator

Dieser Hauptskill erstellt die vollständige formelle Erstantwort-E-Mail an einen potenziellen Mandanten. Er koordiniert alle Teilskills und fügt deren Output zu einem druckfertigen Schreiben zusammen.

## Ablauf (Koordination der Teil-Skills)

1. **Parsing:** Skill `anfrage-eingang-parser` läuft zuerst und liefert strukturierte Daten.
2. **Spam-Check:** Skill `spam-und-massen-anfrage-filter` — bei Spam: keine Antwort generieren, Aussortierungs-Flag setzen.
3. **Dringlichkeit:** Skill `dringlichkeitsmarker` — bei HOCH: sofortigen Anwaltsanruf priorisieren, Hinweis in der Mail einfügen.
4. **Anrede:** Skill `anrede-uebernehmen` — liefert die formelle Anredezeile.
5. **Sprache:** Skill `mehrsprachige-antwort` — bei nicht-deutschsprachiger Anfrage Sprachumschaltung.
6. **Mail-Aufbau:** Dieser Skill fügt alle Bausteine zusammen.
7. **CRM-Eintrag:** Skill `folgekorrespondenz-vorbereiten` wird parallel ausgelöst.

## Aufbau der Erstantwort-Mail

### Betreff

```
Re: [Original-Betreff der Eingangsmail]
```
oder falls kein Betreff vorhanden:
```
Ihre Anfrage an [KANZLEI-NAME] — Eingangsbestätigung
```

### Körper der Mail (Muster-Struktur)

```
[ANREDEZEILE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

[DRINGLICHKEITS-HINWEIS — nur wenn HOCH: Absatz einfügen, sonst weglassen]

Wir begleiten potenzielle Mandantinnen und Mandanten gern dabei, die richtigen
nächsten Schritte zu finden. Bitte beachten Sie, dass [MANDATSVERHAELTNIS-DISCLAIMER-KURZFORM].

Für eine erste Terminabsprache stehen wir Ihnen telefonisch zur Verfügung:

  Sekretariat: [SEKRETARIATS-TELEFON]
  Erreichbarkeit: [ERREICHBARKEITSZEITEN]

Um Ihren Fall bestmöglich vorzubereiten, bitten wir Sie, uns vorab Ihren
Sachverhalt in einer kurzen E-Mail zusammenzufassen:

  — Was ist der Kern Ihres Anliegens?
  — Wann hat das zugrunde liegende Ereignis stattgefunden?
  — Gibt es Fristen, Termine oder Bescheide, die wir kennen sollten?
  — Wer ist die Gegenseite (Person, Unternehmen, Behörde)?

[TRANSKRIPTIONS-ABSCHNITT — nur wenn Anfragende nicht schreiben kann/mag:]

Falls Ihnen eine schriftliche Schilderung schwerfällt, bieten wir Ihnen
einen automatisierten Transkriptionsservice an. Sie rufen dort an und schildern
Ihr Anliegen mündlich. Die Aufnahme wird automatisch verschriftlicht und uns
vertraulich übermittelt.

Wichtiger Hinweis zur Datenverarbeitung: [EINWILLIGUNGS-TEXT-KURZFORM]

Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

[/TRANSKRIPTIONS-ABSCHNITT]

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-TELEFON]
[KANZLEI-E-MAIL]

---
[MANDATSVERHAELTNIS-FUSSZEILE]
```

## Bausteine im Detail

### Dank-Formulierung

Standard: „vielen Dank für Ihre Anfrage, die uns heute zugegangen ist."

Varianten:
- Bei dringlicher Anfrage: „vielen Dank für Ihre Anfrage. Wir haben Ihr Anliegen als dringend zur Kenntnis genommen."
- Bei Empfehlung: „vielen Dank für Ihre Anfrage, die uns durch [Quelle, soweit genannt] zugegangen ist."

### Dringlichkeits-Hinweis (nur bei HOCH)

```
WICHTIG: Aus Ihrer Anfrage haben wir entnommen, dass möglicherweise eine
Frist oder ein Termin unmittelbar bevorsteht. Bitte rufen Sie uns
umgehend unter [SEKRETARIATS-TELEFON] an, damit wir die Situation sofort
einschätzen können. Warten Sie bitte nicht auf eine schriftliche Rückmeldung.
```

### Telefonische Terminvergabe

Pflichtbestandteil. Enthält:
- Telefonnummer des Sekretariats (aus Skill `telefon-konfiguration`)
- Erreichbarkeitszeiten (aus `kanzlei.json`)

### Bitte um Sachverhaltszusammenfassung

Formular-Fragen (s. oben). Alternativ freie Formulierung:
„Bitte schildern Sie uns Ihr Anliegen in einigen Sätzen — Datum des Ereignisses, beteiligte Parteien, bestehende Fristen und Ihr Ziel."

### Transkriptionsservice-Hinweis

Nur einfügen wenn:
- Die anfragende Person explizit schreibt, dass sie nicht schreiben kann/mag, oder
- Die Sekretariatsmitarbeiterin den Modus manuell aktiviert.

Enthält: Telefonnummer des Transkriptionsservices, kurze Ablauferklärung, DSGVO-Einwilligungshinweis in Kurzform (Langform aus Skill `einwilligung-hinweis-datenschutz`).

### Mandatsverhältnis-Disclaimer

Kurzform in der Mail: „Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis begründet und keine Rechtsberatung darstellt."

Langform in der Fußzeile: aus Skill `mandatsverhaeltnis-hinweis`.

### Schlussformel

Standard: „Mit freundlichen Grüßen"

Varianten bei Sprache:
- Englisch: „Yours sincerely," / „Kind regards,"
- Französisch: „Veuillez agréer l'expression de mes salutations distinguées,"
- Italienisch: „Distinti saluti,"

## Ausgabe

Der Skill gibt die fertige E-Mail als formatierten Text aus, bereit zum Kopieren in das E-Mail-Programm des Sekretariats. Zusätzlich:
- Interne Zusammenfassung der getroffenen Entscheidungen (welche Heuristiken, welche Abschnitte eingefügt/weggelassen)
- Hinweis auf ausstehende manuelle Prüfungen (z. B. wenn Name nicht ermittelbar war)

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datengrundlage
- `anrede-uebernehmen` — Anredezeile
- `telefon-konfiguration` — Telefonnummern
- `transkriptionsdienst-erklaerung` — Transkriptions-Abschnitt
- `einwilligung-hinweis-datenschutz` — DSGVO-Einwilligung
- `mandatsverhaeltnis-hinweis` — Disclaimer
- `dringlichkeitsmarker` — Dringlichkeits-Hinweis
- `spam-und-massen-anfrage-filter` — Vor-Filterung
- `folgekorrespondenz-vorbereiten` — CRM-Eintrag parallel
- `mehrsprachige-antwort` — Sprache der Antwort
- `muster-erstantwort` — Vorlagenschreiben als Referenz
