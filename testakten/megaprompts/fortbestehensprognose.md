# Megaprompt: fortbestehensprognose

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `fortbestehensprognose`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fortbestehensprognose StaRUG/InsO: ordnet Rolle (Geschäftsführung, Wirtschaftsprüfer, I…
2. **fortbestehensprognose-erstpruefung-und-mandatsziel** — Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel im Fortbestehensprognose.
3. **annahmen-belastbarkeit-plausibilisieren** — Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA…
4. **annahmen-sammeln-bilanzieller-status** — Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklu…
5. **ausloesendes-ereignis-erfassen** — Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinwei…
6. **bilanzieller-status-aufnehmen** — Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Üb…
7. **forderungsverzicht-besserungsschein** — Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstar…
8. **kaltstart-interview** — Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand /…
9. **sanierungsbausteine-vorschlagen-annahmen** — Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsb…
10. **start-chronologie-fristen** — Einstieg, Schnelltriage und Fallrouting im Fortbestehensprognose-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken…
11. **stundungsanfrage-glaeubiger** — Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gl…
12. **zusammenfuehren** — Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszena…
13. **comfortletter-weich-erzeugen** — Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unters…
14. **prognose-stichtag-stundungsanfrage-glaeubiger** — Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plaus…
15. **quellen-livecheck** — Quellen-Live-Check für Fortbestehensprognose StaRUG/InsO: prüft Normen (§ 18 InsO drohende Zahlungsunfähigkeit, StaRUG §…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fortbestehensprognose StaRUG/InsO: ordnet Rolle (Geschäftsführung, Wirtschaftsprüfer, Insolvenzverwalter), markiert Frist (Antragsfrist 3 Wochen § 15a InsO), wählt Norm (§ 18 InsO drohende Zahlungsunfähigkeit, StaRUG §§ 1/14/49, IDW S 11) und Zuständigkeit (Insolv..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fortbestehensprognose** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `annahmen-behoerden-gericht-und-registerweg` — Annahmen Behoerden Gericht und Registerweg
- `annahmen-belastbarkeit-plausibilisieren` — Annahmen Belastbarkeit Plausibilisieren
- `annahmen-sammeln-bilanzieller-status` — Annahmen Sammeln Bilanzieller Status
- `ausloesendes-ereignis-erfassen` — Ausloesendes Ereignis Erfassen
- `bilanzieller-status-aufnehmen` — Bilanzieller Status Aufnehmen
- `bilanzstatus-risikoampel-und-gegenargumente` — Bilanzstatus Risikoampel und Gegenargumente
- `comfortletter-sonderfall-edge` — Comfortletter Sonderfall Edge
- `comfortletter-weich-erzeugen` — Comfortletter Weich Erzeugen
- `eskalation-sonderfall-und-edge-case` — Eskalation Sonderfall und Edge Case
- `fbp-bankenkommunikation-waiver-integrierte` — FBP Bankenkommunikation Waiver Integrierte
- `fbp-integrierte-planung-bauleiter` — FBP Integrierte Planung Bauleiter
- `fbp-stresstest-szenarien-leitfaden` — FBP Stresstest Szenarien Leitfaden
- `fbp-zahlungsunfaehigkeit` — FBP Zahlungsunfaehigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fortbestehensprognose sind InsO, StaRUG, § 19 Abs. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `fortbestehensprognose-erstpruefung-und-mandatsziel`

_Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel im Fortbestehensprognose._

# Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Fortbestehensprognose Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fortbestehensprognose** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Pruefungen und Leistungspunktsystem.
- `§ 16 HRG` — Pruefungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Pruefungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** InsO, IDW, StaRUG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fortbestehensprognose** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `annahmen-belastbarkeit-plausibilisieren`

_Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Personal) und Risikokategorisierung. Plausibilitaetsband für je..._

# Annahmen plausibilisieren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Prüfraster pro Annahme

### 1. Vergangenheits-Vergleich

- Stimmt die Annahme mit den **letzten drei Jahren** der BWA / SuSa / Jahresabschluss überein?
- Bei Abweichung: ist die Veränderung **konkret begründet** (neuer Kunde Standortschliessung Tariferhöhung)?
- Bei stark abweichender Optimismus-Annahme **ohne neuen Anlass**: Reduktion auf historisches Niveau im Plausi-Szenario.

### 2. Markt- und Branchenentwicklung

- **Branchenindex** vorhanden? (z. B. ifo Geschäftsklimaindex DESTATIS Branchenkennzahlen).
- **Auftragsbestand der Branche** rückschau.
- **Makro-Indikatoren** Konjunktur Zinsen Energiepreise.

### 3. Interne Konsistenz

- Umsatz steigt, aber Materialkosten bleiben gleich? Konsistenz prüfen.
- Personalkosten steigen, aber Personalstand sinkt? Begründung erforderlich (Tariferhöhung + Reduzierung gleichzeitig).
- Working Capital verbessert sich rapide? Begründung notwendig.

### 4. Belegbarkeit der Maßnahmen

- Sanierungsmaßnahmen mit Effekt — ist der Effekt **belegt** (Vergleichswerte historisch Kostenrechnung)?
- Zeitplan realistisch (z. B. Standortschliessung in 60 Tagen)?
- Einmalkosten realistisch erfasst?

### 5. Drittvereinbarungen

- Patronatserklärungen / Comfortletter: bereits unterzeichnet oder nur in Verhandlung?
- Gesellschafterdarlehen mit Rangrücktritt: notarielle Urkunde vorhanden?
- Bankenzusage: schriftlich oder mundlich?

## Plausibilitätsband pro Annahme

```yaml
plausibilisierung:
 - annahme-id: umsatz-hauptsegment
 band: realistisch # konservativ / realistisch / ambitioniert / nicht-belastbar
 begruendung: |
 Auftragsbestand bis 09/2026 belegt; ab 10/2026 Modellfortschreibung
 auf Basis Vorjahr +3%
 risiko: mittel
 sensitivitaet-szenario:
 negativ: 10% Umsatzrückgang ab 10/2026
 effekt-eur: -190000 (kumuliert)

 - annahme-id: kostensenkung-standort
 band: ambitioniert
 begruendung: |
 Kündigung Standortmietvertrag erfordert 9-Monats-Kündigungsfrist;
 Schliessung bis 08/2026 nur möglich wenn Mieter Aufhebung akzeptiert.
 Aktuell in Verhandlung — nicht belegt.
 risiko: hoch
 sensitivitaet-szenario:
 negativ: Schliessung gelingt nicht im Planhorizont
 effekt-eur: 50000 monatliche Mehrkosten

 - annahme-id: bankenzusage-erhöhung-kreditlinie
 band: nicht-belastbar
 begruendung: |
 Verhandlung mit Bank laeuft. Bisher keine schriftliche Zusage.
 Bank verweist auf laufendes Rating-Verfahren.
 risiko: hoch
 sensitivitaet-szenario:
 negativ: Kreditlinie wird nicht erhöht
 effekt-eur: keine zusätzliche Liquidität 80000 EUR
```

## Konservativer Maßstab

Eine Fortbestehensprognose ist nicht der Ort für Optimismus. **IDW S 11** und **BGH-Rspr.** verlangen einen vorsichtigen objektiven Maßstab.

- Bei Zweifeln: **konservative** Annahmen wählen.
- Wenn eine Annahme **ambitioniert** oder **nicht-belastbar** ist und entscheidend für das Prognoseergebnis ist: das Ergebnis ist **nicht verwertbar** als positive Fortbestehensprognose. Maßnahme: entweder Belegbarkeit nachholen oder Annahme entfernen.

## Sensitivitätsszenarien

```yaml
szenarien:
 basisszenario:
 annahmen: alle wie in annahmen.yaml
 ergebnis-12-monate-liquiditaet: positiv
 bemerkung: Plan-Szenario

 negativ-szenario:
 annahmen: alle ambitioniert-Annahmen reduziert auf konservativ
 ergebnis-12-monate-liquiditaet: knapp positiv # vor Maßnahmen
 bemerkung: Risiko-Szenario; bei Eintritt sind Zusatzmaßnahmen erforderlich

 stress-szenario:
 annahmen: zusätzlich Wegfall Top-Kunde
 ergebnis-12-monate-liquiditaet: negativ
 bemerkung: Reines Stress-Szenario; in der Plausibilisierung
 als unwahrscheinlich eingeschaetzt
```

## Sonderfälle

### Stille Reserven die zur Plausibilisierung herangezogen werden

Wenn der Status stille Reserven enthält (Skill `bilanzieller-status-aufnehmen`) muss die Liquidität auch realistisch über Verkauf erzielbar sein:

- Verkehrswert-Gutachten vorhanden?
- Realistisch verkaufbar im Planhorizont?
- Auswirkung auf den Betrieb (z. B. Verkauf einer Maschine führt zu Produktionsausfall)?

### Comfortletter

- **Weicher Comfortletter** (Best Effort) ist im Status **nicht** zu berücksichtigen.
- **Harte externe Patronatserklärung** mit Forderungsverzicht im Insolvenzfall ist berücksichtigungsfähig — siehe Skill `patronatserklaerung-extern-hart-erzeugen`.

## Ausgabe

- `plausibilisierung.md` mit jeder Annahme bewertet (Band Risiko Sensitivitaet).
- Drei Szenarien (Basis Negativ Stress) mit Endergebnis.
- Empfehlung: bei mehr als zwei nicht-belastbaren oder ambitionierten Annahmen die das Ergebnis tragen ist die Prognose **nicht positiv** zu werten.
- Liste konkreter Maßnahmen zur Verbesserung der Belastbarkeit (Belegnachholung Verhandlungsabschluss Drittvereinbarung).

## Aktuelle Leitentscheidungen — Annahmen-Plausibilitaet

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Annahmen-Plausibilitaet

§ 19 Abs. 2 InsO (Fortbestehensprognose) → § 15b InsO (Haftung bei fehlerhafter Prognose) → IDW S 11 Rn. 45 ff. (Annahmen-Qualitaet) → IDW S 6 Rn. 90 ff. (Plausibilitaetspruefung Sanierungskonzept)

## Triage — Annahmen-Check

Bevor losgelegt wird, klaere:

1. **Konsistenz-Test:** Passt Umsatzwachstum zu Personalkosten und Material? (Umsatz +10% ohne Personal-Aufstockung bei Vollauslastung → inkonsistent)
2. **Vergangenheits-Abgleich:** Welche Wachstumsraten wurden in den letzten 3 Jahren tatsaechlich erreicht? Neue Annahmen muessen daraus ableitbar sein.
3. **Sensitivity-Test:** Welche Annahme ist am kritischsten? Was passiert wenn Haupt-Kunden 20% weniger abnimmt?
4. **Worst-Case-Szenario:** Prognose auch bei pessimistischsten Annahmen noch positiv?

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 43 GmbHG
- § 3a EStG
- § 102 StaRUG
- § 266a StGB
- § 1 StaRUG
- § 93 AktG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG

### Leitentscheidungen

- BGH II ZR 296/05
- BGH IX ZR 285/14
- BGH IX ZR 56/22
- BGH II ZR 206/22
- BGH IV ZR 66/25

---

## Skill: `annahmen-sammeln-bilanzieller-status`

_Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt- und Branchenentwicklung. Annahmen muessen konkret nachvollzi..._

# Annahmen sammeln (Fortführung)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Pflichtfelder pro Annahme

```yaml
annahmen:
 - bezeichnung: Umsatzentwicklung Hauptgeschaeft
 art: umsatz
 horizont-monate: 12
 werte:
 - monat: 2026-06
 wert: 195000
 - monat: 2026-07
 wert: 180000
 # ...
 begruendung: |
 Vorjahreswerte plus 3% Wachstum bei stabiler Auftragslage.
 Auftragsbestand zum 20.05.2026 deckt bis September 2026.
 belege:
 - auftragsbestand-2026-05-20.xlsx
 - kundenbestätigung-grossauftrag-X.pdf
 risiko: mittel # niedrig / mittel / hoch
 sensitivitaet:
 negativ-szenario: -15% Umsatz waehrend zweier Monate
 positiv-szenario: +10% Umsatz
```

## Annahmebereiche

### 1. Umsatzentwicklung

- **Auftragsbestand** zum Stichtag.
- **Kundenpipeline** quasi-sichere Folgeaufträge.
- **Saisonalität** historisch über drei Jahre.
- **Top-Kunden-Konzentration** Risiko bei Wegfall.

### 2. Kostenentwicklung

- **Materialkosten** Lieferantenpreise Energie.
- **Personalkosten** Tarifsteigerungen Sozialabgaben.
- **Mieten** Vertragsprüfung Indexmiete.
- **Energie** aktueller Preis und Vertragslaufzeit.

### 3. Working Capital

- **Forderungslaufzeiten** Tage Outstanding (DSO).
- **Vorrats-Reichweite** Umschlagsdauer.
- **Lieferanten-Zahlungsziele** ggf. verschlechtert wegen Krise (DPO).

### 4. Investitionen und Desinvestitionen

- **Geplante Investitionen** und ihre Finanzierung.
- **Desinvestitionen** Verkauf nicht-betriebsnotwendiger Vermögenswerte.

### 5. Finanzierung

- **Bestehende Kreditlinien** Volumen Ausnutzung Endfälligkeit.
- **Tilgungspläne** der bestehenden Darlehen.
- **Neue Finanzierungsangebote** Bank schriftliche Zusagen.
- **Gesellschafterzusagen** Patronatserklärungen Comfortletter.

### 6. Sanierungsmaßnahmen

- **Bereits eingeleitete** Maßnahmen (Kostensenkung Personalreduzierung Standortschliessungen).
- **Geplante** Maßnahmen mit Zeitplan und Effekt.
- **Gegenfinanzierung** der Sanierungskosten.

## Abgrenzung zwischen Annahmen und Wünschen

**Annahme**: Eine konkrete nachvollziehbare Erwartung mit Begründung und Beleg.

**Wunsch**: Eine optimistische Hoffnung ohne Beleg.

Im Streit (z. B. späteren Haftungsprozess) wird genau geprüft ob es Wünsche oder Annahmen waren. Wer optimistisch ohne Belege geplant hat ist haftungsexponiert (§ 43 GmbHG, § 15b InsO).

## Konkretheit

Jede Annahme braucht:

- **Zahl** (in EUR oder Prozent oder Tagen) — keine Spannweiten außer bei Sensitivitaet.
- **Zeitraum** — Monat oder Quartal.
- **Begründung** — woher kommt die Zahl?
- **Beleg** — Excel Auftragsbestand Bestätigung Kunde Mietvertrag etc.

## Sammlung der Annahmen

```yaml
prognose-id: FP-2026-0001
stichtag: 2026-05-20
horizont-monate: 12 # gesetzlicher Maßstab seit SanInsFoG 2021

annahmen:
 umsatz:
 - bezeichnung: Hauptsegment Produktion
 monatswerte: [195000, 180000, 220000, 240000, 230000, 200000, 190000, 195000, 210000, 220000, 215000, 225000]
 begruendung: Auftragsbestand bis September 2026; Mai-Oktober historisch +10% über Schnitt
 belege: [auftragsbestand-2026-05-20.xlsx]
 risiko: mittel

 kosten:
 - bezeichnung: Material und Energie
 basismonats-wert: 95000
 jahressteigerung: 3%
 begruendung: Lieferantenverträge bis 06/2027 Indexbindung 3%
 belege: [lieferantenverträge-übersicht.xlsx]
 risiko: niedrig
 - bezeichnung: Personalkosten
 basismonats-wert: 78000
 jahressteigerung: 4%
 begruendung: Tarifabschluss Metall 04/2026 4% per 01.07.2026
 belege: [tarifabschluss-04-2026.pdf]
 risiko: niedrig

 working-capital:
 forderungstage-soll: 30
 forderungstage-ist: 42
 vorratsreichweite-soll: 60
 vorratsreichweite-ist: 75
 begruendung-abweichung: kundenseits verzoegerte Zahlungen seit Q1 2026
 massnahmen: Mahnwesen verschärft

 investitionen:
 - bezeichnung: Ersatzinvestition CNC
 betrag: 80000
 monat: 2026-09
 finanzierung: Sale-and-Lease-back

 finanzierung:
 bank-kreditlinie: 150000
 ausnutzung-ist: 92%
 gesellschafterdarlehen-mit-rangruecktritt: 120000
 weitere-massnahmen: keine

 sanierungsmassnahmen:
 - bezeichnung: Standortschliessung Nebenwerk
 effekt-monatlich: 12000
 ab-monat: 2026-08
 einmalkosten: 60000
 einmalkosten-monat: 2026-07
```

## Ausgabe

- `annahmen.yaml` mit allen Pflichtfeldern.
- Hinweis auf Skill `annahmen-belastbarkeit-plausibilisieren` als nächsten Schritt.
- Liste fehlender Belege als Prüfer-Flag.
- Empfehlung: bei einer Annahme die als unbelegt markiert ist *nicht* in die Liquidität übernehmen — oder explizit als "Modellannahme ohne Beleg" markieren.

## Aktuelle Leitentscheidungen — Annahmen-Sammlung Fortbestehensprognose

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — Annahmen-Vollstaendigkeit

1. **Einnahmen-Seite vollstaendig?** Auftragsbestand, Rahmenvertraege, Neukundenpipeline — alle konkret belegbar?
2. **Kosten-Seite vollstaendig?** Personal (inkl. SV), Material/Wareneinsatz, Fixkosten, Miete, Finanzierungskosten — alle als Einzelpositionen?
3. **Working Capital?** Debitorenlaufzeit, Kreditorenlaufzeit, Lagerbestand — als Cashflow-Auswirkung erfasst?
4. **Ausserordentliche Ereignisse?** Investitionen, Tilgungen, FA-Stundungen ablaufend, Avale faellig werdend?

## Paragrafenkette

§ 19 Abs. 2 InsO (Fortbestehensprognose) → IDW S 11 Rn. 30-65 (Annahmen-Basis) → § 43 GmbHG (Sorgfaltspflicht GF bei Prognose)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 43 GmbHG
- § 3a EStG
- § 102 StaRUG
- § 266a StGB
- § 1 StaRUG
- § 93 AktG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG

### Leitentscheidungen

- BGH II ZR 296/05
- BGH IX ZR 285/14
- BGH IX ZR 56/22
- BGH II ZR 206/22
- BGH IV ZR 66/25

---

## Skill: `ausloesendes-ereignis-erfassen`

_Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass Gesellschafterhinweis eigene Sorge des Geschäftsführers. Do..._

# Auslösendes Ereignis erfassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Die Fortbestehensprognose ist kein Selbstzweck — sie ist die Antwort auf einen konkreten Anlass. Der Anlass wird dokumentiert weil **er Beweis ist**: bei späteren Haftungsfragen (§ 15b InsO, § 43 GmbHG, § 826 BGB ggue Gläubigern) zeigt die Dokumentation dass der Geschäftsführer **zeitnah** auf Anzeichen reagiert hat.

## Typische Auslöser

### 1. Hinweis des Steuerberaters nach § 102 StaRUG

Seit 01.01.2021 hat der Steuerberater eine **Hinweispflicht**: wenn ihm bei der Bilanzaufstellung Anhaltspunkte für einen möglichen Insolvenzeröffnungsgrund auffallen muss er den Mandanten darauf hinweisen.

- Datum des Hinweises (schriftlich / mündlich / im Gespräch)
- Wortlaut wenn schriftlich
- Konkrete Anhaltspunkte die der StB genannt hat
- Quittierung des Hinweises durch den Mandanten

### 2. Hinweis des Wirtschaftsprüfers

Bei prüfungspflichtigen Gesellschaften (mittelgroße oder große KapGes nach § 267 HGB) kann der Prüfer im Rahmen des Jahresabschlusses einen **Hinweis zur Going-Concern-Annahme** geben oder den Bestätigungsvermerk einschraenken oder versagen.

### 3. Eigene Feststellung bei der Bilanzaufstellung

- **Eigenkapital negativ** (Aktiva kleiner als Passiva).
- **Wesentliche stille Lasten** im Status (z. B. Pensionsrückstellungen außerbilanziell).
- **Erhebliche außergewöhnliche Verluste** im laufenden Geschäftsjahr.

### 4. Liquiditätsengpass

- Mahnungen Gerichtsbeschlüsse oder Zahlungsverzug bei wesentlichen Gläubigern.
- Kreditlinie ausgeschoepft Kontoüberziehung.
- Lohn- und Gehaltszahlungen knapp.
- Steuer- und Sozialversicherungsabgaben nicht puenktlich.

### 5. Gesellschafterhinweis

- Brief oder E-Mail des Gesellschafters mit Sorge über Lage.
- Gesellschafterbeschluss zur Prüfung der Fortbestehensprognose.

### 6. Eigene Sorge des Geschäftsführers

- Subjektive Wahrnehmung dass die Lage kritisch wird.
- Wichtig: auch ohne externen Hinweis muss der Geschäftsführer aktiv prüfen — Sorgfaltspflicht § 43 GmbHG, § 93 AktG.

### 7. Externes Ereignis

- Wegfall Hauptkunde.
- Kreditlinien-Kündigung der Bank.
- Markteinbruch.
- Insolvenz eines wesentlichen Lieferanten / Abnehmers.

## Dokumentation

```yaml
fall-id: FP-2026-0001
stichtag-pruefung: 2026-05-20
ausloeser:
 typ: hinweis-steuerberater # hinweis-steuerberater / hinweis-wp / eigene-feststellung-bilanz / liquiditätsengpass / gesellschafterhinweis / eigene-sorge / externes-ereignis
 datum: 2026-05-15
 hinweisgeber: Steuerberater Mueller, Kanzlei XYZ
 mitteilungsform: schriftlich # schriftlich / muendlich / e-mail
 wortlaut: |
 "Nach Aufstellung des Jahresabschlusses 2025 ergibt sich ein negatives
 Eigenkapital von 82.000 EUR. Wir weisen Sie nach § 102 StaRUG auf die
 Pflicht zur Prüfung einer Fortbestehensprognose nach § 19 Abs. 2 InsO
 hin."
 konkrete-anhaltspunkte:
 - Eigenkapital negativ 82.000 EUR Stichtag 31.12.2025
 - SuSa weist Lieferantenverbindlichkeiten 410.000 EUR (Vorjahr 180.000)
 - Sozialversicherungsbeitraege drei Monate offen 45.000 EUR
 reaktion-geschaeftsfuehrung:
 erste-reaktion-am: 2026-05-20
 schritte:
 - Beauftragung Erstellung Fortbestehensprognose
 - Aktivierung Plugin fortbestehensprognose
 - Termin mit Insolvenzanwalt vereinbart für 2026-05-27 als Sicherheit
```

## Pflichthinweis Frist

Mit Eintritt der **Insolvenzreife** (Zahlungsunfähigkeit § 17 oder Überschuldung § 19 InsO) beginnen die Antragsfristen des § 15a InsO. **Die Fortbestehensprognose ist nicht zu verwechseln mit dieser Frist** — sie ist die Prüfung **ob** Überschuldung trotz negativen Bilanzbildes verneint werden kann.

- Frist Zahlungsunfähigkeit: **drei Wochen** (§ 15a Abs. 1 S. 2 InsO).
- Frist Überschuldung: **sechs Wochen** (§ 15a Abs. 1 S. 2 InsO seit SanInsFoG 2021).

Im Zweifel **vor Ablauf der Frist** Insolvenzanwalt zu Rate ziehen.

## Ausgabe

- `ausloesendes-ereignis.yaml` mit allen Pflichtfeldern.
- Erste Risikobewertung (grün / gelb / rot).
- Empfehlung: bei rot direkt zu `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einschalten — diese Prüfung kann fortgesetzt werden aber nicht ohne anwaltliche Begleitung.

## Aktuelle Leitentscheidungen — Ausloesende Ereignisse

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Ausloesende Ereignisse

§ 102 StaRUG (Warnpflicht Rechtsberater) → § 19 InsO (Ueberschuldung als Eröffnungsground) → § 15a InsO (Antragspflicht 3/6 Wochen) → § 15b InsO (Haftung GF) → § 43 GmbHG (Sorgfaltspflicht)

## Triage — Ausloesende Ereignisse

1. **Wer hat das Signal gesandt?** Steuerberater (§ 102 StaRUG), Wirtschaftspruefer, eigene Erkenntnis GF, Bank-Gespraech?
2. **Datum des Signals?** Tag-genau dokumentieren → Beginn der Haftungszeit-Uhr.
3. **Schriftliche Dokumentation?** E-Mail, Aktenvermerk, Protokoll vorhanden?
4. **Sofortmassnahmen?** Liquiditaetsplanung starten, Anwalt einschalten, Steuerberater beauftragen?

---

## Skill: `bilanzieller-status-aufnehmen`

_Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle Verpflichtungen (Pensionsrückstellungen Buergschaften Comfo..._

# Bilanzieller Status aufnehmen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Der **bilanzielle** Überschuldungsstatus ist die Voraussetzung um in die Prüfung der **insolvenzrechtlichen** Überschuldung nach § 19 Abs. 2 InsO einzusteigen. Beide Schritte sind zu trennen:

1. **Bilanzieller Überschuldungsstatus** (Stichtagsbetrachtung). Aktiva kleiner als Passiva?
2. **Insolvenzrechtliche Überschuldung** (§ 19 InsO). Nur wenn bilanzielle Überschuldung vorliegt UND keine positive Fortbestehensprognose.

## Stichtagsbilanz

```yaml
stichtag: 2026-05-20 # oder Bilanzstichtag des letzten Jahresabschlusses
bilanzansatz: hgb # hgb / ifrs / mischung

aktiva:
 a-anlagevermoegen:
 immaterielle: 50000
 sachanlagen: 320000
 finanzanlagen: 0
 b-umlaufvermoegen:
 vorraete: 180000
 forderungen-laul: 120000
 sonstige-forderungen: 15000
 fluessige-mittel: 18000
 c-rechnungsabgrenzung: 5000
 aktiva-summe: 708000

passiva:
 a-eigenkapital:
 gezeichnetes-kapital: 25000
 kapitalruecklage: 0
 gewinnruecklagen: 0
 bilanzergebnis: -107000 # negativ
 eigenkapital-summe: -82000 # negativ
 b-rueckstellungen:
 pensionen: 0
 sonstige: 22000
 c-verbindlichkeiten:
 banken: 250000
 lieferanten: 410000
 sonstige: 38000
 steuern: 25000
 sozialversicherung: 45000
 d-rechnungsabgrenzung: 0
 passiva-summe: 708000

bilanzielle-ueberschuldung: ja # Aktiva = Passiva aber EK negativ = bilanzielle Überschuldung
hoehe-bilanzielle-ueberschuldung: 82000
```

## Stille Reserven

Vermögenswerte deren Buchwert geringer ist als der Verkehrswert. Im Status zu addieren (heben die bilanzielle Überschuldung).

```yaml
stille-reserven:
 - position: CNC-Anlage
 buchwert: 95000
 verkehrswert: 180000
 stille-reserve: 85000
 - position: Betriebsgrundstueck
 buchwert: 120000
 verkehrswert: 210000
 stille-reserve: 90000
summe-stille-reserven: 175000
```

## Stille Lasten

Verpflichtungen die in der Handelsbilanz nicht oder zu niedrig passiviert sind. Im Status zu addieren (verschärfen die bilanzielle Überschuldung).

```yaml
stille-lasten:
 - position: Drohende Inanspruchnahme aus Bürgschaft
 bilanziell: 0
 insolvenzrechtlich: 50000
 - position: Pensionsrückstellung Erfüllungsbetrag versus Bilanzwert
 bilanziell: 0
 insolvenzrechtlich: 30000
summe-stille-lasten: 80000
```

## Bereits qualifizierter Rangrücktritt

Forderungen mit qualifiziertem Rangrücktritt (§ 19 Abs. 2 S. 2 InsO) werden im Überschuldungsstatus **nicht passiviert**.

```yaml
qualifizierter-rangruecktritt:
 - glaeubiger: Hauptgesellschafter Karl Mueller
 forderung: Gesellschafterdarlehen vom 15.03.2024
 nennbetrag: 120000
 rangruecktritt-erklaert-am: 2026-05-22
 rangruecktritt-form: notarielle Urkunde # idealtypisch
 bgh-konform: ja # siehe Skill gesellschafterdarlehen-rangrücktritt
```

## Insolvenzrechtlicher Überschuldungsstatus

```
Aktiva (Handelsbilanz) 708.000 EUR
+ stille Reserven 175.000 EUR
- stille Lasten -80.000 EUR
= Insolvenzrechtliche Aktiva 803.000 EUR

Passiva (Handelsbilanz) 790.000 EUR (Aktiva minus EK)
- qualifizierter Rangrücktritt -120.000 EUR
= Insolvenzrechtliche Passiva 670.000 EUR

Differenz 133.000 EUR positiv
```

Ergebnis: trotz **bilanzieller Überschuldung von 82.000 EUR** ist die **insolvenzrechtliche Bilanzbasis positiv** weil stille Reserven und Rangrücktritt dies neutralisieren. Reine Vermögensbilanz **ist nicht ausreichend** — die Fortbestehensprognose ist zusätzlich erforderlich (Skill `annahmen-sammeln-fortfuehrung`).

## Wichtige Hinweise

- Bei **Personengesellschaften ohne natürlich-personige Vollhafter** (z. B. GmbH und Co. KG mit ausschließlich Komplementär-GmbH) gilt § 19 InsO entsprechend.
- Bei **Einzelkaufmann** oder Personengesellschaft mit natürlich-personiger Vollhafter ist § 19 InsO **nicht anwendbar** — Insolvenzantragspflicht ergibt sich nur aus Zahlungsunfähigkeit § 17 InsO.
- Die Erstellung des Status ist **Geschäftsleiter-Pflicht**. Bei Buchführungsmängeln (kein aktueller Stand kein Status möglich) kommt **Bankrott** § 283b StGB in Betracht.

## Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

- `bilanzieller-status.yaml` mit Stichtag Bilanzwerten stillen Reserven Lasten Rangrücktritt und insolvenzrechtlicher Bilanzbasis.
- Erste Ergebnisaussage (insolvenzrechtliche Bilanzbasis positiv / negativ).
- Empfehlung: bei negativer Bilanzbasis ohne Aussicht auf Fortbestehensprognose **sofort** Insolvenzanwalt — § 15a InsO Sechs-Wochen-Frist beginnt zu laufen.

## Aktuelle Leitentscheidungen — Bilanzieller Status

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bilanzieller Status

§ 19 Abs. 2 InsO (Ueberschuldungsbegriff) → § 19 Abs. 2 S. 2 InsO (qualifizierter Rangruecktritt) → § 35 Abs. 1 InsO (Massebegriff stille Reserven) → HGB §§ 252-255 (Bewertungsgrundsaetze) → IDW S 11 Rn. 20-42 (Status-Ermittlung)

## Triage — Bilanzieller Status

1. **Stichtag festlegen:** Welches Datum hat der Status? (aktuellstes Datum mit verlaesslichen Daten)
2. **Stille Reserven identifizieren:** Grundstuecke zum Buchwert vs. Verkehrswert; Forderungen vs. Marktpreis; Beteiligungen.
3. **Ausserbilanzielle Verpflichtungen:** Pensionen, Buergschaften, noch nicht ausgewiesene Verluste aus schwebenden Geschaeften.
4. **Sanierungsmassnahmen einbeziehen?** Gesellschafterdarlehen mit Rangruecktritt, Patronatserklaerung, Kapitalzufuhr — bereits vorhanden oder noch planerisch?

---

## Skill: `forderungsverzicht-besserungsschein`

_Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die verzichtete Forderung wird nicht passiviert. Steuerliche Folge..._

# Forderungsverzicht mit Besserungsschein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Wirkung

Gläubiger verzichtet auf eine Forderung. Effekt:

- **Im Status**: Forderung entfaellt aus den Passiva. Bilanzbild verbessert sich.
- **Liquidität**: keine direkte Liquiditätszuflussverbesserung (die Forderung war ggf ohnehin nicht in den nächsten 12 Monaten zur Zahlung fällig).
- **Bilanz**: Ertrag (Sanierungserloes).

Mit **Besserungsschein**: Wenn die Schuldnerin später wieder zahlungsfähig wird lebt die Forderung wieder auf. Der Verzicht ist also bedingt.

## Anwendungsfall

- Bank verzichtet auf Teil-Tilgung eines Darlehens.
- Lieferant verzichtet auf Forderung mit Besserungsschein als Sanierungsbeitrag.
- Hauptgesellschafter verzichtet auf Forderung (statt Rangrücktritt).

## Steuerliche Folgen

### Beim Schuldner

Ertragsbuchung Sanierungserloes. **Sanierungsgewinn § 3a EStG** kann steuerbefreit sein wenn die Voraussetzungen (Sanierungsabsicht Sanierungsfähigkeit Sanierungseignung Gläubigergleichbehandlung) erfüllt sind.

Vor Unterzeichnung **steuerliche Beratung** zwingend.

### Beim Gläubiger

Forderungsausfall regelmäßig als Betriebsausgabe abzugsfähig. Bei Banken Wertberichtigung. Steuerlich vor Verzicht prüfen lassen.

## Mustervorlage

```
FORDERUNGSVERZICHTSVEREINBARUNG MIT BESSERUNGSSCHEIN

zwischen

 [Vor- und Nachname Gläubiger]
 [Anschrift]
 - im Folgenden "der Gläubiger" -

und

 [Firma der Schuldnerin]
 vertreten durch [Geschäftsführer]
 [Anschrift]
 HRB [...] AG [...]
 - im Folgenden "die Schuldnerin" -

1. Praeambel

Der Gläubiger ist Inhaber folgender Forderung gegen die Schuldnerin:

 [Bezeichnung der Forderung]
 Hauptforderung [Betrag] EUR
 zuzueglich Zinsen
 zum [Stichtag] insgesamt [Gesamtbetrag] EUR

Die Schuldnerin befindet sich in einer angespannten wirtschaftlichen Lage
und hat eine Fortbestehensprognose nach § 19 Abs. 2 InsO erstellt. Mit
Sanierungsbeitrag durch den Gläubiger ist die Prognose positiv.

2. Verzicht

2.1 Der Gläubiger verzichtet hiermit gegenüber der Schuldnerin auf die
oben bezeichnete Forderung in voller Höhe einschließlich Zinsen und
Nebenforderungen.

2.2 Die Forderung erlischt im Status der Schuldnerin und ist in der
insolvenzrechtlichen Status-Aufstellung nicht mehr zu passivieren.

3. Besserungsschein

3.1 Der Verzicht ist bedingt durch das Wiedererstarken der Zahlungsfähigkeit
der Schuldnerin.

3.2 Die Forderung lebt wieder auf wenn

 a) die Schuldnerin im Jahresabschluss ein positives Eigenkapital aufweist
 oder
 b) die Schuldnerin in einem Geschäftsjahr einen Jahresueberschuss von mehr
 als [X] EUR erwirtschaftet oder
 c) der Gläubiger bei nachhaltiger Verbesserung der wirtschaftlichen Lage
 in Textform die Wiederaufnahme verlangt.

