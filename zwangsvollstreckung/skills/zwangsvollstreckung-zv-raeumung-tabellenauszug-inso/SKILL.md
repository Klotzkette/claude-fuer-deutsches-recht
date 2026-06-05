---
name: zwangsvollstreckung-zv-raeumung-tabellenauszug-inso
description: "ZV Raeumung Tabellenauszug Inso: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZV Raeumung Tabellenauszug Inso

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZV Raeumung Tabellenauszug Inso** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zv-raeumung-885` | Vermieter hat Räumungsurteil und will Wohnung oder Gewerberaum räumen lassen. § 885 ZPO Räumungsvollstreckung. Prüfraster: Räumungstitel Klausel Zustellung Mitbewohner Kinder Untermieter Drittwiderspruch § 771 Vollstreckungsschutz § 765a ZPO Berliner Modell § 885a ZPO beschraenkter Räumungsauftrag. Output: Räumungsauftrag an GV und Strategie-Memo. Abgrenzung zu zv-abwehr-schuldner (Schuldnerseite) und zv-mobiliar-gv-auftrag (Mobiliar). |
| `zv-tabellenauszug-201-inso` | Gläubiger hat Insolvenzforderung die im Verfahren festgestellt wurde und will nach Insolvenzende vollstrecken. § 201 Abs. 2 InsO Tabellenauszug als Titel. Prüfraster: Voraussetzungen festgestellt nicht bestritten kein RSB-Versagungsgrund Klausel und Zustellung 30-Jahres-Verjährung § 197 BGB Schranken Restschuldbefreiung § 301 InsO. Output: Vollstreckungsantrag aus Tabellenauszug. Abgrenzung zu zv-titel-klausel-zustellung (klassischer Titel) und zv-kommandocenter. |
| `zv-vermoegensauskunft-gv` | Gläubiger weiss nichts über Vermögen des Schuldners und will Auskunft erzwingen. § 802c ZPO Vermogensauskunft EV. Prüfraster: Antrag beim GV Sperrfrist 2 Jahre § 802d ZPO Eintragung Schuldnerverzeichnis § 882b ZPO Erzwingungshaft § 802g ZPO. Output: Auftrag Vermogensauskunft GV und Auswertungsprotokoll Vermogensverzeichnis. Abgrenzung zu zv-kontensuche-drittschuldner (Drittauskunfte) und zv-mobiliar-gv-auftrag (Pfaendung nach Ermittlung). |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZV Raeumung Tabellenauszug Inso**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zv-raeumung-885`

**Fokus:** Vermieter hat Räumungsurteil und will Wohnung oder Gewerberaum räumen lassen. § 885 ZPO Räumungsvollstreckung. Prüfraster: Räumungstitel Klausel Zustellung Mitbewohner Kinder Untermieter Drittwiderspruch § 771 Vollstreckungsschutz § 765a ZPO Berliner Modell § 885a ZPO beschraenkter Räumungsauftrag. Output: Räumungsauftrag an GV und Strategie-Memo. Abgrenzung zu zv-abwehr-schuldner (Schuldnerseite) und zv-mobiliar-gv-auftrag (Mobiliar).

# Räumung § 885 ZPO / Berliner Räumung § 885a ZPO

## Aufgabe

Wohn- oder Gewerberäume vom Schuldner herausverlangen. Hier kollidieren Eigentumsschutz und sozialer Schutz – Skill achtet ausdrücklich auf Mitbewohner und Härtefallschutz.

## Startet bei

- Räumungstitel (Urteil, gerichtlicher Vergleich) vorhanden
- Schuldner verweigert freiwillige Herausgabe
- Räumungsfrist § 721 ZPO abgelaufen

## Rechtsgrundlagen

