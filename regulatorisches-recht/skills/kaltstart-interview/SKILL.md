---
name: kaltstart-interview
description: "Ersteinrichtung des Plugins für aufsichtsrechtliche Praxis. Laden, wenn das Praxisprofil noch nicht konfiguriert ist oder neu eingerichtet werden soll."
---

# Ersteinrichtung – Regulatorisches Recht

## Zweck

Dieser Skill konfiguriert das Plugin einmalig auf Ihre Praxis: Welche Behörden beobachten Sie? Welche Richtlinien haben Sie? Was ist für Sie wesentlich? Das Ergebnis ist ein befülltes Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md`, auf das alle anderen Skills zugreifen.

**Dieser Skill ist der einzige, der ohne befülltes Praxisprofil ausgeführt werden darf.** Alle anderen Skills stoppen und verweisen hierher, solange `[PLATZHALTER]`-Marker im Profil vorhanden sind.

## Eingaben

- Keine Vorbereitung erforderlich – der Skill führt Sie durch alles.
- Optional: Vorhandene Richtliniendokumente oder eine Übersicht der beobachteten Behörden vorab bereithalten.

## Ablauf

### Schritt 1 – Prüfung des Unternehmensprofils

```
Gibt es bereits ein Unternehmensprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md?
```

- **Ja:** Profil lesen, Informationen bestätigen lassen.
- **Nein:** Folgende Felder abfragen und in der Profildatei anlegen:
  - Name und Rechtsform
  - Hauptgeschäftstätigkeit und Aufsichtsrechtssegment (Bank, Zahlungsinstitut, Wertpapierfirma, Energieversorger, Pharmaunternehmen usw.)
  - Jurisdiktion(en): Deutschland, EU-weit, grenzüberschreitend
  - Risikopostur (konservativ / Standard / risikoaffin)
  - Wichtige Ansprechpartner (Compliance-Leiter, Chefjustitiar, externer Anwalt)

### Schritt 2 – Rollenklärung

```
Wer nutzt dieses Plugin?
```

Optionen zur Auswahl stellen:
1. Rechtsanwalt / Jurist (Anwalt-Arbeitsergebnisheader aktiv)
2. Nicht-Jurist mit Zugang zu einem Anwalt (Recherchenotizen-Header; anwaltlichen Ansprechpartner erfassen)
3. Nicht-Jurist ohne Anwaltszugang (Recherchenotizen-Header; Warnung bei folgenreichen Handlungen)

### Schritt 3 – Beobachtete Behörden

Dem Nutzer die folgende Liste vorlegen und um Auswahl sowie Erläuterung des Beobachtungsgrunds bitten:

| Behörde | Typischer Grund |
|---|---|
| BaFin | Finanzaufsicht (KWG, ZAG, WpHG, WpIG, GwG, KAGB) |
| Deutsche Bundesbank | CRR/KWG-Meldewesen, Offsite-Prüfungen |
| BMF | Steuerrecht (AO, UStG), BMF-Schreiben |
| Bundesnetzagentur (BNetzA) | Energie (EnWG), Telekommunikation (TKG) |
| BMG | Heilmittel (HeilMWerbG, AMG, MPG) |
| EBA | CRR/CRD-Leitlinien, DORA-Durchführungsstandards |
| ESMA | MiFID II/MiFIR, EMIR, Wertpapierrecht |
| EZB / SSM | Bedeutende Institute, SREP |
| BAFA | Außenwirtschaft, Sanktionen |
| BMJ | Änderungen des bürgerlichen und Strafrechts |

Für jede ausgewählte Behörde erfassen:
- Zuständigkeit / Beobachtungsgrund
- Feed-Quelle (RSS-URL, E-Mail-Verteiler, manuell)

### Schritt 4 – Richtlinienbibliothek

```
Haben Sie eine Richtlinienbibliothek, die gegen neue Regulierungsakte geprüft werden soll?
```

- **Ja:** Speicherort (Drive-Ordner, SharePoint-URL, lokaler Pfad) erfassen; verfügbare Richtlinien auflisten lassen (Name, Datei, letzte Aktualisierung, Verantwortlicher).
- **Nein:** Vermerken, dass Diffs gegen manuell eingefügten Inhalt laufen.

### Schritt 5 – Materialitätsschwelle

Die drei Stufen mit praxisbezogenen Beispielen kalibrieren:

**Immer wesentlich (sofort handeln):**
- Neue aufsichtsrechtliche Pflicht mit Frist im eigenen Segment
- BaFin-Anordnung oder -Maßnahme gegen das eigene Institut oder einen Wettbewerber im selben Sektor
- Gesetzesänderung mit Umsetzungsfrist < 6 Monate

**Prüfenswert (beurteilen und entscheiden):**
- BaFin-Konsultationsentwurf / EBA-Konsultationspapier
- BaFin-Rundschreiben ohne unmittelbaren Handlungsbedarf
- BMF-Schreiben zu steuerlichen Zweifelsfragen

**Zur Kenntnis (Notiz, kein Handlungsbedarf):**
- Rede eines BaFin-Vorstands ohne Ankündigung
- EBA-Diskussionspapier ohne Umsetzungsfrist
- Akademischer Kommentar

### Schritt 6 – Gap-Response-Prozess

Erfassen:
- Wer triagiert Regulierungsänderungen?
- Wer verantwortet Richtlinienaktualisierungen?
- Wie werden Gaps erfasst (Ticketsystem, Tabellenkalkulation, Confluence-Seite)?
- Eskalationsweg bei wesentlichen Lücken mit Frist

### Schritt 7 – Feed-Konfiguration

Für jede ausgewählte Behörde erfassen:
- Feed-URL oder E-Mail-Abonnement
- Prüfrhythmus (täglich / wöchentlich)

Hinweis: Folgende Feeds sind öffentlich zugänglich:
- BaFin-Newsroom: `https://www.bafin.de/SiteGlobals/Forms/Suche/Servicesuche_Formular.html?input_=6073958`
- EUR-Lex: Über `eur-lex.europa.eu/oj/direct-access.html`
- Bundesgesetzblatt: `https://www.bgbl.de` (Abonnement empfohlen)
- ESMA: `https://www.esma.europa.eu/press-news/esma-news`
- EBA: `https://www.eba.europa.eu/news-press/news`

