---
name: handbook-updates
description: >
  Prüft eine geplante Änderung des Personalhandbuchs auf Folgewirkungen —
  andere betroffene Regelungen, standortspezifische Besonderheiten nach
  Tarifvertrag oder Betriebsvereinbarung, Mitbestimmungsrechte des Betriebsrats
  und die Frage, ob ein bestehendes Leistungsversprechen beschnitten wird.
  Lädt, wenn jemand sagt „Handbuch aktualisieren", „neue Regelung einpflegen"
  oder „Richtlinie ändern".
language: de
triggers:
  - "Personalhandbuch aktualisieren"
  - "Handbuch ändern"
  - "Betriebsvereinbarung anpassen"
  - "Richtlinie einpflegen"
  - "Arbeitsordnung überarbeiten"
  - "betriebliche Regelung"
  - "Folgewirkungen Handbuchänderung"
---

# Personalhandbuch-Aktualisierung (Arbeitsrecht)

## Zweck

Änderungen am Personalhandbuch haben Folgewirkungen. Eine geänderte
Urlaubsregelung betrifft die Berechnung der Urlaubsabgeltung bei Beendigung,
die Verweisklauseln in anderen Abschnitten und ggf. bestehende
Betriebsvereinbarungen zum Thema. Diese Skill findet die Folgewirkungen,
bevor sie zu Widersprüchen werden.

Lädt, wenn eine Regelungsänderung im Personalhandbuch vorbereitet wird und
Folgewirkungen systematisch geprüft werden sollen.

## Eingaben

- Betroffener Abschnitt des Personalhandbuchs
- Neuer Regelungstext (Entwurf)
- Grund der Änderung (gesetzliche Anforderung, Unternehmensentscheidung, Bereinigung)
- Jurisdiktioneller Fußabdruck des Unternehmens (Standorte, Tarifbindung)
- Bestehende Betriebsvereinbarungen zum Thema (falls bekannt)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 87 BetrVG: Erzwingbares Mitbestimmungsrecht des Betriebsrats bei
  Ordnung des Betriebs, Arbeitszeit, Urlaub, betrieblichem Datenschutz u. a.
  — Handbuchänderungen in diesen Bereichen erfordern Betriebsratszustimmung
  oder Einigungsstellenverfahren
- § 77 BetrVG: Betriebsvereinbarungen — Vorrang und Ablösung;
  Nachwirkung gekündigter Betriebsvereinbarungen (§ 77 Abs. 6 BetrVG)
- §§ 305 ff. BGB: AGB-Kontrolle für vorformulierte Arbeitsbedingungen;
  Inhaltskontrolle nach § 307 BGB; Transparenzgebot § 307 Abs. 1 S. 2 BGB
- § 2 NachwG: Nachweispflicht wesentlicher Arbeitsbedingungen;
  Änderungen sind dem Arbeitnehmer spätestens am ersten Tag nach Wirksamwerden
  schriftlich mitzuteilen
- §§ 611a, 613 BGB: Arbeitsvertragliche Einbindung von Handbuchregelungen
  durch Bezugnahmeklauseln

**Leitentscheidungen:**

- BAG, Urt. v. 11.04.2006 – 9 AZR 557/05, NZA 2006, 1149 Rn. 20 ff.:
  Wirksame Einbeziehung von Personalhandbuch-Regelungen durch Bezugnahmeklausel
  im Arbeitsvertrag; AGB-Kontrolle; Maßstab der überraschenden Klausel
  nach § 305c Abs. 1 BGB
- BAG, Urt. v. 12.01.2005 – 5 AZR 364/04, NZA 2005, 465 Rn. 31:
  Verschlechterung einer durch betriebliche Übung entstandenen
  Leistungsverpflichtung — einseitige Abänderung unwirksam; Änderungskündigung
  als richtiger Weg; Vertrauensschutz der Arbeitnehmer
- BAG, Urt. v. 23.01.2018 – 1 AZR 65/17, NZA 2018, 735 Rn. 16 ff.:
  Mitbestimmung des Betriebsrats bei einseitiger Änderung betrieblicher
  Regelungen, die in den Bereich des § 87 BetrVG fallen; Einigungsstellenverfahren