- § 885 ZPO – klassische Räumung
- § 885a ZPO – beschränkter Räumungsauftrag (Berliner Modell)
- § 721 ZPO – Räumungsfrist im Urteil
- § 794a ZPO – Räumungsfrist bei Vergleich
- § 765a ZPO – Vollstreckungsschutz
- § 771 ZPO – Drittwiderspruchsklage
- § 750 Abs. 2 ZPO – Zustellung
- § 750 Abs. 3 ZPO – nur an im Titel benannte Schuldner
- § 562 BGB – Vermieterpfandrecht

## Workflow

1. **Drei-Säulen-Prüfung** plus Räumungsfrist abgelaufen.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Räumungsauftrag** an GV mit klarer Bezeichnung Räumungsobjekt (Adresse, Lage im Haus).
4. **Räumungsart wählen**:
 - **§ 885 ZPO klassisch**: GV räumt das Objekt, schuldnerische Habe wird entfernt, eingelagert, verwertet (umfangreiche Lager- und Vorschusskosten).
 - Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **Termin** beim GV anberaumen; Vorschuss leisten; Eröffnungswerkzeug (Schlüsseldienst) bestellen.
6. **Wohnungsöffnung**: Schloss durch Schlüsseldienst öffnen, neue Schließanlage installieren.
7. **Schuldnerhabe**:
 - § 885: einlagern (vier Wochen Aufbewahrungspflicht), dann verwerten.
 - § 885a: Vermieterpfandrecht greift sofort; Gläubiger muss Schuldner aber Gelegenheit geben, Sachen abzuholen.
8. **Vollstreckungsschutz** § 765a ZPO: Härtefall (Erkrankung, Suizidgefahr, Geburtshochphase) → einstweilige Einstellung möglich.

## Berliner Räumung § 885a ZPO

- Seit 2013 ausdrücklich gesetzlich geregelt.
- Gläubiger ist Vermieter mit Pfandrecht § 562 BGB.
- Auftrag explizit beschränkt: "nur Herausgabe der Räume, keine Wegschaffung der Sachen".
- Reduziert Kosten erheblich; trotzdem GV-Auftrag erforderlich.
- Verwertung des Pfandgutes über pfandweisen Verkauf, Versteigerung oder freihändig.

## Mitbewohner und Dritte

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Untermieter**: braucht eigenen Titel.
- **Minderjährige Kinder**: durch Titel gegen sorgeberechtigten Elternteil erfasst.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
RÄUMUNG [Mandant] gegen [Schuldner], GV [Bezirk]

Titel: [Räumungsurteil / Vergleich]
Räumungsfrist: abgelaufen am DD.MM.JJJJ
Objekt: [Adresse, Lage, Räume]
Titel-Schuldner: [Personen aufzählen]
Weitere Bewohner: [eigene Titel? ja/nein]
Räumungsart: [§ 885 klassisch / § 885a Berlin]
Pfandrecht § 562 BGB: [ja – Vermieter / nein]
Erwartete Kosten: EUR x

NÄCHSTER SCHRITT: Termin GV
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals räumen gegen Personen, die nicht im Titel stehen.
- Niemals § 885 klassisch wählen, wenn § 885a vermietertauglich und günstiger ist.
- Niemals Härtefall ignorieren (§ 765a ZPO Antrag möglich).
- Bei minderjährigen Kindern: Jugendamt-Beteiligung mitdenken.
- Schlüsseldienst, Vorschuss, Versicherung der Habe sicherstellen.

## Querverweise

- `zv-titel-klausel-zustellung`
- `zv-mobiliar-gv-auftrag` – ähnliche GV-Mechanik
- `zv-abwehr-schuldner`
- `zv-elektronische-zustellung-2027`

## 2. `zv-tabellenauszug-201-inso`

