---
name: famr-trennungsfolgen
description: "Famr Trennungsfolgen im Plugin Fachanwalt Familienrecht: prüft konkret Fachanwalt Familienrecht — Allgemein im Familienrecht, Trennungsfolgen, Vermoegensauseinandersetzung im Scheidungsfall, Anschluss-Skills Router im Plugin fachanwalt-familienrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Famr Trennungsfolgen

## Arbeitsbereich

**Famr Trennungsfolgen** ordnet den Fall über die tragenden Prüfungslinien: Fachanwalt Familienrecht — Allgemein im Familienrecht, Trennungsfolgen, Vermoegensauseinandersetzung im Scheidungsfall. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `allgemein` | Fachanwalt Familienrecht — Allgemein im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `famr-trennungsfolgen-workflow` | Trennungsfolgen: Unterhalt (Trennung, Kind), Hausrat, Wohnungszuweisung, Sorgerecht, Umgang, Versorgungsausgleich-Vorab. Pruefraster und Erstgespraechs-Checkliste mit Mandantenfragen. |
| `famr-vermoegensauseinandersetzung-workflow` | Vermoegensauseinandersetzung im Scheidungsfall: Zugewinnausgleich Anfangs- und Endvermoegen, Auskunftsanspruch § 1379 BGB, Bewertungsstichtag, gemeinsame Konten und Immobilien. Pruefraster und Mustertexte. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-familienrecht: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-familienrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `allgemein`

**Fokus:** Fachanwalt Familienrecht — Allgemein im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

