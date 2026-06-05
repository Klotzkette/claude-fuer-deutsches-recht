---
name: gesamtstrafenbildung-stgb-gestaendnis
description: "Gesamtstrafenbildung Stgb Gestaendnis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gesamtstrafenbildung Stgb Gestaendnis

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gesamtstrafenbildung Stgb Gestaendnis** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesamtstrafenbildung-53-54-stgb-erste-instanz` | Erstinstanzliche Gesamtstrafenbildung bei Realkonkurrenz §§ 53 und 54 StGB. Einzelstrafen werden zuerst gebildet; danach Gesamtstrafe aus der hoechsten Einzelstrafe (Einsatzstrafe) plus angemessener Erhoehung. Obergrenze § 54 Abs. 2 StGB. Sondergrenzen Geldstrafe vs. Freiheitsstrafe. Verhaeltnis zu Tateinheit § 52 StGB. Begruendungspflicht im Urteil. |
| `gestaendnis-und-strafmilderung` | Gestaendnis als Strafmilderungsgrund. Umfang Reichweite Glaubhaftigkeit. Differenzierung schlankes Gestaendnis vs. qualifiziertes Gestaendnis. Verbindung zu Reue und Wiedergutmachung. Wirkung in der Strafzumessung praktisch 25 bis 33 Prozent Rabatt; orientierender Faustwert. Doppelverwertung mit Verstaendigung vermeiden. Schweigen darf nicht schaerfend gewertet werden. |
| `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` | Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung wenn Einbeziehung nach § 55 StGB nicht moeglich ist (Strafe bereits vollstreckt, verjaehrt oder erlassen, Bewaehrung abgelaufen, Auslandsstrafen). BGH-staendige Linie: Schutzzweck des § 55 StGB rechtfertigt Strafabschlag als rechtspolitisches Ausgleichs-Element. Anwendung in Hauptverhandlung und Beschluss-Verfahren. Verteidigerantrag und Begruendungspflicht. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Gesamtstrafenbildung Stgb Gestaendnis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesamtstrafenbildung-53-54-stgb-erste-instanz`

**Fokus:** Erstinstanzliche Gesamtstrafenbildung bei Realkonkurrenz §§ 53 und 54 StGB. Einzelstrafen werden zuerst gebildet; danach Gesamtstrafe aus der hoechsten Einzelstrafe (Einsatzstrafe) plus angemessener Erhoehung. Obergrenze § 54 Abs. 2 StGB. Sondergrenzen Geldstrafe vs. Freiheitsstrafe. Verhaeltnis zu Tateinheit § 52 StGB. Begruendungspflicht im Urteil.

# Gesamtstrafenbildung — §§ 53 und 54 StGB

## Worum geht es?

Bei **Realkonkurrenz** (mehrere selbststaendige Taten in einem Verfahren) sind nach §§ 53 und 54 StGB zuerst die **Einzelstrafen** festzusetzen und daraus eine **Gesamtstrafe** zu bilden. Die hoechste Einzelstrafe ist die **Einsatzstrafe**; sie wird um eine angemessene Quote erhoeht. Die Gesamtstrafe darf weder die Summe der Einzelstrafen erreichen noch das gesetzliche Hoechstmass ueberschreiten.

## Wann brauchen Sie diese Skill?

- Sie bereiten ein Plaedoyer oder ein Urteil bei mehreren Taten vor.
- Sie pruefen ein Urteil im Revisionsverfahren auf Gesamtstrafen-Fehler.
- Sie verhandeln in einer Verstaendigung den Gesamtstrafrahmen.

## Rechtliche Grundlagen

