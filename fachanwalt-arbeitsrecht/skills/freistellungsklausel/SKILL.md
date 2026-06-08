---
name: freistellungsklausel
description: "Freistellungsklausel im Plugin Fachanwalt Arbeitsrecht: prüft konkrete Prüfungslinie für fachanwalt arbeitsrecht bag, Freistellungsklausel im Arbeitsvertrag, Abfindungsrechner modular. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Freistellungsklausel

## Arbeitsbereich

**Freistellungsklausel** ordnet den Fall über die tragenden Prüfungslinien: Prüfungslinie für fachanwalt arbeitsrecht bag, Freistellungsklausel im Arbeitsvertrag, Abfindungsrechner modular. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` | Prüfungslinie für fachanwalt arbeitsrecht bag freistellungsklausel unwirksam: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `spezial-freistellungsklausel-sonderfall-und-edge-case` | Freistellungsklausel im Arbeitsvertrag: BAG 5 AZR 108/25 (pauschale Klausel unwirksam), anlassbezogene Formulierung, Vergütungsfortzahlung, Urlaubsverfall während Freistellung, Verrechnung mit Urlaubsabgeltung, Edge Cases. |
| `ar-abfindungs-rechner-modular` | Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG. Beispielrechnung und Mustertext für Aufhebungsvertrag und Vergleich. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`

**Fokus:** Prüfungslinie für fachanwalt arbeitsrecht bag freistellungsklausel unwirksam: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

### Rechtsprechung live prüfen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsprechung live prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Kaltstart-Rückfragen

1. **Liegt eine schriftliche Kündigung vor?** — Datum und Zugangstag; Freistellung parallel oder erst danach erklärt?
2. **Welchen Wortlaut hat die Freistellungsklausel im Arbeitsvertrag?** — Pauschale Klausel ("nach Kündigung freigestellt") versus konkrete Begründung im Einzelfall.
3. **Hat der Arbeitgeber zusätzlich zum Klausel-Verweis einen konkreten Grund für die Freistellung genannt?** — Geheimhaltung, Konkurrenz, Vertrauensverlust, Betriebsfrieden — nur diese tragen.
4. **Will die Mandantin tatsächlich weiterarbeiten?** — Oder ist der Beschäftigungsanspruch nur Verhandlungsmasse für den Vergleich?
5. **Wie lange läuft die Kündigungsfrist noch?** — Kurze Restlaufzeit: Weiterbeschäftigungsantrag praktisch wenig wert; Verhandlungshebel im Vergleich umso stärker.
6. **Ist Annahmeverzug bereits eingetreten?** — Ab welchem Datum hat AG die tatsächliche Beschäftigung verweigert?
7. **Plant die Mandantin eine Wettbewerbs-Tätigkeit?** — Konkurrenzschutz-Vereinbarung im AV? Post-kontraktuelles Wettbewerbsverbot?
8. **Wurde ein Aufhebungsvertrag angeboten?** — Freistellungsklausel in Aufhebungsvertrag im Einzelfall konkret formulieren.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Kernaussage des Urteils

Leitentscheidung: BAG, Urteil vom 25.03.2026 - 5 AZR 108/25 (Wirksamkeit einer Freistellungsklausel; Widerruf der Dienstwagennutzung).

Tragende Aussage: Eine vom Arbeitgeber vorformulierte (formularmäßige) Klausel, die diesen ohne weitere Voraussetzungen berechtigt, den Arbeitnehmer nach Ausspruch einer Kuendigung bis zum Ablauf der Kuendigungsfrist von der Arbeitsleistung unter Fortzahlung der Verguetung freizustellen, ist nach § 307 Abs. 1 Satz 1 BGB unwirksam. Der verfassungsrechtlich geschuetzte Beschaeftigungsanspruch des Arbeitnehmers ueberwiegt das pauschale Freistellungsinteresse. Eine Freistellung verlangt einen konkreten Anlasstatbestand (z.B. Geheimhaltungs-, Konkurrenz- oder Vertrauensschutz) und Interessenabwaegung im Einzelfall.

