---
name: artenschutz-naturschutz-aufstellungsbeschluss
description: "Artenschutz Naturschutz Aufstellungsbeschluss: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Artenschutz Naturschutz Aufstellungsbeschluss

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Artenschutz Naturschutz Aufstellungsbeschluss** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `artenschutz-naturschutz-planung` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP) CEF-Massnahmen Eingriffsregelung § 1a Abs. 3 BauGB FFH-Vertraeglichkeit § 34 BNatSchG. Stadtbezogene Arten Mauersegler Schwalben Fledermaeuse. Output: Artenschutz-Prüfprotokoll und Angriffspunkte Normenkontrolle. Abgrenzung zu umweltbericht-umweltprüfung (UVPG) und abwaegungsgebot-1-abs-7-baugb. |
| `aufstellungsbeschluss-bekanntmachung` | Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs. 1 Beschluss als Satzung § 10 Abs. 1 ortsuebliche Bekanntmachung § 10 Abs. 3 Identität ausgelegte und beschlossene Fassung Zuständigkeit Beschlussfähigkeit. Output: Verfahrensfehlerprüfung-Protokoll. Abgrenzung zu beteiligung-frueh-foermlich (Beteiligungsverfahren) und planerhaltung-214-215-baugb. |
| `benutzungssatzung-kommunale-einrichtung` | Benutzungssatzungen kommunaler Einrichtungen: Markthalle, Friedhof, Kita, Bibliothek, Sportanlage, Hausrecht und Grundrechte.; Normanker: VwGO § 47; Kommunalordnungen; Grundrechte; Gebührenrecht; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Artenschutz Naturschutz Aufstellungsbeschluss**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `artenschutz-naturschutz-planung`

**Fokus:** Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP) CEF-Massnahmen Eingriffsregelung § 1a Abs. 3 BauGB FFH-Vertraeglichkeit § 34 BNatSchG. Stadtbezogene Arten Mauersegler Schwalben Fledermaeuse. Output: Artenschutz-Prüfprotokoll und Angriffspunkte Normenkontrolle. Abgrenzung zu umweltbericht-umweltprüfung (UVPG) und abwaegungsgebot-1-abs-7-baugb.

# Artenschutz und Naturschutz in der Bauleitplanung

## Zweck

Artenschutz ist materieller Pflichtprogramm-Punkt jedes B-Plans, der bauliche Veränderungen vorsieht. Lücken in der speziellen artenschutzrechtlichen Prüfung (saP) sind häufiger Treffer.

## Schritt 1 — Zugriffsverbote § 44 BNatSchG


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Drei Verbote
- **Tötungsverbot** § 44 Abs. 1 Nr. 1 BNatSchG: Verbot, wildlebenden Tieren der besonders geschützten Arten nachzustellen, sie zu fangen, zu verletzen oder zu töten
- **Störungsverbot** § 44 Abs. 1 Nr. 2 BNatSchG: Verbot, wildlebende Tiere der streng geschützten Arten und der europäischen Vogelarten während der Fortpflanzungs-, Aufzucht-, Mauser-, Überwinterungs- und Wanderungszeiten erheblich zu stören
- **Lebensstättenschutzverbot** § 44 Abs. 1 Nr. 3 BNatSchG: Verbot, Fortpflanzungs- oder Ruhestätten der wildlebenden Tiere der besonders geschützten Arten aus der Natur zu entnehmen, zu beschädigen oder zu zerstören

### Geltungsbereich
- Besonders geschützte Arten: nach EU-Recht (FFH-Richtlinie, Vogelschutz-RL) sowie Bundesartenschutzverordnung
- Streng geschützte Arten: Teilmenge der besonders geschützten Arten
- Im Bauplanungsrecht primär: alle europäisch geschützten Arten

## Schritt 2 — Spezielle artenschutzrechtliche Prüfung (saP)

### Aufbau saP
1. Relevanzprüfung — welche Arten sind im Plangebiet zu erwarten
2. Bestandserfassung — Begehung im richtigen Zeitraum
3. Konfliktanalyse — Welche Zugriffsverbote werden berührt
4. Maßnahmen-Konzept — Vermeidung, CEF, FCS
5. Ausnahme-Begründung § 45 Abs. 7 BNatSchG

