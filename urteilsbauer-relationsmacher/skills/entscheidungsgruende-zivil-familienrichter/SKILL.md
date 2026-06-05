---
name: entscheidungsgruende-zivil-familienrichter
description: "Entscheidungsgruende Zivil Familienrichter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Entscheidungsgruende Zivil Familienrichter

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Entscheidungsgruende Zivil Familienrichter** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `entscheidungsgruende-zivil-schreiben` | Entscheidungsgründe eines Zivilurteils im Urteilsstil schreiben: Richter hat Beweise erhoben und muss Begründung formulieren. Normen: § 313 Abs. 3 ZPO (Entscheidungsgründe), § 286 ZPO. Prüfraster: Urteilsstil (kein Gutachtenstil), Obersatz, Anspruchsgrundlage, Subsumtion, Beweiswürdigung, Einwendungen, Verjährung, Nebenentscheidungen. Output Entscheidungsgründe-Entwurf im korrekten Urteilsstil. Abgrenzung: Tatbestand siehe tatbestand-zivil-schreiben; Tenor siehe tenor-bauen-zivil; Relation (Vorstufe) siehe relation-zivil. |
| `familienrichter-spezifika` | FamFG-Spezifika für Familienrichter anwenden: Richter am Familiengericht muss Beschluss statt Urteil abfassen. Normen: § 38 FamFG (Beschluss), § 137 FamFG (Verbund- und Folgesachen), § 1697a BGB (Kindeswohlprüfung), FamFG §§ 58 ff. (Beschwerde), VersAusglG. Prüfraster: Verbundpflicht, Versorgungsausgleich von Amts wegen, Rechtsmittelbelehrung FamFG, Sorgerechtsbeschluesse. Output FamFG-Beschluss-Entwurf, Verbund-Checkliste. Abgrenzung: Familienrecht materiell siehe fachanwalt-familienrecht-Plugin; ZPO-Beschluesse siehe beschluss-bauen-zpo. |
| `incoterms-und-gefahruebergang` | Incoterms-Klausel und Gefahruebergang in internationalem Kaufvertrag prüfen: Streit über Transportschaden oder Lieferpflicht. Normen: Incoterms 2020 (FOB, CIF, EXW, DAP, DDP), CISG Art. 31 und 67 ff. (Gefahruebergang). Prüfraster: Einschlaegige Incoterms-Klausel, Lieferort, Gefahruebergang-Zeitpunkt, Versicherungspflicht, Zoll, Verhaltnis zu CISG. Output Rechtsgutachten-Entwurf zu Gefahruebergang, Anspruchsschema. Abgrenzung: CISG Anwendbarkeit siehe cisg-prüfen; IPR siehe internationales-privatrecht. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Entscheidungsgruende Zivil Familienrichter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `entscheidungsgruende-zivil-schreiben`

**Fokus:** Entscheidungsgründe eines Zivilurteils im Urteilsstil schreiben: Richter hat Beweise erhoben und muss Begründung formulieren. Normen: § 313 Abs. 3 ZPO (Entscheidungsgründe), § 286 ZPO. Prüfraster: Urteilsstil (kein Gutachtenstil), Obersatz, Anspruchsgrundlage, Subsumtion, Beweiswürdigung, Einwendungen, Verjährung, Nebenentscheidungen. Output Entscheidungsgründe-Entwurf im korrekten Urteilsstil. Abgrenzung: Tatbestand siehe tatbestand-zivil-schreiben; Tenor siehe tenor-bauen-zivil; Relation (Vorstufe) siehe relation-zivil.

# Entscheidungsgründe schreiben

Im Urteilsstil (nicht im Gutachtenstil). Reihenfolge: Ergebnis - Begründung.

## Triage zu Beginn

1. Im Urteilsstil oder Gutachtenstil? (Antwort: immer Urteilsstil — Ergebnis vor Begründung.)
2. Welche Anspruchsgrundlagen sind durchgreifend — welche nicht?
3. Muss Beweiswürdigung integriert oder separat abgehandelt werden?
4. Welche Nebenentscheidungen (Zinsen, Kosten, Vollstreckbarkeit) fehlen noch?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 313 Abs. 3 ZPO — Entscheidungsgründe: kurze Zusammenfassung der Erwägungen
- § 286 ZPO — Beweiswürdigung
- § 286 BGB — Verzugszinsen (ab Mahnung oder Fälligkeit)
- § 288 BGB — gesetzlicher Verzugszinssatz (5 Prozentpunkte über Basiszinssatz)
- § 291 BGB — Rechtshängigkeitszinsen (ab Klageerhebung)
- § 91, 92 ZPO — Kosten
- § 708, 709 ZPO — vorläufige Vollstreckbarkeit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Obersatz:** "Die Klage ist [zulässig und] begründet / [zulässig, aber] unbegründet / teilweise begründet."
2. **Zulässigkeit** (kurz, nur problematische Punkte ausführen):
 - Rechtsweg, Zuständigkeit, Partei- und Prozessfähigkeit, Rechtsschutzbedürfnis.
