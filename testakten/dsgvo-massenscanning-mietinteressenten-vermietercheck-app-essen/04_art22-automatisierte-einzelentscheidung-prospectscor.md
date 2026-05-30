# 04 — Art. 22 DSGVO: Automatisierte Einzelentscheidung durch ProspectScore Pro

**Aktenzeichen:** DSB-NW-44/26
**Bearbeiter:** RA Dr. Cornelius Specht, RA Lars Drosselberg
**Datum:** 17. Januar 2026
**Betreff:** Rechtmaessigkeit automatisierter Einzelentscheidungen und Profiling

---

## 1. Regelungsinhalt Art. 22 DSGVO

Art. 22 Abs. 1 DSGVO gewaehrt betroffenen Personen das Recht, nicht einer ausschliesslich auf einer automatisierten Verarbeitung — einschliesslich Profiling — beruhenden Entscheidung unterworfen zu werden, die ihr gegenueber rechtliche Wirkung entfaltet oder sie in aehnlicher Weise erheblich beeintraechtigt.

Art. 22 Abs. 2 DSGVO regelt Ausnahmen: Die automatisierte Entscheidung ist zulaessig, wenn sie (a) fuer den Abschluss oder die Erfuellung eines Vertrags zwischen der betroffenen Person und dem Verantwortlichen erforderlich ist, (b) aufgrund von Rechtsvorschriften der Union oder der Mitgliedstaaten zulaessig ist oder (c) mit ausdruecklicher Einwilligung der betroffenen Person erfolgt.

Bei besonderen Kategorien personenbezogener Daten (Art. 9 DSGVO) ist Art. 22 Abs. 4 DSGVO zu beachten.

---

## 2. Pruefung: Liegt eine automatisierte Einzelentscheidung vor?

### 2.1 Tatbestandsmerkmal „ausschliesslich automatisiert"

Der EDSA hat in seinen Leitlinien 01/2022 zu automatisierten Einzelentscheidungen (Art. 22 DSGVO) klargestellt, dass eine Entscheidung dann als „ausschliesslich automatisiert" gilt, wenn kein menschlicher Eingriff mit substanziellem Einfluss auf das Ergebnis stattfindet. Ein bloss formales Review (Mensch bestaetigt maschinell vorgeschlagenes Ergebnis ohne eigene Pruefung) genuegt nicht.

**Sachverhalt VCS:**
- ProspectScore Pro generiert einen Risiko-Score (0–100)
- Privatvermieter erhalten den Score und eine abgeleitete Empfehlung (GRUEN / GELB / ROT)
- Laut Aussage von 127 Vermietern (Klaeger im VDuG-Verfahren) haben diese ausschliesslich auf Basis der Ampelfarbe entschieden
- Interne Nutzungsstatistiken belegen: 94% aller Mietabsagen korrelieren mit ROT-Einstufung
- Kein Prozess zur menschlichen Ueberpruefung des Scores implementiert

**Ergebnis:** Die Entscheidung ueber die Vermietung basiert faktisch ausschliesslich auf dem automatisierten Score. Das Tatbestandsmerkmal ist erfullt.

### 2.2 Tatbestandsmerkmal „erhebliche Beeintraechtigung"

Die Verweigerung einer Wohnungsanmietung aufgrund des ROT-Scores stellt eine erhebliche Beeintraechtigung im Sinne des Art. 22 Abs. 1 DSGVO dar. Der Europaeische Datenschutzausschuss (EDSA, Leitlinien 01/2022, Rn. 15) nennt als Beispiel ausdruecklich den Ausschluss vom Zugang zu Wohnraum.

**Ergebnis:** Erhebliche Beeintraechtigung liegt vor.

### 2.3 Zwischenergebnis

Der Tatbestand des Art. 22 Abs. 1 DSGVO ist erfullt. Die Verarbeitung ist grundsaetzlich verboten, soweit keine Ausnahme nach Art. 22 Abs. 2 DSGVO greift.

---

## 3. Pruefung der Ausnahmetatbestaende Art. 22 Abs. 2 DSGVO

### 3.1 Art. 22 Abs. 2 lit. a — Vertragserfuellung

Wie bereits in Akte 03 (Art. 6 lit. b) festgestellt: Zwischen VCS und den Mietinteressenten besteht kein Vertrag. **Ergebnis: Nicht einschlaegig.**

### 3.2 Art. 22 Abs. 2 lit. b — Gesetzliche Grundlage

Eine spezialgesetzliche Grundlage, die automatisiertes Profiling fuer Mietbonitaetszwecke erlaubt, existiert im deutschen Recht nicht. § 34 BDSG betrifft Auskunftspflichten, nicht Erlaubnisse fuer automatisiertes Scoring. **Ergebnis: Nicht einschlaegig.**

### 3.3 Art. 22 Abs. 2 lit. c — Einwilligung

