<!--
KONFIGURATIONSPFAD

Benutzerspezifische Konfiguration für dieses Plugin liegt unter einem versionsunabhängigen Pfad, der Plugin-Updates übersteht:

  ~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/CLAUDE.md

Regeln für jeden Skill, Befehl und Agenten in diesem Plugin:
1. Konfiguration von diesem Pfad LESEN. Nicht von dieser Datei.
2. Wenn diese Datei nicht existiert oder noch [PLATZHALTER]-Marker enthält, VOR substantieller Arbeit STOPPEN. Meldung: „Dieses Plugin benötigt eine Einrichtung, bevor es nützliche Ergebnisse liefern kann. Führe /gesellschaftsrecht:kaltstart-interview aus – es dauert ca. 10–15 Minuten, und jeder Befehl in diesem Plugin hängt davon ab. Ohne Einrichtung sind Ergebnisse generisch und stimmen möglicherweise nicht mit deiner tatsächlichen Praxis überein." NICHT mit Platzhalter- oder Standardkonfiguration fortfahren. Einzige Skills, die ohne Einrichtung laufen: /gesellschaftsrecht:kaltstart-interview selbst und ein --integrationen-pruefen-Flag.
3. Einrichtung und kaltstart-interview SCHREIBEN in diesen Pfad, dabei übergeordnete Verzeichnisse erstellen, wenn nötig.
4. Bei erstem Lauf nach einem Plugin-Update: wenn eine befüllte CLAUDE.md am alten Cache-Pfad vorhanden ist, aber nicht am Konfigurationspfad, diese nach vorne kopieren.
5. Diese Datei (die du gerade liest) ist die VORLAGE. Sie wird mit dem Plugin geliefert und zeigt die Struktur, die die Konfiguration haben soll. Sie wird bei jedem Plugin-Update ersetzt. Niemals Benutzerdaten hier schreiben.

**Geteiltes Unternehmensprofil.** Unternehmensebene-Fakten (wer du bist, was du tust, wo du tätig bist, deine Risikohaltung, Schlüsselpersonen) liegen unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` – eine Ebene über dieser Datei, geteilt von allen Plugins. Vor diesem Plugin-Praxisprofil lesen. Falls nicht vorhanden, erstellt die Einrichtung dieses Plugins sie.
-->

# Gesellschaftsrechtliches Praxisprofil
*Erstellt durch Kaltstart am [DATUM]. Aktive Module: [M&A | Organe & Protokoll | Börse/Kapitalmarkt | Gesellschafts-Compliance]*
*Wenn `[PLATZHALTER]`, führe `/gesellschaftsrecht:kaltstart-interview` aus.*

---

## Unternehmensprofil

**Rechtsträger-Name:** [PLATZHALTER] *(aus unternehmens-profil.md – dort bearbeiten, um über alle Plugins hinweg zu ändern)*
**Branche / Sektor:** [PLATZHALTER] *(aus unternehmens-profil.md)*
**Stadium:** [PLATZHALTER — GmbH / AG / Tochter einer AG / Personengesellschaft (HGB/MoPeG)]
**Hauptrechtsordnung:** Deutsches Recht (GmbHG, AktG, HGB, UmwG, WpÜG, MoPeG, GwG) *(aus unternehmens-profil.md)*
**Größe des Rechtsteams:** [PLATZHALTER] *(aus unternehmens-profil.md)*
**Eskalation:** [PLATZHALTER — externe Kanzlei, GC-Name oder Vorstandseskalationspfad]

**Praxiskontext:** [PLATZHALTER — Einzelkanzlei/kleine Kanzlei | Mittel-/Großkanzlei | Inhouse | Behörde/Rechtsberatungsstelle] *(aus unternehmens-profil.md)*

---

## Wer dieses Plugin nutzt

**Rolle:** [PLATZHALTER — Rechtsanwalt / juristische Fachkraft | Nichtjurist mit Anwaltszugang | Nichtjurist ohne Anwaltszugang]
**Anwaltskontakt:** [PLATZHALTER — Name / Team / externe Kanzlei / k. A.; ausfüllen wenn Nichtjurist]

*Skills lesen diesen Abschnitt, um den Arbeitsergebnis-Header zu wählen und zu entscheiden, ob folgenreiche Handlungen gesperrt werden sollen (siehe `## Ergebnisse` unten und die jeweiligen Skill-Sperren).*

---

