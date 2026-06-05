---
name: stbv-strafbefehl-abwesenheit-vertretung
description: "Stbv Strafbefehl Abwesenheit Vertretung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Stbv Strafbefehl Abwesenheit Vertretung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Stbv Strafbefehl Abwesenheit Vertretung** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stbv-strafbefehl-pruefung-bauleiter` | Bauleiter Pruefung Strafbefehl § 407 StPO: Tatvorwurf, Strafhoehe, Folgen, Einspruchsfrist. Pruefraster fuer Verteidiger Erstgespraech. |
| `strafbefehl-abwesenheit-vertretung` | Mandant kann oder will zur Hauptverhandlung nach Strafbefehl-Einspruch nicht erscheinen und Verteidiger soll ihn vertreten. Prüfraster Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO Voraussetzungen und Antrag. Verwerfung des Einspruchs § 412 StPO bei unentschuldigtem Ausbleiben Folgen. Wiedereinsetzung nach Verwerfung § 44 StPO. Output Entbindungsantrag Vertretungsvollmacht Muster-Sprechzettel für Verhandlung ohne Mandant. Abgrenzung: strafbefehl-hauptverhandlung-vorbereitung für allgemeine HV-Vorbereitung. |
| `strafbefehl-akteneinsicht-147` | Akteneinsicht im Strafbefehlsverfahren nach § 147 StPO. Antrag bei Staatsanwaltschaft oder Amtsgericht. Versagungsgründe § 147 Abs. 2 StPO. Akte im Strafbefehlsverfahren: Ermittlungsakte Messakte Bußgeldheft. Beschwerderecht § 147 Abs. 5 StPO. eAkte § 32f StPO. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Stbv Strafbefehl Abwesenheit Vertretung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stbv-strafbefehl-pruefung-bauleiter`

**Fokus:** Bauleiter Pruefung Strafbefehl § 407 StPO: Tatvorwurf, Strafhoehe, Folgen, Einspruchsfrist. Pruefraster fuer Verteidiger Erstgespraech.

# StBV: Strafbefehl-Pruefung

## Spezialwissen: StBV: Strafbefehl-Pruefung
- **Spezialgegenstand:** StBV: Strafbefehl-Pruefung / stbv strafbefehl pruefung bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, StBV, BGH, BVerfG.
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

## 2. `strafbefehl-abwesenheit-vertretung`

**Fokus:** Mandant kann oder will zur Hauptverhandlung nach Strafbefehl-Einspruch nicht erscheinen und Verteidiger soll ihn vertreten. Prüfraster Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO Voraussetzungen und Antrag. Verwerfung des Einspruchs § 412 StPO bei unentschuldigtem Ausbleiben Folgen. Wiedereinsetzung nach Verwerfung § 44 StPO. Output Entbindungsantrag Vertretungsvollmacht Muster-Sprechzettel für Verhandlung ohne Mandant. Abgrenzung: strafbefehl-hauptverhandlung-vorbereitung für allgemeine HV-Vorbereitung.

# Abwesenheit in der Hauptverhandlung — § 411 Abs. 2 StPO

## Triage zu Beginn

1. **Erscheinungspflicht des Mandanten?** — § 411 Abs. 2 StPO: Angeklagter kann auf Anordnung des Richters von Erscheinungspflicht entbunden werden wenn nur Sachverstaendige gehört werden oder Sachverhalt unstreitig.
2. **Entbindungsantrag bereits gestellt?** — Antrag muss vor dem Termin gestellt werden; Gericht entscheidet nach Ermessen.
3. **Was passiert bei unentschuldigtem Ausbleiben?** — § 412 StPO: Gericht kann Einspruch verwerfen; Mandant muss Wiedereinsetzung beantragen (§ 44 StPO).
4. **Verteidiger kann allein handeln?** — Nach Entbindung kann Verteidiger die HV allein fuehren (§ 411 Abs. 2 StPO).
5. **Erkrankung des Mandanten?** — Entschuldigung durch Attest; Terminsverlegung beantragen.

## Zentrale Normen

- **§ 411 Abs. 2 StPO** — Entbindung von Erscheinungspflicht: Gericht kann anordnen, Verteidiger kann allein handeln
- **§ 412 StPO** — Verwerfung des Einspruchs: unentschuldigtes Ausbleiben → Einspruch gilt als zurueckgenommen; Beschluss
- **§ 412 Satz 2 StPO** — Wiedereinsetzung moeglich wenn Ausbleiben entschuldigt
- **§ 44 StPO** — Wiedereinsetzung allgemein (s. separaten Skill)
- **§ 231 StPO** — Unterbrechung bei Ausbleiben des Angeklagten (in der allgemeinen Hauptverhandlung; § 411 lex specialis)
- **§ 213 StPO** — Terminbestimmung; Terminsverlegung moeglich

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Abwesenheits-Strategie

```
Mandant erscheint nicht zur HV — warum?
├─ Vorab Entbindungsantrag gestellt und genehmigt?
│ └─ Verteidiger leitet HV allein → regulaere Beweisaufnahme und Plaedoyer
├─ Mandant krank am HV-Tag?
│ ├─ Attest vorhanden → Terminsverlegung beantragen, Fax ans Gericht
│ └─ Kein Attest → Gericht informieren, Terminverlegung muendlich beantragen
├─ Mandant hat vergessen / nicht erschienen ohne Entschuldigung?
│ └─ Einspruch kann verworfen werden (§ 412 StPO)
│ └─ Sofort Wiedereinsetzungsantrag (§ 44 StPO) + Einspruch nachholen
└─ Mandant weigert sich zu erscheinen?
 └─ Entbindungsantrag stellen und erklaeren dass HV ohne ihn moeglich
