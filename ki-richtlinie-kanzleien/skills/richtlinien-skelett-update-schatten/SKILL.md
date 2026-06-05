---
name: richtlinien-skelett-update-schatten
description: "Richtlinien Skelett Update Schatten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richtlinien Skelett Update Schatten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Richtlinien Skelett Update Schatten** im Plugin KI-Richtlinie für Kanzleien. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `richtlinien-skelett-erzeugen` | KI-Nutzungsrichtlinie Skelett für Kanzleien erzeugen: Anwendungsfall Kanzlei will erstmals KI-Nutzungsrichtlinie erstellen und benoetigt vollständige Grundstruktur. § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz, Art. 28 DSGVO AVV. Prüfraster alle Pflichtbausteine Anwendungsbereich Erlaubtes Verbotenes Dienstleisterpflichten Datenschutz Berufsrecht Sanktionen. Output Richtlinien-Skelett mit Kapiteln und Platzhaltern anpassbar an Kanzlei-Groesse. Abgrenzung zu Executive-Summary-Bausteine für Kurzfassung und zu Compliance-Regelsatz. |
| `richtlinien-update-zyklus` | KI-Nutzungsrichtlinie regelmäßig prüfen und aktualisieren: Anwendungsfall bestehende KI-Richtlinie ist aelter als sechs Monate oder es gibt wesentliche neue Rechtsentwicklung. Art. 4 KI-VO KI-Kompetenz, KI-VO Durchführungsrechtsakte, neue BRAK- und DAV-Stellungnahmen. Prüfraster Prüfintervall alle sechs Monate, Triggerliste neue Rechtsprechung BRAK-Stellungnahmen KI-VO-Akte relevante Gerichtsentscheidungen. Output Richtlinien-Update-Protokoll mit Aenderungslog und naechstem Prüftermin. Abgrenzung zu Richtlinien-Skelett für Neuerstellung und zu Literatur-und-Quellen. |
| `schatten-ki-aufdeckung` | Schatten-KI in Kanzleien erkennen und konstruktiv umgehen: Anwendungsfall Kanzleiführung vermutet oder stellt fest dass Mitarbeitende nicht autorisierte KI-Dienste mit privaten Accounts nutzen. § 43a BRAO Verschwiegenheit, DSGVO Datenschutzverletzung, § 203 StGB Berufsgeheimnis. Prüfraster Stilanalyse von Arbeitsergebnissen, Browser-Logs, freiwillige Selbstauskunft, vertrauliche Anlaufstelle, konstruktiver Umgang. Output Aufdeckungs- und Praeventionstrategie mit Kommunikationsplan. Abgrenzung zu Compliance-Regelsatz und zu Richtlinien-Skelett. |

## Arbeitsweg

Im Plugin KI-Richtlinie für Kanzleien gilt für **Richtlinien Skelett Update Schatten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `richtlinien-skelett-erzeugen`

**Fokus:** KI-Nutzungsrichtlinie Skelett für Kanzleien erzeugen: Anwendungsfall Kanzlei will erstmals KI-Nutzungsrichtlinie erstellen und benoetigt vollständige Grundstruktur. § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz, Art. 28 DSGVO AVV. Prüfraster alle Pflichtbausteine Anwendungsbereich Erlaubtes Verbotenes Dienstleisterpflichten Datenschutz Berufsrecht Sanktionen. Output Richtlinien-Skelett mit Kapiteln und Platzhaltern anpassbar an Kanzlei-Groesse. Abgrenzung zu Executive-Summary-Bausteine für Kurzfassung und zu Compliance-Regelsatz.

# Richtlinien-Skelett erzeugen

Dieses Skill erzeugt das vollständige Grundgerüst einer KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen. Das Skelett folgt einer 13-Kapitel-Struktur, die alle wesentlichen rechtlichen, organisatorischen und praktischen Aspekte abdeckt und als Ausgangspunkt für die Individualisierung dient.

## Rechtlicher Hintergrund

