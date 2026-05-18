---
name: marketing-claims-review
description: >
  Prüfung von Werbeaussagen auf Irreführungs- und Wettbewerbsrechtsrisiken nach
  deutschem und europäischem Recht. Lädt, wenn der Nutzer „Werbetext prüfen",
  „Marketingaussagen freigeben", „UWG-Prüfung", „Health Claims", „klimaneutral
  prüfen" oder vergleichbare Werbebehauptungen zur Überprüfung vorlegt.
language: de
triggers:
  - "Werbetext prüfen"
  - "Marketingaussagen prüfen"
  - "UWG-Prüfung"
  - "Health Claims"
  - "klimaneutral Werbung"
  - "Werbeaussagen freigeben"
  - "irreführende Werbung"
  - "vergleichende Werbung"
  - "Influencer-Werbung"
  - "Heilmittelwerbegesetz"
---

# Werbeaussagen-Prüfung (Marketing Claims Review)

## Zweck

Das Marketing möchte das Produkt bestmöglich darstellen. Das Recht verlangt, dass Werbeaussagen wahr oder zumindest nicht nachweislich falsch sind. Diese Skill identifiziert Behauptungen, die Abmahnrisiken, behördliche Anfragen (Bundeskartellamt, Verbraucherschutzverbände) oder eine UWG-Klage auslösen können, und schlägt Alternativformulierungen vor, die Werbewirkung und Rechtskonformität verbinden.

Die Skill lädt automatisch, wenn der Nutzer Werbetexte, Landingpages, Produktbeschreibungen, E-Mail-Kampagnen, Anzeigentexte oder Influencer-Briefings zur Prüfung vorlegt.

## Eingaben

- **Werbetext / Werbemittel** — Landingpage, E-Mail, Anzeige, Produktbeschreibung, Tagline, Social-Media-Post, Influencer-Brief (als Datei oder direkte Eingabe)
- **Produktbeschreibung** — Was tut das Produkt tatsächlich? Welche Nachweise liegen vor?
- **Nachweisunterlagen** — Studien, Testzertifikate, Kundendaten (soweit vorhanden)
- **Zielgruppe und Medium** — B2C oder B2B, Online, Print, Social Media, Rundfunk, Fachpresse
- **Zielmärkte** — Deutschland, Österreich, Schweiz, EU-weit; Sonderregelungen bei Lebensmitteln, Arzneimitteln, Medizinprodukten

## Rechtlicher Rahmen

### Kernvorschriften

**Allgemeines Wettbewerbs- und Werberecht**
- § 3 UWG: Verbot unlauterer geschäftlicher Handlungen
- § 5 UWG: Irreführende geschäftliche Handlungen (irreführende Angaben über Beschaffenheit, Herkunft, Testergebnisse, Alleinstellungsbehauptungen)
- § 5a UWG: Irreführung durch Unterlassen
- § 6 UWG: Vergleichende Werbung (zulässig nur bei objektivem, nachweisbarem und sachlichem Vergleich auf Grundlage wesentlicher Merkmale)
- § 7 UWG: Unzumutbare Belästigung (Spam, unerwünschte Telefonwerbung)
- §§ 8, 9 UWG: Unterlassung, Schadensersatz; Aktivlegitimation von Mitbewerbern und Verbänden (§ 8 Abs. 3 UWG)
- Anlage 1 zu § 3 Abs. 3 UWG: Stets unzulässige geschäftliche Handlungen (Schwarze Liste)

**Klimaaussagen und Nachhaltigkeitswerbung**
- BGH, Urt. v. 27.06.2024 – I ZR 98/23, GRUR 2024, 1166 (Klimaneutralität): Werbeaussage „klimaneutral" ist irreführend nach § 5 Abs. 1 UWG, wenn die Kompensation nicht transparent offengelegt wird; Verbraucher interpretieren „klimaneutral" als absolute Eigenschaft, nicht als Kompensationsversprechen. Die Aussage erfordert eine klare, unmittelbar zugängliche Erläuterung des Kompensationswegs. `[verify]`
- BGH, Urt. v. 08.07.2021 – I ZR 214/18, GRUR 2021, 1561 (Umweltengel): Werbung mit Umwelteigenschaften unterliegt erhöhter Substantiierungspflicht. `[verify]`
- RL 2024/825/EU (Green Claims-RL, Umsetzungsfrist läuft): Verschärfte Anforderungen an Nachhaltigkeitsaussagen, insb. Verbot unbelegter Klimaneutrality-Claims