**Stiller Modus für mandanten- und organgerichtete Ergebnisse.** Wenn ein Skill ein Ergebnis produziert, das ein Nicht-Rechts- oder externes Publikum lesen wird – ein Mandantenhinweis, ein Vorstandsmemo, ein Gesellschafterbeschluss, eine Zusammenfassung für Stakeholder, ein Mandantenbrief – interne Kommentare unterdrücken. Konkret:
- Arbeitsergebnis-Header: BEIBEHALTEN (schützt das Dokument)
- ⚠️ Prüfer-Hinweis: BEIBEHALTEN (einziger Ort, wo der Prüfer alles Notwendige findet)
- Quellenattributionstags: BEIBEHALTEN inline, aber zusammengefasst (Fußnote oder Endnote für ein sauberes Ergebnis)
- Skill-Fit-Kommentare: ENTFERNEN
- Plugin-Befehlsübergaben: ENTFERNEN aus dem Ergebnis; in separaten Prüfer-Hinweis
- „Ich habe folgende Dateien gelesen...": ENTFERNEN

Das Ergebnis soll lesen wie vom Partner verfasst. Meta-Kommentar kommt in einen Prüfer-Hinweis darüber oder in eine separate Nachricht, nicht in das Dokument.

## Verfügbare Integrationen

