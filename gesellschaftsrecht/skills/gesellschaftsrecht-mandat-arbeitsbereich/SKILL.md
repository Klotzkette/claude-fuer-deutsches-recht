---
name: gesellschaftsrecht-mandat-arbeitsbereich
description: "Mandats-Workspaces verwalten — anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen, damit Mehrfachmandatsanwälte den Kontext eines Mandats sauber von jedem anderen trennen. Wird von allen inhaltlichen Skills gelesen, die wissen müssen, in welchem Mandat sie arbeiten. Lädt bei „neues Mandat\", „Mandat wechseln\", „Mandate auflisten\", „Mandat schließen\" oder wenn der Nutzer nur auf Praxisebene arbeiten möchte."
---

# Mandats-Workspace

## Kernsachverhalt

Rechtsanwälte führen parallel mehrere Mandate. Jedes Mandat hat seinen eigenen Mandanten, seine eigene Gegenpartei, seine eigene Transaktionsphase, seine eigenen vertraulichen Unterlagen und seine eigene Handlungslogik. Die Vermischung von Mandatsinhalten — auch unbeabsichtigt — verletzt die anwaltliche Verschwiegenheitspflicht (§ 43a Abs. 2 BRAO, § 203 Abs. 1 Nr. 3 StGB) und kann Interessenkonflikte begründen (§ 43a Abs. 4 BRAO).

Dieser Skill verwaltet Mandats-Workspaces: Er legt sie an, listet sie auf, wechselt zwischen ihnen, schließt sie und archiviert sie. Alle inhaltlichen Skills im Gesellschaftsrecht-Paket lesen den aktiven Mandats-Workspace, bevor sie arbeiten, und beziehen sich ausschließlich auf dessen Kontext.

**Im M&A-Kontext** unterstützt dieser Skill die typischen Transaktionsphasen: NDA-Phase und Datenraumzugang, LOI-Phase, Due-Diligence, SPA-Verhandlung, Signing/Closing und Post-Closing-Integration.

## Kaltstart-Rückfragen

Vor Anlage eines neuen Mandats-Workspace sind folgende Angaben erforderlich:

1. **Mandant:** Name der vertretenen Partei (oder interne Geschäftseinheit bei In-house-Juristen)?
2. **Gegenpartei:** Wer ist die andere Seite (Käufer/Verkäufer, Mitgesellschafter, Schuldner)? Mehrere Gegenparteien möglich.
3. **Mandatstyp:** M&A Käuferseite / M&A Verkäuferseite / Finanzierung / Governance-Mandat / Gesellschaftsreorganisation / Integrationsprojekt / Sonstige?
4. **Transaktionsphase:** NDA | LOI | Due Diligence | SPA-Verhandlung | Signing/Closing | Post-Closing-Integration | Laufende Beratung?
5. **Vertraulichkeitsstufe:** Standard / Erhöht / Clean-Team? (Erhöht = besondere Sorgfalt in mandatsübergreifenden Settings.)
6. **Wesentliche Fakten:** 2–5 Sätze zu Gegenstand, Stakeholdern und dem, was auf dem Spiel steht.
7. **Mandatsspezifische Abweichungen vom Praxisstandard:** Was weicht von den Kanzlei-Standardvorgaben ab (z.B. abweichende Haftungsdeckelung, Sprachregelung, Rechtsordnung)?
8. **Verbundene Mandate:** Slug-Verweise auf verwandte Mandate (z.B. NDA-Mandat, das dem SPA-Mandat vorausging)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte mit Auszügen

**§ 43a Abs. 2 BRAO — Verschwiegenheitspflicht**
> „Der Rechtsanwalt ist zur Verschwiegenheit verpflichtet. Diese Pflicht bezieht sich auf alles, was ihm in Ausübung seines Berufes bekanntgeworden ist."

Die Verschwiegenheitspflicht gilt unbegrenzt zeitlich, auch nach Mandatsbeendigung. Sie gilt für alle Mitarbeiter der Kanzlei (§ 43a Abs. 2 S. 3 BRAO) und für alle Informationsträger — physisch und digital.

