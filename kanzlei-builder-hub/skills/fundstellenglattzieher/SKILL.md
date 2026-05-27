---
name: fundstellenglattzieher
description: "Normen- und Rechtsprechungszitate in Schriftsaetzen und Skills vereinheitlichen: einheitliche Zitierweise. Normen: allgemein BRAO. Pruefraster: Normzitat-Format, BGH-Aktenzeichen, Quellenangaben. Output: Text mit vereinheitlichten Fundstellen. Abgrenzung: nicht inhaltliche Rechtspruefung."
---

# Fundstellenglattzieher / Zitatenkorrektor

## Zweck

Dieser Skill prüft und korrigiert sämtliche juristischen Fundstellen in
einem vorliegenden Text — Schriftsatz, Memo, Aufsatz, Gutachten,
Klagebegründung, Mandantenbrief — gegen den im Repository verbindlichen
Zitierstandard ([`references/zitierweise.md`](../../../references/zitierweise.md))
und vereinheitlicht sie auf die in der deutschen Praxis übliche Form.

Der Skill ändert **ausschließlich** Form und Reihenfolge der Belege, nicht
deren inhaltliche Aussage. Er erstellt für jede Korrektur eine
Änderungsbegründung und kennzeichnet Fundstellen, die er nicht eindeutig
verifizieren kann (z. B. weil eine Heftnummer übrig bleibt oder das
Aktenzeichen unvollständig ist).

## Eingaben

- **Quelltext** mit Fundstellen (Markdown, .docx-Export, Klartext)
- Optional: **Hauseigene Stilrichtlinie**, falls zusätzlich zur
  `zitierweise.md` Spezifika gelten (z. B. Kanzleibrief: nur amtliche
  Sammlung statt Parallelfundstelle)
- Optional: **Vorgabe Notation** für Kommentare:
  - `A` = Langform: `<Bearbeiter>, in: <Werk>, <Aufl.> <Jahr>, § X Rn. Y`
  - `B` = Kurzform: `<Werk>/<Bearbeiter>, <Aufl.> <Jahr>, § X Rn. Y`
  Default: Langform (Repository-Primärnotation, Abschnitt 4 der
  `zitierweise.md`).

## Rechtlicher Rahmen

Dieser Skill setzt rein typografisch-formale Konventionen um; er macht
keine Aussage über materielles Recht. Maßgeblich ist die
**`references/zitierweise.md`** des Repositorys, dort insbesondere:

- **Abschnitt 2** — Rechtsprechung (Schema, Pflichtbestandteile, Reihenfolge)
- **Abschnitt 3** — Gesetze und Verordnungen
- **Abschnitt 4** — Kommentare (Schema, Pflichtbestandteile)
- **Abschnitt 5** — Aufsätze
- **Abschnitt 11** — Typografische Detailregeln (Zeitschriften, Bücher,
  Bearbeiter)
- **Abschnitt 12** — Gesetzeszitate (Strukturhinweise, Abkürzung)
- **Abschnitt 13** — Gebräuchliche juristische Abkürzungen

## Ablauf

### 1. Fundstellen extrahieren

Der Skill identifiziert im Quelltext alle Belege. Mustererkennung:

- Gerichtszitate: `BGH|BVerfG|BAG|BFH|BVerwG|BSG|OLG|LG|AG|EuGH|EGMR…`
  gefolgt von `Urt.|Beschl.|Vfg.` + Datum + Aktenzeichen.
- Zeitschriftenkürzel: `NJW|NJW-RR|NZA|ZIP|GRUR|MMR|K&R|ZUM|MDR|DStR|BB|
  BStBl.|FamRZ|NZG|NZI|ZInsO|WM|BKR|CR|ZD|NVwZ|DÖV|DVBl.|NStZ|StV|wistra|
  ZEV|NZM|ZMR|IBR|ZGR|ZEuP|JZ|JuS|JA|NJOZ|BeckRS|juris`.
- Kommentarmuster: `<Name>, in: <Werk>` oder `<Werk>/<Name>`.
- Gesetzeszitate: `§|Art.` + Zahl + `Abs.|S.|Nr.|UAbs.|Hs.|Var.|lit.`.

### 2. Pro Fundstelle prüfen

Für jeden Treffer wird gegen folgenden Prüfkatalog kontrolliert:

#### 2.1 Rechtsprechung

