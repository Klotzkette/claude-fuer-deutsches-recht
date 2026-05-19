# CLAUDE.md – Rechtsberatungsstelle

> Konfigurationsdatei für das Plugin `rechtsberatungsstelle`. Wird von allen Skills automatisch geladen.
> Zitierweise: `../references/zitierweise.md`. Methodik: `../references/methodik-deutsches-recht.md`.

---

## Wer nutzt dieses Plugin?

<!-- Beim Einrichten per /cold-start-interview ausfüllen -->
```
Rolle:            [Anleitender Volljurist | Studierender | Verwalter]
Name:             [Name oder Pseudonym]
Beratungsstelle:  [z. B. "Refugee Law Clinic Bremen", "JuRI Köln"]
Hochschule:       [z. B. "Universität Bremen"]
Semester:         [z. B. "WS 2024/25"]
Fachbereiche:     [AsylG/AufenthG | SGB II/XII | Mietrecht | Verbraucherrecht | Familienrecht | Sonstiges]
Rechtsgrundlage:  [§ 6 II Nr. 2 RDG | § 8 RDG | Zugelassener Anwalt]
```

---

## Rollenbeschreibungen

**Anleitender Volljurist**
Zur Anleitung berechtigte Person i. S. d. § 6 Abs. 2 Nr. 2 RDG: zugelassener Rechtsanwalt, habilitierter Jurist oder in sonstiger Weise fachlich qualifizierter Volljurist. Trägt die Gesamtverantwortung für alle Mandate. Gibt Schriftsätze und Mandantenmitteilungen frei. Läuft `/cold-start-interview` und `/supervisor-review-queue`. Kann `/build-guide` und `/customize` aufrufen.

**Studierender**
Jurastudierender, der Rechtsdienstleistungen ausschließlich unentgeltlich und unter Anleitung des Volljuristen erbringt (§ 6 Abs. 2 Nr. 2 RDG). Führt Intakes durch, fertigt Entwürfe und Memos an, recherchiert – aber entscheidet nichts alleine und sendet nichts ohne Prüfung.

---

## RDG-Grenzen (verbindlich für alle Skills)

> **§ 3 RDG:** Rechtsdienstleistungen dürfen nur durch Personen erbracht werden, die zur Erbringung solcher Leistungen befugt sind.
> **§ 6 Abs. 2 Nr. 2 RDG:** Unentgeltliche Rechtsdienstleistungen durch Studierende sind zulässig, wenn sie unter Anleitung einer zur Anleitung berechtigten Person stehen.
> **§ 20 RDG:** Zuwiderhandlungen sind bußgeldbewehrt (bis zu 5.000 EUR).

**Was Studierende dürfen (§ 6 II Nr. 2 RDG):**
- Rechtliche Auskünfte im Rahmen der Beratung erteilen (unter Aufsicht)
- Schriftsatz- und Widerspruchsentwürfe anfertigen (als Entwurf, nicht zur Absendung)
- Memos und Recherchen für den Anleiter erstellen
- Intake-Gespräche führen

**Was Studierende nicht dürfen:**
- Entgeltliche Rechtsdienstleistungen erbringen
- Schriftsätze ohne Freigabe des Anleiters versenden
- Eigenständige Mandatsstrategie festlegen
- Vergleiche abschließen oder Mandate niederlegen

---

## Berufsrechtliche Pflichten (analog anwendbar)

### Verschwiegenheit
- § 43a Abs. 2 BRAO: Anwaltliche Verschwiegenheitspflicht des anleitenden Anwalts.
- § 203 Abs. 1 Nr. 3 StGB: Unbefugte Offenbarung fremder Geheimnisse durch Rechtsanwälte.
- **Für Studierende gilt § 203 Abs. 1 Nr. 3 StGB analog, da sie im Rahmen des Mandatsverhältnisses tätig werden.** Keine Weitergabe von Mandantendaten an Dritte.
- § 53 Abs. 1 Nr. 3 StPO: Zeugnisverweigerungsrecht des Anwalts schützt das Mandatsgespräch.
- DSGVO Art. 5, 9: Besondere Kategorien personenbezogener Daten (Asylstatus, Gesundheit) – erhöhte Sorgfalt.

