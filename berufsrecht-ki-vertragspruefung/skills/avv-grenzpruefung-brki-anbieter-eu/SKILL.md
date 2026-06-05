---
name: avv-grenzpruefung-brki-anbieter-eu
description: "Avv Grenzpruefung Datenschutz, Brki Anbieter Due Diligence, Brki Eu Us Dpf Transferpruefung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Avv Grenzpruefung Datenschutz, Brki Anbieter Due Diligence, Brki Eu Us Dpf Transferpruefung

## Arbeitsbereich

Dieser Skill bündelt **Avv Grenzpruefung Datenschutz, Brki Anbieter Due Diligence, Brki Eu Us Dpf Transferpruefung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `avv-grenzpruefung-datenschutz` | Kanzlei nutzt KI-Dienstleister und prüft ob AVV nach Art. 28 DSGVO die berufsrechtliche Prüfung ersetzt. Berufsrecht laeuft parallel und ist strenger als Datenschutzrecht. Normen Art. 28 DSGVO §§ 43e BRAO 62a StBerG. Prüfraster AVV-Prüfpunkte Berufsrecht-Parallelitaet Abgrenzungspunkte Stolperfallen. Output Parallelprüfungs-Vermerk Lückenliste. Abgrenzung zu verschwiegenheitsklausel-prüfen (Verschwiegenheit-Hauptprüfung) und gutachten-erstellen (Gesamtgutachten). |
| `brki-anbieter-due-diligence` | Anbieter-Due-Diligence beim Einsatz von KI in der Kanzlei: Sitz, Rechtsform, Zertifizierungen (ISO 27001, SOC 2 Typ II), Datenhaltung, Subunternehmer, Auditierbarkeit, Datenschutz-Folgenabschaetzung. Strukturierte Bewertung mit Score je Kategorie. |
| `brki-eu-us-dpf-transferpruefung` | Spezialfall Transfer nach USA unter EU-US-Data-Privacy-Framework DPF: Liste teilnehmender Unternehmen, Pruefraster fuer Wirksamkeit (Selbstzertifizierung, Annual-Recertification), Backup-Plan SCC Modul 2 plus TIA bei Verlust DPF. |

## Arbeitsweg

