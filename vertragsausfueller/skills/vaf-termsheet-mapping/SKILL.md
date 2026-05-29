---
name: vaf-termsheet-mapping
description: "Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten muessen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent, Klausel-Bibliothek Vertragsmodule. Prüfraster Term Sheet vollständig Parteien Objekt Preis Laufzeit, Widersprüche Vorlage vs. Term Sheet, Bindungswirkung Letter of Intent, steuerliche Punkte erklärt. Output Mapping-Tabelle Term Sheet zu Vertragsfeld mit Lueckenliste und Widerspruchs-Ampel. Abgrenzung zu Template-Erkennung und zu Feldinventar."
---

# Term-Sheet-Mapping

## Triage zu Beginn

1. Liegt das Term Sheet vollständig vor — alle Eckdaten (Parteien, Objekt, Preis, Laufzeit, Optionen)?
2. Gibt es Widersprüche zwischen Term Sheet und Vorlage — welche Seite hat Vorrang?
3. Sind im Term Sheet steuerliche Punkte geregelt (USt, Grunderwerbsteuer)?
4. Hat das Term Sheet Bindungswirkung oder ist es unverbindlich (Letter of Intent)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 311 Abs. 2 BGB — vorvertragliche Pflichten (culpa in contrahendo)
- § 150 BGB — modifizierte Annahme (Term-Sheet-Abweichungen vom Angebot)
- §§ 133, 157 BGB — Auslegung (Term Sheet als Auslegungshilfe)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill überführt wirtschaftliche Eckdaten in Vertragsklauseln. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Parteien, Objekt, Preis, Laufzeit, Optionen, Kaution, Nebenpflichten, Versicherung und Sonderbedingungen auslesen.
2. Jeden Term-Sheet-Punkt einem Feld, einer Klausel oder einer Anlage zuordnen.
3. Punkte ohne Vertragsklausel als Ergänzungsbedarf markieren.
4. Konflikte wie abweichende Laufzeit, Miete, Umsatzsteuer oder Rückbaupflicht sichtbar machen.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

---

<!-- AUDIT 27.05.2026
Bundle: bundle_047.json
-->