**Fokus:** Gläubiger hat Insolvenzforderung die im Verfahren festgestellt wurde und will nach Insolvenzende vollstrecken. § 201 Abs. 2 InsO Tabellenauszug als Titel. Prüfraster: Voraussetzungen festgestellt nicht bestritten kein RSB-Versagungsgrund Klausel und Zustellung 30-Jahres-Verjährung § 197 BGB Schranken Restschuldbefreiung § 301 InsO. Output: Vollstreckungsantrag aus Tabellenauszug. Abgrenzung zu zv-titel-klausel-zustellung (klassischer Titel) und zv-kommandocenter.

# Vollstreckung aus Tabellenauszug § 201 InsO

## Aufgabe

Der vollstreckbare Tabellenauszug ist ein eigener Titel (§ 201 Abs. 2 Satz 1 InsO). Dieser Skill prüft, ob aus ihm vollstreckt werden darf, und steuert die nächste Pfändung.

## Startet bei

- Insolvenzverfahren ist aufgehoben (§ 200 InsO) oder eingestellt (§§ 207, 211 InsO)
- Forderung wurde zur Tabelle festgestellt und vom Schuldner nicht (wirksam) bestritten
- Restschuldbefreiung nicht erteilt oder Forderung von ihr ausgenommen (§ 302 InsO)

## Rechtsgrundlagen

- § 201 InsO – Rechte der Insolvenzgläubiger nach Verfahrensaufhebung
- § 178 Abs. 3 InsO – Wirkung der Feststellung
- § 197 Abs. 1 Nr. 5 BGB – 30 Jahre Verjährung
- § 301 InsO – Wirkung der Restschuldbefreiung
- § 302 InsO – Ausnahmen (Deliktsforderung, Unterhalt, hinterzogene Steuern)
- §§ 727, 750 ZPO – Klausel und Zustellung
- § 794 Abs. 1 Nr. 1 ZPO i.V.m. § 201 InsO – Titelqualität

## Workflow

1. **Tabellenauszug prüfen**: Ist die Forderung mit dem Vermerk "festgestellt" eingetragen, nicht "bestritten"? Bestreitet der Insolvenzverwalter, aber nicht der Schuldner – Titel gegen Schuldner trotzdem entstanden.
2. **Verfahrensstand**: Verfahren aufgehoben/eingestellt? Vollstreckung erst danach zulässig (§ 89 InsO greift bis dahin).
3. **Restschuldbefreiung**:
 - **Nicht erteilt** (versagt oder Verfahren nach IK-Plan): freie Vollstreckung.
 - **Erteilt**: § 301 InsO – Vollstreckung grundsätzlich gesperrt; **Ausnahmen § 302 InsO** (vorsätzliche unerlaubte Handlung mit Eintrag in der Tabelle, Unterhaltsrückstände aus pflichtwidriger Verletzung, hinterzogene Steuern).
 - **Wohlverhaltensphase**: Vollstreckung gegen den pfändbaren Teil des Schuldnereinkommens nur eingeschränkt zulässig.
4. **Klausel** beim Insolvenzgericht (§ 201 Abs. 2 Satz 2 InsO, § 727 ZPO) bzw. wenn Insolvenzgericht das Verfahren geführt hat – aus der vollstreckbaren Ausfertigung.
5. **Zustellung** an Schuldner § 750 ZPO.
6. **Pfändung** durchziehen über `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt` oder `zv-mobiliar-gv-auftrag`.
7. **Verjährung** beachten: 30 Jahre ab Eintragung (§ 197 Abs. 1 Nr. 5 BGB) – Zinsen separat (§ 197 Abs. 2 BGB drei Jahre regelmäßig, aber bei rechtskräftig festgestellten Zinsen 30 Jahre für ab Feststellung entstandene, drei Jahre für nach Feststellung entstehende künftige Zinsen).

## Schranken der Restschuldbefreiung

§ 302 InsO listet die nicht erfassten Forderungen:

