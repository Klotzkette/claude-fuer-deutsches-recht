---
name: workflow-kaltstart-und-routing
description: "Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: europäischem Technikregulierungsrecht."
---

# Kaltstart und Routing

## Aufgabe
Nutze diesen Workflow-Skill für Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.

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

## Routing-Diagnose KI-VO
- **"Wir bauen / entwickeln ein KI-System"** → Anbieterrolle (Art. 3 Nr. 3); weiter zu `rolle-anbieter-pruefen-art-3-nr-3`, dann Risikoklassifizierung.
- **"Wir setzen ein KI-System ein"** → Betreiberrolle (Art. 3 Nr. 4); weiter zu `rolle-betreiber-pruefen-art-3-nr-4`, danach Betreiberpflichten Art. 26.
- **"Wir importieren ein KI-System"** → Importeur (Art. 3 Nr. 6); Pflichten Art. 23.
- **"Bevollmächtigter eines Drittland-Anbieters"** → Art. 22, 25.
- **"Wir nutzen ein Foundation Model / LLM mit allgemeinem Zweck"** → GPAI (Art. 51 ff.); Modell vs. System unterscheiden.

## Routing-Diagnose Mandantenziel
- **Markteintritt / Inverkehrbringen** → Risikoklassifizierung + ggf. Konformitätsbewertung Art. 43 + Doku Anhang IV + CE/EU-DB.
- **Behördenkommunikation / Marktüberwachung** → Art. 70-79; Vorfallmeldung Art. 73.
- **Vertragsverhandlung mit KI-Anbieter** → Anhang-XI/XII-Anforderungen + AVV DSGVO + Berufsrecht (falls relevant).
- **Interne Compliance / Inventar** → ki-governance-Plugin verlinken.

## Trade-off
Schnelle Erstindikation gegen tiefere Subsumtion: erste Routing-Antwort sollte 1-2 Spezialskills mit Begründung benennen, nicht alle möglichen Wege auflisten. Bei Zweifel: konservativ einstufen und Anhang-III-Prüfung als Erstanker.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Europäische Technikregulierung:** Welcher Produkt-, System- oder Lieferstand ist betroffen und welche Nachweise tragen seine Verwendung?

**Erste Ansicht:** Zeige die Kette von Produkt und Version über Anforderung und Prüfnachweis bis zur betroffenen Charge, Lieferung oder Nutzung. Kennzeichne offene Befunde und widersprechende Unterlagen einzeln.

**Sinnvolle Interaktion:** Eine Auswahl auf Version, Markt oder Charge zeigt nur den einschlägigen Nachweisstand. Der Wechsel darf keine Konformität oder Freigabe automatisch erklären; fehlende Nachweise bleiben sichtbar.

**Datengrundlage:** Produkt oder System, Version, Charge, Markt, beteiligte Rolle, Anforderung, Nachweisdatum und Fundstelle. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** belegter Prüfbericht mit konkreter Nachforderung und den beauftragten Maßnahmen- oder Kommunikationstexten. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