### Interessenkonflikt
- § 43a Abs. 4 BRAO: Keine widerstreitenden Interessen. Vor jedem Intake Konfliktprüfung durchführen.
- BORA § 3: Konkretisierung des Verbots der Vertretung widerstreitender Interessen.

### Umgang mit Mandantengeld
- Durch Studierende kein Mandantengeld entgegennehmen. Nur der zugelassene Anleiter kann ein Anderkonto führen.

---

## Wichtige Normen nach Fachbereich

### Asyl- und Aufenthaltsrecht
- **AsylG:** § 1 (Anwendungsbereich), §§ 3–3e (Flüchtlingsschutz), § 4 (subsidiärer Schutz), § 60 Abs. 5, 7 (Abschiebungsverbote), § 36 (Beschleunigtes Verfahren, 1-Woche-Frist!), § 74 Abs. 1 (Klagefrist 2 Wochen bei § 36-Bescheid; sonst 2 Wochen oder 1 Monat je nach Bescheid), § 80 Abs. 5 VwGO (Eilrechtsschutz).
- **AufenthG:** § 25 (humanitäre Aufenthaltstitel), § 60a (Duldung), § 81 Abs. 3, 4 (Fiktionswirkung).
- **GFK:** Abkommen über die Rechtsstellung der Flüchtlinge v. 28.07.1951.
- **BVerwG-Rspr.:** BVerwG, Urt. v. 20.02.2020 – 1 C 1.19, BVerwGE 167, 319 (subsidiärer Schutz, Prognosestandard).
- **BAMF-Statistik:** Entscheidungsquoten nach Herkunftsland – Referenz `references/plausibilitaetsbaender/asyl.md`.

### Sozialrecht (SGB II / SGB XII / SGB IX)
- **SGB II:** § 7 (Anspruchsvoraussetzungen), § 9 (Hilfebedürftigkeit), §§ 11–11b (Einkommen), § 12 (Vermögen), § 22 (Bedarfe für Unterkunft), § 31 (Sanktionen).
- **SGB XII:** § 27 (Hilfe zum Lebensunterhalt), § 41 (Grundsicherung im Alter).
- **SGB IX:** § 76b (Eingliederungshilfe für Geflüchtete).
- **SGG:** § 84 (Widerspruchsfrist 1 Monat), § 87 (Klagefrist 1 Monat), § 86b (einstweiliger Rechtsschutz).
- **BSG-Rspr.:** BSG, Urt. v. 14.03.2018 – B 14 AS 17/17 R, BSGE 125, 210 (Sanktionsrecht); BSG, Urt. v. 18.01.2011 – B 4 AS 90/10 R, BSGE 107, 154 (Kosten der Unterkunft).
- **Plausibilitätsbänder:** `references/plausibilitaetsbaender/sozialrecht.md`.

### Mietrecht
- **BGB:** §§ 535 ff. (Mietvertrag), § 536 (Mietminderung bei Mängeln), § 543 (außerordentliche Kündigung), §§ 558–558e (Mieterhöhung bis zur ortsüblichen Vergleichsmiete), §§ 559–559b (Modernisierungsmieterhöhung), §§ 574–574b (Sozialklausel), §§ 305–310 (AGB-Kontrolle).
- **AGB-Kontrolle:** Ernst, in: MüKoBGB, 9. Aufl. 2022, §§ 305 ff. (Schönheitsreparaturen; Anfangsrenovierungsklauseln i. d. R. unwirksam nach BGH).
- **WoBindG:** Sozialwohnungen.
- **Mietspiegel:** Örtliche Mietspiegel gem. § 558c BGB – Qualifizierter Berliner Mietspiegel 2023/2024 als Referenz.
- **BGH-Rspr.:** BGH, Urt. v. 22.11.2023 – VIII ZR 77/23, NJW 2024, 430 (Mieterhöhung, Begründungsanforderungen).
- **Plausibilitätsbänder:** `references/plausibilitaetsbaender/mietrecht.md`.

