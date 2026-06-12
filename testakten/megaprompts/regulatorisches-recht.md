# Megaprompt: regulatorisches-recht

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `regulatorisches-recht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Regulatorisches Recht (Sektoren): ordnet Rolle (Unternehmen reguliert, Aufsichtsbehörde…
2. **aufsichtsrecht-erstpruefung-und-mandatsziel** — Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel.
3. **anschluss-router** — Einstieg, Schnelltriage und Fallrouting im Regulatorisches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken…
4. **aufsichts-feed-monitor** — Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifiziere…
5. **dora-ikt-vertragspruefung** — IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. …
6. **inkasso-rdg-luecken-mar-mifid** — Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 1…
7. **luecken** — Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zusta…
8. **luecken-aufzeiger** — Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG…
9. **mandat-arbeitsbereich** — Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfan…
10. **regrecht-einfuehrung-sektoren** — Einfuehrung regulatorisches Recht in den wichtigsten Sektoren: Bank, Versicherung, Energie, Telekommunikation, Verkehr, …
11. **regulatorisches-richtlinien-neufassung** — Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG …
12. **richtlinien-anhoerung-red-aufsichtsrecht** — Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. P…
13. **richtlinien-neufassung** — Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk.…
14. **stellungnahmen** — Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prü…
15. **ustva-aufsichtskommunikation-grundregeln-dora** — Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen …

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Regulatorisches Recht (Sektoren): ordnet Rolle (Unternehmen reguliert, Aufsichtsbehörde, Verbraucher/Kunden), markiert Frist (Beschwerdefrist Aufsichtsbescheid), wählt Norm (TKG, EnWG, KWG, VersAufsG, AMG, Branchen-Spezialgesetze) und Zuständigkeit (BNetzA), leite..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Regulatorisches Recht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anhoerung-red-team-und-qualitaetskontrolle` — Anhoerung RED Team und Qualitaetskontrolle
- `anschluss-router` — Anschluss Router
- `aufsichts-feed-monitor` — Aufsichts Feed Monitor
- `aufsichtskommunikation-grundregeln` — Aufsichtskommunikation Grundregeln
- `aufsichtsrecht-erstpruefung-und-mandatsziel` — Aufsichtsrecht Erstpruefung und Mandatsziel
- `aufsichtssanktion-revision-spezial` — Aufsichtssanktion Revision Spezial
- `aufsichtsverfahren-anhoerung-gwg` — Aufsichtsverfahren Anhoerung GWG
- `aufsichtsverfahren-formular-portal-und-einreichung` — Aufsichtsverfahren Formular Portal und Einreichung
- `dora-ikt-vertragspruefung` — Dora IKT Vertragspruefung
- `dora-stellvertreter-und-konzern` — Dora Stellvertreter und Konzern
- `enwg-feeds-heilmwerbg` — ENWG Feeds Heilmwerbg
- `feeds-compliance-dokumentation-und-akte` — Feeds Compliance Dokumentation und Akte
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Regulatorisches Recht sind EnWG, GwG, HeilMWerbG, KWG, RDG, TKG, WpHG, ZAG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `aufsichtsrecht-erstpruefung-und-mandatsziel`

_Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel._

# Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Aufsichtsrecht Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Regulatorisches Recht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 1 Abs. 1 KWG` — Bankgeschaefte.
- `§ 32 Abs. 1 KWG` — Erlaubnispflicht.
- `§ 25a Abs. 1 KWG` — ordnungsgemaesse Geschäftsorganisation.
- `§ 44 Abs. 1 KWG` — Auskunfts- und Pruefungsrechte.
- `§ 1 Abs. 1 ZAG` — Zahlungsdienste.
- `§ 10 Abs. 1 ZAG` — Erlaubnis Zahlungsinstitut.
- `Art. 16 DORA` — vereinfachter IKT-Risikomanagementrahmen.
- `Art. 28 DORA` — IKT-Drittparteienrisiko.
- `§ 675f BGB` — Zahlungsdiensterahmenvertrag.
- `§ 765 BGB` — Bürgschaft.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Aufsichtsrecht: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, RDG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aufsichtsrecht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `anschluss-router`

_Einstieg, Schnelltriage und Fallrouting im Regulatorisches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenstän..._

# Regulatorisches Recht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Regulatorisches Recht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest.

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
| `aufsichts-feed-monitor` | Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist… |
| `dora-ikt-vertragspruefung` | IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. 28 30 DORA VO (EU) 2022/2554. Prüfraster: Pflichtklauseln Art. 30 DORA Ausstiegsstrategien… |
| `inkasso-rdg` | Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg… |
| `luecken` | Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit… |
| `luecken-aufzeiger` | Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG Art. 12 80 AEUV Art. 107. Prüfraster: Normtext Regelungsziele Luecken unbeabsichtigte Folgen… |
| `regulatorisches-recht-anpassen` | Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf.… |
| `regulatorisches-recht-kaltstart-interview` | Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen. KWG WpHG DORA VAG GwG. Prüfraster: Branche Regulierungsrahmen Sachverhalt Fristen Pflichten Risiko. Output: Mandatssteckbrief Normenkarte… |
| `regulatorisches-recht-mandat-arbeitsbereich` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behörden. Output: Mandatssteckbrief Arbeitsplan… |
| `richtlinien-neufassung` | Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg.… |
| `richtlinien-vergleich` | Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der… |
| `stellungnahmen` | Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege… |
| `ustva` | Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse… |

## Worum geht es?

Dieses Plugin deckt das Aufsichtsrecht für regulierte Unternehmen ab — Banken, Zahlungsdienstleister, Wertpapierdienstleister, Energieversorger, Telekommunikationsunternehmen, Inkassodienstleister und weitere Sektoren. Es unterstuetzt bei Mandatsaufnahme, Richtlinienpflege, Regulierungsluecken-Analyse, Compliance-Dokumentation und Stellungnahmen gegenueber Behörden.

Im Mittelpunkt stehen das Kreditwesengesetz (KWG), das Zahlungsdiensteaufsichtsgesetz (ZAG), das Wertpapierhandelsgesetz (WpHG), das Geldwaeschegesetz (GwG), die DORA-Verordnung, das EnWG und das TKG. Das Plugin eignet sich für Rechtsanwaelte, Compliance-Beauftragte und Unternehmensjuristen, die in regulierten Branchen beraten.

## Wann brauchen Sie diese Skill?

- Ein Finanzunternehmen muss pruefen, ob ein neues Geschaeftsmodell einer BaFin-Erlaubnis nach KWG oder ZAG bedarf.
- Eine Kanzlei bereitet eine Stellungnahme zu einem neuen Regulierungsvorhaben vor.
- Ein Unternehmen will interne Compliance-Richtlinien nach DORA, MaRisk oder WpHG aktualisieren.
- Ein Inkassounternehmen fragt, ob seine Taetigkeiten unter das RDG fallen.
- Ein reguliertes Unternehmen beobachtet neue BaFin- oder EBA-Veroeffentlichungen und will relevante Aenderungen schnell identifizieren.

## Fachbegriffe (kurz erklaert)

- **KWG** — Kreditwesengesetz; regelt die Zulassung und Beaufsichtigung von Kreditinstituten und Finanzdienstleistungsinstituten.
- **ZAG** — Zahlungsdiensteaufsichtsgesetz; setzt die PSD2-Richtlinie um und regelt Zahlungsinstitute.
- **WpHG** — Wertpapierhandelsgesetz; regelt Wohlverhaltenspflichten, Maerkte und Produktueberwachung.
- **DORA** — Digital Operational Resilience Act (EU-VO 2022/2554); Anforderungen an digitale Betriebsstabilitaet und IKT-Drittanbietervertraege für Finanzunternehmen.
- **MaRisk** — Mindestanforderungen an das Risikomanagement der BaFin; konkretisiert § 25a KWG.
- **RDG** — Rechtsdienstleistungsgesetz; regelt, wer aussergerichtliche Rechtsdienstleistungen erbringen darf, insbesondere Inkasso.
- **GwG** — Geldwaeschegesetz; Pflichten für Verpflichtete (Banken, Rechtsanwaelte, Immobilienmakler u. a.) zur Geldwaeschepraeventition.
- **BaFin** — Bundesanstalt für Finanzdienstleistungsaufsicht; zuständige Behörde für KWG, ZAG und WpHG.

## Rechtsgrundlagen

- § 1 KWG (Begriffsbestimmungen Bankgeschaefte und Finanzdienstleistungen)
- §§ 1 ff. ZAG (Zahlungsdienste, Erlaubnispflicht)
- §§ 63 ff. WpHG (Wohlverhaltenspflichten)
- §§ 1 ff. GwG (Verpflichtete, Sorgfaltspflichten)
- Art. 1 ff. DORA-VO EU 2022/2554 (IKT-Risikomanagement)
- §§ 2 ff. RDG (Zulaessige Rechtsdienstleistungen)
- § 25a KWG i. V. m. MaRisk (Risikomanagement)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Branche, Regulierungsrahmen und konkretes Rechtsproblem bestimmen.
2. Mandat strukturieren und Arbeitsbereich abgrenzen (Skill `regulatorisches-recht-kaltstart-interview` oder `regulatorisches-recht-mandat-arbeitsbereich`).
3. Passenden Fachskill auswaehlen (z. B. DORA, Inkasso, Richtlinien, Lueckenanalyse).
4. Eilfristen und Meldepflichten pruefen (Aufsichtsfristen koennen kurz sein).
5. Anschluss-Skill bestimmen (z. B. Richtlinie anpassen oder Stellungnahme verfassen).

## Skill-Tour (was gibt es hier?)

- `aufsichts-feed-monitor` — Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren.
- `dora-ikt-vertragspruefung` — IKT-Drittanbietervertraege auf DORA-Konformitaet pruefen für Finanzunternehmen, die digitale Dienstleistungen einkaufen.
- `inkasso-rdg` — Inkasso- und Rechtsdienstleistungserlaubnis nach RDG pruefen, wenn gewerbliche Forderungseinziehung betrieben wird.
- `luecken` — Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren (KWG, WpHG, DORA, VAG, GwG).
- `luecken-aufzeiger` — Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen.
- `regulatorisches-recht-anpassen` — Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen.
- `regulatorisches-recht-kaltstart-interview` — Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen.
- `regulatorisches-recht-mandat-arbeitsbereich` — Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen.
- `richtlinien-neufassung` — Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen.
- `richtlinien-vergleich` — Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen.
- `stellungnahmen` — Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen.
- `ustva` — Umsatzsteuervoranmeldung im regulatorischen Kontext pruefen für Finanzunternehmen oder regulierte Entitaeten mit USt-Fragen.

## Worauf besonders achten

- Regulatorische Pflichten aendern sich haeufig: EBA-Guidelines, BaFin-Rundschreiben und neue EU-Verordnungen koennen Bestandsregelungen kurzfristig ueberlagern.
- KWG und ZAG-Erlaubnisse sind vorgelagert — kein Geschaeft ohne Erlaubnis starten.
- DORA gilt ab 17.01.2025 für alle in Art. 2 DORA genannten Finanzentitaeten; IKT-Drittanbietervertraege muessen nachgeruestet werden.
- Inkasso-Taetigkeiten ohne RDG-Registrierung sind strafbewehrt (§ 20 RDG).
- Sektorspezifische Normen (EnWG, TKG) haben eigene Aufsichtsstrukturen (BNetzA) neben BaFin — Zustaeindigkeit immer klaeren.

## Typische Fehler

- Erlaubnispflicht nach KWG oder ZAG uebersehen: Neue Geschaeftsmodelle (z. B. Krypto, Buy-now-pay-later) werden ohne Vorab-Pruefung gestartet.
- DORA nur als IT-Thema behandelt: Vertragliche Anforderungen an IKT-Drittanbieter werden von der Rechtsabteilung nicht koordiniert.
- Luecken in Compliance-Richtlinien nach Gesetzesaenderungen nicht nachgepflegt: Alte MaRisk-Version oder veraltete GwG-Interna bleiben im Einsatz.
- Fristen für Stellungnahmen zu Konsultationsverfahren verpasst: Europ. Behörden (EBA, ESMA) setzen kurze Fristen.
- Inkasso und Rechtsberatung nicht sauber getrennt: RDG-Grenze wird ueberschritten.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- DORA-VO EU 2022/2554 anwendbar ab 17.01.2025
- MaRisk-Novelle 2023 der BaFin

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 UStG
- § 25a KWG
- § 4 RDGEG
- § 13d RDG
- § 203 StGB
- Art. 288 AEUV
- § 25b KWG
- § 1 ZAG
- § 13 RDG
- § 10 ZAG
- Art. 80 AEUV
- § 17 UStG

### Leitentscheidungen

- EuGH C-6/64
- EuGH C-117/20

---

## Skill: `aufsichts-feed-monitor`

_Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist Handlungsbedarf Meldepflicht. Output: Monitoring-Bericht relevante Aenderungen Handlun..._

# Regulatorischer Feed-Watcher

## Eingaben

- **Watchlist:** Welche Behörden und Rechtsgebiete sind zu überwachen?
- **Wesentlichkeitsschwellenwert:** Wie ist Materialität konfiguriert?
- **Prüfzeitraum:** Seit wann? (Standard: seit letztem Lauf; alternativ `--since DATUM`)
- **Quellen:** Konfigurierte Feeds, RSS-Adressen, Dienste.
- **Alternativ:** Manuell eingefügter Regulierungstext zur Einzelklassifikation.

## Rechtlicher Rahmen

### Kernvorschriften

