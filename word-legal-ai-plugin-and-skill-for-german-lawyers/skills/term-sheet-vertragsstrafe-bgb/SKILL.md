---
name: term-sheet-vertragsstrafe-bgb
description: "Term Sheet Vertragsstrafe BGB: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Term Sheet Vertragsstrafe BGB

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Term Sheet Vertragsstrafe BGB** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `term-sheet-zu-vertrag-uebersetzung` | Uebersetzung eines Term Sheets oder Letter of Intent in einen ausgearbeiteten Vertrag. Identifiziert die typischen Term-Sheet-Punkte (Parteien Praeambel Leistung Verguetung Laufzeit Kuendigung Gewaehrleistung Haftung Geheimhaltung Recht Gericht Schiedsklausel Schriftform Salvatorisch), mappt jeden Punkt auf einen Vertragsabschnitt, fuegt notwendige Boilerplate-Klauseln hinzu, schliesst typische Term-Sheet-Luecken (Definitionen Verzug Force Majeure Datenschutz IP Aenderungen) und liefert einen vollstaendigen Vertragsentwurf inklusive Mandantenmemo zu offenen Punkten. |
| `vertragsstrafe-339-bgb` | Drafting und Prüfung von Vertragsstrafeklauseln nach §§ 339-345 BGB. Klärt Bestimmtheit der zu sichernden Hauptverbindlichkeit, Verschuldenserfordernis, Höhe und Verhältnismäßigkeit, Verhältnis zum Schadensersatz (§ 340 BGB Erfüllung statt vs. § 341 BGB neben Erfüllung), richterliche Herabsetzung nach § 343 BGB und deren Ausschluss bei Vollkaufleuten gem. § 348 HGB sowie die AGB-rechtlichen Grenzen nach § 309 Nr. 6 BGB. Liefert Mustertext mit Strafhöhe, Verfallsregelung und Anrechnungsregel. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Term Sheet Vertragsstrafe BGB**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `term-sheet-zu-vertrag-uebersetzung`

**Fokus:** Uebersetzung eines Term Sheets oder Letter of Intent in einen ausgearbeiteten Vertrag. Identifiziert die typischen Term-Sheet-Punkte (Parteien Praeambel Leistung Verguetung Laufzeit Kuendigung Gewaehrleistung Haftung Geheimhaltung Recht Gericht Schiedsklausel Schriftform Salvatorisch), mappt jeden Punkt auf einen Vertragsabschnitt, fuegt notwendige Boilerplate-Klauseln hinzu, schliesst typische Term-Sheet-Luecken (Definitionen Verzug Force Majeure Datenschutz IP Aenderungen) und liefert einen vollstaendigen Vertragsentwurf inklusive Mandantenmemo zu offenen Punkten.

# Term Sheet zu Vertrag

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
10. **Mitteilung und Zustellung** — Adresse fuer rechtlich relevante Mitteilungen.
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
- **Mapping-Tabelle** als Anhang fuer interne Doku.
- **Mandantenmemo** zu offenen Punkten.
- **Markup-Modus aus**, da Erstentwurf.

## Beispiel: Term-Sheet-Punkt vs. Vertragsklausel

### Term-Sheet-Punkt

> 4. **Verguetung:** EUR 500.000 zahlbar in drei Tranchen: 30 Prozent bei Signing, 40 Prozent bei Milestone 1, 30 Prozent bei Abnahme.

### Vertragsklausel (ausgearbeitet)

> ### § 4 Verguetung
>
> (1) Die Verguetung fuer die Erbringung der in § 2 beschriebenen Leistungen betraegt insgesamt EUR 500.000 zuzueglich der jeweils gesetzlichen Umsatzsteuer.
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
- `definitionen-klauseln-stringent` fuer den Definitionsapparat
- `boilerplate-klauseln-katalog` fuer Schlussbestimmungen
- `klausel-bibliothek-katalog` fuer fertige Klauselbausteine
- `defensive-drafting-fallen-erkennen` fuer Review der Gegenfassung

## Quellen (Stand 05/2026)

