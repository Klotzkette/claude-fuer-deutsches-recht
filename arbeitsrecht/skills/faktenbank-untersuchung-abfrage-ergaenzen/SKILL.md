---
name: faktenbank-untersuchung-abfrage-ergaenzen
description: "Faktenbank Untersuchung Abfrage Ergaenzen im Plugin Arbeitsrecht: prüft konkret Faktenbank und Quellen-Gate für aktuelle arbeitsrechtliche, Beantwortet Fragen gegen ein laufendes, Fügt einer laufenden internen Untersuchung neue Daten hinzu, Befragu. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Faktenbank Untersuchung Abfrage Ergaenzen

## Arbeitsbereich

**Faktenbank Untersuchung Abfrage Ergaenzen** ordnet den Fall über die tragenden Prüfungslinien: Faktenbank und Quellen-Gate für aktuelle arbeitsrechtliche, Beantwortet Fragen gegen ein laufendes, Fügt einer laufenden internen Untersuchung neue Daten hinzu. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `rechtsstand-mai-2026-faktenbank` | Faktenbank und Quellen-Gate für aktuelle arbeitsrechtliche Aussagen mit Stand 29.05.2026. Dieses Fachmodul dient als Quellen-Gate vor Ausgaben zu BAG-/BSG-Rechtsprechung, Statusfeststellung, AGG/Equal Pay, Urlaub, Freistellung, Kündigung, Arbeitszeit und Lohn/SV. Zitiert nur Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbare Quelle. |
| `untersuchung-abfrage` | Beantwortet Fragen gegen ein laufendes Untersuchungsprotokoll — was Zeugen gesagt haben, wo Schilderungen im Widerspruch stehen, welche Lücken bestehen, was die stärksten Belege zu jeder Frage sind. Lädt, wenn der Anwalt das Untersuchungsprotokoll abfragen möchte, ohne jeden Eintrag einzeln durchlesen zu müssen. |
| `untersuchung-ergaenzen` | Fügt einer laufenden internen Untersuchung neue Daten hinzu — Dokumente, Befragungsnotizen oder Beobachtungen. Verarbeitet Dokumentenpakete anhand dokumentierter Auswahlkriterien, markiert relevante Funde und protokolliert alles Gesichtete zur Deckungsverifikation. Lädt, wenn neue Beweise, Befragungsnotizen oder Dokumentenlieferungen für eine laufende Untersuchung eingehen. |
| `untersuchung-eroeffnen` | Eröffnet eine neue interne Untersuchungssache — führt die Sachverhaltserfassung durch, generiert die Quellencheckliste und legt das persistente Untersuchungsprotokoll an. Lädt, wenn eine Beschwerde oder ein Hinweis eingeht und ein vertraulicher Untersuchungsarbeitsbereich eingerichtet werden soll. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `rechtsstand-mai-2026-faktenbank`

**Fokus:** Faktenbank und Quellen-Gate für aktuelle arbeitsrechtliche Aussagen mit Stand 29.05.2026. Dieses Fachmodul dient als Quellen-Gate vor Ausgaben zu BAG-/BSG-Rechtsprechung, Statusfeststellung, AGG/Equal Pay, Urlaub, Freistellung, Kündigung, Arbeitszeit und Lohn/SV. Zitiert nur Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbare Quelle.

### Rechtsstand Mai 2026 — Faktenbank Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsstand Mai 2026 — Faktenbank Arbeitsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill ist kein allgemeines Lehrbuch, sondern das Quellen-Gate für faktische Aussagen im Arbeitsrecht-Plugin. Er wird geladen, wenn der Nutzer nach aktueller Rechtslage, Rechtsprechung, Fristen, Lohn-/Sozialversicherung, Statusfeststellung, Kündigung, AGG, Urlaub oder Freistellung fragt.

Stand dieser Faktenbank: **29.05.2026**. Vor einer konkreten Ausgabe trotzdem Normtext und Rechtsprechung live prüfen, wenn die Aussage fristen-, haftungs- oder streitentscheidend ist.

## Quellenregel

- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung nur zitieren mit: Gericht, Entscheidungsform, Datum, Aktenzeichen, kurzer tragender Aussage, freier/amtlicher Link.
- Wenn ein Aktenzeichen nicht frei verifizierbar ist: nicht zitieren, sondern als Recherchebedarf markieren.
- Literatur nur verwenden, wenn der Nutzer sie hochlädt oder ein lizenzierter Live-Zugriff tatsächlich geöffnet wurde.

## Verifizierte Rechtsprechungsanker

