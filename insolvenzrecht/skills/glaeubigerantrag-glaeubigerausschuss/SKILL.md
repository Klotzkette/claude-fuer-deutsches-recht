---
name: glaeubigerantrag-glaeubigerausschuss
description: "Glaeubigerantrag Glaeubigerausschuss: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Glaeubigerantrag Glaeubigerausschuss

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Glaeubigerantrag Glaeubigerausschuss** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `glaeubigerantrag-pruefung` | Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowohl aus Gläubigerperspektive (Antragstellung) als auch aus Schuldnerperspektive (Abwehrstrategien). Lädt, wenn ein Mandant als Gläubiger einen Insolvenzantrag stellen will, wenn ein Schuldner einen Gläubigerantrag abwehren muss oder wenn Zulässigkeitsvoraussetzungen des Gläubigerantrags zu prüfen sind. |
| `glaeubigerausschuss-mitwirkung` | Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorlaeufiger Gläubigerausschuss § 22a InsO Schwellenwerte. Aufgaben Überwachung Insolvenzverwalter Beschlussfassung wesentliche Verwertungs-Entscheidungen Verguetungsprüfung. Rechte Akteneinsicht Anhoerung Beschlussantrag Kassen-Prüfung Haftung § 71 InsO. Output Ausschuss-Arbeitsmemo mit Checkliste laufender Pflichten und Risiko-Hinweisen. Abgrenzung: gläubigerantrag-prüfung für Eroefffnungsantrag des Gläubiger. |
| `inso-dsgvo-art17-nach-restschuldbefreiung` | Art. 17 DSGVO als insolvenzrechtlicher Anschlussanspruch nach Restschuldbefreiung: Löschung, Einschränkung, Widerspruch, Beschwerde und Klage. |
| `inso-eroeffnungsantrag-checkliste` | Checkliste Eroeffnungsantrag § 13 InsO: zustaendiges Gericht, Glaeubigerliste, Vermoegensverzeichnis, Erklaerung Geschaeftsleitung. Pruefraster fuer Schuldner- und Glaeubigeranwalt. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Glaeubigerantrag Glaeubigerausschuss**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `glaeubigerantrag-pruefung`

**Fokus:** Prüft Zulässigkeit und Begründetheit eines Gläubigerantrags auf Eröffnung des Insolvenzverfahrens nach § 14 InsO — sowohl aus Gläubigerperspektive (Antragstellung) als auch aus Schuldnerperspektive (Abwehrstrategien). Lädt, wenn ein Mandant als Gläubiger einen Insolvenzantrag stellen will, wenn ein Schuldner einen Gläubigerantrag abwehren muss oder wenn Zulässigkeitsvoraussetzungen des Gläubigerantrags zu prüfen sind.

# Prüfung Gläubigerantrag nach § 14 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Prüfung Gläubigerantrag nach § 14 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill strukturiert die vollständige Prüfung eines Gläubigerantrags auf
Eröffnung des Insolvenzverfahrens. Er deckt ab: die Zulässigkeitsvoraussetzungen
(rechtliches Interesse, Glaubhaftmachung der Forderung und des Eröffnungsgrundes),
die formellen Anforderungen der Antragsschrift, die Besonderheiten bei
Behördengläubigern sowie die wesentlichen Abwehrstrategien des Schuldners.

## Eingaben

- Gläubigerseite: Art und Höhe der Forderung, Titulierungsstand, bisherige
 Vollstreckungsversuche, vorhandene Nachweise zum Eröffnungsgrund
- Schuldnerseite: Aktuelle Zahlungslage, verfügbare Liquidität, Stellungnahme zur
 bestrittenen Forderung, Bereitschaft zur sofortigen Zahlung oder zur Vorlage
 eines Sanierungskonzepts
- Verfahrensstatus: Liegt bereits ein Eigenantrag vor? Sind andere Gläubigeranträge
 anhängig? Gibt es ein laufendes StaRUG-Verfahren?

## Rechtlicher Rahmen

### Gesetzliche Grundlagen

**§ 14 Abs. 1 S. 1 InsO** legt die drei kumulativen Voraussetzungen des
Gläubigerantrags fest:

1. **Rechtliches Interesse** an der Eröffnung des Insolvenzverfahrens
2. **Glaubhaftmachung der Forderung** (Bestand, Fälligkeit, Höhe)
3. **Glaubhaftmachung des Eröffnungsgrundes** (§§ 17–19 InsO)

