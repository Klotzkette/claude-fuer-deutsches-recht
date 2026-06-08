---
name: start-chronologie-fristen
description: "Start Chronologie Fristen im Plugin Fachanwalt Erbrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt Erbrecht-Plugin, Chronologie und Belegmatrix im Plugin fachanwalt-erbrecht, Fristen- und Risikoampel im Plugin fachanwalt-erbrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Start Chronologie Fristen

## Arbeitsbereich

**Start Chronologie Fristen** ordnet den Fall über die tragenden Prüfungslinien: Einstieg, Schnelltriage und Fallrouting im Fachanwalt Erbrecht-Plugin, Chronologie und Belegmatrix im Plugin fachanwalt-erbrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Erbrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-erbrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-erbrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Erbrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

### Fachanwalt Erbrecht — Allgemein

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt Erbrecht — Allgemein` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Erbrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein.

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
| `erstgespraech-mandatsannahme` | Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen. §§ 1922 ff. BGB Erbfolge § 43a BRAO. Prüfraster: Erblasser Testament gesetzliche Erben Pflichtteilsberechtigte Nachlassbestand… |
| `fachanwalt-erbrecht-erbschaftsausschlagung` | Erbschaftsausschlagung erlaeutern und Erklärung formulieren wenn Erbe ueberschuldet ist oder sonstige Gründe vorliegen. §§ 1942 1944 1945 BGB Ausschlagung. Prüfraster: Ausschlagungsfrist sechs Wochen drei Monate… |
| `fachanwalt-erbrecht-erbschein-antrag` | Erbschein beantragen wenn Erbfolge nachgewiesen werden muss. §§ 2353 2356 BGB Erbschein §§ 352 353 FamFG Verfahren. Prüfraster: Erbscheinsart gesetzliche oder testamentarische Erbfolge Quoten Vorlage Nachlassgericht… |
| `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig` | Krypto-Vermögenswerte und digitale Wallets im Erbfall sichern und auf Erben uebertragen. §§ 1922 1967 BGB digitale Nachlasswerte. Prüfraster: Wallet-Zugang Private Keys Multi-Sig Wertermittlung Steuer Erbschaft… |
| `fachanwalt-erbrecht-orientierung` | Erbrechtsmandat einordnen Bearbeitungsroute bestimmen und erste Prioritaeten setzen. §§ 1922 2229 2303 BGB § 43a BRAO. Prüfraster: Erbfolge Testament Pflichtteil Ausschlagung Nachlassinsolvenz Fristen. Output:… |
| `fachanwalt-erbrecht-pflichtteilsberechnung` | Pflichtteilsanspruch berechnen wenn Erblasser nahe Angehoerige vom Erbe ausgeschlossen hat. §§ 2303 2311 2314 BGB Pflichtteil. Prüfraster: Pflichtteilsberechtigter Nachlasswert Bewertung Auskunftsanspruch… |
| `fachanwalt-erbrecht-pflichtteilsergaenzung-2325` | Pflichtteilsergaenzungsanspruch nach § 2325 BGB berechnen wenn Erblasser Schenkungen gemacht hat. § 2325 BGB Pflichtteilsergaenzung § 2329 BGB. Prüfraster: Schenkung innerhalb 10 Jahre Abschmelzung Wertbestimmung… |
| `fachanwalt-erbrecht-testamentsentwurf` | Testament oder Erbvertrag entwerfen wenn Mandant Nachlassplanung vornehmen moechte. §§ 2229 2231 2247 BGB Testament §§ 2274 ff. BGB Erbvertrag. Prüfraster: Testierfähigkeit Form Erbeinsetung Vermaechtnisse… |
| `fachanwalt-erbrecht-testamentsvollstreckung` | Testamentsvollstreckung einrichten oder bei Streit über Vollstreckerbefugnisse beraten. §§ 2197 ff. BGB Testamentsvollstreckung. Prüfraster: Anordnung Befugnisse Aufgaben Haftung Verguetung Aufsicht Nachlassgericht… |
| `fachanwalt-erbrecht-verhandlung-mediation-erbengemeinschaft` | Streit in der Erbengemeinschaft durch Verhandlung oder Mediation lösen. §§ 2032 2042 2047 BGB Erbengemeinschaft. Prüfraster: Erbteile Nachlassbestand Verwaltungsmassnahmen Teilungsklage Auseinandersetzung… |
| `mandat-triage-erbrecht` | Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen. §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Output: Triage-Memo… |
| `nachlassinsolvenz-erbenhaftung-begrenzen` | Nachlassinsolvenz beantragen oder Erbenhaftung auf den Nachlass begrenzen wenn Nachlass ueberschuldet ist. §§ 1975 1980 2059 BGB Nachlassinsolvenz §§ 315 ff. InsO. Prüfraster: Nachlassueberschuldung Antragspflicht… |
| `pflichtteil-berechnen` | Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch berechnen. §§ 2303 2311 2325 BGB Pflichtteil. Prüfraster: Pflichtteilsquote Nachlasswert Bewertungsstichtag Abzuege Ergaenzungsanspruch Auskunft. Output:… |
| `schriftsatzkern-substantiierung` | Erbrechtsklage oder erbrechtlichen Antrag substantiiert formulieren. §§ 2303 2353 BGB §§ 253 286 ZPO. Prüfraster: Anspruchsgrundlage Sachverhalt Beweisangebot Antrag Streitwert Fristen. Output: Schriftsatzkern… |
| `vergleichsverhandlung-strategie` | Erbrechtlichen Streit durch Vergleich lösen und Verhandlungsstrategie entwickeln. §§ 2303 2042 BGB §§ 779 BGB Vergleich. Prüfraster: Vergleichsziele BATNA Nachlasswert Kosten Zeitperspektive Geheimhaltung. Output:… |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren. Aktualisierte Eckpfeiler 2025: BGH 12.03.2025 - IV ZR 88/24 (Pflichtteil nichteheliches Kind); BGH 02.07.2025 - IV ZR 93/24 (Zuwendung an Hausarzt; Berufsordnung kein § 134 BGB-Verbot). |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## 2. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-erbrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

### Chronologie und Belegmatrix

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Chronologie und Belegmatrix` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Chronologie und Belegmatrix im Plugin fachanwalt-erbrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen..

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

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-erbrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

