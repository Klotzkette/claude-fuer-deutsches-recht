---
name: verarbeitungsverzeichnis-vvt-generator
description: "Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren. Art. 30 DSGVO VVT-Pflicht. Prüfraster: Pflichtangaben Art. 30 Abs. 1 Verantwortlicher Zweck Kategorien Empfaenger Fristen Maßnahmen. Output: vollständiges VVT je Verarbeitungstätigkeit. Abgrenzung: nicht fü..."
---

# VVT — Verzeichnis von Verarbeitungstätigkeiten

## Eingaben

- Anzahl Beschäftigte
- Branche / Geschäftsmodell
- Existierende AVV-Verträge
- Existierende DSFA-Auswertungen
- Verarbeitungs-Übersicht (welche Prozesse?)
- Dienstleister-Liste (Auftragsverarbeiter)

## Schritt 1 — Anwendungsbereich Art. 30 Abs. 5 DSGVO

### Grundregel

- VVT-Pflicht für **alle** Verantwortlichen und Auftragsverarbeiter

### Ausnahme

- Unternehmen mit **weniger als 250 Beschäftigten**
- Wenn Verarbeitungs nicht **regelmäßig**
- Wenn keine **besonderen Kategorien** Art. 9 oder strafrechtlichen Daten
- Wenn kein **Risiko für Rechte und Freiheiten** der Betroffenen

### Praktische Konsequenz

- **Fast alle Unternehmen** ab eingen Beschäftigten — VVT Pflicht
- HR-Verarbeitung führt regelmäßig zu Pflicht
- Auch Kleinunternehmen oft pflichtig
- **Sicherer Weg:** VVT erstellen unabhängig von Schwellen

## Schritt 2 — Inhalts-Pflichten Verantwortlicher Art. 30 Abs. 1

### Pro Verarbeitungs-Tätigkeit

a) **Name und Kontaktdaten** Verantwortlicher (und ggf. gemeinsam Verantwortliche Vertreter DSB)

b) **Zwecke** der Verarbeitung

c) **Kategorien** Betroffener

d) **Kategorien** personenbezogene Daten

e) **Kategorien** Empfänger (auch in Drittländern und internationale Organisationen)

f) Bei **Drittland-Übermittlungen** — Drittland-Bezeichnung und ggf. Geeignete Garantien (Art. 46) oder Bezeichnung als Übermittlung nach Art. 49

g) **Geplante Lösch-Fristen** der Daten-Kategorien

h) **Allgemeine Beschreibung der technischen und organisatorischen Maßnahmen** Art. 32

## Schritt 3 — Inhalts-Pflichten Auftragsverarbeiter Art. 30 Abs. 2

### Pro Auftrag

a) **Name und Kontaktdaten** Auftragsverarbeiter und jedes Verantwortlichen für den der Auftragsverarbeiter tätig wird

b) **Kategorien** Verarbeitungs-Tätigkeiten im Auftrag

c) **Drittland-Übermittlungen** wie beim Verantwortlichen

d) **Allgemeine Beschreibung TOMs**

## Schritt 4 — VVT-Struktur und Format

### Schriftlich oder elektronisch

- **Schriftform** ausreichend
- **Elektronisch** häufiger (Excel CRM-Modul Datenschutz-Software)
- **Vorlage** bei Aufsichtsbehörde auf Anforderung Art. 30 Abs. 4 DSGVO

### Empfohlene Struktur

```
VVT [Unternehmens-Name]
Stand: [Datum]
Verantwortlicher: [Name Anschrift]
DSB: [Name]

Aufgenommen: [Datum]
Letzte Änderung: [Datum]

Verarbeitungs-Tätigkeit Nr. [N]:

Zweck der Verarbeitung:
[Konkrete Beschreibung]

Rechtsgrundlage (Art. 6 / 9 DSGVO) — EMPFOHLEN
(Art. 30 fordert das nicht ausdrücklich, ist aber
für Aufsichtsbehörden-Prüfung sehr hilfreich):
[Rechtsgrundlage]

Kategorien Betroffener:
[z.B. Beschäftigte, Kunden, Lieferanten, Bewerber]

Datenkategorien:
[z.B. Stammdaten, Vertragsdaten, Zahlungsdaten,
besondere Kategorien]

Empfänger:
[z.B. Dienstleister IT, Lohnbüro, Behörden]

Drittland-Übermittlung:
[Ja/Nein; bei Ja: Land und Garantien]

Lösch-Frist:
[z.B. 10 Jahre nach Vertragsende — gesetzliche
Aufbewahrungspflicht]

TOMs:
[Verweis auf TOMs-Dokument]
```

## Schritt 5 — Typische Verarbeitungs-Tätigkeiten

### Personalwesen

