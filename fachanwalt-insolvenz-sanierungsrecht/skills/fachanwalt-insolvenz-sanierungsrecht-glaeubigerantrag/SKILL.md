---
name: fachanwalt-insolvenz-sanierungsrecht-glaeubigerantrag
description: "Workflow-Skill zu fachanwalt insolvenz sanierungsrecht glaeubigerantrag. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

## Mandantenfragen beim Kaltstart

1. Wie hoch ist die Forderung des Mandanten gegen die Schuldnerin – liegt Fälligkeit und Vollstreckbarkeit vor?
2. Wurden alle außergerichtlichen Maßnahmen ausgeschöpft (Mahnung, Mahnbescheid, Vollstreckung)?
3. Liegen Indizien für Zahlungsunfähigkeit i.S.d. § 17 InsO vor (Zahlungsstockungen, Rücklastschriften, offene Vollstreckungen, Brancheninsider-Informationen)?
4. Handelt es sich um eine juristische Person – dann auch Überschuldung § 19 InsO möglich?
5. Besteht ein Eigeninteresse über die Forderungsbeitreibung hinaus (z.B. Hauptgläubiger, Sicherungsinteressen)?
6. Sollen sofortige Sicherungsmaßnahmen (§ 21 InsO: vorläufiger Insolvenzverwalter, Zustimmungsvorbehalt, ZV-Einstellung) beantragt werden?
7. Ist das Rechtsschutzbedürfnis gegeben – liegt keine bloße Druckausübung vor?
8. Sind Verfahrenskosten gedeckt: kann der Mandant ggf. gemäß § 26 Abs. 1 InsO Kostenvorschuss leisten?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 14 InsO | Gläubigerantrag: Glaubhaftmachung Forderung und Eröffnungsgrund; Rechtsschutzbedürfnis |
| § 14 Abs. 2 InsO | Anhörung der Schuldnerin vor Eröffnungsbeschluss |
| § 17 InsO | Zahlungsunfähigkeit: Schuldner kann fällige Zahlungspflichten nicht erfüllen; 10%-Schwelle BGH |
| § 18 InsO | Drohende Zahlungsunfähigkeit: nur Eigenantrag, nicht für Gläubigerantrag |
| § 19 InsO | Überschuldung: nur bei juristischen Personen; negatives Reinvermögen + fehlende Fortführungsprognose |
| § 21 InsO | Sicherungsmaßnahmen: vorläufiger IV, allgemeines Verfügungsverbot, Zustimmungsvorbehalt, ZV-Einstellung |
| § 22 InsO | Aufgaben und Befugnisse des vorläufigen Insolvenzverwalters |
| § 26 InsO | Abweisung mangels Masse: wenn keine kostendeckenden Mittel vorhanden; Kostenvorschuss durch Gläubiger |
| § 27 InsO | Eröffnungsbeschluss: Datum, Stunde, Verwalterbestellung |
| § 294 ZPO | Glaubhaftmachung: eidesstattliche Versicherung, Urkunden |

## Leitentscheidungen

