---
name: defensive-drafting-deutscher-kanzleistil
description: "Defensive Drafting Deutscher Kanzleistil: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Defensive Drafting Deutscher Kanzleistil

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Defensive Drafting Deutscher Kanzleistil** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `defensive-drafting-fallen-erkennen` | Defensives Drafting beim Review fremder Entwuerfe. Erkennt die zwoelf haeufigsten Fallen: kaschierte Haftungsfreistellung, verschobene Beweislast, einseitiger Gerichtsstand, unfaire Aenderungsvorbehalte, kurze Verjaehrungsverkuerzung, Nachhaftung der Geschaeftsfuehrung, Lock-in-Mechanismen Auto-Renewal, Schiedsklauseln mit Kostenrisiko, Closing-Bedingungen unter Gegnerkontrolle, Service-Level ohne Sanktion, Audit-Rechte ohne Reziprozitaet, Sprachklausel und Gerichtsstandsklausel divergierend. Mit Beispielklauseln, Roten-Flaggen-Wortliste und Verteidigungsformulierungen. |
| `deutscher-kanzleistil-kalibrieren` | Kalibriert juristische Texte auf den passenden deutschen Kanzleistil: Frankfurter Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht oder Behörde. Erstellt ein Stilprofil mit Ton, Satzlänge, Gliederung, Anrede, Risikoniveau, Schärfegrad und No-Go-Formulierungen und überarbeitet Beispielpassagen in diesem Register. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Defensive Drafting Deutscher Kanzleistil**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `defensive-drafting-fallen-erkennen`

**Fokus:** Defensives Drafting beim Review fremder Entwuerfe. Erkennt die zwoelf haeufigsten Fallen: kaschierte Haftungsfreistellung, verschobene Beweislast, einseitiger Gerichtsstand, unfaire Aenderungsvorbehalte, kurze Verjaehrungsverkuerzung, Nachhaftung der Geschaeftsfuehrung, Lock-in-Mechanismen Auto-Renewal, Schiedsklauseln mit Kostenrisiko, Closing-Bedingungen unter Gegnerkontrolle, Service-Level ohne Sanktion, Audit-Rechte ohne Reziprozitaet, Sprachklausel und Gerichtsstandsklausel divergierend. Mit Beispielklauseln, Roten-Flaggen-Wortliste und Verteidigungsformulierungen.

# Defensive Drafting und Fallen-Erkennung

## Zweck

Beim Review fremder Vertragsentwuerfe verlieren Mandanten regelmaessig viel Geld nicht durch boese Absicht, sondern durch routinierte Standardklauseln, die einseitig zu ihrem Nachteil wirken. Dieser Skill ist eine Pruefcheckliste fuer die zwoelf haeufigsten Fallen: woran Sie sie erkennen (Rote-Flaggen-Wortliste), warum sie problematisch sind (rechtliche Wirkung) und wie Sie sie chirurgisch entschaerfen (Verteidigungsklauseln).

Er ergaenzt `agb-konforme-klauseln-305-310-bgb` (AGB-Inhaltskontrolle) und `haftungsausschluss-und-haftungsbegrenzung` (Haftungsklauseln), schaut aber breiter auf das Vertragswerk.

## Eingaben

- Fremder Vertragsentwurf (Lieferant, Kunde, M&A-Gegenseite, IT-Anbieter)
- Rolle des Mandanten (Kaeufer, Verkaeufer, Auftraggeber, Auftragnehmer)
- Verhandlungsmacht (oben, gleichauf, unten)
- Branche und Vertragswert (bestimmt Risikoschwelle)

## Rechtlicher und methodischer Rahmen

- § 43a BRAO Sorgfaltspflicht: Mandant ist auf einseitige Klauseln hinzuweisen, auch wenn rechtlich wirksam.
- §§ 305-310 BGB: AGB-Recht als erste Verteidigungslinie, vgl. `agb-konforme-klauseln-305-310-bgb`.
- § 138 BGB Sittenwidrigkeit und § 242 BGB Treu und Glauben: Auffangnormen jenseits des AGB-Rechts.
- Verhandlungsdoktrin: Streichen, ersetzen, gegen-ersetzen. Nicht jede Falle wird gestrichen; manche werden gespiegelt.

