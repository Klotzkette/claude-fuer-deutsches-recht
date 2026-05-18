---
name: privilege-log-review
description: Erstprüfung der Vertraulichkeits- und Vorlageschutzklassifizierung von Dokumenten in Prozessmandaten — offensichtlich geschützte, offensichtlich nicht geschützte und zweifelhafte Dokumente werden sortiert und für die anwaltliche Prüfung markiert. Lädt, wenn der Nutzer Dokumente auf Vertraulichkeitsschutz prüfen, eine Vorlagepflicht-Liste erstellen oder vorzulegende Unterlagen nach § 142 ZPO oder § 97 StPO sichten möchte.
language: de
triggers:
  - "Vertraulichkeitsprotokoll prüfen"
  - "Vorlagepflicht Dokumente"
  - "Mandatsgeheimnis prüfen"
  - "§ 142 ZPO Vorlage"
  - "§ 97 StPO Beschlagnahmeschutz"
  - "Zeugnisverweigerung Berufsgeheimnisträger"
  - "Verschwiegenheit anwaltlich"
  - "Dokumentenvorlage Klage"
  - "Beschlagnahmeverbot Kanzlei"
---

# Vertraulichkeitsschutz-Erstprüfung (Vorlagepflicht und Verschwiegenheit)

## Zweck

Ein Dokumentensatz im Prozess hat drei Arten von Einträgen: zweifelsfrei geschützt, zweifelsfrei nicht geschützt und die Fälle, die juristisches Urteilsvermögen erfordern. Dieser Skill sortiert die ersten beiden Kategorien, damit die Anwaltszeit vollständig für die dritte zur Verfügung steht.

**Dies ist eine Erstprüfung. Der Anwalt prüft jeden markierten Eintrag. Keine Ausnahmen.**

Hinweis: Ein direktes Pendant zum US-amerikanischen „privilege log" gibt es im deutschen Recht nicht. Dieser Skill deckt die deutschen Rechtsinstitute ab, die vergleichbare Schutzfunktionen erfüllen: Vorlagepflicht nach § 142 ZPO, Beschlagnahmeschutz nach § 97 StPO, Zeugnisverweigerungsrecht nach § 53 StPO und die anwaltliche Verschwiegenheitspflicht nach § 43a Abs. 2 BRAO, § 203 StGB.

## Eingaben

- **Dokumentenbestand** (erforderlich): Dateipfad oder im Dialog übermittelte Dokumentenliste
- **Mandatsbezeichnung (Slug)**: Zur Zuordnung in die Mandatsakte
- **Verfahrensart**: ZPO-Verfahren, StPO-Verfahren, VwGO, FGO, SGG — maßgeblich für die anwendbaren Normen
- **Kontext**: Wurde eine Urkundenvorlageanordnung nach § 142 ZPO erlassen? Liegt eine Durchsuchungs-/Beschlagnahmemaßnahme vor?

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 142 ZPO** — Anordnung der Urkundenvorlegung durch das Gericht; Voraussetzungen: erheblich und zumutbar; kein Zwang zur Vorlage, wenn Verweigerungsrecht besteht.
- **§ 144 ZPO** — Anordnung der Inaugenscheinnahme; parallele Schranken wie § 142 ZPO.
- **§ 97 StPO** — Beschlagnahmeverbote; insbesondere Abs. 1 Nr. 1: Schriftstücke des Rechtsanwalts, die Zeugnisverweigerungsberechtigten gehören; Abs. 2: Schutz von Dokumenten im Gewahrsam des Verteidigers oder Beistands.
- **§ 53 StPO** — Zeugnisverweigerungsrecht der Rechtsanwälte, Ärzte, Notare und sonstiger Berufsgeheimnisträger; gilt auch im Verfahren auf Vorlage.
- **§ 53a StPO** — Erstreckt das Zeugnisverweigerungsrecht auf berufsmäßig tätige Gehilfen.
- **§ 43a Abs. 2 BRAO** — Absolute Verschwiegenheitspflicht des Rechtsanwalts; schützt alle Informationen, die der Anwalt in Ausübung des Berufs anvertraut bekommt.
- **§ 203 Abs. 1 Nr. 3 StGB** — Strafbare Verletzung von Privatgeheimnissen durch Rechtsanwälte; stärkt § 43a BRAO strafrechtlich ab.
- **§ 160a StPO** — Schutz von Berufsgeheimnisträgern bei verdeckten Ermittlungsmaßnahmen; gilt über den Verweis für den gesamten Bereich der Beweiserhebung.