**§ 14 Abs. 1 S. 2 InsO** schützt das Antragsrecht bei vorausgegangener
Befriedigung: Wurde der Gläubiger in den letzten sechs Monaten vor Antragstellung
befriedigt, bleibt seine Antragsbefugnis gleichwohl bestehen, wenn die Befriedigung
als Insolvenzanfechtung nach §§ 129 ff. InsO angreifbar wäre. Dies verhindert den
"Taktikzahlungseinwand" des Schuldners, der kurz vor Verfahrenseröffnung
Teilzahlungen leistet, um den antragstellenden Gläubiger zu beseitigen, ohne die
Insolvenzlage zu beheben.

**§ 13 InsO** regelt Form und Inhalt des Antrags; für Gläubigeranträge gelten
ergänzend die §§ 14 ff. InsO.

**§ 26 InsO**: Weist das Gericht den Antrag mangels Deckung der Verfahrenskosten
ab (Abweisung mangels Masse), erfolgt die Eintragung im Schuldnerverzeichnis
(§ 882b ZPO) — eine eigenständige wirtschaftliche Sanktion.

**§ 56a InsO** gewährt dem Schuldner ein Vorschlagsrecht für den
Insolvenzverwalter, wenn er selbst Insolvenzantrag stellt. Dieses Recht entfällt
beim reinen Gläubigerantrag.

**§§ 17, 18, 19 InsO** definieren die antragsrelevanten Eröffnungsgründe:
Zahlungsunfähigkeit (§ 17), drohende Zahlungsunfähigkeit (§ 18, nur für
Schuldner-Eigenantrag) und Überschuldung (§ 19, juristische Personen).

### Rechtsprechung (Maßstab; Aktenzeichen vor Ausgabe über dejure.org / openjur.de verifizieren)

**Anforderungen an Glaubhaftmachung Forderung § 14 InsO:** Gläubiger muss Tatsachen darlegen, aus denen die überwiegende Wahrscheinlichkeit des Bestehens der Forderung folgt; vollständige Beweisführung nicht erforderlich. Zulässige Mittel: eidesstattliche Versicherung (§ 294 ZPO), Titel, Mahnbescheid, Kontoauszüge, Rechnungen mit Empfangsbestätigung.

**Indizien für Zahlungsunfähigkeit § 17 InsO:** fruchtlose Pfändungsversuche, Rückgabe von Lastschriften, Wechselproteste, Häufung von Mahnverfahren, Lohnsteuer- und SV-Rückstände, BWA mit negativem Saldo. Die Indizien dienen der Glaubhaftmachung der überwiegenden Wahrscheinlichkeit der ZU.

**Streitige Forderung:** Antrag zulässig, wenn nach § 294 ZPO glaubhaft gemacht; bloßes Bestreiten des Schuldners ohne substantiierten Gegenvortrag beseitigt die Glaubhaftmachung nicht.

**Missbräuchlicher Druckantrag:** Antrag, der allein der wirtschaftlichen Druckausübung dient, ist unzulässig; das rechtliche Interesse an der Eröffnung muss zur gerichtlichen Entscheidung noch bestehen.

Für aktuelle BGH-Linie zu allen vorgenannten Punkten Datum, Aktenzeichen und Randnummer vor Ausgabe über offene Quellen verifizieren.

### Quellen (nur verifiziert)

- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
 Antragsberechtigung, Glaubhaftmachung, Forderungserfordernis und Missbrauch)
- Hölzle, in: K. Schmidt, InsO, 20. Aufl. 2023, § 14 Rn. 1–55 (Dogmatik des
 rechtlichen Interesses, Zulässigkeit bei titulierter und nicht-titulierter
 Forderung, § 14 Abs. 1 S. 2 InsO)
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
 Indizienbeweis, Glaubhaftmachungsstandard im Gläubigerantrag)

### IDW S 11

Der **IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen,
Stand 2017)** liefert das fachliche Rüstzeug zur Feststellung der
Zahlungsunfähigkeit (Liquiditätsstatus, 10 %/3-Wochen-Grundsatz) und der
Überschuldung (Fortbestehensprognose + Überschuldungsstatus). Im Gläubigerantrag
ist IDW S 11 relevant, wenn ein Gutachter zur Glaubhaftmachung des Eröffnungsgrundes
beauftragt wird oder das Gericht einen vorläufigen Sachverständigen bestellt.

## Ablauf


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1 — Gläubigerprüfung: Forderung

- **Titulierungsstand**: Liegt ein vollstreckbarer Titel vor (Urteil, Beschluss,
 Vollstreckungsbescheid)? Wenn ja, entfällt das Glaubhaftmachungsproblem für
 die Forderung weitgehend.