- **BGBl.** — amtliches Verkündungsblatt; maßgeblich für Inkrafttreten von Normen.
- **ABl. EU, Reihe L + C** — verbindliche EU-Rechtsakte und Leitlinien.
- **BaFin-Rundschreiben** (z. B. MaRisk BA 2023, BAIT, ZAIT) — konkretisieren
 aufsichtsrechtliche Anforderungen; §§ 6, 25b KWG, §§ 6, 23 VAG, §§ 6 ff. WpHG.
- **BSI** — Technische Richtlinien und Kritis-Verlautbarungen (§§ 8a ff. BSIG).
- **EU-KI-VO (VO (EU) 2024/1689)** — Hochrisiko-Klassifikation, Konformitätspflichten.
- **CSRD (RL (EU) 2022/2464)** — nichtfinanzielle Berichterstattung, ESRS-Standards.
- **Art. 20 Abs. 3 GG** — Rechtsstaatsprinzip, Normenklarheit; Maßstab für die
 Bewertung behördlicher Verlautbarungen ohne formelle Ermächtigungsnorm.

### Leitentscheidungen / Aktualitäts-Anker

Stand 05/2026. Vor Verwendung im Schriftsatz live verifizieren — keine Aktenzeichen aus Modellwissen.

- EuGH, Urt. v. 13.02.2025 — C-383/23 (ILVA) — DSGVO-Bußgelder können auf gesamten Konzernumsatz bezogen werden; "Unternehmen" im wettbewerbsrechtlichen Sinne — relevant für Monitoring nationaler Bußgeldpraxis.
- EuGH, Urt. v. 02.12.2025 — C-492/23 (Russmedia) — DSGVO geht DSA vor; kein Provider-Privileg bei DSGVO-Verstößen — relevant für Plattform-Compliance-Monitoring.
- EuGH, Urt. v. 19.03.2026 — C-526/24 (Brillen Rottler) — Erstmaliger DSGVO-Auskunftsantrag kann rechtsmissbräuchlich sein.
- BVerfG-Linien zu Wesentlichkeit und Normenklarheit (BVerfGE 33, 125; 49, 89 — Kalkar) im Mandat über [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) live verifizieren.
- DORA-Aktualisierungen 2025/2026: ESA-Liste kritischer IKT-Drittdienstleister (November 2025); BaFin DORA-Informationsregister-Frist 09.–30.03.2026.
- AMLR (EU) 2024/1624 — Anwendbarkeit ab 10.07.2027; AMLA-Behörde mit Sitz in Frankfurt seit 01.07.2025 operativ.
- KI-VO (EU) 2024/1689 — Verbote anwendbar seit 02.02.2025; GPAI ab 02.08.2025; Hochrisiko-KI-Hauptanwendung ab 02.08.2026; Sicherheitsbauteile ab 02.08.2027.

### Kommentare

- `Sachs (Hrsg.), GG, 10. Aufl. 2021, Art. 20 Rn. 78 ff.` — Rechtsstaatsprinzip
 und Normenklarheit als Bewertungsmaßstab für behördliche Verlautbarungen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Rechtsetzungskompetenzen; relevant für Verbindlichkeitsgrad von BaFin-Rundschreiben.
- `Schwennicke/Auerbach (Hrsg.), KWG/CRR, 4. Aufl. 2022, § 6 KWG Rn. 5 ff.`
 — Praxis der BaFin-Verlautbarungen und deren Rechtswirkung.

## Ablauf

### Schritt 0: Lückenprüfung

Watchlist und Quellkonfiguration gegen den internen Quellkatalog prüfen. Besteht eine
offensichtliche Lücke (z. B. "BaFin" in der Watchlist, aber weder Bundesanzeiger noch
BaFin-Journal konfiguriert), einmalig hinweisen — nicht wiederholen, wenn die Lücke
bekannt und akzeptiert ist.

### Schritt 1: Abruf

| Quelle | Inhalte |
|---|---|
| BGBl. (bgbl.de) | Gesetze, Verordnungen |
| ABl. EU / EUR-Lex | EU-Rechtsakte, konsolidierter Bestand |
| BaFin (bafin.de/RSS) | Rundschreiben, Merkblätter, Allgemeinverfügungen |
| BSI (bsi.bund.de) | Technische Richtlinien, Kritis-Warnungen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich |
| BMJ | Referentenentwürfe, Pressemitteilungen |
| Bundesrat | Drucksachen, Stellungnahmen |
| Bundesanzeiger | Behördenbekanntmachungen |

Kostenpflichtige Dienste (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang Premium, Wolters Kluwer) werden genutzt,
wenn konfiguriert. Duplikate ebenenübergreifend entfernen.

**Keine stille Ergänzung.** Bei wenigen Treffern keine eigenständige Webrecherche —
Optionen dem Nutzer vorlegen (Zeitfenster, andere Quelle, Websuche mit Prüfvermerk,
stoppen). Die Entscheidung trifft der Nutzer.

**Quellenkennung** (nie entfernen): `[BGBl.]`, `[ABl. EU]`, `[BaFin-RSS]`, `[BSI]`,
`[Websuche — prüfen]`, `[Modell-Wissen — prüfen]`, `[manuell eingegeben]`.
Sekundärquellen (Kanzlei-Newsletter, Fachportale) zusätzlich mit `[Sekundärquelle]`
kennzeichnen; Materialitätsstufe absenken bis zur Primärquellenbestätigung.

### Schritt 2: Klassifikation

| Eintragstyp | Einordnung |
|---|---|
| Gesetz / Verordnung (final) | Immer wesentlich |
| Referentenentwurf / Konsultationsdokument | Prüfenswert — Kommentierungsfrist festhalten |
| Enforcement / Bußgeldbescheid | Sektorentreffer → wesentlich; Themennähe → prüfenswert |
| Leitlinien / Merkblätter | Prüfenswert |
| Pressemitteilungen / Statements | Zur Kenntnis / überspringen |

Referentenentwürfe und Konsultationen nie als "immer wesentlich" einstufen — noch keine
Compliance-Pflicht. Im Eintrag explizit vermerken: "Vorstufe. Kommentierungsfrist
[Datum]. Noch keine Compliance-Lücke."

### Schritt 3: Anreicherung

Für jeden Eintrag oberhalb "Zur Kenntnis": einzeilige Zusammenfassung + Relevanzhinweis
+ Link + Inkrafttreten bzw. Kommentierungsfrist. "Zur Kenntnis"-Einträge: nur Anzahl.

## Regulatorischer Feed-Check — [Datum]
Zeitraum: [letzter Lauf] – [jetzt] | Quellen: [...] | Einträge: [N]

### Kurzfazit
[N Einträge erfordern Handlung bis [Datum] — Top 3: X, Y, Z]

### Immer wesentlich
**[Behörde] — [Titel]**
[Zusammenfassung]. [Relevanz]. In Kraft: [Datum]. [Link] [Quellenkennung]
→ Empfehlung: [nächster Schritt]

### Prüfenswert
**[Behörde] — [Titel]**
[Zusammenfassung]. Kommentierungsfrist: [Datum]. [Link] [Quellenkennung]

### Zur Kenntnis
[N] Einträge — [Titelliste mit Links]

---
Letzter Prüfzeitpunkt: [Zeitstempel]
Fundstellen vor Verwendung verifizieren. Abgleich mit Primärquelle erforderlich.
```

Zusätzlich Dateiausgabe (Markdown) unter konfiguriertem Pfad oder
`~/regulatorisches-digests/reg-digest-YYYY-MM-DD.md`; bei mehreren Tagesläufen
anhängen statt überschreiben.

## Beispiel

**Watchlist:** "BaFin — Zahlungsdienste", "EU — KI-Verordnung". Letzter Lauf: 01.07.2024.

BaFin-RSS liefert Merkblatt zu § 25b KWG-Auslagerungen → "Prüfenswert" (Leitlinie).
EUR-Lex liefert delegierte Verordnung zur KI-VO → "Immer wesentlich" (EU-Rechtsakt).

```
### Immer wesentlich
**EU — Delegierte Verordnung (EU) 2024/XXX zur KI-Verordnung**
Konkretisiert Konformitätsbewertung für Hochrisiko-KI (Art. 43 KI-VO, Annex III Nr. 5).
In Kraft: 01.08.2024. [ABl. EU L 2024/XXX] [ABl. EU]
→ KI-Inventar gegen Hochrisiko-Katalog prüfen; ggf. Konformitätsbewertung einleiten.
```

## Risiken und typische Fehler

- **Sekundärquelle als Primärquelle verwenden:** Kanzlei-Newsletter berichten über
 Entscheidungen, sind aber nicht die Entscheidung. Immer auf BGBl., ABl. oder
 Behördenwebsite verweisen.
- **Referentenentwurf als geltendes Recht einstufen:** Klare Kennzeichnung als Vorstufe.
- **Kommentierungsfristen übergehen:** Fristen sind real und oft kurz — immer im Tracker.
- **Verbindlichkeitsgrad verwischen:** BaFin-Rundschreiben sind keine Gesetze.
 Unterschied Gesetz / VO / Leitlinie / Merkblatt in der Ausgabe erkennbar halten.
- **Stille Ergänzung durch Websuche:** Ohne Rückfrage unzulässig.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jeder Eintrag muss enthalten: Behörde, Dokumenttyp, Datum, Direktlink zur Primärquelle,
Quellenkennung und ggf. Kommentierungsfrist. Zitierweise Rechtsprechung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Zitierweise Kommentare:
`Sachs/Sachs, GG, 10. Aufl. 2021, Art. 20 Rn. 78`

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 UStG
- § 25a KWG
- § 4 RDGEG
- § 13d RDG
- § 203 StGB
- Art. 288 AEUV
- § 25b KWG
- § 1 ZAG
- § 13 RDG
- § 10 ZAG
- Art. 80 AEUV
- § 17 UStG

### Leitentscheidungen

- EuGH C-6/64
- EuGH C-117/20

---

## Skill: `dora-ikt-vertragspruefung`

_IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. 28 30 DORA VO (EU) 2022/2554. Prüfraster: Pflichtklauseln Art. 30 DORA Ausstiegsstrategien Aufsichtsrechte Subdienstleister Laufzeit Sicherheitsanforderungen. Output: DORA-Vertr..._

# DORA-IKT-Vertragsprüfung

## Zweck

Prüft Verträge mit IKT-Drittdienstleistern, die ein **Finanzunternehmen** i. S. v. Art. 2 DORA (Kreditinstitute, Zahlungs-/E-Geld-Institute, Wertpapierfirmen, Versicherer, Verwalter alternativer Investmentfonds, KVGen, OGAW, Zentralverwahrer, ZGP, Handelsplätze, Krypto-Dienstleister u. a.) abgeschlossen hat oder abschließen will, auf die Anforderungen der **Verordnung (EU) 2022/2554** (Digital Operational Resilience Act – "DORA") sowie der **dazu erlassenen RTS/ITS und EBA-/ESA-Leitlinien**.

Ergebnis ist eine tabellarische Lückenanalyse mit:

- Klauseltext (Ist),
- DORA-Anker (Soll),
- Lückenbewertung (konform / teilkonform / nicht konform / fehlt),
- konkretem Verbesserungsvorschlag inkl. Klausel-Entwurf,
- Kritikalitäts-Score (1 = niedrig … 5 = "kritisch oder wichtig" i. S. v. Art. 28 III DORA, § 28 BaFin-Auslegungshilfe).

Anwendungsfälle: Vertragsanbindung eines neuen IKT-Dienstleisters; Re-Papering bestehender Cloud-/SaaS-/Outsourcing-Verträge zum Geltungsbeginn 17. Januar 2025; ad-hoc-Prüfung im Rahmen einer BaFin-Sonderprüfung nach § 44 KWG / § 306 VAG.

## Eingaben

1. **Vertragsdokument** (PDF/DOCX/MD) inkl. aller Anlagen, SLAs, DPAs, Sub-Outsourcing-Listen.
2. **Klassifikation der Funktion** (kritisch / wichtig / sonstige) gem. Art. 28 II DORA i. V. m. RTS (Delegierte VO (EU) 2024/1773).
3. **Finanzunternehmens-Profil:** Aufsichtsregime (KWG, ZAG, KAGB, VAG, MiCAR), Größe (Art. 2 IV DORA – Verhältnismäßigkeitsklausel).
4. **Dienstart:** Cloud (IaaS/PaaS/SaaS), Managed Service, Software-Lizenz, Datenanalyse, Konnektivität.
5. **Datenkategorien:** personenbezogene Daten (DSGVO), Kundengeheimnis (§ 9 KWG / § 311 VAG), Berufsgeheimnis (§ 203 StGB).

## Rechtlicher Rahmen

### Primärrecht
- **DORA-Verordnung:** VO (EU) 2022/2554 v. 14.12.2022, ABl. L 333/1; Geltungsbeginn 17.01.2025 (Art. 64 II).
- **DORA-Änderungs-RL:** RL (EU) 2022/2556 (Anpassung sektoraler Rechtsakte).
- **Art. 28 DORA** – allgemeine Grundsätze für Vertragsvereinbarungen mit IKT-Drittdienstleistern.
- **Art. 29 DORA** – Vorabbewertung des IKT-Konzentrationsrisikos.
- **Art. 30 DORA** – **Pflichtinhalte** des IKT-Drittdienstleistervertrags.
- **Art. 30 III DORA** – verschärfte Pflichtinhalte bei **kritischen oder wichtigen Funktionen**.
- **Art. 31–44 DORA** – Aufsichtsrahmen kritischer Drittdienstleister (Lead Overseer ESA).

### Tertiärrecht / RTS / ITS
- Delegierte VO (EU) 2024/1773 v. 13.03.2024 (RTS zu Subunternehmer-Ketten, Art. 30 V DORA).
- Delegierte VO (EU) 2024/1772 (RTS Klassifizierung schwerwiegender IKT-Vorfälle).
- Delegierte VO (EU) 2024/1505 (ergänzende RTS-Pakete der ESAs).
- DurchführungsVO (EU) 2024/2956 (ITS zum Informationsregister).
- Vollständiger RTS-/ITS-Bestand siehe `references/dora-rechtsquellen.md` und Live-Abruf via EUR-Lex-Connector.

### Soft Law
- ESA Joint Final Reports zu RTS/ITS DORA (JC 2023/Y).
- BaFin-Merkblatt "DORA – Hinweise zur Anwendung", Stand 2024 (laufend aktualisiert).
- EBA Outsourcing Guidelines EBA/GL/2019/02 (für CRR-Institute; durch DORA überlagert, aber Auslegungshilfe).
- EIOPA Outsourcing Guidelines (Versicherungen).
- BaFin BAIT/VAIT/KAIT/ZAIT – soweit nicht durch DORA verdrängt (Stand: BaFin-Konsultation zur Aufhebung 2024/2025).

### Deutsches Aufsichtsrecht (flankierend)
- § 25b KWG (Auslagerung; weiterhin Auffanglinie für Nicht-IKT-Auslagerungen).
- § 24 ZAG; § 32 VAG; § 36 KAGB.
- FISG 2021 (Verschärfung Auslagerungsrecht).
- Datenschutz: Art. 28 DSGVO AVV, § 11 BDSG.

### Leitentscheidungen / Auslegung / Aktualität

Stand 05/2026. DORA ist seit dem 17.01.2025 voll anwendbar. Wichtigste Entwicklungen seit Geltungsbeginn:

- **Liste kritischer IKT-Drittdienstleister:** Die ESAs (EBA, EIOPA, ESMA) haben im November 2025 erstmals 19 kritische IKT-Drittdienstleister benannt (u. a. Amazon, Microsoft, Google). Für diese werden ab 2026 Joint Examination Teams (JET) eingerichtet und Lead Overseers benannt. Aktuelle Liste über die ESA-Webseiten (EBA, ESMA, EIOPA) verifizieren.
- **BaFin DORA-Informationsregister:** Erste Meldefrist 11.04.2025; folgende reguläre Frist BaFin 09.–30.03.2026; Pflichtfelder nach DurchführungsVO (EU) 2024/2956. Aktualität über [bafin.de/DORA](https://www.bafin.de/DE/Aufsicht/DORA/DORA_node.html).
- **BaFin-Auslegungshinweise:** Fachartikel "Im Aufsichtsfokus: Wenn Konzentrationen zum Risiko werden" (BaFin 07.01.2025) und nachfolgende Hinweise zum vereinfachten IKT-Risikomanagementrahmen und Drittparteienrisiken. Live über [bafin.de](https://www.bafin.de) prüfen.

Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Rechtsprechung im Mandat live verifizieren — keine Aktenzeichen aus Modellwissen.

## Ablauf

1. **Dokumentenaufnahme.** Vertrag, Anlagen, DPA, SLA, Sub-Listen einlesen; Funktionsklassifikation (kritisch/wichtig vs. sonstige) festhalten.
2. **Konnektor aufrufen.** EUR-Lex-Connector: aktuellste konsolidierte Fassung VO 2022/2554 inkl. aller Anhänge + delegierter RTS/ITS abrufen (siehe Abschnitt "Konnektor & Datenquellen"). Versionsstand im Output dokumentieren.
3. **Pflichtklausel-Matrix anwenden.** Jede Pflicht aus Art. 30 II DORA (alle Verträge) und Art. 30 III DORA (kritische/wichtige Funktionen) sowie aus den RTS gegen den Vertrag mappen. Vorlage in `references/dora-klauselmatrix.md`.
4. **Lücken markieren.** Für jede Pflicht: zitierte Vertragsstelle (Klausel-Nr., Wortlaut) oder "fehlt"; Bewertung; Kritikalitätsstufe.
5. **Verbesserungsvorschläge formulieren.** Pro Lücke konkreter Klauselentwurf (DE), bei Bedarf EN-Übersetzung; Berücksichtigung Verhältnismäßigkeit Art. 4 DORA.
6. **Sekundärthemen prüfen.** Datenschutz (Art. 28 DSGVO, § 203 III StGB Berufsgeheimnis-Klausel), AGB-Kontrolle (§§ 305 ff. BGB, B2B-Strahlwirkung), § 9 KWG Kundengeheimnis, Exit-/Wiederherstellbarkeit, Subunternehmer-Kette gemäß RTS 2024/1773.
7. **Konzentrationsrisiko (Art. 29).** Wenn Lead-Overseer-Kandidat oder erheblicher Marktanteil: gesonderter Abschnitt mit Konzentrationsanalyse, Multi-Vendor-Empfehlung.
8. **Output erzeugen.** Tabular Review (siehe unten) + Executive Summary für die Geschäftsleitung + Klausel-Patch-Liste für Rechtsabteilung/Procurement.
9. **Aufnahme in Informationsregister.** Hinweis: Pflichtfelder gem. DurchführungsVO 2024/2956 (Register of Information) im Output identifizieren und mappen.

## Konnektor & Datenquellen

| Quelle | Zweck | Aufruf |
| --- | --- | --- |
| EUR-Lex | Konsolidierte Fassung VO (EU) 2022/2554 + Anhänge | `eur-lex://celex/02022R2554-<DATUM>` |
| EUR-Lex | Delegierte VOen 2024/1773, 2024/1772, 2024/1505, 2024/2956 | `eur-lex://celex/32024R1773` etc. |
| ESA-Webseiten | Final Reports / Q&A | https://www.eba.europa.eu, www.esma.europa.eu, www.eiopa.europa.eu |
| BaFin-Newsroom | nationale Auslegungshilfen, FAQ DORA | https://www.bafin.de/dora |
| Bundesanzeiger | nationale Umsetzungsakte FISG/DORA-DurchfG | https://www.bundesanzeiger.de |