3.3 Der Rückzahlungsbetrag betraegt im Fall des Wiederauflebens

 - höchstens den urspruenglichen Forderungsbetrag,
 - mindestens [X] Prozent des verfügbaren Eigenkapitals des Folgejahres,
 - wird in Raten über [N] Monate getilgt.

3.4 Die Besserungsklausel laeuft für [N] Jahre ab Unterzeichnung. Nach
Ablauf entfaellt die Wiederauflebensmöglichkeit endgültig.

4. Steuerliche Hinweise

Die Parteien sind sich bewusst dass dieser Verzicht beim Schuldner Ertrag
ausloest. Vor Unterzeichnung wurde steuerlicher Rat eingeholt.

5. Form und Wirksamkeit

5.1 Diese Vereinbarung ist beidseitig unterzeichnet wirksam.

5.2 Änderungen und Ergänzungen bedürfen der Schriftform.

5.3 Gerichtsstand: [Sitz der Schuldnerin].

[Ort], [Datum]

___________________________
[Gläubiger]

___________________________
[Geschäftsführer]
für die Schuldnerin
```

## Hinweise

### Echtheit der Sanierungsabsicht

Wird der Forderungsverzicht später als Scheingeschäft angesehen (z. B. weil keine ernsthafte Sanierungsabsicht vorlag) kann er anfechtbar sein.

### Gläubigergleichbehandlung

Bei Sanierungsverzicht ist auf Gläubigergleichbehandlung zu achten. Wenn nur einzelne Gläubiger verzichten und andere nicht ist das in Ordnung — solange der Vorgang nicht als Begueneten-Bezugnahme zu Lasten der nicht-verzichtenden Gläubiger zu werten ist.

### Besserungsschein-Trigger genau definieren

Der Trigger für das Wiederaufleben muss objektiv und nachprüfbar sein. Klauseln wie "wenn es uns wieder besser geht" sind ungeeignet.

## Ausgabe

- `forderungsverzicht-besserungsschein-<glaeubiger>.docx`.
- Steuerliche Prüfer-Flag — Steuerberater einbinden.
- Statusupdate (Skill `bilanzieller-status-aufnehmen`): Forderung entfaellt aus den Passiva.
- Eintrag im Sanierungsbausteine-Tracker.

## Aktuelle Leitentscheidungen — Forderungsverzicht und Besserungsschein

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Forderungsverzicht

§ 19 Abs. 2 InsO (Ueberschuldungsbereinigung) → § 3a EStG (steuerfreier Sanierungsgewinn) → § 397 BGB (Erlass/Verzicht) → § 158 BGB (haengende Bedingung Besserungsschein) → § 133 InsO (Anfechtungsrisiko bei selektivem Verzicht)

## Triage — Forderungsverzicht Check

1. **Glaeubiger und Betrag?** Wer verzichtet auf wie viel?
2. **Steuerliche Folge?** Sanierungsgewinn § 3a EStG: Nachweise Sanierungsplan, Sanierungsabsicht, Sanierungseignung vorbereiten.
3. **Besserungsschein-Formulierung?** Bedingung klar definiert (Wiederherstellung ZF anhand konkreter Liquiditaets-Schwelle).
4. **Anfechtungsschutz?** Verzicht muss Teil eines Gesamtsanierungskonzepts sein (IDW S 6 Qualitaet) um Vorsatzanfechtung § 133 InsO auszuschliessen.

---

## Skill: `kaltstart-interview`

_Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steuerliche Ansprechpartner ist welches Geschäftsjahr und welche Rechtsform vorliegt un..._

# /fortbestehensprognose:fortbestehensprognose-kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fortbestehensprognose** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Disclaimer (Schlüsselstelle)

Dieses Plugin liefert eine **Selbstdokumentation** der Fortbestehensprognose nach § 19 Abs. 2 InsO. Es ersetzt **nicht** die anwaltliche Prüfung durch einen Insolvenzrechtler bei Anzeichen für Insolvenzreife. Die Antragspflicht nach § 15a InsO (drei Wochen bei Zahlungsunfähigkeit, sechs Wochen bei Überschuldung) ist persönliche Pflicht des Geschäftsleiters mit strafrechtlicher Bewehrung (§ 15a Abs. 4 InsO) und Haftungsrisiko (§ 15b InsO, frühere § 64 GmbHG). Im Zweifel **vor** Ablauf der Frist Insolvenzanwalt konsultieren.

## Ablauf

1. Datei `~/.claude/plugins/config/claude-fuer-deutsches-recht/fortbestehensprognose/CLAUDE.md` prüfen.
2. Falls befüllt: bestätigen, gegebenenfalls --redo für Neu-Interview.
3. Andernfalls Interview unten ausführen.

## Interview

### 1. Wer nutzt das Plugin

- **Rolle:** Geschäftsführer GmbH / Vorstand AG / Geschäftsleiter Personengesellschaft / Gesellschafter mit Eigenverantwortung / Finanzleiter / sonst?
- **Persönliche Antragspflicht** nach § 15a InsO? Wer ist Geschäftsleiter mit Antragspflicht? Bei mehreren ist jeder einzeln verpflichtet (BGH-Rspr.).
- **Anwaltlicher Ansprechpartner** (Insolvenzanwalt) — Name, Erreichbarkeit. Bei negativer Prognose sofort eskalieren.
- **Steuerlicher Ansprechpartner** (Steuerberater / Wirtschaftsprüfer) — Name, Erreichbarkeit.

### 2. Unternehmensprofil

- **Rechtsform** GmbH AG GmbH und Co. KG Aktiengesellschaft Personengesellschaft.
- **Stammkapital** (relevant für Mantel- bzw. Anhalt-Insolvenzreife).
- **Geschäftsjahr** und Bilanzstichtag.
- **Branche** (relevant für Plausibilisierung).
- **Beschaeftigte** Anzahl.
- **Umsatz** im laufenden Jahr und Vorjahr.

### 3. Buchhaltung und Bilanzierung

- **Buchhaltungssoftware** DATEV Lexware SAP sevDesk sonst.
- **Bilanzierungsstandard** HGB / IFRS / Mischung.
- **Letzter Jahresabschluss** Datum.
- **Aktueller Stand** unterjaehrige BWA SuSa Konzernreporting verfügbar.

### 4. Ausgangslage

- Was hat den Anlass gegeben für diese Prüfung? (siehe Skill `ausloesendes-ereignis-erfassen`)
- Bilanzielle Überschuldung bereits festgestellt? (Aktiva kleiner als Passiva?)
- Stille Reserven oder Lasten vorhanden?
- Aktuelle Liquiditätslage subjektiv: angespannt? ausreichend? bereits überschritten?

### 5. Eskalationspfad

- **Ab welchem Befund** wird sofort der Insolvenzanwalt eingeschaltet? Empfehlung: bei jedem 🔴-Flag im Verlauf.
- **Drei-Wochen-Frist** § 15a InsO bei Zahlungsunfähigkeit (§ 17 InsO) ist persönliche Pflicht. **Sechs Wochen** bei Überschuldung (§ 19 InsO seit SanInsFoG 2021).
- **Kein Aufschieben** wegen Sanierungsverhandlungen — die Frist beginnt mit Eintritt der Insolvenzreife (objektives Kriterium).

### 6. Standort

- **Sitz und Insolvenzgericht** (Belegenheits-AG nach § 3 InsO).
- **Bundesland** (relevant für Justiznetzwerk).

## Rechtlicher Rahmen

- **InsO** § 15a (Antragspflicht), § 15b (Zahlungsverbot ab Insolvenzreife), § 17 (Zahlungsunfähigkeit), § 18 (drohende Zahlungsunfähigkeit, Prognose 24 Monate seit 2021), § 19 (Überschuldung, Fortbestehensprognose 12 Monate seit 2021).
- **StaRUG** §§ 29 ff. (Restrukturierungsrahmen vor Insolvenzreife), § 102 (Hinweispflicht Steuerberater).
- **IDW S 11** Beurteilung des Vorliegens von Insolvenzeröffnungsgründen.
- **IDW S 6** Anforderungen an Sanierungskonzepte.
- **GmbHG** § 64 a.F. — heute § 15b InsO.

## Ausgabe

Profil wird geschrieben. Empfohlene nächste Skills:

1. `/fortbestehensprognose:ausloesendes-ereignis-erfassen` — Anlass und Vorinformation
2. `/fortbestehensprognose:bilanzieller-status-aufnehmen` — Ausgangsfeststellung
3. `/fortbestehensprognose:annahmen-sammeln-fortfuehrung` — Prognoseannahmen
4. (parallel) `/liquiditaetsplanung` — für die rollierende 12-Monats-Liquidität

Bei aktuten Anzeichen für Zahlungsunfähigkeit (Liquiditätslücke über 10 Prozent seit mehr als drei Wochen) **sofort** Insolvenzanwalt einschalten und mit Plugin `insolvenzrecht` arbeiten — nicht in diesem Plugin weiterarbeiten.

## Rechtlicher Rahmen und Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Kaltstart

§ 19 InsO (Ueberschuldungsgrund) → § 15a InsO (Antragspflicht) → § 15b InsO (Zahlungs-/Haftungsrisiko) → § 43 GmbHG (Sorgfaltspflicht GF) → IDW S 11 (Standard Insolvenz-Beurteilung)

---

## Skill: `sanierungsbausteine-vorschlagen-annahmen`

_Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinbarungen Forderungsverzichte mit Besserungsschein Eigenkapita..._

# Sanierungsbausteine vorschlagen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Auswahlmatrix

Aus der Zusammenführung (Skill `fortbestehensprognose-zusammenfuehren`) ergibt sich die Lücke zwischen aktueller Liquidität / Bilanzbasis und der Schwelle zur positiven Fortbestehensprognose. Die Bausteine sind nach Effekt und Umsetzungszeit zu wählen.

| Baustein | Effekt | Umsetzungszeit | Skill |
|---|---|---|---|
| Externe harte Patronatserklärung | Liquiditäts- und Bilanzeffekt sofort | 1 bis 2 Tage | patronatserklaerung-extern-hart-erzeugen |
| Comfortletter (intern/weich) | Symbolisch / Reputation; kein Bilanzeffekt | 1 Tag | comfortletter-weich-erzeugen |
| Gesellschafterdarlehen mit Rangrücktritt | Bilanzeffekt sofort; Liquidität bei Auszahlung | 3 bis 7 Tage notariell | gesellschafterdarlehen-rangrücktritt |
| Forderungsverzicht mit Besserungsschein | Bilanzeffekt sofort | 5 bis 14 Tage | forderungsverzicht-besserungsschein |
| Stundung Forderung (Lieferant Bank) | Liquiditätseffekt sofort | 5 bis 10 Tage | stundungsanfrage-gläubiger |
| Kapitalerhöhung Gesellschafter | Bilanz- und Liquiditätseffekt | 14 bis 28 Tage notariell | (Plugin gesellschaftsrecht) |
| Sale-and-Lease-back | Liquidität einmalig | 14 bis 30 Tage | externe Bank |
| Kreditlinienerhöhung | Liquidität sofort wenn zugesagt | je nach Bank | externe Bank |
| StaRUG-Restrukturierungsplan | Vielschichtig — bei drohender Zahlungsunfähigkeit | mehrere Wochen | Plugin insolvenzrecht / StaRUG-Berater |

## Prüfraster pro Baustein

### Externe harte Patronatserklärung

- **Patron** muss bonitaer sein und sich gegenüber dem Begueneten **direkt** verpflichten.
- Patronatserklärung **schriftlich** mit **klarem Verzicht auf Insolvenzanforderung** im Insolvenzfall.
- Mehrwert: Forderung des Patrons gegen sich selbst (im Insolvenzfall) entlastet den Status.
- Skill `patronatserklaerung-extern-hart-erzeugen` mit Mustervorlage.

### Comfortletter (weich)

- **Nicht** ausreichend für die Fortbestehensprognose-Bilanzentlastung.
- Kann aber **Liquiditätsunterstützung** signalisieren (z. B. an Bank).
- Skill `comfortletter-weich-erzeugen`.

### Gesellschafterdarlehen mit qualifiziertem Rangrücktritt

- Bestehendes Gesellschafterdarlehen wird mit **qualifiziertem Rangrücktritt** versehen.
- Im Status nicht passiviert (§ 19 Abs. 2 S. 2 InsO).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Form: **notariell oder mit Schriftform unterzeichnet von beiden Parteien**.
- Skill `gesellschafterdarlehen-rangruecktritt`.

### Forderungsverzicht mit Besserungsschein

- Gläubiger verzichtet auf Forderung — im Insolvenzfall waere er ohnehin Auseinandersetzungsgläubiger.
- **Besserungsschein** lebt die Forderung wieder auf wenn das Unternehmen wieder zahlungsfähig.
- Steuerliche Folgen prüfen (Ertrag aus Forderungsverzicht — Sanierungsklausel § 3a EStG).
- Skill `forderungsverzicht-besserungsschein`.

### Stundungen

- Lieferanten Bank Steuern (Achtung: Steuerstundung § 222 AO) Sozialversicherung (sehr restriktiv).
- **Schriftlich** und mit **klarem Termin**.
- Skill `stundungsanfrage-glaeubiger`.

### Kapitalerhöhung

- Bareinlage durch Gesellschafter oder Sacheinlage (mit Sachgründungsbericht).
- Notarurkunde Handelsregistereintragung.
- Plugin `gesellschaftsrecht` (Skill kapitalerhöhung).

### Sale-and-Lease-back

- Verkauf eines Vermögenswerts (Maschine Grundstück) an Leasing-Geber mit anschließendem Leasing.
- Liquiditätseffekt einmalig.
- Folgekosten (Leasingraten) im Liquiditätsplan berücksichtigen.

### StaRUG-Restrukturierungsplan

- Nur bei **drohender** Zahlungsunfähigkeit (§ 18 InsO mit Prognose 24 Monate) — nicht bei akuter Zahlungsunfähigkeit oder Überschuldung.
- Restrukturierungsbeauftragter wird vom Gericht bestellt.
- Plan kann **mit Mehrheit der Gläubiger** durchgesetzt werden.
- Externe Begleitung durch StaRUG-Anwalt notwendig.

## Empfehlungslogik

```yaml
empfehlungen:
 zur-erreichung-positive-prognose:
 pflicht:
 - baustein: patronatserklaerung-extern-hart
 umfang: 200000 EUR
 patron: Hauptgesellschafter
 skill: patronatserklaerung-extern-hart-erzeugen
 prioritaet: kritisch
 umsetzung-bis: 2026-05-27

 empfohlen:
 - baustein: stundungsanfrage-glaeubiger
 anzahl: 5 Lieferanten
 skill: stundungsanfrage-glaeubiger
 prioritaet: hoch
 umsetzung-bis: 2026-06-15

 - baustein: gesellschafterdarlehen-rangruecktritt
 umfang: 120000 EUR bestehend
 skill: gesellschafterdarlehen-rangruecktritt
 prioritaet: hoch
 umsetzung-bis: 2026-05-25 notariell

 optional-bei-eskalation:
 - baustein: forderungsverzicht-besserungsschein
 umfang: 50000 EUR Bank
 skill: forderungsverzicht-besserungsschein
 prioritaet: mittel
 umsetzung-bis: 2026-06-30

 ergebnis-nach-massnahmen:
 bilanzbasis-vorher: positiv 133000 EUR
 bilanzbasis-nach-massnahmen: positiv 333000 EUR (zusätzlich Patronage 200000)
 liquiditaet-vorher-stress: negativ
 liquiditaet-nach-massnahmen-stress: positiv
 gesamtprognose: positiv mit Maßnahmen
