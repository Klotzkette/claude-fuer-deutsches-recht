---
name: kaltstart-interview
description: "Ersteinrichtung des Arbeitsrecht-Plugins – ermittelt Standortprofil, Tarifbindung, Betriebsratssituation und Eskalationsregeln aus Personalhandbuch und Kündigungsunterlagen. Ausführen bei Neuinstallation, bei noch nicht befüllter CLAUDE.md-Konfiguration oder mit --redo oder --check-integrations."
---

# /arbeitsrecht:arbeitsrecht-kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Arbeitsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:arbeitsrecht-kaltstart-interview` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Eingaben

- Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` (Zieldatei)
- Kanzlei-/Unternehmensname, Branche, Mitarbeiterzahl, Standorte
- Personalhandbuch (optional, verbessert Ausgaben erheblich)
- Bis zu drei aktuelle Kündigungsunterlagen (optional)
- Angaben zu Tarifbindung, Betriebsrat, HRIS-System

## Ablauf

### Vorabprüfung

1. `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` prüfen.
 - `--check-integrations`: Nur den Integrationsabschnitt neu ermitteln, Interview überspringen.
 - `--redo`: Vollständiges Interview neu ausführen, auch wenn Konfiguration vorhanden.
 - Kein Flag: Falls Konfiguration vorhanden und vollständig (keine `[PLATZHALTER]`), melden: "Plugin bereits eingerichtet. Änderung mit `--redo` oder gezielt mit `/arbeitsrecht:arbeitsrecht-anpassen`."
 - Falls Konfiguration aus altem Cache-Pfad vorhanden: Dorthin migrieren und mitteilen.

2. **Teil 0 – Was ist verbunden?**
 Alle konfigurierten Integrationen aktiv testen (nicht nur deklariert). Nur `✓` melden, wenn ein Tool-Aufruf in dieser Sitzung erfolgreich war. Nicht getestete Integrationen: `⚪` mit kurzem Hinweis zur Prüfung.

### Interview (Teile 1–5)

**Teil 1 – Praxisumfeld und Nutzerrolle**

Alle folgenden Fragen in einem einzigen Prompt stellen:

> Damit das Plugin für Ihre Praxis kalibriert ist, bitte kurz beantworten:
>
> 1. **Kanzlei oder Unternehmen?** (Kanzlei / Rechtsabteilung in-house / Behörde)
> 2. **Praxisumfeld:** (Einzelkanzlei / Mittelkanzlei / Großkanzlei / Fachanwalt Arbeitsrecht / Syndikusrechtsanwalt)
> 3. **Wer nutzt dieses Plugin?** (Rechtsanwalt / Fachanwalt / Syndikus | HR-Leitung mit Anwaltszugang | HR ohne Anwaltszugang)
> 4. **Anwaltlicher Ansprechpartner** (falls HR-Nutzer): Name / Team / Außenkanzlei
> 5. **Kanzlei-/Unternehmensname und Branche** (für unternehmens-profil.md, falls nicht vorhanden)

**Teil 2 – Standort-Fußabdruck**

> Wo beschäftigen Sie Mitarbeiter?
>
> - Bundesländer (mit ca. Mitarbeiterzahl je Bundesland)
> - Ausländische Standorte (für Entsendung/AÜG-Prüfung)
> - Gesamtmitarbeiterzahl (maßgeblich für KSchG-Schwellenwert § 23 KSchG: > 10 AN)
> - Remote-first oder überwiegend Präsenz?

Aus den Angaben ermitteln:
- Gilt das KSchG allgemein? (§ 23 KSchG: > 10 AN, Beschäftigung > 6 Monate)
- Tarifbindung? Welche Tarifverträge?
- Betriebsrat vorhanden? Ggf. Sprecherausschuss (SprAuG)?
- Besondere Kündigungsschutzträger im Betrieb? (Schwerbehinderte, Betriebsratsmitglieder, Datenschutzbeauftragte)

**Teil 3 – Einstellung und Kündigung**

> - Wann prüft die Rechtsabteilung Einstellungen? (alle / nur Führungskräfte / nur bei Befristung)
> - Gibt es ein Standard-Arbeitsvertragsmuster?
> - Wann prüft die Rechtsabteilung Kündigungen? (alle / nur bei KSchG / RIF / Führungskräfte)
> - Standard-Abfindungsformel? (0,5 × Bruttomonatsgehalt × Beschäftigungsjahre nach § 1a KSchG oder Einzelvereinbarung)
> - Aufhebungsvertrag als Standard? Musterstandort?

**Teil 4 – Seed-Dokumente**

> Bitte stellen Sie Folgendes bereit (optional, verbessert Ausgaben erheblich):
> - Aktuelles Personalhandbuch (oder Ablageort)
> - Bis zu drei aktuelle Kündigungsunterlagen (anonymisiert ist in Ordnung)
> - Muster-Aufhebungsvertrag, falls vorhanden

Dokumente lesen und daraus extrahieren:
- Bestehendes Eskalationsschema
- Besondere Klauseln (Wettbewerbsverbote, Rückzahlungsklauseln, Freiwilligkeitsvorbehalte)
- Unterschriften-/Genehmigungsprozess bei Kündigungen

**Teil 5 – Systeme und Integrationen**

> - HRIS-System? (Workday / BambooHR / Personio / DATEV / keins)
> - Urlaubsdaten-Zugang für die Rechtsabteilung?
> - Dokumentenablage? (DMS / SharePoint / Google Drive / lokal)
> - E-Mail-Integration gewünscht?

### Konfiguration schreiben

Alle gesammelten Informationen in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` schreiben. Übergeordnete Verzeichnisse anlegen. Company-profile.md erstellen, falls nicht vorhanden.

