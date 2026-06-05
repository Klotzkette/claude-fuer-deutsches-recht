---
name: folgekorrespondenz-vorbereiten-konfliktcheck
description: "Folgekorrespondenz Vorbereiten Konfliktcheck: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Folgekorrespondenz Vorbereiten Konfliktcheck

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Folgekorrespondenz Vorbereiten Konfliktcheck** im Plugin Mandantenanfragen-Assistent. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `folgekorrespondenz-vorbereiten` | Nach Eingang einer Anfrage muss Sekretariat CRM-Eintrag und Akte anlegen. CRM-Eintrag Kanzlei-Intake. Prüfraster: Name Mail Telefon Anliegen-Stichwort Dringlichkeit Datum Sprachkennung Konfliktcheck-Status. Output: Skeleton-Eintrag für CRM und Aktenanlage. Abgrenzung zu anfrage-eingang-parser (Parsing) und mandanten-intake im Sozialrecht. |
| `konfliktcheck-vorab` | Sekretariat soll vor Terminvergabe Interessenkonflikt prüfen. § 43a Abs. 4 BRAO § 3 BORA Interessenkonflikt-Check. Prüfraster: Gegenseite und Beteiligte erfragen Datenbankabgleich bestehende Mandate. Output: Konfliktcheck-Anweisung und Abfragemuster. Abgrenzung zu mandatsverhältnis-hinweis (nach Mandatsannahme) und vertraulichkeit-erinnerung. |
| `ma-aufnahmegespraech-leitfaden` | Aufnahmegespraechsleitfaden Mandant: Sachverhalt, Eilbedarf, Ziel, Bereits eingeleitete Schritte, Andere beauftragte Anwaelte, Konflikte, Vergueng. Strukturierte Fragen und typische Stolpersteine. Mustertext zur Mandatsbestaetigung. |

## Arbeitsweg

Im Plugin Mandantenanfragen-Assistent gilt für **Folgekorrespondenz Vorbereiten Konfliktcheck**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `folgekorrespondenz-vorbereiten`

**Fokus:** Nach Eingang einer Anfrage muss Sekretariat CRM-Eintrag und Akte anlegen. CRM-Eintrag Kanzlei-Intake. Prüfraster: Name Mail Telefon Anliegen-Stichwort Dringlichkeit Datum Sprachkennung Konfliktcheck-Status. Output: Skeleton-Eintrag für CRM und Aktenanlage. Abgrenzung zu anfrage-eingang-parser (Parsing) und mandanten-intake im Sozialrecht.

# Folgekorrespondenz-Vorbereiten

Dieser Skill erstellt auf Basis der geparsten Eingangsanfrage einen fertigen Skeleton-Eintrag für das CRM-System oder die manuelle Aktenanlage. Ziel: Die Sekretariatsmitarbeitende kann den Vorgang sofort weiterführen, ohne Informationen erneut aus der Originalmail suchen zu müssen.


## Triage zu Beginn
1. Sind alle Pflichtfelder (Name, E-Mail, Anliegen, Dringlichkeit, Datum) aus dem Parsing verfuegbar?
2. Welches CRM oder welche Aktenstruktur wird genutzt (DATEV, RA-MICRO, Advoware, manuell)?
3. Wurde der Konfliktcheck bereits durchgefuehrt oder muss er im CRM-Eintrag als ausstehend markiert werden?
4. Soll der Eintrag automatisch oder nach manueller Freigabe gespeichert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. b DSGVO — Vertragsanbahnung als Rechtsgrundlage fuer CRM-Speicherung
- Art. 5 Abs. 1 lit. e DSGVO — Speicherbegrenzung: CRM-Eintrag nur so lange, wie fuer das Ziel notwendig
- § 43 BRAO — Sorgfaltspflicht: vollstaendige und sofortige Akten-/CRM-Dokumentation
- § 51 BRAO — Haftung: mangelnde Dokumentation als Organisationspflichtverletzung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Skeleton-Eintrag: Standardformat

```
=== NEUER VORGANG — ERSTANFRAGE ===
Eingangsdatum: [DATUM UND UHRZEIT]
Eingangskanal: E-Mail

--- KONTAKT ---
Name: [NACHNAME, VORNAME] | [Titel falls vorhanden]
E-Mail: [ABSENDER-ADRESSE]
Telefon: [TELEFONNUMMER oder "nicht genannt"]
Postanschrift: [ADRESSE oder "nicht genannt"]
Sprache: [DE / EN / FR / IT / Sonstiges]

--- ANLIEGEN ---
Rechtsgebiet: [Ersteinschätzung: z. B. Arbeitsrecht / Mietrecht / Strafrecht]
Stichwörter: [Kommagetrennte Liste — max. 5 Begriffe]
Beteiligte: [Gegner / Behörde / weitere Parteien oder "nicht genannt"]
Sachverhalt-Kurzfassung:
 [2-4 Sätze aus dem Parsing — wortwörtlich oder eng paraphrasiert]

--- DRINGLICHKEIT ---
Stufe: [HOCH / MITTEL / NIEDRIG / UNBEKANNT]
Begründung: [Frist, Termin, Eile-Signal oder "kein Hinweis"]
Massnahme: [Sofortiger Anwaltsrückruf erforderlich / Normale Bearbeitung / Abwarten]

--- STATUS ---
Spam-Check: [KLAR / VERDÄCHTIG / SPAM]
Konfliktcheck: [AUSSTEHEND — vor Terminvergabe durchführen!]
Erstantwort: [VERSENDET am DATUM / AUSSTEHEND]
Transkription: [AKTIV / NICHT AKTIV]

--- INTERNE NOTIZEN ---
[Platz für manuelle Ergänzungen der Sekretariatsmitarbeitenden]

=== ENDE SKELETON-EINTRAG ===
```