| Thema | Gesicherter Anker | Tragende Aussage für den | Freie Quelle |
|---|---|---|---|
| Mindesturlaub und Vergleich | BAG, Urteil vom 03.06.2025, 9 AZR 104/24 | Auf gesetzlichen Mindesturlaub kann während des bestehenden Arbeitsverhältnisses nicht wirksam durch gerichtlichen Vergleich verzichtet werden; § 13 Abs. 1 Satz 3 BUrlG sperrt Abweichungen zu Lasten des Arbeitnehmers. | https://www.bundesarbeitsgericht.de/entscheidung/9-azr-104-24/ |
| Entgeltgleichheit / Paarvergleich | BAG, Urteil vom 23.10.2025, 8 AZR 300/24 | Für den Anspruch auf gleiches Entgelt kann ein Paarvergleich genügen; bei geringerer Vergütung einer Frau für gleiche oder gleichwertige Arbeit greift die Vermutung einer Benachteiligung wegen des Geschlechts. | https://www.bundesarbeitsgericht.de/entscheidung/8-azr-300-24/ |
| Freistellungsklausel und Dienstwagen | BAG, Urteil vom 25.03.2026, 5 AZR 108/25 | Eine AGB-Klausel, die den Arbeitgeber im gekündigten Arbeitsverhältnis pauschal zur Freistellung und zum Widerruf der Dienstwagennutzung berechtigt, kann unangemessen sein; konkrete Interessenabwägung nötig. | https://www.bundesarbeitsgericht.de/presse/wirksamkeit-einer-freistellungsklausel-widerruf-der-dienstwagennutzung/ |
| Status Honorarlehrkraft | BSG, Urteil vom 05.11.2024, B 12 BA 3/23 R | Statusprüfung bleibt einzelfallbezogen; Vertragsbezeichnung und Parteiwille tragen nicht, wenn tatsächliche Eingliederung und fehlendes Unternehmerrisiko für Beschäftigung sprechen. | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2024/2024_11_05_B_12_BA_03_23_R.html |
| Status in fremder Betriebsorganisation | BSG, Urteil vom 12.06.2024, B 12 BA 2/22 R | Bei Tätigkeiten in einer fremden Arbeitsorganisation sind Eingliederung, Weisungsbindung, eigene Betriebsmittel, Preis-/Personalrisiko und unternehmerische Freiheit konkret zu prüfen. | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2024/2024_06_12_B_12_BA_02_22_R.html |

## Norm- und Praxisanker

| Thema | Normen | Workflow-Hinweis |
|---|---|---|
| Kündigungsschutz | §§ 1, 4, 7, 9, 10, 12, 17, 18 KSchG; §§ 622, 626 BGB; § 102 BetrVG | Erst Frist/Zugang und Sonderkündigungsschutz sichern, dann Grund, Sozialauswahl, Betriebsrat, Massenentlassung, Weiterbeschäftigung und Vergleichsdruck prüfen. |
| Befristung und Schriftform | § 14 Abs. 4, §§ 16, 17 TzBfG; §§ 126, 126a, 623 BGB | Befristungsabrede vor Arbeitsbeginn schriftlich oder mit wirksamer QES; Scan/einfache Signatur reicht nicht. Dreiwochenfrist ab vereinbartem Ende. |
| Urlaub | §§ 1, 3, 7, 13 BUrlG | Mindesturlaub nicht durch Vergleich im laufenden Arbeitsverhältnis preisgeben; bei Beendigung Urlaubsabgeltung getrennt prüfen. |
| AGG / Equal Pay | §§ 1, 7, 15, 22 AGG; EntgTranspG | Erst Vergleichsperson und gleiche/gleichwertige Arbeit, dann Vermutung, Rechtfertigung, Fristen und Auskunfts-/Dokumentationslage. |
| Status/Scheinselbständigkeit | § 611a BGB; §§ 7, 7a, 28p SGB IV; § 266a StGB | Tatsächliche Durchführung vor Vertragstext; bei hohem Risiko DRV-Statusfeststellung, SV-Nachberechnung und Strafbarkeitsrisiko getrennt dokumentieren. |
| Arbeitszeit und Mindestlohn | ArbZG, MiLoG, NachwG, EFZG | Bei Arbeitszeit immer Aufzeichnung, Bereitschaft/Überstunden, Ausschlussfristen, Mindestlohnfestigkeit und Beweislast getrennt prüfen. |

## Ausgabe-Standard

Jede aktuelle arbeitsrechtliche Antwort enthält am Ende kurz:

1. **Gesicherte Quellen:** Normen und ggf. Gerichtsentscheidungen mit Datum/Aktenzeichen/Link.
2. **Nicht verifiziert:** Alles, was nicht frei/amtlich geprüft werden konnte.
3. **Nächster Fachmodul:** aus diesem Plugin, z. B. `kuendigungs-pruefung`, `arbeitnehmer-status`, `lohnsteuer-sozialversicherung`, `agg-pruefung-bewerber-und-beschaeftigte`, `aufhebungsvertrag` oder `entfristung-schriftform-14-abs-4-erkennen`.

