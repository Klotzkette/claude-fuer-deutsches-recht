---
name: open-source-pruefung
description: "Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet GPL LGPL MIT Apache genehmigungsfähige Bibliotheken. Output: Compliance-Bericht mit Handlungsempfehlungen je Abhaengigkeit. Abgrenzung zu ip-klausel-prüfung (vertragliche IP) und fto-triage (Patente) im Gewerblicher Rechtsschutz: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Open-Source-Lizenz-Compliance-Prüfung

## Arbeitsbereich

Unternehmen will Software ausliefern oder als Open Source veroffentlichen und fragt nach Lizenz-Compliance. Open-Source-Lizenz-Compliance. Prüfraster: Manifest SBOM Repository Copyleft-Pflichten Lizenzkompatibilitaet GPL LGPL MIT Apache genehmigungsfähige Bibliotheken. Output: Compliance-Bericht mit Handlungsempfehlungen je Abhaengigkeit. Abgrenzung zu ip-klausel-prüfung (vertragliche IP) und fto-triage (Patente). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Diese Skill teilt mit, welche Lizenzen im Abhängigkeitsbaum enthalten sind, welche Pflichten diese Lizenzen angesichts des Einsatzmodells auslösen, und was für jede einzelne Abhängigkeit zu tun ist: Pflichten erfüllen, ersetzen, entfernen, anwaltliche Prüfung einholen oder kommerzielle Lizenz beschaffen.

Dies ist eine Erstklassifikation. Copyleft-Analysen hängen vom Einsatzmodell, der Einbindungstiefe, der Rechtsordnung und bisweilen von noch nicht gerichtlich geklärten Rechtsfragen ab (insbesondere AGPL-Netzwerktrigger, GPL-3.0-Patentklausel). Alles was als starkes Copyleft oder unklare Lizenz eingestuft wird, geht vor Auslieferung oder Veröffentlichung an einen Rechtsanwalt. Die Skill liefert den Befund; der Anwalt entscheidet.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

1. **Was wird geprüft?**
 - Abhängigkeitsliste (`package.json`, `requirements.txt`, `go.mod`, `Gemfile`, `Cargo.toml`, `pom.xml`, SBOM nach SPDX / CycloneDX, Lockfile)
 - Einzelne Bibliothek — ein konkretes Paket, das hinzugefügt werden soll
 - Eigener Code — Vorbereitung zur Open-Source-Veröffentlichung

2. **Einsatzmodell** (vor Klassifikation der Pflichten zwingend festlegen):
 - SaaS / gehosteter Dienst — Nutzer greifen über Netz zu; kein Code wird ausgeliefert
 - Distribuiertes Programm — kompilierter Code wird ausgeliefert (Desktop-App, Mobile-App, On-Prem-Server, CLI)
 - Nur intern — ausschließlich im Unternehmen genutzt, keine Auslieferung nach außen
 - Eingebettet / Firmware — ausgeliefert in Hardware oder als Closed-System-Firmware

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 69a ff. UrhG** — Urheberrechtsschutz für Computerprogramme; § 69b UrhG Arbeitnehmerprogramme
- **§ 31 Abs. 1 UrhG** — Einfaches und ausschließliches Nutzungsrecht; Copyleft-Lizenzen räumen einfache Nutzungsrechte unter Bedingungen ein
- **§ 31 Abs. 5 UrhG** — Zweckübertragungslehre: Im Zweifel nur für Vertragszweck erforderliche Rechte; Copyleft-Bedingungen müssen explizit akzeptiert werden
- **§ 97 UrhG** — Unterlassungs- und Schadensersatzanspruch bei Lizenzverletzung; Grundlage für GPL-Enforcement-Klagen
- **§§ 14, 15 UrhG** — Bearbeitungsrecht, Verwertungsrechte; Copyleft wirkt über das Bearbeitungsrecht

### Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Spindler, in: Schricker/Löwenheim, UrhG, 6. Aufl. 2020, § 69a Rn. 1 (Softwareschutz allgemein)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Dreier, in: Dreier/Schulze, UrhG, 7. Aufl. 2022, § 31 Rn. 60 (Nutzungsrechtseinräumung, Copyleft-Mechanismus)
- Metzger/Jaeger, Open Source Software und deutsches Urheberrecht, GRUR Int. 1999, 839 (847) — Grundlagenaufsatz zur Wirksamkeit der GPL nach deutschem Recht

## Ablauf

### Schritt 1: Prüfungsumfang klären

Aus dem Übergabematerial ableiten oder fragen:

- Abhängigkeitsliste → alle Einträge klassifizieren, Pflichten aufrollen
- Einzelbibliothek → ein Paket klassifizieren, transitive Abhängigkeiten soweit verfügbar
- Ausgehender Code → Was ist eingebettet (direkt und transitiv)? Ist die gewählte Ausgangslizenz mit allen eingebetteten Lizenzen kompatibel? Sind LICENSE/NOTICE-Dateien korrekt?

### Schritt 2: Einsatzmodell festlegen

Das Einsatzmodell bestimmt, welche Copyleft-Pflichten ausgelöst werden:

| Einsatzmodell | Wesentliche Lizenzen |
|---|---|
| SaaS | AGPL-3.0 (Netzwerktrigger), Attribution bei Permissive in der UI, SSPL/BUSL/Elastic bei konkurrierendem Dienst |
| Distribuiertes Programm | GPL-2.0, GPL-3.0, LGPL, MPL, EPL (alle greifen bei Distribution); Permissive Attribution |
| Nur intern | Kein Copyleft-Auslöser bei interner Nutzung ohne Distribution. AGPL greift dennoch, wenn externe Nutzer über Netz zugreifen. Permissive Attribution gute Praxis. |
| Embedded / Firmware | GPL besonders schwer erfüllbar (Quellcodeoffenlegung + reproduzierbarer Build + Installationsinfo); vor Auslieferung planen |

Einsatzmodell im Ausgabevermerk kennzeichnen.

### Schritt 3: Jede Abhängigkeit klassifizieren

Nicht nur Metadaten lesen — tatsächlichen Lizenztext prüfen. LICENSE-Dateien können falsch sein; Package-Metadaten können veraltet sein.

Klassifikation:

| Kategorie | Beispiele | Wesentliche Pflichten |
|---|---|---|
| **Permissiv** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC | Attribution, Lizenztextbeibehaltung; Apache-2.0 ergänzend Patentlizenz + NOTICE-Pflicht |
| **Schwaches Copyleft** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0, CDDL | Datei- oder bibliotheksweite Quellcodeoffenlegung; Verlinkungsregeln variieren |
| **Starkes Copyleft** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (je nach Version) | Breite Quellcodeoffenlegung; AGPL erstreckt sich auf Netzwerknutzung |
| **Public Domain / Widmung** | CC0, Unlicense, WTFPL | Keine Pflichten; aber: Public-Domain-Widmung nicht in allen Rechtsordnungen anerkannt (in Deutschland fraglich, §§ 29, 64 UrhG) |
| **Nicht-OSI Source-Available** | SSPL, BUSL, Commons Clause, Elastic License, Fair Source | Kein Open Source — schränken kommerzielle oder konkurrierende Nutzung ein; Lizenztext lesen |
| **Unbekannt / Proprietär** | Vendor-spezifisch, fehlendes Lizenz-File, Widerspruch File vs. Headers | Stopp — nicht als Permissiv behandeln |

Besonders kennzeichnen:

- **Dual-lizenzierte Pakete** — welche Lizenz nutzen wir? Wahl kann Pflichten ändern.
- **Veraltete Pakete** — kein aktiver Maintainer; gibt es einen gepflegten Ersatz?
- **Copyleft in transitiver Abhängigkeit** — Toplevel-Lizenz ist permissiv, aber eine transitive Abhängigkeit ist Copyleft.
- **Lizenswechsel bei bekannten Projekten** — Redis, MongoDB, Elastic, HashiCorp haben relizenziert; angepinnte Version prüfen.

