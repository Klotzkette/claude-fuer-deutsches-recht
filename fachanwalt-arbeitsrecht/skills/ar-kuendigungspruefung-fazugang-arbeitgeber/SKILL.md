---
name: ar-kuendigungspruefung-fazugang-arbeitgeber
description: "AR Kuendigungspruefung Fazugang Arbeitgeber im Plugin Fachanwalt Arbeitsrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Kündigungsprüfung, Arbeitgeber-Zustellworkflow. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# AR Kuendigungspruefung Fazugang Arbeitgeber

## Arbeitsbereich

**AR Kuendigungspruefung Fazugang Arbeitgeber** ordnet den Fall über die tragenden Prüfungslinien: Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Kündigungsprüfung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Arbeitsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `ar-kuendigungspruefung-workflow` | Kündigungsprüfung: Schritt-für-Schritt vom Zugang der Kündigung bis zur Klageerhebung oder Vergleichsstrategie. Schriftform § 623 BGB, KSchG-Anwendbarkeit § 23, Betriebsratsanhörung § 102 BetrVG, Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz, Massenentlassung § 17 KSchG. |
| `fazugang-neu-006-arbeitgeber-zustellworkflow-rechtssicher-organi` | Arbeitgeber-Zustellworkflow: rechtssichere Organisation der Kündigungszustellung, Parallelwege (Bote + Einschreiben + Gerichtsvollzieher), Checklisten, Kuvertierungsprotokoll, Risikomanagement bei mehreren Empfängern (Massenentlassung). |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Arbeitsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

# Fachanwalt Arbeitsrecht — Allgemein

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt Arbeitsrecht — Allgemein` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Arbeitsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Arbeitsrecht nach FAO Paragraf 10. Aktuelle BAG-Rechtsprechung 2025/2026 (Equal Pay Paarvergleich AGG, kein Verzicht Mindesturlaub BUrlG, Freistellungsklausel unwirksam Paragraf 307 BGB). KSchG Kündigungsschutzklage. BetrVG. TzBfG. AGG. EntgTranspG.

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
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und… |
| `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` | Aufhebungsvertrag mit Sperrzeit-Vermeidung nach § 159 SGB III bei Eigeninitiative oder drohender Kündigung. Anwendungsfall Arbeitgeber und Arbeitnehmer wollen Arbeitsverhältnis auflösen ohne Sperrzeit für… |
| `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich` | Anwaltsperspektive zu BAG 23.10.2025 - 8 AZR 300/24 (Paarvergleich Equal Pay): für Klage auf Differenzentgelt; Beweislastumkehr nach § 22 AGG durch Paarvergleich mit einem einzelnen Vergleichskollegen. |
| `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht` | Anwaltsperspektive zu BAG 03.06.2025 - 9 AZR 104/24 (kein Urlaubsverzicht durch Prozessvergleich): Vergleichsformulierung zur Trennung von Mindesturlaub und Mehrurlaub. |
| `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` | Anwaltsperspektive zu BAG 25.03.2026 - 5 AZR 108/25 (Freistellungsklausel unwirksam): Beschaeftigungsanspruch durchsetzen, Annahmeverzug sichern, AGB-Kontrolle. |
| `fachanwalt-arbeitsrecht-befristung-tzbfg` | Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer. Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befristungsvertrag gestaltet werden. Normen § 14 TzBfG… |
| `fachanwalt-arbeitsrecht-bem-verfahren` | Betriebliches Eingliederungsmanagement BEM nach § 167 Abs. 2 SGB IX als Voraussetzung wirksamer personenbedingter Kündigung. Anwendungsfall Arbeitnehmer war laenger als sechs Wochen krank und Arbeitgeber will… |
| `fachanwalt-arbeitsrecht-betriebsratsanhoerung` | Betriebsratsanhoerung nach § 102 BetrVG vor jeder Kündigung. Anwendungsfall Kündigung soll ausgesprochen werden und BR-Anhörung muss korrekt durchgeführt werden. Normen § 102 BetrVG Anhörungs- und Widerspruchsrecht §… |
| `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung` | Anwaltsperspektive bei Betriebsratsbeschluss-Maengeln: Mandatsannahme durch den Betriebsrat, Prüfung der ordnungsgemäßen Beschlussfassung (§ 25 Abs. 2, § 29 Abs. 2 BetrVG), strategisches Vorgehen bei festgestelltem… |
| `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` | Verteidigung von Hinweisgebern nach HinSchG gegen Repressalien durch Arbeitgeber. Anwendungsfall Arbeitnehmer hat intern oder extern Hinweis gegeben und wurde daraufhin gekündigt versetzt oder gemobbt. Normen §§ 35-37… |
| `fachanwalt-arbeitsrecht-kuendigungsschutzklage` | Kündigungsschutzklage nach § 4 KSchG mit Drei-Wochen-Frist ab Zugang der schriftlichen Kündigung. Anwendungsfall Arbeitnehmer erhaelt Kündigung und will Klage erheben oder Arbeitgeber prüft Kündigungsrisiko. Normen § 4… |
| `fachanwalt-arbeitsrecht-massenentlassung-17-kschg` | Massenentlassung mit Anzeigepflicht nach § 17 KSchG und Konsultationspflicht des Betriebsrats. Anwendungsfall Unternehmen plant Stellenabbau mit Schwellenwerten 5/25/30 Beschaeftigte. Normen § 17 KSchG Anzeige… |
| `fachanwalt-arbeitsrecht-orientierung` | Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO. Anwendungsfall Kanzlei will Arbeitsrechtsmandat beurteilen oder Anwalt bereitet sich auf… |
| `fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg` | Gueteverhandlung im Arbeitsgerichtsverfahren nach § 54 ArbGG mit Auflösungsantrag und Abfindungsstrategie. Anwendungsfall Guetetermin steht an und Vergleich oder Auflösungsantrag soll vorbereitet werden. Normen § 54… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Kündigungsschutzklage, Befristungskontrollklage, Zahlungsklage Arbeitsgericht: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge,… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Individual- und kollektives Arbeitsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `ar-kuendigungspruefung-workflow`

**Fokus:** Kündigungsprüfung: Schritt-für-Schritt vom Zugang der Kündigung bis zur Klageerhebung oder Vergleichsstrategie. Schriftform § 623 BGB, KSchG-Anwendbarkeit § 23, Betriebsratsanhörung § 102 BetrVG, Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz, Massenentlassung § 17 KSchG.

# AR: Kündigungsprüfung — Workflow

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AR: Kündigungsprüfung — Workflow` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Strukturierter Arbeitsablauf zur vollständigen Prüfung einer Kündigung — von der Erstmeldung des Mandanten bis zum klaren Handlungsvorschlag. Kritischer Zeitdruck: Die Drei-Wochen-Frist nach § 4 KSchG läuft ab Zugang der Kündigung.

