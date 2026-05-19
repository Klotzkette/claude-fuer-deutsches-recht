---
name: richtlinien-entwurf
description: >
  Entwirft eine betriebliche Regelung (Richtlinie, Betriebsordnung, Policy)
  mit standortspezifischen Ergänzungen, wo das Recht oder Tarifverträge
  abweichende Regeln erfordern. Prüft Mitbestimmungsrechte des Betriebsrats
  und ob bestehende Leistungsversprechen berührt werden. Lädt, wenn jemand
  sagt „Richtlinie entwerfen zu [Thema]", „wir brauchen eine Regelung zu"
  oder eine Regelungslücke benennt.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Richtlinie entwerfen
  - Policy entwerfen
  - Betriebsordnung
  - Regelung entwerfen
  - Handbuch-Policy
  - Arbeitsanweisung
  - betriebliche Regelung neu
---

# Richtlinien-Entwurf (Arbeitsrecht)

## Zweck

Eine Regelung, die für München passt, kann in Frankfurt falsch sein — nicht
wegen des Landes, sondern wegen des Tarifvertrags, der Betriebsvereinbarung
oder der Konzernstruktur. Diese Skill entwirft eine Kernregelung und erstellt
standortspezifische Ergänzungen, wo der Betrieb, ein Tarifvertrag oder eine
bestehende Betriebsvereinbarung abweichende Anforderungen stellt.

Lädt, wenn eine neue oder geänderte Arbeitsregelung für ein oder mehrere
Unternehmen / Standorte benötigt wird und die Folgewirkungen auf Betriebsrat,
Tarifvertrag und bestehende Zusagen geprüft werden sollen.

## Eingaben

- Thema der Regelung (z. B. Mobile Arbeit, Elternzeit-Ergänzung, Spesen,
  Social Media, Datenschutz am Arbeitsplatz)
- Anlass (gesetzliche Anforderung, Unternehmensinitiative, Regelungslücke)
- Geltungsbereich (alle Arbeitnehmer / bestimmte Rollen / bestimmte Standorte)
- Bestehende Betriebsvereinbarungen und Tarifbindung (falls bekannt)
- Jurisdiktioneller Fußabdruck (Standorte und Länder)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 87 BetrVG: Erzwingbares Mitbestimmungsrecht des Betriebsrats —
  Regelungen in den Bereichen § 87 Abs. 1 Nr. 1–13 (u. a. Ordnung des
  Betriebs, Arbeitszeit, Urlaub, Datenschutz, Vergütungsgrundsätze)
  können nicht ohne Zustimmung des Betriebsrats eingeführt werden
- § 77 BetrVG: Betriebsvereinbarungen — Vorrang und Ablöseprinzip;
  Nachwirkung (§ 77 Abs. 6 BetrVG); günstigerer Tarifvertrag geht vor
- §§ 305 ff. BGB: AGB-Kontrolle für vorformulierte Arbeitsbedingungen;
  § 305c Abs. 1 BGB: Verbot überraschender Klauseln; § 307 BGB:
  Inhaltskontrolle; Transparenzgebot
- § 2 NachwG: Schriftliche Mitteilung wesentlicher Arbeitsbedingungen
  bei erstmaliger Vereinbarung und bei Änderungen
- §§ 3 ff. AGG: Diskriminierungsverbote — Regelungen dürfen keine
  unmittelbaren oder mittelbaren Benachteiligungen wegen geschützter
  Merkmale enthalten oder bewirken
- ArbZG: Arbeitszeitgesetz — Regelungen zur Arbeitszeit dürfen
  gesetzliche Höchstgrenzen (§ 3 ArbZG: 8 Stunden täglich, maximal
  10 Stunden) und Ruhezeiten (§ 5 ArbZG) nicht unterschreiten
- § 26 BDSG / Art. 88 DSGVO: Beschäftigtendatenschutz — Regelungen zur
  Überwachung, Zugriffsrechten oder Kommunikation erfordern
  Datenschutzprüfung und ggf. Betriebsvereinbarung nach § 26 BDSG

**Leitentscheidungen:**

- BAG, Urt. v. 11.04.2006 – 9 AZR 557/05, NZA 2006, 1149 Rn. 20 ff.:
  AGB-Kontrolle von Handbuchregelungen, die durch Bezugnahmeklausel
  einbezogen wurden; überraschende Klauseln nach § 305c BGB;
  Transparenzgebot nach § 307 Abs. 1 S. 2 BGB; Reichweite der
  Inhaltskontrolle bei Arbeitsregelungen
