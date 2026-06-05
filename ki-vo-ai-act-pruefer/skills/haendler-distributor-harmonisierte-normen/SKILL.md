---
name: haendler-distributor-harmonisierte-normen
description: "Haendler Distributor Harmonisierte Normen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Haendler Distributor Harmonisierte Normen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Haendler Distributor Harmonisierte Normen** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `haendler-distributor-pflichten-art-24` | Distributeur oder Grosshaendler von KI-Systemen fragt: Welche Sorgfaltspflichten habe ich beim Weitervertrieb von Hochrisiko-KI? Art. 24 KI-VO Haendler-Pflichten. Prüfraster: Plausibilitaetsprüfung CE-Kennzeichnung vorhanden EU-Konformitätserklärung vorhanden Lagerung und Transport risikofrei keine wesentliche Aenderung. Wann wird Haendler zum Anbieter oder Einführer Art. 25 KI-VO. Output: Checkliste Haendler-Sorgfaltspflichten. Abgrenzung zu einführer-importer-pflichten-art-23 (Import) und anbieter-werden-art-25 (Rollenwechsel). |
| `harmonisierte-normen-gap-uebergang` | Harmonisierte Normen, gemeinsame Spezifikationen und ISO/IEC-Standards im KI-VO-Uebergang: Gap-Analyse, Vermutungswirkung, Standards-Roadmap, Audit-Evidence und keine falsche Normenbehauptung. |
| `high-risk-negative-determination-memo` | Negativvermerk zur Hochrisiko-Einstufung: Art. 6 Abs. 2/Anhang III nicht einschlaegig oder Rueckausnahme Art. 6 Abs. 3. Dokumentiert Zweckbestimmung, tatsächliche Nutzung, Profiling-Sperre, Restpflichten und Re-Evaluation. |
| `hochrisiko-art-6-abs-1-sicherheitsbauteil` | Unternehmen integriert KI-Komponente in ein reguliertes Produkt (Medizinprodukt Maschine Fahrzeug) und fragt: Wird das Gesamtprodukt dadurch zum Hochrisiko-KI-System? Art. 6 Abs. 1 KI-VO Sicherheitsbauteil Anhang I. Prüfraster: ist Produkt in Anhang I gelistet (MDR IVDR Luftfahrt Kfz Spielzeug Maschinen etc.) und ist KI-Komponente Sicherheitsbauteil und erfordert das Sektorrecht Drittbeurteilung. Output: Entscheidungsbaum mit Ergebnis und Begründung. Abgrenzung zu hochrisiko-art-6-abs-2-anhang-iii (eigenständige Anhang-III-Hochrisiko-Einstufung). |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Haendler Distributor Harmonisierte Normen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `haendler-distributor-pflichten-art-24`

**Fokus:** Distributeur oder Grosshaendler von KI-Systemen fragt: Welche Sorgfaltspflichten habe ich beim Weitervertrieb von Hochrisiko-KI? Art. 24 KI-VO Haendler-Pflichten. Prüfraster: Plausibilitaetsprüfung CE-Kennzeichnung vorhanden EU-Konformitätserklärung vorhanden Lagerung und Transport risikofrei keine wesentliche Aenderung. Wann wird Haendler zum Anbieter oder Einführer Art. 25 KI-VO. Output: Checkliste Haendler-Sorgfaltspflichten. Abgrenzung zu einführer-importer-pflichten-art-23 (Import) und anbieter-werden-art-25 (Rollenwechsel).

# Händler-Pflichten (Distributor) — Art. 24 KI-VO

## Zweck

Händler (distributor) sind alle Akteure in der Lieferkette, die ein Hochrisiko-KI-System bereitstellen, ohne Anbieter oder Einführer zu sein und ohne das System wesentlich zu verändern. Art. 24 KI-VO legt ihre Pflichten fest.

## Wer ist Händler?

Ein Händler ist eine in der Lieferkette tätige natürliche oder juristische Person, die ein Hochrisiko-KI-System im Unionsmarkt bereitstellt, ohne es in eigener Verantwortung in Verkehr zu bringen oder zu nutzen.

**Typische Beispiele:** Softwaremarktplätze, IT-Reseller, Systemintegratoren (soweit sie das System nicht wesentlich verändern), Cloud-Anbieter (in bestimmten Konstellationen).

## Pflicht 1 — Plausibilitätsprüfung vor Bereitstellung (Art. 24 Abs. 1 KI-VO)