## Kaltstart — Sofortmaßnahmen
Bei Eingang einer Kündigung gelten folgende Prioritäten in dieser Reihenfolge:

1. **Zugang sichern:** Genaues Zugangsdatum (Briefkasteneinwurf, persönliche Übergabe) mit Beweismittel dokumentieren.
2. **Frist berechnen:** 3 Wochen ab Zugang = Klagefrist § 4 KSchG. Datum im Kalender markieren.
3. **Schriftform prüfen:** Liegt eine eigenhändig unterzeichnete Originalurkunde vor (§ 623 BGB)? E-Mail, Fax, WhatsApp = nichtig (§ 125 BGB).
4. **Mandantenentscheidung zeitnah:** Klage, Aufhebungsverhandlung oder Klageverzicht?

## Phase 1: Formelle Prüfung

### A) Schriftform § 623 BGB
- Original-Unterschrift des Kündigungsberechtigten zwingend
- Faksimile-Stempel genügt nicht
- Elektronische Übermittlung genügt nicht
- Fehler → Nichtigkeit; Kündigung ist inexistent

### B) Kündigungsberechtigter
- Wer hat unterzeichnet? Ist die Person zur Kündigung bevollmächtigt?
- Bei Vollmacht: War die Vollmacht im Original beigefügt (§ 174 BGB)? Zurückweisung sofort nach Empfang!
- Bei Organen (GF, Vorstand): Vertretungsberechtigung aus Handelsregister prüfen

### C) Zugang § 130 BGB
- Persönliche Übergabe: Zugang sofort
- Briefkasteneinwurf: Zugang wenn Leerung üblicherweise zu erwarten war (BAG-Linie: bis 17/18 Uhr am selben Tag, danach am nächsten Werktag)
- Urlaub, Krankheit, Auslandsaufenthalt: Zugang dennoch, wenn Kenntnisnahmemöglichkeit besteht

