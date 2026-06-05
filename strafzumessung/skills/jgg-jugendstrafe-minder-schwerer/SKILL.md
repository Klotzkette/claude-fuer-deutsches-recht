---
name: jgg-jugendstrafe-minder-schwerer
description: "JGG Jugendstrafe Minder Schwerer: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# JGG Jugendstrafe Minder Schwerer

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **JGG Jugendstrafe Minder Schwerer** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` | Strafzumessung im Jugendstrafrecht. Erziehungsgedanke § 2 JGG. Massnahmen-Trio: Erziehungsmassregeln §§ 9-12 JGG, Zuchtmittel §§ 13-16 JGG, Jugendstrafe §§ 17-18 JGG. Voraussetzung Jugendstrafe schaedliche Neigungen oder Schwere der Schuld § 17 JGG. Strafrahmen Jugendstrafe 6 Monate bis 5 Jahre, bei Verbrechen bis 10 Jahre. Heranwachsende § 105 JGG. JStVollzG. |
| `minder-schwerer-fall-und-besonders-schwerer-fall` | Strafrahmen-Modifikation durch minder schweren Fall (Strafrahmen-Senkung) und besonders schweren Fall (Strafrahmen-Anhebung). Gesamtwuerdigung aller Tat- und Taeter-Umstaende. Beziehung zu Regelbeispielen. Konkurrenz minder schwerer Fall vs. § 49 StGB. Pruefungsreihenfolge. Anwendungsfaelle § 213 StGB Totschlag, § 249 Abs. 2 StGB Raub, § 243 StGB Diebstahl, § 263 Abs. 3 StGB Betrug. |
| `nachtraegliche-gesamtstrafenbildung-55-stgb` | Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Voraussetzung: spaetere Tat wurde **vor** einer frueheren Verurteilung begangen (Zaesurwirkung). Beschluss-Verfahren § 460 StPO. Einbeziehung rechtskraeftiger Strafen. Haerteausgleich, wenn die Einbeziehung nicht moeglich ist (Bewaehrung bereits erledigt, Strafvollstreckung beendet). BGH-staendige Linie. Verteidigung im Vollstreckungsstadium. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **JGG Jugendstrafe Minder Schwerer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln`

**Fokus:** Strafzumessung im Jugendstrafrecht. Erziehungsgedanke § 2 JGG. Massnahmen-Trio: Erziehungsmassregeln §§ 9-12 JGG, Zuchtmittel §§ 13-16 JGG, Jugendstrafe §§ 17-18 JGG. Voraussetzung Jugendstrafe schaedliche Neigungen oder Schwere der Schuld § 17 JGG. Strafrahmen Jugendstrafe 6 Monate bis 5 Jahre, bei Verbrechen bis 10 Jahre. Heranwachsende § 105 JGG. JStVollzG.

# Strafzumessung im Jugendstrafrecht

## Worum geht es?

Das Jugendgerichtsgesetz (JGG) gilt fuer Jugendliche (14 bis unter 18 Jahre) und unter bestimmten Voraussetzungen fuer Heranwachsende (18 bis unter 21 Jahre, § 105 JGG). Tragend ist der **Erziehungsgedanke** (§ 2 JGG). Die Strafzumessung folgt einem dreistufigen System: Erziehungsmassregeln, Zuchtmittel, Jugendstrafe.

## Wann brauchen Sie diese Skill?

- Mandant ist Jugendlicher oder Heranwachsender; Sie pruefen die anwendbaren Sanktionen.
- Heranwachsender Mandant — Sie pruefen § 105 JGG (Anwendung Jugendrecht oder Erwachsenenrecht).
- Sie bereiten die Strafzumessungsverhandlung vor der Jugendkammer oder dem Jugendrichter vor.

## Rechtliche Grundlagen

### Anwendungsbereich

