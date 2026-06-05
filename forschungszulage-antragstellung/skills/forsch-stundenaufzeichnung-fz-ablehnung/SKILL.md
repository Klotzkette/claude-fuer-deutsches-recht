---
name: forsch-stundenaufzeichnung-fz-ablehnung
description: "Forsch Stundenaufzeichnung FZ Ablehnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Forsch Stundenaufzeichnung FZ Ablehnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Forsch Stundenaufzeichnung FZ Ablehnung** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `forsch-stundenaufzeichnung-leitfaden` | Leitfaden Stundenaufzeichnung FZulG: zuwendungsfaehige Personalkosten, eigene Beschaeftigte, Auftragsforschung, Dokumentationspflichten. Pruefraster fuer Personalcontrolling. |
| `fz-ablehnung-nachbesserung-einspruch` | Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-Widerspruch, Finanzamt-Kürzung, Einspruch nach AO, neue Tatsachen, Beleg- und Textreparatur, Klage Finanzgericht als Ultima Ratio. Mit Fristenmatrix, Reparaturplan und Mustertexten. |
| `fz-bemessungsgrundlage-2026` | Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, KMU-Erhöhung. Mit Personalkostenformel, Stundenaufzeichnungsstruktur und Pitfalls zum Gesellschafter-Geschäftsführer. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **Forsch Stundenaufzeichnung FZ Ablehnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `forsch-stundenaufzeichnung-leitfaden`

**Fokus:** Leitfaden Stundenaufzeichnung FZulG: zuwendungsfaehige Personalkosten, eigene Beschaeftigte, Auftragsforschung, Dokumentationspflichten. Pruefraster fuer Personalcontrolling.

# Forsch: Stundenaufzeichnung

## Spezialwissen: Forsch: Stundenaufzeichnung
- **Spezialgegenstand:** Forsch: Stundenaufzeichnung / forsch stundenaufzeichnung leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FZulG.
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

## 2. `fz-ablehnung-nachbesserung-einspruch`

**Fokus:** Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-Widerspruch, Finanzamt-Kürzung, Einspruch nach AO, neue Tatsachen, Beleg- und Textreparatur, Klage Finanzgericht als Ultima Ratio. Mit Fristenmatrix, Reparaturplan und Mustertexten.

# Ablehnung, Nachbesserung, Einspruch

## Worum geht es

Ablehnungen und Nachforderungen kommen vor — die häufigsten Gründe sind nicht "verlorene Fälle", sondern reparable Schwächen in der Projektbeschreibung oder der Belegfähigkeit. Dieser Skill trennt sauber die beiden Ebenen (BSFZ vs. Finanzamt), führt durch den Reparaturprozess, sichert Fristen und liefert Mustertexte.

## Wann dieses Modul hilft

- Bei BSFZ-Rückfrage oder ablehnender Bescheinigung.
- Bei Finanzamt-Bescheid mit Kürzung oder Ablehnung.
- Vor jedem Einspruch.
- Wenn unklar ist, welche Ebene den Bescheid kritisiert (BSFZ vs. Finanzamt).

## Sachrahmen — die zwei Ebenen sauber trennen

| Ebene | Prüft | Rechtsbehelf |
| --- | --- | --- |
| BSFZ | FuE-Eigenschaft des Vorhabens | Widerspruch / neuer Antrag (vom Antragsteller mit BSFZ-Verfahrensregeln zu prüfen) |
| Finanzamt | Höhe, Personalkosten, Bemessungsgrundlage, Festsetzung | Einspruch nach § 347 ff. AO; Klage Finanzgericht |

Einspruchsfrist beim Finanzamt grundsätzlich **ein Monat** ab Bekanntgabe (§ 355 AO — vom Antragsteller mit konkreter Fassung zu prüfen).

## Praxisleitfaden — die häufigsten Ablehnungsgründe

### BSFZ — typische Ablehnungs-/Rückfrage-Gründe

