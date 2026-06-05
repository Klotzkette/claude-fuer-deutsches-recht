---
name: textform-paragraph-verteidigungsstrategie
description: "Paragraph Verteidigungsstrategie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Paragraph Verteidigungsstrategie

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Paragraph Verteidigungsstrategie** im Plugin Schriftform/Textform BGB. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `textform-paragraph-126b-bgb-dauerhafter-datentraeger` | Prüffeld für textform paragraph 126b bgb dauerhafter datentraeger: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `verteidigungsstrategie-bei-formangriff` | Mandant wird von Vertragspartner mit Formmangel-Einwand konfrontiert und Anwalt muss Verteidigung aufbauen. Verteidigung Formverstoß §§ 125 242 BGB. Prüfraster: Heilungsmöglichkeiten nach Vollzug (§ 311b BGB) Nachholung der Form § 242 BGB Treuwidrigkeitseinwand (Berufung auf Formmangel wer selbst arglistig handelte) Beweislastverteilung. Output: Verteidigungsstrategie-Memo und Klausel-Aenderungsvorschlaege. Abgrenzung zu anspruchsformulierungen-bei-formverstoss (Angreifer-Seite) und form-checker-fuer-vertrag-oder-willenserklärung. |
| `wohnraummiete-kuendigung-paragraph-568-bgb` | Prüffeld für wohnraummiete kuendigung paragraph 568 bgb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Schriftform/Textform BGB gilt für **Paragraph Verteidigungsstrategie**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `textform-paragraph-126b-bgb-dauerhafter-datentraeger`

**Fokus:** Prüffeld für textform paragraph 126b bgb dauerhafter datentraeger: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Textform § 126b BGB — Dauerhafter Datenträger

## Rechtsgrundlagen

- **§ 126b BGB** — Textform: Erklärung in Textform muss
 - in einer lesbaren Schrift abgegeben sein
 - die Person des Erklärenden nennen
 - den Abschluss der Erklärung erkennbar machen (z. B. durch Wiedergabe des Namens oder Signatur)
 - auf einem dauerhaften Datenträger abgegeben oder zugegangen sein

- **§ 126b S. 2 BGB** — Dauerhafter Datenträger: Mittel, das es dem Empfänger ermöglicht, eine inhaltlich unveränderte Erklärung für einen angemessenen Zeitraum zu speichern und zu reproduzieren

- **Umsetzung EU-Recht**: Verbraucherrichtlinien fordern Textform vielfach als Mindeststandard (§ 356 BGB, §§ 481 ff. BGB, § 492 BGB).

## BGH-Linie

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Der BGH hat in der Leitentscheidung zum Maklervertrag § 656a BGB bestätigt:

> **Lehrsatz**: E-Mail-Austausch kann die Textform des § 126b BGB erfüllen. Dabei können Erklärungen auf getrennten Datenträgern (separate E-Mails) stehen — eine körperliche Einheit ist nicht erforderlich. Ein konkludenter Abschluss eines Maklervertrags ist möglich, wenn aus dem Gesamtkontext der E-Mails der Vertragsschluss-Wille hinreichend deutlich wird.

> **Kritischer Lehrsatz**: Bei Verstoß gegen die Textform des § 656a BGB ist nicht nur der Maklervertrag unwirksam — auch ein Bereicherungsanspruch auf Rückgewähr bereits gezahlter Provision ist nach dem Schutzzweck des § 656a BGB ausgeschlossen.

## Workflow

### Drei-Stufen-Prüfung Textform

**Stufe 1 — Dauerhafter Datenträger**

| Medium | Dauerhafter Datenträger? |
|--------|-------------------------|
| E-Mail (empfangen im Postfach) | Ja — empfängerseits speicherbar |
| WhatsApp-Nachricht | Ja — wenn nicht nur flüchtiger Chat |
| SMS | Ja — auf Empfänger-Gerät gespeichert |
| PDF als E-Mail-Anhang | Ja |
| Brief / Fax (Papier) | Ja |
| Gespräch per Telefon | Nein — flüchtig |
| Webseiten-Chatfenster ohne Speicherung | Zweifelhaft |
| Messenger-Nachrichten mit automatischem Ablaufdatum | Nein |