- **§ 1 Abs. 1 JGG** — Geltung fuer Jugendliche (14 bis unter 18 bei Tatbegehung).
- **§ 105 JGG** — Heranwachsende (18 bis unter 21 bei Tatbegehung): Anwendung Jugendrecht, wenn die Persoenlichkeitsentwicklung der eines Jugendlichen gleichsteht **oder** die Tat eine typische Jugendverfehlung ist.
- **§ 19 StGB** — Schuldunfaehigkeit unter 14 Jahren.

### Erziehungsgedanke

- **§ 2 JGG** — Erziehungsgedanke vorrangig vor Strafe und Suehne.
- Strafzumessung folgt erzieherischer, nicht primaer schuldorientierter Logik.

### Stufung der Sanktionen

#### 1. Erziehungsmassregeln (§§ 9-12 JGG)

- **§ 10 JGG Weisungen** — Aufenthalt, Arbeit, Schule, Familie, Freizeit, sozial-paedagogische Massnahmen, Verkehrsunterricht, Anti-Aggressionstraining etc.
- **§ 11 JGG Hilfen zur Erziehung** — Verweis auf jugendhilferechtliche Massnahmen.

#### 2. Zuchtmittel (§§ 13-16 JGG)

- **§ 14 JGG Verwarnung** — formliche Ruege.
- **§ 15 JGG Auflagen** — Schadenswiedergutmachung, persoenliche Entschuldigung, Arbeitsleistungen, Geldbusse.
- **§ 16 JGG Jugendarrest** — Freizeit-, Kurz-, Dauerarrest bis 4 Wochen.

#### 3. Jugendstrafe (§§ 17, 18 JGG)

- **§ 17 Abs. 1 JGG** — Jugendstrafe ist Freiheitsentzug in Jugendstrafanstalt.
- **§ 17 Abs. 2 JGG** — Voraussetzung:
 - **Schaedliche Neigungen**, deren Bekaempfung erzieherische Massnahmen nicht ausreichen, **oder**
 - **Schwere der Schuld** bei Straftaten von erheblicher Bedeutung.
- **§ 18 Abs. 1 JGG** — Mindestmass 6 Monate, Hoechstmass:
 - bei Vergehen: 5 Jahre.
 - bei Verbrechen, fuer die Hoechststrafe ueber 10 Jahre Freiheitsstrafe nach allgemeinem Strafrecht steht: bis 10 Jahre.
 - bei besonders schweren Mordfaellen bei Heranwachsenden nach § 105 JGG: bis 15 Jahre.
- **§ 18 Abs. 2 JGG** — Strafzumessungs-Grundsatz: erforderliche erzieherische Einwirkung.

### Sonderregeln

- **§ 21 JGG** — Aussetzung der Jugendstrafe zur Bewaehrung bis 1 Jahr regelmaessig; bis 2 Jahre bei guenstiger Prognose.
- **§ 22 JGG** — Bewaehrungszeit 1 bis 3 Jahre, mindestens 1 Jahr.
- **§ 27 JGG** — Aussetzung der Verhaengung der Jugendstrafe.
- **§ 31 JGG** — Einheitliche Massnahme oder Strafe bei mehreren Taten.
- **§ 105 JGG** — Heranwachsende.
- **§ 106 JGG** — Strafzumessung bei Heranwachsenden im allgemeinen Strafrecht; Sondergrenzen.

## Strafzumessungs-Grundsatz

- **Erziehung** vor **Suehne**.
- **Stufung**: Erziehungsmassregeln zuerst pruefen, dann Zuchtmittel, erst zuletzt Jugendstrafe.
- **Jugendstrafe** nur, wenn Erziehungsmassregeln und Zuchtmittel nicht ausreichen oder Schwere der Schuld es gebietet.
- **§ 18 Abs. 2 JGG** — Strafhoehe der Jugendstrafe nach der erforderlichen erzieherischen Einwirkung; das schliesst weder die Beruecksichtigung der Schuld noch praeventive Erwaegungen aus, aber der Erziehungsgedanke ist tragend.

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Anwendungsbereich** klaeren:
 - Tatbegehungsalter? Jugendlich oder Heranwachsend?
 - Bei Heranwachsenden: § 105 JGG-Pruefung. Antrag auf Jugendrecht meist verteidigungsguenstig.
