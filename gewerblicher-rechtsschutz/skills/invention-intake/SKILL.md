---
name: invention-intake
description: >
  Erstprüfung einer Erfindungsmeldung nach deutschem Recht — Neuheit,
  erfinderische Tätigkeit, technischer Charakter (EPÜ), Schutzfähigkeit,
  Arbeitnehmererfindung (ArbnErfG) und strategischer Wert. Lädt, wenn eine
  Erfindungsmeldung eingereicht wird und eine Ersteinschätzung zu Anmeldung,
  Weiterverfolgung oder Ablehnung benötigt wird.
language: de
triggers:
  - "Erfindungsmeldung"
  - "Arbeitnehmererfindung"
  - "Patentanmeldung prüfen"
  - "Inanspruchnahme Erfindung"
  - "technische Schutzrechte"
  - "Neuheitsprüfung"
  - "Schutzrechtsstrategie Patent"
  - "ArbnErfG Meldung"
---

# Erfindungseingang — Erstprüfung

## Zweck

Diese Skill führt eine strukturierte Erstprüfung einer Erfindungsmeldung durch. Sie schirmt offensichtliche Ausschlussgründe ab, identifiziert kritische Fristen (insbesondere neuheitsschädliche Vorveröffentlichungen nach § 3 PatG) und empfiehlt eine von drei Handlungsoptionen: **WEITERVERFOLGEN** (Beauftragung einer Patentrecherche und Einschaltung eines Patentanwalts), **KLÄREN** (Rückfragen an den Erfinder oder Spezialisten) oder **ABLEHNEN** (mit konkreter Begründung).

Die Skill trifft keine Patentierbarkeitsaussage. Eine solche setzt eine vollständige Patentrecherche, Anspruchskonstruktion und das fachliche Urteil eines zugelassenen Patentanwalts voraus.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

Wenn der Nutzer keine Erfindungsmeldung eingereicht hat, werden folgende Angaben in einem Durchgang abgefragt:

1. **Was ist die Erfindung?** Beschreibung in eigenen Worten — was sie tut, wie sie funktioniert, was die Kernidee ist.
2. **Welches Problem wird gelöst?** Was war zuvor nicht möglich oder mangelhaft?
3. **Worin liegt der Unterschied zum Stand der Technik?** Was haben andere bisher gemacht, und was macht diese Erfindung anders?
4. **Wer hat erfunden, und wann?** Namen, Arbeitsverhältnis (Arbeitnehmer/Freier Mitarbeiter?), ungefähres Entstehungsdatum.
5. **Wurde die Erfindung bereits offenbart?** Publikation, Messe, Konferenz, Angebot, öffentliches Repository, Kundendemonstration (auch unter NDA). Wenn ja: wann und wie.
6. **Wird die Erfindung bereits genutzt oder ist sie geplant?** In Produktion, im Pilotbetrieb, auf der Roadmap oder noch auf dem Papier?
7. **Welches Technologiegebiet?** Software, Hardware, Mechanik, Biotechnologie, KI/ML, Chemie, Medizinprodukt etc.

Bei formeller Erfindungsmeldung (IDF oder Unternehmensformular): Felder daraus entnehmen, nur Fehlende erfragen.

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 1–5 PatG** — Patentierbarkeitsvoraussetzungen: Neuheit (§ 3), erfinderische Tätigkeit (§ 4), gewerbliche Anwendbarkeit (§ 5)
- **Art. 52–57 EPÜ** — Patentierbarkeit im europäischen Patentsystem; technischer Charakter als Voraussetzung; Art. 56 EPÜ erfinderische Tätigkeit (Aufgabe-Lösungs-Ansatz)
- **§§ 5–12 ArbnErfG** — Meldepflicht (§ 5), Inanspruchnahme durch den Arbeitgeber (§ 6 Abs. 1: Frist 4 Monate), unbeschränkte vs. beschränkte Inanspruchnahme; Vergütungspflicht (§§ 9 ff. ArbnErfG)
- **§ 3 Abs. 1 PatG** — Absolutes Neuheitserfordernis: jede Offenbarung vor dem Anmeldetag ist neuheitsschädlich; eine Schonfrist für Vorveröffentlichungen gilt im deutschen und europäischen Patentrecht nicht
- **§§ 1–3 GebrMG** — Gebrauchsmuster als schnellerer Schutzrechtsweg (keine erfinderische Tätigkeit im gleichen Maßstab, aber Neuheit + erfinderischer Schritt erforderlich)
- **§ 26 GeschGehG** — Geschäftsgeheimnis als Alternative bei mangelnder Erkennbarkeit der Verletzung

