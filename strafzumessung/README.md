# Strafzumessung

Plugin für die **Strafzumessung nach deutschem Strafrecht** — vom Strafbefehl bis zur großen Strafkammer. Adressaten: Strafverteidiger und Staatsanwaltschaft.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Strafzumessung (`strafzumessung`, dieses Plugin) | [strafzumessung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafzumessung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Worum geht es?

Strafzumessung ist die zentrale richterliche Aufgabe nach Schuldspruch: Bestimmung von Strafart und Strafhoehe innerhalb des gesetzlichen Strafrahmens auf Grundlage der **Schuld** (§ 46 Abs. 1 Satz 1 StGB), unter Beruecksichtigung der **praeventiven Wirkungen** (§ 46 Abs. 1 Satz 2 StGB), nach den **Strafzumessungstatsachen** des § 46 Abs. 2 StGB und unter Beachtung des **Doppelverwertungsverbots** (§ 46 Abs. 3 StGB).

Das Plugin deckt die Strafzumessung vom Strafbefehlsverfahren ueber die Hauptverhandlung bis zur Vollstreckung ab, inklusive Bewaehrung, Strafmilderung, Regelbeispielen, Gesamtstrafenbildung, Verstaendigung und Jugendstrafrecht.

## Schnellstart

1. Mit `orientierung-strafzumessung-triage` einsteigen.
2. Rolle (Strafverteidigung, Staatsanwaltschaft) und Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe) angeben.
3. Den vom Triage-Skill empfohlenen Spezial-Skill aktivieren.
4. Bei Bedarf parallel mit den Plugins `strafbefehl-verteidiger` oder `fachanwalt-strafrecht` arbeiten.

## Enthaltene Skills

### Block A — Orientierung und Grundlagen
- `orientierung-strafzumessung-triage` — Einstieg, Triage, Spezial-Skill-Routing.
- `paragraph-46-stgb-grundsatz-strafzumessung` — § 46 StGB, Schuld als Grundlage.
- `strafzumessungs-tatsachen-46-ii-stgb` — Katalog § 46 Abs. 2 StGB.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik vor jeder Zumessung.

### Block B — Geldstrafe
- `geldstrafe-tagessatzanzahl-bestimmen` — § 40 Abs. 1 StGB, Tagessatzanzahl als Schuldgroesse.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — § 40 Abs. 2 StGB, Nettoeinkommen / 30.
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Vorrang Geldstrafe; § 47 StGB.

### Block C — Freiheitsstrafe und Bewaehrung
- `freiheitsstrafe-strafmass-pruefen` — Konkrete Zumessung im Strafrahmen.
- `bewaehrung-56-stgb-positive-sozialprognose` — § 56 StGB.
- `bewaehrung-auflagen-und-weisungen-56b-c-stgb` — §§ 56b, 56c StGB.
- `bewaehrungswiderruf-56f-stgb` — § 56f StGB.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — U-Haft-Anrechnung § 51 StGB, Reststrafenaussetzung § 57 StGB.

### Block D — Strafmilderung und Schaerfung
- `strafmilderung-49-stgb-zwingend-fakultativ` — § 49 StGB.
- `minder-schwerer-fall-und-besonders-schwerer-fall` — Strafrahmen-Modifikation.
- `regelbeispiele-rechtsprechung` — § 243 StGB, § 263 Abs. 3 StGB u.a.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — § 46a StGB; BGH 4 StR 232/25.

### Block E — Strafbefehl und kleine Verfahren
- `strafbefehl-strafzumessung-407-stpo` — Strafzumessung im Strafbefehl.
- `153a-stpo-einstellung-gegen-auflage` — Einstellung mit Auflage.

### Block F — Hauptverhandlung und Verstaendigung
- `verstaendigung-257c-stpo-strafzumessung` — § 257c StPO; BVerfG 2 BvR 2628/10; BGH 1 StR 525/11.
- `gestaendnis-und-strafmilderung` — Gestaendnis als Strafmilderungsgrund.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Strafurteil-Begruendung.

### Block G — Gesamtstrafenbildung
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — §§ 53, 54 StGB.
- `nachtraegliche-gesamtstrafenbildung-55-stgb` — § 55 StGB, Zaesurwirkung, § 460 StPO.
- `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` — BGH-staendige Linie.

### Block H — Sonderfaelle
- `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` — JGG; § 105 JGG Heranwachsende.

## Querverweise zu anderen Plugins

- `strafbefehl-verteidiger` — Spezial-Plugin Strafbefehlsverfahren.
- `fachanwalt-strafrecht` — Strafrechts-Gesamtverteidigung, Plaedoyer, Revision.
- `verkehrsowi-verteidiger` — Verkehrs-OWi-Strafzumessung.
- `urteilsbauer-relationsmacher` — Urteilsverfassung.
- `subsumtions-pruefer` — vor Schuldspruch.

## Hinweise zur Anwendung