```

## Zeitliche Reihenfolge

- **Sofort** (binnen Tagen): Patronatserklärung Rangrücktritt
- **Innerhalb Wochen** (drei Wochen Frist § 15a InsO bei Zahlungsunfähigkeit beachten): Stundungen Forderungsverzichte
- **Innerhalb Frist § 15a InsO Sechs Wochen**: alle Maßnahmen verbindlich
- **Bei Frist-Überschreitung**: keine zusätzliche Maßnahme mehr ausreichend — sofort Insolvenzantrag (Skill `wenn-prognose-negativ-naechste-schritte`).

## Ausgabe

- `sanierungsbausteine-empfehlung.md` mit konkreter Maßnahmenliste je Prioritaet.
- Nächste Skill-Verlinkungen je Maßnahme.
- Eintrag in Tagesnotizen zur Umsetzungskontrolle.
- Stichtag-Wiedervorlage in zwei Wochen zur Prüfung der tatsächlichen Umsetzung.

## Aktuelle Leitentscheidungen — Sanierungsbausteine

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Sanierungsbausteine

§ 19 Abs. 2 InsO (Fortbestehensprognose) → §§ 29 ff. StaRUG (vorinsolvenzliche Sanierung) → § 39 Abs. 4 InsO (Sanierungsprivileg Gesellschafterdarlehen) → § 3a EStG (steuerfreier Sanierungserloes) → § 133 InsO (Anfechtungsschutz bei echtem Sanierungskonzept)

## Triage — Sanierungsbaustein-Auswahl

1. **Zeitbedarf?** Patronatserklaerung/Rangruecktritt: 1-2 Tage. StaRUG-Plan: 4-8 Wochen. Kapitalerhöhung: 4-12 Wochen.
2. **Glaeubiger-Einbindung noetig?** Stundungsanfragen, Verzichte — Zustimmung einholen.
3. **Steuerliche Wirkung?** Sanierungserloes § 3a EStG: Voraussetzungen pruefen; Steuerberater einbinden.
4. **Gesamtkonzept?** Alle Bausteine zusammen muessen eine positive Prognose tragen (IDW S 11 Konformitaet).

---

## Skill: `start-chronologie-fristen`

_Einstieg, Schnelltriage und Fallrouting im Fortbestehensprognose-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenstän..._

# Fortbestehensprognose — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fortbestehensprognose**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz… |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand… |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK… |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten… |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht… |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im… |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und… |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab… |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `liquiditaet-12-monate` | Erstellt die rollierende Zwoelf-Monats-Liquiditaetsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib.… |
| `patronatserklaerung-extern-hart-erzeugen` | Erzeugt eine harte externe Patronatserklärung des Gesellschafters (oder eines Dritten) zugunsten der Gesellschaft. Erfasst Patron Begueneten Hoehe Bedingungen Laufzeit Insolvenzfeste Klausel. Zur Berücksichtigung im… |
| `prognose-dokumentation-stichtag` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg… |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit… |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause)… |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsverbot… |

## Worum geht es?

Dieses Plugin begleitet Geschaeftsfuehrer und Vorstande bei der Erstellung einer Fortbestehensprognose nach § 19 Abs. 2 InsO. Es dokumentiert Schritt für Schritt: ausloesende Ereignisse, bilanziellen Status, Fortfuehrungsannahmen, Plausibilisierung, rollende Zwoelf-Monats-Liquiditaet, Sensitivitaetsszenarien und Sanierungsbausteine (Patronatserklaerung, Comfortletter, Rangruecktritt, Stundung, Forderungsverzicht). Wenn die Prognose negativ ausfaellt, eskaliert das Plugin zum Pflichtenkatalog des Geschaeftsfuehrers nach §§ 15a, 15b InsO.

Das Plugin richtet sich an Eigenverantwortliche: Geschaeftsfuehrer, Vorstande und Finanzleiter — nicht als Ersatz für die Beauftragung eines Insolvenzrechtsanwalts.

## Wann brauchen Sie diese Skill?

- Der Steuerberater oder Wirtschaftspruefer weist auf negatives Eigenkapital oder bilanziellen Ueberschuldungsverdacht hin (§ 102 StaRUG).
- Das Unternehmen zeigt Liquiditaetsengpaesse und Sie als Geschaeftsfuehrer muessen dokumentieren, dass Sie aktiv gehandelt haben.
- Gesellschafter oder Banken verlangen eine Fortbestehensprognose als Voraussetzung für Unterstuetzungsmassnahmen.
- Sie pruefe Sanierungsbausteine (Gesellschafterdarlehen, Rangruecktritt, Patronatserklaerung) und wollen die insolvenzrechtliche Wirkung verstehen.
- Die Prognose ist knapp positiv oder negativ und Sie benoetigen den Pflichtenkatalog für die naechsten Schritte.

## Fachbegriffe (kurz erklaert)

- **Fortbestehensprognose** — Einschaetzung, ob das Unternehmen im Prognosezeitraum (ueblicherweise 12 Monate) ueberwiegend wahrscheinlich zahlungsfaehig bleiben wird (§ 19 Abs. 2 InsO, Massstab IDW S 11).
- **Ueberschuldung** — Passiva uebersteigen Aktiva nach bilanzieller Bewertung; bei positiver Fortbestehensprognose kein Insolvenzgrund nach § 19 Abs. 2 InsO.
- **Rangruecktritt** — Erklaerung des Gesellschafters, seine Darlehensforderung hinter alle anderen Glaeubiger zurueckzustellen; fuehrt zur Nichtpassivierung im insolvenzrechtlichen Status.
- **Patronatserklaerung (hart)** — Rechtsverbindliche Erklaerung des Gesellschafters oder Mutterunternehmens, die Tochtergesellschaft so auszustatten, dass sie zahlungsfaehig bleibt; beruecksichtigungsfaehig im Status.
- **Comfortletter** — Weiche Erklaerung des Patrons; nicht rechtsverbindlich; nicht ausreichend für insolvenzrechtlichen Status.
- **IDW S 11** — Institut der Wirtschaftspruefer, Standard 11: Massstab und Methodik für die Fortbestehensprognose.
- **StaRUG** — Gesetz ueber den Stabilisierungs- und Restrukturierungsrahmen; Option vor formeller Insolvenz.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit (Insolvenzgrund)
- § 18 InsO — Drohende Zahlungsunfaehigkeit (nur Eigenantrag; Prognosezeitraum 24 Monate)
- § 19 InsO — Ueberschuldung und Fortbestehensprognose (Prognosezeitraum **12 Monate** seit 01.01.2024; SanInsKG-Verkürzung auf 4 Monate galt nur bis 31.12.2023, ist nicht verlängert worden)
- § 15a InsO — Insolvenzantragspflicht (sechs Wochen bei Ueberschuldung, drei Wochen bei Zahlungsunfaehigkeit)
- § 15b InsO — Zahlungsverbot und Haftung bei Insolvenzverschleppung
- § 43 GmbHG — Haftung des Geschaeftsfuehrers
- §§ 1-93 StaRUG — Restrukturierungsrahmen
- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater-Hinweispflicht bei Krisensignalen; bei verfehlter Fortbestehensprognose haftet Berater. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung zugunsten des (faktischen) GF. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen GF. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- § 3a EStG — Steuerliche Behandlung Sanierungsgewinn

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer nutzt das Plugin (GF, Vorstand, Finanzleiter), Rechtsform, Geschaeftsjahr, Buchhaltungssystem.
2. Phase des Mandats bestimmen: Ausloeser erfassen, bilanzieller Status, Annahmen, Plausibilisierung, Liquiditaetsplanung oder Sanierungsbaustein-Erstellung.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Dreiwochenfrist Zahlungsunfaehigkeit, Sechswochenfrist Ueberschuldung nach § 15a InsO.
5. Anschluss-Skill bestimmen: Wenn Prognose negativ, sofort `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einbinden.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Einstieg**

