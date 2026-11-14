---
name: fachanwalt-iwr-cisg-anwendbarkeit
description: "Für CISG-Anwendbarkeit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# CISG-Anwendbarkeit

## Zweck

Prüfung, ob das UN-Kaufrecht (CISG) auf grenzüberschreitenden Warenkauf anwendbar ist.

## 1) Eingangs-Abfrage

1. Beide Parteien-Sitze in CISG-Staaten?
2. Warenkauf zwischen Unternehmern (B2B)?
3. Vertraglicher Ausschluss CISG?
4. Reklamation / Mangelpunkt aktuell?
5. Anwendbares Kollisions-Recht (Rom I-VO)?

## 2) Sachlicher Anwendungsbereich Art. 1 CISG

- **Warenkauf** zwischen Unternehmern aus verschiedenen Vertragsstaaten
- Ausschluesse Art. 2: Konsum-Kaeufe, Versteigerung, Wertpapiere, Schiff, Luftfahrzeug
- Art. 3: Werk-Lieferungs-Verträge (wenn Material vom Kaeufer: kein CISG)

## 3) Raeumlicher Anwendungsbereich

### Direkt Art. 1 Abs. 1 a) CISG

- Beide Parteien-Sitze in CISG-Staat
- Aktueller Stand (12/2024): 97 Vertragsstaaten (u. a. DE, A, CH, USA, China, Japan, Brasilien; Ruanda seit 01.10.2024).
- Offizielle Liste UNCITRAL: https://uncitral.un.org/en/texts/salegoods/conventions/sale_of_goods/status — vor Verwendung tagesaktuell pruefen.

### Indirekt Art. 1 Abs. 1 b) CISG

- Kollisions-Recht führt zu CISG-Staat
- Beispiel: DE-Verkaeufer, NIC (nicht-Vertragsstaat)-Kaeufer; Rom I-VO führt zu DE -> CISG anwendbar

## 4) Ausschluss Art. 6 CISG

### Voraussetzung

- **Eindeutiger** Vertraglicher Ausschluss
- "Es gilt deutsches Recht" -> CISG bleibt (Teil deutschen Rechts)
- Korrekt: "Es gilt deutsches Recht unter Ausschluss des UN-Kaufrechts (CISG)"

### Strategie

- Bei Verkaeufer-AGB: meist Ausschluss empfohlen (klare BGB-Anwendung)
- Bei Kaeufer-Bestellung: CISG-Anwendung oft Vorteil

## 5) Mängelpflichten Art. 35-39 CISG

### Art. 35 CISG — Vertragsgemäße Ware

- Wesentliche Eigenschaften
- Hinweis-Pflichten

### Untersuchungspflicht Art. 38 CISG

- Kaeufer muss Ware so bald wie möglich untersuchen

### Ruegepflicht Art. 39 CISG

- **Innerhalb angemessener Frist** nach Entdeckung
- Bei Versäumnis: Verlust der Gewaehrleistungs-Rechte

### Spaetestens Art. 39 II CISG

- 2 Jahre ab Übergabe der Ware

## 6) Workflow CISG-Prüfung

### Schritt 1 — Parteien-Sitze

- IHK-Verzeichnis CISG-Vertragsstaaten
- Aktuelle Liste: https://uncitral.un.org

### Schritt 2 — Vertragsausschluss-Prüfung

- AGB lesen
- Explizite Ausschluss-Klausel suchen

### Schritt 3 — Anwendbares Kollisions-Recht

- Rom I-VO Art. 4
- Bei Warenkauf: Verkaeufer-Recht typisch
- CISG vorrangig vor nationalem Kaufrecht

### Schritt 4 — Sachverhaltsanalyse

- Mängel-Stand
- Ruege-Zeitpunkt vs. Entdeckung
- Untersuchung erfolgt?

## 7) Vergleich CISG vs. BGB

| Punkt | CISG | BGB |
|---|---|---|
| Mängelrecht | Art. 35-44 | §§ 434 ff. |
| Ruegepflicht | Pflicht, 1 Monat | nur § 377 HGB im Handelskauf |
| Verjaehrung | 4 Jahre Art. 39 II analog | 2 Jahre § 438 |
| Verzugszinsen | nicht geregelt -> nationales Recht | § 288 BGB |
| Vertragsstrafe | nicht geregelt | § 339 BGB |

## 8) Typische Fehler

1. **"Deutsches Recht" als CISG-Ausschluss missverstanden**
2. **Ruegefrist verpasst** -> Verlust der Mängelrechte
3. **Untersuchungs-Pflicht missachtet** -> Verlust
4. **Bei Werk-Lieferung CISG faelschlich angewendet** (Art. 3)

## 9) BGH-Linien


## Anschluss

- `fachanwalt-iwr-brussels-ia-zustaendigkeit` — bei Forum-Frage
- `cisg-pruefen` (Vollplugin-Skill) — vertiefte Prüfung
- `incoterms-und-gefahruebergang` — bei Lieferungs-Risiko

## Vertiefung: Triage und Output-Template CISG-Anwendbarkeit

### Triage — Bevor losgelegt wird, klaere:

1. Haben beide Parteien Niederlassung in CISG-Vertragsstaaten? → Art. 1 Abs. 1 lit. a CISG
2. Fuehrt IPR-Verweisung in CISG-Staat? → Art. 1 Abs. 1 lit. b CISG (von DE nicht erklaert; kein Problem)
3. Ist Warenkauf (kein Verbraucherkauf, keine Dienstleistung, kein Strom)?
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Ergaenzende Leitsaetze


### Output-Template Checkliste CISG-Anwendbarkeit
**Adressat:** Intern (Kaltstart) — Tonfall: schnell, checkboxorientiert

```
CHECKLISTE CISG-ANWENDBARKEIT
===================================
[ ] Parteien haben Sitz in verschiedenen Staaten
[ ] Beide Staaten Vertragsstaaten CISG
[ ] Gegenstand: Kauf von Waren (nicht Dienstleistungen)
[ ] Kein Verbraucherkauf
[ ] CISG nicht ausgeschlossen (Art. 6 CISG)
===================================
ERGEBNIS:
[ ] CISG ANWENDBAR
[ ] CISG NICHT ANWENDBAR → Anwendbares Recht nach Rom I
```


<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

