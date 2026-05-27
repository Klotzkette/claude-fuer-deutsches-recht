---
name: dd-findings-extraktion
description: "Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer Datenraum pruefen, DD-Issues extrahieren aus [Ordner], Due-Diligence-Pruefung oder was ist im VDR sagt oder auf VDR-Dokumente hinweist."
---

# DD-Issue-Extraktion (Findings-Report)

## Triage zu Beginn

Vor dem Start des DD-Reviews folgende Fragen klären:

1. **Transaktionsstruktur:** Share Deal oder Asset Deal? GmbH oder AG?
2. **Wesentlichkeitsschwelle:** Welcher Mindestvertragswert ist zu prüfen (aus Praxisprofil)?
3. **Prüfkategorien:** Welche Kategorien sind für diesen Deal relevant (Gesellschaftsrecht, IP, Arbeitsrecht, Umwelt)?
4. **VDR-Vollständigkeit:** Gibt es offensichtliche Lücken (fehlende Kategorien, Platzhalter-Dokumente)?
5. **DD-Tiefe:** Full Legal DD oder Red-Flag-Review?
6. **Zeitplan:** Wann muss der Findings-Report vorliegen (Signing-Druck)?

## Zentrale Normen

§§ 311 Abs. 2, 241 Abs. 2 BGB (vorvertragliche Aufklärungspflichten) — § 442 BGB (Kenntnis des Käufers) — § 443 BGB (Garantien) — § 15 GmbHG (Abtretung GmbH-Anteile) — § 40 GmbHG (Gesellschafterliste) — § 613a BGB (Betriebsübergang) — §§ 35 ff. GWB (Fusionskontrolle) — Art. 28 DSGVO (Auftragsverarbeitung) — §§ 142, 144 ZPO (Urkundenvorlegung)

## Aktuelle Rechtsprechung

- BGH, Urt. v. 01.03.2010 – II ZR 213/08, NJW 2010, 1808 Rn. 12 — Beim Unternehmenskauf traegt der Kaeufer grundsaetzlich das Risiko nicht offenbarter Maengel; der Verkaeufer haftet aber nach den Grundsaetzen der c.i.c., wenn er arglistig Auskunft verweigert oder falsche Auskuenfte erteilt.
- BGH, Urt. v. 06.04.2001 – V ZR 394/99, NJW 2001, 2875 Rn. 17 — Vorvertragliche Aufklaerungspflicht des Verkaefers bei Unternehmenskauf; sie besteht bei objektiv wesentlichen, fuer den Kaeufer wertbestimmenden Umstaenden, die dieser nicht selbst erkennen kann.
- BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18 — Change-of-Control-Klauseln koennen auch bei mittelbarem Kontrollwechsel ausgeloest werden; massgeblich ist die vertragliche Formulierung und nicht nur der gesellschaftsrechtliche Kontrollbegriff.
- OLG Frankfurt, Urt. v. 10.09.2020 – 26 U 35/19 — Unzureichende Offenlegung im Datenraum genuegte nicht; spaeterer Hinweis auf versteckte Dokumente heilt die Aufklaerungspflichtverletzung nicht.

## Kommentarliteratur

- Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 10 ff. (Unternehmenskauf, Gewährleistung und Due Diligence).
- Altmeppen, in: Roth/Altmeppen, GmbHG, 11. Aufl. 2023, § 15 Rn. 80 (Übertragung GmbH-Anteile, Abtretungsverbote).
- Hopt, in: Baumbach/Hopt, HGB, 41. Aufl. 2024, § 354a Rn. 1 (Abtretungsverbot zwischen Kaufleuten).

## Zweck

Der Datenraum hat 2.000 Dokumente. Irgendwo darin befinden sich die 30, die für den Deal entscheidend sind. Dieser Skill liest Dokumente gegen die DD-Kategorien und Wesentlichkeitsschwellen aus dem Praxisprofil, extrahiert Issues und schreibt sie im Hausformat.

**Vorprozessuale Beweiserhebung im deutschen Recht.** Die Due Diligence (Sorgfaltsprüfung) in deutschen M&A-Transaktionen läuft ausschließlich über den virtuellen Datenraum (VDR – Virtual Data Room), den Frage-Antwort-Prozess (Q&A) und den Disclosure Letter (Offenlegungserklärung). Was nicht offengelegt wurde, ist weder bekannt noch garantiert – das im SPA (Share Purchase Agreement, Unternehmenskaufvertrag) verankerte Garantieregime modifiziert insoweit den allgemeinen Grundsatz, dass der Käufer das Risiko nicht offenbarter Mängel trägt. Gesetzliche Auskunftsansprüche im Streitfall: §§ 142, 144 ZPO; § 810 BGB; §§ 242, 259, 666 BGB; Art. 15 DSGVO; § 254 ZPO (Stufenklage).

