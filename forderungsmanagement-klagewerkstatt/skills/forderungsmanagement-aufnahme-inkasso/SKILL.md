---
name: forderungsmanagement-aufnahme-inkasso
description: "Aufnahme Inkasso: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aufnahme Inkasso

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Aufnahme Inkasso** im Plugin Forderungsmanagement / Klagewerkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `forderungsmanagement-aufnahme` | Forderung systematisch aufnehmen: Glaeubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen § 288 BGB, vorgerichtliche Anwaltskosten, Mahngebuehren), Faelligkeit, Verjaehrungsbeginn. Output: vollstaendige Forderungsbeschreibung als Basis fuer Mahnverfahren oder Klage. |
| `inkasso-zahlungsklage-ersteller` | Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten § 288 BGB Gerichtsortfindung §§ 12 13 29 ZPO. Output: Klage-Entwurf Zahlungsklage für klare fällige belegte Ansprüche. Abgrenzung zu zv-mahnbescheid-online (Mahnverfahren) und klagevorlage-aus-eigenen-mustern (hauseigene Muster). |
| `klagevorlage-aus-eigenen-mustern` | Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage Zuständigkeitsprüfung online Sachverhalt-Dialog. Output: Klageschrift DOCX und Markdown plus Mini-Plugin ZIP für naechste Klagen ohne erneute Extraktion. Abgrenzung zu klage-aus-eigenem-skill (Nutzung des Plugins) und inkasso-zahlungsklage-ersteller. |

## Arbeitsweg

Im Plugin Forderungsmanagement / Klagewerkstatt gilt für **Aufnahme Inkasso**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `forderungsmanagement-aufnahme`

**Fokus:** Forderung systematisch aufnehmen: Glaeubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen § 288 BGB, vorgerichtliche Anwaltskosten, Mahngebuehren), Faelligkeit, Verjaehrungsbeginn. Output: vollstaendige Forderungsbeschreibung als Basis fuer Mahnverfahren oder Klage.

# Forderung aufnehmen

## Fachkern: Forderung aufnehmen
- **Spezialgegenstand:** Forderung aufnehmen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `inkasso-zahlungsklage-ersteller`

**Fokus:** Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten § 288 BGB Gerichtsortfindung §§ 12 13 29 ZPO. Output: Klage-Entwurf Zahlungsklage für klare fällige belegte Ansprüche. Abgrenzung zu zv-mahnbescheid-online (Mahnverfahren) und klagevorlage-aus-eigenen-mustern (hauseigene Muster).

# Inkasso-Zahlungsklage-Ersteller

## Fachkern: Inkasso-Zahlungsklage-Ersteller
- **Spezialgegenstand:** Inkasso-Zahlungsklage-Ersteller wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Triage — kläre vor dem Einsatz

1. Liegt ein vollständiger Mahnvorlauf vor (Rechnung mit Fälligkeit, mindestens eine Mahnung mit Fristsetzung)?
2. Ist die Hauptforderung noch nicht vor Klageeinreichung vollständig bezahlt (Erfüllungskontrolle)?
3. Sind Schuldner-Anschrift und Verbraucher-/Unternehmereigenschaft geklärt (Gerichtsstand § 29c ZPO bei Verbrauchern)?
4. Welche Nebenforderungen (Mahnkosten, Verzugszinsen, Inkassokosten) sollen eingeklagt werden — sind sie belegt und verhältnismäßig?
5. Liegt eine Abtretungskette vor — ist die Aktivlegitimation des Gläubigers/Zessionars lückenlos dokumentiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

§ 286 BGB (Verzugseintritt) — § 288 BGB (Verzugszinsen: +5 Pp. B2C, +9 Pp. B2B) — § 280 Abs. 2 BGB (Verzugsschaden) — § 249 BGB (Schadensersatz) — § 253 ZPO (Klageschrift) — §§ 12, 13, 29, 29c ZPO (örtliche Zuständigkeit) — §§ 23, 71 GVG (sachliche Zuständigkeit ab 01.01.2026: AG bis 10.000 EUR, LG darueber; § 47 EGZPO Uebergangsvorschrift) — § 93 ZPO (sofortiges Anerkenntnis, Kostenfolge) — § 812 BGB (Bereicherungsrecht als Auffanganspruch)

## Basiszinssatz § 247 BGB

