---
name: dokumentenintake-forderungsportfolio
description: "Dokumentenintake Forderungsportfolio: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake Forderungsportfolio

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Fachkern: Dokumentenintake Forderungsportfolio
- **Normen-/Quellenanker:** BGB Forderungsabtretung, HGB, KWG/ZAG-Erlaubnisfragen, InsO-Anfechtung, Factoringvertrag, Debitorenmanagement, Datenschutz und Geldwäsche.
- **Entscheidende Weiche:** Echtes/unechtes Factoring, Forderungsbestand, Abtretbarkeit, Einwendungen, Debitoreninformation, Insolvenzrisiko und Refinanzierung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Vor jedem Forderungsankauf, vor jedem Portfolio-Audit und vor jeder Sonderprüfung steht der **Dokumentenintake**: das geordnete Einlesen, Strukturieren und Klassifizieren der Unterlagen, die der Kunde zur Verfügung stellt. Beim Mengen-Geschäft (mehrere Tausend Forderungen pro Monat) entscheidet die Qualität des Intake-Prozesses über die spätere Beweisbarkeit jeder einzelnen Forderung.

Dieser Skill standardisiert den Intake: einheitliche Datenformate, Pflichtfelder pro Forderung, Belegklassifikation, Eingangskontrollen, automatisierte Plausibilitätschecks (Rechnungsnummer eindeutig, Lieferschein vorhanden, Betrag stimmig), DSGVO-Konformität. Ziel: kein Forderungsankauf ohne vollständigen Intake-Datensatz.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sie nehmen ein neues Factoring-Mandat auf und bauen die Intake-Pipeline.
- Bei einem bestehenden Kunden ändert sich das ERP-System, die Intake-Schnittstelle muss angepasst werden.
- Im Portfolio-Verkauf brauchen Sie einen reproduzierbaren Intake-Standard für den Investor.
- Im Streitfall fehlen plötzlich Belege – der Intake-Prozess muss nachvollziehbar dokumentiert sein.

Fragen zum Einstieg:
- Welches ERP nutzt der Kunde (SAP, DATEV, Sage, individuelle Lösung)?
- Welche Schnittstellen sind möglich (DATEV-Export, CSV, REST-API, SAP-IDOC)?
- Wie viele Forderungen pro Monat im Durchschnitt?
- Welche Belegtypen sind nötig (Bestellung, AB, LS, Rechnung, Abnahme)?
- Wie ist die Datenqualität historisch (Vollständigkeitsquote, Fehlerquote)?

## Rechtlicher Rahmen

- **HGB §§ 238, 239**: Buchführungsgrundsätze – ordnungsgemäße Erfassung aller Geschäftsvorfälle.
- **§ 257 HGB**: Aufbewahrungspflichten 6–10 Jahre, je nach Dokument.
- **GoBD (Grundsätze ordnungsgemäßer Buchführung in elektronischer Form)**: Unveränderbarkeit, Vollständigkeit, Nachvollziehbarkeit.
- **§ 14 UStG**: Pflichtangaben einer Rechnung.
- **DSGVO Art. 5, 6, 28, 32**: Datenverarbeitung im Intake.
- **BGB § 666**: Auskunftspflicht im Geschäftsbesorgungsverhältnis.
- **AO §§ 145, 147**: Steuerliche Aufzeichnungs- und Aufbewahrungspflichten.
- **BSI IT-Grundschutz**: für sichere Intake-Pipelines (kein zwingendes Recht, aber Stand der Technik).

## / Schritt für Schritt

1. **Schnittstellen definieren**: ERP-Export, CSV-Schema, API-Endpoint mit Authentifizierung.
2. **Pflichtfelder festlegen**: Forderungs-ID, Debitor-ID, Rechnungsnummer, Rechnungsdatum, Fälligkeit, Betrag (netto/brutto/USt), Leistungszeitraum, Auftragsnummer.
3. **Belegtypen definieren**: Welche Dokumente müssen pro Forderung vorliegen?
4. **Plausibilitätschecks**: Doppelte Rechnungsnummern, Betragsdifferenzen Brutto/Netto, fehlende Lieferscheine, Datumssprünge.
5. **Eingangskontrolle**: Vier-Augen-Prinzip bei Großforderungen, Reklamationsbestand abgleichen.
6. **DSGVO-Compliance**: Daten in geschützter Umgebung, AVV mit IT-Hostern, Löschkonzept.
7. **Reporting**: Wöchentlicher Intake-Bericht mit Vollständigkeitsquote, Fehlerquote, Abweichungen.

