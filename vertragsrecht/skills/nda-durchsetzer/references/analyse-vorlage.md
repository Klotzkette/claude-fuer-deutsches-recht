# Analyse-Vorlage NDA-Durchsetzer

> Verbindliche Struktur der **strukturierten Analyse**, die parallel zum
> Redline-Dokument als eigenständiges Dokument auszuliefern ist.
> Reihenfolge und Abschnittsnummern sind verbindlich — sie sollen
> Mandantinnen, Mandanten und verhandelnden Anwältinnen, Anwälten ein
> wiedererkennbares Format bieten.

---

## Kopfzeile (Pflichtfelder)

| Feld | Beispielinhalt |
|---|---|
| Mandantin / Mandant | Maschinenbau Müller GmbH |
| Gegenseite | Roboterhersteller AG, München |
| Anlass | Anbahnung Komponentenlieferantenmandat Mehrachsen-Steuerung |
| Rolle der Mandantin | Discloser (vorrangig), beidseitige Vertraulichkeit |
| Prüflings-NDA | Dokumentversion, Datum, 12 Klauseln |
| Hausvorlage | Vorlage Nr. X, Datum |
| Erstellt am | TT.MM.JJJJ |
| Bearbeiter (in) | Name, Berufsbezeichnung |
| Anwaltlicher Vorbehalt | „Endkontrolle durch verantwortliche Rechtsanwältin / verantwortlichen Rechtsanwalt vor Versand zwingend." |

---

## 1. Executive Summary

**Umfang:** 3 bis 5 kurze Absätze, max. 1 Seite.

**Inhalte (Pflicht):**

1. **Gesamtbewertung** — eine Zeile: „Das NDA ist in der vorliegenden
   Fassung [annahmefähig nach Redline / nur nach grundlegender
   Überarbeitung tragbar / als Verhandlungsgrundlage ungeeignet]."
2. **Drei bis fünf kritischste Abweichungen** vom Hausstandard, jeweils
   in einem Halbsatz mit Risikoampel:
   - `[ROTE LINIE]` — Mindeststandard verletzt, ohne Korrektur nicht
     zeichnungsfähig.
   - `[NACHTEILIG]` — Marktstandard verletzt, nachverhandeln.
   - `[NEUTRAL]` — Marktüblich, kein Korrekturbedarf.
   - `[GÜNSTIG]` — vorteilhaft, beibehalten.
3. **Handlungsempfehlung:**
   - **Redline & Verhandeln** (Standard).
   - **Eigenes NDA als Gegenvorschlag** (bei mehr als drei
     `[ROTE LINIE]`-Treffern oder grundlegend abweichender Systematik).
   - **Ablehnung des NDA-Wegs** (z. B. Schiedsverfahren in Übersee mit
     Geheimnis-Zwang).
4. **Verhandlungshebel** — was die Gegenseite voraussichtlich akzeptiert,
   was nicht; mögliche Kompromisslinien.

---

## 2. Struktureller Vergleich

**Format:** Tabelle, eine Zeile pro Regelungsbereich.

| Regelungsbereich | Hausvorlage | Prüflings-NDA | Abweichung |
|---|---|---|---|
| Definition Confidential Information | weite Definition, mündlich umfasst | nur schriftlich gekennzeichnet | nachteilig |
| Ausnahmen | abschließende fünf | abschließende vier (eigenständige Entwicklung fehlt) | nachteilig |
| Dauer | 5 Jahre + unbefristet GeschGehG | 2 Jahre flat | nachteilig |
| Rückgabe / Löschung | mit Backup-Ausnahme, schriftliche Bestätigung | sofort, ohne Bestätigungspflicht | NEUTRAL bis nachteilig |
| Beweislast | keine Umkehr | Beweislastumkehr bei Vorliegen bei Drittem | rote Linie |
| Vertragsstrafe | 25.000 € / max. 250.000 € | nicht geregelt | fehlende Regelung |
| Recht | dt. Recht, CISG aus | kalifornisches Recht | rote Linie |
| Gerichtsstand | Sitz Mandantin / Frankfurt | ICC Genf | nachteilig |
| Verbundene Unternehmen | § 15 AktG, § 278 BGB | nicht geregelt | fehlende Regelung |
| Lizenzausschluss | ausdrücklich | nicht geregelt | fehlende Regelung |
| Salvatorische | zurückhaltend | pauschal | nachteilig |
| Weitere Klauseln | – | 60-monatige Abwerbeverbots-Klausel | unüblich |

**Pflichtangabe:** fehlende Regelungen ausdrücklich mit „nicht geregelt"
kennzeichnen — nicht weglassen.

