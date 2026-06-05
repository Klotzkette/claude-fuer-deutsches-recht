---
name: vwr-eilrechtsschutz-widerspruch-klage
description: "VWR Eilrechtsschutz Widerspruch Klage: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# VWR Eilrechtsschutz Widerspruch Klage

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **VWR Eilrechtsschutz Widerspruch Klage** im Plugin Fachanwalt Verwaltungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vwr-spezial-eilrechtsschutz` | Spezialfall Eilrechtsschutz vor Verwaltungsgericht: § 80 Abs. 5 VwGO Aussetzung der Vollziehung, § 123 VwGO einstweilige Anordnung, Abwaegungspruefung, Begruendungsanforderungen. Pruefraster und Mustertexte fuer Eilantrag. |
| `widerspruch-oder-klage-erstpruefung` | Entscheidung Widerspruch vs. direkte Klage treffen: Mandant fragt was als naechstes zu tun ist nach Erhalt eines Bescheids. Normen: § 68 VwGO (Vorverfahren statthaft?), § 42 VwGO (Anfechtungs-/Verpflichtungsklage), § 74 VwGO (Klagefrist), §§ 80 und 80a und 123 VwGO (vorlaeufiger Rechtsschutz). Prüfraster: Vorverfahrenspflicht (Bundesland), Statthaftigkeit, Klagebefugnis, Frist, vorlaeufiger Rechtsschutz-Bedarf. Output Vorabbewertung Erfolgsaussicht, Streitwert § 52 GKG, Routing. Abgrenzung: Widerspruchsschrift siehe fachanwalt-verwaltungsrecht-widerspruchsschrift; Eilantrag siehe eilantrag-80-abs-5-vwgo. |

## Arbeitsweg

Im Plugin Fachanwalt Verwaltungsrecht gilt für **VWR Eilrechtsschutz Widerspruch Klage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vwr-spezial-eilrechtsschutz`

**Fokus:** Spezialfall Eilrechtsschutz vor Verwaltungsgericht: § 80 Abs. 5 VwGO Aussetzung der Vollziehung, § 123 VwGO einstweilige Anordnung, Abwaegungspruefung, Begruendungsanforderungen. Pruefraster und Mustertexte fuer Eilantrag.

# Verwaltungsrecht: Eilrechtsschutz

## Spezialwissen: Verwaltungsrecht: Eilrechtsschutz
- **Spezialgegenstand:** Verwaltungsrecht: Eilrechtsschutz / vwr eilrechtsschutz. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VwGO.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `widerspruch-oder-klage-erstpruefung`

**Fokus:** Entscheidung Widerspruch vs. direkte Klage treffen: Mandant fragt was als naechstes zu tun ist nach Erhalt eines Bescheids. Normen: § 68 VwGO (Vorverfahren statthaft?), § 42 VwGO (Anfechtungs-/Verpflichtungsklage), § 74 VwGO (Klagefrist), §§ 80 und 80a und 123 VwGO (vorlaeufiger Rechtsschutz). Prüfraster: Vorverfahrenspflicht (Bundesland), Statthaftigkeit, Klagebefugnis, Frist, vorlaeufiger Rechtsschutz-Bedarf. Output Vorabbewertung Erfolgsaussicht, Streitwert § 52 GKG, Routing. Abgrenzung: Widerspruchsschrift siehe fachanwalt-verwaltungsrecht-widerspruchsschrift; Eilantrag siehe eilantrag-80-abs-5-vwgo.

# Widerspruch oder Klage — Erstprüfung

## Zweck

Der typische Erstkontakt im Verwaltungsrecht: Mandant kommt mit Bescheid. Frage ist: Widerspruch einlegen Klage erheben Eilantrag stellen — alle drei? Dieses Raster sortiert.

## Eingaben

- Verwaltungsakt (Bescheid Verfügung Anordnung)
- Bekanntgabedatum
- Rechtsbehelfsbelehrung
- Mandatsverlauf bisher
- Bundesland (für Vorverfahrenspflicht)

## Schritt 1 — Verwaltungsakt? § 35 VwVfG

- Hoheitliche Maßnahme
- Behörde
- Einzelfall
- Außenwirkung
- Regelungsgehalt

Wenn nein — Realakt informelle Maßnahme — andere Klagearten Feststellungs- oder Unterlassungsklage.

## Schritt 2 — Statthaftigkeit der Klageart

| Klageziel | Klageart | Norm |
|---|---|---|
| Aufhebung belastenden VA | Anfechtungsklage | § 42 Abs. 1 1. Alt. VwGO |
| Erlass begünstigenden VA | Verpflichtungsklage | § 42 Abs. 1 2. Alt. VwGO |
| Sonstige Leistung | Allgemeine Leistungsklage | unbenannt |
| Bestehen / Nicht-Bestehen Rechtsverhältnis | Feststellungsklage | § 43 VwGO |
| Unwirksamkeit Satzung Verordnung | Normenkontrolle | § 47 VwGO bei VwGH |

## Schritt 3 — Vorverfahrenspflicht

- **Grundsatz** § 68 VwGO Vorverfahren als Klagezulässigkeitsvoraussetzung
- **Ausnahme** durch Landesgesetz Abschaffung des Widerspruchsverfahrens in vielen Bundesländern für viele Materien — länderspezifische Prüfung erforderlich
- **Sonderfälle** Untätigkeitsklage § 75 VwGO nach drei Monaten

