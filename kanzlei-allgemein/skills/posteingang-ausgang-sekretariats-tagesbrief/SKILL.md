---
name: posteingang-ausgang-sekretariats-tagesbrief
description: "Posteingang Ausgang Sekretariats Tagesbrief: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Posteingang Ausgang Sekretariats Tagesbrief

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Posteingang Ausgang Sekretariats Tagesbrief** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `posteingang-ausgang` | Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Postausgang erfasst Versandtag Empfaenger Inhalt Versandweg (Post beA EGVP E-Mail) Versandnummer Quittung. Beide Buecher mit Audit-Trail und Verbindung zur jeweiligen Mandatsakte. |
| `sekretariats-tagesbrief` | Erzeugt morgens den Tagesbrief der Kanzlei mit allen Informationen die Anwalt und Sekretariat für den Tag brauchen — Fristen heute und in der naechsten Woche Vorfristen aus dem Fristenbuch eingegangene Post vom Vortag offene Mandantenrückrufe Termine Gerichts- und Behoerdentermine Wiedervorlagen Geburtstage des Tages Honorarrückstaende über Schwelle. Strukturiert zur schnellen Sichtung in fuenf Minuten. Bricht Information so herunter dass Anwalt entscheiden kann was Prioritaet hat. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Posteingang Ausgang Sekretariats Tagesbrief**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `posteingang-ausgang`

**Fokus:** Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Postausgang erfasst Versandtag Empfaenger Inhalt Versandweg (Post beA EGVP E-Mail) Versandnummer Quittung. Beide Buecher mit Audit-Trail und Verbindung zur jeweiligen Mandatsakte.

# Posteingang und Postausgang


## Triage zu Beginn
1. Handelt es sich um einen Eingang (Fristbeginn pruefen) oder einen Ausgang (Versandnachweis sichern)?
2. Welcher Eingangsweg: Post (Vier-Tages-Fiktion), beA (sofortige Zustellung), E-Mail, Fax, persoenlich?
3. Gibt es ein fristwahrendes Dokument (Urteil, Klageschrift, Bescheid) mit sofortigem Fristen-Handlungsbedarf?
4. Muss der Eintrag per Audit-Trail unveraenderbar dokumentiert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 187-188 BGB i.V.m. § 222 ZPO — Fristbeginn bei Zustellung
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion fuer Postsendungen ab 01.01.2025
- § 173 ZPO — beA-Zustellungszeitpunkt: Eingang im Empfangspostfach
- § 51 BRAO — Haftung bei fehlerhafter oder fehlender Postbuchdokumentation

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Posteingang

### Erfassung pro eingegangenem Schriftstück

```yaml
- eingang-id: PE-2026-04223
 empfangsdatum: 2026-05-20
 eingangsweg: post # post / bea / egvp / e-mail / fax / persoenlich
 absender: Amtsgericht München
 art: urteil # urteil / beschluss / verfügung / mandantenbrief / behörden-bescheid / sonstiges
 mandat-az: 2026/0042
 betreff: Klage gg. ABC GmbH
 zustaendigkeit: RA Mueller
 fristfolge: berufungsfrist
 fristtermin: 2026-06-20
 aktion: an-fristenbuch
 ablage: mandate/2026-0042/02_bescheide/2026-05-20-urteil-ag-muenchen.pdf
```

### Pflichtschritte

1. **Eingangsdatum** zwingend erfassen — bei Postzustellung das tatsächliche Empfangsdatum (nicht das Postaufgabedatum).
2. **Zuordnung zur Akte** — wenn keine Akte vorhanden Neueinrichtung (Skill `mandantenakte-anlegen`).
3. **Fristerkennung** — bei Urteilen Beschlüssen Bescheiden sofort Frist ins Fristenbuch.
4. **Anwalt informieren** — Zuständigen anwaltlich benachrichtigen.

### Vier-Tages-Fiktionen (PostModG, seit 1.1.2025)

Bei Postzustellungen verschiedener Verfahrensordnungen gilt die Vier-Tages-Fiktion (§ 270 ZPO, § 122 Abs. 2 AO, § 41 Abs. 2 VwVfG, § 37 Abs. 2 SGB X, § 4 Abs. 2 VwZG — jeweils n.F. durch Postrechtsmodernisierungsgesetz, BGBl. 2024 I Nr. 236) für den Fristbeginn. Für Schriftstücke mit Aufgabe zur Post vor dem 1.1.2025 gilt weiterhin die alte Drei-Tages-Fiktion. Bei nachweislich früherem Zugang gilt der tatsächliche Zugang. Dokumentation des Eingangsdatums daher entscheidend.