# Fachanwalt Familienrecht — Allgemein

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt Familienrecht — Allgemein` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Familienrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergaenzend zum Plugin kanzlei-allgemein.

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
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose… |
| `fachanwalt-familienrecht-duesseldorfer-tabelle-unterhalt` | Unterhaltsberechnung nach Duesseldorfer Tabelle und BGB: Mandant will Kindes- oder Ehegattenunterhalt berechnen oder anfechten. Normen: § 1601 ff. BGB (Verwandtenunterhalt), § 1612a BGB (Mindestunterhalt), §§ 1569-1587… |
| `fachanwalt-familienrecht-kindeswohlgefaehrdung-eilantrag` | Kindeswohlgefaehrdung nach § 1666 BGB: Eilantrag auf Sorgerechtsentzug oder Schutzanordnung stellen oder dagegen verteidigen. Normen: § 1666 BGB (Eingriff Familiengericht), § 49 FamFG (Einstweilige Anordnung), § 8a SGB… |
| `fachanwalt-familienrecht-mediation-156-famfg-cochemer` | Familienrechtliche Mediation nach § 156 FamFG und Cochemer Modell: Vermittlungsverfahren § 165 FamFG bei Umgangsverweigerung, ADR-Pfade (Familienmediation DGFM, Familiengerichts-Mediation § 278a ZPO analog, Cochemer… |
| `fachanwalt-familienrecht-orientierung` | Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB ueberblicken. Normen: FamFG (Beschluss statt Urteil, Verbund § 137 FamFG), §§ 23a, 23b GVG… |
| `fachanwalt-familienrecht-sbgg-personenstandswechsel-folgen` | Spezial-Mandat Selbstbestimmungsgesetz SBGG in Kraft 1.11.2024 Personenstandswechsel ohne aerztliches Gutachten. Folgen für Sorgerecht Unterhalt Versorgungsausgleich Ehename Geschlechtseintrag Kinder. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren. Aktualisierte Hinweise 2025/2026: BVerfG 07.10.2025 - 1 BvR 746/23 (Umgangsausschluss-Begründung); BGH 22.01.2025 - XII ZB 148/24 (Elternunterhalt-Selbstbehalt); Düsseldorfer Tabelle 2026 in Kraft seit 01.01.2026. |
| `fachanwalt-familienrecht-unterhaltsberechnung` | Kindes- und Ehegattenunterhalt vollständig berechnen: Mandant trennt sich oder wurde getrennt und will Unterhaltshoehe festlegen. Normen: §§ 1601 ff. BGB (Kindesunterhalt), § 1361 BGB (Trennungsunterhalt), §§ 1569 ff.… |
| `fachanwalt-familienrecht-versorgungsausgleich` | Versorgungsausgleich im Scheidungsverbund durchführen: Rentenanrechte aus Ehe aufteilen. Normen: VersAusglG (seit 2009), §§ 1 und 10 VersAusglG (Hin- und Herrechnung), § 17 VersAusglG (externe Teilung), § 18 VersAusglG… |
| `fachanwalt-familienrecht-zugewinnausgleich-berechnen` | Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endvermögen. Normen: § 1373 BGB (Zugewinn), § 1374 BGB (Anfangsvermögen inkl. Privilegierungen Abs. 2),… |
| `mandat-triage-familienrecht` | Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich. Normen: § 63 FamFG (Beschwerde 1 Monat), § 1600b BGB (Vaterschaftsanfechtung 2 Jahre),… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Scheidungsantrag, Unterhaltsklage, Sorgerechtsantrag, VA-Beschwerde: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `umgangsregelung-mustervorlagen` | Umgangsregelungen nach §§ 1684 und 1685 BGB formulieren: Regelmäßiger Umgang oder Streit um Umgangsrecht soll durch Vereinbarung oder Beschluss gelöst werden. Normen: § 1684 BGB (Umgang Eltern), § 1685 BGB (Umgang… |
| `unterhalt-duesseldorfer-tabelle` | Kindes- und Ehegattenunterhalt nach Duesseldorfer Tabelle berechnen: Praktische Berechnungsaufgabe mit konkreten Einkommensdaten. Normen: §§ 1601 ff. BGB, § 1605 BGB (Selbstauskunft), § 1613 BGB (Verzug). Prüfraster:… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Familien-, Kindschafts- und Versorgungsausgleichsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

<!-- BEGIN ACTUAL-SKILL-ROUTING -->

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `abaenderung-versorgungsausgleich-51-versausglg` | Abänderung Versorgungsausgleich § 51 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschw... |
| `aerztliche-versorgungswerke-berufsstaendische-versorgung` | Ärztliche Versorgungswerke berufsständische Versorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und... |
| `anpassung-wegen-invaliditaet-oder-besonderer-haerte` | Anpassung wegen Invalidität oder besonderer Härte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Besc... |
| `anpassung-wegen-unterhalt-33-ff-versausglg` | Anpassung wegen Unterhalt §§ 33 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwer... |
| `anrechte-dokumentenintake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Anrechte Dokumentenintake. |
| `anwartschaft-dynamisch-statisch-bewertung` | Anwartschaft dynamisch statisch Bewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde,... |
| `ausgleich-nach-der-scheidung-20-ff-versausglg` | Ausgleich nach der Scheidung §§ 20 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Besch... |
| `auslaendische-anrechte-versorgungsausgleich` | Ausländische Anrechte Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde,... |
| `ausschluss-grobe-unbilligkeit-27-versausglg` | Ausschluss grobe Unbilligkeit § 27 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwer... |
| `beamtenrechtliche-kuerzung-und-rueckausnahme` | Beamtenrechtliche Kürzung und Rückausnahme: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde,... |
| `beamtenversorgung-versorgungsausgleich` | Beamtenversorgung Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB... |
| `beschwerde-gegen-va-beschluss-famfg` | Beschwerde gegen VA-Beschluss FamFG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI... |
| `betriebliche-altersversorgung-direktzusage-pensionskasse-fonds` | Betriebliche Altersversorgung Direktzusage Pensionskasse Fonds: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsver... |
| `ehezeit-bestimmen-3-versausglg` | Ehezeit bestimmen § 3 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, B... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinb... |
| `eu-auslandsrenten-und-scheidung` | EU-Auslandsrenten und Scheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Be... |
| `excel-pruefmatrix-anrechte` | Excel-Prüfmatrix Anrechte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenv... |
| `externe-teilung-14-versausglg` | Externe Teilung § 14 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Be... |
| `fachanwalt-familienrecht-duesseldorfer-tabelle-unterhalt` | Prüfungslinie für fachanwalt familienrecht duesseldorfer tabelle unterhalt. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum u... |
| `fachanwalt-familienrecht-kindeswohlgefaehrdung-eilantrag` | Kindeswohlgefaehrdung nach § 1666 BGB: Eilantrag auf Sorgerechtsentzug oder Schutzanordnung stellen oder dagegen verteidigen. Normen: § 1666 BGB (Eingriff Familiengericht), § 49 FamFG (Einst... |
| `fachanwalt-familienrecht-mediation-156-famfg-cochemer` | Familienrechtliche Mediation nach § 156 FamFG und Cochemer Modell: Vermittlungsverfahren § 165 FamFG bei Umgangsverweigerung, ADR-Pfade (Familienmediation DGFM, Familiengerichts-Mediation §... |
| `fachanwalt-familienrecht-orientierung` | Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB ueberblicken. Normen: FamFG (Beschluss statt Urteil, Verbund § 137 FamFG), §§ 2... |
| `fachanwalt-familienrecht-sbgg-personenstandswechsel-folgen` | Prüfungslinie für fachanwalt familienrecht sbgg personenstandswechsel folgen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum... |
| `fachanwalt-familienrecht-scheidungsantrag-stellen` | Prüfungslinie für fachanwalt familienrecht scheidungsantrag stellen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Akte... |
| `fachanwalt-familienrecht-unterhaltsberechnung` | Kindes- und Ehegattenunterhalt vollständig berechnen: Mandant trennt sich oder wurde getrennt und will Unterhaltshoehe festlegen. Normen: §§ 1601 ff. BGB (Kindesunterhalt), § 1361 BGB (Trenn... |
| `fachanwalt-familienrecht-versorgungsausgleich` | Versorgungsausgleich im Scheidungsverbund durchführen: Rentenanrechte aus Ehe aufteilen. Normen: VersAusglG (seit 2009), §§ 1 und 10 VersAusglG (Hin- und Herrechnung), § 17 VersAusglG (exter... |
| `fachanwalt-familienrecht-zugewinnausgleich-berechnen` | Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endvermögen. Normen: § 1373 BGB (Zugewinn), § 1374 BGB (Anfangsvermögen inkl... |
| `famr-einfuehrung-themen` | Familienrecht einfuehrend: Ehe, Scheidung, Zugewinn, Versorgungsausgleich, Unterhalt (Trennungs-, Ehegatten-, Kindes-, Volljaehrigen-), Sorgerecht, Umgangsrecht, Vaterschaft, Adoption. Entsc... |
| `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Spezialfall Kindeswohlgefaehrdung und Eilantrag: § 1666 BGB, Anordnungen Familiengericht, einstweilige Anordnung § 49 FamFG, Inobhutnahme Jugendamt § 42 SGB VIII. Pruefraster und Mustertexte... |
| `famr-mandantenaufnahme-spezial` | Mandantenaufnahme im Familienrecht: emotionale Lage, Eilbedarf (Gewaltschutz, Kindeswohlgefaehrdung, Wegnahme Kind), Vertraulichkeit Familienangehoerige, Verfahrenskostenhilfe. Strukturierte... |
| `famr-regenbogenfamilien-recht-spezial` | Spezialfall Regenbogenfamilien: rechtliche Elternschaft nach BGH, Stiefkindadoption, Co-Mutter-Anerkennung, Reform des Abstammungsrechts (Entwurf 2024 ff.), Sorgerecht bei Trennung. Pruefras... |
| `famr-trennungsfolgen-workflow` | Trennungsfolgen: Unterhalt (Trennung, Kind), Hausrat, Wohnungszuweisung, Sorgerecht, Umgang, Versorgungsausgleich-Vorab. Pruefraster und Erstgespraechs-Checkliste mit Mandantenfragen. |
| `famr-trennungsjahr-praxis` | Trennungsjahr in der Praxis § 1565 BGB: Voraussetzungen, Beleg, Trennung innerhalb der Ehewohnung, Ausnahmen Haertefall. Praxistipps für Beweissicherung, Schriftverkehr, Mandantenleitfaden.... |
| `famr-vermoegensauseinandersetzung-workflow` | Vermoegensauseinandersetzung im Scheidungsfall: Zugewinnausgleich Anfangs- und Endvermoegen, Auskunftsanspruch § 1379 BGB, Bewertungsstichtag, gemeinsame Konten und Immobilien. Prue... |
| `famr-versorgungsausgleich-spezial` | Spezialfall Versorgungsausgleich: VersAusglG, Anrechte Berechnung pro Versorgungstraeger, externe Teilung, interne Teilung, Anpassung wegen Unterhaltszahlung. Pruefraster und Beispielsfall.... |
| `fehlerhafte-auskunft-versorgungstraeger` | Fehlerhafte Auskunft Versorgungsträger: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB... |
| `fragebogen-versorgungsausgleich-ausfuellen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fragebogen Versorgungsausgleich ausfüllen. |
| `geringfuegigkeit-18-versausglg` | Geringfügigkeit § 18 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Be... |
| `gesetzliche-rentenversicherung-entgeltpunkte` | Gesetzliche Rentenversicherung Entgeltpunkte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerd... |
| `grundprinzip-versorgungsausgleich-halbteilung-1-versausglg` | Grundprinzip Versorgungsausgleich Halbteilung § 1 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbu... |
| `interne-teilung-10-versausglg` | Interne Teilung § 10 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Be... |
| `kapitalwert-korrespondierender-kapitalwert-pruefen` | Kapitalwert korrespondierender Kapitalwert prüfen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Besc... |
| `kirchliche-zusatzversorgung` | Kirchliche Zusatzversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamte... |
| `kosten-versorgungstraeger-teilungskosten` | Kosten Versorgungsträger Teilungskosten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SG... |
| `kurze-ehezeit-3-abs-3-versausglg` | Kurze Ehezeit § 3 Abs 3 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI,... |
| `lebensversicherung-abgrenzung-zugewinn-va` | Lebensversicherung Abgrenzung Zugewinn VA: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde,... |
| `mandantenblatt-versorgungsausgleich-in-einfacher-sprache` | Mandantenblatt Versorgungsausgleich in einfacher Sprache: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund u... |
| `mandantenkommunikation-rentenfolgen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Mandantenkommunikation Rentenfolgen. |
| `mandat-triage-familienrecht` | Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich. Normen: § 63 FamFG (Beschwerde 1 Monat), § 1600b BGB (Vate... |
| `nachtraegliche-auskunft-und-vollstreckung` | Nachträgliche Auskunft und Vollstreckung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, S... |
| `nicht-ausgleichsreife-anrechte-19-versausglg` | Nicht ausgleichsreife Anrechte § 19 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwe... |
| `notarielle-scheidungsfolgenvereinbarung-va` | Notarielle Scheidungsfolgenvereinbarung VA: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde,... |
| `öffentlicher-dienst-zusatzversorgung-vbl` | Öffentlicher Dienst Zusatzversorgung VBL: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, S... |
| `pensionszusage-bewertung-insolvenzrisiko` | Pensionszusage Bewertung Insolvenzrisiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, S... |
| `private-rentenversicherung-kapitalwahlrecht` | Private Rentenversicherung Kapitalwahlrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde... |
| `red-team-va-beschluss-rechnerisch` | Red-Team VA-Beschluss rechnerisch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI,... |
| `rentenluecke-nach-scheidung-handlungsoptionen` | Rentenlücke nach Scheidung Handlungsoptionen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerd... |
| `rentnerfall-beide-beziehen-rente` | Rentnerfall beide beziehen Rente: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, B... |
| `riester-ruerup-versorgungsausgleich` | Riester Rürup Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI,... |
| `scheidungsverbund-va-fristenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Scheidungsverbund VA Fristenplan. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Scheidungsantrag, Unterhaltsklage, Sorgerechtsantrag, VA-Beschwerde: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Re... |
| `soldatenversorgung-bundeswehr-schnittstelle` | Soldatenversorgung Bundeswehr Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde... |
| `spezial-duesseldorfer-abschlussprodukt-und-uebergabe` | Duesseldorfer: Abschlussprodukt und Übergabe im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-ehevertrag-red-team-und-qualitaetskontrolle` | Ehevertrag: Red-Team und Qualitätskontrolle im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-eingetragene-mandantenkommunikation-entscheidungsvorlage` | Eingetragene: Mandantenkommunikation und Entscheidungsvorlage im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-ergaenzend-sonderfall-und-edge-case` | Ergaenzend: Sonderfall und Edge-Case-Prüfung im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-fachanwalt-erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-famfg-livequellen-und-rechtsprechungscheck` | Famfg: Livequellen- und Rechtsprechungscheck im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-familiengericht-verhandlung-vergleich-und-eskalation` | Familiengericht: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-familienrecht-tatbestand-beweis-und-belege` | Familienrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-fristen-behoerden-gericht-und-registerweg` | Fristen: Behörden-, Gerichts- oder Registerweg im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-kanzlei-fristennotiz-und-naechster-schritt` | Kanzlei: Fristennotiz und nächster Schritt im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-lebenspartnerschaft-beweislast-und-darlegungslast` | Lebenspartnerschaft: Beweislast, Darlegungslast und Substantiierung im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-literatur-schriftsatz-brief-und-memo-bausteine` | Literatur: Schriftsatz-, Brief- und Memo-Bausteine im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-mandate-risikoampel-und-gegenargumente` | Mandate: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-normen-dokumentenmatrix-und-lueckenliste` | Normen: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-orientierung-fristen-form-und-zuständigkeit` | Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-scheidung-zahlen-schwellen-und-berechnung` | Scheidung: Zahlen, Schwellenwerte und Berechnung im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-sorge-compliance-dokumentation-und-akte` | Sorge: Compliance-Dokumentation und Aktenvermerk im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-umgang-mehrparteien-konflikt-und-interessen` | Umgang: Mehrparteienkonflikt und Interessenmatrix im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-unterhalt-internationaler-bezug-und-schnittstellen` | Unterhalt: Internationaler Bezug und Schnittstellen im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `spezial-zugewinn-formular-portal-und-einreichung` | Zugewinn: Formular, Portal und Einreichungslogik im Plugin fachanwalt familienrecht; mit V90-Fachkern, Normenradar, Fristen-/Beweislastmatrix, Gegenargumenten und direkt verwertbarem Arbeitsprodukt. |
| `steuerliche-folgen-externe-teilung` | Steuerliche Folgen externe Teilung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI,... |
| `tod-eines-ehegatten-anpassung-37-ff-versausglg` | Tod eines Ehegatten Anpassung §§ 37 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Besc... |
| `tod-nach-rechtskraft-vor-umsetzung` | Tod nach Rechtskraft vor Umsetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI,... |
| `umgangsregelung-mustervorlagen` | Umgangsregelungen nach §§ 1684 und 1685 BGB formulieren: Regelmäßiger Umgang oder Streit um Umgangsrecht soll durch Vereinbarung oder Beschluss gelöst werden. Normen: § 1684 BGB (Umgang Elte... |
| `unterhalt-duesseldorfer-tabelle` | Kindes- und Ehegattenunterhalt nach Duesseldorfer Tabelle berechnen: Praktische Berechnungsaufgabe mit konkreten Einkommensdaten. Normen: §§ 1601 ff. BGB, § 1605 BGB (Selbstauskunft), § 1613... |
| `unternehmerversorgung-gesellschafter-geschaeftsfuehrer` | Unternehmerversorgung Gesellschafter-Geschäftsführer: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und B... |
| `va-bei-lebenspartnerschaft` | VA bei Lebenspartnerschaft: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamten... |
| `va-im-internationalen-scheidungsfall` | VA im internationalen Scheidungsfall: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB V... |

Weitere Skills: insgesamt 108 Anschluss-Skills in diesem Plugin.

<!-- END ACTUAL-SKILL-ROUTING -->

## Fachlicher Zuschnitt

- **Thema:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Familienrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig.
- **Arbeitsfokus:** ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage..
- **Plugin-Rahmen:** Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehev....
- **Qualitätsanspruch:** Antworte nicht mit einer austauschbaren Standard-Checkliste. Nutze die Fachlogik dieses Plugins, benenne die konkret einschlägigen Normgruppen, Behörden, Register, Fristen, Dokumente oder Verfahrenshandlungen und trenne sichere Punkte von Live-Check-Bedarf.
- **Eloquenz und Nutzen:** Führe die Nutzerin oder den Nutzer wie eine erfahrene Fachperson: kurze Orientierung, präzise Rückfragen, dann ein verwertbares Produkt mit Varianten, Gegenargumenten und nächstem Handgriff.

## 2. `famr-trennungsfolgen-workflow`

**Fokus:** Trennungsfolgen: Unterhalt (Trennung, Kind), Hausrat, Wohnungszuweisung, Sorgerecht, Umgang, Versorgungsausgleich-Vorab. Pruefraster und Erstgespraechs-Checkliste mit Mandantenfragen.

# FamR: Trennungsfolgen

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `FamR: Trennungsfolgen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: FamR: Trennungsfolgen
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

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
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `famr-vermoegensauseinandersetzung-workflow`

**Fokus:** Vermoegensauseinandersetzung im Scheidungsfall: Zugewinnausgleich Anfangs- und Endvermoegen, Auskunftsanspruch § 1379 BGB, Bewertungsstichtag, gemeinsame Konten und Immobilien. Pruefraster und Mustertexte.

# FamR: Vermoegensauseinandersetzung

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `FamR: Vermoegensauseinandersetzung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: FamR: Vermoegensauseinandersetzung
- **Normen-/Quellenanker:** BGB.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

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
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 4. `workflow-anschluss-skills-router`

**Fokus:** Anschluss-Skills Router im Plugin fachanwalt-familienrecht: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor.

# Anschluss-Skills Router

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anschluss-Skills Router` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Anschluss-Skills Router im Plugin fachanwalt-familienrecht: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor..

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

## 5. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-familienrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Chronologie und Belegmatrix` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe
Dieses Modul bearbeitet: Chronologie und Belegmatrix im Plugin fachanwalt-familienrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen..

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
