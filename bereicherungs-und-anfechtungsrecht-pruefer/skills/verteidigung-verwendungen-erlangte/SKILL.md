---
name: verteidigung-verwendungen-erlangte
description: "Verteidigung Verwendungen Erlangte: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verteidigung Verwendungen Erlangte

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Verteidigung Verwendungen Erlangte** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verteidigung-gegen-bereicherungsklage` | Dieses Fachmodul greift, wenn eine Bereicherungsklage systematisch abgewehrt werden soll. Normen: §§ 814 und 815 BGB; § 817 BGB; § 818 Abs. 3 BGB; § 819 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; Halte Beweisbedarf und offene Tatsachen sichtbar; Formuliere Hilfspositionen für Wertersatz, Saldo und Zug um Zug. Output: Verteidigungsschriftsatz-Bausteine mit Einreden-Reihenfolge. Abgrenzung: nicht aktive Bereicherungsklage selbst. |
| `verwendungen-auf-das-erlangte` | Dieses Fachmodul greift, wenn Aufwendungen auf den erhaltenen Gegenstand als Abzug oder Gegenrecht auftauchen. Normen: §§ 994 bis 1003 BGB; § 818 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und ersparte Aufwendungen vor § 818 Abs. 3 BGB; Bewerte Dienstleistung und Gebrauchsvorteil objektiv nach Markt- oder Nutzungswert. Output: Verwendungs-Berechnung mit notwendigen, nützlichen und Luxusverwendungen. Abgrenzung: nicht EBV-Verwendungsersatz §§ 994 ff. BGB ohne Bereicherungsbezug. |
| `weichenstellung-bereicherung-oder-anfechtung` | Triage-Entscheidung: welcher Regelungskreis ist einschlägig - Bereicherungsrecht, außerinsolvenzliche Anfechtung oder Insolvenzanfechtung. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Rechtsgrundmangel, Insolvenzeröffnung, vollstreckbarer Titel. Output: Weiterleitungsmatrix zum richtigen Prüf-Skill. Abgrenzung: kein inhaltlicher Anspruchsgutachter. |
| `weitergabe-und-822-verteidigung` | Dieses Fachmodul greift, wenn ein erlangter Vorteil unentgeltlich an Dritte weitergegeben wurde. Normen: § 822 BGB; § 818 Abs. 3 BGB. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der verletzten Position; Ordne Nutzung, Verfügung oder Weitergabe der passenden Anspruchsgrundlage zu. Output: Prüfergebnis § 822 BGB mit Subsidiaritätsanalyse und Verteidigungsbausteinen. Abgrenzung: nicht Direktanspruch gegen Erstempfänger § 812 BGB. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Verteidigung Verwendungen Erlangte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verteidigung-gegen-bereicherungsklage`

**Fokus:** Dieses Fachmodul greift, wenn eine Bereicherungsklage systematisch abgewehrt werden soll. Normen: §§ 814 und 815 BGB; § 817 BGB; § 818 Abs. 3 BGB; § 819 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; Halte Beweisbedarf und offene Tatsachen sichtbar; Formuliere Hilfspositionen für Wertersatz, Saldo und Zug um Zug. Output: Verteidigungsschriftsatz-Bausteine mit Einreden-Reihenfolge. Abgrenzung: nicht aktive Bereicherungsklage selbst.

# Verteidigung gegen Bereicherungsklage

## Einsatzbereich

Dieses Fachmodul greift, wenn eine Bereicherungsklage systematisch abgewehrt werden soll. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welches praktische Ziel soll der Output erreichen?
2. Welche Tatsachen sind beweisbar und welche offen?
3. Welche Einreden muss der Entwurf antizipieren?
4. Welche Haupt-, Hilfs- oder Zug-um-Zug-Anträge sind nötig?
5. Welche Aussage darf ohne verifizierte Grundlage nicht getroffen werden?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview.
- Halte Beweisbedarf und offene Tatsachen sichtbar.
- Formuliere Hilfspositionen für Wertersatz, Saldo und Zug um Zug.
- Vermeide ungeprüfte Fundstellen und scheinpräzise Beträge.
- Gib am Ende eine knappe Risikoeinschätzung aus.

## Typische Fehler

- Rechtliches Ergebnis ohne Tatsachenbasis ausgeben.
- Hilfsanträge und Einreden vergessen.
- Unverifizierte Zitate oder Scheinsicherheit verwenden.

## Arbeitsausgabe