### Fristen- und Risikoampel

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristen- und Risikoampel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin fachanwalt-erbrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Kritische Fristen Erbrecht
- Ausschlagung: sechs Wochen ab Kenntnis vom Anfall und Berufungsgrund (§ 1944 Abs. 1 BGB); sechs Monate bei Auslandsbezug oder gewöhnlichem Auslandsaufenthalt (§ 1944 Abs. 3 BGB). Form: vor Nachlassgericht oder notariell (§ 1945 BGB).
- Pflichtteilsverjährung: drei Jahre ab Kenntnis von Erbfall und beeinträchtigender Verfügung (§§ 2332, 195, 199 BGB); Höchstfrist 30 Jahre ab Erbfall.
- Pflichtteilsergänzung: zehn-Jahres-Frist Schenkungen ab Vollzug, Abschmelzung pro Jahr (§ 2325 Abs. 3 BGB).
- Anfechtung Testament/Erbvertrag: ein Jahr ab Kenntnis (§ 2082 BGB).
- Erbschaftsteuer: Anzeigepflicht drei Monate ab Kenntnis (§ 30 ErbStG); Steuererklärungsfrist nach Aufforderung mindestens einen Monat (§ 31 ErbStG).
- Inventarfrist auf Antrag eines Gläubigers (§ 1994 BGB) zur Haftungsbegrenzung.

## Trade-off Haftung
- Ausschlagung schließt auch Vermächtnis aus (§ 2180 BGB beachten: gesonderte Ausschlagung).
- Beschränkung Erbenhaftung über Nachlassinsolvenz (§ 1980 BGB), Nachlassverwaltung (§ 1981 BGB) oder Dürftigkeitseinrede (§ 1990 BGB) prüfen.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
