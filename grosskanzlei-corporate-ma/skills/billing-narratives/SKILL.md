---
name: billing-narratives
description: "Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise erstellen. Paragraf 3a RVG Stundenhonorar, GoBD Buchungsanforderungen, XRechnung ZUGFeRD. P..."
---

# Big-Law Billing Narratives (Corporate M&A)

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Big-Law Billing Narratives (Corporate M&A)
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Triage zu Beginn

Vor der Erstellung von Billing Narratives klären:

1. **Honorarvereinbarung vorhanden?** Stundenhonorar (Paragraf 3a RVG) oder Pauschalhonorar oder Success Fee oder Cap + Success Fee? Kein Narrative ohne klar definiertes Abrechnungsmodell.
2. **Taetigkeiten vollstaendig erfasst?** Alle Time Entries nach Phase, Workstream und Deliverable vorliegend? Fehlende Entries flaggen.
3. **Budgetstatus geprueft?** Aktuelles WIP gegen Budget halten; Scope Creep und Abweichungen markieren bevor Narrative erstellt wird.
4. **Mandantenvertraulichkeit:** Narrative darf kein Mandatsgeheimnis unnoetig offen legen (Paragraf 43a Abs. 2 BRAO); Formulierungen müssen prüfbar aber nicht erläuternd sein.
5. **Rechnungsreife?** Sind alle Bedingungen erfuellt (Leistungsstand, SPA-Meilenstein, vereinbarter Faelligkeitspunkt)? Bei Unsicherheit nicht abrechnen.
6. **E-Rechnung erforderlich?** Oeffentlicher Auftraggeber oder SPA-Klausel zu XRechnung/ZUGFeRD? Dann an `grosskanzlei-ma-erechnung-gobd` uebergeben.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Billing-Narrative-Struktur für M&A-Deals

### Time-Entry-Kategorien

| Phase | Workstream | Typische Taetigkeit |
|---|---|---|
| Pre-DD | Transaction Setup | Mandatsanlage, NDA-Verhandlung, VDR-Einrichtung |
| Due Diligence | Legal DD | Vertragsreview, Issue-Extraktion, Red-Flag-Report |
| Due Diligence | Corporate DD | Handelsregister-Auswertung, Gesellschafterliste |
| Signing | SPA-Verhandlung | Vertragsverhandlung, Kommentierung, Signing-Prep |
| Closing | Vollzug | CP-Tracking, Closing-Actions, Notartermin |
| Post-Closing | PMI | Vertragsuebernahmen, Paragraf 613a BGB, Gesellschafterliste |

### Narrative-Formulierungsregeln

1. **Mandantentauglich:** Keine Rechtsbegriffe ohne Erklaerung; kein unnoetig detaillierter Sachverhalt.
2. **Prüfbar:** Jede Taetigkeit muss einem Workstream und Deliverable zugeordnet sein.
3. **Vertraulich:** Kein Inhalt aus privilegierten Dokumenten (anwaltliche Stellungnahmen, DD-Reports) in externe Narrative.
4. **Zeitgenau:** Time Entries tagesgenau; keine rueckwirkenden Grosskorrekturen ohne Erklaerung.
5. **Budget-Delta markieren:** Abweichungen > 10 % zum vereinbarten Budget kommentieren.

### Narrative-Muster nach Workstream

```
Due Diligence — Legal: Vertragsreview (Commercial Contracts)
Pruefen und Analysieren von [N] Lieferantenvertraegen im Datenraum; Erstellung eines
Issue-Summary für [N] Material-Contract-Eintraege; Identifizierung von [N] Change-of-
Control-Klauseln mit Zustimmungserfordernis; Abstimmung mit Deal-Team zu CP-Implikationen.
[N.N h]
```

```
Signing — SPA-Verhandlung: Kommentierung Paragraf [Klausel] / Garantiekatalog
Erarbeitung der Kanzleiposition zu Abschnitt [X] des SPA-Entwurfs (Garantiekatalog);
Abstimmung mit Mandant zu akzeptablem Risikoprofil; Einarbeitung in Track-Changes-Version;
Verhandlungssitzung [DATUM] mit Gegenseite.
[N.N h]
```

## Schritt-für-Schritt-Workflow

**Vorab:** Das folgende Prüfschema ist eine Standardlinie. Wenn die Mandantenlage abweicht, werden die Schritte gekürzt, umgestellt oder an einen Spezialskill übergeben. Maßgeblich ist ein belastbares Ergebnis, nicht das Abarbeiten einer Tabelle.

