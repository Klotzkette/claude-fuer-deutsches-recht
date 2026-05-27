---
name: stb-kaltstart-interview
description: "Kaltstart-Interview fuer das Steuerberater-Plugin um Praxisprofil zu befuellen. Anwendungsfall Erstinstallation oder Konfiguration enthaelt noch Platzhalter-Marker oder Re-Interview mit --redo oder Konnektoren-Pruefung mit --integrationen-pruefen. Erfragt Rolle Steuerberater Wirtschaftspruefer Bilanzbuchhalter Geschaeftsfuehrer Mandanten-Schwerpunkte KMU Freiberufler GmbH Buchhaltungs-System DATEV Lexware sevDesk Eskalationsstrukturen Schnittstelle Anwalt. Output Kanzlei-Konfigurationsprofil CLAUDE.md. Abgrenzung zu stb-bwa-sus-bilanz-pruefung mandatsbezogener Krisencheck."
---

# /steuerrecht-anwalt-und-berater:stb-kaltstart-interview

## Rechtliche Grundlagen (Orientierung für das Interview)

### Zentrale Normen
- **StBerG** § 3 (Befugnis), § 57 (Verschwiegenheit), § 64 (Vergütung)
- **AO** §§ 149 ff. (Erklärungspflichten), § 153 (Berichtigungspflicht), § 371 (Selbstanzeige)
- **HGB** §§ 238 ff. (Buchführungspflicht), §§ 264 ff. (Jahresabschluss)
- **InsO** §§ 17 19 (Insolvenzgründe), § 15a (Antragspflicht)
- **StaRUG** § 102 (Hinweispflichten bei drohender Insolvenz)

### Aktuelle Rechtsprechung
- BGH, Urt. v. 26.01.2017 - IX ZR 285/14, NJW 2017, 1104 Rn. 18 — Der Steuerberater verletzt seine Beratungspflichten, wenn er einen sich abzeichnenden Insolvenzgrund nicht meldet; er ist zu aktiver Warnung verpflichtet.
- BGH, Urt. v. 07.03.2013 - IX ZR 64/12, NJW 2013, 1944 Rn. 14 — Steuerbescheide, die der Steuerberater im Auftrag des Mandanten entgegennimmt, lösen Fristen aus; der Steuerberater ist für ordnungsgemäße Weiterleitung und Fristwahrung verantwortlich.
- BFH, Urt. v. 18.06.2015 - VI R 12/14, BStBl II 2015, 857 Rn. 12 — Der Steuerberater, der Steuererklärungen einreicht, haftet für deren inhaltliche Richtigkeit nach Maßgabe seiner Mandatspflichten; Haftungsausschluss durch klare Mandatsabgrenzung möglich.
- BGH, Urt. v. 14.07.2016 - IX ZR 291/14, NJW-RR 2016, 1394 Rn. 22 — Die Verpflichtung des Steuerberaters zur Belehrung über steuerliche Risiken gilt unabhängig davon, ob der Mandant danach fragt; bei erkennbarer steuerlicher Fehleinschätzung des Mandanten muss der Steuerberater aktiv warnen.

### Kommentarliteratur
- BeckOK StBerG/Gehre — Kommentar zum Steuerberatungsgesetz
- Tipke/Kruse, AO/FGO, § 153 Rn. 1-30 (Berichtigungspflicht bei Erklärungsfehlern)

## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (DATEV-Schnittstelle, Dokumentenspeicher, Mandanten-Portal, E-Mail). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `✓` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren.

---

## Kaltstart-Interview: Steuerberater-Werkzeuge

### 1. Wer nutzt dieses Plugin?

- **Rolle:** Steuerberater (§ 3 StBerG) / Wirtschaftsprüfer mit Steuerberatungsmandat / Bilanzbuchhalter / Geschäftsleiter (Eigenbilanzierung) / Finanzleiter?
- **Anwaltlicher / steuerlicher Ansprechpartner** (bei Nicht-Steuerberatern): Name, Kanzlei
- **Berufsverband:** DStV, BStBK, IDW, sonstiger oder keiner
- **Kammer-Zugehörigkeit:** Steuerberaterkammer Bezirk

### 2. Mandanten-Struktur

