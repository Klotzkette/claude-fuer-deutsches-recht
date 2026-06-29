---
name: kaltstart-interview
description: "Produktrecht-Plugin erstmalig einrichten und Launch-Tracker verbinden sowie Risikokalibrierung der Rechtsabteilung erfassen. Verbindet Launch-Tracker liest vergangene Reviews lernt Risikokalibrierung. Normen ProdSG MarktueberwG CE-Kennzeichnungs-Pflichten EU-Produktsicherheits-VO 2023/988. Prüfra..."
---

# /kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

## `--check-integrations`

Führt die Integrations-Verfügbarkeitsprüfung erneut durch (Launch-Tracker, Dokumentenspeicher, Slack) und aktualisiert `## Verfügbare Integrationen` in der Konfiguration. Führt kein neues Interview durch. Verwenden wenn ein MCP verbunden oder getrennt wurde.

Beim Prüfen: nur `✓` melden wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren mit einer einzeiligen Anleitung zur Bestätigung. Niemals `✓` auf Basis von `.mcp.json`-Deklarationen allein melden.

---

### Kaltstart-Interview: Produktrecht

## Kaltstart-Prüfung

`~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` lesen:
- **Existiert nicht** → Interview starten.
- **Enthält `<!-- SETUP PAUSED AT: -->`** → Nutzer begrüßen und Fortsetzung von diesem Abschnitt anbieten.
- **Enthält `[PLATZHALTER]`-Marker aber keinen Pause-Kommentar** → Vorlage wurde nie ausgefüllt; Neustart oder Fortsetzung ab erstem Platzhalter anbieten.
- **Ausgefüllt (keine Platzhalter, kein Pause-Kommentar)** → bereits konfiguriert; überspringen außer `--redo`.

## Gemeinsames Unternehmensprofil prüfen

Nach `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` suchen.

- **Wenn vorhanden:** Lesen. Einzeilige Bestätigung zeigen: "Sie sind [Name], [Praxissetting], bei [Unternehmen], [Branche], tätig in [Jurisdiktionen]. Stimmt das? (Oder sagen Sie 'aktualisieren' um das gemeinsame Profil zu ändern.)" Wenn bestätigt, Unternehmensfragen überspringen – direkt zu plugin-spezifischen Fragen.
- **Wenn nicht vorhanden:** Dieses Plugin ist das erste das der Nutzer einrichtet. Nach Orientierung und Verzweigung die Unternehmensfragen stellen und das gemeinsame Profil schreiben.

## Installationsumfang-Prüfung

Vor der Orientierung, wenn das Arbeitsverzeichnis innerhalb eines Projekts (nicht dem Home-Verzeichnis) liegt, einmal darauf hinweisen:

> **Hinweis – dieses Plugin scheint projektbegrenzt zu sein, was bedeutet ich kann nur Dateien in [aktuelles Verzeichnis] lesen. Wenn Sie Dokumente von anderen Speicherorten möchten (Downloads, Dokumente, Dropbox), installieren Sie nutzerbegrenzt – vgl. QUICKSTART.md.**

Bestätigung des Nutzers abfragen: mit Projektumfang fortfahren oder pausieren um nutzerbegrenzt neu zu installieren.

## Vor dem Interview

Vor sonstigen Fragen eine kurze Vorab-Präambel zeigen – 3–4 kurze Zeilen:

> **`produktrecht` ist für Personen die Produktlaunches, Werbeaussagen und Feature-Risiken prüfen – die rechtliche Seite des Shippens.** Nicht Ihr Bereich? `/kanzlei-builder-hub:verwandte-skills-vorschlag`.
>
> **2 Minuten** ergibt Ihre Rolle, Ihr Review-Framework-Level (formales Gate vs. beratend) und Produkt-/Praxiskontext (Verbraucher, Unternehmen, beide), mit vernünftigen Standardwerten überall. **15 Minuten** fügt Ihre Risikokalibrierungstabelle (was hier blockiert vs. was shippt), Ihre Eskalationsmatrix, Ihre Review-Framework-Kategorien, Ihr Memo-Format und Ihre Launch-Tracker-Integration hinzu.
>
> Schnell oder vollständig? (Jederzeit aufrüsten mit `/kaltstart-interview --full`.)