Bevor der Händler ein Hochrisiko-KI-System bereitstellt, muss er prüfen, ob:
- Das System die CE-Kennzeichnung trägt
- Die EU-Konformitätserklärung vorhanden und zugänglich ist
- Die Gebrauchsanweisung in der Sprache des Mitgliedstaates vorliegt, in dem das System bereitgestellt wird
- Der Anbieter und gegebenenfalls der Einführer ihre Pflichten nach Art. 16 bis 23 KI-VO erfüllt haben (soweit dies der Händler anhand der verfügbaren Informationen beurteilen kann)

**Prüffragen:**
- Liegt Ihnen die CE-Kennzeichnung des Systems vor?
- Liegt Ihnen die EU-Konformitätserklärung vor?
- Liegt die Gebrauchsanweisung in der relevanten Sprache vor?

## Pflicht 2 — Keine Bereitstellung bei bekanntem Verstoß (Art. 24 Abs. 1 lit. b KI-VO)

Der Händler darf das System nicht bereitstellen, wenn er Grund zu der Annahme hat, dass:
- Das System nicht den Anforderungen der KI-VO entspricht
- Das System eine ernste Gefahr darstellt

## Pflicht 3 — Kooperation mit Marktüberwachungsbehörden (Art. 24 Abs. 2 KI-VO)

Der Händler muss:
- Mit nationalen Marktüberwachungsbehörden auf Anfrage kooperieren
- Dokumentation bereitstellen, die die Konformität des Systems nachweist (soweit er darüber verfügt)
- Die Identität des Anbieters und des Einführers angeben

## Pflicht 4 — Aufbewahrung (Art. 24 Abs. 3 KI-VO)

Der Händler muss für zehn Jahre aufbewahren:
- Kopie der Konformitätserklärung (soweit er darüber verfügt)
- Kontaktdaten des Anbieters und des Einführers

## Wann wird der Händler zum Anbieter oder Einführer?

**Zum Anbieter wird der Händler (Art. 24 Abs. 4 i.V.m. Art. 25 KI-VO), wenn er:**
- Das System unter eigenem Namen oder eigener Marke in Verkehr bringt
- Das System wesentlich verändert (auch durch Konfiguration, Anpassung, Re-Training)
- Den bestimmungsgemäßen Zweck des Systems ändert

**Zum Einführer wird der Händler, wenn:**
- Das System aus einem Drittland stammt und er das System als Erster in der EU in Verkehr bringt

**Prüffragen:**
- Verändern Sie das System in irgendeiner Weise (Konfiguration, Anpassung, Fine-Tuning)?
- Vermarkten Sie das System unter eigenem Namen oder eigener Marke?

## Praktische Bedeutung für Software-Marktplätze

Betreiber von App-Stores oder Software-Marktplätzen, auf denen Hochrisiko-KI-Systeme angeboten werden, können als Händler eingestuft werden. Sie müssen dann die Pflichten nach Art. 24 KI-VO erfüllen.

Die Abgrenzung zu Hosting-Diensten, die nur infrastrukturelle Dienste erbringen (Mere-Conduit), ist noch nicht abschließend durch Leitlinien konkretisiert.

## Meldepflicht bei Risiken (Art. 24 Abs. 2 KI-VO)

Der Händler muss den Anbieter, den Einführer und die nationalen Behörden informieren, wenn er feststellt, dass das System eine Gefahr darstellt oder nicht der KI-VO entspricht.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — HAENDLER DISTRIBUTOR PFLICHTEN ART 24
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 24 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `harmonisierte-normen-gap-uebergang`

**Fokus:** Harmonisierte Normen, gemeinsame Spezifikationen und ISO/IEC-Standards im KI-VO-Uebergang: Gap-Analyse, Vermutungswirkung, Standards-Roadmap, Audit-Evidence und keine falsche Normenbehauptung.

# Harmonisierte Normen und Übergang

## Problem

Die KI-VO wird durch harmonisierte Normen, gemeinsame Spezifikationen, Leitlinien und Codes konkretisiert. In der Übergangsphase ist gefährlich, Standards als fertige Rechtssicherheit zu verkaufen.

## Prüfraster