## Die zwoelf Fallen

### Falle 1: Kaschierte Haftungsfreistellung

**Rote-Flaggen-Wortliste:** "Schadensersatz nur bei Vorsatz", "Haftung ist auf den vertragstypischen Schaden begrenzt", "indirekte Folgeschaeden sind ausgeschlossen", "Mangelfolgeschaeden sind ausgeschlossen", "Haftung der Hoehe nach begrenzt auf den Auftragswert".

**Wirkung:** Begrenzt die Haftung des Vertragspartners auf einen Teil seines Verschuldens. In AGB regelmaessig unwirksam nach § 309 Nr. 7 BGB; im Individualvertrag wirksam.

**Verteidigung:**
- Pruefen, ob Klausel in AGB: dann oft § 309 Nr. 7 BGB einschlaegig.
- Ausnahmen einfuegen: "Die Haftungsbegrenzung gilt nicht fuer Schaeden aus der Verletzung des Lebens, des Koerpers oder der Gesundheit, fuer Schaeden aus vorsaetzlicher oder grob fahrlaessiger Pflichtverletzung und fuer Schaeden aus der Verletzung wesentlicher Vertragspflichten (Kardinalpflichten)."
- Hoehe an Versicherungssumme koppeln statt an Auftragswert.

### Falle 2: Verschobene Beweislast

**Rote-Flaggen-Wortliste:** "Der Auftragnehmer haftet, wenn er die Schadensursache nicht widerlegt", "Der Besteller hat die Mangelfreiheit zu beweisen", "Im Zweifel gilt", "Die Lieferung gilt als genehmigt".

**Wirkung:** Kehrt die gesetzliche Beweislast um. In AGB oft Verstoss gegen § 309 Nr. 12 BGB.

**Verteidigung:** Klausel streichen und die gesetzliche Beweislastverteilung herstellen. Wenn nicht durchsetzbar, Beweislast spiegeln (gilt fuer beide Seiten).

### Falle 3: Einseitiger Gerichtsstand

**Rote-Flaggen-Wortliste:** "Ausschliesslicher Gerichtsstand ist Muenchen", "Der Auftragnehmer kann auch am Sitz des Auftraggebers klagen", "Gerichtsstand fuer alle Streitigkeiten ist Hamburg".

**Wirkung:** Belastet den Mandanten mit hohen Reisekosten und unbekannter Gerichtsbarkeit. Im B2C oft unwirksam nach § 38 ZPO, im B2B regelmaessig wirksam.

**Verteidigung:** Wechselseitig: Klaeger klagt am Sitz des Beklagten. Oder neutraler dritter Gerichtsstand (z. B. Frankfurt am Main).

### Falle 4: Unfairer Aenderungsvorbehalt

**Rote-Flaggen-Wortliste:** "Der Anbieter behaelt sich vor, die Leistungen jederzeit anzupassen", "Preisaenderungen werden mit einer Frist von vier Wochen wirksam", "Aenderungen dieser AGB werden per E-Mail mitgeteilt und gelten als angenommen".

**Wirkung:** Vertragsumgestaltung waehrend der Laufzeit. AGB-Verstoss gegen § 308 Nr. 4, § 309 Nr. 1, § 307 BGB.

**Verteidigung:**
- Aenderungen nur mit beidseitiger Schriftform.
- Preisanpassung an objektiven Index (z. B. Verbraucherpreisindex Statistisches Bundesamt) koppeln.
- Schweigen ist keine Annahme: explizite Zustimmung.
- Sonderkuendigungsrecht bei jeder einseitigen Aenderung.

### Falle 5: Kurze Verjaehrungsverkuerzung

**Rote-Flaggen-Wortliste:** "Maengelansprueche verjaehren in zwoelf Monaten ab Lieferung", "Ansprueche verjaehren spaetestens nach einem Jahr".

