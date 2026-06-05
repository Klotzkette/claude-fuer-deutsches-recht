---
name: normenkontrolle-satzungsnormenkontrolle
description: "Satzungsnormenkontrolle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Satzungsnormenkontrolle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Satzungsnormenkontrolle** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `normenkontrolle-satzungsnormenkontrolle-47-vwgo` | Allgemeine Satzungsnormenkontrolle nach § 47 VwGO: kommunale Satzungen, Landesrechtsverordnungen, Landesrechtseröffnung und Abgrenzung zur Inzidentkontrolle.; Normanker: VwGO § 47 Abs. 1 Nr. 2; jeweiliges Landesausführungsgesetz; Kommunalrecht; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar. |
| `anpassungsgebot-flaechennutzungsplan` | Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet Konflikt FNP-Darstellung vs. B-Plan-Festsetzung Ausnahmen § 8 Abs. 3 und 4 BauGB Parallelverfahren § 13a Abs. 2 BauGB. Output: Entwicklungsgebot-Prüfprotokoll und Angriffspunkt für Normenkontrollantrag. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Abwaegungsfehler) und planerhaltung-214-215-baugb. |
| `antragsbefugnis-eigentuemer-nachbar` | Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Massstab Eigentuemer im Plangebiet immer antragsbefugt Nachbar bei abwaegungserheblichem Belang BVerwG vom 31.1.2017 Verbandsklagebefugnis § 64 BNatSchG § 2 UmwRG. Output: Antragsbefugnis-Analyse und Empfehlung Mandatsannahme. Abgrenzung zu statthaftigkeit-47-vwgo (Statthatfigkeit) und jahresfrist-47-abs-2-vwgo (Frist). |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Satzungsnormenkontrolle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `normenkontrolle-satzungsnormenkontrolle-47-vwgo`

**Fokus:** Allgemeine Satzungsnormenkontrolle nach § 47 VwGO: kommunale Satzungen, Landesrechtsverordnungen, Landesrechtseröffnung und Abgrenzung zur Inzidentkontrolle.; Normanker: VwGO § 47 Abs. 1 Nr. 2; jeweiliges Landesausführungsgesetz; Kommunalrecht; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar.

# Allgemeine Satzungsnormenkontrolle nach § 47 VwGO: kommunale Satzungen, Landesrechtsverordnungen, Landesrechtseröffnung und Abgrenzung zur Inzidentkontrolle.

## Auftrag

Dieser Skill löst § 47 VwGO aus der reinen Bauleitplanung. Er prüft, ob eine im Rang unter dem Landesgesetz stehende Rechtsvorschrift direkt vor dem OVG/VGH überprüft werden kann oder ob nur eine Inzidentkontrolle im Verfahren gegen einen Einzelakt passt.

## Normanker

VwGO § 47 Abs. 1 Nr. 2; jeweiliges Landesausführungsgesetz; Kommunalrecht. Vor jeder Ausgabe muss das jeweilige Landesrecht geprüft werden, weil § 47 Abs. 1 Nr. 2 VwGO die Normenkontrolle außerhalb der BauGB-Fälle nur eröffnet, soweit Landesrecht dies bestimmt.

## Prüfprogramm

1. Normtyp: Satzung, Rechtsverordnung, Bebauungsplan, Polizeiverordnung, Benutzungssatzung oder bloßer Verwaltungsakt?
2. Statthaftigkeit: § 47 Abs. 1 Nr. 1 oder Nr. 2 VwGO, Landesrechtseröffnung, Rang unter Landesgesetz.
3. Antragsteller: mögliche Rechtsverletzung, Adressat, Eigentümer, Nutzer, Gemeinde, Verband oder Konkurrent.
4. Frist und Rechtsschutzbedürfnis: Jahresfrist, fortbestehende Beschwer, Parallelverfahren.
5. Materielle Kontrolle: Ermächtigung, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.
6. Rechtsfolge: Unwirksamkeit, Bekanntmachung der Entscheidung, Wirkung auf Folgebescheide, neue Satzung.

