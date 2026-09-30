---
name: 21-bea-versandfertig-schriftsatz-anlagen
description: "Für eine fachlich freigegebene Endfassung mit Anlagen, die beA-versandfertig werden soll. Schützt Originale, bindet Hashes, Stempel, Namen und Fingerprint. Versendet nie selbst; erst grünes Paket geht an Skill 16."
---

# Schriftsatz und Anlagen beA-versandfertig machen

## Zweck und Anwendungsfall

Finalisiere einen entworfenen Schriftsatz samt Anlagen als kontrolliertes PDF-Paket. Ändere Anträge, Tatsachen oder Recht nie stillschweigend; ohne Endfassung zu Skill 14, 15 oder 17. Signatur, Übermittlung und Eingang übernimmt Skill 16 anwaltlich. Zustände: `NICHT_VERSANDFERTIG`, `FREIGABE_AUSSTEHEND`, `VERSANDFERTIG`; Grundlage: `../../references/bea-versandfertig.md`.

## Bedienmodus

Arbeite die Kontrollspur vollständig ab. Im Profi- oder Schnelllauf verdichte nur die Darstellung, nie Inventar, Hashbindung, Vierfachabgleich, Sichtprüfung, Freigabe oder Stopps. Liefere Arbeitskopf, Prüfbericht und genau einen nächsten Schritt.

## Erste Antwort

Die erste Antwort liefert Startkarte, SHA-256-Inventar und vollständig befüllte Anlagenmatrix. Nur fehlende Quellen, unauflösbare Bezugnahmen, Nummerierungs-/Hashkonflikte und Freigabe als Lücken nennen. Keine Theorie-, Menü- oder Werkzeugvorträge, höchstens drei echte Rückfragen. Hilfsskriptausfall manuell überbrücken; ohne grünen Prüflauf höchstens `FREIGABE_AUSSTEHEND`, nie `VERSANDFERTIG`.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Direkt mit dem referenziell geschlossenen, hashgebundenen `model_state` des kanonischen Heads starten; ausgelassene IDs nur über hostseitiges `retrieve_state_items` gegen denselben Head nachladen. Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel; Tabellen erst ab drei Vergleichswerten. Übergabe als belegtes Delta mit genau einem nächsten Skill. Fach-, Frist-, Freigabe-, CAS- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

Höchstens drei Fragen je Runde; nichts fragen, was aus Dateien hervorgeht.

- Kanzlei: Gericht, Aktenzeichen/Neueingang, Rolle, Schriftsatzart, Frist, letzte Anlage/Präfix, Hausstil, Stempel, verantwortende Person, Signaturweg und strukturierte `recipient_id`.
- Mandant oder sonstigen Dokumentenlieferanten nur zu fehlenden Belegen, Original-/Lesbarkeitsstatus, Rückseiten, Datum, Absender und Empfänger befragen.
- Nur die anwaltliche Freigabeperson entscheidet über Anlagenfolge, Freigabe und Signaturweg. Skill 21 paketiert; Skill 16 allein darf übermitteln.

## Harte Stopps

Setze **`NICHT_VERSANDFERTIG`**, wenn ein Punkt offen ist:

- Endfassung, Gericht/Neueingang, Parteirolle, Frist oder verantwortende Person unklar; Anlagenfolge nicht rekonstruiert.
- Genannte Anlage fehlt, Datei ohne Zuordnung oder Original unvollständig, unleserlich, verschlüsselt oder durch Konvertierung verändert.
- Stempel verdeckt Inhalt, eine Signatur würde verändert oder eine Datei-, Format-, Namens- oder Scriptprüfung meldet Fehler/Warnung.
- Hash weicht vom Auftrag ab, Manifest fehlt, Freigabe nennt anderen Fingerprint oder die anwaltliche Freigabe fehlt.

## Arbeitsordner

Nur in Kopien arbeiten:

```text
bea-paket/
├── original/      unveränderte Eingänge mit SHA-256
├── arbeit/        Konvertierung, OCR, Stempelkopien
├── versand/       die im beA auszuwählenden PDFs
└── kontrolle/     Verzeichnis, Hashes, Prüfbericht, Freigabe
```

Nie Quelldateien überschreiben. Nur `versand/` wird an Skill 16 übergeben.

## Ablauf / Checkliste

### 1. Startkarte, Originalschutz