---

## 3. Detaillierter Klausel-für-Klausel-Vergleich

**Format:** pro Klausel des Prüflings eine eigene Mini-Tabelle nach dem
Schema aus `SKILL.md`. Reihenfolge folgt der Nummerierung des
Prüflings, nicht der Hausvorlage.

### Schema pro Klausel

| Feld | Inhalt |
|---|---|
| **Prüflings-Klausel** | § X / Ziffer Y, Überschrift |
| **Inhalt der Prüflings-Klausel** | wörtlich oder verkürzt, **ohne Interpretation** |
| **Referenz-Klausel der Hausvorlage** | § X / Ziffer Y, Überschrift |
| **Inhaltlicher Vergleich** | Was steht im Prüfling, was in der Referenz, wo weicht es ab? |
| **Risikoampel** | `[GÜNSTIG]` / `[NEUTRAL]` / `[NACHTEILIG]` / `[ROTE LINIE]` |
| **Begründung der Bewertung** | Norm, Rspr., Marktstandard — mit Pinpoint |
| **Redline-Vorschlag** | minimale Einfügung / Streichung im Änderungsmodus |
| **Verhandlungsargument** | wie wird der Vorschlag der Gegenseite verkauft? |
| **Fallback / Kompromisslinie** | was, wenn Gegenseite den Vorschlag ablehnt? |

**Pflichten:**
- Bei unklarer Klausel: Eintrag `[KLAUSEL UNKLAR — RÜCKFRAGE]` in der
  Risikoampel und Erläuterung statt zu raten.
- Bei jedem `[ROTE LINIE]`-Treffer: zwingend Eintrag in
  Abschnitt 6 als Priorität 1.
- Bei jedem `[NACHTEILIG]`-Treffer: zwingend Eintrag in Abschnitt 6 als
  Priorität 2 oder 3.

---

## 4. Fehlende Regelungen

**Format:** pro fehlender Regelung eine eigene Mini-Tabelle.

| Feld | Inhalt |
|---|---|
| **Bereich** | Verbundene Unternehmen / Kein Lizenzübergang / Vertragsstrafe / … |
| **Schutzzweck** | Warum ist diese Regelung wichtig? |
| **Folgen ohne Regelung** | Was passiert nach dispositivem Recht? Welche Lücken bleiben? |
| **Vorgeschlagener Klauselentwurf** | vollständige Klausel in der Systematik des Prüflings (mit Klauselnummer und Überschrift entsprechend) |
| **Einfügungsstelle** | nach § X / als § Y / als Unterabsatz von § Z |
| **Priorität** | 1–4 (siehe Abschnitt 6) |

**Pflichtumfang:** mindestens die zehn Mindeststandards aus
`references/mindeststandards.md` abgearbeitet — auch wenn alle vorhanden
sind, ausdrücklich „vollständig vorhanden" vermerken.

---

## 5. Unübliche oder riskante Klauseln im Prüfling

**Format:** pro unüblicher Klausel eine eigene Mini-Tabelle.

| Feld | Inhalt |
|---|---|
| **Klausel im Prüfling** | § X / Ziffer Y, Überschrift |
| **Inhalt** | wörtlich oder verkürzt |
| **Pendant in der Hausvorlage** | „kein Pendant" oder Verweis |
| **Versteckte Risiken** | z. B. faktisches Abwerbeverbot, faktische Wettbewerbsbeschränkung, faktische Exklusivität |
| **Wechselwirkung mit anderen Klauseln** | z. B. Beweislastumkehr + sehr weite Definition + sehr lange Dauer = unkontrollierbares Haftungsrisiko |
| **Empfehlung** | Streichung / Modifikation / Bedingung knüpfen / akzeptabel mit Begründung |
| **Priorität** | 1–4 |

**Pflichthinweis bei wettbewerbs-/kartellrechtlich relevanten Klauseln:**
Verweis auf §§ 1, 2 GWB und Art. 101 AEUV; bei Verdacht **rote Linie**,
weil unwirksam.

---

## 6. Priorisierte Änderungsliste

**Format:** eine Tabelle, alle Änderungspunkte aus den Abschnitten 3, 4
und 5 in einer Liste, sortiert nach Priorität.