## Ausgabe

Erzeuge eine Statthaftigkeitsskizze, Satzungs-Red-Team, Eilantragsskizze, Schriftsatzgliederung oder Bürger-/Mandantenbrief.

## 2. `anpassungsgebot-flaechennutzungsplan`

**Fokus:** Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet Konflikt FNP-Darstellung vs. B-Plan-Festsetzung Ausnahmen § 8 Abs. 3 und 4 BauGB Parallelverfahren § 13a Abs. 2 BauGB. Output: Entwicklungsgebot-Prüfprotokoll und Angriffspunkt für Normenkontrollantrag. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Abwaegungsfehler) und planerhaltung-214-215-baugb.

# Anpassungsgebot — Flächennutzungsplan

## Zweck

Das Entwicklungsgebot bindet den B-Plan an den FNP. Verletzung ist beachtlicher Verfahrensfehler und häufig übersehener Angriffspunkt.

## Schritt 1 — Wortlaut § 8 BauGB

### § 8 Abs. 1 BauGB
- Bebauungspläne enthalten die rechtsverbindlichen Festsetzungen für die städtebauliche Ordnung

### § 8 Abs. 2 S. 1 BauGB (Entwicklungsgebot)
- Bebauungspläne sind aus dem Flächennutzungsplan zu entwickeln

### § 8 Abs. 3 S. 1 BauGB (Parallelverfahren)
- Vor dem Flächennutzungsplan kann ein Bebauungsplan aufgestellt werden, wenn dringende Gründe es erfordern und der Bebauungsplan der beabsichtigten städtebaulichen Entwicklung nicht entgegensteht

### § 8 Abs. 4 BauGB (selbständiger B-Plan)
- Ein Bebauungsplan kann aufgestellt werden, ohne dass ein Flächennutzungsplan vorliegt, wenn er der städtebaulichen Entwicklung nicht widerspricht

## Schritt 2 — Entwicklungsgebot — Begriff "Entwickeln"

### Maßstab
- B-Plan-Festsetzungen müssen aus FNP-Darstellungen "entwickelt" sein
- Entwicklung verlangt sachlichen Bezug, keine 1:1-Identität
- Konkretisierung der FNP-Aussage durch B-Plan

### Beispiel
- FNP: "Wohnbaufläche W"
- B-Plan: WA (allgemeines Wohngebiet) — entspricht Entwicklungsgebot
- B-Plan: GE (Gewerbegebiet) — widerspricht Entwicklungsgebot

### Toleranz
- Geringfügige Abweichungen toleriert
- Größere Abweichungen erfordern FNP-Änderung im Parallelverfahren oder vorab

## Schritt 3 — Parallelverfahren § 8 Abs. 3 BauGB

### Voraussetzungen
- Dringende Gründe für vorgezogenen B-Plan
- B-Plan steht der beabsichtigten städtebaulichen Entwicklung nicht entgegen
- Tatsächlich praktisch häufig parallel betrieben

### Pflichten
- FNP-Änderungsverfahren muss eingeleitet sein
- Beide Pläne werden gemeinsam zur Beschlussfassung gebracht
- Reihenfolge: erst FNP-Wirksamkeit, dann B-Plan-Wirksamkeit (oder zeitgleich)

### Häufige Treffer
- B-Plan wird vor FNP-Änderung wirksam
- Vorgezogener B-Plan ohne dringende Gründe
- Stadt argumentiert mit "Investor-Druck" — kein dringender Grund

## Schritt 4 — Berichtigungsmöglichkeit § 13a Abs. 2 BauGB

### Voraussetzung
- B-Plan der Innenentwicklung nach § 13a BauGB
- Geringfügige Abweichung vom FNP

### Verfahren
- FNP wird im Wege der "Berichtigung" angepasst
- Kein förmliches FNP-Änderungsverfahren erforderlich
- Bekanntmachung Berichtigung im Amtsblatt