### Leitentscheidungen

- BGH, Urt. v. 11.02.2014 – X ZR 107/12, GRUR 2014, 647 (Bildunterschrift II) — Neuheitsschädlichkeit von Internetpublikationen; maßgeblicher Zeitpunkt der öffentlichen Zugänglichkeit
- BGH, Urt. v. 26.10.2010 – X ZR 47/07, GRUR 2011, 129 (Lernspiele) — Abgrenzung technische Lehre / abstrakte Idee; Anforderungen an den technischen Charakter
- BGH, Urt. v. 17.10.2001 – X ZR 58/99, BGHZ 149, 68 (Luftverteiler) — Arbeitnehmererfindung: Abgrenzung Dienst- und freie Erfindung; Meldepflicht nach § 5 ArbnErfG
- BGH, Urt. v. 16.04.2002 – X ZR 127/99, GRUR 2002, 801 (Abgestuftes Getriebe) — Berechnung der Arbeitnehmererfindervergütung; Anteilsfaktor

### Kommentare

- Benkard/Melullis, PatG, 12. Aufl. 2023, § 3 Rn. 1 ff. (Neuheitsbegriff, Stand der Technik)
- Bartenbach/Volz, ArbnErfG, 6. Aufl. 2019, § 5 Rn. 1 ff. (Meldepflicht und Form) und § 9 Rn. 1 ff. (Vergütung)
- Mes, PatG/GebrMG, 5. Aufl. 2020, § 1 Rn. 20 ff. (technischer Charakter, Software- und KI-Erfindungen)
- BeckOK PatR/Bremi, 30. Ed. (Stand 01.01.2025), Art. 56 EPÜ Rn. 10 ff. (Aufgabe-Lösungs-Ansatz EPA)

## Ablauf

### Schritt 1: Meldung aufnehmen

Vorliegende Erfindungsmeldung vollständig lesen. Fehlen Angaben: Rückfragen gemäß Abschnitt „Eingaben" in einem Durchgang stellen. Unvollständige Meldungen nicht screenen — ein Screening von „einer neuen KI-Lösung für X" ohne technische Substanz ist schlechter als kein Screening.

**Arbeitnehmererfindung prüfen:** Wenn der Erfinder Arbeitnehmer ist, zunächst klären: Handelt es sich um eine Diensterfindung (§ 4 Abs. 2 ArbnErfG: Entstehung aus dem Arbeitverhältnis oder wesentlich auf betriebliche Erfahrungen/Tätigkeiten beruhend)? Wenn ja: Meldepflicht nach § 5 ArbnErfG auslösen und Inanspruchnahmefrist (4 Monate, § 6 Abs. 1) dokumentieren.

### Schritt 2: Sechs Prüfungsschirme

Jeden Schirm in der Reihenfolge abarbeiten. Ergebnis je Schirm: `✓ grün`, `🟡 unklar — Klärungsbedarf`, `🔴 Rote Flagge`.

#### Schirm 1: Neuheitssignale (§ 3 PatG, Art. 54 EPÜ)

**Rote Flaggen (🔴):**
- „Wir haben [bekannte Technik] auf [neues Gebiet] angewandt" — Anwendung bekannter Methoden ohne technische Besonderheit
- „Wettbewerber machen etwas Ähnliches" — Beschreibung selbst stellt Neuheit in Frage
- Merkmal findet sich bereits in öffentlich zugänglichen Produkten, Publikationen oder Patenten

