---
name: projekt-arbeitsweise
description: "Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan Immobilienrechtsmandat. Abgrenzung: nicht Einzelverfahren im Immobilienrechtspraxis."
---

# Projekt-Arbeitsweise Immobilienrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Projekt-Arbeitsweise Immobilienrecht
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.

## Leitidee

Freihaendiges Prompting funktioniert für einzelne Aufgaben aber
nicht für dauerhafte Mandate. Eine immobilienrechtliche
Rechtsabteilung arbeitet projektbezogen — pro Objekt pro
Transaktion pro Mietverhältnis. Der Skill legt Projekt-Skelette
an und fixiert die Vorgaben so dass eingehende Dokumente immer
gegen denselben Maßstab geprüft werden.

## Inputs

- Projekt-Bezeichnung (Objekt Aktenzeichen Transaktion)
- Optional: hauseigenes Playbook Musterverträge Klauselkatalog
- Optional: AVV-Anforderungen der Abteilung
- Optional: Compliance-Vorgaben (zB Geldwäschegesetz
 Sanktionslisten)

## Projekt-Skelett

```
<Projekt>/
 00_Projekt-Setup/
 vorgaben.md
 playbook.md
 musterklauseln.md
 avv-anforderungen.md
 zitierregeln.md
 01_Verträge/
 02_Korrespondenz/
 03_Schriftsätze/
 04_Recherche/
 05_Mandantenkontakt/
 06_Ablage/
 audit.md
```

`vorgaben.md` ist die zentrale Konfiguration. Sie nennt:

- Rechtsgebiet und Schwerpunkte
- Welche Skills bei welchem Dokumenttyp auslösen
- Welches Playbook gilt
- Welche Musterverträge als Referenz dienen
- Welche AVV-Anforderungen zwingend sind
- Welche Zitierregeln gelten

## AVV-Prüfung nach Art. 28 DSGVO

Eingehende AVV oder AV-Verträge werden gegen den Mindestkatalog
nach Art. 28 Abs. 3 DSGVO geprüft:

- Gegenstand und Dauer der Verarbeitung
- Art und Zweck der Verarbeitung
- Art der personenbezogenen Daten
- Kategorien betroffener Personen
- Pflichten und Rechte des Verantwortlichen
- Weisungsgebundenheit
- Vertraulichkeit
- Sicherheit der Verarbeitung Art. 32 DSGVO
- Unterauftragsverarbeiter
- Unterstützung bei Betroffenenrechten Art. 12-22 DSGVO
- Unterstützung bei Meldepflichten Art. 33 und 34 DSGVO
- Löschung oder Rückgabe nach Vertragsende
- Nachweise und Audit-Rechte

Ausgabe: Ampelmatrix mit Hinweis welche Pflichtangabe fehlt oder
abweicht.

## Interne Compliance-Vorgaben

Falls in `vorgaben.md` hinterlegt werden zusätzlich geprüft:

- Sanktionslisten und Embargo-Vorgaben
- Geldwäschegesetz — Kenntnis des wirtschaftlich Berechtigten bei
 Immobilien-Transaktionen § 3 GwG
- Mindest-Vertragsstrafen bei Geheimhaltungsverletzung
- Maximal akzeptierte Indexierungs-Schwellen bei
 Gewerbemietverträgen
- Schriftform-Mindestanforderungen Gewerbemiete § 550 BGB

## Auto-Routing

Der Skill ordnet eingehende Dokumente auf Basis von
Dateiname und Inhalt einem Unterordner zu. Auslöser-Regeln aus
`vorgaben.md`:

- Verträge mit Begriffen Mietvertrag Kaufvertrag in
 `01_Verträge/`
- Schreiben Email-Exports in `02_Korrespondenz/`
- Schriftsätze mit Begriffen Klage Erwiderung Berufung in
 `03_Schriftsätze/`

Pro eingehendem Dokument wird ein Eintrag in `audit.md` gesetzt:
Zeitpunkt Quelle Empfänger angewandte Pruefskills Ergebnis.

## Integration mit anderen Skills

Der Skill ist Hub für die anderen Skills des Plugins:

- Eingehender Vertrag → `vertragspruefung-playbook`
- Eingehende Mandanten-Korrespondenz mit Mängelanzeige →
 `mieteranfragen-bearbeitung`
- Grundbuch-PDFs → `grundbuchanalyse`
- Fragmentarische Sachverhalts-Unterlagen →
 `sachverhaltsermittlung`
- Komplette Mandats-Erstaufbereitung → `memorandums-ersteller`
 (separates Plugin)

## Agenten-Workflows

Der Skill ist so gebaut dass ein Agent auf einen Watch-Ordner
reagieren kann. Sobald ein PDF in `00_Inbox/` landet wird auf
Basis der `vorgaben.md` automatisch der passende Skill gestartet
und das Ergebnis in den richtigen Unterordner geschrieben.

## Nachvollziehbarkeit und Audit

Jede Änderung an `vorgaben.md` ist versioniert. Jede
Skill-Ausführung steht in `audit.md` mit Eingabe-Datei und
Ergebnis-Datei. Bei Prüfung durch Aufsicht oder Geschäftsleitung
ist nachvollziehbar wer wann mit welchen Vorgaben geprüft hat.

## Output beim Setup

- Projekt-Verzeichnisbaum
- `vorgaben.md` ausgefüllt mit den getroffenen Festlegungen
- `audit.md` mit Eintrag Setup
- Optional Vorlage-Dateien aus `00_Projekt-Setup/` befüllt

## Beispielformulierungen

- "Lege ein Projekt für das Bürogebäude Friedrichstraße 100
 an. Playbook Gewerbemiete Standard. AVV-Prüfung Pflicht."
- "Prüfe diesen eingehenden AVV nach Art. 28 DSGVO und unsere
 internen Vorgaben."
- "Routinge die letzten 30 eingehenden Mails in die richtigen
 Projekt-Ordner."
- "Erzeuge audit.md für den Quartalsbericht — welche Skills
 wurden im Projekt Erbpacht Tegel zwischen Januar und März
 angewandt?"

## Aktuelle Rechtsprechung — Projekt-relevante Normen

## Paragrafenkette Projekt-Setup

- Mandatsdokumentation: BRAO § 43, BORA § 1 ff.
- Datenschutz: Art. 6 DSGVO, Art. 28 DSGVO (AVV)
- GwG-Dokumentation: §§ 10 ff. GwG
- Aufbewahrungspflicht: § 50 StBerG analog, Steuerrecht 10 Jahre

