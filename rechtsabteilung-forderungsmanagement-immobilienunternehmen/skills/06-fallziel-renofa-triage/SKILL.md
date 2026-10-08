---
name: 06-fallziel-renofa-triage
description: "Verbindlicher interner Router nach Intake, Fallkarte oder Änderungskarte. Prüft Fallziel, Rolle, RDG, Paragraf 79 ZPO, interne 10000-EUR-Freigabe und Eskalation. Wählt automatisch Zahlung, Kündigung, Räumung, Mieterhöhung, Verteidigung, Kosten oder Vollstreckung und zeigt statt eines Skillmenüs genau eine nächste Arbeitsaktion."
---

# Fallziel und Renofa-Triage

## Zweck und Anwendungsfall

Die bearbeitende Person ist Fachangestellte oder Fachkraft der Immobilien-Rechtsabteilung; eine zusätzliche Qualifikation als Rechtsfachwirtin oder eine Anwaltszulassung wird nicht unterstellt. RDG und ZPO setzen die Grenzen. Dieser Skill ordnet den Vorgang nach dem Intake ein und entscheidet, ob die Abteilung selbst bearbeitet oder eskaliert. Wenn der Nutzer ohne Skillauswahl einen schon klaren Sachverhalt vorgibt, erzeugt dieser Skill sofort die Startkarte und routet weiter.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Fallart (Mietrückstand, Räumung, Mieterhöhung, Verteidigung) und Streitwert.
- Bekannte Komplikationen (Insolvenz, Sachverständigenstreit, Strafrecht, Widerklage).
- Ergebnis des RDG-Grenzen-Checks aus Skill 07.
- Bei laufender Akte: bisheriger Fachpfad, Änderungskarte, neue Frist und überholte Bewertung.

## Ablauf / Checkliste

1. Prüfen, was die Renofa selbst darf: außergerichtliches Forderungsmanagement der beschäftigenden Gesellschaft oder im belegten Konzernverbund; gerichtliches Mahnverfahren nur als optionale Abzweigung nach ausdrücklicher Entscheidung; Parteiprozess am Amtsgericht in Wohnraummietsachen. Vor dem Amtsgericht besteht im ersten Rechtszug nach Paragraf 78 ZPO i. V. m. Paragraf 79 ZPO kein Anwaltszwang; die Konzerngesellschaft kann sich nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO durch Beschäftigte der Partei oder eines verbundenen Unternehmens vertreten lassen. Beschäftigtenstatus, Verbund, Vollmacht und interne Freigabe sind zu belegen. Bei Wohnraummietsachen ist das AG nach Paragraf 23 Nr. 2a GVG streitwertunabhängig zuständig; auch ein Mietrückstand über 10.000 EUR bleibt damit gesetzlich im Parteiprozess (die interne 10.000-EUR-Grenze ist eine reine Freigabeschwelle, kein Anwaltszwang). Details siehe Skills 07 und 22.
2. Prüfen, was die Renofa nicht ohne gesonderte Befugnis oder Eskalation betreibt: Landgericht (dort gilt Anwaltszwang nach Paragraf 78 Abs. 1 S. 1 ZPO, insbesondere bei Geschäftsraummiete über 10.000 EUR Streitwert); Berufung und Revision; BGH-Sachen; strafrechtliche Komponente; Insolvenzverfahren des Mieters; komplexe Streitsachen mit Sachverständigem. Beschwerden nicht pauschal dem Anwaltszwang zuordnen, sondern Statthaftigkeit, Ausgangsgericht und Vertretungsregel des konkreten Rechtsbehelfs prüfen.
3. Die Forderungsart der Rollengrenze zuordnen:

| Forderung | Sachlich | Anwaltszwang | Renofa selbst |
|---|---|---|---|
| Mietrückstand Wohnraum, jeder Streitwert | AG (Paragraf 23 Nr. 2a GVG) | nein (Paragraf 78 ZPO) | ja |
| Räumungsklage Wohnraum | AG (Paragraf 23 Nr. 2a GVG) | nein | ja |
| Verbundene Zahlungs- und Räumungsklage Wohnraum | AG (Paragraf 23 Nr. 2a GVG) | nein | ja |
| Mieterhöhungs-Zustimmungsklage Wohnraum | AG (Paragraf 23 Nr. 2a GVG) | nein | ja |
| Geschäftsraum bis einschließlich 10.000 EUR | AG (Paragraf 23 Nr. 1 GVG) | nein | ja (interne Freigabe) |
| Geschäftsraum über 10.000 EUR | LG (Paragraf 71 GVG) | ja (Paragraf 78 ZPO) | nein, Eskalation |
| Berufung gegen AG-Urteil | LG | ja | nein, Eskalation |

4. Entscheidungsampel setzen:

| Status | Bedeutung |
|---|---|
| Grün | eigene Bearbeitung möglich, nächster Skill benannt |
| Gelb | eigene Bearbeitung nur nach Freigabe oder Belegnachlieferung |
| Rot | Eskalation an Rechtsanwalt, Stammkanzlei oder Abteilungsleitung |

5. Bei laufender Akte nur das Delta neu triagieren. Den bisherigen Fachpfad beibehalten, solange neue Zahlung, Frist, Einwendung, Titel- oder Rollengrenze keinen Pfadwechsel erzwingt.
6. Startkarte oder Änderungskarte ausgeben: Fallart, Ampel, kurzer Grund, fehlende Kernstücke, Frist und genau eine nächste Arbeitsaktion in Klartext. Den Folgeskill intern wählen; Nutzer müssen weder Skillnummern kennen noch einen Skill auswählen. Nur wenn zwei fachlich gleich tragfähige Ziele von einer echten Unternehmensentscheidung abhängen, ein Menü mit höchstens drei konkreten Rechtsfolgen anbieten.
7. Rückfragen begrenzen: maximal drei Fragen, jeweils mit Grund und Folge. Bei gelber Ampel vorläufig weiterarbeiten; bei roter Ampel stoppen und Eskalation formulieren.
8. Für Bedienführung und Übergaben `references/bedienfuehrung-workflows.md` nutzen.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen.

## Ausgabeformat

Startkarte oder Änderungskarte, Routing-Entscheidung Renofa ja oder nein, beibehaltener oder geänderter Fachpfad, Entscheidungsampel, Begründung, Eskalations-Trigger, höchstens drei Rückfragen und nächste Arbeitsaktion in Klartext. Die technische Skill-ID darf nur als interne Übergabe ergänzt werden und wird nicht zur Nutzerentscheidung gemacht. Die Entscheidung wird in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Reiner Wohnraum-Mietrückstand von 6.200 EUR: grüne Ampel, eigene Bearbeitung, Verweis auf den Zahlungsklage-Skill.
- Der Mieter kündigt Berufung an: rote Ampel, Eskalation an die Stammkanzlei nach Skill 08.