### Verbraucherrecht
- **BGB §§ 305–310:** AGB-Inhaltskontrolle (MüKoBGB-Komm.).
- **BGB §§ 312 ff.:** Fernabsatz, Widerrufsrecht.
- **UKlaG, UWG:** Verbandsklage.

### Arbeitsrecht / KSchG (nur als Querschnittsthema)
- **KSchG:** § 1 (soziale Rechtfertigung), § 4 (3-Wochen-Frist Kündigungsschutzklage!), § 9 (Auflösung).
- **BGB §§ 622, 626:** Kündigungsfristen, außerordentliche Kündigung.
- **BetrVG § 102:** Anhörung des Betriebsrats.

---

## Gutachtenstil und Urteilsstil

| Dokument | Stil |
|---|---|
| Memo | Gutachtenstil (Obersatz → Definition → Subsumtion → Ergebnis) |
| Widerspruch, Klage, Schriftsatz | Urteilsstil (Ergebnis zuerst, dann Begründung) |
| Mandantenbrief | Einfache Sprache, kein Juristenjargon |
| Intake-Protokoll | Neutral-deskriptiv |

---

## Aufsichtsmodell und Freigabestufen

```
Stufe 0 – Entwurf (Studierender + KI)
  ↓ Analyse durch Studierenden
Stufe 1 – Studentischer Entwurf
  ↓ Prüfung durch anleitenden Volljuristen
Stufe 2 – Freigabe durch Anleiter
  ↓ Versand / Einreichung
Stufe 3 – Abgesandt / Eingereicht
```

**Pflichtgates:**
- Vor Einreichung eines Widerspruchs: Stufe 2.
- Vor Klageerhebung: Stufe 2 + Protokolleintrag.
- Vor Versand an Mandant: Stufe 2.
- Semesterübergabe: Stufe 2 (alle laufenden Mandate).

---

## Quellen und Kommentare

- **RDG:** Krenzler, in: Krenzler (Hrsg.), Rechtsdienstleistungsgesetz, 2. Aufl. 2021, § 6 Rn. 44 ff.
- **BRAO/BORA:** Henssler/Prütting (Hrsg.), BRAO, 5. Aufl. 2019; BORA in der jeweils gültigen Fassung.
- **BGB Mietrecht (AGB):** Wurmnest, in: MüKoBGB, 9. Aufl. 2022, §§ 305–310.
- **SGB II:** Kallert, in: Gagel, SGB II/III, Loseblatt (Stand 2024).
- **AsylG:** Bergmann/Dienelt (Hrsg.), Ausländerrecht, 14. Aufl. 2022.
- **AufenthG:** Kluth/Heusch (Hrsg.), BeckOK AuslR, 41. Ed. (Stand 01.01.2025).
- **Zitierweise:** `../references/zitierweise.md`.

---

## Verbot der Rechtsberatung über das Plugin hinaus

Dieses Plugin unterstützt die Arbeit in einer Beratungsstelle. Es ist kein eigenständiger Rechtsberatungsdienst. Personen ohne Anbindung an eine zugelassene Beratungsstelle dürfen die Ausgaben nicht als Rechtsrat verwenden.

---

## Sicherheitshinweise

- Keine personenbezogenen Mandantendaten in Prompts an Cloud-Modelle ohne datenschutzrechtliche Absicherung (DSGVO Art. 28 Auftragsverarbeitung).
- Aufbewahrungsfristen für Mandantenakten: mindestens 5 Jahre nach Mandatsende (§ 50 BRAO).
- Bei Verdacht auf Kindeswohlgefährdung oder häusliche Gewalt: Meldepflichten prüfen (§ 4 KKG, §§ 8a, 8b SGB VIII).
