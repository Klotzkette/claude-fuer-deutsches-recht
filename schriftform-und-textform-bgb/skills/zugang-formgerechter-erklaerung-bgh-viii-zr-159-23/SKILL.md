---
name: zugang-formgerechter-erklaerung-bgh-viii-zr-159-23
description: "Für Zugang Formgerechter Erklärung BGH Viii Zr 159 23: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---


## Rechtsgrundlagen

- BGH, Urt. v. 27.11.2024 – Az. VIII ZR 159/23 — qES-Wohnraumkuendigung; Anforderungen an Zugang in der korrespondierenden Form; Stand der Norm vor Einfuehrung des Paragraf 130e ZPO am 17.07.2024. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.11.2024&Aktenzeichen=VIII+ZR+159/23
- **Paragraf 568 Abs. 1 BGB** — Schriftform der Wohnraummiete-Kündigung
- **Paragraf 126 Abs. 3 BGB** i.V.m. **Paragraf 126a Abs. 1 BGB** — Ersatz der Schriftform durch qES
- **Paragraf 130 Abs. 1 S. 1 BGB** — Zugang empfangsbedürftiger Willenserklärungen
- **Paragraf 130e ZPO** — Zugangsfiktion bei gerichtlicher Weiterleitung qualifiziert signierter Dokumente (eingefuehrt 17.07.2024)
- **Paragraf 298 Abs. 3 ZPO** — Transfervermerk bei Ausdruck elektronischer Dokumente durch Gericht
- **eIDAS-Verordnung** VO (EU) Nr. 910/2014 — Definition der qualifizierten elektronischen Signatur

## BGH-Linie — Lehrsatz der Entscheidung

### Sachverhalt (vereinfacht)

Ein Vermieter erklärte die Kündigung des Wohnraummietverhältnisses durch ein elektronisch übermitteltes Dokument mit qualifizierter elektronischer Signatur. Im Rechtsstreit wurde das Dokument durch das Gericht ausgedruckt und mit einem Transfervermerk nach Paragraf 298 Abs. 3 ZPO in die Akte aufgenommen. Die Frage war, ob dieser Ausdruck den formgerechten Zugang der Kündigung beim Mieter bewirkte.

### Entscheidung des BGH

> **Leitsatz**: Die Kündigung eines Wohnraummietverhältnisses durch ein mit einer qualifizierten elektronischen Signatur versehenes Dokument wahrt die Schriftform des Paragraf 568 Abs. 1 BGB i.V.m. Paragraf 126a Abs. 1 BGB nur dann, wenn das elektronische Dokument dem Empfänger so zugegangen ist, dass er die Echtheit der qualifizierten elektronischen Signatur selbst prüfen kann.

> **Zur Frage des Transfervermerks**: Der Ausdruck eines elektronischen Dokuments durch das Gericht mit einem Transfervermerk gemäß Paragraf 298 Abs. 3 ZPO stellt keinen formgerechten Zugang gegenüber dem Erklärungsempfänger dar. Der Transfervermerk dient allein der Dokumentation für die Gerichtsakte, nicht der Herstellung des Zugangs beim Empfänger.

### Dogmatische Begründung

Der BGH stützt die Entscheidung auf folgende Überlegungen:

**Erstens** — **Formzweck**: Die qualifizierte elektronische Signatur soll Identität und Erklärungswillen des Unterzeichners für den Empfänger nachweisbar machen. Dieser Zweck wird nur erfüllt, wenn der Empfänger die Signatur tatsächlich prüfen kann — also das digitale Dokument mit der eingebetteten kryptographischen Signaturinformation erhält.

**Zweitens** — **Gerichtlicher Ausdruck und Paragraf 298 ZPO**: Der Transfervermerk nach Paragraf 298 Abs. 3 ZPO dokumentiert, dass eine elektronische Datei existiert hat und wie sie im Zeitpunkt des Ausdrucks aussah. Er ersetzt aber nicht den direkten Zugang des digitalen Dokuments beim Erklärungsempfänger. Der Mieter hatte das qES-Dokument selbst nie erhalten.

**Drittens** — **Form und Zugang als kumulative Voraussetzungen**: Schriftform/elektronische Form und Zugang sind zwei eigenständige Tatbestandsmerkmale. Die Form muss beim Zugang gewahrt sein — nicht erst nachträglich bei Gericht nachgewiesen werden.

