---
name: patentlizenzvertrag-drafting-review
description: "Patentlizenzvertrag Drafting Review: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Patentlizenzvertrag Drafting Review

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Patentlizenzvertrag Drafting Review** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patentlizenzvertrag-de-en-drafting` | Setzt Patentlizenz-Term-Sheets in deutsch-englische Vertragsklauseln um; erklärt Legal-English-Begriffe im deutschen Rechtskontext und vermeidet unklare Transaktionssprache. |
| `patentlizenzvertrag-review` | Prüft Patentlizenzverträge: Schutzrechte, Territory, Field of Use, Exklusivität, Unterlizenzen, Royalties, Milestones, Improvements, Inhaberschaft, Gewährleistung, Durchsetzung, Kündigung und Insolvenzrisiken. |
| `spezial-anspruchsentwurf-dokumentenmatrix-und-lueckenliste` | Anspruchsentwurf: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin patentrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Patentlizenzvertrag Drafting Review**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `patentlizenzvertrag-de-en-drafting`

**Fokus:** Setzt Patentlizenz-Term-Sheets in deutsch-englische Vertragsklauseln um; erklärt Legal-English-Begriffe im deutschen Rechtskontext und vermeidet unklare Transaktionssprache.

# Patentlizenzvertrag DE/EN

## Ziel

Term Sheet, E-Mail oder Mandantenbrief in verwendbare Klauselstruktur überführen. Englisch nur dort verwenden, wo es vertraglich gewollt ist; deutsche Rechtswirkung klar erklären.

## Variablenmapping

| Term-Sheet-Begriff | Vertragsstelle | Klärung |
| --- | --- | --- |
| Licensed Patents | Schedule Schutzrechte | Anmeldungen, erteilte Patente, Teilanmeldungen, Fortsetzungen |
| Territory | Grant Clause | Staaten, EP-Validierungen, Einheitspatent, Export |
| Field | Field of Use | Produkt, Indikation, Branche, Kundenkreis |
| Exclusivity | Grant / Covenants | exklusiv, sole, non-exclusive, carve-outs |
| Sublicense | Sublicensing | Konzern, Distributor, OEM, Consent |
| Royalty | Payment | Basis, Satz, Mindestlizenz, Audit |
| Improvements | IP Ownership | wer darf was anmelden und nutzen |

## Output

- vollständige Klauselstruktur.
- zweisprachige Definitionen.
- offene Variablenliste.
- Risikoübersicht für deutsche Rechtsanwendung.

## Stilregel

Begriffe wie "best efforts", "reasonable efforts", "affiliate", "change of control" und "material breach" nicht unkommentiert in deutsches Recht übernehmen. Definiere den Pflichtenmaßstab konkret.

## Pflicht-Klauseln im deutschen Rechtsrahmen

- **Rechtswahl / Gerichtsstand:** Rom-I-VO (EU 593/2008) für Vertragspflichten; bei Lizenzgeber-Sitz DE typischerweise deutsches Recht und Gerichtsstand DE; ICC-/DIS-Schiedsklausel als Alternative für grenzüberschreitende Lizenzen.
- **Kartellrechtskonformität:** Vertikal-GVO (EU 2022/720) und TT-GVO (EU 316/2014, Auflauf 30.04.2026, danach Folgeregelung prüfen!) für vertikale F&E- und Lizenzvereinbarungen.
- **Kernklauseln zwingend formulieren:**
 - Lizenzgegenstand (Patente / Patentfamilie konkret listen mit Az.).
 - Lizenzart (ausschließlich/nicht ausschließlich/Sublizenz).
 - Räumlicher Umfang (Territory).
 - Sachlicher Umfang (Field of Use).
 - Zeitliche Dauer (idR an Patentablauf gekoppelt).
 - Lizenzgebühr (running royalty Prozentsatz, Pauschallizenz, Mindestlizenz).
 - Auditrecht, Berichtspflicht (§ 259 BGB Rechenschaftspflicht).
 - Verbesserungen / Improvements (Eigentum, Cross-License?).
- **Mängelhaftung Patente:** § 311a BGB iVm § 437 BGB analog; § 312i BGB nicht anwendbar (kein Verbrauchergeschäft typischer Weise).
- **Nichtigkeit oder Beschränkung:** Anpassungsklausel (Pacta sunt servanda + Wegfall der Geschäftsgrundlage § 313 BGB).
- **Steuerklauseln:** Withholding Tax bei grenzüberschreitenden Lizenzen; § 50a EStG bei Vergütung an ausländische Lizenzgeber (Steuerabzug 15 %); DBA-Reduktion möglich.
- **Insolvenzfeste Strukturierung:** § 103 InsO Wahlrecht des Insolvenzverwalters; bei "ausschließliche Lizenz" Schutz vor Wegfall durch Insolvenz prüfen (str.).
- Falle: "Best efforts" in deutsches Recht — § 276 BGB Sorgfaltsmaßstab ist konkret zu definieren; "due diligence" reicht nicht ohne konkrete Pflichten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `patentlizenzvertrag-review`

**Fokus:** Prüft Patentlizenzverträge: Schutzrechte, Territory, Field of Use, Exklusivität, Unterlizenzen, Royalties, Milestones, Improvements, Inhaberschaft, Gewährleistung, Durchsetzung, Kündigung und Insolvenzrisiken.

# Patentlizenzvertrag prüfen

## Red-Flag-Check

| Thema | Frage |
| --- | --- |
| Schutzrechte | Welche Patente/Anmeldungen genau, welcher Rechtsstand, welche Länder? |
| Lizenzart | einfach, exklusiv, allein, konzernweit, nicht übertragbar? |
| Field of Use | Produktfeld technisch und wirtschaftlich klar? |
| Unterlizenz | erlaubt, zustimmungspflichtig, Konzern-/OEM-/Distributor-Abdeckung? |
| Gegenleistung | upfront, milestone, running royalty, Mindestumsatz, auditierbare Basis? |
| Verbesserungen | wem gehören Improvements, wer darf sie nutzen, wer muss anmelden? |
| Durchsetzung | wer klagt, wer trägt Kosten, wer kontrolliert Vergleich? |
| Gewährleistung | Bestand, Nichtverletzung, Inhaberschaft, technische Eignung sauber begrenzt? |
| Ende | Kündigung, Sell-off, Know-how-Rückgabe, Daten, Lagerbestand, Insolvenz? |

## Output

- Executive Summary.
- Klauselmatrix `OK / verhandeln / riskant / unklar`.
- konkrete Änderungswünsche.
- Verhandlungspunkte nach Priorität.
- Mandantenmail oder Redline-Kommentar.

## Typische Fehler

- Territory und validierte Länder widersprechen sich.
- Exklusivität kollidiert mit eigener Nutzung oder bestehenden Lizenzen.
- "Patent" meint Anmeldung, aber Vertrag behandelt es wie erteiltes Schutzrecht.
- Erfinderpersönlichkeitsrechte werden wie übertragbare Vermögensrechte formuliert.
- Royalty Base passt nicht zu Produktbündeln, Ersatzteilen oder Dienstleistungen.

## Pflicht-Normen und Doktrinen
- **§ 15 PatG:** Übertragung und Lizenz; Lizenz ist sukzessionsfest, wenn dinglich bestellt.
- **VertikalGVO (EU) 2022/720 + Leitlinien:** Marktanteils-Sicherheitshafen 30 %; Kernbeschränkungen (RPM, Gebiete) bleiben verboten.
- **TT-GVO (EU) 316/2014:** Gruppenfreistellung für Technologietransfer; Marktanteilsschwellen (20 % bei Wettbewerbern, 30 % bei Nichtwettbewerbern); Kernbeschränkungen Art. 4.
- **FRAND / SEP:** EuGH Huawei/ZTE, C-170/13, Urt. v. 16.07.2015 -- pflichtgemäßes Verhandlungsritual.
- **Insolvenz des Lizenzgebers:** § 103 InsO Wahlrecht des Insolvenzverwalters; einfache Lizenz erlischt nicht zwingend, aber Risiko der Anfechtung. Schutz durch ausschließliche Lizenz mit Eintragung im DPMA-Register (§ 30 PatG); ggf. Treuhand.
- **AGB-Recht / B2B:** §§ 305 ff. BGB greifen im B2B-Geschäft begrenzt, aber Inhaltskontrolle nach § 307 BGB bleibt; bei Massenverträgen Klauselrisiko.
- **Compliance:** Exportkontrolle (Dual-Use-VO (EU) 2021/821), Sanktionsrecht, Embargos.

## Praxis-Tipp
- Konkrete Beispiele für Royalty-Bemessung im Vertrag (Stücklohn vs. Umsatz), Audit-Right mit 12-Monats-Vorlauf, Vertraulichkeit auf 5-10 Jahre.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-anspruchsentwurf-dokumentenmatrix-und-lueckenliste`

**Fokus:** Anspruchsentwurf: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin patentrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anspruchsentwurf: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Anspruchsentwurf: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Anspruchsentwurf: Dokumentenmatrix, Lückenliste und Nachforderung / anspruchsentwurf dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FTO ist eine Arbeitsmethode, keine Rechtsquelle. Je nach Teilfrage PatG §§ 1-5, 9, 10, 14, 34, 64; EPÜ Art. 52-57 und 69; UPCA Art. 32 und 62; UPC-Verfahrensordnung; nationale Patentgesetze/Patentämter live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anspruchsentwurf** prüfen.
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
