---
name: 15-klage-differenzschaden
description: "Für eine freigegebene, bezifferte Differenzschadensklage bei verbleibendem Fahrzeug. Erstellt Rubrum, Antrag, Streitgegenstand, Subsumtion, Beweise und Vorteilsausgleich vollständig. Keine Zug-um-Zug-Rückabwicklung."
---

# Klage auf Differenzschaden

## Zweck und Anwendungsfall

Dieser Skill erstellt die Klage der Fahrlässigkeitslinie: Differenzschaden nach § 823 Abs. 2 BGB i.V.m. § 6 Abs. 1, § 27 Abs. 1 EG-FGV, typischerweise beim Thermofenster. Das Fahrzeug bleibt beim Kläger; beantragt wird ein bezifferter Betrag, den das Gericht nach § 287 ZPO im Korridor von 5 bis 15 Prozent des Kaufpreises schätzt; Endprodukt ist die vollständig ausformulierte Klageschrift.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater (Kanzlei, Verbraucherschutz, Legal-Tech): Menüs, kurze Prüffragen, Tabellen, Ampel, Lückenliste, nächster Schritt. Schwierige Punkte als Eskalation an eine Rechtsanwältin oder einen Rechtsanwalt markieren; keine Rechtsberatung ohne anwaltliche Verantwortung bei Anwaltszwang oder RDG-Grenzen.

## Erste Antwort

Die erste Antwort liefert sofort eine vorläufige, aber vollständig ausformulierte Klage mit beziffertem Zahlungsantrag samt Prozesszinsen, Quotenabsatz und Aufzehrungskontrolle mit Rechenweg. Fehlende Falldaten werden an ihrer konkreten Textstelle benannt, insbesondere Kaufpreis, Zielquote, aktueller Wert oder Restwert und dazugehöriger Beleg. Verboten: Theorie-Vorträge, Menü-Aufzählungen, Werkzeug-Fehlersuche, mehr als drei Rückfragen, Rückfragen trotz möglichem Platzhalter-Entwurf. Korpus-Skripte sind nur Beschleuniger; bei Fehlschlag ohne Meldungslärm manuell weiterarbeiten, ein Werkzeugfehler blockiert nie den Entwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Klagewegvermerk aus Skill 13, Schadenstabelle aus Skill 08, Verjährungsbefund aus Skill 07.
- Einordnungsbefund aus Skill 05; Anspruchsschreiben und Zustellprotokoll aus Skill 09.
- Typgenehmigungs-, Herstellungs-, Kauf- und Updatezeitpunkt samt Normfassung aus Skill 04/06.

## Ablauf / Checkliste

1. Kontrollpunkte: Verjährung, fahrzeugbezogene Betroffenheit mit greifbaren Anhaltspunkten, Bezifferung nach Vorteilsausgleich und Zuständigkeit; ein Sachverständigenangebot ersetzt fehlenden Primärvortrag nicht.
2. Rubrum und Antrag: bezifferter Zahlungsantrag nebst Prozesszinsen; keine Feststellungsklage zur technischen Aufklärung; Ausnahmen vom Vorrang der Leistungsklage nur mit eigenständigem Feststellungsinteresse. Beim Berufungsübergang vom großen Schadensersatz Hilfsantrag nach `VIa ZR 947/23` ausdrücklich stellen; übrige Zulässigkeit prüfen.
3. Sachverhalt: Kauf, Motorbaureihe, ursprüngliche Funktion, Rückruf, Update-Einladung/-Installation/-Version, Vorher-nachher-Folgen, Kenntnisverlauf; jede Tatsache mit Anlage.
4. Anspruch: Pflichten aus der zeitlich anwendbaren EG-FGV-Fassung, Einrichtung, Erwerbskausalität und Schaden darlegen; §§ 6, 27 EG-FGV nicht ohne Datumsprüfung auf post-transitionelle Typgenehmigungen übertragen (VO (EU) 2018/858). Bei erst per Update installierter Einrichtung `C-666/23`: Handlung, eigener Schaden und Streitgegenstand getrennt vom Erwerbsschaden; die Offenlegung vom 22.09.2015 belegt keine Kenntnis der Update-Funktion; eigene §§-195/199-BGB-Rechnung aus Skill 07, kein Neubeginn.
   Verschulden wird bei objektivem Verstoß vermutet; Entlastung sequenzieren: Irrtum sämtlicher relevanter §-31-BGB-Repräsentanten oder ordnungsgemäße Ressortorganisation, danach Unvermeidbarkeit, zuletzt (auch hypothetische) Behördenbilligung. Behördenvorgänge weder pauschal entwerten noch als Legalitätszeugnis übernehmen; `VIa ZR 314/24` trifft keine Aussage zu dieser Spur.
