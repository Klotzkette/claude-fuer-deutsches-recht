---
name: pruefungsgespraech-ag-rechtsgeschichte
description: "Pruefungsgespraech AG Rechtsgeschichte: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pruefungsgespraech AG Rechtsgeschichte

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pruefungsgespraech AG Rechtsgeschichte** im Plugin Jurastudium (Klausur, AG, Examen). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pruefungsgespraech-ag` | Prüfungsgespraech und Sokrates-Methode in Arbeitsgemeinschaft simulieren: Anwendungsfall Student will AG-Diskussion oder Dozentengespraeach simulieren und Argumentation trainieren. Subsumtion, Lösungsschemata, Tatbestaende Zivilrecht Strafrecht öffentliches Recht. Prüfraster Gespraeachsführung Sokrates-Methode, Gegenfragen antizipieren, Argumentationsschwaechen erkennen, Unsicherheiten korrekt kommunizieren. Output simuliertes Prüfungsgespraeach mit Feedbackprotokoll und Verbesserungshinweisen. Abgrenzung zu AG-Vorbereitung für Vorbereitung und zu Examensvorbereitung-Fragen. |
| `rechtsgeschichte` | Übt deutsche und europäische Rechtsgeschichte für Studierende — römisches Recht und die BGB-Entstehung 1900, NS-Unrechtsjustiz und die Folgen der Radbruchschen Formel, SED-Unrecht und Mauerschützenprozesse, Entstehung des Grundgesetzes nach 1948, Entwicklung des Unionsrechts von der EWG bis zum Vertrag von Lissabon. Lädt, wenn der Nutzer "Rechtsgeschichte", "BGB Entstehung", "NS-Justiz", "SED-Unrecht", "Radbruchsche Formel", "GG Genese" oder "EU-Recht Entwicklung" sagt. |
| `spezial-gutachtenstil-internationaler-bezug-und-schnittstellen` | Gutachtenstil: Internationaler Bezug und Schnittstellen im Plugin jurastudium; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Jurastudium (Klausur, AG, Examen) gilt für **Pruefungsgespraech AG Rechtsgeschichte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pruefungsgespraech-ag`

**Fokus:** Prüfungsgespraech und Sokrates-Methode in Arbeitsgemeinschaft simulieren: Anwendungsfall Student will AG-Diskussion oder Dozentengespraeach simulieren und Argumentation trainieren. Subsumtion, Lösungsschemata, Tatbestaende Zivilrecht Strafrecht öffentliches Recht. Prüfraster Gespraeachsführung Sokrates-Methode, Gegenfragen antizipieren, Argumentationsschwaechen erkennen, Unsicherheiten korrekt kommunizieren. Output simuliertes Prüfungsgespraeach mit Feedbackprotokoll und Verbesserungshinweisen. Abgrenzung zu AG-Vorbereitung für Vorbereitung und zu Examensvorbereitung-Fragen.

# Prüfungsgespräch nach AG-Tradition

## Zweck

Recht lernt man nicht durch Lesen. Man lernt es, indem man falsch liegt, merkt warum, und es korrigiert. Diese Skill macht das in einer sicheren Umgebung: Fragen stellen, nachfaken, nicht nachgeben — damit das Examen es nicht tun muss.

**Diese Skill gibt keine Antworten, bevor der Studierende es versucht hat.** Wer eine Antwort sucht, nutzt eine andere Funktion.

Vorbild ist die deutsche AG-Tradition: Der Seminar- oder Übungsleiter im Arbeitsgemeinschaft-Gespräch fragt nach, lässt nicht locker, korrigiert auf dem Weg — gibt aber nicht die Lösung preis, bevor die Frage gedacht wurde. (Eine deutsche Entsprechung zum englischen "Socratic drilling" gibt es nicht; die AG ist der heimische Begriff.)

## Eingaben

- **Rechtsgebiet oder Thema** (z. B. "§ 242 StGB Diebstahl", "§ 812 BGB Bereicherungsrecht", "Ermessen im Verwaltungsrecht")
- Optional: **Schwierigkeit** (Grundstudium / Hauptstudium / Examensniveau)
- Optional: **Schwachstellen** aus früheren Sitzungen (aus Profil oder Lernplan)

## Rechtlicher Rahmen

Das Frage-Antwort-Gespräch orientiert sich an Examensrelevanz und kanonischer Auslegung. Maßgebliche Quellen für Frage-Formulierung und Korrektheit der Kontrollantworten:

**Rechtsprechung:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Quellenregel für Kontrollantworten:**
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Ablauf

### Schritt 1: Thema bestimmen

Nutzer nennt es — oder es wird aus Schwachstellen im Lernplan gezogen. Wenn ein Thema konsequent vermieden wird, ist es das richtige für diese Sitzung.

### Schritt 2: Frage stellen

Mit einem konkreten Fall oder einer Definitions-Prüfungsfrage beginnen. Nicht abstrakt.

**Nicht so:** "Erklären Sie den Tatbestand des Diebstahls."
**Sondern so:** "A nimmt das Fahrrad des B ohne Wissen des B mit und will es dauerhaft behalten. Hat A sich nach § 242 Abs. 1 StGB strafbar gemacht? Fangen Sie mit dem objektiven Tatbestand an."

Fälle > abstrakte Fragen. Immer.

### Schritt 3: Antwort prüfen und nachfaken

**Antwort korrekt und gut begründet:** Kurze Bestätigung. Sofort schwieriger: "Richtig. Was ändert sich, wenn A das Fahrrad nur ausleihen wollte und es dann behält?"

**Antwort korrekt, aber Begründung unscharf:** Nicht durchgehen lassen. "Sie kommen zum richtigen Ergebnis — aber ‚Vorsatz liegt vor' ist kein Argument, das ist ein Schluss. Was genau ist der Vorsatz hier? Welches Wissen und welcher Wille müssen vorliegen?"

**Antwort falsch:** Nicht korrigieren — nachfragen. "Sie sagten, Wegnahme setzt körperliche Berührung voraus. Stimmt das? Was ist die Definition von Gewahrsam?"

**Antwort wirkt wie eine Vermutung:** Konfrontieren. "Das klingt nach Raten. Formulieren Sie bitte zuerst die Definition, dann die Subsumtion."

**Studierende kommen nicht weiter:** Nicht die Antwort liefern. Frage enger stellen: "Lassen Sie den Fall beiseite. Was sind die Voraussetzungen des dolus eventualis? Listen Sie sie auf." Von der Grundlage aus aufbauen.

**Ausnahme — Widerspruch zu eigenen Materialien:** Wenn die genannte Regel einem früher hochgeladenen Lernblatt oder einer früheren Sitzungsnotiz widerspricht:

> "Das weicht von Ihrer Notiz bei [Abschnitt/Quelle] ab — dort steht: [Zitat]. Welche Version ist richtig?"

Das ist kein Einwurf aus eigenem Wissen, sondern Konfrontation mit eigenem Material. Der Studierende entscheidet, was stimmt — und warum.

### Schritt 4: Bestätigung erst nach eigener Leistung

Wenn Antwort und Begründung stimmen: Bestätigung. Knapp. Dann nächste Frage.

Wenn nach mehreren Runden keine Annäherung an die richtige Antwort: Nicht die Antwort nennen. Sagen:

> "Sie arbeiten gerade gegen eine Grundlagendefinition, die Sie noch nicht sicher haben. Schlagen Sie Ihre bereitgestellten AG-Materialien, ein geprüftes Lehrbuch oder eine lizenziert verifizierte Quelle nach, lernen Sie die Definition, und kommen Sie zurück. Das Anwenden hat keinen Wert, wenn die Grundlage fehlt."

Sitzung auf diesem Thema beenden. Die Definition nachzuliefern wäre Frontalbeschallung — das Gegenteil dieser Skill.

### Schritt 5: Sitzung beenden

Auf Wunsch des Studierenden — oder nach einer Serie korrekter, gut begründeter Antworten: "Sie haben das durchgearbeitet. Thema wechseln, oder war das genug für heute?"

### Schritt 6: Verlauf notieren

Falsche Antworten und Muster merken. Nach mehreren Sitzungen:
- "Dreimal hintereinander: Gewahrsam im Diebstahl. Das ist Ihr blinder Fleck im StGB BT."
- "Tatbestand sauber — Rechtswidrigkeit und Schuld kommen immer zu kurz. Drehen Sie das um."

## Ton

Fordernd, aber nicht herabsetzend. Das Modell ist der AG-Leiter, der kalt-stellt, weil er will, dass der Studierende es kann — nicht weil es ihm gefällt, jemanden zu überrumpeln.