**Grüne Flaggen (✓):**
- Neuer **Mechanismus** — nicht nur neue Anwendung, sondern neue technische Wirkungsweise
- Neue **Kombination** mit unerwartetem Ergebnis
- Lösung eines bisher ungelösten Problems mit spezifischer technischer Lehre

#### Schirm 2: Erfinderische Tätigkeit (§ 4 PatG, Art. 56 EPÜ)

EPA-Prüfungsansatz: Aufgabe-Lösungs-Ansatz. Würde ein Fachmann ausgehend vom nächstliegenden Stand der Technik und der zugrunde liegenden technischen Aufgabe zur beanspruchten Lösung gelangen?

**Rote Flaggen (🔴):**
- Kombinieren bekannter Elemente auf vorhersehbare Weise (predictable combination)
- Routinemäßige Optimierung bekannter Parameter ohne überraschenden Effekt
- „Obvious to try" — eine aus wenigen naheliegenden Alternativen ohne Hindernis

**Grüne Flaggen (✓):**
- Stand der Technik lehrte vom Lösungsweg ab (teaching away)
- Unerwarteter technischer Effekt (surprising effect)
- Langbekanntes Problem, das trotz Bemühungen bisher ungelöst geblieben ist

#### Schirm 3: Technischer Charakter und Schutzfähigkeit (Art. 52 EPÜ, § 1 PatG)

Software, KI/ML und Geschäftsmethoden: Nicht per se ausgeschlossen, aber technischer Charakter muss vorliegen. EPA: „technical character" — weitgehend jeder Bezug zur Technik genügt; Abgrenzung gilt auf der Ebene der erfinderischen Tätigkeit.

**Rote Flaggen (🔴):**
- Reine Geschäftsmethode ohne technische Umsetzung
- Mathematischer Algorithmus ohne technische Anwendung
- Ablauf menschlicher Tätigkeiten ohne computergestützte oder physische Komponente
- KI-Invention: Schutzbegehren richtet sich allein auf Funktion (empfehlen, klassifizieren, vorhersagen) ohne konkrete technische Mittel

**Grüne Flaggen (✓):**
- Technische Verbesserung des Computers selbst (Architektur, Sicherheit, Effizienz)
- Technische Mittel werden konkret beschrieben, nicht nur Ergebnisse beansprucht
- Einbettung in technisches Gebiet (Bildverarbeitung, Signalübertragung, Steuerung)

#### Schirm 4: Neuheitsschädliche Vorveröffentlichung / Fristen (§ 3 PatG)

Im deutschen und europäischen Patentrecht gilt **absolutes Neuheitserfordernis**: jede öffentliche Zugänglichmachung vor dem Anmeldetag ist neuheitsschädlich. Eine Schonfrist für Vorveröffentlichungen gilt nicht.

**Ausnahme:** § 3 Abs. 5 PatG (Ausstellungsprioritätsprinzip) und Art. 55 EPÜ (offensichtlicher Missbrauch oder Ausstellungsprivileg) — sehr eng, nicht als Sicherheitsnetz einplanen.

Kategorisierung:

**🔴 Wahrscheinlich neuheitsschädlich:**
- Öffentliche Veröffentlichung, Verkauf, Angebot, Messedemonstration, öffentliches Repository **vor dem Anmeldetag**
- Preprint, Konferenzbeitrag, Social-Media-Post, Blogbeitrag mit technischem Inhalt

**🟡 Fristdruck:**
- Veröffentlichung liegt vor, Anmeldung noch nicht erfolgt — **sofortiger Handlungsbedarf**

**✓ Unbedenklich:**
- Keine Offenbarung außerhalb vertraulicher Kanäle
- Kundenpräsentation unter NDA (Sorgfalt: NDA-Reichweite prüfen)

Konkret erfragen: Konferenzbeiträge (auch eingereicht, nicht nur angenommen), Preprints, öffentliche Repositories, Messeauftritte, Angebote an Kunden, Investorenpräsentationen ohne NDA.

#### Schirm 5: Erkennbarkeit einer Verletzung (Detectability)

