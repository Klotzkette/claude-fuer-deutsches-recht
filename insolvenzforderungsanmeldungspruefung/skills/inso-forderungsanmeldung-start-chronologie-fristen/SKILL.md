---
name: inso-forderungsanmeldung-start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Insolvenzforderungsanmeldungspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Insolvenzforderungsanmeldungspruefung."
---

# Insolvenzforderungsanmeldungspruefung — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzforderungsanmeldungspruefung — Allgemein` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Insolvenzforderungsanmeldungspruefung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung.

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
| `ifap-aktenanlage-batchregister` | Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes… |
| `ifap-beleg-und-urkundencheck` | Belege und Urkunden bei Insolvenzforderungsanmeldung prüfen: Anwendungsfall Gläubiger legt Rechnungen Verträge Titel Lieferscheine Kontoauszüge vor; Insolvenzverwalter oder Prüfungsstelle muss Belegkette aufbauen und… |
| `ifap-dubletten-serienforderungen` | Dubletten und Serienforderungen in Insolvenzanmeldungen erkennen: Anwendungsfall mehrere Gläubiger melden gleichartige oder identische Forderungen an; Inkassounternehmen und Originalgläubiger reichen parallel ein. §… |
| `ifap-formalpruefung-174` | Formalprüfung Forderungsanmeldung nach § 174 InsO: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle prüft ob eingegangene Anmeldung Mindestangaben hat und tabellenfähig ist. § 174 InsO Pflichtinhalt, § 175 InsO… |
| `ifap-grund-betrag-zinsen` | Anspruchsgrund Betrag und Zinsen der Insolvenzforderung prüfen: Anwendungsfall Insolvenzverwalter prüft ob angemeldeter Betrag rechnerisch korrekt und durch Anspruchsgrundlage gedeckt ist. § 174 InsO… |
| `ifap-intake-kanalcheck` | Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. §… |
| `ifap-kommandocenter` | Kommandocenter Insolvenzforderungsanmeldungsprüfung: Steuerung des gesamten Prüfpfads von Eingang bis Tabelle. Anwendungsfall Insolvenzverwalter oder Kanzlei erhält neuen Forderungsstapel und muss schnell den richtigen… |
| `ifap-masseverbindlichkeit-abgrenzen` | Masseverbindlichkeiten von Insolvenzforderungen abgrenzen: Anwendungsfall Insolvenzverwalter erkennt Forderung die nach Verfahrenseroeffnung entstanden sein koennte und muss klaeren ob es Masseverbindlichkeit oder… |
| `ifap-nachforderung-maengelschreiben` | Mängel- und Nachforderungsschreiben bei unvollständigen Insolvenzanmeldungen: Anwendungsfall Forderungsanmeldung nach § 174 InsO hat Mängel und Insolvenzverwalter muss Gläubiger präzise und freundlich zur Ergänzung… |
| `ifap-nachtraegliche-anmeldung-177` | Verspätete und nachträgliche Forderungsanmeldungen nach § 177 InsO: Anwendungsfall Gläubiger meldet Forderung nach Ablauf der Anmeldefrist an oder ändert bereits angemeldete Forderung. § 177 InsO Nachtragsanmeldung, §… |
| `ifap-pruefentscheidung` | Prüfentscheidung Forderung festzustellen oder zu bestreiten: Anwendungsfall nach abgeschlossener Prüfung trifft Insolvenzverwalter Entscheidung über Feststellung Teilfeststellung Bestreiten oder Rückstellung. § 176… |
| `ifap-pruefungstermin-176` | Prüfungstermin nach § 176 InsO vorbereiten: Anwendungsfall Prüfungstermin beim Insolvenzgericht naht und Insolvenzverwalter muss Einzelforderungen, Widersprüche und Erörterungspunkte aufbereiten. § 176 InsO… |
| `ifap-quality-gate` | Qualitätsgate vor Tabelleneintrag Prüfungstermin und Verteilung: Anwendungsfall alle Prüfschritte wurden durchgeführt und jetzt muss vor Versand oder Eintrag nochmals Vollständigkeit Plausibilitaet und Risiken geprüft… |
| `ifap-rang-nachrang-absonderung` | Rang Nachrang Absonderung und Aussonderung bei Insolvenzforderungen prüfen: Anwendungsfall Gläubiger behauptet Sonderrechte wie Absonderungsrecht aus Sicherungsuebereignung oder Nachrang. §§ 38-39 InsO… |
| `ifap-schuldnerwiderspruch-184` | Schuldnerwiderspruch nach § 184 InsO prüfen und Fristen einhalten: Anwendungsfall Schuldner widerspricht Forderung und bei titulierten Forderungen laeuft Monatsfrist für Aufnahme des Rechtsstreits. § 184 InsO… |
| `ifap-streitige-forderung-179-180` | Streitige Forderungen nach §§ 179 und 180 InsO nachverfolgen: Anwendungsfall Forderung wurde beim Prüfungstermin bestritten und Gläubiger muss Feststellungsklage erheben oder laufenden Rechtsstreit aufnehmen. § 179… |
| `ifap-tabellenauszug-178` | Tabellenauszug und Feststellungswirkung nach § 178 InsO: Anwendungsfall Forderung ist festgestellt und Gläubiger fragt nach Status oder Insolvenzverwalter muss Tabellenauszug als vollstreckbaren Titel erstellen. § 178… |
| `ifap-tabellenimport-175` | Tabelleneintrag und Tabellenimport nach § 175 InsO: Anwendungsfall Forderungen sind geprüft und muessen in gerichtliche Tabelle überführt werden oder CSV-Import in Verwaltungssoftware vorbereitet werden. § 175 InsO… |
| `ifap-vbuh-pruefung` | Vorsätzlich begangene unerlaubte Handlung und Steuerstraftat in Insolvenzanmeldung prüfen: Anwendungsfall Gläubiger meldet Forderung mit Kennzeichnung als vbuH vorsaetzliche unerlaubte Handlung… |
| `ifap-verteilung-bestrittene-189` | Verteilung bei bestrittenen Forderungen nach § 189 InsO: Anwendungsfall Insolvenzverwalter bereitet Abschlags- oder Schlussverteilung vor und muss bestrittene Forderungen korrekt zurückbehalten oder ausklammern. § 189… |

