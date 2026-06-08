---
name: fa-gewerblicher-rs-gr-abmahnung-portfolio
description: "FA Gewerblicher RS GR Abmahnung Portfolio im Plugin Fachanwalt Gewerblicher Rechtsschutz: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt Gewerblicher, Abmahnung im gewerblichen Rechtsschutz, Schutzrechtsportfolio-Pflege."
---

# FA Gewerblicher RS GR Abmahnung Portfolio

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Gewerblicher Rechtsschutz-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Gewerblicher Rechtsschutz**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezuege. Markenanmeldung DPMA EUIPO. UWG-Abmahnung §§ 8 ff. UWG. Designverletzung. Einstweilige Verfuegung Verletzungsklage Lizenzanaloger Schadensersatz.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `erstgespraech-mandatsannahme` | Erstgespraech im gewerblichen Rechtsschutz strukturieren und Mandat aufnehmen. § 14 MarkenG § 139 PatG § 8 UWG § 43a BRAO. Prüfraster: Schutzrecht Verletzungshandlung Parteistellung Eilbedürfnis Fristen. Output:… |
| `fachanwalt-gewerblicher-rechtsschutz-abmahnung-uwg` | UWG-Abmahnung prüfen versenden oder auf Eingang reagieren. § 8 UWG Unterlassungsanspruch §§ 3 4 5 UWG Verbotsgrunde §§ 12 13 UWG Durchsetzung. Prüfraster: Verletzungshandlung Abmahnberechtigung Fristen UE… |
| `fachanwalt-gewerblicher-rechtsschutz-abmahnung-vergleich-wipo` | Abmahnung oder Vergleich bei Domainnamen-Streit und WIPO-Schiedsverfahren vorbereiten. UDRP WIPO-Schiedsregeln § 14 MarkenG Markenrecht. Prüfraster: Domain-Name Verwechslungsgefahr Boese-Glauben-Registrierung… |
| `fachanwalt-gewerblicher-rechtsschutz-designverletzung` | Geschmacksmuster- oder Designverletzung prüfen und Ansprüche durchsetzen oder abwehren. §§ 1 2 38 GeschmMG §§ 11 ff. GeschmMG Verletzungsansprüche EU-Geschmacksmuster-VO. Prüfraster: Schutzfähigkeit Neuheit Eigenart… |
| `fachanwalt-gewerblicher-rechtsschutz-marken-widerspruch` | Widerspruch gegen Markenanmeldung beim DPMA oder EUIPO einlegen oder abwehren. §§ 42 43 MarkenG Widerspruchsverfahren Art. 46 EUTMR. Prüfraster: Widerspruchsfrist Widerspruchsmarke Verwechslungsgefahr… |
| `fachanwalt-gewerblicher-rechtsschutz-markenanmeldung` | Markenanmeldung beim DPMA oder EUIPO vorbereiten und stratgisch gestalten. §§ 3 7 8 9 MarkenG Schutzvoraussetzungen Art. 4 7 EUTMR. Prüfraster: Markenfähigkeit absolute Schutzhindernisse Waren- und… |
| `fachanwalt-gewerblicher-rechtsschutz-orientierung` | Gewerblichen Rechtsschutz-Mandat einordnen und Bearbeitungsroute bestimmen. § 14 MarkenG § 139 PatG § 8 UWG GeschmMG UWG. Prüfraster: Schutzrecht Verletzungsart Parteistellung Route Fristen Eilbedürfnis. Output:… |
| `fachanwalt-gewerblicher-rechtsschutz-patent-nichtigkeitsklage` | Patentnichtigkeitsklage beim BPatG vorbereiten oder Verteidigung des Patents gegen Nichtigkeitsangriff. §§ 81 ff. PatG Nichtigkeitsverfahren § 22 PatG Nichtigkeitsgründe. Prüfraster: Nichtigkeitsgrund Stand der Technik… |
| `fachanwalt-gewerblicher-rechtsschutz-uwg-einstweilige-verfuegung` | Einstweilige Verfuegung im UWG-Verfahren beantragen oder abwehren bei dringenden Wettbewerbs- oder Markenrechtsverletzungen. §§ 935 940 ZPO §§ 8 12 UWG § 14 MarkenG. Prüfraster: Verfuegungsanspruch Verfuegungsgrund… |
| `fachanwalt-gewrechts-geschgehg-kollisionen-nda-hinschg-urhg` | Kollisionen zwischen gewerblichem Rechtsschutz NDA-Recht HinSchG und Urheberrecht prüfen wenn mehrere Schutzrechtsregime sich ueberschneiden. §§ 1 ff. GeschmMG § 14 MarkenG §§ 1 ff. HinSchG §§ 97 ff. UrhG. Prüfraster:… |
| `fachanwalt-gewrechts-ki-vo-50-genai` | KI-generierte Inhalte auf gewerblichen Rechtsschutz prüfen wenn GenAI-Outputs Schutzrechte beruehren. Art. 50 KI-VO Transparenzpflichten §§ 2 7 UrhG KI-Autorschaft. Prüfraster: Urheberrechtsschutz KI-Autorschaft… |
| `schriftsatzkern-substantiierung` | Klage oder Antrag im gewerblichen Rechtsschutz substantiiert ausformulieren. § 14 MarkenG § 139 PatG § 8 UWG §§ 253 286 ZPO. Prüfraster: Anspruchsgrundlage Sachverhalt Beweisangebot Streitwert Antrag. Output:… |
| `vergleichsverhandlung-strategie` | Streit im gewerblichen Rechtsschutz durch Vergleich lösen und Verhandlungsstrategie entwickeln. § 14 MarkenG § 139 PatG § 8 UWG § 779 BGB Vergleich. Prüfraster: Vergleichsziele BATNA Streitwert Kosten… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## 2. `gr-abmahnung-workflow`