5. Quote und Vorteilsausgleich: Korridor fallbezogen schätzen, Einrichtungen nicht addieren; Nutzungsvorteile und objektiven Restwert nach BGH-Linie rechnen, mögliche vollständige Aufzehrung offen ausweisen.
6. Beweise: Urkunden, Sachverständigengutachten, sekundäre Darlegungslast konkret auslösen. EA288-Sammlung und Parallelverfahren nur bei belegt vergleichbarer Motor-/Softwarekonfiguration und Quelle; `VIa ZR 1580/22` ist Anwendungsanker, kein Beweis für Einrichtung oder Haftung. Nachweise zweistufig: `diesel-fuenfjahre-query.py --query "[Motor Funktion]" --arbeitsset`, für EA288-Hypothesen `ea288-corpus-query.py`; Rang C/D und Kanzleimaterial nie als Beleg, jede Fundstelle am Volltext verifizieren.
7. Statuskontrolle: `C-666/23`, `VIa ZR 87/24` und `VIa ZR 613/24` zusammen darstellen; bei drohender Aufzehrung Laufleistung, Restwert, Stichtag, Bruttoquote oder Angemessenheit angreifen. Die weiter anhängigen EuGH-Gesamtsystemvorlagen `C-95/26`, `C-152/26`, `C-173/26`, `C-270/26`, `C-293/26` und `C-443/26` nur als offene Fragen und Aussetzungsaspekt führen. `C-113/26`, `C-114/26` und `C-440/26` wurden im August 2026 ohne Sachantwort gestrichen; keine Antwort, Beweislastumkehr, Divergenz oder Vorlagepflicht erfinden.
8. Anlagen aus der Belegmatrix; Ausformulierungskontrolle; danach Skill `21-bea-versandfertig-schriftsatz-anlagen`; erst dessen grüne Übergabe geht an Skill 16.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Eine bezifferte Leistungsklage schreiben, die objektiven Verstoß, Verschulden, Erwerbskausalität, Quote und Vorteilsausgleich jeweils eigenständig trägt.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Keine Klagefreigabe bei spekulativem Fahrzeugbezug, fehlender Netto-Rechnung oder unzulässigem Feststellungsersatz.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Tragende Linie: Bei fahrlässigem Verstoß haftet der Hersteller auf den Differenzschaden von 5 bis 15 Prozent des Kaufpreises; Verschulden wird vermutet. | Bestätigt |
| BGH, Urt. v. 15.02.2024 - VII ZR 905/21 | Den Differenzschaden grundsätzlich beziffert als Leistung beantragen; technische Aufklärung oder Sachverständigenbeweis begründen allein kein Feststellungsinteresse. | Amtlich geprüft |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | EG-Typgenehmigung oder hypothetische Behördenbestätigung trägt einen daraus hergeleiteten unvermeidbaren Verbotsirrtum nicht. | Amtlich geprüft |
| BGH, Urt. v. 28.07.2026 - VIa ZR 545/23; VIa ZR 151/23 | Konkreter Thermofenstervortrag genügt für die weitere Differenzschadenprüfung; Einrichtung, Verschulden, Kausalität und Quote bleiben zu beweisen. | Amtlich geprüft |
| BGH, Urt. v. 03.09.2025 - VIa ZR 26/24 | Der Hersteller trägt tatsächlichen Rechtsirrtum und Unvermeidbarkeit getrennt; für einen konkreten Behördenvorgang ist vollständige Offenlegung zentral. | Amtlich geprüft |
| Fünfjahreskorpus 26.08.2021 bis 26.08.2026: 135 Entscheidungen und Statusakten | Für den konkreten Schriftsatz höchstens sechs ausgewogene Treffer mit Quellenrang und Gegenlinie laden. | Kuratierter Arbeitskorpus mit Quellenrängen |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

Antrag:

„1. Die Beklagte wird verurteilt, an die Klägerin [Betrag in EUR] nebst Zinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz seit Rechtshängigkeit zu zahlen."

Baustein Quotenbegründung:

