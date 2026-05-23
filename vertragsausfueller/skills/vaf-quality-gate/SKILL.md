---
name: vaf-quality-gate
description: "Letzte Pruefschleuse vor Ausgabe eines Vertragsentwurfs. Sucht fehlende Werte, ungeklaerte Wahlklauseln, Rechenfehler, Normierungsprobleme, Anlagenluecken, Freigabehindernisse, Track-Changes-Konflikte. Mit Pruefraster Stop-Kriterien Eskalations-Matrix Beispielprotokollen. Originaldateien nie ueberschrieben. Track Changes nur nach ausdruecklicher Bestaetigung."
---

# Quality Gate — Vertragsausfueller

## Zweck

Letzte Schleuse, bevor ein Vertragsentwurf, eine Redline oder ein Track-Changes-Dokument an den Mandanten oder die Gegenseite herausgeht. Verhindert sechs typische Fehlerklassen: leere Pflichtfelder, ungeklaerte Wahlklauseln, Rechenfehler, normwidrige Formulierungen, fehlende Anlagen, fehlende Freigaben. Liefert ein Pruefprotokoll mit Go / Go mit Warnungen / No-go.

Arbeitet freistehend im Vertragsausfueller-Plugin, setzt keine anderen Plugins voraus.

## 1) Eingangs-Trigger

Der Quality Gate startet automatisch oder auf Anfrage, wenn vorliegt:

- hochgeladene Word-Vorlage oder alter Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline / Track Changes
- Wunsch nach Bilingual-Fassung (DE/EN)

## 2) Sechs-stufiges Pruefraster

### Stufe 1 — Pflichtfeld-Vollstaendigkeit

Pruefen, ob alle Pflichtfelder belegt sind:

| Pflichtfeld | Typisch | Stopper-Frage |
|---|---|---|
| Parteien | Name, Anschrift, Vertretungsbefugnis | Ist die Vertretung dokumentiert? |
| Vertragsgegenstand | konkrete Leistung | Eindeutig im Wortlaut? |
| Hauptleistungspflichten | Lieferung, Zahlung, Frist | Konkret und vollstreckbar? |
| Zeitliche Geltung | Anfang, Ende, Verlaengerung | Datum und Dauer im Wortlaut? |
| Vertragsstrafe / Sicherheiten | falls vereinbart | Hoehe und Voraussetzung? |
| Anwendbares Recht / Gerichtsstand | bei B2B blank lassen oder DE | Wahl getroffen? |
| Schriftform / elektronische Signatur | je nach Norm | Form gewahrt? |
| Unterschrift / Datum | Pflichtfeld | Leerzeichen markiert? |

**Stopper-Kriterium**: Ein leeres Pflichtfeld -> No-go.

### Stufe 2 — Platzhalter-Reste

Pruefen, ob alle `[...]`, `XXX`, `TBD`, `noch zu klaeren`, `tba`, `t.b.a.`, `‹...›` aufgeloest sind. Auch in Fussnoten, Anlagen-Verweisen und unterschriftsblocken.

**Stopper-Kriterium**: Ein Platzhalter im Hauptteil -> No-go. In Anlagen-Verweis -> Warnung mit Hinweis.

### Stufe 3 — Zahlen- und Fristenlogik

Pruefen:

- Sind alle Zahlen mathematisch konsistent (Hauptsumme = Summe der Teilbetraege)?
- Sind Prozentsaetze konsistent (z.B. Mwst. + Brutto = Netto + Mwst.)?
- Sind alle Fristen kalendermaessig korrekt (z.B. „14 Tage ab Rechnungsdatum" konsistent mit „Faelligkeit 14 Tage nach Rechnung")?
- Sind die Fristen rechtswirksam (Verbraucher: Mindestlaufzeiten? Widerrufsrecht?)?
- Stimmt das Schluss-Datum mit der Vertragsdauer?

**Stopper-Kriterium**: Rechenfehler -> No-go. Frist juristisch problematisch -> Warnung mit Klauselvorschlag.

### Stufe 4 — Normwidrige Formulierungen

Pruefen gegen typische AGB-Fallen und Klauselverbote:

| Typ | Norm | Beispiel-Fall |
|---|---|---|
| Verzugszinsen ueber Basis + 9 % bei B2C | Paragraf 288 IV BGB | „12 % Verzugszinsen" -> Verstoss |
| Schadensersatzbeschraenkung auf Eigenleistung | Paragraf 309 Nr. 7a, b BGB | Ausschluss fuer Personenschaeden -> nichtig |
| Schiedsgerichtsklausel ohne Klarheit | Paragraf 1031 ZPO | Verbraucher ohne Sondervereinbarung -> nichtig |
| Lange Bindungsfrist bei Verbrauchern | Paragraf 309 Nr. 9 BGB | Verlaengerung > 1 Jahr automatisch -> Risiko |
| Salvatorische Klausel als Lueckenfueller | BGH NJW 2009, 2671 Rn. 13 | wirkt nicht heilend bei AGB |

**Stopper-Kriterium**: Bei klarem Klauselverstoss B2C -> No-go. Bei B2B-Streitfall -> Warnung mit Risiko-Hinweis.

### Stufe 5 — Anlagen-Luecken

