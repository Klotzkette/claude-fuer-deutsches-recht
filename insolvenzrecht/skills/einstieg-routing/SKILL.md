---
name: einstieg-routing
description: "Führt insolvenzrechtliche Beratung, Vertretung, Verwaltung, Sachbearbeitung und Berichte von einer gemeinsamen Aktenaufnahme zum konkreten Arbeitsprodukt. Wählt passende lokale Fachmodule und übergibt Spezialaufträge mit Belegen an Forderungsanmelder, Insolvenzreifeprüfer oder Planwerkstatt."
---

# Insolvenzrecht: vom Auftrag zum fertigen Arbeitsprodukt

## 1. Zweck und Anwendungsfall

Bearbeite die konkrete Insolvenzfrage bis zur bestellten Bewertung, Anmeldung, Korrespondenz, Verwaltungsentscheidung oder zum Bericht. Dieser Skill ist der gemeinsame Einstieg für allgemeines Insolvenzrecht und die integrierten Fachmodule. Ein Verfahrensbericht braucht eine andere Perspektive als die Abwehr eines Anspruchs gegen einen Gläubiger. Wähle deshalb Rolle und Produkt einmal; übernimm bekannte Tatsachen in jeden anschließenden Arbeitsschritt.

## 2. Eingaben

Lies vorhandene Angaben und Unterlagen zuerst. Übernimm Schuldner und weitere Rechtsträger, Mandantenrolle oder Bestellungsumfang, Aktenzeichen, Verfahrensstand, Stichtag, Empfänger, Frist und gewünschtes Arbeitsprodukt. Bei Verwaltung und Sachbearbeitung den Bestellungsbeschluss und dessen Befugnisse tatsächlich lesen. Bei Berichten zusätzlich Berichtszeitraum, letzten Bericht, Rechnungslegung und Berichtsauftrag abgleichen. Fehlt nur eine entscheidende Angabe, frage nur danach und bearbeite unabhängige Teile weiter.

Ohne Unterlagen und Auftrag frage knapp, welches Ergebnis gebraucht wird, etwa Beratung, Verwaltungsschreiben, Aktenbearbeitung oder Bericht. Dateien ohne Auftrag still sichten und höchstens zwei passende Produkte anbieten. Ein klarer Auftrag führt direkt zur Bearbeitung; die Wahl eines Fachmoduls darf keine erneute Aufnahme auslösen.

## 3. Ablauf und Fachauswahl

### 3.1. Ein gemeinsamer Arbeitsstand

Führe einen Arbeitsstand mit Rolle, Produkt, Rechtsträger, Verfahren, Stichtag, Tatsachen samt Fundstellen, streitigen Angaben, Fristen, offenen entscheidenden Fragen und Entwurfsstand. Eine neue Datei ändert nur betroffene Positionen und Folgerungen; bereits bestätigte Tatsachen nicht erneut abfragen. Bei einem Rollenwechsel benennen, aus wessen Sicht jetzt gearbeitet wird. Parteivortrag nicht als Feststellung des Gerichts oder Verwalters umetikettieren.

### 3.2. Passendes lokales Fachmodul lesen

Die [Fachmodulübersicht](../../references/fachmodule/INDEX.md) erschließt die erhaltenen Fachtexte und Vorlagen. Lies den passenden Modulindex und daraus nur die für den Auftrag benötigten Fachreferenzen. Die folgende Auswahl ist eine Arbeitsanweisung, keine zusätzliche Eingabemaske. Ältere Router in Fachreferenzen starten keinen neuen Dialog; dieser gemeinsame Arbeitsstand geht vor.

| Rolle oder Auftrag | Lokales Modul | Typische vollständige Produkte |
|---|---|---|
| Beratung oder Vertretung von Geschäftsleitung, Schuldner, Gläubiger oder Anfechtungsgegner | [Fachanwaltsmodul](../../references/fachmodule/fachanwalt/INDEX.md) und passende eigene Insolvenzrecht-Skills | Krisenmemo, Stellungnahme, Anspruchsabwehr, Antrag oder Schriftsatz nach Auftrag |
| Insolvenzverwaltung, vorläufige Verwaltung oder Sachwaltung | [Verwaltung](../../references/fachmodule/verwaltung/INDEX.md) | Entscheidung zur Fortführung oder Verwertung, Vertrag, Gläubigerkorrespondenz, Aufgaben- und Fristenstand |
| Operative Sachbearbeitung der Verfahrensakte | [Sachbearbeitung](../../references/fachmodule/sachbearbeitung/INDEX.md) | Beleg- und Forderungsprüfung, Auskunftsschreiben, Sicherheitenzuordnung, Kassenabgleich, Verfahrensfortschreibung |
| Bericht, Schlussrechnung, Abschluss oder Nachtragsverteilung | [Berichte](../../references/fachmodule/berichte/INDEX.md) | Vollständiger Bericht für den bestimmten Adressaten mit abgestimmten Anlagen und offenem Prüfstand |

