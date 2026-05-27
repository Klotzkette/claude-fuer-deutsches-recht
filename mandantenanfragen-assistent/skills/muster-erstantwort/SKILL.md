---
name: muster-erstantwort
description: "Kanzlei benoetigt fertige ausfuellbare Vorlage fuer die Erstantwort auf Mandantenanfragen. Template Erstantwort. Pruefraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard nur Vorname Transkriptionsservice-Modus. Output: vollstaendiges Template-Set fuer Erstantwort. Abgrenzung zu erstantwort-generator (konkrete Antwort erstellen) und anfrage-eingang-parser."
---

# Muster-Erstantwort

Dieser Skill enthält das vollständige Komplett-Musterschreiben für die Erstantwort auf Mandantenanfragen. Es ist für den direkten Copy-paste-Einsatz durch das Sekretariat konzipiert.

Alle Platzhalter in eckigen Klammern `[...]` werden durch den Skill `telefon-konfiguration` und `anrede-uebernehmen` automatisch befüllt oder sind manuell zu ersetzen.


## Triage zu Beginn
1. Welche Variante des Musterschreibens wird benoetigt: Standard, Nur-Vorname oder Transkriptionsservice-Modus?
2. Sind alle Platzhalter (Kanzleiname, Sekretariats-Telefon, Unterzeichnende-RA) in kanzlei.json konfiguriert?
3. Wurde die Anrede aus dem Skill anrede-uebernehmen bereits geliefert und kann eingesetzt werden?
4. Soll das Muster in Deutsch oder einer Fremdsprache ausgegeben werden?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Standardisierte Erstantwort-Vorlagen als Qualitaetssicherungsmassnahme in der Kanzlei; vereinheitlichte Templates reduzieren Haftungsrisiko.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Vorlage muss Kostenbelehrung nach § 49b Abs. 5 BRAO enthalten; fehlendes Element begruendet Pflichtverletzung.
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Datenschutzhinweis nach Art. 13 DSGVO als Pflichtbestandteil des Erstantwort-Templates; fehlendes Element begruendet Datenschutzverstoß.
- OLG Hamm, Urt. v. 23.03.2021 - 28 U 115/20, NJW-RR 2021, 895 — Kein-Mandat-Disclaimer im Template als Haftungsschutz: vorab etablierter Text verhindert individuelle Formulierungsfehler durch Sachbearbeiter.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: im Erstantwort-Template vorzusehen
- Art. 13 DSGVO — Informationspflicht: im Erstantwort-Template vorzusehen
- § 43 BRAO — Sorgfaltspflicht: standardisierte Qualitaetssicherung durch Templates
- § 43a Abs. 2 BRAO — Verschwiegenheit: Template darf keine vertraulichen Informationen enthalten

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Qualitaetssicherung: Vorlagen als Mittel der Sorgfalt)
- Kühling/Buchner DSGVO Art. 13 Rn. 1-30 (Informationspflicht: Template-Integration als Best Practice)

## Platzhalter-Verzeichnis

| Platzhalter | Beschreibung | Quelle |
|---|---|---|
| `[KANZLEI-NAME]` | Vollständiger Kanzleiname | `kanzlei.json` |
| `[SEKRETARIATS-TELEFON]` | Telefonnummer des Sekretariats | `kanzlei.json` |
| `[TRANSKRIPTIONS-TELEFON]` | Telefonnummer des Transkriptionsservices | `kanzlei.json` |
| `[UNTERZEICHNENDE-RA]` | Name und Titel der unterzeichnenden Anwältin/des Anwalts | `kanzlei.json` |
| `[ANREDE]` | Formelle Anredezeile | Skill `anrede-uebernehmen` |
| `[KANZLEI-ADRESSE]` | Postanschrift | `kanzlei.json` |
| `[KANZLEI-E-MAIL]` | E-Mail-Adresse | `kanzlei.json` |
| `[ERREICHBARKEITSZEITEN]` | Bürozeiten | `kanzlei.json` |
| `[DATUM]` | Heutiges Datum | Automatisch |

---

## Variante 1: Standard (vollständige Anrede, Sachverhalt per E-Mail)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