## 2. `untersuchung-abfrage`

**Fokus:** Beantwortet Fragen gegen ein laufendes Untersuchungsprotokoll — was Zeugen gesagt haben, wo Schilderungen im Widerspruch stehen, welche Lücken bestehen, was die stärksten Belege zu jeder Frage sind. Lädt, wenn der Anwalt das Untersuchungsprotokoll abfragen möchte, ohne jeden Eintrag einzeln durchlesen zu müssen.

### Untersuchungsprotokoll-Abfrage (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Untersuchungsprotokoll-Abfrage (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Beantwortet Fragen gegen das Untersuchungsprotokoll — was Zeugen gesagt haben,
wo Schilderungen im Widerspruch stehen, welche Lücken bestehen, was die
stärksten Belege zu jeder Untersuchungsfrage sind.

Lädt, wenn der Anwalt das Erkenntnisbild der Untersuchung abfragen möchte,
ohne alle Protokolleinträge einzeln lesen zu müssen.

## Eingaben

- Bezeichnung der Untersuchungssache
- Konkrete Frage gegen das Protokoll

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 626 BGB: Wichtiger Grund für außerordentliche Kündigung — Abfragen
 des Protokolls helfen, den Tatverdacht zu verdichten oder zu widerlegen
- § 22 AGG: Beweislastverteilung bei Diskriminierungsvorwürfen — bei
 AGG-Sachverhalt strukturierte Protokollauswertung als Basis für
 Enthaftungsnachweis des Arbeitgebers
- § 1 Abs. 2 KSchG: Soziale Rechtfertigung der Kündigung — Abfragen der
 Stärke der Beweislage je Untersuchungsfrage hilft, Wirksamkeitsrisiken
 einer verhaltens- oder personenbedingten Kündigung zu bewerten
- § 26 BDSG: Verarbeitungszweck — Protokollabfragen dienen ausschließlich
 dem Untersuchungszweck; kein Zweckwechsel ohne neue Rechtsgrundlage

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Verdachtskündigung — dringender Tatverdacht erfordert objektive Schwere
 auf Basis des tatsächlich Ermittelten; Protokollauswertung bestimmt, ob
 Schwelle erreicht ist
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Tatkündigung — Überzeugungsmaßstab des Arbeitgebers; Protokollauswertung
 zur Überprüfung, ob der volle Nachweis einer Pflichtverletzung vorliegt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Widersprüchliche Zeugenaussagen im Kündigungsschutzprozess — der Arbeitgeber
 trägt die Darlegungs- und Beweislast für den Kündigungsgrund; nur was
 bei der Kündigung bekannt war, zählt (Nachschieben von Gründen nur
 eingeschränkt möglich)

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- § 626 BGB: Zwei-Wochen-Frist, Verdachtskündigung und Anhörung nur mit verifizierter BAG-Rechtsprechung oder Nutzerquelle vertiefen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Darlegungs- und Beweislast des Arbeitgebers; Nachschieben von
 Kündigungsgründen
- AGG: §§ 12, 15, 22 AGG anhand Gesetz, Nutzerquelle und frei verifizierter Rechtsprechung prüfen.

## Ablauf

**Schritt 1 — Referenz-Skill laden**

Lade die Referenz-Skill `interne-untersuchung` und führe Modus 3
(Protokoll abfragen) aus.

**Schritt 2 — Gesamtes Protokoll lesen**

Immer das vollständige Protokoll lesen, bevor eine Frage beantwortet wird.

**Schritt 3 — Eintrags-IDs zitieren**

In jeder Antwort Protokoll-Eintrags-IDs in Klammern angeben. Dies ermöglicht
Rückverfolgung zur Primärquelle und belegt die Erkenntnisgrundlage.

**Schritt 4 — Bei fehlenden Erkenntnissen**

Falls das Protokoll zu einem Thema nichts enthält:

> Zum Thema [Thema] liegen in diesem Untersuchungsprotokoll
> ([N] Einträge gesichtet) keine Erkenntnisse vor. Dies sollte als
> Beweislücke erfasst werden.

Anbieten, den Punkt als Beweislücke zu protokollieren.

**Schritt 5 — Abfragetypen**

**Sachverhaltsabfrage** ("Was hat [Person] zu [Thema] gesagt?"):
Aus Protokolleinträgen antworten, Eintrags-IDs zitieren.

**Widerspruchsabfrage** ("Wo widersprechen sich die Schilderungen?"):
Alle `widerspricht_eintrag`-Verknüpfungen zeigen. Pro Widerspruch:
Was ist der Konflikt, welche Einträge stehen in Spannung, welche
dokumentarische Evidenz bezieht sich auf den Widerspruch.

