---
name: aufsichts-feed-monitor
description: "Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist Handlungsbedarf Meldepflicht. Output: Monitoring-Bericht relevante Aenderungen Handlungsliste. Abgrenzung: nicht für tiefe Regulierungsanalyse (stellungnahmen)."
---

# Regulatorischer Feed-Watcher

## Zweck

Die Skill ruft konfigurierte regulatorische Quellen ab, filtert nach Wesentlichkeit und
gibt aus, was seit dem letzten Lauf neu ist. Der Filter ist der eigentliche Mehrwert —
ungefilterter Rohinput ist Rauschen. Quellen: Bundesgesetzblatt (BGBl.), Amtsblatt der
EU (ABl. EU), EUR-Lex, BaFin-Rundschreiben, BSI-Verlautbarungen, EuGH-/BGH-Newsletter,
Bundesanzeiger, BMJ-Referentenentwürfe, Bundesrat-Drucksachen. Themen: Finanzaufsicht,
IT-Sicherheit, Datenschutz, KI-Regulierung (EU-KI-VO), ESG/CSRD.

## Eingaben

- **Watchlist:** Welche Behörden und Rechtsgebiete sind zu überwachen?
- **Wesentlichkeitsschwellenwert:** Wie ist Materialität konfiguriert?
- **Prüfzeitraum:** Seit wann? (Standard: seit letztem Lauf; alternativ `--since DATUM`)
- **Quellen:** Konfigurierte Feeds, RSS-Adressen, Dienste.
- **Alternativ:** Manuell eingefügter Regulierungstext zur Einzelklassifikation.

## Rechtlicher Rahmen

### Kernvorschriften

- **BGBl.** — amtliches Verkündungsblatt; maßgeblich für Inkrafttreten von Normen.
- **ABl. EU, Reihe L + C** — verbindliche EU-Rechtsakte und Leitlinien.
- **BaFin-Rundschreiben** (z. B. MaRisk BA 2023, BAIT, ZAIT) — konkretisieren
  aufsichtsrechtliche Anforderungen; §§ 6, 25b KWG, §§ 6, 23 VAG, §§ 6 ff. WpHG.
- **BSI** — Technische Richtlinien und Kritis-Verlautbarungen (§§ 8a ff. BSIG).
- **EU-KI-VO (VO (EU) 2024/1689)** — Hochrisiko-Klassifikation, Konformitätspflichten.
- **CSRD (RL (EU) 2022/2464)** — nichtfinanzielle Berichterstattung, ESRS-Standards.
- **Art. 20 Abs. 3 GG** — Rechtsstaatsprinzip, Normenklarheit; Maßstab für die
  Bewertung behördlicher Verlautbarungen ohne formelle Ermächtigungsnorm.

### Leitentscheidungen / Aktualitäts-Anker

Stand 05/2026. Vor Verwendung im Schriftsatz live verifizieren — keine Aktenzeichen aus Modellwissen.

- EuGH, Urt. v. 13.02.2025 — C-383/23 (ILVA) — DSGVO-Bußgelder können auf gesamten Konzernumsatz bezogen werden; "Unternehmen" im wettbewerbsrechtlichen Sinne — relevant für Monitoring nationaler Bußgeldpraxis.
- EuGH, Urt. v. 02.12.2025 — C-492/23 (Russmedia) — DSGVO geht DSA vor; kein Provider-Privileg bei DSGVO-Verstößen — relevant für Plattform-Compliance-Monitoring.
- EuGH, Urt. v. 19.03.2026 — C-526/24 (Brillen Rottler) — Erstmaliger DSGVO-Auskunftsantrag kann rechtsmissbräuchlich sein.
- BVerfG-Linien zu Wesentlichkeit und Normenklarheit (BVerfGE 33, 125; 49, 89 — Kalkar) im Mandat über [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) live verifizieren.
- DORA-Aktualisierungen 2025/2026: ESA-Liste kritischer IKT-Drittdienstleister (November 2025); BaFin DORA-Informationsregister-Frist 09.–30.03.2026.
- AMLR (EU) 2024/1624 — Anwendbarkeit ab 10.07.2027; AMLA-Behörde mit Sitz in Frankfurt seit 01.07.2025 operativ.
- KI-VO (EU) 2024/1689 — Verbote anwendbar seit 02.02.2025; GPAI ab 02.08.2025; Hochrisiko-KI-Hauptanwendung ab 02.08.2026; Sicherheitsbauteile ab 02.08.2027.

### Kommentare

- `Sachs (Hrsg.), GG, 10. Aufl. 2021, Art. 20 Rn. 78 ff.` — Rechtsstaatsprinzip
  und Normenklarheit als Bewertungsmaßstab für behördliche Verlautbarungen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
  Rechtsetzungskompetenzen; relevant für Verbindlichkeitsgrad von BaFin-Rundschreiben.
- `Schwennicke/Auerbach (Hrsg.), KWG/CRR, 4. Aufl. 2022, § 6 KWG Rn. 5 ff.`
  — Praxis der BaFin-Verlautbarungen und deren Rechtswirkung.

## Ablauf

### Schritt 0: Lückenprüfung

Watchlist und Quellkonfiguration gegen den internen Quellkatalog prüfen. Besteht eine
offensichtliche Lücke (z. B. "BaFin" in der Watchlist, aber weder Bundesanzeiger noch
BaFin-Journal konfiguriert), einmalig hinweisen — nicht wiederholen, wenn die Lücke
bekannt und akzeptiert ist.

### Schritt 1: Abruf

