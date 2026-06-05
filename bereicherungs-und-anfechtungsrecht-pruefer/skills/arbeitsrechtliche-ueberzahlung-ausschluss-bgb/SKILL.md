---
name: arbeitsrechtliche-ueberzahlung-ausschluss-bgb
description: "Arbeitsrechtliche Ueberzahlung Ausschluss BGB: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arbeitsrechtliche Ueberzahlung Ausschluss BGB

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Arbeitsrechtliche Ueberzahlung Ausschluss BGB** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arbeitsrechtliche-ueberzahlung` | Dieses Fachmodul greift, wenn Arbeitsentgelt überzahlt wurde und Ausschlussfristen oder Entreicherung drohen. Normen: § 611a BGB; §§ 812 und 818 BGB; § 199 BGB; tarifliche Ausschlussfristen. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Berechnungsblatt Rückforderung mit Ausschlussfrist- und Entreicherungsprüfung. Abgrenzung: nicht Schadensersatz §§ 280 ff. BGB. |
| `ausschluss-814-bgb-kenntnis-der-nichtschuld` | Bereicherungsanspruch scheitert an § 814 BGB wegen positiver Kenntnis des Leistenden von der Nichtschuld. Normen: § 814 BGB. Prüfraster: positive Kenntnis vs. bloss Zweifel, Zeitpunkt der Kenntnis, Abgrenzung zu condictio indebiti. Output: Prüfergebnis Ausschlussgrund § 814 BGB mit Begründung. Abgrenzung: nicht § 817 BGB (Gesetzes-/Sittenverstoß). |
| `ausschluss-817-bgb-gesetzes-und-sittenverstoss` | Bereicherungsanspruch gesperrt durch § 817 S. 2 BGB wegen eigenen Gesetzes- oder Sittenverstosses des Leistenden. Normen: §§ 817 134 138 BGB. Prüfraster: beiderseitiger Verstoß, Sperrwirkung, enge Rückausnahmen nach h.M. Output: Prüfergebnis Ausschlussgrund § 817 BGB und Handlungsempfehlung. Abgrenzung: nicht § 814 BGB (Kenntnis der Nichtschuld). |
| `bankueberweisung-fehlbuchung-und-empfaengerhorizont` | Dieses Fachmodul greift, wenn eine Banküberweisung, Fehlbuchung oder Fehlleitung bereicherungsrechtlich zugeordnet werden muss. Normen: §§ 675 ff. BGB; § 675u BGB; §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Empfängerhorizont-Analyse mit Anspruch gegen Bank oder Endempfänger. Abgrenzung: nicht zivilrechtliche Schenkungsrückforderung. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Arbeitsrechtliche Ueberzahlung Ausschluss BGB**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arbeitsrechtliche-ueberzahlung`

**Fokus:** Dieses Fachmodul greift, wenn Arbeitsentgelt überzahlt wurde und Ausschlussfristen oder Entreicherung drohen. Normen: § 611a BGB; §§ 812 und 818 BGB; § 199 BGB; tarifliche Ausschlussfristen. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung; Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung. Output: Berechnungsblatt Rückforderung mit Ausschlussfrist- und Entreicherungsprüfung. Abgrenzung: nicht Schadensersatz §§ 280 ff. BGB.

# Arbeitsrechtliche Überzahlung

## Einsatzbereich

Dieses Fachmodul greift, wenn Arbeitsentgelt überzahlt wurde und Ausschlussfristen oder Entreicherung drohen. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welches Spezialregime steht neben oder vor §§ 812 ff. BGB?
2. Welche Schutzrichtung verfolgt dieses Regime?
3. Welche Leistungen und Gegenleistungen sind betroffen?
4. Würde Bereicherungsrecht die Spezialwertung unterlaufen?
5. Welche Fristen, Formfragen oder Rechtswege sind gesondert zu prüfen?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht.
- Übernimm Schutzwertungen in Saldo, Wertersatz und Entreicherung.
- Trenne Rückabwicklung, Schadensersatz und öffentlich-rechtliche Erstattung.
- Setze § 812 BGB nur ergänzend ein, wenn kein abschließendes Regime greift.
- Markiere Rechtsweg-, Frist- und Beweisrisiken.

