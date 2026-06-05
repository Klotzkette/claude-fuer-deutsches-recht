---
name: genehmigungspflicht-jahresbericht
description: "Genehmigungspflicht Jahresbericht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Genehmigungspflicht Jahresbericht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Genehmigungspflicht Jahresbericht** im Plugin Betreuungsrecht (§§ 1814 ff. BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `genehmigungspflicht-pruefung` | Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB) — etwa Grundstücksverkauf, Erbausschlagung, Heimvertragsabschluss, Wohnungsauflösung, freiheitsentziehende Maßnahmen. Lädt, wenn Schlagwörter wie "Genehmigung Betreuungsgericht", "§ 1848 BGB", "§ 1850 BGB", "§ 1851 BGB", "freiheitsentziehende Maßnahme" oder "Heimvertrag" auftreten. |
| `jahresbericht-betreuungsgericht` | Jahresbericht und Anfangs-/Schlussbericht für das Betreuungsgericht nach § 1863 BGB erstellen: persönliche Kontakte, Wünsche der betreuten Person, Ziele, Maßnahmen, Gründe für Fortbestand oder Änderung der Betreuung, Vermögens-Eckdaten und Anlagen. Für Berufsbetreuer ebenso wie ehrenamtliche Familienbetreuer; trennt Bericht, Vermögensverzeichnis (§ 1835 BGB) und Rechnungslegung/Vermögensübersicht. |
| `schutzplan-betreute-person-risikoampel` | Schutzplan für die betreute Person: prüft Risiken bei Gesundheit, Wohnen, Vermögen, Einsamkeit, Verträgen, digitalem Betrug, Angehörigenkonflikt, Pflege, Heim und Selbstgefährdung und erzeugt eine klare Risikoampel mit mildesten geeigneten Maßnahmen. |

## Arbeitsweg

Im Plugin Betreuungsrecht (§§ 1814 ff. BGB) gilt für **Genehmigungspflicht Jahresbericht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `genehmigungspflicht-pruefung`

**Fokus:** Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB) — etwa Grundstücksverkauf, Erbausschlagung, Heimvertragsabschluss, Wohnungsauflösung, freiheitsentziehende Maßnahmen. Lädt, wenn Schlagwörter wie "Genehmigung Betreuungsgericht", "§ 1848 BGB", "§ 1850 BGB", "§ 1851 BGB", "freiheitsentziehende Maßnahme" oder "Heimvertrag" auftreten.

# Genehmigungspflicht-Prüfung (§§ 1848 ff. BGB)

## Zweck

Dieser Skill prüft, ob ein konkret geplantes Rechtsgeschäft oder eine
Maßnahme des Betreuers nach dem **Vier-Augen-Prinzip** der Genehmigung
des Betreuungsgerichts bedarf. Die Reform 2023 hat das System der
Genehmigungspflichten neu strukturiert (§§ 1848–1858 BGB für Vermögens-
sorge; §§ 1828–1834 BGB für personenbezogene Maßnahmen). Ohne
erforderliche Genehmigung sind Geschäfte schwebend unwirksam (§ 1855 BGB).

## Eingaben

