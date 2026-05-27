---
name: launch-pruefung
description: "Produktmanager oder Rechtsabteilung will vor dem Launch pruefen ob das Produkt oder Feature produktrechtlich freigegeben werden kann. Vollstaendige rechtliche Freigabeprufung gegen konfiguriertes Pruefrahmenwerk und Risikokalibrierung. Normen ProdSG Produktsicherheitsgesetz MarktueberwG CE-Konformitaet EU-Produktsicherheits-VO 2023/988. Pruefraster KI-VO-Anforderungen UWG-Verstoessrisiken DSGVO DSA Verbraucherschutz BGB. Output Launch-Freigabe-Checkliste mit Ampel-Status offenen Punkten und Eskalations-Empfehlung. Abgrenzung: feature-risikobewertung fuer vertiefte Einzel-Risiko-Analyse."
---

# Produkt-Launch-Freigabeprüfung

## Zweck

Diese Skill führt eine vollständige produktrechtliche Freigabeprüfung durch: Sie liest das PRD oder die technische Produktbeschreibung, prüft jeden Kategorie des konfigurierten Prüfrahmenwerks und kalibriert die Befunde gegen die hinterlegten Risikoschwellen. Das Ergebnis ist ein Prüfvermerk, den ein Produktmanager liest und daraus genau weiß, was vor der Markteinführung erledigt sein muss.

Die Skill lädt automatisch, wenn der Nutzer eine Markteinführung, eine CE-Prüfung, eine Konformitätsbewertung oder eine Produktsicherheitsprüfung anspricht.

## Eingaben

- **PRD / Produktbeschreibung** — als Datei, Link oder direkte Eingabe
- **Technische Unterlagen** — Konstruktionszeichnungen, Stücklisten, Prüfberichte (soweit vorhanden)
- **Marketingplan** — falls vorhanden; bei substanziellem Marketinginhalt Weiterleitung an `werbeaussagen-pruefung`
- **Geplantes Markteinführungsdatum** — für die Dringlichkeitskalibrierung
- **Zielmarkt(e)** — EU-Binnenmarkt, nationale Sonderregelungen, Drittstaaten
- **Produktkategorie** — Verbraucherprodukt, Maschinenprodukt, Medizinprodukt, Lebensmittel, Kosmetikum usw.

## Rechtlicher Rahmen

### Kernvorschriften

**Produktsicherheit und Marktüberwachung**
- Produktsicherheitsgesetz (ProdSG) i. d. F. der GPSR-Umsetzung vom 13.12.2024 (Umsetzung VO (EU) 2023/988)
- VO (EU) 2023/988 über die allgemeine Produktsicherheit (GPSR), anwendbar ab 13.12.2024
- Produkthaftungsgesetz (ProdHaftG), ggf. ab 09.12.2026 in der Fassung gemäß RL 2024/2853/EU
- Maschinenverordnung (VO (EU) 2023/1230, MaschV) — für Maschinen und Sicherheitsbauteile
- CE-Kennzeichnung: je nach Produktgruppe RL 2014/30/EU (EMV), RL 2014/35/EU (Niederspannung), RL 2014/53/EU (Funkanlagen RED), RL 93/42/EWG / MDR VO (EU) 2017/745 (Medizinprodukte)
- VO (EU) 305/2011 (Bauprodukte-VO) — wo anwendbar

**Produkthaftung**
- §§ 1–15 ProdHaftG: Haftung des Herstellers für fehlerhafte Produkte, unabhängig vom Verschulden
- §§ 823 Abs. 1, 826 BGB: deliktische Haftung (Parallelweg)
- BGH, Urt. v. 16.06.2009 – VI ZR 107/08, NJW 2009, 2952 (Produkthaftung Hersteller — Beweislastverteilung) `[verify]`
- BGH, Urt. v. 02.02.2021 – VI ZR 1234/19, NJW 2021, 3458 (Produkthaftung — Konstruktionsfehler und Beweislast) `[verify]`

**Verbraucher- und Wettbewerbsrecht**
- §§ 433 ff. BGB: Kaufvertrag, Gewährleistung, Beschaffenheitsgarantie (§ 443 BGB)
- § 5 UWG: Irreführende Werbung (betrifft auch Produktbeschreibungen)
- BGH, Urt. v. 27.06.2024 – I ZR 98/23, GRUR 2024, 1166 (Klimaneutralität — Irreführung durch Produktkennzeichnung) `[verify]`

**Marktüberwachung**
- Marktüberwachungs-VO (EU) 2019/1020
- Zuständige Behörden: Bundesanstalt für Arbeitsschutz und Arbeitsmedizin (BAuA) für den Geräte- und Produktsicherheitsbereich; Bundesnetzagentur für Funkanlagen und Elektromagnetische Verträglichkeit; Landesbehörden im Vollzug

