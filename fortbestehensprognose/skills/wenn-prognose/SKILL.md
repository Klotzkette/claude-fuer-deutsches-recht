---
name: wenn-prognose
description: "Wenn Prognose im Plugin Fortbestehensprognose im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Wenn Prognose

## Arbeitsbereich

**Wenn Prognose** priorisiert Aktenlage, Fristen, Zuständigkeit, Beweislast und gewünschten Output. Die Prüfung beginnt beim sachtragenden Prüfungslinie und endet mit einem verwertbaren Arbeitsergebnis.

## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsverbot § 15b InsO. Prüfung der drohenden Zahlungsunfähigkeit § 18 InsO mit StaRUG-Option. Einbindung Insolvenzanwalt zwingend. Prüfung Selbstantrag oder Eigenverwaltung oder Schutzschirmverfahren oder StaRUG-Restrukturierungsplan. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `wenn-prognose-negativ-naechste-schritte`

**Fokus:** Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsverbot § 15b InsO. Prüfung der drohenden Zahlungsunfähigkeit § 18 InsO mit StaRUG-Option. Einbindung Insolvenzanwalt zwingend. Prüfung Selbstantrag oder Eigenverwaltung oder Schutzschirmverfahren oder StaRUG-Restrukturierungsplan.

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
- Status-Eintrag im Sanierungsbausteine-Tracker: "Prüfung negativ — Eskalation eingeleitet".
- Ende dieses Plugin-Workflows; Fortführung im Plugin `insolvenzrecht` durch Insolvenzanwalt.

## Aktuelle Leitentscheidungen — Negative Prognose und Handlungspflichten (Stand Mai 2026)

- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden; Amtsniederlegung "auf der Flucht" schützt nicht. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktische Geschäftsführung erfasst auch Hintermänner im Firmenbestattermodell. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherer trägt für jede einzelne Zahlung Darlegungs- und Beweislast für positive Kenntnis; § 15a / § 15b InsO nicht koppelbar.
- **BGH IX ZR 285/14 vom 26.01.2017** und **BGH IX ZR 56/22 vom 29.06.2023** — Berater-Hinweispflicht (Insolvenzvertiefungsschaden, Drittschutzwirkung).

## Paragrafenkette Negative Prognose

§ 19 InsO (Ueberschuldung wenn Prognose negativ) → § 15a InsO (Antragspflicht 3/6 Wochen) → § 15b InsO (Zahlungsverbot) → § 43 GmbHG (Haftung GF) → §§ 283 ff. StGB (Bankrott-Strafbarkeit) → §§ 29 ff. StaRUG (letzte Chance StaRUG)

## Triage — Sofortmassnahmen bei negativer Prognose

1. **Insolvenzanwalt sofort einschalten!** Frist § 15a InsO laeuft ab heute: 6 Wochen (Ueberschuldung), 3 Wochen (ZU). Sofort-Kalender-Alarm.
2. **Zahlungen einfrieren?** § 15b InsO: keine Zahlungen die Masse schmälern; Masselohn und Betriebskosten OK; Gesellschafterrueckzahlungen VERBOTEN.
3. **StaRUG-Option pruefen:** Drohende ZU § 18 InsO? Dann StaRUG-Restrukturierungsplan als Alternative zum Insolvenzantrag.
4. **Dokumentation sichern:** Alle Unterlagen fuer Insolvenzantrag vorbereiten: Verzeichnisse, Bilanzen, Glaeubigerliste, Antrag-Vorläufer.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
