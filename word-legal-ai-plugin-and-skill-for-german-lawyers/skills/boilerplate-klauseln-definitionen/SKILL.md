---
name: boilerplate-klauseln-definitionen
description: "Boilerplate Klauseln Katalog, Definitionen Klauseln Stringent: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Boilerplate Klauseln Katalog, Definitionen Klauseln Stringent

## Arbeitsbereich

Dieser Skill bündelt **Boilerplate Klauseln Katalog, Definitionen Klauseln Stringent** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `boilerplate-klauseln-katalog` | Katalog typischer Boilerplate-Klauseln im deutschen Wirtschaftsvertrag mit Wirksamkeitsanalyse und Mustertexten. Behandelt salvatorische Klausel (BGH-kritisch nach § 139 BGB), Schriftformklausel inklusive doppelter Schriftformklausel, Gerichtsstand nach § 38 ZPO, Rechtswahl nach Rom-I-VO, Erfuellungsort, Bekanntmachung, Uebertragungsverbot. Je Klausel: Voraussetzung, AGB-Risiko, Mustertext. |
| `definitionen-klauseln-stringent` | Defined Terms in Vertraegen sauber bauen. Hierarchie und Konsistenz: einmal definieren, im gesamten Dokument einheitlich verwenden, mit Grossschreibung sichtbar machen. Trennung zwischen zentralem Definitionen-Abschnitt (alphabetisch) und Inline-Definitionen ('im Folgenden Vertrag'). Mit Beispielklauseln, Konsistenzpruefung per Suchen-Ersetzen-Logik und einem Katalog typischer Anti-Pattern wie verschachtelte Definitionen oder Definitionsdoppel. |

## Arbeitsweg

Für **Boilerplate Klauseln Katalog, Definitionen Klauseln Stringent** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `word-legal-ai-plugin-and-skill-for-german-lawyers` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `boilerplate-klauseln-katalog`

**Fokus:** Katalog typischer Boilerplate-Klauseln im deutschen Wirtschaftsvertrag mit Wirksamkeitsanalyse und Mustertexten. Behandelt salvatorische Klausel (BGH-kritisch nach § 139 BGB), Schriftformklausel inklusive doppelter Schriftformklausel, Gerichtsstand nach § 38 ZPO, Rechtswahl nach Rom-I-VO, Erfuellungsort, Bekanntmachung, Uebertragungsverbot. Je Klausel: Voraussetzung, AGB-Risiko, Mustertext.

# Boilerplate-Klauseln: Katalog mit Mustertexten

## Zweck

Boilerplate ist kein Beiwerk. Salvatorische Klausel, Schriftform, Gerichtsstand und Rechtswahl entscheiden im Streitfall ueber Wirksamkeit, Gerichtszustaendigkeit und anwendbares Recht. Dieser Skill liefert einen Katalog der Standard-Boilerplate-Klauseln mit Wirksamkeitsanalyse, AGB-Risiko und Mustertext.

Er ist kein Sammelsurium. Er ordnet, was wirklich gebraucht wird, und kennzeichnet, wo BGH-Rechtsprechung die Reichweite einschraenkt.

## Eingaben

- Vertragsart (Individualvertrag oder AGB)
- Parteien (B2B oder B2C)
- Sitz der Parteien (fuer Gerichtsstand und Rechtswahl)
- Streitwert-Erwartung (fuer Schiedsklausel-Erwaegung)

## Rechtlicher und methodischer Rahmen

- § 38 ZPO: Gerichtsstandsvereinbarung. Nur unter Kaufleuten oder mit Auslandsbezug zulaessig.
- Rom-I-VO: Verordnung (EG) Nr. 593/2008. Rechtswahl bei vertraglichen Schuldverhaeltnissen.
- § 126 BGB, § 127 BGB: Schriftform und gewillkuerte Schriftform.
- § 139 BGB: Teilnichtigkeit. Salvatorische Klausel als Modifikation der gesetzlichen Folge.
- § 305c Abs. 2 BGB, § 307 BGB: AGB-Kontrolle. Boilerplate ist AGB-pflichtig in AGB-Vertraegen.