## Typische Fehler

- Spezialrecht durch § 812 BGB überspielen.
- Schutzvorschriften in Wertersatz umwandeln.
- Fristen oder Rechtsweg übersehen.

## Arbeitsrecht-spezifische Schwerpunkte

- **Rechtsgrundlage:** § 812 Abs. 1 S. 1 Alt. 1 BGB (Leistungskondiktion), wenn Lohn ohne Anspruch gezahlt — z. B. nach Beendigung, bei doppelter Zahlung, bei zu hoher Eingruppierung, bei nicht erbrachter Arbeitsleistung (krank ohne Lohnfortzahlungsanspruch).
- **Ausschlussfristen:** zentrale Hürde. Tarifliche oder einzelvertragliche Ausschlussfristen (typisch 3 Monate ab Fälligkeit) müssen vom Arbeitgeber strikt gewahrt werden. **Fristbeginn** bei Bereicherungsanspruch ist die Zahlung des Entgelts (str.); BAG-Linie beachten — Verifikation des Az.
- **Entreicherung § 818 Abs. 3 BGB:** großzügig zugunsten des Arbeitnehmers — bei Konsum für laufende Lebenshaltung (Miete, Lebensmittel) regelmäßig Entreicherung anerkannt. Sparvermögen, Anschaffungen oder Schuldentilgung dagegen meist nicht entreichert.
- **§ 819 BGB Verschärfung:** Bei Kenntnis des Arbeitnehmers vom Fehlen des Rechtsgrunds (z. B. mündliche Vereinbarung Gehaltskürzung, dennoch volle Zahlung) Wegfall der Entreicherungseinrede.
- **Nettolohn-Bruttolohn-Problem:** Rückforderbar ist grds. der **Bruttolohn**, weil Arbeitnehmer rechtlich darüber verfügt hat; ggf. Anpassung Lohnsteuer und Sozialversicherung. Bei Erstattung im laufenden Lohnabrechnungszeitraum unproblematisch.
- **Rechtsweg:** Arbeitsgericht zuständig (§ 2 Abs. 1 Nr. 3 ArbGG) — Bereicherungsanspruch zwischen Arbeitgeber und Arbeitnehmer.

## Insolvenz-Schnittstelle

- Bei Insolvenz des Arbeitnehmers: Lohnvorpfändungsbeschluss, Pfändbarkeitsgrenzen § 850c ZPO beachten.
- Bei Insolvenz des Arbeitgebers: rückforderbarer Überzahlungsbetrag ist Insolvenzforderung § 38 InsO; Insolvenzgeld-Vorfinanzierung beachten.
- Anfechtung § 130, § 131 InsO bei zu hoher Lohnzahlung in der Krise möglich.

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

## 2. `ausschluss-814-bgb-kenntnis-der-nichtschuld`

**Fokus:** Bereicherungsanspruch scheitert an § 814 BGB wegen positiver Kenntnis des Leistenden von der Nichtschuld. Normen: § 814 BGB. Prüfraster: positive Kenntnis vs. bloss Zweifel, Zeitpunkt der Kenntnis, Abgrenzung zu condictio indebiti. Output: Prüfergebnis Ausschlussgrund § 814 BGB mit Begründung. Abgrenzung: nicht § 817 BGB (Gesetzes-/Sittenverstoß).

# Ausschluss nach § 814 BGB — Kenntnis der Nichtschuld

## Triage — kläre vor der Prüfung

1. Hat der Leistende im Zeitpunkt der Leistung alle tatsächlichen Umstände gekannt, die zur Nichtschuld führen?
2. Lag nur ein Rechtsirrtum vor (Tatsachen bekannt, rechtliche Wertung fehlt)?
3. Beruhte die Leistung auf bloßem Zweifel oder Verdacht (kein § 814-Ausschluss)?
4. Wer beruft sich auf § 814 BGB, und wer trägt die Beweislast?
5. Kommt daneben § 814 Alt. 2 BGB (sittliche Pflicht) in Betracht?

