<!--
KONFIGURATIONSPFAD

Die nutzerspezifische Konfiguration dieses Plugins liegt versionssicher unter:

  ~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md

Regeln für alle Skills, Befehle und Agenten in diesem Plugin:
1. Konfiguration aus dem obigen Pfad LESEN. Nicht aus dieser Datei.
2. Falls diese Datei nicht existiert oder noch [PLATZHALTER]-Marker enthält, VOR substanzieller Arbeit ANHALTEN. Meldung: „Das Plugin muss eingerichtet werden, bevor es nützliche Ausgaben liefern kann. Bitte /vertragsrecht:ersteinrichtung ausführen – Dauer ca. 10–15 Minuten; alle Funktionen hängen davon ab. Ohne Einrichtung sind Ausgaben generisch und spiegeln nicht die tatsächliche Praxis wider." NICHT mit Platzhalter- oder Standard-Konfiguration fortfahren. Die einzige Funktion, die ohne Einrichtung läuft, ist /vertragsrecht:ersteinrichtung selbst sowie ein optionales --integration-check-Flag.
3. Einrichtung und Ersteinrichtung SCHREIBEN in diesen Pfad, ggf. übergeordnete Verzeichnisse anlegen.
4. Diese Datei (die Sie gerade lesen) ist das TEMPLATE. Sie wird bei jedem Plugin-Update ersetzt. Nutzerdaten niemals hier speichern.

**Gemeinsames Mandantenprofil.** Unternehmensfakten (wer Sie sind, was Sie tun, wo Sie tätig sind, Risikobereitschaft, Schlüsselpersonen) liegen in `~/.claude/plugins/config/claude-fuer-deutsches-recht/company-profile.md` – eine Ebene höher, gemeinsam genutzt von allen Plugins. Diese Datei vor dem Praxisprofil des Plugins lesen. Falls sie nicht existiert, legt die Einrichtung sie an.
-->

# Vertragsrechtliches Praxisprofil

*Diese Datei wird beim Ersteinrichtungs-Interview befüllt. Bis dahin ist sie ein Template. Solange [PLATZHALTER]-Werte sichtbar sind, bitte `/vertragsrecht:ersteinrichtung` ausführen.*

*Nach Befüllung: Diese Datei direkt bearbeiten. Jeder Skill in diesem Plugin liest sie vor Beginn jeder Tätigkeit. Eine Änderung hier wirkt sich überall aus.*

---

## Rechtsrahmen und anwendbares Recht

Dieses Plugin arbeitet im Rahmen des deutschen Privatrechts. Maßgebliche Rechtsquellen:

### BGB – Schuldrecht (Allgemeiner und Besonderer Teil)
- **§§ 241 ff. BGB** – Allgemeines Schuldrecht, Leistungspflichten, Nebenpflichten, Schutzpflichten
- **§§ 280 ff. BGB** – Schadensersatz, Pflichtverletzung, Vertretenmüssen
- **§§ 305–310 BGB** – AGB-Recht (Einbeziehung, Überraschungsklauseln, Inhaltskontrolle, Transparenzgebot)
- **§§ 311 ff. BGB** – Vertragsschluss, vorvertragliche Pflichten (§ 311 II BGB, culpa in contrahendo)
- **§§ 433 ff. BGB** – Kaufvertrag; §§ 631 ff. BGB – Werkvertrag; §§ 611 ff. BGB – Dienstvertrag
- **§§ 339 ff. BGB** – Vertragsstrafe
- **§§ 355 ff., 312g BGB** – Verbraucherwiderrufsrecht, Fernabsatz

### AGB-Recht im Detail (§§ 305–310 BGB)
- **§ 305 BGB** – Einbeziehungsvoraussetzungen
- **§ 305c BGB** – Überraschende und mehrdeutige Klauseln (Unklarheitenregel)
- **§ 307 BGB** – Inhaltskontrolle, unangemessene Benachteiligung; § 307 I 2 BGB Transparenzgebot
- **§ 308 BGB** – Klauselverbote mit Wertungsmöglichkeit
- **§ 309 BGB** – Klauselverbote ohne Wertungsmöglichkeit (z. B. § 309 Nr. 7 Haftungsausschluss; § 309 Nr. 9 Vertragslaufzeit)
- **§ 310 BGB** – Anwendungsbereich; Sonderregeln B2B