- **§ 52 StGB** — Tateinheit (eine Strafe aus dem schwersten Tatbestand).
- **§ 53 Abs. 1 StGB** — Realkonkurrenz: Mehrere Taten in einem Verfahren; auf eine **Gesamtstrafe** ist zu erkennen.
- **§ 53 Abs. 2 StGB** — Trifft Freiheitsstrafe mit Geldstrafe zusammen, ist auf Gesamtstrafe zu erkennen. Geldstrafe kann nach pflichtgemaessem Ermessen gesondert verhaengt werden.
- **§ 54 StGB** — Bildung der Gesamtstrafe:
 - **Abs. 1**: Einsatzstrafe ist die hoechste Einzelstrafe; diese wird unter Beruecksichtigung der Person des Taeters und der einzelnen Straftaten erhoeht. Die Gesamtstrafe darf die Summe der Einzelstrafen nicht erreichen.
 - **Abs. 2 Satz 1**: Bei Freiheitsstrafe Hoechstgrenze 15 Jahre; bei lebenslang Hoechstgrenze lebenslang.
 - **Abs. 2 Satz 2**: Bei Geldstrafe Hoechstgrenze 720 Tagessaetze.
 - **Abs. 3**: Trifft Freiheitsstrafe und Geldstrafe zusammen, ist je 1 EUR Geldstrafe = 1 Tag Freiheitsstrafe umrechenbar (oder Geldstrafe gesondert).

## Strafzumessungs-Grundsatz

- **Schritt 1**: Jede einzelne Tat wird mit einer **Einzelstrafe** versehen (nach § 46 StGB).
- **Schritt 2**: Die **Einsatzstrafe** ist die hoechste der Einzelstrafen.
- **Schritt 3**: Die Einsatzstrafe wird um eine **angemessene Quote** erhoeht (nicht: einfache Addition; nicht: Verdoppelung).
- **Schritt 4**: Beachten der absoluten Grenzen (Hoechstmass; Summe der Einzelstrafen).
- **Verbot**: Die einzelne Strafe darf bei der Gesamtstrafenbildung nicht erneut strafschaerfend einfliessen (Doppelverwertungs-Variante).

## Faustwerte fuer die Erhoehung

| Fallgestaltung | Erhoehung der Einsatzstrafe |
|---|---|
| Wenige, sehr aehnliche Taten | ca. 25-50 % der Summe der weiteren Einzelstrafen |
| Mehrere unterschiedliche Taten | etwas hoeher |
| Schwere und leichte Taten gemischt | abhaengig vom Schwergewicht |

**Diese Werte sind orientierend**; das Gericht muss im Einzelfall die Person und die Einzeltaten konkret wuerdigen.

## Beispiel

- Tat 1: Diebstahl, Einzelstrafe 6 Monate.
- Tat 2: Koerperverletzung, Einzelstrafe 9 Monate.
- Tat 3: Beleidigung, Einzelstrafe 30 Tagessaetze.

Schritt-fuer-Schritt:

1. Einsatzstrafe = 9 Monate (hoechste Freiheitsstrafe).
2. Erhoehung: Tat 1 hinzu (6 Monate), Tat 3 hinzu (30 Tagessaetze).
3. Erhoehung nicht durch Addition (waere 15 Monate + 30 Tagessaetze), sondern durch angemessene Quote unter Wuerdigung.
4. Beispielsweise Gesamtstrafe: 1 Jahr 1 Monat.
5. Bei Geldstrafe daneben: Umrechnung der 30 Tagessaetze in 1 Monat Freiheitsstrafe (§ 54 Abs. 3 StGB), wenn keine gesonderte Geldstrafe verhaengt wird.

## Schritt-fuer-Schritt-Anleitung (Gericht / Verteidigung)

1. **Einzelne Taten** identifizieren und je nach § 46 StGB konkrete Einzelstrafe festsetzen.
2. **Einsatzstrafe** = hoechste Einzelstrafe.
3. **Gesamtstrafen-Spielraum** bestimmen: Einsatzstrafe + 1 Monat (Mindest) bis Summe (Maximum, nicht erreichend).
4. **Wuerdigung**:
 - Person des Taeters: Vorleben, soziale Lage.
 - Tatbild: aehnliche Taten, neue Schaden, gleiches Opfer.
 - Inneres Tatbild: zeigt sich kriminelle Karriere oder Spontantat?
5. **Gesamtstrafe** im Spielraum festlegen.
6. **§ 54 Abs. 2 StGB Hoechstgrenzen**: zeitige Freiheitsstrafe max. 15 Jahre; Geldstrafe max. 720 Tagessaetze.
7. **Begruendung** im Urteil: Einzelstrafen, Einsatzstrafe, Erhoehungsbruchteil, Spielraum, finale Gesamtstrafe (§ 267 Abs. 3 StPO).

## Sonderkonstellationen

### Mehrere Geldstrafen

