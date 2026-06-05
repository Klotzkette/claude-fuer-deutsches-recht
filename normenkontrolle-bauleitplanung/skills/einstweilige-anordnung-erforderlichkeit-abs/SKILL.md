---
name: einstweilige-anordnung-erforderlichkeit-abs
description: "Einstweilige Anordnung Erforderlichkeit ABS: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Einstweilige Anordnung Erforderlichkeit ABS

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Einstweilige Anordnung Erforderlichkeit ABS** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `einstweilige-anordnung-47-abs-6-vwgo` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Massstab Eilbedürftigkeit Baugenehmigung beantragt Antragsbefugnis Aussetzung Vollzug B-Plan Glaubhaftmachung. Output: Eilantrag § 47 Abs. 6 VwGO Schriftsatz. Abgrenzung zu normenkontrollantrag-schriftsatz (Hauptsache) und jahresfrist-47-abs-2-vwgo (Frist beachten). |
| `erforderlichkeit-1-abs-3-baugb` | Prüffeld für erforderlichkeit 1 abs 3 baugb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `festsetzungskatalog-9-baugb-baunvo` | Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche Nutzung GRZ GFZ Vollgeschosse Hoechstgrenzen § 17 BauNVO Stellplaetze § 9 Abs. 1 Nr. 4 BauGB Schallschutz § 9 Abs. 1 Nr. 24 BauGB. Output: Festsetzungs-Prüfprotokoll und Teilunwirksamkeitsbegründung. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Abwaegung) und vorhabenbezogener-bebauungsplan-12-baugb. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Einstweilige Anordnung Erforderlichkeit ABS**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `einstweilige-anordnung-47-abs-6-vwgo`

**Fokus:** Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Massstab Eilbedürftigkeit Baugenehmigung beantragt Antragsbefugnis Aussetzung Vollzug B-Plan Glaubhaftmachung. Output: Eilantrag § 47 Abs. 6 VwGO Schriftsatz. Abgrenzung zu normenkontrollantrag-schriftsatz (Hauptsache) und jahresfrist-47-abs-2-vwgo (Frist beachten).

# Einstweilige Anordnung § 47 Abs. 6 VwGO

## Zweck

Der Eilantrag ist die schärfste Waffe der Mandantenseite. Bei drohendem Vollzug (Baugenehmigung, Baustart) muss er parallel zum Hauptsacheantrag eingereicht werden.

## Schritt 1 — Wortlaut § 47 Abs. 6 VwGO

### Norm
- Das Gericht kann auf Antrag eine einstweilige Anordnung erlassen, wenn dies zur Abwehr schwerer Nachteile oder aus anderen wichtigen Gründen dringend geboten ist

### Bedeutung
- Schutzinstrument für die Zeit zwischen Antragstellung und Hauptsacheentscheidung
- Verhinderung irreversibler Tatsachen-Schaffung

## Schritt 2 — Antragsbefugnis und Statthaftigkeit

### Akzessorietät
- Antragsbefugnis wie im Hauptsacheverfahren § 47 Abs. 2 VwGO
- Statthaftigkeit wie im Hauptsacheverfahren

### Frist
- Innerhalb der Jahresfrist der Hauptsache stellbar
- Eilantrag kann auch vor Einreichung Hauptsache gestellt werden, sofern Hauptsache binnen 14 Tagen folgt

## Schritt 3 — Materielle Voraussetzungen

### Schwerer Nachteil oder wichtige Gründe
- Schwerer Nachteil bei drohender Bautätigkeit
- Wichtige Gründe bei Kettenwirkung des Plans (Folgeplanungen)

### Dringend geboten
- Anstehender Vollzug
- Baugenehmigung beantragt
- Baugenehmigung erteilt
- Bauarbeiten begonnen oder unmittelbar bevorstehend

### Vollzugsfolgenabwägung
- BVerfG-Maßstab für einstweilige Anordnung
- Abwägung Folgen ohne und mit Eilantrag

## Schritt 4 — Folgenabwägung

### Erfolgsprognose Hauptsache
- Wenn Hauptsacheantrag offensichtlich begründet — Eilantrag stattzugeben
- Wenn offensichtlich unbegründet — Eilantrag abzulehnen
- Wenn offen — reine Folgenabwägung

