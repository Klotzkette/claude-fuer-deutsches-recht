---
name: pruefungsvorschlaege
description: "Prüft und genehmigt (oder lehnt ab) ausstehende Playbook-Aktualisierungsvorschläge des Playbook-Monitor-Agenten und überträgt genehmigte Änderungen in das Kanzleiprofil. Lädt, wenn der Monitor Vorschläge gemeldet hat, wenn der Nutzer „Playbook-Vorschläge prüfen\", „welche Playbook-Updates sind ausstehend\" oder „Abweichungsvorschläge durchgehen\" sagt."
---

# Playbook-Vorschläge prüfen und genehmigen

## Zweck

Diese Skill führt durch ausstehende Vorschläge des Playbook-Monitor-Agenten
und überträgt genehmigte Änderungen in das Kanzleiprofil. Der Monitor beobachtet
Verhandlungsmuster: wenn ein Anwalt eine Abweichung vom Standard-Playbook
wiederholt billigt (Schwellenwert: 5 Mal in den letzten 12 Monaten), generiert
er einen Vorschlag, das Playbook an die gelebte Praxis anzupassen.

Lädt automatisch nach einer Monitor-Meldung oder wenn der Nutzer ausstehende
Vorschläge explizit abfragen möchte.

## Eingaben

Keine Argumente erforderlich — die Skill arbeitet aus der ausstehenden
Vorschlags-Datei. Die Vorschlagsdatei wird vom Playbook-Monitor-Agenten
geschrieben.

## Rechtlicher Rahmen

### Grundprinzip: Klauselkontrolle nach AGB-Recht

Playbook-Vorschläge betreffen typischerweise Klauselpositionen im Bereich
des BGB-Schuldrechts und des AGB-Rechts. Jede Anpassung einer Playbook-Position
muss an den gesetzlichen Grenzen gemessen werden:

- § 305 BGB — Einbeziehungsvoraussetzungen; eine Klausel, die nicht wirksam
  einbezogen wurde, ist keine Verhandlungsposition, die in ein Playbook gehört
- § 305c BGB — Überraschende und mehrdeutige Klauseln; eine Klausel, die
  nach Entstehung und Inhalt so ungewöhnlich ist, dass der Vertragspartner
  nicht mit ihr rechnet, wird nicht Vertragsbestandteil — auch ein Playbook,
  das solche Klauseln als „Standard" führt, erzeugt keine belastbaren Positionen
- § 307 Abs. 1 S. 2 BGB — Transparenzgebot; das Playbook muss die eigene
  Position klar und verständlich formulieren, um sie in Verhandlungen
  durchzusetzen und AGB-rechtliche Kontrolle zu bestehen
- § 307 Abs. 2 BGB — Abweichung von wesentlichen Grundgedanken der gesetzlichen
  Regelung als Indiz für unangemessene Benachteiligung
- §§ 308, 309 BGB — Klauselverbote; Positionen, die gegen diese Verbote
  verstoßen, dürfen nicht als reguläre Playbook-Positionen geführt werden

### Begründungspflicht mit Kommentarbelegen

Jeder Vorschlag zur Änderung einer Playbook-Position muss mit Quellen
begründet sein. Maßgebliche Kommentare für Playbook-Vorschläge im Vertragsrecht:

- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 307 Rn. 1 — Leitstelle für
  Inhaltskontrolle und Transparenzgebot
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 45 — Differenzierte Analyse
  zu einzelnen Klauseltypen
- Wolf/Lindacher/Pfeiffer, AGB-Recht, 7. Aufl. 2020, § 307 BGB Rn. 100
  — Klauselkontrolle in der Verhandlungspraxis (Doppelautoren-Kommentar)
- Coester-Waltjen, in: Staudinger, BGB, Neubearbeitung 2022, § 307 Rn. 200
  — Systematische Darstellung Generalklausel

### Leitentscheidungen für Playbook-Anpassungen

- BGH, Urt. v. 25.10.2016 – VI ZR 516/15, NJW 2017, 1104 Rn. 14
  (Haftungsbeschränkung in AGB; Grenze der zulässigen Absenkung;
  § 309 Nr. 7 BGB)