| Punkt | Ergebnis | Belegbedarf |
|---|---|---|
| Anspruchsziel | [...] | [...] |
| beteiligte Personen | [...] | [...] |
| Vermögensvorteil | [...] | [...] |
| Zweck/Zurechnung | [...] | [...] |
| Rechtsgrund/Behaltensgrund | [...] | [...] |
| § 818 BGB | [...] | [...] |
| Einreden/Spezialregime | [...] | [...] |
| vorläufiges Ergebnis | [...] | [...] |

## Mini-Check vor Output

- Kein Direktanspruch ohne begründete Zurechnung.
- Kein Wertersatz ohne Bewertungsmethode.
- Keine Entreicherung ohne konkreten Vermögensweg.
- Keine Saldierung ohne beiderseitige Leistungstabelle.
- Offene Tatsachen bleiben als offen markiert.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `verwendungen-auf-das-erlangte`

**Fokus:** Dieses Fachmodul greift, wenn Aufwendungen auf den erhaltenen Gegenstand als Abzug oder Gegenrecht auftauchen. Normen: §§ 994 bis 1003 BGB; § 818 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und ersparte Aufwendungen vor § 818 Abs. 3 BGB; Bewerte Dienstleistung und Gebrauchsvorteil objektiv nach Markt- oder Nutzungswert. Output: Verwendungs-Berechnung mit notwendigen, nützlichen und Luxusverwendungen. Abgrenzung: nicht EBV-Verwendungsersatz §§ 994 ff. BGB ohne Bereicherungsbezug.

# Verwendungen auf das Erlangte

## Einsatzbereich

Dieses Fachmodul greift, wenn Aufwendungen auf den erhaltenen Gegenstand als Abzug oder Gegenrecht auftauchen. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Was war ursprünglich erlangt und was ist heute noch vorhanden?
2. Welche Nutzungen, Surrogate, Erlöse oder Ersatzforderungen gibt es?
3. Welche eigenen Ausgaben wurden erspart?
4. Wann traten Verlust, Verbrauch, Kenntnis und Rechtshängigkeit ein?
5. Welche Bewertungsmethode ist belegbar?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Erstelle eine Vermögensbilanz statt einer Gegenstandsliste.
- Prüfe Nutzungen, Surrogate und ersparte Aufwendungen vor § 818 Abs. 3 BGB.
- Bewerte Dienstleistung und Gebrauchsvorteil objektiv nach Markt- oder Nutzungswert.
- Ordne Wertverluste nach Risiko, Kenntnis und Rechtshängigkeit zu.
- Verlange substantiierte Belege für Entreicherung.

## Verwendungsarten

| Art | Behandlung |
|---|---|
| notwendige Erhaltung | möglicher Gegenanspruch oder Saldoposten |
| werterhöhende Verbesserung | nur im Umfang fortwirkender Wertsteigerung relevant |
| Luxusaufwand | regelmäßig eigenes Risiko |
| Aufwand zur Nutzung | bei Gebrauchsvorteil gegenrechnen oder gesondert prüfen |
| Aufwand nach Kenntnis | strenger prüfen |
| Aufwand in Spezialregime | EBV, Rücktritt, Mietrecht oder Vertragsrecht vorrangig |

Verwendungen mindern den Herausgabeanspruch nicht automatisch. Sie können Gegenrecht, Zurückbehaltung, Saldoposten oder unbeachtlich sein.

## Typische Fehler

- "Geld ist weg" als Ergebnis genügen lassen.
- Surrogate und Ersparnisse übersehen.
- Zinsen, Nutzungen und Wertersatz doppelt zählen.

## Arbeitsausgabe

| Punkt | Ergebnis | Belegbedarf |
|---|---|---|
| Anspruchsziel | [...] | [...] |
| beteiligte Personen | [...] | [...] |
| Vermögensvorteil | [...] | [...] |
| Zweck/Zurechnung | [...] | [...] |
| Rechtsgrund/Behaltensgrund | [...] | [...] |
| § 818 BGB | [...] | [...] |
| Einreden/Spezialregime | [...] | [...] |
| vorläufiges Ergebnis | [...] | [...] |

## Verwendungs-Output

| Verwendung | notwendig/nützlich/Luxus | Wertsteigerung | prozessuale Behandlung |
|---|---|---|---|
| [...] | [...] | [...] EUR | Abzug / Gegenanspruch / Zug um Zug / nein |

## Mini-Check vor Output