Ist eine Verletzung am Markt erkennbar? Server-seitige Algorithmen, interne Fertigungsschritte und reine Datenverarbeitungsmethoden ohne erkennbare Außenwirkung sind schwer durchzusetzen.

**🔴 Geringe Erkennbarkeit:**
- Server-seitiger Algorithmus ohne erkennbares Ausgabemuster
- Internes Fertigungsverfahren (z. B. neuer Ätzschritt in Halbleiterproduktion)
- Trainings-Methodik für ML-Modell — nur durch aufwendige Tests erahnbar

Bei geringer Erkennbarkeit: Abwägung Patent vs. Geschäftsgeheimnis nach GeschGehG vornehmen. Wer die Entscheidung in der Praxis trifft: gemäß Unternehmensrichtlinie / Mandatsprofil.

**✓ Hohe Erkennbarkeit:**
- Konsumentenprodukt mit sichtbaren Merkmalen
- Veröffentlichte API, Protokoll, SDK
- Physischer Mechanismus in verteiltem Produkt

#### Schirm 6: Strategischer Wert

Passt die Erfindung zur Schutzrechtsstrategie des Unternehmens? Prüfung anhand des Mandatsprofils:

- **Offensiv (Durchsetzungsportfolio):** Ist der Anspruch breit und assertionsfähig?
- **Defensiv (Freedom to Operate):** Schützt die Anmeldung eine relevante Technologie?
- **Lizenz-/Erlösmodell:** Ist die Erfindung lizenzierbar und wer würde zahlen?
- **Kerntechnologie vs. Peripherie:** Kern hat höheren Wert.
- **Wettbewerbslandschaft:** In patentintensiven Sektoren (Pharma, Halbleiter) frühzeitig anmelden.

### Schritt 3: Erfindungsprüfungsvermerk erstellen

Format:

> **Erfindungsprüfungsvermerk — [Titel der Erfindung]**
>
> **Ergebnis: [WEITERVERFOLGEN / KLÄREN / ABLEHNEN]**
>
> *[Ein Satz — Begründung im Klartext.]*
>
> ---
>
> ### Prüfungsergebnisse
>
> | Prüfschirm | Ergebnis | Anmerkung |
> |---|---|---|
> | Neuheitssignale | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Erfinderische Tätigkeit | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Technischer Charakter | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Vorveröffentlichung / Fristen | [✓ / 🟡 / 🔴] | [einzeiliger Grund + Daten] |
> | Erkennbarkeit | [✓ / 🟡 / 🔴] | [einzeiliger Grund] |
> | Strategischer Wert | [✓ / 🟡 / 🔴] | [Bezug zum Mandatsprofil] |
>
> ---
>
> ### Offene Punkte
>
> - [Frage / Klärungsbedarf]
>
> ### Nächste Schritte
>
> 1. **Patentrecherche beauftragen** — Suchanfrage für Patentanwalt mit Anspruchskonzepten, Erfindernamen, IPC-Klasse und bekannten Referenzen.
> 2. **Rückfrage an Erfinder** — Klärung offener Punkte zu [konkreten Punkten].
> 3. **An Patentanwalt übergeben** — bei Grenzfragen zum technischen Charakter oder zur Schutzstrategie.
> 4. **Ablehnen und Dankesschreiben** — Begründung archivieren.
> 5. **Geschäftsgeheimnis-Route** — Hinweis an zuständige Stelle gemäß GeschGehG.

### Schritt 4: Arbeitnehmererfindung — Pflichtprozess

Wenn der Erfinder Arbeitnehmer ist:

- **§ 5 ArbnErfG — Meldepflicht:** Erfinder hat unverzüglich zu melden. Form: schriftlich, Beschreibung der Erfindung, Entstehungsumstände.
- **§ 6 Abs. 1 ArbnErfG — Inanspruchnahmefrist:** Arbeitgeber hat **4 Monate** ab Eingang der Meldung, um unbeschränkt oder beschränkt in Anspruch zu nehmen. Frist läuft automatisch; Untätigkeit gilt als Freigabe.
- **§§ 9 ff. ArbnErfG — Vergütungspflicht:** Bei Inanspruchnahme entsteht Vergütungsanspruch. Bemessung nach den Richtlinien für die Vergütung von Arbeitnehmererfindungen im privaten Dienst (1959/zuletzt geändert). Faktoren: Erfindungswert, Anteilsfaktor, Mitarbeiterstellung.
- Frist im Vermerk dokumentieren und in das Fristenkontrollsystem des Mandanten eintragen.

