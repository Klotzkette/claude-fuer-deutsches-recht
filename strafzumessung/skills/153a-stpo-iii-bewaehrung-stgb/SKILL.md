---
name: 153a-stpo-iii-bewaehrung-stgb
description: "153a Stpo Einstellung Gegen Auflage, 267 Iii Stpo Begruendungsanforderungen Strafurteil, Bewaehrung 56 Stgb Positive Sozialprognose: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# 153A Stpo Einstellung Gegen Auflage, 267 Iii Stpo Begruendungsanforderungen Strafurteil, Bewaehrung 56 Stgb Positive Sozialprognose

## Arbeitsbereich

Dieser Skill bündelt **153A Stpo Einstellung Gegen Auflage, 267 Iii Stpo Begruendungsanforderungen Strafurteil, Bewaehrung 56 Stgb Positive Sozialprognose** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `153a-stpo-einstellung-gegen-auflage` | Einstellung gegen Auflage nach § 153a StPO. Zustimmungserfordernis Staatsanwaltschaft, Gericht und Beschuldigter. Voraussetzung kein oeffentliches Interesse an der Strafverfolgung Vergehen. Auflagen Geldzahlung gemeinnuetzige Arbeit Schadenswiedergutmachung Unterhaltspflicht TOA. Verhaeltnis zur Strafzumessung; Wirkung wie eine kuenftige Strafbefehlsersatzhandlung. |
| `267-iii-stpo-begruendungsanforderungen-strafurteil` | Begruendungsanforderungen an die Strafzumessung im Strafurteil § 267 Abs. 3 StPO. Pflicht zur Mitteilung der bestimmenden Strafzumessungsgruende. Strafrahmen, Schuldrahmen, Strafzumessungstatsachen § 46 Abs. 2 StGB. Bewaehrungs- und Strafaussetzungsbegruendung. Strafzumessungsruege im Revisionsverfahren. Typische Aufhebungsgruende: Pauschalbegruendung Doppelverwertung Schweigen Praevention vor Schuld. |
| `bewaehrung-56-stgb-positive-sozialprognose` | Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Voraussetzungen positive Sozialprognose Abs. 1 bis 1 Jahr; besondere Umstaende Abs. 2 bis 2 Jahre; Verteidigung der Rechtsordnung Abs. 3. Prognose-Faktoren Vorleben, soziale Bindungen, Reue, Wiedergutmachung, Therapiebereitschaft. Bewaehrungszeit § 56a. Auflagen Weisungen. Schnittstelle 267 Abs. 3 StPO. |

## Arbeitsweg

