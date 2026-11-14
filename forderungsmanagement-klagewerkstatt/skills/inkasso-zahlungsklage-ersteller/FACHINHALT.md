---
name: inkasso-zahlungsklage-ersteller
description: "Für Inkasso-Zahlungsklage-Ersteller: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik."
---

# Inkasso-Zahlungsklage-Ersteller

## Triage — kläre vor dem Einsatz

1. Liegt ein vollständiger Mahnvorlauf vor (Rechnung mit Fälligkeit, mindestens eine Mahnung mit Fristsetzung)?
2. Ist die Hauptforderung noch nicht vor Klageeinreichung vollständig bezahlt (Erfüllungskontrolle)?
3. Sind Schuldner-Anschrift und Verbraucher-/Unternehmereigenschaft geklärt (Gerichtsstand Paragraf 29c ZPO bei Verbrauchern)?
4. Welche Nebenforderungen (Mahnkosten, Verzugszinsen, Inkassokosten) sollen eingeklagt werden — sind sie belegt und verhältnismäßig?
5. Liegt eine Abtretungskette vor — ist die Aktivlegitimation des Gläubigers/Zessionars lückenlos dokumentiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

Paragraf 286 BGB (Verzugseintritt) — Paragraf 288 BGB (Verzugszinsen: +5 Pp. B2C, +9 Pp. B2B) — Paragraf 280 Absatz 2 BGB (Verzugsschaden) — Paragraf 249 BGB (Schadensersatz) — Paragraf 253 ZPO (Klageschrift) — Paragrafen 12, 13, 29, 29c ZPO (örtliche Zuständigkeit) — Paragraf 23 Nummer 1 GVG und Paragraf 71 Absatz 1 GVG (allgemeine Wertzuständigkeit ab 01.01.2026: Amtsgericht bis einschließlich 10.000 EUR, Landgericht darüber; Paragraf 47 EGZPO Übergangsvorschrift) — Paragraf 23 Nummer 2a GVG (Wohnraummietsachen ausschließlich Amtsgericht) — Paragraf 93 ZPO (sofortiges Anerkenntnis, Kostenfolge) — Paragraf 812 BGB (Bereicherungsrecht als Auffanganspruch)

## Basiszinssatz Paragraf 247 BGB

- Basiszinssatz seit 1. Juli 2026: 1,52 Prozent. Zinsläufe über den Stichtag in Perioden mit 1,27 beziehungsweise 1,52 Prozent Basiszins teilen. Amtliche Bundesbank-Tabelle: https://www.bundesbank.de/de/bundesbank/organisation/agb-und-regelungen/basiszinssatz-607820
- Daraus B2C-Verzugszinssatz (Paragraf 288 Abs. 1 BGB) 6,27 Prozent, B2B-Verzugszinssatz (Paragraf 288 Abs. 2 BGB) 10,27 Prozent. Halbjaehrliche Pruefung am 01.01. und 01.07. erforderlich.
- Verzugspauschale Paragraf 288 Abs. 5 BGB (B2B): 40 EUR pro Vorgang.

## Aenderungen Zustaendigkeitsrecht ab 01.01.2026

Gesetz zur Änderung des Zuständigkeitsstreitwerts der Amtsgerichte (BGBl. 2025 I Nr. 318 vom 11.12.2025) hebt mit Wirkung ab 01.01.2026 an:

- Sachliche Zuständigkeit Amtsgericht von 5.000 auf 10.000 EUR für allgemeine Forderungssachen nach Paragraf 23 Nummer 1 GVG. Wohnraummietsachen bleiben davon unabhängig nach Paragraf 23 Nummer 2a GVG ausschließlich beim Amtsgericht.
- Berufungssumme Paragraf 511 Abs. 2 ZPO von 600 auf 1.000 EUR.
- Wertgrenze Nichtzulassungsbeschwerde Paragraf 26 EGZPO von 20.000 auf 25.000 EUR.
- Uebergangsvorschrift Paragraf 47 EGZPO regelt Altverfahren.

Quelle: https://www.brak.de/newsroom/news/zivilgerichtsbarkeit-hoehere-wertgrenzen-fuer-zustaendigkeit-und-rechtsmittel-ab-112026/

## Rechtsprechung

- Rechtsprechung zu Verzug und Paragraf 286 BGB live ueber https://dejure.org und https://openjur.de pruefen.
- Aktenzeichen und Datum erst nach Verifikation in den Schriftsatz uebernehmen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill baut aus einer Forderungsakte einen sauberen Mahn- und Klageworkflow. **Eingeklagt werden nur Ansprüche, die klar, fällig, durchsetzbar und belegt sind.** Unsichere Positionen werden nicht eingeklagt, sondern als Rückfrage oder Nichtklage-Empfehlung ausgegeben.