Auf die Wahl des Nutzers warten bevor etwas anderes gezeigt wird.

## Nach der Wahl

Sobald der Nutzer gewählt hat, orientieren:

> "Dieses Plugin pflegt Ihr Praxisprofil (Review-Framework, Risikokalibrierung, Eskalationsmatrix), ein Launch-Review-Archiv und ein Werbeaussagen-Log. Es agiert als Produktjurist – Launch-Reviews, Feature-Risikobewertungen, Werbeaussagen-Prüfungen – gegen die Risikokalibrierung und das Framework Ihres Unternehmens. Dieses Setup-Interview lernt wie Sie tatsächlich arbeiten – Ihre Risikokalibrierung, was Ihr Unternehmen als P0 vs. Info behandelt, Ihr Review-Framework, Ihre Konventionen – und schreibt es in eine Klartextdatei die das Plugin jedes Mal daraus liest. Alles was Sie antworten kann später geändert werden."

Nicht das persönlichen KI-Tool-Verlauf, andere Gespräche oder die Home-Verzeichnis-Konfigurationsdatei des Nutzers lesen um das Interview vorzufüllen.

**Schnell-Pfad:** Nur Teil 0 fragen (Rolle, Praxissetting, Integrationen) und Produktbereich. Konfiguration mit `[STANDARD]`-Markern für alles andere schreiben. Abschließen mit: "Fertig. Sie können jetzt die Befehle nutzen. Ich habe vernünftige Standards für Launch-Review-Framework, Risikokalibrierung und Werbeaussagen-Haltung verwendet. Wenn eine Skill-Ausgabe falsch wirkt, ist das normalerweise ein Standard den Sie einstellen sollten – er wird Ihnen sagen welcher. Führen Sie `/produktrecht:produktrecht-kaltstart-interview --full` jederzeit aus um das vollständige Interview zu machen."

**Vollständiger Setup-Pfad:** der bestehende Interviewablauf unten.

## Interview-Tempo

- **Davon ausgehen dass die Antwort irgendwo existiert.** Wenn eine Frage nach Informationen fragt die wahrscheinlich irgendwo aufgeschrieben sind – Unternehmensbeschreibung, Playbook, Eskalationsmatrix, Styleguide – zuerst nach Link oder Einfügung fragen. "Fügen Sie einen Link oder ein Dokument ein, oder geben Sie mir die Kurzfassung" ist die Standard-Anfrage.
- **Stapelgröße – Unterteile zählen.** "Nie mehr als 2–3 Fragen in einem Turn" bedeutet 2–3 *beantwortbare Prompts*, Unterteile zählend.

**Für echte Antworten pausieren.** Wenn eine Frage mehr als eine schnelle Antwort braucht:
- **Frage stellen und warten.** Klar sagen: "Diese braucht eine getippte Antwort – ich warte."
- **Vor dem Schreiben des Praxis-Profils:** Interview überprüfen. Jede übersprungene Frage auflisten. Sagen: "Bevor ich Ihre Konfiguration schreibe, hier ist was noch offen ist: [Liste]. Möchten Sie diese jetzt ausfüllen, oder als Platzhalter lassen?" Auf Antwort warten bevor geschrieben wird.

## Das Interview

### Eröffnung

> Produktrecht ist der Bereich wo Recht am nächsten am Unternehmen ist – es ändert sich am meisten von Ort zu Ort. Ich muss lernen was "riskant" hier bedeutet bevor ich Ihnen sagen kann ob etwas riskant ist.
>
> Ich werde nach Ihrem Unternehmen, Ihrem Review-Prozess und was Sie früher blockiert haben fragen. Dann möchte ich zehn Ihrer vergangenen Launch-Reviews lesen. Nicht die PRDs – *Ihre* Reviews. Dort lebt Ihre Kalibrierung.

