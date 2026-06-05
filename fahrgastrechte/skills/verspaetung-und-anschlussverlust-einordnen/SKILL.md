---
name: verspaetung-und-anschlussverlust-einordnen
description: "Ordnet das Stoerungsereignis rechtlich ein: Verspaetung (Art. 19 VO 2021/782 bei mindestens 60 Min Endziel), Zugausfall (Art. 18), verpasster Anschluss unter Durchgangsfahrkarte (Art. 12 Abs. 3) oder Vorverlegung. Differenzierung Fernverkehr vs SPNV (mit § 11 EVO 20 Min Schwelle). Behandelt Mehrfach-PNRs versus Einheits-PNR. Pinpoint auf Norm und Folgerechte (Wahlrecht Erstattung/Weiterreise/Entschaedigung)."
---

# Verspätung, Zugausfall oder Anschlussverlust einordnen

## Zweck

Klärt für einen erfassten Fall (vorab über `ticket-und-reisedaten-erfassen`), welcher Tatbestand der VO 2021/782 vorliegt. Maßgeblich für die Folge-Skills (Entschädigungsberechnung, Forderung, Widerspruch, Klage).

## Tatbestände im Überblick

| Tatbestand | Norm | Konsequenz |
|---|---|---|
| **Verspätung am Zielort ≥ 60 Min** | Art. 19 VO + Art. 18 VO | Entschädigung (25/50 %) UND Wahlrecht Erstattung/Weiterreise |
| **Verspätung am Zielort < 60 Min** | Art. 19 Abs. 9 VO | Kein Entschädigungsanspruch (Mindestschwelle nicht erreicht) |
| **Zugausfall** | Art. 18 + Art. 19 VO | Wahlrecht Erstattung/Weiterreise; Entschädigung wenn Endziel-Verspätung ≥ 60 Min |
| **Verpasster Anschluss (Einheits-PNR)** | Art. 12 Abs. 3 VO | Wie Verspätung; Endziel-Maßstab |
| **Verpasster Anschluss (separate PNRs)** | Art. 12 Abs. 4–5 VO | Anspruch je Vertrag separat; ggf. 75 %-Entschädigung des Fahrkartenverkäufers |
| **Vorverlegung der Abfahrt** | nicht ausdrücklich in VO 2021/782 — analog Art. 8 | Falls Fahrgast den vorverlegten Zug nicht erreicht: Behandlung wie Ausfall |
| **Nichtbeförderung (Überbuchung im Eisenbahnverkehr)** | praktisch selten; Art. 18 analog | Wahlrecht; ggf. Schadensersatz nach Art. 26 Abs. 5 Anhang I CIV |
| **SPNV — 20-Min-Schwelle für Alternativzug** | § 11 EVO | Recht auf Wechsel auf anderen Zug (nicht: Entschädigung — die folgt Art. 19 VO) |

## Differenzierungs-Schema

### Schritt 1: Welcher Verkehr?

- **Fernverkehr** (ICE, IC, EC, FlixTrain, ÖBB) → Art. 19 VO ungeschmälert (60/120 Min).
- **SPNV** (RE, RB, S-Bahn im SPNV-Sinn) → Art. 19 VO ungeschmälert PLUS § 11 EVO Zusatzrechte (20-Min-Schwelle für Alternativzug; 120-EUR-Limit Ersatzbeförderung bei Nachtfahrt).
- **Stadt-/Vorortverkehr (S-Bahn-Tarifgebiete, U-Bahn)** — Deutschland hat ausgenommen; Ansprüche nach Tarifbedingungen und nationalen Sonderregeln.

### Schritt 2: Welche Ankunftsverspätung am ZIELORT (nicht Etappe)?

| Verspätung am Endziel | Anspruch |
|---|---|
| 0–59 Min | kein Entschädigungsanspruch nach Art. 19 |
| 60–119 Min | 25 % des Fahrpreises |
| ≥ 120 Min | 50 % des Fahrpreises |

**Achtung:** Auch wenn ein Etappenzug 120 Min Verspätung hatte, der Fahrgast aber durch günstigen Anschlusszug nur 30 Min am Endziel verspätet war: **kein Anspruch** (Art. 19 Abs. 9 VO).

### Schritt 3: Durchgangsfahrkarte oder separate Tickets?

- **Einheitliche PNR**: alle Etappen sind Durchgangsfahrkarte → Anspruch bezieht sich auf Endziel-Verspätung (Art. 12 Abs. 3 VO).
- **Separate PNRs** (z.B. Hin- mit Sparpreis, Anschlussfahrt mit anderem Ticket): jede Strecke einzeln zu bewerten; Anschluss-Garantie greift nicht. Ausnahme Art. 12 Abs. 4 VO: bei Fahrkartenverkäufer / Reiseveranstalter kombiniert + Fehlinformation → 75 %-Entschädigung des Vermittlers.

### Schritt 4: Tatbestand benennen

```yaml
einordnung:
  tatbestand: verspaetung-am-zielort-mindestens-60-min
  norm-anker:
    - Art. 19 Abs. 1 lit. a VO 2021/782   # 25 %
    - Art. 18 Abs. 1 VO 2021/782          # Wahlrecht
    - Art. 20 VO 2021/782                 # Hilfeleistung
  endziel-verspaetung-min: 105
  verspaetungsstufe: stufe-1-25-prozent   # stufe-1-25 | stufe-2-50
  durchgangsfahrkarte: ja
  spnv: nein                              # ja triggert zusätzlich § 11 EVO
  folge-skills:
    - entschaedigung-berechnen
    - forderung-an-db-erste-stufe
    - eigenbefoerderung-und-betreuung-art-18   # falls Auslagen entstanden
```

