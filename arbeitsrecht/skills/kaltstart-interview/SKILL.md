---
name: kaltstart-interview
description: "Ersteinrichtung des Arbeitsrecht-Plugins – ermittelt Standortprofil, Tarifbindung, Betriebsratssituation und Eskalationsregeln aus Personalhandbuch und Kündigungsunterlagen. Ausführen bei Neuinstallation, bei noch nicht befüllter CLAUDE.md-Konfiguration oder mit --redo oder --check-integrations."
---

# /arbeitsrecht:arbeitsrecht-kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:arbeitsrecht-kaltstart-interview` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB Paragrafen 611a, 613a, 615, 623; KSchG Paragrafen 1, 4, 7; TzBfG Paragrafen 14, 15, 16; AGG Paragrafen 1, 3, 7, 15, 22; EntgTranspG Paragrafen 3, 5, 7; BUrlG Paragrafen 1, 3, 7; BetrVG Paragrafen 87, 99, 102; ArbZG; NachwG; SGB IX Paragrafen 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer Paragraf 623 BGB, Zugang nach Paragraf 130 BGB, Dreiwochenfrist Paragrafen 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
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
> - Gesamtmitarbeiterzahl (maßgeblich für KSchG-Schwellenwert Paragraf 23 KSchG: > 10 AN)
> - Remote-first oder überwiegend Präsenz?

Aus den Angaben ermitteln:
- Gilt das KSchG allgemein? (Paragraf 23 KSchG: > 10 AN, Beschäftigung > 6 Monate)
- Tarifbindung? Welche Tarifverträge?
- Betriebsrat vorhanden? Ggf. Sprecherausschuss (SprAuG)?
- Besondere Kündigungsschutzträger im Betrieb? (Schwerbehinderte, Betriebsratsmitglieder, Datenschutzbeauftragte)

**Teil 3 – Einstellung und Kündigung**

> - Wann prüft die Rechtsabteilung Einstellungen? (alle / nur Führungskräfte / nur bei Befristung)
> - Gibt es ein Standard-Arbeitsvertragsmuster?
> - Wann prüft die Rechtsabteilung Kündigungen? (alle / nur bei KSchG / RIF / Führungskräfte)
> - Standard-Abfindungsformel? (0,5 × Bruttomonatsgehalt × Beschäftigungsjahre nach Paragraf 1a KSchG oder Einzelvereinbarung)
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
- KSchG Paragraf 23 (Schwellenwert > 10 AN), Paragraf 1 (Kündigungsschutz), Paragraf 17 (Massenentlassung)
- BetrVG Paragraf 102 (BR-Anhörung vor Kündigung), Paragraf 99 (Zustimmung bei Einstellung)
- SGB IX Paragraf 168 (Zustimmung Inklusionsamt bei Schwerbehinderung)
- MuSchG Paragraf 17 (Kündigungsverbot Schwangerschaft)
- BEEG Paragraf 18 (Kündigungsverbot Elternzeit)
- KSchG Paragraf 15 (Sonderkündigungsschutz BR-Mitglieder)
- BDSG Paragraf 26 (Beschäftigtendatenschutz)

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
 Kündigung Schwerbehinderte → immer Inklusionsamt Paragraf 168 SGB IX
 Kündigung BR-Mitglied → immer Paragraf 15 KSchG prüfen, GC
 Kündigung Schwangerschaft → Paragraf 17 MuSchG Zustimmung Behörde
 [...]

Seed-Dokumente gelesen: [N]
⚪ Integrationen: [Liste mit Status]

Konfiguration gespeichert: ~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
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
- **Tarifbindung übersehen.** Nachwirkung (Paragraf 4 Abs. 5 TVG), Allgemeinverbindlicherklärung (Paragraf 5 TVG) oder Bezugnahmeklausel im Arbeitsvertrag können Tarifrecht anwendbar machen, ohne Verbandsmitgliedschaft.
- **Betriebsrat-Situation unklar.** Betriebsrat kann auch in kleinen Betrieben (ab 5 wahlberechtigten AN) gewählt werden (Paragraf 1 BetrVG). Auf Paragraf 102 BetrVG hinweisen, sobald Kündigung im Raum steht.
- **Datenschutz bei Seed-Dokumenten.** Kündigungsunterlagen sind personenbezogen; Paragraf 26 BDSG. Anonymisierung oder Pseudonymisierung empfehlen.