### Folgen ohne Eilanordnung
- Bauarbeiten beginnen
- Nicht-rückbaubare Tatsachen geschaffen
- Mandantenrechte (Eigentum, Wohnqualität) irreversibel beeinträchtigt
- Auch wenn Hauptsache später Erfolg hat, fragwürdiger Rückbau

### Folgen mit Eilanordnung
- Investor verliert Zeit (Geld)
- Stadt verliert Steuermittel
- Sind diese Folgen reversibel? In der Regel ja
- Vollzugsfolgenabwägung tendiert pro Mandant bei drohendem Hochbau

## Schritt 5 — Antrag-Formulierung

### Hauptantrag Eilantrag
- "Der Bebauungsplan Nr. X 'Name' der Stadt Y wird bis zur Entscheidung in der Hauptsache vorläufig außer Vollzug gesetzt."

### Hilfsantrag bei Baugenehmigung
- "Hilfsweise: Die Antragsgegnerin wird angewiesen, auf der Grundlage des Bebauungsplans Nr. X bis zur Entscheidung in der Hauptsache keine Baugenehmigungen zu erteilen."

### Bei Drittwirkung gegen Vorhabenträger
- Parallel-Antrag gegen Sofortvollzug der Baugenehmigung nach § 80 Abs. 5, § 80a VwGO
- Im Verwaltungsgericht (erste Instanz) — Eingang dort sicherstellen

## Schritt 6 — Glaubhaftmachung

### § 920 Abs. 2 ZPO i.V.m. § 173 VwGO
- Antragsteller muss Anspruch und Eilbedürftigkeit glaubhaft machen
- Geringerer Beweismaßstab als Vollbeweis
- Eidesstattliche Versicherung zulässig

### Beweismittel
- Eidesstattliche Versicherung Mandantin zu konkretem Drohstand
- Eidesstattliche Versicherung Sachverständiger zu drohenden Schäden
- Privat-Gutachten als Untermauerung
- Presse-Berichte zu Bauplanung
- Schriftverkehr Stadt-Investor

## Schritt 7 — Schriftsatz-Aufbau

### Aufbau
1. Antrag (Hauptantrag, Hilfsantrag)
2. Statthaftigkeit und Antragsbefugnis (kurz)
3. Sachverhalt (kompakt — Eilrichter haben wenig Zeit)
4. Eilbedürftigkeit
 4.1 Drohender Vollzug konkret (Baugenehmigung beantragt, Bauarbeiten geplant)
 4.2 Irreversibilität bei Realisierung
5. Erfolgsprognose Hauptsache
 5.1 Stärkste Fehler kompakt
 5.2 Verweis auf Hauptsacheschriftsatz für Details
6. Vollzugsfolgenabwägung
 6.1 Folgen ohne Eilanordnung
 6.2 Folgen mit Eilanordnung
 6.3 Saldo
7. Glaubhaftmachung-Anlagen
8. Streitwert

## Schritt 8 — Anlagen Eilantrag

### Pflichtanlagen
- Vollmacht
- Bekanntmachung B-Plan
- Eidesstattliche Versicherung Mandantin
- Nachweis drohenden Vollzugs (Bauantrag, Pressebericht)
- Lageplan
- ggf. Privatgutachten

### Glaubhaftmachung-Beleg
- Eingangsstempel Bauantrag (über Akteneinsicht oder Pressestelle)
- Baustellenfoto
- Aufgrabungs-Nachweis
- Bauherrenversammlung-Protokoll

## Schritt 9 — Streitwert Eilverfahren

### Streitwertkatalog Verwaltungsgerichtsbarkeit
- Halbe Hauptsache
- Bei 60.000 EUR Hauptsache: 30.000 EUR Eilantrag
- Bei Mehrwert-Plänen entsprechend höher

## Schritt 10 — Praktische Hinweise

### Vorbereitung
- Eilantrag parallel zum Hauptsachenantrag drafetn — beide gleichzeitig einreichen, wenn Eilbedarf von Anfang an besteht
- Bei späterem Eilbedarf separat einreichen
- Eilrichter telefonisch über Senatsgeschäftsstelle vorbereiten

