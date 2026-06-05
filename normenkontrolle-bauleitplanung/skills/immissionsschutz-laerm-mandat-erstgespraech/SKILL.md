---
name: immissionsschutz-laerm-mandat-erstgespraech
description: "Immissionsschutz Laerm Mandat Erstgespraech: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Immissionsschutz Laerm Mandat Erstgespraech

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Immissionsschutz Laerm Mandat Erstgespraech** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `immissionsschutz-laerm-bauleitplanung` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik Worstcase Trennungsgrundsatz § 50 BImSchG aktive vs. passive Massnahmen Verkehrslaerm BAB Schiene. Output: Immissionsschutz-Prüfprotokoll und Angriffspunkte Normenkontrolle. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Abwaegungsfehler) und umweltbericht-umweltprüfung (UVPG). |
| `mandat-erstgespraech-normenkontrolle` | Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist Statthaftigkeit Erstprüfung Plan-Unterlagen vorlaeufige Erfolgsaussichten Kostenaufklärung RVG Streitwert. Output: Erstgespraechen-Protokoll Mandatsannahme-Empfehlung Fallplan. Abgrenzung zu normenkontrollantrag-schriftsatz (Hauptschriftsatz) und jahresfrist-47-abs-2-vwgo. |
| `muendliche-verhandlung-vgh-strategie` | Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche Beweisanträge Ortsbesichtigung Hilfsanträge Teilunwirksamkeit Wirkungsausspruch Kostenentscheidung. Revision § 132 VwGO nur grundsaetzliche Bedeutung. Output: Verhandlungsstruktur und Plaedoyer-Entwurf. Abgrenzung zu normenkontrollantrag-schriftsatz (Schriftsatz vor Verhandlung) und einstweilige-anordnung-47-abs-6-vwgo. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Immissionsschutz Laerm Mandat Erstgespraech**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `immissionsschutz-laerm-bauleitplanung`

**Fokus:** Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik Worstcase Trennungsgrundsatz § 50 BImSchG aktive vs. passive Massnahmen Verkehrslaerm BAB Schiene. Output: Immissionsschutz-Prüfprotokoll und Angriffspunkte Normenkontrolle. Abgrenzung zu abwaegungsgebot-1-abs-7-baugb (Abwaegungsfehler) und umweltbericht-umweltprüfung (UVPG).

# Immissionsschutz und Lärm in der Bauleitplanung

## Zweck

Lärm ist der häufigste materielle Hebel im Normenkontrollverfahren bei Innenstadt-Plänen. DIN 18005 und TA Lärm liefern die Orientierungswerte, der Trennungsgrundsatz § 50 BImSchG den materiellen Maßstab.

## Schritt 1 — DIN 18005 Schallschutz im Städtebau


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Orientierungswerte (in dB(A))
| Gebietstyp | Tag (6-22 Uhr) | Nacht (22-6 Uhr) |
|---|---|---|
| Reines Wohngebiet | 50 | 40/35 |
| Allgemeines Wohngebiet | 55 | 45/40 |
| Besondere Wohngebiete | 60 | 45/40 |
| Dorfgebiete, Mischgebiete | 60 | 50/45 |
| Kerngebiete | 65 | 55/50 |
| Gewerbegebiete | 65 | 55/50 |

### Status DIN 18005
- Keine Rechtsverordnung, sondern technische Norm
- "Orientierungswerte" — keine zwingenden Grenzwerte
- BVerwG: in der Abwägung als Orientierung heranzuziehen
- Überschreitung erforderlich-begründungspflichtig

### Drei-dB-Sprung
- Bei Überschreitung um mehr als 3 dB(A) — besondere Begründung erforderlich
- Bei mehr als 5 dB(A) — regelmäßig Abwägungsdisproportionalität
- Bei mehr als 10 dB(A) — Disproportionalität fast immer

## Schritt 2 — TA Lärm