- **Nicht-titulierte Forderung**: Belege zusammenstellen — Rechnung, Lieferschein,
 Empfangsbestätigung, Kontoauszug, eidesstattliche Versicherung nach § 294 ZPO.
- **Fälligkeit**: Die Forderung muss im Zeitpunkt der Antragstellung bestehen und
 fällig sein. Eine bedingte oder gestundete Forderung genügt grundsätzlich nicht
 (Ausnahme: Stundung durch Druckausübung, Sittenwidrigkeit der Stundung).
- **Höhe**: Für das rechtliche Interesse keine gesetzliche Mindestgrenze; jedoch
 prüft das Gericht implizit, ob die Forderungshöhe im Verhältnis zur
 Verfahrenserwartung steht. Bagatellbeträge können das rechtliche Interesse in
 Frage stellen.

### Schritt 2 — Glaubhaftmachung des Eröffnungsgrundes

Aufbau eines Indizienpakets für Zahlungsunfähigkeit (§ 17 InsO):

| Indiz | Beweismittel |
|---|---|
| Fruchtlose Pfändungsversuche | Pfändungsprotokoll des GV (nicht älter als 3 Monate) |
| Lastschriftrückgaben | Kontoauszüge des Gläubigers (Stichwort "nicht eingelöst") |
| Wechselproteste | Notarprotokoll |
| SV-Rückstand ≥ 3 Monate | Kontoauszug Krankenkasse, Rückstandsbescheinigung |
| Lohnsteuerrückstände | ELSTER-Mahnbescheide, Rückstandsmitteilung FA |
| Negative BWA | Betriebswirtschaftliche Auswertung mit kumuliertem Negativsaldo |
| Häufung von Mahnverfahren | SCHUFA-Auskunft, Registerauskunft gerichtlicher Mahnbescheide |

Mindestens zwei bis drei dieser Indizien sollten kombiniert werden, um die Gesamtschau der überwiegenden Wahrscheinlichkeit der Zahlungsunfähigkeit zu tragen (st. BGH-Rspr.; konkrete Aktenzeichen vor Ausgabe über offene Quellen verifizieren).

### Schritt 3 — Antragsschrift formal (§§ 13, 14 InsO)

Zwingender Inhalt:
- Bezeichnung Gläubiger (vollständiger Name/Firma, Anschrift)
- Bezeichnung Schuldner (Firma, Sitz, Registergericht/HRB-Nr.)
- Darlegung des rechtlichen Interesses
- Darlegung und Glaubhaftmachung der Forderung mit Belegen
- Darlegung und Glaubhaftmachung des Eröffnungsgrundes mit Indizienbelegen
- Antrag auf Anordnung vorläufiger Sicherungsmaßnahmen (§§ 21, 22 InsO),
 falls eilbedürftig (z. B. drohende Vermögensverschiebungen)
- Kostenvorschuss (§ 26 InsO; wird bei Behörden oft erlassen)

### Schritt 4 — Reaktion auf Anhörung des Schuldners (§ 14 Abs. 2 InsO)

Das Insolvenzgericht hört den Schuldner vor der Entscheidung an. Typische
Schuldnerreaktionen und die rechtliche Bewertung:

- **Bestreiten der Forderung**: Substantiiertes Bestreiten hemmt nicht automatisch das Verfahren; bei titulierter oder durch starke Indizien glaubhaft gemachter Forderung bleibt der Antrag zulässig (vgl. BGH-Linie; Az. vor Ausgabe verifizieren).
- **Sofortige Zahlung der titulierten Forderung**: Beseitigt das rechtliche
 Interesse grundsätzlich, außer § 14 Abs. 1 S. 2 InsO greift (Zahlung innerhalb
 von 6 Monaten als potenzielle Anfechtungszahlung).
- **Zahlungsplan/Ratenzahlungsvereinbarung**: Kein Anspruch des Schuldners auf
 Aussetzung; missbräuchlicher Druckantrag-Einwand bei kurzfristiger Rücknahme nach Einlenken (Az. vor Ausgabe verifizieren).
- **Einreichung Sanierungskonzept**: Kein verfahrensrechtlicher Aufschubgrund;
 jedoch kann das Gericht faktisch zögern, wenn ein plausibles Sanierungskonzept
 vorgelegt wird.

### Schritt 5 — Schutzschrift / Einstweiliger Rechtsschutz (Schuldnerseite)

- **Schutzschrift**: Vor oder unmittelbar nach Anhörung beim Insolvenzgericht
 hinterlegen; Inhalt: Bestreiten der Forderung mit Belegen, Bestreiten des
 Eröffnungsgrundes (aktuelle Liquiditätsübersicht, ggf. IDW S 11-Stellungnahme),
 Druckantrag-Einwand falls zutreffend.
