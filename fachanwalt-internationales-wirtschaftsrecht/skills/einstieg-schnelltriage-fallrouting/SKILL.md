---
name: einstieg-schnelltriage-fallrouting
description: "Einstieg, Schnelltriage und Fallrouting im Fachanwalt Internationales Wirtschaftsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output a..."
---

# Einstieg, Schnelltriage und Fallrouting im Fachanwalt Internationales Wirtschaftsrecht-Plugin


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: FAO § 5 36 Monate Praxis, CISG Art. 39 angemessene Frist Mängelrüge, Brüssel Ia Art. 35 einstweiliger Rechtsschutz, NYÜ Art. V Anerkennung 3 Jahre.
- Tragende Normen verifizieren: FAO § 14r, Rom I (VO 593/2008), Rom II (VO 864/2007), Brüssel Ia (VO 1215/2012), CISG, UNCITRAL Model Law, INCOTERMS 2020, IPR-G, AWG, AWV, EU-Sanktionsverordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Internationale Vertragsparteien, ICC, UNCITRAL, Schiedsgericht (DIS, ICC, SCC), nationale Gerichte, Zoll, BAFA, BMWK, EuGH.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Internationaler Kaufvertrag, Schiedsklausel, ICC-Schiedsverfahren-Eingabe, Exportlizenz BAFA, Sanktionsprüfung, INCOTERMS-Klausel, Letter of Credit — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Internationales Wirtschaftsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Internationales Wirtschaftsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Internationales Wirtschaftsrecht. CISG Bruessel Ia Rom I Rom II Schiedsverfahren ICC UNCITRAL Investitionsschutz ICSID WTO EU-Aussenhandel LkSG. Schnittstelle Plugin kanzlei-allgemein.

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
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Internationales Wirtschafts- und Schiedsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und… |
| `fachanwalt-internationales-wirtschaftsrecht-cisg-pruefung` | Deutsches Unternehmen hat Streit mit ausländischem Handelspartner über Kaufvertrag und fragt: Gilt UN-Kaufrecht und welche Ansprüche bestehen? CISG UN-Kaufrecht. Prüfraster: Anwendungsbereich Art. 1-5 CISG Abbedingung… |
| `fachanwalt-internationales-wirtschaftsrecht-orientierung` | Einstieg in den Skill-Verbund Internationales Wirtschaftsrecht. FAO § 14i IWR CISG UN-Kaufrecht Bruessel-Ia-VO Rom I und II VO grenzüberschreitende Vertragspraxis Schiedsverfahren ICC UNCITRAL VIAC.… |
| `fachanwalt-internationales-wirtschaftsrecht-rom-i-anwendbarkeit` | Vertragsparteien aus verschiedenen Ländern streiten über Vertragsrecht und fragen: Nach welchem Recht wird der Vertrag beurteilt? VO (EG) 593/2008 Rom-I. Prüfraster: Rechtswahl Art. 3 objektive Anknuepfung Art. 4… |
| `fachanwalt-internationales-wirtschaftsrecht-schiedsklausel` | Mandant verhandelt internationalen Vertrag und fragt: Sollen wir eine Schiedsklausel aufnehmen und wie formulieren wir sie richtig? § 1031 ZPO Schiedsklausel. Prüfraster: Formvorschrift Art. II UN-Übereinkommen New… |
| `fachanwalt-iwr-brussels-ia-zuständigkeit` | Grenzüberschreitender Rechtsstreit: Gläubigerseite oder Beklagter fragt vor Klageerhebung welches EU-Gericht zuständig ist. VO 1215/2012 Bruessel-Ia. Prüfraster: allgemeiner Gerichtsstand Art. 4 Beklagter-Wohnsitz… |
| `fachanwalt-iwr-cisg-anwendbarkeit` | Unternehmen hat grenzüberschreitenden Warenkauf und fragt: Gilt UN-Kaufrecht automatisch oder können wir es ausschließen? CISG Anwendbarkeit Art. 1 CISG. Prüfraster: sachlicher Anwendungsbereich Warenkauf Art. 1… |
| `fachanwalt-iwr-embargo-pruefung-russland` | Sanktions-Prüfung EU-Russland-Sanktionen VO 833/2014 und VO 269/2014. Sektor-Sanktionen Personen-Sanktionen Eingefrorenes Vermögen § 7 AWG. BAFA-Genehmigung. Strafbarkeit § 18 AWG. Compliance-Check Workflow… |
| `fachanwalt-iwr-eu-us-dpf-data-privacy-framework` | EU-US Data Privacy Framework (DPF) seit 10.7.2023 als Angemessenheitsbeschluss (EU) 2023/1795 nach Schrems II Aufhebung. Folge für Standard Contractual Clauses SCC und Transfer Impact Assessment TIA.… |
| `fachanwalt-iwr-icc-uncitral-schiedsverfahren` | Mandant hat Schiedsklausel und will internationales Schiedsverfahren einleiten oder sich verteidigen. ICC UNCITRAL SIAC HKIAC Schiedsverfahren. Prüfraster: anwendbares Recht Sitz Schiedsgericht New Yorker Übereinkommen… |
| `gerichtsstand-und-rechtswahl-pruefen` | Gerichtsstand und Rechtswahl bei internationalen Handelsstreitigkeiten: Brüssel Ia VO 1215/2012 (Art. 25 Gerichtsstandsklausel, Art. 7 Erfüllungsort), Lugano-Übereinkommen 2007 (EFTA), Schiedsklausel-Wirksamkeit § 1029… |
| `mandat-triage-iwr` | Neues internationales Wirtschaftsrechtsmandat kommt rein und Anwalt klaert Sachgebiet und Sofort-Fristen. Eingangs-Triage IWR. Prüfraster: Mandantenrolle (Exporteur Importeur Investor) Geschäft (Warenkauf Investition… |
| `sanktions-compliance-pruefung` | Sanktions-Compliance: EU-Sanktionen (VO 269/2014 und 833/2014 Russland-Paket 1–14), US-OFAC SDN-Liste, UK-HMT/OFSI, UN-Sicherheitsrat-Resolutionen. Asset-Freeze, sektorale Embargos, Dienstleistungsverbote,… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage mit CISG-/EuGVVO-Bezug, Schiedsklage, Vollstreckung Auslandsurteil: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Internationales Wirtschafts- und Schiedsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.