**Fokus:** Abmahnung im gewerblichen Rechtsschutz: Berechtigung, Vollmacht, konkrete Verletzungsform, Anspruch, Frist, Unterlassungserklärung modifiziert annehmen. Prüfraster für Markenrecht, Patentrecht, Designrecht, UWG und UrhG. Mustertexte.

### GR: Abmahnung-Workflow

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 14 Abs. 6 MarkenG | Unterlassungs- und Schadensersatzanspruch bei Markenverletzung |
| § 9 PatG | Ausschließliches Benutzungsrecht; Verletzungsansprüche § 139 PatG |
| § 42 DesignG | Unterlassung und Schadensersatz bei Designverletzung |
| § 97 UrhG | Unterlassung und Schadensersatz bei Urheberrechtsverletzung |
| § 97a UrhG | Abmahnung: Form, Inhalt, Kostenerstattung |
| § 8 UWG | Unterlassungsanspruch bei unlauterem Wettbewerb |
| § 13 Abs. 2 UWG | Formerfordernisse der Abmahnung |
| § 13 Abs. 3 UWG | Kostenerstattung bei berechtigter Abmahnung |
| § 8c UWG | Rechtsmissbräuchliche Abmahnung: Ausschluss Kostenerstattung |

## Prüfschema vor der Abmahnung

**Schritt 1 – Aktivlegitimation**

| Schutzrecht | Aktivlegitimierter |
|---|---|
| Marke | Eingetragener Inhaber (§ 14 MarkenG), ausschließlicher Lizenznehmer (wenn ermächtigt) |
| Patent | Patentinhaber (§ 139 PatG), ausschließlicher Lizenznehmer |
| Design | Eingetragener Inhaber (§ 42 DesignG) |
| Urheberrecht | Urheber (§ 7 UrhG), Werknutzungsberechtigter (§ 31 UrhG) |
| UWG | Mitbewerber (§ 8 Abs. 3 Nr. 1 UWG), qualifizierter Verband (§ 8 Abs. 3 Nr. 2 UWG) |