- Kein Direktanspruch ohne begründete Zurechnung.
- Kein Wertersatz ohne Bewertungsmethode.
- Keine Entreicherung ohne konkreten Vermögensweg.
- Keine Saldierung ohne beiderseitige Leistungstabelle.
- Offene Tatsachen bleiben als offen markiert.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `weichenstellung-bereicherung-oder-anfechtung`

**Fokus:** Triage-Entscheidung: welcher Regelungskreis ist einschlägig - Bereicherungsrecht, außerinsolvenzliche Anfechtung oder Insolvenzanfechtung. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Rechtsgrundmangel, Insolvenzeröffnung, vollstreckbarer Titel. Output: Weiterleitungsmatrix zum richtigen Prüf-Skill. Abgrenzung: kein inhaltlicher Anspruchsgutachter.

# Weichenstellung: Bereicherung oder Anfechtung?

## Triage — kläre vor der Weichenstellung

1. Besteht ein wirksamer Rechtsgrund für die Vermögensverschiebung (wirksamer Vertrag, gesetzliche Pflicht), oder fehlt er (nichtig, weggefallen)?
2. Ist über das Vermögen des Schuldners ein Insolvenzverfahren eröffnet oder beantragt?
3. Hat der Gläubiger einen vollstreckbaren Titel gegen den Schuldner (§ 2 AnfG)?
4. Hat die Zwangsvollstreckung nicht zur Befriedigung geführt (Fruchtlosigkeit als AnfG-Voraussetzung)?
5. Besteht noch Eigentum des Anspruchstellers am streitigen Gegenstand (§ 985 BGB vorrangig)?

## Zentrale Normen

§ 812 Abs. 1 BGB (Leistungskondiktion: kein Rechtsgrund) — §§ 129 ff. InsO (Insolvenzanfechtung: Verfahren eröffnet) — §§ 1–13 AnfG (Gläubigeranfechtung: Titel vorhanden, kein Insolvenzverfahren) — § 985 BGB (Vindikation: Eigentum noch vorhanden) — § 17 InsO (Zahlungsunfähigkeit) — § 2 AnfG (Titel + Fruchtlosigkeit) — § 826 BGB (sittenwidrige Schädigung, Konkurrenz)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Weichenstellungs-Schema

### Frage 1: Liegt ein Rechtsgrund für die Vermögensverschiebung vor?

**Kein Rechtsgrund** (Vertrag nichtig, nie zustande gekommen, weggefallen):
→ Bereicherungsrecht §§ 812 ff. BGB.
→ Skill: `leistungskondiktion-grundtatbestand-812-i-1-alt-1`

**Rechtsgrund vorhanden** (wirksamer Vertrag, gesetzliche Pflicht):
→ Weiter zu Frage 2.

### Frage 2: Ist ein Insolvenzverfahren eröffnet oder beantragt?

**Insolvenzverfahren eröffnet oder Antrag gestellt:**
→ Insolvenzanfechtung §§ 129 ff. InsO.
→ Skill: `inso-grundtatbestand-129-gläubigerbenachteiligung`

**Kein Insolvenzverfahren:**
→ Weiter zu Frage 3.

### Frage 3: Liegt ein vollstreckbarer Titel vor?

**Vollstreckbarer Titel vorhanden** + fruchtlose Vollstreckung:
→ AnfG-Anfechtung (§ 2 AnfG).
→ Skill: `anfg-grundtatbestand-und-anfechtungsberechtigte`

**Kein Vollstreckungstitel:**
→ AnfG nicht unmittelbar anwendbar; Klage auf Leistung oder Feststellung prüfen.

## Kombinationen und Besonderheiten

- § 812 BGB und AnfG können nebeneinander stehen, wenn der Rechtsgrund nachträglich entfällt.
- Mit Insolvenzverfahren verdrängt § 129 InsO den AnfG-Pfad.
- § 133 InsO kann mit § 826 BGB konkurrieren.
- Bei § 812 BGB zuerst klären, ob es um Leistung, Eingriff, Verfügung eines Nichtberechtigten oder Mehrpersonenabwicklung geht.
- Bei gegenseitigen Verträgen immer Saldo und Zug-um-Zug-Fragen mitdenken.
- Bei Mehrpersonenfällen nicht vom Zahlungsempfänger automatisch auf den richtigen Anspruchsgegner schließen.

## Bereicherungsrechtliche Feinsortierung

