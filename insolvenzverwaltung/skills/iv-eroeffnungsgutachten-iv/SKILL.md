---
name: iv-eroeffnungsgutachten-iv
description: "IV Eroeffnungsgutachten IV: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Eroeffnungsgutachten IV

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Eroeffnungsgutachten IV** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-eroeffnungsgutachten` | Eroeffnungsgutachten als Sachverständiger oder vorlaeufiger Insolvenzverwalter erstellen wenn Gericht Prüfauftrag erteilt. §§ 17 18 19 InsO Eroffnungsgründe §§ 26 54 InsO Massekostendeckung. Prüfraster: Zahlungsunfähigkeit drohende ZU Überschuldung Massekosten Sicherungsbedarf Fortführungsempfehlung. Output: Gutachtengliederung mit Sachverhalt Ergebnis Empfehlung. Abgrenzung: nicht für laufende Verwaltung nach Eroeffnung (iv-regelverfahren-eroeffnung). |
| `iv-forderungsanmeldung-pruefung` | Eingehende Forderungsanmeldungen nach § 174 InsO prüfen und Tabelle für Prüfungstermin vorbereiten. §§ 174 175 176 InsO §§ 38 39 InsO Rang. Prüfraster: Schriftform Beleg Grund Betrag Rang Absonderungsrechte vorsaetzlich unerlaubte Handlung Nachrang. Output: Tabellenvermerke Bestreitenserklärungen Nachforderungen. Abgrenzung: nicht für Prüfungstermin selbst (iv-tabelle-prüfungstermin) oder allgemeine Masseeinsammlung. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Eroeffnungsgutachten IV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-eroeffnungsgutachten`

**Fokus:** Eroeffnungsgutachten als Sachverständiger oder vorlaeufiger Insolvenzverwalter erstellen wenn Gericht Prüfauftrag erteilt. §§ 17 18 19 InsO Eroffnungsgründe §§ 26 54 InsO Massekostendeckung. Prüfraster: Zahlungsunfähigkeit drohende ZU Überschuldung Massekosten Sicherungsbedarf Fortführungsempfehlung. Output: Gutachtengliederung mit Sachverhalt Ergebnis Empfehlung. Abgrenzung: nicht für laufende Verwaltung nach Eroeffnung (iv-regelverfahren-eroeffnung).

# Eröffnungsgutachten

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eröffnungsgutachten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Erstellt die Arbeitsgliederung für ein Eröffnungsgutachten mit Sachverhalt, Eröffnungsgründen, Massekostendeckung, Sicherungsbedarf und gerichtlicher Empfehlung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- das Gericht ein Gutachten zur Verfahrenseröffnung beauftragt
- Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit oder Überschuldung zu prüfen ist
- eine Fortführung bis zur Eröffnung möglich erscheint

## Eingaben

- Antrag und Anlagen
- BWA, SuSa, OPOS, Bankdaten, Lohn- und Steuerstände
- Vermögensverzeichnis und Sicherheiten

## Workflow

1. **Sachverhalt sichern** - Antrag, Gesellschaft, Geschäftsbetrieb und Unterlagenstand darstellen.
2. **Eröffnungsgründe prüfen** - § 17, § 18 und § 19 InsO anhand konkreter Zahlen trennen.
3. **Masse prüfen** - freie Masse, Kosten, Verwertung, Vorschuss und Massearmut abgleichen.
4. **Empfehlung bauen** - Eröffnung, Abweisung, Sicherungsmaßnahmen oder weitere Aufklärung begründen.

## Ausgabe

- Gutachtengliederung
- Zahlen- und Belegliste
- Empfehlungsentwurf an das Insolvenzgericht

## Qualitätsgates

- Eröffnungsgrund und Kostendeckung getrennt
- jede Zahl mit Quelle
- fehlende Unterlagen als Aufklärungsbedarf markiert

## Rote Schwellen

- Kassenbestand nicht verifiziert
- Sicherheiten ungeklärt
- Betriebsfortführung ohne Liquiditätsbrücke

## Interne Vorlagen

- assets/templates/eroeffnungsgutachten-gliederung.md
- assets/templates/liquiditaetsstatus-kurzcheck.md

## Amtliche Erstquellen