**Deckungsabfrage** ("Was fehlt noch?" / "Wo haben wir Lücken?"):
`quellen-checkliste.yaml` und `beweislücken` im log.yaml auslesen. Melden:
- Noch offene Checklistenpunkte
- Protokollierte Beweislücken
- Schilderungen, die auf noch nicht erhobene Quellen hinweisen

**Stärkeabfrage** ("Was ist die stärkste Evidenz zu jeder Frage?"):
Für jede Untersuchungsfrage: höchstbewertete Protokolleinträge, dokumentarische
Bestätigungen und ungelöste Widersprüche — frageweise strukturiert.

**Reife-Abfrage** (Verdachtsgrad für Kündigung):
Für eine Verdachtskündigung nach § 626 BGB: Protokolleinträge nach
objektiver Schwere und Dringlichkeit des Verdachts auswerten. Anhörung
der beschuldigten Person dokumentiert? Falls nicht: flaggen.

## Ausgabeformat

Direkte Antwort auf die gestellte Frage, mit Eintrags-IDs in Klammern.
Bei fehlenden Erkenntnissen: expliziter Hinweis und Angebot zur
Beweislückendokumentation. Bei Widerspruchsabfragen: tabellarische
Gegenüberstellung der Einträge mit Beschreibung des Konflikts.

## Beispiel

```
/arbeitsrecht:untersuchung-abfrage Sache-Mueller
Was hat der Zeuge Bauer zum Dezember-Meeting gesagt?
```

```
/arbeitsrecht:untersuchung-abfrage Sache-Mueller
Wo widersprechen sich die Schilderungen?
```

```
/arbeitsrecht:untersuchung-abfrage Sache-Mueller
Was fehlt noch?
```

Beispiel-Antwort bei Widerspruchsabfrage:

```
Identifizierte Widersprüche:

Widerspruch 1 — Eintrag #3 vs. Eintrag #7:
 Eintrag #3 (Beschwerdeführerin Koch, 15.01.2025): "Das Gespräch fand nur
 zwischen mir und Herrn Müller statt."
 Eintrag #7 (Zeuge Bauer, 22.01.2025): "Frau Schmidt war bei dem Gespräch
 anwesend."
 Dokumentarische Evidenz: Kalender-Eintrag vom 12.11.2024 (Eintrag #5)
 zeigt drei Teilnehmer. Widerspruch zur Schilderung der Beschwerdeführerin.

Handlungsbedarf: Frau Schmidt als Zeugin befragen (Checkliste Punkt 3 — noch offen).
```

## Risiken und typische Fehler

- **Protokollabfrage ohne vollständiges Lesen**: Antworten ohne Lesen des
 Gesamtprotokolls können Widersprüche und Lücken übersehen. Immer alle
 Einträge sichten.
- **Fehlende Eintrags-IDs**: Antworten ohne Eintrags-ID-Referenzen sind
 nicht rückverfolgbar und erschweren spätere Anfechtungen.
- **Lücken nicht als Lücken benennen**: "Dazu weiß ich nichts" ist kein
 angemessenes Ergebnis — die Nicht-Existenz von Erkenntnissen im Protokoll
 muss explizit als potenzielle Beweislücke benannt werden.
- **Widersprüche glätten**: Widersprechende Schilderungen dürfen nicht
 harmonisiert werden. Sie müssen direkt benannt werden — der Anwalt
 entscheidet, welcher Version geglaubt wird.
- **Zweckbindung beachten**: Protokolldaten dürfen nur für Untersuchungs-
 zwecke genutzt werden (§ 26 BDSG). Keine Weitergabe für andere Zwecke
 ohne neue Rechtsgrundlage.

## Quellenpflicht

Bei Abfragen zur Beweislage für Kündigung zitieren:
- § 626 BGB (Tatverdacht / Wichtiger Grund)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bei AGG-Sachverhalt: § 22 AGG und frei verifizierte BAG-Rechtsprechung

Detaillierter Abfrageprozess, Zitierregeln und Lückendokumentations-Templates
befinden sich in der Referenz-Skill `interne-untersuchung` — diese vor
inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Ergänzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Protokollabfrage klären

1. Welche Art der Abfrage ist gewünscht (Sachverhalts-, Widerspruchs-, Deckungsabfrage oder Stärkeabfrage)?
2. Ist eine Kündigung in der Schwebe? → Dann Reife-Abfrage nach § 626 BGB-Schwellenwert
3. Liegt ein AGG-relevanter Sachverhalt vor? → Besondere Sorgfalt bei § 22 AGG-Beweislast

## 3. `untersuchung-ergaenzen`