### Senatsentscheidung
- In der Regel ohne mündliche Verhandlung
- Beschluss innerhalb Wochen
- Bei besonderer Eile zwischen 1-3 Wochen möglich

### Rechtsmittel
- Beschluss des BayVGH im Eilverfahren ist im Normenkontrollverfahren nicht beschwerdefähig zum BVerwG (§ 152 Abs. 1 VwGO)
- In Sonderkonstellationen (verfassungsrechtlich) Verfassungsbeschwerde möglich

### Bei Erfolg
- Plan vorläufig außer Vollzug
- Genehmigungen können nicht mehr erteilt werden
- Anhängige Baugenehmigungs-Verfahren werden gestoppt

## Schritt 11 — Häufige Fehler

- Eilantrag zu spät — Vollzug bereits eingetreten
- Glaubhaftmachung nur durch Behauptung statt eidesstattliche Versicherung
- Erfolgsprognose zu schwach dargestellt
- Streitwert zu hoch / zu niedrig
- Parallel-Antrag gegen Baugenehmigung versäumt
- Vollzugsfolgenabwägung formelhaft

## Quellen

- VwGO §§ 47 Abs. 6, 80 Abs. 5, 80a, 152, 173
- ZPO § 920 Abs. 2
- BVerwG, Beschluss vom 18.05.2010 – 4 BN 19.10 (Eilantrag B-Plan; bverwg.de)
- BayVGH, Beschluss vom 22.04.2014 – 15 NE 13.2538 (Vollzugsfolgenabwägung; Bayern.Recht)
- BVerwG, Beschluss vom 12.06.2019 – 4 BN 4.19 (Eilantrag B-Plan, schwere Nachteile; bverwg.de)

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026)

- BVerwG 12.06.2019, 4 BN 4.19 — Massstab "schwere Nachteile" beim Eilantrag § 47 Abs. 6 VwGO (bverwg.de)
- BVerwG 23.06.2020, 9 A 22.19 — Klimaschutz als beruecksichtigungspflichtiger Belang (bverwg.de)
- Aktuelle OVG-/VGH-Beschluesse vor Ausgabe ueber landesrecht-[bundesland].de und bverwg.de verifizieren

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `erforderlichkeit-1-abs-3-baugb`

**Fokus:** Prüffeld für erforderlichkeit 1 abs 3 baugb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Erforderlichkeit § 1 Abs. 3 BauGB

## Zweck

Die Erforderlichkeit ist die strengste materielle Hürde und kein Abwägungselement. Wer hier punktet, bringt den Plan ohne Detail-Diskussion zu Fall. Stets beachtlich, nicht rügepflichtig.

## Schritt 1 — Wortlaut und Bedeutung

### § 1 Abs. 3 S. 1 BauGB
- Die Gemeinden haben die Bauleitpläne aufzustellen, sobald und soweit es für die städtebauliche Entwicklung und Ordnung erforderlich ist

### Doppelte Schranke
- Negativ: ein Plan, der nicht erforderlich ist, darf nicht erlassen werden
- Positiv: ein Plan kann erlassen werden, wenn er erforderlich ist
- Erforderlichkeit ist Wirksamkeitsvoraussetzung

### Maßstab
- Nicht "objektiv notwendig"
- Sondern: städtebaulich vertretbares Konzept
- Weiter Spielraum, aber nicht grenzenlos

## Schritt 2 — Planrechtfertigung

### Inhalt Planrechtfertigung
- Erkennbares städtebauliches Konzept
- Konzept muss in der Begründung des Plans dokumentiert sein
- Nicht erforderlich: detaillierte volkswirtschaftliche Begründung

### Typische Planrechtfertigungen
- Innenentwicklung statt Außenentwicklung
- Schaffung Wohnraum bei nachweisbarem Bedarf
- Reaktivierung Brachflächen
- Stadtreparatur städtebaulicher Brüche
- Sicherung sozialer Infrastruktur

### Schwacher Punkt
- Wenn die Begründung nur formelhaft auf "Schaffung von Wohnraum" oder "wirtschaftliche Entwicklung" verweist, ohne Standortbezug
- Wenn die Begründung den Bedarf nicht durch Daten unterlegt
- Wenn die Begründung keine Auseinandersetzung mit dem konkreten Standort enthält