**Gesundheitsbezogene Angaben**
- Health-Claims-VO (EG) 1924/2006: Nährwert- und gesundheitsbezogene Angaben über Lebensmittel nur zulässig, wenn in der Positivliste (Art. 13 oder Art. 14) gelistet oder ausdrücklich zugelassen
- Heilmittelwerbegesetz (HWG): §§ 3, 3a HWG — irreführende Heilmittelwerbung verboten; § 5 HWG — Pflichtangaben; § 11 HWG — besondere Verbote (z. B. Vorher-Nachher-Bilder, Laienempfehlungen)
- LMIV VO (EU) 1169/2011: Irreführungsverbot für Lebensmittelkennzeichnung und -werbung

**Vergleichende Werbung und Konkurrentennennung**
- BGH, Urt. v. 02.04.2015 – I ZR 167/13, GRUR 2015, 1134 (Vergleichende Werbung — Prüfkriterien): Vergleich muss objektiv, nachweisbar, nicht irreführend und nicht verunglimpfend sein. `[verify]`
- BGH, Urt. v. 11.10.2017 – I ZR 78/16, GRUR 2018, 431 (Vergleichende Preisangaben): Zeitliche Aktualität des Vergleichs erforderlich. `[verify]`

**Influencer-Werbung und Kennzeichnungspflicht**
- BGH, Urt. v. 09.09.2021 – I ZR 90/20, GRUR 2022, 160 (Influencer II): Kommerzielle Postings ohne klare Kennzeichnung als Werbung sind unlauter nach § 5a Abs. 6 UWG (jetzt § 5a Abs. 4 UWG n. F.). `[verify]`
- § 22 MStV (Medienstaatsvertrag): Werbekennzeichnungspflicht für Telemedien und Social Media
- BGH GRUR 2022, 1812: Weitere Konkretisierung zur Werbekennzeichnung bei Eigenpromotion `[verify]`

### Kommentarliteratur

- Köhler/Bornkamm/Feddersen, UWG, 42. Aufl. 2024, § 5 Rn. 1.1 ff. (Irreführende Werbung) `[verify]`
- Harte-Bavendamm/Henning-Bodewig (Hrsg.), UWG, 5. Aufl. 2021, § 6 Rn. 10 ff. (Vergleichende Werbung) `[verify]`
- Sosnitza, UWG, 4. Aufl. 2022, § 5 Rn. 44 ff. (Alleinstellungsbehauptungen) `[verify]`
- Streinz/Kraus, LFGB, 2. Aufl. 2022, § 11 Rn. 5 ff. (Irreführungsverbot Lebensmittel) `[verify]`

## Ablauf

### Schritt 1: Standards laden und Branchenkontext klären

Aus der CLAUDE.md → `## Marketingaussagen-Standards` lesen:
- Unternehmensrichtlinie zu vergleichender Werbung (erlaubt mit Nachweis / nicht empfohlen / nie)
- Substantiierungsstandard (welcher Nachweis ist vor Veröffentlichung erforderlich)
- Historisch abgelehnte Aussagen (aus früheren Prüfungen lernen)

Branchenspezifika vorab klären: Lebensmittel → Health-Claims-VO; Arzneimittel/Medizinprodukte → HWG; Finanzprodukte → WpHG-Werbepflichten; Energieversorgung → EnWG-Transparenzregeln.

> **Nur anwendbare Normen zitieren.** Kein pauschales Auflisten aller UWG-Paragraphen. Eine Norm verdient einen Platz im Prüfvermerk nur, wenn sie einer konkreten, zitierten Werbeaussage zugeordnet werden kann.

### Schritt 2: Alle Werbeaussagen extrahieren