- **StaRUG-Verfahren**: Einleitung eines Restrukturierungsverfahrens nach StaRUG
 kann faktisch den Insolvenzantrag überlagern; Anzeige der Restrukturierungssache
 hat keine automatische Sperrwirkung gegen Gläubigeranträge, kann aber gerichtlich
 koordiniert werden.
- **Eigenantrag des Schuldners**: Strategisch oft günstiger als Abwehr — der
 Schuldner erhält das Vorschlagsrecht für den Insolvenzverwalter (§ 56a InsO),
 kann Eigenverwaltung beantragen (§§ 270 ff. InsO) und behält größeren Einfluss
 auf das Verfahren, als wenn der Gläubigerantrag zur Eröffnung führt.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Glaeubiger-Insolvenzantrag pruefend und Kurzgutachten erstellen | Kurzgutachten nach Pruefschema; Template unten |
| Variante A — Forderung noch nicht tituliert Antrag riskant | Titulierung zuerst; Insolvenzantrag nach Urteil oder Vollstreckungstitel |
| Variante B — Schuldner bietet Zahlung an wenn Antrag zurueckgenommen | Ruecknahme-Verhandlung pruefen; wirtschaftliches Ergebnis beachten |
| Variante C — Mehrere Glaeubiger koordinierter Antrag moeglich | Koordinierter Sammelantrag pruefen; Hauptglaeubiger bestimmen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Ausgabeformat

Strukturiertes Prüfungsmemo mit:
1. **Zulässigkeitsprüfung** (tabellarische Checkliste: Merkmal — Befund —
 Bewertung)
2. **Begründetheitsprüfung** (Indizienliste mit Beweismitteln und
 Bewertungsstärke)
3. **Handlungsempfehlung** (Gläubiger: Antragstellung ratsam/nicht ratsam;
 Schuldner: Abwehrmittel priorisiert nach Erfolgsaussicht)
4. **Formulierungsvorschlag** für den zentralen Antragssatz
5. **Quellen** (vollständige Zitierung aller herangezogenen Entscheidungen und
 Kommentarstellen)


## Beispiel

**Sachverhalt:**
Das Finanzamt München stellt beim AG München — Insolvenzgericht — einen
Gläubigerantrag gegen die Muster GmbH (HRB 123456 AG München). Rückständig:
57.000 EUR Lohnsteuer (Zeitraum Jan–Jun 2024) + 30.000 EUR Umsatzsteuer
(Q1 und Q2 2024) = 87.000 EUR gesamt. Bisherige Vollstreckungsmaßnahmen:
drei Pfändungsversuche des Vollziehungsbeamten, alle fruchtlos (Protokolle
vom 15.04., 03.06. und 18.07.2024). Zusätzlich: Mahnbescheid wegen USt
rechtskräftig seit 12.03.2024; BWA-Auszüge April–Juni 2024 zeigen
kumulierten negativen Cash-flow von −38.000 EUR.

**Prüfung:**

*Zulässigkeit:*
- Rechtliches Interesse (+): Das Finanzamt ist öffentlich-rechtlicher Gläubiger;
 sein Interesse an der Verfahrenseröffnung folgt aus der Insolvenzquotenchance
 und der Anfechtungsmöglichkeit nach §§ 129 ff. InsO für zurückliegende Zahlungen.
 Behördengläubiger, insbesondere Finanzämter und Sozialversicherungsträger, stellen
 häufig Gläubigeranträge; im FA-Bereich oft im Zusammenhang mit einer
 Strafanzeige nach § 266a StGB (Vorenthalten von SV-Beiträgen), was das
 behördliche Interesse weiter objektiviert.
- Forderung glaubhaft gemacht (+): Rechtskräftiger Mahnbescheid für USt-Forderung;
 Steuerbescheide für LSt-Rückstände; Höhe belegbar durch Steuerkonto-Auszug.
- Fälligkeit (+): Steuerliche Fälligkeit nach § 41a EStG (LSt) und § 18 UStG (USt)
 jeweils eingetreten und unstreitig.

*Begründetheit:*
Eröffnungsgrund § 17 InsO durch Indizienkombination glaubhaft gemacht (st. BGH-Linie; Az. vor Ausgabe verifizieren):
- Drei fruchtlose Pfändungsversuche (schwergewichtiges Indiz)
- Negative kumulierte BWA (strukturelle Unterdeckung)
- 6-monatiger Lohnsteuerausfall (laufende Zahlungsunfähigkeit gegenüber FA)
- Rechtskräftiger Mahnbescheid ohne Zahlung (fehlende Zahlungsbereitschaft/-fähigkeit)

