---
name: zeuge-vorbereitung
description: "Für Zeugenvernehmung-Vorbereitung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen."
---

# Zeugenvernehmung-Vorbereitung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Vorbereitung auf eine Zeugenvernehmung im deutschen Zivil- oder Strafverfahren. Drei Perspektiven:
- **Eigener Zeuge vorbereiten** (Information des Mandanten über Ablauf, Paragraf 373 ff. ZPO; Paragraf 395 StPO)
- **Gegnerischen Zeugen befragen** (Fragenkatalog aus der Mandatstheorie entwickeln)
- **Strafverteidigung:** Vorbereitung auf Hauptverhandlung (Paragrafen 244 ff. StPO), Pflichtverteidiger-Gespräch

> Die Zeugenvernehmung findet ausschließlich vor dem Gericht statt (Paragraf 396 ZPO, Paragraf 238 Abs. 2 StPO). Eine vorgerichtliche anwaltliche Befragung von Zeugen kennt das deutsche Recht nicht. Eine informelle Zeugen-"Vorbefragung" durch den Anwalt ist berufsrechtlich sensibel (Paragraf 1 BORA – Sachlichkeit; vgl. Paragraf 26 BRAO) und darf Zeugen nicht beeinflussen.

## Eingaben

- Aktives Mandat (Slug)
- Zeuge: Name, Rolle im Verfahren (Zeuge der Partei / gegnerischer Zeuge / Zeuge von Amts wegen)
- Vernehmungsmodus: `--eigener-zeuge`, `--gegnerischer-zeuge`, `--strafverfahren`
- Vorhandene Dokumente: Zeugenaussagen (Erstvernehmung, Polizeiprotokoll), Schriftverkehr des Zeugen, Anlagen, Chronologie

## Ablauf

### Modus: Eigener Zeuge vorbereiten (`--eigener-zeuge`)

1. **Ablaufbelehrung:** Dem Mandanten/Zeugen den Vernehmungsablauf erklären (Paragrafen 395, 396, 402 ZPO): Vorführung, allgemeine Personalien, Belehrung, freie Schilderung, Befragung durch Gericht, Fragen der Parteien, Eid/eidesstattliche Versicherung (Paragraf 391 ZPO).

2. **Zeugnisverweigerungsrecht prüfen:** Paragrafen 383–385 ZPO (Angehörige, Berufsgeheimnisträger, Selbstbelastungsverbot); Paragraf 52 StPO; Paragraf 55 StPO (Auskunftsverweigerungsrecht).

3. **Erinnerungslücken identifizieren:** Aus Chronologie bekannte Ereignisse mit Zeugenwissen abgleichen; offene Punkte markieren.

4. **Fragenvorbereitung:** Erwartete Fragen des Gerichts und der Gegenseite vorab erarbeiten; angemessene Antworten (wahrheitsgemäß, nicht überschießend) vorbereiten.

5. **Vorhalte vorantizipieren:** Schriftstücke, E-Mails oder frühere Aussagen, die dem Zeugen vorgehalten werden könnten, identifizieren.

### Modus: Gegnerischen Zeugen befragen (`--gegnerischer-zeuge`)

1. **Zeugenprofil erstellen:** Aus Mandatsakte und Chronologie: Was weiß der Zeuge, was hat er gesagt, welche Dokumente hat er unterzeichnet?

2. **Themengliederung:**
 - Kernthemen (direkt anspruchsrelevant)
 - Glaubwürdigkeitsthemen (Widersprüche zu früheren Aussagen, Eigeninteresse)
 - Bestätigungsthemen (ungünstige Tatsachen aus Zeugen-Sicht bestätigen lassen)

3. **Fragenkatalog:** Geschlossene Kontrollfragen (auf ein Ja/Nein ausgerichtet) zuerst; offene Fragen nur bei sicherer Antwort; Fangfragen vermeiden (Prozessrisiko: Zeuge weicht aus).

4. **Vorhalte:** Dokumente, auf die vorgehalten werden soll, mit Anlage-Nr. verzeichnen.

5. **Glaubwürdigkeitsangriff:** Widersprüche zu protokollierten Aussagen, Eigeninteresse, Abhängigkeiten.

### Modus: Strafverfahren (`--strafverfahren`)

1. **Akteneinsicht Paragraf 147 StPO:** Vernehmungsprotokolle aus der Ermittlungsakte identifizieren.
2. **Belehrung Paragraf 136 StPO / Paragraf 55 StPO:** Sicherstellen, dass Auskunftsverweigerungsrecht bekannt ist.
3. **Hauptverhandlung Paragraf 244 StPO:** Beweisantragsrecht der Verteidigung (Beweisantrag auf Zeugenladung, Paragraf 244 Abs. 3, 6 StPO).

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Risiken / typische Fehler

- **Zeugencoaching verboten:** Der Anwalt darf den Zeugen nicht zu einer bestimmten Aussage anleiten; nur Erläuterung des Ablaufs und Erinnerungshilfe auf Basis vorhandener Dokumente zulässig (vgl. Paragraf 1 BORA).
- **Gegnerischer Zeuge – keine Kontaktaufnahme:** Kontaktaufnahme mit gegnerischem Zeugen außerhalb des Verfahrens ist berufsrechtlich problematisch (Paragraf 12 BORA).
- **Vereidigung:** Paragraf 391 ZPO – Gericht entscheidet; falsche Zeugenaussage ist strafbar (Paragraf 153 StGB); Zeuge vor Vernehmung hierüber belehren.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
