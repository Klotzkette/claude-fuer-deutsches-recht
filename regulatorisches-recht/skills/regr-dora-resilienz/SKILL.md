---
name: regr-dora-resilienz
description: "Regr Dora Resilienz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Regr Dora Resilienz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Regr Dora Resilienz** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `regr-dora-resilienz-spezial` | Spezialfall DORA Digital Operational Resilience Act: IKT-Risikomanagement, Drittparteienrisiko, TLPT-Tests. Pruefraster fuer Finanzunternehmen und IKT-Dienstleister. |
| `regr-finanzdienstleistungsregulierung-bauleiter` | Bauleiter Finanzdienstleistungsregulierung: KWG, ZAG, KAGB, WpHG, BaFin-Mitteilungen. Pruefraster fuer Lizenz- und Erlaubnistatbestaende. |
| `regr-mica-kryptoassets-spezial` | Spezialfall MiCA-Verordnung Kryptoassets: Asset-Referenced-Tokens, E-Money-Tokens, andere Kryptowerte. Pruefraster fuer Emittent, CASP, Vertrieb. |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Regr Dora Resilienz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `regr-dora-resilienz-spezial`

**Fokus:** Spezialfall DORA Digital Operational Resilience Act: IKT-Risikomanagement, Drittparteienrisiko, TLPT-Tests. Pruefraster fuer Finanzunternehmen und IKT-Dienstleister.

# RegR: DORA-Resilienz

## Spezialwissen: RegR: DORA-Resilienz
- **Spezialgegenstand:** RegR: DORA-Resilienz / regr dora resilienz spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DORA, IKT, TLPT.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `regr-finanzdienstleistungsregulierung-bauleiter`

**Fokus:** Bauleiter Finanzdienstleistungsregulierung: KWG, ZAG, KAGB, WpHG, BaFin-Mitteilungen. Pruefraster fuer Lizenz- und Erlaubnistatbestaende.

# RegR: FDL-Regulierung Bauleiter

## Aufgabe
Bauleiter Finanzdienstleistungsregulierung: KWG, ZAG, KAGB, WpHG, BaFin-Mitteilungen.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Finanzdienstleistungsregulierung

### 1. Lizenz-/Erlaubnistatbestände im Überblick

| Geschäftstyp | Norm | Erlaubnis | Aufsicht |
|---|---|---|---|
| **Bankgeschäfte** § 1 I KWG (Einlagengeschäft, Kreditgeschäft, Diskontgeschäft, Garantiegeschäft, Depotgeschäft etc.) | § 32 I KWG | KWG-Erlaubnis | BaFin / Bundesbank |
| **Finanzdienstleistungen** § 1 Ia KWG (Anlagevermittlung, Anlageberatung, Finanzportfolioverwaltung, Drittstaateneinlagenvermittlung, etc.) | § 32 I KWG | KWG-Erlaubnis | BaFin |
| **Wertpapierdienstleistungen** § 2 II WpIG (Investmentaktiengesellschaft, Wertpapierinstitut) | § 15 WpIG | WpIG-Erlaubnis | BaFin |
| **Zahlungsdienste** § 1 ZAG (Geldtransfer, E-Geld, Zahlungsauslösedienst, Kontoinformationsdienst) | § 10 ZAG | ZAG-Erlaubnis | BaFin |
| **Investmentvermögen verwalten** § 1 I KAGB (OGAW, AIF) | § 17 KAGB | KAGB-Erlaubnis | BaFin |
| **Versicherungsgeschäfte** § 7 VAG | § 8 VAG | VAG-Erlaubnis | BaFin |
| **Crypto Asset Service Provider** MiCA (VO 2023/1114) seit 30.12.2024 | Art. 59 ff. MiCA | CASP-Zulassung | BaFin |

### 2. Erlaubnisvoraussetzungen (Grundmuster KWG / WpIG)