Empfohlene MCP-Konnektoren (s. `CONNECTORS.md`):

```jsonc
{
 "mcpServers": {
 "eur-lex": { "command": "node", "args": ["./mcp/eur-lex.js"] },
 "bafin": { "command": "node", "args": ["./mcp/bafin.js"] },
 "esa-feeds": { "command": "node", "args": ["./mcp/esa-feeds.js"] }
 }
}
```

Vor jeder Prüfung: **immer** konsolidierte Fassung der DORA-VO frisch abrufen, Versions-/Stand-Datum in der Output-Kopfzeile mitführen.

## Pflichtklausel-Matrix (Auszug Art. 30 DORA)

| # | DORA-Anker | Pflichtinhalt (Soll) | Geltung |
| --- | --- | --- | --- |
| 1 | Art. 30 II lit. a | Vollständige und genaue Beschreibung aller Funktionen und Dienste, inkl. Sub-Funktionen | alle Verträge |
| 2 | Art. 30 II lit. b | Standorte (Region/Land) der Erbringung und Datenverarbeitung | alle |
| 3 | Art. 30 II lit. c | Verfügbarkeit, Authentizität, Integrität und Vertraulichkeit der Daten | alle |
| 4 | Art. 30 II lit. d | Zugriff, Wiederherstellung und Rückgabe (Exit) personenbezogener und nicht-personenbezogener Daten | alle |
| 5 | Art. 30 II lit. e | Service Level mit klaren Leistungszielen | alle |
| 6 | Art. 30 II lit. f | Unterstützung bei IKT-Vorfällen (mit/ohne Zusatzkosten) | alle |
| 7 | Art. 30 II lit. g | Volle Mitwirkung gegenüber zuständigen Behörden und Resolution Authority | alle |
| 8 | Art. 30 II lit. h | Kündigungsrechte und Mindestkündigungsfristen | alle |
| 9 | Art. 30 II lit. i | Teilnahme an IKT-Sicherheits-Awareness/Trainings (soweit relevant) | alle |
| 10 | Art. 30 III lit. a | Ausführliche Beschreibung Service-Level inkl. Updates, Versionen | nur kritisch/wichtig |
| 11 | Art. 30 III lit. b | Kündigungsfristen + Berichtspflichten zugunsten der Aufsicht | nur kritisch/wichtig |
| 12 | Art. 30 III lit. c | Recht zur **Überwachung der Leistung** des Dienstleisters fortlaufend | nur kritisch/wichtig |
| 13 | Art. 30 III lit. d | Operational and IKT-Sicherheitsanforderungen + Schulung | nur kritisch/wichtig |
| 14 | Art. 30 III lit. e | Beteiligung an **TLPT** (Threat-Led Penetration Testing) gem. Art. 26/27 DORA | kritisch/wichtig |
| 15 | Art. 30 III lit. f | **Uneingeschränkte Audit-/Einsichtsrechte** für Institut, externe Auditoren und zuständige Behörden, **inkl. Lead Overseer** | kritisch/wichtig |
| 16 | Art. 30 III lit. g | **Exit-Strategie** mit angemessenem Übergangszeitraum, Datenmigration, keine Schlechterstellung | kritisch/wichtig |
| 17 | Art. 30 III lit. h | Notfallpläne, Business Continuity, Wiederanlauf | kritisch/wichtig |
| 18 | Art. 30 II lit. j + RTS 2024/1773 | Vorgaben für Subunternehmer-Kette inkl. Genehmigungs-/Anzeigepflichten | nach Risiko |
| 19 | Art. 28 VII DORA | Keine vertragliche Verkürzung der Aufsichts-/Resolution-Rechte | alle |
| 20 | DurchfVO 2024/2956 | Datenpunkte für Informationsregister identifizierbar | alle |

Die vollständige Matrix mit allen Unterpunkten und Bewertungsschemata liegt in `references/dora-klauselmatrix.md`.

## Ausgabeformat

### A. Tabular Review (CSV/Markdown-Tabelle)

| Pflicht-# | DORA-Anker | Soll | Klausel (Ist) | Bewertung | Kritikalität (1–5) | Verbesserungsvorschlag | Klausel-Entwurf |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | Art. 30 II lit. d | Vollständige Rückgabe und Löschung der Daten in maschinenlesbarem Format binnen 30 Tagen | § 14.3 ("Daten werden auf Wunsch zurückgegeben") | teilkonform | 4 | Fristen, Format und Löschnachweis fehlen | "Der Auftragnehmer übergibt … binnen 30 Kalendertagen nach Vertragsbeendigung in einem branchenüblichen, maschinenlesbaren, nicht-proprietären Format und löscht alle Kopien einschließlich Backups innerhalb von 90 Tagen; die Löschung ist durch ein qualifiziertes Löschprotokoll nachzuweisen." |
| 15 | Art. 30 III lit. f | Audit-/Einsichtsrechte inkl. Lead Overseer, ohne Kostenbeteiligung des Instituts | § 17 ("Audit einmal jährlich, Selbstkosten anteilig") | nicht konform | 5 | Erweiterung auf Behörden + Lead Overseer; Kostenklausel anpassen | "Der Auftragnehmer gewährt dem Auftraggeber, von ihm benannten externen Prüfern sowie der zuständigen Aufsichts- und Resolution-Behörde einschließlich des Lead Overseers im Sinne von Art. 31 ff. DORA … uneingeschränkte und kostenfreie Audit- und Einsichtsrechte …" |

### B. Executive Summary (Memo, max. 1 Seite)

- Gesamtbewertung (Ampel + Score-Mittelwert)
- Top-3-Lücken (Kritikalität 5)
- Re-Papering-Aufwand (Schätzung)
- Empfehlung: vertraglich nachverhandelbar / Exit-/Alternativen-Prüfung notwendig
- Hinweis auf Aufnahme ins Informationsregister
- Quellenkopf mit Versionsstand der DORA-VO

### C. Klausel-Patch-Liste (DOCX/Markdown)

Pro Verbesserungsvorschlag ein Patch-Block mit:

- Klauselnummer alt / neu
- Diff (alt → neu)
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Verhandlungsschwere (1–3)

## Beispiel (Auszug Memo)

> **Mandat:** Prüfung des Master Services Agreement zwischen X-Bank AG (CRR-Institut, BaFin-Aufsicht) und CloudCo Inc. (SaaS, Kernbanken-Modul). Funktionsklassifikation: **kritisch oder wichtig** i. S. v. Art. 28 II DORA.
>
> **Kurzantwort:** Der Vertrag ist in der aktuellen Fassung nicht DORA-konform. Von 20 Pflichtinhalten sind 7 vollständig, 9 teilkonform und 4 fehlend. Re-Papering bis 17.01.2025 erforderlich (Art. 64 II DORA).
>
> **Tragende Lücken:**
> Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
> 2. Sub-Outsourcing-Liste ist statisch, ohne Anzeige- und Genehmigungspflichten. Delegierte VO (EU) 2024/1773 verlangt Materialitätsschwellen und Ex-ante-Anzeige.
> 3. Exit-Strategie fehlt; § 18 MSA enthält nur eine Datenrückgabeklausel ohne Migrationsunterstützung – Verstoß gegen Art. 30 III lit. g DORA. Vgl. Zetzsche/Anker-Sørensen, EuZW 2023, 645 (648).
> 4. Beteiligung an TLPT-Tests nicht vereinbart (Art. 30 III lit. e i. V. m. Art. 26, 27 DORA).
>
> **Empfehlung:** Klausel-Patch-Liste umsetzen (siehe Anlage); Eskalation bei CloudCo wegen Audit- und Exit-Klauseln; Aufnahme in Informationsregister (DurchfVO 2024/2956) vorbereiten.

