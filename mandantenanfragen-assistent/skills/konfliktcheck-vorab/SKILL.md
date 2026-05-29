---
name: konfliktcheck-vorab
description: "Sekretariat soll vor Terminvergabe Interessenkonflikt prüfen. § 43a Abs. 4 BRAO § 3 BORA Interessenkonflikt-Check. Prüfraster: Gegenseite und Beteiligte erfragen Datenbankabgleich bestehende Mandate. Output: Konfliktcheck-Anweisung und Abfragemuster. Abgrenzung zu mandatsverhältnis-hinweis (nach Mandatsannahme) und vertraulichkeit-erinnerung."
---

# Konfliktcheck-Vorab

Dieser Skill erinnert an die berufsrechtliche Pflicht zum Interessenkonflikt-Check vor Mandatsannahme und instruiert das Sekretariat, die dafür erforderlichen Informationen bereits bei der Terminvergabe zu erfragen.


## Triage zu Beginn
1. Sind alle konfliktsrelevanten Informationen vorhanden: Gegenseite, Beteiligte, Rechtsgebiet, Aktenzeichen?
2. Ist die anfragende Person oder die Gegenseite ein bekannter oder ehemaliger Mandant (auch Sozietaetsmitglieder pruefen)?
3. Gibt es Anzeichen fuer einen Gesamtkonflikt (Sozietaet als Ganzes betroffen, § 3 Abs. 2 BORA)?
4. Bei Interessenkonflikt: welche Konsequenz (Mandatsablehnug, Hinweis an Suchenden auf andere Kanzlei)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 4 BRAO — Verbot der Vertretung widerstreitender Interessen
- § 3 BORA — Konkretisierung des Interessenkonflikt-Verbots: gilt auch fuer ehemalige Mandanten und Sozietaetsmitglieder
- § 356 StGB — Parteiverrat: strafrechtliche Konsequenz bei gleichzeitiger Vertretung gegenlaeufiger Interessen
- § 14 BRAO — Widerruf der Zulassung bei schwerwiegenden Berufsrechtsverletzungen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rechtsgrundlage

### § 43a Abs. 4 BRAO — Verbot der Vertretung widerstreitender Interessen

> "Der Rechtsanwalt darf nicht tätig werden, wenn er eine andere Partei in derselben Rechtssache im widerstreitenden Interesse bereits beraten oder vertreten hat oder mit ihr in Sozietät verbunden ist."

### § 3 BORA — Verbot der Vertretung widerstreitender Interessen (Konkretisierung)

§ 3 BORA konkretisiert das Verbot: Ein Rechtsanwalt darf für mehrere Auftraggeber in derselben Rechtssache dann nicht tätig werden, wenn zwischen ihnen widerstreitende Interessen bestehen. Gilt auch für ehemalige Mandantinnen und Mandanten sowie für Sozietätsmitglieder (§ 3 Abs. 2 BORA).

### Folgen einer Pflichtverletzung

- Möglicher Widerruf der Zulassung (§ 14 BRAO)
- Schadensersatzpflicht gegenüber dem betroffenen Mandanten
- Berufsrechtliche Ahndung durch die Rechtsanwaltskammer
- Strafrechtliche Relevanz in besonders schweren Fällen (Parteiverrat § 356 StGB)

## Pflicht-Informationen für den Konfliktcheck

Das Sekretariat muss vor Terminvergabe — oder spätestens beim Erstgespräch — folgende Informationen erfragen und im CRM vermerken:

### Block A: Anfragende Person

- Vollständiger Name
- Wohnort oder Unternehmenssitz
- Bevollmächtigte oder Vertreter (z. B. bei GmbH: Geschäftsführer)

### Block B: Gegenseite / Beteiligte

- Vollständiger Name oder Firma der Gegenseite
- Soweit bekannt: Wohnort, Unternehmenssitz, Rechtsform
- Weitere Beteiligte: Miterben, Mitgesellschafter, Bürgschaftsgeber
- Behörde oder Institution (bei Verwaltungs- oder Steuersachen)

### Block C: Sachverhalts-Grundriss

- Rechtsnatur des Streits (Vertragsstreit, Scheidung, Erbauseinandersetzung, Strafrecht etc.)
- Vertragsbeziehungen oder gemeinsame Vorgeschichte mit der Kanzlei

## Ablauf des Konfliktchecks in der Kanzlei

1. **Erfassung der Daten:** Sekretariat erfasst Angaben zu Anfragender und Gegenseite beim Erstgespräch oder vor Terminvergabe.
2. **Abgleich mit Mandantendatenbank:** Alle Namen und Unternehmen werden gegen die bestehende Mandantenakte abgeglichen.
3. **Sozietätsmitglieder:** Prüfung erstreckt sich auf alle Partner und angestellten Anwälte der Kanzlei.
4. **Ergebnis:** 
   - `KLAR` — Mandat kann angenommen werden
   - `KONFLIKT` — Mandat nicht möglich; anfragende Person erhöflich ablehnen und ggf. auf andere Kanzlei hinweisen
   - `UNKLAR` — Rücksprache mit Rechtsanwalt erforderlich vor Terminvergabe

## Skript für das Sekretariat: Was beim Erstanruf zu fragen ist

```
"Um sicherzustellen, dass wir Ihnen helfen dürfen, benötige ich noch
kurz einige Angaben. Wen haben Sie als Gegenseite — also: gegen wen
oder gegen welches Unternehmen geht es in Ihrem Fall?"

Falls die anfragende Person zögert:
"Das ist für uns nur intern wichtig, um zu prüfen, ob wir Sie in
diesem Fall vertreten dürfen. Ich leite nichts an die Gegenseite weiter."
```

## CRM-Eintrag nach Konfliktcheck

```
KONFLIKTCHECK
=============
Durchgeführt am:   [DATUM]
Durchgeführt von:  [MITARBEITENDE]
Anfragende Person: [NAME]
Gegenseite:        [NAME / FIRMA]
Ergebnis:          [KLAR / KONFLIKT — TYP / UNKLAR — Rücksprache]
Notiz:             [Ggf. Begründung]
```

## Hinweis bei KONFLIKT: Ablehnungsformulierung

Falls ein Interessenkonflikt besteht, wird kein Mandat angenommen. Formular-Text für die ablehnende Rückmeldung:

```
Sehr geehrte[r] [NAME],

vielen Dank für Ihre Anfrage. Wir haben geprüft, ob wir Ihnen in Ihrem
Anliegen behilflich sein können. Leider müssen wir Ihnen mitteilen, dass
wir aus internen berufsrechtlichen Gründen in diesem Fall nicht für Sie
tätig werden können.

Wir empfehlen Ihnen, sich an eine andere Kanzlei zu wenden. Die
Rechtsanwaltskammer [ZUSTÄNDIGE KAMMER] kann Ihnen Empfehlungen geben
(Tel. [KAMMER-TELEFON]).

Mit freundlichen Grüßen
[KANZLEI-NAME]
```

## Verweise auf andere Skills

- `anfrage-eingang-parser` — liefert Beteiligte und Gegnerinfos
- `folgekorrespondenz-vorbereiten` — enthält Konfliktcheck-Statusfeld
- `mandatsverhaeltnis-hinweis` — parallel relevanter Disclaimer
- `vertraulichkeit-erinnerung` — nach erfolgreichem Check und Mandatsbegründung
