---
name: telefon-konfiguration
description: "Kanzlei muss Telefonnummern fuer Sekretariat und Transkriptionsservice in den Antwort-Templates hinterlegen. Konfigurationsverwaltung Kanzlei-Nummern. Pruefraster: kanzlei.json Sekretariatsnummer Transkriptionsnummer Lesen und Setzen der Platzhalter. Output: konfigurierte Telefonnummern in Templates. Abgrenzung zu erstantwort-generator (E-Mail-Erstellung) und muster-erstantwort."
---

# Telefon-Konfiguration

Dieser Skill verwaltet die Kanzlei-spezifischen Kontaktdaten — insbesondere Telefonnummern — und stellt sicher, dass alle Antwort-Templates mit den aktuellen Daten befüllt werden.


## Triage zu Beginn
1. Sind alle Pflicht-Felder in kanzlei.json bereits konfiguriert (Kanzleiname, Telefon, E-Mail, Unterzeichnende-RA)?
2. Hat sich eine Telefonnummer oder ein Kanzlei-Datum geaendert, das in allen Templates aktualisiert werden muss?
3. Gibt es mehrere Kanzlei-Standorte mit unterschiedlichen Telefonnummern, die getrennt gepflegt werden muessen?
4. Sollen die Konfigurationsdaten verschluesselt gespeichert werden (Datenschutzanforderungen)?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Kanzlei-Kontaktdaten muessen immer aktuell sein; veraltete Telefonnummern in Schreiben verhindern Mandantenkontakt und begruenden Sorgfaltspflichtverletzung.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Kanzleiimpressum (Kontaktdaten) als Pflichtangabe: falsche oder fehlende Angaben koennen Abmahnrisiken begruenden.
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Verantwortliche Stelle nach Art. 4 Nr. 7 DSGVO muss korrekt und erreichbar angegeben sein; veraltete Kontaktdaten verletzen Betroffenenrechte.
- BGH, Urt. v. 17.01.2019 - IX ZR 52/18, NJW 2019, 1232 — Angaben zur Kanzlei auf Briefbogen und in E-Mails muessen vollstaendig und korrekt sein; fehlerhafte Pflichtangaben koennen Formfehler des Schreibens begruenden.

## Zentrale Normen
- § 5 TMG — Impressumspflicht: vollstaendige Kanzlei-Kontaktdaten fuer elektronische Kommunikation
- Art. 4 Nr. 7 DSGVO — Verantwortlicher: muss mit aktuellen Kontaktdaten erreichbar sein
- Art. 13 Abs. 1 lit. a DSGVO — Informationspflicht: Kontaktdaten des Verantwortlichen bei Ersterhebung
- § 43 BRAO — Sorgfaltspflicht: korrekte und aktuelle Kanzlei-Stammdaten in aller Kommunikation

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-20 (Kanzlei-Stammdaten: Aktualitaetspflicht)
- Kühling/Buchner DSGVO Art. 13 Rn. 1-20 (Kontaktdaten des Verantwortlichen als Informationspflicht)

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