## Worum geht es?

Dieses Plugin unterstuetzt Insolvenzverwalter, Pruefungsstellen und Kanzleien bei der strukturierten Pruefung von Insolvenzforderungsanmeldungen nach §§ 174-189 InsO. Es deckt den gesamten Pruefpfad ab: vom kanaluebergreifenden Eingang der Anmeldungen ueber Formalprüfung, Belegprüfung, Anspruchsgrundlage, Betrag, Zinsen, Rangprüfung und vorsaetzlich begangene unerlaubte Handlung (vbuH) bis hin zu Pruefungstermin, Bestreitungsverfahren, Tabelleneintrag, Tabellenauszug und Verteilung.

Das Plugin ist freistehend und eignet sich sowohl für Einzelforderungen als auch für Massenverfahren mit strukturiertem Batchregister.

## Wann brauchen Sie diese Skill?

- Sie sind Insolvenzverwalter und erhalten einen neuen Stapel von Forderungsanmeldungen nach § 174 InsO.
- Sie muessen Formalmaengel in einer Forderungsanmeldung identifizieren und ein Maengelschreiben erstellen.
- Sie bereiten den Pruefungstermin nach § 176 InsO vor und benoetigen eine strukturierte Terminmappe.
- Ein Glaeubiger hat die Forderung als vbuH gekennzeichnet und Sie muessen die Restschuldbefreiungsrelevanz pruefen.
- Sie bereiten die Schlussverteilung vor und muessen bestrittene Forderungen nach § 189 InsO korrekt behandeln.

## Fachbegriffe (kurz erklaert)

