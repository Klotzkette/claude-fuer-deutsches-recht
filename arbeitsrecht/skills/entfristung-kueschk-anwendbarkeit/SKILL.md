---
name: entfristung-kueschk-anwendbarkeit
description: "Entfristung Kueschk Anwendbarkeit im Plugin Arbeitsrecht: prüft konkret Prüft Anwendbarkeit des Kündigungsschutzgesetzes, Elektronische Signaturen und Befristungsabreden, Grundwarnung Entfristungsklage, Sprechzettel für Guetetermin und Kammertermin in der. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Entfristung Kueschk Anwendbarkeit

## Arbeitsbereich

**Entfristung Kueschk Anwendbarkeit** ordnet den Fall über die tragenden Prüfungslinien: Prüft Anwendbarkeit des Kündigungsschutzgesetzes, Elektronische Signaturen und Befristungsabreden, Grundwarnung Entfristungsklage. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `kueschk-anwendbarkeit-kschg-pruefen` | Prüft Anwendbarkeit des Kündigungsschutzgesetzes: Wartezeit sechs Monate nach § 1 Abs. 1 KSchG; Schwellenwert zehn Arbeitnehmer nach § 23 KSchG; Berechnung von Teilzeitkraeften und Auszubildenden; allgemeiner Kündigungsschutz bei Nichtanwendbarkeit. |
| `entfristung-elektronische-signatur-vorsicht` | Elektronische Signaturen und Befristungsabreden: einfache Signatur, Scan und fortgeschrittene Signatur genuegen nicht; echte qualifizierte elektronische Signatur nach § 126a BGB kann die Schriftform ersetzen. Prüft DocuSign Adobe Sign HelloSign Zertifikate, beide Parteien, Timing, Zugang und Rechtsfolge § 16 Satz 1 TzBfG. |
| `entfristung-grundwarnung-drei-wochen-frist` | Grundwarnung Entfristungsklage: § 17 TzBfG drei Wochen ab vereinbartem Vertragsende; absolute Ausschlussfrist; § 17 Satz 2 TzBfG i.V.m. § 7 KSchG Fiktion Wirksamkeit der Befristung bei Fristversaeumnis; Fristberechnung; nachtraegliche Zulassung. |
| `entfristung-guetetermin-und-kammertermin-sprechzettel` | Sprechzettel für Guetetermin und Kammertermin in der Entfristungsklage: Antragsstellung; Kernargumente Schriftformmangel und Sachgrundmangel; Vergleichsstrategie; Vorbereitung Zeugenvernehmung; Verhandlungsposition; Normen § 54 und § 57 ArbGG. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `kueschk-anwendbarkeit-kschg-pruefen`

**Fokus:** Prüft Anwendbarkeit des Kündigungsschutzgesetzes: Wartezeit sechs Monate nach § 1 Abs. 1 KSchG; Schwellenwert zehn Arbeitnehmer nach § 23 KSchG; Berechnung von Teilzeitkraeften und Auszubildenden; allgemeiner Kündigungsschutz bei Nichtanwendbarkeit.

# KSchG-Anwendbarkeit prüfen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KSchG-Anwendbarkeit prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre sofort

1. Wann begann das Arbeitsverhältnis? (6-Monats-Wartezeit nach § 1 Abs. 1 KSchG)
2. Wie viele Arbeitnehmer beschäftigt der Betrieb? (Schwellenwert > 10 nach § 23 Abs. 1 KSchG)
3. Gibt es mehrere Betriebe im Unternehmen? (Betriebs- nicht Unternehmensbezug!)
4. Bestehen Sonderkündigungsschutzmechanismen unabhängig vom KSchG? (MuSchG, BEEG, SGB IX, § 15 KSchG)
5. Wann wurde die Kündigung zugestellt? (§ 4 KSchG-Frist läuft auch ohne KSchG-Anwendbarkeit für Sonderschutz)

