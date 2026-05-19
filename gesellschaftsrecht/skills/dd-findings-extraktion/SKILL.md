---
name: dd-findings-extraktion
description: >
  Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und
  Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer
  „Datenraum prüfen", „DD-Issues extrahieren aus [Ordner]", „Due-Diligence-Prüfung",
  „was ist im VDR" sagt oder auf VDR-Dokumente hinweist.
language: de
triggers:
  - "Datenraum prüfen"
  - "DD-Issues"
  - "Due Diligence"
  - "VDR-Prüfung"
  - "Findings-Report"
  - "Datenraum-Dokumente"
---

# DD-Issue-Extraktion (Findings-Report)

## Zweck

Der Datenraum hat 2.000 Dokumente. Irgendwo darin befinden sich die 30, die für den Deal entscheidend sind. Dieser Skill liest Dokumente gegen die DD-Kategorien und Wesentlichkeitsschwellen aus dem Praxisprofil, extrahiert Issues und schreibt sie im Hausformat.

**Vorprozessuale Beweiserhebung im deutschen Recht.** Die Due Diligence (Sorgfaltsprüfung) in deutschen M&A-Transaktionen läuft ausschließlich über den virtuellen Datenraum (VDR – Virtual Data Room), den Frage-Antwort-Prozess (Q&A) und den Disclosure Letter (Offenlegungserklärung). Was nicht offengelegt wurde, ist weder bekannt noch garantiert – das im SPA (Share Purchase Agreement, Unternehmenskaufvertrag) verankerte Garantieregime modifiziert insoweit den allgemeinen Grundsatz, dass der Käufer das Risiko nicht offenbarter Mängel trägt. Gesetzliche Auskunftsansprüche im Streitfall: §§ 142, 144 ZPO; § 810 BGB; §§ 242, 259, 666 BGB; Art. 15 DSGVO; § 254 ZPO (Stufenklage).

## Eingaben

- Praxisprofil: `## M&A → DD-Struktur` (Kategorien, Schwellen)
- Praxisprofil: `## M&A → Issues-Memo-Format`
- Mandats-Kontext: `mandate/[code]/deal-kontext.md`
- VDR-Inventar oder Dokumentenliste

## Ablauf

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
| [etc.] | | | |

**Lücken:** [Anforderungskategorien ohne VDR-Inhalt – Nachforderung erforderlich]
```

### Schritt 2: Wesentlichkeitsschwelle anwenden

Gemäß Praxisprofil und Mandats-Kontext-Schwellen. Nicht alles prüfen, wenn die Schwelle Verträge >X EUR vorschreibt.

Bei Verträgen: nach angegebenem Wert (falls in Dateiname/Metadaten) oder nach Gegenparteirelevanz sortieren. Top-down prüfen bis Schwelle erreicht oder Kategorie erschöpft.

### Schritt 3: Issues extrahieren

Je gelesenes Dokument gegen den Standardkatalog für seine Kategorie prüfen:

**Gesellschaftsrecht / Verfassung:**
- Gesellschaftsvertrag / Satzung vollständig und aktuell?
- Kapitalaufbringung nachgewiesen (§§ 7, 19 GmbHG; §§ 36, 54 AktG)?
- Gesellschafterstruktur und Gesellschafterliste (§ 40 GmbHG) korrekt?
- Vinkulierungsklauseln, Vorkaufsrechte, Mitziehrechte?
- Beirat oder Gesellschafterausschuss mit eingeschränkten Rechten?
- Nachschuss- / Einziehungsklauseln (§§ 26, 34 GmbHG)?
- Auflösungsklauseln, Optionsrechte?

**Wesentliche Verträge:**
- Change-of-Control-Klausel (ausgelöst durch diesen Deal? Zustimmung erforderlich?)
- Abtretungsbeschränkung (kann der Vertrag auf Käufer übergehen?)
- Exklusivität / Wettbewerbsverbot (schränkt Käufer-Geschäft ein?)
- Mindestabnahme / Ausschließlichkeit (MFN, Preisbindung)
- Kündigungsrechte (kann Gegenpartei wegen des Deals kündigen?)
- Ungewöhnliche Haftungsregelungen; AGB-Kontrolle §§ 305 ff. BGB
- Compliance-Zusicherungen (Antikorruption, Sanktionen, Exportkontrolle)

**IP / Technologie:**
- Eigentumsnachweis (Abtretungen von Gründern/Arbeitnehmern vorhanden? § 69b UrhG; § 4 ArbNErfG)
- Open Source im Produkt (Copyleft-Risiko? GPL/LGPL/AGPL)
- Kern-IP lizenziert vs. Eigentum
- Anhängige oder drohende IP-Streitigkeiten
- Datenschutz (Verarbeitungsverzeichnis Art. 30 DSGVO; technisch-organisatorische Maßnahmen Art. 32 DSGVO)

**Arbeitnehmer:**
- Change-of-Control-Abfindungsansprüche (Kosten)
- Risiko Betriebsübergang § 613a BGB (Unterrichtungspflicht; Widerspruchsrecht 1 Monat)
- Betriebsrat – Anhörungs- / Mitbestimmungsrechte? (§ 102 BetrVG Kündigung; § 111 BetrVG Betriebsänderung)
- Anhängige Arbeitsrechtstreitigkeiten
- Schlüsselpersonen-Bindungsrisiko
- Scheinselbstständigkeit (§ 611a BGB; Nachzahlungsrisiko Sozialversicherung)

**Rechtsstreitigkeiten / Behörden:**
- Anhängige Verfahren und Rückstellungen
- Angedrohte Ansprüche
- Behördliche Anfragen oder laufende Prüfungen
- Wiederkehrende Streitigkeiten (Produkthaftung, Verbraucherschutz)
- Kartellrecht / BKartA-Verfahren

**Umwelt / Regulatorisch:**
- Altlasten (BBodSchG); laufende Sanierungsmaßnahmen
- Umweltgenehmigungen / BImSchG-Genehmigungen
- Produktsicherheit / CE-Kennzeichnung
- Sektorspezifische Genehmigungen (BaFin, BNetzA, etc.)

### Schritt 4: Finding formulieren

> **Quellenattribution.** Bei Verweis auf Normen, Rechtsprechung oder Behördenmaßnahmen mit entsprechendem Tag versehen: `[juris]`, `[beck-online]`, `[Westlaw DE]` bei Zitaten aus Recherchetool in dieser Sitzung; `[Websuche — prüfen]` bei Web-Suche-Zitaten; `[Modellwissen — prüfen]` bei Zitaten aus Modellwissen; `[Nutzer bereitgestellt]` bei VDR- oder Deal-Team-Quellen. Tags niemals entfernen oder zusammenfassen.

Je Finding-Vorlage aus Praxisprofil. Falls Seed-Memo dieses Format hat:

```
Finding #N: [Titel]
Kategorie: [Anforderungskategorie]
Schweregrad: [Stufe nach Hausschema]
Dokumente: [VDR-Pfad + Dokumentenname]
Finding: [Was das Dokument aussagt und warum es relevant ist]
Empfehlung: [Preisanpassung / Einbehalt / Zustimmung erforderlich / Garantie / Vertragsabbruch]
Vollzugshandlung: [ja – Zustimmung erforderlich / nein]
```

**Schweregradeinstufung (wenn Hausschema R/G/G):**
- 🔴 **Blockierend:** Beeinflusst Deal-Wert oder -struktur. Change-of-Control erfordert Zustimmung eines Hauptkunden. Ungeklärte IP-Eigentümerschaft. Verdeckte wesentliche Verbindlichkeit.
- 🟠 **Hoch:** Erheblich, aber lösbar. Zustimmung wahrscheinlich zu erlangen, aber Verhandlung nötig.
- 🟡 **Mittel:** Klärungsbedarf; lösbar. CoC-Information-only; Open Source mit Remediation; Risiko der Scheinselbstständigkeit.
- 🟢 **Niedrig:** Für die Akte vermerkt. Im Einklang mit Garantien. Kein Handlungsbedarf über die Garantie hinaus.

### Schritt 5: Bericht je Kategorie

Findings nach Anforderungskategorie gruppieren. Innerhalb der Kategorie nach Schweregrad sortieren.

```markdown
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