## Risiken und typische Fehler

- **Fehlende Funktionsklassifikation.** Ohne Einstufung als "kritisch oder wichtig" werden Art.-30-III-Pflichten oft übersehen. Dokumentieren!
- **AGB-Übernahme.** Standard-Cloud-AGB (Microsoft, AWS, GCP) sind regelmäßig **nicht** DORA-konform. Nachverhandlung über DORA-Addendum/SCC-ähnliche Anhänge erforderlich.
- **Sub-Out-Ketten.** Mehrstufige Subunternehmer-Ketten müssen vollständig abgebildet werden (RTS 2024/1773). Materialitätsschwellen vereinbaren.
- **Berufsgeheimnis.** § 203 III StGB-Klausel ("mitwirkende Personen") fehlt häufig – kritisch bei Daten, die unter § 203 StGB fallen (Banken: § 9 KWG; Versicherer: § 311 VAG; Rechtsanwälte: § 43a Abs. 2 BRAO).
- **Datenschutz.** Art. 28 DSGVO AVV ist separat oder integriert, aber **immer** mitzuprüfen.
- **Kündigungsrechte.** Art. 28 VII DORA setzt zwingende außerordentliche Kündigungsrechte voraus (z. B. behördliche Anordnung, schwerwiegende IKT-Vorfälle, Verstoß gegen anwendbares Recht).
- **Verhältnismäßigkeit.** Art. 4 DORA – kleinere Institute (z. B. nach Art. 16 DORA "vereinfachter Rahmen") können geringere Anforderungen haben. Nicht überregulieren.
- **Aktualität.** RTS/ITS-Pakete werden laufend nachgeschoben (ESA-Roadmap 2024–2026). Vor Audit immer EUR-Lex-Snapshot ziehen.
- **Halluzinationsrisiko.** Bei jedem Klauselzitat: konkretes Aktenzeichen/Fundstelle prüfen.

## Quellenpflicht

Jede juristische Aussage in der tabellarischen Auswertung wird belegt nach [`../../../references/zitierweise.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/references/zitierweise.md). Mindestens:

- DORA-Artikel mit Absatz/Buchstabe und Anhang (sofern Anhang einschlägig).
- Einschlägige delegierte VO mit CELEX-Nr.
- Mindestens ein BaFin- oder ESA-Verlautbarungs-Beleg, sofern vorhanden.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Reihenfolge der Belege: EU-Recht vor nationalem Recht; Verordnung vor Soft Law; Rspr. vor Literatur (Rspr. zur DORA selbst liegt nur vereinzelt vor – ausdrücklich kennzeichnen: "Rspr. zu DORA liegt soweit ersichtlich noch nicht vor, vgl. aber …").

---

## Skill: `inkasso-rdg-luecken-mar-mifid`

_Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg Inkassoerlaubnis Zulassung Aufsicht Kundenschutz. Output: RDG-Prüfmemo Erlaubnis-Empfeh..._

# Inkassodienstleistungen (RDG)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Begleitet die rechtskonforme Durchführung von Inkassodienstleistungen durch registrierte Inkassounternehmen (§ 10 Abs. 1 Nr. 1 RDG) und Rechtsanwälte (§ 43d BRAO). Er deckt Registrierungsvoraussetzungen, erlaubten Tätigkeitsumfang, Hinweispflichten gegenüber Schuldnern, Vergütungsfragen (§ 4 RDGEG) und die datenschutzkonforme Verarbeitung von Schuldnerdaten (Art. 6 Abs. 1 lit. f DSGVO) ab. Relevanz insb. für Legal-Tech-Geschäftsmodelle nach dem "LexFox"-Urteil des BGH. Anwendungsfälle: Mietpreisbremse-Durchsetzung durch Inkassounternehmen, Consumer-Inkasso-Modelle, Forderungsinkasso im B2C-Bereich, anwaltliches Inkasso.

## Eingaben

Das Modell benötigt:

- **Art des Akteurs**: Registriertes Inkassounternehmen (§ 10 RDG) oder Rechtsanwalt (§ 43d BRAO)?
- **Registrierungsstatus**: RDG-Registrierung vorhanden (§ 13 RDG)? Welche Behörde?
- **Forderungsart**: Mietforderung, Kaufpreisforderung, Schadenersatz, Verbraucherrechte-Ansprüche?
- **Schuldner**: Verbraucher (§ 13 BGB) oder Unternehmer?
- **Geschäftsmodell**: Klassisches Inkasso (Abtretung oder Einzugsermächtigung) oder Legal-Tech-Modell (Schuldner zahlt Erfolgsprovision)?
- **Vergütungsstruktur**: Wie wird die Vergütung berechnet? Auf Basis RVG, RDGEG oder abweichend?
- **Datenlage**: Welche Schuldnerdaten werden verarbeitet? Von wem bezogen (Gläubiger, Auskunfteien)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 10 Abs. 1 Nr. 1 RDG**: Natürliche und juristische Personen, die nicht als Rechtsanwalt zugelassen sind, dürfen Inkassodienstleistungen erbringen, wenn sie bei der zuständigen Behörde registriert sind.
- **§ 2 Abs. 2 Satz 1 RDG**: Inkassodienstleistung = Einziehung fremder oder zum Zweck der Einziehung auf eigene Rechnung abgetretener Forderungen, wenn die Forderungseinziehung als eigenständiges Geschäft betrieben wird.
- **§ 13 Abs. 1 RDG**: Registrierungspflicht; zuständig: Oberlandesgericht des Sitzes; Voraussetzungen: Sachkunde, Zuverlässigkeit, Berufshaftpflichtversicherung.
- **§ 13c RDG**: Pflichten registrierter Personen: Hinweispflichten gegenüber Auftraggebern und Schuldnern, Dokumentationspflichten, Treuhandpflichten.
- **§ 43d BRAO**: Rechtsanwälte dürfen Inkassodienstleistungen erbringen; keine gesonderte RDG-Registrierung erforderlich; aber: Einhaltung von § 43d BRAO-Anforderungen (Transparenz, Hinweis auf anwaltliche Stellung, Trennung von sonstigem Mandat).
- **§ 4 RDGEG (Vergütung)**: Vergütung für Inkassodienstleistungen registrierter Personen richtet sich nach den Vorschriften des RVG (analog); abweichende Vereinbarungen nur unter bestimmten Voraussetzungen zulässig; Verbraucher: keine Belastung mit überhöhten Kosten.
- **§ 13d RDG**: Hinweispflicht gegenüber Schuldnern: Mitteilung, wer Forderungsinhaber/Einzugsermächtiger ist, Hinweis auf Möglichkeit, Forderung zu bestreiten, Rechtsbehelfsbelehrung.
- **Art. 6 Abs. 1 lit. f DSGVO**: Berechtigtes Interesse als Rechtsgrundlage für Verarbeitung von Schuldnerdaten im Inkasso; Interessenabwägung: Inkasso-Interesse vs. Rechte der Schuldner; ErwGr. 47 DSGVO: Forderungseinzug als anerkanntes berechtigtes Interesse.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Schritt 1 – Zulässigkeitsprüfung: Inkassodienstleistung i.S.d. RDG**
- Liegt Einziehung fremder oder abgetretener Forderungen als eigenständiges Geschäft vor (§ 2 Abs. 2 Satz 1 RDG)?
- Abgrenzung zu unerlaubter Rechtsberatung: Geht die Tätigkeit über Forderungseinziehung hinaus (umfassende Rechtsberatung)? → Unzulässig ohne Anwaltszulassung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 2 – Registrierung prüfen (§ 13 RDG)**
- Registrierung beim zuständigen OLG (§ 13 Abs. 1 RDG) vorhanden?
- Sachkunde nachgewiesen? Berufshaftpflichtversicherung abgeschlossen?
- Laufende Pflichten: Meldung von Änderungen, Jahresabschlüsse, Kundengeldtreuhandkonto.
- Rechtsanwalt: Keine Registrierung erforderlich; stattdessen § 43d BRAO beachten.

**Schritt 3 – Hinweispflichten gegenüber Schuldnern (§ 13d RDG)**
- Erstes Anschreiben muss enthalten:
 - Identität des Inkassounternehmens (vollständiger Name, Anschrift, Registrierungsnummer).
 - Forderungsinhaber und Rechtsgrund der Forderung.
 - Forderungsbetrag mit Aufschlüsselung (Hauptforderung, Zinsen, Kosten).
 - Hinweis auf Recht des Schuldners, die Forderung zu bestreiten.
 - Kontaktmöglichkeit für Rückfragen.
- Irrleitende oder einschüchternde Kommunikation ist unzulässig (§ 4 UWG, Lauterkeitsrecht).

**Schritt 4 – Vergütung (§ 4 RDGEG)**
- Vergütung nach RVG-Grundsätzen analog (Inkassovergütungsverordnung außer Kraft, nunmehr § 4 RDGEG).
- Verbraucher-Schuldner: Inkassokosten nur in Höhe der nach RVG erstattungsfähigen Kosten (§ 4 Abs. 5 RDGEG); keine Kostenwälzung oberhalb RVG-Niveau auf Schuldner.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 5 – Datenschutz (Art. 6 Abs. 1 lit. f DSGVO)**
- Rechtsgrundlage für Verarbeitung von Schuldnerdaten: berechtigtes Interesse des Forderungsgläubigers/Inkassounternehmens (Art. 6 Abs. 1 lit. f DSGVO; ErwGr. 47).
- Interessenabwägung dokumentieren: Forderungseinziehungsinteresse vs. Datenschutzinteressen des Schuldners.
- Informationspflicht nach Art. 14 DSGVO beim ersten Kontakt mit Schuldner (Datenherkunft: Gläubiger).
- Auskunfteien-Meldung (SCHUFA): Nur bei erheblicher Forderung, nach Mahnung, keine unverhältnismäßige Beeinträchtigung (Berechtigungsinteresse nach § 31 BDSG i.V.m. Art. 6 Abs. 1 lit. f DSGVO).

## Beispiel

**Sachverhalt**: Legal-Tech-Startup L (RDG-registriert) zieht für Mieter M Ansprüche aus der Mietpreisbremse ein. L lässt sich die Forderung abtreten und nimmt 30 % Erfolgsprovision vom Erstattungsbetrag. L sendet Schreiben an Vermieter V ohne Hinweis auf M's Widerspruchsmöglichkeit.

**Gutachtenstil**:

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Hinweispflicht (§ 13d RDG)*: Das Schreiben an V muss V auf sein Recht hinweisen, die Forderung zu bestreiten. Das Fehlen dieses Hinweises verletzt § 13d RDG und kann als irreführende Geschäftspraxis nach § 5 UWG abgemahnt werden.

*Datenschutz*: L verarbeitet Schuldner-V's Daten auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an Forderungseinziehung). V ist nach Art. 14 DSGVO beim ersten Kontakt über die Datenherkunft (Mandant M) zu informieren.

## Risiken und typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Fehlende Hinweispflichten (§ 13d RDG)**: Erstes Schreiben ohne vollständige Pflichtangaben ist abmahn- und bußgeldfähig; v.a. fehlender Widerspruchshinweis.
- **Überhöhte Inkassokosten**: Verbraucher-Schuldnern dürfen über RVG-Niveau hinausgehende Kosten nicht auferlegt werden (§ 4 Abs. 5 RDGEG); Überschreitung → Rückforderungsanspruch.
- **Datenschutzverletzung bei Auskunftei-Meldung**: SCHUFA-Meldung ohne vorherige Mahnung und ohne Verhältnismäßigkeit ist ein eigenständiger DSGVO-Verstoß.
- **Fehlende RDG-Registrierung**: Tätigkeit ohne Registrierung ist gemäß § 3 RDG verboten; Verträge können nach § 134 BGB nichtig sein; Abtretung von Forderungen zu Inkassozwecken an nicht registrierte Person: unwirksam.
- **Treuhandpflichten verletzt**: Vereinnahmte Schuldnerzahlungen müssen unverzüglich an Gläubiger weitergeleitet werden (§ 13c RDG); Vermischung mit Eigengeldern ist strafbar (§ 246 StGB).

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `luecken`

_Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit Risikoklassifizierung. Abgrenzung: nicht für Lueckenaufzeiger-Perspektive nach aussen (luecken-a..._

# Gap-Tracker

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Gap-Tracker-Datei: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml`
- Optional: Filter (nach Schweregrad, Frist, Eigentümer, Status)
- Optional: Gap-ID zum gezielten Aktualisieren

## Ablauf

### 1. Tracker lesen

Gap-Tracker lesen. Falls nicht vorhanden:
```
Noch keine Gaps erfasst. Starten Sie mit /regulatorisches-recht:lücken-aufzeiger,
um eine Gap-Analyse gegen eine Aufsichtsverlautbarung durchzuführen.
```

### 2. Status-Übersicht ausgeben

```
Gap-Übersicht – Stand: TT.MM.JJJJ

Gesamt: N | 🔴 Blockierend: N | 🟠 Hoch: N | 🟡 Mittel: N | 🟢 Gering: N
Offen: N | In Bearbeitung: N | Geschlossen: N | Überfällig: N
```

### 3. Sortierte Gap-Tabelle ausgeben

| Gap-ID | Verlautbarung | Anforderung (Kurzfassung) | Schwere | Frist | Eigentümer | Status |
|---|---|---|---|---|---|---|
| GAP-2025-001 | MaRisk AT 4.3.2 | Datenhaltung 10 Jahre | 🔴 | 31.12.2025 | Compliance | offen |

Sortierung: zuerst 🔴, dann nach Frist aufsteigend.

### 4. Aktionen anbieten

Nach der Übersicht:
```
Was möchten Sie tun?
a) Gap schließen (Gap-ID angeben)
b) Eigentümer setzen / ändern
c) Status aktualisieren (offen → in Bearbeitung → geschlossen)
d) Richtlinienneufassung für einen Gap starten → /richtlinien-neufassung
e) Eskalationsnotiz für überfällige Gaps erstellen
f) Alle geschlossenen Gaps archivieren
```

### 5. Tracker aktualisieren

Änderungen in der YAML-Datei speichern und Änderungszeitpunkt vermerken.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bindung an Gesetz und Recht, Rechtsluecken-Klaerung) — §§ 133, 157 BGB (Auslegungsgrundsaetze) — § 5 EGBGB (Analogie bei Rechtsluecken im Privatrecht) — §§ 13, 31 EnWG (Luecken in Regulierungs-Normen)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Dieser Skill liest und schreibt ausschließlich interne Tracking-Daten; keine normspezifische Zitierung erforderlich. Gap-Inhalte enthalten Normverweise aus dem erzeugenden `luecken-aufzeiger`-Lauf.