| Gericht | AZ | Datum | Kernaussage |
|---------|----|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Antragsberechtigung: jeder Insolvenzgläubiger; Forderung gegen Schuldner | § 14 Abs. 1 InsO | Fehlt Gläubigerstellung → Antrag unzulässig |
| 2 | Glaubhaftmachung Forderung: Titel, Urkunden, eidesstattliche Versicherung | § 14 Abs. 1, § 294 ZPO | Ohne Glaubhaftmachung → Antrag unzulässig |
| 3 | Glaubhaftmachung Eröffnungsgrund | §§ 17, 19 InsO | ZU oder Überschuldung (nur jur. Person); drohende ZU nicht ausreichend für Gläubigerantrag |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 3b | Überschuldung § 19: nur jur. Person; neg. Reinvermögen + fehlende Fortführungsprognose | § 19 InsO | Beide Voraussetzungen kumulativ |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 5 | Anhörung der Schuldnerin § 14 Abs. 2 | § 14 Abs. 2 InsO | Pflicht des Gerichts; keine Voraussetzung des Gläubigers |
| 6 | Sicherungsmaßnahmen § 21 InsO beantragen | § 21 InsO | Sofortschutz: ZV-Einstellung, vorläufiger IV, Zustimmungsvorbehalt |
| 7 | Massekostenprüfung § 26 InsO | § 26 InsO | Masseunzulänglichkeit → Abweisung; Kostenvorschuss durch Gläubiger möglich |
| 8 | Eröffnungsbeschluss § 27 InsO | § 27 InsO | Verwalterbestellung, Insolvenzbeschlag § 80 InsO |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Glaeeubigerantrag auf Insolvenzeroffnung stellen | Vollstaendiger Antrag § 14 InsO nach Baustein unten |
| Variante A — Schuldnerin stellt Gegenantrag | Widerspruchs-Baustein unten; Zahlungsunfaehigkeit belegen |
| Variante B — Mandant will schnell Geld sehen | Vorlaeufige Insolvenzverwaltung beantragen; Aussondern pruefen |
| Variante C — laufende Zwangsvollstreckung parallel | Koordination Insolvenzeröffnung und ZV; Moratoriumswirkung § 21 InsO |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Vollständiger Gläubigerantrag § 14 InsO

```
An das Amtsgericht [Ort] – Insolvenzgericht –

Antrag auf Eröffnung des Insolvenzverfahrens gemäß § 14 InsO

Antragstellerin (Gläubigerin):
[Firma GmbH], [Anschrift], vertreten durch Geschäftsführer [Name]
– nachfolgend: Gläubigerin –

Schuldnerin:
[Firma UG/GmbH/AG], [Anschrift], HR-Nr. [XX], AG [Ort]
– nachfolgend: Schuldnerin –

I. Antrag
Die Gläubigerin beantragt, das Insolvenzverfahren über das Vermögen der Schuldnerin
zu eröffnen.

Hilfsweise: Für den Fall mangelnder Masse beantragt die Gläubigerin, einen Kosten-
vorschuss gemäß § 26 Abs. 1 Satz 2 InsO in Höhe von [Betrag] EUR einzahlen zu dürfen,
um das Verfahren zu ermöglichen.

II. Glaubhaftmachung der Forderung (§ 14 Abs. 1 InsO)
Die Gläubigerin hat gegen die Schuldnerin eine Forderung in Höhe von [Betrag] EUR aus
[Warenlieferung/Darlehen/Dienstleistung] gemäß [Vertragsdatum], fällig seit [Datum].

Belege: Rechnung Anlage K1, Mahnschreiben Anlage K2, Zahlungsbefehl/Urteil Anlage K3.
Die Forderung ist trotz mehrfacher Mahnung (zuletzt [Datum]) nicht beglichen worden.

III. Glaubhaftmachung des Eröffnungsgrundes (§ 17 InsO)
Die Schuldnerin ist zahlungsunfähig (§ 17 InsO). Maßstab BGH-Linie zur Liquiditätsbilanz und Zahlungseinstellung (vor Antrag konkrete Aktenzeichen über dejure.org / openjur.de mit Datum verifizieren). Konkrete Indizien:
a) Liquiditätsstatus zum Stichtag: Unterdeckung > 10 % (vgl. ständige BGH-Linie);
b) Rücklastschriften der Schuldnerin vom [Datum], Anlage K4;
c) Vollstreckungsversuche anderer Gläubiger (Pfändungsprotokolle Anlage K5);
d) Eigene eidesstattliche Versicherung der Gläubigerin über Zahlungsverweigerung, Anlage K6.

[Bei jur. Person alternativ § 19 InsO:]
Die Schuldnerin ist überschuldet (§ 19 InsO): Der letzte Jahresabschluss [Jahr] weist ein
negatives Eigenkapital von [Betrag] EUR aus. Eine positive Fortführungsprognose ist nach
[Sachverhalt] nicht gegeben.

IV. Sicherungsmaßnahmen (§ 21 InsO)
Es wird beantragt:
a) Bestellung eines vorläufigen Insolvenzverwalters;
b) Anordnung eines allgemeinen Verfügungsverbots gemäß § 21 Abs. 2 Nr. 2 InsO;
c) Einstellung aller laufenden Zwangsvollstreckungsmaßnahmen gemäß § 21 Abs. 2 Nr. 3 InsO.

Begründung: Es besteht Gefahr der Vermögensverschiebung: [konkrete Hinweise].

V. Rechtsschutzbedürfnis
Der Antrag dient nicht der Druckausübung, sondern der geordneten Befriedigung sämtlicher
Gläubiger. Außergerichtliche Einigung ist an [Datum] gescheitert.

[Ort, Datum]
[Anwalt/Gläubiger]

Anlagen: K1–K6
```