## Zentrale Normen

- § 1 Abs. 1 KSchG — Wartezeit 6 Monate ununterbrochen
- § 23 Abs. 1 KSchG — Schwellenwert: regelmäßig mehr als 10 Arbeitnehmer
- § 23 Abs. 1 Satz 2 KSchG — Auszubildende zählen nicht
- § 5 Abs. 3 BetrVG — leitende Angestellte: eigene Regelungen, kein BetrVG
- §§ 138, 242 BGB — allgemeiner Kündigungsschutz (Treu und Glauben, Sittenwidrigkeit)
- §§ 17, 18 MuSchG; § 18 BEEG; § 168 SGB IX — Sonderkündigungsschutz unabhängig von KSchG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Prüfung

### Schritt 1: Wartezeit § 1 Abs. 1 KSchG

Das KSchG gilt nur bei Arbeitsverhältnis **länger als 6 Monate** ohne Unterbrechung.

- Beginn: erster Arbeitstag
- Ende: Datum des Zugangs der Kündigung
- Vorbeschäftigungszeiten beim selben Arbeitgeber können angerechnet werden

**Entscheidungsbaum:**
```
Arbeitsverhältnis ab: [DATUM]
Kündigung zugegangen: [DATUM]
Dauer: [MONATE]
 ≤ 6 Monate → KSchG nicht anwendbar
 > 6 Monate → weiter zu Schritt 2
```

### Schritt 2: Betriebsgröße § 23 Abs. 1 KSchG

KSchG gilt nur wenn **regelmäßig mehr als 10 Arbeitnehmer** im Betrieb beschäftigt.

**Berechnung:**
- Vollzeitkräfte (> 30 Std./Woche): zählen als 1.0
- Teilzeitkräfte bis 30 Std./Woche: zählen als 0.75
- Teilzeitkräfte bis 20 Std./Woche: zählen als 0.5
- Auszubildende: zählen **nicht** (§ 23 Abs. 1 Satz 2 KSchG)
- Leitende Angestellte (§ 5 Abs. 3 BetrVG): zählen nicht für BetrVG, aber für KSchG ja

**Beispielrechnung:**
```
8 Vollzeitkräfte = 8.0
3 Halbtagskräfte (≤ 20 Std.) = 1.5
Gesamt = 9.5 → KSchG gilt NICHT (Grenze > 10 nicht überschritten)
```

**Maßgeblicher Zeitpunkt:** Regelmäßige Beschäftigtenzahl im Jahresdurchschnitt, nicht Stichtag.

### Schritt 3: Betrieb oder Unternehmen?

KSchG-Geltungsbereich ist der **Betrieb** (nicht das Gesamtunternehmen). Ein Unternehmen kann mehrere Betriebe haben. Jeder Betrieb wird separat bewertet.

### Schritt 4: Sonderkündigungsschutz prüfen (immer!)

Unabhängig von KSchG-Anwendbarkeit bestehen Sonderkündigungsschutz-Mechanismen:

| Schutztatbestand | Norm | Auch im Kleinbetrieb? |
|---|---|---|
| Schwangerschaft / Mutterschutz | § 17 MuSchG | JA |
| Elternzeit | § 18 BEEG | JA |
| Schwerbehinderung | § 168 SGB IX | JA |
| Betriebsratsmitglied | § 15 KSchG | JA |
| HinSchG-Meldung | § 33 HinSchG | JA |

### Schritt 5: Allgemeiner Kündigungsschutz § 242 BGB

Bei Nichtanwendbarkeit des KSchG: Kündigung muss trotzdem Grundsätze von Treu und Glauben wahren. Angriffspunkte:
- Diskriminierung (§§ 1-7 AGG)
- Sittenwidrigkeit (§ 138 BGB)
- Verstoss gegen Art. 12 GG (grundkündigungsschutz im Kleinbetrieb)

## Ergebnistabelle

