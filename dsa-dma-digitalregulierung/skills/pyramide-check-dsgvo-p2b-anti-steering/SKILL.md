---
name: pyramide-check-dsgvo-p2b-anti-steering
description: "Pyramide Check DSGVO P2B Anti Steering: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pyramide Check DSGVO P2B Anti Steering

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pyramide Check DSGVO P2B Anti Steering** im Plugin DSA/DMA Digitalregulierung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `digitalregulierung-pyramide-check` | Sachverhalt den richtigen EU-Digitalregulierungs-Rechtsakten zuordnen: Anwalt oder Unternehmen fragt welche Regulierung greift. Normen: DSA (EU) 2022/2065, DMA (EU) 2022/1925, Data Act (EU) 2023/2854, DGA, AI Act (EU) 2024/1689, NIS-2, DORA, CRA, eIDAS 2.0, DDG, P2B-VO, § 19a GWB. Prüfraster: Akteurstyp, Dienst-Typ (Vermittlungsdienst, Hosting, Online-Plattform, VLOP, Kernplattformdienst, Gatekeeper), Datentyp, Risikoklasse. Output Kurzprüfschema mit Verweis auf Fachmodule. Abgrenzung: DSGVO-Fragen siehe datenschutzrecht-Plugin; AI Act spezifisch siehe ki-vo-ai-act-prüfer-Plugin. |
| `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` | Schnittstellen zwischen DSA/DMA und DSGVO, P2B-VO und § 19a GWB analysieren: Mehrere Regelwerke treffen gleichzeitig auf einen Sachverhalt. Normen: Art. 2 Abs. 4 DSA (kein Verdrangen DSGVO), Art. 1 Abs. 5 DMA, P2B-VO (EU) 2019/1150 (Plattform-Nutzer-Beziehungen), § 19a GWB (unterhalb DMA-Schwellen). Prüfraster: Konkurrenz DSA/DMA vs. DSGVO vs. P2B-VO, § 19a GWB als Luecken-Fuelung, Mehr-Anker-Strategie für welche Rechtsfolge. Output Schnittstellen-Memo, Anspruchs-Matrix. Abgrenzung: VLOP-Designation siehe dsa-vlop-vlose-einordnung-und-pflichten; Gatekeeper DMA siehe dma-gatekeeper-schwellen-und-kernplattformdienste. |
| `dma-anti-steering-app-store-design` | Anti-Steering Pflichten Art. 5 Abs. 4 DMA fuer App-Stores: Entwickler duerfen ausserhalb des Stores informieren, ueber alternative Preise und Zahlwege. Pruefraster: keine Behinderung, keine Strafgebuehr, kein Linkverbot. Apple- und Google-Beispiele, EU-Verfahren. Compliance-Checkliste fuer Gatekeeper und Entwicklerschriftsatz bei Verstoss. |

## Arbeitsweg

Im Plugin DSA/DMA Digitalregulierung gilt für **Pyramide Check DSGVO P2B Anti Steering**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `digitalregulierung-pyramide-check`

**Fokus:** Sachverhalt den richtigen EU-Digitalregulierungs-Rechtsakten zuordnen: Anwalt oder Unternehmen fragt welche Regulierung greift. Normen: DSA (EU) 2022/2065, DMA (EU) 2022/1925, Data Act (EU) 2023/2854, DGA, AI Act (EU) 2024/1689, NIS-2, DORA, CRA, eIDAS 2.0, DDG, P2B-VO, § 19a GWB. Prüfraster: Akteurstyp, Dienst-Typ (Vermittlungsdienst, Hosting, Online-Plattform, VLOP, Kernplattformdienst, Gatekeeper), Datentyp, Risikoklasse. Output Kurzprüfschema mit Verweis auf Fachmodule. Abgrenzung: DSGVO-Fragen siehe datenschutzrecht-Plugin; AI Act spezifisch siehe ki-vo-ai-act-prüfer-Plugin.

# Digitalregulierung — Pyramiden-Check

## Zweck

Bei jedem digitalrechtlichen Mandat zuerst klären: **Welcher Rechtsakt greift überhaupt?** Die EU-Digitalregulierung ist geschichtet und überlappt — derselbe Sachverhalt kann gleichzeitig DSA, DSGVO und nationales Wettbewerbsrecht auslösen.