### HGB – Handelskauf und Handelsgeschäfte
- **§§ 343 ff. HGB** – Handelsgeschäfte allgemein
- **§§ 373 ff. HGB** – Handelskauf; § 377 HGB Rügepflicht
- **§§ 407 ff. HGB** – Frachtrecht
- Beachte: Im B2B-Verhältnis gelten erweiterte Gestaltungsfreiheiten bei AGB (§ 310 I BGB).

### CISG – UN-Kaufrecht
- Gilt bei grenzüberschreitenden Warenkaufverträgen zwischen Unternehmern mit Sitz in verschiedenen Vertragsstaaten (Art. 1 CISG).
- **Art. 14 ff. CISG** – Vertragsschluss; **Art. 25 CISG** – wesentliche Vertragsverletzung; **Art. 45 ff. CISG** – Käuferrechte; **Art. 74 ff. CISG** – Schadensersatz.
- Abwahl möglich nach Art. 6 CISG; Klausel empfohlen: „Das CISG findet keine Anwendung."

### UWG – Lauterkeitsrecht
- **§ 3 UWG** – Verbot unlauterer geschäftlicher Handlungen
- **§ 3a UWG** – Rechtsbruch
- **§ 5 UWG** – Irreführende geschäftliche Handlungen
- **§ 7 UWG** – Unzumutbare Belästigung (E-Mail-Marketing)
- **§ 8 UWG** – Beseitigung und Unterlassung; § 8a UWG – Verbandsklagen
- **§ 13 UWG** – Abmahnung; § 13a UWG – Vertragsstrafe

### LkSG – Lieferkettensorgfaltspflichtengesetz
- Gilt ab 1.000 Arbeitnehmern (seit 01.01.2024; schrittweise ab 500 AN).
- **§ 3 LkSG** – Sorgfaltspflichten; **§ 6 LkSG** – Risikoanalyse; **§ 7 LkSG** – Präventionsmaßnahmen.
- Vertragliche Einbindung: Lieferanten-CoC, Audit-Klauseln, Kündigungsrecht bei Verstoß.

### DSGVO / BDSG
- **Art. 28 DSGVO** – Auftragsverarbeitungsvertrag (AVV); Sub-Auftragsverarbeiter Art. 28 IV DSGVO.
- **Art. 82 DSGVO** – Schadensersatz bei Datenschutzverstößen.
- **§§ 26, 31 BDSG** – Beschäftigtendatenschutz.

---

## Wer sind wir

[Unternehmensname] ist eine [Rechtsform]. Das Vertragsteam besteht aus [Anzahl] Personen. [Name GC / Leiter Rechtsabteilung] ist der finale Eskalationspunkt. Wir verarbeiten monatlich ca. [Anzahl] Verträge, überwiegend [Lieferanten-/Kunden-/gemischt]. Wir nutzen [CLM-System] für die Vertragslebenszyklusverwaltung.

*(Unternehmensname, Rechtsform, Branche und Größe kommen aus company-profile.md – dort ändern, damit Änderungen in allen Plugins wirken.)*

**Das macht uns Kopfzerbrechen:** [PLATZHALTER – was das Team beschäftigt, in eigenen Worten]

**Einsatzkontext:** [PLATZHALTER – Kanzlei (klein/mittel/groß) | Rechtsabteilung | Behörde/öffentlicher Dienst]

---

## Nutzerrolle

**Rolle:** [PLATZHALTER – Rechtsanwalt/Jurist | Nicht-Jurist mit Anwaltszugang | Nicht-Jurist ohne Anwaltszugang]
**Anwaltlicher Ansprechpartner:** [PLATZHALTER – Name / Team / externe Kanzlei / nicht zutreffend (wenn selbst Anwalt)]

---

## Verfügbare Integrationen

| Integration | Status | Fallback bei Nichtverbindung |
|---|---|---|
| CLM (Ironclad, Agiloft o. Ä.) | [PLATZHALTER ✓/✗] | Manuelle Pflege; Verlängerungstracker läuft gegen lokales Register |
| E-Signatur (DocuSign o. Ä.) | [PLATZHALTER ✓/✗] | Nutzer leitet Unterschriftsprozess außerhalb des Plugins |
| Dokumenten-Ablage (Drive / SharePoint / Box) | [PLATZHALTER ✓/✗] | Nutzer lädt Verträge für jede Prüfung direkt hoch |
| Slack | [PLATZHALTER ✓/✗] | Benachrichtigungen und Zusammenfassungen direkt inline zugestellt |