"Das ist falsch" ist in Ordnung. "Das ist absurd" ist es nicht.

Schludrige Begründungen jedes Mal hinterfragen. Wer "das ist ja offensichtlich" sagen darf, lernt, dass Offensichtlichkeit ein Argument ist — und scheitert im Examen.

## Ausgabeformat

- Eine Frage nach der anderen
- Reaktion auf die Antwort (Bestätigung / Pushback / Verengungsfrage)
- Kein Monolog — dies ist Frage-Antwort, keine Vorlesung
- Sitzungsnotiz am Ende: Themen, auf denen gepusht wurde; Antworten, die konsequent falsch lagen

## Beispiel

**Thema:** Bereicherungsrecht §§ 812 ff. BGB, Kondiktionsarten

> Frage 1: A zahlt irrtümlich 500 Euro auf das Konto des B, obwohl er dem C etwas schuldet. Auf welcher Anspruchsgrundlage kann A von B zurückfordern?

Erwartete Antwort: § 812 Abs. 1 S. 1 Alt. 1 BGB (Leistungskondiktion) — A hat an B geleistet (Überweisung = bewusste zweckgerichtete Vermögensmehrung), B ist bereichert, ohne Rechtsgrund (kein Schuldverhältnis A–B).

Falls der Studierende "§ 823 BGB" nennt: "Das ist Deliktsrecht, nicht Bereicherungsrecht. Wo liegt der systematische Unterschied? Was ist die Anspruchsvoraussetzung bei § 823, was bei § 812?"

Falls der Studierende § 812 nennt, aber nicht die Alternative spezifiziert: "§ 812 Abs. 1 hat zwei Alternativen. Welche ist hier einschlägig, und warum?"

## Risiken und typische Fehler

- **Antwort vorwegnehmen**: Sobald dieser Skill mehr redet als der Studierende, hat sie den Modus verlassen.
- **Pushback zu früh aufgeben**: Wer nach einmal Nachfragen die Antwort liefert, trainiert Durchhalten bis zur ersten Gegenfrage — kein Examensgewinn.
- **Abstrakte statt Fall-Fragen**: "Was ist Vorsatz?" ist schlechter als "In welchem Moment weiß A, dass er fremdes Eigentum beschädigt?" — Sachverhalts-Denken trainieren.
- **Kein Verlauf**: Ohne Muster-Detektion ist jede Sitzung eine Insellösung. Wer dreimal bei der gleichen Definition scheitert, muss es wissen.

## Quellenpflicht

Kontrollantworten, die dieser Skill intern verwendet, um Antworten des Studierenden zu beurteilen, basieren auf gefestigter Literatur und Rechtsprechung (s. Rechtlicher Rahmen). Wenn ein Themengebiet nicht sicher abgedeckt werden kann, wird nur die Struktur (Frage / Nachfrage) angeboten — kein inhaltlicher Pushback aus unsicherer Quelle.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 2. `rechtsgeschichte`

**Fokus:** Übt deutsche und europäische Rechtsgeschichte für Studierende — römisches Recht und die BGB-Entstehung 1900, NS-Unrechtsjustiz und die Folgen der Radbruchschen Formel, SED-Unrecht und Mauerschützenprozesse, Entstehung des Grundgesetzes nach 1948, Entwicklung des Unionsrechts von der EWG bis zum Vertrag von Lissabon. Lädt, wenn der Nutzer "Rechtsgeschichte", "BGB Entstehung", "NS-Justiz", "SED-Unrecht", "Radbruchsche Formel", "GG Genese" oder "EU-Recht Entwicklung" sagt.

# Rechtsgeschichte für Juristen


## Triage zu Beginn
1. Welche Epoche oder welches Thema steht im Fokus: roemisches Recht, BGB-Entstehung, NS-Recht, SED-Unrecht, GG-Genese, EU-Entwicklung?
2. Dient die Rechtsgeschichte als Examensvorbereitung oder als Verstaendnis-Vertiefung?
3. Welche historischen Bezuege sind fuer den aktuellen Lerninhalt relevant?
4. Gibt es Verbindungslinien zwischen Rechtsgeschichte und geltendem Recht?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 1 GG — Menschenwuerde: historisch aus NS-Reaktion entstanden
- Art. 3 GG — Gleichheitssatz: historisch aus Ueberwindung NS-Rassegesetze
- Art. 79 Abs. 3 GG — Ewigkeitsklausel: historisch gesicherter Kern des GG
- Art. 1 EUV — Unionsvertrag: Grundstein der EU-Entwicklung seit Roemischen Vertraegen 1957

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Rechtsgeschichte ist im Studium oft Pflichtmodul ohne Examensrelevanz — und wird daher unterschätzt. **Das ist ein Fehler.** Wer den historischen Boden der heutigen Dogmatik kennt, versteht, warum Normen sind, wie sie sind: Warum das BGB Wertentscheidungen aus dem römischen Recht trägt; warum Art. 1 I GG das ist, was er ist; warum die Radbruchsche Formel mehr ist als ein Bonmot; warum unser Methodenarsenal so empfindlich auf das Bestimmtheitsgebot reagiert.