## Erstprüfung in vier Schritten

### Schritt 1 — Akteurstyp bestimmen

| Akteur | Mögliche Rechtsakte |
|---|---|
| Online-Vermittlungsdienst (Hosting, Marktplatz, soziales Netzwerk) | DSA, P2B-VO, DDG |
| Sehr große Online-Plattform (VLOP) oder Suchmaschine (VLOSE) | DSA Kapitel III Abschnitt 5 (Art. 33 ff.) |
| Gatekeeper iSd Art. 3 DMA | DMA |
| Anbieter von KI-Systemen | AI Act |
| Anbieter eines Datenvermittlungsdienstes | DGA |
| Hersteller eines IoT-Produkts | Data Act, CRA |
| Anbieter qualifizierter Vertrauensdienste | eIDAS 2.0 |
| Betreiber wesentlicher/wichtiger Einrichtungen | NIS-2 |
| Finanzunternehmen / IKT-Drittdienstleister | DORA |
| Marktbeherrschendes oder marktübergreifend bedeutendes Digitalunternehmen | § 19a GWB |

### Schritt 2 — Dienst-Typ einordnen (DSA-Hierarchie)

DSA arbeitet mit einer Hierarchie aufsteigender Pflichten:

1. **Reiner Durchleitungsdienst** (Art. 4) — minimale Pflichten, Haftungsprivileg
2. **Caching** (Art. 5)
3. **Hosting-Dienst** (Art. 6) — Notice-and-Action, Art. 16
4. **Online-Plattform** (Art. 19 ff.) — interne Beschwerdeverfahren, trusted flaggers, Transparenzberichte
5. **VLOP / VLOSE** ab 45 Mio. monatlich aktiven Nutzern in der EU (Art. 33) — Systemrisiko, Audits, Forschungsdatenzugang
6. **Online-Marktplatz** — zusätzlich Art. 30 ff. (Händler-Identifikation)

Kleinunternehmen sind teilweise befreit (Art. 19 für kleine/Kleinst-Unternehmen).

### Schritt 3 — Datentyp prüfen

- **Personenbezogene Daten** → DSGVO gilt zusätzlich (Art. 2 Abs. 4 DSA, kein lex specialis)
- **Nicht-personenbezogene maschinengenerierte Daten (IoT)** → Data Act
- **Daten der öffentlichen Hand für Weiterverwendung** → DGA, Open-Data-RL
- **Geschäftsgeheimnisse** → GeschGehG bleibt anwendbar

### Schritt 4 — Risiko- und Inhaltsklasse

- **Illegale Inhalte** → DSA Art. 16
- **Schädliche aber legale Inhalte (Desinformation, Wahlen)** → DSA Art. 34/35 systemische Risiken
- **KI-System mit hohem Risiko** → AI Act Anhang III
- **Kritische Infrastruktur** → NIS-2 / CRA

## Anwendungsverhältnis

- **Lex specialis derogat legi generali** gilt nur eingeschränkt: DSA, DSGVO und Wettbewerbsrecht laufen oft parallel
- **DMA verdrängt nicht das allgemeine Kartellrecht** (Art. 1 Abs. 6 DMA): Art. 102 AEUV und § 19a GWB bleiben anwendbar
- **§ 19a GWB ist enger gefasst als DMA**, kann aber Sachverhalte erfassen, die unterhalb der DMA-Schwellen liegen
- **DDG ersetzt NetzDG und Teile des TMG** und implementiert DSA in Deutschland — Aufsicht: BNetzA als Digital Services Coordinator (DSC)

## Weiterleitung an Fachmodule

| Anliegen | Skill |
|---|---|
| VLOP-Designation prüfen | `dsa-vlop-vlose-einordnung-und-pflichten` |
| Gatekeeper-Schwellen | `dma-gatekeeper-schwellen-und-kernplattformdienste` |
| Systemische Risikobewertung | `dsa-art-34-systemische-risikobewertung` |
| Algorithmen-Zugang für Forschung | `dsa-art-40-forschungsdatenzugang-algorithmen` |
| Account-Sperre Mandant | `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` |
| Schnittstellen DSGVO/P2B/GWB | `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` |
| Zustellung an Auslandsplattform | `zustellung-und-vertreter-art-13-dsa-art-37-dma` |
| Klage gegen VLOP-Bescheid | `klage-gegen-vlop-einordnung-art-263-aeuv` |