## Schritt 3 — Gefälligkeitsplanung

### Definition
- Planung, die ausschließlich oder überwiegend privaten Interessen eines Investors dient
- Ohne eigenständige städtebauliche Rechtfertigung
- BVerwG, Urteil vom 11.3.1988 – 4 C 56.84

### Indizien
- Initiative ging vom Investor aus, nicht von der Stadt
- Plan-Inhalt exakt zugeschnitten auf das Vorhaben des Investors
- Stadt hat kein eigenes Konzept zum Gebiet
- Wirtschaftliche Beziehung Stadt-Investor (städtebaulicher Vertrag, Durchführungsvertrag)
- Übernahme Planungskosten durch Investor
- Vorhabenträger hat bereits Grundstücke gekauft und vermarktet

### Rechtsfolge
- Plan unwirksam, soweit er reine Gefälligkeitsplanung darstellt
- Aber: vorhabenbezogener B-Plan § 12 BauGB ist nicht per se Gefälligkeitsplanung
- § 12 BauGB legitimiert Vorhabenträger-Initiative, verlangt aber städtebauliches Konzept

## Schritt 4 — Vorhabenbezogener B-Plan § 12 BauGB

### Konstruktion
- Vorhaben- und Erschließungsplan plus B-Plan
- Vorhabenträger schließt mit Gemeinde Durchführungsvertrag
- Plan ist auf das konkrete Vorhaben zugeschnitten

### Erforderlichkeitsprüfung
- Auch hier: städtebauliches Konzept erforderlich
- Aber zulässig, dass Konzept stark auf Vorhaben fokussiert
- Differenzierung: Vorhabenträger-Initiative ja — fehlende Stadt-Konzeption nein

### Häufige Treffer
- Durchführungsvertrag bereits unterzeichnet vor Aufstellungsbeschluss — Vorfestlegung
- Stadt hat keinerlei eigene Anforderungen formuliert
- Plan deckt sich 1:1 mit Investor-Wünschen
- Andere Gestaltungs-Alternativen nicht erwogen

## Schritt 5 — Verhinderungsplanung / Negativplanung

### Definition
- Plan, dessen einziger Zweck die Verhinderung eines bestimmten Vorhabens ist
- Ohne eigenes positives städtebauliches Konzept

### Grundsätzlich unzulässig
- Negativplanung verstößt gegen § 1 Abs. 3 BauGB
- BVerwG, Urteil vom 18.12.1990 – 4 C 16.88

### Ausnahme positiver Auffangbereich
- Wenn die Verhinderung des Vorhabens nur Teil eines breiteren positiven Konzepts ist
- Z.B. Sicherung Mischnutzung, Erhalt Stadtbild, Lärmschutz
- Dann grundsätzlich zulässig

## Schritt 6 — Zeitlicher Aspekt "sobald und soweit"

### "Sobald"
- Frühestens, wenn die städtebauliche Entwicklung es erfordert
- Verfrühte Planung problematisch wenn keine konkrete Anstoßfunktion

### "Soweit"
- Räumlich und sachlich nur soweit erforderlich
- Übermaß-Planung problematisch
- Wenn größere Flächen überplant werden als das Konzept erfordert

### Audit
- Stimmt der Plan-Umgriff mit dem Konzept?
- Werden Flächen ohne erkennbare Konzeptbindung mit überplant?

## Schritt 7 — Abgrenzung Erforderlichkeit / Abwägung

### Zwei verschiedene Stufen
- § 1 Abs. 3 BauGB: ob überhaupt geplant werden darf (Planrechtfertigung)
- § 1 Abs. 7 BauGB: wie geplant wird (Abwägung)
- Erst Erforderlichkeit, dann Abwägung

### Strategische Bedeutung
- Erforderlichkeitsmangel ist nicht heilbar
- Nicht über § 215 BauGB-Rügefrist filterbar
- Im Schriftsatz prominent vor Abwägungsfehlern platzieren

## Schritt 8 — Audit-Schwerpunkte