### Kommentarliteratur und Aufsätze

- Klindt/Schucht (Hrsg.), Produktsicherheitsgesetz (ProdSG/GPSR), 3. Aufl. 2025, § 3 ProdSG Rn. 12 ff. `[verify]`
- Kullmann, Produkthaftungsgesetz, 6. Aufl. 2021, § 1 ProdHaftG Rn. 15 ff. `[verify]`
- Foerste/Graf von Westphalen (Hrsg.), Produkthaftungshandbuch, 3. Aufl. 2012, § 24 Rn. 5 ff. `[verify]`
- Pfeiffer, NJW 2025, 123 (Umsetzung der GPSR — Änderungen im deutschen Produktsicherheitsrecht) `[verify]`

## Ablauf

### Schritt 1: Eingaben erfassen

Fehlende Dokumente beim Nutzer anfordern. Sofern ein Ticket-System (z. B. Jira, Linear) verbunden ist, Ticket und Kommentare abrufen — oft enthält die Kommentarhistorie Kontext, den das PRD nicht erfasst.

### Schritt 2: Produkt und Markteinführung verstehen

Vor der Checkliste in klarer Sprache beantworten:
- Was tut dieses Produkt? An wen richtet es sich (Verbraucher, gewerbliche Abnehmer, Mischnutzung)?
- Was ist neu gegenüber bereits geprüften Versionen?
- Neue Materialien, neue Nutzungsszenarien, neue Zielmärkte, neue Vertriebswege?
- Handelt es sich um ein reglementiertes Produkt (Medizinprodukt, Lebensmittel, Kosmetikum, Spielzeug, Maschine)?

**KI-Komponente — vor dem Rahmenwerk-Durchlauf prüfen.** Enthält das Produkt eine KI-Funktionalität — Drittanbieter-Modell, intern trainiertes Modell, automatisierte Klassifikation, generative Inhalte, Empfehlungen, Prognosen — auch wenn das PRD den Begriff „KI" nicht verwendet? Wörter wie „intelligent", „automatisiert", „personalisiert", „generiert", „vorgeschlagen" sind Hinweise. Sofern KI-Komponente erkannt → explizit kennzeichnen und ergänzend zum Rahmenwerk-Durchlauf nach dem KI-Rechtsrahmen (KI-VO (EU) 2024/1689) prüfen.

### Schritt 3: Prüfrahmenwerk durcharbeiten

Für jede der nachfolgenden Kategorien prüfen. Auto-Überspringen nur mit einzeiliger Begründung.

| Nr. | Kategorie | Leitfrage | Auto-Überspringen wenn |
|---|---|---|---|
| 1 | **Produktsicherheit / CE-Konformität** | Ist das Produkt sicher i. S. d. ProdSG/GPSR? CE-Kennzeichnung zutreffend? Technische Dokumentation vollständig? | Reine Softwareanpassung ohne Hardwarebezug |
| 2 | **Produkthaftung** | Konstruktionsfehler, Fabrikationsfehler, Instruktionsfehler (§ 1 Abs. 2 ProdHaftG)? Waren- und Personenschadenspotenzial? | Dienstleistung ohne Produktkomponente |
| 3 | **Kennzeichnung und Dokumentation** | Konformitätserklärung (DoC) vorhanden? Betriebsanleitung in DE? Hinweise auf Restrisiken? CE-Zeichen korrekt angebracht? | Unverändertes Altprodukt ohne neue Merkmale |
| 4 | **Datenschutz / DSGVO** | Neue Datenerhebung, neue Zwecke, neue Empfänger? Datenschutz-Folgenabschätzung erforderlich? | Keine personenbezogenen Daten verarbeitet |
| 5 | **Gewerbliche Schutzrechte / IP** | Drittanbieter-IP, Open-Source-Lizenzen, Designschutz, Patente von Wettbewerbern? | Keine neuen technischen Merkmale, keine Drittsoftware |
| 6 | **Vertragliche Zusagen und Garantien** | Widerspruch zu bestehenden AGB, SLA, Beschaffenheitsgarantien (§ 443 BGB), Werbeversprachen? | Keine kundenwirksamen Änderungen |
| 7 | **Marketingaussagen** | Prüfungsbedürftige Werbebehauptungen? Substantiierungspflicht? Bei substanziellem Marketinginhalt → Weiterleitung an `werbeaussagen-pruefung` | Kein Marketingmaterial vorhanden |
| 8 | **Sektor-spezifische Regulierung** | Berührt die Markteinführung einen regulierten Sektor (Medizinprodukte, Lebensmittel, Kosmetika, Spielzeug)? Spezialrecht anwendbar? | Kein geregelter Sektor betroffen |

