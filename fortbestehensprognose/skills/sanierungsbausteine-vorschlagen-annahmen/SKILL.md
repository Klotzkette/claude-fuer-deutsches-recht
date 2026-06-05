---
name: sanierungsbausteine-vorschlagen-annahmen
description: "Sanierungsbausteine Vorschlagen Annahmen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sanierungsbausteine Vorschlagen Annahmen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Sanierungsbausteine Vorschlagen Annahmen** im Plugin Fortbestehensprognose (IDW S 11). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinbarungen Forderungsverzichte mit Besserungsschein Eigenkapitalmassnahme StaRUG-Restrukturierungsplan. Empfehlungsmatrix nach Effekt und Umsetzungszeit. Empfiehlt konkret welche Dokumente erzeugt werden sollten (Skills patronatserklärung-extern-hart-erzeugen gesellschafterdarlehen-rangrücktritt stundungsanfrage-gläubiger). |
| `spezial-annahmen-behoerden-gericht-und-registerweg` | Annahmen: Behörden-, Gerichts- oder Registerweg im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bilanzstatus-risikoampel-und-gegenargumente` | Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Fortbestehensprognose (IDW S 11) gilt für **Sanierungsbausteine Vorschlagen Annahmen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `sanierungsbausteine-vorschlagen`

**Fokus:** Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinbarungen Forderungsverzichte mit Besserungsschein Eigenkapitalmassnahme StaRUG-Restrukturierungsplan. Empfehlungsmatrix nach Effekt und Umsetzungszeit. Empfiehlt konkret welche Dokumente erzeugt werden sollten (Skills patronatserklärung-extern-hart-erzeugen gesellschafterdarlehen-rangrücktritt stundungsanfrage-gläubiger).

# Sanierungsbausteine vorschlagen

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

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `spezial-annahmen-behoerden-gericht-und-registerweg`

**Fokus:** Annahmen: Behörden-, Gerichts- oder Registerweg im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Annahmen: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Annahmen: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Annahmen: Behörden-, Gerichts- oder Registerweg / annahmen behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, IDW, StaRUG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Annahmen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-bilanzstatus-risikoampel-und-gegenargumente`

**Fokus:** Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fortbestehensprognose; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien / bilanzstatus risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, IDW, StaRUG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bilanzstatus** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Bilanzstatus § 19 InsO — zweistufige Prüfung
1. **Rechnerische Überschuldung** (Stufe 1):
 - Liquidationswertbilanz (nicht Fortführungsbilanz!) — Vermögensgegenstände zu Veräußerungswerten, Verbindlichkeiten in voller Höhe.
 - Eigenkapital negativ → rechnerische Überschuldung.
 - Wichtige Position: Stille Reserven aktivieren, Pensionsrückstellungen prüfen, immaterielle Vermögensgegenstände (Goodwill bei going-concern, Veräußerungswert bei Liquidation).
2. **Fortbestehensprognose** (Stufe 2):
 - Prognosezeitraum **12 Monate** (§ 19 Abs. 2 S. 1 InsO seit SanInsFoG).
 - Maßstab: „überwiegende Wahrscheinlichkeit" der Fortführungsfähigkeit — quantitativ > 50 Prozent.
 - Bei positiver Prognose: keine Überschuldung trotz rechnerischer Überschuldung.

## Verteidigungslinien Geschäftsführer
- **Rangrücktritt** § 39 Abs. 2 InsO: Gesellschafterforderungen werden als Eigenkapital behandelt — neutralisiert rechnerische Überschuldung. Achtung: nur **qualifizierter** Rangrücktritt zählt (nicht nur „bis zur Sanierung", sondern unter Beschränkung auf freies Vermögen).
- **Patronatserklärung / Comfortletter:** harte Patronatserklärung (rechtlich bindend, im Außen- oder Innenverhältnis) heilt Liquiditätslücke. Weiche Patronatserklärung (politisch-moralisch) reicht nicht.
- **Forderungsverzicht mit Besserungsschein:** Verzicht bedingt durch wirtschaftliche Verbesserung — entlastet Bilanz, ohne Gläubigerposition vollständig zu opfern.
- **Stundungsvereinbarungen:** Verschiebung der Fälligkeit — wirkt auf Liquiditätsplan, nicht auf rechnerische Überschuldung.
- **Kapitalerhöhung / Gesellschafterzuschuss:** wirkt direkt auf Eigenkapital.

## Risikoampel
- **ROT:** rechnerische Überschuldung und negative Prognose → Überschuldung § 19 InsO, Antragspflicht § 15a InsO 6 Wochen.
- **GELB:** rechnerische Überschuldung, aber Prognose tendenziell positiv mit erkennbaren Annahmenrisiken → Sensitivität, IDW EPS 11 nachschärfen.
- **GRÜN:** rechnerische Überschuldung neutralisiert (Rangrücktritt, Patronatserklärung) und Prognose positiv → keine Überschuldung.

## Anti-Halluzinations-Hinweise
- 12-Monats-Horizont (nicht 24!) für § 19 InsO seit SanInsFoG 2021.
- Pandemie-Sonderregelung (4 Monate temporär) ist ausgelaufen.
