---
name: vaf-plausibilitaetscheck-termsheet
description: "Vaf Plausibilitaetscheck, Vaf Termsheet Mapping, Altvertraege Dokumentenmatrix Und Lueckenliste: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Vaf Plausibilitaetscheck, Vaf Termsheet Mapping, Altvertraege Dokumentenmatrix Und Lueckenliste

## Arbeitsbereich

Dieser Skill bündelt **Vaf Plausibilitaetscheck, Vaf Termsheet Mapping, Altvertraege Dokumentenmatrix Und Lueckenliste** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `vaf-plausibilitaetscheck` | Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden. §§ 305 ff. BGB Klausel-Konsistenz, § 550 BGB Schriftformhürde. Prüfraster Betraege Netto/Brutto konsistent, Fristen rechtlich zulässig, Anlagenverzeichnis vollständig, Parteidaten aktuell, Umsatzsteuer-Option konsistent. Output Plausibilitätsprotokoll mit Fehlerampel und Korrekturbedarf. Abgrenzung zu Quality-Gate für Gesamtprüfung und zu Clean-Output. |
| `vaf-termsheet-mapping` | Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten muessen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent, Klausel-Bibliothek Vertragsmodule. Prüfraster Term Sheet vollständig Parteien Objekt Preis Laufzeit, Widersprüche Vorlage vs. Term Sheet, Bindungswirkung Letter of Intent, steuerliche Punkte erklärt. Output Mapping-Tabelle Term Sheet zu Vertragsfeld mit Lueckenliste und Widerspruchs-Ampel. Abgrenzung zu Template-Erkennung und zu Feldinventar. |
| `spezial-altvertraege-dokumentenmatrix-und-lueckenliste` | Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Für **Vaf Plausibilitaetscheck, Vaf Termsheet Mapping, Altvertraege Dokumentenmatrix Und Lueckenliste** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `vertragsausfueller` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `vaf-plausibilitaetscheck`

**Fokus:** Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden. §§ 305 ff. BGB Klausel-Konsistenz, § 550 BGB Schriftformhürde. Prüfraster Betraege Netto/Brutto konsistent, Fristen rechtlich zulässig, Anlagenverzeichnis vollständig, Parteidaten aktuell, Umsatzsteuer-Option konsistent. Output Plausibilitätsprotokoll mit Fehlerampel und Korrekturbedarf. Abgrenzung zu Quality-Gate für Gesamtprüfung und zu Clean-Output.

# Plausibilitätscheck

## Triage zu Beginn

1. Sind alle Geldbeträge konsistent (Netto + Umsatzsteuer = Brutto; Gesamtmiete = Kaltmiete + Nebenkosten)?
2. Sind alle Fristen kalendergenau und rechtlich zulässig (z.B. keine unzulässig kurzen Widerrufsfristen)?
3. Stimmen Anlagenverzeichnis und Anlagenbezugnahmen im Text überein?
4. Sind Parteidaten vollständig und aktuell (Handelsregistereintrag, Vertreter)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 551 BGB — Höchstgrenze Kaution (3 Monatskaltmieten)
- § 556 BGB — Betriebskosten Abrechnung (Jahresfrist)
- § 288 BGB — Verzugszinsen (§ 288 Abs. 1: 5 Prozentpunkte B2C; § 288 Abs. 2: 9 Prozentpunkte B2B)
- § 269 BGB — Leistungsort (relevant für Fristberechnung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill härtet den Entwurf vor Versand oder Verhandlung. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Gesamtmiete gegen Kaltmiete und Nebenkosten rechnen.
2. Kaution gegen Monatsmieten, Mietbeginn gegen Laufzeitende und Optionsfristen prüfen.
3. Verweise auf Anlagen, Klauseln und Signaturblöcke kontrollieren.
4. Unplausibles als rote Rückfrage markieren, nicht still korrigieren.

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

## 2. `vaf-termsheet-mapping`

**Fokus:** Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten muessen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent, Klausel-Bibliothek Vertragsmodule. Prüfraster Term Sheet vollständig Parteien Objekt Preis Laufzeit, Widersprüche Vorlage vs. Term Sheet, Bindungswirkung Letter of Intent, steuerliche Punkte erklärt. Output Mapping-Tabelle Term Sheet zu Vertragsfeld mit Lueckenliste und Widerspruchs-Ampel. Abgrenzung zu Template-Erkennung und zu Feldinventar.

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

## 3. `spezial-altvertraege-dokumentenmatrix-und-lueckenliste`

**Fokus:** Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Altvertraege: Dokumentenmatrix, Lückenliste und Nachforderung / altvertraege dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX/PDF sind Dateiformate, keine Rechtsquellen. Je nach Vertrag BGB §§ 145 ff., 241, 280, 305 ff., 311; einschlägige Formvorschriften; bei Einreichung ZPO/beA-Vorgaben; bei Verbrauchern §§ 312 ff., 355 ff. BGB live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Altvertraege** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
