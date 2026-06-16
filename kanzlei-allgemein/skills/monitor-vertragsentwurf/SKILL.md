---
name: monitor-vertragsentwurf
description: "Scannt Akteninhalt auf Fristen Action-Items Wiedervorlagen und Zustellungen. Anwendungsfall Schriftsatz beA-Nachricht oder Urteil wurde hochgeladen und Fristen sollen automatisch erkannt werden. Normen § 222 ZPO §§ 187 188 BGB § 517 ZPO Berufungsfrist § 548 ZPO Revisionsfrist BRAO-Haftungsfristen..."
---

# Fristen- und Action-Monitor

## Arbeitsbereich

Scannt Akteninhalt auf Fristen Action-Items Wiedervorlagen und Zustellungen. Anwendungsfall Schriftsatz beA-Nachricht oder Urteil wurde hochgeladen und Fristen sollen automatisch erkannt werden. Normen § 222 ZPO §§ 187 188 BGB § 517 ZPO Berufungsfrist § 548 ZPO Revisionsfrist BRAO-Haftungsfristen. Prüfraster Fristart Rechtsgrundlage Fristbeginn Hauptfrist Vorfrist Verantwortlicher Wiedervorlage EB-Bedarf. Output Fristen- und Action-Register mit Vorfrist Übertragungsvermerk Eskalationshinweis. Abgrenzung zu fristenbuch-führen (zentrales Buchführen) und kanzlei-allgemein-fristen-monitor. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Geht es um eine akute Frist (heute/morgen) oder um eine Vorschau für die naechste Woche?
2. Handelt es sich um eine Notfrist (Berufung, Revision, Klage) oder eine einfache Wiedervorfrist?
3. Welche Verfahrensordnung gilt (ZPO, VwGO, StPO, SGG, FGO, FamFG) — für korrekte Fristberechnung?
4. Sind alle relevanten Akten-Eingaenge seit dem letzten Fristen-Scan erfasst?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 187-193 BGB — Fristberechnung: Allgemeine Regeln auch für prozessuale Fristen
- § 222 ZPO — Fristberechnung im Zivilprozess; Verweis auf BGB-Regeln
- § 517 ZPO — Berufungsfrist: ein Monat ab Urteilszustellung (Notfrist, unverlaengerbar)
- § 233 ZPO — Wiedereinsetzung in den vorigen Stand: Voraussetzungen und Antragsfrist

## Scanquellen

- Neue Eingänge aus Intake.
- Aktenordner.
- beA-Nachrichten.
- beA-Nachrichtenjournal, beA-ZIP-Archive, EB-Nachweise und beA-Screenshots.
- gerichtliche Verfügungen.
- Behördenbescheide.
- Mandantenmails und Messenger.
- interne Notizen.

## Ablauf

1. **Quelle erfassen**: Dokument, Eingangstag, Zustellart, Akte.
2. **Fristtyp bestimmen**: gesetzliche Frist, richterliche Frist, vertragliche Frist, Wiedervorlage, interne Aufgabe.
3. **Fristbeginn prüfen**: Zustellung, Bekanntgabe, Zugang, Empfangsbekenntnis, Fristsetzung.
4. **Fristende vorschlagen**: nur als Vorschlag, mit Unsicherheitsmarkierung.
5. **Vorfrist setzen**: Standard nach Kanzleiprofil.
6. **Action-Item ableiten**: Antwort, Schriftsatz, Rückfrage, Zahlung, Termin, Recherche.
7. **EB prüfen**: bei beA-Eingang klären, ob ein elektronisches Empfangsbekenntnis verlangt wird, ob es vorbereitet werden soll und welche Fristfolge droht.
8. **Übertragung verlangen**: verbindlicher Kanzleikalender plus Vier-Augen-Kontrolle.

## Ausgabe

`assets/templates/fristen-und-action-register.md` verwenden.

Jede Frist bekommt:

- Quelle.
- Berechnungsannahme.
- Unsicherheiten.
- Verantwortlichen.
- Übertragungsvermerk.
- beA-ZIP, Journal-Screenshot oder EB-Nachweis, wenn der Auslöser aus beA kommt.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Blockadevermeidung

Wenn Fristberechnung unsicher ist, nicht stehen bleiben:

1. konservativ früheste mögliche Frist markieren,
2. Rückfrage formulieren,
3. sofortige manuelle Prüfung verlangen.