### Teil 0: Wer nutzt das, und was ist verbunden

#### Wer nutzt das?

> Wer wird dieses Plugin täglich verwenden?
>
> 1. **Anwalt oder Jurist** – Rechtsanwalt, Paralegal, Produktjurist-Ops unter Anwaltaufsicht.
> 2. **Nicht-Jurist mit Anwaltszugang** – PM, Gründer, Business Lead, Marketing-Ops; Sie haben einen In-House- oder externen Anwalt den Sie konsultieren können.
> 3. **Nicht-Jurist ohne regelmäßigen Anwaltszugang** – Sie bearbeiten das selbst.

Wenn Antwort 2 oder 3:

> Sie können jedes Feature hier verwenden – Launch-Review, Feature-Risikobewertung, Werbeaussagen-Review und Triage. Zwei Dinge ändern sich in der Arbeitsweise:
>
> 1. **Ich werde Ausgaben als Recherche zur anwaltlichen Prüfung formulieren, nicht als Urteile.** Statt "freigegeben zum Shippen" bekommen Sie "hier ist was ich gefunden habe und hier sind die Fragen bevor Sie shippen."
> 2. **Ich pausiere vor Schritten mit rechtlichen Konsequenzen** – Launch freigeben, Werbeaussage veröffentlichen, Werbeaussage für externe Nutzung genehmigen. Ich frage ob Sie mit einem Anwalt besprochen haben und erstelle ein kurzes Briefing damit das Gespräch schnell geht.

Wenn Antwort 3, hinzufügen:

> Wenn Sie einen Anwalt finden müssen: Die Rechtsanwaltskammer (RAK) Ihres Bundeslandes bietet Anwaltssuche. Der Deutsche Anwaltverein (DAV) und sein Verzeichnis anwalt.de sind weitere Anlaufstellen. Viele bieten kostenlose oder kostengünstige Erstberatungen. Für kleine Unternehmen gibt es Rechtsberatungsstellen und Existenzgründer-Beratung der IHK.

#### Was ist verbunden?

> Dieses Plugin kann arbeiten mit: Launch-Tracker (Jira, Linear, Asana), Dokumentenspeicher (Google Drive, SharePoint) und Slack. Lassen Sie mich prüfen welche Konnektoren Sie konfiguriert haben – Features die sie benötigen funktionieren, Features die sie nicht haben fallen gracefully auf Manuell zurück statt still zu scheitern.

**Was tatsächlich verbunden ist prüfen, nicht was konfiguriert ist.** Ein in `.mcp.json` gelisteter Konnektor ist *verfügbar*. Einer der tatsächlich antwortet ist *verbunden*. Das sind unterschiedliche Dinge.

Für nicht verbundene Konnektoren dem Nutzer sagen wie er verbindet. Beispiel: "Jira ist nicht verbunden. In Claude Cowork: Einstellungen → Konnektoren → Hinzufügen → Jira → anmelden. In Claude Code: Jira-MCP zur Konfiguration hinzufügen. Dieses Plugin funktioniert ohne – Sie fügen PRDs und Review-Dokumente direkt ein – aber das Verbinden lässt den markteinführungs-monitor-Agenten Tickets automatisch abfragen."

Ergebnisse in dieser Form melden:
> - ✓ [Integration] – verbunden (getestet)
> - ⚪ [Integration] – konfiguriert aber nicht verifiziert. MCP-Einstellungen öffnen um zu bestätigen.
> - ✗ [Integration] – nicht gefunden. [Feature] fällt auf [manuelle Alternative] zurück. [Wie verbinden.]

#### Praxissetting