**§ 203 Abs. 1 Nr. 3 StGB — Verletzung von Privatgeheimnissen**
> „Wer unbefugt ein fremdes Geheimnis, namentlich ein zum persönlichen Lebensbereich gehörendes Geheimnis oder ein Betriebs- oder Geschäftsgeheimnis, offenbart, das ihm als Rechtsanwalt [...] anvertraut worden ist oder sonst bekanntgeworden ist, wird mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe bestraft."

**§ 43a Abs. 4 BRAO — Verbot der Wahrnehmung widerstreitender Interessen**
> „Der Rechtsanwalt darf keine widerstreitenden Interessen vertreten."

Dieser Skill führt **keine** Interessenkonfliktprüfung durch. Die Konfliktprüfung obliegt dem Anwalt vor jeder Mandatsannahme. Der Skill stellt lediglich sicher, dass Mandatsinhalte technisch getrennt bleiben.

**§ 53 StPO — Zeugnisverweigerungsrecht des Rechtsanwalts**
> Dem Rechtsanwalt steht ein Zeugnisverweigerungsrecht zu über das zu, was ihm in dieser Eigenschaft anvertraut oder bekanntgeworden ist.

**§§ 1 ff. GwG — Geldwäscheprävention / Mandantenidentifizierung**
Bei M&A-Mandaten (Kauf/Verkauf von Unternehmen) gilt der Rechtsanwalt als Verpflichteter i.S.d. § 2 Abs. 1 Nr. 10 GwG. Pflichten: Identifizierung des Mandanten (§ 10 GwG), Feststellung wirtschaftlich Berechtigter (§ 11 GwG), Dokumentation (§ 8 GwG).

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Leitsatz / Relevanz |
|---|---|---|---|
| BGH | IX ZR 199/14 | NJW 2015, 3239 | Anwaltliche Verschwiegenheitspflicht; Schadensersatz nach § 280 Abs. 1 BGB bei schuldhafter Verletzung durch den Anwalt |
| BGH | IX ZR 280/14 | NJW 2016, 317 | Interessenkonflikt; fristlose Kündigung des Mandatsvertrags bei Pflichtenkollision; Schadensersatz des Mandanten |
| BGH | IX ZR 221/15 | NJW 2017, 2835 | Umfang der Verschwiegenheitspflicht bei Kanzleiwechsel; Weitergabe von Mandatsinhalten an neue Kanzlei unzulässig |
| BVerfG | 1 BvR 2241/16 | NJW 2018, 2392 | Beschlagnahmeverbot für Handakten des Rechtsanwalts (§ 97 StPO); Schutzbereich der Verschwiegenheitspflicht |
| OLG München | 15 U 3248/19 | NJW-RR 2020, 638 | Schadensersatz wegen Verletzung des Interessenkonfliktverbots; Mandant kann Herausgabe von Vorteilen verlangen |