**Wirkung:** Verkuerzt die regulaere Verjaehrung von zwei Jahren (§ 438 BGB) oder fuenf Jahren (Bauwerk). In B2C nichtig bei Neuware (§ 476 II BGB neu); in B2B grundsaetzlich zulaessig, in AGB Pruefung nach § 307 BGB.

**Verteidigung:** Verjaehrungsregelung auf gesetzliches Mass zurueckfuehren. Bei Software und IT-Werken auf zwei Jahre. Bei Bauwerken auf fuenf Jahre.

### Falle 6: Nachhaftung der Geschaeftsfuehrung

**Rote-Flaggen-Wortliste:** "Die Geschaeftsfuehrer haften persoenlich gesamtschuldnerisch", "Die Geschaeftsfuehrung garantiert die Richtigkeit der Angaben", "buergt persoenlich".

**Wirkung:** Durchgriffshaftung der Organe. Wirksam, aber regelmaessig nicht gewollt. Steuerlich problematisch.

**Verteidigung:** Geschaeftsfuehrerhaftung streichen oder durch D&O-Versicherung deckeln. Garantien nur fuer Sachverhalte, nicht fuer Rechtsfolgen.

### Falle 7: Lock-in durch Auto-Renewal

**Rote-Flaggen-Wortliste:** "Der Vertrag verlaengert sich automatisch um ein Jahr, sofern nicht drei Monate vor Ablauf gekuendigt wird", "stillschweigende Verlaengerung", "Kuendigung muss schriftlich erfolgen, sonst Verlaengerung".

**Wirkung:** Mandant haengt im Vertrag, weil Kuendigungsfrist verpasst wurde. In B2C teilweise nichtig nach FairCV-Gesetz; in B2B AGB-rechtlich problematisch nach § 309 Nr. 9 BGB.

**Verteidigung:**
- Erinnerungspflicht des Anbieters einbauen: "Der Anbieter erinnert den Kunden spaetestens drei Monate vor Ablauf an die Kuendigungsmoeglichkeit. Unterlaesst er dies, verlaengert sich der Vertrag nicht."
- Kuendigungsfrist auf maximal einen Monat.
- Verlaengerung maximal um sechs Monate (nicht ein Jahr).

### Falle 8: Schiedsklauseln mit Kostenrisiko

**Rote-Flaggen-Wortliste:** "Streitigkeiten werden durch Schiedsgericht der ICC entschieden", "ICDR Arbitration in New York", "DIS Schiedsgerichtsordnung", "der unterlegene Teil traegt die Schiedskosten".

**Wirkung:** Hohes Kostenrisiko (Schiedskosten teilweise sechsstellig) und Ausschluss der staatlichen Gerichte. Wirksam.

**Verteidigung:**
- Wertgrenze fuer Schiedsklausel: erst ab Streitwert X.
- Mediationsstufe vorgeschaltet.
- DIS Sport-Schiedsordnung statt ICC bei kleineren Werten.
- Schiedsort am Sitz des Mandanten.

### Falle 9: Closing-Bedingungen unter Gegnerkontrolle

**Rote-Flaggen-Wortliste:** "Closing erfolgt nach Erteilung kartellrechtlicher Freigaben durch den Kaeufer", "Voraussetzung des Closings ist die Zustimmung des Aufsichtsrats des Kaeufers", "Material Adverse Change nach billigem Ermessen des Kaeufers".

**Wirkung:** Kaeufer hat einseitiges Exit-Recht zwischen Signing und Closing.

**Verteidigung:**
- "Reasonable best efforts" zur Beseitigung der Bedingungen.
- Hell-or-High-Water-Klausel: Kaeufer muss bestimmte Auflagen akzeptieren.
- Long-Stop-Date: harte Frist, sonst Vertragsbruch.
- MAC-Klausel auf objektive Kriterien beschraenken (z. B. EBITDA-Drop > 25 Prozent).

### Falle 10: Service-Level ohne Sanktion

