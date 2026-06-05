---
name: wipo-stand-technik-ueberwachung-konkurrenten
description: "Wipo Stand Technik Ueberwachung Konkurrenten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wipo Stand Technik Ueberwachung Konkurrenten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Wipo Stand Technik Ueberwachung Konkurrenten** im Plugin Patentrecherche (FTO, Validity). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-wipo-compliance-dokumentation-und-akte` | Wipo: Compliance-Dokumentation und Aktenvermerk im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `stand-der-technik-recherche` | Recherche Stand der Technik vor eigener Patentanmeldung. Identifiziert anhand des Erfindungsmaterials und der ermittelten CPC-IPC-Klassen die wichtigsten Veröffentlichungen die der Anmeldetag-Reife der Mandantenerfindung im Wege stehen koennten. Patent- und Nichtpatentliteratur (NPL) Aufsaetze Konferenzproceedings Dissertationen Datenblaetter Produktinformationen. Berücksichtigt § 3 Abs. 1 PatG Art. 54 Abs. 2 EPUe (Stand der Technik weltweit jede Sprache) und § 3 Abs. 2 PatG Art. 54 Abs. 3 EPUe (aeltere Anmeldungen nur Neuheitsschaedlich). Liefert Trefferdossiers mit Pinpoint auf Anspruch oder Absatz Bewertung als A X Y P E im Stil der EPA-Recherchezeichen. Disclaimer Vorrecherche keine amtliche Recherche. |
| `ueberwachung-konkurrenten` | Laufende Überwachung neuer Patentanmeldungen von Konkurrenten der Mandantin. Definiert Watch-Profile pro Mandant mit Anmelder-Namen (inklusive Konzern-Toechter und ehemaliger Schreibweisen), CPC-IPC-Klassen, Schlagwoerter, Territorien. Laeuft als woechentlicher oder monatlicher Job in Espacenet Smart Search Google Patents oder bei Bezahl-Tools wie PatBase Alert. Liefert Delta-Liste neuer Treffer seit letzter Iteration mit Bewertung relevant oder nicht relevant. Erinnert an Einspruchsfrist Art. 99 EPUe neun Monate ab Erteilungs-Veröffentlichung. Disclaimer Vollständigkeit nicht garantiert insbesondere bei Konzern-Konstruktionen und Tochterfirmen ohne klare Namens-Bindung. |

## Arbeitsweg

