---
name: geschgehg-halluzinations-handhabung-kanzlei
description: "Geschgehg Halluzinations Handhabung Kanzlei: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geschgehg Halluzinations Handhabung Kanzlei

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geschgehg Halluzinations Handhabung Kanzlei** im Plugin KI-Richtlinie für Kanzleien. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geschgehg-bausteine` | GeschGehG-Bausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei muss beim KI-Einsatz Geschäftsgeheimnisse von Mandanten und eigene Kanzleiinformationen schützen. § 1 Abs. 3 Nr. 1 GeschGehG angemessene Geheimhaltungsmassnahmen, § 203 StGB Berufsgeheimnis, §§ 43a und 43e BRAO. Prüfraster Geheimnisqualifikation der Mandatsinformationen, angemessene technische Massnahmen, Vertragspflichten für KI-Dienstleister. Output GeschGehG-Bausteine für KI-Richtlinie mit konkreten Formulierungen. Abgrenzung zu Berufsrecht-Bausteine und zu Musterklauseln-IT. |
| `halluzinations-handhabung` | Halluzinationen von KI in juristischer Arbeit erkennen und Prozessbetrug vermeiden: Anwendungsfall Anwalt nutzt KI für Rechtsprechungs-Recherche und muss sicherstellen dass keine falschen Fundstellen in Schriftsatz oder Gutachten einfliessen. OLG Koblenz Haftung Halluzination, AG Köln 02.07.2025, § 43 BRAO Sorgfaltspflicht. Prüfraster Pflicht zur Quellenverifizierung jedes KI-Zitats, Vier-Augen-Prinzip für Schriftsaetze, Dokumentation der Prüfung. Output Prüfprotokoll-Vorlage für KI-Zitate mit Verifikations-Checkliste. Abgrenzung zu Prompting-Leitfaden und zu Compliance-Regelsatz. |
| `kanzlei-kontext-analyse` | Kanzlei-Kontext erfassen für massgeschneiderte KI-Nutzungsrichtlinie: Anwendungsfall vor Erstellung einer KI-Richtlinie muss Groesse Rechtsgebiete Mandantenstruktur IT-Infrastruktur und Syndikus-Inhouse-Besonderheiten des Mandanten analysiert werden. § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz, DSGVO Datenschutzbeauftragter. Prüfraster Kanzleigroesse, Rechtsgebiete mit Hochrisiko-Potential, internationale Mandate, bestehende Tools, Tailoring-Bedarf. Output Kanzlei-Kontext-Profil als Grundlage für Richtlinien-Erstellung. Abgrenzung zu Richtlinien-Skelett-Erzeugen und zu Compliance-Regelsatz. |

## Arbeitsweg

Im Plugin KI-Richtlinie für Kanzleien gilt für **Geschgehg Halluzinations Handhabung Kanzlei**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geschgehg-bausteine`

**Fokus:** GeschGehG-Bausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei muss beim KI-Einsatz Geschäftsgeheimnisse von Mandanten und eigene Kanzleiinformationen schützen. § 1 Abs. 3 Nr. 1 GeschGehG angemessene Geheimhaltungsmassnahmen, § 203 StGB Berufsgeheimnis, §§ 43a und 43e BRAO. Prüfraster Geheimnisqualifikation der Mandatsinformationen, angemessene technische Massnahmen, Vertragspflichten für KI-Dienstleister. Output GeschGehG-Bausteine für KI-Richtlinie mit konkreten Formulierungen. Abgrenzung zu Berufsrecht-Bausteine und zu Musterklauseln-IT.

# GeschGehG-Bausteine

Das Gesetz zum Schutz von Geschäftsgeheimnissen (GeschGehG) ergänzt das anwaltliche Berufsrecht und das Datenschutzrecht um einen spezifischen zivilrechtlichen Geheimnisschutz. Beim Einsatz von KI-Systemen in Kanzleien ist das GeschGehG relevant, wenn vertrauliche Mandatsinformationen, die als Geschäftsgeheimnis qualifizieren, an externe KI-Dienstleister übermittelt werden.

## Rechtlicher Hintergrund