1. Deliktische Forderungen aus vorsätzlich unerlaubter Handlung – **Eintragung mit Vermerk "aus vorsätzlich begangener unerlaubter Handlung"** ist Voraussetzung.
2. Geldstrafen, Geldbußen, Ordnungs- und Zwangsgelder.
3. Hinterzogene Steuern, sofern Verurteilung.
4. Pflichtwidrige Unterhaltsforderungen.
5. Zinslose Darlehen für die Verfahrenskosten.

Nur diese Forderungen lassen sich nach Restschuldbefreiung weiterhin vollstrecken – Skill prüft das ausdrücklich.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
TABELLENAUSZUG § 201 InsO [Mandant] gegen [Schuldner]

InsO-Verfahren: AG [Ort] Az [IN/IK ...]
Aufhebung/Einstellung: am DD.MM.JJJJ
Forderung Tabelle: lfd Nr x, EUR y, "festgestellt"
Bestritten von: [niemand / Insolvenzverwalter / Schuldner]
Restschuldbefreiung: [nicht erteilt / erteilt / versagt / verfahrensgegenstand]
§ 302-Privileg: [nein / Deliktsforderung mit Eintrag / Unterhalt / ...]
Verjährung: 30 Jahre ab Feststellung, ab DD.MM.JJJJ
Klausel: [vorhanden / beim AG Insolvenzgericht beantragen]
Zustellung § 750: [erfolgt am DD.MM.JJJJ / offen]

NÄCHSTER SKILL: [zv-pfueb-bank / zv-pfueb-arbeitsentgelt / ...]
```

## Qualitätsgates

- Niemals vor Aufhebung/Einstellung des Verfahrens vollstrecken.
- Niemals nach Restschuldbefreiung vollstrecken, wenn § 302 InsO nicht greift – Schadensersatzrisiko.
- Niemals deliktische Privilegierung ohne Eintragungsvermerk in der Tabelle annehmen.
- Verjährung 30 Jahre: jüngere Forderungen aus laufender Tabelle möglich.
- Klausel und Zustellung wie bei jedem Titel.

## Querverweise

- `insolvenzforderungsanmeldungspruefung/ifap-tabellenauszug-178` – wenn der Auszug erst beschafft wird (anderes Plugin, eng verzahnt)
- `zv-titel-klausel-zustellung`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-abwehr-schuldner` – Vollstreckungsgegenklage nach Restschuldbefreiung

## 3. `zv-vermoegensauskunft-gv`

**Fokus:** Gläubiger weiss nichts über Vermögen des Schuldners und will Auskunft erzwingen. § 802c ZPO Vermogensauskunft EV. Prüfraster: Antrag beim GV Sperrfrist 2 Jahre § 802d ZPO Eintragung Schuldnerverzeichnis § 882b ZPO Erzwingungshaft § 802g ZPO. Output: Auftrag Vermogensauskunft GV und Auswertungsprotokoll Vermogensverzeichnis. Abgrenzung zu zv-kontensuche-drittschuldner (Drittauskunfte) und zv-mobiliar-gv-auftrag (Pfaendung nach Ermittlung).

# Vermögensauskunft

## Aufgabe

Sachstandsermittlung beim Schuldner über alle Vermögenswerte. Voraussetzung für gezielte Pfändung, wenn Bank, Arbeitgeber oder andere Werte unbekannt sind.

## Startet bei

- Vollstreckbarer Titel + Klausel + Zustellung
- Keine konkreten Vermögenswerte bekannt **oder** bisherige Vollstreckungsversuche erfolglos
- Keine Sperrfrist § 802d ZPO offen

## Rechtsgrundlagen

- § 802a Abs. 2 Nr. 2 ZPO – Mindestauftrag
- § 802c ZPO – Abnahme der Vermögensauskunft, eidesstattliche Versicherung
- § 802d ZPO – Sperrfrist zwei Jahre
- § 802f ZPO – Verfahren beim Gerichtsvollzieher
- § 802g ZPO – Erzwingungshaft
- § 802l ZPO – Drittauskünfte (Rentenversicherung, BZSt, Bundesanstalt für Finanzdienstleistungsaufsicht / Kontensuche)
- § 882b ZPO – Schuldnerverzeichnis
- §§ 13, 27 GvKostG – Gebühren