### Anwendungsbereich
- Bei gewerblicher Nutzung — Lärm aus Anlagen
- Lärm aus Tiefgaragen
- Lärm aus Anlieferzonen
- Lärm aus Klima- und Lüftungsanlagen

### Grenzwerte (Auszug, Immissionsrichtwert)
- Reines Wohngebiet: Tag 50, Nacht 35
- Allgemeines Wohngebiet: Tag 55, Nacht 40
- Mischgebiet: Tag 60, Nacht 45
- Gewerbegebiet: Tag 65, Nacht 50

### Spitzenpegelregel
- Einzelne Geräuschspitzen dürfen Tag um 30 dB(A), Nacht um 20 dB(A) den Grenzwert überschreiten
- Bei seltenen Ereignissen Sonderregelung

## Schritt 3 — Trennungsgrundsatz § 50 BImSchG

### Wortlaut
- Bei raumbedeutsamen Planungen und Maßnahmen sind die für eine bestimmte Nutzung vorgesehenen Flächen einander so zuzuordnen, dass schädliche Umwelteinwirkungen auf ausschließlich oder überwiegend dem Wohnen dienende Gebiete sowie auf sonstige schutzbedürftige Gebiete soweit wie möglich vermieden werden

### Anwendung B-Plan
- Wohnen nicht direkt neben Industrie
- Wenn unvermeidbar: Schutzmaßnahmen
- Trennungsgrundsatz ist Abwägungsdirektive, kein absolutes Verbot

### Bahnhofsnähe Besonderheit
- Bahnverkehr ist gewachsene Vorbelastung
- Trennungsgrundsatz wirkt für künftige zusätzliche Belastungen
- Schienenverkehr fällt unter 16. BImSchV (Verkehrslärmschutz-VO)

## Schritt 4 — Schienenverkehrslärm 16. BImSchV

### Grenzwerte Schienenverkehr (Neubau/wesentliche Änderung)
- Reines Wohngebiet: Tag 59, Nacht 49
- Allgemeines Wohngebiet: Tag 59, Nacht 49
- Kern-/Mischgebiet: Tag 64, Nacht 54
- Gewerbegebiet: Tag 69, Nacht 59

### Schienenbonus
- Bis 2014 Schienenbonus -5 dB(A)
- Seitdem aufgehoben für Eisenbahn-Verkehr
- Aktuell ohne Bonus zu rechnen

### Bei Plan-Aufstellung in Bahnhofsnähe
- Bestandslärm Schiene durch 16. BImSchV maßgeblich
- Aber: B-Plan kann Neubebauung an die Lärmquelle heranrücken
- Heranrückende Wohnbebauung muss Lärmschutz selbst tragen

## Schritt 5 — Verkehrslärm Straße 16. BImSchV

### Anwendung
- Neubau oder wesentliche Änderung von Verkehrswegen
- Bei B-Plan-Festsetzungen, die Verkehrszuwachs verursachen
- Indirekte Anwendung über § 50 BImSchG

### Berechnung
- RLS-90 (Richtlinie Lärmschutz Straßen)
- Modellierung Verkehrsmenge, Geschwindigkeit, LKW-Anteil, Steigung, Belag

## Schritt 6 — Schallschutzgutachten Audit

### Inhalt eines vollständigen Gutachtens
- Methodik (Mess- und Berechnungsverfahren)
- Eingangsdaten (Verkehrsmenge, Tagesgang, Nachtanteil)
- Worst-case-Szenario
- Berechnungsergebnisse pro Fassade pro Geschoss
- Vergleich mit Orientierungswerten / Grenzwerten
- Schutzkonzept (aktiv/passiv)
- Restrisiko-Darstellung

### Häufige Mängel
- Eingangsdaten zu optimistisch
- Tagesgang glättet Spitzen
- Nachtwert ohne Spitzenpegelbetrachtung
- Nur Best-case statt Worst-case
- Fehlende Berücksichtigung Lärmkumulation aus mehreren Quellen
- Passiver Schallschutz als Hauptkonzept ohne Außenwohnbereich-Schutz