- BGH, Urt. v. 19.11.2019 – XI ZR 9/18, NJW 2020, 461 Rn. 22 ff.
  (Transparenzgebot; Änderungsklauseln müssen klar und verständlich sein)
- BGH, Urt. v. 08.12.2011 – VII ZR 111/11, NJW 2012, 1431 Rn. 20
  (Haftungsfreizeichnung für Vorsatz unwirksam; § 276 Abs. 3 BGB;
  § 309 Nr. 7 lit. b BGB; kein Verhandlungsspielraum für das Playbook)
- BGH, Urt. v. 14.01.2020 – VIII ZR 163/18, NJW 2020, 1431 Rn. 25
  (Klauselkontrolle Gewährleistungsverkürzung; § 309 Nr. 8 BGB;
  Grenzen für Mängelrechtsausschluss in AGB)
- BGH, Urt. v. 29.06.2011 – VIII ZR 212/08, BGHZ 190, 115 Rn. 20 ff.
  (AGB-Einbeziehung im unternehmerischen Verkehr; § 305 Abs. 2 BGB)

### Kommentarliteratur

- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 307 Rn. 45
  (Transparenzgebot bei Haftungsklauseln)
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 309 Rn. 90
  (Haftungsausschlussverbote im Detail)
- Wolf/Lindacher/Pfeiffer, AGB-Recht, 7. Aufl. 2020, Vor § 307 BGB
  Rn. 50 ff. (Verhandlungsspielraum bei AGB-Klauseln)
- Lehmann-Richter, in: BeckOGK BGB, 70. Ed. (Stand 01.08.2024), § 307
  Rn. 100 ff. (Inhaltskontrolle Schritt für Schritt)

## Ablauf

### Schritt 1 — Vorschlagsdatei laden

Lade den Playbook-Monitor-Agenten und führe Schritt 5 (Prüf- und
Genehmigungsablauf) aus.

Falls keine Vorschlagsdatei existiert oder sie leer ist:

> *Keine ausstehenden Vorschläge. Das Playbook ist aktuell.*

Nicht weiterprocedieren.

### Schritt 2 — Vorschläge einzeln vorstellen

Jeden Vorschlag vollständig anzeigen. Vier Optionen anbieten:

| Option | Bedeutung |
|---|---|
| **Übernehmen** | Änderung sofort in das Kanzleiprofil schreiben |
| **Ablehnen** | Vorschlag verwerfen; kein Schreiben |
| **Bearbeiten** | Vorschlag vor Übernahme anpassen |
| **Zurückstellen** | Vorschlag für spätere Entscheidung aufbewahren |

### Schritt 3 — Diff anzeigen vor Schreiben

Für **Übernehmen** oder **Bearbeiten**: Den exakten Diff
(alter Wert → neuer Wert) im Kanzleiprofil zeigen, bevor geschrieben wird.
Nur nach ausdrücklicher Bestätigung durch den Anwalt übertragen.

**Format des Diffs:**

```
## Playbook — Haftungsbeschränkung (Verwender-Seite)

AKTUELL:
Fallback-Position: 12 Monate Jahresvergütung

NEU (Vorschlag):
Fallback-Position: 18 Monate Jahresvergütung

Begründung (Monitor): 7 von 12 unterzeichneten Verträgen in den letzten
12 Monaten wurden mit 18 Monaten abgeschlossen. Muster liegt oberhalb
des Schwellenwerts (5 Mal).

Quelle: Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 309 Nr. 7 Rn. 15
(Zulässigkeit 18-Monate-Cap als Fallback bei IT-Dienstleistungsverträgen)

Übernehmen? (ja / nein / bearbeiten)
```

### Schritt 4 — Ablehnen oder Zurückstellen

Entscheidung protokollieren. Kanzleiprofil unverändert lassen.

Bei **Ablehnen**: In Abweichungslog eintragen, mit Begründung des Anwalts
(falls angegeben) oder mit dem Vermerk „Abgelehnt ohne Begründung".

