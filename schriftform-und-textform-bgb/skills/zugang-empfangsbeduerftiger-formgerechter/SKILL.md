---
name: zugang-empfangsbeduerftiger-formgerechter
description: "Zugang Empfangsbeduerftiger Formgerechter: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zugang Empfangsbeduerftiger Formgerechter

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Zugang Empfangsbeduerftiger Formgerechter** im Plugin Schriftform/Textform BGB. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb` | Mandant fragt: Wann gilt Kündigung Mahnung oder sonstige Erklärung als zugegangen und ab wann laeuft die Frist? § 130 BGB Zugang. Prüfraster: Machtbereichslehre Möglichkeit der Kenntnisnahme Zugangsvereitelung Annahmeverweigerung Briefkasten-Grundsaetze abweichende Grundsaetze Unternehmen mit Eingangsstempel. Output: Zugangs-Prüfprotokoll und Empfehlung Beweissicherung. Abgrenzung zu zugang-formgerechter-erklärung-bgh-viii-zr-159-23 (qES-spezifisch) und wohnraummiete-kündigung-paragraph-568-bgb. |
| `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` | Prüffeld für zugang formgerechter erklaerung bgh viii zr 159 23: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Schriftform/Textform BGB gilt für **Zugang Empfangsbeduerftiger Formgerechter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb`

**Fokus:** Mandant fragt: Wann gilt Kündigung Mahnung oder sonstige Erklärung als zugegangen und ab wann laeuft die Frist? § 130 BGB Zugang. Prüfraster: Machtbereichslehre Möglichkeit der Kenntnisnahme Zugangsvereitelung Annahmeverweigerung Briefkasten-Grundsaetze abweichende Grundsaetze Unternehmen mit Eingangsstempel. Output: Zugangs-Prüfprotokoll und Empfehlung Beweissicherung. Abgrenzung zu zugang-formgerechter-erklärung-bgh-viii-zr-159-23 (qES-spezifisch) und wohnraummiete-kündigung-paragraph-568-bgb.

# Zugang empfangsbedürftiger Willenserklärungen § 130 BGB

## Rechtsgrundlagen

- **§ 130 Abs. 1 S. 1 BGB** — Willenserklärung wird wirksam, sobald sie dem Empfänger zugeht (unter Abwesenden)
- **§ 130 Abs. 1 S. 2 BGB** — Widerruf: wirksam, wenn Widerruf nicht später als die Erklärung zugeht
- **§ 130 Abs. 2 BGB** — Zugang auch wenn Erklärende bereits gestorben oder geschäftsunfähig geworden
- **§ 130 Abs. 3 BGB** — Nicht-empfangsbedürftige Willenserklärungen (z. B. Testament) ausgenommen
- **§ 132 BGB** — Zugang durch Zustellung (gerichtliche Zustellung als Zugangsersatz)

## BGH-Linie

### Machtbereichslehre (ständige BGH-Rechtsprechung)

Eine Willenserklärung geht zu, wenn sie so in den **Machtbereich des Empfängers** gelangt, dass der Empfänger unter normalen Umständen die **Möglichkeit der Kenntnisnahme** hat.

Maßgebend ist der **Empfänger-Horizont**: Wann ist gewöhnlicherweise mit Kenntnisnahme zu rechnen?

**Briefkasten-Grundsätze (BGH-Dauerrechtsprechung)**:
- Einwurf in den Briefkasten bis zur üblichen Postzustellungszeit → Zugang noch an diesem Tag
- Einwurf nach der üblichen Postzustellungszeit (z. B. abends 18 Uhr) → Zugang erst am nächsten Werktag
- Bei gewerblichem Empfänger: Bürozeiten maßgebend

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- E-Mail geht zu, wenn sie auf dem Mailserver des Empfängers eingegangen und abrufbar ist
- Nicht erst, wenn der Empfänger sie tatsächlich gelesen hat
- Absendung allein reicht nicht: Eingang im Postfach des Empfängers erforderlich

### Zugangsvereitelung

Wer den Zugang vereitelt (z. B. Briefkasten zugeklebt, Empfangsbekenntnis verweigert, E-Mail-Postfach gelöscht), muss sich so behandeln lassen, als ob die Erklärung zugegangen wäre — § 242 BGB, Treuwidrigkeitseinwand.

### Annahmeverweigerung

Weigert sich der Empfänger, ein Schriftstück entgegenzunehmen (z. B. eingeschriebener Brief zurückgegeben), so ist die Erklärung dennoch zugegangen, wenn:
- Die Weigerung grundlos war
- Der Empfänger Kenntnis vom Inhalt hatte oder haben konnte

Grundloses Zurückweisen eines eingeschriebenen Briefs: Zugang mit Rückgabezeitpunkt fingiert (BGH-Rechtsprechung).

## Workflow

### Zugangszeitpunkt nach Medium