## Beispiel

**Eingabe:** `/regulatorisches-recht:lücken`

**Ausgabe:**
```
Gap-Übersicht – Stand: 01.06.2025

Gesamt: 7 | 🔴 2 | 🟠 3 | 🟡 2 | 🟢 0
Offen: 5 | In Bearbeitung: 2 | Geschlossen: 0 | Überfällig: 0

| Gap-ID | Verlautbarung | Anforderung | Schwere | Frist | Eigentümer | Status |
|-------------|----------------------|---------------------|---------|------------|-------------|---------------|
| GAP-2025-001| MaRisk AT 4.3.2 | Datenhaltung 10 J. | 🔴 | 31.12.2025 | Compliance | offen |
| GAP-2025-002| MaRisk BTR 3.2 | ESG-Integration | 🔴 | 31.03.2026 | Risiko | in Bearbeitung|
| GAP-2025-003| MaRisk BTO 1.2.4 | Kreditvergabe | 🟠 | 30.06.2026 | Kredit | offen |
```

## Risiken / typische Fehler

- **Veralteter Tracker:** Ohne regelmäßige `luecken-aufzeiger`-Läufe veraltet der Tracker. Hinweis anzeigen, wenn der letzte Lauf > 90 Tage zurückliegt.
- **Eigentümer nicht gesetzt:** Gaps ohne Eigentümer werden nicht umgesetzt. Unzugeordnete Gaps explizit markieren.
- **Fristüberschreitung ohne Eskalation:** Für überfällige Gaps automatisch Eskalationsnotiz-Option hervorheben.

---

## Skill: `luecken-aufzeiger`

_Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG Art. 12 80 AEUV Art. 107. Prüfraster: Normtext Regelungsziele Luecken unbeabsichtigte Folgen Verbesserungsvorschlaege. Output: Lueckenanalyse Stellungnahmen-Vorentwurf. Abgrenz..._

# Gap-Analyse: Interne Richtlinien vs. Aufsichtsverlautbarungen

## Eingaben

- **Aufsichtsverlautbarung:** BaFin-Rundschreiben / Leitlinie (hochgeladen oder per Link)
- **Interne Richtlinie(n):** Zu prüfende Bestandsdokumente (hochgeladen oder aus Richtlinienbibliothek)
- **Segment:** Art des Instituts / Unternehmens (z. B. Kreditinstitut KWG § 1, Zahlungsinstitut ZAG § 1, Wertpapierfirma WpIG § 2)
- Optional: Übergangsfrist aus der Verlautbarung
- Optional: Bestehende Gap-Liste aus vorherigem Lauf

## Ablauf

### 1. Verlautbarung einlesen und strukturieren

Die Aufsichtsverlautbarung lesen und gliedern:

| Modul / Abschnitt | Regelungsinhalt | Adressatenkreis | Übergangsfrist |
|---|---|---|---|
| [z. B. AT 4.3.2] | [Anforderung] | [Alle Institute / Bedeutende Institute] | [TT.MM.JJJJ] |

Für MaRisk-Rundschreiben (BaFin RS 09/2017 i.d.F. Novelle 2023) [Modellwissen – prüfen auf aktuelle Fassung]:
- **AT-Module:** Allgemeiner Teil (AT 1 – AT 9)
- **BT-Module:** Besonderer Teil (BTO Kreditgeschäft, BTRO Handelsgeschäft)
- **BTR-Module:** Besondere Anforderungen Risikosteuerung (BTR 1–4)

### 2. Interne Richtlinien einlesen und zuordnen

Für jede interne Richtlinie ermitteln:
- Welches Modul / welchen Abschnitt der Verlautbarung deckt sie ab?
- Letzte Aktualisierung
- Verantwortlicher

Zuordnungsmatrix erstellen:

| Verlautbarungsabschnitt | Interne Richtlinie | Deckungsgrad | Bemerkung |
|---|---|---|---|
| AT 4.3.2 | IKS-Richtlinie v. 01.03.2023 | teilweise | Datenhaltungsfristen fehlen |
| BT 3.1 | Stresstesting-Policy | vollständig | Aktuell |
| BTR 2.3 | Liquiditätsrichtlinie | keine | Richtlinie fehlt `[prüfen]` |

### 3. Gap-Identifikation

Für jede identifizierte Lücke:

```yaml
gap:
 id: "[GAP-2025-001]"
 verlautbarung: "[BaFin RS 09/2017 Novelle 2023, AT 4.3.2]"
 anforderung: "[Beschreibung der neuen Anforderung]"
 bestandsregel: "[Aktuelle interne Regelung oder 'keine']"
 luecke: "[Was fehlt oder abweicht]"
 schweregrad: "[🔴 Blockierend / 🟠 Hoch / 🟡 Mittel / 🟢 Gering]"
 frist: "[TT.MM.JJJJ oder 'keine Frist']"
 eigentuemer: "[PLATZHALTER]"
 status: "offen"
```

Schweregradkriteria:
- 🔴 **Blockierend:** Fehlende Anforderung ist prüfungsrelevant; BaFin-Prüfung würde Mängelbescheid auslösen
- 🟠 **Hoch:** Anforderung ist klar formuliert, Lücke vorhanden, Frist < 3 Monate
- 🟡 **Mittel:** Anforderung besteht, Lücke marginal oder Frist > 3 Monate
- 🟢 **Gering:** Best-Practice-Empfehlung ohne verbindlichen Charakter

### 4. Gap-Bericht erstellen

**Zusammenfassung:**
- Gesamtzahl Gaps: N
- Davon 🔴 Blockierend: N | 🟠 Hoch: N | 🟡 Mittel: N | 🟢 Gering: N
- Nächste Frist: TT.MM.JJJJ (GAP-2025-xxx)

**Detaillierte Gap-Tabelle:** (alle Gaps mit Status, Frist, Eigentümer)

**Handlungsempfehlungen:** Priorisierte Liste nach Schweregrad und Frist

### 5. Gap-Tracker schreiben

Gap-Liste in `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml` aktualisieren.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Lueckenfuellungs-Pflicht) — § 5 EGBGB (Analogie) — §§ 133, 157 BGB (Auslegung) — §§ 306 Abs. 2 BGB (Lueckenfuellung AGB-Recht) — Art. 288 AEUV (Richtlinien-Umsetzungs-Luecken)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Verlautbarungen und Normen:
- BaFin-Rundschreiben 09/2017 (BA) – Mindestanforderungen an das Risikomanagement (MaRisk) i.d.F. der Novelle 2023 [Modellwissen – prüfen auf aktuelle Fassung; abrufbar unter bafin.de]
- BaFin-Rundschreiben 10/2017 (VA) – VAIT (Versicherungsaufsichtliche Anforderungen an die IT) [Modellwissen – prüfen]
- BaFin-Rundschreiben 10/2018 (BA) – BAIT (Bankaufsichtliche Anforderungen an die IT) i.d.F. 2021 [Modellwissen – prüfen]
- EBA-Leitlinien EBA/GL/2021/04 – IRRBB/CSRBB [Modellwissen – prüfen]
- § 25a KWG (Ordnungsgemäße Geschäftsorganisation)
- § 25b KWG (Auslagerungen)
- Art. 74 CRD V (Governance-Anforderungen)

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Lerch, ZAG, 2. Aufl. 2020, § 27 Rn. 1 ff. (Risikomanagement Zahlungsinstitute).

## Beispiel

**Eingabe:** "Bitte die MaRisk-Novelle 2023 gegen unsere Risikomanagement-Richtlinien prüfen. Richtlinien sind im Ordner /compliance/richtlinien/ hinterlegt."

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], Richtlinien [Nutzer-Input]
> - **Gelesen:** MaRisk vollständig; 5 Richtlinien
> - **Zu Ihrer Einschätzung:** 2 Gaps mit 🔴 markiert `[prüfen]`
> - **Vor Verwendung:** MaRisk-Fassung gegen bafin.de aktuellen Stand prüfen

---

**Gap-Bericht: MaRisk-Novelle 2023**
*Erstellt: 01.06.2025 | Institut: Musterbank AG | Segment: KWG-Kreditinstitut*

**Zusammenfassung:** 7 Gaps identifiziert: 🔴 2 | 🟠 3 | 🟡 2 | 🟢 0

| Gap-ID | Modul | Anforderung | Lücke | Schwere | Frist |
|---|---|---|---|---|---|
| GAP-2025-001 | AT 4.3.2 | Datenhaltung 10 J. | Richtlinie sieht 7 J. vor | 🔴 | 31.12.2025 |
| GAP-2025-002 | BTR 3.2 | ESG-Risikointegration | Keine ESG-Policy vorhanden | 🔴 | 31.03.2026 |
| GAP-2025-003 | BTO 1.2.4 | Kreditvergabestandards | Teilweise abgedeckt | 🟠 | 30.06.2026 |

**Handlungsempfehlungen:**
1. **Sofort (GAP-2025-001):** IKS-Richtlinie um Datenhaltungsklausel ergänzen; Norm: AT 4.3.2 MaRisk. Verantwortlich: Compliance.
2. **Bis 31.12.2025 (GAP-2025-002):** ESG-Risikorichtlinie neu erstellen; `/regulatorisches-recht:richtlinien-neufassung` nutzen.

## Risiken / typische Fehler

- **Veraltete MaRisk-Version:** BaFin novelliert MaRisk regelmäßig; stets die aktuell gültige Fassung von bafin.de verwenden. Modellwissen über MaRisk-Inhalte immer gegen die offizielle Fassung prüfen: `[Modellwissen – prüfen]`.
- **Adressatenkreis-Fehler:** Nicht alle MaRisk-Anforderungen gelten für alle Institute gleichermaßen (Proportionalitätsgrundsatz § 25a Abs. 1 S. 3 KWG). Institutsgröße und -komplexität beachten.
- **Fehlende Übergangsfrist:** MaRisk-Novellen enthalten oft gestaffelte Übergangsfristen für einzelne Module. Nicht alle Gaps haben dieselbe Frist.
- **Nur formale Prüfung:** Auch wenn eine interne Richtlinie den Anforderungswortlaut übernimmt, kann sie in der Praxis nicht gelebt werden. Hinweis auf erforderliche Prozessprüfung.
- **Auslagerungsrisiken:** § 25b KWG-Anforderungen an ausgelagerte Tätigkeiten separat prüfen – nicht durch Richtlinienprüfung allein abgedeckt.

---

## Skill: `mandat-arbeitsbereich`

_Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behörden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Abgrenzung: nicht für inhaltliche Regulierungsprüfung im Regul..._

# Mandat-Workspace-Verwaltung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktives Praxisprofil mit aktivierten Mandat-Workspaces
- Mandat-Subkommando: `neu | auflisten | wechseln | schließen | keiner`
- Optional: Mandat-Name, Mandant, Rechtsgebiet, Frist

## Ablauf

### Subkommando: `neu`

Abfragen:
```
1. Mandant (intern: nur Kürzel, kein vollständiger Name in Logs)
2. Mandat-Bezeichnung / Slug (z. B. bafin-prüfung-2025-mandantA)
3. Art des Mandats:
 a) Gap-Analyse gegen Regulierungsakt
 b) Konsultationsbeitrag
 c) Richtlinienneufassung
 d) Behördenanfrage
 e) Sonstiges
4. Zuständige Behörde(n)
5. Leitfrist (falls bekannt)
```

Mandatsordner anlegen:
```
~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/mandate/<mandat-slug>/
├── mandat.md # Mandat-Fakten und Übersteuerungen
├── gap-tracker.yaml # Mandat-spezifische Gaps
├── comment-tracker.yaml
└── verification-log.md
```

`mandat.md` Vorlage:
```markdown
### Mandat: [Bezeichnung]
Erstellt: [TT.MM.JJJJ]
Mandant: [Kürzel]
Art: [Typ]
Behörde(n): [Liste]
Leitfrist: [TT.MM.JJJJ]
Status: aktiv

## Mandat-spezifische Fakten
[Abweichungen vom Praxisprofil; Mandant-spezifische Materialitätsschwelle usw.]

## Datenschutz-Hinweis
§ 43a Abs. 2 BRAO, § 203 StGB. Dieser Ordner enthält mandantenbezogene Daten.
Cross-Mandat-Kontext: deaktiviert (Standard).
```

