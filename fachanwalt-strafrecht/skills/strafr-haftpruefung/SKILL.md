---
name: strafr-haftpruefung
description: "Strafr Haftpruefung im Strafrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Haftpruefung und Haftbeschwerde §§ 117 ff, Chronologie und Belegmatrix im Plugin fachanwalt-strafrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Strafr Haftpruefung

## Arbeitsbereich

**Strafr Haftpruefung** ordnet den Fall über die tragenden Prüfungslinien: Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Haftpruefung und Haftbeschwerde §§ 117 ff. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Strafrecht-Plugin. Startet nicht nur Beratung und Strategie, sondern auch die tägliche Strafprozess-Durchführung: Fristenlog, Aktenlog, U-Haft, Akteneinsicht, Hauptverhandlungs-Tagesmappe, Antragslog, Mandanteninstruktionen, Rechtsmittel und Revisionssicherung. Bei Dokument-Upload ohne Begleittext ordnet der Skill das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `strafr-haftpruefung-haftbeschwerde-workflow` | Haftpruefung und Haftbeschwerde §§ 117 ff. StPO: dringender Tatverdacht, Haftgrund, Verhaeltnismaessigkeit, Sechsmonatspruefung. Mustertext Haftpruefungsantrag und Haftbeschwerde. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-strafrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-strafrecht: macht aus Strafbefehl, Urteil, Beschluss, Ladung, Haftbefehl, beA-/EGVP-Eingang oder Aktennachlieferung eine Sofortampel für Frist, Zuständigkeit, U-Haft, Rechtsmittel, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Strafrecht-Plugin. Startet nicht nur Beratung und Strategie, sondern auch die tägliche Strafprozess-Durchführung: Fristenlog, Aktenlog, U-Haft, Akteneinsicht, Hauptverhandlungs-Tagesmappe, Antragslog, Mandanteninstruktionen, Rechtsmittel und Revisionssicherung. Bei Dokument-Upload ohne Begleittext ordnet der Skill das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

# Fachanwalt Strafrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Strafrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Strafrecht. Orientierung StPO StGB Nebenstrafrecht. Strafverteidigung Ermittlungsverfahren Hauptverhandlung Berufung Revision Verfassungsbeschwerde plus tägliche Prozessführung: Fristen, Aktenlog, Haft, Akteneinsicht, HV-Organisation, Anträge, Mandantenkommunikation, Rechtsmittel, Vollstreckung. Ergaenzt aktenaufbereiter-strafrecht und kanzlei-allgemein.

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

### 3a. Strafprozess-Operations-Modus

Wenn der Nutzer nicht nur eine Rechtsfrage stellt, sondern eine laufende Strafakte führen will, schalte sofort in den Operations-Modus. Der Skill behandelt die Akte wie ein lebendes Verteidigungsprojekt: Heute sichern, morgen vorbereiten, nächste Woche sauber nachhalten.

**Priorität bei jeder Strafakte:**

1. **Freiheit und Frist:** U-Haft, Vorführung, Durchsuchung, Vernehmungstermin, Strafbefehl, Urteil, Beschluss, Rechtsmittel, Zustellung.
2. **Akte und Beweise:** Akteneinsicht, Nachlieferungen, Sonderbände, digitale Datenträger, Asservate, Gutachten, Zeugen, Protokolle.
3. **Mandant und Kommunikation:** Schweigerecht, Verhalten gegenüber Polizei/StA/Gericht, Familie/Arbeitgeber/Presse/Social Media, Haftbesuch.
4. **Hauptverhandlung:** Tagesmappe, Sitzungsplan, Einlassung, Fragelisten, Beweisanträge, Widersprüche, Protokollierung, Revisionssicherung.
5. **Abschluss:** Urteil, Rechtsmittelentscheidung, Bewährung, Auflagen, Zahlungen, Vollstreckung, Führungszeugnis, Mandantenbrief.

**Standardausgabe im Operations-Modus:**