| Quelle | Inhalte |
|---|---|
| BGBl. (bgbl.de) | Gesetze, Verordnungen |
| ABl. EU / EUR-Lex | EU-Rechtsakte, konsolidierter Bestand |
| BaFin (bafin.de/RSS) | Rundschreiben, Merkblätter, Allgemeinverfügungen |
| BSI (bsi.bund.de) | Technische Richtlinien, Kritis-Warnungen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich |
| BMJ | Referentenentwürfe, Pressemitteilungen |
| Bundesrat | Drucksachen, Stellungnahmen |
| Bundesanzeiger | Behördenbekanntmachungen |

Kostenpflichtige Dienste (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang Premium, Wolters Kluwer) werden genutzt,
wenn konfiguriert. Duplikate ebenenübergreifend entfernen.

**Keine stille Ergänzung.** Bei wenigen Treffern keine eigenständige Webrecherche —
Optionen dem Nutzer vorlegen (Zeitfenster, andere Quelle, Websuche mit Prüfvermerk,
stoppen). Die Entscheidung trifft der Nutzer.

**Quellenkennung** (nie entfernen): `[BGBl.]`, `[ABl. EU]`, `[BaFin-RSS]`, `[BSI]`,
`[Websuche — prüfen]`, `[Modell-Wissen — prüfen]`, `[manuell eingegeben]`.
Sekundärquellen (Kanzlei-Newsletter, Fachportale) zusätzlich mit `[Sekundärquelle]`
kennzeichnen; Materialitätsstufe absenken bis zur Primärquellenbestätigung.

### Schritt 2: Klassifikation

| Eintragstyp | Einordnung |
|---|---|
| Gesetz / Verordnung (final) | Immer wesentlich |
| Referentenentwurf / Konsultationsdokument | Prüfenswert — Kommentierungsfrist festhalten |
| Enforcement / Bußgeldbescheid | Sektorentreffer → wesentlich; Themennähe → prüfenswert |
| Leitlinien / Merkblätter | Prüfenswert |
| Pressemitteilungen / Statements | Zur Kenntnis / überspringen |

Referentenentwürfe und Konsultationen nie als "immer wesentlich" einstufen — noch keine
Compliance-Pflicht. Im Eintrag explizit vermerken: "Vorstufe. Kommentierungsfrist
[Datum]. Noch keine Compliance-Lücke."

### Schritt 3: Anreicherung

Für jeden Eintrag oberhalb "Zur Kenntnis": einzeilige Zusammenfassung + Relevanzhinweis
+ Link + Inkrafttreten bzw. Kommentierungsfrist. "Zur Kenntnis"-Einträge: nur Anzahl.

## Ausgabeformat

```
## Regulatorischer Feed-Check — [Datum]
Zeitraum: [letzter Lauf] – [jetzt] | Quellen: [...] | Einträge: [N]

### Kurzfazit
[N Einträge erfordern Handlung bis [Datum] — Top 3: X, Y, Z]

### Immer wesentlich
**[Behörde] — [Titel]**
[Zusammenfassung]. [Relevanz]. In Kraft: [Datum]. [Link] [Quellenkennung]
→ Empfehlung: [nächster Schritt]

### Prüfenswert
**[Behörde] — [Titel]**
[Zusammenfassung]. Kommentierungsfrist: [Datum]. [Link] [Quellenkennung]

### Zur Kenntnis
[N] Einträge — [Titelliste mit Links]

---
Letzter Prüfzeitpunkt: [Zeitstempel]
Fundstellen vor Verwendung verifizieren. Abgleich mit Primärquelle erforderlich.
```

Zusätzlich Dateiausgabe (Markdown) unter konfiguriertem Pfad oder
`~/regulatorisches-digests/reg-digest-YYYY-MM-DD.md`; bei mehreren Tagesläufen
anhängen statt überschreiben.

## Beispiel

**Watchlist:** "BaFin — Zahlungsdienste", "EU — KI-Verordnung". Letzter Lauf: 01.07.2024.

BaFin-RSS liefert Merkblatt zu § 25b KWG-Auslagerungen → "Prüfenswert" (Leitlinie).
EUR-Lex liefert delegierte Verordnung zur KI-VO → "Immer wesentlich" (EU-Rechtsakt).

```
### Immer wesentlich
**EU — Delegierte Verordnung (EU) 2024/XXX zur KI-Verordnung**
Konkretisiert Konformitätsbewertung für Hochrisiko-KI (Art. 43 KI-VO, Annex III Nr. 5).
In Kraft: 01.08.2024. [ABl. EU L 2024/XXX] [ABl. EU]
→ KI-Inventar gegen Hochrisiko-Katalog prüfen; ggf. Konformitätsbewertung einleiten.
```

## Risiken und typische Fehler

- **Sekundärquelle als Primärquelle verwenden:** Kanzlei-Newsletter berichten über
  Entscheidungen, sind aber nicht die Entscheidung. Immer auf BGBl., ABl. oder
  Behördenwebsite verweisen.
- **Referentenentwurf als geltendes Recht einstufen:** Klare Kennzeichnung als Vorstufe.
- **Kommentierungsfristen übergehen:** Fristen sind real und oft kurz — immer im Tracker.
- **Verbindlichkeitsgrad verwischen:** BaFin-Rundschreiben sind keine Gesetze.
  Unterschied Gesetz / VO / Leitlinie / Merkblatt in der Ausgabe erkennbar halten.
- **Stille Ergänzung durch Websuche:** Ohne Rückfrage unzulässig.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jeder Eintrag muss enthalten: Behörde, Dokumenttyp, Datum, Direktlink zur Primärquelle,
Quellenkennung und ggf. Kommentierungsfrist. Zitierweise Rechtsprechung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Zitierweise Kommentare:
`Sachs/Sachs, GG, 10. Aufl. 2021, Art. 20 Rn. 78`