## Prüfschema: Mandats-Workspace


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Praxisprofil lesen | `## Mandats-Workspaces` in CLAUDE.md: Aktiviert oder deaktiviert? | Deaktiviert bei In-house-Juristen (Standard); nur aktivieren bei Mehrfachmandatskanzlei |
| 2 | Unterbefehl identifizieren | Ersten Token auswerten: neu / liste / wechseln / schließen / keine? | Routing zu Schritt 3–7 |
| 3 | Slug-Eindeutigkeit | Slug bereits in `mandate/<slug>/` oder `mandate/_archiv/<slug>` vorhanden? | Bei Duplikat: anderen Slug vorschlagen (Mandant + Typ + Jahr) |
| 4 | Interessenkonfliktprüfung | Durch Anwalt: Gegenpartei gleichzeitig Mandant in anderem Mandat? | Skill führt keine Prüfung durch; Hinweis und Bestätigungsabfrage |
| 5 | GwG-Identifizierung | Bei M&A-Mandat: Mandantenidentifizierung (§ 10 GwG) dokumentiert? | Hinweis auf GwG-Pflichten bei Mandatsanlage |
| 6 | Aufnahme-Interview | Alle Pflichtfelder erfasst (Mandant, Gegenpartei, Typ, Phase, Vertraulichkeit, Fakten, Abweichungen)? | Vollständige mandat.md generierbar |
| 7 | Dateierstellung | mandat.md + verlauf.md + notizen.md angelegt? Pfad korrekt? | Workspace operationsbereit |
| 8 | Aktives-Mandat-Zuweisung | Soll nach Anlage direkt gewechselt werden? | Nur auf ausdrückliche Anfrage; niemals automatisch |
| 9 | Mandatsübergreifender Kontext | CLAUDE.md-Schalter auf `aus`? | Wenn auf `an`: Warnung bei erhöhter Vertraulichkeit; Einzelgenehmigung verlangen |
| 10 | Wechsel bestätigen | Inhalt der neuen mandat.md zusammengefasst anzeigen? | Verwechslungsschutz bei vielen parallelen Mandaten |
| 11 | Schließung archivieren | Bei Schließen: `mandate/<slug>/` → `mandate/_archiv/<slug>/`; Schließungsdatum in verlauf.md? | Archivierte Mandate für Konfliktprüfungen dauerhaft lesbar |
| 12 | Nachpflege | Transaktionsphase nach Fortschritt aktualisieren (z.B. von Due Diligence → SPA-Verhandlung)? | Kontext bleibt aktuell für alle nachgelagerten Skills |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Verschwiegenheitspflichtverletzung durch RA | Mandant als Kläger (§ 280 Abs. 1 BGB) | Nachweis: Was wurde offenbart, wann, an wen, welcher Schaden? |
| Kein Interessenkonflikt | Rechtsanwalt (§ 43a Abs. 4 BRAO) | RA muss belegen, dass keine widerstreitenden Interessen bestanden |
| GwG-Identifizierungspflicht erfüllt | Rechtsanwalt (§ 8 GwG: Dokumentationspflicht) | Kopien der Identifizierungsunterlagen und Dokumentation im Mandat |
| Mandatsbeendigung | Derjenige, der sich auf die Beendigung beruft | Schriftliche Kündigung oder Mandatsbeendigungs-Protokoll |
| Interessenkonflikt-Kündigung rechtmäßig | Rechtsanwalt | Nachweis der Kollisionslage; Hinweis an Mandant nach § 627 BGB |

## Fristen und Verjährung

| Frist / Aufbewahrung | Norm | Inhalt | Folge bei Versäumnis |
|---|---|---|---|
| Aufbewahrung Handakten | § 50 BRAO | Mind. 6 Jahre nach Mandatsbeendigung | Disziplinarrechtliche Konsequenzen; Beweisschwierigkeiten |
| Verjährung anwaltliche Pflichtverletzung | §§ 195, 199 BGB | 3 Jahre ab Kenntnis; max. 10 Jahre ab Entstehung | Mandant verliert Schadensersatzanspruch |
| GwG-Dokumentation | § 8 Abs. 4 GwG | 5 Jahre nach Ende der Geschäftsbeziehung | Bußgeld §§ 56 f. GwG |
| Mandatskündigung (fristlos wegen Interessenkonflikt) | §§ 626 f. BGB | Unverzüglich nach Kenntnis der Kollisionslage | Schadensersatzpflicht wenn Frist versäumt |
| Herausgabe Handakten nach Mandatsende | § 50 Abs. 2 BRAO | Auf Verlangen des Mandanten; angemessene Frist | Schadensersatz; Disziplinarverfahren |

## Typische Gegenargumente