| Übermittlungsweg | Zugangszeitpunkt |
|-----------------|-----------------|
| Brief (Briefkasten) | Bei Einwurf während üblicher Zustellzeit: sofort; nach Zustellzeit: nächster Werktag |
| Einschreiben (Benachrichtigung) | Nicht bei Hinterlegung auf Postamt, sondern bei tatsächlichem Empfang |
| Bote (persönliche Übergabe) | Übergabe oder Einwurf |
| E-Mail (Empfänger-Postfach) | Eingang auf Empfänger-Mailserver, wenn abrufbar |
| Fax | Eingang im Speicher des Empfänger-Faxgeräts |
| WhatsApp / Messenger | Eingang auf Empfänger-Gerät (Doppelhaken) — str. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

### Beweislast Zugang

Der **Erklärende trägt die Beweislast** für den Zugang. Beweismittel:

- Einschreiben mit Rückschein (nur Übermittlung, nicht Inhalt)
- Botenattest (Erklärung des Boten über Übergabe)
- Empfangsbestätigung (am sichersten)
- Zustellungsurkunde nach ZPO bei gerichtlicher Zustellung

## Templates

### Mandantenhinweis: Zugang sichern

```
Empfehlung zur Zugangssicherung bei wichtigen Erklärungen:

Für rechtserhebliche Erklärungen (Kündigung, Widerruf, Mahnung) empfehlen wir:

Option A — Papier:
 Bote mit Übergabe gegen Quittung oder Einwurf mit Attest
 Alternativ: Einschreiben/Rückschein (beweist Übermittlung, nicht Inhalt)

Option B — Elektronisch (qES):
 qES-Dokument per E-Mail an Empfänger; Eingangsbestätigung anfordern.
 Achtung: Ausdruck durch Gericht oder Dritte wahrt keine Formwirksamkeit
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Option C — Gerichtliche Zustellung:
 Bei streitigem Verhältnis: Antrag auf Zustellung nach § 132 BGB möglich.
```

### Checkliste Zugangsnachweis

```
□ Welches Übermittlungsmedium wurde verwendet?
□ Zeitpunkt des Eingangs beim Empfänger dokumentiert?
□ Eingangsbestätigung des Empfängers vorhanden?
□ Boten-Attest / Zustell-Urkunde archiviert?
□ Bei qES: Datei mit Signatur beim Empfänger elektronisch eingegangen?
□ Widerrufs-Möglichkeit: Widerruf rechtzeitig abgesandt?
```

## Fallstricke

- **Einschreiben ohne Rückschein**: Beweist nicht den Inhalt. Bei Kündigung: Kopie des Schreibens zusätzlich aufbewahren; Zeugen für Übergabe hinzuziehen.
- **Urlaubsabwesenheit des Empfängers**: Zugang tritt ein, wenn Brief im Briefkasten liegt — auch wenn Empfänger im Urlaub ist und Brief erst später liest. Ausnahme: Empfänger hat Urlaubs-Abwesenheit angekündigt und Erklärende wusste davon (einzelfallabhängig).
- **Spam-Filter**: E-Mail landet im Spam-Ordner → BGH und OLG-Rechtsprechung uneinheitlich. Sicherheitshalber zusätzlich per Post übermitteln oder Empfangsbestätigung anfordern.
- **qES und Zugang**: Die qES-Erklärung muss digital (nicht als Papierausdruck) beim Empfänger ankommen, damit Formwirksamkeit und Zugang zusammenfallen (→ `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`).

## Querverweise

- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` (Sonderfall qES-Zugang)
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `dokumentations-und-beweisarchitektur`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`

<!-- AUDIT 27.05.2026 bundle_043
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=06.10.2022&Aktenzeichen=VII+ZR+895%2F21
-->

## 2. `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`

**Fokus:** Prüffeld für zugang formgerechter erklaerung bgh viii zr 159 23: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtsgrundlagen

- BGH, Urt. v. 27.11.2024 – Az. VIII ZR 159/23 — qES-Wohnraumkuendigung; Anforderungen an Zugang in der korrespondierenden Form; Stand der Norm vor Einfuehrung des § 130e ZPO am 17.07.2024. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.11.2024&Aktenzeichen=VIII+ZR+159/23
- **§ 568 Abs. 1 BGB** — Schriftform der Wohnraummiete-Kündigung
- **§ 126 Abs. 3 BGB** i.V.m. **§ 126a Abs. 1 BGB** — Ersatz der Schriftform durch qES
- **§ 130 Abs. 1 S. 1 BGB** — Zugang empfangsbedürftiger Willenserklärungen
- **§ 130e ZPO** — Zugangsfiktion bei gerichtlicher Weiterleitung qualifiziert signierter Dokumente (eingefuehrt 17.07.2024)
- **§ 298 Abs. 3 ZPO** — Transfervermerk bei Ausdruck elektronischer Dokumente durch Gericht
- **eIDAS-Verordnung** VO (EU) Nr. 910/2014 — Definition der qualifizierten elektronischen Signatur

## BGH-Linie — Lehrsatz der Entscheidung

### Sachverhalt (vereinfacht)