Für **Avv Grenzpruefung Datenschutz, Brki Anbieter Due Diligence, Brki Eu Us Dpf Transferpruefung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `berufsrecht-ki-vertragspruefung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `avv-grenzpruefung-datenschutz`

**Fokus:** Kanzlei nutzt KI-Dienstleister und prüft ob AVV nach Art. 28 DSGVO die berufsrechtliche Prüfung ersetzt. Berufsrecht laeuft parallel und ist strenger als Datenschutzrecht. Normen Art. 28 DSGVO §§ 43e BRAO 62a StBerG. Prüfraster AVV-Prüfpunkte Berufsrecht-Parallelitaet Abgrenzungspunkte Stolperfallen. Output Parallelprüfungs-Vermerk Lückenliste. Abgrenzung zu verschwiegenheitsklausel-prüfen (Verschwiegenheit-Hauptprüfung) und gutachten-erstellen (Gesamtgutachten).

# AVV-Grenzprüfung Datenschutz

## Fachkern: AVV-Grenzprüfung Datenschutz

- **KI-/Berufsrechtsproblem (AVV-Grenzprüfung Datenschutz):** Kanzlei nutzt KI-Dienstleister und prüft ob AVV nach Art. 28 DSGVO die berufsrechtliche Prüfung ersetzt. Berufsrecht laeuft parallel und ist strenger als Datenschutzrecht. Normen Art. 28 DSGVO §§ 43e BRAO 62a StBerG. Prüfraster AVV-Prüfpunkte Berufsrecht-Parallelitaet Abgrenzungspunkte Stolperfallen. Output Parallelprüfungs-Vermerk Lückenliste. Abgrenzung zu verschwiegenheitsklausel-prüfen (Verschwiegenheit-Hauptprüfung) und gutachten-erstellen (Gesamtgutachten).
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Triage zu Beginn — kläre vor der Prüfung

1. Liegt überhaupt eine AVV nach Art. 28 DSGVO vor? (Vertragsdokument, Datum, Unterzeichnung)
2. Verarbeitet der Anbieter personenbezogene Daten — oder nur nicht-personenbezogene Geheimnisse (Strategiedokumente, anonymisierte Vertragsanalyse)?
3. Welcher Berufsträger ist betroffen (Rechtsanwalt, Steuerberater, Notar)? Norm-Adapter festlegen.
4. Handelt es sich um Kanzleiinfrastruktur oder ein Einzelmandats-Tool (§ 26a Abs. 4 BNotO: Sonderfall)?
5. Sind die parallelen Prüfbereiche (Verschwiegenheit, Belehrung §§ 203/204 StGB, Subunternehmer) bereits separat abgearbeitet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zweck dieser Skill

Diese Skill ist bewusst eine **Grenzprüfung**, keine vertiefte Datenschutzprüfung. Das Plugin behandelt das Berufsrecht und das Strafrecht. Die datenschutzrechtliche Prüfung ist eine eigene, parallele Aufgabe — sie wird häufig mit der berufsrechtlichen Prüfung verwechselt oder vermischt.

Das Plugin `datenschutzrecht` im selben Repository deckt diese Prüfung ab.

## Was die AVV regelt — und was nicht

Die Auftragsverarbeitungsvereinbarung nach Art. 28 DSGVO regelt die Verarbeitung personenbezogener Daten. Sie regelt:

- Gegenstand, Dauer, Art und Zweck der Verarbeitung
- Kategorien betroffener Personen und Datenarten
- Pflichten und Rechte des Verantwortlichen
- Weisungsbindung des Auftragsverarbeiters
- TOM (Art. 32 DSGVO)
- Unterauftragnehmer (Art. 28 Abs. 4 DSGVO)
- Mitwirkungspflichten
- Löschung am Vertragsende

Die AVV regelt **nicht** das Berufsgeheimnis. Sie schützt nicht die Verschwiegenheit als solche, sondern den personenbezogenen Datenschutz. Beide Schutzregimes laufen parallel.

## Zentrale Normen

- **Art. 28 DSGVO** — Auftragsverarbeitung: Pflicht zur AVV, Mindestinhalt, Unterauftragnehmer-Klausel
- **Art. 32 DSGVO** — Technische und organisatorische Maßnahmen
- **Art. 83 Abs. 4 DSGVO** — Bußgeld bis 10 Mio. EUR oder 2 % Jahresumsatz bei Verstoß gegen Art. 28
- **§§ 43e BRAO, 62a StBerG, 50a WPO, 39c PAO, 26a BNotO** — Berufsrecht läuft parallel
- **§§ 203, 204 StGB** — Strafrecht: Verschwiegenheitspflicht als Straftatbestand

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Was das Berufsrecht zusätzlich verlangt

Die berufsrechtliche Dienstleisterregelung (§§ 43e BRAO, 62a StBerG, 50a WPO, 39c PAO, 26a BNotO) verlangt darüber hinaus:

- Verschwiegenheitspflicht in Textform — auch wenn keine personenbezogenen Daten verarbeitet werden (z.B. anonymisierte Vertragsanalyse)
- Strafrechtliche Belehrung (§§ 203, 204 StGB)
- Festlegung Subunternehmer mit berufsrechtlicher (nicht datenschutzrechtlicher) Weiterverpflichtung
- Beachtung des § 203 Abs. 4 Satz 2 Nr. 1 StGB (Sekundärpflicht)

## Entscheidungsbaum

```
AVV vorhanden?
 Nein → DSGVO-Verstoß bei personenbezogenen Daten; separate Meldung nötig
 Ja → Inhalt nach Art. 28 Abs. 3 DSGVO vollständig?
 Nein → Lücken dokumentieren; Rückfragebrief
 Ja → Berufsrechtliche Verschwiegenheitsverpflichtung separat?
 Nein → Muss separat/zusätzlich vereinbart werden
 Ja → Strafrechtliche Belehrung §§ 203/204 StGB enthalten?
 Nein → Ergänzungsklausel erforderlich
 Ja → GRÜN: AVV-Prüfung abgeschlossen; Berufsrecht separat OK