- **Mandanten-Typen:** KMU / Freiberufler / GmbH / GmbH & Co. KG / Einzelunternehmer / Vereine / sonstige
- **Branchen-Schwerpunkte** (falls vorhanden): Bau / Handel / Dienstleistung / Healthcare / Immobilien / Gastronomie
- **Anzahl aktiver Mandanten:** N (orientiert die Skalierung der Werkzeuge)
- **Typische Umsatzgröße der Mandanten:** Bandbreite (für BWA- und Liquiditätsplanungs-Kalibrierung)

### 3. Buchhaltungs- und Bilanzierungssystem

- **Buchhaltungs-Software:** DATEV / Lexware / sevDesk / Addison / SAP / sonstige
- **Bilanzierungsstandard:** HGB / IFRS (selten bei KMU) / Mischung
- **Bilanzerstellung:** durch Steuerberater (für Mandanten) / durch Mandanten selbst (mit Plausibilisierung)

### 4. Liquiditätsplanung

- **Standard-Horizonte:** 3 / 6 / 12 Monate (Standard für Mandantenberatung) / 13-Wochen-Planung (Krise) / 21-Tage-Planung (drohende Zahlungsunfähigkeit, § 17 InsO)
- **Schwellenwert für Warnungen:** Liquiditätsgrad I, II, III nach Bilanz-Kennzahlen
- **Eskalation an Insolvenzberater / Sanierungsberater:** ab wann (z. B. < 7 Tage Liquidität)?

### 5. Berichtspflichten

- **Hauptverpflichtungen:**
  - Umsatzsteuer-Voranmeldung (§ 18 UStG): monatlich / quartalsweise
  - Jahresabschluss (§ 264 HGB, § 325 HGB): 12 Monate nach GJ-Ende für mittelgroße/große, 6 Monate für kleine GmbH
  - Lohnsteueranmeldung
  - E-Bilanz nach § 5b EStG
- **Hinweispflichten gegenüber Mandanten** (§ 102 StaRUG): bei drohender Insolvenz

### 6. Beratungstiefe

- **Reines Steuermandat:** ja / nein
- **Mit betriebswirtschaftlicher Beratung:** ja / nein
- **Mit Sanierungsberatung:** ja / nein (Hinweis: Sanierungsberatung jenseits Steuerberatung kann Rechtsdienstleistung sein — § 5 RDG beachten)

### 7. Standort

- **Bundesland:** [Bayern / NRW / etc.]
- **Praxistypus:** Einzelkanzlei / Sozietät / Partnerschaftsgesellschaft

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde
- Welche Skills jetzt sinnvoll als nächstes laufen können:
  - `/steuerrecht-anwalt-und-berater:stb-bwa-sus-bilanz-pruefung` — bei Plausibilisierung der laufenden BWA/SuSa/Bilanz
  - `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3-6-12-monate` — für klassische Liquiditätsplanung
  - `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3wochen` — bei akutem Liquiditätsengpass / drohender Zahlungsunfähigkeit
- Hinweis auf Mandatsgeheimnis (§ 57 StBerG, § 203 StGB)

## Rechtlicher Rahmen

- **StBerG** — Steuerberatungsgesetz: § 3 (Befugnis), § 5 (Vorbehaltene Tätigkeiten), § 57 (Verschwiegenheit), § 64 (Vergütung)
- **AO** — Abgabenordnung: Erklärungspflichten §§ 149 ff., Berichtigungspflicht § 153, Selbstanzeige § 371
- **UStG** — § 18 (Voranmeldung, Jahreserklärung)
- **EStG** — § 5b (E-Bilanz)
- **HGB** — §§ 238 ff. (Buchführungspflicht), §§ 264 ff. (Jahresabschluss), § 325 (Offenlegung)
- **InsO** — §§ 17, 18, 19, 15a (für Hinweispflicht bei Mandantenkrise)
- **StaRUG** — § 102 (Hinweispflichten der Geschäftsleiter)

## Hinweise

Dieses Plugin ist kein Ersatz für die individuelle Mandantenberatung durch einen Steuerberater. Es liefert Werkzeuge und Vorlagen zur Strukturierung der Arbeit. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen zu prüfen.
