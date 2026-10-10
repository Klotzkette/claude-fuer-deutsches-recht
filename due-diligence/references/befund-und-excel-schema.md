# 1. Befundregister und Excel-Auswertung

Das Arbeitsbuch soll eine konkrete Entscheidung erklären. Es ist weder eine Sammlung leerer Kontrollblätter noch ein automatisches Rechtsurteil. Der Aufbau richtet sich nach den tatsächlich beauftragten Bereichen. Eingaben, Berechnungen und Ergebnisse bleiben nachvollziehbar; unbekannte Daten werden nicht als null gerechnet.

## 1.1. Stabile Kennungen

Verwenden Sie `D-0001` für Quellen, `B-0001` für Befunde, `Q-0001` für Rückfragen und bestehende Personal- oder Darlehensnummern für Datensätze. Eine Kennung bleibt bei Sortierung unverändert. Datensatzkennungen wie `B-0001` sind von Produktkennungen wie `fachbefunde` zu unterscheiden. Die in [Arbeitsweise und Übergaben](arbeitsweise.md) festgelegten Produktkennungen bleiben auch bei abweichenden lesefreundlichen Excel-Blattnamen bestehen. Ein Befund kann mehrere Quellen und Gegenbelege haben. Dokumentdatum, Bereitstellung im Datenraum und Prüfdatum werden getrennt gespeichert; eine verspätete Antwort macht eine frühere Berichtsfassung nicht rückwirkend vollständig. Die referenzierte Quelle wird mit Seite, Vertragsabschnitt oder Tabellenblatt und Zelle konkretisiert; ein bloßer Dateiname genügt bei umfangreichen Unterlagen nicht.

## 1.2. Zweckmäßige Arbeitsblätter

| Blatt | Inhalt | Berechnungen | Grenzen |
| --- | --- | --- | --- |
| Übersicht | Gegenstand, Stichtag, wesentliche Befunde, Entscheidungen | Bezug auf ermittelte Ergebnisse | Kein grünes Gesamtsignal für ungeprüfte Bereiche |
| Befunde | Tatsachenkern, Quelle, Gegenbeleg, Rechtsfrage, Folge, Status | Nur echte Zusammenfassungen | Schwere und Belegsicherheit getrennt |
| Rückfragen | Konkrete Frage, benötigter Beleg, Verantwortlicher, Antwort | Offene Fragen nachvollziehbar zählen | Keine Erledigung durch Antwort ohne nötigen Nachweis |
| Personal | ID, Vertragsstand, tatsächliche Bedingungen, Kostenquellen | Belegte Monats- und Jahresüberleitung | Geschäftsführerverträge getrennt |
| Kredite | ID, Hauptforderung, Zinsen, Kosten, Zahlungen, Fälligkeit | Getrennte Salden und Stichtagsrechnung | Buchsaldo ist kein Rechtsanspruch |
| Zahlenüberleitung | Ausgangswert, Korrektur, Kategorie, Annahme, Ergebnis | Transparente Summen und Szenarien | Doppelerfassung verhindern |
| Dokumente | Herkunft, Version, Datum, Fundstelle, Prüfungstiefe | Anzahl und Abdeckung | Gesamt-PDF und Originale nicht doppelt zählen |

Die sichtbare Blattreihenfolge stellt Übersicht und relevante Ergebnisse nach vorn. Größere Quelldaten und Berechnungen können eigene Blätter erhalten. Bei einem kleinen Auftrag genügt eine entsprechend gegliederte Tabelle. Quellen stehen bei den zugehörigen Eingaben, nicht als Dekoration im Titel.

## 1.3. Befundfelder

Jeder wesentliche Befund enthält Kennung, Titel, betroffenen Gegenstand, festgestellte Tatsache, genauer Quellenbezug, Gegenbeleg oder Lücke, maßgebliche Rechtsfrage, geprüfte Grundlage, Rechtsstand, wirtschaftliche Bedeutung, Schätzannahmen, vorgeschlagene Maßnahme, Zuständigkeit, Nachforderung und Status. Bei Verweisen auf Entscheidungen wird erläutert, was die Entscheidung trägt und was sie nicht trägt. Fehlende Felder werden kenntlich gemacht, nicht erfunden.

## 1.4. Zahlenfelder und Formeln

Kennzeichnen Sie Währung, Einheit, Stichtag, Vorzeichen und Datenart. Ein Originalbuchwert bleibt erhalten; Korrekturen stehen daneben und bilden mit ihm eine Überleitung. Für eine Forderung werden Hauptforderung, Vertragszinsen, Verzugszinsen, Kosten und Zahlungen getrennt geführt. Die konkrete Anrechnung der Zahlung richtet sich nach der rechtlichen Einordnung; die Formel darf sie nicht aus Bequemlichkeit unterstellen.

Für Portfolioabdeckung werden Anzahl und Volumen getrennt gerechnet. Nenner und Stichtag müssen zur Grundgesamtheit passen. Eine risikoorientierte Auswahl gibt keine statistische Fehlerquote der übrigen Verträge vor. In der Bankakte sind 20 ausführliche Dokumentenfälle und 980 weitere Datenzeilen ausdrücklich unterschiedliche Erkenntnisstände.

Vor Übergabe sind Schlüsselsummen mit einer unabhängigen Rechnung abzugleichen. Testen Sie einen geänderten Eingabewert und seine Auswirkungen sowie leere Werte, doppelte Kennungen und neue Datensätze. Verhindern Sie still abgeschnittene Summenbereiche. Ein Checkfeld beobachtet das Rechenmodell; die eigentlichen Geschäftsrechnungen sollen nicht von einem abschließenden Prüfblatt abhängen.

## 1.5. Nachvollziehbare Ausgabe

Fixieren Sie geeignete Kopfzeilen, setzen Sie Filter und lesbare Zahlenformate und erläutern Sie die editierbaren Eingaben. Prüfen Sie alle verwendeten Tabellenblätter visuell. Text und Zahlen dürfen nicht abgeschnitten werden. Formeltext, ein Vorschaubild und erfolgreicher Export belegen keine Neuberechnung im Zielprogramm; nennen Sie nicht durchgeführte Zielsystemprüfungen ausdrücklich.