- Basiszinssatz zum 01.01.2026: 1,27 Prozent (unveraendert gegenueber 01.07.2025). Bundesbank-Bekanntmachung: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- Daraus B2C-Verzugszinssatz (§ 288 Abs. 1 BGB) 6,27 Prozent, B2B-Verzugszinssatz (§ 288 Abs. 2 BGB) 10,27 Prozent. Halbjaehrliche Pruefung am 01.01. und 01.07. erforderlich.
- Verzugspauschale § 288 Abs. 5 BGB (B2B): 40 EUR pro Vorgang.

## Aenderungen Zustaendigkeitsrecht ab 01.01.2026

Gesetz zur Aenderung des Zustaendigkeitsstreitwerts der Amtsgerichte (BGBl. 2025 I Nr. 318 vom 11.12.2025) hebt mit Wirkung ab 01.01.2026 an:

- Sachliche Zustaendigkeit Amtsgericht von 5.000 auf 10.000 EUR (§ 23 GVG n.F.).
- Berufungssumme § 511 Abs. 2 ZPO von 600 auf 1.000 EUR.
- Wertgrenze Nichtzulassungsbeschwerde § 26 EGZPO von 20.000 auf 25.000 EUR.
- Uebergangsvorschrift § 47 EGZPO regelt Altverfahren.

Quelle: https://www.brak.de/newsroom/news/zivilgerichtsbarkeit-hoehere-wertgrenzen-fuer-zustaendigkeit-und-rechtsmittel-ab-112026/

## Rechtsprechung

- Rechtsprechung zu Verzug und § 286 BGB live ueber https://dejure.org und https://openjur.de pruefen.
- Aktenzeichen und Datum erst nach Verifikation in den Schriftsatz uebernehmen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill baut aus einer Forderungsakte einen sauberen Mahn- und Klageworkflow. **Eingeklagt werden nur Ansprüche, die klar, fällig, durchsetzbar und belegt sind.** Unsichere Positionen werden nicht eingeklagt, sondern als Rückfrage oder Nichtklage-Empfehlung ausgegeben.

## Sofortregeln

1. Nicht alles einklagen, was im Forderungskonto steht — jede Position braucht Anspruchsgrundlage, Betrag, Fälligkeit, Verzug, Beleg und Einwendungskontrolle.
2. Erfüllung blockt: vor Klageeinreichung bezahlte Hauptforderung darf nicht mehr eingeklagt werden.
3. Nebenforderungen sind kein Autopilot: Mahnkosten, Verzugszinsen, Inkassokosten werden einzeln geprüft.
4. Gerichtsort vor Klage: sachliche und örtliche Zuständigkeit sind zu prüfen und zu dokumentieren.
5. Mahnung vor Eskalation: wenn kein ausreichender Mahnvorlauf vorliegt, zuerst Mahnschreiben.

## Pflichtablauf


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1: Akte aufnehmen

Felder: Gläubiger, Schuldner (Verbraucher/Unternehmer), Forderungsgrund, Hauptforderung, Mahnvorlauf, Verzug, Nebenforderungen, Prozessgeschichte, Gerichtsort.

### Schritt 2: Mahnvorlauf prüfen

Mahnchronologie: Rechnung → Zahlungserinnerung → Mahnung(en) → letzte Mahnung mit Klagehinweis → Inkassoschreiben → Zahlungseingänge.

Ampelbeurteilung: grün (klar), gelb (unklar, nacharbeitbar), rot (rechtlich ungeeignet oder bereits erledigt).

### Schritt 3: Anspruchs-Gatekeeper

Prüfe je Position: Anspruchsgrundlage, Betrag, Fälligkeit, Durchsetzbarkeit, Verzug, Verschulden, Prozessrisiko, Gerichtsort.

- GRÜN → in den Klageantrag.
- GELB → Rückfrage oder Belegbedarf.
- ROT → nicht einklagen, Begründung angeben.

### Schritt 4: Gerichtsort finden

Sachlich: AG bis 10.000 EUR (§ 23 GVG), LG darüber (§ 71 GVG). Örtlich: §§ 12, 13, 29, 29c ZPO. Online-Abgleich über justiz.de oder justizadressen.nrw.de; Quelle und Abrufdatum dokumentieren.

### Schritt 5: Output bauen