3. **Begründetheit** — für jede Anspruchsgrundlage:
 - AG benennen → Tatbestandsmerkmale subsumieren → Ergebnis.
 - Einwendungen/Einreden des Beklagten prüfen.
 - Verjährung prüfen.
4. **Beweiswürdigung** einfügen (§ 286 ZPO), soweit Tatsachen streitig waren.
5. **Nebenentscheidungen formulieren:**
 - Zinsen (§ 286, 288, 291 BGB), Kosten (§ 91, 92 ZPO), Vollstreckbarkeit (§ 708, 709 ZPO).

## Output-Template

**Adressat:** Urteil → Entscheidungsgründe — Tonfall: sachlich-juristisch, Urteilsstil

```
## Entscheidungsgründe

Die Klage ist zulässig und begründet.

**I. Zulässigkeit**
Das Amtsgericht [ORT] ist sachlich (§ 23 Nr. 1 GVG, Streitwert [BETRAG] EUR) und örtlich
(§ 29 ZPO, Erfüllungsort [ORT]) zuständig. [Weitere Punkte nur wenn problematisch.]

**II. Begründetheit**

**1. Anspruch aus § [AG] BGB**
Der Kläger hat einen Anspruch auf [RECHTSFOLGE] gegen den Beklagten aus § [AG] BGB.
[TATBESTANDSMERKMALE subsumieren]

**2. Zinsen**
Der Zinsanspruch ergibt sich aus § 288 Abs. 1 BGB (5 Prozentpunkte über dem Basiszinssatz)
ab [DATUM DER MAHNUNG / Rechtshängigkeit].

**3. Kosten**
Die Kostenentscheidung beruht auf § 91 ZPO.

**4. Vorläufige Vollstreckbarkeit**
Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 709 ZPO.
```

## Aufbau

1. **Obersatz**: "Die Klage ist zulaessig, aber nur teilweise begründet."
2. **Zulässigkeit**: kurz; nur die problematischen Punkte ausführlich.
3. **Begründetheit** - pro Anspruchsgrundlage:
 - Anspruchsgrundlage benennen
 - Tatbestandsmerkmale subsumieren
 - Rechtsfolge
 - Einwendungen / Einreden
 - Verjaehrung
 - Bei mehreren Anspruchsgrundlagen: nur die durchgreifende ausführen oder Anspruchskonkurrenzen knapp behandeln
4. **Beweiswürdigung** (separater Abschnitt vor der konkreten Subsumtion oder integriert)
5. **Nebenentscheidungen**:
 - Zinsen Paragraf 286 BGB, Paragraf 288 BGB, Paragraf 291 BGB
 - Kosten Paragraf 91 ff ZPO
 - Vorläufige Vollstreckbarkeit Paragraf 708 ff ZPO
 - Streitwertbeschluss separat oder im Tenor
 - Berufungszulassung Paragraf 511 Abs. 4 ZPO

## Urteilsstil vs Gutachtenstil

- Gutachtenstil: "Es koennte ein Anspruch aus ... bestehen. Dies setzt voraus, dass ..."
- **Urteilsstil**: "Der Kläger hat einen Anspruch aus ... in Höhe von ... Der Beklagte ist Verkaeufer im Sinne ..."

## Stil

Praesens, Indikativ, im Aktiv, kurze Sätze, eine Sache pro Satz.

## 2. `familienrichter-spezifika`

**Fokus:** FamFG-Spezifika für Familienrichter anwenden: Richter am Familiengericht muss Beschluss statt Urteil abfassen. Normen: § 38 FamFG (Beschluss), § 137 FamFG (Verbund- und Folgesachen), § 1697a BGB (Kindeswohlprüfung), FamFG §§ 58 ff. (Beschwerde), VersAusglG. Prüfraster: Verbundpflicht, Versorgungsausgleich von Amts wegen, Rechtsmittelbelehrung FamFG, Sorgerechtsbeschluesse. Output FamFG-Beschluss-Entwurf, Verbund-Checkliste. Abgrenzung: Familienrecht materiell siehe fachanwalt-familienrecht-Plugin; ZPO-Beschluesse siehe beschluss-bauen-zpo.

# Familienrichter Spezifika

Familiensachen folgen FamFG statt ZPO (mit Verweisen auf ZPO).

## Triage zu Beginn

