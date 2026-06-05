---
name: klausurloesungen-fehlerdiagnose-konsens
description: "Klausurloesungen Fehlerdiagnose Konsens: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klausurloesungen Fehlerdiagnose Konsens

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Klausurloesungen Fehlerdiagnose Konsens** im Plugin Bgb At Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klausurloesungen-fehlerdiagnose` | Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüfungsreihenfolge (Auslegung vor Anfechtung), übersehene Normen wie § 122 BGB und § 179 BGB, unvollständige Subsumtion. Output: annotiertes Feedback und Verbesserungsvorschläge. |
| `konsens-dissens-paragraphen-154-155` | Prüft offenen und versteckten Dissens nach §§ 154 und 155 BGB: fehlende Einigung über Nebenpunkte, Vorbehalt der Beurkundung, ergänzende Vertragsauslegung als Heilungsmechanismus, Abgrenzung von Anfechtung und Dissens. Klausurfall mit Lösungsskizze. |
| `missbrauch-vertretungsmacht` | Klausurfall zum Missbrauch der Vertretungsmacht: kollusives Zusammenwirken von Vertreter und Drittem zum Nachteil des Vertretenen, Kenntnis oder Kennenmüssen des Dritten, Rechtsfolge der Unwirksamkeit analog § 138 BGB oder § 242 BGB. BGH-Linie zum Evidenzmaßstab. |

## Arbeitsweg

Im Plugin Bgb At Pruefer gilt für **Klausurloesungen Fehlerdiagnose Konsens**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klausurloesungen-fehlerdiagnose`

**Fokus:** Analysiert fehlerhafte Klausurlösungen im BGB Allgemeiner Teil: typische Aufbaufehler beim Anspruchsaufbau, falsche Prüfungsreihenfolge (Auslegung vor Anfechtung), übersehene Normen wie § 122 BGB und § 179 BGB, unvollständige Subsumtion. Output: annotiertes Feedback und Verbesserungsvorschläge.

# Klausurlösungen — Fehlerdiagnose und Verbesserung

## Mandantenfall

- Examenskandidat hat Klausurlösung zu § 119 BGB eingereicht — Auslegung fehlt, Motivirrtum als Anfechtungsgrund gewertet.
- Student prüft § 164 BGB ohne Offenkundigkeit zu erörtern und übersieht den vollmachtlosen Vertreter.
- Klausurkonstellation: Gutachtenstil-Mängel — Ergebnis steht vor Begründung, Normen fehlen.

## Erste Schritte

1. Prüfungsreihenfolge kontrollieren: Anspruchsgrundlage — Tatbestand — Subsumtion — Ergebnis.
2. Vorrang der Auslegung (§§ 133 und 157 BGB) vor Anfechtung, Dissens und Lückenfüllung prüfen.
3. Übersehene Normen identifizieren: § 122 BGB bei Anfechtung, § 179 BGB bei Vertretung ohne Vollmacht.
4. Subsumtion auf Vollständigkeit prüfen: Norm — Tatbestandsmerkmal — Sachverhalt — Rechtsfolge.
5. Gutachtenstil vs. Urteilsstil: Im Gutachten Ergebnis nicht vorwegnehmen.
6. Feedback formulieren: konkret, normenbezogen, mit Korrekturanweisung.

## Rechtsrahmen

- §§ 133 und 157 BGB: Auslegung als vorrangige Prüfungsstufe.
- § 119 BGB: Anfechtungsrecht — Irrtumskategorien und Motivirrtum.
- § 122 BGB: Schadensersatzpflicht des Anfechtenden — häufig übersehen.
- § 164 BGB: Stellvertretung — Offenkundigkeit als Tatbestandsmerkmal.
- § 179 BGB: Haftung des Vertreters ohne Vertretungsmacht.

## Prüfraster

1. Aufbaurüge: Entspricht die Prüfungsstruktur dem Anspruchsaufbau (Wer will was von wem woraus)?
2. Auslegungsvorrang: Wurde Auslegung vor Anfechtung und Dissens geprüft?
3. Normzitate: Sind alle einschlägigen Normen genannt und korrekt zitiert?
4. Subsumtion: Ist jedes Tatbestandsmerkmal auf den Sachverhalt angewendet?
5. Rechtsfolge: Ist die Rechtsfolge der einschlägigen Norm korrekt benannt?
6. Gutachtenstil-Einhaltung: Kein Ergebnis vor Begründung im Obersatz.
7. Fehlende Folgeprüfungen (§§ 122 und 179 BGB) ergänzt?