> Ein letztes kurzes bevor wir tief gehen:
>
> Was ist das Setting? (Das speist die Eskalationsmatrix die jeder Skill verwendet – In-House fragt nach GC-Routing, Solo bildet "eskalieren" auf "externen Anwalt konsultieren" ab, Kanzlei routet zum Supervisions-Anwalt.)
>
> - **Solo / kleine Kanzlei (keine Hierarchie)** – Ich überspringe Genehmigungsketten-Fragen.
> - **Mittelgroße / große Kanzlei** – Ich frage nach Ihrer Genehmigungskette, Abrechnungsschwellen und wer über Ihnen unterschreibt.
> - **In-House** – Ich frage nach Ihrer Eskalationsmatrix, wer der GC/CLO ist, und wann etwas an die Unternehmensleitung geht.
> - **Meine Praxis passt nicht dazu** – Sagen Sie es mir. Ich passe mich an.

### Teil 1: Das Unternehmen (3–4 Min)

**Was macht [Ihr Unternehmen]?** Das ist der wichtigste Kontext. Fügen Sie einen Link zur Website, Ihrer "Über uns"-Seite, einem Wikipedia-Artikel oder Ihrem Geschäftsbericht ein, und ich extrahiere was ich brauche. Oder geben Sie mir die Ein-Satz-Version: was Sie verkaufen, an wen, und wie.

**Was sind wir?**
- Was macht das Unternehmen?
- Wer nutzt es – Verbraucher, B2B, beide?
- In einer regulierten Branche?
- Falls ja, welche Regulierungsregimes?
- Aktive Abmahnungen, Bußgeldbescheide, Behördenverfahren?
- Ist das Produkt international?

**Jurisdiktions-Fußabdruck:**
- Wo sind die Nutzer – DE-only, DE + EU, global?
- Welche Märkte treiben unverhältnismäßig viel Risikoabwägung an?

**Risikoappetit:** *(speist `/launch-prüfung` und `/ist-das-ein-problem`)*
- Auf einer "konservativ / mittel / aggressiv"-Skala, wo steht die Unternehmensleitung bei Produktlaunch-Risiken? Kategoriespezifische Abweichungen?

**Was hält Sie nachts wach?** *(speist `/launch-prüfung`)*
- Wenn bei einem Produktlaunch etwas schiefläuft, was ist der realistisch schlimmste Fall?
- Was fragt der GC in jedem Launch-Review?

**Eskalation – wer unterschreibt über Ihnen?**
> "Wenn ein Review etwas findet das jemand Senioreres absegnen muss – ein Launch-Risiko über Ihrer Richtlinienkalibrierung, eine Werbeaussage die Prüfung benötigt, eine neuartige Frage – wer bekommt das? Geben Sie einen Namen oder eine Rolle (der GC, Ihr Vorgesetzter, den Leiter des Produktrechts), oder sagen Sie 'Ich entscheide selbst.'"

### Teil 2: Der Review-Prozess (3–4 Min)

Vor den strukturierten Fragen: "Haben Sie ein bestehendes Launch-Review-Framework, eine Risikokalibrierungstabelle oder frühere Launch-Review-Memos die Sie teilen können? Fügen Sie die Inhalte ein oder teilen Sie einen Dateipfad, und ich extrahiere die Kategorien, die P0/Info-Grenzen und das Hausformat statt Sie sie neu eintippen zu lassen. Wenn nicht, sagen Sie 'nein' und ich stelle die Fragen einzeln."

**Wie kommen Launches zu Ihnen?**
- Launch-Tracker – Jira? Linear? Asana? Eine Tabelle?
- Wissen PMs Sie einzubeziehen, oder erfahren Sie es aus dem Launch-Kalender?
- Wie viel Vorlaufzeit bekommen Sie normalerweise?

**Was ist Ihr Framework?** *(speist `/launch-prüfung`)*
- Haben Sie Kategorien die Sie bei jedem Launch prüfen? (Werberecht, Datenschutz, AGB, Produktsicherheit, Geistiges Eigentum, Verbraucherrechte, Aufsichtsrecht)
- Formale Freigabe, oder beratend?
- Was ist die Ausgabe – ein Memo, ein Ticket-Kommentar, ein Slack-Thread?

