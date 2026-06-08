---
name: inso-ki-anfechtungsansprueche-schuldnerakten
description: "KI-gestütztes Screening von Schuldnerakten auf mögliche Insolvenzanfechtungsansprüche nach §§ 129-147 InsO. Prüft Zahlungsdaten, Kontoauszüge, OPOS, Verträge, Sicherheiten, Gesellschafterdarlehen und Kommunikation; erzeugt Kandidatenmatrix mit Belegen, Unsicherheiten und Human-Review-Grenzen. Schwerpunkt: § 133-Wertungen, Dreiecksverhältnisse, Bargeschäft und § 135."
---

# KI-Screening Schuldnerakten — mögliche Anfechtungsansprüche

## Aufgabe

Dieser Skill nutzt KI nicht als Ersatz für die anwaltliche oder insolvenzverwalterliche Prüfung, sondern als **beleggebundenes Screening-Werkzeug**. Er soll aus Schuldnerakten mögliche Anfechtungskandidaten erkennen, strukturieren, priorisieren und mit Quellenstellen versehen.

Die richtige Antwort kann in schwierigen Fällen auch lauten: **Der Sachverhalt reicht für eine rechtliche Prüfung durch KI nicht aus.** Das ist kein Fehler, sondern ein verwertbares Ergebnis.

## Grundregel

KI darf:

- Massendaten vorsortieren.
- Zahlungen, Sicherheiten, Verzichtserklärungen, Aufrechnungen und Dreipersonenvorgänge erkennen.
- jede Transaktion einem möglichen Tatbestand zuordnen.
- Belege und Gegenbelege aus der Akte verlinken.
- Unsicherheiten, Lücken und menschliche Prüfentscheidungen markieren.

KI darf nicht:

- Gläubigerbenachteiligungsvorsatz nach § 133 InsO als bewiesen ausgeben, wenn nur Indizien vorliegen.
- Kenntnis des Anfechtungsgegners fingieren.
- aus fehlenden Unterlagen auf Tatsachen schließen.
- komplexe Dreiecksverhältnisse, Cash-Pooling, Treuhand, Konzernverrechnungen oder Globalzessionen ohne Human Review final bewerten.
- Fristen oder Normfassungen aus dem Gedächtnis verwenden.

## Eingaben

Mindestens benötigt:

- Eröffnungsbeschluss, Insolvenzantrag und Datum der Verfahrenseröffnung.
- Kontoauszüge, Zahlungsjournal, OPOS-Listen, Debitoren/Kreditoren und Sachkonten.
- Rechnungen, Verträge, Sicherheitenunterlagen, Ratenzahlungsvereinbarungen.
- Mahnungen, Vollstreckungsschreiben, Rücklastschriften, Stundungen und E-Mail-Verkehr.
- Gesellschafterliste, Darlehensverträge, Bürgschaften, Patronatserklärungen.
- Unterlagen zur Zahlungsunfähigkeit: Liquiditätsstatus, BWA, SuSa, Zahlungsstockungen, nicht bediente fällige Verbindlichkeiten.

## Workflow

### 1. Akteninventar und Quellenanker

Erstelle zuerst ein Quellenregister.

| Quelle | Zeitraum | Datenart | Vollständig? | Lücke |
|---|---|---|---|---|
| Kontoauszug Bank 1 | [...] | Zahlung | ja/nein | [...] |
| OPOS Kreditoren | [...] | Forderungen | ja/nein | [...] |
| E-Mails Mahnungen | [...] | Kenntnisindizien | ja/nein | [...] |

Ohne Quellenanker darf keine Tatsache in die Anfechtungsmatrix übernommen werden.

### 2. Transaktionsnormalisierung

Jede erkannte Bewegung bekommt eine eindeutige ID.

| ID | Datum | Betrag | Zahler | Empfänger | Vorgang | Quelle |
|---|---:|---:|---|---|---|---|
| IA-001 | [...] | [...] EUR | Schuldner | Lieferant | Zahlung Rechnung | Kontoauszug S. [...] |

Bei Sammelzahlungen, Verrechnungen oder Drittzahlungen wird zusätzlich eine Beteiligten-Grafik in Textform erstellt.

### 3. Tatbestandsrouting