### Strategischer Angriffspunkt
- Wenn die Abweichung in Wahrheit nicht "geringfügig" ist
- Wenn der B-Plan in Wahrheit nicht Innenentwicklung nach § 13a darstellt
- Wenn die Berichtigung nicht bekanntgemacht ist

## Schritt 5 — Selbständiger B-Plan § 8 Abs. 4 BauGB

### Anwendungsbereich
- In Gemeinden ohne wirksamen FNP
- Bei isolierten Festsetzungen ohne FNP-Bezug

### Voraussetzung
- B-Plan widerspricht nicht der städtebaulichen Entwicklung
- Strenge Anforderung — restriktiv anwendbar

### Praxis
- Selten relevant in größeren Städten mit umfassendem FNP
- Bei Flecken-Plänen, Sonderzonen denkbar

## Schritt 6 — FNP-Bezug konkret prüfen

### Audit-Schritte
1. FNP-Auszug für das Plangebiet beschaffen
2. FNP-Darstellung identifizieren (Wohnbauflache, gemischte Baufläche, Gewerbefläche, Grünfläche, Verkehrsfläche)
3. B-Plan-Festsetzung mit FNP-Darstellung vergleichen
4. Bei Abweichung: Parallelverfahren oder Berichtigung dokumentiert?

### Häufige Konstellationen
- FNP: "gemischte Baufläche" — B-Plan: WA — Entwicklung zulässig
- FNP: "Wohnbauflache" — B-Plan: MK (Kerngebiet) — problematisch
- FNP: "Grünfläche" — B-Plan: WA — widerspricht Entwicklungsgebot
- FNP: "Bahnanlage" — B-Plan: MU (urbanes Gebiet) — FNP-Änderung zwingend

## Schritt 7 — Konflikt Bahn-Anlage / Bahnflächen

### Sonderfall Bahnhofsbrachen
- Bahnflächen sind häufig im FNP als "Bahnanlage" oder "Fläche für Bahnbetrieb" dargestellt
- Bei Umwandlung in städtisches Quartier — FNP-Änderung erforderlich
- Eisenbahnrecht (Allgemeines Eisenbahngesetz, AEG) für Entwidmung relevant

### Entwidmung § 23 AEG
- Vor B-Plan-Beschluss muss Bahnfläche entwidmet sein
- Sonst Konflikt mit Eisenbahnrecht
- Eisenbahn-Bundesamt zuständig

### Strategischer Hebel
- Wenn Entwidmung nicht vorliegt — B-Plan wirft zwei Probleme auf:
 - FNP-Konflikt
 - Eisenbahnrechts-Konflikt
- Beides als Verstoß gegen Erforderlichkeit oder beachtlicher Fehler

## Schritt 8 — Rechtsfolge bei Verstoß gegen § 8 Abs. 2 BauGB

### Wirksamkeit
- Verstoß gegen Entwicklungsgebot ist beachtlich (§ 214 Abs. 2 BauGB)
- Bei Beachtlichkeit kann Plan unwirksam sein
- § 215 BauGB-Rügefrist gilt

### Heilung
- Durch nachträgliche FNP-Änderung und ergänzendes Verfahren
- Häufiger Heilungsweg der Stadt

## Schritt 9 — Audit-Checkliste

| Punkt | Prüfung |
|---|---|
| FNP-Darstellung Plangebiet identifiziert? | |
| B-Plan-Festsetzung identifiziert? | |
| Übereinstimmung Entwicklungsgebot? | Ja/nein |
| Bei Abweichung: Parallelverfahren? | Ja/nein |
| Bei Abweichung: Berichtigung § 13a Abs. 2 BauGB? | Ja/nein |
| Bei Bahnflächen: Entwidmung § 23 AEG? | Ja/nein |
| FNP-Änderung bekannt gemacht? | Ja/nein |

## Quellen

