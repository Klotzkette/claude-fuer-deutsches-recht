---
name: tatbestandsmerkmale-vier-zerlegen
description: "Tatbestandsmerkmale Vier Zerlegen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Tatbestandsmerkmale Vier Zerlegen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Tatbestandsmerkmale Vier Zerlegen** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-tatbestandsmerkmale-dokumentenmatrix-und-lueckenliste` | Tatbestandsmerkmale: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-vier-behoerden-gericht-und-registerweg` | Behörden-, Gerichts- oder Registerweg im Plugin subsumtions-pruefer; prüft welcher Weg zur zuständigen Behörde, zum richtigen Gericht oder zum einschlägigen Register führt. Gibt Normen, Fristen und Zuständigkeitsregeln für die vier klassischen Wege. |
| `spezial-zerlegen-risikoampel-und-gegenargumente` | Zerlegen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Tatbestandsmerkmale Vier Zerlegen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-tatbestandsmerkmale-dokumentenmatrix-und-lueckenliste`

**Fokus:** Tatbestandsmerkmale: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Tatbestandsmerkmale: Dokumentenmatrix, Lückenliste und Nachforderung

## Aufgabe

Dieser Skill erstellt eine Dokumentenmatrix, die jedem Tatbestandsmerkmal die vorhandenen und fehlenden Belege zuordnet. Ergebnis ist eine präzise Lückenliste mit Nachforderungsprioritäten.

## Warum Dokumentenmatrix?

Ohne strukturierte Beleglage-Übersicht:
- Fehlen Beweise für entscheidende Tatbestandsmerkmale (Klagerisiko)
- Sind Schriftsätze angreifbar wegen Pauschalbehauptungen
- Wird Beweislast falsch eingeschätzt
- Verzögert sich die Fallbearbeitung durch ungeordnetes Nachfragen

## Schritt 1 — Tatbestandsmerkmale identifizieren

Alle TBM der Anspruchsgrundlage auflisten:

Beispiel § 280 Abs. 1 BGB (Schadensersatz wegen Pflichtverletzung):
1. Schuldverhältnis (Vertrag, gesetzliches Schuldverhältnis)
2. Pflicht aus dem Schuldverhältnis
3. Pflichtverletzung (Handlung oder Unterlassen)
4. Vertretenmüssen (§ 276 BGB; Vermutung!)
5. Schaden (materiell; immateriell § 253 Abs. 2 BGB)
6. Kausalität (haftungsbegründend: Pflichtverletzung → Schaden; haftungsausfüllend: Schaden → Schadenshöhe)

## Schritt 2 — Dokumentenmatrix erstellen

| Nr. | Tatbestandsmerkmal | Norm | Vorhanden? | Dokument / Beleg | Fundstelle (Anlage) | Lücke |
|---|---|---|---|---|---|---|
| 1 | Schuldverhältnis | § 433 BGB (Kauf) | Ja | Kaufvertrag v. TT.MM | Anlage K1 | — |
| 2 | Pflichtverletzung | § 433 Abs. 1 BGB | Streitig | Lieferschein; Mängelrüge | Anlage K2, K3 | Mängelprotokoll fehlt |
| 3 | Vertretenmüssen | § 276 BGB | Vermutet | — | — | Entlastungsbeweis Beklagter |
| 4 | Schaden | § 249 BGB | Teils | Kostenvoranschlag | Anlage K4 | Abrechnung ausstehend |
| 5 | Kausalität | § 286 ZPO | Offen | — | — | Sachverständigengutachten nötig? |

## Schritt 3 — Lückenliste priorisieren

Prioritäten:
- **Rot (kritisch):** Fehlendes Beweismittel für TBM, das Kläger beweisen muss; ohne Beleg kein Anspruch
- **Gelb (wichtig):** Streitiges TBM mit schwachem Beleg; Beweisrisiko mittel
- **Grün (gesichert):** TBM belegt oder nicht streitig (§ 138 Abs. 3 ZPO: Zugeständnis durch Nichtbestreiten)

## Schritt 4 — Nachforderung formulieren

Muster-Nachforderungsschreiben an Mandanten:

```
Betreff: Fehlende Unterlagen für Ihr Verfahren

