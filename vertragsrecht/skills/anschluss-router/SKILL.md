---
name: anschluss-router
description: "Einstieg, Schnelltriage und Fallrouting im Vertragsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Vertragsrecht."
---

# Vertragsrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; §§ 305 ff. BGB, NDA, SaaS- — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Vertragsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB §§ 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen.

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
| `abmahnung-uwg` | Unterstützt beim Verfassen und Prüfen von UWG-Abmahnungen nach § 13 UWG sowie der dazugehörigen modifizierten Unterlassungserklärung mit Vertragsstrafe und der Schutzschrift. Lädt, wenn ein Mandat eine… |
| `aenderungs-historie` | Verfolgt, wie sich ein Vertrag über Basisvertrag und alle Nachträge hinweg verändert hat – entweder als Gesamtüberblick aller Änderungen oder als Klausel-Rückverfolgung für eine bestimmte Bestimmung. Laden, wenn der… |
| `agb-pruefung` | Unterstützt bei der rechtlichen Prüfung von Allgemeinen Geschäftsbedingungen (AGB) auf Einbeziehung, Inhaltskontrolle und Transparenzgebot nach §§ 305–310 BGB. Lädt, wenn ein Mandat die Prüfung, Erstellung oder… |
| `eskalations-marker` | Ordnet ein Vertragsproblem dem richtigen Genehmiger per Eskalationsmatrix aus dem Praxisprofil zu und erstellt die Genehmigungsanfrage. Laden, wenn der Nutzer fragt "wer muss das genehmigen\", "eskalieren\", "braucht… |
| `lieferantenvertrag-pruefung` | Prüfung eines eingehenden Lieferanten- oder Dienstleistervertrags gegen das Playbook der Rechtsabteilung. Werk-/Dienstvertrag (§§ 631 und 611 BGB), Gewährleistung, Haftungsbegrenzung, LkSG-Anforderungen, CISG-Abwahl.… |
| `nda-durchsetzer` | Überarbeitet ein NDA der Gegenseite **konservativ im Änderungsmodus**, ohne Struktur, Nummerierung, Reihenfolge oder Look-&-Feel zu verändern, und erstellt parallel eine strukturierte Analyse (Executive Summary,… |
| `nda-pruefung` | Schnelle Triage von eingehenden NDA-/Geheimhaltungsvereinbarungen in GRÜN / GELB / ROT, damit nur die Vereinbarungen anwaltliche Zeit beanspruchen, die sie wirklich brauchen. Geeignet für Vertrieb und BD zur… |
| `pruefungsvorschlaege` | Prüft und genehmigt (oder lehnt ab) ausstehende Playbook-Aktualisierungsvorschläge des Playbook-Monitor-Agenten und überträgt genehmigte Änderungen in das Kanzleiprofil. Lädt, wenn der Monitor Vorschläge gemeldet hat,… |
| `saas-msa-pruefung` | Prüfung von SaaS-Abonnement- und Rahmenverträgen (MSA) mit Schwerpunkt auf AGB-Kontrolle (§§ 305–310 BGB), automatischer Verlängerung, Preiseskalation, Datenschutz (Art. 28 DSGVO), Haftungsbegrenzung und Vertragsstrafe… |
| `stakeholder-zusammenfassung` | Übersetzt ein Vertragsprüfungsmemo in eine Zusammenfassung für Geschäftsführung, Vorstand oder Einkauf — kein Rechtsgutachten, sondern eine klare Entscheidungsgrundlage. Lädt, wenn der Nutzer "Zusammenfassung für… |
| `vertragspruefung` | Prüft einen Vertrag gegen das Kanzlei-Playbook nach deutschem Recht. Identifiziert Vertragsstruktur anhand der Titelseite, ordnet das Dokument dem richtigen Prüfpfad zu (Lieferantenvertrag, NDA, AGB-Klauselkontrolle,… |
| `vertragsrecht-anpassen` | Geführte Anpassung des Kanzleiprofils im Vertragsrecht — ändert einzelne Einstellungen ohne erneutes Erstgespräch. Lädt, wenn der Nutzer "Profil anpassen\", "Playbook ändern\", "Eskalation aktualisieren\",… |
| `vertragsrecht-kaltstart-interview` | Führt das Erstgespräch zur Mandatsaufnahme im Vertragsrecht durch und schreibt das Kanzlei- bzw. Mandatsprofil. Lädt beim ersten Einsatz des Plugins, wenn die Konfigurationsdatei noch Platzhalter enthält oder wenn der… |
| `vertragsrecht-mandat-arbeitsbereich` | Verwaltet Mandatsarbeitsbereiche — neu anlegen, auflisten, wechseln, abschließen oder von Mandatsebene auf Kanzleiebene wechseln. Lädt, wenn ein Anwalt mit mehreren Mandanten ein neues Mandat anlegen, zum aktiven… |
| `vertragsverlaengerungs-monitor` | Zeigt Verträge mit ablaufenden Kündigungsfristen an und warnt rechtzeitig, bevor Verlängerungs-/Kündigungsfenster schließen. Relevant insbesondere bei § 309 Nr. 9 BGB (automatische Verlängerung). Laden, wenn der Nutzer… |
| `widerruf-fernabsatz` | Unterstützt bei Fragen zum Widerrufsrecht im Fernabsatzrecht nach §§ 312g und 355 BGB: Belehrungspflichten, Fristberechnung, Rechtsfolgen des Widerrufs und Ausnahmen. Lädt, wenn ein Mandat Widerrufsbelehrung,… |

## Worum geht es?

Dieses Plugin unterstuetzt Rechtsanwaelte und Unternehmensjuristen bei der Pruefung, Verhandlung und Verwaltung von Vertraegen nach deutschem Recht. Schwerpunkte sind Lieferanten- und Dienstleistervertraege, AGB-Kontrolle nach §§ 305 ff. BGB, Nichtoffenbarungsvereinbarungen (NDA), SaaS- und Rahmenvertraege sowie das Widerrufsrecht im Fernabsatz.

Das Plugin arbeitet mit einem Kanzlei-Playbook-Konzept: Einmal definierte Standards (Roter Bereich, Gelber Bereich, Gruenes Licht) werden bei jeder Vertragspruefung konsistent angewendet. Ergebnisse werden entweder als juristisches Memo oder als vereinfachte Stakeholder-Zusammenfassung ausgegeben.

## Wann brauchen Sie diese Skill?

- Die Rechtsabteilung erhaelt einen Lieferantenvertrag der Gegenseite und will ihn gegen das eigene Playbook pruefen.
- Ein Unternehmen will ein NDA auf kritische Klauseln (Geheimhaltungsumfang, Laufzeit, Rueckgabe) pruefen lassen.
- Ein SaaS-Anbieter oder -Kaeufer prueft einen Subscription Agreement auf AGB-Konformitaet und automatische Verlaengerungsklauseln.
- Eine UWG-Abmahnung ist eingegangen und muss beantwortet oder selbst verfasst werden.
- Ein Vertrag laeuft aus und die Kuendigungs- oder Verlaengerungsfrist ist knapp.

## Fachbegriffe (kurz erklaert)

- **AGB** — Allgemeine Geschaeftsbedingungen; vorformulierte Vertragsbedingungen unterliegen der Inhaltskontrolle nach §§ 307-309 BGB.
- **NDA** — Non-Disclosure Agreement (Nichtoffenbarungsvereinbarung); verpflichtet Parteien zur Geheimhaltung vertraulicher Informationen.
- **MSA** — Master Service Agreement; Rahmenvertrag für wiederkehrende Leistungsbeziehungen, ergaenzt durch spezifische Leistungsbeschreibungen.
- **Playbook** — Internes Regelwerk der Rechtsabteilung mit Mindestanforderungen und Roten Linien für Vertragsverhandlungen.
- **Eskalationsmatrix** — Festgelegte Zuständigkeiten für die Genehmigung von Vertragsabweichungen nach Risikohoehe.
- **Fernabsatz** — Vertragsschluss ohne gleichzeitige Anwesenheit via Internet, Telefon oder Katalog; loest Widerrufsrecht nach § 312g BGB aus.
- **UWG** — Gesetz gegen den unlauteren Wettbewerb; regelt Abmahnungen bei wettbewerbswidrigen Handlungen.

## Rechtsgrundlagen

- §§ 305-310 BGB (AGB-Kontrolle)
- §§ 311-313 BGB (Schuldverhaeltnisse, culpa in contrahendo, Stoerung der Geschaeftsgrundlage)
- §§ 631 ff. BGB (Werkvertrag), §§ 611 ff. BGB (Dienstvertrag)
- §§ 312g, 355 BGB (Widerrufsrecht im Fernabsatz)
- § 13 UWG (Abmahnung im Wettbewerbsrecht)
- §§ 17-18 GeschGehG (Geschaeftsgeheimnisschutz, relevant für NDA)
- § 307 BGB (Generalklausel Inhaltskontrolle)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Vertragstyp, Vertragspartnerrolle (Lieferant, Auftraggeber, Lizenznehmer) und Rechtsabteilungs-Profil.
2. Kanzlei-Profil aufnehmen oder aktualisieren (`vertragsrecht-kaltstart-interview` oder `vertragsrecht-anpassen`).
3. Passenden Skill auswaehlen (z. B. NDA-Pruefung, Lieferantenvertrag, AGB, SaaS/MSA, Abmahnung).
4. Eilfristen pruefen: Kuendigungsfristen, Verlaengerungsfristen, Abmahn-Fristen.
5. Anschluss-Skill bestimmen: Gegenentwurf erstellen, Eskalation oder Stakeholder-Zusammenfassung?

## Skill-Tour (was gibt es hier?)

- `vertragsrecht-kaltstart-interview` — Erstgespraech zur Mandatsaufnahme im Vertragsrecht; Kanzlei- oder Mandatsprofil anlegen.
- `vertragsrecht-mandat-arbeitsbereich` — Mandatsarbeitsbereiche verwalten: neu anlegen, auflisten, wechseln oder abschliessen.
- `vertragsrecht-anpassen` — Kanzleiprofil im Vertragsrecht gezielt anpassen ohne erneutes Erstgespraech.
- `vertragspruefung` — Vertrag gegen das Kanzlei-Playbook nach deutschem Recht pruefen und Risikokategorien ausweisen.
- `lieferantenvertrag-pruefung` — Eingehenden Lieferanten- oder Dienstleistervertrag gegen das Playbook pruefen (Werk-/Dienstvertrag, Haftungscaps).
- `nda-pruefung` — Schnelle Triage eingehender NDA in Gruen/Gelb/Rot; nur auffaellige Vereinbarungen eskalieren.
- `nda-durchsetzer` — NDA der Gegenseite konservativ im Aenderungsmodus ueberarbeiten ohne Struktur zu veraendern.
- `agb-pruefung` — AGB auf Einbeziehung, Inhaltskontrolle nach §§ 305-310 BGB und unwirksame Klauseln pruefen.
- `saas-msa-pruefung` — SaaS-Abonnement- und Rahmenvertraege pruefen (AGB-Kontrolle, automatische Verlaengerung, Datenschutzklauseln).
- `abmahnung-uwg` — UWG-Abmahnung verfassen oder pruefen sowie modifizierte Unterlassungserklaerung entwerfen.
- `widerruf-fernabsatz` — Widerrufsrecht im Fernabsatz nach §§ 312g und 355 BGB pruefen; Belehrungspflichten und Fristberechnungen.
- `eskalations-marker` — Vertragsproblem dem richtigen Genehmiger per Eskalationsmatrix zuordnen und Genehmigungsanfrage erstellen.
- `stakeholder-zusammenfassung` — Vertragspruefungsmemo in eine Zusammenfassung für Geschaeftsfuehrung oder Einkauf uebersetzen.
- `aenderungs-historie` — Veraenderungen eines Vertrags ueber Basisvertrag und Nachtraege hinweg nachvollziehen.
- `vertragsverlaengerungs-monitor` — Vertraege mit ablaufenden Kuendigungsfristen anzeigen und rechtzeitig warnen.
- `pruefungsvorschlaege` — Ausstehende Playbook-Aktualisierungsvorschlaege pruefen und genehmigen oder ablehnen.

## Worauf besonders achten

- AGB-Kontrolle im B2B-Verkehr: § 307 BGB gilt auch zwischen Kaufleuten; marktunuebliche Haftungsausschluesse koennen unwirksam sein.
- Kuendigungsfristen in laufenden Vertraegen pruefen, bevor Verlaengerungsautomatik greift — besonders bei SaaS-Vertraegen.
- NDA-Laufzeiten: Zeitlich unbeschraenkte Geheimhaltungspflichten koennen nach deutschem Recht problematisch sein.
- Fernabsatz-Widerrufsrecht gilt auch im B2C-SaaS: 14 Tage Widerrufsfrist, Belehrungspflicht vor Vertragsschluss.
- Abmahnungen nach UWG haben kurze Reaktionsfristen — Unterlassungserklaerung nicht vorschnell unterzeichnen.

## Typische Fehler

- Haftungsklauseln in AGB ohne Differenzierung nach Verschuldensgrad: Totalausschluss ist nach § 309 Nr. 7 BGB unwirksam.
- NDA mit unklarem Schutzgegenstand: Was als vertraulich gilt, ist nicht hinreichend definiert — im Streitfall beweisbar schwach.
- SaaS-Vertraege ohne Datenrueckgabeklausel: Mandant verliert Zugang zu Daten nach Vertragsende.
- Verlaengerungsklausel uebersehen: Vertrag verlaengert sich automatisch um ein Jahr, weil Kuendigungsfenster verpasst wurde.
- Playbook nicht auf aktuellen Gesetzesstand gebracht: AGB-Aenderungen durch EuGH-Rechtsprechung oder BGH-Urteile werden nicht eingepflegt.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- BGB in der zum Stand-Datum geltenden Fassung
- UWG in der geltenden Fassung