**Stufe 2 — Person des Erklärenden**

Die Erklärung muss den Erklärenden nennen. Es genügt die Absender-E-Mail-Adresse oder ein Vor- und Nachname in der Signatur. Anonyme Nachrichten ohne Zuordenbarkeit erfüllen Textform nicht.

**Stufe 3 — Abschluss der Erklärung erkennbar**

Der Erklärungsabschluss kann durch Wiedergabe des Namens am Ende, Grußformel mit Namen oder eine eindeutige Signatur kenntlich gemacht werden. Kein Formerfordernis für eigenhändige Unterschrift.

### Textform vs. Schriftform — Abgrenzungstabelle

| Merkmal | Textform § 126b BGB | Schriftform § 126 BGB |
|---------|--------------------|-----------------------|
| Eigenhändige Unterschrift | Nicht erforderlich | Erforderlich |
| Papierdokument | Nicht erforderlich | Erforderlich (Original) |
| E-Mail | Erfüllt Textform | Erfüllt Schriftform nicht |
| qES | Nicht erforderlich | Ersetzt Schriftform (§ 126a) |
| WhatsApp | Erfüllt Textform (bei Speicherbarkeit) | Nein |

## Templates

### Textform-konforme E-Mail für Maklervertrag (§ 656a BGB)

```
Betreff: Maklerauftrag Immobilie [Adresse] — Auftragsbestätigung

Sehr geehrte(r) Herr/Frau [Name],

hiermit beauftrage ich Sie, [Name des Maklers / der Maklerfirma],
als Immobilienmakler für den [Kauf / Verkauf / die Vermittlung] der
Immobilie [genaue Adresse].

Ich bin damit einverstanden, dass im Erfolgsfall eine Maklerprovision
in Höhe von [X %] des Kaufpreises zzgl. gesetzlicher Mehrwertsteuer
fällig wird.

Mit freundlichen Grüßen
[Vor- und Nachname]
[Datum]
```

### Textform-Bestätigung für Mieterhöhung (§ 558a BGB)

```
Betreff: Mieterhöhung gemäß § 558 BGB — [Wohnungsadresse]

Sehr geehrte(r) Herr/Frau [Name],

ich fordere Sie auf, ab dem [Datum] eine erhöhte Miete in Höhe
von [Betrag] Euro monatlich zu zahlen. Die bisherige Miete beträgt
[Betrag] Euro monatlich.

Begründung: [Vergleichswohnungen / Mietspiegel / Sachverständigengutachten]

[Vor- und Nachname]
[Datum]
```

## Fallstricke

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **WhatsApp-Sicherung**: WhatsApp-Nachrichten können als dauerhafter Datenträger dienen — aber: nach Verlust des Geräts oder Löschen der App sind Nachrichten ggf. nicht mehr reproduzierbar. Für Beweissicherung Screenshot anfertigen und in Akte nehmen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Querverweise

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- → `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift` (Abgrenzung)
- → `formerfordernisse-im-bgb-ueberblick`
- → `dokumentations-und-beweisarchitektur` (Sicherung WhatsApp/E-Mail)

<!-- AUDIT 27.05.2026 bundle_043
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

## 2. `verteidigungsstrategie-bei-formangriff`

**Fokus:** Mandant wird von Vertragspartner mit Formmangel-Einwand konfrontiert und Anwalt muss Verteidigung aufbauen. Verteidigung Formverstoß §§ 125 242 BGB. Prüfraster: Heilungsmöglichkeiten nach Vollzug (§ 311b BGB) Nachholung der Form § 242 BGB Treuwidrigkeitseinwand (Berufung auf Formmangel wer selbst arglistig handelte) Beweislastverteilung. Output: Verteidigungsstrategie-Memo und Klausel-Aenderungsvorschlaege. Abgrenzung zu anspruchsformulierungen-bei-formverstoss (Angreifer-Seite) und form-checker-fuer-vertrag-oder-willenserklärung.

# Verteidigungsstrategie bei Formangriff

## Rechtsgrundlagen

