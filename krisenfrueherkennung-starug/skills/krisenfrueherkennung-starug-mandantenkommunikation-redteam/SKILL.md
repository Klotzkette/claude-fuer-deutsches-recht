---
name: krisenfrueherkennung-starug-mandantenkommunikation-redteam
description: "Mandantenkommunikation Redteam: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenkommunikation Redteam

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenkommunikation Redteam** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin krisenfrueherkennung-starug: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin krisenfrueherkennung-starug: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | Insolvenzantragspflicht nach § 15a InsO und Drei-Wochen-Frist: GF prüft ob Insolvenzantrag gestellt werden muss. Normen: § 15a InsO (Antragspflicht), § 15a Abs. 4 InsO (Strafbarkeit), § 18 InsO (drohende ZU als StaRUG-Tor), § 1 StaRUG (Fruehwarnung). Prüfraster: Triggerlogik (ZU oder Überschuldung), Maximalfrist 3 Wochen, Handlungskorridore in der Frist, Verhältnis zu StaRUG. Output Handlungs-Memo mit Optionen (Antrag, StaRUG, außergerichtliche Sanierung), Zeitplan. Abgrenzung: Fortbestehensprognose siehe fortbestehensprognose-zweistufig; StaRUG-Plan siehe restrukturierungsplan-architektur-paragraph-7ff-starug. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **Mandantenkommunikation Redteam**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin krisenfrueherkennung-starug: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin krisenfrueherkennung-starug: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Kommunikation Krisenfrüherkennung § 1 StaRUG — Pflichtinhalte
- **§ 1 Abs. 1 Satz 1 StaRUG (Stand prüfen):** Geschäftsleiter haftungsbeschränkter Gesellschaften müssen Entwicklungen, die den Fortbestand der juristischen Person gefährden können, fortlaufend überwachen.
- **§ 1 Abs. 1 Satz 2 StaRUG:** Bei Erkennen einer bestandsgefährdenden Entwicklung sind geeignete Gegenmaßnahmen zu ergreifen.
- **§ 1 Abs. 1 Satz 3 StaRUG:** Den zur Überwachung berufenen Organen ist unverzüglich Bericht zu erstatten — schriftliche Form empfohlen.
- **Konsequenzen bei Pflichtverletzung:** § 43 GmbHG (Innenhaftung), § 826 BGB (Außenhaftung in Ausnahmefällen), strafrechtlich § 15a Abs. 4, 5 InsO bei verspätetem Antrag.
- **Was an die Mandantin gehört (Pflichtbausteine):** Welche Kennzahlen werden überwacht? Welche Schwellen lösen Alarm aus? Wer berichtet wem in welcher Frequenz? Welche Maßnahmen sind bereits beschlossen?
- **Honorar:** Bei laufender Begleitung empfiehlt sich Mandatsvereinbarung mit Stunden- oder Monatspauschalhonorar — RVG-Tabelle deckt diese Beratung nicht ab.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin krisenfrueherkennung-starug: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin krisenfrueherkennung-starug: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Red-Team Krisenfrüherkennung
- **Wer ist Adressat von § 1 StaRUG?** Geschäftsleiter haftungsbeschränkter Gesellschaften (GmbH, AG, KGaA, GmbH & Co. KG bei nicht natürlicher Komplementärin) — Einzelunternehmer und OHG ohne Kapitalgesellschaftsbeteiligung sind nicht erfasst.
- **Welche Maßstäbe?** "Geeignete Maßnahmen" sind ungeschriebener Sorgfaltsmaßstab — angemessen ist, was eine sorgfältige Geschäftsleitung in der konkreten Lage zur Krisenabwehr ergreifen würde (BGH ständige Rspr. zu § 43 GmbHG).
- **Schwelle zu § 18 InsO/StaRUG-Zugang:** Drohende Zahlungsunfähigkeit (24 Monate, § 18 Abs. 2 InsO) öffnet das Restrukturierungsverfahren nach § 29 StaRUG.
- **Trennung zu § 15a InsO:** § 1 StaRUG ist Pflicht im Vorfeld; § 15a InsO ist Antragspflicht nach Eintritt von Zahlungsunfähigkeit (§ 17) oder Überschuldung (§ 19). Höchstfristen: 3 Wochen / 6 Wochen.
- **Halluzinationsprüfung:** Keine BGH-Az aus Modellwissen; bei Unklarheit zu IDW S 11 oder IDW S 6 Verifikation gegen die Originaltexte (Live-Check).
- **Praxis:** Niemals "in der Krise" ohne § 18-Test sagen — der Eröffnungsgrund ist Tatbestand, nicht Lebensgefühl.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist`

**Fokus:** Insolvenzantragspflicht nach § 15a InsO und Drei-Wochen-Frist: GF prüft ob Insolvenzantrag gestellt werden muss. Normen: § 15a InsO (Antragspflicht), § 15a Abs. 4 InsO (Strafbarkeit), § 18 InsO (drohende ZU als StaRUG-Tor), § 1 StaRUG (Fruehwarnung). Prüfraster: Triggerlogik (ZU oder Überschuldung), Maximalfrist 3 Wochen, Handlungskorridore in der Frist, Verhältnis zu StaRUG. Output Handlungs-Memo mit Optionen (Antrag, StaRUG, außergerichtliche Sanierung), Zeitplan. Abgrenzung: Fortbestehensprognose siehe fortbestehensprognose-zweistufig; StaRUG-Plan siehe restrukturierungsplan-architektur-paragraph-7ff-starug.

# Insolvenzantragspflicht — § 15a InsO und die Drei-Wochen-Frist

§ 15a InsO ist das härteste Instrument im deutschen Insolvenzrecht gegenüber Geschäftsführern. Wer nach Eintritt der Zahlungsunfähigkeit oder Überschuldung nicht innerhalb von drei Wochen Insolvenzantrag stellt, begeht eine Straftat — und haftet persönlich für Schäden, die nach Fristablauf eintreten. Diese Norm ist kein Papiertiger: Staatsanwaltschaften verfolgen sie aktiv, und Insolvenzverwalter nutzen sie systematisch als Regressgrundlage. Das Heft des Handelns verliert, wer diese Frist verstreichen lässt.

---

## Rechtsgrundlagen

- § 15a InsO (Antragspflicht)
- § 15a Abs. 4 InsO (Straftatbestand: Freiheitsstrafe bis zu drei Jahre oder Geldstrafe)
- § 15a Abs. 5 InsO (fahrlässige Variante)
- § 15b InsO (Zahlungsverbote nach Insolvenzreife)
- § 43 GmbHG (Sorgfaltspflicht)
- § 64 GmbHG a.F. / § 15b InsO n.F. (Masseerhaltungspflicht)
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers für Neugläubigerschäden, solange die durch ihn geschaffene Gefährdungslage fortwirkt. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH 5 StR 287/24 vom 27.02.2025** — Faktische Geschäftsführung / Firmenbestattung: auch Hintermänner ohne Außenauftritt können als faktische Geschäftsführer haften. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Versicherung: Wissentlichkeitsausschluss erfordert positive Kenntnis pro Pflichtverletzung; § 15a / § 15b InsO nicht koppelbar.

---

## Pflichten

### 1. Tatbestand des § 15a InsO

Die Antragspflicht wird ausgelöst, wenn:

**Tatbestandsalternative 1 — Zahlungsunfähigkeit § 17 InsO:**
- Fällige Verbindlichkeiten können nicht mehr bezahlt werden
- Zahlungsrückstand übersteigt 10 % der Gesamtverbindlichkeiten (BGH-Wesentlichkeitsschwelle)
- Das Unvermögen ist nicht nur vorübergehend

**Tatbestandsalternative 2 — Überschuldung § 19 InsO:**
- Aktiva < Passiva auf Liquidationsbasis (rechnerische Überschuldung)
- KEINE positive Fortbestehensprognose vorhanden

**Normadressaten:**

| Rechtsform | Antragspflichtige Person |
|---|---|
| GmbH | Geschäftsführer (alle, nicht nur einer) |
| AG | Vorstandsmitglieder (alle) |
| GmbH & Co. KG | GF der Komplementär-GmbH |
| Verein (rechtsfähig) | Vorstand |
| Genossenschaft | Vorstand |
| Faktischer GF | Ebenfalls antragspflichtig (BGH-Rspr.) |

### 2. Die Drei-Wochen-Frist — Inhalt und Berechnung

Drei-Wochen-Frist nach § 15a Abs. 1 S. 1 InsO bei Zahlungsunfähigkeit (§ 17 InsO); Sechs-Wochen-Frist seit 01.01.2021 (SanInsFoG) bei Überschuldung (§ 19 InsO). Beide Fristen sind Höchstfristen, keine "Schonfrist". Konkrete Aktenzeichen der BGH-Linie zur Fristberechnung über offene Quellen verifizieren.

**Berechnung:**
```
Tag 0: Kenntnis des Insolvenzgrundes (Datum + Uhrzeit protokollieren!)
Tag 1: Beginn der Drei-Wochen-Frist
Tag 21: Ablauf der Frist — Antragstellung muss erfolgt sein