## Ausgabeformat

Der Erfindungsprüfungsvermerk enthält: Titel, Ergebnis (WEITERVERFOLGEN / KLÄREN / ABLEHNEN), Prüftabelle, offene Punkte, nächste Schritte. Bei aktiver Mandatssache: Ausgabe in den Mandatsordner.

Kein internes Arbeitsnarrativ im Vermerk. Der Vermerk ist sofort verwendbar.

## Beispiel

**Eingabe:** „Neuer Cache-Algorithmus auf Basis eines erlernten Modells anstelle von LRU; im ersten Quartal dieses Jahres entwickelt, noch nicht veröffentlicht, Prototyp intern im Staging."

**Ergebnis (Beispiel):**

> **Erfindungsprüfungsvermerk — Lernbasierter Cache-Algorithmus**
>
> **Ergebnis: WEITERVERFOLGEN** — Neuheit und technischer Charakter sind prima facie gegeben; keine neuheitsschädliche Vorveröffentlichung erkennbar; strategische Relevanz in Abhängigkeit vom Mandatsprofil prüfen.
>
> | Prüfschirm | Ergebnis | Anmerkung |
> |---|---|---|
> | Neuheitssignale | 🟡 | Mechanismus neu, aber verwandte Literatur (ML-Caching) vorhanden — Recherche erforderlich |
> | Erfinderische Tätigkeit | 🟡 | Unerwarteter Effizienzgewinn behauptet — durch Recherche zu belegen |
> | Technischer Charakter | ✓ | Konkrete technische Verbesserung der Cache-Verwaltung |
> | Vorveröffentlichung | ✓ | Keine Offenbarung, intern und vertraulich |
> | Erkennbarkeit | 🟡 | Server-seitig: Abwägung Patent vs. Geschäftsgeheimnis empfohlen |
> | Strategischer Wert | 🟡 | Abhängig vom Mandatsprofil |

## Risiken und typische Fehler

- **Neuheitsschädliche Vorveröffentlichung übersehen:** Jede öffentliche Zugänglichmachung vor Anmeldetag zerstört die Patentierbarkeit weltweit (außer engen Ausnahmefällen). Eine Schonfrist für Vorveröffentlichungen gilt nicht.
- **ArbnErfG-Fristen versäumen:** Die 4-Monats-Inanspruchnahmefrist (§ 6 Abs. 1 ArbnErfG) läuft automatisch. Nicht im Fristenbuch eingetragen = Freigabe der Erfindung.
- **Patentierbarkeit bestätigen:** Die Skill trifft keine Patentierbarkeitsaussage. „Besteht die Erstprüfung" ist nicht „patentierbar".
- **Erkennbarkeitsfrage ignorieren:** Ein Patent auf eine nicht erkennbare Verletzungsform veröffentlicht das Know-how ohne Durchsetzungsmöglichkeit.
- **KI/Software-Erfindungen: technischen Charakter unterschätzen:** Der EPA bewertet technischen Charakter weit; nicht vorschnell ablehnen.

## Quellenpflicht

Jede Aussage zu Neuheit, erfinderischer Tätigkeit oder Vergütung muss auf konkreten Normen oder Entscheidungen beruhen. Pflichtquellen in jedem Vermerk:

- **Gesetzestext:** § 3, § 4, § 5 PatG; §§ 5, 6, 9 ff. ArbnErfG; Art. 52–56 EPÜ
- **Rechtsprechung:** mindestens eine BGH-Entscheidung zur Neuheit oder erfinderischen Tätigkeit
- **Kommentar:** Benkard PatG oder Bartenbach/Volz ArbnErfG mit § und Randnummer
- Alle Quellen mit Fundstelle zitieren. Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.
