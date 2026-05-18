---
name: stakeholder-summary
description: >
  Übersetzt ein Vertragsprüfungsmemo in eine Zusammenfassung für
  Geschäftsführung, Vorstand oder Einkauf — kein Rechtsgutachten, sondern
  eine klare Entscheidungsgrundlage. Lädt, wenn der Nutzer „Zusammenfassung
  für Geschäftsführung", „für den Vorstand aufbereiten", „Managementzusammenfassung",
  „für Einkauf erklären" oder „nicht-juristische Zusammenfassung" sagt.
language: de
triggers:
  - "Zusammenfassung Geschäftsführung"
  - "Vorstandszusammenfassung"
  - "Management-Briefing"
  - "Risikomatrix"
  - "nicht-juristische Zusammenfassung"
  - "für Einkauf aufbereiten"
  - "Vertragsstatus berichten"
  - "Mandantenkurzfassung"
---

# Mandantenzusammenfassung Vertragsrecht

## Zweck

Der Geschäftsführer, der diesen Vertrag beauftragt hat, will kein
Rechtsgutachten. Er will wissen: Können wir unterschreiben? Was ist der
Haken? Was müssen wir tun? Diese Skill liest das fertige Prüfungsmemo
und verdichtet es auf genau das.

Lädt, wenn eine Vertragsanalyse abgeschlossen ist und das Ergebnis an
eine Person außerhalb der Rechtsabteilung weitergegeben werden soll.

## Eingaben

- Das fertige Prüfungsmemo (aus `/vertragsrecht:review`)
- Optional: Empfänger (Geschäftsführung, Vorstand, Einkauf, Finance, IT)
- Optional: Kanal (E-Mail, Slack, Jour fixe)

## Rechtlicher Rahmen

### Grundlagen der rechtssicheren Kommunikation an Mandanten

Zusammenfassungen an Mandanten und interne Nicht-Juristen unterliegen
besonderen Sorgfaltsanforderungen — auch informelle Kurzfassungen erzeugen
Vertrauen beim Empfänger und können haftungsrechtliche Folgen haben, wenn
sie wesentliche Risiken weglassen.

- § 280 Abs. 1 BGB — Pflichtverletzung durch fehlerhafte Beratung;
  Schadensersatzpflicht des Anwalts bei falsch oder unvollständig
  kommunizierten Risiken
- § 675 BGB i.V.m. §§ 611 ff. BGB — Anwaltsvertrag als Dienstvertrag
  mit besonderer Sorgfaltspflicht; vollständige und zutreffende Aufklärung
  des Mandanten
- § 43a Abs. 2 BRAO — Mandatsgeheimnis; Weiterleitung von Zusammenfassungen
  außerhalb des Vertrauenskreises bedarf der Prüfung (Privilegkreis)
- §§ 164 ff. BGB — Vollmacht; eine Zusammenfassung, die impliziert, der
  Vertrag sei unterschriftsreif, kann als Beratungsleistung wirken, auf
  die sich der Mandant verlässt

### Sorgfaltspflicht bei Risikoangaben

- BGH, Urt. v. 10.07.2014 – IX ZR 197/12, NJW 2014, 2951 Rn. 14
  (Anwaltshaftung bei fehlerhafter Beratung; vollständige Risikoaufklärung
  als Kernpflicht; § 280 Abs. 1 BGB, § 675 BGB)
- BGH, Urt. v. 15.10.2009 – IX ZR 143/08, NJW 2010, 146 Rn. 8
  (Haftung für unvollständige Aufklärung über rechtliches Risiko;
  Schadensersatzpflicht bei Weglassen wesentlicher Informationen)
- BGH, Urt. v. 06.07.2006 – IX ZR 88/05, NJW-RR 2006, 1568 Rn. 12
  (Beratungspflicht des Rechtsanwalts; Belehrung über alle
  entscheidungsrelevanten Gesichtspunkte)
- BGH, Urt. v. 07.03.2019 – IX ZR 143/18, NJW 2019, 1949 Rn. 20
  (Aufklärungspflicht bei Vertragsgestaltung; Hinweis auf AGB-Unwirksamkeit
  als Bestandteil ordnungsgemäßer Beratung)

### Kommentarliteratur