- BauGB §§ 5 8 13a 214
- AEG § 23
- BVerwG, Urteil vom 28.2.1975 – 4 C 30.72 (Entwicklungsgebot)
- BVerwG, Urteil vom 26.2.1999 – 4 CN 6.98 (Parallelverfahren)
- BVerwG, Urteil vom 27.10.1999 – 11 A 31.98 (Entwidmung Bahnfläche)
- BayVGH, Urteil vom 5.10.2017 – 15 N 16.1652 (Berichtigung)

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `antragsbefugnis-eigentuemer-nachbar`

**Fokus:** Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Massstab Eigentuemer im Plangebiet immer antragsbefugt Nachbar bei abwaegungserheblichem Belang BVerwG vom 31.1.2017 Verbandsklagebefugnis § 64 BNatSchG § 2 UmwRG. Output: Antragsbefugnis-Analyse und Empfehlung Mandatsannahme. Abgrenzung zu statthaftigkeit-47-vwgo (Statthatfigkeit) und jahresfrist-47-abs-2-vwgo (Frist).

# Antragsbefugnis § 47 Abs. 2 VwGO

## Zweck

Zweite Säule der Zulässigkeit. Die Antragsbefugnis filtert nicht selbst betroffene Bürger heraus. Wer sie versäumt, scheitert ohne Sachprüfung.

## Schritt 1 — Maßstab Möglichkeitstheorie

### Wortlaut § 47 Abs. 2 S. 1 VwGO
- Antragsbefugt ist jede natürliche oder juristische Person, die geltend macht, durch die Rechtsvorschrift oder deren Anwendung in ihren Rechten verletzt zu sein oder in absehbarer Zeit verletzt zu werden

### Möglichkeitstheorie
- Es genügt, dass eine Rechtsverletzung möglich erscheint
- Kein Vollbeweis im Zulässigkeitsstadium
- Schlüssige Darlegung tatsächlicher Anhaltspunkte
- Verstärkter Maßstab seit 1996/2006-Verkürzung — aber keine Beweisanforderung

### Schwelle
- Geltendmachung muss substanziiert erfolgen
- Bloße Behauptung "ich bin betroffen" reicht nicht
- Konkrete Bezugnahme auf bestimmten Belang notwendig

## Schritt 2 — Eigentümer im Plangebiet

### Grundregel
- Eigentümer eines Grundstücks im Plangebiet ist stets antragsbefugt
- Begründung Art. 14 GG: B-Plan-Festsetzungen wirken unmittelbar auf das Eigentum
- BVerwG seit Jahrzehnten unverändert

### Anwendung
- Egal ob Festsetzungen den Mandanten begünstigen oder belasten
- Auch bei nur teilweise im Plangebiet liegenden Grundstücken
- Erbbauberechtigte gleichgestellt
- Wohnungseigentümer für Sondereigentum und Miteigentum am gemeinschaftlichen Eigentum

## Schritt 3 — Eigentümer außerhalb des Plangebiets

### Schwelle abwägungserheblicher Belang
- Außerhalb des Plangebiets nicht automatisch betroffen
- Erforderlich: abwägungserheblicher privater Belang
- BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16
- BVerwG, Beschluss vom 8.6.2011 – 4 BN 42.10
- Abwägungserheblich = mehr als nur geringfügig betroffen

### Typische abwägungserhebliche Belange
- Lärmzunahme durch Verkehr aus dem Plangebiet
- Verschattung durch Hochbauten
- Gefahr durch Schadstoffemissionen
- Sichtbeziehung bei besonderer landschaftlicher Bedeutung
- Wertminderung wenn auf abwägungserheblichen Belang zurückführbar

### Nicht abwägungserhebliche Belange
- Allgemeine Aussichtseinbußen ohne besondere Schutzwürdigkeit
- Reine wirtschaftliche Konkurrenz
- Bloße Wertminderung ohne Substanz-Beeinträchtigung (BVerwG, Beschluss vom 9.2.1995 – 4 NB 17.94)
- Diffuse "Verschlechterung der Wohnqualität"

## Schritt 4 — Andere Berechtigte

