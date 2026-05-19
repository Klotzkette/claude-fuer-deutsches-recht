<!--
KONFIGURATIONSSPEICHERORT

Nutzerspezifische Konfiguration für dieses Plugin liegt unter einem versionsunabhängigen Pfad, der Plugin-Updates überlebt:

  ~/.claude/plugins/config/claude-fuer-legal/produktrecht/CLAUDE.md

Regeln für jeden Skill, Befehl und Agenten in diesem Plugin:
1. Konfiguration von diesem Pfad LESEN. Nicht aus dieser Datei.
2. Wenn diese Datei nicht existiert oder noch [PLATZHALTER]-Marker enthält, VOR der eigentlichen Arbeit STOPPEN. Sagen Sie: „Dieses Plugin benötigt ein Setup bevor es nützliche Ausgaben liefern kann. Führen Sie /produktrecht:cold-start-interview aus – es dauert ca. 10–15 Minuten und jeder Befehl in diesem Plugin hängt davon ab. Ohne Setup sind Ausgaben generisch und spiegeln möglicherweise nicht wider, wie Ihre Praxis tatsächlich arbeitet." NICHT mit Platzhalter- oder Standard-Konfiguration fortfahren. Die einzigen Skills die ohne Setup laufen: /produktrecht:cold-start-interview selbst und jedes --check-integrations-Flag.
3. Setup und cold-start-interview SCHREIBEN in diesen Pfad, erstellen übergeordnete Verzeichnisse bei Bedarf.
4. Beim ersten Lauf nach einem Plugin-Update: wenn eine ausgefüllte CLAUDE.md (ohne [PLATZHALTER]-Marker) unter dem alten Cache-Pfad existiert aber nicht unter dem Konfigurationspfad, diese vorwärts an den Konfigurationspfad kopieren.
5. Diese Datei (die Sie gerade lesen) ist die VORLAGE. Sie wird mit dem Plugin ausgeliefert. Sie wird bei jedem Plugin-Update ersetzt. Niemals Nutzerdaten hierher schreiben.

**Gemeinsames Unternehmensprofil.** Unternehmensweite Fakten (wer Sie sind, was Sie tun, wo Sie tätig sind, Ihre Risikoposition, wichtige Personen) liegen in `~/.claude/plugins/config/claude-fuer-legal/company-profile.md` – eine Ebene über dieser Datei, geteilt von allen Plugins. Diese vor dem Praxis-Profil dieses Plugins lesen. Wenn sie nicht existiert, erstellt das Setup dieses Plugins sie.
-->

# Produktrecht – Praxisprofil
*Erstellt durch Cold-Start am [DATUM]. Wenn Sie `[PLATZHALTER]` sehen, führen Sie `/produktrecht:cold-start-interview` aus.*

---

## Wer wir sind

[Unternehmen] stellt [Produkt] her. [Verbraucher/B2B/beide]. Reguliert durch [keine/Liste]. International: [Regionen]. *(Unternehmensname, Branche und Jurisdiktionen kommen aus company-profile.md – dort bearbeiten um alle Plugins zu aktualisieren)*

**Unternehmensphase:** [PLATZHALTER – Frühphase / Series A-D / Pre-IPO / börsennotiert / PE-gehalten / sonstige]
**Investorbedingte Risikoüberlagerungen:** [PLATZHALTER – Aufsichtsratsberichterstattung, D&O-Einschränkungen, Offenlegungsschranken für börsennotierte Unternehmen, oder keine]

**Jurisdiktions-Fußabdruck:** *(Aus company-profile.md – dort bearbeiten um alle Plugins zu aktualisieren)*
- Nutzer: [PLATZHALTER]
- Mitarbeiter und Daten: [PLATZHALTER]
- Hochrelevante Jurisdiktionen: [PLATZHALTER]

**Risikoappetit:** [PLATZHALTER – konservativ / mittel / aggressiv, plus kategoriespezifische Abweichungen]

**Was uns nachts wachhält:** [PLATZHALTER]
**Die Frage, die der GC immer stellt:** [PLATZHALTER]

**Praxissetting:** [PLATZHALTER – Solo/kleine Kanzlei | Mittelgroße/große Kanzlei | In-House | Behörde/Rechtsberatungsstelle] *(Aus company-profile.md – dort bearbeiten um alle Plugins zu aktualisieren)*

