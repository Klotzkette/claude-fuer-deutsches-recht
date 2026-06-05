---
name: vertragsausfueller-vaf-quality-gate-redline-qa
description: "VAF Quality Gate Redline QA: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# VAF Quality Gate Redline QA

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **VAF Quality Gate Redline QA** im Plugin Vertragsausfüller. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vaf-quality-gate` | Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln erfolgen. §§ 305-309 BGB AGB-Recht, §§ 125 ff. BGB Formvorraussetzungen. Prüfraster alle Pflichtfelder befüllt, Zahlen und Fristen plausibel, AGB-Klauseln rechtlich zulässig, Anlagen vollständig, Track-Changes-Bestätigung vorhanden. Output Qualitaets-Ampel mit Freigabe oder Liste zu behebender Fehler. Abgrenzung zu Plausibilitaetscheck für Teilprüfung und zu Clean-Output. |
| `vaf-redline-qa` | Redline und Track-Changes-Fassung prüfen: Anwendungsfall Gegenentwurf oder überarbeitete Fassung liegt vor und soll auf Vollständigkeit versteckte Änderungen Formatbrüche und ungeklärte Klauselentscheidungen geprüft werden. §§ 145 ff. BGB Vertragsänderungen, §§ 305 ff. BGB AGB-Änderungskontrolle. Prüfraster Ausgangsfassung und überarbeitete Fassung identifiziert, alle Track-Changes-Status klar, materielle Änderungen gegen Freigaben geprüft. Output QA-Protokoll mit Änderungsübersicht und offenen Klauselentscheidungen. Abgrenzung zu Clean-Output und zu Klauselentscheidung. |
| `vaf-rueckfrageninterview` | Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Prüfraster offene Pflichtfelder nach Priorität sortieren, Freitext oder Tabellen-Eingabe anbieten, Platzhalter-Schnellversion bei Zeitdruck, Teilantworten aus vorhandenen Dokumenten verwerten. Output vollständig ausgefülltes Feldinventar oder Schnell-Entwurf mit markierten Platzhaltern. Abgrenzung zu Feldinventar für Vorbereitung und zu Kommandocenter. |

## Arbeitsweg

Im Plugin Vertragsausfüller gilt für **VAF Quality Gate Redline QA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vaf-quality-gate`

**Fokus:** Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln erfolgen. §§ 305-309 BGB AGB-Recht, §§ 125 ff. BGB Formvorraussetzungen. Prüfraster alle Pflichtfelder befüllt, Zahlen und Fristen plausibel, AGB-Klauseln rechtlich zulässig, Anlagen vollständig, Track-Changes-Bestätigung vorhanden. Output Qualitaets-Ampel mit Freigabe oder Liste zu behebender Fehler. Abgrenzung zu Plausibilitaetscheck für Teilprüfung und zu Clean-Output.

# Quality Gate — Vertragsausfueller


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

## 2. `vaf-redline-qa`

**Fokus:** Redline und Track-Changes-Fassung prüfen: Anwendungsfall Gegenentwurf oder überarbeitete Fassung liegt vor und soll auf Vollständigkeit versteckte Änderungen Formatbrüche und ungeklärte Klauselentscheidungen geprüft werden. §§ 145 ff. BGB Vertragsänderungen, §§ 305 ff. BGB AGB-Änderungskontrolle. Prüfraster Ausgangsfassung und überarbeitete Fassung identifiziert, alle Track-Changes-Status klar, materielle Änderungen gegen Freigaben geprüft. Output QA-Protokoll mit Änderungsübersicht und offenen Klauselentscheidungen. Abgrenzung zu Clean-Output und zu Klauselentscheidung.

# Redline-QA

## Triage zu Beginn

1. Welche Fassung ist Ausgangsdokument und welche ist die überarbeitete Fassung?
2. Sind alle Track-Changes-Markierungen angenommen oder abgelehnt oder noch ausstehend?
3. Entsprechen alle materiellen Änderungen freigegebenen Klauselentscheidungen?
4. Hat der Mandant die Herausgabe der Redline ausdrücklich bestätigt?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 119 ff. BGB — Anfechtung (bei verdeckten Änderungen im Redline-Prozess)
- § 241 Abs. 2 BGB — Nebenpflicht zur Rücksichtnahme (kein Einbringen unbesprochener Änderungen)
- § 307 BGB — Transparenzgebot (bei Änderungen per AGB)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill kontrolliert Änderungsfassungen vor Herausgabe. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Jede Änderung einem Feld, einer Rückfrage oder einer Klauselentscheidung zuordnen.
2. Formatbrüche, doppelte Leerzeichen, zerstörte Nummerierung und Anlagenverweise prüfen.
3. Materielle Abweichungen vom Term Sheet separat hervorheben.
4. Freigabe erst empfehlen, wenn Clean- und Redline-Fassung denselben Stand haben.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

---

<!-- AUDIT 27.05.2026
Bundle: bundle_047.json
-->

## 3. `vaf-rueckfrageninterview`

**Fokus:** Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Prüfraster offene Pflichtfelder nach Priorität sortieren, Freitext oder Tabellen-Eingabe anbieten, Platzhalter-Schnellversion bei Zeitdruck, Teilantworten aus vorhandenen Dokumenten verwerten. Output vollständig ausgefülltes Feldinventar oder Schnell-Entwurf mit markierten Platzhaltern. Abgrenzung zu Feldinventar für Vorbereitung und zu Kommandocenter.

# Rückfrageninterview


## Triage zu Beginn

1. Welche Felder sind noch offen — Pflichtfelder oder optionale Felder?
2. Sind die Rückfragen nach Priorität geordnet (Parteien, Gegenstand, Preis, Frist, Risiko)?
3. Hat der Mandant Zeit für ein ausführliches Interview oder soll ein Schnell-Entwurf mit Platzhaltern erstellt werden?
4. Gibt es bereits Dokumente (E-Mail, Term Sheet) die Teilantworten enthalten?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 280 BGB — Schadensersatz wegen Pflichtverletzung (Beratungshaftung)
- §§ 675, 611 BGB — Anwaltsvertrag (Dienstvertrag mit Geschäftsbesorgung)
- § 3 BRAO — Anwalt als unabhängiger Berater

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill füllt Datenlücken ohne den Nutzer zu überfordern. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Maximal zehn wichtigste Rückfragen zuerst stellen.
2. Fragen nach Parteien, Gegenstand, Geld, Frist, Risiko und Anlagen gruppieren.
3. Unbekannte Werte als Platzhalter mit Warnung stehen lassen, wenn der Nutzer schnell einen Entwurf will.
4. Nach jeder Antwort aktualisieren, welche Felder nun freigegeben sind.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 394/12 (claimed: Verlaesslichkeit von Auskuenften, NJW 2014, 2360): NOT_FOUND auf dejure.org. NJW 2014, 2360 gehoert zu BGH I ZR 169/12 (BearShare – Filesharing-Stoererhaftung) – thematisch unverwandt. Eintrag geloescht. -->
