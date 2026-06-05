---
name: strafrecht-verfahrensstadium-strafbefehl
description: "Strafrecht Verfahrensstadium Strafbefehl: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strafrecht Verfahrensstadium Strafbefehl

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Strafrecht Verfahrensstadium Strafbefehl** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-strafrecht-fristen-form-und-zustaendigkeit` | Strafrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-verfahrensstadium-strafbefehl-bis-kammer` | Strafzumessung vom Strafbefehl bis zur großen Strafkammer: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` | Taeter-Opfer-Ausgleich § 46a StGB und Schadenswiedergutmachung als Strafmilderung oder Absehen von Strafe. Nr. 1 Wiedergutmachung gegenueber dem Verletzten erfordert friedensstiftenden kommunikativen Prozess (BGH 4 StR 232/25 vom 20.11.2025). Nr. 2 wesentliche Schadenswiedergutmachung trotz erheblichem Aufwand. Rechtsfolge § 49 Abs. 1 StGB oder Absehen bei Strafe nicht ueber 1 Jahr. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Strafrecht Verfahrensstadium Strafbefehl**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-strafrecht-fristen-form-und-zustaendigkeit`

**Fokus:** Strafrecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Strafrecht: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Strafrecht: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Strafrecht: Fristen, Form, Zuständigkeit und Rechtsweg / strafrecht fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Strafrecht** prüfen.
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

## Strafzumessungs-Fristen / Form / Zustaendigkeit Bausteine
- **Strafzumessungs-Zustaendigkeit nach Verfahrensstand:**
 - **StA-Antrag Strafbefehl § 407 StPO:** StA setzt Strafmass vor.
 - **AG Strafrichter § 25 GVG:** bis 2 Jahre Freiheitsstrafe.
 - **AG Schoeffengericht § 28 GVG:** bis 4 Jahre.
 - **LG grosse Strafkammer § 76 GVG:** ueber 4 Jahre / Wirtschaft.
 - **LG Schwurgericht § 74 II GVG:** Toetungsdelikte.
- **Strafzumessungs-relevante Fristen:**
 - **Verjaehrungsfristen** §§ 78-79b StGB:
 - 3 Jahre: Vergehen mit Strafrahmen bis 1 Jahr (§ 78 III Nr. 5 StGB).
 - 5 Jahre: 1-5 Jahre Strafrahmen.
 - 10 Jahre: 5-10 Jahre Strafrahmen.
 - 20 Jahre: ueber 10 Jahre Strafrahmen.
 - 30 Jahre: lebenslange Freiheitsstrafe.
 - Mord § 211 StGB: unverjaehrbar § 78 II StGB.
 - **§ 78c StGB Unterbrechung** durch z. B. Vernehmung Beschuldigter, Erhebung oeffentliche Klage, Eroeffnungsbeschluss; **§ 78b StGB Ruhen** bei Verhinderung gesetzlicher Verfolgung.
 - **Bewaehrungszeit § 56a StGB:** 2-5 Jahre.
 - **Bewaehrungswiderruf § 56f StGB** bei neuer Tat in Bewaehrungszeit.
 - **Strafrest-Aussetzung § 57 StGB:** nach Halbstrafe (Erstverurteilung) oder 2/3 (Regel).
 - **BZRG-Tilgungsfristen § 46 BZRG:** 5 Jahre (Geldstrafe bis 90 TS, Freiheitsstrafe bis 3 Monate), 10 Jahre (bis 1 Jahr), 15 Jahre (sonst).
- **Form-Re-Check Strafzumessung:**
 - **Urteilsbegruendung §§ 267 StPO** muss Strafzumessungstatsachen § 46 StGB einzeln darstellen; Lueckenhaftigkeit = Sachruege Revision.
 - **Doppelverwertungsverbot § 46 III StGB** beachten (Tatbestandsmerkmale nicht zugleich strafschaerfend).
 - **Verstaendigung § 257c StPO** schriftlich im Protokoll; Belehrung § 257c V StPO Pflicht.
- **Rechtsweg Strafzumessung:**
 - Berufung § 314 StPO bei AG-Urteil; volle Tatsachenrevision.
 - Revision §§ 333, 337 StPO Sachruege gegen Strafzumessung; Erfolg selten (BGH-Linie: Strafzumessung Tatrichter, nur Wertungsfehler / Lueckenhaftigkeit greift).
 - Nachtraegliche Gesamtstrafe § 460 StPO Antrag Vollstreckungsbehoerde / Gericht.

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.