**Schritt 2 – Verletzungshandlung konkret benennen**
- Exakte Beschreibung: Welches Schutzrecht, welche Handlung, wann, wo, wie?
- Beweissicherung: Screenshots mit Zeitstempel, Testkauf mit Quittung, eidesstattliche Versicherung.

**Schritt 3 – Fristdauer**
- Regelmäßig: **2–3 Werktage** bei UWG-Eilsachen (wenn eV-Antrag droht).
- **1–2 Wochen** bei Patent-/Marken-/Design-Abmahnungen ohne akute Dringlichkeit.
- Längere Frist: bei komplexen technischen Sachverhalten sinnvoll.

**Schritt 4 – Unterlassungserklärung (UE)**
- Anforderungen: strafbewehrt, unbefristet, ausreichend weit formuliert.
- Vertragsstrafe: Hamburger Brauch (Angemessenheitsvorbehalt) vs. fester Betrag.
- Modifizierte UE: Annahme nur wenn abgegebene UE die Wiederholungsgefahr beseitigt.

## Muster-Abmahnung (Gerüst)

```
[Briefkopf Kanzlei] [Ort, Datum]

An [Verletzer / Anwalt der Gegenseite] - Per E-Mail + Einschreiben -

Abmahnung wegen Verletzung von [Schutzrecht]
Unsere Mandantin: [Name]

Sehr geehrte Damen und Herren,

wir zeigen die Vertretung der [Mandantin] an (Vollmacht Anlage 1).

I. Schutzrecht unserer Mandantin
[Beschreibung des Schutzrechts, Reg.-Nr., Anmeldetag, Schutzbereich]
(Anlage 2: Registerauszug)

II. Verletzungshandlung
Am [Datum] haben Sie auf / in [Plattform / Medium] folgende Handlung vorgenommen:
[konkrete Beschreibung] (Anlage 3: Screenshot / Testkauf).

III. Ansprüche
Die oben beschriebene Handlung verletzt [Schutzrecht] und berechtigt unsere
Mandantin zur Geltendmachung von Unterlassung, Auskunft und Schadensersatz.

IV. Aufforderung
Wir fordern Sie auf, bis zum [Datum, Frist] die beigefügte strafbewehrte
Unterlassungserklärung (Anlage 4) zu unterzeichnen und uns zuzusenden.

V. Kosten
Die Kosten dieser Abmahnung betragen [Betrag] €. Wir erwarten Zahlung bis [Datum].

Ohne fristgerechte Reaktion werden wir einstweilige Verfügung beantragen.

[Unterschrift]
```

## Reaktion auf eingehende Abmahnung