*Erneut prüfen: `/vertragsrecht:ersteinrichtung --check-integrations`*

---

## Playbook

**Aktive Seite:** [PLATZHALTER – Verkäufer / Käufer / beides – wird bei Ersteinrichtung gesetzt]

*Verkäuferseite = das Unternehmen verkauft eigene Produkte oder Dienstleistungen. Wir sind Lieferant/Auftragnehmer. In der Regel unser Muster.*
*Käuferseite = das Unternehmen kauft bei Dritteanbietern/Lieferanten. Wir sind Auftraggeber. In der Regel deren Muster.*

> Skills, die einen Vertrag gegen dieses Playbook prüfen, ermitteln zunächst die Seite des Unternehmens. Falls unklar, fragen. Dann den zutreffenden Playbook-Abschnitt lesen. Verkäufer-Positionen niemals auf Käufer-Verträge anwenden und umgekehrt.

### Verkäufer-Playbook

*Gilt, wenn das Unternehmen Verkäufer/Auftragnehmer ist. In der Regel unser Muster.*

*[Nicht konfiguriert – `/vertragsrecht:ersteinrichtung --seite verkäufer` ausführen]*

#### Haftungsbegrenzung (§§ 276, 309 Nr. 7 BGB; § 307 BGB)

*Die Haftungsbegrenzung hat vier Dimensionen – der Betrag ist die unwichtigste.*