## Schritt 7 — Aktiver und passiver Schallschutz

### Aktiver Schallschutz
- Lärmschutzwand
- Lärmschutzwall mit Begrünung
- Verkehrsverlagerung
- Lärmreduzierte Fahrbahn
- Tempo-Reduzierung

### Passiver Schallschutz
- Schallschutzfenster
- Schalldämmlüfter
- Verschiebung Schlafräume an Lärm-abgewandte Seite
- Selten ausreichend allein

### Außenwohnbereiche
- Balkone, Terrassen, Gärten
- Passive Maßnahmen wirken nicht
- BVerwG: Außenwohnbereiche eigenständig zu schützen
- Häufige Schwachstelle der Stadt-Argumentation

## Schritt 8 — Belange Schlafräume / Außenwohnbereiche

### Schlafräume nachts
- Nachtwert besonders kritisch
- Bei Überschreitung — gesundheitliche Beeinträchtigung
- Lärmwirkung WHO: über 55 dB(A) nachts kardiovaskuläre Risiken

### Außenwohnbereiche
- Tagwert maßgeblich
- Bei Überschreitung Orientierungswert — eingeschränkte Nutzbarkeit
- Wertminderung des Wohngebrauchs

### Schulhöfe / Kitas
- Eigene Sonderschutzbedürftigkeit
- Sportplätze, Kinderspielplätze haben eigene Vorschriften (Sportanlagenlärmschutz-VO 18. BImSchV)

## Schritt 9 — Audit-Punkte Lärm im B-Plan

| Punkt | Prüfung |
|---|---|
| Schallschutzgutachten vorhanden? | Ja/nein |
| Methodik nachvollziehbar? | Ja/nein |
| Worst-case berücksichtigt? | Ja/nein |
| Alle Lärmquellen erfasst (Straße/Schiene/Anlage)? | Ja/nein |
| Tag- und Nachtwerte beide ausgewiesen? | Ja/nein |
| Überschreitungen Orientierungswerte? | Ja/nein |
| Aktiver Schallschutz vorgesehen? | Ja/nein |
| Außenwohnbereiche geschützt? | Ja/nein |
| Trennungsgrundsatz beachtet? | Ja/nein |
| Begründung Überschreitung substantiell? | Ja/nein |

## Schritt 10 — Strategischer Angriffspunkt

### Schwächste Punkte
- Außenwohnbereich-Schutz fehlt — fast immer Schwachpunkt
- Spitzenpegel nicht ermittelt
- Lärmkumulation aus Straße + Schiene + Anlage nicht summiert
- Verkehrsannahmen zu optimistisch

### Im Schriftsatz
- Subsumtion unter § 50 BImSchG und § 1 Abs. 7 BauGB
- Verweis auf DIN 18005-Überschreitung
- Argumentation Disproportionalität wenn > 5 dB(A) ohne Schutz

## Quellen

- BImSchG §§ 41 50, 16. BImSchV, 18. BImSchV
- DIN 18005-1:2002 Schallschutz im Städtebau
- TA Lärm vom 26.8.1998 (zuletzt geändert 1.6.2017)
- RLS-19 (Richtlinien für den Lärmschutz an Straßen 2019)
- BVerwG, Urteil vom 28.5.2014 – 6 A 1.13 (DIN 18005)
- BVerwG, Urteil vom 9.7.2008 – 9 A 14.07 (Außenwohnbereich)
- BVerwG, Urteil vom 19.4.2012 – 4 CN 3.11 (Verkehrslärmprognose)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Lärmschutz

§ 50 BImSchG (Trennungsgrundsatz) → § 41 BImSchG (Verkehrslärmschutz) → 16. BImSchV (Grenzwerte Schiene/Straße) → 18. BImSchV (Sportlärm) → DIN 18005-1 (Orientierungswerte) → § 9 Abs. 1 Nr. 24 BauGB (Schallschutzflächen) → § 1 Abs. 6 Nr. 1 BauGB (allgemeine Wohlfahrtspflege) → § 2 Abs. 3 BauGB (Ermittlungspflicht)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Bearbeitung

