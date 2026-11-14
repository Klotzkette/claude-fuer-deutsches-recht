---
name: sozialrecht-fallaufnahme-routing
description: "Für Master-Routing-Skill der sozialrechtlichen Kanzlei: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# 1. Sozialrechtlichen Fall bearbeiten

## 1.1. Zweck

Ordne einen sozialrechtlichen Auftrag anhand von Bescheid, Leistungsziel und Verfahrensstand ein. Führe die nötigen Fachprüfungen durch und erstelle das bestellte Dokument; eine Liste von Skills ist kein Ersatz dafür.

## 1.2. Akte und offene Angaben

Lies vorhandene Anfragen, Bescheide, Zugangsnachweise, Widersprüche und gerichtliche Schreiben. Ermittle betroffene Person, Leistungsträger, Zeitraum und gewünschtes Ergebnis daraus. Bei mehreren Familienmitgliedern trenne Ansprüche und Fristen; frage bekannte Angaben nicht erneut ab.

Fehlen der tatsächliche Zugang, die angegriffene Regelung oder das Ziel, kläre nur diese offenen Punkte. Bei akuter Existenznot, dringendem Hilfsmittelbedarf oder ausfallender Pflege beziehungsweise Schulbegleitung benenne die konkrete drohende Folge und die erreichbaren Belege. Eile bestimmt die Reihenfolge, beendet aber nicht die Bearbeitung.

## 1.3. Fachlicher Ablauf

### 1.3.1. Frist und Verfahren bestimmen

Prüfe Bekanntgabe und Belehrung, Widerspruch nach Paragraf 84 SGG, Klage nach Paragraf 87 SGG sowie aufschiebende Wirkung und Eilrechtsschutz nach Paragrafen 86a und 86b SGG. Nicht allein aus dem Bescheiddatum rechnen. Der optionale Skill `bescheid-frist-quick-check` kann unterstützen.

Bei möglicher Fristversäumung Grund, Dauer und Wegfall des Hindernisses klären und die Voraussetzungen von Paragraf 67 SGG prüfen. Keine starre Zweiwochenweiche zwischen Wiedereinsetzung und Überprüfungsantrag verwenden: Die Wiedereinsetzungsfrist knüpft an den Wegfall des Hindernisses an. Einen Überprüfungsantrag nach Paragraf 44 SGB X gesondert auf Anwendungsbereich, Voraussetzungen und Nutzen prüfen, nicht automatisch als Ersatz für einen Rechtsbehelf.

### 1.3.2. Passende Fachprüfung wählen

- Grundsicherung: Nach Paragrafen 19 ff. SGB II streitige Monate, Haushalt, Bedarf und Zuflüsse abgleichen; optional `sgb-ii-bescheid`.
- Hilfsmittel: Funktionsbedarf, vorhandene Versorgung und Ablehnungsgrund nach Paragraf 33 SGB V sowie gegebenenfalls Paragrafen 47 ff. SGB IX prüfen; optional `hilfsmittelantrag-pruefen`.
- Schulbegleitung: konkreten Unterstützungsbedarf, Stundenumfang und Trägerzuständigkeit nach Paragrafen 90 ff. SGB IX beziehungsweise Paragraf 35a SGB VIII abgrenzen; optional `eingliederungshilfe-schule`.
- Pflegegrad: Alltagshilfe und Modulbewertungen nach Paragrafen 14 und 15 SGB XI gegenüberstellen; optional `pflegegrad-widerspruch`.
- Erwerbsminderungsrente: Leistungsbild, Eintrittszeitpunkt und Versicherungszeiten nach Paragrafen 43 und 240 SGB VI prüfen; optional `erwerbsminderungsrente`.
- Schwerbehinderung: Funktionsbeeinträchtigungen und Bewertung nach Paragraf 152 SGB IX und VersMedV prüfen; optional `gdb-schwerbehinderung`.
- Asylbewerberleistungen: konkrete Regelung nach Paragrafen 1a bis 3 AsylbLG und Bescheidgrundlage prüfen; keine automatische Übernahme des SGB-II-Maßstabs.

