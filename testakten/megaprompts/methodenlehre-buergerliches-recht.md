# Megaprompt: methodenlehre-buergerliches-recht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 136 Skills (gekuerzt fuer Chat-Fenster) des Plugins `methodenlehre-buergerliches-recht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Methodenlehre Bürgerliches Recht: ordnet Rolle (Studierender, Anwalt, Richter), markier…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Methodenlehre Buergerliches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterla…
3. **methodenlehre-erstpruefung-und-mandatsziel** — Dieses Skill leitet die methodische Erstprüfung eines neuen Mandats an und hilft, das Mandatsziel präzise zu definieren:…
4. **abschlussprodukt-uebergabe** — Dieses Skill definiert und strukturiert das juristische Abschlussprodukt eines zivilrechtlichen Mandats und leitet die m…
5. **abwaegung-gewichtung-intensitaet** — Unterstützt die methodisch saubere Gewichtung kollidierender Rechtspositionen nach Intensität, Rang, Normzweck und Eingr…
6. **abwaegung-material-auswahl** — Leitet durch die methodisch begründete Auswahl von Abwägungsmaterial im Zivilrecht. Das Skill zeigt, welche Fakten, Norm…
7. **abwaegungslast-non-liquet** — Behandelt die methodische Frage, wie mit Abwägungslagen umzugehen ist, in denen das Material keine eindeutige Entscheidu…
8. **abwaegungszustaendigkeit-institutionen** — Klärt, welche Institution im Rechtssystem für eine konkrete Abwägungsentscheidung zuständig ist — Gesetzgeber, Gericht, …

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Methodenlehre Bürgerliches Recht: ordnet Rolle (Studierender, Anwalt, Richter), markiert Frist (keine harten Fristen), wählt Norm (BGB, Art. 20 III GG (Auslegung)) und Zuständigkeit (zuständige Stelle), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Methodenlehre Buergerliches Recht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abschlussprodukt-uebergabe` — Abschlussprodukt Uebergabe
- `abwaegung-gewichtung-intensitaet` — Abwaegung Gewichtung Intensitaet
- `abwaegung-material-auswahl` — Abwaegung Material Abwaegungslast NON
- `abwaegung-material-auswahl` — Abwaegung Material Auswahl
- `abwaegungslast-non-liquet` — Abwaegungslast NON Liquet
- `abwaegungszustaendigkeit-institutionen` — Abwaegungszustaendigkeit
- `abwaegungszustaendigkeit-institutionen` — Abwaegungszustaendigkeit Institutionen
- `analogie-und-teleologische-reduktion` — Analogie und Teleologische Reduktion
- `anspruchsgrundlagen-behoerden-gericht-und-registerweg` — Anspruchsgrundlagen Anwaltsperspektive
- `argumentum-figuren-e-contrario-a-maiore-a` — Argumentum Figuren E Contrario A Maiore A
- `auslegung-rechtsfortbildung-grenzprotokoll` — Auslegung Rechtsfortbildung Grenzprotokoll
- `begruendung-anhoerung-adressatenfaehigkeit` — Begruendung Anhoerung Adressatenfaehigkeit
- `bverfg-grenzen-richterlicher-rechtsfortbildung` — Bverfg Grenzen Diskurstheorie Habermas
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Regelungs- und Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 1 Abs. 1 GG` — normative Grenze jeder Rechtsanwendung.
- `Art. 20 Abs. 3 GG` — Gesetzesbindung und Rechtsbindung.
- `Art. 19 Abs. 4 GG` — effektiver Rechtsschutz.
- `Art. 97 Abs. 1 GG` — richterliche Unabhaengigkeit.
- `§ 133 BGB` — Auslegung von Willenserklaerungen.
- `§ 157 BGB` — Vertragsauslegung nach Treu und Glauben.
- `§ 242 BGB` — Korrektiv der Rechtsausuebung.
- `§ 1 StGB` — Bestimmtheit im Strafrecht.
- `Art. 6 Abs. 1 EMRK` — faires Verfahren.
- `Art. 47 GRCh` — wirksamer Rechtsbehelf.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Methodenlehre Buergerliches Recht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Methodenlehre Buergerliches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Ski..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Methodenlehre Buergerliches Recht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Regelungs- und Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 1 Abs. 1 GG` — normative Grenze jeder Rechtsanwendung.
- `Art. 20 Abs. 3 GG` — Gesetzesbindung und Rechtsbindung.
- `Art. 19 Abs. 4 GG` — effektiver Rechtsschutz.
- `Art. 97 Abs. 1 GG` — richterliche Unabhaengigkeit.
- `§ 133 BGB` — Auslegung von Willenserklaerungen.
- `§ 157 BGB` — Vertragsauslegung nach Treu und Glauben.
- `§ 242 BGB` — Korrektiv der Rechtsausuebung.
- `§ 1 StGB` — Bestimmtheit im Strafrecht.
- `Art. 6 Abs. 1 EMRK` — faires Verfahren.
- `Art. 47 GRCh` — wirksamer Rechtsbehelf.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Methodenlehre Buergerliches Recht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Methodenlehre und Rechtsanwendung im deutschen buergerlichen Recht aus Anwaltsperspektive. Gutachtenstil. Anspruchsgrundlagen-Reihenfolge. Auslegung Wortlaut System Historie Telos pragmatisch ohne starren Vorrang. Verfassungs- und unionsrechtskonforme Auslegung. Lueckenfuellung. Verjährung.

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

Das Plugin enthält 20 Skills, gegliedert in fünf Blöcke. Für eine konkrete zivilrechtliche Bewertung reicht meistens `methodenlehre-anwenden` plus ein oder zwei Vertiefungsskills aus den Auslegungs- oder Rechtsfortbildungs-Blöcken. Die Strömungs-Skills sind für Hausarbeiten, Methoden-Memos und akademische Diskussion gedacht.

**Block A — Praxis-Einstieg und Anwendung**

| Skill | Wann vorschlagen? |
|---|---|
| `methodenlehre-anwenden` | Immer dann, wenn eine zivilrechtliche Frage methodisch sauber geprüft werden soll: Anspruchsgrundlagen-Reihenfolge, Auslegung der einschlägigen Norm nach Wortlaut/System/Historie/Telos, Lückenfüllung durch Analogie oder teleologische Reduktion. |
| `methoden-mix-in-der-praxis-anwaltsschriftsatz` | Wenn ein Anwaltsschriftsatz mehrere Auslegungsmethoden bewusst kombinieren soll. Vorrangdiskussion (Larenz vs. BGH-pragmatisch). Formulierungsmuster für offene und geschlossene Rechtslagen. |

**Block B — Klassische Auslegungskanones (Savigny-Vierer)**

| Skill | Wann vorschlagen? |
|---|---|
| `savigny-vier-auslegungsmethoden` | Wenn das Gerüst der vier Auslegungsmethoden gebraucht wird. Theoretische Grundlage, Werkstand, Verhältnis zur modernen pragmatischen Auslegung. |
| `wortlaut-grammatikalische-auslegung` | Wenn der Wortlaut trägt oder als Grenze diskutiert werden muss. Legaldefinitionen, Mehrdeutigkeit, unbestimmte Rechtsbegriffe. |
| `systematische-auslegung` | Wenn Stellung der Norm, Nachbarnormen, Verweisungen oder Konkordanz mit HGB/ZPO/GG/Unionsrecht den Ausschlag geben. |
| `historische-auslegung` | Wenn Gesetzesmaterialien Argumente liefern. Bundestags-Drucksachen, Ausschussberichte, Schuldrechtsmodernisierung 2002 und neuere Reformen. über dipbt.bundestag.de. |
| `teleologische-auslegung` | Wenn Sinn und Zweck der Norm das stärkste Argument ist — in der BGH-Praxis fast immer. Schutzzwecknormen. |

**Block C — Verfassungs- und Unionsrechtskonforme Auslegung**

| Skill | Wann vorschlagen? |
|---|---|
| `verfassungs-und-unionsrechtskonforme-auslegung` | Wenn Grundrechte mittelbare Drittwirkung entfalten (BVerfGE 7, 198) oder eine Norm unionsrechtlichen Ursprung hat (Marleasing, von Colson). Grenzen contra legem. |

**Block D — Rechtsfortbildung und Argumentationsfiguren**

| Skill | Wann vorschlagen? |
|---|---|
| `analogie-und-teleologische-reduktion` | Wenn die Wortlaut-Grenze überschritten werden muss. Planwidrige Lücke, vergleichbare Interessenlage. Drittschadensliquidation, Vertrag mit Schutzwirkung Dritter, § 906 II 2 BGB analog. |
| `argumentum-figuren-e-contrario-a-maiore-a-fortiori` | Wenn ein Umkehrschluss, Erst-recht-Schluss oder a fortiori-Argument trägt oder zurückgewiesen werden muss. Verhältnis zur Analogie. |

**Block E — Methodische Strömungen und Theoriegeschichte**

| Skill | Wann vorschlagen? |
|---|---|
| `pandekten-und-begriffsjurisprudenz` | Wenn Begriffspyramide oder logisches Ableitungsmodell zu erkennen oder zu kritisieren ist. AT, Stellvertretungsrecht. |
| `interessenjurisprudenz-heck` | Wenn ratio legis als Interessenabwägung formuliert werden soll. Vorstufe zur Wertungsjurisprudenz. |
| `wertungsjurisprudenz-larenz-canaris` | Wenn objektive Wertungen und Grundrechtsdogmatik die Auslegung tragen. Hauptströmung der deutschen Privatrechtslehre seit der Nachkriegszeit. |
| `topik-viehweg-vs-systemdenken` | Wenn Problemdenken statt Systemdenken überzeugt: Generalklauseln, Vertragsauslegung, Schiedsverfahren. |
| `diskurstheorie-habermas-alexy` | Wenn Diskursregeln und Anspruch auf Richtigkeit als methodische Stufe gebraucht werden. Verhältnismäßigkeit, Abwägung. |
| `systemtheorie-luhmann-rechtssystem-autopoiese` | Wenn das Recht als operativ geschlossenes autopoietisches System beschrieben werden soll. BGH als Beobachter zweiter Ordnung. |
| `oekonomische-analyse-des-rechts-coase-posner` | Wenn Effizienzargumente diskutiert werden. Coase-Theorem, Transaktionskosten. Schadens-, Vertrags-, Nachbarrecht. |
| `legal-realism-und-critical-legal-studies` | Wenn eine kritische Außensicht auf die deutsche Wertungsjurisprudenz nötig ist. Holmes, Llewellyn, Frank, Unger, Kennedy. |
| `rechtspluralismus-und-mehrebenen-system` | Wenn parallele Rechtsordnungen, lex mercatoria, Sport-Schiedsgerichte oder die Mehrebenenordnung Deutschland/EU mitgedacht werden müssen. |

**Routing-Faustregel:**

- *Schnelle Erstbewertung einer zivilrechtlichen Frage* → `methodenlehre-anwenden` direkt aktivieren.
- *Auslegung einer konkreten Norm* → `methodenlehre-anwenden` plus den zur tragenden Methode passenden Skill aus Block B (Wortlaut, System, Historie, Telos).
- *Wortlaut zu weit oder zu eng* → zusätzlich `analogie-und-teleologische-reduktion` und ggf. `argumentum-figuren-e-contrario-a-maiore-a-fortiori`.
- *Norm hat unionsrechtlichen Ursprung* → zusätzlich `verfassungs-und-unionsrechtskonforme-auslegung`.
- *Anwaltsschriftsatz mit mehreren Argumentationslinien* → `methoden-mix-in-der-praxis-anwaltsschriftsatz`.
- *Hausarbeit, Methoden-Memo, akademische Reflexion* → passende Skills aus Block E (Strömungen).
- *BGB-AT-Detailprüfung (Vertragsschluss, Anfechtung, Stellvertretung, Form, Verjährung)* → Plugin `bgb-at-pruefer` zusätzlich hinzuladen; dieses Plugin bleibt die methodische Klammer.
- *Zitierfragen* → Plugin `zitierweise-deutsches-recht`.
- *Konkrete Rechtsgebiete* (Erbrecht, Arbeitsrecht, Familienrecht, Gesellschaftsrecht etc.) → das jeweilige Fachplugin; die Methodenlehre dieses Plugins gilt als Grundierung.

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

---

## Skill: `methodenlehre-erstpruefung-und-mandatsziel`

_Dieses Skill leitet die methodische Erstprüfung eines neuen Mandats an und hilft, das Mandatsziel präzise zu definieren: Es zeigt, wie a..._

# Dieses Skill leitet die methodische Erstprüfung eines neuen Mandats an und hilft, das Mandatsziel präzise zu definieren


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Dieses Skill leitet die methodische Erstprüfung eines neuen Mandats an und hilft, das Mandatsziel präzise zu definieren. Es zeigt, wie aus dem Mandantenanliegen eine rechtlich präzise Fragestellung entwickelt wird, welche Auslegungsmethoden für die Erstprüfung heranzuziehen sind und wie Mandatsziel, Rechtsfrage und Bearbeitungsstrategie methodisch aufeinander abgestimmt werden. Das Skill sichert von Anfang an die methodische Kohärenz des Mandats.

### Erstprüfung und Mandatszieldefinition

## Fachlicher Kern — Juristische Methodenlehre
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstprüfung und Mandatszieldefinition` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** Wortlaut, Systematik, Historie, Telos, Verfassung, Unionsrecht, Analogie, teleologische Reduktion, Generalklauseln, Präjudizien, Beweislast und prozessuale Umsetzbarkeit.
- **Verifizierte Anker:** Dworkin als Prinzipien-/Integritätskontrolle für hard cases; Kelsen als Normstufen-/Kompetenzhygiene; Canaris-Systemdenken und Larenz-Wertungsjurisprudenz kritisch prüfen, Larenz’ NS-Vergangenheit und autoritäre Ordnungsnähe nicht ausblenden.
- **Arbeitsmodus:** Keine Formel behaupten („Ausnahmen eng“, „h.M.“), sondern Normzweck, Lücke, Vergleichbarkeit, Kompetenz, Bindung und Folgen offenlegen; Rechtsfortbildung nur mit sauberem Grenzprotokoll.
- **Outputpflicht:** Auslegungsmatrix, Lückenprotokoll, Schriftsatzargument, Gutachtenbaustein, Richterrechts-Red-Team oder Begründungscheck.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