### Besonderheit: Syndikusrechtsanwalt (§ 46 BRAO)

Der Syndikusrechtsanwalt (§ 46 BRAO) hat eine Zwitterstellung. Die Verschwiegenheitspflicht und der Beschlagnahmeschutz gelten nur für seine Tätigkeit als Anwalt (§ 46 Abs. 3 BRAO: Befugnis zum Tätigwerden in Rechtsangelegenheiten des Arbeitgebers), nicht für rein kaufmännische oder unternehmensinterne Dokumente. Das OLG Hamburg hat dies für Konzernmandatsverhältnisse konkretisiert. Im EU-Kartellverfahren ist die Korrespondenz von Syndikusanwälten ohnehin nicht geschützt (EuGH, Rs. C-550/07 P — Akzo Nobel).

### Leitentscheidungen

- **BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, NJW 2005, 1917** — Verfassungsrechtlicher Schutz des Mandatsgeheimnisses; Durchsuchung in Kanzleiräumen ist nur bei dringendem Tatverdacht gegen den Anwalt selbst zulässig; Beschlagnahmeverbot des § 97 StPO ist verfassungsrechtlich abgesichert.
- **BGH, Beschl. v. 10.07.2019 – StB 23/19, NStZ 2019, 687 Rn. 12 ff.** — Reichweite des Beschlagnahmeverbots nach § 97 StPO bei Durchsuchung einer Rechtsanwaltskanzlei; Beweismittelgewahrsam des Verteidigers.
- **BGH, Beschl. v. 07.11.2018 – XII ZB 2/16, NJW 2019, 374 Rn. 20** — Vorlageverweigerung nach § 142 ZPO; Grenzen des gerichtlichen Ermessens bei anwaltlichen Korrespondenzdokumenten.
- **EuGH, Urt. v. 08.12.2022 – C-694/20 (Orde van Vlaamse Balies)** — Schutz anwaltlicher Kommunikation im EU-Recht; Pflicht zur Meldung von Steuergestaltungen (DAC6-Richtlinie) verletzt die Verteidigungsrechte, soweit Rechtsanwälte zur Offenbarung mandatsrelevanter Informationen verpflichtet werden; wegweisend für den Schutzumfang im EU-Kontext.

### Kommentarliteratur

- `Meyer-Goßner/Schmitt, StPO, 67. Aufl. 2024, § 97 Rn. 4 ff.` — Beschlagnahmeverbot; Gewahrsam; Treuhandverhältnis.
- `Zöller/Greger, ZPO, 35. Aufl. 2024, § 142 Rn. 5 ff.` — Urkundenvorlagepflicht; Weigerungsrechte; Verhältnismäßigkeit.
- `Henssler/Prütting/Dittmann, BRAO, 5. Aufl. 2023, § 43a Rn. 44 ff.` — Verschwiegenheitspflicht; Schutzbereich; Durchbrechungen.
- `BeckOK StPO/Bär, 52. Ed. (Stand 01.01.2024), § 53 Rn. 8 ff.` — Zeugnisverweigerungsrecht des Rechtsanwalts; Reichweite auf Dritte.

## Ablauf

### Schritt 0: Anwendbares Recht bestimmen

Vor der Dokumentenprüfung: Welches Verfahrensrecht gilt?

- **ZPO-Verfahren**: § 142 ZPO (Urkundenvorlage), § 144 ZPO (Inaugenscheinnahme); Weigerungsrecht nach § 142 Abs. 2 ZPO i.V.m. §§ 383, 384 ZPO.
- **StPO-Verfahren**: § 97 StPO (Beschlagnahmeverbot); § 53 StPO (Zeugnisverweigerungsrecht); § 160a StPO (Schutz bei Ermittlungsmaßnahmen).
- **VwGO/FGO/SGG**: Parallelvorschriften; Vorlagepflicht vergleichbar §§ 86, 99 VwGO; Akteneinsichtsrechte.

Quellenattribuierung: Jeden Regelhinweis und jede Entscheidung in der Ausgabe mit Herkunftsnachweis versehen: `[Primärquelle]`, `[Kommentar – prüfen]`, `[Trainingsdaten – prüfen]`. Quellen mit Prüfvermerk tragen höheres Fehlerrisiko und sollten zuerst verifiziert werden.

### Schritt 1: Formatkontrolle

Hat der Dokumentensatz die erforderlichen Angaben?

