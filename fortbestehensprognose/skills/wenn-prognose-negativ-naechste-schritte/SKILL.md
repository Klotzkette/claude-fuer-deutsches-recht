---
name: wenn-prognose-negativ-naechste-schritte
description: "Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog fuer den Geschaeftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Ueberschuldung drei Wochen bei Zahlungsunfaehigkeit. Zahlungsverbot § 15b InsO. Pruefung der drohenden Zahlungsunfaehigkeit § 18 InsO mit StaRUG-Option. Einbindung Insolvenzanwalt zwingend. Pruefung Selbstantrag oder Eigenverwaltung oder Schutzschirmverfahren oder StaRUG-Restrukturierungsplan."
---

# Wenn die Prognose negativ ist — nächste Schritte

## Disclaimer (Schlüsselstelle)

Wenn die Fortbestehensprognose negativ ausfällt liegt **insolvenzrechtliche Überschuldung** nach § 19 InsO vor. Die Antragspflicht beginnt zu laufen. **Ohne Insolvenzanwalt** sollte ab diesem Punkt nicht weitergearbeitet werden. Jede Tagesverzoegerung kann zur **strafrechtlichen Haftung** nach § 15a Abs. 4 InsO und zur **zivilrechtlichen Haftung** nach § 15b InsO führen.

## Sofortmaßnahmen — innerhalb 24 Stunden

### 1. Insolvenzanwalt einschalten

- Insolvenzanwalt aus dem Profil (Skill `fortbestehensprognose-kaltstart-interview`).
- Termin innerhalb der nächsten 48 Stunden.
- Vorlage: vollständige Prognosedokumentation aus Skill `prognose-dokumentation-stichtag`.

### 2. Zahlungsverhalten anpassen — § 15b InsO

Mit Eintritt der Insolvenzreife dürfen **keine Zahlungen** mehr geleistet werden die nicht mit der Sorgfalt eines ordentlichen und gewissenhaften Geschäftsleiters vereinbar sind.

Ausnahmen (§ 15b Abs. 1 InsO):

- Zahlungen die zur Erhaltung des Geschäftsbetriebs erforderlich sind.
- Zahlungen die im Rahmen ordentlicher Geschäftstätigkeit unvermeidbar sind.
- Zahlungen aus zweckgebundener Treuhand (Sozialversicherungsbeitraege Lohnsteuer).

**Praktisch**:

- Sozialversicherungsbeitraege Arbeitnehmer-Anteil: **weiter abführen** (§ 266a StGB Pflicht zur Abführung).
- Lohn- und Gehaltszahlung: weiter (sonst gefährden der Betrieb).
- Lohnsteuer abführen.
- Umsatzsteuer Voranmeldungen abgeben (auch wenn keine Zahlung erfolgt).
- Bezahlung von Lieferanten nur nach Abstimmung mit Insolvenzanwalt — Risiko § 15b InsO.

### 3. Frist § 15a InsO

| Insolvenzgrund | Frist nach Eintritt |
|---|---|
| Zahlungsunfähigkeit § 17 InsO | drei Wochen (§ 15a Abs. 1 S. 2 InsO) |
| Überschuldung § 19 InsO | sechs Wochen (§ 15a Abs. 1 S. 2 InsO seit SanInsFoG 2021) |
| Drohende Zahlungsunfähigkeit § 18 InsO | **keine Antragspflicht** — aber Antragsoption |

**Achtung**: Die Frist beginnt mit **Eintritt** des Insolvenzgrunds — nicht mit Kenntnis. Im Streit ist das objektive Datum maßgeblich.

## Mittelfristige Optionen (zusammen mit Insolvenzanwalt)

### Option A — Regelinsolvenzantrag

- Selbstantrag § 15 InsO.
- Antrag durch Insolvenzanwalt vorbereitet.
- Bei Eröffnung: Insolvenzverwalter übernimmt.