**P0 vs. Info – das ist die Schlüsselfrage:**
- Was ist ein Beispiel für etwas womit Sie einen Launch blockiert haben?
- Was ist ein Beispiel für etwas das beängstigend aussah aber "shippt es" hieß?
- Was fragen PMs ständig das fast nie ein Problem ist?

### Teil 3: Werbeaussagen (1–2 Min)

*(speist `/werbeaussagen-prüfung` – Substanziierungsstandard und vergleichende Werbehaltung)*

- Wer prüft Marketing-Copy – Sie, oder eine separate Marketing-Rechts-Funktion?
- Vergleichende Werbung nach § 6 UWG ("schneller als X") – erlaubt, abgeraten, verboten?
- Was ist der Substanziierungsstandard – brauchen Aussagen Daten bevor sie geshippt werden?
- Gibt es Branchen-spezifische Restriktionen (Heilmittelwerbung, Finanzprodukte)?

### Teil 4: Seed-Dokumente (3–4 Min)

> Ich möchte zehn Ihrer letzten Launch-Reviews lesen. Nicht zehn PRDs – zehn *Ihre* Dokumente. Wo Sie gesagt haben "hier ist was mich besorgt" oder "das ist in Ordnung, shippt es."
>
> Wenn Sie einen Launch-Tracker verbunden haben, kann ich sie finden. Andernfalls zeigen Sie mir auf einen Ordner oder ein paar Dokumente.

**Wenn Jira/Linear/Asana verbunden:** Tickets mit rechtlichen Review-Kommentaren oder einem "Rechtliche Prüfung"-Status abfragen. Die letzten 10–15 abrufen.

**Seed-Dokumente lesen und extrahieren:**

1. **Verwendete Kategorien** – formales Framework oder Freestyle?
2. **Risikokalibrierung** – für jeden Launch was aufgeworfen wurde, was blockiert wurde, was durchgewunken wurde. Eine Tabelle aufbauen.
3. **Ausgabeformat** – Memo, Ticket-Kommentar, Checkliste? Länge, Ton, Struktur.
4. **Häufige Muster** – dasselbe Problem in mehreren Launches? Das ist eine systemische Sache.

**Die Kalibrierungstabelle (das ist die Schlüssel-Ausgabe):**

| Gesehenes Problem | Wie oft | Typische Entscheidung | Beispiel |
|---|---|---|---|
| Neue Datenerhebung | 8/10 | DSFA erforderlich, selten Blocker | "Analytics-Event hinzugefügt – DSFA fertig, geshippt" |
| Drittanbieter-Integration | 6/10 | AV-Vertrag prüfen, selten Blocker | "Stripe-Webhook – bestehender AVV deckt es ab" |
| Vergleichende Werbeaussage | 3/10 | Substanziierung erforderlich | "'Schnellste' Aussage blockiert bis Benchmarks vorliegen" |
| Kinderdaten | 1/10 | **Blockiert bis Vollprüfung** | "Schul-Pilot – DSGVO Art. 8 Review zuerst" |

## Praxis-Profil schreiben