## Spezialfall: Vorverlegung

VO 2021/782 regelt Vorverlegung **nicht ausdrücklich**, anders als die Fluggast-VO 261/2004 (für die der EuGH Vorverlegungen als Annullierung behandelt — Aktenzeichen vor Verwendung in einem Schriftsatz über curia.europa.eu live verifizieren, nicht aus Modellwissen zitieren). In der Eisenbahn-Praxis: Die DB schickt ggf. eine Verfrühungs-Mitteilung; der Fahrgast erreicht den Zug nicht.

**Sachgerechte Einordnung:** Wenn der Fahrgast den vorverlegten Zug nicht erreichen kann und keine anderweitige Beförderung mit gleicher Ankunftszeit angeboten wird, ist die Situation funktional einem Ausfall gleichzustellen. Art. 18 (Wahlrecht) und Art. 19 (Entschädigung) sind entsprechend anwendbar.

→ Hinweis: Live-Recherche bei curia.europa.eu oder bundesgerichtshof.de prüfen, ob neuere Entscheidung speziell zu Eisenbahn-Vorverlegung vorliegt.

## Spezialfall: Nichtbeförderung (Eisenbahn-Überbuchung)

Im Eisenbahnverkehr selten (anders als bei Flügen). Wenn die DB / FlixTrain die Beförderung verweigert (z.B. wegen Überfüllung in der reservierten 1. Klasse): Wahlrecht analog Art. 18; Schadensersatz Art. 26 Abs. 5 Anhang I CIV. Im Klagefall sehr individuell — vorbereitende Eilprüfung erforderlich.

## Spezialfall: Streiks DB-Personal

Die häufigste Standardausrede der DB: "Streik = außergewöhnlicher Umstand". **Falsch.** Art. 19 Abs. 10 Unterabs. 2 VO 2021/782 schließt Streiks des EVU-Personals **ausdrücklich** von der Befreiungsregel aus. Auch Streiks bei DB Netz AG (Infrastrukturbetreiber) sind nach derselben Norm nicht befreiend.

## Spezialfall: Wetter

- Normales Winterwetter (Schnee, Glatteis) → kein außergewöhnlicher Umstand. EVU muss sich vorbereiten.
- Extremereignisse (Jahrhundert-Sturm, Hochwasser, Lawinen) → **kann** außergewöhnlich sein. Beweislast EVU; muss zumutbare Vorkehrungen darlegen.

## Spezialfall: Personenschäden (Notarzteinsatz auf der Strecke)

- Im Grunde Drittverschulden (Art. 19 Abs. 10 lit. c VO) — befreiend, wenn nicht vermeidbar.
- ABER: Wenn DB den Personenschaden zumutbar erkennen konnte und nicht alternative Routenführung anbot, bleibt sie haftungspflichtig.

## Spezialfall: Bauarbeiten und Baustellenfahrplan

Bauarbeiten gehören zum betrieblichen Risiko des EVU — kein außergewöhnlicher Umstand. Wenn der Baustellenfahrplan vorab veröffentlicht war und der Fahrgast wusste, dass eine reduzierte Streckenkapazität existiert: dennoch Anspruch, solange die VO-Schwellen erreicht sind. Bei Vorab-Information über konkreten Zugausfall vor Ticketkauf entfällt der Anspruch (Art. 19 Abs. 9 VO).

## Ausgabe

```
Einordnung Fahrgastrechte-Fall FGR-2026-0042
Datum: 12.05.2026
Strecke: Berlin Hbf — München Hbf (ICE 503, Einheits-PNR)
Geplante Ankunft: 13:20
Tatsächliche Ankunft: 15:05 (Türöffnung am Bahnsteig)
Endziel-Verspätung: 105 Minuten

Tatbestand: Verspätung am Zielort 60–119 Minuten (Art. 19 Abs. 1 lit. a VO 2021/782)

Anspruchsgrundlage:
 - Art. 19 Abs. 1 lit. a VO 2021/782 — 25 % des Fahrpreises Entschädigung
 - Art. 18 VO 2021/782 — Wahlrecht (hier nicht relevant, Fahrt durchgeführt)
 - Art. 20 VO 2021/782 — Hilfeleistung war geschuldet (Verpflegung)

Befreiung? Nein:
 - DB-Begründung "technischer Defekt" → nach VO 2021/782 Art. 19 Abs. 10 zählt nicht zu den
   außergewöhnlichen Umständen außerhalb des Eisenbahnbetriebs. Beweislast DB.

Operating EVU: DB Fernverkehr AG (passivlegitimiert)

Höhe (vorab):
 - Pro Reisendem: 25 % von 79,00 EUR Ticketpreis = 19,75 EUR
 - 3 Reisende: 59,25 EUR Entschädigung
 - Verpflegungs-Auslage: 12,50 EUR (Art. 20 VO)
 - Gesamt: 71,75 EUR

Nächster Skill: entschaedigung-berechnen (exakte Berechnung)
                forderung-an-db-erste-stufe (Antrag stellen)
```

## Leitentscheidungen Einordnung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