## Sofortregeln

1. Nicht alles einklagen, was im Forderungskonto steht — jede Position braucht Anspruchsgrundlage, Betrag, Fälligkeit, Verzug, Beleg und Einwendungskontrolle.
2. Erfüllung blockt: vor Klageeinreichung bezahlte Hauptforderung darf nicht mehr eingeklagt werden.
3. Nebenforderungen sind kein Autopilot: Mahnkosten, Verzugszinsen, Inkassokosten werden einzeln geprüft.
4. Gerichtsort vor Klage: sachliche und örtliche Zuständigkeit sind zu prüfen und zu dokumentieren.
5. Mahnung vor Eskalation: wenn kein ausreichender Mahnvorlauf vorliegt, zuerst Mahnschreiben.

## Pflichtablauf


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1: Akte aufnehmen

Felder: Gläubiger, Schuldner (Verbraucher/Unternehmer), Forderungsgrund, Hauptforderung, Mahnvorlauf, Verzug, Nebenforderungen, Prozessgeschichte, Gerichtsort.

### Schritt 2: Mahnvorlauf prüfen

Mahnchronologie: Rechnung → Zahlungserinnerung → Mahnung(en) → letzte Mahnung mit Klagehinweis → Inkassoschreiben → Zahlungseingänge.

Ampelbeurteilung: grün (klar), gelb (unklar, nacharbeitbar), rot (rechtlich ungeeignet oder bereits erledigt).

### Schritt 3: Anspruchs-Gatekeeper

Prüfe je Position: Anspruchsgrundlage, Betrag, Fälligkeit, Durchsetzbarkeit, Verzug, Verschulden, Prozessrisiko, Gerichtsort.

- GRÜN → in den Klageantrag.
- GELB → Rückfrage oder Belegbedarf.
- ROT → nicht einklagen, Begründung angeben.

### Schritt 4: Gerichtsort finden

Sachlich: allgemeine Forderung bis einschließlich 10.000 EUR Amtsgericht nach Paragraf 23 Nummer 1 GVG, darüber Landgericht nach Paragraf 71 Absatz 1 GVG. Wohnraummietsachen bleiben nach Paragraf 23 Nummer 2a GVG streitwertunabhängig beim Amtsgericht. Örtlich: Paragrafen 12, 13, 29, 29c ZPO. Online-Abgleich über justiz.de oder justizadressen.nrw.de; Quelle und Abrufdatum dokumentieren.

### Schritt 5: Output bauen

1. Mahnchronologie als Tabelle.
2. Anspruchsmatrix mit Ampel.
3. Klagefreigabe (was wird eingeklagt, was nicht, warum).
4. Gerichtsortprüfung mit Quellenplatzhalter.
5. Klageentwurf nur für grüne Positionen.
6. Beleg- und Anlagenliste mit K-Sigeln.
7. Kosten-/Risiko-Hinweis zu Paragraf 93 ZPO.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zahlungsklage gegen saumigen Schuldner | Mahnverfahren oder Klageschrift nach Schema; Template unten |
| Variante A — Schuldner gibt Ratenzahlung an | Ratenvereinbarung statt Klage; Vollstreckungstitel danach |
| Variante B — Forderung wirtschaftlich zweifelhaft Insolvenz droht | Insolvenzantrag pruefen statt Klage; Klage nur wenn Masse erwartet |
| Variante C — Mandant will Geschaeftsbeziehung erhalten | Aussergerichtliche Einigung zuerst; Klage als letztes Mittel |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template

**Inkasso-Zahlungsklage — Anspruchsmatrix**

Schuldner: [...] | Forderungsstand: [...] EUR | Stand: [Datum]

| Position | Betrag EUR | Ampel | Begründung |
|---|---|---|---|
| Hauptforderung | [...] | GRÜN/ROT | [...] |
| Verzugszinsen | [...] | GRÜN/GELB | ab [...] |
| Mahnkosten | [...] | GRÜN/GELB | Beleg: [...] |
| Inkassokosten | [...] | GRÜN/GELB | Verhältnismäßigkeit: [...] |

**Gerichtsort:** AG/LG [...] — Online-Quelle: [...] — Abrufdatum: [...]

**Klageantrag (nur grüne Positionen):**
Der Beklagte wird verurteilt, an den Kläger [...] EUR nebst Zinsen in Höhe von [...] Prozentpunkten über dem Basiszinssatz seit [...] zu zahlen.

**Empfehlung:** [Klage einreichen / zuerst Mahnung / Positionen [...] nicht einklagen]

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->
