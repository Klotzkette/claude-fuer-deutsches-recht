---
name: gegenseite-status-mahnbescheid-mahnschreiben
description: "Gegenseite Status Mahnbescheid Mahnschreiben: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gegenseite Status Mahnbescheid Mahnschreiben

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gegenseite Status Mahnbescheid Mahnschreiben** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gegenseite-status` | Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: §§ 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz, Sicherheitsleistung. Output: Statusbericht Gegenseite. Abgrenzung: nicht Streitwert oder Anspruchstabelle. |
| `mahnbescheid` | Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: §§ 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Schuldners. Output: Mahnbescheidsantrag-Entwurf. Abgrenzung: nicht Klageschrift § 253 ZPO. |
| `mahnschreiben-aufnahme` | Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empfehlung Reaktion. Abgrenzung: nicht eigenes Mahnschreiben erstellen. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Gegenseite Status Mahnbescheid Mahnschreiben**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gegenseite-status`

**Fokus:** Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: §§ 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz, Sicherheitsleistung. Output: Statusbericht Gegenseite. Abgrenzung: nicht Streitwert oder Anspruchstabelle.

# Statusabfrage Externe Bevollmächtigte

## Zweck

Jede Woche dieselbe Statusanfrage an externe Bevollmächtigte für 5–15 Prozessmandate zu schreiben ist mechanische Routinearbeit. Inhalt je Mandat ist wiederkehrend (Stand, ausstehende Entscheidungen, Budgetkontrolle). Die Adressaten sind gleich (Partneranwalt der mandatierten Sozietät). Der Ton ist einheitlich (gemäß der im Kanzleiprofil hinterlegten Direktive für externe Bevollmächtigte). Dieser Skill erstellt alle Entwürfe; der Anwalt prüft und versendet.

## Eingaben

- **Mandatsprotokoll `_log.yaml`**: Filterquelle und Feldquelle
- **`akte.md` und `verlauf.md`** je Mandat: Mandatskontext und aktuelle Entwicklungen
- **Kanzleikonfiguration `CLAUDE.md`**: Direktive für externe Bevollmächtigte (Tonvorgabe), Unterzeichner, Budgethaltung
- **Flags** (optional): `--alle`, `--slug=[bezeichnung]`, `--kein-outlook`

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 4 BRAO** — Anwaltliche Fortbildungs- und Berichterstattungspflicht gegenüber dem Mandanten; regelmäßige Rückmeldung der externen Bevollmächtigten ist Teil der ordnungsgemäßen Mandatsführung.
- **§ 667 BGB** — Auskunftspflicht des Beauftragten; der externe Bevollmächtigte hat dem Auftraggeber auf Verlangen Auskunft zu erteilen; die wöchentliche Statusanfrage ist Ausfluss dieses Anspruchs.
- **§ 43a Abs. 2 BRAO** — Vertraulichkeit; die Statuskorrespondenz mit externen Bevollmächtigten ist durch die gemeinsame Verschwiegenheitspflicht geschützt.
- **§ 49b BRAO; §§ 2 ff. RVG** — Vergütung; Budgetanfragen und Kostenkontrollen im Statusschreiben orientieren sich am vereinbarten Honorar und etwaigen Vergütungsrahmen.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1: Mandate filtern

**Standardfilter:**

- `status != geschlossen`
- `externe_bevollmaechtigte.sozietaet != null` UND `externe_bevollmaechtigte.partner != null`
- Entweder: letzte Aktualisierung vor mehr als 10 Tagen ODER `nächste_frist` innerhalb von 21 Tagen

Übersprungen werden: Mandate mit Update in den letzten 10 Tagen (kein erneutes Anschreiben erforderlich) sowie Mandate ohne hinterlegte E-Mail-Adresse des externen Bevollmächtigten (Markdown-Entwurf wird trotzdem erstellt; Outlook-Entwurf nicht).