**Fokus:** Fügt einer laufenden internen Untersuchung neue Daten hinzu — Dokumente, Befragungsnotizen oder Beobachtungen. Verarbeitet Dokumentenpakete anhand dokumentierter Auswahlkriterien, markiert relevante Funde und protokolliert alles Gesichtete zur Deckungsverifikation. Lädt, wenn neue Beweise, Befragungsnotizen oder Dokumentenlieferungen für eine laufende Untersuchung eingehen.

### Untersuchungs-Datenpflege (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Untersuchungs-Datenpflege (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Fügt Daten in ein laufendes Untersuchungsprotokoll ein. Verarbeitet
Dokumentenpakete anhand dokumentierter Auswahlkriterien (§ 26 BDSG —
Verhältnismäßigkeit), markiert relevante Funde, protokolliert alle
gesichteten Unterlagen zur Deckungsverifikation.

Lädt, wenn neue Erkenntnisse, Befragungsnotizen oder Dokumentenlieferungen
für eine laufende Untersuchung zur Verarbeitung eingehen.

## Eingaben

- Bezeichnung der Untersuchungssache (oder Slug)
- Art der Daten: Befragungsnotizen / Dokumentenpaket / Anwaltsnotizen /
 Bestätigung Anhörungshinweis
- Inhalt der Daten (eingefügt oder angehängt)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Verarbeitung von Beschäftigtendaten zur Aufdeckung von
 Straftaten oder schwerwiegenden Pflichtverletzungen — Verhältnismäßigkeit
 ist Voraussetzung; Verarbeitung nur soweit zur Sachaufklärung erforderlich
- Art. 5 Abs. 1 lit. c DSGVO: Datenminimierungsgrundsatz — nur notwendige
 Daten erheben und verarbeiten
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Überwachungseinrichtungen
 — vor Auswertung von E-Mails oder IT-Kommunikation ist Zustimmung des
 Betriebsrats oder eine einschlägige Betriebsvereinbarung erforderlich
- § 626 BGB: Außerordentliche Kündigung; Frist des § 626 Abs. 2 BGB (zwei
 Wochen ab Kenntnis) — Dokumentation des Zeitpunkts des Kenntniserwerbs ist
 untersuchungskritisch
- § 241 Abs. 2 BGB: Mitwirkungspflicht des Arbeitnehmers im Rahmen
 des Untersuchungsverfahrens; Grenzen bei Selbstbelastung

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Beweisverwertungsverbot bei rechtswidrig erlangten Dokumenten — heimliche
 Videoüberwachung ohne Betriebsratsinhaber führt zum Verwertungsverbot
 auch im Kündigungsschutzprozess; Grundsatz gilt sinngemäß für
 rechtswidrig ausgewertete Kommunikation
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Verdachtskündigung — Anforderungen an die Dokumentation des Tatverdachts;
 objektive Schwere; inhaltliche Mindestanforderungen an die Anhörung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Erstattungsfähigkeit von Untersuchungskosten (Detektivkosten) — nur bei
 konkreter Verdachtslage bei Beauftragung und Verhältnismäßigkeit

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Beschäftigtendatenschutz: § 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Überwachungseinrichtungen; Rechtsprechung nur frei verifiziert zitieren.
- § 626 BGB: Zwei-Wochen-Frist, Verdachtskündigung und Anhörung nur mit verifizierter BAG-Rechtsprechung oder Nutzerquelle vertiefen.

## Ablauf

**Schritt 1 — Kontext laden**

Lese `CLAUDE.md` im Plugin-Verzeichnis.

**Schritt 2 — Sache identifizieren**

Falls mehrere Untersuchungsordner existieren: Frage, zu welcher Sache die
Daten gehören. Bei nur einer Sache: direkt fortfahren.

**Schritt 3 — Referenz-Skill laden**

Lade die Referenz-Skill `interne-untersuchung` und führe Modus 2 (Daten
hinzufügen) aus.

**§ 87 Abs. 1 Nr. 6 BetrVG-Check vor Dokumentenverarbeitung:**
Bei E-Mail- oder IT-Auswertungen: Prüfe, ob eine einschlägige
Betriebsvereinbarung vorliegt oder der Betriebsrat zugestimmt hat.
Falls unklar — flaggen, bevor Verarbeitung beginnt.

**Schritt 4 — Nach Verarbeitung melden**

Zeige Oberflächenrate und Liste relevanter Funde:

```
Dokumentenprüfung abgeschlossen.
Geprüft: [N] Dokumente
Relevant: [N]
Geprüft / nicht relevant: [N]
Neue Beweislücken: [N]

Relevante Funde:
 - [Kurzbeschreibung] → Auswahlkriterium: [Nr.]
 - [Kurzbeschreibung] → Auswahlkriterium: [Nr.]
```

**Schritt 5 — Quellencheckliste aktualisieren**

