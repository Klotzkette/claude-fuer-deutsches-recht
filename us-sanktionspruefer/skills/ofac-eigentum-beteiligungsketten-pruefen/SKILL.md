---
name: ofac-eigentum-beteiligungsketten-pruefen
description: Prüft die OFAC-Eigentumsregel über mehrere Beteiligungsebenen mit Aggregation blockierter Eigentümer. Trennt Kontrolle und Vertreterhandeln von automatischer Blockierung und erstellt einen belegten Beteiligungsvermerk samt Nachforderung.
---

# 1. Eigentumsketten nach der OFAC-50-Prozent-Regel prüfen

## 1.1. Zweck und Anwendungsfall

Kläre, ob ein nicht selbst gelistetes Unternehmen wegen direkten oder mittelbaren Eigentums blockiert ist. OFAC-FAQ 398 und 401 verlangen mindestens 50 Prozent Eigentum, einzeln oder zusammen bei blockierten Personen. Kontrolle allein löst diese Eigentumsregel nicht aus; andere Blockierungsgrundlagen, Regierungsdefinitionen und das Handeln gelisteter Vertreter bleiben möglich.

## 1.2. Eingaben

Datierte Registerauszüge, Anteilsliste, Beteiligungsverträge, Vollzugsnachweise, Treuhandangaben, Kapitalarten und bekannte amtliche Listungskennungen. Lege Prüfzeitpunkt und betroffenes Geschäft fest. Prozentzahl, Anteilseinheit und Nenner müssen zusammenpassen. Eine Geldwäsche-UBO-Liste mit anderer Erhebungsschwelle ersetzt keine vollständige Eigentumsstruktur.

## 1.3. Ablauf / Checkliste

1. Zeichne Gesellschaften und unmittelbare Anteilseigner als einfache Tabelle oder Baum mit Datum, Quote und Belegstelle. Widersprüchliche Fassungen nicht mitteln. Eigentum und bloße Stimmrechts-/Managementbefugnis getrennt erfassen.
2. Kennzeichne tatsächlich blockierte Eigentümer anhand aktueller beziehungsweise historisch einschlägiger Quellen. Summiere deren unmittelbare Anteile am selben Rechtsträger ohne doppelte Erfassung desselben Anteils. Unterschiedliche Blockierungsprogramme schließen Aggregation blockierter Eigentümer nicht aus; Non-SDN-Spezialregeln getrennt prüfen.
3. Prüfe die nächste Ebene: Wird eine Zwischengesellschaft dadurch selbst blockiert, zählen ihre eigenen Beteiligungen für die weitere Prüfung. Nicht einfach alle Quoten multiplizieren. FAQ 401: 50 Prozent an einer Zwischenholding und deren 50 Prozent am Ziel können das Ziel blockieren, obwohl das rechnerische wirtschaftliche Produkt 25 Prozent ist.
4. Summiere unmittelbare Beteiligungen blockierter Personen und Anteile selbst blockierter Zwischenunternehmen am Ziel. Zirkuläre Beteiligungen, Treuhand, Optionen oder Sonderrechte nicht mit einer frei erfundenen Rechenregel erledigen; belastbare Dokumente und gegebenenfalls US-Fachbeurteilung anfordern.
5. Liegt die Summe unter 50 Prozent, gesondert kontrollieren: eigene Designation, behördlich blockierte Regierung, blockierter Unterzeichner oder wirtschaftliches Interesse an der konkreten Zahlung. FAQ 400 ist kein allgemeines Kontrollkriterium, sondern betrifft Geschäfte mit der blockierten Person.
6. Beteiligungsänderungen zeitlich prüfen. Bereits rechtmäßig blockiertes Vermögen nicht wegen späterer Anteilsveränderung eigenmächtig freigeben; FAQ 402 und konkrete Autorisierung prüfen. Keine Anteilsverschiebung als Umgehungsmodell entwerfen.
7. Liefere das begründete Beteiligungsergebnis und nötigenfalls ein vollständiges Nachforderungsschreiben. Nach einem neuen Registerbeleg nur betroffene Knoten und Folgerungen aktualisieren, dann zur konkreten Transaktionsprüfung zurückkehren.

## 1.4. Quellenpflicht

[Quellenregister Q09 bis Q12](../../references/quellenregister.md), [Zitierweise](../../references/zitierweise.md). Für diese spezifische Rechenlogik sind OFAC-Guidance und FAQ maßgebliche Behördenauslegung; kein sachfremdes Urteil erzwingen. Die EU-Kontrollprüfung und BIS-Endnutzerkontrollen nicht mit dieser Regel gleichsetzen. Eigentumsbelege und Listenstände müssen denselben relevanten Zeitpunkt betreffen.

## 1.5. Ausgabeformat

Beteiligungsbaum mit nachvollziehbarer Rechnung und ausformulierter rechtlicher Bewertung; fehlende Nachweise mit konkreter Folge benennen. Ausformulierungspflicht: eine Tabelle ersetzt den begründeten Vermerk nicht. Formatstandard: Times New Roman 11 pt soweit möglich, dezimale Gliederung. Keine automatische Kontensperre oder Entsperrung; Entscheidungsvorlage für den Verantwortlichen.

## 1.6. Beispiele

Zwei blockierte Anteilseigner halten 30 und 20 Prozent unmittelbar: zusammen 50 Prozent. Hält ein blockierter Eigentümer nur 25 Prozent an jeder von zwei nicht anderweitig blockierten Gesellschaften, werden deren jeweils 50 Prozent am Ziel nicht ohne Weiteres zugerechnet; FAQ 401, Beispiel 5, erläutert diese Grenze. Beides sind Rechenbeispiele, keine Listungsbehauptungen über reale Personen.