**Flags:**
- `--alle` → Entwurf für alle aktiven Mandate, unabhängig von der Aktualität
- `--slug=[bezeichnung]` → Entwurf nur für ein Mandat (Ad-hoc-Anfrage)
- `--kein-outlook` → kein Outlook-Entwurf, auch wenn MCP verfügbar

### Schritt 2: Je Mandat — E-Mail-Entwurf erstellen

Jede E-Mail folgt demselben Grundgerüst; Inhalt ist mandatsspezifisch.

**Betreff:** gemäß Kanzleidirektive (Fallback: `[Mandat: [Bezeichnung]] — Wöchentlicher Sachstand`)

**Rumpf-Gerüst:**

```
[Vorname des Partneranwalts],

[Ein einleitender Satz — natürlich, entspricht dem Kanzleiston.]

Kurze Rückmeldung zu [Mandatsbezeichnung] erbeten. Einige Punkte:

1. **Sachstand seit [Datum der letzten Aktualisierung aus verlauf.md]** — Was hat sich bewegt, was ist noch offen? Gab es Schriftsätze, Termine, Korrespondenz oder Telefonate seit unserem letzten Austausch?

2. **Bevorstehende Fristen** — Ich vermerke [nächste_frist aus Protokoll + etwaige Fristen aus akte.md]. Bitte Abdeckungsplan bestätigen und ggf. weitere Termine mitteilen.

3. **Ausstehende Entscheidungen** — [offene Fragen aus akte.md, die externen Input erfordern; entfällt, falls keine vorhanden — umnummerieren]

4. **Budget** — [monatlich / quartalsweise / auf Anfrage gemäß Kanzleikonfiguration]. Wo stehen wir gegenüber [Budgetrahmen aus akte.md]? Gibt es Abweichungen?

[Falls wesentlich und relevant: 5. Konkrete Bitte — z. B. "Bitte Entwurf des Schriftsatzes vor [Datum] übersenden" — aus offenen Punkten in akte.md.]

[Grußformel — Name, Funktion, Kontakt. Aus Kanzleikonfiguration.]
```

Ton wird der Kanzleidirektive angepasst — einige Kanzleien schreiben förmlich, andere per Vorname und Stichpunkte. Die Direktive hat Vorrang.

### Schritt 3: Ausgabe erstellen

### Schritt 4: Abschicken-Schranke

Jedem Entwurf wird folgender Hinweis angefügt (vor dem Versenden entfernen):

> Dies ist ein Entwurf zur anwaltlichen Prüfung vor dem Versand an externe Bevollmächtigte. Prüfen Sie auf privilegierte Inhalte, die nicht aus dem Mandatsverhältnis herausgegeben werden sollten, sachliche Richtigkeit, Ton und Budgethaltung. Auch routinemäßige Wochenanfragen können Strategie, Positionierungen oder unbeabsichtigte Zugeständnisse enthalten.

## Ausgabeformat

### Markdown-Entwürfe

Datei: `gegenseite-status/[JJJJ-MM-TT]/[slug].md`

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

# [Mandatsbezeichnung] — Statusanfrage externe Bevollmächtigte — [JJJJ-MM-TT]

**An:** [externe_bevollmaechtigte.email] ([Partner], [Sozietät])
**Von:** [Unterzeichner Name/E-Mail aus Kanzleikonfiguration]
**Betreff:** [Betreffzeile]

> Der Arbeitsergebnis-Kopf oben gilt für diesen internen Vermerk. Der ausgehende E-Mail-Text unten geht an externe Bevollmächtigte in einem Mandatsverhältnis, das selbst durch Verschwiegenheit (§ 43a Abs. 2 BRAO) geschützt ist — Vertraulichkeitskennzeichnung gemäß Kanzleikonfiguration auf der versendeten E-Mail anbringen (typisch: "Vertraulich — Anwaltskorrespondenz / Mandatsgeheimnis").