- **Forderungsanmeldung** — Erklaerung des Glaeubiger gegenueber dem Insolvenzgericht oder Insolvenzverwalter ueber seine Insolvenzforderung (§ 174 InsO).
- **Tabelle** — Das vom Insolvenzgericht gefuehrte Verzeichnis aller angemeldeten Insolvenzforderungen (§ 175 InsO).
- **Pruefungstermin** — Termin beim Insolvenzgericht, in dem Forderungen auf Feststellung oder Bestreitung geprüft werden (§ 176 InsO).
- **Feststellungswirkung** — Die anerkannte Forderung wirkt wie ein rechtskraeftiger Titel gegen den Schuldner (§ 178 InsO).
- **vbuH** — Vorsaetzlich begangene unerlaubte Handlung; Forderungen aus vbuH sind von der Restschuldbefreiung ausgenommen (§ 302 Nr. 1 InsO).
- **Nachrang** — Insolvenzforderungen, die erst nach den einfachen Insolvenzforderungen befriedigt werden (§ 39 InsO).
- **Absonderungsrecht** — Recht bestimmter Glaeubiger, aus bestimmten Gegenstanden der Insolvenzmasse vorab befriedigt zu werden (§§ 49-51 InsO).

## Rechtsgrundlagen

- §§ 38-39 InsO — Insolvenzforderungen und Nachrang
- §§ 47-51 InsO — Aussonderung und Absonderungsrechte
- §§ 53-55 InsO — Masseverbindlichkeiten
- §§ 174-177 InsO — Anmeldung und Nachtragsanmeldung
- §§ 178-183 InsO — Feststellung, Bestreiten und Wirkung
- §§ 184-186 InsO — Schuldnerwiderspruch
- §§ 188-196 InsO — Verteilung und Schlussverteilung
- § 302 InsO — Ausnahmen von der Restschuldbefreiung (vbuH)
- § 850f Abs. 2 ZPO — Pfaendungsfreigrenze bei vbuH

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Verwalterrolle, Verfahrensstand (Eroeffnung, Pruefungstermin, Verteilung), Forderungstyp.
2. Phase des Mandats bestimmen: Eingangserfassung, Formalprüfung, inhaltliche Pruefung, Entscheidung, Termin oder Verteilung.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Pruefungstermin-Termin, Frist Schuldnerwiderspruch (§ 184 InsO Monatsfrist), Verteilungs-Nachweis (§ 189 InsO).
5. Anschluss-Skill bestimmen: nach Formalprüfung folgt inhaltliche Pruefung; nach Pruefungstermin folgt Tabelleneintrag oder Streitverfahren.

## Skill-Tour (was gibt es hier?)

**Einstieg und Steuerung**

- `ifap-kommandocenter` — Steuerung des gesamten Pruefpfads von Eingang bis Tabelle; zeigt naechste Schritte und Fristen an.
- `ifap-intake-kanalcheck` — Kanaluebergreifende Eingangserfassung: Post, E-Mail, Portal, Tabellenexport und Nachtrag.
- `ifap-aktenanlage-batchregister` — Strukturiertes Batchregister für Massenverfahren mit Glaeubigerstamm, Fristen und Audit-Trail.

**Formalprüfung**

- `ifap-formalpruefung-174` — Formalprüfung nach § 174 InsO: Pflichtinhalt, Glaeubiger, Anspruchsgrund, Betrag, Urkundenvorlage.
- `ifap-beleg-und-urkundencheck` — Prueft Belegkette (Rechnungen, Vertraege, Titel) auf Vollstaendigkeit und Beweiswert.
- `ifap-dubletten-serienforderungen` — Erkennt Doppelerfassungen und Serienforderungen (z.B. Inkasso und Originalglaeubiger parallel).
- `ifap-nachtraegliche-anmeldung-177` — Behandlung verspaeteter Forderungsanmeldungen nach § 177 InsO mit Kostenpflicht und Sondertermin.
- `ifap-nachforderung-maengelschreiben` — Erstellt praezises Maengelschreiben bei unvollstaendiger Anmeldung mit konkreten Nachforderungen.