Achtung: Drei Wochen = 21 Tage, nicht drei Kalenderwochen mit flexiblem Ende.
```

**Verlängerung der Frist:** Die Drei-Wochen-Frist kann nur dann länger dauern, wenn innerhalb der Frist ernsthafte und aussichtsreiche Sanierungsverhandlungen geführt werden. Dies ist eng auszulegen — Gerichte prüfen ex post sehr genau, ob die Sanierungsbemühungen tatsächlich aussichtsreich waren.

**Maximale Gesamtfrist:** Auch bei laufenden Sanierungsverhandlungen gibt es keine unbegrenzte Verlängerung. § 15a Abs. 1 S. 2 InsO verlangt den Antrag ohne schuldhaftes Zögern, spätestens drei Wochen nach Eintritt der Zahlungsunfähigkeit und spätestens sechs Wochen nach Eintritt der Überschuldung. Zahlungsunfähigkeit ist daher der rote Sofortfall; Überschuldung ist kein Drei-Monats-Fenster.

### 3. Strafrechtliche Sanktion — § 15a Abs. 4 InsO

**Vorsätzliche Verletzung:** Freiheitsstrafe bis zu drei Jahre oder Geldstrafe
**Fahrlässige Verletzung:** Freiheitsstrafe bis zu einem Jahr oder Geldstrafe (§ 15a Abs. 5 InsO)

Strafverfolgung durch Staatsanwaltschaft erfolgt regelmäßig, wenn:
- Der Insolvenzantrag erkennbar verspätet gestellt wurde
- Schadensersatzansprüche anderer Gläubiger bestehen
- Gläubiger Strafanzeige erstattet haben

### 4. § 15b InsO — Das Zahlungsverbot

Parallel zur Antragspflicht gilt das Zahlungsverbot des § 15b InsO: Nach Eintritt der Insolvenzreife dürfen nur noch Zahlungen geleistet werden, die

- im gewöhnlichen Geschäftsgang anfallen und
- mit der Sorgfalt eines ordentlichen Kaufmanns vereinbar sind.

Unzulässige Zahlungen nach Insolvenzreife begründen Schadensersatzansprüche des späteren Insolvenzverwalters gegen den Geschäftsführer persönlich. Die Beweislast liegt beim Geschäftsführer (§ 93 Abs. 2 S. 2 AktG analog für GmbH-GF).

### 5. Der "Quasi-Notgeschäftsführer"

In der Praxis entsteht nach Eintritt der Insolvenzreife und Ausscheiden des regulären GF die Situation, dass kein neuer GF bestellt wird. In diesem Fall:

- Gesellschafter sind subsidiär antragspflichtig (§ 15a Abs. 3 InsO)
- Faktische Geschäftsführer (wer tatsächlich die Geschäfte führt) sind ebenfalls antragspflichtig
- Ein "kommissarischer" GF, der die Geschäfte fortführt ohne formal bestellt zu sein, haftet wie ein regulärer GF

---

## Vorgehen

### Schritt 1: Insolvenzreife-Check — Sofortprüfung

Bei jedem Krisenalarm-Signal sofort prüfen:

- [ ] Können aktuell fällige Verbindlichkeiten bezahlt werden? (§ 17 InsO)
- [ ] Wurde die letzte Lohnzahlung vollständig und rechtzeitig geleistet?
- [ ] Wurden Steuern/Sozialversicherungsbeiträge fristgerecht bezahlt?
- [ ] Gibt es gerichtliche Mahnbescheide oder Vollstreckungsandrohungen?
- [ ] Ist das Eigenkapital aufgezehrt? Gibt es eine positive FBP? (§ 19 InsO)

Wenn ein Punkt kritisch: Sofortiger Anruf beim Restrukturierungs-/Insolvenzrechtsberater.

### Schritt 2: Fristbeginn protokollieren

Das genaue Datum (und die Uhrzeit) der Erkenntnis des Insolvenzgrundes muss protokolliert werden:

```
PROTOKOLL — ERKENNTNIS INSOLVENZREIFE