- Gesamtgeldstrafe nach § 53 Abs. 2 i.V.m. § 54 Abs. 2 Satz 2 StGB.
- Hoechstgrenze 720 Tagessaetze.
- Tagessatzhoehe wird in der Gesamtgeldstrafe einheitlich festgesetzt (§ 54 Abs. 3 StGB).

### Freiheitsstrafe und Geldstrafe

- Auf Gesamtstrafe (Freiheitsstrafe) zu erkennen.
- Geldstrafe in Freiheitsstrafe-Tage umrechnen (§ 54 Abs. 3 StGB: 1 Tagessatz = 1 Tag Freiheitsstrafe) oder Geldstrafe gesondert (§ 53 Abs. 2 Satz 2 StGB).
- Geldstrafe **neben** Freiheitsstrafe nur bei Bereicherungsabsicht (§ 41 StGB) — Vorsicht: nicht verwechseln.

### Lebenslange Freiheitsstrafe und zeitige Freiheitsstrafe

- Gesamtstrafe ist **lebenslang** (§ 54 Abs. 1 Satz 3 StGB).
- Reststrafenaussetzung nach § 57a, 57b StGB.

### Tateinheit (§ 52 StGB) zwischen mehreren Taten

- Bei Tateinheit gibt es nur **eine** Strafe aus dem schwersten Tatbestand.
- Bei Realkonkurrenz (verschiedene Handlungen) gibt es Einzelstrafen, dann Gesamtstrafe.

## Typische Fehler

- **Einzelstrafen weggelassen**: das Urteil muss jede Einzelstrafe ausweisen, sonst Strafzumessungsmangel.
- **Einsatzstrafe falsch** (nicht die hoechste).
- **Gesamtstrafe = Summe**: Verstoss gegen § 54 Abs. 1 Satz 2 StGB.
- **Erhoehung pauschal** ohne Begruendung der Person und der Einzeltaten.
- **Geldstrafe + Freiheitsstrafe** Umrechnung uebersehen oder falsch (§ 54 Abs. 3 StGB).
- **Verlautete Bewaehrungsfaehigkeit** bei Gesamtstrafe nahe 2 Jahre uebersehen.

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Einzelstrafen-Bildung.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen vor jeder Einzelstrafe.
- `nachtraegliche-gesamtstrafenbildung-55-stgb` — wenn Verurteilungen aus verschiedenen Verfahren stammen.
- `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` — Sondersituation.
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrungsperspektive bei Gesamtstrafe.

## Quellen und Stand 05/2026

- §§ 52, 53, 54 StGB in der geltenden Fassung.
- §§ 38, 39, 41 StGB.
- § 267 Abs. 3 StPO Begruendung.
- Quellenregel: vgl. `references/zitierweise.md`.

## 2. `gestaendnis-und-strafmilderung`

**Fokus:** Gestaendnis als Strafmilderungsgrund. Umfang Reichweite Glaubhaftigkeit. Differenzierung schlankes Gestaendnis vs. qualifiziertes Gestaendnis. Verbindung zu Reue und Wiedergutmachung. Wirkung in der Strafzumessung praktisch 25 bis 33 Prozent Rabatt; orientierender Faustwert. Doppelverwertung mit Verstaendigung vermeiden. Schweigen darf nicht schaerfend gewertet werden.

# Gestaendnis und Strafmilderung

## Worum geht es?

Das Gestaendnis ist nach § 46 Abs. 2 StGB ein wesentliches Element des Nachtatverhaltens. Praktisch ist es der haeufigste Strafmilderungsgrund. Reichweite, Zeitpunkt und Echtheit des Gestaendnisses beeinflussen das Mass der Milderung.

## Wann brauchen Sie diese Skill?

- Sie beraten den Mandanten, ob er sich einlassen oder gestehen soll.
- Sie bereiten den Schlussvortrag vor und stellen den Strafmilderungsgrund heraus.
- Sie pruefen, ob das Gericht das Gestaendnis ausreichend gewichtet hat.

## Rechtliche Grundlagen