### Schritt 8 – Mandat-Workspaces (nur Kanzleibetrieb)

```
Beraten Sie mehrere externe Mandanten (Kanzlei) oder sind Sie für ein Unternehmen tätig (Inhouse)?
```

- **Kanzlei:** Matter-Workspaces aktivieren; Isolation erläutern (mandantsübergreifender Kontext standardmäßig deaktiviert).
- **Inhouse:** Matter-Workspaces deaktiviert; Praxisprofil gilt für das gesamte Unternehmen.

### Schritt 9 – Zusammenfassung und Schreiben

Die erfassten Informationen als befülltes Praxisprofil zusammenfassen, dem Nutzer zur Bestätigung vorlegen und dann in `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/CLAUDE.md` schreiben.

Abschließend melden:
```
Einrichtung abgeschlossen. Folgende Skills stehen jetzt zur Verfügung:
- /regulatorisches-recht:aufsichts-feed-monitor – Feeds jetzt prüfen
- /regulatorisches-recht:richtlinien-vergleich – Diff gegen Ihre Richtlinienbibliothek
- /regulatorisches-recht:luecken – Offene Lücken anzeigen
- /regulatorisches-recht:stellungnahmen – Konsultationsbeiträge verwalten
- /regulatorisches-recht:richtlinien-neufassung – Richtlinienneufassung
```

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen dieses Skills:
- § 43a Abs. 2 BRAO (Mandantengeheimnis)
- § 203 StGB (Anwaltsgeheimnis)
- BORA §§ 2, 6 (Berufspflichten)

## Ausgabeformat

- Interaktives Gesprächsformat (Frage → Antwort → nächste Frage)
- Abschließend: Übersichts-Tabelle des erstellten Profils
- Schreiben in CLAUDE.md, keine separate Ausgabedatei

## Beispiel

**Eingabe:** `/regulatorisches-recht:kaltstart-interview`

**Ausgabe (Auszug):**
```
Willkommen bei der Ersteinrichtung des Plugins Regulatorisches Recht.

Ich richte das Plugin auf Ihre Praxis aus. Dazu stelle ich Ihnen einige Fragen.
Haben Sie bereits ein allgemeines Unternehmensprofil? (ja/nein)

[Nutzer: nein]

Gut, wir legen es gemeinsam an. Wie lautet der Name Ihres Unternehmens / Ihrer Kanzlei?
...
```

Nach Abschluss:
```
Praxisprofil wurde gespeichert. Zusammenfassung:

| Feld | Wert |
|---|---|
| Unternehmen | Musterbank AG |
| Segment | Kreditinstitut (KWG § 1) |
| Beobachtete Behörden | BaFin, Bundesbank, EBA |
| Richtlinienbibliothek | SharePoint: /compliance/richtlinien |
| Materialitätsschwelle | Neue Pflicht mit Frist < 6 Monate → sofort |
| Prüfrhythmus | Täglich |
```

## Risiken / typische Fehler

- **Unvollständige Behördenliste:** Wird `BNetzA` vergessen und das Unternehmen betreibt eine regulierte Energieinfrastruktur, laufen alle Diff-Analysen ins Leere. Explizit nach Nebenaktivitäten fragen.
- **Falsche Rollenauswahl:** Wenn ein Nicht-Jurist das Plugin als „Rechtsanwalt" konfiguriert, fehlt der Hinweis auf erforderliche Anwaltsprüfung. Bei Zweifeln zum nicht-juristischen Modus default.
- **Materialitätsschwelle zu niedrig gesetzt:** Führt zu Alert-Flut; jeder Feed-Eintrag wird als wesentlich markiert. Lieber hoch einsetzen und nach 2 Wochen nachjustieren.
- **Keine Richtlinienbibliothek verbunden:** Policy-Diff und Gap-Analyse laufen gegen eingefügten Inhalt; qualitativ deutlich schlechter als gegen indizierte Dokumente.
