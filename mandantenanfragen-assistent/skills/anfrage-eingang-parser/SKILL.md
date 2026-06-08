---
name: anfrage-eingang-parser
description: "Sekretariat oder Anwalt erhielt E-Mail-Anfrage eines potentiellen Mandanten und will sie schnell strukturiert auswerten. E-Mail-Parser Kanzlei. Prüfraster: Anrede Name Absender E-Mail-Adresse Telefon Sachverhaltsfetzen Stichwörter dringliche Hinweise auf Fristen oder Haftungsrisiken. Output: strukturiertes Datenblatt mit Kontaktdaten und Sachverhalts-Extrakt. Abgrenzung zu erstantwort-generator (Antwort erstellen) und dringlichkeitsmarker (Eilbedarf) im Mandantenanfragen Assistent."
---

# Anfrage-Eingang-Parser

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieser Skill extrahiert aus einer eingehenden Mandantenanfrage per E-Mail alle relevanten Informationen in strukturierter Form, damit das Sekretariat und die bearbeitende Rechtsanwältin sofort den Überblick haben.

## Triage zu Beginn
1. Ueber welchen Kanal ist die Anfrage eingegangen: E-Mail, Webformular, beA, Telefonnotiz, Messenger?
2. Gibt es eindeutige Fristen-Signale oder Eile-Marker, die sofortige Weiterleitung erfordern?
3. Kann die anfragende Person identifiziert werden (Name, E-Mail, Telefon) oder ist die Anfrage anonym?
4. Ist die Anfrage in deutscher Sprache oder in einer Fremdsprache (Weiterleitung an mehrsprachige-antwort)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. b, f DSGVO — Rechtsgrundlage für Verarbeitung von Erstanfrage-Daten
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur notwendige Daten aus der Anfrage extrahieren
- § 43 BRAO — Sorgfaltspflicht: sofortige Bearbeitung und Dokumentation eingehender Anfragen
- § 49b Abs. 5 BRAO — Kostenbelehrungspflicht: vor Mandatsannahme ueber voraussichtliche Kosten informieren

## Extraktionsfelder

### 1. Anrede (Pflichtfeld für Folge-Skills)

- Vollständige Anredezeile aus der Mail, z. B. "Sehr geehrte Damen und Herren", "Guten Tag, ich heiße Maria Mustermann", "Hallo"
- Falls die Anfragende Person ihre eigene Anredeform nennt (z. B. "Meine Name ist Dr. Klaus-Dieter Müller-Strauss"), diese festhalten.
- Titel aus der Signatur, aus dem E-Mail-Header oder aus dem Fließtext extrahieren.
- Hinweis: Die exakte Anrede wird im Skill `anrede-uebernehmen` weiterverarbeitet.

### 2. Name

- Vorname, Nachname, ggf. akademischer Grad, Adelsprädikat, Doppelname
- Quellen: Signatur, Fließtext, E-Mail-Adresse (Heuristik), Betreffzeile
- Unsicherheit kennzeichnen: `[Name unklar: ...]`

### 3. E-Mail-Adresse

- Absender-Adresse aus dem Header
- Etwaige Rückantwort-Adresse (Reply-To), wenn abweichend
- Verteilerliste/CC-Adressen als Zusatz-Information

### 4. Telefonnummer und weitere Kontaktdaten

- Mobilnummer, Festnetznummer aus Signatur oder Fließtext
- Postanschrift, falls angegeben
- Fax, soweit genannt (selten, aber in manchen Branchen noch üblich)

### 5. Sachverhaltsfetzen

- Stichpunktartige Zusammenfassung des geschilderten Anliegens
- Rechtsgebiet-Zuordnung (Ersteinschätzung, nicht verbindlich): z. B. Mietrecht, Arbeitsrecht, Erbrecht, Strafrecht
- Beteiligte Parteien soweit genannt (Gegner, Behörde, Arbeitgeber, Vermieter etc.)
- Relevante Daten, Beträge, Verträge, Bescheide

### 6. Dringliche Hinweise

- Explizite Fristnennung: Datum, Fristende, Hauptverhandlung, Klagefrist
- Implizite Eile-Signale: "sofort", "dringend", "nächste Woche", "bis Ende der Woche"
- Haftungsrisiken: Versäumnisurteil, Zwangsvollstreckung, Insolvenzantrag
- Hinweis an den Skill `dringlichkeitsmarker` weitergeben

## Heuristiken und Sonderfälle

### E-Mail-Adresse als Namenquelle

Beispiel: `kd.mueller-strauss@example.de` → Hinweis: Vorname K.D., Nachname Müller-Strauss (ungesichert, nur als Interpretations-Hinweis kennzeichnen).

### Keine Anrede vorhanden

Manche Anfragen beginnen direkt mit dem Sachverhalt: "Ich habe von meinem Arbeitgeber eine Kündigung erhalten ...". In diesem Fall:
- Anrede (roh): `[nicht vorhanden]`
- Name aus Signatur oder Fließtext suchen
- Skill `anrede-uebernehmen` erhält den Hinweis, eine neutrale Höflichkeitsform zu verwenden.

### Mehrere Absender / Ehepaar / Erbengemeinschaft

Bei "Wir möchten uns melden ..." oder "Ich schreibe im Namen meiner Mutter ...":
- Alle Personen aufführen
- Hauptkontakt kennzeichnen
- Komplexere Anrede-Heuristik für Skill `anrede-uebernehmen` vormerken

### Sprache der Anfrage

- Erkannte Sprache festhalten (DE / EN / FR / IT / Sonstiges)
- Mehrsprachige Anfragen: Sprache der Hauptaussage priorisieren
- Übergabe an Skill `mehrsprachige-antwort` wenn nicht Deutsch

## Qualitätssicherung

Nach der Extraktion:
1. Vollständigkeit prüfen: Fehlen Pflichtfelder (Name, E-Mail), kennzeichnen und für manuelle Ergänzung markieren.
2. Keine Interpretation über den Wortlaut hinaus: Sachverhaltsfetzen sind Zitate oder direkte Zusammenfassungen, keine rechtliche Würdigung.
3. Keine Rechtsberatung: Dieser Skill erstellt keine rechtliche Bewertung — nur Faktenextraktion.

## Verweise auf andere Skills

- `anrede-uebernehmen` — übernimmt die rohe Anrede und konvertiert sie in die formelle Anredezeile der Antwortmail
- `dringlichkeitsmarker` — wertet die dringlichen Hinweise aus diesem Skill weiter aus
- `spam-und-massen-anfrage-filter` — prüft die geparste Anfrage auf Spam-Muster
- `konfliktcheck-vorab` — verwendet Beteiligte und Gegner aus der Extraktion
- `folgekorrespondenz-vorbereiten` — befüllt den CRM-Skeleton-Eintrag mit den hier extrahierten Daten

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 13 DSGVO
- Art. 28 DSGVO
- Art. 9 DSGVO
- § 203 StGB
- § 4 KSchG
- § 356 StGB
- § 29 VwVfG
- Art. 6 DSGVO
- § 5 TMG
- § 263 StGB
- Art. 32 DSGVO
- Art. 15 DSGVO

### Leitentscheidungen

- BGH VI ZR 7/20
- BGH VI ZR 246/19