### Option B — Eigenverwaltungsantrag (§ 270 ff. InsO)

- Geschäftsleitung bleibt im Amt (Sachwalter wird bestellt).
- Voraussetzungen Eigenverwaltungsplan strenge Bonitätsanforderung.

### Option C — Schutzschirmverfahren (§ 270d InsO)

- Bei drohender Zahlungsunfähigkeit oder Überschuldung **vor** Eintritt der Zahlungsunfähigkeit.
- Bescheinigung eines erfahrenen Sanierungsanwalts oder WPs erforderlich (Aussichten auf Sanierung).
- Antrag auf Schutzschirm zur Erarbeitung eines Insolvenzplans.

### Option D — StaRUG-Restrukturierungsrahmen

- Nur bei **drohender** Zahlungsunfähigkeit § 18 InsO (24-Monats-Prognose) — **nicht** bei akuter Zahlungsunfähigkeit oder Überschuldung.
- Restrukturierungsplan mit Gläubiger-Mehrheiten.
- Restrukturierungsbeauftragter durch Restrukturierungsgericht.
- Bescheinigung nach §§ 50 51 StaRUG (IDW S 9) wird empfohlen.

## Prüfraster Auswahl Verfahren

```yaml
verfahren-pruefraster:
  zahlungsunfaehigkeit-eingetreten:
    frist: drei-Wochen
    optionen:
      - Regelinsolvenzantrag (Selbstantrag)
      - Eigenverwaltung (wenn Voraussetzungen erfüllt)
      - Schutzschirmverfahren nur bei drohender Zahlungsunfähigkeit
        BEVOR Zahlungsunfähigkeit eintrat
    ausgeschlossen: StaRUG (zu spaet)
    
  überschuldung-eingetreten-aber-zahlungsfähig:
    frist: sechs-Wochen
    optionen:
      - Regelinsolvenzantrag
      - Eigenverwaltung
      - Schutzschirmverfahren
    pruefung-staerug: nur wenn drohende Zahlungsunfähigkeit
      separat festgestellt werden kann (Prognose 24 Monate negativ)
    
  drohende-zahlungsunfaehigkeit:
    frist: keine
    optionen:
      - StaRUG-Restrukturierungsrahmen (bevorzugt)
      - Eigenantrag § 18 InsO mit Eigenverwaltung
      - Schutzschirmverfahren
```

## Beratungsbedarf

In jedem Fall:

- **Insolvenzanwalt** (Skill `insolvenzrecht` aus dem entsprechenden Plugin)
- **Wirtschaftsprüfer** bei IDW S 11 / S 9 Bescheinigung
- **Sanierungsberater** wenn Sanierungskonzept IDW S 6 erforderlich

## Eskalation an Insolvenzanwalt

Schreiben an Insolvenzanwalt:

```
Sehr geehrte Damen und Herren,

ich bin Geschäftsführer der [Firma]. Nach Erstellung der
Fortbestehensprognose nach § 19 Abs. 2 InsO zum Stichtag [Datum] habe ich
das Ergebnis dass die Prognose negativ ausfaellt. Damit liegt
insolvenzrechtliche Überschuldung vor.

Stichtag: [Datum]
Anlass: [siehe Fortbestehensprognose Anlage]
Ergebnis: insolvenzrechtliche Überschuldung
Frist § 15a InsO: bis [Datum + sechs Wochen]

Ich bitte um umgehende Terminvereinbarung zur Prüfung des weiteren Vorgehens
(Regelinsolvenz / Eigenverwaltung / Schutzschirmverfahren / ggf. StaRUG).

Anlagen:
  - Fortbestehensprognose mit allen Anlagen (Datum [...])
  - Bilanz [Jahr]
  - Aktuelle BWA SuSa
  - 12-Monats-Liquiditätsplan
  - Sanierungsbausteine-Empfehlung

Mit freundlichen Grüßen
[Geschäftsführer]
```