§ 2 Nr. 1 GeschGehG: Definition des Geschäftsgeheimnisses — vertrauliche Information mit wirtschaftlichem Wert, für die angemessene Geheimhaltungsmaßnahmen getroffen wurden. § 1 Abs. 3 Nr. 1 GeschGehG: Das GeschGehG lässt berufs- und strafrechtliche Vorschriften unberührt — § 203 StGB und §§ 43a, 43e BRAO bleiben vorrangig. § 4 GeschGehG: Verbotene Handlungen — Erlangung, Nutzung und Offenlegung ohne Zustimmung. § 10 GeschGehG: Schadensersatzansprüche. Richtlinie (EU) 2016/943 (Trade Secrets Directive) als unionsrechtliche Grundlage.

## Vorgehen

1. **Qualifikation als Geschäftsgeheimnis prüfen**: Nicht jede Mandatsinformation ist automatisch ein Geschäftsgeheimnis im Sinne des GeschGehG. Voraussetzung sind wirtschaftlicher Wert und aktive Geheimhaltungsmaßnahmen.
2. **Angemessene Schutzmaßnahmen definieren**: Die Kanzlei muss darlegen können, welche Maßnahmen sie zum Schutz der Informationen ergriffen hat (Zugangsbeschränkungen, Verschlüsselung, vertragliche Pflichten).
3. **Vorrang des Berufsrechts beachten**: § 1 Abs. 3 Nr. 1 GeschGehG stellt klar, dass das GeschGehG das Berufsrecht nicht verdrängt — die strengeren Anforderungen der §§ 43a, 43e BRAO und § 203 StGB bleiben maßgeblich.
4. **Mandanten informieren**: Bevor KI-Systeme für die Bearbeitung mandantenbezogener Informationen eingesetzt werden, die potenzielle Geschäftsgeheimnisse des Mandanten darstellen, ist die Zustimmung des Mandanten einzuholen. Nach der Offenlegung kann der Schutz erloschen sein.
5. **Vertragliche Absicherung mit KI-Dienstleistern**: Der Dienstleister muss zur Verschwiegenheit verpflichtet sein; § 43e-BRAO-Vertrag erfüllt diese Anforderung zugleich (vgl. Skill `musterklauseln-it-vertrag`).

## Vorlagentext / Bausteine

**Baustein Geschäftsgeheimnisschutz:**
Vertrauliche Informationen von Mandanten, die als Geschäftsgeheimnisse im Sinne des § 2 Nr. 1 GeschGehG qualifizieren, dürfen nur mit Zustimmung des Mandanten in KI-Systeme eingegeben werden. Die Kanzlei ergreift angemessene Schutzmaßnahmen im Sinne des GeschGehG: Zugangsbeschränkungen zu KI-Systemen auf autorisiertes Personal, vertragliche Verschwiegenheitspflichten gegenüber KI-Dienstleistern sowie Dokumentation der getroffenen Maßnahmen.

**Baustein Verhältnis zu § 203 StGB:**
Der berufs- und strafrechtliche Schutz nach § 203 StGB bleibt nach § 1 Abs. 3 Nr. 1 GeschGehG von den Regelungen des GeschGehG unberührt. In der anwaltlichen Praxis überlagert § 203 StGB in Verbindung mit §§ 43a, 43e BRAO den Schutz des GeschGehG vollständig. Die Einhaltung der berufsrechtlichen Anforderungen stellt zugleich sicher, dass auch die Anforderungen des GeschGehG erfüllt sind.

**Baustein Mandanteninformation:**
Mandanten sind vor dem Einsatz von KI-Systemen für die Bearbeitung ihrer Angelegenheiten darauf hinzuweisen, wenn dabei Informationen, die Geschäftsgeheimnisse des Mandanten darstellen könnten, an KI-Dienstleister übermittelt werden. Die Zustimmung des Mandanten ist einzuholen, bevor der Schutz durch eine (auch versehentliche) Offenlegung erlischt.

## Hinweise zur Aktualisierung

Das GeschGehG ist ein vergleichsweise junges Gesetz (in Kraft seit 26. April 2019), das sich in der Rechtsprechung noch weiter konturiert. Neue Entscheidungen des BGH oder der Oberlandesgerichte zum GeschGehG im Kontext digitaler Dienstleistungen sind zu beobachten und ggf. in die Richtlinie einzuarbeiten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 1 GeschGehG — Anwendungsbereich
- § 2 Nr. 1 GeschGehG — Definition Geschaeftsgeheimnis (angemessene Geheimhaltungsmassnahmen)
- § 4 GeschGehG — Handlungsverbote (unbefugte Nutzung)
- § 43a Abs. 2 BRAO — Verschwiegenheit als berufsrechtlicher Schutzmechanismus
- § 203 StGB — Berufsgeheimnis