Für **153A Stpo Einstellung Gegen Auflage, 267 Iii Stpo Begruendungsanforderungen Strafurteil, Bewaehrung 56 Stgb Positive Sozialprognose** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `strafzumessung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `153a-stpo-einstellung-gegen-auflage`

**Fokus:** Einstellung gegen Auflage nach § 153a StPO. Zustimmungserfordernis Staatsanwaltschaft, Gericht und Beschuldigter. Voraussetzung kein oeffentliches Interesse an der Strafverfolgung Vergehen. Auflagen Geldzahlung gemeinnuetzige Arbeit Schadenswiedergutmachung Unterhaltspflicht TOA. Verhaeltnis zur Strafzumessung; Wirkung wie eine kuenftige Strafbefehlsersatzhandlung.

# Einstellung gegen Auflage — § 153a StPO

## Worum geht es?

§ 153a StPO erlaubt die Einstellung des Verfahrens **gegen Auflagen oder Weisungen**, wenn das oeffentliche Interesse an der Strafverfolgung beseitigt werden kann und die Schwere der Schuld nicht entgegensteht. Es bedarf der Zustimmung des Beschuldigten, des Gerichts (im gerichtlichen Stadium) und der Staatsanwaltschaft. Mit Erfuellung der Auflage ist die Tat **nicht mehr** verfolgbar (Verbrauch der Strafklage in dem Umfang).

## Wann brauchen Sie diese Skill?

- Sie sondieren eine Einstellung mit Staatsanwaltschaft oder Gericht.
- Sie pruefen, ob die Schwere der Schuld den Weg ueber § 153a StPO oeffnet oder versperrt.
- Sie verhandeln die Hoehe der Geldauflage und vergleichen sie mit der drohenden Geldstrafe.

## Rechtliche Grundlagen

- **§ 153a Abs. 1 StPO** — Vorlaeufige Einstellung mit Auflagen durch die Staatsanwaltschaft (mit Zustimmung des Gerichts, ab dem Zwischenverfahren bereits Gerichts-Zustimmung).
- **§ 153a Abs. 2 StPO** — Einstellung durch das Gericht in jedem Stadium.
- **§ 153a Abs. 3 StPO** — Auflagenkatalog:
 - Nr. 1: Wiedergutmachung des Schadens.
 - Nr. 2: Geldbetrag an gemeinnuetzige Einrichtung oder Staatskasse.
 - Nr. 3: Sonstige gemeinnuetzige Leistung.
 - Nr. 4: Unterhaltsleistung.
 - Nr. 5: Taeter-Opfer-Ausgleich, § 46a StGB.
 - Nr. 6: Verkehrserziehungsmassnahme.
 - Nr. 7: Beratungs-/Therapiemassnahme.
- **§ 153 StPO** — Einstellung **ohne** Auflage bei Geringfuegigkeit (Bagatelle).

## Strafzumessungs-Grundsatz

§ 153a StPO ist **keine** Strafe; daher kein BZRG-Eintrag, kein Vorstrafenstatus. Aber:

- Die Auflagenhoehe orientiert sich faktisch an der **drohenden Strafe**.
- Daumenregel: Geldauflage entspricht ungefaehr der Geldstrafe, die bei Verurteilung gedroht haette.
- Anrechnung von Geldauflage auf eine spaeter doch verhaengte Strafe nach § 153a Abs. 1 Satz 6 StPO (bei Wiederaufnahme).

## Voraussetzungen

1. **Vergehen** (keine Verbrechen).
2. **Schwere der Schuld** steht nicht entgegen.
3. **Auflage** ist geeignet, das oeffentliche Interesse zu beseitigen.
4. **Zustimmung** Beschuldigter + Gericht + Staatsanwaltschaft.

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Eignung pruefen**:
 - Vergehen? Strafdrohung max. 5 Jahre Freiheitsstrafe oder Geldstrafe (allgemein).
 - Schwere der Schuld vertretbar? Bei einschlaegigen Vorbelastungen oft schwierig.
2. **Auflagenpaket** mit Mandant abstimmen:
 - Schadenswiedergutmachung: vorrangig.
 - Geldauflage: Hoehe realistisch (i.d.R. 500-15 000 EUR; bei Wirtschaftsstrafsachen hoeher).
 - Gemeinnuetzige Arbeit als Alternative.
 - TOA wenn moeglich.
3. **Verhandlung** mit Staatsanwaltschaft / Gericht:
 - Schriftlicher Vorschlag mit konkretem Auflagenpaket.
 - Begruendung: warum oeffentliches Interesse beseitigt ist.
 - Kompensation gegenueber drohender Strafe darstellen.
4. **Belehrung** des Mandanten: Zustimmung wird mit Verbrauch der Strafklage ueber den **abgegrenzten Tatvorwurf** wirksam; keine spaetere Strafverfolgung dieses Vorwurfs.
5. **Erfuellungsnachweis** sichern: Zahlungsbeleg, Stundenkarte gemeinnuetzige Arbeit, TOA-Bestaetigung. Erfuellung innerhalb der gesetzten Frist (verlaengerbar nach § 153a Abs. 1 Satz 4 StPO).

## Schritt-fuer-Schritt-Anleitung (Anklage)

- **§ 153 StPO** bei Bagatellen; ohne Auflage.
- **§ 153a StPO** bei mittlerer Schwere mit Auflage.
- Bei Anklage **trotz** Einigungsspielraum: Begruendung der "oeffentlichen Interesse"-Erforderlichkeit.

## Wirkung der Einstellung

- **Strafklageverbrauch** in Bezug auf den abgegrenzten Vorwurf.
- **Kein BZRG-Eintrag**.
- Berufsrechtliche Folgen oft minimal (im Vergleich zur Verurteilung).
- Bei **Nichterfuellung**: Wiederaufnahme des Verfahrens; gezahlte Geldauflage wird angerechnet (§ 153a Abs. 1 Satz 6 StPO).

## Vergleich Strafbefehl vs. § 153a StPO

| Merkmal | Strafbefehl | § 153a StPO |
|---|---|---|
| Schuldspruch | ja | nein |
| BZRG-Eintrag | ja | nein |
| Sanktion | Geldstrafe / Bewaehrung | Auflage |
| Vorstrafe | ja | nein |
| Beschleunigung | ja | ja |
| Hoehe Geld | Tagessatze x Zahl | i.d.R. aehnlich, oft etwas hoeher |

## Typische Fehler

- **Schwere der Schuld** uebersehen: Bei Wiederholungstaetern oder hoher Schadenshoehe ist § 153a STO oft nicht moeglich.
- **Auflagenerfuellung** versaeumt: Verfahren wird wiederaufgenommen.
- **Zustimmung** vor Mandantenbelehrung: Unterschrift ohne Konsequenz-Verstaendnis.
- **Auflagenhoehe** zu niedrig angesetzt: Staatsanwaltschaft / Gericht lehnen ab.
- **TOA-Anbau** ungenutzt: Kombination § 153a + TOA-Auflage bringt oft das Gericht zur Zustimmung.

## Querverweise

- `strafbefehl-strafzumessung-407-stpo` — Alternative.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — TOA als Auflage.
- `verstaendigung-257c-stpo-strafzumessung` — Verstaendigung als Alternative.
- Plugin `strafbefehl-verteidiger`: `strafbefehl-einstellung-153-153a-170`.
- Plugin `fachanwalt-strafrecht`: `vergleichsverhandlung-strategie`.

## Quellen und Stand 05/2026

- §§ 153, 153a StPO in der geltenden Fassung.
- § 46a StGB.
- Quellenregel: vgl. `references/zitierweise.md`.

## 2. `267-iii-stpo-begruendungsanforderungen-strafurteil`

**Fokus:** Begruendungsanforderungen an die Strafzumessung im Strafurteil § 267 Abs. 3 StPO. Pflicht zur Mitteilung der bestimmenden Strafzumessungsgruende. Strafrahmen, Schuldrahmen, Strafzumessungstatsachen § 46 Abs. 2 StGB. Bewaehrungs- und Strafaussetzungsbegruendung. Strafzumessungsruege im Revisionsverfahren. Typische Aufhebungsgruende: Pauschalbegruendung Doppelverwertung Schweigen Praevention vor Schuld.

# Begruendung der Strafzumessung im Urteil — § 267 Abs. 3 StPO

## Worum geht es?

Das Strafurteil muss die **bestimmenden** Strafzumessungsgruende in seinen Gruenden mitteilen (§ 267 Abs. 3 Satz 1 StPO). Diese Begruendung ist Voraussetzung fuer die revisionsrechtliche Pruefung der Strafzumessung. Bei Versagung der Bewaehrung sind die Gruende ausdruecklich darzulegen (§ 267 Abs. 3 Satz 4 StPO).

## Wann brauchen Sie diese Skill?

- Sie schreiben einen Urteilsentwurf als Richter oder Berichterstatter.
- Sie pruefen ein Urteil revisionsmaessig auf Strafzumessungsfehler.
- Sie reviewen die Strafzumessungsbegruendung im Ausbildungs- oder Qualitaetskontext.

## Rechtliche Grundlagen

- **§ 267 Abs. 3 Satz 1 StPO** — Mitteilung der bestimmenden Strafzumessungsgruende.
- **§ 267 Abs. 3 Satz 2 StPO** — Bei Geldstrafe Tagessatzhoehe und -anzahl.
- **§ 267 Abs. 3 Satz 4 StPO** — Bei Versagung der Bewaehrung Mitteilung der Gruende.
- **§ 267 Abs. 3 Satz 5 StPO** — Bei Verstaendigung Mitteilung von Inhalt und Belehrung.
- **§ 46 Abs. 1, 2, 3 StGB** — Materielle Pflicht-Inhalte.
- **§ 337 StPO** — Revision wegen Rechtsverletzung; Strafzumessung kann mit Sach- oder Verfahrensruege angegriffen werden.

## Strafzumessungs-Grundsatz

Die Begruendung muss:

- den **Strafrahmen** angeben (Grundtatbestand, Modifikation durch Regelbeispiel oder minder schweren Fall, § 49-Milderung);
- die **bestimmenden** Strafzumessungstatsachen (§ 46 Abs. 2 StGB) nennen;
- die **Abwaegung** zwischen strafmildernden und strafschaerfenden Faktoren erkennbar machen;
- bei **Geldstrafe** die Tagessatzanzahl und -hoehe getrennt begruenden (§ 267 Abs. 3 Satz 2 StPO);
- bei **Versagung der Bewaehrung** die negative Sozialprognose oder andere Gruende darlegen (§ 267 Abs. 3 Satz 4 StPO);
- bei **Verstaendigung** Inhalt und Belehrung mitteilen (§ 267 Abs. 3 Satz 5 StPO).

## Struktur einer Strafzumessungsbegruendung (Muster)

```
III. Strafzumessung

