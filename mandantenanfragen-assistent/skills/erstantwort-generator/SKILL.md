---
name: erstantwort-generator
description: "Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Prüfraster: Dank für Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung Mandatsverhältnis-Disclaimer Schlussformel. Output: fertige Erstantwort-E-Mail mit allen Pflichthinweisen. Abgrenzung zu muster-erstantwort (Template-Vorlage) und anrede-uebernehmen im Mandantenanfragen Assistent: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Erstantwort-Generator

## Arbeitsbereich

Sekretariat oder Anwalt muss professionelle Erstantwort-E-Mail an potentiellen Mandanten senden. Hauptskill Erstantwort-E-Mail. Prüfraster: Dank für Anfrage exakte Anrede Terminvergabe-Hinweis Transkriptionsservice mit DSGVO-Einwilligung Mandatsverhältnis-Disclaimer Schlussformel. Output: fertige Erstantwort-E-Mail mit allen Pflichthinweisen. Abgrenzung zu muster-erstantwort (Template-Vorlage) und anrede-uebernehmen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieser Hauptskill erstellt die vollständige formelle Erstantwort-E-Mail an einen potenziellen Mandanten. Er koordiniert alle Teilskills und fügt deren Output zu einem druckfertigen Schreiben zusammen.

## Triage zu Beginn
1. Sind alle Teil-Skills bereits ausgefuehrt (Parsing, Spam-Check, Dringlichkeit, Anrede, Sprache)?
2. Welche Dringlichkeitsstufe wurde gesetzt — bei HOCH Sofortruf-Hinweis in der Mail einfuegen?
3. Besteht bereits ein Mandatsverhältnis oder handelt es sich um eine Erstanfrage (Kein-Mandat-Disclaimer erforderlich)?
4. Soll der Transkriptionsservice-Hinweis aktiviert werden (Trigger: Anfrage ist kurz/fragmentarisch oder Nutzer kann nicht schreiben)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: Hinweis auf voraussichtliche Gesamtkosten vor Mandatsannahme
- Art. 13 DSGVO — Informationspflicht: Ersterhebung personenbezogener Daten begruendet sofortige Informationspflicht
- § 43 BRAO — Sorgfaltspflicht: zeitnahe und vollstaendige Beantwortung eingehender Anfragen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch gegenueber dem potenziellen Mandanten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

Standard: "vielen Dank für Ihre Anfrage, die uns heute zugegangen ist."

Varianten:
- Bei dringlicher Anfrage: "vielen Dank für Ihre Anfrage. Wir haben Ihr Anliegen als dringend zur Kenntnis genommen."
- Bei Empfehlung: "vielen Dank für Ihre Anfrage, die uns durch [Quelle, soweit genannt] zugegangen ist."

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
"Bitte schildern Sie uns Ihr Anliegen in einigen Sätzen — Datum des Ereignisses, beteiligte Parteien, bestehende Fristen und Ihr Ziel."

### Transkriptionsservice-Hinweis

Nur einfügen wenn:
- Die anfragende Person explizit schreibt, dass sie nicht schreiben kann/mag, oder
- Die Sekretariatsmitarbeiterin den Modus manuell aktiviert.

Enthält: Telefonnummer des Transkriptionsservices, kurze Ablauferklärung, DSGVO-Einwilligungshinweis in Kurzform (Langform aus Skill `einwilligung-hinweis-datenschutz`).

### Mandatsverhältnis-Disclaimer

Kurzform in der Mail: "Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis begründet und keine Rechtsberatung darstellt."

Langform in der Fußzeile: aus Skill `mandatsverhaeltnis-hinweis`.

### Schlussformel

Standard: "Mit freundlichen Grüßen"

Varianten bei Sprache:
- Englisch: "Yours sincerely," / "Kind regards,"
- Französisch: "Veuillez agréer l'expression de mes salutations distinguées,"
- Italienisch: "Distinti saluti,"

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
