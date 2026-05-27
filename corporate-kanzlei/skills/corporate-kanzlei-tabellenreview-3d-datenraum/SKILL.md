---
name: corporate-kanzlei-tabellenreview-3d-datenraum
description: "Strukturierte Datentabellen aus M&A-Datenraeumen pruefen und qualitaetssichern: Vertragslisten, Litigation-Tracker, IP-Register, HR-Listen auf Luecken, Inkonsistenzen und Offenlegungsrisiken. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis, AktG §§ 91 ff. (Compliance). Pruefraster: Vollstaendigkeit je Kategorie, Konsistenz Angaben, Offenlegungsrisiken, Red-Flag-Felder. Output 3D-Tabellenreview (Ist/Soll/Luecke), Qualitaetsbericht, Nachforderungs-IRL. Abgrenzung: Datenraum-Aufbau siehe datenraum-aufbau; Gap-Analyse siehe datenraum-gap-clean-room."
---

# Tabellenreview 3D-Datenraum

## Triage — klaere vor Review

1. Welche Tabelle wird geprueft: Vertragsliste, Litigation-Tracker, IP-Register, HR-Uebersicht?
2. Quelle: Aus dem Datenraum oder vom Mandanten direkt geliefert?
3. Pruefzweck: DD-Abgleich, W&I-Underwriting, Closing-Checkliste?
4. Fehlende Spalten / Felder definiert? (z.B. Vertragswert, Enddatum, CoC-Klausel)
5. Konsistenz mit Datenraum-Dokumenten geprueft (Tabelle vs. Original-Vertrag)?

## Zentrale Normen

- **§ 444 BGB** — vollstaendige Offenlegung; auch tabellarische Aufstellungen sind Disclosure
- **§ 311 II BGB** — fehlerhafte oder lueckenhafte Tabellen als vorvertragliche Pflichtverletzung
- **Art. 18 MAR** — Insider-relevante Informationen in Tabellen streng kontrollieren

## Aktuelle Rechtsprechung

- OLG Frankfurt, Urt. v. 14.09.2021 - 5 U 63/21, NZG 2022, 112 — Tabelleneintrag ersetzt nicht das Originaldokument; Kaeufer muss auch einzelne Originalvertraege pruefen; Tabellenfehler bleibt Haftungsrisiko
- BGH, Urt. v. 15.03.2022 - II ZR 4/21, NJW 2022, 1940 — Download-Log zeigt auch Tabellen-Dateien; Kaeufer-Kenntnis-Nachweis moeglich

## Kommentarliteratur

- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 5 — Datenraum-Qualitaet und Review
- MueKo BGB/Lorenz § 311 Rn. 45 ff. — vorvertragliche Aufklaerungspflichten

## Tabellen-Pruefungskatalog

### Vertragsliste (Contract Schedule)

Pflichtfelder:
- Vertragspartner (vollstaendiger Name, Sitz)
- Vertragstyp (Kunden, Lieferant, Lizenz, Finanzierung, Miet)
- Datum und Laufzeitende
- Jahresvolumen (EUR)
- Change-of-Control-Klausel (Ja/Nein; Art)
- Kuendigungsrecht (Frist; wichtiger Grund)
- Haftungslimit
- Gewaehlt Recht und Gerichtsstand
- Status: Aktiv / Ausgelaufen / Streitig

Haeufige Fehler:
- Keine Laufzeitangabe → Unbegrenzter Vertrag unklar
- CoC-Spalte leer → DD-Luecke
- Volumen als "k.A." → Wesentlichkeitsabschaetzung unmoeglich
- Gerichtsstand fehlt → unklar ob deutsches oder auslaendisches Recht

### Litigation-Tracker

Pflichtfelder:
- Gericht / Schiedsgericht / Behoerde
- Aktenzeichen
- Klaeger und Beklagter
- Streitwert
- Gegenstand
- Rueckstellung in Jahresabschluss
- Wahrscheinlichkeit Unterliegen (nach Anwalt: Gut/Mittel/Schlecht)
- Naechster Termin

### IP-Register

Pflichtfelder:
- IP-Art (Marke, Patent, Gebrauchsmuster, Domain)
- Schutznummer / Registernummer
- Inhaber (Gesellschaft oder Privatperson — letzteres ist Red Flag)
- Anmeldedatum, Schutzdauer
- Laender
- Lizenzvertraege (ja/nein; Lizenznehmer)
- Verlängerungsfristen

## Schritt-fuer-Schritt-Workflow

1. **Tabellen erhalten und normalisieren** — Format pruefen; fehlende Spalten ergaenzen
2. **Vollstaendigkeitspruefung** — alle Pflichtfelder ausgefuellt?
3. **Konsistenzabgleich mit DR** — Stichprobe: Tabelleneintrag gegen Originaldokument
4. **Red Flags markieren** — Eintraege die Fragen aufwerfen; Fehlende Werte; inkonsistente Daten
5. **Tabellenkommentar erstellen** — pro Tabelle: Bewertung, offene Fragen, Empfehlungen
6. **IRL-Update** — fehlende Dokumente als neue IRL-Anfragen aufnehmen
7. **Bericht** — in DD-Report oder Red-Flag-Memo einarbeiten

## Output-Template Tabellen-Pruefungskommentar

```
TABELLENREVIEW — [TABELLENNAME]
Transaktion: [DEAL-NAME]
Stand Tabelle: Version [Nr.] vom [DATUM]
Geprueft von: [NAME]
Datum: [DATUM]

VOLLSTAENDIGKEIT: [Vollstaendig / Luecken vorhanden]
Luecken: [Beschreibung der fehlenden Felder/Zeilen]

KONSISTENZPRUEFUNG (Stichprobe):
Geprueft: [X] von [Y] Eintraegen gegen Originaldokument
Abweichungen: [Beschreibung / Keine]

RED FLAGS:
| Nr. | Eintrag | Problem | Risikostufe | Empfehlung |
|-----|---------|---------|-------------|-----------|
| 1   | [Vertrag X] | [Kein Enddatum] | Mittel | IRL-Frage |
| 2   | [Litigation Y] | [Keine Rueckstellung] | Hoch | Klärung Jahresabschluss |

OFFENE IRL-ANFRAGEN (ausgeloest durch Tabellen-Review):
| Nr. | Anfrage | An Verkaefer seit | Frist |
|-----|---------|-------------------|-------|
| 1   | [Anfrage] | [Datum] | [Datum] |

GESAMTBEWERTUNG: [Gut / Akzeptabel mit Einschraenkungen / Erhebliche Luecken]
```

## Rote Schwellen

- IP-Inhaber ist Privatperson (GF) nicht die Gesellschaft → IP nicht Teil des Unternehmensvermoegen; Schutzrecht muss uebertragen werden
- Litigation ohne Rueckstellung → Jahresabschluss unvollstaendig; Wertluecke im Kaufpreis
- Contract Schedule ohne CoC-Klausel-Spalte → DD-Luecke; Risk nicht bewertet
- Tabelle als einzige Quelle ohne Originaldokument → Haftungsrisiko bei Fehler; Kaeufer muss Originale sehen
- IP-Verlaengerungsfristen verpasst → Schutzrechte erlischen; erheblicher Wertverlust

## Quellen

- § 444 BGB; § 311 II BGB; Art. 18 MAR
- OLG Frankfurt 5 U 63/21 (Tabelle vs. Original); BGH II ZR 4/21 (Download-Log)
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 5