> Dieses Ergebnis entstammt VDR-Materialien, die vertraulich oder privilegiert oder beides sind. Es übernimmt den Vertraulichkeits-/Privilegierungsstatus der Quelle – Verteilung außerhalb des Vertraulichkeitskreises kann den Schutz aufheben.

# DD-Issues: [Deal-Code] — [Kategorie]

**Geprüfte Dokumente:** [N] von [M] in Kategorie
**Abdeckung:** [Alle | >X EUR-Schwelle | Top-N]
**Findings:** [N]🔴 [N]🟡 [N]🟢

---

### Zusammenfassung

[🔴 N blockierend · 🟠 N hoch · 🟡 N mittel] — [das Eine, was das Deal-Team wissen muss]

---

[Jedes Finding im Hausformat]

---

## Lücken

- [Anforderungspunkt ohne responsive Dokumente]
- [Referenziertes Dokument nicht im VDR]
```

## Übergaben

- **An ki-werkzeug-uebergabe:** Bei Nutzung von Luminance/Kira gemäß Praxisprofil massenhafte Vertragsextraktion dorthin übergeben.
- **An dealteam-zusammenfassung:** Aggregierte Findings speisen das Deal-Team-Briefing.
- **An wesentliche-vertraege-anlage:** Vertragsextraktionen speisen die Disclosure Schedule.
- **An vollzugs-checkliste:** Jedes Finding, das eine diskrete Vorvertrags-Handlung impliziert. Nicht auf „Zustimmungen" beschränkt – auch:
  - **Gesellschafter-/Organentscheidung** – Gesellschafterbeschlüsse, AR-Beschlüsse, ggf. § 179a AktG-HV-Beschluss
  - **Behördliche Einreichungen** – BKartA-Anmeldung, BMWK-FDI-Prüfung, BaFin-Anzeige
  - **Zustimmungen von Gegenparteien** – Change-of-Control, Abtretungsbeschränkungen
  - **Ablösungen, Kündigungen** – Freigabe Gesellschafterdarlehen (§ 30 GmbHG), Ablösung von Grundpfandrechten, Freistellungserklärungen
  - **Treuhand- / Einbehaltmechanismen** – Kaufpreiseinbehalt, R&W-Versicherungslieferung

## Batch-Verarbeitung

Für große Kategorien (300 Verträge): in Chargen verarbeiten. Nach jeder Charge laufende Issues-Liste aktualisieren und 🔴-Punkte sofort melden – nicht auf Abschluss der gesamten Kategorie warten.

## Entscheidungsbaum zum Abschluss

Mit dem Entscheidungsbaum-Nächste-Schritte aus CLAUDE.md `## Ergebnisse` abschließen.

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