| Reaktion | Wann sinnvoll | Risiko |
|---|---|---|
| Vollständige UE unterzeichnen | Verletzung eindeutig; schnelle Lösung | Anerkenntnis der Verletzung |
| Modifizierte UE | Formulierung zu weit; Sachverhalt klärungsbedürftig | Wiederholungsgefahr bleibt ggf. |
| Keine Reaktion / Ablehnung | Abmahnung unbegründet; Missbrauch § 8c UWG | EV-Antrag der Gegenseite |
| Negative Feststellungsklage | Zur Perpetuierung der Gerichtszuständigkeit | Kostentragung bei Verlust |
| Schutzschrift ZSSR | Vorbeugende Schutzschrift ([zssr.de](https://www.zssr.de)) | Kein Rechtsmittel, nur Prävention |

## Kostenpositionen

| Position | Grundlage | Streitwert-Beispiel 50.000 € |
|---|---|---|
| Geschäftsgebühr 1,3 | RVG VV Nr. 2300 | 1.641 € |
| Auslagenpauschale | RVG VV Nr. 7002 | 20 € |
| USt. 19 % | UStG | 311,79 € |
| Gesamt | | 1.972,79 € |

## Einstieg
1. Welches Schutzrecht und welche Verletzungshandlung liegen vor?
2. Wer ist aktivlegitimiert (Markeninhaber / Lizenznehmer / UWG-Mitbewerber)?
3. Liegt eine eingehende Abmahnung vor, oder soll eine ausgehende vorbereitet werden?
4. Welche Fristen laufen (Dringlichkeit, Verjährung)?
5. Output: Abmahnungsentwurf, UE-Entwurf, Reaktionsmemo, Schutzschriften-Auftrag?

## Plugin-Kontext
Skill gehört zu `fachanwalt-gewerblicher-rechtsschutz`. Anschluss-Skills: `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung`, `spezial-verfuegung-beweislast-und-darlegungslast`, `workflow-fristen-und-risikoampel`.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für vollständige Mandantenberatung.
- Keine eigenständige Schutzrechts-Prüfung ohne Registerauszug.
- Keine Bewertung nicht belegter Verletzungshandlungen.

## 3. `gr-portfolio-pflege-workflow`

**Fokus:** Schutzrechtsportfolio-Pflege: Jahresgebühren-Fristenplan, Verlängerungsfristen Marke/Patent/Design/Gebrauchsmuster, Löschungsrisiken, DPMA-Statusabfrage, Portfolioaudit, Kostenoptimierung und strategische Aufgabe von Schutzrechten.

### Schutzrechtsportfolio-Pflege

## Fristenübersicht nach Schutzrechtstyp

### Markenrecht

| Schutzrecht | Schutzfrist | Verlängerungsfrist | Gebühr |
|---|---|---|---|
| Deutsche Marke (DPMA) | 10 Jahre ab Anmeldetag | Vor Ablauf (6 Monate Nachfrist + Zuschlag) | [dpma.de/dpma/gebuehren](https://www.dpma.de/dpma/gebuehren/index.html) |
| Unionsmarke (EUIPO) | 10 Jahre ab Anmeldetag | Vor Ablauf (6 Monate Nachfrist) | [euipo.europa.eu/fees](https://euipo.europa.eu/ohimportal/en/fees-and-payments) |
| IR-Marke (WIPO) | 10 Jahre ab Registrierung | Verlängerung bei WIPO (zentral) | [wipo.int/madrid/fees](https://www.wipo.int/madrid/en/fees/) |

**Benutzungspflicht:** Deutsche Marke: ernsthafte Benutzung innerhalb von 5 Jahren nach Eintragung (§ 26 MarkenG); Nichtbenutzung = Verfallsrisiko (§ 49 MarkenG).

### Patentrecht

| Schutzrecht | Laufzeit | Jahresgebühren | Fristbeginn |
|---|---|---|---|
| Deutsches Patent | Max. 20 Jahre ab Anmeldetag | Ab 3. Jahr (PatG § 17) | Anmeldetag |
| EP-Patent (EPÜ) | Max. 20 Jahre | Nationaler Jahresbeitrag je Validierungsland | Anmeldetag |
| Einheitspatent (UPC) | Max. 20 Jahre | Einheitliche Jahresgebühr beim EPA | Erteilungstag |
| Gebrauchsmuster (DE) | 3 Jahre, verlängerbar bis 10 Jahre | Verlängerungsgebühr je Periode | Anmeldetag |

### Designrecht

| Schutzrecht | Laufzeit | Verlängerung |
|---|---|---|
| Deutsches Design (DPMA) | 5 Jahre, bis 25 Jahre verlängerbar | Verlängerungsgebühr vor Ablauf (§ 27 DesignG) |
| Eingetragenes GGM (EUIPO) | 5 Jahre, bis 25 Jahre verlängerbar | Verlängerungsgebühr bei EUIPO |
| Nicht eingetragenes GGM | 3 Jahre ab Offenbarung, nicht verlängerbar | – |

## Portfolioaudit-Matrix

| Schutzrecht | Status (aktiv/abgelaufen) | Nächste Frist | Priorität | Strategie |
|---|---|---|---|---|
| Marke [Name] DPMA | | | | Verlängern / Aufgeben |
| Patent [Nr.] EPA | | | | Jahresgebühr zahlen / Fallenlassen |
| Design [Nr.] EUIPO | | | | Verlängern / Aufgeben |
| Gebrauchsmuster [Nr.] | | | | Verlängern / Ablaufen lassen |

## Strategische Entscheidungen im Portfolio

**Beibehaltung sinnvoll wenn:**
- Aktive Benutzung des Schutzrechts (Marke) oder laufende Entwicklung / Produktion.
- Wettbewerber in der Branche präsent; Schutzrecht als Abwehrmittel wertvoll.
- Lizenzeinnahmen oder Lizenzierungspotenzial.

**Aufgabe / Nichtfortsetzung sinnvoll wenn:**
- Kein wirtschaftliches Interesse mehr.
- Kerngeschäft hat sich verschoben.
- Jährliche Gebühren übersteigen wirtschaftlichen Nutzen.
- Schutzrecht hat Nichtigkeitsrisiko (unklare Schutzfähigkeit).

**Teilweise Aufgabe:**
- Einschränkung des Waren-/Dienstleistungsverzeichnisses (Beschränkungsantrag DPMA/EUIPO).
- Rückgabe einzelner Patentansprüche.
- Nationale Phase eines PCT-Patents nur in Schlüsselmärkten weiterverfolgen.

## Fristen-Checkliste (laufend)

| Schutzrecht | Ablaufdatum | Verlängerungsfrist | Gebühr gezahlt? | Zuständig |
|---|---|---|---|---|
| | | | ☐ | |
| | | | ☐ | |

## DPMA-Statusabfrage

- Markenregister: [dpma.de/marken/markenrecherche](https://www.dpma.de/marken/markenrecherche/)
- Patentregister: [dpma.de/patente/patentsuche](https://www.dpma.de/patente/patentsuche/)
- Designregister: [dpma.de/designs/designrecherche](https://www.dpma.de/designs/designrecherche/)
- Unionsmarken: [euipo.europa.eu/eSearch](https://euipo.europa.eu/eSearch/)
- EP-Patente: [epo.org/en/searching-for-patents/technical/espacenet](https://www.epo.org/en/searching-for-patents/technical/espacenet)

## Kostenoptimierung

| Maßnahme | Einsparpotenzial |
|---|---|
| Gebührenreduktion durch Bündelung (Verlängerung mehrerer Schutzrechte gleichzeitig) | Gering |
| Aufgabe nicht mehr genutzter Schutzrechte | Mittel–Hoch |
| Nationalphasen-Selektion bei PCT-Patenten | Hoch |
| Gebrauchsmuster statt Patent (kürzer, billiger) bei kurzlebigen Produkten | Mittel |
| Portfolioverkauf / Lizenzierung statt Pflege | Fallabhängig |

## Einstieg
1. Welche Schutzrechte sollen geprüft werden (Typ, Nummer, Inhaber)?
2. Sind Verlängerungsfristen bekannt oder sollen sie recherchiert werden?
3. Besteht ein konkreter Anlass (drohender Verfall, Budgetentscheidung)?
4. Soll eine Priorisierungsmatrix oder ein Fristenplan erstellt werden?
5. Output: Portfolioaudit-Tabelle, Fristenplan, Kostenschätzung, Strategiememo?

## Plugin-Kontext
Anschluss-Skills: `spezial-markenanmeldung-compliance-dokumentation-und-akte`, `spezial-rechtsschutz-fristen-form-und-zuständigkeit`, `workflow-fristen-und-risikoampel`.

## Was dieser Arbeitsgang nicht macht
- Keine vollständige Fristenberechnung ohne Kenntnis aller konkreten Anmeldedaten.
- Kein Ersatz für vollständige Mandantenberatung und laufende Fristenüberwachung.