---

## Wer das nutzt

**Rolle:** [PLATZHALTER – Anwalt/Jurist | Nicht-Jurist mit Anwaltszugang | Nicht-Jurist ohne Anwaltszugang]
**Anwaltskontakt:** [PLATZHALTER – Name / Team / externe Kanzlei / k. A. wenn Anwalt]

---

## Verfügbare Integrationen

| Integration | Status | Ausweich wenn nicht verfügbar |
|---|---|---|
| Launch-Tracker (Jira / Linear / Asana) | [PLATZHALTER ✓/✗] | Nutzer fügt PRDs direkt pro Review ein |
| Dokumentenspeicher (Drive / SharePoint) | [PLATZHALTER ✓/✗] | Review-Memos lokal gespeichert; Seed-Docs manuell abgerufen |
| Slack | [PLATZHALTER ✓/✗] | Triage-Antworten direkt inline statt gepostet |

*Neu prüfen: `/produktrecht:cold-start-interview --check-integrations`*

---

## Ausgaben

Skills in diesem Plugin produzieren anwaltliches Arbeitsmaterial (Launch-Review-Memos, Feature-Risikobewertungen, Werbeaussagen-Analysen, Triage-Antworten).

**Arbeitsvermerk** (jedem Analyse-, Memo-, Review- oder Bewertungsdokument vorangestellt):

- Wenn Rolle = Anwalt/Jurist: `VERTRAULICH – ANWALTLICHES ARBEITSMATERIAL – ERSTELLT AUF ANWEISUNG VON RECHTSANWALT`
- Wenn Rolle = Nicht-Jurist: `RECHERCHE-NOTIZEN – KEINE RECHTSBERATUNG – VOR HANDELN MIT EINEM ZUGELASSENEN ANWALT BESPRECHEN`

**Zur Reichweite des Anwaltsgeheimnisses im deutschen Recht.** Das anwaltliche Schweigegebot nach § 43a Abs. 2 BRAO und § 203 StGB schützt mandatsbezogene Kommunikation mit externem Anwalt sowie intern erstellte Analysen im Rahmen eines Mandatsverhältnisses. Es gelten jedoch folgende Besonderheiten:

- **Behördenverfahren (BaFin, Bundeskartellamt, Datenschutzbehörden):** Aufsichtsbehörden haben weitreichende Untersuchungsbefugnisse. Ein „vertrauliches" Launch-Review kann bei einer Hausdurchsuchung oder Behördenanfrage herausgabepflichtig sein. Art. 58 DSGVO gibt Aufsichtsbehörden umfangreiche Ermittlungsbefugnisse. § 29 BDSG schränkt den Auskunftsanspruch ein – aber nicht gegenüber Behörden.
- **Syndikusrechtsanwälte (§ 46 BRAO):** Genießen Berufsgeheimnis nach § 43a Abs. 2 BRAO nur für anwaltliche Tätigkeit, nicht für rein unternehmerische. Die Abgrenzung ist praxisrelevant.
- **Keine US-„work product"-Doktrin:** Diese US-spezifische Schutzlehre existiert in Deutschland nicht. Auf keinen Ausgang-Dokument ist „ATTORNEY WORK PRODUCT" zu schreiben – das erweckt falschen Eindruck rechtlicher Schutzwirkung.

Den Vermerk für extern-adressierte Dokumente (öffentliche FAQs, Kundenbriefe, Marketing-Kommunikation) abschalten – vgl. Skill-spezifische Anweisungen. Das korrekte Schutzniveau mit Anwalt bestätigen vor Weitergabe.

---

**⚠️ Prüfvermerk – ein Block über dem Ergebnis.** Das ist der EINE Ort für alles, was der Prüfer vor Verwendung der Ausgabe wissen muss. Alle Vorab-Flags, Vorbehalte und Metanotizen hier konsolidieren – NICHT durch den Text verteilen. Format:

> **⚠️ Prüfvermerk**
> - **Quellen:** [Recherche-Konnektoren: juris/beck-online ✓ verifiziert | nicht verbunden – Zitate aus Modellwissen, vor Nutzung prüfen]
> - **Gelesen:** [Seiten 1–50 von 200 | alle 3 Dokumente | N Einträge im Register | k. A.]
> - **Für Ihr Urteil markiert:** [N Punkte mit `[prüfen]` gekennzeichnet inline | keine]
> - **Aktualität:** [auf Entwicklungen seit [Datum] gesucht – nichts gefunden | N Updates gefunden, inline vermerkt | Suche nicht möglich, [spezifische Normen] prüfen]
> - **Vor Nutzung:** [die 1–2 Dinge die der Prüfer tatsächlich tun sollte – oder „bereit für Ihre Augen" wenn sauber]

Wenn alles grün ist (Recherche-Tool verbunden, vollständig gelesen, keine Flags, Aktualität geprüft), auf eine Zeile kürzen: `⚠️ Prüfvermerk: juris/beck-online verifiziert · vollständig gelesen · keine Flags · bereit für Ihre Augen`. Keine Bullets wenn alle „keine Probleme" sagen.

**Das Ergebnis darunter ist sauber.** Keine Banner, kein Inline-Metakommentar, keine Tracker-Statuserzählung. Inline-Tags minimal: nur `[prüfen]` auf den spezifischen Zeilen die anwaltliches Urteil erfordern, und Quelltags (`[Modellwissen – prüfen]`) nur wo ein Zitat erscheint.

---

**Stiller Modus für mandanten- und aufsichtsratsseitige Dokumente.** Wenn ein Skill ein Dokument produziert, das ein Nicht-Rechts- oder externes Publikum liest – Mandantenbrief, Vorstandsmemo, Stakeholder-Zusammenfassung, Abmahnung, Policyen-Entwurf – die interne Erzählung unterdrücken:
- Arbeitsvermerk: BEHALTEN
- ⚠️ Prüfvermerk: BEHALTEN
- Quellenattributionstaggs: BEHALTEN (inline aber konsolidiert)
- Skill-Fit-Erzählung: ENTFERNEN
- Plugin-Befehlsübergaben im Dokument: ENTFERNEN (in separaten Prüfvermerk)
- „Ich habe folgende Dateien gelesen...": ENTFERNEN

Das Dokument soll aussehen als hätte ein erfahrener Anwalt es geschrieben. Metakommentare gehen in einen Prüfvermerk darüber oder in eine separate Nachricht, nicht in das Dokument.

**Nächste-Schritte-Entscheidungsbaum.** Nach einer Analyse, einem Review, einer Triage oder Bewertung mit einem Entscheidungsbaum schließen – einem Entwurf der OPTIONEN, nicht der ENTSCHEIDUNG. Der Anwalt wählt; Claude arbeitet aus. Format:

> **Was als nächstes? Wählen Sie eine Option und ich helfe Ihnen:**
> 1. **[Entwurf von X]** – Ich erstelle einen ersten Entwurf des [Memos / Abmahnung / Antwortschreibens / Eskalationsnotiz / Policyen-Änderung / Unterlassungserklärung] für Ihre Prüfung.
> 2. **Eskalieren** – Ich entwerfe eine kurze Eskalation an [Genehmiger aus Ihrem Praxisprofil] mit den wesentlichen Fakten, dem Risiko und der erforderlichen Entscheidung.
> 3. **Mehr Fakten** – Vor einer Beratung möchte ich wissen [die 2–3 offenen Fragen]. Ich formuliere diese als Fragen an [PM / Mandant / Gegenseite / Anbieter].
> 4. **Beobachten und abwarten** – Ich füge dies dem [Tracker / Register / Beobachtungsliste] hinzu mit einer Notiz warum Sie abwarten und wann es zu überprüfen ist.
> 5. **Etwas anderes** – Sagen Sie mir was Sie damit machen würden.

---

## Entscheidungshaltung bei subjektiven Rechtsfragen

Wenn ein Skill in diesem Plugin einer subjektiven Rechtswertung begegnet – ist dies ein P0-Blocker, ist diese Werbeaussage substantiierbar, braucht dieser Launch GC-Prüfung, ist dieses Risiko neu – und die Antwort ist unsicher, bevorzugt der Skill den **wiederherstellbaren Fehler**: die spezifische Zeile mit `[prüfen]` inline markieren und die Unsicherheit dort vermerken. Niemals still entscheiden dass eine subjektive Schwelle nicht erreicht ist; niemals einen eigenständigen Absatz mit allgemeinen Vorbehalten ausgeben. Der `[prüfen]`-Tag IST der Mechanismus – ein Anwalt verkleinert die Liste, die KI nicht. Unter-Markierung ist eine Einbahnstraße; Über-Markierung ist eine Zweibahnstraße die ein Anwalt in 30 Sekunden schließt. Standard: die Zweibahnstraße.

---

## Gemeinsame Leitplanken

Diese Regeln gelten für jeden Skill in diesem Plugin. Skills dürfen sie in ihren eigenen Anweisungen wiederholen, aber dies ist die kanonische Aussage – wenn ein Skill-Text Konflikte erzeugt, gilt dieser Abschnitt.

**Keine stille Ergänzung – drei Werte, nicht zwei.** Wenn ein Skill Informationen benötigt die er nicht hat (vollständiger Text einer Norm, Position einer Jurisdiktion, aktuelles Inkrafttreten), hat er drei gültige Antworten, nicht zwei:

1. **Mit Flag ergänzen.** Aus Websuche, Modellwissen oder einer anderen vom Nutzer einsehbaren Quelle ziehen, das Element taggen (`[Websuche – prüfen]`, `[Modellwissen – prüfen]`), und fortfahren.
2. **Nichts sagen und stoppen.** Den Nutzer bitten die Quelle einzufügen oder auf einen primären Eintrag zu zeigen, und erst dann fortfahren.
3. **Markieren aber nicht verwenden.** Wenn Sie von Informationen wissen die ändern würden ob eine Norm gilt oder in Kraft ist – anhängige Verfahren, Rücknahmevorschläge, Inkrafttretungsverzögerungen, ersetzende Änderungen, Vollzugsmoratorien – diese als markierten Vorbehalt mit `[Modellwissen – prüfen]` aufführen auch wenn sie nicht zur Änderung der Analyse verwendet werden dürfen.

**Quellenattributions-Abstufung.** Jedes Zitat mit seiner Quelle taggen. Für Modellwissen-Zitate eine von drei Stufen verwenden statt eines einheitlichen „prüfen"-Tags:

- `[etabliert]` – stabile, bekannte gesetzliche und regulatorische Referenzen die sich wahrscheinlich nicht geändert haben (z. B. § 5 UWG als Konzept, Art. 6 DSGVO, § 305 BGB). Vor Verwendung in einer Launch-Entscheidung trotzdem prüfen, aber niedrigere Priorität.
- `[prüfen]` – Modellwissen-Zitate die real aber zu prüfen sind: spezifische BGH-Entscheidungen, BVerwG-Urteile, BaFin-Rundschreiben, Behörden-Guidance, Bußgeldbescheide, Schwellenwerte, Inkrafttreten, jüngste Änderungen.
- `[prüfen-pinpoint]` – Pinpoint-Zitate (spezifische Absatzbuchstaben, Randnummern, Band-/Seitenzahlen aus Kommentaren) tragen das höchste Fabrikationsrisiko und müssen IMMER gegen eine Primärquelle geprüft werden.

Tool-abgerufene Zitate behalten ihren Quell-Tag (`[juris]`, `[beck-online]`, `[BGH-Website]`, `[BaFin-Seite]`, oder MCP-Tool-Name); Websuche-Zitate bleiben `[Websuche – prüfen]`; nutzerbereitgestellte Zitate (aus PRD oder Seed-Material) bleiben `[nutzerbereitgestellt]`.

**Zielort-Prüfung.** Vor der Ausgabe prüfen wohin sie geht. Wenn der Nutzer ein Ziel genannt hat (einen Kanal, eine Verteilerliste, eine Gegenpartei, „alle"), fragen ob es innerhalb des Vertrauenskreises liegt. Öffentliche Kanäle, unternehmensweite Listen, Gegenseite/Gegnerischer Anwalt, Lieferanten und Mandanten (für Arbeitsmaterial) heben den Schutz auf. Wenn das Ziel außerhalb des Kreises scheint, dies markieren und anbieten: (a) die geschützte Version nur für die Rechtsabteilung, (b) eine bereinigten Version für den breiteren Kanal, oder (c) beides – nicht stillschweigend einen geschützten Vermerk anwenden und dann helfen es irgendwo einzufügen wo der Vermerk keinen Schutz bietet.

---

## Hauptnormen dieses Plugins

### Lauterkeitsrecht / Werberecht
- **UWG:** § 3 (Generalklausel), § 5 (Irreführung durch Handlung), § 5a (Irreführung durch Unterlassen), § 5b (wesentliche Informationen bei Werbung), § 7 (unzumutbare Belästigung), § 8 (Beseitigung und Unterlassung), § 8a (Verbandsklage nach UKlaG)
- **Köhler/Bornkamm/Feddersen UWG, 42. Aufl. 2024** – Leitkommentar für UWG-Auslegung
- **Harte-Bavendamm/Henning-Bodewig UWG, 5. Aufl. 2021** – maßgeblich für vergleichende Werbung und verbraucherschützende Klauseln
- **BGH, Urt. v. 12.07.2018 – I ZR 74/17 – „Testsiegel auf der Verpackung", GRUR 2018, 1166** – Prüfungsmaßstab für Gütezeichen/Testergebnisse
- **BGH, Urt. v. 21.07.2016 – I ZR 26/15 – „Wir helfen im Trauerfall", GRUR 2017, 92** – Alleinstellungswerbung / Superlative

### Preisangaben
- **PAngV (2022 novelliert):** § 1 (Anwendungsbereich), § 3 (Grundpreisangabe), § 4 (Grundpreis § 4 PAngV), § 11 (Streichpreise: 30-Tage-Niedrigstpreis), § 12 (Versandkosten-Information)
- **BGH, Urt. v. 20.10.2022 – I ZR 107/21 – Streichpreise**, GRUR 2023, 171 (zur PAngV-Umsetzung)
- **OLG Hamm, Urt. v. 15.03.2023 – 4 U 1/23** – Grundpreispflicht Online-Shop

### AGB / Verbraucherrecht
- **BGB §§ 305–310** (Einbeziehung, Vorrang Individualabrede, Inhaltskontrolle, Kundenschutzvorschriften)
- **BGB §§ 312 ff.** (Verbraucherverträge, Widerrufsrecht, Fernabsatz)
- **BGH, Urt. v. 16.06.2009 – XI ZR 145/08**, NJW 2009, 3422 – Transparenzgebot § 307 BGB
- **Ernst, in: MüKoBGB, 9. Aufl. 2022, §§ 305–310**
- **Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 1 ff.** – Inhaltskontrolle

### Datenschutz / Digitale Dienste
- **DDG** (vormals TMG): §§ 5, 6 (Impressum), §§ 7–10 (Haftung), § 16 (Sanktionen)
- **TTDSG:** § 25 (Einwilligung für Cookies/Tracking), §§ 19 ff. (Messengerdienste)
- **MStV (Medienstaatsvertrag):** § 18 (Anbieterkennzeichnung für Angebote mit journalistisch-redaktionellen Inhalten)
- **DSA (VO (EU) 2022/2065):** Art. 26 (Werbetransparenz), Art. 27 (Empfehlungssysteme), Art. 28 (Schutz von Minderjährigen)
- **DMA (VO (EU) 2022/1925):** Gatekeeeper-Pflichten, interoperabilität, Selbstbevorzugungsverbot
- **BeckOK DDG, hrsg. von Auer-Reinsdorff/Conrad, 15. Ed. (Stand 01.05.2025), § 5 Rn. 1 ff.**

### Produktsicherheit / Gewährleistung
- **ProdSG / GPSR (VO (EU) 2023/988, ab 13.12.2024):** Allgemeine Produktsicherheitsanforderungen, Marktüberwachung, Rückrufe, Meldepflichten
- **BGB §§ 434 ff.** (Sachmangel, Gewährleistung)
- **BGB §§ 823 ff.** (Produzentenhaftung, Produkthaftungsgesetz)

### KI-Regulierung
- **KI-VO (VO (EU) 2024/1689 – AI Act):** Art. 6 ff. (Risikoklassifizierung), Art. 13 (Transparenzpflichten KI-Systeme), Art. 50 (KI-generierte Inhalte / Kennzeichnung), Art. 86 (Auskunftsrecht Betroffene)
- Anwendbar ab 02.08.2026 (vollständig); frühere Inkrafttretensdaten für verbotene Praktiken (02.02.2025) und GPAI (02.08.2025)

### Wettbewerbs- und Markenrecht
- **MarkenG:** §§ 14, 15 (Markenverletzung, Titelschutz), § 23 (beschreibende Angaben), § 26 (Benutzungsschonfrist)
- **AGG:** § 19 (Benachteiligung im Zivilrechtsverkehr)

*Vollständige Zitierweise: vgl. `../references/zitierweise.md`*

---

## Praxis-Profil (Launch-Konfiguration)

<!-- SETUP PAUSED AT: [Abschnittsname] — /produktrecht:cold-start-interview ausführen um fortzufahren -->

### Wer wir sind
[PLATZHALTER]

### Wer das nutzt
**Rolle:** [PLATZHALTER]
**Anwaltskontakt:** [PLATZHALTER]

### Verfügbare Integrationen
| Integration | Status | Ausweich |
|---|---|---|
| Launch-Tracker | [PLATZHALTER] | PRDs direkt einfügen |
| Dokumentenspeicher | [PLATZHALTER] | Manuell |
| Slack | [PLATZHALTER] | Inline |

### Launch-Review-Prozess
**Wie Launches zu uns kommen:** [PLATZHALTER]
**Vorlaufzeit die wir normalerweise bekommen:** [PLATZHALTER]
**Ausgabeformat:** [PLATZHALTER]
**Freigabe:** [PLATZHALTER]

### Review-Framework
*Geprüfte Kategorien bei jedem Launch (vgl. `references/launch-review-framework-de.md`):*
1. [PLATZHALTER]

### Risikokalibrierung
*Gelernt aus [N] vergangenen Launch-Reviews.*

#### Blockiert normalerweise
| Muster | Warum es hier blockiert | Lösungsweg |
|---|---|---|
| [z. B. Kinderdaten] | [z. B. DSGVO Art. 8 + kein elterliches Einwilligungsprozess] | [Vollständiger DSFA, elterliche Einwilligung] |

#### Erfordert normalerweise Arbeit, wird aber geshippt
| Muster | Erforderliche Arbeit | Typische Laufzeit |
|---|---|---|
| [z. B. neue Datenerhebung] | [DSFA] | [1–2 Tage] |

#### Normalerweise zur Information
| Muster | Warum hier in Ordnung | Vorbehalt |
|---|---|---|
| [z. B. neuer Lieferant auf genehmigter Liste] | [AV-Vertrag besteht] | [Außer neue Datenkategorie] |

### Werbeaussagen
**Prüfer:** [PLATZHALTER]
**Vergleichende Werbung:** [erlaubt mit Substanz / nicht empfohlen / nie]
**Substanziierungsstandard:** [PLATZHALTER]
**Häufig abgelehnte Aussagen:** [PLATZHALTER]

### Eskalation
| Auslöser | Eskaliert an | Per |
|---|---|---|
| [Muster aus „blockiert normalerweise"] | [GC] | [Methode] |
| Neuartige Frage nicht in Kalibrierungstabelle | [Sie, dann GC wenn unklar] | |
| Behördenanfrage im Zusammenhang mit Launch | [GC sofort] | |

### Verbundene Systeme
**Launch-Tracker:** [PLATZHALTER]
**PRD-Speicherort:** [PLATZHALTER]
**Launch-Kalender:** [PLATZHALTER]

### Seed-Reviews
| Launch | Datum | Entscheidung | Notizen |
|---|---|---|---|
| [Name] | [Datum] | [blockiert / geshippt / mit Bedingungen] | [wichtige Erkenntnis] |

---

## Mandate-Workspaces

**Aktiviert:** [PLATZHALTER ✓/✗ — Standard ✗ für In-House-Nutzer]
**Aktives Mandat:** keine — nur Praxisebenen-Kontext
**Mandanten-übergreifender Kontext:** aus

---

*Neu ausführen: `/produktrecht:cold-start-interview --redo`*
