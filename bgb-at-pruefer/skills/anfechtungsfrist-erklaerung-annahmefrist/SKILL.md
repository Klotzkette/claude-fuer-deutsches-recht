---
name: anfechtungsfrist-erklaerung-annahmefrist
description: "Anfechtungsfrist Erklaerung Annahmefrist: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anfechtungsfrist Erklaerung Annahmefrist

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anfechtungsfrist Erklaerung Annahmefrist** im Plugin Bgb At Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anfechtungsfrist-erklaerung-bestaetigung` | Prüft Anfechtungsfrist und Bestätigungstatbestand: Frist bei Irrtumsanfechtung nach § 121 BGB (unverzüglich) und bei arglistiger Täuschung nach § 124 BGB (ein Jahr), Fristbeginn, Bestätigung nach § 144 BGB als Ausschlussgrund. |
| `annahmefrist-verspaetung-paragraphen-147-149` | Klausurfall zur Annahmefrist nach §§ 147 bis 149 BGB: Annahme unter Anwesenden sofort, unter Abwesenden in angemessener Frist, verspätete Annahme als neues Angebot und Rechtsfolgen des Verspätungsanzeigeverzichts nach § 149 BGB. |
| `bedingung-befristung-paragraphen-158-163` | Klausurfall zu Bedingung und Befristung nach §§ 158 bis 163 BGB: aufschiebende und auflösende Bedingung, Zeitbestimmung, Vereitelung des Bedingungseintritts nach § 162 BGB, Rückwirkung nach § 159 BGB und Zwischenverfügungen. |

## Arbeitsweg

Im Plugin Bgb At Pruefer gilt für **Anfechtungsfrist Erklaerung Annahmefrist**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anfechtungsfrist-erklaerung-bestaetigung`

**Fokus:** Prüft Anfechtungsfrist und Bestätigungstatbestand: Frist bei Irrtumsanfechtung nach § 121 BGB (unverzüglich) und bei arglistiger Täuschung nach § 124 BGB (ein Jahr), Fristbeginn, Bestätigung nach § 144 BGB als Ausschlussgrund.

# Anfechtungsfrist, Anfechtungserklärung und Bestätigung — §§ 121 bis 124 und § 144 BGB

## Mandantenfall

- Mandant bemerkt Irrtum beim Kauf drei Wochen nach Vertragsschluss und fragt, ob Anfechtung noch möglich ist.
- Käufer hat Täuschung entdeckt, aber mehrere Monate gewartet — ist die Jahresfrist des § 124 BGB noch offen?
- Klausurkonstellation: Erklärungsempfänger behauptet, Anfechtender habe den Vertrag durch späteres Handeln bestätigt.

## Erste Schritte

1. Anfechtungsgrund festlegen — bestimmt die anwendbare Frist.
2. Bei §§ 119 und 120 BGB: § 121 BGB — unverzüglich nach Kenntnis des Anfechtungsgrunds.
3. Bei § 123 BGB: § 124 BGB — ein Jahr ab Entdeckung der Täuschung oder Aufhören der Drohung.
4. Absolute Ausschlussfrist bei § 124 BGB: 10 Jahre ab Abgabe der Willenserklärung.
5. Anfechtungserklärung: Inhalt und Form; eindeutige Anfechtungsabsicht erforderlich, aber kein Formzwang.
6. Bestätigung nach § 144 BGB: Erklärung oder schlüssiges Verhalten nach Kenntnis des Anfechtungsgrunds.

## Rechtsrahmen

- § 121 BGB: Unverzügliche Anfechtung bei Irrtum — ohne schuldhaftes Zögern nach Kenntnis.
- § 124 BGB: Jahresfrist bei arglistiger Täuschung oder Drohung; absolute Höchstfrist 10 Jahre.
- § 144 BGB: Bestätigung des anfechtbaren Rechtsgeschäfts schließt Anfechtung aus.
- § 119 BGB: Irrtumsanfechtungsgrundlage für § 121 BGB-Frist.
- § 123 BGB: Anfechtungsgrundlage für § 124 BGB-Frist.
- § 130 BGB: Zugang der Anfechtungserklärung als Zeitpunkt für Fristwahrung.

## Prüfraster

1. Anfechtungsgrund bestimmt anwendbare Fristnorm (§ 121 oder § 124 BGB).
2. Fristbeginn: Wann hat der Anfechtende Kenntnis vom Anfechtungsgrund erlangt?
3. Unverzüglichkeit bei § 121 BGB: Zeitspanne und etwaige Gründe für Verzögerung?
4. Jahresfrist bei § 124 BGB: Fristbeginn und Ablaufdatum konkret berechnen.
5. Absolute Ausschlussfrist 10 Jahre bei § 124 Abs. 3 BGB einhalten?
6. Bestätigung nach § 144 BGB: Ausdrücklich oder durch schlüssiges Handeln nach Kenntnis?
7. Zugang der Anfechtungserklärung beim Anfechtungsgegner rechtzeitig?