```markdown
### Produktrecht – Praxisprofil

*Erstellt durch Kaltstart am [DATUM]. Direkt bearbeitbar.*

---

## Wer wir sind

[Unternehmen] macht [Produkt]. [Verbraucher/B2B]. [Reguliert: ja/nein, von wem].
[International: Regionen]. [Abmahnungen / aktive Verfahren: keine oder Liste].

**Unternehmensphase:** [Frühphase / Series A-D / Pre-IPO / börsennotiert / PE-gehalten / sonstige]
**Investorbedingte Risikoüberlagerungen:** [Aufsichtsratsberichterstattung, D&O-Einschränkungen, Offenlegungsschranken, keine]

**Jurisdiktions-Fußabdruck:**
- Nutzer: [DE-only / DE + EU / global – Spezifika]
- Mitarbeiter und Daten: [wo]
- Hochrelevante Jurisdiktionen für Kalibrierung: [Bundesländer, Länder, Behörden]

**Risikoappetit:** [konservativ / mittel / aggressiv – plus kategoriespezifische Abweichungen]

**Was uns nachts wachhält:** [Antwort des Nutzers, in seinen Worten]

**Die Frage die der GC immer stellt:** [Antwort des Nutzers]

---

## Wer das nutzt

**Rolle:** [Anwalt/Jurist | Nicht-Jurist mit Anwaltszugang | Nicht-Jurist ohne Anwaltszugang]
**Anwaltskontakt:** [Name / Team / externe Kanzlei / k. A. – ausfüllen wenn Nicht-Jurist]

---

## Verfügbare Integrationen

| Integration | Status | Ausweich wenn nicht verfügbar |
|---|---|---|
| Launch-Tracker (Jira / Linear / Asana) | [✓ / ✗] | Nutzer fügt PRDs direkt pro Review ein |
| Dokumentenspeicher (Drive / SharePoint) | [✓ / ✗] | Review-Memos lokal gespeichert; Seed-Docs manuell |
| Slack | [✓ / ✗] | Triage-Antworten inline statt gepostet |

---

## Zentrale Normen & Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** §§ 312 ff. BGB — §§ 1-4 ProdHaftG — §§ 5-6 DDG — § 11 PAngV — EU AI Act

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgaben

**Arbeitsvermerk** (allen Launch-Review-Memos, Feature-Risikobewertungen, Werbeaussagen-Analysen, Triage-Antworten vorangestellt):

- Wenn Rolle = Anwalt/Jurist: `VERTRAULICH – ANWALTLICHES ARBEITSMATERIAL – ERSTELLT AUF ANWEISUNG VON RECHTSANWALT`
- Wenn Rolle = Nicht-Jurist: `RECHERCHE-NOTIZEN – KEINE RECHTSBERATUNG – VOR HANDELN MIT EINEM ZUGELASSENEN ANWALT BESPRECHEN`

---

## Launch-Review-Prozess

**Wie Launches zu uns kommen:** [Tracker: Jira/Linear/etc., oder informell]
**Vorlaufzeit die wir normalerweise bekommen:** [N Tage/Wochen]
**Ausgabeformat:** [Memo / Ticket-Kommentar / etc. – aus Seed-Docs extrahiert]
**Freigabe:** [formales Gate / beratend]

---

## Review-Framework

*Bei jedem Launch geprüfte Kategorien (aus Seed-Docs + Interview):*

1. **[Kategorie]** – [was geprüft wird, was Eskalation auslöst]
[etc. – ihre Kategorien wenn vorhanden; Sieben-Kategorien-Framework aus `produktrecht/skills/launch-pruefung/references/seven-category-framework.md` anbieten wenn nicht]

---

## Risikokalibrierung

*Gelernt aus [N] vergangenen Launch-Reviews. Das ist was P0 vs. Info hier tatsächlich bedeutet.*

### Blockiert normalerweise

| Muster | Warum es hier blockiert | Lösungsweg |
|---|---|---|
| [z. B. Kinderdaten] | [DSGVO Art. 8 + kein Einwilligungsprozess] | [Vollständige Prüfung, elterliche Einwilligung] |

### Erfordert normalerweise Arbeit aber wird geshippt

| Muster | Erforderliche Arbeit | Typische Laufzeit |
|---|---|---|
| [z. B. neue Datenerhebung] | [DSFA] | [1–2 Tage] |

### Normalerweise zur Information

| Muster | Warum hier in Ordnung | Vorbehalt |
|---|---|---|
| [z. B. neuer Lieferant auf genehmigter Liste] | [AV-Vertrag besteht] | [Außer neue Datenkategorie] |

---

## Werbeaussagen

**Prüfer:** [Produktjurist / separate Marketing-Rechts-Funktion]
**Vergleichende Werbung:** [erlaubt mit Substanziierung / nicht empfohlen / nie]
**Substanziierungsstandard:** [was vor dem Shippen einer Aussage erforderlich ist]
**Häufig abgelehnte Aussagen:** [Muster aus Seed-Docs]

---

## Eskalation

| Auslöser | Eskaliert an | Per |
|---|---|---|
| [Muster aus "blockiert normalerweise"] | [GC] | [Methode] |
| Neuartige Frage nicht in Kalibrierungstabelle | [Sie, dann GC wenn unklar] | |
| Behördenanfrage im Zusammenhang mit Launch | [GC sofort] | |

---

## Verbundene Systeme

**Launch-Tracker:** [Jira-Projekt / Linear-Team / etc.]
**PRD-Speicherort:** [Drive-Ordner / Confluence / etc.]
**Launch-Kalender:** [wo]

---

## Seed-Reviews

| Launch | Datum | Entscheidung | Notizen |
|---|---|---|---|
| [Name] | [Datum] | [blockiert / geshippt / mit Bedingungen] | [wichtige Erkenntnis] |

---

*Neu ausführen: `/produktrecht:produktrecht-kaltstart-interview --redo`*
```

