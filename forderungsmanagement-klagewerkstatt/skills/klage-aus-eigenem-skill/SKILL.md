---
name: klage-aus-eigenem-skill
description: "Für Klagewerkstatt — Laufzeit aus eigenem Skill: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik."
---

# Klagewerkstatt — Laufzeit aus eigenem Skill

## Triage — kläre vor dem Einsatz

1. Ist das hauseigene Klage-Plugin (`klagewerkstatt-<kanzlei>`) installiert — enthält es `assets/vorlagen-leer/standardklage.md` und `references/hausregeln.json`?
2. Sind Sachverhalt, Parteien, Forderungshöhe und Beklagtenanschrift vollständig bekannt?
3. Welche sachliche Zuständigkeit liegt vor: allgemeine Forderung bis einschließlich 10.000 EUR Amtsgericht, darüber Landgericht; Wohnraummietsache nach Paragraf 23 Nummer 2a GVG stets Amtsgericht?
4. Welche örtliche Zuständigkeit gilt (Paragrafen 12, 13 ZPO allgemein; Paragraf 29 ZPO Erfüllungsort; Paragraf 29c ZPO Verbraucherverträge)?
5. Soll zusätzlich ein Kurz-Memo im Gutachtenstil mit Prozessrisiken erstellt werden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

Paragraf 253 ZPO (Klageschrift) — Paragrafen 130, 130a, 130d ZPO (Schriftsatz, elektronisches Dokument, beA-Pflicht) — Paragraf 23 Nummer 1 GVG und Paragraf 71 Absatz 1 GVG (allgemeine Wertzuständigkeit) — Paragraf 23 Nummer 2a GVG (Wohnraummietsachen ausschließlich Amtsgericht) — Paragrafen 12, 13, 29, 29c, 38 ZPO (örtliche Zuständigkeit) — VO (EU) 1215/2012 (Brüssel Ia, internationale Zuständigkeit) — Paragrafen 286, 288, 280 BGB (Verzug, Verzugszinsen, Verzugsschaden) — RVG VV (Rechtsanwaltsvergütung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ist die Laufzeit-Variante. Er setzt voraus, dass das hauseigene Klage-Plugin bereits installiert ist. Er nimmt Sachverhalt und Beklagtenadresse entgegen, prüft online die Zuständigkeit, füllt die hauseigene Vorlage und liefert die Klageschrift als DOCX und Markdown.

## Ablauf

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

**Schritt 1 — Hausvorlage finden**

Prüfen, ob `klagewerkstatt-<slug>` installiert ist. Wenn nicht: auf `klagevorlage-aus-eigenen-mustern` verweisen.

**Schritt 2 — Sachverhalt einsammeln**

Parteien, Forderungsgrund, Betrag, Fälligkeit, Verzug, Beklagtenanschrift, Beweise, Anlagen.

**Schritt 3 — Zuständigkeit online prüfen (Pflicht)**

Sachlich: Paragraf 23 Nummer 1 und Nummer 2a GVG sowie Paragraf 71 Absatz 1 GVG. Wohnraummietsachen bleiben auch bei hohen Zahlungsrückständen beim Amtsgericht; Gewerberaummiete folgt der allgemeinen Wertzuständigkeit. Örtlich: Paragrafen 12, 13, 29, 29c, 38 ZPO. Online-Recherche unter `https://www.justizadressen.nrw.de/de/justiz/suche` und `https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php`. Quelle und Abrufdatum dokumentieren. BeA-SAFE-ID nachtragen.

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
| Variante B — Mandant will Vereinfachung Mahnverfahren statt Klage | Mahnbescheid Paragraf 688 ZPO als kostenguenstigere Alternative |
| Variante C — allgemeine Forderung bis einschließlich 10.000 EUR oder Wohnraummietsache | Amtsgericht zuständig; bei Wohnraummiete streitwertunabhängig nach Paragraf 23 Nummer 2a GVG; in erster Instanz kein Anwaltszwang, aber Prozessrisiko prüfen |

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
| Sachlich | Amtsgericht / Landgericht; bei Wohnraum Paragraf 23 Nummer 2a GVG, sonst Wertzuständigkeit nach Paragraf 23 Nummer 1 GVG und Paragraf 71 Absatz 1 GVG |
| Örtlich (Paragrafen 12/13/29/29c ZPO) | AG/LG [...] wegen [...] |
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

---
**Halluzinations-Audit 27.05.2026**

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
