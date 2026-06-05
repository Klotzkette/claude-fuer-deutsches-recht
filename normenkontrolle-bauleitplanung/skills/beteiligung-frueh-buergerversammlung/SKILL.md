---
name: beteiligung-frueh-buergerversammlung
description: "Beteiligung Frueh Buergerversammlung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beteiligung Frueh Buergerversammlung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beteiligung Frueh Buergerversammlung** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beteiligung-frueh-foermlich` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behoerdenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1 Monat Behoerdenbeteiligung §§ 4 Abs. 1 und 2 Wiederholung bei wesentlicher Aenderung § 4a Abs. 3 Online-Pflicht § 4a Abs. 4. Output: Beteiligungsfehler-Prüfprotokoll und Angriffspunkte. Abgrenzung zu aufstellungsbeschluss-bekanntmachung (formelle Verfahrenskette) und planerhaltung-214-215-baugb. |
| `buergerversammlung-protokoll-audit` | Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege sinngemäße Niederschrift Vorfestlegungs-Anzeichen Auswertung für Mandantenchronologie. Output: Audit-Protokoll Buergerversammlung mit Bewertung Fehlstellen. Abgrenzung zu beteiligung-frueh-foermlich (Beteiligungsverfahren gesamt) und normenkontrollantrag-schriftsatz. |
| `eilantrag-47-abs-6-ausserhalb-baurecht` | Eilantrag nach § 47 Abs. 6 VwGO außerhalb des Baurechts: schwere Nachteile, wichtige Gründe, Vollzugsfolgen und Antragsstrategie.; Normanker: VwGO § 47 Abs. 6; Grundrechtsbezug; Folgenabwägung; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Beteiligung Frueh Buergerversammlung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beteiligung-frueh-foermlich`

**Fokus:** Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behoerdenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1 Monat Behoerdenbeteiligung §§ 4 Abs. 1 und 2 Wiederholung bei wesentlicher Aenderung § 4a Abs. 3 Online-Pflicht § 4a Abs. 4. Output: Beteiligungsfehler-Prüfprotokoll und Angriffspunkte. Abgrenzung zu aufstellungsbeschluss-bekanntmachung (formelle Verfahrenskette) und planerhaltung-214-215-baugb.

# Beteiligung — frühzeitig und förmlich

## Zweck

Audit der zweistufigen Beteiligung. Hier finden sich die meisten Verfahrenshebel: Auslegungsdauer, Bekanntmachung der Auslegung, Identität der ausgelegten Unterlagen, Online-Veröffentlichung, Behandlung der Stellungnahmen.

## Schritt 1 — Frühzeitige Beteiligung § 3 Abs. 1 BauGB

### Inhalt
- Frühzeitige Unterrichtung der Öffentlichkeit über allgemeine Ziele und Zwecke der Planung
- Hinweis auf wesentliche Auswirkungen
- Gelegenheit zur Äußerung und Erörterung

### Form
- Häufig Bürgerversammlung
- Auslegung von Vorentwurf möglich
- Im beschleunigten Verfahren § 13a BauGB kann von früher Beteiligung abgesehen werden

### Audit-Punkte
- Wurde frühe Beteiligung durchgeführt? Ja/nein
- Wie wurde sie angekündigt? Anstoßfunktion?
- Wurde die Öffentlichkeit über wesentliche Auswirkungen unterrichtet?
- Gibt es Niederschrift der Äußerungen?

## Schritt 2 — Förmliche Beteiligung Öffentlichkeit § 3 Abs. 2 BauGB

### Auslegung
- Planentwurf und Begründung einschließlich Umweltbericht
- Auslegungsdauer mindestens ein Monat
- Auslegung an einer für die Öffentlichkeit zugänglichen Stelle

### Bekanntmachung der Auslegung
- Mindestens eine Woche vor Beginn (BVerwG-Linie)
- Hinweis auf Art der Stellungnahmen
- Hinweis dass nicht fristgerechte Stellungnahmen unberücksichtigt bleiben können (alte Präklusion)
- Hinweis Auslegungsort, -beginn, -ende

### Online-Veröffentlichung § 4a Abs. 4 BauGB
- Seit 2017 zusätzlich Einstellung in das Internet
- Pflicht zur Veröffentlichung auf der Internet-Seite der Gemeinde
- Pflicht zur Veröffentlichung in einem zentralen Internet-Portal des Landes
- In Bayern: zentrales Bauleitplan-Portal

### Inhaltliche Identität
- Ausgelegt werden müssen genau die Unterlagen, die im Bekanntmachungstext genannt sind
- Erkenntliche Diskrepanz zwischen Bekanntmachungstext und ausliegender Mappe — beachtlicher Fehler

## Schritt 3 — Behördenbeteiligung § 4 BauGB

### Frühzeitige Beteiligung § 4 Abs. 1 BauGB
- Träger öffentlicher Belange, deren Aufgabenbereich berührt wird
- Bei B-Plan in Augsburg z.B. Regierung von Schwaben, Wasserwirtschaftsamt, Untere Naturschutzbehörde, IHK, Handwerkskammer, Deutsche Bahn, Nachbargemeinden
- Aufforderung zur Stellungnahme zu allgemeinen Zielen

### Förmliche Beteiligung § 4 Abs. 2 BauGB
- Versendung des förmlichen Planentwurfs
- Frist mindestens ein Monat
- Stellungnahmen sind in die Abwägung einzustellen

### Konsultation der Nachbargemeinden § 2 Abs. 2 BauGB
- Bei interkommunaler Abstimmungspflicht
- Bei interkommunal abgestimmten Belangen

## Schritt 4 — Erneute Auslegung § 4a Abs. 3 BauGB

### Voraussetzung
- Wesentliche Änderung des Entwurfs nach Auslegung
- Substantielle Berührung der Grundzüge der Planung

### Verfahren
- Erneute Auslegung im selben Verfahren
- Beschränkung auf geänderte Teile möglich
- Frist mindestens zwei Wochen bei Beschränkung

### Häufiger Treffer
- Aufstockung Bauhöhe nach Auslegung
- Hinzufügen neuer Festsetzungen ohne erneute Auslegung
- Gravierende Änderung der Verkehrsführung
- Neuer Vorhabenträger nach Auslegung

## Schritt 5 — Behandlung der Stellungnahmen

### Eingangsverwaltung
- Eingangsstempel der Gemeinde
- Eingangsverzeichnis
- Eingangsbestätigung gegenüber Bürgern (gute Praxis, nicht zwingend)

### Inhaltliche Behandlung
- Jede Stellungnahme ist abwägungsrelevant
- Pauschale Zurückweisungen formelhaft sind Indiz für Abwägungsdefizit
- Substantielle Auseinandersetzung erforderlich

### Wegfall der Präklusion 2017
- Vor 2017 konnte Präklusion eintreten wenn nicht fristgerecht eingewendet
- Durch BVerwG-Rechtsprechung und unionsrechtskonforme Auslegung weitgehend abgemildert
- Heute kein Verlust materieller Rüge durch Nicht-Einwendung (BVerwG, Urteil vom 18.11.2010 – 4 CN 3.10)
- Trotzdem strategisch sinnvoll, eingewendet zu haben

## Schritt 6 — Audit Stellungnahmen Mandant

### Eigene Einwendungen
- Vollständige Sammlung Mandanten-Einwendungen
- Datum und Eingang bei der Stadt
- Bezugnahme auf den jeweiligen Auslegungsstand
- Eingangsbestätigung

### Behandlung
- Welche Aussagen finden sich in der Abwägungsdokumentation zu den Mandantenpunkten?
- Wurde der Belang erkannt? Falsch dargestellt? Mit anderen Belangen vermischt?
- Hat die Stadt einen Gegen-Beleg vorgelegt? Sachgerecht?

## Schritt 7 — Online-Pflicht und Barrierefreiheit § 4a Abs. 4 BauGB

### Mindestpflicht
- Veröffentlichung auf Gemeinde-Website
- Veröffentlichung im zentralen Landes-Portal
- Vollständigkeit aller auszulegenden Unterlagen

### Häufige Treffer
- Nur Planurkunde online, nicht Begründung
- Nur PDF mit niedriger Auflösung
- Fehlende textliche Festsetzungen
- Umweltbericht nicht eingestellt
- BVerwG zur Bedeutung Online-Veröffentlichung in Entwicklung

## Schritt 8 — Beachtlichkeit Verfahrensfehler

### § 214 Abs. 1 BauGB
- Beachtlich: Verstöße gegen Verfahrens- und Formvorschriften, soweit ausdrücklich aufgeführt
- Insbesondere § 3 Abs. 2 und § 4 Abs. 2 BauGB

### § 215 Abs. 1 BauGB
- Auch beachtliche Verstöße werden unbeachtlich, wenn nicht binnen Jahresfrist gerügt

### Strategie
- Sofortige Rüge gegenüber Gemeinde binnen Jahresfrist
- Parallel Normenkontrollantrag binnen Jahresfrist § 47 Abs. 2 VwGO

## Quellen

- BauGB §§ 2 3 4 4a 13 13a 214 215
- BVerwG, Urteil vom 18.11.2010 – 4 CN 3.10 (Präklusion)
- BVerwG, Urteil vom 29.1.2009 – 4 C 16.07 (Auslegung Identität)
- BVerwG, Urteil vom 18.7.2013 – 4 CN 3.12 (erneute Auslegung)

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `buergerversammlung-protokoll-audit`

**Fokus:** Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege sinngemäße Niederschrift Vorfestlegungs-Anzeichen Auswertung für Mandantenchronologie. Output: Audit-Protokoll Buergerversammlung mit Bewertung Fehlstellen. Abgrenzung zu beteiligung-frueh-foermlich (Beteiligungsverfahren gesamt) und normenkontrollantrag-schriftsatz.

# Bürgerversammlung — Protokoll-Audit

## Zweck

Die Bürgerversammlung ist der zentrale Erörterungsort der frühzeitigen Beteiligung. Aus dem Protokoll lassen sich Vorfestlegung der Stadt, formelhafte Behandlung von Belangen und atmosphärische Indizien für Abwägungsdefizite herausarbeiten.

## Schritt 1 — Rechtsrahmen

### Frühzeitige Beteiligung § 3 Abs. 1 BauGB
- Öffentlichkeit ist möglichst frühzeitig über die allgemeinen Ziele und Zwecke der Planung zu unterrichten
- Gelegenheit zur Äußerung und Erörterung
- Form steht der Gemeinde frei

### Übliche Form
- Bürgerversammlung in einem öffentlichen Saal
- Auslage des Planentwurfs vor der Versammlung
- Vortrag durch Planungsamt oder externes Planungsbüro
- Diskussionsrunde

### Niederschriftspflicht
- Keine ausdrückliche Pflicht zum Wortprotokoll
- Aber zumindest sinngemäße Wiedergabe der eingeworfenen Belange (gute Verwaltungspraxis)
- Niederschrift wird Bestandteil der Verfahrensakte

## Schritt 2 — Einladung und Tagesordnung

### Einladung
- Ortsübliche Bekanntmachung
- Frist regelmäßig mindestens eine Woche
- Hinweis auf Veranstaltungsort und Beginn

### Audit-Punkte
- Wann wurde eingeladen? Frist ausreichend?
- Wo wurde eingeladen? Ortsüblichkeit?
- Tagesordnung inhaltlich aussagekräftig? Anstoßfunktion?

## Schritt 3 — Ablauf und Sitzungsleitung

### Typischer Ablauf
1. Begrüßung Oberbürgermeister oder Bürgermeisterin
2. Vortrag Planungsamt
3. Vortrag Vorhabenträger (häufig bei privater Plan-Initiative)
4. Fragen und Wortmeldungen aus dem Publikum
5. Abschluss mit Hinweis auf Auslegungsverfahren

### Audit-Punkte Sitzungsleitung
- Wer hat die Leitung übernommen?
- Wurden Wortmeldungen gleichmäßig zugelassen?
- Wurde die Diskussion strukturell beschnitten?
- Gab es eine Beschränkung der Redezeit, die kritischen Bürgern den Zugang erschwerte?

## Schritt 4 — Vortrag der Stadt und des Vorhabenträgers

### Inhalt
- Allgemeine Ziele der Planung
- Anlass der Planung
- Wesentliche Festsetzungen im Überblick
- Auswirkungen Umwelt Verkehr Soziales

### Häufige Treffer
- Vortrag suggeriert Beschlussreife ("der Plan wird so kommen")
- Vortrag stellt Alternativen einseitig dar
- Vortrag verschweigt zentrale Probleme (Stellplatzreduzierung, Lärmwerte)
- Vortrag enthält Werbeaussagen Vorhabenträger statt neutraler Information

## Schritt 5 — Wortmeldungen und Aussprache

### Audit der Niederschrift
- Welche Belange wurden eingeworfen?
- Welche Wortmeldungen wurden namentlich aufgenommen, welche anonymisiert?
- Wurde Mandantin selbst gehört?
- Wurden Belange zusammengefasst oder einzeln aufgenommen?

### Kritische Indizien
- Niederschrift erwähnt nur Stadt-Positionen, Bürger-Beiträge in Sammelposten
- Wortmeldungen mit konkreten Zahlen werden zusammenfassend pauschal wiedergegeben
- Fehlende Antworten der Stadt zu Detailfragen
- Zwischenrufe und Buh-Rufe sind Indiz für unausgewogene Sitzungsleitung — gehören aber meist nicht ins Protokoll

## Schritt 6 — Vorfestlegungs-Anzeichen

### Indizien Vorfestlegung
- Stadt-Vertreter verwendet Zukunftsform statt Konjunktiv ("der Plan wird festsetzen", nicht "der Plan soll festsetzen")
- Vorhabenträger präsentiert bereits konkrete Grundstücksaufteilung, Bauphasen, Mietverträge
- Hinweise auf bereits abgeschlossene Verträge mit der Stadt
- Aussagen wie "wir können hier nicht mehr zurück" oder "die Stadt hat sich verpflichtet"

### Rechtliche Bedeutung
- Vorfestlegung ist Anhaltspunkt für Abwägungsausfall
- Eine Abwägung, deren Ergebnis bereits feststeht, ist eine Schein-Abwägung
- BVerwG zur Abwägungsausfall-Rechtsprechung

## Schritt 7 — Mandantenchronologie

### Eigenmitschrift Mandant
- Hat Mandantin selbst Notizen gemacht? Audio aufgezeichnet?
- Wer war als Begleitung dabei (Zeuge)?
- Auch nachträgliche Aufzeichnung im Aktenvermerk dokumentieren

### Eidesstattliche Versicherung
- Bei abweichendem Sachverhalt eidesstattliche Versicherung Mandantin und Zeugen
- Im Eilantrag § 47 Abs. 6 VwGO als Glaubhaftmachung verwendbar

## Schritt 8 — Vergleich mit Abwägungsdokumentation

### Spätere Behandlung
- Welche der in der Bürgerversammlung geäußerten Belange tauchen in der Abwägungsdokumentation auf?
- Welche fehlen ganz?
- Welche werden inhaltlich verfälscht wiedergegeben?

### Strategische Bedeutung
- Fehlende Behandlung in der Abwägung = Abwägungsdefizit
- Verfälschte Wiedergabe = Abwägungsausfall im Einzelpunkt
- Diese Lücken sind die schärfsten Angriffspunkte im Normenkontrollverfahren

## Schritt 9 — Audit-Checkliste

| Punkt | Prüfung |
|---|---|
| Einladung ortsüblich? | Ja/nein |
| Frist gewahrt? | Ja/nein |
| Tagesordnung aussagekräftig? | Ja/nein |
| Vortragsmaterial neutral? | Ja/nein |
| Wortmeldungen gleichmäßig zugelassen? | Ja/nein |
| Niederschrift vollständig? | Ja/nein |
| Mandantin gehört worden? | Ja/nein |
| Vorfestlegungs-Indizien? | Ja/nein |
| Belange in spätere Abwägung übernommen? | Ja/nein |
| Eigene Mitschrift Mandantin? | Ja/nein |

## Quellen

- BauGB § 3 Abs. 1
- BayGO Art. 18 (Bürgerversammlung allgemein)
- BVerwG, Urteil vom 5.7.1974 – 4 C 50.72 (Abwägungsausfall-Linie)
- BVerwG, Urteil vom 12.12.1969 – 4 C 105.66 (Abwägungsgebot Grundlagen)

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `eilantrag-47-abs-6-ausserhalb-baurecht`

**Fokus:** Eilantrag nach § 47 Abs. 6 VwGO außerhalb des Baurechts: schwere Nachteile, wichtige Gründe, Vollzugsfolgen und Antragsstrategie.; Normanker: VwGO § 47 Abs. 6; Grundrechtsbezug; Folgenabwägung; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar.

# Eilantrag nach § 47 Abs. 6 VwGO außerhalb des Baurechts: schwere Nachteile, wichtige Gründe, Vollzugsfolgen und Antragsstrategie.

## Auftrag

Dieser Skill löst § 47 VwGO aus der reinen Bauleitplanung. Er prüft, ob eine im Rang unter dem Landesgesetz stehende Rechtsvorschrift direkt vor dem OVG/VGH überprüft werden kann oder ob nur eine Inzidentkontrolle im Verfahren gegen einen Einzelakt passt.

## Normanker

VwGO § 47 Abs. 6; Grundrechtsbezug; Folgenabwägung. Vor jeder Ausgabe muss das jeweilige Landesrecht geprüft werden, weil § 47 Abs. 1 Nr. 2 VwGO die Normenkontrolle außerhalb der BauGB-Fälle nur eröffnet, soweit Landesrecht dies bestimmt.

## Prüfprogramm

1. Normtyp: Satzung, Rechtsverordnung, Bebauungsplan, Polizeiverordnung, Benutzungssatzung oder bloßer Verwaltungsakt?
2. Statthaftigkeit: § 47 Abs. 1 Nr. 1 oder Nr. 2 VwGO, Landesrechtseröffnung, Rang unter Landesgesetz.
3. Antragsteller: mögliche Rechtsverletzung, Adressat, Eigentümer, Nutzer, Gemeinde, Verband oder Konkurrent.
4. Frist und Rechtsschutzbedürfnis: Jahresfrist, fortbestehende Beschwer, Parallelverfahren.
5. Materielle Kontrolle: Ermächtigung, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.
6. Rechtsfolge: Unwirksamkeit, Bekanntmachung der Entscheidung, Wirkung auf Folgebescheide, neue Satzung.

## Ausgabe

Erzeuge eine Statthaftigkeitsskizze, Satzungs-Red-Team, Eilantragsskizze, Schriftsatzgliederung oder Bürger-/Mandantenbrief.