| Punkt | Prüfung |
|---|---|
| Städtebauliches Konzept in Begründung? | Ja/nein |
| Konzept mit Standortbezug? | Ja/nein |
| Bedarf durch Daten unterlegt? | Ja/nein |
| Initiative Stadt oder Investor? | Stadt/Investor |
| Durchführungsvertrag vor Aufstellungsbeschluss? | Ja/nein |
| Plan-Umgriff entspricht Konzept? | Ja/nein |
| Nur Verhinderung eines konkreten Vorhabens? | Ja/nein |
| Alternativen erwogen? | Ja/nein |

## Quellen

- BauGB § 1 Abs. 3, § 1 Abs. 7, § 8, § 12, § 215
- BVerwG, Urteil vom 11.3.1988 – 4 C 56.84 (Gefälligkeitsplanung)
- BVerwG, Urteil vom 18.12.1990 – 4 C 16.88 (Negativplanung)
- BVerwG, Urteil vom 27.3.2013 – 4 CN 7.11 (Vorhabenbezogener B-Plan)
- BVerwG, Urteil vom 26.3.2009 – 4 C 21.07 (Erforderlichkeitsmaßstab)

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `festsetzungskatalog-9-baugb-baunvo`

**Fokus:** Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche Nutzung GRZ GFZ Vollgeschosse Hoechstgrenzen § 17 BauNVO Stellplaetze § 9 Abs. 1 Nr. 4 BauGB Schallschutz § 9 Abs. 1 Nr. 24 BauGB. Output: Festsetzungs-Prüfprotokoll und Teilunwirksamkeitsbegründung. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Abwaegung) und vorhabenbezogener-bebauungsplan-12-baugb.

# Festsetzungs-Katalog § 9 BauGB iVm BauNVO

## Zweck

§ 9 BauGB ist die zentrale Norm für den Inhalt qualifizierter Bebauungspläne. Sie ist **abschließend** — Festsetzungen außerhalb des Katalogs sind unwirksam. Dieses Skill prüft Bebauungsplan-Festsetzungen auf Rechtsgrundlage und Grenzen.

## Eingaben

- Bebauungsplan-Festsetzungen (textlich beschrieben)
- Planzeichnung (soweit zugänglich)
- Bezugnahme auf BauNVO-Fassung
- Bezug zu sonstigen Spezialgesetzen (BImSchG, BNatSchG, AEG)

## Schritt 1 — § 9 BauGB als abschließender Katalog

### Geltung

- § 9 Abs. 1 BauGB enthält 26 nummerierte Festsetzungs-Tatbestände (Nr. 1 bis 26)
- § 9 Abs. 2 erweitert für besondere Fälle
- § 9 Abs. 3 vorhabenbezogene Bebauungspläne § 12 BauGB
- § 9 Abs. 4 ergänzende Regelungen
- § 9 Abs. 5, 6, 7 Hinweise und Kennzeichnungen (nicht Festsetzungen)
- § 9 Abs. 8 Begründungs-Erfordernis

### Konsequenz Abschließlichkeit

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bezugnahme auf Spezialgesetze nur soweit § 9 BauGB dies zulässt
- Konstruktion **"Hinweise"** vs. **Festsetzungen** entscheidend

## Schritt 2 — Kern-Festsetzungen § 9 Abs. 1

### Nr. 1 — Art der baulichen Nutzung

- Konkretisierung über BauNVO §§ 2 bis 9, 11
- Baugebietstypen: WS, WR, WA, WB, MD, MI, MU, MK, GE, GI, SO
- Ausnahmen und Beschränkungen § 1 Abs. 4-9 BauNVO

### Nr. 2 — Maß der baulichen Nutzung

Drei Faktoren nach § 16 ff. BauNVO:
- Grundflächenzahl GRZ (§ 19 BauNVO)
- Geschossflächenzahl GFZ (§ 20 BauNVO)
- Höhe baulicher Anlagen — Wandhöhe, Firsthöhe, Geschoßzahl (§ 18 BauNVO)
- Bei Festsetzung mehrerer Maß-Werte: kumulativ einzuhalten

#### Höchstgrenzen § 17 BauNVO