- **Aufgabenkreise** des Betreuers (Bestellungsurkunde)
- **Konkret geplante Maßnahme** (z. B. "Verkauf der Eigentumswohnung der
 betreuten Person in Berlin-Charlottenburg")
- **Beteiligte Personen** (Vertragspartner, Heimträger, Arzt)
- **Wirtschaftliche Eckdaten** (Kaufpreis, Heimkosten, Darlehenssumme)
- **Wünsche/Willen der betreuten Person** zum Geschäft (§ 1821 BGB)
- **Vorhandensein einer Vorsorgevollmacht** (verdrängt ggf. Betreuung)

## Rechtlicher Rahmen

### Systematik der Genehmigungspflichten nach Reform 2023

Die §§ 1848–1858 BGB regeln **vermögensbezogene** Genehmigungspflichten:

- § 1848 BGB — Grundsatz: Genehmigung des Gerichts bei wesentlichen
 Vermögensverfügungen
- § 1849 BGB — Genehmigung bei Geschäften über Grundstücke und Rechte an
 Grundstücken
- § 1850 BGB — Genehmigung bei Erbschaftsangelegenheiten (Annahme/
 Ausschlagung der Erbschaft, Erbteilsverkauf)
- § 1851 BGB — Genehmigung bei Aufgabe/Auflösung der Wohnung der
 betreuten Person
- § 1852 BGB — Genehmigung bei Geschäften über erwerbsmäßige Tätigkeit
- § 1853 BGB — Genehmigung bei Kreditaufnahme, Verfügungen über Wertpapiere
- § 1854 BGB — Genehmigung bei Schenkungen (Ausschluss anstandspflichtiger
 Schenkungen)
- § 1855 BGB — Rechtsfolge: schwebende Unwirksamkeit ohne Genehmigung

### Personenbezogene Maßnahmen (§§ 1828–1834 BGB)

- § 1828 BGB — Einwilligung in ärztliche Maßnahmen
- § 1829 BGB — Genehmigung bei lebensgefährlichen oder schwer
 beeinträchtigenden ärztlichen Maßnahmen
- § 1831 BGB — Genehmigung **freiheitsentziehender Unterbringung**
 (geschlossene Heimunterbringung, geschlossene psychiatrische Klinik)
- § 1832 BGB — Genehmigung **freiheitsentziehender Maßnahmen** in offener
 Einrichtung (Bettgitter, Bauchgurt, sedierende Medikamente zur
 Bewegungseinschränkung)

### § 1855 BGB — Schwebende Unwirksamkeit

Rechtsgeschäfte ohne erforderliche Genehmigung sind **schwebend
unwirksam**. Die Genehmigung kann auch nachträglich erteilt werden. Wird
sie versagt, ist das Geschäft endgültig unwirksam. Der Vertragspartner kann
nach § 1856 BGB widerrufen.

### Kanonische Rechtsprechung (Stand 05/2026, Live-Verifikation vor Verwendung)

- BGH, Beschluss vom 12.02.2025 - XII ZB 433/24: Bei Genehmigung oder Anordnung einer medikamentösen Zwangsbehandlung muss der Entscheidungstenor das jeweilige Medikament/den Wirkstoff, die (Höchst-)Dosierung sowie die Verabreichungshäufigkeit hinreichend genau bezeichnen (§ 323 Abs. 1 Nr. 1 FamFG). Quelle: bundesgerichtshof.de / dejure.org.
- BGH, Beschluss vom 24.09.2025 - XII ZB 513/24: Wunsch des/der Betroffenen, durch nahe Angehörige betreut zu werden, hat Vorrang vor Berufsbetreuer; Amtsermittlungspflicht § 26 FamFG.
- Etablierte Linien (zu verifizieren): Bei freiheitsentziehender Unterbringung (§ 1831 BGB n.F.) enge Voraussetzungen — erhebliche Selbstgefährdung, medizinische Indikation, Verhältnismäßigkeit, kein milderes Mittel. SV-Gutachten regelmäßig erforderlich (§ 321 FamFG).
- Bei freiheitsentziehenden Maßnahmen in offener Einrichtung (§ 1832 BGB, vormals § 1906 Abs. 4 BGB a.F.): Bettgitter und Bauchgurt sind genehmigungspflichtig, wenn regelmäßig oder über längeren Zeitraum eingesetzt.
- Grundstücksverkauf (§ 1849 BGB): Verkehrswertnachweis durch qualifiziertes Gutachten/Maklerwertindikation; auffallend niedriger Kaufpreis löst Prüfungspflicht aus.
- Erbausschlagung (§ 1850 BGB): Gericht prüft wirtschaftliches Interesse der betreuten Person (Überschuldung, dingliche Lasten).

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, dejure.org oder openjur.de verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Aufgabenkreis prüfen**
 Liegt die geplante Maßnahme überhaupt im übertragenen Aufgabenkreis?
 (Vermögenssorge / Gesundheitssorge / Aufenthaltsbestimmung — § 1815 BGB).
 Fehlt der Aufgabenkreis, ist Erweiterung beim Gericht zu beantragen.

2. **Tatbestand der Genehmigungspflicht prüfen**
 Subsumtion unter konkreten §§ 1848 ff. BGB bzw. §§ 1831, 1832 BGB.

3. **Wunsch der betreuten Person ermitteln (§ 1821 BGB)**
 Auch bei genehmigungspflichtigen Geschäften ist der Wille der betreuten
 Person primärer Maßstab.

4. **Antrag beim Betreuungsgericht stellen**
 Schriftlich oder zur Niederschrift der Geschäftsstelle. Beizufügen:
 - Begründung der Maßnahme
 - Wirtschaftliche Eckdaten (Verkehrswertgutachten, Kostenvoranschlag)
 - Stellungnahme zum Willen der betreuten Person
 - Bei medizinischen Maßnahmen: ärztliches Zeugnis / Gutachten

5. **Anhörung durch das Gericht abwarten**
 Persönliche Anhörung der betreuten Person grundsätzlich Pflicht
 (§ 278 FamFG); bei Unterbringung Sachverständigengutachten
 zwingend (§ 321 FamFG).

6. **Genehmigungsbeschluss umsetzen**
 Geschäft erst nach Rechtskraft des Beschlusses vollziehen. Bei
 Grundstücken: Beschluss als Anlage zum Notarvertrag.

## Ausgabeformat

Strukturierte Prüfung in folgender Form:

```
Genehmigungspflicht-Prüfung
Geplante Maßnahme: [konkret]
Geprüft am: [Datum]
Betreute Person: [Name, AZ]
Aufgabenkreise: [Aufzählung]

1. Aufgabenkreis-Zuordnung
 [Ja/Nein, Begründung]

2. Einschlägige Rechtsnorm
 [§ XXXX BGB — Tatbestand]

3. Subsumtion
 [Tatbestandsmerkmal 1 — erfüllt/nicht erfüllt — Begründung]
 [Tatbestandsmerkmal 2 — ...]

4. Wunsch und Wille der betreuten Person (§ 1821 BGB)
 [Ermittelt durch ..., Inhalt: ...]

5. Ergebnis
 [ ] genehmigungspflichtig — Antrag beim Betreuungsgericht erforderlich
 [ ] nicht genehmigungspflichtig — Begründung
 [ ] Aufgabenkreis-Erweiterung erforderlich

6. Empfohlene Anlagen für Genehmigungsantrag
 [Liste]

7. Belege
 [BGH-Entscheidungen, Kommentarstellen]
```

## Beispiel

**Sachverhalt:** Frau Hannelore K. (Heimbewohnerin, siehe Schwester-Skill)
wird zunehmend nachts unruhig, verlässt regelmäßig ihr Zimmer und gefährdet
sich durch Stürze. Die Pflegeheimleitung schlägt vor, nachts Bettgitter
anzubringen sowie ein leichtes Sedativum (Pipamperon 20 mg) zu verabreichen.

**Prüfung:**

> *2. Einschlägige Rechtsnorm:* § 1832 BGB — Genehmigung bei
> freiheitsentziehenden Maßnahmen in offener Einrichtung
>
> *3. Subsumtion:*
> - Maßnahme: Bettgitter + sedierende Medikation
> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
> Rn. 27 ff. — auch in offener Einrichtung)
> - Sedativum: Wenn primär zur Bewegungseinschränkung verabreicht
> (nicht therapeutisch), ebenfalls § 1832 BGB
> - Regelmäßigkeit: jede Nacht — Tatbestand erfüllt
>
> *4. Wille der betreuten Person:* Frau K. wurde am 18.02.2026 befragt
> (Aktenvermerk). Sie äußerte: "Ich will nicht eingesperrt sein, aber
> hinfallen will ich auch nicht." Bei eingeschränkter Einsichtsfähigkeit
> ist mutmaßlicher Wille zu erschließen — Schutz vor Sturzschäden hat
> Priorität.
>
> *5. Ergebnis:* genehmigungspflichtig. Antrag beim Betreuungsgericht
> Berlin-Spandau, AZ XVII 0234/24.
>
> *6. Anlagen:*
> - Ärztliches Zeugnis Dr. Petersen v. 02.03.2026 (Sturzgefahr)
> - Stellungnahme Pflegeheimleitung Sonnenhof
> - Aktenvermerk Anhörung Frau K. v. 18.02.2026
> - Prüfung milderer Mittel (Niedrigflurbett, Sturzmatte) — Stellungnahme

