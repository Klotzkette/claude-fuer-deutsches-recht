---
name: uebernimmt-telefon-konfiguration
description: "Uebernimmt Telefon Konfiguration: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Uebernimmt Telefon Konfiguration

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Uebernimmt Telefon Konfiguration** im Plugin Mandantenanfragen-Assistent. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-uebernimmt-schriftsatz-brief-und-memo-bausteine` | Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin mandantenanfragen assistent; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `telefon-konfiguration` | Kanzlei muss Telefonnummern für Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Prüfraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der Platzhalter. Output: konfigurierte Telefonnummern in Templates. Abgrenzung zu erstantwort-generator (E-Mail-Erstellung) und muster-erstantwort. |
| `transkriptionsdienst-erklaerung` | Mandant kann seinen Fall nicht schriftlich schildern und soll stattdessen anrufen. Transkriptionsservice Erklärung in Erstantwort. Prüfraster: Telefonnummer Ablauf des Anrufs Verarbeitungshinweis DSGVO-Einwilligung Kein-Mandat-Hinweis. Output: Transkriptionsservice-Hinweis für Erstantwort. Abgrenzung zu einwilligung-hinweis-datenschutz (DSGVO-Klausel) und erstantwort-generator. |

## Arbeitsweg

Im Plugin Mandantenanfragen-Assistent gilt für **Uebernimmt Telefon Konfiguration**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-uebernimmt-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin mandantenanfragen assistent; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Uebernimmt: Schriftsatz-, Brief- und Memo-Bausteine / uebernimmt schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DSGVO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Uebernimmt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `telefon-konfiguration`

**Fokus:** Kanzlei muss Telefonnummern für Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Prüfraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der Platzhalter. Output: konfigurierte Telefonnummern in Templates. Abgrenzung zu erstantwort-generator (E-Mail-Erstellung) und muster-erstantwort.

# Telefon-Konfiguration

Dieser Skill verwaltet die Kanzlei-spezifischen Kontaktdaten — insbesondere Telefonnummern — und stellt sicher, dass alle Antwort-Templates mit den aktuellen Daten befüllt werden.


## Triage zu Beginn
1. Sind alle Pflicht-Felder in kanzlei.json bereits konfiguriert (Kanzleiname, Telefon, E-Mail, Unterzeichnende-RA)?
2. Hat sich eine Telefonnummer oder ein Kanzlei-Datum geaendert, das in allen Templates aktualisiert werden muss?
3. Gibt es mehrere Kanzlei-Standorte mit unterschiedlichen Telefonnummern, die getrennt gepflegt werden muessen?
4. Sollen die Konfigurationsdaten verschluesselt gespeichert werden (Datenschutzanforderungen)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 5 TMG — Impressumspflicht: vollstaendige Kanzlei-Kontaktdaten fuer elektronische Kommunikation
- Art. 4 Nr. 7 DSGVO — Verantwortlicher: muss mit aktuellen Kontaktdaten erreichbar sein
- Art. 13 Abs. 1 lit. a DSGVO — Informationspflicht: Kontaktdaten des Verantwortlichen bei Ersterhebung
- § 43 BRAO — Sorgfaltspflicht: korrekte und aktuelle Kanzlei-Stammdaten in aller Kommunikation

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Platzhalter-Konfiguration: kanzlei.json

Die Kanzlei hinterlegt ihre Kontaktdaten in einer Datei `kanzlei.json`. Das Beispiel-Format:

```json
{
 "kanzlei": {
 "name": "[KANZLEI-NAME]",
 "adresse": {
 "strasse": "[STRASSE UND HAUSNUMMER]",
 "plz": "[POSTLEITZAHL]",
 "ort": "[ORT]"
 },
 "telefon_sekretariat": "[SEKRETARIATS-TELEFON]",
 "telefon_transkription": "[TRANSKRIPTIONS-TELEFON]",
 "erreichbarkeit": "[Z.B. Mo-Fr 09:00-17:00 Uhr]",
 "email_kanzlei": "[KANZLEI-E-MAIL]",
 "unterzeichnende_ra": "[VORNAME NACHNAME, Rechtsanwalt/Rechtsanwaeltin]",
 "rechtsanwaltsgesellschaft": "[FALLS ZUTREFFEND]"
 }
}
```

### Felder und Verwendung

| Feld | Beschreibung | Verwendung in |
|---|---|---|
| `name` | Vollständiger Kanzleiname | Briefkopf, Schlussformel, Fußzeile |
| `adresse` | Postanschrift der Kanzlei | Briefkopf, Fußzeile |
| `telefon_sekretariat` | Hauptnummer für Terminvergabe | Erstantwort-Body, Dringlichkeits-Hinweis |
| `telefon_transkription` | Nummer des Transkriptionsservices | Transkriptions-Abschnitt |
| `erreichbarkeit` | Bürozeiten | Erstantwort-Body |
| `email_kanzlei` | Haupt-E-Mail-Adresse | Briefkopf, Fußzeile |
| `unterzeichnende_ra` | Name der unterzeichnenden Anwältin/des Anwalts | Schlussformel |
| `rechtsanwaltsgesellschaft` | Partnerschaftsgesellschaft, GmbH o. ä. | Briefkopf, Fußzeile (optional) |

## Platzhalter-Ersetzung

Beim Aufruf des `erstantwort-generator`-Skills werden alle Platzhalter in doppelten eckigen Klammern `[...]` durch die Werte aus `kanzlei.json` ersetzt.

Beispiel-Ersetzung:
- `[SEKRETARIATS-TELEFON]` → `+49 89 12345-0`
- `[TRANSKRIPTIONS-TELEFON]` → `+49 89 12345-99`
- `[KANZLEI-NAME]` → `Müller & Partner Rechtsanwälte`
- `[ERREICHBARKEITSZEITEN]` → `Montag bis Freitag, 09:00 bis 17:00 Uhr`

## Validierung

Bevor die `kanzlei.json` für die Produktion verwendet wird:

1. **Telefonnummer-Format:** Deutsche Nummern im Format `+49 [ORTSVORWAHL] [NUMMER]` oder `0[ORTSVORWAHL] [NUMMER]`. Internationale Nummern im E.164-Format.
2. **Vollständigkeit:** Alle Pflichtfelder müssen ausgefüllt sein. Fehlende Pflichtfelder → Warnung und Verwendung des Platzhalter-Textes.
3. **E-Mail:** Grundlegendes Format `[name]@[domain].[tld]` prüfen.
4. **Transkriptions-Nummer:** Gesondert prüfen — dies ist die Nummer, die im DSGVO-Einwilligungshinweis erscheint. Fehlende oder ungültige Nummer → Transkriptions-Abschnitt deaktivieren und Warnung ausgeben.

## Fehlerfallbehandlung

| Fehlerfall | Verhalten |
|---|---|
| `kanzlei.json` nicht vorhanden | Platzhalter-Text `[KANZLEI-NAME]` etc. in der Antwort belassen; interne Warnung |
| Telefonnummer fehlt | Abschnitt mit dieser Nummer aus der Antwort entfernen; Warnung |
| Transkriptions-Nummer fehlt | Transkriptions-Abschnitt vollständig deaktivieren |
| Ungültiges JSON | Fehler melden; keine Antwort generieren bis korrigiert |

## Anpassung für verschiedene Kanzlei-Konstellationen

### Einzelanwalt / Einzelanwältin

```json
{
 "kanzlei": {
 "name": "Rechtsanwältin Dr. Lena Hoffmann",
 "telefon_sekretariat": "+49 30 98765-0",
 "telefon_transkription": "+49 30 98765-10",
 "unterzeichnende_ra": "Dr. Lena Hoffmann, Rechtsanwältin"
 }
}
```

### Große Kanzlei mit Empfang

```json
{
 "kanzlei": {
 "name": "Steinacker Lichtenberg Partnerschaftsgesellschaft mbB",
 "telefon_sekretariat": "+49 89 12345-0",
 "telefon_transkription": "+49 800 123456-99",
 "erreichbarkeit": "Mo-Do 08:30-18:00 Uhr, Fr 08:30-16:00 Uhr"
 }
}
```

### Kanzlei mit mehreren Standorten

Für jeden Standort eine separate `kanzlei-[standort].json` anlegen und beim Abruf den Standort angeben.

## Verweise auf andere Skills

- `erstantwort-generator` — Hauptabnehmer der Konfigurationsdaten
- `transkriptionsdienst-erklaerung` — benötigt `telefon_transkription`
- `muster-erstantwort` — Platzhalter werden durch diesen Skill befüllt

## 3. `transkriptionsdienst-erklaerung`

**Fokus:** Mandant kann seinen Fall nicht schriftlich schildern und soll stattdessen anrufen. Transkriptionsservice Erklärung in Erstantwort. Prüfraster: Telefonnummer Ablauf des Anrufs Verarbeitungshinweis DSGVO-Einwilligung Kein-Mandat-Hinweis. Output: Transkriptionsservice-Hinweis für Erstantwort. Abgrenzung zu einwilligung-hinweis-datenschutz (DSGVO-Klausel) und erstantwort-generator.

# Transkriptionsdienst-Erklärung

Dieser Skill formuliert den vollständigen Abschnitt in der Erstantwort-Mail, in dem der automatisierte Transkriptionsservice beschrieben wird. Er kommt zum Einsatz, wenn die anfragende Person signalisiert, dass sie ihren Sachverhalt nicht schriftlich schildern kann oder möchte.

## Triage zu Beginn
1. Liegt ein Ausloeser fuer den Transkriptionsservice vor (Anfrage kurz/fragmentarisch, Nutzer kann nicht schreiben, expliziter Wunsch)?
2. Ist ein Auftragsverarbeitungsvertrag nach Art. 28 DSGVO mit dem Transkriptions-Dienstleister vorhanden?
3. Enthaelt die Sprachaufnahme potenziell besondere Datenkategorien (Gesundheit, Strafrecht — Art. 9 DSGVO)?
4. Wird die Einwilligung per automatisierter Ansage (Tastendruck) oder schriftlich eingeholt?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. a DSGVO — Einwilligung als Rechtsgrundlage fuer Sprachaufnahme vor Mandatsannahme
- Art. 28 DSGVO — AVV mit Transkriptionsdienstleister: zwingend vor Inbetriebnahme
- Art. 9 Abs. 2 lit. a DSGVO — Ausdrückliche Einwilligung bei besonderer Datenkategorien (Gesundheit, Strafrecht)
- Art. 13 DSGVO — Informationspflicht bei Ersterhebung von Sprachdaten: vollstaendige Vorab-Aufklaerung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wann wird dieser Skill aktiviert?

Aktivierung wenn einer der folgenden Auslöser erkannt wird:

- Explizit: "Ich kann nicht schreiben", "Ich schreibe lieber nicht", "Ich würde lieber anrufen und erzählen", "kann mich nicht gut schriftlich ausdrücken", "bin nicht so gut mit dem Computer"
- Implizit: Kurze, fragmentarische Anfrage ohne Sachverhalts-Details trotz offensichtlich komplexem Anliegen
- Manuell: Die Sekretariatsmitarbeiterin aktiviert den Modus explizit

## Ablauf des Transkriptionsservices

Der Ablauf, der in der Mail erklärt wird:

1. **Anruf:** Die anfragende Person ruft unter der Transkriptions-Telefonnummer an.
2. **Einwilligungsabfrage:** Zu Beginn des Anrufs wird eine automatisierte Ansage abgespielt, die auf die Verarbeitung der Sprachdaten hinweist. Die anrufende Person muss ihr Einverständnis durch Drücken einer Taste oder durch ein klares mündliches "Ja" bestätigen.
3. **Wichtig:** Ohne Einverständnis-Bestätigung wird die Aufnahme nicht gestartet. Der Anruf endet, oder die Person wird an das Sekretariat weitergeleitet.
4. **Schilderung:** Nach bestätigtem Einverständnis schildert die Person ihr Anliegen mündlich.
5. **Automatische Verschriftung:** Die Sprachaufnahme wird durch einen automatisierten Transkriptionsservice verschriftlicht.
6. **Übermittlung:** Das Transkript wird der Kanzlei vertraulich übermittelt und dem potenziellen Mandantenvorgang zugeordnet.
7. **Rückmeldung:** Das Sekretariat meldet sich auf Basis des Transkripts beim Anfragenden zurück.

## Mail-Abschnitt (Standard-Formulierung)

```
Falls Ihnen eine schriftliche Schilderung schwerfällt, bieten wir einen
automatisierten Transkriptionsservice an:

