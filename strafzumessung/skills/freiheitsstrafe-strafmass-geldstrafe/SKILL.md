---
name: freiheitsstrafe-strafmass-geldstrafe
description: "Freiheitsstrafe Strafmass Geldstrafe: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Freiheitsstrafe Strafmass Geldstrafe

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Freiheitsstrafe Strafmass Geldstrafe** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `freiheitsstrafe-strafmass-pruefen` | Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB. Strafrahmen pruefen, Strafhoehe innerhalb des Schuldrahmens bestimmen, Wechselwirkung mit Bewaehrung (§ 56 StGB) und Aussetzung des Strafrests (§ 57 StGB). Faustwerte fuer typische Tatbestaende. Schnittstelle Verteidigungsplaedoyer, Antragsstrafe Staatsanwaltschaft, Urteilsbegruendung. |
| `geldstrafe-tagessatzanzahl-bestimmen` | Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs. 1 StGB. 5 bis 360 Tagessaetze als Grundgrenze; bei Gesamtgeldstrafe bis 720 Tagessaetze. Die Anzahl bildet die Schuldkomponente und folgt § 46 StGB. Abgrenzung zur Tagessatzhoehe, die das Nettoeinkommen abbildet. Schnittstelle Strafbefehl, Hauptverhandlung, Gesamtstrafe. |
| `geldstrafe-vs-freiheitsstrafe-47-stgb` | Vorrang der Geldstrafe vor kurzer Freiheitsstrafe nach § 47 StGB. Kurze Freiheitsstrafe unter 6 Monaten nur bei besonderen Umstaenden in der Tat oder in der Persoenlichkeit. Begruendungspflicht des Gerichts. Verhaeltnis Geldstrafe + Freiheitsstrafe (§ 41 StGB). Strategiewahl Verteidigung gegen kurze Freiheitsstrafe; Umstellungsantrag in Geldstrafe; Bewaehrungsperspektive. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Freiheitsstrafe Strafmass Geldstrafe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `freiheitsstrafe-strafmass-pruefen`

**Fokus:** Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB. Strafrahmen pruefen, Strafhoehe innerhalb des Schuldrahmens bestimmen, Wechselwirkung mit Bewaehrung (§ 56 StGB) und Aussetzung des Strafrests (§ 57 StGB). Faustwerte fuer typische Tatbestaende. Schnittstelle Verteidigungsplaedoyer, Antragsstrafe Staatsanwaltschaft, Urteilsbegruendung.

# Freiheitsstrafe — Strafmass pruefen

## Worum geht es?

Sobald feststeht, dass Freiheitsstrafe verhaengt wird, ist innerhalb des konkreten Strafrahmens die **Hoehe** zu bestimmen. Grundlage ist § 46 StGB. § 38 StGB regelt die zeitige Freiheitsstrafe (1 Monat bis 15 Jahre), § 39 StGB die Bemessung (Monate, Jahre und Monate). Die Hoehe entscheidet ueber Bewaehrungsfaehigkeit (§§ 56, 57 StGB).

## Wann brauchen Sie diese Skill?

- Sie verteidigen in der Hauptverhandlung und plaedieren auf konkrete Strafhoehe.
- Sie pruefen den Strafantrag der Staatsanwaltschaft auf Angemessenheit.
- Sie sondieren eine Verstaendigung; Strafrahmen-Untergrenze und -Obergrenze bilden den Handlungsspielraum.
- Sie schreiben die Strafzumessung im Urteil oder pruefen sie revisionsmaessig.

## Rechtliche Grundlagen