- **§ 46 Abs. 2 StGB** — Nachtatverhalten, namentlich Bemuehen um Schadenswiedergutmachung und Ausgleich.
- **§ 136 StPO** — Belehrung; Schweigen darf nicht zum Nachteil gewertet werden.
- **§ 243 Abs. 5 StPO** — Schweigerecht zur Sache.
- **§ 257c StPO** — Verstaendigung; Gestaendnis oft Voraussetzung.

## Strafzumessungs-Grundsatz

- **Schweigen ist kein Schuldzugestaendnis** und darf nicht strafschaerfend gewertet werden (st. Rspr. seit BGHSt 25, 365 ff.; Aktenzeichen vor Zitat verifizieren).
- **Gestaendnis** ist ein klassischer Strafmilderungsgrund, weil es:
 - Reue und Einsicht zeigt;
 - die Beweisaufnahme verkuerzt (prozessoekonomischer Wert);
 - das Opfer entlastet (keine ueberlange Vernehmung).
- **Tat-Verschleierung** in der Hauptverhandlung darf nicht **schaerfend** gewertet werden, soweit sie sich im Rahmen zulaessiger Verteidigung bewegt.

## Arten von Gestaendnissen

### Schlankes Gestaendnis

- Knappes "Ja, das stimmt"-Gestaendnis.
- Wirkt strafmildernd, aber begrenzt.
- Geringerer Rabatt bei Verstaendigung.

### Qualifiziertes Gestaendnis

- Detailliertes Eingestaendnis von Tatablauf, Beweggrund, Folgen.
- Verbunden mit Reue und Wiedergutmachung.
- Erheblich strafmildernd.

### Teilgestaendnis

- Nur eines von mehreren Vorwuerfen wird eingestanden.
- Wirkt nur fuer die eingestandene Tat.
- Vorsicht: kein Gestaendnis = kein automatisches Bestreiten der anderen Vorwuerfe.

### Spaetes Gestaendnis

- Erst kurz vor Schluss der Beweisaufnahme.
- Geringerer prozessoekonomischer Wert.
- Geringere Milderungswirkung.

### Fruehes Gestaendnis

- Bereits im Ermittlungsverfahren.
- Hoher Wert: Ermittlungsoekonomie, Opferschutz, Hinweis auf Einsicht.

## Faustwerte Gestaendnis-Wirkung

| Konstellation | Orientierender Rabatt |
|---|---|
| Frueh, vollstaendig, mit Reue | 25-33 % |
| Frueh, schlank | 10-20 % |
| Spaet, vollstaendig | 10-20 % |
| Spaet, schlank | 0-10 % |
| Im Rahmen Verstaendigung | meist 25-33 % |
| Aufrichtiges Gestaendnis + TOA | bis 50 % oder Absehen von Strafe (§ 46a StGB) |

**Diese Werte sind orientierend** und durch die Rechtsprechung des einschlaegigen Tatgerichts gepraegt.

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Mandantengespraech**: Beweislage und Risiko ohne Gestaendnis besprechen.
2. **Beweislage** pruefen:
 - Belastungszeugen, Geschaedigtenaussage, Sachbeweise.
 - Eigene Verteidigungs-Hebel (Aussagepsychologie, Aussage gegen Aussage).
3. **Entscheidung**: Schweigen, Bestreiten, Teil-Gestaendnis, vollstaendiges Gestaendnis.
4. **Zeitpunkt**: Frueher meist besser; in komplexen Faellen erst nach Akteneinsicht.
5. **Form**:
 - Schriftliche Einlassung verlesen.
 - Verbindung mit Reue, Schadenswiedergutmachung, TOA.
6. **In der Hauptverhandlung**: Gestaendnis als zentrales Strafmilderungselement im Plaedoyer aufgreifen.

## Schritt-fuer-Schritt-Anleitung (Anklage)

- Strafzumessungs-Antrag beruecksichtigt Gestaendnis-Wirkung.
- Bei Verstaendigung Strafrahmen-Vorschlag entsprechend.
- Vorsicht: Schweigen darf nicht schaerfend gewertet werden.

## Wechselwirkung mit § 46a StGB (TOA)

- Gestaendnis + TOA: starke Kombination.
- Bei Strafe nicht ueber 1 Jahr Absehen von Strafe nach § 46a StGB moeglich.
- Reine Schadenswiedergutmachung ohne kommunikativen Prozess reicht nicht (BGH 4 StR 232/25 vom 20.11.2025); Gestaendnis kann den kommunikativen Prozess stuetzen.

