---
name: workflow-kaltstart-und-routing
description: "Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: mandantenanfragen-assistent."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill prüft eingehende Mandantenanfragen binnen Minuten auf Eilbedarf, Konflikt, Mandatsfähigkeit und beste Antwortroute. Er ist das Türschloss der Kanzlei und reduziert späteren Korrekturaufwand.

## Erste 4-Minuten-Triage
1. **Eingangsdatum, Frist?** Klagefrist (Kündigungsschutz § 4 KSchG: 3 Wochen), Widerspruch (1 Monat § 70 VwGO / § 84 SGG), Einspruch Mahnbescheid (2 Wochen § 694 ZPO), Strafbefehl (2 Wochen § 410 StPO).
2. **Konfliktcheck (§ 43a Abs. 4 BRAO):** Mandant gegen aktuellen oder früheren Mandanten? Datenbank konsultieren.
3. **Zuständigkeit:** Eigenes Fachgebiet? Sonst Verweisung an Kollegen oder Rechtsanwaltskammer (§ 49 BRAO Hinweispflicht).
4. **Beratungsstufe:** Vorprüfung (kostenlos), Erstberatung (§ 34 RVG: max. 190 EUR netto Verbraucher), Folge-Mandat mit RVG / Honorarvereinbarung (§ 3a RVG schriftlich/Textform).

## Routing-Optionen
- **Eilig + zuständig:** sofort Mandatsannahme in Textform; Vorbestätigung Eingang; parallel inhaltliche Klärung.
- **Eilig + nicht zuständig:** Hinweis und sofortige Verweisung; ggf. interim Notmaßnahme dokumentieren.
- **Nicht eilig + zuständig:** Erstberatungsangebot mit Kostenhinweis (§ 49b Abs. 5 BRAO Pflicht zur Kostenaufklärung).
- **Beratungshilfeberechtigt:** Hinweis auf Beratungshilfeschein des AG (BerHG).

## Anti-Muster
- Mandatsannahme ohne Vergütungsregelung -> Honorarstreit.
- Ad-hoc-Rechtsauskunft per E-Mail ohne Mandatsverhältnis -> Haftungsrisiko (§ 280 BGB i. V. m. Auskunftsvertrag).

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Juristische Methodik und Arbeitstechnik:** Welche Quelle trägt welche Aussage und wo beginnt eine eigene Folgerung?

**Erste Ansicht:** Zeige eine Quellenkarte mit Originalaussage, genauer Fundstelle, zeitlichem und sachlichem Kontext sowie abgeleiteter Aussage. Eine Rezeptions- oder Argumentationslinie braucht belegte Verbindungen.

**Sinnvolle Interaktion:** Eine Auswahl kann Originaltext, Übersetzung und eigene Einordnung gegenüberstellen. Nicht verifizierte Zitate bleiben offen; weder fehlende Textstellen noch historische Übergänge ergänzen.

**Datengrundlage:** Quelle, Fassung, Datum, genaue Textstelle, Aussage, Übertragungsschritt und Aussagegrenze. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** quellengebundene Analyse, Überprüfung oder ausformulierter Argumentationsabschnitt. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