Medizinische Fragen, wirtschaftliche Voraussetzungen und Statusfragen getrennt bearbeiten. Bei Versicherungsstatus die tatsächliche Eingliederung, Weisungen, Rechtsmacht und das Unternehmerrisiko prüfen, nicht bloß den Vertragstitel.

### 1.3.3. Nachfordern und fortsetzen

Fehlt ein Modulbogen im Pflegegutachten, frage genau danach und vergleiche nach Eingang die streitige Alltagshilfe mit der Bewertung. Fehlt bei Grundsicherung ein Zuflussnachweis, kläre Zahlungsdatum und Zweck und rechne den betroffenen Monat neu. Bei Erwerbsminderung einen Widerspruch zwischen Befund und Stundenangabe durch konkrete medizinische Fragen klären, nicht durch eine eigene Diagnose.

Arbeite neue Antworten in Rechnung, Beweiswürdigung und den bestellten Text ein. Eine weitere entscheidende Lücke rechtfertigt eine kurze Anschlussfrage, aber keine erneute Gesamtaufnahme. Amtsermittlung ersetzt weder die Unterscheidung zwischen Angabe und Nachweis noch die Prüfung verbleibender Nichterweislichkeit.

### 1.3.4. Begleitende Aufgaben auswählen

Akteneinsicht für fehlende entscheidende Bestandteile vorbereiten, nicht automatisch erneut bei bereits vollständiger Akte. PKH und Beratungshilfe nur bei entsprechendem Bedarf und Auftrag prüfen. Anlagen nach tatsächlichen Belegbezügen ordnen; die bloße Zahl der Dateien löst kein eigenes Verfahren aus. Bei Verständnisschwierigkeiten den Mandantenbrief sprachlich anpassen, ohne rechtliche Voraussetzungen wegzulassen.

## 1.4. Quellen

Normen und tragende Entscheidungen anhand zugänglicher Quellen prüfen; Entscheidungen mit Gericht, Form, Datum, Aktenzeichen und einschlägiger Passage angeben. Amtlicher Bezug für die Wiedereinsetzung: [Paragraf 67 SGG](https://www.gesetze-im-internet.de/sgg/__67.html). Unverifizierte Fundstellen und Literatur aus Modellwissen nicht übernehmen.

## 1.5. Ergebnis und Endkontrolle

Liefere den bestellten Brief, Antrag oder Vermerk unter dem gewünschten Dateinamen. Ohne Dokumentenauftrag erläutere Streitgegenstand, Fristlage, Beweislage und begründete Empfehlung in einem kurzen Vermerk. Interne Bearbeitungsreihenfolgen und Quellenkontrollen sind keine Pflichtgliederung des Empfängertextes.

Bei offenen entscheidenden Nachweisen liefere einen erkennbaren Teilstand und setze nach Eingang bis zum bestellten Ergebnis fort. Prüfe vor Abschluss insbesondere richtige Person, Zeitraum, Zuständigkeit, Frist und Einarbeitung neuer Angaben. Versand, Einreichung, Vergleich oder Verzicht nur mit ausdrücklicher Freigabe; eine interne Überarbeitung benötigt keine neue Erlaubnis.

Vollständige Sätze, keine Stichwortskelette; ausschließlich dezimale Gliederung. Formatierte Dokumente verwenden Times New Roman 11 pt, sonst Exporthinweis. Ohne Zugriff oder Export liefere den bearbeitbaren Text und benenne die konkreten Einschränkungen getrennt vom Mandantenbrief, ohne erfolgreiche Datei- oder Quellenprüfung vorzutäuschen.

## 1.6. Beispiel

Für ein Kind ist Schulbegleitung ab Schuljahresbeginn streitig, während bei einem Elternteil ein Pflegegradverfahren läuft. Ordne Unterlagen und Fristen getrennt zu. Fehlt für die Schulbegleitung die Beschreibung der konkreten Unterstützungssituationen, frage sie nach und vervollständige anschließend den dafür bestellten Entwurf; der Pflegefall wird dadurch nicht ungefragt zum zweiten Dokumentenauftrag.