## Auch im Zweifel

Wenn nicht klar ist ob die Prognose negativ ist (Grenzfall): **lieber Anwalt einschalten** als die Frist verstreichen lassen. Die Anwaltsgebuehr ist deutlich geringer als die persönliche Haftung.

## Ausgabe

- `eskalation-an-insolvenzanwalt-<datum>.docx` als Mitteilung.
- Termin im Kalender innerhalb 24 Stunden.
- Status-Eintrag im Sanierungsbausteine-Tracker: „Prüfung negativ — Eskalation eingeleitet".
- Ende dieses Plugin-Workflows; Fortführung im Plugin `insolvenzrecht` durch Insolvenzanwalt.


## Aktuelle Leitentscheidungen — Negative Prognose und Handlungspflichten

- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Negative Prognose und Insolvenzantragspflicht: bei negativer Fortbestehensprognose Ueberschuldung nach § 19 InsO gegeben; Antragspflicht § 15a InsO: 6 Wochen (Ueberschuldung), 3 Wochen (Zahlungsunfaehigkeit).
- BGH, Urt. v. 15.03.2016 — II ZR 119/14, NJW 2016, 2493 — § 15b InsO Zahlungsverbot: Geschaeftsfuehrer darf nach Insolvenzreife keine Zahlungen mehr leisten die die Glaeubiger benachteiligen; Ausnahme: Zahlungen zur Aufrechterhaltung des Geschaftsbetriebs ohne Massebeeintraechtigung.
- BGH, Urt. v. 26.01.2017 — IX ZR 285/14 — Drohende ZU und StaRUG-Option: auch bei negativer Fortbestehensprognose kann StaRUG Restrukturierungsplan greifen wenn drohende ZU vorliegt (§ 18 InsO); StaRUG als letzte Chance vor Insolvenzantrag.
- BGH, Urt. v. 06.05.2021 — IX ZR 72/20, NZI 2021, 631 — Sanierungsversuch nach negativer Prognose: echter Sanierungsversuch mit schlussigem Konzept schuetzt vor Strafbarkeit § 283 StGB und Vorsatzanfechtung; Konzept muss vor Antragsfrist vorliegen.

## Paragrafenkette Negative Prognose

§ 19 InsO (Ueberschuldung wenn Prognose negativ) → § 15a InsO (Antragspflicht 3/6 Wochen) → § 15b InsO (Zahlungsverbot) → § 43 GmbHG (Haftung GF) → §§ 283 ff. StGB (Bankrott-Strafbarkeit) → §§ 29 ff. StaRUG (letzte Chance StaRUG)

## Triage — Sofortmassnahmen bei negativer Prognose

1. **Insolvenzanwalt sofort einschalten!** Frist § 15a InsO laeuft ab heute: 6 Wochen (Ueberschuldung), 3 Wochen (ZU). Sofort-Kalender-Alarm.
2. **Zahlungen einfrieren?** § 15b InsO: keine Zahlungen die Masse schmälern; Masselohn und Betriebskosten OK; Gesellschafterrueckzahlungen VERBOTEN.
3. **StaRUG-Option pruefen:** Drohende ZU § 18 InsO? Dann StaRUG-Restrukturierungsplan als Alternative zum Insolvenzantrag.
4. **Dokumentation sichern:** Alle Unterlagen fuer Insolvenzantrag vorbereiten: Verzeichnisse, Bilanzen, Glaeubigerliste, Antrag-Vorläufer.

## Kommentarliteratur

- MüKo InsO/Haarmeyer § 15a InsO Rn. 1-80 — Antragspflicht, Fristen, Haftungsfolgen.
- Uhlenbruck/Mock § 19 InsO Rn. 75-90 — Negative Prognose und InsO-Folgen.
- K. Schmidt/Uhlenbruck, GmbH in Krise, § 4 Rn. 4.30 — Handlungskatalog bei negativer Prognose.