## Mandantenfrage zuerst klären

Wer hat das Anliegen?

- **Plattform / Unternehmen selbst** → Pflichten-Compliance, ggf. Klage gegen Designation
- **Nutzer / Verbraucher** → Beschwerde, ADR, einstweilige Verfügung, Schadensersatz
- **Wettbewerber** → DMA-Beschwerde bei Kommission, kartellrechtliche Schritte
- **Forscher / Behörde** → Art. 40 DSA, Auskunftsverlangen
- **Geschäftlicher Nutzer (Händler auf Marktplatz)** → P2B-VO, DMA Art. 5/6

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 1–3 DSA (VO 2022/2065) — Sachlicher und territorialer Anwendungsbereich
- Art. 1–3 DMA (VO 2022/1925) — Gatekeeper-Regime
- Art. 2, 6 KI-VO (VO 2024/1689) — AI Act Risikoklassen
- Art. 2–6 NIS-2-RL (RL 2022/2555) — Cybersicherheit
- § 19a GWB — Nationales Digitalrecht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Welcher Akteurstyp ist der Mandant? (Nutzer / Plattformbetreiber / Drittanbieter / Behörde)
2. Welcher Dienst-Typ liegt vor? (Vermittlungsdienst / Hosting / Online-Plattform / VLOP / Gatekeeper)
3. Was ist der konkrete Sachverhalt? (Account-Sperre / Wettbewerb / Datenschutz / KI-Einsatz / Sicherheit)
4. Welcher Rechtsakt ist primär einschlägig?

## Output-Template — Digitalregulierungs-Pyramiden-Check

**Adressat:** Mandant / Kanzlei intern — Tonfall: sachlich-strukturiert

```
Digitalregulierungs-Pyramiden-Check [DATUM]
Sachverhalt: [KURZBESCHREIBUNG]
Akteurstyp: [NUTZER / PLATTFORM / DIENSTEANBIETER]
Dienst-Typ: [VERMITTLUNGSDIENST / HOSTING / ONLINE-PLATTFORM / VLOP / GATEKEEPER]

Einschlägige Rechtsakte:
| Rechtsakt | Einschlaegig | Norm | Besonderheit |
|--------------------|--------------|-----------------|--------------|
| DSA | | Art. [X] | |
| DMA | | Art. [X] | |
| KI-VO | | Art. [X] | |
| NIS-2 | | Art. [X] | |
| DSGVO | | Art. [X] | |
| § 19a GWB | | | |

Empfohlene Vertiefung: → Skill [SPEZIALSKILL]
```

## 2. `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb`

**Fokus:** Schnittstellen zwischen DSA/DMA und DSGVO, P2B-VO und § 19a GWB analysieren: Mehrere Regelwerke treffen gleichzeitig auf einen Sachverhalt. Normen: Art. 2 Abs. 4 DSA (kein Verdrangen DSGVO), Art. 1 Abs. 5 DMA, P2B-VO (EU) 2019/1150 (Plattform-Nutzer-Beziehungen), § 19a GWB (unterhalb DMA-Schwellen). Prüfraster: Konkurrenz DSA/DMA vs. DSGVO vs. P2B-VO, § 19a GWB als Luecken-Fuelung, Mehr-Anker-Strategie für welche Rechtsfolge. Output Schnittstellen-Memo, Anspruchs-Matrix. Abgrenzung: VLOP-Designation siehe dsa-vlop-vlose-einordnung-und-pflichten; Gatekeeper DMA siehe dma-gatekeeper-schwellen-und-kernplattformdienste.

# Schnittstellen — DSA, DMA, DSGVO, P2B-VO und § 19a GWB

## Grundsatz

Die EU-Digitalregulierung ist **kein lex specialis** zur DSGVO oder zum Wettbewerbsrecht. Mehrere Rechtsakte können denselben Sachverhalt erfassen und unterschiedliche Rechtsfolgen auslösen.

## DSA — DSGVO