- **Fehlende Neuheit.** "Stand der Technik nicht ausreichend zitiert" / "Vorhaben deckt sich mit bestehenden Verfahren".
- **Unzureichende Beschreibung der Unsicherheit.** Risiko nur allgemein erwähnt, nicht spezifiziert.
- **Routine-Verdacht.** Vorhaben ähnelt zu sehr Wartung, Customizing, Serienpflege.
- **Mangelhafte Abgrenzung.** Routine-Anteile sind im Vorhaben enthalten oder nicht offen gelegt.
- **Marketing-Sprache** ohne technischen Inhalt.

### Finanzamt — typische Kürzungs-/Ablehnungsgründe

- **Personalkosten-Höhe** zweifelhaft: Bruttoansätze, SV-Beiträge, Altersvorsorge nicht ausreichend belegt.
- **FuE-Anteilberechnung** nicht plausibel: keine Stundenaufzeichnung, nur Pauschalannahmen.
- **Auftragsforschung:** Auftragnehmer außerhalb EU/EWR, Vertrag fehlt Leistungsbeschreibung, 70-Prozent-Kürzung nicht angewandt.
- **Eigenleistung:** Gesellschafter-Geschäftsführer doppelt (Lohn + Eigenleistung), 40-Stunden-Cap überschritten.
- **AGVO-Kumulierung:** Höchstintensität überschritten.
- **Wirtschaftsjahr-Zuordnung:** Aufwendungen falschem Jahr zugeordnet.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| BSFZ-Widerspruch vs. neuer Antrag | gleiche AZ-Linie | sauberer Neustart | neuer Antrag, wenn grundlegende Schwächen |
| Nachbesserung vs. Einspruch | informeller Dialog | förmlicher Rechtsbehelf | Nachbesserung zuerst, Einspruch fristwahrend |
| Klage Finanzgericht vs. Verhandlungslösung | grundsätzlich klären | pragmatische Einigung | Verhandlung bevorzugen, Klage Ultima Ratio |
| Vollständige Neufassung vs. Stellungnahme | hoher Aufwand, hohe Erfolgsquote | niedriger Aufwand, geringeres Ergebnis | Neufassung bei tragenden Schwächen |

## Fristen — die wichtigsten Daten

| Vorgang | Frist | Hinweis |
| --- | --- | --- |
| Einspruch Finanzamt-Bescheid | grundsätzlich 1 Monat ab Bekanntgabe | § 355 AO; Bekanntgabefiktion § 122 AO; vom Antragsteller live zu prüfen |
| Klage Finanzgericht | 1 Monat nach Einspruchsentscheidung | § 47 FGO |
| BSFZ-Rückfrage | Frist im Rückfragebrief der BSFZ | unbedingt einhalten, sonst Ablehnung |
| BSFZ-Widerspruch | nach Maßgabe des Bescheinigungsbescheids | Antragsteller mit Bescheid abgleichen |

## Schritt für Schritt — Reparaturplan

1. Bescheid / Rückforderung vollständig auswerten: was wird gerügt, auf welcher Ebene?
2. Ebene zuordnen (BSFZ vs. Finanzamt).
3. Frist eintragen, Mahnung im Kalender setzen.
4. Konkret rugierte Punkte auflisten.
5. Reparatur planen:
 a. Welche Tatsachen sind ergänzungsfähig?
 b. Welche Belege fehlen?
 c. Welche Formulierungen sind missverständlich?
6. Bei BSFZ: ergänzende Stellungnahme oder neuer Antrag.
7. Bei Finanzamt: Einspruch fristwahrend einlegen, Begründung folgt.
8. Verhandlungsgespräch mit Sachbearbeiter prüfen.
9. Bei Stillstand: Klage Finanzgericht erst nach gescheiterter Einspruchsentscheidung.

## Mustertexte

**Einspruch Finanzamt (fristwahrend):**

"Sehr geehrte Damen und Herren,

namens und in Vollmacht der [Mandantin] lege ich gegen den Forschungszulagenbescheid vom [Datum], Steuernummer [...], Einspruch ein.