## Phase 2: KSchG-Anwendbarkeit

| Merkmal | Norm | Prüfung |
|---|---|---|
| Betriebsgröße > 10 VZÄ | § 23 KSchG | Vollzeitkräfte + anteilig Teilzeit; Leiharbeitnehmer? (BAG-Linie) |
| Betriebszugehörigkeit > 6 Monate | § 1 Abs. 1 KSchG | Probezeiten, Vorbeschäftigung beim selben Arbeitgeber |
| Betrieb im Geltungsbereich | § 23 KSchG | Deutsches Arbeitsverhältnis |

Wenn KSchG nicht anwendbar: allgemeiner Kündigungsschutz (§ 242 BGB, § 138 BGB, Maßregelungsverbot § 612a BGB) prüfen.

## Phase 3: Sonderkündigungsschutz

| Schutz | Norm | Voraussetzung |
|---|---|---|
| Schwangerschaft / Mutterschutz | § 17 MuSchG | Behördliche Zustimmung Landesamt zwingend |
| Elternzeit | § 18 BEEG | Behördliche Zustimmung zwingend (Ausnahmen eng) |
| Schwerbehinderung | § 168 SGB IX | Zustimmung Integrationsamt zwingend |
| Betriebsratsmitglied | §§ 15 KSchG, 103 BetrVG | BR-Zustimmung oder gerichtliche Ersetzung |
| Datenschutzbeauftragter | § 38 BDSG | Besonderer Kündigungsschutz |
| Wahlvorstand / Kandidaten | § 15 KSchG | Schutz ab Bekanntmachung der Wahl |

**Konsequenz:** Fehlt eine behördliche Zustimmung → Kündigung ist schwebend unwirksam oder nichtig.

## Phase 4: Betriebsratsanhörung § 102 BetrVG

### Checkliste
- [ ] Ist ein Betriebsrat vorhanden?
- [ ] Wurde dieser vor Ausspruch der Kündigung angehört?
- [ ] Enthielt das Anhörungsschreiben: Name des Arbeitnehmers, Art der Kündigung, Kündigungsgründe, Sozialdaten?
- [ ] Wurde die Frist eingehalten (ordentlich: 1 Woche; außerordentlich: 3 Tage; § 102 Abs. 2 BetrVG)?
- [ ] Hat der BR Einwände erhoben? Wenn ja: wurden sie beachtet?

**Rechtsfolge Fehler:** Kündigung ist unwirksam — unabhängig vom materiellen Kündigungsgrund.

## Phase 5: Massenentlassungsanzeige § 17 KSchG

### Schwellenwerte (§ 17 Abs. 1 KSchG)
| Betriebsgröße | Entlassungen innerhalb 30 Tagen |
|---|---|
| 21–59 AN | ≥ 6 |
| 60–499 AN | ≥ 10 % oder ≥ 26 |
| ≥ 500 AN | ≥ 30 |

**Neue BAG/EuGH-Linie (BAG 6 AZR 152/22, EuGH C-134/24):** Anzeige muss nach Abschluss der BR-Konsultation, aber vor Ausspruch der Kündigungen erfolgen. Fehler = Unwirksamkeit aller betroffenen Kündigungen, keine Heilung möglich.

## Phase 6: Soziale Rechtfertigung § 1 KSchG

### Betriebsbedingt
1. Unternehmerische Entscheidung (Wegfall des Arbeitsplatzes)
2. Dringende betriebliche Erfordernis
3. Keine anderweitige Beschäftigungsmöglichkeit
4. **Sozialauswahl § 1 Abs. 3 KSchG:** Betriebszugehörigkeit, Lebensalter, Unterhaltspflichten, Schwerbehinderung — Vergleichsgruppe nach Austauschbarkeit

### Verhaltensbedingt
1. Pflichtverletzung (nachweisbar)
2. Abmahnung (grds. erforderlich, außer schwere Pflichtverletzung)
3. Negative Prognose (Wiederholungsgefahr)

### Personenbedingt
1. Eignungsmangel / Krankheit
2. Negative Gesundheitsprognose
3. Erhebliche betriebliche Beeinträchtigung
4. Interessenabwägung (BAG-Dreistufentest)

## Entscheidungsmatrix: Klage oder Vergleich?