## 2. `spezial-verfahrensstadium-strafbefehl-bis-kammer`

**Fokus:** Strafzumessung vom Strafbefehl bis zur großen Strafkammer: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Strafzumessung vom Strafbefehl bis zur großen Strafkammer

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `strafzumessung`. Kontext des Plugins: Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer. § 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewaehrung § 56 § 49 Regelbeispiele besonders schwerer Fall Verstaendigung § 257c StPO TOA § 46a Gesamtstrafe § 55 JGG.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Strafzumessung vom Strafbefehl bis zur großen Strafkammer** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## Strafzumessung pro Verfahrensstadium Bausteine
- **Strafbefehl §§ 407 ff. StPO (Vergehen):**
 - Hoechstrahmen Geldstrafe (regelmaessig 360 TS); Freiheitsstrafe bis 1 Jahr nur **mit Verteidiger und auf Bewaehrung** § 407 II 2 StPO.
 - Strafzumessung StA-Antrag massgeblich; Gericht kann abweichen ggf. ablehnen (zurueck zur Anklage).
 - Tagessatz-Hoehe nach Schaetzung Einkommen.
- **AG Strafrichter § 25 GVG:**
 - Bis 2 Jahre Freiheitsstrafe; Geldstrafe.
 - Pruefung Bewaehrung § 56 StGB regelmaessig.
- **AG Schoeffengericht § 28 GVG:**
 - Bis 4 Jahre Freiheitsstrafe; bei Anklagen StA, die ueber Strafrichter hinausgehen.
 - Bewaehrung § 56 StGB; Massregeln § 61 ff. StGB.
- **LG grosse Strafkammer § 76 GVG:**
 - Ueber 4 Jahre Freiheitsstrafe; schwere Wirtschaftsstrafsachen, Mehrtaeter, Banden.
 - Komplexe Strafzumessung mit § 46 StGB-Bilanz; Gesamtstrafe § 55 StGB.
- **LG Schwurgericht § 74 II GVG:**
 - Toetungsdelikte §§ 211-222 StGB.
 - Lebenslange Freiheitsstrafe bei Mord; bei besonders schwerer Schuld Vorbehalt § 57a StGB (15 J. Mindestverbuessung; ggf. lebenslang).
- **JGG §§ 17, 18:**
 - Jugendstrafe bei schaedlichen Neigungen / Schwere der Schuld; 6 Monate bis 5 / 10 Jahre.
 - § 105 JGG bei Heranwachsenden: Jugendrecht / Erwachsenenrecht je nach Reife.
- **Strafzumessungs-Korridore typisch (Indikativ - regional unterschiedlich, keine Az-Auflistung aus Modellwissen):**
 - Diebstahl § 242 StGB: regelmaessig Geldstrafe; ab Schaden 1000+ EUR und Wiederholung Freiheitsstrafe diskussiert.
 - Betrug § 263 StGB: Schaden-Korridor entscheidend; Regelbeispiel § 263 III StGB ab ~50.000 EUR / Bandenmaessigkeit.
 - Trunkenheit § 316 StGB: idR Geldstrafe + Fahrerlaubnisentzug § 69 StGB.
 - Koerperverletzung § 223 StGB: Geldstrafe; § 224 (gefaehrlich) regelmaessig Freiheitsstrafe diskutiert.
- **Verstaendigung § 257c StPO** in allen Stadien moeglich; Korridor verbindlich.

## 3. `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung`

**Fokus:** Taeter-Opfer-Ausgleich § 46a StGB und Schadenswiedergutmachung als Strafmilderung oder Absehen von Strafe. Nr. 1 Wiedergutmachung gegenueber dem Verletzten erfordert friedensstiftenden kommunikativen Prozess (BGH 4 StR 232/25 vom 20.11.2025). Nr. 2 wesentliche Schadenswiedergutmachung trotz erheblichem Aufwand. Rechtsfolge § 49 Abs. 1 StGB oder Absehen bei Strafe nicht ueber 1 Jahr.

# Taeter-Opfer-Ausgleich und Schadenswiedergutmachung — § 46a StGB