---

[Rumpf gemäß Gerüst]
```

### Outlook-Entwürfe (falls MCP verfügbar)

Falls die Outlook-MCP-Integration authentifiziert ist:

- Je Mandat wird ein Entwurf im Outlook-Postfach (Ordner "Entwürfe") angelegt mit `an`, `von`, `betreff` und `text`
- Der Entwurf liegt montags zur Prüfung bereit
- Falls die MCP-Integration nicht verfügbar oder fehlerhaft ist: Rückfall auf Markdown und Hinweis an den Nutzer

### Laufergebnis-Zusammenfassung

Nach Verarbeitung aller Mandate: `gegenseite-status/[JJJJ-MM-TT]/_zusammenfassung.md`

```markdown
# Statusanfrage Externe Bevollmächtigte — Lauf [JJJJ-MM-TT]

**Mandate verarbeitet:** [N]
**Entwürfe erstellt:** [N]
**Outlook-Entwürfe:** [erstellt / übersprungen — Grund]

## Entwurf erstellt für

| Mandat | Externer Partner | Zuletzt aktualisiert | Grund der Aufnahme |
|---|---|---|---|
| [slug] | [Partner] | [Datum] | [veraltet / bevorstehende Frist / --alle / --slug] |

## Übersprungen

| Mandat | Grund |
|---|---|
| [slug] | aktuelles Update (zuletzt bearbeitet [Datum]) |
| [slug] | keine E-Mail des externen Bevollmächtigten im Protokoll — nachtragen mit `/mandat-update [slug]` |

## Auffälligkeiten