1. Mahnchronologie als Tabelle.
2. Anspruchsmatrix mit Ampel.
3. Klagefreigabe (was wird eingeklagt, was nicht, warum).
4. Gerichtsortprüfung mit Quellenplatzhalter.
5. Klageentwurf nur für grüne Positionen.
6. Beleg- und Anlagenliste mit K-Sigeln.
7. Kosten-/Risiko-Hinweis zu § 93 ZPO.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zahlungsklage gegen saumigen Schuldner | Mahnverfahren oder Klageschrift nach Schema; Template unten |
| Variante A — Schuldner gibt Ratenzahlung an | Ratenvereinbarung statt Klage; Vollstreckungstitel danach |
| Variante B — Forderung wirtschaftlich zweifelhaft Insolvenz droht | Insolvenzantrag pruefen statt Klage; Klage nur wenn Masse erwartet |
| Variante C — Mandant will Geschaeftsbeziehung erhalten | Aussergerichtliche Einigung zuerst; Klage als letztes Mittel |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template

**Inkasso-Zahlungsklage — Anspruchsmatrix**

Schuldner: [...] | Forderungsstand: [...] EUR | Stand: [Datum]

| Position | Betrag EUR | Ampel | Begründung |
|---|---|---|---|
| Hauptforderung | [...] | GRÜN/ROT | [...] |
| Verzugszinsen | [...] | GRÜN/GELB | ab [...] |
| Mahnkosten | [...] | GRÜN/GELB | Beleg: [...] |
| Inkassokosten | [...] | GRÜN/GELB | Verhältnismäßigkeit: [...] |

**Gerichtsort:** AG/LG [...] — Online-Quelle: [...] — Abrufdatum: [...]

**Klageantrag (nur grüne Positionen):**
Der Beklagte wird verurteilt, an den Kläger [...] EUR nebst Zinsen in Höhe von [...] Prozentpunkten über dem Basiszinssatz seit [...] zu zahlen.

**Empfehlung:** [Klage einreichen / zuerst Mahnung / Positionen [...] nicht einklagen]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 3. `klagevorlage-aus-eigenen-mustern`

**Fokus:** Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage Zuständigkeitsprüfung online Sachverhalt-Dialog. Output: Klageschrift DOCX und Markdown plus Mini-Plugin ZIP für naechste Klagen ohne erneute Extraktion. Abgrenzung zu klage-aus-eigenem-skill (Nutzung des Plugins) und inkasso-zahlungsklage-ersteller.

# Klagewerkstatt — Lernlauf aus eigenen Mustern

## Fachkern: Klagewerkstatt — Lernlauf aus eigenen Mustern
- **Spezialgegenstand:** Klagewerkstatt — Lernlauf aus eigenen Mustern wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Dieser Skill ist der **Lernlauf** der Klagewerkstatt. Er macht in einem Durchgang vier Dinge:

1. Aus eigenen Klagemustern, Urteilen, Kommentaren, Aufsätzen und Formatvorlagen wird eine **hauseigene generische Standardklage-Vorlage** destilliert (Markdown + DOCX, mit Platzhaltern).
2. Der Sachverhalt wird im Dialog und aus weiteren hochgeladenen Dokumenten eingesammelt und in die Vorlage gespiegelt.
3. **Online-Prüfung der Zuständigkeit** ist Pflicht: justizadressen.nrw.de und justiz.de Gerichtssuche. Streitwert → AG/LG; Beklagtenadresse → örtliche Zuständigkeit; Sondertatbestände beachten.
4. Aus den extrahierten Hausregeln wird ein **eigenes Mini-Plugin als ZIP** generiert (`klagewerkstatt-<kanzlei>.zip`), das in Claude Code direkt installierbar ist und beim nächsten Mal ohne erneute Extraktion in der hauseigenen Vorlage produziert (siehe Schwester-Skill `klage-aus-eigenem-skill`).

Memo (rechtliche Würdigung) wird **nur auf ausdrückliche Anfrage** erstellt.

## Ablauf

**Schritt 1 — Kanzlei-Profil**
Einmal abfragen und merken:

> Kanzleiname, Rechtsanwältin/Rechtsanwalt mit Anschrift, BeA-SAFE-ID, AGB-Klausel zum Gerichtsstand (sofern für Verbraucher unzulässig nach § 29c ZPO klar abgrenzen), übliche Mandantengruppe (B2B, B2C, gemischt), bevorzugte Zinsformel (Basiszins+5/+9, §§ 288 Abs. 1/2 BGB), Standard-Anlagenliste (z. B. Rechnung, Auftragsbestätigung, Mahnungen, Lieferschein, AGB).

**Schritt 2 — Materialaufnahme (Lernkorpus)**
Den Nutzer bitten, alle einschlägigen Eigenmaterialien hochzuladen oder per Pfad zu nennen:

- Eigene Klage-Muster (mind. 2, gern 5–15) als DOCX, PDF, MD, TXT.
- Urteile zur eigenen Forderungspraxis (Volltexte oder Auszüge).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Format- und Layout-Vorlagen (Briefkopf-DOCX, Schriftarten, Nummerierung).
- Optional: typische Mahnschreiben, Verzugsbriefe, RVG-Berechnungen.

Bei Schweigen mit den im Plugin liegenden Leervorlagen unter `assets/vorlagen-leer/` arbeiten und das im Endprodukt transparent kennzeichnen.

**Schritt 3 — Extraktion der Hausregeln**
Aus dem Lernkorpus extrahieren (Zusammenfassung am Schluss dem Nutzer vorlegen):

- Aufbau der Klageschrift (Rubrum, Anträge, Begründung, Beweismittel, Anlagen, Schluss).
- Standardklauseln: Antragswortlaut, Zinsantrag, vorgerichtliche RA-Kosten als Nebenforderung, Mahnverzugsbeginn, Verzugszinsen (§§ 286, 288 BGB), Verzugsschaden (§ 280 BGB).
- Tonalität: knapp/ausführlich; aktiv/passiv; Direktanrede des Gerichts.
- Zitierweise: Pinpoint, Randnummer, jüngere BGH-Entscheidungen zuerst, deutsche Kommentartradition.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anlagenstrategie und Anlagensigel (K1, K2, …).

**Schritt 4 — Hauseigene Standardvorlage erzeugen**
Aus den Hausregeln eine **generische Klage-Vorlage** schreiben:

- Format: Markdown (Vorlage in `assets/vorlagen-leer/standardklage.md`) und parallel DOCX (über `office/docx`-Skill). Layout aus dem mitgelieferten Briefkopf, sonst Klotzkette-Default.
- Platzhalter strikt in geschweiften Doppelklammern: `{{kanzlei.briefkopf}}`, `{{rubrum.klagepartei}}`, `{{rubrum.beklagte}}`, `{{rubrum.bevollmaechtigte}}`, `{{gericht.bezeichnung}}`, `{{gericht.adresse}}`, `{{gericht.bea_safe_id}}`, `{{streitwert.eur}}`, `{{antrag.hauptforderung}}`, `{{antrag.zinsen}}`, `{{antrag.kosten}}`, `{{sachverhalt}}`, `{{rechtliche_würdigung}}`, `{{anlagen.liste}}`, `{{ort_datum}}`, `{{unterschrift}}`.
- Standardabschnitte enthalten Hausregel-Bausteine.

**Schritt 5 — Sachverhalt einsammeln**
Strukturierte Rückfragen (alle als Liste auf einmal stellen, damit der Nutzer in einem Schwung antworten kann):

- Forderungsgrund (Kauf, Werkvertrag, Dienstvertrag, Darlehen, Miete, sonstiges) mit kurzer Vertragsbeschreibung.
- Beklagte(r): Name, Anschrift, Rechtsform, ggf. gesetzliche Vertretung; **Anschrift exakt** für die Zuständigkeitsprüfung.
- Hauptforderung in EUR, Fälligkeitsdatum, etwaige Teilzahlungen.
- Mahnungen mit Datum, Form und Inhalt; Mahnverzugseintritt.
- Vorgerichtliche RA-Kosten als Nebenforderung (Geschäftsgebühr Nr. 2300 VV RVG, Anrechnung Vorbem. 3 Abs. 4 VV RVG).
- Beweismittel: Urkunden, Zeugen, Sachverständige, Parteivernehmung, Augenschein.
- Besonderheiten: Verbrauchereigenschaft des Beklagten, AGB-Gerichtsstand, Erfüllungsort, ausländische Beteiligung (EuGVVO/Brüssel Ia VO 1215/2012).

Zusätzlich Dokumenten-Drop akzeptieren (Rechnungen, Mahnungen, Korrespondenz). Aus diesen Dokumenten Felder automatisch befüllen und die Belegung jeweils kennzeichnen.

**Schritt 6 — Zuständigkeit online prüfen (Pflicht)**

Pflichtschritt vor Auslieferung. Reihenfolge:

1. **Sachliche Zuständigkeit** rechnerisch: Streitwert ≤ 10.000 EUR → AG (§ 23 Nr. 1 GVG i. d. F. seit 1.1.2026); > 10.000 EUR → LG (§ 71 GVG). Sondertatbestände beachten: Wohnraummietsachen AG ohne Streitwertgrenze (§ 23 Nr. 2a GVG), Nachbarschaftsstreitigkeiten AG (§ 23 Nr. 2e GVG), Familiensachen FamG, Handelssachen Kammer für Handelssachen (§§ 95, 96 GVG).
2. **Örtliche Zuständigkeit** rechtlich: allgemeiner Gerichtsstand der Beklagten (§§ 12, 13 ZPO). Erfüllungsort (§ 29 ZPO) prüfen — bei Geldschulden Sitz der Klagepartei nur bei qualifizierter Schickschuld, sonst Wohnsitz Beklagte. Verbraucher-Sondertatbestand § 29c ZPO. AGB-Gerichtsstand prüfen, aber bei Verbrauchern nach § 38 ZPO unwirksam.
3. **Online-Adressrecherche** (immer ausführen):
 - Für NRW-Anschriften: `pplx content fetch "https://www.justizadressen.nrw.de/de/justiz/suche?suchbegriff=<PLZ_oder_Ort>"` (PLZ oder Ort der Beklagten). Wenn PLZ allein nicht reicht, mit Ort nachfassen.
 - Bundesweit ergänzend: `pplx content fetch "https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php"` und Landes-Justizportale.
 - Treffer prüfen und Bezeichnung, Postanschrift, Telefax und — wo bekannt — die BeA-EGVP-SAFE-ID (Bundesweites elektronisches Adressverzeichnis SAFE, abrufbar in beA bzw. unter justiz.de) einsetzen. Wenn keine SAFE-ID gelistet, mit dem Hinweis "EGVP-Adresse über beA-Adressbuch (SAFE-ID) zu ergänzen" markieren.
4. Quelle und Abrufdatum stets im Output ausweisen (Anlage `Zuständigkeitsprüfung`).

**Schritt 7 — Klageschrift erzeugen**

- **Immer**: `Klage-<Beklagte>-<YYYYMMDD>.docx` (über `office/docx`) und Spiegel `Klage-<Beklagte>-<YYYYMMDD>.md`.
- Anlagenkonvolut als Liste mit K-Sigeln; Anlagenkopfbogen optional.
- **Padlet** (auf Wunsch): single-file HTML aus `assets/padlet/klage-padlet.html` mit Live-Vorschau und Pflegefeldern; speichert in `localStorage`.

**Schritt 8 — Eigenes Mini-Plugin als ZIP erzeugen**

Aus den Hausregeln und der Standardvorlage wird ein eigenes Plugin gepackt:

- Skript: `python scripts/plugin_aus_hausregeln.py --kanzlei "<Name>" --vorlage <pfad.md> --regeln <regeln.json> --ziel <ziel.zip>`.
- Inhalt des ZIP:
 - `klagewerkstatt-<slug>/.claude-plugin/plugin.json` (Name `klagewerkstatt-<slug>`, Version 0.1.0).
 - `klagewerkstatt-<slug>/skills/klage-erstellen/SKILL.md` (siehe Schwester-Skill `klage-aus-eigenem-skill` als Bauanleitung; im erzeugten Plugin lebt die Skill-Datei eigenständig).
 - `klagewerkstatt-<slug>/assets/vorlage/standardklage.md` und `.docx`.
 - `klagewerkstatt-<slug>/references/hausregeln.json`, `belegmuster.md`, `anlagenliste.md`, `zustaendigkeit-quellen.md`.
 - `klagewerkstatt-<slug>/README.md` mit Direkt-Download-Hinweis und Installationsanleitung.
- ZIP-Dateiname `klagewerkstatt-<slug>.zip`. Datei dem Nutzer zum Download geben mit Installationsanweisung für Claude Code (`Customize Plugins → Install from .zip`).

**Schritt 9 — Memo (nur auf Anfrage)**

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Anspruchsgrundlagen, Beweislage und Prozessrisiken erstellen?

Bei Zustimmung: zwei Seiten, DOCX oder Markdown.

## Rechtlicher Rahmen