- **§ 125 BGB** — Nichtigkeit und Zweifelsregel bei Formmangel
- **§ 242 BGB** — Treu und Glauben: Einwand der Treuwidrigkeit gegen Formmangel-Berufung
- **§ 311b Abs. 1 S. 2 BGB** — Heilung Grundstückskauf
- **§ 766 S. 3 BGB** — Heilung Bürgschaft
- **§ 518 Abs. 2 BGB** — Heilung Schenkungsversprechen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## BGH-Linie

### § 242 BGB — Treuwidrigkeitseinwand

Die Berufung auf einen Formmangel kann nach ständiger BGH-Rechtsprechung treuwidrig (§ 242 BGB) sein. Die Hürden sind hoch — der BGH lässt den Treuwidrigkeitseinwand nur in Ausnahmefällen zu:

**Voraussetzungen (kumulativ, BGH-Dauerrechtsprechung)**:
- Die Partei, die sich auf den Formmangel beruft, hat den Formmangel selbst veranlasst oder von ihm gewusst
- Vollzug des Rechtsgeschäfts oder schützenswertes Vertrauen der Gegenpartei
- Die Berufung auf den Formmangel führt zu einem Ergebnis, das für die andere Partei schlechthin unerträglich oder existenzbedrohend wäre
- Reine Spekulationsabsicht der Formmangel-Partei

**BGH-Formel**: Treuwidrigkeitseinwand ist ausnahmsweise zulässig, wenn die Berufung auf den Formmangel im konkreten Einzelfall mit Grundsätzen von Treu und Glauben unvereinbar wäre — etwa wenn die Partei, die sich auf den Formmangel beruft, diesen bewusst herbeigeführt hat und nun aus eigenem Fehlverhalten Nutzen zieht.

### Heilung — Überblick

| Rechtsgeschäft | Heilungsnorm | Voraussetzung |
|---------------|-------------|--------------|
| Grundstückskauf § 311b BGB | § 311b Abs. 1 S. 2 BGB | Auflassung + Eintragung im Grundbuch |
| Bürgschaft § 766 BGB | § 766 S. 3 BGB | Bürge erfüllt Hauptschuld |
| Schenkungsversprechen § 518 BGB | § 518 Abs. 2 BGB | Leistung des Versprochenen |
| Arbeitsvertrag § 14 Abs. 4 TzBfG | Keine gesetzliche Heilung | — |
| Maklervertrag § 656a BGB | Keine gesetzliche Heilung | — |
| Kündigung § 568 BGB | Keine Heilung; Neuerklärung erforderlich | — |

### Nachholung der Form

Wenn keine gesetzliche Heilungsnorm existiert, können die Parteien das Rechtsgeschäft durch eine formwirksame Neuerklärung oder Bestätigung nachträglich wirksam machen. Die Neuerklärung muss alle Formerfordernisse der ursprünglichen Erklärung erfüllen.

**Achtung**: Rückwirkung der Neuerklärung auf den ursprünglichen Zeitpunkt ist bei formgebundenen Rechtsgeschäften grundsätzlich nicht möglich — die Willenserklärung wirkt erst ab der formwirksamen Neuerklärung.

## Workflow

### Verteidigungsstrategie — Prüfschema

```
SCHRITT 1: Liegt tatsächlich ein Formmangel vor?
 → Welche Form war vorgeschrieben? (Gesetzliche oder gewillkürte Form?)
 → Wurde die Form eingehalten? (Unterschrift? qES? Textform?)
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

SCHRITT 2: Ist Heilung möglich?
 → § 311b Abs. 1 S. 2 BGB (Grundstück): Auflassung + Eintragung?
 → § 766 S. 3 BGB (Bürgschaft): Hauptschuld erfüllt?
 → § 518 Abs. 2 BGB (Schenkung): Leistung vollzogen?
 → Sonstige gesetzliche Heilungsnorm?

SCHRITT 3: Nachholung der Form möglich?
 → Neuerklärung in der gesetzlich vorgeschriebenen Form
 → Sind alle Voraussetzungen für eine wirksame Neuerklärung erfüllbar?
 → Frist: Liegt noch Zeit für formwirksame Neuerklärung vor Verjährung / Fristablauf?

SCHRITT 4: § 242 BGB — Treuwidrigkeitseinwand?
 → Hat die andere Partei den Formmangel selbst veranlasst?
 → Liegt schützenswertes Vertrauen oder Vollzug vor?
 → Ist die Berufung auf den Formmangel schlechthin unerträglich?
 → Ist Spekulationsabsicht der anderen Partei erkennbar?

SCHRITT 5: Beweislast
 → Wer behauptet den Formmangel?
 → Wer trägt die Beweislast für die Formwahrung?
 → Welche Beweismittel stehen zur Verfügung?
```

