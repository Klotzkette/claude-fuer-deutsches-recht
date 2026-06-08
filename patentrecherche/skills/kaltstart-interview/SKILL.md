---
name: kaltstart-interview
description: "Kaltstart-Interview für das Patentrecherche-Plugin. Stellt fest wer recherchiert (Patentanwaeltin Patentanwalt Patentassessor Patentingenieur Recherchekraft) welche Kanzlei und welche Technikgebiete (Mechanik Elektrotechnik Chemie Biotech Informatik Verfahrenstechnik) welcher Mandant und welcher Recherchezweck (Stand der Technik vor Anmeldung Einspruch Nichtigkeit Freedom to Operate Konkurrenten-Monitoring Prüfungsbescheid-Antwort) welcher Rechtsraum (DPMA EPA WIPO USPTO weltweit) und mit welchen Datenbankzugaengen (kostenfrei Espacenet Google Patents oder Bezahl-Zugaenge wie PatBase STN Orbit Questel). Schreibt das Profil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/patentrecherche/CLAUDE.md. Disclaimer Vorrecherche ersetzt keine amtliche Recherche und keine Eigenprüfung der Patentanwaeltin."
---

# kaltstart-interview

## Zweck

Beim ersten Einsatz des Plugins wird das Anwender-Profil erfasst, damit die anschließenden Skills passend zur Kanzlei und zum Technikgebiet arbeiten. Das Interview läuft einmal je Kanzlei und wird bei Bedarf aktualisiert.

## Ablauf

Frage in dieser Reihenfolge, jeweils mit Kurzbegründung:

### 1. Wer recherchiert

- Patentanwältin / Patentanwalt
- Patentassessorin / Patentassessor (im 2. Examensjahr)
- Patentingenieurin / Patentingenieur (technische Mitarbeit)
- Externe Recherchekraft / Recherchezentrum
- Rechtsanwältin / Rechtsanwalt mit gewerblichem-Rechtsschutz-Schwerpunkt (sonst auf `gewerblicher-rechtsschutz` verweisen)

### 2. Kanzlei

- Name, Standort
- Größe (Einzelkanzlei, mittelgroße Kanzlei, internationale Großkanzlei)
- Verbindung mit Anwaltssozietät (gemischte Kanzlei)?

### 3. Technikgebiete

Mehrfachauswahl:

- Mechanik / Maschinenbau
- Elektrotechnik / Halbleiter
- Chemie / Pharma
- Biotechnologie / Life Sciences
- Informatik / Software / KI
- Verfahrenstechnik
- Medizintechnik / MedTech
- Werkstofftechnik
- Automotive
- Sonstiges (Freitext)

Hieraus ergeben sich Schwerpunktklassen in CPC und IPC, die im Skill `klassifikation-cpc-ipc` als Default vorgeschlagen werden.

### 4. Datenbankzugänge

- **Frei zugänglich (Standard):** Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO Patent Public Search.
- **Bezahl-Zugänge (optional, deutlich leistungsfähiger):** PatBase (Minesoft), STN (FIZ Karlsruhe), Orbit (Questel), Derwent Innovations Index, GenomeQuest (Biotech-Sequenzen).
- **Fachdatenbanken:** Lexis Nexis Patent Advisor, Patsnap, IPlytics.

Wenn nur freie Datenbanken: Hinweis, dass agentische Bedienung dort funktioniert. Wenn Bezahl-Zugänge: Hinweis, dass Bezahl-DBs **nicht** agentisch bedient werden — sie bleiben in der manuellen Recherche der Patentanwältin.

### 5. Typische Mandantenstruktur

- Industrie / Konzern
- Mittelstand
- Start-ups
- Hochschulen / Forschungseinrichtungen
- Einzelerfinder
- Inhouse-Mandant (Patentanwältin in Konzern-IP-Abteilung)

### 6. Typische Recherchezwecke

Welche der folgenden Recherchen kommen in der Kanzlei vor (Mehrfachauswahl):