1. **Time Entries importieren:** Alle Zeiteintragungen für den Abrechnungszeitraum nach Phase und Workstream sortieren.
2. **Budget-Abgleich:** WIP gegen vereinbartes Budget halten; Abweichungen > 10 % markieren und begruenden.
3. **Narrative verfassen:** Pro Workstream ein Narrative-Block nach Formulierungsregeln oben.
4. **Mandantenvertraulichkeit prüfen:** Kein Mandatsgeheimnis unnoetig offen gelegt? Narratives mandantentauglich formuliert?
5. **Rechnungspflichtangaben prüfen:** Paragraf 14 UStG-Angaben vollstaendig (Leistungsbeschreibung, Zeitraum, Steuernummer, USt-ID)?
6. **Cap-/Success-Fee-Check:** Gesamthonorar gegen vereinbarten Cap prüfen; Success-Fee-Bedingungen eingetreten?
7. **E-Rechnungspflicht prüfen:** Oeffentlicher Auftraggeber? XRechnung/ZUGFeRD erforderlich? → an `grosskanzlei-ma-erechnung-gobd` uebergeben.
8. **Rechnungsreife-Ampel ausgeben:** Gruen (alle Bedingungen erfuellt), Gelb (offene Punkte), Rot (Rechnung zurueckhalten).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Billing Narrative für M-and-A-Mandat erstellen | Narrative nach Schema; Template unten |
| Variante A — Mandant will kurzere Rechnungen weniger Detail | Kurzform-Narrative ohne Einzelleistungsaufstellung |
| Variante B — Stuendliche Abrechnung vs Pauschalhonorar | Bei Pauschalhonorar vereinfachtes Narrative ohne Stundenangaben |
| Variante C — Mehrteiliges Projekt Abrechnung in Phasen | Phasen-Narrative separat; Gesamtnachweis am Ende |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Mandant / Matter-Controller — Tonfall: knapp, prüfbar, mandantentauglich

```
BILLING NARRATIVE LEDGER
Mandat: [MANDATSCODE] / [ZIELGESELLSCHAFT]
Abrechnungszeitraum: [DATUM] bis [DATUM]
Erstellt: [TT.MM.JJJJ]
Matter-Controller: [NAME]

> Vertraulich — Mandatsgeheimnis Paragraf 43a Abs. 2 BRAO.

--- BUDGET-STATUS ---
Vereinbartes Budget: [BETRAG EUR]
WIP aktuell: [BETRAG EUR]
Abweichung: [+ / - BETRAG EUR] ([%])
Scope-Creep-Flag: [KEIN / JA: BESCHREIBUNG]

--- TIME ENTRIES NACH WORKSTREAM ---

WORKSTREAM: Due Diligence — Legal
[DATUM] | [TIMEKEEPER] | [N.N h] | [NARRATIVE]
[DATUM] | [TIMEKEEPER] | [N.N h] | [NARRATIVE]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

WORKSTREAM: SPA-Verhandlung
[Analog]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

WORKSTREAM: Closing
[Analog]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

--- RECHNUNGS-ZUSAMMENFASSUNG ---
Honorar netto: [BETRAG EUR]
Umsatzsteuer 19 %: [BETRAG EUR]
Auslagen: [BETRAG EUR]
Summe brutto: [BETRAG EUR]
Cap-Pruefung: [UNTER CAP / CAP ERREICHT]
Success Fee: [NICHT FAELLIG / FAELLIG: BETRAG EUR]

--- RECHNUNGSREIFE-AMPEL ---
Status: [GRUEN / GELB / ROT]
Offene Punkte: [KEINE / LISTE]
Freigabe durch: [PARTNER-NAME]

--- E-RECHNUNG ---
XRechnung/ZUGFeRD erforderlich: [JA → Uebergabe grosskanzlei-ma-erechnung-gobd / NEIN]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klärenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Rote Schwellen

- **Honorarvereinbarung Paragraf 3a RVG muendlich oder fehlend** — Formverstos; Anwalt kann nur RVG-Pflichtgebuehren verlangen; Vereinbarung unverzueglich schriftlich nachholen.
- **Narrative enthaelt Mandatsgeheimnis** — Paragraf 43a Abs. 2 BRAO; Formulierungen vor Versand prüfen; keine anwaltlichen Stellungnahmen, keine Parteiinterna in externen Narratives.
- **WIP ueberschreitet Cap ohne Mandanteninformation** — Haftungsrisiko; Mandant informieren und Scope-Abgleich durchfuehren bevor weitergearbeitet wird.
- **Rechnungspflichtangaben Paragraf 14 UStG unvollstaendig** — kein Vorsteuerabzug für Mandant; Rechnung korrigieren; Mahngebueehr-Risiko.
- **Leistung ohne Akte / Workstream** — GoBD-Verstos; Time Entry kann nicht verbucht werden; Nacherfassung nur mit Erklaerung.

## Arbeitsmodus

- Taetigkeiten nach Phase, Workstream und Deliverable erfassen.
- Narratives knapp, mandantentauglich und prüfbar formulieren.
- Budgetabweichungen und Scope Creep markieren.
- WIP, Cap, Success Fee, Auslagen, Rabatte und Steuerlogik als eigene Prüfpunkte fuehren.
- Bei Rechnungsreife an `grosskanzlei-ma-erechnung-gobd` uebergeben.

## Standardausgabe

- Billing Narrative Ledger.
- Budgetstatus nach Workstream.
- Rechnungsreife-Ampel.
- Übergabe an E-Rechnung/GoBD mit Belegkette.

## Vorlagen

- assets/templates/billing-narrative-ledger.md
- assets/templates/erechnung-gobd-billing.md

## Quellen und Vertiefung

- Paragraf 3a RVG (Stundenhonorar-Vereinbarung; Formerfordernis)
- Paragraf 49b BRAO (Vergaetungsvereinbarung)
- Paragraf 4a RVG (Erfolgshonorar)
- Paragraf 14 UStG (Rechnungspflichtangaben)
- Paragraf 146 AO / Paragraf 238 ff. HGB (GoBD; Buchfuehrungspflicht)
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.
- Mayer, in: Gerold/Schmidt, RVG, 26. Aufl. 2023, Paragraf 3a Rn. 5 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---
<!-- AUDIT 27.05.2026 bundle_004 -->
**Halluzinations-Audit 27.05.2026**
