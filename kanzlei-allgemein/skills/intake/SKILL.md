---
name: intake
description: "Strukturiert jeden Kanzlei-Eingang aus Brief Fax beA E-Mail SMS iMessage WhatsApp Telegram Teams Screenshot Upload oder Telefonnotiz. Erkennt Absender Akte Aktenzeichen Fristen Action-Items Datenschutzrisiken und nächsten Schritt. Fragt bei Unsicherheit gezielt nach im Kanzlei Allgemein."
---

# Intake und Eingangstriage

## Aktenstart statt Formularstart

Wenn zu **Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Kanzlei Allgemein** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Ueber welchen Kanal ist der Eingang erfolgt: Brief, beA, E-Mail, Telefonnotiz, Messenger?
2. Gibt es ein bestehendes Mandat, dem der Eingang zugeordnet werden kann, oder handelt es sich um einen Neueingang?
3. Enthaelt der Eingang fristwahrendes Material (Klage, Bescheid, Urteil, EB)?
4. Sind Datenschutzrisiken oder Mandatsgeheimnis-relevante Informationen im Eingang enthalten?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 51 BRAO — Haftung für Organisationspflichtverletzungen im Kanzleibetrieb
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht: alle Eingaenge unterliegen dem Mandatsgeheimnis
- § 173 ZPO — Zustellungszeitpunkt bei beA-Eingang (massgebend für Fristbeginn)
- Art. 5 Abs. 1 lit. f DSGVO — Integritaet und Vertraulichkeit bei der Verarbeitung von Mandantendaten

## Unterstützte Eingangskanäle

- Brief, Scan, Foto, Fax.
- beA-Nachricht, EGVP-Ausdruck, Empfangsbekenntnis.
- E-Mail und Anhänge.
- SMS, iMessage, WhatsApp, Telegram, Teams.
- Screenshot, Audio-Notiz, Telefonnotiz.
- Ordnerdrop oder Datenraum-Upload.

## Ablauf

1. **Kanal bestimmen**: Quelle, Empfangsdatum, technische Metadaten, Zuverlässigkeit.
2. **Absender und Beteiligte extrahieren**: Mandant, Gegner, Gericht, Behörde, Versicherung, Dritte.
3. **Aktenbezug prüfen**: eigenes Aktenzeichen, fremdes Aktenzeichen, Name, Sache, Gericht.
4. **Fristen und Action-Items erkennen**: Rechtsbehelfsfrist, gerichtliche Verfügung, Antwortfrist, Wiedervorlage, Rückruf.
5. **Mandatsannahme/GwG-Indikatoren erkennen**: neue Anfrage, Unternehmensmandant, Immobilien, Gesellschaft, Transaktion, Ausweiskopie, Handelsregisterauszug, wirtschaftlich Berechtigte, PEP, Fremdgeld, Drittzahlung, abweichender Zahler.
6. **Datenschutz und Geheimnis prüfen**: Drittinhalte, Gesundheitsdaten, Bankdaten, Ausweiskopien, Kinder, Strafdaten, besondere Kategorien.
7. **Priorität setzen**: sofort, heute, diese Woche, warten, nur ablegen.
8. **Ausgabe erzeugen**: Intake-Karte plus vorgeschlagene Ablage.

## Kanalregeln

### Messenger und Screenshots

- Authentizität nicht unterstellen.
- Kontext erfassen: wer schreibt, wann, in welchem Thread.
- Keine privaten Drittinhalte unnötig übernehmen.
- Bei Screenshots immer prüfen, ob abgeschnittene Inhalte entscheidend sein könnten.

### beA

- Empfangstag und eventuelle Zustellung sauber dokumentieren.
- Empfangsbekenntnis nie ohne Freigabe abgeben.
- Keine beA-PIN, Zertifikate oder Token speichern.
- Bei beA-Connect immer `kanzlei-allgemein-bea-journal` verwenden: Nachrichtenjournal einsehen, Screenshot sichern, jede eingegangene Nachricht als ZIP exportieren oder herunterladen, ZIP entpacken und der Akte zuordnen.
- Wenn ein elektronisches Empfangsbekenntnis verlangt wird, EB-anbieten und vor Abgabe ausdrücklich warnen.

### Fax und Brief

- Eingangsstempel und Lesbarkeit prüfen.
- Bei Fristbezug Originaleingang und Scanzeit trennen.

## Intake-Karte

- Kanal:
- Eingang am:
- Absender:
- Betroffene Akte:
- Externe Aktenzeichen:
- Kurzinhalt:
- Fristen:
- Action-Items:
- Risiken:
- Mandatsannahme/GwG:
- Vorschlag:
- Rückfragen:
```

## Übergabe

- Neue Sache: `kanzlei-allgemein-akte` und bei Annahme-/Identifizierungs-/GwG-Indikatoren `kanzlei-allgemein-mandatsannahme-gwg`.
- Unklare Aktenzeichen: `kanzlei-allgemein-aktenzeichen`.
- Frist oder Handlung: `kanzlei-allgemein-fristen-monitor`.
- Antwortentwurf oder Versand: `kanzlei-allgemein-output-versand`.
- beA-Journal, beA-ZIP oder elektronisches Empfangsbekenntnis: `kanzlei-allgemein-bea-journal`.