Im Plugin Patentrecherche (FTO, Validity) gilt für **Wipo Stand Technik Ueberwachung Konkurrenten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-wipo-compliance-dokumentation-und-akte`

**Fokus:** Wipo: Compliance-Dokumentation und Aktenvermerk im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Wipo: Compliance-Dokumentation und Aktenvermerk

## Spezialwissen: Wipo: Compliance-Dokumentation und Aktenvermerk
- **Spezialgegenstand:** Wipo: Compliance-Dokumentation und Aktenvermerk / wipo compliance dokumentation und akte. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO/WIPO/USPTO/DPMA sind Patentämter, INPADOC/CPC/IPC/Espacenet/DEPATISnet Recherchedatenbanken, FTO eine Arbeitsmethode — keine Rechtsquellen. Tragende Normen je nach Frage: PatG §§ 1–5 (Schutzfähigkeit, Neuheit), § 4 (erfinderische Tätigkeit), §§ 9, 10 (Schutzwirkung), §§ 34, 35, 37 (Anmeldung, Prioritäten), §§ 81 ff. (Nichtigkeit); EPÜ Art. 52–57 (Patentierbarkeit), Art. 54 (Neuheit), Art. 56 (erfinderische Tätigkeit), Art. 69 (Schutzbereich), Art. 87 ff. (Priorität); PCT Art. 1 ff.; UPCA. Quellen über DPMAregister, EPO Register, USPTO PatFT, WIPO Patentscope und WIPO Lex live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Wipo** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `stand-der-technik-recherche`

**Fokus:** Recherche Stand der Technik vor eigener Patentanmeldung. Identifiziert anhand des Erfindungsmaterials und der ermittelten CPC-IPC-Klassen die wichtigsten Veröffentlichungen die der Anmeldetag-Reife der Mandantenerfindung im Wege stehen koennten. Patent- und Nichtpatentliteratur (NPL) Aufsaetze Konferenzproceedings Dissertationen Datenblaetter Produktinformationen. Berücksichtigt § 3 Abs. 1 PatG Art. 54 Abs. 2 EPUe (Stand der Technik weltweit jede Sprache) und § 3 Abs. 2 PatG Art. 54 Abs. 3 EPUe (aeltere Anmeldungen nur Neuheitsschaedlich). Liefert Trefferdossiers mit Pinpoint auf Anspruch oder Absatz Bewertung als A X Y P E im Stil der EPA-Recherchezeichen. Disclaimer Vorrecherche keine amtliche Recherche.

# stand-der-technik-recherche

## Zweck

Vor einer eigenen Patentanmeldung der Mandantin (oder zur Beratung der Mandantin "lohnt sich die Anmeldung?") wird der Stand der Technik recherchiert. Dieses Skill nutzt die Treffer aus `agentische-datenbank-recherche` und ordnet sie methodisch ein.

## Rechtsrahmen

- **§ 3 Abs. 1 PatG / Art. 54 Abs. 2 EPÜ.** Stand der Technik ist alles, was vor dem Anmeldetag (oder Prioritätstag) der Öffentlichkeit zugänglich gemacht worden ist — schriftlich, mündlich, durch Benutzung oder in sonstiger Weise. **Weltweit. In jeder Sprache.**
- **§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ.** Ältere nationale / EP-Anmeldungen mit früherem Anmelde-/Prioritätstag, aber später veröffentlicht, gelten **nur für die Neuheit** als Stand der Technik, **nicht für die erfinderische Tätigkeit**. Wichtig bei der Bewertung.
- **§ 3 Abs. 5 PatG / Art. 55 EPÜ.** Sechs-Monats-Frist für unschädliche Offenbarungen wegen offensichtlichen Missbrauchs (§ 3 Abs. 5 PatG) oder anlässlich amtlich anerkannter Ausstellungen — eng auszulegen.

## Material

1. **Aus `agentische-datenbank-recherche`** — die strukturierte Treffertabelle aus Patentdatenbanken.
2. **NPL-Recherche** ergänzend:
 - **Google Scholar** (`https://scholar.google.com`) — Aufsätze, Dissertationen, Konferenz-Proceedings.
 - **Crossref / Lens.org** (`https://www.lens.org`) — DOI-basierte Recherche; Lens kombiniert Patente und NPL.
 - **arXiv** (`https://arxiv.org`) — bei Informatik, Mathematik, Physik wichtig.
 - **PubMed** (`https://pubmed.ncbi.nlm.nih.gov`) — Life Sciences / Biotech.
 - **IEEE Xplore**, **ACM Digital Library**, **SpringerLink**, **ScienceDirect** — wenn die Kanzlei Zugänge hat.
3. **Öffentliche Vorbenutzungen** — Produkt-Datenblätter, Konferenzvorträge, Messeauftritte, frühere Patente derselben Mandantin (Selbstbeschwerde). **Internet Archive Wayback Machine** (`https://web.archive.org`) ist hilfreich, um Vorveröffentlichungstage zu sichern.

## Ablauf

### Schritt 1: Anmeldetag der Mandantin festlegen

Wenn die Anmeldung noch nicht eingereicht ist: voraussichtlicher Anmeldetag (heute oder geplant). **Alles, was vor diesem Tag veröffentlicht ist, ist relevant.** Maßgeblich ist die Veröffentlichung — das Datum der Veröffentlichung, nicht das Datum der Anmeldung der entgegenstehenden Veröffentlichung.

Achtung: § 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ — auch ältere, noch nicht veröffentlichte Anmeldungen können einschlägig sein, **nur für die Neuheit**.

### Schritt 2: Recherchezeichen vergeben

EPA-übliche Recherchezeichen, hier zur internen Sortierung übernommen:

- **X** — besonders relevant, **alleine** neuheitsschädlich (wenn alle Merkmale des Hauptanspruchs vorweggenommen sind)
- **Y** — besonders relevant, **in Kombination mit anderen** für erfinderische Tätigkeit schädlich
- **A** — allgemeiner Stand der Technik, Hintergrund
- **P** — Zwischenliteratur, **veröffentlicht zwischen Prioritätsdatum und Anmeldetag** der Mandantin — nur dann relevant, wenn Priorität nicht wirksam ist
- **E** — ältere Anmeldung mit **früherem** Prioritätstag, später veröffentlicht (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ)
- **L** — wird in Rechercheberichten zitiert, wenn sie die Glaubhaftigkeit des Patents in Frage stellt (selten)
- **T** — theoretische Grundlage / Stand der Technik nach Anmeldetag, wird nur zitiert, wenn die Erfindung damit begründet wird

