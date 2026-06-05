---
name: inso-gesellschafterdarlehen-grundtatbestand
description: "Inso Gesellschafterdarlehen Grundtatbestand: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inso Gesellschafterdarlehen Grundtatbestand

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Inso Gesellschafterdarlehen Grundtatbestand** im Plugin Bereicherungs- und Anfechtungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inso-gesellschafterdarlehen-135` | Gesellschafterdarlehen und gleichgestellte Forderungen nach § 135 InsO prüfen: Sicherheiten zehn Jahre, Befriedigung ein Jahr, Drittdarlehen mit Gesellschaftersicherheit, Gebrauchsüberlassung, Sanierungsprivileg und Kleinbeteiligtenausnahme. Output: Anspruchsmatrix mit Rollenprüfung, Fristen, Rückgewähr und Verteidigung. |
| `inso-grundtatbestand-129-glaeubigerbenachteiligung` | Grundvoraussetzungen der Insolvenzanfechtung nach § 129 InsO klären: Rechtshandlung, objektive Gläubigerbenachteiligung, Kausalität. Normen: § 129 InsO. Prüfraster: Rechtshandlungsbegriff, unmittelbare vs. mittelbare Benachteiligung, Kausalitätsprüfung. Output: Checkliste Grundtatbestand als Einstieg für §§ 130 ff. InsO. Abgrenzung: nicht AnfG (ohne Insolvenzeröffnung). |
| `inso-inkongruente-deckung-131` | Inkongruente Deckungsanfechtung nach § 131 InsO prüfen: Sicherung oder Befriedigung, die der Gläubiger nicht, nicht in der Art oder nicht zu der Zeit beanspruchen konnte. Fristen letzter Monat, zweiter oder dritter Monat; Zahlungsunfähigkeit oder Kenntnis der Gläubigerbenachteiligung. Output: Normmatrix mit Abgrenzung zu § 130, § 133 und § 142. |
| `inso-ki-anfechtungsansprueche-schuldnerakten` | KI-gestütztes Screening von Schuldnerakten auf mögliche Insolvenzanfechtungsansprüche nach §§ 129-147 InsO. Prüft Zahlungsdaten, Kontoauszüge, OPOS, Verträge, Sicherheiten, Gesellschafterdarlehen und Kommunikation; erzeugt Kandidatenmatrix mit Belegen, Unsicherheiten und Human-Review-Grenzen. Schwerpunkt: § 133-Wertungen, Dreiecksverhältnisse, Bargeschäft und § 135. |

## Arbeitsweg

Im Plugin Bereicherungs- und Anfechtungsrecht gilt für **Inso Gesellschafterdarlehen Grundtatbestand**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `inso-gesellschafterdarlehen-135`

**Fokus:** Gesellschafterdarlehen und gleichgestellte Forderungen nach § 135 InsO prüfen: Sicherheiten zehn Jahre, Befriedigung ein Jahr, Drittdarlehen mit Gesellschaftersicherheit, Gebrauchsüberlassung, Sanierungsprivileg und Kleinbeteiligtenausnahme. Output: Anspruchsmatrix mit Rollenprüfung, Fristen, Rückgewähr und Verteidigung.

# Gesellschafterdarlehen — § 135 InsO

## Triage — kläre vor der Prüfung

1. Wer hat das Darlehen gewährt: formeller Gesellschafter, nahestehende Person, Konzernunternehmen oder außenstehender Dritter?
2. Geht es um **Sicherheit** für eine Gesellschafterdarlehensforderung oder um **Befriedigung**?
3. Liegt die Sicherheit innerhalb von zehn Jahren oder die Befriedigung innerhalb eines Jahres vor dem Eröffnungsantrag?
4. Hat ein Gesellschafter für ein Drittdarlehen Sicherheit bestellt oder als Bürge gehaftet?
5. Greifen § 39 Abs. 4 oder Abs. 5 InsO entsprechend, insbesondere Sanierungsprivileg oder Kleinbeteiligtenausnahme?
6. Wurde ein Gegenstand zur Nutzung überlassen, der für die Fortführung des Unternehmens wesentlich ist?

## Zentrale Normen

§ 135 InsO — § 39 Abs. 1 Nr. 5 InsO — § 39 Abs. 4 und 5 InsO — § 129 InsO — § 138 InsO — § 143 Abs. 3 InsO — § 146 InsO.

## Gesetzliche Struktur

| Norm | Prüfungspunkt | Frist |
|---|---|---|
| § 135 Abs. 1 Nr. 1 InsO | Sicherung für Gesellschafterdarlehen oder gleichgestellte Forderung | zehn Jahre vor Antrag oder nach Antrag |
| § 135 Abs. 1 Nr. 2 InsO | Befriedigung eines Gesellschafterdarlehens oder gleichgestellter Forderung | ein Jahr vor Antrag oder nach Antrag |
| § 135 Abs. 2 InsO | Befriedigung eines Dritten, wenn Gesellschafter Sicherheit bestellt hat oder als Bürge haftet | ein Jahr |
| § 135 Abs. 3 InsO | Nutzungsüberlassung eines betriebswesentlichen Gegenstands | Aussonderung für höchstens ein Jahr gesperrt; Ausgleich für Gebrauch oder Ausübung |
| § 135 Abs. 4 InsO | § 39 Abs. 4 und 5 InsO gelten entsprechend | Ausnahmeprüfung |

## Rollenprüfung

§ 135 InsO verlangt nicht nur einen Zahlungsvorgang, sondern eine gesellschaftsrechtlich oder wirtschaftlich relevante Finanzierungsrolle.

| Rolle | Relevanz |
|---|---|
| formeller Gesellschafter | regelmäßig § 135 prüfen |
| Treugeber, beherrschende Konzernperson, wirtschaftlich gleichgestellter Dritter | Gleichstellung nur mit belastbaren Rechten und Einfluss prüfen |
| externer Kreditgeber ohne Einfluss | grundsätzlich kein § 135 Abs. 1; § 133 oder § 130 gesondert prüfen |
| Gesellschafter als Bürge oder Sicherungsgeber | § 135 Abs. 2 und § 143 Abs. 3 prüfen |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sanierungs- und Kleinbeteiligtenprüfung

Prüfe § 39 Abs. 4 und 5 InsO entsprechend:

- Sanierungsprivileg: Erwerb der Beteiligung zum Zweck der Sanierung; ernsthafte Sanierungsperspektive und dokumentierter Sanierungsbezug.
- Kleinbeteiligtenausnahme: keine Geschäftsführung und Beteiligung innerhalb der gesetzlichen Schwelle.

Wenn diese Punkte streitig sind, wird der Vorgang als Human Review markiert.

## Prüfschema

1. Forderung aus Darlehen oder wirtschaftlich gleichgestellter Rechtshandlung?
2. Gesellschafter oder gleichgestellte Rolle?
3. Sicherheit oder Befriedigung?
4. Frist: zehn Jahre bei Sicherheit, ein Jahr bei Befriedigung?
5. Drittdarlehen mit Gesellschaftersicherheit oder Bürgschaft?
6. Ausnahme nach § 39 Abs. 4 oder 5 InsO?
7. Bei Nutzungsüberlassung: betriebswesentlicher Gegenstand, Sperrzeit und angemessener Ausgleich?
8. Rechtsfolge: Rückgewähr nach § 143 InsO, ggf. Erstattung durch Gesellschafter nach § 143 Abs. 3 InsO?

## Output-Template

**Prüfung § 135 InsO**

| Merkmal | Ergebnis | Beleg |
|---|---|---|
| Darlehen oder gleichgestellte Forderung | ja/nein | [...] |
| Gesellschafterrolle oder Gleichstellung | ja/nein/offen | [...] |
| Sicherheit oder Befriedigung | Sicherheit/Befriedigung | [...] |
| Frist | zehn Jahre/ein Jahr/offen | [...] |
| Drittdarlehen mit Gesellschaftersicherheit | ja/nein | [...] |
| Nutzungsüberlassung und Ausgleich | ja/nein/offen | [...] |
| § 39 Abs. 4 oder 5 InsO | greift/greift nicht/offen | [...] |

**Ergebnis:** § 135 InsO [naheliegend / nicht naheliegend / Human Review erforderlich].

---

Hinweis: Keine Rechtsberatung. § 135 InsO ist besonders anfällig für Rollen- und Konzernfehler; wirtschaftliche Gleichstellung nie ohne belastbare Tatsachen annehmen.

## 2. `inso-grundtatbestand-129-glaeubigerbenachteiligung`

**Fokus:** Grundvoraussetzungen der Insolvenzanfechtung nach § 129 InsO klären: Rechtshandlung, objektive Gläubigerbenachteiligung, Kausalität. Normen: § 129 InsO. Prüfraster: Rechtshandlungsbegriff, unmittelbare vs. mittelbare Benachteiligung, Kausalitätsprüfung. Output: Checkliste Grundtatbestand als Einstieg für §§ 130 ff. InsO. Abgrenzung: nicht AnfG (ohne Insolvenzeröffnung).

# Grundtatbestand Insolvenzanfechtung — § 129 InsO

## Triage — kläre vor der Prüfung

1. Ist ein Insolvenzverfahren eröffnet, oder handelt es sich um eine Einzelgläubigeranfechtung (→ AnfG)?
2. Wann wurde die angefochtene Rechtshandlung vorgenommen — ist die Anfechtungsfrist noch offen?
3. Liegt eine Rechtshandlung (rechtlich wirksames Handeln/Unterlassen) oder ein bloßer Tatsachenakt vor?
4. Sind die Befriedigungsaussichten der Insolvenzgläubiger durch die Handlung tatsächlich verschlechtert worden?
5. Handelt es sich um unmittelbare oder mittelbare Benachteiligung?
6. Sind alle Tatsachen aus der Akte belegt, oder handelt es sich um KI-Inferenz?

## Zentrale Normen

§ 129 InsO (Grundtatbestand) — § 130 InsO (kongruente Deckung) — § 131 InsO (inkongruente Deckung) — § 132 InsO (unmittelbar nachteilige Rechtshandlung) — § 133 InsO (Vorsatzanfechtung) — § 134 InsO (unentgeltliche Leistung) — § 142 InsO (Bargeschäftsprivileg) — § 143 InsO (Rechtsfolge Rückgewähr) — § 27 InsO (Verfahrenseröffnung)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

§ 129 InsO ist die Generalklausel der Insolvenzanfechtung. Sie bildet die Voraussetzungen, die jeder besondere Anfechtungstatbestand (§§ 130–135 InsO) zusätzlich erfüllen muss.

## Tatbestandsmerkmale § 129 Abs. 1 InsO

### 1. Rechtshandlung

**Definition:** Jedes Handeln oder Unterlassen, das eine rechtliche Wirkung auslöst und das Vermögen des Schuldners verändert. Dazu gehören:
- Kaufverträge, Abtretungen, Sicherungsübereignungen.
- Zahlungen auf bestehende Schulden.
- Vollstreckungsmaßnahmen (wenn der Schuldner diese ermöglicht).
- Unterlassen der Geltendmachung einer Forderung (in engen Grenzen).

**Nicht:** bloße Tatsachenakte ohne rechtliche Bindung.

### 2. Vor Eröffnung des Insolvenzverfahrens

Die Rechtshandlung muss vor Eröffnung des Insolvenzverfahrens vorgenommen worden sein (§ 27 InsO).

### 3. Objektive Gläubigerbenachteiligung

**Definition:** Tatsächliche Verschlechterung der Befriedigungsaussichten. Maßstab: hypothetischer Vergleich.

**Unmittelbare Benachteiligung:** Durch die Rechtshandlung selbst, ohne Zwischenschritte.

**Mittelbare Benachteiligung:** Durch das Zusammenspiel mit weiteren Umständen; Kausalzusammenhang muss feststehen.

### 4. Kausalität

Die Rechtshandlung muss kausal für die Benachteiligung sein: Wären die Gläubiger ohne die Handlung besser gestellt?

## KI-Auswertung von Schuldnerakten

Bei KI-gestützter Aktenauswertung darf § 129 InsO nur als Kandidat markiert werden, wenn Rechtshandlung, Zeitpunkt, Vermögensabfluss und Gläubigerbenachteiligung jeweils mit einer Quelle belegt sind. Nicht belegte Plausibilitäten werden als Lücke ausgegeben, nicht als Tatsache.

## Anfechtungsberechtigte

Regelmäßig macht der Insolvenzverwalter die Anfechtung geltend. In Eigenverwaltung ist § 280 InsO zu beachten; dort kann der Sachwalter Rechtshandlungen nach §§ 129 bis 147 InsO anfechten. Bei vorläufiger Verwaltung ist die konkrete gerichtliche Anordnung zu prüfen.

## Prüfschema

1. Insolvenzverfahren eröffnet + Anfechtungsbefugnis gegeben?
2. Liegt eine Rechtshandlung vor (kein bloßer Tatsachenakt)?
3. Handlung vor Verfahrenseröffnung?
4. Objektive Gläubigerbenachteiligung nachweisbar?
5. Kausalzusammenhang zwischen Handlung und Benachteiligung?

## Output-Template

**Prüfung § 129 InsO — Grundtatbestand Insolvenzanfechtung**

Sachverhalt (kurz): [...]

| Merkmal | Ergebnis |
|---|---|
| Insolvenzverfahren eröffnet | ja / nein |
| Anfechtungsberechtigter | Insolvenzverwalter / Sachwalter |
| Rechtshandlung identifiziert | ja: [...] |
| Zeitpunkt: vor Verfahrenseröffnung | ja / nein |
| Objektive Gläubigerbenachteiligung | ja (unmittelbar / mittelbar) / nein |
| Kausalzusammenhang | ja / nein |

**Weiter:** Besonderer Tatbestand (§§ 130–135 InsO): [...]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

## 3. `inso-inkongruente-deckung-131`

**Fokus:** Inkongruente Deckungsanfechtung nach § 131 InsO prüfen: Sicherung oder Befriedigung, die der Gläubiger nicht, nicht in der Art oder nicht zu der Zeit beanspruchen konnte. Fristen letzter Monat, zweiter oder dritter Monat; Zahlungsunfähigkeit oder Kenntnis der Gläubigerbenachteiligung. Output: Normmatrix mit Abgrenzung zu § 130, § 133 und § 142.

# Inkongruente Deckung — § 131 InsO

## Triage — kläre vor der Prüfung

1. Hatte der Gläubiger einen fälligen, einredefreien Anspruch auf genau diese Leistung?
2. War die Leistung in Art, Zeitpunkt oder Sicherungsform abweichend vom Geschuldeten?
3. Lag die Handlung im letzten Monat vor dem Antrag, nach dem Antrag oder im zweiten/dritten Monat vor dem Antrag?
4. War der Schuldner im zweiten/dritten Monat zahlungsunfähig?
5. Kannte der Gläubiger im zweiten/dritten Monat die Gläubigerbenachteiligung oder zwingende Umstände?
6. Ist die Inkongruenz nur Indiz für § 133 InsO oder trägt bereits § 131 InsO?

## Zentrale Normen

§ 131 InsO — § 129 InsO — § 130 InsO — § 133 InsO — § 140 InsO — § 142 InsO — § 143 InsO.

## Gesetzliche Struktur

| Norm | Zeitraum | Voraussetzung |
|---|---|---|
| § 131 Abs. 1 Nr. 1 InsO | letzter Monat vor Antrag oder nach Antrag | Inkongruenz genügt |
| § 131 Abs. 1 Nr. 2 InsO | zweiter oder dritter Monat vor Antrag | Schuldner zahlungsunfähig |
| § 131 Abs. 1 Nr. 3 InsO | zweiter oder dritter Monat vor Antrag | Gläubiger kannte Gläubigerbenachteiligung |
| § 131 Abs. 2 InsO | Kenntnisersatz und Nahestehende | zwingende Umstände oder Vermutung |

## Begriff der Inkongruenz

Inkongruent ist eine Sicherung oder Befriedigung, wenn der Gläubiger sie:

- überhaupt nicht beanspruchen konnte,
- nicht in dieser Art beanspruchen konnte,
- nicht zu diesem Zeitpunkt beanspruchen konnte.

Typische Beispiele:

- nachträgliche Sicherheit ohne vorherige Sicherungsabrede.
- vorzeitige Tilgung noch nicht fälliger Forderungen.
- Zahlung unter Vollstreckungsdruck in Konstellationen, in denen die Deckung nicht freiwillig geschuldet war.
- Sicherung für Altverbindlichkeiten kurz vor Antrag.

## Verhältnis zu § 133 InsO

Inkongruenz kann ein starkes Indiz für § 133 InsO sein. Sie ersetzt aber nicht automatisch Benachteiligungsvorsatz und Kenntnis. Für § 133 ist eine eigene Gesamtwürdigung nötig.

## Prüfschema

1. Rechtshandlung und Zeitpunkt nach § 140 InsO.
2. Deckungscharakter: Sicherung oder Befriedigung eines Insolvenzgläubigers.
3. Inkongruenz nach Art, Zeit oder Ob.
4. Fristgruppe § 131 Abs. 1 Nr. 1, Nr. 2 oder Nr. 3.
5. Zusatzvoraussetzungen bei Nr. 2 oder Nr. 3.
6. Bargeschäft und § 133 gesondert markieren.

## Output-Template

**Prüfung § 131 InsO — Inkongruente Deckung**

| Merkmal | Ergebnis | Beleg |
|---|---|---|
| Sicherung/Befriedigung | [...] | [...] |
| Inkongruenz | Art/Zeit/Ob | [...] |
| Zeitraum | Nr. 1/Nr. 2/Nr. 3 | [...] |
| Zahlungsunfähigkeit | ja/nein/offen | [...] |
| Kenntnis Benachteiligung | ja/nein/offen | [...] |
| § 133-Indizwirkung | stark/mittel/schwach | [...] |

**Ergebnis:** § 131 InsO [naheliegend / nicht naheliegend / offen].

---

Hinweis: Keine Rechtsberatung. Bei § 131 InsO ist die exakte Kongruenzprüfung oft entscheidender als die Krisenkenntnis.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `inso-ki-anfechtungsansprueche-schuldnerakten`

**Fokus:** KI-gestütztes Screening von Schuldnerakten auf mögliche Insolvenzanfechtungsansprüche nach §§ 129-147 InsO. Prüft Zahlungsdaten, Kontoauszüge, OPOS, Verträge, Sicherheiten, Gesellschafterdarlehen und Kommunikation; erzeugt Kandidatenmatrix mit Belegen, Unsicherheiten und Human-Review-Grenzen. Schwerpunkt: § 133-Wertungen, Dreiecksverhältnisse, Bargeschäft und § 135.

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