Die erste methodische Weichenstellung eines Mandats entscheidet über Effizienz und Erfolg der gesamten Bearbeitung. Wer das Mandatsziel präzise definiert und die Erstprüfung methodisch strukturiert, vermeidet Sackgassen und Doppelarbeit. Dieses Skill trainiert den systematischen Einstieg in neue Mandate, von der ersten Mandantenschilderung bis zur belastbaren Ersteinschätzung.

## Mandantenfall

- Ein Unternehmer schildert telefonisch einen Vertragsstreit in drei Sätzen. Das Skill hilft, aus dieser Kurzdarstellung die relevanten Rechtsfragen zu extrahieren, ein provisorisches Mandatsziel zu formulieren und die nächsten Klärungsschritte zu benennen.
- Eine Privatperson erscheint mit einem Stapel Dokumente und einer vagen Beschwerde über einen Nachbarn. Das Skill strukturiert das Erstgespräch, filtert die rechtlich relevanten Aspekte heraus und formuliert das Mandatsziel als konkrete Rechtsfrage.
- Eine Unternehmerin schildert eine Situation, die gleichzeitig vertragsrechtliche, deliktische und öffentlich-rechtliche Aspekte enthält. Das Skill hilft, die verschiedenen Rechtsfragen zu priorisieren und ein klares Mandatsziel zu definieren, das die Ressourcen des Mandats optimal einsetzt.

## Erste Schritte

