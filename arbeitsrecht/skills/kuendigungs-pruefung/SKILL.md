---
name: kuendigungs-pruefung
description: Rechtliche Prüfung einer ordentlichen oder außerordentlichen Kündigung – KSchG (allgemeiner und besonderer Kündigungsschutz), § 102 BetrVG (Betriebsratsanhörung), §§ 622, 626 BGB (Fristen und wichtiger Grund), Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz (MuSchG, BEEG, SGB IX, § 15 KSchG).
language: de
triggers:
  - "kündigung prüfen"
  - "kündigungsprüfung"
  - "termination review"
  - "kann ich kündigen"
  - "betriebsbedingte kündigung"
  - "verhaltensbedingte kündigung"
  - "personenbedingte kündigung"
argument-hint: "[Kündigungsanlass und Beschreibung des Arbeitsverhältnisses]"
---

# /arbeitsrecht:kuendigungs-pruefung

## Zweck

Die meisten Kündigungen sind rechtlich unproblematisch. Einige sind Klagen, die noch nicht eingereicht wurden. Dieser Skill findet die Hochrisikofälle, bevor die 3-Wochen-Frist des § 4 KSchG beginnt zu laufen: Sonderkündigungsschutz, fehlende Betriebsratsanhörung, mangelhafte Sozialauswahl, unzureichende Dokumentation.

## Eingaben

- Kündigungsanlass (betriebsbedingt / verhaltensbedingt / personenbedingt)
- Angaben zum Arbeitnehmer: Beschäftigungsdauer, Position, Gehaltsgruppe, Familienstand (für Sozialauswahl), Schwerbehinderung, Betriebsratsmandat, Schwangerschaft/Elternzeit
- Angaben zum Betrieb: Mitarbeiterzahl (KSchG § 23), Betriebsrat vorhanden?
- Vorherige Abmahnungen? (für verhaltensbedingte Kündigung)
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Kündigungsregeln, Eskalation

## Ablauf

### 1. Vorprüfung: Anwendungsbereich KSchG (§ 23 KSchG)

**Schwellenwert:** KSchG gilt für Arbeitnehmer, die länger als 6 Monate beschäftigt sind (§ 1 Abs. 1 KSchG), wenn im Betrieb **mehr als 10 Arbeitnehmer** i.S.d. § 23 KSchG beschäftigt sind (Vollzeitkräfte zählen voll; Teilzeitkräfte bis 20 h = 0,5; bis 30 h = 0,75; Leiharbeitnehmer ohne Berücksichtigung).

**Kleinbetrieb (≤ 10 AN):** Kein allgemeiner KSchG-Schutz, aber Grundrechtsschutz (BAG, Urt. v. 21.02.2001 – 2 AZR 15/00, NZA 2001, 833: Kündigung darf kein verkapptes Diskriminierungsmittel sein `[Modellwissen – prüfen]`); BVerfG, Beschl. v. 27.01.1998 – 1 BvL 15/87, NJW 1998, 1475.

### 2. Sonderkündigungsschutz-Check (vor allem anderen)

Bei Vorliegen eines der folgenden Merkmale: **🔴 Blockierend – sofortige Eskalation**

| Schutztatbestand | Norm | Anforderung |
|---|---|---|
| Schwangerschaft / Mutterschutz | § 17 MuSchG | Zustimmung zuständige Behörde (Amt für Arbeitsschutz) vor Ausspruch |
| Elternzeit | § 18 BEEG | Zustimmung zuständige Behörde; Ausnahme bei schwerwiegenden Gründen § 18 Abs. 1 S. 2 BEEG |
| Schwerbehinderte / Gleichgestellte | § 168 SGB IX | Zustimmung Inklusionsamt (früher: Integrationsamt) vor Ausspruch; 3-Wochen-Antragsfrist |
| Betriebsratsmitglied, Wahlvorstand u.a. | § 15 KSchG | Ordentliche Kündigung ausgeschlossen; ao. Kündigung § 103 BetrVG (BR-Zustimmung) |
| Datenschutzbeauftragter | § 38 Abs. 2 BDSG i.V.m. § 6 Abs. 4 BDSG | Kündigungsschutz während Amtszeit + 1 Jahr danach |
| Elternzeitbeantragung | § 18 Abs. 1 BEEG | Beginnt ab Antragstellung |
| Pflegezeit | § 5 PflegeZG | Schutz wie BEEG |