## Quellen und Zitierweise

Einschlägige Normen für die Eskalationstabelle:
- KSchG § 23 (Schwellenwert > 10 AN), § 1 (Kündigungsschutz), § 17 (Massenentlassung)
- BetrVG § 102 (BR-Anhörung vor Kündigung), § 99 (Zustimmung bei Einstellung)
- SGB IX § 168 (Zustimmung Inklusionsamt bei Schwerbehinderung)
- MuSchG § 17 (Kündigungsverbot Schwangerschaft)
- BEEG § 18 (Kündigungsverbot Elternzeit)
- KSchG § 15 (Sonderkündigungsschutz BR-Mitglieder)
- BDSG § 26 (Beschäftigtendatenschutz)

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

## Ausgabeformat

Abschlussbericht des Interviews:

```
Arbeitsrecht-Plugin: Einrichtung abgeschlossen
=============================================

Praxisumfeld: [Kanzlei/in-house/Syndikus]
Nutzerrolle: [Anwalt / HR mit Zugang / HR ohne Zugang]
KSchG anwendbar: [ja/nein – Begründung]
Tarifbindung: [ja: Tarif / nein]
Betriebsrat: [ja / nein / unklar]

Standorte:
 DE-BY: N Mitarbeiter
 DE-NW: N Mitarbeiter
 [...]

Eskalationstabelle:
 Betriebsbedingte Kündigung → immer GC + Außenberater
 Kündigung Schwerbehinderte → immer Inklusionsamt § 168 SGB IX
 Kündigung BR-Mitglied → immer § 15 KSchG prüfen, GC
 Kündigung Schwangerschaft → § 17 MuSchG Zustimmung Behörde
 [...]

Seed-Dokumente gelesen: [N]
⚪ Integrationen: [Liste mit Status]

Konfiguration gespeichert: ~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiele

```
/arbeitsrecht:arbeitsrecht-kaltstart-interview
```

```
/arbeitsrecht:arbeitsrecht-kaltstart-interview --redo
```

```
/arbeitsrecht:arbeitsrecht-kaltstart-interview --check-integrations
```

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Tarifbindung übersehen.** Nachwirkung (§ 4 Abs. 5 TVG), Allgemeinverbindlicherklärung (§ 5 TVG) oder Bezugnahmeklausel im Arbeitsvertrag können Tarifrecht anwendbar machen, ohne Verbandsmitgliedschaft.
- **Betriebsrat-Situation unklar.** Betriebsrat kann auch in kleinen Betrieben (ab 5 wahlberechtigten AN) gewählt werden (§ 1 BetrVG). Auf § 102 BetrVG hinweisen, sobald Kündigung im Raum steht.
- **Datenschutz bei Seed-Dokumenten.** Kündigungsunterlagen sind personenbezogen; § 26 BDSG. Anonymisierung oder Pseudonymisierung empfehlen.