Sie rufen unter der folgenden Nummer an und schildern Ihr Anliegen
mündlich:

 Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

Ablauf:
 1. Automatische Ansage mit Datenschutzhinweis
 2. Bestätigung Ihres Einverständnisses (Tastendruck oder mündliches "Ja")
 — Ohne Bestätigung wird keine Aufnahme gestartet.
 3. Freie Schilderung Ihres Anliegens
 4. Automatische Verschriftung und vertrauliche Weiterleitung an uns

Bitte beachten Sie: Da zwischen uns noch kein Mandatsverhältnis besteht,
gilt für die Verarbeitung Ihrer Sprachdaten das ausdrückliche
Einverständnis nach Art. 6 Abs. 1 lit. a DSGVO als Rechtsgrundlage.
Sie können dieses Einverständnis jederzeit widerrufen. Einzelheiten
entnehmen Sie bitte unserem Datenschutzhinweis, den wir Ihnen auf
Anfrage gerne zusenden.
```

## Wichtige inhaltliche Anforderungen

### Kein Mandat, kein Vertrauensverhältnis

In diesem Stadium besteht noch kein Anwalts-Mandatsverhältnis. Das bedeutet:
- Die Schweigepflicht nach § 43a Abs. 2 BRAO gilt noch nicht für das spezifische Anliegen (wohl aber für allgemeine anwaltliche Verschwiegenheit im Rahmen der Berufsausübung).
- Die Verarbeitung der Sprachdaten bedarf deshalb einer ausdrücklichen Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), nicht einer vertraglichen Notwendigkeit.
- Der Skill `einwilligung-hinweis-datenschutz` liefert die vollständige DSGVO-Klausel.

### Keine Zusagen zur Mandatsannahme

Die Formulierung des Transkriptionsservice-Abschnitts enthält keine Zusagen, dass die Kanzlei das Mandat annehmen wird. Zulässig: "Wir melden uns auf Basis des Transkripts bei Ihnen." Nicht zulässig: "Wir werden Ihren Fall übernehmen."

### Technisch neutrale Sprache

Keine Nennung von Markennamen, Anbietern oder technischen Details des Transkriptionsservices in der Mandantenmail — diese sind interne Infrastruktur.

## Konfigurierbare Parameter

Aus `kanzlei.json`:
- `telefon_transkription` — Rufnummer des Transkriptionsservices
- Optional: Betriebszeiten des Transkriptionsservices, falls abweichend von Kanzleizeiten

## Verweise auf andere Skills

- `einwilligung-hinweis-datenschutz` — vollständige DSGVO-Einwilligung
- `mandatsverhaeltnis-hinweis` — Disclaimer zum fehlenden Mandat
- `telefon-konfiguration` — liefert `telefon_transkription`
- `erstantwort-generator` — bettet diesen Abschnitt in die Antwortmail ein

<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