## Wechselwirkung mit Verstaendigung

- Gestaendnis ist meist Voraussetzung der Verstaendigung.
- **Doppelverwertung vermeiden**: Gestaendnis als Strafmilderungsgrund in § 46 StGB **und** als Verstaendigungs-"Gegenleistung" — beides ist verzahnt; das Urteil muss die Strafzumessung sauber begruenden.

## Typische Fehler

- **Schweigen** strafschaerfend gewertet — revisionsanfaellig.
- **Gestaendnis** nicht ausreichend gewichtet im Urteil (§ 267 Abs. 3 StPO).
- **Strafmilderung** wegen Gestaendnisses und Verstaendigung doppelt berechnet.
- **Verspaetetes Gestaendnis** ueberschaetzt: geringerer Wert.
- **Falsches Gestaendnis** (Schutzbehauptung) kann sich strafschaerfend auswirken oder zu falsa demonstrans-Problem fuehren — Mandanten ausfuehrlich beraten.

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Grundsatz.
- `strafzumessungs-tatsachen-46-ii-stgb` — Detailkatalog.
- `verstaendigung-257c-stpo-strafzumessung` — Verzahnung Verstaendigung.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — Kombination TOA.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Urteilsbegruendung.

## Quellen und Stand 05/2026

- § 46 Abs. 2 StGB in der geltenden Fassung.
- §§ 136, 243 Abs. 5, 257c StPO.
- BGH zur Bewertung des Schweigens — Aktenzeichen verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

## 3. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`

**Fokus:** Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung wenn Einbeziehung nach § 55 StGB nicht moeglich ist (Strafe bereits vollstreckt, verjaehrt oder erlassen, Bewaehrung abgelaufen, Auslandsstrafen). BGH-staendige Linie: Schutzzweck des § 55 StGB rechtfertigt Strafabschlag als rechtspolitisches Ausgleichs-Element. Anwendung in Hauptverhandlung und Beschluss-Verfahren. Verteidigerantrag und Begruendungspflicht.

# Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung

## Worum geht es?

Wenn eine nachtraegliche Gesamtstrafenbildung nach § 55 StGB **nicht** moeglich ist — typischerweise weil die fruehere Strafe bereits vollstreckt, verjaehrt oder erlassen ist (auch nach abgelaufener Bewaehrung) —, kann der **Haerteausgleich** als nicht-kodifiziertes, von der staendigen Rechtsprechung entwickeltes Instrument zum Tragen kommen. Er gleicht die zufaelligen Nachteile aus, die durch die getrennte Aburteilung entstehen.

**BGH-staendige Linie**: Der Schutzzweck des § 55 StGB darf nicht durch verfahrenstechnische Zufaelle (Reihenfolge der Verurteilungen, Tempo der Vollstreckung, Ausland) entwertet werden. Wenn eine Einbeziehung an einem ausserhalb der Schuld liegenden Umstand scheitert, ist ein Strafabschlag zu gewaehren. **Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.**

## Wann brauchen Sie diese Skill?

- Mandant ist bereits einmal verurteilt; die fruehere Strafe wurde mittlerweile vollstreckt oder die Bewaehrung ist erlassen worden.
- Eine weitere Tat des Mandanten, die er **vor** der frueheren Verurteilung begangen hat, wird nun abgeurteilt.
- Sie pruefen ein Urteil, das die Sondersituation uebersehen hat.
- Auslandsstrafen liegen vor und koennen nicht einbezogen werden.

## Rechtliche Grundlagen

- **§ 55 StGB** — Nachtraegliche Gesamtstrafenbildung; vgl. `nachtraegliche-gesamtstrafenbildung-55-stgb`.
- **§ 46 StGB** — Strafzumessungsgrundsatz; Haerteausgleich wird als Strafzumessungsfaktor in die konkrete Strafe eingearbeitet.
- **§ 267 Abs. 3 StPO** — Begruendung; Haerteausgleich muss als bestimmender Strafzumessungsgrund mitgeteilt werden.
- **BGH-staendige Linie**: Schutzzweck des § 55 StGB rechtfertigt rechnerischen Strafabschlag bei zufaelliger Nichteinbeziehung. Aktenzeichen verifizieren.

