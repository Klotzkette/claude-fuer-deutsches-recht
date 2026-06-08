---
name: term-sheet-vertragsstrafe-bgb
description: "Uebersetzung eines Term Sheets oder Letter of Intent in einen ausgearbeiteten Vertrag. Identifiziert die typischen Term-Sheet-Punkte (Parteien Praeambel Leistung Verguetung Laufzeit Kuendigung Gewaehrleistung Haftung Geheimhaltung Recht Gericht Schiedsklausel Schriftform Salvatorisch), mappt jeden Punkt auf einen Vertragsabschnitt, fuegt notwendige Boilerplate-Klauseln hinzu, schliesst typische Term-Sheet-Luecken (Definitionen Verzug Force Majeure Datenschutz IP Aenderungen) und liefert einen vollstaendigen Vertragsentwurf inklusive Mandantenmemo zu offenen Punkten im Word Legal Ai Plugin And Skill For German Lawyers: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Term Sheet zu Vertrag

## Arbeitsbereich

Uebersetzung eines Term Sheets oder Letter of Intent in einen ausgearbeiteten Vertrag. Identifiziert die typischen Term-Sheet-Punkte (Parteien Praeambel Leistung Verguetung Laufzeit Kuendigung Gewaehrleistung Haftung Geheimhaltung Recht Gericht Schiedsklausel Schriftform Salvatorisch), mappt jeden Punkt auf einen Vertragsabschnitt, fuegt notwendige Boilerplate-Klauseln hinzu, schliesst typische Term-Sheet-Luecken (Definitionen Verzug Force Majeure Datenschutz IP Aenderungen) und liefert einen vollstaendigen Vertragsentwurf inklusive Mandantenmemo zu offenen Punkten. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Ein Term Sheet (Letter of Intent, Eckdatenpapier, Heads of Terms) ist die wirtschaftliche Einigung in zwei bis fuenf Seiten. Der ausgearbeitete Vertrag ist 20 bis 80 Seiten. Dazwischen liegt eine Uebersetzungsaufgabe: Welche Punkte sind im Term Sheet schon geklaert? Welche fehlen? Welche Boilerplate-Klauseln muessen ergaenzt werden? Welche Verhandlungspunkte sind noch offen?

Dieser Skill fuehrt strukturiert durch diese Uebersetzung. Er hilft, Luecken systematisch zu schliessen, ohne wirtschaftliche Punkte zu ueberschreiben, die nicht im Term Sheet stehen.

## Eingaben

- Term Sheet, Letter of Intent oder Heads of Terms (Word, PDF oder Klartext)
- Vertragstyp (Liefervertrag, Dienstvertrag, Werkvertrag, M&A SPA, Lizenzvertrag, Kooperationsvertrag)
- Parteienrolle (welche Seite vertreten Sie?)
- Vorhandene Standardvertraege oder Templates der Kanzlei
- Zeitschiene (Signing-Frist)

## Rechtlicher und methodischer Rahmen

- Term Sheets sind regelmaessig **rechtlich unverbindlich** (außer ausdruecklich vereinbart). Bindend sind ueblicherweise nur Vertraulichkeit, Exklusivitaet und Kostentragung (Break-up Fees).
- "Subject to Contract"-Klauseln klaeren die Unverbindlichkeit. Bei Fehlen kann sich aus dem Verhalten der Parteien eine vertragliche Bindung ergeben (vgl. § 311 BGB).
- Vertragslueckenfuellung: Was im Term Sheet fehlt, gilt nicht automatisch als nicht-vereinbart. Der ausgearbeitete Vertrag kann ergaenzen, solange er den wirtschaftlichen Kern nicht ueberschreibt.
- Sorgfalt: § 43a BRAO. Mandant muss klar erkennen, was aus dem Term Sheet uebernommen wurde und was neu ist.

## Mapping Term-Sheet-Punkt zu Vertragsabschnitt