## Eingaben

- Praxisprofil: `## M&A → DD-Struktur` (Kategorien, Schwellen)
- Praxisprofil: `## M&A → Issues-Memo-Format`
- Mandats-Kontext: `mandate/[code]/deal-kontext.md`
- VDR-Inventar oder Dokumentenliste

## Schritt-fuer-Schritt-Workflow

### Schritt 1: VDR-Inventarisierung

Falls VDR-Connector (Box/Datasite/Intralinks) verbunden: Index abrufen. VDR-Ordner auf DD-Anforderungskategorien abbilden. Lücken notieren – Kategorien ohne VDR-Inhalt.

```markdown
## VDR-Inventar: [Deal-Code]

| Anforderungskategorie | VDR-Ordner | Dokumente | Status |
|---|---|---|---|
| Gesellschaftsrecht / Verfassung | /01-Gesellschaft | 45 | Geprüft |
| Wesentliche Verträge | /02-Verträge | 312 | In Bearbeitung |
| IP / Technologie | /03-IP | 89 | Nicht begonnen |
| Arbeitnehmer | /04-HR | 120 | Nicht begonnen |
| Rechtstreitigkeiten / Behörden | /05-Streitigkeiten | 23 | Geprüft |
```

**Lücken:** [Anforderungskategorien ohne VDR-Inhalt – Nachforderung erforderlich]

### Schritt 2: Wesentlichkeitsschwelle anwenden

Gemäß Praxisprofil und Mandats-Kontext-Schwellen. Nicht alles prüfen, wenn die Schwelle Verträge über einem bestimmten Betrag vorschreibt.

Bei Verträgen: nach angegebenem Wert oder nach Gegenparteirelevanz sortieren. Top-down prüfen bis Schwelle erreicht oder Kategorie erschöpft.

### Schritt 3: Issues extrahieren

Je gelesenes Dokument gegen den Standardkatalog für seine Kategorie prüfen:

**Gesellschaftsrecht / Verfassung:**
- Gesellschaftsvertrag / Satzung vollständig und aktuell?
- Kapitalaufbringung nachgewiesen (§§ 7, 19 GmbHG; §§ 36, 54 AktG)?
- Gesellschafterstruktur und Gesellschafterliste (§ 40 GmbHG) korrekt?
- Vinkulierungsklauseln, Vorkaufsrechte, Mitziehrechte?
- Beirat oder Gesellschafterausschuss mit eingeschränkten Rechten?
- Nachschuss-/Einziehungsklauseln (§§ 26, 34 GmbHG)?

**Wesentliche Verträge:**
- Change-of-Control-Klausel (ausgelöst durch diesen Deal? Zustimmung erforderlich?)
- Abtretungsbeschränkung (kann der Vertrag auf Käufer übergehen?)
- Exklusivität / Wettbewerbsverbot
- Kündigungsrechte wegen des Deals
- Ungewöhnliche Haftungsregelungen; AGB-Kontrolle §§ 305 ff. BGB

**IP / Technologie:**
- Eigentumsnachweis (Abtretungen von Gründern/Arbeitnehmern vorhanden? § 69b UrhG; § 4 ArbNErfG)
- Open Source im Produkt (Copyleft-Risiko? GPL/LGPL/AGPL)
- Datenschutz (Verarbeitungsverzeichnis Art. 30 DSGVO; technisch-organisatorische Maßnahmen Art. 32 DSGVO)

**Arbeitnehmer:**
- Change-of-Control-Abfindungsansprüche
- Risiko Betriebsübergang § 613a BGB (Unterrichtungspflicht; Widerspruchsrecht 1 Monat)
- Betriebsrat (§ 102 BetrVG Kündigung; § 111 BetrVG Betriebsänderung)
- Scheinselbstständigkeit (§ 611a BGB; Nachzahlungsrisiko Sozialversicherung)

**Rechtsstreitigkeiten / Behörden:**
- Anhängige Verfahren und Rückstellungen
- Behördliche Anfragen oder laufende Prüfungen
- Kartellrecht / BKartA-Verfahren

### Schritt 4: Finding formulieren

> **Quellenattribution.** Bei Verweis auf Normen, Rechtsprechung oder Behördenmaßnahmen mit entsprechendem Tag versehen: `[juris]`, `[beck-online]`, `[Westlaw DE]` bei Zitaten aus Recherchetool; `[Modellwissen — prüfen]` bei Zitaten aus Modellwissen; `[Nutzer bereitgestellt]` bei VDR- oder Deal-Team-Quellen.

Je Finding-Vorlage aus Praxisprofil:

