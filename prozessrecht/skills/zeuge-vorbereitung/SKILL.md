---
name: zeuge-vorbereitung
description: "Vorbereitung einer Zeugenvernehmung nach §§ 373 ff. ZPO oder §§ 48 ff. StPO – Fragenkatalog, Themengliederung, Glaubhaftigkeitsanalyse und Vorbereitung auf Vorhalte. Verwenden, wenn der Nutzer sagt „Zeuge vorbereiten\", „Vernehmungsvorbereitung [Name]\", „Fragenkatalog für Zeugen\" oder sich auf eine bevorstehende Beweisaufnahme vorbereitet."
---

# Zeugenvernehmung-Vorbereitung

## Zweck

Vorbereitung auf eine Zeugenvernehmung im deutschen Zivil- oder Strafverfahren. Drei Perspektiven:
- **Eigener Zeuge vorbereiten** (Information des Mandanten über Ablauf, § 373 ff. ZPO; § 395 StPO)
- **Gegnerischen Zeugen befragen** (Fragenkatalog aus der Mandatstheorie entwickeln)
- **Strafverteidigung:** Vorbereitung auf Hauptverhandlung (§§ 244 ff. StPO), Pflichtverteidiger-Gespräch

> Die Zeugenvernehmung findet ausschließlich vor dem Gericht statt (§ 396 ZPO, § 238 Abs. 2 StPO). Eine vorgerichtliche anwaltliche Befragung von Zeugen kennt das deutsche Recht nicht. Eine informelle Zeugen-„Vorbefragung" durch den Anwalt ist berufsrechtlich sensibel (§ 1 BORA – Sachlichkeit; vgl. § 26 BRAO) und darf Zeugen nicht beeinflussen.

## Eingaben

- Aktives Mandat (Slug)
- Zeuge: Name, Rolle im Verfahren (Zeuge der Partei / gegnerischer Zeuge / Zeuge von Amts wegen)
- Vernehmungsmodus: `--eigener-zeuge`, `--gegnerischer-zeuge`, `--strafverfahren`
- Vorhandene Dokumente: Zeugenaussagen (Erstvernehmung, Polizeiprotokoll), Schriftverkehr des Zeugen, Anlagen, Chronologie

## Ablauf

### Modus: Eigener Zeuge vorbereiten (`--eigener-zeuge`)

1. **Ablaufbelehrung:** Dem Mandanten/Zeugen den Vernehmungsablauf erklären (§§ 395, 396, 402 ZPO): Vorführung, allgemeine Personalien, Belehrung, freie Schilderung, Befragung durch Gericht, Fragen der Parteien, Eid/eidesstattliche Versicherung (§ 391 ZPO).

2. **Zeugnisverweigerungsrecht prüfen:** §§ 383–385 ZPO (Angehörige, Berufsgeheimnisträger, Selbstbelastungsverbot); § 52 StPO; § 55 StPO (Auskunftsverweigerungsrecht).

3. **Erinnerungslücken identifizieren:** Aus Chronologie bekannte Ereignisse mit Zeugenwissen abgleichen; offene Punkte markieren.

4. **Fragenvorbereitung:** Erwartete Fragen des Gerichts und der Gegenseite vorab erarbeiten; angemessene Antworten (wahrheitsgemäß, nicht überschießend) vorbereiten.

5. **Vorhalte vorantizipieren:** Schriftstücke, E-Mails oder frühere Aussagen, die dem Zeugen vorgehalten werden könnten, identifizieren.

### Modus: Gegnerischen Zeugen befragen (`--gegnerischer-zeuge`)

1. **Zeugenprofil erstellen:** Aus Mandatsakte und Chronologie: Was weiß der Zeuge, was hat er gesagt, welche Dokumente hat er unterzeichnet?

2. **Themengliederung:**
   - Kernthemen (direkt anspruchsrelevant)
   - Glaubwürdigkeitsthemen (Widersprüche zu früheren Aussagen, Eigeninteresse)
   - Bestätigungsthemen (ungünstige Tatsachen aus Zeugen-Sicht bestätigen lassen)