Bei **Zurückstellen**: Vorschlag für die nächste Runde erhalten.

### Schritt 5 — Abschluss nach allen Vorschlägen

Zusammenfassung zeigen: wie viele Vorschläge übernommen, abgelehnt,
zurückgestellt. Danach Vorschlagsdatei archivieren.

```
Ergebnis:
- 2 Vorschläge übernommen (Haftungsdeckel Fallback, Verjährungsfrist Gewährleistung)
- 1 Vorschlag abgelehnt (Gerichtsstand München → Frankfurt)
- 1 Vorschlag zurückgestellt (Datenlöschfrist AVV)

Kanzleiprofil aktualisiert. Vorschlagsdatei archiviert.
```

## Ausgabeformat

Für jeden Vorschlag: Vollständiger Vorschlagsblock (Klausel, aktueller Wert,
vorgeschlagener neuer Wert, Begründung, Quellenbeleg) + vier Optionen.
Nach Entscheidung: Diff-Anzeige vor Schreiben.
Am Ende: Gesamtübersicht aller Entscheidungen.

## Beispiel

**Szenario:** Der Playbook-Monitor hat festgestellt, dass die Kanzlei in
8 von 10 Fällen eine Verlängerung der Gewährleistungsverjährung auf 2 Jahre
(statt Kanzlei-Standard 1 Jahr) akzeptiert hat.

**Vorschlag:**

```
Klausel: Gewährleistung — Verjährungsfrist (Kunden-Seite)

AKTUELL:
Standardposition: 1 Jahr (§ 438 Abs. 2 BGB; zulässige AGB-Verkürzung
im B2B-Bereich)
Fallback: 1,5 Jahre

NEU (Vorschlag):
Fallback: 2 Jahre (gesetzlicher Regelfall § 438 Abs. 1 Nr. 3 BGB)

Begründung: 8/10 unterzeichneter Verträge aus den letzten 12 Monaten
wurden mit 2 Jahren abgeschlossen.

Quelle:
- BGH, Urt. v. 14.01.2020 – VIII ZR 163/18, NJW 2020, 1431 Rn. 25
  (Grenzen Gewährleistungsverkürzung in AGB)
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 438 Rn. 10
  (Zulässige Verjährungszeiträume in AGB)
```

Anwalt wählt „Übernehmen" → Diff angezeigt → Kanzleiprofil aktualisiert.

## Risiken und typische Fehler

- **Vorschlag ohne Quellenbeleg akzeptieren.** Jeder Vorschlag zur Änderung
  einer Klauselposition muss mit BGH-Rechtsprechung oder Kommentarbeleg
  unterlegt sein. Vorschläge ohne Beleg nicht als „Übernehmen"-fähig markieren.
- **Diff nicht anzeigen.** Ohne Anzeige des exakten Diffs kann der Anwalt
  nicht beurteilen, ob die Änderung korrekt ist. Niemals direkt schreiben
  ohne Bestätigung.
- **Zwingende Verbote als veränderbar darstellen.** Wenn ein Vorschlag eine
  Position betrifft, die gegen §§ 308, 309 BGB oder § 276 Abs. 3 BGB verstößt
  (z. B. Ausschluss der Haftung für Vorsatz oder Körperverletzung), diesen
  Vorschlag mit Fehlermeldung zurückweisen und nicht zur Genehmigung stellen.
- **Zurückgestellte Vorschläge vergessen.** Zurückgestellte Vorschläge bleiben
  in der Datei und werden beim nächsten Aufruf erneut vorgelegt.

## Quellenpflicht

Jeder Vorschlag in der Ausgabe muss enthalten:
- Den betroffenen Paragraphen (z. B. § 309 Nr. 7 BGB, § 438 BGB)
- Mindestens eine BGH-Entscheidung zur Klauselgrenze in korrekter Zitierweise
- Mindestens einen Kommentarbeleg im Bearbeiterstil „Bearbeiter, in: Werk"
  (z. B. Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 307 Rn. 45)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
