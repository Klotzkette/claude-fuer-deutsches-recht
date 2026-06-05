---
name: klassifikation-cpc-neuheit-patentfamilien
description: "Klassifikation CPC Neuheit Patentfamilien: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klassifikation CPC Neuheit Patentfamilien

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Klassifikation CPC Neuheit Patentfamilien** im Plugin Patentrecherche (FTO, Validity). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klassifikation-cpc-ipc` | CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche muessen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC (Cooperative Patent Classification EPA/USPTO). Prüfraster: Technikgebiet aus Beschreibung extrahieren, Hauptklassen und Nebenklassen, CPC feiner als IPC, Verifikation per WIPO-IPC-Online und Espacenet-Classification-Browser. Output Klassifikations-Empfehlung mit Begründung je Klasse. Abgrenzung: Eigentliche Recherche siehe agentische-datenbank-recherche, stand-der-technik-recherche; FTO siehe freedom-to-operate-recherche. |
| `neuheit-pruefen` | Prüft Neuheit nach § 3 PatG und Art. 54 EPUe. Methodisches Schema: ein Anspruch wird in seine Merkmale zerlegt und Merkmal-fuer-Merkmal gegen genau eine Entgegenhaltung verglichen. Neuheitsschaedlich ist nur die vollständige Vorwegnahme aller Merkmale in einer einzigen Entgegenhaltung (kein Mosaik). Berücksichtigt die EPA-Konzepte unmittelbare und eindeutige Offenbarung implizite Offenbarung und unzulässige Auswahlerfindungen. Erzeugt Merkmalsanalyse-Tabelle pro Entgegenhaltung. Bewertet jedes Merkmal als offenbart nicht offenbart oder implizit offenbart mit Pinpoint. Gibt Gesamtergebnis und Empfehlung an die Patentanwaeltin. Disclaimer keine amtliche Prüfung. |
| `patentfamilien-analyse` | Patentfamilien-Analyse über INPADOC und Espacenet-Family-View. Sammelt zu einem konkreten Treffer alle Familienmitglieder weltweit DE EP US JP CN KR WO und sonstige Aemter mit gleichem Prioritaetstag. Liefert eine Familientabelle pro Familienmitglied mit Veröffentlichungsnummer Anmeldetag Prioritaetstag Status Klassifikation Validierungsstaaten Anmelder Link. Erlaeutert den Unterschied zwischen INPADOC-Familie (gleicher Prioritaetstag) und Domestic Patent Family (gleicher Anmelder und enge technische Verwandtschaft). Markiert wann die Familie in welchem Staat noch geschützt ist und wann ein Mitglied bereits abgelaufen ist. Disclaimer Familiendaten koennen luekenhaft sein nicht alle Aemter melden vollständig. |

## Arbeitsweg

Im Plugin Patentrecherche (FTO, Validity) gilt für **Klassifikation CPC Neuheit Patentfamilien**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klassifikation-cpc-ipc`

**Fokus:** CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche muessen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC (Cooperative Patent Classification EPA/USPTO). Prüfraster: Technikgebiet aus Beschreibung extrahieren, Hauptklassen und Nebenklassen, CPC feiner als IPC, Verifikation per WIPO-IPC-Online und Espacenet-Classification-Browser. Output Klassifikations-Empfehlung mit Begründung je Klasse. Abgrenzung: Eigentliche Recherche siehe agentische-datenbank-recherche, stand-der-technik-recherche; FTO siehe freedom-to-operate-recherche.

# klassifikation-cpc-ipc

## Zweck

Damit die anschließende Datenbankrecherche zielgenau läuft, müssen die richtigen **Klassen** bestimmt werden. Eine schlecht gewählte Klasse erzeugt entweder Trefferchaos oder verfehlt einschlägige Treffer komplett.

## Grundlagen

- **CPC** — Cooperative Patent Classification, gemeinsame Klassifikation von EPA und USPTO. Etwa 250.000 Untergruppen, etwa zehnmal feiner als IPC. Verwendet ab 2013, abgelöst hat sie die alte ECLA und die alte USPC.
- **IPC** — International Patent Classification, WIPO-Klassifikation. Etwa 70.000 Untergruppen. Wird global an Patentschriften angebracht, auch von Ämtern, die keine CPC vergeben.
- Eine Anmeldung trägt typischerweise mehrere CPC- und mehrere IPC-Symbole — eine **Hauptklasse** und mehrere **Nebenklassen**.

