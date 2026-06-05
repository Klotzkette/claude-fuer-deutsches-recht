---
name: laienhilfe-kita-integration-klage
description: "Laienhilfe Kita Integration Klage: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Laienhilfe Kita Integration Klage

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Laienhilfe Kita Integration Klage** im Plugin Fachanwalt Sozialrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `laienhilfe-kita-integration` | Laienverstaendlicher Sozialrechts-Skill zu Kita Integration. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung. |
| `laienhilfe-klage-sozialgericht-einfach` | Laienverstaendlicher Sozialrechts-Skill zu Klage Sozialgericht Einfach. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung. |
| `laienhilfe-konto-pfaendung-sozialleistungen` | Laienverstaendlicher Sozialrechts-Skill zu Konto Pfaendung Sozialleistungen. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung. |
| `laienhilfe-krankengeld-ablauf` | Laienverstaendlicher Sozialrechts-Skill zu Krankengeld Ablauf. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung. |

## Arbeitsweg

Im Plugin Fachanwalt Sozialrecht gilt für **Laienhilfe Kita Integration Klage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `laienhilfe-kita-integration`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Kita Integration. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Kita Integration

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Kita Integration` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Kita Integration** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

## Erst sortieren

1. Welcher Bescheid, Brief, Anruf oder Termin liegt vor?
2. Von welcher Stelle kommt er: Jobcenter, Krankenkasse, Pflegekasse, Rentenversicherung, Sozialamt, Jugendamt, Berufsgenossenschaft oder Sozialgericht?
3. Welches Datum steht auf dem Schreiben und wann ist es angekommen?
4. Was will die Person erreichen: Geld, Leistung, Hilfsmittel, Pflegegrad, GdB, Fristverlaengerung, Akteneinsicht, Eilentscheidung oder einfach Verstehen?
5. Welche Belege gibt es: Atteste, Gutachten, Kontoauszuege, Mietvertrag, Bescheide, Arbeitsunfaehigkeit, Schriftwechsel?

## Arbeitsweise

- Schwierige Woerter erst in einfache Sprache uebersetzen.
- Fristen immer sichtbar ausgeben.
- Zwischen sicher, unklar und zu beweisen unterscheiden.
- Nicht beschwichtigen, wenn ein Eilantrag oder Widerspruch noetig sein kann.
- Keine falschen Versprechen machen.

## Ausgabe

**Kurz erklaert**
- Was bedeutet das Schreiben?
- Was ist das Risiko?
- Was muss als naechstes getan werden?

**Unterlagenliste**
| Unterlage | Warum wichtig? | Vorhanden? |
| --- | --- | --- |
| ... | ... | ... |

**Naechster Schritt**
Formuliere bei Bedarf einen einfachen Brief oder eine E-Mail mit klarer Bitte, Aktenzeichen, Datum, Anlagenliste und Frist.

## Fehler vermeiden

- Keine Frist verstreichen lassen.
- Telefonate direkt mit Datum, Uhrzeit und Namen notieren.
- Nie Originale ohne Kopie abgeben.
- Nicht nur Gefuehle schildern, sondern konkrete Tatsachen und Belege.
- Bei Existenznot, Wohnung, Krankenversicherung, Pflege oder Schulbegleitung immer Eilrechtsschutz mitdenken.

## Qualitaetsgate

Ist die Antwort freundlich, einfach, respektvoll und trotzdem rechtlich praezise? Sind die Begriffe aus SGB und SGG erklaert? Sind Umlaute und Namen sauber uebernommen? Sind offene Punkte sichtbar markiert?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `laienhilfe-klage-sozialgericht-einfach`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Klage Sozialgericht Einfach. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Klage Sozialgericht Einfach

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Klage Sozialgericht Einfach` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Klage Sozialgericht Einfach** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

## Norm- und Praxisanker