## Triage zu Beginn
1. Welche Mandats- oder Unternehmensdaten sind als Geschaeftsgeheimnis einzustufen?
2. Wurden angemessene Geheimhaltungsmassnahmen nach § 2 Nr. 1 GeschGehG ergriffen?
3. Erlaubt der KI-Anbieter Training auf Eingabedaten — droht Verlust des Geheimnisschutzes?
4. Gibt es einen Geheimhaltungsvertrag mit dem KI-Anbieter (NDA / AVV mit Vertraulichkeitsklausel)?
5. Wurden Mitarbeiter auf die GeschGehG-Pflichten im KI-Kontext hingewiesen?

## Output-Template — GeschGehG-Baustein fuer KI-Richtlinie
**Adressat:** Kanzlei-Mitarbeiter / Rechtsabteilung — Tonfall: verbindlich, schutzbewusst
```
GESCHAEFTSGEHEIMNIS-BAUSTEIN (GeschGehG)
Fuer: KI-Nutzungsrichtlinie [KANZLEI] — Stand: [DATUM]

§ [X] SCHUTZ VON GESCHAEFTSGEHEIMNISSEN BEIM KI-EINSATZ

(1) Mandatsdaten, Strategieunterlagen und sonstige Informationen, die dem GeschGehG
oder der anwaltlichen Verschwiegenheit unterfallen, duerfen nur in KI-Systeme
eingegeben werden, die eine Verarbeitung ohne Training auf Eingaben gewährleisten
(§ 2 Nr. 1 GeschGehG i.V.m. § 43a Abs. 2 BRAO).

(2) Vor Eingabe ist zu pruefen: Erlaubt der KI-Anbieter Training auf die Daten?
Kann durch die Eingabe der Geheimnischarakter verloren gehen?

(3) Mit jedem KI-Anbieter muss ein Vertraulichkeitsvertrag oder AVV nach Art. 28 DSGVO
abgeschlossen sein, der die Nutzung zur Modellverbesserung ausschliess.

(4) Verletzungen sind sofort dem Compliance-Officer zu melden: [KONTAKT]
```

## 2. `halluzinations-handhabung`

**Fokus:** Halluzinationen von KI in juristischer Arbeit erkennen und Prozessbetrug vermeiden: Anwendungsfall Anwalt nutzt KI für Rechtsprechungs-Recherche und muss sicherstellen dass keine falschen Fundstellen in Schriftsatz oder Gutachten einfliessen. OLG Koblenz Haftung Halluzination, AG Köln 02.07.2025, § 43 BRAO Sorgfaltspflicht. Prüfraster Pflicht zur Quellenverifizierung jedes KI-Zitats, Vier-Augen-Prinzip für Schriftsaetze, Dokumentation der Prüfung. Output Prüfprotokoll-Vorlage für KI-Zitate mit Verifikations-Checkliste. Abgrenzung zu Prompting-Leitfaden und zu Compliance-Regelsatz.

# Halluzinations-Handhabung

Das sogenannte "Halluzinieren" von KI-Systemen — die Erzeugung von nicht existierenden, aber plausibel wirkenden Zitaten, Gerichtsentscheidungen und Fundstellen — ist das größte praktische Haftungsrisiko beim Einsatz von KI-Systemen in der anwaltlichen Arbeit. Die eiserne Regel lautet: Jede einzelne Fundstelle aus einem KI-System ist ausnahmslos zu verifizieren.