| Gebietsart | GRZ | GFZ | Bauliche Anlagenhöhe |
|---|---|---|---|
| WS, WR | 0,4 | 1,2 | – |
| WA, WB | 0,4 | 1,2 (WB 1,6) | – |
| MD | 0,6 | 1,2 | – |
| MI, MU | 0,6/0,8 | 1,2/3,0 | – |
| MK | 1,0 | 3,0 | – |
| GE | 0,8 | 2,4 | – |
| GI | 0,8 | 2,4 | – |
| Sondergebiete | nach Festsetzung | nach Festsetzung | – |

#### Überschreitung § 17 Abs. 2 BauNVO

- Nur bei besonderen städtebaulichen Gründen
- Begründung im Plan zwingend
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Nr. 3 — Überbaubare und nicht überbaubare Grundstücksflächen

- Baulinien, Baugrenzen, Bauteppich
- Bauweise (offen, geschlossen, abweichend)

### Nr. 4 — Stellplätze und Garagen

- Eingeschränkt nutzbar — meist Verweis auf Landesbauordnung
- Konkurrenz mit Art. 47 ff. BayBO
- Stellplatzsatzung der Gemeinde nach Art. 81 BayBO

### Nr. 5 — Flächen für Gemeinbedarf

- Schulen, Kindertagesstätten, kirchliche Anlagen, Verwaltung
- Konkretisierung über Nutzungs-Zweck

### Nr. 6 — Verkehrsflächen

- Öffentliche Straßen, Wege, Plätze, Stellplätze für Fahrräder etc.
- Bahnflächen sind grundsätzlich § 38 BauGB-Spezialregelung (siehe unten)

### Nr. 10 — Grünflächen

- Öffentliche und private Grünflächen
- Hier auch festsetzbar: Spielplätze, Bestattungsstätten, Friedhöfe

### Nr. 14 — Flächen für Versorgungs-Anlagen

- Elektrizität, Gas, Wasser, Wärme, Kommunikation

### Nr. 15 — Flächen für Lagerung von Wasser und Abwasser

### Nr. 18 — Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Boden, Natur und Landschaft

- Wichtig für Eingriffs-Ausgleich
- Externes Ausgleichs-Bereich nach § 9 Abs. 1a BauGB

### Nr. 21 — Schutzpflichten gem. § 41 BImSchG

- Aktive und passive Schallschutz-Maßnahmen

### Nr. 24 — Festsetzung zur Erhaltung gesunder Wohn- und Arbeitsverhältnisse

- Passiver Schallschutz, gestaltete Außenwohnbereiche
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 3 — Festsetzungen außerhalb § 9 BauGB

### Häufige Fehler

#### Fehler 1: Dynamische Verweisung auf Spezialgesetze

- "Es gelten die Anforderungen der DIN xxxx in der jeweils geltenden Fassung"
- Problematisch: Dynamische Verweisung auf ändernde Spezial-Regelungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Fehler 2: Mobilitätskonzept als Festsetzung

- Häufig: B-Plan setzt "Mobilitätskonzept ist Bestandteil der Satzung" fest
- Problematisch: Konkrete Inhalte oft nicht in der Satzung, sondern nur in Anlagen-Papier
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Fehler 3: Energetische Anforderungen über GEG-Standard

- Festsetzung "Effizienzhaus 40" — zulässig nur als Festsetzung der Erschließungs-Tiefenstandards
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Fehler 4: Werbe-Anlagen und Außengastronomie

- Über § 9 BauGB nur eingeschränkt regelbar
- Konkurrenz mit § 81 BayBO örtliche Bauvorschriften — meist diese Norm einschlägig

#### Fehler 5: Photovoltaik-Pflichten

- Über § 9 Abs. 1 BauGB problematisch
- Landesrechtliche Erlaubnis: Art. 44a BayBO (seit 01/2025)

## Schritt 4 — § 9 Abs. 5 6 7 BauGB Hinweise

### § 9 Abs. 5 — Vermerk im Plan

- Bauflächen mit erheblichen Bodennutzungs-Beschränkungen
- Z.B. Altlasten, Bergbauschäden

### § 9 Abs. 6 — Festsetzungen aus anderen Vorschriften

- Soweit andere Rechtsvorschriften Inhalts-Festsetzungen erlauben
- Z.B. Ausgleichs-Flächen nach Naturschutzrecht

### § 9 Abs. 7 — Geltungsbereich

- Räumlicher Geltungsbereich

