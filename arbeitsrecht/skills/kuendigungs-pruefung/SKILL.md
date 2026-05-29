---
name: kuendigungs-pruefung
description: "Rechtliche Prüfung einer ordentlichen oder außerordentlichen Kündigung – KSchG (allgemeiner und besonderer Kündigungsschutz), § 102 BetrVG (Betriebsratsanhörung), §§ 622 und 626 BGB (Fristen und wichtiger Grund), Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz (MuSchG, BEEG, SGB IX, § 15 KSchG)."
---

# /arbeitsrecht:kündigungs-prüfung

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Frist abgewartet? (ordentlich: 1 Woche; außerordentlich: 3 Tage; § 102 Abs. 2 BetrVG)
- Ordnungsgemäße Bedenken des BR beachtet (keine Vetorechte bei ordentlicher Kündigung, aber Widerspruch nach § 102 Abs. 3 BetrVG gibt Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG)

Verweis auf separaten Skill: `/arbeitsrecht:betriebsrat-anhörung`

### 4. Prüfung des Kündigungsgrunds (§ 1 KSchG)

**A – Betriebsbedingte Kündigung:**

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Wegfall des Arbeitsplatzes:** Konkret und dauerhaft; bloße Umsatzrückgänge genügen nicht
3. **Weiterbeschäftigung auf freiem vergleichbaren Arbeitsplatz** ausgeschlossen (§ 1 Abs. 2 S. 2 KSchG)
4. **Sozialauswahl (§ 1 Abs. 3 KSchG)** – zentraler Prüfpunkt (siehe unten)
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Sozialauswahl (§ 1 Abs. 3 KSchG):**

Unter vergleichbaren Arbeitnehmern müssen die sozial am wenigsten schutzwürdigen entlassen werden. Kriterien:
- Betriebszugehörigkeit
- Lebensalter
- Unterhaltsverpflichtungen
- Schwerbehinderung

Prüfschema:
1. Vergleichsgruppe bilden (gleiche Hierarchieebene, austauschbar durch Einarbeitung ≤ 3 Monate)
2. Sozialpunkte berechnen (§ 1 Abs. 3 S. 1 KSchG; keine gesetzliche Punktetabelle – Betriebsvereinbarung oder Interessenausgleich empfohlen)
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**B – Verhaltensbedingte Kündigung:**

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Interessenabwägung:** Schwere der Pflichtverletzung vs. Dauer der Beschäftigung, Sozialauswahl, Wiederholungsgefahr

Verweis auf separaten Skill: `/arbeitsrecht:abmahnung-arbeitsrecht`

**C – Personenbedingte Kündigung (insb. krankheitsbedingt):**

1. **Prognose negativer Art:** Weitere erhebliche Fehlzeiten zu erwarten?
2. **Betriebliche Beeinträchtigung:** Erhebliche Störung des Betriebsablaufs oder Entgeltfortzahlungskosten > 6 Wochen p.a.?
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Abfindungsangebot (§ 1a KSchG)

Arbeitgeber kann mit der Kündigung eine Abfindung nach § 1a KSchG anbieten (0,5 Monatsgehalt × Beschäftigungsjahre), wenn Arbeitnehmer keine Klage erhebt. Dies schließt Wiedereinstellungsansprüche aus.

### 7. DSGVO-Auskunftsersuchen als Druckmittel im Kündigungskontext

**Typische Konstellation:** Unmittelbar vor oder nach Ausspruch der Kündigung – oft zeitgleich mit der Ankündigung einer KSchG-Klage – stellt der Arbeitnehmer oder sein Bevollmächtigter ein Auskunftsersuchen nach Art. 15 DSGVO. Ziel ist häufig, über den Umweg des Datenschutzrechts Einblick in interne Personalakten, Abmahnungsunterlagen oder Vermerke zu erlangen und so den Arbeitgeber unter Vergleichsdruck zu setzen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Ein Auskunftsersuchen kann nach Art. 12 Abs. 5 S. 2 DSGVO als exzessiv abgelehnt oder mit angemessenen Kosten belegt werden, wenn der Verantwortliche (Arbeitgeber) zwei Elemente nachweist:

1. **Objektives Element:** Äußere Umstände lassen auf missbräuchliche Zweckverfolgung schließen — z. B. ungewöhnlich kurzer zeitlicher Abstand zwischen Zugang der Kündigung und Auskunftsantrag, Muster massenhafter Legal-Tech-gestützter Antragstellung, Anmeldung zur Datenverarbeitung allein zum Zweck der Anfrage.
2. **Subjektives Element:** Missbräuchliche Absicht — Instrumentalisierung des Auskunftsrechts vorrangig zur Generierung von Schadensersatzansprüchen nach Art. 82 DSGVO oder zur Prozesstaktik, nicht zum Schutz personenbezogener Daten.

Hürden sind **hoch**: Das Auskunftsrecht ist ein Grundrecht (Art. 8 GRCh); Ausnahmen sind eng auszulegen. Auch ein erstmaliges Ersuchen kann exzessiv sein, aber bloße Mehrfachanträge oder die bloße Tatsache vergangener Auskunftsansprüche genügen nicht.

**BAG-Linie zu Art. 82 DSGVO:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Praxishinweise für den Arbeitgeber:**
- DSGVO-Auskunft fristgerecht innerhalb eines Monats beantworten (Art. 12 Abs. 3 DSGVO); unberechtigte Ablehnung kann eigenständigen Schadensersatzanspruch nach Art. 82 DSGVO auslösen.
- Dokumentation für Missbrauchseinwand anlegen: Datum Kündigung, Datum Auskunftsantrag, Vorliegen von Legal-Tech-Vollmacht, Muster bei anderen Mitarbeitern.
- Parallellauf Kündigungsschutzverfahren und DSGVO-Auskunftsstreit im Blick behalten: Zuständiges Gericht für Auskunftsklage ist nach Art. 79 DSGVO i.V.m. § 44 BDSG das Landgericht (nicht das Arbeitsgericht); Koordinierung der Prozesstaktik erforderlich.

Querverweis: `datenschutzrecht/skills/dsgvo-auskunft/SKILL.md` (soweit im Plugin vorhanden).

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Dörner/Vossen, in: KR, 13. Aufl. 2022, § 1 KSchG Rn. 1 ff. (Sozialauswahl)
- Becker/Wolff, in: APS, 6. Aufl. 2021, § 1 KSchG Rn. 500 ff. (betriebsbedingte Kündigung)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