- **§ 38 StGB** — Zeitige Freiheitsstrafe 1 Monat bis 15 Jahre; lebenslang.
- **§ 39 StGB** — Bemessung: bis 1 Jahr in vollen Wochen und Monaten; ueber 1 Jahr in Jahren und Monaten.
- **§ 46 StGB** — Grundsatz; vgl. `paragraph-46-stgb-grundsatz-strafzumessung`.
- **§ 47 StGB** — Vorrang Geldstrafe bei kurzer Freiheitsstrafe; vgl. `geldstrafe-vs-freiheitsstrafe-47-stgb`.
- **§ 56 StGB** — Aussetzung zur Bewaehrung; vgl. `bewaehrung-56-stgb-positive-sozialprognose`.
- **§ 57 StGB** — Aussetzung des Strafrests bei zeitiger Freiheitsstrafe.
- **§ 57a StGB** — Aussetzung des Strafrests bei lebenslanger Freiheitsstrafe (besondere Schwere der Schuld § 57a Abs. 1 Satz 1 Nr. 2 StGB).

## Strafzumessungs-Grundsatz

- **Spielraum schuldangemessener Strafe**: Ober- und Untergrenze; innerhalb davon nach Praevention bemessen.
- **Wechselwirkung Strafhoehe und Bewaehrung**:
 - Bis 1 Jahr: Bewaehrung Regelfall bei positiver Sozialprognose (§ 56 Abs. 1 StGB).
 - 1 bis 2 Jahre: Bewaehrung moeglich, aber nur bei besonderen Umstaenden (§ 56 Abs. 2 StGB).
 - Ueber 2 Jahre: keine Bewaehrung mehr.
- Verteidigung achtet darauf, ob ein Strafmass moeglichst unter 2 Jahre (und idealerweise unter 1 Jahr) liegt.

## Schritt-fuer-Schritt-Anleitung

1. **Konkreten Strafrahmen** feststellen (vgl. `strafrahmen-und-strafzumessungsstufen`).
2. **Schuldrahmen-Spielraum** bilden: untere und obere Grenze schuldangemessener Strafe.
3. **Strafzumessungstatsachen** aus § 46 Abs. 2 StGB sammeln und gewichten (vgl. `strafzumessungs-tatsachen-46-ii-stgb`).
4. **Strafmilderungsgruende** pruefen: §§ 46a, 17, 21, 23 Abs. 2, 27 Abs. 2, 28 Abs. 1, 49 StGB.
5. **Bewaehrungsperspektive** im Blick: Wenn 1-Jahres- oder 2-Jahres-Schwelle in Reichweite, Argumente entsprechend ausrichten.
6. **Lange Verfahrensdauer** als Kompensationsfaktor pruefen (Art. 6 EMRK; Vollstreckungsmodell der st. Rspr.).
7. **Anrechnung** U-Haft / Auslieferungshaft nach § 51 StGB; vgl. `freiheitsstrafe-ohne-bewaehrung-vollstreckung`.

## Faustwerte (orientierend, kein Praejudiz)

| Tatbestandsbereich | Typischer Bereich |
|---|---|
| Einfacher Diebstahl § 242 Erstverstoss | 30-90 Tagessaetze; selten Freiheitsstrafe |
| Wohnungseinbruchsdiebstahl § 244 Abs. 4 (Mindeststrafe 1 Jahr) | 1 bis 3 Jahre |
| Betrug § 263 mittlere Schaeden | Geldstrafe bis 1 Jahr |
| Betrug § 263 schwere Schaeden / gewerbsmaessig | 1 bis 3 Jahre |
| Koerperverletzung § 223 ohne Vorbelastung | Geldstrafe bis 6 Monate |
| Gefaehrliche Koerperverletzung § 224 | 6 Monate bis 3 Jahre |
| Schwere Koerperverletzung § 226 | 1 Jahr bis 10 Jahre |
| Raub § 249 Abs. 1 | Mindeststrafe 1 Jahr, oft 2-4 Jahre |
| Schwerer Raub § 250 Abs. 1 | 3 bis 6 Jahre |
| Totschlag § 212 | 5 bis 15 Jahre |
| Mord § 211 | lebenslang |

Diese Werte ersetzen **keinen** Einzelfall; sie zeigen, wo regional, gerichtsbezogen und individuell zumeist Verhandlungsraum liegt.

## Verteidigungs-Hebel