**Sektor-Overlays.** Falls eine der folgenden Produktgruppen betroffen ist, ergänzend prüfen:

| Produktgruppe | Zusätzliche Prüfpflichten |
|---|---|
| **Medizinprodukte** | MDR VO (EU) 2017/745, IVDR VO (EU) 2017/746, Risikoklassifizierung, Benannte Stelle (Notified Body), klinische Bewertung, EUDAMED-Registrierung |
| **Lebensmittel / Nahrungsergänzung** | LMIV VO (EU) 1169/2011 (Pflichtangaben, Allergenkennzeichnung), LFGB, Health-Claims-VO (EG) 1924/2006, Novel-Food-VO (EU) 2015/2283 |
| **Kosmetika** | VO (EG) 1223/2009, Sicherheitsbewertung, CPNP-Notifizierung, INCI-Kennzeichnung |
| **Spielzeug** | Spielzeug-RL 2009/48/EG, nationale Umsetzung (2. GPSGV) |
| **Maschinen** | MaschV VO (EU) 2023/1230 (ab 20.01.2027), vorher RL 2006/42/EG, CE-Verfahren, Technische Dokumentation (Anh. IV), Betriebsanleitung |
| **Funkanlagen / Elektrogeräte** | RED RL 2014/53/EU, EMV-RL 2014/30/EU, Niederspannungs-RL 2014/35/EU, ggf. WEEE, RoHS |
| **Chemikalien / SVHC** | REACH-VO (EG) 1907/2006, CLP-VO (EG) 1272/2008, Sicherheitsdatenblatt |

**Ausgabe je Kategorie:**

```markdown
### [Nr.]. [Kategorie]

**Geprüft:** [was konkret geprüft wurde]
**Befund:** [Unauffällig | Klärungsbedarf | Blocker | Übersprungen]
**Detail:** [Konkrete Beschreibung, bezogen auf das PRD]
**Kalibrierung:** [gemäß CLAUDE.md — typischerweise FYI / erfordert Maßnahme / blockiert]
**Maßnahme:** [Was zu tun ist, wer verantwortlich ist, bis wann]
```

### Schritt 4: Schweregrad kalibrieren

Jeden Befund gegen die Kalibrierungstabelle in der CLAUDE.md abgleichen:
- Entspricht einem „typischerweise FYI"-Muster → vermerken, nicht blockieren
- Entspricht „erfordert Maßnahme" → Maßnahme und Zeitrahmen konkret benennen
- Entspricht „blockiert" → prominent kennzeichnen, eskalieren
- **Neuartig** (nicht in der Tabelle) → explizit vermelden: „Dieser Befund entspricht keinem Muster in der Kalibrierung — menschliche Entscheidung erforderlich"

### Schritt 5: Prüfvermerk zusammenstellen

```markdown
# Produkt-Launch-Prüfvermerk: [Produktname / Feature-Name]

**Geprüft:** [Datum] | **Launch-Datum:** [Datum] | **Prüfer:** [Name]
**PRD:** [Link] | **Ticket:** [Link, sofern verbunden]

---

## Ergebnis

[Ein Absatz: Kann das Produkt in den Markt? Was muss vorher erledigt werden?]

**Freigabe:** [Freigegeben | Freigabe unter Bedingungen | Blockiert bis X | Eskalation erforderlich]

---

## Befunde nach Kategorie

[Alle Kategorieblöcke aus Schritt 3 — übersprungene Kategorien am Ende mit Begründung]

---

## Maßnahmenplan

| Nr. | Maßnahme | Verantwortlich | Frist | Blockierend? |
|---|---|---|---|---|
| 1 | [konkret] | [PM/Technik/Recht] | [Datum] | Ja/Nein |

---

## Eskalationen

[Falls vorhanden — an wen, warum]

---

## Hinweise für künftige Prüfungen

[Falls diese Markteinführung ein Muster offenbart, das die Kalibrierungstabelle aktualisieren sollte]
```

### Schritt 6: Privilegierten Vermerk UND bereinigten Ticket-Kommentar ausgeben

⚠️ **Vertraulichkeitshinweis:** Die vollständige Mandatsnotiz nicht in ein breit zugängliches Ticket (Jira/Linear) einstellen — Postings in Kanäle außerhalb des Mandatsgeheimniskreises können den Schutz aufheben.

**Ausgabe 1 — Vollständiger Prüfvermerk (intern/mandatsgeschützt):** Vollständige Analyse aus Schritt 5: Ergebnis, Befunde nach Kategorie mit Risikobegründung, Maßnahmenplan, Eskalationen. Nur an Personen innerhalb des Mandatsgeheimniskreises verteilen.

