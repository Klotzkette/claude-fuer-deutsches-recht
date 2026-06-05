---
name: schutzrechts-fristennotiz-ip-klausel
description: "Schutzrechts Fristennotiz IP Klausel: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schutzrechts Fristennotiz IP Klausel

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schutzrechts Fristennotiz IP Klausel** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-schutzrechts-fristennotiz-und-naechster-schritt` | Schutzrechts-Fristennotiz und nächster Schritt: Schnellerfassung aller relevanten Fristen bei einem IP-Mandat, sofortige Bewertung der Handlungsdringlichkeit und konkreter nächster Schritt für Anwalt und Mandant. |
| `ip-klausel-pruefung` | Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung exklusiv/nicht-exklusiv Gewährleistung Freistellung Reichweite. Output: IP-Klausel-Prüfbericht mit Risikokennzeichnung und Aenderungsvorschlaegen. Abgrenzung zu unterlassungsverlangen (Verletzung) und open-source-prüfung (OSS-Compliance). |
| `spezial-klausel-beweislast-und-darlegungslast` | Beweislast und Darlegungslast im gewerblichen Rechtsschutz: Wer muss was beweisen bei Marken-, Patent-, Design-, Urheber- und UWG-Verletzungen? Beweislastumkehr, sekundäre Darlegungslast, Beweiserleichterungen und praktische Konsequenzen. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **Schutzrechts Fristennotiz IP Klausel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-schutzrechts-fristennotiz-und-naechster-schritt`

**Fokus:** Schutzrechts-Fristennotiz und nächster Schritt: Schnellerfassung aller relevanten Fristen bei einem IP-Mandat, sofortige Bewertung der Handlungsdringlichkeit und konkreter nächster Schritt für Anwalt und Mandant.

# Spezial: Schutzrechts-Fristennotiz und nächster Schritt

## Zweck und Mandatsbezug

Dieser Skill erstellt eine **sofort nutzbare Fristennotiz** für ein konkretes IP-Mandat und benennt den nächsten Schritt. Er ist das schnellste Werkzeug, um bei einem neuen Mandat oder bei einer eingehenden Abmahnung sofort die zeitkritische Lage zu erfassen und nichts zu übersehen.

Mandatsbezug: Anwalt nimmt Telefonmandat an – Mandant hat Abmahnung erhalten. In fünf Minuten muss die Fristenlage klar sein. Oder: Kanzlei-Assistent soll nach Übergabe eines neuen Mandats einen Fristencheck durchführen.

## Schnellerfassung: Neun Felder

### Feld 1 – Mandat-Grunddaten

```
Mandant: _______________
Gegenseite: _______________
Verfahren: [Abmahnung / EV / Anmeldung / Widerspruch / Sonstiges]
Datum heute: _______________
Datum Eingang Mandatsunterlagen: _______________
```

### Feld 2 – Kritische Frist (sofort ermitteln)

```
Fristart: _______________
Fristauslöser (Datum): _______________
Fristdauer: _______________
Fristende: _______________
Restzeit: _______________ Tage
Konsequenz bei Versäumnis: _______________
```

### Feld 3 – Schutzrecht

```
Art: [Marke / Patent / Design / Urheberrecht / UWG / GeschGehG]
Register: [DPMA / EUIPO / EPA / Keine Eintragung]
Registernummer: _______________
Status: [Eingetragen / Angemeldet / Abgelaufen / Streitig]
Inhaberschaft: [Mandant / Lizenznehmer mit Klagerecht / Dritter]
Laufzeit: _______________
```

### Feld 4 – Verletzungssachverhalt

```
Verletzungshandlung: _______________
Datum der Verletzung: _______________
Datum der Erstkenntnis: _______________
Belege vorhanden: [Screenshot / Kaufbeleg / Zeuge / Keine]
Verletzungsprodukt/-dienstleistung: _______________
```

### Feld 5 – Vorhandene Unterlagen

```
Vorhanden: Fehlend:
[ ] Schutzrechtsurkunde [ ] Registerauszug
[ ] Vollmacht [ ] Eidesstattliche Versicherung
[ ] Abmahnschreiben [ ] Verletzungsbeleg
[ ] Korrespondenz [ ] Weitere Anlagen
```

### Feld 6 – Verfahrensstand

```
Aktuelle Stufe:
[ ] Vor Abmahnung
[ ] Abmahnung versandt / empfangen (Datum: _______)
[ ] EV beantragt (Datum: _______) / erlassen (Datum: _______)
[ ] EV vollzogen (Datum: _______)
[ ] Widerspruch (Datum: _______)
[ ] Hauptsacheklage (Datum: _______)
[ ] Vergleichsverhandlungen laufen
```