- BAG, Urt. v. 12.01.2005 – 5 AZR 364/04, NZA 2005, 465 Rn. 31:
  Betriebliche Übung als Anspruchsgrundlage; einseitige Verschlechterung
  einer durch betriebliche Übung entstandenen Leistungspflicht unwirksam;
  Änderungskündigung als erforderliches Instrument
- BAG, Urt. v. 23.01.2018 – 1 AZR 65/17, NZA 2018, 735 Rn. 16 ff.:
  Mitbestimmungspflicht bei einseitiger Änderung betrieblicher Regelungen
  in § 87 BetrVG-Bereichen; Einigungsstellenverfahren bei Scheitern der
  Einigung

**Kommentarliteratur:**

- Kania, in: ErfK, 25. Aufl. 2025, § 87 BetrVG Rn. 1:
  Katalog der erzwingbaren Mitbestimmungsrechte; Reichweite bei einzelnen
  Themenfeldern (Homeoffice, Datenschutz, Zeiterfassung)
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 200:
  AGB-Kontrolle vorformulierter Arbeitsbedingungen; Inhaltskontrolle;
  Transparenzgebot im Arbeitsrecht
- Thüsing, in: HWK, 11. Aufl. 2024, § 2 NachwG Rn. 1:
  Nachweispflicht; schriftliche Mitteilung bei Änderungen; Folgen

## Ablauf

**Schritt 1 — Kontext laden**

Lese `CLAUDE.md` im Plugin-Verzeichnis → jurisdiktioneller Fußabdruck,
Handbuch-Standort, Tarifbindungen, bestehende Betriebsvereinbarungen.

**Schritt 2 — Regelung scopen**

- Welches Thema? (Mobile Arbeit, Elternzeit, Social Media, Spesen, etc.)
- Warum jetzt? (Gesetzliche Anforderung, Unternehmensinitiative, Regelungslücke)
- Für wen gilt sie? (Alle Arbeitnehmer, bestimmte Rollen, bestimmte Standorte)

**Schritt 3 — Mitbestimmungsprüfung**

Prüfe, ob die geplante Regelung in einen Mitbestimmungstatbestand des
§ 87 Abs. 1 BetrVG fällt:

| Regelungsthema | Mitbestimmungstatbestand |
|---|---|
| Ordnung des Betriebs, Verhaltensregeln | § 87 Abs. 1 Nr. 1 BetrVG |
| Beginn/Ende der täglichen Arbeitszeit, Pausen | § 87 Abs. 1 Nr. 2, 3 BetrVG |
| Urlaubsplanung, -grundsätze | § 87 Abs. 1 Nr. 5 BetrVG |
| Einführung von Überwachungstechnik (IT, Zeiterfassung) | § 87 Abs. 1 Nr. 6 BetrVG |
| Unfallverhütung, Gesundheitsschutz | § 87 Abs. 1 Nr. 7 BetrVG |
| Grundsätze des betrieblichen Lohngestaltung | § 87 Abs. 1 Nr. 10 BetrVG |
| Mobile Arbeit / Homeoffice | § 87 Abs. 1 Nr. 1, 2, 6 BetrVG |

Falls Mitbestimmung ausgelöst: explizit flaggen und empfohlenes Vorgehen
angeben (Einholung Betriebsratszustimmung oder Einigungsstellenverfahren
nach § 76 BetrVG).

**Schritt 4 — Jurisdiktioneller Scan**

Für jeden Standort / jede tarifvertragliche Bindung im Fußabdruck prüfen:
Gibt es abweichende gesetzliche, tarifvertragliche oder
betriebsvereinbarungsbasierte Anforderungen zu diesem Thema?

**Häufige Themen mit Varianz:**

| Thema | Varianzquelle |
|---|---|
| Arbeitszeitregelungen | ArbZG-Mindestanforderungen; Branchentarifverträge (z. B. BAP/iGZ für Zeitarbeit) |
| Urlaubsansprüche | Tarifvertragliche Mehrurlaubs-Ansprüche; BUrlG-Mindest |
| Mobiles Arbeiten | Betriebsvereinbarungen; § 87 Abs. 1 Nr. 1, 2, 6 BetrVG |
| Überstundenregelungen | ArbZG-Grenzen; TV-Mehrarbeitszuschläge |
| Datenschutz am Arbeitsplatz | § 26 BDSG; Betriebsvereinbarung als Rechtsgrundlage |
| Außertarifliche Zulagen | Gleichbehandlungsgrundsatz; AGG |
| Kündigung / Abfindung | KSchG; TV-Abfindungsregelungen |

