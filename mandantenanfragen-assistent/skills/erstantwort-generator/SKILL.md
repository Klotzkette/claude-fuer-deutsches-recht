---
name: erstantwort-generator
description: "Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Pruefraster: Dank fuer Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung Mandatsverhaeltnis-Disclaimer Schlussformel. Output: fertige Erstantwort-E-Mail mit allen Pflichthinweisen. Abgrenzung zu muster-erstantwort (Template-Vorlage) und anrede-uebernehmen."
---

# Erstantwort-Generator

Dieser Hauptskill erstellt die vollständige formelle Erstantwort-E-Mail an einen potenziellen Mandanten. Er koordiniert alle Teilskills und fügt deren Output zu einem druckfertigen Schreiben zusammen.


## Triage zu Beginn
1. Sind alle Teil-Skills bereits ausgefuehrt (Parsing, Spam-Check, Dringlichkeit, Anrede, Sprache)?
2. Welche Dringlichkeitsstufe wurde gesetzt — bei HOCH Sofortruf-Hinweis in der Mail einfuegen?
3. Besteht bereits ein Mandatsverhältnis oder handelt es sich um eine Erstanfrage (Kein-Mandat-Disclaimer erforderlich)?
4. Soll der Transkriptionsservice-Hinweis aktiviert werden (Trigger: Anfrage ist kurz/fragmentarisch oder Nutzer kann nicht schreiben)?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Pflicht zur Eingangsbestaetigung innerhalb angemessener Zeit; verzoegertes Antworten kann als Ablehnung gewertet werden und Vertrauensschaeden ausloesen.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Kostenbelehrung nach § 49b Abs. 5 BRAO muss vor oder mit Mandatsannahme erteilt werden; Erstantwort ist guter Zeitpunkt fuer diesen Hinweis.
- BGH, Urt. v. 17.01.2019 - IX ZR 52/18, NJW 2019, 1232 — Kein-Mandat-Disclaimer in der Erstantwort schutzt Kanzlei vor konkludenter Mandatsbegrundung durch inhaltliche Ersthinweise.
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Datenschutzhinweis nach Art. 13 DSGVO muss bei Ersterhebung von Kontaktdaten erteilt werden; Erstantwort-Mail ist passender Zeitpunkt.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: Hinweis auf voraussichtliche Gesamtkosten vor Mandatsannahme
- Art. 13 DSGVO — Informationspflicht: Ersterhebung personenbezogener Daten begruendet sofortige Informationspflicht
- § 43 BRAO — Sorgfaltspflicht: zeitnahe und vollstaendige Beantwortung eingehender Anfragen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch gegenueber dem potenziellen Mandanten

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 49b Rn. 80-100 (Kostenbelehrung: Inhalt und Zeitpunkt)
- Kühling/Buchner DSGVO Art. 13 Rn. 1-30 (Informationspflicht bei Ersterhebung von Kontaktdaten)

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