## Worum geht es?

§ 46a StGB ermoeglicht eine **Strafmilderung** nach § 49 Abs. 1 StGB oder bei Strafe nicht ueber **1 Jahr** Freiheitsstrafe oder Geldstrafe bis 360 Tagessaetzen sogar das **Absehen von Strafe**. Voraussetzung:

- **Nr. 1**: Taeter hat in dem Bemuehen, einen Ausgleich mit dem Verletzten zu erreichen (Taeter-Opfer-Ausgleich), seine Tat ganz oder zum ueberwiegenden Teil wiedergutgemacht oder deren Wiedergutmachung ernsthaft angestrebt, **oder**
- **Nr. 2**: die Schadenswiedergutmachung von dem Taeter erhebliche persoenliche Leistungen oder persoenlichen Verzicht erfordert hat und er das Opfer ganz oder zum ueberwiegenden Teil entschaedigt.

## Wann brauchen Sie diese Skill?

- Sie verteidigen einen Mandanten, der mit dem Opfer ins Gespraech kommen oder Schaden ersetzen kann oder bereits hat.
- Sie planen eine Verstaendigung (§ 257c StPO) und wollen TOA als Strafmilderungs-Baustein einbringen.
- Sie pruefen ein Urteil oder eine Strafzumessungsruege, in der § 46a StGB nicht oder fehlerhaft angewendet wurde.

## Rechtliche Grundlagen

- **§ 46a StGB** — Voraussetzungen und Rechtsfolge (Milderung oder Absehen).
- **§ 49 Abs. 1 StGB** — technische Anwendung der Milderung.
- **§ 155a StPO** — Pruefungspflicht der Staatsanwaltschaft, ob TOA in Betracht kommt.
- **§ 155b StPO** — Datenuebermittlung an Vermittlungsstellen.
- **§ 153a StPO** — Einstellung gegen Auflage; oft mit TOA verbunden.

## Strafzumessungs-Grundsatz

### § 46a Nr. 1 StGB — TOA (Taeter-Opfer-Ausgleich)

BGH, Beschluss vom 20.11.2025 — 4 StR 232/25 (4. Strafsenat): § 46a Nr. 1 StGB setzt einen **friedensstiftenden kommunikativen Prozess** zwischen Taeter und Opfer voraus, der eine Verantwortungsuebernahme des Taeters erkennen laesst; **blosse Schadenswiedergutmachung ohne kommunikatives Element genuegt nicht** (Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25).

Erforderlich sind also:

- Kommunikativer Kontakt mit dem Opfer (direkt oder ueber Vermittler).
- Anerkennung des Unrechts gegenueber dem Opfer.
- Wiedergutmachung ganz oder ueberwiegend **oder** ernsthaftes Bemuehen.
- Akzeptanz des Opfers ist hilfreich, aber nicht unbedingt Tatbestandsmerkmal — st. Rspr. relativiert: Wenn das Opfer den Ausgleich ablehnt, kann das Bemuehen genuegen.

### § 46a Nr. 2 StGB — Wesentliche Schadenswiedergutmachung

- Erhebliche persoenliche Leistung des Taeters: hoher Aufwand, finanzielle Anstrengung, Verzicht.
- Opfer ganz oder zum ueberwiegenden Teil entschaedigt.
- Kommunikativer Prozess ist hier nicht zwingend, die Wiedergutmachung steht im Zentrum.

## Rechtsfolge

- Strafmilderung nach § 49 Abs. 1 StGB (zwingend, wenn Tatbestand erfuellt).
- Bei Strafe nicht ueber 1 Jahr Freiheitsstrafe oder Geldstrafe bis 360 Tagessaetze: **Absehen von Strafe** moeglich (wenn auch nicht zwingend; pflichtgemaesses Ermessen).

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **TOA-Eignung pruefen**:
 - Ist das Opfer ansprechbar?
 - Liegt eine Tat vor, die einen kommunikativen Prozess erlaubt (auch bei Sexualstraftaten moeglich; vgl. BGH 4 StR 232/25, sehr restriktive Pruefung)?
