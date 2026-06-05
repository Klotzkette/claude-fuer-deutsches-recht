---
name: ips-verfahrenswahl-restrukturierungsplan
description: "Ips Verfahrenswahl, Restrukturierungsplan Fristen Form Und Zustaendigkeit, Ips Darstellender Teil: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ips Verfahrenswahl, Restrukturierungsplan Fristen Form Und Zustaendigkeit, Ips Darstellender Teil

## Arbeitsbereich

Dieser Skill bündelt **Ips Verfahrenswahl, Restrukturierungsplan Fristen Form Und Zustaendigkeit, Ips Darstellender Teil** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ips-verfahrenswahl` | Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit Masse Zeitfenster Eingriffstiefe Gerichtsbedarf No-go-Schwellen. Output: Routenmatrix Empfehlung mit Bedingungen Risikoampel. Abgrenzung: nicht für Detailplanung der gewaehlten Route. |
| `spezial-restrukturierungsplan-fristen-form-und-zustaendigkeit` | Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg im Insolvenzplan und StaRUG: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `ips-darstellender-teil` | Darstellenden Teil des Insolvenzplans oder StaRUG-Plans vollständig verfassen. § 220 InsO § 6 StaRUG Darstellungspflichten. Prüfraster: Krisengeschichte Massnahmen Finanzplanung Vergleichsrechnung Sonderaktiva Sicherheiten Steuerfolgen Offenlegung Widerspruchsfreiheit. Output: Darstellender Teil als Entwurf Risiko- und Lueckenliste. Abgrenzung: nicht für gestaltenden Teil (ips-gestaltender-teil). |

## Arbeitsweg

Für **Ips Verfahrenswahl, Restrukturierungsplan Fristen Form Und Zustaendigkeit, Ips Darstellender Teil** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insolvenzplan-starug-planwerkstatt` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ips-verfahrenswahl`

**Fokus:** Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit Masse Zeitfenster Eingriffstiefe Gerichtsbedarf No-go-Schwellen. Output: Routenmatrix Empfehlung mit Bedingungen Risikoampel. Abgrenzung: nicht für Detailplanung der gewaehlten Route.

# Verfahrenswahl und Routenentscheidung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verfahrenswahl und Routenentscheidung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Den passenden Sanierungsrahmen auswählen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Drohende Zahlungsunfähigkeit, Zahlungsunfähigkeit, Überschuldung, Masse, Organpflichten und Zeitfenster erfassen.
2. Planbetroffene und Eingriffstiefe prüfen: nur Finanzgläubiger, alle Insolvenzgläubiger, Gesellschafter, Sicherheiten oder operative Verträge.
3. Gerichtsbedarf prüfen: Vorprüfung, Abstimmung, Stabilisierung, Planbestätigung oder Insolvenzverfahren.
4. No-go-Schwellen markieren, insbesondere Arbeitnehmerforderungen im StaRUG, Massefähigkeit, Insolvenzantragspflichten und ungesicherte Datenlage.

## Ausgabe

- Routenmatrix
- Empfehlung mit Bedingungen
- Risikoampel
- Entscheidungsnotiz

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und Leitentscheidungen (Stand Mai 2026)

- Eröffnungsgründe: § 17 InsO (ZU; Antragspflicht), § 18 InsO (drohende ZU; StaRUG-Zugang; Prognose 24 Monate), § 19 InsO (Überschuldung; Antragspflicht; Prognose 12 Monate seit 01.01.2024).
- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — StaRUG verfassungsrechtlich tragfähig; relevant für Verfahrenswahl bei börsennotierten AGs. <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers; bei Verfahrenswahl Haftungsrisiken sorgfältig dokumentieren. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>

## Paragrafenkette (Insolvenzplan / StaRUG)

§ 217 InsO (Plan-Option) → § 218 InsO (Plan-Vorlage) → §§ 220-221 InsO (darstellender und gestaltender Teil) → § 222 InsO (Gruppen) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Planbestaetigung) → § 254 InsO (Planwirkung) → §§ 7-39 StaRUG (StaRUG-Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown)

## Triage — Plan-Vorarbeiten

Bevor losgelegt wird, klaere:
1. **Verfahrensart?** InsO-Plan (§§ 217 ff. InsO) oder StaRUG-Restrukturierungsplan (§§ 7-39 StaRUG)?
2. **Klassenbildung schluessig?** § 222 InsO / § 10 StaRUG — gleiche Rechte und Interessen je Gruppe.
3. **Mehrheits-Simulation?** Ist 75%-Schwelle (StaRUG) oder 50%+50% (InsO) realistisch?
4. **Vergleichsrechnung?** Liquidationswert als Referenz fuer Best-Interest-Test berechnen.
5. **Cramdown-Szenario?** Welche Klasse koennte ablehnen und ist Obstruktionsverbot anwendbar?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `spezial-restrukturierungsplan-fristen-form-und-zustaendigkeit`

**Fokus:** Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg im Insolvenzplan und StaRUG: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Restrukturierungsplan: Fristen, Form, Zuständigkeit und Rechtsweg / restrukturierungsplan fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Restrukturierungsplan** prüfen.
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

## 3. `ips-darstellender-teil`

**Fokus:** Darstellenden Teil des Insolvenzplans oder StaRUG-Plans vollständig verfassen. § 220 InsO § 6 StaRUG Darstellungspflichten. Prüfraster: Krisengeschichte Massnahmen Finanzplanung Vergleichsrechnung Sonderaktiva Sicherheiten Steuerfolgen Offenlegung Widerspruchsfreiheit. Output: Darstellender Teil als Entwurf Risiko- und Lueckenliste. Abgrenzung: nicht für gestaltenden Teil (ips-gestaltender-teil).

# Darstellender Teil

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Darstellender Teil` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Die Entscheidungsgrundlage vollständig machen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Krisenentwicklung, Ursachen und bisherige Maßnahmen erzählen.
2. Künftige Maßnahmen, Finanzplanung, Vergleichsrechnung und Sanierungsbeiträge verständlich darstellen.
3. Sonderaktiva, Haftungs- und Anfechtungsthemen, Sicherheiten, Steuerfolgen und Drittrechte offenlegen.
4. Klarheit, Vollständigkeit, Widerspruchsfreiheit und Verständlichkeit als Qualitätsgates prüfen.

## Ausgabe

- Darstellender Teil als Entwurf
- Entscheidungserhebliche Angaben
- Risiko- und Lückenverzeichnis
- Freigabefassung

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Insolvenzplan / StaRUG)

§ 217 InsO (Plan-Option) → § 218 InsO (Plan-Vorlage) → §§ 220-221 InsO (darstellender und gestaltender Teil) → § 222 InsO (Gruppen) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Planbestaetigung) → § 254 InsO (Planwirkung) → §§ 7-39 StaRUG (StaRUG-Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown)

## Triage — Plan-Vorarbeiten

Bevor losgelegt wird, klaere:
1. **Verfahrensart?** InsO-Plan (§§ 217 ff. InsO) oder StaRUG-Restrukturierungsplan (§§ 7-39 StaRUG)?
2. **Klassenbildung schluessig?** § 222 InsO / § 10 StaRUG — gleiche Rechte und Interessen je Gruppe.
3. **Mehrheits-Simulation?** Ist 75%-Schwelle (StaRUG) oder 50%+50% (InsO) realistisch?
4. **Vergleichsrechnung?** Liquidationswert als Referenz fuer Best-Interest-Test berechnen.
5. **Cramdown-Szenario?** Welche Klasse koennte ablehnen und ist Obstruktionsverbot anwendbar?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