- §§ 16 bis 19 InsO
- § 26 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 129/22 vom 18.04.2024** — Bei Liquiditätsstatus im Eröffnungsgutachten: Verwalter muss konkret darlegen, dass der Schuldner mit dauerhafter Nichtbefriedigung anderer Gläubiger gerechnet hat. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH II ZR 206/22 vom 23.07.2024** — Bei Sachverhaltsaufnahme mit Wechsel der Geschäftsleitung: fortwirkende Haftung des ausgeschiedenen GF in Anfechtungs- und Haftungsprüfungen berücksichtigen. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- IDW S 11 als Methodik-Standard für Liquiditätsstatus und Fortbestehensprognose (Prognosezeitraum 12 Monate seit 01.01.2024).

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

## 2. `iv-forderungsanmeldung-pruefung`

**Fokus:** Eingehende Forderungsanmeldungen nach § 174 InsO prüfen und Tabelle für Prüfungstermin vorbereiten. §§ 174 175 176 InsO §§ 38 39 InsO Rang. Prüfraster: Schriftform Beleg Grund Betrag Rang Absonderungsrechte vorsaetzlich unerlaubte Handlung Nachrang. Output: Tabellenvermerke Bestreitenserklärungen Nachforderungen. Abgrenzung: nicht für Prüfungstermin selbst (iv-tabelle-prüfungstermin) oder allgemeine Masseeinsammlung.

# Forderungsanmeldungen prüfen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Forderungsanmeldungen prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüft eingehende Forderungsanmeldungen so, dass Tabelle, Bestreiten und Prüfungstermin belastbar vorbereitet werden.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Forderungsanmeldungen eingehen
- Belege fehlen oder Rang unklar ist
- vbuH-, Steuerstraf- oder Unterhaltskennzeichen auftauchen

## Eingaben

- Anmeldung, Belege, Rechnungen, Titel
- Schuldnerbuchhaltung, OPOS, Verträge
- Rangangaben und Sicherungsrechte

## Workflow

1. **Form prüfen** - Schriftform oder elektronisches Dokument, Grund, Betrag und Belege erfassen.
2. **Materiell prüfen** - Buchhaltung, Vertrag, Titel, Zinsen, Rang und Absonderungsrechte abgleichen.
3. **Entscheidung** - feststellen, vorläufig bestreiten, endgültig bestreiten oder Nachforderung stellen.
4. **Dokumentieren** - Tabellenvermerk mit Grund, Betrag, Rang und Belegstatus erzeugen.

## Ausgabe

- Prüfvermerk je Forderung
- Nachforderungsschreiben
- Tabellenimportliste

## Qualitätsgates

- Betrag und Grund getrennt geprüft
- Rang nicht aus Gläubigerangabe übernommen
- vbuH nur mit Tatsachen geprüft

## Rote Schwellen

- fehlende Urkunden
- doppelte Anmeldung
- Forderung als Masseverbindlichkeit fehlklassifiziert

## Interne Vorlagen

- assets/templates/forderungen-und-tabelle.md
- assets/templates/tabellenpruefung.csv

## Amtliche Erstquellen

- § 174 InsO
- § 175 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Anforderungen an die Forderungsanmeldung (§ 174 Abs. 2 InsO); bei Abtretung müssen Zedent und Zessionar die abgetretene Forderung jeweils gesondert anmelden und einen eigenen Prüfungstermin durchlaufen. Wirksame Anmeldung setzt hinreichende Individualisierung voraus, nicht aber eine schlüssige Rechtsbegründung.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Kapitalmarktrechtliche Schadensersatzforderungen geschädigter Aktionäre sind keine einfachen Insolvenzforderungen iSd § 38 InsO; sie treten hinter die einfachen Insolvenzgläubiger zurück. Bedeutung: Bei Prüfung von Aktionärsforderungen Rangfrage konkret einordnen, Bestreiten der einfachen Insolvenzforderungseigenschaft regelmäßig geboten.
 Quelle: BGH-Pressemitteilung 2025/211; <https://www.lto.de/recht/kanzleien-unternehmen/k/bgh-ixzr12724-wirecard-insolvenzmasse-forderungen-aktionaere-urteil>
- Weitere BGH-Linien zur Individualisierung der Forderung, zur Vorsatzfeststellung nach § 174 Abs. 2 / § 302 Nr. 1 InsO vor Ausgabe über dejure.org / openjur.de verifizieren.

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