2. **Sozialanamnese** vorbereiten:
 - Persoenlichkeit (Entwicklung, Schulbildung, soziales Umfeld).
 - Tat: Bagatelle, Krisentat, Jugendverfehlung?
 - Schaedliche Neigungen erkennbar (Suchtproblematik, Gewalt, Eigentumsdelikte als Muster)?
3. **Sanktionsvorschlag** mit Mandant und Jugendgerichtshilfe abstimmen:
 - **Erziehungsmassregel** (Weisung, sozial-paedagogische Massnahme).
 - **Zuchtmittel** (Auflage, Jugendarrest).
 - **Jugendstrafe** vermeiden, wenn moeglich; sonst Bewaehrung sichern.
4. **Bewaehrungsperspektive**: § 21 JGG.
5. **Strafzumessungs-Argumentation**:
 - Erziehung: lernfaehig, sozial integriert, Schul- oder Berufsperspektive.
 - Keine schaedlichen Neigungen erkennbar.
 - Tat als Einzelfall, nicht als Muster.

## Heranwachsende — § 105 JGG

- Anwendung Jugendrecht, wenn:
 - Persoenlichkeitsentwicklung des Heranwachsenden noch der eines Jugendlichen gleichsteht (Reife-Beurteilung), **oder**
 - die Tat eine typische **Jugendverfehlung** ist (Tat- und Persoenlichkeitsbeurteilung).
- Wirkung der Anwendung Jugendrecht:
 - Strafrahmen nach Jugendrecht (max. 10 Jahre bei Verbrechen; bei Mordfaellen bis 15 Jahre).
 - Bewaehrungsregeln nach § 21 JGG.
 - Vollzug in der Jugendstrafanstalt.

## Sanktionen — Faustwerte

| Sanktion | Anwendungsbereich |
|---|---|
| Erziehungsmassregel | Bagatelle, Spontantat, Erstkonflikt |
| Zuchtmittel (Verwarnung) | Bagatelle, geringfuegige Tat |
| Zuchtmittel (Auflage) | mittlere Schwere |
| Zuchtmittel (Jugendarrest) | mittlere Schwere mit Erziehungsbedarf |
| Jugendstrafe Bewaehrung | mittlere bis schwere Tat mit positiver Prognose |
| Jugendstrafe ohne Bewaehrung | schwere Tat, schaedliche Neigungen, negative Prognose |

## Aussetzung zur Bewaehrung (§§ 21, 22 JGG)

- Bis 1 Jahr: Aussetzung Regelfall bei guenstiger Sozialprognose (§ 21 Abs. 1 JGG).
- Bis 2 Jahre: bei besonderen Umstaenden (§ 21 Abs. 2 JGG).
- Bewaehrungszeit 1 bis 3 Jahre, mindestens 1 Jahr.
- Auflagen / Weisungen analog § 23 JGG.

## Aussetzung der Verhaengung (§ 27 JGG)

- Wenn nicht mit Sicherheit beurteilbar ist, ob die schaedlichen Neigungen so erheblich sind, dass eine Jugendstrafe erforderlich ist, kann das Gericht die Verhaengung **aussetzen**.
- Bewaehrungszeit 1 bis 2 Jahre; bei guenstigem Verlauf erfolgt Freispruch oder Einstellung.

## Typische Fehler