### Anforderungen
- Sachverständige mit nachgewiesener Qualifikation
- Begehung in der jeweils relevanten Jahreszeit
- Dokumentation mit Karten, Fotos, Artenlisten
- BVerwG, Urteil vom 9.7.2008 – 9 A 14.07 (saP-Anforderungen)

## Schritt 3 — Stadtbezogene Arten

### Gebäudebrüter
- **Mauersegler** Apus apus — Nester in Dachgesimsen, Mauerlöchern
- **Mehlschwalben** Delichon urbicum — Nester an Außenwänden
- **Rauchschwalben** Hirundo rustica — Nester innen in offenen Gebäuden
- **Haussperlinge** Passer domesticus — Hohlräume in Fassaden
- **Dohlen** Corvus monedula — höher gelegene Mauerlöcher
- Alle europäische Vogelarten = besonders geschützt

### Fledermäuse
- **Zwergfledermaus** — sehr verbreitet, Hangplätze in Dachräumen
- **Großer Abendsegler** — Baumhöhlen, größere Quartiere
- **Mausohr** — strenger Schutz
- Alle streng geschützt (Anhang IV FFH-RL)

### Reptilien
- **Zauneidechse** Lacerta agilis — auf Brachflächen, Bahndämmen, Steingärten
- Anhang IV FFH-RL — strenger Schutz

### Brachflächen-Arten
- **Wildbienen** und **Hummeln** — auf Ruderalflächen
- **Spezielle Schmetterlinge** je nach Standort

## Schritt 4 — CEF-Maßnahmen (continuous ecological functionality)

### Voraussetzung
- Vorgezogene Ausgleichsmaßnahme
- Maßnahme muss vor Eingriff wirken
- Räumlicher und zeitlicher Bezug zur betroffenen Lokalpopulation

### Beispiele
- Künstliche Mauersegler-Nistplätze an Ersatzgebäude vor Abriss
- Fledermaus-Kästen in räumlicher Nähe vor Quartier-Beseitigung
- Anlage Eidechsen-Habitat (Steinhaufen, Trockenmauern) vor Brachflächen-Bebauung

### Funktionsbeweis
- Monitoring erforderlich
- Erfolgskontrolle über mehrere Jahre

## Schritt 5 — Ausnahme § 45 Abs. 7 BNatSchG

### Drei kumulative Voraussetzungen
1. **Zwingende Gründe des überwiegenden öffentlichen Interesses** einschließlich solcher sozialer oder wirtschaftlicher Art
2. **Keine zumutbaren Alternativen**
3. **Erhaltungszustand der Populationen** verschlechtert sich nicht (FCS = favourable conservation status)

### Anforderung Plan
- Begründung erforderlich
- Standort-Alternativen ernsthaft geprüft
- Populations-Auswirkung dokumentiert

### Häufige Treffer
- Wirtschaftliches Interesse als "zwingend" deklariert ohne überwiegende Begründung
- Alternativen nur formelhaft erwähnt
- FCS-Bewertung fehlt oder pauschal

## Schritt 6 — Eingriffsregelung § 1a Abs. 3 BauGB

### Stufen
- **Vermeidung** — der Eingriff selbst vermeiden
- **Minimierung** — bei Unvermeidbarkeit reduzieren
- **Ausgleich** — gleichartige Wiederherstellung
- **Ersatz** — andere gleichwertige Maßnahmen

### Bilanzierung
- Eingriffs-Wert in Wertpunkten
- Ausgleichs-Wert in Wertpunkten
- Saldo darf nicht negativ sein

### Räumliche und funktionale Zuordnung
- Ausgleichsfläche möglichst im selben Naturraum
- Funktional gleichwertig

## Schritt 7 — FFH-Vorprüfung § 34 BNatSchG

### Anwendung
- Wenn Plangebiet in FFH- oder Vogelschutzgebiet liegt
- Oder daran angrenzt
- Oder Wirkungspfade ins Gebiet hineinragen