| Term-Sheet-Punkt | Vertragsabschnitt | Boilerplate-Skill |
|---|---|---|
| Parteien | Rubrum, Eingangsformel | `dokumentarchitektur-vertrag-und-schriftsatz` |
| Praeambel/Hintergrund | Praeambel | - |
| Definitionen (selten im Term Sheet) | § Definitionen | `definitionen-klauseln-stringent` |
| Leistungsgegenstand | § Leistung | `anspruchsgrundlage-und-rechtsfolgen-klauseln` |
| Verguetung/Preis | § Verguetung | - |
| Zahlungsbedingungen | § Zahlung, Verzug | - |
| Laufzeit | § Laufzeit | - |
| Kuendigung | § Kuendigung | `kuendigungsklauseln-und-vertragsbeendigung` |
| Gewaehrleistung/Garantien | § Gewaehrleistung | - |
| Haftung | § Haftung | `haftungsausschluss-und-haftungsbegrenzung` |
| Geheimhaltung/NDA | § Vertraulichkeit | `geheimhaltung-nda-vertraulichkeit` |
| Recht/Gericht | § Schlussbestimmungen | `boilerplate-klauseln-katalog` |
| Force Majeure (fehlt oft) | § Hoehere Gewalt | `force-majeure-und-erschwerung-313-bgb` |
| Vertragsstrafe (fehlt oft) | § Vertragsstrafe | `vertragsstrafe-339-bgb` |
| Aenderungen | § Aenderungen, Schriftform | `boilerplate-klauseln-katalog` |
| Salvatorische Klausel | § Schlussbestimmungen | `boilerplate-klauseln-katalog` |
| IP-Rechte (oft fehlend) | § Schutzrechte | `ip-rechteuebertragung-und-lizenzen` |
| Datenschutz (immer noetig) | § Datenschutz, AVV | externes Plugin datenschutzrecht |
| Mitarbeiter-Abwerbeklausel | § Sonstiges | - |

## Typische Term-Sheet-Luecken

Diese Punkte fehlen in fast jedem Term Sheet und muessen aktiv ergaenzt werden:

1. **Definitionen-Apparat** — Im Term Sheet werden Begriffe oft synonym verwendet; im Vertrag braucht es einen Definitionskatalog.
2. **Verzug und Mahnung** — Wann tritt Verzug ein, wann braucht es Mahnung, wann ist sie entbehrlich (§ 286 BGB).
3. **Maengelanzeige und Untersuchungsobliegenheit** — § 377 HGB im B2B-Kaufvertrag.
4. **Force Majeure** — Naturkatastrophen, Pandemie, Krieg, Cyber-Angriff.
5. **Datenschutz und AVV** — Sobald personenbezogene Daten verarbeitet werden, ist Art. 28 DSGVO Pflicht.
6. **Aenderungen des Vertrags** — Schriftformklausel mit Ausnahme der Schriftformklausel selbst.
7. **Salvatorische Klausel** — Was passiert bei Teilnichtigkeit.
8. **Abtretungsverbot oder Zustimmungsvorbehalt** — § 399 BGB.
9. **Aufrechnungsverbot oder -beschraenkung** — Wirksamkeitsgrenzen § 309 Nr. 3 BGB.
10. **Mitteilung und Zustellung** — Adresse für rechtlich relevante Mitteilungen.
11. **Geheimhaltung nach Vertragsende** — Nachlaufzeit drei bis fuenf Jahre.
12. **Sprachklausel** — Welche Sprachfassung ist verbindlich.

## Ablauf / Checkliste

1. **Term Sheet lesen, Punkte nummerieren.** Aktivieren Sie Track Changes parallel.
2. **Mapping-Tabelle ausfuellen.** Welche Term-Sheet-Punkte gehen in welchen Vertragsabschnitt?
3. **Luecken-Tabelle erstellen.** Pruefen Sie die zwoelf typischen Term-Sheet-Luecken oben.
4. **Vertragsskelett aufbauen.** Skill `dokumentarchitektur-vertrag-und-schriftsatz`.
5. **Definitionen extrahieren.** Skill `definitionen-klauseln-stringent`. Term-Sheet-Begriffe in Definitionen ueberfuehren.
6. **Term-Sheet-Punkte einarbeiten.** Wirtschaftliche Punkte nicht aendern, nur dogmatisch sauber formulieren.
7. **Boilerplate ergaenzen.** Skill `boilerplate-klauseln-katalog`.
8. **Risikoklauseln pruefen.** Haftung, Gewaehrleistung, Vertragsstrafe, AGB-Konformitaet.
9. **Mandantenmemo zu offenen Punkten.** Liste der Luecken, die im Term Sheet nicht geklaert waren, mit Vorschlag und Risikohinweis.
10. **Senden an Mandant zur Freigabe.** Erst dann an die Gegenseite.

## Mandantenmemo (Beispielstruktur)

