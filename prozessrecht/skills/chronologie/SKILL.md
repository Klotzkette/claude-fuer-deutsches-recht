---
name: chronologie
description: "Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabellarische Sachverhaltschronologie. Abgrenzung: nicht vollständige Klageschrift im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Sachverhalts-Chronologie

## Arbeitsbereich

Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabellarische Sachverhaltschronologie. Abgrenzung: nicht vollständige Klageschrift. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Erstellung

1. **Modus:** Arbeitschronologie (intern, vollständig), Schriftsatz-Chronologie (aufbereitet) oder Zeugenchronologie (gefültert)?
2. **Dokumentenbasis:** Liegen die Quellen vor (Verträge, E-Mails, Schriftsätze, Anlagen)?
3. **Zeitraum:** Welcher Zeitraum ist mandatsrelevant — gibt es einen frühesten relevanten Stichtag?
4. **Lücken:** Gibt es bekannte Zeiträume, für die keine Dokumente vorliegen?
5. **Prozessuale Funktion:** Für Sachverhaltsdarstellung (§ 253 ZPO), Zeugenvernehmung (§§ 373 ff. ZPO) oder Berufungsbegründung (§ 520 Abs. 3 ZPO)?

## Zentrale Normen
- § 253 Abs. 2 Nr. 1 ZPO (Anforderungen an die Klageschrift — vollständiger Sachvortrag)
- § 138 ZPO (Erklärungspflicht der Parteien — Vollständigkeit und Wahrheitspflicht)
- § 373 ff. ZPO (Zeugenbeweis — Grundlage der Zeugenchronologie)
- § 520 Abs. 3 ZPO (Berufungsbegründung — tatsächliche Angaben)
- § 286 ZPO (Freie Beweiswuerdigung — Chronologie als Hilfsmittel)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Aufbau einer mandatsbezogenen Sachverhalts-Chronologie aus vorliegenden Dokumenten, Schriftsätzen, Verträgen, E-Mails und Anlagen. Die Chronologie dient als Grundlage für Sachverhaltsdarstellungen im Schriftsatz (§ 253 Abs. 2 Nr. 1 ZPO), Zeugenvernehmungsvorbereitung (§§ 373 ff. ZPO), Berufungsbegründung (§ 520 Abs. 3 ZPO) und interne Mandatsbriefings.

Drei Modi:
- **Arbeitschronologie** – intern, vollständig, mit Lückenmarkierungen
- **Sachverhaltsdarstellungs-Chronologie** – aufbereitet für den Schriftsatz, urteilsstilgerecht
- **Zeugenchronologie** – gefiltert auf einen bestimmten Zeugen für Vernehmungsvorbereitung

## Eingaben

- Aktives Mandat (Slug)
- Hochgeladene Dokumente: Verträge, Korrespondenz, E-Mails, Protokolle, Rechnungen, Sachverständigengutachten, Gerichtsentscheidungen
- Wahl des Modus: `--arbeits` | `--sachverhalt` | `--zeuge=[Name]`
- Optional: bekannte Schlüsseldaten (z. B. Vertragsschluss, Fälligkeitsdatum, Kündigungserklärung)

## Ablauf

1. **Dokumente parsen:** Alle hochgeladenen Dateien auf datierte Ereignisse scannen. Datum, Uhrzeit (soweit angegeben), Ereignisbeschreibung, Quelle (Dokumentenbezeichnung, Anlage-Nr.) und beteiligte Personen extrahieren.

2. **Deduplizierung:** Gleiche Ereignisse aus verschiedenen Quellen zusammenführen; Widersprüche markieren als `[WIDERSPRUCH: Quelle A gibt X an, Quelle B gibt Y an]`.

3. **Mandatstheorien-Tagging:** Jedes Ereignis nach Relevanz für die Mandatstheorie markieren:
 - 🔑 Kernereig­nis (unmittelbar anspruchsbegründend oder -ausschließend)
 - ⚠️ Risikopunkt (könnte gegen Mandantin sprechen)
 - 📎 Hintergrundinformation
 - ❓ Ungeklärt / Beleg fehlt

4. **Lücken identifizieren:** Zeiträume ohne belegte Ereignisse und inhaltliche Lücken (z. B. fehlende Zugangsbestätigung, unklare Übergabe) als `[LÜCKE: Zeitraum MM/JJJJ bis MM/JJJJ – kein Beleg]` markieren.

5. **Modus anwenden:**
 - *Arbeitschronologie:* Vollständige Liste mit Quellenangaben und Anmerkungen.
 - *Sachverhaltsdarstellung:* Fließtext im Urteilsstil, Ereignisse in der dritten Person, Beweisquellen als Fußnoten.
 - *Zeugenchronologie:* Nur Ereignisse mit Beteiligung des Zeugen; Ergänzung um mögliche Wissenslücken des Zeugen.

6. **Versionierung:** Neue Chronologien als `chronology-v[N].md` im Mandatsordner speichern.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

### Arbeitschronologie (Tabelle)

| Datum | Ereignis | Quelle / Anlage | Beteiligte | Tag | Anmerkung |
|---|---|---|---|---|---|
| 12.03.2022 | Abschluss Werkvertrag | Anlage K1 (Vertrag v. 12.03.2022) | Kl., Bekl. | 🔑 | Unterschriften vorhanden |
| 15.04.2022 | Fristsetzung Mängelbeseitigung (Schreiben Kl.) | Anlage K3 | Kl. → Bekl. | 🔑 | Zugang streitig |
| [LÜCKE] | Zeitraum 16.04. – 30.05.2022 | – | – | ❓ | Keine Korrespondenz vorhanden |

### Sachverhaltsdarstellung (Fließtext-Modus)

> Am 12. März 2022 schlossen die Parteien einen Werkvertrag über die Erstellung einer Software (Anlage K1). Mit Schreiben vom 15. April 2022, dem Beklagten zugegangen am 17. April 2022 (Anlage K2: Rückschein), setzte die Klägerin eine Nachfrist zur Mängelbeseitigung bis zum 1. Mai 2022.
>
> *Beweis für Zugang: Zeugnis des Herrn Anton Mayer, [Anschrift]; Anlage K2 (Zustellungsnachweis).*

## Risiken / typische Fehler

- **Unklarer Zugangszeitpunkt:** Zugangsnachweis für Mahnungen und Fristsetzungen ist entscheidend für Verzugsbeginn (§ 286 Abs. 1 BGB); fehlende Belege zwingend als Lücke markieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Veraltete Chronologie:** Nach jedem Mandat-Update (`/mandat-update`) die Chronologie ergänzen; veraltete Versionen archivieren.
- **Zeugenchronologie zu weit gefasst:** Nur mandatsrelevante Ereignisse einbeziehen; nicht alle Ereignisse, an denen der Zeuge beteiligt war.
- **Datenschutz:** Personenbezogene Daten Dritter nur soweit erforderlich; DSGVO-Minimierungsgrundsatz (Art. 5 Abs. 1 lit. c DSGVO) beachten.