### Einwand gegen Räumungsklage nach formwidriger Kündigung

```
Formwidrigkeitseinwand (Mieter):

Die Kündigung vom [Datum] wahrte nicht die Schriftform des § 568 Abs. 1 BGB.
[Begründung: keine eigenhändige Unterschrift / kein zugegangenes qES-Dokument]

Die Kündigung ist daher gemäß § 125 S. 1 BGB unwirksam. Das Mietverhältnis
besteht fort. Der Räumungsantrag ist unbegründet.
```

### § 174 BGB Zurückweisung (sofort nach Erhalt)

```
Sehr geehrte Damen und Herren,

wir weisen die durch Herrn Rechtsanwalt [Name] in Ihrem Namen erklärte
Kündigung vom [Datum] unverzüglich zurück, da uns keine Vollmachtsurkunde
im Original vorgelegt wurde (§ 174 S. 1 BGB).

Die Kündigung gilt daher als nicht zugegangen. Wir behalten uns vor,
die Unwirksamkeit im Rechtsstreit geltend zu machen.

[Unterschrift]
```

## Templates

### Argumentationsrahmen § 242 BGB Treuwidrigkeitseinwand

```
§ 242 BGB — Treuwidrigkeitseinwand gegen Berufung auf Formmangel

I. Die Gegenpartei hat den Formmangel selbst veranlasst:
 [Sachverhaltsdarstellung: Wer hat warum die Schriftform nicht eingehalten?]

II. Schützenswertes Vertrauen / Vollzug:
 [Darstellung: Partei hat auf Wirksamkeit des Vertrags vertraut, Leistungen erbracht]

III. Unzumutbarkeit der Formmangel-Berufung:
 [Darstellung: welche konkreten Nachteile entstehen bei Nichtigkeitserklärung?]

IV. Kein Schutzzweck der Formnorm verletzt:
 [Prüfung: Schutzzweck der verletzten Formnorm — verlangt der Schutzzweck hier
 wirklich Nichtigkeit oder schützt § 242 BGB die schutzwürdigere Partei?]

Ergebnis: Die Berufung auf den Formmangel ist im konkreten Fall nach
§ 242 BGB ausgeschlossen.
```

## Fallstricke

- **Hohe Hürden § 242 BGB**: Der BGH lässt den Treuwidrigkeitseinwand nur in engen Grenzen zu. Wer lediglich argumentiert, es sei "unfair", sich auf den Formmangel zu berufen, wird damit regelmäßig scheitern.
- **Heilung ≠ Rückwirkung**: Selbst wenn Heilung möglich ist (z. B. § 766 S. 3 BGB), wirkt sie nicht auf den ursprünglichen Zeitpunkt zurück — Zwischenzeiträume (z. B. Zinslauf) bleiben ggf. unberührt.
- **§ 174 BGB Unverzüglichkeit**: Wer nicht unverzüglich (d. h. ohne schuldhaftes Zögern, in der Regel binnen einer Woche) zurückweist, verliert das Recht zur Zurückweisung wegen fehlender Vollmacht — die Kündigung gilt dann als wirksam erklärt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Querverweise

- → `anspruchsformulierungen-bei-formverstoss`
- → `formerfordernisse-im-bgb-ueberblick`
- → `gewerberaummiete-paragraph-550-bgb-langzeitform` (§ 242 BGB bei § 550 BGB)
- → `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt`

<!-- AUDIT 27.05.2026 bundle_043
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Maßnahme: Keine Änderung am Skill-Text erforderlich. AZ und Inhalt bestätigt.
Quelle: https://www.otto-schmidt.de/blog/zivil-und-zivilverfahrensrecht-blog/montagsblog-neues-vom-bgh-ZRBLOG0004000.html
-->