## Schritt 5 — Bahnflächen § 38 BauGB

### Grundsatz

- Für Bahnflächen gelten Sondervorschriften
- BauGB-Festsetzungen sind eingeschränkt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konsequenz für nicht-entwidmete Bahnflächen

- Stadt kann keine baulichen Festsetzungen treffen
- Vor Entwidmung nach § 23 AEG kein wirksamer B-Plan möglich
- Bei dennoch erfolgter Festsetzung: Teil-Nichtigkeit oder Gesamt-Nichtigkeit

### Prüfungs-Schritt

- Welche Flurstücke sind als Bahnflächen vermerkt?
- Liegt eine Entwidmungs-Entscheidung der Eisenbahn-Verwaltung vor?
- Datum Entwidmung vs. Datum Satzungs-Beschluss

## Schritt 6 — Hochhäuser, Gebäude-Hochhaus-Verordnung

### Bayerische Hochhaus-Richtlinie

- Gebäude über 22 m Hochhaus nach Art. 2 Abs. 4 BayBO
- Brandschutz-Anforderungen
- Festsetzung Hochhaus-Standorte über § 9 Abs. 1 Nr. 1 + Nr. 2 BauGB

### Höhen-Festsetzung

- Wand-/Trauf-/First-Höhe nach § 18 BauNVO
- Bezugshöhe muss klar definiert sein

### Verschattung

- Bei Hochhäusern Verschattungs-Studie erforderlich
- Ermittlungspflicht § 2 Abs. 3 BauGB
- Im Plangebiet-Inneren und in Nachbarschaft

## Schritt 7 — Stellplatz-Festsetzungen

### Rechtsgrundlage

- § 9 Abs. 1 Nr. 4 BauGB (Stellplätze und Garagen)
- Art. 47 BayBO Grundsatz Stellplatzpflicht
- Art. 81 BayBO Stellplatzsatzung als örtliche Bauvorschrift

### Reduzierung durch B-Plan

- Art. 47 Abs. 2 Satz 2 BayBO: B-Plan kann abweichend festsetzen
- Voraussetzungen:
 - städtebauliche Rechtfertigung
 - anderweitige Bedarfsdeckung (z.B. ÖPNV-Nähe, Mobilitätskonzept)
 - Verhältnismäßigkeit

### Praktische Höchstgrenze

- Reduzierung über 50 % verlangt besondere Begründung
- Bei nahezu vollständigem Stellplatz-Verzicht: tragfähiges Mobilitätskonzept zwingend

## Schritt 8 — Schallschutz-Festsetzungen

### Rechtsgrundlage

- § 9 Abs. 1 Nr. 24 BauGB (Erhaltung gesunder Wohn-/Arbeitsverhältnisse)
- § 9 Abs. 1 Nr. 21 BauGB (Schutz-Maßnahmen nach BImSchG)

### Festsetzungs-Typen

- **Aktiver Schallschutz** — Lärmschutzwall, -wand (Festsetzung Lage, Höhe)
- **Passiver Schallschutz** — Schalldämmungs-Anforderungen Außenbauteile
- **Festsetzung Außenwohnbereiche** — bei zulässigen Pegeln

### DIN 18005

- Orientierungswerte:
 - Reines Wohngebiet 50 dB(A) Tag / 35 dB(A) Nacht
 - Allgemeines Wohngebiet 55 / 40 dB(A)
 - Mischgebiet 60 / 45 dB(A)
 - Urbanes Gebiet 63 / 48 dB(A)
- Statische Bezugnahme zulässig

### TA Lärm

- Bei Anlagen-Festsetzungen
- Statische Bezugnahme

## Schritt 9 — Naturschutz-Festsetzungen

### § 9 Abs. 1 Nr. 18 BauGB

- Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Boden, Natur und Landschaft
- Externe Ausgleichs-Maßnahmen § 9 Abs. 1a BauGB

### § 9 Abs. 1 Nr. 20 BauGB

- Flächen für Maßnahmen zum Schutz vor Naturgewalten
- Hochwasserschutz, Bodenerosionsschutz

### Verzahnung BNatSchG

- Eingriffs-Ausgleichs-Bilanz nach § 18 BNatSchG
- Festsetzung Vermeidungs-, Minderungs- und Ausgleichs-Maßnahmen