- **Quellenregel beachten**: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Aktenzeichen vor Zitat in **dejure.org** oder **openjur.de** verifizieren. Lizenzierte Datenbanken nur bei vorhandenem Zugang.
- **Keine Praejudizienbindung** (Ausnahme § 31 BVerfGG). BGH-Linien sind argumentationsstuetzend, nicht bindend.
- **Mandantengeheimnis** wahren (§ 43a Abs. 2 BRAO; § 203 StGB).
- **Frueher BGH-Beschluss** zum TOA: BGH, Beschluss vom 20.11.2025 — 4 StR 232/25 (friedensstiftender kommunikativer Prozess).
- **BVerfG zur Verstaendigung**: 2 BvR 2628/10 vom 19.03.2013.
- **BGH-Belehrungspflicht**: 1 StR 525/11 vom 07.02.2012.

## Stand

- 05/2026.
- §§ 38 ff. StGB, §§ 407 ff. StPO, JGG, BtMG.
- Aktualitaetspruefung jaehrlich empfohlen.

## Lizenz

Apache-2.0 OR MIT (siehe Plugin-Root).


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `153a-stpo-einstellung-gegen-auflage` | Einstellung gegen Auflage nach § 153a StPO. Zustimmungserfordernis Staatsanwaltschaft, Gericht und Beschuldigter. Voraussetzung kein oeffentliches Interesse an der Strafverfolgung Vergehen. Auflagen Geldzahlung gemeinnuetzige Arbeit Scha... |
| `267-iii-stpo-begruendungsanforderungen-strafurteil` | Begruendungsanforderungen an die Strafzumessung im Strafurteil § 267 Abs. 3 StPO. Pflicht zur Mitteilung der bestimmenden Strafzumessungsgruende. Strafrahmen, Schuldrahmen, Strafzumessungstatsachen § 46 Abs. 2 StGB. Bewaehrungs- und Stra... |
| `bewaehrung-56-stgb-positive-sozialprognose` | Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Voraussetzungen positive Sozialprognose Abs. 1 bis 1 Jahr; besondere Umstaende Abs. 2 bis 2 Jahre; Verteidigung der Rechtsordnung Abs. 3. Prognose-Faktoren Vorleben, soziale Bin... |
| `bewaehrung-auflagen-und-weisungen-56b-c-stgb` | Auflagen § 56b StGB und Weisungen § 56c StGB im Bewaehrungsbeschluss. Auflagen dienen der Genugtuung Wiedergutmachung Geldzahlung gemeinnuetzige Arbeit. Weisungen lenken kuenftiges Verhalten Aufenthalt Beruf Therapie Kontaktverbot. Bewae... |
| `bewaehrungswiderruf-56f-stgb` | Widerruf der Strafaussetzung zur Bewaehrung nach § 56f StGB. Widerrufsgruende neue Straftat in der Bewaehrungszeit, Verletzung von Auflagen Weisungen, Entziehung von der Bewaehrungshilfe. Verhaeltnismaessigkeitspruefung. Beschluss-Verfah... |
| `freiheitsstrafe-ohne-bewaehrung-vollstreckung` | Freiheitsstrafe ohne Bewaehrung. Anrechnung Untersuchungshaft und Auslieferungshaft § 51 StGB. Vollstreckungsplanung Reststrafenaussetzung § 57 StGB Halbstrafe Drittel. Lebenslang § 57a StGB. Strafaufschub § 456 StPO. Strafunterbrechung... |
| `freiheitsstrafe-strafmass-pruefen` | Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB. Strafrahmen pruefen, Strafhoehe innerhalb des Schuldrahmens bestimmen, Wechselwirkung mit Bewaehrung (§ 56 StGB) und Aussetzung des Strafrests (§ 57 StGB). Faustwerte fuer typ... |
| `geldstrafe-tagessatzanzahl-bestimmen` | Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs. 1 StGB. 5 bis 360 Tagessaetze als Grundgrenze; bei Gesamtgeldstrafe bis 720 Tagessaetze. Die Anzahl bildet die Schuldkomponente und folgt § 46 StGB. Abgrenzung zur Tagessatzhoe... |
| `geldstrafe-vs-freiheitsstrafe-47-stgb` | Vorrang der Geldstrafe vor kurzer Freiheitsstrafe nach § 47 StGB. Kurze Freiheitsstrafe unter 6 Monaten nur bei besonderen Umstaenden in der Tat oder in der Persoenlichkeit. Begruendungspflicht des Gerichts. Verhaeltnis Geldstrafe + Frei... |
| `gesamtstrafenbildung-53-54-stgb-erste-instanz` | Erstinstanzliche Gesamtstrafenbildung bei Realkonkurrenz §§ 53 und 54 StGB. Einzelstrafen werden zuerst gebildet; danach Gesamtstrafe aus der hoechsten Einzelstrafe (Einsatzstrafe) plus angemessener Erhoehung. Obergrenze § 54 Abs. 2 StGB... |
| `gestaendnis-und-strafmilderung` | Gestaendnis als Strafmilderungsgrund. Umfang Reichweite Glaubhaftigkeit. Differenzierung schlankes Gestaendnis vs. qualifiziertes Gestaendnis. Verbindung zu Reue und Wiedergutmachung. Wirkung in der Strafzumessung praktisch 25 bis 33 Pro... |
| `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` | Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung wenn Einbeziehung nach § 55 StGB nicht moeglich ist (Strafe bereits vollstreckt, verjaehrt oder erlassen, Bewaehrung abgelaufen, Auslandsstrafen). BGH-staendige Linie: Schutzzweck... |
| `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` | Strafzumessung im Jugendstrafrecht. Erziehungsgedanke § 2 JGG. Massnahmen-Trio: Erziehungsmassregeln §§ 9-12 JGG, Zuchtmittel §§ 13-16 JGG, Jugendstrafe §§ 17-18 JGG. Voraussetzung Jugendstrafe schaedliche Neigungen oder Schwere der Schu... |
| `minder-schwerer-fall-und-besonders-schwerer-fall` | Strafrahmen-Modifikation durch minder schweren Fall (Strafrahmen-Senkung) und besonders schweren Fall (Strafrahmen-Anhebung). Gesamtwuerdigung aller Tat- und Taeter-Umstaende. Beziehung zu Regelbeispielen. Konkurrenz minder schwerer Fall... |
| `nachtraegliche-gesamtstrafenbildung-55-stgb` | Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Voraussetzung: spaetere Tat wurde **vor** einer frueheren Verurteilung begangen (Zaesurwirkung). Beschluss-Verfahren § 460 StPO. Einbeziehung rechtskraeftiger Strafen. Haerteausgleich,... |
| `orientierung-strafzumessung-triage` | Einstieg und Triage im Plugin Strafzumessung. Ordnet das Mandat (Strafverteidiger, Staatsanwaltschaft, Beistand) nach Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe), erkennt Eilf... |
| `paragraph-46-stgb-grundsatz-strafzumessung` | Grundsatznorm der Strafzumessung § 46 StGB. Schuld als Grundlage (Abs. 1 Satz 1), praeventive Wirkungen auf das kuenftige Leben des Taeters (Abs. 1 Satz 2), Katalog der Strafzumessungstatsachen (Abs. 2), Doppelverwertungsverbot (Abs. 3).... |
| `regelbeispiele-rechtsprechung` | Regelbeispielkataloge im Strafrecht. § 243 StGB Diebstahl (Einbruch, Bandentat, Gewerbsmaessigkeit, Sache von erheblichem Wert). § 263 Abs. 3 StGB Betrug (Gewerbsmaessigkeit, hoher Vermoegensverlust, Anschlag auf das Vermoegen, Wirtschaf... |
| `strafbefehl-strafzumessung-407-stpo` | Strafzumessung im Strafbefehl § 407 StPO. Strafrahmen Strafbefehl bis 360 Tagessaetze Geldstrafe; Freiheitsstrafe bis 1 Jahr nur mit Bewaehrung und nur bei Pflichtverteidiger. Pauschalisierung der Strafzumessung. Tagessatzhoehe oft schae... |
| `strafmilderung-49-stgb-zwingend-fakultativ` | Strafmilderung nach § 49 StGB. Abs. 1 zwingende Milderung mit konkreten Bezugsgroessen Hoechstmass 3/4 Mindeststrafe ermaessigt; bei lebenslang 3 bis 15 Jahre. Abs. 2 fakultative Milderung bis zum gesetzlichen Mindestmass. Anwendungsfael... |
| `strafrahmen-und-strafzumessungsstufen` | Strafrahmen-Logik vor der konkreten Zumessung. Aufbau abstrakter Strafrahmen aus Grundtatbestand, Qualifikation, Privilegierung. Modifikationen durch Regelbeispiele und minder schweren Fall. Verschiebung durch §§ 49 Abs. 1 23 Abs. 2 28 A... |
| `strafzumessungs-tatsachen-46-ii-stgb` | Katalog der Strafzumessungstatsachen § 46 Abs. 2 StGB. Beweggruende und Ziele (auch menschenverachtende), Gesinnung und Wille, Mass der Pflichtwidrigkeit, Art der Ausfuehrung und verschuldete Auswirkungen, Vorleben, persoenliche und wirt... |
| `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` | Taeter-Opfer-Ausgleich § 46a StGB und Schadenswiedergutmachung als Strafmilderung oder Absehen von Strafe. Nr. 1 Wiedergutmachung gegenueber dem Verletzten erfordert friedensstiftenden kommunikativen Prozess (BGH 4 StR 232/25 vom 20.11.2... |
| `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` | Bestimmung der Tagessatzhoehe nach § 40 Abs. 2 StGB. Hoehe richtet sich nach Nettoeinkommen geteilt durch 30; Mindesthoehe 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Sonderfaelle Arbeitslose, Buergergeld-Empfaenger, Studieren... |
| `verstaendigung-257c-stpo-strafzumessung` | Verstaendigung im Strafverfahren § 257c StPO und Strafzumessung. Strafrahmen statt Strafmass; Bindungswirkung bei vollstaendiger Belehrung; Belehrungspflicht Abs. 4 und 5. BVerfG 2 BvR 2628/10 vom 19.03.2013 Verfassungskonformitaet. BGH... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
