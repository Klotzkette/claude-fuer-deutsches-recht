---
name: workflow-redteam-qualitygate
description: "Red-Team-Quality-Gate für das Plugin gewerblicher-rechtsschutz: systematischer letzter Check vor Abgabe von Schriftsätzen, Memos, Abmahnungen und Entscheidungsvorlagen. Sechs Qualitätsstufen, Freigabe-Entscheidung und Dokumentation im Gewerblicher Rechtsschutz."
---

# Workflow: Red-Team Quality Gate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Quality-Gate: Sechs Stufen

### Stufe 1 – Formaler Check (5 Minuten)

**Fragen:**
- [ ] Ist das Dokument vollständig adressiert (Empfänger, Absender, Datum)?
- [ ] Sind alle Anlagen vorhanden und im Text referenziert?
- [ ] Ist das Dokument unterschrieben oder signiert (beA-Pflicht)?
- [ ] Stimmt die Fristangabe im Dokument?
- [ ] Ist das Aktenzeichen korrekt?

**Ergebnis:** Alle Punkte grün → Weiter zu Stufe 2. Sonst korrigieren.

### Stufe 2 – Fristen-Check (3 Minuten)

**Fragen:**
- [ ] Wurde das Dokument rechtzeitig erstellt (Frist noch nicht abgelaufen)?
- [ ] Enthält das Dokument selbst gesetzte Fristen an die Gegenseite?
- [ ] Sind gesetzte Fristen angemessen (nicht zu kurz, nicht zu lang)?
- [ ] Wurde Fristende in Fristenbuch eingetragen?

**Ergebnis:** Fristen korrekt → Weiter zu Stufe 3.

### Stufe 3 – Quellen-Check (10 Minuten)

**Fragen:**
- [ ] Sind alle Normzitate mit Paragrafennummer und aktuellem Gesetzesstand korrekt?
- [ ] Sind alle Rechtsprechungszitate mit Gericht, Datum, AZ und prüfbarer Quelle versehen?
- [ ] Keine BeckRS-Alleinzitate für tragende Aussagen?
- [ ] Behördenangaben (Gebühren, Fristen) live geprüft?
- [ ] Registerdaten (Marke, Patent) mit aktuellem Registerauszug bestätigt?

**Ergebnis:** Alle Quellen geprüft → Weiter zu Stufe 4.

### Stufe 4 – Materieller Check (15 Minuten)

**Fragen (je nach Dokumenttyp):**

**Abmahnung:**
- [ ] Aktivlegitimation eindeutig begründet?
- [ ] Verletzungshandlung tatbestandsmäßig subsumiert?
- [ ] Unterlassungserklärung sachlich korrekt und vollständig?
- [ ] Streitwert / Kosten korrekt?

**EV-Antrag:**
- [ ] Verfügungsanspruch mit Norm und Sachverhalt vollständig?
- [ ] Verfügungsgrund / Dringlichkeit belegt?
- [ ] Glaubhaftmachungspaket vollständig?
- [ ] Tenor nicht zu weit formuliert?

**Memo / Gutachten:**
- [ ] Gutachtenstruktur (Obersatz, Definition, Subsumtion, Ergebnis)?
- [ ] Alle relevanten Tatbestandsmerkmale geprüft?
- [ ] Keine unmarkierten Annahmen?

**Ergebnis:** Material belastbar → Weiter zu Stufe 5.

### Stufe 5 – Gegenargument-Check (10 Minuten)

Systematisch drei Gegenargumente entwickeln und prüfen:

```
Gegenargument 1: _______________
Stärke: [stark / mittel / schwach]
Antwort im Dokument vorbereitet: [Ja / Nein / Teilweise]

Gegenargument 2: _______________
Stärke: [stark / mittel / schwach]
Antwort: [Ja / Nein / Teilweise]

Gegenargument 3: _______________
Stärke: [stark / mittel / schwach]
Antwort: [Ja / Nein / Teilweise]
```

**Ergebnis:** Keine unbehandelten starken Gegenargumente → Weiter zu Stufe 6.

### Stufe 6 – Freigabe-Entscheidung

**Entscheidungskriterien:**

| Entscheidung | Kriterien |
|---|---|
| ✅ FREIGABE | Alle Stufen 1–5 ohne offene rote Punkte |
| ⚠️ FREIGABE MIT VORBEHALT | Ein oder zwei kleinere offene Punkte; nicht wesentlich für Ergebnis |
| 🚫 ZURÜCK ZUR ÜBERARBEITUNG | Wesentlicher materieller Fehler; Quellenproblem; starkes unbehandeltes Gegenargument |

**Freigabe-Protokoll:**
```
QUALITY-GATE PROTOKOLL
Dokument: _______________
Datum: _______________
Reviewer: _______________
Stufe 1 (Formal): _______________
Stufe 2 (Fristen): _______________
Stufe 3 (Quellen): _______________
Stufe 4 (Material): _______________
Stufe 5 (Gegenargument): _______________
Entscheidung: ✅ / ⚠️ / 🚫
Anmerkungen: _______________
```

## Schnell-Quality-Gate (5 Minuten, bei Zeitdruck)

Wenn keine Zeit für vollständiges Quality-Gate:

1. Tenor/Antrag/Kernaussage korrekt?
2. Frist geprüft?
3. Kritische Anlagen vorhanden?
4. Keine offensichtlichen Fehler?

Wenn alle vier Punkte grün: Notfall-Freigabe mit Vorbehalt.

## Typische Freigabe-Blocker

- Tenor zu weit formuliert (Risiko: Gericht lehnt ab oder kürzt erheblich).
- Eidesstattliche Versicherung fehlt (EV-Antrag ohne Glaubhaftmachung).
- Zustellungsnachweis fehlt (Ordnungsmittelantrag ohne Beweis des Vollzugs).
- Schutzrecht abgelaufen (Abmahnung ohne Grundlage).
- Verjährung übersehen.

## Anschluss-Skills

- `spezial-source-red-team-und-qualitaetskontrolle` – Detailliertes Red-Team
- `workflow-rechtsquellen-livecheck` – Quellenprüfung
- `spezial-klausel-beweislast-und-darlegungslast` – Beweisführung
- `workflow-output-waehlen` – Outputformat

