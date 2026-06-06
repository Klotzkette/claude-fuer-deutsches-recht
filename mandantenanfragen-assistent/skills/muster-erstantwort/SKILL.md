---
name: muster-erstantwort
description: "Kanzlei benoetigt fertige ausfuellbare Vorlage für die Erstantwort auf Mandantenanfragen. Template Erstantwort. Prüfraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard nur Vorname Transkriptionsservice-Modus. Output: vollständiges Template-Set für Erstantwort. Abgrenzung zu erstantwort-generator (konkrete Antwort erstellen) und anfrage-eingang-parser im Mandantenanfragen Assistent: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Muster-Erstantwort

## Arbeitsbereich

Kanzlei benoetigt fertige ausfuellbare Vorlage für die Erstantwort auf Mandantenanfragen. Template Erstantwort. Prüfraster: Platzhalter KANZLEI-NAME SEKRETARIATS-TELEFON TRANSKRIPTIONS-TELEFON UNTERZEICHNENDE-RA. Drei Varianten Standard nur Vorname Transkriptionsservice-Modus. Output: vollständiges Template-Set für Erstantwort. Abgrenzung zu erstantwort-generator (konkrete Antwort erstellen) und anfrage-eingang-parser. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieser Skill enthält das vollständige Komplett-Musterschreiben für die Erstantwort auf Mandantenanfragen. Es ist für den direkten Copy-paste-Einsatz durch das Sekretariat konzipiert.

Alle Platzhalter in eckigen Klammern `[...]` werden durch den Skill `telefon-konfiguration` und `anrede-uebernehmen` automatisch befüllt oder sind manuell zu ersetzen.

## Triage zu Beginn
1. Welche Variante des Musterschreibens wird benoetigt: Standard, Nur-Vorname oder Transkriptionsservice-Modus?
2. Sind alle Platzhalter (Kanzleiname, Sekretariats-Telefon, Unterzeichnende-RA) in kanzlei.json konfiguriert?
3. Wurde die Anrede aus dem Skill anrede-uebernehmen bereits geliefert und kann eingesetzt werden?
4. Soll das Muster in Deutsch oder einer Fremdsprache ausgegeben werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: im Erstantwort-Template vorzusehen
- Art. 13 DSGVO — Informationspflicht: im Erstantwort-Template vorzusehen
- § 43 BRAO — Sorgfaltspflicht: standardisierte Qualitaetssicherung durch Templates
- § 43a Abs. 2 BRAO — Verschwiegenheit: Template darf keine vertraulichen Informationen enthalten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

[Identischer Textblock wie Variante 1 ab "Bitte beachten Sie ..."]
```

Falls Nachname nicht ermittelbar:
Anrede: "Sehr geehrte anfragende Person,"

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
 2. Bestätigung Ihres Einverständnisses (Tastendruck oder "Ja")
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