- **Heranwachsenden** automatisch Erwachsenenrecht angewandt: § 105 JGG-Pruefung notwendig.
- **Jugendstrafe** als erste Wahl behandelt; Stufung uebersprungen.
- **Schaedliche Neigungen** ohne Tatsachenbasis bejaht.
- **Schwere der Schuld** ohne erforderliche Tatschwere.
- **Erziehungsgedanke** rein floskelhaft, nicht konkret in die Strafzumessung eingearbeitet.
- **Sozialanamnese** der Jugendgerichtshilfe nicht ausgewertet.
- **Vollzug** in Jugendstrafanstalt (§§ 89 ff. JGG) nicht beachtet.
- **§ 31 JGG**: bei mehreren Taten ist eine **einheitliche** Massnahme oder Strafe zu bilden — kein einfaches "Aufsummieren".

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — bei Anwendung Erwachsenenrecht.
- `bewaehrung-56-stgb-positive-sozialprognose` — Analoge Aussetzung im Erwachsenenrecht.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Vollstreckung; bei JGG Sonderregeln in JStVollzG.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Begruendungspflicht auch im Jugendurteil.

## Quellen und Stand 05/2026

- §§ 1, 2, 9-12, 13-16, 17-22, 27, 31, 105, 106 JGG in der geltenden Fassung.
- §§ 89 ff. JGG Vollzug.
- Landes-JStVollzGe.
- BGH zum Heranwachsenden-Recht und zur Schwere der Schuld — Aktenzeichen verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

## 2. `minder-schwerer-fall-und-besonders-schwerer-fall`

**Fokus:** Strafrahmen-Modifikation durch minder schweren Fall (Strafrahmen-Senkung) und besonders schweren Fall (Strafrahmen-Anhebung). Gesamtwuerdigung aller Tat- und Taeter-Umstaende. Beziehung zu Regelbeispielen. Konkurrenz minder schwerer Fall vs. § 49 StGB. Pruefungsreihenfolge. Anwendungsfaelle § 213 StGB Totschlag, § 249 Abs. 2 StGB Raub, § 243 StGB Diebstahl, § 263 Abs. 3 StGB Betrug.

# Minder schwerer Fall und besonders schwerer Fall

## Worum geht es?

Viele Tatbestaende sehen einen **modifizierten Strafrahmen** vor:

- **Minder schwerer Fall**: gesenkter Strafrahmen, z.B. § 213 StGB beim Totschlag, § 249 Abs. 2 StGB beim Raub.
- **Besonders schwerer Fall**: erhoehter Strafrahmen, oft mit **Regelbeispielen**, z.B. § 243 StGB Diebstahl, § 263 Abs. 3 StGB Betrug.

Die Modifikation erfolgt durch **Gesamtwuerdigung** aller Umstaende.

## Wann brauchen Sie diese Skill?

- Sie wollen die Strafrahmen-Senkung "minder schwerer Fall" zugunsten des Mandanten erreichen.
- Sie pruefen, ob ein Regelbeispiel erfuellt ist und ob die Indizwirkung entkraeftet werden kann.
- Sie ordnen die Pruefungsreihenfolge bei mehreren Strafrahmen-Modifikationen.

## Rechtliche Grundlagen

### Minder schwerer Fall — Beispiele

- **§ 213 StGB** — Minder schwerer Fall des Totschlags: Provokation des Opfers oder sonstige mildernde Umstaende; Strafrahmen 1 bis 10 Jahre statt 5 bis 15 Jahre.
- **§ 249 Abs. 2 StGB** — Minder schwerer Fall des Raubs: 6 Monate bis 5 Jahre statt 1 bis 15 Jahre.
- **§ 250 Abs. 3 StGB** — Minder schwerer Fall des schweren Raubs.
- **§ 226 Abs. 3 StGB** — Minder schwerer Fall der schweren Koerperverletzung.
- **§ 224 Abs. 1 letzter Halbsatz StGB** — Minder schwerer Fall der gefaehrlichen Koerperverletzung: Freiheitsstrafe 3 Monate bis 5 Jahre statt 6 Monate bis 10 Jahre.

### Besonders schwerer Fall — Beispiele

- **§ 243 StGB** — Besonders schwerer Fall des Diebstahls mit Regelbeispielkatalog: 3 Monate bis 10 Jahre.
- **§ 263 Abs. 3 StGB** — Besonders schwerer Fall des Betrugs mit Regelbeispielkatalog: 6 Monate bis 10 Jahre.
- **§ 267 Abs. 3 StGB** — Besonders schwerer Fall der Urkundenfaelschung.
- **§ 240 Abs. 4 StGB** — Besonders schwerer Fall der Noetigung.

