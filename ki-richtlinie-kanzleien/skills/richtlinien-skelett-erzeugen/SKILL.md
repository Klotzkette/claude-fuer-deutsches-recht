---
name: richtlinien-skelett-erzeugen
description: "KI-Nutzungsrichtlinie Skelett für Kanzleien erzeugen: Anwendungsfall Kanzlei will erstmals KI-Nutzungsrichtlinie erstellen und benoetigt vollständige Grundstruktur. § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz, Art. 28 DSGVO AVV. Prüfraster alle Pflichtbausteine Anwendungsbereich Erlaubtes Verbotenes Dienstleisterpflichten Datenschutz Berufsrecht Sanktionen. Output Richtlinien-Skelett mit Kapiteln und Platzhaltern anpassbar an Kanzlei-Groesse. Abgrenzung zu Executive-Summary-Bausteine für Kurzfassung und zu Compliance-Regelsatz."
---

# Richtlinien-Skelett erzeugen

Dieses Skill erzeugt das vollständige Grundgerüst einer KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen. Das Skelett folgt einer 13-Kapitel-Struktur, die alle wesentlichen rechtlichen, organisatorischen und praktischen Aspekte abdeckt und als Ausgangspunkt für die Individualisierung dient.

## Rechtlicher Hintergrund

Eine vollständige KI-Nutzungsrichtlinie muss die relevanten Rechtsquellen kohärent abbilden: Die DSGVO (Art. 5, 6, 9, 28) zum Datenschutz, die BRAO (§§ 43, 43a, 43e) und BORA (§ 2) zum Berufsrecht, das UrhG (§ 2 Abs. 2, § 5) zum Urheberrecht, das GeschGehG zum Geheimnisschutz sowie die KI-VO (Art. 3, 4, 6, 50, Anhang III) zur Regulierung von KI-Systemen. Die BRAK-Hinweise vom Dezember 2024 und die DAV-Stellungnahme Nr. 32/2025 geben den Stand der berufsrechtlichen Diskussion wieder.

## Vorgehen


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

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