**Ergebnis:** Antrag zulässig und begründet; Eröffnung nach § 27 InsO zu erwarten.

## Risiken und typische Fehler

### Gläubigerseite

1. **Unzureichende Glaubhaftmachung der Forderung**: Bloße Behauptung ohne Belege
 genügt nicht; eidesstattliche Versicherung allein bei nicht-titulierter Forderung
 führt regelmäßig zur Unzulässigkeit (st. BGH-Linie; Az. vor Ausgabe verifizieren).

2. **Fehlende Aktualität der Indizienmittel**: Pfändungsprotokolle älter als drei
 bis vier Monate verlieren an Überzeugungskraft; aktuellere Beweismittel sind
 nachzuliefern.

3. **Missbräuchlicher Druckantrag**: Ein Antrag, der erkennbar nur zur
 Druckausübung gestellt und nach Zahlung sofort zurückgenommen wird, kann als
 rechtsmissbräuchlich eingestuft werden und Schadensersatzansprüche des
 Schuldners auslösen (Az. der einschlägigen BGH-Entscheidungen vor Ausgabe über
 offene Quellen verifizieren). Prüfen: hat der Mandant ein echtes
 Eröffnungsinteresse oder nur ein Zahlungsinteresse?

4. **§ 14 Abs. 1 S. 2 InsO — Taktikzahlung übersehen**: Befriedigt der Schuldner
 den antragstellenden Gläubiger kurz nach Antragstellung innerhalb der
 6-Monatsfrist, bleibt das Antragsrecht bestehen, wenn die Zahlung
 anfechtbar ist. Gläubiger darf Antrag bei anfechtbarer Befriedigung
 aufrechterhalten.

### Schuldnerseite

5. **Sofortige Zahlung als Anfechtungsrisiko**: Zahlt der Schuldner die
 antragsbegründende Forderung kurzfristig, um den Antrag zu Fall zu bringen,
 ist diese Zahlung nach § 133 Abs. 1 InsO (Vorsatzanfechtung) oder § 131 InsO
 (inkongruente Deckung) anfechtbar, wenn innerhalb der Anfechtungsfristen
 Insolvenz eröffnet wird. Der Schuldner "kauft" sich damit nur Zeit, ohne die
 Insolvenzlage zu beseitigen.

6. **Eigeninteresse vs. Gemeininteresse**: Der Gläubigerantrag dient nicht nur
 dem individuellen Gläubigerinteresse, sondern dem Schutz der
 Gläubigergesamtheit. Dies schränkt die Missbrauchsrechtsprechung auf klare
 Einzelfälle ein; der bloße Verdacht missbräuchlicher Motive genügt nicht.

7. **Zu späte Eigenantragsstellung**: Wartet der Schuldner zu lang mit dem
 Eigenantrag, verliert er das Vorschlagsrecht nach § 56a InsO und riskiert
 zudem eine persönliche Haftung der Geschäftsführer nach § 15a InsO
 (Insolvenzverschleppungshaftung).

8. **StaRUG-Verfahren ohne Sperrwirkung**: Das StaRUG-Restrukturierungsverfahren
 sperrt Gläubigeranträge nicht automatisch. Ohne gerichtliche Anordnung nach
 § 29 Abs. 2 Nr. 1 StaRUG bleibt der Gläubigerantrag vollständig wirksam.

## Quellenpflicht

Jede Handlungsempfehlung ist mit mindestens einer der nachstehenden Quellen
zu belegen. Pinpoint-Angaben (Randnummer) sind Pflicht.

| Quelle | Fundstelle |
|---|---|
| BGH IX. Zivilsenat zur Glaubhaftmachung der Forderung iSd § 14 InsO | Az., Datum, Randnummer vor Ausgabe über dejure.org / openjur.de verifizieren |
| BGH IX. Zivilsenat zur Indizienlinie der Zahlungseinstellung § 17 Abs. 2 S. 2 InsO | Az. vor Ausgabe verifizieren |
| BGH IX. Zivilsenat zum missbräuchlichen Druckantrag und rechtlichen Interesse | Az. vor Ausgabe verifizieren |
| Literatur (Kommentare, Handbücher) | nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle |
| IDW S 11 (Stand 2017) | Tz. 15–42 (Zahlungsunfähigkeit), Tz. 43–71 (Überschuldung) |

---

*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*


