---
name: policy-monitor
description: >
  Drift-Monitoring der Datenschutzerklärung und Datenschutzrichtlinien: wöchentlicher
  Abgleich zwischen gelebter Praxis / neuen Verarbeitungstätigkeiten und publizierten
  Erklärungen. Erkennt Inkonsistenzen und entwirft Aktualisierungen.
  Zweiter Modus: Direkt-Anfrage für konkrete geplante Änderungen.
language: de
triggers:
  - "Policy-Monitor"
  - "Datenschutzerklärung prüfen"
  - "policy drift"
  - "Richtlinie aktualisieren"
  - "Datenschutzerklärung veraltet"
  - "Consent Management"
---

# Policy-Monitor – Drift-Monitoring Datenschutzerklärung

## Zweck

Zwei Modi: (1) **Sweep-Modus** – regelmäßiger Abgleich aller Datenschutz-Commitment-Flächen gegen aktuelle Verarbeitungspraxis, um Drift zu erkennen. (2) **Direkt-Modus** – für eine konkrete geplante Änderung prüfen, ob und wie die Datenschutzerklärung angepasst werden muss.

Typische Drifts: neue Tracking-Tool-Integration ohne Datenschutzerklärungsupdate, neuer Sub-AV ohne Empfängerlistenaktualisierung, verlängerte Speicherfristen ohne Ankündigung, neue Drittlandtransfers ohne Transfermechanismus in der Erklärung.

## Eingaben

- **Sweep-Modus:** Ausgabenordner aus `CLAUDE.md` (wo DSFAs, AVV-Reviews, Triage-Ergebnisse gespeichert sind), Datenschutzerklärungsquelle (URL oder Datei), Liste aktueller Verarbeitungstätigkeiten
- **Direkt-Modus:** Beschreibung der geplanten Änderung der Verarbeitungspraxis

## Ablauf – Sweep-Modus

1. **Commitment-Inventur.**
   Alle Datenschutz-Commitment-Flächen aus `CLAUDE.md` lesen:
   - Datenschutzerklärung (Haupt-URL / Dokument)
   - CMP / Cookie-Consent-Banner-Konfiguration
   - App-Store Privacy Labels
   - In-Produkt-Einwilligungsflows
   - Sektorspezifische Hinweise (TTDSG, KUG)

2. **Praxis-Inventur.**
   Aktuelle Verarbeitungspraxis aus Ausgaben des Plugins rekonstruieren:
   - Neueste AVV-Reviews (neue Sub-AVs, neue Drittlandtransfers)
   - Neueste DSFA-Ergebnisse (neue Verarbeitungstätigkeiten)
   - Neueste Triage-Ergebnisse (Rechtsgrundlagenänderungen)
   - Aus `CLAUDE.md` bekannte Systemliste und Drittlandsituation

3. **Drift-Analyse.**
   Für jede Commit-Fläche: Ist-Inhalt gegen Praxis-Inventur abgleichen.

   | Commit-Fläche | Praxis-Ist | Erklärung-Ist | Drift? | Schwere |
   |---|---|---|---|---|
   | Datenschutzerklärung – Empfänger | [aktuelle Liste] | [publizierte Liste] | Ja/Nein | 🔴/🟡/🟢 |
   | Cookie-Banner – Kategorien | [aktiv gesetzt] | [angekündigt] | Ja/Nein | … |
   | Speicherfristen | [tatsächlich] | [publiziert] | Ja/Nein | … |
   | Drittlandtransfer-Mechanismus | [aktuell] | [publiziert] | Ja/Nein | … |

4. **Drift-Klassifikation.**
   - 🔴 **Sofortiger Handlungsbedarf:** Verarbeitung erfolgt, die in der Erklärung nicht angekündigt ist → Informationspflicht-Verstoß Art. 13/14 DSGVO, potenziell rechtswidrige Verarbeitung.
   - 🟠 **Hoch:** Wesentliche Erweiterung des Verarbeitungsumfangs nicht reflektiert (z.B. neuer Zweck, neues Empfänger-Land).
   - 🟡 **Mittel:** Aktualisierung empfohlen, keine unmittelbare Rechtswidrigkeit (z.B. neue Formulierung genauer als nötig, aber nicht falsch).
   - 🟢 **Gering:** Kosmetische Anpassung, kein Handlungsdruck.

5. **Änderungsentwürfe.**
   Für jede 🔴- und 🟠-Drift: konkreten Textvorschlag für die Datenschutzerklärung formulieren (nicht als Meta-Kommentar, sondern als fertiger Erklärungstext).

6. **Sweep-Bericht.**
   Zusammenfassung: [N] Drifts, davon [N] 🔴, [N] 🟠, [N] 🟡; Änderungsvorschläge inline; Folgeaktionen.

## Ablauf – Direkt-Modus

1. Geplante Änderung der Verarbeitungspraxis beschreiben lassen.
2. Prüfen: Welche Art. 13/14 DSGVO-Pflichtinformationen sind betroffen?
   - Neue Datenkategorie → Art. 13 Abs. 1 lit. c DSGVO
   - Neuer Zweck → Art. 13 Abs. 1 lit. c DSGVO
   - Neuer Empfänger → Art. 13 Abs. 1 lit. e DSGVO
   - Neue Speicherfrist → Art. 13 Abs. 2 lit. a DSGVO
   - Neues Drittland → Art. 13 Abs. 1 lit. f DSGVO