1. Handelt es sich um eine Familiensache (§ 111 FamFG) — welche Kategorie (Ehe, Unterhalt, Sorge, Umgang)?
2. Ist die Scheidungssache mit Folgesachen zu verbinden (§ 137 FamFG — Verbundpflicht)?
3. Sind Kinder betroffen — Verfahrensbeistand (§ 158 FamFG) bestellt?
4. Ist Versorgungsausgleich zu prüfen (§§ 1 ff. VersAusglG)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 38 FamFG — Beschluss als Entscheidungsform (kein Urteil)
- § 111 FamFG — Familiensachen (Katalog)
- § 137 FamFG — Verbund; Folgesachen zwingend mit Scheidung
- § 158, 159 FamFG — Verfahrensbeistand, Kindesanhörung
- § 1697a BGB — Kindeswohlprinzip
- §§ 1 ff. VersAusglG — Versorgungsausgleich
- §§ 58 ff. FamFG — Rechtsmittel (Beschwerde, Frist 1 Monat)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Verfahrenskategorie bestimmen:** Welche Familiensache (§ 111 FamFG)?
2. **Verbund prüfen:** Liegt Scheidung vor? Welche Folgesachen sind zwingend verbunden?
3. **Anhörungen durchführen/prüfen:** Kinder ab 3 Jahren (§ 159 FamFG), Eltern, Jugendamt, Verfahrensbeistand.
4. **Kindeswohl-Maßstab (§ 1697a BGB):** Bei Sorge und Umgang ausdrücklich abwägen.
5. **Beschluss formulieren (§ 38 FamFG):** Kein "Im Namen des Volkes", kein Urteil.
6. **Rechtsmittelbelehrung FamFG:** Beschwerde §§ 58 ff. FamFG, Frist 1 Monat (Eilfälle 14 Tage).

## Output-Template

**Adressat:** Familiengericht → Beschluss — Tonfall: sachlich-formal

```
## Beschluss

In der Familiensache [AKTENZEICHEN]
betreffend [Sorge/Umgang/Unterhalt] für das Kind [NAME], geb. [DATUM],

hat das Amtsgericht [ORT] — Familiengericht — am [DATUM] beschlossen:

1. [REGELUNG SORGE / UMGANG / UNTERHALT]
2. Die Kosten des Verfahrens trägt [PARTEI].
3. Der Verfahrenswert wird auf [BETRAG] EUR festgesetzt.

Gründe:
[KINDESWOHLPRÜFUNG, ABWÄGUNG, ANHÖRUNGSERGEBNIS]

Rechtsmittelbelehrung:
Gegen diesen Beschluss ist die Beschwerde nach § 58 FamFG statthaft. Die Beschwerde ist
binnen einer Frist von einem Monat nach Bekanntgabe beim [GERICHT] einzulegen.
```

## Wichtigste Unterschiede

- **Beschluss** statt Urteil (Paragraf 38 FamFG)
- **Anhörung** zwingend in vielen Verfahren (Kinder ab 14 Jahren, Eltern, Pflegepersonen)
- **Verbundverfahren** Paragraf 137 FamFG bei Scheidung: Folgesachen werden zwingend mitverhandelt
- **Versorgungsausgleich** ist Folgesache, wird im Verbund entschieden
- **Verfahrensbeistand** Paragraf 158 FamFG (insbesondere in Kindersachen)
- **Verfahrenskostenhilfe** Paragraf 76 ff FamFG (entspricht PKH der ZPO)

## Massstab Kindeswohl

Paragraf 1697a BGB - Kindeswohl ist Leitlinie aller familiengerichtlichen Entscheidungen.

## Rechtsmittelbelehrung FamFG

Beschwerde nach Paragraf 58 ff FamFG, Frist 1 Monat (in Eilfällen 14 Tage), beim erlassenden Gericht oder beim Beschwerdegericht (OLG).

## Form

- "Im Namen des Volkes" entfaellt
- Stattdessen: "Beschluss"
- Tenor wie beim Urteil, aber mit den familiengerichtlichen Spezifika (z. B. Sorgerechtsregelung, Umgangsregelung)

## 3. `incoterms-und-gefahruebergang`

**Fokus:** Incoterms-Klausel und Gefahruebergang in internationalem Kaufvertrag prüfen: Streit über Transportschaden oder Lieferpflicht. Normen: Incoterms 2020 (FOB, CIF, EXW, DAP, DDP), CISG Art. 31 und 67 ff. (Gefahruebergang). Prüfraster: Einschlaegige Incoterms-Klausel, Lieferort, Gefahruebergang-Zeitpunkt, Versicherungspflicht, Zoll, Verhaltnis zu CISG. Output Rechtsgutachten-Entwurf zu Gefahruebergang, Anspruchsschema. Abgrenzung: CISG Anwendbarkeit siehe cisg-prüfen; IPR siehe internationales-privatrecht.