**Ausgabe 2 — Bereinigter Ticket-Kommentar (SICHER FÜR TRACKER).** Nach dem Vermerk mit einem klaren `---`-Trenner und der Überschrift `## SICHER FÜR TRACKER (nicht mandatsgeschützt)` einen kurzen Kommentarblock ausgeben, der NUR enthält:
- **Launch-Status:** Grün / Gelb / Rot
- **Bedingungen als Maßnahmeneinträge:** jede Bedingung als Handlungsanweisung an PM/Technik, ohne rechtliche Begründung
- **Frist** und **Verantwortlicher** je Bedingung

Der bereinigte Block enthält weder rechtliche Begründungen noch interne Überlegungen, keine Normenverweise, keine Eskalationsnotizen.

## Ausgabeformat

Prüfvermerk im internen Format gemäß CLAUDE.md. Falls kein Hausformat vorgegeben, Standard aus Schritt 5 verwenden. Immer beide Ausgaben erzeugen: vollständiger Vermerk und bereinigter Tracker-Kommentar.

## Beispiel

**Sachverhalt:** Neues Haushaltsgerät mit WLAN-Schnittstelle soll in Deutschland und Österreich auf den Markt gebracht werden.

**Beispielhafte Befunde:**
- **Kategorie 1 (Produktsicherheit/CE):** CE-Kennzeichnung nach RED RL 2014/53/EU erforderlich; Konformitätsbewertungsverfahren (Selbsterklärung nach Modul A) noch nicht abgeschlossen — **Blocker**.
- **Kategorie 3 (Kennzeichnung):** Betriebsanleitung liegt nur auf Englisch vor; § 3 Abs. 2 Nr. 4 ProdSG verlangt Unterlagen in der Amtssprache des Bestimmungslands — **Blocker** (Übersetzung DE/AT erforderlich).
- **Kategorie 7 (Marketing):** Behauptung „das sicherste Gerät auf dem Markt" ohne Nachweis — potenziell irreführend nach § 5 UWG — Weiterleitung an `werbeaussagen-pruefung`.

## Risiken und typische Fehler

- **CE-Kennzeichnung ohne vollständiges Konformitätsbewertungsverfahren:** Häufiger Fehler bei Start-ups. § 5 ProdSG (GPSR-Umsetzung) verbietet das Inverkehrbringen nicht konformer Produkte; Bußgeld und Marktrücknahme durch BAuA möglich.
- **Fehlende oder unvollständige Betriebsanleitung in Landessprache:** Verletzt § 3 Abs. 2 ProdSG, führt zu Instruktionsfehler i. S. d. § 1 Abs. 2 Nr. 2 ProdHaftG (haftungsrelevant).
- **Vernachlässigung der GPSR-Meldepflichten:** Art. 9 GPSR verpflichtet Hersteller zu unverzüglicher Meldung unsicherer Produkte an Marktüberwachungsbehörden; Unterlassen ist Ordnungswidrigkeit.
- **Produkthaftungsrisiko durch unklare Gebrauchsanweisung:** BGH, Urt. v. 02.02.2021 – VI ZR 1234/19, NJW 2021, 3458: Instruktionsfehler kann Produkthaftung auslösen, auch wenn das Produkt technisch einwandfrei ist. `[verify]`
- **Verwechslung von CE-Pflicht und CE-freier Produktkategorie:** Nicht jedes Produkt unterliegt CE-Pflicht; Fehlkennzeichnung (CE ohne einschlägige RL) ist ebenfalls unzulässig.
- **KI-Komponenten ohne Risikobewertung nach KI-VO:** KI-VO (EU) 2024/1689 gilt ab 02.08.2026 für Hochrisiko-KI-Systeme; frühzeitige Klassifizierung verhindern.

## Quellenpflicht

Jede Norm, Entscheidung oder Behördenaussage im Prüfvermerk muss belegt sein:

- **Primärquellen:** EUR-Lex (Verordnungen, Richtlinien), BAuA-Website, BfArM (Medizinprodukte), BVL (Lebensmittel)
- **Rechtsprechung:** juris, beck-online, NJW, GRUR, Gewerblicher Rechtsschutz und Urheberrecht (GRUR-RS)
- **Kommentare:** Klindt ProdSG, Kullmann ProdHaftG, Foerste/von Westphalen Produkthaftungshandbuch
- **Zitierhinweis:** Entscheidungen in der Form `BGH, Urt. v. TT.MM.JJJJ – Az., Fundstelle Rn. X`; Normen stets mit §-Zeichen und Absatz-/Nummerierungsangabe

Quellen, die nur aus dem Modellwissen stammen, sind mit `[verify]` zu kennzeichnen. Pinpoint-Zitate (konkrete Randnummern) tragen `[verify-pinpoint]`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