## Workflow

### Praxisablauf für wirksame qES-Kündigung (Vermieter)

```
Schritt 1: Dokument erstellen und qES anbringen
  → Kündigungsschreiben als PDF/A erstellen
  → qES über qualifizierten Vertrauensdiensteanbieter (z. B. D-Trust) anbringen
  → Zertifikats-Gültigkeit prüfen

Schritt 2: Dokument elektronisch übermitteln
  → PDF mit eingebetteter Signatur als E-Mail-Anhang an Mieter senden
  → NICHT ausdrucken und physisch zustellen (dann ist qES nicht mehr prüfbar)
  → Alternativ: über gesicherte Plattform zustellen (De-Mail, EGVP wenn zulässig)

Schritt 3: Zugang sichern
  → Eingangsbestätigung des Mieters anfordern
  → Sendebericht der E-Mail aufbewahren
  → Alternativ: Bote übergibt USB-Stick mit der Datei gegen Quittung

Schritt 4: Empfänger muss Signatur prüfen können
  → Sicherstellen, dass Mieter Software hat oder einfach erhalten kann
  → Adobe Acrobat Reader (kostenlos) oder validator.bund.de reichen
```

### Konsequenzen der Entscheidung für verschiedene Akteure

| Akteur | Konsequenz |
|--------|------------|
| Vermieter (Kündigung) | Ohne sicheren digitalen Zugang der qES-Datei beim Mieter: Kündigung formunwirksam |
| Mieter | Muss qES-Anhänge in E-Mails und WhatsApp auf Künd. prüfen (→ Mandantenwarnung) |
| Gerichte | Paragraf 298 Abs. 3 ZPO-Ausdruck reicht für Zugang beim Erklärungsempfänger nicht |
| Anwälte | Schriftsatz mit qES-Anlage muss über Postfach des Mandanten zugehen, nicht nur Gerichtspost |

### Empfehlung für die Praxis bis zur gesetzlichen Klarstellung

**Vermieter**: Kündigung per Papier mit Originalunterschrift und Bote oder Einschreiben bleibt die sicherste Option. qES-Versand per E-Mail ist rechtlich möglich, birgt aber das Zugangsrisiko (Spam-Filter, technische Probleme).

**Mieter**: Nach dieser Entscheidung ist es künftig denkbar, dass wirksame Kündigungen per E-Mail mit qES-Anhang zugehen können. E-Mail-Postfach und WhatsApp-Nachrichten auf solche Anhänge prüfen und nicht vorschnell löschen (→ `mandantenwarnung-qes-per-email-whatsapp-und-zugang`).

## Templates

### Gesprächsvorlage Vermieter-Beratung qES-Kündigung

```
Thema: Kündigung Wohnraummiete per qualifizierter elektronischer Signatur


Die Kündigung per qES ist grundsätzlich zulässig (Paragraf 568 Abs. 1 BGB i.V.m.
Paragraf 126a Abs. 1 BGB). Aber: Das qES-Dokument muss dem Mieter so zugehen,
dass er die Signatur prüfen kann. Ein späterer Gerichtsausdruck mit
Transfervermerk (Paragraf 298 Abs. 3 ZPO) reicht nicht.

Unsere Empfehlung: Kündigung als PDF mit qES per E-Mail an Mieter;
Eingangsbestätigung anfordern; Sendebericht sichern. Alternativ: Papier
mit Originalunterschrift, übergeben durch Boten gegen Quittung.
```

## Fallstricke

- **Nur ein Ausdruck ist kein Zugang**: Viele Anwälte und Richter übersehen, dass Paragraf 298 Abs. 3 ZPO-Ausdrucke nur für die Gerichtsakte bestimmt sind — nicht für den Beweis des Zugangs beim Erklärungsempfänger.
- **E-Mail im Spam**: qES-Dokument per E-Mail gesendet, landet im Spam-Filter des Mieters → technisch eingegangen, aber Zugang str. Besser: Eingangsbestätigung anfordern.
- **WhatsApp-Anhang mit qES**: Technisch möglich, aber unüblich und Zugang schwer nachzuweisen. Empfehlung: E-Mail mit Eingangsbestätigung bevorzugen.

## Querverweise

- → `elektronische-form-paragraph-126a-bgb-qes`
- → `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `kuendigung-per-schriftsatz-zustellung-formfragen`

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