## Schritt 10 — Prüfraster für Mandanten-Vertretung

### Schritt 10.1 — Festsetzungs-Inventar

- Welche Festsetzungen enthält der Plan?
- Jeweils Rechtsgrundlage benennen lassen

### Schritt 10.2 — Außerhalb-Katalog-Prüfung

- Sind Festsetzungen ohne erkennbare Rechtsgrundlage in § 9 BauGB?
- Bei Verstoß: Teil-Nichtigkeit / Gesamt-Nichtigkeit?

### Schritt 10.3 — Höchstgrenzen-Prüfung § 17 BauNVO

- Werden GRZ/GFZ überschritten?
- Liegen die Voraussetzungen für Überschreitung § 17 Abs. 2 BauNVO vor?
- Begründung im Plan ausreichend?

### Schritt 10.4 — Dynamische Verweisungen

- Bezugnahme auf "jeweils geltende Fassung" einer DIN-Norm?
- Dynamische Verweisung unzulässig → Bestimmtheits-Mangel

### Schritt 10.5 — Mobilitätskonzept-Festsetzung

- Konkret in der Satzung oder nur in Anlage?
- Bestimmtheit ausreichend?

## Schritt 11 — Anwendung auf Bebauungsplan Augsburg Nr. 900

**Beispielsfälle:**

a) **§ 11 Satzung "Mobilitätskonzept"** — Anlage B-1, nur Stichpunktliste. Bestimmtheits-Mangel.

b) **§ 12 Satzung "Energetische Anforderungen"** — Festsetzung "KfW-Effizienzhaus 40". Bezugnahme auf "den jeweils gültigen Standard nach GEG bezogen" — dynamische Verweisung, problematisch.

c) **§ 9 Abs. 4 Satzung "Künstliche Nisthilfen"** — Festsetzung 60 Mauersegler-Nisten + 30 Mehlschwalben-Nisten. § 9 Abs. 1 Nr. 18 BauGB iVm BNatSchG einschlägig. Festsetzung zulässig.

d) **§ 13 Satzung "Materialgebote Fassaden"** — Stoff- und Farbgebote. Über Art. 81 BayBO örtliche Bauvorschrift einschlägig — § 9 BauGB nicht ausreichend.

e) **§ 6 Satzung "Stellplatz 0,3/WE"** — Reduzierung auf 30 % der Stellplatzsatzung-Werte. Art. 47 Abs. 2 Satz 2 BayBO grundsätzlich zulässig, aber **70 % Reduzierung benötigt tragfähiges Mobilitätskonzept**. Im konkreten Fall fragwürdig.

f) **§ 18 Satzung "Bahnflächen"** — Hinweis auf nicht-entwidmete DB-Flächen. § 38 BauGB einschlägig — **keine Festsetzungen zulässig** auf nicht-entwidmeten Bahnflächen.

## Verzahnung mit anderen Skills

- `erforderlichkeit-1-abs-3-baugb`
- `abwaegungsgebot-1-abs-7-baugb`
- `immissionsschutz-laerm-bauleitplanung`
- `stellplatzsatzung-bay-bauordnung`
- `vorhabenbezogener-bebauungsplan-12-baugb`

## Quellen

- BauGB §§ 9, 30, 38
- BauNVO §§ 1-26
- PlanzVO
- BayBO Art. 47, 81
- **BVerwG 04.05.2022, 4 CN 2.21** — Konzentrationszonen-Planung Wind/Solar (bverwg.de)
- **BVerwG 03.04.2020, 4 CN 2.19** — Erhaltungssatzung § 172 BauGB (bverwg.de)
- **BVerwG 17.06.2020, 4 CN 6.18** — Bekanntmachung Bebauungsplan, Anstossfunktion (bverwg.de)
- **BVerwG 11.04.2024, 4 BN 50.23** — Klimaschutz als Abwaegungsbelang (bverwg.de)
- Konkrete weitere Entscheidungen vor Ausgabe per bverwg.de mit Datum verifizieren
- Ernst/Zinkahn/Bielenberg BauGB
- Battis/Krautzberger/Löhr BauGB
- Söfker BauNVO