### Schritt 3: Pinpoint pro Treffer

Pro Treffer eine kurze Dossierseite:

```
Treffer: EP 3 456 789 A1
 Anmelder: Siemens AG
 Anmeldetag: 15.03.2019 Prio: 14.03.2018
 Klassifikation: CPC H02J 3/14
 Recherchezeichen: X
 Relevanter Pinpoint:
 Anspruch 1, Merkmale a)-d) decken sich mit Anspruch 1 der Mandantenerfindung;
 Absatz [0023]-[0027] (Bezugszeichen 12, 14) beschreibt baugleiches Verfahren.
 Bewertung: Hauptanspruch der Mandantenerfindung ist gegen diesen Treffer nicht neuheitsfähig.
 Empfehlung: Anspruchsformulierung anpassen oder Erfindung in Richtung verbleibender Merkmale eingrenzen.
 Link: https://worldwide.espacenet.com/patent/search/family/.../publication/EP3456789A1
```

### Schritt 4: NPL-Treffer parallel dokumentieren

Aufsätze / Datenblätter / Wayback-Snapshot werden im gleichen Schema dokumentiert, mit DOI, Veröffentlichungsdatum, Pinpoint (Seite / Abschnitt).

### Schritt 5: Synthese

- **Anzahl X-Treffer** (= Erfindung nicht neu im Sinne des § 3 PatG)
- **Anzahl Y-Treffer** (= Erfindung nicht erfinderisch im Sinne des § 4 PatG)
- **Anzahl A-Treffer** (= reine Hintergrund-Dokumente)
- **Anzahl P/E-Treffer** (= Prioritäts-/Art. 54(3)-Treffer, gesondert behandeln)
- **Anzahl NPL-Treffer**

Empfehlung an die Patentanwältin:

- Erfindung in der jetzigen Formulierung anmeldungsfähig
- Anmeldung mit eingegrenztem Anspruch sinnvoll (Vorschlag: …)
- Anmeldung nicht sinnvoll, Erfindung wahrscheinlich nicht patentfähig
- Anmeldung in anderem Schutzbereich (Gebrauchsmuster nach GebrMG, das mit anderem Stand der Technik arbeitet) eventuell sinnvoll

## Hinweise

- **Volltextsuche in allen Sprachen** ist nicht möglich. Klar kommunizieren.
- **Geheime ältere Anmeldungen** (Art. 54(3) EPÜ-Anmeldungen, die noch nicht publiziert sind) sind beim Recherche-Tag **nicht** erfassbar. Erst nach Ablauf der 18-Monats-Geheimhaltungsfrist.
- **Selbst-Beschwerde:** Frühere Anmeldungen der Mandantin selbst können neuheitsschädlich sein — § 3 PatG kennt keine "eigene" Ausnahme. **Mandant ausdrücklich fragen**, ob es frühere Anmeldungen oder Veröffentlichungen gibt.
- **Vorträge / Messen** der Mandantin in den letzten 18 Monaten erfragen — nicht selten erfolgt dort eine offenkundige Vorbenutzung.

## Disclaimer

> **Hinweis zur Recherche.** Diese Stand-der-Technik-Recherche ist eine KI-gestützte Vorrecherche und keine amtliche Recherche. Geheime ältere Anmeldungen (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ) sind erst nach Ablauf der 18-Monats-Frist erfassbar. Nicht-deutsche, nicht-englische und nicht-französische Volltexte werden nicht vollständig durchsucht. Die Bewertung als X/Y/A/P/E ist eine vorläufige Einschätzung — die amtliche Recherche durch DPMA oder EPA kann zu anderen Ergebnissen kommen.

## Triage-Fragen vor Stand-der-Technik-Recherche