- **Heute zuerst:** [ein bis drei zwingende Handlungen]
- **Fristen/Wiedervorlagen:** [Datum, Norm, Verantwortlicher, Vorfrist]
- **Aktenlog:** [neuer Eingang, Bedeutung, fehlende Teile]
- **Verteidigungslinie:** [aktuelle Arbeitsannahme, nicht endgültige Bewertung]
- **Nächster Skill:** `strafprozess-cockpit-taegliche-kanzleifuehrung` oder spezieller Strafprozess-Skill
- **Eine Rückfrage:** nur wenn ohne sie ein falscher Schritt droht.

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
| `strafprozess-cockpit-taegliche-kanzleifuehrung` | Wenn eine laufende Strafakte nicht nur geprüft, sondern täglich gesteuert werden muss: Verfahrensstand, Fristen, Haft, Akteneinsicht, offene Anträge, Mandantenkommunikation, Termine und nächste Schritte in einer Verteidigungsübersicht. |
| `strafprozess-aktenlog-fristen-und-wiedervorlagen` | Wenn Eingangspost, beA/EGVP, Ladungen, Beschlüsse, Strafbefehle, Urteile oder Nachlieferungen in ein belastbares Fristenbuch und Aufgabenlog überführt werden müssen. |
| `strafprozess-ermittlungsverfahren-sofortmassnahmen` | Wenn Vorladung, Durchsuchung, Beschlagnahme, Festnahme, StA-/Polizeikontakt oder die erste Schweigerechts- und Akteneinsichtsstrategie sofort sitzen müssen. |
| `strafprozess-akteneinsicht-nachlieferungen-und-sonderbaende` | Wenn Akteneinsicht nicht nur beantragt, sondern auf Vollständigkeit, Teilversagung, U-Haft-Mindestinformationen, Sonderbände, Asservate und digitale Beweise kontrolliert werden muss. |
| `strafprozess-pflichtverteidigung-beiordnung-und-wechsel` | Wenn notwendige Verteidigung, Beiordnung, Vorschlagsrecht, Eilbestellung, Verteidigerwechsel oder Entpflichtung operativ durchgesetzt werden sollen. |
| `strafprozess-haft-und-besuchsmanagement` | Wenn U-Haft, Haftprüfung, Haftbeschwerde, Haftverschonung, Besuch, Telefon, Post, Familie, Arbeitgeber und Beschleunigungskontrolle parallel organisiert werden müssen. |
| `strafprozess-hv-tagesmappe-und-sitzungsplan` | Wenn eine Hauptverhandlung als Arbeitstag vorbereitet wird: Zeitplan, Zeugenprogramm, Fragelisten, Einlassungsentscheidung, Antragsentwürfe, Pausenstrategie und Nachbereitung. |
| `strafprozess-antragslog-beweisantraege-und-widerspruch` | Wenn Beweisanträge, Beweisermittlungsanträge, Widersprüche, § 257-StPO-Erklärungen, Ablehnungsbeschlüsse und Revisionssicherung sauber nachgehalten werden müssen. |
| `strafprozess-sitzungsprotokoll-und-revisionssicherung` | Wenn während oder nach der Hauptverhandlung Protokollierung, Verständigung, Belehrungen, Anträge, letztes Wort und mögliche Revisionsrügen gesichert werden müssen. |
| `strafprozess-mandantenkommunikation-und-instruktionen` | Wenn der Mandant klare, knappe Verhaltensanweisungen zu Schweigen, Vernehmung, Haft, Hauptverhandlung, Arbeitgeber, Presse, Social Media oder Bewährung braucht. |
| `strafprozess-rechtsmittel-und-notfristencockpit` | Wenn Strafbefehl, Berufung, Revision, sofortige Beschwerde, einfache Beschwerde, Wiedereinsetzung, Zustellung oder Empfangsbekenntnis fristensicher bearbeitet werden müssen. |
| `strafprozess-verhandlungslog-sta-gericht-nebenklage` | Wenn Gespräche mit Staatsanwaltschaft, Gericht, Nebenklage, Bewährungshilfe oder Sachverständigen dokumentiert und taktisch sauber weitergeführt werden müssen. |
| `strafprozess-abschluss-urteil-bewaehrung-vollstreckung` | Wenn nach Urteil, Einstellung oder Verständigung Rechtsmittel, Bewährung, Auflagen, Zahlungen, Vollstreckung, Führungszeugnisfolgen und Aktenabschluss organisiert werden müssen. |
| `strafrecht-spezial-188-stgb-easy-verteidigung` | Wenn es um Anzeige, Anhörung, Strafbefehl oder Anklage wegen § 188 StGB geht und schnell eine handliche Verteidigungslinie gegen den Vorwurf der Politikerbeleidigung gebraucht wird. |
| `strafrecht-spezial-188-stgb-anklage-und-strafbefehl` | Wenn ein förmliches Dokument vorliegt und Fristen, Einspruch, § 199-StPO-Erwiderung, Eröffnungsangriff oder Einstellungsanregung gebaut werden müssen. |
| `strafrecht-spezial-188-stgb-social-media-beweise` | Wenn der Vorwurf aus X, Facebook, Instagram, TikTok, Telegram, WhatsApp, Blog, Video oder Screenshot stammt und Kontext, Reichweite und Account-Zuordnung entscheidend sind. |
| `strafrecht-spezial-188-stgb-art5-schrift-und-hv` | Wenn Art. 5 GG, § 193 StGB, Machtkritik, Deutung, Hauptverhandlung, Zeugenfragen oder Plädoyer bei § 188 StGB sauber herausgearbeitet werden sollen. |
| `akteneinsicht-strafrecht-auswerten` | Strukturierte Auswertung der Strafakte nach Akteneinsicht § 147 StPO. Erstellt Beweismittelverzeichnis (Urkunden Augenscheinsobjekte Zeugen Sachverständige) Personenregister Chronologie Aussagen-Synopse mit… |
| `erstgespraech-mandatsannahme` | Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen. § 136 StPO… |
| `fachanwalt-strafrecht-adhaesionsverfahren` | Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess. §§ 403-406c StPO… |
| `fachanwalt-strafrecht-akteneinsicht-beantragen` | Akteneinsicht § 147 StPO sauber beantragen und gegen Teilversagung absichern: Verteidigerrecht, U-Haft-Mindestinformationen, nicht verteidigter Beschuldigter, Verletzteneinsicht, elektronische Akte und gerichtliche Entscheidung. |
| `fachanwalt-strafrecht-anklage-reaktion` | Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverfahren: Anwendungsfall Mandant hat Anklageschrift erhalten und Verteidiger muss strategisch auf Eroeffnungsverfahren reagieren. § 199 StPO… |
| `fachanwalt-strafrecht-chatcontrol-csam-anwaltsgeheimnis-53-stpo` | Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prüft ob Chat-Control-Massnahmen Anwaltsgeheimnis verletzen oder Mandatskommunikation abhoeren koennten. § 53 StPO… |
| `fachanwalt-strafrecht-einlassung-vorbereiten` | Schriftliche Einlassung des Beschuldigten vorbereiten oder Schweigen § 136 StPO. Schweigerecht ist Grundrecht und darf nicht nachteilig gewertet werden BGH st. Rspr. Aber Teilschweigen kann gewürdigt werden. Strategie… |
| `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` | Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidiger muss Hauptverhandlung strukturiert vorbereiten mit Einlassung Beweisanträgen und Verfahrenstaktik. § 136 StPO Schweigerecht, § 244 StPO… |
| `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` | Insolvenzantrag-Massnahmen durch Staatsanwaltschaft im Wirtschaftsstrafrecht: Anwendungsfall Staatsanwaltschaft hat Insolvenzantrag gestellt oder Vermögenswerte beschlagnahmt und Verteidiger muss reagieren. § 283 StGB… |
| `fachanwalt-strafrecht-nebenklage-opfervertretung` | Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straftat moechte als Nebenklaeger am Verfahren teilnehmen und anwaltliche Vertretung benoetigen. §§ 395-406h StPO Nebenklage, § 403 StPO… |
| `fachanwalt-strafrecht-orientierung` | Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden. § 136 StPO Belehrung, § 137… |
| `fachanwalt-strafrecht-untersuchungshaft-haftpruefung` | Untersuchungshaft und Haftprüfung nach §§ 112 ff. StPO: Anwendungsfall Mandant wurde verhaftet und Strafverteidiger muss Haftbefehl anfechten oder Haftprüfungsantrag stellen. §§ 112-113 StPO Haftgründe Fluchtgefahr… |
| `fachanwalt-strafrecht-verstaendigung-257c-toa-46a` | Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a StGB vorbereiten: Anwendungsfall Strafverteidiger prüft ob Einigung durch Deal Einstellung oder TOA für Mandanten vorteilhaft ist. § 257c StPO Verständigung… |
| `fachanwalt-strafrecht-wahlverteidiger-mandat` | Wahlverteidiger-Mandat im Strafrecht beginnen: Anwendungsfall Beschuldigter waehlt Strafverteidiger und Erstgespraeach muss Schweigerecht Akteneinsicht Honorar und Strategie klaeren. § 136 StPO Schweigerecht… |
| `fachanwalt-strafrecht-zeugenbeistand` | Zeugenbeistand im Strafverfahren für Zeugen mit eigenem Rechtsinteresse: Anwendungsfall Person ist als Zeuge geladen hat aber eigenes Aussageverweigerungsrecht oder Selbstbelastungsrisiko und benoetigt anwaltlichen… |
| `mandat-triage-strafrecht` | Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug… |
| `plaedoyer-vorbereitung-strafverteidigung` | Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen. §§ 410 ff. StPO… |
| `vergleichsverhandlung-strategie` | Verhandlungs- und Einigungsstrategie im Strafverfahren: Anwendungsfall Sachverhalt eignet sich für prozessuale Einigung und Strafverteidiger will Verständigung Einstellung oder TOA vorbereiten. § 257c StPO… |

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

