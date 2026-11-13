---
name: kommandocenter
description: "Für Zwangsvollstreckung – Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Zwangsvollstreckung – Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Liegen alle drei Säulen vor: Titel (§ 704 ZPO), Klausel (§ 724 ZPO), Zustellung (§ 750 ZPO)?
2. Welches Vollstreckungsziel wird verfolgt (Geld, Räumung, Herausgabe, Handlung)?
3. Sind Vermögenswerte bekannt (Konto, Arbeitgeber, Grundbesitz)?
4. Ist der Schuldner in Insolvenz — § 89 InsO Vollstreckungsverbot prüfen?

## Zentrale Normen

- § 704 ZPO — Vollstreckungstitel
- § 724 ZPO — vollstreckbare Ausfertigung (Klausel)
- § 750 ZPO — Zustellung als Vollstreckungsvoraussetzung
- § 802a ZPO — Aufgaben des Gerichtsvollziehers
- § 829 ZPO — Pfändungs- und Überweisungsbeschluss (Forderungspfändung)
- § 89 InsO — Vollstreckungsverbot nach Insolvenzeröffnung

## Eingaben

1. **Titelart**: Urteil (rechtskräftig oder vorläufig vollstreckbar), Vollstreckungsbescheid, gerichtlicher oder notarieller Vergleich, notarielle Urkunde mit Unterwerfung (§ 794 Abs. 1 Nr. 5 ZPO), vollstreckbare Ausfertigung des Tabellenauszugs (§ 201 InsO), Kostenfestsetzungsbeschluss.
2. **Vollstreckungsziel**: Geld, Räumung, Herausgabe, Handlung, Unterlassung.
3. **Schuldnersituation**: Privatperson, Selbstständige, Unternehmen, Insolvenz, Verbraucherinsolvenz, P-Konto bekannt.
4. **Bekannte Vermögenswerte**: Bankkonten, Arbeitgeber, Grundbesitz, Kfz, Forderungen gegen Dritte.
5. **Bisherige Vollstreckungsversuche**: erfolglos, Vermögensauskunft schon abgegeben, Sperrfrist § 802d ZPO.

## Drei-Säulen-Prüfung vor jedem Vollstreckungsschritt

Niemand darf vollstrecken, ohne **alle drei** Säulen geprüft zu haben:

1. **Titel** § 704 ZPO – formgerechte Ausfertigung vorhanden.
2. **Klausel** § 724 ZPO – vollstreckbare Ausfertigung mit Klauselvermerk (Ausnahme: Vollstreckungsbescheid, der die Klausel von Gesetzes wegen trägt § 796 Abs. 1 ZPO; Tabellenauszug § 201 Abs. 2 InsO).
3. **Zustellung** § 750 ZPO – Titel mit Klausel ist dem Schuldner vor der Vollstreckung zugestellt worden (Wartefrist 2 Wochen für Klauselzustellung bei Klauseln nach §§ 726 ff. ZPO).

Wenn auch nur eine Säule fehlt: **STOPP**. Der Skill bricht die Vollstreckung ab und ruft `titel-klausel-zustellung`.

## Routing-Tabelle

| Wenn vorhanden / gewünscht | Lade Skill |
| --- | --- |
| Forderung noch ohne Titel | `forderungsmanagement-klagewerkstatt/inkasso-zahlungsklage-ersteller` (anderes Plugin) |
| Antrag auf Mahnbescheid | `mahnbescheid-online-mobiliar-gv` |
| Mahnbescheid liegt vor, kein Widerspruch | `vollstreckungsbescheid-zv` |
| Vollstreckungsbescheid in Hand, Konto bekannt | `pfueb-bank` |
| Lohnforderung gepfändet werden soll | `pfueb-arbeitsentgelt` |
| Forderung gegen Mieter, Finanzamt, Krankenkasse | `pfueb-802l-arbeit` |
| Kein Vermögen bekannt | `vermoegensauskunft-gv` oder `kontensuche-drittschuldner` |
| Notarielle Urkunde mit Grundschuld vorhanden | `notarielle-urkunde-grundschuld` |
| Vollstreckung in Immobilie | `zvg-antrag-glaeubiger` |
| Tabellenauszug aus aufgehobenem oder beendetem Insolvenzverfahren | `tabellenauszug-201-inso` |
| Mobile Pfändung vor Ort | `mobiliar-gv-auftrag` |
| Räumung von Wohn- oder Geschäftsraum | `raeumung-tabellenauszug-inso` |
| Schuldnerseite: Vollstreckung wehren | `abwehr-schuldner` |
| Pfändungsfreigrenze berechnen | `pfaendungstabelle-pfueb-arbeitsentgelt` |