## 3. `wohnraummiete-kuendigung-paragraph-568-bgb`

**Fokus:** Prüffeld für wohnraummiete kuendigung paragraph 568 bgb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Wohnraummiete-Kündigung — § 568 BGB und Formfragen

## Rechtsgrundlagen

- **§ 568 Abs. 1 BGB** — Kündigung des Wohnraummietverhältnisses: Schriftform erforderlich
- **§ 573 BGB** — Ordentliche Kündigung durch Vermieter: berechtigtes Interesse
- **§ 573c BGB** — Kündigungsfristen
- **§ 569 BGB** — Außerordentliche fristlose Kündigung: Begründungspflicht
- **§ 126 Abs. 3 BGB** i.V.m. **§ 126a BGB** — Ersatz der Schriftform durch qES
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 130 BGB** — Zugang der Willenserklärung

## BGH-Linie

### Schriftformerfordernis § 568 Abs. 1 BGB

Die Kündigung des Wohnraummietverhältnisses bedarf gemäß § 568 Abs. 1 BGB zwingend der Schriftform. Die Schriftform kann nach § 126 Abs. 3 BGB durch die elektronische Form (qES, § 126a BGB) ersetzt werden. Ein ausdrücklicher gesetzlicher Ausschluss der qES-Möglichkeit besteht im Mietrecht — anders als z. B. in § 623 BGB (Arbeitsrecht) — nicht.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Der BGH hat entschieden, dass eine formwirksame qES-Kündigung dem Mieter so zugehen muss, dass er die Signatur selbst prüfen kann. Das qES-Dokument muss elektronisch beim Mieter eingehen. Ein Ausdruck durch das Gericht mit Transfervermerk (§ 298 Abs. 3 ZPO) ersetzt diesen Zugang nicht.

### Begründungspflicht

**Ordentliche Kündigung durch Vermieter** (§ 573 BGB): Berechtigtes Interesse erforderlich (Eigenbedarf, Vertragspflichtverletzung, wirtschaftliche Verwertung). Begründung muss in der Kündigung selbst enthalten sein — Nachschieben von Gründen nur eingeschränkt möglich.

**Außerordentliche fristlose Kündigung** (§ 569 BGB): Wichtiger Grund (z. B. erheblicher Mietrückstand, § 543 Abs. 2 Nr. 3 BGB). Keine gesetzliche Begründungspflicht in der Kündigung selbst, aber Begründung empfehlenswert.

**Kündigung durch Mieter**: Schriftform erforderlich (§ 568 Abs. 1 BGB), aber keine Begründungspflicht für ordentliche Kündigung.

## Workflow

### Checkliste Kündigung Wohnraummiete (Vermieter)

```
□ Berechtigtes Interesse vorhanden? (§ 573 BGB)
 → Eigenbedarf? Pflichtverletzung? Wirtschaftliche Verwertung?

□ Kündigungsfrist berechnet? (§ 573c BGB)
 → bis 5 Jahre Mietdauer: 3 Monate
 → bis 8 Jahre: 6 Monate
 → über 8 Jahre: 9 Monate

□ Formwahl:
 Option A (empfohlen): Papierkündigung mit eigenhändiger Unterschrift
 → Bote mit Übergabequittung oder Einschreiben/Rückschein

 Option B (zulässig, aber risikobehaftet): qES-Kündigung per E-Mail
 → PDF mit qES als Anhang an Mieter
 → Eingangsbestätigung anfordern
 → Sendebericht sichern
 → Hinweis in E-Mail: rechtliches Dokument mit qES

□ Begründung in der Kündigung enthalten? (§ 573 Abs. 3 BGB)

□ Zugang des Mieters sichergestellt?
 → Boten-Quittung / Einschreiben-Rückschein / Empfangsbestätigung
```

### Kündigung durch Mieter — Checkliste

