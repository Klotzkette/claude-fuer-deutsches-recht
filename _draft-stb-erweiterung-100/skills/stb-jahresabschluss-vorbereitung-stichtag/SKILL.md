---
name: stb-jahresabschluss-vorbereitung-stichtag
description: "Jahresabschluss-Vorbereitung Stichtag. Anwendungsfall systematische JA-Vorbereitung Inventur Periodenabgrenzung Rueckstellungen Anlagenspiegel. Methodik 8-Wochen-Vorlauf. Output JA-Vorbereitungs-Routine."
---

# Jahresabschluss-Vorbereitung zum Stichtag

## Kernsachverhalt

Der Jahresabschluss erfordert systematische Vorbereitung 8-12 Wochen vor dem Bilanzstichtag und eine geordnete Abwicklung in den ersten vier Monaten danach. Inventur, Periodenabgrenzung, Rueckstellungen, Anlagenspiegel und Mandantenfragebogen muessen aufeinander abgestimmt sein. Die folgende Standardroutine setzt den Bilanzstichtag (i.d.R. 31.12.) als Anker; die Phasen koennen bei abweichendem Geschaeftsjahr entsprechend verschoben werden.

## Kaltstart-Rueckfragen

1. Welcher Bilanzstichtag?
2. Welche Rechtsform und Groessenklasse?
3. Liegt Pruefungspflicht vor (§ 316 HGB)?
4. Welche besonderen Vorgaenge im Jahr?
5. Welche Sondererlaeuterungen ?
6. Welche Fristen extern (Bundesanzeiger 12 Monate, Steuererklaerung)?
7. Welche Mandantenkommunikations-Routine?
8. Welche StBVV-Honorarvereinbarung?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — Aufstellungspflicht.

**§ 264 Abs. 1 HGB** — Aufstellungsfrist 3-6 Monate.

**§ 325 HGB** — Veroeffentlichung Bundesanzeiger 12 Monate.

**§ 316 HGB** — Pruefungspflicht groessere Kapitalgesellschaften.

**§ 240 HGB** — Inventarpflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 35 StBVV** — Honorar Jahresabschluss.

## Workflow

### Phase 1 — 8 Wochen vor Stichtag (Anker Stichtag: T-8 Wochen)

- Mandantenfragebogen (siehe `stb-mandantenfragebogen-jahresabschluss`) versenden mit Rueckfrist 4 Wochen.
- Inventur-Termin und -Anweisung mit Mandant schriftlich abstimmen (insbesondere bei Stichtagsinventur am 31.12.).
- Bei Pruefungspflicht (§ 316 HGB): Vor-Pruefungs-Vorbereitung mit dem Wirtschaftspruefer; Pruefungsplanung abstimmen.
- Hinweis an Mandant zu Investitionen, IAB § 7g EStG, Sonder-AfA-Optionen vor Stichtag.

### Phase 2 — Stichtag und Inventur (Bilanzstichtag)

- Inventur vor Ort begleiten oder Beobachterrolle bei groesseren Mandanten; bei kleineren Mandanten Stichprobenbegleitung.
- Inventurprotokolle aufnehmen (Mengen, Bewertungshinweise, Pruefdatum, Bearbeiter).
- Bestandsabweichungen unmittelbar klaeren (Cut-off-Listen Lieferungen / Wareneingang).

### Phase 3 — 1. Quartal nach Stichtag (Wochen 1-4): Bestandskonten abstimmen

- Dezember-Buchungen finalisieren (letzte Belege, Bank-Cut-off, Lohn-Dezember inkl. Boni).
- Bank-Saldenabstimmung Endbestand; Saldenbestaetigungen einholen.
- OPOS-Pflege (Debitoren / Kreditoren); zweifelhafte Forderungen markieren.

### Phase 4 — 1. Quartal nach Stichtag (Wochen 5-10): Abgrenzungen, Rueckstellungen, Anlagen

- Periodenabgrenzung (RAP) gemaess `stb-jahresabschluss-abgrenzungen-rap-rai`.
- Rueckstellungen quantifizieren gemaess `stb-jahresabschluss-rueckstellungen-bewertung`.
- Anlagenspiegel und AfA gemaess `stb-jahresabschluss-anlagenverzeichnis-afa`.
- Saldenabstimmung Forderungen, Verbindlichkeiten, Banken; Werterhellungstatsachen pruefen.

### Phase 5 — 2. Quartal nach Stichtag (Wochen 10-14): Entwurf und Mandantengespraech

- Jahresabschluss-Entwurf (Bilanz, GuV, Anhang); bei Pflichtgesellschaft Lagebericht.
- Wahlrechtsausuebung dokumentieren (Mandantenwahl protokolliert).
- Mandantengespraech zum Entwurf (Brueckenschlag zu `stb-jahresgespraech-mandant-bwa-basis`).

### Phase 6 — 2.-3. Quartal nach Stichtag (Wochen 14-26): Freigabe, Uebermittlung, Offenlegung

- Mandanten-Freigabe schriftlich (Aufstellungserklaerung).
- E-Bilanz-Uebermittlung an FA gemaess `stb-jahresabschluss-elektronische-uebermittlung-ebilanz`.
- Offenlegung im Unternehmensregister (§ 325 HGB) innerhalb 12 Monaten nach Stichtag gemaess `stb-jahresabschluss-veroeffentlichung-bundesanzeiger`.

## Output

- Aufgestellter Jahresabschluss.
- E-Bilanz uebermittelt.
- Bundesanzeiger-Veroeffentlichung.

## Strategie und Praxis-Tipps

- 8-12 Wochen Vorlauf sind Standard.
- Bei Pruefungspflicht: zusaetzliche 4-6 Wochen fuer WP.
- Inventur-Beobachtung beim Mandanten ist wertvoll fuer Bewertung.
- Mandantenfragebogen ist Effizienz-Hebel.
- StBVV § 35: Honorar nach Gegenstandswert; ggf. Pauschal mit Mandant.

## Querverweise

- `stb-mandantenfragebogen-jahresabschluss` — Fragebogen.
- `stb-jahresabschluss-warenbestand-inventur` — Inventur.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandsabstimmung.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — AfA.
- `stb-jahresabschluss-veroeffentlichung-bundesanzeiger` — Bundesanzeiger.
- `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` — E-Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 242, 252, 264, 316, 325.
- StBVV § 35.
- IDW PS 480.