| Integration | Status | Fallback wenn nicht verfügbar |
|---|---|---|
| VDR (Datasite, Intralinks, Box) | [✓ / ✗] | DD-Abruf aus lokalem Ordner; Dokumente ablegen unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/mandate/[code]/vdr-mirror/` |
| Datenraum-Tool | [✓ / ✗] | Protokolle/Beschlüsse aus lokalen Vorlagen; keine Portal-Veröffentlichung |
| Dokumentenspeicher (Google Drive, SharePoint, Box) | [✓ / ✗] | Lokale Pfade lesen; keine systemübergreifende Suche |
| Slack | [✓ / ✗] | Briefings nur als Dateien; keine Kanal-Zusammenfassungen |

*Neu prüfen: `/gesellschaftsrecht:kaltstart-interview --integrationen-pruefen`*

---

## Ergebnisse

**Arbeitsergebnis-Header** (wird jedem Analyse-, Memo-, Prüf- oder Entwurfsergebnis vorangestellt):

- Wenn Rolle **Rechtsanwalt / juristische Fachkraft**: `VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS — ERSTELLT AUF ANWEISUNG DES RECHTSANWALTS — §§ 43a II BRAO, 203 StGB`
- Wenn Rolle **Nichtjurist** (beide Typen): `RECHERCHE-NOTIZEN — KEINE RECHTSBERATUNG — VOR HANDLUNGEN MIT EINEM ZUGELASSENEN RECHTSANWALT IN DEINER RECHTSORDNUNG ÜBERPRÜFEN`

**Anwaltsgeheimnis und Verschwiegenheitspflicht (§ 43a Abs. 2 BRAO, § 203 StGB).** Ein eigenständiges prozessuales Arbeitsergebnis-Privileg existiert im deutschen Recht nicht. Schutz vor Offenbarung richtet sich nach:
- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht des Rechtsanwalts
- § 203 StGB: strafrechtliche Sanktion für unbefugte Offenbarung
- § 383 ZPO: Zeugnisverweigerungsrecht des Rechtsanwalts im Zivilprozess
- § 53 StPO: Zeugnisverweigerungsrecht im Strafverfahren

**Bei Mandaten mit internationalem Bezug** (z. B. cross-border M&A) den Header anpassen und einen Jurisdiktionshinweis ergänzen: „[Hinweis: Das Anwaltsgeheimnis in [Jurisdiktion] weicht ab – zutreffendes Privileg-/Vertraulichkeitsregime vor Verwendung dieser Markierung zur Abschirmung des Dokuments bestätigen.]"

*Vertraulichkeitsmerkmal bei extern gerichteten Ergebnissen (ausgeführte Beschlüsse, Einreichungsdokumente, Briefe) entfernen – siehe jeweils Skill-Anweisungen. Gesellschaftsrechtliche Urkunden (beschlossene Protokolle, Beschlüsse) werden nie als vertraulich gekennzeichnet; nur die zugehörigen Entwurfsnotizen und Analysen sind es.*

**Nichtjurist-Ausgabemodus.** Wenn das Praxisprofil angibt, dass der Nutzer kein Rechtsanwalt ist, Ergebnisse für einen Leser strukturieren, der juristisches Fachjargon nicht entpacken kann: (1) die anwaltliche Zusammenfassung oben, nicht unten, (2) jede rechtliche Markierung erhält in Klammern eine einzeilige Erklärung in Alltagssprache, (3) jedes Gesetzeszitat erhält eine Betreffzeile in Alltagssprache.

---

**⚠️ Prüfer-Hinweis — ein Block über dem Ergebnis.** Dies ist der EINZIGE Ort für alles, was der Prüfer vor der Verwendung des Ergebnisses wissen muss. Jedes Pre-Check-Flag, jeden Vorbehalt und jede Meta-Notiz hier zusammenführen. Format:

> **⚠️ Prüfer-Hinweis**
> - **Quellen:** [Rechercheconnector: juris/beck-online ✓ verifiziert | nicht verbunden — Zitate aus Modellwissen, vor Verwendung prüfen]
> - **Gelesen:** [Seiten 1–50 von 200 | alle 3 Dokumente | N Einträge im Register | n. A.]
> - **Für dein Urteil markiert:** [N mit `[prüfen]` inline markierte Punkte | keine]
> - **Aktualität:** [nach Entwicklungen seit [Datum] gesucht — nichts gefunden | N Updates gefunden, inline vermerkt | konnte nicht suchen, prüfe [spezifische Normen]]
> - **Vor Verwendung:** [die 1–2 Dinge, die der Prüfer tatsächlich tun sollte — oder „bereit für deine Augen" wenn sauber]

---

**Entscheidungsbaum für nächste Schritte.** Nach einer Analyse, Prüfung oder Einschätzung mit einem Entscheidungsbaum abschließen – einem Entwurf der OPTIONEN, nicht der ENTSCHEIDUNG. Der Anwalt wählt; Claude setzt um. Format:

> **Wie weiter? Wähle eine Option und ich helfe dir, sie auszuarbeiten:**
> 1. **[Entwurf von X]** — Ich erstelle einen Erstentwurf des [Memos / Markups / Antwortschreibens / Eskalationshinweises / Beschlusses]
> 2. **Eskalieren** — Ich entwerfe eine Kurzeskalation an [Genehmiger aus deinem Praxisprofil]
> 3. **Mehr Fakten einholen** — Vor einer Beratung würde ich [die 2–3 offenen Fragen] benötigen
> 4. **Abwarten** — Ich ergänze dies im [Tracker / Register / Beobachtungsliste] mit einem Hinweis
> 5. **Anderes** — sag mir, wie du mit diesem Ergebnis vorgehen würdest

---

## Gemeinsame Leitplanken

Diese Regeln gelten für jeden Skill in diesem Plugin.

**Keine stille Ergänzung.** Wenn ein Skill Informationen benötigt, die er nicht hat, gibt es drei gültige Reaktionen:
1. **Mit Flag ergänzen.** Aus Websuche, Modellwissen oder anderer Quelle abrufen, Element taggen und fortfahren.
2. **Nichts sagen und stoppen.** Nutzer bitten, die Quelle einzufügen, und erst dann fortfahren.
3. **Flag, aber nicht verwenden.** Wenn bekannte Information vorliegt, die ändern würde, ob eine Regel gilt – als markierten Vorbehalt mit `[Modellwissen — prüfen]` kennzeichnen.

**Währungs-Trigger.** Für Fragen, bei denen Aktualität entscheidend ist: Websuche erforderlich. Gilt wenn die Frage abhängt von: aktueller Rechtsprechung oder Gesetzgebung, Inkrafttreten, Vollzugshaltung, einem jährlich aktualisierten Schwellenwert.

**Benutzer-angegebene Rechtsfakten verifizieren.** Wenn der Nutzer eine Norm, ein Aktenzeichen, ein Datum, eine Frist, eine Registernummer oder einen Schwellenwert nennt, diesen vor dem Aufbau von Analysen gegen Mandatsdokumente, das Praxisprofil oder eigenes Wissen verifizieren.

**Keine Präjudizienbindung.** Deutsche Rechtsprechung ist nicht bindend (Ausnahme: § 31 BVerfGG für BVerfG-Entscheidungen). BGH-Rspr. des II. Zivilsenats ist in gesellschaftsrechtlichen Fragen maßgeblich (h.M.) und wird entsprechend zitiert; abweichende Meinungen und Gegenauffassungen aus Kommentarliteratur (Roth/Altmeppen, Scholz, MüKoGmbHG, Hüffer/Koch, Schmidt/Lutter, MüKoAktG, MüKoHGB) sind argumentativ relevant.

**Zitierweise:** Immer nach `../references/zitierweise.md` (BGH-Stil). Beispiel:
- BGH, Urt. v. 16.12.1991 – II ZR 58/91, BGHZ 116, 359 (Rn. 14) – zur Kapitalaufbringung bei der GmbH.
- Roth/Altmeppen, GmbHG, 10. Aufl. 2021, § 34 Rn. 12.
- Scholz, GmbHG, 12. Aufl. 2018, § 46 Rn. 45.

**Pre-Check vor jedem Skill, der Autorität zitiert.** Prüfen, ob ein Rechercheconnector (juris, beck-online, Westlaw DE) tatsächlich antwortet. Falls keiner verfügbar: in der **Quellen:**-Zeile des Prüfer-Hinweises vermerken.

**Quellen-Tags nach tatsächlichem Handeln, nicht nach Wunsch.**
- `[juris]` / `[beck-online]` / `[Westlaw DE]` — NUR wenn das Zitat in diesem Gespräch aus einem Tool-Ergebnis stammt.
- `[Norm / Amtsblatt]` — NUR wenn Text von offizieller Quelle in dieser Sitzung abgerufen.
- `[Nutzer bereitgestellt]` — der Nutzer hat es eingefügt oder verlinkt.
- `[Modellwissen — prüfen]` — alles andere. Dies ist der Standard.

**Eskalation bei Interessenkonflikten.** § 43a Abs. 4 BRAO: Kein Anwalt darf widerstreitende Interessen vertreten. Bei Mandatswechsel oder Cross-Border-Transaktion auf Konfliktcheck hinweisen.

**Querweiser Schweregrad-Boden.** Wenn ein Skill ein Finding mit einem Schweregrad produziert und ein anderer Skill es übernimmt, trägt der nachgelagerte Skill den vorgelagerten Schweregrad als BODEN. Ein 🔴 Finding vorgelagert kann nicht stillschweigend nachgelagert reduziert werden.

Kanonische Skala: 🔴 Blockierend / 🟠 Hoch / 🟡 Mittel / 🟢 Niedrig.

---

## Rechtsrahmen (Deutschland)

### Pflichtgesetze

| Gesetz | Vollbezeichnung | Relevanz |
|---|---|---|
| **GmbHG** | Gesetz betreffend die GmbH | Gründung, Kapital, Geschäftsführer, Gesellschafterrechte |
| **AktG** | Aktiengesetz | Vorstand, Aufsichtsrat, HV, Kapitalmaßnahmen |
| **HGB** | Handelsgesetzbuch | Handelsregister, Rechnungslegung, Bilanzpublizität § 325 |
| **UmwG** | Umwandlungsgesetz | Verschmelzung, Spaltung, Formwechsel, Vermögensübertragung |
| **WpÜG** | Wertpapiererwerbs- und Übernahmegesetz | Öffentliche Übernahmen, Pflichtangebote § 35, Squeeze-out §§ 39a ff. |
| **MoPeG** | Modernisierung Personengesellschaftsrecht | GbR-Register ab 01.01.2024, GbR als Rechtsträger |
| **WEG** | Wohnungseigentumsgesetz | Wenn gesellschaftsrechtlich relevant (WEG-Gesellschaft) |
| **GwG** | Geldwäschegesetz | Transparenzregister § 20, wirtschaftlich Berechtigte |
| **InsO** | Insolvenzordnung | Insolvenzantragspflicht § 15a GmbHG, Anfechtung §§ 129 ff. |
| **DSGVO/BDSG** | Datenschutz | DD-Datenweitergabe, Consent-Anforderungen |

### Due Diligence – vorprozessuale Beweiserhebung im deutschen Recht

**Vorprozessuale Beweiserhebung ist in deutschen Verfahren auf eng begrenzte gesetzliche Instrumente beschränkt.** Due Diligence (DD) in deutschen M&A-Transaktionen läuft ausschließlich über:

1. **Q&A-Prozess:** Käufer stellt schriftliche Fragen; Verkäufer beantwortet nach Ermessen.
2. **Virtueller Datenraum (VDR):** Verkäufer stellt Dokumente bereit; was nicht bereitgestellt wird, gilt als nicht offenbart (Disclosure-Prinzip).
3. **Disclosure Letter:** Schriftliche Offenbarungserklärung des Verkäufers, die im SPA (Share Purchase Agreement) integriert oder als Anlage beigefügt wird und Garantien modifiziert.
4. **Gesetzliche Auskunftsansprüche** (außerhalb der DD-Phase, im Streitfall):
   - § 666 BGB (Auskunft des Beauftragten)
   - § 259 BGB (Rechenschaftspflicht)
   - § 242 BGB (Treu und Glauben)
   - Art. 15 DSGVO (Datenschutz-Auskunftsrecht)
   - §§ 142, 144 ZPO (gerichtliche Urkundenvorlage)
   - § 254 ZPO (Stufenklage)

**Folge:** Was im Datenraum nicht offenbart wurde, ist weder beweisbar noch garantiert. Disclosure-Lücken schützen den Käufer nur, wenn der SPA dies entsprechend regelt (Knowledge Qualifier, Disclosure Carve-out).

### Kommentarliteratur (zitationspflichtig)

- **GmbH:** Roth/Altmeppen, GmbHG; Scholz, GmbHG; Lutter/Hommelhoff, GmbHG; MüKoGmbHG (Fleischer/Goette)
- **AG:** Hüffer/Koch, AktG; Schmidt/Lutter, AktG; MüKoAktG (Wacker/Habersack)
- **HGB:** MüKoHGB (Schmidt); Staub, HGB (Großkommentar)
- **Umwandlung:** Lutter, UmwG; Kallmeyer, UmwG
- **Übernahme:** Assmann/Pötzsch/Uwe H. Schneider, WpÜG

### BGH II. Zivilsenat – Leitentscheidungen

| Entscheidung | Aktenzeichen | Thema |
|---|---|---|
| BGHZ 116, 359 | II ZR 58/91 | Kapitalaufbringung GmbH |
| BGHZ 149, 10 | II ZR 184/00 | Existenzvernichtungshaftung (Trihotel) |
| BGHZ 176, 204 | II ZR 3/04 | Trihotel – Haftung nach § 826 BGB |
| BGHZ 179, 71 | II ZR 225/07 | Gesellschafterhaftung bei Insolvenz |
| BGH NZG 2019, 1023 | II ZR 44/18 | Gesellschafterbeschluss Anfechtung |
| BGH ZIP 2020, 1571 | II ZR 175/19 | GmbH-Geschäftsführer-Abberufung |

---

## Mandat-Arbeitsbereiche

*Nur relevant für Mehrmandat-Kanzleien (Einzelkanzlei, kleine Kanzlei, Großkanzlei). Inhouse-Juristen mit einem Unternehmen: dieser Abschnitt ist deaktiviert.*

**Aktiviert:** ✗ (beim Kaltstart für Kanzleien eingestellt; Inhouse-Juristen sehen dies nie)
**Aktives Mandat:** keins
**Mandatsübergreifender Kontext:** aus

---

## Aktive Module

*Nur Abschnitte für aktive Module werden unten geschrieben. Inaktive Module werden vollständig weggelassen.*

---

<!-- MODUL: M&A — aktivieren wenn Unternehmen M&A-Transaktionen durchführt -->

## M&A

**Typische Seite:** [PLATZHALTER — Käufer / Verkäufer / beide — Hinweis: variiert je Deal, per Mandat-Kontext setzen bei /gesellschaftsrecht:kaltstart-interview --neues-mandat]
**Dealrhythmus:** [PLATZHALTER — Serienerwerber N Deals/Jahr mit Standardplaybook / je Deal individuell]
**Deal-Lead:** [PLATZHALTER — Corp Dev / Legal / externe Kanzlei als Hauptberater]

### DD-Struktur

**Anforderungskategorien:**
1. [PLATZHALTER — aus Seed-Anforderungsliste übernommen]

**Wesentlichkeitsschwellen:**
- Verträge: [PLATZHALTER — alle / >X EUR Jahreswert / Top-N nach Umsatz]
- Rechtsstreitigkeiten: [PLATZHALTER — alle anhängigen / >X EUR Risiko / nur wesentliche]

**VDR typisch:** [PLATZHALTER — Datasite / Intralinks / Box / SharePoint / variiert]
**Disclosure Letter:** [PLATZHALTER — als SPA-Anlage / eigenständig / kein gesonderter DL]

### Issues-Memo-Format

*Aus [früherem Mandatsnamen] entnommen.*

**Struktur:** [PLATZHALTER]
**Schweregrad-Schema:** [PLATZHALTER — Rot/Gelb/Grün | Kritisch/Hoch/Mittel/Niedrig | anderes]
**Finding-Vorlage:**
```
[PLATZHALTER — genaue Struktur aus Seed-Memo]
```
**Adressat:** [PLATZHALTER — nur Deal-Lead / Deal-Team / Vorstand]
**Tiefe:** [PLATZHALTER — einzeilig / vollständige Analyse / gestaffelt nach Schweregrad]

### KI-gestützte Prüfung

**Tool:** [PLATZHALTER — Luminance / Kira / keins]
**Verwendet für:** [PLATZHALTER]
**Vertrauensniveau:** [PLATZHALTER — Ergebnis übernehmen / Stichproben / vollständige Neuprüfung]
**Übergabe:** [PLATZHALTER — wer lädt, wer QA macht]

### Vollzugscheckliste

**Ort:** [PLATZHALTER — Excel / Smartsheet / Deal-Tool]
**Verantwortlicher:** [PLATZHALTER]
**Aktualisierungsrhythmus:** [PLATZHALTER]

### Deal-Team-Briefing

**Rhythmus:** [PLATZHALTER — täglich / wöchentlich / Meilenstein]
**Format:** [PLATZHALTER — E-Mail / Slack / Ruf]
**Was die Geschäftsführung liest:** [PLATZHALTER — nur Kurzfassung / vollständiges Memo / je Empfänger]

### Seed-Dokumente (M&A)

| Dokument | Quelle | Datum | Hinweise |
|---|---|---|---|
| DD-Anforderungsliste | [PLATZHALTER] | | |
| Früheres Issues-Memo | [PLATZHALTER] | | |

---

<!-- MODUL: Organe & Protokoll — aktivieren für Vorstandsprotokolle, Aufsichtsratsprotokolle, Gesellschafterversammlungen -->

## Organe & Protokoll

**Rolle:** [PLATZHALTER — Protokollführer / Syndikusrechtsanwalt / Externer Anwalt ohne formelle Sekretariatsfunktion]
**Organ-Größe:** [PLATZHALTER — N Mitglieder Vorstand / N Mitglieder Aufsichtsrat / N Gesellschafter]
**Zusammensetzung:** [PLATZHALTER — Anteilseigner/Unabhängige-Aufteilung, ggf. Mitbestimmung §§ 96 ff. AktG, DrittelbG, MitbestG]
**Ausschüsse:** [PLATZHALTER — Prüfungsausschuss / Vergütungsausschuss / Nominierungsausschuss / sonstige]

**Protokollformat:** [PLATZHALTER — ausführliche Niederschrift / Beschlussprotokoll / Hybridform]
**Protokoll-Timing:** [PLATZHALTER — zirkuliert innerhalb von N Tagen nach Sitzung]
**Genehmigungsprozess:** [PLATZHALTER — zirkuliert zur Prüfung / genehmigt bei nächster Sitzung / sonstig]
**Sitzungsfrequenz AG:** [PLATZHALTER — Vorstand: N/Jahr; Aufsichtsrat: mind. 2/Jahr gem. § 110 AktG]
**Sitzungsfrequenz GmbH:** [PLATZHALTER — Gesellschafterversammlung: N/Jahr gem. § 49 GmbHG]

**Beschlüsse im schriftlichen Verfahren:**
- Verwendet für: [PLATZHALTER — Routinebestellungen / Kapitalmaßnahmen / Jahresabschluss / weit gefasst]
- Grenzen: [PLATZHALTER — § 48 Abs. 2 GmbHG setzt Einvernehmen aller Gesellschafter voraus; § 121 AktG schließt für manche AG-Beschlüsse schriftliches Verfahren aus]

**Beschluss-Repository:** [PLATZHALTER — Ordnerpfad / Google Drive / SharePoint / Box-Ort oder „nur Seed-Dokumente"]
**Beschlussformat:**
- Beschlusssprache: [PLATZHALTER — „Es wird beschlossen:" / „Die Gesellschafterversammlung beschließt:" / sonstig]
- Präambel-Tiefe: [PLATZHALTER — vollständige WOHINGEGEN / minimal / keine]
- Bevollmächtigungssprache: [PLATZHALTER — aus Seed oder Repository entnommen]
- Elektronische Unterschriften: [PLATZHALTER — akzeptiert (qualifizierte eSignatur gem. eIDAS/VDG) / nicht akzeptiert]

**Protokollvorlage:**
*Aus Seed-Protokoll entnommen. Vom Protokoll-Skill für jeden Entwurf verwendet.*
- Struktur: [PLATZHALTER]
- Beschlusssprache: [PLATZHALTER]
- Diskussionstiefe: [PLATZHALTER]
- Header-Format: [PLATZHALTER]
- Unterschriftenblock: [PLATZHALTER — Protokollführer allein / Vorsitz + Protokollführer]

**Jährliche Governance-Zykluseinträge:**
- [PLATZHALTER — z. B. Jahresabschluss-Feststellung, Ergebnisverwendung, Entlastung Geschäftsführer/Vorstand/AR, Abschlussprüfer-Beauftragung]

---

<!-- MODUL: Börse/Kapitalmarkt — aktivieren für WpÜG-Reporting, Kapitalmarktrecht, Ad-hoc, §§ 15 ff. WpHG -->

## Börse/Kapitalmarkt

**Börse:** [PLATZHALTER — Xetra/Frankfurt / NYSE / Nasdaq / sonstig]
**Geschäftsjahresende:** [PLATZHALTER]
**Emittentenstatus:** [PLATZHALTER — großer Emittent / mittelgroßer Emittent / kleiner Emittent]

**Ad-hoc-Meldungen (§ 17 MAR):**
- Verantwortlich: [PLATZHALTER — CFO / Legal / IR]
- Zuständige Behörde: BaFin (Bundesanstalt für Finanzdienstleistungsaufsicht)
- Meldeplattform: DGAP / EQS / andere

**Stimmrechtsmitteilungen (§§ 33 ff. WpHG):**
- Tracking: [PLATZHALTER — Legal / externe Kanzlei / IR]
- Meldefristen: § 33 WpHG — 4 Handelstage

---

<!-- MODUL: Gesellschafts-Compliance — aktivieren für Filialverwaltung, Handelsregister, Kapital -->

## Gesellschafts-Compliance

**Aktive Rechtsträger:** [PLATZHALTER — N Gesellschaften]
**Wichtige Rechtsordnungen:** [PLATZHALTER — Liste]
**Registerführer:** [PLATZHALTER — Handelsregister / Transparenzregister / Partnerschaftsregister]

**Gesellschaftsverwaltungssystem:** [PLATZHALTER — Brainware / CorpTech / manuell]
**Stammkapital-Tool:** [PLATZHALTER — Ledgy / manuell / Notarurkunde]

**Routineeinreichungs-Verantwortlicher:** [PLATZHALTER — Legal / Legal Ops / externe Kanzlei]
**Jahresabschluss-Tracking:** [PLATZHALTER — wie verfolgt, wer prüft; Frist § 325 HGB: 12 Monate nach GJ-Ende]

**Konzerninterne Verträge vorhanden:** [PLATZHALTER — ja / nein / teilweise]
**Transparenzregister aktuell:** [PLATZHALTER — ja / ausstehend; § 20 GwG: Mitteilung innerhalb von 2 Wochen bei Änderungen]

**Compliance-Tracker:** `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/gesellschaften/compliance-tracker.yaml`
**Letzter Compliance-Bericht:** [PLATZHALTER — Datum oder null]
**Letztes Gesundheits-Audit:** [PLATZHALTER — Datum oder null]

**Gesellschaftstabelle:**
*Aus Organigramm-Upload entnommen oder aus Interview-Antworten erstellt.*

| Gesellschaftsname | Typ | Rechtsordnung | Muttergesellschaft | Beteiligung % | Status |
|---|---|---|---|---|---|
| [PLATZHALTER] | [GmbH/AG/GmbH & Co. KG/GbR] | [PLATZHALTER] | [PLATZHALTER] | [PLATZHALTER] | [Aktiv/Ruhend] |

---

*Vollständiges Interview neu ausführen: `/gesellschaftsrecht:kaltstart-interview --redo`*
*Modul hinzufügen: `/gesellschaftsrecht:kaltstart-interview --modul [m&a | organe | boerse | compliance]`*
*Neues M&A-Mandat: `/gesellschaftsrecht:kaltstart-interview --neues-mandat`*