## Ablauf / Checkliste

1. **Klauselbedarf pruefen.** Im B2C-AGB sind viele Boilerplate-Klauseln unwirksam. Pruefen Sie pro Klausel.
2. **Klauseltyp waehlen.** Individualabrede oder AGB.
3. **Mustertext anpassen.** Pauschalmuster sind Ausgangspunkt, kein Endpunkt.
4. **AGB-Risiko bewerten.** Ist die Klausel im B2B noch wirksam? Im B2C oft nicht.
5. **Konsistenz mit dem Rest des Vertrages.** Gerichtsstand muss zur Rechtswahl passen.

### Klausel 1: Salvatorische Klausel (§ 139 BGB)

**Voraussetzung:** Modifikation des § 139 BGB (Gesamtnichtigkeit als Default). Praxisrelevant in nahezu jedem Vertrag.

**AGB-Risiko:** Im B2B nach BGH grundsaetzlich wirksam, aber nicht als Generalheilmittel. Sie kehrt nicht die Darlegungslast um; im Streit muss die Partei, die sich auf Teilnichtigkeit beruft, die Auslegung tragen.

**Mustertext (Individualvertrag, B2B):**

```
Sollte eine Bestimmung dieses Vertrages unwirksam oder undurchfuehrbar sein
oder werden, bleibt die Wirksamkeit der uebrigen Bestimmungen unberuehrt.
Anstelle der unwirksamen oder undurchfuehrbaren Bestimmung gilt diejenige
wirksame und durchfuehrbare Regelung als vereinbart, die dem wirtschaftlichen
Zweck der unwirksamen oder undurchfuehrbaren Bestimmung am naechsten kommt.
Entsprechendes gilt fuer den Fall, dass dieser Vertrag eine Luecke enthaelt.
```

### Klausel 2: Schriftformklausel (§ 126 BGB)

**Voraussetzung:** Gewillkuerte Schriftform nach § 127 BGB. Vorsicht: doppelte Schriftformklausel im B2B grundsaetzlich wirksam (Aenderung dieser Klausel selbst nur in Schriftform), im B2C nach AGB-Recht angreifbar.

**Mustertext (Doppelte Schriftform, B2B):**

```
Aenderungen und Ergaenzungen dieses Vertrages beduerfen der Schriftform.
Dies gilt auch fuer die Aufhebung dieser Schriftformklausel selbst.
Muendliche Nebenabreden bestehen nicht.
```

**Hinweis:** Der BGH hat in mehreren Entscheidungen klargestellt, dass eine doppelte Schriftformklausel in AGB die mittels Individualabrede vorgenommene Aenderung nicht ausschliessen kann. Vor Verwendung im B2C aktuelle BGH-Rspr. pruefen.

### Klausel 3: Gerichtsstandsvereinbarung (§ 38 ZPO)

**Voraussetzung:** Beide Parteien Kaufleute, juristische Personen des oeffentlichen Rechts oder oeffentlich-rechtliche Sondervermoegen (§ 38 Abs. 1 ZPO), oder Auslandsbezug. Im B2C unzulaessig (§ 38 Abs. 2, Abs. 3 ZPO).

**Mustertext (B2B):**

```
Ausschliesslicher Gerichtsstand fuer alle Streitigkeiten aus diesem Vertrag
ist Berlin.
```

### Klausel 4: Rechtswahl (Rom-I-VO)

**Voraussetzung:** Vertragliches Schuldverhaeltnis. Art. 3 Rom-I-VO erlaubt Rechtswahl. Verbraucherschutz nach Art. 6 Rom-I-VO bleibt unberuehrt.

**Mustertext:**

```
Dieser Vertrag unterliegt deutschem Recht unter Ausschluss des UN-Kaufrechts
(CISG) und des deutschen internationalen Privatrechts.
```

### Klausel 5: Erfuellungsort

**Voraussetzung:** Modifikation des § 269 BGB (Wohnsitz des Schuldners).

**Mustertext:**

```
Erfuellungsort fuer Lieferung und Zahlung ist der Sitz des Lieferanten.
```

### Klausel 6: Bekanntmachungs- bzw. Mitteilungsklausel