### Widerspruchsschreiben Schuldnerin gegen Gläubigerantrag

```
An das Amtsgericht [Ort] – Insolvenzgericht –, Az. [XX IN YY/ZZ]

Stellungnahme der Schuldnerin gemäß § 14 Abs. 2 InsO

I. Die Schuldnerin widerspricht dem Antrag.

II. Keine Zahlungsunfähigkeit
Die behauptete Zahlungsstockung beruht auf einer [streitigen Gegenforderung/
Zahlungsausstand Dritter]. Aktuelle Liquidität: [Kontoauszüge Anlage S1].
Liquiditätslücke <10% (Nachweis Anlage S2).

III. Forderung bestritten
Die Forderung der Antragstellerin ist wegen [Sachmangel/Aufrechnung] nicht fällig.
Beweis: Anlage S3.

IV. Antrag auf Zurückweisung
Das Gericht möge den Eröffnungsantrag zurückweisen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast

| Frage | Beweislast |
|-------|-----------|
| Gläubigerstellung + Forderungshöhe | Gläubigerin: Glaubhaftmachung § 294 ZPO (kein Vollbeweis nötig) |
| Zahlungsunfähigkeit § 17 InsO | Gläubigerin: Indiziennachweis; Schuldnerin kann durch Liquiditätsplan widerlegen |
| Überschuldung § 19 InsO | Gläubigerin: Jahresabschluss, Gutachten; Schuldnerin: positive Fortführungsprognose |
| Rechtsschutzbedürfnis | Gläubigerin muss positiv darlegen; Schuldnerin kann Missbrauch geltend machen |
| Massekostendeckung § 26 InsO | Gericht prüft von Amts wegen; Gläubigerin kann Kostenvorschuss anbieten |

## Fristen

| Verfahrensschritt | Frist |
|-------------------|-------|
| Antragstellung | Jederzeit; keine Vorfrist; aber: Gläubiger trägt Kosten bei Abweisung § 26 InsO |
| Anhörung Schuldnerin § 14 Abs. 2 InsO | Gericht setzt Frist (i.d.R. 1–2 Wochen) |
| Sicherungsmaßnahmen § 21 InsO | Sofort nach Antragstellung möglich (ohne Anhörung in Eilfällen) |
| Eröffnungsbeschluss § 27 InsO | Nach Anhörung; Gericht soll unverzüglich entscheiden |
| Anfechtungsfristen nach Eröffnung | Ab Eröffnung läuft Verjährung für Verwalter |
| Kostenvorschuss § 26 InsO | Gericht setzt angemessene Frist zur Einzahlung |
| Beschwerde gegen Abweisung § 34 InsO | 2 Wochen ab Zustellung |

## Gegenargumente und Reaktion

| Gegenargument | Rechtliche Grundlage | Reaktion Gläubiger |
|---------------|---------------------|--------------------|
| Zahlungsunfähigkeit liege nicht vor | § 17 InsO | Liquiditätsstatus zum Stichtag konkret darstellen; Indizien iSd ständiger BGH-Linie zur Zahlungseinstellung |
| Forderung bestritten (Gegenforderung) | § 14 Abs. 1 InsO | Bestreitung muss substanziiert sein; bei Titulierung Gläubigerforderung unbestreitbar |
| Stundung bestreitend Forderung fällig | BGH-Linie zur echten Stundung | Beweis konkret echter Stundungsvereinbarung; faktische Duldung beseitigt Fälligkeit nicht (Verifikation Az. über dejure.org) |
| Masselosigkeit § 26 InsO | § 26 InsO | Kostenvorschuss anbieten; Forderung aus Masseverbindlichkeit nach § 55 InsO bei Eröffnung sichergestellt |
| Überschuldung bestritten (positive Fortführungsprognose) | § 19 InsO | Gegengutachten anfordern; Bankgespräche und Finanzierungszusagen als Belege; Prognosezeitraum 12 Monate (SanInsKG endete 31.12.2023) |
| Schuldnerin leitet außergerichtliche Sanierung ein | §§ 17 ff. InsO | Keine automatische Rücknahme des Antrags; Gläubiger kann Verfahren fortsetzen; Vergleich verhandeln |

## Streitwert und Kosten

Verfahrenskosten bei Gläubigerantrag: Gerichtsgebühren nach GKG Anlage 1 Nr. 2310 (Insolvenzeröffnungsverfahren); bei Abweisung trägt der Gläubiger die Kosten (§ 26 InsO, § 91 ZPO analog).

Kostenvorschuss § 26 InsO: typisch 3.000–15.000 EUR; deckt vorläufigen Verwalter + Gerichtskosten. Bei späterer Eröffnung wird Vorschuss erstattet (Masseverbindlichkeit).

Anwaltliche Vergütung: Gebühr nach RVG; Beratungsgebühr 190–8.500 EUR je nach Streitwert (§§ 13, 14 RVG); bei Gerichtsverfahren 1,3 Verfahrensgebühr + 1,2 Terminsgebühr.

Haftungsrisiko: Gläubiger, der mutwillig oder leichtfertig Antrag stellt, haftet nach § 14 Abs. 3 InsO für Schaden der Schuldnerin.

## Strategische Empfehlung

| Situation | Empfehlung |
|-----------|-----------|
| Forderung tituliert, Vollstreckung erfolglos | Gläubigerantrag stellen; Indizien für ZU aus Vollstreckungsprotokollen |
| Mehrere Gläubiger haben gleichartige Situation | Koordination mit anderen Gläubigern vor Antragstellung; Lead-Gläubiger festlegen |
| Schuldnerin bietet kurzfristige Zahlung | Vergleich mit Zahlungsplan prüfen; § 14-Antrag als Druckmittel wirksam |
| Schuldnerin versucht § 270b-Schutzschirm | Gläubigerantrag ist weiter zulässig; Schutzschirm schließt Gläubigerantrag nicht aus |
| Masselosigkeit befürchtet | Kostenvorschuss § 26 InsO anbieten; sichert Verfahrensdurchführung + Anfechtungsrecht des Verwalters |
| Gesellschafter der Schuldnerin haften persönlich (GbR, OHG) | Simultane Pfändung Gesellschaftervermögen erwägen |
| Staatsanwaltschaft ermittelt wegen Insolvenzverschleppung | Gläubigerantrag unabhängig von Strafverfahren; ggf. koordinieren |

## Anschluss-Skills

- `fachanwalt-insolvenz-sanierungsrecht-insolvenzanfechtung` — nach Eröffnung: Anfechtung von Vorauszahlungen
- `fachanwalt-insolvenz-sanierungsrecht-anfechtungsklage-verwalter` — Verwalter-Klagestrategie
- `fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan` — Alternative StaRUG-Verfahren vor Antragstellung
- `fachanwalt-handels-gesellschaftsrecht-geschaeftsfuehrerhaftung` — GF-Haftung § 15a InsO parallel prüfen

## Quellen

- InsO §§ 14, 17, 18, 19, 21, 22, 26, 27
- BGH-Linie zur Zahlungsunfähigkeit (Liquiditätsbilanz, 10 %-Schwelle, Zahlungseinstellung): konkrete Aktenzeichen vor Ausgabe über dejure.org / openjur.de mit Datum verifizieren.
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers (für Antragsbegründung bei Wechsel der Geschäftsleitung).
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle.