## 2. `strafr-haftpruefung-haftbeschwerde-workflow`

**Fokus:** Haftpruefung und Haftbeschwerde §§ 117 ff. StPO: dringender Tatverdacht, Haftgrund, Verhaeltnismaessigkeit, Sechsmonatspruefung. Mustertext Haftpruefungsantrag und Haftbeschwerde.

# StrafR: Haftpruefung-Workflow

## Spezialwissen: StrafR: Haftpruefung-Workflow
- **Normen-/Quellenanker:** StPO.

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

## 3. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-strafrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieses Modul bearbeitet: Chronologie und Belegmatrix im Plugin fachanwalt-strafrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen..

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

## 4. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-strafrecht: macht aus Strafbefehl, Urteil, Beschluss, Ladung, Haftbefehl, beA-/EGVP-Eingang oder Aktennachlieferung eine Sofortampel für Frist, Zuständigkeit, U-Haft, Rechtsmittel, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin fachanwalt-strafrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Strafverteidigung-Fristen-Speziallage
- **Einspruch Strafbefehl § 410 StPO: 2 Wochen** ab Zustellung.
- **Berufung § 314 StPO: 1 Woche** ab Verkuendung; Begruendung freiwillig, aber empfohlen.
- **Revision §§ 341, 345 StPO:** Einlegung binnen 1 Woche; Revisionsanträge und Begründung grundsätzlich binnen 1 Monat nach Ablauf der Einlegungsfrist, bei späterer Urteilszustellung ab Zustellung; Verteidiger-/Anwaltsunterschrift für die Begründung beachten.
- **Beschwerde § 311 StPO: 1 Woche** ab Zustellung (sofortige Beschwerde) bzw. unbefristet (einfache Beschwerde § 304 StPO).
- **U-Haft:** Haftprüfung nach § 117 StPO jederzeit beantragbar; mündliche Verhandlung nach §§ 118, 118a StPO prüfen; Haftbeschwerde als Beschwerde nach § 304 StPO einordnen; OLG-Haftprüfung nach sechs Monaten § 121 StPO vormerken.
- **Klageerzwingungsverfahren § 172 StPO:** Beschwerde 2 Wochen, Antrag OLG 1 Monat ab Bescheid GenStA.
- **Akteneinsicht § 147 StPO:** Verteidigerrecht nach Abs. 1; im laufenden Ermittlungsverfahren nur bei konkreter Gefährdung des Untersuchungszwecks einschränkbar; bei U-Haft oder beantragter vorläufiger Festnahme sind haftrelevante Informationen in geeigneter Weise zugänglich zu machen, regelmäßig durch Akteneinsicht (§ 147 Abs. 2 S. 2 StPO).
- **Notwendige Verteidigung §§ 140-141 StPO:** sofort bei U-Haft, Verbrechen, Hauptverhandlung Schwurgericht; Pflichtverteidigerbestellung.
- **Wiedereinsetzung § 44 StPO:** 1 Woche ab Wegfall, Bewilligung unanfechtbar.
- **Risikoampel:** Rot bei Frist Rechtsmittel, U-Haft, drohendem Bewaehrungswiderruf § 56f StGB; Gelb bei unklarer Beweislage; Gruen bei dokumentierter Strategie.