### Schritt 4: Pflichten auf Einsatzmodell abbilden

Für jedes klassifizierte Paket:

```markdown
### [Paket@Version] — [Lizenz]

**Klassifikation:** [Permissiv / Schwaches Copyleft / Starkes Copyleft / Public Domain / Nicht-OSI / Unbekannt]

**Pflichten für unser Einsatzmodell ([SaaS / Distribuiert / Intern / Embedded]):**

- [ ] [Konkrete Pflicht — z. B. "Attribution in NOTICES-Datei, die mit der App ausgeliefert wird"]
- [ ] [z. B. "Bei Modifikation und Distribution: Quellcode der Änderungen veröffentlichen"]
- [ ] [z. B. "AGPL-Netzwerktrigger — wenn Nutzer über Netz auf unsere modifizierte Version zugreifen, Quellcode anbieten"]

**Risiko:** 🔴 Kritisch | 🟠 Hoch | 🟡 Mittel | 🟢 Niedrig

**Empfehlung:** [Pflichten erfüllen | Ersetzen durch [Alternative] | Entfernen | Anwaltliche Prüfung vor Auslieferung | Kommerzielle Lizenz bei [Anbieter] beschaffen]
```

**Verlinkungsbeziehung bestimmt den Schweregrad:**

- **Statische Verlinkung / gemeinsame Kompilierung:** Werke zu einem Binary vereint. Starkes Signal für Copyleft-Auslösung.
- **Dynamische Verlinkung / Shared Library:** Werke zur Laufzeit trennbar. LGPL explizit erlaubt (§ 6 LGPL — "work that uses the Library"). GPL-Position umstritten.
- **Header-Einbindung / Inline-Funktionen:** Kann abhängig von Einbindungstiefe ein abgeleitetes Werk begründen.
- **Subprozess / IPC:** Getrennte Prozesse über wohldefinierte Schnittstellen. Im Regelfall kein abgeleitetes Werk.
- **Netzwerk-API-Aufruf:** Für die meisten Lizenzen kein Auslöser. Für **AGPL-3.0**: Bereitstellung der Software über Netz gilt als Verbreitung — auch AGPL-Komponente hinter einer API triggert in einer Microservice-Architektur.
- **Dateiweises Copyleft (MPL):** Nur modifizierte Dateien tragen das Copyleft, nicht das gesamte Werk.

**Schweregrad-Kalibrierung:**

| Stufe | Bedeutung |
|---|---|
| 🔴 Kritisch | Starkes Copyleft in einem Einsatzmodell, das es auslöst (GPL in distribuiertem Binary, AGPL in SaaS). Nicht-OSI-Lizenz, die dem Geschäftsmodell widerspricht (z. B. SSPL bei gebautem verwaltetem Dienst). Lizenz nicht bestimmbar bei tragender Abhängigkeit. |
| 🟠 Hoch | Schwaches Copyleft mit Pflichten, die noch nicht eingerichtet sind (Dateilevel-Disclosure, NOTICE-Anforderungen). Dual-lizenziert mit unklarer Lizenzwahl. Lizenzdatei widerspricht File-Headern. |
| 🟡 Mittel | Permissiv mit noch nicht umgesetzten Attributionspflichten (fehlende NOTICES-Datei). Transitive Copyleft-Abhängigkeit, die je nach Einbindung greifen kann oder nicht. |
| 🟢 Niedrig | Permissiv mit bereits erfüllten Pflichten. Copyleft in einem Einsatzmodell, das es nicht auslöst (GPL-Bibliothek nur intern, keine Distribution). |

### Schritt 5: Kritische Befunde am Anfang des Vermerks kennzeichnen