- **Anfangskapital** § 33 KWG bzw. § 17 WpIG (gestaffelt nach Geschäftsart; 730.000 / 150.000 Euro typisch).
- **Geschäftsleitende Personen** § 33 I 1 Nr. 2 KWG: Zuverlässigkeit + fachliche Eignung; mindestens zwei (Vier-Augen-Prinzip § 33 I 1 Nr. 5 KWG).
- **Inhaber bedeutender Beteiligungen** § 2c KWG: Zuverlässigkeit; Anzeigepflicht ab 10 % Stimmrechte.
- **Geschäftsorganisation** § 25a KWG: Risikomanagement, Compliance, IT, Auslagerungen.
- **Geschäftsplan** mit Tätigkeitsfeld, Strategie, Vorausschau.
- **Sicherungseinrichtungen** § 23a KWG / Einlagensicherung.

### 3. Bewilligungsverfahren BaFin

- **Antrag** schriftlich; umfangreiche Beilagen (Geschäftsplan, Lebensläufe, Compliance-Konzept).
- **Bearbeitungsdauer**: i.d.R. 6-12 Monate; **6-Monats-Frist** § 33 KWG / Art. 14 V CRR.
- **Vorab-Kontakt** mit BaFin sinnvoll (vor formellen Antrag).
- **EU-Pass** für Mitgliedstaaten: Notifikation; keine erneute Erlaubnis (§ 24a KWG, MiFID II, PSD2, etc.).

### 4. Laufende Aufsicht

- **Anzeigepflichten** §§ 24, 24a KWG: bedeutende Veränderungen.
- **Berichts- und Meldepflichten** §§ 25 ff. KWG (Eigenmittel, Liquidität, Großkredite, Marktrisiken).
- **MaRisk** (BaFin-Verlautbarung): Mindestanforderungen Risikomanagement.
- **BAIT / VAIT / ZAIT / KAIT**: bankaufsichtliche Anforderungen IT; ab 2025 ergänzt durch **DORA** (VO 2022/2554).
- **Inhaber-Aufsicht** § 2c KWG; **Inhaberkontrollverfahren** bei Aktienerwerb über Schwellen.

### 5. Sanktionen bei Erlaubnislosem Geschäft

- **Strafbar** § 54 KWG: bis 5 Jahre Freiheitsstrafe; § 63 ZAG; § 339 KAGB.
- **Verwaltungsmaßnahmen** § 37 KWG: Untersagung; Liquidation des Geschäfts.
- **BaFin-Bußgeld** §§ 56-60 KWG: bis 5 Mio. Euro / höhere Umsatzanteile.

## Praxisfallen

- **Crowdinvesting / Token-Emission**: oft Wertpapier-Prospektpflicht (VO 2017/1129) oder Vermögensanlage (VermAnlG); MiCA seit 30.12.2024 ergänzt für Kryptowerte.
- **Embedded Finance**: BaaS-Modelle (Banking as a Service) lösen Pflichten beim Diensteanbieter aus; Outsourcing nach § 25b KWG.
- **EWR-Pass**: nur für lizenzierte EU/EWR-Unternehmen; Drittstaaten brauchen separate Erlaubnis (§ 53 KWG für Zweigstelle).
- **MaComp** für Wertpapierdienstleister: BaFin-Mindestanforderungen Compliance.
- **BaFin-Auslegungs- und Anwendungshinweise** sind keine Rechtsnorm, aber faktische Bindung; Abweichung ist begründungspflichtig.
- **Sandbox / Regulatory Sandbox** existiert in DE nicht in dem Maße wie in UK; BaFin pflegt aber "no action letters" / Konsultationen.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `regr-mica-kryptoassets-spezial`

**Fokus:** Spezialfall MiCA-Verordnung Kryptoassets: Asset-Referenced-Tokens, E-Money-Tokens, andere Kryptowerte. Pruefraster fuer Emittent, CASP, Vertrieb.

# RegR: MiCA Kryptoassets

## Spezialwissen: RegR: MiCA Kryptoassets
- **Spezialgegenstand:** RegR: MiCA Kryptoassets / regr mica kryptoassets spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** CASP, BGH, BVerfG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