Die Begründung folgt nach Akteneinsicht. Wir bitten um vorläufige Aussetzung der Vollziehung gemäß § 361 AO, soweit die Festsetzung über den unstreitigen Teil hinausgeht. Akteneinsicht wird beantragt.

Mit freundlichen Grüßen [Berufsbezeichnung]."

**Stellungnahme an BSFZ (Vorlage, bei Rückfrage zur Neuheit):**

"Sehr geehrte Damen und Herren,

zur Rückfrage vom [Datum] in Sachen Antrag [AZ] nehmen wir wie folgt Stellung:

1. Stand der Technik: Wir ergänzen die Quellen [neue Quellen 1, 2]. Die Recherche zeigt, dass die spezifische Kombination [A] mit [B] dort nicht beschrieben ist.

2. Neuheit: Die Neuheit liegt in [konkretes technisches Merkmal]. Im Unterschied zum Stand der Technik [Punkt 1, Punkt 2].

3. Technische Unsicherheit: [konkrete Hürde, Voruntersuchungen, vergleichbare gescheiterte Vorhaben].

4. Abgrenzung zur Routine: Folgende Tätigkeiten gehören nicht zum Vorhaben: [Aufzählung].

Mit freundlichen Grüßen [Verfasser]."

**Reparaturplan-Tabelle:**

| Kritikpunkt | Ebene | Reparatur | Belegnachschub | Fristtag |
| --- | --- | --- | --- | --- |
| Stand der Technik unzureichend | BSFZ | zwei Quellen ergänzen | Patentrecherche | TT.MM.JJJJ |
| Personalkosten nicht belegt | FA | Lohnkonten beifügen | Lohnabrechnung 12/JJJJ | TT.MM.JJJJ |
| FuE-Anteil zu hoch | FA | Stundenaufzeichnung beifügen | Auszug aus Zeiterfassung | TT.MM.JJJJ |

## Typische Fehler

- Frist versäumt, weil Einspruch erst nach interner Beratung formuliert wurde — Einspruch fristwahrend einlegen, Begründung nachreichen.
- BSFZ und Finanzamt verwechselt — Einspruch bei der falschen Stelle.
- Inhaltliche Neufassung statt sachlicher Stellungnahme — wirkt unkooperativ.
- Belege ohne Bezug zum konkreten Kritikpunkt eingereicht.
- Klage Finanzgericht vor Einspruchsentscheidung erhoben.

## Output

- Kritik-Synopse (Ebene, Punkt, Bewertung).
- Reparaturplan mit Verantwortlichen und Fristen.
- Antwortentwurf (BSFZ-Stellungnahme oder Einspruchsbegründung).
- Einspruchsentwurf fristwahrend, sobald Finanzamt-Bescheid betroffen.
- Liste fehlender Belege.

## Querverweise

- `fz-bsfz-bescheinigung-projektbeschreibung` für die Neufassung der Projektbeschreibung.
- `fz-bemessungsgrundlage-2026` für die Personalkostenreparatur.
- `fz-dokumentationspaket-betriebspruefung` für Belegnachschub.
- `fz-kumulierung-beihilfen-agvo` bei AGVO-Kürzungen.

## Quellen Stand 05/2026