- Mandate ohne externe Bevollmächtigte: [Liste — bei hohem/kritischem Risiko gesondert markiert]
- Mandate mit externen Bevollmächtigten, aber ohne E-Mail-Adresse: [Liste]
```

## Beispiel

**Sachverhalt:** Mandat `bauer-ag-berufung-2025`, OLG Hamburg. Letztes Update vor 14 Tagen. Nächste Frist: Berufungserwiderung in 18 Tagen. Externer Partner: RA Dr. Schneider, Schneider & Partner.

**Ergebnis:** Entwurf mit Statusanfrage zu eingereichten Schriftsätzen seit letztem Austausch, Bestätigung der Berufungserwiderungsfrist, Budget-Abfrage gemäß Quartals-Direktive. Gespeichert unter `gegenseite-status/2025-05-12/bauer-ag-berufung-2025.md`.

## Risiken und typische Fehler

- **Vertraulichkeit:** Die Statuskorrespondenz mit externen Bevollmächtigten ist durch § 43a Abs. 2 BRAO geschützt; Entwürfe nicht an Personen außerhalb des Mandatskreises weitergeben.
- **Nicht geprüfte Entwürfe versenden:** Auch kurze Statusanfragen können strategische Hinweise, Budgetkonzessionen oder unbeabsichtigte Zugaben enthalten.
- **Veraltete Kontaktdaten:** Falls die E-Mail des externen Partners nicht im Protokoll hinterlegt ist, wird kein Outlook-Entwurf angelegt; der Nutzer erhält einen Hinweis, die Daten nachzupflegen.
- **Mandatsübergreifende Abfrage:** Nur bei aktivem `Mandatsübergreifender Kontext: an` in der Kanzleikonfiguration darf das System mandatsübergreifend lesen.

## Quellenpflicht

- Gesetzestexte: §§ 43a, 49b BRAO; §§ 2 ff. RVG; § 667 BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 2. `mahnbescheid`

**Fokus:** Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: §§ 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Schuldners. Output: Mahnbescheidsantrag-Entwurf. Abgrenzung: nicht Klageschrift § 253 ZPO.

# Mahnverfahren – §§ 688 ff. ZPO

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Für den operativen Mahnantrag (Barcode-Datensatz, zentrales Mahnportal, EGVP/beA-Übermittlung) und
den Übergang zum Vollstreckungsbescheid samt Klausel und Zustellung lädt das freistehende Plugin
`zwangsvollstreckung` die Skills `zv-mahnbescheid-online` und `zv-vollstreckungsbescheid-folge`.
Dieser Skill liefert die dogmatische Grundlage und Strategie; das Plugin liefert das fertige
Formularpaket.

## Zweck

Dieser Skill begleitet das gerichtliche Mahnverfahren als kostengünstiges und schnelles
Verfahren zur Titulierung unstreitiger Geldforderungen. Anwendungsfelder: Forderungseinzug
bei Zahlungsverzug (Kauf-, Werk-, Darlehensverträge), Rückforderungsansprüche, titulierter
Verzugszinsanspruch. Der Skill deckt den gesamten Ablauf ab: Mahnantrag → Widerspruch →
Abgabe ins streitige Verfahren oder Vollstreckungsbescheid → Einspruch → Vollstreckung.

## Eingaben

Das Modell benötigt:

1. **Forderungsdetails**: Hauptforderung (Betrag, Entstehungsgrund), Zinsen (Verzugszinsen
 § 288 BGB; bei Verbraucher 5 % über Basiszinssatz, bei Unternehmer 9 % über Basiszinssatz),
 Mahnkosten, Auslagen
2. **Parteien**: Name, Anschrift, Rechtsform von Antragsteller und Antragsgegner
3. **Zuständigkeit**: Wohnsitz/Sitz des Antragsgegners → zuständiges Mahngericht (§ 689 ZPO)
4. **Aktuelle Situation**: Liegt bereits ein Mahnbescheid vor? Wurde Widerspruch eingelegt?
 Ist Vollstreckungsbescheid beantragt?
5. **Verjährungsstand**: Wann ist die Forderung fällig geworden? Verjährung droht?

## Rechtlicher Rahmen

### Normen

- **§ 688 ZPO** – Zulässigkeit des Mahnverfahrens (nur Geldforderungen; keine bedingten
 Forderungen; nicht gegen unbekannte Erben)
- **§ 689 ZPO** – Zuständigkeit (zentrale Mahngerichte der Länder; in Bayern: AG Coburg)
- **§ 690 ZPO** – Inhalt des Mahnantrags (Pflichtangaben: Parteien, Forderung, Zinsen,
 Entstehungsgrund kurz bezeichnet)
- **§ 692 ZPO** – Erlass des Mahnbescheids ohne Sachprüfung
- **§ 694 ZPO** – Widerspruch gegen den Mahnbescheid (binnen 2 Wochen ab Zustellung)
- **§ 696 ZPO** – Abgabe an das Streitgericht nach Widerspruch
- **§ 699 ZPO** – Antrag auf Vollstreckungsbescheid (nach Ablauf der Widerspruchsfrist oder
 nach Nicht-Einlegung des Widerspruchs; max. 6 Monate nach Zustellung des Mahnbescheids)
- **§ 700 ZPO** – Einspruch gegen den Vollstreckungsbescheid (2 Wochen ab Zustellung;
 § 700 Abs. 1 ZPO: VB steht einem Versäumnisurteil gleich)
- **§ 701 ZPO** – Weiteres Verfahren nach Einspruch
- **§ 204 Abs. 1 Nr. 3 BGB** – Verjährungshemmung durch Mahnantrag (ab Eingang beim Gericht)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 durch Mahnbescheid; § 204 Abs. 1 Nr. 3 BGB setzt voraus, dass die Forderung im Mahnantrag
 ausreichend individualisiert ist; pauschale Sammelbezeichnungen genügen nicht und hemmen
 die Verjährung nicht.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 anforderung im Mahnverfahren; der Entstehungsgrund muss so bezeichnet sein, dass der
 Antragsgegner die Forderung zuordnen kann; Verweis auf "Lieferscheine" ohne Nummer
 unzureichend.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Zulässigkeitsprüfung** (§ 688 ZPO): Ist die Forderung eine bezifferte Geldforderung?
 Keine aufschiebende Bedingung? Kein Auslandsaufenthalt des Antragsgegners (§ 688 Abs. 2 ZPO)?
2. **Verjährungsprüfung** (§§ 195, 199 BGB): Verjährungsfrist bereits abgelaufen oder kurz
 vor Ablauf? → Sofortiger Mahnantrag zur Hemmung (§ 204 Abs. 1 Nr. 3 BGB).
3. **Mahnantrag** (§ 690 ZPO) über www.online-mahnantrag.de:
 - Pflichtangaben: Antragsteller/Gegner (vollständig), Forderungsbetrag, Entstehungsgrund
 (Vertragstyp + Datum), Zinsen (Fälligkeitsdatum + Zinssatz), Gerichtsgebühr (§ 12 GKG)
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Erlass und Zustellung** (§§ 692, 693 ZPO): Gericht erlässt MB ohne Sachprüfung; Zustellung
 an Antragsgegner; 2-Wochen-Frist für Widerspruch beginnt.
5. **Widerspruch** (§ 694 ZPO): Binnen 2 Wochen → Abgabe an Streitgericht (§ 696 ZPO);
 Antragsteller muss innerhalb 1 Monat Kostenvorschuss einzahlen, sonst Rücknahmefiktion.
6. **Kein Widerspruch** → Antrag auf Vollstreckungsbescheid (§ 699 ZPO) innerhalb 6 Monaten;
 VB wird zugestellt; Einspruchsfrist 2 Wochen (§ 700 ZPO).
7. **Einspruch gegen VB** (§ 700 ZPO): Verfahren wie nach Widerspruch; VB gilt als
 Versäumnisurteil (§ 700 Abs. 1 ZPO).
8. **Vollstreckung**: VB ohne Einspruch → Vollstreckungsklausel beantragen (§§ 724 ff. ZPO);
 Pfändung oder Forderungspfändung einleiten (→ Skill vollstreckung).

## Ausgabeformat

- **Checkliste** für den Mahnantrag (Pflichtangaben, Zinsen, Anlagen)
- **Mahnantragsentwurf** (kann direkt auf online-mahnantrag.de übertragen werden)
- **Rechtliches Memo** zur Verjährungshemmung und Individualisierung der Forderung
- **Widerspruchsschreiben** (falls Mandant Antragsgegner ist)

## Beispiel

**Sachverhalt**: Handwerksbetrieb H hat Malerarbeiten für Vermieter V erbracht und eine Rechnung
über EUR 4.850,00 (fällig 01.12.2024) gestellt. V zahlt nicht; ein außergerichtliches Mahnschreiben
blieb erfolglos.

**Prüfung (Urteilsstil)**:

Das Mahnverfahren ist statthaft (§ 688 Abs. 1 ZPO): Die Forderung ist auf Zahlung einer
bestimmten Geldsumme gerichtet; keine aufschiebende Bedingung; V hat Wohnsitz in Deutschland.

*Individualisierung (§ 690 Abs. 1 Nr. 3 ZPO)*: Als Entstehungsgrund ist einzutragen: "Werklohn
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(§ 288 Abs. 2 BGB, da V Unternehmer).

*Verjährung*: Die Forderung entstand 2024; Regelverjährung 3 Jahre (§ 195 BGB), Beginn
01.01.2025. Kein Handlungsbedarf, aber Mahnantrag hemmt Verjährung ab Eingang (§ 204 Abs. 1
Nr. 3 BGB), was vorsorglich zu nutzen ist.

## Risiken und typische Fehler

- **Unzureichende Individualisierung**: Verjährungshemmung tritt nicht ein; Vollstreckungsbescheid
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Versäumte 6-Monatsfrist** für VB-Antrag: Mahnbescheid verliert Wirkung; neues Verfahren
 erforderlich; Verjährungshemmung endet (§ 204 Abs. 2 BGB).
- **Falsche Zinsen**: § 288 Abs. 1 vs. Abs. 2 BGB (Verbraucher vs. Unternehmer);
 zu hoch angesetzte Zinsen führen zu Teilvollstreckungsschutz.
- **Auslands-Antragsgegner**: § 688 Abs. 2 Nr. 2 ZPO – Mahnverfahren unzulässig →
 Klage erforderlich.
- **Berufsrecht**: Mandantendaten (Forderungsunterlagen) nur in verschlüsselter Form
 übermitteln (§ 43a Abs. 2 BRAO, § 203 StGB).

## Quellenpflicht

Jede Aussage zu Zulässigkeit, Inhalt des Mahnantrags und Verjährungswirkung ist nach
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rn.). Kommentare mit Bearbeiter, Werk, Aufl., §, Rn. Keine allgemeinen Pauschalverweise.

---

<!-- AUDIT-HINWEIS 27.05.2026: Halluzinierte BGH-Zitate entfernt (NOT_FOUND oder WRONG_TOPIC gemaess dejure.org-Pruefung). Betroffene AZ siehe inline-Kommentare. Frontmatter unveraendert. -->

## 3. `mahnschreiben-aufnahme`

**Fokus:** Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empfehlung Reaktion. Abgrenzung: nicht eigenes Mahnschreiben erstellen.

# Mahnschreiben-Intake

## Triage — kläre vor dem Intake

1. **Forderungsart:** Kaufpreis, Werkverguetung, Schadensersatz, Darlehensrueckzahlung oder sonstiger Anspruch?
2. **Faelligkeit:** Ist die Forderung bereits fällig und durchsetzbar (§ 271 BGB)?
3. **Verjaehrung:** Ist die dreijährige Regelverjährung (§ 195 BGB) gewährt oder droht sie?
4. **BATNA:** Was ist die beste Alternative zum Mahnschreiben (gerichtliches Mahnverfahren, Klage, Verhandlung)?
5. **Vertraulichkeitsfilter:** Dürfen mandatsbezogene Daten in das eingesetzte KI-System eingespielt werden?

## Zentrale Normen
- § 271 BGB (Fälligkeit)
- § 286 BGB (Verzug — Mahnungserfordernis)
- § 288 BGB (Verzugszinsen)
- § 291 BGB (Prozesszinsen)
- § 195 BGB (Regelverjährung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Strukturierte Erfassung aller für ein Mahnschreiben oder eine vorgerichtliche Aufforderung notwendigen Informationen, bevor der Entwurf erstellt wird. Der Skill führt ein geordnetes Interview und schreibt die Antworten in `demand-letters/[slug]/intake.md`.

## Eingaben

- Neuer Slug oder vorhandenes Mandat (Slug)
- Optional: `--full` für vollständigen erweiterten Intake (inkl. BATNA, Prozesskostenrisiko, Streitwertschätzung)

## Ablauf

1. **Mandantenidentifikation:**
 - Vollständiger Name / Firma, Anschrift, Kontaktperson
 - Mandantentyp: Verbraucher (§ 13 BGB) oder Unternehmer (§ 14 BGB) – für Verzugszinsberechnung relevant (§ 288 Abs. 1 vs. 2 BGB)

2. **Schuldneridentifikation:**
 - Vollständiger Name / Firma, Anschrift, HRB-Nummer (bei Gesellschaften)
 - Zustellungsfähige Anschrift vorhanden? (für spätere Klagezustellung, § 253 Abs. 2 Nr. 1 ZPO)
 - Ist die Passivlegitimation des Schuldners geklärt? (z. B. bei Gesamtschuld § 421 BGB, Rechtsnachfolge, Konzernmutter)

3. **Sachverhaltserfassung:**
 - Wie kam das Schuldverhältnis zustande? (Vertragsurkunde vorhanden?)
 - Was wurde nicht geleistet oder schlecht geleistet?
 - Wann war Leistung fällig?
 - Hat der Mandant bereits gemahnt? (schriftlich / mündlich / konkludent – relevant für § 286 Abs. 1 BGB)
 - Gab es Reaktionen des Schuldners (Einwände, Aufrechnungen, Minderung)?

4. **Forderungserfassung:**
 - Hauptforderung (Betrag, Art, Rechtsgrundlage)
 - Nebenforderungen: Verzugszinsen (§ 288 BGB), vorgerichtliche Anwaltskosten (§ 13 RVG i. V. m. VV 2300), Schadensersatz (§§ 280, 281 BGB)
 - Fälligkeitsdatum und bisherige Mahnungen (mit Datum)
 - Offene Restforderung (nach Teilzahlungen)

5. **Hebel und Risiko (BATNA):**
 - Was ist die beste Alternative des Mandanten ohne Mahnschreiben?
 - Welche Risiken bestehen (Aufrechnung, Gegenansprüche, Insolvenzrisiko)?
 - Ist ein Güteantrag (§ 15a EGZPO) im zuständigen Bundesland Pflicht?
 - Empfiehlt sich ein Mahnbescheid (§§ 688 ff. ZPO) statt Mahnschreiben?

6. **Vertraulichkeitsfilter:**
 - Enthält der Sachverhalt vertrauliche Informationen Dritter, die nicht in das Schreiben dürfen?
 - Besteht Zeugnisverweigerungsrecht des Mandanten für bestimmte Tatsachen?

7. **Intake-Datei schreiben:** `demand-letters/[slug]/intake.md` mit allen Feldern befüllen. Fehlende Pflichtfelder markieren.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```yaml
# demand-letters/[slug]/intake.md
mandant:
 name: ""
 typ: "Unternehmer / Verbraucher"
 anschrift: ""