Für die Durchsetzung Ihres Anspruchs aus § [Norm] benötigen wir noch folgende Unterlagen:

1. [Dokument A]: Wird benötigt für [Tatbestandsmerkmal X]; bitte bis [Datum] einreichen.
2. [Dokument B]: Wird benötigt für [Tatbestandsmerkmal Y]; alternativ [Zeuge Z] möglich.
3. [Dokument C]: Optionale Verbesserung der Beweislage zu [TBM Z].

Ohne Dokument A ist eine Klageerhebung nicht empfehlenswert.
```

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Anspruchsgrundlage wird geprüft und welche TBM sind einschlägig?
2. Welche Unterlagen hat der Mandant bereits eingereicht?
3. Welche Fristen, Zustellungen oder Schwellen sind kritisch?
4. Welcher Output wird gebraucht: Dokumentenmatrix, Nachforderungsliste, Schriftsatzvorbereitung?

## Arbeitsworkflow

1. **Fallbild bilden:** Norm, Parteien, vorhandene Dokumente und offene Belege in eine kurze Matrix bringen.
2. **Dokumentenmatrix erstellen:** Pro TBM: Beleg, Anlage, Lücke.
3. **Lückenliste priorisieren:** Rot/Gelb/Grün je nach Beweislastlage und Beweisstärke.
4. **Nachforderung formulieren:** Präzise Liste mit Deadlines und Alternativbelegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Dokumentenmatrix:** TBM, Norm, Vorhanden, Beleg, Anlage, Lücke.
- **Lückenliste:** Rot/Gelb/Grün mit Priorität und Nachforderungstext.
- **Qualitätsgate:** keine Scheingenauigkeit; offene Belege immer sichtbar markieren.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (BGB §§ 249, 276, 280; ZPO §§ 138, 286).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `spezial-vier-behoerden-gericht-und-registerweg`

**Fokus:** Behörden-, Gerichts- oder Registerweg im Plugin subsumtions-pruefer; prüft welcher Weg zur zuständigen Behörde, zum richtigen Gericht oder zum einschlägigen Register führt. Gibt Normen, Fristen und Zuständigkeitsregeln für die vier klassischen Wege.

# Behörden-, Gerichts- und Registerweg

## Aufgabe

Dieser Skill bestimmt den richtigen Weg zu Behörde, Gericht oder Register. Er unterscheidet die vier klassischen Wege: ordentliche Gerichtsbarkeit, Verwaltungsgerichtsbarkeit, Registerwege und Behördenwege. Ergebnis ist ein konkreter Wegweiser mit Normen, Fristen und Zuständigkeiten.

## Weg 1 — Ordentliche Gerichtsbarkeit (ZPO, GVG)

**Wann:** Zivilrechtliche Streitigkeiten (§ 13 GVG); Vertragsrecht, Deliktsrecht, Erbrecht, Familienrecht, Handelsrecht.

| Gericht | Zuständigkeit | Norm |
|---|---|---|
| Amtsgericht | bis EUR 5.000; Miete, Unterhalt unabhängig vom Streitwert | §§ 23, 23a GVG |
| Landgericht | ab EUR 5.000; Handelssachen; Kapitalmarkt | § 71 GVG; § 95 GVG |
| Oberlandesgericht | Berufung gegen LG-Urteile; bestimmte erstinstanzliche Verfahren | §§ 119 ff. GVG |
| Bundesgerichtshof | Revision; bestimmte erste Instanz | § 133 GVG |

**Örtliche Zuständigkeit:** §§ 12 ff. ZPO; allgemeiner Gerichtsstand: Wohnsitz des Beklagten (§ 13 ZPO).

## Weg 2 — Verwaltungsgerichtsbarkeit (VwGO)

**Wann:** Öffentlich-rechtliche Streitigkeiten nicht verfassungsrechtlicher Art (§ 40 VwGO); Anfechtung von Verwaltungsakten, Verpflichtungsklagen, Normenkontrolle.

| Verfahren | Klageart | Norm |
|---|---|---|
| Anfechtung VA (z. B. Bußgeldbescheid) | Anfechtungsklage | § 42 Abs. 1 Alt. 1 VwGO |
| Erlass VA (z. B. Genehmigung) | Verpflichtungsklage | § 42 Abs. 1 Alt. 2 VwGO |
| Feststellung Rechtsverhältnis | Feststellungsklage | § 43 VwGO |
| Vorläufiger Rechtsschutz | Antrag §§ 80, 123 VwGO | § 80 Abs. 5 VwGO |

**Vorverfahren:** Widerspruch (§§ 68 ff. VwGO) vor Klageerhebung; Frist: 1 Monat ab Bekanntgabe des VA (§ 70 VwGO); Klagefrist: 1 Monat ab Zustellung Widerspruchsbescheid (§ 74 VwGO).

**Sondergerichte:** Finanzgericht (§ 33 FGO, Steuersachen); Sozialgericht (§ 51 SGG, Sozialversicherung); Arbeitsgericht (§ 2 ArbGG, Arbeitsrecht).

## Weg 3 — Registerwege

| Register | Zuständigkeit | Fundstelle / Abfrage |
|---|---|---|
| Handelsregister | AG am Sitz der Gesellschaft (§ 8 HGB) | handelsregister.de |
| Grundbuch | AG-Grundbuchamt am Lageort (§ 1 GBO) | Grundbucheinsicht über AG oder notar |
| Marken-/Patentregister | DPMA | dpma.de |
| Gewerbezentralregister | Bundesamt für Justiz | bundesjustizamt.de |
| Insolvenzregister | Insolvenzgericht am Sitz | insolvenzbekanntmachungen.de |
| Vereinsregister | AG-Registergericht | handelsregister.de (VR-Abteilung) |

## Weg 4 — Behördenwege

| Behörde | Sachgebiet | Kontakt |
|---|---|---|
| Datenschutzbehörde (Landesbeauftragte) | DSGVO-Beschwerden, Bußgelder | Zuständige Landesdatenschutzbehörde |
| Bundesnetzagentur | Telekommunikation, Post, Energie, Rundfunk | bundesnetzagentur.de |
| Bundesamt für Justiz | GewZR, Kartellbehörde (Teile) | bundesjustizamt.de |
| Bundeskartellamt | Wettbewerbs- und Kartellrecht | bundeskartellamt.de |
| Gewerbeamt | Gewerbeanmeldung, -abmeldung | Kommunale Behörde |
| Finanzamt | Steuerrecht, Umsatzsteuer | Elektronisch via ELSTER |

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Was ist das Ziel (Anspruch durchsetzen, VA anfechten, Register einsehen, Beschwerde einreichen)?
2. Wer ist Gegner (Privatperson, Unternehmen, Behörde)?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Wegweiser, Memo, Checkliste, Entwurf, Schriftsatzbaustein?

## Arbeitsworkflow

1. **Fallbild bilden:** Ziel, Gegner, Behörde/Gericht, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Weg bestimmen:** Ordentliche Gerichtsbarkeit, VwGO, Register oder Behörde?
3. **Fristen prüfen:** Klagefrist, Widerspruchsfrist, Verjährung, Ausschlussfristen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen und Alternativwegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen (z. B. verfahrensart-bestimmen, ziel-und-rechtsweg-bestimmung).

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** Wegweiser mit Normen, Fristen und Zuständigkeiten.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (GVG, ZPO, VwGO, FGO, SGG, ArbGG, GBO, HGB).
- Behördenwebseiten und Register live prüfen (handelsregister.de, dpma.de, bundeskartellamt.de).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-zerlegen-risikoampel-und-gegenargumente`

