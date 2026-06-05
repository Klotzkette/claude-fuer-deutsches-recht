---
name: vowi-tempomessverfahren-bussgeldbescheid
description: "Vowi Tempomessverfahren Bussgeldbescheid: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vowi Tempomessverfahren Bussgeldbescheid

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vowi Tempomessverfahren Bussgeldbescheid** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vowi-tempomessverfahren-fehlerquellen-spezial` | Spezialfall Tempomessverfahren und Fehlerquellen: Poliscan, ES 3.0, ES 8.0, Riegl, Eichschein, Verkehrsfehlergrenzen. Pruefraster fuer Verteidiger und Sachverstaendiger. |
| `spezial-bussgeldbescheid-tatbestand-beweis-und-belege` | Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `verkehrsowi-anhoerung-bussgeldbescheid` | Anhoerung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhoerungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhoerung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch 2-Wochen-Frist). Prüfraster: Anhoerungsbogen zurücksenden oder nicht, Schweige-Empfehlung, Frist ab Zustellung. Output Empfehlungsschreiben Mandant, Muster Schweigeerklarung, Einspruchs-Template. Abgrenzung: Einspruch und Frist siehe verkehrsowi-fristen-einspruch; Messverfahren-Angriff siehe verkehrsowi-beweisverwertung-standardisiert. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Vowi Tempomessverfahren Bussgeldbescheid**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vowi-tempomessverfahren-fehlerquellen-spezial`

**Fokus:** Spezialfall Tempomessverfahren und Fehlerquellen: Poliscan, ES 3.0, ES 8.0, Riegl, Eichschein, Verkehrsfehlergrenzen. Pruefraster fuer Verteidiger und Sachverstaendiger.

# VOWi: Tempomessverfahren

## Spezialwissen: VOWi: Tempomessverfahren
- **Spezialgegenstand:** VOWi: Tempomessverfahren / vowi tempomessverfahren fehlerquellen spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ES.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `spezial-bussgeldbescheid-tatbestand-beweis-und-belege`

**Fokus:** Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage / bussgeldbescheid tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** OWiG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bussgeldbescheid** prüfen.
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

## Qualitätsanker: Messdaten, Messakte und faires Verfahren

- **Verifizierter Leitanker:** BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Verfahren zugänglich sein, wenn sie konkret und rechtzeitig verlangt werden.
- **Praktische Übersetzung:** Niemals nur pauschal „Messung bestreiten“. Immer präzise anfordern: Falldatei/Rohmessdaten, Messreihe soweit vorhanden und relevant, Token/Passwort, Eichschein, Gebrauchsanweisung, Schulungsnachweise, Wartungs-/Reparaturhinweise, Standort-/Beschilderungsunterlagen, Statistik und Auswerteprotokoll.
- **Angriffslinie:** Standardisiertes Messverfahren ist eine Beweiserleichterung, kein Denkverbot. Der Skill muss aus Unterlagen konkrete Einwendungen machen: falsches Gerät, fehlende Eichung, fehlerhafte Bedienung, unklare Fahreridentität, unplausible Messreihe, fehlende Einsicht, Frist-/Gehörsproblem.
- **Output-Pflicht:** Immer ein kurzes Anforderungsschreiben oder einen gerichtsfesten Begründungsbaustein anbieten, wenn Akteneinsicht, Messunterlagen oder Fristwahrung Thema sind.

## 3. `verkehrsowi-anhoerung-bussgeldbescheid`

**Fokus:** Anhoerung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhoerungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhoerung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch 2-Wochen-Frist). Prüfraster: Anhoerungsbogen zurücksenden oder nicht, Schweige-Empfehlung, Frist ab Zustellung. Output Empfehlungsschreiben Mandant, Muster Schweigeerklarung, Einspruchs-Template. Abgrenzung: Einspruch und Frist siehe verkehrsowi-fristen-einspruch; Messverfahren-Angriff siehe verkehrsowi-beweisverwertung-standardisiert.

# Anhoerung und Bussgeldbescheid — §§ 55 und 66 OWiG

## Triage zu Beginn