## Konstellationen, die typisch Haerteausgleich ausloesen

### 1. Fruehere Strafe vollstreckt

Wird die fruehere Strafe vor der jetzigen Verurteilung vollstaendig vollstreckt, kann sie nicht mehr in eine Gesamtstrafe einbezogen werden. Der Verurteilte ist gegenueber einer gemeinsamen Aburteilung schlechter gestellt.

### 2. Bewaehrungszeit abgelaufen / Strafe erlassen (§ 56g StGB)

Wird die Bewaehrung gluecklich beendet und die Strafe erlassen, kann sie nicht mehr einbezogen werden. Auch hier waere eine gemeinsame Aburteilung guenstiger gewesen.

### 3. Verjaehrung der frueheren Strafe

Die Strafe ist verjaehrt; keine Einbeziehung mehr.

### 4. Auslandsstrafen

Auslandsstrafen werden grundsaetzlich **nicht** in eine nachtraegliche Gesamtstrafe nach § 55 StGB einbezogen (st. Rspr.; Az verifizieren). Ein Haerteausgleich kann bei rein "schicksalhaft" zustandegekommener Auslandsstrafe geboten sein.

### 5. Strafe aus Strafbefehl bereits gezahlt

Eine vollstaendig gezahlte Geldstrafe aus Strafbefehl wird nicht einbezogen.

## Hoehe und Form des Haerteausgleichs

- **Kein** starres Berechnungsschema.
- **Orientierung**: Was waere die Gesamtstrafe gewesen, wenn beide Taten in einem Verfahren abgeurteilt worden waeren?
- **Differenz** zwischen hypothetischer Gesamtstrafe und kumulierten Einzelstrafen kann als Massstab dienen.
- **Strafabschlag** wird auf die nunmehr zu verhaengende Strafe angerechnet — entweder durch Senkung der Einzelstrafe oder durch ausdruecklichen Abschlag in der Strafzumessungsbegruendung.

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Vorverurteilungen** und Status pruefen: BZRG-Auszug, Vollstreckungsakte, Bewaehrungsentscheidungen.
2. **Zaesur-Pruefung**: Wurde die abzuurteilende Tat **vor** der frueheren Verurteilung begangen?
3. **Einbeziehung pruefen** (§ 55 StGB):
 - Ist die fruehere Strafe noch offen? Dann § 55 StGB; vgl. `nachtraegliche-gesamtstrafenbildung-55-stgb`.
 - Ist sie schon vollstreckt / erlassen / verjaehrt? Dann **Haerteausgleich**.
4. **Antrag** in der Hauptverhandlung oder im Schriftsatz:

 ```
 Wir beantragen, bei der Strafzumessung einen Haerteausgleich
 zu gewaehren, da die Tat vom [Datum] vor der Verurteilung
 vom [Datum] begangen wurde und eine Einbeziehung in eine
 Gesamtstrafe nach § 55 StGB allein deshalb ausscheidet,
 weil die damals verhaengte Strafe inzwischen [vollstreckt /
 erlassen / verjaehrt] ist. Eine gemeinsame Aburteilung haette
 zu einer wesentlich niedrigeren Gesamtstrafe gefuehrt.
 ```

5. **Hoehe** des Haerteausgleichs vortragen:
 - Hypothetische Gesamtstrafe bei gemeinsamer Aburteilung berechnen.
 - Differenz zwischen dieser hypothetischen Gesamtstrafe und der jetzt zu erwartenden kumulierten Strafenlast.
 - Strafabschlag konkret beantragen (z.B. "Strafabschlag von [X] Monaten" oder "Reduktion der zu verhaengenden Strafe um etwa [X] %").
6. **Begruendungspflicht** im Urteil: Das Gericht muss den Haerteausgleich als bestimmenden Strafzumessungsgrund angeben (§ 267 Abs. 3 StPO).

## Verhaeltnis zu § 55 StGB

| Situation | Rechtsfolge |
|---|---|
| Fruehere Strafe noch offen | § 55 StGB Einbeziehung; nachtraegliche Gesamtstrafe |
| Fruehere Strafe vollstreckt / verjaehrt / erlassen | **Haerteausgleich** im Rahmen § 46 StGB |
| Tat **nach** Vorverurteilung begangen (Zaesur uebersprungen) | Weder § 55 StGB noch Haerteausgleich; reguläre Einzelstrafe |
| Auslandsstrafen | § 55 StGB scheidet aus; Haerteausgleich in Ausnahmefaellen |