Offene Quelle: dejure.org, Vernetzung BAG 25.03.2026 - 5 AZR 108/25; BAG-Pressemitteilung "Wirksamkeit einer Freistellungsklausel - Widerruf der Dienstwagennutzung". Status: Volltext zum Stand der Bearbeitung noch nicht voll veroeffentlicht - vor Schriftsatzverwendung Volltext pruefen.

Der Beschäftigungsanspruch des Arbeitnehmers darf nur mit verifizierter Rechtsprechung begründet werden. Vor einer Ausgabe ist zu prüfen, welche Entscheidung die tragende Aussage wirklich trägt und ob sie für Freistellung nach Kündigung, AGB-Kontrolle und Annahmeverzug passt.

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 307 Abs. 1 BGB | AGB-Inhaltskontrolle: unangemessene Benachteiligung |
| § 307 Abs. 2 Nr. 1 BGB | Abweichung vom wesentlichen Grundgedanken der gesetzlichen Regelung |
| § 615 BGB | Annahmeverzug: AG schuldet Vergütung bei verweigerter Beschäftigung |
| § 611a BGB | Beschäftigungspflicht als vertragliche Hauptpflicht |
| Art. 1, 2 GG | Persönlichkeitsrecht und allgemeines Persönlichkeitsrecht als Grundlage des Beschäftigungsanspruchs |

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wann ist Freistellung weiterhin zulässig

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Freistellungsgrund | Anforderung |
|---|---|
| Geheimhaltungsbedenken | Konkreter Zugang zu schutzbedürftigen Informationen (Kundendaten, Produktentwicklung, Preisstrategien) |
| Konkurrenzsorge | Konkrete Tatsachen für geplanten Wechsel zu Mitbewerber; bloßer Branchenwechsel genügt nicht |
| Vertrauensverlust | Pflichtenverletzung, die die Kündigung trägt; schwere Loyalitätsverletzung |
| Störung Betriebsfrieden | Konkrete erhebliche Störung, dokumentiert; bloße Antipathie reicht nicht |
| Überlapping-Beschäftigung nicht möglich | Stelle bereits neu besetzt; Tätigkeiten physisch nicht mehr vorhanden |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anwaltliche Strategie

### Aus Arbeitnehmer-Sicht

| Konstellation | Empfehlung |
|---|---|
| Mandantin will weiterzuarbeiten (Reputation, laufende Projekte) | Beschäftigungsanspruch geltend machen; AG in Annahmeverzug setzen |
| Mandantin will nicht weiterarbeiten, aber Vergleich | Beschäftigungsanspruch als Verhandlungsmasse nutzen; höhere Abfindung fordern |
| Aufhebungsvertrag in Vorbereitung | Freistellungsklausel konkret formulieren; Einzelfall begründen |

### Aus Arbeitgeber-Sicht

| Konstellation | Empfehlung |
|---|---|
| Freistellung notwendig wegen Konkurrenz | Konkrete Tatsachen dokumentieren; Freistellung mit schriftlicher Begründung erklären |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Neue Freistellungsklausel im AV | Klausel mit offenem Tatbestand ("soweit sachlich begründeter Anlass besteht") formulieren; Inhaltskontrolle prüfen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — widerrufliche Freistellungsklausel in Klageschrift ruegen | Ruege-Baustein nach Template unten |
| Variante A — Mandant will trotzdem Freistellung | Freistellungs-Vereinbarung mit klarer Vergaetungspflicht statt ruegen |
| Variante B — Arbeitgeber hat Klausel nicht aktiviert | Praeventivruegeung in Klageschrift aufnehmen |
| Variante C — Klausel wurde bereits aktiviert | Lohnfortzahlungsklage unverzueglich erheben |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbaustein — Beschäftigungsanspruch geltend machen