## Klassen-Schema (Hauptsektionen)

| Sektion | Inhalt |
| --- | --- |
| A | Täglicher Lebensbedarf (Landwirtschaft, Lebensmittel, Bekleidung, Medizinprodukte, Sport) |
| B | Arbeitsverfahren, Transport (Mechanik, Trennen, Mischen, Formen, Drucken, Transport, Verpacken, Mikro/Nano) |
| C | Chemie, Hüttenwesen (anorganische und organische Chemie, Polymere, Metallurgie, Werkstoffe) |
| D | Textilien, Papier |
| E | Bauwesen (Hochbau, Erdarbeiten, Wasserbau, Bergbau) |
| F | Maschinenbau, Beleuchtung, Heizung, Waffen, Sprengen |
| G | Physik (Messen, Optik, Elektrik-Messung, Informatik G06, Akustik, Erkennung, Atomphysik) |
| H | Elektrotechnik (Schaltkreise, Halbleiter H01L, Energie H02, Nachrichtentechnik H04, Hochfrequenz) |
| Y | CPC-Querschnittsschemata (Y02 Klima/CO2, Y04 IoT/Smart Grid, Y10 Cross-Reference) — **nur CPC, nicht IPC** |

## Ablauf

### 1. Erfindungsmaterial einlesen

- Erfindungsbeschreibung
- Anspruchsentwurf
- Datenblatt
- Skizzen / Zeichnungen
- Memo der Patentanwältin

Wenn nur sehr knappes Material vorhanden ist: an `rueckfragen-mandant` weiterleiten.

### 2. Schlüsselbegriffe extrahieren

Maximal 10 Begriffe, gegliedert in:

- **Was tut die Erfindung** (Verfahren, Funktion, Wirkung)
- **Wie ist sie aufgebaut** (Vorrichtungsmerkmale, Komponenten)
- **Wo wird sie eingesetzt** (Anwendungsfeld)
- **Mit welchen Stoffen / Materialien** (bei chemischen Erfindungen)

### 3. Kandidatenklassen sammeln

Zwei Wege parallel:

**a) Espacenet Classification Browser.** Bei den Schlüsselbegriffen den [Espacenet Classification Search](https://worldwide.espacenet.com/patent/cpc-browser) öffnen und die Begriffe nacheinander eingeben. Trefferklassen mit jeweiliger Definition notieren.

**b) Top-Down über Sektion / Klasse.** Aus dem Technikgebiet (Kaltstart-Interview) die wahrscheinliche Sektion wählen, von dort über die [WIPO IPC Online Publication](https://www.wipo.int/classifications/ipc/ipcpub) bis zur Untergruppe navigieren.

### 4. Auswahl Haupt- und Nebenklassen

Vorschlag formulieren:

```
Hauptklasse CPC: H02J 3/00 — Schaltungsanordnungen oder Systeme für die Versorgung oder Verteilung elektrischer Energie
 Entsprechende IPC: H02J 3/00
Nebenklassen CPC:
 - H02J 3/14 — Anpassung der Leistung an den Verbrauch (Lastmanagement)
 - G06Q 50/06 — Energie-, Wasser- oder Gasversorgung
 - Y02E 60/00 — Technologies für die Reduktion von Treibhausgasen (CPC-only)
```

Pro Klasse zwei Sätze Begründung, **warum** sie passt — verankert in den Schlüsselbegriffen.

### 5. Verifikation

- Auf den Espacenet-Klassen-Definitionsseiten die **Anmerkungen** lesen (Hinweise "nicht hier, sondern dort").
- Eine Stichprobe (3–5 bekannte Patente der Mandantin) klassifizieren lassen und prüfen, ob die Klassen aus Schritt 4 dort tatsächlich angebracht sind.

### 6. Übergabe

Die endgültige Klassenliste übergibt das Skill in maschinenlesbarer Form an `agentische-datenbank-recherche`:

```yaml
klassen:
 cpc_haupt: H02J 3/00
 cpc_neben: [H02J 3/14, G06Q 50/06, Y02E 60/00]
 ipc_haupt: H02J 3/00
 ipc_neben: [H02J 3/14, G06Q 50/06]
```

## Hinweise

- **CPC ist feiner.** Wenn EPA-/USPTO-/CN-/KR-Patente recherchiert werden, immer CPC. Wenn ältere Patente vor 2013 oder Patente aus Ländern ohne CPC: zusätzlich IPC.
- **Y-Sektion.** Y02 ist ein CPC-Querschnittsschema für Klimatechnologien — relevant für Energietechnik, Bauwesen, Verkehr. Y04 IoT, Y10 Cross-Reference. **Nicht in IPC** vorhanden.
- **Mehrere Klassen sind die Regel.** Eine moderne Anmeldung hat oft 5–15 CPC-Symbole. Recherche-Klassenset darf großzügig sein; verengt wird über Schlüsselbegriffe und Volltext.
- **Symbol-Syntax.** Sektion (Buchstabe) + Klasse (zweistellig) + Unterklasse (Buchstabe) + Hauptgruppe (1–3 Ziffern) + `/` + Untergruppe (2–6 Ziffern). Beispiel `H04L 9/00` heißt H/H04/H04L/H04L 9/00.

## Disclaimer

> **Hinweis zur Klassifikation.** Die hier vorgeschlagenen CPC- und IPC-Klassen sind eine KI-gestützte **Vorklassifikation** zur Recherche-Steuerung und keine amtliche Klassifikation. Die endgültige Klasseneinordnung einer eigenen Anmeldung erfolgt durch das Patentamt. Für die Recherchesteuerung sind ergänzend Schlüsselbegriffe und Volltextsuchen einzusetzen — keine Klassenrecherche ohne Volltext.

## Triage-Fragen vor Klassifikations-Recherche

Bevor die CPC/IPC-Klassen festgelegt werden, klaere:
1. Welches technische Gebiet ist primaer betroffen (Hauptklasse) und welche Querschnittsklassen koennen relevant sein?
2. Sind Y-Klassen (CPC-spezifisch, Klimatechnologie, IoT) zutreffend?
3. Soll IPC zusaetzlich zu CPC eingesetzt werden (notwendig fuer Laender ohne CPC und aeltere Patente vor 2013)?
4. Wurde die Klassifikation anhand des naechstliegenden Anspruchsmerkmals (nicht des Funktionsergebnisses) bestimmt?

## Aktuelle Rechtsprechung

> **EPA, Technische Beschwerdekammer, T 0190/99 (Klassifikationsirrtum):** Ein Fehler in der Klassifikation einer Anmeldung beeintraichtigt die Neuheit und erfinderische Taetigkeit der Anmeldung nicht, solange der beanspruchte Gegenstand ordnungsgemaess offenbart ist; die Klassifikation ist eine verwaltungstechnische Einordnung, kein Schutzrechtsmerkmal.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **DPMA, Merkblatt Klassifikation 2023:** CPC-Klassen werden von Espacenet und Google Patents korrekt indexiert; fuer die agentische Recherche ist die Kombination von Klassen- und Schluessel-wort-Suche unverzichtbar, da Klassifikationsfehler der Aemter zu Luecken fuehren koennen.

## 2. `neuheit-pruefen`

**Fokus:** Prüft Neuheit nach § 3 PatG und Art. 54 EPUe. Methodisches Schema: ein Anspruch wird in seine Merkmale zerlegt und Merkmal-fuer-Merkmal gegen genau eine Entgegenhaltung verglichen. Neuheitsschaedlich ist nur die vollständige Vorwegnahme aller Merkmale in einer einzigen Entgegenhaltung (kein Mosaik). Berücksichtigt die EPA-Konzepte unmittelbare und eindeutige Offenbarung implizite Offenbarung und unzulässige Auswahlerfindungen. Erzeugt Merkmalsanalyse-Tabelle pro Entgegenhaltung. Bewertet jedes Merkmal als offenbart nicht offenbart oder implizit offenbart mit Pinpoint. Gibt Gesamtergebnis und Empfehlung an die Patentanwaeltin. Disclaimer keine amtliche Prüfung.

# neuheit-prüfen

## Zweck

Prüft, ob ein konkreter Anspruch (Mandantin oder Drittpatent) gegenüber konkreten Entgegenhaltungen **neu** ist. Genaues Werkzeug, das auf den Vorrecherche-Treffern aufsetzt.

## Rechtsrahmen

- **§ 3 PatG.** Eine Erfindung gilt als neu, wenn sie nicht zum Stand der Technik gehört.
- **Art. 54 EPÜ.** Wortgleich für das EPA.
- **EPA-Beschwerdekammern-Doktrin:**
 - **Unmittelbare und eindeutige Offenbarung** — eine Entgegenhaltung nimmt einen Anspruch nur dann vorweg, wenn alle Merkmale **direkt und unmittelbar erkennbar** sind (G 2/88, T 305/87).
 - **Implizite Offenbarung** — ein Merkmal ist implizit offenbart, wenn der Fachmann es zwingend mitliest (G 2/10 zu Disclaimern, T 6/80).
 - **Auswahlerfindungen** — Auswahl eines Sub-Bereichs aus einem offenbarten Bereich kann neu sein, wenn (1) der Sub-Bereich eng ist, (2) abseits des präferierten Bereichs der Entgegenhaltung liegt, (3) eine eigene technische Lehre vermittelt (T 198/84, T 279/89).
- **Kein Mosaik** — anders als bei der erfinderischen Tätigkeit darf bei der Neuheitsprüfung **nicht** kombiniert werden. Ein Anspruch wird gegen **genau eine** Entgegenhaltung geprüft. Mehrere Entgegenhaltungen lassen sich nur kombinieren, wenn die eine ausdrücklich auf die andere verweist und der Fachmann beide unmittelbar zusammenliest (T 153/85).

## Ablauf

### Schritt 1: Anspruch zerlegen

Aufbau einer Merkmalsanalyse-Tabelle. Der Hauptanspruch wird in **Merkmale** zerlegt — jeder grammatikalisch und technisch eigenständige Bestandteil ist ein Merkmal. Beispiel:

```
Anspruch 1 — Vorrichtung zum Lastmanagement in einem Energieversorgungsnetz:
M1: ein Energieversorgungsnetz mit mindestens einer Quelle und mindestens einem Verbraucher,
M2: ein Steuergerät, das mit der Quelle und dem Verbraucher verbunden ist,
M3: wobei das Steuergerät einen Speicher für historische Lastdaten umfasst,
M4: wobei das Steuergerät eingerichtet ist, anhand eines Prognosemodells einen Soll-Lastpfad zu bestimmen,
M5: wobei das Steuergerät eingerichtet ist, bei Abweichung des Ist-Lastpfads vom Soll-Lastpfad einen Eingriff in den Verbraucher auszuloesen,
M6: dadurch gekennzeichnet, dass das Prognosemodell ein neuronales Netzwerk mit mindestens drei Schichten umfasst.
```

### Schritt 2: Pro Entgegenhaltung eine Tabelle

Pro Entgegenhaltung Spalte "offenbart / nicht offenbart / implizit offenbart" mit Pinpoint:

| Merkmal | EP 3 456 789 A1 | Pinpoint |
| --- | --- | --- |
| M1 | offenbart | Abs. [0001], Fig. 1 (Bezugszeichen 1, 2, 3) |
| M2 | offenbart | Abs. [0012], Fig. 1 (Bezugszeichen 4) |
| M3 | offenbart | Abs. [0014], Bezugszeichen 5 |
| M4 | offenbart | Abs. [0016]: "Prognosemodell" |
| M5 | offenbart | Abs. [0020]–[0022] |
| M6 | **nicht offenbart** | — Modell ist linear, kein neuronales Netz |

### Schritt 3: Bewertung pro Entgegenhaltung

- **Alle Merkmale offenbart** → Anspruch ist gegenüber dieser Entgegenhaltung **nicht neu**, neuheitsschädlich.
- **Mindestens ein Merkmal nicht offenbart** → Anspruch ist gegenüber dieser Entgegenhaltung **neu**. Die Entgegenhaltung kann aber für die erfinderische Tätigkeit (§ 4 PatG) relevant bleiben.
- **Implizite Offenbarung** kennzeichnen — kritisch bewerten (Beweislast hoch).
- **Auswahlerfindung** — wenn der Anspruch einen Sub-Bereich aus einem in der Entgegenhaltung offenbarten Bereich auswählt, prüfen, ob die T-198/84-Kriterien greifen.

### Schritt 4: Gesamt-Bewertung

Tabelle aller Entgegenhaltungen mit Bewertungsspalte:

| Entgegenhaltung | Neuheitsschaedlich? | Bemerkung |
| --- | --- | --- |
| EP 3 456 789 A1 | nein | M6 nicht offenbart, lineares Modell statt neuronalem Netz |
| US 2020/0123456 A1 | ja | alle Merkmale Anspruch 1 + Abs. [0034] |
| WO 2019/123456 A1 | nein | M4 und M6 nicht offenbart |

### Schritt 5: Folgen

- **Mindestens eine neuheitsschädliche Entgegenhaltung** → Empfehlung an Patentanwältin: Anspruch umformulieren (Aufnahme weiterer Merkmale aus der Beschreibung, Beschränkung auf Sub-Konfigurationen), oder Anmeldung in dieser Form nicht aufrechterhalten.
- **Keine neuheitsschädliche Entgegenhaltung** → weiter zu `erfinderische-taetigkeit-pruefen`. Neuheit allein reicht nicht.

## Hinweise

- **Sprache des Anspruchs** spielt eine Rolle. "Umfassend" ist offen (weitere Bauteile möglich), "bestehend aus" ist abgeschlossen. Bei der Merkmalsanalyse exakt am Wortlaut bleiben.
- **Funktionale Merkmale** (z. B. "eingerichtet, X zu tun") sind in der Auslegung delikat. EPA-Praxis: Eine Vorrichtung, die geeignet ist, X zu tun, nimmt das funktionale Merkmal vorweg (T 219/89, T 1090/12) — die Mandantin sollte daher nicht zu weit funktional formulieren.
- **Zahlenbereiche** (M6 "mindestens drei Schichten") — eine Entgegenhaltung mit "zwei Schichten" nimmt M6 nicht vorweg. Eine Entgegenhaltung mit "beliebige Anzahl von Schichten" nimmt M6 vorweg.
- **Kombinationen aus zwei Entgegenhaltungen** sind in der Neuheitsprüfung verboten (T 153/85). Wenn die Mandantin nur dann neuheitsschädlich getroffen wird, wenn man Entgegenhaltung A mit Entgegenhaltung B mosaikartig zusammenfügt → Neuheit ist gegeben, Frage verschiebt sich zur erfinderischen Tätigkeit.

## Disclaimer

> **Hinweis zur Prüfung.** Diese Neuheitsprüfung ist eine KI-gestützte Vorprüfung und keine amtliche Prüfung durch DPMA oder EPA. Die Bewertung als "neu" oder "nicht neu" ist eine Einschätzung anhand der Recherche-Treffer; die amtliche Prüfung kann zu anderen Ergebnissen kommen, weil weitere oder andere Entgegenhaltungen gefunden werden oder die Auslegung des Anspruchs anders ausfällt.

## Triage-Fragen vor Neuheitspruefung

Bevor die Neuheitspruefung beginnt, klaere:
1. Ist der Prioritaetszeitpunkt klar (Anmeldetag oder Prioritaetsdatum aus frueherer Anmeldung)?
2. Sind geheime aeltere Anmeldungen (§ 3 II PatG / Art. 54 III EPU) beruecksichtigt?
3. Wurden alle relevanten CPC/IPC-Klassen fuer die Recherche eingesetzt?
4. Handelt es sich um einen Hauptanspruch oder einen abhaengigen Anspruch (abhaengige Ansprueche koennen weniger Merkmale enthalten = leichter angreifbar)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Technische Beschwerdekammer, T 153/85:** Bei der Neuheitspruefung ist jede Entgegenhaltung einzeln zu betrachten; eine neuheitsschaedliche Wirkung kann nur aus einer einzigen Schrift hergeleitet werden, nicht durch Kombination mehrerer Dokumente.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `patentfamilien-analyse`

**Fokus:** Patentfamilien-Analyse über INPADOC und Espacenet-Family-View. Sammelt zu einem konkreten Treffer alle Familienmitglieder weltweit DE EP US JP CN KR WO und sonstige Aemter mit gleichem Prioritaetstag. Liefert eine Familientabelle pro Familienmitglied mit Veröffentlichungsnummer Anmeldetag Prioritaetstag Status Klassifikation Validierungsstaaten Anmelder Link. Erlaeutert den Unterschied zwischen INPADOC-Familie (gleicher Prioritaetstag) und Domestic Patent Family (gleicher Anmelder und enge technische Verwandtschaft). Markiert wann die Familie in welchem Staat noch geschützt ist und wann ein Mitglied bereits abgelaufen ist. Disclaimer Familiendaten koennen luekenhaft sein nicht alle Aemter melden vollständig.

# patentfamilien-analyse

## Zweck

Ein einzelnes Patentdokument steht selten allein — es ist Teil einer **Patentfamilie**, die aus der gleichen Erstanmeldung hervorgegangen ist. Für die FTO-Recherche, die Stand-der-Technik-Recherche und die Einspruchsstrategie ist es entscheidend, die ganze Familie zu kennen.

## Konzepte

### INPADOC-Familie

Definition über den **Prioritätstag**. Alle Anmeldungen weltweit, die direkt oder indirekt auf dieselbe Erstanmeldung priorisieren (Pariser Verbandsübereinkunft, Art. 4 PVÜ — 12 Monate Prioritätsfrist).

- Eine Erstanmeldung in DE am 15.03.2018.
- Innerhalb 12 Monaten Nachanmeldungen in EP, US, JP, CN, KR mit Priorität DE 15.03.2018.
- 18 Monate nach Prioritätstag (15.09.2019): Veröffentlichung der Anmeldungen.
- Alle gehören zur **INPADOC patent family** mit Stamm-Prioritätstag 15.03.2018.

INPADOC wird vom EPA gepflegt und ist über Espacenet und EPO Open Data zugänglich.

### Domestic Patent Family

Definition über **gleichen Anmelder + technische Verwandtschaft**. Continuation-in-Part, Teilanmeldung (§ 39 PatG / Art. 76 EPÜ), Zusatzanmeldung. Die Domestic Family ist enger als die INPADOC-Familie und kann anderen Anmeldetag haben.

### Simple Family

Definition über **gleichen Satz aller Prioritätsdaten**. Engere Definition als INPADOC, in Espacenet als "Simple family" gekennzeichnet.

## Ablauf

### Schritt 1: Treffer zur Recherche-Bewertung übernehmen

Aus den Recherche-Treffern (Output von `agentische-datenbank-recherche`) den Treffer auswählen, dessen Familie analysiert werden soll. Typisch: jeder X-Treffer und jeder kritische Y-Treffer aus `stand-der-technik-recherche` und jeder Rot-/Gelb-Treffer aus `freedom-to-operate-recherche`.

### Schritt 2: Espacenet Family View öffnen

In Espacenet zum Treffer navigieren, "Family list" oder "INPADOC patent family" auswählen.

URL-Schema:
```
https://worldwide.espacenet.com/patent/search/family/<family-id>/publication/<publication-no>?q=<publication-no>
```

Die Family-ID ist eine zentrale Kennzahl — sie identifiziert die INPADOC-Familie eindeutig.

### Schritt 3: Familientabelle erstellen

Pro Familienmitglied:

| Veröff.-Nr. | Anmelder | Anmeldetag | Prio | Status | Klasse | Validierung | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DE 10 2018 005 432 A1 | Siemens AG | 15.03.2018 | DE 15.03.2018 | zurückgenommen | H02J 3/14 | — | DPMAregister-Link |
| EP 3 456 789 A1 | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt | H02J 3/14 | DE FR GB | EPO-Register-Link |
| EP 3 456 789 B1 | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt 12.09.2021 | H02J 3/14 | DE FR GB IT NL | EPO-Register-Link |
| US 10,876,543 B2 | Siemens AG | 15.03.2019 | DE 15.03.2018 | erteilt 05.10.2020 | H02J 3/14 | US | USPTO-Link |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| CN 110123456 A | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt CN | H02J 3/14 | CN | Espacenet-CN-Link |
| JP 6789012 B2 | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt JP | H02J 3/14 | JP | Espacenet-JP-Link |

### Schritt 4: Rechtsstand markieren

Pro Familienmitglied: ist es noch in Kraft? Wann läuft die Schutzdauer ab (= Anmeldetag + 20 Jahre)? Sind die Jahresgebühren bezahlt? — über `rechtsstand-pruefen`.

### Schritt 5: Auswertung

- **In welchen Staaten** ist die Erfindung in Kraft? Daraus ergeben sich die Territorien, in denen die Familie für FTO relevant ist.
- **In welchen Staaten** ist die Familie nie eingetreten? Dort bestehen für die Mandantin keine Verbietungsrechte.
- **In welchen Staaten** ist die Familie abgelaufen / zurückgenommen / nicht erteilt? Dort frei.
- **Continuation- / Teilanmeldungen** — sind weitere Anmeldungen aus derselben Stammanmeldung anhängig? Diese können bei Erteilung **künftige** Verbietungsrechte begründen.

### Schritt 6: Output an aufrufendes Skill

Familientabelle als strukturiertes YAML/JSON an `freedom-to-operate-recherche` oder `recherchebericht-erstellen`.

## Hinweise

- **Datenlücken.** Nicht alle Ämter melden vollständig an INPADOC. Bei JP-, CN-, KR-Patenten kann die Familie unvollständig erfasst sein. Bei kritischen Mandaten: amtliche Direktrecherche im Zielland.
- **Späte Nachanmeldungen** außerhalb der 12-Monats-Prioritätsfrist sind keine echte Familie, sondern eigenständige Anmeldungen mit eigenem Stand der Technik.
- **EP-Patente mit Einheitlichem Patent (UP).** Seit Juni 2023 gibt es das Einheitliche Patent. Erfasst alle Teilnehmer-Staaten als ein einziges Schutzrecht; in der Familienliste oft als "European patent with unitary effect" gekennzeichnet.
- **PCT-Anmeldungen** (WO …) sind keine eigentlichen Patente, sondern Anmeldewege. Erst durch nationale Phasen entstehen die einzelnen Patente.
- **Anmelderwechsel.** Familienmitglieder können verschiedene Anmelder haben (Anmelderwechsel, Konzernverschiebung). Bei FTO immer auf den **aktuellen** eingetragenen Inhaber im jeweiligen Register prüfen.

## Disclaimer

> **Hinweis zur Familienanalyse.** Diese Patentfamilien-Analyse beruht auf INPADOC-Daten und ist eine KI-gestützte Vorrecherche. Datenlücken sind insbesondere bei JP- CN- KR- und einzelnen weiteren Aemtern möglich. Continuation- und Teilanmeldungen können anhängig sein, ohne dass sie schon veröffentlicht sind. Die Familie kann durch Anmelderwechsel verschoben sein. Die finale Familie- und Rechtsstandsbewertung muss durch direkte Recherche in den nationalen Registern abgesichert werden.

## Triage-Fragen vor Patentfamilien-Analyse

Bevor die Familienanalyse begonnen wird, klaere:
1. Ist das Ausgangsdokument (Stammanmeldung oder Hauptpatent) korrekt identifiziert?
2. Sind Continuation-, Divisional- und CIP-Anmeldungen (US) oder Teilanmeldungen (EP) beruecksichtigt?
3. Wurden JP, CN, KR-Familienmitglieder direkt in den nationalen Registern nachgeprueft (INPADOC-Luecken)?
4. Gibt es ein Einheitliches Patent (UP) unter dem EP-Patent — wenn ja, welche Staaten sind abgedeckt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Erweiterte Beschwerdekammer, G 2/10 (Teilanmeldung):** Eine EP-Teilanmeldung kann nur Gegenstande umfassen, die in der Stammanmeldung zum Zeitpunkt der Einreichung der Teilanmeldung offenbart waren; neue Merkmale koennen nicht nachtraeglich in eine Teilanmeldung eingefuehrt werden.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