## 5. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin fachanwalt-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Strafrecht-Mandantenkommunikation Speziallage
- **Pflicht-Hinweise im Strafrecht**: § 137 StPO Mandat als Verteidiger; § 43a Abs. 2 BRAO Mandantengeheimnis (Schweigerecht / -pflicht des Verteidigers § 53 I Nr. 2 StPO); klare Belehrung zur Eigenbelastungsfreiheit nemo tenetur Art. 2 i.V.m. 1 I GG.
- **Aussageverhalten** dokumentieren: ausdruecklich raten zur Verweigerung der Aussage bis vollstaendige Akteneinsicht (§ 136 I 2 StPO Schweigerecht); keine telefonischen Angaben gegenueber Polizei ohne Vorbereitung.
- **Strategie-Entscheidungen** brauchen Mandantenfreigabe vorab und schriftlich: Strafbefehl Einspruch / Verteidigungslinie / Gestaendnisbereitschaft / Verstaendigung § 257c StPO / TOA § 46a StGB / Rechtsmittelverzicht.
- **Kosten transparent machen:** RVG-Verguetung (insb. Hauptverhandlungstermine, Akteneinsicht VV 4100 ff. RVG); Honorarvereinbarung § 3a RVG schriftlich; Pflichtverteidigung §§ 140-141 StPO Kostenfolgen Mandant bei Verurteilung.
- **Haftbesuch / Verteidigergespraech in JVA:** schriftliche Vorbereitung; bei U-Haft ungestoerter Verteidigerkontakt § 148 StPO (Ausnahme: Untersagung bei §§ 129a, 129b StGB Verdacht).
- **Schweigepflichtentbindung** für Aerzte/Therapeuten nur eng abgrenzen.
- **Sprachbarriere**: Dolmetscher § 187 GVG zwingend; bei Auslaender Pflichtverteidigerbestellung § 140 II StPO erweitert.