Wenn die hinzugefügten Daten einen Checklistenpunkt abdecken: Anwalt fragen,
ob der Punkt als "erledigt" oder "in Bearbeitung" markiert werden soll.
Nicht automatisch als erledigt markieren — der Anwalt entscheidet, wann eine
Quelle ausreichend abgedeckt ist.

**§ 626 Abs. 2 BGB-Kenntnisdatum:**
Bei Befragungsnotizen oder Dokumenten, die erstmals den konkreten Tatverdacht
begründen oder wesentlich vertiefen: Datum des Kenntniserwerbs explizit im
Protokolleintrag vermerken. Die Zwei-Wochen-Frist für eine außerordentliche
Kündigung beginnt ab diesem Zeitpunkt zu laufen.

## Ausgabeformat

Zusammenfassung nach Schritt 4 (Zählbericht), dann Aufforderung zur
Aktualisierung der Quellencheckliste falls zutreffend. Bei
§ 626 Abs. 2 BGB-relevantem Kenntnisdatum: gesonderter Hinweisblock.

## Beispiel

```
/arbeitsrecht:untersuchung-ergänzen Sache-Mueller
[Befragungsnotizen aus Gespräch mit Zeugin K. — 12.02.2025]
```

```
/arbeitsrecht:untersuchung-ergänzen Sache-Mueller
[E-Mail-Export 01.01.2025–31.01.2025 — nach BR-Betriebsvereinbarung freigegeben]
```

Beispiel-Ausgabe nach Dokumentenverarbeitung:

```
Dokumentenprüfung abgeschlossen.
Geprüft: 47 Dokumente
Relevant: 5
Geprüft / nicht relevant: 42
Neue Beweislücken: 2

Relevante Funde:
 - E-Mail vom 08.01.2025 Müller an Schmitt: "das solltest du lieber nicht aufschreiben"
 → Auswahlkriterium 4 (implizite Selbstbelastung)
 - E-Mail vom 15.01.2025: widerspricht Schilderung von Zeugin K. in Eintrag #3
 → Auswahlkriterium 5 (Widerspruch zu bestehendem Protokolleintrag)
```

## Risiken und typische Fehler

- **§ 87 Abs. 1 Nr. 6 BetrVG-Versäumnis**: Rechtswidrig ausgewertete
 Kommunikation kann einem Beweisverwertungsverbot unterliegen und die
 Kündigung gefährden. Betriebsvereinbarung vor Auswertung sicherstellen.
- **Verhältnismäßigkeit nach § 26 BDSG**: Massenhafte Dokumentenauswertung
 ohne konkreten Verdacht ist unzulässig. Auswahlkriterien dokumentieren,
 um Verhältnismäßigkeit nachweisen zu können.
- **§ 626 Abs. 2 BGB-Frist**: Die Zwei-Wochen-Frist beginnt ab sicherer
 Kenntnisnahme. Unklare Dokumentation des Kenntniszeitpunkts kann zur
 Fristversäumnis führen.
- **Selektive Protokollierung**: Nur relevante Funde zu protokollieren und
 nicht-relevante Dokumente nicht zu erfassen, untergräbt die Deckungsverifikation.
 Jedes gesichtete Dokument muss protokolliert werden.
- **False Negative durch zu enge Kriterien**: Auswahlkriterien großzügig
 handhaben — ein False Positive (irrelevanter Fund protokolliert) ist
 besser als ein übersehener wesentlicher Beweis.

## Quellenpflicht

Bei Ausgaben zu Dokumentenverarbeitung zitieren:
- § 26 BDSG (Verhältnismäßigkeit, Straftatenaufdeckung)
- § 87 Abs. 1 Nr. 6 BetrVG (Mitbestimmung)
- Art. 5 Abs. 1 lit. c DSGVO (Datenminimierung)
- § 626 Abs. 2 BGB (Zwei-Wochen-Frist, Kenntnisdatum)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Beschäftigtendatenschutz: § 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.

Detaillierte Auswahlkriterien, Protokolleintrag-Format und
Deckungsverifikationsregeln befinden sich in der Referenz-Skill
`interne-untersuchung` — diese vor inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Ergänzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Dateneingabe klären

1. Handelt es sich um neue Zeugenaussagen, Dokumentenlieferung oder anwaltliche Notizen?
2. Liegt eine § 87 Abs. 1 Nr. 6 BetrVG-freigabe für E-Mail-/IT-Auswertungen vor?
3. Begründet die neue Erkenntnis erstmals einen konkreten Tatverdacht? → Dann Kenntnisdatum für § 626 Abs. 2 BGB festhalten!

## 4. `untersuchung-eroeffnen`