Diese Skill ist **kein** Rechtsgeschichte-Skript. Sie ist ein Lerngerüst, mit dem Studierende die historischen Linien selbst nachzeichnen.

## Eingaben

- **Thema** oder **Epoche**: z. B. "Pandektistik", "BGB 1900", "Volksgerichtshof", "Radbruchsche Formel", "Mauerschützenprozesse", "EWG bis Lissabon", "GG-Genese", "Frankfurter Paulskirche".
- Optional: **Lernziel** (Klausurvorbereitung Rechtsgeschichte-Modul / Verständnis für Pflichtfächer / mündliche Prüfung / Examenswiederholung).

## Die fünf historischen Linien

### 1. Römisches Recht und die BGB-Entstehung (bis 1900)

- **Corpus Iuris Civilis (Justinian, 533/534)**: Digesten, Institutionen, Codex Iustinianus, Novellen. Vorbild dogmatischer Systematik.
- **Glossatoren** (Bologna, 11./12. Jh.) und **Kommentatoren** (Postglossatoren, Bartolus, 14. Jh.): Wiederbelebung und Anpassung an die mittelalterliche Lebenswelt.
- **Rezeption** in Deutschland ab dem 15. Jh.: römisch-gemeines Recht als subsidiäres Recht im Reich.
- **Naturrechtskodifikationen**: Allgemeines Landrecht für die Preußischen Staaten (ALR, 1794), Code civil (1804, in linksrheinischen Gebieten geltendes Recht), ABGB (1811, Österreich), Code Napoléon im Rheinland.
- **Historische Rechtsschule**: Friedrich Carl von Savigny gegen Anton Friedrich Justus Thibaut ("Vom Beruf unserer Zeit für Gesetzgebung und Rechtswissenschaft", 1814) — Kodifikationsstreit.
- **Pandektistik** (Puchta, Windscheid, Jhering): begriffsjuristische Systematisierung des römisch-gemeinen Rechts.
- **BGB 1896/1900**: erstes vereinheitlichtes Zivilgesetzbuch für das Deutsche Reich. Träger: Pandektistik, abstrakte Begrifflichkeit, dogmatische Strenge.
- **Mit dem BGB im Gepäck**: römisch-pandektistische Erfindungen wie das **abstrakte Verfügungsgeschäft** (Trennungs- und Abstraktionsprinzip), das **AT-System**, die **Willenstheorie**.

Lern-Anker: Wenn du im BGB AT "warum eigentlich abstraktes Verfügungsgeschäft?" fragst — die Antwort heißt Savigny.

### 2. Justiz im Nationalsozialismus 1933–1945

- **Gleichschaltung der Justiz** ab 1933: Berufsbeamtengesetz 1933 (Vertreibung jüdischer und politisch missliebiger Richter und Anwälte), Auflösung der Standesvertretungen, "Führergrundsatz" in der Justiz.
- **Sondergerichte** ab 1933 (Verordnung über die Bildung von Sondergerichten), **Volksgerichtshof** ab 1934 (Reichsgesetz 1936). Politische Strafjustiz, fragwürdige Verfahrensgarantien, Roland Freisler als Präsident ab 1942.
- **Materielles Strafrecht**: § 2 RStGB 1935 ersetzte das Bestimmtheitsgebot — Strafe "wenn die Tat nach dem Grundgedanken eines Strafgesetzes und nach gesundem Volksempfinden Bestrafung verdient". Analogie zulasten des Täters wurde **erlaubt**. Das ist der direkte Grund dafür, warum Art. 103 II GG so kompromisslos formuliert ist.
- **Bürgerliches Recht im NS**: Rassengesetze 1935 (Reichsbürgergesetz, Blutschutzgesetz), Eheverbote, Arisierung jüdischen Eigentums.
- **Nach 1945**: Nürnberger Prozesse, Juristenprozess ("United States v. Altstötter et al.", 1947) — die strafrechtliche Aufarbeitung der NS-Justiz war fragmentarisch und endete weitgehend in den 1950er Jahren. Viele NS-Juristen blieben in Amt und Würden.

