# 14 — Redline-Workflow: Word Track Changes mit Gegenseite

**AZ:** MR-2026-DR-0717
**Datum:** 20. August 2026
**Bearbeiter:** Senior Associate Dr. (iur.) Mira Pohlmann

---

## Workflow-Beschreibung

Der Redline-Workflow zwischen Roosendaal Birkenhainer Partners mbB und Schäfer Schoeneberg Stoll mbB läuft ausschliesslich über Microsoft Word mit der eingebauten Track-Changes-Funktion (Änderungen verfolgen). Dieses Aktenstück beschreibt das vereinbarte Protokoll und hält Probleme aus dem Redline-Austausch zu SPA v3 vs. v4 fest.

---

## Vereinbartes Protokoll (Redline Protocol)

### Grundregeln (vereinbart per E-Mail vom 08.08.2026)

1. **Dateiformat:** Ausschliesslich .docx (kein PDF, kein RTF). Kein Passwortschutz.
2. **Track Changes:** Alle Änderungen als nachverfolgte Änderungen (Strg+Umschalt+E); keine direkte Textänderung ohne Markierung.
3. **Kommentare:** Offene Punkte als Word-Kommentar (Einfügen > Kommentar); Format: "[Partei — Datum] Kommentartext"
4. **Farben:** Roosendaal Birkenhainer = Blau; Schäfer Schoeneberg = Rot (automatische Zuweisung per Nutzer-Account, Anweisung an Kanzleipersonal: immer unter dem eigenen Kanzlei-Windows-Login arbeiten)
5. **Dateiname-Konvention:** SPA_Volkenrath_[Version]_[Kürzel-Einsender]_[Datum].docx — Beispiel: SPA_Volkenrath_v3_SSS_20260908.docx
6. **Übermittlung:** Verschlüsselt per E-Mail oder über gesicherten Datentransfer-Link; kein Versand über persönliche E-Mail-Accounts
7. **Acceptance Protocol vor Rückversand:** Niemals Track Changes akzeptieren, bevor nicht vollständiger interner Review abgeschlossen; Antwortversion behält alle fremden Track Changes als sichtbare Änderungen

---

## Typische Fehler und deren Vermeidung

| Fehler | Folge | Vermeidung |
|---|---|---|
| Track Changes versehentlich akzeptiert | Verlust des Redlines; unklar welche Positionen verändert | Immer Kopie des Eingangs-Redlines archivieren bevor Bearbeitung |
| Falscher Nutzer-Account | Änderungen in falscher Farbe | Nutzer-Account vor Bearbeitung prüfen (Word > Optionen > Benutzerinfo) |
| Kommentare einer Partei gelöscht statt beantwortet | Informationsverlust; Gegenseite merkt nicht, dass Kommentar adressiert wurde | Kommentare nur per "Antworten"-Funktion schliessen, nie löschen |
| Direkte Textänderung ohne Track Change | "Stealth Edit" — kann als Vertrauensbruch gewertet werden | Track Changes immer aktiviert lassen während Drafting |
| Metadaten nicht entfernt bei Abgabe an Notar | Notar sieht interne Diskussion und Kommentare | Notarfassung: Track Changes akzeptieren, Kommentare löschen, Metadaten bereinigen |

---

## Redline v3 vs. v4: Besondere Probleme

### Problem 1 — "Ghosted" Track Changes

In SPA v3 (Roosendaal-Fassung) fanden sich nach Versand an Gegenseite Track-Changes-Markierungen aus einer alten Version (SPA v1 internem Entwurf), die durch fehlerhaftes Dokument-Zusammenführen wieder auftauchten.

**Folge:** Schäfer Schoeneberg Stoll sah interne Kommentare der Verkaeuferkanzlei aus der Frühphase (u.a. interne Bewertung zum Knowledge Qualifier).

**Lehre:** Vor externem Versand immer: Strg+A, dann alle Markierungen prüfen via "Alle Änderungen anzeigen" — oder Dokument frisch aus clean version erstellen.

### Problem 2 — Kollidierender Tracked Text in Tabellen

In Art. 6-Tabelle (Indemnification-Übersicht) kollidierten Track-Changes-Formatierungen in Tabellenzellen, sodass Text unleserlich wurde (Word-Bug mit Tabellen und eingeschalteten Revisionsmarkierungen).

**Lösung:** Tabellen in Redlines als Screenshot einbetten (Bild, nicht editierbares Objekt); daneben leere Kommentar-Zelle für Klärungen.

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