- Klagefrist: § 87 SGG – einen Monat ab Zustellung Widerspruchsbescheid; drei Monate bei fehlender/fehlerhafter Belehrung § 66 SGG.
- Klagearten: Anfechtungsklage § 54 Abs. 1 SGG (gegen Verwaltungsakt), Verpflichtungsklage § 54 Abs. 1 (auf Erlass VA), Leistungsklage § 54 Abs. 5 (auf konkrete Leistung), Feststellungsklage § 55 SGG.
- Sachliche Zustaendigkeit: § 51 SGG – Sozialgericht (SG) erstinstanzlich; ortliche Zustaendigkeit § 57 SGG (Wohnsitz Klaeger).
- Klage zu Protokoll: § 90 SGG – Klage auch zur Niederschrift der Geschaeftsstelle moeglich (besondere Erleichterung Selbstvertreter).
- Postulationsfaehigkeit: § 73 SGG – vor SG kein Anwaltszwang (vor LSG/BSG anders, § 73 Abs. 4 SGG).
- Gerichtskostenfreiheit: § 183 SGG – Versicherte, Leistungsempfaenger und Behinderte sind gerichtskostenfrei; nur Anwaltskosten.
- Praxis-Tipp: Klage in einfacher Sprache moeglich – mindestens: "Ich klage gegen den Bescheid vom XX.XX.XXXX, Az. XXX, in Gestalt des Widerspruchsbescheids vom XX.XX.XXXX. Ich beantrage [konkret], weil [Sachverhalt/Argumente]." Belege beifuegen. Bei Selbstvertretung Skill "selbstvertreter-sozialgericht" nutzen; bei Beweisbedarf Antrag nach § 109 SGG (Gutachter eigener Wahl) im Hinterkopf behalten.

## Erst sortieren

1. Welcher Bescheid, Brief, Anruf oder Termin liegt vor?
2. Von welcher Stelle kommt er: Jobcenter, Krankenkasse, Pflegekasse, Rentenversicherung, Sozialamt, Jugendamt, Berufsgenossenschaft oder Sozialgericht?
3. Welches Datum steht auf dem Schreiben und wann ist es angekommen?
4. Was will die Person erreichen: Geld, Leistung, Hilfsmittel, Pflegegrad, GdB, Fristverlaengerung, Akteneinsicht, Eilentscheidung oder einfach Verstehen?
5. Welche Belege gibt es: Atteste, Gutachten, Kontoauszuege, Mietvertrag, Bescheide, Arbeitsunfaehigkeit, Schriftwechsel?

## Arbeitsweise

- Schwierige Woerter erst in einfache Sprache uebersetzen.
- Fristen immer sichtbar ausgeben.
- Zwischen sicher, unklar und zu beweisen unterscheiden.
- Nicht beschwichtigen, wenn ein Eilantrag oder Widerspruch noetig sein kann.
- Keine falschen Versprechen machen.

## Ausgabe

**Kurz erklaert**
- Was bedeutet das Schreiben?
- Was ist das Risiko?
- Was muss als naechstes getan werden?

**Unterlagenliste**
| Unterlage | Warum wichtig? | Vorhanden? |
| --- | --- | --- |
| ... | ... | ... |

**Naechster Schritt**
Formuliere bei Bedarf einen einfachen Brief oder eine E-Mail mit klarer Bitte, Aktenzeichen, Datum, Anlagenliste und Frist.

## Fehler vermeiden

- Keine Frist verstreichen lassen.
- Telefonate direkt mit Datum, Uhrzeit und Namen notieren.
- Nie Originale ohne Kopie abgeben.
- Nicht nur Gefuehle schildern, sondern konkrete Tatsachen und Belege.
- Bei Existenznot, Wohnung, Krankenversicherung, Pflege oder Schulbegleitung immer Eilrechtsschutz mitdenken.

## Qualitaetsgate