Pruefen:

- Sind alle im Vertragstext genannten Anlagen vorhanden?
- Sind die Anlagen mit derselben Bezeichnung versehen (Anlage 1, Annex 1, A1)?
- Sind die Anlagen vom Auftraggeber bestaetigt?
- Bei AGB als Anlage: sind die AGB einbezogen (Bezugnahme im Vertragstext)?

**Stopper-Kriterium**: Genannte Anlage fehlt -> Warnung mit Auflistung. Bei AGB-Bezugnahmemangel -> No-go.

### Stufe 6 — Freigabe-Hindernisse

Pruefen:

- Ist die Vertragsart vom Mandanten freigegeben (z.B. „Generalvollmacht" benoetigt Sonderfreigabe)?
- Ist die Vertretungsbefugnis dokumentiert?
- Bei Hoehen-Schwellen (z.B. Streitwert > 100.000 EUR): Gesellschafterbeschluss?
- Bei sensiblen Klauseln (z.B. Wettbewerbsverbot, Geheimhaltung mit Vertragsstrafe): explizite Freigabe?

**Stopper-Kriterium**: Fehlende Freigabe -> No-go.

## 3) Track-Changes-Vorpruefung

Bei Wunsch nach Redline / Track Changes:

- [ ] Ist die Ausgangsfassung eindeutig (welcher Vertragsstand wird als Basis genommen)?
- [ ] Ist die Vergleichsfassung freigegeben (kein Entwurfsstand)?
- [ ] Sind Track Changes vom Mandanten **ausdruecklich** bestaetigt?
- [ ] Ist die Track-Changes-Funktion konsistent eingesetzt (keine Mischung Hand-Markierungen + Word-Tracker)?

**Stopper-Kriterium**: Keine ausdrueckliche Bestaetigung -> No-go.

## 4) Ausgabe-Format Quality-Gate-Protokoll

```
QUALITY-GATE-PROTOKOLL
======================
Vertrag: [Bezeichnung]
Stand: [Datum, Uhrzeit]
Vorpruefer: [Plugin]

PFLICHTFELDER
[Ergebnis: OK / Lueckend]
Luecken: ...

PLATZHALTER
[Ergebnis: OK / Reste vorhanden]
Reste: Zeile XX [Text]

ZAHLENLOGIK
[Ergebnis: OK / Fehler]
Fehler: Hauptsumme = X EUR, Summe Teilbetraege = Y EUR

NORMWIDRIGE FORMULIERUNGEN
[Ergebnis: OK / Risiko / Verstoss]
Hinweise: ...

ANLAGEN
[Ergebnis: OK / Lueckend]
Fehlend: Anlage 3 (im Vertragstext genannt)

FREIGABE
[Ergebnis: OK / Fehlend]
Offen: ...

GESAMT-AMPEL: GRUEN / GELB / ROT
Empfehlung: Go / Go mit Warnungen / No-go
```

## 5) Eskalations-Matrix

| Ampel | Konsequenz | Naechster Schritt |
|---|---|---|
| GRUEN (Go) | Vertrag bereit zur Ausgabe | Bei Wunsch: Track Changes auf Bestaetigung |
| GELB (Go mit Warnungen) | Vertrag ausgebbar, aber Risiko | Mandanten ueber Warnung informieren, Bestaetigung |
| ROT (No-go) | Vertrag nicht ausgebbar | Rueckfrage an Mandanten, Klauselvorschlag |

## 6) Leitplanken

- **Originaldateien werden nie ueberschrieben.** Es entsteht stets eine neue Datei mit Suffix `_qg_yyyymmdd` o.ae.
- **Track Changes, Redline oder Vergleichsfassung nur nach ausdruecklicher Rueckfrage und Bestaetigung.** Nicht eigenmaechtig.
- **Offene Werte bleiben sichtbar** in der ausgegebenen Datei (z.B. als `[noch zu klaeren: ...]`); sie werden nicht erfunden.
- **Juristische Wahlentscheidungen werden erklaert und protokolliert** in der Vertragsdatenmatrix und im Rueckfragen-Protokoll.
- **Risiken werden konkret benannt** (Norm, Folge, Vorschlag), nicht pauschalisiert.

## 7) Typische Fehler beim Quality-Gate

1. **Platzhalter im Footer uebersehen.** Pruefe explizit auch Kopf-/Fusszeilen.
2. **Anlagen-Verzeichnis unvollstaendig.** Bei AGB-Bezug ist auch die Empfangsbestaetigung Anlage.
3. **Track Changes ohne Bestaetigung.** Klassischer Compliance-Fehler.
4. **Mwst.-Klausel uebersehen** (B2C: Brutto, B2B: Netto + Mwst.).
5. **Schriftform Paragraf 126 BGB nicht beachtet.** Bei langfristigen Vertraegen sicherheitshalber Schriftform.

## 8) Schnittstellen

- `vaf-vertragsdatenmatrix` — liefert die Eingabedaten
- `vaf-rueckfragen` — fuettert die ungeklaerten Punkte
- `vaf-ausfuellprotokoll` — protokolliert die Entscheidungen
- `vaf-track-changes` — nach GRUEN-Ampel und Bestaetigung