## Trade-off-Matrix

| Intake-Modus | Vorteil | Nachteil |
|---|---|---|
| Vollautomatisiert per API | Schnell, fehlerarm | Setup-Aufwand, ERP-abhängig |
| CSV-Batch täglich | Robust, einfach | Verzögerung 24h |
| Manuelle Einzelmeldung | Flexibel | Skaliert nicht |
| Datenraum-Upload durch Kunden | Klar abgegrenzt | Setzt Kundendisziplin voraus |
| Direkt-Anbindung ERP (Read-Only) | Aktuell, vollständig | Hohe IT-Anforderungen |

## Praxistipps

- **Pflichtfelder hart durchsetzen**: Forderungen ohne komplette Belege werden nicht angekauft, sondern in "Pending"-Status gestellt.
- **Doppelten Eingang verhindern**: Eindeutige Rechnungs-ID + Debitor-ID als Primärschlüssel.
- **Eingangsbestätigung versenden**: Kunde erhält automatisierte Quittung mit Hash-Wert über das eingegangene Datenpaket.
- **GoBD-Konformität sicherstellen**: Unveränderbarkeit der Originalbelege beweissicher dokumentieren.
- **Versionierung**: Bei Rechnungskorrekturen alte und neue Version archivieren, Versionshistorie nachvollziehbar.

## Mustertexte

**Klausel im Factoringvertrag (Intake-Pflichten Kunde)**

"Der Kunde übermittelt jede zum Ankauf angebotene Forderung im definierten Datenformat (CSV nach Anlage 5) mit folgenden Pflichtfeldern: Forderungs-ID, Debitor-ID, Rechnungsnummer (eindeutig), Rechnungsdatum, Fälligkeitsdatum, Bruttobetrag, USt-Satz, Leistungszeitraum, Auftragsbestätigungs-ID. Zusätzlich übermittelt der Kunde die Belegkette (Bestellung, AB, Lieferschein, Rechnung, Abnahmebestätigung) als PDF/A im Datenraum. Forderungen ohne vollständige Belegkette werden nicht angekauft."

**Datenformat-Spezifikation (Auszug)**

```
forderungs_id;debitor_id;rechnungsnummer;rechnungsdatum;faelligkeit;betrag_netto;ust_betrag;betrag_brutto;leistung_von;leistung_bis;auftrags_id
F-2026-001;D-12345;R-2026-0089;2026-05-15;2026-06-15;10000,00;1900,00;11900,00;2026-05-01;2026-05-14;A-2026-0234
```

**Eingangsquittung an Kunden (automatisiert)**

"Sehr geehrte Damen und Herren, wir bestätigen den Eingang Ihrer Forderungsmeldung vom … mit folgenden Kennzahlen: Eingangsdatum/Uhrzeit, Anzahl Forderungen …, Gesamtvolumen … EUR, Hash-Wert SHA-256 … . Plausibilitätsprüfung läuft, Sie erhalten innerhalb von zwei Werktagen Rückmeldung. Forderungen, die Plausibilitätskriterien nicht erfüllen, werden separat ausgewiesen."

## Typische Fehler

- Intake ohne Pflichtfelder-Disziplin – Forderungen ohne Belege werden angekauft.
- Doppelte Rechnungsnummern unentdeckt – führt zu Streit über tatsächlich angekaufte Forderungen.
- GoBD-Verstoß durch nachträgliche Veränderung der Originalbelege.
- Eingangsquittung fehlt – Streit über Datum und Inhalt der Meldung.
- DSGVO-Compliance unklar – Datenexporte ungeschützt.

## Quellen Stand 06/2026

- HGB §§ 238, 239, 257 zu Buchführung und Aufbewahrung.
- AO §§ 145, 147 zu steuerlichen Aufzeichnungspflichten.
- GoBD-Schreiben des BMF in aktueller Fassung.
- DSGVO Art. 5, 6, 28, 32 zur Datenverarbeitung.
- UStG § 14 zu Rechnungsanforderungen.