### Vorprüfung
- Auf erhebliche Beeinträchtigung von Schutz- und Erhaltungszielen
- Bei Zweifeln — volle Verträglichkeitsprüfung

### Wirkungspfade
- Lärm, Licht, Bewegung
- Wasserabfluss, Wasserentnahme
- Schadstoffeinträge

## Schritt 8 — Audit saP

### Methodik-Audit
- Wer hat saP erstellt? Qualifikation?
- Begehung in welchem Zeitraum? Mehrere Begehungen?
- Welche Arten wurden gezielt erfasst? Welche nicht?
- Ist die Bestandsaufnahme aktuell? (i.d.R. höchstens 5 Jahre alt)

### Inhalts-Audit
- Sind alle stadtbezogen relevanten Arten geprüft?
- Sind CEF-Maßnahmen verbindlich festgesetzt?
- Sind sie zeitlich vor Eingriff verortet?
- Gibt es Monitoring?
- Wird Erhaltungszustand der Population thematisiert?

### Festsetzungs-Audit
- Sind CEF-Maßnahmen in den textlichen Festsetzungen des Plans?
- Oder nur in Begründung?
- Festsetzung in Begründung allein ist rechtlich unzureichend

## Schritt 9 — Strategische Angriffspunkte

### Häufige Schwachpunkte
- Begehung zur falschen Jahreszeit
- Fehlende Begehung im Spätsommer (Mauerseglerbrut)
- Pauschale Aussage "keine geschützten Arten festgestellt" ohne Methodik
- CEF-Maßnahmen nur in Begründung, nicht in Festsetzung
- Ausnahme-Begründung formelhaft
- FFH-Vorprüfung übersehen bei angrenzendem Schutzgebiet

### Im Schriftsatz
- Subsumtion unter § 44 BNatSchG und § 1a Abs. 3 BauGB
- Verstoß gegen Ermittlungspflicht § 2 Abs. 3 BauGB
- Abwägungsdefizit § 1 Abs. 7 BauGB

## Quellen

- BNatSchG §§ 34 44 45
- BauGB §§ 1a 2 1 Abs. 7 9
- FFH-Richtlinie 92/43/EWG
- Vogelschutz-Richtlinie 2009/147/EG
- BVerwG, Urteil vom 9.7.2008 – 9 A 14.07 (saP)
- BVerwG, Urteil vom 6.11.2013 – 9 A 14.12 (FCS)
- BVerwG, Urteil vom 23.4.2014 – 9 A 25.12 (Tötungsverbot)
- BayVGH, Urteil vom 30.3.2017 – 14 N 16.1112 (Stadtarten)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Artenschutz/Naturschutz

§ 44 Abs. 1 Nr. 1-3 BNatSchG (Zugriffsverbote) → § 44 Abs. 5 BNatSchG (Legalausnahme Planung) → § 45 Abs. 7 BNatSchG (Ausnahme) → § 67 BNatSchG (Befreiung) → § 34 BNatSchG (FFH-Verträglichkeit) → § 1a Abs. 3 BauGB (Eingriffsregelung) → § 2 Abs. 3 BauGB (Ermittlungspflicht) → § 1 Abs. 7 BauGB (Abwägungsgebot)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Bearbeitung

Kläre vor Beginn der saP-Prüfung:
1. Ist das Plangebiet ein Neubau- oder Umnutzungsgebiet? (Brachflächen haben höheres Artenpotenzial)
2. Liegen Altgebäude im Plan-Umgriff? (Gebäudebrüter-Pflichterfassung)
3. Ist die saP älter als 5 Jahre? (Neuerhebung erforderlich)
4. Welches Bundesland? (Landesrechtliche Ergänzungen zu § 44 BNatSchG beachten)
5. Gibt es Hinweise auf Vorkommen streng geschützter Arten aus regionalem Artenkataster?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Artenschutzrechtliche Ruege im Planungsverfahren | Artenschutz-Ruegeschriftsatz nach Schema; Template unten |
| Variante A — Artenschutz klar verletzt Behoerde kooperativ | Informelle Einwendung zuerst; Klage nur bei Ablehnung |
| Variante B — Saison-Schutz Bruetzeit laeuft noch | Sofortige Einwendung mit Fristsetzung; Vollzugsstopp beantragen |
| Variante C — Ausnahme nach § 45 BNatSchG moeglich | Ausnahme-Antrag statt Klage; Kompensationsmassnahmen anbieten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Artenschutz-Rüge im Schriftsatz

