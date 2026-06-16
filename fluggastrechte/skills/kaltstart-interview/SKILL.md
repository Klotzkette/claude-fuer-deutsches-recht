---
name: kaltstart-interview
description: "Kaltstart-Interview für das Fluggastrechte-Plugin. Klaert Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reiseplan-Konvention. Schreibt das Profil nach ~/.claude/plugins/config/claude-fuer-de..."
---

# /fluggastrechte:fluggastrechte-kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fluggastrechte** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Ablauf

1. Datei `~/.claude/plugins/config/claude-fuer-deutsches-recht/fluggastrechte/CLAUDE.md` prüfen.
2. Falls befüllt: bestätigen.
3. Andernfalls Interview unten.

## Disclaimer

Dieses Plugin unterstützt das eigene Geltendmachen von Fluggastrechten als Verbraucher. Es ist **keine Rechtsberatung**. Bei komplexen Fällen (mehrere Passagiere mit unterschiedlichen Anspruechen Gesellschafts-Bezügen Verspätungs-Lawinen Schlichtungsstelle vor Gericht) anwaltliche Hilfe einholen — z. B. über die Schlichtungsstelle Luftverkehr (SOEP).

## Interview

### 1. Wer nutzt das Plugin

- Eigener Fluggast / Mitreisender Familie / Vertretung Bekannter / kleine Anwaltskanzlei?
- Anzahl betroffener Personen (Passagiere) pro Fall typisch.

### 2. Buchungsstammdaten

- **Name** wie in der Buchung steht (wichtig für Schriftverkehr — Airline-Datenabgleich).
- **Bevorzugte Sprache** im Schriftverkehr Deutsch / Englisch.
- **Wohnsitz und Adresse** (für Gerichtsstand bei Klage).
- **Bevorzugter Zustellweg** der Forderungsschreiben — Post (Einschreiben) oder E-Mail an Airline-Service-Postfach.

### 3. Reiseplan-Konvention

- **Buchungsbestätigung** liegt vor (PDF Boardingpass E-Mail).
- **Tickets** der Mitreisenden ebenfalls vorhanden (Vollmachten Skill `vollmacht-familienmitglieder`).
- **Schlichtungsstelle** SOEP bereits angeschrieben? Wenn ja: SOEP-Verfahren vorhanden.

### 4. Eskalation

- Bei Ausbleiben einer Reaktion oder bei Streitstand zur Schlichtungsstelle Luftverkehr **SOEP** (Schlichtungsstelle für den öffentlichen Personenverkehr e. V.) — kostenfrei für Verbraucher. Voraussetzung: keine Klage anhängig.
- Bei Erfolglosigkeit Klage zum Amtsgericht — Skill `klage-amtsgericht-fluggast`.

## Ausgabe

Profil wird geschrieben. Empfohlene nächste Skills:

- `/fluggastrechte:ticket-und-fluginformationen-erfassen` — Daten zum Fall sammeln
- `/fluggastrechte:annullierung-oder-verspätung-einordnen` — Rechtskategorie zuordnen
- `/fluggastrechte:airline-standardausreden-prüfen` — typische Gegenargumente kennen

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Rechtlicher Rahmen — Überblick

- **VO (EG) Nr. 261/2004** — Fluggastrechteverordnung des Europaeischen Parlaments und des Rates.
- **EuGH-Rechtsprechung** — Auslegungsmaßstab für alle Mitgliedstaaten.
- **BGB §§ 631 ff.** — Reisevertrag bei Pauschalreisen ergänzend.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Verjährung** drei Jahre § 195 BGB (Ende Kalenderjahr Kenntnis § 199 Abs. 1 BGB).

## Leitentscheidungen Kaltstart / Eingangsinterview

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Hinweise

Auch nach der Brexit-Anpassung gilt die VO 261/2004 in der EU. Fluege ab Drittstaat zu einem EU-Flughafen mit Nicht-EU-Airline fallen **nicht** unter die VO; Fluege ab EU mit Nicht-EU-Airline schon. Prüfkriterium: Art. 3 VO 261/2004.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)