| Kriterium | Ergebnis | KSchG anwendbar? |
|---|---|---|
| Wartezeit < 6 Monate | Nicht erfüllt | Nein |
| Betrieb ≤ 10 AN (gewichtet) | Nicht erfüllt | Nein |
| Beides erfüllt | Erfüllt | Ja |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 2. `entfristung-elektronische-signatur-vorsicht`

**Fokus:** Elektronische Signaturen und Befristungsabreden: einfache Signatur, Scan und fortgeschrittene Signatur genuegen nicht; echte qualifizierte elektronische Signatur nach § 126a BGB kann die Schriftform ersetzen. Prüft DocuSign Adobe Sign HelloSign Zertifikate, beide Parteien, Timing, Zugang und Rechtsfolge § 16 Satz 1 TzBfG.

# Vorsicht: Elektronische Signaturen bei Befristungsabreden

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorsicht: Elektronische Signaturen bei Befristungsabreden` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

In der Praxis werden Arbeitsverträge immer häufiger digital unterzeichnet. Dieser Skill trennt sauber zwischen Scan/einfacher Signatur, fortgeschrittener elektronischer Signatur und echter qualifizierter elektronischer Signatur (QES). Gerade bei Befristungen ist diese Unterscheidung prozessentscheidend.

## Zentrale Normen

- **§ 14 Abs. 4 TzBfG** — Schriftformerfordernis für Befristungsabreden
- **§ 126 BGB** — gesetzliche Schriftform; § 126 Abs. 3 BGB erlaubt Ersatz durch elektronische Form, wenn das Gesetz nichts anderes bestimmt
- **§ 126a BGB** — elektronische Form durch qualifizierte elektronische Signatur
- **§ 16 S. 1 TzBfG** — Rechtsfolge unwirksamer Befristung: Vertrag gilt als unbefristet
- **§ 17 TzBfG** — Klagefrist 3 Wochen ab vereinbartem Vertragsende (absolute Ausschlussfrist!)

## Das Problem

§ 14 Abs. 4 TzBfG verlangt für Befristungsabreden Schriftform. Ein Scan, eine eingefügte Bildunterschrift, ein Klick im Portal oder eine fortgeschrittene elektronische Signatur ersetzt diese Form nicht.

**Das bedeutet:** Eine echte QES nach § 126a BGB kann die gesetzliche Schriftform grundsätzlich ersetzen. Sie muss aber wirklich qualifiziert sein, von beiden Parteien in der richtigen Form angebracht werden und rechtzeitig vor Vertragsbeginn zugehen. Wenn nur ein Scan oder eine einfache/fortgeschrittene Signatur vorliegt, ist die Befristungsabrede regelmäßig formunwirksam; Rechtsfolge: § 16 Satz 1 TzBfG — der Vertrag gilt als unbefristet.

## Rechtsprechung und Dogmatik

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wie erkenne ich eine elektronische Signatur?

**Typische Merkmale eines digital unterzeichneten Vertrags:**

1. **Plattform-Hinweise im Dokument:**
 - "This document was signed via DocuSign"
 - "Powered by Adobe Acrobat Sign"
 - "Signiert mit HelloSign / Dropbox Sign"
 - Signatur-ID oder Zertifikat am Ende des Dokuments

2. **Unterschrift-Optik:**
 - Maschinenschriftliche oder stilisierte Unterschrift
 - Unterschrift in anderem Font als handschriftlich
 - Farbige Signatur-Felder (DocuSign-typisch: blaue Kästchen)

3. **Empfang:**
 - Vertrag per E-Mail erhalten und "online unterschrieben"
 - Per Link in Browser-Portal unterzeichnet
 - E-Mail mit "Dokument ist unterschrieben"-Zertifikat erhalten

4. **Kein physisches Original:**
 - Nie eine Originalurkunde mit echter Tinte erhalten
 - Vertrag liegt nur als PDF vor

## Unterschied: Einfache vs. qualifizierte elektronische Signatur

| Signaturtyp | Sicherheitsniveau | Genuegt für § 14 Abs. 4 TzBfG? |
|---|---|---|
| Einfache (eingescannte Unterschrift, Klick) | Niedrig | Nein |
| Fortgeschrittene (kryptographisch, ohne Zertifikat) | Mittel | Nein |
| Qualifizierte (mit qualifiziertem Zertifikat, z.B. eID) | Hoch | Ja, wenn beide Erklärungen § 126a BGB erfüllen und rechtzeitig zugehen |
| Eigenhändige Unterschrift auf Papier | Höchste (gesetzliche Schriftform) | Ja |

## Prüfschritte im Entfristungsworkflow

1. Wie wurde der Arbeitsvertrag übermittelt? (E-Mail, Portal, Papier)
2. Liegt eine Originalurkunde mit Tintensignatur vor?
3. Falls digital: liegt ein QES-Zertifikat beider Parteien vor oder nur eine einfache/fortgeschrittene Signatur?
4. Haben beide Parteien dasselbe Dokument oder jeweils die für die andere Seite bestimmte Ausfertigung wirksam unterzeichnet?
5. War der Vertrag vor Arbeitsaufnahme unterzeichnet und zugegangen?
6. Gibt es Verlängerungsabreden? — Auch diese müssen formwirksam sein.
7. Drohende 3-Wochen-Frist § 17 TzBfG: Wann endet der Vertrag laut Urkunde?

## Fazit

Ein professionell aussehender Signaturvorgang genügt nicht automatisch. Entscheidend ist, ob wirklich eine QES nach § 126a BGB vorliegt. Ohne QES oder Papieroriginal ist die Befristungsabrede regelmäßig unwirksam; mit echter QES ist sie nicht allein wegen der elektronischen Form angreifbar.

**Praxishinweis:** Viele Arbeitgeber nutzen Portale, deren Standard-Signatur nur einfach oder fortgeschritten ist. Nicht der Markenname der Plattform entscheidet, sondern das konkrete Zertifikat, die Signaturstufe, die Identifizierung und der rechtzeitige Zugang.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `entfristung-grundwarnung-drei-wochen-frist`

**Fokus:** Grundwarnung Entfristungsklage: § 17 TzBfG drei Wochen ab vereinbartem Vertragsende; absolute Ausschlussfrist; § 17 Satz 2 TzBfG i.V.m. § 7 KSchG Fiktion Wirksamkeit der Befristung bei Fristversaeumnis; Fristberechnung; nachtraegliche Zulassung.

# Grundwarnung: Dreiwochenfrist § 17 TzBfG

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundwarnung: Dreiwochenfrist § 17 TzBfG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Die Dreiwochenfrist des § 17 TzBfG ist die wichtigste und gefährlichste Frist im Entfristungsrecht. Sie läuft auch wenn man keinen Anwalt hat, auch wenn man noch weiterbeschäftigt wird, und auch wenn man von der Frist nichts weiß.

## Zentrale Normen

- § 17 TzBfG — Klagefrist 3 Wochen ab vereinbartem Vertragsende
- § 7 KSchG (analog) — Fiktionswirkung bei Fristversäumnis (Befristung gilt als wirksam)
- § 5 KSchG (analog) — Nachträgliche Zulassung bei unverschuldeter Versäumnis
- §§ 187, 188 BGB — Fristberechnung
- § 193 BGB — Verlängerung bei Wochenende/Feiertag
- § 15 Abs. 5 TzBfG — Unbefristetes Arbeitsverhältnis bei Weiterbeschäftigung ohne Widerspruch

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Die Norm — § 17 TzBfG (vollständig)

> **Satz 1:** Will der Arbeitnehmer geltend machen, dass die Befristung eines Arbeitsvertrags rechtsunwirksam ist, so muss er innerhalb von drei Wochen nach dem vereinbarten Ende des befristeten Arbeitsvertrags Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis auf Grund der Befristung nicht beendet ist.
>
> **Satz 2:** Die §§ 5 bis 7 des Kündigungsschutzgesetzes gelten entsprechend.

## Schritt-für-Schritt-Prüfung der Frist

### Schritt 1: Fristbeginn bestimmen

Die Frist beginnt mit dem **vereinbarten** Ende des Arbeitsvertrags (laut Vertragsurkunde), nicht dem tatsächlichen Ende.

**Fristbeginn-Entscheidungsbaum:**
```
Vertrag sagt: "befristet bis 31.03.2025"
→ Fristbeginn: 01.04.2025 (§ 187 Abs. 1 BGB — Anfangstag zählt nicht)
→ Fristende: 22.04.2025 um 24:00 Uhr (3 × 7 Tage = 21 Tage, §§ 188 Abs. 2, 187 Abs. 1 BGB)
→ Fällt 22.04.2025 auf Samstag/Sonntag/Feiertag: nächster Werktag (§ 193 BGB)
```

**Besonderheit Weiterbeschäftigung:**
Arbeitnehmer wird nach dem 31.03.2025 noch weiterbeschäftigt → Frist läuft trotzdem ab 01.04.2025. Weiterbeschäftigung hemmt den Fristlauf NICHT.

### Schritt 2: Fristende berechnen

```
Fristende = Vereinbartes Vertragsende + 1 Tag (§ 187 Abs. 1 BGB) + 21 Tage