1. Welche KI-VO-Pflicht soll durch Standard abgedeckt werden?
2. Gibt es eine harmonisierte Norm mit Vermutungswirkung?
3. Gibt es nur Entwurf, ISO/IEC-Standard oder Branchenstandard?
4. Welche Lücke bleibt zum konkreten Artikel?
5. Welche Evidence kann der Standard trotzdem liefern?
6. Wann wird die Roadmap aktualisiert?

## Typische Bausteine

- AI Management System.
- Risikomanagement.
- Datenqualität.
- Cybersecurity.
- Logging.
- Human Oversight.
- Modellkarten und technische Dokumentation.

## Output

- Standards-Gap-Matrix.
- Übergangsfahrplan.
- Audit-Evidence-Liste.
- Formulierung, was behauptet werden darf und was nicht.

## Qualitätsregel

Nie "ISO erfüllt KI-VO" pauschal schreiben. Immer Artikel, Standardkapitel, Nachweis und Lücke nebeneinanderstellen.

## 3. `high-risk-negative-determination-memo`

**Fokus:** Negativvermerk zur Hochrisiko-Einstufung: Art. 6 Abs. 2/Anhang III nicht einschlaegig oder Rueckausnahme Art. 6 Abs. 3. Dokumentiert Zweckbestimmung, tatsächliche Nutzung, Profiling-Sperre, Restpflichten und Re-Evaluation.

# High-Risk Negative Determination Memo

## Ziel

Wenn ein Unternehmen ein System nicht als Hochrisiko einstuft, muss diese Entscheidung später nachvollziehbar sein. Dieser Skill baut den Negativvermerk.

## Aufbau

1. Systembeschreibung.
2. Anbieter-/Betreiberrolle.
3. Zweckbestimmung.
4. Tatsächliche Nutzung.
5. Anhang-III-Matrix.
6. Art. 6 Abs. 3 Rückausnahme, wenn relevant.
7. Profiling-Sperre.
8. Restpflichten: Art. 4, Art. 5, Art. 50, GPAI, DSGVO.
9. Re-Evaluation-Trigger.

## Re-Evaluation-Trigger

- neuer Use Case;
- neue Nutzergruppe;
- neue Datenart;
- Integration in HR, Kredit, Bildung, Justiz, Medizin oder öffentliche Verwaltung;
- Modellwechsel;
- Incident;
- Behörden- oder Leitlinienänderung.

## Output

Ein unterschriftsreifer Vermerk mit klarer Entscheidung:

- "Nicht Hochrisiko, weil..."
- "Grenzen der Freigabe..."
- "Diese Nutzungen bleiben verboten oder freigabepflichtig..."

## Warnung

Ein Negativvermerk schützt nur, wenn er aktuell gehalten wird. Er ist kein Freibrief für spätere Zweckverschiebung.

## 4. `hochrisiko-art-6-abs-1-sicherheitsbauteil`

**Fokus:** Unternehmen integriert KI-Komponente in ein reguliertes Produkt (Medizinprodukt Maschine Fahrzeug) und fragt: Wird das Gesamtprodukt dadurch zum Hochrisiko-KI-System? Art. 6 Abs. 1 KI-VO Sicherheitsbauteil Anhang I. Prüfraster: ist Produkt in Anhang I gelistet (MDR IVDR Luftfahrt Kfz Spielzeug Maschinen etc.) und ist KI-Komponente Sicherheitsbauteil und erfordert das Sektorrecht Drittbeurteilung. Output: Entscheidungsbaum mit Ergebnis und Begründung. Abgrenzung zu hochrisiko-art-6-abs-2-anhang-iii (eigenständige Anhang-III-Hochrisiko-Einstufung).

# Hochrisiko-KI: Sicherheitsbauteil — Art. 6 Abs. 1 KI-VO

## Zweck

Art. 6 Abs. 1 KI-VO ist einer von zwei Pfaden zur Hochrisiko-Einstufung. Ein KI-System ist Hochrisiko, wenn es Sicherheitsbauteil eines Produkts ist, das unter Anhang-I-Sektorrecht fällt und einer Drittprüfung unterzogen werden muss. Dieser Skill prüft beide Voraussetzungen im Entscheidungsbaum.

## Zwei kumulativ zu erfüllende Voraussetzungen

### Voraussetzung 1 — Sicherheitsbauteil oder Produkt selbst