- `fortbestehensprognose-kaltstart-interview` — Ersteinrichtung: Rolle, Rechtsform, Ansprechpartner, Buchhaltungssystem und Profil schreiben.

**Aufnahme und Analyse**

- `ausloesendes-ereignis-erfassen` — Dokumentiert Anlass, Datum, Hinweisgeber und Mitteilungsform der Fortbestehenspruefung.
- `bilanzieller-status-aufnehmen` — Nimmt Aktiva, Passiva, Eigenkapital und ausserbilanzielle Verpflichtungen auf; prueft bilanziellen Ueberschuldungsverdacht.
- `annahmen-sammeln-fortfuehrung` — Sammelt Fortfuehrungsannahmen zu Umsatz, Kosten, Personal, Investitionen und Working Capital.
- `annahmen-belastbarkeit-plausibilisieren` — Plausibilisiert Annahmen gegen Vergangenheit und Marktentwicklung; erzeugt Plausibilitaetsprotokoll.
- `liquiditaet-12-monate` — Rollende Zwoelf-Monats-Liquiditaetsvorschau mit Einzahlungen, Auszahlungen und Linienverbleib.

**Sanierungsbausteine (Dokumente erzeugen)**

- `sanierungsbausteine-vorschlagen` — Empfehlungsmatrix für Sanierungsmassnahmen nach Effekt und Umsetzungszeit.
- `patronatserklaerung-extern-hart-erzeugen` — Harte externe Patronatserklaerung als DOCX zur Unterzeichnung erzeugen.
- `comfortletter-weich-erzeugen` — Comfortletter (weich, nicht rechtsverbindlich) erstellen mit Warnhinweis zur insolvenzrechtlichen Wirkung.
- `gesellschafterdarlehen-rangruecktritt` — BGH-konforme Rangruecktrittserklaerung nach § 19 Abs. 2 S. 2 InsO erzeugen.
- `forderungsverzicht-besserungsschein` — Forderungsverzicht mit Besserungsschein erstellen mit steuerlichen Hinweisen.
- `stundungsanfrage-glaeubiger` — Stundungsanfragen an Glaeubiger (Lieferanten, Bank, Finanzamt, Sozialversicherung) individuell erstellen.