- **Lizenz unbekannt** — als "Prüfung erforderlich" klassifizieren, nicht als Permissiv. Unklassifizierte Abhängigkeit sollte eine Lieferentscheidung aufhalten.
- **Lizenzdatei widerspricht File-Headern** — beide lesen und Widerspruch melden.
- **Inkompatible Kombinationen** — GPL-2.0-only + Apache-2.0 historisch bekannte Inkompatibilität; MPL / EPL / GPL-Kombinationen sorgfältig prüfen.
- **Nicht-OSI-Lizenzen als Open Source getarnt** — SSPL, BUSL, Commons Clause, Elastic License. Lizenztexte lesen; nicht dem GitHub-"Open Source"-Badge vertrauen.
- **Lizenswechsel** — wenn Vorgängerversion permissiv und aktuelle Version Source-Available ist: angepinnte Version entscheidet.

### Schritt 6: Ausgehende Prüfung (nur bei Code-Veröffentlichung als Open Source)

- Gewählte Ausgangslizenz mit jeder eingebetteten Abhängigkeitslizenz kompatibel? (Kein MIT-Release bei eingebettetem GPL-Code möglich — das kombinierte Werk muss GPL sein)
- LICENSE-Datei vorhanden und korrekt?
- NOTICE-Datei vorhanden mit erforderlichen Attributionen (Apache-2.0 u. a.)?
- Drittlizenz-Texte gebearbeitet wo erforderlich?
- Kein proprietärer oder vertraulicher Code, keine Kundendaten, keine eingebetteten Zugangsdaten in der Repository-History?
- Marken- und Markenrechtsrichtlinien für den Projektnamen geprüft (getrennt von der Urheberrechtslizenz)?

### Schritt 7: Vermerk zusammenstellen

```markdown
[ARBEITSERGEBNIS-KOPFZEILE]

# OSS-Lizenz-Prüfung: [Projekt / Abhängigkeitsliste / Paket]

**Geprüft:** [Datum]
**Umfang:** [Abhängigkeitsliste / Einzelbibliothek / Ausgehender Code]
**Einsatzmodell:** [SaaS / Distribuiert / Intern / Embedded]

---

## Ergebnis

[Zwei Sätze. Kann ausgeliefert werden? Was muss zuerst passieren?]

**Geprüfte Pakete:** [N]
**Nach Klassifikation:** [N permissiv, N schwaches Copyleft, N starkes Copyleft, N Public Domain, N Nicht-OSI, N unbekannt]
**Befunde:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Genehmigung erforderlich von:** [Name, gemäß Mandatsprofil]

---

## Kritische Anfangshinweise

[Unbekannte Lizenzen, Lizenz-Konflikte, Nicht-OSI als OSS getarnt, inkompatible Kombinationen]

---

## Nach Paket

[Blöcke aus Schritt 4, nach Schweregrad gruppiert]

---

## Rechtsordnungshinweis

OSS-Lizenz-Durchsetzbarkeit variiert: Der AGPL-Netzwerkauslöser ist in Deutschland grundsätzlich durchsetzbar (vgl. LG München I); Public-Domain-Widmungen sind im deutschen Recht problematisch (§§ 29, 64 UrhG — kein vollständiger Rechteentzug möglich, nur schuldrechtliche Abreden). Anwendbares Recht für Downstream-Distribution (z. B. bei Kunden in anderen Jurisdiktionen) und Mandatsprofil-Flaggen beachten.

---

## Ausgehende Prüfung (soweit einschlägig)

[Aus Schritt 6]

---

## Weiterleitungshinweise

[Wer genehmigt; was löst automatische Eskalation aus]
```

## Ausgabeformat

Vermerk mit Arbeitsergebnis-Kopfzeile, Gesamtbewertung, kritischen Anfangshinweisen, Paketblöcken nach Schweregrad, Rechtsordnungshinweis, ausgehende Prüfung (falls einschlägig), Weiterleitungshinweise.