```
Finding #N: [Titel]
Kategorie: [Anforderungskategorie]
Schweregrad: [Stufe nach Hausschema]
Dokumente: [VDR-Pfad + Dokumentenname]
Finding: [Was das Dokument aussagt und warum es relevant ist]
Empfehlung: [Preisanpassung / Einbehalt / Zustimmung erforderlich / Garantie / Vertragsabbruch]
Vollzugshandlung: [ja – Zustimmung erforderlich / nein]
```

**Schweregradeinstufung:**
- Rot **Blockierend:** Beeinflusst Deal-Wert oder -struktur.
- Orange **Hoch:** Erheblich, aber lösbar.
- Gelb **Mittel:** Klärungsbedarf; lösbar.
- Gruen **Niedrig:** Für die Akte vermerkt.

### Schritt 5: Bericht je Kategorie

Findings nach Anforderungskategorie gruppieren. Innerhalb der Kategorie nach Schweregrad sortieren.

### Schritt 6: Batch-Verarbeitung

Für große Kategorien (300 Verträge): in Chargen verarbeiten. Nach jeder Charge laufende Issues-Liste aktualisieren und blockierende Punkte sofort melden.

## Output-Template

**Adressat:** Deal-Team (Lead Counsel) — **Tonfall:** sachlich-juristisch, präzise

```
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

> Dieses Ergebnis entstammt VDR-Materialien, die vertraulich oder privilegiert
> oder beides sind. Verteilung außerhalb des Vertraulichkeitskreises kann den
> Schutz aufheben.

# DD-Issues: [DEAL-CODE] — [KATEGORIE]
Erstellt: [DATUM] | Bearbeiter: [NAME]

Geprüfte Dokumente: [N] von [M] in Kategorie
Abdeckung: [Alle | >X EUR-Schwelle | Top-N]
Findings: [N] blockierend  [N] hoch  [N] mittel  [N] niedrig

---

## Zusammenfassung

[N] blockierend · [N] hoch · [N] mittel — [das Eine, was das Deal-Team wissen muss]

---

## Finding #1: [TITEL]

Kategorie: [KATEGORIE]
Schweregrad: [STUFE]
Dokument: [VDR-PFAD/DOKUMENTENNAME]

**Sachverhalt:**
[Was das Dokument konkret aussagt]

**Rechtliche Bewertung:**
[Norm + Folge]

**Empfehlung:**
[Preisanpassung / Einbehalt / Zustimmung einholen / Garantie verlangen]

**Vollzugshandlung:** [ja/nein]

---

## Lücken

- [Anforderungspunkt ohne responsive Dokumente]
- [Referenziertes Dokument nicht im VDR]
```

## Rote Schwellen

- Change-of-Control bei wesentlichen Verträgen (Umsatzanteil >10 %) → sofortige Eskalation an Deal-Lead
- IP-Eigentumsluecke bei Kerntechnologie → blockierendes Finding; Abtretungs-Chain prüfen
- Betriebsübergang § 613a BGB ohne Unterrichtungsplan → Vollzugsverzögerung droht
- Fehlende aktuelle Gesellschafterliste (§ 40 GmbHG) → gutgläubiger Erwerb Dritter möglich
- BKartA-Verfahren oder FDI-Prüfung offen → Vollzugsverbot beachten (§ 41 GWB)

## Übergaben

- **An ki-werkzeug-uebergabe:** Bei Nutzung von Luminance/Kira massenhafte Vertragsextraktion dorthin übergeben.
- **An dealteam-zusammenfassung:** Aggregierte Findings speisen das Deal-Team-Briefing.
- **An wesentliche-vertraege-anlage:** Vertragsextraktionen speisen die Disclosure Schedule.
- **An vollzugs-checkliste:** Jedes Finding, das eine diskrete Vollzugshandlung impliziert.

## Quellen und Zitierweise

Zitierweise nach `../../references/zitierweise.md`.

Kommentarliteratur:
- Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 10 (Unternehmenskauf, Gewährleistung).
- Altmeppen, in: Roth/Altmeppen, GmbHG, 11. Aufl. 2023, § 15 Rn. 80 (Übertragung GmbH-Anteile).
- BGH, Urt. v. 01.03.2010 – II ZR 213/08, NJW 2010, 1808 Rn. 12 (Informationsasymmetrie und Risikoverteilung beim Unternehmenskauf).
- BGH, Urt. v. 06.04.2001 – V ZR 394/99, NJW 2001, 2875 Rn. 17 (Aufklärungspflicht Verkäufer beim Unternehmenskauf).

## Was dieser Skill nicht tut

- Er trifft keine Wesentlichkeitsentscheidung bei Grenzfällen. Er wendet die Schwelle an; ein Mensch entscheidet über den Grenzfall.
- Er verhandelt keine Garantien. Er erstellt die Findings, die deren Inhalt informieren.
- Er ersetzt keine KI-Massenprüfung. Für hochvolumige Klauselextraktion an ki-werkzeug-uebergabe übergeben.