Eine vollständige KI-Nutzungsrichtlinie muss die relevanten Rechtsquellen kohärent abbilden: Die DSGVO (Art. 5, 6, 9, 28) zum Datenschutz, die BRAO (§§ 43, 43a, 43e) und BORA (§ 2) zum Berufsrecht, das UrhG (§ 2 Abs. 2, § 5) zum Urheberrecht, das GeschGehG zum Geheimnisschutz sowie die KI-VO (Art. 3, 4, 6, 50, Anhang III) zur Regulierung von KI-Systemen. Die BRAK-Hinweise vom Dezember 2024 und die DAV-Stellungnahme Nr. 32/2025 geben den Stand der berufsrechtlichen Diskussion wieder.

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Kanzlei-Kontext abfragen**: Ergebnis des Skills `kanzlei-kontext-analyse` als Grundlage nutzen.
2. **13 Kapitel anlegen**: Alle Kapitel mit Überschrift und Kurzbeschreibung vorstrukturieren.
3. **Kapitel priorisieren**: Je nach Kanzlei-Profil einzelne Kapitel ausführlicher oder schlanker gestalten (z.B. Drittland-Transfer nur bei internationalen Mandaten relevant).
4. **Prompting-Anlage anhängen**: Vier-Elemente-Methode als Anhang immer beifügen.
5. **Platzhalter einbauen**: Für kanzleispezifische Angaben (Name, DSB, Ansprechpartner, Datum) Platzhalter "[...]" verwenden.
6. **Versionierung einrichten**: Stand-Datum und Versions-Nummer im Dokumentkopf festhalten.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — KI-Nutzungsrichtlinie Skelett fuer Kanzlei erstellen | Skelett nach Schema; Template unten |
| Variante A — Kanzlei will nur Kernregeln kein langes Dokument | Kurzrichtlinie 2 bis 3 Seiten statt Vollskelett |
| Variante B — Richtlinie ist Teil groesserer Kanzlei-Policy | Modul-Richtlinie als Teil des Gesamtpolicys |
| Variante C — Richtlinie nur fuer bestimmten Fachbereich | Fachbereich-spezifisches Skelett; nicht kanzleiweite Geltung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Standardgliederung KI-Nutzungsrichtlinie:**

```
Richtlinie zur Nutzung von KI-Systemen in [Name der Kanzlei/Rechtsabteilung]
Stand: [Monat/Jahr] | Version [X.X]
Verantwortlich: [Name Geschäftsführung/Partnerkreis]

1. KI im Einsatz – worum geht es?
2. Executive Summary (6 Eckpunkte)
3. Potenziale und Einsatzmöglichkeiten
4. Rechtlicher Begriff des KI-Systems (Art. 3 Nr. 1 KI-VO, OECD-Definition)
5. Rechtliche Rahmenbedingungen (DSGVO, BRAO, UrhG, GeschGehG)
6. Generelle Handlungsempfehlungen
 6.1 Datenschutz (DSGVO)
 6.2 Berufsrecht (BRAO/BORA/StGB)
 6.3 Urheberrecht (UrhG)
 6.4 Geheimnisschutz (GeschGehG)
 6.5 Technisch-vertragliche Absicherung
 6.6 Ausländische Dienstleister (§ 43e Abs. 4 BRAO)
7. Spezifische Vorgaben
 7.1 Schatten-KI
 7.2 Compliance-Regelsatz
 7.3 Organisatorische Maßnahmen
8. Exkurs: Rechtsberatung und RDG
9. KI-Kompetenz als Pflicht (Art. 4 KI-VO)
10. Exkurs: KI-Verordnung (KI-VO)
11. Ausblick und Fazit
12. Disclaimer
13. Weiterführende Literatur
Anlage: Prompting-Leitfaden
Anlage: Musterklauseln § 43e BRAO
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Das Skelett ist bei wesentlichen Rechtsänderungen (neue KI-VO-Durchführungsrechtsakte, neue BRAK-Hinweise, neue BAG- oder OLG-Entscheidungen) anzupassen. Der Skill `richtlinien-update-zyklus` legt das Prüfintervall fest.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 4 KI-VO — KI-Kompetenzverpflichtung als Richtlinien-Anforderung
- Art. 26/29 KI-VO — Betreiberpflichten in Richtlinie operationalisieren
- Art. 22 DSGVO — Automatisierte Entscheidungen
- § 43a Abs. 2 BRAO — Verschwiegenheits-Abschnitt
- § 87 Abs. 1 Nr. 6 BetrVG — Betriebsrats-Beteiligungserfordernis

## Triage zu Beginn
1. Welche Kanzleigroesse und Rechtsgebiete — bestimmt Umfang des Skeletts?
2. Ist ein Betriebsrat vorhanden — muss Skelett Mitbestimmungsabschnitt enthalten?
3. Welche KI-Systeme sollen durch die Richtlinie abgedeckt werden?
4. Gibt es bereits Teilregelungen — ist das Skelett Ersterfassung oder Konsolidierung?
5. Wer genehmigt die fertige Richtlinie — Partnerkreis, GF, Betriebsrat?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Richtlinien-Skelett KI-Nutzung
**Adressat:** Richtlinien-Verantwortlicher — Tonfall: strukturiert, modular
```
RICHTLINIEN-SKELETT KI-NUTZUNG
[KANZLEI] — Entwurf — Stand: [DATUM]
VOR EINSATZ ANWALTLICHE PRUEFUNG UND BETRIEBSRATSEINBINDUNG ERFORDERLICH