## Postausgang

### Erfassung pro versendetem Schriftstück

```yaml
- ausgang-id: PA-2026-09817
 versanddatum: 2026-05-21
 versandweg: bea
 empfaenger: Amtsgericht München
 empfaenger-safe-id: 1234567890ABCDEF
 art: schriftsatz
 mandat-az: 2026/0042
 betreff: Berufung in Sachen Mueller gg. ABC GmbH
 unterzeichnet-von: RA Mueller
 versandnummer: V-2026-00123 # Verweis auf versand-vor-check
 quittung-pdf: mandate/2026-0042/03_schriftsaetze/2026-05-21-bea-quittung.pdf
 zugehoerige-frist: berufungsfrist 20.06.2026
 fristerledigung: ja
```

### Pflichtschritte

1. **Vor Versand** den Skill `versand-vor-check` durchlaufen.
2. **Versandnummer** aus dem Versand-Vor-Check übernehmen.
3. **Quittung** sichern (beA EGVP Einschreiben).
4. **Fristerledigung** im Fristenbuch markieren (Verweis zurück).
5. **Mandant informieren** über den Versand falls vereinbart.

## Vier-Augen-Prinzip

Bei Notfristen (Berufung Revision Kündigungsschutzklage): Posteingang Akte und Postausgang von zwei Personen gegenkontrolliert (Sekretariat + Anwalt).

## Audit-Trail

- Append-only Logbuch `posteingang.jsonl` und `postausgang.jsonl`.
- Änderungen nur durch Korrektureintrag (kein Überschreiben).
- Bei Korrektur: Begründung Datum und ausführende Person.

## Tagesbrief-Integration

- Posteingang des Vortags und der Nacht erscheint im `sekretariats-tagesbrief`.
- Offene Posteingangs-Posten (noch nicht der Akte zugeordnet) werden täglich gemeldet.

## Sichere Ablage

- Pro Mandat unter `mandate/<az>/02_eingaenge/<datum>-<absender>-<art>.pdf`.
- Postausgang unter `mandate/<az>/03_schriftsaetze/<datum>-<empfaenger>-<art>.pdf` plus Quittung.
- Verbindungen zu Fristenbuch und Honorar-Tracker.

## Datenschutz

- Posteingang und -ausgang enthalten Mandantengeheimnis-relevante Daten.
- Zugriff nur durch berechtigtes Kanzleipersonal.
- Externe Cloud-Speicherung nur mit AVV.

## Ausgabe

- Aktualisierte Logbücher.
- Tagesbrief-Einträge.
- Verbindungen zu Akte Fristenbuch und Honorar-Tracker.

## 2. `sekretariats-tagesbrief`

**Fokus:** Erzeugt morgens den Tagesbrief der Kanzlei mit allen Informationen die Anwalt und Sekretariat für den Tag brauchen — Fristen heute und in der naechsten Woche Vorfristen aus dem Fristenbuch eingegangene Post vom Vortag offene Mandantenrückrufe Termine Gerichts- und Behoerdentermine Wiedervorlagen Geburtstage des Tages Honorarrückstaende über Schwelle. Strukturiert zur schnellen Sichtung in fuenf Minuten. Bricht Information so herunter dass Anwalt entscheiden kann was Prioritaet hat.

# Sekretariats-Tagesbrief


## Triage zu Beginn
1. Fuer welchen Tag und welche Kanzlei wird der Tagesbrief erstellt?
2. Welche Fristen (heute, morgen, diese Woche) sind aus dem Fristenbuch zu uebernaehmen?
3. Gibt es besondere Eingaenge vom Vortag (Klageschriften, Urteile, Bescheide), die besondere Aufmerksamkeit erfordern?
4. Sind Geburtstage, Feiertage oder Abwesenheiten zu beachten, die die Tagesplanung beeinflussen?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 53 BRAO — Vertretungspflicht bei Verhinderung des Anwalts
- § 51 BRAO — Haftung fuer Organisationspflichtverletzungen im Sekretariat
- § 517 ZPO — Berufungsfrist (Notfrist): muss im Tagesbrief an erster Stelle erscheinen
- § 222 ZPO — Fristberechnung: korrekte Berechnung als Grundlage des Tagesbriefs

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Morgens den Tag strukturieren. Fünf Minuten Lesezeit; danach klare Prioritaeten.

## Aufbau