**Rote-Flaggen-Wortliste:** "Verfuegbarkeit von 99 Prozent angestrebt", "Bearbeitung erfolgt zeitnah", "Reaktionszeit nach besten Kraeften".

**Wirkung:** Soft-Verpflichtung ohne Konsequenz bei Verstoss. Kein Rechtsanspruch auf Einhaltung.

**Verteidigung:**
- SLA mit Service-Credits: Bei Unterschreitung anteilige Verguetungsrueckgabe.
- Eskalationsstufen (gelb, rot) mit definierten Folgen.
- Ausserordentliches Kuendigungsrecht bei wiederholtem Verstoss.

### Falle 11: Audit-Rechte ohne Reziprozitaet

**Rote-Flaggen-Wortliste:** "Der Anbieter ist berechtigt, die Nutzung der Software zu auditieren", "Die Lizenznehmerin gestattet der Lizenzgeberin Zutritt zu ihren Raeumen".

**Wirkung:** Einseitige Pruefrechte. Bei Auftragsverarbeitung nach DSGVO eigene Kategorie (Art. 28 III lit. h).

**Verteidigung:**
- Reziprozitaet: Auch der Auftraggeber darf den Auftragnehmer auditieren (vgl. DSGVO).
- Vorankuendigung mindestens vier Wochen.
- Geheimhaltungspflicht des Auditors.
- Kosten beim Audierenden.

### Falle 12: Sprachklausel und Gerichtsstandsklausel divergierend

**Rote-Flaggen-Wortliste:** "Vertragssprache ist Englisch, Gerichtsstand Frankfurt", "Im Streitfall gilt die englische Fassung", "Auslegungsfragen unterliegen dem Recht von New York".

**Wirkung:** Deutscher Richter muss englisches Recht anwenden. Hohe Beweisanforderungen an auslaendisches Recht (§ 293 ZPO). Verlangsamung und Kostensteigerung.

**Verteidigung:**
- Vertragssprache und Rechtswahl synchronisieren.
- Bei Bilingualismus: deutsche Fassung als verbindlich erklaeren.
- Schiedsklausel statt staatlichem Gericht erwaegen.

## Ablauf / Checkliste

1. Vertragsentwurf zwoelf-mal durchgehen, jede Falle aktiv suchen.
2. Treffer in einer Risiko-Tabelle erfassen (Klausel, Falle, Risiko, Empfehlung, Verhandelbarkeit).
3. Verteidigungsklauseln als Markup einarbeiten.
4. Reihenfolge der Verhandlung priorisieren: zuerst Hochrisiko-Fallen (1, 5, 9), dann mittleres Risiko (3, 4, 7, 10), dann Detail (12).
5. Pro Klausel den Fallback definieren (was, wenn Gegenseite nicht nachgibt).

## Ausgabeformat

- Tabelle: Klausel-Nummer | Klausel-Auszug | Falle-Nr | Risiko (rot/gelb/gruen) | Verteidigungsformulierung | Fallback.
- Markup-Vorlage fuer Track-Changes im Word-Dokument.
- Mandantenbrief mit Top-3-Risiken in Klartext.

## Querverweise

- `agb-konforme-klauseln-305-310-bgb` fuer AGB-Inhaltskontrolle
- `haftungsausschluss-und-haftungsbegrenzung` fuer Haftungsdrafting
- `klausel-bibliothek-katalog` fuer fertige Verteidigungsformulierungen
- `revisions-prozess-redlines-comparison` fuer den Markup-Workflow

## Quellen (Stand 05/2026)

- §§ 305, 305c, 306, 307, 308, 309, 310 BGB; §§ 38, 293 ZPO; § 138, § 242 BGB; § 43a BRAO.
- DSGVO Art. 28 fuer Audit-Reziprozitaet.
- BGH-Rechtsprechung zur AGB-Inhaltskontrolle und MAC-Klauseln vom Nutzer fundstellengenau zu verifizieren.
- Zitierweise: `references/zitierweise.md`.

## 2. `deutscher-kanzleistil-kalibrieren`