Jeden Satz oder jede Phrase, die eine Tatsache behauptet, einen Vergleich anstellt oder eine Zusage macht, auflisten. Reine Anpreisungen ohne konkreten Tatsachenkern (subjektive Einschätzungen, die kein vernünftiger Verbraucher für bare Münze nimmt) vorerst zurückstellen.

### Schritt 3: Klassifizieren und prüfen

**Werbeaussagen-Taxonomie:**

**Vage / subjektive Anpreisungen (Puffery)**

Subjektive Wertungen ohne messbaren Inhalt. Ob sie wettbewerbsrechtlich relevant sind, hängt vom konkreten Kontext und der angesprochenen Verkehrskreise ab.

| Beispiel |
|---|
| „Der beste Weg, Ihre Projekte zu managen" |
| „Sie werden es lieben" |
| „Revolutionär" |

**Konkrete Tatsachenbehauptungen (erhöhter Substantiierungsbedarf)**

Messbare, spezifische Aussagen, auf die ein vernünftiger Verbraucher vertraut.

| Beispiel | Erforderlicher Nachweis |
|---|---|
| „50 % schneller als [Wettbewerber]" | Benchmark-Daten, offengelegte Methodik, Datum |
| „Von 10.000 Unternehmen genutzt" | Aktuelle Nutzerzahl, nicht kumulierte Registrierungen |
| „Spart 5 Stunden pro Woche" | Studie oder Kundendaten mit offengelegter Stichprobe |
| „Klinisch geprüft" (Kosmetik) | Art und Umfang der Prüfung, keine Verwechselung mit Arzneimittelzulassung |
| „DSGVO-konform" | Konkrete Konfiguration und AV-Vertrag vorhanden — dies ist eine vertragliche Zusage |

**Klimaneutralitäts- und Nachhaltigkeitsaussagen (besonderer Fokus)**

Seit BGH, Urt. v. 27.06.2024 – I ZR 98/23, GRUR 2024, 1166 gilt: Die Aussage „klimaneutral" ist ohne unmittelbar zugängliche, vollständige Erläuterung des Kompensationswegs irreführend i. S. d. § 5 Abs. 1 UWG.

| Aussage | Prüfmuster |
|---|---|
| „Klimaneutral" (ohne Erläuterung) | Blocker — Erläuterung des Kompensationsansatzes auf derselben Kommunikationsfläche erforderlich |
| „CO₂-neutral bis 2030" | Zeitplan, Maßnahmen und Zwischenziele belegen |
| „Nachhaltig produziert" | Welches Label, welche Norm, welcher Verifizierer? |
| „100 % Ökostrom" | Herkunftsnachweis (Herkunftsnachweisregister nach EEG) |

**Vergleichende Werbung (§ 6 UWG, erhöhte Sorgfalt)**

Nennung eines Konkurrenten oder impliziter Bezug. Zulässig nur bei objektivem, nachweisbarem, aktuellem und sachlichem Vergleich.

| Beispiel | Lösungsmuster |
|---|---|
| „Schneller als [Konkurrent X]" | Head-to-Head-Daten mit offengelegter Methodik, oder Abstraktion auf „schneller als herkömmliche Lösungen" mit Substantiierung |
| „Die einzige Plattform, die X kann" | Falsch, wenn irgendein Mitbewerber X ebenfalls kann — „Die erste Plattform, die X…" (wenn wahr) oder Streichung von „einzig" |
| „[Konkurrent] kann das nicht" | Funktion zeigen und den Vergleich dem Betrachter überlassen |

**Implizite Behauptungen**

Nicht ausdrücklich formuliert, aber von vernünftigen Verkehrskreisen so verstanden.

| Beispiel | Implikation | Lösung |
|---|---|---|
| „Endlich eine sichere Alternative" | Konkurrenten sind unsicher | „Endlich Sicherheit, die Sie nachprüfen können" |
| Kundenlogos ohne Kontext | Diese Unternehmen empfehlen uns | „Zu unseren Kunden zählen…" ist zulässig; „Vertraut von…" impliziert mehr |
| „Für den Gesundheitsbereich entwickelt" | Medizinprodukt oder DSGVO-Gesundheitsdaten-Konformität | Konkretisieren oder qualifizieren |

