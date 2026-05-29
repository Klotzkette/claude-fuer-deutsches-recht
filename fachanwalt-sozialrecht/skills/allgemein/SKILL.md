---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Sozialrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Fachanwalt Sozialrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Sozialrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Sozialrecht nach FAO § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch § 84 SGG Klage § 87 SGG Eilantrag § 86b SGG. Buergergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Spezial-Skill aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
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
- **Primärer Pfad:** `skill-name` — [warum dieser Skill hilft]
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
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

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

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `akteneinsicht-anfordern` | Mandant oder Anwalt benoetigt Einsicht in die Verwaltungsakte oder Gerichtsakte in einem laufenden Sozialrechtsverfahren. § 25 SGB X Akteneinsicht Verwaltungsverfahren § 120 SGG gerichtliches Verfahren Art. 15 DSGVO… |
| `akteneinsicht-auswerten` | Anwalt hat Sozialrechts-Verwaltungs- oder Gerichtsakte erhalten und muss diese systematisch für Widerspruch oder Klage auswerten. § 25 SGB X § 120 SGG. Prüfraster: chronologische Sichtung Identifikation… |
| `anlagen-erstellen` | Anwalt muss Anlagenkonvolut zu Widerspruch Klage oder Schriftsatz in korrekter juristischer Konvention erstellen. Anlagenanhaenge Sozialrecht K1/W1/A1-Konvention. Prüfraster: Sigel Bezeichnung Quelle Datum Seitenzahl… |
| `bescheid-frist-quick-check` | 60-Sekunden-Sofortprüfung der Frist eines sozialrechtlichen Bescheids. Eingabe Datum der Bekanntgabe (Zugang) und Datum des Bescheids und Status der Rechtsbehelfsbelehrung. Berechnung Widerspruchsfrist § 84 SGG ein… |
| `bescheidanalyse` | Mandant hat Sozialleistungsbescheid erhalten und Anwalt muss dessen Inhalt rechtlich aufschluesseln. §§ 33 35 SGB X Form und Begründungspflicht § 24 SGB X Anhoerung. Prüfraster: Behoerde Aktenzeichen Bescheiddatum… |
| `eilantrag-sozialrecht` | Mandant ist auf Sozialleistung angewiesen die sofort wegfaellt oder verweigert wird (Buergergeld Wohnungslosigkeit Krankenversicherung). § 86b SGG Eilrechtsschutz. Prüfraster: Abs. 1 SGG aufschiebende Wirkung bei… |
| `eingliederungshilfe-schule` | Kind mit Behinderung benoetigt Schulbegleitung und Eltern oder Anwalt muessen Anspruch klaeren und durchsetzen. SGB IX Teil 2 §§ 90 ff. Eingliederungshilfe § 35a SGB VIII bei seelischer Behinderung. Prüfraster:… |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Sozialrecht (SGB I-XIV): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fachanwalt-sozialrecht-erwerbsminderungsrente` | Versicherter erhielt Ablehnung der Erwerbsminderungsrente oder ist ausgesteuert und fragt nach Rentenanspruch. §§ 43 240 SGB VI. Prüfraster: volle Erwerbsminderung unter 3 Stunden taeglich teilweise unter 6 Stunden… |
| `fachanwalt-sozialrecht-eu-rente-antrag` | Versicherter mit Beschaeftigungszeiten im EU-Ausland fragt nach Rente und wie die auslaendischen Zeiten angerechnet werden. VO (EG) 883/2004 Sozialversicherungskoordinierung. Prüfraster: Antragstellung im Wohnsitzland… |
| `fachanwalt-sozialrecht-gdb-schwerbehinderung` | Mandant hat Behinderung und moechte Schwerbehindertenausweis und Merkzeichen beantragen oder Ablehnungsbescheid anfechten. § 152 SGB IX Feststellungsverfahren Versorgungsmedizin-Verordnung. Prüfraster: GdB-Feststellung… |
| `fachanwalt-sozialrecht-krankengeld-aussteuerung` | Mandant war langzeitkrank und Krankengeld laeuft nach 78 Wochen aus oder ist ausgelaufen und fragt nach Anschlusssicherung. § 44 SGB V Krankengeld Bezugsdauer 78 Wochen innerhalb 3 Jahren. Prüfraster: Anschluss ALG I §… |
| `fachanwalt-sozialrecht-long-covid-bk-anerkennung-bg` | Pflegekraft Arzt Lehrer oder Kassierer hat Long-COVID und fragt ob Berufserkrankungsanerkennung bei der Berufsgenossenschaft möglich ist. § 9 SGB VII BK-Liste Anlage 1 BKV insbesondere BK 3101 Infektionskrankheiten… |
| `fachanwalt-sozialrecht-orientierung` | Einstieg in den Skill-Verbund Sozialrecht. Orientierung im Sozialrecht Fachanwaltschaft nach § 14 FAO Weiterbildungspflicht. SGB I bis XIV im Überblick SGB II Buergergeld SGB VI Rente SGB V Krankenversicherung SGB IX… |
| `fachanwalt-sozialrecht-sgb-ii-bescheid` | Mandant erhielt Buergergeld-Bescheid mit zu niedrigem Betrag Sanktion oder Aufhebungs-Rückforderungsbescheid. SGB II Buergergeld. Prüfraster: Bedarfsberechnung Regelbedarf § 20 Mehrbedarfe § 21 Kosten der Unterkunft §… |
| `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` | Vergleich vor Sozialgericht § 101 SGG. Widerspruchsverhandlung Behoerde § 84 SGG. Mediation in Sozialleistungs-Streit zunehmend. Anhoerung GdB-Verfahren Vergleich Schwerbehinderung. Workflow Korrespondenz Behoerde… |
| `fachanwalt-sozialrecht-widerspruch-sozialleistung` | Mandant hat Sozialleistungsbescheid erhalten und Anwalt formuliert Widerspruch. § 84 SGG Widerspruchsfrist ein Monat. Prüfraster: Frist (Bekanntgabe Vier-Tage-Fiktion § 37 Abs. 2 SGB X seit 1.1.2025 PostModG)… |
| `fristenbuch-sozialrecht` | Anwalt oder Sekretariat muss Fristen in Sozialrechtsverfahren erfassen und ueberwachen. Fristenbuch Sozialrecht. Standardfristen: § 84 SGG Widerspruch 1 Monat § 87 SGG Klage 1 Monat § 173 SGG Beschwerde 1 Monat… |
| `hilfsmittelantrag-pruefen` | Mandant benoetigt Hilfsmittel (Rollstuhl Hoerhilfe Prothese Pflegebett Treppenlift) und fragt welcher Kostentraeger zuständig ist und wie Antrag und Widerspruch aussehen. § 33 SGB V Hilfsmittelverzeichnis § 139 SGB V §… |
| `klage-sozialgericht` | Nach negativem Widerspruchsbescheid muss Klage zum Sozialgericht erhoben werden. §§ 87 ff. SGG Klagefrist. Prüfraster: Klagefrist 1 Monat nach Widerspruchsbescheid § 87 Abs. 1 SGG kein Anwaltszwang vor SG… |
| `mandanten-intake` | Erstgespräch oder Telefon-Intake in einer Sozialrechtskanzlei — Stammdaten Mandant erfassen Fristen identifizieren und Akte anlegen. Sozialrechtliches Mandats-Intake. Prüfraster: Geburtsdatum Versichertennummer… |
| `mandantenbrief-leichte-sprache` | Erklärung eines sozialrechtlichen Bescheids für den Mandanten in einfacher oder leichter Sprache. Drei Stufen Standardbrief (B1) Einfache Sprache (A2 nach GER) Leichte Sprache (Regeln Netzwerk Leichte Sprache und DIN… |
| `mandat-triage-sozialrecht` | Neues sozialrechtliches Mandat: Sekretariat oder Anwalt muss Sachgebiet klaeren und zum richtigen Skill weiterleiten. Eingangs-Triage Sozialrecht SGB I-XIV. Prüfraster: Sachgebiet (SGB II Buergergeld SGB V… |
| `pflegegrad-widerspruch` | Mandant erhielt zu niedrigen Pflegegrad oder Pflegekasse verweigert Pflegegrad. Widerspruch gegen Pflegegrad-Bescheid nach SGB XI. Prüfraster: sechs Module § 15 SGB XI Mobilitaet Kognition Verhalten Selbstversorgung… |
| `pkh-erfolgsaussicht-pruefen` | Mittellose Mandanten benoetigen Prozesskostenhilfe für sozialgerichtliche Klage. PKH-Erfolgsaussichtsprüfung Sozialrecht. Prüfraster: wirtschaftliche Voraussetzungen Einkommen Vermögen Selbstbehalt Schonvermögen § 90… |
| `prozesskostenhilfe-antrag` | Anwalt erstellt PKH-Antrag für Sozialgerichtsverfahren und muss alle Belege korrekt zusammenstellen. § 73a SGG iVm §§ 114 ff. ZPO. Prüfraster: Erklärung persoenliche und wirtschaftliche Verhältnisse Formular ZP1a… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Widerspruch + SG-Klage, Eilantrag § 86b SGG, Überprüfungsantrag § 44 SGB X: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge,… |
| `schulung-fallbesprechung` | Strukturierte Fallbesprechung für Schulung Inhouse-Fortbildung Referendariats-AG oder Prüfungs-Vorbereitung Fachanwalt Sozialrecht. Nimmt eine bestehende Akte (Bescheid plus medizinische Unterlagen plus… |
| `sozialrecht-fallaufnahme-routing` | Master-Routing-Skill der sozialrechtlichen Kanzlei. Nimmt einen frischen Fall an und entscheidet in drei Schritten welche weiteren Skills wann gezogen werden. Schritt 1 Fristlage (bescheid-frist-quick-check) Schritt 2… |
| `sozialrecht-kanzlei-kaltstart-interview` | Kaltstart-Interview für die sozialrechtliche Kanzlei. Erfragt Schwerpunktbereiche (Buergergeld SGB II / SGB IX Schwerbehinderung / SGB V Krankenversicherung / SGB XI Pflege / Asylbewerberleistungsgesetz) zuständige… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Sozialrecht (SGB I-XIV): ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |
| `widerspruchsfrist-und-zustellung-sgb` | Anwalt muss bei eingehendem oder ausgehendem Bescheid klaeren ob und wann die Widerspruchsfrist laeuft und ob Zustellungsmaengel die Frist beeinflussen. § 37 SGB X Zustellung und Bekanntgabe-Fiktion. Prüfraster:… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Spezial-Skills aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.