**Prognose und Dokumentation**

- `fortbestehensprognose-zusammenfuehren` — Alle Bausteine zusammenfuehren und Gesamtbewertung nach IDW S 11 erstellen.
- `prognose-dokumentation-stichtag` — Abschliessende Selbstdokumentation zum Stichtag als Haftungsbeleg.

**Eskalation**

- `wenn-prognose-negativ-naechste-schritte` — Pflichtenkatalog bei negativer Prognose: § 15a InsO, § 15b InsO, StaRUG-Option, Insolvenzanwalt.

## Worauf besonders achten

- **Selbstdokumentation ersetzt keinen Insolvenzrechtsanwalt.** Das Plugin hilft GF bei Eigenverantwortung; bei negativer oder knapp positiver Prognose ist Fachanwaltskonsultation zwingend.
- **Rangruecktritt muss BGH-konform formuliert sein.** Fehlformulierungen sind insolvenzrechtlich wirkungslos; Skill `gesellschafterdarlehen-rangruecktritt` liefert BGH-konforme Formulierung.
- **Nur harte Patronatserklaerung ist beruecksichtigungsfaehig.** Comfortletter reicht nicht aus; das Plugin weist explizit darauf hin.
- **Dreiwochenfrist laeuft ohne Hemmung.** Sobald Zahlungsunfaehigkeit eingetreten ist, laeuft § 15a InsO-Frist ohne Moeglichkeit der Verlaengerung.
- **Steuerliche Folgen von Sanierungsgewinn beachten.** Forderungsverzicht loest beim Schuldner Ertrag aus; Skill `forderungsverzicht-besserungsschein` enthaelt entsprechenden Hinweis.

## Typische Fehler

- Prognose wird auf der Basis zu optimistischer Annahmen erstellt ohne Plausibilisierung gegen Vergangenheit und Markt.
- Bilanzieller Status wird mit insolvenzrechtlichem Status gleichgesetzt; beide koennen abweichen (stille Reserven, Rangruecktritt).
- Comfortletter wird als ausreichend für positiven Status behandelt; fuehrt zu fehlerhafter Prognose.
- Dokumentation erfolgt nach dem Ereignis (nachtraeglich), nicht zum Stichtag; Haftungsschutz entfaellt.
- Steuerwirkung des Sanierungsgewinns (§ 3a EStG) wird nicht beachtet; unerwartete Steuerlast.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (InsO, StaRUG, GmbHG, EStG, BGB)
- IDW S 11 (Fortbestehensprognose) und IDW S 6 (Sanierungskonzept) in geltender Fassung

---

## Skill: `stundungsanfrage-glaeubiger`

_Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause) Begründung Sicherheitsangebot. Pro Gläubiger eigenes Schreiben. Hinweis Steuerstu..._