## Rechtlicher Hintergrund

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Quellenprüfung als Standard-Schritt**: In den Arbeitsablauf für jeden Schriftsatz und jede Beratung als festen Schritt integrieren: Jedes KI-generierte Zitat wird vor der Verwendung in der Originalquelle nachgeschlagen.
2. **Primärquellen nutzen**: Gerichtsentscheidungen aus offiziellen Portalen (z.B. openjur, Bundesgerichtshof-Website, ECLI-Suche), Gesetze aus dem Bundesgesetzblatt oder gesetze-im-internet.de.
3. **Dokumentation der Prüfung**: Im Arbeitsvermerk oder in der Akte festhalten, welche Fundstellen KI-generiert waren und wie die Verifikation erfolgte (Prüfer, Datum, Quelle).
4. **Vier-Augen-Prinzip bei kritischen Schriftsätzen**: Schriftsätze, die auf KI-generierte Fundstellen gestützt werden, sollten von einer zweiten Person vor Einreichung geprüft werden.
5. **Schulung zu Halluzinationsmustern**: Mitarbeitende müssen typische Muster erkennen lernen: besonders eloquente Formulierungen, genaue Randnummernangaben, unbekannte Senate oder Spruchkörper können Warnsignale sein.
6. **Konsequenz bei Auffinden einer Halluzination**: Gesamtes KI-generiertes Dokument erneut vollständig prüfen; keine selektive Verifikation.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Halluzinations-Pruefprotokoll fuer KI-Output erstellen | Pruefprotokoll nach Schema; Template unten |
| Variante A — Halluzination in bereits versandtem Dokument | Fehlerkorrektur-Protokoll; Mandant sofort informieren |
| Variante B — Pruefung nicht moeglich keine Originalquellen | Quellenangaben-Luecke dokumentieren; Vorbehalt in Dokument |
| Variante C — Routinemaessige Qualitaetssicherung kein Einzelfall | Systematisches Pruefverfahren einrichten; Checkliste standardisieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Baustein Quellenprüfungspflicht:**
Alle von KI-Systemen generierten Fundstellen, Zitate, Gesetzesangaben und Rechtsprechungshinweise sind vor ihrer Verwendung in Schriftsätzen, Gutachten oder Beratungsunterlagen ausnahmslos anhand der Originalquelle zu verifizieren. KI-Systeme können Fundstellen erfinden, die nicht existieren. Ein Unterlassen der Prüfung stellt eine Verletzung der anwaltlichen Sorgfaltspflicht nach § 43 BRAO dar und kann Haftungsansprüche des Mandanten begründen.

**Baustein Vier-Augen-Prinzip:**
Schriftsätze, die unter wesentlicher Mitwirkung von KI-Systemen erstellt wurden, sind vor Einreichung bei Gericht oder Weitersendung an Mandanten von einer zweiten Person inhaltlich zu überprüfen. Dabei ist besonderes Augenmerk auf die Korrektheit aller Zitate und Fundstellen zu legen.

**Baustein Dokumentationsprotokoll:**
Für jeden Schriftsatz oder jede Beratungsunterlage, bei der KI-Systeme wesentlich mitgewirkt haben, wird ein Prüfprotokoll angelegt mit folgenden Angaben: Datum der Prüfung, Name der prüfenden Person, geprüfte Fundstellen und Verifikationsquelle, Ergebnis der Prüfung.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Gerichtliche Entscheidungen zum Umgang mit KI-generierten Fundstellen (insbesondere Entscheidungen zum Prozessbetrug oder zur anwaltlichen Haftung) sind laufend zu beobachten und in die Schulungsunterlagen aufzunehmen. BRAK und DAV werden ihre Stellungnahmen weiterentwickeln.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43 BRAO — Gewissenhafte Berufsausuebung (Sorgfaltspflicht)
- § 263 StGB — Prozessbetrug bei wissentlich falschen Angaben
- § 138 ZPO — Wahrheitspflicht der Parteien
- § 280 BGB — Schadensersatz bei Verletzung anwaltlicher Sorgfaltspflichten
- Art. 5 Abs. 1 lit. d DSGVO — Richtigkeit der verarbeiteten Informationen