**Voraussetzung:** Empfangszustaendigkeit, Form der Erklaerung.

**Mustertext:**

```
Mitteilungen unter diesem Vertrag bedurften der Textform (§ 126b BGB). Sie
gelten als zugegangen, wenn sie an die im Rubrum angegebene Anschrift
gerichtet sind und in den Macht-bereich des Empfaengers gelangen.
```

### Klausel 7: Uebertragungsverbot (§ 399 BGB)

**Voraussetzung:** Vertragliches Abtretungsverbot. Wirksamkeit bei B2B nach § 354a HGB beschraenkt (Geldforderungen aus beiderseitigem Handelsgeschaeft bleiben abtretbar).

**Mustertext:**

```
Rechte und Pflichten aus diesem Vertrag duerfen nur mit vorheriger
schriftlicher Zustimmung der jeweils anderen Partei uebertragen oder
abgetreten werden. § 354a HGB bleibt unberuehrt.
```

### Klausel 8: Gesamtnichtigkeitsausschluss (zusammen mit Salvatorischer Klausel)

Faellt unter Klausel 1 (Salvatorische).

## Typische Drafting-Fehler

- **Salvatorische Klausel als Allzweckwaffe.** Sie heilt nicht jede Klausellucke und kehrt nicht die Darlegungslast um.
- **Doppelte Schriftform im B2C.** Vorsicht. Im AGB-Verhaeltnis schwer wirksam zu halten.
- **Gerichtsstand mit Verbraucher.** Unzulaessig nach § 38 Abs. 2, Abs. 3 ZPO.
- **Rechtswahl ohne CISG-Ausschluss.** Bei internationalem Warenkauf gilt CISG automatisch, falls nicht ausgeschlossen.
- **Mitteilungsklausel ohne Empfangsadresse.** Macht keine Zustellung pruefbar.
- **Abtretungsverbot ohne § 354a HGB.** Bei Geldforderungen aus Handelsgeschaeft unwirksam.

## Ausgabeformat

- Boilerplate-Abschnitt fertig formuliert, durchnummeriert.
- Tabelle Klausel zu AGB-Risiko zu Hinweis.

## Beispiel

**Boilerplate-Block (B2B-Lieferantenvertrag):**

```
§ 12 Salvatorische Klausel
[Text wie oben]

§ 13 Schriftform
[Text wie oben]

§ 14 Gerichtsstand und Rechtswahl
(1) Ausschliesslicher Gerichtsstand ist Berlin.
(2) Dieser Vertrag unterliegt deutschem Recht unter Ausschluss des UN-Kaufrechts.

§ 15 Erfuellungsort
Erfuellungsort fuer Lieferung und Zahlung ist der Sitz des Lieferanten.

§ 16 Abtretung
[Text wie oben]
```

## Querverweise

- `dokumentarchitektur-vertrag-und-schriftsatz`
- `agb-konforme-klauseln-305-310-bgb`
- `b2b-vs-b2c-klausel-strategie`
- `verweis-und-querverweis-technik`

## Quellen (Stand 05/2026)

- § 139 BGB, § 126 BGB, § 127 BGB, § 269 BGB, § 399 BGB, § 354a HGB. gesetze-im-internet.de.
- § 38 ZPO; Rom-I-VO (Verordnung (EG) Nr. 593/2008). eur-lex.europa.eu.
- BGH-Rspr. zu salvatorischer Klausel und doppelter Schriftformklausel: vom Nutzer mit konkretem Aktenzeichen ueber bundesgerichtshof.de zu verifizieren.

## 2. `definitionen-klauseln-stringent`

**Fokus:** Defined Terms in Vertraegen sauber bauen. Hierarchie und Konsistenz: einmal definieren, im gesamten Dokument einheitlich verwenden, mit Grossschreibung sichtbar machen. Trennung zwischen zentralem Definitionen-Abschnitt (alphabetisch) und Inline-Definitionen ('im Folgenden Vertrag'). Mit Beispielklauseln, Konsistenzpruefung per Suchen-Ersetzen-Logik und einem Katalog typischer Anti-Pattern wie verschachtelte Definitionen oder Definitionsdoppel.