## Reform-Stand 2026/2027 (ZVollstrDigitG)

Das Gesetz zur weiteren Digitalisierung der Zwangsvollstreckung (BGBl. 2026 I Nr. 152; BT-Drs. 21/4816) bringt für die Praxis vier zentrale Änderungen, die der Skill bei jeder Beratung mitberücksichtigt:

1. **Elektronischer PfÜB-Antrag**: ab 1.10.2026 nach Paragraf 829a ZPO n.F. mit elektronischen Kopien von Titel, Klausel und Zustellungsnachweis.
2. **Strukturierter Datensatz**: ab 1.1.2027 XML-Datensatz nach Paragraf 829 Absatz 5 ZPO n.F. möglich; bei Widerspruch zwischen PDF und XML ist XML maßgeblich.
3. **Pflicht für Kreditinstitute**: ab 1.6.2027 müssen Banken einen sicheren elektronischen Übermittlungsweg eröffnen nach Paragraf 173 Absatz 2 Nummer 1 ZPO n.F.; vorher freiwillig.
4. **Paragraf 840 ZPO Drittschuldnererklärung**: Postzustellung zusätzlich zur Gerichtsvollzieherzustellung und elektronischen Zustellung.

Das Gesetz vom 20. Mai 2026 wurde am 26. Mai 2026 im BGBl. 2026 I Nr. 152 verkündet. Für operative Details `elektronische-zustellung-eu` und `pfueb-bank` nutzen.

## Qualitätsgates

- Niemals Folge-Skill laden, wenn eine der drei Säulen rot ist.
- Niemals Mobiliar- oder Forderungspfändung empfehlen, wenn Schuldner in Insolvenz – dann § 89 InsO Vollstreckungsverbot greift.
- Niemals Sperrfrist § 802d ZPO (zwei Jahre Vermögensauskunft) ignorieren.
- Bei einer natürlichen Person die seit 1. Juli 2026 geltende Pfändungstabelle, gesetzliche Unterhaltspflichten und gerichtliche Abweichungen erfassen; P-Konto-Schutz getrennt nach Paragrafen 899 ff. ZPO prüfen.

## Arbeitsstil

Disziplinarisch, klar, ohne juristisches Wortgeklingel. Wenn Säulen wackeln, ist das die einzige Botschaft. Wenn der Schuldner offensichtlich vermögenslos ist, sagt der Skill das frühzeitig und schickt nicht in eine teure Mobiliarvollstreckung.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Zwangsvollstreckung:** Welche Verfahrensfrage ist jetzt entscheidungsreif und welcher Beleg fehlt für die nächste Handlung?

**Erste Ansicht:** Zeige Verfahrensstand und Frist als kurze Zeitachse; ordne Streitpunkte in einer Tabelle nach Vortrag, Gegenposition, Beleg, Rechtsmaßstab und nächstem Arbeitsschritt.

**Sinnvolle Interaktion:** Eine Auswahl eines Streitpunkts zeigt die tragenden Belegstellen und den zugehörigen Entwurfsabschnitt. Alternative Tatsachenannahmen bleiben getrennt; ein Klick entscheidet keine streitige Rechtsfrage.

**Datengrundlage:** Verfahrensrolle, Antrag oder Ziel, Ereignis und Zugang, streitige Tatsache, Beleg, Rechtsquelle und offener Punkt. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** das verlangte ausformulierte Schreiben, der Schriftsatz, Bescheid, Entscheidungsentwurf oder Vermerk. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