### Pflichtinhalte und Form der Klageschrift
- **§ 253 Abs. 2 ZPO** Klageinhalt (Parteien, Gericht, Anträge, Sachverhalt, Beweismittel).
- **§ 130 ZPO** Form der Schriftsätze; **§ 130a ZPO** elektronisches Dokument; **§ 130d ZPO** Pflicht zur elektronischen Einreichung für Rechtsanwältinnen und Rechtsanwälte (beA).
- **§ 78 ZPO** Anwaltszwang vor LG aufwärts.
- **§ 12 RVG / Anlage 2 VV RVG**: Gebührentabelle; **Nr. 2300 VV RVG** Geschäftsgebühr; **Vorbem. 3 Abs. 4 VV RVG** Anrechnung 0,65; **Nr. 3100 VV RVG** Verfahrensgebühr.

### Sachliche Zuständigkeit
- **§ 23 Nr. 1 GVG** AG bis 10.000 EUR (i. d. F. seit 1.1.2026).
- **§ 71 GVG** LG über 10.000 EUR.
- **§ 23 Nr. 2a GVG** Wohnraummietsachen AG ohne Streitwertgrenze.

### Örtliche Zuständigkeit
- **§§ 12, 13 ZPO** allgemeiner Gerichtsstand der Beklagten.
- **§ 17 ZPO** Sitz juristischer Personen.
- **§ 29 ZPO** besonderer Gerichtsstand des Erfüllungsortes.
- **§ 29c ZPO** Verbraucherverträge (Wohnsitz Verbraucher).
- **§ 38 ZPO** Gerichtsstandsvereinbarung (zwischen Vollkaufleuten zulässig, gegenüber Verbraucher gemäß § 38 Abs. 3 ZPO eingeschränkt).
- **§ 17 ZPO** Sitz; **§ 24 ZPO** dinglicher Gerichtsstand.
- Bei grenzüberschreitenden Sachverhalten **Brüssel Ia VO (EU) 1215/2012**, insb. Art. 7 Nr. 1 lit. a und b (Erfüllungsort), Art. 17–19 (Verbrauchersachen), Art. 25 (Gerichtsstandsvereinbarung).

### Materielle Anspruchsgrundlagen (Standard)
- **§ 433 Abs. 2 BGB** Kaufpreisanspruch; **§ 631 Abs. 1 BGB** Werklohnanspruch; **§ 611a Abs. 2 BGB** Vergütungsanspruch Dienstvertrag; **§ 535 Abs. 2 BGB** Miete; **§ 488 BGB** Darlehensrückzahlung.
- **§ 286 BGB** Verzug; **§ 288 Abs. 1 BGB** Verzugszinsen 5 Prozentpunkte über Basiszins; **§ 288 Abs. 2 BGB** 9 Prozentpunkte zwischen Unternehmern für Entgeltforderung; **§ 288 Abs. 5 BGB** Verzugspauschale 40 EUR (B2B).
- **§ 280 BGB** Schadensersatz inkl. vorgerichtlicher RA-Kosten.

### Leitentscheidungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabeformat

1. **Klageschrift** als DOCX (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und Markdown-Spiegel.
2. **Anlage Zuständigkeitsprüfung** mit Online-Quellen und Abrufdatum.
3. **Hauseigenes Mini-Plugin** als ZIP (`klagewerkstatt-<slug>.zip`) mit Standardvorlage, Hausregeln und sofort installierbarem Skill `klage-erstellen`.
4. **Optional**: HTML-Padlet zur Pflege, DOCX-Anlagenkopfbogen, Memo im Gutachtenstil.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

- Bei drohender Zahlungsunfähigkeit der Beklagten an Liquiditätsplanung (`liquiditaetsplanung`) zur Schnellprüfung.
- Bei einstweiligem Rechtsschutz/Mahnverfahren an `prozessrecht` (Plugin) oder das freistehende
 Plugin `zwangsvollstreckung` (`zv-mahnbescheid-online`, `zv-vollstreckungsbescheid-folge`) verweisen.
- Nach Rechtskraft des Titels an `zwangsvollstreckung` zur operativen Durchsetzung (`zv-pfueb-bank`,
 `zv-pfueb-arbeitsentgelt`, `zv-vermoegensauskunft-gv`).
- Wenn der Nutzer beim nächsten Mal nur den Sachverhalt einreichen will: Schwester-Skill `klage-aus-eigenem-skill` mit dem im Schritt 8 erzeugten Plugin verwenden.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweise (27.05.2026)

Drei halluzinierte Rechtsprechungsbelege wurden im Abschnitt "Leitentscheidungen" korrigiert:

| # | Fehlerhaftes AZ | Status | Korrektur |
|---|---|---|---|
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Recherchequelle: dejure.org (Abruf 27.05.2026). Frontmatter unveraendert. Kein Commit.