## Triage — Glaeubigerantrag

Bevor losgelegt wird, klaere:

1. **Forderung vollstreckbar?** Titel oder Glaubhaftmachung § 14 Abs. 1 InsO; eidesstattliche Versicherung ausreichend.
2. **Eröffnungsgrund glaubhaft?** Mindestens 2-3 Indizien für Zahlungsunfähigkeit iSd § 17 Abs. 2 S. 2 InsO oder Überschuldungsstatus iSd § 19 InsO.
3. **Rechtliches Interesse aktuell?** Kein missbräuchlicher Druckantrag; echtes Eröffnungsinteresse zum Zeitpunkt der gerichtlichen Entscheidung erforderlich.
4. **Sicherungsantrag § 21 InsO?** Sofort-Massnahmen bei Vermoegensgefaehrdung beantragen?
5. **Kostenvorschuss § 26 InsO?** Glaeubigerinteresse an Verfahren trotz Massearmut?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template Kurzgutachten Glaeubigerantrag

**Adressat:** Mandant (Glaeubiger) — Tonfall: sachlich-empfehlend

```
INTERNES GUTACHTEN — GLAEUBIGERANTRAG § 14 InsO
Datum: [DATUM] Mandant: [GLAEUBIGER] Schuldner: [SCHULDNER]

ERGEBNIS: Glaeubigerantrag [SINNVOLL / NICHT SINNVOLL]

BEGRUENDUNG:
Forderung: EUR [BETRAG], Faelligkeit [DATUM], Vollstreckbarkeit [JA/NEIN]
ZU-Nachweis: [Indizien aufzaehlen]
Rechtsschutzbeduernis: [Beurteilung]
Sicherungsantrag § 21 InsO: [EMPFOHLEN weil ...]
Kostenvorschuss: EUR [BETRAG] ggf. erforderlich (§ 26 InsO)

NAECHSTER SCHRITT: [Antrag einreichen bis DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 2. `glaeubigerausschuss-mitwirkung`

**Fokus:** Mandant ist Mitglied des Gläubiger-ausschusses oder soll in den Ausschuss gewählt werden und fragt nach Rechten Pflichten und Haftung. Prüfraster §§ 67 ff. InsO Gläubigerausschuss vorlaeufiger Gläubigerausschuss § 22a InsO Schwellenwerte. Aufgaben Überwachung Insolvenzverwalter Beschlussfassung wesentliche Verwertungs-Entscheidungen Verguetungsprüfung. Rechte Akteneinsicht Anhoerung Beschlussantrag Kassen-Prüfung Haftung § 71 InsO. Output Ausschuss-Arbeitsmemo mit Checkliste laufender Pflichten und Risiko-Hinweisen. Abgrenzung: gläubigerantrag-prüfung für Eroefffnungsantrag des Gläubiger.

# Gläubigerausschuss-Mitwirkung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gläubigerausschuss-Mitwirkung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Der Gläubigerausschuss ist das wichtigste Mitwirkungs-Organ der Gläubiger im Insolvenzverfahren — Überwachung des Verwalters und wichtigste Entscheidungen.

## Schritt 1 — Bestellung

### Endgültiger Gläubigerausschuss § 67 InsO

- **Bestellung durch Gläubigerversammlung** im Berichtstermin
- **Mitglieder** Vertreter unterschiedlicher Gläubiger-Gruppen (gesicherte/ungesicherte Gläubiger Arbeitnehmer Lieferanten Finanzamt)
- **Zahl** typisch drei bis sieben

### Vorläufiger Gläubigerausschuss § 22a InsO

- **Schon im Eröffnungsverfahren** durch Insolvenzgericht bestellt
- Pflicht bei größeren Unternehmen
 - **§ 22a Abs. 1 InsO** Bilanzsumme mehr als sechs Millionen Euro
 - oder Umsatz mehr als zwölf Millionen Euro
 - oder Mitarbeiter mehr als fünfzig
- **Antrag** beim Insolvenzgericht möglich
- **Eilbestellung** bei Eröffnungsantrag

### Mitgliederschaft

- Bereitschafts-Erklärung
- Gläubiger-Eigenschaft

## Schritt 2 — Aufgaben

### Überwachung Insolvenzverwalter § 69 InsO

- **Kassenprüfung** Aufzeichnungen Belege
- **Quartalsbericht** Verwalter
- **Berichts-Verlangen**

### Beschlussfassung über wichtige Verwalter-Entscheidungen

- **Veräußerung wesentlicher Vermögensgegenstände** § 160 Abs. 2 InsO
- **Stilllegung** Geschäftsbetrieb
- **Aufnahme oder Fortführung** wesentlicher Vertrags-Beziehungen
- **Personalmaßnahmen** in größeren Konstellationen
- **Vergleiche** mit größerem Volumen

### Vergütungsprüfung § 73 Abs. 1 InsO

- Verwalter-Vergütungs-Antrag nach InsVV
- Stellungnahme an Insolvenzgericht

### Gläubiger-Interessen-Vertretung

- Im Berichts-Termin
- In Gläubigerversammlung

## Schritt 3 — Rechte

### Akteneinsicht

- Vollumfänglich in Insolvenz-Akten
- Verwalter-Akten

### Anhörung

- Vor wesentlichen Beschlüssen
- Bei Verfügung über wesentliche Vermögensgegenstände

### Beschlussantrag

- Im Gläubigerausschuss
- An Gericht

### Verwalter-Abberufung

- Antrag bei wichtigem Grund § 59 InsO

## Schritt 4 — Pflichten und Haftung § 71 InsO

### Gewissenhafte Aufgabenwahrnehmung

- **Sorgfalt eines ordentlichen Geschäftsmanns**
- **Treuepflicht** gegenüber Gläubiger-Gesamtheit
- **Verschwiegenheits-Pflicht** gegenüber Dritten

### Haftung

- **Gegenüber Gläubigern und Insolvenzmasse**
- **Bei Pflichtverletzung** Schadensersatz
- **Mehrere Mitglieder** gesamtschuldnerisch

### D&O-Versicherung

- Häufig vom Mandanten als Mitglied vorgesehen
- Bei großen Unternehmen Standard

## Schritt 5 — Vergütung Mitglieder § 73 Abs. 1 InsO

- **Angemessene Vergütung** nach InsVV
- **Auslagen-Ersatz**
- Aus Insolvenzmasse

## Schritt 6 — Beschluss-Verfahren

### Beschlussfähigkeit

- Mehrheit der Mitglieder anwesend / vertreten

### Beschluss

- **Einfache Mehrheit** der Anwesenden
- Bei Stimmen-Gleichheit Stimme des Vorsitzenden

### Protokoll

- Schriftlich
- Bei wichtigen Beschlüssen Begründung

## Schritt 7 — Strategische Aspekte für Mitglied

### Aktive Mitwirkung

- **Regelmäßige Berichts-Anforderung** Verwalter
- **Kassen-Prüfung** alle drei bis sechs Monate
- **Beteiligung an wichtigen Entscheidungen**
- **Frage-Stellung**

### Konflikt mit Verwalter

- Bei Pflichtverletzung Antrag Abberufung
- Bei Schadensersatz-Ansprüchen Geltendmachung Gläubigerversammlung

### Konflikt im Gläubigerausschuss

- Bei systematischen Konflikten Rücktritts-Erklärung
- Ggf. neue Bestellung durch Gläubigerversammlung

## Schritt 8 — Spezielle Konstellationen

### Eigenverwaltung § 270 ff. InsO

- Gläubigerausschuss mit erhöhter Bedeutung
- Sachwalter überwacht
- Bei Schutzschirm § 270d InsO

### Konzern-Insolvenz § 269a ff. InsO

- Konzern-Gläubigerausschuss-Optionen
- Koordination

### StaRUG-Verfahren

- **Restrukturierungs-Beauftragter** statt Insolvenzverwalter
- **Restrukturierungs-Plan-Abstimmung** durch Gläubiger-Gruppen
- Andere Logik als InsO

## Schritt 9 — Berichtstermin § 156 InsO

- **Verwalter berichtet** über Vermögens-Stand, mögliche Sanierungs-Wege
- **Gläubiger entscheidet** über Fortführung Stilllegung
- **Gläubigerausschuss** vor entscheidet vor Versammlung

## Schritt 10 — Prüfungs-Termin § 175 InsO

- **Forderungs-Tabellen-Prüfung**
- **Bestreitungen** der Verwalter
- **Klageweg** für streitige Forderungen § 179 InsO

## Schritt 11 — Wahrnehmung als Anwalt für Mitglied

- **Vorbereitungs-Briefing** mit Mandant vor Sitzung
- **Aktenstudium** Verwalter-Bericht
- **Beschluss-Empfehlung** schriftlich
- **Bei Sitzung-Anwesenheit** Stimm-Vorbereitung

## Schritt 12 — Sonderpflichten Vorsitzende

- **Einladung** zur Sitzung
- **Tages-Ordnung** vorbereiten
- **Protokoll-Verantwortung**
- **Außenvertretung** des Ausschusses

## Checkliste vor Sitzung

- Sitzungs-Termin
- Tages-Ordnung
- Verwalter-Berichte gelesen
- Sachverhalts-Komplex verstanden
- Argumentations-Linie vorbereitet
- Beschluss-Vorschlag formuliert
- Stellvertreter bei Verhinderung

## Ausgabe

- `glaeubigerausschuss-mitwirkung-{az}.md`
- Sitzungs-Vorbereitungs-Memo
- Beschluss-Vorschlag-Entwurf
- Frist im Fristenbuch (Sitzungs-Termine)
- Bei Konflikt: Strategie-Memo

## Quellen

- InsO §§ 22a 59 67–73 156 160 175 270 270d
- StaRUG
- InsVV
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- HK-InsO


## Aktuelle Leitentscheidungen — Glaeubigerausschuss (Stand Mai 2026)

- Konkrete BGH/LG-Linien zu Haftung und Pflichten des Gläubigerausschusses (§§ 67–73, 160 InsO), insbesondere zur Mitwirkung bei bedeutenden Massnahmen, vor Ausgabe über dejure.org / openjur.de mit Datum und Aktenzeichen verifizieren.
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Bei AG-Insolvenzen mit großem Aktionärsanteil: Aktionärsforderungen sind nachrangig; Auswirkungen auf Stimmrechtsausübung und Ausschussbesetzung beachten.

## Paragrafenkette Glaeubigerausschuss

§ 67 InsO (Einsetzung) → § 68 InsO (Mitglieder) → § 69 InsO (Pflichten und Rechte) → § 70 InsO (Entlassung) → § 71 InsO (Haftung) → § 72 InsO (Verguetung) → § 73 InsO (Verguetung) → § 160 InsO (besonders bedeutsame Rechtshandlungen)

## Triage — Glaeubigerausschuss

Bevor losgelegt wird, klaere:
1. **Ausschuss obligatorisch?** § 67 Abs. 2 InsO: bei grossen Verfahren (>250 AN, >6 Mio. EUR Bilanzsumme oder >12 Mio. EUR Umsatz) ist vorlaeufiger Ausschuss zwingend.
2. **Zustimmungspflicht § 160 InsO?** Welche Geschaefte benoetigen Ausschuss-Zustimmung (Betriebsveraesserung, ungewoehnlich hohe Verbindlichkeiten, Rechtsstreitigkeiten ueber EUR 10.000)?
3. **Interessenkonflikt?** Ausschussmitglied ist gleichzeitig Glaeubiger und Bieter in Verwertung → § 71 InsO Haftungsrisiko.
4. **Informations-Hol-Pflicht?** Mitglieder muessen aktiv Informationen vom IV anfordern; passives Warten genuegt nicht.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `inso-dsgvo-art17-nach-restschuldbefreiung`

**Fokus:** Art. 17 DSGVO als insolvenzrechtlicher Anschlussanspruch nach Restschuldbefreiung: Löschung, Einschränkung, Widerspruch, Beschwerde und Klage.

# DSGVO Art. 17 nach Restschuldbefreiung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DSGVO Art. 17 nach Restschuldbefreiung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Einsatz

Für Schuldnerberatung und Anwälte, die den wirtschaftlichen fresh start tatsächlich durchsetzen wollen.

## Norm- und Quellenanker

DSGVO Art. 17, 18, 21, 77, 79; InsO §§ 300, 301; EuGH C-26/22/C-64/22.

## Arbeitsfragen

1. Welche Daten sind für wen noch erforderlich?
2. Welche Rechtsgrundlage behauptet Verantwortlicher?
3. Welche Nachteile lassen sich dokumentieren?

## Output

Art.-17-Prüfung mit Interessenabwägung und Beschwerde-/Klageentwurf.

## Red Flags

- Löschung zu früh/zu pauschal verlangt
- berechtigte Altforderung nicht getrennt
- Empfängerliste fehlt

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 4. `inso-eroeffnungsantrag-checkliste`

**Fokus:** Checkliste Eroeffnungsantrag § 13 InsO: zustaendiges Gericht, Glaeubigerliste, Vermoegensverzeichnis, Erklaerung Geschaeftsleitung. Pruefraster fuer Schuldner- und Glaeubigeranwalt.

# Inso: Eroeffnungsantrag-Checkliste

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Inso: Eroeffnungsantrag-Checkliste` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Inso: Eroeffnungsantrag-Checkliste
- **Spezialgegenstand:** Inso: Eroeffnungsantrag-Checkliste / inso eroeffnungsantrag checkliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