Wie in Akte 03 (3.1) festgestellt: Die erteilten Einwilligungen sind wegen Koppelung und mangelnder Informiertheit unwirksam. Zudem war die ausdrueckliche Einwilligung in automatisierte Einzelentscheidungen (Art. 22 Abs. 2 lit. c DSGVO i.V.m. ErwGr. 71) gesondert erforderlich — dies erfolgte nicht. **Ergebnis: Nicht einschlaegig.**

---

## 4. Schutzpflichten bei zulaessiger automatisierter Entscheidung (Art. 22 Abs. 3 DSGVO)

Auch wenn — hypothetisch — eine Ausnahme greifen wuerde, haette VCS folgende Garantien gemaess Art. 22 Abs. 3 DSGVO implementieren muessen:

| Garantie | Status bei VCS |
|----------|----------------|
| Recht auf menschliche Ueberpruefung | Nicht implementiert |
| Recht auf Darlegung des eigenen Standpunkts | Kein Beschwerdemechanismus vorhanden |
| Recht auf Anfechtung der Entscheidung | Keine Einspruchsmoeglichkeit |
| Transparente Information (Art. 13 Abs. 2 lit. f DSGVO) | Profiling in Datenschutzerklaerung nicht explizit |

---

## 5. Profiling und besondere Datenkategorien

### 5.1 Familienstatus als Diskriminierungsmerkmal

Der Familienstatus (mit/ohne Kinder) zaehlt nicht zu den besonderen Kategorien nach Art. 9 DSGVO. Jedoch kann das Profiling auf Basis des Familienstatus eine mittelbare Diskriminierung nach dem Allgemeinen Gleichbehandlungsgesetz (AGG) § 19 Abs. 1 Nr. 1 darstellen: Familien mit Kindern koennen systematisch schlechter bewertet werden.

### 5.2 Gesundheitliche Indikatoren im Score

Laut Penetrationstest-Bericht (s. Akte 07) verarbeitete ProspectScore Pro in einer frueheren Modellversion (v2.1 bis v2.4) Daten aus Krankenversicherungsstatusdaten, die im Rahmen der Schufa-Abfrage mitgeliefert wurden. Soweit Gesundheitsdaten (Art. 9 Abs. 1 DSGVO) in den Score eingeflossen sind, gilt Art. 22 Abs. 4 DSGVO: Die ausdrueckliche Einwilligung gemaess Art. 9 Abs. 2 lit. a DSGVO oder ein Rechtfertigungsgrund nach Art. 9 Abs. 2 DSGVO waere zusaetzlich erforderlich. Beides lag nicht vor.

---

## 6. Haftungsfolgen

### 6.1 Ordnungswidrigkeitenrecht

Ein Verstoss gegen Art. 22 DSGVO ist gemaess Art. 83 Abs. 4 DSGVO mit einem Bussgeld bis 10.000.000 EUR oder 2% des weltweiten Jahresumsatzes bedroht. In Kombination mit dem Verstoss gegen Art. 6 DSGVO (Art. 83 Abs. 5 lit. a, bis 20 Mio. EUR) koennen gemaess Art. 83 Abs. 3 DSGVO Geldbussen kumuliert werden, wobei der Hoechstbetrag nicht ueberschritten werden darf.

**Anwendbarer Hoechstbetrag:** 20.000.000 EUR (Art. 83 Abs. 5 DSGVO: hoehere Sanktion).

### 6.2 Zivilrechtliche Haftung

Betroffene, die nachweislich aufgrund eines fehlerhaften ROT-Scores eine Wohnung nicht erhalten haben, koennen gemaess Art. 82 DSGVO Schadensersatz verlangen. Der immaterielle Schaden liegt nach BGH VI ZR 10/24 bereits im Kontrollverlust ueber eigene Daten (s. Akte 11).

---

## 7. Handlungsempfehlungen

1. **Sofortige Abschaltung** des ProspectScore-Pro-Moduls bis zur Erlangung konformer Rechtsgrundlagen
2. **Implementierung Human-in-the-Loop** (HITL) — obligatorische menschliche Ueberpruefung vor jeder Entscheidungsweitergabe an Vermieter
3. **Aktualisierung der Datenschutzerklaerung** mit expliziter Information ueber Profiling (Art. 13 Abs. 2 lit. f, Art. 14 Abs. 2 lit. g DSGVO)
4. **Einspruchsmechanismus** fuer betroffene Mietinteressenten (Art. 22 Abs. 3 DSGVO)
5. **DSFA** fuer das KI-Profiling-Modul (Art. 35 DSGVO, s. Akte 05)

---

## Quellen

- DSGVO Art. 9, 13, 14, 22 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- EDSA-Leitlinien 01/2022 zu automatisierten Einzelentscheidungen — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-012022-data-subject-rights-automated-decision_de)
- BDSG § 34 — [dejure.org/gesetze/BDSG](https://dejure.org/gesetze/BDSG)
- AGG § 19 — [dejure.org/gesetze/AGG](https://dejure.org/gesetze/AGG)
- BGH VI ZR 10/24 — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- OLG Koeln, Urt. v. 14.07.2022 — 20 U 168/21 — [openjur.de](https://openjur.de)