**Inhaltliche Pruefung**

- `ifap-grund-betrag-zinsen` — Prueft Anspruchsgrundlage, Betrag und Zinsberechnung der angemeldeten Forderung.
- `ifap-rang-nachrang-absonderung` — Klassifiziert Forderung nach Rang: einfach, Nachrang, Absonderungsrecht oder Aussonderungsrecht.
- `ifap-masseverbindlichkeit-abgrenzen` — Grenzt Masseverbindlichkeiten von Insolvenzforderungen nach Entstehungszeitpunkt ab.
- `ifap-vbuh-pruefung` — Prueft Kennzeichnung als vbuH, Restschuldbefreiungsrelevanz und Begruendungsanforderungen.

**Pruefungsentscheidung und Termin**

- `ifap-pruefentscheidung` — Entscheidung ueber Feststellung, Teilfeststellung, Bestreiten oder Rueckstellung.
- `ifap-pruefungstermin-176` — Vorbereitung des Pruefungstermins nach § 176 InsO: Terminmappe, Widersprueche, schriftliches Verfahren.
- `ifap-quality-gate` — Qualitaetsgate vor Tabelleneintrag, Pruefungstermin und Verteilung: Vollstaendigkeit und Plausibilitaet.

**Bestreiten und Streit**

- `ifap-streitige-forderung-179-180` — Nachverfolgung bestrittener Forderungen: Feststellungsklage (§ 179 InsO), Tabellenklage (§ 180 InsO).
- `ifap-schuldnerwiderspruch-184` — Schuldnerwiderspruch nach § 184 InsO pruefen und Monatsfrist für Aufnahme des Rechtsstreits einhalten.

**Tabelle und Verteilung**

- `ifap-tabellenimport-175` — Tabelleneintrag und CSV-Import nach § 175 InsO mit tabellenfaehiger Ausgabe.
- `ifap-tabellenauszug-178` — Tabellenauszug als vollstreckbaren Titel nach § 178 InsO erstellen.
- `ifap-verteilung-bestrittene-189` — Verteilung bei bestrittenen Forderungen nach § 189 InsO: Rueckbehalt-Berechnung.

## Worauf besonders achten

- **Formalmaengel fruehzeitig behandeln.** Eine formal unvollstaendige Anmeldung nach § 174 InsO kann nicht festgestellt werden; Maengelschreiben sofort nach Eingang erstellen.
- **vbuH-Kennzeichnung erfordert Tatsachengrundlage.** Nicht jede Deliktsforderung ist automatisch vbuH; der Glaeubiger muss Tatsachen darlegen (§ 174 Abs. 2 InsO).
- **Masseverbindlichkeiten nicht als Insolvenzforderungen behandeln.** Entstehungszeitpunkt (vor oder nach Eroeffnung) und Verwalterhandeln sind entscheidend.
- **Monatsfrist nach Pruefungstermin beachten.** Bei Schuldnerwiderspruch zu titulierten Forderungen laeuft die Aufnahme-Frist nach § 184 InsO ab Pruefungstermin.
- **Verteilung korrekt berechnen.** Bestrittene Forderungen nach § 189 InsO koennen nur beruecksichtigt werden, wenn der Glaeubiger rechtzeitig Nachweis erbringt.

## Typische Fehler

- Rang wird nicht geprueft; Nachrang-Forderungen (§ 39 InsO) werden als einfache Insolvenzforderungen eingetragen.
- Belegkette ist unvollstaendig; Forderung wird festgestellt ohne dass Anspruchsgrundlage belegt ist.
- Dubletten werden nicht erkannt; Doppelzahlung im Verteilungsverfahren ist moegliche Folge.
- Pruefungstermin wird ohne Terminmappe angegangen; streitige Forderungen koennen nicht geordnet behandelt werden.
- Schuldnerwiderspruch bei titulierten Forderungen wird nicht nachverfolgt; Glaeubiger verliert Feststellungswirkung durch Fristversaeumnis.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (InsO, ZPO, BGB)

