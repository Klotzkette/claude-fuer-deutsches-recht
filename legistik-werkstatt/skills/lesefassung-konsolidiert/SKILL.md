---
name: lesefassung-konsolidiert
description: "Erstellt eine Lesefassung des geaenderten Stammgesetzes in der nach Inkrafttreten gueltigen Form. Einheitlich gelesen ohne Aenderungsmarkierung. Hilfreich fuer Adressaten und Vollzugsbehoerden. Pro Stammgesetz eine eigene Datei. Praezise Datierung Stand nach Inkrafttreten des neuen Gesetzes und der zugehoerigen Verordnung. Mit Pruefliste Format-Konventionen Inkrafttretens-Handling Verweis-Pflege Beispiel-Header DOCX-Ausgabe-Konventionen."
---

# Lesefassung konsolidiert

> Wie sieht das Gesetz aus, wenn das neue Gesetz in Kraft getreten ist? Klipp und klar zum Mitlesen.

## Zweck

Die Lesefassung zeigt das Stammgesetz in der nach Inkrafttreten gueltigen Form — **ohne** Aenderungsmarkierung, **mit** allen Aenderungen eingearbeitet. Adressaten (Buerger, Unternehmen) und Vollzugsbehoerden brauchen diese Fassung, um zu sehen, „wie es ab Tag X heisst", ohne den Aenderungs-Diff lesen zu muessen.