# Definitionen-Klauseln stringent

## Zweck

Defined Terms (definierte Begriffe) sind das Skelett eines komplexen Vertrages. Sie sorgen dafuer, dass derselbe Sachverhalt im gesamten Dokument identisch beschrieben wird. Wer "Vertrag" definiert, muss "Vertrag" konsequent meinen, nicht abwechselnd "diese Vereinbarung", "der vorliegende Kontrakt" oder "die Abrede".

Dieser Skill liefert die Drafting-Disziplin: ein Begriff, eine Definition, einheitliche Verwendung. Er trennt zentrale Definitionen (alphabetischer Abschnitt am Anfang) von Inline-Definitionen (im Fliesstext). Er gibt Ihnen die Konsistenzpruefung an die Hand.

## Eingaben

- Vertragsentwurf oder Term Sheet
- Liste der zu definierenden Begriffe (oder Auftrag, sie zu identifizieren)
- Position im Vertrag: zentraler Abschnitt vs. Inline

## Rechtlicher und methodischer Rahmen

- § 305c Abs. 2 BGB: Unklarheitenregel zulasten des Verwenders. Inkonsistente Begriffe gehen zulasten des AGB-Verwenders.
- § 307 Abs. 1 Satz 2 BGB: Transparenzgebot. Defined Terms muessen klar verstaendlich definiert sein.
- §§ 133, 157 BGB: Vertragsauslegung. Defined Terms binden die Auslegung.
- Konvention: Defined Terms grossschreiben oder kursiv setzen, damit sie im Text sichtbar sind.

## Ablauf / Checkliste

1. **Begriffe identifizieren.** Welche Konzepte tauchen mehr als einmal auf? Welche tragen Rechtsfolgen?
2. **Zentral oder inline?** Faustregel: mehr als zehn Begriffe oder Verwendung in mehreren Klauseln, dann zentraler Definitionen-Abschnitt.
3. **Definitionsstruktur waehlen.** Alphabetisch (Default) oder thematisch (bei sehr grossen Vertraegen).
4. **Defined Term auszeichnen.** Grossschreibung des Anfangs ("Vertrag", "Vertragspartei", "Closing", "Long Stop Date") oder kursiv ("Vertrag").
5. **Definition formulieren.** Knapp, eindeutig, ohne andere Defined Terms zu verschachteln, wo unnoetig.
6. **Konsistenzpruefung durchfuehren.** Volltextsuche, jeder Defined Term im Dokument identisch geschrieben.
7. **Anti-Pattern checken.** Siehe unten.

### Beispielklauseln

**Zentraler Definitionen-Abschnitt:**

```
§ 1 Definitionen

In diesem Vertrag haben die folgenden Begriffe die nachstehende Bedeutung:

"Anlage" bezeichnet jede mit diesem Vertrag verbundene Anlage gemaess Anlagenverzeichnis.

"Bestellt" bezeichnet die Bestellung der Ware durch den Besteller gemaess § 3.

"Besteller" bezeichnet die [Besteller AG, Anschrift, HRB ...], die Partei dieses Vertrages ist.

"Closing" bezeichnet den Vollzug dieses Vertrages gemaess § 8.

"Lieferant" bezeichnet die [Lieferant GmbH, Anschrift, HRB ...], die Partei dieses Vertrages ist.

"Parteien" bezeichnet den Besteller und den Lieferanten gemeinsam; "Partei" bezeichnet jede der beiden.

"Vertrag" bezeichnet diese Vereinbarung einschliesslich aller Anlagen.

"Vertraulichkeitszeitraum" bezeichnet den in § 7 Abs. 3 definierten Zeitraum.
```

**Inline-Definition (Kurzvertrag):**

```
Zwischen der A-GmbH, Musterstrasse 1, 10115 Berlin (im Folgenden "Lieferant"),
und der B-AG, Beispielstrasse 2, 20095 Hamburg (im Folgenden "Besteller"),
wird folgender Liefervertrag (im Folgenden "Vertrag") geschlossen.
```

### Konsistenzpruefung