### Subkommando: `auflisten`

Alle Mandate auflisten:
```
Aktive Mandate:
| Slug | Mandant | Art | Behörde | Leitfrist | Status |
|---|---|---|---|---|---|
| bafin-prüfung-2025-A | Mandant A | Gap-Analyse | BaFin | 31.12.2025 | aktiv |
```

### Subkommando: `wechseln`

```
Zu welchem Mandat wechseln?
[Liste der aktiven Mandate anzeigen]
```
Nach Auswahl: Aktives Mandat im Profil setzen. Skills lesen jetzt `mandat.md` dieses Mandats.

### Subkommando: `schließen`

```
Mandat [Slug] schließen?
Hinweis: Dateien bleiben erhalten. Status wird auf 'geschlossen' gesetzt.
Lernerkenntnisse ins Praxisprofil übertragen? (ja/nein)
```

### Subkommando: `keiner`

Aktives Mandat deaktivieren → Skills laufen wieder auf Praxisebene.

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Relevante Berufsrechtsnormen:
- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht)
- § 203 StGB (Verletzung von Privatgeheimnissen)
- § 50 BRAO (Aktenführung)
- BORA § 2 (Unabhängigkeit), § 6 (Handakten)

## Beispiel

**Eingabe:** `/regulatorisches-recht:regulatorisches-recht-mandat-arbeitsbereich neu`

**Ausgabe:**
```
Neues Mandat anlegen.

Mandant-Kürzel (nur intern sichtbar): MandantA
Mandat-Bezeichnung: MaRisk-GAP-2025-MandantA
Art: Gap-Analyse
Zuständige Behörde: BaFin
Leitfrist: 31.12.2025

Mandat angelegt unter:
~/.../mandate/mairisk-gap-2025-mandanta/

Aktives Mandat: MaRisk-GAP-2025-MandantA

Nächster Schritt: /regulatorisches-recht:lücken-aufzeiger
```

## Risiken / typische Fehler

- **Cross-Mandat-Kontext versehentlich aktiviert:** Skills dürfen mandantsübergreifend niemals Informationen verbinden, wenn Cross-Mandat-Kontext deaktiviert ist (Standard). Explizite Anfrage erforderlich.
- **Klarnamen in Pfaden:** Mandanten-Klarnamen nicht in Dateinamen oder Logs verwenden. Nur Kürzel.
- **Nicht geschlossene Mandate:** Alte aktive Mandate ohne Leitfrist überprüfen und bei Abschluss schließen; beugt Versehen mit veralteten Kontextinformationen vor.
- **Mandantengeheimnis:** Inhalte aus `mandat.md` und den mandat-spezifischen Trackern sind vertraulich nach § 43a Abs. 2 BRAO. Nie in gemeinsame Kontexte oder Protokolle exportieren.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** §§ 611-630 BGB (Dienstvertrag, Mandatsrecht) — §§ 48-49 VwVfG — §§ 3-7 BORA (Berufsrecht Rechtsanwaelte)

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

---

## Skill: `regrecht-einfuehrung-sektoren`

_Einfuehrung regulatorisches Recht in den wichtigsten Sektoren: Bank, Versicherung, Energie, Telekommunikation, Verkehr, Pharma, Lebensmittel. Pro Sektor: Aufsicht, Kernnormen, Lizenzpflicht, typische Compliance-Aufgaben. Entscheidungstabelle und Verweis auf passende Detail-Skills im Regulatorisch..._

# Regrecht: Sektoren-Einfuehrung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Regrecht: Sektoren-Einfuehrung
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `regulatorisches-richtlinien-neufassung`

_Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf. Output: ueberarbeitetes Dokument Aenderungsprotokoll. Abgrenzung: nicht für Neu..._

# Praxisprofil anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktives Praxisprofil (muss vorhanden sein – sonst `regulatorisches-recht-kaltstart-interview` ausführen)
- Konkrete Angabe, was geändert werden soll

## Ablauf

### 1. Profilzustand prüfen

Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` lesen. Falls `[PLATZHALTER]`-Marker vorhanden: zum `regulatorisches-recht-kaltstart-interview` umleiten.

### 2. Änderungswunsch klären

Dem Nutzer die Hauptkategorien anbieten:

```
Was soll angepasst werden?
a) Beobachtete Behörden (hinzufügen / entfernen)
b) Richtlinienbibliothek (Speicherort, neue Richtlinien, Verantwortliche)
c) Materialitätsschwelle (Stufen neu kalibrieren)
d) Feed-Konfiguration (URLs, Prüfrhythmus)
e) Gap-Response-Prozess (Triageperson, Eigentümer, Eskalationsweg)
f) Rolle (Rollenänderung des Nutzers)
g) Mandat-Workspaces (aktivieren / deaktivieren)
h) Sonstiges
```

### 3. Änderung durchführen

Nur den betroffenen Abschnitt des Praxisprofils aktualisieren. Restliche Konfiguration unberührt lassen. Änderung mit Datum versehen:

```
[Geändert am TT.MM.JJJJ: <Beschreibung der Änderung>]
```

### 4. Bestätigung

Geänderten Abschnitt dem Nutzer zur Bestätigung vorlegen, dann speichern.

### 5. Abhängige Einstellungen prüfen

- Bei Hinzufügen einer Behörde: Feed-URL und Prüfrhythmus ebenfalls erfassen.
- Bei Änderung der Materialitätsschwelle: Hinweis, dass der `aufsichts-feed-monitor` beim nächsten Lauf die neue Schwelle anwendet.
- Bei Änderung des Richtlinienspeichers: Hinweis, dass `richtlinien-vergleich` den neuen Pfad nutzt.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

§§ 48, 49 VwVfG (Rücknahme, Widerruf) — §§ 313, 314 BGB (Anpassung, Kuendigung bei Aenderung der Grundlage) — Art. 288 AEUV (Richtlinien-Anpassungspflicht)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Keine normativen Anforderungen an das Praxisprofil selbst. Inhaltliche Anforderungen richten sich nach dem Plugin-Zweck.

## Beispiel

**Eingabe:** "Bitte die BNetzA als weitere beobachtete Behörde hinzufügen. Feed: https://www.bundesnetzagentur.de/DE/Presse/RSS/rss_node.html"

**Ausgabe:**

> Praxisprofil aktualisiert:
>
> **Neu hinzugefügte Behörde:**
> | Behörde | Zuständigkeit | Beobachtungsgrund | Feed-Quelle |
> |---|---|---|---|
> | Bundesnetzagentur (BNetzA) | EnWG, TKG | Telekommunikationsregulierung | RSS: bundesnetzagentur.de/RSS |
>
> Gespeichert in `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` [Geändert am 01.06.2025]
>
> Hinweis: Der `aufsichts-feed-monitor` erfasst BNetzA-Einträge ab dem nächsten Lauf.

## Risiken / typische Fehler

- **Versehentliches Überschreiben:** Dieser Skill ändert nur den angegebenen Abschnitt. Nie das gesamte Profil überschreiben.
- **Ungültige Feed-URLs:** Feed-URL vor dem Speichern testen; defekte Feeds führen zu stillen Fehlern im `aufsichts-feed-monitor`.
- **Fehlende Neuindizierung:** Nach Änderung des Richtlinienspeichers muss die Bibliothek neu indiziert werden. Hinweis geben.

---

## Skill: `richtlinien-anhoerung-red-aufsichtsrecht`

_Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der Aenderungen. Output: Vergleichstabelle Differenzanalyse. Abgrenzung: nicht für Lueckenanal..._

# Richtlinien-Diff

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Neue Norm / Verlautbarung:** Text oder Link (BaFin-Rundschreiben, MaRisk-Modul, EBA-Leitlinie, Gesetzestext)
- **Bestehende Richtlinie:** Bestandsdokument (hochgeladen oder aus Bibliothek)
- **Scope:** Optional – nur bestimmte Abschnitte vergleichen
- Optional: Vorheriger Diff-Lauf zum Vergleich

## Ablauf

### 1. Neue Norm strukturieren

Neue Norm / Verlautbarung lesen und in nummerierte Anforderungen zerlegen:

| Nr. | Abschnitt | Anforderungstext (Kurzfassung) | Verbindlichkeit |
|---|---|---|---|
| A01 | AT 4.3.2 | Aufbewahrung von Daten mind. 10 Jahre | Verbindlich |
| A02 | AT 4.3.2 | Backup-Konzept mit Wiederherstellungstest | Verbindlich |
| A03 | AT 4.3.2 | Dokumentation der Datenklassifizierung | Empfehlung |

Verbindlichkeitskennzeichnung:
- **Verbindlich:** "hat sicherzustellen", "muss", "sind zu"
- **Empfehlung/Best Practice:** "sollte", "kann", "wird empfohlen"

### 2. Bestehende Richtlinie strukturieren

Bestehende Richtlinie lesen und relevante Abschnitte den neuen Anforderungen zuordnen.

### 3. Diff-Tabelle erstellen

| Anforderung (Norm) | Deckung in Richtlinie | Status | Differenz |
|---|---|---|---|
| A01: Datenhaltung 10 J. | § 4 Abs. 2 IKS-Richtlinie: 7 Jahre | 🔴 Abweichung | Frist 3 J. kürzer |
| A02: Backup-Konzept | § 5 IKS-Richtlinie: vollständig | 🟢 Gedeckt | – |
| A03: Datenklassifizierung | Keine Regelung | 🟡 Lücke (Best Practice) | Empfehlung fehlt |
| – | § 7 IKS-Richtlinie: Prüfprotokoll | ⚪ Überschuss | Norm enthält keine solche Pflicht |

Status-Legende:
- 🔴 **Abweichung:** Richtlinie weicht von verbindlicher Anforderung ab
- 🟡 **Lücke:** Anforderung fehlt in Richtlinie (verbindlich: 🔴 potentiell; Best Practice: 🟡)
- 🟢 **Gedeckt:** Anforderung vollständig und korrekt abgebildet
- ⚪ **Überschuss:** Richtlinie enthält Regelung, die die Norm nicht fordert (kein Problem, aber zur Kenntnis)

### 4. Zusammenfassung

```
Diff-Zusammenfassung: [Normtitel] vs. [Richtlinientitel]
Analysiert: N Normabschnitte | N Richtlinienabschnitte

Handlungsbedarf:
🔴 N Abweichungen (verbindliche Anforderungen, Richtlinie weicht ab)
🟡 N Lücken (neue Anforderungen ohne Entsprechung)
🟢 N gedeckt
⚪ N Überschüsse (Richtlinie enthält Mehr als die Norm fordert)
```

### 5. Empfehlung

Für jede 🔴-Abweichung und jede wesentliche 🟡-Lücke:
- Konkrete Formulierungsänderung vorschlagen (Ausgangspunkt für `/richtlinien-neufassung`)
- Frist aus der Verlautbarung angeben
- Eskalationsbedarf markieren (`[prüfen]` bei Unklarheit)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen und Verlautbarungen:
- BaFin-Rundschreiben 09/2017 (BA) – MaRisk, alle Novellen [Modellwissen – prüfen auf aktuelle Fassung]
- BaFin-Rundschreiben 10/2018 (BA) – BAIT [Modellwissen – prüfen]
- BaFin-Rundschreiben 10/2017 (VA) – VAIT [Modellwissen – prüfen]
- BaFin-Rundschreiben 05/2021 (IO) – ZAIT (Zahlungsdienstleister IT) [Modellwissen – prüfen]
- EBA-Leitlinien EBA/GL/2019/04 – IKT-Risikomanagement [Modellwissen – prüfen]
- DORA Art. 5 ff. (EU) 2022/2554 (ICT Risk Management)
- § 25a KWG (Ordnungsgemäße Geschäftsorganisation)

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

## Beispiel

**Eingabe:** `/regulatorisches-recht:richtlinien-vergleich MaRisk-AT-4.3.2-Novelle-2023`

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], IKS-Richtlinie v. 01.03.2023 [Nutzer-Input]
> - **Gelesen:** AT 4.3.2 vollständig; IKS-Richtlinie §§ 1–12
> - **Zu Ihrer Einschätzung:** 2 Positionen mit 🔴 markiert `[prüfen]`

---

**Diff: MaRisk AT 4.3.2 (Novelle 2023) vs. IKS-Richtlinie (Stand: 01.03.2023)**

| Anforderung (Norm) | Deckung in Richtlinie | Status | Differenz |
|---|---|---|---|
| Datenhaltung ≥ 10 Jahre | § 4 Abs. 2: 7 Jahre | 🔴 | Verlängerung um 3 Jahre erforderlich `[prüfen]` |
| Backup-Konzept mit Test | § 5 Abs. 1–3 | 🟢 | – |
| Datenklassifizierungsdoku. | Keine Regelung | 🟡 | Abschnitt zu ergänzen |

**Empfohlene Änderung für 🔴:**
> § 4 Abs. 2 IKS-Richtlinie: "Aufbewahrungsfrist von 7 Jahren" → **"mindestens 10 Jahren"** (Anpassung an MaRisk AT 4.3.2 Novelle 2023).

**Nächster Schritt:** `/regulatorisches-recht:richtlinien-neufassung` für den vollständigen Neufassungsentwurf.

## Risiken / typische Fehler

- **Nur Wortlaut-Vergleich:** Eine Richtlinie kann die Norm wörtlich übernehmen, sie aber organisatorisch nicht umsetzen. Hinweis, dass der Diff nur den Dokumenteninhalt vergleicht, nicht die gelebte Praxis.
- **Verlautbarungsversion:** MaRisk und BAIT werden novelliert; stets Version und Datum der verwendeten Norm angeben und prüfen, ob aktuell.
- **Best-Practice vs. verbindlich:** EBA-Leitlinien sind nach Art. 16 EBA-VO "comply or explain" – nicht 1:1 verbindlich. Status klar kennzeichnen.
- **Proportionalitätsgrundsatz:** Nicht jede Norm gilt für jede Institutsgröße gleich (§ 25a Abs. 1 S. 3 KWG). Adressatenkreis prüfen und im Diff ausweisen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** Art. 288 AEUV — §§ 133, 157 BGB — § 47 GGO (Ressortabstimmung Richtlinien-Vergleich)

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

---

## Skill: `richtlinien-neufassung`

_Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg. Output: neue Richtlinie Implementierungshinweise. Abgrenzung: nicht für Anpassun..._

# Richtlinien-Neufassung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Gap oder Diff:** Ergebnis aus `luecken-aufzeiger` oder `richtlinien-vergleich` (oder manuelle Beschreibung der Lücke)
- **Bestandsrichtlinie:** Vollständiger Text (hochgeladen oder eingefügt)
- **Aufsichtsverlautbarung:** BaFin-Rundschreiben / Leitlinie (für Normzitate)
- Optional: Richtlinienformat-Vorlage des Unternehmens
- Optional: Übergangsfrist

## Ablauf

### 1. Ausgangslage erfassen

Aus dem Gap/Diff die zu schließende(n) Lücke(n) identifizieren:
- Welche Abschnitte der Bestandsrichtlinie müssen geändert werden?
- Welche Abschnitte sind neu hinzuzufügen?
- Gibt es Abschnitte, die gestrichen oder eingeschränkt werden müssen?

### 2. Normgrundlagen ermitteln

Für jede Änderung die maßgebliche Aufsichtsnorm zitieren:

```
Änderungsgrund: MaRisk AT 4.3.2 Novelle 2023 – Datenhaltungsfrist 10 Jahre
Maßgebliche Norm: BaFin-Rundschreiben 09/2017 (BA) i.d.F. 2023, AT 4.3.2
Verbindlichkeit: verbindliche Mindestanforderung [Modellwissen – prüfen]
Übergangsfrist: 31.12.2025
```

### 3. Redline-Entwurf erstellen

Format: Änderungen nach Redline-Konvention kennzeichnen:
- **~~Durchgestrichen~~** = zu streichender Text
- **`Fett/kursiv`** oder `[NEU:]` = neuer Text
- `[Normverweis]` = Quelle der Änderung

Beispiel:
```
§ 4 Aufbewahrungspflichten