I. VORBEMERKUNG UND GELTUNGSBEREICH
 § 1 Zweck und Geltung
 § 2 Begriffsbestimmungen (KI-System, Anbieter, Betreiber)

II. ERLAUBTE UND VERBOTENE KI-NUTZUNG
 § 3 Freigegebene KI-Systeme (Freigabeliste)
 § 4 Verbotene Praktiken (Art. 5 KI-VO)
 § 5 Hochrisiko-KI (Anhang III KI-VO)

III. DATENSCHUTZ UND BERUFSRECHT
 § 6 Anonymisierungspflicht
 § 7 Auftragsverarbeitungsvertrag (Art. 28 DSGVO)
 § 8 Verschwiegenheit (§ 43a Abs. 2 BRAO / § 203 StGB)
 § 9 GeschGehG-Schutz

IV. QUALITAETSSICHERUNG
 § 10 Menschliche Pruefung und Vier-Augen-Prinzip
 § 11 Halluzinations-Pruefung und Quellenverifizierung
 § 12 Dokumentationspflichten

V. SCHULUNG UND KOMPETENZ
 § 13 KI-Schulungspflicht (Art. 4 KI-VO)
 § 14 Fortbildungspflicht Fachanwaelte

VI. GOVERNANCE UND VERANTWORTUNG
 § 15 KI-Beauftragter
 § 16 Meldepflichten bei Sicherheitsvorfaellen
 § 17 Betriebsratsrechte (§ 87 Abs. 1 Nr. 6 BetrVG)
 § 18 Aenderung und Aktualisierung der Richtlinie