### 3. Betriebsratsanhörung (§ 102 BetrVG)

Falls Betriebsrat vorhanden: **Jede Kündigung vor Ausspruch anhören.** Ohne ordnungsgemäße Anhörung ist die Kündigung unwirksam (§ 102 Abs. 1 S. 3 BetrVG).

Checkliste:
- Ist der BR schriftlich informiert worden?
- Inhalt der Anhörung vollständig? (Personalien, Art der Kündigung, Kündigungsfrist, Kündigungsgrund; BAG, Urt. v. 22.09.1994 – 2 AZR 31/94, NZA 1995, 363 `[Modellwissen – prüfen]`)
- Frist abgewartet? (ordentlich: 1 Woche; außerordentlich: 3 Tage; § 102 Abs. 2 BetrVG)
- Ordnungsgemäße Bedenken des BR beachtet (keine Vetorechte bei ordentlicher Kündigung, aber Widerspruch nach § 102 Abs. 3 BetrVG gibt Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG)

Verweis auf separaten Skill: `/arbeitsrecht:betriebsrat-anhoerung`

### 4. Prüfung des Kündigungsgrunds (§ 1 KSchG)

**A – Betriebsbedingte Kündigung:**

1. **Unternehmerische Entscheidung:** Vom Arbeitgeber frei, aber dringend erforderlich (keine andere zumutbare Beschäftigungsmöglichkeit; BAG, Urt. v. 29.03.2007 – 2 AZR 31/06, NZA 2007, 912 Rn. 21 `[Modellwissen – prüfen]`)
2. **Wegfall des Arbeitsplatzes:** Konkret und dauerhaft; bloße Umsatzrückgänge genügen nicht
3. **Weiterbeschäftigung auf freiem vergleichbaren Arbeitsplatz** ausgeschlossen (§ 1 Abs. 2 S. 2 KSchG)
4. **Sozialauswahl (§ 1 Abs. 3 KSchG)** – zentraler Prüfpunkt (siehe unten)
5. **Massenentlassung** (§§ 17–18 KSchG): Bei Entlassung von ≥ 5 (kleiner Betrieb) bis ≥ 30 AN (großer Betrieb) innerhalb von 30 Tagen: Anzeigepflicht bei der Agentur für Arbeit VOR Ausspruch der Kündigungen. Fehler führt zur Unwirksamkeit (BAG, Urt. v. 22.11.2012 – 2 AZR 371/11, NZA 2013, 437 `[Modellwissen – prüfen]`)

**Sozialauswahl (§ 1 Abs. 3 KSchG):**

Unter vergleichbaren Arbeitnehmern müssen die sozial am wenigsten schutzwürdigen entlassen werden. Kriterien:
- Betriebszugehörigkeit
- Lebensalter
- Unterhaltsverpflichtungen
- Schwerbehinderung

Prüfschema:
1. Vergleichsgruppe bilden (gleiche Hierarchieebene, austauschbar durch Einarbeitung ≤ 3 Monate)
2. Sozialpunkte berechnen (§ 1 Abs. 3 S. 1 KSchG; keine gesetzliche Punktetabelle – Betriebsvereinbarung oder Interessenausgleich empfohlen)
3. Herausnahme von Leistungsträgern (§ 1 Abs. 3 S. 2 KSchG): Restriktiv; BAG, Urt. v. 07.07.2011 – 2 AZR 476/10, NZA 2012, 150 `[Modellwissen – prüfen]`

**B – Verhaltensbedingte Kündigung:**