1. Strafrahmen
 Der Strafrahmen ergibt sich aus § ... StGB
 ([Strafrahmen]). [Ggf. Regelbeispiel / minder schwerer Fall
 / § 49 StGB-Milderung]. Daraus ergibt sich der konkrete
 Strafrahmen von [...] bis [...].

2. Strafzumessungstatsachen (§ 46 Abs. 2 StGB)

 a) Zugunsten des Angeklagten

 [Konkrete Tatsachen, z.B. Gestaendnis, Reue, TOA,
 Schadenswiedergutmachung, Erstverstoss, lange Verfahrens-
 dauer (Art. 6 EMRK), persoenliche Verhaeltnisse].

 b) Zulasten des Angeklagten

 [Konkrete Tatsachen, z.B. Vorstrafen einschlaegig,
 Tatfolgen ueberdurchschnittlich, Tatbeteiligung mehrerer].

3. Gesamtabwaegung
 Unter Wuerdigung der genannten Umstaende hat das Gericht
 eine [Strafart] von [Strafmass] verhaengt.

4. Strafaussetzung zur Bewaehrung [oder: keine Aussetzung]
 [Sozialprognose und Begruendung].

5. Anrechnung U-Haft (§ 51 StGB)
 [Tage].

6. [Bei Verstaendigung]
 Hinweis nach § 257c Abs. 5 StPO erfolgte am [Datum].
 Inhalt der Verstaendigung: [...].
