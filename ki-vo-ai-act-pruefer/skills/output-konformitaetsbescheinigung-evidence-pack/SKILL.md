---
name: output-konformitaetsbescheinigung-evidence-pack
description: "Druckreifes KI-VO-Konformitätspaket erzeugen: interne Konformitätsbescheinigung, EU-Konformitätserklärung nach Art. 47/Anhang V, Art.-43-Bewertungsnachweis, CE-/EU-DB-/Post-Market-Check, Evidence Index und Lückenliste ohne falsche Bescheinigung."
---

# Output Konformitätsbescheinigung und Evidence-Pack

## Zweck

Dieser Skill erzeugt ein druckreifes Konformitätspaket für KI-Systeme nach der Verordnung (EU) 2024/1689. Er ist der Output-Skill nach Art.-3-Prüfung, Rollenklärung, Hochrisiko-Einstufung, Anforderungen Art. 9-15 und Konformitätsbewertung Art. 43.

**Wichtige Grenze:** Der Skill darf keine echte behördliche oder notifizierte Bescheinigung behaupten. Wenn die Voraussetzungen nicht belegt sind, heißt das Dokument `Konformitätsvermerk (Entwurf)` oder `Readiness-Bescheinigung`, nicht finale Konformitätsbescheinigung. Eine EU-Konformitätserklärung nach Art. 47 i.V.m. Anhang V wird nur als unterschriftsreife Vorlage erstellt, wenn die zugrunde liegenden Nachweise vorhanden sind.

## Wann verwenden?

- Anbieter eines Hochrisiko-KI-Systems braucht eine Akte für Geschäftsführung, Audit, Kunden oder Marktaufsicht.
- Die Konformitätsbewertung nach Art. 43 soll dokumentiert werden.
- Eine EU-Konformitätserklärung nach Art. 47 und Anhang V soll vorbereitet werden.
- Betreiber/Kunde verlangt Nachweise zu Risikomanagement, Datenqualität, Human Oversight, Logging und Cybersecurity.
- Es soll eine klare Lückenliste entstehen, bevor CE-Kennzeichnung, EU-Datenbank oder Marktfreigabe erfolgen.

## Vorprüfung

Vor dem Output prüfen:

1. **Systemabgrenzung:** Was ist das konkrete KI-System, Version, Produktname, Modellkomponenten, Zweckbestimmung?
2. **Rolle:** Anbieter, Betreiber, Importeur, Händler, Bevollmächtigter, Produkthersteller?
3. **Risikoklasse:** Art. 6 Abs. 1/2, Anhang I/III, Rückausnahme Art. 6 Abs. 3, GPAI-Schnittstelle.
4. **Pflichtenstatus:** Art. 9 bis 15 erfüllt oder offen?
5. **Konformitätsbewertung:** Art. 43-Pfad, interne Kontrolle oder benannte Stelle?
6. **Normen/Spezifikationen:** Harmonisiert im Amtsblatt oder nur ISO/IEC-/Branchenstandard als Belegrahmen?
7. **Registrierung/CE:** Art. 48/49/71 einschlägig?
8. **Post-Market:** Art. 72 ff. Monitoring und Incident-Prozess vorhanden?

Wenn diese Punkte nicht belegt sind, zuerst die passenden Spezial-Skills vorschlagen:

- `liegt-ki-system-vor-art-3-nr-1`
- `hochrisiko-art-6-abs-2-anhang-iii`
- `hochrisiko-risikomanagementsystem-art-9`
- `hochrisiko-technische-dokumentation-art-11-und-anhang-iv`
- `hochrisiko-konformitaetsbewertung-art-43-bis-49`
- `output-konformitaetserklaerung-eu-anhang-v`

## Output-Paket

### 1. Konformitätsbescheinigung / Konformitätsvermerk

Erzeuge ein Dokument mit Statuskopf:

| Status | Bezeichnung | Wann verwenden |
|---|---|---|
| Final | `Interne Konformitätsbescheinigung des Anbieters` | Alle Nachweise vollständig, Art.-43-Pfad abgeschlossen, zeichnungsbefugte Freigabe |
| Entwurf | `Konformitätsvermerk (Entwurf)` | Prüfung weitgehend abgeschlossen, aber Nachweise oder Freigaben fehlen |
| Readiness | `KI-VO-Readiness-Bescheinigung` | Noch keine finale Konformität, aber dokumentierter Stand und Maßnahmenplan |
| Drittstelle | `Bescheinigung unter Bezugnahme auf notifizierte Stelle` | Nur wenn eine echte benannte Stelle beteiligt war und Nachweis vorliegt |

Pflichtinhalt:

- Systemname, Version, eindeutige Kennung.
- Anbieter/Rechtsträger, Anschrift, Datenschutz-/Compliancekontakt.
- Zweckbestimmung und bestimmungsgemäßer Einsatz.
- Risikoeinstufung mit Art.-6-/Anhang-Begründung.
- Konformitätsbewertungspfad nach Art. 43.
- Nachweisübersicht Art. 9-15.
- Normen, Standards, Common Specifications, angewandte Testmethoden.
- EU-Datenbank-/CE-/Post-Market-Status.
- Abweichungen, Auflagen, Gültigkeitsdauer, Review-Trigger.
- Unterschriftsblock.