1. Höre die Mandantenschilderung vollständig an und erfasse den Sachverhalt ohne vorschnelle Einordnung.
2. Formuliere auf Basis der Schilderung eine vorläufige Rechtsfrage: "Welches Recht gibt wem welchen Anspruch gegen wen aus welchem Grund?"
3. Prüfe, welche Anspruchsgrundlagen prima facie in Betracht kommen, und erstelle eine Rangfolge nach Erfolgswahrscheinlichkeit.
4. Definiere das Mandatsziel: Durchsetzung, Abwehr, Beratung, Vertragsgestaltung oder präventive Risikoklärung?
5. Identifiziere sofortigen Handlungsbedarf (Fristen, einstweilige Verfügung, Verjährungsunterbrechung).
6. Dokumentiere Mandatsziel, vorläufige Rechtsfrage und nächste Schritte im Erstprotokoll.

## Rechtsrahmen

- § 133 BGB — Auslegung als erster methodischer Schritt bei unklarem Sachverhalt
- § 157 BGB — Interessengerechte Auslegung des Mandantenanspruchs
- § 675 BGB — Anwaltsvertrag; Pflicht zur klaren Mandatszieldefinition und Aufklärung
- § 195 BGB — Verjährungsfristen; sofortiger Prüfpunkt in der Erstprüfung
- § 12 BORA — Pflicht zur Interessenklarstellung und Mandatsbegrenzung

## Prüfraster

1. Ist der Sachverhalt vollständig und ohne Wertungsverzerrung erfasst?
2. Sind alle prima-facie relevanten Anspruchsgrundlagen identifiziert?
3. Ist das Mandatsziel klar und mit dem Mandanten abgestimmt?
4. Sind sofortige Handlungsbedarfe (Fristen, einstweiliger Rechtsschutz) erkannt und dokumentiert?
5. Ist die Erstprüfung methodisch strukturiert (Auslegung, Anspruchsprüfung, Risikoeinschätzung)?
6. Ist das Erstprotokoll vollständig und als Ausgangsdokument für die weitere Bearbeitung geeignet?

## Typische Fallstricke

- Das Mandatsziel wird nicht klar definiert, was zu divergierenden Erwartungen zwischen Anwalt und Mandant führt.
- Fristen werden bei der Erstprüfung nicht geprüft, sodass sofortiger Handlungsbedarf übersehen wird.
- Die Erstprüfung konzentriert sich auf eine offensichtliche Anspruchsgrundlage und übersieht günstigere Alternativen.
- Das Erstprotokoll wird nicht dokumentiert, was bei späteren Meinungsverschiedenheiten keine Grundlage bietet.

## Quellen