Die Modulwahl folgt dem Ergebnis, nicht allein der Berufsbezeichnung. Ein Verwalter, der einen Schlussbericht bestellt, erhält das Berichtsmodul; eine Sachbearbeiterin mit Anspruchsprüfung erhält zusätzlich die passende Fachreferenz. Eigene Spezialskills, etwa `opos-titelabgleich-dreiwochen-liquiditaetsbruecke`, `forderungsanmeldung-glaeubiger-174-177-inso` oder die Register-/Grundbuchpfade für ausländische Insolvenzverwalter, bleiben gezielt nutzbar. Keine vollständige Bibliothek ungefragt laden.

### 3.3. Drei eigenständige Spezialwerkzeuge

Für die vollständigen Spezialaufträge bleiben folgende Plugins eigenständig. Eine kurze Vorfrage darf hier beantwortet werden. Wenn der Auftrag den Spezialworkflow verlangt, eine konkrete Übergabe vorbereiten und dort mit demselben Arbeitsstand fortsetzen, soweit das Werkzeug tatsächlich verfügbar ist.

| Spezialauftrag | Eigenständiges Werkzeug | Übergabe und erwarteter Rücklauf |
|---|---|---|
| Forderung anmelden, eingegangene Anmeldung prüfen oder Tabellenstreit vorbereiten | Forderungsanmelder / `insolvenzforderungen-checker` und vorhandene `insolvenzforderungsanmeldungspruefung` | Gläubiger- oder Verwaltungsrolle, Beschluss, Frist, Anspruch, Beträge, Rang, Sicherheiten, Abtretungen, Titel, Belege und bisheriger Tabellenstand; Anmeldung oder Prüfvermerk mit Restfragen zurückführen |
| Zeitpunkt und Umfang der Zahlungsunfähigkeit oder Überschuldung vollständig prüfen | `zahlungsunfaehigkeits-und-ueberschuldungspruefer` | Rechtsträger, Stichtage, Konten, OPOS, Fälligkeiten, Kredit- und Sicherheitenverträge, Prognose, Rangvereinbarungen und Belegkennungen; nachrechenbaren Status und begründeten Befund übernehmen |
| Insolvenzplan oder StaRUG-Restrukturierungsplan ausarbeiten und prüfen | `insolvenzplan-starug-planwerkstatt` | Verfahrensweg, Planauftrag, Beteiligte, Forderungsbestand, Bewertung, Finanzierung, Vergleichsszenario und belegte Annahmen; Plantext, Berechnungen und Vollzugsfragen zurückführen |

Ist das Spezialplugin nicht erreichbar, behaupte keinen Wechsel. Erledige die bereits belegbare Teilaufgabe und liefere das nutzbare Übergabepaket samt präziser offener Spezialfrage. Planvorlagen gehören zur eigenständigen Planwerkstatt; eine bloße Planüberschrift im Verwaltungsmodul ist kein vollständiger Planworkflow.

Anfechtung bleibt als eigener Vertiefungspfad `insolvenzanfechtung` erhalten. Für Verbraucherfälle `verbraucherinsolvenz-schuldenbereinigung`, für tatsächliche US-Verfahren `us-bankruptcy-code` und für Krisenfrüherkennung, Liquiditätsplanung, Fortbestehensprognose oder Zwangsverwaltung die jeweils einschlägigen Spezialwerkzeuge verwenden. Eine Anerkennungs- oder Grundbuchfrage zum ausländischen Verwalter bleibt im vorhandenen Insolvenzrecht-Spezialpfad; nicht allein wegen Auslandsbezug den gesamten Auftrag umleiten.

### 3.4. Befund, Zahlen und Fristen sichern

Trenne Insolvenzreife, Antragspflicht, einzelne Zahlungen, Forderungsprüfung und Anfechtung. Nach § 15a Absatz 1 InsO ist ein erforderlicher Antrag ohne schuldhaftes Zögern zu stellen; drei beziehungsweise sechs Wochen sind Höchstfristen. Gerichtliche Anmeldefrist nach § 28 Absatz 1 InsO, Prüfung und Verteilung gesondert erfassen. Eine rechtliche Bewertung ermächtigt nicht zu einer Zahlung oder Einreichung.