- § 311 BGB (vorvertragliches Schuldverhaeltnis); § 286, § 288 BGB (Verzug); § 377 HGB (Untersuchungs- und Ruegepflicht); § 399 BGB (Abtretungsverbot); § 309 BGB (AGB-Klauselverbote); Art. 28 DSGVO (Auftragsverarbeitung).
- Zitierweise: `references/zitierweise.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `vertragsstrafe-339-bgb`

**Fokus:** Drafting und Prüfung von Vertragsstrafeklauseln nach §§ 339-345 BGB. Klärt Bestimmtheit der zu sichernden Hauptverbindlichkeit, Verschuldenserfordernis, Höhe und Verhältnismäßigkeit, Verhältnis zum Schadensersatz (§ 340 BGB Erfüllung statt vs. § 341 BGB neben Erfüllung), richterliche Herabsetzung nach § 343 BGB und deren Ausschluss bei Vollkaufleuten gem. § 348 HGB sowie die AGB-rechtlichen Grenzen nach § 309 Nr. 6 BGB. Liefert Mustertext mit Strafhöhe, Verfallsregelung und Anrechnungsregel.

# Vertragsstrafe nach §§ 339-345 BGB

## Zweck

Dieser Skill unterstützt Sie beim Drafting und bei der Prüfung von Vertragsstrafeklauseln. Eine Vertragsstrafe sichert eine Hauptverbindlichkeit ab, schafft einen pauschalierten Druck zur Erfüllung und kann zugleich den Schaden des Gläubigers vereinfacht liquidieren. Fehler im Drafting führen typischerweise zur Unbestimmtheit, zur Unwirksamkeit in AGB oder zur richterlichen Herabsetzung.

## Eingaben

- Art der gesicherten Hauptverbindlichkeit (Tun, Unterlassen, Geheimhaltung, Wettbewerbsverbot, Lieferfrist usw.).
- Vertragsverhältnis (B2B, B2C, Arbeitsverhältnis, AGB oder Individualabrede).
- Kaufmannseigenschaft der Parteien (für § 348 HGB relevant).
- Ziel der Klausel: Druck zur Erfüllung, Schadenspauschalierung oder beides.
- Sanktionierungsobjekt: jede Zuwiderhandlung, Dauerverletzung, Tagesstrafe?

## Rechtlicher und methodischer Rahmen

- **Anspruchsgrundlage:** § 339 BGB.
- **Verfall:** Bei Tun oder Geben nur durch Verzug (§ 339 S. 1 BGB), bei Unterlassen durch Zuwiderhandlung (§ 339 S. 2 BGB).
- **Verschulden:** Streitig. Herrschende Meinung verlangt Vertretenmüssen (§ 286 IV BGB analog für Verzug, § 276 BGB allgemein). Klausel darf das Verschuldenserfordernis vertraglich modifizieren, in AGB jedoch nur eng (§ 309 Nr. 7 b BGB beachten, wenn an Pflichtverletzung anknüpfend).
- **Verhältnis zum Schadensersatz:** § 340 BGB (Strafe statt der Erfüllung; weitergehender Schaden bleibt), § 341 BGB (Strafe neben der Erfüllung; auf Schadensersatz anrechenbar). Welche Variante gilt, ergibt sich aus der Auslegung der Klausel.
- **Richterliche Herabsetzung:** § 343 BGB ermöglicht Herabsetzung einer unverhältnismäßig hohen Strafe; nicht bei beiderseitigem Handelsgeschäft mit Vollkaufmann gem. § 348 HGB, dort lediglich Korrektiv über § 242 BGB.
- **AGB-Recht:** § 309 Nr. 6 BGB verbietet Vertragsstrafen in AGB gegenüber Verbrauchern und nach § 310 I BGB mittelbar auch im B2B-Verkehr außer in den engen Ausnahmen (Lohn- und Dienstverhältnis mit Strafe zulasten Arbeitgeber, vereinzelte Konstellationen mit objektiver Verstärkung der Hauptpflicht).
- **Arbeitsrecht:** Bei Wettbewerbsverboten regelmäßig Strafversprechen üblich; gesonderte Wirksamkeitsanforderungen nach §§ 74 ff. HGB.

## Ablauf / Checkliste

1. Hauptverbindlichkeit identifizieren und exakt bezeichnen (kein Verweis auf "diesen Vertrag insgesamt").
2. Auslösenden Tatbestand definieren: einzelne Zuwiderhandlung, Dauerverletzung mit Tagesstrafe, fortgesetzte Handlung als Einheit (vgl. BGH-Linie zum Strafverfall).
3. Verschuldenserfordernis ausdrücklich regeln oder bewusst dem Gesetz folgen.
4. Höhe verhältnismäßig festsetzen; bei wiederholten Verstößen Kappungsgrenze erwägen (z. B. zehnfache Einzelstrafe).
5. § 340 oder § 341 BGB klarstellen (statt oder neben Erfüllung).
6. Anrechnungsregel zum Schadensersatz formulieren.
7. AGB-Check: § 309 Nr. 6 BGB und § 307 BGB; bei B2B Ausstrahlungswirkung beachten.
8. Bei Vollkaufleuten: § 348 HGB nutzen, Herabsetzungsausschluss klarstellen.
9. Form prüfen: Wettbewerbsverbote mit Vertragsstrafe häufig schriftformbedürftig (vgl. § 74 HGB).
10. Verjährung: regelmäßige Verjährung § 195 BGB, Beginn § 199 BGB.

## Typische Drafting-Fehler

- Hauptverbindlichkeit unbestimmt: Klausel ist nichtig.
- Strafhöhe ohne Bezug zum Schadenspotenzial: Risiko der Herabsetzung oder AGB-Unwirksamkeit wegen unangemessener Benachteiligung (§ 307 BGB).
- "Pro Verstoß"-Klausel ohne Definition des Verstoßes: bei Dauerverletzung uferlos.
- Fehlende Anrechnungsregel: doppelte Inanspruchnahme schwer durchsetzbar.
- Vertragsstrafe in Verbraucher-AGB: nach § 309 Nr. 6 BGB unwirksam, Klausel fällt ersatzlos weg.
- Kopplung an verschuldensunabhängigen Tatbestand in AGB: regelmäßig Unwirksamkeit nach § 307 BGB.
- Verzicht auf Vorbehalt nach § 341 III BGB (Vertragsstrafe muss bei Annahme der Erfüllung vorbehalten werden).

## Ausgabeformat

- Klauselentwurf in Urteilsstil mit nummerierten Absätzen.
- Begleitendes Memo: AGB-Risiko, Höhenkalibrierung, Bezug zu § 340/§ 341 BGB, Anrechnungsregel, Hinweis zur Herabsetzung.
- Kurze Risikoliste am Ende.

## Beispiel

Mustertext (Individualabrede, B2B, Unterlassungspflicht):

> § X Vertragsstrafe
> (1) Verletzt der Lizenznehmer die in § Y geregelte Unterlassungspflicht schuldhaft, hat er für jede Zuwiderhandlung eine Vertragsstrafe in Höhe von EUR 10.000 an den Lizenzgeber zu zahlen. Bei einer fortgesetzten Zuwiderhandlung gilt jeder angefangene Kalendertag der Zuwiderhandlung als gesonderter Verstoß, höchstens jedoch dreißig Tage pro einheitlichem Lebensvorgang.
> (2) Die Vertragsstrafe wird neben der Erfüllung verwirkt (§ 341 BGB). Ein über die Strafe hinausgehender Schaden bleibt unberührt; die verwirkte Vertragsstrafe ist auf einen Schadensersatzanspruch anzurechnen.
> (3) Der Lizenzgeber behält sich die Vertragsstrafe bei Annahme der weiteren Vertragserfüllung ausdrücklich vor (§ 341 III BGB).
> (4) Die Parteien sind sich einig, dass die Voraussetzungen eines beiderseitigen Handelsgeschäfts vorliegen; § 348 HGB findet Anwendung.

Hinweis: In AGB gegenüber Verbrauchern ist die Klausel nach § 309 Nr. 6 BGB unwirksam. Im AGB-B2B-Geschäft prüfen, ob § 307 BGB die Klausel über die Ausstrahlungswirkung der Klauselverbote indirekt erfasst; gegebenenfalls Höhe absenken und Kappung einziehen.

## Querverweise

- `geheimhaltung-nda-vertraulichkeit` – Vertragsstrafe in NDA-Konstellationen.
- `haftungsausschluss-und-haftungsbegrenzung` – Abgrenzung Strafe und Haftungsbegrenzung.
- `agb-konforme-klauseln-305-310-bgb` – § 309 Nr. 6 BGB und Ausstrahlungswirkung.
- `transparenzgebot-307-bgb` – Bestimmtheit der Hauptverbindlichkeit.

## Quellen (Stand 05/2026)

- §§ 339-345 BGB, § 286 IV BGB, §§ 276, 307, 309 Nr. 6 BGB.
- §§ 74 ff. HGB (Wettbewerbsverbote), § 348 HGB (Herabsetzungsausschluss).
- Methodische Grundlagen: `references/methodik-buergerliches-recht.md`.
- Zitierweise: `references/zitierweise.md`. Konkrete Rechtsprechung des BGH zur Vertragsstrafe (etwa zur "fortgesetzten Handlung" und zur Kappungsgrenze in AGB) ist vom Nutzer fundstellengenau zu verifizieren.
