---
name: quality-gate-redline-qa
description: "Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln erfolgen. §§ 305-309 BGB AGB-Recht, §§ 125 ff. BGB Formvorraussetzungen. Prüfraster alle Pflichtfelder befüllt, Zahlen und Fristen plausibel, AGB-Klauseln rechtlich zulässig, Anlagen vollständig, Track-Changes-Bestätigung vorhanden. Output Qualitaets-Ampel mit Freigabe oder Liste zu behebender Fehler. Abgrenzung zu Plausibilitaetscheck für Teilprüfung und zu Clean-Output im Vertragsausfueller: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Quality Gate — Vertragsausfueller

## Arbeitsbereich

Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln erfolgen. §§ 305-309 BGB AGB-Recht, §§ 125 ff. BGB Formvorraussetzungen. Prüfraster alle Pflichtfelder befüllt, Zahlen und Fristen plausibel, AGB-Klauseln rechtlich zulässig, Anlagen vollständig, Track-Changes-Bestätigung vorhanden. Output Qualitaets-Ampel mit Freigabe oder Liste zu behebender Fehler. Abgrenzung zu Plausibilitaetscheck für Teilprüfung und zu Clean-Output. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Wurde das Feldinventar vollständig ausgefüllt (vaf-feldinventar) und der Plausibilitätscheck durchgeführt (vaf-plausibilitaetscheck)?
2. Sind alle Klauselentscheidungen getroffen und protokolliert (vaf-klauselentscheidung)?
3. Ist die Ampel des Quality Gate grün oder gibt es offene No-go-Kriterien?
4. Hat der Mandant ausdrücklich Track Changes / Redline bestätigt?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 307 Abs. 1 S. 2 BGB — Transparenzgebot (Klausel muss klar und verständlich sein)
- § 139 BGB — Teilnichtigkeit (unwirksame Klausel → Gesamtvertrag nur bei separabler Klausel)
- § 306 BGB — Rechtsfolge unwirksamer AGB (dispositives Recht tritt ein)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Letzte Schleuse, bevor ein Vertragsentwurf, eine Redline oder ein Track-Changes-Dokument an den Mandanten oder die Gegenseite herausgeht. Verhindert sechs typische Fehlerklassen: leere Pflichtfelder, ungeklärte Wahlklauseln, Rechenfehler, normwidrige Formulierungen, fehlende Anlagen, fehlende Freigaben. Liefert ein Pruefprotokoll mit Go / Go mit Warnungen / No-go.

Arbeitet freistehend im Vertragsausfueller-Plugin, setzt keine anderen Plugins voraus.

## 1) Eingangs-Trigger

Der Quality Gate startet automatisch oder auf Anfrage, wenn vorliegt:

- hochgeladene Word-Vorlage oder alter Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline / Track Changes
- Wunsch nach Bilingual-Fassung (DE/EN)

## 2) Sechs-stufiges Prüfraster

### Stufe 1 — Pflichtfeld-Vollständigkeit

Prüfen, ob alle Pflichtfelder belegt sind:

| Pflichtfeld | Typisch | Stopper-Frage |
|---|---|---|
| Parteien | Name, Anschrift, Vertretungsbefugnis | Ist die Vertretung dokumentiert? |
| Vertragsgegenstand | konkrete Leistung | Eindeutig im Wortlaut? |
| Hauptleistungspflichten | Lieferung, Zahlung, Frist | Konkret und vollstreckbar? |
| Zeitliche Geltung | Anfang, Ende, Verlängerung | Datum und Dauer im Wortlaut? |
| Vertragsstrafe / Sicherheiten | falls vereinbart | Höhe und Voraussetzung? |
| Anwendbares Recht / Gerichtsstand | bei B2B blank lassen oder DE | Wahl getroffen? |
| Schriftform / elektronische Signatur | je nach Norm | Form gewahrt? |
| Unterschrift / Datum | Pflichtfeld | Leerzeichen markiert? |

**Stopper-Kriterium**: Ein leeres Pflichtfeld -> No-go.

### Stufe 2 — Platzhalter-Reste

Prüfen, ob alle `[...]`, `XXX`, `TBD`, `noch zu klaeren`, `tba`, `t.b.a.`, `'...'` aufgeloest sind. Auch in Fußnoten, Anlagen-Verweisen und unterschriftsblocken.

**Stopper-Kriterium**: Ein Platzhalter im Hauptteil -> No-go. In Anlagen-Verweis -> Warnung mit Hinweis.

### Stufe 3 — Zahlen- und Fristenlogik

Prüfen:

- Sind alle Zahlen mathematisch konsistent (Hauptsumme = Summe der Teilbetraege)?
- Sind Prozentsätze konsistent (z.B. Mwst. + Brutto = Netto + Mwst.)?
- Sind alle Fristen kalendermaessig korrekt (z.B. "14 Tage ab Rechnungsdatum" konsistent mit "Fälligkeit 14 Tage nach Rechnung")?
- Sind die Fristen rechtswirksam (Verbraucher: Mindestlaufzeiten? Widerrufsrecht?)?
- Stimmt das Schluss-Datum mit der Vertragsdauer?

**Stopper-Kriterium**: Rechenfehler -> No-go. Frist juristisch problematisch -> Warnung mit Klauselvorschlag.

### Stufe 4 — Normwidrige Formulierungen