Gesellschaft: [Firma GmbH]
Datum und Uhrzeit der Erkenntnis: [TT.MM.JJJJ, HH:MM Uhr]
Art des Insolvenzgrundes: [ ] § 17 InsO [ ] § 19 InsO [ ] beide
Grundlage der Erkenntnis:
 [ ] Eigene Analyse der Liquiditätsplanung
 [ ] Beratereinschätzung von [fiktive Kanzlei], [Datum]
 [ ] Ergebnis IDW S 11-Gutachten

Fristablauf (21 Tage): [TT.MM.JJJJ]

Sofortmaßnahmen eingeleitet:
 [ ] Insolvenzrechtsberater beauftragt am [Datum]
 [ ] Sanierungsverhandlungen begonnen am [Datum]
 [ ] Insolvenzantrag beim AG [Ort] gestellt am [Datum]

Unterschrift GF: ___________________
```

### Schritt 3: Erlaubte Zahlungen nach Insolvenzreife

Nach Insolvenzreife nur noch folgende Zahlungen leisten:

- Löhne und Gehälter für laufenden Zeitraum (Masseschutz)
- Zahlungen zur Aufrechterhaltung des Betriebs im normalen Geschäftsgang
- Steuervoranmeldungen (Steuerzahlungen können Masseschuld sein)
- KEINE Ausschüttungen, Gesellschafterdarlehen zurückzahlen, präferenzielle Gläubiger befriedigen

---

## Templates

### Muster: Insolvenzantrag-Checkliste

```
CHECKLISTE — VORBEREITUNG INSOLVENZANTRAG