| Befund | Weiterer Skill |
|---|---|
| Leistung an den Beklagten, Rechtsgrund fehlt | `leistungskondiktion-grundtatbestand-812-i-1-alt-1` |
| unklarer Rechts- oder Behaltensgrund | `rechtsgrund-und-behaltensgrund-prüfen` |
| Zweckabrede oder Zweckverfehlung | `zweckverfehlung-und-kondiktionszweck` |
| Zahlungskette, Anweisung, Drittleistung | `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` |
| nichtiger gegenseitiger Vertrag | `saldotheorie-rueckabwicklung-nichtiger-vertraege` |
| Eingriff in zugewiesene Nutzung | `eingriffskondiktion-zuweisungsgehalt` |
| Streit um Entreicherung/Wertersatz | `umfang-der-herausgabe-818-bgb-und-entreicherung` |

## Merksatz

Kein Rechtsgrund → Bereicherungsrecht.
Rechtsgrund + kein Insolvenzverfahren + Titel → AnfG.
Rechtsgrund + Insolvenzverfahren → InsO-Anfechtung.

## Output-Template

**Weichenstellung: Bereicherung oder Anfechtung?**

Sachverhalt (kurz): [...]

| Frage | Antwort | Pfad |
|---|---|---|
| Rechtsgrund vorhanden? | nein → | § 812 BGB |
| Rechtsgrund vorhanden? | ja → Frage 2 | |
| Insolvenzverfahren eröffnet/beantragt? | ja → | §§ 129 ff. InsO |
| Kein Insolvenzverfahren, Titel vorhanden? | ja + fruchtlos → | AnfG (§ 2) |
| Eigentum noch vorhanden? | ja → | § 985 BGB (vorrangig) |

**Empfohlener Regelungskreis:** [...] → Weiter zu Skill: [...]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 4. `weitergabe-und-822-verteidigung`

**Fokus:** Dieses Fachmodul greift, wenn ein erlangter Vorteil unentgeltlich an Dritte weitergegeben wurde. Normen: § 822 BGB; § 818 Abs. 3 BGB. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der verletzten Position; Ordne Nutzung, Verfügung oder Weitergabe der passenden Anspruchsgrundlage zu. Output: Prüfergebnis § 822 BGB mit Subsidiaritätsanalyse und Verteidigungsbausteinen. Abgrenzung: nicht Direktanspruch gegen Erstempfänger § 812 BGB.

# Weitergabe und § 822 BGB Verteidigung

## Einsatzbereich

Dieses Fachmodul greift, wenn ein erlangter Vorteil unentgeltlich an Dritte weitergegeben wurde. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welche Rechtsposition weist den wirtschaftlichen Nutzen zu?
2. Hat der Gegner diese Position ohne Leistung des Anspruchstellers genutzt?
3. Gab es Lizenz, Gestattung oder gesetzliche Erlaubnis?
4. Ist § 816 BGB oder § 822 BGB spezieller?
5. Wie wird der objektive Nutzungs- oder Lizenzwert bestimmt?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt.
- Bestimme den Zuweisungsgehalt der verletzten Position.
- Ordne Nutzung, Verfügung oder Weitergabe der passenden Anspruchsgrundlage zu.
- Bewerte nach objektivem Markt-, Lizenz- oder Erlöswert.
- Trenne Bereicherung von Schaden, Gewinnabschöpfung und Unterlassung.

## Typische Fehler

- Alt. 2 als Auffangtatbestand ohne Zuweisungsgehalt nutzen.
- Schadensersatz und Bereicherung vermischen.
- Lizenzwert ohne Methode schätzen.

## Arbeitsausgabe

| Punkt | Ergebnis | Belegbedarf |
|---|---|---|
| Anspruchsziel | [...] | [...] |
| beteiligte Personen | [...] | [...] |
| Vermögensvorteil | [...] | [...] |
| Zweck/Zurechnung | [...] | [...] |
| Rechtsgrund/Behaltensgrund | [...] | [...] |
| § 818 BGB | [...] | [...] |
| Einreden/Spezialregime | [...] | [...] |
| vorläufiges Ergebnis | [...] | [...] |

## Mini-Check vor Output

- Kein Direktanspruch ohne begründete Zurechnung.
- Kein Wertersatz ohne Bewertungsmethode.
- Keine Entreicherung ohne konkreten Vermögensweg.
- Keine Saldierung ohne beiderseitige Leistungstabelle.
- Offene Tatsachen bleiben als offen markiert.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