> Sehr geehrte Frau Mandantin,
>
> beigefuegt erhalten Sie den ausgearbeiteten Vertragsentwurf zum Term Sheet vom Datum. Wir haben folgende Punkte ergaenzt, die im Term Sheet nicht erwaehnt waren:
>
> 1. **Definitionsapparat** — sieben definierte Begriffe (...).
> 2. **Verzug** — Frist von 14 Tagen ab Rechnungserhalt; Verzugszinsen nach § 288 BGB.
> 3. **Datenschutz** — Auftragsverarbeitungsvertrag als Anlage 3.
> 4. **Force Majeure** — Standardklausel mit Mitteilungspflicht.
> 5. (...)
>
> Folgende Punkte aus dem Term Sheet sind in der ausgearbeiteten Fassung nicht eindeutig geregelt und beduerfen Ihrer Entscheidung:
>
> 1. **Verguetungsanpassung** — Im Term Sheet ist "Anpassung jaehrlich" erwaehnt. Wir empfehlen Kopplung an den Verbraucherpreisindex; alternativ jaehrliche Verhandlung. Bitte entscheiden Sie.
> 2. **Haftungshoehe** — Term Sheet nennt keine Obergrenze. Wir empfehlen 5 Mio. EUR pro Schadensfall und 10 Mio. EUR im Vertragsjahr; alternativ Versicherungssumme.
> 3. (...)
>
> Bei Fragen stehen wir gerne zur Verfuegung.
>
> Mit freundlichen Gruessen

## Ausgabeformat

- **Ausgearbeiteter Vertragsentwurf** als .docx mit Formatvorlagen.
- **Mapping-Tabelle** als Anhang für interne Doku.
- **Mandantenmemo** zu offenen Punkten.
- **Markup-Modus aus**, da Erstentwurf.

## Beispiel: Term-Sheet-Punkt vs. Vertragsklausel

### Term-Sheet-Punkt

> 4. **Verguetung:** EUR 500.000 zahlbar in drei Tranchen: 30 Prozent bei Signing, 40 Prozent bei Milestone 1, 30 Prozent bei Abnahme.

### Vertragsklausel (ausgearbeitet)

> ### § 4 Verguetung
>
> (1) Die Verguetung für die Erbringung der in § 2 beschriebenen Leistungen betraegt insgesamt EUR 500.000 zuzueglich der jeweils gesetzlichen Umsatzsteuer.
>
> (2) Die Verguetung ist in drei Tranchen zu zahlen:
>
> a) 30 Prozent der Verguetung (EUR 150.000 zuzueglich Umsatzsteuer) werden mit Unterzeichnung dieses Vertrages durch beide Parteien faellig.
>
> b) 40 Prozent der Verguetung (EUR 200.000 zuzueglich Umsatzsteuer) werden mit Erreichen des Milestones gemaess Anlage 1, Ziffer 1, faellig. Das Erreichen des Milestones ist durch schriftliche Mitteilung der Auftragnehmerin an die Auftraggeberin festzustellen; die Auftraggeberin kann binnen 14 Tagen nach Zugang dieser Mitteilung schriftlich widersprechen.
>
> c) 30 Prozent der Verguetung (EUR 150.000 zuzueglich Umsatzsteuer) werden mit der Abnahme der Gesamtleistung gemaess § 6 faellig.
>
> (3) Die Verguetung ist binnen 30 Tagen nach Rechnungserhalt ohne Abzug zu zahlen. Bei Zahlungsverzug schuldet die Auftraggeberin Verzugszinsen in Hoehe von neun Prozentpunkten ueber dem Basiszinssatz (§ 288 Abs. 2 BGB) sowie eine Verzugspauschale von EUR 40 je Mahnung (§ 288 Abs. 5 BGB).
>
> (4) Aufrechnung und Zurueckbehaltungsrechte sind nur mit unbestrittenen oder rechtskraeftig festgestellten Gegenforderungen zulaessig.

Der ausgearbeitete Vertrag hat den Term-Sheet-Punkt nicht veraendert (EUR 500.000, drei Tranchen, Verteilung 30/40/30), aber alle Detailfragen geregelt (Umsatzsteuer, Milestone-Feststellung, Faelligkeit, Verzug, Aufrechnung).

## Querverweise

- `dokumentarchitektur-vertrag-und-schriftsatz` für das Vertragsskelett
- `definitionen-klauseln-stringent` für den Definitionsapparat
- `boilerplate-klauseln-katalog` für Schlussbestimmungen
- `klausel-bibliothek-katalog` für fertige Klauselbausteine
- `defensive-drafting-fallen-erkennen` für Review der Gegenfassung

## Quellen (Stand 05/2026)

- § 311 BGB (vorvertragliches Schuldverhaeltnis); § 286, § 288 BGB (Verzug); § 377 HGB (Untersuchungs- und Ruegepflicht); § 399 BGB (Abtretungsverbot); § 309 BGB (AGB-Klauselverbote); Art. 28 DSGVO (Auftragsverarbeitung).
- Zitierweise: `references/zitierweise.md`.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