Gib zuerst die Startkarte aus. Inventarisiere jede Quelle mit Herkunft, Format, Seitenzahl, Lesbarkeit, Signaturhinweis und SHA-256; kennzeichne Entwurf, Endfassung und Dubletten — Dateiname oder Änderungsdatum beweisen keine Endfassung. Nicht-PDF-Inputs in Arbeitskopien aufbereiten — der Paketbauer akzeptiert nur finale PDFs. Auftrag nach `../../assets/schemas/bea-paketauftrag.schema.json` befüllen; `approved_sha256` bindet die Haupt-PDF, `expected_sha256` die Anlage.

### 2. Schriftsatz lesen

Extrahiere Anlagenbezugnahmen mit Fundstelle, Verzeichnis, Beweisantritte, Vertragsdaten, FIN, Rückrufcode, Kaufpreis, Datum, Absender; markiere Widersprüche und korrigiere nichts ohne Freigabe.

### 3. Anlagenmatrix

Führe je Anlage: Bezeichnung (`K12`, `B4`), Schriftsatzfundstelle, Kurzinhalt, Original- und Versand-SHA-256, Seitenzahlen, Verarbeitung (Konvertierung, OCR, Stempel), Status mit Grund. Jede Bezugnahme braucht genau eine Anlage; jede Anlage eine Bezugnahme oder eine freigegebene andere Funktion.

### 4. Nummerierung

Klägerseite regelmäßig `K1` fortlaufend, Beklagtenseite `B1`; Folgeschriftsätze setzen die **zuletzt eingereichte** Nummer fort, nie die lokale Entwurfsnummer. Eingereichte Anlagen nie umnummerieren; Konvolute nur anwaltlich freigegeben; abweichende Konvention dokumentieren.

### 5. Paketauftrag

Der Auftrag bindet Vorgang, Rolle, Dokument, Frist, Verantwortung, Signaturweg, Anlagenfolge und Hauptdokument-Hash; je Anlage Nummer, Quell-Hash, Titel, Datum, Fundstelle und Stempelmodus. Signatur: qES oder einfache Signatur plus persönliche sichere Übermittlung derselben Person; beA-/EGVP-Angabe allein genügt nicht (`VIa ZR 1559/22`). Unbekannte Felder, Platzhalter, Doppelquellen/Hardlinks, Steuerzeichen und Nummernlücken sperren; höchstens 200 MB, je PDF 5.000 Seiten/14.400 Punkte je Achse; `already_stamped` umgeht nie die Prüfung.

Paket in neuem Zielordner erzeugen:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/tools/bea-paket-bauer.py" \
  bea-paketauftrag.json --output bea-paket
```

Der Paketbauer arbeitet atomar, überschreibt nichts und erzeugt alle vier Ordner samt Manifest, Prüfbericht und Freigabevorlage; Erststatus `FREIGABE_AUSSTEHEND`.

### 6. Versandkopien

Prüfe Original-, Arbeits- und Versandkopien visuell (Seiten, Orientierung, Farben, Unterschriften, Stempel, Lesbarkeit); OCR darf nur Suchtext ergänzen. Stempel bei Bedarf separat erzeugen:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/tools/bea-anlagenstempel.py" original/Kaufvertrag.pdf \
  --label "Anlage K12" --output arbeit/01_Anlage_K12_Kaufvertrag.pdf --audit kontrolle/K12_stempel_audit.json
```

Bei verdecktem Inhalt nach Freigabe `--pages cover`. Digital signierte Quellen nicht neu serialisieren; Deckblatt gesondert freigeben. Audit, Original und Ausgabe brauchen verschiedene Pfade; `--force` nur nach Zielprüfung; jede Stempel-PDF rendern und prüfen.

### 7. Benennung

Plugin-Hausstandard:

```text
00_K_2026-07-10_Replik_16_O_123_24.pdf
01_Anlage_K12_Kaufvertrag_2020-05-14.pdf
```

Nur ASCII, Ziffern, Unterstrich, Minus; ein Punkt vor `.pdf`; Ziel 80, absolut 90 Zeichen; keine Leerzeichen, Umlaute, `ß` oder nichtssagende Namen. Rollenpräfix am Hauptdokument, Anlagenpräfix an jeder Anlage; Sortiernummern mindestens zweistellig.

### 8. Vierfachabgleich

Prüfe automatisiert und manuell die Deckungsgleichheit von Bezugnahme, Stempel, Dateiname und Anlagenverzeichnis; zusätzlich das Hauptdokument gegen den freigegebenen Hash und jede Versanddatei gegen das Manifest. Im `versand/`-Ordner liegt genau ein Hauptdokument; eine nach Paketbau geänderte Datei entwertet Paket-Fingerprint und Freigabe.

