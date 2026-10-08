# CLAUDE.md — Repo-Leitfaden für Sprachmodelle

Dieser Leitfaden ist verbindlich für jeden Modell-Lauf, der in diesem
Repository Vorlagen erstellt, ändert oder bewertet. Er ergänzt
`CONTRIBUTING.md` (für menschliche Mitwirkende) und wird vor jedem
Lauf in Kontext geladen.

## 1. Sprache und Schreibweise

- Alle Texte in **deutscher Rechtschreibung**.
- **Sie-Form** als Standard in Mandantenkommunikation. Die Du-Form ist
  nur zulässig, wenn das Mandat sie ausdrücklich vorgibt.
- **Echte Umlaute und scharfes s**: ä ö ü Ä Ö Ü ß. Niemals
  ASCII-Ersatzschreibungen wie „ae", „oe", „ue", „Ae", „Oe", „Ue", „ss".
  Diese Regel gilt für Vorlagen, READMEs, Commit-Botschaften, PR-Titel
  und -Bodies, YAML-Beschreibungen, Skript-Hilfetexte. Einzige Ausnahme:
  technische Slugs in Dateinamen und URLs.
- Typografische Anführungszeichen („…") in Fließtext. ASCII-Quotes nur
  in Code, YAML-Strings und Skript-Snippets.
- Englische Fachbegriffe nur dort, wo etabliert (Letter of Intent, Term
  Sheet, Due Diligence) und im Vorlagentext einmal kurz erklärt.

## 2. Methodik

- **Gutachtenstil** für Memos (Sachverhalt — Frage — Kurzantwort —
  Bewertung — Ergebnis — Risiken — Quellenverzeichnis).
- **Urteilsstil** für Schriftsätze (Antrag — Sachverhalt — rechtliche
  Würdigung).
- **Mandantenbrief**-Struktur: Anrede/Bezug — Sachstand — Empfehlung —
  Nächste Schritte — Kostenhinweis — Unterschrift.
- Vertrags-, Satzungs-, Beschluss- und Vollmachtsvorlagen folgen dem
  Kautelarstandard aus `references/kautelarstandard.md`: Parteien,
  Vertretung, Form, Vollzug, Leistungsprogramm, Risikoallokation,
  Beendigung, Datenschutz, Streitregelung und bei zweisprachigen Fassungen
  Sprachvorrang. Die geforderte Regelungstiefe je Baustein und Vertragstyp
  steht in `references/regelungstiefe-vertraege.md`.
- Jede Überarbeitung folgt zusätzlich der Gegenstandsindividualisierung aus
  `references/gegenstandsindividualisierung.md`: Vor der ersten Änderung wird
  intern fixiert, welcher konkrete Gegenstand, welche Rollen, welche
  Interessenlage, welche Rechtsordnung und welche fallspezifischen Risiken
  dieses Dokument tragen. Jeder Satz muss auf diesen Gegenstand einrasten.
- Jede Vorlagendatei braucht oben einen klaren Rubrum-, Parteien-,
  Beteiligten- oder Adressatenkopf und unten einen Schluss-,
  Unterzeichnungs-, Einreichungs- oder Freigabeblock. Auch leere Muster
  müssen sofort erkennen lassen, wer handelt, gegen wen oder für wen die
  Vorlage wirkt, welches Gericht, welche Behörde oder welche Stelle
  adressiert wird und wer die finale Fassung unterzeichnet oder freigibt.
- Rubrum, Vertragseingang, notarieller Urkundseingang und Adressatenkopf
  werden als normaler Eingangstext gesetzt, niemals als Bulletpoint-Liste
  und nicht als listenartige Parteienschablone. Ausfüllfelder stehen im
  gesamten Dokument in eckigen Klammern, etwa `[vollständiger Name,
  Anschrift, Vertretung]`, `[Datum]` oder `[Betrag in EUR]`. Spitze
  Klammern sind in Vorlagen nicht mehr als Platzhalter zulässig.
- Bei Verträgen steht eine Präambel nur dort, wo sie inhaltlich trägt,
  dann aber als erster materieller Abschnitt `1. Präambel / Gegenstand`.
  Eine Präambel steht niemals unnummeriert vor dem Vertragstext. Das Rubrum
  steht davor als formaler Kopf; es ersetzt nicht die Vertragsparteien, den
  Gegenstand oder die Unterschriften. Wenn ein Vertrag Abschnitt
  `1. Präambel / Gegenstand` enthält, muss in den Schlussbestimmungen
  ausdrücklich stehen, dass Abschnitt 1 Bestandteil dieses Vertrags ist und
  Regelungsgehalt hat.
- Der Gegenstand wird im formalen Kopf nur knapp als Akten- oder
  Fassungsangabe genannt. Ein materieller Gegenstandstext steht als
  nummerierter Abschnitt `1. Gegenstand` oder bei Verträgen als
  `1. Präambel / Gegenstand`; ein fett gesetzter Zwischenkopf
  `**Gegenstand:**` vor dem ersten Regelungsabschnitt ist unzulässig.

## 3. Quellen

- Jede juristische Aussage belegt.
- Zitierweise verbindlich nach `references/zitierweise.md`; Primärquellen
  nach `references/pruefquellen.md` prüfen.
- Leitentscheidungen aus `references/leitentscheidungen-anker.md`
  dienen als **Such-Gerüst**, nicht als Zitatpool. Vor Übernahme in
  eine Mandatsfassung: Az. live in der amtlichen oder primären Quelle
  verifizieren.
- Amtliche Startpunkte aus
  `references/rechtsprechungsradar-amtliche-pruefanker.md` sind
  Prüfanker. Sie dürfen nicht ungeprüft als fertige Zitate übernommen
  werden; Pressemitteilungen tragen keine Randnummernzitate.
- Lieber **weniger** Rechtsprechung zitieren als spekulativ.

## 4. Verboten

- **Halluzinierte Aktenzeichen.** Wenn nicht verifizierbar, weglassen.
- **Präjudizienbindungs-Argumente**, außer im Rahmen von § 31 BVerfGG.
- **Verletzungen des Mandantengeheimnisses** (§ 43a Abs. 2 BRAO,
  § 203 Abs. 1 Nr. 3 StGB). Mandatsbezogene Inhalte vor Eingabe in
  Drittsysteme anonymisieren oder pseudonymisieren.
- **Erfundene Klar-Namen** im Vorlagentext (z. B. „Max Mustermann"). Nur
  Platzhalter in eckigen Klammern: `[Name]`, `[Datum]`, `[Az.]`.
- **Vermeintliche** Volltext-Zitate aus dem Modellwissen ohne Quelle.

## 5. Konversationsstil im Mandat

- Kurz starten, schnell zum Dokument.
- Keine Lehrbuch-Intros, keine ausschweifenden Vorreden.
- Sofort Entwurf liefern, mit `[noch zu klären: …]`-Platzhaltern für
  offene Tatsachenfragen.
- Bei Zwischenfragen: präzise, nicht belehrend.

## 6. Vorspruch und Kurz-Hinweis

Jede Vorlagen-Markdown-Fassung und die zugehörige ODT-Fassung beginnen nach
dem H1-Titel nur mit einem kurzen Hinweis. Der ausführliche Vorspruch steht
ausschließlich in der `README.md` des jeweiligen Vorlagenordners. Die
Mustertexte stehen in `templates/_kurzhinweis.md` und
`templates/_readme-vorspruch.md`.

Der kurze Hinweis in der Vorlage muss weiterhin die prüfbaren Kerntokens
enthalten, damit der Eval-Harness erkennt, dass die Nutzungsgrenze nicht
entfernt wurde:

- unverbindlich
- experimenteller Text
- keine Rechtsberatung
- Verwendung ausschließlich auf eigene Gewähr und auf eigene Gefahr
- Verweis auf BRAO § 43a Abs. 2, StGB § 203, DSGVO
- Lizenz Apache-2.0 ODER MIT

Ausführliche Erläuterungen, Haftungsgrenzen, Datenschutz- und
Verschwiegenheitshinweise gehören in die README, nicht in den eigentlichen
Vertrags-, Schriftsatz- oder Formulartext.

### 6.1 Verbindliche Erstseiten-Fußzeile

Jede paginierte ODT-Fassung trägt ausschließlich auf Seite 1 in der Fußzeile
den folgenden zweisprachigen Hinweis:

> Mit KI generiert. Dies ist ein experimentelles Dokument. Benutzung auf
> eigene Gefahr und eigenes Risiko.
>
> Generated with AI. This is an experimental document. Use at your own risk.

Der Hinweis gehört nicht in den Markdown-Mustertext und nicht in dessen
materiellen Regelungsinhalt. `scripts/md-to-odt.py` setzt ihn zentral als
Erstseiten-Fußzeile; Folgeseiten tragen nur die Seitennummer.
`scripts/check-odt-integrity.py` prüft bei jeder bestehenden und neu erzeugten
ODT-Fassung Wortlaut, Einmaligkeit und Position. Manuelle Abweichungen sind
nicht zulässig.

## 7. Eval-Harness

Vor jedem Commit:

```
python3 scripts/run-eval.py --report
```

Erforderlich: `All-Pass: <N>/<N>`. Das human_review-Token
(`r90-az-live-verifiziert`, `r91-endpruefung-anwalt`) wird als
`skipped` gewertet und blockiert den Auto-Merge nicht — muss aber im
PR-Body kommentiert sein.

Modellvergleich:

```
python3 scripts/run-eval.py --json-out runs/<label>.json --label <label>
python3 scripts/compare-eval-runs.py runs/<label1>.json runs/<label2>.json
```

Stiltreue-Prüfungen (Spezial-Stilebenen, z. B. Kanonik, klassisches
Latein, PrALR) über `scripts/llm-judge-eval.py`. Der Judge läuft im
Dry-Run, wenn kein `ANTHROPIC_API_KEY` gesetzt ist — der Prompt wird
dann zur manuellen Übergabe ausgegeben.

## 8. Git-Konventionen

- **PRs nicht als Draft**; direkt als „ready".
- **Merge per Merge-Commit** auf `main`.
- **Kein Force-Push** auf `main`.
- Branch-Namen klein, mit Bindestrich (`feature/<thema>`,
  `fix/<thema>`).
- Commit-Botschaften deutsch, mit echten Umlauten und ß.
- **Codex-Review verbindlich anstoßen — nicht blockierend.** Der
  Standardworkflow je PR ist exakt:
  1. PR erzeugen (`mcp__github__create_pull_request`, `draft: false`).
  2. Direkt im Anschluss einen Kommentar mit dem Inhalt
     `@codex review` posten (`mcp__github__add_issue_comment`).
  3. **Sofort** mergen (`mcp__github__merge_pull_request`,
     `merge_method: merge`) — **nicht** auf Codex' Antwort warten.

  Ausnahmen vom Standardworkflow:

  - **Draft-PR vom Nutzer angefordert:** PR mit `draft: true` erzeugen,
    **nicht** mergen. Der `@codex review`-Kommentar wird erst gepostet,
    sobald der PR vom Nutzer auf „ready" gesetzt wurde. Auf das Go des
    Nutzers warten.
  - **Review-Pause vom Nutzer angefordert (ohne Draft):** PR mit
    `draft: false` (ready) erzeugen und direkt im Anschluss
    `@codex review` posten, aber **nicht** mergen. Auf das Go des
    Nutzers warten — der ready-PR bleibt zur Prüfung offen.
  - Wenn weder Draft noch Pause angefordert wurde, gilt der
    Standardworkflow ohne Wartezeit auf Codex.

- Der erzeugte `DOWNLOADS.md`-Index ist die vollständige Downloadachse des
  Repositories. Er enthält den Schnellzugriff auf alle Rechtsgebiete, ODT-
  und Markdown-ZIP-Downloads der Hauptvorlagen sowie Einzel-Downloads jeder
  Datei unter `vorlagen-gerichtsleitend/`. Nach jeder Neuanlage, Löschung
  oder Umbenennung wird `python3 scripts/build-download-index.py` ausgeführt.

## 9. Skill-Konvention (falls Skills hinzukommen)

- Frontmatter genau `name` und `description`.
- `description` max. 1024 Zeichen.
- Keine Zahlen-Kommas in der `description` (statt „1,5" verwende „1.5"
  oder „eineinhalb").

## 10. Was dieser Harness NICHT leistet

- Keine inhaltliche Rechtsprüfung. Eine Vorlage kann formal alle Checks
  bestehen und trotzdem rechtlich falsch sein. Deshalb ist `r91-
  endpruefung-anwalt` (Endprüfung durch zugelassene Berufsträgerin)
  Pflicht.
- Keine Mandatssicherheit. Vorlagen sind Gerüst, kein Endprodukt.
- Kein Ersatz für die Sachfragen-Prüfung am konkreten Mandat.

## 11. Rechtsprechungs-Hyperlinks

Eine Gerichtsentscheidung darf in einer fertigen Mandatsfassung nur dann
als Zitat erscheinen, wenn sie mit einem Hyperlink zur offiziellen oder
anerkannten Quelle versehen ist. Die maßgeblichen Quellen stehen in
`references/pruefquellen.md`.

Unverifizierbare oder halluzinierte Entscheidungen dürfen **nicht**
zitiert werden — weglassen, wenn kein Direktlink verifizierbar. Dies
gilt auch für Rechtsprechungsanker in Vorlagen. Dort sind Suchbegriffe
für die Live-Recherche ausreichend; Aktenzeichen bleiben Rechercheanker,
bis Datum, Entscheidungsform, Fundstelle und Randnummern live geprüft sind.

## 12. Anwendungshinweise nur im README

Hinweise darüber, wofür eine Vorlage geeignet oder nicht geeignet ist
(„geeignet für …", „nicht geeignet bei …", „Anwendungsbereich",
„typische Einsatzfälle", „Hinweise zur Verwendung" u. Ä.), gehören
**ausschließlich in die `README.md`** des jeweiligen Vorlagenordners.

In der jeweiligen Vorlagen-Markdown- und ODT-Fassung dürfen solche
Anwendungshinweis-Abschnitte **nicht** enthalten sein. Dort gehören nur
die eigentlichen Vertragstexte, Schriftsätze, Formulare oder Muster.

## 13. Abkürzungserklärung

Ungewöhnliche Gesetzesabkürzungen müssen beim ersten Auftreten in einer
Datei (`README.md` oder sprechend benannte Vorlagen-Markdown-Datei) ausgeschrieben werden. Als
„ungewöhnlich" gelten alle Abkürzungen, die nicht zum allgemeinen
juristischen Grundwortschatz (BGB, HGB, ZPO, StGB, GG u. Ä.) gehören.
Beispiele, die zwingend einmal ausgeschrieben werden müssen:

- CMR (Übereinkommen über den Beförderungsvertrag im internationalen
  Straßengüterverkehr)
- CISG (UN-Kaufrecht, Convention on Contracts for the International
  Sale of Goods)
- VOB/B (Vergabe- und Vertragsordnung für Bauleistungen, Teil B)
- ADSP (Allgemeine Deutsche Spediteurbedingungen)
- ZVG (Zwangsversteigerungsgesetz)
- InsO (Insolvenzordnung) — beim ersten Auftreten außerhalb des Titels
- StaRUG (Unternehmensstabilisierungs- und -restrukturierungsgesetz)
- WEG (Wohnungseigentumsgesetz)
- UmwG (Umwandlungsgesetz)
- GmbHG (Gesetz betreffend die Gesellschaften mit beschränkter Haftung)
- AktG (Aktiengesetz)

Das Schema ist: `<Abkürzung> (<Langform>)` beim ersten Auftreten im
Text; danach darf die Abkürzung allein stehen.

## 14. Gliederung, Nummerierung und Einrückung

Diese Regel gilt **ausnahmslos und ohne Bestandsschutz** für jede Vorlage
und jeden Vertrag in diesem Repository — sowohl in der MD- als auch in der
ODT-Fassung — und ist für **jeden Modell-Lauf** verbindlich, auch für
andere Systeme als Claude, insbesondere Perplexity, Codex und spätere
Agenten. Sie betrifft die Gliederung der Dokumente selbst (Abschnitte,
Klauseln, Absätze, Aufzählungen), nicht die Zitierweise von Normen und
Entscheidungen.

Detailspec: [gliederung](references/gliederung.md).
Prüfung im CI: `scripts/check-gliederung.py`.

### 14.1 Ausschließlich Dezimalgliederung

Gegliedert und durchnummeriert wird **nur dezimal**:

```
1
1.1
1.1.1
1.1.1.1
```

— und so weiter in beliebiger Tiefe. Jede andere Gliederung ist
**unzulässig**, insbesondere:

- römische Ziffern (`I.`, `II.`, `III.`, `iv)` …),
- Großbuchstaben- und Kleinbuchstaben-Ebenen (`A.`, `B.`, `C.`, `a)`,
  `b)` …),
- Buchstaben-Zahlen-Mischformen (`A.1`, `B.2`, `II.1` …),
- Klammer-Buchstaben in Präambeln und Erwägungsgründen (`(A)`, `(B)`,
  `(C)`),
- gemischte Verlagsgliederungen (`A. I. 1. a) aa)`), wie sie viele
  deutsch-juristische Verlage verwenden.

Grund: Eine durchgehende Dezimalgliederung bleibt eindeutig und sowohl
maschinell als auch menschlich referenzierbar. Bei gemischten Buchstaben-,
Ziffern- und Klammerebenen findet man sich nicht mehr zurecht.

Zulässig bleibt allein das Paragrafenzeichen als Klauselüberschrift in
Verträgen (`§ 1`, `§ 2` …), weil es eine arabische Zahl trägt; die
Unterpunkte einer solchen Klausel werden dann dezimal gebildet (`1.1`,
`1.2`, `1.2.1`) und niemals mit Buchstaben oder Klammerziffern.

### 14.2 Leerzeile zwischen den Ebenen

Sobald untergliedert wird, steht **zwischen einem Gliederungspunkt und
dem folgenden Text oder der nächsten Ebene eine Leerzeile**. Ohne sie
verklumpt der Text und wird unlesbar. Das gilt auch für fett gesetzte
Gliederungszeilen im Fließtext.

Richtig:

```
1   Leistungsumfang

   1.1   Der Auftragnehmer erbringt die in Anlage 1 beschriebenen Leistungen.

   1.2   Nicht geschuldet sind Leistungen, die dort nicht genannt sind.
```

Falsch (keine Leerzeilen, alles verklumpt):

```
1 Leistungsumfang
1.1 Der Auftragnehmer erbringt die in Anlage 1 beschriebenen Leistungen.
1.2 Nicht geschuldet sind Leistungen, die dort nicht genannt sind.
```

### 14.3 Maßvolle Einrückung

Eingerückt wird **sparsam**: gerade so viel, dass die Ebenen erkennbar
bleiben, aber nie so tief, dass das Dokument zerfleddert wirkt. Eine
geringe, gleichmäßige Einrückung je Ebene (etwa drei Leerzeichen oder
eine Listenebene) genügt. Tiefe Staffel-Einrückungen über mehrere
Ebenen sind zu vermeiden; im Zweifel lieber flacher und ruhiger setzen,
damit das Dokument gut aussieht. Markdown-Quelltext kennt eine wichtige
Grenze: keine Vier-Leerzeichen-Einrückungen, weil Markdown diese als
Codeblock interpretiert.

### 14.4 Eindeutige Querverweise

Querverweise im Text und in README-Hinweisen referenzieren die
Gliederung **vollständig**: `siehe Abschnitt 3.2.1`, niemals `siehe a)
oben` — mehrdeutig, weil mehrere `a)` im Dokument existieren können.

## 15. Dateinamen für Vorlagen

Vorlagedateien tragen immer einen sprechenden Dateinamen. Der Dateistamm ist
identisch mit dem Vorlagen-Unterordner. Im Ordner
`grundschuldbestellung-notariell/` liegen also
`grundschuldbestellung-notariell.md` und
`grundschuldbestellung-notariell.odt`.

Nicht zulässig sind generische Dateinamen wie `vertrag.md`, `text.odt`,
`antrag.md`, `vorlage.md`, `VORLAGE.odt`, `SKILL.md`, `SkillMD` oder ähnliche
Platzhalter. Vor jedem Commit wird geprüft, ob solche Dateien noch oder wieder
im Repo liegen.

Direktdownload-Links in `README.md` müssen ebenfalls sprechend beschriftet
sein. Nicht zulässig sind Linktexte wie `vertrag.odt herunterladen`,
`text.md herunterladen`, `Markdown-Quelle` oder `ODT-Arbeitsfassung` ohne
Dokumentnamen. Der Linktext nennt kurz den konkreten Inhalt, etwa
`AGB Online-Shop B2C – ODT herunterladen`.

Der Markdown-Direktdownload verweist nicht auf die rohe `<slug>.md`,
sondern auf die gleichnamige `<slug>.md.zip` im selben Ordner. GitHub
serviert `.md` mit `Content-Type: text/plain`, sodass Browser die Datei
inline anzeigen statt herunterzuladen; die ZIP-Fassung erzwingt den
Download zuverlässig. Jede Vorlagen-Markdown ist deshalb von einer
byte-identischen `<slug>.md.zip` begleitet, die genau eine Datei (die
`<slug>.md`) mit deterministischem Zeitstempel enthält. Die ZIPs werden
durch `python3 scripts/build-md-zips.py` erzeugt; die CI prüft die
Synchronität durch `scripts/check-md-zip-integrity.py`. Der Linktext
lautet `... – Markdown (ZIP) herunterladen`, die Zusatzbeschriftung
`— Bearbeitbare Markdown-Fassung, gepackt für direkten Download`. Die
rohe `<slug>.md` bleibt im Block „Vorschau im Repository" als Vorschau-Quelle
verlinkt. Dieselbe Vorschauzeile verlinkt außerdem die lokale
`<slug>.odt`; der ODT-Direktdownload bleibt ein sprechend beschrifteter
`raw/main`-Link. `scripts/validate-vorlagen.py` prüft alle vier Ziele exakt.

Zusätzlich führt [`DOWNLOADS.md`](DOWNLOADS.md) jede Hauptvorlage mit
Menüseite, ODT-Direktdownload und Markdown-ZIP-Direktdownload. Nach jeder
Neuanlage, Löschung oder Umbenennung ist
`python3 scripts/build-download-index.py` auszuführen; der Validator
vergleicht den Index bytegenau mit dem kanonischen Bestand und prüft relative
Markdown-Links auf vorhandene Ziele. Vor Releases erzeugt
`python3 scripts/build-release-assets.py` die drei stabil benannten
Komplettpakete und `SHA256SUMS.txt` unter `dist/`; diese Dateien werden als
Release-Assets hochgeladen, aber nicht eingecheckt.

### 15.1 Drei-Ordner-Sicht nach Dokumenttyp

Die kanonische Ablage einer Vorlage bleibt immer der fachlich passende
Rechtsgebietsordner. Vorlagen werden nicht physisch in drei neue
Hauptordner verschoben, weil sonst Rubrics, ODT-Dateien, Markdown-ZIP-
Downloads und bestehende Direktlinks auseinanderfallen.

Die zusätzliche Sortierung nach Dokumenttyp steht ausschließlich unter
`kategorien/`:

- `kategorien/01-vertragliche-vorlagen/` für Verträge, Satzungen, AGB,
  Vollmachten, Sicherheiten, Vergleiche und sonstige kautelarische
  Vorlagen.
- `kategorien/02-prozessuale-vorlagen-und-formulare/` für Klagen,
  Anträge, Beschwerden, Widersprüche, behördliche und gerichtliche
  Formulare, Protokolle, Verzeichnisse, Nachweise und Dokumentationsmuster.
- `kategorien/03-sonstige-vorlagen/` für Leitvorlagen, Pläne, Vermerke,
  Risikomatrizen, Strategie- und Prüfpapiere sowie sonstige Arbeitshilfen.

Diese Ordner enthalten nur README-Indizes mit Links auf die Originalorte.
Neue Vorlagen werden zuerst im Rechtsgebietsordner angelegt; danach wird
genau ein Eintrag in der passenden Drei-Ordner-Sicht ergänzt. Vor jedem
Commit prüft `python3 scripts/check-kategorien-index.py`, ob jede Vorlage
genau einmal verlinkt ist und die Zähler in `kategorien/README.md` stimmen.

Zusätzlich wird jede Vorlage im `README.md` ihres Rechtsgebiets genau einmal
mit dem H1-Titel ihrer eigenen Vorlagen-README verlinkt. Das Wurzel-README
verlinkt jeden Rechtsgebietsordner. Diese fachliche Navigationsachse wird
durch `scripts/validate-vorlagen.py` geprüft; sie ersetzt die Drei-Ordner-
Sicht nicht, sondern ergänzt sie.

## 16. Keine Mandatsreife Prüfmatrix in Vorlagen

Der früher am Ende jeder Vorlagen-Markdown enthaltene Abschnitt
`Mandatsreife Prüfmatrix` wurde repoweit entfernt. Er wirkte als generische
Freigabeliste, die jede Vorlage gleich aussehen ließ und keinen konkreten
Mandatsbezug trug. Die anwaltliche Endprüfung erfolgt außerhalb der
Vorlage, anhand der vom Mandat gesetzten Anforderungen.

- `## Mandatsreife Prüfmatrix` und `### Mandatsreife Prüfmatrix` sind als
  Abschnittsüberschriften ausdrücklich verboten und werden vom Validator
  `scripts/validate-vorlagen.py` (`VERBOTENE_TEMPLATE_ABSCHNITTE`)
  blockiert.
- Der Pflicht-Token `Mandatsreife Prüfmatrix` ist aus
  `PFLICHT_TOKENS` entfernt; Vorlagen brauchen die Phrase nicht mehr zu
  enthalten.
- Der Eval-Rubric-Check `r81-mandatsreife-pruefmatrix` ist aus dem
  Generator `scripts/generate-default-rubrics.py` und aus allen
  bestehenden `rubric.yaml` gestrichen.
- Inhaltliche Prozessschritte zur Freigabe gehören in Mandatsakten,
  Checklisten oder Skill-Anweisungen, nicht in die ausgelieferte Vorlage.

## 17. Vollständige Sätze, keine Stummelsprache, kein generischer Fülltext

Diese Regel hat oberste Priorität und gilt ausnahmslos für jede
Vorlagen-Markdown- und ODT-Fassung.

- **Gegenstand zuerst fixieren.** Vor jeder Überarbeitung wird nach
  `references/gegenstandsindividualisierung.md` intern festgelegt, was genau
  geregelt oder geleistet wird, wer die Beteiligten sind, welches Recht gilt
  und welche Besonderheiten diesen Fall von vergleichbaren Dokumenten
  unterscheiden.
- **Ganze Sätze.** Der Vertrags-, Schriftsatz- und Vorlagentext wird
  durchgehend in vollständigen, grammatisch korrekten Sätzen ausformuliert.
  Keine Stummelsprache, keine Halbsätze, keine Telegramm- oder
  Stichwortklauseln. Auch Aufzählungspunkte im materiellen Text sind volle
  Sätze und nicht bloße Schlagworte. Statt „- Instrument, Standort,
  Stimmtonhöhe." heißt es etwa „Der Auftragnehmer stimmt das im Rubrum
  bezeichnete Instrument am vereinbarten Standort auf die gewünschte
  Stimmtonhöhe." Die Devise lautet: klar, sprachlich korrekt und eloquent.
- **Kein generischer Fülltext.** Keine inhaltsleeren Mustersätze, die in
  jeder beliebigen Vorlage stehen könnten — etwa „Diese Vorlage ist auf
  einen konkret geprüften B2B-Sachverhalt zugeschnitten …", „Die Kernpunkte
  dieses Musters sind …", pauschale „ergibt sich aus dieser Vereinbarung
  und der Anlage 1"-Floskeln oder generische `Feld | Eintrag`-
  Vertragsdaten-Tabellen, deren Angaben ohnehin im Vertragstext stehen.
  Jede Vorlage ist konkret auf ihren Vertragstyp zugeschnitten.
- **Anti-Generik-Test.** Jeder Satz wird gefragt: Könnte er unverändert in
  einem völlig anderen Vertrag, Schriftsatz, Skill oder Plugin stehen? Wenn
  ja, wird er auf die konkrete Leistung, Rolle, Frist, Schnittstelle,
  Rechtsfolge oder das konkrete Risiko dieses Dokuments zugespitzt oder
  gestrichen.
- **Präambel.** Trägt ein Vertrag eine Präambel, heißt der Abschnitt stets
  `1. Präambel / Gegenstand` (siehe Abschnitt 2).
- Ausgenommen bleiben allein strukturelle Freigabeelemente. Rubrum,
  Beteiligtenkopf, Vertragseingang und notarieller Urkundseingang stehen
  immer als normaler Eingangstext ohne Bulletpoints oder nummerierte
  Parteienliste.

## 18. Keine enge, zentrierte Spalte im Dokument

Der Fließtext einer Vorlage steht über die volle Satzbreite. Niemals wird
Body- oder Rubrumtext in eine schmale, mittig zentrierte Spalte gezwungen,
weder in der MD- noch in der ODT-Fassung.

Technischer Hintergrund: Pandocs `multiline_tables`/`simple_tables` deuten
die `---`-Trennlinien zwischen Abschnitten sonst als Tabellenränder und
packen ganze Textblöcke in eine einspaltige, zentrierte Tabelle.
`scripts/md-to-odt.py` schaltet diese Extensions daher ab; die Regel wird
über `scripts/check-odt-spaltenlayout.py` geprüft.

## 19. Zweisprachige Vorlagen immer zweispaltig

Jede zweisprachige (deutsch-englische) Vorlage stellt beide Sprachfassungen in
einer zweispaltigen Tabelle nebeneinander dar: **Deutsch in der linken,
Englisch in der rechten Spalte.** Die Spalten laufen satz- und absatzgenau
parallel, sodass jede deutsche Aussage in derselben Tabellenzeile ihrer
englischen Entsprechung exakt gegenübersteht — Satz für Satz, Absatz für
Absatz. Die Sprachfassungen werden niemals hintereinander, verschachtelt oder
vermischt gesetzt.

Umgesetzt wird die Zweispaltigkeit über eine Markdown-Pipe-Tabelle mit genau
zwei Spalten (deutsch links, englisch rechts). Diese Tabelle ist vollbreit und
gerade keine enge Mittelspalte (Abschnitt 18). Der Vorrang der deutschen
Fassung bleibt unberührt (Abschnitt 2 und Abschnitt 16); bei Auslegungszweifeln
ist die deutsche Spalte maßgeblich.