## Typische Fallstricke

- Unverzüglichkeit nach § 121 BGB ist kein starres Zeitfenster — beurteilungsabhängig, aber eine Woche gilt meist als Richtwert.
- Bei § 123 BGB gilt als Fristbeginn der Zeitpunkt der Entdeckung, nicht der Vertragsschluss.
- Bestätigung nach § 144 BGB setzt Kenntnis des Anfechtungsgrunds voraus — unbewusstes Weiterhandeln genügt nicht.
- Die 10-Jahres-Frist des § 124 Abs. 3 BGB ist eine absolute Ausschlussfrist, keine Verjährungsfrist.

## Output

- Fristberechnungsschema: Fristbeginn, -lauf und -ende konkret mit Datum
- Gutachtenstil-Prüfung der Anfechtungserklärung und Rechtzeitigkeit
- Analyse Bestätigung § 144 BGB: Liegt wirksame Bestätigung vor?
- Rückfragenliste zu Kenntniszeitpunkt und späteren Handlungen

## Quellen

- [§ 121 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__121.html)
- [§ 124 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__124.html)
- [§ 144 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__144.html)
- [dejure.org § 121 BGB](https://dejure.org/gesetze/BGB/121.html)
- [dejure.org § 124 BGB](https://dejure.org/gesetze/BGB/124.html)

## Vertiefung

### Fristberechnung im Detail

§ 121 BGB (unverzüglich nach Kenntnis): Grundsätzlich gilt eine kurze Zeitspanne von einigen Tagen.
Bei anwaltlicher Vertretung kann die Frist etwas länger sein, da Rücksprache erforderlich ist. Eine
Woche gilt als Anhaltswert, mehr als zwei Wochen sind regelmäßig zu lang.

§ 124 BGB (bei §§ 123 und 124 BGB): Ein Jahr ab Entdeckung der Täuschung oder Ende der Zwangslage.
Absolute Ausschlussfrist zehn Jahre ab Abgabe der Willenserklärung.

### Bestätigung nach § 144 BGB

Mit der Bestätigung nach § 144 BGB verzichtet der Anfechtungsberechtigte auf sein Anfechtungsrecht.
Die Bestätigung muss in Kenntnis des Anfechtungsgrunds erfolgen. Sie kann ausdrücklich oder durch
schlüssiges Verhalten (z.B. Erfüllung der Verbindlichkeit) erklärt werden.

### Klausur-Checkliste Anfechtungsfrist

- Fristtyp bestimmen: § 121 BGB (unverzüglich) oder § 124 BGB (ein Jahr)?
- Fristbeginn: Kenntnis des Anfechtungsgrunds festgestellt?
- Absolute Frist nach § 121 Abs. 2 BGB oder § 124 Abs. 3 BGB beachtet?
- Bestätigung nach § 144 BGB: Kenntnis des Anfechtungsgrunds bei Bestätigung vorhanden?

## 2. `annahmefrist-verspaetung-paragraphen-147-149`

**Fokus:** Klausurfall zur Annahmefrist nach §§ 147 bis 149 BGB: Annahme unter Anwesenden sofort, unter Abwesenden in angemessener Frist, verspätete Annahme als neues Angebot und Rechtsfolgen des Verspätungsanzeigeverzichts nach § 149 BGB.

# Annahmefrist und verspätete Annahme — §§ 147 bis 149 BGB

## Mandantenfall

- Mandant erhält ein schriftliches Angebot und antwortet nach drei Wochen — ist der Vertrag zustande gekommen?
- Käufer nimmt Angebot rechtzeitig an, Annahmeerklärung geht aber wegen Poststreiks verspätet ein.
- Klausurkonstellation: Antragende Seite zeigt Verspätung nicht unverzüglich an — welche Rechtsfolgen nach § 149 BGB?

## Erste Schritte

1. Art der Kommunikation bestimmen: unter Anwesenden (§ 147 Abs. 1 BGB) oder unter Abwesenden (§ 147 Abs. 2 BGB).
2. Bei unter Anwesenden: Annahme sofort oder unverzüglich erforderlich.
3. Bei unter Abwesenden: angemessene Frist berechnen — Übermittlung, Überlegung, Rückantwort.
4. Verspätete Annahme: gilt nach § 150 Abs. 1 BGB als neues Angebot.
5. § 149 BGB prüfen: Erkennbar rechtzeitig abgesandte Annahme verspätet eingegangen — Pflicht zur unverzüglichen Anzeige.
6. Rechtsfolge des § 149 S. 2 BGB: Unterlassene Anzeige lässt Vertrag als zustande gekommen gelten.

## Rechtsrahmen

- § 147 Abs. 1 BGB: Annahme unter Anwesenden sofort.
- § 147 Abs. 2 BGB: Annahme unter Abwesenden innerhalb der erwartbaren Frist.
- § 148 BGB: Antragender kann Annahmefrist ausdrücklich festsetzen.
- § 149 BGB: Verspätet eingegangene Annahmeerklärung — Anzeigelast des Antragenden.
- § 150 Abs. 1 BGB: Verspätete Annahme gilt als neues Angebot.
- § 150 Abs. 2 BGB: Annahme unter Erweiterungen oder Einschränkungen gilt als Ablehnung und neues Angebot.

## Prüfraster

1. Annahmefrist: unter Anwesenden oder Abwesenden — welche Norm gilt?
2. Beginn und Ende der angemessenen Frist nach § 147 Abs. 2 BGB konkret bestimmen.
3. Ist die Annahme innerhalb der Frist zugegangen?
4. Verspätet — aber erkennbar rechtzeitig abgesandt: § 149 BGB anwendbar?
5. Hat der Antragende die Verspätung unverzüglich angezeigt?
6. Rechtsfolge: Vertrag zustande gekommen oder nicht?
7. Geänderte Annahme nach § 150 Abs. 2 BGB: Liegt ein neues Angebot vor?

## Typische Fallstricke

- Die angemessene Frist nach § 147 Abs. 2 BGB umfasst auch die Zeit für Überlegung — nicht nur Übermittlungszeiten.
- § 149 BGB schützt den Annahme-Absender; Pflicht zur Anzeige liegt beim Antragenden.
- Verspätete Annahme ohne § 149 BGB begründet kein Vertragsschluss, sondern ein neues Angebot.
- Bei ausdrücklicher Fristsetzung nach § 148 BGB gilt nur diese Frist.

## Output

- Gutachtenstil-Prüfung des Vertragsschlusses mit Fristberechnung
- Schema: Fristbeginn — Fristablauf — Zugang der Annahme — Ergebnis
- Analyse § 149 BGB mit Anzeigelast-Prüfung
- Klausurlösungsskizze: Vertrag zustande gekommen oder neues Angebot?

## Quellen

- [§ 147 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__147.html)
- [§ 148 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__148.html)
- [§ 149 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__149.html)
- [§ 150 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__150.html)
- [dejure.org § 149 BGB](https://dejure.org/gesetze/BGB/149.html)

## Vertiefung

### Berechnung der Annahmefrist

Die angemessene Frist nach § 147 Abs. 2 BGB umfasst: (1) Bearbeitungszeit für das Angebot,
(2) Übermittlungszeit, (3) Überlegungszeit und (4) Übermittlungszeit der Annahme zurück.
Bei schriftlichem Angebot entspricht dies regelmäßig zwei bis drei Wochen per Post.

### Wirkung der verspäteten Annahme

Nach § 149 BGB gilt die verspätete Annahme als neues Angebot an den ursprünglichen Antragenden.
Dieser kann die verspätete Annahme sofort annehmen oder stillschweigend ablehnen. Nimmt er nicht
unverzüglich an, kommt kein Vertrag zustande. Dies wird in Klausuren oft falsch bewertet.

### Klausur-Checkliste Annahmefrist

- Annahmefrist ausdrücklich vereinbart oder nach § 147 Abs. 2 BGB zu bestimmen?
- Annahme innerhalb der Frist zugegangen — Zeitpunkt dokumentiert?
- Verspätete Annahme nach § 149 BGB als neues Angebot gewertet?
- Ablehnung: unverzüglich durch den Antragenden erklärt oder konkludent?
- Abgeänderte Annahme nach § 150 Abs. 2 BGB als weiteres Angebot?

## 3. `bedingung-befristung-paragraphen-158-163`

**Fokus:** Klausurfall zu Bedingung und Befristung nach §§ 158 bis 163 BGB: aufschiebende und auflösende Bedingung, Zeitbestimmung, Vereitelung des Bedingungseintritts nach § 162 BGB, Rückwirkung nach § 159 BGB und Zwischenverfügungen.

# Bedingung und Befristung — §§ 158 bis 163 BGB

## Mandantenfall

- Mandant schließt Kaufvertrag unter der Bedingung, dass er seinen alten Wagen verkauft — Wirkung bei Eintritt oder Ausbleiben der Bedingung?
- Vertragspartei vereitelt arglistig den Bedingungseintritt — § 162 BGB Rechtsfolge?
- Klausurkonstellation: Vertrag mit Befristung (Zeitbestimmung) — wann tritt Wirkung ein, wann erlischt sie?

## Erste Schritte

1. Bedingung oder Befristung bestimmen: aufschiebende (§ 158 Abs. 1 BGB) oder auflösende Bedingung (§ 158 Abs. 2 BGB)?
2. Zeitbestimmung nach §§ 163 und 158 BGB abgrenzen: sicheres vs. ungewisses Ereignis.
3. Wirkung bei Bedingungseintritt: Rechtsfolge tritt ex nunc ein (Grundsatz).
4. Rückwirkung nach § 159 BGB: nur wenn Parteien dies vereinbart haben.
5. Vereitelung nach § 162 BGB: Partei hat treuwidrig den Eintritt verhindert oder herbeigeführt.
6. Zwischenverfügungen: § 161 BGB schützt Erwerber vor Verfügungen in der Schwebezeit.

## Rechtsrahmen

- § 158 Abs. 1 BGB: Aufschiebende Bedingung — Wirkung erst bei Eintritt der Bedingung.
- § 158 Abs. 2 BGB: Auflösende Bedingung — Wirkung endet bei Eintritt.
- § 159 BGB: Rückwirkung bei vereinbarter Rückbeziehung.
- § 160 BGB: Schadensersatz bei Vereitelung in der Schwebezeit.
- § 161 BGB: Schutz des Erwerbers vor Zwischenverfügungen.
- § 162 BGB: Unredliche Herbeiführung oder Vereitelung des Bedingungseintritts.

## Prüfraster

1. Art der Bedingung: aufschiebend oder auflösend?
2. Ist das Ereignis ungewiss (Bedingung) oder sicher (Befristung)?
3. Ist die Bedingung erlaubt — keine Wollensbedingung, keine rechtswidrige Bedingung?
4. Schwebezeit: Welche Rechte bestehen bereits, welche sind noch ausgesetzt?
5. § 162 BGB: Hat eine Partei treuwidrig auf den Bedingungseintritt eingewirkt?
6. Zwischenverfügungen nach § 161 BGB: Ist ein Dritter durch Verfügung in der Schwebezeit betroffen?
7. Rechtsfolge bei Eintritt oder Ausbleiben der Bedingung?

## Typische Fallstricke

- Wollensbedingung ist keine echte Bedingung nach §§ 158 ff. BGB, sondern Auslegungsproblem.
- § 162 BGB setzt Treuwidrigkeit voraus — bloße Passivität genügt nicht als Vereitelung.
- Rückwirkung nach § 159 BGB ist keine gesetzliche Regel, sondern muss vereinbart werden.
- Zwischenverfügungen: § 161 BGB greift nur bei schuldrechtlicher Übereignungspflicht.

## Output

- Gutachtenstil-Abschnitt: Bedingungsart, Schwebezeit, Eintrittsfolge
- § 162 BGB-Analyse: Treuwidrigkeit und Fiktion des Bedingungseintritts
- Zwischenverfügungs-Schema nach § 161 BGB
- Klausurlösungsskizze mit Ergebnis

## Quellen

- [§ 158 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__158.html)
- [§ 162 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__162.html)
- [§ 161 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__161.html)
- [dejure.org § 158 BGB](https://dejure.org/gesetze/BGB/158.html)
- [dejure.org § 162 BGB](https://dejure.org/gesetze/BGB/162.html)

## Vertiefung

### Bedingungs- und Befristungsarten

Aufschiebende Bedingung (§ 158 Abs. 1 BGB): Rechtswirkung tritt erst mit Bedingungseintritt ein.
Auflösende Bedingung (§ 158 Abs. 2 BGB): Rechtswirkung endet mit Bedingungseintritt.
Anfangstermin (§ 163 BGB): Rechtswirkung beginnt zu einem bestimmten Zeitpunkt.
Endtermin (§ 163 BGB): Rechtswirkung endet zu einem bestimmten Zeitpunkt.

### Treuwidrige Bedingungsvereitelung

§ 162 BGB schützt beide Parteien: Wenn die Bedingung treuwidrig vereitelt wird, gilt sie als
eingetreten. Wenn sie treuwidrig herbeigeführt wird, gilt sie als nicht eingetreten. Dies ist
klausurrelevant bei Potestativbedingungen.

### Klausur-Checkliste Bedingung und Befristung

- Bedingung oder Befristung im Rechtsgeschäft ausdrücklich oder konkludent vereinbart?
- Aufschiebend oder auflösend — Wirkungsrichtung bestimmt?
- Bedingungseintritt: Tatsächlich eingetreten oder vereitelt?
- § 162 BGB: Treuwidrige Vereitelung oder Herbeiführung der Bedingung?
- Schwebezustand: Wirkung auf vorläufige Rechte und Pflichten der Parteien?