Genehmigt von: [UNTERSCHRIFT], [DATUM]
```

## 2. `richtlinien-update-zyklus`

**Fokus:** KI-Nutzungsrichtlinie regelmäßig prüfen und aktualisieren: Anwendungsfall bestehende KI-Richtlinie ist aelter als sechs Monate oder es gibt wesentliche neue Rechtsentwicklung. Art. 4 KI-VO KI-Kompetenz, KI-VO Durchführungsrechtsakte, neue BRAK- und DAV-Stellungnahmen. Prüfraster Prüfintervall alle sechs Monate, Triggerliste neue Rechtsprechung BRAK-Stellungnahmen KI-VO-Akte relevante Gerichtsentscheidungen. Output Richtlinien-Update-Protokoll mit Aenderungslog und naechstem Prüftermin. Abgrenzung zu Richtlinien-Skelett für Neuerstellung und zu Literatur-und-Quellen.

# Richtlinien-Update-Zyklus

Eine KI-Nutzungsrichtlinie ist kein statisches Dokument. Die KI-Technologie entwickelt sich in einem Tempo, das berufsrechtliche und datenschutzrechtliche Einschätzungen rasch überholen kann. Gleichzeitig entstehen neue Regulierungsebenen (KI-VO-Durchführungsrechtsakte, nationale Umsetzungsgesetze) und neue Gerichtsentscheidungen. Dieser Skill legt einen strukturierten Update-Zyklus fest, der sicherstellt, dass die Richtlinie stets aktuell bleibt.

## Rechtlicher Hintergrund

Art. 4 KI-VO: KI-Kompetenz muss auf dem aktuellen Stand gehalten werden — was eine aktuelle Richtlinie voraussetzt. Art. 5 Abs. 2 DSGVO: Rechenschaftspflicht erfordert, dass die getroffenen Maßnahmen dem aktuellen Stand entsprechen. § 43 BRAO: Gewissenhaftigkeit umfasst die laufende Anpassung der Kanzlei-Compliance an neue Rechtsentwicklungen. BRAK-Hinweise 12/2024 und DAV-Stellungnahme 32/2025 werden fortgeschrieben. Die KI-VO wird durch Durchführungsrechtsakte und Leitlinien des EU-KI-Büros konkretisiert (Art. 113 KI-VO enthält den Inkrafttreten-Stufenplan).

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Reguläres Halbjahres-Review**: Alle sechs Monate überprüfen, ob neue Entwicklungen (neue Rechtsprechung, neue BRAK/DAV-Stellungnahmen, neue KI-VO-Akte) eine Anpassung erfordern.
2. **Event-getriggerte Updates**: Bei bestimmten Ereignissen (Trigger-Liste) wird die Richtlinie unmittelbar angepasst, ohne das nächste reguläre Review abzuwarten.
3. **Verantwortliche Person benennen**: Eine Person (z.B. Datenschutzbeauftragter, Berufsrechtsbeauftragter oder Partnerkreis-Mitglied) ist für den Update-Zyklus verantwortlich.
4. **Änderungshistorie führen**: Jede Version der Richtlinie mit Datum, geändertem Inhalt und Grund der Änderung dokumentieren.
5. **Kommunikation bei Updates**: Alle Mitarbeitenden über wesentliche Änderungen informieren; bei grundlegenden Änderungen erneute Schulung durchführen.
6. **Inkrafttretungs-Übersicht KI-VO**: Zeitplan für relevante KI-VO-Bestimmungen im Blick behalten (z.B. Hochrisiko-Personalwesen: 2. August 2026).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Update-Zyklus-Protokoll fuer KI-Richtlinie erstellen | Update-Protokoll nach Schema; Template unten |
| Variante A — Richtlinie noch sehr neu kein Update noetig | Minimal-Protokoll; Update-Trigger definieren |
| Variante B — Update bereits faellig Aenderungen schon identifiziert | Delta-Update durchfuehren; Protokoll rueckwirkend anlegen |
| Variante C — Automatisierter Update-Trigger per Monitoring | Automatisierungs-Protokoll statt manueller Zyklusfestlegung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Trigger-Liste für sofortigen Richtlinien-Update:**

☐ Neue BRAK-Hinweise oder DAV-Stellungnahmen zum KI-Einsatz in der Anwaltschaft
☐ Neue BGH- oder OLG-Entscheidungen zur Haftung bei KI-Nutzung in anwaltlichen Schriftsätzen
☐ Neue KI-VO-Durchführungsrechtsakte oder Leitlinien des EU-KI-Büros
☐ Wesentliche EuGH-Entscheidungen zum Datenschutz im KI-Kontext
☐ Neue Entscheidungen von Datenschutzbehörden zu konkreten KI-Anbietern (z.B. Untersagungen)
☐ Änderung der genutzten KI-Dienstleister (neue AVV und § 43e-Vereinbarungen erforderlich)
☐ Wesentliche Änderungen der AGB oder Datenschutzrichtlinien genutzter KI-Anbieter
☐ Neue Gerichtsentscheidungen zum RDG oder AGG im KI-Kontext
☐ Änderungen des EU-US Data Privacy Framework oder Schrems-III-Entscheidung des EuGH
☐ Inkrafttreten neuer KI-VO-Bestimmungen (nächstes Datum: 2. August 2026)

**Baustein Versionshistorie:**

| Version | Stand | Verantwortliche Person | Wesentliche Änderungen |
|---|---|---|---|
| 1.0 | [Monat/Jahr] | [Name] | Erstversion |
| 1.1 | [Monat/Jahr] | [Name] | [Beschreibung] |

**Baustein Kommunikationspflicht:**
Über Änderungen der KI-Nutzungsrichtlinie werden alle Mitarbeitenden innerhalb von zwei Wochen nach dem Update informiert. Bei wesentlichen Änderungen (neue Verbote, neue Pflichten) ist eine Kurzschulung durchzuführen; die Teilnahme ist zu dokumentieren.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Dieser Skill selbst ist Teil des Update-Zyklus: Falls neue EU-Zeitpläne oder Inkrafttreten-Daten für KI-VO-Bestimmungen bekannt werden, ist die Trigger-Liste entsprechend anzupassen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 17 KI-VO — Qualitaetsmanagement-System mit laufender Ueberprueufung (Anbieter)
- Art. 29 KI-VO — Betreiberpflicht zur laufenden Beobachtung und Anpassung
- Art. 5 Abs. 2 DSGVO — Rechenschaftspflicht (Richtlinie muss aktuell sein)
- § 43 BRAO — Fortlaufende Kompetenz als Berufsanforderung

## Triage zu Beginn
1. Wann wurde die Richtlinie zuletzt aktualisiert — ist sie aelter als ein Jahr?
2. Gab es seit letztem Update relevante Rechtsprechung (EuGH SCHUFA-Score, Dun & Bradstreet)?
3. Sind neue KI-Systeme eingefuehrt worden, die noch nicht in der Richtlinie abgedeckt sind?
4. Haben sich regulatorische Anwendungsdaten geaendert (KI-VO Stufenplan bis 2026)?
5. Ist der Betriebsrat bei Richtlinien-Aenderungen neu einzubinden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Update-Zyklus-Protokoll
**Adressat:** KI-Governance-Verantwortlicher — Tonfall: strukturiert, prozessorientiert
```
RICHTLINIEN-UPDATE-ZYKLUS-PROTOKOLL
[KANZLEI] — Richtlinienversion: [VERSION] — Letztes Update: [DATUM]