| Einwand | Begründung Gegenseite | Erwiderung |
|---|---|---|
| Mandatsworkspace für In-house-Juristen unnötig | In-house-Jurist arbeitet nur für einen Mandanten (das eigene Unternehmen) | Richtig — Skill bei In-house-Standard deaktiviert; nur bei tatsächlichem Mehrfachmandatsverhältnis aktivieren |
| Mandatsinformationen können zusammengefasst werden | Effizienzgewinn bei mandatsübergreifendem Vergleich | § 43a Abs. 2 BRAO gilt für jedes einzelne Mandat; mandatsübergreifende Auswertung nur mit ausdrücklicher Erlaubnis jedes Mandanten |
| Interessenkonfliktprüfung übertrieben | Kein Interessenkonflikt bei reinen Transaktionsmandaten | § 43a Abs. 4 BRAO ist streng; bereits latente Interessenkollision begründet Pflicht zur Niederlegung (BGH IX ZR 280/14) |
| Digitale Trennung nicht ausreichend | Mandatsinhalte sind ohnehin in unterschiedlichen Softwaresystemen gespeichert | Verschwiegenheitspflicht gilt auch für KI-gestütztes Drafting und Kontextverarbeitung; mandatsübergreifender Kontext-Schalter muss bewusst gesetzt werden |
| Slug-System zu komplex | Einfachere Identifikation reicht | Slug-Eindeutigkeit ist zentral für fehlerfreies Routing; klares Muster (Mandant-Typ-Jahr) verhindert Verwechslungen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Gesellschaftsrechtlichen Mandats-Workspace aufbauen | Arbeitsbereich nach Schema; Template unten |
| Variante A — Mandat nur punktuell Einzelfrage | Verkuerzte Dokumentation; nur relevante Teile des Templates |
| Variante B — Internationales Gesellschaftsrecht noetig | Common-Law-Kompass Skill parallel einsetzen |
| Variante C — M-and-A-Transaktion laeuft parallel | M-and-A-Skill parallel; Arbeitsbereich entsprechend erweitern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Mandatsniederlegungsschreiben bei Interessenkonflikt

```
An [Mandant]
[Anschrift]

[Ort, Datum]

Mandatsniederlegung — Az. [Aktenzeichen]

Sehr geehrte/r [Name],

wir haben in der oben bezeichneten Angelegenheit Ihre Interessen vertreten. Im Verlauf
unserer Mandatsbearbeitung haben wir festgestellt, dass eine Pflichtenkollision im
Sinne des § 43a Abs. 4 BRAO vorliegt, die es uns nicht gestattet, das Mandat weiter zu
führen.

Wir legen das Mandat hiermit mit sofortiger Wirkung nieder. Diese Entscheidung basiert
ausschließlich auf unserer berufsrechtlichen Verpflichtung und stellt kein Werturteil
über Ihre Rechtssache dar.

Wir empfehlen Ihnen dringend, unverzüglich eine andere Kanzlei zu beauftragen.
Zur Sicherung Ihrer Rechte weisen wir auf folgende laufende Fristen hin:
- [Frist 1: z.B. Anfechtungsfrist § 246 AktG: [Datum]]
- [Frist 2: ...]

Ihre Handakten werden wir Ihnen auf Anforderung gemäß § 50 Abs. 2 BRAO unverzüglich
herausgeben.

Mit freundlichen Grüßen
[Kanzlei / Name]
Rechtsanwalt / Rechtsanwältin
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


### Baustein 2: Mandats-Workspace-Vorlage (mandat.md)

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — je nach Nutzerprofil aus CLAUDE.md]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]
**Transaktionsphase:** [NDA | LOI | Due Diligence | SPA-Verhandlung | Signing/Closing | Post-Closing | Laufend]

---

## Parteien

**Mandant:** [Name; Rechtsform; HR-Nummer falls relevant]
**Gegenpartei:** [Name(n); ggf. Rechtsform]

## Mandatstyp

[M&A Käuferseite / M&A Verkäuferseite / Finanzierung / Governance / Reorganisation / Integration / Sonstige]
[Ein-Satz-Begründung: Warum dieser Typ?]

## Wesentliche Fakten

[2–5 Sätze: Worum geht es? Wer sind die Stakeholder? Was steht auf dem Spiel?
Was macht dieses Mandat vom Standardprofil abweichend?]

## Mandatsspezifische Abweichungen vom Praxisprofil

*Jede Abweichung vom Kanzlei-Standard auf Mandatsebene — gilt nur für dieses Mandat.*

- [z.B. „Haftungsdeckelung: Mandant besteht auf 24 Monaten statt Hausstandard 12 Monate."]
- [z.B. „Ton: beziehungspflegend — Gegenpartei ist strategischer Partner."]
- [z.B. „Anwendbares Recht: Deutsches Recht zwingend, kein englisches Recht."]

## GwG-Compliance (§§ 1 ff. GwG)

- [ ] Mandantenidentifizierung durchgeführt (§ 10 GwG)
- [ ] Wirtschaftlich Berechtigte ermittelt (§ 11 GwG)
- [ ] Dokumentation angelegt (§ 8 GwG; Aufbewahrung 5 Jahre nach Ende der Geschäftsbeziehung)

## Verbundene Mandate

- [slug — ein Satz, warum verbunden; z.B. „NDA-Phase vorgelagerter Rechtsauftrag"]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf Mandatsunterlagen
einsehen? Ist mandatsübergreifender Kontext für dieses Mandat unzulässig?]
```