**Absolute Behauptungen**

Kein Spielraum für Ausnahmen. Ein Gegenbeispiel macht sie falsch.

| Beispiel | Lösungsmuster |
|---|---|
| „Fällt nie aus" | „99,9 % Verfügbarkeit" (mit SLA-Definition) |
| „100 % genau" | Konkrete, substantiierte Prozentzahl mit Benchmark |
| „Garantiert" | Nur wenn tatsächlich eine Garantie mit Bedingungen angeboten wird — schafft sonst Gewährleistungsversprechen (§ 443 BGB) |
| „Immer" / „Jedes" | „Typischerweise" / „In den meisten Fällen" |

**Für jede Behauptung ausgeben:**

```markdown
**Behauptung:** „[genaues Zitat]"
**Typ:** [Konkrete Tatsache | Vergleichend | Implizit | Absolut | Klimaschutz/Nachhaltig | HWG/Health Claim]
**Nachweis vorhanden:** [Ja — Link/Referenz | Nein | Unbekannt]
**Bewertung:** [✅ Unbedenklich | ⚠️ Nachweis erforderlich | ⚠️ Umformulierung nötig | 🔴 Streichen]
**Empfohlene Formulierung:** „[Alternativtext, der die Werbewirkung erhält]"
**Begründung:** [eine Zeile mit Normbezug]
```

### Schritt 4: Produktabgleich

Entspricht das Produkt wirklich dem, was der Werbetext verspricht? Häufiges Phänomen: Marketingtext wurde auf Basis eines frühen Entwurfs verfasst, das Produkt hat sich geändert, der Text nicht. PRD oder PM befragen.

### Schritt 5: Ausgabe zusammenstellen

```markdown
# Werbeaussagen-Prüfvermerk: [Kampagne / Asset-Name]

**Geprüft:** [Datum]
**Werbemittel:** [Landingpage / E-Mail / Anzeige / etc.]

---

## Zusammenfassung

[N] Behauptungen geprüft. [N]✅ [N]⚠️ [N]🔴

**Freigabe:** [Ja | Mit Änderungen gemäß unten | Nein — Überarbeitung erforderlich]

---

## Behauptungen im Einzelnen

[Alle Behauptungsblöcke aus Schritt 3 — 🔴 zuerst, dann ⚠️, dann ✅]

---

## Empfohlene Überarbeitung

[Für kurze Assets (≤ 50 Wörter, Headline, Tagline, Einzeiler): den tatsächlich überarbeiteten Text ausgeben, nicht eine Beschreibung. Der Nutzer soll ihn direkt übernehmen können.
Für mittellange Assets (51–300 Wörter): überarbeiteten Text mit Korrekturen inline.
Für längere Assets (> 300 Wörter): Änderungs-Diff als Aufzählung.]

---

## Erforderliche Nachweise vor Veröffentlichung

| Behauptung | Benötigter Nachweis | Zuständig |
|---|---|---|
| [Behauptung] | [Datentyp / Studie / Zertifikat] | [PM / Marketing / Recht] |
```

## Ausgabeformat

Prüfvermerk im internen Format gemäß CLAUDE.md. Für kurze Assets (Tagline, Headline) ist das Ergebnis die tatsächlich überarbeitete Formulierung, nicht eine Metabeschreibung der Änderungen.

## Beispiel

**Sachverhalt:** Landingpage für ein Nahrungsergänzungsmittel mit folgenden Aussagen: (1) „Stärkt Ihr Immunsystem", (2) „Klimaneutral produziert", (3) „50 % wirksamer als Vitamin-C-Tabletten der Konkurrenz".