# Stundungsanfrage Gläubiger

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Wirkung in der Liquiditätsplanung

Eine Stundung verschiebt die Fälligkeit eines Liquiditätsabflusses nach hinten oder verteilt ihn in Raten. Wirkung:

- **Verbessert** die Liquidität im Stundungszeitraum.
- **Verschlechtert** die Liquidität im Folgezeitraum (es sei denn umgekehrt durch operativ erwirtschaftete Mittel kompensiert).
- **Nur schriftlich** im Liquiditätsplan ansetzen.

Eine muendlich erbetene und nicht schriftlich zugestandene Stundung darf nicht in den Liquiditätsplan eingebaut werden.

## Kategorien der Gläubiger

### 1. Lieferanten

- Regelmäßig **bilateral verhandelbar**.
- Beziehungs-Vorteil: Lieferanten haben Interesse an Fortführung des Kunden.
- Empfehlung: schriftliche Stundungsanfrage mit konkretem Verzugsplan und ggf. **Teilzahlung als Goodwill-Geste**.

### 2. Bank

- Bei bestehenden Darlehen Tilgungspause oder Verlängerung.
- Bei Kreditlinie Erhöhung oder Verlängerung.
- Bank verlangt regelmäßig **Sanierungskonzept** (IDW S 6) oder zumindest die Fortbestehensprognose.
- Verhandlung erfordert Bankgespräch — schriftliche Stundungszusage ggf. erst nach Prüfung.

### 3. Vermieter

- Verhandlung möglich. Mietkündigung gemäß BGB § 543 wegen Zahlungsverzug nicht stundungsfähig — Verzug muss vermieden werden.
- Schriftliche Stundungszusage erforderlich.

### 4. Steueramt (§ 222 AO)

- **Erhebliche Härte** muss vorliegen (§ 222 S. 1 AO).
- Stundung ist **Ermessensentscheidung** der Finanzbehörde.
- Bei drohender Insolvenz oft restriktiv.
- Sicherheitsleistung verlangt (§ 222 S. 2 AO).
- Hinweis: Lohnsteuer kann **nicht** gestundet werden (§ 222 S. 3 AO i.V.m. § 41a EStG).

### 5. Sozialversicherungsträger (§ 76 Abs. 2 SGB IV)

- **Sehr restriktiv** — nur in Ausnahmefällen.
- Sozialversicherungsbeitraege sind treuhaenderisch und Arbeitnehmer-Anteil.
- Nichtabführung kann § 266a StGB auslösen (Vorenthalten Sozialversicherungsbeitraege Arbeitnehmer-Anteil).
- **Pflicht zur Abführung** der Arbeitnehmer-Beitraege bleibt grundsaetzlich auch bei Stundung — daher Stundung praktisch fast unwirksam.

## Mustervorlage Lieferant

```
[Briefkopf der Gesellschaft]

[Datum]

An [Lieferant]
[Anschrift]

Betreff: Stundungsanfrage Rechnungen Nr. [...] vom [...]

Sehr geehrte Damen und Herren,

mit Bezug auf die offenen Rechnungen

 Rechnung Nr. [...] vom [...] in Höhe von [...] EUR (fällig [...])
 Rechnung Nr. [...] vom [...] in Höhe von [...] EUR (fällig [...])
 Gesamt offene Forderung: [...] EUR

bitten wir Sie um Stundung wie folgt:

 - Fälligkeit verschoben auf [neues Datum]
 - alternativ Ratenzahlung in [N] gleichen Monatsraten ab [Datum]
 - Erste Rate in Höhe von [...] EUR überweisen wir bereits am [...]

Hintergrund: Unsere Gesellschaft befindet sich in einer angespannten
wirtschaftlichen Phase die wir aktiv durch Maßnahmen (Standortoptimierung
Patronatserklärung des Hauptgesellschafters Erhöhung der Kreditlinie)
gegensteuern. Eine vollständige Fortbestehensprognose nach § 19 Abs. 2 InsO
liegt unserer Geschäftsführung vor; sie weist mit Maßnahmen positive
Wahrscheinlichkeit aus.

Wir versichern Ihnen dass die Lieferung und Zahlung in der Geschäftsbeziehung
absolute Prioritaet hat. Unsere Beziehung zu Ihnen ist langfristig und wir
sehen unsere Verpflichtung gegenüber Ihnen ausserordentlich.

Eine schriftliche Bestätigung der Stundung erbitten wir bis zum [Datum].

Mit freundlichen Grüßen

[Geschäftsführer]
```

## Mustervorlage Bank

```
[Briefkopf der Gesellschaft]

[Datum]

An [Bank]
[Anschrift]

Betreff: Antrag auf Tilgungspause Darlehen Nr. [...] / Verlängerung
 Kreditlinie

Sehr geehrte Damen und Herren,

mit Verweis auf unsere bestehende Geschäftsbeziehung beantragen wir:

1. Tilgungspause für das Darlehen Nr. [...] in Höhe von [...] EUR für einen
Zeitraum von [...] Monaten (von [...] bis [...]).

2. Verlängerung der Kreditlinie (Linie [...] EUR) bis zum [...].

Hintergrund: Unsere Gesellschaft befindet sich in einer wirtschaftlich
angespannten Phase die wir aktiv durch Maßnahmen gegensteuern. Eine
Fortbestehensprognose nach § 19 Abs. 2 InsO liegt vor und weist mit unseren
laufenden Sanierungsmaßnahmen einschließlich Patronatserklärung des
Hauptgesellschafters in Höhe von [...] EUR positive Wahrscheinlichkeit auf
die Fortfuehrung im Prognosezeitraum von zwölf Monaten.

Wir übersenden Ihnen vorab:

 - Fortbestehensprognose mit Stichtag [...]
 - Patronatserklärung des Hauptgesellschafters vom [...]
 - 12-Monats-Liquiditätsplan einschließlich Sensitivitaetsszenarien

Für ein persönliches Gespraech sind wir gerne kurzfristig verfügbar.

Mit freundlichen Grüßen

[Geschäftsführer]
```

## Mustervorlage Steueramt (§ 222 AO)

```
[Briefkopf der Gesellschaft]

[Datum]

An das Finanzamt [...]
[Anschrift]

Steuernummer: [...]

Betreff: Antrag auf Stundung gemäß § 222 AO

Sehr geehrte Damen und Herren,

namens und im Auftrag der oben genannten Gesellschaft beantragen wir gemäß
§ 222 AO Stundung der nachstehenden Steuern:

 Koerperschaftsteuer Vorauszahlung Q2/2026, fällig [...]: [...] EUR
 Solidaritaetszuschlag, fällig [...]: [...] EUR
 Gewerbesteuer Vorauszahlung Q2/2026, fällig [...]: [...] EUR

bis zum [neues Datum] beziehungsweise alternativ Ratenzahlung in
[N] Monatsraten ab [...].

Begründung: Die Erhebung der Steuer in der gesetzten Frist würde eine
erhebliche Haerte für die Steuerpflichtige bedeuten. Ihre wirtschaftliche
Lage ist angespannt; eine Fortbestehensprognose mit positiver Wahrscheinlichkeit
ist erstellt. Die laufenden Verhandlungen mit Patronen und Kreditgebern
zeigen positive Entwicklung; mit Vollzug der Sanierungsbausteine ist die
fristgerechte Zahlung gesichert.

Über Sicherheitsleistung ($ 222 S. 2 AO) sind wir gerne im Gespraech
(z. B. Bürgschaft des Patrons Sicherungsuebereignung Maschinen).

Auf Verlangen reichen wir Folgendes nach:

 - Fortbestehensprognose mit Stichtag [...]
 - Aktueller Liquiditätsplan
 - Patronatserklärung des Hauptgesellschafters

Lohnsteuer und Umsatzsteuer (Treuhand-Steuern) sind hiervon ausdrücklich nicht
betroffen. Diese werden weiterhin fristgerecht abgeführt.

Mit freundlichen Grüßen

[Geschäftsführer]
```

## Schriftliche Stundungszusage

Erst nach **schriftlicher** Stundungszusage des Gläubigers darf die Fälligkeit im Liquiditätsplan verschoben werden.

```yaml
stundungen:
 - glaeubiger: Lieferant XYZ GmbH
 offene-forderung: 24000
 urspruengliche-faelligkeit: 2026-06-15
 gestundete-faelligkeit: 2026-09-15
 zusage-vom: 2026-06-05
 zusage-form: E-Mail mit Bestätigung
 bemerkung: Anzahlung 5000 EUR mit Stundungserklärung gezahlt
```

## Ausgabe

- Pro Gläubiger eigenes `stundungsanfrage-<glaeubiger>.docx`.
- Versand per Einschreiben oder über Bank-Portal / E-Mail.
- Wiedervorlage zur Prüfung der Zusage in 14 Tagen.
- Tracker mit Status (versendet / zugesagt / abgelehnt / verhandlung).
- Hinweis: bei Ablehnung Liquiditätsplan-Update mit weiteren Maßnahmen erforderlich.

## Aktuelle Leitentscheidungen — Stundungsanfragen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Stundungsanfragen

§ 271 BGB (Faelligkeit) → § 222 AO (Stundung Steuer) → § 76 SGB IV (Stundung SV-Beitraege) → § 17 InsO (ZU-Beseitigung durch Stundung) → § 130 InsO (Anfechtungsrisiko bei Stundungsvereinbarung)

## Triage — Stundungsanfrage-Strategie

1. **Glaeubiger-Typ?** Lieferant (oft kulant), Bank (meist rigide), FA (sachliche Haerte erforderlich), SV-Traeger (sehr restriktiv).
2. **Stundungszeitraum?** Realistischer Zeitraum bis zur Liquiditaetsverbesserung angeben.
3. **Sicherheitsangebot?** Abtretung Forderungen, Eigentuemervorbehalt-Verlaengerung, persönliche Buergschaft GF?
4. **Anfechtungsrisiko?** Stundungsvereinbarung in Krisenzeit + spaetere Zahlung = § 130 InsO Risiko; FA-Stundungsantrag schriftlich und mit Liquiditaetsplan belegen.

## Output-Template Stundungsschreiben an Finanzamt

**Adressat:** Finanzamt [ORT] — Tonfall: sachlich-erklaerend

```
Stundungsantrag nach § 222 AO
Steuernummer: [STEUERNUMMER]
Schuldner: [FIRMA]
Datum: [DATUM]

Sehr geehrte Damen und Herren,

wir beantragen Stundung der faelligen Steuerverbindlichkeiten aus [Steuerbescheid vom DATUM, Az. XX]
in Hoehe von EUR [BETRAG] bis zum [DATUM].

Begruendung:
[FIRMA] befindet sich in einer voruibergehenden Liquiditaetsengpass-Situation aufgrund [Ursache].
Eine detaillierte Liquiditaetsplanung liegt als Anlage bei (Anlage 1 — 13-Wochen-Forecast).
Nach aktueller Planung ist die Begleichung der Steuerschuld bis [DATUM] moeglich.

Wir bitten um Stundung ohne Saumniszuschlaege für den genannten Zeitraum.

Anlagen: Liquiditaetsplanung (Anlage 1), aktuelle BWA (Anlage 2)
```

---

## Skill: `zusammenfuehren`

_Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfä..._

# Fortbestehensprognose zusammenführen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Maßstab

§ 19 Abs. 2 InsO seit SanInsFoG 2021: "Die Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich" — Prognosezeitraum **zwölf Monate**.

**Überwiegend wahrscheinlich** bedeutet **mehr als 50 Prozent** Wahrscheinlichkeit (klassische BGH-Rspr. zur Vorhersage; bestätigt durch IDW S 11).

### Operativ — was bedeutet das?

Die abstrakte Wahrscheinlichkeitsformel ist methodisch durch die **Zahlungsfähigkeitsprognose** zu fuellen. Die Fortbestehensprognose ist genau dann positiv wenn das Unternehmen über den Zwölf-Monats-Horizont mit überwiegender Wahrscheinlichkeit **nicht in die Zahlungsunfähigkeit nach § 17 InsO gerät**. Das bedeutet konkret:

- In jedem Zeitabschnitt der zwölf Monate müssen **mindestens 90 Prozent** der dann fälligen Verbindlichkeiten aus den verfügbaren Mitteln (Liquiditätsbestand plus Kreditlinie plus rechtzeitig erzielbare Zufluesse) gedeckt werden können.
- Maßstab: BGH-Linie zum 10-%-/3-Wochen-Schema (Zahlungsstockung vs. Zahlungsunfähigkeit). Konkrete Aktenzeichen vor Ausgabe über dejure.org / openjur.de mit Datum und Randnummer verifizieren.

