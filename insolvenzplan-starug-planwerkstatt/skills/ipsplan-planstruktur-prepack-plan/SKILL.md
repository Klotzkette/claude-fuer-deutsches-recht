---
name: ipsplan-planstruktur-prepack-plan
description: "Ipsplan Planstruktur Prepack Plan: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ipsplan Planstruktur Prepack Plan

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ipsplan Planstruktur Prepack Plan** im Plugin Insolvenzplan / StaRUG. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ipsplan-planstruktur-bauleiter` | Bauleiter Planstruktur Insolvenzplan und StaRUG-Restrukturierungsplan: darstellender und gestaltender Teil, Anlagen. Pruefraster fuer Planerstellung. |
| `ipsplan-prepack-plan-spezial` | Spezialfall Prepack-Plan und Eigenverwaltung: Plan vor Antrag, Sachwalter, Glaeubiger einbinden. Pruefraster fuer Krisenberater. |
| `sanierungsmoderation-94-starug` | Sanierungsmoderation nach § 94 StaRUG vorbereiten und durchführen wenn außergerichtliche Einigung mit moderierender Instanz angestrebt wird. §§ 94 ff. StaRUG Sanierungsmoderation. Prüfraster: Antrag Bestellungsvoraussetzungen Moderationsplan Vertraulichkeit Gläubiger-Einbeziehung Abschlussbericht. Output: Moderationsplan Kommunikationsleitfaden Abschlussbericht. Abgrenzung: nicht für StaRUG-Restrukturierungsplan (ips-starug-plan-architektur). |

## Arbeitsweg

Im Plugin Insolvenzplan / StaRUG gilt für **Ipsplan Planstruktur Prepack Plan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ipsplan-planstruktur-bauleiter`

**Fokus:** Bauleiter Planstruktur Insolvenzplan und StaRUG-Restrukturierungsplan: darstellender und gestaltender Teil, Anlagen. Pruefraster fuer Planerstellung.