**Beispiel-Ergebnis:**
- **(1) „Stärkt Ihr Immunsystem"** → 🔴 **Streichen oder ersetzen.** Gesundheitsbezogene Angabe für Nahrungsergänzungsmittel nur zulässig, wenn in der Positivliste der Health-Claims-VO (EG) 1924/2006 gelistet. „Vitamin C trägt zur normalen Funktion des Immunsystems bei" wäre zulässig (Art. 13-Claim, zugelassen). Allgemein gehaltener Immunsystem-Claim ohne Nährstoffbezug ist nicht gelistet → Abmahnrisiko.
- **(2) „Klimaneutral produziert"** → ⚠️ **Umformulierung nötig.** Nach BGH, Urt. v. 27.06.2024 – I ZR 98/23, GRUR 2024, 1166 ist der Claim ohne unmittelbar zugängliche Erläuterung irreführend. Alternativ: „Produziert mit vollständig kompensierten CO₂-Emissionen — [Link zu Kompensationspartner und Methodik]."
- **(3) „50 % wirksamer als…"** → ⚠️ **Nachweis erforderlich.** Vergleichende Werbung (§ 6 UWG) zulässig nur mit objektivem, aktuellem, nachweisbarem Vergleich. Head-to-Head-Studie mit offengelegter Methodik vorlegen oder Formulierung streichen.

## Risiken und typische Fehler

- **Klimaneutralitäts-Claims ohne Transparenz:** Seit BGH GRUR 2024, 1166 konstant hohes Abmahnrisiko. Sämtliche Nachhaltigkeitsaussagen auf Plausibilität und Belegbarkeit prüfen; Kompensationspartner und Methodik immer offenlegen. Verschärfte Anforderungen durch Green Claims-RL 2024/825/EU (Umsetzungsfrist beachten).
- **Ungesicherte Alleinstellungsbehauptungen:** „Die Nr. 1", „Marktführer", „Einzig" — nur zulässig mit aktuellem, belastbarem Beleg (Marktanteilsstudie, Zertifikat o. Ä.).
- **Influencer-Posts ohne Werbekennzeichnung:** Nach BGH GRUR 2022, 160 (Influencer II) und §§ 5a Abs. 4 UWG, 22 MStV muss kommerzielle Kommunikation klar als Werbung erkennbar sein. „#ad" oder „Werbung" prominent am Anfang des Beitrags; nicht versteckt im Hashtag-Block.
- **Health-Claims außerhalb der Positivliste:** Jede gesundheitsbezogene Angabe für Lebensmittel und Nahrungsergänzungsmittel benötigt einen zugelassenen Claim nach Art. 13 oder 14 VO 1924/2006. Eigene Formulierungen sind grundsätzlich unzulässig.
- **HWG-Verstöße in Heilmittelwerbung:** § 3 HWG verbietet irreführende Werbung für Arzneimittel, Medizinprodukte und Verfahren. § 11 HWG verbietet spezifisch Laienempfehlungen, Vorher-Nachher-Bilder, Angst- und Druckwerbung gegenüber Verbrauchern.
- **Veraltete vergleichende Werbung:** BGH GRUR 2018, 431 — Preisvergleiche und Leistungsvergleiche müssen aktuell sein; veraltete Benchmarks machen die Werbung irreführend.
- **Fehlende Substantiierung bei absoluten Behauptungen:** „100 %" und „immer" unterliegen einem Nulltoleranzmaßstab; ein einziges dokumentiertes Gegenbeispiel genügt für eine begründete Abmahnung.

## Quellenpflicht

Jede Norm, Entscheidung oder Behördenaussage im Prüfvermerk muss belegt sein:

- **Primärquellen:** Gesetze und Verordnungen im Volltext (gesetze-im-internet.de, EUR-Lex), BfR-Stellungnahmen (Health Claims), Bundeskartellamt-Leitfäden
- **Rechtsprechung:** juris, beck-online, GRUR, NJW, GRUR-RS — BGH-Entscheidungen zur Zitierform `BGH, Urt. v. TT.MM.JJJJ – Az., Fundstelle Rn. X`
- **Kommentare:** Köhler/Bornkamm/Feddersen UWG, Harte-Bavendamm/Henning-Bodewig UWG, Sosnitza UWG
- **Branchenspezifisch:** BfArM (Arzneimittelwerbung), BVL (Lebensmittelkennzeichnung), DAZ (Apothekenwesen)

Quellen, die nur aus dem Modellwissen stammen, tragen das Tag `[verify]`. Pinpoint-Zitate (konkrete Randnummern, Seitenzahlen) tragen `[verify-pinpoint]`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