## Strafzumessungs-Grundsatz

### Minder schwerer Fall

- Erfordert **Gesamtwuerdigung**: alle straftatbezogenen und persoenlichen Umstaende werden zusammengenommen.
- Schwellenfrage: weicht das Gesamtgewicht der Tat so deutlich nach unten von der Durchschnittstat ab, dass der gesetzliche Regelstrafrahmen unangemessen waere?
- Strafmilderungsgruende nach § 49 StGB koennen den Tatbestand des minder schweren Falls **mitausloesen** ("vertypte Milderungsgruende" bei Gesamtwuerdigung beruecksichtigen). Wenn der Tatbestand des minder schweren Falls bejaht wird, **entfaellt** die zusaetzliche Milderung nach § 49 StGB regelmaessig nicht automatisch; vielmehr kann der gemilderten Strafrahmen weiter nach § 49 StGB modifiziert werden. **St. Rspr.; Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.**

### Besonders schwerer Fall

- Bei **Regelbeispielen** Indizwirkung: ist ein Regelbeispiel erfuellt, ist die Indizwirkung fuer besonders schweren Fall regelmaessig gegeben.
- Gegenindizien koennen die Indizwirkung **entkraeften** — Gesamtwuerdigung.
- Bei "unbenannten besonders schweren Faellen" muss die Tat in Gewicht und Charakter den Regelbeispielen ungefaehr entsprechen.

## Pruefungsreihenfolge

1. **Grundtatbestand** und **Qualifikationen** pruefen.
2. **Regelbeispiele** (besonders schwerer Fall): Ist Tatbestand erfuellt? Indizwirkung. Gegenindizien?
3. **Minder schwerer Fall**: Gesamtwuerdigung; Tatbild deutlich unterhalb des Durchschnitts?
4. **Vertypte Milderungsgruende** nach § 49 StGB (Versuch, Beihilfe, § 21, § 17, § 28 Abs. 1, § 46a StGB).
5. Konkreten Strafrahmen festlegen.
6. Strafe im Schuldrahmen nach § 46 StGB konkretisieren.

## Konkurrenz minder schwerer Fall vs. § 49 StGB

Wenn ein vertypter Milderungsgrund vorliegt **und** zusaetzlich ein minder schwerer Fall in Betracht kommt: **Wahlrecht** des Gerichts in der Logik der st. Rspr.:

- Pruefung des minder schweren Falls **unter Einbeziehung** des vertypten Milderungsgrundes.
- Wenn minder schwerer Fall bejaht: weitere Milderung nach § 49 StGB ist nicht zwingend.
- Wenn minder schwerer Fall verneint: Milderung nach § 49 StGB greift fuer den Regelstrafrahmen.

In der Verteidigungspraxis stets **hilfsweise** beide Wege beantragen. **Aktenzeichen der einschlaegigen BGH-Linie vor Zitat verifizieren.**

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Strafrahmen-Modifikation** identifizieren: Liegt eine minder schwere Fall-Norm vor? Liegt ein Regelbeispiel-Katalog vor?
2. **Argumente fuer minder schweren Fall** sammeln:
 - Provokation, Notlage, akuter Affekt.
 - Erstmaliger Verstoss.
 - Tatfolgen geringfuegig.
 - Tatumstaende untypisch.
3. **Argumente gegen Regelbeispiel-Indiz** sammeln:
 - Konkreter Vorgang weicht von der Modellvorstellung des Regelbeispiels ab.
 - Sonstige starke Strafmilderungs-Gesichtspunkte ueberwiegen.
4. **Antrag**: "Wir beantragen Verurteilung nach minder schwerem Fall (§ ..., Abs. ...). Hilfsweise Strafmilderung nach § 49 Abs. 1 StGB."