## Typische Fallstricke

- Motivirrtum als Anfechtungsgrund nach § 119 Abs. 1 BGB zu werten ist ein klassischer Fehler.
- § 122 BGB wird systematisch übersehen — immer nach erfolgreicher Anfechtung prüfen.
- Offenkundigkeit bei § 164 BGB fehlt häufig — kein Stellvertretungseffekt ohne sie.
- Urteilsstil in Klausuren verwenden statt Gutachtenstil ist ein Bewertungsmangel.

## Output

- Annotiertes Feedback zur eingereichten Lösung mit Zeilennummern
- Rangliste der schwerwiegendsten Fehler nach Punktgewichtung
- Musterlösung-Skizze für den fehlerhaften Abschnitt
- Wiederholungscheckliste für häufige BGB-AT-Klausurfehler

## Quellen

- [§ 133 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__133.html)
- [§ 119 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__119.html)
- [§ 122 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__122.html)
- [§ 179 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [dejure.org § 164 BGB](https://dejure.org/gesetze/BGB/164.html)

## Vertiefung

### Systematisches Fehler-Tracking

Für die Klausurvorbereitung empfiehlt sich ein persönliches Fehlerprotokoll: Welche Normen werden
regelmäßig übersehen? Wo fehlt die Subsumtion? Wo wird der Gutachtenstil verletzt? Systematische
Wiederholung der häufigsten Fehler beschleunigt den Lernfortschritt erheblich.

### Punktgewichtung in der Klausur

BGB-AT-Klausuren gewichten: Anspruchsaufbau (5-10 %), Tatbestandsprüfung (40-50 %), Subsumtion
(20-30 %), Ergebnis (5-10 %), Gutachtenstil (10-20 %). Fehler in der Subsumtion kosten die meisten
Punkte.

### Klausur-Checkliste Fehlerdiagnose

- Falsche Anspruchsgrundlage gewählt?
- Auslegung vor Anfechtung unterlassen?
- Tatbestandsmerkmale unvollständig oder falsch definiert?
- § 122 BGB nach Anfechtung übersehen?
- Gutachtenstil verletzt (Ergebnis vor Begründung)?

## 2. `konsens-dissens-paragraphen-154-155`

**Fokus:** Prüft offenen und versteckten Dissens nach §§ 154 und 155 BGB: fehlende Einigung über Nebenpunkte, Vorbehalt der Beurkundung, ergänzende Vertragsauslegung als Heilungsmechanismus, Abgrenzung von Anfechtung und Dissens. Klausurfall mit Lösungsskizze.

# Konsens und Dissens — §§ 154 und 155 BGB

## Mandantenfall

- Parteien haben Preis vereinbart, aber Lieferzeitpunkt offen gelassen — versteckter Dissens nach § 155 BGB?
- Vertragsverhandlungen scheitern daran, dass Parteien aneinander vorbeigeredet haben — offener Dissens?
- Klausurkonstellation: Kauf eines Grundstücks, Parteien einig über Preis aber streiten über mitverkauftes Inventar.

## Erste Schritte

1. Vertragsschluss prüfen: Haben Angebot und Annahme sich gedeckt (kongruente Willenserklärungen)?
2. Offener Dissens (§ 154 BGB): Parteien wissen, dass sie sich über einen Punkt nicht geeinigt haben — kein Vertrag.
3. Versteckter Dissens (§ 155 BGB): Parteien glauben sich einig, sind es aber nicht — kein Vertrag in der Regel.
4. Wesentliche vs. unwesentliche Punkte: Betrifft der Dissens essentialia negotii?
5. Ergänzende Vertragsauslegung nach §§ 133 und 157 BGB als Heilungsmittel prüfen.
6. Beurkundungsvorbehalt nach § 154 Abs. 2 BGB: Kein Vertrag bis zur Beurkundung.

## Rechtsrahmen

- § 154 Abs. 1 BGB: Offener Dissens — kein Vertrag solange Einigung fehlt.
- § 154 Abs. 2 BGB: Beurkundungsvorbehalt — kein Vertrag bis Beurkundung.
- § 155 BGB: Versteckter Dissens — Vertrag soweit der Einigung erstreckt.
- §§ 133 und 157 BGB: Auslegung und ergänzende Vertragsauslegung.
- § 242 BGB: Treu und Glauben bei Dissens-Einwand nach vollständiger Leistung.

## Prüfraster

1. Übereinstimmende Willenserklärungen: Decken sich Angebot und Annahme vollständig?
2. Offener Dissens (§ 154 Abs. 1 BGB): Wissen die Parteien von der fehlenden Einigung?
3. Beurkundungsvorbehalt (§ 154 Abs. 2 BGB): Gibt es eine solche Vereinbarung?
4. Versteckter Dissens (§ 155 BGB): Glauben die Parteien irrtümlich, einig zu sein?
5. Wesentlichkeit des Dissens-Punktes: Essentialia negotii oder Nebenpunkt?
6. Ergänzende Vertragsauslegung: Kann der offene Punkt nach §§ 133 und 157 BGB gefüllt werden?
7. § 242 BGB: Rechtsmissbrauch bei Dissens-Berufung nach vollständiger Leistung?

## Typische Fallstricke

- Versteckter Dissens (§ 155 BGB) ist schwerer zu erkennen als offener Dissens — genau auf Übereinstimmung der Erklärungen achten.
- Ergänzende Vertragsauslegung ist kein Allheilmittel — nur bei Vertragslücke, nicht bei fehlendem Konsens.
- Beurkundungsvorbehalt nach § 154 Abs. 2 BGB führt zu Formzwang — oft übersehen.
- Anfechtung wegen Irrtums und Dissens schließen sich nicht aus, aber sind sorgfältig abzugrenzen.

## Output

- Gutachtenstil-Abschnitt zu §§ 154 und 155 BGB
- Prüfampel: Vertrag zustande gekommen / Dissens / Heilung durch Auslegung möglich
- Klausurlösungsskizze mit Abgrenzung offener/versteckter Dissens
- Rückfragenliste zu Vertragsverhandlungsprotokollen und Nebenpunkten

## Quellen

- [§ 154 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__154.html)
- [§ 155 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__155.html)
- [§ 157 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__157.html)
- [dejure.org § 154 BGB](https://dejure.org/gesetze/BGB/154.html)
- [dejure.org § 155 BGB](https://dejure.org/gesetze/BGB/155.html)

## Vertiefung

### Dissens-Dogmatik

Dissens bedeutet: Die Willenserklärungen der Parteien decken sich nicht vollständig. Beim offenen
Dissens (§ 154 Abs. 1 BGB) wissen die Parteien, dass sie sich noch nicht geeinigt haben. Beim
versteckten Dissens (§ 155 BGB) glauben beide, es bestehe Einigkeit — tatsächlich verstehen sie
aber das Gleiche unterschiedlich.

### Anwendung in der Klausur

Dissens prüfen, wenn: Parteien über Nebenpunkte streiten, Erklärungen inhaltlich nicht übereinstimmen
oder Parteien aneinander vorbeigeredet haben. Dann: Einigen sich auf das Übereinstimmende soweit
möglich (§ 155 BGB), der Rest ist offen.

### Klausur-Checkliste Dissens

- Haben Angebot und Annahme sich vollständig gedeckt?
- Offener Dissens § 154 BGB: Wussten Parteien, dass ein Punkt offen ist?
- Beurkundungsvorbehalt § 154 Abs. 2 BGB: Vereinbart und noch nicht beurkundet?
- Versteckter Dissens § 155 BGB: Parteien haben trotz Unterschiede geglaubt, einig zu sein?
- Ergänzende Auslegung: Kann Lücke nach §§ 133 und 157 BGB geschlossen werden?

## 3. `missbrauch-vertretungsmacht`

**Fokus:** Klausurfall zum Missbrauch der Vertretungsmacht: kollusives Zusammenwirken von Vertreter und Drittem zum Nachteil des Vertretenen, Kenntnis oder Kennenmüssen des Dritten, Rechtsfolge der Unwirksamkeit analog § 138 BGB oder § 242 BGB. BGH-Linie zum Evidenzmaßstab.

# Missbrauch der Vertretungsmacht

## Mandantenfall

- Geschäftsführer verkauft GmbH-Vermögen unter Wert an befreundeten Dritten — Missbrauch der Vertretungsmacht.
- Vertreter schließt für Auftraggeber nachteiligen Vertrag mit eigenem wirtschaftlichem Vorteil — kollusives Handeln?
- Klausurkonstellation: Bankmitarbeiter bevollmächtigt, überweist Kundengelder an eigenes Konto — Wirksamkeit?

## Erste Schritte

1. Vorliegen einer wirksamen Vollmacht bestätigen — Missbrauch setzt Vertretungsmacht voraus.
2. Überschreitung des Innenverhältnisses prüfen: Vertreter handelt außerhalb der internen Bindung.
3. Kollusion: Vertreter und Dritter handeln bewusst zum Nachteil des Vertretenen.
4. Evidenz: Missbrauch war für den Dritten offenkundig oder er kannte das Innenverhältnis.
5. Rechtsfolge bestimmen: § 138 BGB (Sittenwidrigkeit bei Kollusion) oder § 242 BGB (Einwendung).
6. Schadensersatzansprüche des Vertretenen gegen Vertreter nach §§ 280 und 249 BGB prüfen.

## Rechtsrahmen

- § 164 BGB: Stellvertretung — Vertretungsmacht als Grundlage.
- § 138 BGB: Sittenwidrigkeit — Rechtsfolge bei kollusivem Missbrauch.
- § 242 BGB: Treu und Glauben — Einwendung gegen evidenten Missbrauch ohne Kollusion.
- §§ 280 und 249 BGB: Schadensersatz gegen missbrauchenden Vertreter.
- § 166 BGB: Wissenszurechnung — Kenntnis des Vertreters wirkt für und gegen Vertretenen.

## Prüfraster

1. Wirksame Vollmacht des Vertreters im Außenverhältnis? (Sonst § 177 BGB prüfen)
2. Überschreitung des Innenverhältnisses: Vertreter handelt gegen interne Bindung?
3. Kollusion: Beweisbar gemeinschaftliches Handeln von Vertreter und Drittem zum Nachteil?
4. Evidenz beim Dritten: Kannte oder musste der Dritte den Missbrauch kennen?
5. Rechtsfolge: § 138 BGB (Nichtigkeit) oder § 242 BGB (Einwendung) — Abgrenzung nach BGH?
6. Schadensersatz des Vertretenen gegen den Vertreter (§§ 280 und 249 BGB)?
7. Herausgabe des erlangten Vorteils (§ 812 BGB) beim kollusiven Dritten?

## Typische Fallstricke

- Missbrauch der Vertretungsmacht unterscheidet sich von Überschreitung der Vertretungsmacht — Vollmacht besteht!
- Nur evident erkennbarer Missbrauch führt zu § 242 BGB — bloße Verdachtsmomente reichen nicht.
- Bei Kollusion ist § 138 BGB die richtige Rechtsfolge, nicht § 242 BGB.
- § 166 BGB-Wissenszurechnung kann zu Lasten des Vertretenen wirken — Doppelwirkung beachten.

## Output

- Gutachtenstil-Abschnitt zum Missbrauch der Vertretungsmacht
- Prüfampel: Vertrag wirksam / nichtig nach § 138 BGB / Einwendung nach § 242 BGB
- Klausurlösungsskizze mit Schadensersatz-Folgeprüfung
- Rückfragenliste zu Vollmachtsumfang und Drittkenntnis

## Quellen

- [§ 164 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__164.html)
- [§ 138 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__138.html)
- [§ 242 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__242.html)
- [dejure.org § 164 BGB](https://dejure.org/gesetze/BGB/164.html)
- [dejure.org § 138 BGB](https://dejure.org/gesetze/BGB/138.html)

## Vertiefung

### BGH-Evidenzmaßstab

Der BGH hat in mehreren Entscheidungen den Evidenzmaßstab für den Missbrauch der Vertretungsmacht
geprägt: Der Missbrauch muss für den Dritten ohne Weiteres, d.h. auf den ersten Blick erkennbar
gewesen sein. Eine bloße Verdachtssituation oder abstrakte Risikoerwägung reicht nicht.

### Kollusion und Betrug

Bei Kollusion zwischen Vertreter und Drittem liegt regelmäßig auch ein Betrug (§ 263 StGB) und
eine vorsätzliche sittenwidrige Schädigung (§ 826 BGB) vor. Die zivilrechtliche Unwirksamkeit
nach § 138 BGB tritt neben die strafrechtliche Verantwortlichkeit.

### Klausur-Checkliste Missbrauch der Vertretungsmacht

- Formelle Vollmacht des Vertreters im Außenverhältnis besteht?
- Überschreitung des Innenverhältnisses durch Vertreter festgestellt?
- Kollusion: Gemeinsames Handeln von Vertreter und Drittem zum Nachteil des Vertretenen?
- Evidenz: War Missbrauch für Dritten auf den ersten Blick erkennbar?
- Rechtsfolge: § 138 BGB (Kollusion) oder § 242 BGB (Evidenz ohne Kollusion)?
