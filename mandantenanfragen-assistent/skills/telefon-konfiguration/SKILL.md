---
name: telefon-konfiguration
description: "Kanzlei muss Telefonnummern für Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Prüfraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der Platzhalter. Output: konfigurierte Telefonnummern in Templates. Abgrenzung zu erstantwort-generator (E-Mail-Erstellung) und muster-erstantwort im Mandantenanfragen Assistent: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Telefon-Konfiguration

## Arbeitsbereich

Kanzlei muss Telefonnummern für Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Prüfraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der Platzhalter. Output: konfigurierte Telefonnummern in Templates. Abgrenzung zu erstantwort-generator (E-Mail-Erstellung) und muster-erstantwort. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

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