Falls das Thema keine standortspezifische Varianz aufweist (z. B. reines
Verhaltensgebot ohne Vergütungsrelevanz): diesen Schritt überspringen.

**Schritt 5 — Kernregelung entwerfen**

Eine Regelung. Gilt für alle erfassten Arbeitnehmer. Klar und verständlich —
Arbeitnehmer sollen sie ohne juristische Vorkenntnisse verstehen.

Struktur:
- Zweck (ein Satz — warum diese Regelung besteht)
- Geltungsbereich (wer ist erfasst)
- Die Regel (was ist geboten / erlaubt / untersagt)
- Verfahren (wie beantragen, wer genehmigt, was passiert bei Verstoß)
- Ansprechpartner (an wen wenden bei Fragen)

Vermeiden: „unbeschadet", „vorbehaltlich", verschachtelte Ausnahmen.
Das ist eine Betriebsregelung, kein Vertrag.

**Datenschutzprüfung:** Falls die Regelung die Verarbeitung von
Beschäftigtendaten vorsieht oder ermöglicht (z. B. IT-Monitoring,
Zeiterfassung, Zugangskontrolle): Rechtsgrundlage nach § 26 BDSG und
ggf. DSFA nach Art. 35 DSGVO prüfen. Bei automatisierter Überwachung
ist eine Betriebsvereinbarung als Rechtsgrundlage nach § 26 Abs. 4 BDSG
der sichere Weg.

**Schritt 6 — Standortspezifische Ergänzungen**

Für jeden Standort, an dem die Regel abweicht:

```markdown
### [Standort]-Ergänzung

Für Arbeitnehmer am Standort [Standort] gilt abweichend bzw. ergänzend:

- [Spezifische Abweichung]
- [Rechtsgrundlage oder Tarifvertragsbezug]
```

Ergänzungen knapp halten — nur Abweichendes; Kernregelung nicht wiederholen.

**Schritt 7 — Quercheck**

- Kollidiert diese Regelung mit einer bestehenden Regelung im Handbuch?
- Verspricht sie mehr, als das Unternehmen liefern will? (Eine Regelung ist
  ein Versprechen — Gerichte halten Arbeitgeber an Handbuchzusagen.)
- Enthält sie unabsichtlich eine vertragliche Bindung? (Betriebliche Übung
  nach drei gleichförmigen Wiederholungen — Disclaimer-Klausel wenn nötig,
  aber als eigenständigen Abschnitt, nicht als Fußnote.)
- AGG-Konformität: Enthält die Regelung mittelbare Benachteiligungen wegen
  geschützter Merkmale nach § 1 AGG?

## Ausgabeformat

```markdown
# [Regelungsname]

## Kernregelung

**Geltung:** [alle Arbeitnehmer / bestimmte Gruppen / Standorte]

**Zweck**
[Ein Satz]

**Geltungsbereich**
[Wer ist erfasst]

**Die Regelung**
[Was ist geboten / erlaubt / untersagt]

**Verfahren**
[Wie beantragen, Genehmigung, Konsequenzen bei Verstoß]

**Ansprechpartner**
[HR-Kontakt / Vorgesetzte]

---

## Standortspezifische Ergänzungen

### [Standort 1]
[Ergänzung]

### [Standort 2]
[Ergänzung]

---

## Entwurfsnotizen (intern — vor Einpflegen ins Handbuch entfernen)

- **Mitbestimmung:** [Tatbestand § 87 BetrVG — betroffene Nr. / nicht betroffen]
- **Betriebsrat-Vorgehen:** [Zustimmung erforderlich / Einigungsstellenverfahren]
- **Datenschutz:** [§ 26 BDSG-Prüfung, DSFA erforderlich ja/nein]
- **Jurisdiktioneller Scan:** [welche Standorte geprüft, wo Varianz]
- **Kollisionen mit bestehendem Handbuch:** [keine | Liste]
- **Recht derzeit im Wandel:** [Themen, die in Bewegung sind]
- **Review-Turnus:** [jährlich / bei Änderung von Gesetz/TV]
```

## Beispiel

Szenario: Entwurf einer Mobile-Work-Regelung für ein Unternehmen mit
Standorten in Hamburg und München, Tarifbindung nach TV Gesamtmetall.

Ausgabe (Auszug Entwurfsnotizen):

