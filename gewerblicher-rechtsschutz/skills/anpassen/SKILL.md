---
name: anpassen
description: "Anpassung und Konfiguration des Plugins gewerblicher-rechtsschutz: Mandatsprofil, Kanzleipräferenzen, Normenauswahl, Sprachstil und Outputformat an konkreten Bedarf anpassen. Skill für Kanzleien, die den Plugin-Rahmen ihrem Arbeitsalltag anpassen wollen im Gewerblicher Rechtsschutz: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Gewerblicher Rechtsschutz: Plugin anpassen

## Arbeitsbereich

Anpassung und Konfiguration des Plugins gewerblicher-rechtsschutz: Mandatsprofil, Kanzleipräferenzen, Normenauswahl, Sprachstil und Outputformat an konkreten Bedarf anpassen. Skill für Kanzleien, die den Plugin-Rahmen ihrem Arbeitsalltag anpassen wollen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck und Mandatsbezug

Dieser Skill ermöglicht die **Anpassung des Plugins `gewerblicher-rechtsschutz`** an das spezifische Mandatsprofil einer Kanzlei, eines Rechtsabteilungsleiters oder eines spezialisierten Beratungsunternehmens. Er steuert, welche Normen vorrangig geprüft werden, welcher Sprachstil verwendet wird, welche Gerichte und Behörden typischerweise relevant sind und welches Outputformat bevorzugt wird.

Mandatsbezug: Kanzlei mit Schwerpunkt Markenrecht nutzt das Plugin anders als ein Patentanwalt im Maschinenbaubereich. Rechtsabteilung eines Software-Unternehmens benötigt andere Standardabfragen als ein auf Abmahnungen spezialisierter Klagenanwalt.

## Konfigurationsdimensionen

### 1. Mandatsprofil und Rollenstruktur

Das Plugin kann auf verschiedene Nutzerrollen kalibriert werden:

| Rolle | Fokus | Typische Aufgaben |
|---|---|---|
| Fachanwalt GewRS | Vollständiges IP-Recht | Abmahnung, Klage, Vergleich, Beratung |
| Patentanwalt | PatG, DesignG, ArbnErfG | Anmeldung, FTO, EV, Lizenz |
| Rechtsabteilung Industrie | UWG, MarkenG, PatG | Compliance, Lizenz, Abwehr |
| Startup-Berater | MarkenG, UWG, UrhG | Anmeldung, Erstschutz, Abmahnung-Reaktion |
| Richter/Rechtspfleger | Alle Normen | Verfahrensrechtliche Fragen |

**Konfigurationsabfrage:** Welche Rolle ist primär? Wird das Plugin von einer einzelnen Person oder einem Team genutzt?

### 2. Normenprioritäten

Je nach Kanzleiprofil können unterschiedliche Normengruppen priorisiert werden:

- **Markenrecht:** MarkenG, CTMR (VO (EU) 2017/1001), Madrider System, WIPO-UDRP
- **Patentrecht:** PatG, EPÜ, PCT, GebrMG, ArbnErfG
- **Lauterkeitsrecht:** UWG, Richtlinie 2005/29/EG (UGP-RL), Richtlinie 2006/114/EG (Vergleichende Werbung)
- **Urheberrecht:** UrhG, InfoSoc-Richtlinie (2001/29/EG), DSM-Richtlinie (2019/790)
- **Designrecht:** DesignG, Gemeinschaftsgeschmacksmuster-VO (6/2002)
- **Prozessrecht:** ZPO (einstweiliger Rechtsschutz §§ 916 ff.), GKG (Streitwert)

**Konfigurationsabfrage:** Welche Normengruppen dominieren im Alltag?

### 3. Gerichtsstands- und Behördenpräferenzen

Das Plugin kann auf bestimmte Gerichte und Behörden ausgerichtet werden:

- **Patentgericht:** Bundespatentgericht München, EPA (Einspruch, Beschwerde)
- **Markengerichte:** DPMA, EUIPO, LG Hamburg/München/Frankfurt/Düsseldorf für EV
- **Zivilgerichte:** LG mit Spezialkammer GewRS; OLG
- **Behörden:** DPMA (Anmeldung, Widerspruch, Löschung), EUIPO

**Konfigurationsabfrage:** Welche Gerichte und Behörden sind im Arbeitsalltag am häufigsten relevant?

### 4. Sprachstil und Fachtonalität

| Stil | Einsatz |
|---|---|
| Juristisch-präzise (Gutachtenstil) | Schriftsätze, Memos für Anwälte |
| Mandantenfreundlich | Mandantenbriefe, Erstgespräche |
| Tabellarisch-komprimiert | Interne Arbeitsmaterialien |
| Bilinguale Ausgabe (DE/EN) | Internationale Mandate |