```

## Output-Template Entbindungsantrag

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]
Hauptverhandlungstermin: [DATUM]

Antrag auf Entbindung von der Erscheinungspflicht nach § 411 Abs. 2 StPO

Ich beantrage meinen Mandanten [NAME] von der Pflicht zum
persoenlichen Erscheinen in der Hauptverhandlung am [DATUM]
zu entbinden.

Begruendung: Der Sachverhalt ist unstreitig. Es werden lediglich
[Sachverstaendige / keine schwierigen Beweisfragen] gehört.
Mein Mandant ist durch mich vollstaendig vertreten.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Entbindungsantrag vor dem Termin stellen, nicht am Terminstag.
- Bei Verwerfung nach § 412 StPO: sofort Wiedereinsetzungsantrag (1-Woche-Frist § 45 StPO).
- Mandant immer ueber Folgen des Nichterscheinens aufklaeren.
- Anwaltliche Endkontrolle vor dem Termin.

## 3. `strafbefehl-akteneinsicht-147`

**Fokus:** Akteneinsicht im Strafbefehlsverfahren nach § 147 StPO. Antrag bei Staatsanwaltschaft oder Amtsgericht. Versagungsgründe § 147 Abs. 2 StPO. Akte im Strafbefehlsverfahren: Ermittlungsakte Messakte Bußgeldheft. Beschwerderecht § 147 Abs. 5 StPO. eAkte § 32f StPO.

# Akteneinsicht im Strafbefehlsverfahren — § 147 StPO

## Triage zu Beginn

1. **Verfahrensstadium klären:** Ist der Strafbefehl bereits erlassen oder noch im Ermittlungsverfahren? Liegt die Akte noch bei der Staatsanwaltschaft oder schon beim Amtsgericht?
2. **Deliktart:** Strassenverkehrsdelikt (§§ 316, 315c, 142 StGB), Betrug, Koerperverletung, Diebstahl — beeinflusst welche Bestandteile der Akte kritisch sind.
3. **Liegt eine Vollmacht des Mandanten vor?** — Ohne Vollmacht keine Akteneinsicht (§ 147 Abs. 1 StPO: dem Verteidiger steht Akteneinsicht zu).
4. **Digitale oder Papierakte?** — eAkte: elektronische Uebersendung nach § 32f StPO; Papierakte: physische Uebersendung oder Einsicht in der Geschaeftsstelle.
5. **Vollstaendigkeit pruefen:** Bussgeldheft, Messprotokoll, Schulungsnachweis, Befundbericht — bei Verkehrsdelikten besonders wichtig.

## Zentrale Normen

- **§ 147 Abs. 1 StPO** — Recht auf Akteneinsicht fuer den Verteidiger
- **§ 147 Abs. 2 StPO** — Versagungsrecht der Staatsanwaltschaft bei Gefaehrdung des Untersuchungszwecks (nur im laufenden Ermittlungsverfahren vor Abschluss)
- **§ 147 Abs. 4 StPO** — Akteneinsicht fuer nicht verteidigten Beschuldigten in entsprechender Anwendung
- **§ 147 Abs. 5 StPO** — Rechtsbehelf gegen Versagung: Antrag auf gerichtliche Entscheidung
- **§ 406e StPO** — Akteneinsicht fuer Verletzte und Nebenklaeger
- **§ 32f StPO** — elektronische Akteneinsicht (eAkte)
- **§ 49 OWiG i.V.m. § 147 StPO** — entsprechende Geltung im Bussgeldbescheid-Verfahren

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Daten als Beweisgrundlage im Strafbefehl): Akteneinsicht muss die Auswertungs- und Authentifizierungsprotokolle der ANOM-Daten umfassen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25
- BGH (GSSt) 03.02.2025 — GSSt 1/24 (KCanG): Akteneinsicht insbesondere in Mengenermittlung und Auswertung; sanktionsfreie Eigenkonsummenge fuer Tatverdachtspruefung herauszupraeparieren. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 speziell zu § 147 StPO im Strafbefehlsverfahren ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 147 StPO Strafbefehl" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Vollmacht sichern** — ohne Vollmacht kein Anspruch.
2. **Akteneinsichtsgesuch stellen** bei der Staatsanwaltschaft (Ermittlungsverfahren) oder Amtsgericht (nach Anklage/Strafbefehl-Erlass); Inhalt: Aktenzeichen, Mandantenname, Vollmacht, Bitte um Uebersendung aller Aktenbestandteile einschliesslich Beiakten.
3. **Vollstaendigkeit pruefen bei Eingang:** Inhaltsverzeichnis vorhanden? Fehlende Teile sofort ruegen.
4. **Bei Verkehrsdelikten:** Messakte, Eichschein, Bedienungsanleitung, Schulungsnachweis, Rohmessdaten gesondert anfordern.
5. **Bei Versagung:** Rechtsbehelf nach § 147 Abs. 5 StPO beim Ermittlungsrichter (§ 162 StPO).
6. **Aktenexzerpt und Beweismittelverzeichnis anlegen** — Grundlage fuer Einlassung und Beweisantraege.

## Output-Template Akteneinsichtsgesuch

**Adressat:** Staatsanwaltschaft [ORT] / Amtsgericht [ORT] — Tonfall: sachlich-foermlich

```
An die Staatsanwaltschaft [ORT]
[Anschrift]

In der Strafsache gegen
[NAME MANDANT]
Az.: [AKTENZEICHEN]

Antrag auf Akteneinsicht nach § 147 StPO

Sehr geehrte Damen und Herren,

ich zeige an, dass ich die Verteidigung von Herrn/Frau [NAME MANDANT]
uebernommen habe. Vollmacht liegt bei.

Ich beantrage vollstaendige Akteneinsicht nach § 147 Abs. 1 StPO
einschliesslich aller Beiakten, Asservate und ggf. Messunterlagen.

[Bei Verkehrsdelikt: Ich bitte gesondert um Uebersendung der
vollstaendigen Messakte einschliesslich Rohmessdaten, Eichschein,
Bedienungsanleitung und Schulungsnachweis des Messbeamten.]

Mit kollegialen Gruessen
[KANZLEI]
```

## Harte Leitplanken

- Akteneinsicht nie ohne Vollmacht beantragen.
- Rohmessdaten bei Geschwindigkeitsmessungen grundsaetzlich mitverlangen.
- Bei Versagung sofort Rechtsbehelf nach § 147 Abs. 5 StPO — Einspruchsfrist laeuft unabhaengig davon.
- Anwaltliche Endkontrolle bei jedem Schritt.