| Lage | Empfehlung |
|---|---|
| Formfehler oder fehlende BR-Anhörung | Klage einlegen; Verhandlungsmacht ist maximal |
| KSchG nicht anwendbar, keine Formfehler | Vergleich; Klagechancen begrenzt |
| Starke betriebliche Kündigung, korrekte Sozialauswahl | Vergleich mit guter Abfindung realistisch |
| Sonderkündigungsschutz betroffen | Klage; volle Nichtigkeitsfolge |
| Mandant will schnell Anschlussstelle | Vergleich mit günstigem Zeugnistext |

## Anschluss-Skills
- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` für Klageschrift und Verfahrensstrategie
- `ar-abfindungs-rechner-modular` für Abfindungsberechnung
- `fachanwalt-arbeitsrecht-massenentlassung-17-kschg` für § 17 KSchG-Tiefenprüfung
- `fazugang-neu-001-kuendigung-durch-boten-beweisvermerk-und-prozessstrategie` für Zugangsfragen

## Quellenregel
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link: [dejure.org](https://dejure.org), [openjur.de](https://openjur.de), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de), [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Aktuelle BAG-Linie zu § 17 KSchG und Sozialauswahl stets live prüfen vor Ausgabe.
- Keine BeckRS-, juris- oder Kommentar-Blindzitate.
- Annahmen explizit markieren.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für vollständige Mandantenberatung.
- Keine Prozessprognose ohne konkrete Tatsachenbasis.

## 3. `fazugang-neu-006-arbeitgeber-zustellworkflow-rechtssicher-organi`

**Fokus:** Arbeitgeber-Zustellworkflow: rechtssichere Organisation der Kündigungszustellung, Parallelwege (Bote + Einschreiben + Gerichtsvollzieher), Checklisten, Kuvertierungsprotokoll, Risikomanagement bei mehreren Empfängern (Massenentlassung).

# Arbeitgeber-Zustell— Rechtssicher organisieren

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Arbeitgeber-Zustell— Rechtssicher organisieren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Praxisleitfaden für Arbeitgeber und Kanzleien, die Kündigungen rechtssicher zustellen müssen. Besonderes Augenmerk bei Massenentlassungen, wenn viele Kündigungen gleichzeitig organisiert werden müssen.

## Einstieg
Wenn ein konkreter Zustellungsauftrag vorliegt, zuerst klären:

1. **Anzahl der Empfänger:** Eine Kündigung oder mehrere (Massenentlassung)?
2. **Fristkritikalität:** Gibt es ein Datum, bis zu dem alle Kündigungen zugegangen sein müssen (z.B. tarifliche Ausschlussfrist)?
3. **Bekannte Zustellungshindernisse:** Bekannte Abwesenheiten, Auslandsaufenthalte, Postprobleme?
4. **Sonderkündigungsschutz:** Betriebsratsmitglieder, Schwangere, Elternzeit — hier andere Verfahren!
5. **Verfügbare Ressourcen:** Interne Boten, externe Kurierdienste, Gerichtsvollzieher?

## Zustellwege im Überblick

### Weg 1: Botenzustellung (Empfehlung Standard)
- Unternehmensmitarbeiter oder externer Bote überbringt das Schreiben persönlich
- Bei Nichtantreffen: Einwurf in Briefkasten; Beweisvermerk erstellen (→ Skill 001)
- **Vorteil:** Sofortiger Zugang bei persönlicher Übergabe; flexibel
- **Risiko:** Streit über Einwurfzeitpunkt wenn kein Zeuge

### Weg 2: Einwurf-Einschreiben (Ergänzung)
- Parallel zur Botenzustellung; sichert zweiten Zugangsbeweis
- Sendungsverfolgungsprotokoll als Dokumentation aufbewahren
- **Nicht als alleiniger Weg** bei zeitkritischen Fristen (→ Skill 002 für Risiken)

### Weg 3: Gerichtsvollzieher-Zustellung
- Auftrag über Anwalt; öffentliche Urkunde schafft Beweis nach § 418 ZPO
- **Kosten:** Ca. 20–30 € Gebühr pro Zustellung
- **Vorteil:** Unbestreitbarer Zugangszeitpunkt
- **Empfehlung:** Bei besonders streitanfälligen Fällen oder wenn der Empfänger bereits anwaltlich vertreten ist

### Weg 4: Notar-Zustellung
- Notar erstellt Zustellungsprotokoll mit Beglaubigung
- Teuerste Option, aber höchste Beweiskraft
- **Empfehlung:** Nur bei sehr hohem wirtschaftlichem Risiko (z.B. Vorstandskündigung)

## Standard-für eine Kündigung

```
Vorbereitung (Tag -1):
□ Schreiben mit Originaldatum und -unterschrift anfertigen
□ Adresse des Empfängers prüfen (letzte bekannte Meldeadresse)
□ Boten und ggf. Zeugen organisieren
□ Beweisvermerk-Formular bereit