Komplementaer zu:
- **Synopse**: zeigt alt vs. neu in zwei Spalten
- **Aenderungsanordnung**: zeigt die Aenderung als Befehl („Paragraf 3 Absatz 2 wird wie folgt geaendert: ...")
- **Lesefassung**: zeigt das fertige neue Gesetz

## 1) Inhalte pro Datei

Eine Datei je Stammgesetz. Bei einem Aenderungsgesetz, das mehrere Stammgesetze beruehrt, entsprechend mehrere Lesefassungen.

### Header-Block

```
Lesefassung [Name des Stammgesetzes]
Stand nach Inkrafttreten des [Aenderungs-Gesetz-Name] vom [Datum BGBl. Fundstelle]
und der [Zugehoerigen Verordnung] vom [Datum BGBl. Fundstelle]

Konsolidiert auf den [Datum].
Erstellt durch: [Referat / Verantwortlicher / Pruefer]
```

### Format

- Markdown mit Ueberschrift pro Paragraf: `## § 3 Antragstellung`
- Absaetze als Aufzaehlung mit Klammer-Zahl: `(1) ...`, `(2) ...`
- Saetze nicht nummeriert (auch wenn Gesetz Satz-Nr. hat — die folgen im Text)
- Aufzaehlungen mit `1.`, `a)`, `aa)` wie im Gesetz
- DOCX-Export fuer offizielle Versendung an Adressaten und Vollzugsbehoerden

## 2) Was muss in die Lesefassung

### Geaenderte Paragrafen

Mit dem **neuen Wortlaut** komplett. Auch wenn nur ein Komma geaendert wurde — der gesamte Paragraf, damit die Lesefassung in sich konsistent ist.

### Nicht-geaenderte, aber bezugsrelevante Paragrafen

Bei sehr stark auf andere Paragrafen verweisenden Gesetzen ist es sinnvoll, **alle** Paragrafen aufzunehmen, damit der Adressat nicht zwischen zwei Dokumenten springen muss.

### Anlagen, soweit Bestandteil des Gesetzes

Mit Verweis und gegebenenfalls verlinkt. Bei umfangreichen Anlagen ggf. separate Datei.

### Inkrafttretens-Vorschriften

Am Ende der Lesefassung in einer Klar-Kennzeichnung:

```
Diese Lesefassung gilt ab dem [Datum].
Bis zum [Datum] gilt die vorherige Fassung (siehe Aenderungsanordnung vom ...).
```

### Stand und Datum

Das Datum des **Inkrafttretens** ist massgeblich. Bei stufenweisem Inkrafttreten mehrere Lesefassungen erstellen (z.B. „Lesefassung Stand 01.01.2026" und „Lesefassung Stand 01.07.2026").

## 3) Pruefliste vor Freigabe

### Vollstaendigkeit

- [ ] Alle vom Aenderungsgesetz beruehrten Paragrafen aufgenommen
- [ ] Anlagen aktualisiert
- [ ] Inkrafttretens-Datum klar dokumentiert
- [ ] Stand-Datum (Konsolidierung) klar dokumentiert

### Konsistenz

- [ ] Numerierung konsistent (keine doppelten Paragrafen, keine Luecken)
- [ ] Verweise innerhalb des Gesetzes aktualisiert (z.B. „Paragraf 3 Absatz 4" stimmt jetzt, nachdem Absatz 3 weggefallen ist)
- [ ] Verweise auf externe Normen aktualisiert (z.B. wenn EuGVVO geaendert wurde, deren Verweise aktualisieren)
- [ ] Begriffsdefinitionen konsistent (wenn `Verbraucher` neu definiert ist, ueberall der neue Begriff)

### Format

- [ ] Markdown-Lesefassung erstellt
- [ ] DOCX-Lesefassung erstellt
- [ ] Header-Block vorhanden mit Stand und Inkrafttreten
- [ ] Gerichts-/Adressaten-tauglich (keine Entwurfs-Wasserzeichen, kein Track Changes)

### Kontrolle

- [ ] Stichprobe: 3-5 Paragrafen mit dem amtlichen BGBl-Text abgeglichen
- [ ] Aenderungsanordnung gegengelesen — wurde alles umgesetzt?
- [ ] Zweitlesung durch zweite Person empfohlen

## 4) Typische Fehler

1. **Inkrafttretens-Verschachtelung uebersehen.** Wenn das Aenderungsgesetz mehrere Inkrafttretens-Daten hat (typisch bei Uebergangsregelungen), braucht es mehrere Lesefassungen.
2. **Verweise nicht nachgezogen.** Wenn Paragraf 3 Absatz 3 entfaellt, muss in Paragraf 7 der Verweis auf „Paragraf 3 Absatz 3" angepasst werden.
3. **Anlagen vergessen.** Bei BGBl-Veroeffentlichung sind Anlagen oft separat — leicht zu uebersehen.
4. **Standard-Header fehlt.** Adressaten muessen erkennen koennen, **welcher** Stand vorliegt.
5. **DOCX mit Track Changes ausgegeben.** Lesefassung ist per Definition ohne Aenderungsmarkierung — Word-Datei vor Export bereinigen.
6. **Zwei Stammgesetze in einer Datei.** Bei einem Aenderungsgesetz, das BGB und HGB anpasst, **zwei** Lesefassungen — eine fuer BGB, eine fuer HGB.

## 5) Verhaeltnis zur amtlichen Konsolidierung

Die Lesefassung ist **kein** amtliches Dokument. Die amtliche Konsolidierung erfolgt durch das Bundesministerium der Justiz fuer die [www.gesetze-im-internet.de](https://www.gesetze-im-internet.de) — meist mit zeitlicher Verzoegerung von einigen Wochen bis Monaten nach Verkuendung. Vorlaeufige Lesefassungen sind sinnvoll, weil:

- die Adressaten frueher Klarheit brauchen
- die Vollzugsbehoerden die Anwendung vorbereiten muessen
- der parlamentarische Beratungsbedarf ohne Lesefassung erschwert ist

**Wichtig im Header**: Klar machen, dass es sich um eine **Arbeits-Lesefassung** handelt, nicht um den amtlichen Wortlaut.

## 6) Anschluss

- `xml-paralleldarstellung` — bei XML-pflichtigen Veroeffentlichungen
- `synopse-erstellen` — fuer den Aenderungs-Diff alt vs. neu
- `dokumente-rendern-docx-pdf` — fuer den DOCX-/PDF-Export der Lesefassung
- `referentenentwurf-bauen` — bei aenderbarem Entwurfsstand
- `inkrafttreten-uebergangsrecht` — bei stufenweisem Inkrafttreten oder Uebergangsregelungen