3. **Fragenkatalog:** Geschlossene Kontrollfragen (auf ein Ja/Nein ausgerichtet) zuerst; offene Fragen nur bei sicherer Antwort; Fangfragen vermeiden (Prozessrisiko: Zeuge weicht aus).

4. **Vorhalte:** Dokumente, auf die vorgehalten werden soll, mit Anlage-Nr. verzeichnen.

5. **Glaubwürdigkeitsangriff:** Widersprüche zu protokollierten Aussagen, Eigeninteresse, Abhängigkeiten.

### Modus: Strafverfahren (`--strafverfahren`)

1. **Akteneinsicht § 147 StPO:** Vernehmungsprotokolle aus der Ermittlungsakte identifizieren.
2. **Belehrung § 136 StPO / § 55 StPO:** Sicherstellen, dass Auskunftsverweigerungsrecht bekannt ist.
3. **Hauptverhandlung § 244 StPO:** Beweisantragsrecht der Verteidigung (Beweisantrag auf Zeugenladung, § 244 Abs. 3, 6 StPO).

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Greger, in: Zöller, ZPO, 35. Aufl. 2024, §§ 373–401 Rn. 1 ff. (Zeugenvernehmung: Ablauf, Zeugnisverweigerungsrecht, Vereidigung).
- BGH, Urt. v. 28.02.2018 – IV ZR 252/16, NJW 2018, 1382 Rn. 21 (Glaubhaftigkeitsprüfung bei Zeugenbeweis: Gesamtwürdigung, § 286 ZPO).
- BGH, Urt. v. 16.07.2010 – V ZR 224/09, NJW 2011, 295 Rn. 18 (Freiheit der Beweiswürdigung bei Zeugenaussagen).
- Huber, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 373 Rn. 5 ff. (Beweisantritt durch Zeugenbeweis).
- Meyer-Goßner/Schmitt, StPO, 67. Aufl. 2024, § 52 Rn. 1 ff. (Zeugnisverweigerungsrecht wegen persönlicher Beziehung).
- BGH, Urt. v. 30.10.2008 – III ZR 307/07, NJW 2009, 227 Rn. 14 (Vereidigung, § 391 ZPO: Ermessen des Gerichts).

## Ausgabeformat

### Vernehmungs-Vorbereitung – Eigener Zeuge

**Zeuge:** [Name]  
**Vernehmungsdatum:** TT.MM.JJJJ  
**Verfahren:** [Mandat-Slug], [Gericht], Az.: [Aktenzeichen]

**Kernwissen des Zeugen (aus Chronologie):**
| Datum | Ereignis | Belegdokument | Zeugen-Relevanz |
|---|---|---|---|
| 12.03.2022 | Vertragsschluss | Anlage K1 | Zeuge anwesend |

**Fragenkatalog – erwartete Fragen:**
1. Wann wurden Sie auf das Projekt aufmerksam?
2. Waren Sie beim Vertragsschluss am 12.03.2022 anwesend?
...

**Vorhalte (antizipiert):**
- E-Mail v. 05.04.2022 (Anlage B3): Zeuge bat um Verlängerung – klären, warum.

**Zeugnisverweigerungsrecht:** Nicht einschlägig (kein Angehöriger, kein Berufsgeheimnisträger).

## Risiken / typische Fehler

- **Zeugencoaching verboten:** Der Anwalt darf den Zeugen nicht zu einer bestimmten Aussage anleiten; nur Erläuterung des Ablaufs und Erinnerungshilfe auf Basis vorhandener Dokumente zulässig (vgl. § 1 BORA).
- **Zeugnisverweigerungsrecht übersehen:** Vor der Vernehmung stets §§ 383–385 ZPO, § 52, 55 StPO prüfen; Nichtbelehrung führt zur Unverwertbarkeit (§ 252 StPO; BGH, Urt. v. 27.02.1992 – 4 StR 23/92, BGHSt 38, 302).
- **Gegnerischer Zeuge – keine Kontaktaufnahme:** Kontaktaufnahme mit gegnerischem Zeugen außerhalb des Verfahrens ist berufsrechtlich problematisch (§ 12 BORA).
- **Vereidigung:** § 391 ZPO – Gericht entscheidet; falsche Zeugenaussage ist strafbar (§ 153 StGB); Zeuge vor Vernehmung hierüber belehren.