- Palandt/Weidenkaff, BGB, 83. Aufl. 2024, § 675 Rn. 10 ff.
  (Anwaltsvertrag; Beratungspflicht, Schadensersatz bei Pflichtverletzung)
- MüKoBGB/Heermann, 9. Aufl. 2022, § 675 Rn. 50 ff.
  (Dienstvertrag mit anwaltlicher Beratungskomponente)
- Henssler/Prütting, BRAO, 5. Aufl. 2019, § 43a Rn. 80 ff.
  (Mandatsgeheimnis bei Weiterleitung von Arbeitsergebnissen)
- BeckOGK BGB/Martens, 70. Ed. (Stand 01.08.2024), § 675 Rn. 30 ff.

## Ablauf

### Schritt 1 — Mandatskontext

Prüfe `## Mandatsarbeitsbereiche` im Kanzleiprofil. Wenn aktiviert und
kein aktives Mandat gesetzt: „Für welches Mandat ist diese Zusammenfassung?
(`/vertragsrecht:matter-workspace wechseln <kürzel>` oder `kanzleiebene`)."
Aktive `mandat.md` für mandatsspezifischen Kontext laden.

### Schritt 2 — Privilegkreis-Check

Vor der Ausgabe prüfen, wohin sie geht. Wenn der Nutzer einen Empfänger
oder Kanal genannt hat:

- Interne Rechtsabteilung / unter anwaltlicher Aufsicht → privilegiertes
  Arbeitsergebnis behalten
- Geschäftsführung, Vorstand, Einkauf (intern) → Arbeitergebnis-Kennzeichnung
  entfernen oder anpassen; kein Mandatsgeheimnis verletzt, aber Kennzeichnung
  täuscht über Privilegstatus
- Gegenseite, externe Berater, Lieferant → ROT; privilegierte Kennzeichnung
  entfernen; Mandant darauf hinweisen, dass die Weiterleitung den Privilegstatus
  dieser Kommunikation beeinflussen kann

Angebot: (a) privilegierte Version für interne Rechtsabteilung, (b) bereinigte
Version für Weitergabe, (c) beides.

### Schritt 3 — Empfänger bestimmen

Wenn nicht angegeben, fragen:

> Für wen ist diese Zusammenfassung? Das bestimmt, was wichtig ist und
> was wegfällt.

| Empfänger | Interessiert an | Interessiert nicht an |
|---|---|---|
| **Geschäftsführung / Vorstand** | Unterschriftsempfehlung, Hauptrisiken, Eskalationsbedarf | Paragraphen, Klauselstruktur |
| **Einkauf / Beschaffung** | Preis, Verlängerungsmechanik, Genehmigungsweg | Haftungsstruktur |
| **Budget-/Kostenstellenverantwortlicher** | Gesamtkosten, Verlängerungspreisrisiko, außerbilanzielle Verpflichtungen | Gerichtsstand |
| **IT / Datenschutz** | Datenspeicherung, Unterauftragnehmer, AVV, ISO/SOC-Zertifizierung | Alles andere |
| **Geschäftsführer als Sponsor** | Reputationsrisiko, Rechtssicherheit, Zeitplanung | Einzelheiten |

### Schritt 4 — Zusammenfassung erstellen

**Längen-Maximum: 200 Wörter (ohne Risikomatrix und Eskalationsstatus).**
Wer mehr schreibt, packt Details hinein, die der Empfänger nicht braucht —
dafür ist das Memo da.

**Struktur (in dieser Reihenfolge):**

1. **Ein Absatz** — Urteil und Vertragsinhalt in Geschäftssprache.
   Nicht „Dienstleistungsrahmenvertrag für die Bereitstellung
   cloudbasierter Analysedienste" — sondern „das ist der Vertrag für
   das Dashboard-Tool, das das Marketing-Team angefragt hat."

2. **Ein Absatz** — Der Haken, wenn es einen gibt. Was überrascht den
   Empfänger später, wenn es ihm jetzt keiner sagt? Beispiel: „Achtung:
   der Vertrag verlängert sich automatisch jährlich; Kündigung muss
   6 Wochen vorher erfolgen. Ich habe es im Fristen-Tracker eingetragen,
   aber Sie sollten das wissen." Bei sauberem Vertrag: „Kein besonderer
   Hinweis — alles entspricht Standard."