Beispiel:
 Vereinbartes Ende: 31.03.2025
 Fristbeginn: 01.04.2025
 Fristende: 21.04.2025 (Montag) → letzter Tag für Klageeingang beim ArbG
```

### Schritt 3: Versäumnis feststellen?

**Ist die Frist bereits abgelaufen?**
- Ja → § 7 KSchG analog: Befristung gilt als wirksam. Nur noch nachträgliche Zulassung (§ 5 KSchG) möglich.
- Nein → Sofort Klage erheben (Skill: `entfristung-klageschrift-laie-baustein` oder `entfristung-klageschrift-anwalt-baustein`)

### Schritt 4: Nachträgliche Zulassung prüfen (§ 5 KSchG analog)

Falls Frist versäumt:
- War die Versäumnis unverschuldet? (z.B. schwere Krankheit, Naturkatastrophe, fehlerhafter Behördenrat)
- Frist für Zulassungsantrag: 2 Wochen nach Wegfall des Hindernisses
- Antrag gleichzeitig mit der Klage einreichen
- Prüfungsmaßstab: streng — bloße Rechtsunkenntnis genügt nicht

## Entscheidungsbaum

```
Ist Frist noch nicht abgelaufen?
├── Ja → Klage sofort einreichen → entfristung-klageschrift-laie/anwalt-baustein
└── Nein → War Versäumnis unverschuldet?
 ├── Ja → Antrag auf nachträgliche Zulassung (§ 5 KSchG) + Klage gleichzeitig
 └── Nein → Befristung gilt als wirksam (§ 7 KSchG) — kein Rechtsmittel mehr