**Fokus:** Eröffnet eine neue interne Untersuchungssache — führt die Sachverhaltserfassung durch, generiert die Quellencheckliste und legt das persistente Untersuchungsprotokoll an. Lädt, wenn eine Beschwerde oder ein Hinweis eingeht und ein vertraulicher Untersuchungsarbeitsbereich eingerichtet werden soll.

### Untersuchungseröffnung (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Untersuchungseröffnung (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Eröffnet eine neue interne Untersuchungssache — führt die strukturierte
Sachverhaltserfassung durch, generiert die auf den Untersuchungstyp
zugeschnittene Quellencheckliste und legt das persistente
Untersuchungsprotokoll an.

Lädt, wenn eine Beschwerde oder ein Hinweis vorliegt und ein strukturierter,
vertraulicher Untersuchungsarbeitsbereich eingerichtet werden soll.

## Eingaben

- Kurzbeschreibung des Vorwurfs oder der Besorgnis (kann nach Sachverhaltserfassung
 verfeinert werden)
- Ist die Untersuchung anwaltsgeleitet? (Beeinflusst Schutzstatus der Unterlagen)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Verarbeitung von Beschäftigtendaten zur Aufdeckung von
 Straftaten oder schwerwiegenden Pflichtverletzungen — Erforderlichkeit
 und Verhältnismäßigkeit als Voraussetzung; Protokolldaten sind
 Beschäftigtendaten
- §§ 34, 36, 37 HinSchG: Hinweisgeberschutzgesetz — Vertraulichkeit der
 Identität der hinweisgebenden Person; Verbot von Repressalien; interne
 Meldestelle; Dokumentationspflichten
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen
 Überwachungseinrichtungen — vor Kommunikationsauswertungen klären
- § 82 Abs. 2 BetrVG: Recht des Arbeitnehmers, ein Betriebsratsmitglied
 zu Besprechungen über Beschwerden hinzuzuziehen
- §§ 84, 85 BetrVG: Beschwerderecht des Arbeitnehmers; Behandlung durch
 den Betriebsrat
- § 626 Abs. 2 BGB: Zwei-Wochen-Frist — Dokumentation des ersten
 Kenntniszeitpunkts ab Eröffnung kritisch
- §§ 3 ff. AGG: Diskriminierungsverbote — bei AGG-relevantem Sachverhalt
 strukturierte Untersuchung als Enthaftungsvoraussetzung

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Verdachtskündigung — umfassende Sachaufklärung vor Kündigung zwingend;
 Untersuchungspflicht des Arbeitgebers; Dokumentationsanforderungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Beginn der Zwei-Wochen-Frist des § 626 Abs. 2 BGB — Fristbeginn erst
 nach ausreichender Sachaufklärung; Pflicht, Ermittlungen zügig zu führen;
 mutwillige Verzögerung kann Verwirkung begründen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Inhaltliche Anforderungen an die Anhörung der beschuldigten Person vor
 Verdachtskündigung; Frage und Antwortrecht; Protokollierungspflicht

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Beschäftigtendatenschutz: § 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.
- § 626 BGB: Zwei-Wochen-Frist, Verdachtskündigung und Anhörung nur mit verifizierter BAG-Rechtsprechung oder Nutzerquelle vertiefen.
- AGG: §§ 12, 15, 22 AGG anhand Gesetz, Nutzerquelle und frei verifizierter Rechtsprechung prüfen.

## Ablauf

**Schritt 1 — Kontext laden**

Lese `CLAUDE.md` im Plugin-Verzeichnis → jurisdiktioneller Fußabdruck,
Eskalationstabelle, etwaige Untersuchungsprotokolle.

**Schritt 2 — Bestehende Sache prüfen**

Falls bereits ein Untersuchungsordner mit demselben Slug existiert: Warnung
ausgeben, bevor überschrieben wird.

**Schritt 3 — Referenz-Skill laden**

Lade die Referenz-Skill `interne-untersuchung` und führe Modus 1
(Neue Untersuchung eröffnen) aus.

**Vertraulichkeits-Vorabprüfung:**

> Vor der Eröffnung: Ist diese Untersuchung anwaltsgeleitet? Wenn ja —
> erhöhter Schutz der Arbeitsergebnisse. Wenn nein — Schutzstatus und
> Weitergabe der Unterlagen vorab klären. Unterlagen mit fehlerhaftem
> Schutzstatus können in einem etwaigen Verfahren problematisch werden.

**Schritt 4 — Sachverhaltserfassung, Quellencheckliste, Protokoll**

Alle Schritte aus Modus 1 der Referenz-Skill vollständig ausführen:
Sachverhaltserfassung in einem Block, Quellencheckliste je nach Untersuchungstyp
generieren und dem Anwalt vorlegen, Protokolldateien anlegen.

