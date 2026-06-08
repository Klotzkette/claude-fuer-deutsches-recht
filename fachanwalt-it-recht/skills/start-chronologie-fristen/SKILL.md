---
name: start-chronologie-fristen
description: "Start Chronologie Fristen im Plugin Fachanwalt It Recht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt IT Recht-Plugin, Chronologie und Belegmatrix im Plugin fachanwalt-it-recht, Fristen- und Risikoampel im Plugin fachanwalt-it-recht."
---

# Start Chronologie Fristen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt IT Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt IT Recht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein.

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
| `cyber-incident-response-72h` | Sofortmassnahmen bei aktivem Cyber-Vorfall Ransomware Datenexfiltration oder Insider-Threat. Anwendungsfall Cyberangriff ist entdeckt und IT-rechtliche Meldepflichten sowie Beweissicherung muessen binnen Stunden… |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für IT-, Datenschutz- und Telemedienrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und… |
| `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` | Cyber-Vorfall-Sofortmassnahmen Ransomware Datenleck Hack. Meldepflichten 72 Stunden Art. 33 DSGVO BSIG NIS2UmsuCG kritische Infrastruktur. Forensik Beweissicherung Chain-of-Custody Behörden Cybercrime.… |
| `fachanwalt-it-recht-datenschutz-folgenabschaetzung` | Datenschutz-Folgenabschaetzung DSFA nach Art. 35 DSGVO bei voraussichtlich hohem Risiko. Anwendungsfall neues Verarbeitungsverfahren mit hohem Risiko für Betroffene soll eingeführt werden. Normen Art. 35 DSGVO… |
| `fachanwalt-it-recht-it-vertrag-verhandlung-eu-odr` | IT-Vertragsverhandlung SaaS Cloud Lizenz mit Schlichtungsklauseln und EU-ODR-Optionen. Anwendungsfall IT-Vertrag soll verhandelt werden und Streitbeilegungsklauseln muessen aktuell gestaltet werden. Normen BGB §§ 305… |
| `fachanwalt-it-recht-ki-vo-hochrisiko-konformitaetsbewertung` | KI-VO-Konformitätsbewertung für Hochrisiko-KI-Systeme nach Art. 16-29 KI-VO 2024/1689. Anwendungsfall Unternehmen entwickelt oder setzt Hochrisiko-KI ein und benoetigt CE-Kennzeichnung und Konformitätserklarung. Normen… |
| `fachanwalt-it-recht-open-source-compliance-audit` | Open-Source-Software Compliance Audit für GPL LGPL MIT BSD Apache Copyleft und SBOM. Anwendungsfall Software-Produkt enthaelt Open-Source-Komponenten und Lizenzpflichten muessen vor Auslieferung geprüft werden. Normen… |
| `fachanwalt-it-recht-orientierung` | Orientierung im IT-Recht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will IT-Mandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung IT-Recht vor. Normen DSGVO BDSG TDDDG TKG NIS2UmsuCG… |
| `fachanwalt-it-recht-saas-vertrag-verhandlung` | SaaS-Vertragsverhandlung mit Datenschutz Verfuegbarkeit Vendor-Lock-in und Exit-Klausel. Anwendungsfall SaaS-Vertrag soll verhandelt oder geprüft werden und IT-rechtliche Pflicht-Klauseln muessen geprüft werden. Normen… |
| `fachanwalt-it-recht-software-mangel` | Prüfung von Softwaremangelansprüchen nach Kauf-Werk- oder Dienstvertragsrecht. Anwendungsfall Software funktioniert nicht wie vereinbart und Mandant will Nachbesserung Minderung Rücktritt oder Schadensersatz. Normen §§… |
| `fachanwalt-it-recht-vertragsstrafe-pruefen` | Vertragsstrafenklausel in IT-Vertraegen auf AGB-Wirksamkeit und Hoechstgrenzen prüfen. Anwendungsfall IT-Vertrag enthaelt Vertragsstrafenklausel und es stellt sich die Frage ob sie wirksam vereinbart ist. Normen § 339… |
| `mandat-triage-it-recht` | Strukturierte Eingangs-Abfrage für IT-rechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues IT-Rechtsmandat geht ein und muss schnell triagiert und dem richtigen zugeordnet werden. Normen Art. 33… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Unterlassungsklage Datenschutz, Klage IT-Vertrag, DSGVO-Bußgeldwiderspruch: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge,… |
| `softwarefehler-mangelhaftung-pruefen` | Strukturierte Prüfung bei mangelhafter Software mit Vertragstyp-Einordnung. Anwendungsfall Software versagt und Mandant braucht Einordnung ob Kauf- Werk- oder Dienstvertragsrecht gilt. Normen §§ 433 ff. BGB Kauf §§ 631… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für IT-, Datenschutz- und Telemedienrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## 2. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-it-recht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

### Chronologie und Belegmatrix

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

## 3. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-it-recht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

### Fristen- und Risikoampel

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