```
Die Beklagte hat das Arbeitsverhältnis am [Datum] gekündigt
und die Klägerin gleichzeitig unter Hinweis auf § [X] des
Arbeitsvertrags von der Arbeitsleistung freigestellt.

Die in § [X] enthaltene Klausel ist eine formularmäßige
Standardklausel, die den Arbeitgeber pauschal und ohne
weitere Voraussetzung zur einseitigen Freistellung
berechtigen soll. Diese Klausel ist nach der Rechtsprechung
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
unwirksam, weil sie die Klägerin unangemessen benachteiligt
im Sinne des § 307 Abs. 1 BGB.

Konkrete tragfaehige Gründe für eine Freistellung legt die
Beklagte nicht dar. Pauschale Hinweise genuegen nicht.

Der Beschaeftigungsanspruch der Klaegerin (BAG GS,
nach verifizierter Rechtsprechung besteht bis zum Ablauf der
Kuendigungsfrist am [Datum] fort.

Die Beklagte befindet sich seit [Datum der Freistellung]
in Annahmeverzug nach § 615 BGB.
```

## Schriftsatzbaustein — Annahmeverzug-Antrag

```
Es wird beantragt:

1. Die Beklagte wird verurteilt, die Klägerin zu
 den bisherigen Arbeitsbedingungen als [Tätigkeit]
 tatsächlich zu beschäftigen.

2. Die Beklagte wird verurteilt, an die Klägerin
 EUR [Betrag] brutto (Vergütung für den Zeitraum
 [Datum] bis [Datum]) nebst Zinsen in Höhe von
 5 Prozentpunkten über dem Basiszinssatz ab
 Fälligkeit zu zahlen.

Begründung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
unwirksam. Die Beklagte ist seit [Datum] in Annahme-
verzug. Die Vergütung für den Annahmeverzugszeitraum
berechnet sich wie folgt: [Monat x Brutto-Monatsgehalt].
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast und Darlegungslast

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- AGB-Inhaltskontrolle prüft das Gericht von Amts wegen; keine Beweislast der Parteien.

## Prüfschema Freistellung

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Rechtsfolge bei Fehler |
|---|---|---|---|
| 1 | Freistellungsklausel im AV vorhanden? | § 307 BGB | Nur Einzelfall-Freistellung möglich |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 3 | Konkreter Freistellungsgrund? (Tabelle oben) | § 307 Abs. 1 BGB | Ohne Grund: Freistellung unwirksam |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 5 | AG in Annahmeverzug? | § 615 BGB | Vergütungspflicht trotz Freistellung |
| 6 | Wettbewerbsverbot relevant? | §§ 74 ff. HGB | Bei nachvertr. Wettbewerbsverbot: Karenzentschädigung |

## Fristen

| Frist | Dauer | Rechtsgrundlage |
|---|---|---|
| Annahmeverzug | Ab Zeitpunkt der Freistellung, wenn kein Grund | § 615 BGB |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Schadensersatz bei unwirksamer Freistellung | 3 Jahre | §§ 195, 199 BGB |

## Streitwert und Kosten

- **Weiterbeschäftigungsantrag**: Bruttomonatsverdienst (§ 42 Abs. 2 GKG).
- **Annahmeverzug-Anspruch**: Summe der ausstehenden Vergütung.
- **Erste Instanz**: § 12a ArbGG — keine Kostenerstattung.
- **Wirtschaftlicher Hauptwert**: meist im Vergleich (Abfindungs-Erhöhung wegen Beschäftigungsanspruch).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Klausel-Wortlaut | Bewertung |
|---|---|
| "Der Arbeitnehmer wird nach Kündigung freigestellt." | Unwirksam — pauschal, kein Tatbestand |
| "Bei betriebsbedingter Kündigung kann der AG freistellen." | Wahrscheinlich unwirksam — kein konkreter Anlass |
| "Freistellung erfolgt, wenn berechtigte Geheimhaltungsinteressen vorliegen." | Wirksam — konkreter offener Tatbestand |
| "Freistellung erfolgt bei konkreter Gefährdung von Geschäftsgeheimnissen." | Wirksam — hinreichend konkret |

## Anschluss-Skills

- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` — parallele Kündigungsschutzklage
- `fachanwalt-arbeitsrecht-betriebsratsanhoerung` — bei Fragen zur BR-Anhörung
- `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` — wenn Freistellung als Repressalie

## Quellen

- BGB §§ 307, 615, 611a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 2. `spezial-freistellungsklausel-sonderfall-und-edge-case`

