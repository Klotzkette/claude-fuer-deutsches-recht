---
name: fruehwarnsystem-architektur-zwei-jahres-horizont
description: "StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont architektieren: Unternehmen will § 1 StaRUG Krisenfrueherkennung implementieren. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW S 6 (Sanierungsstandard), IDW PS 340 n.F. (Risikomanagement-Prüfung). Prüfraster: Risiko-Inventar, KPI-Kaskade, Eskalationsstufen, Reporting-Frequenzen, Schwellenwerte, Organisationseinbettung. Output Fruehwarnsystem-Konzept, Implementierungsplan, Governance-Struktur. Abgrenzung: KPI-Set Ampelsystem siehe kennzahlenset-und-ampelsystem-starug-konform; Liquiditaetsplanung siehe rollierende-liquiditaetsplanung-24-monate-template im Krisenfrueherkennung Starug."
---

# Frühwarnsystem-Architektur mit Zwei-Jahres-Horizont

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StaRUG; § 1 StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Ein Frühwarnsystem nach § 1 StaRUG ist kein Excel-Sheet in einer Schublade — es ist eine lebende Governance-Struktur. IDW PS 340 n.F. und IDW S 6 geben die fachlichen Standards vor. Wer diesen Rahmen nicht in die operative Unternehmenssteuerung integriert, erfüllt die gesetzliche Pflicht nur auf dem Papier — und steht im Haftungsfall ohne belastbaren Nachweis da.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht)
- § 91 Abs. 2 AktG (Risikoüberwachungssystem für AG)
- IDW PS 340 n.F. (Anforderungen an Risikofrüherkennungssysteme, Stand 2020)
- IDW S 6 (Anforderungen an Sanierungskonzepte, Stand 2018)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen, Stand 2021)
- § 18 InsO (drohende Zahlungsunfähigkeit)

---

## Pflichten

### 1. Rechtliche Anforderungen an das Frühwarnsystem

Ein § 1 StaRUG-konformes Frühwarnsystem muss folgende Mindestanforderungen erfüllen:

**Formale Anforderungen:**
- Schriftlich dokumentiert und von der Geschäftsführung förmlich beschlossen
- Klar definierte Verantwortlichkeiten (wer meldet was an wen bis wann)
- Regelmäßige Überprüfung und Aktualisierung (mindestens jährlich)
- Nachweis der tatsächlichen Anwendung (Protokolle, Berichte)

**Inhaltliche Anforderungen (IDW PS 340 n.F.):**
- Risikoidentifikation, Risikobewertung und Risikoüberwachung
- Festlegung von Risikotoleranzgrenzen und Eskalationsschwellen
- Integration in die Unternehmensplanung (kein separates Silo)
- Bestandsgefährdungsrisiken besonders hervorheben

### 2. IDW PS 340 n.F. — Kernelemente

IDW PS 340 n.F. (Neufassung 2020) verlangt:

| Element | Inhalt |
|---|---|
| Risikoidentifikation | Vollständige Erfassung aller wesentlichen Risiken (intern + extern) |
| Risikobewertung | Eintrittswahrscheinlichkeit und Schadenshöhe quantifizieren |
| Risikoaggregation | Gesamtrisikoprofil — Wechselwirkungen berücksichtigen |
| Risikoüberwachung | KPIs, Meilensteine, Plan-Ist-Abweichungen |
| Berichterstattung | Regelkreis von GF zum Aufsichtsorgan |

---

## Templates

### Muster: Risiko-Inventar (Tabellenstruktur)

```
Risiko-Inventar — [Firma GmbH] — Stand: [Datum]

Nr. | Risikokategorie | Risikobeschreibung | Eintrittswsk. | Schaden EUR | Risikoscore | Verantwortlich | KPI | Schwelle ROT
----|----------------|-------------------|--------------|------------|------------|---------------|-----|-------------
R01 | Liquidität | Refinanzierungsrisiko: Hausbankkredit läuft [Datum] aus | Mittel | [Betrag] | Hoch | CFO | Kredit-Restlaufzeit | < 6 Monate
R02 | Umsatz | Kundenkonzentration: Kunde X = [x]% Umsatz | Niedrig | [Betrag] | Mittel | CSO | Umsatzanteil Top-1-Kunde | > 25 %
R03 | Personal | Schlüsselpersonenrisiko: Geschäftsführer [Name] | Niedrig | [Betrag] | Mittel | GF | Nachfolgeplanung | Nicht vorhanden
```

### Muster: Frühwarnsystem-Beschluss der Geschäftsführung

```
Beschluss der Geschäftsführung — Frühwarnsystem § 1 StaRUG

Gesellschaft: [Firma GmbH]
Datum: [TT.MM.JJJJ]

Die Geschäftsführung beschließt:

1. Das vorliegende Frühwarnsystem (Systemhandbuch vom [Datum])
 wird als verbindliche Governance-Struktur eingeführt.
2. Verantwortlich für Pflege und Reporting: [Name, Funktion].
3. Die KPI-Schwellenwerte gemäß Anlage 1 gelten ab sofort.
4. Abweichungen von Stufe 2 (Gelb) werden unverzüglich protokolliert.
5. Das System wird jährlich, erstmals zum [Datum], überprüft.

[Unterschriften GF]
```

---

## Fallstricke

1. **Frühwarnsystem auf Papier ist kein Frühwarnsystem** — im Haftungsfall wird geprüft, ob das System tatsächlich gelebt wurde. Fehlende Reports, keine Protokolle, keine Eskalationen: Indizienbeweis für Pflichtverletzung.

2. **Schwellenwerte zu weit gefasst** schützen nicht. Wer "ROT erst ab Zahlungsunfähigkeit" definiert, hat kein Frühwarnsystem, sondern ein Brandmeldesystem nach dem Brand.

3. **Keine Integration in Planungsprozess** — das Frühwarnsystem muss mit der operativen Planung verbunden sein. Eigenständige Silo-Lösung ohne Rückkopplung erfüllt IDW PS 340 n.F. nicht.

4. **Outsourcing an Steuerberater ohne eigene Überwachung** reicht nicht. Der Steuerberater liefert Daten, die GF muss sie auswerten und auf Abweichungen reagieren.

5. **Jährliche statt rollierende Überprüfung** ist zu grob. Das Risiko-Inventar muss nach wesentlichen Veränderungen ad hoc überprüft werden.

---

## Aktuelle Leitentscheidungen — Fruehwarnsystem und § 1 StaRUG

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Fruehwarnsystem

§ 1 StaRUG (Pflicht zur Fruehwarnung) → § 102 StaRUG (Rechtsberater-Warnpflicht) → § 43 GmbHG (Sorgfaltspflicht GF) → § 93 AktG (Vorstandshaftung) → § 91 Abs. 2 AktG (Fruehwarnsystem-Pflicht AG) → § 15a InsO (Antragspflicht bei erkannter ZU/Ueberschuldung)

## Triage — Fruehwarnsystem

1. **Kennzahlen-Set?** Welche Kennzahlen werden in welchem Rhythmus erhoben? (Liquiditaet, EBIT, Forderungslaufzeit, Eigenkapital-Quote)
2. **Ampelsystem vorhanden?** Gruene, gelbe, rote Schwellen definiert?
3. **Eskalationskette?** Wer wird bei roten Ampeln informiert? GF → Aufsichtsrat → Anwalt?
4. **Historische Daten?** 2 Jahre Ruckschau für Trend-Erkennung vorhanden?