## Beispiel

**Eingabe:** `requirements.txt` eines Python-SaaS-Projekts enthält `flask-login` (MIT), `celery` (BSD-3-Clause), `cryptography` (Apache-2.0/BSD), `mysqlclient` (GPL-2.0).

**Befund (Auszug):**

> ### mysqlclient@2.1.1 — GPL-2.0
>
> **Klassifikation:** Starkes Copyleft
>
> **Pflichten für unser Einsatzmodell (SaaS):**
> - [ ] Kein Distributions-Auslöser bei reiner SaaS-Nutzung — Quellcodeoffenlegungspflicht der GPL trifft grundsätzlich auf physische Distribution
> - [ ] AGPL-Auslöser gilt nicht für GPL-2.0 — jedoch: falls künftig Binary ausgeliefert wird, entsteht Pflicht
> - [ ] Kommerziell: MySQL Connector/Python (proprietäre Lizenz) oder `PyMySQL` (MIT) als Alternative prüfen
>
> **Risiko:** 🟡 Mittel (SaaS ohne Distribution) / 🔴 Kritisch (bei künftiger Binary-Distribution)
>
> **Empfehlung:** Ersetzen durch `PyMySQL` (MIT) zur Risikominimierung; alternativ anwaltliche Prüfung ob SaaS-Einsatz tatsächlich GPL-frei bleibt.

## Risiken und typische Fehler

- **GPL-Durchsetzbarkeit in Deutschland unterschätzen:** Deutsche Gerichte haben GPL-Bedingungen konsequent durchgesetzt (LG München I, BGH). Verstöße führen automatisch zum Verlust des Nutzungsrechts.
- **AGPL-Netzwerkauslöser ignorieren:** Bei SaaS-Anwendungen, die AGPL-Komponenten nutzen, muss der gesamte Quellcode den Nutzern angeboten werden — auch ohne physische Distribution.
- **Public Domain im deutschen Recht:** § 64 UrhG: Urheberrecht erlischt 70 Jahre nach Tod des Urhebers. Eine "Widmung" in die Gemeinfreiheit ist deutschrechtlich nicht vollständig möglich; CC0 ist die bestmögliche Annäherung.
- **Dynamische vs. statische Verlinkung:** Gleiche Lizenz, entgegengesetztes Ergebnis. LGPL + statisch gelinkt = 🔴; LGPL + dynamisch gelinkt = 🟢.
- **Lizenswechsel nicht erkannt:** Angepinnte Version bestimmt die Lizenz — nicht die aktuelle Upstream-Version.

## Quellenpflicht

Alle Klassifikationen und Pflichtaussagen müssen belegbar sein:

- **Gesetze:** §§ 31, 69a, 97 UrhG
- **Rechtsprechung:** mindestens eine Entscheidung zur GPL-Durchsetzbarkeit (LG München I oder BGH Afterlife)
- **Lizenztext:** direkt aus dem Repository oder SPDX; als `[Lizenztext gelesen — [Quelle]]` kennzeichnen
- **Kommentar oder Aufsatz:** Schricker/Löwenheim UrhG oder Metzger/Jaeger GRUR Int. 1999 mit Seitenangabe
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen vor Open-Source-Pruefung

Bevor die Lizenz-Compliance-Analyse beginnt, klaere:
1. Handelt es sich um statische oder dynamische Verlinkung (entscheidend fuer GPL vs. LGPL-Frage)?
2. Wird die Software als SaaS-Dienst betrieben (AGPL: Netzwerk-Austauschklausel — Quellcode-Pflicht auch ohne Distribution)?
3. Sind alle Abhaengigkeiten in der Dependency-Liste erfasst (transitive Dependencies often missed)?
4. Ist ein SBOM (Software Bill of Materials) erstellt (Compliance-Dokumentation, EU Cyber Resilience Act)?

## Aktuelle Rechtsprechung

> Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
