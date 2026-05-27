---
name: insolvenzrecht-kaltstart-interview
description: "Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter / beratender Anwalt / Geschäftsleiter / Sanierungsberater / Wirtschaftsprüfer), typischen Verfahrensarten (Regelinsolvenz / Eigenverwaltung / Schutzschirm / StaRUG / Konzerninsolvenz), bevorzugten Gutachten-Standards (IDW S 6 / S 9 / S 11) und Eskalationsstrukturen. Lädt bei Erstinstallation oder wenn die Konfiguration noch [PLATZHALTER]-Marker enthält. Mit --redo für ein erneutes Interview, mit --integrationen-pruefen nur für eine Konnektoren-Prüfung."
---

# /insolvenzrecht:insolvenzrecht-kaltstart-interview

## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (Dokumentenspeicher, Forderungsanmeldung-Portal, Insolvenzbekanntmachungen-RSS, Buchhaltungs-MCP). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `✓` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren.

---

## Kaltstart-Interview: Insolvenzrecht

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Insolvenzverwalter (§ 56 InsO) / Sachwalter (§ 274 InsO) / Sanierungsmoderator (§ 94 StaRUG) / beratender Anwalt (Schuldner- oder Gläubigerseite) / Geschäftsleiter mit Antragspflicht (§ 15a InsO) / Sanierungsberater (außerhalb gerichtlicher Verfahren) / Wirtschaftsprüfer mit Insolvenzmandaten?
- **Anwaltlicher Ansprechpartner** (bei Nicht-Anwälten): Name, Kanzlei, Erreichbarkeit
- **Berufsverband:** VID (Verband Insolvenzverwalter), Gravenbrucher Kreis, DRSC, IDW, sonstige

### 2. Typische Mandate / Verfahren

- **Verfahrensarten:** Regelinsolvenz / Eigenverwaltung (§§ 270 ff. InsO) / Schutzschirmverfahren (§ 270d InsO) / StaRUG / Restrukturierungsbeauftragter / Konzerninsolvenzen / Verbraucherinsolvenz
- **Branchen-Schwerpunkte** (falls vorhanden): Baugewerbe / Handel / Dienstleistung / Industrie / Immobilien / Healthcare
- **Volumen** (für Sanierungsberater): typische Bilanzsumme der Mandanten

### 3. Gutachten- und Berichtsstandards

- **IDW S 6** (Sanierungskonzept): wird verwendet ja / nein
- **IDW S 9** (Anforderungen an Insolvenzpläne): ja / nein
- **IDW S 11** (Beurteilung Insolvenzeröffnungsgründe): ja / nein
- **Eigene Hausstandards:** zusätzliche Templates, Checklisten, Berichtsstrukturen

### 4. Zuständige Insolvenzgerichte

- **Hauptzuständigkeiten:** AG/LG nach Bezirk; bei Konzerninsolvenzen: § 3a InsO (Gruppen-Gerichtsstand)
- **Bekanntmachungen:** insolvenzbekanntmachungen.de — wird regelmäßig überwacht?

### 5. Antragspflicht-Prüfung

- **Wann konsultiert das Mandat / der Geschäftsleiter typischerweise:** schon bei drohender Zahlungsunfähigkeit (§ 18 InsO) / erst bei Zahlungsunfähigkeit (§ 17 InsO) / erst bei Überschuldung (§ 19 InsO)
- **Standard für Fortbestehensprognose:** 12 Monate (§ 19 Abs. 2 InsO) / Branchenstandard / einzelfallabhängig
- **3-Wochen-Frist (§ 15a InsO):** Eskalationspfad bei Annäherung

### 6. Vergütung

- **InsVV-Anwendung:** Regelvergütung nach §§ 1 ff. InsVV / Vergütungsvereinbarung mit Gericht
- **Honorarberatung:** Stundensatz / RVG / Pauschalen

### 7. Standort

- **Bundesland / Hauptgerichtsbezirk:** [Bayern / NRW / etc.]
- **Kanzleitypus:** Einzelkanzlei / Sozietät / Großkanzlei / Inhouse

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde
- Welche Skills jetzt sinnvoll als nächstes laufen können:
  - `/insolvenzrecht:zahlungsunfähigkeit-prüfung-17-inso` — bei Liquiditätsengpässen
  - `/insolvenzrecht:überschuldung-prüfung-19-inso` — bei bilanzieller Überschuldung mit Fortbestehensprognose
  - `/insolvenzrecht:antragspflicht-15a-inso` — bei drohender 3-Wochen-Frist
  - `/insolvenzrecht:gläubigerantrag-prüfung` — bei eingegangenem Gläubigerantrag
  - `/insolvenzrecht:liquiditätsvorschau-insolvenzrechtlich` — für 21-Tage-Liquiditätsstatus
- Hinweis auf Mandatsgeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB)

## Rechtlicher Rahmen

- **InsO** — Insolvenzordnung: §§ 15a, 17, 18, 19, 56, 270 ff. (Eigenverwaltung), 286 ff. (Restschuldbefreiung)
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz (seit 01.01.2021)
- **InsVV** — Insolvenzrechtliche Vergütungsverordnung
- **IDW-Standards:** S 6 (Sanierungskonzept), S 9 (Insolvenzplan), S 11 (Insolvenzeröffnungsgründe)
- **Maßgebliche Rspr.:** BGH IX. Zivilsenat (Insolvenz) und II. Zivilsenat (Gesellschaftsrecht/Geschäftsleiterhaftung)

## Hinweise

Dieses Plugin ersetzt keine anwaltliche Beratung. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen (Beck-Online, juris) zu prüfen. Insolvenzantragspflicht und Eröffnungsgründe sind hochkomplex; im Zweifel **immer** anwaltliche Begleitung.


## Rechtlicher Rahmen — Kaltstart-Orientierung

- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Erstpruefung: sofortige Klärung ob Fortbestehensprognose positiv; negativer Status loest Antragspflicht aus.
- BGH, Urt. v. 24.05.2005 — IX ZR 123/04, BGHZ 163, 134 — ZU-Schnelltest: 10%-Luecken-Formel im Kaltstart anwenden; 3-Wochen-Fenster erfassen.
- BGH, Urt. v. 15.03.2016 — II ZR 119/14, NJW 2016, 2493 — Haftungsrisiko GF: Kaltstart-Zeitpunkt ist haftungsrelevant; ab heute laeuft Uhr fuer § 15a, § 15b InsO.
- BGH, Urt. v. 06.05.2021 — IX ZR 72/20, NZI 2021, 631 — Krisenstadium und Pfad-Wahl: im Kaltstart sofort Krisenstadium einordnen (StaRUG vs. InsO vs. Sanierung) — Entscheidung hat Anfechtungs- und Haftungsfolgen.