3. **2–3 Punkte Checkliste** — Was der Empfänger konkret tun muss
   (höchstens drei Punkte; wenn ein vierter nötig ist, sind die ersten
   drei nicht präzise genug).

4. **Eine Zeile Abschluss** — Wer genehmigt, bis wann.

### Schritt 5 — Risikomatrix (optional, für Eskalationsfälle)

Wenn das Prüfungsmemo ROTE Befunde enthält oder mehrere GELBE Positionen
gleichzeitig betroffen sind, optionale Risikomatrix erstellen:

| Klausel | Risiko | Wahrscheinlichkeit | Handlung |
|---|---|---|---|
| [Klausel] | [Risiko in Geschäftssprache] | Gering / Mittel / Hoch | [konkrete Handlung] |

Die Matrix ist vom 200-Wörter-Limit ausgenommen.

### Schritt 6 — Eskalationsstatus

Das Prüfungsmemo kann mehrere Genehmigungsadressaten benennen
(GC, CISO, CFO, Geschäftsführung). Vor der Zusammenfassung zählen:

1. Wie viele Eskalationsziele hat das Prüfungsmemo genannt?
2. Wie viele Eskalationsentwürfe liegen bereits vor?
3. Delta = noch nicht eingeleitet.

Kurzer Eskalationsblock in der Zusammenfassung (oberhalb der Checkliste):

```
Eskalationsstatus: [M] von [N] Eskalationspfaden eingeleitet.
Noch ausstehend:
- [Adressat] — [ein Satz zum Befund]
```

Wenn alle eingeleitet: `[N] von [N] Eskalationspfaden eingeleitet.`
Wenn das Prüfungsmemo keine Eskalationen vorsieht: Block weglassen.

## Ausgabeformat

```markdown
[ARBEITSERGEBNIS-KENNZEICHNUNG — nur für interne juristische Kreise;
bei Weiterleitung an Nicht-Juristen entfernen]

**[Vertragspartner] [Vertragstyp]** — [UNTERSCHRIFTSREIF / ÄNDERUNGEN ERFORDERLICH / BLOCKIERT]

[Absatz 1: Was ist dieser Vertrag — in Geschäftssprache.]

[Absatz 2: Der Haken, falls vorhanden. Oder: „Kein besonderer Hinweis."]

**Eskalationsstatus:** [M] von [N] Eskalationspfaden eingeleitet.
[Ausstehende Adressaten, falls vorhanden]

**Was jetzt zu tun ist:**
- [ ] [Handlungspunkt — konkret]
- [ ] [Handlungspunkt — konkret]

**Genehmigung:** [Wer genehmigt und bis wann]
```

### Übersetzungstabelle: juristischer Befund → Geschäftssprache

| Juristischer Befund | Übersetzung für Empfänger |
|---|---|
| „Haftung auf 12 Monate Vergütung begrenzt" | „Wenn sie etwas kaputt machen, können wir maximal ein Jahresgehalt zurückfordern." |
| „Keine ordentliche Kündigung" | „Einmal unterschrieben, sitzen wir die Laufzeit aus — wir können nicht einfach kündigen, wenn wir den Dienst nicht mehr nutzen." |
| „Automatische Verlängerung mit 6-Wochen-Frist" | „Verlängert sich jedes Jahr automatisch. Kündigen müssen wir 6 Wochen vorher." |
| „Keine Freistellung bei IP-Verletzung" | „Wenn jemand klagt, dass dieses Tool ein Patent verletzt, übernimmt der Anbieter die Verteidigung nicht." |
| „Unterauftragnehmerliste nicht offengelegt" | „Wir wissen nicht, welche anderen Unternehmen über diesen Anbieter Zugang zu unseren Daten haben." |
| „AVV fehlt trotz Verarbeitung personenbezogener Daten" | „Datenschutzrechtlich ist dieser Vertrag noch nicht fertig — ein Pflichtanhang fehlt (DSGVO-Anforderung)." |
| „SLA-Gutschriften auf 10 % der Monatsgebühr begrenzt" | „Wenn das System ausfällt, bekommen wir eine kleine Gutschrift. Die deckt die tatsächlichen Ausfallkosten für das Unternehmen nicht." |

