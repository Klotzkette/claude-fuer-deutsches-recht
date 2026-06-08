---
name: anpassen
description: "Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen BDSG-Besonderheiten Anpassungsbedarf. Output: Anpassungsprotokoll ueberarbeitete Dokumente. Abgrenzung: nicht für Neuerstellung von Dokumentation."
---

# Customize – Praxisprofil anpassen

## Zweck

Gezieltes Aktualisieren einzelner Abschnitte von `CLAUDE.md`, ohne das gesamte Kaltstart-Interview zu wiederholen. Typische Anlässe: neue Aufsichtsbehörde wegen Umzug der Hauptniederlassung, geänderter AVV-Dealbreaker nach Vertragsverhandlung, neue Systemliste nach IT-Migration, aktualisertes DSFA-Format nach Audit-Feedback, Wechsel des internen DSB.

## Eingaben

- Welcher Abschnitt soll geändert werden? (frei formuliert oder Menüauswahl)
- Neuer Wert oder neue Position
- Optional: Beleg für die Änderung (z.B. neues Gerichtsurteil, neue EDSA-Leitlinie, Managemententscheidung)

## Ablauf

1. **Abschnitt identifizieren.** Nutzer nennt, was geändert werden soll. Bei Unklarheit eine strukturierte Liste der änderbaren Bereiche anzeigen:
 - Organisationsdaten (Name, Rechtsform, Standort)
 - Zuständige Aufsichtsbehörde
 - Rolle (Verantwortlicher / Auftragsverarbeiter)
 - Datenschutzbeauftragte·r (Name, intern/extern)
 - Rechtsgrundlagen-Übersicht (Art. 6/9 DSGVO)
 - AVV-Playbook (Klausel-Positionen, Deal-Breaker)
 - Drittlandtransfer-Mechanismen (SCC, DPF, BCR)
 - Systemliste für Betroffenenanfragen
 - DSFA-Format und Auslöser
 - Datenschutzerklärungsangaben
 - Ausgaben-Konfiguration (Ordner, Namenskonvention)
 - Integrations-Einstellungen

2. **Aktuellen Wert zeigen.** Den aktuellen Wert aus `CLAUDE.md` lesen und ausgeben, damit der Nutzer die Änderung klar gegen den Ist-Zustand vergleichen kann.

3. **Änderung vorbereiten.** Neuen Wert formulieren. Bei normativen Änderungen (z.B. neue Aufsichtsbehörde wegen Art. 56 DSGVO) die Rechtsgrundlage der Änderung nennen.

4. **Bestätigung einholen.** Den geplanten Schreibvorgang explizit bestätigen lassen – vor dem Überschreiben.

5. **Schreiben.** `CLAUDE.md` an der betroffenen Stelle aktualisieren. Rest unverändert lassen.

6. **Zusammenfassung.** Was wurde geändert, was blieb unverändert, gibt es Folgeaktionen (z.B. Datenschutzerklärung aktualisieren nach geänderter Systemliste)?

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 56 DSGVO (federführende Aufsichtsbehörde)
- Art. 37 DSGVO, § 38 BDSG (DSB-Benennungspflicht)
- Art. 28 DSGVO (AVV-Mindestanforderungen für Playbook-Änderungen)
- Art. 46, 47, 49 DSGVO (Drittlandtransfer-Mechanismen)
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Ausgabeformat

Kurze Änderungsbestätigung:
```
Geändert: [Abschnitt]
Alter Wert: [Wert]
Neuer Wert: [Wert]
Rechtsgrundlage der Änderung: [Norm oder "organisatorische Entscheidung"]
Folgeaktionen: [z.B. "Datenschutzerklärung prüfen, ob Änderung dort sichtbar werden muss"]
```

## Beispiel

**Situation:** Das Unternehmen zieht seinen Hauptsitz von Bayern nach Hessen.

**Analyse:**
Die Zuständigkeit der Aufsichtsbehörde richtet sich nach der Hauptniederlassung in der EU, Art. 56 Abs. 1 DSGVO. Mit Umzug nach Hessen wechselt die federführende Aufsichtsbehörde vom Bayerischen Landesamt für Datenschutzaufsicht (BayLDA) zum Hessischen Beauftragten für Datenschutz und Informationsfreiheit (HBDI). Für laufende Aufsichtsverfahren beim BayLDA ist der Wechsel mit Hauptniederlassungsverlegung dem BayLDA mitzuteilen (Art. 60 Abs. 1 DSGVO analog, h.M.).

**Änderung:**
```
Zuständige Aufsichtsbehörde: HBDI (zuvor: BayLDA)
Rechtsgrundlage: Art. 56 Abs. 1 DSGVO
Datum: [Umzugsdatum]
Folgeaktionen: Laufende Verfahren beim BayLDA auf HBDI übertragen; Datenschutzerklärung (Aufsichtsbehördenverweis) aktualisieren; Kontaktdaten HBDI in CLAUDE.md einpflegen.
```

## Risiken / typische Fehler

- **Teilaktualisierung vergessen:** Wer den DSB wechselt, muss auch die Datenschutzerklärung und ggf. das Verarbeitungsverzeichnis (Art. 30 Abs. 1 lit. a DSGVO: Name und Kontakt DSB) aktualisieren.
- **AVV-Playbook ohne Begründung:** Änderungen an Klauselpositionen sollten mit Datum und Anlass dokumentiert werden (Präzedenzfall, Gerichtsurteil, Managemententscheidung), damit spätere Prüfer die Position nachvollziehen können.
- **Integrations-Änderungen ohne Test:** Neue Connector-Einstellung erst nach erfolgreichem Test-Aufruf als ✓ markieren.
- **Überschreiben von Mandats-Ebene:** Wenn Mandat-Arbeitsbereiche aktiviert sind, prüfen, ob die Änderung das Praxisprofil oder nur ein einzelnes Mandat betrifft. Mandat-Ebene überschreibt Praxisprofil nur für dieses Mandat.

## Quellen / Updates

Stand: 05/2026. Bei BDSG-Novellen, neuen BRAO-Regeln oder Aufsichtsbehörden-Neustrukturierungen Skill aktualisieren.

**Querverweise:**
- `datenschutzrecht/skills/datenschutzrecht-kaltstart-interview/SKILL.md` — Vollständige Neukonfiguration
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Drittlandtransfer-Mechanismen im Praxisprofil

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Was genau soll geändert werden? (Aufsichtsbehörde / AVV-Dealbreaker / Systemliste / DSB)
2. Hat die Änderung Auswirkungen auf andere Dokumente (Datenschutzerklärung, VVT, DSFA)?
3. Liegt ein Beleg (Urteil, EDSA-Leitlinie, Managemententscheidung) für die Änderung vor?
4. Betrifft die Änderung das Praxisprofil oder nur ein einzelnes Mandat?

## Output-Template — Änderungsbestätigung

**Adressat:** Datenschutzbeauftragter / Kanzlei intern — Tonfall: sachlich-strukturiert

```
Praxisprofil-Änderungsprotokoll [DATUM]
Abschnitt: [ABSCHNITT]
Alter Wert: [ALTER WERT]
Neuer Wert: [NEUER WERT]
Beleg/Rechtsgrundlage: [NORM / BESCHLUSS / DATUM]
Folgeaktionen:
- Datenschutzerklaerung aktualisieren: [ja/nein]
- VVT aktualisieren: [ja/nein]
- Aufsichtsbehoerde informieren: [ja/nein]
- Weitere: [...]
Durchgefuehrt von: [SACHBEARBEITER]
```

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.