Ist die Antwort freundlich, einfach, respektvoll und trotzdem rechtlich praezise? Sind die Begriffe aus SGB und SGG erklaert? Sind Umlaute und Namen sauber uebernommen? Sind offene Punkte sichtbar markiert?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `laienhilfe-konto-pfaendung-sozialleistungen`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Konto Pfaendung Sozialleistungen. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Konto Pfaendung Sozialleistungen

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Konto Pfaendung Sozialleistungen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Konto Pfaendung Sozialleistungen** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

## Erst sortieren

1. Welcher Bescheid, Brief, Anruf oder Termin liegt vor?
2. Von welcher Stelle kommt er: Jobcenter, Krankenkasse, Pflegekasse, Rentenversicherung, Sozialamt, Jugendamt, Berufsgenossenschaft oder Sozialgericht?
3. Welches Datum steht auf dem Schreiben und wann ist es angekommen?
4. Was will die Person erreichen: Geld, Leistung, Hilfsmittel, Pflegegrad, GdB, Fristverlaengerung, Akteneinsicht, Eilentscheidung oder einfach Verstehen?
5. Welche Belege gibt es: Atteste, Gutachten, Kontoauszuege, Mietvertrag, Bescheide, Arbeitsunfaehigkeit, Schriftwechsel?

## Arbeitsweise

- Schwierige Woerter erst in einfache Sprache uebersetzen.
- Fristen immer sichtbar ausgeben.
- Zwischen sicher, unklar und zu beweisen unterscheiden.
- Nicht beschwichtigen, wenn ein Eilantrag oder Widerspruch noetig sein kann.
- Keine falschen Versprechen machen.

## Ausgabe

**Kurz erklaert**
- Was bedeutet das Schreiben?
- Was ist das Risiko?
- Was muss als naechstes getan werden?

**Unterlagenliste**
| Unterlage | Warum wichtig? | Vorhanden? |
| --- | --- | --- |
| ... | ... | ... |

**Naechster Schritt**
Formuliere bei Bedarf einen einfachen Brief oder eine E-Mail mit klarer Bitte, Aktenzeichen, Datum, Anlagenliste und Frist.

## Fehler vermeiden

- Keine Frist verstreichen lassen.
- Telefonate direkt mit Datum, Uhrzeit und Namen notieren.
- Nie Originale ohne Kopie abgeben.
- Nicht nur Gefuehle schildern, sondern konkrete Tatsachen und Belege.
- Bei Existenznot, Wohnung, Krankenversicherung, Pflege oder Schulbegleitung immer Eilrechtsschutz mitdenken.

## Qualitaetsgate