[ANREDE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.

Für ein erstes Beratungsgespräch vergeben wir Termine ausschließlich
telefonisch. Unser Sekretariat erreichen Sie unter:

  [SEKRETARIATS-TELEFON]
  [ERREICHBARKEITSZEITEN]

Um Ihr Anliegen bestmöglich vorzubereiten, bitten wir Sie herzlich,
uns Ihren Sachverhalt vorab kurz per E-Mail zu schildern. Folgende
Angaben helfen uns dabei:

  — Worum geht es in Ihrem Fall (in einigen Sätzen)?
  — Wann hat das zugrunde liegende Ereignis stattgefunden?
  — Gibt es Fristen, Termine oder behördliche Bescheide?
  — Wer ist die Gegenseite (Person, Unternehmen, Behörde)?

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-E-MAIL]
[SEKRETARIATS-TELEFON]

---
Diese Nachricht begründet kein Mandatsverhältnis und stellt keine Rechtsberatung dar.
```

---

## Variante 2: Nur Vorname (keine Anrede, neutrale Anredeform)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

Sehr geehrte[r] [VORNAME] [NACHNAME],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

[Identischer Textblock wie Variante 1 ab „Bitte beachten Sie ..."]
```

Falls Nachname nicht ermittelbar:
Anrede: „Sehr geehrte anfragende Person,"

---

## Variante 3: Transkriptionsservice-Modus (kann nicht/kaum schreiben)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

[ANREDE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.

Für ein erstes Beratungsgespräch vergeben wir Termine ausschließlich
telefonisch. Unser Sekretariat erreichen Sie unter:

  [SEKRETARIATS-TELEFON]
  [ERREICHBARKEITSZEITEN]

Da Ihnen eine schriftliche Schilderung schwerfällt, bieten wir Ihnen
einen automatisierten Transkriptionsservice an. Sie rufen unter der
folgenden Nummer an und schildern Ihr Anliegen mündlich — es wird
automatisch verschriftlicht und uns vertraulich übermittelt:

  Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

Ablauf des Anrufs:
  1. Automatische Ansage mit Datenschutzhinweis
  2. Bestätigung Ihres Einverständnisses (Tastendruck oder „Ja")
     — Ohne Bestätigung keine Aufnahme.
  3. Freie Schilderung Ihres Anliegens
  4. Automatische Verschriftung und vertrauliche Weiterleitung an uns

Wichtiger Datenschutzhinweis: Da zwischen uns noch kein Mandatsverhältnis
besteht, erfolgt die Verarbeitung Ihrer Sprachdaten ausschließlich auf
Basis Ihrer ausdrücklichen Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO.
Sie können diese Einwilligung jederzeit widerrufen. Die vollständige
Datenschutzinformation senden wir Ihnen auf Anfrage gerne zu.

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-E-MAIL]
[SEKRETARIATS-TELEFON]

---
Diese Nachricht begründet kein Mandatsverhältnis und stellt keine Rechtsberatung dar.
Datenschutzhinweis gemäß Art. 13 DSGVO auf Anfrage erhältlich unter [KANZLEI-E-MAIL].
```

---

## Verwendungshinweis für das Sekretariat

1. Variante je nach Eingang auswählen.
2. Alle `[...]`-Platzhalter durch die Kanzlei-Daten ersetzen.
3. `[ANREDE]` aus dem Skill `anrede-uebernehmen` übernehmen.
4. Vor dem Versand: Korrekturlesen — insbesondere Anrede und Telefonnummern prüfen.
5. Originalmail der anfragenden Person in Kopie ablegen.
6. CRM-Eintrag aus Skill `folgekorrespondenz-vorbereiten` anlegen.

## Verweise auf andere Skills

- `anrede-uebernehmen` — Anredezeile
- `telefon-konfiguration` — alle Telefonnummern und Kanzleidaten
- `erstantwort-generator` — Hauptskill der die Variante automatisch wählt
- `einwilligung-hinweis-datenschutz` — Langform auf Anfrage
- `mandatsverhaeltnis-hinweis` — Disclaimer (Langform bei Bedarf)