Wenn die Liquiditätsplanung in jedem Zeitabschnitt diese Schwelle einhaelt — auch im plausibilisierten Negativ-Szenario — ist die Fortbestehensprognose **positiv**. Wenn die Schwelle in einem oder mehreren Zeitabschnitten oder über laengere Phasen reisst und auch durch Sanierungsbausteine nicht verbindlich geschlossen werden kann ist die Prognose **negativ**.

Die "mehr als 50 Prozent Wahrscheinlichkeit" der Prognose ist also nicht abstrakt zu vermuten sondern aus dem Liquiditätsplan und seiner Sensitivitaet abzuleiten: über das Basis-Szenario hinaus muss auch das **plausible Negativ-Szenario** die Schwelle einhalten — andernfalls reicht die Wahrscheinlichkeit nicht aus.

## Abgrenzung zur Sanierungsfähigkeit

Die positive Fortbestehensprognose ist nicht automatisch ein tragfähiges Sanierungskonzept. Sie beantwortet primär die insolvenzrechtliche Zahlungsfähigkeitsfrage. Sanierungsfähigkeit geht weiter:

- **Fortbestehensprognose:** Kann das Unternehmen im Prognosezeitraum überwiegend wahrscheinlich zahlungsfähig bleiben?
- **Sanierungsfähigkeit:** Ist das Unternehmen nach Maßnahmen wieder dauerhaft wettbewerbs-, rendite- und finanzierungsfähig?
- **Sanierungskonzept:** Verbindet Ausgangslage, Krisenursachen, Leitbild, Maßnahmen, integrierte GuV-/Bilanz-/Liquiditätsplanung, Szenarien und Dokumentation.

Wenn der Nutzer Bankgespräch, StaRUG, Schutzschirm, Eigenverwaltung, Insolvenzplan oder Sanierungskonzept nennt, nach der Fortbestehensprognose ausdrücklich den Sanierungsfähigkeits-Check empfehlen. Eine einmalige Finanzierungszusage kann die Fortbestehensprognose tragen, aber trotzdem kein nachhaltig saniertes Geschäftsmodell ergeben.

## Prüfablauf

### Schritt 1 — Bilanzielle Überschuldung gegeben?

Aus Skill `bilanzieller-status-aufnehmen`:

- Bilanzielle Überschuldung gegeben? Wenn nein: § 19 InsO nicht erfüllt — Fortbestehensprognose **nicht erforderlich** (aber häufig sinnvoll als Krisendokumentation).
- Wenn ja: weiter zu Schritt 2.

### Schritt 2 — Annahmen plausibilisiert?

Aus Skill `annahmen-belastbarkeit-plausibilisieren`:

- Annahmen überwiegend **realistisch** oder **konservativ**?
- Maximal eine oder zwei **ambitionierte** Annahmen die nicht tragend sind?
- **Nicht-belastbare** Annahmen ausgeschlossen?

Wenn die Annahmen die das Ergebnis tragen ambitioniert oder nicht-belastbar sind: Prognose **nicht positiv**.

### Schritt 3 — Liquidität über 12 Monate positiv

Aus Skill `liquiditaet-12-monate`:

- **Basis-Szenario** positiv über alle zwölf Monate?
- **Negativ-Szenario** mit zumutbaren Maßnahmen abdeckbar?
- **Stress-Szenario** zumindest mit zusätzlichen Maßnahmen (Patronatserklärung Gesellschafterdarlehen) abdeckbar?

### Schritt 4 — Gesamtbewertung

Drei mögliche Ergebnisse:

#### A. Prognose positiv

- Bilanzbild trotz Überschuldung positiv (stille Reserven Rangrücktritt).
- Liquidität über zwölf Monate positiv im Basis-Szenario und im Negativ-Szenario.
- Annahmen plausibel und überwiegend belegt.
- Sanierungsmaßnahmen falls noch erforderlich umgesetzt oder vertraglich gesichert.

**Folge**: Keine insolvenzrechtliche Überschuldung nach § 19 Abs. 2 InsO. Antragspflicht entfaellt insoweit. **Aber**: Zahlungsfähigkeit § 17 InsO und drohende Zahlungsunfähigkeit § 18 InsO bleiben **eigene** Prüfungspunkte — siehe Plugin `insolvenzrecht`.

#### B. Prognose positiv mit Sanierungsmaßnahmen

- Ohne Maßnahmen waere die Prognose negativ.
- Mit konkreten umsetzbaren Maßnahmen ist die Prognose positiv.

**Folge**: Maßnahmen müssen tatsächlich umgesetzt werden. Skill `sanierungsbausteine-vorschlagen` mit konkreten Vorschlägen.

**Wichtig**: Maßnahmen müssen **rechtzeitig** umgesetzt und **verbindlich** sein:

- Patronatserklärung **schriftlich unterzeichnet** und vom Patron einsehbar.
- Gesellschafterdarlehen **mit qualifiziertem Rangrücktritt** notariell.
- Stundungsvereinbarungen **schriftlich** mit Gläubigern.
- Forderungsverzichte **schriftlich** ggf. mit Besserungsschein.

#### C. Prognose negativ

- Liquidität über zwölf Monate **nicht sicherstellbar**.
- Sanierungsmaßnahmen reichen nicht.
- Keine ausreichende Patronage- / Gesellschafterstuetzung.

**Folge**:
- **Insolvenzrechtliche Überschuldung gegeben** (§ 19 InsO).
- **Antragspflicht** sechs Wochen nach Eintritt § 15a Abs. 1 S. 2 InsO.
- **Sofort Insolvenzanwalt** einschalten — Skill `wenn-prognose-negativ-naechste-schritte`.
- Prüfung **drohende Zahlungsunfähigkeit** § 18 InsO mit StaRUG-Option (Prognosezeitraum 24 Monate).

## Stichtag und Dokumentation

Die Prognose ist immer auf den **Stichtag des Tages** zu beziehen an dem sie erstellt wird. Das Verhältnis Stichtag → 12 Monate ist rollierend.

```yaml
prognose-zusammenfassung:
 prognose-id: FP-2026-0001
 stichtag: 2026-05-20
 geschaeftsleiter: Mueller, Hans (GF GmbH XYZ)
 prognose-horizont: 2026-06 bis 2027-05

 bilanzbild:
 bilanzielle-ueberschuldung: ja (Höhe 82000 EUR)
 insolvenzrechtliche-bilanzbasis: positiv (133000 EUR)
 rangruecktritt: Gesellschafterdarlehen 120000 EUR
 stille-reserven: 175000 EUR

 liquiditaet:
 basis-szenario: positiv
 negativ-szenario: positiv knapp (Endbestand Monat 11 bei 8000 EUR)
 stress-szenario: negativ ohne Patronatserklärung positiv mit

 annahmen-belastbarkeit:
 realistisch: 7
 konservativ: 2
 ambitioniert: 1 (Kostensenkung Standortschliessung)
 nicht-belastbar: 0

 sanierungsmassnahmen-erforderlich: ja
 konkret-belegt:
 - Patronatserklärung Hauptgesellschafter 200000 EUR (unterzeichnet)
 - Gesellschafterdarlehen 120000 EUR mit Rangrücktritt (notariell)
 - Stundungsvereinbarungen Lieferanten (schriftlich von 5 Lieferanten)
 noch-offen:
 - Stundung Bank Tilgung (in Verhandlung — noch nicht schriftlich)

 ergebnis: positiv-mit-maßnahmen
 bewertung-wahrscheinlichkeit: überwiegend (mehr als 50 Prozent)

 pflicht-ueberpruefung: vierteljaehrlich oder bei wesentlicher Änderung
```

## Sonderfall — der konkrete Tag der Erstellung zählt

- Die Prognose ist **stichtagsbezogen**.
- Bei einer wesentlichen Änderung der Annahmen (Wegfall Hauptkunde Verlust Kreditlinie) muss die Prognose **neu erstellt** werden.
- Bei vierteljaehrlicher Routineprüfung — Dokumentation der laufenden Prüfung als Beweis für aktive Pflichterfüllung des Geschäftsleiters.

## Ausgabe

- `prognose-zusammenfassung.md` mit Stichtag Bewertung Beleg-Status.
- Weiterleitung an:
 - `sanierungsbausteine-vorschlagen` wenn Maßnahmen erforderlich.
 - `wenn-prognose-negativ-naechste-schritte` wenn Ergebnis negativ.
 - `prognose-dokumentation-stichtag` zur abschließenden Dokumentation.

## Aktuelle Leitentscheidungen — Zusammenfuehren der Prognose (Stand Mai 2026)

- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater haftet bei verfehlter Fortbestehensprognose auf Insolvenzvertiefungsschaden. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung der Hinweis- und Warnpflicht des Beraters zugunsten des (faktischen) GF. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen GF; bei negativer Prognose nach Amtsniederlegung weiterhin Haftungsexposition. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- Konkrete BGH-Linie zu IDW S 11-konformer Prognose-Plausibilität und qualifiziertem Rangrücktritt vor Ausgabe über dejure.org / openjur.de verifizieren.

## Paragrafenkette Prognose-Zusammenfuehren

§ 19 Abs. 2 InsO (Fortbestehensprognose als zweite Stufe Ueberschuldung) → IDW S 11 Rn. 60-90 (Ergebnis und Dokumentation) → § 15a InsO (Antragspflicht bei negativer Prognose) → § 15b InsO (Haftungsrisiko)

## Triage — Prognose-Ergebnis

1. **Positiv (Prognose grueen)?** → Dokumentieren (IDW S 11 Vorlage), Wiedervorlage in 3 Monaten, Sanierungsbausteine weiterverfolgen.
2. **Knapp positiv (mit Massnahmen)?** → Massnahmen konkretisieren und terminieren; Sicherheitsmarge pruefen.
3. **Negativ?** → Sofort `wenn-prognose-negativ-naechste-schritte` ausfuehren; Anwalt einschalten; Antragspflicht pruefen.

---

## Skill: `comfortletter-weich-erzeugen`

_Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechtsverbindlich durchsetzbar. Wirkung Reputation und Banken-Signal. Nicht ausreichend..._

# Comfortletter (weich)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Wirkung und Grenze

Der Comfortletter ist eine **moralische Unterstützungserklärung** ohne rechtliche Bindung. Er wirkt im Geschäftsverkehr (Bank Lieferant Investor) als **Reputations-Signal**.

**Wirkung im Status der Gesellschaft**:

- **Keine** Berücksichtigung als Aktivposten.
- **Keine** Wirkung auf die Fortbestehensprognose.
- **Reine** Unterstützungsabsichtserklärung.

Wer den Comfortletter mit einer harten externen Patronatserklärung verwechselt schiebt eine **Selbsttaeuschung** in den Status hinein. Bei späterer Insolvenz wird das aufgedeckt; Haftungsrisiko des Geschäftsleiters § 15b InsO und § 43 GmbHG.

## Wann sinnvoll

- **Bank-Signal**: Die Bank verlangt eine schriftliche Unterstützungsabsicht des Mutterunternehmens — nicht als Sicherheit aber als Indikator.
- **Lieferanten-Signal**: Beim Verhandeln mit Lieferanten kann der Comfortletter Vertrauen schaffen.
- **Investor-Signal**: Bei Verhandlungen mit potenziellen Investoren als "Soft Backing".

## Wann NICHT sinnvoll

- Als **alleinige** Maßnahme im Status der Gesellschaft.
- Wenn die Fortbestehensprognose ohne den Comfortletter negativ ist.
- Wenn der Patron tatsächlich bonitaer ist und eine harte Erklärung abgeben könnte (dann sollte er auch).

## Mustervorlage

```
COMFORTLETTER

[Briefkopf des Patrons]

[Datum]

An die Geschäftsführung
der [Firma der Gesellschaft]
[Anschrift]

Sehr geehrte(r) [Anrede Geschäftsführer],

als [Hauptgesellschafter / Mutterunternehmen / Patron] der [Firma der
Gesellschaft] übermitteln wir Ihnen hiermit die folgende
Unterstuetzungsabsichtserklärung:

1. Wir verfolgen mit Interesse die wirtschaftliche Entwicklung der Gesellschaft
und beobachten ihre Lage.

2. Wir beabsichtigen die Gesellschaft für die Erfüllung ihrer wirtschaftlichen
und finanziellen Verpflichtungen im Rahmen unseres unternehmerischen
Beurteilungsspielraums und nach unseren Möglichkeiten zu unterstützen.

3. Diese Erklärung stellt KEINE rechtsverbindliche Garantie und KEINE harte
Patronatserklärung dar. Sie begründet keine einklagbare Verpflichtung uns
gegenüber der Gesellschaft oder ihren Gläubigern.

4. Diese Erklärung kann jederzeit ohne Begründung schriftlich widerrufen
werden.

[Optionale Ergänzung — sehr behutsam]:

5. Wir werden im Falle einer akuten Liquiditätsenge unser unternehmerisches
Urteil dahingehend ausueben möglichst rechtzeitig Maßnahmen zu prüfen.

Mit freundlichen Grüßen

[Patron]
[Position]
```