| Schritt | Suche | Erwartet |
|---|---|---|
| 1 | "Vertragspartei" | nicht vorhanden, wenn "Partei" definiert ist |
| 2 | "Vereinbarung" | nicht vorhanden im operativen Text, wenn "Vertrag" definiert ist |
| 3 | "vorliegender Kontrakt" | streichen |
| 4 | "Liefergegenstand" und "Ware" | nur einer als Defined Term zulaessig |
| 5 | "Besteller" und "Auftraggeber" | nur einer |

### Anti-Pattern

- **Verschachtelte Definitionen.** "Vertrag bezeichnet diese Vereinbarung einschliesslich aller Anlagen, soweit nichts anderes bestimmt ist." Streichen Sie den Soweit-Zusatz oder definieren Sie ihn explizit.
- **Definitionsdoppel.** "Lieferant" im Vorspann und nochmal in § 1.
- **Wechselnde Schreibweise.** "Closing" und "closing" sind unterschiedliche Begriffe in der Volltextsuche.
- **Zirkulaere Definitionen.** "Lieferung" bezeichnet die Lieferung der Ware. Streichen oder funktional definieren.
- **Ungenutzte Defined Terms.** Wer definiert, soll auch verwenden. Sonst streichen.

## Typische Drafting-Fehler

- Zentrale Definitionen ohne Auszeichnung. Defined Terms verschwinden im Fliesstext.
- Falsche Reihenfolge. Begriffe werden verwendet, bevor sie definiert sind. Loesung: vorne definieren oder Defined Term mit Verweis "(siehe § 12)" einfuehren.
- Klein- statt Grossschreibung im Defined Term. "Vertrag" und "vertrag" sind nicht dasselbe.
- Definitionen, die selbst Rechtsfolgen anordnen. Definitionen definieren, sie regeln nicht. "Lieferzeit bezeichnet vier Wochen; bei Verzug schuldet der Lieferant Schadensersatz." Die Schadensersatzregelung gehoert in die operative Klausel.
- Defined Terms in der Praeambel. Praeambel ist Kontext, nicht Regelung.

## Ausgabeformat

- Definitionen-Abschnitt fertig formuliert, alphabetisch.
- Konsistenztabelle mit Treffern, die zu streichen oder zu vereinheitlichen sind.
- Optional: Markup im Originalvertrag mit Hinweisen pro Treffer.

## Beispiel

**Aufgabe:** "Bauen Sie aus folgendem Term Sheet einen Definitionen-Abschnitt: Lieferant ist eine GmbH, Besteller eine AG, Liefergegenstand sind Industrieventile, Closing erfolgt am Long Stop Date oder spaeter, Anlage 1 enthaelt die technische Spezifikation."

**Loesung:**

```
§ 1 Definitionen

"Anlage 1" bezeichnet die technische Spezifikation des Liefergegenstandes.

"Besteller" bezeichnet die [Besteller AG, Anschrift, HRB ...].

"Closing" bezeichnet den Vollzug dieses Vertrages gemaess § 8.

"Liefergegenstand" bezeichnet die in Anlage 1 spezifizierten Industrieventile.

"Lieferant" bezeichnet die [Lieferant GmbH, Anschrift, HRB ...].

"Long Stop Date" bezeichnet den 31. Dezember 2026.

"Parteien" bezeichnet den Besteller und den Lieferanten gemeinsam.

"Vertrag" bezeichnet diese Vereinbarung einschliesslich aller Anlagen.
```

## Querverweise

- `dokumentarchitektur-vertrag-und-schriftsatz`
- `verweis-und-querverweis-technik`
- `transparenzgebot-307-bgb`
- `drafting-prinzipien-klarheit-bestimmtheit-praezision`

## Quellen (Stand 05/2026)

- § 305c Abs. 2 BGB, § 307 Abs. 1 Satz 2 BGB, §§ 133, 157 BGB. gesetze-im-internet.de.
- Konvention zur Defined-Terms-Auszeichnung folgt internationaler M&A-Praxis und ist in deutscher Wirtschaftsvertragsgestaltung etabliert. Konkretes Hauskonvention je Kanzlei pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