| Feld | Vorhanden? |
|---|---|
| Datum | |
| Verfasser/Urheber | |
| Empfänger (An, CC, BCC) | |
| Dokumentenart | |
| Behaupteter Schutztatbestand (Mandatsgeheimnis / Beschlagnahmeverbot / Zeugnisverweigerung) | |
| Beschreibung (ausreichend zur Beurteilung ohne Offenbarung des Geschützten) | |

Fehlende Felder → vor der inhaltlichen Prüfung zur Ergänzung markieren.

### Schritt 2: Eintrag für Eintrag

Für jeden Eintrag:

```
Eintrag [N] ([Aktenzeichen/Belegnummer]): [✅ Geschützt | ✅ Geschützt + ⚠️ Markiert | ❌ Nicht geschützt (Bewertung)]
[Bei ✅ (ohne Markierung): einzeilige Begründung mit Norm]
[Bei ✅ + ⚠️: Schutz behalten; konkrete Frage, die der Anwalt beantworten muss; Argumente pro und contra]
[Bei ❌: einzeilige Begründung — Schutz bleibt im Register, bis der Anwalt ihn entfernt]
```

**Dreistufenregel:** Der Skill entscheidet nie stillschweigend eine subjektive Schwellenwertfrage. Bei jeder unsicheren Entscheidung — Mandatsgeheimnis oder rein kaufmännischer Zweck, Beschlagnahme­schutz grenzwertig, gemischter Inhalt, Beteiligung Dritter — wird die Schutzklassifizierung beibehalten und eine ⚠️-Markierung gesetzt. Zu wenig als geschützt zu kennzeichnen öffnet die Tür zu Beweismittelverlust (einbahnige Tür); zu viel als geschützt zu kennzeichnen ist vom Anwalt korrigierbar (zweiseitige Tür). Den korrigierbaren Fehler bevorzugen.

### Schritt 3: Mustererkennung

Über den gesamten Dokumentensatz:

- Gleiche Frage wiederholt? (Z. B. dieselbe Drittpartei in 50 Einträgen — eine Entscheidung löst 50 Markierungen)
- Überklassifizierungsmuster? (Wenn alles als geschützt gekennzeichnet wird, ohne Differenzierung — dem Anwalt zur Kenntnis bringen; aber die Entscheidung zur Einschränkung liegt beim Anwalt)
- Unzureichende Beschreibungen? (So vage, dass ein Gericht eine In-Camera-Prüfung anordnen könnte)

## Ausgabeformat

### Vor der Vorlage an das Gericht oder die Gegenseite — Schranke

Vor Einreichung einer Aufstellung vorzulegender/verweigernder Dokumente beim Gericht oder vor Übergabe an die Gegenseite:

> Die Vorlage oder Verweigerung von Dokumenten hat rechtliche Folgen — unzureichende Verweigerungsbegründungen können zur Vorlageerzwingung führen; unberechtigte Zurückhaltung kann Kostennachteile auslösen; eine versehentlich offengelegte Unterlage ist möglicherweise nicht rückrufbar. Wurde dies mit einem Anwalt besprochen? Falls ja: bitte bestätigen. Falls nein, hier ist ein Briefing für das Gespräch:
>
> [Zusammenfassung: Mandat, Anzahl geprüfter Dokumente, ⚠️-Markierungen und kritische Grenzfälle, Muster (Überklassifizierung, vage Beschreibungen), Normenlage je Schutztatbestand, was bei Vorlage schiefgehen kann.]

Ohne ausdrückliche Bestätigung wird die Liste nicht als vorlagebereits behandelt. Erstprüfung, Sortierung und interne Markierung erfordern die Schranke nicht — der Umgang mit dem Gericht schon.

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

## Vertraulichkeitsschutz-Erstprüfung: [Mandat] — [Datum]

**Anwendbare Normen:** [§ 142 ZPO / § 97 StPO / § 53 StPO / § 43a BRAO — Pinpoint-Zitate] `[UNSICHER — Aktualität prüfen]`
**Dokumente geprüft:** [N]
**Ergebnis:** [N] ✅ sicher geschützt / [N] ✅+⚠️ Schutz beibehalten & markiert / [N] ❌ Schutzentfernung empfohlen (Anwalt bestätigt)

### ✅ + ⚠️ Markiert — Schutz beibehalten, Anwalt entscheidet

| Eintrag | Belegnummer | Frage | Pro Schutz | Contra Schutz | Zu klärende Entscheidung |
|---|---|---|---|---|---|
| [N] | [Bereich] | [Was subjektiv ist] | [eine Zeile] | [eine Zeile] | [konkrete zu treffende Entscheidung] |