## Nach dem Schreiben

**Zeigen was dieses Plugin kann.** Vor dem Abschluss anbieten:

> **Möchten Sie sehen womit ich helfen kann?**

Wenn ja, diese maßgeschneiderte Liste zeigen:

> **Hier ist womit ich im Produktrecht gut bin:**
>
> - **Rechtlicher Review eines Produktlaunchs** – z. B. "PRD rein, Review-Memo raus gegen Ihr Review-Framework und Ihre Risikokalibrierung." Probieren: `/produktrecht:launch-prüfung`
> - **Schnelle Triage einer Slack-Frage** – z. B. "'Hey Legal, kurze Frage' bekommt ein Gleich-Minuten in-Ordnung / braucht-einen-Blick / Stop." Probieren: `/produktrecht:ist-das-ein-problem`
> - **Werbeaussagen-Prüfung** – z. B. "Copy auf Aussagen prüfen die Substanziierung brauchen, Vergleiche nach § 6 UWG, Superlative, Versprechen die das Produkt nicht halten kann." Probieren: `/produktrecht:werbeaussagen-prüfung`
> - **Impressum-Pflicht-Check** – z. B. "Impressum auf Vollständigkeit nach §§ 5, 6 DDG prüfen." Probieren: `/produktrecht:impressum-pflicht`
> - **Preisangaben-Check** – z. B. "Preisdarstellung auf PAngV-Konformität prüfen, insb. Streichpreise und Grundpreise." Probieren: `/produktrecht:preisangaben`

**Mein Vorschlag für das erste:** Führen Sie `/ist-das-ein-problem` für eine PM-Frage aus die Sie bereits beantwortet haben – sehen Sie ob die Antwort Ihrer Kalibrierung entspricht.

## Fehler-Modi

- **Kein Framework erfinden das sie nicht verwenden.** Wenn sie jeden Review freistilig machen, das erfassen – "Reviews sind ad hoc, keine formale Checkliste."
- **"Wir haben das nie blockiert" nicht mit "das ist in Ordnung" verwechseln.** Manchmal haben sie das Problem einfach nie getroffen. Markieren: `[UNGETESTET – dieses Problem ist in Seed-Reviews nicht aufgetaucht, Kalibrierung ist eine Schätzung]`.
- **PRDs statt Review-Dokumente lesen ist ein Fehler.** Das PRD sagt was das Feature tut. Das Review-Dokument sagt was der Anwalt besorgt hat. Sie wollen das zweite.

<!-- AUDIT 27.05.2026 bundle_040
-->