**Fokus:** Zerlegen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Zerlegen: Risikoampel, Gegenargumente und Verteidigungslinien

## Aufgabe

Dieser Skill zergliedert einen Sachverhalt in seine Risikobestandteile und erstellt eine strukturierte Gegenargument- und Verteidigungslinienanalyse. Ergebnis ist eine dreifarbige Risikoampel mit konkreten Handlungsempfehlungen.

## Risikoampel-Schema

### Rot — Kritisches Risiko

**Definition:** Kein Beleg vorhanden; Beweislast beim Nutzer; Norm eindeutig gegen Nutzer; Verjährung oder Ausschlussfrist droht oder abgelaufen.

**Typische Auslöser:**
- Wesentliches Tatbestandsmerkmal nicht belegt (Sprung-Subsumtion)
- Beweislastumkehr wirkt gegen Nutzer (§ 630h BGB, § 22 AGG, Art. 82 Abs. 3 DSGVO)
- Frist bereits abgelaufen oder noch innerhalb 30 Tage (Verjährung, Anfechtungsfrist, Klagefrist)
- Norm eindeutig nicht einschlägig (falsche Anspruchsgrundlage)

**Sofortmaßnahmen:**
- Frist sichern (Klageerhebung, Verjährungsunterbrechung § 204 BGB)
- Beweismittel sichern (Zeugenvernehmung vor Klage, Urkundenvorlage)
- Mandant auf Risiko hinweisen; Mandate-Akte dokumentieren