- [§ 133 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__133.html)
- [§ 675 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__675.html)
- [§ 195 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__195.html)
- [§ 12 BORA auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bora/__12.html)
- [dejure.org Anwaltspflichten Erstberatung](https://dejure.org/gesetze/BRAO/43a.html)

## Abgrenzungen und Methodik

Die Erstprüfung ist methodisch von der vollständigen Rechtsprüfung zu unterscheiden: Sie dient der Orientierung
und der Bestimmung des Mandatsziels, nicht der abschließenden Klärung aller Rechtsfragen. Eine zu tiefe
Erstprüfung kann Zeit und Ressourcen verschwenden, die besser in die eigentliche Mandatsbearbeitung investiert
werden sollten. Umgekehrt darf die Erstprüfung so oberflächlich nicht sein, dass wichtige Fristen oder Risiken
übersehen werden.

## Praktische Anwendungshinweise

Das Erstprotokoll sollte spätestens 24 Stunden nach dem Erstgespräch erstellt sein. Es bildet die Grundlage
für die Honorarvereinbarung und die Mandatserteilung. Wenn bei der Erstprüfung bereits erkennbar ist, dass
das Mandat außerhalb der eigenen Kompetenz liegt, muss der Mandant sofort an einen spezialisierten Kollegen
verwiesen werden. Die Erstprüfung ist auch Ausgangspunkt für die Interessenkonfliktprüfung (§ 12 BORA),
die vor jeder Mandatsübernahme zwingend durchzuführen ist.

## Hinweis zur Methodensicherheit

Die methodische Konsistenz der Argumentation ist nicht nur ein akademisches Qualitätsmerkmal, sondern hat
unmittelbare Konsequenzen für die Überzeugungskraft vor Gericht und in der Verhandlung. Inkonsequente
oder widersprüchliche Argumentation wird von gut vorbereiteten Gegenseiten ausgenutzt und kann einen
substanziell starken Fall erheblich schwächen. Die konsequente Anwendung methodischer Prinzipien
schützt die eigene Position und macht sie resilient gegenüber Angriffen.

---

## Skill: `abschlussprodukt-uebergabe`

_Dieses Skill definiert und strukturiert das juristische Abschlussprodukt eines zivilrechtlichen Mandats und leitet die methodisch korrekte Übergabe an den Mandanten an. Es zeigt, welche Dokumente am Ende eines Mandats zu übergeben sind, wie ein Abschlussprotokoll erstellt wird, wie offene Risiken..._

# Bürgerliches Abschlussprodukt und Übergabe

## Fachlicher Anker

- **Normen:** § 675 BGB, § 242 BGB, § 43a Abs. 4 BRAO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Mandantenfall

- Ein Mandant hat einen Vergleich vor dem Landgericht geschlossen. Das Abschlussprotokoll muss den Vergleichsinhalt, die vollstreckbaren Pflichten, offene steuerliche Fragen und Verjährungshinweise für etwaige Restansprüche dokumentieren.
- Eine Unternehmerin hat einen langen Vertragsstreit außergerichtlich beigelegt. Die Übergabe umfasst die vollständige Vertragsakte, das Einigungsprotokoll, offene steuerliche und handelsrechtliche Folgen sowie Hinweise zur internen Dokumentation für spätere Audits.
- Ein Mandant hat ein Klageverfahren verloren. Die Übergabe muss das Urteil erläutern, Rechtsmittelmöglichkeiten benennen, Fristen setzen und den Mandanten über die Kostenfolgen informieren, bevor das Mandat abgeschlossen wird.

## Erste Schritte

1. Erstelle eine vollständige Liste aller im Mandat erstellten Dokumente (Schriftsätze, Gutachten, Verträge, Korrespondenz, Beschlüsse, Urteile).
2. Formuliere ein Abschlussprotokoll, das das Mandatsergebnis, offene Verpflichtungen und Risiken zusammenfasst.
3. Prüfe alle offenen Fristen (Vollstreckungsfristen, Rechtsmittelfristen, Verjährungsfristen für Restansprüche) und dokumentiere diese.
4. Weise den Mandanten auf potenzielle Folgerisiken hin (Steuerfolgen, Auswirkungen auf Drittverträge, Registerpflichten).
5. Übergib vollständige Mandatsakte (physisch oder digital) und hole eine schriftliche Empfangsbestätigung ein.
6. Beende das Mandat formal durch Abschlussschreiben mit Zusammenfassung des Ergebnisses und Empfehlung für weitere Schritte.

## Rechtsrahmen

- § 675 BGB — Geschäftsbesorgungsvertrag; anwaltliche Pflichten zur ordnungsgemäßen Mandatsführung
- § 242 BGB — Treu und Glauben; Aufklärungspflicht des Anwalts gegenüber dem Mandanten
- § 43a Abs. 4 BRAO — Verschwiegenheitspflicht; Grenzen der Mandatsdokumentation
- § 50 BRAO — Pflicht zur Aktenführung und Aufbewahrung
- § 195 BGB — Regelverjährung; relevant für Hinweise auf noch offene Ansprüche nach Mandatsende

## Prüfraster

1. Sind alle Mandatsdokumente vollständig und geordnet in der Akte?
2. Ist das Abschlussprotokoll vollständig und klar formuliert?
3. Sind alle offenen Fristen dokumentiert und dem Mandanten mitgeteilt?
4. Wurden Folgerisiken und -pflichten vollständig aufgezeigt?
5. Ist die Kostenrechnung erstellt und dem Mandanten übergeben?
6. Wurde die Mandatsakte zur Übergabe freigegeben und eine Empfangsbestätigung eingeholt?
7. Sind Aufbewahrungsfristen für die Anwaltskanzlei dokumentiert?

## Typische Fallstricke

- Restansprüche verjähren nach Mandatsabschluss, weil der Mandant nicht auf offene Fristen hingewiesen wurde.
- Steuer- und registerrechtliche Folgen des Mandatsergebnisses werden nicht kommuniziert.
- Die Mandatsakte wird unvollständig übergeben, was bei späteren Rechtsstreitigkeiten zu Haftungsrisiken führt.
- Rechtsmittelfristen werden beim Abschlussprotokoll nicht dokumentiert, sodass Mandanten Rechtsbehelfsmöglichkeiten versäumen.

## Quellen

- [§ 675 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__675.html)
- [§ 43a BRAO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/brao/__43a.html)
- [§ 50 BRAO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/brao/__50.html)
- [§ 195 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__195.html)
- [dejure.org Anwaltshaftung](https://dejure.org/gesetze/BGB/675.html)

## Abgrenzungen und Methodik

Das Abschlussprotokoll ist von der laufenden Mandatsdokumentation zu unterscheiden: Während Letztere den
laufenden Fortschritt festhält, dokumentiert Ersteres das endgültige Ergebnis, offene Restrisiken und
Folgepflichten. Ohne vollständiges Abschlussprotokoll kann der Anwalt nicht nachweisen, dass er seiner
Aufklärungspflicht vollständig genügt hat, was in Haftungsfällen entscheidend ist.

## Praktische Anwendungshinweise

Das Abschlussschreiben an den Mandanten sollte immer folgende Elemente enthalten: Zusammenfassung des
Ergebnisses in verständlicher Sprache, Hinweis auf alle offenen Fristen, Hinweis auf steuerliche und
registerrechtliche Folgen, Empfehlung für weitere Schritte und die Bitte, etwaige Unstimmigkeiten innerhalb
einer Frist anzuzeigen. Die Aufbewahrungsfrist für die Mandatsakte (Anwaltsrecht: fünf Jahre) ist zu
dokumentieren und einzuhalten. Eine digitale Sicherung der wichtigsten Dokumente schützt vor Aktenverlust.

## Hinweis zur Methodensicherheit

Die methodische Konsistenz der Argumentation ist nicht nur ein akademisches Qualitätsmerkmal, sondern hat
unmittelbare Konsequenzen für die Überzeugungskraft vor Gericht und in der Verhandlung. Inkonsequente
oder widersprüchliche Argumentation wird von gut vorbereiteten Gegenseiten ausgenutzt und kann einen
substanziell starken Fall erheblich schwächen. Die konsequente Anwendung methodischer Prinzipien
schützt die eigene Position und macht sie resilient gegenüber Angriffen.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 20 Abs. 3 GG (Gesetzesbindung)
- Art. 97 GG (richterliche Unabhängigkeit, Gesetzesbindung)
- § 133 BGB (Auslegung Willenserklärung)
- § 157 BGB (Auslegung Verträge)
- § 242 BGB (Treu und Glauben)
- § 305c Abs. 2 BGB (Unklarheitenregel)
- EGBGB Art. 6 (ordre public)
- GG Art. 1, 2 (Verfassungskonforme Auslegung)
- ZPO § 286 (freie Beweiswürdigung)
- GVG § 132 (Vorlage Großer Senat)

### Leitentscheidungen

- BVerfG 1 BvR 730/04 (verfassungskonforme Auslegung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
- BGH GSZ 1/11 (BGH-Methodik)
- BVerfG 2 BvR 883/14 (Wortlautgrenze)
- BGH V ZR 250/02 (teleologische Reduktion)

### Anwendung im Skill

- Auslegungscanon: Wortlaut, Systematik, Historie, Telos; verfassungskonforme Auslegung BVerfG 1 BvR 730/04 als Grenze.
- Analogie nur bei planwidriger Regelungsluecke; teleologische Reduktion BGH V ZR 250/02 als Korrelat.
- Richterrecht BGH GSZ 1/14: Rechtsfortbildung an Art. 20 Abs. 3, Art. 97 GG gebunden.

---

## Skill: `abwaegung-gewichtung-intensitaet`

_Unterstützt die methodisch saubere Gewichtung kollidierender Rechtspositionen nach Intensität, Rang, Normzweck und Eingriffstiefe. Das Skill führt durch die Schritte der Abwägungsjurisprudenz im Zivilrecht und hilft dabei, Schutzwürdigkeit, Verhältnismäßigkeit und praktische Konkordanz nachvollzi..._

# Abwägung: Gewichtung und Intensität kollidierender Rechtspositionen

## Fachlicher Anker

- **Normen:** § 626 BGB, § 903 BGB, § 906 BGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Mandantenfall

- Ein Arbeitgeber kündigt einem langjährigen Arbeitnehmer wegen einer Bagatellverfehlung. Das Gericht muss zwischen Eigentumsfreiheit des Arbeitgebers und sozialem Schutzinteresse des Arbeitnehmers gewichten. Intensität des Eingriffs (Existenzverlust) vs. Normzweck des § 626 BGB.
- Zwei Nachbarn streiten über eine Baumhecke, die Licht entzieht. Zwischen § 903 BGB (Eigentümerfreiheit) und § 906 BGB (Duldungspflicht) steht eine Abwägung nach Ortsüblichkeit und Wesentlichkeit der Beeinträchtigung.
- Ein Verlag veröffentlicht ein Porträt, das persönliche Gesundheitsdaten nennt. Zwischen Pressefreiheit (Art. 5 GG) und allgemeinem Persönlichkeitsrecht (§ 823 Abs. 1 BGB, Art. 2 Abs. 1 GG) ist nach Schwere und Schutzbedarf zu gewichten.

## Erste Schritte

1. Identifiziere die kollidierenden Rechtspositionen präzise: Welche Norm, welches Rechtsgut, welcher Rechtsträger steht auf jeder Seite?
2. Bestimme den Rang jeder Position: Verfassungsrang, einfaches Recht, Vertrag, bloßes Interesse?
3. Messe die Eingriffsintensität: Ist die Beeinträchtigung nur marginal, erheblich oder existenziell?
4. Prüfe den Normzweck der einschlägigen Regelung: Schützt die Norm primär eine der kollidierenden Positionen oder enthält sie selbst eine Abwägungsentscheidung des Gesetzgebers?
5. Wende das Verhältnismäßigkeitsprinzip dreistufig an: Geeignetheit, Erforderlichkeit, Angemessenheit des Eingriffs.
6. Dokumentiere das Ergebnis der praktischen Konkordanz: Welches Gewicht bekommt welche Position, und warum ist das die schonendste Lösung?

## Rechtsrahmen

- § 242 BGB — Treu und Glauben als Einfallstor für Verhältnismäßigkeitsgedanken im Zivilrecht
- § 906 BGB — gesetzlich typisierte Abwägungsentscheidung bei Immissionen als Muster strukturierter Interessenabwägung
- Art. 1 Abs. 3 GG — Grundrechtsbindung auch im Privatrecht durch mittelbare Drittwirkung
- Art. 2 Abs. 1 GG — allgemeines Persönlichkeitsrecht als gewichtungsrelevante Verfassungsposition
- Art. 14 GG — Eigentumsfreiheit als gegenläufige Schutzposition mit Sozialbindung nach Abs. 2
- § 826 BGB — sittenwidrige Schädigung als Auffangnorm nach intensiver Abwägung von Schutzbedarf und Handlungsfreiheit

## Prüfraster

1. Sind alle kollidierenden Positionen vollständig erfasst und namentlich benannt?
2. Wurde der normative Rang jeder Position (Verfassung, Gesetz, Vertrag) korrekt bestimmt?
3. Ist die Intensitätsmessung nachvollziehbar und an Tatsachen rückgebunden?
4. Hat der Gesetzgeber eine Vorrangentscheidung getroffen, die vorrangig zu respektieren ist?
5. Wurde die Verhältnismäßigkeitsprüfung dreistufig und vollständig durchgeführt?
6. Ist das Ergebnis der praktischen Konkordanz das schonendste verfügbare Mittel?
7. Ist die Abwägung frei von versteckten Ergebnisvorgaben und offen begründet?

## Typische Fallstricke

- Gewichtung wird intuitiv vorgenommen, ohne die kollidierenden Positionen explizit zu benennen — die Abwägung bleibt angreifbar.
- Normzweck wird ignoriert: Enthält die Norm selbst bereits eine legislative Abwägungsentscheidung, ist gerichtliche Eigengewichtung unzulässig.
- Intensitätsunterschiede werden nivelliert: Existenzielle Eingriffe auf einer Seite müssen stärkeres Gewicht erhalten als Bagatellinteressen auf der anderen.
- Verhältnismäßigkeit wird auf Angemessenheit verkürzt — Geeignetheit und Erforderlichkeit werden übersprungen.
- Praktische Konkordanz wird als bloßes Kompromissgebot missverstanden; sie verlangt optimale Entfaltung beider Positionen, nicht arithmetische Mitte.

## Vertiefung: Intensitätsstufen in der Rechtsprechung

Das BVerfG unterscheidet in ständiger Rechtsprechung zwischen leichten, mittleren und schweren Grundrechtseingriffen. Diese Trias ist auf zivilrechtliche Abwägungen übertragbar: Eingriffe in die Sozialsphäre des Persönlichkeitsrechts sind weniger gewichtig als Eingriffe in die Intimsphäre. Dieses Stufenmodell macht Abwägungsentscheidungen revisionsrechtlich überprüfbar.

## Hinweise zur Praxis

Bei der Formulierung von Schriftsätzen empfiehlt sich eine tabellarische Darstellung der kollidierenden Positionen mit ihren jeweiligen Schutzgütern, Eingriffsintensitäten und normativen Rängen. Gerichte schätzen strukturierte Abwägungsdarstellungen, weil sie die Urteilsbegründung erleichtern. Verweisen Sie stets auf die normspezifische Abwägungsvorgabe des Gesetzgebers, bevor Sie eigene Gewichtungen einführen.

## Weiterführende Analyse

Die Intensitätsstufen lassen sich in der Praxis anhand von drei Leitfragen operationalisieren: Wie dauerhaft ist die Beeinträchtigung? Wie reversibel sind die Folgen? Wie zentral ist das beeinträchtigte Rechtsgut für die Persönlichkeit oder das Vermögen? Je höher die Antworten auf diese Fragen, desto intensiver der Eingriff und desto strengere Anforderungen an die Rechtfertigungslage auf der Gegenseite. Diese dreistufige Intensitätskarte macht das Abwägungsergebnis rational begründbar und angreifbar.

## Checkliste zur Selbstprüfung

Vor Abgabe des fertigen Dokuments sollten folgende Punkte kurz geprüft werden: Sind alle Auslegungsmethoden zumindest erwähnt? Ist die Methodenwahl explizit begründet? Sind alle Behauptungen normativ oder empirisch rückgebunden? Ist das Ergebnis konsistent mit vergleichbaren Entscheidungen? Ist die institutionelle Zuständigkeit für die getroffene Entscheidung gewahrt? Wurde die Gegenposition ernsthaft berücksichtigt? Sind alle verwendeten Quellen korrekt angegeben?

## Quellen

- [§ 242 BGB – Treu und Glauben](https://www.gesetze-im-internet.de/bgb/__242.html)
- [§ 906 BGB – Zuführung unwägbarer Stoffe](https://www.gesetze-im-internet.de/bgb/__906.html)
- [Art. 14 GG bei dejure](https://dejure.org/gesetze/GG/14.html)
- [BVerfGE 7, 198 – Lüth-Urteil zur mittelbaren Drittwirkung](https://www.bverfg.de/e/rs19580115_1bvr040051.html)
- [§ 826 BGB bei dejure](https://dejure.org/gesetze/BGB/826.html)

> Dieses Skill ist Teil des Methodenlehre-Curriculums im Bürgerlichen Recht und steht im Kontext des Rechtsstaats- und Demokratieprinzips des Grundgesetzes.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 20 Abs. 3 GG (Gesetzesbindung)
- Art. 97 GG (richterliche Unabhängigkeit, Gesetzesbindung)
- § 133 BGB (Auslegung Willenserklärung)
- § 157 BGB (Auslegung Verträge)
- § 242 BGB (Treu und Glauben)
- § 305c Abs. 2 BGB (Unklarheitenregel)
- EGBGB Art. 6 (ordre public)
- GG Art. 1, 2 (Verfassungskonforme Auslegung)
- ZPO § 286 (freie Beweiswürdigung)
- GVG § 132 (Vorlage Großer Senat)

### Leitentscheidungen

- BVerfG 1 BvR 730/04 (verfassungskonforme Auslegung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
- BGH GSZ 1/11 (BGH-Methodik)
- BVerfG 2 BvR 883/14 (Wortlautgrenze)
- BGH V ZR 250/02 (teleologische Reduktion)

### Anwendung im Skill

- Auslegungscanon: Wortlaut, Systematik, Historie, Telos; verfassungskonforme Auslegung BVerfG 1 BvR 730/04 als Grenze.
- Analogie nur bei planwidriger Regelungsluecke; teleologische Reduktion BGH V ZR 250/02 als Korrelat.
- Richterrecht BGH GSZ 1/14: Rechtsfortbildung an Art. 20 Abs. 3, Art. 97 GG gebunden.

---

## Skill: `abwaegung-material-auswahl`

_Leitet durch die methodisch begründete Auswahl von Abwägungsmaterial im Zivilrecht. Das Skill zeigt, welche Fakten, Normen, Präjudizien und Wertungsgesichtspunkte in eine Abwägungsentscheidung einbezogen werden dürfen und welche ausgeblendet werden müssen. Es schützt vor willkürlicher Materialaus..._

# Abwägung: Materialauswahl und Abwägungsgrundlagen

## Fachlicher Anker

- **Normen:** § 307 BGB, § 253 BGB, § 133 BGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Mandantenfall

- Ein Gericht stützt eine Abwägungsentscheidung auf Pressemitteilungen und öffentliche Meinung statt auf Normzweck und Tatsachenbefund. Der Anwalt muss die Materialauswahl methodisch angreifen und zeigen, dass nicht-rechtliches Material unzulässig eingeflossen ist.
- Im Vertragsrecht soll ermittelt werden, ob eine AGB-Klausel nach § 307 BGB unangemessen benachteiligt. Das Gericht muss entscheiden, welche Marktdaten, Branchenpraktiken und Schutzzweckerwägungen zulässigerweise einbezogen werden.
- Ein Richter erwägt bei der Schadensbemessung nach § 253 BGB Schmerzensgeld: Er wählt zwischen vergleichbaren Präjudizien, statistischen Schmerzensgeldtabellen und individuellen Leidensnachweisen — die Methode der Materialauswahl ist entscheidend.

## Erste Schritte

1. Bestimme den Abwägungsrahmen: Welche Norm enthält die Abwägungsöffnung und welche Materialien erlaubt ihr Wortlaut und Zweck?
2. Trenne zulässiges von unzulässigem Abwägungsmaterial: Nur rechtlich relevante Tatsachen, Normzweckerwägungen und gesicherte Präjudizien sind zulässig.
3. Prüfe die Verlässlichkeit der Tatsachengrundlage: Sind Fakten durch Beweismittel gesichert oder nur behauptet?
4. Identifiziere etwaige gesetzgeberische Vorgewichtungen durch Regelbeispiele, Legaldefinitionen oder parlamentarische Materialien.
5. Ordne das Material nach Gewichtsklassen: normative Vorgaben haben Vorrang vor Analogien, diese vor bloßen Interessenerwägungen.
6. Dokumentiere ausgeschlossenes Material und begründe den Ausschluss — das schützt vor dem Vorwurf der willkürlichen Selektion.

## Rechtsrahmen

- § 307 BGB — Generalklausel für unangemessene Benachteiligung, erfordert normzweckorientierte Materialauswahl
- § 133 BGB — Auslegung nach wirklichem Willen als Schranke für Materialauswahl bei Vertragsinterpretation
- § 253 BGB — Schmerzensgeld: Präjudizien und individuelle Verhältnisse als zulässiges Material
- Art. 3 Abs. 1 GG — Gleichheitssatz als Maßstab für Konsistenz der Materialauswahl zwischen vergleichbaren Fällen
- § 286 ZPO — freie richterliche Überzeugungsbildung als verfahrensrechtlicher Rahmen für Tatsachenmaterial
- Art. 20 Abs. 3 GG — Gesetzesbindung als Grenze für die Einbeziehung nicht-normativen Materials

## Prüfraster

1. Ist der Abwägungsrahmen der maßgeblichen Norm vollständig erfasst?
2. Ist das einbezogene Material normzweckkonform und rechtlich erheblich?
3. Sind Tatsachenbehauptungen von gesicherten Befunden getrennt?
4. Hat der Gesetzgeber durch Regelbeispiele oder Materialien eine Vorauswahl getroffen?
5. Ist die Auswahl vergleichbar konsistent mit parallelen Entscheidungen (Gleichheitsprüfung)?
6. Wurde unzulässiges Material (Meinungen, Stimmungsbilder, politische Wertungen) explizit ausgeblendet?
7. Ist die Materialauswahl schriftlich begründet und damit überprüfbar?
8. Wurden Gegen-Materialien ernsthaft erwogen und ihrerseits begründet ausgeschlossen?

## Typische Fallstricke

- Selektive Materialauswahl zugunsten des gewünschten Ergebnisses, ohne Auseinandersetzung mit konträren Materialien.
- Verwechslung von Tatsachen und Wertungen: Gesellschaftliche Stimmungsbilder sind kein rechtliches Abwägungsmaterial.
- Übergewichtung von Einzelpräjudizien, obwohl die Gesamtrechtsprechung ein anderes Bild ergibt.
- Nichtbeachtung legislativer Vorgewichtungen durch Regelbeispiele in Normen wie § 307 Abs. 2 BGB.
- Fehlende Transparenz über ausgeschlossenes Material — der Eindruck der Willkür entsteht.

## Vertiefung: Hierarchie des Abwägungsmaterials

Abwägungsmaterial ist nicht gleichrangig. Normative Vorgaben des Gesetzgebers stehen an erster Stelle, gefolgt von gesicherten Präjudizien, anerkannten Rechtsprinzipien und zuletzt bloßen Interessenerwägungen. Diese Hierarchie ist in der Rechtsanwendung konsequent einzuhalten und transparent zu kommunizieren, damit Abwägungsentscheidungen nicht als beliebig erscheinen.

## Hinweise zur Praxis

Bei strittiger Materialauswahl empfiehlt sich ein Abwägungsprotokoll, das alle erwogenen Materialien listet und die Ausschlüsse begründet. Dies schützt vor späteren Vorwürfen selektiver Argumentation und erleichtert das Nachvollziehen der Entscheidung. In Revisionssachen kann fehlerhafte Materialauswahl als Rechtsfehler gerügt werden, wenn sie das Ergebnis beeinflusst hat.

## Weiterführende Analyse

Bei komplexen Abwägungsentscheidungen empfiehlt sich eine Materialmatrix: Zuerst werden alle potenziell relevanten Materialien gesammelt (Normen, Präjudizien, Empirie, Rechtslehre), dann nach Zulässigkeit gefiltert, schließlich nach Gewichtsklassen geordnet. Diese Matrix macht die Auswahl transparent und angreifbar. Besonders hilfreich ist die explizite Spalte für ausgeschlossenes Material mit Ausschlussbegründung — sie schützt vor dem Vorwurf der Willkür besser als jedes inhaltliche Argument.

## Checkliste zur Selbstprüfung

Vor Abgabe des fertigen Dokuments sollten folgende Punkte kurz geprüft werden: Sind alle Auslegungsmethoden zumindest erwähnt? Ist die Methodenwahl explizit begründet? Sind alle Behauptungen normativ oder empirisch rückgebunden? Ist das Ergebnis konsistent mit vergleichbaren Entscheidungen? Ist die institutionelle Zuständigkeit für die getroffene Entscheidung gewahrt? Wurde die Gegenposition ernsthaft berücksichtigt? Sind alle verwendeten Quellen korrekt angegeben?

## Quellen

- [§ 307 BGB – Inhaltskontrolle](https://www.gesetze-im-internet.de/bgb/__307.html)
- [§ 133 BGB – Auslegung von Willenserklärungen](https://www.gesetze-im-internet.de/bgb/__133.html)
- [§ 253 BGB – Immaterieller Schaden](https://www.gesetze-im-internet.de/bgb/__253.html)
- [Art. 3 GG bei dejure](https://dejure.org/gesetze/GG/3.html)
- [§ 286 ZPO bei dejure](https://dejure.org/gesetze/ZPO/286.html)

> Dieses Skill ist Teil des Methodenlehre-Curriculums im Bürgerlichen Recht und steht im Kontext des Rechtsstaats- und Demokratieprinzips des Grundgesetzes.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 20 Abs. 3 GG (Gesetzesbindung)
- Art. 97 GG (richterliche Unabhängigkeit, Gesetzesbindung)
- § 133 BGB (Auslegung Willenserklärung)
- § 157 BGB (Auslegung Verträge)
- § 242 BGB (Treu und Glauben)
- § 305c Abs. 2 BGB (Unklarheitenregel)
- EGBGB Art. 6 (ordre public)
- GG Art. 1, 2 (Verfassungskonforme Auslegung)
- ZPO § 286 (freie Beweiswürdigung)
- GVG § 132 (Vorlage Großer Senat)

### Leitentscheidungen

- BVerfG 1 BvR 730/04 (verfassungskonforme Auslegung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
- BGH GSZ 1/11 (BGH-Methodik)
- BVerfG 2 BvR 883/14 (Wortlautgrenze)
- BGH V ZR 250/02 (teleologische Reduktion)

### Anwendung im Skill

- Auslegungscanon: Wortlaut, Systematik, Historie, Telos; verfassungskonforme Auslegung BVerfG 1 BvR 730/04 als Grenze.
- Analogie nur bei planwidriger Regelungsluecke; teleologische Reduktion BGH V ZR 250/02 als Korrelat.
- Richterrecht BGH GSZ 1/14: Rechtsfortbildung an Art. 20 Abs. 3, Art. 97 GG gebunden.

---

## Skill: `abwaegungslast-non-liquet`

_Behandelt die methodische Frage, wie mit Abwägungslagen umzugehen ist, in denen das Material keine eindeutige Entscheidung erlaubt. Das Skill systematisiert die Non-liquet-Problematik im Zivilrecht und zeigt, welche Entscheidungsregeln bei Abwägungsunklarheit greifen — Beweislastverteilung, Regel..._

# Abwägungslast und Non-liquet: Entscheiden bei unsicherer Abwägungsgrundlage

## Fachlicher Anker

- **Normen:** § 830 BGB, § 138 BGB, § 363 BGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Mandantenfall

- Im Arzthaftungsprozess steht fest, dass ein Fehler vorlag, aber unklar bleibt, ob er kausal für den Schaden war. Die Abwägungslage bezüglich der Kausalität ist non-liquet. Es stellt sich die Frage, ob § 830 BGB, Beweislasterleichterungen oder der Anscheinsbeweis greifen.
- Bei der Sittenwidrigkeitsprüfung nach § 138 BGB liegen Indizien vor, die für und gegen eine Übervorteilung sprechen. Das Gericht muss entscheiden, welche Seite die Last trägt, die Abwägungsunklarheit aufzulösen.
- Ein Arbeitgeber kündigt und behauptet verhaltensbedingten Grund; der Arbeitnehmer bestreitet jede Pflichtverletzung substantiiert. Beide Sachverhaltsversionen sind gleich plausibel. Wer trägt bei diesem Abwägungspatt die Darlegungs- und Beweislast?

## Erste Schritte

1. Stelle fest, ob ein echtes Non-liquet vorliegt oder ob die Unsicherheit durch weitere Sachaufklärung auflösbar ist.
2. Prüfe, ob die einschlägige Norm eine Beweislastverteilung enthält oder ob allgemeine Grundsätze greifen (actori incumbit probatio, § 363 BGB, § 280 BGB).
3. Untersuche, ob Regelfallannahmen oder gesetzliche Vermutungen die Abwägungslücke schließen.
4. Erwäge Beweislasterleichterungen: Anscheinsbeweis, Beweismaßreduzierung nach § 287 ZPO, Umkehr der Beweislast bei Gefahrenbereichs- oder Produkthaftungslagen.
5. Prüfe, ob die institutionelle Zuständigkeit verlangt, bei echter Abwägungsunklarheit zugunsten des Gesetzgebers zurückzuweisen (Vorlage, Verfassungsbeschwerde).
6. Dokumentiere das Non-liquet offen: Methodische Ehrlichkeit verlangt, Unklarheiten nicht durch Scheinsicherheit zu überdecken.

## Rechtsrahmen

- § 363 BGB — Beweislastverteilung bei Erfüllungseinrede als Beispiel gesetzlicher Lösung des Non-liquet
- § 280 Abs. 1 Satz 2 BGB — Verschuldensvermutung als gesetzliche Non-liquet-Auflösung im Schuldverhältnis
- § 287 ZPO — richterliches Ermessen bei Schadensschätzung und Beweismaßreduzierung
- § 138 BGB — Sittenwidrigkeit als Wertungsbegriff, der Abwägungsunsicherheit trägt, ohne sie zu eliminieren
- Art. 100 GG — Vorlagepflicht als institutionelle Konsequenz bei nicht auflösbarer Verfassungsabwägung
- Art. 20 Abs. 3 GG — Gesetzesbindung als Maßstab: Non-liquet-Fälle müssen an den Gesetzgeber zurückgegeben werden, wenn keine normative Lösung erkennbar ist

## Prüfraster

1. Liegt ein echtes Non-liquet vor oder ist die Unklarheit tatsächlicher Natur und durch Beweisaufnahme auflösbar?
2. Enthält die einschlägige Norm eine explizite Beweislast- oder Entscheidungsregel?
3. Greifen gesetzliche Vermutungen oder Regelfallannahmen?
4. Ist eine Beweislasterleichterung durch Anscheinsbeweis oder Sphärentheorie begründbar?
5. Hat das Gericht seine Überzeugungsbildung nach § 286 ZPO vollständig ausgeschöpft?
6. Ist eine Richtervorlage wegen nicht auflösbarer Verfassungsfrage geboten?
7. Wird das Non-liquet im Ergebnis transparent gemacht oder durch Scheinbegründungen verdeckt?
8. Entspricht die Restunsicherheitsverteilung dem Normzweck der einschlägigen Regelung?

## Typische Fallstricke

- Non-liquet-Situationen werden durch voreilige Überzeugungsbildung verdeckt statt offen ausgewiesen.
- Beweislastverteilung wird nicht normativ hergeleitet, sondern intuitiv zugeteilt.
- § 287 ZPO wird als Freifahrtschein für beliebige Schadensschätzung ohne methodische Grundlage missverstanden.
- Gesetzliche Vermutungen werden übersehen oder rechtswidrig umgekehrt.
- Die institutionelle Konsequenz eines echten Abwägungspatts — Vorlage oder Zurückhaltung — wird nicht erwogen.

## Vertiefung: Beweislastverteilung als Systemfrage

Die Verteilung der Beweislast im deutschen Zivilrecht folgt dem Grundsatz, dass jede Partei die Voraussetzungen der ihr günstigen Norm darlegen und beweisen muss. Bei Non-liquet-Situationen ist daher zuerst die Frage zu stellen: Welche Partei trägt die Last der Abwägungsunklarheit? Die Antwort ergibt sich aus dem Normzweck und dem Schutzbedürfnis der Parteien.

## Hinweise zur Praxis

Non-liquet-Situationen sind im Schriftsatz offen auszuweisen und nicht durch Scheingewissheiten zu überdecken. Gerichte schätzen Ehrlichkeit über Abwägungsunklarheiten und begründen ihre Entscheidungen tragfähiger, wenn die Parteien die Unsicherheiten klar benennen. Beweislastargumente sollten stets normativ hergeleitet und nicht nur behauptet werden.

## Weiterführende Analyse

In der Praxis bewährt sich für Non-liquet-Situationen das Drei-Stufen-Modell: Stufe 1 — Kann die Unsicherheit durch weitere Sachaufklärung aufgelöst werden? Stufe 2 — Enthält die anwendbare Norm eine Verteilungsregel für die Restunsicherheit (Beweislast, Vermutung, Fiktion)? Stufe 3 — Ist die institutionelle Konsequenz (Vorlage, Zurückverweisung, Gesetzgeberhinweis) zu ziehen? Erst wenn alle drei Stufen erschöpft sind, ist ein echtes Non-liquet ausgewiesen.

## Checkliste zur Selbstprüfung

Vor Abgabe des fertigen Dokuments sollten folgende Punkte kurz geprüft werden: Sind alle Auslegungsmethoden zumindest erwähnt? Ist die Methodenwahl explizit begründet? Sind alle Behauptungen normativ oder empirisch rückgebunden? Ist das Ergebnis konsistent mit vergleichbaren Entscheidungen? Ist die institutionelle Zuständigkeit für die getroffene Entscheidung gewahrt? Wurde die Gegenposition ernsthaft berücksichtigt? Sind alle verwendeten Quellen korrekt angegeben?

## Quellen

- [§ 280 BGB bei dejure](https://dejure.org/gesetze/BGB/280.html)
- [§ 287 ZPO – Schadensermittlung](https://www.gesetze-im-internet.de/zpo/__287.html)
- [§ 363 BGB bei dejure](https://dejure.org/gesetze/BGB/363.html)
- [Art. 100 GG – Vorlagepflicht](https://dejure.org/gesetze/GG/100.html)
- [§ 138 BGB – Sittenwidrigkeit](https://www.gesetze-im-internet.de/bgb/__138.html)

> Dieses Skill ist Teil des Methodenlehre-Curriculums im Bürgerlichen Recht und steht im Kontext des Rechtsstaats- und Demokratieprinzips des Grundgesetzes.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 20 Abs. 3 GG (Gesetzesbindung)
- Art. 97 GG (richterliche Unabhängigkeit, Gesetzesbindung)
- § 133 BGB (Auslegung Willenserklärung)
- § 157 BGB (Auslegung Verträge)
- § 242 BGB (Treu und Glauben)
- § 305c Abs. 2 BGB (Unklarheitenregel)
- EGBGB Art. 6 (ordre public)
- GG Art. 1, 2 (Verfassungskonforme Auslegung)
- ZPO § 286 (freie Beweiswürdigung)
- GVG § 132 (Vorlage Großer Senat)

### Leitentscheidungen

- BVerfG 1 BvR 730/04 (verfassungskonforme Auslegung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
- BGH GSZ 1/11 (BGH-Methodik)
- BVerfG 2 BvR 883/14 (Wortlautgrenze)
- BGH V ZR 250/02 (teleologische Reduktion)

### Anwendung im Skill

- Auslegungscanon: Wortlaut, Systematik, Historie, Telos; verfassungskonforme Auslegung BVerfG 1 BvR 730/04 als Grenze.
- Analogie nur bei planwidriger Regelungsluecke; teleologische Reduktion BGH V ZR 250/02 als Korrelat.
- Richterrecht BGH GSZ 1/14: Rechtsfortbildung an Art. 20 Abs. 3, Art. 97 GG gebunden.

---

## Skill: `abwaegungszustaendigkeit-institutionen`

_Klärt, welche Institution im Rechtssystem für eine konkrete Abwägungsentscheidung zuständig ist — Gesetzgeber, Gericht, Behörde oder Schiedsgericht. Das Skill verhindert Kompetenzkonfusionen und stärkt die demokratische Legitimation richterlicher Abwägung. Es analysiert Abwägungsöffnungen in Norm..._

# Abwägungszuständigkeit: Welche Institution darf abwägen?

## Fachlicher Anker

- **Normen:** Art. 20 Abs. 3 GG, Art. 97 GG, § 1.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Mandantenfall

- Ein Gericht möchte die Miethöhe in einer Großstadt durch Abwägung der sozialpolitischen Folgen regulieren, obwohl der Gesetzgeber im Mietrecht bereits eine abschließende Interessenabwägung vorgenommen hat. Die Frage ist, ob die richterliche Abwägung die gesetzgeberische ersetzen darf.
- Im Kartellrecht will ein Schiedsgericht eine Marktmachtabwägung vornehmen, die eigentlich dem Bundeskartellamt zugewiesen ist. Das Skill klärt, ob und in welchem Umfang das Schiedsgericht die Behördenabwägung substituieren kann.
- Ein Verwaltungsgericht überprüft die behördliche Abwägung beim Erlass einer Baugenehmigung: Wie weit reicht die Kontrolldichte, und ab wann überschreitet das Gericht seine Prüfungskompetenz?

## Erste Schritte

1. Identifiziere die abwägungsöffnende Norm und prüfe, ob sie die Abwägung an eine bestimmte Institution delegiert oder dem Rechtsanwender allgemein überlässt.
2. Bestimme die institutionelle Stellung des handelnden Akteurs: Gesetzgeber, Verwaltung, ordentliches Gericht, Fachgericht, Schiedsgericht.
3. Prüfe, ob der Gesetzgeber eine abschließende Abwägungsentscheidung getroffen hat — dann ist für richterliche Eigenabwägung kein Raum.
4. Ermittle den Kontrollmaßstab: Volldurchprüfung, Vertretbarkeitskontrolle oder Missbrauchs- bzw. Willkürkontrolle?
5. Untersuche die Rückbindungspflicht: Erfordert die Abwägung demokratische Legitimation, die nur der Gesetzgeber oder eine demokratisch rechenschaftspflichtige Behörde liefern kann?
6. Formuliere das Ergebnis institutionell klar: Die Abwägung liegt bei Institution X, weil Norm Y dies anordnet bzw. Art. 20 Abs. 3 GG es gebietet.

## Rechtsrahmen

- Art. 20 Abs. 3 GG — Bindung der vollziehenden Gewalt und Rechtsprechung an Gesetz und Recht als institutionelle Grenzziehung
- Art. 97 GG — richterliche Unabhängigkeit im Rahmen des Gesetzes, keine Unabhängigkeit vom Gesetz
- § 1 GWB — Kartellverbot mit institutioneller Zuständigkeit der Kartellbehörde für Abwägungen
- § 307 BGB — Inhaltskontrolle als richterliche Abwägungsaufgabe, aber begrenzt durch gesetzgeberisch vorgeformte Wertungen
- § 315 BGB — Leistungsbestimmungsrecht: Abwägung primär durch Partei, sekundär durch Gericht auf Billigkeit
- Art. 100 Abs. 1 GG — Vorlagepflicht als institutionelle Konsequenz, wenn Gericht abwägend von Gesetzeswortlaut abweichen will

## Prüfraster

1. Enthält die einschlägige Norm eine Zuweisung der Abwägungskompetenz?
2. Hat der Gesetzgeber bereits eine abschließende Interessenabwägung vorgenommen?
3. Welche Kontrolldichte ist für die handelnde Institution gegenüber der abwägenden Institution angemessen?
4. Verfügt das handelnde Organ über die demokratische Legitimation für die konkrete Abwägungsentscheidung?
5. Wird durch die Abwägung eine normsetzende Entscheidung getroffen, die dem Gesetzgeber vorbehalten ist?
6. Ist die institutionelle Zuständigkeit im Ergebnis klar kommuniziert?
7. Wurden Ausweichentscheidungen (z.B. Vorlage, Zurückverweisung) geprüft?

## Typische Fallstricke

- Gerichte übernehmen Abwägungsaufgaben, die kraft Normstruktur oder Demokratieprinzip beim Gesetzgeber liegen.
- Behördliches Ermessen wird richterlich vollständig ersetzt statt nur auf Vertretbarkeit kontrolliert.
- Die Abwägungsöffnung einer Norm wird als unbegrenzte richterliche Eigenständigkeit missverstanden.
- Fehlen der demokratischen Rückbindung bei weitreichenden Abwägungsentscheidungen wird nicht thematisiert.
- Die Vorlagepflicht nach Art. 100 GG wird übersehen, wenn Abwägungsergebnisse gegen förmliches Gesetz verstoßen.

## Vertiefung: Ermessen und Kontrolldichte im Mehrebenensystem

Im Mehrebenensystem des deutschen Rechts besteht eine Hierarchie der Abwägungszuständigkeiten: Unionsrecht hat Anwendungsvorrang, Bundesrecht bricht Landesrecht, und innerhalb jeder Ebene gelten klare institutionelle Zuweisungen. Bei grenzüberschreitenden Sachverhalten muss die Abwägungszuständigkeit daher auf jeder Ebene gesondert bestimmt werden.

## Hinweise zur Praxis

Die institutionelle Kompetenzfrage ist im Schriftsatz oder Gutachten stets als Vorfrage zu behandeln, bevor inhaltlich abgewogen wird. Fehlerhafte institutionelle Zuständigkeit führt zur Aufhebbarkeit der Entscheidung unabhängig vom Sachinhalt. Besondere Aufmerksamkeit gilt dem Verhältnis von behördlichem Ermessen und richterlicher Kontrolle.

## Weiterführende Analyse

Die Frage der institutionellen Zuständigkeit für Abwägungsentscheidungen gewinnt im föderalen Mehrebenensystem besondere Schärfe: Neben Bund und Ländern spielen auch europäische Institutionen eine Rolle. Der Anwalt muss stets prüfen, ob die abwägende Institution die Kompetenz auch im Mehrebenensystem hat. Dies gilt besonders im Bereich der grundrechtsgebundenen Abwägungen, wo Art. 51 GRCh die Anwendung der Grundrechtecharta begrenzt.

## Checkliste zur Selbstprüfung

Vor Abgabe des fertigen Dokuments sollten folgende Punkte kurz geprüft werden: Sind alle Auslegungsmethoden zumindest erwähnt? Ist die Methodenwahl explizit begründet? Sind alle Behauptungen normativ oder empirisch rückgebunden? Ist das Ergebnis konsistent mit vergleichbaren Entscheidungen? Ist die institutionelle Zuständigkeit für die getroffene Entscheidung gewahrt? Wurde die Gegenposition ernsthaft berücksichtigt? Sind alle verwendeten Quellen korrekt angegeben?

## Quellen

- [Art. 20 GG bei dejure](https://dejure.org/gesetze/GG/20.html)
- [Art. 97 GG – Richterliche Unabhängigkeit](https://dejure.org/gesetze/GG/97.html)
- [§ 315 BGB – Bestimmung der Leistung](https://www.gesetze-im-internet.de/bgb/__315.html)
- [Art. 100 GG – Vorlagepflicht](https://dejure.org/gesetze/GG/100.html)
- [§ 307 BGB bei dejure](https://dejure.org/gesetze/BGB/307.html)
- [BVerfGE 34, 269 – Soraya, zu richterlicher Rechtsfortbildung](https://www.bverfg.de/e/rs19730214_1bvr111268.html)

> Dieses Skill ist Teil des Methodenlehre-Curriculums im Bürgerlichen Recht und steht im Kontext des Rechtsstaats- und Demokratieprinzips des Grundgesetzes.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 20 Abs. 3 GG (Gesetzesbindung)
- Art. 97 GG (richterliche Unabhängigkeit, Gesetzesbindung)
- § 133 BGB (Auslegung Willenserklärung)
- § 157 BGB (Auslegung Verträge)
- § 242 BGB (Treu und Glauben)
- § 305c Abs. 2 BGB (Unklarheitenregel)
- EGBGB Art. 6 (ordre public)
- GG Art. 1, 2 (Verfassungskonforme Auslegung)
- ZPO § 286 (freie Beweiswürdigung)
- GVG § 132 (Vorlage Großer Senat)

### Leitentscheidungen

- BVerfG 1 BvR 730/04 (verfassungskonforme Auslegung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
- BGH GSZ 1/11 (BGH-Methodik)
- BVerfG 2 BvR 883/14 (Wortlautgrenze)
- BGH V ZR 250/02 (teleologische Reduktion)

### Anwendung im Skill

- Auslegungscanon: Wortlaut, Systematik, Historie, Telos; verfassungskonforme Auslegung BVerfG 1 BvR 730/04 als Grenze.
- Analogie nur bei planwidriger Regelungsluecke; teleologische Reduktion BGH V ZR 250/02 als Korrelat.
- Richterrecht BGH GSZ 1/14: Rechtsfortbildung an Art. 20 Abs. 3, Art. 97 GG gebunden.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

