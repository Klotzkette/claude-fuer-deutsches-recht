# 14 — Redline-Workflow: Word Track Changes mit Gegenseite

**AZ:** MR-2026-DR-0717
**Datum:** 20. August 2026
**Bearbeiter:** Senior Associate Dr. (iur.) Mira Pohlmann

---

## Workflow-Beschreibung

Der Redline-Workflow zwischen Roosendaal Birkenhainer Partners mbB und Schaefer Schoeneberg Stoll mbB laeuft ausschliesslich ueber Microsoft Word mit der eingebauten Track-Changes-Funktion (Aenderungen verfolgen). Dieses Aktenstueck beschreibt das vereinbarte Protokoll und haelt Probleme aus dem Redline-Austausch zu SPA v3 vs. v4 fest.

---

## Vereinbartes Protokoll (Redline Protocol)

### Grundregeln (vereinbart per E-Mail vom 08.08.2026)

1. **Dateiformat:** Ausschliesslich .docx (kein PDF, kein RTF). Kein Passwortschutz.
2. **Track Changes:** Alle Aenderungen als nachverfolgte Aenderungen (Strg+Umschalt+E); keine direkte Textaenderung ohne Markierung.
3. **Kommentare:** Offene Punkte als Word-Kommentar (Einfuegen > Kommentar); Format: "[Partei — Datum] Kommentartext"
4. **Farben:** Roosendaal Birkenhainer = Blau; Schaefer Schoeneberg = Rot (automatische Zuweisung per Nutzer-Account, Anweisung an Kanzleipersonal: immer unter dem eigenen Kanzlei-Windows-Login arbeiten)
5. **Dateiname-Konvention:** SPA_Volkenrath_[Version]_[Kuerzel-Einsender]_[Datum].docx — Beispiel: SPA_Volkenrath_v3_SSS_20260908.docx
6. **Uebermittlung:** Verschluesselt per E-Mail oder ueber gesicherten Datentransfer-Link; kein Versand ueber persoenliche E-Mail-Accounts
7. **Acceptance Protocol vor Rueckversand:** Niemals Track Changes akzeptieren, bevor nicht vollstaendiger interner Review abgeschlossen; Antwortversion behaelt alle fremden Track Changes als sichtbare Aenderungen

---

## Typische Fehler und deren Vermeidung

| Fehler | Folge | Vermeidung |
|---|---|---|
| Track Changes versehentlich akzeptiert | Verlust des Redlines; unklar welche Positionen veraendert | Immer Kopie des Eingangs-Redlines archivieren bevor Bearbeitung |
| Falscher Nutzer-Account | Aenderungen in falscher Farbe | Nutzer-Account vor Bearbeitung pruefen (Word > Optionen > Benutzerinfo) |
| Kommentare einer Partei geloescht statt beantwortet | Informationsverlust; Gegenseite merkt nicht, dass Kommentar adressiert wurde | Kommentare nur per "Antworten"-Funktion schliessen, nie loeschen |
| Direkte Textaenderung ohne Track Change | "Stealth Edit" — kann als Vertrauensbruch gewertet werden | Track Changes immer aktiviert lassen waehrend Drafting |
| Metadaten nicht entfernt bei Abgabe an Notar | Notar sieht interne Diskussion und Kommentare | Notarfassung: Track Changes akzeptieren, Kommentare loeschen, Metadaten bereinigen |

---

## Redline v3 vs. v4: Besondere Probleme

### Problem 1 — "Ghosted" Track Changes

In SPA v3 (Roosendaal-Fassung) fanden sich nach Versand an Gegenseite Track-Changes-Markierungen aus einer alten Version (SPA v1 internem Entwurf), die durch fehlerhaftes Dokument-Zusammenfuehren wieder auftauchten.

**Folge:** Schaefer Schoeneberg Stoll sah interne Kommentare der Verkaeuferkanzlei aus der Fruehphase (u.a. interne Bewertung zum Knowledge Qualifier).

**Lehre:** Vor externem Versand immer: Strg+A, dann alle Markierungen pruefen via "Alle Aenderungen anzeigen" — oder Dokument frisch aus clean version erstellen.

### Problem 2 — Kollidierender Tracked Text in Tabellen

In Art. 6-Tabelle (Indemnification-Uebersicht) kollidierten Track-Changes-Formatierungen in Tabellenzellen, sodass Text unleserlich wurde (Word-Bug mit Tabellen und eingeschalteten Revisionsmarkierungen).

**Loesung:** Tabellen in Redlines als Screenshot einbetten (Bild, nicht editierbares Objekt); daneben leere Kommentar-Zelle fuer Klaerungen.

---

## Archivierungsregeln

Alle Redline-Versionen werden im Kanzlei-DMS (Anwalts-Software) unter AZ MR-2026-DR-0717 archiviert:

| Version | Dateiname (DMS) | Datum |
|---|---|---|
| Draft 1 (Roosendaal) | SPA_v1_RBP_20260418.docx | 18.04.2026 |
| Markup v1 (Gegenseite) | SPA_v1_SSS_Markup_20260714.docx | 14.07.2026 |
| Draft 2 (Roosendaal) | SPA_v2_RBP_20260808.docx | 08.08.2026 |
| Markup v2 (Gegenseite) | SPA_v2_SSS_Markup_20260908.docx | 08.09.2026 |
| Draft 3 (Roosendaal) | SPA_v3_RBP_20260925.docx | 25.09.2026 |
| Draft 4 / Final (Roosendaal) | SPA_v4_RBP_20261010.docx | 10.10.2026 |