## Triage zu Beginn
1. Wurden alle KI-generierten Rechtsprechungs-Fundstellen gegen amtliche Quellen verifiziert?
2. Ist ein Vier-Augen-Pruefungsprozess fuer Schriftsaetze mit KI-Inhalten etabliert?
3. Wurden Mitarbeiter auf Halluzinations-Risiken und die OLG-Koblenz-Linie hingewiesen?
4. Gibt es ein Protokoll-System zur Dokumentation der Pruefvorgaenge?
5. Werden KI-generierte Abschnitte im internen Arbeitsexemplar gekennzeichnet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Halluzinations-Pruefprotokoll
**Adressat:** Kanzlei intern — Tonfall: strukturiert, dokumentierend
```
HALLUZINATIONS-PRUEFPROTOKOLL
[DATUM] — [AKTENZEICHEN] — Sachbearbeiter: [NAME]

Schriftsatz: [BEZEICHNUNG] — Datum: [DATUM]

KI-generierte Abschnitte:
1. [ABSCHNITT / FUNDSTELLE — KI-Behauptung: BESCHREIBUNG]
 Verifiziert gegen: [QUELLE: juris / Beckonline / EUR-Lex / amtliche Sammlung]
 Ergebnis: [KORREKT / FEHLERHAFT — Korrektur: BESCHREIBUNG / NICHT GEFUNDEN — GESTRICHEN]

2. [WEITERE ABSCHNITTE analog]

Vier-Augen-Pruefung:
Geprueft von: [ZWEITE PERSON]
Datum: [DATUM]
Freigabe fuer Versand: [JA / NEIN — Korrekturbedarf: BESCHREIBUNG]
```

## 3. `kanzlei-kontext-analyse`

**Fokus:** Kanzlei-Kontext erfassen für massgeschneiderte KI-Nutzungsrichtlinie: Anwendungsfall vor Erstellung einer KI-Richtlinie muss Groesse Rechtsgebiete Mandantenstruktur IT-Infrastruktur und Syndikus-Inhouse-Besonderheiten des Mandanten analysiert werden. § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz, DSGVO Datenschutzbeauftragter. Prüfraster Kanzleigroesse, Rechtsgebiete mit Hochrisiko-Potential, internationale Mandate, bestehende Tools, Tailoring-Bedarf. Output Kanzlei-Kontext-Profil als Grundlage für Richtlinien-Erstellung. Abgrenzung zu Richtlinien-Skelett-Erzeugen und zu Compliance-Regelsatz.

# Kanzlei-Kontext-Analyse

Bevor eine KI-Nutzungsrichtlinie erstellt oder angepasst wird, muss der konkrete Kanzlei-Kontext systematisch erfasst werden. Größe, Rechtsgebiete, Mandantenstruktur und vorhandene IT-Infrastruktur bestimmen maßgeblich, welche Anforderungen an Datenschutz, Berufsrecht und Compliance gelten und wie streng die Richtlinie ausgestaltet sein muss.

## Rechtlicher Hintergrund

Die DSGVO verpflichtet Verantwortliche nach Art. 5 Abs. 2 DSGVO zur Rechenschaft über die Einhaltung ihrer Pflichten. § 43 BRAO verpflichtet zur gewissenhaften Berufsausübung, was eine angemessene organisatorische Ausstattung einschließt. Art. 4 KI-VO verlangt kontextspezifische KI-Kompetenz, also auf das konkrete Einsatzszenario zugeschnittene Kenntnisse. Für Syndikus-Anwälte gelten zusätzlich §§ 46 ff. BRAO mit besonderen Verschwiegenheitsregelungen gegenüber dem Arbeitgeber.

## Vorgehen

1. **Organisationsstruktur erfassen**: Anzahl der Berufsträger (Anwälte, Syndici, Referendare), Anzahl und Art der nicht-anwaltlichen Mitarbeitenden, Standorte (national/international).
2. **Rechtsgebiete identifizieren**: Welche Bereiche werden bearbeitet (Arbeitsrecht, Strafrecht, Datenschutzrecht, M&A, Familienrecht)? Manche Bereiche (z.B. Strafrecht, Familienrecht) erfordern besonders strenge Anonymisierungspflichten.
3. **Mandantenstruktur analysieren**: Privatpersonen vs. Unternehmensmandate; grenzüberschreitende Mandate (Drittlandtransfer-Risiko); Mandate mit sensiblen Daten nach Art. 9 DSGVO.
4. **IT-Infrastruktur inventarisieren**: Welche KI-Dienstleister werden bereits genutzt oder geplant? Bestehen Auftragsverarbeitungsverträge (AVV)? Welche Cloud-Dienste laufen bereits?
5. **Berufsrechtliche Besonderheiten klären**: Sind Syndikus-Anwälte beteiligt (§§ 46 ff. BRAO)? Gibt es einen Datenschutzbeauftragten oder Berufsrechtsbeauftragten (§ 31 BORA)?
6. **Risikoexposition bewerten**: Aus den erfassten Informationen ergibt sich das Richtlinien-Profil: Kleinkanzlei mit wenigen Mandaten benötigt eine schlanke Richtlinie; Großkanzlei mit internationalen Mandaten benötigt umfassende Regelwerke inklusive Drittland-Transfer-Regelungen.