### 9. Freigabe

Rendere alle PDFs; prüfe Inhalt, Folge, Lesbarkeit, Stempel und Fundstellen. Erst nach anwaltlicher Abnahme `kontrolle/freigabe.json` mit Name, sekundengenauem ISO-Zeitpunkt samt Zeitzone und sechs Bestätigungen erzeugen. Der Produktionszeitpunkt `created_at` ist an den Fingerprint gebunden; Zeitänderung entwertet die Freigabe, Zukunftsabweichung über fünf Minuten sperrt. Freigabe ist weder Signatur noch Versandnachweis.

### 10. Paketprüfung

```bash
python3 "$CLAUDE_PLUGIN_ROOT/tools/bea-paket-pruefer.py" bea-paket --role K \
  --anlagen-prefix K --start 12 --expected-az "16 O 123/24" --report bea-paket/kontrolle/bea-pruefbericht.json
```

Der Prüfer kontrolliert Struktur, Namen, Hardlinks, Folge, Auftrag/Manifest, Bezugnahmen, Zeiten, Fingerprint, Freigabe, Hashes, PDF-Grenzen, aktive/signierte Inhalte; ohne gepinnte `pypdf`-Tiefenprüfung bleibt die Freigabe gesperrt. Exitcodes: `0` `VERSANDFERTIG`, `2` `FREIGABE_AUSSTEHEND`, `1` gesperrt; visuelle, rechtliche und beA-Prüfung bleiben nötig.

### 11. Übergabe

Gib `VERSANDFERTIG` nur bei null Fehlern/Warnungen, Vierfachabgleich und anwaltlicher Freigabe aus. Der Completion-Candidate führt `versandfreigabe` exakt als `status,paket_fingerprint_sha256,freigabe_revision,recipient_id,connector_namespace,action_id`: Fachbearbeitung setzt Paket, aktuelle Revision und Empfänger; `connector_namespace` und `action_id` bleiben bis zur vertrauenswürdigen Host-Completion `null`. Der Host übernimmt die stabile Dispatcher-Namensdomäne `provider:environment:tenant`, erzeugt daraus mit Fall, Revision, Paket und Empfänger die Action-ID und publiziert per CAS gegen den kanonischen Head. Namespace-/Head-Drift sperrt; Skill 21 erfindet oder übernimmt diese Werte nie.

Übergabe an Skill 16: `versand/`, Gericht/Aktenzeichen/Rolle/Frist, Verantwortung, Signaturweg und Formnachweis; Dateiliste mit SHA-256/Gesamtgröße; Fingerprint, Anlagenverzeichnis, Manifest, Freigabe, Prüfbericht, `recipient_id`, `connector_namespace`, `action_id`; ausdrücklicher Hinweis: noch nicht versandt. Provider-, Environment- oder Tenant-Wechsel verlangt neue Skill-21-Revision und Action-ID.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Die anwaltlich freigegebene Argumentation samt Beweisbezug in ein integritätsgesichertes, widerspruchsfreies Versandpaket überführen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Bezugnahme, Anlage, Stempel, Dateiname, Reihenfolge und Hash stimmen überein; jede Warnung sperrt `VERSANDFERTIG`.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| Keine Dieselgate-Leitentscheidung einschlägig | Für Paketbildung, Anlagenstempel und Dateinamen sind §§ 130a, 130d ZPO, ERVV, aktuelle ERVB und die in references/bea-versandfertig.md dokumentierte ERV-Rechtsprechung maßgeblich. | Hinweis |
| BGH, Urt. v. 14.07.2026 - VIa ZR 946/22 | Signaturdatei, Prüfbericht und gerichtliche Eingangsbestätigung als zusammengehörige Kontrollspur erhalten; den bloßen Standardhinweis zur fehlenden Sperrabfrage nicht mit einer konkret fehlgeschlagenen Signaturprüfung verwechseln. | Amtlich geprüft |
| BGH, Urt. v. 18.06.2026 - VIa ZR 1559/22 | Nachricht, Schriftsatz, qES oder VHN und Eingangsbestätigung als einheitliche Beweiskette sichern; die beA-/EGVP-Bezeichnung allein genügt nicht. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Versandreife-Tabelle

Der strengste Befund bestimmt den Status.