(2) Daten des Risikomanagements sind für einen Zeitraum von
~~mindestens sieben (7) Jahren~~ **[NEU: mindestens zehn (10) Jahren]**
aufzubewahren. [MaRisk AT 4.3.2 Novelle 2023 – prüfen]

[NEU: (3) Für die Datenklassifizierung ist eine schriftliche
Dokumentation zu erstellen und jährlich zu aktualisieren.
[MaRisk AT 4.3.2 Novelle 2023 – prüfen]]
```

### 4. Neue Abschnitte vollständig entwerfen

Für neu hinzuzufügende Abschnitte vollständigen Text erstellen. Orientierung an:
- Wortlaut der Aufsichtsnorm (ggf. direktes Zitat mit Anpassung)
- Formulierungsstil der Bestandsrichtlinie
- Proportionalitätsgrundsatz (§ 25a Abs. 1 S. 3 KWG)

### 5. Metadaten der Richtlinie aktualisieren

```
Version: [alte Versionsnummer] → [neue Versionsnummer]
Stand: [TT.MM.JJJJ]
Änderungsgrund: Anpassung an [Verlautbarung]
Geprüft durch: [Freigabe durch Rechtsabteilung / Compliance / Vorstand erforderlich]
Nächste Überprüfung: [TT.MM.JJJJ – empfohlen: 12 Monate]
```

### 6. Freigabe-Checkliste

Am Ende des Entwurfs ausgeben:

```
Freigabe-Checkliste vor Inkraftsetzung:
☐ Rechtliche Prüfung abgeschlossen [prüfen]
☐ Compliance-Review durchgeführt
☐ Betroffene Fachabteilung informiert
☐ Vorstand / Geschäftsleitung hat zugestimmt (§ 25a Abs. 1 S. 2 KWG)
☐ Mitarbeiter geschult (falls neue Pflichten)
☐ Versionskontrolle aktualisiert
☐ Datum des Inkrafttretens festgelegt
```

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 288 AEUV (Richtlinien) — §§ 40-44 GGO (Verwaltungsvorschriften-Neufassung) — §§ 305-310 BGB (AGB-Neufassung) — §§ 133, 157 BGB (Auslegung)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Jede Änderung im Redline wird mit der maßgeblichen Norm in Kurzform zitiert:
- `[MaRisk AT 4.3.2 Novelle 2023]` – mit Modellwissens-Hinweis, wenn nicht aus Primärquelle
- `[§ 25a Abs. 1 S. 3 KWG – Proportionalität]`
- `[EBA/GL/2021/04 Rz. 45]` – für EBA-Leitlinien

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Lerch, ZAG, 2. Aufl. 2020, § 27 Rn. 20 ff.
- BaFin-Rundschreiben 09/2017 (BA) – MaRisk [Primärquelle; abrufbar: bafin.de]

## Beispiel

**Eingabe:** "Bitte die IKS-Richtlinie für GAP-2025-001 (MaRisk AT 4.3.2 – Datenhaltung) neu fassen. Richtlinie hochgeladen."

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], IKS-Richtlinie [Nutzer-Input]
> - **Gelesen:** § 4 IKS-Richtlinie, AT 4.3.2 MaRisk
> - **Zu Ihrer Einschätzung:** 1 Position `[prüfen]` – Aufbewahrungsfrist; Formulierung zur Datenklassifizierung ist Erstentwurf
> - **Vor Verwendung:** Rechts- und Compliance-Freigabe erforderlich; Inkrafttreten bis 31.12.2025

---

**VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS – ERSTENTWURF ZUR INTERNEN PRÜFUNG**

**IKS-Richtlinie – Redline-Entwurf**
*Version 2.0 (Entwurf) | Stand: 01.06.2025 | Änderungsgrund: MaRisk-Novelle 2023*

---

**§ 4 Aufbewahrungspflichten**

(2) Daten des Risikomanagements sowie sämtliche für die Beurteilung der wirtschaftlichen Verhältnisse des Instituts erforderliche Unterlagen sind für einen Zeitraum von ~~mindestens sieben (7) Jahren~~ **[NEU: mindestens zehn (10) Jahren]** aufzubewahren und jederzeit innerhalb angemessener Frist abrufbar zu halten. [MaRisk AT 4.3.2 Novelle 2023 – Modellwissen, prüfen]

**[NEU: (3) Eine schriftliche Dokumentation der Datenklassifizierung ist zu erstellen. Diese ist mindestens jährlich auf Aktualität zu prüfen und bei wesentlichen Änderungen unverzüglich zu aktualisieren. [MaRisk AT 4.3.2 Novelle 2023 – Modellwissen, prüfen]]**

---

**Änderungsübersicht:**
| § | Änderungstyp | Normgrundlage | Status |
|---|---|---|---|
| § 4 Abs. 2 | Friständerung 7 → 10 Jahre | MaRisk AT 4.3.2 | `[prüfen]` |
| § 4 Abs. 3 (neu) | Neuer Absatz Datenklassifizierung | MaRisk AT 4.3.2 | `[prüfen]` |

## Risiken / typische Fehler

- **Direktes Inkraftsetzen ohne Freigabe:** Der Redline-Entwurf ist ein Arbeitsdokument. Niemals ohne rechts- und compliance-seitige Freigabe sowie (bei KWG-Instituten) Geschäftsleiterzustimmung inkraftsetzen.
- **Wörtliche Übernahme von Normtext:** Aufsichtstext ist oft Mindeststandard, nicht optimaler Richtlinientext. Formulierungen ggf. konkretisieren.
- **Fehlende Schulungsmaßnahmen:** Neue Pflichten in internen Richtlinien wirken nicht ohne Mitarbeiterschulungen. Hinweis in Checkliste.
- **Versionskontrolle:** Jede Richtlinienänderung erfordert eine neue Versionsnummer und ein Änderungsprotokoll. Ohne Versionskontrolle ist die Richtlinie in BaFin-Prüfungen nur schwer nachzuweisen.
- **Proportionalitätsgrundsatz vergessen:** Für kleine und mittelgroße Institute gelten teils erleichterte Anforderungen (§ 25a Abs. 1 S. 3 KWG); Redline ggf. anpassen.

---

## Skill: `stellungnahmen`

_Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege Verhältnismäßigkeit. Output: strukturierte Stellungnahme mit Einzelanmerkungen Aenderungsvor..._

# Konsultationsbeiträge

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Konsultationsdokument (hochgeladen oder per Link)
- Aktives Praxisprofil (Behörden, Segment, Materialitätsschwelle)
- Optional: Eigene interne Richtlinien, die vom Entwurf berührt werden
- Optional: Vorherige Stellungnahmen derselben Behörde zur Konsistenzprüfung

## Ablauf

### 1. Konsultation erfassen

Falls noch nicht im Kommentar-Tracker eingetragen:

```yaml
konsultation:
 behoerde: "[BaFin / EBA / ESMA / BNetzA / EU-Kommission]"
 titel: "[Vollständiger Titel des Konsultationsdokuments]"
 referenz: "[z. B. BaFin-RS 2024/xx | EBA/CP/2024/xx]"
 kommentierungsfrist: "[TT.MM.JJJJ]"
 einreichungsform: "[E-Mail / Online-Portal / Postalisch]"
 einreichungsadresse: "[URL oder E-Mail]"
 status: "offen"
 entscheidung: "[teilnehmen / nicht teilnehmen / offen]"
 eigentuemer: "[Name / Team]"
```

Datei schreiben: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/comment-tracker.yaml`

### 2. Relevanzprüfung

Fragen:
1. Berührt der Entwurf das eigene Aufsichtssegment (z. B. KWG-Institut, ZAG-Institut, Wertpapierfirma WpIG)?
2. Enthält er neue Pflichten mit Übergangsfrist?
3. Weicht er von der bisherigen Praxis ab (MaRisk-Novelle, neue EBA-Leitlinie)?
4. Besteht Anlass zur inhaltlichen Einwirkung (z. B. unverhältnismäßige Anforderungen, Auslegungsunklarheiten)?

Ergebnis: **Teilnahmeempfehlung** (begründet) oder **Verzicht** (mit Begründung vermerkt).

### 3. Inhaltsanalyse des Entwurfs

Strukturierte Analyse:

| Nr. | Entwurfsabschnitt | Regelungsinhalt | Eigene Betroffenheit | Handlungsbedarf |
|---|---|---|---|---|
| 1 | [Abschnitt] | [Inhalt] | [hoch / mittel / gering] | [Kommentar / Umsetzung / keiner] |

Für jeden Abschnitt mit hoher Betroffenheit:
- Aktuelle Anforderung (aus Bestandsrichtlinien)
- Neue Anforderung laut Entwurf
- Delta / Lücke
- Formulierungsvorschlag für die Stellungnahme

### 4. Stellungnahmenentwurf

Format gemäß Behördenstandard:

**BaFin-Konsultationen:**
```
An: [E-Mail der BaFin-Fachabteilung]
Betreff: Stellungnahme zum Konsultationsentwurf [Titel], Ref. [RS-Nr.]

[Institution / Kanzlei]
[Datum]

Sehr geehrte Damen und Herren,

wir bedanken uns für die Möglichkeit zur Stellungnahme zum Konsultationsentwurf
[Titel] vom [Datum].

Allgemeine Anmerkungen:
[...]

Zu den einzelnen Abschnitten:

Zu Abschnitt [X]:
[Konkrete Anmerkung mit Normverweis]

Wir bitten um Berücksichtigung unserer Anmerkungen.

Mit freundlichen Grüßen
[Unterzeichner]
```

**EBA/ESMA-Konsultationen:**
Format nach dem offiziellen Antwortbogen der Behörde (Excel/Word-Template); Fragen der Behörde einzeln beantworten. Die Antworten sollen prägnant, normbezogen und mit Quellen belegt sein.

### 5. Fristenüberwachung

Alle offenen Konsultationen im Tracker prüfen:
- Frist < 14 Tage: 🔴 sofortiger Handlungsbedarf
- Frist 14–30 Tage: 🟠 Entwurf erstellen
- Frist > 30 Tage: 🟡 Beobachten

Tracker aktualisieren nach Einreichung:
```yaml
status: "eingereicht"
einreichungsdatum: "[TT.MM.JJJJ]"
einreichungsbestaetigung: "[Aktenzeichen / Eingangsbestätigung]"
```

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 47-51 GGO (Verbands-Anhörung, Stellungnahme-Verfahren) — Art. 41 GRCh (Recht auf gute Verwaltung, Anhörungsrecht) — §§ 28, 29 VwVfG (Anhörungsrecht im Verwaltungsverfahren) — §§ 2, 3 UmwRG (Verbandsklage, Stellungnahme)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen und Verlautbarungen:
- BaFin-Konsultationsverfahren: Bekanntmachung auf BaFin-Newsroom, bafin.de
- § 4 Abs. 2 FinDAG (Aufgaben der BaFin)
- Art. 16 EBA-Verordnung (EU) Nr. 1093/2010 (Leitlinien-Verfahren der EBA)
- Art. 10 ESMA-Verordnung (EU) Nr. 1095/2010 (Technische Standards)
- § 68 EnWG (BNetzA-Konsultationsverfahren)
- BaFin-Rundschreiben: z. B. RS 10/2012 (BA) – MaRisk [Modellwissen – prüfen auf aktuelle Fassung]

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Lerch, ZAG, 2. Aufl. 2020 (Zahlungsdiensteaufsicht).