| Aspekt | DSA | DSGVO |
|---|---|---|
| Schutzgut | Schutz vor illegalen Inhalten, systemischen Risiken | Schutz personenbezogener Daten |
| Aufsicht | DSC + Kommission | Aufsichtsbehörden, EDSA |
| One-Stop-Shop | Nein für VLOP | Ja (Art. 56 DSGVO) |
| Bußgeld | bis 6 % Welt-Umsatz | bis 4 % Welt-Umsatz |

**Schnittpunkte:**

- Profiling und Empfehlungssysteme: Art. 27 + 38 DSA und Art. 22 DSGVO
- Kinderschutz: Art. 28 DSA und Art. 8 DSGVO
- Forschungsdatenzugang: Art. 40 DSA verlangt DSGVO-Konformität
- Transparenz: Art. 39 DSA Werbearchiv und Art. 13/14 DSGVO

**Art. 2 Abs. 4 DSA**: DSA berührt nicht die Anwendung anderer EU-Rechtsakte über audiovisuelle Mediendienste, Urheberrecht, terroristische Online-Inhalte, Verbraucherschutz, Datenschutz **— gleichrangige Anwendung**.

## DMA — Kartellrecht (Art. 101/102 AEUV, GWB)

**Art. 1 Abs. 6 DMA**: DMA gilt **unbeschadet** der Anwendung von Art. 101/102 AEUV und nationaler Wettbewerbsregeln, die einseitiges Verhalten regeln (z. B. § 19a GWB).

**Parallelanwendung:**

- DMA: ex-ante, listenartige Verhaltenspflichten für Gatekeeper
- Kartellrecht: ex-post, Marktmachtmissbrauch, Einzelfallprüfung
- § 19a GWB: ex-ante-light, nur für Unternehmen mit marktübergreifender Bedeutung

**Strategische Hebel für Beschwerdeführer:**

- DMA-Beschwerde an Kommission (Art. 27 DMA): schneller, aber begrenzt auf Gatekeeper-Pflichten
- § 19a GWB an BKartA: erfasst zT mehr Verhaltensweisen, BKartA hat eigene Designations-Verfahren
- Art. 102 AEUV: klassisch, schwerere Beweislast, Schadensersatz nach § 33a GWB

## P2B-VO 2019/1150 — DSA / DMA

**Verordnung (EU) 2019/1150** (Platform-to-Business) regelt das Verhältnis Online-Vermittlungsdienst und Online-Suchmaschine zum **gewerblichen Nutzer**:

| Norm | Pflicht |
|---|---|
| Art. 3 P2B | Klare AGB, Vorab-Information bei Änderungen |
| Art. 4 P2B | Account-Sperre nur mit Begründung und Vorlauf |
| Art. 5 P2B | Ranking-Hauptparameter offenlegen |
| Art. 6 P2B | Nebenwaren / -dienstleistungen offenlegen |
| Art. 7 P2B | Eigene Waren bevorzugen — offenlegen |
| Art. 9 P2B | Datenzugang offenlegen |
| Art. 11 P2B | Internes Beschwerdesystem |
| Art. 12 P2B | Mediation |

P2B gilt für **alle** Online-Vermittlungsdienste, nicht nur Gatekeeper. DSA und DMA überlagern, ersetzen P2B aber nicht.

**Praxisfolge**: Für Händler auf Marktplätzen — sowohl DMA Art. 5 (Anti-Steering) als auch P2B Art. 7 (Eigenpräferenz) zitieren.

## § 19a GWB

- Designation durch BKartA-Beschluss nach **Verfügung über marktübergreifende Bedeutung** (§ 19a Abs. 1 GWB)
- Untersagungsbefugnis für sieben benannte Verhaltensweisen (§ 19a Abs. 2)
- Designations-Beschlüsse für mehrere Big-Tech-Konzerne sind bestandskräftig
- Aktuelle Fälle 2024/25 (BGH KVR / OLG Düsseldorf VI-Kart): Self-Preferencing, Tracking-Pflichten, Konditionenmissbrauch

**Verhältnis zum DMA:** Bei Doppelregulierung ist BKartA verpflichtet, das nationale Verfahren zu führen, wenn nicht ausschließlich Gatekeeper-Pflichten betroffen sind. Bei reinen DMA-Verstößen ist die Kommission allein zuständig (Art. 1 Abs. 7 DMA).

## Mehr-Anker-Strategie

