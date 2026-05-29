---
name: ip-klausel-pruefung
description: "Anwalt prüft Vertrag auf IP-Klauseln (Übertragung Lizenz Inhaberschaft Freistellung) oder Mandant fragt nach Risiken. IP-Klauseln Vertragsrecht. Prüfraster: Übertragung Inhaberschaft Lizenzgewaehrung exklusiv/nicht-exklusiv Gewährleistung Freistellung Reichweite. Output: IP-Klausel-Prüfbericht mit Risikokennzeichnung und Aenderungsvorschlaegen. Abgrenzung zu unterlassungsverlangen (Verletzung) und open-source-prüfung (OSS-Compliance)."
---

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