# IPSPlan: Planstruktur

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IPSPlan: Planstruktur` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: IPSPlan: Planstruktur
- **Spezialgegenstand:** IPSPlan: Planstruktur / ipsplan planstruktur bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `ipsplan-prepack-plan-spezial`

**Fokus:** Spezialfall Prepack-Plan und Eigenverwaltung: Plan vor Antrag, Sachwalter, Glaeubiger einbinden. Pruefraster fuer Krisenberater.

# IPSPlan: Prepack-Plan

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IPSPlan: Prepack-Plan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: IPSPlan: Prepack-Plan
- **Spezialgegenstand:** IPSPlan: Prepack-Plan / ipsplan prepack plan spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH, BVerfG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `sanierungsmoderation-94-starug`

**Fokus:** Sanierungsmoderation nach § 94 StaRUG vorbereiten und durchführen wenn außergerichtliche Einigung mit moderierender Instanz angestrebt wird. §§ 94 ff. StaRUG Sanierungsmoderation. Prüfraster: Antrag Bestellungsvoraussetzungen Moderationsplan Vertraulichkeit Gläubiger-Einbeziehung Abschlussbericht. Output: Moderationsplan Kommunikationsleitfaden Abschlussbericht. Abgrenzung: nicht für StaRUG-Restrukturierungsplan (ips-starug-plan-architektur).

# Sanierungsmoderation § 94 StaRUG

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsmoderation § 94 StaRUG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Die Sanierungsmoderation ist ein vorinsolvenzliches präventives Werkzeug nach §§ 94 ff. StaRUG (seit 1.1.2021). Sie ermöglicht vertraulichen Vergleich vor Eskalation in Restrukturierungs-Verfahren oder Insolvenz.

## Eingaben

- Wirtschaftliche Lage Schuldner (Liquidität Überschuldung drohende Zahlungs-Unfähigkeit)
- Gläubiger-Liste mit Forderungs-Höhen
- Bisherige Sanierungs-Versuche
- Sanierungs-Konzept-Skizze
- Streit-Punkte mit Hauptgläubigern

## Schritt 1 — Anwendungsbereich § 94 StaRUG

### Voraussetzungen

- **Schuldner** Unternehmer (natürliche oder juristische Person)
- **Wirtschaftliche Lage** gefährdet (drohende Zahlungs-Unfähigkeit § 18 InsO oder bereits drohende Restrukturierungs-Bedürftigkeit)
- **Aussicht auf Erfolg** Sanierungs-Gespräche

### Abgrenzung

- **StaRUG-Restrukturierungs-Verfahren** §§ 31 ff. — bei Schwierigkeit der Vergleichs-Findung
- **Insolvenz** bei Eingetretener Zahlungs-Unfähigkeit § 17 InsO oder Überschuldung § 19 InsO
- **Sanierungsmoderation** vorgelagert / vorbeugend

## Schritt 2 — Antrag § 95 StaRUG

### Antrag-Inhalt

- Bezeichnung Schuldner
- Sachstand wirtschaftliche Lage
- Schilderung Sanierungs-Bedarf
- Liste Gläubiger Forderungs-Höhen
- Geforderter Verhandlungs-Inhalt

### Antragsteller

- Schuldner selbst

### Zuständigkeit

- Restrukturierungs-Gericht (LG-Insolvenz-Abteilung)
- Bestimmt durch Schuldner-Sitz

### Form

- Schriftlich elektronisch
- Mit Unterlagen

## Schritt 3 — Bestellung Moderator § 95 StaRUG

### Auswahl

- Gericht bestellt Sanierungsmoderator
- Vorschlags-Recht Schuldner (im Antrag)
- Vorraussetzung Eignung (Erfahrung Wirtschafts-Sanierung)

### Anforderungen Moderator

- Wirtschafts-Beratungs-Erfahrung
- Häufig: Wirtschafts-Prüfer, Rechtsanwalt mit Sanierungs-Schwerpunkt
- Unabhängigkeit

### Vergütung

- Nach billigem Ermessen Gericht
- Schuldner trägt Kosten

## Schritt 4 — Aufgaben Moderator § 96 StaRUG

### Vermittler-Rolle

- **Sachverhalts-Aufklärung** Wirtschaftslage Schuldner
- **Sanierungs-Konzept** ausarbeiten mit Schuldner
- **Verhandlungen** mit Gläubigern moderieren
- **Vergleichs-Versuch** zwischen Schuldner und Gläubigern
- **Berichte** an Gericht (Halbzeit Abschluss)

### Vertraulichkeit § 97 StaRUG

- **Pflicht zur Verschwiegenheit** Moderator und Beteiligte
- Bei Schaden durch Verletzung: Schadensersatz-Pflicht
- Ausnahme: Mitteilung an Gericht und Beteiligte des Verfahrens

### Befugnisse

- **Keine Verfügungs-Befugnis** über Vermögen Schuldner
- **Keine Zwangs-Befugnisse** gegenüber Gläubigern
- Reine Moderations- und Berater-Rolle

## Schritt 5 — Verfahrens-Dauer § 94 Abs. 2 StaRUG

- **Drei Monate** Standard-Dauer
- **Verlängerung** auf bis zu sechs Monate durch Gericht-Beschluss möglich
- **Aufhebung** bei offensichtlicher Aussichts-Losigkeit oder Antrags-Rücknahme

## Schritt 6 — Sanierungsvergleich § 97 StaRUG und Bestätigung § 100 StaRUG

### Bei Erfolg

- **Sanierungs-Vergleich** zwischen Schuldner und Gläubigern, § 97 StaRUG (Inhalt, Form, Wirkung)
- **Bestätigung durch Restrukturierungs-Gericht** auf Antrag, § 100 StaRUG
- Wirkung: Anfechtungs-Privileg nach § 90 StaRUG bei späterer Insolvenz

### Anfechtungs-Privileg § 90 StaRUG

- Bestätigter Sanierungs-Vergleich (§ 100 StaRUG) bzw. Restrukturierungs-Plan ist im Umfang des § 90 StaRUG anfechtungs-privilegiert
- Schutz-Wirkung gegen Vorsatz-Anfechtung § 133 InsO
- Bargeschäfts-Privileg § 142 InsO bleibt ergänzend anwendbar

### Vergleichs-Inhalte typisch

- Stundung Schulden
- Teil-Erlass
- Tilgungs-Plan
- Sicherheits-Bestellung
- Anteils-Übertragungen (Debt-Equity-Swap)
- Sanierungs-Maßnahmen Schuldner-seite

## Schritt 7 — Vorteile gegenüber anderen Verfahren

### Gegenüber Insolvenz

- **Vertraulichkeit** Bewahrung Reputation
- **Geringere Kosten**
- **Schnellere Lösung**
- **Erhalt Geschäftsbetrieb**
- **Erhalt Geschäftsführer-Verfügung**

### Gegenüber Restrukturierungs-Verfahren StaRUG §§ 31 ff.

- **Niedrigere Schwelle**
- **Keine Mehrheits-Beschluss-Bindung** Gläubiger
- **Reine Konsens-Findung**
- **Kein öffentliches Verfahren**

### Gegenüber außergerichtlichem Vergleich

- **Bestätigungs-Möglichkeit** mit Anfechtungs-Schutz
- **Strukturiertes Verfahren**
- **Vertraulichkeits-Schutz**
- **Gerichtlich begleitet**

## Schritt 8 — Konkretes Vorgehen

### Vor-Phase

1. **Wirtschaftlich Lage analysieren** (Skill `liquiditaetsvorschau-3wochen` etc.)
2. **Sanierungs-Konzept-Skizze** (IDW S 6 Mindeststandard)
3. **Gläubiger-Sondierung** vorab
4. **Anwalts-Beratung** Sanierungs-Spezialist

### Antrags-Phase

1. **Antrag beim Restrukturierungs-Gericht** mit Moderator-Vorschlag
2. **Bestellung Moderator** durch Gericht
3. **Erstes Beratungs-Gespräch** mit Moderator

### Verhandlungs-Phase

1. **Gläubiger-Verhandlungen** moderiert durch Moderator
2. **Sanierungs-Konzept** finalisieren
3. **Einzel-Vergleiche** mit Gläubigern
4. **Gesamt-Vergleich** entwerfen

### Abschluss-Phase

1. **Bestätigungs-Antrag** beim Gericht § 100 StaRUG
2. **Anhörung** Gläubiger
3. **Bestätigungs-Beschluss** § 100 Abs. 2 StaRUG
4. **Umsetzung** Sanierungs-Maßnahmen

## Schritt 9 — Bei Misserfolg

### Optionen

- **Übergang StaRUG-Restrukturierungs-Verfahren** §§ 31 ff. — strukturiertes Mehrheits-Verfahren
- **Insolvenz-Antrag** bei eingetretener Zahlungs-Unfähigkeit / Überschuldung
- **Außergerichtlicher Vergleich** ohne Gericht (Risiko Anfechtung)

### Wechsel-Strategie

- Skill `mandat-triage-insolvenzrecht` aktivieren
- Antragspflicht § 15a InsO prüfen
- Eil-Modus

## Schritt 10 — Schuldner-Strategie

### Vor Antrag

- **Frühzeitig** vor wirtschaftlicher Eskalation
- **Sanierungs-Konzept** mit Realitätssinn (IDW S 6)
- **Gläubiger sondieren** zu Vergleichs-Bereitschaft
- **Geschäftsführer-Pflichten** beachten § 15a InsO (Sanierungsmoderation entlastet nicht von Antragspflicht bei eingetretener Zahlungs-Unfähigkeit)

### Während Verfahren

- **Kooperation** mit Moderator
- **Vollständige Information** Wirtschaftslage
- **Transparenz** gegenüber Gläubigern
- **Operativ stabilisieren** (Liquiditäts-Sicherung)

### Vergleichs-Verhandlungen

- **Kompromiss-Bereitschaft**
- **Win-Win-Argumentation** (Insolvenz-Vergleich Quote-Vergleich)
- **Sicherheits-Angebote** wenn möglich
- **Sanierungs-Pflichten** des Schuldners eingehen

## Schritt 11 — Gläubiger-Strategie

### Bei Information über Sanierungsmoderation

- **Sachstand erfragen** Moderator
- **Forderungs-Anmeldung** prüfen
- **Verhandlungs-Bereitschaft** signalisieren oder verweigern

### Verhandlung

- **Eigene Position** stark vortragen
- **Sicherheiten** verlangen
- **Tilgungs-Plan** strukturieren
- **Alternative Insolvenz-Quote** als Benchmark

### Bei Zustimmungs-Entscheidung

- **Vergleich-Bedingungen** detail
- **Schriftform** § 126 BGB
- **Anfechtungs-Schutz** durch Gerichts-Bestätigung anstreben

## Schritt 12 — Anwalts-Mandat

### Schuldner-Seite

- **Sanierungs-Anwalt** mit StaRUG-Erfahrung
- **Wirtschafts-Prüfer** parallel für IDW S 6
- **Steuerberater** für steuerliche Effekte (Sanierungsgewinn-Steuer)

### Gläubiger-Seite

- **Insolvenz-Spezialist**
- **Bewertung Vergleichs-Vorschlag** vs. Insolvenz-Quote
- **Schaden-Maximierung**

## Verzahnung mit anderen Skills

- `liquiditaetsvorschau-3wochen` — Liquidität-Analyse
- `liquiditaetsvorschau-3-6-12-monate` — mittel-langfristige Planung
- `fortbestehensprognose-zusammenfuehren` — IDW S 6
- `mandat-triage-insolvenzrecht` — bei Misserfolg
- `antragspflicht-15a-inso` — Geschäftsführer-Pflichten
- `glaeubigerausschuss-mitwirkung` — bei späterem Verfahren
- `anfechtungsrechte-pruefen` — Schutz durch § 90 StaRUG

## Ausgabe

- `sanierungsmoderation-{schuldner}.md` mit Wirtschaftslage Vorbereitung Antrag
- Antrags-Schriftsatz § 95 StaRUG
- Sanierungs-Konzept-Skelett
- Gläubiger-Liste
- Verhandlungs-Strategie
- Vergleichs-Entwürfe
- Bei Misserfolg: Eskalations-Plan

## Quellen

- StaRUG §§ 94 95 96 97 100 90
- InsO §§ 17 18 19 142
- **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit bei Bargeschäft im Sanierungskontext; konkretes gezielt schädigendes Verhalten erforderlich. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA) — verfassungsrechtliche Tragfähigkeit von Sanierungsverfahren. <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- IDW S 6 (Sanierungs-Fähigkeit)
- Literatur (Frind, Skauradszun) nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle


## Weitere Leitentscheidungen StaRUG-Moderation

- Konkrete Restrukturierungsgerichts-Entscheidungen zur Sanierungsmoderation (§§ 94–100 StaRUG), insbesondere zur Bestellung des Moderators und zur Bestätigung des Sanierungsvergleichs (§ 97 StaRUG), vor Ausgabe über dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