2. **Vermittlungsstelle** einschalten (Taeter-Opfer-Ausgleichsstelle der Landesjustiz, gemeinnuetzige Vermittlungstraeger).
3. **Mandantengespraech** vorbereiten: Verantwortungsuebernahme, Reue, Bereitschaft zur Wiedergutmachung; sensible Themen (Verletzungen des Opfers, evtl. Trauma) klaeren.
4. **Erste Kontaktaufnahme** ueber den Vermittler; **keine** direkte Kontaktaufnahme bei Sexualstraftaten oder Gewaltdelikten ohne Vorbereitung.
5. **Ausgleichsgespraech** durchfuehren; Protokollieren lassen.
6. **Wiedergutmachung** vereinbaren: Geldzahlung, Entschuldigung, andere Form der Wiedergutmachung (z.B. Therapie-Vereinbarung, gemeinnuetzige Leistung im Sinne des Opfers).
7. **Beleg fuer das Gericht**: TOA-Protokoll, Quittung, Bescheinigung der Vermittlungsstelle.
8. **Antrag in der Hauptverhandlung**: "Wir beantragen die Anwendung von § 46a Nr. 1 StGB. Die Strafe ist nach § 49 Abs. 1 StGB zu mildern; hilfsweise ist von Strafe abzusehen (§ 46a Satz 2 StGB)."

## Bei Schadenswiedergutmachung (Nr. 2)

- **Erheblicher Aufwand**: nicht jede pflichtgemaesse Zahlung reicht; es muss Verzicht / Anstrengung erkennbar sein.
- Beleg fuer Hoehe, Form und persoenlicher Aufwand. Mietminderung, Vermoegensverkauf, Kredit fuer Wiedergutmachung.
- Zahlung an Versicherung reicht oft **nicht**, weil diese sich an den Taeter wendet (Verzicht-Rueckforderung); st. Rspr.; Aktenzeichen verifizieren.

## Sondersituationen

### TOA bei Sexualstraftaten

BGH 4 StR 232/25 vom 20.11.2025: TOA ist auch bei sexuellem Missbrauch nicht generell ausgeschlossen, aber die Pruefung ist streng. Der kommunikative Prozess muss real stattgefunden haben und das Opfer darf nicht (re-)traumatisiert werden. Vorgehen mit Vermittler **zwingend**.

### TOA bei Vermoegensdelikten

- Schadenswiedergutmachung im Vordergrund.
- Kommunikatives Element: Anerkennung des Schadens, Entschuldigung.

### TOA bei juristischen Personen als Opfer

- Statt kommunikativem Prozess steht die Wiedergutmachung mit Ansprechen des Vorstands / der Geschaeftsfuehrung im Mittelpunkt.

## Typische Fehler

- **Blosse Zahlung** ohne kommunikativen Prozess — nach BGH 4 StR 232/25 nicht ausreichend fuer § 46a Nr. 1 StGB.
- **Direkter Opferkontakt** in sensiblen Faellen — kann re-traumatisieren und das Verfahren erschweren.
- **TOA-Belege** fehlen oder zu spaet.
- **§ 46a Nr. 2 StGB** verwechselt mit Nr. 1: bei Nr. 2 muss der Aufwand erheblich sein, nicht nur die Wiedergutmachung.
- **Absehen von Strafe**-Antrag uebersehen, obwohl Strafrahmen es zulaesst.
- **TOA verspaetet**: Gericht erkennt es als verfahrenstaktische Schutzbehauptung, wenn TOA erst kurz vor der Hauptverhandlung beginnt.

## Querverweise

- `strafmilderung-49-stgb-zwingend-fakultativ` — technische Anwendung.
- `verstaendigung-257c-stpo-strafzumessung` — TOA als Verhandlungsbaustein.
- `153a-stpo-einstellung-gegen-auflage` — Einstellung mit TOA-Auflage.
- `gestaendnis-und-strafmilderung` — Verbindung zum Gestaendnis.
- Plugin `fachanwalt-strafrecht`: `fachanwalt-strafrecht-verstaendigung-257c-toa-46a`.

## Quellen und Stand 05/2026

- § 46a StGB in der geltenden Fassung.
- §§ 49 Abs. 1, 155a, 155b, 153a StPO.
- BGH, Beschluss vom 20.11.2025 — 4 StR 232/25 (TOA bei sexuellem Missbrauch, friedensstiftender kommunikativer Prozess); offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25.
- Weitere BGH-Rspr. — Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.
