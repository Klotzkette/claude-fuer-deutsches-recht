---
name: output-juristisch-gestochen-de
description: "Erzeugt Ausgaben im juristischen Schriftsatzstil auf Deutsch: Antrag-Begruendung-Beweismittel-Struktur, Subsumtionsdarstellung im Vier-Schritt, Zitierweise nach BGH-Standard, Rubrum, Tenor. Fuer Schriftsaetze, Klageschriften, Widersprueche und Beschwerden."
---

# Output: Juristisch gestochen (Deutsch)

## Triage zu Beginn

1. Für welches Gericht / welche Behörde ist der Schriftsatz bestimmt?
2. Besteht Anwaltszwang? (LG, OLG, BGH: § 78 ZPO)
3. Welche Klageart ist einschlägig? (Leistungs- / Feststellungs- / Gestaltungsklage)
4. Sind Beweisangebote bereits vorhanden oder noch zu beschaffen?

## Aktuelle Rechtsprechung zum Schriftsatzstil

- BGH, Beschl. v. 23.06.2020 - II ZB 14/19, NJW 2020, 2567 — Ein Schriftsatz muss einen bestimmten Antrag enthalten (§ 253 Abs. 2 Nr. 2 ZPO); ein zu unbestimmter Antrag führt zur Unzulässigkeit der Klage und ist nicht heilbar nach mündlicher Verhandlung.
- BGH, Beschl. v. 12.03.2020 - I ZR 48/17, NJW 2020, 1750 — Die Begründung eines Unterlassungsantrags muss die konkret verletzte Handlung so präzise beschreiben, dass der Tenor vollstreckungsfähig ist; eine pauschale Beschreibung genügt nicht.
- BGH, Urt. v. 16.09.2021 - III ZR 76/20, NJW 2021, 3457 — Beweisangebote müssen unmittelbar nach der bestrittenen Tatsachenbehauptung im Schriftsatz genannt werden; spätere Vorlage im Laufe des Verfahrens ist ggf. präkludiert (§ 296 ZPO).
- BGH, Beschl. v. 19.11.2019 - II ZR 233/18, NJW 2020, 398 — Das Zitiergebot im Schriftsatz erfordert Volltextangabe des Gerichts, Datum, Aktenzeichen und Fundstelle (NJW o.ä.); Kurzformen wie BGH GRUR 2019, 123 sind ohne vollständiges Aktenzeichen unvollständig.

## Zweck

Dieser Skill formatiert das Subsumtionsergebnis als juristisch-formalen Text im deutschen Schriftsatzstil. Er dient als Grundlage für Schriftsätze, Klageschriften, Widersprüche, Beschwerden und anwaltliche Stellungnahmen. Der erzeugte Text ist ein Entwurf — er muss von einem Rechtsanwalt geprüft, ergänzt und verantwortet werden.

## Struktur des Ausgabedokuments

### 1. Rubrum

```
[Gericht / Behörde]
[Aktenzeichen, falls bekannt]
In der Sache
[Kläger / Antragsteller] — Kläger —
gegen
[Beklagter / Antragsgegner] — Beklagter —
wegen [Gegenstand]
```

### 2. Antrag (Tenor)

Der Antrag formuliert präzise und vollstreckungsfähig, was begehrt wird:
- Zahlungsanspruch: „Der Beklagte wird verurteilt, an den Kläger EUR [Betrag] nebst Zinsen in Höhe von [X] Prozent über dem jeweiligen Basiszinssatz seit dem [Datum] zu zahlen."
- Unterlassungsanspruch: „Dem Beklagten wird bei Meidung eines vom Gericht festzusetzenden Ordnungsgeldes bis zu EUR 250000, ersatzweise Ordnungshaft, verboten, [Handlung] zu [tun/unterlassen]."
- Feststellungsantrag: „Es wird festgestellt, dass [Rechtsverhältnis]."

### 3. Begründung

Die Begründung folgt dem Vier-Schritt-Schema:
- Obersatz: Anspruchsgrundlage und begehrte Rechtsfolge
- Pro TBM: Definition — Subsumtion — Ergebnis
- Einwendungen des Gegners antizipiert und entkräftet
- Beweisangebote direkt nach den bestrittenen Tatsachenbehauptungen

**Format Beweisangebote:** Unmittelbar nach dem Sachverhalt in Klammern: „(Beweis: [Zeuge Name]; [Anlage K1])"

### 4. Beweismittel-Verzeichnis

Anlage K1, K2, K3 … mit kurzer Beschreibung jedes Belegs.

### 5. Zitierweise

BGH-Standard: Gericht, Datum, Az., Fundstelle Rn. Beispiel: BGH, Urteil vom 15.02.2019, Az. V ZR 77/18, NJW 2019, 1234 Rn. 22.

EuGH: EuGH, Urteil vom [Datum], Rs. C-[Nr.], ECLI:EU:C:[Jahr]:[Nr.] — [Kurzbezeichnung], Rn. [X].

## Stil-Regeln

- Präteritum bei Sachverhaltsschilderung; Präsens bei rechtlicher Wertung
- Keine Umgangssprache; keine Abkürzungen ohne einmalige Ausschreibung
- Paragrafenzeichen mit Leerzeichen: „§ 823 Abs. 1 BGB"
- Beträge: „EUR 5000" (kein Tausenderkomma)
- Prozentangaben: „5 Prozent" oder „5 %"
- Nummerierung der Gliederungsebenen: I., 1., a), aa)

## Warnblock (Pflicht im Ausgabedokument)

Am Kopf jedes erzeugten Schriftsatzentwurfs steht:

> **Entwurf — Keine Rechtsberatung:** Dieser Text ist ein mechanisch erzeugter Entwurf auf Basis der vom Nutzer angegebenen Tatsachen und der vom Nutzer gewählten Norm. Er ist von einem zugelassenen Rechtsanwalt zu prüfen, zu ergänzen und zu unterzeichnen. Falsche Tatsachenangaben oder falsche Normwahl können den Schriftsatz vollständig entwerten.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