## Schritt-fuer-Schritt-Anleitung (Anklage)

1. **Regelbeispiel-Vortrag** mit Tatsachen substantiieren.
2. **Unbenannte besonders schwere Faelle** nur bei klarem Vergleichsgewicht zu den Regelbeispielen.
3. **Gegenargumente** zum minder schweren Fall antizipieren.

## Typische Fehler

- **Minder schwerer Fall pauschal** abgelehnt: ohne Gesamtwuerdigung; Revisionsangriff.
- **Regelbeispiel automatisch** zu besonders schwerem Fall: Indizwirkung nicht widerlegt geprueft.
- **Doppelte Anwendung**: Tatumstand begruendet minder schweren Fall **und** wird zusaetzlich strafmildernd in § 46 StGB beruecksichtigt — moegliche Verstoss gegen § 46 Abs. 3 StGB.
- **§ 49 StGB** nicht im Verhaeltnis zum minder schweren Fall geprueft.

## Querverweise

- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik.
- `regelbeispiele-rechtsprechung` — Detail zu Regelbeispielen.
- `strafmilderung-49-stgb-zwingend-fakultativ` — Verhaeltnis zu § 49 StGB.
- `paragraph-46-stgb-grundsatz-strafzumessung` — Anwendung im Schuldrahmen.

## Quellen und Stand 05/2026

- §§ 213, 224, 226, 240, 243, 249, 250, 263, 267 StGB in der geltenden Fassung.
- BGH-Linie zur Konkurrenz minder schwerer Fall / § 49 StGB — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

## 3. `nachtraegliche-gesamtstrafenbildung-55-stgb`

**Fokus:** Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Voraussetzung: spaetere Tat wurde **vor** einer frueheren Verurteilung begangen (Zaesurwirkung). Beschluss-Verfahren § 460 StPO. Einbeziehung rechtskraeftiger Strafen. Haerteausgleich, wenn die Einbeziehung nicht moeglich ist (Bewaehrung bereits erledigt, Strafvollstreckung beendet). BGH-staendige Linie. Verteidigung im Vollstreckungsstadium.

# Nachtraegliche Gesamtstrafenbildung — § 55 StGB

## Worum geht es?

§ 55 StGB ermoeglicht eine **nachtraegliche** Bildung einer Gesamtstrafe, wenn ein bereits rechtskraeftig Verurteilter wegen einer **anderen** Tat verurteilt wird, die er **vor** der frueheren Verurteilung begangen hat. Es findet eine **rueckwirkende** Gesamtbetrachtung statt — so, als waeren beide Taten in einem Verfahren entschieden worden. Die fruehere Verurteilung wirkt als **Zaesur**.

## Wann brauchen Sie diese Skill?