1. **Abmahnung vorausgegangen?** Grundsätzlich erforderlich außer bei schwerwiegenden Pflichtverletzungen (BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227: „Emmely-Entscheidung" zur Interessenabwägung `[Modellwissen – prüfen]`)
2. Abmahnung hinreichend bestimmt? (BAG, Urt. v. 19.11.2015 – 2 AZR 217/15, NZA 2016, 540: konkrete Schilderung, klare Verhaltenserwartung, Sanktionsandrohung `[Modellwissen – prüfen]`)
3. **Interessenabwägung:** Schwere der Pflichtverletzung vs. Dauer der Beschäftigung, Sozialauswahl, Wiederholungsgefahr

Verweis auf separaten Skill: `/arbeitsrecht:abmahnung-arbeitsrecht`

**C – Personenbedingte Kündigung (insb. krankheitsbedingt):**

1. **Prognose negativer Art:** Weitere erhebliche Fehlzeiten zu erwarten?
2. **Betriebliche Beeinträchtigung:** Erhebliche Störung des Betriebsablaufs oder Entgeltfortzahlungskosten > 6 Wochen p.a.?
3. **Interessenabwägung** (BAG, Urt. v. 13.05.2015 – 2 AZR 565/14, NZA 2016, 116 `[Modellwissen – prüfen]`)
4. **BEM** (Betriebliches Eingliederungsmanagement) nach § 167 Abs. 2 SGB IX: Vor Kündigung durchführen, andernfalls erhöhte Darlegungslast des Arbeitgebers (BAG, Urt. v. 12.07.2007 – 2 AZR 716/06, NZA 2008, 173 `[Modellwissen – prüfen]`)

### 5. Kündigungsfristen (§ 622 BGB / Tarifvertrag)

| Beschäftigungsdauer | Frist (§ 622 Abs. 2 BGB) |
|---|---|
| 0–2 Jahre | 4 Wochen zum 15. oder Monatsende |
| 2–5 Jahre | 1 Monat zum Monatsende |
| 5–8 Jahre | 2 Monate |
| 8–10 Jahre | 3 Monate |
| 10–12 Jahre | 4 Monate |
| 12–15 Jahre | 5 Monate |
| 15–20 Jahre | 6 Monate |
| > 20 Jahre | 7 Monate |

Tarifvertragliche Abweichungen prüfen! Ggf. günstigere Individualvereinbarung.

**Außerordentliche Kündigung (§ 626 BGB):** Wichtiger Grund + 2-Wochen-Frist ab Kenntnis (§ 626 Abs. 2 BGB); BAG, Urt. v. 21.06.2012 – 2 AZR 694/11, NZA 2013, 199 `[Modellwissen – prüfen]`.

### 6. Abfindungsangebot (§ 1a KSchG)

Arbeitgeber kann mit der Kündigung eine Abfindung nach § 1a KSchG anbieten (0,5 Monatsgehalt × Beschäftigungsjahre), wenn Arbeitnehmer keine Klage erhebt. Dies schließt Wiedereinstellungsansprüche aus.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-deutsches-recht.md`.

Wesentliche Quellen:
- Dörner/Vossen, in: KR, 13. Aufl. 2022, § 1 KSchG Rn. 1 ff. (Sozialauswahl)
- Becker/Wolff, in: APS, 6. Aufl. 2021, § 1 KSchG Rn. 500 ff. (betriebsbedingte Kündigung)
- Preis, in: ErfK, 24. Aufl. 2024, § 626 BGB Rn. 1 ff. (außerordentliche Kündigung)
- BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 (Verhältnismäßigkeit, „Emmely")
- BAG, Urt. v. 07.07.2011 – 2 AZR 476/10, NZA 2012, 150 (Leistungsträgerherausnahme)
- BAG, Urt. v. 22.11.2012 – 2 AZR 371/11, NZA 2013, 437 (Massenentlassung)
- BAG, Urt. v. 12.07.2007 – 2 AZR 716/06, NZA 2008, 173 (BEM)

## Ausgabeformat

Strukturierte Kündigungsprüfung als Memo:

```
KÜNDIGUNGSPRÜFUNG – [Arbeitnehmer-ID/Position] – [Datum]
VERTRAULICH – MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

Ergebnis: [🟢 Kündigung rechtlich möglich / 🟡 Kündigung möglich mit Auflagen / 🔴 Kündigung nicht empfohlen]

⚠️ Prüfhinweis: [Quellen, Flags, Aktualität]

I.   KSchG-Anwendungsbereich         [🟢 / 🟡 / N/A]
II.  Sonderkündigungsschutz-Check    [🟢 / 🔴 Flag: ...]
III. Betriebsratsanhörung            [🟢 / 🔴 ausstehend]
IV.  Kündigungsgrund (§ 1 KSchG)     [🟢 / 🟡 / 🔴]
     Typ: [betriebsbedingt / verhaltensbedingt / personenbedingt]
     Begründung: ...
V.   Sozialauswahl (falls bb.)       [🟢 / 🟡 / 🔴]
     Vergleichsgruppe: [N AN]
     Sozialpunkte: [Tabelle]
VI.  Kündigungsfrist                 [Frist]
VII. Abfindungsangebot (optional)    [§ 1a KSchG Betrag]

Offene Flaggen: [Liste mit [prüfen]-Markierungen]
Eskalation: [ja/nein – Begründung]

Wie weiter? [Entscheidungsbaum]
```

## Beispiele

**Beispiel – Betriebsbedingte Kündigung mit Sozialauswahl:**

*Sachverhalt:* Mandant (Maschinenbauunternehmen, 35 AN, kein BR) will eine von drei Stellen im Bereich Vertriebsinnendienst streichen. Drei Arbeitnehmer: A (10 Jahre, 45 Jahre, 2 Kinder), B (3 Jahre, 30 Jahre, ledig, anerkannte Schwerbehinderte GdB 50), C (8 Jahre, 55 Jahre, geschieden, 1 Kind).

*Ergebnis (Urteilsstil):*

Die beabsichtigte Kündigung ist der des Arbeitnehmers C am ehesten begründbar. In der Sozialauswahl nach § 1 Abs. 3 KSchG sind alle drei Arbeitnehmer in eine Vergleichsgruppe einzustellen (gleiche Funktion, Austauschbarkeit gegeben). Arbeitnehmer B genießt Sonderkündigungsschutz nach § 168 SGB IX; eine Kündigung erfordert Zustimmung des Inklusionsamts (🔴 Blockierend). A und C stehen im direkten Auswahlvergleich: Die längere Betriebszugehörigkeit von A (10 Jahre), sein Lebensalter (45 J.) und die Unterhaltsverpflichtungen (2 Kinder) überwiegen die Schutzwürdigkeit von C (8 Jahre, 55 Jahre, 1 Kind). C ist nach Sozialpunkten am wenigsten schutzwürdig – Kündigung sozialauswahl-konform, wenn Interessenausgleich dokumentiert wird.

🟠 Empfehlung: Vor Ausspruch formlose (da kein BR vorhanden) Kündigung und schriftliche Sozialauswahldokumentation erstellen. Abfindungsangebot gem. § 1a KSchG erwägen.

## Risiken / typische Fehler

- **Massenentlassungsanzeige vergessen** (§§ 17–18 KSchG) – führt zur Unwirksamkeit aller Kündigungen; Schwellenwerte im Blick behalten.
- **Betriebsratsanhörung inhaltlich unvollständig** – fehlende Angaben zur Person oder zum Kündigungsgrund machen Anhörung unwirksam (§ 102 Abs. 1 S. 3 BetrVG).
- **Sonderkündigungsschutz übersehen** – insbesondere bei Betriebsratsmitgliedern, Schwangeren, Elternzeitnehmenden.
- **Sozialauswahl ohne Dokumentation** – bei Klagefrist-Ablauf (§ 4 KSchG) kaum nachrüstbar; immer schriftlich begründen.
- **2-Wochen-Frist § 626 Abs. 2 BGB** – beginnt mit positiver Kenntnis des Kündigungsberechtigten, nicht mit vager Vermutung.
- **BEM nicht durchgeführt** – erhöhte Darlegungslast; vor krankheitsbedingter Kündigung dokumentieren.