## Risiken und typische Fehler

**1. Genehmigung vor Vollzug einholen**
Geschäft erst nach Rechtskraft des Genehmigungsbeschlusses abschließen.
Vorzeitige Vollziehung führt zur schwebenden Unwirksamkeit (§ 1855 BGB).

**2. "Bettgitter sind keine Freiheitsentziehung"**
Verbreiteter Irrtum: Auch in offenen Einrichtungen sind Bettgitter und
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
24/12 Rn. 27 ff.). Einmalige kurzzeitige Maßnahme bei akuter Eigen-
gefährdung kann ohne Genehmigung erlaubt sein (Notstand).

**3. Heimvertrag**
Der Abschluss eines Heimvertrags durch den Betreuer ist regelmäßig **nicht**
nach § 1851 BGB genehmigungspflichtig, sondern Verwaltungsmaßnahme. Die
**Auflösung der bisherigen Wohnung** ist dagegen genehmigungspflichtig
(§ 1851 BGB), sofern Lebensmittelpunkt aufgegeben wird.

**4. Schenkung an Familie**
Schenkungen sind nach § 1854 BGB grundsätzlich genehmigungspflichtig.
Ausnahme: anstandsbedingte Gelegenheitsgeschenke (Geburtstag, Weihnachten)
in angemessenem Umfang.