Bevor die Recherche begonnen wird, klaere:
1. Was ist der Prioritaetszeitpunkt — nach diesem Datum relevante Dokumente sind nicht massgeblich (§ 3 I PatG)?
2. Gibt es bekannte Vorveröffentlichungen durch den Mandanten selbst (Messevortrag, Dissertation, Produktkatalog)?
3. Sind Nicht-Patent-Literatur (NPL) — Aufsaetze, Normen, Konferenz-Proceedings — fuer das Technikgebiet besonders relevant?
4. Welcher Fachmann ist massgeblich (IPC/CPC-basierte Einordnung des Technikgebiets)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `ueberwachung-konkurrenten`

**Fokus:** Laufende Überwachung neuer Patentanmeldungen von Konkurrenten der Mandantin. Definiert Watch-Profile pro Mandant mit Anmelder-Namen (inklusive Konzern-Toechter und ehemaliger Schreibweisen), CPC-IPC-Klassen, Schlagwoerter, Territorien. Laeuft als woechentlicher oder monatlicher Job in Espacenet Smart Search Google Patents oder bei Bezahl-Tools wie PatBase Alert. Liefert Delta-Liste neuer Treffer seit letzter Iteration mit Bewertung relevant oder nicht relevant. Erinnert an Einspruchsfrist Art. 99 EPUe neun Monate ab Erteilungs-Veröffentlichung. Disclaimer Vollständigkeit nicht garantiert insbesondere bei Konzern-Konstruktionen und Tochterfirmen ohne klare Namens-Bindung.

# überwachung-konkurrenten

## Zweck

Für viele Mandanten — insbesondere Mittelstands- und Konzernkundinnen — ist es wichtig, **neue Anmeldungen** von Konkurrenten frühzeitig zu erkennen. Anwendungsfälle:

- **Einspruch** rechtzeitig einlegen (Art. 99 EPÜ — neun Monate ab Erteilungs-Veröffentlichung).
- **FTO-Risiken** vor Markteintritt erkennen.
- **Technologie-Strategie** der Konkurrenz beobachten.
- **Lizenzverhandlungen** vorbereiten.

## Watch-Profil

Pro Mandant ein Watch-Profil. Felder:

```yaml
mandant: Beispiel GmbH
profil_name: Watch_Beispiel_2026
anmelder:
 - "Siemens AG"
 - "Siemens Aktiengesellschaft" # alte Schreibweise
 - "Siemens Energy AG" # ehemalige Tochter, ggf. relevant
 - "Siemens Mobility GmbH"
 - "Siemens Healthineers AG"
klassen_cpc:
 - H02J 3/14
 - H02J 3/00
 - Y02E 60/00
schlagworte_und:
 - "lastmanagement"
 - "demand response"
schlagworte_oder:
 - "smart grid"
 - "intelligentes Netz"
territorien: [DE, EP, US, JP, CN, KR, WO]
zeitfenster: ab Anmeldetag 01.01.2024
publikationsstatus: [Anmeldung, Erteilung]
intervall: woechentlich
naechste_iteration: 27.05.2026
```

## Ablauf

### Initial-Lauf

1. Watch-Profil mit der Mandantin durchgehen — Konkurrenten benennen, Konzern-Töchter dazu, ehemalige Namen und Schreibvarianten ergänzen.
2. Klassen über `klassifikation-cpc-ipc` festlegen.
3. Schlagwörter aus dem Mandanten-Technikfokus.
4. Territorien aus den Märkten der Mandantin.
5. Erste Vollrecherche der letzten 24 Monate als Baseline — Treffer dokumentieren.
6. Intervall festlegen (wöchentlich / monatlich / vierteljährlich).

### Iteration

Pro Iteration (z. B. wöchentlich):

1. Espacenet Smart Search mit Anmelder + Klassen + Schlagwörter, Datumsfilter "neu seit letzter Iteration".
2. Google Patents Alert (wenn registriert) — Alternative: direkter Aufruf mit Filtern `assignee=`, `cpc=`, `after=`.
3. WIPO PATENTSCOPE für PCT-Anmeldungen.
4. USPTO PPUBS für US-Anmeldungen (mit `.AN.`-Feld für Assignee).
5. Delta-Liste bilden — nur **neue** Treffer seit letzter Iteration.

### Bewertung pro Treffer

Pro Treffer:

- **Relevant** (rot): Trifft Mandanten-Produkt direkt — Verletzungsrisiko, Einspruchschance.
- **Beobachtung** (gelb): Konkurrent ist in benachbartem Gebiet aktiv — Trendindikator.
- **Hintergrund** (grün): Nicht relevant, dokumentiert.