# Incoterms und Gefahrübergang

Die Incoterms (International Commercial Terms) der Internationalen Handelskammer (ICC) regeln Lieferort, Gefahrübergang, Kostenverteilung und Versicherungspflichten.


## Triage zu Beginn

1. Welche Incoterms-Klausel wurde vereinbart — Fassung 2020, 2010 oder älter?
2. Welcher Lieferort ist im Vertrag benannt (Ort muss bei DAP, DDP, FCA genau angegeben sein)?
3. Wurde die Klausel wirksam einbezogen (AGB-Recht, Einbeziehungsvereinbarung)?
4. Hat ein Gefahrübergang stattgefunden — wann und wo?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- Art. 31 CISG — Lieferpflicht (Lieferort ohne Vereinbarung)
- Art. 67 CISG — Gefahrübergang bei Versendungskauf
- Art. 68 CISG — Gefahrübergang bei auf dem Transport verkaufter Ware
- § 269 BGB — Leistungsort
- § 346 HGB — Handelsgebräuche
- § 305 ff. BGB — AGB-Einbeziehung (bei B2C-Geschäften)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Klausel identifizieren:** Welche Klausel, welche Fassung? Im Vertrag oder AGB?
2. **Wirksame Einbeziehung prüfen:** B2B: Handelsbrauch (§ 346 HGB) oder vertragliche Vereinbarung; B2C: strenge Einbeziehungsvoraussetzungen (§ 305 Abs. 2 BGB).
3. **Gefahrübergang bestimmen:** Wann und wo ist Gefahr übergegangen? (Klauselspezifisch.)
4. **Schadensort nach Gefahrübergang:** Wer trägt den Verlust/die Beschädigung?
5. **Verhältnis zu CISG:** Incoterms konkretisieren Art. 31, 67 CISG — keine eigenständige Rechtsquelle, sondern Vertragsklausel.

## Output-Template

**Adressat:** Entscheidungsgründe — Tonfall: sachlich-juristisch

```
## Incoterms / Gefahrübergang

Die Parteien haben die Klausel [KLAUSEL, z.B. FOB Hamburg, Incoterms 2020] vereinbart.

**Einbeziehung:** Die Klausel wurde wirksam einbezogen durch [Vertragstext / Handelsbrauch § 346 HGB].

**Gefahrübergang:** Die Gefahr ist auf den Käufer übergegangen am [DATUM] mit [Verladung im Hafen
Hamburg / Bereitstellung im Werk / Übergabe an Frachtführer in ...].

**Folge:** Der [Schaden / Verlust] am [DATUM] nach Gefahrübergang liegt im Risikobereich des Käufers.
```

## Aktuelle Fassung

Incoterms 2020 (gilt ab 1. Januar 2020). Aeltere Fassungen sind weiterhin in Verträgen anzutreffen, deshalb immer die Fassung in der Klausel beachten.

## Wichtige Klauseln

- **EXW** (Ex Works) - Gefahr und Kosten gehen mit der Bereitstellung im Lager des Verkaeufers über.
- **FCA** (Free Carrier) - Verkaeufer übergibt an Frachtführer am benannten Ort.
- **FOB** (Free on Board) - Seetransport. Gefahr- und Kostenübergang mit Verladung auf das Schiff im Verschiffungshafen. Verkaeufer traegt bis zur Verladung, Kaeufer ab Verladung. Versicherung Pflicht des Kaeufers.
- **CIF** (Cost Insurance Freight) - Verkaeufer schließt Versicherung ab, traegt Fracht bis Bestimmungshafen, Gefahr geht aber bereits mit Verladung über.
- **DAP** (Delivered at Place) - Verkaeufer traegt bis zum Ankunftsort.
- **DDP** (Delivered Duty Paid) - Verkaeufer traegt alles bis zum Bestimmungsort einschließlich Zoll.

## Verhältnis zu CISG

Incoterms sind keine gesetzliche Regelung, sondern Vertragsklausel. Sie konkretisieren Artikel 31 CISG (Lieferort) und Artikel 67 ff CISG (Gefahrübergang). Im Streitfall:

1. Erst prüfen, ob Incoterms wirksam einbezogen sind (AGB-Prüfung).
2. Dann Auslegung der Klausel nach der jeweiligen Incoterms-Fassung.
3. Lückenfueller: CISG / nationales Recht.

## Tatbestand

Im Tatbestand die Klausel wörtlich oder als Bezugnahme angeben, im Entscheidungsgrund subsumieren.