Zustellungstag:
□ Schreiben kuvertieren; Kuvertierungsprotokoll ausfüllen
 (Inhalt, Datum, Unterschrift des Kuvertierenden)
□ Bote übergibt oder wirft ein
□ Beweisvermerk ausfüllen (Datum, Uhrzeit, Adresse, Art)
□ Paralleles Einwurf-Einschreiben aufgeben (Post-Quittung aufheben)

Dokumentation (gleicher Tag):
□ Beweisvermerk in Personalakte ablegen
□ Sendungsverfolgungsnummer notieren
□ Ggf. Foto des Briefkastens
□ Zeuge unterschreibt Beweisvermerk
```

## Massenentlassung — Besondere Anforderungen

### Koordination mit § 17 KSchG-Anzeige
**Wichtig (BAG 6 AZR 152/22, EuGH C-134/24):** Die Massenentlassungsanzeige muss nach Abschluss der Betriebsratsberatung, aber vor Ausspruch der Kündigungen bei der Agentur für Arbeit eingehen. Der Ausspruch der Kündigung = Zugang bei Arbeitnehmer.

**Massenentlassung:**
1. Konsultation Betriebsrat nach § 17 Abs. 2 KSchG abschließen
2. Massenentlassungsanzeige bei der Agentur für Arbeit einreichen
3. Eingangsbestätigung der Agentur für Arbeit abwarten
4. Erst dann: Kündigungen zustellen

### Logistik bei vielen Empfängern
- Nummeriertes Kuvertierungsprotokoll für alle Empfänger
- Separate Beweisvermerke pro Empfänger
- Teamorganisation: Mehrere Boten; klare Zuordnung welcher Bote zu welchem Empfänger
- Zeitprotokoll mit Uhrzeit und Ergebnis je Empfänger

## Sonderfälle

### Sonderkündigungsschutz (Betriebsratsmitglieder, Schwangere, Elternzeit)
Keine Kündigung ohne behördliche Zustimmung oder (bei BR-Mitglied) BR-Beschluss gem. § 103 BetrVG! Zustellung einer Kündigung ohne diese Voraussetzungen ist unwirksam und setzt Frist nicht in Gang.

### Empfänger verweigert Annahme
- Verweigerung dokumentieren (Beweisvermerk)
- Schreiben in Briefkasten einwerfen
- Ggf. Zeuge für Verweigerungsvorgang
- Annahmeverweigerung schließt Zugang nicht aus (§ 130 BGB: Empfänger kann Zugang nicht durch Verweigerung verhindern)

## Checkliste Post-Zustellung

- [ ] Beweisvermerk archiviert (Datum, Uhrzeit, Art, Zeuge)
- [ ] Sendungsverfolgungsbeleg archiviert (bei Einschreiben)
- [ ] Kuvertierungsprotokoll archiviert
- [ ] Klagefrist-Ablauf im Wiedervorlagenkalender notiert
- [ ] Personalakte aktualisiert
- [ ] Ggf. Betriebsrat über Ausspruch informiert (§ 102 Abs. 4 BetrVG)

## Anschluss-Skills
- `fazugang-neu-001-kuendigung-durch-boten-beweisvermerk-und-prozessstrategie` für Beweisvermerk-Details
- `fazugang-neu-002-einwurf-einschreiben-risiko-nach-aktueller-bag-linie` für Einschreibenrisiken
- `fachanwalt-arbeitsrecht-massenentlassung-17-kschg` für § 17 KSchG-Anforderungen
- `workflow-fristen-und-risikoampel` für Fristenmanagement

## Quellenregel
- Normtext live prüfen auf [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- BAG-Entscheidungen via [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de) und [dejure.org](https://dejure.org).
- Keine modellwissensbasierten Zustellstandards ohne Verifikation.
- Annahmen explizit kennzeichnen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für individuelle Prüfung bei Sonderkündigungsschutz.
- Keine Garantie für rechtssichere Zustellung in allen Einzelfällen; Einzelfallprüfung bleibt notwendig.