**§ 82 Abs. 2 BetrVG-Hinweis:**
Wenn ein Arbeitnehmer zu Gesprächen geladen wird, die seine Beschwerde
oder seine Stellung im Untersuchungsverfahren berühren: Hinweisen, dass
er nach § 82 Abs. 2 BetrVG das Recht hat, ein Betriebsratsmitglied
hinzuzuziehen. Dies protokollieren.

**Schritt 5 — Erstes Protokolldatum sichern**

Datum und Uhrzeit der Eröffnung im Protokoll festhalten. Dies ist bei
einer eventuellen Verdachtskündigung der Ausgangszeitpunkt für die
Fristberechnung nach § 626 Abs. 2 BGB (Frist beginnt mit sicherer
Kenntnis, nicht mit bloßem Verdacht — aber Aufklärung ist zügig
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

Vertraulichkeitsprüfung, dann strukturierte Sachverhaltserfassungs-Abfrage
in einem Block, dann Quellencheckliste zur Bestätigung durch den Anwalt,
dann Bestätigung der angelegten Protokolldateien:

```
Untersuchung eröffnet — [Sachebezeichnung] — [ISO-Datum]
Protokolldatei: investigation-[slug]/log.yaml
Quellencheckliste: investigation-[slug]/quellen-checkliste.yaml
Dokumentenprotokoll: investigation-[slug]/dokumente-geprueft.yaml

Nächste Schritte:
 /arbeitsrecht:untersuchung-ergänzen [slug] — Daten hinzufügen
 /arbeitsrecht:untersuchung-abfrage [slug] — Protokoll abfragen
 /arbeitsrecht:untersuchungs-memo [slug] — Vermerk entwerfen
```

## Beispiel

```
/arbeitsrecht:untersuchung-eroeffnen
Belästigungsbeschwerde gegen Abteilungsleiter in der Hamburger Niederlassung.
```

```
/arbeitsrecht:untersuchung-eroeffnen
(Skill fragt nach Details)
```

Beispiel-Ausgabe nach Sachverhaltserfassung (Betriebsrat-Flag):

> Hinweis: Die beschuldigte Person ist Betriebsratsmitglied. Kündigung
> erfordert Zustimmung des Betriebsrats (§ 103 BetrVG) oder gerichtliche
> Ersetzung. Dies ändert den weiteren Verfahrensablauf wesentlich —
> Protokoll anpassen und externen Arbeitsrechtler einbinden.

## Risiken und typische Fehler

- **Anwaltsleitung unklar**: Ohne klare Anwaltsleitung ist der Schutzstatus
 der Untersuchungsunterlagen fraglich. Vor Anlegen der ersten Datei klären.
- **§ 626 Abs. 2 BGB-Uhr läuft**: Die Frist beginnt bei sicherer Kenntnis.
 Mutwillige Verzögerung der Untersuchung kann dazu führen, dass die
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 82 Abs. 2 BetrVG versäumt**: Wenn dem Arbeitnehmer das Recht auf
 Hinzuziehung eines Betriebsratsmitglieds nicht mitgeteilt wird, kann
 dies das Verfahren belasten.
- **HinSchG-Vertraulichkeit**: Bei Hinweisgebersachen ist die Identität der
 hinweisgebenden Person streng vertraulich zu halten (§ 8 Abs. 1 HinSchG).
 Protokolleinträge so gestalten, dass die Identität nicht für Unbefugte
 erkennbar ist.
- **Betriebsrat-Sonderstatus**: Beschuldigte Betriebsratsmitglieder
 genießen besonderen Schutz (§ 103 BetrVG). Früh klären.

## Quellenpflicht

Bei jeder Eröffnung zitieren:
- § 26 BDSG (Datenschutz, Verhältnismäßigkeit)
- §§ 34, 36, 37 HinSchG (bei Hinweisgebersachen)
- § 82 Abs. 2, §§ 84, 85 BetrVG (Betriebsratsrechte)
- § 626 Abs. 2 BGB (Fristbeginn-Dokumentation)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Beschäftigtendatenschutz: § 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.

Detaillierte Sachverhaltserfassung, Quellenchecklisten-Vorlagen und
Protokolldateiformate befinden sich in der Referenz-Skill
`interne-untersuchung` — diese vor inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Ergänzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Eröffnung klären

1. Ist die Untersuchung anwaltsgeleitet? (→ legal privilege, Schutzstatus klären)
2. Handelt es sich um einen HinSchG-Sachverhalt? (→ § 8 HinSchG Vertraulichkeit)
3. Liegt ein Betriebsratsmitglied als Beschuldigte/r vor? (→ § 103 BetrVG beachten)
4. Schwerbehindert? Werdende Mutter? (→ besonderer Kündigungsschutz)
5. § 626 Abs. 2 BGB-Uhr: Datum/Uhrzeit der Eröffnung festhalten