Bei einem Beratungsfall **alle relevanten Anker prüfen**:

| Sachverhalt | Anker 1 | Anker 2 | Anker 3 |
|---|---|---|---|
| Account-Sperre (Verbraucher) | DSA Art. 17–23 | DSGVO Art. 15, 22 | BGB Vertragsstörung + GG Art. 5 mittelbare Drittwirkung |
| Account-Sperre (Händler) | DSA Art. 17–23 | P2B Art. 4, 11 | DMA Art. 6 Abs. 13 (Beendigung KPD) |
| Self-Preferencing | DMA Art. 6 Abs. 2 | P2B Art. 7 | § 19a Abs. 2 Nr. 1 GWB / Art. 102 AEUV |
| Datenverknüpfung über Dienste | DMA Art. 5 Abs. 2 | DSGVO Art. 6 + 9 | § 19a Abs. 2 Nr. 4 GWB |
| Empfehlungssystem | DSA Art. 27, 38 | DSGVO Art. 22 | AI Act je nach Einordnung |
| Werbung politisch | VO 2024/900 | DSA Art. 39 | DSGVO |

## Anwaltliche Praxis

- **Welche Norm hat den schärfsten Hebel?** — Bußgeld, Untersagung, Schadensersatz, Eilrechtsschutz
- **Welche Behörde reagiert am schnellsten?** — BKartA, BNetzA als DSC, BfDI / LDA, Kommission
- **Wer trägt die Beweislast?** — Gerichtsstand, prozessuale Strategie
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 2 Abs. 4 DSA — DSGVO bleibt unberührt
- Art. 1 Abs. 5 DMA — DSGVO bleibt unberührt
- Art. 3–5 P2B-VO (2019/1150) — Transparenz gegenüber gewerblichen Nutzern
- § 19a GWB — Sonderregeln für Unternehmen mit überragender marktübergreifender Bedeutung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Welche Ansprüche kommen in Betracht? (DSGVO-Betroffenenrechte / DSA-Beschwerde / P2B-VO / § 19a GWB)
2. Ist der Anspruchsgegner ein VLOP (DSA) / Gatekeeper (DMA) / Marktbeherrscher (GWB)?
3. Ist der Mandant gewerblicher Nutzer (P2B-VO) oder Privatperson (DSA Art. 20)?
4. Welche Mehrwert-Strategie ist sinnvoll? (parallele Ansprüche aus mehreren Normen)

## Output-Template — Mehrankerstrategie

**Adressat:** Kanzlei intern / Mandant — Tonfall: sachlich-juristisch

```
Mehr-Anker-Strategie Digitalregulierung [DATUM]
Sachverhalt: [KURZBESCHREIBUNG]
Mandant-Rolle: Nutzer / Gewerblicher Nutzer / Wettbewerber

Anspruchs-Matrix:
| Norm | Anspruch | Adressat | Rechtsfolge | Aussichten |
|-----------|-----------------------------|--------------|---------------------|-----------|
| Art. 17 DSA | Begruendungspflicht | Plattform | Wiederherstellung | |
| Art. 20 DSA | Interne Beschwerde | Plattform | Reversierung | |
| Art. 15 DSGVO | Auskunft | Plattform | Datenkopie | |
| P2B-VO Art. 3 | Transparenz | Plattform | Korrektur | |
| § 19a GWB | Missbrauchsabstellung | BKartA | Untersagung | |

Empfohlene Strategie: [BESCHREIBUNG]
Nächste Schritte: [LISTE]
```

## 3. `dma-anti-steering-app-store-design`

**Fokus:** Anti-Steering Pflichten Art. 5 Abs. 4 DMA fuer App-Stores: Entwickler duerfen ausserhalb des Stores informieren, ueber alternative Preise und Zahlwege. Pruefraster: keine Behinderung, keine Strafgebuehr, kein Linkverbot. Apple- und Google-Beispiele, EU-Verfahren. Compliance-Checkliste fuer Gatekeeper und Entwicklerschriftsatz bei Verstoss.

# DMA: Anti-Steering App-Store

## Spezialwissen: DMA: Anti-Steering App-Store
- **Spezialgegenstand:** DMA: Anti-Steering App-Store / dma anti steering app store design. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 5, DMA, EU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