### Einspruchsfrist-Tracker

Bei Treffern mit Status "erteilt" Frist berechnen:

- **EP-Patent:** Art. 99 EPÜ — neun Monate ab Veröffentlichung der Erteilung.
- **DE-Patent:** § 59 PatG — drei Monate ab Veröffentlichung der Erteilung.

Frist im Output mit Stichtag dokumentieren.

### Quartalsbericht

Aggregierter Bericht alle drei Monate mit:

- Anzahl neuer Treffer je Konkurrent
- Schwerpunkt-Klassen
- Auffällige Anmeldetrends
- Aktuelle Einspruchsfristen
- Empfehlungen (Einspruch / FTO-Recherche / Beobachtung)

## Hinweise

- **Konzern-Töchter.** Konkurrenten melden oft über Tochterfirmen an. Vor jedem Lauf prüfen, ob neue Töchter entstanden sind, die ergänzt werden sollten.
- **Strohmann-Anmeldungen.** Manche Konzerne melden über Anwaltskanzleien oder Trustees an, um die Verbindung zu verschleiern. Hier hilft nur Recherche über Klassen + Schlagwörter, nicht über Anmeldername.
- **Bezahl-Alerts.** PatBase Alert, Orbit, Patsnap und IPlytics bieten leistungsfähigere Alerts — vor allem für große Mandanten lohnt sich die Kombination mit dem frei zugänglichen Watch.
- **Datenverzögerung.** Veröffentlichung erfolgt 18 Monate nach Prioritätstag. Konkurrenz-Anmeldungen werden also erst 1,5 Jahre nach dem Anmeldetag sichtbar.
- **Nicht-Patent-Literatur.** Ergänzend Google Scholar Alerts und Konferenz-Listings (IEEE, ACM) — Konkurrenten reden oft schon auf Konferenzen, bevor die Anmeldung publiziert ist.

## Output

- **Delta-Tabelle** mit Spalten: Datum, Veröff.-Nr., Anmelder, Anmeldetag, Status, Klassen, Titel, Relevanz, Einspruchsfrist (wenn anwendbar), Link.
- **Empfehlung pro Treffer:** weiter beobachten / FTO-Recherche / Einspruch vorbereiten / Lizenzdialog.

## Disclaimer

> **Hinweis zur Überwachung.** Diese laufende Überwachung ist eine KI-gestützte Vorrecherche. Vollständigkeit kann nicht garantiert werden — insbesondere bei Konzern-Konstruktionen mit Tochterfirmen ohne klare Namens-Bindung, bei Strohmann-Anmeldungen und bei Anmeldungen in nicht durchsuchten Klassen oder Sprachen. Einspruchsfristen sind durch die Patentanwältin in einer eigenständigen Prüfung der Veröffentlichungsdaten zu verifizieren bevor die Frist als verbindlich eingetragen wird.

## Triage-Fragen vor Konkurrenten-Ueberwachung

Bevor die Monitoring-Konfiguration eingerichtet wird, klaere:
1. Sind alle relevanten Konkurrenten-Anmelder-Namen (inkl. Tochtergesellschaften und Strohmann-Kanzleien) erfasst?
2. Welche CPC/IPC-Klassen und Schluesselbegriffe sollen fuer das Keyword-Monitoring eingesetzt werden?
3. Ist eine Einspruchsfrist-Ueberwachung (9 Monate nach Erteilung, § 59 PatG / Art. 99 EPU) eingerichtet?
4. Wird die 18-Monats-Veroeffentlichungsverzoegerung in der Strategieplanung beruecksichtigt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Technische Beschwerdekammer, T 328/87 (Drittbeobachtungen):** Im EPA-Erteilungsverfahren koennen Dritte Beobachtungen (Art. 115 EPU) einreichen, ohne am Verfahren beteiligt zu werden; durch fruehzeitige Beobachtung koennen relevante Entgegenhaltungen in das Pruefungsverfahren eingebracht werden, bevor ein formeller Einspruch noetig wird.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Massnahme: Datum und Leitsatz korrigiert auf tatsaechlichen Inhalt.
Quelle: dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.09.2017&Aktenzeichen=X+ZB+1%2F17
-->