### Feld 7 – Risikoampel

```
Dringlichkeit: [ ] Sofort handeln [ ] Diese Woche [ ] Keine Eile
Schutzrecht: [ ] Stark [ ] Mittel [ ] Schwach / Streitig
Verletzung: [ ] Eindeutig [ ] Plausibel [ ] Zweifelhaft
Gesamtrisiko: [ ] Grün [ ] Gelb [ ] Rot
```

### Feld 8 – Nächster Schritt

```
Was: _______________
Bis wann: _______________
Verantwortlich: _______________
Abhängig von: _______________ (z.B. Mandantenentscheidung / fehlende Unterlagen)
```

### Feld 9 – Folge-Fristen

```
| Frist | Auslöser | Fristende | Verantwortlich |
|---|---|---|---|
| _______ | _______ | _______ | _______ |
| _______ | _______ | _______ | _______ |
| _______ | _______ | _______ | _______ |
```

## Anwendungsbeispiele

### Beispiel A: Abmahnung empfangen

```
Fristart: Reaktionsfrist auf Abmahnung
Fristauslöser: Zugang Abmahnung 01.03.2025
Fristdauer: 14 Tage (gesetzt)
Fristende: 15.03.2025
Restzeit: 12 Tage
Konsequenz: Abmahner beantragt EV ohne weitere Ankündigung

Nächster Schritt:
Was: Abmahnung prüfen, Entscheidungsvorlage für Mandanten erstellen
Bis wann: 04.03.2025 (3 Tage)
Abhängig von: Vollständige Abmahnunterlagen von Mandant
```

### Beispiel B: EV erlassen

```
Fristart: Vollziehungsfrist § 929 Abs. 2 ZPO
Fristauslöser: Zustellung EV an Antragsteller 01.03.2025
Fristdauer: 1 Monat
Fristende: 01.04.2025
Restzeit: 30 Tage
Konsequenz: EV verliert Kraft; Neuantrag erforderlich

Nächster Schritt:
Was: Vollstreckbare Ausfertigung beantragen; GV-Auftrag erteilen
Bis wann: 05.03.2025
Verantwortlich: Anwalt + Kanzlei-Assistent
```

### Beispiel C: DPMA-Widerspruch

```
Fristart: Widerspruchsfrist § 42 MarkenG
Fristauslöser: Veröffentlichung der Marke im Markenblatt 01.02.2025
Fristdauer: 3 Monate
Fristende: 01.05.2025
Restzeit: 59 Tage
Konsequenz: Keine Wiedereinsetzung; Widerspruch endgültig versäumt

Nächster Schritt:
Was: Widerspruchsschrift vorbereiten; Benutzungsnachweis ältere Marke zusammenstellen
Bis wann: 15.04.2025 (Puffer von 2 Wochen vor Fristende)
```

## Fristennotiz-Erstellung: Workflow

1. Mandatsdaten eintragen (5 Minuten).
2. Kritische Frist sofort berechnen und ins Fristenbuch eintragen.
3. Fehlende Unterlagen identifizieren und Mandant anfordern.
4. Nächsten Schritt definieren und verantwortliche Person benennen.
5. Mandanteninfo: Kurze E-Mail mit Fristennotiz als Anlage.

## Quellenregel