**Praxis:** Wenn unsicher dann Vorsichtshalber Widerspruch UND Untätigkeitsklage nach drei Monaten erwägen.

## Schritt 4 — Klagebefugnis § 42 Abs. 2 VwGO

- Möglichkeitstheorie — Verletzung eigener Rechte muss möglich sein
- Schutznorm-Theorie — Norm muss subjektives Recht gewähren
- Adressat: Klagebefugnis grundsätzlich gegeben
- Dritter: subjektiv-öffentlich-rechtliche Norm prüfen (Baurecht Nachbarrecht Konkurrentenklage)

## Schritt 5 — Frist

- **Widerspruch** ein Monat ab Bekanntgabe § 70 VwGO
- **Klage** ein Monat ab Bekanntgabe Widerspruchsbescheid § 74 VwGO
- **Klage ohne Vorverfahren** ein Monat ab Bekanntgabe VA § 74 VwGO
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr § 58 Abs. 2 VwGO
- **Wiedereinsetzung** § 60 VwGO innerhalb zwei Wochen ab Wegfall

**Bekanntgabe-Fiktion**

- **§ 41 Abs. 2 Satz 1 VwVfG** vier Tage nach Aufgabe zur Post bei Inland-Bescheid (seit 01.01.2025 PostModG — vorher drei Tage)
- **§ 41 Abs. 2 Satz 2 VwVfG** elektronisch übermittelter Bescheid gilt vier Tage nach Absendung als bekannt gegeben (seit 01.01.2025 PostModG — vorher drei Tage)
- **§ 41 Abs. 2a VwVfG** Bekanntgabe durch Abruf über öffentlich zugängliche Netze (Portal-Zustellung mit Einwilligung): gilt am Tag nach dem Abruf als bekannt gegeben

## Schritt 6 — Vorläufiger Rechtsschutz

### Anfechtungs-Konstellation

- **§ 80 Abs. 1 VwGO** aufschiebende Wirkung von Widerspruch / Anfechtungsklage
- **§ 80 Abs. 2 VwGO Ausnahmen** öffentliche Abgaben sofortige Vollziehung gesetzlich angeordnet
- **§ 80 Abs. 5 VwGO** Antrag auf Wiederherstellung / Anordnung aufschiebender Wirkung
- **§ 80a VwGO** Begünstigung Dritter Konkurrentenkonstellation

### Verpflichtungs-/Leistungs-Konstellation

- **§ 123 VwGO** einstweilige Anordnung
- **Sicherungsanordnung** zur Sicherung eines Rechtsverhältnisses
- **Regelungsanordnung** zur vorläufigen Regelung

### Eilbedürftigkeit

- Drohender Nachteil substantiieren
- Anordnungsgrund glaubhaft machen § 920 ZPO analog (§ 123 Abs. 3 VwGO iVm)
- Hauptsachevorwegnahme nur ausnahmsweise

## Schritt 7 — Streitwert § 52 GKG

- **Verwaltungsstreitigkeit** EUR 5000 Auffangwert § 52 Abs. 2 GKG
- **Bedeutung-konkretisiert** wenn quantifizierbar
- **Beamtenrecht** typisch Bezüge zwölf Monate
- **Baurecht Nachbarklage** EUR 7500 bis 15000 typisch
- **Asyl** EUR 5000

## Schritt 8 — Erfolgsaussicht

- Formal: Frist Form Begründung
- Material: Tatsachen Rechtsanwendung Ermessen Verhältnismäßigkeit
- Verfahrensfehler: Anhörung § 28 VwVfG Begründung § 39 VwVfG Bestimmtheit § 37 Abs. 1 VwVfG
- Ermessensfehler: Unterschreitung / Überschreitung / Fehlgebrauch / Nichtgebrauch

## Praktische Empfehlung

| Konstellation | Empfehlung |
|---|---|
| Bescheid frisch — ein-Monats-Frist offen — Erfolgsaussicht eindeutig | Widerspruch (oder direkt Klage wo Vorverfahren entfallen) |
| Sofortige Vollziehung angeordnet — Frist offen | parallel § 80 Abs. 5 VwGO |
| Drohender Vollzug — Antrag steht aus | § 123 VwGO Eilantrag |
| Frist nahezu abgelaufen — Klärung der Erfolgsaussicht offen | Widerspruch jetzt einlegen — Begründung später |
| Frist verstrichen — Rechtsbehelfsbelehrung fehlerhaft | Ein-Jahres-Frist § 58 Abs. 2 VwGO prüfen |

## Ausgabe

- `erstpruefung-{az}.md` Memo nach Gutachtenstil
- Empfehlung: Widerspruch / Klage / Eilantrag / Kombination
- Frist im Fristenbuch (Hauptfrist Vorfrist)
- Streitwert-Anzeige zur Kostenabschätzung
- Mandatsvereinbarung Vorlage

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quellen

- VwGO §§ 40 ff. 42 43 47 58 60 68 70 74 75 80 80a 123
- VwVfG §§ 28 35 37 39 41
- GKG § 52
- BVerwGE Std.Spruch zur Klagebefugnis und Schutznorm
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Eyermann VwGO
