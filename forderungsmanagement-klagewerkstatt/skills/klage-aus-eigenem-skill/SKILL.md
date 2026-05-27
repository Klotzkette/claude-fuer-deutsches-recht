---
name: klage-aus-eigenem-skill
description: "Kanzlei hat hauseigenes Klage-Plugin (klagewerkstatt-kanzlei) installiert und will damit Klagen aus eigenem Sachverhalt erstellen. Laufzeit-Variante Klagewerkstatt. Pruefraster: Sachverhalt Beklagtenadresse Zustaendigkeit §§ 12 13 29 29c ZPO §§ 23 71 GVG. Output: fertige Klageschrift DOCX und Markdown. Abgrenzung zu klagevorlage-aus-eigenen-mustern (Lernlauf) und inkasso-zahlungsklage-ersteller (standalone)."
---

# Klagewerkstatt — Laufzeit aus eigenem Skill

## Triage — kläre vor dem Einsatz

1. Ist das hauseigene Klage-Plugin (`klagewerkstatt-<kanzlei>`) installiert — enthält es `assets/vorlagen-leer/standardklage.md` und `references/hausregeln.json`?
2. Sind Sachverhalt, Parteien, Forderungshöhe und Beklagtenanschrift vollständig bekannt?
3. Welche sachliche Zuständigkeit liegt vor (AG bis 10.000 EUR / LG darüber, §§ 23, 71 GVG)?
4. Welche örtliche Zuständigkeit gilt (§§ 12, 13 ZPO allgemein; § 29 ZPO Erfüllungsort; § 29c ZPO Verbraucherverträge)?
5. Soll zusätzlich ein Kurz-Memo im Gutachtenstil mit Prozessrisiken erstellt werden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

§ 253 ZPO (Klageschrift) — §§ 130, 130a, 130d ZPO (Schriftsatz, elektronisches Dokument, beA-Pflicht) — §§ 23, 71 GVG (sachliche Zuständigkeit) — §§ 12, 13, 29, 29c, 38 ZPO (örtliche Zuständigkeit) — VO (EU) 1215/2012 (Brüssel Ia, internationale Zuständigkeit) — §§ 286, 288, 280 BGB (Verzug, Verzugszinsen, Verzugsschaden) — RVG VV (Rechtsanwaltsvergütung)

## Rechtsprechung

BGH, Beschl. v. 20.04.2023 – III ZB 75/21, NJW 2023, 1743 — Klageschriften im beA-Verfahren müssen strukturiert als PDF/A übermittelt werden; Anlagen sind als gesonderte Dateien beizufügen und im Schriftsatz eindeutig zu bezeichnen.

BGH, Urt. v. 13.01.2021 – VIII ZR 66/20, NJW 2021, 765 — Der Gerichtsstand des Erfüllungsortes nach § 29 ZPO setzt voraus, dass der streitige Erfüllungsort der eingeklagten Leistungspflicht konkret feststeht; bei unklarem Erfüllungsort gilt der allgemeine Gerichtsstand (§§ 12, 13 ZPO).

BGH, Urt. v. 25.02.2016 – I ZR 136/14, NJW 2016, 2181 — § 29c ZPO schützt Verbraucher bei Haustürgeschäften und Fernabsatzverträgen; eine abweichende Gerichtsstandsvereinbarung (§ 38 ZPO) ist gegenüber Verbrauchern nur bei nachträglicher Vereinbarung nach Entstehung des Streitigkeitsverhältnisses wirksam.

BGH, Urt. v. 05.04.2017 – VIII ZR 179/16, NJW 2017, 1659 — Fehlt eine ladungsfähige Anschrift des Beklagten bei Klageerhebung, ist die Klage unzulässig; der Kläger trägt die Darlegungs- und Beweislast für die aktuelle Anschrift.

## Kommentarliteratur

Zöller, ZPO, 35. Aufl. 2024, §§ 12–29c Rn. 1–60 (Gerichtsstände, Verbraucherverträge, Gerichtsstandsvereinbarungen).
Thomas/Putzo, ZPO, 45. Aufl. 2024, § 253 Rn. 1–45 (Klageschrift, Antrag, Begründung).
Musielak/Voit, ZPO, 20. Aufl. 2023, §§ 130a, 130d Rn. 1–25 (beA, elektronisches Dokument).

## Zweck

Dieser Skill ist die Laufzeit-Variante. Er setzt voraus, dass das hauseigene Klage-Plugin bereits installiert ist. Er nimmt Sachverhalt und Beklagtenadresse entgegen, prüft online die Zuständigkeit, füllt die hauseigene Vorlage und liefert die Klageschrift als DOCX und Markdown.

## Ablauf


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

**Schritt 1 — Hausvorlage finden**

Prüfen, ob `klagewerkstatt-<slug>` installiert ist. Wenn nicht: auf `klagevorlage-aus-eigenen-mustern` verweisen.

**Schritt 2 — Sachverhalt einsammeln**

Parteien, Forderungsgrund, Betrag, Fälligkeit, Verzug, Beklagtenanschrift, Beweise, Anlagen.

**Schritt 3 — Zuständigkeit online prüfen (Pflicht)**

Sachlich: §§ 23, 71 GVG. Örtlich: §§ 12, 13, 29, 29c, 38 ZPO. Online-Recherche unter `https://www.justizadressen.nrw.de/de/justiz/suche` und `https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php`. Quelle und Abrufdatum dokumentieren. BeA-SAFE-ID nachtragen.

**Schritt 4 — Klage erzeugen**

Vorlage `assets/vorlagen-leer/standardklage.md` befüllen, DOCX über `office/docx` rendern. Anlagenliste ergänzen. Dateiname: `Klage-<Beklagte>-<YYYYMMDD>.docx`.

**Schritt 5 — Memo (nur auf Anfrage)**

Kurz-Memo im Gutachtenstil: Anspruchsgrundlagen, Beweislage, Prozessrisiken.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Klageschrift aus eigenem Skill-Output generieren | Klageschrift nach Skill-Output-Schema; Template unten |
| Variante A — Skill-Output unvollstaendig Luecken vorhanden | Luecken manuell fuellen; dann Template anwenden |
| Variante B — Mandant will Vereinfachung Mahnverfahren statt Klage | Mahnbescheid § 688 ZPO als kostenguenstigere Alternative |
| Variante C — Streitwert unter 5000 EUR Amtsgericht zustaendig | Vereinfachtes Verfahren AG; kein Anwaltszwang in Klageerhebung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template

**Klageschrift-Entwurf**

An das [Amtsgericht / Landgericht] [Ort]

Klage

des [Kläger], [Anschrift] — Kläger —

gegen

[Beklagter], [Anschrift] — Beklagter —

Streitwert: [...] EUR

**Zuständigkeitsprüfung:**
| Prüfpunkt | Ergebnis |
|---|---|
| Sachlich (§§ 23/71 GVG) | AG / LG wegen Streitwert [...] EUR |
| Örtlich (§§ 12/13/29/29c ZPO) | AG/LG [...] wegen [...] |
| Online-Quelle | [...] — Abrufdatum: [...] |
| BeA-SAFE-ID | [...] |

**Klageantrag:**
Der Beklagte wird verurteilt, an den Kläger [...] EUR nebst Zinsen in Höhe von [...] Prozentpunkten über dem Basiszinssatz seit [...] zu zahlen.

**Begründung:** [Sachverhalt nach ODUE-Schema: Obersatz — Definition — Untersatz — Ergebnis]

**Anlagenliste:**
- Anlage K 1: [...]
- Anlage K 2: [...]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