- [ ] Gericht in üblicher Abkürzung (kein „Bundesgerichtshof")?
- [ ] Entscheidungsform abgekürzt (`Urt.` / `Beschl.` / `Vfg.`)?
- [ ] Datum vorhanden mit `v. TT.MM.JJJJ`?
- [ ] Aktenzeichen vollständig (Senatszeichen + lfd. Nr. + Jahr)?
- [ ] Erste Fundstelle aus amtlicher Sammlung, sonst aus führender
      Zeitschrift?
- [ ] Randnummer nach Fundstelle als `Rn. X` (keine
      Seitenzahl-Doppelung)?
- [ ] Keine pauschale `Rn. X ff.`, sondern Punkt-Randnummer oder
      konkrete Spanne `Rn. 14–21`?
- [ ] Kein „S." bei Zeitschriftenangabe (gem. Abschnitt 11.1)?
- [ ] Kein Punkt am Ende des Zeitschriftenkürzels, wenn unzulässig?
- [ ] Kurzbezeichnung — falls etabliert — mit Gedankenstrich
      angefügt (`– „L'Oreal SA"`)?

#### 2.2 Kommentare

- [ ] Bearbeiter steht **vor** dem Werk (Langform) oder **nach** dem
      Werk mit `/` (Kurzform) — je nach Vorgabe?
- [ ] Auflage **vor** Jahr (`9. Aufl. 2024`)?
- [ ] Bei Loseblatt/BeckOK: `Ed.` statt `Aufl.` und Stand mit
      `(Stand TT.MM.JJJJ)`?
- [ ] Norm konkret (`§ 535 BGB Rn. 119`) — nicht „§ 535 BGB ff."?
- [ ] Kein Publikationsort (Ausnahme Dissertationen)?

#### 2.3 Aufsätze

- [ ] Reihenfolge `<Autor> <Zeitschrift> <Jahr>, <Anfangsseite>
      (<Zitatseite>)` eingehalten?
- [ ] Kein Aufsatztitel innerhalb des Schriftsatzes (Abschnitt 11.1)?
- [ ] Kein `S.` vor Seitenzahl bei Zeitschriftenangabe?
- [ ] Anfangsseite, Komma, Klammer-Zitatseite — keine doppelten
      Klammern, keine zusätzliche `,` zwischen Anfangsseite und
      Klammer (`819 (827)`, nicht `819, (827)`)?
- [ ] Heftnummer entfernt bei fortlaufender Seitenzählung?

#### 2.4 Gesetze

- [ ] `§` mit geschütztem Leerzeichen vor Norm-Nummer?
- [ ] `Abs.`, `S.`, `Nr.`, `UAbs.`, `Hs.`, `Var.`, `lit.` korrekt
      verwendet?
- [ ] Gesetzeskürzel der allgemein abgekürzten Gesetze ohne Vollform
      (Abschnitt 12.2)?
- [ ] Bei selten zitierten Gesetzen: Vollform beim erstmaligen Zitieren
      vorhanden? (Hinweis, kein automatischer Eingriff.)

#### 2.5 EU- und Völkerrecht

- [ ] `VO (EU) JJJJ/NNN` korrekt geschrieben?
- [ ] `Art. X Abs. Y UAbs. Z lit. a DSGVO` (lit. statt Buchstabe)?
- [ ] EuGH-Entscheidung mit Rechtssachen-Bezeichnung in Klammern
      (`C-252/21 (Meta Platforms)`)?

#### 2.6 Floskeln und Abkürzungen

- [ ] Reine „vgl."-Zusätze vor punktgenauen Belegen entfernt?
- [ ] Verwendete Abkürzungen sind in der Whitelist (Abschnitt 13)?
- [ ] Inkonsistente Schreibweisen vereinheitlicht
      (`i.V.m.` ↔ `iVm` — durchgehend `iVm`)?

### 3. Korrigieren und protokollieren

Für jede Korrektur erzeugt der Skill einen Eintrag:

```
[ID]    [vor:]                                                    [nach:]
F0001   BGH, NJW 2022, 2754                                       BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21
F0002   Grüneberg/Grüneberg § 280 Rn. 28                          Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 280 Rn. 28
F0003   vgl. BGH NJW 2015, 1296, 1297                             BGH, Urt. v. 04.02.2015 – VIII ZR 154/14, NJW 2015, 1296 (1297)
F0004   Grisse, Aufsatztitel, ZUM 2020 Heft 11, 819, 827          Grisse ZUM 2020, 819 (827)
F0005   §433 I 1 BGB                                              § 433 Abs. 1 S. 1 BGB
F0006   i.V.m. § 312a BGB                                         iVm § 312a BGB
```

### 4. Unklare Fälle markieren

Wenn der Skill **nicht** zuverlässig korrigieren kann (fehlendes
Aktenzeichen, unklare Randnummer, unbekanntes Zeitschriftenkürzel,
fehlende Auflage), wird die Fundstelle mit `[FUNDSTELLE PRÜFEN]`
markiert und ein Hinweis ausgegeben.

### 4a. Hard-Stop bei Palandt

Jeder Treffer des Wortes `Palandt` — in welcher Schreibvariante auch
immer (`Palandt`, `Palandt/Bearbeiter`, `Palandt, BGB`, `vgl. Palandt`)
— löst den Spezialmarker **`[FUNDSTELLE PRÜFEN — PALANDT]`** aus und
wird **niemals stillschweigend** in `Grüneberg` umgeschrieben. Im
Korrekturprotokoll wird die Stelle als Pflicht-Rückfrage geführt:

> Rückfrage Palandt: Der BGB-Kommentar heißt seit der 81. Aufl. 2022
> **Grüneberg**. Ist (a) eine konkrete Palandt-**Altauflage**
> (≤ 80. Aufl. 2021) gemeint — bitte Auflage und Bearbeiter angeben —
> oder (b) ein **aktueller Beleg**, der dann auf
> `Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § X Rn. Y`
> umzustellen ist?

Erst nach ausdrücklicher Antwort wird der Marker aufgelöst. Details
und Regex-Varianten siehe
[`references/regex-muster.md`](./references/regex-muster.md) Abschn. 11
sowie [`references/zitierweise.md`](../../../references/zitierweise.md)
Abschn. 10a.

### 5. Ausgabe

Drei Artefakte:

1. **Korrigierter Volltext** — Markdown/Klartext mit ersetzten
   Fundstellen, inhaltlich unverändert.
2. **Korrekturprotokoll** als Markdown-Tabelle mit
   `ID | Original | Korrektur | Begründung | Belegstelle in zitierweise.md`.
3. **Liste offener Punkte** — Fundstellen mit `[FUNDSTELLE PRÜFEN]`
   und je einem Hinweis, was fehlt.

## Ausgabeformat

````markdown
## Korrekturprotokoll Fundstellen

| ID | Original | Korrektur | Begründung | Belegstelle |
|---|---|---|---|---|
| F0001 | `BGH, NJW 2022, 2754` | `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21` | Entscheidungsform, Datum, Aktenzeichen und Randnummer ergänzt | zitierweise.md Abschn. 2 |
| F0004 | `Grisse, Aufsatztitel, ZUM 2020 Heft 11, 819, 827` | `Grisse ZUM 2020, 819 (827)` | Aufsatztitel entfällt; Heftnummer entfällt bei fortlaufender Seitenzählung; Zitatseite in Klammern | zitierweise.md Abschn. 11.1 |
| F0005 | `§433 I 1 BGB` | `§ 433 Abs. 1 S. 1 BGB` | Leerzeichen nach `§`; arabische Ziffern mit `Abs.`/`S.` | zitierweise.md Abschn. 12.1 |

## Offene Punkte

- `[FUNDSTELLE PRÜFEN]` Zeile 42 – „BGH Rn. 12" ohne Datum/Aktenzeichen.
- `[FUNDSTELLE PRÜFEN]` Zeile 78 – Kommentarwerk ohne Auflage.
````

Der korrigierte Volltext folgt im Anschluss.

## Beispiel

**Eingabe (Auszug):**

> Die Haftung folgt aus § 280 I BGB, vgl. BGH NJW 2022, 2754, 2756. Siehe
> auch Grüneberg/Grüneberg § 280 Rn 28. Zur Reichweite jüngst Grisse,
> Plattformhaftung und Wandel, ZUM 2020, Heft 11, 819, 827. Vergleichbar
> die Rspr des EuGH MMR 11, 596 ff. mit Anm. Hören – L'Oreal SA. Im
> Übrigen i. V. m. § 312a IV BGB.

**Ausgabe (korrigierter Text):**

> Die Haftung folgt aus § 280 Abs. 1 BGB (BGH, Urt. v. 13.07.2022 –
> VIII ZR 317/21, NJW 2022, 2754 (2756)). Grüneberg, in: Grüneberg, BGB,
> 84. Aufl. 2025, § 280 Rn. 28. Zur Reichweite jüngst Grisse ZUM 2020,
> 819 (827). Vergleichbar die st. Rspr. des EuGH MMR 2011, 596 Rn. 116
> mAnm Hören – L'Oreal SA. Im Übrigen iVm § 312a Abs. 4 BGB.

**Korrekturprotokoll (Auszug):**

| ID | Original | Korrektur | Begründung |
|---|---|---|---|
| F0001 | `§ 280 I BGB` | `§ 280 Abs. 1 BGB` | Römische Ziffer durch `Abs.` + arabische Ziffer |
| F0002 | `vgl. BGH NJW 2022, 2754, 2756` | `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 (2756)` | `vgl.` entfernt; Aktenzeichen/Datum ergänzt; Zitatseite in Klammern |
| F0003 | `Grüneberg/Grüneberg § 280 Rn 28` | `Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 280 Rn. 28` | Langform (Repository-Primärnotation); Auflage und Jahr ergänzt; Punkt hinter `Rn.` |
| F0004 | `Grisse, Plattformhaftung und Wandel, ZUM 2020, Heft 11, 819, 827` | `Grisse ZUM 2020, 819 (827)` | Aufsatztitel und Heftnummer entfallen; Zitatseite in Klammern |
| F0005 | `EuGH MMR 11, 596 ff. mit Anm. Hoeren – L'Oreal SA` | `EuGH MMR 2011, 596 Rn. 116 mAnm Hoeren – L'Oreal SA` | Vierstelliges Jahr; pauschales `ff.` durch konkrete Randnummer ersetzt; `mAnm` als Standardabkürzung |
| F0006 | `i. V. m.` | `iVm` | Punktlose Standardabkürzung (Abschn. 13) |

## Risiken und typische Fehler

**1. Fundstellen werden nicht „erfunden"**
Der Skill ergänzt nur, was im Originaltext **belegt oder eindeutig
ableitbar** ist. Fehlt das Aktenzeichen, wird `[FUNDSTELLE PRÜFEN]`
gesetzt — der Skill recherchiert nicht selbständig nach, weil die
Falschzuschreibung von Aktenzeichen ein gravierender Fehler wäre.

**2. Pauschale `ff.`-Ersetzung**
Eine `Rn. 28 ff.` darf nicht stumpf auf eine Punkt-Randnummer
reduziert werden, wenn die Spanne im Original tatsächlich gemeint war.
In Zweifelsfällen `[FUNDSTELLE PRÜFEN]` setzen.

**3. Heftnummern bei wechselnder Praxis**
Manche Zeitschriften (z. B. ältere Jahrgänge JuS oder JA) werden in
Bibliotheken heftbezogen geführt. Bei eindeutig fortlaufender Seiten-
zählung wird die Heftnummer entfernt; bei separat paginierten Heften
wird sie belassen.

**4. Kommentarbearbeiter-Verwechslung**
Bei Großkommentaren (Grüneberg-BGB, MüKoBGB) ist der **Bearbeiter** zu
benennen, nicht nur der Herausgeber. `Grüneberg, BGB, § 280 Rn. 28`
ohne Bearbeiternamen ist unvollständig, auch wenn Werk und Heraus-
geber denselben Namen tragen.

**5. Doppelte Punkte in Klammerzusätzen**
`§ 312a Abs. 4 BGB.)` — der Schlusspunkt der Sentenz steht **außerhalb**
der Klammer, wenn der Klammerinhalt kein vollständiger Satz ist.

**6. Auflage versus Edition**
- Klassische Kommentare: `9. Aufl. 2024`
- Beck-Online-Kommentare und Loseblatt: `70. Ed. (Stand 01.02.2025)`
Verwechslung führt zur Stilstörung.

**7. Sprachvariante**
Die Whitelist in `references/zitierweise.md` Abschnitt 13 nutzt die
**punktlose** Form (`iVm`, `iSv`). Wenn ein Dokument einheitlich die
gepunktete Form verwendet, kann diese stehen bleiben, sofern der Skill
es eindeutig erkennt; Mischformen werden vereinheitlicht.

**8. Palandt nicht automatisch in Grüneberg umbenennen**
Der Kommentar heißt seit der 81. Aufl. 2022 Grüneberg, davor Palandt.
Die automatische Ersetzung würde eine Altauflagen-Zitierung verfälschen.
Deshalb gilt der Hard-Stop aus Abschnitt 4a: Pflicht-Rückfrage, keine
stille Umbenennung.

## Quellenpflicht

Bei jeder Korrektur gibt der Skill als Begründung die einschlägige
**Abschnittsnummer der `references/zitierweise.md`** an. So bleibt für
die Nutzerin und den Nutzer nachvollziehbar, auf welche Stilregel sich
die Korrektur stützt.

---
*Dieser Skill ändert nur Form und Reihenfolge der Belege, nicht deren
materiellen Inhalt. Vor Veröffentlichung des Schriftsatzes ist der
korrigierte Text durch den verantwortlichen Bearbeiter selbständig
gegenzulesen.*