- [§ 929 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/929.html)
- [§ 42 MarkenG – dejure.org](https://dejure.org/gesetze/MarkenG/42.html)
- [§ 59 PatG – dejure.org](https://dejure.org/gesetze/PatG/59.html)
- Fristen immer über offizielle Quellen bestätigen; keine Pauschalangaben aus Modellwissen.

## Anschluss-Skills

- `spezial-fristen-abschlussprodukt-und-uebergabe` – Fristenmatrix vollständig
- `workflow-fristen-und-risikoampel` – Fristen
- `spezial-compliance-mandantenkommunikation-entscheidungsvorlage` – Mandanteninfo
- `workflow-dokumentenintake` – Dokumentenerfassung

## 2. `ip-klausel-pruefung`

**Fokus:** Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung exklusiv/nicht-exklusiv Gewährleistung Freistellung Reichweite. Output: IP-Klausel-Prüfbericht mit Risikokennzeichnung und Aenderungsvorschlaegen. Abgrenzung zu unterlassungsverlangen (Verletzung) und open-source-prüfung (OSS-Compliance).

# IP-Klausel-Prüfung

## Zweck

Diese Skill liest die IP-Klauseln eines Vertrags und gibt dem Rechtsanwalt für jede Klausel eine strukturierte Auswertung: Was steht drin, wie weicht es von der Marktpraxis oder der Hausposition ab, welches Risiko besteht, und — wo angebracht — welcher konkrete Änderungsvorschlag greift. Das Ziel ist ein Vermerk, der in einem Durchgang handlungsfähig macht.

Die wichtigsten IP-Klauseln in den meisten Verträgen sind Rechteeinräumung und Inhaberschaft. Fehler hier sind schwer zu korrigieren. Eine fehlende oder unklare Rechteübertragung taucht später in Due-Diligence-Prozessen, Finanzierungsrunden und Rechtsstreitigkeiten auf.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

- **Vertragsdokument:** Dateilink, eingefügter Text oder Beschreibung.
- **Vertragstyp:** Arbeitsvertrag, Dienstvertrag (freier Mitarbeiter), Werkvertrag/SOW, Lizenzvertrag (ein- oder ausgehend), Kooperationsvertrag, MSA, M&A-Nebenabrede, sonstige.
- **Position des Mandanten:** Rechtegebend (Lizenzgeber / Übertrager) oder Rechteempfangend (Lizenznehmer / Erwerber) oder beides.
- **Rechtsordnung des Vertrags:** Welches Recht ist vereinbart?

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 11–24 UrhG** — Urheberpersönlichkeitsrechte (unveräußerlich; § 14 UrhG Entstellungsschutz)
- **§ 29 UrhG** — Urheberrecht ist nicht übertragbar; nur Einräumung von Nutzungsrechten (§§ 31 ff. UrhG) möglich
- **§§ 31–44 UrhG** — Einräumung von Nutzungsrechten: einfaches vs. ausschließliches Nutzungsrecht (§ 31 Abs. 1), Übertragung von Nutzungsrechten (§ 34), Unterlizenzen (§ 35), Zweckübertragungslehre (§ 31 Abs. 5)
- **§§ 43, 69b UrhG** — Urheberrecht an Computerprogrammen bei Arbeitsverhältnissen: Nutzungsrechte beim Arbeitgeber kraft Gesetzes (§ 69b Abs. 1)
- **§§ 15–22 PatG** — Übertragung und Lizenzierung von Patenten; Vindikationsanspruch; Miterfinderschaft
- **§§ 27–31 MarkenG** — Übertragung und Lizenzierung von Marken
- **§§ 1–4 GeschGehG** — Geschäftsgeheimnis: Voraussetzungen, angemessene Schutzmaßnahmen
- **§§ 4, 5 ArbnErfG** — Zuordnung von Arbeitnehmererfindungen (Patent-/Gebrauchsmusterrechte beim Arbeitgeber nach Inanspruchnahme)
- **§§ 433 ff., 311, 280 BGB** — Gewährleistungs- und Haftungsregelungen bei Rechtsmängeln

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Leistner, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 31 Rn. 1 (Nutzungsrechte, Übertragbarkeit)
- Spindler, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 29 Rn. 1 (Nicht-Übertragbarkeit des Urheberrechts)
- Melullis, in: Benkard, PatG, 12. Aufl. 2023, § 15 Rn. 1 (Patentübertragung und -lizenz)
- Ingerl/Rohnke, MarkenG, 3. Aufl. 2010, § 27 Rn. 1 (Markenübertragung – Doppelautoren-Kommentar)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Orientierung

Vertrag einmal vollständig lesen. Antworten auf folgende Fragen:

| Frage | Antwort |
|---|---|
| Vertragstyp? | Arbeitsvertrag / Dienstvertrag / Werkvertrag-SOW / Lizenzvertrag ein- oder ausgehend / Kooperation / Sonstiges |
| Position des Mandanten bei IP? | Rechtegebend / -empfangend / beides |
| Vertragspartner? | Name und Einschätzung — Einzelperson, Startup, Großunternehmen |
| Steht Vergütung für IP gesondert? | Arbeitsentgelt, Werkhonorar, Lizenzgebühr, Vorauszahlung, keine |
| Anwendbares Recht? | Welche Rechtsordnung; ist das Mandatsprofil betroffen? |

Bei Unklarheit über die IP-Position (Kooperationsvertrag, beidseitige Rechteeinräumung): nachfragen.

### Schritt 2: Prüfung der Rechteübertragungsklauseln (höchste Priorität)

Bei Arbeitsverträgen, Dienstverträgen und Werkverträgen, wo der Mandant IP des Vertragspartners erwerben soll, zunächst folgende Punkte prüfen:

**A — Urheber- und Leistungsschutzrechte:**
- § 29 UrhG: Urheberrecht ist nicht übertragbar. Möglich ist nur die Einräumung von Nutzungsrechten (§§ 31 ff. UrhG). Eine Klausel, die "das Urheberrecht überträgt", ist rechtlich ungenau und erreicht das Ziel nicht.
- § 31 Abs. 1 UrhG: Unterschied zwischen einfachem (nicht ausschließlichem) und ausschließlichem Nutzungsrecht — ausschließliches Nutzungsrecht erlaubt Klage auf eigenem Namen, einfaches nicht.
- § 31 Abs. 5 UrhG (Zweckübertragungslehre): Im Zweifel werden nur für den Vertragszweck unbedingt erforderliche Rechte eingeräumt. Umfang muss explizit definiert sein.
- Urheberpersönlichkeitsrechte (§§ 12–14 UrhG) sind unveräußerlich; lediglich Verzichtserklärungen oder Nichtausübungsabreden (im Rahmen des § 138 BGB) möglich.

**B — Patente und Gebrauchsmuster:**
- Bei Arbeitnehmern: Nutzungsrechte entstehen nach Inanspruchnahme gemäß § 6 ArbnErfG beim Arbeitgeber automatisch.
- Bei freien Mitarbeitern: Ausdrückliche schriftliche Abtretung (§ 15 PatG) erforderlich. Zukunftsbezogene Abtretungsklauseln (noch nicht entstandene Patente) sind zulässig.

**C — Klauselsprache prüfen:**
- Aktuelle Einräumung: "räumt hiermit ein" ist stärker als "verpflichtet sich einzuräumen" (Leistungspflicht vs. dingliche Wirkung)
- Umfang: Alle für die Leistung relevanten Nutzungsarten einschließlich unbekannter Nutzungsarten (§ 31a UrhG) — explizit regeln, wenn gewollt
- Unterlizenzen: Klausel für die Berechtigung zur Unterlizenzierung (§ 35 UrhG) prüfen
- Vorbestehende IP: Welche Rechte des Auftragnehmers sind explizit ausgenommen?

Wenn wesentliche Punkte fehlen oder unklar sind: am Anfang des Vermerks mit 🔴 oder 🟠 kennzeichnen und Änderungsvorschlag beifügen.

### Schritt 3: Klausel-für-Klausel-Prüfung

Für jede IP-relevante Klausel einen Prüfblock erstellen:

```markdown
### [Abschnitt X.X]: [Klauselbezeichnung]

**Was sie sagt:** [Zusammenfassung in eigenen Worten, ein bis zwei Sätze]

**Marktstandard (für diesen Vertragstyp, diese Position, dieses Recht):**
[kurze Referenz]

**Risiko:** 🔴 Kritisch | 🟠 Hoch | 🟡 Mittel | 🟢 Niedrig

**Warum es darauf ankommt:** [ein bis zwei Sätze — was schief geht, wenn die Klausel so bleibt]

**Änderungsvorschlag (soweit erforderlich):**
> "[konkrete Ersatzformulierung]"

**Entscheidungsvorbehalt:** [Bei subjektiven Zuordnungsfragen: anwaltliche Prüfung empfehlen, Argumente pro/contra aufzeigen]
```

Zu prüfende Klauseltypen:

- **Rechteeinräumung / Urheberrechtsklausel** — Wer bekommt welche Nutzungsrechte?
- **Eigentumsklausel an Arbeitsergebnissen** — Abgrenzung Diensterfindung / freie Erfindung / Werk
- **Verbesserungen und Ableitungen** — Wer gehört Verbesserungen an vorbestehendem IP? Wer derivate Werke?
- **Hintergrund-IP vs. Vordergrund-IP** — Ist vorbestehendes IP klar definiert und für den Vertragszweck lizenziert?
- **Lizenzgewährungen** — Umfang, Ausschließlichkeit, Territorium, Verwendungszweck (field of use), Sublizenzierbarkeit, Laufzeit, Kündigungsgründe, Vergütung
- **IP-Gewährleistungen** — Nichtverstoß gegen Drittrechte, Verfügungsberechtigung, Originalität des Werkes
- **IP-Freistellungen** — Umfang, Cap, Verfahren, Ausschlüsse (Modifikationen durch den anderen Teil, ungenehmigte Nutzungen)
- **Open-Source-Erklärungen** — Angaben zu eingebetteten OSS-Komponenten; GPL/LGPL/AGPL-Risiken
- **Marken** — Nutzungsrechte an Marken des anderen Teils, Qualitätskontrolle bei Lizenzen (§ 30 Abs. 2 MarkenG)
- **Geschäftsgeheimnisse** — Behandlung von GeschGehG-Material, angemessene Schutzmaßnahmen (§ 2 Nr. 1 lit. b GeschGehG), Rückgabe nach Vertragsende

**Schweregrad-Kalibrierung:**

| Stufe | Bedeutung |
|---|---|
| 🔴 Kritisch | Nicht unterzeichnen ohne Korrektur. Fehlende Rechteeinräumung wo sie erforderlich ist. Unbeschränkte Lizenz wo beschränkte gewollt ist. Exklusive Einräumung wo nicht exklusiv gewollt. |
| 🟠 Hoch | Stark nachverhandeln; eskalieren wenn keine Bewegung. Unklarer Umfang, fehlendes Urheberpersönlichkeitsrecht-Waiver, fehlende further-assurance-Klausel. |
| 🟡 Mittel | Im ersten Durchgang pushen; akzeptieren wenn letzter offener Punkt. Sprachlich ungenau, Überlebenszeitraum kürzer als Standard. |
| 🟢 Niedrig | Vermerken, kein Kapital einsetzen. Stilistische Abweichung ohne inhaltliche Auswirkung. |

### Schritt 4: Klausel-übergreifende Konsistenzprüfung

IP-Klauseln scheitern als System. Prüfen:

- **Passt die Lizenzgewährung zum Umfang des lizenzierten Rechts?** (Lizenz zur "Nutzung" ist enger als Lizenz zur "Nutzung, Bearbeitung und Erstellung abgeleiteter Werke".)
- **Decken die Gewährleistungen ab, was die Lizenz umfasst?** (Gewährleistung nur für Patente bei einer Lizenz, die auch Urheberrecht und Geschäftsgeheimnisse umfasst, hinterlässt Lücken.)
- **Deckt die Freistellung was die Gewährleistung verspricht?** (Gewährleistung ohne Freistellung ist ein Versprechen ohne Rechtsbehelf.)
- **Zieht Kündigung die Lizenz zurück?** (Oder überlebt eine bezahlte Lizenz die Kündigung? Beides vertretbar — Frage ist, ob es der Absicht entspricht.)
- **Stimmt die IP-Regelung in diesem Vertrag mit verbundenen SOW, Bestellformularen oder Nebenbriefen überein?** Konflikte kennzeichnen.

### Schritt 5: Rechtsordnungshinweis

IP-Regelungen sind rechtsordnungsabhängig. Kennzeichnen wenn relevant:

- **Urheberpersönlichkeitsrechte:** In Deutschland (und EU) grundsätzlich unveräußerlich (§§ 12–14 UrhG). Nur Nichtausübungsabreden möglich. Bei grenzüberschreitenden Verträgen ist das anwendbare Recht zu klären, da ausländische Rechtsordnungen abweichende Regelungen kennen können.
- **§ 69b UrhG:** Computerprogramme: Bei Arbeitsverhältnissen Nutzungsrechte kraft Gesetzes beim Arbeitgeber — explizite Einräumung für das Sicherheitsgefühl in der Due Diligence aber sinnvoll.
- **Zweckübertragungslehre (§ 31 Abs. 5 UrhG):** Gilt im deutschen Recht automatisch; Common-Law-Jurisdiktionen kennen keine vergleichbare Restriktion.
- **KI-generierte Werke:** Nach deutschem Recht ist Schutzvoraussetzung eine menschliche Schöpfung (§ 2 Abs. 2 UrhG — persönliche geistige Schöpfung). Rein KI-generierte Werke ohne menschlichen schöpferischen Beitrag sind nicht urheberrechtsschutzfähig; eine Rechteübertragungsklausel kann nur Rechte übertragen, die bestehen. Wenn KI-Einsatz wahrscheinlich (Softwareentwicklung, Content, Design): 🟠 Hoch — KI-Nutzungsoffenbarungspflicht und Regelung über KI-Anteile empfehlen.

### Schritt 6: Vermerk zusammenstellen

Format:

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Mandatsprofil]

# IP-Klausel-Prüfung: [Vertragspartner] — [Vertragstyp]

**Geprüft:** [Datum]
**Position bei IP:** [Rechtegebend / -empfangend / beides]
**Anwendbares Recht:** [Rechtsordnung]

---

## Ergebnis

[Zwei Sätze. Hält die IP-Zuordnung stand? Was muss zuerst geändert werden?]

**Befunde:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Genehmigung erforderlich von:** [Name, gemäß Mandatsprofil]

---

## Rechteübertragungsprüfung

[✅ Unbedenklich | ⚠️ Lücke vorhanden — siehe oben]

---

## Klauseln nach Schweregrad

[Alle Klauselblöcke aus Schritt 3, gruppiert Kritisch → Niedrig]

---

## Klausel-übergreifende Konsistenz

[Befunde aus Schritt 4]

---

## Rechtsordnungshinweis

[Befunde aus Schritt 5]

---

## Weiterleitungshinweise

[Wer genehmigt; was löst automatische Eskalation aus]
```

## Ausgabeformat

Vermerk mit Arbeitsergebnis-Kopfzeile, Gesamtbewertung, Rechteübertragungsprüfung, Klauselblöcke nach Schweregrad, Konsistenzprüfung, Rechtsordnungshinweis, Weiterleitungshinweise. Änderungsvorschläge: kleinstmögliche Eingriffsgranularität (Wort vor Phrase vor Satz vor Klausel).

## Beispiel

**Eingabe:** Werkvertrag mit einem freien Softwareentwickler, der "alle Urheberrechte an den Arbeitsergebnissen überträgt".

**Befund (Auszug):**

> ### Abschnitt 5.1: Rechteübertragungsklausel
>
> **Was sie sagt:** "Der Auftragnehmer überträgt alle Urheberrechte an den Arbeitsergebnissen auf den Auftraggeber."
>
> **Marktstandard:** Einräumung ausschließlicher Nutzungsrechte in allen bekannten und unbekannten Nutzungsarten.
>
> **Risiko:** 🔴 Kritisch
>
> **Warum es darauf ankommt:** Urheberrecht ist nach § 29 UrhG nicht übertragbar. Die Klausel erreicht das angestrebte Ziel nicht. In einer Due-Diligence-Prüfung wird dies auffallen.
>
> **Änderungsvorschlag:**
> "Der Auftragnehmer räumt dem Auftraggeber hiermit das ausschließliche, räumlich, zeitlich und inhaltlich unbeschränkte Nutzungsrecht an allen im Rahmen dieses Vertrags erstellten Arbeitsergebnissen ein, einschließlich des Rechts zur Bearbeitung und Weiterübertragung sowie zur Einräumung von Unterlizenzen."

## Risiken und typische Fehler

- **§ 29 UrhG übersehen:** "Übertragung des Urheberrechts" ist deutschrechtlich unwirksam — nur Nutzungsrechtseinräumung möglich.
- **Zweckübertragungslehre nicht beachtet:** Zu eng gefasste Klauseln schränken spätere Nutzungsarten ein (z. B. keine Streaming-Rechte wenn nur "Vervielfältigung" lizenziert).
- **Urheberpersönlichkeitsrechte ignorieren:** Nichtausübungsabrede vergessen → Risiko späterer Unterlassungsansprüche des Urhebers bei Entstellungen.
- **KI-generierte Werke:** Unklar ob urheberrechtsschutzfähig; Abtretungsklausel ohne KI-Offenbarungspflicht ist Blindflug.
- **Arbeitnehmererfindungen:** Ohne formelle Inanspruchnahme nach § 6 ArbnErfG bleiben Patentrechte beim Erfinder — trotz Vertragsklausel.

## Quellenpflicht

Jede Klauselaussage muss auf eine Norm oder Entscheidung gestützt sein. Pflichtquellen:

- **Gesetze:** §§ 29, 31, 31a, 35, 69b UrhG; §§ 15, 22 PatG; § 27 MarkenG; ArbnErfG
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zur Zweckübertragungslehre oder Nutzungsrechtsreichweite
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen; keine stillen Ergänzungen aus dem Modellwissen ohne Hinweis.

## Triage-Fragen vor IP-Klausel-Pruefung

Bevor die Klauselanalyse beginnt, klaere:
1. Handelt es sich um eine Nutzungsrechtseinraeumung (§ 31 UrhG) oder eine unzulaessige "Uebertragung des Urheberrechts" (§ 29 UrhG)?
2. Sind kuenftige Nutzungsarten von der Einraeumung erfasst (§ 31a UrhG — Schriftformerfordernis, Widerrufsrecht)?
3. Besteht eine Arbeitnehmererfindungs-Komponente (§ 69b UrhG Software, ArbnErfG) die separate Regelung erfordert?
4. Ist die Zweckuebertragungslehre (§ 31 V UrhG) bei zu engen Klauseln zu beachten?

## Aktuelle Rechtsprechung

<!-- AUDIT 27.05.2026: 4 halluzinierte Leitentscheidungen geprüft und bereinigt.
Frontmatter unverändert. Kein Commit. Bearbeiter: Halluzinations-Reparatur-Pipeline. -->

## 3. `spezial-klausel-beweislast-und-darlegungslast`

**Fokus:** Beweislast und Darlegungslast im gewerblichen Rechtsschutz: Wer muss was beweisen bei Marken-, Patent-, Design-, Urheber- und UWG-Verletzungen? Beweislastumkehr, sekundäre Darlegungslast, Beweiserleichterungen und praktische Konsequenzen.

# Spezial: Klausel – Beweislast und Darlegungslast im IP-Recht

## Zweck und Mandatsbezug

Dieser Skill behandelt die **Beweislast- und Darlegungslastverteilung** im gewerblichen Rechtsschutz. Wer im IP-Verfahren muss welche Tatsachen beweisen? Wo gibt es gesetzliche Beweislastumkehrungen, sekundäre Darlegungslasten und Beweiserleichterungen? Diese Fragen sind entscheidend für die Vorbereitung von Klagen, Abwehrstrategien und Schriftsätzen.

Mandatsbezug: Anwalt fragt: Muss ich beweisen, dass der Beklagte das Patent verletzt, oder muss der Beklagte beweisen, dass er es nicht verletzt? Mandant behauptet, keine Verletzung begangen zu haben – welche Mitwirkungspflichten bestehen?

## Grundsatz der Beweislast

### Allgemeiner Grundsatz

- Grundsatz im deutschen Zivilprozessrecht: **Wer eine Tatsache für sich in Anspruch nimmt, trägt die Beweislast** (actori incumbit probatio).
- IP-Kläger trägt Beweislast für:
 1. Schutzrecht (Existenz, Inhaberschaft, Gültigkeit).
 2. Verletzungshandlung (Tatbestand, Zurechnung).
 3. Schaden (bei Schadensersatzklage).
- Beklagter trägt Beweislast für:
 1. Rechtfertigungsgründe (Erschöpfung, Lizenz, Vorbenutzungsrecht).
 2. Nichtverschulden (nur bei § 10 GeschGehG).

## Beweislast nach Rechtsgebieten

### Markenrecht

| Frage | Beweislast | Norm |
|---|---|---|
| Marke eingetragen und valide | Kläger | Registerauszug DPMA/EUIPO |
| Ähnlichkeit / Verwechslungsgefahr | Kläger | Richterliche Beurteilung; Beweismittel: Gutachten, Umfrage |
| Benutzung durch Beklagten | Kläger | Screenshot, Kaufbeleg, Zeuge |
| Erschöpfung (§ 24 MarkenG) | Beklagter | Kaufbeleg mit EU-Herkunft |
| Ernsthafte Benutzung (§ 26 MarkenG) | Markeninhaber bei Einrede | Rechnungen, Kataloge, Werbung |
| Bekanntheitsschutz (§ 14 Abs. 2 Nr. 3) | Kläger | Marktumfrage, Umsatzdaten |

**Sekundäre Darlegungslast:** Wenn Kläger plausible Darlegung liefert, muss Beklagter substantiiert widersprechen oder seine eigene Lieferkette darlegen.

### Patentrecht

| Frage | Beweislast | Norm / Norm |
|---|---|---|
| Patent eingetragen, Anspruch identifiziert | Kläger | Patentrolle, Patentschrift |
| Patentverletzung (wortsinngemäß) | Kläger | Technisches Gutachten |
| Äquivalenz-Verletzung | Kläger | Sachverständigengutachten |
| Vorbenutzungsrecht (§ 12 PatG) | Beklagter | Entwicklungsunterlagen, Zeugen |
| Zwangslizenz (§ 24 PatG) | Lizenzsucher | FRAND-Bereitschaft nachweisen |
| Nichteinhaltung ArbnErfG | Arbeitnehmer/Arbeitgeber | Meldung, Inanspruchnahmeerklärung |

**Wichtig:** BGH hat bei Patentprozessen hohe Anforderungen an technisches Gutachten; Scheingenauigkeit vermeiden. Bei äquivalenter Verletzung: Drei-Stufen-Test (BGH „Schneidmesser").

**Besonderheit Verfahrenspatent (§ 139 Abs. 3 PatG):**
- Verfahrenspatent + Herstellung gleichen Erzeugnisses → **Beweislastumkehr**: Beklagter muss beweisen, dass er ein anderes Verfahren verwendet.

### Designrecht

| Frage | Beweislast |
|---|---|
| Design eingetragen und valide | Kläger |
| Übereinstimmung / Ähnlichkeit | Richterliche Beurteilung; ggf. Gutachten |
| Neuheit / Eigenart (bei Angriff) | Angreifer (bei Nichtigkeitsklage) |
| Informierter Benutzer | Richterliche Beurteilung |

### Urheberrecht

| Frage | Beweislast |
|---|---|
| Werkqualität | Kläger; bei kreativem Werk oft offensichtlich |
| Urheberschaft | Kläger; Vermutung nach § 10 UrhG (Namensvermutung) |
| Vervielfältigung ohne Lizenz | Kläger (Zugänglichkeit + fehlende Lizenz) |
| Schöpfungshöhe (§ 2 Abs. 2 UrhG) | Kläger; besonders bei Computerprogrammen |
| Schadenshöhe (Lizenzanalogie) | Kläger; Schätzung nach § 287 ZPO |

**Besonderheit Filesharing:** BGH-Rechtsprechung zu sekundärer Darlegungslast des Anschlussinhabers (BGH „Sommer unseres Lebens"; „BearShare"); Anschlussinhaber muss Haushaltsangehörige benennen.

### UWG

| Frage | Beweislast |
|---|---|
| Mitbewerbereigenschaft | Kläger |
| Spürbarkeit | Kläger |
| Irreführung (§ 5 UWG) | Kläger; aber: Verkehrsauffassung durch Richter |
| Rechtsbruch (§ 3a UWG) | Kläger |
| Wiederholungsgefahr | Wird vermutet nach erstmaliger Verletzung |
| Erstbegehungsgefahr | Kläger |

## Beweiserleichterungen

### § 287 ZPO – Schadensschätzung

- Gericht kann Schadenshöhe schätzen.
- Anwendung im IP-Recht bei Lizenzanalogie: Kläger muss nur Grundlage liefern; Höhe schätzt Gericht.
- BGH: Schätzung auch bei dürftiger Tatsachengrundlage zulässig.

### Anscheinsbeweis (prima facie)

- Bei typischen Geschehensabläufen: Beweis durch Lebenserfahrung.
- Z.B.: Patent verletzt, Beklagter vertreibt technisch identisches Produkt → Anschein der Verletzung.

### Sekundäre Darlegungslast

- Wenn Kläger Tatsachen aus Sphäre des Beklagten darlegen muss, die ihm nicht zugänglich sind.
- Beklagter muss dann substantiiert widersprechen.
- Beispiel: Lieferkette, interne Prozesse, Produktionsverfahren.

## Beweismittel im IP-Recht

| Beweismittel | Typischer Einsatz | Beweiswert |
|---|---|---|
| Eidesstattliche Versicherung | EV-Verfahren (Glaubhaftmachung § 920 ZPO) | Mittel (kein Kreuzwerhör) |
| Urkunde (Registerauszug) | Schutzrecht, Priorität | Hoch |
| Zeuge | Verletzungshandlung, Erstkenntnis | Mittel |
| Sachverständigengutachten | Technische Patentverletzung; Verwechslungsgefahr | Hoch |
| Augenschein (Produkt, Screenshot) | Verletzungsprodukt | Mittel |
| Parteivernehmung | Entscheidungsfälle | Gering |
| Testkauf | UWG, Marke | Mittel-Hoch |

## Typische Beweisfallen

- **Keine eidesstattliche Versicherung:** EV-Antrag ohne Glaubhaftmachung; abgewiesen.
- **Registerauszug veraltet:** DPMA/EUIPO-Auszug > 3 Monate; Gericht akzeptiert nicht.
- **Screenshot ohne Metadaten:** Datum und URL fehlen; Beweiskraft zweifelhaft.
- **Sachverständiger ohne Fachkunde:** Gutachten wird nicht verwertet.
- **Sekundäre Darlegungslast ignoriert:** Beklagter schweigt; Gericht wertet das gegen ihn.

## Quellenregel

- [§ 139 PatG Abs. 3 – dejure.org](https://dejure.org/gesetze/PatG/139.html)
- [§ 10 UrhG – dejure.org](https://dejure.org/gesetze/UrhG/10.html)
- BGH-Rechtsprechung: [bgh.de](https://www.bundesgerichtshof.de); Entscheidungen mit Gericht, Datum, AZ.
- Keine BeckRS-Blindzitate; Rechtsprechung nur mit verifizierbarer Quelle.

## Anschluss-Skills

- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand und Beleglage
- `verletzungs-triage` – Erstentscheidung IP-Verletzung
- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag und Glaubhaftmachung
