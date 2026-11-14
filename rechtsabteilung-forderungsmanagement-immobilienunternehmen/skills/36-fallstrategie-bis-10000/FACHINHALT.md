---
name: 36-fallstrategie-bis-10000
description: "Strategieentscheidung erst nach Triage für Forderungs- und Vertragsstreitigkeiten an der internen 10000-EUR-Grenze. Nutzen, Risiko, Kulanz, Direktklage, Kündigung, Vergleich oder Eskalation abwägen. Kein Intake- oder Standard-Router. Output Entscheidungsvorlage."
---

# Fallstrategie bis 10.000 EUR

## Zweck und Anwendungsfall

Dieser Skill entscheidet nach abgeschlossener Triage zwischen mehreren wirtschaftlich und rechtlich tragfähigen Vorgehensweisen. Er wird nur geladen, wenn die interne 10.000-EUR-Grenze, Kulanz, Aufwand oder Prozessrisiko eine echte Unternehmensentscheidung erfordern. Intake und Standard-Routing bleiben bei Skills 33 und 06.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Fallakte mit Streitwert oder vorläufigem Forderungsvolumen.
- Ziel: Zahlung, Räumung, Mieterhöhung, Verteidigung oder Vergleich.
- Hinweise zu Komplexität und Gegenwehr.

## Ablauf / Checkliste

1. Streitwert und internes Forderungsvolumen bestimmen.
2. Gesetzliche Zuständigkeit und Anwaltszwang nach Skill 22 prüfen: Wohnraummietsachen sind nach Paragraf 23 Nr. 2a GVG streitwertunabhängig Amtsgerichtssachen ohne Anwaltszwang (Paragraf 78 ZPO i. V. m. Paragraf 79 ZPO). Auch bei Streitwerten weit über 10.000 EUR kann die Konzerngesellschaft sich dort bei erfülltem Paragrafen 79 ZPO durch Beschäftigte vertreten lassen. Bei Geschäftsraummiete gilt die Sonderzuweisung nicht; bis einschließlich 10.000 EUR ist grundsätzlich das Amtsgericht, darüber grundsätzlich das Landgericht zuständig.
3. Interne 10.000-EUR-Grenze als reines Bearbeitungs- und Freigabekriterium anwenden. Diese Grenze hat nichts mit der gesetzlichen Zuständigkeit oder dem Anwaltszwang zu tun: Sie ist nur die interne Schwelle, ab der die Bereichsleitung freigeben oder an die Stammkanzlei eskaliert werden muss.
4. Gegenwehr, Beweisrisiken, Gutachterbedarf und Öffentlichkeitsrisiko bewerten.
5. Nächste Arbeitsaktion bestimmen und den Folgeskill nur intern routen.
6. Skill `06-fallziel-renofa-triage` bleibt Pflicht-Vorfilter: Skill 36 darf nur final routen, wenn Rolle, RDG-Grenze, Streitwert, interne Freigabe und Eskalationslage dokumentiert sind.
7. Eskalation an Rechtsanwalt auslösen, wenn rechtlich oder intern erforderlich.
8. Direktklage, Schreiben, Vergleich, Räumung, Mieterhöhung oder Verteidigung als Prozesspfad begründen.
9. Gerichtliches Mahnverfahren nur als ausdrückliche Nebenoption ausweisen; bei klarem Mahnbescheid-, Mahnverfahren- oder Vollstreckungsbescheid-Wording zu Skill `17`, `18` oder `19` routen.
10. Bei Betriebskosten-Nachforderung, Belegeinsicht oder Einwendungsfrist nicht zu Skill `20` springen, sondern zuerst Skill `44-betriebskosten-rueckstand-streit` nutzen.
11. Kosten- und Vollstreckungsstatus sauber trennen: ohne Kostengrundentscheidung kein KFA; mit KFA-Bedarf Skill `46`, mit KFB Skill `47`, mit positivem vollstreckbaren Titel Skill `48`, bei Räumungstitel zusätzlich Skills `25` und `26`, bei laufender Überwachung Skill `50`.
12. Strategiekarte erzeugen: Ziel, Ampel, Aufwand, Risiko, nächster Workflow, benötigte Belege und Entscheidungsvorlage.
13. Nur bei einer echten Unternehmensentscheidung höchstens drei konkrete Ergebnisoptionen mit Betrag, Zeit, Risiko und erforderlicher Freigabe anbieten. Keine Skillnummern zur Auswahl stellen.
14. Jede Strategie endet mit einer klaren Bedienhandlung: Entwurf erstellen, Rückfrage versenden, Frist setzen, Freigabe einholen oder an Skill 08 übergeben.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert.

Gesetzliche Zuständigkeit nie mit interner Bearbeitungsgrenze verwechseln. Normen sauber trennen. Insbesondere: bei Wohnraum entscheidet Paragraf 23 Nr. 2a GVG (immer AG, kein Anwaltszwang am AG), nicht die interne 10.000-EUR-Schwelle. Für Bedienführung und Übergaben `references/bedienfuehrung-workflows.md` nutzen.

## Ausgabeformat

Strategiekarte und Entscheidungsvorlage mit Kurzsachverhalt, Ziel, Streitwert, interner Grenze, Entscheidungsampel, Risiken, höchstens drei echten Ergebnisoptionen und einer nächsten Arbeitsaktion in Klartext. Der Folgeskill bleibt interne Routinginformation.

## Beispiele

- 4.800 EUR Mietrückstand Wohnraum: direkte Zahlungsklage am AG, kein Anwaltszwang, Konzern-Inhouse-Vertretung nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO.
- 11.500 EUR Räumungssache Wohnraum: gesetzlich weiter AG ohne Anwaltszwang (Paragraf 23 Nr. 2a GVG); intern wird die Bereichsleitung freigegeben, weil der Streitwert über der internen 10.000-EUR-Schwelle liegt.
- 18.000 EUR Mietrückstand Geschäftsraum: sachlich LG (Paragraf 71 GVG), Anwaltszwang am LG (Paragraf 78 ZPO); Eskalation an Stammkanzlei nach Skill 08.