Bei Statusrechnungen Stichtag, Prognosezeitraum und tatsächlichen Verlauf auseinanderhalten. Die vorhandenen amtlichen Entscheidungsanker zur Nennwertberücksichtigung von Titeln, zur Dreiwochenrechnung und zu tatsächlichen Drittmitteln nur im jeweiligen Aussagebereich nutzen. Bei Berichten Anfangsbestand, Bewegungen und Endbestand gegen die Belege abstimmen; frühere Berichte sind Vergleichsgrundlagen, keine automatisch richtigen Tatsachenquellen.

## 4. Quellenpflicht

Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln. Für tragende Aussagen die konkrete Normfassung und den amtlichen Entscheidungstext prüfen; ältere Fachreferenzen sind Recherchehilfen. Die Konsolidierung ist keine erneute Vollprüfung aller übernommenen Rechtsprechungsanker. Keine Literaturfundstelle ohne Nutzerquelle oder verifizierten lizenzierten Zugriff. Fehlenden Zugriff und offene Aussagegrenzen im internen Vermerk dokumentieren.

## 5. Ausgabeformat

Liefere das bestellte Endprodukt in vollständigen, ausformulierten Sätzen. Tabellen und Visualisierungen erklären die Belege und ergänzen den fertigen Text; ein Aufgabenplan oder eine reine Quellenliste ersetzt keinen bestellten Bericht, Brief oder Schriftsatz. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Ohne Exportfunktion vollständigen Text und getrennten Exporthinweis ausgeben. Empfänger, Anlagen, Beträge, Fristen und Unterschriftsrolle vor Abschluss abgleichen.

Nach neuen Angaben denselben Entwurf fortschreiben, betroffene Berechnungen erneut prüfen und wesentliche Ergebnisänderungen erklären. Nur tatsächlich vorhandene Anlagen als beigefügt bezeichnen. Keine Außenhandlung, Speicherung oder erfolgreiche Übermittlung behaupten, die nicht stattgefunden hat; erforderliche Freigaben getrennt von der vollständigen Entwurfsarbeit behandeln.

## 6. Beispiele

Ein Gläubiger lädt ein Rückforderungsschreiben und Ratenabreden hoch: Rolle aus den Unterlagen übernehmen, Zahlungen einzeln zuordnen und eine belegte Erwiderung mit Anfechtungsvertiefung erstellen. Dafür keinen neuen Sanierungsintake beginnen.

Eine Sachbearbeiterin reicht Konten, Bestellungsbeschluss und Verwertungsliste für den Zwischenbericht ein: Sachbearbeitungsstand und Befugnisse prüfen, Kasse abstimmen und das Berichtsmodul für den ausformulierten Bericht verwenden. Fehlt nur der Erlösbeleg einer Maschine, den konkreten Betrag offenlassen und den übrigen Bericht fertigstellen.

Eine Geschäftsleitung fragt nach dem Zeitpunkt der Insolvenzreife: den eigenen Status-Skill für eine begrenzte OPOS-Frage nutzen; für die vollständige historische Prüfung das bestehende Belegpaket an den eigenständigen Insolvenzreifeprüfer übergeben. Ein Statusbefund ersetzt keinen gesonderten Antragspflicht- oder Organhaftungsbefund.

<!-- BEGIN werkstatt-visualisierung -->
## 7. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Insolvenz- und Sanierungsrecht:** Welche belegten Beträge tragen das Ergebnis und welche Annahme verändert es?

**Erste Ansicht:** Zeige Ausgangswerte, Zu- und Abgänge oder Forderungsbestand in einer nachvollziehbaren Tabelle und bei Zeitreihen als Verlauf. Trenne Stichtag, Zeitraum, Fälligkeit und tatsächlichen Geldfluss.

**Sinnvolle Interaktion:** Erlaube bei geeigneter Oberfläche einen Stichtags- oder Szenariowechsel. Nur belegte oder ausdrücklich angenommene Positionen lassen sich ein- oder ausblenden; Rechenergebnis und Begründung zeigen gemeinsam die Differenz zum Ausgangsstand.

**Datengrundlage:** Betrag, Währung, Vorzeichen, Datum, Zuordnungsgrund, Berechnungsregel und Originalfundstelle. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** nachrechenbare Berechnung mit begründetem Befund und dem bestellten Bericht oder Anspruchsschreiben. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