```
Tagesbrief Kanzlei XYZ
Datum: Donnerstag, 21. Mai 2026
Verfasst von: Sekretariat ...
Empfänger: alle Anwälte und Sekretariat

==========================================
1. NOTFRISTEN HEUTE
==========================================

Az 2025/0234 — Berufungsfrist heute 24:00 Uhr (Notfrist)
 Mandant Schmidt GmbH
 Berufung gegen Urteil LG München vom 21.04.2026 (Zustellung 21.04.2026)
 Status: Entwurf fertig — qeS-Signatur und beA-Versand bis spaetestens 17:00 Uhr
 Verantwortlich: RA Mueller

==========================================
2. VORFRISTEN IN DEN NAECHSTEN SIEBEN TAGEN
==========================================

Az 2026/0042 — Berufungsbegründungsfrist 28.05.2026 (Vorfrist heute)
Az 2026/0089 — Klagefrist 02.06.2026 (Vorfrist 26.05.2026)
Az 2026/0103 — Einspruchsfrist Sozialleistungsbescheid 30.05.2026

==========================================
3. POSTEINGANG VOM VORTAG
==========================================

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 zur Akte und Prüfung durch RA Mueller bis (Datum)

PE-2026-04221 — Mandant Schmidt — Rückfrage zur Berufung
 Antwort durch RA Mueller bis heute Mittag

PE-2026-04222 — Steuerberater des Mandanten Mueller GmbH
 Belege zur Außenprüfung Az 2026/0067
 zur Akte

==========================================
4. TERMINE HEUTE
==========================================

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
14:00 — Mandantengespraech Frau Schulz Az 2026/0091 (RA Mueller)
16:30 — Telefonkonferenz Gegenseite Kanzlei XYZ (Az 2026/0042)

==========================================
5. TERMINE NAECHSTE WOCHE
==========================================

23.05.2026 10:00 — SG München Az ... (RA Schulz)
27.05.2026 14:00 — Schlussbesprechung BP (RA Mueller; Steuerberater Wagner)
28.05.2026 11:00 — Notartermin Beurkundung GmbH (RA Schmidt)

==========================================
6. RUECKRUFE / WIEDERVORLAGEN
==========================================

Az 2026/0017 — Wiedervorlage seit drei Monaten ruhend — Klaerung mit RA Mueller
Mandant Schaefer Rückrufwunsch seit 19.05.2026

==========================================
7. HEUTE GEBURTSTAG
==========================================

Hans Mueller (Mueller GmbH) — Glückwunsch-Mail vorbereitet zur Freigabe
Dr. Schulz (Kollege) — Karte gestern verschickt

==========================================
8. HONORARRUECKSTAENDE UEBER 60 TAGEN
==========================================

Az 2026/0017 — Rechnung 2026/00098 vom 12.03.2026 über 3.200 EUR
 Letzte Mahnung 28.04.2026 — Stufe 2 erreicht — Entscheidung Klage durch RA Mueller

Az 2025/0188 — Rechnung 2025/00451 vom 14.11.2025 über 1.850 EUR
 Stufe 3 — Inkasso oder Klage

==========================================
9. NACHRICHTEN UND HINWEISE
==========================================

- beA-Stoerung gemeldet für 19.05.2026 von 08:00 bis 11:30 — eventuell relevant für Fristen
- Kammer-Rundschreiben zur Justizmodernisierung 2026 eingegangen — RA Mueller zur Information
```

## Erstellung

1. **Datenquellen** zusammenführen:
 - Fristenbuch (`fristenbuch-fuehren`)
 - Posteingang (`posteingang-ausgang`)
 - Termine (Kalendersystem)
 - Honorar-Tracker (`mahnwesen-honorar`)
 - Geburtstagsverteiler (`geburtstage-feiertage`)
 - Aktenbestand (`aktenbestand-pflege`)
2. **Filterung** auf relevant für heute und nächste sieben Tage.
3. **Erstellung** als Markdown plus PDF zur Verteilung.
4. **Versand** als interne E-Mail oder zentral im Kanzleisystem.

## Sicherheit

- Tagesbrief enthält Mandantenname und Mandatsdetails — Verteilung nur an Kanzleipersonal mit Mandatsgeheimnis-Pflicht.
- Keine externe Cloud-Speicherung ohne AVV.

## Ausgabe

- `tagesbrief-<datum>.md` und PDF.
- Einträge für Erinnerungen im Kalendersystem.
- Tagesbrief-Archiv unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/tagesbriefe/`.