### Gelb — Mittleres Risiko

**Definition:** Beleg vorhanden, aber schwach oder streitig; Norm einschlägig, aber Streitstand ungeklärt; Frist noch offen (mehr als 30 Tage).

**Typische Auslöser:**
- Streitstand bei zentralem TBM; BGH-Linie unklar oder divergent
- Beweismittel vorhanden, aber Beweisstärke zweifelhaft (Zeuge befangen; Urkunde echt streitig)
- Einrede der Gegenseite möglich aber noch nicht erhoben
- Verfahrenskosten übersteigen möglichen Gewinn

**Maßnahmen:**
- Zusätzliche Belege beschaffen
- Rechtsprechungsrecherche für streitigen Punkt (→ rechtsprechung-recherche-strategie)
- Vergleichs-/Mediationsoption prüfen

### Grün — Geringes Risiko

**Definition:** Alle TBM belegt; Norm eindeutig einschlägig; keine erheblichen Einreden der Gegenseite erkennbar; Frist gesichert.

**Maßnahme:** Schriftsatz finalisieren; Fristenkontrolle.

## Gegenargumente strukturieren

### Antizipatorische Verteidigungsanalyse

Für jedes vom Nutzer beanspruchte TBM: Was wird die Gegenseite einwenden?

| TBM | Nutzer-Argument | Gegenargument Gegenseite | Entgegnung | Risiko |
|---|---|---|---|---|
| Pflichtverletzung | Lieferung 14 Tage verspätet | Höhere Gewalt (§ 275 Abs. 1 BGB) | Höhere Gewalt nicht belegt; Risiko beim Lieferanten | Gelb |
| Kausalität | Schaden durch Verspätung | Kläger hätte anderweitig beschafft | Beschaffungsalternative nicht zumutbar | Grün |

### Vier Klassen von Gegenargumenten

1. **Tatbestandliche Gegenargumente:** TBM nicht erfüllt (z. B. kein Vertrag; kein Schaden)
2. **Rechtliche Einreden:** Verjährung, § 320 BGB (Zug-um-Zug), Aufrechnung (§ 387 BGB)
3. **Beweisrechtliche Gegenargumente:** Beweismittel unzulässig; Beweislast falsch verteilt
4. **Sachverhaltliche Gegenargumente:** Andere Deutung der Tatsachen; Alternativursache

## Verteidigungslinien

**Primäre Verteidigungslinie:** Tatbestand nicht erfüllt (TBM fehlt).
**Sekundäre Verteidigungslinie:** TBM erfüllt, aber Einrede erhoben (Verjährung, § 320, Aufrechnung).
**Tertiäre Verteidigungslinie:** TBM und Einreden überwunden, aber Schaden / Kausalität bestritten.

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welche Anspruchsgrundlage wird geprüft und welche TBM sind strittig?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen belegen die Punkte?
5. Welcher Output wird gebraucht: Risikoampel, Memo, Gegenargumentation, Verteidigungsstrategie?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Risikoampel erstellen:** Pro TBM: Rot/Gelb/Grün mit Begründung.
3. **Gegenargument-Matrix:** Pro TBM: Gegenargument der Gegenseite, Entgegnung, Risikobewertung.
4. **Verteidigungslinien skizzieren:** Primär, sekundär, tertiär.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Risikoampel:** TBM, Bewertung (Rot/Gelb/Grün), Begründung, Sofortmaßnahme.
- **Gegenargument-Matrix:** TBM, Nutzer-Argument, Gegenargument, Entgegnung.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (BGB §§ 204, 275, 320, 387 ff.; ZPO §§ 286, 294; AGG § 22).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
