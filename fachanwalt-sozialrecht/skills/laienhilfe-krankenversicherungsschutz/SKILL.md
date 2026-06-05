---
name: laienhilfe-krankenversicherungsschutz
description: "Laienhilfe Krankenversicherungsschutz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Laienhilfe Krankenversicherungsschutz

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Laienhilfe Krankenversicherungsschutz** im Plugin Fachanwalt Sozialrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `laienhilfe-krankenversicherungsschutz` | Laienverstaendlicher Sozialrechts-Skill zu Krankenversicherungsschutz. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung. |
| `laienhilfe-merkzeichen` | Laienverstaendlicher Sozialrechts-Skill zu Merkzeichen. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen fuer Behoerde, Widerspruch, Klage oder Beratung. |
| `laienhilfe-muendliche-verhandlung-sg` | Laienverstaendlicher Sozialrechts-Skill zu Muendliche Verhandlung Sg. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen fuer Behoerde, Widerspruch, Klage oder Beratung. |
| `laienhilfe-mutterschaft-elterngeld-schnittstelle` | Laienverstaendlicher Sozialrechts-Skill zu Mutterschaft Elterngeld Schnittstelle. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen fuer Behoerde, Widerspruch, Klage oder Beratung. |

## Arbeitsweg

Im Plugin Fachanwalt Sozialrecht gilt für **Laienhilfe Krankenversicherungsschutz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `laienhilfe-krankenversicherungsschutz`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Krankenversicherungsschutz. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen für Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Krankenversicherungsschutz

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Krankenversicherungsschutz` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Krankenversicherungsschutz** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

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

## 2. `laienhilfe-merkzeichen`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Merkzeichen. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen fuer Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Merkzeichen

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Merkzeichen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Merkzeichen** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

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

## Merkzeichen - Themenspezifika
- **Rechtsgrundlage:** § 229 SGB IX (Merkzeichen-Voraussetzungen); § 3 Schwerbehindertenausweisverordnung (SchwbAwV); VersorgungsmedizinV / VersorgungsmedizinG.
- **Wichtige Merkzeichen mit Voraussetzungen und Vorteilen:**
 - **G (Gehbehinderung):** erhebliche Beeintraechtigung Bewegungsfaehigkeit im Strassenverkehr; in Behinderungsgrad-Massstaeben 50/50; Vorteil: oeffentlicher Nahverkehr unentgeltlich (mit Wertmarke EUR 91 / Jahr, ermaessigt EUR 46) bzw. KFZ-Steuerermaessigung 50 %.
 - **aG (aussergewoehnliche Gehbehinderung):** dauerhafte Mobilitaetseinschraenkung erheblich; Voraussetzung u. a. Querschnittlaehmung, beidseitige Beinamputation, doppelte Oberschenkelamputation, vergleichbare schwerere Faelle (VersMedV strenge BSG-Linie); Vorteil: Behindertenparkplatz; KFZ-Steuerbefreiung.
 - **B (Begleitperson):** Notwendigkeit staendiger Begleitung; Begleitperson reist im oeffentlichen Verkehr kostenlos mit.
 - **H (Hilflosigkeit):** dauerhaft hilflos im taeglichen Leben (vergleichbar Pflegegrad 4-5); KFZ-Steuerbefreiung, hoehere Pauschbetraege.
 - **Bl (Blindheit):** mehr als 1/50 Sehkraft beidaeugig; Landesblindengeld; KFZ-Steuerbefreiung.
 - **Gl (Gehoerlosigkeit):** Hoer-/Sprachverlust seit dem Spracherwerb; Vorteil Telefonpauschale.
 - **RF (Rundfunkbeitragsbefreiung):** wegen Schwerbehinderung Teilhabe an Veranstaltungen ausgeschlossen.
 - **TBl (Taubblindheit):** Kombination Hoer- und Sehbehinderung; besondere Foerderungen.
- **Versorgungsmedizinische Grundsaetze (VersMedV / Anlage 2):** Mindestkriterien je Merkzeichen; behandelnder Arzt mit konkreten Funktionsbefunden untermauern.
- **Antrag / Widerspruch:**
 - **Antrag** beim Versorgungsamt; **Aenderungsantrag** bei Verschlechterung.
 - **Widerspruch § 84 SGG:** 1 Monat; Klage SG 1 Monat.
 - **§ 109 SGG-Wahl-Sachverstaendiger** bei Klage.
- **Praxis-Tipp:** Fokus auf Funktionsbeeintraechtigung im Alltag (Gehstrecke konkret in Metern; Hilfsmittelbedarf; Begleitnotwendigkeit). Bei aG-Verweigerung: BSG-Linie zur Gleichstellung (vergleichbare schwerwiegende Faelle); Stellungnahme Facharzt unverzichtbar.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `laienhilfe-muendliche-verhandlung-sg`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Muendliche Verhandlung Sg. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen fuer Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Muendliche Verhandlung Sg

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Muendliche Verhandlung Sg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Muendliche Verhandlung Sg** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

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

## 4. `laienhilfe-mutterschaft-elterngeld-schnittstelle`

**Fokus:** Laienverstaendlicher Sozialrechts-Skill zu Mutterschaft Elterngeld Schnittstelle. Erklaert Bescheid, Frist, Unterlagen, typische Fehler, naechste Schritte und einfache Formulierungen fuer Behoerde, Widerspruch, Klage oder Beratung.

# Laienhilfe: Mutterschaft Elterngeld Schnittstelle

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Laienhilfe: Mutterschaft Elterngeld Schnittstelle` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum es geht

Dieser Skill erklaert **Mutterschaft Elterngeld Schnittstelle** so, dass auch Menschen ohne juristische Vorkenntnisse handlungsfaehig werden. Er ersetzt keine Beratung, verhindert aber typische Fehler: Fristen uebersehen, falsche Stelle anschreiben, Unterlagen ungeordnet schicken, zu viel oder zu wenig sagen, Begriffe missverstehen.

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