Ist die Antwort freundlich, einfach, respektvoll und trotzdem rechtlich praezise? Sind die Begriffe aus SGB und SGG erklaert? Sind Umlaute und Namen sauber uebernommen? Sind offene Punkte sichtbar markiert?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `laienhilfe-krankengeld-ablauf`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Krankengeld Ablauf. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Krankengeld Ablauf

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Krankengeld Ablauf` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Krankengeld Ablauf** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

## Erst sortieren

1. Welcher Bescheid, Brief, Anruf oder Termin liegt vor?
2. Von welcher Stelle kommt er: Jobcenter, Krankenkasse, Pflegekasse, Rentenversicherung, Sozialamt, Jugendamt, Berufsgenossenschaft oder Sozialgericht?
3. Welches Datum steht auf dem Schreiben und wann ist es angekommen?
4. Was will die Person erreichen: Geld, Leistung, Hilfsmittel, Pflegegrad, GdB, Fristverlaengerung, Akteneinsicht, Eilentscheidung oder einfach Verstehen?
5. Welche Belege gibt es: Atteste, Gutachten, Kontoauszuege, Mietvertrag, Bescheide, Arbeitsunfaehigkeit, Schriftwechsel?

## Arbeitsweise

- Schwierige Woerter erst in einfache Sprache uebersetzen.
- Fristen immer sichtbar ausgeben.
- Zwischen sicher, unklar und zu beweisen unterscheiden.
- Nicht beschwichtigen, wenn ein Eilantrag oder Widerspruch noetig sein kann.
- Keine falschen Versprechen machen.

## Ausgabe

**Kurz erklaert**
- Was bedeutet das Schreiben?
- Was ist das Risiko?
- Was muss als naechstes getan werden?

**Unterlagenliste**
| Unterlage | Warum wichtig? | Vorhanden? |
| --- | --- | --- |
| ... | ... | ... |

**Naechster Schritt**
Formuliere bei Bedarf einen einfachen Brief oder eine E-Mail mit klarer Bitte, Aktenzeichen, Datum, Anlagenliste und Frist.

## Fehler vermeiden

- Keine Frist verstreichen lassen.
- Telefonate direkt mit Datum, Uhrzeit und Namen notieren.
- Nie Originale ohne Kopie abgeben.
- Nicht nur Gefuehle schildern, sondern konkrete Tatsachen und Belege.
- Bei Existenznot, Wohnung, Krankenversicherung, Pflege oder Schulbegleitung immer Eilrechtsschutz mitdenken.

## Qualitaetsgate

Ist die Antwort freundlich, einfach, respektvoll und trotzdem rechtlich praezise? Sind die Begriffe aus SGB und SGG erklaert? Sind Umlaute und Namen sauber uebernommen? Sind offene Punkte sichtbar markiert?

## Krankengeld / Ablauf - Themenspezifika
- **Rechtsgrundlage:** §§ 44-51 SGB V; §§ 46 (Beginn / Ende), 47 (Hoehe), 48 (Hoechstdauer 78 Wochen wegen derselben Krankheit binnen 3 Jahre), 51 (Reha-/Rentenantragsaufforderung).
- **Beginn Krankengeld § 46 SGB V:**
 - Bei Krankenhausaufenthalt: ab Aufnahme.
 - Bei AU: ab Tag nach Feststellung AU (Achtung Aenderung seit 2020 - rueckwirkender Tag möglich); seit 2023 elektronische AU (eAU).
 - **Lueckenlose Krankschreibung** zwingend - **Verlust Krankengeldanspruch** bei Lueckentag (BSG-Linie staendige Rspr; bei Aerztewechsel insbesondere kritisch).
 - **Lueckenfueller-Frist:** AU-Folgebescheinigung muss spaetestens am Werktag nach Ende der vorherigen AU erfolgen.
- **Hoehe Krankengeld § 47 SGB V:**
 - 70 % des Bruttoarbeitsentgelts, max. 90 % des Nettoarbeitsentgelts.
 - Hoechstrenze § 47 VI SGB V (Beitragsbemessungsgrenze).
 - Einmalzahlungen anrechnen § 23a SGB IV.
- **Hoechstbezugsdauer § 48 SGB V:** 78 Wochen (546 Tage) wegen derselben Krankheit binnen 3 Jahre ("Blockfrist").
- **Aussteuerung Krankenkasse § 51 SGB V:**
 - Aufforderung Reha-/Rentenantrag innerhalb 10 Wochen ab Aufforderung; bei Nichtantrag Wegfall Krankengeld.
 - Sehr kritisch: rechtzeitige Anwaltsberatung; ggf. Widerspruch gegen Aufforderung; Beratung DRV vor Rentenantrag.
- **Anschlussleistungen:**
 - **Nahtlosigkeitsregelung § 145 SGB III:** ALG bei Restleistungsfaehigkeit unter 15 h/Woche bis Rentenbescheid.
 - **EM-Rente § 43 SGB VI** bei dauerhafter Erwerbsminderung.
 - **Buergergeld** subsidiaer.
- **Praxis-Tipp:** AU-Bescheinigungen immer am letzten Tag der AU verlaengern (besser einen Tag vorher); nie auf den Postweg verlassen; eAU bei Kasse pruefen lassen; Aerztewechsel mit aktueller Information vermeiden Lueckentage.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