REGELMAESSIGE REVIEW-TERMINE:
- Quartalsreview: [DATUM] — Verantwortlich: [NAME]
- Jahres-Vollpruefung: [DATUM] — Verantwortlich: [NAME]

ANLASSBEZOGENE UPDATE-TRIGGER:
☑/☐ Neue EuGH / BGH-Rechtsprechung: [DATUM / AZ]
☑/☐ Neue KI-VO Anwendungsphase (Hochrisiko ab 02.08.2026)
☑/☐ Neues KI-System eingefuehrt: [SYSTEMNAME, DATUM]
☑/☐ Datenpanne oder Sicherheitsvorfall

AKTUELLER UPDATE-BEDARF:
| Abschnitt | Aenderungsbedarf | Prioritaet | Verantwortlicher | Frist |
|---|---|---|---|---|
| [ABSCHNITT] | [BESCHREIBUNG] | HOCH/MITTEL | [NAME] | [DATUM] |

BETRIEBSRATS-EINBINDUNG: ☑/☐ Erforderlich — geplant am [DATUM]
FREIGABE NACH UPDATE: [DATUM] durch [NAME]
```

## 3. `schatten-ki-aufdeckung`

**Fokus:** Schatten-KI in Kanzleien erkennen und konstruktiv umgehen: Anwendungsfall Kanzleiführung vermutet oder stellt fest dass Mitarbeitende nicht autorisierte KI-Dienste mit privaten Accounts nutzen. § 43a BRAO Verschwiegenheit, DSGVO Datenschutzverletzung, § 203 StGB Berufsgeheimnis. Prüfraster Stilanalyse von Arbeitsergebnissen, Browser-Logs, freiwillige Selbstauskunft, vertrauliche Anlaufstelle, konstruktiver Umgang. Output Aufdeckungs- und Praeventionstrategie mit Kommunikationsplan. Abgrenzung zu Compliance-Regelsatz und zu Richtlinien-Skelett.

# Schatten-KI Aufdeckung

"Schatten-KI" bezeichnet die heimliche oder geduldete Nutzung nicht autorisierter KI-Systeme und Chatbots durch Mitarbeitende im Kanzleibetrieb — oft mit privaten Accounts und ohne Wissen der Kanzleiführung. Diese Praxis gefährdet Datenschutz, Anwaltsgeheimnis und Compliance erheblich. Dieser Skill beschreibt Methoden zur Erkennung und zum konstruktiven Umgang mit Schatten-KI.

## Rechtlicher Hintergrund

§ 43a Abs. 2 BRAO, § 203 StGB: Jede Übermittlung von Mandatsgeheimnissen an nicht autorisierte externe Dienste kann eine Verletzung der Verschwiegenheitspflicht darstellen — auch wenn der Mitarbeitende dies nicht beabsichtigt. Art. 5 DSGVO: Rechenschaftspflicht des Verantwortlichen — die Kanzlei muss darlegen können, dass Daten rechtmäßig verarbeitet werden. § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmungsrecht des Betriebsrats bei technischer Überwachung von Mitarbeitenden. § 26 BDSG: Zulässigkeit der Verarbeitung von Beschäftigtendaten. Art. 4 KI-VO: Pflicht zur KI-Kompetenz setzt voraus, dass der Einsatz bekannt und geregelt ist.

## Vorgehen

1. **Offene Kommunikation zuerst**: Schatten-KI ist oft ein Zeichen dafür, dass Mitarbeitende ein reales Bedürfnis nach KI-Unterstützung haben. Zunächst im Dialog klären, warum KI-Systeme genutzt werden und welche Aufgaben damit erledigt werden.
2. **Schulung und Sensibilisierung**: Alle Mitarbeitenden über die Risiken der Schatten-KI aufklären (Verschwiegenheitspflicht, Datenschutz, Haftung) und gleichzeitig Alternativen aufzeigen (autorisierte Kanzlei-Accounts).
3. **Stilanalyse**: KI-typische Texteigenschaften (übermäßig formaler Stil, fehlerfreie Grammatik bei sonst fehleranfälligen Mitarbeitenden, wiederkehrende Formulierungen) können Hinweise geben — keine Beweiskraft, aber Anlass für ein Gespräch.
4. **Browser- und Netzwerk-Logs**: Im Rahmen des datenschutzrechtlich und arbeitsrechtlich Zulässigen können Netzwerklogs Zugriffe auf externe KI-Dienste aufdecken. Betriebsrat einbinden; keine verdachtslose Totalüberwachung.
5. **Freiwillige Selbstauskunft und Amnestie**: Mitarbeitende können eingeladen werden, offen zu kommunizieren, welche KI-Tools sie nutzen. Eine Amnestie für vergangene Verstöße gegen nicht existierende Richtlinien schafft Vertrauen.
6. **Vertrauliche Anlaufstelle einrichten**: Einen Ansprechpartner (z.B. Datenschutzbeauftragter oder Berufsrechtsbeauftragter) benennen, an den Mitarbeitende Fragen zur KI-Nutzung ohne Angst vor Konsequenzen richten können.

## Vorlagentext / Bausteine

**Baustein Schatten-KI-Richtlinie:**
Mitarbeitende dürfen für berufliche Tätigkeiten ausschließlich die von der Kanzlei autorisierten KI-Accounts und -Dienste verwenden. Die Nutzung privater Accounts oder nicht autorisierter KI-Dienste für die Bearbeitung von Mandatsangelegenheiten ist untersagt. Verstöße können berufsrechtliche Konsequenzen (Verletzung der Verschwiegenheitspflicht nach § 43a BRAO, § 203 StGB) und arbeitsrechtliche Folgen haben.

**Baustein Meldestelle:**
Für Fragen zum zulässigen Einsatz von KI-Systemen steht [Name Datenschutzbeauftragter/Berufsrechtsbeauftragter] als vertrauliche Anlaufstelle zur Verfügung. Mitarbeitende, die unsicher sind, ob ein KI-Tool im konkreten Fall eingesetzt werden darf, sind ausdrücklich aufgefordert, vorher Rücksprache zu halten.

## Hinweise zur Aktualisierung

Mit zunehmender Verbreitung von KI-Funktionen in alltäglichen Arbeitstools (MS Office, E-Mail-Clients) wird die Abgrenzung zwischen autorisierter und nicht autorisierter KI-Nutzung schwieriger. Die Richtlinie muss angepasst werden, sobald neue KI-Integrationen in bestehende Kanzlei-Software eingeführt werden.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a Abs. 2 BRAO — Verschwiegenheit (gilt auch bei privaten Accounts)
- Art. 5 Abs. 2 DSGVO — Rechenschaftspflicht der Kanzlei
- Art. 28 DSGVO — AVV-Pflicht (Schatten-KI hat keinen AVV)
- § 203 StGB — Berufsgeheimnis (Strafbarkeit bei Weitergabe)
- § 626 BGB — Ausserordentliche Kuendigung bei grobem Verstoss

## Triage zu Beginn
1. Gibt es Hinweise auf nicht freigegebene KI-Tools im Einsatz — Browser-Erweiterungen, private Accounts?
2. Wurden Mitarbeiter ueber Schatten-KI-Risiken und das Privat-Account-Verbot informiert?
3. Gibt es technische Massnahmen zur Unterbindung (URL-Filter, Geraetemanagemement)?
4. Wie wird Schatten-KI-Nutzung erkannt — technisch oder durch Selbstmeldung?
5. Welche arbeitsrechtlichen Konsequenzen drohen bei Verstoss?

## Output-Template — Schatten-KI-Aufdeckungs-Protokoll
**Adressat:** IT-Sicherheit / Compliance — Tonfall: strukturiert, massnahmenorientiert
```
SCHATTEN-KI-AUFDECKUNGS-PROTOKOLL
[DATUM] — Kanzlei: [NAME MANDANT]

ERKANNTE NICHT-FREIGEGEBENE KI-TOOLS:
| Tool | Erkannt durch | Datum | Nutzer (anonym) | Mandatsdaten involviert |
|---|---|---|---|---|
| [TOOL] | [METHODE] | [DATUM] | [ROLLE] | [JA/NEIN/UNBEKANNT] |

MASSNAHMEN:
1. Sofortmassnahme: [BESCHREIBUNG — z.B. Zugang sperren, Nutzer informieren]
2. Datenrisiko-Pruefung: Waren Mandatsdaten betroffen? [JA/NEIN — wenn JA: DSGVO-Pruefung]
3. Nachsorge: [SCHULUNG / AKTENNOTIZ / MITARBEITERGESPRAECH]

DSGVO-MASSNAHMEN (falls Mandatsdaten betroffen):
☑/☐ Datenpanne nach Art. 33 DSGVO pruefbeduerftig
☑/☐ Berufsrechtliche Meldepflicht (§ 43a BRAO) gegeben

PRAEVENTION:
☑/☐ URL-Filter aktualisiert
☑/☐ Mitarbeiterschulung angesetzt

Verantwortlicher: [NAME], [DATUM]
```