**Direktschäden-Deckel (Vielfaches der Vergütung):** [PLATZHALTER – z. B. „12 Monatsvergütungen"]

**Mittelbare Schäden/Folgeschäden:** [PLATZHALTER – ausgeschlossen / gedeckelt / unbegrenzt / spiegelsymmetrisch zu Direktschäden]
*Hinweis: § 309 Nr. 7 BGB verbietet den Ausschluss von Haftung für Vorsatz und grobe Fahrlässigkeit gegenüber Verbrauchern. Im B2B-Bereich ist ein Ausschluss für leichte Fahrlässigkeit bei nicht wesentlichen Pflichten möglich.*

**Zulässige Ausnahmen (oberhalb des Deckels):** [PLATZHALTER – z. B. „Vorsatz, grobe Fahrlässigkeit, Verletzung von Leben/Körper/Gesundheit, Verletzung wesentlicher Vertragspflichten (Kardinalpflichten), Datenschutzverstöße"]

**Akzeptable Bemessungsgrundlage:** [PLATZHALTER – z. B. „im vorangegangenen Vertragsjahr gezahlte Vergütung" vs. „insgesamt nach Vertrag zu zahlende Vergütung"]

**Akzeptable Fallback-Positionen:**
- [PLATZHALTER]

**Nie akzeptieren:**
- [PLATZHALTER – z. B. „Ausschluss für grobe Fahrlässigkeit bei Kardinalpflichten (BGH-Rspr. beachten)", „unbegrenzte Haftung für mittelbare Schäden"]

*BGH-Leitlinie: BGH, Urt. v. 19.09.2007 – VIII ZR 141/06, NJW 2007, 3774 – Ausschluss der Haftung für leichte Fahrlässigkeit bei Verletzung von Kardinalpflichten unwirksam. Grüneberg, in: Grüneberg, BGB, 83. Aufl. 2024, § 307 Rn. 38.*

#### Freistellung (Indemnification)

**Standardposition:** [PLATZHALTER – z. B. „Wir stellen für IP-Verletzungsansprüche frei, die aus unserem Produkt entstehen; Auftraggeber stellt für eigene Daten und eigenverantwortliche Nutzung frei"]

**Akzeptable Fallback-Positionen:**
- [PLATZHALTER]

**Nie akzeptieren:**
- [PLATZHALTER]

#### Datenschutz (Art. 28 DSGVO, §§ 26 ff. BDSG)

**Standardposition:** [PLATZHALTER – z. B. „Unser AVV als Auftragsverarbeiter; AVV des Auftraggebers mit Anmerkungen akzeptiert"]

**Anforderungen:**
- Sub-Auftragsverarbeiter: Genehmigungspflicht (Art. 28 IV DSGVO)
- Meldepflicht Datenpannen: 72 Stunden (Art. 33 DSGVO)
- Löschung nach Vertragsende: Zertifikat
- Standardvertragsklauseln bei Drittlandübermittlung (Art. 46 DSGVO)

**Nie akzeptieren:**
- [PLATZHALTER]

#### Laufzeit und Kündigung (§§ 314, 620 BGB; § 309 Nr. 9 BGB)

**Standardposition:** [PLATZHALTER – z. B. „1 Jahr, automatische Verlängerung, 3 Monate Kündigungsfrist"]

*Hinweis: § 309 Nr. 9 BGB begrenzt stillschweigende Verlängerungen in B2C-Verträgen auf jeweils 1 Jahr; Kündigungsfrist max. 3 Monate.*

**Akzeptable Fallback-Positionen:**
- [PLATZHALTER]

**Nie akzeptieren:**
- [PLATZHALTER – z. B. „Bindung über 5 Jahre ohne außerordentliches Kündigungsrecht"]

#### Gerichtsstand und Rechtswahl

**Bevorzugt:** [PLATZHALTER – z. B. „München / Hamburg / Frankfurt, deutsches Recht, CISG ausgeschlossen"]
**Akzeptabel:** [PLATZHALTER]
**Eskalation erforderlich:** [PLATZHALTER]
**Nie:** [PLATZHALTER]

#### Das eine K.-o.-Kriterium

[PLATZHALTER – der Deal-Breaker auf Verkäuferseite. Jede Verkäufer-Prüfung beginnt damit.]

---

### Käufer-Playbook

*Gilt, wenn das Unternehmen Auftraggeber/Käufer ist. In der Regel deren Muster.*

*[Nicht konfiguriert – `/vertragsrecht:ersteinrichtung --seite käufer` ausführen]*

#### Haftungsbegrenzung (§§ 276, 309 Nr. 7 BGB; § 307 BGB)

**Direktschäden-Deckel (Vielfaches der Vergütung):** [PLATZHALTER]

**Mittelbare Schäden/Folgeschäden:** [PLATZHALTER]

**Ausnahmen, die wir verlangen (oberhalb des Deckels):** [PLATZHALTER – z. B. „grobe Fahrlässigkeit, Vorsatz, IP-Verletzung, Datenpanne, Verletzung von Leben/Körper/Gesundheit"]

**Nie akzeptieren:**
- [PLATZHALTER – z. B. „Lieferanten-Haftung auf 3 Monatsvergütungen begrenzt", „undefinierte Bemessungsgrundlage"]

#### Freistellung

**Standardposition:** [PLATZHALTER]

**Akzeptable Fallback-Positionen:**
- [PLATZHALTER]

**Nie akzeptieren:**
- [PLATZHALTER]

#### Gewährleistung (§§ 434 ff., 633 ff. BGB)

**Standardposition:** [PLATZHALTER – z. B. „2 Jahre gesetzliche Gewährleistung; keine Abkürzung im B2B; Nacherfüllung vor Rücktritt"]

*Hinweis: § 309 Nr. 8 BGB enthält Klauselverbote zur Gewährleistung gegenüber Verbrauchern; im B2B nach § 310 I BGB teilweise abdingbar, aber § 307 BGB beachten.*

**Akzeptable Fallback-Positionen:**
- [PLATZHALTER]

**Nie akzeptieren:**
- [PLATZHALTER]

#### Datenschutz (Art. 28 DSGVO)

**Standardposition:** [PLATZHALTER – z. B. „Lieferant unterzeichnet unseren AVV als Auftragsverarbeiter"]

**Anforderungen:**
- [PLATZHALTER – z. B. „ISO 27001 / SOC 2 Type II für alle Lieferanten mit Zugang zu personenbezogenen Daten"]

**Nie akzeptieren:**
- [PLATZHALTER]

#### Laufzeit und Kündigung

**Standardposition:** [PLATZHALTER – z. B. „Kündigung aus wichtigem Grund jederzeit (§ 314 BGB); ordentliche Kündigung mit 3 Monaten Frist"]

**Akzeptable Fallback-Positionen:**
- [PLATZHALTER]

**Nie akzeptieren:**
- [PLATZHALTER]

#### Gerichtsstand und Rechtswahl

**Bevorzugt:** [PLATZHALTER]
**Akzeptabel:** [PLATZHALTER]
**Eskalation erforderlich:** [PLATZHALTER]
**Nie:** [PLATZHALTER]

#### Das eine K.-o.-Kriterium

[PLATZHALTER – der Deal-Breaker auf Käuferseite. Jede Käufer-Prüfung beginnt damit.]

---

## Eskalation

| Kann genehmigen | Ohne Eskalation | Eskaliert an | Per |
|---|---|---|---|
| [Sachbearbeiter/Junior-Jurist] | [PLATZHALTER Schwellenwert] | [Syndikusanwalt] | [Slack/E-Mail] |
| [Syndikusanwalt] | [PLATZHALTER Schwellenwert] | [GC / Leiter Rechtsabteilung] | [Methode] |
| [GC] | [PLATZHALTER Schwellenwert] | [CFO/Vorstand] | [Methode] |

**Betragsschwellen:** [PLATZHALTER]

**Automatische Eskalationen unabhängig vom Betrag:**
- [PLATZHALTER – z. B. „Unbegrenzte Haftung, IP-Zuordnung an Lieferanten, alles auf der Nie-Liste oben"]

---

## Hausstandard

**Ton bei Klausel-Redlines:** [PLATZHALTER]

**Stakeholder-Zusammenfassungen:** [PLATZHALTER – wer liest sie, wie lang]

**Ablageort für Arbeitsergebnisse:** [PLATZHALTER – CLM, Drive-Ordner, Slack-Kanal]

**Verlängerungs-Alerts gehen an:** [PLATZHALTER – Slack-Kanal oder E-Mail]

---

## Ausgaben

**Arbeitsergebnis-Header** (wird jeder Analyse, jedem Vermerk, jeder Prüfung oder Bewertung vorangestellt):

- Falls Rolle = Rechtsanwalt/Jurist: `VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS – ERSTELLT AUF ANWEISUNG EINES RECHTSANWALTS – ANWALTLICHE VERSCHWIEGENHEITSPFLICHT (§ 43a II BRAO, § 203 StGB)`
- Falls Rolle = Nicht-Jurist: `RECHERCHE-HINWEISE – KEINE RECHTSBERATUNG – VOR HANDELNS MIT EINEM ZUGELASSENEN RECHTSANWALT ABSTIMMEN`

**Deutschrechtlicher Hinweis zum Anwaltsgeheimnis.** Das anwaltliche Arbeitsergebnis-Privileg (US: „attorney work product") existiert im deutschen Recht nicht als eigenständige Prozessregel. Der Schutz ergibt sich aus:
- § 43a Abs. 2 BRAO, § 203 StGB – anwaltliche Verschwiegenheitspflicht
- § 53 StPO – Zeugnisverweigerungsrecht
- § 383 I Nr. 6 ZPO – Zeugnisverweigerungsrecht in Zivilverfahren
- Bei Syndikusanwälten: BGH, Beschl. v. 07.12.2023 – AnwZ (Brfg) 1/23 – eingeschränktes Zeugnisverweigerungsrecht beachten.

Interne Compliance-Analysen, DPIAs oder Launch-Reviews sind grundsätzlich nicht vor BaFin-/Behörden-Untersuchungen geschützt. Externe Mandatierung schützt besser als interne Analyse. Der Header `VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS` ist eine Kennzeichnung, keine Garantie.

**Für Mandanten-/Vorstands-Dokumente:** Interne Metakommentare unterdrücken. Speziell:
- Arbeitsergebnis-Header: BEHALTEN
- ⚠️ Prüfer-Hinweis: BEHALTEN
- Quellenkennzeichnungs-Tags: BEHALTEN (inline oder als Fußnote)
- Skill-Workflow-Erklärungen: KÜRZEN
- Plugin-Befehlsverweise: KÜRZEN (in gesonderten Prüfer-Hinweis)

Das Ergebnis soll lesen wie von einem Berufsjuristen verfasst.

**⚠️ Prüfer-Hinweis – ein Block über dem Dokument.** Hier stehen alle Informationen, die der Prüfer vor der Nutzung der Ausgabe kennen muss:

> **⚠️ Prüfer-Hinweis**
> - **Quellen:** [Recherche-Connector: CourtListener/Juris/Beck-Online ✓ verifiziert | nicht verbunden – Zitate aus Trainingswissen, vor Nutzung prüfen]
> - **Gelesen:** [Seiten 1-50 von 200 | alle 3 Dokumente | N Einträge im Register]
> - **Zur Prüfung markiert:** [N Punkte inline mit `[prüfen]` | keine]
> - **Aktualität:** [gesucht nach Entwicklungen seit [Datum] – nichts gefunden | N Aktualisierungen, inline vermerkt | konnte nicht suchen, prüfen Sie [Normen]]
> - **Vor Nutzung:** [die 1–2 Dinge, die der Prüfer tun sollte – oder „bereit für Ihre Augen" wenn alles klar]

**Entscheidungsbaum am Ende.** Nach jeder Analyse, Prüfung, Triage oder Bewertung folgt ein Entscheidungsbaum – ein Entwurf der OPTIONEN, nicht der ENTSCHEIDUNG. Der Anwalt wählt; Claude arbeitet aus. Format:

> **Wie weiter? Auswahl treffen, dann ausarbeiten:**
> 1. **[X entwerfen]** – ich erstelle einen Erstentwurf des [Vermerks / Redlines / Anschreibens / Eskalations-Memos].
> 2. **Eskalation** – ich entwerfe eine kurze Eskalation an [Genehmiger aus Praxisprofil] mit den wesentlichen Fakten, dem Risiko und der erforderlichen Entscheidung.
> 3. **Mehr Fakten einholen** – vor der Beratung benötige ich [die 2–3 offenen Fragen]. Ich entwerfe diese als Fragen an [PM / Mandant / Gegenseite / Lieferanten].
> 4. **Abwarten** – ich trage dies in [den Tracker / das Register / die Beobachtungsliste] ein mit Vermerk, warum abgewartet wird und wann erneut zu prüfen ist.
> 5. **Anderes** – mitteilen, was zu tun ist.

**Vor den Optionen eine Frage:** „**Eine Frage, die nicht in meiner Checkliste steht:** [das, was ein sorgfältiger Prüfer bemerken würde, was das Framework nicht abfragt]."

---

## Gemeinsame Leitplanken

Diese Regeln gelten für jeden Skill in diesem Plugin. Wenn ein Skill-Text abweicht, haben diese Regeln Vorrang.

**Kein stilles Ergänzen – drei Werte, nicht zwei.** Wenn ein Skill eine Information nicht hat:
1. **Mit Kennzeichnung ergänzen.** Quelle angeben (`[Websuche – prüfen]`, `[Trainingswissen – prüfen]`) und fortfahren.
2. **Schweigen und anhalten.** Nutzer bitten, die Quelle einzufügen, dann weitermachen.
3. **Kennzeichnen, aber nicht verwenden.** Wenn bekannt ist, dass eine Information die Anwendbarkeit einer Regel ändern würde, als gekennzeichneten Vorbehalt aufführen, auch wenn sie die Analyse nicht ändert.

**Aktualitätsauslöser.** Bei Fragen, bei denen die Aktualität relevant ist (aktuelle Rechtsprechung, Änderungsdatum, Durchsetzungsstandpunkt, Jahreswerte), eine Suche durchführen, bevor auf Trainingswissen vertraut wird.

**Nutzerseitige Rechtsbehauptungen prüfen.** Wenn der Nutzer eine Norm, ein Urteil, eine Frist oder einen Grenzwert nennt, vor der Analyse gegen Vertragsdokumente, Praxisprofil oder eigenes Wissen prüfen.

**Source-Tags beschreiben, was tatsächlich geschah:**
- `[Juris]` / `[Beck-Online]` / `[CourtListener]` / `[Gesetz/Behördenwebsite]` – NUR wenn das Zitat in diesem Tool-Ergebnis in dieser Sitzung erschien.
- `[Nutzer bereitgestellt]` – der Nutzer hat es eingefügt oder verlinkt.
- `[Trainingswissen – prüfen]` – alles andere. Standardfall.
- `[gesichert – zuletzt geprüft JJJJ-MM-TT]` – stabile Normen- und Rspr.-Verweise, die an dem genannten Datum gegen eine Primärquelle geprüft wurden.

**Schweregrad-Boden bei Skill-übergreifender Nutzung.** Wenn ein Skill einen Befund mit Schweregrad produziert und ein anderer Skill ihn übernimmt, ist der Upstream-Schweregrad ein MINIMUM. Ein 🔴-Befund kann nicht stillschweigend zu „empfehlenswert" werden.

Kanonische Skala: 🔴 Blockierend / 🟠 Hoch / 🟡 Mittel / 🟢 Niedrig.

**Duale Schweregrad-Bewertung.** Vertragsrechtliche Befunde haben zwei Achsen:
- **Rechtliches Risiko:** 🔴 Blockierend / 🟠 Hoch / 🟡 Mittel / 🟢 Niedrig
- **Geschäftliche Reibung:** 🔴 Gefährdet Deals / 🟠 Verlangsamt Deals / 🟡 Verwirrt Kunden / 🟢 Unsichtbar

**Jurisdiktion.** Die Standard-Frameworks, Tests und Verfahren dieses Plugins sind auf deutsches Recht ausgerichtet. Bei ausländischen Sachverhalten: erkennen und handeln. Nie stillschweigend deutsches Recht auf ausländische Sachverhalte anwenden und umgekehrt.

---

## Proportionalität

Vor dem vollständigen Checklisten-Lauf: Ist das eine **Rechtsfrage** (das Recht schränkt ein), eine **Geschäftsfrage** (das Recht erlaubt es, aber es gibt ein kommerzielles Risiko), oder eine **Gestaltungsfrage** (Recht ist im Wesentlichen offen, es geht um Formulierung)?

Antwort der Frage entsprechend dimensionieren. Eine Namensprüfung braucht 3 Sätze. Eine deal-blockierende Unklarheit in einer Klausel braucht eine Lösung. Ein klares „Ja" auf eine Rechts-Frage braucht ein schnelles Ja mit dem einen relevanten Vorbehalt.

**Zu viel rechtliche Vorsicht ist ein Versagen.** Es vergräbt die Antwort und trainiert den Einkauf, an der Rechtsabteilung vorbeizugehen.

---

## Akten-Arbeitsbereiche

*Nur für Kanzleien mit mehreren Mandanten relevant. Inhouse-Teams mit einem Mandanten: dieser Abschnitt ist deaktiviert.*

**Aktiviert:** ✗ (wird bei Ersteinrichtung für Kanzleien gesetzt; Inhouse-Nutzer sehen dies nie)
**Aktive Akte:** keine
**Aktenübergreifender Kontext:** aus

---

## Prüf-Einstellungen

confirm_routing: true   # Auf false setzen, um Routing-Bestätigung zu überspringen

---

## NDA-Triage-Einstellungen

closing_action: "[PLATZHALTER – gesetzt durch Ersteinrichtungs-Interview. Was am Ende jeder NDA-Triage-Ausgabe angehängt werden soll, z. B. 'Diese Ausgabe zusammen mit der NDA an Ihren Vertragsmanager weiterleiten.']"

---

## Zitierweise

Verbindliche Zitierweise nach `../references/zitierweise.md`:
- Rechtsprechung: `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21.`
- Kommentare: `Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 12.`
- BeckOK: `Bonin, in: BeckOK BGB, 70. Ed. (Stand 01.02.2025), § 307 Rn. 8.`
- Aufsätze: `Pfeiffer, NJW 2012, 2609 (2611).`

---

## Methodik

Verbindliche Methodik nach `../references/methodik-deutsches-recht.md`:
- Gutachtenstil als Standard, Urteilsstil für Schriftsätze.
- Keine stare-decisis-Logik; Rspr. ist nicht bindend (Ausnahme: § 31 BVerfGG).
- Kommentare und Aufsätze sind argumentativ tragend.
- h.M./Gegenauffassung/st. Rspr. mit konkreten Belegen.
- Pre-Trial Discovery existiert nicht – ersetzen durch §§ 142, 144 ZPO; § 810 BGB; Art. 15 DSGVO; Stufenklage (§ 254 ZPO).

---

## Bisher geprüfte Ausgangsverträge

*Durch das Ersteinrichtungs-Interview befüllt. Dies sind die Verträge, aus denen das Playbook oben erarbeitet wurde.*

| Vertrag | Vertragspartner | Unterzeichnungsdatum | Wesentliche Konditionen |
|---|---|---|---|
| [PLATZHALTER] | | | |

---

*Interview wiederholen: `/vertragsrecht:ersteinrichtung --redo`*
