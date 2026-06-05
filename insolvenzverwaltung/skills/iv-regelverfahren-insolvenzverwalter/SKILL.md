---
name: iv-regelverfahren-insolvenzverwalter
description: "IV Regelverfahren Insolvenzverwalter: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Regelverfahren Insolvenzverwalter

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Regelverfahren Insolvenzverwalter** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-regelverfahren-eroeffnung` | Regelinsolvenzverfahren nach Eroffnungsbeschluss umsetzen: Besitzuebergang Masse Tabelle Berichtstermin Verwertung. §§ 80 148 149 InsO §§ 151 ff. InsO Masseberechnung. Prüfraster: Verfuegungsbefugnis Bekanntmachungen Leistungssperren Massekonto Tabellenvorbereitung erste Verwertung. Output: Verfahrensplan Masseregister Tabellenstruktur. Abgrenzung: nicht für Eroeffnungsgutachten (iv-eroeffnungsgutachten) oder Abschlussphase. |
| `spezial-insolvenzverwalter-fristen-form-und-zustaendigkeit` | Insolvenzverwalter: Fristen, Form, Zuständigkeit und Rechtsweg im Insolvenzverwaltung: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/SGB III), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Regelverfahren Insolvenzverwalter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-regelverfahren-eroeffnung`

**Fokus:** Regelinsolvenzverfahren nach Eroffnungsbeschluss umsetzen: Besitzuebergang Masse Tabelle Berichtstermin Verwertung. §§ 80 148 149 InsO §§ 151 ff. InsO Masseberechnung. Prüfraster: Verfuegungsbefugnis Bekanntmachungen Leistungssperren Massekonto Tabellenvorbereitung erste Verwertung. Output: Verfahrensplan Masseregister Tabellenstruktur. Abgrenzung: nicht für Eroeffnungsgutachten (iv-eroeffnungsgutachten) oder Abschlussphase.

# Regelverfahren nach Eröffnung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Regelverfahren nach Eröffnung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Setzt den Eröffnungsbeschluss in Verwaltungspraxis um: Besitz, Masse, Tabelle, Berichtstermin, Verwertung, Kommunikation und Verteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Eröffnungsbeschluss zugestellt ist
- Forderungsanmeldungen und Berichtstermin vorbereitet werden
- die erste Verwertungsphase startet

## Eingaben

- Eröffnungsbeschluss
- Masseverzeichnis, Verträge, Gläubigerliste
- Forderungsanmeldungen und Sicherungsrechte

## Workflow

1. **Eröffnung umsetzen** - Verfügungsbefugnis, Bekanntmachungen und Leistungssperren kontrollieren.
2. **Masse organisieren** - Massekonto, Verträge, Versicherungen, Forderungen und Verwertung anlegen.
3. **Tabelle vorbereiten** - Anmeldefristen, Forderungen, Rang und Widersprüche strukturieren.
4. **Berichtstermin** - Fortführung, Verwertung, Planoption und Ausschussfragen vorbereiten.

## Ausgabe

- Eröffnungs-Checkliste
- Masse- und Vertragsregister
- Berichtsterminpaket

## Qualitätsgates

- Massekonto getrennt
- Forderungen nicht mit Masseverbindlichkeiten vermischt
- Berichtspflichten terminiert

## Rote Schwellen

- ungeklärte Drittrechte
- fortlaufende Verträge ohne Entscheidung
- Sicherungsrechte nicht erfasst

## Interne Vorlagen

- assets/templates/regelverfahren-eroeffnung.md
- assets/templates/masseverzeichnis.md

## Amtliche Erstquellen

- §§ 27, 28, 80 ff. InsO
- §§ 174 ff. InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `spezial-insolvenzverwalter-fristen-form-und-zustaendigkeit`

**Fokus:** Insolvenzverwalter: Fristen, Form, Zuständigkeit und Rechtsweg im Insolvenzverwaltung: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/SGB III), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Insolvenzverwalter: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzverwalter: Fristen, Form, Zuständigkeit und Rechtsweg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Insolvenzverwalter: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Insolvenzverwalter: Fristen, Form, Zuständigkeit und Rechtsweg / insolvenzverwalter fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, StaRUG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Insolvenzverwalter** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Insolvenzverwalter-Fristen — Kernzeiten
- **§ 22 InsO Sicherungsmaßnahmen:** ab Bestellung sofort (in der Praxis: erste 24–72 Stunden).
- **§ 156 InsO Berichtstermin:** ca. 6 Wochen bis 3 Monate nach Eröffnung — Verwalter berichtet zu Lage, Fortführung/Stilllegung, Vergleichsoptionen.
- **§ 158 InsO Stilllegung:** vor Berichtstermin nur mit Zustimmung Gläubigerausschuss oder bei Massearmut.
- **§ 176 InsO Prüfungstermin:** Frist zur Anmeldung (regelmäßig 4–6 Wochen) endet vor diesem Termin.
- **§ 187, § 196 InsO Verteilung:** Abschlagsverteilung möglich nach Prüfungstermin; Schlussverteilung am Ende.
- **§ 200 InsO Aufhebung:** nach Schlussverteilung.
- **§ 174 Abs. 3 InsO Nachrang § 39 InsO:** gesonderte Aufforderung des Gerichts erforderlich, vor Aufforderung keine Anmeldung erfolgt.
- **§ 113 InsO Kündigungsfrist Arbeitsverhältnisse:** 3 Monate (auch bei längerer ordentlicher Kündigungsfrist) — Sonderkündigungsrecht Verwalter.
- **§ 109 InsO Mietverhältnisse:** Sonderkündigungsrecht Verwalter mit 3-Monats-Frist.
- **§ 103 InsO Erfüllungswahl:** unverzüglich, sonst Nichterfüllungswahl angenommen — bei Hinweis des Vertragspartners zur Stellungnahme aufgefordert.

## Zuständigkeit
- **Insolvenzgericht** = Amtsgericht am Sitz des Schuldners (§ 2 InsO). Bei Sitzverlegung in den letzten 6 Monaten: vorheriger Sitz (§ 3 Abs. 1 InsO).
- **Beschwerden gegen Verwalter-Entscheidungen:** sofortige Beschwerde § 6 InsO.
- **Restrukturierungsgericht** = Landgericht beim OLG-Sitz (§ 34 StaRUG) — nur für StaRUG-Verfahren.

## Form
- Berichte und Anträge zum Insolvenzgericht: schriftlich (Schriftsatz) oder beA-Übermittlung; Anlagen elektronisch oder in Papier.
- Verwaltervergütungsantrag § 63 InsO i.V.m. InsVV § 8 ff. — mit Begründung der Zu- und Abschläge.
- Schlussbericht und Schlussrechnung § 197 InsO — beim Insolvenzgericht einzureichen.