## Sonderkonstellationen

### Bewaehrungswiderruf-Drohung

Wenn die fruehere Strafe noch in Bewaehrung laeuft, ist die Einbeziehung nach § 55 StGB zumeist guenstiger als ein Bewaehrungswiderruf (§ 56f StGB) + getrennte neue Strafe. Verteidiger pruefen, welcher Weg wirtschaftlich besser ist; vgl. `bewaehrungswiderruf-56f-stgb`.

### Mehrere Zaesuren

Bei mehreren Vorverurteilungen ist sorgfaeltig zu pruefen, welche Strafen einbeziehbar sind und welche nicht — und ob fuer die nicht einbeziehbaren ein Haerteausgleich vorzunehmen ist.

### Geldstrafe schon gezahlt

Auch eine bereits gezahlte Geldstrafe kann Haerteausgleich begruenden, wenn sie haette einbezogen werden koennen (st. Rspr.; Az verifizieren).

## Begruendung im Urteil (Muster-Element)

```
[...] Bei der Strafzumessung war zu beruecksichtigen, dass die hier
abzuurteilende Tat vor der Verurteilung des Angeklagten durch
[Gericht] vom [Datum] (Az.: [...]) begangen wurde. Eine Einbeziehung
der damals verhaengten Strafe von [Einzelstrafe] in eine Gesamtstrafe
nach § 55 StGB ist nicht moeglich, da diese Strafe bereits vollstaendig
[vollstreckt / erlassen / verjaehrt] ist.

Es waere eine Gesamtstrafe von voraussichtlich [hypothetische Strafe]
gebildet worden. Daraus errechnet sich eine zu beruecksichtigende
Haerte, die das Gericht durch einen Abschlag von [X] Monaten
ausgleicht. Die Strafe von [konkrete Strafe] beruecksichtigt diesen
Haerteausgleich.
```

## Typische Fehler

- **Haerteausgleich uebersehen**: revisionsrechtlich relevanter Strafzumessungsmangel.
- **Hoehe pauschal**: Das Gericht muss die hypothetische Gesamtstrafe und die Differenz nachvollziehbar machen.
- **Verwechslung mit § 55 StGB**: Haerteausgleich ist subsidiaer; vorrangig ist die Einbeziehung nach § 55 StGB.
- **§ 55 StGB-Voraussetzungen** nicht systematisch geprueft: zuerst Zaesur, dann Status der frueheren Strafe.
- **Bewaehrungsstrafe** als "erlassen" angesehen, obwohl die Bewaehrung noch laeuft.
- **Auslandsstrafen** automatisch als haerteausgleichsbeduerftig gewertet — die st. Rspr. ist hier restriktiver; Einzelfallpruefung.

## Quellen-Recherche-Hinweis

Die BGH-Rspr. zum Haerteausgleich bei nicht moeglicher Einbeziehung nach § 55 StGB ist umfangreich und gefestigt; Leitentscheidungen finden sich beispielsweise in BGHSt-Bestaenden zur Gesamtstrafenbildung. **Vor Zitat im Schriftsatz immer Aktenzeichen in dejure.org oder openjur.de verifizieren**, da konkrete Az nicht aus Modellwissen uebernommen werden duerfen (vgl. Quellenregel `references/zitierweise.md`).

## Querverweise

- `nachtraegliche-gesamtstrafenbildung-55-stgb` — Mutternorm.
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — Grundlagen.
- `bewaehrungswiderruf-56f-stgb` — Alternativ-Pfad bei laufender Bewaehrung.
- `paragraph-46-stgb-grundsatz-strafzumessung` — Einbettung in Strafzumessung.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Begruendungspflicht im Urteil.

## Quellen und Stand 05/2026

- § 55 StGB in der geltenden Fassung.
- §§ 53, 54, 56g StGB.
- § 267 Abs. 3 StPO.
- BGH-staendige Linie zum Haerteausgleich bei nicht moeglicher Einbeziehung — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.