**Kommentarliteratur:**

- Erfurter Kommentar/Kania, 24. Aufl. 2024, § 87 BetrVG Rn. 1 ff.:
  Katalog erzwingbarer Mitbestimmungsrechte; Reichweite der Mitbestimmung
  bei Regelungsänderungen
- MüKoBGB/Wurmnest, 9. Aufl. 2022, § 307 Rn. 200 ff.:
  AGB-Kontrolle vorformulierter Arbeitsbedingungen; Inhaltskontrolle
  und Transparenzgebot im Arbeitsverhältnis
- HWK/Thüsing, 11. Aufl. 2024, § 2 NachwG Rn. 10 ff.:
  Nachweispflicht bei Änderungen wesentlicher Arbeitsbedingungen,
  Formerfordernis und Folgen der Verletzung

## Ablauf

**Schritt 1 — Änderung erfassen**

- Welcher Abschnitt wird geändert?
- Was ist der neue Wortlaut?
- Warum? (Gesetzliche Anforderung, Unternehmensentscheidung, Bereinigung)

**Schritt 2 — Vergleich mit dem aktuellen Stand**

Zeige den Vergleich:

```diff
- [bisheriger Wortlaut]
+ [neuer Wortlaut]
```

**Schritt 3 — Querverweise prüfen**

Durchsuche das Personalhandbuch nach Bezügen auf den geänderten Abschnitt:

- Andere Regelungen, die auf diesen Abschnitt verweisen
  („zur Urlaubsabgeltung siehe Abschnitt …")
- Definierte Begriffe, die dieser Abschnitt verwendet oder definiert
- Standort- oder tarifvertragliche Sonderregelungen, die diesen Abschnitt
  modifizieren

Für jeden Querverweis: Gilt er nach der Änderung noch unverändert?
Wird er durch die Änderung falsch oder unvollständig? Kennzeichne Konflikte.

**Schritt 4 — Mitbestimmungsprüfung**

Prüfe, ob die geplante Änderung in den Bereich eines Mitbestimmungstatbestands
nach § 87 BetrVG fällt (insbesondere Nr. 1 Ordnung des Betriebs, Nr. 2/3
Arbeitszeit, Nr. 5 Urlaub, Nr. 6 Überwachungstechnik, Nr. 10
Entlohnungsgrundsätze). Falls ja:

> Mitbestimmungshinweis: Diese Änderung berührt [Tatbestand § 87 Abs. 1
> Nr. X BetrVG]. Eine wirksame Einführung ohne Zustimmung des Betriebsrats
> ist nicht möglich. Optionen: (1) Zustimmung des Betriebsrats einholen,
> (2) Einigungsstellenverfahren nach § 76 BetrVG.

**Schritt 5 — Prüfung standortspezifischer Besonderheiten**

Prüfe für jeden Standort im Fußabdruck:
- Modifiziert eine bestehende Betriebsvereinbarung diesen Bereich?
- Macht die Änderung eine bestehende Betriebsvereinbarung obsolet, falsch
  oder unvollständig?
- Entsteht für einen Standort erstmals Anpassungsbedarf?

**Schritt 6 — Leistungsversprechen-Check**

Wird durch die Änderung eine bislang gewährte Leistung reduziert oder gestrichen?

Falls ja: Risikokennzeichnung. In der Rechtsprechung können Handbuchregelungen
als vertragliche Vereinbarung oder betriebliche Übung bindend sein
(vgl. BAG, Urt. v. 12.01.2005 – 5 AZR 364/04). Eine Verschlechterung kann
eine Änderungskündigung oder eine Mitarbeiterinformation mit Zustimmungserfordernis
erfordern. Nicht blockieren — kennzeichnen.

**Schritt 7 — Nachweispflicht**

Prüfe, ob die geänderte Regelung eine „wesentliche Arbeitsbedingung" i. S. d.
§ 2 Abs. 1 NachwG darstellt. Falls ja: Informationspflicht gegenüber den
betroffenen Arbeitnehmern spätestens am Tag nach Wirksamwerden.

## Ausgabeformat

```markdown
## Handbuchänderung: [Abschnitt]

### Änderung
[diff]

### Querverweis-Auswirkungen
| Abschnitt | Bezug zur Änderung | Noch korrekt? | Handlungsbedarf |
|---|---|---|---|
| [Name] | [wie] | Ja/Nein | [was] |

### Mitbestimmung
[Falls § 87 BetrVG betroffen: Tatbestand und erforderliches Vorgehen]
[Falls nicht betroffen: „Kein erzwingbares Mitbestimmungsrecht betroffen"]

### Standortspezifische Auswirkungen
| Standort | Bestehende Betriebsvereinbarung | Nach Änderung | Maßnahme |
|---|---|---|---|
| [Standort] | [Inhalt] | [weiter gültig / obsolet / anzupassen] | [keine / Update / neu] |

### Leistungsversprechen-Check
[Falls Leistungsreduzierung: Kennzeichnung + rechtliche Risikoeinschätzung]

### Nachweispflicht
[Falls § 2 NachwG betroffen: Information an Arbeitnehmer erforderlich]

### Freigabe-Checkliste
- [ ] Querverweise angepasst
- [ ] Betriebsvereinbarungen aktualisiert (falls erforderlich)
- [ ] Betriebsrat involviert (falls § 87 BetrVG betroffen)
- [ ] Leistungsversprechen-Frage geklärt (falls Reduzierung)
- [ ] Versionsnummer und Datum aktualisiert
- [ ] Mitarbeiterinformation gemäß § 2 NachwG (falls erforderlich)
```

## Beispiel

Szenario: Das Unternehmen möchte die Urlaubsregelung von 30 auf 25 Werktage
Jahresurlaub (bei einer 5-Tage-Woche) reduzieren. Die Regelung war im
Personalhandbuch niedergelegt und wurde seit drei Jahren allen Einstellungen
versprochen.

Ausgabe der Skill:

> Leistungsversprechen-Check: Die Reduzierung des Jahresurlaubs unterschreitet
> den bisher im Handbuch versprochenen Wert. Sofern die 30-Tage-Regelung durch
> betriebliche Übung (§ 611a BGB i. V. m. Grundsatz der betrieblichen Übung)
> oder vertragliche Bezugnahme bindend ist, bedarf die Änderung entweder der
> individuellen Zustimmung jedes betroffenen Arbeitnehmers oder einer
> Änderungskündigung (§§ 2, 4 KSchG). Mitbestimmung des Betriebsrats nach
> § 87 Abs. 1 Nr. 5 BetrVG ist zu prüfen.

## Risiken und typische Fehler

- **Mitbestimmung vergessen**: Änderungen in Bereichen des § 87 BetrVG
  ohne Betriebsratsinhaber sind unwirksam — auch wenn sie sachlich gerechtfertigt sind.
- **Betriebliche Übung unterschätzt**: Was über Jahre konsistent gewährt wurde,
  kann bindend sein — auch ohne ausdrücklichen Vertrag.
- **NachwG-Frist versäumt**: Änderungen wesentlicher Arbeitsbedingungen müssen
  spätestens am nächsten Arbeitstag schriftlich mitgeteilt werden.
- **AGB-Kontrolle nicht geprüft**: Vorformulierte Handbuchklauseln unterliegen
  §§ 305 ff. BGB; überraschende oder unangemessen belastende Klauseln sind
  unwirksam.
- **Standortspezifika übersehen**: Betriebsvereinbarungen an einzelnen
  Standorten können bundesweite Handbuchregelungen einschränken oder erweitern.

## Quellenpflicht

Jede Ausgabe dieser Skill muss bei mitbestimmungsrelevanten Änderungen zitieren:

- § 87 BetrVG (Mitbestimmungstatbestand), § 77 BetrVG (Betriebsvereinbarung)
- § 2 NachwG (Nachweispflicht)
- §§ 305 ff. BGB (AGB-Kontrolle)
- BAG, Urt. v. 11.04.2006 – 9 AZR 557/05, NZA 2006, 1149 (Einbeziehung)
- BAG, Urt. v. 12.01.2005 – 5 AZR 364/04, NZA 2005, 465 (betriebliche Übung)
- Erfurter Kommentar/Kania, 24. Aufl. 2024, § 87 BetrVG

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