## Vorlagentext / Bausteine

**Checkliste Kanzlei-Kontext (Musterfragen):**

- Wie viele zugelassene Rechtsanwältinnen und Rechtsanwälte sind in der Kanzlei tätig?
- Gibt es Syndikus-Anwältinnen oder -Anwälte nach §§ 46 ff. BRAO?
- In welchen Rechtsgebieten ist die Kanzlei schwerpunktmäßig tätig?
- Werden Mandate mit besonders sensiblen personenbezogenen Daten bearbeitet (z.B. Strafrecht, Familienrecht, Gesundheitsrecht)?
- Gibt es internationale Mandate, bei denen Daten in Drittstaaten übermittelt werden könnten?
- Welche KI-Dienste oder Chatbots werden bereits genutzt (ggf. auch informell/"Schatten-KI")?
- Existiert ein Datenschutzbeauftragter? Ist dieser intern oder extern bestellt?
- Existiert ein Berufsrechtsbeauftragter nach § 31 BORA?
- Welche bestehenden IT-Sicherheitsrichtlinien oder Compliance-Dokumente gibt es?
- Sind Mitarbeitende bereits im Umgang mit KI-Systemen geschult worden?

## Hinweise zur Aktualisierung

Die Kontextanalyse sollte bei wesentlichen Änderungen der Kanzleistruktur (Fusion, neue Rechtsgebiete, neue Standorte) erneut durchgeführt werden. Mindestens einmal jährlich ist zu überprüfen, ob sich die IT-Infrastruktur oder die genutzten KI-Dienstleister verändert haben, was eine Anpassung der Richtlinie erforderlich machen kann.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a Abs. 2 BRAO — Verschwiegenheit (kanzleigroessen-unabhaengig)
- § 43e BRAO — IT-Dienstleister-Regelung
- § 45 BRAO — Interessenkonflikt-Verbot
- Art. 28 DSGVO — AVV-Pflicht fuer alle Kanzleigroessen
- § 26 BDSG — Beschaeftigtendatenschutz (bei Mitarbeiter-KI)

## Triage zu Beginn
1. Wie gross ist die Kanzlei — Einzelanwalt, Boutique (2-10 RA), Mittelgross (11-50), Gross (50+)?
2. Welche Rechtsgebiete werden betrieben — IT-Recht, Datenschutz, Strafrecht, Familienrecht?
3. Gibt es Inhouse-/Syndikus-Anwaelte — gelten andere Compliance-Anforderungen?
4. Sind internationale Mandate vorhanden — welche Drittland-Jurisdiktionen?
5. Welche IT-Dienstleister werden bereits eingesetzt — ist deren KI-Konformitaet bekannt?

## Output-Template — Kanzlei-Kontext-Analyse
**Adressat:** Richtlinien-Verantwortlicher — Tonfall: strukturiert, analysierend
```
KANZLEI-KONTEXT-ANALYSE
[DATUM] — Kanzlei: [NAME MANDANT]

KANZLEI-PROFIL:
Groe: [Einzelanwalt / Boutique / Mittelgross / Gross]
Rechtsgebiete: [LISTE]
Syndikus/Inhouse: [JA — Besonderheiten: / NEIN]
Internationale Mandate: [JA — Jurisdiktionen: / NEIN]

RISIKOPROFIL:
Mandatsvolumen KI-relevant: [HOCH / MITTEL / NIEDRIG]
Besonders sensible Rechtsgebiete: [STRAFRECHT / FAMILIENRECHT / MEDIZIN / ...]
Datenschutz-Risikoniveau: [HOCH / MITTEL / NIEDRIG]

BESTEHENDE IT-DIENSTLEISTER:
| Dienstleister | Zweck | DSGVO-konform | KI-faehig |
|---|---|---|---|
| [ANBIETER] | [ZWECK] | [JA/NEIN] | [JA/NEIN] |

TAILORING-ANFORDERUNGEN:
- [SPEZIFISCHE ANFORDERUNG aufgrund Kontext]
- [SPEZIFISCHE ANFORDERUNG aufgrund Kontext]

Erstellt: [NAME], [DATUM]
```