### 2. EU-Konformitätserklärung nach Art. 47 / Anhang V

Erstelle eine Vorlage nur mit den erforderlichen Angaben:

- Name und Anschrift des Anbieters oder Bevollmächtigten.
- Erklärung, dass die EU-Konformitätserklärung in alleiniger Verantwortung des Anbieters ausgestellt wird.
- Eindeutige Identifizierung des KI-Systems.
- Erklärung der Konformität mit der KI-VO und ggf. sonstigem Unionsrecht.
- Verweise auf angewandte harmonisierte Normen oder gemeinsame Spezifikationen, soweit einschlägig.
- Gegebenenfalls Name und Kennnummer der notifizierten Stelle und Bescheinigungsangaben.
- Ort, Datum, Name, Funktion und Unterschrift.

Verweise auf `output-konformitaetserklaerung-eu-anhang-v`, wenn der Nutzer nur die Erklärung ohne Gesamtpaket möchte.

### 3. Evidence Index

Erzeuge eine Aktenliste:

| ID | Nachweis | Artikel | Stand | Eigentümer | Status | Fundstelle |
|---|---|---|---|---|---|---|
| E-01 | Risikomanagementakte | Art. 9 | ... | ... | grün/gelb/rot | ... |
| E-02 | Data-Governance-Bericht | Art. 10 | ... | ... | ... | ... |
| E-03 | Technische Dokumentation | Art. 11/Anhang IV | ... | ... | ... | ... |
| E-04 | Logging-Konzept | Art. 12 | ... | ... | ... | ... |
| E-05 | Gebrauchsanweisung/Transparenz | Art. 13 | ... | ... | ... | ... |
| E-06 | Human-Oversight-Konzept | Art. 14 | ... | ... | ... | ... |
| E-07 | Accuracy/Robustness/Cybersecurity | Art. 15 | ... | ... | ... | ... |
| E-08 | QMS | Art. 17 | ... | ... | ... | ... |
| E-09 | Konformitätsbewertung | Art. 43 | ... | ... | ... | ... |
| E-10 | Post-Market Monitoring | Art. 72 | ... | ... | ... | ... |

### 4. Lückenliste und Maßnahmenplan

Jede Lücke mit:

- Pflicht.
- Befund.
- Risiko.
- Maßnahme.
- Verantwortlicher.
- Frist.
- Blockiert Marktfreigabe: ja/nein.

### 5. Kunden- oder Behördenpaket

Wenn der Nutzer "für Kunden", "für Behörde" oder "zum Ausdrucken" sagt, zusätzlich:

- Einseitige Management Summary.
- Nicht-technische Systembeschreibung.
- Zweckbestimmungs- und Nutzungsgrenzen.
- Art.-6-/Anhang-III-Matrix.
- Zusammenfassung der Konformitätsbewertung.
- Auflagen und Review-Prozess.

## Standards und Normen

- Harmonisierten Normen kommt Vermutungswirkung nur zu, soweit die Fundstelle im Amtsblatt der Europäischen Union veröffentlicht ist.
- ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 22989, ISO/IEC 23053 und vergleichbare Standards können als Governance- und Nachweisrahmen dienen, ersetzen aber nicht automatisch KI-VO-Anforderungen.
- Wenn keine harmonisierte Norm einschlägig oder veröffentlicht ist, dokumentiere alternative angemessene Mittel und Tests.

## Warnsignale

Setze den Status nie auf final, wenn:

- System und Version nicht eindeutig sind.
- Zweckbestimmung und tatsächliche Nutzung auseinanderfallen.
- Anhang-III-Einstufung nicht entschieden ist.
- Art. 9-15 nur behauptet, aber nicht belegt sind.
- Bei erforderlicher Drittstellenprüfung keine benannte Stelle vorliegt.
- CE-Kennzeichnung oder EU-Datenbank-Registrierung als erledigt behauptet wird, aber Nachweise fehlen.
- GPAI-Komponenten genutzt werden, deren Anbieterpflichten/Lieferantennachweise unklar sind.

## Abschlussformat

Am Ende immer:

1. **Status:** Final / Entwurf / Readiness / Stop.
2. **Darf unterschrieben werden?** Ja/Nein/Ja mit Auflagen.
3. **Nicht behaupten:** Liste von Aussagen, die wegen fehlender Nachweise nicht gemacht werden dürfen.
4. **Nächste Schritte:** Maximal sieben priorisierte Maßnahmen.

## Quellen und Aktualität

- Stand: 05/2026.
- Verordnung (EU) 2024/1689, insbesondere Art. 3, 6, 9-17, 25, 43-49, 71-73 und Anhang IV/V.
- Europäische Kommission/JRC: harmonisierte Standards geben erst nach Veröffentlichung im Amtsblatt eine Vermutungswirkung.