| Befund | Status / Folge | Nächster Schritt |
| --- | --- | --- |
| Freigabe bindet den aktuellen Paket-Fingerprint, Prüfer meldet Exit 0 | `VERSANDFERTIG` — Abgleich, Hashbindung, Freigabe vollständig | Übergabe an Skill 16 |
| Technisch fehlerfrei, Freigabe fehlt oder nennt anderen Fingerprint | `FREIGABE_AUSSTEHEND` — Freigabe gilt nur für das geprüfte Paket | Anwaltliche Abnahme zum aktuellen Fingerprint |
| Bezugnahme ohne Anlage, Datei ohne Zuordnung, Anlagenfolge nicht rekonstruiert | `NICHT_VERSANDFERTIG` — Zuordnung ist Pflicht | Zuordnung und letzte Nummer klären; Lücke an Skill 14, 15 oder 17 |
| Stempel verdeckt Inhalt oder signierte Quelle würde neu serialisiert | `NICHT_VERSANDFERTIG` — Integrität vor Stempeloptik | `--pages cover` nach Freigabe oder Deckblatt |
| SHA-256 weicht vom Manifest ab, Datei nach Paketbau geändert, Namens-/Formatfehler | `NICHT_VERSANDFERTIG` — Fingerprint und Freigabe entwertet; jede Warnung sperrt | Paket neu bauen, prüfen, freigeben |
| Original unvollständig, unleserlich oder verschlüsselt | `NICHT_VERSANDFERTIG` — kein scheinbar vollständiges Paket | Bessere Originaldatei konkret anfordern |

### Baustein Freigabevermerk

1

[Name], Rechtsanwältin/Rechtsanwalt, gibt im Verfahren [Klagepartei] gegen [Hersteller], [Gericht], Az. [Aktenzeichen/Neueingang], den Schriftsatz [Schriftsatzart] vom [Datum TT.MM.JJJJ] mit den Anlagen [erste bis letzte Anlagennummer] zum beA-Versand frei.

2

Geprüft und bestätigt werden: die Endfassung des Hauptdokuments gegen den freigegebenen Hash [SHA-256-Wert]; der Vierfachabgleich aus Bezugnahme, Stempel, Dateiname, Anlagenverzeichnis; die Sichtkontrolle aller Versand-PDFs; die Anlagennummerierung ab [Anlagennummer]; Namens-, Format- und Größenvorgaben; die Übereinstimmung mit dem Manifest zum Fingerprint [Fingerprint-Wert].

3

Die Freigabe gilt nur für das Paket mit diesem Fingerprint; jede nachträgliche Änderung entwertet sie. Sie ist Kontrollnachweis und ersetzt weder Signatur noch Versand- oder Eingangsnachweis; Signatur und Übermittlung erfolgen durch [verantwortende Person] über Skill 16. [Ort], [Datum TT.MM.JJJJ], [hh:mm:ss] Uhr [Zeitzone]; [Name, Berufsbezeichnung].

## Quellenpflicht

Es gelten `../../references/bea-versandfertig.md`, `../../references/rechtsstand-2026-gesetzgebung.md`, §§ 130a, 130d ZPO, §§ 2, 5 ERVV und die am Versandtag aktuelle ERVB. NRW-Dateinamenshinweise sind Empfehlungen; der ASCII-/Unterstrich-Standard ist eine strengere interne Portabilitätsregel. Keine technische oder gerichtliche Vorgabe aus Modellwissen erfinden.

## Ausgabeformat

1. **Kontrollansicht**: Der `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt`; nie Bestandteil von Schriftsatz, Anlage oder Exportdatei.

2. **Fachprodukt**: Startkarte, Anlagenmatrix, Konfliktliste, Versanddateiliste mit Hashes, Prüfbericht, Freigabestatus; genau ein nächster Schritt: Skill 16 oder Fehlerbehebung.

## Beispiele

**Fortgesetzte Anlagenfolge:** Freigegebene Replik mit vier neuen Anlagen, zuletzt eingereicht K11: Startkarte, Inventar, Anlagenmatrix K12 bis K15; Übergabe an Skill 16 erst bei grünem Prüfbericht.

**Unvollständiger Scan:** Kaufvertrag ohne Unterschriften-Rückseite: `NICHT_VERSANDFERTIG`, fehlende Seite konkret benannt und angefordert.

**Freigabe zu altem Fingerprint:** Paket nach Nachstempelung neu gebaut, Freigabe vom Vortag: `FREIGABE_AUSSTEHEND`, vorbefüllter Freigabevermerk zum neuen Fingerprint.