- AO §§ 347 bis 367 (Einspruchsverfahren) und § 355 AO (Frist) — vom Antragsteller mit konsolidierter Fassung zu prüfen.
- FGO § 47 (Klagefrist).
- BSFZ-Verfahrensregeln.
- FZulG.
- `references/forschungszulage-quellen-und-zahlen.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `fz-bemessungsgrundlage-2026`

**Fokus:** Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, KMU-Erhöhung. Mit Personalkostenformel, Stundenaufzeichnungsstruktur und Pitfalls zum Gesellschafter-Geschäftsführer.

# Bemessungsgrundlage 2026

## Worum geht es

Die Höhe der Forschungszulage hängt nicht von der BSFZ ab, sondern allein von den ansatzfähigen Aufwendungen und dem Höchstbetrag der Bemessungsgrundlage (BMG). Dieser Skill liefert die Berechnungslogik, die Personalkostenformel, die Behandlung von Auftragsforschung und Eigenleistung sowie typische Pitfalls.

Stand 2026 — alle Zahlen vom Antragsteller mit aktueller Gesetzesfassung und BMF-Verwaltungsanweisungen abzugleichen.

## Wann dieses Modul hilft

- Vor dem Finanzamt-Antrag, zur belastbaren Berechnung.
- Bei Sanity-Check der ersten Förderhöhenschätzung.
- Bei der Trennung Eigenforschung / Auftragsforschung.
- Wenn Gesellschafter-Geschäftsführer mitarbeitet (Stolperfalle).
- Bei Mehrjahresvorhaben für die jährliche Aufteilung.

## Sachrahmen — BMG-Komponenten und Caps

| Komponente | Ansatz | Maximum/Bedingung |
| --- | --- | --- |
| Eigene FuE-Personalkosten | Bruttolohn + Arbeitgeberanteil zur Sozialversicherung + Altersvorsorge | nur FuE-Anteil je Mitarbeiter |
| Eigenleistung Einzelunternehmer/persönlich tätiger Gesellschafter | ab 2026 pauschal 100 Euro je Arbeitsstunde | max. 40 Stunden je Woche |
| Auftragsforschung | 70 Prozent der Kosten | Auftragnehmer muss seine Geschäftsleitung in EU/EWR haben; bei EWR-Staaten zusätzlich Amtshilfevoraussetzung nach § 2 Abs. 5 FZulG prüfen; klare Leistungsbeschreibung |
| Wirtschaftsgüter | AfA, soweit dem FuE-Vorhaben zuordenbar | bewegliche abnutzbare Wirtschaftsgüter des Anlagevermögens |
| Gemein- und Betriebskosten | pauschal 20 Prozent der übrigen förderfähigen Aufwendungen | nur für Vorhaben mit Beginn nach 31.12.2025 |

**BMG-Höchstbetrag:** ab 01.01.2026 12 Mio. Euro pro Wirtschaftsjahr (verbundene Unternehmen ggf. gemeinsam — vom Antragsteller live zu prüfen).

**Fördersatz:** 25 Prozent; KMU-Erhöhung um 10 Prozentpunkte möglich (Antragstellervoraussetzungen prüfen).

## Praxisleitfaden — Personalkostenformel und Pitfalls

### Personalkostenformel

Förderfähige Personalkosten je Mitarbeiter und Wirtschaftsjahr:

```
PK_je_MA = (Bruttolohn + Arbeitgeber-SV + Altersvorsorge) × FuE-Anteil
```

FuE-Anteil ist der dokumentierte Zeitanteil aus der Stundenaufzeichnung. Pauschale Annahmen ("Herr X arbeitet zu 60 Prozent in der FuE") halten der Außenprüfung nicht stand.

### Beispiel Brutto-TV-L 13 (rein illustrativ; Werte vom Antragsteller mit aktueller Lohnabrechnung zu ersetzen)

- Bruttojahreslohn: 65.000 Euro
- Arbeitgeber-SV ca. 13.000 Euro
- Altersvorsorge ca. 4.500 Euro
- Personalvollkosten 82.500 Euro
- Dokumentierter FuE-Anteil 70 Prozent
- Förderfähig: 82.500 × 0.70 = 57.750 Euro
- Bei 25 Prozent Fördersatz: Zulage 14.437 Euro je Mitarbeiter
- Bei KMU-Erhöhung 35 Prozent: 20.212 Euro

### Stundenaufzeichnung — die Pflichtspalten

| Datum | Person | Vorhaben/AP | Stunden | Tätigkeit (FuE-konkret) | Kürzel Auftrag/Eigen |
| --- | --- | --- | --- | --- | --- |
| 12.03.2026 | M. Müller | V-1 / AP-2 | 6.5 | Aufbau Messreihe Variante A, Kalibrierung | E |
| 12.03.2026 | M. Müller | Service | 1.5 | Wartung Bestandsanlage | N |

- `E` = Eigenforschung, `A` = Auftragsforschung, `N` = nicht FuE.
- Schon dieses Detail genügt vielen Außenprüfern, weil es Konsistenz zur Projektakte zeigt.

### Eigenleistung Einzelunternehmer / persönlich tätiger Gesellschafter

- Pauschale 100 Euro je Stunde, max. 40 Stunden je Woche, ab 2026 (vom Antragsteller mit aktueller Fassung zu prüfen).
- **Pitfall Gesellschafter-Geschäftsführer:** Wer als GmbH-Gesellschafter-Geschäftsführer ein Gehalt bezieht, fällt nicht automatisch in die Eigenleistung. Die Personalkosten werden über die Lohnabrechnung berücksichtigt. Doppelansatz vermeiden.
- **Pitfall Einzelunternehmer:** Eigenleistung ist die einzige Möglichkeit, weil keine Lohnabrechnung existiert.

### Auftragsforschung — die 70-Prozent-Regel

- Förderfähig nur 70 Prozent der Kosten.
- Auftragnehmer muss seine Geschäftsleitung in einem EU-Mitgliedstaat oder in einem EWR-Staat mit ausreichender Amtshilfe nach § 2 Abs. 5 FZulG haben. Eine außerhalb dieses Rahmens ansässige Forschungseinrichtung ist für die Auftragsforschungsregel nicht förderfähig.
- **Klare Leistungsabgrenzung im Vertrag.** Wer was wann mit welchem Ziel.
- Subunternehmer des Auftragnehmers werden mitgeprüft.
- Verbundene Unternehmen sind kritisch — die BSFZ und das Finanzamt prüfen genau, ob es sich nicht doch um eigene FuE im Konzern handelt.

### Wirtschaftsgüter / AfA

- Nur bewegliche, abnutzbare Wirtschaftsgüter des Anlagevermögens.
- Anteilige AfA, soweit dem FuE-Vorhaben zugeordnet.
- Keine Grundstücke, keine Software-Lizenzen mit Sonderregeln (Einzelfall prüfen).

### 20-Prozent-Gemeinkostenpauschale

- Für Vorhaben mit Beginn nach 31.12.2025.
- 20 Prozent der übrigen förderfähigen Aufwendungen (eigene Personalkosten + Eigenleistung + 70-Prozent-Auftrag + AfA).
- Keine Belegpflicht für die Pauschale selbst — die Pauschale ersetzt die Einzelbelegnahme der Gemeinkosten.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Eigenforschung vs. Auftragsforschung | 100 Prozent BMG | 70 Prozent BMG | Eigen bevorzugen, wenn Personal vorhanden |
| Gesellschafter Eigenleistung vs. Lohn | 100 Euro/Std., 40-Stunden-Cap | reguläre Personalkosten | Lohn meist günstiger ab ca. 30 Euro/Std. Vollkosten |
| Vollverteilung vs. konservativ | maximal anteilig | nur dokumentierte Stunden | konservativ; Außenprüfung honoriert das |
| Sammel-AP vs. detaillierte AP | weniger Verwaltung | bessere Nachvollziehbarkeit | detaillierte AP für Außenprüfung |

## Schritt für Schritt

1. Wirtschaftsjahr und Vorhaben festlegen.
2. Pro Mitarbeiter Lohnkosten + SV + Altersvorsorge ermitteln.
3. FuE-Anteil aus Stundenaufzeichnung ermitteln (Stundenzahl FuE / Stundenzahl gesamt).
4. Auftragsforschungskosten aus Rechnungen sammeln, mit 70 Prozent ansetzen.
5. Eigenleistung Einzelunternehmer / persönlich tätiger Gesellschafter mit 100 Euro × dokumentierte Stunden (max. 40/Woche).
6. AfA für Wirtschaftsgüter anteilig zuordnen.
7. Zwischensumme bilden.
8. 20-Prozent-Gemeinkostenpauschale auf die Zwischensumme aufschlagen (sofern Vorhabensbeginn nach 31.12.2025).
9. BMG-Cap prüfen (12 Mio. Euro/Jahr).
10. Fördersatz anwenden (25 Prozent oder 35 Prozent KMU).
11. Drei Szenarien dokumentieren: konservativ / realistisch / maximal.

## Datenqualitäts-Ampel

| Ampel | Datenlage | Behandlung |
| --- | --- | --- |
| Grün | Lohnkonten, Stunden je AP, BSFZ-Bescheid, Verträge/Rechnungen liegen vor | belastbare Berechnung |
| Gelb | Stunden plausibel, aber nacherfasst; Auftragsvertrag lückenhaft | Berechnung mit Risikoabschlag und Nachforderungsplan |
| Rot | nur Managementschätzung, keine AP-Zuordnung, unklare Auftragnehmer | keine Betragszusage; erst Dokumentation reparieren |

## Mustertexte / Vorlagen

**Berechnungstabelle (Vorlage):**

| Komponente | Brutto | Faktor | Förderfähig |
| --- | --- | --- | --- |
| Personalkosten Mitarbeiter A | 82.500 Euro | 70 Prozent | 57.750 Euro |
| Personalkosten Mitarbeiter B | 75.000 Euro | 50 Prozent | 37.500 Euro |
| Eigenleistung Gesellschafter | 100 Euro × 800 Std. | 100 Prozent | 80.000 Euro |
| Auftragsforschung Institut X | 120.000 Euro | 70 Prozent | 84.000 Euro |
| AfA Maschine M-12 | 40.000 Euro | 60 Prozent | 24.000 Euro |
| Zwischensumme | | | 283.250 Euro |
| 20 Prozent Pauschale | | | 56.650 Euro |
| Bemessungsgrundlage | | | 339.900 Euro |
| Forschungszulage 25 Prozent | | | 84.975 Euro |
| Forschungszulage 35 Prozent (KMU) | | | 118.965 Euro |

**Anteilssatz-Plausibilität:** Wenn ein Mitarbeiter zu 90 Prozent in FuE arbeitet, muss in der Stundenaufzeichnung diese Quote nachweisbar sein. Das Finanzamt vergleicht Lohnkonto, Tätigkeitsbeschreibung und Stundenaufzeichnung.

## Typische Fehler

- Vollkosten ohne Stundennachweis hochgerechnet.
- Auftragsforschung mit 100 Prozent statt 70 Prozent angesetzt.
- Gesellschafter-Geschäftsführer doppelt (Lohn + Eigenleistung).
- Auftragsforschung außerhalb EU/EWR mit angesetzt.
- 20-Prozent-Pauschale auf nicht-zulässige Posten angewendet.
- 12-Mio-Cap übersehen bei verbundenen Unternehmen.

## Output

- Berechnungstabelle pro Wirtschaftsjahr.
- Beleganforderungsliste (Lohnkonten, Verträge, Rechnungen, AfA-Plan).
- Sensitivitätsanalyse konservativ / realistisch / maximal.
- Hinweis auf KMU-Voraussetzungen und Erhöhungs-Antrag (separat zu prüfen).

## Querverweise

- `fz-finanzamt-festsetzung-auszahlung` für die Antragstellung beim Finanzamt.
- `fz-dokumentationspaket-betriebspruefung` für die Belegfähigkeit.
- `fz-kumulierung-beihilfen-agvo` für AGVO-Höchstintensität.
- `fz-roadmap-mehrjahresantrag` für die Aufteilung über Wirtschaftsjahre.

## Quellen Stand 05/2026

- FZulG, insbesondere §§ 3, 4, 5 (vom Antragsteller mit konsolidierter Fassung zu prüfen).
- Wachstumschancengesetz, Auftragsforschungsregelung 70 Prozent.
- Steuerliches Investitionssofortprogramm 2025/2026: https://www.bescheinigung-forschungszulage.de/steuerliches-investitionssofortprogramm
- `references/forschungszulage-quellen-und-zahlen.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