## Felder im Detail

### Eingangsdatum und -kanal

- Automatisch befüllt mit dem aktuellen Zeitstempel (ISO 8601: `YYYY-MM-DD HH:MM`)
- Eingangskanal: E-Mail, Telefon, Kontaktformular, Post — für E-Mail-basierte Anfragen stets "E-Mail"

### Kontakt-Felder

Aus dem Parsing-Skill (`anfrage-eingang-parser`) übernommen. Fehlende Felder werden mit "nicht genannt" markiert und für manuelle Ergänzung hervorgehoben.

### Rechtsgebiet-Ersteinschätzung

**Wichtig:** Dies ist eine nicht-verbindliche Ersteinschätzung des Parsing-Algorithmus. Sie dient der Vorsortierung im Sekretariat und darf NICHT als rechtliche Einschätzung an die anfragende Person weitergegeben werden.

Mögliche Rechtsgebiete (Auswahl):
- Arbeitsrecht, Mietrecht, Familienrecht, Erbrecht, Strafrecht
- Gesellschaftsrecht, Vertragsrecht, Schadensersatz
- Verwaltungsrecht, Sozialrecht, Steuerrecht
- Verkehrsrecht, Insolvenzrecht, IP-Recht
- Sonstiges / Unbekannt

### Dringlichkeitsstufen

| Stufe | Beschreibung | Sofortmaßnahme |
|---|---|---|
| HOCH | Frist erkannt, Haftungsrisiko, bevorstehende Verhandlung | Anwalt ruft sofort zurück |
| MITTEL | Zeitdruck vorhanden, aber keine akute Frist | Rückmeldung innerhalb 24h |
| NIEDRIG | Kein Zeitdruck erkennbar | Rückmeldung im normalen Ablauf |
| UNBEKANNT | Keine Aussage zu Dringlichkeit möglich | Wie MITTEL behandeln |

### Konfliktcheck-Status

Standardmäßig: `AUSSTEHEND`. Die Sekretariatsmitarbeitende trägt nach Durchführung des Konfliktchecks ein:
- `KLAR — kein Konflikt erkannt` oder
- `KONFLIKT — Mandat nicht möglich` oder
- `KONFLIKT — Rücksprache mit RA erforderlich`

### Transkriptions-Status

- `AKTIV` wenn die anfragende Person den Transkriptionsservice nutzen soll/wird
- `NICHT AKTIV` bei Standardverfahren mit schriftlicher Sachverhaltsschilderung

## Integration in gängige CRM-Systeme

Dieser Skill gibt einen Text-basierten Skeleton aus, der in alle gängigen Systeme eingefügt werden kann:

- **RA-MICRO:** Als neue Akte anlegen; Felder manuell übertragen; Aktenzeichen generieren.
- **Advoware:** Neues Mandat anlegen; Kontaktdaten übertragen; Status auf "Erstanfrage" setzen.
- **DATEV Anwalt:** Neues Verfahren anlegen; Mandantenakte erstellen.
- **Eigenentwicklung / Excel:** Tabellenzeile; CSV-Import möglich.

## Ausgabe

```
SKELETON-EINTRAG BEREIT
Für CRM-System oder manuelle Akte kopieren und einfügen.
Ausstehende Felder sind mit [BITTE ERGÄNZEN] markiert.
Konfliktcheck: AUSSTEHEND — vor Terminvergabe durchführen!
```

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datenquelle
- `dringlichkeitsmarker` — Dringlichkeitsstufe und Begründung
- `spam-und-massen-anfrage-filter` — Spam-Check-Status
- `konfliktcheck-vorab` — Hinweis auf ausstehenden Konfliktcheck

## 2. `konfliktcheck-vorab`

**Fokus:** Sekretariat soll vor Terminvergabe Interessenkonflikt prüfen. § 43a Abs. 4 BRAO § 3 BORA Interessenkonflikt-Check. Prüfraster: Gegenseite und Beteiligte erfragen Datenbankabgleich bestehende Mandate. Output: Konfliktcheck-Anweisung und Abfragemuster. Abgrenzung zu mandatsverhältnis-hinweis (nach Mandatsannahme) und vertraulichkeit-erinnerung.

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
Durchgeführt am: [DATUM]
Durchgeführt von: [MITARBEITENDE]
Anfragende Person: [NAME]
Gegenseite: [NAME / FIRMA]
Ergebnis: [KLAR / KONFLIKT — TYP / UNKLAR — Rücksprache]
Notiz: [Ggf. Begründung]
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

## 3. `ma-aufnahmegespraech-leitfaden`

**Fokus:** Aufnahmegespraechsleitfaden Mandant: Sachverhalt, Eilbedarf, Ziel, Bereits eingeleitete Schritte, Andere beauftragte Anwaelte, Konflikte, Vergueng. Strukturierte Fragen und typische Stolpersteine. Mustertext zur Mandatsbestaetigung.

# Aufnahmegespraechs-Leitfaden

## Spezialwissen: Aufnahmegespraechs-Leitfaden
- **Spezialgegenstand:** Aufnahmegespraechs-Leitfaden / ma aufnahmegespraech leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