schuldner:
 name: ""
 anschrift: ""
 hrb: ""
 passivlegitimation_geklaert: true/false
schuldverhaeltnis:
 entstehungsgrund: ""
 vertrag_vorhanden: true/false
 anlage: ""
forderung:
 art: ""
 hauptbetrag: 0.00
 faelligkeit: ""
 bisherige_mahnungen: []
 verzugszinsen_p_a: "5% / 9% über Basiszinssatz"
 anwaltskosten: 0.00
anspruchsgrundlage: ""
fristen_geplant:
 fristsetzung_bis: ""
batna: ""
risiken: []
gueteantrag_erforderlich: false
vertraulichkeit_geprueft: true
```

## Risiken / typische Fehler

- **Fehlende Passivlegitimation:** Bei GmbH-Schuldner Handelsregisterauszug abrufen; Insolvenzantrag prüfen (InsO § 17 ff.) – Mahnung an insolventen Schuldner ist sinnlos.
- **Gesamtschuldner übersehen:** Bei mehreren Schuldnern (§ 421 BGB) alle mahnen, um Verjährungshemmung (§ 213 BGB) zu bewirken.
- **Verjährung prüfen:** Intake prüft automatisch die Regelverjährung (§§ 195, 199 BGB: 3 Jahre zum 31.12.); kürzere Sonderfristen (§ 438 BGB: 2 Jahre für Mängelansprüche; § 548 BGB: 6 Monate für Vermieter; § 195 ff. BGB) gesondert markieren.
- **Unterlassungsaufforderung ohne Vertragsstrafe:** Abmahnungen nach UWG, UrhG, MarkenG müssen eine Unterlassungs- und Verpflichtungserklärung mit Vertragsstrafeversprechen enthalten; fehlt dies, kann der Abgemahnte eine nicht der Kostenfolge des § 97a UrhG entsprechende Erklärung abgeben.