**Frage:** Ist das KI-System:
- (A) Ein Sicherheitsbauteil eines Produkts? Ein Sicherheitsbauteil ist nach Art. 3 Nr. 14 KI-VO eine Komponente eines Produkts oder Systems, die eine Sicherheitsfunktion für das Produkt oder System erfüllt, oder deren Ausfall oder Fehlfunktion die Gesundheit und Sicherheit von Personen oder Sachen gefährdet.
- (B) Oder selbst ein Produkt, das unter Anhang-I-Sektorrecht fällt?

**Abgrenzung:**
- Ein KI-System zur Qualitätskontrolle in einer Maschine: Sicherheitsbauteil, wenn es die Maschinensicherheit gewährleistet
- Ein autonomes Fahrzeugsystem: Kann selbst Produkt nach Anhang I sein
- Ein KI-System für die Verwaltung (z.B. HR-Software): Kein Sicherheitsbauteil

### Voraussetzung 2 — Anhang-I-Sektorrecht

Das Produkt (oder der Bereich des Sicherheitsbauteils) muss unter eines der in Anhang I aufgeführten Sektorrechtsakte fallen. Vollständige Liste:

| Nr. | Sektorrechtsakt |
|---|---|
| 1 | Maschinenverordnung (EU) 2023/1230 |
| 2 | Spielzeugrichtlinie 2009/48/EG |
| 3 | Richtlinie 2006/42/EG (aufgehoben durch Maschinenverordnung, Übergangsregeln beachten) |
| 4 | Richtlinie 2014/53/EU (Funkanlagen) |
| 5 | Richtlinie 2014/34/EU (ATEX — Geräte in explosionsgefährdeten Bereichen) |
| 6 | Richtlinie 2006/42/EG (Druckgeräte) — Verordnung (EU) 2014/68/EU |
| 7 | Verordnung (EU) 2016/424 (Seilbahnen) |
| 8 | Richtlinie 2013/29/EU (pyrotechnische Gegenstände) |
| 9 | Richtlinie 2014/90/EU (Schiffsausrüstung) |
| 10 | Richtlinie 2016/797/EU (Eisenbahnsystem) |
| 11 | Verordnung (EU) 2018/858 (Kraftfahrzeuge) |
| 12 | Verordnung (EU) 2019/2144 (Fahrzeugsicherheit) |
| 13 | Verordnung (EU) 2018/1139 (Luftfahrt) |
| 14 | Verordnung (EU) 2017/745 (Medizinprodukte — MDR) |
| 15 | Verordnung (EU) 2017/746 (In-vitro-Diagnostika — IVDR) |

**Prüffragen:**
- Fällt das Produkt, in das das KI-System integriert ist, unter einen dieser Sektorrechtsakte?
- Falls ja, welcher konkret?

### Voraussetzung 3 — Drittprüfung nach Sektorrecht erforderlich

Die dritte kumulativ erforderliche Voraussetzung: Das Produkt oder das KI-System als Sicherheitsbauteil muss nach dem einschlägigen Sektorrechtsakt einer Konformitätsbewertung durch eine dritte Partei (benannte Stelle) unterzogen werden.

**Prüffragen:**
- Sieht das einschlägige Sektorrecht eine Konformitätsbewertung durch eine benannte Stelle vor?
- Ist die benannte Stelle für das KI-System zuständig oder nur für das Gesamtprodukt?

**Wenn nur Selbstkonformitätsbewertung vorgesehen:** Art. 6 Abs. 1 KI-VO greift nicht. Prüfen Sie Art. 6 Abs. 2 KI-VO.

## Ergebnis des Entscheidungsbaums

**Hochrisiko nach Art. 6 Abs. 1 KI-VO, wenn:**
- KI-System ist Sicherheitsbauteil oder Produkt nach Anhang I UND
- Einschlägiges Sektorrecht erfordert Drittkonformitätsbewertung

**Keine Hochrisiko-Einstufung nach Art. 6 Abs. 1, wenn:**
- KI-System ist kein Sicherheitsbauteil oder kein Produkt nach Anhang I (→ prüfe Art. 6 Abs. 2)
- Sektorrecht erfordert keine Drittprüfung

**Folge bei Hochrisiko-Einstufung nach Art. 6 Abs. 1:**
- Konformitätsbewertung durch benannte Stelle (kein reines Selbstbewertungsmodul möglich für das KI-System)
- Koordination zwischen KI-VO-Konformitätsbewertung und Sektorrechts-Konformitätsbewertung

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — HOCHRISIKO ART 6 ABS 1 SICHERHEITSBAUTEIL
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Abs. 1 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
