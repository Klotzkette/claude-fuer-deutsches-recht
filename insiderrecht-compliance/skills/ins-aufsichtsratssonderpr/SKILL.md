---
name: ins-aufsichtsratssonderpr
description: "Ins 047 Aufsichtsratssonderpr Fung, Ins 048 Bankaufsichtliches Handeln: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 047 Aufsichtsratssonderpr Fung, Ins 048 Bankaufsichtliches Handeln

## Arbeitsbereich

Dieser Skill bündelt **Ins 047 Aufsichtsratssonderpr Fung, Ins 048 Bankaufsichtliches Handeln** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-047-aufsichtsratssonderpr-fung` | Prueft Insiderrecht-Konsequenzen einer Sonderuntersuchung durch den Aufsichtsrat oder Wirtschaftspruefer: Informationsfluss, Insiderlisten und Ad-hoc-Pflicht. |
| `ins-048-bankaufsichtliches-handeln` | Analysiert Insiderrecht bei bankaufsichtsrechtlichen Massnahmen (KWG, SSM): Vertraulichkeit, Ad-hoc-Pflicht und Koordination mit BaFin/EZB. |

## Arbeitsweg

Für **Ins 047 Aufsichtsratssonderpr Fung, Ins 048 Bankaufsichtliches Handeln** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-047-aufsichtsratssonderpr-fung`

**Fokus:** Prueft Insiderrecht-Konsequenzen einer Sonderuntersuchung durch den Aufsichtsrat oder Wirtschaftspruefer: Informationsfluss, Insiderlisten und Ad-hoc-Pflicht.

# Aufsichtsrats-Sonderprüfung – Insiderrecht

## Rechtlicher Rahmen

Wenn der Aufsichtsrat eine Sonderuntersuchung zu internen Missständen, Bilanzunstimmigkeiten
oder Compliance-Verstößen beauftragt, entstehen insiderrechtlich komplexe Situationen:
Ist der Untersuchungsgegenstand eine Insiderinformation? Besteht Ad-hoc-Pflicht? Wer darf
über die Untersuchung informiert werden?

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- §§ 111, 142 AktG (Sonderprüfung): https://www.gesetze-im-internet.de/aktg/__111.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html

## Ziel dieses Skills

Dieser Skill prüft, ob und wann die Sonderuntersuchung und ihre Ergebnisse zu einer
Insiderinformation werden, und steuert die Ad-hoc-Entscheidung.

## Arbeitsprogramm

### Schritt 1 – Insiderinformations-Prüfung des Untersuchungsgegenstands

- Was ist Gegenstand der Sonderuntersuchung?
 (Bilanzmanipulation, Korruption, Compliance-Verstöße, Kartellverhalten, persönliche Fehlverhaltensvorwürfe)
- Ist der Untersuchungsgegenstand bereits als Insiderinformation zu qualifizieren?
- Kursrelevanz: Würde ein verständiger Anleger die Existenz der Untersuchung oder ihr
 voraussichtliches Ergebnis berücksichtigen?

### Schritt 2 – Zeitpunkt der Insiderinformation

- Mögliche Zeitpunkte: AR-Beschluss zur Untersuchung; erster Hinweis, der die Untersuchung
 auslöste; Zwischenergebnisse; finales Ergebnis
- Geltl/Daimler-Test: Auch Zwischenschritte können eigenständige Insiderinformationen sein
- Dokumentiere frühestmöglichen Zeitpunkt

### Schritt 3 – Informationskreis und Insiderlisten

- Wer ist in die Untersuchung eingebunden?
 (Beauftrage Kanzlei, WP, AR-Ausschuss, ggf. Vorstand – sofern nicht selbst Untersuchungsgegenstand)
- Alle Wissensträger in die Insiderliste aufnehmen
- Informationsfluss zwischen AR und Vorstand: Nur „need to know"

### Schritt 4 – Aufschub-Möglichkeit

- Laufende Untersuchung: Legitimes Interesse am Aufschub möglich, wenn Offenlegung die
 Untersuchung beeinträchtigen würde
- Grenzen: Wenn Markt bereits von dem Untersuchungsgegenstand informiert ist (z. B. durch
 Medien) → kein Aufschub mehr
- Trigger für Aufhebung: Abschluss der Untersuchung oder Leak der Ergebnisse

### Schritt 5 – Ad-hoc bei Untersuchungsergebnis

- Wesentliche Befunde (z. B. Bilanzfehler, Verluste, Strafanzeige) sind ad-hoc-pflichtig
- Koordination: Untersuchungsbericht fertig → CFO und Compliance prüfen → Ad-hoc unverzüglich
- Inhalt: Was wurde festgestellt, welche Maßnahmen werden ergriffen, Ausblick

## Red-Team-Fragen

- Wurde der frühestmögliche Insiderinformationszeitpunkt identifiziert?
- Ist der Aufschub während der laufenden Untersuchung rechtlich begründet?
- Wurden alle Wissensträger in die Insiderliste aufgenommen (inkl. externe Kanzlei und WP)?
- Wurden PDMR-Eigengeschäfte im Zeitraum der Untersuchung geprüft?
- Ist das finale Untersuchungsergebnis Gegenstand einer Ad-hoc-Pflicht?

## Ausgabeformat