Gesellschaft: [Firma GmbH]
Zuständiges AG: [Insolvenzgericht — i.d.R. am Sitz der Hauptniederlassung]

DOKUMENTE FÜR DEN ANTRAG:
 [ ] Aktueller Jahresabschluss (letzter testierter)
 [ ] Aktuelle BWA mit Kommentar
 [ ] Liquiditätsplan (kurzfristig, 13 Wochen)
 [ ] Gläubigerliste mit Forderungshöhen
 [ ] Handelsregisterauszug (nicht älter als drei Monate)
 [ ] Gesellschafterliste
 [ ] IDW S 11-Gutachten (sofern vorhanden)

INFORMATIONEN ZUM ANTRAG:
 [ ] Insolvenzgrund benennen (§ 17 / § 18 / § 19 InsO)
 [ ] Antragsberechtigung nachweisen (GF-Bestellungsurkunde)
 [ ] Insolvenzmasse schätzen (Aktiva, verwertbar)
 [ ] Verfahrenskosten vorfinanzieren oder glaubhaft machen

NACH ANTRAGSTELLUNG:
 [ ] Mitarbeiter informieren
 [ ] Banken benachrichtigen
 [ ] Wichtige Vertragspartner informieren
 [ ] Buchhaltung sichern
```

---

## Fallstricke

1. **Fristbeginn falsch berechnet** — die Frist beginnt mit der Kenntnis, nicht mit dem Eintritt des Insolvenzgrundes. Wer "es schon länger wusste", hat möglicherweise die Frist bereits verpasst.

2. **Sanierungsverhandlungen als Fristaufschub** — nur echte, aussichtsreiche Verhandlungen verlängern die Frist. Gespräche ohne konkretes Ergebnis schützen nicht.

3. **Ein GF stellt Antrag, anderer nicht** — alle antragspflichtigen GF müssen den Antrag stellen. Derjenige, der keinen Antrag stellt, haftet gesondert.

4. **Gesellschafterweisung zur Weiterführung** — Weisungen der Gesellschafter, die Antragstellung zu unterlassen, schützen den GF nicht. § 15a InsO ist zwingend.

5. **Zahlungen nach Insolvenzreife** — jede nicht mehr zulässige Zahlung nach Eintritt der Insolvenzreife ist vom Insolvenzverwalter rückforderbar. Kreditkartenzahlungen, Barabhebungen, Überweisungen — alles wird geprüft.

---

## Querverweise

- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Abgrenzung vor Antragspflicht
- → `fortbestehensprognose-zweistufig` — FBP als Voraussetzung für modifizierten Überschuldungsbegriff
- → `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — persönliche Haftungsfolgen
- → `pflichtenkollision-und-shift-of-fiduciary-duties` — Pflichtenwandel bei Insolvenzreife
- → `restrukturierungsplan-architektur-paragraph-7ff-starug` — letzte StaRUG-Chance vor § 15a InsO


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?