- Mandant ist bereits einmal rechtskraeftig verurteilt; jetzt wird eine weitere Tat abgeurteilt, die **vor** der frueheren Verurteilung begangen wurde.
- Sie pruefen die Akte, ob nachtraegliche Gesamtstrafenbildung moeglich ist (oder schon haette erfolgen muessen).
- Sie schreiben einen Antrag im Beschluss-Verfahren nach § 460 StPO.
- Sie pruefen, ob die Einbeziehung nicht (mehr) moeglich ist und ob ein **Haerteausgleich** erforderlich wird (vgl. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`).

## Rechtliche Grundlagen

- **§ 55 Abs. 1 StGB** — Wird ein bereits rechtskraeftig Verurteilter spaeter wegen einer anderen Tat verurteilt, die vor der frueheren Verurteilung begangen wurde, so ist eine nachtraegliche Gesamtstrafe nach §§ 53, 54 StGB zu bilden. Vorverurteilung muss in den Aburteilung einbezogen werden, soweit die Strafe noch nicht **vollstreckt, verjaehrt oder erlassen** ist.
- **§ 55 Abs. 2 StGB** — Bei Nebenstrafen, Nebenfolgen und Massregeln gilt § 53 Abs. 4 StGB sinngemaess.
- **§ 460 StPO** — Beschluss-Verfahren zur nachtraeglichen Gesamtstrafenbildung; zustaendig ist das Gericht des letzten Verfahrens.
- **§ 462 StPO** — Anhoerung, sofortige Beschwerde.
- **§ 462a StPO** — Strafvollstreckungskammer fuer bestimmte Konstellationen.

## Zentrale Voraussetzung — Zaesurwirkung

Die fruehere Verurteilung wirkt als **Zaesur**: Sie bildet die Trennlinie zwischen Taten, die nachtraeglich noch in eine Gesamtstrafe einbezogen werden koennen, und Taten, die in der Folgezeit begangen wurden. Massgeblich ist das **Datum der ersten tatrichterlichen Verurteilung** im jeweiligen Verfahren (st. Rspr.; Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren).

**Beispiel**:

- 01.03.2024: Tat A.
- 15.05.2024: Tat B.
- 10.07.2024: Verurteilung Tat A (AG, Geldstrafe 90 Tagessaetze; rechtskraeftig).
- 20.11.2024: Tat C.
- 15.04.2025: Tat B wird abgeurteilt (LG, Freiheitsstrafe 8 Monate).

Tat B wurde **vor** der Verurteilung vom 10.07.2024 begangen. Bei der Verurteilung am 15.04.2025 ist nach § 55 StGB eine nachtraegliche Gesamtstrafe aus der Geldstrafe vom 10.07.2024 und der Freiheitsstrafe vom 15.04.2025 zu bilden.

Tat C wurde **nach** der Verurteilung vom 10.07.2024 begangen — sie kann **nicht** mit Tat A in eine Gesamtstrafe einbezogen werden; die Verurteilung vom 10.07.2024 wirkt als Zaesur.

## Wann ist eine Einbeziehung nicht (mehr) moeglich?

§ 55 Abs. 1 Satz 1 StGB schliesst die Einbeziehung aus, wenn die fruehere Strafe:

- **vollstreckt** ist;
- **verjaehrt** ist;
- **erlassen** ist (z.B. nach abgelaufener Bewaehrung, § 56g StGB).

In solchen Faellen kommt der **Haerteausgleich** in Betracht; vgl. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`.

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **BZRG-Auszug** und Verfahrensakte pruefen: Welche Vorverurteilungen liegen vor? Welche Tatzeiten?
2. **Zaesur-Pruefung**: Wurde die abzuurteilende Tat **vor** der ersten tatrichterlichen Verurteilung begangen?
3. **Status der Vorverurteilung**:
 - Vollstreckung schon abgeschlossen? — Haerteausgleich.
 - Verjaehrt? — Haerteausgleich.
 - Erlassen (Bewaehrung gluecklich abgelaufen)? — Haerteausgleich.
 - Noch offen / in Vollstreckung / Bewaehrung laufend? — Einbeziehung nach § 55 StGB.
4. **Antrag**:
 - **In der Hauptverhandlung**: "Wir beantragen, gemaess § 55 StGB eine Gesamtstrafe aus der Strafe aus dem Urteil [Az.] vom [Datum] und der hier zu verhaengenden Strafe zu bilden."
 - **Nach Rechtskraft (Beschluss-Verfahren)**: § 460 StPO; zustaendig ist das Gericht des **letzten** Verfahrens.
5. **Begruendung im Urteil**: Einzelstrafen, Einsatzstrafe, Gesamtstrafe; vgl. `gesamtstrafenbildung-53-54-stgb-erste-instanz`.
6. **Bewaehrungsperspektive**: Gesamtstrafe darf nicht ueber 2 Jahre liegen, wenn Bewaehrung erhalten bleiben soll.

## Beschluss-Verfahren nach § 460 StPO

- Antrag der Staatsanwaltschaft oder des Verurteilten.
- Zustaendig: Gericht des **letzten** Verfahrens.
- Anhoerung des Verurteilten und der Staatsanwaltschaft (§ 462 Abs. 2 StPO).
- Entscheidung durch **Beschluss**; sofortige Beschwerde nach § 462 Abs. 3 StPO innerhalb einer Woche.
- Die einbezogenen Strafen verlieren ihre Selbststaendigkeit; die alte Strafvollstreckungsgrundlage wird ersetzt durch den neuen Gesamtstrafen-Beschluss.

## Strafzumessungs-Grundsatz bei nachtraeglicher Gesamtstrafenbildung

- **Hypothetische Gesamtbetrachtung**: Wie waere entschieden worden, wenn beide Taten in einem Verfahren abgeurteilt worden waeren?
- **Schutzzweck** des § 55 StGB: Der Verurteilte soll durch die Aufspaltung in mehrere Verfahren **nicht schlechter gestellt** werden, als wenn beide Taten gemeinsam abgeurteilt worden waeren.
- **Bildung**: hoechste Einzelstrafe als Einsatzstrafe, dann angemessene Erhoehung; max. 15 Jahre Freiheitsstrafe / 720 Tagessaetze Geldstrafe (§ 54 Abs. 2 StGB).

## Sonderfaelle

### Mehrere fruehere Verurteilungen

- Es koennen **mehrere** fruehere Verurteilungen einbezogen werden, soweit die jeweilige Tat vor der jeweiligen frueheren Verurteilung begangen wurde.
- Komplexe Konstellationen: oft mehrere Zaesuren mit unterschiedlichen Einbeziehungsmoeglichkeiten.

### Verstrickung mit Bewaehrungsstrafe

- Wird die fruehere Bewaehrungsstrafe in die Gesamtstrafe einbezogen, faellt sie als selbststaendige Bewaehrungsstrafe weg.
- Die neue Gesamtstrafe kann ihrerseits zur Bewaehrung ausgesetzt werden (§ 56 StGB); Bewaehrungs-Voraussetzungen pruefen.
- Falls die Bewaehrungsstrafe schon **erlassen** ist (§ 56g StGB), Einbeziehung nicht moeglich — Haerteausgleich.

### Mehrere offene Verfahren

- Wenn mehrere Verfahren gleichzeitig laufen, sind die Verfahren oft prozessoekonomisch zu **verbinden** (§ 4 StPO), damit nachtraegliche Gesamtstrafenbildung entfaellt.

### Auslandsstrafen

- Auslandsstrafen werden **nicht** einbezogen (BGH st. Rspr.; Aktenzeichen verifizieren).
- Kompensation kann ggf. durch Strafmilderung erfolgen.

## Typische Fehler

- **Zaesur falsch bestimmt**: Massgeblich ist das erste tatrichterliche Urteil im jeweiligen Verfahren, **nicht** die Rechtskraft.
- **Einbeziehung uebersehen**: Wenn das Gericht die fruehere Strafe nicht einbezieht, obwohl sie noch offen ist, liegt Strafzumessungsmangel vor (Revisionsruege).
- **Haerteausgleich nicht angesprochen**: Wenn Einbeziehung nicht moeglich ist, muss der Schutzzweck des § 55 StGB durch Haerteausgleich gewahrt werden.
- **Bewaehrung** der frueheren Strafe nicht beachtet: Bei Einbeziehung faellt die alte Bewaehrungsanordnung weg.
- **Gesamtstrafen-Obergrenze** ueberschritten (§ 54 Abs. 2 StGB).
- **Mehrere Zaesuren** in komplexer Konstellation falsch geordnet.

## Querverweise

- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — Grundlagen.
- `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` — Sondersituation.
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung der neuen Gesamtstrafe.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Vollstreckungsmodalitaeten.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Begruendungspflicht.

## Quellen und Stand 05/2026

- § 55 StGB in der geltenden Fassung.
- §§ 53, 54 StGB.
- §§ 460, 462, 462a StPO.
- BGH-staendige Linie zu Zaesurwirkung, Einbeziehung und Schutzzweck — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.