**Fokus:** Kalibriert juristische Texte auf den passenden deutschen Kanzleistil: Frankfurter Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht oder Behörde. Erstellt ein Stilprofil mit Ton, Satzlänge, Gliederung, Anrede, Risikoniveau, Schärfegrad und No-Go-Formulierungen und überarbeitet Beispielpassagen in diesem Register.

# Deutscher Kanzleistil Kalibrieren

## Zweck

Gute juristische Texte klingen nicht überall gleich. Ein Partner-Update in einer M&A-Boutique, ein Mandantenbrief aus einer Familienrechtskanzlei, ein Schriftsatz an ein Landgericht und eine englische Clause Note für einen US-Counsel brauchen verschiedene Register. Dieser Skill macht das Register bewusst und reproduzierbar.

## Stilprofile

| Profil | Wo es passt | Ton | Struktur |
|---|---|---|---|
| Großkanzlei Corporate | Deal, SPA, Term Sheet, Board Memo | knapp, belastbar, entscheidungsorientiert | Executive Summary, Issue List, Options, Recommendation |
| Prozess-Boutique | Schriftsatz, Strategiepapier, Terminvorbereitung | präzise, scharf, aber sachlich | These, Beleg, Beweis, Angriffspunkt |
| Kleinkanzlei Mandat | Mandantenbrief, Vergleich, außergerichtliches Schreiben | menschlich, klar, führend | Sachstand, Einschätzung, Empfehlung, nächste Schritte |
| Inhouse Legal | Management-Memo, Freigabevorlage | lösungsorientiert, risikobasiert | Ampel, Entscheidungspunkt, Budget, Owner |
| Behörde/Gericht | Antrag, Stellungnahme, Schriftsatz | nüchtern, beweisbar, ohne Theater | Antrag, Sachverhalt, Rechtliches, Beweisangebot |
| US/UK-Korrespondenz | Cross-Border Deal, Local Counsel Note | international höflich, nicht übersetzt klingend | Background, German law position, practical consequence |

## Ablauf

1. Bestimme Adressat und Entscheidungssituation.
2. Wähle ein Profil aus der Tabelle oder kombiniere zwei Profile.
3. Lege den Schärfegrad fest: deeskalierend, neutral, bestimmt, hart, prozessual.
4. Lege die Tiefe fest: One-pager, Kurzvermerk, Memo, Schriftsatz, Vertragsfassung.
5. Überarbeite den Text auf Satzlänge, Gliederung, Wortwahl und Ergebnisführung.
6. Gib am Ende ein Stilprofil aus, damit Folge-Skills im gleichen Register weiterarbeiten.

## Stilprofil-Ausgabe

```text
Stilprofil:
- Profil: Großkanzlei Corporate
- Adressat: Partnerin und Mandant
- Ton: knapp, entscheidungsorientiert, ohne Floskeln
- Schärfegrad: neutral-bestimmt
- Satzlänge: kurz bis mittel
- Ergebnisführung: Empfehlung in den ersten fünf Zeilen
- No-Gos: Gutachtenstil, lange historische Herleitung, "dürfte", "wohl" ohne Risikobegründung
```

## Typische No-Gos

- Großkanzlei: keine langen Lehrbuchpassagen, keine ungeordnete Normensammlung.
- Boutique: keine aggressive Rhetorik ohne Beleg.
- Kleinkanzlei: keine überhebliche Belehrung des Mandanten.
- Inhouse: keine Empfehlung ohne Entscheidungspunkt.
- Gericht: keine Pointe, kein Marketington, keine unnötigen Adjektive.
- US/UK: keine wörtliche Übersetzung deutscher Schachtelsätze.

## Output

- Stilprofil.
- Kurze Begründung der Stilwahl.
- Überarbeitete Passage oder Gliederung.
- Hinweis auf passende Folge-Skills, insbesondere `stil-und-ton-juristische-texte`, `schriftsatz-ueberarbeiten-richterlesbar`, `mandantenmemo-und-partner-update` oder `us-uk-legal-writing-fuer-deutsche`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