### Was NICHT hineingehört

- Paragraphennummern
- Definierte Begriffe in Anführungszeichen
- Das Wort „Haftungsfreizeichnung" (stattdessen: „sie übernehmen keine
  Verantwortung, wenn…")
- Das Wort „ungeachtet"
- Risikomatrizen mit Farbpunkten (sofern nicht explizit angefordert)
- Relativierungsfloskeln à la „Dies ist keine Rechtsauskunft" — der Empfänger
  weiß, wer diese Zusammenfassung geschrieben hat

## Beispiel

**Szenario:** SaaS-Vertrag für ein Marketing-Tool, Kunden-Seite,
zwei GELBE Befunde (automatische Verlängerung, Preisanpassungsklausel),
kein ROTER Befund. Empfänger: Geschäftsführerin.

```
VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS

**TechSoft GmbH SaaS-Lizenzvertrag** — UNTERSCHRIFTSREIF (mit Hinweis)

Das ist der Vertrag für die neue Marketing-Automatisierungsplattform,
die das Team seit Q3 testen möchte. Laufzeit 12 Monate, Jahresgebühr
24.000 €, Datenspeicherung ausschließlich in der EU.

Zwei Punkte, die Sie kennen sollten: Der Vertrag verlängert sich automatisch
um ein Jahr, wenn wir nicht 6 Wochen vorher kündigen — ich habe das im
Fristen-Tracker eingetragen. Außerdem darf TechSoft den Preis bei Verlängerung
um bis zu 5 % erhöhen; das muss in die Budgetplanung für nächstes Jahr.

Eskalationsstatus: kein Eskalationsbedarf nach Playbook-Prüfung.

**Was jetzt zu tun ist:**
- [ ] Verlängerungstermin im Kalender sichern (6 Wochen vor Ende = XX.XX.XXXX)
- [ ] Preisanpassung in Budgetplanung aufnehmen (+max. 5 % ab 2. Jahr)

**Genehmigung:** Unterschrift durch Prokuristin; keine GC-Freigabe erforderlich.
```

## Risiken und typische Fehler

- **Fristen-Tracker-Eintragung behaupten ohne Prüfung.** Nur dann schreiben
  „im Fristen-Tracker eingetragen", wenn `/vertragsrecht:fristen-tracker`
  tatsächlich für diesen Vertrag ausgeführt wurde. Andernfalls:
  „noch nicht eingetragen — bitte als Handlungspunkt aufnehmen."
- **Klauseln trunkieren.** Bedingte Klauseln vollständig paraphrasieren —
  nie verkürzte Version, die die Bedingung weglässt.
- **Privilegkreis ignorieren.** Bei Weiterleitung außerhalb der
  Rechtsabteilung Kennzeichnung anpassen; darauf hinweisen, dass die
  Weiterleitung vertraulicher Rechtsberatung an Dritte den Schutz
  dieser Kommunikation beeinflusst.
- **Eskalationsadressen weglassen.** Auch wenn der Empfänger die Namen
  nicht kennt, muss der Eskalationsstatus intern vollständig sein.
  Die Zusammenfassung signalisiert dem Anwalt, ob alle Eskalationspfade
  beschritten wurden.
- **„Kein Risiko" bei sauberem Vertrag nicht sagen.** Stattdessen:
  „Kein besonderer Hinweis — der Vertrag entspricht unserem Standard
  und ist unterzeichnungsreif."

## Quellenpflicht

Wenn die Zusammenfassung auf ein spezifisches Risiko hinweist (z. B.
DSGVO-Pflicht, Haftungsobergrenze), muss das zugrundeliegende Prüfungsmemo
die folgenden Quellen enthalten (nicht die Zusammenfassung selbst — die
ist für Nicht-Juristen):
- Gesetzesnorm (z. B. Art. 28 DSGVO, § 309 Nr. 7 BGB)
- BGH-Entscheidung in korrekter Zitierweise
- Kommentarbeleg im Bearbeiterstil
  (z. B. Palandt/Grüneberg, BGB, 83. Aufl. 2024, § 307 Rn. 45)

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