**Adressat:** OVG/VGH — Tonfall sachlich-wissenschaftlich-juristisch

```
III. Verstoß gegen § 44 Abs. 1 Nr. 3 BNatSchG — Lebensstättenschutz [NAME ART]

1. Bestandsaufnahme methodisch unzureichend (§ 2 Abs. 3 BauGB)
 Die saP der [BUERO] vom [DATUM] enthält zur Art [NAME] lediglich [SATZ AUS GUTACHTEN].
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Insbesondere wurde die [KONKRETER MANGEL: Begehung im Maerz statt im Hochsommer / Kartierung nur Kerngebiet ohne Puffer].

2. CEF-Maßnahme nicht verbindlich festgesetzt
 Die Maßnahme [BEZEICHNUNG] ist nur in Begründung Seite X erwähnt, aber nicht in den textlichen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

3. FCS-Nachweis fehlt
 Der Erhaltungszustand der Lokalpopulation von [ART] wird nicht bewertet.
 Ohne diesen Nachweis ist die Ausnahme nach § 45 Abs. 7 BNatSchG nicht erfüllt
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 2. `aufstellungsbeschluss-bekanntmachung`

**Fokus:** Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs. 1 Beschluss als Satzung § 10 Abs. 1 ortsuebliche Bekanntmachung § 10 Abs. 3 Identität ausgelegte und beschlossene Fassung Zuständigkeit Beschlussfähigkeit. Output: Verfahrensfehlerprüfung-Protokoll. Abgrenzung zu beteiligung-frueh-foermlich (Beteiligungsverfahren) und planerhaltung-214-215-baugb.

# Aufstellungsbeschluss und Bekanntmachung

## Zweck

Audit der formellen Verfahrenskette des B-Plans. Häufigste Treffer im Normenkontrollverfahren liegen hier: Bekanntmachung fehlerhaft, Beschlussvorlage abweichend, Anstoßfunktion verletzt.

## Schritt 1 — Verfahrenskette im Überblick

### Reguläre Kette
1. Aufstellungsbeschluss § 2 Abs. 1 BauGB
2. Frühzeitige Beteiligung Öffentlichkeit § 3 Abs. 1 BauGB
3. Frühzeitige Beteiligung Behörden § 4 Abs. 1 BauGB
4. Erarbeitung Planentwurf
5. Förmliche Beteiligung Öffentlichkeit § 3 Abs. 2 BauGB (Auslegung)
6. Förmliche Beteiligung Behörden § 4 Abs. 2 BauGB
7. Ggf. erneute Auslegung bei Änderung § 4a Abs. 3 BauGB
8. Abwägungsbeschluss
9. Satzungsbeschluss § 10 Abs. 1 BauGB
10. Bekanntmachung § 10 Abs. 3 BauGB
11. Beizustellen: Begründung mit Umweltbericht zur Einsichtnahme

### Beschleunigte Verfahren
- § 13 BauGB vereinfachtes Verfahren — Schritte verkürzt
- § 13a BauGB Innenentwicklung — keine Umweltprüfung im Einzelfall
- § 13b BauGB Außenentwicklung Wohnbau — Befristung beachten

## Schritt 2 — Aufstellungsbeschluss § 2 Abs. 1 BauGB

### Inhalt
- Beschluss des Gemeinderats, einen B-Plan aufzustellen
- Räumlicher Geltungsbereich abgrenzbar
- Planziel und allgemeines Anliegen

### Form
- Sitzungsöffentlichkeit gewahrt § 52 BayGO
- Beschlussfähigkeit § 47 BayGO
- Befangenheit § 49 BayGO geprüft

### Bekanntmachung Aufstellungsbeschluss
- Ortsübliche Bekanntmachung
- Häufig Amtsblatt
- Fehlt die Bekanntmachung — Verfahrensfehler, aber häufig unbeachtlich nach § 214 BauGB

## Schritt 3 — Identität der Planfassung

### Identitätsprüfung
- Welche Planfassung wurde frühzeitig ausgelegt?
- Welche Planfassung wurde förmlich ausgelegt?
- Welche Planfassung wurde als Satzung beschlossen?
- Welche Planfassung wurde bekanntgemacht?

### Häufige Treffer
- Beschluss-Vorlage zeigt Plan-Stand vom 15.3., Beschluss verweist auf Plan vom 22.4. — Identitätsfehler
- Auslegung erfolgte über Plan-Stand 10.1., Beschluss über 5.5. ohne erneute Auslegung — § 4a Abs. 3 BauGB-Verstoß
- Beschluss umfasst zusätzliche Änderungen die nie ausgelegt waren — beachtlich (§ 214 Abs. 1 S. 1 Nr. 2 BauGB)

## Schritt 4 — Erneute Auslegung § 4a Abs. 3 BauGB

### Pflicht zur erneuten Auslegung
- Wenn Planentwurf nach Auslegung in der Substanz geändert wird
- Substanz = Berührung der Grundzüge der Planung
- Bloße redaktionelle Änderungen genügen nicht für erneute Auslegung

### Begrenzte erneute Auslegung
- Beschränkung auf die geänderten Teile möglich (§ 4a Abs. 3 S. 2 BauGB)
- Hinweis im Bekanntmachungstext erforderlich
- Frist mindestens zwei Wochen

### Häufiger Fehler
- Stadt erkennt nach Auslegung den Hochbauwunsch des Vorhabenträgers, Aufstockung von 6 auf 8 Geschosse, ohne erneute Auslegung in Beschluss aufgenommen — beachtlich

## Schritt 5 — Satzungsbeschluss § 10 Abs. 1 BauGB

### Beschlussgegenstand
- Beschluss umfasst Planurkunde, textliche Festsetzungen, Begründung mit Umweltbericht
- Beschluss in einem Akt — kein Aufspalten zulässig

### Beschlussvorlage
- Vollständig zur Sitzung ausgelegt
- Sieben Tage vor Sitzung an Stadträte verteilt (Bayern: § 47 Abs. 2 BayGO)
- Abwägungsdokumentation als Anlage

### Sitzungsöffentlichkeit
- Beratung und Beschluss in öffentlicher Sitzung § 52 BayGO
- Nichtöffentliche Beratung bei B-Plan-Beschluss in der Regel rechtswidrig

## Schritt 6 — Bekanntmachung § 10 Abs. 3 BauGB

### Inhalt der Bekanntmachung
- Bezeichnung des Plans
- Geltungsbereich
- Inkrafttreten
- Ort der Einsichtnahme in den Plan
- Hinweis auf § 215 BauGB-Rügefrist
- Hinweis auf § 44 BauGB-Entschädigungsanspruch
- Hinweis auf Beachtlichkeit nach § 214 BauGB

### Anstoßfunktion
- BVerwG, Beschluss vom 15.4.1988 – 4 N 4.87
- Bekanntmachung muss Anstoß-funktion erfüllen
- Bürger muss erkennen können, dass und wo er sich informieren kann
- Bei zu allgemeiner Bezeichnung — Anstoßfunktion verletzt

### Form der Bekanntmachung
- Ortsüblich nach Hauptsatzung der Gemeinde
- Amtsblatt regelmäßig vorgesehen
- Ersatzbekanntmachung bei umfangreichen Plänen möglich (§ 10 Abs. 3 S. 2 BauGB)
- Online-Veröffentlichung als zusätzliche Option, nicht ausreichend allein

## Schritt 7 — Häufige Treffer in der Bekanntmachung

| Fehler | Beachtlichkeit |
|---|---|
| Falsches Aktenzeichen / Plannummer | Anstoßfunktion verletzt — beachtlich |
| Fehlender Hinweis auf § 215 BauGB | Rügefrist läuft nicht — strategisch wichtig |
| Fehlender Hinweis auf § 44 BauGB | Entschädigungsanspruch bleibt — meist nicht beachtlich für Plan-Wirksamkeit |
| Falscher Einsichtsort | Anstoßfunktion verletzt — beachtlich |
| Geltungsbereich nur grob beschrieben | Anstoßfunktion fraglich |
| Bekanntmachung in nicht ortsüblicher Form | Wirksamkeit fraglich |

## Schritt 8 — Audit-Vorgehen

### Beschaffung
- Auszug Sitzungsniederschrift Aufstellungsbeschluss
- Auszug Sitzungsniederschrift Satzungsbeschluss
- Beschlussvorlagen
- Auslegungsnachweise (Auslegungsverfügung, Auslegungsbeginn, Auslegungsende)
- Bekanntmachungsexemplare aller Verfahrensschritte (Aufstellungs-Bek., Auslegungs-Bek., Satzungs-Bek.)

### Tabellarisches Audit
- Zeile pro Verfahrensschritt
- Spalten: Datum, Beschlussfähigkeit, Befangenheit, Bekanntmachung, Anstoßfunktion ja/nein, Fehler ja/nein, Beachtlichkeit
- Auswertung am Schluss

## Quellen

- BauGB §§ 2 3 4 4a 9 10 13 13a 13b 44 214 215
- BayGO Art. 47 49 52
- BVerwG, Beschluss vom 15.4.1988 – 4 N 4.87 (Anstoßfunktion)
- BVerwG, Urteil vom 18.7.2013 – 4 CN 3.12 (Identität Planfassung)
- BVerwG, Beschluss vom 18.12.1987 – 4 NB 2.87 (Ortsüblichkeit)

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `benutzungssatzung-kommunale-einrichtung`

**Fokus:** Benutzungssatzungen kommunaler Einrichtungen: Markthalle, Friedhof, Kita, Bibliothek, Sportanlage, Hausrecht und Grundrechte.; Normanker: VwGO § 47; Kommunalordnungen; Grundrechte; Gebührenrecht; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug nutzbar.

# Benutzungssatzungen kommunaler Einrichtungen: Markthalle, Friedhof, Kita, Bibliothek, Sportanlage, Hausrecht und Grundrechte.

## Auftrag

Dieser Skill löst § 47 VwGO aus der reinen Bauleitplanung. Er prüft, ob eine im Rang unter dem Landesgesetz stehende Rechtsvorschrift direkt vor dem OVG/VGH überprüft werden kann oder ob nur eine Inzidentkontrolle im Verfahren gegen einen Einzelakt passt.

## Normanker

VwGO § 47; Kommunalordnungen; Grundrechte; Gebührenrecht. Vor jeder Ausgabe muss das jeweilige Landesrecht geprüft werden, weil § 47 Abs. 1 Nr. 2 VwGO die Normenkontrolle außerhalb der BauGB-Fälle nur eröffnet, soweit Landesrecht dies bestimmt.

## Prüfprogramm

1. Normtyp: Satzung, Rechtsverordnung, Bebauungsplan, Polizeiverordnung, Benutzungssatzung oder bloßer Verwaltungsakt?
2. Statthaftigkeit: § 47 Abs. 1 Nr. 1 oder Nr. 2 VwGO, Landesrechtseröffnung, Rang unter Landesgesetz.
3. Antragsteller: mögliche Rechtsverletzung, Adressat, Eigentümer, Nutzer, Gemeinde, Verband oder Konkurrent.
4. Frist und Rechtsschutzbedürfnis: Jahresfrist, fortbestehende Beschwer, Parallelverfahren.
5. Materielle Kontrolle: Ermächtigung, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.
6. Rechtsfolge: Unwirksamkeit, Bekanntmachung der Entscheidung, Wirkung auf Folgebescheide, neue Satzung.

## Ausgabe

Erzeuge eine Statthaftigkeitsskizze, Satzungs-Red-Team, Eilantragsskizze, Schriftsatzgliederung oder Bürger-/Mandantenbrief.