Prüfen gegen typische AGB-Fallen und Klauselverbote:

| Typ | Norm | Beispiel-Fall |
|---|---|---|
| Verzugszinsen über Basis + 9 % bei B2C | Paragraf 288 IV BGB | "12 % Verzugszinsen" -> Verstoß |
| Schadensersatzbeschraenkung auf Eigenleistung | Paragraf 309 Nr. 7a, b BGB | Ausschluss für Personenschäden -> nichtig |
| Schiedsgerichtsklausel ohne Klarheit | Paragraf 1031 ZPO | Verbraucher ohne Sondervereinbarung -> nichtig |
| Lange Bindungsfrist bei Verbrauchern | Paragraf 309 Nr. 9 BGB | Verlängerung > 1 Jahr automatisch -> Risiko |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

**Stopper-Kriterium**: Bei klarem Klauselverstoß B2C -> No-go. Bei B2B-Streitfall -> Warnung mit Risiko-Hinweis.

### Stufe 5 — Anlagen-Lücken

Prüfen:

- Sind alle im Vertragstext genannten Anlagen vorhanden?
- Sind die Anlagen mit derselben Bezeichnung versehen (Anlage 1, Annex 1, A1)?
- Sind die Anlagen vom Auftraggeber bestätigt?
- Bei AGB als Anlage: sind die AGB einbezogen (Bezugnahme im Vertragstext)?

**Stopper-Kriterium**: Genannte Anlage fehlt -> Warnung mit Auflistung. Bei AGB-Bezugnahmemangel -> No-go.

### Stufe 6 — Freigabe-Hindernisse

Prüfen:

- Ist die Vertragsart vom Mandanten freigegeben (z.B. "Generalvollmacht" benoetigt Sonderfreigabe)?
- Ist die Vertretungsbefugnis dokumentiert?
- Bei Höhen-Schwellen (z.B. Streitwert > 100.000 EUR): Gesellschafterbeschluss?
- Bei sensiblen Klauseln (z.B. Wettbewerbsverbot, Geheimhaltung mit Vertragsstrafe): explizite Freigabe?

**Stopper-Kriterium**: Fehlende Freigabe -> No-go.

## 3) Track-Changes-Vorprüfung

Bei Wunsch nach Redline / Track Changes:

- [ ] Ist die Ausgangsfassung eindeutig (welcher Vertragsstand wird als Basis genommen)?
- [ ] Ist die Vergleichsfassung freigegeben (kein Entwurfsstand)?
- [ ] Sind Track Changes vom Mandanten **ausdruecklich** bestätigt?
- [ ] Ist die Track-Changes-Funktion konsistent eingesetzt (keine Mischung Hand-Markierungen + Word-Tracker)?

**Stopper-Kriterium**: Keine ausdrueckliche Bestätigung -> No-go.

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

| Ampel | Konsequenz | Nächster Schritt |
|---|---|---|
| GRUEN (Go) | Vertrag bereit zur Ausgabe | Bei Wunsch: Track Changes auf Bestätigung |
| GELB (Go mit Warnungen) | Vertrag ausgebbar, aber Risiko | Mandanten über Warnung informieren, Bestätigung |
| ROT (No-go) | Vertrag nicht ausgebbar | Rueckfrage an Mandanten, Klauselvorschlag |

## 6) Leitplanken

- **Originaldateien werden nie überschrieben.** Es entsteht stets eine neue Datei mit Suffix `_qg_yyyymmdd` o.ae.
- **Track Changes, Redline oder Vergleichsfassung nur nach ausdruecklicher Rueckfrage und Bestätigung.** Nicht eigenmaechtig.
- **Offene Werte bleiben sichtbar** in der ausgegebenen Datei (z.B. als `[noch zu klaeren: ...]`); sie werden nicht erfunden.
- **Juristische Wahlentscheidungen werden erklärt und protokolliert** in der Vertragsdatenmatrix und im Rückfragen-Protokoll.
- **Risiken werden konkret benannt** (Norm, Folge, Vorschlag), nicht pauschalisiert.

## 7) Typische Fehler beim Quality-Gate

1. **Platzhalter im Footer übersehen.** Pruefe explizit auch Kopf-/Fußzeilen.
2. **Anlagen-Verzeichnis unvollständig.** Bei AGB-Bezug ist auch die Empfangsbestätigung Anlage.
3. **Track Changes ohne Bestätigung.** Klassischer Compliance-Fehler.
4. **Mwst.-Klausel übersehen** (B2C: Brutto, B2B: Netto + Mwst.).
5. **Schriftform Paragraf 126 BGB nicht beachtet.** Bei langfristigen Verträgen sicherheitshalber Schriftform.

## 8) Schnittstellen

- `vaf-feldinventar` — extrahiert das Pflichtfeld-Inventar aus der Vorlage
- `vaf-termsheet-mapping` — mappt Term-Sheet-Werte auf die Feldliste
- `vaf-rueckfrageninterview` — klärt offene Punkte mit dem Mandanten
- `vaf-plausibilitaetscheck` — pre-Quality-Gate-Prüfung der Zahlenlogik
- `vaf-redline-qa` — Review von Track-Changes-Fassungen
- `vaf-clean-output` — finaler Clean-Entwurf nach GRUEN-Ampel
- `vaf-track-changes-nur-nach-frage` — Track Changes nur nach Bestätigung