**Fokus:** Freistellungsklausel im Arbeitsvertrag: BAG 5 AZR 108/25 (pauschale Klausel unwirksam), anlassbezogene Formulierung, Vergütungsfortzahlung, Urlaubsverfall während Freistellung, Verrechnung mit Urlaubsabgeltung, Edge Cases.

### Spezial: Freistellungsklausel — Sonderfall und Edge Cases

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Freistellungsklausel — Sonderfall und Edge Cases` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Vertiefte Analyse der Freistellungsklausel im Arbeitsvertrag — nach dem Paradigmenwechsel durch BAG 5 AZR 108/25. Der Skill behandelt die Unwirksamkeit pauschaler Klauseln, korrekte Formulierung und die wichtigsten Edge Cases.

## Einstieg
Wenn ein Sachverhalt mit Freistellungsklausel vorliegt, zuerst klären:

1. **Vorlage der Klausel:** Liegt der genaue Klauseltext vor?
2. **Zeitpunkt:** Geht es um eine Freistellung bei Kündigung, bei Aufhebungsvertrag oder bei laufendem Vertrag?
3. **Vergütung:** Ist in der Klausel geregelt, ob Vergütung weitergezahlt wird?
4. **Urlaubsanspruch:** Welcher Urlaub ist noch offen? Wird er verrechnet?
5. **BAG 5 AZR 108/25:** Wann war die Klausel vereinbart? (Vor oder nach dem Urteil?)

## BAG 5 AZR 108/25 (25.03.2026) — Paradigmenwechsel

### Kernsatz des BAG
Das BAG hat entschieden, dass eine formularvertragliche pauschale Freistellungsklausel, die den Arbeitgeber berechtigt, den Arbeitnehmer jederzeit und ohne Angabe von Gründen freizustellen, nach § 307 Abs. 1 Satz 1 BGB unwirksam ist.

**Begründung:** Eine solche Klausel benachteiligt den Arbeitnehmer unangemessen, weil sie ohne sachliche Rechtfertigung in seine berufliche Entwicklung und seinen Beschäftigungsanspruch eingreift.

**Quellenregel:** BAG 5 AZR 108/25, Pressemitteilung vom 25.03.2026 auf [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de); [dejure.org](https://dejure.org)-Vernetzung. Urteilstext live prüfen.

### Konsequenzen für bestehende Verträge
- Bestehende pauschale Freistellungsklauseln sind nach § 307 Abs. 1 Satz 1 BGB unwirksam
- Unwirksamkeit der Klausel bedeutet: Arbeitgeber kann nicht mehr auf die Klausel gestützt freistellen
- Stattdessen: Freistellung nur bei konkretem Anlasstatbestand und nach Interessenabwägung

### Konsequenzen für neue Vertragsgestaltung
Neue Freistellungsklauseln müssen:
1. Einen konkreten Anlasstatbestand benennen (z.B. nach Ausspruch einer Kündigung)
2. Die Vergütungsfortzahlung während der Freistellung regeln
3. Die Verrechnung mit offenen Urlaubsansprüchen transparent machen
4. Eine klare zeitliche Begrenzung enthalten

## Wirksame Freistellungsklausel — Muster (post-BAG 5 AZR 108/25)

### Variante 1: Nach Kündigung
> „Nach Ausspruch einer ordentlichen oder außerordentlichen Kündigung durch eine der Parteien ist der Arbeitgeber berechtigt, den Arbeitnehmer unter Fortzahlung der vertragsgemäßen Vergütung von der Arbeitsleistung freizustellen. Die Freistellung erfolgt unter Anrechnung noch offener Urlaubs- und etwaiger Überstundenansprüche. Die Freistellung gilt nicht als Erledigung des Vergütungsanspruchs des Arbeitnehmers."

### Variante 2: Bei berechtigtem Interesse (enger)
> „Der Arbeitgeber ist berechtigt, den Arbeitnehmer bei Vorliegen eines berechtigten betrieblichen Interesses (insbesondere nach Ausspruch einer Kündigung oder bei Verdacht einer schwerwiegenden Pflichtverletzung) vorübergehend unter Fortzahlung der Vergütung von der Arbeit freizustellen. Offene Urlaubsansprüche werden auf den Freistellungszeitraum angerechnet."

## Urlaubsverfall während Freistellung

### Grundregel
Während einer bezahlten Freistellung kann Urlaub gewährt werden, wenn:
- Die Freistellung konkret auf den Urlaubsanspruch angerechnet wird (ausdrückliche Erklärung erforderlich)
- Der Arbeitnehmer tatsächlich frei disponieren kann (kein gleichzeitiger Bereitschaftsdienst etc.)

### BAG 9 AZR 104/24 (03.06.2025) — kein Urlaubsverzicht durch Prozessvergleich
Das BAG hat entschieden, dass auf gesetzlichen Mindesturlaub im laufenden Arbeitsverhältnis nicht durch Prozessvergleich verzichtet werden kann. Das betrifft auch Abgeltungsklauseln in Aufhebungsverträgen, die Urlaubsabgeltung pauschal mitregeln.

**Konsequenz:** Jede Abgeltungsklausel muss sicherstellen, dass der gesetzliche Mindesturlaub (§ 3 BUrlG: 24 Werktage) tatsächlich abgegolten wird — und zwar zum Zeitpunkt der Beendigung.

## Edge Cases

### Edge Case 1: Freistellung und Wettbewerbsverbot
Während einer Freistellung kann der Arbeitnehmer keine Konkurrenztätigkeit aufnehmen — das Wettbewerbsverbot läuft weiter, bis das Arbeitsverhältnis endet.

### Edge Case 2: Freistellung und Krankmeldung während der Freistellung
- EFZG: Entgeltfortzahlungsanspruch bei Krankheit besteht auch während Freistellung (6 Wochen)
- Der Urlaubsabzug für die Freistellungszeit kann bei Krankheit nicht durchgeführt werden (§ 9 BUrlG: Krankentage sind keine Urlaubstage)

### Edge Case 3: Einseitige Freistellung ohne Klausel
Ohne wirksame Klausel oder triftigen Grund kann der Arbeitgeber nicht einseitig freistellen. Konsequenz: Weiterbeschäftigungsanspruch des Arbeitnehmers; Klage auf Beschäftigung möglich.

### Edge Case 4: Freistellung im Aufhebungsvertrag
Bei Aufhebungsverträgen: explizite Freistellungsklausel vereinbaren; Urlaubsabrechnung und Vergütungsfortzahlung transparent regeln; BAG 9 AZR 104/24 beachten (Urlaubsverzicht).

## Prüfschema Freistellungsklausel

| Prüfpunkt | Ergebnis | Konsequenz |
|---|---|---|
| Liegt eine formularvertragliche Klausel vor? | Ja/Nein | Ja → AGB-Kontrolle § 307 BGB |
| Enthält die Klausel einen Anlasstatbestand? | Ja/Nein | Nein → nach BAG 5 AZR 108/25 unwirksam |
| Ist Vergütungsfortzahlung geregelt? | Ja/Nein | Nein → Risiko für AG |
| Ist Urlaubsverrechnung transparent? | Ja/Nein | Nein → Urlaubsanspruch bleibt offen |
| BAG 9 AZR 104/24 beachtet? | Ja/Nein | Nein → Mindesturlaub nicht abgegolten |

## Anschluss-Skills
- `ar-aufhebungsvertrag-praxis` für Aufhebungsvertrags-Kontext
- `spezial-urlaub-livequellen-und-rechtsprechungscheck` für Urlaubsfragen
- `workflow-redteam-qualitygate` für Klauselprüfung

## Quellenregel
- BAG 5 AZR 108/25: [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de) Pressemitteilung; [dejure.org](https://dejure.org). Urteilstext live prüfen.
- BAG 9 AZR 104/24: [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de); [dejure.org](https://dejure.org).
- Keine modellwissensbasierten Klauselaussagen ohne Normgrundlage.
- Annahmen explizit kennzeichnen.

## Was dieser Arbeitsgang nicht macht
- Keine individuelle Klauselgestaltung ohne Mandantenkenntnis.
- Keine Prognose über Wirksamkeit jeder konkreten Klausel ohne Vorlage des Wortlauts.

## 3. `ar-abfindungs-rechner-modular`

**Fokus:** Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG. Beispielrechnung und Mustertext für Aufhebungsvertrag und Vergleich.

### AR: Abfindungs-Rechner (modular)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AR: Abfindungs-Rechner (modular)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck
Strukturierte Berechnung und Verhandlungsvorbereitung bei Abfindungen — vom Erstgespräch bis zur Vergleichsformel. Der Skill liefert sowohl eine Rechenlogik als auch eine Strategie-Matrix für den Güte- und Kammertermin vor dem Arbeitsgericht.

## Einstieg
Wenn Unterlagen vorliegen, arbeite zuerst damit. Nur die Rückfragen stellen, die für die erste Weiche nötig sind:

1. **Rolle und Mandat:** Vertritt der Anwalt Arbeitnehmer oder Arbeitgeber? Was ist das Ziel — Maximierung, schnelle Einigung, Sperrzeitvermeidung?
2. **Eckdaten:** Brutto-Monatsgehalt (inkl. regelmäßiger Zulagen), Beschäftigungsdauer in vollen Jahren, Geburtsjahr, Unterhaltspflichten.
3. **Kündigungsart und -risiko:** Ordentliche oder außerordentliche Kündigung? KSchG anwendbar (§ 23 KSchG: > 10 VZÄ, § 1 KSchG: > 6 Monate)? Welche Angriffspunkte sind erkennbar?
4. **Fristen und Verfahrensstand:** Klagefrist § 4 KSchG gewahrt? Gütetermin bereits anberaumt?
5. **Sozialrechtliche Lage:** Wünscht der Mandant nahtlosen Übergang zu ALG I oder ist eine Sperrzeit tolerierbar?

## Rechenlogik — Faustformel und BAG-Linie

### Grundformel
```
Abfindung = Brutto-Monatsgehalt × Beschäftigungsjahre × Faktor
```

| Lage | Faktor |
|---|---|
| Schwache Kündigung (viele Angriffspunkte) | 0,75 – 1,5 |
| Mittlere Lage | 0,5 (BAG-Orientierungswert) |
| Starke Kündigung (kaum Angriffspunkte) | 0,25 – 0,4 |
| Sonderkündigungsschutz (BR, MuSchG, BEEG) | Verhandlungssache; kein gesetzlicher Anspruch |

**Hinweis:** Die Faustformel folgt der langjährigen Verhandlungspraxis; einen gesetzlichen Anspruch auf Abfindung gibt es nur in § 9 KSchG (Auflösungsantrag), § 1a KSchG (betriebsbedingte Kündigung mit Klageverzicht) und bei einvernehmlichem Aufhebungsvertrag.

### Gesetzliche Obergrenzen § 10 KSchG
- Grundregel: bis zu 12 Monatsgehälter
- Bei Vollendung des 50. Lebensjahres und ≥ 15 Jahren Betriebszugehörigkeit: bis zu 15 Monatsgehälter
- Bei Vollendung des 55. Lebensjahres und ≥ 20 Jahren Betriebszugehörigkeit: bis zu 18 Monatsgehälter

### § 1a KSchG — betriebsbedingte Kündigung mit Klageverzicht
- Arbeitgeber bietet in der Kündigungserklärung Abfindung an (0,5 Monatsgehälter/Jahr)
- Arbeitnehmer verzichtet auf Kündigungsschutzklage
- Sperrzeit-Risiko dennoch prüfen; BA urteilt eigenständig

## Sperrzeit § 159 SGB III

### Sperrzeittatbestände
- Eigenkündigung oder Aufhebungsvertrag auf Initiative des Arbeitnehmers → 12 Wochen reguläre Sperrzeit
- Aufhebungsvertrag auf Arbeitgeberinitiative mit „wichtigem Grund" → Sperrzeitbefreiung möglich
- Entlassungsentschädigung (Abfindung) → verkürzt das ALG I nach § 158 SGB III, wenn Kündigungsfrist unterschritten

### Wichtiger Grund (Sperrzeitbefreiung)
Die Bundesagentur für Arbeit (BA) prüft eigenständig: Der Arbeitnehmer muss nachweisen, dass er die Beendigung nicht selbst herbeigeführt hat oder ein anerkannter wichtiger Grund vorlag (z.B. betriebsbedingte Kündigung war unausweichlich, psychische Belastung durch Arbeitssituation, nachgewiesene Pflegesituation).

**Quellenregel:** BA-Merkblätter und Dienstanweisungen der BA live prüfen unter bundesagentur.de; keine modellwissensbasierten Sperrzeitformeln ohne aktuellen Quellenbeleg ausgeben.

## Steuerliche Fünftelregelung § 34 Abs. 1 EStG

### Voraussetzungen
- Außerordentliche Einkünfte (hier: Abfindung als Entschädigung für entgehende Einnahmen)
- Zusammenballung von Einkünften in einem Veranlagungszeitraum
- Anwendbar nur, wenn die Abfindung höher als der entgangene Arbeitslohn ist

### Rechenbeispiel (vereinfacht)
```
Reguläres Jahreseinkommen: 60.000 €
Abfindung: 30.000 €
Steuerpflichtiges Einkommen o. §34: 90.000 €
Mit Fünftelregelung:
 Fiktives EK = 60.000 + (30.000 / 5) = 66.000 €
 Steuer auf 66.000 = X
 Mehrsteuern auf 66.000 vs. 60.000 = Y → Y × 5 = tatsächliche Steuer auf Abfindung