Erzeuge:
1. Insiderinformations-Zeitstrahl (Hinweis → AR-Beschluss → Zwischenergebnis → finales Ergebnis)
2. Insiderlisten-Aktualisierungsplan
3. Aufschub-Begründungsmatrix
4. Ad-hoc-Entwurf für wesentliche Untersuchungsergebnisse

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, bgh.de,
dejure.org.

## 2. `ins-048-bankaufsichtliches-handeln`

**Fokus:** Analysiert Insiderrecht bei bankaufsichtsrechtlichen Massnahmen (KWG, SSM): Vertraulichkeit, Ad-hoc-Pflicht und Koordination mit BaFin/EZB.

# Bankaufsichtliches Handeln – Insiderrecht und MAR

## Rechtlicher Rahmen

Bankaufsichtsrechtliche Maßnahmen der BaFin oder EZB (Kapitalanforderungen, Stresstests,
Zwangsmaßnahmen nach KWG, Anordnungen nach CRR) können für börsennotierte Kreditinstitute
Insiderinformationen nach Art. 7 MAR darstellen. Das Kreditinstitut hat gegenüber der
Aufsichtsbehörde Vertraulichkeitspflichten, aber gegenüber dem Kapitalmarkt Ad-hoc-Pflichten.
Diese Spannung muss aufgelöst werden.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- §§ 44, 45 KWG: https://www.gesetze-im-internet.de/kwg/__44.html
- SSM-Verordnung (EU) 1024/2013: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R1024
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill löst den Konflikt zwischen aufsichtsrechtlicher Vertraulichkeit und kapital-
marktrechtlicher Ad-hoc-Pflicht für börsennotierte Kreditinstitute.

## Arbeitsprogramm

### Schritt 1 – Insiderinformations-Prüfung bei Aufsichtsmaßnahmen

- Ist die aufsichtsrechtliche Maßnahme kursrelevant?
 Hohe Kursrelevanz: Erhöhte Kapitalanforderungen, formelle Ermittlung, Bußgeldbescheid,
 Lizenzaufhebung, Kapitalerhöhungspflicht
 Niedrige Kursrelevanz: Routine-Prüfungen, allgemeine Branchenanforderungen

### Schritt 2 – Vertraulichkeits-Konflikt

- Aufsichtsbehörde erteilt oft explizite Vertraulichkeitsauflagen
- MAR Art. 17 Abs. 4: Aufschub möglich, wenn legitimes Interesse besteht
- Frage: Ist behördliche Vertraulichkeitsauflage ein „legitimes Interesse" im Sinne MAR?
 → Antwort: Ja, wenn Offenlegung die Umsetzung der Maßnahme gefährdet oder Behörde
 explizit Vertraulichkeit fordert (BaFin-Praxis)

### Schritt 3 – Koordination mit BaFin

- Direkte Abstimmung mit BaFin (Kapitalmarktrecht-Abteilung) über Ad-hoc-Pflicht
- BaFin kann im Einzelfall Auskunft erteilen, ob und wann eine Veröffentlichung erwartet wird
- Protokoll aller Gespräche mit BaFin zu dieser Frage

### Schritt 4 – Ad-hoc-Pflicht nach Abschluss des Verfahrens

- Wenn Aufsichtsmaßnahme rechtskräftig: Sofortige Ad-hoc-Pflicht (Aufschub endet)
- Wenn Maßnahme zurückgenommen: Keine Ad-hoc-Pflicht für nicht-verwirklichte Maßnahme
 (aber: laufendes Verfahren kann weiterhin kursrelevant sein)

### Schritt 5 – Sonderfall: EZB-SSM-Verfahren

- SSM-Verfahren gegen bedeutende Institute (§ 89 KWG i.V.m. SSM-VO)
- EZB übt Vertraulichkeit besonders streng aus
- Koordination mit EZB-Vertretern und BaFin als nationaler zuständiger Behörde

## Red-Team-Fragen

- Ist die Aufsichtsmaßnahme kursrelevant?
- Wurde der Aufschub koordiniert und dokumentiert?
- Ist die BaFin als Kapitalmarktaufseher (nicht als Bankenaufseher) informiert?
- Wurde die Aufschub-Dauer minimiert und der Trigger für Beendigung definiert?

## Ausgabeformat

Erzeuge:
1. Kursrelevanz-Analyse bankaufsichtsrechtlicher Maßnahmen
2. Aufschub-Dokumentation (inklusive behördlicher Vertraulichkeitsauflage)
3. BaFin-Koordinationsprotokoll
4. Ad-hoc-Entwurf für rechtskräftige Maßnahme

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Für systemrelevante Institute (G-SIIs, O-SIIs) und Kreditinstitute unter SSM-Direktaufsicht
der EZB gilt zusätzlich, dass aufsichtsrechtliche Informationen im Kollegium der Aufsichtsbehörden
(Art. 113 ff. CRD IV) besonderer Vertraulichkeit unterliegen. Die Ad-hoc-Compliance muss
sicherstellen, dass nur solche Informationen veröffentlicht werden, bei denen die
Aufsichtsbehörde keine Vertraulichkeit ausdrücklich eingefordert hat. Im Zweifelsfall:
Schriftliche Klärung mit EZB/BaFin vor der Veröffentlichung einholen.

Weitere Quellen:
- SSM-Verordnung (EU) 1024/2013: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R1024
- §§ 44 KWG: https://www.gesetze-im-internet.de/kwg/__44.html