## IT-Recht-typische Fristen
- **Mängelrüge Handelsverkehr** § 377 HGB: unverzüglich nach Ablieferung; bei verdeckten Mängeln unverzüglich nach Entdeckung.
- **Verjährung Werkvertrag** § 634a BGB: 2 Jahre für Werke (Software), 5 Jahre bei Bauwerken — bei Software regelmäßig 2 Jahre ab Abnahme.
- **Verjährung Kaufrecht** § 438 BGB: 2 Jahre ab Übergabe.
- **DSGVO-Datenpanne** Art. 33: 72 Stunden.
- **NIS2-Meldung** § 32 BSIG (Umsetzung NIS2-RL): erhebliche Sicherheitsvorfälle binnen 24 Stunden Frühwarnung, 72 Stunden Initialbewertung, 1 Monat Abschlussbericht.
- **DSA Art. 16 Notice-and-Action**: ohne schuldhaftes Zögern.
- **Bußgeldrahmen DSGVO**: bis 20 Mio. EUR oder 4 %; **NIS2**: bis 10 Mio. EUR oder 2 % (wesentliche Einrichtungen), 7 Mio. EUR oder 1,4 % (wichtige Einrichtungen).

## Ampelkriterien
- **Rot**: Frist Art. 33 DSGVO läuft, NIS2-Vorfallmeldepflicht ausgelöst, AGB nicht UWG-konform und Abmahnung eingegangen, Mahnbescheid zugestellt.
- **Gelb**: SLA-Vereinbarung fehlt oder unklar, Vertragsstrafenklausel intransparent, fehlende AVV bei Auftragsverarbeitung.
- **Grün**: Vertrag SaaS-tauglich, AVV + TOM dokumentiert, SLA mit Service-Levels und Pönalen, Notfallprozesse vorhanden.

## 4. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-it-recht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

### Mandantenkommunikation

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

## Mandantenkommunikation IT-Recht
- **Anrede + Bezug:** "In Sachen [Mandant] / Ihre IT-rechtliche Frage"
- **Sachstand kurz:** Vertragstyp, Rollen, Streitstand bzw. Vertragsentwurf-Status.
- **Empfehlung:** zentral umsetzbarer nächster Schritt (z. B. "Verhandlung SLA-Pönalen, AVV nachverhandeln, Mängelmahnung mit Nachfrist setzen, AGB Inhaltskontrolle prüfen").
- **Risikoampel:** Vertrags-, AGB-, Haftungs-, DSGVO-, NIS2-Risiken konsolidiert.
- **Frist:** Mängelrüge § 377 HGB, Verjährung § 634a BGB, Datenpanne 72 Std., NIS2-Meldung 24h/72h/1 Monat.
- **Kostenhinweis:** RVG/Honorarvereinbarung; bei größeren Mandaten ggf. Vergütungsvereinbarung nach § 3a RVG.
- **Aufklärungspflicht:** bei Streit zwischen Vergleich und Klage erforderliche Risiko-/Kostenaufklärung (BGH Anwaltshaftung-Standard).

## Praxis-Tipp
Bei IT-Vertragsverhandlungen ist die Empfehlung "Klage" selten die beste Erstoption — die meisten Konflikte lösen sich durch fundierte Mängelrüge mit Nachfristsetzung (§§ 281, 323 BGB) bzw. AGB-Inhaltskontrolle ohne Klageverfahren. Das spart Zeit und schont Geschäftsbeziehung.

## 5. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-it-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

### Red-Team Qualitygate

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

## Red-Team-Prüfpunkte IT-Recht
1. **Vertragstyp:** Werkvertrag (§§ 631 ff.), Dienstvertrag (§§ 611 ff.), Kaufvertrag (§§ 433 ff.), Mietvertrag (§§ 535 ff.), Lizenzvertrag — wurde der Schwerpunkt richtig bestimmt?
2. **AGB-Kontrolle:** §§ 305 ff. BGB — Einbeziehung, Inhaltskontrolle, Klauselverbote §§ 307-309 BGB. Wurde bei B2C/B2B die richtige Inhaltskontrolle angewandt?
3. **DSGVO-Schnittstelle:** Liegt Auftragsverarbeitung (Art. 28) oder gemeinsame Verantwortlichkeit (Art. 26) vor? AVV vorhanden?
4. **Drittlandstransfer:** DPF / SCC / TIA korrekt geprüft?
5. **OSS-Compliance:** Copyleft-Effekt GPL bei Verbreitung beachtet? Lizenztexte korrekt eingebunden?
6. **NIS2 / KritisV:** Betroffenheit der eigenen oder Mandantorganisation als wesentliche/wichtige Einrichtung geprüft?
7. **Halluzinations-Check:** Keine erfundenen BGH-Az. oder EuGH-Rs.; juris/Beck-Online-Zitate nur mit verifizierbarer Quelle.

## Praxis-Tipp
Bei IT-Verträgen ist die häufigste Falle die formularmäßige Haftungsbeschränkung — z. B. "Haftung nur bei Vorsatz und grober Fahrlässigkeit". § 309 Nr. 7 BGB hält das in vielen Konstellationen nicht; AGB-Recht zwingt zur Berücksichtigung der gesetzlichen Mindesthaftung. Diese Klausel ist oft das erste Argument für eine Mandantforderung.