**Konfigurationsabfrage:** In welchem Sprachstil sollen Outputs standardmäßig erzeugt werden?

### 5. Outputformat-Präferenzen

- **Memo:** Kurzgutachten, 1–3 Seiten, Ergebnis zuerst.
- **Checkliste:** Strukturierter Prüfpfad mit Abhakpunkten.
- **Schriftsatz-Entwurf:** Vollständiger Klage-, Antrags- oder Briefentwurf.
- **Tabelle/Matrix:** Normen × Tatbestandsmerkmale × Tatsachen.
- **Fristenplan:** Chronologischer Überblick mit Verantwortlichkeiten.
- **Red-Team:** Gegenargumente und Schwachstellenanalyse.

**Konfigurationsabfrage:** Welches Outputformat ist Standard, welches Ausnahme?

## Kaltstart-Konfigurationsgespräch

Zu Beginn eines neuen Kanzleiprofils:

1. **Kanzlei/Organisation:** Name, Größe, Standort, Fachgebiet-Schwerpunkte.
2. **Typisches Mandat:** Abmahner oder Abgemahnter? Anmelder oder Verletzer? International oder national?
3. **Normen-Ranking:** Welche drei Normengruppen kommen täglich vor?
4. **Bevorzugte Gerichte:** Welche LG/OLG/BGH-Kammern werden regelmäßig bespielt?
5. **Output-Präferenz:** Schriftsatz, Checkliste, Tabelle oder Kurzgutachten?
6. **Sprache:** Deutsch, Englisch oder bilingual?

## Anpassungsworkflow

### Schritt 1 – Profil dokumentieren

Aus dem Kaltstart-Gespräch ein kurzes Kanzleiprofil erzeugen:
```
Kanzleiprofil:
- Schwerpunkt: [Marken/Patent/UWG/Urheberrecht]
- Typische Mandantenrolle: [Antragsteller/Antragsgegner/Anmelder/Lizenznehmer]
- Primäre Gerichte: [LG …, OLG …, BGH]
- Normen-Priorität: [MarkenG, UWG, ZPO §§ 916 ff.]
- Outputformat-Standard: [Memo/Checkliste/Schriftsatz]
- Sprache: [Deutsch/Englisch]
```

### Schritt 2 – Skills-Routing anpassen

Basierend auf Profil empfehlen, welche Fachmodule bevorzugt genutzt werden sollten:
- Marken-Schwerpunkt → `markenrecherche`, `markenanmeldung-dpma`, `unterlassungsverlangen`
- Patent-Schwerpunkt → `fto-triage`, `erfindungsmeldung-aufnahme`, `schutzrechts-portfolio`
- UWG-Schwerpunkt → `gewr-uwg-abmahnung-checkliste`, `verletzungs-triage`
- EV-Schwerpunkt → `evvollzug-neu-001` bis `evvollzug-neu-008`

### Schritt 3 – Dauereinstellungen festhalten

- Häufig genutzte Streitwert-Tabellen: z.B. OLG Hamburg Streitwertpraxis.
- Regelmäßige Fristen: DPMA-Widerspruchsfrist 3 Monate, Neuheitsfrist PatG, EUIPO-Fristen.
- Vorlagen-Bibliothek: Welche Schriftsatz-Vorlagen wurden bereits angepasst?

## Qualitätssicherung nach Anpassung

- Nach Profilkonfiguration: Testfall mit einem typischen Mandat durchführen.
- Prüfen: Stimmen Normenreferenzen, Gerichtsstand, Outputformat?
- Anpassen: Falls Output nicht passt, Profil verfeinern.
- Periodisch: Plugin bei Gesetzesänderungen (z.B. neue UWG-Novelle, MarkenG-Reform) aktualisieren.

## Quellenregel

- Normänderungen über [gesetze-im-internet.de](https://www.gesetze-im-internet.de) live prüfen.
- DPMA-Praxis über [dpma.de](https://www.dpma.de) aktuell halten.
- EUIPO-Richtlinien über [euipo.europa.eu](https://www.euipo.europa.eu) nachverfolgen.
- Keine BeckRS-Blindzitate; bei spezifischen Gerichtspraxisfragen: Live-Check.

## Anschluss-Skills

- `workflow-kaltstart-und-routing` – Erstgesprächs-Router
- `mandat-triage-gewerblicher-rechtsschutz` – Mandatstriage
- `allgemein` – Plugin-Übersicht
- `gewerblicher-rechtsschutz-kaltstart-interview` – Kaltstart-Interview für neues Mandat
