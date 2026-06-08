---
name: intake-kanalcheck-masseverbindlichkeit
description: "Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. § 174 InsO Forderungsanmeldung, § 177 InsO Nachtragsanmeldung. Prüfraster Kanal-Identifikation, Metadaten-Erfassung, Eingangs-Zeitstempel, Dubletten-Vorabcheck, Prioritaet bei Fristnaehe. Output strukturiertes Eingangsbuch mit Kanal, Datum, Gläubiger und Status. Abgrenzung zu Aktenanlage-Batchregister für Massenerfassung und zu Formalprüfung im Insolvenzforderungsanmeldungspruefung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Intake und Kanalcheck

## Arbeitsbereich

Eingehende Forderungsanmeldungen kanalübergreifend erfassen: Anwendungsfall Insolvenzverwalter-Büro erhält Anmeldungen per Post E-Mail Portal Tabellenexport oder Nachtrag und muss einheitliches Eingangsbuch führen. § 174 InsO Forderungsanmeldung, § 177 InsO Nachtragsanmeldung. Prüfraster Kanal-Identifikation, Metadaten-Erfassung, Eingangs-Zeitstempel, Dubletten-Vorabcheck, Prioritaet bei Fristnaehe. Output strukturiertes Eingangsbuch mit Kanal, Datum, Gläubiger und Status. Abgrenzung zu Aktenanlage-Batchregister für Massenerfassung und zu Formalprüfung. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Intake und Kanalcheck` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe

Erfasst eingehende Forderungsanmeldungen kanalneutral und bildet ein belastbares Eingangsbuch.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Posteingang liegt vor
- Portalexport oder CSV liegt vor
- Gläubiger sendet Nachtrag
- mehrere Kanäle enthalten dieselbe Forderung

## Workflow

1. Eingangskanal, Eingangsdatum, Dateiname, Absender, Vertreter und Gläubiger-ID erfassen.
2. Anmeldung von Begleitschreiben, Anlagen, Rechnungspaketen, Titeln und Zahlungsnachweisen trennen.
3. Fristlage prüfen: rechtzeitig, verspätet, geändert oder offensichtlich nur Ergänzung.
4. Dublettenindizien markieren: gleicher Gläubiger, gleiche Rechnung, gleicher Betrag, gleicher Zeitraum, gleicher Titel.
5. Eingangsbuch und Prüfnummer vergeben, ohne materiell zu entscheiden.

## Ausgabe

- Intake-Register
- Dublettenhinweise
- fehlende Mindestdaten
- Zuordnung zu bestehender Prüfnummer

## Qualitätsgates

- Nachträge werden an die ursprüngliche Anmeldung geklebt.
- E-Mail-Text und Anlagen werden getrennt ausgewertet.
- Unlesbare Dateien werden nicht stillschweigend ignoriert.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend für Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