```

## Sofortprüfungs-Checkliste (Abfrage an Nutzer)

1. Wann endet der Vertrag laut Vertragsurkunde? (Datum exakt)
2. Ist dieses Datum bereits abgelaufen?
3. Falls abgelaufen: seit wie vielen Tagen?
4. Wurde Klage bereits erhoben?
5. Wird der Arbeitnehmer noch weiterbeschäftigt?

## Besonderheit: Mehrere Befristungen

Bei aufeinanderfolgenden befristeten Verträgen:
- Jeder Vertrag hat seine eigene Frist
- Die Frist beginnt mit dem Ende des **jeweils letzten Vertrags**
- Frühere Verträge können nach Fristablauf nicht mehr angegriffen werden
- **Konsequenz:** Bei mehrfacher Verlängerung läuft die Frist nur beim letzten Vertrag

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 4. `entfristung-guetetermin-und-kammertermin-sprechzettel`

**Fokus:** Sprechzettel für Guetetermin und Kammertermin in der Entfristungsklage: Antragsstellung; Kernargumente Schriftformmangel und Sachgrundmangel; Vergleichsstrategie; Vorbereitung Zeugenvernehmung; Verhandlungsposition; Normen § 54 und § 57 ArbGG.

# Gütetermin und Kammertermin: Sprechzettel Entfristungsklage

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gütetermin und Kammertermin: Sprechzettel Entfristungsklage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor der Verhandlungsvorbereitung

1. Gütetermin (§ 54 ArbGG) oder Kammertermin (§ 57 ArbGG)?
2. Welcher Unwirksamkeitsgrund wird verfolgt? (Schriftformmangel / kein Sachgrund / Vorbeschäftigungsverbot)
3. Ist ein Weiterbeschäftigungsantrag gestellt?
4. Vergleichsbereitschaft des Mandanten — welche Untergrenze bei Abfindung?
5. Liegt ein Vergleichsangebot der Gegenseite vor?

## Zentrale Normen

- § 54 ArbGG — Gütetermin (Vorsitzender allein, kein Urteil möglich)
- § 57 ArbGG — Kammertermin (Vollbesetzung, Urteil möglich)
- § 17 TzBfG — Klagefrist als formale Zulässigkeitsvoraussetzung
- §§ 14 Abs. 4, 16 TzBfG — Schriftformmangel und Rechtsfolge
- § 14 Abs. 1 TzBfG — Sachgrundprüfung
- §§ 9, 10 KSchG i.V.m. § 17 Satz 2 TzBfG — Auflösungsantrag auf Abfindung
- § 12a ArbGG — Kein Kostenerstattungsanspruch für Rechtsanwalt in erster Instanz

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Gütetermin (§ 54 ArbGG)

**Was passiert:** Erster Termin vor dem Vorsitzenden allein. Ziel: gütliche Einigung. Kein Urteil möglich.

### Einstieg (wenn Richter nach dem Sachverhalt fragt)
"Ich begehre die Feststellung, dass mein Arbeitsverhältnis nicht durch die Befristung im Vertrag vom [DATUM] zum [VEREINBARTES ENDE] beendet wurde. Die Befristung ist unwirksam, weil [HAUPTGRUND: z.B.: der Vertrag wurde über DocuSign digital unterzeichnet — die Schriftform nach § 14 Abs. 4 TzBfG ist damit nicht gewahrt]."

### Bei Rückfragen zur Vertragsunterzeichnung
"Ich erhielt den Vertrag per E-Mail / über das Online-Portal [NAME]. Ich habe ihn dort elektronisch unterschrieben. Eine Originalurkunde mit eigenhändiger Unterschrift habe ich nie erhalten."

### Wenn Richter auf Vergleich drängt
**Strategie:**
1. Nicht sofort ablehnen — Erstvorschlag der Gegenseite erfragen
2. Zahlen nicht spontan nennen — "Ich benötige kurz Bedenkzeit, bevor ich ein konkretes Angebot mache"
3. Orientierung: 0.5 bis 1 Bruttomonatsverdienst pro Beschäftigungsjahr (analog KüSchK-Faustformel) + evtl. Aufschlag für starken Schriftformmangel-Fall
4. Vergleich niemals unter Druck im Gütetermin unterschreiben — Checkliste `entfristung-vergleichsverhandlung-checkliste` durchgehen
5. Befristungs-Prüfung: Vergleich enthält Beendigungsdatum? Dann Sperrzeit-Risiko bei der Arbeitsagentur prüfen (§ 159 SGB III)

## Kammertermin (§ 57 ArbGG)

### Antragstellung (wenn Richter nach Anträgen fragt)
"Ich halte meine Klageanträge vollumfänglich aufrecht. Ich beantrage:
1. Festzustellen, dass das Arbeitsverhältnis der Parteien über den [DATUM] hinaus als unbefristetes Arbeitsverhältnis fortbesteht.
2. Die Beklagte zu verurteilen, mich als [BERUFSBEZEICHNUNG] zu unveränderten Arbeitsbedingungen weiterzubeschäftigen."

### Wenn Gegenseite behauptet, Vertrag sei ordnungsgemäß unterschrieben
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Wenn Sachgrund behauptet wird
"Die Beklagte hat keinen konkreten Sachgrund nach § 14 Abs. 1 TzBfG dargelegt. Der behauptete [SACHGRUND] lag bei Vertragsschluss nicht vor / trägt die Befristungsdauer nicht. Der Arbeitgeber trägt die Darlegungs- und Beweislast für das Vorliegen des Sachgrunds."

### Wenn Gericht den Fall für schwach hält
"Selbst wenn dem Gericht der Hauptantrag zweifelhaft erscheint, weise ich auf folgende alternative Angriffspunkte hin: [HILFSANTRAG — z.B. Vorbeschäftigungsverbot / fehlende Sachgrunddarlegung / Kettenbefristung]."

## Kernargumente — Schriftformmangel (§ 14 Abs. 4 TzBfG)

1. **Norm:** § 14 Abs. 4 TzBfG: Schriftform ist konstitutive Wirksamkeitsvoraussetzung der Befristungsabrede
2. **Inhalt:** § 126 BGB: eigenhändige Unterschrift auf Urkunde; elektronische Form nur bei echter QES nach § 126a BGB
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **Rechtsfolge:** § 16 Satz 1 TzBfG: Vertrag gilt als auf unbestimmte Zeit geschlossen — automatisch, ohne gerichtliche Gestaltung

## Kernargumente — Fehlender Sachgrund (§ 14 Abs. 1 TzBfG)

1. Sachgrund muss **bei Vertragsschluss** vorgelegen haben — keine Rückwirkung
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Behaupteter Sachgrund muss **konkrete Befristungsdauer** tragen
4. Dauerbeschäftigung auf der Stelle nach Vertragsende widerlegt vorübergehenden Bedarf (§ 14 Abs. 1 Nr. 1 TzBfG)

## Praxistipps

- Alle Unterlagen mitbringen: Arbeitsvertrag (auch wenn nur als PDF), E-Mails über Vertragsschluss, Screenshots des Signier-Portals
- Bei Unklarheiten: Um Schriftsatzfrist bitten statt spontan Stellung zu nehmen (§ 56 ArbGG)
- Kein Vergleich unter Druck unterschreiben — Bedenk- und Prüfzeit erbitten
- § 12a ArbGG: In erster Instanz zahlt jede Seite ihren Anwalt selbst — kein Kostenerstattungsrisiko für Anwalt des Gegners

## Entscheidungsbaum Verhandlungsstrategie

```
Gütetermin:
├── Klarer Schriftformmangel (DocuSign/E-Mail) → Starke Position → Vergleich nur mit gutem Angebot
├── Sachgrundmangel, wenig Beweise → Mittlere Position → Vergleichsbereitschaft signalisieren
└── Fristversäumnis wurde nicht geheilt → Klage unzulässig → sofort prüfen ob Zulassungsantrag möglich

Kammertermin:
├── Beweise für elektronische Unterzeichnung vorgelegt → Schriftformmangel nachgewiesen → Urteil möglich
├── Arbeitgeber legt Originaldokument vor → Hauptangriff entfällt → Hilfsantrag Sachgrund
└── Sachgrunddarlegung lückenhaft → Beweisangebot Zeuge/Urkunde → Beweis durch Gericht
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