**5. Erbausschlagung Frist**
Erbausschlagung ist binnen 6 Wochen nach Kenntnis vom Erbfall zu erklären
(§ 1944 BGB). Bei Genehmigungsbedürftigkeit (§ 1850 BGB) muss der Antrag
**innerhalb der Sechswochenfrist** beim Gericht eingehen; eine Hemmung
greift bei vorzeitiger Antragstellung.

**6. Verkehrswert nicht belegt**
Beim Grundstücksverkauf ist Verkehrswertgutachten oder Maklerwert-
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Behauptungen genügen nicht.

**7. Vorsorgevollmacht verdrängt Betreuung**
Vor Antragstellung prüfen, ob eine wirksame Vorsorgevollmacht besteht
(§ 1820 BGB). Der Bevollmächtigte ist vorrangig zu beteiligen; Betreuung
ist subsidiär.

## Quellenpflicht

Bei jeder Ausgabe sind mindestens folgende Belege anzugeben:

- §§ 1848 ff. BGB, §§ 1831, 1832 BGB (einschlägige Rechtsnormen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; nur Nutzerquelle oder lizenzierte Live-Verifikation verwenden.

---
*Dieser Skill ersetzt keine konkrete fachliche Beratung im Einzelfall.
Vor jeder genehmigungspflichtigen Maßnahme ist der Antrag durch den
verantwortlichen Betreuer zu prüfen.*

## 2. `jahresbericht-betreuungsgericht`

**Fokus:** Jahresbericht und Anfangs-/Schlussbericht für das Betreuungsgericht nach § 1863 BGB erstellen: persönliche Kontakte, Wünsche der betreuten Person, Ziele, Maßnahmen, Gründe für Fortbestand oder Änderung der Betreuung, Vermögens-Eckdaten und Anlagen. Für Berufsbetreuer ebenso wie ehrenamtliche Familienbetreuer; trennt Bericht, Vermögensverzeichnis (§ 1835 BGB) und Rechnungslegung/Vermögensübersicht.

# Jahresbericht des Betreuers ans Betreuungsgericht (§ 1863 BGB)

## Zweck

Dieser Skill unterstützt berufliche und ehrenamtliche Betreuerinnen und
Betreuer bei der Erstellung des **Jahresberichts an das Betreuungsgericht**
nach § 1863 Abs. 3 BGB sowie des **Anfangsberichts** nach § 1863 Abs. 1 BGB.
Aus einer Sammlung unsortierter Eingangsdaten — E-Mail-Verkehr mit Heimen,
Ärzten, Kostenträgern, Aktenvermerken über Besuche und Telefonate,
Arztbriefen, Heim- und Pflegeberichten, Kontoauszügen, Behördenpost —
generiert der Skill einen vollständigen, gerichtstauglich strukturierten
Bericht mit den nach § 1863 BGB zwingend vorgeschriebenen Abschnitten.

## Eingaben

- **Stammdaten der betreuten Person:** Name, Geburtsdatum, Anschrift,
 Aufenthaltsort (eigene Wohnung, Heim, Klinik), Aktenzeichen des
 Betreuungsgerichts, Anordnungsdatum und Aufgabenkreise (§ 1815 BGB)
- **Berichtszeitraum:** Berichtsbeginn und -ende (Anfangsbericht: ab
 Bestellung; Jahresbericht: 12 Monate; Schlussbericht: Ende der Betreuung)
- **Persönliche Kontakte:** Datum, Dauer, Ort und Inhalt jedes Besuchs oder
 Telefonats (§ 1821 Abs. 5 BGB — Pflicht zum persönlichen Kontakt)
- **Wohnsituation:** Wechsel der Wohnung, Heimaufnahme, Heimwechsel,
 Klinikaufenthalte
- **Gesundheitliche Situation:** Diagnosen (aktuelle Arztbriefe), Pflegegrad,
 Behandlungen, ärztliche Maßnahmen mit Einwilligungsbedarf (§§ 1828 ff. BGB)
- **Soziale Kontakte:** Familienangehörige, Freundeskreis, Ehrenamtliche
- **Vermögensentwicklung:** Eckdaten (Anfangsbestand, Endbestand,
 wesentliche Veränderungen) — Detailausweis erfolgt in der gesonderten
 Rechnungslegung (§ 1865 BGB)
- **Wünsche und Präferenzen der betreuten Person** (§ 1821 Abs. 2, 3 BGB —
 Vorrang der Wünsche)
- **Bestehender Anfangs- oder Vorjahresbericht** (zur Fortschreibung)

## Rechtlicher Rahmen

### § 1863 BGB — Berichtspflicht des Betreuers

**Abs. 1 — Anfangsbericht:** Der Betreuer hat unverzüglich nach Bestellung,
spätestens binnen drei Monaten, dem Betreuungsgericht über die persönlichen
Verhältnisse der betreuten Person, die zu erledigenden Aufgaben und die
geplante Ausgestaltung der Betreuung zu berichten.

**Abs. 2 — Inhalt des Anfangsberichts:**
1. die persönlichen Verhältnisse der betreuten Person,
2. die Wünsche der betreuten Person und die geplanten Maßnahmen zu ihrer
 Verwirklichung,
3. ggf. Gründe, weshalb Wünschen nicht entsprochen werden kann,
4. die geplante Ausgestaltung der persönlichen Betreuung, insbesondere die
 Häufigkeit persönlicher Kontakte.

**Abs. 3 — Jahresbericht:** Mindestens einmal jährlich hat der Betreuer dem
Betreuungsgericht über die persönlichen Verhältnisse der betreuten Person
sowie über die Ausführung der Betreuung zu berichten. Der Jahresbericht
enthält insbesondere:

1. eine Darstellung der persönlichen Verhältnisse der betreuten Person,
2. den Umfang und Inhalt der persönlichen Kontakte,
3. die Wünsche der betreuten Person und ihre Verwirklichung,
4. Mitteilung, ob Anlass besteht, die Betreuung aufzuheben oder den
 Aufgabenkreis (§ 1815 BGB) zu erweitern oder einzuschränken.

**Abs. 4 — Schlussbericht:** Bei Beendigung der Betreuung hat der Betreuer
einen Schlussbericht zu erstatten.

### § 1821 BGB — Pflichten des Betreuers; Wünsche der betreuten Person

Die Wünsche der betreuten Person sind **Maßstab** der Betreuung (§ 1821
Abs. 2 BGB). Der Betreuer darf nur dann von Wünschen abweichen, wenn die
betreute Person aufgrund ihrer Erkrankung oder Behinderung ihren Willen
nicht frei bilden kann **und** die Verwirklichung des Wunsches die Person
erheblich gefährden würde (§ 1821 Abs. 3 BGB).

§ 1821 Abs. 5 BGB statuiert die **Pflicht zum persönlichen Kontakt** —
der Betreuer hat die erforderlichen Angelegenheiten persönlich mit der
betreuten Person zu besprechen. Häufigkeit und Form sind im
Anfangs- und Jahresbericht darzustellen.

### § 1815 BGB — Aufgabenkreise

Aufgabenkreise sind nicht pauschal ("alle Angelegenheiten"), sondern
einzeln zu bestimmen. Übliche Aufgabenkreise:

- Vermögenssorge
- Gesundheitssorge
- Aufenthaltsbestimmung
- Wohnungsangelegenheiten
- Behörden- und Sozialleistungsangelegenheiten
- Vertretung gegenüber Heim/Pflegeeinrichtung
- Postangelegenheiten (§ 1815 Abs. 2 Nr. 3 BGB — gesonderter Beschluss)

### § 9 BtOG — Berufliche Betreuung

Berufsbetreuer benötigen Registrierung nach § 23 BtOG und Sachkundenachweis
nach § 24 BtOG. Die Berichtspflichten gelten unverändert; für Berufsbetreuer
gilt zusätzlich der Vergütungsanspruch nach § 7 VBVG (pauschalierte
Stundensätze nach Vergütungstabelle).

### Berichtsqualität

Der Bericht ist Grundlage der gerichtlichen Aufsicht (§ 1862 BGB). Er soll so
konkret sein, dass das Gericht erkennen kann, ob die Betreuung ordnungsgemäß
geführt wird, ob die Aufgabenkreise noch passen und ob die Wünsche der
betreuten Person beachtet werden. Pauschale Sätze wie "keine Besonderheiten"
oder "es geht gut" genügen nicht.

Für persönliche Kontakte gilt: Datum, Ort, Dauer, Beteiligte, eigener Eindruck
und besprochene Wünsche festhalten. Telefonate und Videogespräche können
ergänzen; bei Konflikt, Pflegeheim, Gesundheitsrisiko oder Vermögensrisiko
braucht der Bericht erkennbar einen belastbaren eigenen Eindruck.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Eingabesichtung und Kategorisierung**
 Der Skill sichtet alle eingegebenen Dokumente (E-Mails, Aktenvermerke,
 Arztbriefe, Heimberichte, Kontoauszüge, Behördenpost) und ordnet sie
 einem der vier Pflichtabschnitte des § 1863 Abs. 3 BGB zu: persönliche
 Verhältnisse, persönliche Kontakte, Wünsche, Anlass zur Änderung.

2. **Persönliche Verhältnisse darstellen**
 - Wohnsituation (eigene Wohnung / Heim — mit Namen der Einrichtung,
 Aufnahmedatum, Pflegegrad)
 - Gesundheitlicher Zustand (aktuelle Diagnosen, Veränderungen im
 Berichtszeitraum, Klinikaufenthalte)
 - Soziales Umfeld (Angehörige, Freundeskreis, ehrenamtliche Helfer)
 - Wirtschaftliche Verhältnisse in Eckdaten (Anfangs-/Endvermögen,
 Sozialleistungsbezug)
 - Berufliche oder ehrenamtliche Tätigkeit, Beschäftigung

3. **Persönliche Kontakte tabellarisch belegen**
 Pro Kontakt: Datum, Dauer, Ort, kurze Inhaltsangabe, eigener Eindruck,
 Wunschbezug und offene Folgeaufgabe. Bei Heimbewohnern Kontakte nicht nur
 aus Heimberichten ableiten.

4. **Wünsche und ihre Verwirklichung**
 - Wünsche der betreuten Person (geäußert oder erschlossen aus früheren
 Willensbekundungen, Patientenverfügung, Vorsorgevollmacht)
 - Maßnahmen des Betreuers zur Verwirklichung
 - Bei Abweichung: Begründung (§ 1821 Abs. 3 BGB — erhebliche
 Gefährdung)

5. **Anlass zur Änderung der Betreuung prüfen**
 - Sind alle Aufgabenkreise weiter erforderlich? (Verhältnismäßigkeit,
 § 1814 Abs. 3 BGB)
 - Sind weitere Aufgabenkreise erforderlich geworden?
 - Lässt sich die Betreuung aufheben (z. B. wegen Vorsorgevollmacht
 oder Genesung)?

6. **Vermögensentwicklung — Eckdaten**
 Bei Vermögenssorge: kurze Eckdaten (Anfangsbestand, Endbestand, große
 Veränderungen). Die detaillierte **Rechnungslegung** erfolgt gesondert
 nach § 1865 BGB (vereinfachte Rechnungslegung für Familienangehörige
 nach § 1859 BGB ggf. möglich).

7. **Anlagen zusammenstellen**
 Aktuelle Arztbriefe (sofern für Bericht relevant), Heim-/Pflegebericht
 (sofern vorhanden), gegebenenfalls Patientenverfügung, Vorsorgevollmacht,
 Schreiben mit Wunschäußerungen der betreuten Person.

## Ausgabeformat

Strukturierter Berichtstext mit folgenden Abschnitten (entsprechend
§ 1863 Abs. 3 BGB):

```
An das Amtsgericht – Betreuungsgericht – [Ort]
Aktenzeichen: [XVII … / …]

Jahresbericht des Betreuers nach § 1863 Abs. 3 BGB
Berichtszeitraum: [TT.MM.JJJJ – TT.MM.JJJJ]

Betreute Person: [Name, Vorname]
Geboren: [TT.MM.JJJJ]
Anschrift: [Aktueller Aufenthaltsort, Einrichtung]
Bestellung: [TT.MM.JJJJ]
Aufgabenkreise: [Aufzählung gem. § 1815 BGB]

1. Persönliche Verhältnisse der betreuten Person
 1.1 Wohnsituation
 1.2 Gesundheitlicher Zustand
 1.3 Soziales Umfeld
 1.4 Wirtschaftliche Verhältnisse (Eckdaten)

2. Persönliche Kontakte im Berichtszeitraum
 Tabellarische Aufstellung: Datum | Ort | Dauer | Inhalt
 Gesamtfrequenz: [n Besuche, n Telefonate]

3. Wünsche der betreuten Person und ihre Verwirklichung
 3.1 Geäußerte oder erschlossene Wünsche
 3.2 Umgesetzte Maßnahmen
 3.3 Ggf. Abweichungen und deren Begründung (§ 1821 Abs. 3 BGB)

4. Anlass zur Änderung der Betreuung
 [Aufhebung / Erweiterung / Einschränkung / kein Anlass]

5. Vermögensentwicklung (Eckdaten)
 Anfangsbestand: [Datum, Betrag]
 Endbestand: [Datum, Betrag]
 Wesentliche Veränderungen:
 Gesonderte Rechnungslegung nach § 1865 BGB: beigefügt / folgt am …

6. Anlagen
 [Liste]

Ort, Datum [Name, Unterschrift Betreuer/in]
 Betreuer/in
 ggf. Registrierungs-Nr. bei Berufsbetreuung
```

## Beispiel

**Eingabe (Auszug, pseudonymisiert):**

- Betreuung Frau Hannelore K., geb. 14.03.1942, AZ XVII 0234/24
- Aufgabenkreise: Vermögenssorge, Gesundheitssorge, Aufenthaltsbestimmung,
 Vertretung gegenüber Heim, Postangelegenheiten
- Berichtszeitraum: 01.06.2025 – 31.05.2026
- E-Mails: 12 mit Heimleitung Sonnenhof Berlin-Spandau, 4 mit Hausarzt
 Dr. Petersen, 8 mit Rentenversicherung
- Aktenvermerke: 6 Besuche im Heim (jeweils ca. 60 Min), 14 Telefonate
- Arztbriefe: Kardiologie Vivantes Spandau v. 12.09.2025 (Vorhofflimmern,
 Antikoagulation eingeleitet); Allgemeinmedizin Petersen v. 02.03.2026
- Heimrechnung: Pflegegrad 4, Eigenanteil 2.341 EUR/Monat, Sozialhilfe ergänzt
- Kontoauszüge: Anfangsbestand 18342.12 EUR, Endbestand 16108.77 EUR
- Wunschäußerung Frau K. (Vermerk v. 24.11.2025): "Möchte am Heiligabend
 bei Tochter Susanne in Potsdam sein" — umgesetzt durch Abholfahrt am
 24.12.2025

**Ausgabe (Auszug Abschnitt 2):**

> *2. Persönliche Kontakte im Berichtszeitraum*
>
> Im Berichtszeitraum fanden 6 persönliche Besuche und 14 Telefonate statt.
> Die Besuche erfolgten jeweils im Pflegeheim Sonnenhof, Berlin-Spandau.
>
> | Datum | Ort | Dauer | Inhalt |
> |---|---|---|---|
> | 18.06.2025 | Sonnenhof, Spandau | 65 Min | Vorstellungsgespräch, Erfassung Wünsche |
> | 12.09.2025 | Sonnenhof, Spandau | 50 Min | Besprechung Vorhofflimmern-Diagnose, Einwilligung Antikoagulation |
> | 24.11.2025 | Sonnenhof, Spandau | 55 Min | Erörterung Weihnachtsbesuch bei Tochter |
> | 18.02.2026 | Sonnenhof, Spandau | 60 Min | Pflegegrad-Höherstufung 4, Eigenanteilsfinanzierung |
> | … | … | … | … |
>
> Persönliche Kontakte wurden mit Datum, Ort, Dauer und Inhalt dokumentiert.
> Telefonate und Videogespräche können den persönlichen Eindruck ergänzen,
> ersetzen ihn aber in konflikt- oder risikoreichen Situationen nicht.

## Risiken und typische Fehler

**1. Pauschale Formulierungen**
"Frau K. geht es gut, keine Besonderheiten" genügt nicht. Der Bericht muss
substantiiert die persönlichen Verhältnisse darstellen, damit das Gericht
Aufsicht, Erforderlichkeit und Aufgabenkreise prüfen kann.

**2. Persönliche Kontakte zu selten dokumentiert**
Jeder relevante Kontakt ist mit Datum, Ort, Dauer und Inhalt zu dokumentieren.
Bei Heimbewohnern, Krankheit, Konflikten oder Vermögensrisiken muss der Bericht
erkennen lassen, wie sich der Betreuer einen eigenen Eindruck verschafft hat.

**3. Wünsche nicht eigenständig ermittelt**
Der Bericht muss erkennen lassen, wie der Betreuer die Wünsche der
betreuten Person ermittelt hat (Gespräch, Anhörung, Patientenverfügung).
Die bloße Aussage "Die Betreute hat keine Wünsche geäußert" ist
unzureichend, wenn nicht erkennbar ist, ob der Betreuer aktiv gefragt hat
oder welche Kommunikationshilfen versucht wurden.

**4. Vermischung Bericht und Rechnungslegung**
Der Jahresbericht (§ 1863 BGB) und die Rechnungslegung (§ 1865 BGB) sind
**zwei verschiedene Dokumente**. Im Bericht genügen Vermögens-Eckdaten;
die detaillierte Rechnungslegung mit Belegen wird gesondert eingereicht.

**5. Fristen versäumt**
- Anfangsbericht: binnen 3 Monaten nach Bestellung
- Jahresbericht: jährlich, im vom Gericht festgesetzten Turnus
- Schlussbericht: unverzüglich nach Ende der Betreuung
Fristversäumnis kann zur Anhörung, im Wiederholungsfall zur Entlassung
des Betreuers nach § 1868 BGB führen.

**6. Datenschutz bei KI-Nutzung**
Berichte enthalten besondere Kategorien personenbezogener Daten (Art. 9
DSGVO: Gesundheitsdaten) sowie Sozialdaten. Vor Übergabe an externe
KI-Systeme sind Daten zu pseudonymisieren (siehe Skill
`playbook-aus-eigenen-daten` im Plugin `kanzlei-builder-hub`). Berufliche
Schweige-, Datenschutz- und Vertraulichkeitspflichten sind je nach Rolle und
Konstellation gesondert zu prüfen.

**7. Beendigungsanlass nicht geprüft**
§ 1863 Abs. 3 Nr. 4 BGB verlangt ausdrücklich die Mitteilung, ob Anlass
zur Aufhebung, Erweiterung oder Einschränkung besteht. Dieser Abschnitt
darf nie fehlen; er bewirkt die Verhältnismäßigkeitskontrolle nach
§ 1814 Abs. 3 BGB.

**8. Aufgabenkreis "Postangelegenheiten" / "Postkontrolle"**
Wegen Eingriff in Art. 10 GG nur bei gesondertem gerichtlichen Beschluss
(§ 1815 Abs. 2 Nr. 3 BGB). Im Bericht ist Notwendigkeit fortlaufend zu
begründen.

## Quellenpflicht

Bei jeder Ausgabe sind mindestens folgende Belege anzugeben:

- § 1863 BGB (Berichtspflicht) und § 1821 BGB (Wünsche, persönlicher Kontakt)
- Rechtsprechung nur nach Live-Prüfung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

---
*Dieser Skill ersetzt keine konkrete fachliche Beratung im Einzelfall.
Vor Einreichung beim Betreuungsgericht ist der Bericht durch den
verantwortlichen Betreuer eigenständig zu prüfen.*

## 3. `schutzplan-betreute-person-risikoampel`

**Fokus:** Schutzplan für die betreute Person: prüft Risiken bei Gesundheit, Wohnen, Vermögen, Einsamkeit, Verträgen, digitalem Betrug, Angehörigenkonflikt, Pflege, Heim und Selbstgefährdung und erzeugt eine klare Risikoampel mit mildesten geeigneten Maßnahmen.

# Schutzplan und Risikoampel

## Zweck

Dieser Skill schützt die betreute Person, ohne sie unnötig zu kontrollieren. Er fragt: Wo droht real Schaden, was will die Person, welches mildere Mittel reicht, und was muss dokumentiert werden?

## Risikofelder

| Feld | Beispiele | Erste Maßnahme |
| --- | --- | --- |
| Gesundheit | Medikationsfehler, Klinikentlassung, fehlende Einwilligung | Arztkontakt, Medikationsplan, Wunsch prüfen |
| Wohnen | Kündigung, Heimvertrag, Wohnungsaufgabe, Verwahrlosung | Unterlagen sichern, Genehmigungscheck |
| Vermögen | ungewöhnliche Überweisungen, Betrug, Dauerschuldverträge | Kontoanalyse, Bankrückfrage, Sperren nur verhältnismäßig |
| Soziales | Isolation, Druck durch Angehörige, Besuchskonflikte | Gesprächsvermerk, Interessenmatrix |
| Digitales | Telefonbetrug, Fernwartung, Krypto, Abos | Vertrags-/Kontodatencheck |
| Freiheit | Fixierung, Bettgitter, geschlossene Unterbringung | § 1831 BGB prüfen, Genehmigungspfad |

## Ampellogik

- **Rot:** sofortiger Schaden wahrscheinlich; heute handeln.
- **Gelb:** Risiko plausibel; Unterlagen beschaffen und binnen einer Woche entscheiden.
- **Grün:** beobachten; Routine-Reminder setzen.

## Schutzplan

```text
Schutzplan

1. Konkretes Risiko:
2. Wunsch der betreuten Person:
3. Belege:
4. Mildestes geeignetes Mittel:
5. Muss das Gericht beteiligt werden?
6. Wer erledigt was bis wann?
7. Nächster Kontrolltermin:
```

## Entscheidungsregel

Schutz ist kein Freibrief für Bevormundung. Jede Maßnahme muss am Aufgabenkreis, an § 1821 BGB, am Willen der betreuten Person und an der Erforderlichkeit gemessen werden.