```

## Typische revisionsrechtliche Pruefpunkte

### Pauschalbegruendung

- "Unter Beruecksichtigung aller Umstaende" ohne Einzelabwaegung — revisionsanfaellig.
- BGH st. Rspr.; Aktenzeichen verifizieren.

### Doppelverwertung (§ 46 Abs. 3 StGB)

- Tatbestandsmerkmale duerfen nicht erneut strafschaerfend angefuehrt werden.
- Z.B. bei § 224 Abs. 1 Nr. 2 StGB darf das Tatmittel "Messer" nicht erneut schaerfen.

### Schweigen strafschaerfend

- Schweigen des Angeklagten darf nicht zum Nachteil verwertet werden (st. Rspr.).

### Praevention vor Schuld

- Die Strafe darf nicht aus generalpraeventiven Gruenden ueber den Schuldrahmen hinaus erhoeht werden.

### Bewaehrungsversagung ohne Begruendung

- § 267 Abs. 3 Satz 4 StPO: bei Versagung Bewaehrung muessen die Gruende mitgeteilt werden.

### Strafrahmen nicht angegeben

- Konkreter Strafrahmen muss benannt werden, sonst kann das Revisionsgericht die Schuldangemessenheit nicht pruefen.

### Verstaendigung ohne Mitteilung

- § 267 Abs. 3 Satz 5 StPO und § 273 Abs. 1a StPO: Inhalt und Belehrung muessen mitgeteilt werden.

### Tagessatzhoehe ohne Begruendung

- § 267 Abs. 3 Satz 2 StPO: Tagessatzanzahl und -hoehe getrennt darstellen.

### Lange Verfahrensdauer

- Art. 6 EMRK; Kompensation muss konkret bezeichnet werden (Vollstreckungsmodell).

## Schritt-fuer-Schritt-Anleitung (Verteidigung / Revisionsruege)

1. **Urteilsgruende** durchlesen, Strafzumessungsteil markieren.
2. **Strafrahmen-Pruefung**: Hat das Gericht den richtigen Strafrahmen angegeben?
3. **§ 46 Abs. 2 StGB Pruefung**: Sind die bestimmenden Strafzumessungstatsachen genannt?
4. **§ 46 Abs. 3 StGB**: Doppelverwertung?
5. **Schweigen**: Wird es strafschaerfend gewertet?
6. **Bewaehrung**: Ist die Versagung begruendet?
7. **Verstaendigung**: Mitteilung erfolgt?
8. **Tagessatzhoehe**: Begruendet?
9. **Strafzumessungsruege** formulieren als Sachruege im Revisionsverfahren; bei Verfahrensfehler als Verfahrensruege.

## Schritt-fuer-Schritt-Anleitung (Urteilsverfasser)

1. **Strafrahmen** explizit nennen.
2. **§ 46 Abs. 2 StGB Katalog** abarbeiten: jede einschlaegige Tatsache mit Belegstelle der Beweisaufnahme.
3. **Abwaegung** transparent: nicht nur Auflistung, sondern Gewichtung.
4. **Konkrete Strafe** im Schuldrahmen begruenden.
5. **Bewaehrungsentscheidung** ausdruecklich begruenden.
6. **U-Haft-Anrechnung** ausweisen.
7. **Verstaendigung** mitteilen, falls einschlaegig.
8. **§ 46 Abs. 3 StGB** im Hinterkopf: Tatbestandsmerkmale nicht erneut verwerten.

## Typische Fehler

- Strafzumessungs-Begruendung **vor** dem Strafmass — Reihenfolge muss sein: Strafrahmen, Abwaegung, Mass.
- **Pauschalbegruendung** mit Floskeln.
- **Doppelverwertung**.
- **Schweigen** strafschaerfend.
- **Tagessatzhoehe** ohne Einkommens-Begruendung.
- **Verstaendigung** ohne Mitteilung im Urteil (§ 267 Abs. 3 Satz 5 StPO).
- **U-Haft-Anrechnung** vergessen.

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Grundsatz.
- `strafzumessungs-tatsachen-46-ii-stgb` — Katalog.
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung.
- `verstaendigung-257c-stpo-strafzumessung` — Verstaendigung.
- Plugin `fachanwalt-strafrecht`: `fachanwalt-strafrecht-revisionsbegruendung`.
- Plugin `urteilsbauer-relationsmacher` — Urteilsformulierung.

## Quellen und Stand 05/2026

- § 267 Abs. 3 StPO in der geltenden Fassung.
- §§ 46, 51 StGB.
- §§ 257c, 273 Abs. 1a, 337 StPO.
- Art. 6 EMRK.
- Quellenregel: vgl. `references/zitierweise.md`.

## 3. `bewaehrung-56-stgb-positive-sozialprognose`

**Fokus:** Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Voraussetzungen positive Sozialprognose Abs. 1 bis 1 Jahr; besondere Umstaende Abs. 2 bis 2 Jahre; Verteidigung der Rechtsordnung Abs. 3. Prognose-Faktoren Vorleben, soziale Bindungen, Reue, Wiedergutmachung, Therapiebereitschaft. Bewaehrungszeit § 56a. Auflagen Weisungen. Schnittstelle 267 Abs. 3 StPO.

# Strafaussetzung zur Bewaehrung — § 56 StGB

## Worum geht es?

§ 56 StGB ermoeglicht, Freiheitsstrafen unter zwei Jahren zur Bewaehrung auszusetzen. Es ist die zentrale Weiche fuer das spaetere Verhalten des Verurteilten und das wichtigste Verteidigungs-Ziel bei Freiheitsstrafen nahe der Bewaehrungsschwelle.

## Wann brauchen Sie diese Skill?

- Sie verteidigen gegen eine drohende Freiheitsstrafe und wollen Bewaehrung sichern.
- Sie strukturieren das Plaedoyer um die Sozialprognose.
- Sie pruefen ein Urteil ohne Bewaehrung auf Revisionsangriff.
- Sie planen die Bewaehrungsverhandlung mit dem Mandanten (Auflagen, Weisungen, Bewaehrungshelfer).

## Rechtliche Grundlagen

- **§ 56 Abs. 1 StGB** — Aussetzung von Strafe bis 1 Jahr bei positiver Sozialprognose: Es muss zu erwarten sein, dass der Verurteilte sich schon die Verurteilung zur Warnung dienen lassen wird und kuenftig auch ohne die Einwirkung des Strafvollzugs keine Straftaten mehr begehen wird.
- **§ 56 Abs. 2 StGB** — Aussetzung von Strafe bis 2 Jahre nur bei **besonderen Umstaenden** in der Tat und in der Persoenlichkeit des Verurteilten.
- **§ 56 Abs. 3 StGB** — Aussetzung kann versagt werden, wenn die **Verteidigung der Rechtsordnung** die Vollstreckung gebietet (Strafe von mindestens 6 Monaten).
- **§ 56a StGB** — Bewaehrungszeit 2 bis 5 Jahre, mindestens 2 Jahre.
- **§ 56b, 56c StGB** — Auflagen und Weisungen; vgl. `bewaehrung-auflagen-und-weisungen-56b-c-stgb`.
- **§ 56f StGB** — Widerruf; vgl. `bewaehrungswiderruf-56f-stgb`.
- **§ 56g StGB** — Erlass der Strafe nach Bewaehrungsablauf.

## Strafzumessungs-Grundsatz

Bewaehrung ist **Regelfall** bei Strafe bis 1 Jahr, sofern Sozialprognose positiv ist. Bei Strafe bis 2 Jahre ist Bewaehrung Ausnahme; es muessen **besondere Umstaende** vorliegen.

## Prognose-Faktoren (positiv)

- **Persoenlichkeit**: stabile Lebensfuehrung, keine Vorstrafen, sozial integriert.
- **Vorleben**: keine einschlaegigen Vorstrafen; lange straffreie Zeit.
- **Tatumstaende**: erstmaliger Verstoss, niedrige kriminelle Energie, Notlage.
- **Verhalten nach der Tat**: Reue, Gestaendnis, Schadenswiedergutmachung, TOA (§ 46a StGB), Therapie- oder Suchtberatung in Anspruch genommen.
- **Soziale Bindungen**: Familie, Beruf, fester Wohnsitz, Bindung an Kinder.
- **Lebensplanung**: Ausbildung, Arbeitsstelle, Aussicht auf Stabilitaet.

## Prognose-Faktoren (negativ)

- Einschlaegige Vorbelastung, Wiederholungstaeter.
- Bewaehrungs-Versager in der Vorgeschichte.
- Aktuelle Sucht ohne Therapie.
- Tat in laufender Bewaehrung.
- Fehlende Einsicht oder Vermeidung von Auseinandersetzung.

## "Besondere Umstaende" iSv § 56 Abs. 2 StGB

Bei Strafe ueber 1 bis 2 Jahre. Erforderlich sind Umstaende, die das Gewicht der drohenden Vollstreckung **deutlich** mindern. Typisch:

- Massive Tatfolgen schon beim Taeter (Behinderung, Verstuemmelung in Tatzusammenhang).
- Hohe Strafempfindlichkeit (Sucht-Therapieaufenthalt droht abzubrechen, schwere familiaere Belastung).
- Sehr lange Verfahrensdauer (Vollstreckungsmodell).
- Aussergewoehnliches Nachtatverhalten (komplette Wiedergutmachung, dauerhafte Therapie).

## "Verteidigung der Rechtsordnung" iSv § 56 Abs. 3 StGB

Restriktive Auslegung der st. Rspr.: Nicht jede mediale Empoerung; erforderlich sind besondere Tatumstaende, die das Vertrauen der Allgemeinheit in die Geltung der Rechtsordnung beruehren. **Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.**

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Strafmass-Schwelle** im Blick: Ziel 11 Monate oder 1 Jahr 11 Monate, je nach Konstellation.
2. **Prognose-Vortrag** vorbereiten: Beweise und Beleg sammeln (Arbeitsvertrag, Mietvertrag, Therapiebescheinigung, Schulbestaetigung).
3. **Sozialbericht** der Bewaehrungshilfe anregen, wenn das hilft (§ 56d StGB Bewaehrungshelfer; auch vorab anhoerend).
4. **Konkret beantragen**: "Wir beantragen, die Strafe nach § 56 Abs. [1/2] StGB zur Bewaehrung auszusetzen. Sozialprognose ist positiv, weil [...]."
5. **Auflagenangebote** vorbereiten (Zahlung an gemeinnuetzige Einrichtung, Therapie, Wiedergutmachung); vgl. `bewaehrung-auflagen-und-weisungen-56b-c-stgb`.
6. **Hilfsweise Reststrafenaussetzung** nach § 57 StGB ansprechen, falls Bewaehrung in erster Instanz nicht zugesprochen wird.

## Schritt-fuer-Schritt-Anleitung (Anklage)

- Bei Strafantrag ohne Bewaehrung: konkrete Begruendung, warum Sozialprognose negativ ist.
- Bei Strafe ueber 1 Jahr und bis 2 Jahre Bewaehrung: konkrete Begruendung, warum keine besonderen Umstaende vorliegen.
- "Verteidigung der Rechtsordnung" sparsam und nur bei konkreten Anhaltspunkten.

## Begruendungspflicht des Gerichts

Wird Bewaehrung **versagt**, muss das Urteil im Strafzumessungsteil konkret darlegen, warum die Sozialprognose negativ ist (§ 267 Abs. 3 Satz 4 StPO). Pauschale Wendungen reichen nicht.

## Typische Fehler

- **Pauschale Prognose** ohne Tatsachenbasis (Verteidigung wie Gericht).
- **Bewaehrung bei Strafe ueber 2 Jahren** beantragt: rechtlich ausgeschlossen.
- **Auflagen/Weisungen** im Bewaehrungsbeschluss nicht ausdifferenziert: Mandant uebersieht Risiko des Widerrufs.
- **Sucht ohne Therapie**: Bewaehrung ohne stoffspezifische Therapieweisung ist riskant.
- **Verfahrensdauer-Kompensation** vergessen.

## Querverweise

- `freiheitsstrafe-strafmass-pruefen` — vor Bewaehrungsfrage.
- `bewaehrung-auflagen-und-weisungen-56b-c-stgb` — Auflagen / Weisungen.
- `bewaehrungswiderruf-56f-stgb` — bei Widerruf.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Begruendungspflicht.
- Plugin `fachanwalt-strafrecht` — Plaedoyer-Vorbereitung.

## Quellen und Stand 05/2026

- §§ 56, 56a-g, 57, 57a StGB in der geltenden Fassung.
- § 267 Abs. 3 Satz 4 StPO.
- BGH-Linie zu "Verteidigung der Rechtsordnung" — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.
