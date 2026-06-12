# Megaprompt: fachanwalt-arbeitsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 78 Skills des Plugins `fachanwalt-arbeitsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Z…
2. **orientierung-mandat-fachanwaltschaft** — Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO: Anwe…
3. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konfli…
4. **erstpruefung-und-mandatsziel** — Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielform…
5. **output-waehlen** — Output-Wahl für Fachanwalt Arbeitsrecht: stimmt Adressat (Arbeitnehmer, Arbeitgeber, Betriebsrat), Frist (§ 4 KSchG 3 Wo…
6. **ar-abfindungs-rechner-modular** — Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verha…
7. **ar-aufhebungsvertrag-praxis** — Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG, AGB-Kontrolle von…
8. **ar-einfuehrung-mandantenanliegen** — Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Befristung, Maßregelungsverbot, Dis…
9. **ar-konkurrenzklausel-spezial** — Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB analog: Karenzentschädigung ≥ 50 %, Schriftform, Verbindlichkeit, Frei…
10. **befristung-compliance-dokumentation-und-akte** — Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbefristung-Dokument…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Arbeitsrecht

> Kündigung, Aufhebungsvertrag, Befristung, Betriebsrat, Betriebsübergang — sieben Eilfristen, ein Klagestrang.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 4 KSchG: 3 Wochen** ab Zugang Kündigung. Daneben § 626 II BGB (außerordentlich, 2 Wochen ab Kenntnis), § 15 IV AGG (2 Monate Geltendmachung), § 17 KSchG (Massenentlassungsanzeige), § 9 MuSchG, § 613a VI BGB (1 Monat Widerspruch). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Kündigungsschutz §§ 1, 4, 7 KSchG · Lohn §§ 611a, 614, 615 BGB (Annahmeverzug) · Schadensersatz §§ 280 I, 823 BGB · AGG-Entschädigung §§ 7, 15 AGG · Betriebsübergang § 613a BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Arbeitsgericht am Arbeitsort (§ 48 ArbGG, § 17 ZPO). Streitwert KSchG-Klage: 1/4 Bruttojahresgehalt (§ 42 II GKG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kündigung mit laufender 3-Wochen-Frist: heute Klageschrift. 🟠 Aufhebungsvertrag mit Widerrufsoption: 14 Tage prüfen. 🟢 Lohnklage ohne Verfallsklausel.
- **Beweislage:** 🟠 Zugang der Kündigung trägt der Arbeitgeber (§ 130 BGB); Zustellungsnachweis sichern. 🔴 Bei mündlicher Kündigung: Zeugen organisieren.
- **Wirtschaftlich:** 🔴 Lohnverlust > 3 Monate + Verlust SV-Pflicht: Eilantrag Weiterbeschäftigung (§ 102 V BetrVG) prüfen. 🟠 Abfindung ≈ 0,5 Monatsgehälter pro BJ als Verhandlungsstart.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Kündigung erhalten — Schutzklage prüfen** | `ar-kuendigungspruefung-workflow` | Klageschrift mit Anträgen, Streitwertangabe, Antrag auf vorläufige Weiterbeschäftigung |
| Aufhebungsvertrag angeboten | `ar-aufhebungsvertrag-praxis` | Risikomatrix, Abfindungs-Range, Sperrzeit § 159 SGB III |
| Befristung soll geprüft werden | `befristung-tzbfg` | Sachgrund- vs. sachgrundlose Befristung, Anschlussverbot § 14 II 2 TzBfG |
| Betriebsrats-Beteiligung streitig | `beteiligung-betriebsrat-102-betrvg` | Anhörungsfehler, Heilung, Folge der Unwirksamkeit |
| Betriebsübergang im Raum | `ar-betriebsuebergang-spezial` | Widerspruchsfrist § 613a VI BGB (1 Monat), Informationsanspruch |

## Norm-Radar (live verifizieren)

- **§ 4 KSchG** — 3-Wochen-Frist Kündigungsschutzklage
- **§ 626 BGB** — außerordentliche Kündigung, 2-Wochen-Frist Abs. 2
- **§ 1 KSchG** — Sozialwidrigkeit; KSchG-Anwendung ab 10 AN (Kleinbetrieb)
- **§§ 611a, 615 BGB** — Arbeitsvertrag, Annahmeverzug
- **§ 613a BGB** — Betriebsübergang; Widerspruchsrecht Abs. 6
- **§ 102 BetrVG** — Anhörung Betriebsrat; Folge der Unwirksamkeit

## Genau eine Rückfrage (nur wenn nötig)

> Liegt eine **Kündigung mit Zugangsdatum** vor — oder ist der Triggerpunkt ein anderer (Befristung, Lohn, Aufhebungsvertrag, AGG)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Kündigungsschutz § 1 KSchG; Sozialwidrigkeit** — BAG 2. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`
- **Betriebsübergang § 613a BGB; Identitätswahrung** — BAG 8. Senat (Spijkers-/Süzen-Linie) — *live verifizieren auf* `bundesarbeitsgericht.de + EuGH curia.europa.eu`
- **Befristung ohne Sachgrund; Vorbeschäftigung § 14 II 2 TzBfG** — BAG 7. Senat; BVerfG 1. Senat — *live verifizieren auf* `bundesarbeitsgericht.de + bundesverfassungsgericht.de`
- **AGG-Entschädigung § 15 II; 2-Monats-Frist** — BAG 8. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

## Aktuelle BAG-Linie 2025/2026 (live verifizieren vor Schriftsatzverwendung)

Drei aktuelle Leitentscheidungen, die ueber das Arbeitsrecht in den letzten zwoelf Monaten besonders weit ausstrahlen:

| Entscheidung | Tragende Aussage | Skill-Vertiefung |
| --- | --- | --- |
| **BAG, Urt. v. 23.10.2025 - 8 AZR 300/24** | **Equal Pay - Paarvergleich genuegt.** Eine einzige besser bezahlte Vergleichsperson des anderen Geschlechts mit gleicher oder gleichwertiger Arbeit reicht, um die Vermutung des $ 22 AGG auszuloesen. Der Arbeitgeber muss konkret darlegen, dass die Differenz ausschliesslich auf objektiven, geschlechtsneutralen Gruenden beruht. Pauschale Hinweise auf Medianwerte, Durchschnittsbetrachtungen oder Verhandlungsgeschick reichen nicht. Art. 157 AEUV bekommt damit Schaerfe. | `bag-equal-pay-paarvergleich` (fachanwalt-arbeitsrecht) / `bag-equal-pay-paarvergleich-8azr30024` (arbeitsrecht) |
| **BAG, Urt. v. 03.06.2025 - 9 AZR 104/24** | **Kein Verzicht auf gesetzlichen Mindesturlaub.** Im bestehenden Arbeitsverhaeltnis koennen Arbeitnehmer:innen auf den gesetzlichen Mindesturlaub nicht wirksam verzichten - auch nicht durch gerichtlichen Vergleich. Gilt selbst dann, wenn die Beendigung bereits feststeht und absehbar ist, dass der Urlaub krankheitsbedingt nicht mehr genommen werden kann. Ausgleichs-/Erledigungs-/Abgeltungsklauseln muessen sauber zwischen gesetzlichem Mindesturlaub, vertraglichem Mehrurlaub und bereits entstandener Urlaubsabgeltung unterscheiden. | `bag-mindesturlaub-kein-verzicht` (fachanwalt-arbeitsrecht) / `bag-mindesturlaub-kein-verzicht-9azr10424` (arbeitsrecht) |
| **BAG, Urt. v. 25.03.2026 - 5 AZR 108/25** | **Pauschale Freistellungsklauseln in Arbeitsvertragsformularen unwirksam.** Eine formularmaessige Freistellungsklausel, die dem Arbeitgeber das einseitige Recht gibt, Beschaeftigte nach Kuendigung unter Fortzahlung der Verguetung freizustellen, ist nach AGB-Kontrolle unwirksam, wenn sie Arbeitnehmer:innen unangemessen benachteiligt. Freistellung bleibt im konkreten Fall moeglich - braucht aber einen tragfaehigen Grund (ueberwiegende schutzwuerdige Arbeitgeberinteressen). Die pauschale Vorratsklausel reicht nicht. | `bag-freistellungsklausel-unwirksam` (fachanwalt-arbeitsrecht) / `bag-freistellungsklausel-unwirksam-5azr10825` (arbeitsrecht) |

> Diese drei Aktenzeichen sind Sucheinstieg. Vor Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (bundesarbeitsgericht.de, dejure.org) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung. Spezial-Skills oben enthalten Pruefschemata, Klagebausteine und Verteidigungsmuster.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO: Anwendungsfall Kanzlei wi..._

# Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO. Anwendungsfall Kanzlei will Arbeitsrechtsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung vor. Normen BGB §§ 611a ff. KSchG BetrVG TVG BUrlG EFZG TzBfG AGG ArbGG. Prüfraster Individualarbeitsrecht Kollektivarbeitsrecht Diskriminierungsschutz Verfahren ArbGG LAG BAG verifizierbare Quellen. Output Rechtsgebietsuebersicht mit Normenhierarchie Pflichtliteratur und Mandatstriage-Hinweisen. Abgrenzung zu erstgespraech-mandatsannahme und mandat-triage-Skill.

### Fachanwalt für Arbeitsrecht — Orientierung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Arbeitsrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## FAO-Voraussetzungen (§ 10 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 100 Fälle in den letzten drei Jahren aus dem Arbeitsrecht; davon mindestens 50 Mandate im Individualarbeitsrecht, mindestens 10 Mandate im Kollektivarbeitsrecht, mindestens 20 rechtsförmliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Individualarbeitsrecht | BGB §§ 611a ff. (Arbeitsvertrag); KSchG (Kündigungsschutz); BUrlG (Urlaub); EFZG (Entgeltfortzahlung); TzBfG (Teilzeit und Befristung); NachwG (Nachweisgesetz, idF Aug. 2022); MuSchG; BEEG; ArbZG; ArbStättV |
| Kollektivarbeitsrecht | BetrVG (Betriebsverfassung); TVG (Tarifvertrag); MitbestG; DrittelbG; SprAuG |
| Diskriminierung | AGG (§§ 1, 7, 15) |
| Arbeitsschutz | ArbSchG; ArbStättV; ArbMedVV |
| Insolvenz | InsO §§ 113, 125 ff. |
| Verfahren | ArbGG (Arbeitsgerichtsgesetz) |
| Internationale Bezüge | Rom I-VO; AEntG; AÜG |

## Typische Mandate

- Kündigungsschutzklage (§ 4 KSchG).
- Aufhebungsvertrag (Verhandlung, Sozialplan).
- Befristungskontrollklage (§ 17 TzBfG).
- Sozialplan / Interessenausgleich nach § 112 BetrVG (Kollektivseite).
- Betriebsratsanhörung nach § 102 BetrVG.
- Zeugnisstreitigkeit (§ 109 GewO).
- AGG-Entschädigungsklage (§ 15 AGG).
- Lohn- und Gehaltsklage.
- Mobbing und Schadensersatzklage (§ 280 Abs. 1 BGB iVm Schutzpflicht § 241 Abs. 2 BGB).

## Fristen (Auswahl)

- **Kündigungsschutzklage** § 4 KSchG — drei Wochen ab Zugang der schriftlichen Kündigung.
- **Befristungskontrollklage** § 17 TzBfG — drei Wochen nach vereinbartem Ende.
- **AGG-Entschädigung** § 15 Abs. 4 AGG — schriftliche Geltendmachung binnen zwei Monaten; Klagefrist § 61b ArbGG drei Monate.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Anhörung des Betriebsrats** § 102 BetrVG — eine Woche bei ordentlicher, drei Tage bei außerordentlicher Kündigung.
- **Sozialplanverhandlungen** § 112 Abs. 2, 3 BetrVG — Einigungsstelle nach Scheitern.

## Hauptgerichte

- Arbeitsgericht (ArbG) — erste Instanz, Kammern.
- Landesarbeitsgericht (LAG) — Berufungsinstanz.
- Bundesarbeitsgericht (BAG) — Revisionsinstanz, Erfurt.
- BVerfG bei Grundrechtsfragen.
- EuGH bei unionsrechtlichen Fragen (Befristung, Arbeitszeit, Gleichbehandlung).

## Berufsverband

- Arbeitsgemeinschaft Arbeitsrecht im DAV.

## Schnittstellen

- **`arbeitsrecht`** für operative Mandatsführung, Vorlagen.
- **`kanzlei-allgemein`** für Fristen und Versand.
- **`fachanwalt-sozialrecht`** bei Schnittstellen zur Arbeitslosenversicherung und Sperrzeit.
- **`fachanwalt-insolvenz-sanierungsrecht`** bei Betriebsübergang § 613a BGB und Insolvenz.

## Aktuelle Rechtsprechung - Ueberblick wichtiger Leitentscheidungen (Stand Mai 2026)

Folgende Leitentscheidungen sind im aktuellen Plugin-Stand mit offener Quelle (dejure.org / bundesarbeitsgericht.de) belegt:

- **BAG, 23.10.2025 - 8 AZR 300/24** (Paarvergleich Equal Pay): Ein einzelner Vergleichskollege des anderen Geschlechts genuegt zur Vermutung nach § 22 AGG. Siehe Skill `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich`.
- **BAG, 03.06.2025 - 9 AZR 104/24** (kein Urlaubsverzicht durch Prozessvergleich): Mindesturlaub waehrend laufenden Arbeitsverhaeltnisses nicht disponibel. Siehe Skill `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht`.
- **BAG, 25.03.2026 - 5 AZR 108/25** (Freistellungsklausel unwirksam): Pauschale formularmäßige Freistellungsklausel verstoesst gegen § 307 BGB. Siehe Skill `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`.
- **BAG, 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22** (Massenentlassung): Fehlerhafte oder verfruehte Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller Kuendigungen. Siehe Skill `fachanwalt-arbeitsrecht-massenentlassung-17-kschg`.
- **EuGH, 30.10.2025 - C-134/24 und C-402/24** (Massenentlassung): Keine Heilung fehlender oder verfruehter Anzeige nach Kuendigungsausspruch.
- **BAG, 20.02.2025 - 8 AZR 61/24** (DSGVO-Schadensersatz): "Stoergefuehl" allein begruendet keinen Anspruch nach Art. 82 DSGVO.
- **BAG, 18.06.2025 - 7 AZR 50/24** (Befristung Betriebsratsmitglieder): § 14 Abs. 2 TzBfG anwendbar; Schadensersatz auf Folgevertrag bei Mandatsbenachteiligung.
- **BAG, 22.09.2022 - 8 AZR 4/21** (NachweisG): Schadensersatz neben Bussgeld bei Pflichtverletzung des Arbeitgebers nach NachwG.
- **BAG, 13.09.2022 - 1 ABR 22/21** (Arbeitszeiterfassung): Pflicht des Arbeitgebers zur systematischen Arbeitszeiterfassung aus § 3 Abs. 2 Nr. 1 ArbSchG.

Vor Schriftsatzverwendung jeweils Volltext und ggf. neuere Rechtsprechung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de) verifizieren.

## Paragrafenkette Kernbereiche Individualarbeitsrecht

- § 611a BGB — Arbeitsvertrag
- § 626 BGB — Außerordentliche Kündigung
- §§ 1 ff. KSchG — Kündigungsschutz; § 4 KSchG — Klagefrist drei Wochen
- § 102 BetrVG — Betriebsratsanhörung
- §§ 1, 3 BUrlG — Urlaubsanspruch; § 7 Abs. 3 BUrlG — Verfall
- § 14 TzBfG — Befristung; § 17 TzBfG — Kontrollklage drei Wochen

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespraechsl..._

# Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Individual- und kollektives Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Individual- und kollektives Arbeitsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Individual- und kollektives Arbeitsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Individual- und kollektives Arbeitsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Kuendigung, Abmahnung, Befristung, Aufhebungsvertrag, Lohn, Urlaub, BR-Sachen
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Kuendigungsschutzklage, Befristungskontrollklage, Zahlungsklage Arbeitsgericht). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Individual- und kollektives Arbeitsrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Individual- und kollektives Arbeitsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- KSchG, TzBfG, BetrVG, BGB, EFZG, BUrlG, AGG, NachwG (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Individual- und kollektives Arbeitsrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Individual- und kollektives Arbeitsrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Hoehe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege moeglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Pruefroutinen.

## Aktuelle Rechtsprechung (Stand Mai 2026)

Im Plugin verifizierte Leitentscheidungen mit offener Quelle (dejure.org / bundesarbeitsgericht.de):

- BAG, 23.10.2025 - 8 AZR 300/24 (Paarvergleich Equal Pay)
- BAG, 03.06.2025 - 9 AZR 104/24 (Mindesturlaub kein Verzicht)
- BAG, 25.03.2026 - 5 AZR 108/25 (Freistellungsklausel unwirksam)
- BAG, 01.04.2026 - 6 AZR 152/22 + 157/22 (Massenentlassung)
- EuGH, 30.10.2025 - C-134/24 + C-402/24 (Massenentlassung)

Weitere Entscheidungen siehe Themenskills. Im Erstgespraech keine Rechtsprechung aus Modellwissen zitieren; bei Bedarf vor Verwendung in dejure.org / openjur.de / bundesarbeitsgericht.de verifizieren.

## Paragrafenkette Fristen Arbeitsrecht

- **§ 4 KSchG** — Klage auf Kündigungsschutz: drei Wochen ab Zugang der schriftlichen Kündigung
- **§ 17 TzBfG** — Befristungskontrollklage: drei Wochen ab vereinbartem Ende
- **§ 15 Abs. 4 AGG** — Geltendmachung AGG-Entschädigung schriftlich innerhalb zwei Monate
- **§ 61b ArbGG** — Klage auf AGG-Entschädigung: drei Monate ab schriftlicher Geltendmachung
- **§ 102 Abs. 2 BetrVG** — Betriebsratsanhörung: eine Woche ordentlich, drei Tage außerordentlich

## Triage — Erstgespräch-Einstieg

1. Liegt eine sofortige Klagefrist vor? (Kündigung → § 4 KSchG, Befristungsende → § 17 TzBfG)
2. GwG-Identifizierung abgeschlossen? (Lichtbildausweis, bei juristischer Person Handelsregister)
3. Interessenkonflikt geprüft? (§ 43a Abs. 4 BRAO)
4. Honorarvereinbarung: RVG oder Stundensatz? Vorschuss anfordern!
5. Welche weiteren Fristen sind aus den vorgelegten Unterlagen erkennbar?

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel: Fachanwalt Erstprüfung und Mandatsziel: systema..._

# Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel.

### Spezial: Fachanwalt Erstprüfung und Mandatsziel

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Fachanwalt Erstprüfung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Einstieg
Wenn ein Mandat vorliegt oder angeboten wird, folgende Punkte klären:

1. **Wer ist der Mandant?** Name, Stellung (Arbeitnehmer, Arbeitgeber, Betriebsrat, Gewerkschaft)?
2. **Was ist das Kernproblem?** Kündigung, Vergütung, Diskriminierung, Betriebsverfassung, Vertragsgestaltung?
3. **Gibt es laufende Fristen?** 3-Wochen-Frist § 4 KSchG, § 17 TzBfG, AGG-Frist § 15 Abs. 4 AGG?
4. **Interessenkonflikt?** Vertritt die Kanzlei oder die Fachanwältin/den Fachanwalt bereits die Gegenseite?
5. **Was ist das Ziel des Mandanten?** Bestandsschutz, Abfindung, Schadensersatz, Vertragsänderung?

## Phase 1: Interessenkonflikt-Prüfung (§ 43a BRAO, § 3 BORA)

### Prüfpflicht
Vor jeder Mandatsannahme muss geprüft werden:
- Vertritt die Kanzlei die Gegenseite in derselben oder einer verwandten Angelegenheit?
- Hat ein Anwalt der Kanzlei früher die Gegenseite beraten?
- Gibt es sonstige Interessenkollisionen (Eigeninteressen, familiäre Verbindungen)?

**Rechtsfolge Verstoß:** § 356 StGB (Parteiverrat); berufsrechtliche Sanktionen; Anwaltsvertrag nichtig.

### Dokumentation
Interessenkonflikt-Check in der Kanzleisoftware; schriftliche Bestätigung der Prüfung in der Akte.

## Phase 2: Sachverhaltsaufnahme

### Grunddaten

| Feld | Inhalt |
|---|---|
| Mandantenname | |
| Arbeitgeber/Arbeitnehmer | |
| Betriebsname und -ort | |
| Branche | |
| Betriebsgröße (ca.) | |
| Beginn Arbeitsverhältnis | |
| Letzte Vergütung (brutto) | |
| Besonderer Kündigungsschutz? | |
| Besteht Betriebsrat? | |
| Kündigung erhalten? Datum? | |

### Fristenüberblick (sofort beim Erstgespräch)
- Liegt eine Kündigung vor? → § 4 KSchG-Frist berechnen
- Ist das Befristungsende abgelaufen? → § 17 TzBfG-Frist
- Diskriminierungsfall? → § 15 Abs. 4 AGG-Frist (2 Monate)

## Phase 3: Mandatsziel und Interessenlage

### Mandatsziel klären — vier Grundoptionen

| Option | Beschreibung | Typisch wenn |
|---|---|---|
| Bestandsschutz | Fortsetzung des Arbeitsverhältnisses erzwingen | Mandant will unbedingt weiterarbeiten |
| Abfindung | Hohe Abfindung aushandeln; schnelle Einigung | Neue Stelle in Aussicht; wirtschaftliches Interesse |
| Beides prüfen lassen | Strategie offen halten; im Gütermin entscheiden | Lage noch unklar |
| Schadensersatz/Entschädigung | AGG-Ansprüche, EntgTranspG, sonstige Ansprüche | Diskriminierung, Mobbing, verweigerte Gehaltserhöhung |

### Fragen zur Interessenlage
- Will der Mandant nach Verfahrensabschluss im Betrieb bleiben, oder lieber weg?
- Wie ist die finanzielle Situation? Kann er/sie sich eine Prozessdauer von 6–18 Monaten leisten?
- Besteht Rechtschutzversicherung? (Falls ja: Deckungsanfrage stellen)
- Wie ist das Verhältnis zum Arbeitgeber/Vorgesetzten — sachlich oder eskaliert?

## Phase 4: Erste Risikoampel

### Grün — Starke Position
- Formfehler bei der Kündigung (kein Original, fehlende Vollmacht, keine BR-Anhörung)
- Sonderkündigungsschutz (Schwangerschaft, Elternzeit, Betriebsrat) ohne behördliche Zustimmung
- Massenentlassungsanzeige fehlerhaft (post-BAG 6 AZR 152/22)
- Befristungsabrede nicht schriftlich oder nach Dienstantritt unterzeichnet

### Gelb — Mittlere Lage
- KSchG anwendbar; Kündigung hat Angriffspunkte, aber Ausgang unsicher
- Sozialauswahl ist anfechtbar, aber dokumentiert
- Sachgrundbefristung ist schwach, aber nicht offensichtlich unwirksam

### Rot — Schwache Position
- KSchG nicht anwendbar (Betriebsgröße unter Schwelle, kurze Betriebszugehörigkeit)
- Kündigung formal korrekt; Kündigungsgrund stark (schweres Fehlverhalten mit Beweisen)
- Klagefrist bereits abgelaufen; § 7 KSchG-Fiktion

## Phase 5: Mandatsumfang und Kostenhinweis

### RVG-Werte im Arbeitsrecht
- Streitwert Kündigungsschutzklage: § 42 Abs. 2 GKG = 1 Vierteljahresverdienst
- Abfindungsvergleich: Streitwert kann höher sein (abhängig von Vergleichswert)
- Beratungsgebühr: nach RVG § 34 frei vereinbar oder nach Stundensatz

### Kostenhinweis-Pflicht (§ 49b BRAO, § 3a RVG)
Vor Mandatsannahme: Hinweis auf voraussichtliche Kosten; Vergütungsvereinbarung schriftlich wenn von RVG-Sätzen abgewichen wird.

### Rechtsschutzversicherung
Falls RSV vorhanden: Deckungsanfrage sofort stellen; RSV-Selbstbehalt klären; RSV kann Vergleich beeinflussen (häufig RSV-Limit für Vergleichsabfindung).

## Anschluss-Skills
- `ar-einfuehrung-mandantenanliegen` für Themen-Routing nach Erstprüfung
- `ar-kuendigungspruefung-workflow` wenn Kündigung das Kernproblem ist
- `workflow-kaltstart-und-routing` für weiteres Routing.
- Keine Steuerberatung zur steuerlichen Behandlung von Abfindungen.

---

## Skill: `output-waehlen`

_Output-Wahl für Fachanwalt Arbeitsrecht: stimmt Adressat (Arbeitnehmer, Arbeitgeber, Betriebsrat), Frist (§ 4 KSchG 3 Wochen Kündigungsschutzklage) und Form auf den Zweck ab — typische Outputs: Kündigungsschutzklage, Aufhebungsvertrag-Markup, Vergleichsvorschlag._

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Fachanwalt Arbeitsrecht** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `abmahnung-loeschung-personalakte-bag-2-azr-782-11` — Abmahnung Loeschung Personalakte BAG 2 AZR 782 11
- `aktenzeichen-fehlerkatalog` — Aktenzeichen Fehlerkatalog
- `ar-aufhebungsvertrag-praxis` — AR Aufhebungsvertrag Konkurrenzklausel
- `ar-betriebsuebergang-spezial` — AR Betriebsuebergang Spezial Einfuehrung
- `einstieg-schnelltriage-fallrouting` — AR Kuendigungspruefung Fazugang Arbeitgeber
- `vergleich-arbeitsgericht-abrechnung` — Arbeitsgericht Abrechnung
- `aufhebungsvertrag-faires-verhandeln-bag-6-azr-333-21` — Aufhebungsvertrag Faires Verhandeln BAG 6 AZR 333 21
- `bag-mindesturlaub-kein-verzicht` — BAG
- `befristung-compliance-dokumentation-und-akte` — Befristung FAO Unwirksam Fristennotiz
- `befristung-tzbfg` — Befristung Tzbfg BEM Verfahren Fazugang
- `beteiligung-betriebsrat-102-betrvg` — Beteiligung Betriebsrat Erstgespraech
- `betriebsrat-zahlen-schwellen-und-berechnung` — Betriebsrat BETRVG Datum
- `betriebsratswahl-anfechtung-leiharbeit-bag-7-abr-4-21` — Betriebsratswahl Anfechtung Leiharbeit BAG 7 ABR 4 21
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Fachanwalt Arbeitsrecht (AGG, BetrVG, EntgTranspG, KSchG, TzBfG) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `ar-abfindungs-rechner-modular`

_Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG: Abfindungsrechner modular: Faustformel 0 und5 Monatsg..._

# Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG. Beispielrechnung und Mustertext für Aufhebungsvertrag und Vergleich.

### AR: Abfindungs-Rechner (modular)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AR: Abfindungs-Rechner (modular)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollständige Mandantenberatung oder steuerliche Beratung.
- Keine Festlegung ohne ausdrückliche Mandantenentscheidung.
- Keine Spekulation über individuelle BA-Entscheidungen zur Sperrzeit.

---

## Skill: `ar-aufhebungsvertrag-praxis`

_Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG, AGB-Kontrolle von Klauseln §§ 305 ff: Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG, AGB-Kontrolle..._

# Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG, AGB-Kontrolle von Klauseln §§ 305 ff


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG, AGB-Kontrolle von Klauseln §§ 305 ff. BGB, Widerrufsrecht, Verzicht auf KSchG-Klage, Klauselrisiken. Prüfraster für Verhandlung und Mandantenleitfaden.

### AR: Aufhebungsvertrag in der Praxis

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AR: Aufhebungsvertrag in der Praxis` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Einstieg
Wenn Vertragsentwurf vorliegt, diesen zuerst auswerten. Minimalfragen für die erste Weiche:

1. **Initiative:** Wer hat die Beendigung vorgeschlagen — Arbeitgeber oder Arbeitnehmer? (Sperrzeitrelevanz)
2. **Wirtschaftliche Eckdaten:** Brutto-Monatslohn, Beschäftigungsdauer, Alter, Unterhaltspflichten, voraussichtliche Bezugsdauer ALG I.
3. **Abfindungsbetrag und -fälligkeit:** Liegt ein konkretes Angebot vor? Entspricht es der Faustformel oder weicht es ab?
4. **Kündigungsrisiko:** Hätte eine Kündigung Bestand gehabt? Welche Angriffspunkte (BR-Anhörung, Sozialauswahl, Massenentlassung) gibt es?
5. **Klauselinhalt:** Welche Klauseln enthält der Entwurf (Ausgleichsklausel, Zeugnisnote, Wettbewerbsverbot, Geheimhaltung, Freistellung)?

## Rechtliche Grundstruktur

### Vertragscharakter
Der Aufhebungsvertrag ist ein privatrechtlicher Auflösungsvertrag nach §§ 311, 241 BGB; er bedarf der Schriftform analog § 623 BGB (str., aber h.M. und risikoarme Praxis). Formfehler → Nichtigkeit nach § 125 BGB.

### AGB-Kontrolle §§ 305–310 BGB
Arbeitgeberformulare unterliegen der Inhaltskontrolle nach § 307 BGB. Typische unwirksame Klauseln:
- Pauschale „Abgeltung aller gegenseitigen Ansprüche" ohne Auflistung, wenn Restlöhne unklar sind
- Rückzahlungsklauseln für Fortbildungskosten ohne angemessene Staffelung (BAG-Linie)
- Wettbewerbsverbote ohne Karenzentschädigungsregelung (§§ 74 ff. HGB analog)
- Verfallklauseln, die laufende Ansprüche rückwirkend vernichten

### Widerrufsrecht
Kein gesetzliches Widerrufsrecht beim Aufhebungsvertrag im Arbeitsverhältnis. Eine kurze Bedenkzeit (mind. 1 Woche, besser schriftlich vereinbart) empfiehlt sich zur Vermeidung von Arglistanfechtung. Bei Abschluss „unter Druck" → Anfechtung nach § 123 BGB prüfen.

## Sperrzeitrisiko § 159 SGB III

### Kernregel
Wer das Arbeitsverhältnis selbst beendet oder durch vertragswidriges Verhalten Anlass zur Kündigung gegeben hat, riskiert eine Sperrzeit von bis zu 12 Wochen.

### Sperrzeitbefreiung
Die Bundesagentur für Arbeit prüft eigenständig, ob ein wichtiger Grund vorlag. Anerkannte Gründe in der BA-Praxis:
- Betriebsbedingte Kündigung war konkret drohend und Aufhebungsvertrag war das wirtschaftlich bessere Ergebnis
- Gesundheitliche oder familiäre Gründe (dokumentiert)
- Mobbing oder unzumutbare Arbeitsbedingungen (nachgewiesen)

**Formulierungsregel im Vertrag:** Aufhebungsvertrag auf Initiative des Arbeitgebers klar dokumentieren; „Einvernehmlichkeit" ohne Ursachenbenennung ist gefährlich.

### Ruhenszeitraum § 158 SGB III
Zahlt der Arbeitgeber eine Abfindung und wird die ordentliche Kündigungsfrist nicht eingehalten oder unterschritten, ruht der ALG-I-Anspruch für einen errechneten Zeitraum. Faustregel: Abfindung ÷ täglichem Bemessungsentgelt = Ruhetage (vereinfacht).

**Quellenregel:** Dienstanweisungen der BA und aktuelle Merkblätter live prüfen auf bundesagentur.de; keine modellwissensbasierten Rechenformeln ohne aktuellen Quellenbeleg.

## Klauselprüfung — Checkliste

| Klausel | Risiko | Empfehlung |
|---|---|---|
| Ausgleichsklausel „alle Ansprüche" | Erfasst unbewusst noch offene Lohnforderungen, Urlaubsabgeltung | Explizite Ausnahmen benennen |
| Zeugnisnote | Schlechtere Note als bisher faktisch ausgegeben → Anfechtungsansatz | „gut"-Note mindestens Zielvereinbarung, besser schriftlich fixieren |
| Freistellungsklausel | Pauschale Klausel unwirksam (BAG 5 AZR 108/25) | Anlassbezogen formulieren, Vergütungsfortzahlung klar regeln |
| Rückzahlungsklausel Fortbildung | Ohne Staffelung unwirksam (BAG-Linie) | Gestaffelte Rückzahlungspflicht nach Verbleibdauer |
| Wettbewerbsverbot | Ohne Karenzentschädigung nichtig (§ 74 Abs. 2 HGB analog) | Karenzentschädigung ≥ 50 % der letzten Vergütung vereinbaren |
| Geheimhaltungsklausel | Zu weit → AGB-Kontrolle; Whistleblowing nach HinSchG nicht ausschließbar | Auf Geschäftsgeheimnisse i.S.d. GeschGehG begrenzen |

## Mandantenleitfaden: Entscheidungsmatrix

| Szenario | Empfehlung |
|---|---|
| Kündigung ist wahrscheinlich unwirksam, Mandant will Bestandsschutz | Aufhebungsvertrag ablehnen; Klage einlegen |
| Kündigung hat geringe Angriffspunkte, Mandant will schnell Abfindung | Aufhebungsvertrag verhandeln; Sperrzeitgestaltung sorgfältig |
| Mandant will möglichst hohe Abfindung | Klage einlegen; Gütermin als Verhandlungsplattform nutzen |
| Mandant hat dringende Anschlussbeschäftigung | Freistellungszeit verhandeln; Beendigungsdatum flexibel halten |

## Prüfschema Aufhebungsvertrag

1. **Schriftform** (§ 623 BGB analog) gewahrt?
2. **Anfechtungsrisiken:** Druck, Täuschung, unzureichende Bedenkzeit?
3. **AGB-Kontrolle:** Wer hat formuliert? Klauseln nach § 307 BGB prüfen.
4. **Abfindungsbetrag:** Angemessen im Verhältnis zum Kündigungsrisiko?
5. **Sperrzeitgestaltung:** Initiative, Formulierung, Beratungsprotokoll?
6. **Steuer:** Fünftelregelung § 34 EStG; Brutto- oder Nettovereinbarung?
7. **Zeugnis:** Inhalt, Note, Ausstellungsfrist vereinbart?
8. **Offene Ansprüche:** Überstunden, Urlaubsabgeltung, Boni, variable Vergütung explizit geregelt?
9. **Vollständigkeitsklausel:** Welche Ansprüche sind wirklich erfasst?

## Anschluss-Skills
- `ar-abfindungs-rechner-modular` für Rechenlogik und Verhandlungsformel
- `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` für vertiefte Sperrzeitprüfung
- `fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg` für Verhandlungsstrategie im Gütermin
- `spezial-freistellungsklausel-sonderfall-und-edge-case` für Klauselprüfung

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für vollständige Mandantenberatung oder steuerliche Beratung.
- Keine Festlegung ohne ausdrückliche Mandantenentscheidung.
- Keine individuelle Prognose zur BA-Sperrzeitentscheidung ohne aktuellen Quellenbeleg.

## Aktuelle BAG-Linie 2025/2026 (live verifizieren vor Schriftsatzverwendung)

Drei aktuelle Leitentscheidungen, die ueber das Arbeitsrecht in den letzten zwoelf Monaten besonders weit ausstrahlen:

| Entscheidung | Tragende Aussage | Skill-Vertiefung |
| --- | --- | --- |
| **BAG, Urt. v. 23.10.2025 - 8 AZR 300/24** | **Equal Pay - Paarvergleich genuegt.** Eine einzige besser bezahlte Vergleichsperson des anderen Geschlechts mit gleicher oder gleichwertiger Arbeit reicht, um die Vermutung des $ 22 AGG auszuloesen. Der Arbeitgeber muss konkret darlegen, dass die Differenz ausschliesslich auf objektiven, geschlechtsneutralen Gruenden beruht. Pauschale Hinweise auf Medianwerte, Durchschnittsbetrachtungen oder Verhandlungsgeschick reichen nicht. Art. 157 AEUV bekommt damit Schaerfe. | `bag-equal-pay-paarvergleich` (fachanwalt-arbeitsrecht) / `bag-equal-pay-paarvergleich-8azr30024` (arbeitsrecht) |
| **BAG, Urt. v. 03.06.2025 - 9 AZR 104/24** | **Kein Verzicht auf gesetzlichen Mindesturlaub.** Im bestehenden Arbeitsverhaeltnis koennen Arbeitnehmer:innen auf den gesetzlichen Mindesturlaub nicht wirksam verzichten - auch nicht durch gerichtlichen Vergleich. Gilt selbst dann, wenn die Beendigung bereits feststeht und absehbar ist, dass der Urlaub krankheitsbedingt nicht mehr genommen werden kann. Ausgleichs-/Erledigungs-/Abgeltungsklauseln muessen sauber zwischen gesetzlichem Mindesturlaub, vertraglichem Mehrurlaub und bereits entstandener Urlaubsabgeltung unterscheiden. | `bag-mindesturlaub-kein-verzicht` (fachanwalt-arbeitsrecht) / `bag-mindesturlaub-kein-verzicht-9azr10424` (arbeitsrecht) |
| **BAG, Urt. v. 25.03.2026 - 5 AZR 108/25** | **Pauschale Freistellungsklauseln in Arbeitsvertragsformularen unwirksam.** Eine formularmaessige Freistellungsklausel, die dem Arbeitgeber das einseitige Recht gibt, Beschaeftigte nach Kuendigung unter Fortzahlung der Verguetung freizustellen, ist nach AGB-Kontrolle unwirksam, wenn sie Arbeitnehmer:innen unangemessen benachteiligt. Freistellung bleibt im konkreten Fall moeglich - braucht aber einen tragfaehigen Grund (ueberwiegende schutzwuerdige Arbeitgeberinteressen). Die pauschale Vorratsklausel reicht nicht. | `bag-freistellungsklausel-unwirksam` (fachanwalt-arbeitsrecht) / `bag-freistellungsklausel-unwirksam-5azr10825` (arbeitsrecht) |

> Diese drei Aktenzeichen sind Sucheinstieg. Vor Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (bundesarbeitsgericht.de, dejure.org) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung. Spezial-Skills oben enthalten Pruefschemata, Klagebausteine und Verteidigungsmuster.

---

## Skill: `ar-einfuehrung-mandantenanliegen`

_Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Befristung, Maßregelungsverbot, Diskriminierung AGG, Lohn, Urlaub, BR-Mitbestimmung: Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Be..._

# Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Befristung, Maßregelungsverbot, Diskriminierung AGG, Lohn, Urlaub, BR-Mitbestimmung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Befristung, Maßregelungsverbot, Diskriminierung AGG, Lohn, Urlaub, BR-Mitbestimmung. Routing in Fachmodule. Erstgesprächs-Checkliste.

### AR: Einführung — Typische Mandantenanliegen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AR: Einführung — Typische Mandantenanliegen` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Kaltstart — Erste Weichen
Wenn Unterlagen (Kündigung, Vertrag, Zeugnis, Bescheid) vorliegen, diese zuerst auswerten.

1. **Was ist das Kernproblem?** (s. Anliegen-Klassifikation unten)
2. **Wie ist die Frist?** Gibt es eine laufende 3-Wochen-Klagefrist (§ 4 KSchG) oder AGG-Frist (§ 15 Abs. 4 AGG: 2 Monate)?
3. **Wer ist der Mandant?** Arbeitnehmer oder Arbeitgeber?
4. **Was ist das Ziel?** Bestandsschutz, Abfindung, Schadensersatz, Verhaltensänderung, Dokumentation?

## Anliegen-Klassifikation und Erstrouting

### 1. Kündigung
- **Einschlägig:** §§ 1, 4, 7, 23 KSchG; § 623 BGB (Schriftform); § 102 BetrVG (BR-Anhörung)
- **Kritische Frist:** 3 Wochen ab Zugang der schriftlichen Kündigung (§ 4 KSchG) — Versäumnis = § 7 KSchG-Fiktion
- **Sofortmaßnahme:** Zugangsdatum sichern, Schriftform prüfen, KSchG-Anwendbarkeit prüfen (§ 23 KSchG > 10 VZÄ, § 1 KSchG > 6 Monate), Betriebsratsprotokolle anfordern
- **Routing:** → `fachanwalt-arbeitsrecht-kuendigungsschutzklage`

### 2. Abfindung
- **Einschlägig:** §§ 9, 10 KSchG (Auflösungsantrag); § 1a KSchG (Klageverzicht); BAG-Faustformel 0,5 × Monatsgehalt × Beschäftigungsjahre
- **Sperrzeit:** § 159 SGB III bei Aufhebungsvertrag auf Arbeitnehmerinitiative
- **Routing:** → `ar-abfindungs-rechner-modular`, `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit`

### 3. Zeugnis
- **Einschlägig:** § 109 GewO (Anspruch auf qualifiziertes Zeugnis); Wohlwollenspflicht des Arbeitgebers (BAG-Linie); Zeugnisformulierungen (Codierungen)
- **Ansprüche:** Berichtigungs- oder Benotungsklage vor Arbeitsgericht; kurze Verjährungsfrist beachten
- **Routing:** Individuell nach Zeugnisinhalt; ggf. `workflow-redteam-qualitygate`

### 4. Befristung
- **Einschlägig:** §§ 14–22 TzBfG; § 17 TzBfG (3-Wochen-Entfristungsklage!); BAG zu sachgrundloser Befristung (§ 14 Abs. 2 TzBfG: max. 2 Jahre, max. 3 Verlängerungen)
- **Kritische Frist:** 3 Wochen nach vereinbartem Ende (§ 17 TzBfG) für Entfristungsklage
- **Routing:** → `fachanwalt-arbeitsrecht-befristung-tzbfg`

### 5. Maßregelungsverbot § 612a BGB
- **Einschlägig:** § 612a BGB; Beweislastverteilung; enger Zusammenhang zwischen rechtmäßiger Ausübung von Rechten und Benachteiligung
- **Typische Fälle:** Kündigung nach Klage auf Mindestlohn, Kündigung nach Betriebsratsgründungsversuch, Kündigung nach Krankmeldung
- **Routing:** Sachverhaltsabhängig; ggf. kombiniert mit `fachanwalt-arbeitsrecht-kuendigungsschutzklage`

### 6. Diskriminierung AGG
- **Einschlägig:** §§ 1–22 AGG; § 22 AGG (Beweislastumkehr bei Indizien); § 15 AGG (Schadensersatz, Entschädigung)
- **Kritische Frist:** § 15 Abs. 4 AGG: 2 Monate ab Kenntnis der Benachteiligung (Ausschlussfrist!)
- **Merkmale:** Rasse, Herkunft, Geschlecht, Religion, Behinderung, Alter, sexuelle Identität
- **Routing:** Sachverhaltsabhängig; ggf. `spezial-entgtranspg-verhandlung-vergleich-und-eskalation` bei Entgeltdiskriminierung

### 7. Lohn / Vergütung
- **Einschlägig:** §§ 611a, 614, 615 BGB; MiLoG (Mindestlohn, aktuellen Satz live prüfen); Annahmeverzug § 615 BGB; Ausschlussfristen im Arbeitsvertrag prüfen
- **Typische Streitpunkte:** Nicht bezahlte Überstunden (Nachweis!), Provision, Boni, variable Vergütung, Mindestlohn-Unterschreitung
- **Routing:** Sachverhaltsabhängig; bei Tarifbindung → Tarifvertrag live prüfen

### 8. Urlaub
- **Einschlägig:** §§ 1–13 BUrlG; § 7 BUrlG (Übertragung, Verfall); BAG: kein Verfall ohne Hinweis des Arbeitgebers (EuGH-Konformität); Urlaubsabgeltung § 7 Abs. 4 BUrlG; BAG 9 AZR 104/24: kein Urlaubsverzicht durch Prozessvergleich
- **Routing:** → `spezial-urlaub-livequellen-und-rechtsprechungscheck`

### 9. Betriebsrat und Mitbestimmung
- **Einschlägig:** BetrVG §§ 87 (echtes Mitbestimmungsrecht), 99 (personelle Einzelmaßnahmen), 102 (Anhörung Kündigung), 111 ff. (Betriebsänderung, Interessenausgleich, Sozialplan)
- **Typische Mandate:** BR-Beschlüsse anfechten, Zustimmungsverweigerung bei Einstellung, Einigungsstelle, Unterlassungsanspruch
- **Routing:** → `fachanwalt-arbeitsrecht-betriebsratsanhoerung`, `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung`

## Erstgesprächs-Checkliste

- [ ] Vollständige Personalien und Kontaktdaten
- [ ] Arbeitgeberbezeichnung, Betriebsgröße (ca. Mitarbeiterzahl)
- [ ] Beginn des Arbeitsverhältnisses
- [ ] Letzte Bruttovergütung
- [ ] Liegt eine schriftliche Kündigung oder ein sonstiger Auslöser vor?
- [ ] Genaues Datum des Zugangs/Ereignisses (Fristberechnung!)
- [ ] Welches Ziel hat der Mandant? (Bestandsschutz, Abfindung, Schadensersatz)
- [ ] Gibt es einen Betriebsrat?
- [ ] Sonderkündigungsschutz? (Schwangerschaft, Elternzeit, Schwerbehinderung, BR-Mandat)
- [ ] Welche Unterlagen liegen vor?

## Fristenüberblick (kritisch)

| Frist | Norm | Konsequenz bei Versäumnis |
|---|---|---|
| 3 Wochen Kündigungsschutzklage | § 4 KSchG | § 7 KSchG-Fiktion: Kündigung gilt als wirksam |
| 3 Wochen Entfristungsklage | § 17 TzBfG | Befristung gilt als wirksam |
| 2 Monate AGG-Geltendmachung | § 15 Abs. 4 AGG | Anspruchsverlust |
| Ausschlussfristen Vertrag/TV | Je nach Klausel | Anspruchsverlust |
| 2 Wochen außerordentliche Kündigung | § 626 Abs. 2 BGB | Fristablauf für Arbeitgeber |

## Anschluss-Skills
Alle Fachmodule des Plugins stehen für die jeweiligen Themen bereit. Nach Klassifikation direkt in den passenden Skill wechseln und dort die fachliche Tiefe aktivieren.

## Was dieser Arbeitsgang nicht macht
- Keine Tiefenprüfung; dieser Skill ist der Eingangsrouter, nicht die Fachbearbeitung.
- Keine Festlegung des Mandanten ohne ausdrückliche Entscheidung.

---

## Skill: `ar-konkurrenzklausel-spezial`

_Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB analog: Karenzentschädigung ≥ 50 %, Schriftform, Verbindlichkeit, Freistellung durch Arbeitgeber, Verwirkung, Verstoß und Vertragsstrafe: Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB analog: Karenzentsc..._

# Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB analog: Karenzentschädigung ≥ 50 %, Schriftform, Verbindlichkeit, Freistellung durch Arbeitgeber, Verwirkung, Verstoß und Vertragsstrafe


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB analog: Karenzentschädigung ≥ 50 %, Schriftform, Verbindlichkeit, Freistellung durch Arbeitgeber, Verwirkung, Verstoß und Vertragsstrafe. Prüfraster und Musterklausel.

### AR: Konkurrenzklausel / Nachvertragliches Wettbewerbsverbot (Spezial)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AR: Konkurrenzklausel / Nachvertragliches Wettbewerbsverbot (Spezial)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Einstieg
Wenn Vertragsklausel vorliegt, diese zuerst auswerten. Minimalfragen:

1. **Was liegt vor?** Wettbewerbsverbot im Arbeitsvertrag oder separate Vereinbarung? Zeitraum und räumlicher Umfang?
2. **Karenzentschädigungsregelung?** Ist eine Entschädigung vereinbart? Beträgt sie mindestens 50 % der zuletzt bezogenen vertraglichen Leistungen?
3. **Rolle des Mandanten:** Arbeitnehmer (Wirksamkeitsprüfung, Anspruch auf Entschädigung) oder Arbeitgeber (Freistellung, Durchsetzung, Unterlassung)?
4. **Aktueller Stand:** Arbeitsverhältnis beendet? Aufnahme neuer Tätigkeit bereits erfolgt?
5. **Schriftform:** Ist die Klausel schriftlich vereinbart und vom Arbeitgeber unterzeichnet? (§ 74 Abs. 1 HGB)

## Rechtsrahmen §§ 74–75d HGB (analog für Angestellte)

### Anwendung auf Arbeitnehmer
Die §§ 74 ff. HGB gelten unmittelbar für Handlungsgehilfen (§ 59 HGB) und entsprechend für alle Arbeitnehmer. Im Arbeitsverhältnis sind die Vorschriften als zwingendes Mindestrecht anzusehen.

### Wirksamkeitsvoraussetzungen

| Voraussetzung | Norm | Folge bei Fehlen |
|---|---|---|
| Schriftliche Vereinbarung mit Arbeitgebersignatur | § 74 Abs. 1 HGB | Nichtigkeit der Klausel |
| Karenzentschädigung ≥ 50 % der letzten Vergütung | § 74 Abs. 2 HGB | Unverbindlichkeit (§ 74a Abs. 1 HGB) |
| Berechtigtes Interesse des Arbeitgebers | § 74a Abs. 1 HGB | Unverbindlichkeit |
| Max. 2 Jahre Dauer | § 74a Abs. 1 HGB | Unverbindlichkeit für die überschießende Zeit |
| Aushändigung einer Ausfertigungsurkunde | § 74 Abs. 1 HGB | Unverbindlichkeit |

### Unverbindlich vs. Nichtig
- **Nichtig:** Kein Anspruch auf Entschädigung; Arbeitnehmer muss sich nicht daran halten
- **Unverbindlich:** Arbeitnehmer kann wählen: sich binden (und Entschädigung verlangen) oder sich lösen

## Karenzentschädigung — Berechnung

### Bezugsgröße
50 % der zuletzt bezogenen vertragsmäßigen Leistungen (§ 74 Abs. 2 HGB), also:
- Grundgehalt (Durchschnitt der letzten 12 Monate)
- Regelmäßige Provisionen und Prämien
- Geldwerte Sonderleistungen (Dienstwagen zur privaten Nutzung, Zuschüsse)
- Nicht: unregelmäßige Sonderzahlungen, einmalige Boni

### Anrechnung anderweitigen Erwerbs § 74c HGB
Anderweitiger Verdienst wird angerechnet, soweit die Summe aus Entschädigung und Erwerb 110 % des letzten Gehalts übersteigt. Arbeitnehmer muss anderweitigen Erwerb mitteilen.

### Musterberechnung
```
Letztes Brutto-Monatsgehalt: 4.000 €
Zuletzt bezogene Provision (Ø): + 500 €
Maßgebliche Vergütung: 4.500 €/Monat
Karenzentschädigung (50 %): 2.250 €/Monat
Deckungsgrenze (110 %): 4.950 €/Monat
Neuer Verdienst: 3.500 €/Monat
Anrechnung (3.500 + 2.250 = 5.750 > 4.950): 800 € werden angerechnet
Effektive Entschädigung: 1.450 €/Monat
```

## Freistellung durch Arbeitgeber

### Freistellungsrecht § 75a HGB
Der Arbeitgeber kann den Arbeitnehmer vor Beendigung des Arbeitsverhältnisses schriftlich vom Wettbewerbsverbot freistellen. Dann:
- Kein Entschädigungsanspruch ab dem Zeitpunkt der Freistellung
- Ausnahme: Freistellung in der Absicht, den Arbeitnehmer in seiner wirtschaftlichen Freiheit zu schädigen (treuwidrig)

### Freistellungserklärung nach Vertragsende
Nicht möglich; das Wettbewerbsverbot entsteht mit der Beendigung des Arbeitsverhältnisses.

## Verstoß und Rechtsfolgen

### Arbeitgeber-Seite
- Unterlassungsanspruch + Schadensersatz (§§ 74b, 280 BGB)
- Vertragsstrafe, wenn vereinbart (AGB-Kontrolle beachten: Höhe muss angemessen sein)
- Einstweilige Verfügung beim Arbeitsgericht

### Arbeitnehmer-Seite bei Verstoß
- Verlust des Entschädigungsanspruchs für die Zeit des Verstoßes
- Schadensersatzpflicht; bei Vereinbarung einer Vertragsstrafe diese als Mindestsatz

### AGB-Kontrolle Vertragsstrafe
Klauseln mit Vertragsstrafe unterliegen § 307 BGB. Unangemessen hoch → Reduzierung auf das zulässige Maß (nicht Nichtigkeit im Arbeitsrecht, da § 343 BGB-Kontrolle durch Gericht).

## Prüfschema Konkurrenzklausel

1. Schriftform und Aushändigung gewahrt? (§ 74 Abs. 1 HGB)
2. Karenzentschädigung vereinbart? Mindestens 50 %?
3. Dauer max. 2 Jahre?
4. Berechtigtes Interesse des Arbeitgebers erkennbar? (§ 74a Abs. 1 HGB)
5. Ergebnis: Nichtig / Unverbindlich / Verbindlich?
6. Wenn verbindlich: Anrechnungsberechnung nach § 74c HGB
7. Wenn Verstoß behauptet: Beweis des Verstoßes, Schadensberechnung, Vertragsstrafe

## Muster: Freistellungserklärung (Kurzform)
> „Die [Arbeitgeberin] erklärt hiermit, die [Arbeitnehmerin / den Arbeitnehmer] mit sofortiger Wirkung von dem im Arbeitsvertrag vom [Datum] vereinbarten nachvertraglichen Wettbewerbsverbot freizustellen. Die Pflicht zur Zahlung der Karenzentschädigung entfällt ab dem [Datum] der Zustellung dieser Erklärung."

## Anschluss-Skills
- `ar-aufhebungsvertrag-praxis` wenn das Wettbewerbsverbot in einen Aufhebungsvertrag eingebettet ist
- `spezial-freistellungsklausel-sonderfall-und-edge-case` für Freistellungsklausel und AGB-Prüfung
- `workflow-redteam-qualitygate` für kritische Klauselprüfung

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für vollständige Mandantenberatung.
- Keine individuelle Steuerberatung zur Versteuerung der Karenzentschädigung.
- Keine Aussage über gewerblichen Rechtsschutz oder Betriebsgeheimnis (§§ 1 ff. GeschGehG) ohne separaten Prüfauftrag.

---

## Skill: `befristung-compliance-dokumentation-und-akte`

_Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbefristung-Dokumentation, Anschlussverbot § 14 Abs: Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbef..._

# Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbefristung-Dokumentation, Anschlussverbot § 14 Abs


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbefristung-Dokumentation, Anschlussverbot § 14 Abs. 2 Satz 2 TzBfG, Kettenbefristung, Entfristungsklage-Frist § 17 TzBfG.

### Spezial: Befristung — Compliance, Dokumentation und Akte

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Befristung — Compliance, Dokumentation und Akte` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Einstieg
Wenn ein befristeter Arbeitsvertrag oder eine Verlängerungsvereinbarung vorliegt, zuerst prüfen:

1. **Schriftform:** Befristungsabrede schriftlich vereinbart und vor Dienstantritt unterzeichnet?
2. **Sachgrund oder ohne Sachgrund?** § 14 Abs. 1 (mit Sachgrund) oder § 14 Abs. 2 (sachgrundlos)?
3. **Vorbeschäftigung:** War der Arbeitnehmer schon früher beim gleichen Arbeitgeber beschäftigt?
4. **Laufzeit und Verlängerungen:** Wie oft und wie lange wurde befristet?
5. **Klagefrist:** Ist das Arbeitsverhältnis bereits beendet? Wenn ja: 3-Wochen-Frist § 17 TzBfG?

## § 14 Abs. 4 TzBfG — Schriftform als Wirksamkeitsvoraussetzung

### Grundregel
Die Befristung eines Arbeitsvertrages bedarf zu ihrer Wirksamkeit der Schriftform (§ 14 Abs. 4 TzBfG i.V.m. § 126 BGB). Die Befristungsabrede muss schriftlich vereinbart sein, bevor der Arbeitnehmer seine Arbeit aufnimmt.

### Kritische Praxis-Fehler
- **Fehler 1:** Schriftlicher Vertrag wird dem Arbeitnehmer nach Arbeitsbeginn zugesandt — dann ist die Befristungsabrede unwirksam, obwohl der Vertrag schriftlich ist.
- **Fehler 2:** Verlängerungsvereinbarung erst nach Ablauf der bisherigen Befristung unterzeichnet — dann ist die Verlängerung eine Neubefristung ohne Schriftform.
- **Fehler 3:** Nur der Arbeitgeber unterzeichnet; Arbeitnehmer unterschreibt später — dann liegt kein Vertragsschluss vor Dienstantritt vor.

### Dokumentations-Checkliste Schriftform
- [ ] Befristungsabrede im Vertrag eindeutig bezeichnet?
- [ ] Vertragsschluss (beidseitige Unterschrift) vor Aufnahme der Tätigkeit?
- [ ] Bei Verlängerung: neue Vereinbarung vor Ablauf des alten Vertrages?
- [ ] Kopie des unterzeichneten Vertrages in der Akte?

## § 14 Abs. 1 TzBfG — Sachgrundbefristung

### Zulässige Sachgründe (nicht abschließend)
1. Vorübergehender betrieblicher Bedarf
2. Anschluss an eine Ausbildung oder ein Studium
3. Beschäftigung zur Vertretung (Vertretungsbefristung)
4. Eigenart der Arbeitsleistung (z.B. Saisonarbeit)
5. Erprobung
6. Gründe in der Person des Arbeitnehmers (z.B. eigener Wunsch)
7. Haushaltsmittelfinanzierung (öffentlicher Dienst)
8. Gerichtlicher Vergleich

### Dokumentationsanforderungen je Sachgrund

**Vertretungsbefristung (§ 14 Abs. 1 Nr. 3 TzBfG):**
- Vertretener Arbeitnehmer und Grund für dessen Abwesenheit im Vertrag oder in der Personalakte dokumentieren
- BAG-Linie: Indirekte Vertretung ist zulässig (organisatorischer Zusammenhang genügt), aber der Zusammenhang muss nachvollziehbar sein
- Kettenbefristungen bei Vertretungen: Ab einer gewissen Anzahl und Dauer kann das BAG missbräuchliche Gestaltung annehmen (live prüfen)

**Erprobung (§ 14 Abs. 1 Nr. 5 TzBfG):**
- Maximal 6 Monate als Richtwert; danach fehlt objektiver Erprobungszweck
- Keine Wiederholung der Erprobung für denselben Arbeitnehmer bei gleicher Stelle

## § 14 Abs. 2 TzBfG — Sachgrundlose Befristung

### Voraussetzungen
- Keine vorherige Beschäftigung beim gleichen Arbeitgeber (§ 14 Abs. 2 Satz 2 TzBfG: Anschlussverbot)
- Maximaldauer: 2 Jahre
- Maximale Verlängerungen: 3 Mal innerhalb der 2 Jahre

### Anschlussverbot — kritische Punkte
Das Anschlussverbot gilt nach BAG-Entscheidung von 2011 für jede frühere Beschäftigung beim selben Arbeitgeber, unabhängig wie lang zurück. Dies war später in der Instanzrechtsprechung umstritten; aktuelle BAG-Linie vor Ausgabe live prüfen.

**Dokumentations-Checkliste sachgrundlose Befristung:**
- [ ] Keine Vorbeschäftigung beim selben Arbeitgeber? (Prüfung mit Ergebnis dokumentieren)
- [ ] Gesamtdauer ≤ 2 Jahre?
- [ ] Anzahl der Verlängerungen ≤ 3?
- [ ] Bei Verlängerung: nur Dauer verlängert, keine anderen Änderungen (Aufgaben, Vergütung)?

### Achtung: Verlängerung ist keine inhaltliche Änderung
Eine Verlängerung der sachgrundlosen Befristung ist nur zulässig, wenn ausschließlich die Dauer verlängert wird. Jede inhaltliche Änderung (andere Stelle, höheres Gehalt, andere Abteilung) macht die Verlängerung zu einer Neubefristung — die dann einen Sachgrund benötigt.

## § 17 TzBfG — Entfristungsklage und Frist

### Dreiwöchige Klagefrist
Arbeitnehmer, der die Wirksamkeit der Befristung angreifen will, muss innerhalb von 3 Wochen nach dem vereinbarten Ende des befristeten Arbeitsverhältnisses Klage auf Feststellung erheben, dass das Arbeitsverhältnis aufgrund der Befristung nicht beendet ist.

**Fristversäumnis:** Befristung gilt als wirksam (§ 17 TzBfG analog § 7 KSchG).

### Kettenbefristung und Missbrauchsprüfung
BAG-Linie: Bei Kettenbefristungen prüft das BAG, ob eine missbräuchliche Gestaltung vorliegt. Indizien:
- Sehr hohe Gesamtdauer (> 5–7 Jahre)
- Sehr viele aufeinanderfolgende Befristungen
- Stets gleiche Aufgabe
- Kein sachlicher Grund für die Befristung erkennbar

## Dokumentationsplan für Compliance

| Dokument | Inhalt | Aufbewahrung |
|---|---|---|
| Befristungsvertrag | Schriftliche Befristungsabrede, Sachgrund (wenn vorhanden), Dauer | Personalakte, unbegrenzt |
| Verlängerungsvereinbarung | Nur Zeitverlängerung; vor Ablauf unterzeichnet | Personalakte |
| Vorbeschäftigungsprüfung | Ergebnis der Prüfung (keine Vorbeschäftigung) | Personalakte |
| BR-Information § 99 BetrVG | Zustimmung oder Fiktion bei befristeter Einstellung | Gremienakte |

## Anschluss-Skills
- `fachanwalt-arbeitsrecht-befristung-tzbfg` für Tiefenprüfung Befristungsrecht
- `spezial-tzbfg-schriftsatz-brief-und-memo-bausteine` für Schriftsatzbausteine
- `workflow-fristen-und-risikoampel` für Fristenkontrolle

## Was dieser Arbeitsgang nicht macht
- Keine Beratung zu wissenschaftlichen Befristungen nach WissZeitVG.
- Keine Prüfung besonderer öffentlich-rechtlicher Befristungsregeln (Beamtenrecht, öffentlicher Dienst spezifisch).

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

