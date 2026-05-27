---
name: lesefassung-konsolidiert
description: "Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Aenderung aussieht ohne Aenderungsmarkierungen. Einheitlich lesbar ohne Aenderungsmarkierung Datierung Stand nach Inkrafttreten. Format-Konventionen Inkrafttretens-Handling Verweis-Pflege DOCX-Ausgabe. Output Lesefassung pro Stammgesetz bereinigt datiert. Abgrenzung zu synopse-erstellen Gegenueberestellung alt und neu."
---

# Lesefassung konsolidiert

> Wie sieht das Gesetz aus, wenn das neue Gesetz in Kraft getreten ist? Klipp und klar zum Mitlesen.

## Zweck

Die Lesefassung zeigt das Stammgesetz in der nach Inkrafttreten gültigen Form — **ohne** Änderungsmarkierung, **mit** allen Änderungen eingearbeitet. Adressaten (Bürger, Unternehmen) und Vollzugsbehörden brauchen diese Fassung, um zu sehen, „wie es ab Tag X heisst", ohne den Änderungs-Diff lesen zu müssen.

Komplementär zu:
- **Synopse**: zeigt alt vs. neu in zwei Spalten
- **Änderungsanordnung**: zeigt die Änderung als Befehl („Paragraf 3 Absatz 2 wird wie folgt geändert: ...")
- **Lesefassung**: zeigt das fertige neue Gesetz

## 1) Inhalte pro Datei

Eine Datei je Stammgesetz. Bei einem Änderungsgesetz, das mehrere Stammgesetze beruehrt, entsprechend mehrere Lesefassungen.

### Header-Block

```
Lesefassung [Name des Stammgesetzes]
Stand nach Inkrafttreten des [Aenderungs-Gesetz-Name] vom [Datum BGBl. Fundstelle]
und der [Zugehoerigen Verordnung] vom [Datum BGBl. Fundstelle]

Konsolidiert auf den [Datum].
Erstellt durch: [Referat / Verantwortlicher / Pruefer]
```

### Format

- Markdown mit Überschrift pro Paragraf: `## § 3 Antragstellung`
- Absätze als Aufzaehlung mit Klammer-Zahl: `(1) ...`, `(2) ...`
- Sätze nicht nummeriert (auch wenn Gesetz Satz-Nr. hat — die folgen im Text)
- Aufzaehlungen mit `1.`, `a)`, `aa)` wie im Gesetz
- DOCX-Export für offizielle Versendung an Adressaten und Vollzugsbehörden

## 2) Was muss in die Lesefassung

### Geaenderte Paragrafen

Mit dem **neuen Wortlaut** komplett. Auch wenn nur ein Komma geändert wurde — der gesamte Paragraf, damit die Lesefassung in sich konsistent ist.

### Nicht-geänderte, aber bezugsrelevante Paragrafen

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

## 3) Prüfliste vor Freigabe

### Vollständigkeit

- [ ] Alle vom Änderungsgesetz beruehrten Paragrafen aufgenommen
- [ ] Anlagen aktualisiert
- [ ] Inkrafttretens-Datum klar dokumentiert
- [ ] Stand-Datum (Konsolidierung) klar dokumentiert

### Konsistenz

- [ ] Numerierung konsistent (keine doppelten Paragrafen, keine Lücken)
- [ ] Verweise innerhalb des Gesetzes aktualisiert (z.B. „Paragraf 3 Absatz 4" stimmt jetzt, nachdem Absatz 3 weggefallen ist)
- [ ] Verweise auf externe Normen aktualisiert (z.B. wenn EuGVVO geändert wurde, deren Verweise aktualisieren)
- [ ] Begriffsdefinitionen konsistent (wenn `Verbraucher` neu definiert ist, überall der neue Begriff)

### Format

- [ ] Markdown-Lesefassung erstellt
- [ ] DOCX-Lesefassung erstellt
- [ ] Header-Block vorhanden mit Stand und Inkrafttreten
- [ ] Gerichts-/Adressaten-tauglich (keine Entwurfs-Wasserzeichen, kein Track Changes)

### Kontrolle

- [ ] Stichprobe: 3-5 Paragrafen mit dem amtlichen BGBl-Text abgeglichen
- [ ] Änderungsanordnung gegengelesen — wurde alles umgesetzt?
- [ ] Zweitlesung durch zweite Person empfohlen

## 4) Typische Fehler

1. **Inkrafttretens-Verschachtelung übersehen.** Wenn das Änderungsgesetz mehrere Inkrafttretens-Daten hat (typisch bei Übergangsregelungen), braucht es mehrere Lesefassungen.
2. **Verweise nicht nachgezogen.** Wenn Paragraf 3 Absatz 3 entfaellt, muss in Paragraf 7 der Verweis auf „Paragraf 3 Absatz 3" angepasst werden.
3. **Anlagen vergessen.** Bei BGBl-Veröffentlichung sind Anlagen oft separat — leicht zu übersehen.
4. **Standard-Header fehlt.** Adressaten müssen erkennen koennen, **welcher** Stand vorliegt.
5. **DOCX mit Track Changes ausgegeben.** Lesefassung ist per Definition ohne Änderungsmarkierung — Word-Datei vor Export bereinigen.
6. **Zwei Stammgesetze in einer Datei.** Bei einem Änderungsgesetz, das BGB und HGB anpasst, **zwei** Lesefassungen — eine für BGB, eine für HGB.

## 5) Verhältnis zur amtlichen Konsolidierung

Die Lesefassung ist **kein** amtliches Dokument. Die amtliche Konsolidierung erfolgt durch das Bundesministerium der Justiz für die [www.gesetze-im-internet.de](https://www.gesetze-im-internet.de) — meist mit zeitlicher Verzoegerung von einigen Wochen bis Monaten nach Verkündung. Vorläufige Lesefassungen sind sinnvoll, weil:

- die Adressaten früher Klarheit brauchen
- die Vollzugsbehörden die Anwendung vorbereiten müssen
- der parlamentarische Beratungsbedarf ohne Lesefassung erschwert ist

**Wichtig im Header**: Klar machen, dass es sich um eine **Arbeits-Lesefassung** handelt, nicht um den amtlichen Wortlaut.

## 6) Anschluss

- `xml-paralleldarstellung` — bei XML-pflichtigen Veröffentlichungen
- `synopse-erstellen` — für den Änderungs-Diff alt vs. neu
- `dokumente-rendern-docx-pdf` — für den DOCX-/PDF-Export der Lesefassung
- `referentenentwurf-bauen` — bei aenderbarem Entwurfsstand
- `inkrafttreten-uebergangsrecht` — bei stufenweisem Inkrafttreten oder Übergangsregelungen
## Aktuelle Rechtsprechung & Leitsätze

- BVerfG, Beschl. v. 15.01.2002 — 1 BvR 1783/99, BVerfGE 104, 357 Rn. 25 — Normenklarheits-Gebot erfordert, dass Buerger und Gerichte Geltungsinhalt eines Gesetzes ohne unzumutbaren Aufwand ermitteln koennen; unuebersichtliche Aenderungskette kann Normenklarheit verletzen
- BVerwG, Urt. v. 28.07.2011 — 2 C 28.10, NVwZ 2012, 26 — Lesefassung als Hilfsmittel hat keine eigenstaendige Rechtswirkung; Geltung richtet sich stets nach dem im BGBl. veroeffentlichten Originaltext; abweichende Lesefassung begrundet keine Rechte
- BGH, Urt. v. 26.04.2017 — VIII ZR 233/15, NJW 2017, 2268 — bei Kollision zwischen Originalgesetz und nichtamtlicher Lesefassung hat Originaltext Vorrang; Richtigkeits-Garant liegt beim amtlichen Bundesgesetzblatt

## Zentrale Normen (Paragrafenkette)

Art. 82 GG (Ausfertigung und Verkuendung) — § 1 BGBlG (Bundesgesetzblatt als amtliche Quelle) — §§ 1-5 NormDokVO (Normdokumentations-Verordnung) — Art. 20 Abs. 3 GG (Normklarheit als Rechtsstaatsprinzip)

## Kommentarliteratur

- Maunz/Dürig, GG, Art. 82 Rn. 1 ff. (Verkuendung, Normursprungs-Frage)
- Schneider, Gesetzgebung, 3. Aufl. 2002, § 7 Rn. 1 ff. (Normfassung, Konsolidierung)