## Workflow

1. **Sperrfrist § 802d ZPO** prüfen: Hat der Schuldner in den letzten zwei Jahren bereits Vermögensauskunft erteilt? Wenn ja, Auftrag nur bei glaubhaft gemachter Vermögensänderung.
2. **Auftragsformular** an den am Schuldnerwohnsitz zuständigen Gerichtsvollzieher (Verteilung über Geschäftsstelle Amtsgericht).
3. **Modulwahl**: § 802a Abs. 2 ZPO erlaubt Kombinationsaufträge – Zahlungsaufforderung, Vermögensauskunft, Mobiliarpfändung. Häufig sinnvoll: Modul 1 (Zahlung) + Modul 2 (Vermögensauskunft) + Modul 3 (Sachpfändung).
4. **Termin** beim Gerichtsvollzieher; Schuldner erscheint oder wird vorgeführt.
5. **Vermögensverzeichnis** wird beim zentralen Vollstreckungsgericht hinterlegt; Gläubiger erhält Abdruck.
6. **Drittauskünfte § 802l ZPO** beantragen, wenn Vermögensauskunft unergiebig: Anschrift Arbeitgeber bei Rentenversicherung, Kontodaten bei BZSt, KFZ-Halterdaten beim Kraftfahrt-Bundesamt.
7. **Eintragung Schuldnerverzeichnis** bei Nichtabgabe oder eidesstattlicher Versicherung – Wirkung zwei Jahre.
8. **Auswertung**: vorhandene Konten, Arbeitgeber, Forderungen, Sachwerte – jeweils Anschlussaufträge anstoßen.

## Sperrfrist § 802d ZPO

Zwei Jahre ab letzter Vermögensauskunft. Neue Abnahme nur, wenn:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- oder neuer Gläubiger und altes Verzeichnis bereits älter als sechs Monate ist und Aktualität gefordert wird (in Grenzen).

Andernfalls genügt es, beim zentralen Vollstreckungsgericht Einsicht in das vorhandene Vermögensverzeichnis zu nehmen.

## Erzwingungshaft § 802g ZPO

- Antrag nach unentschuldigtem Nichterscheinen oder Verweigerung.
- Bis sechs Monate Haft.
- Verhältnismäßigkeit prüfen – bei aussichtsloser Vollstreckung oft kontraproduktiv.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
VA-AUFTRAG [Mandant] gegen [Schuldner], Az [GV]

Titel: [Art, Datum]
Sperrfrist § 802d: [frei / bis DD.MM.JJJJ / Glaubhaftmachung beigelegt]
Modul-Auftrag: [1 Zahlung / 2 VA / 3 Sachpfändung]
Drittauskunft § 802l: [ja – Rentenversicherung, BZSt, KBA]
Voraussichtliche Kosten: EUR x (GvKostG)

NÄCHSTER SCHRITT: VA-Termin abwarten / bei Nichterscheinen § 802g
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals VA-Auftrag innerhalb der Sperrfrist ohne Glaubhaftmachung.
- Niemals Erzwingungshaft beantragen, wenn offensichtlich unverhältnismäßig.
- Bei Verbraucherinsolvenz § 287a InsO: Schuldnerverzeichniseintragung kann Restschuldbefreiung gefährden – Schuldnerseite mitdenken.
- Drittauskunft § 802l ZPO erst nach VA mit erfolglosem Ergebnis – nicht vorab.

## Querverweise

- `zv-titel-klausel-zustellung`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-pfueb-mieter-finanzamt`
- `zv-mobiliar-gv-auftrag`
- `zv-kontensuche-drittschuldner`
- `zv-elektronische-zustellung-2027`