| Priorität | Bereich | Forderung an die Gegenseite | Verhandlungsspielraum | Fallback |
|---|---|---|---|---|
| **1 — zwingend / rote Linien** | Recht | Deutsches Recht, CISG aus | keiner | Verhandlung abbrechen |
| **1 — zwingend / rote Linien** | Beweislast | Streichung der Beweislastumkehr in § 8 | keiner | Verhandlung abbrechen |
| **2 — Mindeststandard** | Definition CI | Erweiterung auf mündlich offengelegt | hoch (Argument: bilaterale Gegenseitigkeit) | Erweiterung nur auf erkennbar vertraulich |
| **2 — Mindeststandard** | Verbundene Unternehmen | Einfügung § 15 AktG + § 278 BGB | hoch | Akzeptanz als Mitarbeiter-Haftung |
| **2 — Mindeststandard** | Vertragsstrafe | Einfügung 25.000 € / max. 250.000 € | mittel | 10.000 € / 100.000 € |
| **3 — Marktstandard** | Dauer | Verlängerung von 2 auf 5 Jahre | mittel | 3 Jahre + unbegrenzt GeschGehG |
| **3 — Marktstandard** | Gerichtsstand | Frankfurt a. M. statt ICC Genf | hoch | DIS-Schiedsverfahren Sitz Frankfurt |
| **4 — wünschenswert** | Salvatorische | Zurückhaltende Formulierung mit § 139 BGB | niedrig | belassen |
| **4 — wünschenswert** | Lizenzausschluss | ausdrückliche Klarstellung | hoch | implizit aus dispositivem Recht ausreichend |

**Definition der Prioritätsstufen:**

- **Priorität 1 — zwingend / rote Linien.** Ohne Korrektur nicht
  zeichnungsfähig. Mandantin / Mandant ist klar zu informieren, dass
  ein NDA-Abschluss in der vorliegenden Form unwirksam, rechtswidrig
  oder existenzgefährdend wäre.
- **Priorität 2 — Mindeststandard.** Hausstandard verletzt. In der
  Regel nachverhandeln; Abweichung nur nach ausdrücklicher Freigabe.
- **Priorität 3 — Marktstandard.** Verhandlung üblich; bei Ablehnung
  durch Gegenseite Risiko erläutern und entscheiden lassen.
- **Priorität 4 — wünschenswert.** Verhandeln nur, wenn andere
  Forderungen ohne Aufwand mit durchsetzbar.

---

## Anhang A — Verhandlungs-Cheat-Sheet (optional)

Eine Seite, drei Spalten:

| Punkt | Unsere Position | Wenn Gegenseite ablehnt |
|---|---|---|
| Deutsches Recht | ROTE LINIE | Verhandlung abbrechen |
| Beweislast | ROTE LINIE | Verhandlung abbrechen |
| Mündliche Vertraulichkeit | Mindeststandard | erkennbar vertraulich als Mindestlösung |
| Vertragsstrafe 25.000 €/250.000 € | Mindeststandard | 10.000 €/100.000 € |
| Gerichtsstand DE | Mindeststandard | DIS-Schiedsverfahren Sitz DE |

Das Cheat-Sheet ist als Verhandlungshilfe für die mandatsführende Person
gedacht — **nicht** zur Weitergabe an die Gegenseite.

---

## Anhang B — Quellennachweis

Pflichtinhalte am Ende der Analyse:

- Gesetze: §§ 241, 280, 305 ff., 307, 311, 339, 343 BGB; § 348 HGB;
  § 15 AktG; §§ 2, 3, 5, 6, 7, 10 GeschGehG; § 138 ZPO.
- Rechtsprechung: mindestens zwei BGH-Belege mit Pinpoint nach
  Standard-Zitierweise (siehe `references/zitierweise.md`).
- Kommentarliteratur: mindestens zwei Belege nach Schema
  „Bearbeiter, in: Werk, Aufl. Jahr, § X Rn. Y" (siehe
  `references/zitierweise.md`).
- Aufsätze: nach Schema „Verfasser, NJW 2019, 2540 (2543 f.)" (ohne
  Heftnummer, ohne „S.").

**Palandt-Hinweis:** Wenn im Prüfling oder in Bestandsdokumenten
„Palandt" zitiert wird, im Analyse-Dokument den Hinweis aufnehmen:

> Der BGB-Kommentar „Palandt" heißt seit der 81. Aufl. 2022
> **Grüneberg**. Sofern im Bestand auf eine konkrete Palandt-Altauflage
> Bezug genommen werden soll, ist die Auflage (z. B. 80. Aufl. 2021)
> ausdrücklich zu kennzeichnen.

---

## Hinweis zur Verwendung

Diese Vorlage ist verbindlich. Abweichungen von Reihenfolge oder
Abschnittsnummerierung sind nur zulässig, wenn das einzelne Mandat dies
fachlich erfordert; in diesem Fall ist die Abweichung in der Kopfzeile
zu vermerken.