1. **Anhoerungsbogen erhalten?** — Unterschied zum Bussgeldbescheid: Anhoerung ist Vorstadium; kein Bussgeldbescheid noch offen.
2. **Schweigen oder Stellungnahme?** — § 55 OWiG: Betroffener muss auf Anhoerung nicht reagieren; Schweigen kann nicht nachteilig gewertet werden.
3. **Fahreridentifikation?** — Betroffener muss sich nicht als Fahrender identifizieren; Halter-Auskunft ist OWi-Pflicht (§ 31a StVG bei Halter-Anfrage), aber Fahrernennung ist freiwillig.
4. **Bussgeldbescheid bereits erlassen?** — Wenn ja: Einspruchsfrist 2 Wochen ab Zustellung (§ 67 Abs. 1 OWiG) pruefen.
5. **Zustellungsfiktion pruefen?** — § 33 Abs. 1 OWiG i.V.m. §§ 177-182 ZPO; Einwurf-Einschreiben.

## Zentrale Normen

- **§ 55 OWiG** — Anhoerung des Betroffenen: Behörde muss hoeren; Betroffener muss nicht antworten
- **§ 55 Abs. 1 OWiG** — Schweigen ist nicht zu seinen Ungunsten zu verwenden
- **§ 66 OWiG** — Inhalt des Bussgeldbescheidss; Pflichtangaben nach § 66 Abs. 1 Nr. 1-7 OWiG
- **§ 67 Abs. 1 OWiG** — Einspruch: 2 Wochen ab Zustellung des Bussgeldbescheids
- **§ 67 Abs. 2 OWiG** — Beschraenkter Einspruch (nur Rechtsfolgen) moeglich
- **§ 33 OWiG i.V.m. §§ 177-182 ZPO** — Zustellungsvorschriften
- **§ 31a StVG** — Recht auf Fahrerauskunft (nur Halter-Auskunft, nicht Fahrernennung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anhoerungsbogen — Strategie

```
Anhoerungsbogen erhalten:
├─ EMPFEHLUNG: Nicht ausfullen, nicht zuruecksenden (Schweigen § 55 OWiG)
├─ Ausnahme: Fahreridentifikation offensichtlich aus anderen Quellen bekannt?
│ └─ Dann kann Einlassung zur Sache sinnvoll sein (selten)
└─ FALLFALLE: Unterschrift unter "Ich war der Fahrzeugfuehrer"
 → gilt als Gestaendnis der Fahrereigenschaft → nicht unterschreiben!
```

## Bussgeldbescheid — Pflichtinhalt nach § 66 OWiG

```
□ Name und Anschrift des Betroffenen (§ 66 Abs. 1 Nr. 1)
□ Tathandlung mit Zeit und Ort (§ 66 Abs. 1 Nr. 2)
□ Gesetzliche Merkmale der OWi (§ 66 Abs. 1 Nr. 3)
□ Angabe der verletzten Vorschrift (§ 66 Abs. 1 Nr. 4)
□ Hoehe der Geldbusse (§ 66 Abs. 1 Nr. 5)
□ Hinweis auf Fahrverbot wenn verhaengt (§ 66 Abs. 1 Nr. 5)
□ Belehrung ueber Einspruchsrecht (§ 66 Abs. 1 Nr. 7)

Fehlt ein Pflichtinhalt: Einspruch mit formaler Ruege!
```

## Einspruchsschrift-Template

```
An die [Bussgeldstelle] / Amtsgericht [ORT]
Az.: [AKTENZEICHEN]

Einspruch nach § 67 OWiG

Namens des Betroffenen [NAME] lege ich gegen den Bussgeldbescheid
vom [DATUM], zugestellt am [DATUM], fristgerecht

Einspruch

ein.

[Optional: Der Einspruch wird auf die Rechtsfolgen beschraenkt.]

Ich bitte um Uebersendung der vollstaendigen Verfahrensakte
einschliesslich Messakte.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Anhoerungsbogen nicht selbst ausfullen lassen — Schweigerecht empfehlen.
- Einspruchsfrist 2 Wochen ab Zustellung (§ 67 OWiG) — sofort notieren.
- Bussgeldbescheid auf Pflichtinhalt nach § 66 OWiG pruefen.
- Anwaltliche Endkontrolle bei Einspruchsformulierung.