```
□ Schriftform gewahrt (§ 568 Abs. 1 BGB)?
 → Eigenhändige Unterschrift auf Papier?
 → Oder qES-Dokument digital an Vermieter zugegangen?

□ Kündigungsfrist: 3 Monate zum Monatsende (§ 573c Abs. 1 S. 1 BGB)
 → Zugang der Kündigung bis spätestens dritten Werktag des Monats?
 → Wenn später: Kündigung wirkt erst zum übernächsten Monatsende

□ Zugang beim Vermieter sichergestellt?
 → Boten-Übergabe gegen Quittung oder Einwurf mit Attest
```

### Risikomatrix Formwahl

| Methode | Formwirksamkeit | Zugangssicherheit | Empfehlung |
|---------|----------------|-------------------|------------|
| Papier + Originalunterschrift + Bote | Sicher | Hoch | Beste Wahl |
| Papier + Einschreiben/Rückschein | Sicher | Mittel (Inhalt nicht bewiesen) | Gut |
| qES per E-Mail + Empfangsbestätigung | Zulässig (VIII ZR 159/23) | Mittel | Möglich |
| qES per E-Mail ohne Bestätigung | Zulässig, Zugang str. | Gering | Risikobehaftet |
| E-Mail ohne qES | Formunwirksam | - | Nicht verwenden |
| WhatsApp ohne qES | Formunwirksam | - | Nicht verwenden |

## Templates

### Muster-Kündigung Vermieter (ordentlich, Papierform)

```
[Briefkopf Vermieter]

[Ort], [Datum]

Herrn/Frau [Name Mieter]
[Adresse Mieter]

Kündigung des Mietverhältnisses über die Wohnung [Adresse]

Sehr geehrte(r) Herr/Frau [Name],

hiermit kündige ich das Mietverhältnis über die oben genannte Wohnung
ordentlich gemäß § 573 BGB zum [Datum, Berechnung: Zugang + Kündigungsfrist].

Berechtigtes Interesse (§ 573 Abs. 2 Nr. ... BGB):
[Eigenbedarf / Pflichtverletzung / wirtschaftliche Verwertung: Begründung]

Ich bitte Sie, die Wohnung bis zu diesem Termin vollständig geräumt
und besenrein in dem vertragsgemäßen Zustand zurückzugeben.

Mit freundlichen Grüßen

[Eigenhändige Unterschrift Vermieter]

[Vor- und Nachname in Druckbuchstaben]
```

### Hinweis-E-Mail bei qES-Kündigung (Vermieter)

```
Betreff: Wichtiges rechtliches Dokument — Kündigung Mietverhältnis [Adresse]

Sehr geehrte(r) Herr/Frau [Name],

anbei übersende ich Ihnen die Kündigung des Mietverhältnisses über
die Wohnung [Adresse] als PDF-Datei.

Das Dokument ist mit einer qualifizierten elektronischen Signatur (qES)
nach § 126a BGB versehen, welche die gesetzliche Schriftform des
§ 568 Abs. 1 BGB ersetzt.

Bitte bestätigen Sie den Empfang dieser E-Mail und die Öffnung der
angehängten Datei per Antwort-E-Mail. Die Signatur können Sie mit
Adobe Acrobat Reader oder unter validator.bund.de prüfen.

Mit freundlichen Grüßen
[Name Vermieter]
```

## Fallstricke

- **E-Mail ohne qES**: Eine bloße E-Mail des Vermieters mit dem Kündigungstext erfüllt nicht die Schriftform des § 568 Abs. 1 BGB. Nur qES ersetzt die Schriftform — einfache oder fortgeschrittene Signatur reichen nicht.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Fehlende Begründung**: Fehlt die Begründung bei ordentlicher Kündigung durch den Vermieter, ist die Kündigung formell unwirksam (§ 573 Abs. 3 S. 1 BGB). Nachschieben von Gründen ist eingeschränkt.
- **Teilkündigung**: Bei Wohnraummiete grundsätzlich unzulässig.

## Querverweise

- → `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23`
- → `mandantenwarnung-qes-per-email-whatsapp-und-zugang`
- → `elektronische-form-paragraph-126a-bgb-qes`
- → `prozessablauf-papier-vs-elektronisch`
- → `anspruchsformulierungen-bei-formverstoss` (Räumungsklage)