3. Prüfen: Ändert sich die Rechtsgrundlage (Art. 6/9 DSGVO)? Muss ggf. neue Einwilligung eingeholt werden?
4. Prüfen: Ist eine DSFA erforderlich? (Weiterleitung an `pia-generation` anbieten)
5. Änderungsentwurf für betroffene Abschnitte der Datenschutzerklärung erstellen.
6. Prüfen: Erfordern App-Store-Labels oder Cookie-Banner-Konfiguration Anpassung?

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 13 DSGVO (Informationspflicht bei Datenerhebung bei Betroffenen)
- Art. 14 DSGVO (Informationspflicht bei Datenerhebung nicht bei Betroffenen)
- Art. 5 Abs. 1 lit. a DSGVO (Transparenzgrundsatz)
- Art. 12 DSGVO (Transparente Information)
- §§ 19, 25 TTDSG (Einwilligung Endgerätezugriff, Cookie-Einwilligung)
- EDSA-Leitlinien 03/2022 zu Dunklen Designmustern (Consent-Flows)
- EDSA-Leitlinien 05/2020 zu Einwilligung
- Paal, in: Paal/Pauly, DSGVO/BDSG, 3. Aufl. 2021, Art. 13 Rn. 1 ff.
- Kühling, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 13 Rn. 1 ff.
- Schulze, in: BeckOK DSGVO, 16. Ed. (Stand 01.11.2024), Art. 13 Rn. 1 ff.

## Ausgabeformat

**Sweep-Modus:**
1. Sweep-Datum und geprüfte Quellen
2. Drift-Tabelle (alle Flächen × alle Dimensionen)
3. Drift-Klassifikation mit Schwere
4. Priorisierte Änderungsvorschläge (druckfertige Textbausteine, keine Kommentare im Erklärungstext)
5. Sweep-Folgeaktionen

**Direkt-Modus:**
1. Betroffene Art. 13/14-Pflichten
2. Rechtsgrundlagen-Check
3. DSFA-Hinweis (falls einschlägig)
4. Änderungsentwurf für Datenschutzerklärung (Textbausteine)

## Beispiel (Direkt-Modus)

**Geplante Änderung:** Das Unternehmen möchte einen neuen Analytics-Anbieter mit Sitz in den USA integrieren (bisher EU-only).

**Analyse:**
- Neue Datenkategorie: Nein (Nutzungsverhalten bereits erfasst).
- Neuer Empfänger (Drittland USA): **Ja** – Art. 13 Abs. 1 lit. f DSGVO (Drittlandtransfer mit Transfermechanismus angeben).
- Transfermechanismus prüfen: DPF, SCC Modul 1 oder 2? TIA erforderlich (EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2945).
- Consent-Management: Ist der Anbieter nur nach Einwilligung aktiv (§ 25 TTDSG)? Dann Cookie-Banner anpassen (neue Kategorie / neuer Anbieter).
- DSFA: `use-case-triage` empfehlen – bei umfangreichem Tracking ggf. DSFA nach Art. 35 DSGVO erforderlich.

**Änderungsentwurf (Datenschutzerklärung, Abschnitt „Drittlandsübermittlung"):**
> „[Neue Passage] Wir übermitteln Daten an [Anbieter] mit Sitz in den USA. Die Übermittlung erfolgt auf Grundlage von [Transfermechanismus: EU-Standardvertragsklauseln nach Beschluss 2021/914/EU / EU-US Data Privacy Framework]. Eine Transferfolgenabschätzung liegt vor. Weitere Informationen erhalten Sie auf Anfrage bei unserem Datenschutzbeauftragten."

## Risiken / typische Fehler

- **Sweep ohne konfigurierten Ausgabenordner:** Ohne Ordner-Pfad kann der Sweep keine Praxis-Inventur aus Plugin-Ausgaben erstellen; Direkt-Modus bleibt aber ohne Ausgabenordner vollständig nutzbar.
- **Datenschutzerklärungsversion nicht datiert:** Nutzer sollten publizierte Erklärungen immer mit Datum versehen; anderenfalls kann Drift nicht datiert werden.
- **Cookie-Banner ≠ Datenschutzerklärung:** TTDSG-Einwilligung (§ 25 TTDSG) ist unabhängig von der DSGVO-Rechtsgrundlage; eine korrekte Datenschutzerklärung ersetzt nicht den rechtskonformen Cookie-Banner.
- **Stillschweigendes Weglassen veralteter Klauseln:** Wenn eine Verarbeitung eingestellt wird, muss die Datenschutzerklärung aktiv aktualisiert werden – das Fehlen einer Praxis ist kein Automatismus für korrekte Erklärung.
- **Frequenz:** EDSA empfiehlt anlassbezogene Aktualisierung; ein rein jährliches Review ist bei schnell wachsenden Produkten nicht ausreichend.