### Mieter und Pächter
- Grundsätzlich nicht antragsbefugt, da kein dingliches Recht
- Ausnahme bei besonderer Schutzgehalt (z.B. Gewerbemieter mit existenziell betroffenem Standort) — restriktiv
- Im Zweifel mit Eigentümer-Mandat verknüpfen

### Erbbauberechtigte
- Wie Eigentümer

### Wohnungseigentümer
- Antragsbefugt für eigene Wohnung
- Bei Gemeinschaftsangelegenheiten Beschluss der WEG erforderlich

## Schritt 5 — Verbandsklage Naturschutz

### Anerkannte Vereinigungen § 3 UmwRG
- Vom Bund oder Land anerkannte Vereinigungen
- BUND, NABU, LBV, Bürgerinitiativen mit Anerkennung

### Klagebefugnis § 2 UmwRG
- Bei Plänen mit UVP-Pflicht oder Sondernormen
- Bei FFH-relevanten Plänen
- Bei B-Plänen mit Umweltbericht — über § 2 Abs. 1 UmwRG i.V.m. § 1 Abs. 1 S. 1 Nr. 4 UmwRG
- Eigenständige Antragsbefugnis ohne dingliches Recht

### Naturschutz § 64 BNatSchG
- Bei Entscheidungen mit Naturschutzbezug
- Häufig kumulativ mit § 2 UmwRG geltend gemacht

## Schritt 6 — Gemeinde gegen übergeordnete Planung

### Anpassungsgebot § 8 Abs. 2 BauGB
- B-Plan muss aus FNP entwickelt werden
- Gemeinde gegen FNP-Änderung des Nachbarn — Antragsbefugnis möglich

### Selbstverwaltungsrecht
- Art. 28 Abs. 2 GG, Art. 11 Abs. 2 BayVerfg
- Gemeinden gegen übergreifende Festsetzungen

## Schritt 7 — Praktische Begründung im Schriftsatz

### Aufbau Antragsbefugnis-Begründung
1. Identifikation Mandant und Eigentumsstellung
2. Verortung Grundstück zur Plangrenze (Lageplan, Maßangaben)
3. Konkreter abwägungserheblicher Belang mit Substanz
4. Verweis auf Aufnahme dieses Belangs in eigener Einwendung im Aufstellungsverfahren (verstärkt aber nicht zwingend)
5. Verweis auf zu erwartende Verletzung in absehbarer Zeit

### Beispielsatz
- "Die Antragstellerin ist Alleineigentümerin des Grundstücks Provinostraße 12, eingetragen im Grundbuch von Augsburg Blatt 4711, das unmittelbar an die nördliche Plangrenze angrenzt. Die im B-Plan festgesetzte Bauhöhe von bis zu 30 m wird zu einer Verschattung der nach Süden orientierten Wohnräume sowie zu einer Verkehrslärmzunahme durch die festgesetzte Tiefgaragenzufahrt führen. Diese Belange sind abwägungserheblich (BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16) und wurden bereits in der Einwendung vom 12.10.2023 substantiiert vorgetragen."

## Schritt 8 — Häufige Fehler bei Antragsbefugnis

- Pauschale Behauptung der Betroffenheit ohne räumlichen Bezug
- Fehlende Substanziierung des Belangs
- Belang, der gerade nicht abwägungserheblich ist (allgemeine Aussicht)
- Fehlende Beifügung Grundbuchauszug bei juristischer Person oder Erbengemeinschaft
- Falsche Antragstellerbezeichnung bei Eheleuten (jeder Eigentümer einzeln)

## Quellen

- VwGO § 47 Abs. 2
- GG Art. 14 Abs. 1, Art. 28 Abs. 2
- BayVerfg Art. 11 Abs. 2
- BauGB § 8 Abs. 2
- BNatSchG § 64
- UmwRG §§ 1 2 3
- BVerwG, Beschluss vom 9.2.1995 – 4 NB 17.94 (Wertminderung)
- BVerwG, Beschluss vom 8.6.2011 – 4 BN 42.10 (Nachbar abwägungserheblich)
- BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16 (Maßstab Möglichkeitstheorie)

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