### Baustein 3: Verlaufsdatei-Vorlage (verlauf.md)

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Nur-Anhängen-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Ggf. anfänglicher Kontext — z.B. „Eröffnet auf Eingang eines SPA-Entwurfs von [Gegenpartei]."]

---

## [JJJJ-MM-TT] — Transaktionsphase gewechselt

Von [Phase A] zu [Phase B]. Anlass: [Ereignis, z.B. „LOI unterzeichnet"].

---

## [JJJJ-MM-TT] — Mandat geschlossen

Abschlussdatum: [JJJJ-MM-TT]. Anlass: [Abschluss der Transaktion / Mandatsniederlegung
/ Wunsch des Mandanten]. Archiviert unter `mandate/_archiv/[slug]/`.
```

## Unterbefehle: Vollständige Beschreibung

### `neu <slug>`

1. Slug prüfen: nicht bereits in `mandate/<slug>/` oder `mandate/_archiv/<slug>/` vorhanden. Falls wiederverwendet: anderen Slug vorschlagen.
2. Aufnahme-Interview nach Kaltstart-Rückfragen durchführen.
3. `mandate/<slug>/mandat.md` anhand der Vorlage schreiben.
4. `mandate/<slug>/verlauf.md` mit Eintrag „Eröffnet" anlegen.
5. Leere `mandate/<slug>/notizen.md` erstellen.
6. Nicht automatisch wechseln. Fragen: „Möchten Sie jetzt zu `<slug>` wechseln?"

### `liste`

`mandate/*/mandat.md` aufzählen. Jede Datei lesen, Status extrahieren. Tabelle ausgeben:

| Slug | Mandant | Mandatstyp | Phase | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. Archiv unter separater Überschrift.

### `wechseln <slug>`

1. `mandate/<slug>/mandat.md` auf Existenz prüfen.
2. `Aktives Mandat:`-Zeile in CLAUDE.md auf Praxisebene auf `Aktives Mandat: <slug>` ändern.
3. Inhalt von `mandat.md` zusammenfassen zur Bestätigung.

### `schließen <slug>`

1. `mandate/<slug>/` auf Existenz prüfen.
2. Eintrag „Geschlossen" mit heutigem Datum an `verlauf.md` anhängen.
3. `mandate/<slug>/` → `mandate/_archiv/<slug>/` verschieben.
4. War das geschlossene Mandat das aktive: `Aktives Mandat:` auf `keine — nur Praxiskontextdaten` setzen.

### `keine`

`Aktives Mandat:` in CLAUDE.md auf `keine — nur Praxiskontextdaten` setzen. Mit Nutzer bestätigen.

## Mandatsübergreifender Kontext

CLAUDE.md auf Praxisebene enthält einen `Mandatsübergreifender Kontext:`-Schalter.

**Wenn `aus` (Standard):** Ein Skill, der in Mandat A arbeitet, liest niemals Dateien in `mandate/B/`. Dies ist die Vertraulichkeitsgarantie.

**Wenn `an`:** Ein Skill darf Mandatsdaten mandatsübergreifend nur dann lesen, wenn der Nutzer dies ausdrücklich verlangt (z.B. „Vergleiche die Haftungsbegrenzungen in den letzten fünf Vendor-Mandaten"). Auch bei `an` ist der Standard: nur das aktive Mandat laden, außer bei ausdrücklicher Vergleichsanfrage.

**Bei erhöhter Vertraulichkeit:** Auch wenn der globale Schalter auf `an` steht, gilt für Mandate mit `Vertraulichkeit: erhöht` oder `clean-team`: mandatsübergreifender Kontext nur nach Einzelgenehmigung des Anwalts.

## Hinweise und Risiken

| Risiko | Beschreibung | Abhilfe |
|---|---|---|
| Mandatsübergreifender Kontext bei sensiblem Mandat | Vertrauliche Informationen eines Mandanten fließen in ein anderes Mandat | Schalter auf `aus` halten; bei erhöhter Vertraulichkeit in mandat.md explizit sperren |
| Slug-Verwechslungen | Ähnliche Slug-Namen führen zu falscher Mandatszuweisung | Klares Muster: `[mandant]-[typ]-[jahr]`; z.B. `alpha-gmbh-anteilskauf-2026` |
| Interessenkonflikt nicht erkannt | RA vertritt gleichzeitig Käufer und Verkäufer in derselben Transaktion | Vor Mandatsanlage Konfliktprüfung in Kanzlei-System; Skill kann nicht ersetzen |
| GwG-Identifizierung fehlt | Bußgeld; strafrechtliches Risiko für RA | GwG-Checkliste in mandat.md pflichtmäßig abhaken |
| In-house-Jurist aktiviert Workspaces | Unnötige Komplexität; fehlende Mandantentrennung irrelevant | Bei In-house-Standard deaktiviert; erst bei tatsächlichem Mehrfachmandatsverhältnis aktivieren |

## Beispiel: M&A-Käuferseite

**Szenario:** Sozietät begleitet GmbH-Anteilskauf. Neues Mandat angelegt:
- Slug: `alpha-gmbh-anteilskauf-2026`
- Mandatstyp: M&A Käuferseite
- Phase: Due Diligence
- Vertraulichkeit: erhöht (Clean-Team)
- Verbundene Mandate: `alpha-gmbh-nda-2025` (NDA-Phase), `alpha-gmbh-loi-2025` (LOI-Phase)

Fortschritt: Nach Signing → Mandat-Phase aktualisiert auf `Signing/Closing`. Nach Closing → Phase `Post-Closing-Integration`. Nach Abschluss: `schließen alpha-gmbh-anteilskauf-2026` archiviert das Mandat dauerhaft.

## Output-Template

**Adressat:** Bearbeitender Anwalt / Kanzlei-intern — Tonfall: sachlich-strukturiert, mandatsbezogen

```
--- mandat.md: [SLUG] ---
Mandantscode: [CODE]
Mandant: [NAME DER PARTEI]
Gegenseite: [NAME]
Mandat-Typ: [M&A Kaeuferseite / Gruendung / Strukturierung / Streit]
Phase: [NDA / LOI / Due Diligence / Signing / Closing / Post-Closing]
Vertraulichkeit: [Standard / erhoeht / Clean-Team]
Mandatstraeger: [NAME RECHTSANWALT]
Eroeffnet: [TT.MM.JJJJ]
Geschaeftswert: [BETRAG EUR / noch nicht feststellbar]
Gesellschaft(en): [NAME GmbH, HRB XXXXX, AG [REGISTERGERICHT]]

Verbundene Mandate:
- [SLUG-NDA] (NDA-Phase)
- [SLUG-LOI] (LOI-Phase)

Fristen:
- [TT.MM.JJJJ]: [FRISTBEZEICHNUNG] — Wiedervorlage [TT.MM.JJJJ]
- [TT.MM.JJJJ]: [FRISTBEZEICHNUNG] — kritisch

GwG-Identifizierung: [ABGESCHLOSSEN TT.MM.JJJJ / AUSSTEHEND]
Interessenkonflikt geprueeft: [JA / NEIN — NACHOLEN]

Memo zum Mandatsstand (letzte Aktualisierung [DATUM]):
[FREITEXT: aktueller Bearbeitungsstand, offene Punkte, naechste Schritte]

Aktive Arbeitsbereiche:
- mandate/[SLUG]/dd/ (Due-Diligence-Unterlagen)
- mandate/[SLUG]/vertrag/ (Vertragsentwuerfe)
- mandate/[SLUG]/korrespondenz/ (Schriftwechsel)

Abgeschlossen: [NEIN / JA — TT.MM.JJJJ; archiviert]
---
```

## Rote Schwellen

- **GwG-Identifizierung fehlt** — strafrechtliches Risiko fuer Rechtsanwalt (§§ 10 ff. GwG); vor Weiterarbeit nachholen.
- **Interessenkonflikt nicht geprueft** — Verstoß gegen § 43a Abs. 4 BRAO; Mandat unverzueglich auf Konflikt pruefen.
- **Anwaltliche Verschwiegenheit: Dateien aus anderem Mandat im Workspace** — § 43a Abs. 2 BRAO, § 203 StGB; sofort entfernen; Fehler dokumentieren.
- **Handakten-Aufbewahrungsfrist § 50 BRAO** — mind. 5 Jahre nach Mandat-Abschluss; Loeschung erst nach Ablauf.
- **Frist im Mandat ohne Wiedervorlage** — Haftungsrisiko; jede Frist sofort im Kalender mit Vorlauf-WV verankern.

## Anschluss-Skills

- `gesellschaftsrecht:vollzugs-checkliste` — Vollzugs-Checkliste für das aktive M&A-Mandat
- `gesellschaftsrecht:gesellschafts-compliance` — Compliance-Tracker für Gesellschaften im aktiven Mandat
- `gesellschaftsrecht:aufsichtsrat-protokoll` — Sitzungsprotokolle für das aktive Mandat
- `gesellschaftsrecht:tabellenpruefung` — Tabellenprüfung im Kontext des aktiven Mandats

## Quellen und Zitierweise

- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht)
- § 43a Abs. 4 BRAO (Verbot widerstreitender Interessen)
- § 203 Abs. 1 Nr. 3 StGB (Verletzung von Privatgeheimnissen)
- § 50 BRAO (Handakten; Aufbewahrungspflicht)
- §§ 1 ff. GwG (Geldwäscheprävention; Mandantenidentifizierung)
- §§ 195, 199 BGB (Verjährung)

Zitierweise nach `../../references/zitierweise.md`.

Kommentarliteratur:
- Roth/Altmeppen, GmbHG, 11. Aufl. 2024, Einl. Rn. 15 ff. (Mandatsverhältnis im Gesellschaftsrecht).
- Baumbach/Hopt, HGB, 41. Aufl. 2024, Einl. vor § 1 Rn. 10 ff. (Berufsrecht der rechtsberatenden Berufe).
- BGH, Urt. v. 25.06.2015 – IX ZR 199/14, NJW 2015, 3239 Rn. 18 (Anwaltliche Verschwiegenheitspflicht).
- BGH, Urt. v. 17.09.2015 – IX ZR 280/14, NJW 2016, 317 Rn. 20 (Interessenkonflikt; Kündigung des Mandats).

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall und keine Interessenkonfliktprüfung.
