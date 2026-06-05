---
name: cap-table-client-explainer
description: "CAP Table Client Explainer: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# CAP Table Client Explainer

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **CAP Table Client Explainer** im Plugin Corporate law in legal English. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cap-table-gesellschafterliste` | Erklaert und prueft Cap Table, Gesellschafterliste, wirtschaftliche Beteiligung, Stammkapital, Geschaeftsanteile, Verwässerung und Registerrealitaet. |
| `client-explainer-legal-english` | Erstellt mandantenfreundliche Erklaerungen von Corporate-Legal-English-Begriffen ohne Jargon, mit Beispielen, Risiken und naechsten Entscheidungen. |

## Arbeitsweg

Im Plugin Corporate law in legal English gilt für **CAP Table Client Explainer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cap-table-gesellschafterliste`

**Fokus:** Erklaert und prueft Cap Table, Gesellschafterliste, wirtschaftliche Beteiligung, Stammkapital, Geschaeftsanteile, Verwässerung und Registerrealitaet.

# Cap Table statt Gesellschafterliste

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Cap Table statt Gesellschafterliste` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernunterscheidung

Ein Cap Table ist eine wirtschaftliche Beteiligungsübersicht. Die Gesellschafterliste nach § 40 GmbHG ist ein registerbezogenes Dokument mit rechtlicher Legitimationswirkung nach § 16 GmbHG. Beide können ähnlich aussehen, beantworten aber verschiedene Fragen.

## Prüffragen

1. Ist die Gesellschaft GmbH, UG, AG, SE, KG oder Auslandsgesellschaft?
2. Geht es um rechtliche Inhaberschaft oder wirtschaftliche Verwässerung?
3. Sind VSOP/ESOP, Wandeldarlehen, SAFE-ähnliche Instrumente oder Optionen enthalten?
4. Gibt es mehrere Geschäftsanteile je Gesellschafter?
5. Stimmen Nennbeträge, laufende Nummern und Prozentangaben mit der Gesellschafterliste überein?

## Matrix

| Dokument | Zeigt | Zeigt nicht zwingend |
| --- | --- | --- |
| Gesellschafterliste | formale Geschäftsanteile, Nennbeträge, laufende Nummern | Optionen, VSOP, wirtschaftliche Nebenrechte, fully diluted view |
| Cap Table | aktuelle und hypothetische Beteiligung, Verwässerung, Investor Economics | registerrechtliche Legitimation |
| SHA | schuldrechtliche Rechte und Pflichten | automatisch Registerwirkung |

## Anfängerfehler

- Cap Table als offizielle Gesellschafterliste behandeln.
- Fully diluted Prozentwerte in Registerkontext übernehmen.
- Nennbetrag und wirtschaftliche Beteiligung vermischen.
- VSOP wie echte Anteile behandeln.

## Output

- Abgleichstabelle Cap Table/Gesellschafterliste.
- Liste fehlender Annahmen.
- Warnungen für Partnerbriefing.
- Erklärung für Mandanten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `client-explainer-legal-english`

**Fokus:** Erstellt mandantenfreundliche Erklaerungen von Corporate-Legal-English-Begriffen ohne Jargon, mit Beispielen, Risiken und naechsten Entscheidungen.

# Client Explainer

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Client Explainer` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Ziel

Der Mandant soll die wirtschaftliche und rechtliche Wirkung eines Begriffs verstehen, ohne mit Kanzleijargon erschlagen zu werden.

## Struktur

1. Begriff in einem Satz.
2. Warum er im Deal wichtig ist.
3. Was er für unsere Partei bedeutet.
4. Welche Entscheidung der Mandant treffen muss.
5. Welche Risiken wir noch prüfen.

## Stil

- Kurze Sätze.
- Keine akademische Begriffspracht.
- Englischen Begriff nennen, aber sofort erklären.
- Zahlenbeispiel verwenden, wenn es um Economics geht.
- Keine Scheinsicherheit.

## Output

- E-Mail-Entwurf.
- Kurznotiz für Call.
- Fragenliste für Mandanten.
- Ampel: akzeptieren, verhandeln, ablehnen, prüfen.

## Didaktischer Arbeitsmodus

- Erklaere jeden Begriff zweispurig: englischer Praxisbegriff, naheliegende deutsche Entsprechung und warum beides nicht deckungsgleich sein muss.
- Arbeite immer an der Dokumentstelle: Term Sheet, SHA, SPA, Satzung, Gesellschafterliste, Cap Table, Board Paper oder Closing Checklist.
- Gib eine Anfängerfassung in klarer Sprache und eine Praxisfassung fuer die Partnerin oder den Mandanten.
- Wenn ein common-law-Begriff nach deutschem Recht verwendet wird, markiere Auslegungsrisiko, deutsches Ersatzkonzept und Formulierungsvorschlag.

## Ausgabeformat

1. Kurzantwort.
2. Begriff entschluesselt.
3. Deutsche Rechtsfunktion.
4. Wirtschaftlicher Effekt.
5. Typische Fallen.
6. Naechster Drafting- oder Review-Schritt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