```

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


| Punkt | Status | Bemerkung |
|---|---|---|
| AVV nach Art. 28 DSGVO liegt vor | | |
| Aktueller Stand (Datum, Version) | | |
| Datenkategorien sind beschrieben | | |
| TOM nach Art. 32 DSGVO (Anlage) | | |
| Subunternehmer nach Art. 28 Abs. 4 DSGVO (Anlage) | | |
| Drittlandsübermittlung geregelt (SCC, Adequacy) | | |
| Verweis auf Berufsrecht im Vertrag | | |
| Verschwiegenheitsverpflichtung separat | | |
| Strafrechtliche Belehrung §§ 203/204 StGB | | |

## Typische Stolperfallen

- Anbieter argumentiert, die AVV decke alles ab — sie deckt das Berufsrecht nicht ab
- AVV verweist auf US-Datenschutzstandards — DSGVO-konform fraglich
- Pseudonymisierung wird angepriesen als "berufsrechtlich notwendig" — sie ist es nach DAV S. 11 nicht
- Trennung von Verschwiegenheit und Datenschutz fehlt
- Berufsrechtliche Verpflichtung in der AVV "versteckt" — sollte eigenständig erfolgen

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — AVV-Grenzfall pruefen ob AV oder gemeinsame Verantwortlichkeit | Pruefschema unten; Template fuer Ergebnis-Memo |
| Variante A — AVV eindeutig erforderlich | Direkt zu AVV-Erstellung (skill avv-pruefung) wechseln |
| Variante B — gemeinsame Verantwortlichkeit wahrscheinlich | Art. 26 DSGVO Vereinbarung statt AVV; Template anpassen |
| Variante C — kein Auftragsverhaeltnis sondern eigenstaendige Verarbeitung | Keine AVV; separate Datenschutzvereinbarung pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Parallelpruefungs-Vermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Interner Compliance-Vermerk — Schnittstelle AVV/Berufsrecht
Datum: [DATUM]
Anbieter: [NAME ANBIETER]
Produkt: [PRODUKTNAME]
Berufsgruppe: [BERUF]

A) AVV-Befund (Art. 28 DSGVO)
AVV vorhanden: ja / nein
Inhalt vollstaendig: ja / teilweise / nein
Luecken: [BESCHREIBUNG]

B) Berufsrechtlicher Befund (§§ 43e BRAO / 62a StBerG / ...)
Verschwiegenheitsklausel in Textform: ja / nein
Strafrechtliche Belehrung §§ 203/204 StGB: ja / nein
Subunternehmer-Weiterverpflichtung: ja / nein

C) Ergebnis
AVV-Status: GRUEN / GELB / ROT
Berufsrecht-Status: GRUEN / GELB / ROT
Empfehlung: [Vertragsnutzung freigegeben / Nachverhandlung / Ablehnung]

Unterschrift: [SACHBEARBEITER]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 36/20 (claimed: Berufsgeheimnis §43a BRAO, NJW 2021, 1008): NOT_FOUND auf dejure.org. NJW 2021, 1008 gehoert zu BGH VIII ZR 78/20 (Gebrauchtwagenhandel/Verjaehnungsfrist) – thematisch unverwandt. Eintrag geloescht. -->

## 2. `brki-anbieter-due-diligence`

**Fokus:** Anbieter-Due-Diligence beim Einsatz von KI in der Kanzlei: Sitz, Rechtsform, Zertifizierungen (ISO 27001, SOC 2 Typ II), Datenhaltung, Subunternehmer, Auditierbarkeit, Datenschutz-Folgenabschaetzung. Strukturierte Bewertung mit Score je Kategorie.

# BRKI: Anbieter-Due-Diligence

## Spezialwissen: BRKI: Anbieter-Due-Diligence
- **Spezialgegenstand:** BRKI: Anbieter-Due-Diligence / brki anbieter due diligence. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, ISO, SOC, II, BRKI.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `berufsrecht-ki-vertragspruefung`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `brki-eu-us-dpf-transferpruefung`

**Fokus:** Spezialfall Transfer nach USA unter EU-US-Data-Privacy-Framework DPF: Liste teilnehmender Unternehmen, Pruefraster fuer Wirksamkeit (Selbstzertifizierung, Annual-Recertification), Backup-Plan SCC Modul 2 plus TIA bei Verlust DPF.

# BRKI: EU-US-DPF Transfer

## Spezialwissen: BRKI: EU-US-DPF Transfer
- **Spezialgegenstand:** BRKI: EU-US-DPF Transfer / brki eu us dpf transferpruefung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** USA, EU, US, DPF, SCC, TIA, BRKI.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `berufsrecht-ki-vertragspruefung`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
