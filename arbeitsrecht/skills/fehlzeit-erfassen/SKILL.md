---
name: fehlzeit-erfassen
description: "Für Fehlzeit Erfassen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Neue Abwesenheit oder neuen Urlaubseintrag im Register anlegen – mit allen für die Fristenberechnung nach BUrlG, EFZG, MuSchG und BEEG notwendigen Informationen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Neue Abwesenheit oder neuen Urlaubseintrag im Register anlegen – mit allen für die Fristenberechnung nach BUrlG, EFZG, MuSchG und BEEG notwendigen Informationen. Startet die Überwachung von Fristen ab dem ersten Tag.

### /arbeitsrecht:fehlzeit-erfassen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:fehlzeit-erfassen` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Mitarbeiter-Angaben (Name/ID – anonymisiert genügt)
- Abwesenheitstyp und Startdatum
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Tarifvertrag

## Ablauf

### 1. Konfiguration lesen

Standort-Fußabdruck, HRIS-Status, Tarifvertrag prüfen. Falls HRIS verbunden: Hinweis, dass Eintrag besser dort erfolgt; trotzdem im Register dokumentieren, wenn Nutzer dies wünscht.

### 2. Alle nötigen Informationen in einem einzigen Prompt abfragen

> Kurze Angaben für den Fehlzeiteintrag:
>
> - **Mitarbeiter-ID oder Rolle** (anonymisiert ist in Ordnung)
> - **Bundesland** (bestimmt anwendbare Regeln)
> - **Abwesenheitstyp:**
> - Krankheit / Arbeitsunfähigkeit (EFZG)
> - Urlaub (BUrlG)
> - Mutterschutz / Beschäftigungsverbot (MuSchG)
> - Elternzeit (BEEG)
> - Pflegezeit (PflegeZG)
> - Sonstiges
> - **Startdatum** der Abwesenheit
> - **Voraussichtliches Rückkehrdatum** (falls bekannt – leer lassen wenn unbekannt)
> - **Bei Elternzeit:** Hat die Mitarbeiterin/der Mitarbeiter die Elternzeit schriftlich angemeldet? Anmeldedatum?
> - **Bei Krankheit:** Gleiche Erkrankung wie in zurückliegenden 12 Monaten? (für EFZG-Neuanspruchs-Berechnung)
> - **Schwangerschaft/Entbindung:** Errechneter Entbindungstermin (für MuSchG-Fristen)

### 3. Fristen automatisch berechnen

Je nach Abwesenheitstyp:

**Krankheit (EFZG):**
- BEM-Prüfdatum: ab 6-wöchiger AU innerhalb von 12 Monaten (Paragraf 167 Abs. 2 SGB IX)
- Wenn gleiche Erkrankung: Neuer EFZG-Anspruch? Letzter AU-Zeitraum prüfen.

**Urlaub (BUrlG):**
- Verfallsdatum: 31.12. des laufenden Jahres (Paragraf 7 Abs. 3 S. 1 BUrlG) bzw. 31.03. des Folgejahres bei Übertragung
- Resturlaub berechnen: Gesamtanspruch − genommene Tage

**Mutterschutz (MuSchG):**
- Schutzfrist-Beginn: 6 Wochen vor errechnetem Entbindungstermin (Paragraf 3 MuSchG)
- Schutzfrist-Ende: 8 Wochen nach Entbindung (Paragraf 3 Abs. 2 MuSchG; 12 Wochen bei Frühgeburt)
- Kündigungsschutz-Ende: 4 Monate nach Entbindung (Paragraf 17 Abs. 1 S. 1 Nr. 1 MuSchG)

**Elternzeit (BEEG):**
- Anmeldefrist geprüft? (7 Wochen vor Beginn; Paragraf 16 Abs. 1 BEEG)
- Elternzeit-Ende: 3. Geburtstag des Kindes als maximale Frist
- Kündigungsschutz-Ende: Ende der Elternzeit (Paragraf 18 Abs. 1 BEEG)
- Teilzeit-Anspruch: Ab Beginn der Elternzeit (Paragraf 15 Abs. 6 BEEG)

**Pflegezeit (PflegeZG):**
- Max. 6 Monate (Paragraf 3 Abs. 1 PflegeZG)
- Kündigungsschutz: ab Ankündigung bis 4 Wochen nach Ende (Paragraf 5 PflegeZG)
- Ankündigungsfrist: 10 Arbeitstage vor Beginn (Paragraf 3 Abs. 3 PflegeZG)

### 4. Eintrag schreiben

Register-Eintrag anlegen in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml`:

```yaml
- id: [generierte ID]
 mitarbeiter: [anonymisierte Bezeichnung]
 bundesland: [BL]
 typ: [krankheit|urlaub|mutterschutz|elternzeit|pflegezeit|sonstiges]
 startdatum: [JJJJ-MM-TT]
 rueckkehr_geplant: [JJJJ-MM-TT | unbekannt]
 fristen:
 efzg_erschoepfung: [JJJJ-MM-TT] # nur bei Krankheit
 bem_pruefung: [JJJJ-MM-TT] # nur bei Krankheit ≥ 6 Wochen
 urlaubsverfall_warnung: [JJJJ-MM-TT] # nur bei Urlaub
 schutzfrist_ende: [JJJJ-MM-TT] # MuSchG/BEEG
 ks_schutz_ende: [JJJJ-MM-TT] # Kündigungsschutz-Ende
 notizen: [ggf.]
 status: offen
```

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

- Paragraf 3 EFZG (6-Wochen-Fortzahlung), Paragraf 5 EFZG (Nachweispflicht)
- Paragraf 3, 7 BUrlG (Mindesturlaub, Übertragung, Verfall)
- Paragraf 3 MuSchG (Schutzfristen), Paragraf 17 MuSchG (Kündigungsschutz)
- Paragrafen 15–18 BEEG (Elternzeit, Anmeldung, Kündigungsschutz)
- Paragraf 167 Abs. 2 SGB IX (BEM-Pflicht)

## Beispiele

```
/arbeitsrecht:fehlzeit-erfassen
Mitarbeiterin HR-022, Bayern, Elternzeit ab 01.02.2025.
Anmeldung liegt schriftlich vor (10.12.2024). Rückkehr geplant 01.02.2026.
```

## Risiken / typische Fehler

- **BEEG-Anmeldung nachträglich** – Elternzeit kann nicht rückwirkend beantragt werden; Anmeldedatum prüfen.
- **Mehrere Abwesenheitsperioden bei gleicher Erkrankung** – EFZG-Neuanspruch-Prüfung nicht vergessen.
- **Anonymisierung** – auch im internen Register: Mitarbeiter-IDs statt Namen verwenden; Paragraf 26 BDSG.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
