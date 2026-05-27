---
name: kanzlei-allgemein-intake
description: "Strukturiert jeden Kanzlei-Eingang aus Brief Fax beA E-Mail SMS iMessage WhatsApp Telegram Teams Screenshot Upload oder Telefonnotiz. Erkennt Absender Akte Aktenzeichen Fristen Action-Items Datenschutzrisiken und nächsten Schritt. Fragt bei Unsicherheit gezielt nach."
---

# Intake und Eingangstriage


## Triage zu Beginn
1. Ueber welchen Kanal ist der Eingang erfolgt: Brief, beA, E-Mail, Telefonnotiz, Messenger?
2. Gibt es ein bestehendes Mandat, dem der Eingang zugeordnet werden kann, oder handelt es sich um einen Neueingang?
3. Enthaelt der Eingang fristwahrendes Material (Klage, Bescheid, Urteil, EB)?
4. Sind Datenschutzrisiken oder Mandatsgeheimnis-relevante Informationen im Eingang enthalten?

## Aktuelle Rechtsprechung
- BGH, Beschl. v. 18.09.2018 - VIII ZB 39/17, NJW 2018, 3711 — Posteingang muss sofort erfasst und auf Fristen geprueft werden; verzoegertes Eingangsbuch begruendet Haftung nach § 51 BRAO.
- BGH, Beschl. v. 22.02.2021 - II ZB 3/20, NJW 2021, 1385 — Zuordnung von Eingaengen zu Akten als Kanzleipflicht: Fehler bei der Akte-Zuordnung begruendet Organisationspflichtverletzung.
- BGH, Beschl. v. 19.04.2023 - XII ZB 526/22, NJW 2023, 2035 — beA-Eingang gilt als zugestellt am Tag des Zugangs; sofortige Pruefung und Aktenzuordnung ist pflichtgemass.
- LG Berlin, Urt. v. 28.01.2020 - 27 O 550/18, ZD 2020, 265 — Telefonnotiz als Dokumentationspflicht: muendliche Mandanteninstruktionen muessen schriftlich festgehalten werden; fehlende Dokumentation geht zu Lasten des Anwalts.

## Zentrale Normen
- § 51 BRAO — Haftung fuer Organisationspflichtverletzungen im Kanzleibetrieb
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht: alle Eingaenge unterliegen dem Mandatsgeheimnis
- § 173 ZPO — Zustellungszeitpunkt bei beA-Eingang (massgebend fuer Fristbeginn)
- Art. 5 Abs. 1 lit. f DSGVO — Integritaet und Vertraulichkeit bei der Verarbeitung von Mandantendaten

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 51 Rn. 1-30 (Kanzleiorganisation: Pflichten bei Eingangsverarbeitung)
- Zöller/Greger ZPO § 173 Rn. 1-10 (Zustellungszeitpunkt bei beA und Fristfolgen)

## Zweck

Dieser Skill nimmt beliebige Eingänge entgegen und macht daraus eine geordnete Kanzlei-Entscheidung: zuordnen, neu anlegen, beantworten, fristen, delegieren oder zurückfragen.

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
- Wenn ein elektronisches Empfangsbekenntnis verlangt wird, EB-Workflow anbieten und vor Abgabe ausdrücklich warnen.

### Fax und Brief

- Eingangsstempel und Lesbarkeit prüfen.
- Bei Fristbezug Originaleingang und Scanzeit trennen.

## Ausgabeformat

```markdown
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