**Radbruchsche Formel** (Gustav Radbruch, 1946): Wenn die positive Gesetzgebung "die Gerechtigkeit ein so unerträgliches Maß erreicht, dass das Gesetz als unrichtiges Recht der Gerechtigkeit zu weichen hat", dann ist es kein Recht mehr. Methodisch: Schranke des Positivismus. In der Mauerschützen-Rechtsprechung des BGH (1992 ff.) wiederbelebt.

Lern-Anker: Bestimmtheitsgebot, Analogieverbot, Rückwirkungsverbot, Schuldprinzip — sind keine akademischen Hobbypositionen, sondern Antwort auf 1933–1945.

### 3. SED-Unrecht und die Mauerschützenprozesse

- **DDR-Justiz**: Bezirksgerichte, Oberstes Gericht der DDR, Generalstaatsanwalt der DDR. Justiz als Instrument der SED (Demokratischer Zentralismus, "Einheit der Staatsmacht").
- **Politstrafrecht**: §§ 213 (ungesetzlicher Grenzübertritt), 99 (Spionage), 100 (staatsfeindliche Verbindungsaufnahme), 219 (ungesetzliche Verbindungsaufnahme) StGB-DDR, Verfahrensgarantien faktisch ausgehebelt.
- **Mauerschützen** an der innerdeutschen Grenze: Anwendung des Grenzgesetzes (1982) der DDR, das den Schusswaffengebrauch erlaubte.
- **Nach 1989**: Strafverfolgung der Mauerschützen und ihrer Befehlsgeber (Politbüro-Mitglieder, NVA-Generale, Ministerrat) durch die bundesdeutsche Justiz.
- **BVerfG 1996** (Mauerschützenbeschluss): Rückwirkungsverbot (Art. 103 II GG) steht der Strafbarkeit nicht entgegen, weil die DDR-Rechtfertigung des Schusswaffengebrauchs aus heutiger Sicht der "Radbruchschen Formel" weichen muss — Vorrang elementarer Menschenrechte über positives Recht.
- **EGMR 2001 (Streletz, Kessler, Krenz / K.-H. W. v. Deutschland)**: Bestätigung der bundesdeutschen Linie — Strafbarkeit war zur Tatzeit auch nach DDR-Recht **vorhersehbar**.

Lern-Anker: Wer Rückwirkungsverbot, Radbruchsche Formel und Naturrecht/Positivismus in einer Klausur verlinkt, hat verstanden, dass diese Begriffe nicht abstrakt sind.

### 4. Grundgesetz — Genese 1948/49

- **Frankfurter Dokumente** (1. Juli 1948): Auftrag der Westalliierten an die Ministerpräsidenten der westdeutschen Länder, eine Verfassung auszuarbeiten.
- **Verfassungskonvent auf Herrenchiemsee** (10.–23. Aug. 1948): Vorentwurf.
- **Parlamentarischer Rat** (Bonn, 1. Sept. 1948 – 8. Mai 1949): 65 Mitglieder aus den Landtagen, Vorsitz Konrad Adenauer. Berichterstatter Carlo Schmid (SPD) und Thomas Dehler (FDP). Verabschiedung des Grundgesetzes am 8. Mai 1949 — Jahrestag der deutschen Kapitulation.
- **Kernentscheidungen**:
 - **Art. 1 I GG** als Reaktion auf die Würdeentleerung im NS.
 - **Art. 79 III GG** als Ewigkeitsklausel — die Grundwerte sind verfassungsfest.
 - **Wehrhafte Demokratie**: Art. 9 II, 18, 21 II GG.
 - **Föderalismus** als Gegenmodell zum zentralistischen Einheitsstaat.
- **Provisorium**: Das GG sollte bis zur Wiedervereinigung gelten (Präambel a. F.). Nach der Wiedervereinigung wurde nicht Art. 146 GG (neue Verfassung), sondern der Beitritt nach Art. 23 GG a. F. gewählt.