Kläre bei Mandantenübernahme:
1. Wo liegt das Plangebiet? (Innenstadt = Vorbelastung; Außenbereich = weniger Vorbelastung)
2. Welche Lärmquellen sind vorhanden? (Straße/Schiene/Anlage/Sportanlage)
3. Wurde eine Lärmkumulation aller Quellen berechnet?
4. Sind Außenwohnbereiche (Balkone Terrassen) ausgewiesen und geschützt?
5. Welche Schutzkonzeption sieht der Plan vor — aktiv oder nur passiv?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Laerm-Ruege im Bauleitplanungsverfahren | Laerm-Ruegeschriftsatz nach Schema; Template unten |
| Variante A — Laermschutz noch in Abwaegung korrigierbar | Einwendung im Abwaegungsverfahren zuerst; Normenkontrolle danach |
| Variante B — Grenzwerte eingehalten aber Summationseffekte | Kumulations-Argumentation; mehrere Emittenten zusammen betrachten |
| Variante C — Betroffener ist Gewerbetreibender selbst | Eigene Emittenten-Stellung beachten; defensivere Argumentation |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Lärm-Rüge im Schriftsatz

**Adressat:** OVG/VGH — Tonfall sachlich-juristisch

```
IV. Verstoß gegen § 50 BImSchG und § 2 Abs. 3 BauGB — Lärmermittlung unvollständig

1. Kumulation Straßen- und Schienenlärm nicht berücksichtigt
 Das Schallschutzgutachten der [BUERO] vom [DATUM] behandelt Straßenlärm und Schienenlärm
 separat. Eine Summenpegel-Berechnung fehlt. Dies begründet ein Ermittlungsdefizit
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Außenwohnbereiche ungeschützt
 Für die auf Blatt [X] ausgewiesenen Balkone und Terrassen in den Fensterlagen [HIMMELSRICHTUNG]
 werden Pegelwerte von [Z] dB(A) tagsüber erreicht — [N] dB(A) über DIN 18005-Orientierungswert.
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

3. Abwägungsdisproportionalität
 Die Überschreitung beträgt [X] dB(A). Bei mehr als 5 dB(A) ohne aktive Schutzmaßnahmen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 2. `mandat-erstgespraech-normenkontrolle`

**Fokus:** Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist Statthaftigkeit Erstprüfung Plan-Unterlagen vorlaeufige Erfolgsaussichten Kostenaufklärung RVG Streitwert. Output: Erstgespraechen-Protokoll Mandatsannahme-Empfehlung Fallplan. Abgrenzung zu normenkontrollantrag-schriftsatz (Hauptschriftsatz) und jahresfrist-47-abs-2-vwgo.

# Erstgespräch Normenkontroll-Mandat

## Zweck

Erste Sortierung eines Mandats gegen einen Bebauungsplan, Flächennutzungsplan oder eine örtliche Bauvorschrift. Ergebnis: belastbare Erst-Einschätzung der Erfolgsaussichten und Mandatsannahme-Entscheidung.

## Schritt 1 — Mandantendaten und Betroffenheitsfeststellung

### Persönliche Daten
- Name, Anschrift, Geburtsdatum, Kontakt
- Eigentumsverhältnisse am betroffenen Grundstück (Alleineigentum, Miteigentum, Wohnungseigentum)
- Grundbuchauszug aktuell beziehen lassen
- Familienstand bei gemeinschaftlichem Eigentum

### Räumliche Lage
- Adresse Mandantengrundstück
- Adresse / Bezeichnung Plangebiet
- Abstand Grundstücksgrenze zu Plangebiet
- Skizze Lageplan oder Auszug Stadtplan zur Akte
- Sichtbeziehung, Verkehrsbeziehung, Topografie

### Konkrete Betroffenheit
- Innerhalb Plangebiet — direkte Festsetzungsbetroffenheit
- Außerhalb Plangebiet — drittbetroffener Nachbar
- Belang: Verschattung, Lärm, Verkehr, Geruch, Wertminderung, Aussicht, Klima

## Schritt 2 — Plan-Identifikation

### Pflichtangaben
- Genaue Bezeichnung des Plans (Nummer, Name, Stadt, Stadtteil)
- Aufstellungsbeschluss-Datum
- Beschluss als Satzung
- Bekanntmachungsdatum und Ort (Amtsblatt, Tageszeitung)
- Inkrafttreten
- Art des Plans: B-Plan qualifiziert, einfach, vorhabenbezogen § 12 BauGB, Bebauungsplan der Innenentwicklung § 13a BauGB, FNP, örtliche Bauvorschrift § 9 Abs. 4 BauGB i.V.m. Art. 81 BayBO

### Beschaffung der Planunterlagen
- Bei der planenden Gemeinde mündlich oder schriftlich anfordern
- Online-Bauleitplan-Auskunft sichten
- Bekanntmachung als PDF
- Satzungstext mit textlichen Festsetzungen
- Planurkunde zeichnerisch
- Begründung mit Umweltbericht
- Abwägungsdokumentation Stadtrat

## Schritt 3 — Vier Säulen Zulässigkeit § 47 VwGO

### Säule 1 — Statthaftigkeit
- Im Rang unter Landesgesetz stehende Rechtsvorschrift
- B-Plan und örtliche Bauvorschrift in Bayern erfasst (§ 47 Abs. 1 Nr. 1 VwGO i.V.m. Art. 5 BayAGVwGO)
- FNP grundsätzlich nicht statthaft — aber wenn Festsetzungen mit Außenwirkung (Konzentrationsflächen Windenergie § 35 Abs. 3 S. 3 BauGB) ja
- Frühzeitige Klärung welcher Plan angegriffen wird

### Säule 2 — Antragsbefugnis § 47 Abs. 2 VwGO
- Möglichkeitstheorie: Geltendmachung einer Rechtsverletzung möglich
- Eigentümer im Plangebiet immer
- Nachbar bei abwägungserheblichem Belang (BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16)
- Anerkannter Naturschutzverband § 64 BNatSchG, § 2 UmwRG

### Säule 3 — Antragsfrist § 47 Abs. 2 S. 1 VwGO
- Ein Jahr ab Bekanntmachung der Norm
- Heute kein 2-Jahres-Zeitraum mehr (Verkürzung durch Gesetz vom 22.12.2006)
- Bei Eilbedarf Fristprüfung sofort
- Wiedereinsetzung § 60 VwGO nur bei unverschuldeter Versäumung

### Säule 4 — Rechtsschutzbedürfnis
- Bei Vollzug bereits abgeschlossen — Rechtsschutzbedürfnis problematisch
- Bei Vollzug noch nicht erfolgt — gegeben
- Bei Genehmigung bereits erteilt — parallel Klage gegen Genehmigung erforderlich

## Schritt 4 — Mandantenchronologie und Beteiligung

### Eigene Beteiligung am Aufstellungsverfahren
- An früher Beteiligung § 3 Abs. 1 BauGB teilgenommen?
- Schriftliche Einwendung in förmlicher Beteiligung § 3 Abs. 2 BauGB abgegeben?
- Wortlaut der Einwendungen sichern (eigene Korrespondenz, Mail-Archiv, Eingangsbestätigung Stadt)
- An Bürgerversammlung teilgenommen?
- Mit anderen Anwohnern vernetzt? Bürgerinitiative?

### Bedeutung für Rügefrist § 215 BauGB
- Verfahrensfehler nur dann beachtlich, wenn innerhalb eines Jahres nach Bekanntmachung gerügt
- Wer eingewendet hat, hat in der Regel die Substanz bereits dokumentiert
- Wer nicht eingewendet hat, ist nicht präkludiert (BVerwG, Urteil vom 18.11.2010 – 4 CN 3.10) — aber materiell schwächer
- Anwältin muss die Einwendungen kennen, um Rüge zu fertigen

## Schritt 5 — Erste Erfolgsaussichtenprognose

### Schnellscan-Punkte
- Stimmt die Verfahrenskette in der Begründung formal? Beschlüsse, Bekanntmachungen, Auslegung?
- Gibt es einen Umweltbericht? Plausibel?
- Ist die Abwägung mehr als formelhaft?
- Sind Stellplätze, Lärm, Artenschutz ernsthaft behandelt?
- Hinweise auf Vorfestlegung oder Gefälligkeitsplanung?

### Prognose-Kategorien
- Erfolgsaussichten gering — Mandatsablehnung empfehlen
- Erfolgsaussichten offen — Mandat mit klarer Kosten-Aufklärung
- Erfolgsaussichten gut — Mandat einschließlich Eilantrag prüfen
- Erfolgsaussichten sehr gut — Mandat plus Eilantrag plus parallele Drittklage

## Schritt 6 — Kosten und Streitwert

### Streitwert
- Streitwertkatalog Verwaltungsgerichtsbarkeit Nr. 9.8.1
- Im Regelfall 60.000 EUR pro Antragsteller, mindestens
- Bei wirtschaftlich besonders bedeutendem Plan höher
- Eilantrag § 47 Abs. 6 VwGO: halber Hauptsachestreitwert

### Gebühren RVG
- 1,6-fache Verfahrensgebühr Nr. 3200 VV RVG
- 1,2-fache Terminsgebühr Nr. 3202 VV RVG
- Auslagenpauschale Nr. 7002 VV RVG
- Mandantengespräch über mögliche Mehrkosten Gutachten Schallschutz / Artenschutz

### Wahl-Vereinbarung
- Stundensatz Wahlmandat möglich — schriftliche Honorarvereinbarung § 3a RVG
- Bei Verbandsklage Naturschutz oft RVG plus Spendenakquise

## Schritt 7 — Akten- und Fristanlage

### Akte
- Mandatsbogen
- Vollmacht
- Plan-Mappe mit allen Plan-Unterlagen
- Mandantenchronologie
- Aktennotiz Erstgespräch
- Streitwert- und Kosten-Note

### Fristen
- **Jahresfrist § 47 Abs. 2 VwGO** ab Bekanntmachung — primäre Frist
- **Rügefrist § 215 BauGB** ein Jahr ab Bekanntmachung — parallele Sicherungsfrist
- Beide Fristen mit zweifacher Vorfrist im Fristenkalender (zwei Wochen vor Ablauf, vier Wochen vor Ablauf)

## Schritt 8 — Mandatsannahme oder Ablehnung

### Annahme
- Schriftliche Auftragsbestätigung
- Übersendung Honorarvereinbarung
- Ankündigung Akteneinsicht bei der Gemeinde

### Ablehnung
- Begründung schriftlich
- Hinweis auf Frist
- Hinweis auf andere Beratungswege
- Datenschutzkonforme Vernichtung der überlassenen Unterlagen oder Rückgabe

## Quellen

- VwGO §§ 47 60
- BauGB §§ 1 2 3 4 8 10 12 13a 35 214 215
- BNatSchG § 64
- UmwRG § 2
- BayAGVwGO Art. 5
- BayBO Art. 47 81
- RVG § 3a, VV RVG Nr. 3200 3202 7002
- Streitwertkatalog Verwaltungsgerichtsbarkeit 2013 Nr. 9.8.1
- BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16 (Antragsbefugnis Nachbar)
- BVerwG, Urteil vom 18.11.2010 – 4 CN 3.10 (Präklusionswirkung Einwendung)

## Aktuelle Rechtsprechung — Triage-relevante Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `muendliche-verhandlung-vgh-strategie`

**Fokus:** Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche Beweisanträge Ortsbesichtigung Hilfsanträge Teilunwirksamkeit Wirkungsausspruch Kostenentscheidung. Revision § 132 VwGO nur grundsaetzliche Bedeutung. Output: Verhandlungsstruktur und Plaedoyer-Entwurf. Abgrenzung zu normenkontrollantrag-schriftsatz (Schriftsatz vor Verhandlung) und einstweilige-anordnung-47-abs-6-vwgo.

# Mündliche Verhandlung BayVGH/OVG

## Zweck

Die mündliche Verhandlung ist der entscheidende Auftritt. Senatsentscheidungen fallen in der Regel kurz danach. Vorbereitung und strukturiertes Plädoyer entscheiden.

## Schritt 1 — Vor der Verhandlung

### Termin-Bekanntgabe
- Senatsgeschäftsstelle versendet Ladung
- Verhandlungstermin meist 6-12 Monate nach Schriftsatzeingang
- Vor- und Nachbereitungszeit blocken

### Senatsbesetzung
- Drei Berufsrichter
- Drei ehrenamtliche Richter (Senat in Hauptsache-Besetzung)
- Berichterstatter führt das Verfahren

### Akteneinsicht Gerichtsakte
- § 100 VwGO
- Vor Termin Akteneinsicht beantragen
- Aktenstand der Stadt überprüfen
- Neue Schriftsätze der Gegenseite auswerten

## Schritt 2 — Vorbereitung Mandantin

### Anwesenheit
- Persönliche Anwesenheit nicht Pflicht
- Aber dringend empfohlen
- Eindruck auf Senat zählt — Mandantin als betroffene Person

### Vorbesprechung
- Ablauf erklären
- Mögliche Fragen Senats antizipieren
- Verhaltensregeln im Saal (Stehen bei Senatseintritt, höfliche Anrede)
- Was nicht sagen (keine Selbstbelastung, keine Spekulation)

### Vollmacht
- Schriftliche Vollmacht im Original mitführen

## Schritt 3 — Vorbereitung Schriftsatz

### Letzter Schriftsatz vor Verhandlung
- Replik auf gegnerische Schriftsätze
- Zuspitzung der schärfsten Punkte
- Spätestens 2 Wochen vor Termin einreichen
- Beweisanträge schriftlich angekündigt

### Beweisanträge
- Sachverständigengutachten Lärm / Verkehr / Artenschutz
- Augenscheinseinnahme vor Ort
- Zeugenvernehmung (Bürgerversammlung-Teilnehmer, Stadtrats-Mitglieder)
- Urkundenbeweis durch Beiziehung Verfahrensakten Stadt

## Schritt 4 — Ortsbesichtigung / Augenscheinseinnahme

### Anregung
- Bei räumlich komplexem Sachverhalt anregen
- Senat kann beschließen, Termin vor Ort durchzuführen
- Sehr wirksam bei Verschattung, Lärm, Stadtbild

### Vorbereitung
- Treffpunkt-Adresse
- Standort-Karte mit relevanten Punkten
- Mandantin als Ortskundige
- ggf. Sachverständiger anwesend

## Schritt 5 — Ablauf Verhandlung

### Typischer Ablauf
1. Aufruf der Sache
2. Feststellung Anwesenheit
3. Sachverhalt durch Berichterstatter
4. Beratung des Senats untereinander (kurz, häufig im Saal)
5. Anträge stellen
6. Plädoyer Antragstellerin
7. Plädoyer Antragsgegnerin und Beigeladene
8. Schlussworte
9. Beratung Senat (Unterbrechung)
10. Verkündung oder Verkündungstermin

### Dauer
- 1-3 Stunden typisch
- Bei komplexen Plänen ganztägig möglich

## Schritt 6 — Plädoyer-Aufbau

### Empfohlener Aufbau (15-30 Minuten)
1. **Einleitung** (1-2 Minuten)
 - Konkrete Mandantenbetroffenheit
 - Schlüsselsatz: warum dieser Plan unwirksam ist
2. **Sachverhalt** (2-3 Minuten)
 - Nur die für den Senat wichtigen Tatsachen
 - Verweis auf Schriftsatz für Details
3. **Verfahrensfehler** (5-7 Minuten)
 - Anstoßfunktion / Auslegung / Umweltbericht
 - Subsumtion § 214 BauGB
4. **Materielle Fehler** (8-12 Minuten)
 - Erforderlichkeit (wenn vorhanden) — kurz und scharf
 - Abwägungsausfall (Vorfestlegung) — mit Belegen
 - Abwägungsdefizit / Fehlgewichtung — pro Belang
 - Disproportionalität — Ergebnis
5. **Schluss** (1-2 Minuten)
 - Hilfsantrag Teilunwirksamkeit
 - Antrag

### Stil
- Frei sprechen, nicht ablesen
- Blickkontakt zum Senat
- Wichtigste Punkte zuerst
- Senat-Hinweise und Zwischenfragen ernst nehmen

## Schritt 7 — Anträge

### Hauptantrag
- Wie im Schriftsatz

### Hilfsanträge
- Teilunwirksamkeit
- Hilfsweise: Ortsbesichtigung
- Hilfsweise: Sachverständigengutachten

### Beweisanträge
- Schriftlich überreichen
- Antrag-Begründung kurz mündlich

## Schritt 8 — Wirkungsausspruch Senat

### Bei Erfolg
- Senat spricht Unwirksamkeit aus
- Allgemeinverbindlich (erga omnes)
- Plan ist nichtig — keine künftigen Genehmigungen möglich
- Bereits erteilte Genehmigungen wirken weiter (mangels eigener Anfechtung)

### Bei Teilerfolg
- Teil-Unwirksamkeitserklärung
- Nur soweit der unwirksame Teil reicht
- Voraussetzung: Plan ist im Übrigen sinnvoll

### Bei Misserfolg
- Antrag wird zurückgewiesen
- Kosten der Antragstellerin

### Bei prozessualer Erledigung
- Wenn Stadt während des Verfahrens Plan aufhebt — Erledigung
- Fortsetzungsfeststellungs-Interesse prüfen

## Schritt 9 — Revision § 132 VwGO

### Voraussetzung
- Grundsätzliche Bedeutung
- Abweichung von BVerwG-Rechtsprechung
- Verfahrensmangel

### Statthaftigkeit
- Revision durch BVerwG zugelassen
- Senat-Zulassung in Urteil oder Beschwerde gegen Nichtzulassung

### Frist
- Revision binnen einem Monat nach Zustellung des Urteils

## Schritt 10 — Kostenentscheidung

### § 154 VwGO
- Kostenverteilung nach Obsiegen / Unterliegen
- Bei Teilerfolg quotenmäßig

### Beigeladene
- Eigene Kostentragung als Regel
- Bei aktiver Antragstellung Kostenbeteiligung

## Schritt 11 — Nach der Verhandlung

### Bei Verkündung
- Sofort schriftliches Urteil anfordern
- Mandantin informieren

### Bei Verkündungstermin
- Termin 2-6 Wochen nach Verhandlung
- Anwesenheit nicht zwingend

### Mandantin-Briefing
- Wirkung erläutern
- Folgeverfahren prüfen (Schadensersatz?)
- Rechtsmittel-Möglichkeit besprechen

## Schritt 12 — Häufige Verhandlungsfehler

- Plädoyer zu lang und detailverliebt
- Wichtigste Punkte am Ende statt am Anfang
- Beweisanträge spontan statt schriftlich vorbereitet
- Mandantin unvorbereitet auf Senatsfragen
- Reaktion auf Gegenseite nicht souverän
- Schlüsselanträge vergessen zu stellen

## Quellen

- VwGO §§ 47 100 101 102 103 104 132 154 167
- ZPO § 916 ff. (Beweisanträge)
- BVerwG, Urteil vom 9.4.2008 – 4 CN 1.07 (Wirkungsausspruch)
- BayVGH-Verfahrensordnung, Praxiserlasse

## Aktuelle Rechtsprechung — Leitsaetze Verhandlung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