- Vorrecherche vor Patentanmeldung (Stand der Technik, Neuheit)
- Recherche zur Erstellung der Beschreibung / des Anspruchs
- Antwort auf Prüfungsbescheid (DPMA / EPA)
- Einspruchsrecherche (EPA Art. 99 ff. EPÜ, DPMA § 59 PatG)
- Nichtigkeitsrecherche (BPatG § 81 PatG)
- Freedom-to-Operate (FTO) vor Markteintritt
- Monitoring / Überwachung Konkurrenten
- Due Diligence Patent-Portfolio (M&A)
- Sachverständigentätigkeit Verletzungsverfahren

### 7. Rechtsraum-Schwerpunkt

- Deutschland (DPMA)
- Europa (EPA / EPÜ-Staaten)
- PCT (WIPO)
- USA (USPTO)
- Asien (JPO Japan, KIPO Korea, CNIPA China)
- Global

### 8. Verschwiegenheit / KI-Vertrag

Frage: Wurde der Einsatz des KI-Dienstleisters berufsrechtlich nach § 39c PAO und § 203 Abs. 4 StGB geprüft? Wenn nein: **vor produktivem Einsatz** Plugin `berufsrecht-ki-vertragspruefung` durchlaufen.

### 9. Standard-Output-Sprache

Deutsch (Default) oder Englisch (bei internationalen Mandanten).

## Speicherort

Profil schreiben nach:

```
~/.claude/plugins/config/claude-fuer-deutsches-recht/patentrecherche/CLAUDE.md
```

Format:

```markdown
### patentrecherche — Kanzleiprofil

- Kanzlei: ...
- Patentanwält:innen: ...
- Technikgebiete: ...
- Schwerpunktklassen CPC/IPC: ...
- Datenbankzugänge: ...
- Mandantenstruktur: ...
- Typische Recherchezwecke: ...
- Rechtsraum-Schwerpunkt: ...
- Berufsrechtliche Vorprüfung KI-Dienstleister: ja/nein/in Arbeit
- Output-Sprache: ...
- Profil erstellt am: TT.MM.JJJJ
```

## Disclaimer ans Ende des Interviews

> **Hinweis zur Recherche.** Diese Recherche ist eine KI-gestützte Vorrecherche und keine amtliche Recherche im Sinne einer DPMA-/EPA-Recherche. Die finale Bewertung von Neuheit, erfinderischer Tätigkeit und Schutzrechtsstand muss durch eigene Nachrecherche oder durch Überprüfung der Recherche abgesichert werden. Treffer können unvollständig sein, falsch klassifiziert sein, durch Patentfamilien-Verbindungen verfehlt werden und in nicht maschinenlesbaren Sprachen verborgen sein.

## Weiterleitung

Nach dem Interview: Vorschlag, welches Skill als Nächstes laufen sollte — typischerweise `klassifikation-cpc-ipc`, gefolgt von `agentische-datenbank-recherche` und dem zweckspezifischen Skill (Stand der Technik / Neuheit / Erfinderische Tätigkeit / FTO).

## Triage-Fragen zu Beginn des Kaltstart-Interviews

Bevor das Interview begonnen wird, klaere:
1. Welchen Recherchezweck verfolgt der Mandant — Neuheitspruefung, FTO, Stand der Technik, Wettbewerber-Monitoring?
2. Ist die technische Beschreibung oder der Erfindungsgegenstand hinreichend konkret (Patent, Produktbeschreibung, Skizze)?
3. Welche Zielmärkte/Validierungsstaaten sind zu beruecksichtigen?
4. Stehen Fachleute für Rueckfragen zur Verfuegung, wenn technische Unklarheiten auftreten?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **DPMA, Richtlinien für die Pruefung 2023 (Teil 5 — Rechercheberichte):** Amtliche Rechercheberichte des DPMA umfassen in der Regel eine Suche nach allen in Klassen eingetragenen Patentdokumenten des relevanten Technikgebiets; agentische private Vorrecherchen koennen die amtliche Recherche nicht ersetzen, aber als qualifizierte Vorbereitung dienen.