```

**Hinweis:** Individuelle Steuerberatung bleibt dem Steuerberater vorbehalten; die anwaltliche Aufgabe ist die Aufklärung über das Instrument und die korrekte Vertragsgestaltung (Abfindung als Entschädigung klar benennen).

## Verhandlungsstrategie und Vergleichsformeln

### Güte- und Kammertermin Arbeitsgericht
- Streitwert nach § 42 Abs. 2 GKG: ein Vierteljahresverdienst bei Bestandsschutzstreitigkeiten
- Gerichtliche Vergleiche regeln regelmäßig: Beendigungsdatum, Abfindungshöhe und -fälligkeit, Freistellungszeit, Zeugnisnote, Herausgabe von Unterlagen, etwaige Geheimhaltung

### Muster-Vergleichsformel (Kurzfassung)
> „Die Parteien sind sich einig, dass das zwischen ihnen bestehende Arbeitsverhältnis durch ordentliche arbeitgeberseitige Kündigung vom [Datum] mit Ablauf des [Beendigungsdatum] geendet hat. Die Beklagte zahlt zur Abgeltung aller gegenseitigen Ansprüche aus dem Arbeitsverhältnis und seiner Beendigung an den Kläger eine Abfindung gemäß §§ 9, 10 KSchG in Höhe von [Betrag] brutto, fällig am [Datum]."

### Gegenargumente und Red-Team-Punkte
- Hat der Arbeitgeber die Sozialauswahl dokumentiert? Fehlt die Dokumentation → Angriffsvektor
- Wurde der Betriebsrat ordnungsgemäß nach § 102 BetrVG angehört? → Fehler = Unwirksamkeit
- Massenentlassung § 17 KSchG: Anzeige korrekt und rechtzeitig? (Vgl. BAG 6 AZR 152/22 und EuGH C-134/24)
- Betriebsgröße knapp bei 10 VZÄ: Leiharbeitnehmer, Teilzeitkräfte korrekt gezählt?

## Anschluss-Skills
- `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` für vertiefte Sperrzeitprüfung
- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` für Prüfschema und Klageschrift
- `fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg` für Verhandlungsstrategie
- `spezial-kschg-risikoampel-und-gegenargumente` für Risikoampel

## Quellenregel
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link ausgeben: [dejure.org](https://dejure.org), [openjur.de](https://openjur.de), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de), [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.
- Steuerliche Aussagen als Hinweise kennzeichnen; für Steuerbescheide und -erklärungen Steuerberater empfehlen.
- Annahmen explizit markieren; keine erfundenen BA-Dienstanweisungen oder Praxisformeln ohne Quellenbeleg.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollständige Mandantenberatung oder steuerliche Beratung.
- Keine Festlegung ohne ausdrückliche Mandantenentscheidung.
- Keine Spekulation über individuelle BA-Entscheidungen zur Sperrzeit.