- **Bewerber-Management**
- **Personalakten**
- **Gehalts-Abrechnung**
- **Zeit-Erfassung**
- **Personalentwicklung**
- **Krankheits-Verwaltung**

### Kunden-Beziehung

- **Vertrags-Anbahnung**
- **Vertragsabwicklung**
- **Kundenservice**
- **Marketing / Newsletter**
- **Kundenbewertungen**

### Lieferanten

- **Vertragsanbahnung**
- **Vertragsabwicklung**
- **Zahlungs-Verkehr**
- **Sanktions-Screening**

### Eigene Verarbeitung

- **Buchhaltung**
- **Steuer-Erklärung**
- **Compliance**
- **Risk-Management**
- **IT-Security-Logs**

### Webseite und Online

- **Cookies und Tracking**
- **Web-Analyse**
- **Newsletter**
- **Kontakt-Formular**

## Schritt 6 — Drittland-Übermittlung im VVT

### Pflichten

- **Drittland bezeichnen**
- **Empfänger nennen**
- **Garantie nach Art. 46 DSGVO** spezifizieren:
 - SCC (Standard-Vertrags-Klauseln)
 - BCR (Binding Corporate Rules)
 - Verhaltens-Regeln Art. 40
 - Zertifizierung Art. 42
 - Internationales Abkommen (z.B. EU-US Data Privacy Framework)
- Bei Art. 49 Ausnahme bezeichnen (Einwilligung Vertrag Lebenswichtige Interessen etc.)

### Anhang TIA (Transfer Impact Assessment)

- Bei jeder Drittland-Übermittlung
- Skill `drittlandstransfer-pruefung`

## Schritt 7 — Aktualisierungs-Management

### Anlässe für Aktualisierung

- **Neue Verarbeitungs-Tätigkeit** (z.B. neues Tool eingesetzt)
- **Geänderter Zweck** (z.B. Marketing-Verarbeitung)
- **Neuer Dienstleister** (AVV-Bezug)
- **Drittland-Wechsel**
- **Geänderte Lösch-Fristen**
- **Neue Datenkategorien**

### Frequenz

- **Bei jeder Änderung** zeitnah
- **Mindestens jährliche Vollprüfung**
- **Nach DSFA-Aktualisierung**

### Verantwortliche

- **DSB** koordinierend
- **Fachbereich** für inhaltliche Aktualisierung
- **IT** für TOMs-Bestätigung

## Schritt 8 — Verzahnung mit AVV Art. 28 DSGVO

### Auftragsverarbeitung in VVT

- Pro AVV → Eintrag in VVT
- AVV-Inhalt teilweise direkt übernehmbar
- Vertragsbeginn / -ende dokumentieren

### Sub-Verarbeiter

- Bei Genehmigung Sub-Auftragsverarbeiter — neue VVT-Position
- Bei Sub-Auftragsverarbeiter-Wechsel — VVT-Update

## Schritt 9 — Verzahnung mit DSFA Art. 35

### DSFA-Pflicht-Verarbeitungen

- Hohes Risiko für Rechte und Freiheiten
- Im VVT besonders zu markieren
- DSFA-Ergebnis dokumentieren
- TOMs aus DSFA übernehmen

### Bei Hochrisiko KI-System

- DSFA plus Grundrechte-Folgenabschätzung (Art. 27 KI-VO)
- Skill `ki-verordnung-compliance`

## Schritt 10 — Pflicht-Vorlage Aufsichtsbehörde

### Anlässe

- **Aufsichtsbehörden-Anfrage** Standard-Auskunft
- **Datenpanne-Meldung** mit VVT-Bezug
- **DSGVO-Prüfung** (Audit)
- **Bei Bußgeld-Verfahren**

### Form der Vorlage

- Schriftlich elektronisch
- Vollständigkeit
- Aktualität
- Sprache deutsch

### Bei Mangel

- Bußgeld nach Art. 83 Abs. 4 lit. a DSGVO (bis EUR 10 Mio oder 2 Prozent Konzernumsatz)
- Aufforderung zur Nach-besserung mit Frist

## Schritt 11 — Praktische Aufbau-Schritte

### Phase 1 — Bestandsaufnahme

- Workshop mit allen Fachbereichen
- Verarbeitungs-Inventar
- Daten-Fluss-Diagramm

### Phase 2 — Strukturierung

- Tätigkeits-Liste
- Kategorisierung
- Datenkategorien-Mapping

### Phase 3 — Dokumentation

- VVT-Vorlage ausfüllen
- DSB-Review
- Geschäftsführung-Freigabe

### Phase 4 — Aktualisierung

- Change-Management-Prozess
- Periodische Reviews
- Trigger-basierte Updates

## Schritt 12 — Tool-Empfehlung

### Excel-basiert

- Sinnvoll für kleinere Organisation
- Vorlagen vom BfDI / Aufsichtsbehörden