## Hinweise

- Comfortletter sollte **klar als solchen** bezeichnet werden — keine missverständlichen Formulierungen die als Patronatserklärung gewertet werden könnten (im Streit wird das anhand des Wortlauts geprüft).
- **Schriftlich** und unterzeichnet.
- Im Geschäftsverkehr klar als unverbindlich kommunizieren.

## Ausgabe

- `comfortletter.docx` und PDF.
- Warnhinweis im Sanierungsbausteine-Tracker dass dieser Comfortletter die Prognose NICHT trägt.
- Empfehlung: parallel zum Comfortletter eine harte externe Patronatserklärung mit konkretem Höchstbetrag (Skill `patronatserklaerung-extern-hart-erzeugen`).

## Aktuelle Leitentscheidungen — Comfortletter

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Comfortletter

§ 19 Abs. 2 S. 2 InsO (Passivierungsverbot nur für qualifizierten Rangruecktritt) → § 311 BGB (vorvertragliche Haftung aus Comfortletter) → § 241 Abs. 2 BGB (Schutzpflichten) → § 43 GmbHG (Haftung der Konzernmutter)

## Triage — Comfortletter vs. Patronatserklaerung

1. **Zweck?** Bankgespraech, Fortbestehensprognose oder echte rechtliche Sicherung? → Banken akzeptieren oft Comfortletter; Prognose benoetigt harte Patronatserklaerung.
2. **Rechtsbindungswillen?** Comfortletter = keine Rechtsbindung; Patronatserklaerung = verbindlich.
3. **Formulierung?** Vage Formulierungen ("werden unterstuetzen") koennen trotzdem Haftung ausloesen.
4. **Alternative?** Ersetze Comfortletter durch qualifizierten Rangruecktritt oder harte Patronatserklaerung wenn Fortbestehensprognose abgesichert werden soll.

---

## Skill: `prognose-stichtag-stundungsanfrage-glaeubiger`

_Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg gegenüber dem Geschäftsleiter dass er aktiv geprüft hat (Haftung § 15b InsO §..._

# Prognose-Dokumentation Stichtag

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Pflichtinhalte

Die Dokumentation enthält:

1. **Stichtag** und Anlass
2. **Bilanzieller Status** zum Stichtag mit Aktiva Passiva Eigenkapital Stillen Reserven Stillen Lasten Rangrücktritt
3. **Insolvenzrechtliche Bilanzbasis** mit Rechnung
4. **Annahmen** im Einzelnen mit Belegen und Plausibilisierung
5. **12-Monats-Liquidität** in Szenarien Basis Negativ Stress
6. **Sanierungsbausteine** mit Status (verbindlich umgesetzt / in Verhandlung / geplant)
7. **Gesamtergebnis** mit Begründung
8. **Wiedervorlage-Termin**

## Dokumenten-Vorlage

```
FORTBESTEHENSPROGNOSE
nach § 19 Abs. 2 InsO

Gesellschaft: [Firma]
HRB: [Nummer], AG [Sitz]
Rechtsform: [GmbH / AG]

Stichtag der Prognose: [Datum]
Erstellt durch: [Geschäftsführer Name]
Prognosehorizont: [Monat plus zwölf Monate]

1. ANLASS

[Aus Skill ausloesendes-ereignis-erfassen — z. B. "Hinweis des Steuerberaters
nach § 102 StaRUG vom [Datum] mit dem Hinweis dass die Bilanz 2025 ein
negatives Eigenkapital von [Betrag] EUR aufweist und eine Fortbestehensprognose
nach § 19 Abs. 2 InsO erstellt werden soll."]

2. BILANZIELLER STATUS

[Aus Skill bilanzieller-status-aufnehmen — als knappe Tabelle mit
Aktiva-Passiva und ausweisbarer bilanzieller Überschuldung.]

3. STILLE RESERVEN UND LASTEN

[Stille Reserven mit Bewertung. Stille Lasten gegengerechnet.]

4. RANGRUECKTRITTE

[Forderungen mit qualifiziertem Rangrücktritt nach § 19 Abs. 2 S. 2 InsO.]

5. INSOLVENZRECHTLICHE BILANZBASIS

[Berechnung Aktiva plus Stille Reserven minus Stille Lasten gegen Passiva
minus Rangrücktritts-Forderungen.]

Ergebnis bilanzielle Prüfung: [positiv / negativ]
Höhe: [Betrag] EUR

6. ANNAHMEN FUER DIE FORTFUEHRUNG

[Aus Skill annahmen-sammeln-fortfuehrung. Pro Annahme:
Bezeichnung — Werte — Begründung — Beleg — Risiko.]

7. PLAUSIBILISIERUNG DER ANNAHMEN

[Aus Skill annahmen-belastbarkeit-plausibilisieren. Pro Annahme:
Band (realistisch / konservativ / ambitioniert / nicht-belastbar) —
Sensitivitaetsszenario.]

8. LIQUIDITAET ZWOELF MONATE

Basis-Szenario: [positiv / negativ / knapp positiv]
Negativ-Szenario: [...]
Stress-Szenario: [...]

[Tabelle mit Monatsendbestaenden je Szenario.]

9. SANIERUNGSBAUSTEINE

[Aus Skill sanierungsbausteine-vorschlagen.
Pro Baustein: Bezeichnung — Höhe — Umsetzungsstatus — Beleg.]

 - Patronatserklärung Hauptgesellschafter 200000 EUR — unterzeichnet
 am [Datum] — Anlage A1
 - Gesellschafterdarlehen 120000 EUR mit qualifiziertem Rangrücktritt —
 notariell beurkundet am [Datum] — Anlage A2
 - Stundungsvereinbarungen 5 Lieferanten — schriftlich vorhanden am
 [Datum] — Anlagen A3 bis A7

10. GESAMTBEWERTUNG

Maßstab: § 19 Abs. 2 InsO — überwiegend wahrscheinlich (mehr als 50 Prozent)
dass das Unternehmen im Prognosezeitraum von zwölf Monaten zahlungsfähig
fortgeführt werden kann.

Ergebnis: [POSITIV / POSITIV MIT MASSNAHMEN / NEGATIV]

Begründung:

[Konkrete Begründung in zwei bis fünf Sätzen. Bei "positiv mit Maßnahmen"
explizit aufzählen welche Maßnahmen umgesetzt sein müssen.]

Folge: [Keine Antragspflicht aus Überschuldung / Antragspflicht ausgeloest]

11. WIEDERVORLAGE

Diese Prognose ist zu aktualisieren:

 - vierteljaehrlich zum [nächster Stichtag]
 - bei jeder wesentlichen Änderung der Annahmen
 - bei Eintritt eines der negativen Ereignisse aus dem Stress-Szenario

12. ABSCHLIESSENDE ERKLAERUNG DES GESCHAEFTSFUEHRERS

Ich erklaere dass ich die obigen Annahmen sorgfaeltig geprüft und mit den
verfügbaren Informationen abgeglichen habe. Die Annahmen entsprechen meiner
objektiven Einschätzung zum Stichtag. Bei wesentlichen Änderungen werde ich
diese Prognose unverzueglich aktualisieren.

[Ort], [Datum]

___________________________
[Geschäftsführer]

ANLAGEN

 A1 Patronatserklärung Hauptgesellschafter
 A2 Gesellschafterdarlehen mit Rangrücktritt notariell
 A3 bis A7 Stundungsvereinbarungen
 A8 Liquiditätsplan 12 Monate (Excel)
 A9 Aktueller BWA SuSa
 A10 Hinweisschreiben Steuerberater § 102 StaRUG
 A11 Bilanz 2025 mit Anhang
```

## Aufbewahrung

- Original mit allen Anlagen in der Geschäftsleitungsakte.
- Kopie an Steuerberater und Insolvenzanwalt (falls eingebunden).
- Aufbewahrung mindestens **zehn Jahre** (Anlehnung an § 257 HGB Buchführungspflicht und ggf. § 147 AO).

## Bei späterer Insolvenz

Diese Dokumentation ist Beweis dass der Geschäftsleiter zum Stichtag eine **objektive** Prognose erstellt hat. Sie schuetzt im Haftungsprozess gegen Vorwuerfe:

- **§ 15a Abs. 4 InsO** Insolvenzverschleppung — wenn die Prognose zum Stichtag positiv war kann nicht angenommen werden dass der Geschäftsleiter den Insolvenzgrund kannte und ignorierte.
- **§ 15b InsO** Zahlungsverbot — wenn der Status zum Stichtag nicht-negativ war waren Zahlungen ab diesem Tag nicht zwingend pflichtwidrig.
- **§ 43 GmbHG** Sorgfaltspflicht — Dokumentation belegt dass der Geschäftsleiter aktiv und mit Sorgfalt geprüft hat.
- **§ 826 BGB** sittenwidrige Schädigung der Gläubiger — nicht erfüllt wenn objektive Prognose vorlag.

## Bei aktualisierter Prognose

Wenn die Prognose vierteljaehrlich aktualisiert wird, alte Prognosen aufheben und mit Stichtag-Vermerk archivieren. Die aktuelle Version bleibt federführend.

## Ausgabe

- `fortbestehensprognose-<datum>.docx` und PDF mit allen Anlagen.
- Sicherer Archivpfad: `fortbestehensprognose/protokolle/<stichtag>.zip` mit Anlagenkonvolut.
- Wiedervorlage-Eintrag im Kalender vierteljaehrlich.
- Bei "negativ" Eskalation an Insolvenzanwalt (Skill `wenn-prognose-negativ-naechste-schritte`).

## Aktuelle Leitentscheidungen — Dokumentation der Prognose (Stand Mai 2026)

- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater haftet bei verfehlter FBP; Dokumentation der Hinweise und der angenommenen Prognoseannahmen ist Pflicht. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung des Beratungsmandats; Dokumentation muss erkennbar machen, dass auch GF angesprochen ist. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Wissentlichkeitsausschluss; lückenlose Dokumentation des Prognose-Prozesses ist entscheidend für die Verteidigung gegen "positive Kenntnis"-Vorwurf.

## Paragrafenkette Dokumentation

§ 15b Abs. 1 InsO (Zahlungsverbot nach Insolvenzreife) → § 43 Abs. 1 GmbHG (Sorgfaltspflicht) → § 93 AktG (Vorstandshaftung) → IDW S 11 (Dokumentationsstandard) → GOBD (Aufbewahrungspflichten digitaler Dokumente)

## Triage — Dokumentations-Checkliste

1. **Stichtag festlegen?** Datum und Uhrzeit der Erstellung dokumentieren.
2. **Unterzeichnung?** Geschaeftsfuehrer unterschreibt Prognose (Beweisstueck bei spaeterer Haftungsfrage).
3. **Anlagen?** Alle Berechnungs-Spreadsheets, Auszuege, IDW S 11-Gutachten als Anlagen beifuegen.
4. **Wiedervorlage?** Naechste Aktualisierung terminieren (spaetestens nach 3 Monaten oder bei wesentlichen Aenderungen).

---

## Skill: `quellen-livecheck`

_Quellen-Live-Check für Fortbestehensprognose StaRUG/InsO: prüft Normen (§ 18 InsO drohende Zahlungsunfähigkeit, StaRUG §§ 1/14/49, IDW S 11) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Insolvenzgericht und Quellenhygiene nach references/quellenhygiene.md._

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fortbestehensprognose** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `annahmen-behoerden-gericht-und-registerweg` — Annahmen Behoerden Gericht und Registerweg
- `annahmen-belastbarkeit-plausibilisieren` — Annahmen Belastbarkeit Plausibilisieren
- `annahmen-sammeln-bilanzieller-status` — Annahmen Sammeln Bilanzieller Status
- `ausloesendes-ereignis-erfassen` — Ausloesendes Ereignis Erfassen
- `bilanzieller-status-aufnehmen` — Bilanzieller Status Aufnehmen
- `bilanzstatus-risikoampel-und-gegenargumente` — Bilanzstatus Risikoampel und Gegenargumente
- `comfortletter-sonderfall-edge` — Comfortletter Sonderfall Edge
- `comfortletter-weich-erzeugen` — Comfortletter Weich Erzeugen
- `eskalation-sonderfall-und-edge-case` — Eskalation Sonderfall und Edge Case
- `fbp-bankenkommunikation-waiver-integrierte` — FBP Bankenkommunikation Waiver Integrierte
- `fbp-integrierte-planung-bauleiter` — FBP Integrierte Planung Bauleiter
- `fbp-stresstest-szenarien-leitfaden` — FBP Stresstest Szenarien Leitfaden
- `fbp-zahlungsunfaehigkeit` — FBP Zahlungsunfaehigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (InsO, StaRUG, § 19 Abs) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fortbestehensprognose (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