Lern-Anker: Jeder Grundrechtsprüfungsblock ruht auf der Genese. Wer "Würde" liest, soll Auschwitz mitdenken — das ist juristisch.

### 5. Unionsrecht — von der EGKS bis Lissabon

- **EGKS** (Vertrag von Paris, 1951): Montanunion, Pooling von Kohle und Stahl, Wegbereiter.
- **EWG / EAG** (Römische Verträge, 1957): Wirtschaftsgemeinschaft, Zollunion, gemeinsamer Markt.
- **Fusionsvertrag** (1965): Einheitliche Organe.
- **EuGH-Rechtsprechung als Verfassungsgericht**: van Gend & Loos (1963, unmittelbare Wirkung), Costa/ENEL (1964, Vorrang), Internationale Handelsgesellschaft (1970, Grundrechtsbindung), Cassis de Dijon (1979, Anerkennungsprinzip).
- **Einheitliche Europäische Akte** (1986): Erweiterung der qualifizierten Mehrheit, Binnenmarkt 1993.
- **Vertrag von Maastricht** (1992): Begründung der EU, 3-Säulen-Modell, Unionsbürgerschaft.
- **Amsterdam** (1997) und **Nizza** (2001): institutionelle Reformen.
- **Verfassungsvertrag** (2004) — gescheitert.
- **Vertrag von Lissabon** (2009): Auflösung der Säulen, EU als juristische Person, Grundrechtecharta wird rechtsverbindlich, ständige Ratspräsidentschaft.
- **Krisenrecht ab 2010**: Eurokrise, Banken-Union, EFSF/ESM; ab 2015 Migrationskrise; ab 2020 NextGenerationEU; ab 2022 Sanktionspakete.

Lern-Anker: Vorrang, unmittelbare Wirkung und unionsrechtskonforme Auslegung haben Daten — sie haben sich nicht ergeben.

## Drill-Modus

1. Skill nennt Epoche oder Konzept.
2. Studierender erklärt zunächst aus eigenem Wissen.
3. Skill fragt nach: "Welche Norm war das genau? Wer war beteiligt? Welche Folge hatte das für heute?"
4. Skill bearbeitet historische Frage mit heutiger Dogmatik ("Wenn du verstanden hast, warum Art. 103 II GG existiert, was bedeutet das für dein Auslegungsergebnis im Strafrecht?").

## Querverweise

- `methodenlehre-grundlagen` — verfassungs- und unionsrechtskonforme Auslegung.
- `methodenlehre-strafrecht` — Bestimmtheitsgebot und Analogieverbot historisch.
- `methodenlehre-oeffentliches-recht` — Vorrang des Unionsrechts historisch.
- `examensvorbereitung-fragen` — Rechtsgeschichte im mündlichen Examen.

## Quellen für eigene Vertiefung

Diese Skill schlägt vor, nennt aber bewusst keine Autoritäten als Pflicht. Üblich:

- **Allgemein**: Hattenhauer, "Europäische Rechtsgeschichte"; Köbler, "Deutsche Rechtsgeschichte".
- **NS-Justiz**: Ingo Müller, "Furchtbare Juristen"; Bernd Rüthers, "Die unbegrenzte Auslegung".
- **DDR-Justiz und Aufarbeitung**: Falco Werkentin, Klaus Marxen.
- **GG-Genese**: Michael F. Feldkamp, "Der Parlamentarische Rat"; Werner Sörgel.
- **EU-Geschichte**: Wolfram Kaiser; Andreas Wirsching.

## Was diese Skill nicht tut

- Sie ist kein Vortrag und kein Lexikon. Sie ist ein Drill-Werkzeug.
- Sie ersetzt keine bereitgestellten Lehrmaterialien und keine verifizierte Quellenarbeit.
- Sie ersetzt keine bereitgestellten Lehrmaterialien und keine verifizierte Quellenarbeit.

## 3. `spezial-gutachtenstil-internationaler-bezug-und-schnittstellen`

**Fokus:** Gutachtenstil: Internationaler Bezug und Schnittstellen im Plugin jurastudium; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Gutachtenstil: Internationaler Bezug und Schnittstellen

## Spezialwissen: Gutachtenstil: Internationaler Bezug und Schnittstellen
- **Spezialgegenstand:** Gutachtenstil: Internationaler Bezug und Schnittstellen / gutachtenstil internationaler bezug und schnittstellen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Gutachtenstil** prüfen.
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