Ein Vermieter erklärte die Kündigung des Wohnraummietverhältnisses durch ein elektronisch übermitteltes Dokument mit qualifizierter elektronischer Signatur. Im Rechtsstreit wurde das Dokument durch das Gericht ausgedruckt und mit einem Transfervermerk nach § 298 Abs. 3 ZPO in die Akte aufgenommen. Die Frage war, ob dieser Ausdruck den formgerechten Zugang der Kündigung beim Mieter bewirkte.

### Entscheidung des BGH

> **Leitsatz**: Die Kündigung eines Wohnraummietverhältnisses durch ein mit einer qualifizierten elektronischen Signatur versehenes Dokument wahrt die Schriftform des § 568 Abs. 1 BGB i.V.m. § 126a Abs. 1 BGB nur dann, wenn das elektronische Dokument dem Empfänger so zugegangen ist, dass er die Echtheit der qualifizierten elektronischen Signatur selbst prüfen kann.

> **Zur Frage des Transfervermerks**: Der Ausdruck eines elektronischen Dokuments durch das Gericht mit einem Transfervermerk gemäß § 298 Abs. 3 ZPO stellt keinen formgerechten Zugang gegenüber dem Erklärungsempfänger dar. Der Transfervermerk dient allein der Dokumentation für die Gerichtsakte, nicht der Herstellung des Zugangs beim Empfänger.

### Dogmatische Begründung

Der BGH stützt die Entscheidung auf folgende Überlegungen:

**Erstens** — **Formzweck**: Die qualifizierte elektronische Signatur soll Identität und Erklärungswillen des Unterzeichners für den Empfänger nachweisbar machen. Dieser Zweck wird nur erfüllt, wenn der Empfänger die Signatur tatsächlich prüfen kann — also das digitale Dokument mit der eingebetteten kryptographischen Signaturinformation erhält.

**Zweitens** — **Gerichtlicher Ausdruck und § 298 ZPO**: Der Transfervermerk nach § 298 Abs. 3 ZPO dokumentiert, dass eine elektronische Datei existiert hat und wie sie im Zeitpunkt des Ausdrucks aussah. Er ersetzt aber nicht den direkten Zugang des digitalen Dokuments beim Erklärungsempfänger. Der Mieter hatte das qES-Dokument selbst nie erhalten.

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
| Gerichte | § 298 Abs. 3 ZPO-Ausdruck reicht für Zugang beim Erklärungsempfänger nicht |
| Anwälte | Schriftsatz mit qES-Anlage muss über Postfach des Mandanten zugehen, nicht nur Gerichtspost |

### Empfehlung für die Praxis bis zur gesetzlichen Klarstellung

**Vermieter**: Kündigung per Papier mit Originalunterschrift und Bote oder Einschreiben bleibt die sicherste Option. qES-Versand per E-Mail ist rechtlich möglich, birgt aber das Zugangsrisiko (Spam-Filter, technische Probleme).

**Mieter**: Nach dieser Entscheidung ist es künftig denkbar, dass wirksame Kündigungen per E-Mail mit qES-Anhang zugehen können. E-Mail-Postfach und WhatsApp-Nachrichten auf solche Anhänge prüfen und nicht vorschnell löschen (→ `mandantenwarnung-qes-per-email-whatsapp-und-zugang`).

## Templates

### Gesprächsvorlage Vermieter-Beratung qES-Kündigung

```
Thema: Kündigung Wohnraummiete per qualifizierter elektronischer Signatur

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Die Kündigung per qES ist grundsätzlich zulässig (§ 568 Abs. 1 BGB i.V.m.
§ 126a Abs. 1 BGB). Aber: Das qES-Dokument muss dem Mieter so zugehen,
dass er die Signatur prüfen kann. Ein späterer Gerichtsausdruck mit
Transfervermerk (§ 298 Abs. 3 ZPO) reicht nicht.

Unsere Empfehlung: Kündigung als PDF mit qES per E-Mail an Mieter;
Eingangsbestätigung anfordern; Sendebericht sichern. Alternativ: Papier
mit Originalunterschrift, übergeben durch Boten gegen Quittung.
```

## Fallstricke

- **Nur ein Ausdruck ist kein Zugang**: Viele Anwälte und Richter übersehen, dass § 298 Abs. 3 ZPO-Ausdrucke nur für die Gerichtsakte bestimmt sind — nicht für den Beweis des Zugangs beim Erklärungsempfänger.
- **E-Mail im Spam**: qES-Dokument per E-Mail gesendet, landet im Spam-Filter des Mieters → technisch eingegangen, aber Zugang str. Besser: Eingangsbestätigung anfordern.
- **WhatsApp-Anhang mit qES**: Technisch möglich, aber unüblich und Zugang schwer nachzuweisen. Empfehlung: E-Mail mit Eingangsbestätigung bevorzugen.

## Querverweise

- → `elektronische-form-paragraph-126a-bgb-qes`
- → `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb`
- → `wohnraummiete-kuendigung-paragraph-568-bgb`
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `kuendigung-per-schriftsatz-zustellung-formfragen`