„Der Differenzschaden ist nach § 287 ZPO im Korridor von 5 bis 15 Prozent des Kaufpreises zu schätzen. Im Streitfall ist ein Satz von [Quote in Prozent] Prozent angemessen; dafür sprechen [fallbezogene Quotenfaktoren]; quotenmindernde Umstände von Gewicht sind nicht ersichtlich. Bei einem Kaufpreis von [Betrag in EUR] ergibt sich ein Differenzschaden von [Betrag in EUR]. Nutzungsvorteile und objektiver Restwert sind nur insoweit schadensmindernd anzurechnen, als ihre Summe den Wert des Fahrzeugs bei Vertragsschluss (Kaufpreis abzüglich Differenzschaden) übersteigt; diese Schwelle ist im Streitfall [nicht überschritten / um [Betrag in EUR] überschritten]. [In der Berufungslage: Der hilfsweise verlangte Betrag bleibt hinter dem Hauptantrag zurück und erweitert den Streitstoff nicht.]"

### Rechenbeispiel Aufzehrung

Ausgangswerte: Kaufpreis 32.500,00 EUR, Quote 10 Prozent, Nutzungsvorteil 12.792,00 EUR (98.400 km von 250.000 km), objektiver Restwert 17.500,00 EUR. Rechnung: Differenzschaden 32.500,00 mal 0,10 gleich 3.250,00 EUR; Schwelle 32.500,00 minus 3.250,00 gleich 29.250,00 EUR; Anrechnung 12.792,00 plus 17.500,00 gleich 30.292,00 EUR, Überschuss 1.042,00 EUR; es verbleiben 2.208,00 EUR.

Ergebnis-Satz: Beantragt werden 2.208,00 EUR nebst Prozesszinsen. Erreicht die Summe aus Nutzungsvorteil und Restwert den Kaufpreis, ist der Anspruch vollständig aufgezehrt.

### Entscheidungstabelle

| Wenn | Dann | Begründung | Nächster Schritt |
| --- | --- | --- | --- |
| Summe bis zur Schwelle | Volle Quote | Anrechnung erst oberhalb der Schwelle | Antrag beziffern |
| Schwelle überschritten, unter dem Kaufpreis | Gekürzter Betrag | Anrechnung nur in Höhe des Überschusses | Rechenweg übernehmen |
| Summe erreicht den Kaufpreis | Vollständige Aufzehrung | Ohne Angriff auf die Rechenfaktoren fehlt der wirtschaftliche Kern | Anwaltliche Eskalation |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Tragende Anker aus `references/gepruefte-anker-dieselgate.md`, Normstand aus `references/rechtsstand-2026-gesetzgebung.md`, aktuelles Sechs-Anker-Arbeitsset samt LG-/OLG-Gegenlinien aus `references/diesel-rechtsprechung-2021-2026.md`. EA288-Sammlung ist Nutzermaterial. Statusfallen: nur `C-666/23` ist Sachurteil; `C-667/23`/`C-668/23` und `C-251/23`/`C-308/23` wurden gestrichen; `C-100/23` ist kein Diesel-Urteilsaktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran; nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Vollständig ausformulierte Klageschrift mit Rubrum, nummerierten Anträgen, Sachverhalt, Begründung samt Quotenbegründung, Beweisangeboten und Anlagenverzeichnis in dezimaler Gliederung; Skelett-Schriftsätze sind als Endprodukt verboten.

Übergabe an Skill 21: Freigabestatus, offene Platzhalter, Anlagenbezugnahmen mit Textanker und die freigegebene Haupt-PDF mit SHA-256 ausweisen; ein Textentwurf ist keine Endfassung.

## Beispiele

- Eingang: OM651 mit belegtem Thermofenster, Kaufpreis 32.500,00 EUR. Kernbefund: Aufzehrung droht. Erste Antwort: vorläufige, aber vollständig ausformulierte Klage mit Antrag über 2.208,00 EUR nach Aufzehrungskontrolle und Quotenabsatz; der noch fehlende Restwertbeleg ist im Vorteilsausgleich präzise markiert.
- Eingang: offene EA288-Betroffenheit. Kernbefund: technische Identität unbelegt. Erste Antwort: vorläufige, aber vollständig ausformulierte Klage mit Indizienkette, sekundärer Darlegungslast und offenem Abweisungsrisiko; als konkrete Lücke bleibt der technische Identitätsbeleg bezeichnet.