> Mitbestimmung: Mobile-Arbeit-Regelung berührt § 87 Abs. 1 Nr. 1 BetrVG
> (Ordnung des Betriebs), Nr. 2 BetrVG (Beginn/Ende der Arbeitszeit) und
> Nr. 6 BetrVG (IT-Überwachung bei Homeoffice-Zeiterfassung).
> Betriebsrat-Zustimmung oder Abschluss einer Betriebsvereinbarung ist
> vor Einführung zwingend.
>
> TV Gesamtmetall: Prüfen, ob der einschlägige ERA-TV Regelungen zur
> mobilen Arbeit enthält, die von der Kernregelung abweichen.
>
> Datenschutz: Falls die Regelung IT-Monitoring im Homeoffice vorsieht
> (z. B. Aktivitätstracking), ist eine Betriebsvereinbarung als
> Rechtsgrundlage nach § 26 Abs. 4 BDSG erforderlich und eine DSFA
> nach Art. 35 DSGVO zu prüfen.

## Risiken und typische Fehler

- **Mitbestimmung übergangen**: Eine in § 87 BetrVG-Bereichen eingeführte
  Regelung ohne Betriebsratszustimmung ist unwirksam, auch wenn der Inhalt
  sachlich gerechtfertigt ist.
- **Betriebliche Übung**: Was dreimal gleichförmig gewährt wurde, kann
  bindend werden. Neuregelungen, die bisher praxisübliche Leistungen
  einschränken, brauchen entweder individuelle Zustimmung oder
  Änderungskündigung.
- **AGB-Falle**: Vorformulierte Arbeitsbedingungen unterliegen § 307 BGB.
  Überraschende oder unverhältnismäßig belastende Klauseln sind unwirksam.
- **NachwG versäumt**: Wenn die Regelung wesentliche Arbeitsbedingungen
  ändert, ist schriftliche Mitteilung an die betroffenen Arbeitnehmer
  nach § 2 NachwG erforderlich.
- **AGG-Konformität nicht geprüft**: Regelungen können mittelbar
  diskriminierend wirken (z. B. Teilzeitausschlüsse, die überwiegend
  Frauen treffen). § 3 Abs. 2 AGG beachten.
- **Datenschutz nicht eingeplant**: Technische Überwachungsmaßnahmen
  ohne Betriebsvereinbarung und DSFA können nach § 26 BDSG und
  § 87 Abs. 1 Nr. 6 BetrVG unzulässig sein.

## Quellenpflicht

Jede Ausgabe dieser Skill zitiert je nach Relevanz:

- § 87 BetrVG (Mitbestimmung), § 77 BetrVG (Betriebsvereinbarung)
- §§ 305 ff. BGB (AGB-Kontrolle), § 307 BGB (Inhaltskontrolle)
- § 2 NachwG (Nachweispflicht)
- § 26 BDSG, Art. 88 DSGVO (Beschäftigtendatenschutz)
- BAG, Urt. v. 11.04.2006 – 9 AZR 557/05, NZA 2006, 1149 (AGB-Kontrolle)
- BAG, Urt. v. 12.01.2005 – 5 AZR 364/04, NZA 2005, 465 (betriebliche Übung)
- BAG, Urt. v. 23.01.2018 – 1 AZR 65/17, NZA 2018, 735 (Mitbestimmung)
- Erfurter Kommentar/Kania, 24. Aufl. 2024, § 87 BetrVG Rn. 1 ff.

> **Entwurf, keine geltende Regelung.** Dieser Entwurf ist ein Arbeitsdokument
> für die anwaltliche Überprüfung. Eine Betriebsregelung oder Richtlinie, die
> tatsächlich gilt, hat arbeitsrechtliche Bindungswirkung — in bestimmten
> Bereichen als vertragliche Vereinbarung, durch betriebliche Übung oder
> als Betriebsvereinbarung. Ein in der jeweiligen Jurisdiktion zugelassener
> Rechtsanwalt oder Syndikusrechtsanwalt (§ 46 BRAO) prüft, überarbeitet
> und trägt die fachliche Verantwortung, bevor die Regelung in Kraft tritt.
> Nicht ohne Freigabe verteilen oder einführen.

## Übergabe an handbuch-aktualisierung

Wenn diese Regelung genehmigt ist: `handbuch-aktualisierung`-Skill prüft die
Auswirkung auf das bestehende Handbuch und benennt Querverweise und
Anpassungsbedarf.

## Was diese Skill nicht tut

- Regelungen genehmigen — das ist Aufgabe von HR-Leitung und Rechtsabteilung.
- Regelungen kommunizieren — Mitarbeiterinformation ist HR-Aufgabe.
- Alle denkbaren Jurisdiktionen abdecken — nur den konfigurierten Fußabdruck.
  Bei Erweiterung des Fußabdrucks neu prüfen.
