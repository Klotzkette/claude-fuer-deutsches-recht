---
name: kaltstart-triage
description: "Dokumentengetriebene Ersttriage einer Forderungsakte: wertet zuerst Ordner, ZIP, Rechnungen, Mahnungen, Kontoauszuege, Mahnbescheid, Widerspruch oder Klageentwurf aus, bildet eine Aktenhypothese und fragt danach nur echte Luecken ab. Pinpoints ZPO 253/688 ff.; BGB 271/286/288/362/195/199; GVG 23/71."
---

# Kaltstart-Triage Forderungssache

Eingangsroutine für jede neue Forderungsakte. Ziel ist nicht ein Formularinterview, sondern eine belastbare Aktenhypothese mit moeglichst wenigen Rueckfragen.

## Grundsatz: Akte zuerst, Fragen danach

Wenn ein Ordner, eine ZIP-Datei oder mehrere Dokumente vorhanden sind, wird zuerst `aktenordner-schnellstart` ausgefuehrt. Aus Dateinamen, Briefkoepfen, Vollmacht, Rechnung, Mahnung, Kontoauszug, Mahnbescheid, Widerspruch, Klageentwurf und gerichtlichen Schreiben werden Mandant, Gegner, Forderungsart, Betrag, Zahlungslage, Mahnstand und Fristen rekonstruiert.

Der erste Output lautet nicht "Bitte beantworten Sie sieben Fragen", sondern:

```text
Ich sehe in der Akte vorlaeufig Folgendes:
- mutmasslicher Mandant:
- mutmasslicher Schuldner:
- Forderung / Restforderung:
- Stand Mahnung, Mahnbescheid, Klage oder Vollstreckung:
- auffaellige Risiken:
Ich frage jetzt nur noch die Punkte ab, die aus den Unterlagen nicht sicher folgen.
```

## Nur noch echte Luecken fragen

| Luecke | Frage | Nur stellen, wenn |
|---|---|---|
| Rolle unklar | "Ich vermute, du bist auf Seite [Gläubiger/Schuldner]. Stimmt das?" | Vollmacht, Briefkopf oder Anschreiben widerspruechlich |
| Ziel unklar | "Soll ich eintreiben, abwehren, vergleichen oder nur sortieren?" | kein Mandatsziel aus Mail/Anschreiben erkennbar |
| Frist unklar | "Gibt es eine Frist ausserhalb der Akte?" | gerichtliche Frist oder Verjaehrungsdruck nicht sicher |
| Zahlung unklar | "Ist nach dem letzten Kontoauszug noch etwas bezahlt worden?" | Kontoauszug endet vor aktueller Aktenlage |
| Gegner unklar | "Ist diese Anschrift noch aktuell?" | Zustellung, Umzug, HR-Auszug oder Insolvenzfund unsicher |

Mehr als drei Startfragen sind nur erlaubt, wenn Fristversaeumnis oder falsche Partei droht.

## Routing in drei Spuren

| Befund | Spur | Folgeskill |
|---|---|---|
| Akte ungeordnet oder Dokumentenlage unklar | Akteninventar | aktenordner-schnellstart oder dokumente-intake |
| Forderung schluessig, faellig, Schuldner bekannt, kein ernstliches Bestreiten | Mahnbescheid | mahnbescheid-online |
| Bestreiten wahrscheinlich oder Anspruch muss begruendet werden | Zahlungsklage | zahlungsklage-erstellen |
| Hauptforderung bezahlt, nur Kosten/Zinsen offen | Klageblocker | klagefreigabe-belegte-forderung |
| Forderung wackelig, Belege unklar, Vergleich wirtschaftlich sinnvoll | aussergerichtliche Mahnung oder Vergleich | mahnung-aussergerichtlich-stufenmodell |
| Titel liegt bereits vor | Vollstreckung | zwangsvollstreckung-überblick |

## Risikoampel Erstbewertung

| Ampel | Auslöser |
|---|---|
| gruen | Forderung dokumentiert Schuldner solvent Verjährung in weiter Ferne Zustellung gesichert |
| gelb | Belege luckenhaft Verjährung im laufenden Jahr Schuldner zahlungssaeumig |
| rot | Verjährung tritt in den naechsten sechzig Tagen ein Schuldner verzogen oder insolvent Belegstand schwach |

Rote Ampel triggert sofort Skill verjaehrung-prüfen und gegebenenfalls Mahnbescheid noch am gleichen Werktag.

## Startprodukt

Die Triage endet immer mit einem knappen Arbeitsplan:

| Punkt | Inhalt |
|---|---|
| Aktenbefund | Was liegt vor, was fehlt |
| Parteienhypothese | Mandant, Gegner, Vertreter, Anschriften, Beleg |
| Forderungsmatrix | Hauptforderung, Nebenforderung, Zinsen, Zahlungen, Rest |
| Chronologie | Vertrag, Leistung, Rechnung, Mahnung, Zahlung, Verfahren |
| Fristenampel | Verjaehrung, Widerspruch, Einspruch, gerichtliche Verfuegung |
| Naechster Skill | genau ein Hauptskill und maximal zwei Alternativen |

## Norm-Pinpoints

- ZPO 253 Abs. 2 Klage Pflichtbestandteile
- ZPO 688 ff. Mahnverfahren
- ZPO 690 Mahnbescheidsantrag
- ZPO 696 Abgabe nach Widerspruch
- ZPO 699 700 Vollstreckungsbescheid
- BGB 271 Faelligkeit
- BGB 286 Verzug
- BGB 288 Verzugszinsen
- BGB 362 Erfuellung
- BGB 195 199 Verjährung
- GVG 23 Nr. 1 ab 2026 Streitwertgrenze AG zehntausend Euro

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [BGB 286](https://www.gesetze-im-internet.de/bgb/__286.html)
- [BGB 195](https://www.gesetze-im-internet.de/bgb/__195.html)
- [GVG 23](https://www.gesetze-im-internet.de/gvg/__23.html)