| Konstellation | Erstprüfung |
|---|---|
| geschuldete Zahlung an Insolvenzgläubiger | § 130 InsO |
| nicht geschuldete, nicht so geschuldete oder vorzeitige Deckung | § 131 InsO |
| unmittelbar nachteiliger Vertrag ohne Deckungscharakter | § 132 InsO |
| Vorsatzindizien, Kenntnis, lange Rückschau | § 133 InsO |
| Schenkung oder objektiv unentgeltlicher Teil | § 134 InsO |
| Gesellschafterdarlehen, Drittdarlehen mit Gesellschaftersicherheit | § 135 InsO |
| gleichwertiger unmittelbarer Austausch | § 142 InsO als Verteidigung prüfen |
| Rückgewähr, Gegenleistung, Verjährung | §§ 143-147 InsO |

### 4. § 133 InsO nur als Indizienmatrix

Bei § 133 InsO wird kein finales Ergebnis ohne Human Review ausgegeben. Die KI erstellt nur eine Indizienmatrix.

| Indiz | Beleg | Gegenbeleg | Bewertung |
|---|---|---|---|
| erkannte Zahlungsunfähigkeit | [...] | [...] | stark/mittel/schwach |
| Ratenzahlungsbitte | [...] | [...] | stark/mittel/schwach |
| Vollstreckungsdruck | [...] | [...] | stark/mittel/schwach |
| Sanierungsversuch | [...] | [...] | entlastend/offen/belastend |
| Information des Empfängers | [...] | [...] | stark/mittel/schwach |

Wertungssatz: **Die KI benennt Indizien. Die rechtliche Gesamtwürdigung zu Benachteiligungsvorsatz und Kenntnis bleibt menschlicher Prüfpunkt.**

### 5. Dreiecksverhältnisse und komplexe Strukturen

Bei folgenden Mustern wird zwingend auf Human Review geschaltet:

- Zahlung durch Dritte oder an Dritte.
- Factoring, Zentralregulierung, Konzern-Cash-Pool.
- Sicherheitenbestellung für fremde Forderungen.
- Gesellschafternahes Drittdarlehen.
- Treuhandkonten, Anderkonten, Absonderungsrechte.
- Aufrechnung, Verrechnung, Kontokorrent, Globalzession.

Ausgabe: Beteiligtenrollen, Forderungswege, Vermögensabfluss, mögliche Normen, offene Fragen.

### 6. Kandidatenmatrix

| ID | Empfänger | Vorgang | Normkandidat | Betrag | Frist | Belege | Gegenargument | Review |
|---|---|---|---|---:|---|---|---|---|
| IA-001 | [...] | Zahlung | § 130 InsO | [...] EUR | offen/kritisch | [...] | § 142 möglich | Anwalt prüfen |
| IA-002 | [...] | Sicherheit | § 135 InsO | [...] EUR | offen/kritisch | [...] | kein Gesellschafter? | Anwalt prüfen |

## Qualitätsgate

Vor jeder Ausgabe prüfen:

1. Hat jede Tatsache mindestens einen Quellenanker?
2. Sind Antragsdatum, Eröffnungsdatum und Rechtshandlungsdatum getrennt?
3. Ist § 140 InsO als Zeitpunkt der Vornahme mitgedacht?
4. Sind Fristen und Verjährung getrennt?
5. Ist § 142 InsO nicht als Freibrief, sondern als enges Verteidigungsthema behandelt?
6. Ist bei § 133 InsO der Unterschied zwischen Indiz und bewiesener innerer Tatsache sichtbar?
7. Sind Dreiecksverhältnisse als solche markiert?

## Output-Template

**KI-Screening Insolvenzanfechtung**

Aktenstand: [...]

| Kennzahl | Ergebnis |
|---|---|
| geprüfte Transaktionen | [...] |
| rote Kandidaten | [...] |
| gelbe Kandidaten | [...] |
| zwingender Human Review | [...] |
| nicht prüfbar wegen Aktenlücke | [...] |

**Wichtigste Kandidaten**

| Rang | ID | Norm | Betrag | Warum auffällig | Nächster Schritt |
|---:|---|---|---:|---|---|
| 1 | [...] | [...] | [...] EUR | [...] | [...] |

**Nicht leistbar durch KI**

Die folgenden Punkte können ohne menschliche Bewertung nicht abgeschlossen werden:

- [...]

---

Hinweis: Keine Rechtsberatung. Dieses Screening erzeugt Kandidaten und Belegketten, keine belastbare Anspruchsdurchsetzung ohne fachliche Endprüfung.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