- Strafmilderungsgruende konsequent aufzeigen: §§ 46a, 17, 21 StGB.
- Lange Verfahrensdauer ruegen und Kompensation einfordern.
- Bewaehrungsperspektive sichern: Argumente zur Sozialprognose vorbereiten.
- Wirtschaftliche und persoenliche Verhaeltnisse substantiiert vortragen.

## Antrags-Strategie Staatsanwaltschaft

- Antragstrafe darf nicht hinter der Schuld zurueckbleiben.
- Bei Bewaehrungsantrag konkret Vortrag zur Sozialprognose.
- Bei keinem Bewaehrungsantrag konkret zu den negativen Prognosefaktoren.
- Strafzumessungsrichtlinien der Landes-Justizverwaltungen koennen orientieren (siehe je nach Bundesland; nicht bindend).

## Typische Fehler

- **Schuldrahmen-Begruendung fehlt**: Urteil nennt nur den konkret verhaengten Wert ohne Bandbreite; revisionsanfaellig.
- **Bewaehrungsschwelle** uebersehen: Strafhoehe knapp ueber 2 Jahren ohne Begruendung der Schwere; Verteidigung sollte vor Urteilsverkuendung punktgenau argumentieren.
- **Lange Verfahrensdauer** nicht kompensiert.
- **U-Haft-Anrechnung** in der Urteilsformel uebersehen (§ 51 StGB).
- **Doppelverwertung** Tatbestandsmerkmale.

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Grundsatz.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen vor Zumessung.
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Vollstreckung.
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — bei Mehrtat.

## Quellen und Stand 05/2026

- §§ 38, 39, 46, 47, 49, 51, 56-57a StGB in der geltenden Fassung.
- Art. 6 Abs. 1 EMRK Verfahrensdauer.
- Quellenregel: vgl. `references/zitierweise.md`.

## 2. `geldstrafe-tagessatzanzahl-bestimmen`

**Fokus:** Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs. 1 StGB. 5 bis 360 Tagessaetze als Grundgrenze; bei Gesamtgeldstrafe bis 720 Tagessaetze. Die Anzahl bildet die Schuldkomponente und folgt § 46 StGB. Abgrenzung zur Tagessatzhoehe, die das Nettoeinkommen abbildet. Schnittstelle Strafbefehl, Hauptverhandlung, Gesamtstrafe.

# Tagessatzanzahl der Geldstrafe — § 40 Abs. 1 StGB

## Worum geht es?