## Zentrale Normen

§ 814 BGB (Ausschluss bei Kenntnis der Nichtschuld bzw. sittlicher Pflicht) — § 812 Abs. 1 S. 1 Alt. 1 BGB (Leistungskondiktion) — § 813 BGB (dauernde Einrede) — § 817 BGB (Gesetzes-/Sittenverstoß) — § 242 BGB (Treu und Glauben, venire contra factum proprium)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Obersatz

Hat der Leistende gewusst, dass er zur Leistung nicht verpflichtet war, ist die Rückforderung nach § 814 Alt. 1 BGB ausgeschlossen.

## Tatbestandsmerkmale

### 1. Leistung in Unkenntnis

Der Grundsatz: Bereicherungsanspruch setzt voraus, dass der Leistende irrtümlich geleistet hat.

### 2. Positive Kenntnis der Nichtschuld

**Definition:** Der Leistende muss zum Zeitpunkt der Leistung positiv gewusst haben, dass er nicht verpflichtet ist. Nicht ausreichend sind:
- Zweifel an der Verpflichtung
- Kennenmüssen (fahrlässige Unkenntnis)
- Vermutungen oder Verdacht

**Maßstab:** Der Leistende muss die rechtlichen Tatsachen, aus denen sich das Fehlen der Schuld ergibt, gekannt haben. Rechtsirrtum (fehlende rechtliche Würdigung bekannter Tatsachen) schließt § 814 BGB nach überwiegender Meinung nicht aus.

### 3. Zeitpunkt: Bei Leistungserbringung

Die Kenntnis muss im Moment der Leistung vorhanden sein. Nachträgliche Kenntnis ändert nichts.

## Beweislast

Die Beweislast für die positive Kenntnis trägt der Anspruchsgegner (Bereicherungsschuldner), der sich auf § 814 BGB beruft.

## Abgrenzung zu § 814 Alt. 2 BGB

§ 814 Alt. 2 BGB schließt die Rückforderung aus, wenn die Leistung einer sittlichen Pflicht oder einer Anstandsrücksicht entsprach. Dies ist eng auszulegen.

## Prüfschema

1. Hat der Leistende positiv gewusst, dass er nicht schuldet?
2. Kannte er alle anspruchsausschließenden Tatsachen?
3. Liegt bloßer Rechtsirrtum vor (kein Ausschluss nach § 814 BGB)?
4. Bestand die Kenntnis bei Leistungserbringung?

## Output-Template

**Prüfung § 814 BGB — Kenntnis der Nichtschuld**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Positive Kenntnis aller Tatsachen | ja / nein |
| Nur Rechtsirrtum (Tatsachen bekannt) | ja / nein → kein Ausschluss |
| Zweifel oder Verdacht statt Wissen | ja → kein § 814 |
| Kenntnis im Leistungszeitpunkt | ja / nein |
| Beweislast beim Gegner dargelegt | ja / nein |

**Ergebnis:** § 814 Alt. 1 BGB greift / greift nicht. Bereicherungsanspruch [besteht / ist ausgeschlossen].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 3. `ausschluss-817-bgb-gesetzes-und-sittenverstoss`

**Fokus:** Bereicherungsanspruch gesperrt durch § 817 S. 2 BGB wegen eigenen Gesetzes- oder Sittenverstosses des Leistenden. Normen: §§ 817 134 138 BGB. Prüfraster: beiderseitiger Verstoß, Sperrwirkung, enge Rückausnahmen nach h.M. Output: Prüfergebnis Ausschlussgrund § 817 BGB und Handlungsempfehlung. Abgrenzung: nicht § 814 BGB (Kenntnis der Nichtschuld).

# Ausschluss nach § 817 BGB — Gesetzes- und Sittenverstoß

## Triage — kläre vor der Prüfung