### ❌ Schutzentfernung empfohlen (Anwalt bestätigt vor Streichung)

| Eintrag | Belegnummer | Begründung |
|---|---|---|

*Vermerkt, nicht vollzogen. Der Skill entfernt keine Schutzklassifizierungen aus dem Register — das tut der Anwalt nach Prüfung.*

### ✅ Geschützt (kein Handlungsbedarf)

[Anzahl. Liste auf Anfrage abrufbar.]

### Musterbeobachtungen

[Wiederkehrende Fragen, Überklassifizierung, Beschreibungsprobleme]

### Markierungsdisziplin

- `[PRÜFEN: Sachaussage über Dokument/Verfasser/Datum]`
- `[UNSICHER: Grenzfall Schutztatbestand / Beschlagnahme / Reichweite]`
- `[BELEG FEHLT: Norm, lokale Variante oder Entscheidung als Stütze]`

---

**Anwalt muss alle ⚠️- und ❌-Einträge vor jeder Maßnahme prüfen.**

**Schutzwürdigkeit des Ausgabedokuments:** Diese Prüfung liest per definitionem schutzkandidaten-fähige Unterlagen. Das Ausgabedokument erbt diesen Status — es ist mit dem Mandatsmaterial zu verwahren, entsprechend zu kennzeichnen und nicht außerhalb des Vertrauenskreises zu verbreiten. Eine Weitergabe kann selbst den Schutz aushöhlen.
```

## Beispiel

**Sachverhalt:** Anordnung nach § 142 ZPO; Gericht verlangt Vorlage aller E-Mails zwischen der Partei und ihrem Rechtsanwalt zu einer Schadensersatzforderung.

**Erstprüfungsergebnis:**
- ✅ 12 E-Mails: Mandatsgeheimnis (§ 43a Abs. 2 BRAO); Anwalt bittet um Rechtsrat, Anwalt erteilt Rat; keine Drittpartei im Verteiler.
- ✅+⚠️ 3 E-Mails: Anwalt in CC bei rein kaufmännischer Verhandlung; dominanter Zweck unklar → Anwalt entscheidet.
- ❌ 2 E-Mails: Keine anwaltliche Beteiligung; CC an Anwalt ohne rechtliche Substanz; Bewertung: kein Schutz nach § 43a BRAO.

## Risiken und typische Fehler

- **Syndikusanwalt-Grenzfälle:** Die Schutzwürdigkeit von Korrespondenz des Syndikusrechtsanwalts hängt von seiner konkreten Funktion im Einzelfall ab (§ 46 Abs. 3 BRAO) — nie pauschal als „sicher geschützt" klassifizieren.
- **EU-Kartellverfahren:** Im EU-Kartellverfahren und bei BKartA-Ermittlungen ist Korrespondenz mit Syndikusanwälten nicht geschützt (EuGH Akzo Nobel, C-550/07 P).
- **Wirkung der Weitergabe:** Wird ein eigentlich geschütztes Dokument im Verfahren vorgelegt (auch versehentlich), kann der Schutz vollständig entfallen — Rückruf ist möglich, aber keineswegs sicher.
- **Beschreibungstiefe:** Zu vage Beschreibungen können dazu führen, dass das Gericht eine In-Camera-Vorlage zur eigenen Prüfung anordnet.
- **Fehlende Quellenverifizierung:** Alle Normen- und Entscheidungshinweise in der Ausgabe sind KI-generiert; vor einer Einreichung sind sie gegen Primärquellen (juris, beck-online, Wolters Kluwer) zu verifizieren.

## Quellenpflicht

- Gesetzestexte: §§ 142, 144 ZPO; §§ 53, 53a, 97, 160a StPO; §§ 43a, 46 BRAO; § 203 StGB; §§ 86, 99 VwGO
- Rechtsprechung: BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, NJW 2005, 1917; BGH, Beschl. v. 10.07.2019 – StB 23/19, NStZ 2019, 687; EuGH, Urt. v. 08.12.2022 – C-694/20 (Orde van Vlaamse Balies)
- Kommentare: Meyer-Goßner/Schmitt, StPO, 67. Aufl. 2024, § 97; Zöller/Greger, ZPO, 35. Aufl. 2024, § 142; Henssler/Prütting/Dittmann, BRAO, 5. Aufl. 2023, § 43a

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