Bei der Geldstrafe wird die **Schuld** ueber die **Anzahl der Tagessaetze** ausgedrueckt; die **Hoehe** des einzelnen Tagessatzes spiegelt die wirtschaftlichen Verhaeltnisse wider (§ 40 Abs. 2 StGB; vgl. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst`). Dieser Skill konzentriert sich auf die Zahl.

## Wann brauchen Sie diese Skill?

- Sie pruefen einen Strafbefehl mit Tagessatzfestsetzung und wollen die Schuldkomponente ueberpruefen.
- Sie bereiten den Strafantrag der Staatsanwaltschaft fuer ein Vergehen vor.
- Sie schreiben die Strafzumessung im Urteil oder pruefen sie im Revisionsverfahren.
- Sie bilden eine Gesamtgeldstrafe nach §§ 53, 54 StGB.

## Rechtliche Grundlagen

- **§ 40 Abs. 1 Satz 2 StGB** — "Die Geldstrafe betraegt mindestens fuenf und, soweit das Gesetz nichts anderes bestimmt, hoechstens dreihundertsechzig volle Tagessaetze."
- **§ 54 Abs. 2 Satz 2 StGB** — Gesamtgeldstrafe bis 720 Tagessaetze.
- **§ 47 StGB** — Vorrang Geldstrafe vor kurzer Freiheitsstrafe unter 6 Monaten; vgl. `geldstrafe-vs-freiheitsstrafe-47-stgb`.
- **§ 41 StGB** — Geldstrafe neben Freiheitsstrafe moeglich, wenn der Taeter durch die Tat sich bereichert hat oder zu bereichern versucht hat.
- **§ 53 Abs. 2 StGB** — Bei Realkonkurrenz mehrerer Geldstrafen Gesamtgeldstrafe.

## Strafzumessungs-Grundsatz

- Die Tagessatzanzahl folgt allein **§ 46 StGB**; Strafzumessungstatsachen wie Vorleben, Tatfolgen, Nachtatverhalten sind hier abzubilden.
- Die Hoehe darf **nicht** in die Anzahl einfliessen — das waere eine unzulaessige Vermengung.
- Schuldrahmen-Theorie auch hier: Innerhalb des "Spielraums schuldangemessener Strafe" wird konkret bestimmt.

## Schritt-fuer-Schritt-Anleitung

1. **Strafrahmen pruefen**: Ist Geldstrafe ueberhaupt vorgesehen? Wird die Strafrahmen-Obergrenze des Tatbestands beruehrt (z.B. § 242 StGB: bis 5 Jahre oder Geldstrafe; § 263 Abs. 1 StGB: bis 5 Jahre oder Geldstrafe).
2. **Umrechnungsschluessel** beachten: 30 Tagessaetze = 1 Monat Freiheitsstrafe (faustregelhafte Aequivalenz; nicht starr, aber Orientierung).
3. **Strafzumessungstatsachen** nach § 46 StGB sammeln und gewichten (vgl. `strafzumessungs-tatsachen-46-ii-stgb`).
4. **Anzahl bestimmen** im Schuldrahmen.
5. **Kein Lappenanteil** — § 40 Abs. 1 StGB verlangt "volle" Tagessaetze.
6. **Bei Gesamtgeldstrafe** (§§ 53, 54 StGB): hoechste Einzelstrafe als Einsatzstrafe, dann Erhoehung um angemessenen Bruchteil bis maximal 720 Tagessaetze; vgl. `gesamtstrafenbildung-53-54-stgb-erste-instanz`.

## Faustwerte (orientierend, nicht starr)

| Bereich | Tagessatzanzahl |
|---|---|
| Bagatelle, ggf. § 153a StPO statt Strafbefehl | 5-30 |
| Mittlere Vergehen ohne Vorbelastung | 30-90 |
| Mittlere Vergehen mit Vorbelastung | 90-180 |
| Schwere Vergehen, Mehrtaeterstrukturen | 180-360 |
| Gesamtgeldstrafe Schwer-Komplex | 360-720 |

Die Tabelle ersetzt **keine** Einzelfallbetrachtung; sie zeigt nur das Spielfeld.

## Sonderfaelle

- **Mehrere Einzelstrafen** (Realkonkurrenz, § 53 StGB): Gesamtgeldstrafe nach § 54 Abs. 2 StGB; Erhoehung der hoechsten Einzelstrafe; max. 720 Tagessaetze.
- **Geldstrafe neben Freiheitsstrafe** (§ 41 StGB): nur wenn Bereicherungsabsicht und Bereicherung erkennbar; sonst Aufhebungsgrund.
- **Strafbefehl** (§ 407 Abs. 2 StPO): bis 360 Tagessaetze ohne Hauptverhandlung; vgl. `strafbefehl-strafzumessung-407-stpo`.
- **Verstaendigung** (§ 257c StPO): Strafrahmen-Ober- und Untergrenze fuer Tagessatzanzahl koennen Verhandlungsgegenstand sein; vgl. `verstaendigung-257c-stpo-strafzumessung`.

## Typische Fehler

- **Tagessatzanzahl und -hoehe vermengt**: Schwierige wirtschaftliche Verhaeltnisse mindern die Hoehe, nicht die Anzahl.
- **Doppelverwertung**: Tatbestandsmerkmal wird in die Anzahl eingerechnet.
- **Strafrahmen ignoriert**: Bei Tatbestand mit Mindeststrafe Freiheitsstrafe ist Geldstrafe ausgeschlossen.
- **§ 47 StGB uebersehen**: Wenn das Gericht statt Geldstrafe eine kurze Freiheitsstrafe verhaengt, muss es besondere Umstaende benennen.
- **Gesamtgeldstrafe** falsch gebildet: Es duerfen nicht einfach die Einzelstrafen addiert werden; § 54 Abs. 1 Satz 2 StGB verlangt Erhoehung um eine "angemessene" Quote.

## Querverweise

- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — Hoehenkomponente.
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Vorrang Geldstrafe.
- `strafbefehl-strafzumessung-407-stpo` — Strafbefehl.
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — Gesamtgeldstrafe.

## Quellen und Stand 05/2026

- §§ 40, 41, 47, 53, 54 StGB in der geltenden Fassung.
- § 407 Abs. 2 StPO Strafbefehl.
- Quellenregel: vgl. `references/zitierweise.md`.

## 3. `geldstrafe-vs-freiheitsstrafe-47-stgb`

**Fokus:** Vorrang der Geldstrafe vor kurzer Freiheitsstrafe nach § 47 StGB. Kurze Freiheitsstrafe unter 6 Monaten nur bei besonderen Umstaenden in der Tat oder in der Persoenlichkeit. Begruendungspflicht des Gerichts. Verhaeltnis Geldstrafe + Freiheitsstrafe (§ 41 StGB). Strategiewahl Verteidigung gegen kurze Freiheitsstrafe; Umstellungsantrag in Geldstrafe; Bewaehrungsperspektive.

# Geldstrafe vs. Freiheitsstrafe — § 47 StGB

## Worum geht es?

§ 47 Abs. 1 StGB enthaelt eine gesetzgeberische Wertentscheidung **gegen** kurze Freiheitsstrafen. Eine Freiheitsstrafe unter sechs Monaten darf das Gericht nur verhaengen, wenn besondere Umstaende, die in der Tat oder der Persoenlichkeit des Taeters liegen, die Verhaengung der Freiheitsstrafe zur Einwirkung auf den Taeter oder zur Verteidigung der Rechtsordnung unerlaesslich machen. § 47 Abs. 2 StGB regelt das Verhaeltnis bei Tatbestaenden, die nur Freiheitsstrafe vorsehen.

## Wann brauchen Sie diese Skill?

- Sie verteidigen gegen einen Strafantrag oder ein Urteil mit kurzer Freiheitsstrafe und wollen auf Geldstrafe umstellen lassen.
- Sie pruefen die Strafzumessungsruege bei kurzer Freiheitsstrafe ohne ausreichende Begruendung.
- Sie verhandeln in einer Verstaendigung den Strafrahmen und wollen die Geldstrafe-Schiene sichern.
- Sie sondieren bei einem Tatbestand ohne Geldstrafe-Option, ob § 47 Abs. 2 StGB den Strafrahmen oeffnet.

## Rechtliche Grundlagen

- **§ 47 Abs. 1 StGB** — Eine Freiheitsstrafe unter sechs Monaten verhaengt das Gericht nur, wenn besondere Umstaende, die in der Tat oder in der Persoenlichkeit des Taeters liegen, die Verhaengung einer Freiheitsstrafe zur Einwirkung auf den Taeter oder zur Verteidigung der Rechtsordnung unerlaesslich machen.
- **§ 47 Abs. 2 StGB** — Wenn das Gesetz keine Geldstrafe androht und eine Freiheitsstrafe unter sechs Monaten nicht in Betracht kommt, ist auf Geldstrafe zu erkennen. Der Strafrahmen der Geldstrafe ergibt sich aus § 40 Abs. 1 StGB (5 bis 360 Tagessaetze).
- **§ 41 StGB** — Geldstrafe **neben** Freiheitsstrafe bei Bereicherungsabsicht.

## Strafzumessungs-Grundsatz

§ 47 StGB ist Ausdruck der **Subsidiaritaet** der kurzen Freiheitsstrafe. Praevention und Schuld stehen in einer Stufung:

1. Erste Wahl: Geldstrafe.
2. Nur in Ausnahmefaellen: kurze Freiheitsstrafe; das Gericht muss "besondere Umstaende" konkret benennen.
3. Auch dann moeglichst mit Bewaehrung (§ 56 StGB).

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Strafrahmen pruefen**: Sieht der Tatbestand Geldstrafe vor? Wenn nein, Klappentest fuer § 47 Abs. 2 StGB.
2. **Argumente gegen besondere Umstaende sammeln**:
 - Erstmaliger Verstoss.
 - Niedrige kriminelle Energie.
 - Soziale Integration: Beruf, Familie, intakte Bindungen.
 - Akute persoenliche Belastung (Sucht, Krise) bereits in Behandlung.
 - Kein einschlaegiges Vorleben.
3. **Tagessatz-Berechnung beilegen**, damit das Gericht Geldstrafe konkret verhaengen kann; vgl. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst`.
4. **In der Hauptverhandlung** ausdruecklich beantragen: "Wir beantragen Verhaengung einer Geldstrafe; eine Freiheitsstrafe ist nach § 47 Abs. 1 StGB nicht unerlaesslich, da [...]."
5. **Wenn doch kurze Freiheitsstrafe**: hilfsweise Bewaehrung (§ 56 StGB) sichern; vgl. `bewaehrung-56-stgb-positive-sozialprognose`.
6. **In der Revision**: § 47 Abs. 1 StGB ist eine Vorschrift, deren Verletzung mit der Sachruege geltend gemacht werden kann; Begruendungsmangel im Urteil ist regelmaessiger Aufhebungsgrund.

## Schritt-fuer-Schritt-Anleitung (Anklage)

- Wenn kurze Freiheitsstrafe angestrebt wird, **konkret** vortragen, welche besonderen Umstaende vorliegen:
 - Einschlaegige Vorbelastung, mehrfache Bewaehrungsversager.
 - Tat-Spezifika (z.B. Gewerbsmaessigkeit, Bandenstruktur, Wiederholungstat in Bewaehrung).
 - Schwergewichtige Tatfolgen ueber Tatbestandsmerkmal hinaus.
- Verteidigung der Rechtsordnung nur bei massiven oder oeffentlichkeitswirksamen Faellen tragfaehig.

## Strafmildernde Wirkung gegenueber Geldstrafe

- Geldstrafe statt Freiheitsstrafe ist **kein** automatischer Strafzumessungsabschlag. Anzahl der Tagessaetze kann hoch sein, ohne dass das Strafmass unverhaeltnismaessig wird.
- Faustregel der Praxis: 30 Tagessaetze entsprechen ungefaehr 1 Monat Freiheitsstrafe (orientierend).

## Verhaeltnis zu § 56 StGB (Bewaehrung)

Wird trotzdem eine kurze Freiheitsstrafe (3 bis 6 Monate) verhaengt, ist Bewaehrung nach § 56 Abs. 1 StGB (Strafe bis 1 Jahr) Standard, sofern Sozialprognose positiv ist; vgl. `bewaehrung-56-stgb-positive-sozialprognose`.

## Typische Fehler

- **Pauschale Begruendung** im Urteil: "Die Schwere der Tat erfordert eine Freiheitsstrafe." Das ist keine besondere Umstaende-Begruendung iSv § 47 Abs. 1 StGB; Revisionsruege.
- **Verteidigung der Rechtsordnung** ohne Tatsachen: Floskel, die in der Revision regelmaessig faellt.
- **Vorstrafen** allein begruenden in der Regel nicht ohne weiteres die Unerlaesslichkeit; nur einschlaegige und intensive Vorbelastung.
- **§ 41 StGB falsch** angewendet: Geldstrafe neben Freiheitsstrafe **nur** bei Bereicherungsabsicht.

## Querverweise

- `geldstrafe-tagessatzanzahl-bestimmen` — Anzahl bestimmen.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — Hoehe bestimmen.
- `freiheitsstrafe-strafmass-pruefen` — bei laengerer Freiheitsstrafe.
- `bewaehrung-56-stgb-positive-sozialprognose` — Aussetzung zur Bewaehrung.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Begruendungsmangel als Ruege.

## Quellen und Stand 05/2026

- §§ 40, 41, 47, 56 StGB in der geltenden Fassung.
- Quellenregel: vgl. `references/zitierweise.md`.