1. Welcher der beiden Beteiligten hat gegen ein gesetzliches Verbot oder die guten Sitten verstoßen — nur der Empfänger (§ 817 S. 1), nur der Leistende oder beide (§ 817 S. 2)?
2. Welches konkrete Verbotsgesetz oder welche Sittenwidrigkeit ist einschlägig (§ 134, § 138 BGB, § 1 SchwarzArbG, § 299 StGB)?
3. Liegt ein strukturelles Machtgefälle oder ein nur den Empfänger schützendes Verbotsgesetz vor (teleologische Reduktion)?
4. Wurde die Leistung durch arglistige Täuschung des Empfängers herbeigeführt?
5. Wer trägt die Beweislast für den Verstoß des Leistenden?

## Zentrale Normen

§ 817 BGB (Kondiktionsausschluss bei Verstoß) — § 134 BGB (Verbotsgesetz) — § 138 BGB (Sittenwidrigkeit) — § 812 Abs. 1 S. 1 BGB (Leistungskondiktion) — § 1 Abs. 2 SchwarzArbG — § 299 StGB (Bestechung im geschäftlichen Verkehr) — § 823 Abs. 2 BGB (Schutzgesetzverletzung)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Norm

§ 817 BGB regelt zwei Fallgruppen:
- Satz 1: Rückforderungsrecht bei verbotenem Zweck des Empfängers.
- Satz 2: Ausschluss der Rückforderung, wenn dem Leistenden selbst ein Gesetzes- oder Sittenverstoß zur Last fällt.

## § 817 Satz 1 BGB — Verbotener Zweck beim Empfänger

**Tatbestand:** Der Empfang der Leistung war für den Empfänger mit einem Verstoß gegen ein gesetzliches Verbot oder die guten Sitten verbunden.

**Rechtsfolge:** Rückforderungsrecht des Leistenden, auch wenn kein Irrtum vorlag.

## § 817 Satz 2 BGB — Sperrwirkung bei eigenem Verstoß

**Tatbestand:** Dem Leistenden fällt seinerseits ein solcher Verstoß zur Last.

**Rechtsfolge:** Die Rückforderung ist ausgeschlossen (in pari turpitudine melior est causa possidentis).

**Anwendungsfälle:**
- Zahlung von Bestechungsgeldern (§ 299 StGB): beide Seiten verstoßen.
- Schwarzarbeit (§ 1 Abs. 2 SchwarzArbG): Rückforderung nach h.M. ausgeschlossen.
- Rechtswidriges Glücksspiel: Rückforderung von Einsätzen.

## Rückausnahmen (h.M. und BGH)

§ 817 S. 2 BGB wird teleologisch reduziert bei:
1. Verbotsgesetze, die ausschließlich den Leistenden schützen.
2. Strukturelles Machtgefälle (Sittenwidrigkeit zum Schutz des Schwächeren).
3. Arglistige Täuschung: Wer durch Täuschung zur Leistung gebracht wurde, kann trotz eigenem Verstoß zurückfordern.

## Beweislast

Der Anspruchsgegner trägt die Beweislast für den eigenen Verstoß des Leistenden.

## Prüfschema

1. Liegt ein Gesetzes- oder Sittenverstoß beim Empfänger vor (§ 817 S. 1)?
2. Liegt zugleich ein Verstoß beim Leistenden vor (§ 817 S. 2)?
3. Greift eine Rückausnahme (Schutzzweck, Machtgefälle, Arglist)?
4. Ist der Verstoß tatsächlich dem Leistenden zurechenbar?

## Output-Template

**Prüfung § 817 BGB — Gesetzes- und Sittenverstoß**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Verstoß beim Empfänger (§ 817 S. 1) | ja / nein |
| Verstoß beim Leistenden (§ 817 S. 2) | ja / nein |
| Konkretes Verbotsgesetz / Sittenwidrigkeit | [...] |
| Teleologische Reduktion anwendbar | ja / nein, weil [...] |
| Arglistige Täuschung als Rückausnahme | ja / nein |

**Ergebnis:** § 817 S. 2 BGB greift / greift nicht. Bereicherungsanspruch [besteht / ist ausgeschlossen].

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

---

## 4. `bankueberweisung-fehlbuchung-und-empfaengerhorizont`