### Datenschutz-Software

- Otris
- DataGuard
- Activemind
- bestätigt durch BSI-Standards

### CRM-/IT-Integration

- Automatische Erkennung Verarbeitungen
- Anbindung an AVV-Datenbank
- Anbindung an DSFA-Tool

## Schritt 13 — Beispiel Verarbeitungs-Tätigkeit

```
Verarbeitungs-Tätigkeit Nr. 5: Newsletter-Versand

Zweck: Information bestehender und potentieller
Kunden über Produkt-Updates und Branchen-Themen

Rechtsgrundlage: Art. 6 Abs. 1 lit. a DSGVO
(Einwilligung); § 7 Abs. 2 Nr. 3 UWG bei
Bestandskunden

Kategorien Betroffener: Kunden, Interessenten,
Newsletter-Abonnenten

Datenkategorien:
- E-Mail-Adresse
- Vor- und Nachname (optional)
- Einwilligungs-Datum und -Inhalt
- Anrede (optional)
- Click-Verhalten (Öffnungsrate, Click-Tracking)

Empfänger:
- Newsletter-Versand-Dienstleister Mailchimp Inc. (USA)
- Interne Vertriebs- und Marketing-Abteilung

Drittland-Übermittlung:
USA, Mailchimp Inc.
Garantie: EU-US Data Privacy Framework
(Aktualisierung 2023)
TIA durchgeführt: ja, Skill drittlandstransfer-pruefung

Lösch-Frist:
- Aktive Abonnenten: Bis zum Widerruf
- Nach Widerruf: 3 Jahre Aufbewahrung der
 Widerrufs-Information (Beweis-Funktion)
- Click-Verhalten: 13 Monate (Statistik-Auswertung)

TOMs:
- HTTPS-Verschlüsselung
- Pseudonymisiertes Tracking
- Mailchimp ISO 27001 zertifiziert
- AVV vorhanden gem. Art. 28 DSGVO
```

## Verzahnung mit anderen Skills

- `dsfa-erstellung` — bei DSFA-pflichtigen Verarbeitungen
- `avv-pruefung` — bei Auftragsverarbeitung
- `drittlandstransfer-pruefung` — bei Drittland-Bezug
- `ki-verordnung-compliance` — bei KI-Verarbeitung
- `anwendungsfall-triage` — bei neuem Anwendungsfall
- `datenpanne-meldung` — bei Vorfall

## Ausgabe

- `vvt-{unternehmen}.md` strukturierte VVT-Erstellung
- Erstausgabe Excel oder Markdown
- Aktualisierungs-Trigger-Liste
- Aufsichts-Behörden-Antwort-Vorbereitung
- Frist im Fristenbuch (jährlich Vollprüfung)

## Quellen

- DSGVO Art. 30 5 6 9 30 32 35 46 49
- BDSG-Anpassungen
- KI-VO Art. 27
- BfDI-Mustervorlagen
- DSK Kurzpapiere zur VVT
- EDSA Guidelines
- BVerfG-Linien zur Datenschutz-Verantwortung

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Erstmals anlegen oder bestehenden VVT aktualisieren?
2. Aus Sicht des Verantwortlichen (Art. 30 Abs. 1 DSGVO) oder Auftragsverarbeiters (Art. 30 Abs. 2)?
3. Unterliegt die Organisation der Pflicht? (Art. 30 Abs. 5 DSGVO: unter 250 Mitarbeiter nur bei bestimmten Verarbeitungen)
4. Welche Quellen stehen bereit? (bestehende Systemliste, AVV-Bestand, IT-Asset-Verzeichnis)

## Output-Template — VVT-Eintrag (Verantwortlicher)

**Adressat:** DSB / Aufsichtsbehörde — Tonfall: sachlich-strukturiert

```
VVT-Eintrag [DATUM]
Verantwortlicher: [NAME, ADRESSE, VERTRETER]
DSB: [NAME, KONTAKT] (falls bestellt)

Verarbeitungstätigkeit: [BEZEICHNUNG]
Zweck(e): [ZWECKE nach Art. 30 Abs. 1 lit. b]
Betroffene Gruppen: [GRUPPEN nach Art. 30 Abs. 1 lit. c]
Datenkategorien: [KATEGORIEN nach Art. 30 Abs. 1 lit. c]
Empfaenger (Kategorien): [EMPFAENGER nach Art. 30 Abs. 1 lit. d]
Drittlandtransfer: [LAND / Schutzmechanismus nach Art. 30 Abs. 1 lit. e]
Loeschfristen: [FRISTEN nach Art. 30 Abs. 1 lit. f]
TOM (Verweis): Art. 32 DSGVO — Anlage [X]
Rechtsgrundlage (Empfehlung): Art. [X] DSGVO [§ BDSG]
```

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