## Beispiel

**Eingabe:** "BaFin hat einen Konsultationsentwurf zur MaRisk-Novelle veröffentlicht. Frist: 30.06.2025. Bitte analysieren und Stellungnahme vorbereiten."

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** BaFin-Newsroom [Websuche – prüfen], Konsultationsentwurf [Nutzer-Input]
> - **Gelesen:** Vollständiger Entwurf (40 Seiten)
> - **Zu Ihrer Einschätzung:** 3 Abschnitte mit hoher Betroffenheit markiert `[prüfen]`
> - **Vor Verwendung:** Fristen und Einreichungsmodalitäten gegen bafin.de verifizieren

---

**Konsultation erfasst:** BaFin-RS 2025/xx – MaRisk-Novelle, Frist: 30.06.2025

**Relevanzmatrix:**

| Nr. | Abschnitt | Regelungsinhalt | Betroffenheit |
|---|---|---|---|
| 1 | AT 4.3.2 | Neue Anforderungen an Datenhaltung | hoch `[prüfen]` |
| 2 | BT 3.1 | Erweiterung Stresstesting | mittel |
| 3 | BTR 2.3 | Liquiditätsrisikomanagement | gering |

**Stellungnahmenentwurf (Auszug):**

> Zu AT 4.3.2 (Datenhaltung):
> Wir regen an, die vorgeschlagene Aufbewahrungsfrist von 10 Jahren auf 7 Jahre zu begrenzen, da § 257 HGB und § 147 AO für Handelsbücher eine Frist von 10 Jahren vorsehen, für die hier relevanten operativen Daten jedoch keine vergleichbare Pflichtgrundlage besteht. [Modellwissen – prüfen]

## Risiken / typische Fehler

- **Fristversäumnis:** BaFin- und EBA-Fristen sind nicht verlängerbar; nach Fristablauf keine Einreichung mehr möglich. Frist im Kalender setzen und 14 Tage vorab mit 🔴 markieren.
- **Falsches Einreichungsformat:** BaFin: E-Mail an die zuständige Fachabteilung; EBA/ESMA: Offizielles Antwortformular zwingend. Formfehler führen zur Nichtberücksichtigung.
- **Übermäßige Länge:** Aufsichtsbehörden lesen kurze, präzise Stellungnahmen mit klaren Normverweisen bevorzugt. Maximallänge je nach Behörde beachten.
- **Mandantengeheimnis:** Stellungnahmen für externe Kunden müssen gemäß § 43a Abs. 2 BRAO als vertraulich behandelt werden; öffentliche Stellungnahmen bedürfen der Freigabe.
- **Verfasser-Angabe:** Viele Behörden veröffentlichen Stellungnahmen. Klären, ob anonym oder im Namen des Mandanten eingereicht werden soll.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

---

## Skill: `ustva-aufsichtskommunikation-grundregeln-dora`

_Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse Vorsteuer Fristen Sondervorauszahlung. Output: USt-Prüfprotokoll Voranmeldungs-Check..._

# Umsatzsteuer-Voranmeldung (§ 18 UStG)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Begleitet die fristgerechte und inhaltlich korrekte Abgabe von Umsatzsteuer-Voranmeldungen (UStVA) nach § 18 UStG. Er deckt die Bestimmung des richtigen Voranmeldungszeitraums, die Dauerfristverlängerung nach § 46 UStDV, die Berichtigung nach §§ 153 AO und 17 UStG sowie die technische Abgabe über ELSTER ab. Anwendungsfälle: monatliche oder quartalsweise UStVA erstellen, Dauerfristverlängerung beantragen, versehentlich falsche UStVA berichtigen, Übergang zwischen Voranmeldungszeiträumen.

## Eingaben

Das Modell benötigt:

- **Voranmeldungszeitraum des Mandanten**: monatlich, quartalsweise oder jährlich (Befreiung)?
- **Vorjahres-Zahllast**: Wie hoch war die USt-Zahllast des Vorjahres? (Maßgeblich für Zeitraum-Bestimmung)
- **Aktueller Zeitraum**: Welcher Monat/welches Quartal wird gemeldet?
- **Abzugebende Daten**: Umsätze (Steuersatz, steuerfreie Umsätze), Vorsteuer, innergemeinschaftliche Erwerbe, Reverse Charge?
- **Dauerfristverlängerung**: Beantragt? Sondervorauszahlung bereits entrichtet?
- **Berichtigungsbedarf**: Liegt ein Fehler in einer bereits abgegebenen UStVA vor? Welcher Art (Betrag, Steuersatz, Vorsteuer)?
- **ELSTER-Zugang**: Besteht ein zertifizierter ELSTER-Zugang (Unternehmen)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 18 Abs. 1 UStG**: Pflicht zur Abgabe der UStVA; Voranmeldungszeitraum grundsätzlich das Kalendervierteljahr; bei Jahres-Zahllast > 7.500 EUR: Kalendermonat (§ 18 Abs. 2 Satz 2 UStG); bei Jahres-Zahllast ≤ 1.000 EUR: Finanzamt kann von monatlicher/quartalsweiser Abgabe befreien (§ 18 Abs. 2 Satz 3 UStG).
- **§ 18 Abs. 1 Satz 4 UStG**: Abgabefrist: 10. Tag nach Ablauf des Voranmeldungszeitraums (10. Folgemonat).
- **§ 18 Abs. 2a UStG**: Neugründer: In den ersten zwei Jahren Monatsmeldung, unabhängig von Zahllast.
- **§ 18 Abs. 9 UStG**: Vergütungsverfahren für ausländische Unternehmer.
- **§ 46 UStDV (Dauerfristverlängerung)**: Verlängerung der Abgabe- und Zahlungsfrist um einen Monat auf Antrag; Voraussetzung für Monatszahler: Sondervorauszahlung i.H.v. 1/11 der Jahresvorauszahlung des Vorjahres bis zum 10. Februar des laufenden Jahres (§ 47 Abs. 1 UStDV); Quartalszahler: kein Sondervorauszahlungserfordernis.
- **§ 153 Abs. 1 AO**: Berichtigungspflicht bei erkanntem Fehler in einer Steuererklärung/-anmeldung; unverzügliche Anzeige beim Finanzamt, kein Verschulden erforderlich; Berichtigung = Selbstanzeige i.S.d. § 371 AO bei vorsätzlicher Verkürzung (Abgrenzung!).
- **§ 17 UStG**: Berichtigung des Steuerbetrags bei nachträglicher Änderung der Bemessungsgrundlage (z.B. Entgeltminderung, Rechnungskorrektur, Uneinbringlichkeit).

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Schritt 1 – Voranmeldungszeitraum bestimmen**
- Vorjahres-Zahllast ≤ 1.000 EUR: Befreiung möglich (§ 18 Abs. 2 Satz 3 UStG); Finanzamt entscheidet.
- Vorjahres-Zahllast > 1.000 EUR und ≤ 7.500 EUR: Quartalsmeldung (§ 18 Abs. 2 Satz 1 UStG).
- Vorjahres-Zahllast > 7.500 EUR: Monatsmeldung (§ 18 Abs. 2 Satz 2 UStG).
- Neugründer: erste zwei Kalenderjahre stets monatlich (§ 18 Abs. 2a UStG).

**Schritt 2 – Abgabefrist ermitteln**
- Regulär: 10. Tag nach Ablauf des Voranmeldungszeitraums (§ 18 Abs. 1 Satz 4 UStG).
- Beispiel: Januar-UStVA → Abgabe bis 10. Februar.
- Dauerfristverlängerung (§ 46 UStDV): Frist verschiebt sich um einen Monat (Januar → 10. März).
- Samstag/Sonntag/Feiertag: nächster Werktag (§ 108 Abs. 3 AO).

**Schritt 3 – Dauerfristverlängerung beantragen/sichern (§ 46 UStDV)**
- Antrag über ELSTER (Formular "Antrag auf Dauerfristverlängerung/Anmeldung der Sondervorauszahlung").
- Monatszahler: Sondervorauszahlung bis 10. Februar des Jahres entrichten (1/11 der Vorjahres-Zahllast).
- Quartalszahler: Antrag genügt, keine Sondervorauszahlung erforderlich.
- Sondervorauszahlung wird in der Dezember-UStVA/Jahreserklärung angerechnet.

**Schritt 4 – UStVA erstellen und abgeben**
- Ausfüllen über ELSTER (Pflicht zur elektronischen Abgabe, § 18 Abs. 1 Satz 1 UStG i.V.m. § 87a AO).
- Kennzahlen (KZ) korrekt zuordnen: KZ 81 (19 % USt), KZ 86 (7 % USt), KZ 66 (Vorsteuer), KZ 21 (ig Erwerbe), KZ 52 (Reverse Charge).
- Zahlungseingang beim Finanzamt spätestens am Fälligkeitstag (nicht nur Abgabe der Meldung).

**Schritt 5 – Berichtigung einer fehlerhaften UStVA**
- § 153 AO: Erkannter Fehler → unverzügliche Berichtigung, bevor der Fehler dem Finanzamt auffällt.
- Vorgehen: Korrigierte UStVA über ELSTER für den betreffenden Zeitraum einreichen (ersetzt vorherige Anmeldung).
- Abgrenzung § 371 AO: Berichtigung nur als Selbstanzeige wirksam, wenn der Fehler auf Vorsatz zur Steuerverkürzung zurückgeht; bloß fahrlässige Fehler = § 153 AO, keine Selbstanzeige erforderlich.
- § 17 UStG: Bei Änderung der Bemessungsgrundlage (Storno, Rechnungskorrektur, Skonto) Berichtigung in dem UStVA-Zeitraum, in dem die Änderung eingetreten ist (nicht rückwirkend).

**Schritt 6 – Folgen verspäteter oder fehlerhafter Abgabe**
- Verspätungszuschlag: bis zu 10 % der Steuer, max. 25.000 EUR (§ 152 AO); Ermessen des Finanzamts.
- Schätzung: Finanzamt kann Besteuerungsgrundlagen schätzen (§ 162 AO).
- Säumniszuschlag auf verspätete Zahlung: 1 % pro angefangenem Monat (§ 240 AO).

## Beispiel

**Sachverhalt**: GmbH G hatte im Jahr 2024 eine USt-Zahllast von 14.000 EUR. G hat keine Dauerfristverlängerung beantragt. Die Januar-2025-UStVA enthält einen Vorsteuerfehler (KZ 66 um 1.200 EUR zu hoch), den G am 15.03.2025 erkennt.

**Gutachtenstil**:

*Voranmeldungszeitraum*: Jahres-Zahllast 2024 = 14.000 EUR > 7.500 EUR → G ist zur monatlichen Voranmeldung verpflichtet (§ 18 Abs. 2 Satz 2 UStG).

*Abgabefrist Januar*: Ohne Dauerfristverlängerung: 10. Februar 2025 (§ 18 Abs. 1 Satz 4 UStG). Frist bereits abgelaufen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Dauerfristverlängerung für Zukunft*: G sollte für 2025 Dauerfristverlängerung beantragen (§ 46 UStDV); Sondervorauszahlung = 14.000/11 = 1.272,73 EUR (fällig bis 10.02.2025 – für 2025 ist Frist versäumt; ab 2026 beantragen).

## Risiken und typische Fehler

- **Voranmeldungszeitraum falsch**: Bei Überschreiten der 7.500-EUR-Schwelle im Vorjahr automatischer Wechsel zu monatlicher Meldepflicht – kein gesonderter Bescheid; viele Unternehmen erkennen den Wechsel nicht rechtzeitig.
- **Dauerfristverlängerung ohne Sondervorauszahlung**: Monatszahler, die keine Sondervorauszahlung leisten, haben keine wirksame Dauerfristverlängerung (BFH BFH/NV 2015, 569 Rn. 14); reguläre Frist gilt.
- **§ 153 AO vs. § 371 AO verwechseln**: Irrtümliche Behandlung als Selbstanzeige bei bloß fahrlässigen Fehlern ist unnötig; umgekehrt: bei Vorsatz reicht § 153 AO nicht.
- **§ 17 UStG-Berichtigungszeitpunkt**: Berichtigung bei Änderung der Bemessungsgrundlage gehört in den Zeitraum des Änderungsereignisses, nicht in den Ursprungszeitraum.
- **ELSTER-Pflicht**: Papieranmeldungen sind grundsätzlich nicht zulässig; nur in Härtefällen nach § 150 Abs. 8 AO ausnahmsweise möglich.
- **Zahlung ≠ Abgabe**: Fristwahrung erfordert sowohl rechtzeitige Abgabe der Meldung als auch rechtzeitigen Zahlungseingang beim Finanzamt (§ 18 Abs. 1 Satz 4 UStG).

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 18 UStG (UStVA-Pflicht, Fristen, Dauerfreistellung) — § 152 AO (Verspätungszuschlag) — § 370 AO (Steuerhinterziehung bei falscher UStVA) — ELSTER-Verfahren (elektronische Uebermittlungs-Pflicht) — § 233a AO (Zinsen bei Umsatzsteuer-Nachzahlung)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