**Fokus:** Dieses Fachmodul greift, wenn eine Banküberweisung, Fehlbuchung oder Fehlleitung bereicherungsrechtlich zugeordnet werden muss. Normen: §§ 675 ff. BGB; § 675u BGB; §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont des Endempfängers; Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab. Output: Empfängerhorizont-Analyse mit Anspruch gegen Bank oder Endempfänger. Abgrenzung: nicht zivilrechtliche Schenkungsrückforderung.

# Banküberweisung, Fehlbuchung und Empfängerhorizont

## Einsatzbereich

Dieses Fachmodul greift, wenn eine Banküberweisung, Fehlbuchung oder Fehlleitung bereicherungsrechtlich zugeordnet werden muss. Der Skill zwingt zu einer vermögensorientierten Prüfung: erst Vorteil und Zurechnung, dann Rechtsgrund und Behaltensgrund, zuletzt Umfang, Einreden und prozessuales Ziel.

## Triage — zuerst klären

1. Welche Personen und Beziehungen bilden das Leistungsdreieck oder die Kette?
2. Wer hat den Leistungszweck objektiv gesetzt?
3. War eine Anweisung, Vollmacht, Zession oder Drittleistung wirksam und zurechenbar?
4. Welches Verhältnis ist fehlerhaft?
5. Würde ein Direktanspruch nur ein Insolvenz- oder Vertragsrisiko verschieben?

## Spezifischer Prüfungsfokus

- Bestimme den konkreten Vermögensvorteil und seine heutige Spur im Vermögen.
- Ordne den Vorteil einer Leistungsbeziehung, einem Eingriff oder einer sonstigen Erwerbslage zu.
- Prüfe Rechtsgrund und Behaltensgrund getrennt.
- Kontrolliere, ob § 818 BGB den Anspruch erweitert, begrenzt oder verschärft.
- Leite erst danach Anspruchsgegner, Anspruchshöhe und prozessuales Ziel ab.

## Prüfungslogik

- Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl.
- Bestimme den Empfängerhorizont des Endempfängers.
- Wickle Fehler grundsätzlich in der jeweils fehlerhaften Beziehung ab.
- Prüfe Direktkondiktion nur mit eigenständiger Ausnahmebegründung.
- Halte Vertrauensschutz und Risikozuweisung ausdrücklich fest.

## Bankfall-Schärfung

Unterscheide vier Lagen:

1. **Kundenauftrag richtig, Valuta falsch:** Die Bank ist nur Zahlungswerkzeug; Rückforderung läuft in der Valutabeziehung.
2. **Kundenauftrag falsch, aber zurechenbar:** Empfängerhorizont und Verwendungszweck entscheiden, ob Zahlung als Leistung des Kunden gilt.
3. **Bankfehler ohne zurechenbaren Auftrag:** Bank oder belasteter Kunde kann einen Direktanspruch gegen den Empfänger haben; Empfängerschutz bleibt zu prüfen.
4. **Falsche Empfängeridentität:** Anspruch richtet sich regelmäßig gegen den tatsächlichen Empfänger, nicht gegen den gemeinten Empfänger.

Für § 818 Abs. 3 BGB immer Kontoentwicklung prüfen: Gutschrift, Abbuchungen, Schuldtilgung, Dispositionskredit, Ersatzgutschriften, Kenntniszeitpunkt.

## Typische Fehler

- Tatsächlichen Empfänger automatisch als Schuldner behandeln.
- Doppelmangel zu einem Pauschalanspruch verschmelzen.
- Insolvenzrisiko ohne Rechtsgrund verlagern.

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

## Konto- und Empfängerhorizont-Tabelle

| Punkt | Feststellung |
|---|---|
| Auftraggeber / belastetes Konto | [...] |
| Verwendungszweck | [...] |
| Empfänger durfte Zahlung verstehen als | Leistung von [...] |
| Fehlerquelle | Kunde / Bank / Dritter / unklar |
| Kontoverbrauch nach Gutschrift | [...] |
| Kenntnis des Fehlers ab | [...] |

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
